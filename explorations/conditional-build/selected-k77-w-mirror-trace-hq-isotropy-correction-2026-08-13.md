---
artifact_type: exact_layer0_correction_and_pairing_classification
created: 2026-08-13
status: BASE_Q_THEOREM_PRESERVED__TRACE_Q_SAME_SECTORS_ISOTROPIC__TRACE_Q_CROSS_PAIR_NONDEGENERATE
source_return: SOURCE_SILENT_REPO_W_MIRROR_TRACE_HQ_POLARIZATION
ledger_rows: [RA-G2, LT-SM3, AC-G1a]
---

# Selected K77 W/mirror trace-Hq isotropy correction

## Result first

The previous W/mirror theorem used `Q=gamma_0`, a positive covector in the
observation base, but its prose called that input the tautological vertical
trace receiver. Existing trace ownership already fixed

\[
q_g=g/2
\]

as a negative vector in the normal `(6,4)` plane. The exact calculation was
right for its base-q witness; its Layer-0 attribution was wrong.

The corrected all-axis calculation gives a sharper polarization theorem. Let
`W` and `M=conj(W)` be the rank-192 W and ASD-mirror images and let
`K_q=eta_14 tensor iB gamma(q)`. Then:

- for each of the four canonical base directions, `W^*K_qW` and
  `M^*K_qM` have rank 192 and exact neutral inertia `(96,96,0)`, while
  `W^*K_qM=0`;
- for each of the ten canonical normal directions, the same-sector forms
  vanish exactly, while the cross-pair `W^*K_qM` has rank 192;
- on `W direct-sum M`, the full restricted form has rank 384 in every
  canonical direction.

The linear map from covectors to the W same-sector Gram has rank four and
kernel exactly the normal ten-plane. The W--mirror cross-pair map has rank ten
and kernel exactly the base four-plane. In particular, for the actual trace
axis,

\[
K_{q_g}|_{W\times W}=0,
\qquad
K_{q_g}|_{M\times M}=0,
\qquad
\operatorname{rank}(K_{q_g}|_{W\times M})=192.
\]

Thus W and mirror are complementary maximal isotropic subspaces of a
nondegenerate 384-dimensional Hermitian space. The combined form has exact
Witt inertia `(192,192,0)`. Trace `H_q` is not a same-half norm; it is an
off-diagonal polarization pairing W with its mirror.

## What changes and what does not

The previous exact conjugation theorem and `(96,96)` inertia survive for the
base-q witness. Retracted is only the statement that those were restrictions
of the **trace-owned** form. The corrected trace result does not supply a
luminous-half selector either: selecting W alone makes the trace form vanish,
while the full nondegenerate pairing requires both W and mirror.

This is not yet a physical no-go. A lower-order action, nonzero-fermion
background, real structure, BV/BFV differential, boundary condition or
analytic domain could own a different pairing or turn the cross-pair into
physical cohomological data. That owner must now be typed explicitly.

## Layer 0

| Object | Exact status | Forbidden inference |
| --- | --- | --- |
| base-q witness | neutral nondegenerate form inside W and M | tautological trace receiver |
| vertical trace `q_g` | normal-plane, negative, geometry-owned | observer time or a free base line |
| W and mirror | complementary trace-Hq isotropic sectors | ambient `C^(32,32)` halves |
| W--mirror cross-pair | exact rank 192 | physical mass, symplectic form or BV pairing |
| W plus mirror | nondegenerate Witt-neutral `(192,192)` | positive Hilbert space |

## Exact certificate

The Sage probe runs over `Q(i)` and checks all fourteen canonical covector
directions. It certifies fourteen Hermitian involutions, fourteen
anti-isometry relations, the `4+10` same/cross restriction split, exact span
ranks `4/10`, full combined rank `384`, exact base inertia `(96,96,0)`, and
the trace-axis zero/full-rank statements. No floating spectrum owns a claim.

## Specialist close

1. **Clifford/representation — ACTUAL MATH, very high.** The restriction maps
   detect precisely the base/normal splitting rather than a mysterious
   W/mirror asymmetry.
2. **Krein/operator — ACTUAL MATH, very high.** Total isotropy of W does not
   mean degeneracy of the paired carrier; W and mirror form a Witt pair.
3. **Category/Layer 0 — ACTUAL MATH, very high.** The prior defect was an
   ownership-changing homonym, not a failed matrix certificate.
4. **Analytic/PDE — ACTUAL MATH, high.** No energy, closed domain, spectrum or
   index follows from this finite form.
5. **Symplectic/BV — ACTUAL MATH, high.** The Hermitian cross-pair may be input
   to a future action complex, but it is not a presymplectic or BV result.

## Progress and next gate

```text
Ledger v0.239 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Next: identify whether the selected action, equation-9.16 lower-order vertex,
nonzero-fermion Hessian, BV/BFV complex or analytic domain owns this
off-diagonal trace-Hq pairing—or supplies a different physical form. Kill any
proposal that silently substitutes base q for trace q, treats W/mirror as the
ambient halves, or calls a symmetric cross-pair physical cohomology.
