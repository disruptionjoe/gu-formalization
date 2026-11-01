---
title: "K2412 Exact metric-constrained pool odds and evidence consumer"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional probability certificate; no measured calibration or native GU verdict
scripts:
  - tests/channel-swings/k2412_exact_metric_pool_odds_probe.py
---

# K2412 Exact metric-constrained pool odds and evidence consumer

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
result: K2412
carrier: conditional independent fresh binary-label pools and separately observed Bernoulli histories LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and total variation ON=declared_carrier
real_structure: real probabilities; rational polynomial certificates
grading: pre-pool calibration, fresh hidden roles and hypothetical probability paths
action_owner: repository-construction -- K2403 matching experiment and K2406 effective odds
target: complete exact metric-box odds certificates and conservative evidence factors MAP-TYPE=evaluation
```

## Result and preflight

[K2409](k2409-coupled-drift-calibration-2026-10-31.md) reduced joint metric
calibration to one-dimensional rational extrema. The companion implementation
now supplies complete exact breakpoint/stationary candidates, feasible
probability witnesses and outward rational enclosures for arbitrary finite
rational pseudometrics with strictly interior probability intervals.
A five-member fixture is certified over its entire parameter set and improves
its realized evidence factor from 13/10 to 2873/1608. This is a conditional
consumer calculation, not an empirical power or acquisition-cost result.

The preflight rejected a sampled grid and a refinement scheme that ranks
algebraic values by waiting for disjoint intervals: equal extrema could make
that scheme fail to terminate. Instead every candidate gets a certified value
interval and extrema are enclosed without ranking. Source-native physical
claims and the ledger remain unchanged. The same pre-pool conditioning,
fresh independent labels, hidden roles and matching assumptions as K2409
are required. Historical confidence coverage and any drift-premise failure
probability remain separately charged.

## 1. Complete finite algorithm

Inputs are n=m+1 rational intervals [l_i,u_i] strictly inside (0,1), an exact
finite pseudometric d and an integer 1<=t<=m. The solver rejects floating
point inputs, nonmetric distances and boundary probabilities; it does not
silently apply interior formulas where support changes. It checks symmetry,
nonnegativity, zero diagonal and every triangle inequality.

K2409 proves feasibility iff l_i<=u_j+d_ij for every pair. Infeasibility is a
structured return with no odds value; an empty set never licenses evidence.
The feasible science interval J and simultaneous calibration envelopes are

    J=[l_0,u_0] intersect [max_i(l_i-d_i0),min_i(u_i+d_i0)],
    a_i(x)=max(max_j>=1(l_j-d_ij),x-d_i0),
    b_i(x)=min(min_j>=1(u_j+d_ij),x+d_i0).

They are actual jointly feasible extremal extensions for each x in J.
For each t use the count-polynomial recurrence

    P_k(p)=[z^k] product_i ((1-p_i)+p_i z),
    r(p,x;t)=x/(1-x)*(m-t+1)/t*P_(t-1)(p)/P_t(p).

This is the same elementary-symmetric odds ratio as K2409; common factors
cancel. Every denominator is nonzero on the strictly interior compact domain.
The sharp lower odds minimize r(b(x),x;t); upper odds maximize r(a(x),x;t).
All envelope breakpoints partition J into rational cells. On each cell
f=N/D is rational. The complete candidate set consists of the breakpoints
and every real root of N'D-ND' in its open cell. Constant cells require only
their endpoints. A singleton J works directly, as do zero-distance duplicates.

A stationary candidate is represented exactly by its squarefree rational
polynomial and an isolating rational interval containing exactly one real
root, together with the rational function and envelope witness. This is an
exact algebraic specification, not a floating point root. SymPy rational
root isolation supplies completeness; the solver refines until interval
Horner evaluation excludes zero from the denominator and bounds the VALUE
within the requested tolerance epsilon. Analytic continuity and a nonzero
denominator guarantee eventual refinement. Complexity may grow with the
number of nodes and polynomial degree; no large-instance speed claim is made.

For candidate enclosures [L_j,U_j], the exact minimum is in
[min L_j,min U_j], and maximum in [max L_j,max U_j]. Each interval has width
at most epsilon. Equal candidate values need no ordering or equality oracle.
These outward bounds are safe, but are not themselves claimed attained or
sharp. The exact candidate set characterizes the sharp extrema. A downstream
normalizer uses the OUTER endpoints to preserve its guarantee.

## 2. A complete five-member fixture and original consumer

Take q in [3/8,5/8], four calibration intervals [1/4,3/4], and
 d_ij=|i-j|/16 for i,j=0,...,4. Breakpoints are
3/8,7/16,1/2,9/16,5/8. The exact sharp bounds are:

| Count t | Lower | Upper |
|---|---:|---:|
| 1 | 105/214 | 495/268 |
| 2 | 642/1265 | 2412/1265 |
| 3 | 1265/2412 | 1265/642 |
| 4 | 268/495 | 214/105 |

Every extremum is attained at q=1/2: the lower calibration envelope
(7,6,5,4)/16 attains upper odds, and (9,10,11,12)/16 attains lower odds.
The probe verifies all rational whole-cell inequalities by exact polynomial
root isolation and signs on every root-free component, as well as endpoint
attainment and complement reciprocity. These are separate from rounded
extremum enclosures.

For labels (1,1,0,0,0), direct enumeration of all120 role permutations using
the ORIGINAL Bernoulli likelihoods gives label-event probability2873/81920
and conditional science-position probabilities

    (804/2873,804/2873,1265/8619,1265/8619,1265/8619).

With score one on the first two positions and zero elsewhere, the normalizer
is1608/2873 and the realized unit-bet factor is2873/1608. Dropping the metric
coupling gives upper odds5 and factor13/10. The exact normalizer is attained
by the stated feasible path, while a rounded outward upper odds bound makes
the expected factor no larger than one. No conditional formula is used to
validate itself: the likelihood enumeration is independent of the recurrence.
The inherited stopped-shadow argument supplies delta+eta plus any separately
charged drift-premise failure, under its assumptions; no new coverage model
is inferred from these fixtures.

## 3. Follow-through: interior stationary points and certificate failure control

Even a bare Lipschitz metric box can have an interior stationary extremum.
For t=1, the upper function on (9/16,5/8) has derivative numerator proportional
to

    10485760x^7-78315520x^6+249200640x^5-437520640x^4
      +457190688x^3-283899454x^2+96797624x-13939065.

Exact root counting gives one root in this cell; signs at its endpoints are
negative and positive. This is a strict LOCAL minimum. It is not a claim of
an interior global maximum of the upper envelope, nor a counterexample to a
possible specialized endpoint theorem for those global extrema. The complete
solver needs no such unproved theorem and exercises actual root isolation.

Independent implementation review found a genuine certificate bug before
acceptance: two isolating intervals can touch at a rational nonroot. Sampling
only positive-length gaps can miss a narrow negative component between them.
The corrected sign checker tests every isolator endpoint as well as every
remaining gap. A planted polynomial
(x-1/2-10^-12)(x-1/2+10^-12) verifies detection of that failure. This is a
mathematical control against a real negative well, not a flipped assertion.

## Verification and postflight

The probe checks complete root candidates/enclosures, eight whole-cell sharp
bounds, original120-permutation consumer, constant/singleton/duplicate-node
cases, and invalid-input/infeasible/negative-well controls. Universal validity
uses K2409's proved monotonicity and simultaneous envelopes plus the complete
root-isolation argument above. Independent specialist review checked both
the algorithm and its implementation, including equal-root and endpoint
cases. No external-expert or proof-assistant certification is claimed.

Remaining work includes justified drift/current-pool matching and complete
acquisition costs, or a separately scoped support-aware solver permitting
probabilities zero and one. This implementation intentionally rejects those
inputs rather than claiming to solve their changed conditional support.

Algorithm reference: [SymPy polynomial root isolation documentation](https://docs.sympy.org/latest/modules/polys/reference.html).
Exact inputs, sign checks and proof obligations are stated here; a numerical
root finder is not substituted for these methods.
