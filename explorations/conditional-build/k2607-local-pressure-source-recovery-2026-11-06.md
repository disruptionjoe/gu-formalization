---
title: "K2607 Local recovery of pressure profiles and unknown source positions"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: locally calibrated finite-dimensional mathematical recovery near nonzero separated sources; no physical sensor or global array
scripts:
  - tests/channel-swings/k2607_local_pressure_source_recovery_probe.py
---

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
result: K2607
carrier: finite separated interior B atoms with compact conserved radial A pressures, and their first positional derivatives LAYER=toy CHIRALITY=N/A
pairing: invariant full metric against compact conserved Einstein receivers ON=declared_carrier
real_structure: real fixed K2594 linear preparation and real finite source parameters
grading: profile coefficients, seven-dimensional B locations, conserved receiver and physical apparatus distinct
action_owner: repository-construction -- selected curved-product completion
target: dipole observability and local nonlinear recovery MAP-TYPE=evaluation
```

# Local unknown-position recovery from conserved observations

## Result and scope

Fix m distinct interior B points, and at each point a nonzero pressure in an n-dimensional linearly independent smooth compact radial-pressure space. On the fixed K2594 preparation there exist N=m(n+7) smooth compact conserved receivers, supported away from all reference points, whose readings locally and stably determine all N profile/position parameters. They stay source-disjoint on a sufficiently small parameter neighborhood. The receiver Jacobian is invertible, and the explicit conditioning criteria below survive sufficiently narrow source smoothing.

K2605 already proved finite atomic complete-data uniqueness and known-support finite-dimensional receiver existence. The new burden here is FIRST POSITION DERIVATIVES, differentiability of the actual preparation, and a fixed finite local nonlinear inverse. No global finite-array reconstruction, implemented numerical curved response matrix, guaranteed conditioning as nodes collide, inferred source number, or calibrated apparatus is supplied. The finite receiver family exists by distribution separation; its singular value and derivative bound must actually be determined before numerical use.

SC-ACT-01 ASSERTS its action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, and SC-META-53 remains UNCERTAIN. This selected completion is not those native objects. Source, ledger0.263 LT-GR1b/6b/10 and LT-SM8 and canon are unchanged. No novelty, GU verdict, physical state or causal preparation claim.

## 1. The actual cofactor identity sees every first source jet

Reuse the full-system identity of K2605, including all tensor and homogeneous additions:

    d(X,Y) Z = -F(X,Y) S,  Z=tr_A(Eh),
    c=-424853/(149354 kappa), R=F-cd, deg_Y R=4.

Here d has degree five in Y and a nonzero constant leading coefficient. At kappa=1,

    r4(X)=[Y^4]R
      =-128665108(19845028500669825024 X-8236440909844467455)
        /31733016160503214625,

and r4_k(X)=kappa^-3 r4_1(X/kappa²). Its sole root is lambda_* kappa²>0. These are original coupled-system coefficients, not an illustrative Green kernel.

At one B point use invariant parameter-derivative deltas and compact radial traces:

    S=t0(A) delta_b + sum_a ta(A) partial_(b_a) delta_b.

Parameter differentiation of the invariant atom includes the correct density factors. Suppose Z vanishes off the point in a B neighborhood (with the full admitted radial tube). A supported distribution has locally finite transverse order. The principal symbol of d is a nonzero constant times q_B(xi)^5, where the indefinite quadratic q_B is a nonzero polynomial. Polynomial multiplication is injective even with distribution coefficients in A, by its scalar leading monomial. Thus normal order cannot cancel. The right side has order at most eleven, so Z has order at most one.

Put H=Z+cS EXACTLY. Then dH=-RS has order at most nine. A nonzero supported H has nonnegative order, and dH has order at least ten. Hence H=0 and RS=0. Its order-nine symbol is

    q_B(xi)^4 sum_a r4_k(X) ta xi_a=0.

Polynomial injection forces r4_k(X)ta=0 for each a. The radial energy identity on the compact pressure support with regular center and outer zero collar is

    integral t(X-lambda_* kappa²)t w2 dr
       =-integral (|t'|²+lambda_* kappa²|t|²)w2 dr.

It forces every ta=0. The order-eight remainder then forces t0=0. A zero compact pressure trace forces the pressure itself zero by P'+7alpha P=0 and its outer zero collar, as in K2605. Repeat in disjoint neighborhoods for finitely many points.

Therefore no nonzero monopole/dipole combination can have all off-source Einstein observations zero, regardless of homogeneous additions. This proof does NOT cover arbitrary higher jets: for a second jet, RS may already have order ten, so the strict order gap disappears. Characteristic covectors do not invalidate polynomial injection, but replacing it with elliptic unique continuation would be unjustified.

## 2. Differentiability of the actual fixed preparation

A Lipschitz bound alone is not differentiability. Here the source-variable kernel construction in K2594 supplies more. On a fixed regular annulus, the scalar tenth-order determinant kernel K(x,t) is continuous through source derivative eight; its ninth derivative is bounded piecewise and has the moving diagonal jump. The coefficient functions are smooth on each side. As an L2_x function, that ninth derivative is continuous in t: the moving jump affects a set of length tending to zero, and bounded one-sided coefficients give dominated convergence. Thus t maps to partial_t^8 K as a C1 L2_x function. Its tenth derivative is a locally bounded regular term plus a smooth multiple of delta_t, continuous into H_x^-1. The equation and K2594 frequency estimates bound these by C k22 and C k23 respectively. Consequently the eighth-source-derivative kernel is C2 into H_x^-1. This does not assert a tenth classical derivative across the diagonal.

The P numerator has source derivative order at most eight and total frequency cost at most ten. Its first and second point derivatives are therefore bounded by C k24 and C k25 respectively, with the latter in H_x^-1. Angular point deltas on the six-dimensional angular product are C2 into H^-6; this follows from Sobolev embedding H^6 into C2 with a positive margin. Mixed radial/angular derivatives obey the same combined estimates. The other commutator term P R uses source differentiation of R first and then fixed target differentiation; no unjustified joint classical derivative of order seventeen is taken. The retained second-order Einstein and TT channels are checked as well: their symmetric kernels are continuous, first source derivatives are piecewise bounded and L2-continuous under movement of the diagonal jump, and second source derivatives are regular terms plus a moving delta, continuous into H_x^-1. Their inherited polynomial frequency bounds fit the same conservative ceiling below; they are not discarded in the full-response differentiability claim.

Using the same Bezout coefficient bound and reconstruction as K2594, reserve H^-30 before the eight-order Bezout and at most26-order reconstruction. On compact parameter/source sets the full point-response map is C2 into local H^-64(B), with radial input loss at most135 and enough reserved A derivatives for continuity. Each fixed smooth radial pressure belongs to every needed radial operator domain. We use this conservative ceiling, not a sharp regularity claim. Polynomial frequency domination makes the differentiated angular/radial sums converge; scalar compact tests and finite profiles therefore have a C2 reading map. First derivatives solve the full differentiated source equations by continuity. The compact observer cutoff is inside E(G_A phi), retaining every cutoff derivative.

## 3. An invertible receiver Jacobian

Let theta comprise n profile coefficients and seven coordinate positions for each of m labeled nodes; restrict positions to disjoint coordinate balls. At the reference theta0 the tangent source is

    sum_i [dot(t_i) delta_(b_i) + t_i sum_a dot(b_i^a) partial_(b_i^a)delta_(b_i)].

The trace map is injective on compact conserved radial pressures. Section1 forces dot(b_i)=0 because t_i is nonzero, then dot(t_i)=0 and independence of the basis forces all coefficient variations zero. Thus the N derivative observation distributions are linearly independent outside the reference nodes. Compact smooth tests separate distributions; if their evaluation vectors did not span R^N, a nonzero annihilator would contradict this independence. Select N tests phi_j with invertible

    J0_(j,l)=partial_(theta_l)<h(theta),E(G_A phi_j)> at theta0.

D_j=E(G_A phi_j) is conserved and compact. Its support has positive distance from the finite reference set; shrink the position balls to retain disjointness for ALL theta under consideration. This is local support control, not uniqueness on an arbitrary fixed far-away observation region.

Write F(theta) for this N-vector of readings, sigma=sigma_min(J0)>0, and L an upper bound for ||D²F|| on a convex safe ball B_rho(theta0). If L rho<=sigma/2, the segment integral of DF-J0 gives

    (sigma/2)||theta-eta|| <= ||F(theta)-F(eta)||
                          <= (||J0||+sigma/2)||theta-eta||.

Thus F is injective and its inverse on its image is 2/sigma Lipschitz. The proof bounds the deviation from ONE fixed J0; a pointwise lower singular-value bound alone would not justify a global lower Lipschitz bound. Exactly invertible reading noise of norm delta gives parameter error<=2delta/sigma. A feasible least-squares fit whose residual and true-data error are each<=delta gives <=4delta/sigma, by the triangle inequality. Boundary/existence of a fit still matters.

## 4. Smooth-source and model-error consumers

Choose in each coordinate chart a fixed smooth unit nonnegative mollifier eta and define the invariant probability measure

    mu_(b,epsilon)=integral eta(u) delta_(b+epsilon u) du.

The delta is normalized in invariant density; do not replace this by unweighted coordinate density. Compact supports remain within the source balls for small epsilon. C2 point-response regularity gives uniformly on a smaller safe ball

    ||F_epsilon-F||<=C0 epsilon,
    ||DF_epsilon-DF||<=C1 epsilon.

If L rho<=sigma/4 and C1 epsilon<=sigma/4, the same 2/sigma inverse bound holds for F_epsilon. Its calibrated inverse has the same noise bound. Using the atomic calibration instead adds C0 epsilon model error, so any feasible fit with residual delta to data with noise delta obeys

    ||theta_fit-theta_true|| <= 2(2delta+C0 epsilon)/sigma.

This is a genuine location-and-profile consumer, but C0,C1,sigma and L depend on the declared preparation, basis and tests. No numerical value or noise distribution is supplied by existence.

## 5. Necessary limitations and failure of uniform location conditioning

Any C1 finite reading map that has a local Lipschitz inverse on an open N-dimensional source neighborhood must have injective derivative: take a directional difference quotient in the lower Lipschitz inequality. Hence fewer than N scalar receivers cannot have this form of stable local recovery. This is dimension of the supplied source model, not a particle count or a universal instrumentation optimum.

The nonzero-amplitude and separation hypotheses are substantive. At zero amplitude the corresponding position derivative is exactly zero. With all fixed tests and other parameters bounded, its norm is O(amplitude), so no uniform positive lower singular value persists as amplitude tends to zero. At a collision, two equal-profile amplitude columns coincide; for two nodes separated by d, bounded first derivatives make their difference O(d), so the smallest singular value of that fixed finite array is at most C d. At the coincident limit only the summed profile is observable and labeling is redundant. The statement concerns any ONE fixed C1 bounded array/preparation on that compact coordinate region; it is not an optimal rate for arrays allowed unbounded norms or separation-dependent design. These counterdirections rule out importing a uniform all-source condition number from the local theorem.

A sharper source-splitting consumer follows from the actual C2 map. For a fixed profile with response vector g(b), ||D²g||<=L2 gives

    ||g(b+v)+g(b-v)-2g(b)||<=L2||v||².

Compare the TWO distinct-node configurations b plus/minus v and b plus/minus v/2. For f(t)=g(b+tv)+g(b-tv), ||f'(t)||<=2t L2||v||², so their reading difference is at most3L2||v||²/4 while their labeled position distance is ||v||/sqrt2. Multiply by the common amplitude magnitude when it is not one. A fixed finite bounded array therefore cannot provide a uniform inverse Lipschitz constant as collisions approach, and fixed nonzero noise can conceal arbitrarily close splitting from a combined source. This gives no sharp optimal separation rate or universal numerical L2.

## Evidence and next condition

The probe checks the original remainder coefficient and sign, normal-order polynomial injection for first jets, an independent tenth-order jump/source-derivative fixture, actual conserved-pressure trace injection, and exact local-inverse/noise/collision controls. Analytic distribution and spectral estimates above carry the universal theorem; finite fixtures do not numerically construct a curved response matrix.

Off-grid source recovery and stability already have a substantial literature, for example [Super-Resolution Off the Grid](https://arxiv.org/abs/1509.07943). That paper concerns bandlimited measurements, not this coupled curved-product receiver family; no theorem or novelty transfers merely from the shared inverse-problem vocabulary.

Next compute a physically justified receiver/preparation matrix with certified conditioning, or develop characteristic sufficient regularity. Local reconstruction is now mathematically available for the specified model, while empirical apparatus, native displacement, causal domain, global source number, arbitrary multipoles and uniform collision stability remain separate. Do not requeue first-jet observability or local finite unknown-position inversion as absent.

[K2605](k2605-source-disjoint-pressure-response-2026-11-06.md), [K2594](k2594-reciprocal-distributional-response-2026-11-06.md), [probe](../../tests/channel-swings/k2607_local_pressure_source_recovery_probe.py), [report](../../lab/process/k2607-local-pressure-source-recovery.json).
