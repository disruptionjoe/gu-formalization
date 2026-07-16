---
artifact_type: exploration
status: exploration
created: 2026-07-16
title: "Recovery contract SM selector screen"
lane: RECOVERY-CERTIFICATION
internal_item: SM-CONSISTENT-SECTOR
operational_result: NO_GO
grade: "branch-local process checkpoint; no claim-status, canon, public-posture, or portfolio movement"
tests:
  - tests/recovery-contract/sm_selector_screen_gate.py
depends_on:
  - lab/process/recovery-contract-action-fingerprint-2026-07-16.json
  - lab/process/recovery-certification-matrix.json
  - explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md
  - explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md
---

# Recovery Contract SM Selector Screen

## Question

Does the frozen W203/W229/W230/W236 record-current action fingerprint supply a
target-free selector for a complete low-energy Standard Model sector, or only a
host/relative branch that contains Standard Model-shaped representation data?

## Construction Fork

This screen uses the GU-native gauge quotient, representation inventory, and
record-current action fingerprint. The Standard Model is used only as the
benchmark for the physical sector properties that recovery would need to derive:
the gauge quotient, hypercharge normalization, chirality, Higgs projection,
surviving spectrum, anomaly status, and decoupling of unwanted modes.

The screen does not replace GU objects with a standard field-theory model, and
it does not treat subgroup containment or a matching field-count table as
recovery.

## Result

Operational result: `NO_GO` for complete Standard Model recovery at this
checkpoint.

What survives:

- the typed GU carrier hosts the Pati-Salam / Spin(10) one-generation branch;
- W222's relative hypercharge and chiral-16 anomaly arithmetic survive as exact
  representation checks;
- the result remains useful host evidence and a positive control for the
  arithmetic layer.

What is missing:

- a target-free selector for `A_F = C + H + M_3(C)`;
- a source-native selector for `SU(3) x SU(2) x U(1) / Z_6`;
- an absolute `U(1)_Y` embedding and normalization selector;
- a built chirality-production mechanism rather than a granted chiral shadow;
- a physical Higgs projection and potential from the GU section/action;
- a theorem that the observer-facing shadow has exactly the ordinary surviving
  spectrum with no extra anomalous modes.

Therefore the current branch does not derive a complete low-energy Standard
Model sector. It hosts a strong relative branch, but recovery requires selector
and physical-sector closure.

## Boundary

No claim status, canon verdict, scientific status, public posture, paper state,
or portfolio state moves from this checkpoint. The daily steward may use the
result as advisory evidence when reconciling the recovery lane.

## Validation

Run:

```powershell
python tests\recovery-contract\sm_selector_screen_gate.py
```

Expected result: all checks pass and the script prints `Operational result:
NO_GO for complete Standard Model recovery at this checkpoint.`
