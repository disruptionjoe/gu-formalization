---
title: "K2172 Mean-constrained fidelity and detector energy certificates"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed positive free-field model and binary diagonal effects with reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2172_mean_constrained_fidelity_probe.py
---

# K2172 Mean-constrained fidelity and detector energy certificates

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
result: K2172 mean-constrained fidelity dual, exact profile and certified energy bracket
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

The mean constraint strictly improves the previous norm-and-cap fidelity relaxation
at every positive feasible contrast. A two-multiplier weak dual provides rigorous
infinite-tail certificates without a strong-duality assumption. In the fixed fixture
N=1/3 and exact contrast Delta=1/2, the ENTIRE mean-constrained fidelity problem is
solved explicitly for every feasible click probability w. Its optimizer caps every
occupation n>=2 and adjusts the first two entries.

That fidelity optimizer is NOT the field-energy optimizer at any interior w: a
mass- and mean-preserving perturbation creates a beneficial square-root term in the
other outcome. This supplies both a structural counterexample and a feasible energy
witness. Combining the exact fidelity with a256-bin rigorous probability cover gives

    0.5498 < E_min(Delta=1/2) < 0.84168.                 (0)

The stored lower certificate is0.549840539735118445; the rational witness has energy
between0.841677852979609798 and0.841677852979609799. Bounds cover infinite occupations;
the256 bins partition click probability, not occupation. The actual energy optimum
and optimum effect remain OPEN. This exact-contrast bracket is not a threshold
bound for every Delta>=1/2. K2170's weaker threshold-uniform result remains valid.

The model and cost are unchanged: supplied positive scalar Fock vacuum and
photon-added signal, binary diagonal effects, positive-root Kraus, one real squeeze
per reported outcome; VACUUM OUTPUT FIELD ENERGY only. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b/source/ledger/canon do not move. No physical GU quotient, general-channel
optimum, apparatus, clock, preparation, switching or reset cost is supplied. Layer0
is this toy free-field instrument, not the source Cl77 geometry. No novelty claim.

## 1. Mean-constrained fidelity and a usable weak dual

Let p_n=(1-z)z^n, z=N/(N+1), x_n=p_n e_n, w=sum x_n,
M=sum n x_n=N(w+Delta), r²=R=M/(M+w), g_n=sqrt(1-R)r^n.
For positive contrast, R>z. Define

    H_mean(w,M)=max sum g_n sqrt(x_n)
      over 0<=x_n<=p_n, sum x_n=w, sum n x_n=M.         (1)

This is a concave maximization over convex constraints. The feasible set is compact
in product topology: p_n and n p_n are summable dominating sequences, preserving
both constraints under limits. The overlap is continuous by its uniformly summable
geometric tail. A nonempty feasible set therefore has a unique optimizer, by strict
concavity in the positive coefficients g_n.

For ANY real lambda,nu put t_n=lambda+nu n and

    phi_n(t)=g_n sqrt(p_n)-t p_n,  t<=g_n/(2sqrt(p_n)),
             g_n²/(4t),           t>g_n/(2sqrt(p_n)).

Pointwise maximization of g_n a-t a² on0<=a<=sqrt(p_n) proves

    H_mean <= lambda w+nu M+sum phi_n(t_n).             (2)

The series converges since |t_n|p_n and g_n sqrt(p_n) are summable. No infinite-
dimensional strong duality or finite multiplier attainment is needed. If the
pointwise optimizer

    x_n=min(p_n,g_n²/(4t_n²)) for t_n>0,
    x_n=p_n for t_n<=0

also has the required mass and mean, it attains(2) and is the unique solution.
The uncapped indices satisfy lambda+nu n>c(r/sqrt(z))^n. Linear minus strictly
convex exponential is strictly concave, so this set of integer indices is one
finite interval, possibly empty. Initial AND terminal caps can occur; tail-only
clipping cannot be assumed generally. Finite multipliers need not describe boundary
solutions with zero entries.

For an executable tail bound, with integer K>=0 and R fixed,

    sum_(n>=K) phi_n(t_n)
      <= sqrt((1-R)(1-z)) (sqrt(Rz))^K/(1-sqrt(Rz))
        +z^K [max(0,-lambda-nu K)+max(0,-nu)N].          (3)

Use phi<=g sqrt(p)+(-t)_+p and the exact geometric zeroth and first tail moments.
Outward rational square roots certify(3); no numerical optimizer is trusted.

## 2. The old capped optimizer always has the wrong mean

K2170 maximized the same overlap using only mass and caps. Its unique optimizer is
xcap_n=min(t²g_n²,p_n). Under the probability Q_n=g_n², define
h_n=xcap_n/(wQ_n). Then E_Q h=1. Since R>z, h is nonincreasing, and strictly
decreasing on an infinite capped tail. All Q_n are positive, so

    Cov_Q(n,h)=1/2 sum_ij Q_i Q_j(i-j)(h_i-h_j)<0.

The series is absolutely convergent because h is bounded and Q has finite mean.
Therefore sum n xcap_n=w E_Q(nh)<w E_Q n=M. The cap-only optimizer is never
mean-feasible at positive contrast. Compact attainment in(1) and uniqueness of
xcap imply the strict improvement H_mean<H_cap, for every feasible positive
contrast, including feasible boundary effects. This is a fidelity result; it does
not claim equality in the shift-gap energy bound.

## 3. Exact profile for the full Delta=1/2 fixture

Take N=1/3,z=1/4,Delta=1/2. The exact tail inequality M-w<=N z=1/12 and M<=N
give1/8<=w<=1/2. Every value is feasible via

    R=(2w+1)/(8w+1),
    x0=(8w-1)/12, x1=(16w+1)/48, x_n=p_n (n>=2).       (4)

The tail mass is1/16 and mean7/48, so mass and mean are exactly right. Equivalently
e0=(8w-1)/9, e1=(16w+1)/9, e_n=1 for n>=2.

For1/8<w<1/2 choose lambda=g0/(2sqrt(x0)), t1=g1/(2sqrt(x1)), nu=t1-lambda.
The first two entries are uncapped pointwise maximizers. Their slope is negative:

    x1-Rx0=(64w²+5)/(48(8w+1))>0.

It suffices to check2t1-lambda<=g2/(2sqrt(p2)). Then t_n decreases while the cap
threshold g_n/(2sqrt(p_n)) increases, proving every n>=2 is capped. Divide this
inequality by g0/2. On1/8<w<=1/5, R/x1<=10, x0<=1/20, R>=7/13, giving

    2sqrt(R/x1)-1/sqrt(x0)<=2sqrt(10)-sqrt(20)<2,
    R/sqrt(p2)>=56/(13sqrt(3))>2.

On1/5<=w<1/2, Rx1-p2=(128w²-5)/(192(8w+1))>0. Thus t1<=g2/(2sqrt(p2)) and
2t1-lambda<t1. The exact dual certificate proves(4) optimal. At w=1/8 the
moment inequality uniquely forces x0=0,x1=1/16 and the capped tail, so no finite
multiplier representation is asserted. At w=1/2, M=N forces x_n=p_n for n>=1,
and mass fixes x0=1/4. The same formula holds at both endpoints.

Consequently the exact optimum for every feasible w is

    H_mean=sqrt((1-R)x0)+sqrt((1-R)R x1)
      +sqrt((1-R)(1-z)) (Rz)/(1-sqrt(Rz)).               (5)

No occupation truncation or numerical optimization enters this solution.

## 4. Compose the fidelity into a certified energy lower bound

Reuse K2170's independently reviewed shift gap. With
T=sum(n+1)sqrt(x_n x_(n+1)), eta=sqrt(M(M+w))-T,

    eta >= (1-r)²/(2r) [w-H_mean²].                    (6)

Reuse K2168's convex moment energy L_Delta(w) and K2170's squeeze lower bound q>2/3
in this fixture (C=40/3). Then every detector at exact contrast1/2 obeys

    E >= L_(1/2)(w)+C(2/3)(1-r)²/(2r)[w-H_mean²].      (7)

For each of256 adjacent rational bins[a,b] covering[1/8,1/2], compute an outward
interval for(5) using R in[R(b),R(a)] and the affine x0,x1 intervals. If Hupper
is its nonnegative upper bound, w-H²>=max(0,a-Hupper²). The prefactor is decreasing
in r, so an upper enclosure of sqrt(R(a)) gives a lower prefactor. A supporting
tangent to K2168's globally convex L at the bin midpoint gives a rigorous lower
value throughout the bin. Add the bounds and take the minimum over the complete
cover. All arithmetic uses Fraction and integer-square-root outward enclosures;
rounding always weakens the certificate. JSON records every endpoint and lower
value. This proves(0)'s lower bound, not the sharpness of(6) or the actual optimum.

## 5. Fidelity optimality does not minimize energy: an explicit descent direction

At any interior w, perturb the exact fidelity profile by

    x0 -> x0-epsilon, x1 -> x1+2epsilon,
    x2 -> p2-epsilon, all other entries unchanged.     (8)

Both mass and mean are unchanged, and sufficiently small positive epsilon is
feasible since x0>0 and x1<p1. The click T changes by O(epsilon), because all its
relevant entries are positive. For the complement y=p-x, the new n=1 edge adds

    2sqrt((y1-2epsilon)epsilon)
      =2sqrt(y1)sqrt(epsilon)+O(epsilon^(3/2)).

Its n=0 edge changes only O(epsilon). At ANY fixed positive squeeze pair the
energy therefore drops by2C s0 sqrt(y1)sqrt(epsilon)+O(epsilon). Retaining the
old optimal squeeze pair proves that optimized field energy strictly drops too.
Thus(4) is NOT its optimizer at any interior w. The complement improvement is why
optimizing only the informative branch's overlap cannot solve the full problem.

The same mechanism rules out a larger family of energy ansatzes. Suppose K>=2,
x_n=p_n for all n>=K, y_(K-1)>0, and two earlier coordinates i<j<K are strictly
interior (0<x_i<p_i,0<x_j<p_j). Set

    delta x_K=-epsilon,
    delta x_i=-(K-j)epsilon/(j-i),
    delta x_j=(K-i)epsilon/(j-i).

Mass and mean stay fixed. All existing changed edges vary by O(epsilon), while
the new complementary boundary edge is K sqrt(y_(K-1))sqrt(epsilon)+O(epsilon^(3/2)).
Thus energy strictly decreases for small epsilon at fixed positive squeezes,
and hence after optimizing them. Reverse the signs for a terminal zero tail,
assuming x_(K-1)>0, to gain a click edge instead. This excludes such terminal
saturated/zero tails with two interior coordinates; it does NOT prove every optimal
entry is interior, or exclude constant tails strictly between0 and1. The explicit
profile(4) is the K=2,i=0,j=1 instance.

For a reproducible feasible upper witness choose

    w=311154/1000000, epsilon=2666/1000000,
    click squeeze=1055411/1000000,
    no-click squeeze=860107/1000000.

Use(8), with p_n tails intact. The exact adjacent moments are

    T1=sqrt(x0 x1)+2sqrt(x1 x2)+3sqrt(x2 p3)+13/384,
    T0=sqrt((p0-x0)(p1-x1))+2sqrt((p1-x1)(p2-x2)).

Substitute into the exact branch energy
F_s=(M+w/2)(41s²/6+3/(2s²))-(40/3)s T+(25/3)M-(5/6)w,
and its complementary branch. Outward rational roots prove the upper endpoint in(0).
The rational witness was suggested by floating optimization; only its exact
feasibility and interval energy are evidence. At the SAME w and squeezes, epsilon0
has E>1.0034, while this perturbation has E<0.84168. No optimality is inferred.

## Reproducibility, review and continuation

Run `python tests/channel-swings/k2172_mean_constrained_fidelity_probe.py` in the
repository SymPy environment; `--write` regenerates evidence. Exact symbolic controls
check mass/mean, dual stationarity, cap inequalities, geometric tails, perturbation
and energy identity; actual altered-input/equation faults must fail after a green
baseline. The256-bin interval cover and rational feasible witness are separate
certificate evidence. Independent review checks the infinite-dimensional compactness,
strict cap gap, exact profile and square-root descent proof; finite tests alone do
not establish those universal claims.

Next compare full two-outcome T optimization at fixed moments, certified conic/squeeze
search and stable autonomous physical-smear control. Do not requeue norm-only or
mean-fidelity optimization as the actual energy optimum. The new descent direction
specifies a useful unsaturated-tail family to explore. K2162 already owns general
conic approximation, weak-budget and saturation results remain intact, and K2170's
threshold-uniform bound remains distinct. No arbitrary-channel, total-work,
external-expert or proof-assistant certification is claimed.
