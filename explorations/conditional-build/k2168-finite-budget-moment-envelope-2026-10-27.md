---
title: "K2168 Globally convex finite-budget moment envelope"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed positive free-field model and binary diagonal effects with reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py
---

# K2168 Globally convex finite-budget moment envelope

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2168 globally convex moment relaxation, strict informative gap and certified finite-budget bounds
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

[K2166](k2166-uniform-feedback-weak-budget-2026-10-27.md) settled the sharp weak-budget
coefficient, including rare branches and all occupation tails. The same two-moment
relaxation has stronger GLOBAL structure: its scalar branch energy is strictly convex,
and minimizing the binary bound requires only one strictly convex scalar problem.
Its inverse bounds the whole finite-budget contrast frontier. The bound is sharp at
zero but strictly below the true minimum energy at every positive contrast. It is a
useful bound, not a solution of the actual infinite-effect optimization.

All hypotheses and the fixed signal/instrument class are those of
[K2162](k2162-feedback-detector-frontier-2026-10-27.md) and K2166: positive free scalar
vacuum, N>0, finite supplied moments, binary diagonal effects, and one real squeeze per
reported outcome; hidden diagonal Kraus have a common reported-outcome squeeze. Energy
means vacuum output field energy. Preparation, switching, record/reset, stable autonomous
apparatus, arbitrary local channels and signal-averaged costs remain separate. SC-META-53
remains UNCERTAIN, and LT-SM8/LT-GR6b, source, ledger and canon do not change. No GU-derived
positive state, observed chirality or native family count is obtained.

## 1. Global strict convexity of the relaxed branch

Write R=mu+1/2, S=sqrt(mu(mu+1)), A(x)=alpha x²+beta/x² with
alpha=m2/(2nu)>0, beta=nu/2>0, C=2sqrt(N(N+1)) E_sum>0 and

    G(mu,x)=R A(x)-Cx S+D_M mu+D_w,
    f(mu)=min_(x>0) G(mu,x).

The unique squeeze minimizer solves R A'(x)=CS. For mu>0 this implies A'>0.
At that minimizer, direct differentiation yields

    G_mu,x=-C/(4RS), G_mu,mu=Cx/(4S³), G_x,x=R A'',
    f''(mu)=Cx/(4S³) [1-A'/(4R² x A'')] > 0.          (1)

Indeed xA''-A'=8beta/x³>0 and 4R²>1. This is the Schur complement of the squeeze
Hessian, not joint convexity assumed for G. At mu=0 the minimizer is
x0=(beta/alpha)^(1/4); f extends continuously and f'(0+)=-infinity because the
negative square-root cross term dominates its derivative. K2166's energy coercivity
proves f>=0 with its only zero at N, and gives a strictly positive linear lower tail.

Let x_infinity solve A'(x_infinity)=C and set

    a=A(x_infinity)-C x_infinity+D_M>0,
    b=(a-E_sum)/2.

Expansion of S=mu+1/2-1/(8mu)+O(mu^-2), together with the stationary minimum
and D_w-D_M/2=-E_sum/2, gives

    f(mu)=a mu+b+C x_infinity/(8mu)+O(mu^-2).          (2)

The optimizer correction is O(mu^-2) and changes the displayed energy only at
higher order. Positivity of a follows from K2166's uniform coercive tail, not from
a numerically fitted asymptote.

## 2. A complete scalar minimization, including the rare-outcome endpoint

Relabel the click outcome to make contrast Delta positive and put d=N Delta.
Completeness gives 0<w<=1-Delta and branch means mu1=N+d/w, mu0=N-d/(1-w).
For 0<Delta<1, every allowed detector satisfies

    E >= L_d(w)=w f(mu1)+(1-w)f(mu0).                 (3)

The closure of this RELAXED problem includes

    L_d(0)=a d+f(N-d).                              (4)

This is the recession limit w->0 while M->d>0; it is not a realizable zero-probability
branch of bounded binary effects. With f_i=f(mu_i), p_i=f'(mu_i),

    L'_d=f1-(d/w)p1-f0-(d/(1-w))p0,
    L''_d=d²[f''(mu1)/w³+f''(mu0)/(1-w)³]>0.         (5)

The derivative diverges positively at w=1-Delta because mu0->0. At w=0 its
right limit is

    B(d)=aN+b-f(N-d)-d f'(N-d).

B'(d)=d f''(N-d)>0. Strict convexity of f and its affine asymptote imply
B(0)=aN+b<f(N)=0, while B(N-)=+infinity. Thus there is exactly one d_c in (0,N).
For d<d_c the minimizer is the unique interior root L'_d=0; for d>=d_c it is w=0.
The endpoint transition belongs to the relaxation and may lie beyond the actual
maximal contrast. No physical rare-click phase is inferred.

## 3. Global contrast envelope and its sharpness boundary

Define R_bound(Delta)=min_(0<=w<=1-Delta) L_(N Delta)(w), R_bound(0)=0.
The perspective of a convex f is convex. More explicitly, if h(d)=min_w L_d,
then at an interior minimizing w,

    h'(d)=f'(mu1)-f'(mu0)>0,
    h''(d)=f''(mu1)f''(mu0)/
       [f''(mu1)(1-w)³+f''(mu0)w³]>0.               (6)

These follow by eliminating w from the two-variable perspective Hessian.
On the endpoint branch h'=a-f'(N-d)>0 and h''=f''(N-d)>0. Values and first
derivatives match at d_c by B(d_c)=0. Consequently R_bound is continuous,
strictly increasing and strictly convex on positive contrasts below1.
Its small-contrast asymptote is kappa Delta². First apply K2166's homogeneous
coercivity to the relaxed branches as well: boundary-probability sequences have
Delta²/E tending to zero, while an interior vanishing-energy sequence forces both
means to N. Taylor expansion at that interior vacuum minimum then forces w->1/2;
equivalently the local Schur coefficient in K2166
and the balanced trial w=1/2 give matching bounds.

For budget B, E<=B implies R_bound(Delta)<=B. This yields a global inverse upper
bound, capped by K2162's actual maximal contrast. If B exceeds R_bound at that
cap, the relaxation alone supplies no further restriction.

The inequality is STRICT at every fixed informative contrast in the actual instrument
class. Equality in the branch Cauchy inequality requires a geometric sequence of
Schmidt amplitudes. For a positive click mean mu1>N, this would give

    e_n=c0 (r²/z)^n, r²=mu1/(1+mu1)>z=N/(N+1), c0>0.

It contradicts 0<=e_n<=1. Thus T1<sqrt(M1(M1+w1)); the positive coefficient Cx1
makes the branch energy strictly larger than its relaxed value. Countable hidden
Kraus cannot lower it below the positive-root instrument. K2162's compact-effect
attainment and compact squeeze reduction apply also at fixed feasible contrast
(the contrast equality is closed under the same dominated convergence). Hence the
minimum E_min(Delta) is attained and E_min(Delta)>R_bound(Delta) for every feasible
Delta>0. This last compactness step matters: strictness for each detector alone
would not rule out equality of infima.

## 4. Certified finite-budget consumers

Use the realizable fixture m1=5,m_-1=5/9,m2=41,nu=3,N=1/3,E_sum=10.
Here alpha=41/6,beta=3/2,C=40/3,D_M=25/3,D_w=-5/6. The companion probe uses
ONLY exact rational interval arithmetic, integer-square-root enclosures and monotone
root brackets, not floating minimization:

    0.5423370097 < R_bound(1/2) < 0.5423370099,
    1.2985788504 < R_bound(3/4) < 1.2985788507.         (7)

Both minimizers are interior. It also proves B(N*3/4)<0, so every physically
relevant contrast up to the exact cap Delta_max=3/4 lies before the relaxed endpoint
transition. Full rational optimizer and energy enclosures are saved in the report;
decimal displays are outward rational bounds.

For example field budget B=1/2 cannot reach contrast1/2. The older coarse bound
E>=Delta²/2 only supplied1/8 at that contrast. At saturation, the relaxed bound
is approximately1.299 while K2160/K2162's actual globally optimal saturation energy
is enclosed near4.230496769. This large gap is direct evidence against interpreting
R_bound as the true finite-budget frontier. The new result is useful between zero
and saturation without repeating the old weak-budget or tie optimization.

For each rational mu, the probe brackets x by signs of A'(x)-CS/R. It evaluates f
and f' outward, brackets the unique zero of L', then bounds the minimum below by
the supporting tangent at the midpoint and above by its value there. The proof of
convexity and monotonic roots supplies the global certificate; sampling does not.

## 5. Remaining choices and evidence

A tighter finite-budget bound must price the bounded-effect Cauchy deficit or solve
K2162's effect program; the relaxation cannot be made exact by more digits. A stable
autonomous controller remains a distinct strongest physical alternative: K2154's
strong-control approximation does not supply a bounded-below reusable apparatus or
preparation/reset account. That missing construction is not a prohibition on conditional
research, nor a source-derived constraint.

Symbolic controls independently derive Schur curvature, the perspective derivatives,
its minimized Hessian and physical fixture constants; changed cross coefficient,
complement, weight, Hessian and Cauchy inputs produce real failing checks after a green
baseline. Universal domain, convexity, strict gap and compactness arguments receive
independent internal specialist review. No proof-assistant, external-expert, empirical
or novelty certification is asserted.
