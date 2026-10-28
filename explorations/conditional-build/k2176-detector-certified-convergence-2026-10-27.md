---
title: "K2176 Complete rational certification of infinite detector energy"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, exact contrast one half and contrast magnitude at least one half, vacuum output field energy only
scripts:
  - tests/channel-swings/k2176_detector_certified_convergence_probe.py
---

# K2176 Complete rational certification of infinite detector energy

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
result: K2176 attained fixed-squeeze dual and complete rational certificate class
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For the fixed N=1/3, exact contrast Delta=1/2 model of K2174, EVERY positive
fixed squeeze pair has a UNIQUE optimal infinite effect even when outcome probability
w varies. Its all-occupation tangent dual attains the minimum. Finite rational
references with eventual-constant effects form a COMPLETE certificate class:
their lower bounds can approach the actual fixed-squeeze minimum arbitrarily closely,
despite no eventual-constant effect being an optimizer. This is an existence and
convergence result, not a proved effective rate or uniqueness of the jointly optimized
squeeze pair.

A released exact adaptive certificate covers the entire squeeze square with61
rational rectangles and improves the global bracket to

    0.83103 < E_min(exact Delta=1/2) < 0.831205.   (0)

The upper witness is reused from K2174, not a new optimizer. All occupation tails
are retained exactly. This cost is VACUUM OUTPUT FIELD ENERGY for the supplied
positive scalar Fock model, positive square-root binary diagonal Kraus and one
real squeeze per reported outcome. Apparatus, clock, preparation, switching and
reset are excluded. The threshold extension in Section6 is limited to contrast magnitude at least1/2;
no arbitrary-channel or GU physical-state claim follows. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b, source, ledger0.263
and canon remain unchanged. No novelty or external acceptance claim.

## 1. Unique fixed-squeeze minimizer with variable probability

Use p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n−x_n, q_n=3n−1,
0<=x<=p, and sum q_n x_n=1/2. Write

    T(x)=sum(n+1)sqrt(x_n x_(n+1)),
    E(x;s1,s0)=sum(n+1/2)x_n A(s1)
       +sum(n+1/2)y_n A(s0)−C[s1T(x)+s0T(y)]+35/18,
    A(s)=41s²/6+3/(2s²), C=40/3.                (1)

Fix s1,s0>0. Product compactness and summable geometric domination give existence.
K2174's endpoint sqrt-epsilon descents apply at these fixed squeezes: the positive
coherence gain dominates the O(epsilon) moment terms. Therefore w is interior in
[1/8,1/2]. The uniformly interior same-moment reference constructed there excludes
every zero or saturated coordinate. It does NOT give the optimizer a uniform
margin from its caps.

Suppose x,x' both minimize. Concavity of each positive geometric-mean term forces
equality on every edge in both coherences. The connected chain gives x'=a x and
y'=b y for positive constants a,b. Hence(a−b)e_n=1−b for all n. Positive contrast
forbids a constant effect, so a=b=1. This proves uniqueness without fixing w.

Define g1_n=partial T(x)/partial x_n, g0_n=partial T(y)/partial y_n and

    G_n=s1g1_n−s0g0_n,
    h_n=(n+1/2)[A(s1)−A(s0)]−C G_n.

Finite variations d_j=1,d_0=q_j (j>=1) preserve contrast and are feasible with
both signs at the interior minimizer. Stationarity yields h_j+q_j h0=0, or

    h_n=eta q_n, eta=−h0.                       (2)

No infinite-dimensional multiplier theorem is assumed.

## 2. Absolute convergence and attained all-occupation dual

At each n, at least one of x_n,y_n is>=p_n/2. Its gradient is bounded by

    B_n=[n sqrt(2/z)+(n+1)sqrt(2z)]/2, z=1/4.

This follows from neighboring branch coordinates<=p_(n±1). Since G_n is affine
by(2), the other positive branch gradient is also O(n): e.g. if g1<=B then
g0=(s1g1−G)/s0<=(s1B+|G|)/s0, and symmetrically for g1. Thus BOTH gradients
are bounded by one constant times n+1. All p-weighted tangent sums converge
absolutely, including the branch tangent constants.

For an interior reference v let alpha_n=sqrt(v_(n+1)/v_n) and
beta_n=sqrt((p_(n+1)−v_(n+1))/(p_n−v_n)). K2174's AM-GM tangent gives

    D0=(1/2)sum(n+1)[beta_n p_n+p_(n+1)/beta_n]. (3)

Here D0 is independent of s0. The weak dual is

    L=(5/6)A(s0)+35/18−C s0 D0+eta/2
       +sum p_n min(h_n−eta q_n,0).              (4)

Use v=x* and eta from(2). Tangent equality holds and every positive-part slack
vanishes. Absolute convergence just proved permits the sums, giving L=E(x*).
Thus the dual attains the fixed-squeeze optimum. No assertion of joint-squeeze
convexity follows from this argument.

## 3. Why finite rational certificates suffice

Keep x* through index K. For n>K replace its effect by e_K*, and correct coordinate
zero by delta_K=sum_(n>K) q_n(v_n−x_n*). Since q0=−1 this preserves exact contrast.
The exact error bound is

    |delta_K|<=sum_(n>K)q_n p_n
              =3(K+1)4^−(K+1).                 (5)

For large K the corrected coordinate zero stays strictly interior. All other
coordinates are interior by construction, with an eventual-constant tail.

For fixed n the reference gradients converge to the true ones. To justify passage
to the whole dual, use the O(n) bounds from Section2 for EACH branch. At junction K,
the previous-neighbor term is inherited and the next ratio is replaced by sqrt(z);
at K+1 both neighbors have the same effect. Thus all junction/tail gradients obey
one uniform O(n) bound for all sufficiently large K. Coordinates0,1 remain bounded
by continuity of the small correction. The tangent constant and positive-part sums
are consequently dominated by a fixed multiple of(n+1)p_n, which is summable.
Dominated convergence proves L(v^K,eta*)→E(x*).

For each finite K, approximate its positive head, tail and eta by rationals, solving
coordinate zero from the exact rational contrast equation. Strict finite-coordinate
interiority persists. Finite-reference energy and dual are continuous; the affine
positive-part geometric tail is continuous even when its integer cutoff changes,
because the entering/leaving term then vanishes. Hence rational references remain
arbitrarily tight. No unknown tail is discarded and no effective convergence rate
is claimed.

This releases a constructive certificate strategy. Every fixed-squeeze point has
an arbitrarily tight rational certificate. Continuity and compactness on a bounded
positive squeeze square permit finite covers at any prescribed error, together with
arbitrarily fine squeeze partitions and the Taylor argument below. This is existence
of certified approximation, not a complexity bound or guarantee for a particular
numerical search algorithm. Rational eventually constant feasible profiles also
approximate the energy from above by the same corrected-tail construction.

## 4. Exact diagnostic for the dual gap

For any feasible x and admissible interior reference, let a_n=h_n−eta q_n. The exact
gap decomposes into nonnegative terms:

    E−L = C/2 sum(n+1){s1[ sqrt(alpha_n x_n)−sqrt(x_(n+1)/alpha_n) ]²
                        +s0[ sqrt(beta_n y_n)−sqrt(y_(n+1)/beta_n) ]²}
          +sum[ max(a_n,0)x_n+max(−a_n,0)y_n ].  (6)

The first term is tangent mismatch; the second is cap slack. This is an equality,
not merely two independent lower bounds. Small gap alone gives no unweighted
profile-distance estimate without an additional coercivity inequality. The probe
checks the actual production formulas on distinct feasible witness/reference
profiles and arbitrary eta, with exact tails and outward rational radicals.

## 5. Released global certificate

K2174 proves every global optimum has both squeezes in[2/3,113/100], positive
branch radii R1=M+w/2,R0=N−M+(1−w)/2 with R1+R0=5/6, and stationarity in squeezes.
On the entire interval A''<=H=2843/48. For a rectangle containing an actual global
optimizer s*, with midpoint c and half-widths r1,r0, Taylor at fixed x* gives

    E(x*,c)<=E*+H(R1 r1²+R0 r0²)/2
            <=E*+H(5/6)max(r1²,r0²)/2.          (7)

A weak-dual lower bound at c minus this correction is therefore a lower bound for
the global optimum IF it lies in that rectangle. Take the minimum over an exact
cover to remove that condition. This does not assert that every pointwise minimized
value has bounded second derivatives.

The certificate uses61 rectangles. Each endpoint is an exact rational on a2^20
unit grid scaled to the squeeze interval. Bounds, total area and pairwise interior
disjointness prove a cover; closed rectangles include their boundaries. Each center
uses its own finite rational positive reference and rational eta, supplied as literal
probe input. AM-GM and exact affine geometric tails yield lower bounds without
assuming the references are optimizing or feasible. Square roots are bounded by
integer-isqrt rational enclosures. A verified feasible K2174 witness supplies the upper
bound; its prior tail descent and nonoptimality remain unchanged.

Numerical least-squares scouting only proposed these inputs. A first direct-effect
SLSQP scout suffered poor tail conditioning and did not produce a useful sharp
certificate; solving fixed-squeeze stationary residuals in log-odds produced the
finite inputs. Neither convergence status nor floating energy enters verification.
The exact JSON report supplies the final lower bound, upper bound and gap.

## 6. Released threshold consumer and outcome relabeling

Every one of the61 stored rational multipliers eta is STRICTLY POSITIVE, checked
exactly. For an effect with signed contrast d=sum q_n x_n>=1/2, the same derivation
of(4) has eta*d in place of eta/2. Thus every center certificate already lower-bounds
ALL such effects. No monotonicity of the exact-d optimum is assumed.

The squeeze range also survives this change of constraint. For each branch,
2sqrt(ab)<=a+b gives T_i<=R_i by summing the weighted neighboring edges. Since
A''>0, A'(2/3)<0 and A'(113/100)>C, a minimizing branch squeeze remains inside
the same interval. The threshold-feasible effects form a product-compact set.
Positive contrast excludes zero and full effects, hence both branch radii are
positive; energy continuity then gives a global threshold optimizer. Its squeezes
are stationary, and R1+R0=5/6 still holds. The SAME61-rectangle Taylor certificate
therefore proves

    0.831032736932633356 < inf_(d>=1/2) E
                         < 0.831204005195033235. (8)

The existing exact-d=1/2 witness supplies the upper bound because it is threshold
feasible. Positivity of the geometric-mean and radical enclosures makes the displayed
bounds strict as in the certified report. Replacing x by p−x and swapping s1,s0
leaves E unchanged and sends d to−d. Consequently the identical bracket applies to
inf_(|d|>=1/2) E. The probe checks this swap symbolically, including both moments.

This does NOT prove that the threshold optimum equals the exact-d optimum, occurs
at its threshold, or that the full frontier is monotone. Fixed-squeeze uniqueness
and rational-reference completeness above remain stated at exact d=1/2; no such
extension is inferred merely from the numerical threshold certificate.

## Verification and next work

The named probe verifies exact rectangle coverage, all61 lower certificates, tail
contrast, shared production dual/gap identity, majority-coordinate bounds and
Taylor factors, exact multiplier signs and outcome-swap symmetry. Ten actual data/formula faults fail after a green baseline.
Written uniqueness, domination and completeness proofs receive separate independent
review; finite controls do not prove these theorems. No proof-assistant, external-expert,
novelty, joint-squeeze uniqueness or remote-CI claim.

The remaining question is structural global squeeze uniqueness, a quantitative
convergence/coercivity rate, or a better physical instrument with explicit autonomous
preparation/reset costs. More decimal refinement alone has lower payoff now that a
complete certificate class and a sub0.000175 global energy gap are available. The
actual nonconstant infinite optimum remains unexpressed; threshold location and
frontier monotonicity remain separate questions.
