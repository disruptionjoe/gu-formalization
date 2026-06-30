---
title: "Is GU's shiab the codifferential d_A*?  Explicit Cl(9,5) resolution"
date: 2026-06-26
problem_label: "shiab-vs-codiff"
status: reconstruction
verdict: DISTINCT (shiab != d_A*; canon SC1 sec 3.5 CONFIRMED, persona adjointness-collapse REFUTED)
---

# Is GU's shiab the codifferential d_A*?  Explicit Cl(9,5) resolution

## 1. The dispute

Two readings of GU's "ship-in-a-bottle" (shiab) middle map collide:

- **canon SC1** (`sc1-shiab-domain-codomain-2026-06-23.md` sec 3.5 and sec 3.6
  candidate B): the shiab Phi is the natural Clifford-contraction
  `Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s`. It has the *same type*
  as the formal codifferential `d_A* : Omega^2(S) -> Omega^1(S)` but a *different
  formula* ("no Clifford contraction; uses connection and Hodge star"). SC1 calls
  them **DISTINCT**.
- **Persona steel-man** (`rs-middle-map-persona-steelman-2026-06-26.md`, lead C1):
  the FHE / Homomorphic-Encryption, Info-Coding, Probabilist, and Clifford-04
  lenses each independently argue **adjointness forces shiab = (d_A)\***, i.e. the
  shiab IS the metric codifferential of the spinor-twisted complex ("the single
  strongest convergence" in the sprint).

This file resolves the dispute by **explicit matrix computation** in the verified
`Cl(9,5) = M(64,H) ~ M(128,C)` representation (`tests/oq_rk1_cl95_explicit_rep.py`).
Nothing is tuned. Code: `tests/shiab_vs_codiff_cl95.py`.

## 2. What was built (first principles, explicit rep)

S = C^128 model of the `M(64,H)` spinor module; generators `e[a] = c(e^a)` with
`e[a]^2 = eta_a I`, signature (9,5); chirality `omega = e_0...e_13`, chiral
projectors S = S^+ (+) S^-, each 64 over C (32 over H). Form factors:
`Lambda^1 = R^14` (dim 14), `Lambda^2 = R^14 ^ R^14` (dim 91).

1. **shiab Phi** as a concrete linear map
   `Lambda^2(x)S (11648) -> Lambda^1(x)S (1792)`, built block-wise from
   `Phi(e^b^e^c (x) s) = e^b (x) c(e^c)s - e^c (x) c(e^b)s`. The antisymmetrization
   on the form factor is **metric-free**; the metric/signature enters *only*
   through `c(.)`.

2. **codifferential symbol** `delta_xi = sigma(d_A*)(xi)`, the unique zeroth-order
   (bundle-map) object derivable from the first-order operator d_A*:
   `delta_xi(alpha (x) s) = (iota_{xi^#} alpha) (x) s`. This is *exactly* the
   adjoint-symbol of the de Rham forward map d_A (`sigma(d_A)(xi) = xi ^ . (x) id_S`),
   so comparing Phi to delta_xi is a direct test of "is shiab = (d_A)\* ?". It acts
   as the **identity on the spinor factor S**.

## 3. Actual computed outputs

| quantity | shiab Phi | codiff symbol delta_xi |
|---|---|---|
| domain -> codomain (dim_C) | 11648 -> 1792 | 11648 -> 1792 |
| rank_C (= image dim) | **1792** (surjective) | **1664** (= 13 x 128) |
| kernel_C | 9856 | 9984 |
| rank_H | 896 | 832 |
| Frobenius norm | 152.63 | 137.79 |
| spinor factor action | **Clifford c(.)** (S-nontrivial) | **identity** (S-trivial) |
| operator order | **0** (algebraic) | **1** (differential) |
| chirality grading | **ODD** (swaps S^+<->S^-) | **EVEN** (preserves S^+, S^-) |

Chirality grading, graded Frobenius masses (machine output):

```
Phi      :  +->+  0.00e+00    +->-  107.93     -->+  107.93     -->-  0.00e+00
delta_xi :  +->+  97.43       +->-  0.00e+00   -->+  0.00e+00
```

The shiab sends `Lambda^2(x)S^+` **entirely into** `Lambda^1(x)S^-` (the +->+
block is the **zero matrix**); the codifferential symbol sends `Lambda^2(x)S^+`
**entirely into** `Lambda^1(x)S^+`. Their restricted images live in the two
*complementary* summands S^- and S^+, intersecting only in {0}.

**Best proportionality constant.** Minimizing `||Phi - lambda*delta_xi||_F`:

```
<delta_xi, Phi>_F = 0   (exactly)
best lambda       = 0.000e+00
residual          = 152.63 = full ||Phi||   (the codiff captures NONE of the shiab)
overlap |<delta_xi,Phi>| over 5 random xi = [0, 0, 0, 0, 0]
```

The overlap is **zero for every xi** because each surviving Phi block is a single
**traceless** gamma (`max|Tr e_a| = 0`, Clifford-odd) while each delta block is a
scalar multiple of the identity; `Tr(scalar . gamma) = 0`.

## 4. Why this is decisive and choice-independent

Three independent, metric-free invariants each kill `shiab = d_A*`:

1. **Operator order.** Phi is zeroth-order (no derivatives); d_A* is first-order.
   A nonzero first-order operator cannot equal a zeroth-order one. The steel-man's
   only escape is to match Phi against the *symbol* of d_A* (point 2/3).
2. **Disjoint restricted images (matrix-level, no inner product).** As matrices,
   `Phi(Lambda^2(x)S^+) subset Lambda^1(x)S^-` while
   `delta_xi(Lambda^2(x)S^+) subset Lambda^1(x)S^+`. Since `S^+ cap S^- = {0}`,
   `Phi != lambda*delta_xi` for any lambda != 0, and lambda = 0 gives Phi = 0
   (false). This uses only the omega-eigenspace decomposition, no metric choice.
3. **Clifford parity.** Phi is Clifford-**odd** (built from `c(e^a)`, which
   anticommutes with omega); the d_A* symbol is Clifford-**even** (identity on S).
   Parity is a representation invariant.

The single-number confirmation `lambda = 0` uses the standard Hilbert-Schmidt
inner product (a CHOICE), but it is forced by `Tr(gamma) = 0`, which holds for any
nondegenerate trace pairing on the rep; and invariants (1)-(3) need no inner
product at all. **The conclusion is choice-independent.** Metric choices that *were*
made and do not affect the verdict: (a) Phi's form antisymmetrization is metric-free;
(b) delta_xi raises xi with the fixed (9,5) metric eta and uses a representative
non-null xi, but the comparison is xi-independent; (c) Hilbert-Schmidt positive-
definite matrix pairing for the single lambda number only.

## 5. Verdict

**DISTINCT. The GU shiab is NOT the codifferential d_A* (nor its principal symbol).**
canon SC1 sec 3.5 is **confirmed**; the persona "adjointness forces shiab = (d_A)\*"
convergence (lead C1) is **refuted** at the level of the explicit rep.

The grain of truth in the persona reading: the shiab *is* an adjoint -- but the
adjoint of **Clifford multiplication on the spinor factor**, not of the **exterior
derivative on the form factor**. Concretely, the genuine Hermitian adjoint
`Phi* : Lambda^1(x)S -> Lambda^2(x)S` *raises* form degree (so it is not any
codifferential) and is itself S-nontrivial (Clifford). The two "adjoints" the
personas conflated are:
- de Rham codifferential = adjoint of `d` on the FORM factor -> symbol `iota_xi (x) id_S`, S-trivial, chirality-even;
- Clifford contraction (the shiab) = adjoint of `c(.)` on the SPINOR factor -> S-nontrivial, chirality-odd.

The shiab is the symbol-level analog not of d_A* but of the **Dirac/Clifford
contraction** (the 2-form sibling of the gamma-trace). Lead C1's reduction of the
`d^2=0` obstruction to "a single curvature/commutator term" remains a separate
question; it does not rest on the shiab being d_A*, which it is not.

## 6. Files

- code: `tests/shiab_vs_codiff_cl95.py` (runnable; imports the verified anchor)
- anchor: `tests/oq_rk1_cl95_explicit_rep.py`
- canon claim resolved: `canon/shiab-existence-cl95.md`,
  `explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md` sec 3.5 / 3.6(B)
- persona lead refuted: `explorations/persona-and-dialectic/rs-middle-map-persona-steelman-2026-06-26.md` lead C1
