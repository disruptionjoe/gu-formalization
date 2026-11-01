---
title: "K2418 Exact attainable ranges for metric-calibrated pools"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical verdict
scripts:
  - tests/channel-swings/k2418_support_attainment_probe.py
---

# K2418 Exact attainable ranges for metric-calibrated pools

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
result: K2418
carrier: independent Bernoulli calibration pool with a jointly supplied finite pseudometric LAYER=toy CHIRALITY=N/A
pairing: original supported conditional probability ON=declared_pool
real_structure: rational input and real algebraic extrema
grading: science role and calibration roles; positive-support equivalence classes
action_owner: repository-construction -- K2415 probability model
target: complete attainable conditional range with exact endpoint classification MAP-TYPE=evaluation
```

## Result

[K2415](k2415-boundary-pool-support-2026-10-31.md) certifies infima and suprema but leaves global attainment open and searches support faces exponentially. This result replaces that search with a support-cardinality dynamic program, decides exact global attainment, and therefore describes the complete attainable interval, including open endpoints.

Inputs are m≥1 calibration roles, closed rational probability intervals, a rational pseudometric on calibration and science roles, and integer 1≤t≤m.

This is conditional independent probability mathematics. Joint metric calibration, matching, drift bounds, independence and nonnegative role-blind consumer scores remain supplied assumptions; no empirical calibration is inferred. SC-META-53 remains UNCERTAIN and ledger0.263 is unchanged.

## 1. Polynomial support-face construction

Fix a feasible science probability 0<q<1. Let a and b be K2415's componentwise least and greatest feasible calibration vectors. The pseudometric relation d(i,j)=0 partitions calibration indices into classes; probabilities are identical within each class. A class with a>0 is forced positive, a class with b=0 is forced zero, and a class with a=0<b is optional.

The possible positive-support cardinalities are exactly

    number of forced-positive indices + subset sums of optional class sizes.

Necessity follows from the equality classes and the extremal envelopes. For sufficiency start at a, choose the optional classes, and raise precisely their zero entries to epsilon. Choose epsilon as half the minimum of 1, every positive pairwise distance including science, and the selected original upper bounds. All these numbers are positive. Bounds hold. Across two originally zero classes the new difference is at most epsilon, below any positive crossing distance. Against an originally positive value the difference either decreases or is at most epsilon. A zero-distance class is never split. The fixed positive science class cannot be optional. Thus every subset sum has an exact feasible witness.

Store each reachable count and one predecessor subset. There are at most m+1 counts and m classes: O(m²) arithmetic after envelope construction and pseudometric validation. This is not a bit-complexity claim for arbitrary rational inputs, nor a complexity bound on the full algebraic optimizer.

For total count t, the conditional science-success probability w equals1 precisely when the calibration positive-support count is t−1. This also supplies positive event probability. The zero endpoint follows by complementing all probabilities and replacing t by m+1−t; equivalently its complement positive-support target is m−t. K2415's q=0,1 rules remain separate and require original event support.

A five-coordinate fixture with equality classes of sizes 2 and 3 has possible counts {0,2,3,5}, not every count between0 and 5. The DP produces original-metric witnesses for attainable cases and rejects the gaps. Thirty equal coordinates have only counts0,30; a middle-support request is rejected without enumerating155117520 faces.

## 2. Exact global endpoint comparison

Retain K2415's complete finite candidate set: supported breakpoints, constant-cell values, isolated stationary roots and one-sided limits. Replace its face routine by the proven DP. Each stationary candidate is f(alpha), with alpha the unique real algebraic root in the saved rational isolator. Rational candidates are exact.

Compare two candidate values by first testing exact equality in their common algebraic number field. If unequal, refine their root isolators and evaluate outward rational function intervals until they separate. The equality decision prevents an endless refinement for tied extrema. Isolation and the nonzero cell denominator give convergence; unequal algebraic values have positive separation. Select the global extremum and OR the actual witness flags over *all* tied candidates. A one-sided limit's `not_asserted` flag never becomes a witness.

Why this is complete: an attained extremum away from a breakpoint either occurs on a supported extremal envelope and is a stationary or constant value, or is a zero/one null-envelope fallback detected by the support DP. Optional support classes are constant within each open envelope cell, so a midpoint witness decides its constant fallback. Breakpoints use the original support test. Any limit also attained elsewhere is captured by that other candidate, and exact tie comparison finds it.

The result can be an unattained number strictly between0 and 1. With q=p1=x in[0,1/2], p2=1/2 and t=2, the supported family has x>0 and

    w=1/(2−x), hence range (1/2,2/3].

At x=0 the conditioning event is null. Its complement gives[1/3,1/2). The null endpoint at1/2 in either example is excluded; cancellation does not supply an attaining parameter. Infeasible and all-zero/all-one unsupported families emit no conditional bound or attained value.

## 3. The complete range is an interval

The feasible box-and-metric set F is convex. Its supported subset D={v in F:Z(v)>0} is also convex: take one Bernoulli label assignment with positive likelihood at one endpoint. Every factor in that product remains positive at every strict convex combination with any feasible point. Thus Z stays positive between two supported points. The ratio w is continuous on D, so its image is connected and therefore an interval. Exact infimum/supremum plus the two attainment bits specify that whole interval, or a singleton. This does not imply a uniform lower bound on Z or statistical power.

## Verification and continuation

The exact probe compares486 small cases against the previous face enumeration and validates returned witnesses against original bounds, all pairwise inequalities and uncancelled event probabilities. It covers gapped equality classes, deterministic science endpoints, null and infeasible families, both interior-valued unattained endpoints, algebraically identical values expressed differently, nearby unequal values and the nontrivial prior interior root fixture. Universal support and connectedness arguments have independent internal mathematical review, without external-expert or proof-assistant certification; finite checks alone do not establish them.

The mathematical range/attainment question is now closed under its stated rational input model. Deployment still requires justified current joint calibration and matching. A new empirical conclusion cannot be obtained by enlarging old stationary calibration or choosing a favorable endpoint.

Certificate: [exact report](../../lab/process/k2418-support-attainment.json); [reproducible probe](../../tests/channel-swings/k2418_support_attainment_probe.py).
