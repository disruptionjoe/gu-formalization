---
title: "K2072: Strong compulsory-ladder placement in the global thermal certificate"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact fixed-bath finite/countable lower bound; no optimality, dimension minimum or GU verdict
scripts:
  - tests/channel-swings/k2072_compulsory_ladder_thermal_bound.py
  - tests/channel-swings/k2072_compulsory_ladder_thermal_bound_probe.py
---

# K2072: Strong compulsory-ladder placement in the global thermal certificate

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: stronger joint physical low/high placement consumed in a global thermal certificate
carrier: fixed four-state bath and finite/countable nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: classical marginal return and positive population mass ON=declared_bath_catalyst
real_structure: real nonnegative populations with exact rational certificates
grading: occupied energy and resonance component labels
action_owner: repository-construction -- inherited exact shell-capacity model
target: wide-spacing energy-constrained return MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The stronger compulsory-ladder placement already
used in K2029 can be extended to the low-cell assignment used by K2059/K2070. Consuming
it removes the previous high174 contact, improves the global lower bound, and exposes
the next joint-tail limitation. This is a reuse and extension of physical packing,
not a new generic packing principle or GU evidence. The bath remains(8,4,2,1)/15,
1/2<delta<=1, and E=5/2. Source, ledger and canon are unchanged.

The exact bracket is

    437326017365327165213/1570850681658905890000 <= F_delta(5/2)
        <= 335946011010129/1206372108151072.

The new lower is 0.27840075601806180; the width is
0.00007551903857189, reduced by 17.832894 percent
relative to K2070. Only cell164 needs replacement at this threshold; all671
assignments are compared. The certificate stores the exact affine line and its
valid interval [91135/37292, 1902504111222032340789/758668264726977861095].

## 1. Original spectrum, not independently shifted components

Use K2049's at-most-one occupied component with canonical offset0<=D<1. All other
components have offset>=1. If the low component has at least two retained occupied
levels s, let x=s[-1], z=s[-2]+3. Its compulsory physical levels contain every
D+j, 0<=j<=z, by K2059's translated shell-capacity argument. The root can be1 or2;
root2 starts with gap1 and its first shared shell forces0..3, while root1 starts
with gap2 or3 and the lower singleton/shared shell supplies the missing ground
pair. This is a statement about the original catalyst spectrum.

We prove the safe improved shift for EVERY other occupied component:

    ell(s)=max(1,min(z+1/2,x+2)),   len(s)>=2;
    ell(s)=1,                     singleton.          (1)

The old shift was max(1,s[-2]+1);(1) is no smaller. The open condition delta>1/2
licenses using its weaker closed value1/2 in a lower certificate.

## 2. Same residue and different residue must be separated

A high component with the SAME fractional residue cannot occupy an integer point
between the low occupied positions: their gaps are at most3 and it would share a
bath shell with a low occupied input. It cannot precede the low root: a high root
has energy>=2, whereas the low root is D+1 or D+2 with D<1; a same-residue earlier
high input would either violate its offset>=1 or share a shell. The first high
occupied energy y must therefore be at least D+x+4. Its canonical root r<=2 gives
D_high=y-r>=D+x+2>=x+2. Sharing unoccupied completion levels is permitted throughout.
No disjoint-physical-component assumption is made here.

For a DIFFERENT fractional residue, any physical level in[D,D+z] lies within1/2
of a mandatory ladder point, violating the physical minimum spacing. K2059 shows
the high first occupied energy y>D+z. Since z>=4 and D<1, every potential bath
partner y-1,y-2,y-3 lies above D whenever it is below y. Such a partner cannot
jump underneath the whole compulsory interval.

For canonical root2 the first gap is1; rank4 of its shared shell forces the physical
level y-2. For canonical root1 with first gap2, rank4 forces y-1. Each must lie above
D+z and at distance at least delta from its last mandatory point. Consequently
D_high=y-r>=D+z+delta in both cases. For canonical root1 with first gap3, or a
singleton, the lowest shell contains one occupied bath input and needs two output
columns. Besides level y it needs at least one of y-1,y-2,y-3. Each candidate lies
above D; whichever supplies the second column must be above D+z+delta. Thus
D_high=y-1>=D+z+delta again. These are precisely the inherited single-input rank2
and two-input rank4 capacity conditions, not new freely chosen completion levels.
Combining the two residue cases yields(1).

If the low occupied component extends beyond the cutoff11 prefix, the shorter prefix
only weakens the compulsory interval and the same-residue separation. Use its genuine
positive support first, then the fixed support cell's closure. A zero population at a
bank vertex does not authorize recompressing that vertex and changing its shift.
For no low component use the singleton assignment. Countable supports cause no new
packing issue: the same finite prefix forces the same physical points.

## 3. Consuming the result without dropping any tail inequality

Replace only the high-component shift in K2070's exact assignment method. Keep the
same low-cell response, two/three-terminal geometries, actual incoming convex majorant,
all shorter prefixes, fourth-depth reachability caps, high Bellman recurrence, wholly
erased roots, cutoff64, and every high-bank vertex. The high recurrence sees a-t*ell
in place of a; the shift must enter BOTH its recurrence and vertex energy. Using it
only in the final reported energy would be invalid.

For each new rational(a,t,theta), the producer reconstructs actual maximizing policies
and adds violated affine policy cuts before acceptance. The separate checker evaluates
the actual response envelope and Bellman values directly, using raw bath return for
low vertices and inherited independently checked values for all high vertices.
The complete671-cell/20975-vertex bank and exact terminal geometry are unchanged,
hash-pinned reuse. Their completeness is not inferred anew from these checks.

Every new line is checked on all high cells and on its actual low cell. Retained
older lines are still valid because increasing a lower bound on high offsets weakens
their physical restriction. The global lower is the minimum over ALL671 assigned
lines at E5/2. Exact affine dominance at both stored interval endpoints proves the
same line throughout that interval. This does not optimize over every possible
certificate or physical population.

For finite components K2059's reverse erasure and K2070's joint response prove
R>=a*mass-t*energy. The physical offset comparison above pays each high component
with the same(a,t), so independent incompatible placements are never summed.
Unnormalized finite prefixes and the inherited l1-continuity/finite-mean argument
pass this to countable populations, with no fictitious last atom at infinity.

## 4. Selective fourth-terminal follow-through

After stronger packing and theta69/100 gave lower0.27839933899212543, the active
cap was state(18,2). With low endpoint9 and first tail energy>=12, the ONLY paths
to that state are gaps(3,1,3,2) and(3,2,2,2). Five or more steps would end at least20,
because each adjacent pair of gaps sums to at least4. This is independently checked
by complete finite path enumeration up to18, not inferred from the active optimizer.

Extend the three-terminal prefixes(3,1,3) and(3,2,2) across EVERY allowed next gap:
(3,1,3,1),(3,1,3,2),(3,1,3,3),(3,2,2,2),(3,2,2,3). Keep each actual shorter
three-terminal prefix with reward a-t*n3; for each four-terminal continuation use
rewards a-t*n1,a-t*n2,a-t*n3,G(n4,d4). The fourth response is the same exact raw
positive-part deficit sum as K2070, now on five populations. All other prefixes
retain their original three-terminal response. Remove ONLY cap(18,2); every other
fourth-plus cap remains, including every possible later erasure state. Thus no
unexpanded route can use the removed cap, and every tail length is still paid.

The finite arrangement proof extends in dimension4: include every coordinate,
flow-reversal and possible deficit-zero hyperplane. Intersect all independent
quadruples for vertices and all independent triples of homogeneous boundaries for
recession rays. Cells are pointed polyhedra; an affine objective is controlled by
these vertices and rays. The producer uses exact integer determinant minors; the
checker independently uses rational row reduction and replays the loss from raw
bath-shell maxima. Both p0=1 vertices and p0=0 recession costs are checked. In each
incoming mixture the producer may group multiple paths before taking its two maxima;
that only enlarges its valid upper price. The checker directly tests each actual
path's mixture, which independently suffices for the physical inequality.

This increases the bound again to the stated final value. The remaining contact is
now a four-terminal incoming-mixture contact, not the discarded high174 or isolated
fourth cap. The same globally checked line, countable transfer and energy interval
consume the improvement. No fourth-terminal geometry is claimed for unlisted paths.

## 5. Weight reconnaissance and actual limitation

The placement-only step at theta7/10 raises the lower to0.27839609883571137.
Following that result, exact fixed-weight candidates at 0, 1/2, 4/5, 9/10, 1, 3/5, 13/20, 27/40, 5/8, 17/25, 137/200, 69/100
were evaluated with all actual inequalities. The selected theta69/100 gives the
pre-extension lower0.27839933899212543 and is retained for the fourth-terminal result. At theta1 the lower is only0.27819680680611525, so simply
maximizing the incoming correction is not valid optimization. No weight-optimality
or exhaustive scalar-search claim is made. The new low164 shift is21/2 instead of8.
The cutoff and every high-component cap remain included.

The first strengthened certificate moves the active obstruction from high174 at
old offset8 to fourth-and-later state(18,2). That fourth-state response was then constructed and consumed above. The next input
is an incoming-aware shared response beyond the current four-terminal contact,
a physical inequality changing that contact, or a genuinely new feasible population. Independently increasing
its sharp single-terminal cap would repeat a ruled-out move. Scalar mixture discovery
is reported as discovery, not a proof that the best weight or every tail method is
exhausted. K2068's finite41-level upper remains unchanged.

## 6. Hostile review, controls and limits

Strongest overclaim: the low support must force actual unoccupied physical partners;
canonical relabeling alone proves no stronger shift. The proof above explicitly
uses inherited rank2/rank4 shell capacities. Strongest contrary case: same-residue
components may share mandatory unoccupied levels, so treating all components as
separate fractional ladders would falsely replace the minimum in(1) by z+1/2.
The [2,3] control has z=5, and same-residue high root2 at7 may begin offset5:
its first gap1 completes5..8 and shares physical level5. Hence5 is safe while5.5
would exclude an allowed arrangement. Weakest reproducibility seam: a producer and
its own policy cuts are not independent acceptance; the separate checker evaluates
all actual inequalities, and verifies the geometric shift independently.

Written proofs supply the physical packing, interpolation and countable transfer.
Exact finite checks supply certificate arithmetic. Same-author checking only;
no independent specialist, proof-assistant, novelty or unrestricted-optimality
certification. No new scientific status is assigned to historical source claims.
