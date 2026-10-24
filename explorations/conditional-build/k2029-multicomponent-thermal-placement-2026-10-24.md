---
title: "K2029: Unrestricted wide-spacing thermal optimum and sharp dimension"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact fixed-bath finite/countable catalyst theorem on the stated spacing and energy rectangle; no GU identification or novelty claim
scripts:
  - tests/channel-swings/k2029_multicomponent_thermal_placement.py
  - tests/channel-swings/k2029_multicomponent_thermal_placement_probe.py
---

# K2029: Unrestricted wide-spacing thermal optimum and sharp dimension

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
result: unrestricted wide-spacing thermal frontier, unique optimal diagonal, sharp17-level dimension and component stability
carrier: inherited four-state bath times arbitrary finite or countable nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive initial states and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical state space and real nonnegative energy populations
grading: bath energy shells and resonance components, not fermion grading
action_owner: repository-construction -- exact extreme channel and conserving shell unitaries
target: global catalyst resource frontier on the stated parameter rectangle MAP-TYPE=intertwiner
```

## 1. Result

Keep the exact channel, bath energies0,1,2,3 with probabilities(8,4,2,1)/15,
nonnegative catalyst energies with physical ground0, minimum physical spacing
delta, upper mean-energy budget E, and marginal return convention of
[K2027](k2027-thermal-pattern-frontier-2026-10-24.md). For

    1/2 < delta <= 1,       7/5 <= E <= 8/5,

and every finite or countable catalyst, with any number of occupied components,
the exact optimum is

    F(E) = (985095-61407 E)/2040416 = a-c E.             (1)

K2027 established(1) only for one connected occupied component. The physical
placement argument below closes the multiple-component gap. Its same affine
diagonal attains(1). Every optimizer has that diagonal on occupied levels
1,3,5,7,9,11,13,15, saturates its budget, and requires all17 physical levels
0,...,16. Thus17 is the unrestricted minimum dimension on this rectangle.
Extra unoccupied levels, coherences and realizing unitaries need not be unique.

This is independent conditional quantum-information mathematics. Source,
physics-ledger and canon verdicts do not change. Outside this energy interval,
other bath temperatures and other return conventions remain different problems.

## 2. Two global component bounds

Write b=1/41. Every normalized connected occupied component, translated to its
canonical offset, obeys

    R+b e >= alpha_b = 42061/133660,
    R+c e >= alpha_c = 558727317/1662939040.             (2)

These statements hold for every finite/countable length and every admissible
gap pattern, with no energy-window assumption. They therefore apply to the
high-mean components that K2027's window certificate could not cover.

For each slope, the report stores4575 exact rational LP duals covering all
canonical supports through occupied energy14 and all edge orientations.
The programs include every nonnegative population, including zero faces, and
the positive-part return epigraph. The producer uses inherited edge matrices;
the separate checker reconstructs every row from actual bath-shell maxima.
Both replay all9150 duals without an optimizer. Numeric LP discovery is not
part of acceptance. A common physical equality witness has spectrum0,...,12,
occupied support(1,3,5,7,9,11), and populations

    (324,486,729,81,9,1)/1630.

For an arbitrary canonical component erase its tail above14 without
renormalizing. The [K2020 zero-loss erasure theorem](k2020-posttransition-tail-and-resources-2026-10-24.md)
gives R_original>=R_prefix. If tail mass is q and tail energy h, then h>=15q
and homogeneity gives

    R+lambda e >= (1-q)alpha_lambda+lambda h
                 >= alpha_lambda+(15lambda-alpha_lambda)q.

Both final coefficients are strictly positive. The prefix remains a connected
path; deleting its zero faces only enlarges the finite relaxation. The
established l1 limiting argument treats countable tails. Translation by x
adds lambda x to the bound. Additivity extends the translated inequalities
to any collection of components whose canonical offsets are at least x.
We also reuse K1950's global supporting lines R+e/4>=3/4 and
R+3e/20>=63/100; those are valid even when their pointwise right sides are
negative. No extrapolation of F outside its certified window is used.

## 3. Mandatory physical levels prevent cheap interlacing

Distinguish a **physical resonance component**, which includes unoccupied
completion levels, from a **connected occupied component**. Removing a whole
physical component with no population preserves all active shell dimensions.
Translate the remaining spectrum to ground0. This can only lower energy and
does not change return or spacing. Positive spacing gives a first component
also in the countable case.

First suppose the lowest populated physical component has an occupied level1.
Its first connected occupied support s starts at1; its first gap is2 or3,
since first gap1 would require a negative physical energy. If it is not a
singleton, shell rank forces the four physical levels z,z-1,z-2,z-3 whenever
two occupied bath inputs share shell z. For an edge of gap d starting at x,
the union of these forced levels is the entire integer interval
[x+d-3,x+3]. Successive allowed gaps have sums between4 and6, so these
intervals overlap or touch. The first occupied level1 also forces level0.
Consequently the physical spectrum contains every integer in[0,L], where

    L=1                       for a singleton,
    L=s_last+3-d_last          otherwise.              (3)

A distinct fractional physical component cannot put any level inside this
interval when delta>1/2: every point there is within1/2 of an integer that
is already required. Its physical minimum is therefore at least L+delta.
Its canonical occupied offset is no smaller than that physical minimum.

Another occupied component in the same integer physical component begins at
least4 above s_last. Its canonical first occupied energy is at most2, so
its canonical offset is at least s_last+2. Therefore **all** other occupied
components, including ones sharing unoccupied physical levels, have offset
at least

    x0=min(L+1/2, s_last+2).                            (4)

This is a deliberately weak bound valid throughout the open spacing regime.
No consecutive-completion assumption or uncharged separate flag is used.
For an infinite first occupied component, the forced prefix is unbounded
and leaves no other occupied component; K2027 applies directly.

## 4. Long first components

If L>=7, then x0>=7. All remaining components have mean at least8, so the
normalized first component has mean e1<=E whenever there is a mixture.
K2027 supplies the backward line

    R1+b e1 >= a-(c-b)(7/5),       e1<=7/5,

and R1+c e1>=a for7/5<=e1<=E. The other components satisfy both lines with
strict surplus, because

    alpha_b+7b-[a-(c-b)(7/5)] = 72367441/6818050064 > 0,
    alpha_c+7c-a             = 106201827/1662939040 > 0. (5)

If e1<=7/5, summing the b-lines gives the required bound at total mean e:
a-b e-(c-b)(7/5)>=F(E), since e<=E and E>=7/5. If e1>=7/5, sum the c-lines.
Thus R>=F(E), with a strictly positive charge for every nonzero population
outside the first connected occupied component.

## 5. Short first components

The cases L<7 are finite: all supports start at1, end by6, and obey the
same adjacent-gap rule. There are13 orientation cells, including the
singleton. For each cell let p,z be the unnormalized first-component
populations and return epigraph. Let q,h,r be the aggregate mass, energy and
return of every other component. Impose

    sum p+q=1,    7/5<=s dot p+h<=8/5,
    h>=(x0+1)q,
    r+lambda h >= (alpha_lambda+lambda x0)q,

for the four slopes in section2, together with the first component's shell
inequalities and nonnegativity. The program minimizes sum z+r+c(s dot p+h).
These constraints relax the actual spectrum and permit all numbers of other
components, so a lower bound is safe. Every one of the13 exact duals exceeds
a. The smallest surplus is

    m_short=3404003679/6803670232240 > 0.               (6)

When actual total mean e<7/5, no extra argument is missing: its return is
bounded below by the optimum under budget7/5, using exactly the same program
with an energy-slack variable or, equivalently, increasing h until total
mean7/5. Increasing h relaxes all displayed lower bounds and h's lower bound,
so it gives a feasible relaxed point with the same objective return. The
certified R+c(7/5)>a then implies R>F(7/5)>=F(E).

## 6. The remaining placement case

Suppose the first populated physical component contains no occupied level1.
Its normalized mean e1 is at least2. Every later populated physical component
has minimum at least delta>1/2, hence normalized mean e2>3/2. Aggregate later
components into e2,R2 and let w be the first component's population. The
inherited global lines give

    R1>=63/100-3e1/20,   R2>=7/8-e2/4,
    R>=7/8-e/4+w(e1/10-49/200).

For e1>=49/20 the last term is nonnegative. For2<=e1<49/20,
w<=(E-3/2)/(e1-3/2); the ratio
(e1/10-49/200)/(e1-3/2) increases and is at least -9/100.
Thus for feasible budgets E>=3/2,

    R>=101/100-17E/50 > F(E).                          (7)

The smallest gap on[3/2,8/5] is recorded exactly. Budgets E<=3/2 are
infeasible in this case. If only the first physical component is populated,
its mean at least2 is likewise infeasible. This argument allows multiple
occupied components inside each physical one, because the inherited global
lines are additive after canonical translation.

## 7. Equality, dimension, stability and the spacing boundary

Sections5,6 are strictly above F. Section4 has equality only if q=0.
K2027's all-size equality theorem then forces the unique affine diagonal,
mean E and zero translation. Its eight positive occupied energies force all
levels0,...,16 by shared-shell rank. The physical17-level construction
attains the bound for every delta<=1. This proves unrestricted minimality;
it is not an inference from the size of a successful witness.

For epsilon<min(m_short,m_no_first_one), an epsilon-optimal protocol must
be in the long-first-component case. If q is its total population outside
that connected component, (5) gives

    q <= epsilon / min(72367441/6818050064,
                       106201827/1662939040).          (8)

This is a component-population stability bound, not a bound on the number
of negligible unoccupied or weakly populated levels. K2027's connected tail
bounds are not silently asserted for every conditional component mean.

The restriction delta>1/2 is essential. At delta=1/2 place the two valid
five-level spectra0,...,4 and1/2,...,9/2 together. Mix occupied populations
(9/10,1/10) on(1,3) and(2/5,3/5) on(3/2,7/2), with second weight
w=(E-6/5)/(3/2). The mean is E and return is57/100-E/10, strictly below F
throughout[7/5,8/5]. Both full spectra and all shell capacities are checked.
Consequently the unrestricted optimum has a strict right jump at spacing
1/2, at least F(E)-(57/100-E/10). This is a lower bound on the jump, not a
new exact formula for its left side.

## 8. Review and remaining work

The dangerous extrapolation was applying K2027's energy-window result to
high-mean mixture components. New all-energy supporting lines avoid it.
The dangerous geometric shortcut was assuming every completion consecutive;
(3),(4) use only compulsory levels and explicitly distinguish same-residue
occupied components from distinct physical components. The strict boundary
is tested by actual half-spacing counterexamples. Both original and separate
bath-label replays verify9150+13 duals; the latter also checks901 forced-prefix
examples, actual17-level optima and five mathematical corruptions. Those
examples support the instruments; the arbitrary-length placement proof is
the argument in sections3--6. Input hashes prove provenance separately.

All checks are same-author internal verification. No external specialist,
proof-assistant or novelty certification is claimed. Next substantial thermal
work is the all-energy phase diagram or another bath parameter, requiring new
optimality contacts and supporting lines. Repeating this rectangle's multiple-
component test, equality or17-level minimum would duplicate the result.
