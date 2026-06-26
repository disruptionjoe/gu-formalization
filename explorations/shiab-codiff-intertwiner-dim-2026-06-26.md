---
title: "Shiab Selector Multiplicity — dim Hom_{so(14,C)}(Lambda^2 V (x) S, V (x) S)"
date: "2026-06-26"
problem_label: "SHIAB-SELECTOR-MULT-01"
status: complete
verdict: "dim > 1 — selector NOT uniquely pinned by equivariance (dim=2 per natural chirality block, dim=4 full Dirac). The canon OPEN 'uniqueness of the equivariant map' resolves in the NEGATIVE."
code: "tests/shiab_codiff_intertwiner_dim.py"
methods: ["Racah-Speiser / Brauer-Klimyk irrep decomposition (exact)", "Kostant/Klimyk alternating Weyl-group sum over |W(D_7)|=322560 (independent cross-check)", "from-scratch Freudenthal weight-multiplicity + highest-weight peeling (third independent rebuild, zero shared code, verifier)"]
integrator_note_2026_06_26: "The dim=2 (per chiral block) / dim=4 (full Dirac) figures are the COMPLEX Hom multiplicity (signature-independent). GU's actual spinor is the REAL quaternionic form (Cl(9,5)=M(64,H)), which doubles the count: the real Spin(9,5) chirality-flipping Hom dimension is >= 8. Do NOT equate the real and complex Hom dimensions. Either way dim > 1, so the negative result (selector NOT unique) stands and is strengthened. The two complex channels are the Clifford-trace channel (S+) and the Rarita-Schwinger channel (omega_1+omega_6)."
---

# Shiab Selector Multiplicity

## Question

GU's ship-in-a-bottle (shiab) operator is a natural equivariant map

```
Phi : Omega^2(Y^14) (x) S  ->  Omega^1(Y^14) (x) S
```

Algebraically (pointwise, on the fiber) this is a map of so(14,C)-modules

```
Lambda^2 V (x) S  ->  V (x) S ,    V = C^14,  Lambda^2 V = adjoint (dim 91),
                                   S = Dirac spinor of so(14) (dim 128) = S^+ (+) S^-.
```

`canon/shiab-existence-cl95.md` proves at least ONE such map exists (the Clifford
contraction) but holds OPEN the **uniqueness of the equivariant map / source-forced
selector identity** (Known Failure Modes, "Uniqueness of equivariant map"). The
decisive integer is

```
dim Hom_{so(14,C)}( Lambda^2 V (x) S , V (x) S ).
```

- `dim = 0`  -> no natural map; the Clifford contraction would have to vanish identically; "3 generations as proof" loses its carrier.
- `dim = 1`  -> the selector is UNIQUELY pinned (up to scale); the OPEN canon question closes with uniqueness.
- `dim > 1`  -> residual equivariant freedom; equivariance alone does NOT pin the shiab; an extra (observer / physical) choice is required.

We complexify: Spin(9,5) is a non-compact real form of Spin(14,C), and the
algebraic Hom-multiplicity is a complexified invariant, identical for so(9,5)
and so(14,C) = D_7. No metric-adjoint / d_A* choice enters this computation — the
multiplicity is a pure rep-theory invariant, fully determined by the data.

## Result (actual computed outputs)

Run: `python tests/shiab_codiff_intertwiner_dim.py`. Two independent methods agree.

**Irreducible decompositions (Racah-Speiser, each dimension-checked against the
product of factor dimensions):**

```
V (x) S^+   = 832 (omega_1+omega_7)  (+)  64 (S^-)                          [= 896 ✓]
V (x) S^-   = 832 (omega_1+omega_6)  (+)  64 (S^+)                          [= 896 ✓]
L2 (x) S^+  = 4928 (omega_2+omega_7) (+) 832 (omega_1+omega_6) (+) 64 (S^+) [= 5824 ✓]
L2 (x) S^-  = 4928 (omega_2+omega_6) (+) 832 (omega_1+omega_7) (+) 64 (S^-) [= 5824 ✓]
```

(The 832-dim irrep `W(omega_1+omega_7)` is exactly the Rarita-Schwinger vector-
spinor that appears as the gamma-trace kernel `raw_RS_kernel_rank_C = 832` in
`tests/oq_rk1_cl95_explicit_rep.py` — independent consistency.)

**Chiral 2x2 selector-multiplicity matrix `dim Hom(Lambda^2 V (x) S_x, V (x) S_y)`:**

```
            cod S+   cod S-
   dom S+      0        2
   dom S-      2        0
```

**Headline numbers:**

| selector space | dim |
|---|---|
| `Hom(Lambda^2 V (x) S^+, V (x) S^-)`  — the natural (chirality-flipping) shiab block | **2** |
| `Hom(Lambda^2 V (x) S^-, V (x) S^+)` | **2** |
| `Hom(Lambda^2 V (x) S^+, V (x) S^+)`  (chirality-preserving) | 0 |
| `Hom(Lambda^2 V (x) S^-, V (x) S^-)` | 0 |
| `Hom(Lambda^2 V (x) S, V (x) S)` with full Dirac `S = S^+ (+) S^-` | **4** |

The Clifford contraction `Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a}alpha) s`
uses one Clifford multiplication by a covector, so it is **chirality-flipping**
(`S^+ -> S^-`). Its home is therefore the dim-**2** block, and the
chirality-preserving blocks are 0 — consistent with the operator being odd.

**Where the 2 comes from (the two independent natural maps `Lambda^2 V (x) S^+ -> V (x) S^-`):**
the common constituents of `L2 (x) S^+` and `V (x) S^-` are
`W(omega_1+omega_6)` (dim 832, the vector-spinor / Rarita-Schwinger channel) and
`S^+` (dim 64, the Clifford-trace channel). Two common irreps -> two independent
equivariant maps. The Clifford contraction is ONE fixed linear combination of
these two Stein-Weiss-type projections; a second independent one exists.

## Cross-check (independent method)

The trivial-rep multiplicity in `M_xy = Lambda^2 V (x) (S_x)^* (x) V (x) S_y`,
computed by the Kostant/Klimyk alternating sum

```
m_0(M) = sum_{w in W(D_7)} (-1)^{l(w)} n_M( w.rho - rho ),   |W(D_7)| = 322560,
```

with `n_M` the weight multiplicities of `M` built by direct convolution of the
four factor weight systems, reproduces the same 2x2 matrix `[[0,2],[2,0]]` and the
same full-Dirac total `4`. By Schur, `m_0(M_xy) = dim Hom(Lambda^2 V (x) S_x, V (x) S_y)`.
Both methods agree exactly (the script asserts equality).

## Interpretation for the lead

**The lead "the shiab is the unique equivariant map" is KILLED.** The selector
multiplicity is **2** (natural chirality-flipping block) / **4** (full Dirac) —
strictly greater than 1. Spin(9,5)/so(14,C)-equivariance alone does NOT pin GU's
shiab: there is a 2-dimensional space of natural equivariant maps per chirality,
and the Clifford contraction is only one ray in it. Selecting GU's specific shiab
from this family requires an additional input (a choice of linear combination)
that equivariance does not supply.

This resolves the canon OPEN question "Uniqueness of equivariant map" in the
**negative**: the map is not unique up to scale. The honest canon update is
"multiplicity = 2 (resp. 4); the source-forced selector identity must come from a
structure beyond Spin(9,5)-equivariance, or it remains an observer's choice."

It is NOT `dim = 0` (a map exists — existence canon stands) and NOT `dim = 1`
(uniqueness fails). No quantity was tuned to hit 1, 343.73, or any target; the
FC4-HOLONOMY-01 dim=1 trap is explicitly avoided — the computed answer is 2/4.

## Well-definedness / choices

- The Hom-multiplicity is a complexified rep-theory invariant; **no metric-adjoint
  (`d_A*`) choice and no signature choice enters** — so(9,5) and so(14,C) give the
  same integer. The result is choice-independent.
- The only modeling decision is the meaning of `S`: a single half-spinor (then the
  natural odd map sits in the dim-**2** block `S^+ -> S^-`) versus the full Dirac
  `S^+ (+) S^-` (total dim **4**, all of it chirality-flipping). Both are > 1; the
  conclusion is robust to this choice.
