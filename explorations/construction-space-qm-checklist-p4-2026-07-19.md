---
title: "Construction-Space P4 QM Checklist"
status: active_research
doc_type: exploration
created: 2026-07-19
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
probe: P4-QM-CHECKLIST
---

# Construction-Space P4 QM Checklist

P4 converts the existing `QM-PHYSICAL-SECTOR` conditional-fail certificate into
the construction-space map's per-cell QM R0 checklist. It does not construct a
boundary adapter, change claim status, move canon, or make a public-posture
claim.

## Construction Fork

The quantum object is the GU-native Krein/BRST physical-sector construction,
not the standard-physics default "positive Hilbert space by assumption"
construction. The test remains open to either side: a positive Hilbert or
algebraic state may be the right endpoint, but P4 records that the current GU
branch has not derived it. Indefinite Krein control, a selected sign, or a
formal BRST complex is not counted as a physical quantum sector.

## R0 Checklist

For a construction-space cell to clear the QM track at Rung 0, it must supply
all six checklist objects without contradiction:

| check | required object | current C1 status |
|---|---|---|
| Q1 | physical state space via a well-defined quotient | missing source-defined gauge/BRST differential `d_RS,-1` |
| Q2 | observables as operators or effects on that space | missing observable admissibility certificate |
| Q3 | probability rule with positivity and normalization | missing Born/probability certificate and GU-derived state |
| Q4 | locality/causal structure compatible with pairing/order axes | conditional only; no live QFT-shadow microcausality certificate |
| Q5 | unitary or otherwise state-preserving dynamics | missing QFT-level unitarity/state-preservation certificate |
| Q6 | no negative-norm physical states after constraint discharge | not established before Q1-Q5 exist |

For `C1-W229-RECORD-CURRENT`, the typed boundary adapter axiom is one counted
import. The row is therefore `R1_COND`, not native R2. The condition is useful
for P5 because it states exactly what a source object must provide before the
QM leg can be consumed.

## C4 Adapter Interface Type

`C4-BOUNDARY-ADAPTER` remains gated on a frozen p2c packet. The packet must be
a source-owned boundary/firewall adapter interface with provenance independent
of the GU consequence it enables. At minimum it must expose:

- an exact quotient or physical field-complex interface
- a positivity, majorant, or spectral-section interface sufficient to test
  state positivity
- observable-admissibility and probability-rule hooks
- locality or causal-compatibility hooks
- state-preserving dynamics hooks
- explicit branch assumptions and non-retuning conditions

The adapter must not be constructed inside GU, inferred from the desired GU
result, target-retuned, or treated as evidence that quantum recovery has
already happened.

## Handoff

P4 is complete at checklist-conversion strength. Next Lane 1 work is
`P5-SOURCE-OBJECT-SPEC`: derive the frozen source-object interface contract
from the GR, QM, COSMO, and SM sharp lists plus standing lemmas. P6 conditional
interior work follows after the spec. No paper seed is present.
