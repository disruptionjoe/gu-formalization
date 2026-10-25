---
title: "K2043: Two exact thermal spacing phases and the first physical transition"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unrestricted finite/countable thermal model on the declared energy and spacing intervals; later phases open
scripts:
  - tests/channel-swings/k2043_chamber_offset_frontier.py
  - tests/channel-swings/k2043_chamber_offset_frontier_probe.py
---

# K2043: Two exact thermal spacing phases and the first physical transition

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
result: two exact spacing phases, sharp first transition and physical dimension changes
carrier: four-state bath times finite/countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex states with nonnegative real diagonal populations
grading: physical energy shells and connected occupied components
action_owner: repository-construction -- inherited exact energy-conserving shell channels
target: spacing-dependent optimum, equality and resource costs MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The sufficient cutoff1/23508 of
[K2041](k2041-exact-small-spacing-frontier-2026-10-24.md) can be replaced by
the **sharp first transition** delta_c=2/181. A second exact phase extends
through delta_2=2/145. Both results cover arbitrary finite or countable normal
finite-mean catalysts in the inherited model, not just a bounded search.
Keeping the actual lowest component's return chamber supplies the missing
constraint. At the first transition the optimal right branch drops from22
to20 necessary physical levels.

## 1. Formulas and physical realizations

Keep bath energies0,1,2,3, populations(8,4,2,1)/15, the exact shell channel,
nonnegative physical energies, nondegenerate pure-point catalysts, minimum
physical spacing delta and energy budget E. Define

    (EA,RA)=(1575/653,729/2612),
    (EB,RB)=(675/181,81/362),
    (ED,RD)=(349/145,81/290),  Delta=EB-EA,
    fA(E,d)=RA+(RB-RA)*(E-EA)/(Delta+d),
    fB(U;E,d)=RB+(RU-RB)*(EB-E)/(EB-EU-d).             (1)

On EA<=E<=EB the exact optimum is

    min(fA(E,d),fB(A;E,d))       for0<d<=2/181,
    min(fA(E,d),fB(D;E,d))       for2/181<=d<=2/145.   (2)

The formulas agree at the shared boundary. A,B have populations on1,3,5,7,9

    A=(486,729,81,9,1)/1306, B=(36,54,81,9,1)/181;

D on1,3,5,7 has population(54,81,9,1)/145. Their complete physical ladders
are respectively0,...,10,0,...,10 and0,...,8.

The A branch puts A at offset0 and B at d. The other branch puts B at0 and
U=A or D at d. Fractional residues differ, hence no bath shells are shared;
actual return and mean are the mass-weighted endpoint values, including the
shifted mass's energy cost. The union's minimum gap is d for these d<1/2.
These are exact physical channels by inherited shell-capacity sufficiency.

The switch is the unique solution fA=fB(U); if
sA=(RA-RB)/(Delta+d), sU=(RU-RB)/(EB-EU-d), then

    E_switch=(RB+sU*EB-RA-sA*EA)/(sU-sA).             (3)

Here sU>sA. The switch lies strictly above EU+d and EA, and below EB
throughout the stated intervals. Multiplying positive denominators reduces
these statements to affine endpoint inequalities. Thus the winning B branch
is always physically feasible. For U=A,(3) reduces to(EA+EB+d)/2.

## 2. Why exactly one low-offset component matters

Reuse K2037's canonical support reduction, cutoff-nine arrangement bank
(183 orientation cells,3137 vertex records), and unnormalized zero-loss
return erasure. Canonical occupied supports have gaps1,2,3, adjacent gaps
summing at least4, and first occupied level max(1,3-first_gap); an isolated
input starts at1. Preserve each component's original physical offset d_i>=0.

If d_i<delta<1/2, that component FORCES the physical level d_i:

- with first gap1 the first root is2+d_i, and the shell at3+d_i has two
  occupied inputs, forcing all four outgoing catalyst levels d_i,...,3+d_i;
- with first gap2 the first root is1+d_i and the shell at3+d_i does the same;
- with first gap3, or an isolated input, the shell at1+d_i has only two
  nonnegative possible catalyst partners, d_i and1+d_i, so both are required.

Two distinct such ground levels would violate minimum spacing. If two
components claimed the SAME d_i, their first roots would be1+d_i or2+d_i,
which share a bath shell, so they would be one connected occupied component.
Therefore at most ONE occupied component has d_i<delta. All other components
pay at least delta on their entire mass. This uses physical completion,
including unoccupied levels; roots alone would miss the first-gap1 case.
If no component is low, all pay delta.

The exceptional component's truncated population belongs to one actual
edge-orientation cell. The clipped return is convex and piecewise affine
there; subdividing by deficit signs has the bank's vertices. Any affine
inequality true on all that cell's vertices holds on its whole population.
Do not allow it to combine A and B from incompatible orientations.

## 3. A finite exact certificate with a countable transfer

For each spacing phase and each of the183 cells, the certificate assigns
one or both lines fA and fB. Every assigned line obeys:

    R(v)>=f(e(v),d)          for every vertex in the LOW cell,
    R(v)>=f(e(v)+d,d)        for EVERY bank vertex in any HIGH component,
    f(10,d)<0.                                             (4)

The assignment is fixed throughout its closed spacing interval. After
multiplication by its positive denominator, each inequality in(4) is affine
in d. Checking both endpoints therefore proves the entire interval; a grid
or extrapolation is unnecessary. Phase1 labels are2 A-only,2 B-only,179 both;
phase2 labels are4 A-only,2 B-only,177 both. The two endpoints of phase1
are0 and2/181, and those of phase2 are2/181 and2/145. The d=0 row is a
certificate limit; physical attainment is asserted only for d>0.

Write the assigned line f(e)=a-s e, s>0. Erase a component's occupied
canonical levels above9, without renormalizing. If retained mass is m-q,
removed mass q and removed canonical energy h>=10q, zero-loss erasure and
(4) imply

    R_component >= a*m-s*e_actual
                  +(10s-a)q+s(h-10q)
                  +s*m*(d_i-lower_offset),                (5)

where lower_offset=0 for the exceptional component, delta for all others.
The shifted inequality in(4) is used for the latter; equivalently the last
expression is understood after incorporating that chosen shift in the
retained mass. More explicitly, the right correction is

    (10s-a+s*lower_offset)q+s(h-10q)
       +s*m*(d_i-lower_offset).                            (6)

All terms in(6) are nonnegative, since10s-a>0. Formula(6) is the exact
correction; dropping its additional s*lower_offset*q gives the weaker(5).
Summing over components and adding s*(E-e_actual_total)>=0 yields
R>=f(E). Every protocol admits at least one assigned line for its low cell,
so R>=min(fA(E),fB(E)). When all components are high either line applies.

For countably many components, sums of population and canonical energies
converge by normality and finite mean; corrections are nonnegative. The
inherited erasure theorem is l1-continuous, so the same inequality holds.
There is no claim that small tail mass implies small tail energy. The explicit
constructions in section1 attain the winning branch and prove(2).

## 4. Equality and the resource change

In0<d<2/181 the only equality vertices for the A line are low A and high B;
for the B line they are low B and high A. Strict tail/offset coefficients
eliminate tails and unused budget. Thus K2041's diagonal classification and
22-level interior minimum extend to this whole interval; endpoints need11.

At d=2/181, the B line additionally permits high D. D and A are adjacent
compatible endpoint diagonals of K2037's previous phase; every interpolation
between them is an actual return-affine shape. Therefore on the B-winning
side there is a continuum of optimal shifted D/A shapes, each mixed with
unshifted B using the energy-determined mass. Pure D gives20 physical levels;
any positive A part requires22. The A-winning side still requires22. At the
switch both placements optimize and the minimum is20. Endpoints remain11.
These assertions classify population diagonals, not the implementation of
all optimizing channels. The cell certificate and physical equality vertices
are part of the exact record, not a dimension inference from a convex drawing.

For2/181<d<2/145 the equality vertices reduce to low A/high B on the A
branch and low B/high D on the B branch. Hence the sharp dimensions are22
on the left,20 on the right (including its switch), and11 at EA,EB. Every
populated odd endpoint pair forces its entire consecutive completion by
shell dimension; the two different residues cannot share completion levels.
At2/145 additional low equalities appear; we prove the optimum there but
leave its complete equality/minimum-dimension classification open.

## 5. Both phase endpoints have actual counterexamples beyond them

The shifted D/B slope first improves on shifted A/B exactly when

    d>2/181,

as direct cross-multiplication of their two slopes shows. Choose E near EB,
where the B branch wins and both constructions are feasible. This gives a
physical20-level improvement for every sufficiently close larger spacing,
so2/181 is the first true transition, not a relaxation cutoff.

At the next endpoint use Q=(1/5,3/10,9/20,1/20) on1,3,5,7, with
(EQ,RQ)=(37/10,9/40), completed by0,...,8. Its return equals the D/B line
at d=2/145 and is strictly below it immediately afterward. The A line is
strictly above at that energy, so this9-level catalyst beats the entire
second-phase formula for all sufficiently close larger d. The probe executes
both counterexamples at their respective critical spacing plus1/10^6.
They demonstrate actual physical failure, not merely a negative coefficient.
The subsequent full spacing phase remains open.

## 6. Evidence, hostile checks, and next calculation

The producer checks all3137 bank records against both interval endpoints,
cell assignments, positive tail coefficients, transition identities and
explicit rational counterexamples. The separate checker reconstructs every
vertex's return from bath-label maxima and shell capacities, then uses
cleared two-point line determinants rather than the producer's intercepts.
It verifies30 physical mixtures, both transition rivals, all four forced-ground
cases and31 individual completion-level removals. Four clean-baseline
faults overextend the two spacing intervals, change an endpoint return and
change the actual rival mass. They fail mathematical or physical identities.
The original complete arrangement enumeration and erasure proof are reused by
hash, not rerun. Whole-interval, arbitrary-dimension and equality conclusions
rely on the written arguments, not fixture totals.

Same-author independent implementations are internal checks, not external
specialist acceptance, proof-assistant certification, or a novelty claim.
The strongest transfer risk was the low-offset packing lemma: using occupied
roots alone would be false reasoning for root2 components. Section2 supplies
the actual forced completion. The strongest countable risk is resetting
component offsets after erasure; equations(5)-(6) keep them. No source, physics
ledger or canon verdict changes.

Next compare the full regime beyond2/145, including Q and the newly equal
19/8 vertex, with near5/4 resource necessity and exact capped continuum wings.
The original sufficient cutoff and first transition search are settled; do
not requeue them. Deriving more candidate chords without proving chamber,
physical completion and tail transfer is insufficient.
