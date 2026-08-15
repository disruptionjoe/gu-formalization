---
title: "Selected-K84 RSAP compact SU(4) A3 semisimple singular transition atlas"
status: active_research
doc_type: exact_compact_symmetric_spectral_multiplicity_rank_and_cotangent_transition_atlas
created: "2026-08-15"
registry: lab/process/selected-k84-rsap-compact-su4-a3-semisimple-singular-transition-atlas.json
probe: tests/channel-swings/selected_k84_rsap_compact_su4_a3_semisimple_singular_transition_atlas_probe.py
grade: "COMPACT NORMALITY EXHAUSTS FOUR SINGULAR MULTIPLICITY STRATA; COMPLETE CLOSURE GRAPH AND COTANGENT FRAME NERVE CLOSED; NO NEW LOCAL MODEL"
canon_verdict_change: none
---

# Selected-K84 RSAP compact `SU(4)` `A3` semisimple singular transition atlas

## Result first

The complete semisimple multiplicity atlas inside

```text
T*(SU(4)/SO(4)) -> su(4)*
```

closes at spectral-stratum, exact-rank and cotangent-frame grade. After
writing a moving control as `X=iA`, compactness makes `A` real symmetric and
trace-free. The real spectral theorem therefore excludes every nonsemisimple
control and leaves one canonical configuration, four real eigenlines.

The fifteen set partitions of four labels exhaust exactly five multiplicity
types. The regular type is `1+1+1+1`; the singular types and schedules are:

| singular multiplicity | `dim Z_g / dim Z_m` | factor rank | target/full rank |
|---:|---:|---:|---:|
| `2+1+1` | `5/4` | `14` | `82/90` |
| `2+2` | `7/5` | `13` | `80/89` |
| `3+1` | `9/6` | `12` | `78/88` |
| `4` (origin) | `15/9` | `9` | `72/85` |

Every row saturates the `98D` pointwise symplectic-realization bound. These
are multiplicity strata, not counts of adjoint orbits: eigenvalue parameters
remain inside the first three rows.

Eight exact diagonal paths realize every arrow in the multiplicity closure
graph, including the direct regular approaches and the intermediate
`2+1+1 -> 2+2`, `2+1+1 -> 3+1`, `2+2 -> 4`, and `3+1 -> 4` collisions. Each
path stays inside the same real-symmetric trace-free fibre, and its endpoint
recomputes the claimed full and moving centralizers.

Four exact rational `SO(4)` frames provide a noncommuting finite transition
nerve. Its six inverse-transpose cotangent transitions preserve the
tautological primitive; all four base triangles and all four cotangent
triangles close strictly; the global compact cotangent moment map has zero
Cech defect. No new local model or degree of freedom is required.

## Layer 0 and construction

This is a classical compact symmetric-space and cotangent moment-map result.
It is not a Higgs, family-index, chirality, quantization or physical
phase-space calculation. Those conventional particle comparators do not
classify this atlas and are irrelevant to the gate.

With `H=I_4`, the symmetric decomposition is

```text
h = so(4),
m = {A in Mat_4(R) : A^T=A, tr A=0},
dim h + dim m = 6+9.
```

For each diagonal representative, the probe reconstructs both centralizers
and uses

```text
rank dJ_factor = 9 + rank(ad_A|m)
                = 18 - dim(Z(A) intersect m).
```

Adding the common `72D` leaf and the four zero-coordinate projections gives
the full schedules in the table. No rank is imported from the split or
pseudo-unitary factors.

## Complete multiplicity closure graph

The closure graph tested is

```text
1+1+1+1 -> 2+1+1, 2+2, 3+1, 4
2+1+1   -> 2+2, 3+1
2+2     -> 4
3+1     -> 4.
```

The arrows describe admissible eigenvalue collisions, not claims that each
listed stratum is a single orbit. Because all controls are diagonal in one
compact symmetric fibre, the paths require neither Jordan-sign data nor an
indefinite-form chart change.

The four rational frames are an exact consistency nerve for moving-frame
changes, not a claim that four frames form a global coordinate cover of the
whole symmetric space. Their role is to test the transition law actually
used: the tangent change acts by `A -> Q^T A Q`, and the covector change is
its inverse transpose. This is enough to certify primitive, triangle and
moment compatibility for the admitted overlaps.

## Claim ceiling and next gate

- Compact normality excludes all nonsemisimple moving controls.
- The four singular eigenvalue-multiplicity strata and their complete closure
  graph have exact, bound-saturating rank schedules.
- The admitted compact `SO(4)` cotangent transition nerve closes strictly.
- No new compact local model or degree of freedom is required.
- Cross-real-form incidence remains `TYPE_MISSING`; this packet supplies no
  ambient support embedding or joint-orbit datum.
- The quaternionic `SU*(4)/SO*(4)` six-configuration singular atlas, deeper
  `so(7,7)` strata, the rank-at-most-`49` zero-charge gate and global
  all-strata RSAP remain open. The `182D` cotangent parent remains the
  all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next complete the six-configuration quaternionic `SU*(4)/SO*(4)` singular
transition atlas, again entirely within that factor and without manufacturing
a cross-real-form edge.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k84_rsap_compact_su4_a3_semisimple_singular_transition_atlas_probe.py
```

The certificate uses exact integer and rational arithmetic only.
