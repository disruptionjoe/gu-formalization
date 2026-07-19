---
title: "Construction-space GR R0 lemma, C9 before C3"
status: exploration
doc_type: construction_space_probe
created: 2026-07-19
run_id: RUN-20260719-534-repository-work-cycle-cai-hourly
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
probe: P1-GR-R0-LEMMA-C9-C3
test: tests/recovery-contract/construction_space_gr_r0_c9_c3_gate.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Construction-space GR R0 lemma, C9 before C3

Operational result: `P1 complete`.

This probe applied the GR Rung 0 sharp list to the two current live GR
construction-space cells named by council round 2:

1. `C9-AMBIENT-H-CLASS`, the ambient-curvature / H-class residual-bookkeeping
   route.
2. `C3-BARE-THETA-STIFFNESS`, the bare-theta / fundamental-stiffness route.

It does not change claim status, canon verdicts, public posture, paper state,
or the gravity-leg verdict. It only updates the construction-space search map
with current-evidence R0 dispositions.

## Construction Forks

The gravity functional side is program-native: the `|II|^2` /
second-fundamental-form residual on `Y14 = Met(X4)`. The benchmark metric is
standard-physics comparator data: imported exact Schwarzschild/Kerr in a
`Psi = 0` gravitational vacuum. The built W229 source action uses the
record-current construction, where `Psi = 0` implies `J[Psi] = 0`, hence
`theta = 0`.

The P1 native-vacuum sub-question is therefore explicit:

```text
Is Psi=0 a source-native vacuum selected by GU, or a comparator-side vacuum
condition inherited from importing a GR vacuum metric?
```

Current evidence supports only the second reading for the W229 branch. A
nonzero bare-theta vacuum source is a legitimate reframe candidate only after
it supplies a source-owned field equation, boundary data, normalization, and
tensor shape independently of the Schwarzschild residual.

## Machine Check

`tests/recovery-contract/construction_space_gr_r0_c9_c3_gate.py` reuses the
existing principled Schwarzschild `Q^TF(B)` residual calculation.

Positive controls:

- `Q^TF(B)` is nonzero.
- A predeclared tensor `S = -Q^TF(B)` would algebraically cancel it.
- A metric-proportional stiffness or vacuum-energy stress has zero trace-free
  part and cannot cancel the nonzero trace-free residual.

## C9 Result

`C9-AMBIENT-H-CLASS` is `GATED` at GR R0, not failed.

Reason: it is the right type of route for the GR sharp list's "different
residual bookkeeping" clause and preserves the linear cheap-read clears, but
the current repository evidence does not yet provide a source-owned
higher-codimension first variation or a coefficient frozen before target use.
Those are the gate conditions.

## C3 Result

`C3-BARE-THETA-STIFFNESS` is `R0_FAIL` for the current scalar/isotropic
bare-theta lemma class.

Reason: a scalar or metric-proportional stiffness source is in the wrong tensor
slot. It cannot cancel a nonzero trace-free `Q^TF(B)` residual. An arbitrary
trace-free tensor shaped as `-Q^TF(B)` would be target import unless derived
before target confrontation. A future source-owned bare-theta equation with
boundary data, normalization, and trace-free tensor shape is a new dependency,
not present current evidence.

## Boundary

This is not exhaustion. The GR track now has no unblocked current-evidence C3
survivor, and C9 is gated on a named source-owned object. Gated cells, including
the C4 boundary-adapter cell, keep the predeclared class from supporting an
exhaustion claim.

Paper seed proposal: none.
