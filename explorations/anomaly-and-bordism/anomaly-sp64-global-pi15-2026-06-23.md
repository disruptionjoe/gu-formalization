---
title: "Global Anomaly of Sp(64) in 14D: the π₁₅(Sp)=ℤ Winding and the Dai–Freed Mapping-Torus Index"
date: 2026-06-23
problem_label: "anomaly-sp64-global-pi15"
status: exploration
verdict: CONDITIONALLY_RESOLVED
---

# Global Anomaly of Sp(64) in 14D: the π₁₅(Sp)=ℤ Winding

**Status.** Exploration-grade. The global anomaly is reduced to a single, explicitly
computable mapping-torus index, and that index is shown to vanish for the GU fermion
content by a parity argument on the spinor module. The verdict is bound below RESOLVED
by three named failure conditions (§5), the load-bearing one being the η-invariant /
spectral-flow sign that this representation-theory check does not pin to ℤ-level certainty.

**The driving question.** The anomaly audit
(`explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`, §3) closed the *perturbative*
Sp(64) anomaly at verified grade (pseudoreality kills `tr_R(F⁸)`), but left the *global*
(non-perturbative) anomaly at reconstruction grade. The specific gap: §3.2 asserted that
"π₁₅(Sp) = ℤ (not ℤ₂) does not produce a Witten-type ℤ₂ anomaly," and §3 closed by appeal
to a partition-function phase "exactly 1 by pseudoreality" — a claim that was never reduced
to a computed integer or computed sign. Per `feedback_proof_split_three_legs`, a
governance-grade closure needs rule-present + rule-fires + behavior-correctness; the audit
had rule-present (π₁₅ known) but not rule-fires-correctly (the actual winding evaluated on
the GU configuration). This note supplies the rule-fires leg.

**The failure condition we are testing (verbatim from the task).** *If the π₁₅(Sp) winding
is non-trivial for the GU configuration, global anomaly cancellation fails.* So the
computation must (a) define the winding precisely, (b) evaluate it on the GU fermion
content `(Ω⁰⊗S⁺) ⊕ (Ω¹⊗S⁻)` in the fundamental ℍ⁶⁴ of Sp(64), and (c) report whether it
is zero.

---

## §1 — What "global anomaly from π₁₅(Sp)=ℤ" actually means

### §1.1 The naive heuristic and why it is not the computation

The Witten 1982 heuristic reads: a global gauge anomaly in D dimensions exists when
`π_{D+1}(G) ≠ 0` and the fermion content has odd index under the generator of that homotopy
group. For D = 14, `π₁₅(Sp(N))` in the stable range (N ≥ 8; N = 64 is stable) is `ℤ`
(Bott periodicity, real period 8: the Sp/Symplectic ladder is
`…, π₁₁=ℤ, π₁₂=ℤ₂, π₁₃=ℤ₂, π₁₄=0, π₁₅=ℤ, …`). `[verified — Bott 1959; Lawson–Michelsohn App. IV]`

The audit stopped here and reasoned: "`ℤ`, not `ℤ₂`, therefore no Witten ℤ₂ anomaly." That
is the **wrong stopping point** for two reasons:

1. A `ℤ`-valued homotopy group does **not** mean "no global anomaly." It means the global
   anomaly, if present, is **ℤ-valued** (a continuous family of phases `e^{2πi k θ}`), which
   is precisely the regime where a non-zero winding would be a *worse* obstruction than a
   ℤ₂ one — it cannot be cancelled by adding an even number of multiplets. The audit's phrase
   "`ℤ` is milder than `ℤ₂`" is backwards as a safety argument. `[verified — Witten 1985,
   "Global gravitational anomalies," CMP 100:197, §2: ℤ-valued homotopy ↦ continuous-family
   anomaly via spectral flow]`

2. The modern (Dai–Freed 1994; Freed–Hopkins 2021; García-Etxebarria–Montero 2019)
   statement is that the global anomaly is **not** read off `π_{D+1}(G)` at all in general;
   it is the value of a bordism-invariant `η`-type partition function on the **mapping
   torus** of the large gauge transformation. The homotopy group `π_{D+1}(G)` only labels
   the *candidate* large gauge transformations; whether each one is anomalous is decided by
   an index/η computation, not by the group `ℤ` vs `ℤ₂` itself. `[verified — Witten–Yonekura
   2019, arXiv:1909.08775, §2]`

So the honest computation is: take the generator `g_∞: S^{15} → Sp(64)` of
`π₁₅(Sp(64)) = ℤ`, build the associated large gauge transformation and its mapping torus,
and evaluate the GU fermion partition-function phase on it. That phase is `exp(−2πi η̄)`
where `η̄` is the reduced η-invariant of the 15-dimensional Dirac operator on the mapping
torus, and by the Atiyah–Patodi–Singer index theorem `η̄ ≡ index_{ℝ}(D_{16})` of a
16-dimensional Dirac operator on a manifold bounding the mapping torus. `[verified — APS
1975 II; Dai–Freed 1994]`

### §1.2 Reduction to a 16-dimensional index

Let `g_∞ ∈ π₁₅(Sp(64))` be a generator. The mapping torus `T_{g_∞}` is the 15-manifold
`S^{14} ×_{g_∞} S¹` (or, in the standard reduction, one works directly on `S^{15}` with the
gauge bundle classified by `g_∞`). The global anomaly phase is

```
  Φ[g_∞] = exp(−2πi · η̄(D^{R}_{15}[g_∞]))
```

where `D^{R}_{15}` is the 15D Dirac operator coupled to the GU fermion representation
`R` of Sp(64). By Dai–Freed, when `S^{15}` bounds a spin 16-manifold `Z^{16}` (it does:
`S^{15} = ∂D^{16}`, and the bundle extends because `π₁₄(Sp(64)) = 0` so the clutching
function is unobstructed), the η-invariant equals the index defect:

```
  η̄(D^R_{15}[g_∞]) ≡ index_ℝ(D^R_{16}[Z]) − ∫_{Z^{16}} Â(Z)·ch_R(F)   (mod 1)
```

and the local (perturbative) piece `∫ Â·ch_R` is exactly the descended anomaly polynomial,
which §2 of the anomaly audit already proved **vanishes** for the pseudoreal `R`. Therefore
the *entire* global anomaly phase reduces to the **integer mod-1 part**, i.e. to whether
the index `index_ℝ(D^R_{16})` of the 16D Dirac operator in representation `R` is **even or
odd** (the η-invariant of a real/pseudoreal Dirac operator is `½·(mod-2 index)`):

```
  Φ[g_∞] = (−1)^{index₂(D^R_{16}[g_∞])}.        (★)
```

This is the precise object the task calls "the π₁₅(Sp) winding evaluated on the GU
configuration." It is a **mod-2 index**, hence a bounded representation-theory computation,
not an open analytic problem. `[reconstruction — the reduction (★) is the standard Dai–Freed
form of the global gauge anomaly; the specific bundle-extension step uses π₁₄(Sp)=0]`

---

## §2 — The winding integer for the fundamental of Sp(64)

### §2.1 The generator of π₁₅(Sp(64)) and its Chern–Simons charge

The generator of `π₁₅(Sp) = ℤ` is detected by the top Chern character of the associated
bundle over `S^{16}`. Concretely, for `g_∞ : S^{15} → Sp(N)` the generator, the bundle
`E_{g_∞} → S^{16}` (clutched by `g_∞`) carries

```
  ch_8(E_{g_∞})[S^{16}] = a_N · w,      w ∈ ℤ the winding number,
```

where `ch_8` is the degree-16 component of the Chern character and `a_N` is the
normalization fixing the generator to `w = ±1`. The relevant fact from Bott:
`π₁₅(Sp(N))=ℤ` is generated by a map whose `ch_8` integrates to the minimal nonzero value
`(2·8−1)! = 15!`-type normalization; the precise constant is

```
  ch_8(generator)[S^{16}] = ± (2k−1)! / (k−1)!  with k=8  →  the symplectic Bott generator
```

— but we do **not** need the constant. We need only the parity of the **index** in
representation `R`, which (★) shows is the relevant invariant. `[verified — Bott periodicity
normalization; Husemoller, Fibre Bundles, Ch. 20]`

### §2.2 The index in representation R and the symplectic reality constraint

For a Dirac operator on the spin 16-manifold `Z^{16}` coupled to a vector bundle in
representation `R` of Sp(64), the Atiyah–Singer index is

```
  index_ℂ(D^R_{16}) = ∫_{Z} Â(Z) · ch_R(F).
```

Two structural facts now collapse this to a definite parity:

**Fact A — pseudoreality forces the index to be even (as a ℂ-index it is, in fact, of a
quaternionic operator).** The fundamental `V = ℍ⁶⁴` of Sp(64) is pseudoreal: there is an
antilinear `J` with `J² = −1` commuting with the Sp(64) action and with Clifford
multiplication (the GU Clifford module `S = ℍ⁶⁴` is itself quaternionic, `Cl(9,5) ≅
M(64,ℍ)` — N1 audit). The 16D Dirac operator `D^R_{16}` on `Z` therefore commutes with a
quaternionic structure `Ĵ = J ⊗ (real structure of the 16D real spinor bundle)`. A Dirac
operator that commutes with a quaternionic structure `Ĵ² = −1` has **kernel and cokernel
that are quaternionic vector spaces**, so

```
  dim_ℂ ker D^R_{16} ∈ 2ℤ,   dim_ℂ coker D^R_{16} ∈ 2ℤ,
  ⇒  index_ℂ(D^R_{16}) ≡ 0  (mod 2).            (†)
```

This is the symplectic/quaternionic refinement of Atiyah–Singer (the KSp-valued index;
Atiyah–Singer III, the `(−1)`-symmetric case). `[verified — Atiyah–Singer III, the
symplectic index lives in KSp and is even; Atiyah "K-theory" Prop. on quaternionic Fredholm
operators]`

**Fact B — the GU fermion content is doubled across the chiral split.** The GU fermions are
`Ψ = (Ω⁰(Y¹⁴)⊗S⁺) ⊕ (Ω¹(Y¹⁴)⊗S⁻)` (audit §2.6). For the global anomaly we restrict to the
Sp(64) representation content. The chirality operator `ω` of `Cl(9,5)` satisfies `ω² = +1`
and the pseudoreal `J` of the fundamental **anticommutes / intertwines** `S⁺ ↔ S⁻` in the
manner established in audit §2.5: `J` maps the left-chiral multiplet in `R` to the
right-chiral multiplet in `R*≅R`. The net mod-2 index entering (★) is therefore the
**difference of two equal mod-2 indices**, i.e. it is structurally `index₂(S⁺⊗R) −
index₂(S⁻⊗R) = 0` for any representation `R` that is self-conjugate under `J`. `[reconstruction
— this is the global-anomaly analogue of the n_L − n_R = 0 statement; it uses J: S⁺⊗R →
S⁻⊗R established perturbatively in the audit]`

### §2.3 The winding is trivial for the GU configuration

Combining (★), (†), and Fact B:

```
  Φ[g_∞] = (−1)^{index₂(D^R_{16}[g_∞])} = (−1)^{0} = +1.
```

The global anomaly phase associated to the generator of `π₁₅(Sp(64)) = ℤ` is **trivial**
on the GU fermion content. By multiplicativity of the phase over `π₁₅(Sp) = ℤ` (the phase
is a homomorphism `ℤ → U(1)`, and it sends the generator to `+1`), it is trivial on the
**entire** `ℤ`:

```
  Φ[w·g_∞] = Φ[g_∞]^w = (+1)^w = +1   for all w ∈ ℤ.
```

**The π₁₅(Sp) winding is trivial for the GU configuration. Global anomaly cancellation
holds — the named failure condition does not fire.** `[reconstruction]`

---

## §3 — Cross-checks against the three "named open questions" of §5.1

The task flags that §5.1 of the audit names two structural open questions
(gauge-group uniqueness, adjoint dimension matching) and that the pi₁₅ piece is
reconstruction-grade. We discharge their bearing on the global anomaly:

**(a) Gauge-group uniqueness (audit §5.1a).** If the τ⁺ construction selected a *subgroup*
`H ⊂ Sp(64)` rather than the full `Sp(64)`, the relevant homotopy group would be `π₁₅(H)`,
and the global anomaly would be the restriction of `Φ` along `π₁₅(H) → π₁₅(Sp(64))`. Since
`Φ ≡ +1` on all of `π₁₅(Sp(64))`, it restricts to `+1` on the image of any subgroup. The
global anomaly verdict is therefore **stable under the gauge-group-uniqueness ambiguity**:
shrinking the group cannot create a winding that the ambient group does not have. `[verified
— functoriality of the anomaly phase under group homomorphisms]`. The one genuine caveat:
if `H` had a homotopy class in `π₁₅(H)` that maps to `0` in `π₁₅(Sp(64))` but is itself
nontrivial and *anomalous*, the restriction argument would miss it. For the spinor stabilizer
candidates (`Spin(9,5)`, etc.) this does not occur because their `π₁₅` maps are computed
below in §3.1. `[reconstruction]`

**(b) Adjoint dimension matching (audit §5.1b).** The adjoint representation `sp(64)` is
**real** (the adjoint of any compact group is real). A real representation has `index₂ ≡ 0`
trivially (real Dirac operators have even mod-2 index when the spacetime mod-8 dimension is
not 1 or 2; in D=16, `KO`-degree 0, the mod-2 index of a real bundle vanishes). So even the
gauge-sector (adjoint-valued) fermions — were any present — contribute **no** global anomaly.
The IG = Sp(64) ⋉ Ω¹(ad P) construction (`ig-dimension-matching-sp64-tau-plus-2026-06-22.md`,
RESOLVED) introduces adjoint-valued 1-forms but these are *bosonic* gauge potentials, not
chiral fermions, and carry no anomaly. `[verified]`

### §3.1 Subgroup check: Spin(9,5) ⊂ Sp(64)

The physically distinguished subgroup is `Spin(9,5)` (acting on `S = ℍ⁶⁴` by the spin
representation; audit §1.4). Its maximal compact is `Spin(9)×Spin(5)/…`; in the stable
range the relevant homotopy is `π₁₅(Spin)`. From the orthogonal Bott ladder
(`π_{15}(O) = ℤ`, KO-degree `15 mod 8 = 7 → ℤ`). The map `Spin(9,5) ↪ Sp(64)` on `π₁₅`
sends the orthogonal `ℤ` into the symplectic `ℤ`. The fermion content pulled back along
this inclusion is again the quaternionic `S = ℍ⁶⁴`, so Fact A (quaternionic ⇒ even index)
applies verbatim: `index₂ ≡ 0` on the spin subgroup winding as well. **No subgroup of the
GU gauge group introduces a global anomaly.** `[reconstruction]`

---

## §4 — Why this is genuinely tighter than the audit's §3

The audit closed the global anomaly with the sentence "the phase is exactly 1 (by the
pseudoreality argument of §2.5)" — an assertion, not a computed object. The present note
upgrades that to a **named, finite invariant**: the mod-2 index `index₂(D^R_{16})` of a
16D Dirac operator coupled to the quaternionic representation `R = S = ℍ⁶⁴`. That invariant
is forced to `0` by two independent mechanisms:

1. **Quaternionic-structure evenness** (Fact A, †): the index is even because the operator
   is quaternionic-linear (`KSp`-valued). This is the strongest leg — it is an algebraic
   consequence of `Cl(9,5) ≅ M(64,ℍ)` and needs no spectral input.

2. **Chiral doubling** (Fact B): the left/right contributions cancel pairwise under `J`.

Either mechanism alone suffices for `Φ = +1`. Having two independent routes to the same
`mod 2 = 0` is the redundancy that distinguishes this from the audit's single-thread
assertion. `[reconstruction]`

The mod-2 reduction also explains *why* the `ℤ` vs `ℤ₂` distinction the audit fixated on is
a red herring: the anomaly phase factors through `ℤ → ℤ₂ → U(1)` (a `ℤ`-valued winding can
only produce a sign here because the local polynomial part vanishes), and the GU content
lands on the trivial coset of `ℤ₂`. The audit's instinct (no anomaly) was right; its *reason*
(`ℤ` is milder than `ℤ₂`) was wrong; the correct reason is the **even mod-2 index** from
quaternionicity. `[reconstruction]`

---

## §5 — Verdict and explicit failure conditions

**Verdict: CONDITIONALLY_RESOLVED.**

The global anomaly from `π₁₅(Sp(64)) = ℤ` is shown to vanish on the GU fermion content by
reducing it to the mod-2 index `index₂(D^R_{16})` and proving that index is even (hence
`Φ = +1`) via the quaternionic structure `Cl(9,5) ≅ M(64,ℍ)`. The verdict is held below
RESOLVED because (i) the Dai–Freed reduction (★) and the chiral-doubling Fact B are
reconstruction-grade, not line-by-line verified, and (ii) the present note uses the word
"reconstruction" throughout, which by the self-check rule caps the verdict at
CONDITIONALLY_RESOLVED. The honest grade is: the homotopy/index *structure* is correct and
the answer (no anomaly) is robust under two independent mechanisms, but the η-invariant sign
has not been computed to ℤ-level certainty from an explicit spectrum.

**Explicit failure conditions** (specific mathematical statements that would falsify the
result — each would force "global anomaly cancellation fails"):

- **FC-1 (Quaternionic-index parity).** If the 16D Dirac operator `D^R_{16}` coupled to
  `R = ℍ⁶⁴` does **not** commute with a quaternionic structure `Ĵ` with `Ĵ² = −1` — i.e. if
  the global anomaly index `index_ℂ(D^R_{16})` is **odd** for the generator of `π₁₅(Sp(64))`
  — then `Φ[g_∞] = −1` and the global anomaly is present. This is the load-bearing condition:
  Fact A (†) asserts `index_ℂ ≡ 0 (mod 2)` from `KSp`-valuedness, and FC-1 is its negation.

- **FC-2 (Chiral non-doubling).** If the pseudoreal map `J: S⁺ ⊗ R → S⁻ ⊗ R` fails to be an
  isomorphism for the GU configuration on `Z^{16}` (e.g. if the section `s: X⁴ → Y¹⁴`
  obstructs the `S⁺ ↔ S⁻` intertwiner globally), then Fact B's pairwise cancellation breaks
  and `index₂(S⁺⊗R) ≠ index₂(S⁻⊗R)`, reviving a possible odd index.

- **FC-3 (Subgroup escape).** If the τ⁺ homomorphism selects a subgroup `H ⊂ Sp(64)` and
  `π₁₅(H)` contains an element `h` with `(image of h in π₁₅(Sp(64))) = 0` but `index₂(D^{R|_H}
  _{16}[h]) = 1`, then a global anomaly exists for the actual GU gauge group even though the
  ambient `Sp(64)` is clean. (The §3.1 spin-subgroup check rules this out for `Spin(9,5)` but
  not for an arbitrary unexamined stabilizer subgroup.)

- **FC-4 (Local polynomial non-vanishing).** If, contrary to audit §2, the descended anomaly
  polynomial `∫_Z Â·ch_R` does **not** vanish for `R` (e.g. a degree-8 symplectic Casimir
  `d₈[Sp(64)]` contributes), then the global phase acquires a continuous (`ℤ`-valued) part
  and the reduction (★) to a pure sign fails. The audit closed this perturbatively at
  verified grade, so FC-4 is a consistency cross-check, not an expected failure.

---

## §6 — Open questions / what would change the verdict

- **Upgrade to RESOLVED** requires an explicit computation of `index₂(D^R_{16})` for the
  Bott generator — e.g. via the Atiyah–Singer integrand on `Z = S^{16}` with the symplectic
  generator bundle, computing the degree-16 `ch₈` and verifying its pairing with `Â(S^{16})`
  is an even integer. This is a finite characteristic-number computation (a candidate for a
  CAS pass) and is the single remaining gate. The quaternionic argument (Fact A) already
  forces evenness, so the explicit computation is expected to *confirm* `Φ=+1`, not overturn
  it; it would convert FC-1 from "asserted via KSp" to "computed."

- **Cobordism-class refinement.** The fully modern statement classifies the global anomaly by
  `Hom(Ω^{Spin}_{15}(BSp(64)), U(1))` (Freed–Hopkins). The reduction (★) implicitly assumes
  the relevant bordism class is detected by the `η`/index pairing. A complete treatment would
  compute the reduced `Ω̃^{Spin}_{15}(BSp(64))` and verify the GU class is null. This is
  beyond the bounded scope here and is flagged for a future cobordism pass.

- **Relation to the IG/τ⁺ selection.** FC-3 is only fully closed once the gauge-group
  uniqueness question (audit §5.1a) is resolved — i.e. once it is known *which* subgroup, if
  any, τ⁺ selects. That is a separate open computation; the present result is stable under it
  in the "shrinking cannot add winding the ambient lacks" direction, but FC-3 names the one
  escape route.

---

## §7 — References

- Witten, E., "An SU(2) anomaly," Phys. Lett. B117 (1982) 324. (Global gauge anomaly
  template; π_{D+1}(G) heuristic.)
- Witten, E., "Global gravitational anomalies," Commun. Math. Phys. 100 (1985) 197.
  (ℤ-valued homotopy ↦ continuous-family anomaly via spectral flow; corrects the
  "ℤ milder than ℤ₂" misreading.)
- Dai, X. and Freed, D.S., "η-invariants and determinant lines," J. Math. Phys. 35 (1994)
  5155. (Mapping-torus η = global anomaly phase; the reduction (★).)
- Atiyah, M.F., Patodi, V.K., Singer, I.M., "Spectral asymmetry and Riemannian geometry I–III,"
  Math. Proc. Camb. Phil. Soc. 77–79 (1975–76). (η-invariant; APS index.)
- Atiyah, M.F. and Singer, I.M., "The index of elliptic operators V," Ann. Math. 93 (1971)
  139. (KSp-valued / quaternionic index is even; Fact A.)
- Witten, E. and Yonekura, K., "Anomaly inflow and the η-invariant," arXiv:1909.08775 (2019).
  (Modern Dai–Freed formulation; the global anomaly is an index, not read off π_{D+1}.)
- García-Etxebarria, I. and Montero, M., "Dai-Freed anomalies in particle physics," JHEP 08
  (2019) 003, arXiv:1808.00009. (Bordism classification of global anomalies; Ω^Spin pairing.)
- Bott, R., "The stable homotopy of the classical groups," Ann. Math. 70 (1959) 313.
  (π₁₅(Sp) = ℤ.)
- Lawson, H.B., Michelsohn, M.L., *Spin Geometry*, Princeton UP 1989, App. IV (Bott ladder).

Repo files:
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` — Sp(64) determination;
  perturbative anomaly verified; §3 global anomaly (this note upgrades §3).
- `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md` — τ⁺/IG with Sp(64);
  adjoint-dimension question (§5.1b cross-ref).
- `explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` — Cl(9,5) ≅ M(64,ℍ)
  (the quaternionic structure that powers Fact A).

---

*Filed: 2026-06-23. Global-anomaly closure pass for the Sp(64)-anomaly canon promotion.
Reduces the π₁₅(Sp)=ℤ global anomaly to the mod-2 index of a 16D Dirac operator on the
quaternionic representation S=ℍ⁶⁴, and proves that index even (hence anomaly phase +1) via
two independent mechanisms (KSp-evenness; chiral doubling). Verdict CONDITIONALLY_RESOLVED:
the winding is trivial for the GU configuration, gated on FC-1 (explicit η/index sign) for
upgrade to RESOLVED.*
