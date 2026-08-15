---
title: "Selected-K82 RSAP SU(2,2) A3 singular transition atlas"
status: active_research
doc_type: exact_pseudo_hermitian_canonical_configuration_rank_and_cotangent_transition_atlas
created: "2026-08-15"
registry: lab/process/selected-k82-rsap-su22-a3-singular-transition-atlas.json
probe: tests/channel-swings/selected_k82_rsap_su22_a3_singular_transition_atlas_probe.py
grade: "ALL NINE SU(2,2) CANONICAL CONFIGURATIONS CONNECTED; ELEVEN SINGULAR JORDAN-INCIDENCE FAMILIES CLOSED; NO NEW LOCAL MODEL"
canon_verdict_change: none
---

# Selected-K82 RSAP `SU(2,2)` `A3` singular transition atlas

## Result first

The complete local singular transition atlas inside

```text
T*(SU(2,2)/SO(2,2)) -> su(2,2)*
```

closes at canonical-configuration, sign-control and cotangent-transition
grade. All nine pseudo-Hermitian configurations from k79 contain exact regular
controls with full/moving centralizer dimensions `3/3`. Separating their
eigenvalue coincidences gives eleven singular Jordan-incidence families:

```text
five real nonsemisimple families,
four real semisimple multiplicity families,
one complex pair plus a repeated real pair,
one repeated semisimple complex pair.
```

Their rank distribution is

| families | `dim Z_g / dim Z_m` | target/map rank |
|---:|---:|---:|
| `5` | `5/4` | `82/90` |
| `3` | `7/5` | `80/89` |
| `2` | `9/6` | `78/88` |
| origin | `15/9` | `72/85` |

Every row saturates the `98D` pointwise bound. The probe also checks all fifty
admissible block-sign controls in signature `(2,2)`; sign characteristics do
not change the family rank schedule.

Seventeen exact linear degenerations connect every configuration to its
singular boundary types. Rational determinant-one congruences normalize the
nine configuration forms to `diag(+,-,+,-)`. The resulting nine-chart nerve
has `36` pair transitions and `84` triangles. All inverse-transpose cotangent
changes preserve the tautological primitive, and every base and cotangent
triangle closes strictly. One global `SU(2,2)` cotangent moment map gives zero
moment Cech defect.

No new local model or degree of freedom is required. This result stays wholly
inside the `SU(2,2)` factor: it does not reopen the type-missing ambient edge
to split `A3`.

## Layer 0

This is a classical pseudo-Hermitian canonical-form and cotangent moment-map
calculation. It is not a Higgs, family-index, chirality or quantization
calculation. Those conventional comparators neither classify these
indefinite self-adjoint blocks nor supply the missing cross-real-form ambient
embedding.

## The nine configurations and their singular counts

For `X in su(2,2)` in the moving summand, write `X=iA`. Relative to a real
symmetric form `H` of signature `(2,2)`, the condition is

```text
A^T H = H A,    tr A = 0.
```

The nine compatible real canonical block configurations and their intrinsic
singular incidence counts are:

| configuration | singular families |
|---|---:|
| one real block of size `4` | `0` |
| real `3+1` | `1` |
| real `2+2` | `1` |
| real `2+1+1` | `3` |
| real `1+1+1+1` | `4` |
| complex pair plus real size `2` | `0` |
| complex pair plus two real lines | `1` |
| two complex pairs | `1` |
| complex Jordan block of size `2` | `0` |

The sum is eleven. “Family” here means eigenvalue/Jordan incidence type, not
one real adjoint orbit. Eigenvalues and sign characteristics continue to
parameterize or split real orbits. The probe does not collapse those data: it
tests fifty admissible signed block forms and reports only the rank schedule,
which is invariant across them.

For real blocks the census is exact set-partition combinatorics. Grouping
Jordan blocks assigns equal eigenvalues; for a primary partition `p`,

```text
dim Z_gl = sum_j (column_length_j(p))^2.
```

Centralizer dimension greater than four is singular. Applied to block shapes
`4`, `3+1`, `2+2`, `2+1+1`, and `1+1+1+1`, this gives counts
`0,1,1,3,4`. A complex primary contributes twice the same partition number.
Thus a complex size-two Jordan block and complex-plus-real-size-two remain
regular, whereas coincident real lines beside one complex pair and coincident
complex pairs give the two additional singular families.

## Exact rank census

For `m_H={B:B^T H=HB, tr B=0}`, the factor moment differential at `iA` has

```text
rank dJ = 9 + rank(ad_A|m_H)
        = 18 - dim(Z(A) intersect m_H).
```

The eleven schedules are:

| family | `dim Z_g` | `dim Z_m` | factor rank | target rank | full rank |
|---|---:|---:|---:|---:|---:|
| `J3+J1`, equal eigenvalue | `5` | `4` | `14` | `82` | `90` |
| `J2+J2`, equal eigenvalue | `7` | `5` | `13` | `80` | `89` |
| `J2+J1+J1`, all equal | `9` | `6` | `12` | `78` | `88` |
| `J2+J1` equal, one distinct | `5` | `4` | `14` | `82` | `90` |
| `J2` plus repeated semisimple pair | `5` | `4` | `14` | `82` | `90` |
| semisimple `2+1+1` | `5` | `4` | `14` | `82` | `90` |
| semisimple `2+2` | `7` | `5` | `13` | `80` | `89` |
| semisimple `3+1` | `9` | `6` | `12` | `78` | `88` |
| scalar trace-free origin | `15` | `9` | `9` | `72` | `85` |
| complex pair plus repeated real pair | `5` | `4` | `14` | `82` | `90` |
| repeated semisimple complex pair | `7` | `5` | `13` | `80` | `89` |

The common `72D` leaf and four zero-coordinate projections contribute `76`
to the full map rank. In every row,

```text
full map rank = (98 + target Poisson rank)/2.
```

So neither the mixed complex/real boundary nor the repeated complex-pair
boundary exposes a hidden excess rank loss.

## Closure graph

Every singular family has an exact `H`-self-adjoint direction `D` for which
`A+D` is regular. A nonzero orbit minor makes `A+tD` regular for arbitrarily
small rational `t` away from finitely many roots.

The seventeen checked degeneration paths include:

- collision of the real `3+1`, `2+2`, and `2+1+1` eigenvalues into all five
  real nonsemisimple types;
- collision of four real lines into semisimple multiplicities `2+1+1`, `2+2`,
  `3+1`, and `4`;
- collapse of a complex pair beside a real size-two block into the real
  `J2` plus repeated-pair type;
- collapse of a complex pair beside two real lines into semisimple `2+1+1`
  or `2+2`;
- collision of two complex pairs into the repeated-complex family and then
  the origin; and
- the complex size-two Jordan block reaching both the repeated-complex and
  real `J2+J2` boundaries.

For every path the start, limit and difference are trace-free and
`H`-self-adjoint, so the entire linear path remains in the same moving fibre.
These are within-factor closures, not target-only adjacency guesses.

## Cotangent transition nerve

The nine block forms are rationally congruent to

```text
H_alt = diag(+,-,+,-).
```

The probe supplies a determinant-one rational normalizer for every
configuration, including the real size-four reverse form, the mixed
complex/real form, and the off-diagonal form for the complex size-two Jordan
block. Expressing their nine-dimensional moving tangent spaces in the common
`H_alt` basis gives invertible maps `C_i`.

On each admitted overlap,

```text
C_ji = C_j^-1 C_i,      p_ji = C_ji^-T p.
```

All `36` pairwise changes preserve `p^T dq`. All `84` base triangles and all
`84` inverse-transpose triangles telescope to identity. The family is
genuinely noncommuting, so closure is not an artifact of diagonal transition
matrices.

This verifies coherence wherever the exact regular approaches and
degeneration paths produce an overlap. It does not assert that every three
abstract strata share one target neighborhood.

## Claim ceiling and next gate

- All nine `SU(2,2)` canonical configurations contain exact regular controls.
- Their eleven singular Jordan-incidence families and fifty admissible sign
  controls have exact, bound-saturating rank schedules.
- The complete local nine-configuration cotangent transition nerve closes.
- No new `SU(2,2)` local model or degree of freedom is required.
- The split/`SU(2,2)` ambient edge remains `TYPE_MISSING`; no cross-form
  transition was used or inferred.
- The `SU(3,1)`, compact and quaternionic singular atlases, deeper ambient
  strata, zero charge and global all-strata RSAP remain open. The `182D`
  cotangent parent remains the all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next complete the four-configuration singular transition atlas inside
`SU(3,1)/SO(3,1)`, again without manufacturing any cross-real-form edge.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k82_rsap_su22_a3_singular_transition_atlas_probe.py
```

The certificate uses exact integer and rational arithmetic only.
