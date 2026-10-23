---
title: "K1997: Optimal capped pulses require infinite separation rank"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1997_finite_rank_pulse_obstruction.py
  - tests/channel-swings/k1997_finite_rank_pulse_obstruction_probe.py
---

# K1997: Optimal capped pulses require infinite separation rank

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: finite separation rank excluded for every exact optimal-phase pulse, with fixed-rank residual and growing-rank approximation consumers
carrier: actual K1991 central rectangle of the width9 scalar characteristic strip LAYER=toy CHIRALITY=N/A
pairing: normalized Lebesgue row and column averages and real L2 norm ON=central_rectangle
real_structure: real bounded measurable pulses; factors may be discontinuous
grading: separated coordinate factors, not source chirality
action_owner: repository-construction -- actual optimal scalar phase at cap23/100
target: exact representation and approximation complexity MAP-TYPE=intertwiner
```

## Result and scope

Every bounded measurable pulse realizing the ACTUAL optimal scalar phase and
zero opposite phase at amplitude M=23/100 has **infinite separation rank**
on its central rectangle. In particular no finite sum

    v(u,z)=sum_(j=1)^r a_j(u)b_j(z)

can represent such a pulse there, even with discontinuous measurable factors.
This excludes a whole proposed construction class; it does not exclude the
measurable pulse whose existence was already proved. It applies to every
feasible pulse for that phase, not just the secondary minimum-norm pulse.

[K1993](k1993-pulse-sobolev-corner-obstruction-2026-10-23.md)'s H1 obstruction
is a separate result: finite separation rank permits discontinuous factors,
so it is not a smoothness assumption. Conversely an infinite-rank kernel can
be smooth. The argument below uses the actual two marginal equations and cap.

Released consequences are a strictly positive residual floor for each FIXED
rank, an explicit conditioning-dependent residual bound, and an explicit
rank-at-most-n capped family with continuum residual O(1/n). The latter
converges to an elementary feasible CENTRAL pulse, not to the minimum-norm
pulse, and its finite iterates do not have exact marginals or plateaux.
Explicit wings and the actual regional minimum remain open.

## 1. Opposing saturated marginals on the actual rectangle

Reuse [K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md)'s exact
factorization. Let t be the same root in(9/20,23/50), W=3+4t,
x=u/t in[-1,1], A=3-2t, B=6+2t, and q=v/M. Put probability measures
mu=dx/2 and nu=dz/W on[A,B]. Define

    g(z)=(z-3)/(2t) on[A,3],
          0          on[3,6],
          (z-6)/(2t) on[6,B].

The unchanged central constraints are EXACTLY

    |q|<=1,  int q(x,z)dnu(z)=-x,
              int q(x,z)dmu(x)=g(z).                    (1)

The measure of each ramp in nu is2t/W, positive; g approaches1 on a
positive-measure terminal ramp. Endpoints themselves carry no assertion.
Set h=(1+q)/2. Then0<=h<=1, its row mean is(1-x)/2, and its column mean
is(1+g(z))/2. The mean of g is0. These are not sampled boundary conditions.

## 2. Finite row span gives a contradiction without any continuity assumption

Assume q has finite separation rank as an L2(mu x nu) kernel. Its row
sections lie a.e. in a finite-dimensional subspace. The span of the h rows
is also finite-dimensional. Choose a basis from actual rows: since h is
bounded, these basis functions are in L-infinity(nu). Thus the finite span V
has a finite norm-equivalence constant C>=1 with

    ||f||_infinity <= C ||f||_L1(nu),  f in V.            (2)

This step does NOT assume that originally supplied factor functions were
bounded: selecting a basis of actual bounded rows supplies a bounded basis.
Nor does it assign values at measure-zero endpoints.

Nonnegativity and the exact row constraint now give, for a.e. x,

    0<=h(x,z)<=min(1,C(1-x)/2) for a.e. z.

Fubini permits integration in x outside one common null set. Hence every
column mean has the uniform ceiling

    int h(x,z)dmu(x)
       <= int min(1,C(1-x)/2) dx/2 =1-1/(2C).           (3)

But(1+g(z))/2 exceeds this ceiling on the positive ramp where
g(z)>1-1/C, a set of positive measure. Contradiction. This proves infinite
rank on the central rectangle, hence also rules out a finite global separated
formula whose restriction would have finite rank. Finite tensor polynomials
and finite rectangular step expansions are included; no bound on smoothness
or factor oscillation was used.

Removing the cap breaks the argument: q=-x+g(z) has both exact marginals and
rank at most2, but exceeds the allowed amplitude on positive-measure sets.
Removing exact marginals permits the finite-rank approximation in section5.
These are important contrary controls, not exceptions to the theorem.

## 3. Quantitative consumer for a specified bounded basis

Suppose a capped finite-rank q has EXACT row means -x but approximate column
means. Let C be any valid constant in(2) for the h-row span. On the terminal
ramp, the required h-column mean exceeds(3) by
(g-1+1/C)/2. Since dnu=(2t/W)dg there, the q-column residual obeys

    ||int q dmu -g||_L2(nu)^2 >= 2t/(3W C^3).           (4)

The factor4 converts h error back to q error. This is an explicit certificate
once a valid basis constant is supplied. It is NOT a rank-only bound: poorly
conditioned or highly concentrated finite-dimensional spans can have huge C.
No universal C(r) is asserted. Approximate row means require a separate error
term and cannot be silently substituted into(4).

## 4. Every fixed rank has a positive marginal-residual floor

For an integer r, define K_r={q: |q|<=1, rank(q)<=r} in the Hilbert space
L2(mu x nu). It is weakly compact. The amplitude box is bounded and closed
convex, hence weakly compact. Rank<=r is weakly closed: for arbitrary test
functions f_0,...,f_r and k_0,...,k_r, every determinant of the matrix

    [int f_i(x) q(x,z) k_j(z) dmu dnu]_(i,j=0)^r

must vanish. Each entry is a continuous linear functional in the weak L2
topology. All such determinants vanish iff the associated integral operator
has rank<=r, so their closed intersection proves the assertion. This avoids
the false inference that arbitrary weak limits preserve a varying rank bound.

The combined squared residual

    J(q)=||int q dnu +x||_L2(mu)^2
          +||int q dmu -g||_L2(nu)^2

is weakly lower semicontinuous because conditional averages are bounded linear
maps. It attains a minimum j_r on K_r. If j_r=0, the minimizer would satisfy(1),
contradicting section2. Therefore j_r>0 for every finite r. In particular a
capped sequence whose marginal residuals tend to0 must have ranks tending to
infinity (every fixed bound is eventually exceeded). This compactness proof
supplies neither an explicit formula for j_r nor a lower rate in r.

## 5. Explicit increasing-rank approximation, with exact continuum errors

There is no contradiction with practical approximation. Let n be positive
even, partition x in[-1,1] and the combined ramp coordinate y in[-1,1] into
n equal bins, and let x_i=-1+(2i+1)/n. Define q_n on row bin i by

    q_n(i,j)=sign(j-i) on ramp bin j, including0 when j=i,
    q_n(i,middle)=-x_i.                                 (5)

The sign at0 is0. The two physical ramps have dz=2t dy; the middle is width3.
This is the conditional cell average of the elementary exact central pulse
q_0(x,y)=sign(y-x) on ramps and q_0(x,middle)=-x. That pulse's exact marginals
were already used in K1991; its feasibility is reused, not newly claimed.
The new statement is the exact finite-rank approximation/error calculation.

There are n row indicator factors, so rank(q_n)<=n; |q_n|<=1 everywhere.
Writing alpha=4t/W, its row averages equal -x_i, its ramp column averages
equal y_j, and its middle column mean is0. Direct integration gives

    row residual squared =1/(3n^2),
    column residual squared =alpha/(3n^2),
    J(q_n)=(1+alpha)/(3n^2)>0,
    ||q_n-q_0||^2=alpha/n+(1-alpha)/(3n^2).              (6)

The ramp strong-error term comes only from the n diagonal squares; within
each, sign(y-x) has magnitude1 while its cell mean is0. The middle error is
ordinary midpoint variance. Thus(5) converges strongly to q_0 with the cap
preserved, while every finite step honestly retains nonzero marginal error.
An even n>=sqrt((1+alpha)/(3 epsilon^2)) guarantees combined residual<=epsilon.
These normalized errors are not phase Dirichlet-energy or smoothness bounds.
This construction concerns the central rectangle only and supplies no wings.

## 6. Verification and next boundary

Producer:598 exact rational marginal, cap, residual and conditioning controls.
Separate probe:101 exact integration/algebra/contrary-case controls, with four
corrupted mathematical residual/distance/ceiling inputs rejected after a green
baseline. Its two symbolic integrals check the constants in(3)-(4); the
functional-analysis proof in sections2/4 establishes the universal conclusion.
An initial unsimplified SymPy-expression equality failed; explicit algebraic
simplification repaired the harness before the green baseline and mutation tests.
This is not a claimed detected mathematical fault.

The strongest overclaim would infer pulse nonexistence or a quantified
rank-only barrier. The explicit infinite-rank q_0 refutes the first; C is
basis-dependent and j_r unquantified. The strongest counterexample is the
uncapped rank2 additive solution, which identifies exactly why the cap is
essential. The weakest seam for an effective solver is a computable rank-only
lower bound or an exact-marginal construction using an infinite series.

The related capacity-constrained transport setting is discussed by
[Korman and McCann](https://arxiv.org/abs/1304.6456); no theorem from that paper
is used to establish the rank obstruction here. No novelty claim is made.
These are same-author internal mathematical checks, not external review or
proof-assistant certification. SC-META-53 remains UNCERTAIN. Source,
physics-ledger and canon verdicts remain unchanged.
