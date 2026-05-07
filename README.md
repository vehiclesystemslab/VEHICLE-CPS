# VEHICLE-CPS — Civil Protection Systems

**Environmental Safety through Relational Coherence**

VEHICLE-CPS is a civil protection research initiative by **VEHICLE Systems Lab**. It applies the **Borda Milan Pyramid** and the **VEHICLE Formula-as-Architecture** to high-density human events, public safety operations, leader protection, emergency response and controlled crowd coordination.

VEHICLE-CPS models a human environment as a dynamic relational graph. People, authorized teams, smart bands, active credentials, access points, protected zones, evacuation routes, security rings and critical areas are represented as structured nodes under relational tension.

The project is not designed to replace authorities, civil protection agencies, law enforcement or security companies. Its purpose is to support human decision-making by reducing the time required to detect loss of environmental coherence, anomalous crowd concentration, disconnected operational nodes, route pressure and early signals of unsafe escalation.

---

## Core Thesis

A mass event is not only a crowd.  
It is a structured relational field under tension.

VEHICLE-CPS seeks to measure that tension, classify operational regimes and support admissible human response before small anomalies become major incidents.

---

## What VEHICLE-CPS Is

- A civil protection architecture.
- A research framework for environmental safety.
- A simulation model for high-density human events.
- A relational coherence layer for public safety operations.
- A decision-support system under mandatory human supervision.
- An applied instance of the Borda Milan Pyramid.
- A framework for detecting rising pressure, loss of coherence and unsafe environmental configurations.

---

## What VEHICLE-CPS Is Not

- It is not a facial recognition system.
- It is not an autonomous enforcement system.
- It is not a political surveillance tool.
- It is not designed to profile individuals.
- It does not identify attackers.
- It does not assign guilt.
- It does not make coercive decisions automatically.
- It does not replace human verification.
- It does not replace civil authorities, law enforcement, emergency services or security companies.

---

## Architecture

VEHICLE-CPS reuses the VEHICLE relational architecture:

```text
G = (N, E)
```

Each node carries a structured state:

```text
S_i = (E_i, I_i, A_i, R_i, V_i)
```

Total system tension:

```text
T(X) = T_ext(X) + T_int(X)
```

Projected correction:

```text
V_op(S_i) = P_K[S_i - gamma grad_{S_i} T(X)]
```

Relaxed update:

```text
S_i(t+1) = (1-alpha)S_i(t) + alpha V_op(S_i(t))
```

In the civil protection domain:

- **External tension** may represent density, proximity, bottlenecks, perimeter deformation, route pressure or crowd surge.
- **Internal incoherence** may represent disconnected credentials, incompatible location-state relations, loss of signal, abnormal persistence or critical team disconnection.
- **Projection-governed correction** supports safer operational configurations without replacing human judgment.

---

## Borda Milan Pyramid Integration

VEHICLE-CPS is structured through the Borda Milan Pyramid:

1. **Observed domain** — public events, protected areas, stadiums, concerts, emergency drills and critical infrastructure environments.
2. **Relational conversion** — the environment becomes a graph of people, teams, devices, access points, routes, protected zones and critical areas.
3. **Structured VEHICLE node** — each operational unit is represented through E.I.A.R.(V).
4. **Dual tension** — external relational tension and internal incoherence are measured together.
5. **Projection-governed correction** — the system supports admissible operational configurations.
6. **Operational regimes P0–P6** — the environment is classified into civil protection states.
7. **Attractor discovery** — simulation reveals new patterns of crowd pressure, perimeter deformation and recovery.
8. **Decision support** — authorized teams receive structured information for faster verification and coordinated response.

---

## Operational Regimes P0–P6

| Regime | Name | Meaning |
|---|---|---|
| **P0** | Structural Rest | Event not started or space essentially empty |
| **P1** | Controlled Normal Flow | Occupancy and movement remain compatible |
| **P2** | Localized Review | Small anomalies requiring human verification |
| **P3** | Anomalous Concentration | Bottlenecks, density pressure or unexpected crowd formation |
| **P4** | Perimeter Break / Critical Incoherence | Security ring breach, route conflict or critical node incoherence |
| **P5** | Reinforcement & Containment | Response is active and the field is being reconfigured |
| **P6** | Controlled Evacuation | Partial or full evacuation under monitored tension |

---

## Preventive Civil Protection Support

VEHICLE-CPS is designed as a preventive civil protection support architecture for high-density human environments where authorities, organizers and safety teams must respond to rapidly changing conditions.

It can support authorized human teams in situations involving:

- perimeter pressure;
- anomalous concentration;
- route obstruction;
- crowd surge;
- unauthorized access patterns;
- disconnected operational nodes;
- evacuation stress;
- sudden changes in movement flow;
- high-emotion crowd behavior;
- coordination failures between security rings or response teams.

The system does not accuse, profile or identify attackers. It does not replace law enforcement, civil protection agencies or private security companies. It provides a structured decision-support layer that helps authorized human teams observe, verify and respond faster.

---

## Initial Simulation Phase

The first research phase proposes synthetic simulations with:

- 1,000 nodes;
- 5,000 nodes;
- 10,000 nodes.

The objective is to validate computational viability, operational interpretation, ethical boundaries and institutional usefulness before any physical pilot.

Expected outputs include:

- dynamic graph construction;
- external tension maps;
- internal incoherence measurement;
- P0–P6 classification;
- anomaly-detection timing;
- return-to-safe-state dynamics;
- controlled response scenarios;
- reproducible simulation reports.

---

## Example Civil Protection Environments

- Public events.
- Stadiums and concerts.
- Protected areas.
- Emergency drills.
- Critical infrastructure.
- Controlled access environments.
- Evacuation route planning.
- Crowd pressure and perimeter coherence analysis.

---

## Ethics and Governance

VEHICLE-CPS is designed around prevention, not persecution.

Its ethical principles include:

- mandatory human supervision;
- no automatic coercive action;
- data minimization;
- pseudonymized operational IDs;
- no facial recognition by design;
- no political profiling;
- auditability of alerts;
- explicit limitation to civil protection and event safety use cases.

See [`ETHICS.md`](ETHICS.md) for the full ethical scope.

---

## Roadmap

The project roadmap includes:

1. conceptual consolidation;
2. synthetic simulation;
3. operational scenario modeling;
4. partner validation;
5. controlled pilot design under legal and ethical review.

See [`ROADMAP.md`](ROADMAP.md) for details.

---

## Zenodo

**VEHICLE-CPS v1.1** is archived on Zenodo:

https://zenodo.org/records/20046955

---

## Partnership Opportunity

VEHICLE Systems Lab is seeking partners to develop, validate and test VEHICLE-CPS through simulation, controlled pilots and institutional review.

Potential partners include:

- civil protection agencies;
- event security companies;
- municipalities;
- universities;
- emergency management institutions;
- wearable technology providers;
- venue operators;
- public safety researchers.

---

## Current Status

VEHICLE-CPS is currently in conceptual and simulation design phase.

The next milestone is a reproducible simulation package for 1,000–10,000 human nodes, including tension maps, P0–P6 transitions, anomaly detection timing and controlled response scenarios.

---

## Contact

## Contact

**Roberto Borda Milan**  
VEHICLE Systems Lab  
Santa Cruz, Bolivia  

**Website:** https://vehiclesystemslab.com  
**GitHub:** https://github.com/vehiclesystemslab  
**ORCID:** https://orcid.org/0009-0009-9047-1036  
**Zenodo:** https://zenodo.org/records/20046955  
**DOI:** https://doi.org/10.5281/zenodo.20046955  
**Email:** contact@vehiclesystemslab.com
