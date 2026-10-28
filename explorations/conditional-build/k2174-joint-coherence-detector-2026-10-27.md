---
title: "K2174 Joint-coherence optimizer and global energy certificate"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed positive free-field model and binary diagonal effects with reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2174_joint_coherence_detector_probe.py
---

# K2174 Joint-coherence optimizer and global energy certificate

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
result: K2174 joint-coherence interiority, unique fixed-squeeze optimizer and exact global energy bracket
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

Both reported outcomes must be optimized together. Whenever the fixed mass and mean
admit a uniformly interior effect, the weighted joint coherence has a UNIQUE maximizer,
and EVERY occupation effect lies strictly between0 and1. At positive contrast such
an optimizer cannot have an eventually constant tail. This is a hypothesis-qualified
infinite-sequence theorem; maximal-contrast boundary effects are not covered.

For the fixed N=1/3, exact Delta=1/2 fixture, every global field-energy optimizer
has interior probability and satisfies those conclusions. Fixed-squeeze uniqueness
does NOT prove uniqueness of the full energy optimizer. The optimal infinite profile
and the exact optimum remain OPEN. A new tangent dual retains both outcomes and sums
its entire occupation tail exactly. Its rational squeeze cover and feasible witness give

    0.75913 < E_min(Delta=1/2) < 0.83121.             (0)

The lower certificate is0.759130025419804457. The upper witness is enclosed between
0.831204005195033234 and0.831204005195033235. This replaces K2172's0.5498–0.84168
bracket at the SAME exact contrast, not a threshold-uniform or general-channel bound.

The cost remains VACUUM OUTPUT FIELD ENERGY in the supplied positive scalar Fock
model, positive-root binary diagonal Kraus and one real squeeze per reported outcome.
Apparatus, clock, preparation, switching and reset costs are excluded. SC-META-53
remains UNCERTAIN; LT-SM8/LT-GR6b, source/ledger0.263/canon and GU physical quotient
claims do not move. Layer0 is this supplied positive free-field model, not source
Cl77 geometry. No novelty or external acceptance is asserted.

## 1. The joint infinite-sequence problem

Let p_n=(1−z)z^n, z=N/(N+1), x_n=p_n e_n, y_n=p_n−x_n,
w=sum x_n and M=sum n x_n=N(w+Delta). For fixed s1,s0>0 maximize

    J(x)=s1 T(x)+s0 T(p−x),
    T(x)=sum_(n>=0)(n+1)sqrt(x_n x_(n+1)),           (1)

over0<=x<=p with the stated w,M. Existence follows by product compactness and
summable domination: the constraints are dominated by p,np and edges by
(n+1)sqrt(p_n p_(n+1)). Thus both moments and J are continuous.

Assume a feasible reference v has epsilon p_n<=v_n<=(1−epsilon)p_n for some
epsilon>0. If a candidate x has a zero coordinate but positive mass, the connected
integer chain has an edge between zero and positive entries. Mixing toward v by t
creates on that edge a positive c sqrt(t)+O(t) coherence gain. Concavity bounds the
loss on all remaining edges below by t times their finite summed difference.
Their total loss is O(t); the complementary coherence also satisfies that bound.
Hence x cannot maximize J. Apply the same argument to p−x, whose mass1−w is positive,
to exclude saturated coordinates. Every maximizer is strictly interior coordinatewise.
It need not have a UNIFORM interior margin.

If two maximizers existed, concavity at their midpoint would be equality on every
positive click edge. Equality of the geometric mean forces the adjacent pairs to
be proportional. Connectedness implies x'=a x on the whole chain; their identical
positive mass forces a=1. This proves unique fixed-squeeze, fixed-moment maximization.
No assertion about joint optimization over squeezes follows from this alone.

## 2. Euler recurrence, tail obstruction and a constructive descent

Finite supported variations preserving mass and mean are legitimate at a coordinatewise
interior optimizer. Their annihilator consists of affine sequences, so

    G_n=lambda+mu n,
    G_n=1/2{s1[n sqrt(x_(n−1)/x_n)+(n+1)sqrt(x_(n+1)/x_n)]
            −s0[n sqrt(y_(n−1)/y_n)+(n+1)sqrt(y_(n+1)/y_n)]}. (2)

Omit the previous term at n=0. This is a necessary equation; we do not claim a general
infinite-dimensional multiplier sufficiency theorem.

Suppose e_n=c∈(0,1) for n>=K. For n>=K+1, G is affine with
lambda=(s1−s0)sqrt(z)/2 and mu=(s1−s0)(1/sqrt(z)+sqrt(z))/2.
At K>=1, stationarity forces

    s1[sqrt(e_(K−1)/c)−1]
      −s0[sqrt((1−e_(K−1))/(1−c))−1]=0.            (3)

The left side is strictly increasing in e_(K−1), with unique zero c. Induction
propagates c backward; the entire effect is constant and Delta=0. Thus positive
contrast rules out an eventual constant tail under the interior-reference hypothesis.
Terminal zero/one tails are already excluded by interiority.

This proof releases an explicit improving direction for any fully interior eventual-
constant reference at positive contrast. Choose its TRUE last transition K, so
e_(K−1)≠c. Then d=G_K−2G_(K+1)+G_(K+2) is K/(2sqrt(z)) times(3), hence nonzero.
Perturb x at K,K+1,K+2 by epsilon sign(d)*(1,−2,1). Both moments stay fixed; small
epsilon is feasible and J increases by epsilon|d|+O(epsilon²). At the old positive
squeeze pair field energy decreases. Such references can certify upper bounds and
duals but can never be exact positive-contrast optimizers.

## 3. Every global fixture optimum lies in the theorem's interior

K2172 proves exact feasibility1/8<=w<=1/2 at Delta=1/2. For each interior w choose

    0<delta<min(1,8w−1,(8−16w)/7),
    x0=(8w−1−delta)/12,
    x1=(16w+1+7delta)/48,
    xn=(1−delta)pn (n>=2).                        (4)

Mass and mean are exactly w,(w+1/2)/3, with a uniform positive distance from both
caps in effect coordinates. Thus the preceding theorem applies to every interior w.

At w=1/8 the unique feasible profile has x0=0,x1=1/16,xn=pn for n>=2. Perturb
(delta x0,delta x1)=(2epsilon,epsilon); the exact-contrast constraint3M−w=1/2
is preserved and w increases. The new click edge gains sqrt(2x1)sqrt(epsilon)
while other changes are O(epsilon). At w=1/2, the profile is x0=1/4,xn=pn for
n>=1. Use(−2epsilon,−epsilon); it creates a complement edge of order sqrt(epsilon)
and decreases w. Retaining the old positive squeezes yields strict energy descent
at both endpoints, including their O(epsilon) changes of linear moment terms.

Global minimizers exist: compact effects with fixed contrast and uniform squeeze
bounds below make the continuous energy attain its minimum. Endpoints are not
minimizers, so every global optimum has interior w, every e_n∈(0,1), and a tail
that never becomes constant. This fixture conclusion does not extend to maximal
contrast or all Delta without proving the corresponding interior assumptions.

## 4. An exact dual for BOTH coherences

Choose any fully interior reference v with eventual effect tail c. Put
alpha_n=sqrt(v_(n+1)/v_n), beta_n=sqrt((p_(n+1)−v_(n+1))/(p_n−v_n)). The edge inequality

    sqrt(a b)<=1/2(alpha a+b/alpha)

has residual( sqrt(alpha a)−sqrt(b/alpha) )²/2. Summing both outcomes gives

    J(x)<=D1+sum G_n x_n,
    D1=(s0/2)sum(n+1)[beta_n p_n+p_(n+1)/beta_n].   (5)

G is(2) evaluated at v. Equality holds at v. Both sums converge, since G=O(n).
For any real lambda,mu, fixed moments therefore give the weak dual

    J<=D1+lambda w+mu M+sum pn max(G_n−lambda−mu n,0). (6)

No infinite strong-duality assumption is used. If v_n=c p_n for n>=K, edges n>=K
have alpha=beta=sqrt(z); their exact D1 tail is
s0 sqrt(z) z^K(K+1+N). Gradient indices n>=K+1 are affine. These different tail
starting indices matter.

For rational a,b and an integer L, the exact positive-part geometric sum is

    S_L(a,b)=sum_(n>=L)pn max(a+bn,0).

If b>0, put l=max(L,floor(−a/b)+1); S=z^l[a+b(l+N)]. If b=0, S=z^L max(a,0).
If b<0, put h=ceil(−a/b)−1; S=0 if h<L, otherwise
z^L[a+b(L+N)]−z^(h+1)[a+b(h+1+N)]. Integer-root equality contributes zero and is
handled by these strict cutoffs. The dual retains every occupation.

## 5. Global squeeze coverage and exact energy bracket

The fixture energy at arbitrary positive squeezes is

    E=(M+w/2)A(s1)+(N−M+(1−w)/2)A(s0)
       −C J+35/18,
    A(s)=41s²/6+3/(2s²), C=40/3.                  (7)

For each branch, its minimizing squeeze solves A'(s)=C T/(M+w/2), lying between0
and C because T<=sqrt(M(M+w))<M+w/2. A''>0,
A'(2/3)<0 and A'(113/100)>C. Thus every relevant branch optimum is in[2/3,113/100].
Both branches have positive mass in this fixture.

For exact contrast3M−w=1/2 define h_n=(n+1/2)(A(s1)−A(s0))−C G_n. Any real eta gives

    E >= (5/6)A(s0)+35/18−C D1+eta/2
          +sum pn min(h_n−eta(3n−1),0).           (8)

The finite terms use outward rational square roots. The affine tail is summed
exactly by S. Four explicit rational eta candidates taken from reference gradients
are tested, keeping the strongest lower bound; no numerical optimizer certifies(8).

The proof covers the ENTIRE square of squeeze values, not just grid nodes. Partition
each axis into48 equal intervals, step139/14400; evaluate(8) at all2304 rational
midpoints. Let x* and s* attain the global minimum. At its fixed x*, energy is
stationary in both squeezes, and A''<=2843/48 on the whole square. The sum of branch
radii is N+1/2=5/6. Taylor's theorem bounds the energy increase from s* to the midpoint
of its box by

    correction=(2843/48)(5/6)step²/8.             (9)

A midpoint weak-dual lower value is below the minimum energy at that midpoint,
which is below the energy of x* at that midpoint. Subtract(9) and minimize over all
boxes. This proves a global lower bound; continuity and the uniform remainder,
not sampling, justify transfer between nodes.

The feasible reference for the upper witness has K=9, eventual e=4999999/5000000,
with e1,...,e8 respectively

    .68761789,.93465392,.98833672,.99800536,
    .99966432,.99994399,.99999071,.99999847.

All decimals are exact rationals. Choose x0 from3M−w=1/2, preserving the full tail,
and s1=105488613/10^8,s0=86390048/10^8. Exact feasibility and outward energy
arithmetic prove the upper bound in(0). Floating optimization suggested this witness;
only its rational verification is evidence. The earlier theorem proves it is not
an exact optimizer. The lower bound is global, but is not claimed sharp. As an executable consumer of
the tail obstruction, the probe changes x9,x10,x11 by10^(-14)(−1,2,−1). Exact
mass, mean and caps are preserved, and its fixed-squeeze energy change lies between
−0.000000000001500110 and−0.000000000001500109. Thus the published witness really
has a certified further descent, not merely a formal nonattainment label.

## Verification and continuation

Run `python tests/channel-swings/k2174_joint_coherence_detector_probe.py` in the
repository SymPy environment; `--write` regenerates the report. Exact symbolic/finite
controls check moment identities, edge gradients, AM-GM, geometric tails, endpoint
directions, the production tangent touching both coherences, and squeeze coverage.
Six genuine altered inputs/equations fail specific checks after a green baseline;
one corrupts the actual production dual. The separate2304-box rational certificate
and all-occupation witness establish(0). Written universal proofs receive independent
review; finite checks alone do not establish optimizer structure. Dependencies and
probe bytes are pinned. No proof-assistant, external-expert or remote-CI claim.

The next substantive problem is matching dual/primal bounds for the NONconstant
infinite optimum, or proving further uniqueness/shape beyond the fixed-squeeze
problem. Constant-tail references remain useful approximations with an explicit
descent, never exact optimizers. Compare a stable autonomous physical-smear controller
with preparation/reset costs; field-output energy alone does not supply that account.
