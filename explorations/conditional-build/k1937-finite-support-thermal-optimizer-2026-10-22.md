---
title: "K1937: Sharp finite occupied-support thermal return"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1937_finite_support_thermal_optimizer.py
  - tests/channel-swings/k1937_finite_support_thermal_optimizer_probe.py
---

# K1937: Sharp finite occupied-support thermal return

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
result: exact finite occupied-support minimum, attaining full channels and dynamic programming
carrier: four-state system, four-level Gibbs bath and padded nondegenerate finite catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input half trace norm ON=independent_initial_registers
real_structure: complex adjoint with catalyst energy pinching
grading: additive energy shells; no particle chirality
action_owner: repository-construction -- exact conserving joint unitary
target: all-input marginal catalyst return at fixed occupied-energy count MAP-TYPE=intertwiner
```

## 1. What is now optimized

Use precisely [K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md)'s
four-state extreme Schur target, four-level bath with weights t^b/Z,
0<t<1, and additive energy conservation. All registers are initially
independent; the system Hamiltonian is diagonal. Let N be the number of
strictly positive diagonal energy populations of the catalyst after energy
pinching. Allow arbitrary finite nondegenerate catalyst spectra and initial
coherence with this N. Unoccupied levels are free to be supplied.

The exact minimum of worst-input marginal half trace distance is

    R_N(t) = 1 / [2 max_(gaps,root) S(gaps,root)],              (1)
    S = 1 + sum_left_prefixes product q_d
          + sum_right_prefixes product p_d,
    q_d=L_d/(1+H_d), p_d=H_d/(1+L_d),
    L_d=(1+...+t^(3-d))/Z, H_d=t^d L_d,
    d in{1,2,3}, adjacent gaps d+e>=4.

The maximum ranges over N-site paths and all their roots. Every such rooted
path has an attaining full-channel construction. This fills the attainment
gap expressly left open in K1935 section3. A specified *uncompleted*
physical spectrum can lack necessary empty states; (1) does not assert
attainment on that smaller fixed Hilbert space.

This is occupied-energy support, not catalyst Hilbert dimension, density
matrix rank before pinching, or mean-energy budget. The construction uses
at most 3N+4 catalyst levels. No approximate-channel, product-return,
repeatability, local-control or total-work optimum is asserted.

## 2. Lower certificate and why disconnected spectra cannot help

K1935 sections2-3 prove physical shell rank doubling, at most two occupied
inputs per four-dimensional shell, resonance path gaps1/2/3 with adjacent
sum at least4, and a substochastic orientation matrix. For each component,
its inverse visit reward is no greater than that of an outward-rooted path.
The fixed-input rho12=(|1><1|+|2><2|)/2 therefore yields the lower bound
1/(2 max S). That proof permits arbitrary unoccupied spectral gaps as a
relaxation, and energy pinching contracts worst-input return at the same
conserving unitary. It therefore applies to coherent preparations too.

For disconnected resonance components, the same inverse-visit inequality
uses the maximum component reward, not their sum. Extending a path by an
allowed terminal gap adds a strictly positive prefix term. Thus maximal
reward strictly increases with N; no splitting into smaller components
improves the N-site bound. A nonresonant additional support level cannot
supply an uncounted larger component. This establishes the global lower
bound in(1), not just optimality within a protocol family.

## 3. Matching weights and actual unitary

Choose a path and root r. Set x_r=1, propagate left by
x_child=q_d x_parent and right by x_child=p_d x_parent; normalize
s_i=x_i/S. Each edge's input closer to r is heavier on every shared shell:
leftwards L_d s_parent=(1+H_d)s_child, and rightwards
H_d s_parent=(1+L_d)s_child. These imply the required strict comparison
with H_d s_child or L_d s_child, respectively.

Put the occupied levels at3,3+d1,... in units Delta and include the full
ladder from0 through the largest occupied level plus3. Every shell containing
an occupied input then has all four positions. Triple occupied shells are
excluded by the gap rule.

Use v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2 and
W=[[1,1],[1,-1]]/sqrt2. In each shared shell, send the heavy input to
Wv_j in the two occupied-support positions, its own position first. Send
the light input to Wv_j in the two unoccupied positions. For a singleton
shell, use its occupied position first and any empty position second.
Complete each pair with its orthogonal companion on an unused input column;
leave unused subspaces unitary. This defines four FULL shell unitaries U_j.
Their controlled direct sum on the system commutes with total energy.

Each occupied column has inner products <v_k,v_j>; orthogonal input copies
remain orthogonal. Hence every system matrix unit, including complex phases,
and therefore every entangled system/reference input has exactly the target
Schur channel. Full unitaries on unused states matter: this is not merely
an isometry with an unaccounted pure ancilla.

Tracing the bath kills coherence between distinct output catalyst levels
inside a shell because their bath labels differ. Initial shell mixtures
produce no between-shell coherences. Tracing the controlled system removes
input coherences from the catalyst marginal. For a basis input, the squared
first coordinate of Wv_j is c_j=(1/2,1/2,1,1/2). Therefore

    a_r=c s_r,
    a_i=[1+k_i(1-2c)]s_i,  i != r,
    k_i=H_d for a left child, L_d for a right child.           (2)

For c in[1/2,1], every occupied population has a nonnegative deficit, so
all probability outside support contributes the same total excess. Write
D=sum_(i != r) k_i s_i. The exact return is

    R(c)=(1-c)s_r+(2c-1)D.                                 (3)

## 4. The missing all-input inequality

For a left arm starting with gap d, its leakage divided by the parent
weight obeys the recursion f_d=q_d(H_d+f_tail). Its universal bound is
f_d<=L_d/2. Indeed if the next gap is e, induction gives

    q_d(H_d+L_e/2) <= L_d/2
    iff H_d+L_e<=1.

The latter holds because the two bath-label intervals are disjoint when
d+e>=4. Terminal f_tail=0 satisfies the same bound. For a right arm,
g_d=p_d(L_d+g_tail)<=H_d/2 by the same disjointness inequality.
At the root, left first-gap a and right first-gap b obey L_a+H_b<=1.
An absent arm contributes0. Consequently D<=s_r/2 for every finite path.
Equation(3) gives R(c)<=s_r/2, with equality at c=1/2. By convexity and
the controlled-system trace, this holds for ALL system inputs. Thus the
lower bound is attained at s_r/2=1/(2S). A rho12-only construction would
not suffice; (2)-(3) are the essential all-input proof.

## 5. Finite dynamic program and resource consumers

Let F_n(d),G_n(d) be maximal arm prefix sums with n edges and first gap d.
For n=1 they are q_d,p_d. For n>1,

    F_n(d)=q_d[1+max_(e+d>=4) F_(n-1)(e)],
    G_n(d)=p_d[1+max_(e+d>=4) G_(n-1)(e)].                   (4)

For each split a+b=N-1, maximize 1+F_a(d)+G_b(e), imposing d+e>=4
when both arms are nonempty. A missing arm contributes0. Backtracking
produces the actual gaps and the weights in section3. This finite recursion
is exact for every real0<t<1. For rational t all arithmetic and comparisons
are rational. A fixed N uses O(N) arithmetic recurrence steps. Parent pointers would
use O(N) storage; this small implementation stores full gap tuples, with
additional quadratic copying/storage. Computing all budgets through N uses
O(N^2) arithmetic steps, with integer bit complexity additional. Exhaustive enumeration is a separate
verification, not the production optimizer.

At t=1/2 the minimum occupied supports for return at most1/4,1/5,17/100,
and161/1000 are respectively3,5,9,15. The JSON records exact weights and
optimal paths for representative temperatures and N<=8, and checks strict
decrease through N=20. These finite observations are not a theorem that
all optimizers always use only gap2. K1935's warm N=2 adjacent-gap improvement
is preserved by the same recurrence.

There is also a general sufficient logarithmic support scaling. Choose all
gaps2 with a edges left and b right, a+b=N-1. Writing q=q2,p=p2 gives

    S = S_inf - q^(a+1)/(1-q) - p^(b+1)/(1-p),
    S_inf=1+1/(2t^2)+t^2/2.

For any epsilon>0 above the global infimum t^2/(1+t^2)^2, increasing
both a,b makes (1) meet that tolerance. For fixed t, a,b=O(log(1/epsilon))
suffice. This is a constructive upper scaling, not a sharp dimension or
energy tradeoff. The padded ladder has at most3N+4 levels and mean energy
at most3N Delta. Minimal support inversion is now a finite exact computation;
optimal preparation under a separate mean-energy constraint remains open.

## 6. Hostile review, reproducibility and scope

Strongest overclaim rejected: fixed occupied support is neither a fixed
Hilbert spectrum nor state rank; missing empty shell positions may prevent
attainment. The countercontrol with adjacent gaps1+2 violates rank doubling
and is rejected. Another critical seam is the ALL-input return: the proof
bounds c=1 as well as rho12, with full complex Gram matrices explicitly
checked. The program separately enumerates every orientation and root on
small paths to challenge the inherited outward-visit bound, then compares
its independent maximum against the dynamic program.

Run both frontmatter scripts with Python3/SymPy1.14.0; producer --write
regenerates JSON. Finite controls are exact; analytic arguments above and
K1935 carry the universal quantifiers. Real denominator, complex phase and
triple-support faults are caught only after a green baseline. Report/pin
checks are reporting consistency, not proof. This is internal analytic review
and independently written algorithms, not independent expert or formal review.

Known context: [Ng et al.](https://arxiv.org/abs/1405.3039) study catalytic
resource restrictions; no novelty claim is made for the target-specific
construction. SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, AC-F1 and
source/physics/canon statuses are unchanged. No GU or observed-particle
identification is supplied. Approximate shell rank, fixed-energy optimality,
degenerate spectra and physical reuse remain separate new constructions.
