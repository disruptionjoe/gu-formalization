---
title: "Selected-K85 RSAP SU*(4) A3 singular transition atlas"
status: active_research
doc_type: exact_quaternionic_real_form_canonical_family_rank_and_cotangent_transition_atlas
created: "2026-08-15"
registry: lab/process/selected-k85-rsap-sustar4-a3-singular-transition-atlas.json
probe: tests/channel-swings/selected_k85_rsap_sustar4_a3_singular_transition_atlas_probe.py
grade: "SIX QUATERNIONIC CANONICAL FAMILIES EXHAUSTED; FOUR SINGULAR FAMILIES PLUS ORIGIN SCHEDULED; WITHIN-FACTOR CLOSURE GRAPH AND COTANGENT FRAME NERVE CLOSED"
canon_verdict_change: none
---

# Selected-K85 RSAP `SU*(4)` `A3` singular transition atlas

## Result first

The complete K79 quaternionic spectral/Jordan family census inside

```text
T*(SU*(4)/SO*(4)) -> su*(4)*
```

now closes at exact canonical-family, rank, degeneration and cotangent-frame
grade. The six canonical families are two distinct nonreal pairs, a paired
nonreal size-two Jordan block, a repeated nonreal semisimple pair, one nonreal
pair plus one real double, two distinct real doubles, and a paired real
size-two Jordan block. The first two are regular. The last four are singular;
the origin is their common terminal stratum rather than a seventh canonical
family.

The singular schedules are:

| singular family | `dim Z_g / dim Z_m` | factor rank | target/full rank |
|---|---:|---:|---:|
| one nonreal pair plus real double | `5/4` | `14` | `82/90` |
| repeated nonreal semisimple pair | `7/5` | `13` | `80/89` |
| two distinct real doubles | `7/5` | `13` | `80/89` |
| paired real size-two Jordan block | `7/5` | `13` | `80/89` |
| origin | `15/9` | `9` | `72/85` |

Every row saturates the `98D` pointwise symplectic-realization bound. These
are canonical spectral/Jordan families, not real adjoint-orbit counts.

Twelve exact linear degenerations place every singular family on a regular
approach and connect every family to the origin directly or through a
registered intermediate. Four rational Cayley frames in `SO*(4)` provide a
genuinely noncommuting transition nerve. All six inverse-transpose cotangent
changes preserve the tautological primitive, all four base and cotangent
triangles close strictly, and the global quaternionic cotangent moment map has
zero Cech defect. No new local model or degree of freedom is required.

## Layer 0 and quaternionic construction

This is a classical quaternionic-real-form symmetric-space calculation. It is
not a Higgs, family-index, chirality, quantization or physical phase-space
calculation.

With `J=[[0,I],[-I,0]]`, the real form obeys `XJ=J conjugate(X)`. Writing

```text
X = [[A,B],[-conjugate(B),conjugate(A)]]
```

and splitting by ordinary transpose gives the exact `6+9` decomposition
`su*(4)=so*(4)+m`. Every admitted control is complex symmetric and lies in
`m`. The nonzero nilpotent

```text
N = [[1,i],[i,-1]],   N^2=0
```

supplies both paired Jordan families. Full and moving centralizers are
recomputed directly inside this real form; no pseudo-unitary schedule is
imported.

The four frame controls are Cayley transforms of exact `so*(4)` generators.
They satisfy quaternionic reality, `Q^T Q=I`, and determinant one. Their
action on the nine-dimensional moving space therefore has an exact rational
coordinate matrix, whose inverse-transpose is the cotangent transition.

## Claim ceiling and next gate

- The K79 six-family quaternionic census is complete at its stated
  canonical-family grade; the four singular families and origin have exact,
  bound-saturating schedules.
- The admitted within-factor twelve-path degeneration graph and `SO*(4)` cotangent-frame
  nerve close strictly.
- All five local real-`A3` atlases are now closed at their stated local grades.
- Cross-real-form incidence remains `TYPE_MISSING`; this packet supplies no
  relative ambient embedding or joint-orbit datum.
- Deeper `so(7,7)` strata, the rank-at-most-`49` zero-charge gate and global
  all-strata RSAP remain open. The `182D` cotangent parent remains the
  all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next classify the first deeper ambient `so(7,7)` singular stratum reached by
the completed local `A3` atlases, before attempting the zero-charge gate.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k85_rsap_sustar4_a3_singular_transition_atlas_probe.py
```

The certificate uses exact integer, rational and Gaussian-rational arithmetic
only.
