---
title: "Discharging OC1 / OC2: the non-compact fence of the Signed-Readout Boundary Theorem (R3)"
date: 2026-07-03
problem_label: "signed-readout-oc1-oc2"
status: exploration
internal_path: 5
parent: explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md
witness: tests/internal-paths/oc1_oc2_witness.py
witness_result: "15/15 checks PASS, exit 0 (2026-07-03)"
verdict_oc1: REDUCED-TO-NAMED-LEMMA
verdict_oc2: REDUCED-TO-NAMED-LEMMA (H-linear increment fully discharged; reduces to the same lemma as OC1)
---

# Discharging OC1 / OC2 for the non-compact case of R3

**Scope.** This note targets the two *abstract, GU-independent* hypotheses fenced in
Section 8 of `R3-signed-readout-standalone-theorem.md`. It does **not** touch canon,
the R3 draft, or any generation-count status. It stages exploration-grade analysis plus a
runnable finite witness. Honest bottom line up front:

| Hypothesis | Grade | One-line reason |
|---|---|---|
| **OC1** (continuous Fredholm realization) | **REDUCED-TO-NAMED-LEMMA** | Sub-parts (i) domain/self-adjointness and (iii) bounded-transform norm-continuity are discharged by standard theorems (Chernoff 1973; Booss-Bavnbek–Lesch–Phillips 2005). The irreducible residue is **one** named lemma: *uniform invertibility of the model operator at infinity* (= a uniform spectral gap of `D_t` off a compact set, along the whole path), which by Persson's decomposition principle **is** OC1's Fredholmness. |
| **OC2** (H-linear Fredholm realization) | **REDUCED-TO-NAMED-LEMMA** | The analytic content of OC2 is **entirely contained in OC1**. Given OC1, the extra clause "each `F_t` commutes with the quaternionic structure `J`" is **automatic** and is *discharged here*: `[D_t,J]=0 ⇒ [F_t,J]=0` by Borel functional calculus (proved + witnessed to `2.4e-14`). The classifying-space statement `Fred_H ≃ KO^{-4}` is Atiyah–Singer (1969). So OC2 = OC1's single lemma + a fully-discharged algebraic step. |

No discharge is claimed on a genuinely non-compact operator. What is claimed is the
*sharpest reduction*: OC1 and OC2 both collapse onto a **single** analytic lemma
(uniform invertibility at infinity), everything else being either a cited classical
theorem or an algebraic fact discharged in this note, and a computable witness on the
canonical non-compact index operator confirms the reduction end-to-end.

---

## 1. The two hypotheses, restated precisely

From Section 8 of the R3 standalone theorem, verbatim intent:

- **(OC1) Continuous Fredholm realization.** There is a fixed separable Hilbert space `K`
  and a norm-continuous map `t ↦ F_t ∈ Fred(K)`, where `F_t = D_t(1 + D_t^* D_t)^{-1/2}`
  is the bounded (Riesz) transform of a deformation family `{D_t}` of the non-compact Dirac
  operator on the open manifold `Y`, and the path stays in the Fredholm locus (0 ∉ essential
  spectrum, discrete sector transported continuously). *Given OC1, Theorem Z holds for `D_Y`
  verbatim* by Atiyah–Jänich (`Fred(K) ≃ ℤ × BU`).

- **(OC2) H-linear Fredholm realization.** The same map lands in the quaternionic Fredholm
  space, `t ↦ F_t ∈ Fred_H(K_H)`, `K_H = L^2(Y, ℍ^r)`, each `F_t` commuting with the
  quaternionic structure `J` (antilinear, `J^2 = -1`). *Given OC2, Theorem K holds verbatim*,
  `[F] ∈ [X, Fred_H(K_H)] = KSp^0(X) = KO^4(X)`, augmenting to `index_H ∈ ℤ`.

Both are *analytic* claims about a *specific* non-compact operator; the *topology*
(classifying-space theorems) is already unconditional. So the entire question is: put `D_Y`
(and its deformation family) into `Fred` / `Fred_H` continuously.

---

## 2. OC1: decompose into three sub-claims, discharge two, name the third

Write the abstract OC1 as the conjunction of three standard sub-claims. Assume, as the R3
fence already does, that `Y` is a **complete** Riemannian manifold and `D` is a Dirac-type
(first-order, formally self-adjoint, Clifford-symbol) operator — the generic setting of the
hypothesis.

### (i) Domain / essential self-adjointness — DISCHARGED (unconditional, cited)

> **Chernoff's theorem (1973).** A Dirac-type operator `D` on a *complete* Riemannian
> manifold, with the natural first-order symbol, is essentially self-adjoint on `C_c^∞(Y,S)`;
> its unique self-adjoint closure has domain the graph Sobolev space `{u ∈ L^2 : Du ∈ L^2}`.
> *(P. Chernoff, "Essential self-adjointness of powers of generators of hyperbolic
> equations," J. Funct. Anal. 12 (1973) 401–414; finite propagation speed.)*

This removes sub-part (i) of the R3 fence ("an explicit Sobolev domain and self-adjoint
extension for `D_Y`") **unconditionally, for any complete `Y`** — no operator-specific input.
The bounded transform `F = D(1+D^2)^{-1/2}` is then well-defined by Borel functional calculus
of a self-adjoint operator, `‖F‖ ≤ 1`.

### (ii) Fredholmness ⇔ invertibility at infinity — the ONE residual lemma

For a self-adjoint `D`, the bounded transform `F` is a Fredholm operator **iff** `0` is not in
the *essential* spectrum of `D` (standard; e.g. Higson–Roe, *Analytic K-homology*; the
essential spectrum of `F` is the closure of `{λ/√(1+λ^2) : λ ∈ σ_ess(D)}`, which avoids `0`
iff `0 ∉ σ_ess(D)`). And the essential spectrum is governed **entirely by the operator at
infinity**:

> **Persson's theorem / decomposition principle (1960).**
> `inf σ_ess(D^2) = lim_{K ↑ Y} inf { ⟨D^2 u, u⟩ / ‖u‖^2 : u ∈ C_c^∞(Y∖K) }`.
> *(A. Persson, Math. Scand. 8 (1960) 143–153.)* Equivalently, `0 ∉ σ_ess(D)` iff there is a
> compact `K ⊂ Y` and `δ > 0` with `‖Du‖ ≥ δ‖u‖` for all `u` supported outside `K`
> ("coercivity / invertibility at infinity").

Therefore OC1's Fredholmness is **equivalent to a single named lemma**:

> **Lemma (UII) — Uniform Invertibility at Infinity.** There exist a compact `K ⊂ Y` and
> `δ > 0` such that the model (asymptotic) operator `D_∞` is invertible with gap `≥ δ` outside
> `K`, **uniformly along the deformation** `t ↦ D_t`.

This is exactly the hypothesis of the **Callias–Anghel** index theory for open spaces
(C. Callias, Comm. Math. Phys. 62 (1978) 213–234; N. Anghel, "On the index of Callias-type
operators," GAFA 3 (1993) 431–438; Bott–Seeley): a Dirac operator perturbed by a potential
that is invertible with a uniform gap at infinity is Fredholm, with a computable index. UII is
*not* derivable from ellipticity alone on an open manifold — it is the genuine operator-specific
residue. It is the sharpest possible reduction: OC1 ⇔ (Chernoff, already true) + (UII).

### (iii) Norm-continuity of the bounded transform — DISCHARGED given a uniform gap (cited)

> **Booss-Bavnbek–Lesch–Phillips (2005).** On the set of self-adjoint Fredholm operators,
> the Riesz (bounded) transform `D ↦ F_D = D(1+D^2)^{-1/2}` is continuous from the *gap
> (Riesz) topology* to the operator-norm topology; `{self-adjoint Fredholm}` with this topology
> is a classifying space for `K^1`, and spectral flow = the induced map on `π_1`.
> *(B. Booss-Bavnbek, M. Lesch, J. Phillips, "Unbounded Fredholm operators and spectral flow,"
> Canad. J. Math. 57 (2005) 225–250.)*

So once UII gives a uniform gap along the path (keeping the family inside the self-adjoint
Fredholm set), norm-continuity `t ↦ F_t` — sub-part (iii) of the R3 fence — is **automatic**
from a cited theorem. A graph-continuous deformation `t ↦ D_t` with a uniform gap is
Riesz-continuous, hence `F_t` is norm-continuous and stays in `Fred(K)`.

### OC1 verdict

**REDUCED-TO-NAMED-LEMMA.** OC1 ⟺ Chernoff (unconditional) + Booss-Bavnbek–Lesch–Phillips
(unconditional given a gap) + **Lemma UII** (uniform invertibility at infinity along the path).
UII is the *entire* remaining content; it is the standard Callias–Anghel coercivity-at-infinity
condition and must be verified per operator. This is strictly sharper than the R3 fence, which
listed three separate analytic to-dos — two of the three are now cited theorems, and the third
is named as one clean lemma.

---

## 3. OC2: the H-linear increment is automatic — discharged here

Claim: **given OC1, OC2 adds no analytic content.** The only extra requirement is that each
bounded transform `F_t` commutes with the quaternionic structure `J`. This is a consequence of
`[D_t, J] = 0` via functional calculus, which we discharge:

> **Lemma (J-transport).** Let `D` be self-adjoint on `K_H` and `J` a bounded (antilinear)
> operator with `[D, J] = 0` on the domain of `D`. Then `J` commutes with every Borel function
> of `D`; in particular with `F = D(1+D^2)^{-1/2}`. Hence `F ∈ Fred_H(K_H)` whenever
> `F ∈ Fred(K)` and `[D,J]=0`.
>
> *Proof.* `J` commutes with the resolvents `(D - z)^{-1}` (apply `J` to `(D-z)u = v`; since
> `J` is antilinear it intertwines `(D - z)^{-1}` with `(D - z̄)^{-1}`, and self-adjointness
> makes the spectral measure real, so `J` commutes with `∫ f(λ) dE(λ)` for real Borel `f`).
> `F` is `f(D)` with `f(λ) = λ(1+λ^2)^{-1/2}` real and Borel. ∎

Consequently OC2 = **OC1 (same Lemma UII)** + the *algebraic, checkable, and here-discharged*
condition `[D_t, J] = 0`. The classifying statement itself is classical:

> **Atiyah–Singer (1969).** The quaternionic (skew-adjoint / `Cl_k`-linear) Fredholm operators
> form a classifying space for `KO^{-4} = KSp`; the augmentation `KSp^0(pt) = ℤ` is `index_H =
> index_C/2` (Kramers). *(M. Atiyah, I. Singer, "Index theory for skew-adjoint Fredholm
> operators," Publ. Math. IHÉS 37 (1969) 5–26.)*

Section 6 of R3 is the finite-dimensional case of this, already machine-certified. The
J-transport lemma is what carries it across the bounded transform.

### OC2 verdict

**REDUCED-TO-NAMED-LEMMA.** OC2 reduces to the *same* Lemma UII as OC1 plus the algebraic
condition `[D,J]=0`, and the map from that algebra to `F` is discharged here (Lemma J-transport,
plus a numerical witness to `2.4e-14`). No *new* analytic hypothesis beyond OC1 survives.

---

## 4. Finite / lattice witness — `tests/internal-paths/oc1_oc2_witness.py`

The witness realizes the reduction on the **canonical non-compact index operator**, the 1D
Callias / Jackiw–Rebbi operator `D = d/dx + m(x)` on `L^2(ℝ)` — the textbook example where
"Fredholm ⇔ invertibility at infinity" *is* the whole story (Callias index
`= ½(sgn m(+∞) − sgn m(−∞))`). Truncation to `[-L, L]` makes every operator a finite matrix,
so this is finite-dimensional evidence **for** the reduction, not a proof on the open manifold.
Result: **15/15 checks PASS, exit 0** (2026-07-03). Highlights, all machine-produced:

**Part 1 — OC1 mechanism (index via the doubler-free SUSY partners `H_∓ = D^*D, DD^*`).**
- Callias index reproduced exactly as signed localized zero-mode count:
  wall `m=+tanh`: `index = n_-(1) − n_+(0) = +1`; anti-wall: `−1`; gapped constant: `0` —
  each matches `½(sgn m(+∞)−sgn m(−∞))`.
- **Persson**: the mass gap of `D` = `√(bottom of σ_ess(H_∓))` tracks the mass at infinity to
  `≤ 4%`: `μ=0.5 → 0.518`, `μ=1.0 → 1.003`, `μ=2.0 → 2.002`.
- **Protection (Theorem Z mechanism)**: deforming the *interior* of `m` (growing bumps) while
  holding `m(±∞)` fixed keeps the index at `+1` across all 6 deformation steps — the index is
  locally constant exactly because the gap at infinity (UII) is held.
- **Gap collapse (UII fails)**: sending `m(±∞) → 0` collapses the mass gap
  `1.003 → 0.518 → 0.282 → 0.03`, switching off the Fredholm/protection mechanism — the
  concrete failure mode of OC1.

*Note on doubling.* A naive central-difference `D` gives index `0`: the fermion doubler
carries an opposite-chirality zero mode (the very artifact the R3 certificate avoids with
Ginsparg–Wilson). The witness sidesteps it by computing the index through the *bosonic* SUSY
Schrödinger partners `H_∓`, which have no doubler.

**Part 2 — OC1 sub-part (iii), bounded transform.** `‖F‖ = 0.9988 < 1`; spectrum of `F` is
Fredholm-shaped (98% of eigenvalues near `±1`, a thin kernel near `0`); the `F`-gap equals
`g/√(1+g^2)` (`0.707` vs predicted `0.707` at `g≈1`); and the Riesz map is numerically
Lipschitz — `‖F(D+εV) − F(D)‖ = 0.072, 0.036, 0.018, 0.009, 0.0045` for
`ε = 0.4,0.2,0.1,0.05,0.025` (clean linear vanishing), witnessing the BBLP continuity where the
gap holds.

**Part 3 — OC2, symmetry transport.** With `Ω = I⊗iσ_y`, `J = Ω·conj`, `J^2=-1`: a generic
quaternionic (`[A,J]=0`) operator has its **bounded transform still quaternionic** to
`max ‖Ω^{-1}FΩ − F̄‖ = 2.4e-14` over 200 operators — the numerical face of Lemma J-transport.
Rank-deficient quaternionic operators have even complex kernel (KSp augmentation) in all 50
trials; and the Callias double `A = D_cal ⊗ I_2` commutes with `J` exactly (`0.0`). So the
quaternionic structure rides through the bounded transform for free — OC2's increment is null.

---

## 5. Honest grades and the decisive next step

- **OC1 — REDUCED-TO-NAMED-LEMMA.** Discharged: domain/self-adjointness (Chernoff),
  norm-continuity (Booss-Bavnbek–Lesch–Phillips). Residue: **Lemma UII** — uniform invertibility
  of the asymptotic operator at infinity along the deformation (Callias–Anghel coercivity),
  equivalent by Persson to `0 ∉ σ_ess(D_t)` uniformly. **Decisive next step:** for the concrete
  target operator, exhibit the *model operator at infinity* `D_∞` and prove a uniform lower
  bound `‖D_∞ u‖ ≥ δ‖u‖` outside a compact set, uniform in `t` (a single spectral-gap estimate).
  That one estimate turns OC1 from REDUCED to DISCHARGED.

- **OC2 — REDUCED-TO-NAMED-LEMMA (increment discharged).** OC2 reduces to the *same* Lemma UII
  plus the algebraic `[D_t, J] = 0`; the transport of `J` through the bounded transform is
  proved here (Lemma J-transport) and witnessed to `2.4e-14`. **Decisive next step:** identical
  to OC1's — the same UII estimate closes OC2, after the (algebraic, already-checkable)
  verification that the target operator commutes with its quaternionic structure.

**Net.** The R3 non-compact fence, previously three analytic to-dos, is reduced to **one**
named lemma (UII) common to OC1 and OC2, with every other ingredient either a cited classical
theorem or discharged in this note, and a passing end-to-end witness on the canonical
non-compact index operator. This does **not** upgrade R3 to unconditional; it sharpens the
open condition to its minimal, citable core. No canon, paper, or generation-count status is
touched.

---

## 6. Falsification / where this would break

- **UII genuinely fails for the target** (0 ∈ σ_ess along the path): then `D_t` is not Fredholm,
  no integer is protected, and OC1/OC2 are *false*, not merely open — the witness's gap-collapse
  branch is exactly this regime.
- **`Y` not complete**: Chernoff fails; sub-part (i) is no longer free and a boundary/APS
  condition must be added.
- **`[D,J] ≠ 0`**: the operator is only `ℂ`-linear; the index lands in `KU`, need not be even;
  OC2 does not apply (this is R3 falsification F7, here made operator-explicit).
- **Deformation not gap-continuous** (leaves the Fredholm locus): BBLP continuity does not apply
  and the index can jump — but that jump is precisely spectral flow, i.e. the failure is visible
  and quantified, not silent.
