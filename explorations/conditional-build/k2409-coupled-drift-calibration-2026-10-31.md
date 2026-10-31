---
title: "K2409 Coupled drift calibration and honest adaptation limits"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional probability mathematics; no measured drift or native GU verdict
scripts:
  - tests/channel-swings/k2409_coupled_drift_calibration_probe.py
---

# K2409 Coupled drift calibration and honest adaptation limits

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2409
carrier: conditional independent fresh binary-label pools and separately observed Bernoulli histories LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and total variation ON=declared_carrier
real_structure: real probabilities; rational polynomial certificates
grading: pre-pool calibration, fresh hidden roles and hypothetical probability paths
action_owner: repository-construction -- K2403 matching experiment and K2406 effective odds
target: joint Lipschitz confidence regions, exact pool odds and impossibility of honest smooth adaptation MAP-TYPE=evaluation
```

## Result and semantic preflight

K2406 optimizes a deterministic linear confidence radius and gives sharp odds over a probability rectangle. Its corners can violate a shared drift model. Here an exact feasibility and extremal-extension theorem retains that shared constraint and reduces the sharp pooled odds to one variable. The complete three-member fixture improves the realized maximum factor from 7/5 to 29/15. A separate lower bound shows why data cannot justify replacing a supplied roughness bound by a conveniently smaller one: confidence intervals honest over the rough class must remain wide even at its perfectly stationary submodel.

These are conditional statistical objects, not source-owned GU dynamics or measured calibration. T16/T17 and Layer 0 bind the inference. No particle, cosmology, matching or hardware claim is transferred. The statistical preflight challenges joint attainability, finite-grid extremization and post-selection; the observational preflight asks whether the exposure experiment actually supplies independent innovations, hidden roles and a common conditional residual law. All are assumptions here.

## 1. Exact feasibility and coupled envelopes

There are m calibration members and one science member, all **fresh**, at fixed scheduled exposure times s_i. All bounds below are frozen before revealing any member of that pool; historical labels used to learn the bounds are a separate information source. Conditional on that common pre-pool history, assume the K2403 product-label and matching experiment, and constrain its parameters by

    l_i <= p_i <= u_i,    |p_i-p_j| <= d_ij=L|s_i-s_j|,    p_0=q.       (1)

An observed timestamp or identity must not reveal the science role to the score. The geometry in (1) constrains conditional parameters given the same pre-pool information; sequential conditional means after revealing other members are not silently substituted. L is supplied, not fitted into validity.

More generally d may be any fixed pseudometric. The interval-constrained Lipschitz set is nonempty exactly when

    l_i <= u_j+d_ij for every i,j.                                      (2)

Necessity follows from any feasible p. For sufficiency set

    a_i=max_j(l_j-d_ij),        b_i=min_j(u_j+d_ij).                     (3)

Each function is d-Lipschitz, by the triangle inequality. They respect all intervals by (2), and every feasible p lies coordinatewise between a and b. Consequently both a and b are feasible, simultaneous least/greatest elements. This is stronger than optimizing each coordinate separately with unrelated witnesses.

Fix q=x. After checking (2) among calibration nodes, the feasible x interval is

    J=[l_0,u_0] intersect [max_i(l_i-d_i0), min_i(u_i+d_i0)].            (4)

For x in J replace node 0's interval by [x,x]. The least/greatest calibration vectors become

    a_i(x)=max(max_j>=1(l_j-d_ij), x-d_i0),
    b_i(x)=min(min_j>=1(u_j+d_ij), x+d_i0).                             (5)

Both have q=x and are jointly feasible. Empty J proves incompatibility of the supplied constraints, not a physical discovery. If intervals are simultaneous confidence statements, empty sets can arise on their failure event; use the unconditional full-odds fallback there rather than treating an empty supremum as infinite evidence.

## 2. Exact sharp pooled odds and finite algebraic certification

For 1<=t<=m environment-one labels, retain K2406's effective odds

    r(p,q;t)=odds(q)*(m-t+1)/t * e_(t-1)(odds(p))/e_t(odds(p)).         (6)

Its proved monotonicity in each p_i gives the exact joint-set extrema

    r_min=min_(x in J) r(b(x),x;t),
    r_max=max_(x in J) r(a(x),x;t).                                    (7)

Every bound is attained when the parameters stay in a compact subinterval of (0,1): continuity supplies the extremizing x and (5) supplies one feasible vector realizing it. Boundary probabilities require support/limit handling, as in K2403; the fixture is strictly interior.

For rational intervals/times/L, (5) has finitely many rational breakpoints. On every open cell, each p_i is constant or x plus a rational constant, so (6) is rational in x with nonvanishing denominator. Endpoints and every real root in the cell of N'D-ND' form a complete extremum certificate; a constant cell is immediate. Exact polynomial root isolation and sign checks, not a numerical grid, certify the general finite problem. This is a reduction/algorithm theorem, not an implementation claim for a general root-isolator.

Endpoint-only logic fails for related coupled sets. In the admissible affine submodel p=q+1/8, q in [1/4,3/4], m=t=1, r has its strict interior maximum 49/81 at q=7/16. Endpoint values are 5/9 and 3/7. This control adds a known signed increment; it does not claim the bare Lipschitz box has that same extremum. It tests why a general coupled-model optimizer cannot discard stationary points.

## 3. Complete three-member fixture

Take times (s_0,s_1,s_2)=(0,-1,-2), understood as offsets for future scheduled fresh exposures, L=1/8, q in [3/8,5/8], p_1,p_2 in [1/4,3/4]. The complete constraint includes |p_1-p_2|<=1/8. The envelopes are

    a=(max(1/4,x-1/8), max(1/4,x-1/4)),
    b=(min(3/4,x+1/8), min(3/4,x+1/4)).

Equation (7) gives the sharp t=1 interval [3/7,15/7]. Here is a whole-domain certificate. Write x=q. On [3/8,1/2], the upper function is

    U1=3x(9-8x)/((1-x)(8x+3));

on [1/2,5/8] it is

    U2=x(32x²-76x+45)/((1-x)(-32x²+44x-7)).

For each numerator N and positive denominator D, the two respective certificates for 15D-7N>=0 are

    3(2x-1)(8x-15),
    (2x-1)(128x²-240x+105).

The second quadratic is decreasing and at 5/8 equals 5, hence positive. The lower functions on the same two cells are

    V1=x(32x²-52x+21)/((1-x)(-32x²+20x+5)),
    V2=x(7-8x)/((1-x)(11-8x)).

Their certificates for 7N-3D>=0 are

    (2x-1)(64x²-72x+15),
    (2x-1)(33-40x).

The first quadratic is decreasing on [3/8,1/2] and starts at -3; the second factor of the last expression is at least 8. All denominators are positive directly from their underlying positive odds sums. Both global endpoints are attained at x=1/2: b=(5/8,3/4) gives 3/7; a=(3/8,1/4) gives 15/7. Complementing all labels sends t=1 to t=2 and r to 1/r, proving the sharp t=2 interval [7/15,7/3].

Dropping the coupling gives the looser rectangle [1/5,5] for either t. Its extremal corners are infeasible for (1). With labels (1,0,0) and scores (1,0,0), the actual K2403 normalizer is C=r_max/(r_max+2)=15/29 instead of 5/7. At unit bet the realized maximum factor is 29/15 instead of 7/5. The true probability that the environment-one item is science is at most 15/29, with equality at the displayed feasible maximizer, so the conditional expected factor is at most one. The probe independently sums the original labeled Bernoulli and all six hidden-role permutations; it does not certify this consumer merely by calling (6) twice.

Bounds must cover the whole pre-pool parameter vector simultaneously. The inherited stopped-shadow argument then gives crossing error at most delta+eta, plus any separately charged failure beta of the drift premise. One may tighten a simultaneous confidence rectangle with known constraints after observing historical data; one may not claim uncharged coverage for a retrospectively fitted L. The factor improvement is a conditional feasible-path calculation, not a power or acquisition-cost guarantee.

## 4. Honest adaptation fails even at a stationary truth

This is a different experiment from the fresh pool: independent historical Bernoulli labels, one at each integer age r>=1, with a current target at age zero. Let P_0 have probability 1/2 at every age and currently. For 0<a<1/2 and a known allowed roughness L>0, let P_+ and P_- have histories

    p_r^±=1/2 ± (a-Lr)_+,        current p_0^±=1/2±a.                 (8)

Both paths are L-Lipschitz; the stationary path is in the same class. Set f_r=(a-Lr)_+. Direct likelihood calculation against P_0 gives

    1+chi²(P_± || P_0)=product_(r>=1)(1+4f_r²).                      (9)

Only finitely many factors differ from one. Thus TV(P_±,P_0)<=sqrt(chi²)/2. If I is any confidence interval with coverage at least 1-epsilon under EVERY L-Lipschitz path, transferring each of its two coverage events to P_0 and intersecting yields

    P_0(width(I)>=2a) >= 1-2epsilon-TV(P_+,P_0)-TV(P_-,P_0).          (10)

This includes randomized procedures with common independent randomization. It applies to any finite observed history (omitting factors only improves the bound), and arbitrarily many older observations cannot distinguish the models. It is unconditional under P_0, not conditional coverage given a convenient observed path.

For a=1/9, L=1/72 there are seven nonzero differences and

    1+chi²=164741122962235625/148074416822550528 < 9/8.

Each TV is strictly less than 1/(4 sqrt(2))<1/5. At epsilon=1/20, (10) therefore forces width at least 2/9 with probability **strictly greater than 1/2 under the perfectly stationary law**, irrespective of the number of older labels. This strengthens K2406's lower bound at a rough alternative into a concrete obstruction to honest adaptation at the smooth submodel. It excludes uniformly95%-honest intervals over this class whose widths converge to zero at the stationary law by merely adding older observations. It does not exclude stronger structural assumptions, increasing recent sampling density, or direct current measurement.

The scaling is explicit: log(1+chi²)<=4 sum f_r²<=4a³/(3L), because the decreasing nonnegative ramp sum is bounded by its integral. Choosing a proportional to L^(1/3), below 1/2, bounds TV by a fixed constant. This is an honest adaptation lower bound at a constant submodel, not a minimax-optimality claim for K2406's smoother or a new general statistical method.

With no externally bounded drift at all, identical fair histories can precede current probabilities zero and one; each extends to a finite Lipschitz path on the integer time grid. Uniform 1-epsilon coverage across these models requires the interval to contain both zero and one with probability at least 1-2epsilon under that same history law. Finite past data alone cannot certify an unrestricted future drift upper bound. Reusing a fitted low-drift tube as if supplied contradicts this experiment.

## Verification, alternatives and next condition

The exact probe checks feasibility/extension cases, symbolic whole-cell identities, attainable extrema, direct hidden-role probabilities and the actual e-factor consumer, affine interior-extremum and infeasible-corner controls, and the full 128-history chi-square sum against the stationary law. Universal statements rest on the written Lipschitz, monotonicity and change-of-measure proofs. Finite pass counts are not proofs or measured data.

The strongest alternative is the calibration-free equal-within-environment normalizer from K2403: it avoids a supplied drift law at the cost of between-environment borrowing. A justified stochastic drift model or self-similarity/separation condition may support a different adaptation theorem; it is a changed model whose assumptions need evidence. A useful constructive successor is a fully implemented exact coupled-odds solver for larger metric constraints, or safe confidence regions using valid joint likelihood information beyond a rectangle. Actual deployment additionally needs a measured matching/stability argument and complete acquisition costs.

Postflight specialist questions are (i) joint extremal attainability, (ii) conditioning on one common pre-pool history, (iii) fresh-role exchangeability and timestamp leakage, (iv) true-model coverage after selection, and (v) correct direction of total-variation transfer to the stationary law. Independent internal review checked the joint envelopes, complete extremal proof, original hidden-role consumer and stationary-law change of measure. The native exact probe reproduced the stated fixtures and controls. No external-expert or proof-assistant certification is claimed.
