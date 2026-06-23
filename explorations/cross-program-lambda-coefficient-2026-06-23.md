---
title: "Cross-Program Lambda Coefficient Test"
status: exploration
doc_type: research
updated_at: "2026-06-23"
scope: "Task 5 of 5: GU Tikhonov Lambda vs TaF observer-rate/decoherence coefficient"
depends_on:
  - "DERIVATION-PROGRESS.md"
  - "NEXT-STEPS.md"
  - "explorations/4d-reduction-62-persona-steelman-hegelian-2026-06-22.md"
  - "explorations/4d-reduction-section-pullback-2026-06-22.md"
  - "explorations/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
  - "explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md"
  - "explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md"
  - "explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md"
---

# Cross-Program Lambda Coefficient Test

**Status.** Bounded exploration. Not canon. Not active research. This note does not update
roadmap or status documents.

**Question.** On the compact test case `X^4 = S^4`, compute or constrain the coefficient in
the GU Tikhonov section-selection scale

```
Lambda_GU ~ epsilon_sec^2 / t_obs^2
```

and compare it with the Time-as-Finality observer-rate/decoherence coefficients from FR2.

## 1. Verdict

The dimensional contact survives, but the raw coefficient equality stated in the 4D-reduction
steelman needs a units correction.

GU's `Lambda` is a mass-squared / curvature-scale quantity:

```
[Lambda_GU] = T^-2 = L^-2          (with c = 1)
```

TaF FR2's primitive quantities are rates:

```
lambda_max = 1 / t_obs
Gamma_min(epsilon_dec) = ln(1/epsilon_dec) / t_obs
```

so

```
[lambda_max] = [Gamma_min] = T^-1.
```

The admissible comparison is therefore not `Lambda_GU` against `lambda_max`, but against
`lambda_max^2` or `Gamma_min^2`.

Under the normalized Gaussian/Tikhonov convention defined below,

```
Lambda_GU = C_GU * epsilon_sec^2 / t_obs^2
```

with `C_GU = 1` by convention. In the invariant geometric problem, however, `C_GU` is not
currently computable from existing notes because it depends on the still-missing Hessian of
the section energy at the chosen `S^4` section and on the normalization of the section norm.

Thus the current result is a constraint, not a numerical match:

```
Lambda_GU = C_GU * epsilon_sec^2 * lambda_max^2

Lambda_GU = (C_GU * epsilon_sec^2 / ln(1/epsilon_dec)^2) * Gamma_min(epsilon_dec)^2.
```

There is no generic exact equality with the TaF decoherence coefficient. Equality requires a
separate tolerance-identification condition.

## 2. Setup on Compactified `S^4`

Use the compact test case requested by CPA-1:

```
X^4 = S^4_R
```

where `R` is the round-sphere radius. Let

```
s : S^4_R -> Y^14 = Met(S^4_R)
```

be a section, and let `s_0` be the selected background section. The 4D-reduction notes identify:

```
E[s] = integral_{S^4_R} |II_s|^2 dvol_{g_s}
```

as the Willmore-type section energy, and P62 proposes the regularized section selector:

```
s_reg = argmin_s ( ||II_s||^2 + lambda ||s||^2 ).
```

The P62 identification is:

```
lambda_Tik = Lambda_cosmological.
```

This note assumes that identification. If `lambda_Tik` is only an auxiliary inverse-problem
parameter and not the cosmological curvature term, the cross-program test fails at the first
step.

## 3. Units and Normalization

Use natural units unless otherwise noted:

```
c = hbar = 1
time = length
[Lambda] = T^-2 = L^-2
```

If `c` is restored, then

```
Lambda_GU = C_GU * epsilon_sec^2 / (c^2 t_obs^2).
```

Let section perturbations be written

```
u = s - s_0 in Gamma(N_{s_0}),    N_{s_0} ~= Sym^2 T*S^4_R.
```

Normalize the zeroth-order section norm by the sphere volume:

```
||u||_0^2 = (1 / Vol(S^4_R)) * integral_{S^4_R} |u|^2 dvol_{g_0}.
```

With this convention, `u` and `epsilon_sec` are dimensionless. A finite observation window
defines the frequency scale

```
omega_obs = 1 / t_obs
```

using the non-angular-frequency convention. If angular frequency is used instead, replace
`C_GU` by `(2*pi)^2 C_GU`.

## 4. GU Coefficient Constraint

Linearize the Tikhonov system around `s_0`:

```
E[s_0 + u] = E[s_0] + (1/2) <u, H_s u> + O(u^3)
J_Lambda[u] = (1/2) <u, H_s u> + (1/2) Lambda ||u||_0^2 + ...
```

where `H_s` is the Hessian of the section energy. The finite-observer regularization ansatz
from P62 says the zeroth-order mass term is set by the square of the unresolved section
precision per observation time:

```
Lambda_GU = C_GU * (epsilon_sec / t_obs)^2.
```

On `S^4_R`, equivalently:

```
tau_obs = t_obs / R
Lambda_GU = (C_GU / R^2) * epsilon_sec^2 / tau_obs^2.
```

Because `S^4_R` supplies no further dimensional quantity, the coefficient `C_GU` is
dimensionless. It may depend on:

- the chosen section `s_0` or topological sector,
- the normalization of `||s||^2`,
- whether the frequency convention is angular or non-angular,
- the lowest relevant eigenvalue of the linearized Tikhonov operator.

Under the unit-normalized Gaussian convention above, the bounded computation gives:

```
C_GU = 1
Lambda_GU = epsilon_sec^2 / t_obs^2.
```

This is a convention-level coefficient, not an invariant geometric number. The invariant
coefficient cannot be computed until the explicit `II_s` formula and the Hessian spectrum on
`S^4` are known.

## 5. TaF Rate and Decoherence Coefficients

FR2 gives:

```
lambda_max = 1 / t_obs
Gamma_min(epsilon_dec) = ln(1/epsilon_dec) / t_obs
Gamma_min = ln(1/epsilon_dec) * lambda_max.
```

Therefore the mass-squared quantities comparable with `Lambda_GU` are:

```
lambda_max^2 = 1 / t_obs^2
Gamma_min^2 = ln(1/epsilon_dec)^2 / t_obs^2.
```

So the TaF coefficients are:

```
C_TaF,rate = 1
C_TaF,decoh = ln(1/epsilon_dec)^2.
```

FR2 also gives the operational coupling condition:

```
lambda_max <= Gamma / ln(1/epsilon_dec)
```

for a certifiable classical observer.

## 6. Coefficient Comparison

### 6.1 Comparison to observer service-rate squared

Using `lambda_max^2`:

```
Lambda_GU = C_GU * epsilon_sec^2 * lambda_max^2.
```

With `C_GU = 1`, an exact coefficient match to service-rate squared requires:

```
epsilon_sec = 1.
```

For any genuine small regularization tolerance `epsilon_sec << 1`, GU predicts a suppressed
mass-squared scale relative to the bare TaF service-rate square:

```
Lambda_GU << lambda_max^2.
```

This is not a failure; it says the GU term is a precision-suppressed rate square, not the
raw observer throughput square.

### 6.2 Comparison to decoherence-rate squared

Using `Gamma_min^2`:

```
Lambda_GU = [C_GU * epsilon_sec^2 / ln(1/epsilon_dec)^2] * Gamma_min^2.
```

Exact equality to the TaF decoherence-square coefficient requires:

```
C_GU * epsilon_sec^2 = ln(1/epsilon_dec)^2.
```

If the two tolerances are identified,

```
epsilon_sec = epsilon_dec = epsilon
```

and `C_GU = 1`, equality requires:

```
epsilon = ln(1/epsilon).
```

The solution is the omega constant:

```
epsilon = W(1) ~= 0.567143.
```

That is not a small-error regime. Therefore, in the physically usual regime
`epsilon << 1`, the two coefficients do not match if the same epsilon is used on both sides:

```
epsilon^2 << ln(1/epsilon)^2,
Lambda_GU << Gamma_min^2.
```

### 6.3 Best current interpretation

The clean cross-program relation is:

```
sqrt(Lambda_GU) = sqrt(C_GU) * epsilon_sec * lambda_max

sqrt(Lambda_GU) =
  [sqrt(C_GU) * epsilon_sec / ln(1/epsilon_dec)] * Gamma_min.
```

So GU's Tikhonov scale is a precision-weighted observer frequency. TaF's `Gamma_min` is a
decoherence-certification frequency. They share `t_obs`, but their tolerance factors differ:

- GU P62 uses a quadratic regularization tolerance `epsilon_sec^2`.
- TaF FR2 uses an exponential decoherence tolerance `ln(1/epsilon_dec)`.

That is the real cross-program content. A numerical coefficient match is additional and is
not currently established.

## 7. What Was Computed vs Constrained

Computed under stated convention:

```
C_GU = 1
Lambda_GU = epsilon_sec^2 / t_obs^2
```

Constrained invariantly:

```
Lambda_GU = C_GU(S^4, s_0, norm, spectrum) * epsilon_sec^2 / t_obs^2
```

where `C_GU` is dimensionless and must be extracted from the explicit Tikhonov linearization
on `S^4`.

Corrected cross-program comparison:

```
Lambda_GU / lambda_max^2 = C_GU * epsilon_sec^2

Lambda_GU / Gamma_min^2 =
  C_GU * epsilon_sec^2 / ln(1/epsilon_dec)^2.
```

## 8. Failure Conditions

This cross-program coefficient test fails, or remains non-invariant, under any of the
following conditions:

1. **Raw-unit mismatch.** If one compares `Lambda_GU` directly to `lambda_max` or
   `Gamma_min` rather than to their squares, the comparison is dimensionally invalid.

2. **Wrong Tikhonov identification.** If the Tikhonov parameter in
   `||II_s||^2 + lambda ||s||^2` is not the same object as the cosmological `Lambda`, then
   CPA-1 does not compute the cosmological constant.

3. **Different epsilon meanings.** If `epsilon_sec` is a UV/section-resolution tolerance
   and `epsilon_dec` is a decoherence tolerance, they cannot be identified without a new
   observer-section error model.

4. **Missing Hessian.** Without the explicit `II_s` formula and the Hessian of `E[s]` at the
   chosen `S^4` section, `C_GU` is a convention-dependent normalization, not an invariant
   coefficient.

5. **Different frequency convention.** Angular-frequency normalization changes the coefficient
   by `(2*pi)^2`.

6. **Non-Gaussian regularization.** If the section-selection posterior is not Gaussian near
   `s_0`, or if the optimal Tikhonov parameter scales as `epsilon` rather than `epsilon^2`
   under the relevant source condition, the P62 scaling changes.

7. **S^4 proxy mismatch.** If compactified `S^4` is not an admissible proxy for the Lorentzian
   GU section problem, the computed coefficient is only a Euclidean toy value.

8. **No shared `t_obs`.** If the GU observation timescale and the TaF finalization latency are
   not the same physical operation, the contact reduces to a dimensional analogy.

9. **BvN wall unproven.** FR2's `Gamma_min` assumes a Lindblad/pointer-basis decoherence model.
   It is a rate concept, not a proved BvN obstruction. If the BvN formalization fails, the
   decoherence comparison loses its structural status.

## 9. Next Bounded Computation

To turn the constraint into an invariant coefficient:

1. Choose the test section `s_0 : S^4 -> Y^14` and radius normalization `R = 1`.
2. Compute `II_s` in local moving frames.
3. Linearize `E[s] = integral |II_s|^2` at `s_0` and extract `H_s`.
4. Fix the Tikhonov norm `||s||^2`.
5. Read off the zeroth-order mass term in the Euler-Lagrange equation:

```
(H_s + Lambda I) u = source.
```

Only after this can `C_GU` be compared as a geometric coefficient rather than as a
normalization convention.

## 10. Bottom Line

CPA-1 remains live, but the comparison target must be sharpened:

```
GU Lambda  <->  TaF rate squared
```

not

```
GU Lambda  <->  TaF rate.
```

The strongest current result is:

```
Lambda_GU is a precision-suppressed square of the TaF observer rate.
```

The coefficient is `1` only in the normalized Gaussian convention. The invariant coefficient
is blocked by the same object already identified as the 4D-reduction bottleneck: the explicit
second fundamental form `II_s` and its section-energy Hessian on `S^4`.

