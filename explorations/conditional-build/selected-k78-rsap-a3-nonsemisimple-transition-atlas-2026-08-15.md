---
title: "Selected-K78 RSAP split-A3 nonsemisimple transition atlas"
status: active_research
doc_type: exact_singular_jordan_classification_rank_and_transition_atlas
created: "2026-08-15"
registry: lab/process/selected-k78-rsap-a3-nonsemisimple-transition-atlas.json
probe: tests/channel-swings/selected_k78_rsap_a3_nonsemisimple_transition_atlas_probe.py
grade: "ALL FIVE SINGULAR NONSEMISIMPLE REAL sl4 FAMILIES CLOSED; 98D POINTWISE RANK BOUNDS SATURATED; NO NEW SPLIT-A3 LOCAL MODEL"
canon_verdict_change: none
---

# Selected-K78 RSAP split-`A3` nonsemisimple transition atlas

## Result first

The remaining nonsemisimple singular transition census inside the split
`A3` factor closes. There are exactly five real `sl4` Jordan families in this
class—not nine and not an unbounded collection:

```text
J3(lambda)+J1(lambda)
J2(lambda)+J2(lambda)
J2(lambda)+J1(lambda)+J1(lambda)
J2(lambda)+J1(lambda)+J1(mu), lambda != mu
J2(lambda)+J1(mu)+J1(mu), lambda != mu.
```

The complex-primary configurations add no sixth case. In real dimension four,
a nonsemisimple complex primary can only be a single size-two complex Jordan
block, or share the space with one real size-two block. In both cases there is
one block per real irreducible primary, the minimal polynomial has degree four,
and the control is regular rather than singular.

For exact signature-`(2,2)` symmetrizers, the five `sl4` centralizer dimensions
are `5,7,9,5,5`; the corresponding moving-space centralizer dimensions are
`4,5,6,4,4`. Thus the existing principal factor

```text
T*(SL(4,R)/SO(2,2)) -> sl(4,R)*
```

has ranks `14,13,12,14,14`. On the common `98D` carrier the target/map rank
pairs are consequently

```text
(82,90), (80,89), (78,88), (82,90), (82,90).
```

Every value saturates the pointwise RSAP bound. Exact `SL4` congruences move
all five symmetrizers to the already selected alternating form
`diag(+,-,+,-)`. Their induced nine-dimensional moving-tangent transitions
are invertible; the inverse-transpose cotangent changes preserve the
tautological primitive, and every admitted triangular transition telescopes
to identity. Exact regular approach arcs and nilpotent-scaling degenerations
connect the representatives to the existing regular, semisimple `A1 x A1`,
semisimple `A2`, and `A3`-origin schedules inside the same smooth factor.

No genuinely new local model is required for split `A3`. This does not prove
global all-strata RSAP in `so(7,7)*`. Other real `A3` forms, deeper ambient
strata and zero charge remain open. The naive same-sign `SL2/SO2` sheet also
remains exactly what the predecessor proved it to be: a partial hyperbolic
source sheet, never an RSAP wall chart.

## Layer 0

This is a classical symplectic/Poisson atlas calculation. “Jordan family,”
“moving space” and “chirality” are not being compared here to particle-family,
Standard-Model Higgs or ordinary index-theory constructions. Those comparators
are outside this lane.

## Why the list has exactly five members

Write the real primary decomposition by multiplicities of distinct real
eigenvalues. The possibilities are

```text
4; 3+1; 2+2; 2+1+1; 1+1+1+1.
```

For a primary with Jordan partition `p`, its `gl` centralizer dimension is
the sum of the squares of the column lengths of `p`. Centralizers from
distinct primaries add. A trace-free `4 x 4` matrix is regular exactly when
the resulting `gl4` centralizer has dimension four, equivalently when there
is one Jordan block for each irreducible primary.

Enumerating every partition and then quotienting the exchange of the two
equal-multiplicity primaries in the `2+2` row leaves precisely:

| real primary pattern | Jordan partitions | `dim Z_sl4` |
|---|---|---:|
| `4` | `(3,1)` | `5` |
| `4` | `(2,2)` | `7` |
| `4` | `(2,1,1)` | `9` |
| `3+1` | `(2,1)+(1)` | `5` |
| `2+2` | `(2)+(1,1)` | `5` |

All other nonsemisimple rows have centralizer dimension three and belong to
the already covered regular locus. All other singular rows are semisimple or
the zero control and were attached in the preceding wall/face/origin packets.

For an irreducible quadratic primary, the same formula carries an extra
factor of two. The only nonsemisimple dimension-four possibilities have real
`gl4` centralizer dimension four. This proves, rather than assumes, that no
complex-primary singular case is missing.

## Exact symmetrizers and ranks

Let `R_n` be the reverse identity. Representatives and symmetrizers can be
chosen as follows:

| family | representative | symmetrizer |
|---|---|---|
| `(3,1)` | `J3(0)+0` | `R3+(-1)` |
| `(2,2)` | `J2(0)+J2(0)` | `R2+R2` |
| `(2,1,1)` | `J2(0)+0+0` | `R2+(1)+(-1)` |
| `(2,1)+(1)` | `J2(1)+1+(-3)` | `R2+(1)+(-1)` |
| `(2)+(1,1)` | `J2(1)+(-1)+(-1)` | `R2+(1)+(-1)` |

Each form has determinant one and inertia `(2,2)`, and each pair satisfies

```text
A^T H = H A.
```

For the associated symmetric decomposition `sl4=h_H+m_H`, exact linear
algebra gives `dim(m_H)=9`, `dim(h_H)=6`, and the rank table:

| family | `dim Z_sl4(A)` | `dim(Z(A) intersect m_H)` | factor rank | target rank | full rank |
|---|---:|---:|---:|---:|---:|
| `(3,1)` | `5` | `4` | `14` | `82` | `90` |
| `(2,2)` | `7` | `5` | `13` | `80` | `89` |
| `(2,1,1)` | `9` | `6` | `12` | `78` | `88` |
| `(2,1)+(1)` | `5` | `4` | `14` | `82` | `90` |
| `(2)+(1,1)` | `5` | `4` | `14` | `82` | `90` |

Indeed

```text
rank dJ_A = dim(m_H) + rank(ad_A|m_H)
           = 18 - dim(Z(A) intersect m_H).
```

The common `72D` leaf and four zero-coordinate projections add `76` to the
factor rank. The target rank is `72+15-dim Z_sl4(A)`. In all five rows,

```text
full map rank = (98 + target Poisson rank)/2.
```

So the nonsemisimple strata do not expose a hidden excess rank loss. Their
schedules coincide with the banked semisimple wall, `A1 x A1`, and `A2`
schedules according to centralizer dimension, not according to whether the
matrix diagonalizes.

## Regular approaches and degeneration routing

For each representative, the probe constructs an exact `D in m_H` such that
`A+D` has `sl4` orbit rank twelve. Some `12 x 12` minor of
`ad_(A+tD)` is therefore a nonzero polynomial in `t`. It can vanish for only
finitely many values, so arbitrarily small nonzero rational `t` give regular
controls in the same smooth cotangent factor. This supplies the transition to
the already complete regular block-pivot atlas without an eigenline chart at
the singular endpoint.

Scaling the displayed nilpotent entries gives the lower-rank endpoints:

```text
(3,1), (2,2), (2,1,1)  ->  A3 origin,
(2,1)+(1)               ->  diag(1,1,1,-3),
(2)+(1,1)               ->  diag(1,1,-1,-1).
```

The last two are the banked semisimple `A2` and `A1 x A1` schedules. The
probe checks that both the limiting matrix and its nilpotent difference remain
`H`-self-adjoint, so these are actual paths in the same moving fibre rather
than target-only closure assertions.

## Transition and cocycle construction

Three rational determinant-one congruences normalize

```text
R3+(-1),  R2+R2,  R2+(1)+(-1)
```

to `H_alt=diag(+,-,+,-)`. Two rational `SO(2,2)` boosts distinguish the two
mixed families sharing the third form. Conjugation carries every representative
and every nine-dimensional moving tangent space into the alternating principal
fibre. Expressing those tangent maps in one exact basis gives five invertible
`9 x 9` rational matrices `C_i`.

On any admitted overlap the base transition is

```text
C_ji = C_j^{-1} C_i,
```

and the covector transition is `C_ji^{-T}`. Hence

```text
(C_ji^{-T} p)^T (C_ji dq) = p^T dq.
```

The probe checks all ten pairwise primitive identities and all ten unordered
triangles in both tangent and cotangent coordinates. The transitions are not
artificially commuting, but every cycle closes because it normalizes through
one global factor. The geometric moment map is the restriction of that same
global cotangent moment map, so its Cech defect is zero by equivariance.

This does not claim that every three abstract Jordan strata meet in one target
neighborhood. It proves that wherever the regular approaches and degeneration
arcs produce an admitted overlap, the coordinate changes are restrictions of
one coherent cotangent atlas; there is no Jordan-specific potential or moment
map left to invent.

## Claim ceiling and next gate

- The five singular nonsemisimple real `sl4` Jordan families are exhaustive.
- Their exact centralizer, moving-centralizer and rank schedules close.
- The split-`A3` nonsemisimple transition atlas needs no new local model or
  degree of freedom beyond the already constructed principal factor.
- This is local split-`A3` closure, not global all-strata RSAP for `so(7,7)*`.
- Other real `A3` forms, deeper ambient singular strata, the rank-at-most-`49`
  zero-charge gate and global RSAP remain open.
- The all-charge fallback remains the `182D` cotangent parent.
- The same-sign `SL2/SO2` sheet remains partial and non-RSAP.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next classify the other real `A3` principal-factor candidates. Test their
regular nonsemisimple controls and first singular centralizer jumps before
entering a higher-root subsystem or making any global singular-atlas claim.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k78_rsap_a3_nonsemisimple_transition_atlas_probe.py
```

The certificate uses exact integer and rational arithmetic only.
