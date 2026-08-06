---
artifact_type: hostile_review
created: 2026-08-05
status: PASS_AFTER_EIGHT_MATERIAL_SCOPE_CORRECTIONS
target: explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md
charges:
  - summary_outruns_artifact
  - rigor_defends_superseded_or_mistyped_object
---

# Hostile review: first perturbative background C-operator

## Verdict

`PASS_AFTER_EIGHT_MATERIAL_SCOPE_CORRECTIONS`.

The exact matrix theorem survives. The review rejects every reading in which
it is promoted from a fixed-background two-field Hessian to a completed
interacting GU quantum theory.

## Charge 1 — where the summary outruns the artifact

### 1. “Interacting C” was too broad

The machine object is a linear fundamental symmetry of the TT **second
variation at fixed constant scalar background**. It is not a nonlinear
symmetry of the complete action and not a linear C-operator on Fock space.

**Repair:** the title, Layer 0, result and ledger say “background C” and retain
both larger objects as open.

### 2. The background was being priced as a vacuum

Nothing here proves that `bar theta` solves the complete coupled Euler system.
The Hessian theorem is valid off shell; physical-vacuum stability needs a
stationary selected background first.

**Repair:** the result now calls the background supplied and possibly off
shell, and explicitly excludes a physical-vacuum theorem.

### 3. “Unique” lacked its hypotheses

Uniqueness holds for fixed `K`, distinct real eigenvalues and the positivity
orientation on one connected component. It fails at the scalar collision and
the sign reverses on the disconnected real component.

**Repair:** every uniqueness statement now carries the fixed-K,
distinct-spectrum and connected-component qualifiers.

### 4. “Zero parameter” hid upstream inputs

The first-order C correction has four coefficients and rank-four constraints,
but `alpha`, `b`, `c` and `bar theta` are inputs to that system. The theorem
does not derive them.

**Repair:** the constraint count is now “zero C-correction freedom after
action coefficients and background are supplied.”

### 5. Positive finite matrix was drifting toward unitarity

`K C(u)>0` is finite two-mode background positivity. It says nothing by itself
about a common nonlinear domain, boundedness over modes, Fock completion,
scattering amplitudes, loops or type-III locality.

**Repair:** these are excluded in the result, ledger and next gate; H59/W132
remain live.

## Charge 2 — where rigor was defending a superseded or mistyped object

### 6. The July D1 lift was the wrong completion target

D1's explicit remaining lift is a 192-dimensional record-sector construction.
The new non-toy object is the two-dimensional gravitational TT Hessian. Calling
this “the D1 lift” would solve a neighboring object precisely.

**Repair:** D1 is method precedent and non-duplication control only. Its
192-dimensional lift remains open.

### 7. The old scalar-parity kill was being defended too strongly

The predecessor killed only `(q0,qm,theta)->(q0,-qm,+/-theta)`. Requiring the
same `P` after the Hessian moves would defend a superseded free object. The
proper interacting question allows the eigenspaces and C to move with `u`.

**Repair:** the report keeps both facts: `[P,L(u)]` is generically nonzero,
while the zero-parameter field-mixing `C(u)` exists on the free-connected
component.

### 8. Every discriminant wall was being treated as the same failure

The generic wall is non-scalar Jordan and admits no positive C. The special
`alpha=1,u=-b` collision is scalar and admits a continuum of positive C's;
the failure there is non-selection. The disconnected real component also has
a positive C, but with reversed orientation.

**Repair:** all three strata are separately typed and planted. No wall is
reported as a theory-wide kill.

## Exact hostile rerun obligations

- Reconstruct the action Hessian from `c theta(q0+qm)^2`, including diagonal
  and mixed entries.
- Verify `C^2=1`, `[C,L]=0`, `C^T K=K C`, `det(KC)=1` and positivity on an
  exact point in the free-connected region.
- Derive and solve the first-order constraint system independently.
- Exhibit a generic Jordan wall, a complex-spectrum point, a disconnected
  real point with reversed sign and a scalar non-unique collision.
- Confirm `SOURCE-SILENT`, P1/P2/P3 unused and no D1/full-QFT promotion.

The primary exact probe and independent Sage reconstruction satisfy these
obligations. The review therefore passes at the corrected scope.

## Remaining blocker

The next positivity gate is the complete selected cubic Hessian including
scalar fluctuations, followed by a common interacting BV/Green/Fock domain
and H59/W132 amplitude tests. Super-IG descent and the normalized observer
functional remain separate construction gates.
