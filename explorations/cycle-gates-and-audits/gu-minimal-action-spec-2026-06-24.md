---
title: "GU Minimal Action Specification for the 4D Physics Gates"
date: 2026-06-24
status: exploration
doc_type: research_note
problem_label: "gu-minimal-action-spec"
verdict: "OPEN_SPECIFICATION_WITH_BLOCKING_IG_DYNAMICS"
owned_path: "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
depends_on:
  - "explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md"
  - "canon/dark-energy-theta-divergence-free.md"
  - "canon/theta-field-flrw-dark-energy-eos.md"
  - "canon/schwarzschild-weak-field-rfail.md"
  - "explorations/dark-energy-cosmology/dark-energy-assumption3-variational-2026-06-23.md"
  - "explorations/dark-energy-cosmology/dark-energy-w-window-mechanism-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/rfail-non-umbilic-schwarzschild-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/rfail-schwarzschild-oq2-weak-field-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md"
---

# GU Minimal Action Specification for the 4D Physics Gates

## Verdict

This note specifies the minimal action object that the next worker should test. It is **not**
a claim that the action is Weinstein's action, and it is not a claim that GU reproduces
Schwarzschild/Kerr or the DESI-sign dark-energy coupling.

The honest verdict is:

```text
OPEN_SPECIFICATION_WITH_BLOCKING_IG_DYNAMICS
```

The action can be made precise enough to run the two binary tests only after one missing
ingredient is fixed: the IG-sector variation. The existing reconstruction varies
`S_IG = int |theta|^2` with respect to `A` while holding the IG variables fixed. If the IG
translation field is varied independently with no extra dynamics or constraint, the same
term forces `theta = 0`. Therefore an actual variational principle must say whether the IG
variables are gauge/background data, constrained variables, or dynamical fields with their
own kinetic/potential term.

Until that is supplied from a primary written GU action, exact Schwarzschild/Kerr recovery
and the coefficient of `xi R theta^2` are open action-level questions.

## 1. Objects and Independent Fields

### 1.1 Geometric base

Use the current repo conventions:

```text
X = X^4                         smooth oriented 4-manifold
Y = Y^14 = Met(X)               bundle of Lorentzian metrics over X
gY = g_gimmel                   trace-reversed Frobenius plus tautological horizontal metric
signature(gY) = (9,5)
G = Sp(64)
P -> Y                          principal G-bundle
```

Minimal action convention: `gY` is the fixed canonical gimmel metric. It is not varied as an
independent metric field. The 4D metric is varied through the section:

```text
s: X -> Y
g = s^* gY
```

If a primary source instead varies `gY` independently, this specification is incomplete and
the EL tuple below must be enlarged by `E_gY = 0`.

### 1.2 Dynamical fields

Use distinct symbols to avoid the existing `B` collision:

```text
s        section X -> Y; determines g = s^*gY
A        Sp(64) connection on P -> Y
F_A      dA + (1/2)[A,A]
eps      G-valued IG/gauge variable
beta     IG translation field in Omega^1(Y, ad P)
Psi      Dirac-DeRham spinor-valued field on Y
```

Derived fields:

```text
Gamma(eps)        reference / Levi-Civita / tautological connection fixed by eps and gY
pi(A,eps)         A - Gamma(eps)
theta             pi(A,eps) - Ad(eps^-1) beta
B_s               II_s^H, the horizontal-normalized second fundamental form of s
j_s(B_s)          soldered ad(P_s)-valued image of B_s when needed
```

The horizontal-normalized convention is mandatory:

```text
II_s^H = 0 for the tautological flat LC section.
```

The raw algebraic slice convention is not the action convention for this spec. If the actual
GU action uses the raw `II_s`, the Schwarzschild and FLRW reductions must be redone.

### 1.3 Variations that must be stated

The minimal EL tuple is:

```text
(E_s, E_A, E_eps, E_beta, E_Psi) = 0.
```

Boundary conditions are part of the variation:

- For asymptotically flat Schwarzschild/Kerr tests: fix ADM mass and, for Kerr, angular
  momentum at infinity; use the exterior domain.
- For FLRW reduction: fix the scale-factor endpoints or add the corresponding cosmological
  boundary term.
- For gauge fields: fix either `A` or the canonical conjugate boundary flux on the boundary.

## 2. Minimal Candidate Action

The minimal test action is the following additive action:

```text
S_GU^min[s,A,eps,beta,Psi]
  = S_YM[A]
  + S_DD[A,Psi]
  + S_theta[A,eps,beta]
  + S_W[s,A,eps,beta]
  + S_IG-dyn[eps,beta; A]        (required open slot)
  + S_boundary.
```

The baseline branch of this specification sets:

```text
S_thetaF = 0
S_Rtheta,bare = 0
S_Lambda,bare = 0
```

That is deliberate. The FLRW test must decide whether `xi R theta^2` is generated by GU
reduction, not inserted by hand. If a primary source supplies a nonzero bare curvature
coupling, record it as a different branch and do not count it as a geometry-generated pass
unless the source fixes the sign and normalization.

## 3. Lagrangian Term Inventory

### 3.1 Yang-Mills sector

```text
S_YM[A] = - 1/(4 g_A^2) int_Y dvol_gY <F_A, F_A>_sp,Y
```

Required choices:

- The pairing `< , >_sp` is Ad-invariant.
- Normalize the soldering map so that

  ```text
  <j_s(n_i), j_s(n_j)>_sp = h_ij.
  ```

  If using the raw Clifford-trace map from the IC2 notes, carry the factor
  `<j_s(n_i),j_s(n_j)> = 512 h_ij` explicitly through all reductions.

Variation target:

```text
delta_A S_YM gives g_A^-2 D_A^* F_A.
```

### 3.2 Dirac-DeRham / spinor sector

```text
S_DD[A,Psi] = int_Y dvol_gY <Psi, D_GU(A,eps) Psi>
```

where `D_GU = d_A + d_A^* + Shiab` in the current reconstruction language.

Variation targets:

```text
E_Psi = D_GU(A,eps) Psi = 0
delta_A S_DD = J_Psi
delta_s S_DD contributes T_Psi to the pulled-back 4D stress tensor.
```

For the vacuum Schwarzschild/Kerr gate, set `Psi = 0` and require `J_Psi = 0`.

### 3.3 Distortion norm sector

```text
S_theta[A,eps,beta] = - c_theta/2 int_Y dvol_gY <theta, theta>_sp,Y
theta = A - Gamma(eps) - Ad(eps^-1) beta.
```

Sign and normalization convention:

```text
g_A^-2 D_A^* F_A - c_theta theta + J_Psi + ... = 0.
```

Set `g_A^2 c_theta = 1` if the intended transcript convention is:

```text
D_A^* F_A = theta        in vacuum.
```

This is the convention used for the binary tests below. If a different sign is chosen, every
appearance of `theta` in the reduction must be sign-adjusted.

Important warning:

```text
delta_beta S_theta alone forces theta = 0.
```

Therefore `S_theta` cannot be the complete IG action if `beta` is independently varied.
The missing `S_IG-dyn` or a constraint/gauge-status declaration is load-bearing.

### 3.4 Section / Willmore sector

```text
S_W[s,A,eps,beta] = alpha_W/2 int_X dvol_g |B_s|^2_g,h
B_s = II_s^H
```

Use the horizontal-normalized second fundamental form:

```text
(II_s^H)_{ab}^{(cd)} = (nabla^{g}_{e_a} theta_b)^{(cd)}
```

at linear order, in the moving-frame convention.

Variation target:

```text
E_s^W = alpha_W [Delta^perp H + normal-curvature terms + shape terms] + ...
```

This is the term responsible for the existing exact Schwarzschild obstruction under the
Willmore-only reading. The full Schwarzschild/Kerr test must check whether the remaining
action sectors cancel or modify this residual.

### 3.5 IG dynamics or constraint sector: required open slot

The action must contain one of the following, but the repo does not yet have a primary-source
choice:

```text
Option I:  eps,beta are not varied physical fields.
Option II: eps,beta are constrained gauge/Stueckelberg variables with explicit constraints.
Option III: eps,beta have a dynamical term S_IG-dyn[eps,beta;A].
```

The minimum required property is:

```text
E_beta does not imply theta = 0 unless theta = 0 is intended physics.
E_eps is compatible with theta -> Ad(g)^-1 theta under local G.
```

A viable `S_IG-dyn` must also state whether it generates the FLRW scalar kinetic term, the
mass `M_KK`, and any curvature coupling.

### 3.6 Excluded baseline terms that must be reported if present

These terms are set to zero in `S_GU^min` unless a primary source explicitly supplies them:

```text
S_thetaF      = lambda_thetaF int_Y dvol_gY <theta, D_A^*F_A>
S_DthetaF     = lambda_DthetaF int_Y <D_A theta, F_A>
S_Rtheta,Y    = - 1/2 xi_Y int_Y dvol_gY R_Y <theta,theta>
S_Rtheta,4    = - 1/2 xi_4 int_X dvol_g R[g] |s^*theta|^2
S_torsion     = sum_i k_i int_X dvol_g I_i(theta)
S_Lambda,bare = - int_X dvol_g Lambda_bare
```

Why they are excluded from the baseline:

- `thetaF` changes the `A` equation and can invalidate sector-wise `D_A^*theta = 0`.
- A bare `R theta^2` term would decide the dark-energy `xi` gate by insertion, not by
  reduction.
- A bare 4D `Lambda` hides the umbilic/trace equation.

If any of these terms is included, the next worker must run the two binary tests for that
explicit branch and record the coefficient values.

## 4. Required Sign and Normalization Choices

### 4.1 Four-dimensional conventions

Use:

```text
signature(g) = (-,+,+,+)
R^rho{}_{sigma mu nu} =
  partial_mu Gamma^rho_{nu sigma}
  - partial_nu Gamma^rho_{mu sigma}
  + Gamma^rho_{mu lambda} Gamma^lambda_{nu sigma}
  - Gamma^rho_{nu lambda} Gamma^lambda_{mu sigma}
G_mu nu = Ric_mu nu - (1/2) g_mu nu R
```

The 4D Einstein normalization is:

```text
G_mu nu + Lambda g_mu nu = 8 pi G_N T_mu nu.
kappa_4^2 = 8 pi G_N.
```

Any reduction from the 14D coupling must report:

```text
kappa_4^2 = g_A^2 / C_Gauss      or the corrected fiber-volume formula.
```

Do not silently set `C_Gauss = 1`; the IC4 notes identify this as open.

### 4.2 FLRW scalar normalization

To compare with the dark-energy files, the homogeneous theta mode must be the canonical
scalar `B(t)` in:

```text
S_eff[B,g] contains int_X sqrt(-g) [
  -1/2 g^mu nu partial_mu B partial_nu B
  -1/2 (M_KK^2 + xi R[g]) B^2
  - Lambda_eff
  + ...
]
```

The equation of motion is then:

```text
B_ddot + 3 H B_dot + (M_KK^2 + xi R) B + ... = 0.
```

The dark-energy window note uses this convention. In it:

```text
M_KK^2 = 8 H_0^2              (reconstruction grade)
xi < -0.319                  reaches w_a < 0
xi ~= -0.6                   matches the DESI ratio at reconstruction grade
xi = 0 or xi = +1/6          fails the DESI-sign window
```

If the raw reduction gives a non-canonical field `b_raw`, compute the wavefunction factor:

```text
B = sqrt(Z_theta) b_raw
xi_eff = C_Rtheta / Z_theta.
```

The binary `xi` gate must use `xi_eff`, not the raw coefficient.

## 5. Euler-Lagrange Checklist

The next worker should not test 4D physics until all checklist items are written in the
chosen branch.

### 5.1 Connection equation

Compute:

```text
E_A =
  g_A^-2 D_A^* F_A
  - c_theta theta
  + J_Psi
  + E_A^W
  + E_A^IG-dyn
  + E_A^cross
  = 0.
```

Required outputs:

- Does vacuum imply `D_A^*F_A = theta`, `D_A^*F_A = -theta`, or something else?
- Does the pulled-back equation read

  ```text
  D_a^* F_a + K(A,s) = s^*theta
  ```

  with the Codazzi correction `K(A,s)` exactly as in the Codazzi notes?
- Is `D_A^*theta = 0` an off-shell sector identity, an on-shell consequence, or not true?

### 5.2 Section equation

Compute:

```text
E_s =
  delta_s S_W
  + delta_s S_YM
  + delta_s S_DD
  + delta_s S_theta
  + delta_s S_IG-dyn
  + boundary terms
  = 0.
```

Required outputs:

- The leading Willmore term `Delta^perp H + shape terms`.
- Contributions from `theta`, `F_A`, and `Psi` that could cancel the Schwarzschild/Kerr
  Willmore residual.
- The contracted Gauss relation:

  ```text
  G^X_mu nu = G^Y_T_mu nu + Q_mu nu(B_s) + E^Psi_mu nu
  ```

  with all normalization factors and signs.

### 5.3 IG-variable equations

Compute:

```text
E_beta = delta_beta(S_theta + S_IG-dyn + S_cross) = 0
E_eps  = delta_eps (S_theta + S_IG-dyn + S_DD + S_cross) = 0
```

Required outputs:

- Does `E_beta` force `theta = 0`?
- If not, what prevents it?
- Are `E_beta` and `E_eps` gauge constraints, dynamical equations, or gauge-fixing equations?
- Do they preserve the equivariance of `theta` under local right `G` action?

### 5.4 Spinor equation

Compute:

```text
E_Psi = D_GU(A,eps) Psi = 0
```

For vacuum Schwarzschild/Kerr:

```text
Psi = 0
J_Psi = 0
E^Psi_mu nu = 0
```

must be a consistent solution, not an extra assumption contradicted by the other equations.

## 6. Binary Reduction Check A: Exact Schwarzschild/Kerr

### 6.1 Target configurations

For each metric:

```text
g = Schwarzschild(M)       on the exterior r > 2M
g = Kerr(M,a)              on the exterior domain with |a| < M
```

look for fields:

```text
(s_g, A_g, eps_g, beta_g, Psi_g = 0)
```

such that:

```text
s_g^* gY = g                 up to diffeomorphism/gauge
T_matter = 0
Lambda = 0                   or the explicitly stated asymptotic Lambda branch
```

Boundary data:

- Schwarzschild: asymptotically flat mass `M`.
- Kerr: asymptotically flat mass `M` and angular momentum `J = aM`.
- Gauge fields: finite action/energy on the exterior domain and no hidden external matter
  source at infinity.

### 6.2 Protocol

For each target metric:

1. Construct the section `s_g`.
2. Compute `theta_g`, `B_s = II_s^H`, `H`, `hat B`, `Q(B_s)`, `K(A,s)`, and `E^Psi`.
3. Evaluate the full EL tuple:

   ```text
   E_s = 0
   E_A = 0
   E_eps = 0
   E_beta = 0
   E_Psi = 0
   ```

4. Separately record:

   ```text
   R_fail^GR_mu nu = G_mu nu[g] - 8 pi G T_mu nu - Lambda g_mu nu
   R_section        = E_s projected to 4D tensor data
   R_full           = R_fail^GR + R_section
   ```

   Do not conflate the exact GR residual, which is zero for Schwarzschild/Kerr by definition,
   with the GU section-equation residual.

5. Check that any cancellation is internal to the vacuum GU equations. A solution that works
   only by reclassifying `Q^TF(B_s)` as matter does not pass the vacuum test.

### 6.3 PASS/FAIL

PASS for a target metric iff there exists a smooth vacuum field configuration satisfying the
full EL tuple and the boundary data.

FAIL for a target metric iff:

- the Willmore residual remains nonzero after all `A`, `theta`, `eps`, `beta`, and cross-term
  contributions are included;
- the solution requires `Psi != 0` or nonzero effective matter stress in a branch advertised
  as vacuum;
- the IG equations force `theta = 0` and thereby destroy the constructed solution;
- the result holds only at weak-field order and not exactly;
- the branch relies on an unspecified `S_IG-dyn`.

Interpretation:

```text
Schwarzschild PASS and Kerr PASS:
  exact vacuum GR black-hole gate passes for the written action.

Schwarzschild PASS and Kerr FAIL:
  spherical exact vacuum recovery is not enough; rotating vacuum GR remains obstructed.

Either FAIL:
  the current written action does not reproduce full nonlinear vacuum GR in that sector.
```

## 7. Binary Reduction Check B: FLRW Theta and xi

### 7.1 FLRW ansatz

Use:

```text
g = -dt^2 + a(t)^2 gamma_ij dx^i dx^j
Psi = 0
theta pulled back to one homogeneous isotropic mode
s^*theta = b_raw(t) u_0
```

where `u_0` is normalized by the same pairing used in the action. Reduce to a canonical
scalar `B(t)` with the kinetic normalization in Section 4.2.

### 7.2 Protocol

1. Pull back `S_GU^min` along the FLRW section.
2. Integrate/project over the fiber or normal mode using a stated measure.
3. Canonically normalize the scalar:

   ```text
   S_eff contains -1/2 (partial B)^2.
   ```

4. Read off:

   ```text
   M_KK^2
   xi_eff
   Lambda_eff
   quartic/self-interaction terms
   derivative curvature couplings
   tensor/spin character of the mode
   ```

5. Verify the EOM is exactly in the dark-energy convention:

   ```text
   B_ddot + 3H B_dot + (M_KK^2 + xi_eff R) B + ... = 0.
   ```

6. Compare `xi_eff` with the window:

   ```text
   xi_eff < -0.319       pass threshold for negative w_a window
   xi_eff ~= -0.6        reconstruction-grade DESI ratio match
   ```

### 7.3 PASS/FAIL

PASS iff the written GU action, with no hand-inserted 4D `R theta^2` term unless primary-sourced,
generates a canonical scalar FLRW theta mode with:

```text
M_KK^2 compatible with the stated theta-field mass input,
xi_eff < -0.319,
and preferably xi_eff ~= -0.6 in the same normalization.
```

FAIL iff:

- no `R[g] B^2` term appears;
- `xi_eff = 0`, `xi_eff = +1/6`, or `xi_eff >= -0.319`;
- the sign flips under canonical field normalization;
- the pulled-back `theta` mode is spin-2 or constrained rather than scalar, invalidating the
  Klein-Gordon FLRW analysis;
- the negative `xi` is added as a free phenomenological parameter rather than generated by
  the action;
- the needed value depends on the missing `S_IG-dyn` in an unspecified way.

## 8. Failure Conditions for This Specification

**FC1: Missing IG dynamics.** If `eps` and `beta` are independent variations and the only
IG term is `S_theta = -c_theta/2 int |theta|^2`, then `E_beta` forces `theta = 0`. The
specification is blocked until the action supplies `S_IG-dyn`, a constraint, or a declaration
that the IG variables are not independently varied.

**FC2: Actual GU action uses `theta * D_A^*F_A` instead of `|theta|^2`.** Then the EL equations
in this note are the wrong branch. The next worker must rewrite `E_A`, `E_theta`, `E_eps`, and
`E_beta` for that action and rerun both binary tests.

**FC3: Bare curvature coupling.** If a primary source includes a bare `-1/2 xi R theta^2`
term, the FLRW gate becomes a source-verification problem: quote the source, normalize the
field, and report the fixed `xi`. Do not count a tunable `xi` as a GU prediction.

**FC4: Soldering normalization drift.** If the raw `j_s` normalization factor `512` is dropped
or double-counted, both Newton's constant and `xi_eff` are numerically meaningless.

**FC5: Wrong `II_s` convention.** If the raw algebraic-slice second fundamental form is used
instead of `II_s^H`, flat space has a spurious section curvature and the Schwarzschild/Kerr
test is contaminated.

**FC6: Weak-field/exact conflation.** Passing the canon weak-field Schwarzschild gate at
`O(M/r)` does not pass the exact Schwarzschild/Kerr gate. The full EL residual must vanish,
not merely be small.

**FC7: Vacuum/matter relabeling.** A branch that makes Schwarzschild/Kerr work only by treating
`Q^TF(B_s)` or a gauge residual as matter fails the vacuum test.

**FC8: Scalar-mode assumption fails.** If `s^*theta` is not a homogeneous scalar after FLRW
reduction, the dark-energy `xi` window from the KG files cannot be applied.

**FC9: Primary-source mismatch.** If Weinstein's written action has different field content,
couplings, or variation status, this note is only a reconstruction branch and must be superseded.

## 9. Immediate Next Work

The next worker should do these in order:

1. Resolve `FC1`: find or define the IG-sector term/constraint and the variation status of
   `eps,beta`.
2. Derive the complete EL tuple for the chosen branch.
3. Run Binary Check A on Schwarzschild first, then Kerr.
4. Run Binary Check B on the FLRW theta scalar and extract `xi_eff`.
5. Record the outcome in the matrix from the prior gate:

```text
Gate A exact Schwarzschild/Kerr: PASS or FAIL
Gate B xi R theta^2:             PASS or FAIL
```

## Sources Read

- `explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `explorations/dark-energy-cosmology/dark-energy-assumption3-variational-2026-06-23.md`
- `explorations/dark-energy-cosmology/dark-energy-w-window-mechanism-2026-06-23.md`
- `explorations/dark-energy-cosmology/theta-field-flrw-matter-era-ode-2026-06-23.md`
- `explorations/geometry-curvature-emergence/rfail-non-umbilic-schwarzschild-2026-06-23.md`
- `explorations/geometry-curvature-emergence/rfail-schwarzschild-oq2-weak-field-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
- `explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md`
- `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`
- `explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md`
- `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`
- `explorations/geometry-curvature-emergence/rfail-umbilic-sections-2026-06-23.md`
