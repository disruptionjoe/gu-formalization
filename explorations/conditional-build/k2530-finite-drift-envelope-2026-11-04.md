---
title: "K2530 Finite drift information and sharp distance-anchor feasibility"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-information tests; no measured sensitivity or native GU exclusion
scripts:
  - tests/channel-swings/k2530_finite_drift_envelope_probe.py
---

# K2530 Finite drift information and sharp distance-anchor feasibility

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
result: K2530
carrier: common-momentum radial FLRW emitters and finite normalized-drift node constraints on a compact observed interval LAYER=toy CHIRALITY=N/A
pairing: shared calibrated distance integrals and sourced weak-action windows ON=declared_carrier
real_structure: real Lipschitz drift with strictly positive expansion on each admitted trial
grading: finite data, supplied regularity, kinematic completion and action membership remain distinct
action_owner: repository-construction -- K2367 sourced quadratic metric comparator; kinematic envelope does not assume its equation
target: exact single-anchor feasible image and joint-history weak consumer MAP-TYPE=evaluation
```

## Result and prior evidence

Finite drift samples with an independently supplied regularity bound give a sharp nonlinear distance-anchor interval. An explicit anchor is rejected by this interval although the coarse uniform node bound accepts it. Individual anchor intervals still do not establish joint feasibility; an exact two-anchor counterexample proves why. The same envelopes bound the actual sourced weak columns without requiring a nearly coasting history.

These are conditional information tests, not an application to measured data. [K2528](k2528-observation-forecast-feasibility-2026-11-04.md) found that the specified forecast does not supply the joint calibration, common tracer or continuous regularity premises. No such input is manufactured here. SC-COS-50/51/54 ASSERTS, LT-GR2e NEEDS and ledger0.263 are unchanged. The metric action remains distinct from native connection-distortion cosmology.

Reuse rather than rediscover: [K2409](k2409-coupled-drift-calibration-2026-10-31.md) already constructs finite-node Lipschitz extensions; K2266/K2524 already supply weak profiling/covariance and finite-node ambiguity. K2522 already prices a nearest-node uniform band. New here is the sharp nonlinear anchor image for the moving-emitter map, its explicit discrimination and joint-anchor failure, followed into the sourced weak consumer.

## 1. Freeze one physical and calibration trial

Use K2526's same-momentum radial-geodesic class, one clock/distance unit, fixed trial p>=0 and effective normalized rate q=H0+b_cal, where b_cal is the retained common fractional calibration offset from K2526. The same b_cal belongs to the shared trial; q need not be positive in general. On I=[a,b], a>0, write

    y_p(X)=X/sqrt(1+2pX),
    w_p(X)=d log(y_p)/dX=(1+pX)/(X(1+2pX))>0,
    H(y_p(X))=y_p(X)[q-Q(X)].

Physical past-lightcone trials also require y_p(a)>=1 (with the appropriate endpoint behavior if equality holds) and their actual common tracer domain. At the observer endpoint Q(X0(p))=b_cal and H(1)=H0 must agree; encode Q(X0(p))=b_cal as an exact node constraint when that endpoint belongs to I. The SAME reduced-distance endpoints L_i=D_L(X_i)/X_i give the anchor

    C_p=L_b/sqrt(1+2p b)-L_a/sqrt(1+2p a)
       =F_p,q(Q)=integral_a^b w_p(X)/(q-Q(X)) dX.       (1)

q, p, the distance calibration and their uncertainties are shared across every node, anchor and window. A common calibration shift Q->Q+c and q->q+c leaves q-Q, the H envelopes and every anchor exactly invariant; shifting q separately per anchor does not. Finite-time/calibration/motion corrections must already be included in the node constraints. A marginal standard deviation is not a simultaneous interval. The identity is conditional on the specified lightcone/tracer class; absorption bins alone do not supply it.

Supply a Lipschitz constant L>=0 in the OBSERVED X coordinate, not in y or log y. For sorted distinct nodes x_i with boxes [l_i,u_i], define

    lower(X)=max_i[l_i-L|X-x_i|],
    upper(X)=min_i[u_i+L|X-x_i|].                     (2)

The class of L-Lipschitz functions meeting all boxes is nonempty iff
l_i<=u_j+L|x_i-x_j| for every i,j. Under this condition lower and upper themselves meet all boxes and are L-Lipschitz, and every admissible Q lies between them. This is the inherited extension theorem: each data inequality propagates by the Lipschitz condition, and the envelopes attain the resulting extremes. Convex interpolation Q_t=(1-t)lower+t upper stays admissible.

For the following exact image choose the ROBUST POSITIVITY SLICE

    q>max_I upper.

Then H is uniformly positive for every member, and monotonicity plus dominated continuity in t gives the exact attainable range

    {F_p,q(Q): Q admissible}=[F_p,q(lower),F_p,q(upper)]. (3)

Thus intersection with a supplied anchor interval is necessary and sufficient for ONE anchor in this Lipschitz kinematic class. The extrema may have corners. Nonempty intersection does not prove a smooth action solution; empty intersection excludes its smooth subset as well. A general positive history may have Q<q while q<=max upper: (3) does not cover that slice and it must not be silently discarded. Uncertain trials require a union over all allowed p,q/calibration values, or a certified outer cover, before any class-level rejection. Correlated node boxes require their actual joint feasible set; a rectangular superset is safe for exclusion but loses sharpness and cannot certify joint feasibility.

## 2. Exact information gain, without a coasting tolerance

Set p=0, q=1, I=[1,2], Q(1)=Q(2)=0, L=1. Then lower=-d, upper=d, d=min(X-1,2-X). Direct integration gives

    F(lower)=(1+log 2)/3,
    F(upper)=(3/2)log 3-log 2.                       (4)

The coarse uniform bound -1/2<=Q<=1/2 instead permits
[(2/3)log2,2log2]. The exact anchor C=1 is inside that coarse interval but above (4):

    exp(F(upper))=3sqrt(3)/2 < 8/3 < e.

The first inequality follows by squaring; the second already follows from the first five terms of e's positive series. The positive control Q=0 gives C=log2 inside (4). The failure rejects precisely the supplied nodes/L/q/anchor kinematic class; it is neither a failure of the quadratic action nor a GU verdict. Since F decreases in q and w_p decreases in p>=0, the same C_p>=1 exclusion holds uniformly for q>=1 and p>=0 on this robust slice with the SAME node envelopes. A physical distance band must actually establish C_p>=1 for each trial; fixed raw distances do not generally yield a constant C_p.

## 3. Released joint-anchor obstruction

One common history is essential even after exact single-anchor bounds. On [2,8], set p=0,q=2, b_cal=0 and supply 0<=Q<=1,L=1 on that observed interval. Boxes [0,1] at any chosen nodes are satisfied by constant controls. Require distance differences from the common lower endpoint2:

    F_[2,4]=log2/2, F_[2,8]=3log2/2.               (5)

Each is feasible alone: Q=0 on [2,8] meets the first; Q=2/3 on [2,8] meets the second. Both admit a smooth positive extension to the observer with Q(1)=0 and H0=2; the second rises below X=2, outside the supplied interval. Thus neither control silently changes b_cal or H0. Jointly, equality at the first integral's minimum forces Q=0 on [2,4], by positivity of the weight and continuity. Subtraction requires F_[4,8]=log2, its maximum, forcing Q=1 on [4,8]. Continuity at4 is impossible. Testing the two projected intervals independently would falsely accept (5). This is a functional correlation failure, even with exact calibration and anchors. The global [0,1] bound is supplied explicitly, not inferred from sparse node boxes. It is not fixed by declaring their measurement errors independent.

A practical finite joint representation may retain interval values on cells plus cross-cell Lipschitz constraints and all anchor sums. Every relaxation must be an outer cover for safe rejection. This note does not claim to solve a general many-anchor optimization or infer L from finitely many samples.

## 4. Released sourced weak-column consumer

Use the SAME K2520/K2367 divided sourced equation and s=3log y. For a compact C2 test with phi=phi_s=0 at the endpoints its necessary residual is

    L_phi+alpha C_phi/36-rho D_phi/216-q0 E_phi/108=0,
    (L_phi,C_phi,D_phi,E_phi)
      =integral ( (phi_ss+phi_s)H^(3/2),
                   phi H^(-1/2), phi H^(-5/2),
                   phi exp(s)H^(-5/2) ) ds.         (6)

This reuses the action equation; it is not derived from kinematics. For the current trial ds=3w_p dX and H lies in [h_-,h_+]=[y(q-upper),y(q-lower)], with h_->0. Bound every power monotonically: positive powers increase, negative powers decrease. For a signed coefficient g split g=g_+-g_- with g_+,g_->=0. If A<=H^nu<=B, then

    g_+ A-g_- B <= g H^nu <= g_+ B-g_- A.           (7)

Integrating (7) gives direct outer intervals for all four columns. These depend on supplied L and joint node uncertainty, not closeness to coasting. Corner points in (2) require no derivatives of Q. Actual integration needs exact formulas or certified quadrature with remainders; a sampled numerical grid is not an enclosure. In the X variable, phi_s=phi_X/(3w_p) and
phi_ss=(phi_XX w_p-phi_X w_p')/(9w_p^3); changing trial p changes the test map too.

For four windows form M=[C/36,-D/216,-E/108,L]. If a nominal M0 is invertible and every allowed matrix obeys

    ||M0^-1 (M-M0)||_infinity<1,                    (8)

then no shared unrestricted alpha,rho,q0 can solve (6), since the vector(alpha,rho,q0,1) is nonzero. A sufficient interval check is
|| |M0^-1| E ||_infinity<1 when |M-M0|<=E entrywise. Row/column correlations may make this conservative, never falsely excluding when the outer bounds are valid. Repeat/cover every allowed physical trial; choosing a convenient q,p is not elimination of them. No numerical sensitivity is claimed for (8); the explicit scientific discrimination in this note is (4)/(5), not a generic matrix fixture.

## Evidence and next condition

The exact probe verifies the physical Jacobian and weak-window derivative transformation, piecewise rational integrals, algebraic strict bounds, feasible controls, joint-anchor saturation and the matrix perturbation consumer. Written monotonicity/continuity and extension arguments establish the infinite-class statements; finite checks do not replace them. Independent review is internal, not external-expert, experimental, proof-assistant or novelty certification.

The remaining observation input is an actual joint finite-node/anchor/tracer model with a justified regularity bound (or an action-forward likelihood avoiding that assumption). No such model was present in K2528's forecast. A larger permitted L weakens the test; a measured counterprofile changes the input class rather than falsifying GU. Native source/ledger/canon unchanged.
