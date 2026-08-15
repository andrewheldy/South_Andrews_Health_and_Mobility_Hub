Mission

Build a reusable, evidence-based Parking Garage Development & EV Infrastructure Modeling Skill for the South Andrews Health & Mobility Hub project.

This is NOT a one-off spreadsheet exercise.

The end product should be a portable skill that both Claude and other AI agents can use repeatedly throughout development to:

estimate structured-parking construction costs;

compare structural systems and garage configurations;

estimate stalls, gross area, efficiency and floor count;

compare conventional parking construction against EV-ready and fleet-ready construction;

determine the most cost-effective way to future-proof a garage for EV charging;

model phased EV deployment;

quantify the incremental cost of different infrastructure strategies;

evaluate convertibility and long-term adaptability;

update assumptions as contractor, architect, electrical-engineering and utility data becomes available;

generate Excel underwriting models and concise decision memos from the same assumption set.

The skill must distinguish carefully between:

verified project facts;

sourced industry benchmarks;

engineering assumptions;

user-entered assumptions;

calculated outputs;

items requiring professional validation.

Do not create false engineering precision.

Core Design Principle

Separate:

A. Generic reusable knowledge

Parking-garage construction methods, EV infrastructure, cost logic, formulas, design rules, benchmarks and workflows.

from:

B. Project-specific assumptions

The South Andrews site, current building configuration, local costs, electrical requirements, number of parking floors, fleet requirements, tenant mix, etc.

The generic skill should survive if the South Andrews program changes completely.

South Andrews should be implemented as the first project configuration / test case, not hard-coded into the modeling engine.

Phase 1 — Research the Parking Garage Industry

Conduct a serious research sprint before building the model.

Research parking-garage developers, design-build firms, structural engineers, precast suppliers, parking consultants, electrical engineers and major garage projects.

Prioritize:

actual completed-project data;

developer / GC / structural-engineer sources;

parking consultant data;

public procurement documents;

government construction budgets;

RSMeans or equivalent recognized cost data if accessible;

manufacturer technical documentation;

industry associations;

engineering papers.

Use blogs and marketing content only as secondary evidence.

Research South Florida specifically whenever sufficient data exists.

Structural Systems to Compare

At minimum evaluate:

Precast concrete

double tees

precast columns/beams

field connections

erection speed

transportation limitations

hurricane/coastal considerations

architectural screening implications

Cast-in-place concrete

conventionally reinforced

post-tensioned

flat slab / flat plate where applicable

durability

penetrations

flexibility for future MEP

Hybrid systems

precast + cast-in-place

steel/composite structures where relevant

proprietary/modular parking systems where commercially viable

For every system compare:

$/GSF

$/stall

schedule

structural depth

column spacing

clear height

durability

maintenance

waterproofing

corrosion exposure

embodied complexity

EV integration

future penetrations

adaptability

future conversion potential

South Florida applicability

Do NOT assume one system is best.

Establish the Conventional Garage Baseline

Build a cost framework for a normal structured parking garage with no special fleet or advanced EV infrastructure.

Model major divisions separately.

Examples include:

demolition/site preparation

excavation

foundations

piles / deep foundations if required

concrete

structural frame

decks

ramps

stairs

elevators

façade / screening

waterproofing

striping

wheel stops

guardrails

signage

lighting

ventilation if required

fire protection

drainage

stormwater systems

security

access-control equipment

PARCS

elevators

electrical service

plumbing

landscaping / streetscape

general conditions

contractor OH&P

design / engineering

permits

insurance

testing

contingency

escalation

Keep hard costs, soft costs and owner costs distinct.

Critical Research Question — EV Infrastructure

The most important part of this assignment is determining the cheapest intelligent way to make the garage EV-ready without overbuilding it.

Do NOT begin with the assumption that embedding conduit inside every concrete slab is the best solution.

Investigate and compare alternatives.

At minimum:

Strategy 0 — Conventional Garage

No meaningful EV future-proofing beyond code minimum.

Strategy 1 — Embedded Conduit

Raceways / conduits incorporated into slabs or structural pours.

Evaluate:

construction cost

coordination complexity

future accessibility

repairability

structural coordination

post-tension implications

penetration restrictions

future cable replacement

waterproofing

corrosion

change-order exposure

future charger-location flexibility

Strategy 2 — Exposed Surface Conduit

Conduit mounted along ceilings, beams, columns or walls.

Evaluate the same factors.

Strategy 3 — Overhead Cable Tray / Ladder Rack

Centralized overhead distribution with branch drops to charging locations.

Strategy 4 — Busway / Bus Duct

Distributed electrical bus architecture with future tap-off points.

Determine whether this creates meaningful lifecycle or deployment advantages.

Strategy 5 — Electrical Backbone Only

Install during initial construction:

major electrical rooms;

utility service pathway;

risers;

sleeves;

strategically oversized raceways;

distribution zones;

panel locations;

transformer locations;

communications backbone;

while delaying most branch wiring and EVSE.

Strategy 6 — Modular / Distributed Electrical Rooms

Compare decentralized electrical distribution by parking level or charging zone.

Strategy 7 — Combination Strategy

Determine whether the optimal solution is something like:

build the trunk infrastructure now and install accessible distribution later instead of burying hundreds of individual conduits in concrete.

This question must be answered from engineering and lifecycle evidence, not intuition.

EV Charging Architectures

Model separately:

Level 2

Typical fleet / long-dwell charging.

DC fast charging

Higher-capacity charging.

Distributed DC architecture

Centralized power cabinets with remote dispensers if applicable.

Managed charging

Model the effect of:

load management;

scheduled charging;

charging queues;

power sharing;

demand limiting;

fleet departure requirements;

charger utilization;

transformer diversity.

The model must distinguish:

number of parking spaces

from

number of EV-capable spaces

from

number of wired charging ports

from

number of simultaneously energized vehicles

from

maximum coincident electrical demand.

These are not the same variable.

Fleet-Specific Requirements

Create a separate module for fleet parking because conventional public parking assumptions may not apply.

Inputs should include:

fleet vehicles

daily vehicle utilization

dwell time

miles/day

kWh/mile

required SOC at dispatch

charger power

charger count

charge-session duration

charging-window duration

turnover

peak dispatch time

simultaneous charging limit

cleaning/staging stalls

maintenance stalls

disabled vehicles

fleet reserve percentage

Allow the model to determine charging infrastructure from operational requirements rather than simply assigning a charger to every stall.

Autonomous Vehicle Future-Proofing

Evaluate low-cost provisions that could benefit future AV fleet use:

communications

fiber

Wi-Fi/private wireless

positioning infrastructure

cameras

vehicle identification

remote access

controlled fleet zones

cleaning/staging

automated gates

dedicated circulation

future robotic charging

automated valet / parking systems

car elevators where relevant

Do not assign speculative revenue to AV uses.

Treat AV infrastructure as optionality.

Convertible Garage Design

Model the incremental cost of making parking floors more convertible to office, medical or other future uses.

Potential factors:

flatter floor plates

removable ramps

floor-to-floor height

structural grid

live-load capacity

façade adaptability

utility risers

vertical circulation

daylight

future MEP zones

drainage strategy

Quantify:

conventional garage cost

vs.

convertible garage premium

and determine which adaptability provisions provide meaningful option value versus expensive overdesign.

South Andrews First Test Case

Use the existing project files in the repository as the first implementation case.

Treat all current values as provisional unless verified.

Seed assumptions from the project documents, including approximately:

site: 38,207 SF / ±0.88 acres;

Fort Lauderdale, Florida;

FEMA Zone AE;

mixed healthcare + parking + mobility use;

current working concept approximately nine total levels;

one ground-floor medical-retail level;

approximately two office / healthcare-office levels;

approximately six parking levels;

future fleet / EV uses within portions of the garage;

current preliminary structured-parking plate assumption around 28,000 SF;

preliminary efficiency benchmark around 340 GSF/stall;

preliminary output around 82 stalls per parking level.

These figures are TEST INPUTS.

Do not turn them into permanent rules.

Compare them with the research and flag where professional test-fit work is likely to change them.

South Andrews Electrical Context

Integrate the project's existing electrical-load work where relevant.

The skill should eventually be able to read project inputs such as:

base-building electrical load;

medical load;

imaging load;

parking load;

EV charging load;

utility service capacity;

transformer size;

switchgear;

redundancy;

generation;

battery storage;

solar if applicable.

Do not assume FPL capacity.

Utility capacity must remain a separate validation gate.

Required Model Scenarios

Every parking analysis should be able to compare at least:

Scenario A

Conventional parking garage.

Scenario B

Code-minimum EV garage.

Scenario C

Low-cost EV-future-ready garage.

Scenario D

Moderately electrified garage.

Scenario E

Fleet-heavy EV garage.

Scenario F

High-density future fleet / AV infrastructure.

For each show:

base construction cost

EV incremental cost

electrical-service incremental cost

total development cost

$/GSF

$/stall

$/EV-capable stall

$/installed charging port

schedule impact

utility requirement

expandability

retrofit cost

lifecycle implications

major risks

Cost Data Rules

Every external cost assumption must contain:

source

source URL

publication / company

date

project location

project type

units

original cost

normalization method

adjusted Fort Lauderdale cost

low estimate

base estimate

high estimate

confidence level

Never give a single-point cost where the evidence only supports a range.

Every assumption must be timestamped.

Costs should be capable of escalation to a chosen analysis date.

Model Inputs

Create a structured schema covering at least:

Site

land area

buildable area

parking plate

location

flood condition

soil/foundation assumption

Garage

parking levels

GSF per level

structural system

stall efficiency

stall dimensions

ramps

elevators

stairs

clear height

Other Uses

retail

office

medical

amenity

loading

EV

EV-ready stalls

EV-capable stalls

EVSE stalls

charger types

L2 kW

DCFC kW

diversity

managed-load factor

Electrical

service voltage

service capacity

transformer capacity

switchgear

distribution topology

spare capacity

future expansion

Cost

unit costs

labor/location factor

escalation

contingency

GC fee

soft costs

Schedule

design

entitlement

procurement

foundations

structure

MEP

commissioning

Model Outputs

At minimum calculate:

total project GSF

parking GSF

stalls per floor

total stalls

GSF/stall

parking efficiency

hard cost

soft cost

total development cost

$/GSF

$/stall

EV infrastructure cost

incremental EV readiness premium

electrical capacity

kW/stall

peak managed EV demand

charger utilization

retrofit avoidance value

schedule

scenario comparison

sensitivity analysis

Sensitivities

Automatically test:

parking efficiency

number of floors

structural system

concrete cost

labor cost

foundation cost

EV penetration

charging power

managed-load diversity

transformer/service cost

utility contribution

construction escalation

contingency

convertible-garage premium

Use low / base / high cases.

Skill Architecture

Create:

parking-garage-development-model/
├── SKILL.md
├── README.md
├── references/
│   ├── garage-construction-systems.md
│   ├── parking-efficiency.md
│   ├── ev-infrastructure-options.md
│   ├── electrical-distribution.md
│   ├── fleet-charging.md
│   ├── convertible-garages.md
│   ├── south-florida-cost-benchmarks.md
│   └── source-register.md
├── schemas/
│   ├── project-inputs.yaml
│   ├── cost-assumptions.yaml
│   └── scenario-definition.yaml
├── scripts/
│   ├── calculate_garage.py
│   ├── calculate_ev_load.py
│   ├── calculate_cost.py
│   ├── run_sensitivity.py
│   └── validate_inputs.py
├── templates/
│   └── parking-garage-model.xlsx
└── examples/
    └── south-andrews/
        ├── assumptions.yaml
        ├── assumptions.md
        └── example-output.md

Adapt this architecture if you find a clearly better structure.

SKILL.md Requirements

Keep SKILL.md compact.

It should tell an agent:

when the skill should trigger;

which inputs it needs;

how to classify evidence;

which reference file to load for which question;

which deterministic script to run;

how to generate scenarios;

how to flag uncertainty;

when professional engineering validation is required;

how to produce concise outputs.

Heavy reference material should NOT live in SKILL.md.

Use progressive disclosure.

Workbook

Create an institutional-quality Excel workbook driven by the same underlying assumptions.

Suggested tabs:

Executive Summary

Inputs

Program

Parking Geometry

Structural Systems

Base Garage Cost

EV Infrastructure

Electrical Load

Fleet Charging

Development Cost

Scenarios

Sensitivities

Sources

Change Log

Requirements:

no hidden mystery assumptions;

clear input/calculation/output formatting;

formulas rather than pasted answers;

low/base/high cases;

scenario switches;

visible source references;

no hard-coded numbers inside formulas where an input belongs;

error checks;

units on every relevant input.

Research Questions the Final Skill Must Be Able to Answer

Examples:

What does adding another parking floor cost?

What is the cost per incremental stall?

Should this garage be precast or cast-in-place?

How much does making 25%, 50% or 100% of the garage EV-capable add?

Should we embed conduit in the deck or use accessible overhead distribution?

How much money do we save today by installing only backbone infrastructure?

What would retrofitting charging five years later cost?

How many chargers do 200 fleet vehicles actually need?

What electrical capacity does that charging profile require with load management?

How much does a convertible garage cost compared with a conventional garage?

Which design decisions are cheap today but expensive to retrofit later?

Which future-proofing features are actually worth buying?

Evidence Discipline

Maintain three statuses:

VERIFIEDSupported by strong source or project documentation.

ASSUMPTIONReasonable modeling assumption awaiting confirmation.

VALIDATION REQUIREDMust eventually be confirmed by architect, structural engineer, MEP engineer, contractor, utility, parking consultant, civil engineer or other appropriate professional.

Never silently promote an assumption to a fact.

Final Deliverables

At completion provide:

the complete skill directory;

SKILL.md;

research/reference files;

source register;

calculation scripts;

input schemas;

Excel template;

South Andrews example configuration;

sample South Andrews scenario comparison;

list of remaining unknowns;

list of questions we should eventually send to:

parking consultant;

architect;

structural engineer;

electrical engineer;

GC / CM;

FPL;

EV charging vendors.

Before declaring the skill complete, run the South Andrews example through it and audit the calculations for internal consistency.

The objective is not to produce the largest possible research report.

The objective is to build a durable decision engine that becomes more accurate as real project information arrives.
