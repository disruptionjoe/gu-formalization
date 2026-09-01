---
title: "K77 Shiab Operators — Typed Existence and Isomorphism"
status: canon
doc_type: canon
carrier_scope: current_repository_selected_k77
promoted_from:
  - "lab/active-research/joe-directed/archaeology/ar5-cl95-full-shiab-rank-crosswalk-2026-08-16.md"
  - "explorations/conditional-build/selected-k77-zorro-differentiated-shiab-second-jet-gate-2026-08-14.md"
  - "lab/process/hostile-reviews/2026-08-14-selected-k77-zorro-differentiated-shiab-second-jet-review.md"
promoted_at: "2026-09-01"
promotion_authority: "Joe direct chat — K77 Shiab v2"
verdict: "RESOLVED (two typed real-algebraic existence statements only)"
scope_correction: "K77-SHIAB-01: the natural spinor contraction and the repository-selected grade-one-to-grade-two Hodge--Shiab are two different maps. Both exist over real Cl(7,7); only the second is the current selected K77 operator. Neither result recovers Weinstein's preferred selector or establishes physical dynamics."
independent_verification:
  - "tests/shiab_k77_canon_independent.py"
---

# K77 Shiab operators — typed existence and isomorphism

This is the current K77 companion to the scoped historical K95 result in
`canon/shiab-existence-cl95.md`. It records two exact statements that share
the name “Shiab” but are **not the same mathematical object**.

## Scope and object identity

Let `(V,g)` be a real fourteen-dimensional quadratic space of signature
`(7,7)`. Then

```text
Cl(7,7) ~= M(128,R),
S_R ~= R^128,
S_R = S+ (+) S-,       dim_R S+ = dim_R S- = 64.
```

The two maps are:

| object | source | target | exact result | selection owner |
|---|---:|---:|---|---|
| natural spinor contraction `A` | `Lambda^2 V* tensor S_R` (`11,648`) | `V* tensor S_R` (`1,792`) | surjective; kernel dimension `9,856` | natural Clifford formula, not a source selector |
| repository-selected K77 Hodge--Shiab `H_sel` | `Lambda^2 V* tensor Cl_1` (`1,274`) | `V* tensor Cl_2` (`1,274`) | signed-permutation isomorphism; kernel zero | repository-selected `comm/symi/symi` product |

Here `Cl_1 ~= V` has dimension `14` and `Cl_2 ~= Lambda^2 V` has dimension
`91`. Equal use of a `(7,7)` Clifford algebra does not identify the two
carriers, formulas, maps or source grades.

## Theorem 1 — the natural real K77 spinor contraction exists and is surjective

For a local orthonormal frame with

```text
g(e_a,e_b) = eta_a delta_ab,       eta_a in {+1,-1},
```

define

```text
A(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha)s.
```

This map is real-linear, natural and `Spin(7,7)`-equivariant. It is nonzero:
for a simple form `e^i wedge e^j`, the two displayed contraction components
contain Clifford multiplication by non-null frame covectors, which is
invertible.

The stronger exact result follows from the signature-independent
signed-companion theorem already proved in
`lab/active-research/joe-directed/archaeology/ar5-cl95-full-shiab-rank-crosswalk-2026-08-16.md`.
Writing `x_ab=-x_ba`,

```text
(A x)_a = sum_b gamma_b x_ab,
(A^sharp y)_ab = eta_b gamma_b y_a - eta_a gamma_a y_b.
```

On `V* tensor S`, the composition is diagonal on the gamma-trace and
gamma-traceless summands:

```text
A A^sharp = 12 P_RS + 26 P_trace                 (n=14).
```

Both eigenvalues are nonzero, so `A` is surjective. Therefore

```text
full real module:  rank A = 14*128 = 1,792
                   dim ker A = (91-14)*128 = 9,856

each chiral block: Lambda^2 V* tensor S+/- -> V* tensor S-/+
                   rank = 14*64 = 896
                   dim kernel = (91-14)*64 = 4,928.
```

This construction needs no complexification. Clifford multiplication is odd,
so each chiral block maps to the opposite real half-spinor.

## Theorem 2 — the current selected K77 Hodge--Shiab is an isomorphism

The current repository-selected product is the `comm/symi/symi` member of the
source-admitted two-term Hodge--Shiab grammar. On every basis cell it acts as

```text
F_ij^k  |->  -2 eta_i eta_j eta_k T_k^ij,       i<j.
```

The source and target coordinates are both indexed by the same triples
`(i<j,k)`. Every coefficient is `+2` or `-2`; hence the formula is a coordinate
permutation followed by an invertible diagonal scaling. It is therefore an
exact real isomorphism:

```text
dimension source = 91*14 = 1,274
dimension target = 14*91 = 1,274
rank              = 1,274
kernel dimension  = 0
coefficient split = 637 at +2, 637 at -2.
```

The derivation from the actual selected Hodge--Shiab backend is reproduced by
`tests/channel-swings/selected_k77_zorro_differentiated_shiab_second_jet_probe.py`.
The later independent certificate `tests/shiab_k77_canon_independent.py`
reconstructs all `1,274` coordinate images without importing that backend,
checks the `637/637` sign census, and verifies the exact inverse over `Q`.

This theorem proves the selected map's algebraic existence and invertibility.
It **does not recover Weinstein's preferred Shiab**: the historical notes that
would select the intended product remain missing, and the source-admitted
family contains alternatives.

## K95 nontransfer boundary

The K95 theorem uses

```text
Cl(9,5) ~= M(64,H),      S_R ~= H^64,      dim_R S_R = 256,
```

and its natural contraction has shape `23,296 -> 3,584`. Its quaternionic
commutant, `Sp(64)`/right-`H` constraints, real selector-family counts and
rank/kernel numbers do not transfer to K77. Conversely, the selected K77
`1,274 x 1,274` grade-one-to-grade-two isomorphism is not a correction of the
K95 spinor contraction. The two exact results coexist under different typed
scopes.

## What this does not establish

- That the ambient metric construction uniquely forces K77 rather than every
  conventionally related real-form presentation. K77 is the current
  repository-selected/source-aligned carrier; ambient-signature uniqueness is
  a separate question.
- That `comm/symi/symi` is Weinstein's preferred or source-forced selector.
- Uniqueness of a natural or source-admitted Shiab family.
- A selected source action, compatible reality adjoint, common global domain,
  physical quotient, positivity or BV/BFV cohomology.
- An anomaly cancellation theorem, analytic index or fermion-generation
  count.
- Transfer of any K95 quaternionic selector, gauge-group or index argument.

## Verification and references

Run:

```text
python3 tests/shiab_k77_canon_independent.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_ar5_cl95_full_shiab_rank_crosswalk.py
_local/cas-venv/bin/python tests/channel-swings/selected_k77_zorro_differentiated_shiab_second_jet_probe.py
```

The second command verifies the universal signed-companion theorem across all
nondegenerate fourteen-dimensional signatures. The third derives the selected
K77 basis formula from the exact backend and checks the surrounding
Levi-Civita/Spencer application. The first is the later independent canon
certificate and guards the object split and non-identification ceiling.
