---
title: "Selected-K83 RSAP SU(3,1) A3 singular transition atlas"
status: active_research
doc_type: exact_pseudo_hermitian_canonical_configuration_rank_and_cotangent_transition_atlas
created: "2026-08-15"
registry: lab/process/selected-k83-rsap-su31-a3-singular-transition-atlas.json
probe: tests/channel-swings/selected_k83_rsap_su31_a3_singular_transition_atlas_probe.py
grade: "ALL FOUR SU(3,1) CANONICAL CONFIGURATIONS CONNECTED; NINE SINGULAR JORDAN-INCIDENCE FAMILIES CLOSED; NO NEW LOCAL MODEL"
canon_verdict_change: none
---

# Selected-K83 RSAP `SU(3,1)` `A3` singular transition atlas

## Result first

The complete local singular transition atlas inside

```text
T*(SU(3,1)/SO(3,1)) -> su(3,1)*
```

closes at canonical-configuration, sign-control and cotangent-transition
grade. Signature `(3,1)` admits exactly four of the nine pseudo-Hermitian
dimension-four configurations from the real-form census:

```text
real 3+1,
real 2+1+1,
real 1+1+1+1,
one complex pair plus two real lines.
```

They contain nine singular Jordan-incidence families: one from `3+1`, three
from `2+1+1`, four semisimple multiplicity types from four real lines, and one
repeated-real-pair family beside a complex pair. These are incidence types,
not a count of real adjoint orbits. Continuous eigenvalues and sign
characteristics remain.

All twenty-five admissible block-sign controls have the same familywise rank
schedule. The nine families distribute as follows:

| families | `dim Z_g / dim Z_m` | factor rank | target/full rank |
|---:|---:|---:|---:|
| `5` | `5/4` | `14` | `82/90` |
| `1` | `7/5` | `13` | `80/89` |
| `2` | `9/6` | `12` | `78/88` |
| origin | `15/9` | `9` | `72/85` |

Every row saturates the `98D` pointwise symplectic-realization bound. Eleven
exact linear paths connect all four configurations to every registered
singular family. Rational determinant-one congruences normalize their forms
to `diag(+,+,+,-)`. The four-chart nerve has six pair transitions and four
triangles; every inverse-transpose cotangent lift preserves the tautological
primitive, every triangle closes strictly, and the one global `SU(3,1)`
cotangent moment map has zero Cech defect.

No new local model or degree of freedom is required. Nothing in this packet
supplies the type-missing ambient edge to another real form.

## Layer 0 and construction

This is classical pseudo-Hermitian canonical-form and cotangent moment-map
work. It is not a Higgs, family-index, chirality, quantization or physical
phase-space calculation. Conventional particle comparators do not classify
these indefinite self-adjoint blocks and are not used.

For `X in su(3,1)` in the moving summand, write `X=iA`. Relative to a real
symmetric form `H` of signature `(3,1)`,

```text
A^T H = H A,    tr A = 0.
```

The compatible configurations follow from the signature carried by each real
Jordan block and the neutral signature contributed by a complex conjugate
pair. A size-four real block, `2+2`, a complex pair plus a real size-two
block, two complex pairs, and a complex size-two Jordan block each require at
least two negative directions and therefore do not occur in signature
`(3,1)`. This is why the `SU(2,2)` nine-chart atlas restricts to four charts
rather than being copied wholesale.

For each control the probe reconstructs

```text
m_H = {B : B^T H = H B, tr B = 0}
```

and recomputes both the full and moving centralizers. The factor moment rank is

```text
rank dJ = 9 + rank(ad_A|m_H)
        = 18 - dim(Z(A) intersect m_H).
```

Adding the common `72D` leaf and four zero-coordinate projections gives the
full schedules above. Thus the ranks are exact `(3,1)` results, not imported
from the split or `SU(2,2)` factors.

## Closure and cotangent nerve

Every singular family has an exact `H`-self-adjoint direction whose nearby
control is regular. The eleven registered degenerations cover the `J3+J1`
collision; all three `J2+J1+J1` coincidence patterns; semisimple `2+1+1`,
`2+2`, `3+1` and origin limits; disappearance of a complex pair's imaginary
part; collision of the two real lines beside it; and the combined
complex-to-real `2+2` boundary.

The four rational congruences identify the configuration forms with one
reference `(3,1)` form. Their induced moving-coordinate changes are
invertible. On every pair overlap, the inverse-transpose covector change
preserves `p^T dq`; all four base and cotangent triangles telescope to the
identity. This proves within-factor coherence wherever the exact approaches
and paths give an overlap. It does not assert that every abstract stratum has
one shared neighborhood, and it does not create a cross-real-form edge.

## Claim ceiling and next gate

- All four `SU(3,1)` canonical configurations contain exact regular controls.
- Their nine singular incidence families and twenty-five admissible sign
  controls have exact, bound-saturating rank schedules.
- The complete local four-configuration cotangent transition nerve closes.
- No new `SU(3,1)` local model or degree of freedom is required.
- Cross-real-form incidence remains `TYPE_MISSING`.
- Compact and quaternionic singular atlases, deeper `so(7,7)` strata, zero
  charge and global all-strata RSAP remain open. The `182D` cotangent parent
  remains the all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next complete the compact `SU(4)/SO(4)` semisimple singular transition atlas,
again without manufacturing a cross-real-form edge.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k83_rsap_su31_a3_singular_transition_atlas_probe.py
```

The certificate uses exact integer and rational arithmetic only.
