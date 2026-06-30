---
title: "VZ1 OQ3: Gravitational Velo-Zwanziger — Weyl Tensor of the Gimmel Metric on Y^14"
date: 2026-06-23
problem_label: "vz1-oq3-gravitational-vz"
status: reconstruction
verdict: EVADED
---

# VZ1 OQ3: Gravitational Velo-Zwanziger via the Gimmel Weyl Tensor

## 1. Problem Statement

**What is being computed.** The Velo-Zwanziger theorem has two distinct triggers:

- **(VZ-gauge)** RS sector coupled to a non-trivial gauge field F_A != 0. This was the
  subject of the main VZ program (vz-schur, vz-oq1, vz-oq2, vz-subprincipal,
  vz-f5, vz-f6, vz-4d-eft): verdict EVADED (reconstruction) at both 14D and 4D.

- **(VZ-grav)** RS sector propagating in a curved spacetime background. Christodoulou
  (1970), Buchdahl (1962), and Fierz-Pauli (1939) showed that a spin-3/2 field in
  a generic curved background can exhibit causal pathologies from the curvature terms
  in the characteristic matrix, independent of any internal gauge coupling.

This file addresses **VZ-grav**: does the Weyl tensor W_{ABCD} of the gimmel metric
g_Y on Y^{14} introduce spacelike characteristics for the RS sector of D_GU, independent
of the Sp(64) gauge coupling?

**Why OQ3 of VZ1.** The original VZ1 analysis (`vz1-velo-zwanziger-analysis-2026-06-22.md`)
flagged three open questions:

- OQ1: Does the RS sector decouple from spin-1/2 at some scale?
- OQ2: If RS decouples, is there a guardian symmetry?
- **OQ3: Does the Weyl tensor of the gimmel metric produce gravitational VZ problems
  independent of gauge coupling?**

OQ1 and OQ2 were addressed through the gauge-VZ program (F1-F6). OQ3 is explicitly
gravitational and requires a separate analysis.

**Relevance.** VZ-grav fires differently from VZ-gauge:

- VZ-gauge: the curvature F_A of the internal connection deforms the constraint algebra
  of the RS field equation.
- VZ-grav: the spacetime curvature R_{ABCD} (specifically its Weyl part W_{ABCD})
  deforms the subsidiary condition propagation, because [D_A, D_B] Psi_C ~ W_{ABCD} Psi^D
  when acting on a vector-spinor in a curved background.

For a standalone RS field in a generic curved spacetime (no gauge coupling), the question
is precisely whether the algebraic symbol of the field equations has spacelike zeros.

**The GU setting.** In GU the RS sector is NOT a standalone field. Nevertheless OQ3
asks a structural question: does the Weyl curvature W_{ABCD} of g_Y on Y^{14} (the
gimmel metric) introduce new real characteristics in the RS sector of D_GU beyond the
null cone? This is independent of F_A; it would be present even in the pure-gravity
(zero gauge curvature) sector.

---

## 2. Established Context

Results this computation builds on.

**Geometry.** Y^{14} = Met(X^4), signature (9,5), gimmel metric g_Y. The gimmel metric
is constructed from the Frobenius metric on Sym^2(R^{3,1*}) (signature (7,3)) with
trace-reversal giving fiber (6,4), plus the Lorentzian base (3,1), total (9,5).
Moving-frame Christoffel symbols for g_Y are fully explicit from
`explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`: the H-H-H block = LC of g_s; the
H-H-V block = algebraic slice (-(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd}));
and the V-V-V block = fiber LC.

**Clifford algebra.** Cl(9,5) ~= M(64,H), S = H^{64}. Principal symbol satisfies
sigma_D(xi)^2 = g_Y(xi,xi) Id_S for all xi in T*Y^{14} (established, drives VZ evasion).
This identity is algebraic and does NOT depend on the curvature of g_Y.

**RS sector.** R^{14D} = ker Gamma^{14D} where Gamma^{14D}(psi) = gamma^A psi_A,
summed over all 14 frame directions. This is the kernel of the full 14D gamma trace.

**Curvature structure of g_Y.** The Weyl tensor W_{ABCD} of g_Y encodes the conformally-
invariant part of the Riemann tensor. From the gimmel construction on Y^{14} = Met(X^4):

- The horizontal-horizontal components W_{abcd} pull back to the Weyl tensor of g_s
  on X^4 after section pullback (CONDITIONALLY_RESOLVED, pc2-gauss-y14-curvature).
- The mixed H-V components W_{ab,ij} involve the algebraic slice Christoffel block.
- The vertical-vertical components W_{ijkl} involve the fiber LC of the Frobenius metric.

**Lower-order VZ mechanism.** The classical gravitational VZ mechanism (Christodoulou
1970; Buchdahl 1962): for a standalone spin-3/2 Psi_mu in curved spacetime with
metric g_{mu nu}, the subsidiary condition D^mu Psi_mu = 0 differentiates to give:

```
D^mu D_nu Psi^nu = D^mu D^nu Psi_nu ~ R_{mu nu} Psi^nu + W_{mu nu rho sigma} Psi^{rho sigma} + ...
```

The Weyl tensor appears in the integrability condition for the subsidiary constraints.
For this to introduce new real characteristics, the Weyl tensor must enter the
**principal symbol** of some derived operator, not merely as a lower-order term.

**Prior curvature analysis.** `explorations/vz-evasion/vz-oq2-lower-order-curvature-2026-06-23.md`
(OQ2) established that curvature terms in D_GU are **zero-order operators** (zero-order
in Psi, acting by multiplication). The conclusion: they cannot change the principal
symbol of S_R^{full}. The analysis there covered the Weyl tensor of g_Y, Riemann tensor,
gauge curvature F_A, and Shiab coupling. The gravitational OQ3 question asks whether the
gimmel Weyl tensor has any **special structure** that OQ2's general analysis might have
missed.

---

## 3. Computation

### 3.1 The Gravitational VZ Mechanism: Precise Statement

The gravitational VZ theorem (Fierz-Pauli obstruction in curved spacetime, reviewed by
Porrati 1993 hep-th/9304065; Deser-Waldron 2001) fires through the following chain:

**Step GV1.** Take a spin-3/2 field Psi_A (vector-spinor) satisfying the Rarita-Schwinger
equation in curved spacetime (g_Y metric, no gauge coupling):

```
(D_GU^{grav})_{RS} Psi_A = 0,    Gamma^{14D} Psi = gamma^A Psi_A = 0.
```

**Step GV2.** Act on the subsidiary condition Gamma^{14D} Psi = 0 with D^A:

```
D^A (gamma^B Psi_{AB}) = gamma^B D^A Psi_{AB} + [D^A, gamma^B] Psi_{AB}
                       = gamma^B D^A Psi_{AB} + R^A{}_B Psi_A (schematic).
```

The commutator [D^A, gamma^B] introduces curvature via the Clifford commutation relation.

**Step GV3.** For the Rarita-Schwinger equation to be consistent with the subsidiary
condition, the commutator term (containing the curvature) must be expressible in terms
of the original fields and their first derivatives without introducing a NEW first-order
differential operator acting on Psi. If the curvature contributes a new derivative
operator, its principal symbol adds to the characteristic determinant and potentially
introduces spacelike zeros.

**Step GV4 (Obstruction check).** The critical question: does the Weyl tensor
W_{ABCD} of g_Y enter Step GV3 at first-derivative order (as a coefficient of D_A Psi_B)
or at zero-derivative order (as a multiplicative curvature coupling to Psi_A)?

### 3.2 GU Structural Analysis

**Key structural feature of D_GU that differs from standalone RS.**

In GU, the RS "equation of motion" is not a standalone field equation Psi_A = 0 in
an external background g_Y. Instead, D_GU acts on the full spinor bundle E = T*Y^{14}
(x) S = T*Y^{14} (x) H^{64}, and the RS sector is the sub-bundle:

```
E_{RS} = R^{14D} (x) S_{non-RS} ⊂ E,
```

defined by the kernel of the full gamma trace. The "RS field equation" IS the D_GU
equation restricted to this sub-bundle via the Schur complement S_R^{eff}(xi).

The principal symbol of S_R^{eff} has been computed (vz-schur):

```
S_R^{eff}(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi),
```

where the blocks A, B, C, E come from the 14D Clifford algebra, NOT from a differential
equation for a standalone RS field in a curved background.

**The Weyl tensor enters only as a zero-order term in D_GU.**

The D_GU operator is:

```
D_GU = d_A + d_A* + Phi,
```

where d_A is the gauge-covariant exterior derivative, d_A* its adjoint, and Phi the
zero-order Shiab map. The curvature of the connection d_A enters the SQUARE of D_GU:

```
D_GU^2 = (d_A + d_A*)^2 + [d_A + d_A*, Phi] + Phi^2
        = delta_H + Weitzenbock(R_{g_Y}) + F_A + [d_A, Phi] + Phi^2.
```

The Weitzenbock curvature term is the Riemann tensor of g_Y acting algebraically on
the bundle E. In particular, the Weyl tensor W_{ABCD} enters D_GU^2 as:

```
[Weyl contribution to Weitzenbock] = W_{ABCD} c^A c^B c^C c^D
```

acting on sections of S -- this is a ZERO-ORDER (algebraic) operator, not first-order.

**Why the Weyl tensor cannot promote to first-order.**

The first-order operator D_GU = d_A + d_A* + Phi has principal symbol
sigma_1(D_GU)(xi) = c(xi), which is a Clifford multiplication operator. The Weyl
tensor enters D_GU only through the connection form omega^{AB} (the spin connection of
g_Y), and omega^{AB} is a one-form (zero-order in Psi, first-order in the metric g_Y).
The curvature R^{AB} = d omega^{AB} + omega^{AC} wedge omega_C^{\ B} is a two-form
valued in Lie algebra, and acts on sections of S as:

```
[D_A, D_B] psi = -R_{AB} psi = -(1/4) R_{ABCD} c^C c^D psi.
```

This is zero-order in psi. To get a first-order contribution to the characteristic
determinant from the curvature, one would need the curvature to appear as a COEFFICIENT
of a derivative of psi (i.e., in the form (R)_{...} D_E psi_F). Such terms DO appear
in the classical gravitational VZ mechanism for STANDALONE RS fields, where the
constraint propagation equation involves:

```
D^mu (D_mu Psi_nu - D_nu Psi_mu) = ... + W_{mu nu rho sigma} D^rho Psi^sigma + ...
```

(the Weyl tensor as coefficient of first derivatives of Psi). But in GU:

**The subsidiary condition is NOT propagated by an external operator.**

In the classical gravitational VZ analysis, one takes the divergence of the RS equation
to enforce the subsidiary condition D^mu Psi_mu = 0, generating a new equation that
contains curvature-times-derivative terms. The characteristic matrix of THIS derived
equation can have spacelike zeros.

In GU, the RS subsidiary condition (gamma-trace constraint) is built into the domain
definition of D_GU. The RS sub-bundle E_{RS} = ker Gamma^{14D} is defined BEFORE the
dynamics. The Schur complement S_R^{eff} is the restriction of the symbol to this
sub-bundle. No external differentiation of a constraint is performed; the constraint
is structural.

This is the same argument as OQ2 (vz-oq2-lower-order-curvature) but applied specifically
to the gravitational sector.

### 3.3 Explicit Gimmel Weyl Tensor Analysis

**Claim GVZ-1:** The principal symbol sigma_1(D_GU) = c(xi) contains NO Weyl tensor
contribution.

**Proof.** The principal symbol of a first-order differential operator D = sum_A gamma^A D_A
is determined solely by the leading-derivative part: sigma_1(D)(xi) = i gamma^A xi_A = c(xi).
The connection coefficients omega^{AB}_C in D_A = partial_A + (1/4) omega^{AB}_A c_B c_C
contribute only to lower-order terms (zero-order in Psi). The principal symbol is
connection-independent. QED.

**Claim GVZ-2:** The Weyl tensor W_{ABCD} of g_Y contributes to D_GU^2 as a zero-order
operator (Weitzenbock term), not as a first-order operator.

**Proof.** By the Lichnerowicz-Weitzenbock formula for Dirac operators on a Clifford
module (Lawson-Michelsohn, Spin Geometry §II.8):

```
D_GU^2 = nabla*nabla + R/4 + F_A + [lower order],
```

where R/4 is the scalar curvature term. The full Riemann tensor contribution (including
Weyl) acts on the spinor module via:

```
nabla*nabla section - Delta_{rough} section = (1/4) R_{ABCD} c^A c^B c^C c^D section.
```

This is a zero-order (algebraic) coupling. In particular:

- The Weyl tensor W_{ABCD} enters as (1/4) W_{ABCD} c^A c^B c^C c^D, a zero-order operator.
- The Ricci tensor contributes R_{AB} c^A c^B / 2, also zero-order.
- The scalar curvature contributes R/4 (scalar multiplication).

None of these are first-order operators. QED.

**Claim GVZ-3:** The characteristic cone of S_R^{eff}(xi) is the null cone of g_Y,
even when g_Y has nonzero Weyl curvature.

**Proof.** From GVZ-1 and GVZ-2: the principal symbol sigma_1(D_GU)(xi) = c(xi) is
the sole first-order component. The Schur complement S_R^{eff}(xi) = A(xi) - B(xi)
E(xi)^{-1} C(xi) is built entirely from c(xi) and its contractions. The key identity:

```
c(xi)^2 = g_Y(xi,xi) Id_S
```

is an algebraic identity of the Clifford algebra Cl(9,5) ~= M(64,H). It holds for ALL
xi in T*Y^{14} regardless of the curvature of g_Y. In particular it holds even when
W_{ABCD} != 0.

By the vz-schur §8 argument: if S_R^{eff}(xi) psi_R = 0, then the block-inversion
gives A c(xi)^2 psi_R = g_Y(xi,xi) psi_R (via identities (I)+(II) of that document).
When g_Y(xi,xi) != 0, this forces psi_R = 0. The characteristic cone (where S_R^{eff}
is non-invertible) = null cone of g_Y.

This argument uses only the algebraic Clifford identity, not the specific form of g_Y.
The Weyl tensor of g_Y does not enter the algebraic Clifford identity and therefore
cannot change the characteristic cone. QED.

### 3.4 The Gravitational VZ Mechanism Does Not Apply: Structural Argument

The classical gravitational VZ mechanism requires:

1. A standalone RS field Psi_A in an external background metric g_{mu nu}.
2. A subsidiary condition D^mu Psi_mu = 0 that is imposed EXTERNALLY (not built into the
   field equation domain).
3. Differentiation of (2) using the field equation (1) to derive a new equation whose
   characteristic matrix involves curvature-times-derivative terms.

In GU none of these three conditions hold for the RS sector:

**(H1 fails)** The RS sector in GU is NOT a standalone field. It is defined as the
kernel of the gamma trace within the D_GU domain: R^{14D} = ker Gamma^{14D}. The spin-3/2
nature of the RS sector is an intrinsic structural feature of the Clifford module, not a
separate field placed in a background geometry.

**(H2 fails)** The subsidiary condition is structural (domain-defining), not external.
There is no separate imposition of Gamma^{14D} Psi = 0 as a Lagrange multiplier or
external constraint. The RS sub-bundle is the gammatrace kernel in the spinor bundle.

**(H3 fails)** Since there is no external subsidiary condition to differentiate, the
classical Step GV2-GV3 chain does not produce new first-order derivative terms with
Weyl tensor coefficients. The curvature enters D_GU only as zero-order (Weitzenbock)
terms by GVZ-2.

**Conclusion.** The gravitational VZ mechanism does not apply to the RS sector in GU.
The obstruction conditions H1, H2, H3 (in the gravitational variant) are all absent.

### 3.5 Section-Pullback Gravitational Analysis

After section pullback s: X^4 -> Y^{14}, the RS sector becomes R_s = ker Gamma^{4D}
(established in vz-schur §17-19, OQ3-V3 RESOLVED). The 4D effective RS operator
S_{R_s}^{4D} inherits:

```
sigma_{s*(D_GU)}(eta)^2 = g_s(eta,eta) Id_{E_s}    for all eta in T*X^4.
```

The Weyl tensor of g_s (= Weyl tensor of the induced 4D metric on X^4) enters the 4D
version of the Weitzenbock identity. By the same arguments as GVZ-1 through GVZ-3:

- It contributes only zero-order terms to s*(D_GU).
- The characteristic cone of S_{R_s}^{4D} = null cone of g_s.
- The 4D gravitational VZ mechanism does not apply for the same structural reasons.

**Special structure of the gimmel Weyl tensor at 4D.** The 4D section pullback projects
the Y^{14} Weyl tensor as:

```
s*(W_{g_Y}) = W_{g_s} + mixed H-V terms + normal-bundle terms.
```

From the Codazzi/Gauss machinery (codazzi-sp64, pc2-gauss-y14-curvature):

- The purely horizontal pieces = Weyl tensor of g_s (the 4D spacetime).
- The H-V mixed pieces contain II_s (second fundamental form) -- these contribute
  ZERO-ORDER to s*(D_GU) by the Gauss formula (II_s is a normal-bundle valued 2-tensor,
  its Clifford action on E_s is zero-order).
- The normal components become KK scalar fields, not RS fields, so they do not affect
  the RS characteristic cone.

The Weyl tensor of g_s on X^4 can in principle be non-zero (e.g., for gravitational
waves or black hole spacetimes). The above argument shows this does not cause VZ
acausality for the GU RS sector.

**GU vs. standalone gravitino.** For comparison: in N=1 supergravity, the gravitino
(spin-3/2, gauge field under local SUSY) propagates causally because local supersymmetry
maintains the subsidiary conditions. The GU RS sector achieves causal propagation by a
DIFFERENT mechanism: the RS sub-bundle is the Clifford kernel of a first-order operator
whose principal symbol satisfies sigma^2 = g(xi,xi) Id. This is a purely algebraic,
representation-theoretic evasion -- it does not require local supersymmetry or any special
property of the background Weyl tensor.

### 3.6 K3-type Background: Explicit Check

On the GU-selected K3-type background (oq3a-gu-variational-k3), X^4 has:

- W_{g_s} = Weyl tensor of K3 metric (nonzero in general -- K3 is not conformally flat).
- Ric(g_s) = 0 (Ricci-flat, Yau).
- R(g_s) = 0 (scalar curvature = 0).

On a Ricci-flat 4-manifold, the Weitzenbock formula gives:

```
D_{4D}^2 = nabla*nabla + (1/4) W_{g_s,abcd} c^a c^b c^c c^d.
```

The Weyl term (1/4) W_{abcd} c^a c^b c^c c^d acts on S = H^{64}. Its eigenvalues
determine the mass spectrum of spin-3/2 modes (not their propagation cone). The
characteristic cone argument (GVZ-3) is unaffected: the cone remains the null cone
of g_s regardless of the Weyl eigenvalue magnitude.

**An explicit eigenvalue estimate.** For K3, the Weyl tensor satisfies |W|^2 = O(1/R_K3^4)
where R_K3 is the typical K3 size. The Weyl contribution to D_{4D}^2 contributes a mass
term of order m^2 ~ |W|/R_K3 ~ 1/R_K3^3 for a K3-scale feature. This is subleading
compared to the KK mass m_RS^2 ~ 1/R_s^2 from the discrete-series spectrum (rc3-delta-n):
since R_s ~ R_K3 (both are the compactification scale), 1/R_K3^3 << 1/R_K3^2, so the
Weyl correction to the mass is a small perturbation, not a new characteristic direction.

In summary: the K3 Weyl tensor perturbs the RS mass spectrum but does not shift the
characteristic cone; gravitational VZ does not fire on K3.

---

## 4. Result

**Verdict: EVADED (reconstruction)**

The Weyl tensor of the gimmel metric on Y^{14} does NOT produce gravitational
Velo-Zwanziger causality problems for the RS sector, independent of gauge coupling.

**Main argument (three legs):**

1. **(Algebraic, verified)** The principal symbol sigma_1(D_GU)(xi) = c(xi) is
   connection-independent and satisfies c(xi)^2 = g_Y(xi,xi) Id_S identically as a
   Clifford algebra relation. The Weyl tensor does not enter this identity. Therefore
   the characteristic cone of D_GU -- and of S_R^{eff}(xi) -- is the null cone of g_Y
   regardless of the Weyl tensor value. (GVZ-1, GVZ-3, exact.)

2. **(Structural, reconstruction)** The classical gravitational VZ mechanism requires
   a standalone RS field with an externally imposed subsidiary condition. In GU all three
   structural preconditions (H1: standalone field, H2: external subsidiary, H3: constraint
   differentiation) fail. The RS sub-bundle is domain-defining (structural), not dynamical
   in the VZ sense. (Section 3.4, reconstruction.)

3. **(Curvature zero-order, reconstruction)** The Weyl tensor enters D_GU only via
   the Weitzenbock identity in D_GU^2, as a zero-order algebraic multiplication operator.
   It cannot promote to first-order via the Rarita-Schwinger constraint propagation chain
   because that chain presupposes a standalone constraint structure absent in GU. (GVZ-2,
   reconstruction.)

**Section-pullback preserves evasion.** After 4D section pullback s: X^4 -> Y^{14},
the 4D induced metric g_s can have nonzero Weyl tensor (e.g., for K3 or gravitational
wave backgrounds). The same three-leg argument applies at 4D, with II_s contributing
only zero-order Gauss corrections (confirmed: vz-schur §17-19, F5). The 4D gravitational
VZ evasion is at reconstruction grade.

**Relationship to gauge-coupling VZ evasion.** The gravitational and gauge-coupling
evasions share the same algebraic root: the Clifford identity c(xi)^2 = g_Y(xi,xi) Id_S.
This identity is insensitive to both the gauge curvature F_A (enters as zero-order via
[D_A, D_B] = -F_A) and the spacetime curvature W_{ABCD} (enters as zero-order via
Weitzenbock). Both types of curvature have the same status with respect to the principal
symbol: they are zero-order perturbations of a first-order operator whose symbol is
governed entirely by the Clifford algebra.

The evasion is therefore uniform across both VZ variants (gauge and gravitational), and
the mechanism is purely algebraic.

---

## 5. Explicit Failure Conditions

The gravitational VZ evasion fails if any of the following hold:

**F1** (Standalone RS sector). At some energy scale, the RS sector becomes a standalone
field in 4D with its own Lagrangian and the subsidiary condition Gamma Psi = 0 is
imposed as an external Lagrange multiplier (not built into the D_GU domain). This would
re-activate H1/H2/H3 and reopen gravitational VZ via the classical chain. Current
vz-4d-eft and vz-f6 computations show this does not happen (B/C coupling is O(1) and
kinematic), but it is the primary falsification target.

**F2** (Hidden first-order Weyl coupling). The gimmel metric g_Y has a special geometric
property causing the Weyl tensor W_{ABCD} to enter D_GU at first-order (as a coefficient
of D_A Psi_B), rather than zero-order. This could happen via an unusual gauge choice or
frame anomaly. Falsification test: compute D_GU^2 in an explicit frame on Y^{14} and
verify no W(xi) d/dxi type terms appear in the principal symbol. (CAS-grade computation.)

**F3** (Characteristic cone deformation by nonlinear curvature). At very high curvature
(near the Planck scale or in the K3 large-Weyl-tensor regime), nonlinear curvature effects
could deform the Clifford identity. In perturbative GR this does not occur (the Clifford
identity is representation-theoretic, not dynamical), but in a full quantum gravity theory
the metric could fluctuate and deform Cl(9,5). Falsification test: quantum corrections to
c(xi)^2 = g(xi,xi) Id_S.

**F4** (RS decoupling in gravitational sector). If the gravitational sector (no F_A)
produces a KK mass gap separating the RS sector, the low-energy EFT RS field could become
effectively standalone in a curved background (without gauge coupling) and gravitational
VZ would re-apply. Current rc3-delta-n and vz-4d-eft analyses show no such window, but
this remains a structural check at reconstruction grade.

**F5** (Weyl curvature enters gamma-trace constraint). If the gamma-trace constraint
Gamma^{14D} Psi = 0 is not exactly preserved by D_GU evolution (i.e., [D_GU, Gamma^{14D}]
contains a Weyl tensor contribution proportional to a differential operator), then the
RS sub-bundle is not preserved under evolution and a new effective standalone RS equation
with Weyl coupling emerges. Falsification test: compute [D_GU, Gamma^{14D}] explicitly
and verify it is zero-order in Psi.

---

## 6. Computation of [D_GU, Gamma^{14D}]: F5 Verification

**Claim GVZ-4:** [D_GU, Gamma^{14D}] is a zero-order operator (no first-order derivative
of Psi).

**Computation.** Let Gamma^{14D} = gamma^A partial_A (the gamma-trace operator), where
partial_A means contraction of the vector index with gamma^A. For the principal symbol:

```
sigma_1([D_GU, Gamma^{14D}])(xi) = [c(xi), Gamma^{14D,symbol}(xi)].
```

But Gamma^{14D} = gamma^A e_A is a ZERO-ORDER operator (it contracts the vector index of
a spinor-1-form with gamma matrices -- no derivative acts on Psi). Therefore its principal
symbol is zero, and the commutator [D_GU, Gamma^{14D}] has its first-order principal
symbol equal to [c(xi), 0] = 0.

More precisely: Gamma^{14D}: Gamma(T*Y tensor S) -> Gamma(S) is defined by

```
(Gamma^{14D} Psi)^alpha = g^{AB} gamma_A^{alpha beta} Psi_B^beta.
```

This uses the METRIC g^{AB} and the gamma matrices, but no derivative. The commutator
[D_GU, Gamma^{14D}] acting on Psi produces:

```
[D_GU, Gamma^{14D}] Psi = D_GU(gamma^A Psi_A) - gamma^A D_GU Psi_A.
```

The first-order terms cancel (D_GU is first-order and Gamma is zero-order; [first, zero] =
first-order term from Leibniz minus the same term = 0 at the symbol level). The remaining
commutator is zero-order, involving:

```
[nabla_B, g^{AB}] gamma_A Psi = (nabla_B g^{AB}) gamma_A Psi,
```

which is zero by metric compatibility (nabla g = 0 for the Levi-Civita connection of g_Y).
There may be a torsion correction if nabla is not the LC connection, but in the GU
distortion setup theta = A - Gamma, the relevant connection for the symbol computation
is the LC connection (torsion-free), confirming nabla_B g^{AB} = 0.

**Conclusion:** [D_GU, Gamma^{14D}] is a zero-order curvature/torsion operator. It does
NOT contain W_{ABCD} as a coefficient of a first-order derivative. F5 is satisfied:
the gamma-trace RS sub-bundle is preserved under D_GU evolution up to zero-order
(algebraic) curvature corrections. These corrections shift the RS mass spectrum but
not the characteristic cone.

**Implication for gravitational VZ.** Since [D_GU, Gamma^{14D}] is zero-order, the
RS sub-bundle is preserved under propagation of singularities (Hormander, real principal
type): singularities in the RS sector propagate along null bicharacteristics of c(xi),
which are the null geodesics of g_Y. No Weyl-tensor curvature escapes into the RS
characteristic cone via the commutator route.

---

## 7. Open Questions

**OQ-GVZ-1** (CAS verification of [D_GU, Gamma^{14D}]). The explicit computation in
Section 3.6 is at reconstruction grade. A CAS computation in an explicit local frame on
Y^{14} using the gimmel Christoffel symbols from ii-s-moving-frames would upgrade F5
from reconstruction to verified.

**OQ-GVZ-2** (Quantum corrections to Clifford identity). Whether c(xi)^2 = g_Y(xi,xi) Id_S
receives quantum corrections in a UV completion of GU is not addressed here. This is a
question about the quantum gravity sector, not the classical GU framework. It is unlikely
to affect the classical VZ analysis but is named for completeness.

**OQ-GVZ-3** (Comparison to gravitino in d=11 supergravity). The gravitino in 11D
supergravity propagates causally in curved backgrounds because of local supersymmetry.
Whether the GU RS evasion (Clifford-algebraic) and the SUGRA gravitino evasion (local
SUSY) are equivalent or structurally distinct as gravitational VZ evasion mechanisms
remains to be analyzed. Both evade the classical gravitational VZ constraint but possibly
via distinct algebraic routes.

**OQ-GVZ-4** (Nonlinear curvature at large |W|). For very large Weyl curvature (e.g.,
near a Schwarzschild singularity), the Weitzenbock mass term (1/4) W_{ABCD} c^A c^B c^C c^D
could become comparable to the kinetic term. Whether this produces amplitude instabilities
(as opposed to acausality) is an open question in the stability sector. This does not
threaten VZ evasion (causality is protected by the Clifford identity) but may be relevant
for the GU section-selection Willmore energy.

---

## 8. Summary

| Property | Value | Grade |
|---|---|---|
| Gravitational VZ fires for standalone RS in curved spacetime | YES (classical result) | verified |
| GU RS sector is standalone | NO (Clifford kernel, structural) | reconstruction |
| External subsidiary condition present | NO (domain-defining) | reconstruction |
| Weyl tensor enters D_GU principal symbol | NO (zero-order only) | reconstruction |
| [D_GU, Gamma^{14D}] contains first-order Weyl term | NO (zero-order, F5) | reconstruction |
| Characteristic cone of S_R^{eff} = null cone of g_Y | YES (Clifford algebra, exact) | verified |
| 4D gravitational VZ after section pullback | EVADED (same mechanism) | reconstruction |
| GU RS sector causal propagation on K3 | EVADED (Weyl mass perturbation only) | reconstruction |

**Grade:** reconstruction. The algebraic core (Clifford identity, principal symbol) is
at verified grade. The structural arguments (standalone failure, commutator structure)
are at reconstruction grade, requiring explicit frame computation for upgrade.

**VZ1 OQ3 answered:** The Weyl tensor of the gimmel metric on Y^{14} does NOT produce
gravitational VZ causality problems for the RS sector independent of gauge coupling.
The evasion is structural and algebraic, sharing its root (c(xi)^2 = g(xi,xi) Id)
with the gauge-coupling evasion. Both VZ variants are evaded by the same Clifford-algebra
identity, which is curvature-independent.
