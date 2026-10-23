---
title: "K1989: Genuine capped pulse dual and certified strong distance"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1989_capped_pulse_dual_certificates.py
  - tests/channel-swings/k1989_capped_pulse_dual_certificates_probe.py
---

# K1989: Genuine capped pulse dual and certified strong distance

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
result: no-gap capped continuum dual, exact lower certificate and whole-strip strong-distance bound
carrier: actual optimal scalar phase and width9 characteristic strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue L2 norm with row and column conditional-average projections ON=characteristic_strip
real_structure: real bounded measurable pulse, amplitude23/100
grading: characteristic row and column coordinates, not source chirality
action_owner: repository-construction -- secondary minimum-pulse-norm problem
target: rigorous dual and amplitude-feasible approximate pulse certification MAP-TYPE=intertwiner
```

## The capped target and the new certificate

Use exactly [K1980](k1980-constructive-minimum-norm-pulse-2026-10-23.md)'s
D={(u,z):-3<=u<=3,u<=z<=u+9}, H=L2(D), row/column projections P,Q,
g=2 phi_star/9, M=23/100, and nonempty feasible set
C={|v|<=M,Pv=g,Qv=0}. Let v_dagger be its unique minimum-norm pulse and
p_star=||v_dagger||^2/2. This is the secondary pulse norm, not Dirichlet phase
energy. K1986's uncapped optimizer cannot replace it.

Here is the actual capped dual, with no assumed Slater point or attained
multiplier. For row potential a=Pa and column potential b=Qb in H, define

    h=a+b, w=clip_[−M,M](h),
    f*(h)= h^2/2                      if |h|<=M,
           M|h|−M^2/2                otherwise,
    D(a,b)=<a,g>−int_D f*(a+b).                         (1)

Then sup_(a,b) D(a,b)=p_star. Every pair of finite L2 potentials gives a
rigorous lower bound, even when its clipped w fails the exact marginals.

## Self-contained no-gap argument at the saturated boundary

For any |v|<=M, maximizing hv−v^2/2 pointwise gives f* and maximizer w.
Because <a,v>=<a,Pv> and <b,v>=<b,Qv>, every v in C obeys
D(a,b)<=||v||^2/2. This proves weak duality with the actual strip measure.

Let v_epsilon be K1980's exact regularized minimizer. Its box variational
inequality says that, with

    a_epsilon=(g−Pv_epsilon)/epsilon,
    b_epsilon=−Qv_epsilon/epsilon,

one has v_epsilon=clip(a_epsilon+b_epsilon). These potentials belong to the
required ranges. Substitution into(1) gives the exact identity

    D(a_epsilon,b_epsilon)
      = ||v_epsilon||^2/2
        + [||Pv_epsilon−g||^2+||Qv_epsilon||^2]/epsilon. (2)

K1980 proves v_epsilon -> v_dagger STRONGLY as epsilon ->0. The first term
in(2) tends to p_star, its second term is nonnegative, and weak duality bounds
the whole expression above by p_star. Squeezing proves no gap, and also that
the residual squared divided by epsilon tends to0. This last statement is
an asymptotic consequence, not an effective rate.

Finite dual attainment and bounded limiting potentials do not follow.
The elementary conjugate/duality framework is standard; see
[Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).
The argument above proves the saturated infinite-dimensional case directly;
it does not invoke a finite-dimensional constraint qualification.

## Released strong-distance and saturation consumers

The scalar box-quadratic is1-strongly convex. Directly, h−w is an outward
normal to the interval at w, so for every |v|<=M,

    v^2/2+f*(h)−hv >= (v−w)^2/2.

After integration, for any exactly feasible v,

    ||v−w||^2 <= ||v||^2−2D(a,b).                       (3)

In particular, if U is ANY certified upper bound on ||v_dagger||^2,
then ||v_dagger−w||^2<=U−2D. The always valid U=54M^2 uses existence and the
amplitude cap. A better exactly feasible primal witness immediately improves
the same distance certificate; a small marginal residual alone does not.
Equation(3) applies even when w itself is infeasible. It is a whole-strip
strong L2 error bound, without H1 or phase-energy inference.

The same squared bound B controls local errors and saturation disagreement:
for eta>0, the area where |v_dagger−w|>=eta is at most B/eta^2. If w=M on a
region, the part where v_dagger<=M−eta has that same bound. This is a measure
estimate, not an exact identification of the optimizer's active set.

## Executed continuum certificate on the actual phase

Take24 row intervals and60 column intervals of width1/4. Potentials are
constant on their respective intervals, with stored rational values rounded
to a denominator10^8. A floating coordinate search proposes these numbers;
its convergence or optimality is NOT used as proof. Every certificate is
replayed in exact rational arithmetic from the stored witness.

Integrate f*(a+b) by the exact area of each rectangle intersected with D.
The source phase is the actual K1969 algebraic phase: its quartic root and
lambda interval are retained. Integrate its piecewise polynomial rational
surrogate exactly and subtract the rigorous uniform forcing error times
9 sum_i |a_i| Delta u_i. No grid value stands in for continuum feasibility.
The separate implementation uses polygon clipping and shoelace areas, checks
the algebraic root and coefficient intervals, and independently evaluates
the pointwise strong Fenchel inequality.

The exact rational result gives the outward-rounded bounds

    2.34940177149 < ||v_dagger||^2 <= 2.8566,
    ||v_dagger−w||_H < 0.712179.                        (4)

The report also gives w's exact norm, its saturated area, and a nonzero
cell-mean marginal residual (about1.1191e−7 squared, for the phase surrogate).
The forcing uncertainty is below1e−30 in the dual objective; a nonzero
column residual independently proves w is NOT exactly feasible. The apparently
small residual is therefore not claimed to make w a physical endpoint pulse.
A regularization maximizing sequence exists by(2), but(4) is the achieved
certificate; no arbitrary-accuracy strong stopping modulus is claimed.

## Hostile review and remaining construction

The independent probe checks1475 exact polygon/conjugate controls and rejects
four root, multiplier, lower-bound and strong-bound faults after baseline.
An initial empty-polygon sum introduced a floating zero into the separate
checker; that arithmetic bug was fixed with an exact rational zero before
any result was accepted. It was a checker failure, not a successful mutation.

The largest overclaim would turn the clipped witness into an exactly feasible
optimizer, or promote the secondary norm bound to phase-energy accuracy.
The nonzero residual prevents both. Exact-marginal capped primal construction,
sharper feasible upper bounds, and quantitative dual convergence remain useful
next questions. SC-META-53 remains UNCERTAIN; source, physics-ledger and canon
verdicts stay unchanged. No external verification or novelty claim is made.
