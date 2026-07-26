#!/usr/bin/env python3
"""Read-only verification of key source-workbook cells and formulas."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}
DOC_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def workbook_cells(path: Path, requests: dict[str, list[str]]):
    with zipfile.ZipFile(path) as archive:
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall("m:si", NS):
                shared.append("".join(node.text or "" for node in item.iterfind(".//m:t", NS)))

        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rels.findall("r:Relationship", REL_NS)
        }
        sheet_paths = {}
        for sheet in workbook.findall("m:sheets/m:sheet", NS):
            target = targets[sheet.attrib[DOC_REL]].lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            sheet_paths[sheet.attrib["name"]] = target

        results = []
        for sheet_name, refs in requests.items():
            xml = ET.fromstring(archive.read(sheet_paths[sheet_name]))
            cells = {cell.attrib["r"]: cell for cell in xml.findall(".//m:c", NS)}
            for ref in refs:
                cell = cells.get(ref)
                if cell is None:
                    results.append((sheet_name, ref, None, None))
                    continue
                formula_node = cell.find("m:f", NS)
                value_node = cell.find("m:v", NS)
                value = value_node.text if value_node is not None else None
                if cell.attrib.get("t") == "s" and value is not None:
                    value = shared[int(value)]
                elif cell.attrib.get("t") == "inlineStr":
                    value = "".join(node.text or "" for node in cell.iterfind(".//m:t", NS))
                formula = formula_node.text if formula_node is not None else None
                results.append((sheet_name, ref, value, formula))
        return results


def refs(columns, start, end):
    return [f"{column}{row}" for row in range(start, end + 1) for column in columns]


workbooks = [
    (
        ROOT / "sources/current/South Andrews 6v8 Story Model.xlsx",
        {
            "Assumptions": ["B18"],
            "Returns": refs(["A", "B", "C"], 13, 17) + refs(["A", "B", "C"], 27, 31),
        },
    ),
    (
        ROOT / "sources/current/South_Andrews_8M_Construction_Feasibility.xlsx",
        {
            "Assumptions": ["D7", "D63", "E63"],
            "Financing & Returns": refs(["A", "B", "C", "D", "E"], 7, 28),
        },
    ),
]

for workbook, request in workbooks:
    print(f"WORKBOOK {workbook.relative_to(ROOT)}")
    for sheet, ref, value, formula in workbook_cells(workbook, request):
        if value is not None or formula is not None:
            formula_display = re.sub(r"\s+", " ", formula or "")
            print(f"{sheet}!{ref}\tvalue={value}\tformula={formula_display}")
