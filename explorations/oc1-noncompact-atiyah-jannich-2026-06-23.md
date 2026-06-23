---
title: "OC1: Non-Compact Atiyah-Jannich for D_GU on Y^14"
date: 2026-06-23
problem_label: "oc1-noncompact-atiyah-jannich"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# OC1: Non-Compact Atiyah-Jannich for D_GU on Y^14

## 1. Problem Statement

Gate OC1 for the signed-readout boundary theorem (Parts Z and K):

> Establish the non-compact Atiyah-Jannich theorem for the H-linear Fredholm operator
> D_GU on the non-compact manifold Y^14. Show either:
>
> (A) D_GU is Fredholm in L^2 with appropriate weighted Sobolev spaces, giving a
>     well-defined index; or
> (B) identify the precise obstruction and what additional structure (boundary
>     conditions, APS, L^2 kernel) is needed.
>
> **Failure condition:** if D_GU is genuinely non-Fredholm with no natural completion,
> the integer-valued index is ill-defined and OQ3b/OQ3c collapse.

This file gives a self-contained OC1 analysis building on the prior work in
`signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md` and the discrete-series
computation in `n5-discrete-series-gl4r-2026-06-23.md`. The goal is to determine
which path (A or B) holds for D_GU on Y^14, and to state the result with explicit
failure conditions.

---

## 2. Established Context

The following are inputs, not derived here.

- **Y^14 = Met(X^4)**: non-compact fiber bundle, fiber GL(4,R)/O(3,1) ~= RP^3. Non-compact.
- **D_GU**: H-linear Dirac-type operator on L^2(Y^14, H^64); principal symbol c(xi),
  satisfying c(xi)^2 = g_Y(xi,xi) Id_S (Clifford identity, verified grade).
- **Split signature**: gimmel metric g_Y has signature (9,5); D_GU is NOT elliptic
  (characteristic variety = null cone). Ellipticity is therefore NOT a route to Fredholmness.
- **Flensted-Jensen discrete-series mechanism** (n5-discrete-series §10-18, CONDITIONALLY_RESOLVED):
  SL(4,R)/SO_0(3,1) has split-rank 1 (verified); L^2_disc(SL(4,R) x_{SO_0(3,1)} S(6,4))
  is non-trivial; ind_H(D_GU)|_{L^2_disc} = 24 at reconstruction grade.
- **H-linearity**: D_GU commutes with right-H multiplication on S = H^64; ker and coker
  are H-modules; the natural index is ind_H = dim_H ker - dim_H coker in Z.
- **Clifford identity**: c(xi)^2 = g_Y(xi,xi) Id_S is loop-exact (algebraic, independent
  of gauge field A); this is the VZ evasion engine and the energy-estimate engine.

---

## 3. Path A: Fredholmness via Weighted Sobolev Spaces

### 3.1 Why Standard L^2 Elliptic Theory Fails

On a compact Riemannian manifold, a first-order elliptic operator D is Fredholm on
Sobolev spaces W^{k,2} because the symbol c(xi) is invertible for xi != 0 (elliptic),
making D a Fredholm operator between W^{k,2} and W^{k-1,2} with a parametrix.

Y^14 is non-compact, and D_GU is NOT elliptic (null-cone characteristic variety).
Therefore the standard route fails on TWO separate grounds:

1. **Non-compactness**: even elliptic operators can fail to be Fredholm on non-compact
   manifolds (e.g., the ordinary Dirac operator on R^n has continuous spectrum and
   is NOT Fredholm on unweighted L^2).

2. **Non-ellipticity**: even on compact manifolds, a non-elliptic operator is not
   Fredholm between standard Sobolev spaces (cokernel is infinite-dimensional in general).

### 3.2 The Correct Framework: L^2 Spectral Theory on the Symmetric Space Fiber

The relevant mechanism for D_GU is NOT elliptic parametrix theory. It is:

**L^2 harmonic analysis on the non-compact symmetric space GL(4,R)/O(3,1).**

The key insight from Atiyah-Schmid (1977) and Flensted-Jensen (1980) is:

> For a G-invariant differential operator D on a Riemannian symmetric space G/K,
> the L^2 spectral theory decomposes into:
>   (1) a continuous spectrum component (generalized eigenfunctions, not L^2);
>   (2) a discrete spectrum component L^2_disc(G/K) consisting of genuine L^2
>       eigenfunctions.
> The operator restricted to L^2_disc is compact-resolvable and has a well-defined
> index when L^2_disc is finite-dimensional or carries a finite-rank K-type structure.

For D_GU on Y^14, the fiber direction produces the Harish-Chandra decomposition:

```
L^2(Y^14, H^64) = L^2_disc(Y^14, H^64) oplus L^2_cont(Y^14, H^64)
```

The **discrete summand** L^2_disc is the relevant domain for the Fredholm theory.

### 3.3 Fredholmness on L^2_disc: The Atiyah-Schmid Mechanism

**Claim (reconstruction grade):** D_GU, restricted to L^2_disc(Y^14, H^64) via the
spectral projection P_disc, is Fredholm as an H-linear operator.

**Argument:**

Step 1. *Spectral gap.* On the discrete-series sector, the Casimir operator C_{sl(4,R)}
acts with eigenvalue C_2(pi) = 7/2 (computed explicitly in n5-discrete-series §18;
af1-corrected). This eigenvalue is isolated from the continuous spectrum (which begins
at |rho|^2 = (9/2)^2 = 81/4 in the Plancherel decomposition). Therefore D_GU|_{L^2_disc}
has a spectral gap from zero: zero is not in the essential spectrum of D_GU^* D_GU
on L^2_disc.

Step 2. *Essential spectrum exclusion.* For a Dirac-type operator D on a non-compact
space, the essential spectrum of D on L^2 is determined by the behavior of D at infinity
(Weyl's theorem in the non-compact Riemannian setting). In the symmetric-space fiber
GL(4,R)/O(3,1), the asymptotic operator at the non-compact end is the radial part of
D_GU on the abelian factor A of the Iwasawa decomposition G = KAN. The Flensted-Jensen
discrete series vectors decay exponentially at the A-infinity end (their matrix
coefficients satisfy |<pi(g)v, w>| <= C exp(-rho(log a(g))) for g -> A-infinity), so
the discrete-series sector is insensitive to the behavior of D_GU at infinity. The
essential spectrum of D_GU|_{L^2_disc} is therefore empty (the sector P_disc L^2 is
a closed invariant subspace on which the resolvent is compact).

Step 3. *Finite H-kernel and H-cokernel.* The L^2 kernel of D_GU on the discrete-
series sector consists of harmonic spinors in L^2_disc. The dimension is finite (the
Atiyah-Schmid formal degree sum gives dim_H ker = 24 at reconstruction grade) because
the discrete series are finite-multiplicity representations.

Step 4. *Closed range.* On L^2_disc, D_GU has a spectral gap from zero (Step 1), so
its range is closed. This is the key point: closed range fails on L^2_cont because
zero is an accumulation point of the spectrum there.

**Conclusion (Path A):** D_GU restricted to the discrete-series sector P_disc L^2(Y^14, H^64)
IS Fredholm, with:
```
ind_H(D_GU|_{L^2_disc}) = dim_H ker - dim_H coker = 24 - 0 = 24
```
at reconstruction grade (ind_H = 24 from n5-discrete-series; coker = 0 from chirality
argument: the Dirac-DeRham complex is self-adjoint under the gimmel inner product with
Sp(64) gauge group, so D_GU^* on L^2_disc has the same Fredholm property and
ind_H(D_GU^*) = -ind_H(D_GU) = -24 while dim_H coker(D_GU) = dim_H ker(D_GU^*) = 0
by the discrete-series-sector analytic structure).

### 3.4 The Weighted Sobolev Space Formulation

To make Path A rigorous at verified grade, one works with the weighted Sobolev spaces
adapted to the symmetric space geometry:

**Definition.** For delta in R (the weight), define:
```
L^2_delta(Y^14, S) = { psi in L^2_loc : ||psi||^2_{L^2_delta} = int_{Y^14} |psi(y)|^2 e^{2 delta r(y)} dvol_gg < infty }
```
where r(y) is the distance from a basepoint in the fiber direction (Riemannian distance
on GL(4,R)/O(3,1)).

**Key property.** For delta > 0 (exponential weight toward the non-compact end), the
Sobolev embedding and compactness properties are restored for the discrete-series sector:
- The spectral projection P_disc is bounded on L^2_delta for all delta (the discrete-
  series functions decay faster than any exponential).
- The operator D_GU: W^{1,2}_delta -> L^2_delta is a Fredholm operator for appropriate
  delta determined by the spectral gap rho = 9/2 of the Harish-Chandra c-function.
  Specifically, Fredholmness holds for delta in (-rho, 0) using the standard weighted
  L^2 theory for symmetric-space operators (Mazzeo-Melrose b-calculus or scattering
  calculus approach).

**Caveat (reconstruction grade):** The explicit Sobolev estimate
```
||psi||_{W^{1,2}_delta} <= C (||D_GU psi||_{L^2_delta} + ||psi||_{L^2_delta})
```
requires proving that D_GU has a parametrix in the weighted b-calculus of Melrose.
For a non-elliptic operator in split signature, the standard b-calculus does not
directly apply; one must work in a microlocal framework (e.g., the edge calculus
for the fiber-bundle structure of Y^14 -> X^4, or the Mazzeo-Melrose calculus for
asymptotically hyperbolic spaces).

The correct functional framework is therefore:

> **Path A, precise form:** D_GU is Fredholm on the weighted Sobolev space W^{1,2}_delta
> for delta in (-rho, 0) on the DISCRETE SECTOR, and has ind_H = 24 on that sector.
> The operator is NOT Fredholm on the full (unweighted) L^2 space; the continuous
> spectrum gives an infinite-dimensional kernel in L^2.

---

## 4. Path B: Identification of the Obstruction

If D_GU is NOT Fredholm (which would occur if the discrete sector is empty or if the
spectral gap closes), the precise obstruction is:

**B1. Discrete sector may be empty if limit-of-discrete-series.**

The highest-risk structural failure identified in `weyl-group-s4-orbit-2026-06-23.md`
(OQ-weyl-3): lambda_RS = (1/2, 0, 0, -1/2) lies on the root wall <e_2-e_3, lambda_RS> = 0,
which is the limit-of-discrete-series boundary in the Plancherel decomposition. At this
wall, the Plancherel measure for SL(4,R) may have zero mass (tempered discrete series
vanishes at the wall boundary). If this occurs:

- L^2_disc for S(6,4) is empty.
- D_GU has no L^2 harmonic spinors.
- ind_H(D_GU)|_{L^2_disc} = 0.
- OQ3b and OQ3c collapse; the generation count mechanism fails.

This is OQ3 in `oq-weyl3-limit-discrete-series-2026-06-23.md` and is the primary
remaining structural check.

**B2. Spectral gap may close under deformations.**

If D_GU is deformed (e.g., by varying the Sp(64) gauge field A), the spectral gap
from zero may close, allowing zero to enter the essential spectrum. This would:

- Destroy Fredholmness of D_GU|_{L^2_disc}.
- Make ind_H(D_GU) discontinuous under deformations.
- Break the Atiyah-Jannich stability argument for the signed-readout theorem.

The protection mechanism is the Atiyah-Schmid A-independence result
(signed-readout-oq2d-gu-contact): the Flensted-Jensen discrete spectrum of
L^2_disc(SL(4,R) x_{SO_0(3,1)} S(6,4)) is determined by symmetric-space geometry
alone and does NOT depend on the gauge field A. If this is correct, the spectral gap
cannot be closed by A-deformations.

**B3. Continuous spectrum may obstruct Fredholmness even on the discrete sector.**

In some non-compact settings, the projection P_disc is not a bounded operator on
standard L^2 spaces (e.g., if the spectrum has no gap from the continuous part). For
GL(4,R)/O(3,1) with S(6,4), the Harish-Chandra c-function places the discrete poles
at rho^2 - nu_n^2 for nu_n = (2n+1)/2 in the BC_1 case; the continuous spectrum
starts at rho^2. There IS a spectral gap of size rho^2 - nu_3^2 = (9/2)^2 - (7/2)^2 = 81/4 - 49/4 = 8/R_s^2
between the highest discrete pole nu_3 = 7/2 and the continuous spectrum bottom rho = 9/2.
This gap is consistent with the RC3 delta-N spectrum ({8, 14, 18, 20}/R_s^2 vs
continuous at 81/4 = 20.25/R_s^2 -- the continuous threshold is just above the
highest discrete pole). So B3 is not an obstruction for the known RC3 spectrum.

---

## 5. Synthesis: Verdict for OC1

### 5.1 What Path A Establishes (at Reconstruction Grade)

| Property | Status | Evidence |
|---|---|---|
| D_GU is non-elliptic | RESOLVED (exact) | c(xi)^2 = g_Y(xi,xi)Id; null-cone characteristic variety (sc1-oq2-ellipticity) |
| Standard L^2 Fredholmness fails | RESOLVED (exact) | Continuous spectrum fills essential spectrum on full L^2 |
| Discrete-series sector exists | CONDITIONALLY_RESOLVED | Flensted-Jensen split-rank=1 (verified); c-function poles at nu_n=(2n+1)/2 (rc3-harish-chandra) |
| Spectral gap from zero on L^2_disc | CONDITIONALLY_RESOLVED | C_2(pi)=7/2, continuous spectrum at rho^2=81/4, gap = 8/R_s^2 (RC3) |
| D_GU is Fredholm on L^2_disc | CONDITIONALLY_RESOLVED | Spectral gap + exponential decay + finite H-kernel |
| ind_H(D_GU)|_{L^2_disc} = 24 | CONDITIONALLY_RESOLVED | n5-discrete-series §18; three convergent routes |
| Weighted Sobolev W^{1,2}_delta formulation | SKETCH (exploration grade) | Standard approach; b-calculus or edge-calculus needed |
| A-independence of spectral gap | CONDITIONALLY_RESOLVED | Atiyah-Schmid symmetry-space determination (oq2d-gu-contact) |

### 5.2 What Remains to Upgrade OC1 to RESOLVED

**Primary gate: OQ-weyl-3 (limit-of-discrete-series check).**

The lambda_RS root-wall issue must be resolved. If lambda_RS lies on a wall where the
Plancherel measure has zero weight, the discrete sector is empty and OC1 collapses.
The wall in question is <e_2 - e_3, lambda_RS> = 0. In the BC_1 root system (established
in rc3-harish-chandra), the relevant simple root for the discrete-series boundary is
the short root alpha_1. The explicit c-function formula
```
c(lambda) = c_0 * Gamma(i lambda R_s) * Gamma(i lambda R_s + 1/2) / [Gamma(i lambda R_s + 9/2) * Gamma(i lambda R_s + 5/2)]
```
has poles at nu_n = (2n+1)/2 (n=0,1,2,3) from the Gamma(i lambda + 1/2) factor, and
these poles are IN the interior of the Plancherel strip (not on the wall of the positive
Weyl chamber for A_3). The BC_1 computation uses the involution sigma_B (metric-
conjugation, giving the correct pair SL(4,R)/SO_0(3,1) with split-rank 3). The
tau-correction used in oq3b-rs-index-8 reduces the effective split-rank to 1 for the
twisted L^2(G x_H tau_RS); the poles survive this reduction.

Assessment: the limit-of-discrete-series risk from the A_3 root-wall analysis is at
the boundary of the SIGMA_B involution's Weyl chamber, not the Plancherel support for
the BC_1 effective operator. The Plancherel poles at nu_n = (2n+1)/2 are in the
interior of the Weyl chamber for BC_1. The risk is NOT resolved at verified grade but
the structural evidence strongly suggests the discrete sector is non-empty (the poles
exist and are in the interior). This is the primary gap between CONDITIONALLY_RESOLVED
and RESOLVED.

**Secondary gate: Explicit parametrix construction.**

To upgrade the Fredholmness claim from the spectral argument to a verified proof, one
needs an explicit parametrix for D_GU|_{L^2_disc} in a microlocal sense:
```
Q_disc * D_GU = P_disc + K_L   (K_L compact)
D_GU * Q_disc = P_disc + K_R   (K_R compact)
```
This requires either:
- The b-calculus parametrix for the asymptotic operator of D_GU at the A-infinity end
  of G/K (Melrose-Mazzeo, applicable to asymptotically hyperbolic spaces);
- The Harish-Chandra analytic theory for global parametrices on symmetric spaces;
- Or a Fourier analysis argument using the Plancherel decomposition of L^2(G/K).

At reconstruction grade, the Plancherel argument is the most accessible:

> The projection onto the discrete summand kills the continuous spectrum;
> on the discrete summand, D_GU is a bounded operator with a bounded inverse (spectral
> gap) composed with P_disc, giving the parametrix.

This argument is correct in structure but requires care about: (a) whether P_disc is
bounded on the relevant Sobolev space; (b) whether D_GU P_disc = P_disc D_GU exactly
(G-invariance); (c) whether the spectral gap is uniform over the gauge-field moduli.
All three are expected to hold but have not been verified in coordinate or CAS form.

---

## 6. Failure Conditions

**F1: Discrete sector is empty (OQ-weyl-3 fires).** If the Plancherel measure for
S(6,4) on SL(4,R)/SO_0(3,1) has zero weight at the discrete poles (limit-of-discrete-
series), then L^2_disc is empty, D_GU has no Fredholm structure, and the index is 0
(not 24). Signatures: all three convergent routes to ind_H = 8 (RS) simultaneously fail;
the formal-degree sum 225/48 evaluates to zero at the wall.

**F2: Spectral gap closes under gauge deformations.** If D_GU(A) for some gauge field
A has zero in its L^2_disc essential spectrum (closing the 8/R_s^2 gap), Fredholmness
fails for that A. The A-independence argument (Atiyah-Schmid symmetry-space determination)
would need to be wrong for this to occur. Signature: Casimir eigenvalue C_2(pi_A) =
C_2(pi_{A=0}) for all A; if any gauge field shifts C_2, the gap could close.

**F3: tau-rank-correction formula is wrong.** The oq3b-rs-index-8 argument uses
rank_correction = 2 (from SL(2,C) structure of SO_0(3,1)) to reduce effective split-rank
from 3 to 1 for the twisted L^2(G x_H tau_RS). If this formula is incorrect (no
Kobayashi-Oda reference has been verified), the BC_1 c-function derivation is invalid;
the correct restricted root system for the twisted problem may be A_3, in which case
the discrete poles may not exist at nu = 3/2 and the whole Fredholm chain collapses.

**F4: P_disc is NOT bounded on W^{1,2}_delta.** If the spectral projection onto the
discrete sector is not bounded in the weighted Sobolev topology, the Fredholm argument
for D_GU|_{L^2_disc}: W^{1,2}_delta -> L^2_delta fails. This would require working in a
different functional framework (e.g., higher exponential weights).

**F5: D_GU has genuinely infinite-dimensional kernel on L^2_disc.** This would
require the Atiyah-Schmid multiplicity to be infinite, which is excluded by the finite-
multiplicity theorem for discrete series of semisimple Lie groups. If GL(4,R)/O(3,1)
is not a proper semisimple symmetric pair in the relevant sense, this protection fails.

---

## 7. Relationship to OC2

OC1 establishes Fredholmness and integer-valuedness of ind_H (Part Z of the signed-
readout theorem). OC2 further requires that this Fredholm index lifts to a class in
KSp^0(X) for a compact observer parameter space X (Part K). The relationship is:

- OC1 is necessary for OC2: without Fredholmness, no K-theory class.
- OC1 is not sufficient for OC2: even with Fredholmness, the K-theory lift requires
  a continuous family over X and a compact Hausdorff parameter space X.

OC1 can be RESOLVED independently of OC2. The integer index ind_H = 24 follows from
OC1 alone; the K-theory class in KSp^0(X) requires OC2.

---

## 8. Grade Assessment

The OC1 argument achieves **reconstruction grade** at best. The full verified proof
requires:

1. Explicit Plancherel formula for the fiber operator D_fib on GL(4,R)/O(3,1) twisted
   by S(6,4), showing discrete poles exist at the correct locations.
2. Spectral gap estimate ||D_GU|_{L^2_disc} psi||_{L^2} >= (8/R_s^2)^{1/2} ||psi||_{L^2}
   for all psi in L^2_disc with D_GU psi in L^2_disc.
3. Bounded-operator compactness of the parametrix remainder K_L and K_R.
4. Verification of rank_correction = 2 in the tau-corrected Flensted-Jensen theorem.
5. Root-wall non-degeneracy: Plancherel measure is non-zero in a neighborhood of the
   discrete poles (OQ-weyl-3 explicit computation).

---

## 9. Verdict

**OC1 verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

Path A holds in structure: D_GU is Fredholm on the discrete-series sector L^2_disc
with ind_H = 24 via the Atiyah-Schmid / Flensted-Jensen mechanism. The non-compact
issue is not an obstruction in principle (the discrete spectrum is L^2-complete and
spectrally isolated). The integer-valued index is well-defined on L^2_disc.

Path B: the obstruction to upgrading to RESOLVED is:
1. OQ-weyl-3 (limit-of-discrete-series root-wall check) -- the primary structural gate.
2. tau-rank-correction = 2 verification (Kobayashi-Oda / Oshima reference check).
3. Explicit weighted-Sobolev parametrix construction in the b-calculus or scattering
   calculus.

The failure condition for OC1 -- "D_GU is genuinely non-Fredholm with no natural
completion" -- does NOT hold: the discrete sector provides the natural completion, and
Fredholmness holds there. OQ3b/OQ3c do not collapse; they are gated on the root-wall
check, not on an absence of Fredholm structure.

**Remaining to RESOLVED:**
- OQ-weyl-3: root-wall Plancherel non-degeneracy (primary gate).
- tau-rank-correction = 2 reference (secondary gate).
- Explicit parametrix in b-calculus or scattering calculus (tertiary, proof upgrade).
