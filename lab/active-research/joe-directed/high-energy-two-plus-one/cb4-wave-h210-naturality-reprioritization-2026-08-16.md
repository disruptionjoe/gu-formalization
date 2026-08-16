---
artifact_type: exploration
status: exploration
doc_type: conditional_build_wave_synthesis_and_reprioritization
created: 2026-08-16
work_item: CB-4-WAVE
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-4 synthesis: H210 rank descends under co-moving observation, fixed Pati--Salam does not, and twistors expose the four-dimensional F/Q split as the next gate"
grade: "EXACT scoped synthesis of the finite K77/Spin naturality square, fixed-versus-co-moving Pati--Salam obstruction, twistor/pure-spinor archaeology, and fifteen-lens hostile review. CONDITIONAL on H210. H210-ALIGN and H210-PSRED are separate declared horns. No source action, selected graph/background, external datum, family-row fit, physical quotient, mass, scale, threshold, or observable is derived."
disposition: FINITE_H210_NATURALITY_PASSES__RANK_AND_KERNEL_DESCEND_ON_ADMITTED_OVERLAPS__FIXED_PS_EXCLUDED_FOR_NONZERO_GRAPH__COMOVING_PS_REQUIRES_H210_PSRED__TWISTORS_DO_NOT_SUPPLY_REDUCTION__DECORATED_4D_CLIFFORD_SPLIT_NEXT
canon_verdict_change: none
steering_effect: "Keep H210 first for one more exact conditional-build swing. Compute the co-moving four-dimensional Clifford-trace/gamma-traceless split F_J^tr/Q_J^RS of the contracted port, with Pi_4 distinct from Pi_14 and source-F provenance fenced by H210-ALIGN. Carry H210-PSRED as an assumption rather than attempting to derive it."
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-wave-h210-observation-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-h210-finite-comoving-naturality-square-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-h210-fixed-versus-comoving-ps-typing-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb4-h210-naturality-review.md
  - explorations/conditional-build/selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md
  - explorations/conditional-build/selected-k77-twistor-carrier-weyl-integrability-gate-2026-08-14.md
  - explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md
scripts:
  - tests/channel-swings/joe_directed_cb4_h210_comoving_naturality_probe.py
  - tests/channel-swings/joe_directed_cb4_h210_ps_observer_typing_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This wave tests
> Weinstein's F/Q/Z, `2+1`, imposter, Pati--Salam reunification, and emergent-
> chirality proposal on the banked GU carrier. Ordinary family indices, net-
> chirality arguments, scalar-Higgs VEVs, and conventional `SO(10)` mass
> mechanisms are controls only and do not adjudicate this mechanism without a
> typed bridge.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Horn `H210` is assumed. `H210-ALIGN` and `H210-PSRED` are independent
> conditional inputs. Deriving or varying an action, choosing a graph,
> vacuum, background, or section, fitting a family row, or importing an
> external datum is outside this channel.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-4 wave synthesis — co-moving H210 naturality

## Outcome first

The H210 conditional chain survives the co-moving observation test, but it
does not preserve one fixed Pati--Salam embedding.

1. The finite K77/Spin square commutes exactly when the graph, ambient
   covector, Clifford frame, output spinor, domain spinor, and horizontal
   coframe all move with their correct variances.
2. Therefore pointwise rank and kernel dimension descend for the declared
   associated-bundle morphism on admitted graph/Spin overlaps. Its component
   matrix remains local-frame and Spin-lift dependent. This is not a global
   topology theorem or a physical observation.
3. A nonzero observer tilt cannot preserve the reference Pati--Salam subgroup:

   ```text
   V_10 |_PS = (6,1,1) + (1,2,2),
   Hom_PS(H_4,V_10) = 0.
   ```

4. A chosen co-moving subgroup `PS_J=g_J PS g_J^-1` preserves the transported
   H210 map's equivariance by covariance. The graph projector does not choose
   that subgroup. Global subgroup typing therefore needs the separate declared
   horn

   ```text
   H210-PSRED = observer-normal overlaps reduce at least to N(PS),
                with a principal PS reduction requiring PS-valued overlaps.
   ```

5. Twistor geometry does not supply `H210-PSRED`. It does reveal a more direct
   next test: split the observed covector-spinor into its four-dimensional
   Clifford-trace and gamma-traceless components, and ask whether the H210
   connector reaches the F-shaped carrier slot associated with equation
   (12.22).

In plain English: the connector is not an artifact of the observer coordinates.
It has an invariant rank when everything is transported together. But the
observer motion also moves the internal subgroup labels, and neither the graph
nor the existing twistor structures choose how Pati--Salam moves. Rather than
trying to manufacture that missing choice, the next useful conditional test is
whether the surviving connector actually lands in the kind of four-dimensional
spinor slot that Weinstein calls the imposter.

## Inline pre-flight and archaeology result

Root's pre-flight used source-fidelity, ledger archaeology, representation,
carrier/corner, Clifford/real-form, operator-grammar, naturality, principal-
bundle, emergent-chirality, family-symmetry, twistor/pure-spinor, and
falsification lenses.

The archaeology prevented three inefficient turns:

- the graph-atlas and Cartan/Spin artifacts already owned the fractional graph
  law and finite lift grammar, so the wave tested the composed square rather
  than rebuilding a preferred lift;
- `10|_PS=(6,1,1)+(1,2,2)` already implied the fixed-PS obstruction once the
  observer tilt was typed as `H_4 -> V_10`; and
- the twistor seven-gate already separated base twistors, the normal twistor
  orbit, and the spinorial `J10`, while recording that no base--normal incidence
  map is constructed.

The lane remained a conditional build throughout. Missing action, background,
section, family row, reduction, and external datum stayed dependency fences;
none became an execution target.

## Exact finite naturality result

For a finite K77 transformation in blocks relative to `H+V`, write

```text
g = ((a,b),(c,d)),
L_J=(I,J)^T,
A=a+bJ,
J'=(c+dJ)A^-1.
```

If the ambient covector-spinor is transported by

```text
T'=(g^-T tensor S(g))T,
```

then the exact square is

```text
L_(J')^T T' = A^-T S(g)(L_J^T T).
```

A co-moved domain spinor appends the same invertible right factor to both
sides. Across three mixed Cayley transitions and two exact fields, all tested
flat, isotropic, and banked-receiver squares commute. On each real ambient K77
Weyl half the co-moving ranks are:

| stratum | rank | meaning |
|---|---:|---|
| flat | `0` | a co-moved pure-normal port stays unobserved |
| totally isotropic two-plane | `48` | the signature-sensitive partial rank descends |
| banked receiver | `64` | full real-half rank descends; internal-complex rank is `16` |

For a declared nonzero `r in M_3*`, the banked family-input kernel remains
`ker(r) tensor 16`, complex dimension `32`. Both conjugate halves are carried.
The four wrong transports—frozen tensor, missing graph denominator, vector
instead of covector action, and frozen Clifford frame—fail in both exact
fields.

The invariant datum is rank/kernel of an associated-bundle morphism. A
preferred component matrix, preferred O/Spin lift, physical quotient, or
selected observer is not produced.

## Fixed versus co-moving Pati--Salam

Because `H_4` is PS-trivial and `V_10` has no PS singlet,

```text
Inv_PS(V_10)=0,
Hom_PS(H_4,V_10)=0.
```

Thus only `J=0` preserves the fixed reference embedding. This kills the horn
"nonzero observer tilt with unchanged PS," not H210 itself.

For a chosen graph lift, simultaneous conjugation gives exact local
equivariance. But `g_J` and `g_J k`, with `k in O(H_4) x O(V_10)`, determine the
same graph projector and generally different conjugate PS subgroups. Without
`H210-PSRED`, only the imported embedding's conjugacy type is lift-independent.

The three H210-related horns now have distinct jobs:

| horn | conditional role | not supplied by |
|---|---|---|
| `H210` | nonzero 210-owned family-to-partner port | this lane's action or dynamics |
| `H210-ALIGN` | identify `M_3/ker(r)` with source F/imposter provenance | rank, naturality, or PS covariance |
| `H210-PSRED` | type the moving normal-frame cocycle at least through `N(PS)` | graph projector, covariance, or twistor orbit |

These may be assumed for downstream compatibility tests. Deriving any of them
is off limits here.

## What the twistor lens changes

Three structures must remain separate:

| structure | carrier | what it owns |
|---|---|---|
| base twistor | complex two-plane in `S_L + S_R* ~= C^4` | observed conformal incidence and tangent adapter |
| observer graph | nondegenerate real `H_4 -> V_10` graph | the K77 `4+10` contraction and its fractional atlas |
| normal twistor | `J_N in O(6,4)/U(3,2)` | an orthogonal complex-structure reduction of the normal ten-plane |

No repository-owned adapter identifies the base-twistor graph with the K77
observer graph. The normal twistor cannot canonically produce a PS reduction:
an equivariant map from `O(6,4)/U(3,2)` to `O(6,4)/N(PS)` would require a
conjugate containment of a dimension-`25` stabilizer in a normalizer whose
identity component has dimension `15+6=21`.

Twistors instead contribute the exact post-contraction projector grammar. For

```text
A_J = O_J T : S -> H* tensor S,
```

define

```text
F_J^tr = (1/4) j_4 Gamma_4 A_J,
Pi_4   = I - (1/4) j_4 Gamma_4,
Q_J^RS = Pi_4 A_J.
```

Then

```text
A_J = F_J^tr + Q_J^RS,
Gamma_4 Q_J^RS = 0.
```

The decorations are mandatory. `F_J^tr` is the four-dimensional Clifford-
trace, F-shaped carrier component; it is not yet Weinstein's source-labeled
F/imposter provenance. `Q_J^RS` is the four-dimensional gamma-traceless
component. `Pi_4` acts after contraction and is not the ambient `Pi_14`.
Prior art proves `Pi_4 != Pi_14`, while an already `Gamma_4`-traceless input
has a positive adapter into ambient `ker Gamma_14`.

The hostile reviewer obtained a one-field preview—non-authoritative until the
next two-field certificate—in which the banked receiver has full rank in both
projected maps. This warns that projected ranks are not additive family
counts. The invariant relation to certify is

```text
ker(A_J) = ker(F_J^tr) intersection ker(Q_J^RS).
```

## Hostile-review result and claim ceiling

The fifteen-lens review independently replayed CB-4A (`39/39`), CB-4B (`36`
checks and `5/5` plants), and the twistor-projector prior art (`50/50`). It
upheld the finite square, the fixed-PS obstruction, the subgroup-lift
ambiguity, both-half and family kernels, the contracted codomain, and
`Pi_4 != Pi_14`.

No algebraic repair to either CB-4 probe was required. The mandatory
integration repairs are the explicit `H210-PSRED` horn, local/conditional
descent language, decorated F/Q names, the source-provenance fence, and the
non-additivity of projected ranks.

CB-4 does not derive a source action, observer graph, background, section,
family row, PS reduction, physical quotient, luminous sector, named family,
mass, scale, threshold, domain, positivity, observable, or phenomenology. It
does not restore a free observed `144`. Canon and public posture do not move.

## Reprioritization

| path-relative item | priority | fertility | decision |
|---|---:|---:|---|
| co-moving `F_J^tr/Q_J^RS` split of `O_JT` | 1 | `9/10` | run next over two fields, flat/isotropic/banked strata, both halves; preserve source-provenance fence |
| `H210-PSRED` normalizer-cocycle descent | 2 | `5/10` | carry as a declared horn; do not try to derive it from action, graph, or twistor data |
| full off-diagonal `d0+varpi` composition | 3 | `5/10` | enter only after the F/Q carrier split; derivative-half collision remains live |
| physical quotient against mirrors/B5 extras | 4 | `3/10` here | necessary later, but substantially overlaps the hourly action/domain path |
| full twistor/Bach/Penrose route | deferred | `2/10` here | requires connection, curvature, domain, and cohomology inputs outside this conditional lane |
| preferred finite O/Spin lift | retired | `0/10` | gauge representative, not missing geometry |
| fixed PS at nonzero `J` | killed | `0/10` | excluded by `Hom_PS(H_4,V_10)=0` |
| derive action, selector, section, family row, or external datum | off limits | not scored | violates the conditional-build contract |

Relative to the wider non-hourly portfolio, H210 remains the best beat for one
more bounded wave. Its finite naturality falsifier passed, and the twistor-
informed F/Q split is cheaper and closer to the source's imposter statement
than global reduction or physical-quotient work. If the exact co-moving split
finds `F_J^tr=0` on every intrinsic nonzero stratum, demote H210 below SN-1 as
an explanation of the source's imposter appearance. A nonzero `F_J^tr`
strengthens only carrier fit; `H210-ALIGN`, `H210-PSRED`, both halves, fixed
trace-`H_q`, the full `d0+varpi` collision, and physical reduction remain.

## Next scaffold

The next `Go` wave should assume `H210`, carry `H210-ALIGN` and
`H210-PSRED` as separate declared horns, and compute the decorated split in the
same finite naturality packet:

1. construct `Gamma_4`, `j_4`, `Pi_4`, and separately `Pi_14`;
2. prove the split, gamma-trace identity, projector idempotence, `Pi_4 !=
   Pi_14`, and the positive adapter;
3. replay flat, isotropic-two-plane, paired-null/non-null, and banked-receiver
   strata over both current exact fields and both ambient halves;
4. report ranks, kernels, family kernels, and their intersections without
   adding projected ranks;
5. commute both projected maps through the finite co-moving square, moving the
   horizontal Clifford frame and retaining the right-domain spin transport;
6. fire hostile plants for source-F promotion, projector substitution, frozen
   gamma frame, deleted conjugate half, promoted `H210-ALIGN`, and additive
   family counting; and
7. stop before action, Bach/Yang--Mills, Penrose transform, physical quotient,
   mass, scale, threshold, or observable.

## Successor status — CB-5 banked

CB-5 completed the decorated four-dimensional split. The horizontal F/Q maps
commute in the tested co-moving squares on both ambient halves. Exact rational
counterexamples prove that projected ranks are not determined by raw rank;
the banked full/full/full result is generic only in the declared affine
coefficient family.

The source bridge also sharpened. H210 starts in the Z/internal-partner sector
and has zero upstream correlated-F projection. Observation can create a
horizontal trace, which has a unique pointwise completion into the correlated
equation-(12.22) F carrier relative to the declared split. That construction
does not recover the consumed H210 normal leg and is not yet a full co-moving
horizontal/normal natural transformation. The successor read packet now names
`H210-FCORR`, `H210-ALIGN`, and `H210-PSRED` as three independent declared
horns. CB-6 owns the full correlated-lift naturality and off-diagonal operator
composition gates; further rank sampling is retired.
