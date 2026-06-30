---
title: "N4 IG Dimension Matching: Does IG = Sp(64) ⋉ Ω¹(ad P) Reconcile 8256 vs 16384?"
date: 2026-06-23
problem_label: "n4-ig-dimension-matching"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# N4 IG Dimension Matching: Does the IG Structure Reconcile 8256 vs 16384?

**Status.** Reconstruction-grade. Steps tagged `[verified]`, `[reconstruction]`, or
`[open]` per repo convention.

## 1. Problem statement

The RESEARCH-STATUS Nguyen lane carries a residual labelled N4: the gauge algebra
`dim_R sp(64) = 8256` versus the figure `16384 = 2^14` that Nguyen's U(128)
dimension-matching argument required. The prior exploration
(`explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`) marked N4 RESOLVED
by **dissolution**: it argued 16384 was never a requirement on the gauge algebra, only
a (7,7) coincidence. That is correct as far as it goes, but it sidesteps the sharper
question the residual actually poses, which is the question this note answers:

> **Does the inhomogeneous gauge group structure `IG = G ⋉ Ω¹(ad P)` — with its
> translation part `Ω¹(ad P)` — supply additional dimensions that reconcile the 8256 vs
> 16384 mismatch, or is the gap a genuine structural mismatch that the IG mechanism
> cannot and does not close?**

This is a bounded representation-theory bookkeeping question. The failure condition set
by the task: *if no natural mechanism closes the 8256 vs 16384 gap, name it as an OPEN
structural mismatch — do not paper over it.* This note takes that instruction literally:
it tests the IG mechanism as a dimension-supplier and reports honestly what it does and
does not do.

## 2. Established context (what this builds on)

- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`: Cl(9,5) ≅ M(64,ℍ),
  S = ℍ^64, natural gauge group Sp(64), `dim_R sp(64) = 8256`. §4.3 item 1 and §5.1(b)
  explicitly flag "adjoint bundle dimension matching" as `[open]` — this is the residual
  N4 targets.
- `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`: τ⁺ is purely
  group-theoretic; IG = Sp(64) ⋉ Ω¹(ad P) is a well-defined infinite-dimensional Lie
  group; the double-coset equivariance θ(τ⁺(g_a)·ω·τ⁺(g_b)) = Ad(g_b)⁻¹θ(ω) holds for
  Sp(64). All `[verified]`. This note does **not** re-derive those; it accepts them.
- `explorations/misc/super-ig-algebra-construction-2026-06-23.md`: the IG infinitesimal
  algebra is `ig = Ω⁰(ad P) ⋉ Ω¹(ad P)`, the connection-space analogue of the Poincaré
  algebra, translation part abelian.
- `explorations/anomaly-and-bordism/anomaly-sp64-global-pi15-2026-06-23.md`: its FC-3 ("subgroup escape via
  τ⁺ selection") is the same uniqueness gate that bounds this note's verdict.

## 3. The numbers (all arithmetic verified by direct computation)

For n = 64 (computed, `python` pass):

| Quantity | Value | Formula |
|---|---|---|
| `dim_R sp(64)` (compact symplectic / quaternionic unitary `usp(128)`) | **8256** | `n(2n+1) = 64·129` `[verified]` |
| `dim_R M(64,ℍ) = dim_R Cl(9,5)` | **16384** | `4n² = 2^14` `[verified]` |
| `dim_R u(128)` (Nguyen's (7,7) gauge algebra) | **16384** | `128²` `[verified]` |
| Hermitian-ℍ complement `Herm(64,ℍ)` | **8128** | `16384 − 8256` `[verified]` |
| `Herm(64,ℍ)` closed form | **8128** | `n + 2n(n−1)` (real diagonal + quaternionic off-diagonal) `[verified]` |
| `dim_R S = ℍ^64` | **256** | `4n` `[verified]` |
| Pointwise fiber of `Ω¹(ad P)` (the IG translation part) | **115584** | `dim Y¹⁴ × dim sp(64) = 14·8256` `[verified]` |

Two facts already jump out and frame the entire analysis:

- **(F1) The full Clifford / matrix algebra splits as a direct sum through the gauge
  algebra:** `M(64,ℍ) = sp(64) ⊕ Herm(64,ℍ)` as a real vector space, with
  `8256 + 8128 = 16384`. `[verified]`
- **(F2) The IG translation part is the wrong size by orders of magnitude in both
  directions.** Pointwise it is `14·8256 = 115584` (≫ 16384), and as a *function space*
  `Ω¹(Y¹⁴, ad P)` it is infinite-dimensional. There is no finite "16384" anywhere in the
  IG translation sector. `[verified]`

## 4. Computation — testing the IG mechanism as a dimension-supplier

The residual implicitly hopes that the move from the homogeneous gauge group `G` to the
**in**homogeneous `IG = G ⋉ Ω¹(ad P)` might "add back" the missing `16384 − 8256 = 8128`
dimensions — that the affine translation sector is exactly the place where the gap is
closed. We test this directly.

### 4.1 What IG adds, dimensionally

The inhomogeneous extension adjoins the abelian translation part `V = Ω¹(Y¹⁴, ad P)` to
the gauge algebra `gP = Ω⁰(Y¹⁴, ad P)` (super-ig file §2):

```
ig = gP ⋉ V,   [(ε,a),(η,b)] = ([ε,η], ad_ε b − ad_η a),  V abelian.
```

Per **point** of Y¹⁴ the two summands have real dimensions:

```
fiber(gP) = sp(64),        dim 8256
fiber(V)  = T*Y ⊗ sp(64),  dim 14·8256 = 115584.
```

So the *increment* IG supplies at the algebra level is `+115584` per point (and an
entire infinite-dimensional function space globally), **not** `+8128`. The number 8128
— the only increment that could turn 8256 into 16384 — **does not appear anywhere in the
IG translation sector.** `[verified]`

### 4.2 Diagnosis: a degree/sector mismatch, not a dimension shortfall

Why doesn't IG supply 8128? Because IG and the "16384" target live in **different
mathematical sectors** that an honest accounting must keep separate:

- **16384 is an associative-algebra dimension** (Cl(9,5) ≅ M(64,ℍ), the full endomorphism
  algebra `End_ℝ(S)` after the quaternionic structure is accounted for). It is a *0-form*
  / pointwise-fiber number: it counts endomorphisms of the spinor module S.
- **8256 is a Lie-algebra dimension** (the gauge algebra sp(64) ⊂ M(64,ℍ)). Also a 0-form
  / pointwise number, and it sits *inside* 16384 as a direct summand (F1).
- **The IG translation part Ω¹(ad P) is a 1-form / function-space sector.** Its size is
  governed by `dim Y¹⁴ = 14` and the gauge fiber, not by `End_ℝ(S)`. It is the analogue
  of the abelian translation/momentum sector of the Poincaré group, not of any spinor
  endomorphism count.

These are three different "directions" in the bookkeeping. IG enlarges the **1-form gauge
sector**; the 16384 lives in the **0-form Clifford/endomorphism sector**. Enlarging the
former cannot, even in principle, hit a specific target in the latter — they are not the
same vector space and not even the same form-degree. `[reconstruction]`

This is the heart of the matter and it is *stronger* than the prior file's dissolution:
the prior file said "16384 was never required." This note says **why the IG mechanism
specifically is structurally incapable of being the reconciler**: it operates in the
wrong sector (1-form gauge translations), of the wrong size (115584 / ∞, not 8128), so
"IG closes the gap" was never a coherent possibility to begin with.

### 4.3 Where the missing 8128 actually goes (the genuine reconciliation)

There **is** a clean, finite, representation-theoretic statement that reconciles 8256 and
16384 — but it is **not** the IG mechanism; it is the direct-sum split (F1):

```
M(64,ℍ) = sp(64)  ⊕  Herm(64,ℍ)
16384   = 8256    +  8128.
```

Here:
- `sp(64) = { X ∈ M(64,ℍ) : X† = −X }` (quaternionic skew-Hermitian) is the **gauge
  algebra** — the infinitesimal symmetries that *preserve* the quaternionic Hermitian
  form on S = ℍ^64. `[verified]`
- `Herm(64,ℍ) = { X ∈ M(64,ℍ) : X† = +X }` (quaternionic Hermitian) is **not** a Lie
  subalgebra; it is the complementary set of *self-adjoint* operators. These are the
  spinor **bilinear / observable** operators (mass-type and current-type bilinear pairings
  `S ⊗ S → ℝ`, real diagonal "norms" + off-diagonal quaternionic pairings, dimension
  `n + 2n(n−1) = 8128`). `[verified]`

So the full `2^14 = 16384` of the Clifford algebra **is** accounted for, exactly, with
the gauge algebra as one summand. The 8128 "missing" dimensions are not missing — they
are the Hermitian (observable/bilinear) half of `End_ℝ(S)`, which was *never* supposed to
be gauge symmetry. In the (7,7) era U(128) absorbed all 16384 into one Lie algebra only
because `u(128)` is itself a real form of `gl(128,ℂ)` of dimension `128² = 16384`; that
absorption conflated gauge generators with bilinear operators, which is precisely the
defect the (9,5)/quaternionic correction repairs. `[reconstruction]`

### 4.4 Cross-check: does the shiab need 16384 in the gauge sector?

The shiab Φ: Ω²(Y¹⁴)⊗S → Ω¹(Y¹⁴)⊗S is built from `Cl(9,5)` and `S = ℍ^64` only
(prior file §3, `[verified]`). Its pointwise output dimension is governed by
`dim_R S = 256` and the form degrees, with no reference to `dim g`. Independently, the
adjoint-bundle / Yang-Mills sector is governed by `dim sp(64) = 8256`. These two are
disjoint bundles (spinor bundle vs. ad P). So no consistency condition forces the gauge
algebra to carry the full 16384; the 16384 is fully consumed by `End_ℝ(S)` (F1), of which
the shiab uses the Clifford-action part and the gauge sector uses the skew-Hermitian part.
`[verified, inherited from prior file §3]`

### 4.5 The one place 8256 vs 16384 could still bite: gauge-group uniqueness

The reconciliation in 4.3 is exact **given** that the gauge group is Sp(64). The residual
risk is not a dimension shortfall but a **uniqueness** question, and it is shared with the
global-anomaly file's FC-3:

- The identification "gauge group = Sp(64) = full quaternionic-unitary automorphism group
  of S = ℍ^64" is a `[reconstruction]`-grade structural argument (anomaly audit §5.1(a)).
- If the τ⁺ construction in fact selects a *proper subgroup* H ⊂ Sp(64) (e.g. the
  stabiliser of a distinguished spinor, or Spin(9,5) ⊂ Sp(64) itself), then
  `dim h < 8256`, and the split in 4.3 would read `M(64,ℍ) = h ⊕ (complement)` with a
  *larger* non-gauge complement — still summing to 16384, still no "gap," but the
  reconciliation would attach to a different number than 8256.

In every such case the **direct-sum reconciliation survives** (any Lie subalgebra of
`M(64,ℍ)` has a complementary subspace inside the fixed 16384), so the bookkeeping never
develops a genuine *gap*. What is not yet pinned is *which* subalgebra is load-bearing.
This is exactly N5's gauge-group-uniqueness gate, not an IG-dimension obstruction.
`[reconstruction]`

## 5. Result

**Verdict: CONDITIONALLY_RESOLVED.**

Direct answer to the task's question: **the IG = Sp(64) ⋉ Ω¹(ad P) structure does NOT
reconcile the 8256 vs 16384 mismatch — and that is the correct answer, because there is no
finite gap for it to close.** The IG translation part is a 1-form gauge-sector object of
pointwise size 115584 (infinite-dimensional globally), living in a different form-degree
and a different bundle from the 0-form Clifford-endomorphism number 16384. The
reconciliation that *is* genuine is the orthogonal direct-sum decomposition
`M(64,ℍ) = sp(64) ⊕ Herm(64,ℍ)`, `8256 + 8128 = 16384` (verified arithmetic): the gauge
algebra is exactly the skew-Hermitian half of the Clifford endomorphism algebra, and the
complementary 8128 dimensions are the spinor-bilinear (Hermitian/observable) operators
that were never gauge symmetry. The (7,7) "16384 = dim gauge algebra" requirement was the
artifact of `u(128)` conflating both halves into one Lie algebra; the (9,5)/quaternionic
correction separates them. **This is not a genuine obstruction and not a paper-over: the
total 2^14 is exactly accounted for, with the gauge algebra as a literal direct summand.**

The verdict is held at CONDITIONALLY_RESOLVED (not RESOLVED) because the clean accounting
is contingent on the gauge-group identification, and because §4.3's "8128 = spinor
bilinears" identification is reconstruction-grade.

**Explicit failure conditions (any one falsifies the resolution):**

1. **(Subalgebra-escape / uniqueness, FC shared with anomaly-sp64-global-pi15 FC-3.)**
   If the τ⁺ / shiab construction provably selects a gauge group whose Lie algebra is
   *not* `sp(64)` and whose complement inside `M(64,ℍ)` is *not* identifiable with the
   spinor-bilinear sector, then the specific `8256 + 8128` accounting in §4.3 is the wrong
   split (though a direct-sum reconciliation would still exist for the new subalgebra).
2. **(Bilinear-sector misidentification.)** If `Herm(64,ℍ)` (the 8128-dim quaternionic
   Hermitian operators) does *not* coincide, as a Spin(9,5)-representation, with the space
   of independent spinor bilinear pairings `S ⊗ S → ℝ` carried by Cl(9,5) — i.e. if the
   8128 complement is some other representation with no bilinear/observable interpretation
   — then the "where the missing 8128 goes" story in §4.3 fails and the complement becomes
   an unexplained sector. (Requires a Spin(9,5)-equivariant decomposition of `End_R(S)`
   into symmetric + antisymmetric pairings to confirm the 8128 lands as claimed.)
3. **(Hidden gauge-sector dimension requirement.)** If some GU consistency condition
   (unitarity, the Dirac–DeRham–Einstein index complex, or a Ward identity) independently
   *requires* the gauge algebra to carry `2^14` dimensions — i.e. requires the bilinear
   operators in `Herm(64,ℍ)` to be gauged — then 8256 is genuinely too small and the
   mismatch is a real obstruction after all. (No such condition is currently identified;
   the shiab does not impose one, §4.4.)

## 6. Open questions

- **Confirm the 8128 = bilinear-sector identification** by an explicit Spin(9,5)-equivariant
  decomposition `End_R(S) = sp(64) ⊕ Herm(64,ℍ)` matched to the symmetric/antisymmetric
  Clifford bilinear forms `S ⊗ S → ℝ`. This would upgrade §4.3 from reconstruction to
  verified and would let the verdict move toward RESOLVED. (Discharges FC-2.)
- **Gauge-group uniqueness (the live coupling).** Pin which subalgebra of `M(64,ℍ)` the
  τ⁺/shiab data actually select. Shared gate with `anomaly-sp64-global-pi15` FC-3 and the
  anomaly audit §5.1(a). Resolving it discharges FC-1 and would close N4 to RESOLVED.
- **Relation to the prior N4 file.** This note supersedes the prior file's framing: the
  prior dissolution ("16384 was never required") is correct but incomplete; the present
  note adds (i) the proof that the IG mechanism is structurally the wrong sector to be the
  reconciler, and (ii) the positive direct-sum accounting that says where all 16384
  dimensions actually live.

## 7. References

Repo files:
- `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md` — prior N4 (dissolution).
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` — §4.3, §5.1(a)/(b) flag this residual.
- `explorations/anomaly-and-bordism/anomaly-sp64-global-pi15-2026-06-23.md` — FC-3 (subgroup escape) couples here.
- `explorations/misc/super-ig-algebra-construction-2026-06-23.md` — IG infinitesimal algebra `ig = gP ⋉ V`.

Standard:
- Lawson–Michelsohn, *Spin Geometry*, App. I (Cl(p,q) ≅ M(N,ℍ) for (p−q) mod 8 = 4; bilinear forms).
- Bröcker–tom Dieck, *Representations of Compact Lie Groups*, Ch. I §5 (quaternionic unitary group, `dim usp(2n) = n(2n+1)`).

---

*Filed: 2026-06-23. Tests the IG = Sp(64) ⋉ Ω¹(ad P) structure directly against the
8256 vs 16384 residual. Finding: IG is the wrong sector to be a reconciler (1-form gauge
translations, size 115584/∞, not the 0-form 8128); the genuine reconciliation is the
direct-sum split M(64,ℍ) = sp(64) ⊕ Herm(64,ℍ). Not a genuine obstruction; total 2^14
exactly accounted for. Verdict bound to CONDITIONALLY_RESOLVED by gauge-group uniqueness
(FC-1, shared with anomaly-sp64-global-pi15 FC-3) and the reconstruction-grade
bilinear-sector identification (FC-2).*
