---
title: "K1992: Complete eight-level spacing reduction and a sharp jump"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1992_wide_spacing_eight_level_rigidity.py
  - tests/channel-swings/k1992_wide_spacing_eight_level_rigidity_probe.py
---

# K1992: Complete eight-level spacing reduction and a sharp jump

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
result: all-temperature wide-spacing rigidity through dimension8, complete finite program and sharp half-spacing discontinuity
carrier: nondegenerate catalyst with at most8 levels and fixed four-level Gibbs bath LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitary with arbitrary coherent preparations
grading: actual energy resonance components, not source chirality
action_owner: repository-construction -- fixed exact thermal channel
target: all-positive-spacing finite optimization and physical boundary behavior MAP-TYPE=intertwiner
```

## Result

Let F_d(delta,E,t) be the exact-channel optimum in
[K1990](k1990-small-dimension-thermal-frontier-2026-10-23.md), with AT MOST d
physical energy levels, positive minimum spacing delta, mean energy at most E,
and bath weights t^b/Z for b=0,1,2,3 and0<t<1. Then for every E>=1,

    F_8(delta,E,t)=F_8(1,E,t),   1/2<delta<=1.          (1)

The threshold1/2 is sharp even with finite exact protocols. At t=1/2,E=18/11,

    F_8(1/2,18/11,1/2)=159/374,
    F_8(delta,18/11,1/2)=97/220    for1/2<delta<=1.     (2)

The exact right jump is59/3740. This is a real spectral-spacing discontinuity,
not a tagged-collision infimum or floating optimization artifact.

Together with the prior small-spacing templates, (1) closes the finite
reduction for EVERY positive spacing through dimension8, at every temperature
and budget in the known feasible domain. It does not provide a closed symbolic-
temperature formula or an arbitrary-dimension rate.

## 1. The remaining physical configuration

Reuse K1990's complete component classification and K1984's five-level
classification. Connecting energies whose differences are1,2 or3 gives
integer-translated components. Each mass-carrying component needs at least3
levels; any component that beats return1/2 needs at least5. Through dimension8,
a multi-component improvement can therefore only be5+3. The improving
five-level component has spectrum a+{0,1,2,3,4}, occupied at a+1,a+3.
The three-level component has a single occupied energy.

All other configurations either have return1/2 or reduce to one connected
integer spectrum by removing unused components and translating its minimum
to0. K1968's pinching and sharp shell formula apply to arbitrary coherent
preparations: a diagonal comparison has no greater return. The new construction
below is diagonal and exactly feasible, so the lower comparison also suffices
for coherent protocols. No independent fit or change of bath is introduced.

For completeness, a three-level connected component carrying a single
population has, after translation, one of

    {0,1,2}@1, {0,1,3}@1, {0,1,4}@1,
    {0,2,3}@2, {0,2,4}@2, {0,3,4}@3.                 (3)

Here @ names the occupied level. These follow directly from the four shell
rank inequalities, or exhaustive gaps1,2,3. In particular its span is at least2,
its occupied energy at least1, and each consecutive gap at most3. The argument
does not silently assume every three-level completion is{0,1,2}.

## 2. Wide spacing forbids interleaving

Every point in the interval[a,a+4] is within1/2 of an energy in the contiguous
five-level component. Thus for delta>1/2 no level of the other component can
lie in that interval. The three-level component also cannot straddle the
interval: any crossing consecutive gap would exceed4, whereas its gaps are
at most3. Hence its whole spectrum lies strictly below or strictly above the
five-level component. Unoccupied ground components cannot occur here because
5+3 already uses the full dimension allowance.

This is the missing arbitrary-real-spectrum step. Integer enumeration alone
would not prove it, and rounding a4.6-offset to5 would raise energy rather
than preserve the budget.

## 3. Both separated orders are dominated constructively

Let the five-level component have mass alpha and normalized probabilities
p,1-p at its two occupied levels. Its normalized return R_A is at most1/2;
the pure component has return1/2. The separated return is

    R_tag = alpha R_A + (1-alpha)/2.                  (4)

**Five-level component below.** Translate its minimum to0. Its conditional
mean energy is3-2p<=3. The upper pure component's occupied energy exceeds5,
so the original total mean is at least3-2p. Use the five-level component
alone, with the same p. It has no greater energy, return R_A<=R_tag, spacing1
and fewer levels.

**Pure component below.** Translate its minimum to0. By(3) its span is at
least2 and occupied energy at least1. The upper five-level component starts
above2. Construct instead the ACTUAL seven-level spectrum{0,1,...,6} with
populations

    at1: 1-alpha,   at3: alpha p,   at5: alpha(1-p).    (5)

Its mean is(1-alpha)+alpha(5-2p), no larger than the original mean. Its shell
ranks satisfy the exact channel requirement. The old five-level return edge
between its populations has difference2 and is retained. The new1-to3 edge
can only add nonnegative inflow in the sharp shell-return formula; it removes
no old inflow. Therefore its sharp return is no larger than(4).
This is a new feasible channel comparison, not a claim that an unchanged
unitary survives an overlapping energy identification.

All original protocols have now been dominated at spacing1, dimension at most8
and no greater mean budget. Inclusion of the spacing1 feasible set gives the
opposite inequality, proving(1). The argument is independent of t and E.
It also proves a useful structural necessity: an eight-level benefit from
subunit spacing must interleave its5+3 components.

## 4. Sharp half-spacing witness and the actual optimum

At delta=1/2 choose pure spectrum{0,1,2} and shifted five-level spectrum
{1/2,3/2,5/2,7/2,9/2}. Their union has eight distinct levels and minimum gap1/2.
Use probabilities

    p(1)=117/187, p(3/2)=28/187, p(7/2)=42/187.        (6)

The exact mean is18/11, shell ranks pass, and the sharp conserving-channel
return is159/374. This corresponds to five-level mass70/187 and its normalized
p=2/5. It is strictly below the connected spacing1 optimum97/220.

K1990's COMPLETE two-template reduction includes delta=1/2. Exact probability-
cell optimization at this budget gives159/374 for the better shifted template;
the other template and all connected shapes are no better. A separately
assembled arrangement-vertex solver recovers the same optimum. Thus(6) is
matched, not merely an upper bound. For delta>1/2, (1) and the previously
certified connected curve give97/220, proving the jump in(2). This agrees with
the earlier lower semicontinuity result: the value at the boundary is below
its right limit. No continuity theorem is assumed.

## 5. Complete finite algorithm and executed temperature consumers

The feasible domain through dimension8 is already known: d>=3, delta<=2,
with E>=1 when delta<=1 and E>=2 when1<delta<=2. Otherwise no protocol exists.
Within it:

- For3<=d<=7 and0<delta<=1, use the connected spacing1 templates of at most d levels.
- For d=8 and0<delta<=1/2, use connected integer templates plus K1990's two actual shifted5+3 spectra.
- For d=8 and1/2<delta<=1, use only the connected spacing1 templates, by(1).
- For1<delta<=2, the attained optimum is1/2, by K1981.

For each finite template, split probability space by the shell-balance and
deficit hyperplanes, then optimize on its rational vertices with the mean
budget. This produces the exact optimum; there is no convexification across
distinct spectra. Rational t,delta,E give rational attained optima. At fixed
rational t,delta the complete budget curve is piecewise affine with finitely
many rational pieces. The source of finiteness is the proved template reduction,
not a finite real-spectrum sample.

The producer executes COMPLETE curves at t=1/3,1/2,2/3, each for delta=1/2
and3/4, using the unchanged complete connected-template bank. This extends
the previous single-temperature computation without claiming a symbolic
formula. The separate solver checks budgets18/11,2,3 for all six curves.
Those checks are independent controls; full-curve coverage comes from the
producer's cell/vertex construction and the structural template proof.

## 6. Verification and remaining frontier

The producer passes1701 actual shell-return/energy dominance controls plus
six complete rational budget programs. The separate probe independently
reconstructs all six three-level completions, seven-level feasibility,198
physical dominance cases and18 fixed-budget optima. Its216 counted
controls pass; four changed shape, spectrum, return and curve coefficients
fail genuine assertions after a clean baseline. Existing connected-template
completeness is reused by exact dependency hash; it is not recounted as a
new exhaustive shape check.

Strongest overclaim: spectral compression preserving an old unitary when
components overlap. Section3 instead constructs a new feasible shell protocol
and proves return domination. Strongest contrary case: delta=1/2, where the
actual witness proves the strict inequality and the boundary exclusion must
remain strict. Weakest remaining seam: closed all-temperature formulas and
dimension9 or higher, where new mass-carrying component types appear. Those
are new classification questions; the all-spacing d<=8 finite reduction is
complete. This supplied thermal model is GU-independent. SC-META-53, source,
physics-ledger and canon verdicts remain unchanged. No novelty, external expert
review or proof-assistant certification is claimed.
