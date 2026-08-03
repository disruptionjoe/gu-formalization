---
artifact_type: exploration
status: exploration
doc_type: lemma-note
created: 2026-08-03
work_item: M-M2
register: lab/process/improvement-register-2026-08-03.md
panel_refs:
  - "lab/process/eleven-lens-audit-2026-08-03.md (finding B17: real family dim 16 not 8; measured commutant End_Spin(S±_R) = H)"
  - "lab/process/improvement-register-2026-08-03.md (M-M2, rep-lens items RT-O2/RT-F3)"
title: "M-M2 form-spinor decomposition and the shiab family dimension: multiplicity-free Lambda^2 V (x) S+ = S+ (+) Sigma_1+ (+) Sigma_2+ (64+832+4928=5824) and V (x) S- = S+ (+) Sigma_1+ (64+832=896) give dim_C Hom = 2 per chirality block by inspection (replacing the |W(D_7)|=322560 Weyl-sum machinery); the REAL refinement: End_Spin(9,5)(S±_R) = H, so the real equivariant family is dim_R 16 = 4 x 4 (complexification cross-check S_R (x) C = 2 S_C), and the correct constraint chain is 16 -> 8 (J-commutation) -> 4 (full H-linearity / Sp(64)-equivariance) — NOT canon's 8 -> 4"
grade: "EXACT — finite multiplicity-free representation theory (exact-integer Klimyk re-verification this session) plus exact real-commutant bookkeeping; corrects a canon COUNT and a canon CONSTRAINT NAME without moving any verdict (the dim-4 endpoint and the OPEN selector are unchanged)"
claim_status_change: none
canon_verdict_change: none
depends_on:
  - canon/shiab-existence-cl95.md
  - tests/shiab_codiff_intertwiner_dim.py
  - tests/chase/MOVE-4/move4_spinor_square_forms.py
  - lab/process/eleven-lens-audit-2026-08-03.md
outcome: "Complex Hom = 2 per chirality block re-derived structurally (multiplicity-free decompositions, exact Klimyk, exit 0); real family dimension corrected 8 -> 16 (two independent derivations agree); corrected chain 16 -> 8 -> 4 established; feeds CORRECTION SHIAB-06 in canon/shiab-existence-cl95.md (same batch)"
---

# M-M2 — the form-spinor decomposition and the corrected real family dimension

**What this is.** Register item M-M2. Part I replaces the Weyl-sum machinery
behind canon's SHIAB-03 intertwiner count with a two-decomposition argument
readable by inspection. Part II is the audit's B17 correction worked out: the
real Spin(9,5)-equivariant shiab family has dim_R **16**, not the "≥ 8" in
`canon/shiab-existence-cl95.md:75`, and the "8 → 4 by the SAME J-commutation"
step at `:81` conflates two different constraints. The corrected chain is
**16 → 8 → 4**; the endpoint 4 (and everything canon derives from it) survives
**iff** the imposed constraint is full Sp(64)-equivariance (H-linearity), not
J-commutation alone. Canon receives a dated correction note (CORRECTION
SHIAB-06) in the same batch; no verdict moves.

## Part I — the complex count by inspection

Work over C: so(14,C) = D_7, V = C^14 the vector rep, S± the 64-dim chiral
spinors. In orthogonal (e_i) coordinates, with s± = (1/2,...,1/2,±1/2):

| irrep | highest weight | dim |
|---|---|---|
| S+ | (1/2,1/2,1/2,1/2,1/2,1/2,+1/2) | 64 |
| Sigma_1+ (gamma-traceless vector-spinor, Rarita-Schwinger) | (3/2,1/2,1/2,1/2,1/2,1/2,-1/2) | 832 |
| Sigma_2+ (Cartan product, 2-form-spinor) | (3/2,3/2,1/2,1/2,1/2,1/2,+1/2) | 4928 |

(The superscript + labels the congruence class of S+: the class of a weight,
sum of coordinates mod 2, is constant on an irrep; both decompositions below
land entirely in the S+ class.) The two decompositions, each
**multiplicity-free**:

```text
Lambda^2 V (x) S+  =  S+ (+) Sigma_1+ (+) Sigma_2+      64 + 832 + 4928 = 5824 = 91 x 64
V (x) S-           =  S+ (+) Sigma_1+                    64 + 832        =  896 = 14 x 64
```

(The second is the classical Clifford-multiplication split V (x) S- =
S+ (+) ker(c), with ker(c) = Sigma_1+ irreducible.) Since both sides are
multiplicity-free and share exactly {S+, Sigma_1+}:

```text
dim_C Hom_{so(14,C)}(Lambda^2 V (x) S+, V (x) S-) = 2    per chirality block,
```

the mirror block (S- -> S+, all last-coordinate signs flipped by the diagram
automorphism) likewise gives 2, and the chirality-diagonal blocks give 0
(wrong congruence class). Total for the full Dirac spinor: **4** — exactly
SHIAB-03's number, but now visible from two small decompositions instead of a
Kostant/Klimyk sum over |W(D_7)| = 322560. The two channels are the ones canon
names: the Clifford-trace channel (S+) and the Rarita-Schwinger channel
(Sigma_1+). The standing three-way certificate
`tests/shiab_codiff_intertwiner_dim.py` is unchanged and corroborates.

Session re-verification (scratchpad script, `_local/cas-venv` python, exact
integer arithmetic, exit 0): Weyl dimension formula for each of the five
highest weights (64, 14, 91, 832, 4928); full Klimyk (Racah-Speiser)
decomposition of ad (x) S+ and V (x) S- over D_7 returning exactly the
multiplicity-free lists above; Hom counts 2/2/0 per block as stated; dimension
saturations 5824 = 91x64 and 896 = 14x64 exact.

## Part II — the real refinement: 16, then 8, then 4

**The commutant.** S±_R (dim_R 128) are quaternionic-type real irreducibles of
Spin(9,5) (from Cl(9,5) = M(64,H)), so

```text
End_{Spin(9,5)}(S±_R) = H     (dim_R 4)  — audit B17, measured commutant.
```

The point canon missed: End = H contains the *antilinear* commutant. Writing
H = C_i (+) j C_i, only the C_i half is i-linear; the j C_i half is
i-antilinear. A real-linear equivariant map has no obligation to be i-linear,
so the real Hom space sees all four dimensions of H, not two.

**The count (two independent derivations, agreeing).**

1. *Complexification cross-check.* Quaternionic type means
   S_R (x)_R C ≅ 2 S_C (full Dirac: 256-real-dim S_R complexifies to two
   copies of the 128-dim complex Dirac spinor). Since
   Hom_R(A,B) (x) C = Hom_C(A_C, B_C):

   ```text
   dim_R Hom_{Spin(9,5)}(Lambda^2 V (x) S_R, V (x) S_R)
     = dim_C Hom(Lambda^2 V (x) 2 S_C, V (x) 2 S_C) = (2 x 2) x 4 = 16.
   ```

2. *Common-constituent count.* The real modules share four irreducible real
   constituents, each of multiplicity 1 on each side: [S+]_R, [S-]_R,
   [Sigma_1+]_R, [Sigma_1-]_R. Each contributes Hom_R(X_R, X_R) = H:
   4 channels x dim_R H = **16**.

**The corrected chain.** Let i, j be the complex and quaternionic structures
on S_R (End = H = R<i,j>), acting on both domain and codomain through the
spinor factor. On the 16-real-dim family:

- *Split by i.* Hom_R = (i-linear) (+) (i-antilinear), and F -> jF is an
  equivariant bijection between the halves, so each has dim_R 8. The i-linear
  half is Hom_C(Lambda^2 (x) S_C, V (x) S_C): dim_C 4, dim_R 8 — consistent.
- *Impose J-commutation (F j = j F).* On the i-linear half, conjugation by j
  is an antilinear involution of the dim_C-4 space; its fixed set is a real
  form, dim_R 4. On the i-antilinear half, F -> jF carries the j-commuting
  antilinear maps bijectively onto that same real form: dim_R 4. Total
  **J-commuting family: dim_R 8**.
- *Impose full H-linearity (commute with i AND j — canon's "Sp(64) right-H
  structure", i.e. Sp(64)-equivariance).* This is the i-linear, j-commuting
  piece alone: **dim_R 4**.

```text
16  --(J-commutation)-->  8  --(full H-linearity / Sp(64)-equivariance)-->  4
```

**What canon got wrong, precisely (feeds CORRECTION SHIAB-06):**

- SHIAB-03's "GU's actual REAL quaternionic spinor doubles this to real Hom
  dimension >= 8" undercounts: the doubling accounted for C inside End(S_R)
  but omitted the antilinear half j C. The correct number is 16 = 4 x dim_R H,
  and it is exact, not a bound.
- SHIAB-04's "the SAME J-commutation constraint ... reduces the natural family
  from real dim 8 to real dim 4" names the wrong constraint: J-commutation
  cuts 16 to 8; it is full H-linearity (Sp(64)-equivariance) that reaches 4.
- The **endpoint 4 is unchanged**, so SHIAB-04's downstream analysis (GU's
  shiab is one element of the 4-dim family; residual freedom 3) survives
  verbatim — but only under the honest hypothesis that full Sp(64)-
  equivariance is the imposed GU-derived constraint. If only J-commutation
  were justified as GU-derived, the family would be 8-dimensional and the
  residual freedom 7, not 3. Which hypothesis GU's own structure earns is part
  of the still-OPEN selector question (SHIAB-02/-04); this note does not
  adjudicate it.

Aside, out of scope here: under the (7,7) alternative (real type,
S_R (x) C = S_C, End = R) the same bookkeeping gives a dim_R-4 family with no
quaternionic cut available at all; the signature ledger is register item
M-H4, not this note.

## Grade / honesty

EXACT. Part I is finite multiplicity-free representation theory, re-verified
this session by exact-integer Klimyk (session script, not a committed
certificate; the committed evidence remains `tests/shiab_codiff_intertwiner_dim.py`
and the MOVE-4 checksum). Part II is exact commutant bookkeeping on top of the
audit's measured End_Spin(S±_R) = H (B17), with the complexification
cross-check and the constituent count agreeing at 16. No numerics are
load-bearing. `claim_status_change: none`: the selector stays OPEN, the shiab
existence verdict is untouched; what changes is a dimension count (8 -> 16)
and a constraint name inside canon's discussion, executed as CORRECTION
SHIAB-06 in `canon/shiab-existence-cl95.md` in this batch.

## Layer-0 fence

Family dimensions are channel counts in an equivariant family. Nothing here
selects GU's operator, derives a generation count, or reads a multiplicity as
physics.
