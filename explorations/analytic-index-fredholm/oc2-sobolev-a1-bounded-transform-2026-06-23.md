---
title: "OC2 Analytic Gate A1: P_disc Bounded on Weighted Sobolev K_H Spaces — Framework Assessment and Failure Family"
date: 2026-06-23
problem_label: "oc2-sobolev-analytic-gate-a1"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# OC2 Analytic Gate A1: P_disc Bounded on Weighted Sobolev K_H Spaces

## PRIORITY NOTE (added 2026-06-23, MO-07)

**The fundamental question this file does not answer:** When SL(4,R) has no scalar discrete
series (rank(G) = 3, rank(K) = rank(SO(4)) = 2, 3 ≠ 2 — Harish-Chandra criterion fails),
what is P_disc projecting onto in the non-compact Y^14 setting?

Gate A1 as stated assumes P_disc has a non-empty discrete sector to project onto. For the
scalar sector on the SL(4,R)/SO_0(3,1) fiber, there is no L^2 discrete spectrum at all —
the Harish-Chandra criterion is not met. This means the P_disc appearing in A1 either:

  (i) Projects onto a zero-dimensional space (trivially bounded, but vacuous for physics), or
  (ii) Requires the tau-twisted spinor coefficient S(6,4) to generate discrete L^2 spectrum
       that the scalar sector lacks — which is the content of the open questions E1-E3 and
       the APS/K3 reconstruction route.

**Consequence for this file's verdict:** The three framework candidates (b-calculus,
scattering calculus, Melrose-Piazza) each supply boundedness of P_disc conditional on the
discrete sector being non-empty. None of them verify, from GU first principles, that a
non-trivial discrete sector exists on the non-compact SL(4,R)/SO_0(3,1) fiber.

**Routing clarification:** Gate A1 is only operative for the non-compact Y^14 analytic
program. The APS/K3 route bypasses A1 entirely by working on the compact K3 factor, where
discrete spectrum exists by compactness. The K3 APS route is currently primary (ind_H = 24
at reconstruction grade). Verify whether Gate A1 is still load-bearing after the APS route
is primary — if not, A1 is a secondary open question, not a gate for the main program.

**Three additional failure conditions from this gap (FC7-FC9 below in §8):**
- FC7: Scalar P_disc has empty target on non-compact fiber (no discrete series for SL(4,R))
- FC8: Tau-twist S(6,4) fails to generate discrete L^2 spectrum on the A3 fiber
- FC9: Non-compact Y^14 analytic program is not primary, making A1 non-load-bearing

---

## 1. Problem Statement

The b-parametrix program for D_GU on noncompact Y^14 (oc2-b-parametrix-y14) identified A1
as the primary remaining analytic gate:

> **A1.** P_disc is a bounded H-linear orthogonal projection on L^2_{H,delta} and on
> W^{1,2}_{H,delta}, invariant under D_GU up to compact terms.

The question here: which framework -- b-calculus on asymptotically hyperbolic spaces,
scattering calculus, or Melrose-Piazza pseudodifferential projection -- can supply a bounded
P_disc for the projected discrete sector? What are the precise functional-analytic conditions?
Can those conditions be discharged from GU first principles or do they require new input
about the tau-twisted discrete spectrum? Is there a family for which P_disc is unbounded on
any natural K_H norm?

This note performs the assessment at reconstruction grade and exhibits a concrete failure
family.

## 2. Established Context

From the OC2 predecessor chain (loaded, not re-derived):

- Y^14 = Met(X^4): fiber F = GL(4,R)/O(3,1), 14-dimensional with signature (9,5) on Y^14.
- Cl(9,5) = M(64,H); spinor module S = H^64; gauge group Sp(64).
- D_GU is H-linear; weighted conjugate D_delta = e^{delta r} D_GU e^{-delta r} for r = log-conformal-scale on the dilaton end.
- Indicial roots at the dilaton end: delta_j = -|mu_fib,j| where
  |mu_fib,j| in {2sqrt(2)/R_s, sqrt(14)/R_s, 3sqrt(2)/R_s, sqrt(20)/R_s}
  with continuum threshold 9/(2R_s). (Reconstruction grade, from oc2-b-parametrix-y14 §3.7.)
- Natural Fredholm weight: delta in Window 0 (delta > 0), avoiding all indicial roots.
- The fiber symmetric space SL(4,R)/SO_0(3,1) has split rank 3 (A3 root system, rank of
  restricted root system = 3); the Harish-Chandra criterion for discrete series fails for
  the scalar sector (rank(G)=3, rank(K)=rank(SO(4))=2, 3 != 2). No scalar discrete series.
- APS route (oc1-oc2-aps-closure): ind_H(D_GU) = 24 at reconstruction grade on K3-type X^4.
- tau_RS = 4D(1/2,0) + 4D(0,1/2) is nonunitary as a Lorentz coefficient; tau-twisted
  Flensted-Jensen route fails on four independent structural grounds (generation-count-rank3-resolution).
- Physical DOF count and APS give ind_H(D_RS) = 8 at reconstruction grade; analytic
  representation-theoretic confirmation remains OPEN for the non-compact Y^14 setting.

## 3. Three Candidate Frameworks for P_disc Boundedness

### Framework 1: b-Calculus on Asymptotically Hyperbolic Ends

**Setup.** The b-calculus (Melrose 1993) applies to manifolds with boundary (compact with
corners). For Y^14, compactify the dilaton R^+ fiber direction by x = e^{-r}: the end x=0
is a boundary face. The b-tangent bundle on the compactified fiber has frame {x d/dx, d/y^a}.

A b-pseudodifferential operator P of order 0 is bounded on L^2_b if its full b-symbol
sigma_b(P) is bounded on the b-cotangent bundle, and the operator is uniformly controlled
near the boundary face x=0 via the indicial family.

**Projection via b-calculus.** The spectral projection P_disc = P_{spec(D_GU) in discrete part}
can be expressed as a Cauchy-Riesz contour integral:

```
P_disc = (1/2pi i) integral_Gamma (D_GU - z)^{-1} dz
```

where Gamma is a contour encircling the discrete spectrum in the resolvent set. The resolvent
(D_GU - z)^{-1} for z not in spec(D_GU) is a b-pseudodifferential operator of order -1
when D_GU is b-Fredholm (i.e., when the indicial family I(D_GU - z, lambda) is invertible
for all lambda on the relevant line determined by delta).

**Conditions for b-calculus P_disc boundedness on W^{1,2}_{H,delta}:**

(BC1) D_GU is b-elliptic in the projected sector. This means the projected symbol
      sigma_b(P_disc D_GU P_disc) is invertible on the b-cotangent sphere of the
      compactified fiber, away from zero section.

      For the discrete sector, the fiber Dirac modes have nonzero mass
      (Delta_N eigenvalues in {8,14,18,20}/R_s^2 are strictly positive). The effective
      projected symbol is:
      ```
      sigma_b(D_delta,disc)(xi) = P_disc sigma_b(D_delta)(xi) P_disc
      ```
      which is invertible when the mass gap m^2 = min_j{Delta_N,j} = 8/R_s^2 > 0 dominates.
      Concretely: at the boundary face x=0, the indicial family I(D_delta,disc, lambda) is
      I(D_GU,disc, lambda) = P_disc [Gamma^r(i lambda - delta) + D_tang] P_disc.
      For delta in Window 0 (delta > 0), all indicial roots delta_j < 0 are avoided, so
      the indicial family restricted to the discrete sector is invertible for all lambda in iR.
      This gives b-Fredholmness of D_delta,disc, and the resolvent is in the b-calculus.

(BC2) The contour Gamma is in the resolvent set of D_GU uniformly, and the resolvent
      norm is bounded on the contour. This holds when:
      - Zero is not an indicial root of D_GU - z for z on Gamma.
      - The discrete eigenvalues are isolated from the contour.
      When the discrete spectrum is separated from the continuum threshold by a gap
      (the 8/R_s^2 gap from (BC1)), a small contour Gamma around each discrete eigenvalue
      stays in the resolvent set.

(BC3) The Cauchy integral defining P_disc converges in the b-operator-norm topology on
      W^{1,2}_{H,delta}. This uses the b-calculus composition theorem: the resolvent integral
      converges in the Frechet topology of the b-calculus, giving P_disc as a b-operator of
      order 0. Order 0 b-operators are bounded on L^2_b and map W^{1,2}_{H,delta} into
      W^{1,2}_{H,delta} by the Sobolev mapping property of the b-calculus.

**Conclusion for b-calculus:** Under (BC1)-(BC3), P_disc is bounded on L^2_{H,delta} and
on W^{1,2}_{H,delta}, giving A1 from the b-calculus side. The conditions are:
(a) nonzero mass gap (Delta_N spectrum separated from zero),
(b) discrete spectrum separated from the continuum threshold,
(c) weight delta strictly in the interior of a Fredholm window.

These are exactly the conditions (A2) and (A3) named in oc2-b-parametrix-y14. So b-calculus
supplies A1 IF A2 (discrete eigenvalues separated from zero) holds. The APS/K3 route
establishes that the discrete sector is nonempty (ind_H = 24 > 0) and gives the mass gap
from the Dirac spectrum on K3. The non-compact analytic confirmation of the spectral gap
on Y^14 is still reconstruction-grade.

**Key advantage of b-calculus:** The b-calculus handles the cylindrical dilaton end
(x d/dx structure) naturally. The resolvent in the b-calculus automatically controls the
operator near the boundary face at the order-0 level. No auxiliary cutoffs needed.

**Key limitation:** The b-calculus requires the compactification to be a manifold with
corners; the SL(4,R)/SO_0(3,1) factor has a rank-3 corner structure (three asymptotic
directions), not a single boundary face. The appropriate generalization is the
fibred-corners calculus or the totally characteristic calculus for rank-3 corners.
For the R^+ = dilaton factor alone (single boundary face, rank-1 corner), the standard
b-calculus applies cleanly; for the full fiber end, corner calculus is needed.

### Framework 2: Scattering Calculus

**Setup.** The scattering calculus (Melrose 1994) applies to manifolds with a scattering
(conic/asymptotically Euclidean or asymptotically hyperbolic) end: the metric is
r^{-4} dr^2 + r^{-2} g_Y^{sphere} near r=+infty. For GL(4,R)/O(3,1) the end is
hyperbolic (constant curvature -1 in rank-1 pieces) near the maximum weight Weyl chamber
wall; the scattering calculus is the correct microlocal framework for asymptotically
hyperbolic symmetric spaces.

For the rank-one symmetric space SL(2,R)/SO(2) = H^2 (the hyperbolic plane) the
scattering calculus is standard. For higher-rank A3 symmetric space SL(4,R)/SO_0(3,1),
the correct calculus is the edge or fibred-scattering calculus, accounting for the
three-dimensional family of Weyl-chamber walls.

**P_disc via resolvent in the scattering calculus.** For an asymptotically hyperbolic
space M, the resolvent (Delta - s(n-1-s))^{-1} (with n = dim M = 10 for the fiber, n-1 = 9)
extends meromorphically in s from Re(s) >> 0 through a strip below Re(s) = (n-1)/2 = 9/2.
The poles are called resonances. The spectral projection onto a discrete eigenvalue below
the continuous spectrum threshold L_2 = (n-1)^2/4 = 81/4 is computable from the residue
of the resolvent at the corresponding pole.

For the Dirac operator D_GU (not the scalar Laplacian), the scattering resolvent is in the
scattering calculus at order -1, and spectral projections are obtained by contour integration.

**Conditions for scattering-calculus P_disc boundedness on W^{1,2}_{H,delta}:**

(SC1) The scattering metric on the end of F = GL(4,R)/O(3,1) is well-defined, i.e., the
      symmetric space metric near infinity has a well-controlled scattering asymptotic. For
      the hyperbolic curvature direction (rank-1 piece at each Weyl chamber wall), this holds.
      For the full rank-3 corner, a fibred-scattering structure is needed.

(SC2) The resolvent (D_GU - z)^{-1} extends meromorphically in z from the resolvent set
      through the continuous spectrum threshold to a half-plane containing the discrete
      eigenvalues. For asymptotically hyperbolic Dirac operators (rank-1 case), this is
      standard (Mazzeo-Melrose 1987). For rank-3 symmetric spaces, the meromorphic extension
      through the Plancherel threshold requires the full Harish-Chandra resolvent kernel,
      which is known to be meromorphic in the spectral parameter (e.g., Helgason 1984,
      Chapter IV).

(SC3) Discrete eigenvalues of D_GU below the continuous spectrum threshold form a finite set
      at each energy level, and the residues at the corresponding poles are finite-rank projections.
      For the tau-twisted coefficient bundle S(6,4), the discrete spectrum is established by
      OQ-KK1 (fiber wavefunction) and RC3 (Delta_N spectrum), both at reconstruction grade.

(SC4) The scattering operator norm of P_disc on the weighted Sobolev space W^{1,2}_{H,delta}
      is controlled by the spectral gap and the regularity of the resolvent at the pole.
      This uses the fact that for a simple eigenvalue lambda_0, the residue-projection P_0
      satisfies
      ```
      ||P_0||_{W^{1,2} -> W^{1,2}} <= C / dist(lambda_0, rest of spec)
      ```
      where C depends on the scattering resolvent norm on the contour.

**Conclusion for scattering calculus:** The scattering-calculus framework supplies P_disc
boundedness on W^{1,2}_{H,delta} IF the Harish-Chandra resolvent is meromorphically
extended through the continuous spectrum threshold and the discrete eigenvalues are simple
(or finite multiplicity) with controlled residues. For rank-1 hyperbolic pieces, this is
standard. For the full A3 fiber, the fibred-scattering extension requires the rank-3 analogue
of Mazzeo-Melrose, which exists in the literature (Ji-Mazzeo-Seeger or equivalent) at the
analytic level but requires explicit verification for the twisted spinor bundle case.

**Key advantage of scattering calculus:** The scattering calculus is better adapted to the
hyperbolic-curvature structure of G/H near the cusps and Weyl-chamber boundaries. It gives
explicit meromorphic resolvent extensions and controls the spectral measure near the continuous
spectrum threshold more precisely than b-calculus alone.

**Key limitation:** The rank-3 fibred-scattering extension is significantly harder to make
explicit than the rank-1 or b-calculus analogue. Verifying the required estimates for the
full GU spinor bundle S = H^64 with the S(6,4) tau-twisted coefficient requires non-trivial
representation-theoretic input (the Harish-Chandra c-function for the A3 system twisted by S(6,4)).

### Framework 3: Melrose-Piazza Pseudodifferential Projection

**Setup.** Melrose and Piazza (1997, "Families of Dirac operators, boundaries and the
b-calculus") introduced a systematic approach to constructing smoothing (compact) operators
that project onto the eigenspaces of families of Dirac operators parametrized over a base.
The key construction is the spectral section: a family of bounded projections P_s
such that D_s P_s = P_s^{perp} D_s P_s + (compact), i.e., P_s is almost an eigenspace
projector with controlled compact remainder.

For the GU family {D_x} parametrized by x in the observer parameter space X, the
Melrose-Piazza spectral section gives:

P_sec,x = spectral projection onto {eigenvalues of D_x below threshold M}

for some M > 0 below the continuous spectrum threshold but above all nonzero discrete
eigenvalues in the tau-twisted sector. For a family with uniform spectral gap, P_sec,x
is a smooth family of bounded projections on the Sobolev scale.

**Conditions for Melrose-Piazza spectral section:**

(MP1) The family {D_x} over X is a smooth family of self-adjoint Fredholm operators on
      a fixed Hilbert space K_H. In the GU setting, this requires the common-domain
      trivialization and norm continuity of x |-> D_x (assumed as A4, A5 in the b-parametrix
      theorem). Under those assumptions, (MP1) is satisfied.

(MP2) The spectral gap is uniform in x: the distance from the chosen threshold M to the
      nearest eigenvalue of D_x is bounded below uniformly for x in X. This is the
      compactness-in-x analogue of condition (BC2) above.

(MP3) The Hilbert space K_H is the discrete-sector weighted space L^2_{H,delta,disc}.
      Melrose-Piazza applies directly to families on a fixed Hilbert space; the discrete-sector
      restriction is compatible with the construction since P_disc commutes with D_GU up to
      compact terms (from the b-parametrix).

**What Melrose-Piazza adds over b-calculus alone:**

The Melrose-Piazza spectral section explicitly constructs P_sec,x as a SMOOTH family over X,
not just as a bounded operator at each x. This gives:

1. P_sec,x varies continuously (and smoothly) in norm as x varies in X.
2. P_sec,x commutes with D_x up to a compact operator K_x that varies continuously in x.
3. The restriction D_x P_sec,x is Fredholm with compact remainder, and
   ind_H(D_x P_sec,x) = ind_H(D_x) (index is stable under compact perturbation).

This is precisely what is needed for the bounded-transform norm continuity (condition A5 in
the b-parametrix theorem): the continuous family P_sec,x combined with the b-calculus
Fredholm theorem for each D_x gives norm continuity of F_x = D_x(1+D_x^* D_x)^{-1/2}.

**Conditions dischargeable from GU first principles:**

(D1) The spectral gap (MP2) on the discrete sector is guaranteed by the APS computation:
     the lowest discrete Dirac eigenvalue on K3-type X^4 (at reconstruction grade) is
     separated from zero by the Lichnerowicz bound and from the continuum threshold 9/(2R_s)
     by the gap between the largest discrete mode sqrt(20)/R_s and the threshold 9/(2R_s)
     (a gap of approximately 0.03/R_s -- very narrow but nonzero). This gap is controlled
     by the GU geometry (R_s from the fiber curvature scale) and is not externally imposed.

(D2) H-linearity of P_sec,x follows from the H-linearity of D_x and the spectral projection
     formula (Cauchy integral of an H-linear resolvent is H-linear).

(D3) Invariance of P_sec,x under the Sp(64) gauge symmetry follows from the Sp(64)-equivariance
     of D_GU (Shiab and tau+ are Sp(64)-equivariant; gauge transformations commute with D_GU
     up to inner automorphisms, preserving the spectral projection).

**Conditions requiring new input about tau-twisted discrete spectrum:**

(E1) The discrete eigenvalues of D_GU on the tau-twisted fiber sector exist and are nonzero.
     This is the core of A2 in the b-parametrix theorem. The APS/K3 route gives this at
     reconstruction grade (ind_H(D_GU) = 24 means the kernel is 24-dimensional H-linear;
     nonzero eigenvalues exist by Fredholmness). But explicitly identifying the discrete
     spectrum of D_GU on noncompact Y^14 with the tau-twisted fiber spectrum requires the
     KK-mode decomposition (G2 in the g2-kk-zero-mode-unitarity file).

(E2) The spectral gap is uniform as tau varies. If the tau-twist is a continuous parameter,
     the spectral gap must be lower-bounded uniformly. For the discrete modes indexed by
     Delta_N in {8,14,18,20}/R_s^2, the gap to the continuum threshold is:
     9/(2R_s) - sqrt(20)/R_s = (9/2 - sqrt(20))/R_s ~ 0.03/R_s. This is a very narrow
     gap that requires careful control.

(E3) The Sobolev regularity of the discrete modes: the eigenfunctions phi_j in P_disc are
     smooth sections in W^{k,2}_{H,delta} for all k, so P_disc is bounded on all Sobolev
     orders. For the KK fiber modes constructed in oq-kk1-rs-fiber-wavefunction
     (phi_RS(r) ~ N_RS * e^{-6r} for large r), the exponential decay gives infinite
     differentiability in the weighted sense, so this condition is satisfied.

## 4. Functional-Analytic Conditions: Precise Statement

Combining the three frameworks, the precise conditions for P_disc to be bounded on
W^{1,2}_{H,delta} are:

**Condition Set A (from b-calculus):**

A-i. The b-symbol of P_disc D_GU P_disc is elliptic on the b-cotangent bundle of the
     compactified dilaton end, i.e., the mass gap min_j{Delta_N,j} = 8/R_s^2 > 0.

A-ii. The weight delta is strictly in Window 0 (delta > 0), so the indicial roots
      delta_j = -|mu_fib,j| are all strictly negative and the indicial family of D_GU
      at the dilaton end is invertible.

A-iii. The spectral gap between the discrete fiber Dirac eigenvalues and the continuum
       threshold is positive: 9/(2R_s) - sqrt(20)/R_s ~ 0.03/R_s > 0.

A-iv. The corner structure of the fiber end (rank-3 A3) is controlled by a fibred-corners
      or totally-characteristic extension of the b-calculus, ensuring the b-operator norm
      of P_disc is finite near all boundary faces.

**Condition Set S (from scattering calculus, supplementing A):**

S-i. The Harish-Chandra resolvent for D_GU with coefficient bundle S(6,4) extends
     meromorphically through the continuum threshold, with residues at discrete eigenvalues
     that are bounded finite-rank operators on W^{1,2}_{H,delta}.

S-ii. The scattering matrix for D_GU is well-defined at the continuum threshold: there are
      no accumulation points of discrete eigenvalues at the continuum threshold in the
      tau-twisted sector.

**Condition Set MP (from Melrose-Piazza, supplementing A and S):**

MP-i. The family {D_x}_{x in X} is smooth (C^infty) as a map X -> operators on K_H,
      using the common-domain trivialization.

MP-ii. The spectral gap is uniform: inf_{x in X} dist(0, sigma_{disc}(D_x) \ {0}) > 0.

MP-iii. The Melrose-Piazza spectral section P_sec,x is H-linear and Sp(64)-equivariant,
        which follows from H-linearity and Sp(64)-equivariance of D_x (conditions D2, D3 above).

## 5. Which Conditions Can Be Discharged from GU First Principles

**Dischargeable (GU first principles suffice):**

- A-i: Mass gap min_j{Delta_N,j} = 8/R_s^2 > 0. The fiber Dirac spectrum on the discrete
  sector is strictly positive because the tau-twisted eigenvalues are nonzero (APS/K3
  reconstruction grade; the Lichnerowicz bound on K3 gives a strict lower bound on the
  Dirac eigenvalue). GU first principles supply R_s (the fiber curvature scale, set by the
  GL(4,R)/O(3,1) geometry); the mass gap is a structural fact, not an external input.

- A-ii: Weight window (delta > 0). This is a choice of functional-analytic setup, not a
  theorem; it is dischargeable by selecting delta = epsilon > 0 small.

- D2 (H-linearity of P_disc): From Cl(9,5) = M(64,H) structure, fully algebraic.

- D3 (Sp(64)-equivariance of P_disc): From Sp(64)-equivariance of D_GU, algebraic.

- D3' (A-iii, gap nonzero): The gap 9/(2R_s) - sqrt(20)/R_s is a computable geometric
  constant. It is small but nonzero; whether it closes under deformation of the section s
  or the GU connection A requires checking the spectral flow of D_GU over the observer
  parameter space X. At fixed section, it is dischargeable from GU geometry.

**Not dischargeable without new input about the tau-twisted discrete spectrum:**

- A-iv (corner calculus for rank-3 A3 fiber): The fibred-corners extension of the b-calculus
  for the full A3 symmetric space end requires the rank-3 analogue of Melrose's b-calculus.
  This is a literature theorem (Mazzeo-Piazza edge calculus, or Vasy's multi-body calculus
  for symmetric spaces) but is not derived from GU first principles. The GU construction
  specifies the geometry but not the microlocal analysis.

- S-i (meromorphic extension of Harish-Chandra resolvent for tau-twisted spinors): The
  scalar-sector Harish-Chandra resolvent for SL(4,R)/SO_0(3,1) is known (rank-3 A3 symmetric
  space; Helgason 1984; Anker-Ji 1999). For the twisted coefficient bundle S(6,4), the
  meromorphic extension is expected but not proved in this repo. Requires representation-theoretic
  input (Harish-Chandra c-function for the twisted system; related to the failed tau-correction
  route -- the issue there was that no discrete poles were found, but the meromorphic extension
  itself is a separate question).

- S-ii (no accumulation of discrete eigenvalues at the threshold): For the tau-twisted sector,
  the continuum threshold is at Delta_N = 81/(4R_s^2). The gap between the largest discrete mode
  (Delta_N = 20/R_s^2) and the threshold (81/4 R_s^2 = 20.25/R_s^2) is:
  (81/4 - 20)/R_s^2 = 1/(4R_s^2) ~ 0.25/R_s^2. This is small but positive. The question
  is whether more discrete modes can exist in the gap (0.25/R_s^2 window). The RC3 computation
  identified only the four modes {8,14,18,20}/R_s^2; if these are exhaustive (as expected for
  the BC_1-derived spectrum), then S-ii holds. But the tau-twisted A3 system has not been
  classified to rule out additional discrete modes in the narrow window.

- E1 (existence and nonvanishing of tau-twisted discrete eigenvalues on Y^14): The APS route
  gives ind_H(D_GU) = 24 on K3-type X^4, implying the kernel is 24-dimensional. On noncompact
  Y^14, the kernel count requires the KK-mode decomposition (G2 conditions), which are
  conditionally established at reconstruction grade but not theorem grade.

- MP-ii (uniform spectral gap over X): This requires that the operator D_x does not develop
  a zero eigenvalue on the discrete sector as x varies over the observer parameter space X.
  This is a global (spectral flow) condition on the GU family that goes beyond the pointwise
  computation. If D_x is generic (no special symmetry forcing a zero mode), the gap is
  open-dense in X; but proving it for all x in X requires either a topological argument
  (spectral flow theorem) or an explicit lower bound.

## 6. Failure Family: When P_disc is Unbounded

**Construction of an explicit failure family.**

The failure condition under which P_disc is unbounded on any natural K_H norm occurs when
the discrete spectrum accumulates at zero or at the continuum threshold under a deformation
of the GU data. Here is an explicit family:

**Failure Family F-eps (mass gap collapse).**

Let R_s = R_s(epsilon) be the fiber curvature scale, varying with epsilon > 0. In the A3
geometry, the normal Laplacian eigenvalues scale as:

```
Delta_N,j(epsilon) = c_j / R_s(epsilon)^2
```

for fixed numerical constants c_j in {8, 14, 18, 20}. The continuum threshold scales as:

```
Delta_N,cont(epsilon) = 81 / (4 R_s(epsilon)^2).
```

Now define the deformation:

```
R_s(epsilon) = R_s,0 * sqrt(1 - epsilon)   for epsilon in [0, 1).
```

As epsilon -> 1^-, R_s(epsilon) -> 0, and:

```
Delta_N,j(epsilon) = c_j / (R_s,0^2 (1-epsilon)) -> +infty
Delta_N,cont(epsilon) = 81 / (4 R_s,0^2 (1-epsilon)) -> +infty.
```

This is not the problematic direction. The problem arises in the other limit.

**Failure Family F-flat (section flattening).**

Let s = s_t be a family of sections X^4 -> Y^14 parametrized by t in [0,1], with s_0 being
a K3 embedding (ind_H = 24) and s_1 being a flat (T^4-type) embedding where A-hat(X^4) = 0.

As t -> 1, the section s_t approaches a flat section where:

```
ind_H(D_{s_t}) -> ind_H(D_{s_1}) = 8 * A-hat(T^4) + 8 = 8 * 0 + 8 = 8.
```

The spectral flow from t=0 to t=1 carries 24 - 8 = 16 H-linear eigenvalues from the discrete
kernel through zero (eigenvalues cross zero during the deformation). At the crossing points,
the eigenvalues are zero, so:

```
dist(0, sigma_{disc}(D_{s_t}) \ {0}) = 0   at the crossing times t*.
```

At t = t*, the spectral projection P_disc onto the discrete kernel has a discontinuity (or
an infinite expansion in the Sobolev norm). Precisely:

The spectral projection P_{disc,t} = P_kerD_{s_t} + sum_{0 < lambda_j(t) < M} P_{lambda_j(t)}

has norm jump at t = t* where lambda_j(t*) = 0 and lambda_j crosses zero. The Riesz
projection formula gives:

```
P_{lambda_j, t} = (1/2pi i) integral_{|z - lambda_j(t)| = r} (D_{s_t} - z)^{-1} dz
```

For t near t*, the eigenvalue lambda_j(t) ~ c(t - t*) for small (t-t*). The resolvent near
z = 0 has:

```
||(D_{s_t} - z)^{-1}||_{L^2 -> W^{1,2}} ~ 1/|z - lambda_j(t)| ~ 1/|z - c(t-t*)|.
```

For the contour at radius r = |lambda_j(t)|/2 centered at lambda_j(t), the contour passes
at distance r from z=0. The norm blows up as:

```
||P_{lambda_j, t}||_{W^{1,2} -> W^{1,2}} ~ (1/r) * |contour length| ~ 1/|lambda_j(t)| -> infty
```

as t -> t* (lambda_j(t) -> 0).

**Conclusion:** The family {D_{s_t}, t in [0,1]} exhibits P_disc unbounded on W^{1,2}_{H,delta}
at the spectral-crossing times t*. At these times, the eigenvalue lambda_j(t) = 0 means D_{s_t}
has a zero mode in the discrete sector, the Fredholm gap closes, and P_disc (as the projection
onto the kernel) acquires infinite norm when computed on the Sobolev scale (because the
corresponding eigenfunction has Sobolev norm ~ 1/|lambda_j| when properly normalized in L^2).

**Precise statement of the failure:** For any K_H norm that is a weighted Sobolev norm
W^{k,2}_{H,delta} with k >= 1, and any projection P defined by the Riesz formula on a
contour encircling eigenvalues near zero, the norm ||P||_{L^2 -> W^{1,2}} blows up as the
eigenvalue approaches zero. This is not a pathological deformation: it occurs at any point
in the GU moduli space where a discrete eigenvalue of D_GU (on the discrete sector) is zero.

**The zero-mode subvariety.** The set of GU data (A, s) where D_GU has a zero mode on the
discrete sector is the zero-mode subvariety Z subset A(Y^14, Sp(64)) x Gamma(Y^14, X^4).
At generic points in the complement, P_disc is bounded. The bounded-transform construction
(F_x = D_x(1+D_x^*D_x)^{-1/2}) automatically handles zero modes by including them in the
Fredholm operator without requiring bounded P_disc -- but the specific Riesz projection
P_disc (as defined by the contour integral around the discrete spectrum) is unbounded on Z.

**Resolution:** The correct object for KSp classification is not P_disc but the bounded
transform F_x itself, which is always bounded (it is defined by functional calculus of an
H-linear self-adjoint operator). The Melrose-Piazza spectral section P_sec,x is defined
away from Z (when there is a spectral gap) and serves to connect F_x to the discrete spectrum
count. The failure family shows that P_disc as a Riesz projection is not globally bounded
on W^{1,2}_{H,delta} over the full GU moduli space; it is bounded on an open dense subset
(the complement of Z) but unbounded on the codimension-1 subvariety Z.

## 7. Main Results

### 7.1 Which Framework Best Supplies A1

**Verdict: The b-calculus combined with the Melrose-Piazza spectral section is the most
tractable framework for supplying A1 in the GU setting.**

Specifically:

- b-calculus handles the dilaton end (single boundary face, rank-1 R^+ factor) cleanly.
- Melrose-Piazza spectral section gives P_sec,x as a smooth family of bounded projections
  on K_H away from the zero-mode subvariety Z.
- Scattering calculus is better adapted to the full A3 fiber but requires the rank-3
  fibred-scattering extension and the Harish-Chandra resolvent for twisted spinors.

The combined approach:

1. Use the b-calculus on the dilaton end (R^+ factor) to construct Q_delta with compact
   remainder and verify Fredholmness of D_delta,disc for delta in Window 0.

2. Use the Melrose-Piazza spectral section, with its smooth-family guarantee, to supply
   A1 (P_disc bounded on W^{1,2}_{H,delta}) at all points x in X \ Z (away from zero modes).

3. At points in Z, the zero modes contribute to the kernel and cokernel of D_x; P_disc is
   not needed as a bounded operator there because the bounded transform F_x already handles
   the zero eigenvalues automatically via the functional calculus (1+D^*D)^{-1/2}.

This decomposition gives A1 at all generic points and explains why A1 is not a global
obstruction: the Riesz projection P_disc is bounded on K_H on an open dense set and
the bounded transform F_x extends this to all of X.

### 7.2 Precise Conditions

The precise functional-analytic conditions for P_disc bounded on W^{1,2}_{H,delta} are
(combining A, S, MP above):

**Necessary and sufficient (for the Riesz projection definition):**

NC1. The spectral gap: dist(0, sigma_{disc}(D_GU) \ {0}) > 0. (Mass gap condition; equivalent
     to A-i and A-ii from bc-calculus.)

NC2. The discrete spectrum is separated from the continuous spectrum threshold: the discrete
     eigenvalues do not accumulate at the threshold 9/(2R_s). (Equivalent to S-ii.)

NC3. The weight delta avoids all indicial roots. (A-ii, equivalent to Window 0 condition.)

**Sufficient (for boundedness on the full Sobolev scale):**

SC. The fiber eigenfunctions are smooth (in the sense of the b-Sobolev scale W^{k,2}_{H,delta}
    for all k). This follows from elliptic regularity on the compact K3 factor and from the
    explicit exponential decay of the RS fiber wavefunction phi_RS ~ e^{-6r} (oq-kk1).

### 7.3 Dischargeable vs. New Input Summary

| Condition | Source | Dischargeable from GU? | New input needed |
|---|---|---|---|
| Mass gap min{Delta_N} = 8/R_s^2 > 0 | APS/K3 reconstruction | YES | No |
| Weight in Window 0 (delta > 0) | Operator-analysis choice | YES | No |
| H-linearity of P_disc | Algebraic (Cl(9,5)=M(64,H)) | YES | No |
| Sp(64)-equivariance of P_disc | Algebraic (Sp(64)-equivariant D_GU) | YES | No |
| Discrete eigenvalues separated from continuum | RC3 reconstruction (gap = 1/(4R_s^2)) | PARTIALLY (small gap) | Confirmation that no discrete modes in [20, 81/4]/R_s^2 |
| Rank-3 A3 corner b-calculus | b-calculus on rank-3 end | NO | Literature theorem (Vasy, Mazzeo-Piazza) |
| Harish-Chandra resolvent for twisted spinors | Rep theory for A3 + S(6,4) | NO | New representation-theoretic computation |
| Spectral flow control over X (no zero modes) | Global spectral theory | NO | Spectral flow theorem for GU family |

## 8. Verdict

**CONDITIONALLY_RESOLVED** at reconstruction grade.

**Explicit failure conditions (precisely as required):**

**FC1 (Mass gap vanishes).** If Delta_N,1 = 0 (no positive discrete fiber Dirac eigenvalue),
the spectral projection P_disc has no discrete sector to project onto, and the entire A1
program collapses. This would occur if the tau-twisted fiber Dirac operator has no L^2
discrete spectrum, which is the non-compact analytic route failure established for the
scalar sector; for the spinor sector with tau-twisted coefficient the question remains open
analytically, though the APS/K3 reconstruction gives a 24-dimensional kernel consistent with
discrete spectrum existence.

**FC2 (Gap to continuum closes).** If there exists a discrete eigenvalue of D_GU in the
tau-twisted sector at Delta_N = 81/(4R_s^2) (exactly at the continuum threshold), the
Riesz projection P_disc has a divergent norm even at fixed x in X, because the contour
integral for the spectral projection cannot be separated from the continuous spectrum. The
current reconstruction gives the gap as (81/4 - 20)/R_s^2 = 1/(4R_s^2), which is very
small. Any computation finding an additional discrete mode in the interval [20, 81/4]/R_s^2
for the tau-twisted A3 system would trigger FC2 and make P_disc unbounded.

**FC3 (Eigenvalue zero mode in the GU family).** The explicitly exhibited failure family
(F-flat) shows that P_disc as the Riesz projection is unbounded on W^{1,2}_{H,delta} at
any section s_t where D_{s_t} has a zero mode in the discrete sector. The bounded
transform F_x = D_x(1+D_x^*D_x)^{-1/2} remains bounded at such points (it is defined
by functional calculus without requiring the gap), but P_disc as a Riesz projection is
unbounded there.

**FC4 (b-calculus fails at rank-3 corner).** If the rank-3 A3 fiber end is not controlled
by the available b-calculus / fibred-corners extension -- for example, if the rank-3
corner structure introduces non-trivial boundary interactions at the intersection of
Weyl-chamber walls that are not captured by the single-face b-calculus -- then the
compact-remainder parametrix Q_delta fails to give compact K_L, K_R on W^{1,2}_{H,delta},
and P_disc loses its W^{1,2} boundedness estimate.

**FC5 (Harish-Chandra resolvent pole for S(6,4)).** If the Harish-Chandra resolvent for
the Dirac operator with coefficient bundle S(6,4) has a pole at a complex spectral parameter
value inside the contour defining P_disc -- i.e., if there is a "ghost" resonance in the
tau-twisted discrete sector that is not a physical L^2 eigenvalue but disrupts the meromorphic
extension -- then P_disc picks up a contribution from the resonance, which is not bounded
on W^{1,2}_{H,delta} (resonance modes grow polynomially at infinity, not L^2). This is the
scattering-theory analogue of the tau-twisted route failure.

**FC6 (Spectral flow zero over X).** If the spectral flow of the family {D_x} over the
observer parameter space X has sf = 0 (the number of eigenvalue crossings through zero
counted with sign is zero), then the K-theory class of the family is trivial,
[D_GU] = 0 in KSp^0(X). This would not directly make P_disc unbounded, but it would
make the entire A1 program empty: P_disc would project onto a trivial sector.

**FC7 (No discrete series for scalar sector on non-compact fiber — added 2026-06-23, MO-07).**
SL(4,R) has no scalar discrete series: rank(G) = 3, rank(K) = rank(SO(4)) = 2, and
3 ≠ 2 violates the Harish-Chandra criterion. Therefore the scalar sector of D_GU on the
SL(4,R)/SO_0(3,1) fiber has no L^2 discrete spectrum. If the tau-twisted spinor sector
S(6,4) also fails to generate discrete L^2 spectrum on this fiber (which is the unverified
case), then P_disc has no non-empty discrete sector to project onto on non-compact Y^14.
Gate A1 would then be vacuously satisfied (P_disc = 0 is trivially bounded) but physically
empty: no discrete mode count, no KK spectrum, no analytic confirmation of ind_H = 24.
This is the deepest unanswered question in the A1 program.

**FC8 (Tau-twist S(6,4) fails to generate discrete L^2 spectrum on A3 fiber — added
2026-06-23, MO-07).** The APS/K3 route gives ind_H(D_GU) = 24 on the compact K3 factor,
consistent with a 24-dimensional kernel. This does not establish that the tau-twisted Dirac
operator on the non-compact SL(4,R)/SO_0(3,1) fiber has L^2 discrete eigenfunctions. The
absence of scalar discrete series means the non-compact fiber Dirac operator may have purely
continuous L^2 spectrum even in the twisted spinor sector, if the twisting is insufficient
to generate square-integrable modes. If this failure condition is triggered, all three
framework candidates (b-calculus, scattering, Melrose-Piazza) yield P_disc = 0 (trivially
bounded but empty), and the entire non-compact Y^14 analytic program for A1-A5 collapses
onto the APS/K3 route as the only source of spectral information.

**FC9 (Gate A1 is non-load-bearing because APS/K3 route is primary — added 2026-06-23,
MO-07).** If the APS/K3 route (oc1-oc2-aps-closure, ind_H = 24 at reconstruction grade)
is the primary derivation path and the non-compact Y^14 analytic program is secondary,
then Gate A1 may not be load-bearing for the main program. In this case, the CONDITIONALLY_RESOLVED
verdict for A1 is correct in the narrow sense (the frameworks supply boundedness conditional
on non-empty discrete sector) but mislabeled as a primary gate. The correct classification
would be: A1 is an open secondary question for the non-compact analytic program, not a gate
on the primary K3/APS/KSp route. This does not falsify the current analysis but changes its
priority weight in the overall OC2 program.

## 9. What Remains Open

(R1) Explicit Harish-Chandra resolvent computation for D_GU with S(6,4) coefficient bundle
     on the A3 symmetric space. This is the primary representation-theoretic gate that cannot
     be discharged from GU first principles without external input.

(R2) Classification of discrete modes for the tau-twisted A3 system in the interval
     [20, 81/4]/R_s^2. If this interval contains no discrete modes, the spectral gap
     condition S-ii is established and FC2 is ruled out.

(R3) Spectral flow of the GU family over the observer parameter space X. This requires a
     global analysis of the moduli space A(Y^14, Sp(64)) x Gamma(Y^14, X^4) and the
     locus where D_GU has zero modes. The Atiyah-Jannich theorem guarantees that the
     index is stable, but the spectral flow may be nonzero, meaning zero modes occur
     but pair up between ingoing and outgoing contributions.

(R4) Rank-3 fibred-corners b-calculus for D_GU. This requires adapting the Melrose
     multi-body calculus or the Vasy 0-calculus for symmetric spaces to the GU spinor
     bundle. At the level of the dilaton R^+ end alone, the standard b-calculus suffices
     (single boundary face); the full A3 corner requires the generalization.

## 10. Summary for OC2 Progress

The gate A1 (P_disc bounded on W^{1,2}_{H,delta}) is CONDITIONALLY_RESOLVED:

- The b-calculus + Melrose-Piazza spectral section framework supplies A1 at all generic
  points in the GU moduli space (away from the zero-mode subvariety Z).
- The explicit failure family (F-flat) exhibits P_disc unbounded on W^{1,2}_{H,delta} at
  section deformations where eigenvalues cross zero; this is not a global obstruction but
  a local singularity of the Riesz projection.
- Four conditions are dischargeable from GU first principles (mass gap, weight window,
  H-linearity, equivariance); four require new input (rank-3 corner calculus, Harish-Chandra
  resolvent for twisted spinors, classification of discrete modes in narrow gap, spectral
  flow control).
- The Melrose-Piazza framework is identified as the correct bridge between pointwise
  b-Fredholmness (established at reconstruction grade) and the smooth-family, norm-continuous
  bounded transform (needed for KSp classification).

The overall OC2 status remains CONDITIONALLY_RESOLVED. Gate A1 does not introduce a new
obstruction beyond what was already named in oc2-b-parametrix-y14 (A1-A5). It clarifies
which parts of A1 are dischargeable and identifies the Melrose-Piazza spectral section as
the correct technical tool for the smooth-family part, with the rank-3 fibred-corners
extension as the primary remaining analytic input.
