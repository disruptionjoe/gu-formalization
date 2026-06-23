---
title: "OC2: b-Parametrix and Indicial Roots for D_GU on Noncompact Y^14"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "oc2-b-parametrix-y14"
verdict: "CONDITIONAL_DISCRETE_SECTOR_FREDHOLM; FULL_UNPROJECTED_b-FREDHOLM_NOT_DEFENSIBLE; WEIGHT_WINDOW_IDENTIFIED_CONDITIONALLY"
---

# OC2: b-Parametrix and Indicial Roots for D_GU on Noncompact Y^14

## 1. Scope

This note executes the b-calculus / scattering-parametrix program for D_GU on noncompact
Y^14 that was formulated but not completed in the two predecessor notes:

- `explorations/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md`
- `explorations/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md`

Tasks:

1. Choose a weight function on Y^14.
2. Define the weighted conjugate D_delta and identify the end model.
3. Compute the indicial family I(D_GU, lambda) at the noncompact end.
4. Identify the indicial roots and the weight window for Fredholmness.
5. State the Fredholm result on the projected/discrete sector.
6. Name explicit failure conditions.

The treatment is reconstruction-grade throughout. CAS verification of eigenvalue
formulas is deferred.

## 2. End Geometry of Y^14

### 2.1 Fiber structure

Y^14 = Met(X^4) fibers over X^4 with fiber F = GL(4,R)/O(3,1).

From the N6 computation:

```text
F = GL(4,R)/O(3,1) ~= R^+ x SL(4,R)/SO_0(3,1).
```

The noncompact fiber has a canonical radial direction r coming from the dilatation R^+
factor (r = log of the overall conformal scale of the metric). The semisimple part
SL(4,R)/SO_0(3,1) is a symmetric space of split rank 3 with restricted root system A_3
(from the OQ1 split-rank computation).

### 2.2 The relevant end

The noncompact end of F is reached as r -> +infinity (large conformal factor; metrics
with large overall scale). Along this end, the fiber metric degenerates. The geometry of
the end is approximately:

```text
F_end ~= R^+ x (SL(4,R)/SO_0(3,1)) / (compact).
```

For a rank-one symmetric space the end is asymptotically hyperbolic; for split-rank-3
A_3 the end is more complex (rank-3 corner). However the conformal-scale direction R^+
is genuinely rank-one and cylindrical (dr^2 + g_{sph}), so the correct operator calculus
near the dilaton end is the b-calculus (cylindrical end model).

We compactify the R^+ factor by setting x = e^{-r}, so r -> +infinity becomes x -> 0.
The b-tangent bundle near x = 0 has basis {x d/dx, d/dy^a} where y^a are base and
angular coordinates at fixed r.

### 2.3 Weight function

Define:

```text
r : Y^14 -> [0,+infinity)
```

as the log-conformal-scale coordinate on the fiber, extended to Y^14 by fiber projection.
The weight function is:

```text
w_delta(y) = e^{delta r(y)},   delta in R.
```

The weighted Hilbert space and domain are:

```text
L^2_{H,delta}(Y^14, S) = { psi : e^{delta r} psi in L^2_H(Y^14, S) }

W^{1,2}_{H,delta}(Y^14, S) = { psi : e^{delta r} psi in W^{1,2}_H(Y^14, S) }.
```

Equivalently, define the conjugated operator:

```text
D_delta = e^{delta r} D_GU e^{-delta r}.
```

D_delta acts on unweighted L^2_H and has the same H-linear algebraic structure as D_GU,
since conjugation by a scalar weight commutes with all H-linear algebraic operations.

## 3. Indicial Family

### 3.1 Setup

In the b-calculus on a manifold with boundary at x = 0, the indicial family of a
first-order b-differential operator P is:

```text
I(P, lambda) = x^{-lambda} P x^{lambda}|_{x=0},
```

acting on sections over the boundary face at x = 0. Fredholmness of P on the b-Sobolev
space H^1_b(x^delta L^2) fails precisely when I(P, delta + lambda) is not invertible
for some lambda in iR (the imaginary axis).

For the weighted operator D_delta = e^{delta r} D_GU e^{-delta r}, the indicial family
of D_GU at the end r -> +infinity is:

```text
I(D_GU, lambda) = D_GU|_{normal} (lambda),
```

the normal operator: the leading-order piece of D_GU in the normal direction d/dr
evaluated with d/dr replaced by the spectral parameter i lambda.

### 3.2 Structure of D_GU near the end

In a local b-frame, D_GU = Gamma^r (x d/dx) + D_tang, where:

- Gamma^r is the Clifford multiplication by the radial unit covector dr;
- D_tang is the tangential part (b-tangential first-order operator).

Conjugating by x^delta = e^{-delta r} shifts d/dr -> d/dr - delta, so:

```text
D_delta = Gamma^r (x d/dx - delta) + D_tang.
```

The indicial family is:

```text
I(D_GU, lambda) = Gamma^r (i lambda - delta) + D_tang|_{r=infty}.
```

The indicial roots are the values lambda_j in C such that I(D_GU, lambda_j) is not
invertible as an operator on L^2 at the boundary face.

### 3.3 Radial Clifford element

From Cl(9,5) ~= M(64,H) and the fiber signature (6,4):

```text
(Gamma^r)^2 = g_Y(dr, dr) Id_S.
```

At the conformal-scale end, dr is a spacelike direction (the dilaton direction in the
(9,5)-signature fiber). So:

```text
(Gamma^r)^2 = +1 Id_S   (spacelike).
```

Gamma^r is therefore an invertible H-linear operator on S = H^64, with (Gamma^r)^{-1}
= Gamma^r (since (Gamma^r)^2 = 1).

### 3.4 Indicial equation

The indicial family I(D_GU, lambda) is invertible unless:

```text
det_{H} [ Gamma^r (i lambda - delta) + D_tang ] = 0.
```

Rewriting using Gamma^r invertibility:

```text
I(D_GU, lambda) psi = 0
<=> (i lambda - delta) psi = -(Gamma^r)^{-1} D_tang psi
<=> (i lambda - delta) psi = -Gamma^r D_tang psi.
```

So the indicial roots are:

```text
i lambda - delta = mu_j,
```

where mu_j are the eigenvalues of -Gamma^r D_tang at the boundary face.

Equivalently:

```text
lambda_j = -i(delta + mu_j)   for each eigenvalue mu_j of -Gamma^r D_tang.
```

### 3.5 Tangential operator at the end

D_tang|_{r=infty} is the Dirac-type operator on the boundary face, which is the product
structure SL(4,R)/SO_0(3,1) x X^4 at r = infty. Its eigenvalues are:

```text
{ mu_j } = spectrum(-Gamma^r D_tang|_{boundary}).
```

Two contributions:

(a) The fiber part: eigenvalues of the fiber Dirac operator on SL(4,R)/SO_0(3,1).

From the RC3 computation, the normal Laplacian Delta_N has discrete spectrum:

```text
{ 8, 14, 18, 20 } / R_s^2   (discrete part, reconstruction grade)
```

with continuum threshold at 81/(4 R_s^2). The fiber Dirac eigenvalues mu_fib satisfy
mu_fib^2 = Delta_N eigenvalues (Dirac-to-Laplacian), so:

```text
|mu_fib,j| in { 2sqrt(2), sqrt(14), 3sqrt(2), sqrt(20) } / R_s   (discrete sector)
|mu_fib| >= 9/(2 R_s)   (continuous threshold)
```

Note: the discrete values are reconstruction-grade from the BC_1 computation with
(m_1, m_2) = (7, 1) under the sigma_B involution (rc3-harish-chandra). The A_3
corrected root system gives the continuous Plancherel for the scalar sector; the
discrete values above are for the tau-twisted coefficient bundle S(6,4).

(b) The base part: eigenvalues of the Dirac operator on X^4 (horizontal piece).

For the Dirac operator on a compact X^4 (K3-type), the horizontal eigenvalues lambda_h
are the Dirac spectrum of s*(D_GU) on X^4, which is discrete and bounded below by the
Sobolev gap.

### 3.6 Indicial roots: explicit form

Combining, the indicial roots for the b-parametrix at the dilaton end are:

```text
lambda_j^{indicial} = -i(delta + mu_j)
```

where mu_j ranges over the spectrum of -Gamma^r D_tang at the boundary. In the
discrete-sector projection:

```text
Im(lambda_j^{indicial}) = -(delta + Re(mu_j)).
```

For D_GU to be Fredholm in the weighted b-calculus, the weight delta must satisfy:

```text
delta + Re(mu_j) != 0   for all j in discrete sector.
```

That is, delta must avoid the values:

```text
delta_j = -Re(mu_j) = -|mu_fib,j|   (taking Re(mu_j) = |mu_fib,j| for spacelike dr)
```

and also avoid the continuous threshold:

```text
delta_c = -9/(2 R_s).
```

### 3.7 Weight window for Fredholmness

The discrete fiber eigenvalues are (reconstruction grade):

```text
|mu_fib,1| = 2sqrt(2)/R_s ~= 2.83/R_s     (from Delta_N = 8/R_s^2)
|mu_fib,2| = sqrt(14)/R_s ~= 3.74/R_s     (from Delta_N = 14/R_s^2)
|mu_fib,3| = 3sqrt(2)/R_s ~= 4.24/R_s     (from Delta_N = 18/R_s^2)
|mu_fib,4| = sqrt(20)/R_s ~= 4.47/R_s     (from Delta_N = 20/R_s^2)
continuum: |mu_c| = 9/(2 R_s) = 4.50/R_s
```

The forbidden delta-values (indicial roots) are therefore:

```text
delta in { -2sqrt(2)/R_s, -sqrt(14)/R_s, -3sqrt(2)/R_s, -sqrt(20)/R_s, -9/(2R_s) }
plus the discrete tau-shifted spectrum of -Gamma^r D_tang on the horizontal X^4 part.
```

The weight windows where D_delta,disc is Fredholm on the discrete sector are the
intervals between consecutive forbidden values:

```text
Window 1: -2sqrt(2)/R_s < delta < 0   (between first indicial root and zero)
Window 2: -sqrt(14)/R_s < delta < -2sqrt(2)/R_s
Window 3: -3sqrt(2)/R_s < delta < -sqrt(14)/R_s
Window 4: -sqrt(20)/R_s < delta < -3sqrt(2)/R_s
Window 5: -9/(2R_s) < delta < -sqrt(20)/R_s
```

And the half-line:

```text
Window 0: 0 < delta < +infinity   (above the highest indicial root)
```

is the decay-requiring range where L^2 sections must decay at the end. This is the
natural range for L^2 normalizable sections.

**Natural choice:** delta in Window 0 (delta > 0, mild exponential growth allowed) or
Window 1 (-2sqrt(2)/R_s < delta < 0, mild exponential decay required).

For the discrete-sector Fredholm result, any delta in the interior of a window avoids
all indicial roots and the continuum threshold, giving a Fredholm operator.

## 4. Compact-Remainder Parametrix

### 4.1 Construction on the projected discrete sector

Assume:

1. P_disc is the tau-twisted relative discrete/residual projection (CONDITIONALLY
   established, contingent on the rc1-rs-kk-zero-mode and oq-kk1 computations).
2. delta is in Window 0 or Window 1 (avoiding all indicial roots from Section 3.7).
3. The operator D_delta,disc = P_disc e^{delta r} D_GU e^{-delta r} P_disc acts on
   K_H = L^2_{H,delta,disc}(Y^14, S).

On the discrete sector with these inputs, a b-parametrix is:

```text
Q_delta : L^2_{H,delta,disc} -> W^{1,2}_{H,delta,disc}
```

defined as follows.

**Spectral/resolvent piece:** On the tau-twisted discrete summands with nonzero eigenvalue:

```text
Q_disc = sum_{lambda_j != 0} lambda_j^{-1} P_j
```

where P_j are the finite-multiplicity spectral projections. This is well-defined when
the nonzero discrete spectrum is separated from zero (spectral gap condition).

**b-calculus piece at the end:** At the boundary face x = 0, the indicial family
I(D_GU, delta) is invertible (by the weight-window assumption), so a b-parametrix exists
near the end with residual terms in the residual b-calculus. In the b-calculus, residual
operators have all-order vanishing on the boundary face and are compact on L^2_b by
the weighted Rellich theorem.

The combined parametrix satisfies:

```text
Q_delta D_delta,disc = I_disc - Pi_ker + K_L
D_delta,disc Q_delta = I_disc - Pi_coker + K_R
```

where:

- Pi_ker is the finite-rank H-linear projection onto ker(D_delta,disc);
- Pi_coker is the finite-rank H-linear projection onto coker(D_delta,disc);
- K_L, K_R are compact on K_H = L^2_{H,delta,disc}.

The compactness of K_L, K_R follows from two sources:

1. Spectral-piece remainder: the finite-rank projectors P_j and P_ker are
   compact by finite-dimensionality.
2. b-calculus remainder: residual b-operators on the weighted space are
   compact by the Rellich-type theorem (residual b-kernels decay off-diagonal
   in the weighted double space).

### 4.2 Fredholm conclusion

By Atkinson's theorem for closed densely defined operators: a closed operator T with
closed range and finite-dimensional kernel and cokernel is Fredholm. The parametrix gives
exactly this: finite-rank Pi_ker, Pi_coker and compact K_L, K_R.

Therefore, under the stated assumptions:

```text
D_delta,disc : W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}
```

is Fredholm for delta in the weight windows of Section 3.7.

The Fredholm index is:

```text
ind_H(D_delta,disc) = dim_H ker(D_delta,disc) - dim_H coker(D_delta,disc).
```

By the APS route (established in oc1-oc2-aps-closure and oq-rk2-aps-boundary-rs-k3):

```text
ind_H(D_GU) = ind_H(A) + ind_H(S_R^{eff}) = 16 + 8 = 24
```

at reconstruction grade, assuming K3-type X^4 and APS boundary conditions on the
section-pullback domain.

The delta-independence of the Fredholm index (as long as delta stays within one weight
window) follows from homotopy invariance: two delta values in the same window give
Fredholm operators connected by a compact perturbation (the weight shift is a compact
correction on the discrete sector), and compact perturbations do not change the index.

## 5. The Unprojected Operator: What Cannot Be Claimed

For the full unprojected operator D_GU on all of L^2_{H,delta}(Y^14, S), the b-parametrix
program faces two structural obstructions:

**Obstruction 1: Split-signature null cone.**

The principal symbol of D_GU satisfies sigma(D_GU)(xi)^2 = g_Y(xi, xi) Id_S. The gimmel
metric g_Y has signature (9,5) on Y^14, so there is a null cone. On the null cone,
the principal symbol is not invertible. Therefore D_GU is NOT elliptic in the standard
sense. The b-calculus Fredholm theorem requires ellipticity (invertibility of the full
symbol away from zero section), which fails here.

**Obstruction 2: Continuous spectrum.**

The scalar L^2(SL(4,R)/SO_0(3,1)) Plancherel measure is absolutely continuous (no
scalar discrete series: split-rank 3, A_3 root system, FJ equal-rank fails for scalar
sector as established in rc1-root-mult-disambiguation and oq1-split-rank-verification).
The continuous spectrum persists in L^2_{H,delta}(Y^14, S) on the horizontal sector.
The b-parametrix construction requires the indicial family to be invertible, which fails
at the continuous spectrum threshold where the indicial family has continuous spectrum
rather than discrete eigenvalues.

Therefore:

```text
Full unprojected Fredholmness of D_GU on L^2_{H,delta}(Y^14, S) CANNOT be claimed.
```

The correct target remains the projected discrete sector D_delta,disc.

## 6. Bounded-Transform Continuity

For the KSp classification, the GU family requires a norm-continuous map:

```text
F_x = D_x(1 + D_x^* D_x)^{-1/2} : X -> Fred_H(K_H).
```

A sufficient analytic criterion (from oc2-y14-weighted-fredholm-parametrix, Section 6):

1. Identification of varying L^2 spaces by H-unitaries with one fixed K_H.
2. Common domain W^{1,2}_{H,delta,disc}.
3. Norm continuity of x |-> D_x as a bounded map between fixed Sobolev spaces.
4. Norm continuity of P_disc,x.
5. Uniform Fredholm gap: spectral gap does not close.
6. Functional calculus converting graph-norm continuity to norm continuity of the
   bounded transform.

On the b-calculus side, items 3 and 5 follow from:

- The b-parametrix is uniform in x when the GU operator coefficients (connection A and
  section s) vary continuously: the b-symbol and the indicial family vary continuously.
- The spectral gap is encoded in the distance from zero of the indicial roots. As long
  as delta stays strictly in the interior of a weight window, the indicial family stays
  invertible uniformly in x.

Items 1, 4, and 6 remain as operator-analysis inputs:

- Item 1 requires a unitary trivialization of the L^2 spaces over the parameter space X;
  this uses the fiber-bundle structure and is construction-grade.
- Item 4 requires P_disc,x to be norm continuous; this is a consequence of norm
  continuity of D_x and the spectral projection formula (Cauchy integral of the resolvent),
  provided the spectral gap is uniform.
- Item 6 is the functional-calculus theorem; in the H-linear setting this uses the
  bounded-transform spectral-theory for H-linear unbounded operators, which exists in
  principle but is not explicitly referenced here.

At reconstruction grade: items 3 and 5 are conditionally established by the b-parametrix
construction. Items 1, 4, 6 are assumed as analytic inputs with the stated sufficient
criteria.

## 7. Conditional Fredholm Theorem

**Theorem (OC2 b-parametrix on discrete sector, reconstruction grade).**

Let X be a compact Hausdorff observer parameter space. Let delta lie in the interior of
a weight window from Section 3.7, and let K_H = L^2_{H,delta,disc}(Y^14, S) with domain
W^{1,2}_{H,delta,disc}. Assume:

(A1) P_disc is a bounded H-linear orthogonal projection on L^2_{H,delta} and on
     W^{1,2}_{H,delta}, invariant under D_GU up to compact terms.
(A2) The tau-twisted discrete fiber spectrum is finite at each fiber and the discrete
     eigenvalues are separated from zero and from the continuum threshold.
(A3) The b-calculus indicial family I(D_GU, delta) is invertible at the dilaton end for
     the chosen delta (weight-window condition from Section 3.7).
(A4) The GU operator coefficients A_x and s_x vary continuously in x, making the
     b-symbol and indicial family uniformly invertible.
(A5) H-linear unitary trivialization of K_H over X exists, and the functional calculus
     gives norm-continuous bounded transforms.

Then:

(C1) D_delta,disc : W^{1,2}_{H,delta,disc} -> K_H is Fredholm for each x.
(C2) The parametrix Q_delta satisfies Q_delta D_delta,disc = I - Pi_ker + K_L and
     D_delta,disc Q_delta = I - Pi_coker + K_R with Pi_ker, Pi_coker finite-rank H-linear
     and K_L, K_R compact on K_H.
(C3) ind_H(D_delta,disc) = 24 (from APS route on K3-type X^4).
(C4) The bounded transforms F_x = D_x(1 + D_x^* D_x)^{-1/2} form a norm-continuous
     family X -> Fred_H(K_H), defining [D_GU] in KSp^0(X) = KO^4(X).
(C5) At each point, eps_x([D_GU]) = ind_H(D_x) = 24.

## 8. Indicial Root Summary Table

| Mode | Delta_N eigenvalue (rec. grade) | |mu_fib| | Indicial root delta_j | Window boundary |
|---|---|---|---|---|
| Discrete 1 | 8/R_s^2 | 2sqrt(2)/R_s ~= 2.83/R_s | -2.83/R_s | Window 0/1 boundary |
| Discrete 2 | 14/R_s^2 | sqrt(14)/R_s ~= 3.74/R_s | -3.74/R_s | Window 1/2 boundary |
| Discrete 3 | 18/R_s^2 | 3sqrt(2)/R_s ~= 4.24/R_s | -4.24/R_s | Window 2/3 boundary |
| Discrete 4 | 20/R_s^2 | sqrt(20)/R_s ~= 4.47/R_s | -4.47/R_s | Window 3/4 boundary |
| Continuum | threshold 81/(4R_s^2) | 9/(2R_s) ~= 4.50/R_s | -4.50/R_s | Window 4/5 boundary |

For delta in Window 0 (delta > 0): D_delta,disc is Fredholm in the decay-requiring
regime. Sections in ker(D_delta,disc) decay at the end, which is the natural L^2
condition.

For delta in Window 1 (-2.83/R_s < delta < 0): D_delta,disc is Fredholm allowing
mild growth at the end.

**Recommended weight:** delta in Window 0, specifically:

```text
delta = epsilon > 0   small
```

This is the standard L^2 (no growth) regime. Sections are squarely integrable at the
end. The indicial roots are all strictly negative, so the weight delta = epsilon > 0
avoids all of them.

## 9. Failure Conditions

The b-parametrix Fredholm result fails or downgrades under any of the following:

**F1. Indicial family non-invertible at chosen delta.**

If delta coincides with an indicial root (Section 3.7), I(D_GU, delta) is singular and
the b-calculus parametrix construction fails. This is the primary weight-selection
obstruction.

**F2. Tau-twisted discrete sector does not exist.**

If P_disc is not well-defined (tau_RS is not admissible for (SL(4,R), SO_0(3,1))), the
projected operator D_delta,disc is not a well-defined Fredholm operator. This is the
primary analytic gate established in the predecessor notes (scalar FJ route failed; APS
route survives at reconstruction grade).

**F3. Continuous spectrum enters the projected sector.**

If P_disc does not remove the continuous spectrum (e.g., P_disc is not an exact spectral
projection, or the tau-twisted coefficient system has continuous Plancherel support), the
projected operator D_delta,disc has essential spectrum at zero and is not Fredholm.

**F4. Principal symbol has null cone in the projected sector.**

Even after projection, if P_disc does not remove the null-cone directions of sigma(D_GU),
the projected operator fails ellipticity in those directions. This is not an obstruction
in the b-calculus (which works for normally-elliptic operators whose ellipticity is in
the b-cotangent bundle), but it must be checked that the projected operator is b-elliptic
(elliptic with respect to the b-symbol, which requires the symbol to be invertible on
the b-cotangent sphere, away from the zero section).

For the discrete sector, the fiber Dirac modes have definite mass (eigenvalues of Delta_N
are strictly positive) so the effective mass gap replaces ellipticity: the projected
operator is massive and the effective principal symbol is invertible. This is the
discrete-sector analogue of ellipticity.

**F5. Weight crosses the continuum threshold.**

If delta < -9/(2R_s), the weight crosses the continuum threshold of the unprojected
operator. Even on the projected sector, if the projection interacts with the continuous
spectrum at this weight, compactness of the residual terms may fail.

**F6. Spectral gap closes under deformation.**

If the GU parameter x varies and the discrete eigenvalues collide with zero or with the
continuum threshold (gap closes), the Fredholm property is lost at that point. This is
the uniform-in-x condition A4 above.

**F7. Bounded-transform non-continuity.**

If functional calculus fails to convert common-domain graph continuity to norm continuity
of F_x = D_x(1+D_x^*D_x)^{-1/2} in Fred_H, the KSp classification is not established
even if pointwise Fredholmness holds.

**F8. KK zero-mode unitarity failure.**

If the fiber modes varphi_j(x,n) are not smooth, not normalized, or not complete for
P_disc, the identification of the projected 14D Hilbert space with the 4D finite-rank
mode bundle fails, and ind_H(D_delta,disc) does not equal the APS index on X^4.

## 10. Status of Each Assumption

| Assumption | Status |
|---|---|
| A1: P_disc bounded on weighted Sobolev | CONDITIONALLY_ESTABLISHED (rc1, oq-kk1 give modes; full boundedness on W^{1,2}_{H,delta} not proved) |
| A2: Discrete eigenvalues separated from zero | CONDITIONALLY_ESTABLISHED (rc3, Delta_N spectrum discrete at 8/R_s^2 lowest) |
| A3: Indicial family invertible at chosen delta | ESTABLISHED for delta in weight windows (Section 3.7; contingent on A1 and A2) |
| A4: GU coefficients vary continuously | ASSUMED (follows from smooth section and connection data; standard functional analysis) |
| A5: H-linear unitary trivialization | ASSUMED (follows from fiber-bundle structure; needs explicit construction) |

## 11. Comparison with Predecessor Notes

The two predecessor notes established:

- The formal Fred_H -> KSp^0(X) classification (resolved).
- The H-linearity of D_GU and the H-linear Sobolev domain (resolved algebraically).
- The compact section-pullback Fredholmness on X^4 (resolved under APS).
- The conditional Fredholm theorem shape (conditional tau-discrete sector theorem).
- The failure of the full unprojected Y^14 b-Fredholm claim.

This note adds:

- An explicit weight function r = log-conformal-scale.
- An explicit indicial family computation I(D_GU, lambda) = Gamma^r(i lambda - delta) + D_tang.
- Explicit indicial roots and a weight window table.
- The recommended weight delta in Window 0 (delta > 0, natural L^2 regime).
- An explicit compact-remainder parametrix on the projected discrete sector.
- Delta-independence of the Fredholm index (homotopy within window).
- Named failure conditions F1-F8.

The primary remaining gap is unchanged: the tau-twisted discrete sector existence proof
(A1, A2) requires the Oshima-Matsuki/Kobayashi admissibility theorem for the actual GU
pair or the APS route on compact K3. The b-parametrix construction is contingent on
those inputs.

## 12. Final Verdict

**Verdict:** CONDITIONAL_DISCRETE_SECTOR_FREDHOLM; FULL_UNPROJECTED_b-FREDHOLM_NOT_DEFENSIBLE;
WEIGHT_WINDOW_IDENTIFIED_CONDITIONALLY.

The b-parametrix for D_GU on noncompact Y^14 is constructible on the tau-twisted
discrete sector for delta in the identified weight windows. The indicial roots are
explicitly named as the fiber Dirac eigenvalues {2sqrt(2), sqrt(14), 3sqrt(2), sqrt(20)}/R_s
with continuum threshold 9/(2R_s). The natural weight Window 0 (delta > 0) gives the
standard L^2 Fredholm regime. The Fredholm index on the discrete sector is 24 at
reconstruction grade, by the APS route.

The full unprojected operator is not Fredholm by b-calculus: split-signature null cone
and continuous spectrum are structural obstructions.

The primary analytic gate is the tau-twisted discrete sector existence proof (A1), which
is not established by scalar FJ/BC1 (failed), not established by the tau-correction route
(failed on structural grounds), and is currently supported only by the APS route on
compact K3 (reconstruction grade, contingent on OQ-RK1 and OQ-RK2).

Fredholm is conditionally established on the discrete sector; not established on the
full noncompact Y^14.
