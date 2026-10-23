---
title: "K1998: Uniform spacing transfer and a flat-or-linear onset law"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1998_uniform_small_spacing_transfer.py
  - tests/channel-swings/k1998_uniform_small_spacing_transfer_probe.py
---

# K1998: Uniform spacing transfer and a flat-or-linear onset law

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
result: all-fixed-dimension quantitative spacing transfer and eventually fractional-linear optimal return
carrier: fixed extreme four-state channel, four-level Gibbs bath and finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance with upper mean-energy budget ON=independent_initial_registers
real_structure: real spectra/populations and complex conserving unitaries
grading: actual bath resonance components, not source chirality
action_owner: repository-construction -- unchanged exact thermal channel
target: small-positive-spacing approximation rate and physical resource certificate MAP-TYPE=intertwiner
```

## Results

Keep the EXACT thermal problem of
[K1996](k1996-positive-spacing-finite-program-2026-10-23.md). Let
F_d(delta,E,t) be the optimum at positive minimum spacing, physical dimension
at most d>=3, mean energy at most E>=1, and bath ratio0<t<1. Let V_d(E,t)
be the unspaced nondegenerate infimum computed by
[K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md)'s finite
TAGGED program. Coincident tags are not physical levels.

Set c_d=max(0,floor((d-5)/3)). Then

    V_d(E,t) <= F_d(delta,E,t)
      <= V_d(max(1,E-c_d delta),t),
    0<delta<=1/(c_d+1).                                (1)

Let L_d(t) be the maximum absolute slope of the complete finite piecewise-
affine curve V_d. It is finite and exactly computable for rational t from
that finite program. Uniformly for ALL E>=1,

    0<=F_d(delta,E,t)-V_d(E,t)<=L_d(t)c_d delta.          (2)

There is also a structural small-spacing law at EVERY fixed d,E,t. For some
eta>0 and constants ell>=0,kappa,

    F_d(delta,E,t)=V_d(E,t)+ell delta/(1+kappa delta),
    0<delta<eta.                                       (3)

Thus the gap is either identically zero near0, or has a strictly positive
linear leading coefficient. A positive but purely quadratic/higher-order
onset cannot occur in this fixed-budget, one-energy-constraint model.
For rational E,t, the constants can be computed by finite exact enumeration;
the present work does not execute arbitrary-d enumeration or give a universal
coefficient across dimensions. Neither eta nor ell is uniform in E,t,d here.

Combining the existing full equality-face census with offset packing gives
the SHARP leading coefficient for EVERY fixed d>=10 and6/5<E<11/5 at t=1/2:
ell=(3/20)min(E-6/5,11/5-E). A further finite-ray argument proves that the better of those two ten-level
placements is EXACTLY optimal for all sufficiently small positive spacing,
at each fixed d and interior E; the threshold is not evaluated here. The exact d8,E7/5 example has ell=1/18 and kappa=5/6.
These are independent conditional mathematical results, not GU physics.

## 1. Physical tag separation with controlled energy cost

K1968 already proves finite completeness of the canonical tagged patterns,
shell-rank sufficiency and covariant pinching. A mass-carrying resonance
component needs at least3 physical levels. A component with return below1/2
needs at least two occupied sites and hence at least5 levels; components with
one occupied site have return1/2. These are reused from K1990.

Choose an optimal tagged pattern at budget E0. If its value is1/2, the actual
three-level spectrum{0,1,2} prepared at1 already realizes the bound. Otherwise
at least one component has5 or more levels. With m active components,

    5+3(m-1)<=d, hence m-1<=c_d.

Discard unused components. Each remaining shape consists of distinct integers
with minimum0. Assign its tag index j in{0,...,m-1}, and shift ALL its physical
levels by j delta. If delta<=1/(c_d+1)<=1/m, levels from different components
have distinct fractional offsets. A cross-component difference has the form
integer+k delta with0<|k|<=m-1, so its nonzero absolute value is at least
min(delta,1-(m-1)delta)>=delta. Internal gaps are integers>=1.
Thus the new spectrum is nondegenerate, has ground0, the same dimension and
minimum spacing at least delta. Endpoint equality delta=1/m is allowed.

No new intercomponent bath resonance appears:0<|k|delta<1. Every original
shell unitary therefore remains conserving, every internal return is unchanged,
and the mixture has the same full channel/return. Its mean energy increases
by delta sum_j j w_j <=(m-1)delta<=c_d delta, with w_j the total preparation
weight in tag j. This is an actual physical protocol; no collision limit or
population refitting is being called feasible.

For E>=1+c_d delta take E0=E-c_d delta. The construction proves the upper
inequality in(1). For1<=E<1+c_d delta use the pure three-level protocol,
whose return equals V_d(1,t)=1/2. The lower inequality follows by inclusion
of the positive-spacing protocols in the unspaced class. Coherent preparations
remain covered by the previously proved pinching reduction.

K1968's finite continuous piecewise-affine curve is eventually constant, so
L_d(t) is finite. Apply its Lipschitz bound to the two arguments in(1) to
obtain(2), including E near1. This avoids a division by E-minimum-occupied-
energy, which would become a spurious singularity at integer budgets.
For d<=7, c_d=0 recovers the ALREADY KNOWN rigidity; that special case is
not presented as a new theorem.

## 2. One varying resource row forces fractional-linear branches

K1996's fixed-d finite spectrum algorithm uses finitely many component shapes,
interleavings and longest-path potentials. Every potential is the maximum
of finitely many functions n+k delta with integers n,k. On some punctured
interval0<delta<eta0, each maximum is one affine function. All potential
resonance equalities are also affine; shrink eta0 to avoid their finitely many
positive isolated roots. The actual resonance partitions, shell-rank tests
and occupied supports are then constant on this interval.

For each such spectrum/support, partition the probability simplex into its
finite return-formula sign cells. Their defining normals and affine return
objectives depend on t, but NOT on delta. Only the mean-energy inequality

    sum_i (a_i+b_i delta)p_i <= E

varies with delta. The normalization and nonnegativity constraints are fixed.
Every cell is a compact polytope; an optimum is at a vertex. Choose a maximal
independent active basis for that vertex. If the energy row is inactive, the
vertex/objective is constant. If active, AT MOST ONE basis row depends on
delta. By determinant multilinearity, its determinant and every Cramer
numerator have degree at most1 in delta. Thus its objective is fractional-
linear (a+b delta)/(c+e delta). Singular bases are omitted; bases singular
only at0 are legitimate on the punctured interval.

Feasibility signs and comparisons among this FINITE set of candidates change
only at finitely many polynomial roots, unless tied identically. Consequently
one feasible branch wins throughout a sufficiently small punctured interval.
This is stronger than merely saying the optimum is semialgebraic. The
one-varying-row property is essential: multiple independently varying resource
rows would allow higher-degree determinants.

By(2) the winning branch has finite limit V_d as delta decreases to0. If its
denominator has nonzero constant term, subtracting V_d leaves exactly
ell delta/(1+kappa delta). If the denominator has zero constant term,
boundedness forces the numerator's constant term to vanish too, and the
branch is constant after cancellation. Finally F_d>=V_d forces ell>=0.
If ell=0 the gap vanishes identically; if ell>0 it is Theta(delta).
This proves(3), including degenerate-at-zero bases, without claiming an
unspaced physical optimizer exists.

The coefficient algorithm is explicit: enumerate the finite small-delta
spectra, sign cells and bases; retain those feasible for all sufficiently
small positive delta, compare exact limits and leading coefficients, and
resolve ties by their fractional-linear formulas. Rational t,E give rational
coefficients and rational eta bounds obtainable from root isolation. The
algorithm can be very expensive. It was NOT executed for arbitrary d here.

## 3. Released successor: sharp coefficient on the entire unattained face

At t=1/2, [K1975](k1975-thermal-sharp-dimension-threshold-2026-10-23.md)
proves that for every fixed d>=10 and6/5<E<11/5,

    V_d(E,1/2)=63/100-3E/20.

It also reuses K1950's COMPLETE equality-face census: every normalized
canonical component satisfying R+(3/20)e=63/100 has occupied energies{1,3}
and is precisely type A or B,

    A=(9/10,1/10), e_A=6/5, R_A=9/20,
    B=(2/5,3/5),   e_B=11/5, R_B=3/10.

This is a full equality classification, not just two example protocols.
We now obtain, with r=E-6/5 in(0,1),

    lim_(delta->0+) [F_d(delta,E,1/2)-V_d(E,1/2)]/delta
         =(3/20)min(r,1-r).                              (4)

**Upper bound: try BOTH physical placements.** Two actual five-level ladders
with offsets0,delta have minimum gap delta for0<delta<=1/2. If B is shifted,
its weight w_B=r/(1+delta) gives exact energy E and gap

    G_B=(3/20)r delta/(1+delta).

If A is shifted, w_B=(r-delta)/(1-delta) gives exact energy E for sufficiently
small delta<r, and gap

    G_A=(3/20)(1-r)delta/(1-delta).

Both use10 actual levels and exact shell unitaries. Taking their minimum
proves limsup<=the right side of(4). The old one-placement family alone
misses the better first-order bound when E>17/10.

**Lower bound: near-optimality forces the classified equality faces.**
Take optimal positive-spacing protocols along any sequence delta->0. Pinch
and compress as in K1978, preserving return and not increasing energy. For
fixed d this leaves finitely many integer component shapes of bounded span,
with bounded offsets. Pass to a subsequence with fixed shapes and convergent
component weights w_j, normalized populations and offsets x_j>=0. Components
of vanishing limiting weight do not affect the limiting canonical mean,
because all canonical spans are bounded at fixed d.

Let e_j,R_j denote each normalized component's canonical (offset-zero) energy
and sharp return. Put lambda=3/20, a=63/100. The exact gap decomposes as

    F_d-(a-lambda E)
      =sum_j w_j(R_j+lambda e_j-a)
         +lambda sum_j w_j x_j
         +lambda(E-sum_j w_j(e_j+x_j)).                 (5)

All terms are nonnegative: the global component dual, nonnegative offsets,
and the upper energy budget respectively. The explicit upper family makes
the left side O(delta), hence every positive-weight limiting component must
saturate the classified dual; its offset tends to0, and the limiting actual
mean equals E. Therefore the total limiting B weight is r and A weight is1-r.
In particular limsup max_j w_j<=max(r,1-r).

The distinct component minima x_j are themselves actual physical levels.
They are delta-separated. All but the smallest are at least delta, so

    sum_j w_j x_j >=delta(1-max_j w_j).                 (6)

This bound does not require the smallest-offset component to have the largest
weight; replacing its weight by the largest only weakens the lower bound.
Combining(5)-(6) gives liminf gap/delta>=lambda min(r,1-r), proving(4).
If an unpinched implementation had return above its sharp diagonal shell
value, its extra cost is nonnegative and the same lower argument applies.

This successor evaluates the leading coefficient without enumerating all
larger-dimensional bases. For each FIXED d>=10 the coefficient is the same;
no uniform remainder as d grows is asserted. Equations(3)-(4) also imply a
fixed-d O(delta^2) remainder, the finite-ray follow-through below additionally identifies the eventual
finite-spacing curve. This does not give its full positive-spacing range.

### Finite-ray follow-through: eventual exact ten-level optimality

The finite-program proof gives more than a leading coefficient. Fix d>=10
and an interior E. For each small-delta actual resonance partition, choose
one homogeneous return sign cell in each component. Every such polyhedral
cone has finitely many extreme rays. Normalize each ray to total population1;
its canonical energy and return are constants independent of delta.
A product of component cones is generated by these single-component rays.
Lifting to their nonnegative weights changes neither the feasible populations
nor the linear return on that cell. The only coupled constraints are total
weight1 and one upper mean-energy bound. Hence an optimal lifted vertex uses
at most TWO rays (at most one if the energy inequality is inactive).

There are finitely many ray-pair/spectrum candidates on a small-delta interval.
Each feasible candidate that can win arbitrarily close to0 must limit to the
global line. The nonnegative decomposition(5) forces every positively weighted
limiting ray to be EXACTLY A or B with zero limiting offset. The ray population
is constant, so this is an exact identification, not an O(delta) proximity
claim. At an interior E both types have positive weights. They cannot be two
rays in one component sign cell: linearity would make their whole segment a
component equality face, contradicting the complete two-point classification.
They therefore belong to two distinct components.

Any other candidate has either a strictly larger limiting return, is infeasible
near0, or is tied to such an A/B realization. Finiteness excludes all strictly
worse limits on some common punctured interval. Extra zero-population levels
and components may be dropped. The two occupied types each have support{1,3};
replacing their component shapes by actual five-level ladders{0,...,4} retains
the exact shell construction and return. For sufficiently small delta<=1/2,
put the lower-offset type at0 and the other atdelta. Their original offsets
were nonnegative and at leastdelta apart, so this decreases both type energies.
At the same mixing weights it cannot worsen feasibility or return.
Optimizing those weights at budget E yields exactly the two families above.

Consequently for each fixed d>=10,E in(6/5,11/5) there exists eta_(d,E)>0
such that, for0<delta<eta_(d,E),

    F_d(delta,E,1/2)=63/100-3E/20
      +(3/20)delta min(r/(1+delta),(1-r)/(1-delta)).     (7)

The threshold may be chosen below min(1/2,r). Its numerical value has NOT been
computed;12 exact four-population optimizations below validate the two-ladder
subproblem, not that those sample spacings lie below every global threshold.
The finite candidate algorithm can certify a threshold at a chosen d,E.
There is no claim of a uniform eta across unbounded d or all interior E.

For fixed E<=17/10 the eventual winner shifts B, giving second-order gap
coefficient -(3/20)r. For E>17/10 it shifts A, giving coefficient
+(3/20)(1-r), once delta<2r-1 as well. At E=17/10 the B placement wins.
The switching boundary at finite delta is r=(1+delta)/2. Thus even the
second-order coefficient is now fixed; extending the validity interval or
studying growing d remains a different problem. More fixed finite levels
cannot improve ANY order in the eventual regime, though they can matter
outside it.

## 4. Executed sharpness and effective precision consumers

Reuse K1990's complete d8,t1/2,E7/5 spacing curve. For0<delta<=32/125,

    V_8=13/30,
    F_8(delta)-V_8=delta/(18+15delta),
    (25/546)delta <= F_8(delta)-V_8 <=delta/18.           (4)

Thus the general linear order is sharp in an actual solved model, not just
an artificial matrix pencil. The coefficient1/18 and curvature denominator
5/6 are exact algebraic consequences of the existing curve, reused as a
consumer of the new general theorem.

The producer separates54 actual multi-component protocols (dimensions5
through20, three spacings per component count and three temperatures). It
checks physical distinctness, exact shell ranks, unchanged return and energy
cost. It reads the complete previously certified t1/2 curves for dimensions3
through8, computes their maximum slopes and serializes sufficient spacing
for a uniform return error of1/1000. For d8, L_8=1/4 and c_8=1, so

    delta<=1/250 guarantees F_8(delta,E,1/2)-V_8(E,1/2)<=1/1000

for EVERY E>=1, not just the example budget. It also checks six exact points
of(4). These are physical/control and consumer calculations; they are not
an all-d LP enumeration.

The successor also executes36 exact energy-preserving A/B placements and
packing controls. The separate checker rebuilds shell counts and return flows
from spectra, checks386 physical/curve identities, and independently verifies six exact
symbolic matrix pencils with one varying energy row. It also solves12 complete
four-population two-ladder programs by enumerating the exact local return-cone
rays and their admissible two-ray mixtures. These do not enumerate arbitrary-d
competing spectra or certify the global threshold. Five corrupted energy,
return, modulus, sharp-gap and leading-coefficient inputs fail mathematical assertions after a
green baseline. A structural SymPy-expression comparison initially failed
and was corrected to algebraic simplification before the baseline; that is
not counted as a hostile mathematical detection.

## 5. Hostile review and remaining frontier

Strongest overclaim: calling a finite candidate count an efficient solver,
treating the eventual two-ladder theorem as a full-spacing curve, or claiming a uniform
positive lower coefficient over dimension/temperature/budget. None follows.
Strongest contrary cases are resonance changes, zero determinant at delta0,
and a nearly minimal energy budget; sections1/2 treat each explicitly.
A hidden second varying constraint would invalidate the fractional-linear
argument. The model here has exactly one varying mean-energy row.

The exposed-face eventual curve and all its local coefficients are now closed
for every fixed d>=10. The next thermal question is an explicit validity
threshold/full finite-spacing curve, or a joint limit where d grows as spacing
shrinks. Another proof of O(delta), the leading/second-order coefficient, mere
semialgebraicity or extra temperature samples does not answer those questions. New explicit
pulse or genuinely non-diagonal local pairing work remains a distinct
competitor. Source, physics-ledger and canon verdicts are unchanged;
SC-META-53 remains UNCERTAIN. Same-author internal verification is not external
review, proof-assistant certification or novelty evidence.
