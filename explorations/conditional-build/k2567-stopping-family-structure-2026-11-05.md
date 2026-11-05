---
title: "K2567 A whole multiplier interval with no attaining adaptive policy"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: nonattainment for the original stopping law at positive multipliers through 98/51; no exact intermediate value or one-atom-tail classification
scripts:
  - tests/channel-swings/k2567_stopping_family_structure_probe.py
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
result: K2567
carrier: original predictable fresh fair test/use stopping histories with finite-hit success LAYER=toy CHIRALITY=N/A
pairing: unconditional success probability minus multiplier times expected original leakage ON=declared_carrier
real_structure: real controls and exact rational sign certificates
grading: trial, completed atom, finite schedule and nonabsorbing path remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: original adaptive nonattainment and finite terminal-stage refinement MAP-TYPE=evaluation
```

# No policy attains the value on an intermediate multiplier family

## Result and comparison

For every score 0<S<=1/2 and every multiplier

    0<lambda<=98/51,

no original adaptive policy attains the supremum of p-lambda C, where p is eventual **finite-hit** probability and C is expected original leakage cost. Private randomization, aborts, infinitely many possible trials and infinite expected trial counts are included. Every finite completed deterministic schedule can be strictly improved by a finite schedule: an optimized last atom can be split into two better atoms. The result extends the prior high-budget nonattainment range0<lambda<=4/5 into an intermediate range without asserting an intermediate value formula.

At lambda19/10 the K2565 bracket and rational41-stage witness remain valid. The new theorem says the actual unrestricted supremum in that bracket is unattained, not that the witness is optimal or that one finite atom with a continuum tail is globally optimal. It does not rule out a useful limiting family or K2563's relaxed hybrid compactification. The remaining interval(98/51,4/sqrt3) is not adjudicated; K2559's attained one-stage regime at and above4/sqrt3 supplies an explicit boundary against overextension.

This is independent mathematics for the supplied fresh fair law. SC-META-53 remains UNCERTAIN and LT-SM8/LT-GR6b retain their physical quotient/domain debts. No source, ledger0.263, canon, hardware, empirical, novelty or native GU claim changes.

## 1. Normalize the stage law and its generator

Reuse K2483/K2559's original stage accounting. For0<=a<=b<=1/2 set

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    A_b(v)=max_(0<=a<=b) [v-2w(a,b)]/(1+a), v>0.

The attained stage maximizer a_b(v) is unique. The established exact w_aa>0 and

    M(a,b)=-2(1+a)w_a(a,b)+2w(a,b),
    M_a=-2(1+a)w_aa<0, M(b,b)=0

prove: if v>=M(0,b), then a_b(v)=0; otherwise the unique interior maximizer solves M(a,b)=v. The upper endpoint a=b never maximizes for v>0 since the objective's left derivative there is negative. These strict-convexity and original-law identities are reused from K2559, not inferred from a numerical optimizer.

Define the output generator

    G_b(v)=2w_b(a_b(v),b).

At b=0 its continuous limit is

    q(v)=min_(0<=r<=1) [r v+(1-r)^2/(2(1+r))]
        =2sqrt(1+2v)-v-2, 0<v<=3/2;
        =1/2, v>=3/2.

Its minimizing ratio is r0(v)=max(0,2/sqrt(1+2v)-1). For an interior maximizer, implicit differentiation at fixed OUTPUT v gives

    d_b G_b(v)=2K(a_b(v),b),
    K=w_bb-w_ab^2/w_aa+w_b*w_ab/[(1+a)w_aa].         (1)

This is not the derivative along a fixed input-root or a theta-residual. The whole-domain sign below proves G_b(v)>q(v) in the required region.

## 2. An exact output-root ribbon for every v>=51/98

For b>0 put r=a/b and u(b)=2/5+b/2. Since log(1+x)<=x for x>=0, with x=(b-a)^2/[2(a+b)(2-a-b)],

    M(a,b)<=Mplus(a,b):=-2(1+a)w_a+2x.

At a=b*u(b), exact simplification gives

    51/98-Mplus = b H(b)/J(b),
    H=93125b^5+318000b^4-641900b^3+3832120b^2
                                    -5571616b+1929760,
    J=98(5b+14)(5b^2+14b-20)
                      *(25b^3+340b^2+156b-560).    (2)

On0<=b<=1/2, the numerator bH and denominator J have univariate Bernstein coefficients in y=2b respectively

    [0,482440/3,1143832/5,4556199/20,
       3584403/20,619529/6,1424949/64],
    [15366400,14570640,202736912/15,122223689/10,
       321986399/30,54707863/6,239472849/32].

All denominator coefficients are positive; the numerator has only its origin coefficient zero. Thus (2)>0 for b>0. Because M decreases in a, every interior root for v>=51/98 lies strictly below r=u(b). The limiting b=0 root at v=51/98 is exactly2/5, which is included. If the optimum is at a=0 it is treated separately below. No lower root bound is needed.

## 3. Positive generator derivative on the entire ribbon

Substitute a=rb into the rational derivative expression(1), reduce it exactly to N(r,b)/D(r,b), and substitute

    b=y/2, r=x*(2/5+y/4), 0<=x,y<=1.

The probe independently differentiates the original logarithm and constructs N,D; no copied coefficient table is trusted. Their tensor degrees are(9,13) and(10,16). Every Bernstein coefficient is strictly positive. Their exact minima are

    min N_B=57067571809/256000000000,
    min D_B=861/16;

the denominator maximum is87808/125. Independent inverse Bernstein expansion reconstructs both original power polynomials. Hence K>0 on the full closed ribbon, including b=0 after the removable limit. The two coefficient arrays and their digest are saved in the report. These finite exact coefficients certify the sign everywhere by the convex-hull property, not by sampled signs.

At the a=0 boundary,

    d_b G_b(v)=2w_bb(0,b)
               =-8(b-3)/[(b-4)^2(b-2)^2]>0.

Also M(0,b) strictly increases, with derivative

    4(3b^2-12b+10)/[(b-4)^2(b-2)^2]>0.

At fixed v there is at most one boundary-to-interior transition. The formulas for G agree there; both side derivatives are positive. Consequently

    G_b(v)>q(v), b>0, v>=51/98.                    (3)

An executed quantitative consumer uses k0=(57067571809/256000000000)/(87808/125). On the interior ribbon K>=k0. The boundary derivative is at least5/16: use3-b>=5/2 and(b-4)^2(b-2)^2<=64. Since5/16>2k0, integration through a possible transition gives the uniform bound

    G_b(v)-q(v)>=2k0*b.                            (4)

This is a strict terminal-refinement slope bound, not a positive uniform gap over all policies or a bound on their atom counts.

## 4. An optimized last atom is improved by TWO finite atoms

Fix a positive remaining score s and lambda in the stated interval; put theta=1/lambda>=51/98. Let a*=a_s(theta), so a*<s. The optimal one-atom original dual is lambda A_s(theta). Replace it by the atom(a*,s-epsilon), followed by the small atom(r0(theta)*epsilon,epsilon). For sufficiently small positive epsilon the controls remain admissible. The normalized tail value is

    T_epsilon=[theta-2w(r0*epsilon,epsilon)]/(1+r0*epsilon),
    T_0=theta, T'_0=-q(theta).

The new two-atom dual is

    lambda [T_epsilon-2w(a*,s-epsilon)]/(1+a*).

Its derivative at epsilon=0 equals

    lambda [G_s(theta)-q(theta)]/(1+a*)
         >=2lambda*k0*s/(1+a*)>0.                  (5)

Thus an actual positive finite epsilon gives strict improvement. No infinitely refined fluid policy or limit-attainment convention is required. The controls may be real; for a fixed rational score s, continuity lets nearby rational controls with that same total score retain the strict gain. Irrational fixed scores need not admit rational lengths summing exactly to s. If a last atom was not optimal among one-atom controls, first replacing it by its optimizer improves it already. Prefix survival is positive, so the gain persists when the replacement is attached to any finite earlier schedule. The probe also certifies a concrete rational last-atom split using logarithm intervals and the original survival prefixes.

Let V_lambda(s) be the full original adaptive dual supremum. This establishes

    V_lambda(s)>lambda A_s(1/lambda), for every s>0. (6)

It gives no exact value or global finite atom/tail classification.

## 5. Execute the all-adaptive transfer: no attaining policy

K2483 proves the least Bellman supersolution characterization for the original fresh fair test/use law. Here2/3<=1/(1+s)<=V_lambda(s)<=1; the lower bound is the free a=b=s stage. V is nonincreasing in required score: stop a larger-score policy at the smaller threshold, increasing hit probability and removing only nonnegative future costs. Thus V is Borel and may be evaluated on random adaptive remaining states. Continuity or a measurable optimizer selection is not required.

A reached trial at state s chooses predictable a,b. Put b'=min(b,s), a'=min(a,b'). Original clipping can only decrease failure and cost. Its Bellman slack is nonnegative. On a hit-capable trial b>=s>0, (6) gives the strict lower bound

    delta >= [(1+a')V_lambda(s)+2lambda*w(a',s)-1]/2
          >= (1+a') [V_lambda(s)-lambda A_s(1/lambda)]/2 >0. (7)

Failure has potential0; a hit has potential1. Iterate conditional expectation to any finite horizon, retaining nonnegative live and abort potentials, then discard those terms. For a fixed trial index n and any later horizon, the value gap is at least the expected slack at n. Pass to the infinite horizon using monotone convergence for costs and finite-hit events. Every policy with finite C and positive p has some finite trial n with positive hit probability. Before that trial's independent fair bit, a hit-capable set of reached histories has positive measure. Equation(7) makes its expected slack strictly positive. Therefore

    p-lambda C < V_lambda(S).

No-hit policies have value<=0<V; infinite expected cost has value minus infinity for positive lambda. Nonabsorbing paths approaching score0 never become finite hits. Unbounded trial counts and private randomization do not remove the strict finite-index slack. There is no contradiction between no attainment and arbitrarily close finite approximants.

## 6. Executed relaxed-hybrid consumer and constrained boundaries

K2563's finite-atom compact hybrid optimization does attain a maximum in its relaxed class. Within the present multiplier interval, every such maximizing hybrid with positive atoms must have a positive-length continuum block AFTER its last positive atom. If that final block had length zero, the last atom would either fail one-atom optimality (allowing a same-length improvement) or satisfy it. In the latter case replacing a small part by an optimized continuum suffix has the same strictly positive derivative(5). This modification preserves the allowed atom count: one atom is shortened, no new atom is added. Every earlier atom map is strictly increasing in its future value, as is the continuum flow by uniqueness and its positive variational derivative, so the strict gain survives the prefix. Zero-length padding atoms do not change this argument. A hybrid with no positive atoms already consists wholly of continuum.

This removes a boundary of the relaxed search space while preserving its attainment theorem. It does not prove one atom suffices or that all intermediate continuum blocks vanish. The continuum flow is a relaxed limit, not an original policy declared to reach its threshold only at infinity.


If an exposed constrained-budget frontier contact has supporting multiplier in(0,98/51], no original policy realizes that contact with dual equality. Otherwise it would attain the forbidden dual supremum. This statement is conditional on that supporting contact; it does not identify all corresponding budgets or prove a new strong-duality theorem. Lambda0 is excluded, as are budgets whose only supporting slope is0. K2565's certified finite witness still supplies an attained lower point and an exact-budget upper gap, rather than an attained frontier point.

The strongest contrary case is the established K2559 one-stage attainment at lambda>=4/sqrt3. The present ribbon cannot be continued there: at v=1/2<51/98 its boundary majorant already fails near b=0, and K itself becomes negative at other r values. The probe plants both exact failures. This prevents a positive certificate on one ribbon from becoming an all-output or all-multiplier assertion.

## Verification and next question

The whole-domain algebraic sign, inverse basis reconstruction and rational finite split are exact computation. Uniqueness of stage optimization, derivative/terminal refinement and all-adaptive strictness are explicit proofs with their reused hypotheses. Finite examples and sign controls do not replace those proofs. Internal independent specialists and a distinct hostile reviewer check them; no external-expert, proof-assistant, remote-CI, novelty or physical certification is claimed.

Next determine the transition between this nonattainment interval and the attained one-stage regime, or prove a global structural form for maximizing sequences in the intermediate region. A search for a finite exact optimizer inside the certified interval is now the wrong endpoint; search for limiting policies or value certificates. K2565's value bracket remains the useful quantitative benchmark.

[K2559 stage/root identities](k2559-parametric-stopping-concavity-2026-11-05.md), [K2561 earlier nonattainment](k2561-higher-budget-stopping-2026-11-05.md), [K2483 Bellman law](k2483-adaptive-stopping-bellman-2026-11-01.md), [K2565 value bracket](k2565-bellman-supersolution-2026-11-05.md), [probe](../../tests/channel-swings/k2567_stopping_family_structure_probe.py), [report](../../lab/process/k2567-stopping-family-structure.json).
