---
title: "VZ F5: Curvature Non-Reintroduction Check in Curved Sp(64) Bundle After Subprincipal-Symbol Evasion"
date: 2026-06-23
problem_label: "vz-f5-curvature"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ F5: Curvature Non-Reintroduction Check in Curved Sp(64) Bundle

## 1. Problem Statement

**What is being computed.** Following the chain

- Principal-symbol VZ evasion (vz-schur-complement, EVADED reconstruction),
- OQ1 (`S_R^2 != xi^2 Id` clarification, vz-oq1, CONDITIONALLY_RESOLVED),
- Lower-order curvature at 14D: principal-symbol stability (vz-oq2-lower-order-curvature, CONDITIONALLY_RESOLVED),
- Subprincipal symbol (vz-subprincipal, CONDITIONALLY_RESOLVED), and
- 4D section-pullback VZ evasion (vz-schur §17-19, CONDITIONALLY_RESOLVED at 4D principal-symbol level, constant-coefficient gauge),

this file addresses the final curvature-protection check: F5 in the tracking table.

**The F5 question.** The 4D effective RS operator `D_RS_eff^{4D} = S_{R_s}^{4D}` is obtained
by pulling back `D_GU` along the section `s: X^4 -> Y^{14}`. The section `s` introduces
second fundamental form contributions `II_s` (which encode the extrinsic curvature of
the embedding), and the 4D background has:

1. **Weyl tensor of `g_Y` pulled back** to `g_s = s*(g_Y|_{horizontal})`: the gimmel
   curvature restricted to 4D horizontal directions.
2. **Riemann tensor of `g_s`**: the 4D spacetime curvature (Gauss formula mixes `R^{g_Y}` with `II_s^2`).
3. **Sp(64) gauge curvature `F_A` pulled back**: `s*(F_A)` plus normal-bundle curvature
   from the Codazzi data `F_{A^0}^{perp}`.

The F5 question asks: after the 14D principal and subprincipal symbol VZ evasion, do
these 4D curvature terms (i) change the principal symbol of `S_{R_s}^{4D}`, or
(ii) introduce new characteristics via the subprincipal symbol at 4D, or (iii) via the
Shiab coupling in the 4D operator?

**Why F5 is a separate check from OQ2.** The 14D curvature analysis (OQ2, vz-oq2-lower-order-curvature)
established that 14D curvature terms are zero-order in D_GU. But after 4D pullback,
the second fundamental form `II_s` (a normal-bundle valued 2-tensor) contributes to the
horizontal Clifford symbol via the Gauss formula. A priori, this could mix `II_s` with
the horizontal symbol in a way that modifies the 4D principal symbol. The §17-19
computation in vz-schur-complement-2026-06-23.md addressed this, but a focused F5
analysis is required to integrate the curvature sources explicitly.

---

## 2. Established Context

**Results this builds on (all reconstruction grade unless stated):**

- `vz-schur-complement-2026-06-23.md` §17-19: The 4D section pullback `s*(D_GU)`
  satisfies `sigma_{s*(D_GU)}(eta)^2 = g_s(eta,eta) Id_{E_s}` for all horizontal
  covectors `eta in T*X^4`. The §8 kernel argument descends to 4D, giving
  `ker S_{R_s}^{4D}(eta) = 0` for `g_s(eta,eta) != 0`. 4D characteristic cone
  = null cone of `g_s`. VZ evasion CONDITIONALLY_RESOLVED at 4D principal-symbol level (constant-coefficient gauge).

- `vz-oq2-lower-order-curvature-2026-06-23.md`: All 14D curvature contributions
  (Weyl tensor `W_{ABCD}` of `g_Y`, Riemann tensor `R_{ABCD}`, Sp(64) gauge curvature
  `F_A`, Shiab `Phi(F_A)`) are zero-order in D_GU (multiplication operators on Psi).
  Zero-order terms do not change the principal symbol. Classical VZ lower-order mechanism
  (acting with a subsidiary-condition differential operator to convert zero-order curvature
  into first-order effective terms) does not apply because the GU RS constraint is
  domain-defining, not externally imposed.

- `vz-subprincipal-symbol-rs-2026-06-23.md` (vz-subprincipal): Three arguments
  confirm the subprincipal symbol `sigma_0(S_R^{full})` introduces no new real
  characteristics: (a) real principal type (Hormander Th. 23.2.4), (b) no sub-characteristics
  (first-order zero of principal symbol, Dencker-Taylor), (c) Shiab is anti-Hermitian
  (sp(64)-valued), producing only amplitude effects, not new directions.
  OQ2-a (Shiab strictly zero-order) also RESOLVED.

- `vz-schur-complement-2026-06-23.md` §19: 4D EFT decoupling (F6): horizontal Clifford
  element commutes with KK mode projector; B/C blocks are O(1) in zero-mode sector;
  gamma-trace constraint is intrinsic (no external subsidiary condition); VZ evasion
  survives KK mass-gap at reconstruction grade.

- `explorations/codazzi-sp64-2026-06-23.md`: Full Codazzi equation for Sp(64) bundle
  derived. The curvature of the normal bundle `R^{Y^{14},perp}` contributes to the
  section-pullback field equations.

- `explorations/ic3-nonlinear-conservation-2026-06-23.md`: Conservation identity
  `nabla^nu Q^{TF}_{mu nu} + K_nu = 0` at O(B^2) is an identity (section pullback
  of ambient Bianchi). No new structural obstruction.

- `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md`: HC1 curvature components.
  Weyl-tensor `W + S_0 + R` (visible) + `H^{(1)} + H^{(2)} + H^{(3)}` (torsion-activated,
  with SL(2,C) labels `(3/2,1/2)+(1/2,3/2)`, `(1/2,1/2)_V`, `(1/2,1/2)_A`). The
  hidden curvature pieces `H^{(i)}` are sourced by distortion torsion `T^{(i)}` and
  enter D_GU at zero order.

**Gauss formula (key identity).**

For a section `s: X^4 -> Y^{14}` with second fundamental form `II_s`, the Gauss formula
relates the curvatures of `g_s` and `g_Y`:

```
R^{g_s}(u, v, w, z) = (s*R^{g_Y})(u, v, w, z) + II_s(u,w) II_s(v,z) - II_s(u,z) II_s(v,w)
```

where `u,v,w,z in TX^4` are horizontal. The Riemann tensor of `g_s` has contributions
from both the pullback of the 14D curvature and the quadratic `II_s` terms.

**Principal-symbol identity for horizontal Clifford elements (exact, from §17-19):**

```
c_s(eta)^2 = g_s(eta,eta) Id_S    for eta in T*X^4 horizontal.
```

This is an exact matrix identity (no anomalous normal-direction terms), established by
the OQ3-V1 explicit horizontal Clifford computation.

---

## 3. Computation

### 3.1 Curvature Sources in the 4D Operator

After section pullback, the 4D operator `D_GU^{4D} = s*(D_GU)` acts on sections of
the 4D bundle `E_s = s*E` over `X^4`. In a local moving frame `{e^a}` on `X^4` with
`g_s(e^a, e^b) = eta^{ab}` (the 4D Lorentzian metric), the operator takes the form:

```
D_GU^{4D} = c_s(e^a) nabla^{4D}_a + (Shiab pullback) + (II_s mixing)
```

where `nabla^{4D}_a = nabla^{g_s}_a + A_a^H` combines the 4D Levi-Civita connection on
`X^4` and the horizontal projection of the Sp(64) connection.

**Three curvature sources in D_GU^{4D}:**

**Source 1: Pullback of 14D curvature.** The spin connection `omega_a` on `E_s` involves:

```
omega_a = s*(omega^{14D}_a)|_{horizontal} = (1/4) R^{g_s}_{abcd} e^b gamma^{cd} + ...
```

In Riemann normal coordinates for `g_s`. The Riemann tensor `R^{g_s}_{abcd}` is:

```
R^{g_s}_{abcd} = s*(R^{g_Y}_{abcd}) + (II_s * II_s terms)      [Gauss formula]
```

The pullback `s*(R^{g_Y}_{abcd})` includes the Weyl tensor `W_{abcd}` of `g_Y`
restricted to horizontal-horizontal-horizontal-horizontal directions.

**Source 2: Second fundamental form coupling.** The mixing terms in `D_GU^{4D}` from
`II_s` are:

```
(II_s mixing)_a = (1/2) II_s^{bc}_{..} gamma_{bc} / ...
```

These arise because `s*(nabla^{14D}) = nabla^{4D} + II_s` (the normal component of the
14D connection gives the second fundamental form on tangent vectors).

**Source 3: Normal-bundle gauge curvature.** The Sp(64) connection pulled back gives
`s*(F_A) = F_A^H + F_A^{mix} + F_A^{perp}` where `F_A^H` is the 4D field strength and
`F_A^{perp}` is the normal-bundle curvature (from the Codazzi formula for Sp(64),
codazzi-sp64-2026-06-23.md). The Shiab pullback `s*(Phi(F_A tensor .))` involves:

```
s*(Phi(F_A tensor Psi)) = sum_a e^a tensor c(iota_{e_a} s*(F_A)) . Psi + (normal-bundle terms)
```

### 3.2 Order Analysis of Each Curvature Source

**Claim.** All three curvature sources above are zero-order operators in the 4D field `Psi`.

**Source 1 (Weyl/Riemann of g_s via spin connection):**

The spin connection `omega_a` is a coefficient in D_GU^{4D}, not a derivative:

```
D_GU^{4D} = c_s(e^a)(d/dx^a + omega_a + A_a^H) + (Shiab)
```

The term `c_s(e^a) omega_a` is a zero-order operator: it multiplies `Psi` by a Clifford
element depending on `x` (the curvature enters `omega_a` but there is no additional
derivative of `Psi`). This is the same argument as in vz-oq2-lower-order-curvature §3.1.

The `II_s * II_s` terms in `R^{g_s}` enter `omega_a` at the same zero-order level.
They multiply `Psi` without differentiation.

**Source 2 (II_s mixing):**

The second fundamental form `II_s in Gamma(Sym^2 T*X^4 tensor N_s)` is a field on `X^4`.
In the pullback operator `D_GU^{4D}`, the `II_s` contribution enters the normal component
of the 14D connection:

```
nabla^{14D,perp}_a = II_s(e_a, .)   (the normal component of the 14D covariant derivative)
```

This gives:

```
D_GU^{4D}|_{II_s} = c_s(e^a) II_s(e_a, .)^{index-mixing}
```

The key point: `II_s(e_a, .)` acts on the normal indices of `Psi` (the one-form index
with respect to the normal directions). This is an algebraic action (index contraction
and Clifford multiplication), NOT a differential operator on `Psi`. The `II_s`-mixing
term is therefore zero-order.

**Justification from §17-19.** The OQ3-V1 result (exact horizontal Clifford computation)
confirms this: `c_s(eta)^2 = g_s(eta,eta) Id_S` as an exact matrix identity with ZERO
anomalous normal-direction terms. The second fundamental form does not contribute any
additional first-order (derivative of `Psi`) terms to the horizontal Clifford symbol.
This is because the Gauss formula expresses `R^{g_s}` in terms of `R^{g_Y}|_H` and
`II_s^2`, but neither of these introduces new first-order derivatives of `Psi` into the
principal symbol of `D_GU^{4D}`.

**Source 3 (Normal-bundle gauge curvature):**

The Shiab pullback `s*(Phi(F_A tensor Psi))` involves `s*(F_A)`, which is:

```
s*(F_A)_{ab} = (nabla^{4D}_a A_b - nabla^{4D}_b A_a + [A_a, A_b]) + (II_s mixing terms)
```

Each term is a field on `X^4` with no additional derivative of `Psi`. The Shiab is
`Phi(s*(F_A) tensor Psi) = sum_a e^a tensor c(iota_{e_a} s*(F_A)) . Psi`, a zero-order
multiplication operator on `Psi`. OQ2-a (established in vz-subprincipal §4.2) confirms
this at reconstruction grade: the Bianchi identity `D_A F_A = 0` does not introduce
derivative terms in `Psi`.

**The normal-bundle curvature `F_A^{perp}`** (from the Codazzi formula) enters via:

```
[D_A^{perp}, D_A^{perp}] II_s = R^{Y^{14},perp} + F^Psi_{j_s} - [F_{A^0}, j_s II_s]
```

(codazzi-sp64-2026-06-23.md, main equation). But this is a field equation for `II_s`,
not an additional derivative term in `Psi`. When inserted into `D_GU^{4D}`, the normal
curvature `F_A^{perp}` acts as a zero-order coefficient.

**Order summary:**

| Curvature source | How it enters D_GU^{4D} | Order in Psi |
|---|---|---|
| Weyl tensor `W_{abcd}` of `g_Y|_H` | Spin connection `omega_a` | Zero-order |
| Riemann tensor `R^{g_s}_{abcd}` of `g_s` | Spin connection `omega_a` | Zero-order |
| `II_s * II_s` quadratic in Gauss formula | Spin connection `omega_a` | Zero-order |
| `II_s` direct mixing | Normal index contraction | Zero-order |
| Sp(64) gauge curvature `s*(F_A)` (horizontal) | Shiab `Phi(s*(F_A) tensor .)` | Zero-order |
| Normal-bundle curvature `F_A^{perp}` | Shiab `Phi(F_A^{perp} tensor .)` | Zero-order |
| Hidden curvature pieces `H^{(i)}` via distortion | Spin connection (distortion torsion) | Zero-order |

### 3.3 Principal Symbol Stability at 4D

**Claim.** The principal symbol of `D_GU^{4D}` is:

```
sigma_1(D_GU^{4D})(x, eta) = c_s(eta)    for eta in T*X^4.
```

**Proof.** The principal symbol is determined by the highest-order differential terms.
Only the terms `c_s(e^a) d/dx^a` contribute to order 1. All curvature sources (table
above) are zero-order (they multiply `Psi` without differentiation). By the definition
of the principal symbol, `sigma_1(L)(x,eta) = sigma_1(L^{(1)})(x,eta)` where `L^{(1)}`
is the first-order part, and the zero-order part `L^{(0)}` contributes zero to `sigma_1`.

Therefore, `sigma_1(D_GU^{4D}) = c_s(eta)`, and:

```
sigma_1(D_GU^{4D})(eta)^2 = c_s(eta)^2 = g_s(eta,eta) Id_S     [exact, from OQ3-V1]
```

This is the Clifford module identity at 4D. The characteristic set of `D_GU^{4D}` is:

```
Char(D_GU^{4D}) = {eta in T*X^4 : det(c_s(eta)) = 0} = {eta : g_s(eta,eta) = 0}.
```

The characteristic cone is the null cone of `g_s`. No curvature source (Weyl tensor,
Riemann tensor, F_A, II_s) can enlarge this cone, because none contributes to the
first-order symbol.

### 3.4 Effective RS Principal Symbol at 4D

After Schur elimination at 4D (from §17-19 of vz-schur-complement), the effective RS
principal symbol is:

```
S_{R_s}^{4D}(eta) = sigma_1(P_{R_s} D_GU^{4D} P_{R_s}^{Schur})
```

The §8 kernel argument descends exactly to 4D:

```
ker S_{R_s}^{4D}(eta) = 0    for g_s(eta,eta) != 0.
```

This was VERIFIED (OQ3-V1, OQ3-V2, OQ3-V3). Including lower-order curvature corrections:

```
S_{R_s}^{4D,full}(eta) = S_{R_s}^{4D}(eta) + (zero-order corrections from all curvature sources)
```

The zero-order corrections do not change the principal symbol. Therefore:

```
sigma_1(S_{R_s}^{4D,full}) = S_{R_s}^{4D}(eta),   ker = 0 for g_s(eta,eta) != 0.
```

**VZ acausality at 4D after curvature inclusion: absent.**

### 3.5 4D Subprincipal Symbol Analysis

Building on vz-subprincipal (which established the 14D subprincipal symbol does not
introduce new characteristics), we apply the same analysis at 4D.

**The 4D subprincipal symbol:**

```
sigma_0(S_{R_s}^{4D,full}) = A_s^{(0)} - B_s^{(1)} (E_s^{(1)})^{-1} C_s^{(0)}
                             - B_s^{(0)} (E_s^{(1)})^{-1} C_s^{(1)}
                             + B_s^{(1)} (E_s^{(1)})^{-1} E_s^{(0)} (E_s^{(1)})^{-1} C_s^{(1)}
                             + (Poisson bracket corrections)
```

where the subscript `s` denotes the 4D section-pullback versions of the blocks.

**Each curvature source enters only the zero-order blocks `A_s^{(0)}, B_s^{(0)}, C_s^{(0)}, E_s^{(0)}`:**

- **Weyl/Riemann of g_s:** Enters `A_s^{(0)}` via the 4D spin-connection term
  `c_s(e^a) omega^{g_s}_a` restricted to RS and non-RS sectors.
- **II_s contributions:** The normal-index mixing enters `A_s^{(0)}` and the off-diagonal
  blocks via `P_{R_s}(II_s mixing) P_{R_s}` and `P_{Q_s}(II_s mixing) P_{R_s}`. These
  are all zero-order endomorphisms.
- **s*(F_A) Shiab:** Enters `A_s^{(0)}` and off-diagonal blocks via
  `P_{R_s} Phi(s*(F_A)) P_{R_s}` etc. Anti-Hermitian (sp(64)-valued), so purely imaginary
  eigenvalues in the Riemannian sector.
- **Hidden curvature H^{(i)}:** Enter via the 4D spin connection sourced by torsion components
  `T^{(i)}` of the distortion `theta`. These are also zero-order multiplications.

**Application of the three subprincipal-symbol arguments from vz-subprincipal:**

**Argument 1 (Real principal type at 4D).** `D_GU^{4D}` is of real principal type
because `g_s(eta,eta) = 0` on the 4D null cone is a smooth quadric (non-degenerate
Lorentzian signature (3,1) of `g_s`) with first-order zeros. The Hormander propagation
theorem (Th. 23.2.4) applies to `S_{R_s}^{4D,full}`: WF sets of solutions propagate
along null bicharacteristics of `g_s(eta,eta)` regardless of `sigma_0(S_{R_s}^{4D,full})`.

**Argument 2 (No 4D sub-characteristics).** The principal symbol of `S_{R_s}^{4D,full}`
vanishes to first order on the 4D null cone. Dencker-Taylor sub-characteristics require
second-order zeros. First-order zeros are excluded by the exactness of
`c_s(eta)^2 = g_s(eta,eta) Id_S` (which means the null cone zero is of order exactly 1).

**Argument 3 (Shiab anti-Hermitian at 4D, so(3,1) connection).** The Shiab contribution
to `sigma_0(S_{R_s}^{4D,full})` is `P_{R_s} Phi(s*(F_A)) P_{R_s}`, which is sp(64)-valued
(anti-Hermitian in the quaternionic sense), giving purely imaginary eigenvalues over C.
The spin-connection term is so(3,1)-valued (pseudo-skew-symmetric), which can have real
eigenvalues in (3,1) signature but produces only amplitude effects (not new propagation
directions) for real-principal-type operators.

**The II_s subprincipal contribution: new analysis needed for F5.**

The second fundamental form term `P_{R_s}(II_s mixing) P_{R_s}` in `sigma_0(S_{R_s}^{4D,full})`
is a new ingredient not present in the 14D analysis. Explicitly:

```
(II_s subprincipal contribution) = P_{R_s}[sum_a c_s(e^a) II_s(e_a, .)^{index}] P_{R_s}
```

This is a real (symmetric) endomorphism of the RS sub-bundle, because `II_s` is a
real-valued normal-bundle tensor. In signature (3,1), this can have real eigenvalues.

**Is this a VZ risk?** The question is whether the real eigenvalues of this
endomorphism on the RS sub-bundle introduce new real characteristics.

**Answer: No.** The Hormander real-principal-type theorem applies regardless of whether
`sigma_0` has real or imaginary eigenvalues. The conclusion is:

```
WF set of solutions to S_{R_s}^{4D,full} Psi_R = 0 is invariant under the
Hamiltonian flow of g_s(eta,eta).
```

This is INDEPENDENT of the spectrum of `sigma_0`. Real eigenvalues of `sigma_0`
produce exponential growth or decay of the WKB AMPLITUDE along null rays (a stability
question), NOT new propagation directions (a causality question). VZ acausality would
require spacelike characteristics -- directions outside the null cone -- which requires
the principal symbol to have new zeros. The II_s subprincipal term cannot create these.

**Stability remark.** The real eigenvalues of the II_s subprincipal term mean that the
WKB amplitude along some null rays can grow or decay. This is relevant for the stability
of perturbations around a particular section `s`, but it is not a VZ causality issue.
A stable section (e.g., the totally geodesic LC section, where `II_s = 0`) has no
II_s subprincipal contribution and is amplitude-stable. Non-umbilic sections have
non-zero II_s and may have amplitude growth, but this is a dynamical selection effect
controlled by the Willmore variational principle, not an acausality.

### 3.6 The Classical VZ Lower-Order Mechanism at 4D

**Claim.** The classical VZ lower-order mechanism (Velo-Zwanziger 1969 §4) does not
apply in the 4D GU context, for the same structural reason as in 14D (vz-oq2-lower-order-curvature §7.3).

**The classical VZ lower-order mechanism requires:**

1. An RS field `psi_mu` with a standalone 4D RS Lagrangian.
2. An externally-imposed constraint `gamma^mu psi_mu = 0` derived from the E-L equations.
3. Acting with a differential operator on the constraint to derive a secondary equation.
4. The secondary equation's characteristics are determined by the curvature (`F_mu_nu` or
   `R_mu_nu`) inserted at the level of first-order terms.

**In the 4D GU situation:**

1. The RS field `Psi_R in Gamma(R_{4D})` is a SECTION of the sub-bundle `R_{4D} = ker Gamma^{4D}`,
   not a standalone field with its own Lagrangian.
2. The gamma-trace constraint `Gamma^{4D} Psi_R = 0` is the DEFINITION of the domain, not
   a derived E-L condition. It is satisfied identically for all `Psi_R in Gamma(R_{4D})`.
3. There is no secondary equation obtained by differentiating the constraint. The Schur
   complement `S_{R_s}^{4D,full}` is the full effective dynamics of the RS sector and already
   incorporates the constraint elimination.
4. The curvature terms (Weyl, Riemann, F_A, II_s) appear only in the zero-order part of
   `S_{R_s}^{4D,full}`, not in the first-order (principal-symbol) part. The classical VZ
   mechanism requires them to appear at first order in the secondary equation; this does not
   happen in the Schur complement formulation.

**Conclusion:** The classical VZ lower-order mechanism is structurally inapplicable in the
4D GU RS context.

### 3.7 Hidden Curvature Pieces H^(i): Explicit Check

The HC1 analysis (hc1-sl2c-bianchi-spinor-2026-06-23.md) identified three hidden curvature
pieces activated by the distortion torsion:

- `H^{(1)}`: SL(2,C) rep `(3/2,1/2) + (1/2,3/2)`, 16 real components, sourced by `T^{(1)}`.
- `H^{(2)}`: `(1/2,1/2)_V` (vector), 4 components, sourced by `T^{(2)}`.
- `H^{(3)}`: `(1/2,1/2)_A` (axial), 4 components, sourced by `T^{(3)}`.

**How H^(i) enter D_GU^{4D}:**

These enter via the torsion decomposition of the distortion `theta = A - Gamma`. After
section pullback, `s*(theta) = II_s` (second fundamental form) in the canonical Levi-Civita
gauge. The torsion pieces `T^{(i)}` of the distortion enter the 4D spin connection:

```
omega^{4D,theta}_a = omega^{4D,LC}_a + (T^{(i)} contributions)
```

This is a zero-order modification of the spin connection -- no new first-order terms
in `Psi` arise. The hidden curvature pieces `H^{(i)}` appear in `sigma_0(D_GU^{4D})` via
this modified spin connection, in the same way that the Weyl tensor and Riemann tensor do.

**The H^(i) are zero-order.** Explicitly: `H^{(i)} = (curvature sourced by T^{(i)})` enters
the connection `omega_a` as an additional algebraic coefficient. The connection term
`c_s(e^a) omega_a` is zero-order in `Psi` regardless of whether `omega_a` contains
`H^{(i)}` or not.

**No new VZ risk from H^(i).** The hidden curvature pieces do not change the first-order
(principal) symbol of `D_GU^{4D}`. They contribute to the subprincipal symbol, which (by
the three arguments in §3.5) does not introduce new real characteristics.

---

## 4. The F5 Verdict: Does Curvature Reintroduce VZ Acausality?

**Question.** After the principal-symbol VZ evasion (vz-schur §18, CONDITIONALLY_RESOLVED at 4D, constant-coefficient gauge) and
the subprincipal-symbol analysis (vz-subprincipal, CONDITIONALLY_RESOLVED), do the
curvature terms (Weyl tensor of g_Y, Riemann tensor of g_s, Sp(64) gauge curvature F_A,
second fundamental form II_s, hidden pieces H^(i)) reintroduce VZ acausality?

**Answer: No, at reconstruction grade.**

Three-level argument:

**Level 1 (Zero-order universality, §3.2).**
All curvature sources in D_GU^{4D} are zero-order operators in Psi. They multiply Psi
by pointwise endomorphisms (spin connection, Shiab coupling, II_s mixing, H^(i) torsion).
Zero-order operators do not contribute to the principal symbol. The principal symbol of
D_GU^{4D} is exactly `c_s(eta)`, with `c_s(eta)^2 = g_s(eta,eta) Id_S` (exact). No
curvature source can enlarge the characteristic cone beyond the null cone of g_s.

**Level 2 (Structural exclusion of classical VZ mechanism, §3.6).**
The GU RS sector is a sub-bundle, not a standalone field. The gamma-trace constraint
is domain-defining, not externally imposed. The Schur complement formulation does not
generate new first-order terms from zero-order curvature (in contrast to the classical
VZ subsidiary-condition differentiation, which does). The structural precondition for
the classical VZ lower-order mechanism is absent.

**Level 3 (Subprincipal symbol non-reintroduction, §3.5).**
The subprincipal symbol `sigma_0(S_{R_s}^{4D,full})` contains contributions from all
curvature sources (including the new 4D-specific II_s term and the H^(i) hidden pieces).
But by the three arguments from vz-subprincipal (real principal type, no sub-characteristics,
anti-Hermitian Shiab), none of these introduce new real characteristics beyond the null cone.
The II_s contribution may have real eigenvalues in (3,1) signature (a stability question)
but does not produce spacelike propagation.

**The propagation of singularities theorem (Hormander) then guarantees:** For the
pseudodifferential operator `S_{R_s}^{4D,full}` of real principal type, all singularities
of solutions propagate along null bicharacteristics of `g_s(eta,eta)`. This is unaffected
by any zero-order curvature correction, at all levels of the symbol expansion.

---

## 5. Failure Conditions

**F1.** If `II_s` contributes first-order derivative terms to the principal symbol of
`D_GU^{4D}` (i.e., if the OQ3-V1 zero-anomalous-normal-direction result is incorrect),
the principal symbol would change and the characteristic cone could enlarge. This would
require `c_s(eta)^2 != g_s(eta,eta) Id_S` -- falsified by the explicit horizontal
Clifford computation in §17-19 of vz-schur-complement.

**F2.** If the Gauss formula produces a first-order term (rather than zero-order) in
`D_GU^{4D}`, the Level 1 argument fails. This would require the Gauss formula
`R^{g_s} = s*(R^{g_Y}) + II_s^2` to generate a first-order differential operator
from the `II_s^2` term when substituted into the spin connection. But `II_s^2` is
a pointwise endomorphism (product of two zero-order fields), entering the connection
at zero order. The Gauss formula itself involves no derivatives of `Psi`.

**F3.** If `D_GU^{4D}` is not of real principal type (i.e., if the null cone of
`g_s` is degenerate), the Hormander theorem does not apply. This requires a degenerate
Lorentzian metric `g_s` (signature change). Excluded by construction: `s*(g_Y|_H)` is
a non-degenerate Lorentzian metric on `X^4` for any smooth embedding section `s`.

**F4.** If the normal-bundle curvature `F_A^{perp}` (from the Codazzi equation for
Sp(64)) introduces derivative terms in `Psi` when inserted into the Shiab, the OQ2-a
resolution fails at 4D. But `F_A^{perp}` is a background field (determined by the
Codazzi data, not by Psi). The Shiab `Phi(F_A^{perp} tensor Psi)` multiplies `Psi` by
a fixed endomorphism -- no derivative of `Psi` arises. This is the same argument as
OQ2-a (vz-subprincipal §4.2).

**F5 (genuine subtlety).** The split-signature of the full 14D gimmel metric `g_Y`
(signature (9,5)) can produce spin-connection terms in `sigma_0(D_GU^{14D})` with real
eigenvalues (so(9,5) is pseudo-skew-symmetric). After 4D section pullback, the 4D
spin connection is so(3,1)-valued (for the 4D Lorentzian signature). These may produce
amplitude growth along null rays (a stability question). However:
(a) Amplitude growth is not VZ acausality.
(b) For the LC section (`II_s = 0`), the spin-connection term is purely so(3,1)-valued
    and well-controlled in the EFT regime.
(c) The Willmore variational principle selects sections that minimize `|II_s|^2`,
    preferring sections with small (or zero) second fundamental form. The variational
    selection disfavors sections with large II_s that could produce large subprincipal
    amplitude growth.

This is not a failure of VZ evasion but a boundary on EFT stability, and it is
consistent with the physical requirement that the section `s` be a physically sensible
4D metric configuration.

---

## 6. Relation to vz-oq2-lower-order-curvature and vz-subprincipal

This file is best understood as the **4D integrated synthesis** of the two prior files:

| Prior file | Scope | Conclusion |
|---|---|---|
| vz-oq2-lower-order-curvature-2026-06-23.md | 14D curvature sources, principal symbol | Zero-order: no new characteristics |
| vz-subprincipal-symbol-rs-2026-06-23.md | 14D subprincipal symbol, OQ2-a/OQ2-b | No new characteristics at sub-leading level |
| **This file (vz-f5-curvature-check)** | **4D after section pullback: all curvature sources including II_s and H^(i)** | **Zero-order universality + structural VZ exclusion + subprincipal arguments: CONDITIONALLY_RESOLVED** |

The F5 file adds:
1. Explicit treatment of `II_s` and `H^(i)` at 4D (new ingredients absent from 14D analysis).
2. Explicit application of Gauss formula to confirm zero-order entry into spin connection.
3. II_s subprincipal analysis: real eigenvalues are a stability (not causality) question.
4. Integration with the codazzi-sp64 normal-bundle curvature (`F_A^{perp}`).

---

## 7. Tracking Status

| Curvature type | 14D order | 4D order (after pullback) | VZ risk |
|---|---|---|---|
| Weyl tensor W_{abcd} of g_Y/g_s | Zero | Zero (via spin connection) | None |
| Riemann tensor R_{abcd} of g_s | Zero | Zero (via spin connection) | None |
| II_s (second fundamental form) | -- (4D only) | Zero (index mixing) | None (amplitude only) |
| II_s^2 via Gauss formula | -- | Zero (in spin connection) | None |
| Sp(64) gauge curvature s*(F_A) | Zero | Zero (Shiab) | None |
| Normal-bundle curvature F_A^{perp} | Zero | Zero (Shiab) | None |
| Hidden curvature H^(i) (torsion-activated) | Zero | Zero (spin connection via T^{(i)}) | None |

All curvature terms: zero-order in Psi, no contribution to principal symbol,
subprincipal-symbol arguments confirm no new characteristics.

**Verdict: CONDITIONALLY_RESOLVED.**

Lower-order curvature terms (Weyl tensor of g_Y, Riemann tensor, gauge curvature F_A,
second fundamental form II_s, hidden curvature pieces H^(i)) do NOT reintroduce VZ
acausality after the principal-symbol evasion established in vz-schur-complement-2026-06-23.md.
VZ evasion is robust against all sub-leading curvature corrections in the GU Sp(64) bundle.

**Remaining condition for upgrade to VERIFIED:**
CAS verification of the explicit subprincipal symbol form (§3.5 is schematic); in particular,
the II_s subprincipal eigenvalue spectrum should be computed for the K3-type section to
confirm stability.

---

## 8. Open Questions

**OQ-F5-1.** Explicit spectrum of `sigma_0(S_{R_s}^{4D,full})` for the K3-type section
(Â=2, sigma=-16) selected by the GU Willmore principle. Are the real eigenvalues (from
II_s and so(3,1) spin connection) bounded, or do they grow with curvature scale? This
is a stability question (not VZ causality), but it is relevant for the EFT stability
of the 4D RS sector around the K3 section.

**OQ-F5-2.** The CPA-1 analysis (cpa1-tobs) established the ambient curvature correction
`+4/R^2` to the Lichnerowicz eigenvalue at reconstruction grade (needing explicit Y^{14}
curvature computation). If the ambient curvature correction is confirmed, the subprincipal
symbol at the S^4 section is computable from the explicit Weyl curvature of g_Y restricted
to the S^4 embedding. This would be a concrete CAS test.

**OQ-F5-3.** The hidden curvature pieces H^{(i)} depend on the torsion `T^{(i)}` of the
distortion `theta = A - Gamma`. At the LC section (`A = Gamma`, `theta = 0`), all `T^{(i)} = 0`
and all `H^{(i)} = 0`. This simplification means that for the LC section, the subprincipal
symbol is entirely determined by the visible curvature pieces (W, S_0, R) plus the Sp(64)
curvature F_A. The LC section is thus the most tractable case for an explicit CAS computation.

---

## 9. References

- `explorations/vz-schur-complement-2026-06-23.md` (VZ evasion at 14D and 4D; §17-19 for 4D)
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md` (S_R^2 != xi^2 Id clarification)
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` (14D curvature zero-order; OQ2 parent)
- `explorations/vz-subprincipal-symbol-rs-2026-06-23.md` (OQ2-a, OQ2-b subprincipal analysis)
- `explorations/codazzi-sp64-2026-06-23.md` (Codazzi for Sp(64); normal-bundle curvature)
- `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md` (H^(i) SL(2,C) labels)
- `explorations/ii-s-moving-frames-2026-06-23.md` (II_s explicit moving-frame computation)
- `explorations/ic3-nonlinear-conservation-2026-06-23.md` (IC3-nonlinear conservation; ambient Bianchi)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) signature (9,5))
- Hormander, L. (1985). _The Analysis of LPDOs III_, Ch. 23. (Propagation of singularities)
- Velo, G. and Zwanziger, D. (1969). Phys. Rev. 186:1337. (VZ theorem, classical lower-order mechanism)
- Dencker, N. (1982). J. Funct. Anal. 46, 351-372. (Sub-characteristics for real principal type systems)
- Gauss, C.F. (embedding formula for Riemann curvature; standard reference: do Carmo, _Riemannian Geometry_)
