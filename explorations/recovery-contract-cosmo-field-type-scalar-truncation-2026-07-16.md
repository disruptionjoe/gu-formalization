---
title: "Recovery contract cosmology field-type and scalar-truncation gate"
status: exploration
doc_type: recovery_contract_checkpoint
created: 2026-07-16
run_id: GUH-20260716T101133Z-cosmo-field-type
gate: tests/recovery-contract/cosmo_field_type_scalar_truncation_gate.py
---

# Recovery contract cosmology field-type and scalar-truncation gate

Operational result: `NO_GO` for perturbation-recovery use of the current
theta-background Klein-Gordon object.

The W203/W229/W230/W236 record-current fingerprint is enough to ask the cosmology
field-type question branch-locally. It is not enough to answer it positively. At
the current construction grade, the branch has a typed theta candidate and a
large background/distance evidence chain, but it does not supply:

- a physical FLRW scalar-singlet projector for `s*(theta)`;
- a gauge-invariant observable map;
- a block-diagonal scalar-vector-tensor quadratic action; or
- a closed scalar truncation showing that vector, tensor, connection, and
  non-scalar source residues decouple.

Therefore the existing theta-background KG equation remains background and
distance-model evidence. It cannot be counted as cosmological perturbation
recovery without a new scalar-singlet and truncation certificate.

No claim status, canon verdict, public posture, paper surface, or portfolio
surface changed.

## Construction Fork

The load-bearing construction is the GU-native record-current/source-action
branch fixed by `lab/process/recovery-contract-action-fingerprint-2026-07-16.json`.
Standard FLRW scalar/vector/tensor decomposition is used only as the benchmark
language for perturbations on an imported cosmological background.

The gate does not replace `theta` with an ordinary scalar field. It asks whether
the branch itself derives a physical scalar sector. The answer at this grade is
negative: the canon dark-energy file explicitly treats scalar field type as an
assumption/failure mode, and the fingerprint leaves the physical gauge quotient,
observable map, boundary/initial data, and source-action residues unfrozen.

## Result

The recovery matrix's first decisive cosmology test is:

```text
Decompose s*(theta) under FLRW spatial rotations and determine whether a physical
scalar singlet exists and can form a consistent truncation of the frozen action.
```

The current branch fails the positive side of that test. This is a checkpoint
`NO_GO`, scoped to perturbation-recovery use. It is not a dark-energy verdict
change. The earlier H44/H46C/W129 background and raw-distance results keep their
previous scope: useful background/distance evidence, not a derived SVT
perturbation sector.

## Validation Role

`tests/recovery-contract/cosmo_field_type_scalar_truncation_gate.py` checks that:

- a toy fully closed scalar sector would pass the gate;
- a scalar-looking background model with vector/tensor or gauge mixing fails;
- the fingerprint permits field-type testing but does not itself enable
  cosmological perturbation recovery;
- the recovery matrix requires a scalar singlet and closed truncation;
- the canon dark-energy file marks scalar field type as an assumption/failure
  mode; and
- the current fingerprint lacks the scalar projector, observable map, SVT
  action, source-residue discharge, and frozen boundary data needed for closure.

The gate is a process/scientific-scope boundary check. It does not validate GU
physics or alter any governed status surface.

## Next Recovery Work

The next highest-information recovery item is the `SM-CONSISTENT-SECTOR`
target-free selector screen, unless the daily steward updates the portfolio or a
new frozen packet changes the frontier. A renewed cosmology attempt would need a
new source-owned scalar-singlet/truncation certificate first, not another
background-distance comparison.

Priority signal: advisory internal signal that the cosmology perturbation
checkpoint closed negative at this fingerprint.

Joe signal: none.

Paper seed proposal: none.
