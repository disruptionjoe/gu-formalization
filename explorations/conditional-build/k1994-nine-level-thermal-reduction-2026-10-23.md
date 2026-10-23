---
title: "K1994: Complete small-spacing nine-level thermal program"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1994_nine_level_thermal_reduction.py
  - tests/channel-swings/k1994_nine_level_thermal_reduction_probe.py
---

# K1994: Complete small-spacing nine-level thermal program

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
result: complete six-template reduction for small spacing in dimension9 and an attained rational budget curve
carrier: nondegenerate catalyst with at most9 physical levels and fixed four-level Gibbs bath LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitary; coherent preparation admitted through pinching
grading: actual energy resonance components, not source chirality
action_owner: repository-construction -- fixed exact thermal channel
target: dimension and spacing constrained optimal return MAP-TYPE=intertwiner
```

## Result

For every0<t<1, E>=1 and0<delta<=1/2, the exact nine-level optimum
F9(delta,E,t) reduces to connected integer spectra with at most9 levels,
plus SIX actual shifted two-component templates. This extends the complete
dimension8 small-spacing reduction of
[K1990](k1990-small-dimension-thermal-frontier-2026-10-23.md) through the
new6+3 component possibilities. It does not settle delta>1/2 for dimension9.

The improving component is one of

    A={0,1,2,3,4},       occupied at1,3;
    A={0,1,2,3,4,5},     occupied at2,3;
    A={0,1,2,3,4,5},     occupied at1,4.                (1)

Combine each with the pure component B={0,1,2}, occupied at1. Shift either
A or B upward by delta, keeping the other at0. Optimize the actual three
populations with their actual energies. The union has at most9 distinct
levels and spacing at least delta: its gaps include delta and1-delta.
Distinct components have nonintegral offset and no shared bath shells.
These are physical nondegenerate spectra, not colliding tagged limits.

For rational t,delta,E this is a finite rational program with an attained
rational minimum. The full t=1/2,delta=1/20 budget curve is executed in the
JSON:15 exact affine/constant pieces. Selected values are

| E | F9(1/20,E,1/2) | connected-integer comparison |
|---|---:|---:|
|7/5|109/250|325/734|
|18/11|1007/2530|2795/6424|
|2|77/230|7/20|
|3|81/290|81/290|
|4|9/40|9/40|
|5|27/130|27/130|

The terminal plateau is27/130 from E=323/65 onward. These values are exact
program outputs supported by the complete reduction, not fits to samples.

## 1. Exhaust the new mass-carrying partitions

Reuse the exact shell-rank necessity/sufficiency and sharp return formula
of[K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md).
Covariant pinching gives a diagonal comparison no worse than any coherent
preparation. Exact shell constructions attain the diagonal return, so no
coherence restriction is imposed on the lower bound.

Connect energies when their difference is1,2 or3. A connected component is
integer-translated, and different components have disjoint bath shells. A
mass-carrying component needs at least3 levels; a component of n levels has
at most floor((n-1)/2) occupied energies. Thus components with at most4
levels have one population and return1/2. If all components are of that
kind, the standard three-level pure protocol at mean1 dominates.

Otherwise dimension9 permits only5+3,5+4, or6+3, besides all mass in one
component. In the latter case delete unused components and translate the
occupied component to0. Its integer spectrum can be compressed by replacing
consecutive gaps exceeding3 by3: no original resonance is lost, energy drops,
and any newly coincident total-energy shells accept the direct sum of the
old conserving unitaries. The distinct catalyst levels remain ordered and
integer-spaced. This is the protocol-preserving compression already proved
in[K1984](k1984-commensurate-spectral-rounding-2026-10-23.md), now with9 levels.

A5- or6-level improving component has exactly two occupied energies. If
their separation exceeds3 their occupied shells are disjoint and return is
1/2, so it cannot improve. Enumerate every connected5/6-level shape: after
translation its consecutive gaps lie in{1,2,3}. Impose the four-bath shell
rank inequalities on every candidate pair. Exactly17 spectrum/support pairs
remain. Their COMPLETE list is in the JSON. Their possible occupied gaps
are1,2,3, and the least lower occupied energies are respectively2,1,1.
The corresponding actual contiguous completions are precisely(1).

This finite exhaustion is an exact computational proof at this dimension.
It is not merely random sampling; an independent enumeration reconstructs
all17 pairs. Support locations are preserved up to translation, so normalized
return at any temperature is unchanged. Replacing an original component by
its corresponding minimal template decreases its occupied energies and uses
no more levels. A pure3/4-level component has occupied energy at least1
above its minimum and is similarly dominated by B.

## 2. Arbitrary-real placement is dominated by an actual template

Let a,b be the minima of the improving and pure components. After deleting
unused components and translating the union down, one minimum is0. Since
these are distinct physical energy levels, the other is at least delta.
The component replacements above lower occupied offsets relative to these
minima. If a=0, place the replacement B at delta; if b=0, place replacement
A at delta. This decreases BOTH relevant energy coefficients, preserves the
normalized component returns and all component masses, and uses at most9
levels. Because delta<=1/2, the resulting interleaved template actually has
the required spacing. Therefore every original real-spectrum protocol is
dominated by one of the six templates, a connected template, or pure B.

This argument handles unused ground levels too: remove them before resetting
the ground; the preparation mean can only decrease. An inactive component
never consumes a necessary level in an at-most-dimension problem. Conversely,
every template has a valid exact shell implementation. The two inequalities
prove equality of the template optimum with F9 for the stated parameter range.
No convex hull across different spectra is taken; each probability polytope
is optimized separately, then their values are minimized.

## 3. Exact computation and released consumer

The connected enumeration covers9837 gap words at sizes3--9,516 distinct
valid supports, and122 Pareto representatives. The connected probability
arrangements contain1726 cells and2921 counted vertices. The six shifted
families are optimized with actual rational energies; the unchanged shell
balance and deficit equations split each probability simplex into affine
cells. Projecting their vertices and edges to(mean,return) and taking the
lower envelope computes the COMPLETE budget curve. The upper-budget ray
is included, and no positive-slope segment is treated as obligatory spending.

All15 pieces, every breakpoint and both the connected and mixed curves are
serialized. For example E=3 gives81/290, strictly below dimension8's9/32 at
the same spacing and temperature. For E>=323/65 the nine-level plateau27/130
is below dimension8's9/38. Thus a real ninth level gives a certified benefit;
this is not just a larger enumeration with unchanged optimum. At E=7/5 the
optimum remains109/250, so extra dimension does NOT uniformly improve every
budget. The JSON also carries the complete piecewise-affine ninth-level benefit
over dimension8; every endpoint and an interior point per piece are checked
against both exact curves. These comparisons reuse the complete dimension8 curve, not a loose
upper witness or a comparison at a different temperature.

## 4. Verification and remaining boundary

The separate checker enumerates all9837 shapes independently, proves every
raw valid support is dominated by a stored representative, checks every
shifted spectrum's nondegeneracy/spacing/shell rank, and independently solves
fixed-budget arrangement programs at E=7/5,2,3. Its coverage, physical, optimization and dimension-benefit obligations
pass; four missing-component, missing-four-population, collision and curve
faults fail actual mathematical assertions after a green baseline. The
producer's exhaustive cell/envelope construction proves full-curve coverage;
three independent budget checks alone do not prove that full curve.

Strongest overclaim: transferring low-spacing placement to delta>1/2, where
interleaving violates spacing. The six-level census also contains noncontiguous
completions, so dimension8's wide-spacing proof cannot be copied unchanged.
Strongest contrary case is this new geometry; preserve it for a dedicated
placement/dominance test. The exact full dimension9 wide-spacing frontier and
symbolic-temperature closed formula remain open. This supplied thermal model
is GU-independent; SC-META-53, source, physics-ledger and canon are unchanged.
Same-author separate implementations are internal checks, not independent
expert review or proof-assistant certification. No novelty claim.
