---
title: "K2006: Uniform two-component thermal spacing theorem"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, source verdict, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2006_uniform_two_component_spacing.py
  - tests/channel-swings/k2006_uniform_two_component_spacing_probe.py
---

# K2006: Uniform two-component thermal spacing theorem

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
result: all-dimension two-component spacing reduction, linear spectral box and universal jump locations
carrier: fixed four-state extreme channel, four-level Gibbs bath and finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance under upper mean-energy budget ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real ordered energy populations
grading: actual bath resonance components, not source chirality
action_owner: repository-construction -- unchanged exact thermal model
target: dimension-uniform positive-spacing resource frontier MAP-TYPE=intertwiner
```

## Result and dependency boundary

Every finite protocol in the unchanged K1981/K1996 model is dominated by one
with at most **two populated physical resonance components**, even at fixed
positive minimum spacing. For any finite dimension, a complete canonical
two-shape program replaces arbitrary component partitions and interleavings.
For spacing at most one, an equally good representative fits in
`[0,3(d-1)]`. Interior spacing discontinuities can occur only at `1/2` and
`1`; the boundary at `2` leads to infeasibility. A further consumer improves
K1998's dimension-dependent energy-transfer cost to at most `delta/2`.

The two-component linear-programming theorem is **already proved in
[K1972](k1972-thermal-two-component-reduction-2026-10-22.md)**. The new result
is its spacing-preserving transfer, canonical placement consequences and the
resulting uniform geometry and parameter conclusions. These do not evaluate
the optimal return in every dimension.

This also corrects a prospective inference in K2004 section5 and the former
current-state continuation: `5+5+3` at dimension13 and `5+5+5` at dimension15
cannot create a *necessary* three-component optimization regime. The pure
component merging lemma and the dimension-ten results remain valid; K1972's
stronger argument simply eliminates all three-component families, including
ones with no pure component. No existing numerical frontier is withdrawn.

## 1. Model and opening specialist checks

Let `F_d(delta,E,t)` denote the optimal return with at most `d` nondegenerate
catalyst levels, ground zero, minimum adjacent energy gap `delta>0`, upper
initial mean energy `E`, bath energies `0,1,2,3` and Gibbs weights
`t^b/Z(t)`, `0<t<1`. The target remains the exact extreme four-state channel;
the return is the worst-input **marginal** half trace distance. Coherent
initial preparations are covered by the inherited covariant pinching theorem.
Neither approximate conservation nor approximate channel simulation is admitted.

Opening checks, with their mathematical burdens made explicit:

- **Quantum information:** use the inherited sharp shell construction whose
  worst-input return is common across input states. Do not exchange a general
  supremum with a sum. Retain all physical completion levels of each component.
- **Finite optimization:** reweight actual component preparations, charging
  summed physical dimensions. Population faces with zero coordinates remain
  admissible; a selected sign cell is not the complete probability simplex.
- **Discrete geometry:** forbidden spacing intervals are open, so touching
  endpoints are allowed. Integer shapes need not be contiguous ladders.
- **Parameter analysis:** a minimizing family can disappear at an energy
  threshold; continuity needs an explicit energy repair or the pure baseline.
- **Source criticism:** this is a conditional finite thermal construction.
  Source identification, physical GU states and functional measures are absent.

Layer0 identifies the exact finite model with the one being proved about;
there is no bridge to a source-native GU action or new substrate candidate.

## 2. Transfer of the existing two-component theorem

After pinching and sharp shell optimization, write the actual populated
resonance components as `C_j`. Freeze each component's full physical spectrum,
normalized preparation, mean energy `e_j` and sharp return `r_j`. Its total
population is `w_j`. The inherited formula gives

    mean = sum_j w_j e_j,   return = sum_j w_j r_j,
    sum_j w_j=1,   w_j>=0.

K1972 minimizes the second expression under the same energy budget. An
optimal extreme point has at most two positive weights. Equivalently, on
three positive entries choose a nonzero direction with zero total mass and
zero energy moment; choose its sign not to increase return, then move until
one entry vanishes. This also handles equal component means.

Crucially, this changes **no energy level** in any surviving component.
Delete only entire zero-weight components, including their unused completion
levels. Deletion cannot decrease the remaining minimum gap. If the original
ground was deleted, translate all surviving levels down by their minimum:
spacing, conservation and return are unchanged, while mean energy decreases.
Physical dimension cannot increase. Therefore K1972's dominance theorem
holds unchanged for every positive spacing. It restricts the class needed
to attain the optimum; it does not say every optimizer has only two components.

The inherited sharp construction, not an assumption about arbitrary unitaries,
supplies additivity. No free classical flag, collision limit or uncharged
additional register occurs in this transfer.

## 3. Exact canonical placement of two integer shapes

A connected bath-resonance component has energies `x+A`, with minimum-zero
integer shape `A`; successive sorted shape gaps lie in `{1,2,3}`. Otherwise
the gap disconnects it. Thus `max A<=3(|A|-1)`. A populated component's valid
occupied support satisfies the inherited shell-rank inequalities. Its sharp
return depends on its populations and internal occupied gaps, not its offset.

For two retained components, translate their smaller minimum to zero and
call its shape `A`; let `B` be the higher shape. Original relative offset
`x` is at least `delta`. Both orientations must be retained in a complete
program. Shape replacement is not needed and no contiguous-shape conjecture
is used.

The forbidden offsets are exactly

    union_{c in A-B} (c-delta,c+delta).

Here `A-B` is a finite integer set containing zero. For `0<delta<=1/2`,
the least nonnegative allowed offset is exactly `delta`: its distances from
integer centers are at least `min(delta,1-delta)=delta`. For
`1/2<delta<=1`, define

    n(A,B)=max {n>=0 : 0,1,...,n all belong to A-B}.

The least offset is exactly `n(A,B)+delta`. Adjacent forbidden intervals
overlap when `delta>1/2`. The first missing integer center ends their initial
block. Centers separated by two leave a gap for `delta<1`; at `delta=1`
they merely touch at an **allowed** endpoint. This proves the formula with
both endpoint conventions. Negative centers cannot extend this block past
the last consecutive nonnegative center.

Replace the original relative offset by this least allowed value. It is
no larger than the original feasible offset, so every level's energy weakly
decreases. For `delta<1` the new relative offset is nonintegral: the original
internal resonances are preserved and no cross-component resonance appears.
Thus the exact channel and sharp return are unchanged, with no higher mean
energy or physical dimension.

At `delta=1`, new cross-component resonances may appear. The old orthogonal
unitary blocks can still be embedded block diagonally inside the enlarged
shell, preserving their previous channel and return. Reoptimizing the actual
new shell can improve return. One must **not** assert equality of old and
new sharp returns there. A concrete strict-improvement control is included
in the certificate.

## 4. Complete finite programs and a linear representative box

For any finite `d` and `0<delta<1`, take:

1. Every connected integer shape with at most `d` levels and its valid supports.
2. Every ordered pair of such shapes with summed physical sizes at most `d`,
   placed at offsets zero and the value in section3, with valid supports in
   each component.

Each shape family is finite: its successive gaps are chosen from `{1,2,3}`.
Within a support, optimize the full population simplex under its one energy
inequality, using the inherited continuous piecewise-linear sharp return.
Finite sign-cell linear programs compute this minimum exactly. Zero masses
are permitted; deleting an occupied support site weakens shell-rank demands
and preserves physical implementability. Padding levels are still charged.

Every original protocol is dominated by one of these programs, and every
program describes an actual admissible spectrum and shell construction.
These two inequalities prove completeness. At `delta=1`, the canonical
union is itself connected: the center `n` belongs to `A-B`, so at offset
`n+1` a cross-component pair has gap one. Both shapes were internally
connected. Thus the connected integer programs alone give the optimum at
one. Optimize their **actual** resonances; do not use a frozen noninteger
return formula or assert preservation of the old sharp value.
For `delta>1`, use the already complete K1981 answer. This is a finite
algorithm, not a practical complexity claim or an executed all-d frontier.

There is a useful stronger bound. Since `n(A,B)<=max A`, the pair span is

    max(max A, n+delta+max B)
      <=3(|A|+|B|-2)+delta <=3(d-2)+delta.

The small-spacing placement satisfies the same bound. For `delta<=1` this
is below `3(d-1)`, while every connected shape already has span at most
`3(d-1)`. Thus every feasible protocol has an equally good or better
representative in **`[0,3(d-1)]`**. K1978's compactness and attainment are
reused, not rediscovered; the smaller box follows from the two-component
transfer. No positivity of spacing is discarded when taking compact limits.

## 5. No interior spacing jumps away from one half and one

Fix `d>=3`, `E>=1`, `0<t<1`, and an interior point `delta0` of either
`(0,1/2)` or `(1/2,1)`. There are finitely many canonical families, and each
family's occupied energies have the form `a_i+b_i delta`, with `b_i` zero
or one. Its resonant graph and return function are constant with respect to
delta inside that regime. Its full valid-support simplex is fixed.

Choose a canonical optimizer at `delta0`; existence follows from K1978 or
from the finite compact programs. Write its populations as `p`.

- If its mean is strictly below `E`, unchanged populations remain feasible
  under sufficiently small parameter changes.
- If its mean equals `E` and its minimum occupied energy is strictly below
  `E`, choose a minimum-energy site `i`. At nearby `delta`, let `e'(delta)`
  be the mean of unchanged `p`, and `a'(delta)` that site's energy. Whenever
  `e'>E`, use

      theta=(e'-E)/(e'-a'),
      p'=(1-theta)p+theta unit_i.

  Then `theta->0`, the new mean equals `E`, and the full-simplex return
  converges to its old value. If `e'<=E`, no repair is needed.
- If the minimum occupied energy equals the mean `E`, nondegeneracy forces
  a singleton preparation. Its sharp return is exactly `1/2`. The actual
  pure spectrum `{0,1,2}`, prepared at1, has that value throughout the entire
  neighborhood, regardless of whether the chosen singleton family disappears.

Every sharp return is at most `1/2` in the feasible simplex, because retention at
each occupied site is at least half its original population. Consequently
the last case also covers any optimum already equal to the pure baseline.
These constructions prove upper semicontinuity of the global optimum.
K1987's inherited lower semicontinuity gives continuity. At `E=1`, use the
pure-baseline argument directly; no division by `E-1` is made.

It follows for every finite dimension that the only possible spacing jumps
inside the feasible range are at **`delta=1/2` or `delta=1`**. The existing
K2004 example at one half and K1981 example at one show that both locations
really can occur. There is no claim that every dimension, budget or
temperature exhibits both. Above one the feasible value is identically
`1/2` through two when `E>=2`; beyond two it is infeasible. For `1<=E<2`,
infeasibility already starts immediately above one.

This strengthens K1987's finite-but-unspecified jump set. It does **not**
prove all-dimension constancy in the wide interval `(1/2,1)`: a continuous
nonconstant frontier there remains possible. Crossings between population
branches can create corners, which are not jumps.

## 6. Improved uniform small-spacing transfer

Let `V_d(E,t)` be the **unspaced nondegenerate infimum**, not a value obtained
by permitting coincident physical levels. K1998 already proves a spacing
transfer with cost `c_d delta`, where `c_d=max(0,floor((d-5)/3))`, and range
`delta<=1/(c_d+1)`, together with the flat-or-linear local law. Those earlier
qualitative and asymptotic results are not claimed again here.

The new two-component transfer gives, for every finite `d>=3`, `E>=1` and
`0<delta<=1/2`,

    V_d(E,t) <= F_d(delta,E,t)
      <= V_d(max(1,E-delta/2),t).                         (1)

To prove the upper bound for `E>=1+delta/2`, choose any unspaced actual
protocol with energy at most `E-delta/2`, arbitrarily close to its infimum.
Apply K1972 to reduce it to two populated components, then normalize each
integer shape to its own minimum zero. This only lowers mean energy. Keep
the heavier component at offset zero and shift the lighter by `delta`.
Section3 makes their union an actual nondegenerate spacing-delta spectrum.
The energy increase is `delta min(w,1-w)<=delta/2`, with return unchanged.
If only one component remains, no shift is needed. Take the infimum of
these feasible values. For `1<=E<1+delta/2`, the pure mean1 baseline proves
the displayed bound because `V_d(1,t)=1/2`. Inclusion supplies the lower bound.

Thus, using K1998's finite maximum absolute slope `L_d(t)` of the continuous
piecewise-affine unspaced curve,

    0 <= F_d(delta,E,t)-V_d(E,t) <= L_d(t) delta/2,       (2)

uniformly over all `E>=1` for each fixed `d,t`. The **energy-transfer factor
and spacing range** are dimension-independent; no dimension-independent
bound on `L_d(t)` is asserted. The coefficient one half is a sufficient
transfer bound, not a claim of a sharp global return slope. Existing rigidity
at small dimensions can give a better bound. Unequal-mass controls pay the
actual smaller shift cost, and zero-weight components are deleted.

## 7. Verification, contrary cases and closing specialist assessment

The producer and separate probe are standard-library exact rational programs.
Geometry controls exhaust ordered pairs of integer shapes with one through
four physical levels, plus selected larger shapes. These test the placement
formula; they do not substitute for section3's all-dimension proof. Actual
13-level `5+5+3`, 15-level `5+5+5`, and equal-component-mean examples exercise
the physical weight reduction at several temperatures. The independent
probe reconstructs bath shells and returns by direct bath-label maxima,
rather than the producer's incoming-excess formula. Exact energy-repair and
lighter-component-shift consumers test the parameter arguments.

Contrary cases retain the reasons tempting stronger statements fail:

- Moving isolated mass into an existing edge endpoint can worsen return
  from `22/45` to `1/2`; component reweighting is not that operation.
- A singleton family can disappear at an interior energy threshold; the
  unchanged global pure competitor, not familywise continuity, repairs the proof.
- At spacing one new resonances can strictly improve sharp return. Old block
  preservation gives feasibility and dominance, not equality of sharp formulas.
- Distinct component dimensions add; using their maximum undercharges the
  physical catalyst.

At `t=1/2`, the actual reduction consumers give:

| Original component sizes | Retained physical dimension | Original mean | Final mean | Original return | Final return |
| --- | --- | --- | --- | --- | --- |
| `5+5+3` | 8 | `26/15` | `26/15` | `13/30` | `5/12` |
| `5+5+5` | 5 | `2` | `9/5` | `17/40` | `2/5` |
| `5+5+5`, equal component means | 5 | `2` | `2` | `49/120` | `7/20` |

All keep spacing at least `1/5`. They are feasible dominance witnesses,
not claims of global optimality in dimensions13 or15. The component-weight
optimization on each frozen example is separately certified by a matching
linear-programming dual lower bound.

The final producer completes full production and a separate full replay:
24,000 exact geometric obligations over8,000 shape/spacing combinations,
nine actual physical component reductions, nine exact energy repairs and
30 lighter-component transfers. The final independent probe passes24,000
geometric obligations and517 physical/consumer check groups. It rejects
eight mathematical corruptions after a green baseline: component mass,
least offset, summed dimension, unpaid repair energy, frozen endpoint return,
an actual heavier-component shift, free shift cost, and component return.
Six input hashes are checked separately as provenance, not theorem evidence.

Independent internal review checked the written transfer, endpoints,
continuity and half-spacing bound and the separate implementation. That
review caught an initially label-only heavier-shift mutation. It was replaced
by an actual changed spectrum, support, populations, mean and cost; the
complete probe was rerun and rejected that physical error through its energy
identity. The earlier label-only test receives no mathematical-fault credit.
There were no changes to the mathematical baseline from this harness repair.

Closing specialist assessment: the quantum-information transfer retains the
same channel and explicit shell ownership; the optimization argument uses
whole simplices and exact costs; the geometric proof treats both threshold
endpoints; the continuity proof handles disappearing families and `E=1`;
the source lens permits only conditional internal mathematical credit.
The universal theorems rest on these written proofs and reused exact shell
results. Finite tests, certificate hashes and prose checks have narrower roles.
No proof-assistant acceptance, external expert review or novelty claim is made.

Reproduce from the repository root:

```text
python tests/channel-swings/k2006_uniform_two_component_spacing.py --write
python tests/channel-swings/k2006_uniform_two_component_spacing.py
python tests/channel-swings/k2006_uniform_two_component_spacing_probe.py
```

SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b and AC-F1 remain NEEDS. Source,
physics-ledger and canon verdicts are unchanged. Larger connected-support
programs and the possible all-dimension wide-spacing rigidity remain open;
additional three-component cases are no longer a necessary successor.
