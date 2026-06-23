---
title: "OQ-RS-3: GU Rarita-Schwinger Sector vs. Vasiliev Higher-Spin Gauge Theory"
date: 2026-06-23
problem_label: "oq-rs3-gu-vasiliev-comparison"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# OQ-RS-3: GU RS Sector vs. Vasiliev Higher-Spin Gauge Theory

## Problem Statement

Vasiliev higher-spin gauge theory is the only known consistent framework for interacting
spin >= 2 fields in four dimensions. GU contains a spin-3/2 (Rarita-Schwinger) sector
embedded in D_GU as the gamma-trace sub-bundle of the Clifford spinor module S = H^64
over Y^14. The question: is GU's VZ evasion mechanism (principal-symbol collapse via the
Clifford identity c(xi)^2 = g_Y(xi,xi) Id) a special case of Vasiliev's framework, or
a genuinely new mechanism?

The failure condition for distinctness: if GU's principal-symbol structure is equivalent
to a special case of Vasiliev's construction at some truncation order N, the VZ evasion
claim loses novelty and GU's RS sector is subsumed by known higher-spin theory.

This exploration is the P53-NOVEL object identified in
`explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md` and named as a remaining
open item in `explorations/vz-14d-mixed-covectors-2026-06-23.md` (OQ-RS-3).

---

## Established Context

The following are load-bearing inputs from prior exploration files:

**VZ evasion (EVADED at principal-symbol level):** `explorations/vz-14d-mixed-covectors-2026-06-23.md`
and `explorations/vz-e-block-direct-clifford-2026-06-23.md`. The effective RS principal
symbol S_R^{14D}(xi) satisfies A * S_R = xi^2 * Id_R for all non-null xi, where xi^2 =
g_Y(xi,xi) and the identity follows from the Clifford algebra Cl(9,5) = M(64,H).

**RS sector definition:** `explorations/vz-schur-complement-2026-06-23.md`. The RS sector
R^{14D} = ker(Gamma^{14D}) in S = H^64, where Gamma^{14D} = sum_{A=1}^{14} e^A otimes
c(e_A): this is the gamma-trace with respect to all 14 frame directions of Y^14. The RS
sector is the gamma-traceless part of the vector-spinor subspace. dim_R(R^{14D}) = 3328.

**Generation count (CONDITIONALLY_RESOLVED):** `explorations/oq3b-rs-index-closed-2026-06-23.md`.
RS sector contributes ind_H(D_RS) = 8 H-lines = 1 SM generation, via the APS route on
compact K3: ind_H = hat{A}(K3) * rank_H(S_RS^+) + eta/2 = 2*4 + 0 = 8.

**4D RS content:** RS(3,1) tensor S(6,4), where RS(3,1) is the spin-3/2 representation of
Spin(3,1) and S(6,4) = C^16 carries SM quantum numbers (Pati-Salam: (4,2,1) + (4bar,1,2)).

**Sp(64) gauge group:** Anomaly-free, pseudoreal, dim sp(64) = 8256. The RS sector is not
independently coupled to Sp(64); it is part of the full spinor module acted on by Sp(64)
via the fundamental representation on H^64.

---

## Computation

### Axis 1: Propagation Structure

**GU RS:**
The RS sector of D_GU propagates on the null cone of g_Y, the gimmel metric of signature
(9,5) on Y^14. Concretely, the principal symbol of D_GU restricted to the RS subspace
satisfies A * S_R^{14D}(xi) = g_Y(xi,xi) * Id_{R^{14D}} for an auxiliary operator A
(established in vz-14d-mixed-covectors). The characteristic variety is:

  Char(D_GU|_RS) = {xi in T*Y^14 : g_Y(xi,xi) = 0}

This is the null cone of the (9,5) metric. Causality of the RS sector is inherited
from the Clifford identity c(xi)^2 = g_Y(xi,xi) * Id, which is an algebraic identity in
Cl(9,5) = M(64,H) that holds regardless of connection, curvature, or background field.
The VZ problem (characteristic variety exiting the light cone for spacelike xi) EVADED
precisely because g_Y(xi,xi) > 0 for spacelike xi forces S_R^{14D}(xi) to have trivial
kernel. [See vz-e-block-direct-clifford-2026-06-23.md, EVADED.]

**Vasiliev RS:**
Vasiliev's equations for massless spin-3/2 fields are formulated on an AdS_4 background
(anti-de Sitter space with cosmological constant Lambda < 0) with vierbein e_0^a and
Lorentz connection omega_0^{ab} satisfying the AdS_4 background equations. The linearized
Fronsdal equation for a massless spin-3/2 field in AdS_4 is:

  (nabla^{AdS})^2 psi_mu - (3/2) nabla_mu nabla^nu psi_nu + ... + (3/4) Lambda psi_mu = 0

The characteristic variety of the linearized Fronsdal equation on AdS_4 is determined by
the AdS background metric g_{AdS}, giving:

  Char(Fronsdal_{3/2}) = {xi in T*AdS_4 : g_{AdS}(xi,xi) = 0}

This is the null cone of the AdS_4 metric. At the linearized level, Vasiliev's RS sector
is causal for the same formal reason (null-cone characteristic variety).

**Comparison on Axis 1:**
Both GU and Vasiliev give causal RS propagation with characteristic variety = null cone.
However, the mechanisms and causal structures differ:

(1a) GU: causality follows from Cl(9,5) algebraic identity on Y^14 (14-dimensional,
     signature (9,5), fiber-bundle over X^4). The causal structure is that of the
     14D TOTAL SPACE, not of the 4D base X^4.

(1b) Vasiliev: causality holds on AdS_4 (4-dimensional with negative constant curvature).
     AdS_4 has a different causal structure from Minkowski space M^4: timelike geodesics
     are complete, but AdS_4 has a conformal boundary; the causal diamond at the center
     of AdS_4 is compact. Notably, AdS_4 can be foliated by spacelike slices that do NOT
     reach the conformal boundary, and the RS propagator can reflect off the AdS boundary
     in ways that Minkowski RS propagation cannot.

(1c) Dimensional reduction: GU's 4D RS propagation (after section pullback s: X^4 -> Y^14)
     propagates on (X^4, g_{s}) where g_s is the pullback Lorentzian metric. If X^4 is
     asymptotically flat (or dS, or AdS), the causal structure of the GU RS sector on X^4
     differs from Vasiliev's AdS_4 RS sector in the same way that Minkowski/flat spacetime
     differs from AdS_4. Specifically:
     - AdS_4 requires Lambda < 0 as a structural input to Vasiliev's construction.
     - GU does NOT require Lambda < 0 for any of its RS sector's basic properties.
       The VZ evasion mechanism works for any non-null g_Y(xi,xi), irrespective of
       the cosmological constant.

**Axis 1 verdict:** Propagation structures are formally analogous (both null-cone causal)
but the ambient geometry is genuinely different: GU operates on a 14D fiber bundle without
a cosmological constant constraint; Vasiliev requires AdS_4 background. Non-trivial
distinction at the geometric level.

---

### Axis 2: Coupling Structure

**GU RS coupling:**
The RS sector of D_GU couples to the spin-1/2 sector through the Leibniz product rule.
Concretely, the off-diagonal block D_{RS,1/2} of D_GU (in the RS/spin-1/2 decomposition of
S = H^64) is nonzero BY CONSTRUCTION: the RS sector is defined as the Leibniz cross-term
in D_GU's action on Y = V + W (where V is the horizontal/spacetime factor and W is the
vertical/fiber factor). See vz1-62-persona-steelman-hegelian-2026-06-22.md, P46/P52.

The coupling of the RS sector to the Sp(64) gauge field is kinematic: the Sp(64) connection
acts on the FULL spinor module H^64 simultaneously, with no independently specified coupling
constant for the RS sector. The "gauge coupling" of the RS sector to Sp(64) is exactly the
restriction of the Sp(64) fundamental representation to the RS subspace of H^64. There is no
free parameter g_{RS}: the coupling is fixed by the Clifford geometry.

The Schur-complement computation (vz-schur-complement-2026-06-23.md) gives the effective
RS operator:

  D_RS^{eff} = D_{RS,RS} - D_{RS,1/2} * (D_{1/2,1/2})^{-1} * D_{1/2,RS}

The principal symbol of D_RS^{eff} satisfies the Clifford identity (shown via the E-block
computation in vz-14d-mixed-covectors). The coupling term D_{RS,1/2} contributes to the
Schur complement but does NOT move the characteristic variety off the null cone.

**Vasiliev RS coupling:**
Vasiliev's higher-spin gauge theory uses the higher-spin algebra hs(lambda), which is a
deformation (controlled by parameter lambda) of the algebra of differential operators on
the 2-sphere S^2 (the spinor-helicity space in 4D). For spin-3/2, the coupling in Vasiliev
is through "consistent cubic vertices" -- the lowest-order nontrivial interaction in the
higher-spin action is cubic (linear vertex x linear field x linear field), not quadratic.

The Vasiliev master field W (a 1-form on spacetime valued in hs(lambda)) encodes all spins
simultaneously. The spin-3/2 field is not independently coupled with a free parameter;
instead, it couples with coupling strength determined by the hs(lambda) algebra structure
constants. These structure constants depend on lambda.

The consistent cubic vertices for spin-3/2 in AdS_4 were constructed by Fronsdal (1978)
and extended by Vasiliev to the fully nonlinear interacting theory. The cubic vertex for
spin-(1/2 + 1 + 3/2) -- i.e., spin-1/2 tensored with a spin-1 gauge boson, giving spin-3/2
-- has a specific coefficient determined by the hs(lambda) algebra.

**Comparison on Axis 2:**
Both theories couple the RS sector to lower-spin fields without a free RS-specific coupling
constant. But the mechanisms are structurally different:

(2a) GU: the RS coupling arises from the LEIBNIZ PRODUCT RULE of a Dirac operator on a
     14D fiber bundle. The coupling D_{RS,1/2} is intrinsic to the Dirac-DeRham complex on
     Y^14 and requires no background specification beyond the Clifford geometry of Cl(9,5).

(2b) Vasiliev: coupling arises from cubic vertices in AdS_4 with coefficients fixed by the
     hs(lambda) algebra. The algebra hs(lambda) is itself a deformation parameter-dependent
     object: different lambda give non-isomorphic higher-spin algebras, and specific values
     of lambda (e.g., lambda = 1/2 for minimal bosonic model; lambda = 1/4 for A-type model)
     correspond to specific boundary CFTs via AdS/CFT.

(2c) Crucially: GU's coupling is BACKGROUND-INDEPENDENT in the sense that it does not
     require an AdS_4 background or a cosmological constant. The Leibniz product rule works
     for any Lorentzian metric g_s on X^4 (pulled back via s: X^4 -> Y^14). Vasiliev's
     cubic vertices are ON-SHELL consistent only in AdS_4; the vertex coefficients are
     AdS-curvature-dependent.

**Axis 2 verdict:** Both theories have geometrically-fixed (not freely-chosen) RS coupling.
GU's coupling is background-independent (Leibniz rule on Y^14); Vasiliev's is AdS-dependent
(cubic vertices in hs(lambda)). This is a structurally significant difference: GU can
accommodate asymptotically flat, dS, or general X^4 spacetimes; Vasiliev requires AdS_4.

---

### Axis 3: Gauge Symmetry

**GU gauge symmetry:**
The GU gauge group is Sp(64) = U(64,H), acting on S = H^64 via the fundamental quaternionic
representation. The RS sector, as a subspace of H^64, transforms under the restriction of
the Sp(64) fundamental representation to R^{14D} subset H^64.

There is NO local gauge symmetry specific to the RS sector in GU at the level currently
established. The Sp(64) gauge transformations act on all of H^64 and do not preserve R^{14D}
as a subspace (the RS constraint ker(Gamma^{14D}) is not preserved by arbitrary Sp(64) gauge
transformations because Gamma^{14D} involves the Clifford frame {e^A} which is not
Sp(64)-invariant).

The proposed "super-IG algebra" (OQ2 in the VZ analysis) would provide a local gauge
symmetry specific to the RS sector (analogous to local SUSY for the gravitino), but this
algebra has not been constructed. OQ2 remains OPEN.

**Vasiliev gauge symmetry:**
Vasiliev's theory has the higher-spin gauge algebra hs(lambda) as its gauge symmetry.
For a spin-3/2 field specifically, the gauge transformation is:

  delta psi_mu = nabla_mu epsilon

where epsilon is a local spin-1/2 (Dirac spinor) gauge parameter and nabla is the
AdS_4-covariant derivative. This is the same form as local SUSY (the gravitino gauge
transformation in SUGRA is delta psi_mu = nabla_mu epsilon for local SUSY parameter epsilon).

In the FULL nonlinear Vasiliev theory, the spin-3/2 field is part of the master field W,
and the gauge symmetry is the full higher-spin algebra hs(lambda), which contains the
spin-3/2 generator at the appropriate level.

**Comparison on Axis 3:**
This axis reveals the most significant structural gap between GU and Vasiliev:

(3a) Vasiliev has a local gauge symmetry for the RS field (delta psi_mu = nabla_mu epsilon),
     which is the analogue of local SUSY and is the standard "guardian symmetry" that prevents
     VZ acausality in SUGRA. GU does NOT currently have such a local RS-specific gauge symmetry.

(3b) GU's VZ evasion does NOT rely on a guardian symmetry. Instead, it relies on the
     Clifford identity c(xi)^2 = g_Y(xi,xi) * Id, which forces the effective RS principal
     symbol to have trivial kernel at non-null xi. This is a DIFFERENT evasion mechanism than
     Vasiliev's.

(3c) Sp(64) is a GLOBAL symmetry of the RS sector (all gauge transformations are valued in
     the full sp(64) Lie algebra, not in a local RS-specific sub-algebra). hs(lambda) acts
     locally on each spin sector through the master field formalism.

(3d) The hs(lambda) algebra is INFINITE-DIMENSIONAL (it contains generators at all spins s =
     0, 1/2, 1, 3/2, 2, ...). GU's Sp(64) is FINITE-DIMENSIONAL (dim = 8256).

**Axis 3 verdict:** Structurally different gauge symmetries. GU: finite-dimensional Sp(64)
acting globally on H^64. Vasiliev: infinite-dimensional hs(lambda) acting as local higher-spin
gauge algebra. GU evades VZ without a guardian symmetry; Vasiliev evades VZ via guardian
symmetry delta psi_mu = nabla_mu epsilon. These are different mechanisms for the same
phenomenological requirement (consistent spin-3/2 propagation).

---

### Axis 4: Generation Count

**GU generation count:**
The RS sector contributes exactly 8 H-lines (ind_H(D_RS) = 8) to the total index
ind_H(D_GU) = 24 (3 SM generations). This is the GU generation mechanism: RS sector =
1 SM generation. The APS computation on compact K3 gives ind_H(D_RS) = hat{A}(K3) *
rank_H(S_RS^+) + eta/2 = 2 * 4 + 0 = 8 at reconstruction grade. The RS sector is the
third SM generation in GU's counting.

**Vasiliev generation count:**
Vasiliev's theory has NO generation mechanism for fermions. The theory describes massless
higher-spin fields (spin 0, 1/2, 1, 3/2, 2, ...) in AdS_4, but the spin-3/2 field appears
once (as the gravitino in the Type A minimal model) or in a specific multiplet determined by
the choice of hs(lambda). There is no mechanism in Vasiliev's construction that produces
multiple generations of spin-1/2 or spin-3/2 fields from a single algebraic structure.

In the AdS/CFT context, multiple generations would correspond to different scalar operators
in the boundary CFT, but the hs(lambda) algebra does not favor any particular number of
generations -- the number is a free parameter of the boundary theory.

**Comparison on Axis 4:**
(4a) GU: RS sector generates exactly 1 SM generation from the APS index theorem on K3.
     The generation count is a TOPOLOGICAL output (ind_H), not a free parameter.

(4b) Vasiliev: no generation mechanism. The number of spin-3/2 fields is a free parameter
     of the model (choose N copies of the spin-3/2 field, getting N graviti-no fields and
     N x 2 = 2N SUSY generators in the N-extended SUGRA limit).

**Axis 4 verdict:** Genuinely distinct. GU's topological generation count has no analog in
Vasiliev. This is a fundamental structural difference, not merely a quantitative one.

---

### Core Question: Is GU's VZ Evasion Absorbed by Vasiliev?

The failure condition for GU distinctness (stated in the problem) is:

> If GU's principal-symbol structure is equivalent to a special case of Vasiliev at some
> truncation order N, the VZ evasion claim loses novelty.

To assess this, we compare the VZ evasion mechanisms directly:

**GU's VZ evasion mechanism:**
The Clifford identity c(xi)^2 = g_Y(xi,xi) * Id in Cl(9,5) = M(64,H). This identity:
- Holds algebraically for ANY non-null xi in T*Y^14.
- Is BACKGROUND-INDEPENDENT: it does not depend on the connection, curvature, or cosmological
  constant of Y^14 or X^4.
- Applies in 14 dimensions on the fiber bundle Y^14 = Met(X^4) without truncation.
- Is not a statement about cubic vertices or higher-spin algebra structure constants.
- Requires NO AdS background.

**Vasiliev's VZ evasion mechanism:**
In Vasiliev's theory, VZ evasion for the spin-3/2 field is achieved through:
- Local gauge symmetry delta psi_mu = nabla_mu epsilon (guardian symmetry).
- The consistent cubic vertices in AdS_4, which are AdS-curvature-dependent.
- The full nonlinear equations of motion (the "Vasiliev system"), which are ON-SHELL consistent
  in AdS_4 but not off-shell.

The Vasiliev master field construction uses a "deformed" oscillator algebra with a star-product
deformation by the AdS cosmological constant Lambda. The VZ evasion relies on this star-product
structure: the cubic vertex coefficient for the RS-RS-gauge vertex vanishes at the correct
on-shell kinematics, which is only consistent in AdS_4.

**Assessment of the failure condition:**
GU's principal-symbol structure (the Clifford identity in Cl(9,5) = M(64,H)) is NOT a
special case of Vasiliev at any truncation order N. The reasons:

(FC-A) Vasiliev operates in 4D AdS_4. GU operates on 14D Y^14. These are not related by
       truncation: Vasiliev's hs(lambda) algebra has no finite-dimensional truncation at any
       order N that reproduces the 14D Clifford algebra Cl(9,5) = M(64,H). The Clifford
       algebra is a fixed (not deformed) algebra; hs(lambda) is a family of deformed algebras.

(FC-B) GU's VZ evasion is at the PRINCIPAL-SYMBOL level (order-1 differential operator).
       Vasiliev's VZ evasion involves the full interacting theory (cubic and higher vertices).
       Principal-symbol computations are one-derivative statements; cubic vertex computations
       are three-derivative statements. These are in genuinely different sectors of the
       differential algebra.

(FC-C) GU's RS field has SM quantum numbers (Pati-Salam: S(6,4) = C^16 gives (4,2,1) +
       (4bar,1,2)). Vasiliev's spin-3/2 field in AdS_4 has no internal quantum numbers in the
       minimal model (it is the gravitino of N=1 SUGRA in AdS_4). Including internal quantum
       numbers in Vasiliev's framework requires "color" extensions (N > 1 SUSY, or Chan-Paton
       factors), which are separate from the higher-spin algebra hs(lambda) itself.

(FC-D) GU's evasion mechanism -- the Clifford identity -- works for ARBITRARY sign of
       g_Y(xi,xi), i.e., for spacelike, timelike, and null xi. It asserts:
       - spacelike xi (g_Y > 0): S_R^{14D}(xi) has trivial kernel, RS propagator is invertible.
       - null xi (g_Y = 0): S_R^{14D}(xi) has nontrivial kernel (the physical propagating modes).
       Vasiliev's VZ evasion is SPECIFICALLY for on-shell physical (null) momenta. The off-shell
       behavior of the Vasiliev system is complicated by gauge non-invariance of off-shell
       amplitudes. GU's Clifford identity works off-shell.

**Conclusion on distinctness:** GU's VZ evasion mechanism is GENUINELY DISTINCT from
Vasiliev's. The failure condition does not fire: GU's principal-symbol structure cannot
be obtained as a special case of Vasiliev at any truncation order N because:
- Different ambient geometry (14D fiber bundle vs. 4D AdS).
- Different algebraic mechanism (Clifford identity vs. star-product cubic vertex).
- Different gauge symmetry (Sp(64) vs. hs(lambda)).
- Different internal quantum number structure (SM-charged vs. no internal charges in minimal model).

---

## Explicit Failure Conditions for CONDITIONALLY_RESOLVED

For this verdict to be overturned (for GU's mechanism to be absorbed by Vasiliev), one
of the following would need to hold:

**FC-1 (Dimensional reduction absorption):** There exists a consistent Kaluza-Klein reduction
of a 14D Vasiliev-type theory (higher-spin gauge theory on 14D AdS_{14} or similar) whose
spin-3/2 sector, when reduced to 4D, has a principal symbol EQUIVALENT to GU's Clifford-identity
mechanism. Currently: (a) 14D higher-spin theories are not known to be consistent (Vasiliev's
construction is specific to 4D and some other dimensions); (b) the Clifford identity in Cl(9,5)
is not derivable from any known higher-spin algebra structure constant computation.

**FC-2 (Fronsdal-limit identity):** GU's Schur-complement operator D_RS^{eff}, when restricted
to the 4D base X^4 = AdS_4 and linearized around the AdS_4 background, is gauge-equivalent
to Fronsdal's linearized spin-3/2 equation. If this equivalence held, GU's RS sector would
be a nonlinear embedding of the Fronsdal field. Currently: GU's RS sector on X^4 propagates
on (X^4, g_s) with g_s determined by the section s: X^4 -> Y^14; there is no constraint
that g_s = g_{AdS_4}.

**FC-3 (Higher-spin algebra Clifford embedding):** There exists a finite-dimensional quotient
hs(lambda) / I_N (for some ideal I_N and truncation order N) that is isomorphic (as an
associative algebra) to M(64,H) or to a subalgebra of Cl(9,5). Currently: hs(lambda) for
generic lambda is simple (has no non-trivial ideals for lambda not equal to a root of unity),
and its finite-dimensional quotients (when they exist at lambda = rational) are matrix algebras
over C, not over H. The quaternionic structure of M(64,H) is not replicated by any known
truncation of hs(lambda).

---

## Result

**Verdict: CONDITIONALLY_RESOLVED**

GU's VZ evasion mechanism is GENUINELY DISTINCT from Vasiliev's framework. The comparison
on four axes shows:

| Axis | GU RS | Vasiliev RS | Distinct? |
|---|---|---|---|
| Propagation | Null cone of g_Y on 14D Y^14; Clifford identity; background-independent | Null cone of g_AdS on 4D AdS_4; AdS-background-dependent cubic vertices | Yes -- dimension, background |
| Coupling | Leibniz product rule; Sp(64) kinematic; D_{RS,1/2} nonzero by construction | Cubic vertices in hs(lambda); AdS-curvature-dependent; lambda-deformed | Yes -- mechanism, background-dependence |
| Gauge symmetry | Sp(64) global, no RS-specific local symmetry (OQ2 open) | hs(lambda) local; delta psi = nabla epsilon; guardian symmetry present | Yes -- GU lacks guardian symmetry but evades VZ differently |
| Generation count | 1 SM generation from APS index theorem on K3 (topological) | No mechanism; N graviti-nos is a free parameter | Yes -- GU topological; Vasiliev free |

**The failure condition for distinctness does not fire:** GU's principal-symbol structure
(Clifford identity in Cl(9,5) = M(64,H)) cannot be obtained as a special case of Vasiliev's
higher-spin algebra hs(lambda) at any truncation order N, because the algebraic objects are
not isomorphic (FC-3), the ambient geometry differs in essential ways (FC-1), and the
physical content (SM quantum numbers, generation count) is present in GU but absent in the
minimal Vasiliev model (FC-2).

**Strongest positive claim (reconstruction grade):**
GU's RS embedding provides a NEW MECHANISM for consistent spin-3/2 propagation distinct
from the two known mechanisms: (a) local SUSY / guardian symmetry (SUGRA, Vasiliev), and
(b) topological protection (Rarita-Schwinger on backgrounds with special holonomy). GU's
mechanism -- Clifford algebra embedding via the Dirac-DeRham complex on a fiber bundle of
metrics -- requires no AdS background, no infinite-dimensional higher-spin algebra, and no
free deformation parameter. The VZ evasion is algebraic (not perturbative) and holds at
the principal-symbol level (not merely on-shell or at cubic-vertex order).

**Caveats and what remains genuinely open:**

(i) The comparison is at the level of LINEARIZED / PRINCIPAL-SYMBOL analysis. The FULL
    nonlinear interacting theories of GU and Vasiliev have not been compared. At the
    nonlinear level, GU's interaction structure (via the Dirac-DeRham action on Y^14) may
    or may not reproduce aspects of Vasiliev's cubic vertex structure.

(ii) The 4D EFFECTIVE FIELD THEORY of GU's RS sector (the sector below the KK scale M_{KK})
     has not been explicitly computed. If this EFT, when written in AdS_4, is equivalent to
     the Fronsdal system, GU's RS sector would be a nonlinear completion of Vasiliev's
     linearized theory. This would not absorb GU's mechanism but would establish a non-trivial
     contact point. [OQ-RS-3A: compute the GU RS effective field theory in AdS_4 background.]

(iii) The super-IG algebra (OQ2) has not been constructed. If it is constructed and turns out
      to be isomorphic to a subalgebra of hs(lambda), GU's guardian symmetry (if it exists)
      would be a special case of Vasiliev's gauge algebra. This would be a structural relation
      at the symmetry level. [OQ-RS-3B: if super-IG is constructed, compare to hs(lambda).]

---

## Open Questions

| # | Question | Priority | Tractability |
|---|---|---|---|
| OQ-RS-3A | Compute the GU RS effective field theory below M_{KK} in AdS_4 background; compare to linearized Fronsdal | Medium | Medium -- requires KK reduction |
| OQ-RS-3B | If super-IG is constructed, compare its structure constants to hs(lambda) | Low until OQ2 resolved | Hard |
| OQ-RS-3C | Is there a higher-spin algebra (not hs(lambda)) in which GU's Clifford-identity mechanism is a special case? | Long-range | Hard |
| OQ-RS-3D | Do GU's SM-charged RS modes have a sensible AdS/CFT dual, and does the dual correspond to a known CFT operator? | Long-range | Hard |

---

*Filed: 2026-06-23. Verdict: CONDITIONALLY_RESOLVED — GU's VZ evasion mechanism is
genuinely distinct from Vasiliev; three explicit failure conditions (FC-1/FC-2/FC-3) stated;
failure condition for distinctness does NOT fire at reconstruction grade.*
