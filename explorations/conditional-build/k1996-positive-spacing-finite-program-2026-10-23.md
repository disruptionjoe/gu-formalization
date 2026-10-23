---
title: "K1996: Finite positive-spacing thermal programs and nine-level rigidity"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1996_positive_spacing_finite_program.py
  - tests/channel-swings/k1996_positive_spacing_finite_program_probe.py
---

# K1996: Finite positive-spacing thermal programs and nine-level rigidity

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
result: fixed-d finite actual-spectrum reduction, rational optimum and complete nine-level wide-spacing rigidity
carrier: nondegenerate finite catalyst and unchanged four-level Gibbs bath with exact channel LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and upper mean-energy budget ON=independent_initial_registers
real_structure: complex conserving unitaries and real catalyst energies
grading: actual energy resonance components, not source chirality
action_owner: repository-construction -- fixed thermal channel
target: exact positive-spacing optimization and dimension9 threshold consumer MAP-TYPE=intertwiner
```

## Results and what is reused

For the unchanged thermal model of
[K1994](k1994-nine-level-thermal-reduction-2026-10-23.md), the missing
nine-level wide-spacing branch has the exact answer

    F9(delta,E,t)=F9(1,E,t),  1/2<delta<=1, E>=1, 0<t<1.        (1)

The right side is the complete finite connected-integer program already
available from K1994. Its all-temperature validity is proved by204 exact
component replacements, not by a temperature sample. Together with K1994
for0<delta<=1/2 and K1981 fordelta>1, this closes the finite-program reduction
of the nine-level optimum at every positive spacing and every temperature.
It does not provide a closed symbolic-temperature formula.

There is also a general algorithmic consequence. For EVERY fixed finite d and
positive spacing, the exact optimum reduces to finitely many ACTUAL spectra
and finite piecewise-linear population programs. At rational delta,E,t, a
feasible optimum has rational catalyst energies, rational populations and
rational return value. No rational-unitary assertion is made. The algorithm
is finite, with potentially enormous cost.

This reuses [K1978](k1978-thermal-spectral-spacing-2026-10-23.md)'s
longest-path compression and attainment, and the exact shell necessity,
pinching and sufficiency of
[K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md).
Neither compression nor attainment is new here. The new consequence is an
explicit finite spectrum-selection algorithm and rationality, stronger than
[K1987](k1987-thermal-spacing-parametric-frontier-2026-10-23.md)'s general
semialgebraic/algebraic statement. The full arbitrary-d enumeration is an
algorithm specified below, not a claim that all dimensions were executed.

## 1. Finite actual spectra for arbitrary fixed dimension

Join catalyst levels whose difference is1,2 or3. Each component has a shape
A_c of integers, minimum0, with successive gaps in{1,2,3}; otherwise the sorted
gap would disconnect it. For at most d levels, only finitely many lists of
such shapes exist. Include singletons and components with no initial mass
for general coverage; unnecessary ones may subsequently be discarded.

For each shape list enumerate every interleaving of its ordered levels. For
each adjacent pair(i,a),(j,b), impose the K1978 constraints

    y_c>=0,  y_j>=y_i+delta+a-b.                       (2)

Reject a positive directed cycle. Otherwise the longest-path potentials from
a zero super-source give the coordinatewise least feasible y. They are maxima
of finitely many simple-path weights. Thus for fixed delta this order yields
ONE canonical actual spectrum, with spacing at least delta and ground0.
Some component may become resonant with another; K1978 proves that the old
unitary subspaces remain orthogonal and can be retained inside the enlarged
shell. Every original ordered protocol maps to this spectrum with each level's
energy no higher, and the same channel and return. This justifies discrete
replacement without assuming that the old resonance partition is preserved.

Now enumerate occupied supports of each candidate spectrum. Impose the exact
shell-rank inequalities, and use the sharp shell-return formula on its ACTUAL
resonances. Covariant pinching never worsens return or energy, so diagonal
population optimization loses no coherent optimum. The formula is a finite
sum of positive parts of linear population expressions. Partition the simplex
by all their sign hyperplanes; on each cell minimize the affine return subject
to normalization, nonnegativity and the upper energy budget. A nonempty cell
has a vertex attaining its minimum. Take the minimum across all cells, supports,
spectra, interleavings and dimensions<=d.

Every program is an implementable physical protocol by shell sufficiency;
every original protocol is dominated by one program. These two inequalities
prove exact equality, not just an upper bound or an infimum of colliding tags.
When delta,E,t are rational, (2), all candidate energies and all cell coefficients
are rational. Vertex solutions and values are rational, proving the stated
rationality. Exact arithmetic detects infeasible cells too.

Released parameter consequence: simple-path weights have the form k delta+n
with integer k,n. Their maxima change at finitely many rational spacings.
Additional resonances occur on finitely many affine equalities of this form.
For fixed rational t,E, enumerate probability bases in each resulting spacing
interval. Their feasible solutions and objective values are rational functions
of delta. Comparing finitely many such candidates partitions feasible spacing
into finitely many semialgebraic intervals/points on each of which the value
is rational in delta. Optimizer-change boundaries need not be rational.
This is a finite construction, not a practical complexity bound or a uniform
claim as d grows. The existing exact feasibility domain is unchanged.

## 2. Exhaust every mixed nine-level case without unsafe replacements

Reuse K1994's support-size theorem and complete17-shape improving-component
census. If there is only one mass-carrying component, delete other components
and shift it to0; the connected-integer program applies. If every component
has one occupied level, return is1/2 and the three-level mean1 protocol dominates.
Otherwise dimension9 permits one improving5/6-level component with two
occupied levels and one pure3/4-level component. A pair gap>3 has no shared
occupied shells and cannot improve1/2.

A pure component can be replaced by an actual THREE-level subset containing
its occupied level e. Its lower partners cover bath labels k<=3-a; its upper
partners cover k>=b. Taking the nearest lower and upper partners covers all
four bath labels exactly when a+b<=4. Thus one of the six shapes

    B={0,a,a+b}, occupied at a; a,b>=1 integers, a+b<=4          (3)

suffices. Deletion preserves spacing and mean. Do not replace an improving
noncontiguous shape by a contiguous one yet: that could break intercomponent
spacing. Retain ALL17 shapes from the raw census.

Translate the union so one component minimum is0. Keep its shape fixed and
slide the other to the smallest allowed nonnegative offset x. For shapes A,B,
its forbidden offsets are the open intervals

    (a-b-delta,a-b+delta), a in A,b in B.               (4)

All centers are integers. For1/2<delta<=1 the first forbidden block containing0
has a right endpoint n+delta, with an integer n independent of delta in this
range. Consecutive integer centers have overlapping intervals; atdelta=1,
intervals with center gap2 only TOUCH at an allowed endpoint. This distinction
retains the correct endpoint and avoids treating spacing equality as collision.
Scanning the intervals produces the exact least offset.

The complete family is17 improving shapes times6 pure shapes times2 choices
of ground component:204 placements. Each stored witness identifies the source
shapes, occupied pair, n, and a connected integer spectrum with at most9 levels.
It maps the source pair to two target support sites with the SAME gap; both
pair energies and the pure site's energy are no greater even at the limiting
offset n+1/2. Thus energy domination holds uniformly for everydelta>1/2.
The target shell-rank constraints are checked exactly, not assumed by count.

## 3. Why the replacements dominate at every temperature

For diagonal populations p, the inherited exact return has the form

    R(p)=1/2 sum_i (p_i - incoming_i(p))_+.

For a resonant occupied pair of gap g, incoming flow depends only on p and
bath rates L_g,H_g, where

    L_g=(sum_(b=0)^(3-g) t^b)/(1+t+t^2+t^3), H_g=t^g L_g.

The target preserves the improving pair's gap and its two populations, hence
its original incoming flows at ALL temperatures. The third, previously pure
site keeps its population. Every new target resonance adds a NONNEGATIVE
incoming contribution; it cannot raise any positive-part deficit. Consequently
the target return is no larger, and its mean energy is no higher for EVERY
population vector, temperature and budget. This is the universal argument;
rational temperature controls are checks of its coefficient implementation.

Every target is spacing1-feasible. Conversely spacing1 spectra are feasible
at anydelta<=1. These two inequalities prove(1). No convex combination across
different spectra is used, and coherent preparations are covered by pinching.

## 4. Executed whole-budget and discontinuity consumers

At t=1/2 the wide-spacing curve has15 exact pieces, all serialized in the JSON.
The delta=1/2 curve has16. Their difference is positive EXACTLY when

    1117/743 < E < 79/45.

The complete piecewise-affine right jump is also serialized. For example,

    F9(1/2,18/11,1/2)=159/374,
    lim_(delta down to1/2,delta>1/2) F9(delta,18/11,1/2)=2795/6424,
    right jump=1087/109208 >0.

At E=7/5,2,3,4,5 the half-spacing and wide-spacing values coincide. AtE=3
both equal81/290. The terminal plateau27/130 starts atE=323/65. A ninth
level does not erase the half-spacing discontinuity, but the jump has a
budget-dependent support; it is not a universal positive gap at every E.
The independent fixed-budget solver checks both curves at18/11 and2.
Prior dimension9 small-spacing results remain intact.

## 5. Verification and remaining boundary

The separate checker independently enumerates the17 source shapes, reconstructs
all204 placements, solves their forbidden intervals from endpoints, checks shell
rank, pair-gap and energy domination, and evaluates return at rational controls.
It passes2454 coverage/physical/return/curve checks,228 separate interleaving
feasibility controls and4 independent probability optimizations. Four missing
shape, nonminimal offset, invalid support and wrong-value faults are rejected
after a green baseline. The producer checks1020 actual-spectrum placements
and builds exact whole-budget envelopes. Universal rationality, finite coverage
and all-temperature dominance rely on the arguments above, not sampling.

Strongest overclaim: replacing shapes before enforcing spacing, or assuming
new resonances preserve a tag formula automatically. Sections1-3 explicitly
handle both. Strongest contrary case:delta=1/2 has extra interleavings, retained
as a separate curve with a proved right jump. Weakest reproducibility seam:
the general algorithm's cost grows rapidly; only its placement primitive and
the complete nine-level specialization are executed here. Larger-dimensional
optimal values and a practical all-d solver remain open. The result supplies
an exact reduction and rationality, not a closed all-d formula.
Same-author separate implementations are internal checks, not external review,
formal certification or novelty evidence. SC-META-53 remains UNCERTAIN;
source, physics-ledger and canon verdicts remain unchanged.
