---
title: "K2207 Nonlinear detector stability in a relative-cap neighborhood"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional nonlinear local growth at a fully stationary supplied detector; no certified stationary instance or global optimum
scripts:
  - tests/channel-swings/k2207_detector_nonlinear_stability_probe.py
---

# K2207 Nonlinear detector stability

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
result: quantitative nonlinear local growth from strict infinite Schur stability
carrier: supplied positive scalar Fock vacuum and photon-added signal with binary diagonal occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form; Q-completion and relative-cap Banach perturbations ON=declared_carrier
real_structure: real effects and square-root Kraus with one positive real squeeze per outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction -- supplied free Hamiltonian and output-field energy
target: conditional nonlinear energy growth at fully stationary detectors MAP-TYPE=intertwiner
```

## Result and exact hypotheses

[K2204](k2204-detector-infinite-stability-certificate-2026-10-28.md) gives an
infinite Schur test for quadratic curvature. This result supplies the missing
nonlinear implication in a specified feasible topology. It does not certify
stationarity of K2204's rational test profile, which is explicitly nonstationary.

Keep the supplied scalar model of [K2201](k2201-detector-joint-variational-structure-2026-10-28.md):
p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n-x_n, q_n=3n-1, C=40/3,
R(z)=sum(n+1/2)z_n, T(z)=sum(n+1)sqrt(z_n z_(n+1)), and

    A(s)=41s²/6+3/(2s²),
    E(x,s1,s0)=A(s1)R(x)+A(s0)R(y)-C[s1 T(x)+s0 T(y)]+35/18.

Require all K2204 strict-monotone tail hypotheses (e>=L>0 and
0<sigma<=sqrt((1-e_(n+1))/(1-e_n))<=rho<1), and FULL stationarity:

    h_n=partial E/partial x_n=lambda q_n  for every n,
    A'(s_j)R(z_j)=C T(z_j),  z1=x,z0=y, s_j>0.

The same lambda applies to every coordinate. No probability constraint is added.
Let Q,b1,b0,d1,d0 be the joint Hessian data of K2201/4, D=diag(d1,d0),
K the constrained two-score susceptibility and S=D-K. Assume a certified
rational 0<eta<=1 satisfies S>=eta D. K2204's residual enclosure certifies
this when its lower matrix D-T_Galerkin-delta_res I-eta D is positive
semidefinite; delta_res is a residual bound, not the cap radius below.

Define ||v||cap=sup_n |v_n|/min(x_n,y_n), and B_c={v: ||v||cap<infinity,
sum q_n v_n=0}. For W(v,t)=Q(v)+sum_j d_j t_j², the theorem is

    v in B_c, ||v||cap<=eta/60, max_j |t_j|/s_j<=eta/60
      => E(x+v,s+t)-E(x,s)>=eta W(v,t)/8.                 (1)

After reoptimizing both squeezes, H(x)=min_s E(x,s),

    ||v||cap<=eta/180, v in B_c
      => H(x+v)-H(x)>=eta Q(v)/8.                       (2)

These imply strict nonlinear local minimality in the relative-cap topology.
They say nothing about all feasible Q-small perturbations, singular Schur data,
global uniqueness, a new energy bracket, or a physical apparatus. They establish
no GU source, ledger, canon, physical quotient or external novelty claim.

## 1. Feasible topology and infinite sums

B is weighted l-infinity and complete. If ||v||cap<=delta<1, both branch paths
z_j+tau w_j, w1=v,w0=-v, stay between (1-delta)z_j and (1+delta)z_j
for every tau in[0,1]. Hence they remain interior and retain exact contrast.
The relative-coordinate bounds bound each Q edge by a constant times
s_j delta²(n+1)sqrt(z_n z_(n+1)); this sum is finite. Truncations converge
in Q: interior tails vanish and the final boundary edge is bounded by a
constant times delta² m(z_m+z_(m+1)), tending to zero. Thus B embeds
continuously into the inherited energy completion. Contrast and gradient sums
converge absolutely, since |v_n|<=delta p_n and the inherited scores and
h_n are O(n+1). Coordinate stationarity therefore cancels the first variation
on all B_c. Constrained finite truncations use the inherited finite-coordinate q-repair from K2204; continuity of q and Q makes the repair tend to zero. No Frechet differentiability on an open Q-ball is assumed.

## 2. Strict joint quadratic bound

S>=eta D means K<=(1-eta)D. The constrained Riesz representation gives

    |sum b_j(v)t_j|<=sqrt(1-eta)*sqrt(Q(v)*sum d_j t_j²).

Consequently the joint Hessian J(v,t)=Q(v)+2sum b_j(v)t_j+sum d_j t_j²
satisfies J>=(1-sqrt(1-eta))W>=eta W/2. This holds on the entire constrained
energy completion, before the stronger topology is used for nonlinear control.

## 3. Exact all-tail directional remainder

For one edge f(tau)=sqrt((a+tau u)(b+tau v)), direct differentiation yields

    -f''(tau)=(ub-va)²/[4((a+tau u)(b+tau v))^(3/2)].     (3)

For a branch let F=-D²T(z)[w,w]>=0. Relative-cap bounds imply
F(tau) is between (1+delta)^-3 F and (1-delta)^-3 F.
Dominated edge summation justifies the exact identity

    T(z+w)=T(z)+DT(z)w-I, I=integral_0^1(1-tau)F(tau)d tau.

The branch expansion beyond its linear and half-Hessian terms has remainder

    R(z)[A(s+t)-A(s)-A'(s)t-A''(s)t²/2]
    +R(w)[A(s+t)-A(s)-A'(s)t]
    +C[(s+t)I-sF/2].                                    (4)

Here |R(w)|<=delta R(z), A''=41/3+9/s^4 and the third derivative of A=-36/s^5.
For |t|<=epsilon s, summing both branches gives

    2|Rem|<=g(delta,epsilon)Q(v)+h(delta,epsilon)sum d_j t_j²,
    g=(1+epsilon)(1-delta)^-3-1,
    h=(4/3)epsilon(1-epsilon)^-5+delta(1-epsilon)^-4.     (5)

The g expression dominates the lower deviation too: the sum
(1+epsilon)/(1-delta)^3+(1-epsilon)/(1+delta)^3 is>=2,
by monotonicity in epsilon and convexity at epsilon=0.
For delta,epsilon<=r<=1/4, g<=15r and h<=9r. Indeed
[(1+r)/(1-r)^3]'=(4+2r)/(1-r)^4<=128/9<15 and
(4/3)(1-r)^-5+(1-r)^-4<=6400/729<9.
At r=eta/60, 2|Rem|<=eta W/4. Combine with half of the quadratic lower
bound to obtain(1), retaining every edge and the infinite tail.

## 4. Reoptimized squeeze control

Put k(z)=CT(z)/R(z)>0. The unique minimizing squeeze solves A'(s)=k.
Both R and T change by a factor in[1-delta,1+delta], so k'/k lies between
(1-delta)/(1+delta) and its reciprocal. Since
s A''(s)-A'(s)=12/s³>0 and A'(s)>0 at the minimizer,

    0<d log s/d log k=A'(s)/(s A''(s))<1.

Integrating gives |s'/s-1|<=2delta/(1-delta). For delta<=eta/180 this is
at most eta/60 (ratio<=120/179<1 when eta<=1). Apply(1) to the actual
reoptimized squeezes and drop their nonnegative quadratic contribution to get(2).
This closes the conditional nonlinear implication, not the stationarity input.

## 5. A nonlinear tangent model at the actual nonstationary profile

Effect stationarity is needed only to call the result a local minimum. Without
it, retain ell(v)=sum h_n v_n in the expansion: both(1) and(2) hold with
ell(v) SUBTRACTED from their left sides, assuming minimizing squeezes and the
same strict S certificate. This is a nonlinear tangent lower model.

K2204's actual rational profile t_n=2^(-n-1),
e_n=((1-t_n²)/(1+t_n²))² has S>6I at its certified minimizing squeezes.
Those intervals give s1,s0>4/5; R(z_j)<=R(p)=5/6 implies

    d_j<(5/6)[41/3+9(5/4)^4]<30.

Thus eta=1/5 is valid. The actual profile has a joint tangent lower bound
with coefficient1/40, cap and relative squeeze radii1/300, and a reduced
tangent lower bound with coefficient1/40 and cap radius1/900. This reuses
K2204's all-tail curvature certificate; it is not a new optimum bracket.

It is explicitly NOT a local minimum. Direction a=(2,1,0,...) has q(a)=0.
The exact coherence gradients are gx0=25/68,gy0=5/34,gx1=799/650,gy1=51/26.
Using the actual squeeze intervals, the companion probe certifies

    ell(a)=(5/2)[A(s1)-A(s0)]
      -C[s1(25/34+799/650)-s0(5/17+51/26)]>0.

The probe further certifies the actual step v=-a/100000, with cap norm<=1/900, has strictly negative energy change at the fixed minimizing squeezes, and verifies the tangent lower bound after subtracting ell(v). Reoptimization can only lower that new energy. Positive curvature and a nonlinear tangent bound do not substitute
for full stationarity. This actual countercontrol exercises the theorem's
most consequential missing hypothesis.

## 6. Why an energy ball cannot replace the cap neighborhood

For N>=2 set v_N=2y_N, v_0=2q_N y_N, others zero. Since q0=-1,
q(v)=0 exactly. Yet x_N+v_N>p_N, while Q(v) tends to zero. The inherited
uniform ratio bounds give Q(v)=O(N y_N+N² y_N²); the complementary tail
decays geometrically. For the isolated N spike, neighboring branch edge weights
scale as O(N/y_N), and for the compensating coordinate0 the weight is fixed.
The coefficient1 version reaches the cap. Thus no Q-neighborhood is wholly
feasible even on the exact-contrast space. This does NOT establish instability
against feasible Q-small paths; it only prevents an unjustified open-ball argument.

## Reproduction and next condition

The companion probe checks the exact directional edge identity, squeeze
elasticity and Taylor constants, a nonlinear rational edge against the original
energy, genuine corrupted coefficients, and actual exact-contrast tail spikes
on K2204's rational profile. Universal implications use the written proof;
finite controls do not certify stationarity, the infinite theorem, or novelty.
Run `python tests/channel-swings/k2207_detector_nonlinear_stability_probe.py`;
`--write` regenerates the report. Next supply a certified fully stationary
profile and a strict S certificate. K2198 fixed-squeeze optimizer enclosures
alone are not joint squeeze stationarity. Global comparison remains separate.
