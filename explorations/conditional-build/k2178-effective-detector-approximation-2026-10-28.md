---
title: "K2178 Effective finite-head approximation of detector energy"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, exact contrast one half, vacuum output field energy only
scripts:
  - tests/channel-swings/k2178_effective_detector_approximation_probe.py
---

# K2178 Effective finite-head approximation of detector energy

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
result: K2178 explicit uniform finite-head error and contrast-preserving repair
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

The fixed N=1/3, exact signed contrast1/2 infinite detector problem now has an
explicit uniform finite-head approximation rate. A cap-feasible moment relaxation
and a constructive repair give a certified two-sided error of order
sqrt(K)2^-K, without assumptions on the unknown optimizer's tail or margin.
The released error-budget consumer turns a requested tolerance into a cutoff
and finite optimization precision. It does not solve that finite optimization
or improve K2176's current numerical energy bracket.

This is GU-independent conditional mathematics of the same supplied positive
free-field instrument as [K2176](k2176-detector-certified-convergence-2026-10-27.md).
Its energy is vacuum output field energy, excluding apparatus, clock, preparation,
switching and reset. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b, source,
ledger0.263 and canon stay unchanged. Occupation grading is not source chirality.
No arbitrary-channel, physical quotient, novelty or external acceptance claim.

## Theorem

Write p_n=(3/4)4^-n, q_n=3n-1, x_n=p_n e_n, y=p-x,
R_1=sum(n+1/2)x_n, R_0=5/6-R_1, and

    E(x;s1,s0)=R_1 A(s1)+R_0 A(s0)
                 -(40/3)[s1 T(x)+s0 T(y)]+35/18,
    A(s)=41s²/6+3/(2s²),
    T(x)=sum_(n>=0)(n+1)sqrt(x_n x_(n+1)).

The target E* is the minimum at exact signed contrast sum q_n x_n=1/2.
[K2174](k2174-joint-coherence-detector-2026-10-27.md) permits both squeezes to be restricted to S=[2/3,113/100].

For K>=2 set

    B_K=3(K+1)4^-(K+1),
    D_K=(K+11/6)4^-(K+1),
    H_K=(K+4/3)4^-K/2,
    tau_K=4D_K+(452/15)H_K,
    rho_K=(2453/45)B_K+(452/15)sqrt(3B_K/32).

Define P_K by 0<=x_n<=p_n for n<=K and

    1/2-B_K <= sum_(n=0)^K q_n x_n <= 1/2.

For each head in P_K append the EXACT infinite tail x_n=p_n/2, n>K.
Let m_K be the minimum of the resulting full energy over P_K and S². Then

    m_K-tau_K <= E* <= m_K+rho_K.                 (1)

All sets are nonempty and compact; the energy is continuous, including at caps.
Both errors vanish explicitly. Their combined order is O(sqrt(K)2^-K).
This is an a priori effective convergence theorem, without knowing any unknown
optimizer's coordinatewise margin, gradients, or tail shape.

## Exact tails and truncation lower bound

Direct geometric summation gives

    sum_(n>K) q_n p_n=B_K,
    sum_(n>K)(n+1/2)p_n=D_K,
    sum_(n>=K)(n+1)sqrt(p_n p_(n+1))=H_K.

For a true feasible effect, the omitted contrast is in [0,B_K] because K>=2,
so its retained head belongs to P_K. Replace its tail by p/2, obtaining v.
The radius changes by at most D_K. For either outcome, only coherence edges
n>=K change, with total absolute change at most H_K. Convexity of A and its
endpoint values, together with A>=sqrt(41)>6, give 6<A(s)<10 on S; hence
|A(s1)-A(s0)|<4. Also s1+s0<=226/100. Therefore

    |E(v;s)-E(x;s)| <= 4D_K+(40/3)(226/100)H_K=tau_K.

Explicitly A''(s)=41/3+9/s^4>0. The maximum over the interval is bounded
by the endpoint values 1385/216 and 7584941801/766140000, both strictly below10.
AM-GM gives A(s)>=2sqrt((41/6)(3/2))=sqrt(41)>6 for every s>0.

Apply this at a true minimizer to obtain m_K<=E*+tau_K. There is no dropped
occupation tail in the relaxed objective.

## Uniform repair and upper bound

Fix the reference r_n=p_n f_n, where f_0=1/6 and f_n=5/6 for n>=1. It has
exact contrast 1/2, and p_n/6<=r_n<=5p_n/6. Given any v from P_K with its
half tail, let

    t=4B_K, u=(1-t)v+t r,
    delta=sum q_n u_n-1/2,
    w_0=u_0+delta, w_n=u_n (n>=1).

For K>=2, 0<t<=9/16<1. Since d(v) lies in [1/2-B_K/2,1/2+B_K/2],

    |delta| <= (1-t)B_K/2.

Meanwhile u_0 and p_0-u_0 are both >=t p_0/6=t/8=B_K/2.
Thus w is strictly cap-feasible, and q_0=-1 proves d(w)=1/2. Its eventual
tail is the explicit constant effect 1/2+t/3. This correction's SIGN matters:
one ADDS delta to x0 because the contrast coefficient there is negative.

For fixed squeezes the energy is convex in x: both coherences are concave,
the remaining terms affine. Also

    T(x)+T(p-x) <= T(p)=2/3

by the two-dimensional Cauchy inequality on each edge. Together with 6<A<10,
every cap-feasible effect at squeezes in S satisfies

    -31/10 <= E <= 185/18.

This common range has width 602/45. Convexity therefore bounds the mixture
increase by (602/45)t. Changing coordinate zero alone changes the radius
term by at most 2|delta|<=B_K. Its only affected coherence edge is n=0;
for each branch, |sqrt(a)-sqrt(b)|<=sqrt(|a-b|) and x1,y1<=p1=3/16 imply
a coherence change at most sqrt(p1 |delta|). Consequently

    E(w;s)-E(v;s)
       <= (602/45)(4B_K)+B_K
          +(40/3)(226/100)sqrt((3/16)(B_K/2))
       =rho_K.

Use a relaxed minimizer v and its squeezes to prove E*<=m_K+rho_K.
This does not claim that the repaired profile optimizes the original problem.

## Finite exact objective and a terminating epsilon consumer

The full moments for a head x0,...,xK and constant tail effect c are

    w=sum_(0..K)x_n+c 4^-(K+1),
    M=sum_(0..K)n x_n+c 4^-(K+1)(K+1+1/3).

For a branch its coherence is the finite sum of edges n=0,...,K, with boundary
x_(K+1)=c p_(K+1), plus EXACT tail c H_(K+1). Thus the objective is a finite
algebraic expression with rational data. Introduce nonnegative roots for both
branches' K+1 edges and variables z_i satisfying z_i s_i²=1. The existential
real formula E<a has 3K+7 variables and polynomial degrees at most three.
Real closed field quantifier elimination therefore decides each rational
comparison; bisection provides a theoretical terminating exact certifier.
No quantifier-elimination implementation or practical runtime is asserted here.

For rational epsilon>0, increase K>=2 until an outward rational radical bound
certifies tau_K+rho_K<=epsilon/2; this terminates. Start with m_K in [-4,11]
and use J rational comparison steps, where 15/2^J<=epsilon/2. An interval
[ell,u] for m_K then gives [ell-tau_K,u+rho_K] for E*, width<=epsilon.
Equality at a bisection test is harmless: deciding the strict formula m_K<a
still preserves the closed bracket. Algebraic sample-point extraction can
supply a finite feasible head, to which the explicit repair applies.

The executable epsilon consumer must adapt its radical enclosure precision:
take integer P=max(10^45,ceil(1000/epsilon)) and use integer-square-root bounds
of width1/P. The contribution of rounding to rho is at most(452/15)/P,
which is at most(452/15000)epsilon<epsilon/2. Thus its cutoff search really
terminates for every positive rational epsilon. A fixed precision would
incorrectly stall below its enclosure floor. The scratch control additionally
checks epsilon=10^-60: K208,J205 returns a certified width below5.931e-61.

The exact checker verifies:

- K=20,J=18: conditional on solving the finite problem to width15/2^18,
  the resulting original-problem width is <0.000092142; this is an error
  budget, NOT a newly computed enclosure around an energy value.
- K=16,J=15: corresponding width <0.000960690.
- The generic epsilon consumer picks K20,J19 for epsilon=1/10000, with
  certified resulting width <0.000063532; K27,J25 for epsilon=1/1000000,
  with width <0.000000762051.

These count finite variables and exact-decision calls; they do not establish
practical bit-complexity or numerical-search convergence. Existing K2176
global energy bounds remain the actual released numerical enclosure.

## Counterconstruction, limits and strongest alternative

Naively flattening a cap-boundary head and correcting x0 can leave the box.
The low-head-contrast case x0=0 explicitly detects the error if t is weakened
from4B_K toB_K. The uniform exact-contrast reference is essential to this
repair proof. Dropping the tail, narrowing the head contrast interval, or
reversing the coordinate-zero correction each invalidates an actual formula.

The theorem establishes neither a rate for K2176's AM-GM tangent-dual class,
monotonicity of m_K, global squeeze uniqueness, a physical apparatus energy
account, nor exact-frontier monotonicity/threshold saturation. The strongest
alternative research direction is a structural theorem for the fully squeeze-
minimized frontier or an autonomous controller with owned resource costs.
An infimum over squeeze pairs of convex fixed-squeeze energies need not be
convex, so fixed-squeeze convexity alone cannot establish that alternative.

## Verification and prior art

Run `tests/channel-swings/k2178_effective_detector_approximation_probe.py` in the
repository Python environment; `--write` regenerates its exact report. Written
uniform-tail/repair arguments are independently reviewed separately from finite
controls. The probe checks actual formulas, cap-boundary repairs, infinite tails,
radical intervals and error-budget consumers; planted faults alter those formulas.
No proof-assistant certification or implemented global optimizer is claimed.

Concavity of geometric means and convex mixing are standard; see
[Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).
The real-closed-field quantifier-elimination step is standard algorithmic real
algebra, illustrated by [Mahboubi and Cohen (2012)](https://arxiv.org/abs/1201.3731).
Those sources do not certify this detector-specific construction or its practical
complexity. The explicit constants, caps, contrast and tail identities above must
be checked on the declared instrument.
