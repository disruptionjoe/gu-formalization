---
title: "Recovery contract GR forced-coefficient residual test"
status: exploration
doc_type: recovery_contract_checkpoint
created: 2026-07-16
run_id: GUH-20260716T091221Z-gr-forced-residual
test: tests/recovery-contract/gr_forced_coefficient_residual_test.py
fingerprint: lab/process/recovery-contract-action-fingerprint-2026-07-16.json
---

# Recovery contract GR forced-coefficient residual test

Operational result: `NO_GO` for this branch-local exact-vacuum GR cancellation test.

The action fingerprint from `RECOVERY-CONTRACT` was usable enough to run the first
forced-coefficient gravity benchmark. The test asked whether the frozen
W203/W229/W230/W236 record-current induced-YM branch supplies native source/YM terms that
cancel the nonzero `O(M^2)` Schwarzschild Willmore residual without changing the action,
source law, variation space, or free-quantity ledger.

It does not.

## Construction fork

The residual side uses the GU-native gravity functional fork: the principled `|II|^2`
second-fundamental-form residual on `Y14 = Met(X4)`. The Schwarzschild metric is imported
only as the standard-physics vacuum benchmark.

The source side uses the record-current theta construction because that is the construction
fixed by the W229 action fingerprint. Under that construction, `Psi=0` implies `J=0`, hence
the screened W229 source law gives `theta=0`. The bare geometric distortion branch is a
different construction and is not varied inside this test.

## Result

`tests/recovery-contract/gr_forced_coefficient_residual_test.py` recomputes the principled
Schwarzschild residual:

- the principled mean curvature `H^(1)` vanishes by harmonicity;
- the trace-free quadratic residual `Q^TF(B)` is nonzero;
- its nonzero components have leading falloff `M^2/r^6` on a generic ray.

The same test then consumes the action fingerprint:

- the fingerprint requires the W154 record-current source law;
- in the `Psi=0` vacuum, the record current `J[Psi]` vanishes;
- for sampled admissible `{kappa, Z_U}`, the screened W229 equation gives `theta=0`;
- every frozen source/YM cancellation term available in this branch is therefore zero.

So `Q^TF(B) + source/YM = Q^TF(B)`, still nonzero. No value of the free normalizations
`kappa` or `Z_U` can turn a zero tensor into `-Q^TF(B)`.

## Boundary

This is a branch-local negative result. It does not say that every gravity construction
fails. It says the exact-vacuum GR recovery benchmark cannot be claimed from this frozen
record-current W229 fingerprint. A cancellation would require a different construction or an
extra object, such as a bare theta branch, a fundamental `c_kin > 0` branch, an H-class or
curved-ambient functional term, or another action.

No claim status, canon verdict, public posture, paper surface, `RESEARCH-STATUS`, or
portfolio surface changed. The existing linear Schwarzschild/Kerr cheap-read clears remain
at their prior conditional grade, and exact recovery remains below recovery grade.

## Next recovery work

The next recovery-certification swing should not repeat this branch-local exact-vacuum GR
cancellation test. Worthy follow-ups are:

1. `COSMO-PERTURBATIONS` field-type and scalar-truncation gate under the same fingerprint.
2. `SM-CONSISTENT-SECTOR` target-free selector screen if exact gauge quotient inputs are ready.
3. A different GR construction only if it explicitly names a new action/fork and does not merge
   it with this failed W229 record-current branch.

Priority signal: advisory internal signal that the GR forced-coefficient branch-local item is
closed negative at this construction grade. No Joe signal.

Paper seed proposal: none.
