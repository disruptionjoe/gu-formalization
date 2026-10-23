---
title: "K2004: Ten-level thermal spacing frontier"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, source verdict, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2004_ten_level_spacing_frontier.py
  - tests/channel-swings/k2004_ten_level_spacing_frontier_probe.py
---

# K2004: Ten-level thermal spacing frontier

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
result: complete small-spacing ten-level component reduction and exact finite thermal programs
carrier: fixed four-state extreme channel, four-level Gibbs bath and nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance under upper mean energy budget ON=independent_initial_registers
real_structure: complex conserving unitaries and real spectral populations
grading: actual bath resonance components, not physical chirality
action_owner: repository-construction -- unchanged exact thermal model
target: finite-spacing optimal return with at most ten physical levels MAP-TYPE=intertwiner
```

## 1. Complete component reduction

Keep precisely the model, pinching theorem, shell necessity/sufficiency and
sharp diagonal return of [K1996](k1996-positive-spacing-finite-program-2026-10-23.md).
For every temperature ratio `0<t<1`, mean-energy budget `E>=1` and minimum
spacing `0<delta<=1/2`, the optimum `F10(delta,E,t)` equals the minimum of:

1. The complete connected integer spectrum programs with at most ten levels.
2. Eight improving-component/pure-component templates, described below.
3. One template containing two separate five-level ladders, with independently
   optimized populations on each ladder.

The four improving templates are

| Physical spectrum | Occupied support |
| --- | --- |
| 0,...,4 | 1,3 |
| 0,...,5 | 2,3 |
| 0,...,5 | 1,4 |
| 0,...,6 | 1,3,5 |

For each, combine the pure spectrum `{0,1,2}`, occupied at1, and place either
component at offset0 and the other at offset `delta`. This gives eight
possibilities. The ninth consists of `{0,...,4}` and `{delta,...,4+delta}`,
occupied at `1,3,1+delta,3+delta`. Populations are variables: fixing them to
K1998's A/B rays would NOT give the complete program.

### Why there are no missing component partitions

A mass-carrying bath-resonance component needs at least three physical levels;
with `n` levels it supports at most `floor((n-1)/2)` positive populations
(K1966). A component with one occupied level returns1/2. If all components
have that property, the pure three-level mean1 protocol dominates. Otherwise
an improving component needs at least five levels. Three mass-carrying
components would then need at least `5+3+3=11` levels, exceeding ten.
Thus only one component, an improving component of size at most seven plus a
pure component, or two improving components of size five each can matter.
Unused components can be deleted and the remaining spectrum shifted down,
which only improves the upper energy budget.

For one component, use K1996's finite connected integer reduction directly.
For two, enumerate every size5,6,7 connected physical shape with successive
gaps in `{1,2,3}` and every possible occupied subset under the exact shell-rank
inequalities. The complete improving census has107 rows. Every row has an
explicit map to one of the four templates: each occupied energy decreases,
every preexisting occupied gap1,2,3 is preserved, and dimension does not
increase. Triple supports may gain an additional resonant edge. This is safe:
the sharp return is half the sum of positive population deficits; an added
edge contributes nonnegative incoming excess and cannot increase any deficit.
The census therefore proves domination for ALL populations and temperatures,
not just rational controls. Supports without a resonant occupied pair have
return1/2 and need no improving template. A five-level improving component
can only have the first template's gap2 pair.

A pure component is dominated by the physical three-level spectrum0,1,2.
Its occupied energy is at least one above its minimum; reducing it to one
preserves return1/2. This changes no other component before the final
placement. The two original component minima are distinct physical levels,
so their separation is at least `delta`. Set the lower new minimum to0 and
the other to `delta`, after canonical replacement. Every occupied energy
then decreases. Since the shapes are integer and `0<delta<=1/2`, the union's
minimum separation is at least `min(delta,1-delta)=delta`. Their bath shells
remain disjoint, because their offsets differ nonintegrally. Every template
therefore supplies actual nondegenerate energies and exact conserving shell
unitaries, with its unchanged full channel. Both inequalities in the
reduction hold. No convex hull across different spectra is taken.

## 2. Finite exact optimization

The connected enumeration covers29520 shapes,1216 distinct valid occupied
supports and312 Pareto representatives. A second exact reduction leaves only18
connected templates, all with contiguous physical spectra. Each of the294
removed representatives has a direct certificate to a retained template:
same occupied cardinality, no higher occupied energies or physical dimension,
and preservation of every old occupied gap1,2,3. Added edges only improve
return. The independent checker verifies every map directly, so no unproved
transitive pruning or temperature sample substitutes for coverage. This
all-temperature reduction eliminates redundant population programs while
retaining the full arbitrary-integer-spectrum proof.

The finite sign-cell method is
inherited from K1968: incoming excess and positive deficits define finitely
many affine population cells. A cell's projection to energy and return is
convex and its lower boundary comes from vertex pairs. Optimize each physical
spectrum separately and take the lower envelope, including the horizontal
upper-budget rays. Rational inputs give rational minima and actual witnesses.

The exact connected solver visits18 patterns,1242 sign cells and2951
vertices. Its projected-cell lower hulls retain every minimum/maximum energy
endpoint, equal-energy minima, singleton points and horizontal upper-budget
rays. All7916 vertex-versus-supporting-line inequalities pass. This replaces
redundant vertex-pair segments without changing any cell minimum. The final
connected budget curve has16 pieces; the full curve at `t=1/2,delta=1/20`
has11 pieces; the half-spacing curve has14. The machine-readable certificate
records all coefficients and breakpoints in exact rational form.

At `t=1/2`, the two complete small-spacing consumers are

    F10(delta,3/2,1/2) = 9/20 - 9/[200(1+delta)],  0<delta<=1/2;

    F10(delta,2,1/2) = 33/100 + 3delta/[100(1-delta)],  0<delta<=2/5;
                       7/20,                         2/5<=delta<=1/2.

Thus K1998's B-shift branch is valid through the INCLUDED endpoint1/2 at
budget3/2, while its A-shift branch at budget2 stops being optimal immediately
after the INCLUDED exact threshold2/5. The latter is a crossing with the
connected optimum, not a failure of physical feasibility. The complete
227-segment parametric mixed program plus the connected optimum gives228
candidate partitions per budget. Exact feasibility, denominator and objective
roots yield264 and378 feasible interval/boundary checks, respectively. Every
candidate dominates the displayed physical benchmark; no untested competitor
or isolated algebraic boundary is omitted.

| Budget E | delta=1/20 | delta=1/2 | 1/2<delta<=1 |
| --- | --- | --- | --- |
| 3/2 | 57/140 | 21/50 | 97/220 |
| 2 | 63/190 | 7/20 | 7/20 |

The full energy curve at `delta=1/20` differs from the connected curve only
below11/5. In particular, its two middle branches are
`87/140-E/7` on `[6/5,69/40]` and `123/190-3E/19` on
`[69/40,11/5]`; the certificate retains every surrounding branch.

## 3. Complete wide-spacing successor

The same connected program also gives the exact answer for every
`1/2<delta<=1`: `F10(delta,E,t)=F10(1,E,t)` for every `E>=1` and `0<t<1`.
The proof retains the ACTUAL raw small-component shapes before placement;
it does not move to a contiguous replacement prematurely. For each of107
improving raw shapes, consider each of the six pure three-level shapes
`{0,l,l+h}`, occupied at `l`, with positive integers `l,h` and `l+h<=4`,
and both choices of which component has ground0. Include the sole two
improving five-level case. These are1285 cases, all serialized.

Why the pure census is complete: its occupied level's nearest lower and upper
partners cover all four bath labels exactly when their distances sum to at
most four. Deleting other unused levels preserves original spacing. For two
integer shapes A,B, forbidden relative offsets are the OPEN intervals
`(a-b-delta,a-b+delta)`. Their centers are integers. Throughout
`1/2<delta<1`, intervals at adjacent centers overlap, while centers separated
by at least two do not. Consequently the first forbidden block containing0
has a fixed last integer center `n`, and its right endpoint `n+delta` is the
least feasible offset. At `delta=1`, intervals with center gap two merely
touch at an ALLOWED endpoint, so the same result remains valid. At
`delta=1/2` adjacent intervals merely touch, and this argument does not apply.

The initial requirement of an injective map failed on a concrete case:
`A={0,1,4,5,6,7,8}`, occupied at `{1,5,7}`, and
`B={0,1,4}`, occupied at1, with A shifted by `1+delta`.
This was a failure of that replacement method, not a proof against rigidity.
Two occupied source sites have no occupied resonant neighbor. Their separate
return contributions are exactly half their respective masses, so they can
be aggregated at ONE distinct target site whose energy is no higher than
either source energy. They are never merged into an existing edge endpoint.
The old pair remains unchanged. This is an admissible repair at the same
temperature, budget and ten-level bound. Exactly24 of the1285 witnesses use
aggregation. The restriction is necessary: at `t=1/2`, source support
`{1,3,10}` with populations `{1/45,1/5,7/9}` has return22/45. Merging its
isolated mass into the old low edge endpoint yields populations `{4/5,1/5}`
on `{1,3}` and WORSE return1/2. The checker preserves this exact contrary
control; adding mass to an existing edge endpoint is never permitted.

Every case now has an explicit mass-preserving map of ALL source populations
onto one of the18 actual connected target templates. Multiple source sites
may map to one target only when all of them are isolated in the original
occupied-edge graph. Every old edge endpoint retains its own population.
Thus aggregation alone leaves the return sum unchanged; new target edges
can only improve it. Every old within-component
occupied gap1,2,3 is preserved. Every target occupied energy is no greater
than its source's limiting energy at `delta` decreasing to1/2 from above;
therefore it is no greater throughout the wide range. New target resonances
add only nonnegative incoming flow. This proves return and energy domination
for all populations and temperatures. Every target has integer spacing1 and
uses at most ten levels. At `delta=1`, the first-offset union can acquire
cross-component edges. The comparison is to the ORIGINAL actual resonance
components and their original populations; `n+1/2` is only an energy lower
bound. It does not claim to dominate the newly improved return of the merged
first-offset union. Conversely a spacing1 protocol is feasible at every
smaller spacing. These two directions prove equality.

Together with section1 and the reused K1981 result for `delta>1`, this gives
an exact finite-program reduction for ALL positive spacings in dimension ten.
It supplies no all-dimension formula or GU identification. At `t=1/2`, comparison of every rational curve cell proves a strict right
jump at1/2 precisely for budgets

    1029/820 < E < 28/15.

Inside that open interval the jump is
`F10(1,E,1/2) + E/10 - 57/100`; outside it the jump is zero.
At `E=3/2` its exact size is23/1100. At `E=2` there is no half-spacing jump,
but the jump at spacing1 has exact size3/20: the value7/20 becomes1/2 for
`1<delta<=2`, by K1981. At budget3/2 every `delta>1` is infeasible.
For every budget, `delta>2` is infeasible. These statements complete the two
fixed-budget positive-spacing frontiers, including both discontinuity types.

## 4. Verification and scope

The structural reduction is a finite exhaustive proof plus the explicit
all-population incoming-flow argument, not a statistical sample. The
independent checker reconstructs the complete small census, connected
support coverage, physical spacing and shell ranks; independently solves
selected full-budget programs and verifies threshold consumers. The producer
certifies every exact parametric feasibility/objective interval and isolated
boundary point; the independent numerical-free budget solver supplies separate
controls, not an independent complete root-partition replay. An independent
internal review checks the transfer and root-partition argument. The final independent probe passes12477 exact obligations and rejects all
six mathematical faults after a green baseline: missing small component,
missing four-population coverage, spacing collision, wrong budget curve,
wrong threshold and invalid wide population map. Its exact tests also
include the forbidden-merge contrary control, every half-jump energy cell,
and an actual eleven-to-eight-level pure-component merge. Full producer
execution writes the certificate only after all computations pass. No proof-assistant, external review or novelty
claim is made. Source, physics ledger and canon verdicts remain unchanged.

Reproduce from the repository root:

```text
python tests/channel-swings/k2004_ten_level_spacing_frontier.py --write
python tests/channel-swings/k2004_ten_level_spacing_frontier.py
python tests/channel-swings/k2004_ten_level_spacing_frontier_probe.py
```

The producer requires the same SymPy environment as K1968. It supports an
optional `--checkpoint PATH` scratch output of completed exact curves before
the parametric partition; the checkpoint is evidence only and is never
trusted as a substitute for recomputation. Its default replay compares the
entire regenerated object with the checked-in certificate. This run executed
full production and the independent probe; no separate expensive full
producer replay is claimed. The final probe took about15 seconds on the
local interpreter. Earlier redundant all-pair solvers were intentionally
retired after exact structural and lower-hull reductions; a Fraction-to-int
gap adapter repaired an inherited integer-only harness assumption. Those
harness/method events are not mathematical fault-test credits. The concrete
failed injective wide map and the isolated-only repair remain explicit above.

The reduction's `delta<=1/2` hypothesis is essential to the direct placement.
The wide-spacing case uses the separate1285-case proof above. Unbounded
dimensions are not inferred from either reduction.


## 5. Next mathematical boundary

There is a useful dimension-uniform reduction before the next census:
**at most one pure mass-carrying resonance component is needed.** Here pure
means one occupied site. Choose the
existing pure occupied site of least absolute energy. Move every other pure
component's mass onto it, retain its physical component, and delete the other
pure components. Their combined return remains exactly half their total
mass, energy cannot increase, and deleting levels cannot violate the minimum
spacing. Existing improving components and their populations are unchanged.
This merges mass only within the class of pure components, never into an
improving edge endpoint. It proves the same optimum is attainable in the
restricted class, not that every optimizer already has this form.

Consequently dimension eleven's nominal `5+3+3` partition is dominated.
Dimensions eleven and twelve still require at most two useful components.
The next genuinely new dimension-eleven cases are an improving eight-level
component plus a pure three-level component, and improving components of
sizes five and six. The first potentially useful three-component partition
is `5+5+3` at dimension thirteen; three improving components first fit at
fifteen. These are structural lower dimension thresholds, not assertions that
those partitions actually improve the optimum.

The present107-row census stops at improving size seven. It therefore does
not prove the dimension-eleven frontier, even after eliminating extra pure
components. The eighteen-template connected reduction and isolated-mass
aggregation lemma supply reusable methods for that next complete census.
A second concrete successor is the full joint `(E,delta,t)` phase diagram
inside the nine-template small-spacing program; the exact finite reduction
is already proved, while the reported closed formulas fix `t=1/2` and two
budgets. Neither open consumer weakens the complete dimension-ten finite
program or the two exact positive-spacing frontiers proved here.
