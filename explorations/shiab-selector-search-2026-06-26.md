---
title: "Shiab Selector Search — Does GU Determine Its Own Shiab?"
date: "2026-06-26"
status: complete
verdict: "NO_RESIDUAL_FREEDOM — gu_derived selectors leave a 4-real-dimensional family; selection to GU's unique canon shiab requires the still-OPEN source-forced (RS-sector) action. GU's quaternionic structure narrows but does not pin."
depends_on:
  - "canon/shiab-existence-cl95.md"
  - "tests/shiab_family_basis.py"
  - "tests/shiab_selector_sp64.py"
  - "tests/shiab_selector_quaternionic_Hlinear.py"
  - "tests/shiab_selector_complex_closure.py"
  - "tests/shiab_selector_seesaw_selfadjoint.py"
  - "tests/shiab_selector_gamma_trace.py"
  - "tests/shiab_codiff_intertwiner_dim.py"
  - "tests/oq_rk1_cl95_explicit_rep.py"
provenance: "SHIAB-03 standing result (family dim = 4 complex / >= 8 real). FC4-HOLONOMY-01 respected: nothing tuned to force dim 1."
integrator_notes_2026_06_26:
  - "Verifier verdict mildly_overstated / land_with_fixes: the headline (gu_derived selectors leave real dim 4; selection needs the open source action) is independently re-derived FOUR ways and stands. Fixes folded in below."
  - "FIX (sp64 step-5 bug): tests/shiab_selector_sp64.py's 'full Sp(64) gives 0' side-check used X = e0 e1 e2 e3 - h.c., which is IDENTICALLY ZERO (e0e1e2e3 is Hermitian), so that demonstration is vacuous and the '||[W,X]|| ~ O(1) nonzero' write-up is wrong (the real output is 0). This is a SIDE argument; it does not affect the headline surviving-dim 4 (independently re-derived). The operative GU content is the right-H / Sp(1) commutant (quaternionic-linearity), not the literal full structure group Sp(64)."
  - "CAVEAT (signature-contingent): the sole gu_derived reduction (8R -> 4R via quaternionic/Sp(64) right-H linearity) holds ONLY under the (9,5) signature forcing Cl(9,5)=M(64,H). Canon flags (7,7) as a possible alternative (Cl(7,7)=M(128,R), REAL spinor, no quaternionic J), under which the 'strip the artificial doubling' 8->4 argument collapses. So the one gu_derived cut is contingent on the (9,5) Frobenius result."
  - "PHRASING: the surviving real-dim-4 H-linear space is a real form of complex dim 4 for the FULL Dirac spinor (the 'complex dim 2' holds per chiral block only)."
---

# Shiab Selector Search — Does GU Determine Its Own Shiab?

Canon-adjacent exploration. This file records the selector-search assessment over
the SHIAB-03 natural-equivariant family and answers, honestly, whether any
GU-derived selector (or combination) pins GU's shiab to a unique operator.

## 0. The question

The shiab is the natural equivariant map

```
Phi : Omega^2(Y^14) (x) S  ->  Omega^1(Y^14) (x) S      (Y^14 signature (9,5))
```

SHIAB-03 established (three independent character methods + explicit Cl(9,5) rep)
that **equivariance alone does not pin Phi**: the natural Spin(9,5)-equivariant
family is

```
complex dim = 2 per chiral block  =  4 for the full Dirac spinor
real    dim = 8        (Cl(9,5) = M(64,H): quaternionic doubling of the 4 complex maps)
```

with two complex channels per block: the **Clifford-trace / contraction channel**
(GU's canon shiab) and the **Rarita-Schwinger / wedge channel** (h.w. omega_1 + omega_6).
GU's canon shiab `Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s` is verified
equivariant (matrix defect 0.00e+00) and sits at real coordinates **(1, 0, 1, 0)**
in the ordered basis `[contract_+-, wedge_+-, contract_-+, wedge_-+]` — the pure
Clifford-trace channel, equal weight on both chiralities, zero RS component.

The selector search asks: is there a **GU-derived** condition (not a generic
textbook naturality import) that cuts this family down to GU's one map?

## 1. Selector inventory and origin classification

Five candidate selectors were computed from first principles over the verified
Cl(9,5) = M(64,H) ~ M(128,C) representation. Each was tagged by **origin**
(gu_derived vs textbook_natural) and by whether its surviving subspace **contains
GU's canon shiab**.

| Selector | Origin | Surviving dim | Contains canon shiab? |
|---|---|---|---|
| Spin(9,5)-equivariance (baseline) | textbook_natural | 4 complex / 8 real | yes (it is in the family) |
| **Sp(64) / right-H gauge-equivariance** | **gu_derived** | **4 real** | **yes** |
| **Quaternionic H-linearity (commute with J)** | **gu_derived** | **4 real** | **yes** |
| Complex closure / d^2 = 0 | textbook_natural | **0** (unsatisfiable) | no (kills everything, incl. canon) |
| Self-adjoint / seesaw zero | textbook_natural | 4/8 (vacuous) **or** 0 (over-constrains) | depends on undetermined fold reading |
| Gamma-trace / RS-channel | textbook_natural | 1 complex / block (2C / 4R) | **no — excludes canon, selects wedge-6·contract** |

Key reading of the table:

- Only **two** selectors are genuinely **gu_derived**, and they are the **same
  constraint**. Sp(64) = U(64,H) is the GU gauge group forced by Cl(9,5) = M(64,H);
  its operative, well-posed content is commutation with the quaternionic commutant
  H = {1, i, J, k} (the Sp(1) = right-H factor), which is *exactly* the Quaternionic
  H-linearity selector. (The literal "full Sp(64) structure group" reading is
  ill-posed for a Clifford-built map and trivializes to 0; rejected.) Both scripts
  cut **8 real -> 4 real** by removing the quaternionic-doubling i-multiples
  `i·Phi_k`, and both **retain** the canon shiab.

- The three textbook_natural selectors that *do* move the dimension are each
  disqualified as a GU selector: **closure** is unsatisfiable (and GU withholds
  d^2 = 0 as conditionally obstructed — the computation shows the obstruction does
  NOT vanish, eigenvalues O(1e5–1e6)); **seesaw self-adjointness** is either vacuous
  or forces the Clifford-even codifferential d_A* (which the Clifford-odd family
  cannot equal — the already-resolved "shiab != codifferential" result); **gamma-trace**
  cleanly reaches dim 1 but lands on the spin-3/2 combination `wedge - 6·contract`,
  **actively excluding GU's own Clifford-trace formula**. None is GU-derived, and the
  only one that pins picks the wrong element.

## 2. Residual dimension surviving ALL gu_derived selectors

The gu_derived selectors are the Sp(64) gauge selector and the Quaternionic
H-linearity selector. They impose the identical condition (commute with J), so
their intersection is their common surviving subspace:

```
residual surviving ALL gu_derived selectors  =  REAL dim 4
                                              =  span_R { contract_+- , wedge_+- , contract_-+ , wedge_-+ }
                                              =  2 channels (Clifford-trace, Rarita-Schwinger)  x  2 chiral blocks (S+->S-, S-->S+),
                                                 all with REAL coefficients.
```

This is a **real form** (the fixed set of the antilinear involution
sigma(T) = -J_cod T J_dom), not a complex subspace: it has no complex dimension,
real dim 4. It is **NOT 1**.

Computation backing each leg (all defects machine-zero, 0.00e+00):

- Baseline equivariant family = 8 real (SHIAB-03; reconfirmed by
  `tests/shiab_family_basis.py`, canon coords (1,0,1,0), contract _|_ wedge Frobenius
  overlap 0).
- J commutes with every Clifford generator (`max_a ||[J, e_a]|| ~ 1e-15`), hence with
  every Clifford word, hence both channel operators (contract AND wedge) are right-H
  linear -> all four `Phi_k` survive (defect 0).
- i anticommutes with J -> the four imaginary partners `i·Phi_k` are killed
  (defect `2||U conj(W)|| != 0`). SVD of the real H-linearity constraint per block:
  singular values `[5.29e2, 2.16e2, 0, 0]` -> rank 2 -> 2 survivors/block -> 4 total.

The canon shiab `(1, 0, 1, 0)` has H-linearity defect 0.00e+00 in both blocks, so it
**lies inside the surviving 4-real-dim space** — retained, but not isolated.

## 3. Does any combination of gu_derived selectors pin to 1?

**No.** The two gu_derived selectors are co-extensive (both = "commute with J"), so
"combining" them adds nothing beyond real dim 4. There is genuine **residual
freedom** of real dimension 4 - 1 = 3 beyond GU's single map, parameterized by:

1. **Channel mixing** — Clifford-trace (contract) vs Rarita-Schwinger (wedge). Both
   channels are equivariant, real, and H-linear; nothing GU-derived prefers one.
2. **Independent chiral-block weights** — the coefficients on `S+ -> S-` and
   `S- -> S+` need not be tied; GU's single formula happens to tie them (c is
   chirality-odd), but that tie is a property of the *written formula*, not of any
   derived symmetry.

No GU-derived equivariance/gauge condition removes (1) or (2). Pinning to GU's
exact `(1,0,1,0)` requires, beyond the gu_derived J-linearity:

- **Channel pick** "take the degree-1 Clifford-trace, not the degree-3 RS wedge":
  this is **definitional** — it is reading off GU's written canon formula, classified
  **assumed / textbook_natural**, NOT derived from tau+ / IG / action. (It would cut
  4R -> 2R: `span_R{contract_+-, contract_-+}`.)
- **Chiral tie + scale** "same real coefficient on both blocks, normalized": also a
  property of the written formula, **assumed**. (Cuts 2R -> 1.)

So uniqueness is reachable only by **adopting GU's written formula as a definition**
(an assumed postulate, the channel + tie + scale read directly off the canon
expression) OR by supplying the **source-forced selector identity** — the
tau+ / inhomogeneous-gauge-group / observerse **source action** in the RS sector
whose variation/coupling singles out one element of the family. That action is
**OPEN and not present in the repo** (canon/shiab-existence-cl95.md "What This Does
Not Establish"; the cycle-2 source-selection certificate explicitly: source data
"do not select" the rank-one orbit — the middle arrow is missing).

## 4. Minimal selecting data (and its provenance)

The smallest stack that reaches a unique map, with each leg's provenance:

| # | Condition | Cuts | Provenance |
|---|---|---|---|
| 1 | Spin(9,5)-equivariance | -> 4C / 8R | textbook_natural |
| 2 | Quaternionic H-linearity (= Sp(64) right-H), Cl(9,5)=M(64,H) | 8R -> **4R** | **gu_derived** |
| 3 | Channel = Clifford-trace (degree-1), not RS wedge (degree-3) | 4R -> 2R | **assumed** (reads GU's written formula; NOT derived) |
| 4 | Tie chiral blocks + fix scale | 2R -> 1 | **assumed** (property of the single written formula) |
| — | *OR* source-forced RS-sector action selecting one element | family -> 1 | **gu_derived in principle, OPEN/unavailable** |

The **GU-derived** content stops at line 2 (residual real dim **4**). Everything that
takes 4 -> 1 is either **assumed** (lines 3–4, definitional reading of the canon
formula) or the **open source action** (the only in-principle-derivational route,
not supplied).

## 5. Plain answer: does GU determine its own shiab?

**Not from its derived symmetry principles alone — not yet.** GU's genuinely
GU-derived structure (the (9,5) signature forcing Cl(9,5) = M(64,H), a real
quaternionic spinor S = H^64, and the Sp(64) = U(64,H) gauge group) **does real
work**: it strips the artificial complex doubling and narrows the natural
equivariant family from real dimension 8 to real dimension 4. But it **stops at 4**.
GU's canon shiab is **one specific element** of that 4-real-dimensional family — the
Clifford-trace channel with equal chiral weight, real coordinates (1,0,1,0) — picked
out by GU's **written formula** (a definitional/assumed choice of channel + chiral
tie + scale), not forced by any GU-derived selector. The residual 3 real dimensions
(channel mixing + independent chiral-block weights) are not closed by equivariance,
gauge-covariance, quaternionic-linearity, closure, self-adjointness, or
gamma-tracelessness. Closing them requires the still-**OPEN source-forced selector
identity** — the RS-sector observerse/source action. This is fully consistent with
the earlier theory-gap finding (SHIAB-03; canon "What This Does Not Establish"):
**the selection is a genuine gap, deferred to an action GU has not yet supplied.**

## 6. Next obligation

Construct or obtain the **source-forced selector identity**: the GU
tau+ / inhomogeneous-gauge-group / observerse **source action** in the
Rarita-Schwinger sector whose stationary/coupling condition selects a single element
of the 4-real-dimensional family (and in particular tests whether it lands on GU's
canon (1,0,1,0) Clifford-trace channel, or instead favors the RS wedge / a mixed
combination / untied chiral weights). Concretely:

1. Write the field-theoretic source term (the "middle arrow" the cycle-2 certificate
   names as missing) coupling the shiab to GU's matter/source content.
2. Vary it and read off which family coordinate `(c_contract+-, c_wedge+-,
   c_contract-+, c_wedge-+)` is critical/forced.
3. Either (a) show it forces (1,0,1,0) — GU determines its own shiab — or (b) show it
   forces a different element — GU's canon formula must be revised — or (c) show no
   source-natural functional exists — the selection is adopted as a **postulate** and
   should be labeled as such in canon.

Until that action is in hand, the honest canon status is: **existence (SHIAB-02) +
non-uniqueness (SHIAB-03) settled; selection OPEN**. No GU-derived selector pins the
shiab to dimension 1; the gu_derived selectors leave a >= 4-real-dimensional family,
and GU's canon shiab is one element of it.
