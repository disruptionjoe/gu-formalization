---
artifact_type: exact_actual_base_topological_and_form_slot_obstruction
created: 2026-08-10
status: CURRENT_P3_NORMAL_SUPPORT_CANNOT_DIAGONALIZE_TANGENTIAL_SU2PLUS__ABSTRACT_S4_CLASS_MATCH_RESCOPED__TANGENTIAL_SUPPORT_OR_NEW_SOLDERING_REQUIRED
source_return: SOURCE_CONFIRMS_HORIZONTAL_TANGENT_VERSUS_NORMAL_BUNDLE_SEPARATION__SOURCE_SILENT_P3_COLLAPSE_DIAGONAL_TANGENTIAL_SUPPORT_REDESIGN_AND_RESTRICTED_ACTION
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
canon_verdict_change: none
---

# Selected K77 P3 normal/tangential support obstruction

## Result in plain English

The previous wave found a true abstract fact on a model four-sphere: P3's
`n=+1` Hopf bundle and the positive chiral spin bundle both have `c2=1`.
This wave restores the maps used by the actual construction and finds that
they are bundles over different four-dimensional directions.

P3 is supported on a compactified **normal** four-cycle in the total
fourteen-dimensional space. The proposed source `SU(2)+` connection is the
positive-chiral Levi-Civita connection of the **observer-tangent** four-plane.
The bundle projection sends the entire P3 normal cycle to one base point.
Consequently the tangential source bundle restricts trivially to that normal
cycle:

```text
i_N^* pi^* c2(S_X+) = 0.
```

P3 has `c2=n` there. Hence only the trivial horn `n=0` matches the horizontal
bundle on the actual normal support. The intended `n=+1` amplitude horn does
not. This is not repaired by a gauge transformation: the P3 curvature lives
in normal two-form slots, while the source curvature lives in horizontal
two-form slots. Gauge conjugation changes internal coefficients, not those
covector slots.

A planted horizontal-normal permutation transports the two self-dual bases,
but it changes the observation split. That is a new soldering/reduction
construction, not internal gauge. The repository's full global
`epsilon_IG` reduction remains unconstructed.

Therefore the current nontrivial P3 normal-support route is killed. P3 as an
external datum is not globally killed. Two constructive successors remain:

1. redesign P3 with tangential/base support so its characteristic class lives
   on the same carrier as the chiral source connection; or
2. build a source-owned horizontal-normal soldering reduction and show that
   it has positive constraint surplus.

Do not restrict or vary the action until one successor passes.

## Layer 0

| object | exact carrier | not the same as |
| --- | --- | --- |
| model `S4` in v0.147 | abstract comparison space for two clutching classes | P3's embedded normal cycle with its actual projection to `X` |
| P3 cycle `i_N:S4_N -> Y` | framed compactified four-cycle inside a normal tube | observer tangent/base four-manifold |
| source chiral bundle | `pi^*S_X+`, induced by the horizontal observer frame | a vertical normal spin bundle |
| source restriction to P3 | pullback along `pi o i_N`, a constant map | the `c2=1` chiral bundle on an abstract tangent `S4` |
| P3 curvature | `su(2)`-valued element of `Lambda2 N4*` | tangential `Lambda2+ H*` curvature |
| internal gauge | conjugation in the `su(2)` coefficient factor | a map exchanging `H` and `N4` covector slots |
| soldering repair | moving carrier map that intertwines horizontal and normal slots | an already-available gauge torsor |

The key correction is not “the two bundles have different ranks.” They have
the same relevant rank. Their characteristic classes are being evaluated
after different base maps.

## Exact map and characteristic-class gate

Let `pi:Y -> X` be the metric-bundle projection and let `i_N:S4_N -> Y`
denote P3's selected normal cycle. By construction,

```text
d pi o d i_N = 0,
```

so `pi o i_N` is constant on the cycle. Naturality gives

```text
i_N^* pi^* c2(S_X+) = (pi o i_N)^* c2(S_X+) = 0.
```

The P3 collapse has degree one and its three horns satisfy

```text
c2(P3_n)[S4_N] = n,    n in {-1,0,+1}.
```

Thus the exact matching set on the actual normal support is `{0}`, not
`{+1}`. This does not contradict v0.147: v0.147 computed the two classes on
one abstract tangent model `S4`; it did not prove that this `S4` was the
normal cycle used by P3.

## Exact form-slot control

The probe constructs self-dual bases in the four horizontal and selected
four normal coordinates. Each span has rank three, while their combined span
has rank six and all cross pairings vanish. The restrictions are exact:

```text
P_H F_P3 P_H = 0,
P_N F_source P_N = 0.
```

An arbitrary internal linear combination of P3's three `su(2)` coefficients
still has zero horizontal restriction. The planted slot permutation succeeds
only by failing to commute with the horizontal projector. That is the
negative control showing the obstruction is specifically to internal gauge,
not to every possible future soldering construction.

## Constraint accounting

- Current `n=+1` normal-support diagonal: **killed**.
- Abstract `S4` class theorem: **survives**, re-scoped to a model-space
  comparison.
- Gauge-torsor parameter count: still zero physical cost only after a map on
  the correct carrier exists; it does not create that map.
- Tangential-support redesign: unbuilt; cost and existence open.
- Full horizontal-normal soldering: unbuilt; topology, field ownership,
  coefficients and constraint surplus open.
- Restricted action, Euler/BV/domain and amplitude selection: not attempted.

No residue reduction or P1/P2/P3 assignment is booked.

## Efficient specialist and hostile return

1. **Algebraic topology — ACTUAL MATH, very high.** Characteristic classes
   must be compared after pullback to the same base; constant-map pullback
   kills the tangential class on the normal cycle.
2. **Principal bundles — ACTUAL MATH, very high.** Equal abstract clutching
   degrees do not supply a bundle map when the actual base maps differ.
3. **Differential geometry — ACTUAL MATH, very high.** The vertical cycle is
   annihilated by `d pi`; this is the decisive actual-base datum.
4. **Representation theory — ACTUAL MATH, high.** Both self-dual carriers are
   rank three, but they occupy disjoint exterior-form slots.
5. **Gauge theory — ACTUAL MATH, high.** Internal conjugation cannot exchange
   tangent covector factors.
6. **Symplectic/BV — ACTUAL MATH, high.** A quotient cannot equate bundles
   with different restricted characteristic classes; the soldering field
   would have to enter the action and its presymplectic data explicitly.
7. **Variational geometry — ACTUAL MATH, high.** Restricting the action through
   a nonexistent diagonal would vary the wrong field space.
8. **Source criticism — ACTUAL MATH, high.** The source supports the
   tangent/normal distinction but is silent on P3 and either replacement.

## Progress

```text
Ledger v0.148 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

The two closed conditions are the actual-base diagonal and the proposed
internal-gauge repair. The open condition is the replacement design. The two
remaining named gates are (a) tangential support or a source-owned soldering
with positive constraint surplus and (b) the restricted-action
Euler/BV/domain calculation after that interface exists.

Validation: exact probe `37/37`, including two planted failures. No action,
datum assignment, verdict, residue, quotient, canon or public-posture change.
