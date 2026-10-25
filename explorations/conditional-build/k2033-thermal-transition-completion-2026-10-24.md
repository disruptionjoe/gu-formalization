---
title: "K2033: The complete thermal17 phase and two discontinuous dimension drops"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact fixed-bath thermal17 phase and endpoint diagonals; adjacent phases outside prior window remain open
scripts:
  - tests/channel-swings/k2033_thermal_transition_completion.py
  - tests/channel-swings/k2033_thermal_transition_completion_probe.py
---

# K2033: The complete thermal17 phase

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
result: exact thermal17 phase edges, endpoint diagonals and minimum physical dimensions
carrier: four-state bath times finite or countable completed catalyst LAYER=toy CHIRALITY=N/A
pairing: positive bath/catalyst populations and marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical states with nonnegative diagonal populations
grading: bath energy and resonance components, not fermionic grading
action_owner: repository-construction -- channel and energy-conserving shell unitaries
target: unrestricted fixed-bath return under energy budget and spacing MAP-TYPE=intertwiner
```

## 1. The phase is now closed, with exact endpoint sizes

[Verified conditional mathematics.] For bath energies0,1,2,3 and populations
(8,4,2,1)/15, minimum catalyst spacing1/2<delta<=1, and the inherited channel,
shell-capacity and half-trace return convention, the unrestricted finite/countable
optimal return is

    F17(E)=(985095-61407E)/2040416,
    L=8283273393/6147208289 <= E <= U=3746293/2243485.    (1)

L is about1.3474854 and U about1.6698543. Both are **exact phase edges**.
For L<E<U the unique optimal diagonal is the existing17-level affine population,
with exact mean E, and17 physical levels are necessary and sufficient.

At L there are exactly two optimal diagonals: that17-level population and
K2031's21-level population. Their supports are respectively the odd levels
through15 and through19; the minimum physical dimension at L is17.
At U there are exactly two optimal diagonals: the17-level population and a
five-level protocol with occupied energies1,3 and populations(3-U)/2,(U-1)/2.
The minimum dimension at U is5. These are **isolated diagonal alternatives**,
not a convex segment of equally optimal mixtures. Coherences, empty levels and
implementing unitaries are not classified by diagonal uniqueness.

Together with K2031 below L, the sharp resource dimensions are21 just below L,
17 at L and throughout(L,U), and5 at U. We do not claim a minimum dimension
immediately above U, or an unrestricted optimal formula there. The five-level
protocol beats F17 immediately to the right, which suffices to prove the edge.
Source claims, GU physics ledger and canon remain unchanged.

## 2. The tempting next crossing fails an actual physical test

K2031 supplies a13-level family crossing F17 at
214602655/126183719, about1.700716. That crossing is **not** the unrestricted
right edge. On the complete five-level spectrum0,1,2,3,4, put

    p1=(3-E)/2, p3=(E-1)/2,
    R5(E)=17/20-E/4,       6/5<=E<=11/5.                (2)

The bath-label shell calculation verifies normalization, exact mean, every
shell-capacity inequality and the displayed return. Solving R5=F17 gives U.
At the proposed13-family crossing the actual five-level return is strictly
smaller than F17; the report preserves that protocol as a counterexample.
The next certificate target was therefore changed to U, not obtained by
extrapolating the13-family line. Since R5 has steeper negative slope than F17
and stays feasible above U, F17 cannot remain optimal there.

On the left, K2031's attained F21 has shallower negative slope and intersects
F17 at L. It is strictly smaller just below L. This gives the other exact edge
once the lower certificate throughout[L,U] is proved. Both edges are decided
by physical protocols, not solely by dual sensitivity.

## 3. Complete connected certificate and inherited backward control

The new optimizer-free proof object contains one exact rational certificate
for each of308097 admissible support/orientation cells through canonical occupied
energy21. It includes zero-population faces. Every cell proves

    R+c e >= a, L<=e<=U,
    a=985095/2040416, c=61407/2040416,                  (3)

or certifies infeasibility by an exact minimum/maximum energy bound. No support
or orientation is omitted. Two implementations independently generate coverage
and reconstruct inequality coefficients; the second derives them directly from
bath labels. Discovery first filled the gap through8/5, then attempted the
refuted family crossing, and finally reconstructed the duals needed through U.
The acceptance check uses rational signs and reduced costs, not solver status.

For means below L, reuse K2031's proved connected result and its backward
line with b=43/2000. On[13/10,L], its F21 slope c21 is greater than b; below13/10
its existing backward line applies. Since F21(L)=F17(L), both regions give

    R+b e >= F17(L)+b L, e<=L.                        (4)

This is a new composition of already checked evidence; the unchanged original
low-energy bank is pinned and reused, not counted as newly replayed.

Canonical supports have integer energies. Erasing energies above21 removes
mass q and energy h with h>=22q. Homogeneity, the inherited zero-loss erasure
inequality and(3),(4) give, at a canonical mean e<=E,

    R >= F17(E)+b(E-e)+b(h-22q)+kappa(E)q,
    kappa(E)=(22-E)b-F17(E)>0 on[L,U].                 (5)

The report verifies the exact minimum at the interval endpoints. A canonical
translation tau incurs b*tau as well. Countable supports use the previously
proved l1 erasure theorem. Thus there is no hidden dimension cutoff; equality
has no erased tail, translation or unused energy. The integer22 charge is
valid only after canonical translation, not at an arbitrary real threshold.

## 4. All physical components, including fractional placements

Reuse the compulsory-level argument from
[K2029](k2029-multicomponent-thermal-placement-2026-10-24.md): a first occupied
connected component starting at1 forces every physical integer0,...,J, where
J=1 for a singleton and J=s_last+3-d_last otherwise. At delta>1/2, every other
occupied component has offset at least min(J+1/2,s_last+2). This includes
components sharing empty physical levels and fractional physical components;
no consecutive-completion assumption is imposed on arbitrary competitors.

For J>=8 every other component has offset at least8. The inherited all-energy
banks for slopes b and c are replayed on all9150 canonical cells through14;
15lambda>alpha_lambda gives their all-size/countable transfer. Both translated
lines strictly exceed the corresponding first-component line. Summing either
the backward or main inequality proves R>=F17(E), with positive charge for every
nonzero population outside the first component. Equality therefore has a single
occupied component. The first normalized mean is at most the total budget
because every other normalized mean is at least9.

For J<8, all25 first-component orientation cells are included. Aggregate other
components into mass q, energy h and return r. Impose h>=(offset+1)q and four
translated supporting lines, together with the first-component shell inequalities,
normalization and L<=total mean<=U. Every exact new dual is at least a,
or proves minimum energy above U. Exactly three cells contact a at U. Their
strictly negative upper-energy multiplier forces that endpoint, and their
strictly positive reduced cost on aggregate h forces h=0. Since
h>=(offset+1)q with offset+1>0, q=0: equality has no other component.
The connected equality classification below then supplies the five-level
diagonal. These three cases are strictly above the line at every E<U;
they must not be called strict at U. For smaller actual means, increasing the
relaxed h to reach L relaxes all these constraints without changing return.
This is a relaxation proof, not a fictitious physical energy adjustment.

If the first populated physical component has no occupied level1, K2029's
placement argument gives R>=101/100-17E/50 when E>=3/2; smaller budgets are
infeasible. Its strict gap above F17 remains positive through U. These cases
exhaust arbitrary finite/countable spectra and numbers of components.

## 5. Equality, two isolated choices, and physical dimension

For every contact certificate, complementary slackness sets every positive
reduced-cost variable to zero and every negative-multiplier inequality tight.
A negative lower/upper energy multiplier restricts equality to L/U respectively;
that face cannot be used for interior uniqueness.

For the remaining21 interior contact cells, the exact homogeneous nullspace
forces the known affine17 diagonal. At each endpoint we separately intersect
the original shell/positivity inequalities with normalization, exact energy and
return equality. Complete rational face classification gives only zero-dimensional
nonempty faces. The left union contains exactly the17 and21 diagonals; the right
union exactly the17 and5 diagonals. The separate checker reconstructs the bath
inequalities, solves the complementary equations and checks any residual face
with exact rational polyhedra. The two implementations share the rational
polyhedral backend for that fallback; this is internal verification, not an
independent solver or proof-assistant certificate.

The physical lower bound counts completion levels, not occupied levels. Whenever
two occupied inputs share a bath shell, the capacity inequality forces all four
levels completing that shell. For each endpoint diagonal and the interior17
family, these forced intervals are exactly0,...,20;0,...,16;or0,...,4. Complete
spectra of those sizes attain the values. Thus endpoint minimality is proved,
not inferred from successful witness dimensions. The complete diagonal classification excludes every nontrivial convex mixture
of the two endpoint populations, since it would be a third diagonal. The return functional is
not assumed convex across shell-order cells.

## 6. Stability, controls and next phase

At a fixed strict-interior energy and sufficiently small return surplus, the
short-placement and no-first-one gaps exclude those cases. The three short
endpoint contacts have a gap proportional to U-E, so this exclusion is not
uniform as E approaches U. The long-component margins bound outside-component
population by surplus divided by the smaller margin. For a connected protocol,
(5) bounds tail mass by epsilon/kappa_min, unused energy by epsilon/b, and tail
energy by(22/kappa_min+1/b)epsilon. These control population/energy, not the
number of negligible or empty levels. The inherited half-spacing competitors
preserve the essential delta>1/2 boundary; no exact left-spacing optimum is
newly claimed here.

Actual dual normalization/sign faults and physical population/completion/return
faults are tested after a clean baseline. Provenance hashes are separate from
mathematical checks. The full-form and thermal results do not alter any source
polarity, canonical verdict or physics recovery count. No novelty or external
specialist acceptance is asserted.

A successor search used exact active-equation reconstruction when needed over
all connected supports through14 at E=7/4,9/5,2 (3649,3649,4575 orientation
cells respectively). No sampled competitor beat R5. This is a finite discovery
result, not an all-size certificate, and supplies no new optimality claim.

The immediate remaining thermal question is what attains the optimum above U,
where the five-level line is a feasible upper bound only. It requires a new
supporting-line and physical-placement proof, not extending the now-closed17
phase. K2031's left21 edge and near5/4 accumulation remain open. Capped-wing
continuum feasibility remains a separate mathematical question.
