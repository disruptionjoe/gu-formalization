---
artifact_type: exploration
status: exploration
doc_type: internal-regrade-and-repair
created: 2026-08-15
work_item: VZ-4
channel: vz_repair
title: "VZ-4: the section pullback in vz-schur §18.3 is a CONTRACTION, and the 'not a larger sector' clause fails in EVERY gauge including the flat one. The identification R_s = ker Gamma^4D survives exactly and gauge-independently, but only as a statement about the horizontal subbundle pi^*(T*X^4) -- not as a property of s^*. Two independent defects, not one; the flat-section gauge repairs neither. §18.4's theorem is untouched."
grade: "EXACT only. Part A: sympy symbolic differentiation on a fully general g_ab(x) plus exact Rational sections, 6 sections x 14 basis covectors swept. Part B: exact Gaussian-integer 128x128 representation of Cl(9,5) built by Jordan-Wigner, all 91 anticommutators and 14 squares verified, held as int64 (re,im) pairs with an explicit magnitude guard proving no overflow. 25/25, exit 0. EIGHT planted controls, each drives exit 1, including a CONTRARY CONTROL (a non-flat section with a named nonzero residual 1/3) whose vacuity check plants a flat section and fires. No float is load-bearing anywhere. NOT: a re-derivation of §18.4(a)-(d), a dynamical claim, a decision of REDUCTION-FIDELITY, a canon edit, or any movement of the VZ verdict."
disposition: DEFECT_VERIFIED_INDEPENDENTLY__CONCLUSION_SURVIVES_ON_A_DIFFERENT_AND_GAUGE_FREE_GROUND__STATED_GROUND_AND_KK_COROLLARY_REFUTED__SECOND_DEFECT_FOUND_THAT_THE_FLAT_GAUGE_DOES_NOT_REPAIR
target_claim: OQ3-V3
target_claim_verdict: "INTERNAL-TARGET, SPLIT. V3a (the identification, domain-restricted to the horizontal subbundle) UPHELD and strengthened: exact, gauge-independent. V3b (the stated ground, 's* sends psi to its horizontal part') KILLED: holds iff d_mu g_ab = 0. V3c (the 'not a larger sector' / KK-scalar corollary) KILLED in every gauge, flat section included. This is a regrade of a repository claim. It is NOT evidence about Weinstein's source, which supplies the contraction reading (WG-B06) that this correction restores."
canon_verdict_change: none
canonical_effect: proposed_diff_pending_second_verification
steering_effect: unchanged
depends_on:
  - explorations/vz-evasion/vz-schur-complement-2026-06-23.md
  - canon/no-go-class-relative-map.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - lab/active-research/joe-directed/steward-2026-08-14-research-maintenance-pass.md
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md
fork_assumed:
  - CARRIER-SPLIT
  - SECTION-VS-OBSERVERSE
residual_declared:
  - id: REDUCTION-FIDELITY
    statement: "s*(R^{14D}) is the whole 4D one-form bundle, so a 4D RS configuration neither determines nor is determined by a 14D RS configuration. The identification of 'the 4D RS sector' with 'the observed image of the 14D RS sector' is unavailable in any gauge."
    status: open
    note: "NEW. §18.4 does not use that identification, so nothing moves. Named so no later argument can assume it."
scripts:
  - tests/channel-swings/joe_directed_vz4_pullback_contraction.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`

The object under repair is GU's own declared observation map — pullback along a
metric section, the author-stated Layer-0 correction `WG-B06` ("the relevant map
is a contraction, not a projection"). No conventional comparator is invoked, and
the correction moves the repository *toward* the source reading, not away from it.

---

# VZ-4 — the pullback is a contraction, and there are two defects, not one

## 0. Verdict in one page

`explorations/vz-evasion/vz-schur-complement-2026-06-23.md` §18.3 (`OQ3-V3`) runs
three propositions together under one grade of **VERIFIED / "No approximation is
made."** They have different truth values. That conflation is the defect.

| | proposition | verdict | condition |
|---|---|---|---|
| **V3a** | `s*( R^{14D} ∩ (π^*(T*X⁴) ⊗ S⁻) ) = ker Γ⁴ᴰ` | **UPHELD, exact** | **none — gauge-independent** |
| **V3b** | "the pullback functor `s*` sends `psi` to its horizontal part" | **KILLED** | holds iff `d_μ g_ab = 0` |
| **V3c** | "not a larger sector — no extra RS components from the normal directions survive as 4D spin-3/2 fields"; normal components "do not contribute to `R_s`" | **KILLED** | **in every gauge, flat section included** |

The headline conclusion `R_s = ker Γ⁴ᴰ` **survives**, and survives better than the
steward pass feared: it needs no gauge condition at all. What it needs is a
**domain restriction** — it is a statement about the horizontal subbundle
`π^*(T*X⁴)`, which is canonical, and not a statement about the map `s*`.

**V3c is a second, independent defect that nobody has named, and the flat-section
gauge does not repair it.** It has nothing to do with the missing `d_μ g_ab` term.

## 1. PREFLIGHT — retrieval before the work, and six problem-matched lenses

**Retrieval run before any computation.** Searched: `OQ3-V3` (found all dependents),
`flat-section gauge`, `d_mu g_ab`, `horizontal part`, `contraction, not a projection`,
`second fundamental form`, `H*/N*`, `KK scalar`, `WG-B06`; listed
`lab/active-research/joe-directed/vz-repair/` (empty — **no prior repair attempt exists**);
read `canon/no-go-class-relative-map.md:401`, the steward pass, `AR-1` item 7, `AR-2`,
`MD-1` §2/§5, and `LA-8` `[A1]`–`[A7c]`.

**What retrieval found that changes the framing.** `MD-1`'s identity `E2` is **not new
here and I do not claim it**: `LA-8` (2026-08-15) already re-derived it independently in
sympy as `[A2]`, with `[A6]`/`[A7c]` exactly reproducing the "equals the horizontal
projection iff `d_μ g = 0`" control. This pass is therefore the **third** independent
derivation of `E2`, not the first. Its novel content is **Part B — the Clifford/RS
consequence**, which `MD-1` explicitly declined ("the spinor sector has its own index
structure … MD-1 does not re-decide OQ3-V3") and `LA-8` never entered.

Retrieval also found that the repository has already repaired *one* KK-projection site
today — `GEOMETER-VS-PHYSICS-OBJECTS.md:25` (WITHDRAWN 2026-08-15) and the `[!CAUTION]`
in `lab/methods/source-native-comparator-routing.md` — but not this one. The §18.3 site
survived because it sits in the VZ chain, which the KK sweep did not enter.

**Lens 1 — differential geometer.** `s*` is the transpose of `ds`, so `ker s* = Ann(ds(TX⁴))`,
a *section-dependent* 10-plane. §18.3 identifies it with the *section-independent*
coordinate/frame normal span `N* = span{de^i}`. Predicted: they coincide iff `d_μ g_ab = 0`;
the horizontal subbundle `π^*(T*X⁴) = Ann(V)` is canonical and `s*|_{π^*T*X} = id` always.
**Confirmed** (A2–A5).

**Lens 2 — Clifford/spin geometer.** Transport the gamma trace and a defect operator must
appear: `Γ⁴ᴰ(s*ψ) = Γ¹⁴ᴰ(ψ) + Σ_i Δ_i ψ_i`, `Δ_i = (d_μ g_i)γ^μ_H − γ^i_N`. Since `γ^i_N ∉
span{γ^μ_H}`, `Δ_i` is **never zero** — including at `K = 0`, where it is exactly `−γ^i_N`.
Predicted: the "not larger" clause fails *in the flat gauge too*. **Confirmed** (B3–B5, B7).
This is the lens that goes past `MD-1` and the steward pass.

**Lens 3 — KK reductionist.** "Normal components become 4D scalars" presupposes a product
reduction with a Lorentz-inert internal space. `Y¹⁴ = Met(X⁴)` has fibre `Sym²(T*X⁴)`,
acted on by the same Lorentz group. Predicted: the KK-scalar corollary is the clause that
loses its ground twice over. **Confirmed**, and `MD-1` §2 already killed the inertness leg
independently.

**Lens 4 — grade auditor / verdict-inflation.** Predicted an internal contradiction: the
frontmatter says "OQ3-V1/V2/V3 verified only in constant-coefficient gauge" while §16,
§18.3 and §18.4 grade V3 exact, and canon says "gauge-independent". **Confirmed** (C3).
Also predicted §18.4's "the open upgrade condition is the OQ3-V1 check" was now an
incomplete enumeration. **This prediction was WRONG** — V3a is gauge-independent, so the
enumeration stands. Recorded because a lens that only ever confirms is not a lens.

**Lens 5 — blast-radius typer.** Sort every dependent by which proposition it consumes:
the *claim* (V3a) or the *stated ground* (V3b/V3c). Predicted most consume V3a and are
untouched. **Confirmed**: 2 of 7 consume V3a only; 4 consume V3c; 1 is grade-stale.

**Lens 6 — hyperbolic-PDE / symbol analyst.** The correction term is algebraic (zeroth
order in the symbol), so it cannot change the order or the principal symbol; the question
is whether §18.4's Schur split `E_s = R_s ⊕ Q_s` is intrinsic to 4D. Predicted yes.
**Confirmed** (C6: the theorem statement and proof summary name no normal or vertical
component).

## 2. Part A — the geometry, exactly, on a general section

`Y¹⁴ = Met(X⁴)`; adapted coordinates `(x^μ, u_I)`, `I = 1…10` indexing `Sym²(T*X⁴)`;
the observation section is `s(x) = (x, g_ab(x))` — the section *is* the metric.
`ds` is the 14×4 Jacobian `J`; `s* = Jᵀ`. With fully general `g_ab(x)` (sympy `Function`s):

```
ds(∂_μ) = ∂_μ + (∂_μ g_ab) ∂/∂g_ab                 rank 4          [A1]
(s*ω)_μ = ω_μ + ω_(ab) ∂_μ g_ab                                    [A2]
s* ∘ ι_H = id_{T*X⁴}          for EVERY section, no condition      [A3]
ker s* = span{ du_I − (∂_μ g_I) dx^μ }   ≠  span{du_I}  unless ∂g=0 [A4]
s* = P_H   ⟺   ∂_μ g_ab = 0                (both directions)       [A5]
```

`[A2]` reproduces `MD-1`'s `E2` / `LA-8`'s `[A2]` from scratch. `[A3]` and `[A4]` are the
load-bearing new pieces: `[A3]` is what rescues the conclusion, and `[A4]` names precisely
what §18.3 got wrong — it swapped the section-dependent kernel of `s*` for the
section-independent coordinate normals.

**The notational slip that seeds the error.** §18.3 writes `H*_x = s*(T*X^4)`. But `s*`
maps `T*Y¹⁴ → T*X⁴`; it cannot produce a subbundle *of* `T*Y¹⁴`. The correct object is
`π^*(T*X⁴)`. Once "horizontal" is written as `s*(…)`, the sentence "`s*` sends `psi` to its
horizontal part" reads as a tautology — which is, I think, exactly how a wrong statement
came to be graded VERIFIED by a competent author.

**CONTRARY CONTROL (required, and non-vacuous).** Section `g₀₀ = −1 + x⁰/3`, all other
components Minkowski; covector `ω = du_0` (pure normal, unit coefficient). Then
`P_H ω = 0` but `(s*ω)_0 = ∂_0 g₀₀ = **1/3**`, exact. The same covector on the flat section
gives exactly `0`. Planted control `contrary_control_vacuous` swaps a flat section into the
contrary slot and **fires** — the discriminator provably discriminates.

## 3. Part B — what it does to the RS sector (the part nobody computed)

Exact Gaussian-integer 128×128 representation of `Cl(9,5)`, Jordan–Wigner, all 91
anticommutators and 14 squares verified exactly (B1). Index split matches the repository
carrier split: horizontal `(3,1)`, normal `(6,4)`, total `(9,5)` (B2).

**The transport identity** (B3), exact, swept over six section-derivative matrices `K` and
many spinors:

```
Γ⁴ᴰ(s*ψ) = Γ¹⁴ᴰ(ψ) + Σ_i Δ_i ψ_i ,        Δ_i := (d_μ g_i) γ^μ_H − γ^i_N
Δ_i² = ( g^{μν} d_μ g_i d_ν g_i + η^{ii} ) · Id        (Clifford square, B5)
```

**`Δ_i` is never zero** (B4) — `γ^i_N` is linearly independent of `{γ^μ_H}`. At `K = 0` it
is exactly `−γ^i_N`, whose square is `η^{ii} = ±1`, so it is **invertible**.

**V3a survives, gauge-independently (B6).** For horizontal `ψ` (`ψ_i = 0`): `s*ψ = ψ_H`
exactly, and `Γ⁴ᴰ(s*ψ) = Γ¹⁴ᴰ(ψ)`. Both inclusions check for every `K`:
forward, a horizontal `ψ ∈ ker Γ¹⁴ᴰ` maps into `ker Γ⁴ᴰ`; reverse, every `χ ∈ ker Γ⁴ᴰ`
lifts horizontally into `ker Γ¹⁴ᴰ` and pulls back to itself.

**V3c fails in every gauge (B7, B8).** Take `ψ ∈ ker Γ¹⁴ᴰ` with one nonzero normal
component `ψ_i = v`. Then `Γ⁴ᴰ(s*ψ) = Δ_i v ≠ 0` — **including at `K = 0`.** And because
each `Δ_i` with `(d_μ g_i, −e_i)` non-null is invertible, `Γ⁴ᴰ ∘ s*` restricted to `R^{14D}`
is **onto**, so

```
s*(R^{14D}) = Ω¹(X⁴) ⊗ s*(S⁻)          — the WHOLE 4D one-form bundle
```

strictly larger than `R_s`. The clause "no extra RS components from the normal directions
survive as 4D spin-3/2 fields" is false, and its falsity is not a gauge artefact.

Conclusions are index-convention independent (B9: repeat under `Γ^A = η^{AB}Γ_B`).

## 4. Hostile review, inline

**"The doc already wrote `|_{horizontal 1-forms}` — you are attacking a qualifier it
supplied."** Partly fair, and I concede it: the *displayed conclusion* is defensible as
written and I have left it standing. But §18.3's own **Condition** line states the target
without any restriction — "Verify that the pulled-back RS sector `R_s = s*(R^{14D})`
coincides with `ker Gamma^{4D}`" — and two prose passages make unrestricted claims about
the map and the image. One correct qualifier surrounded by three incorrect sentences is a
defect, not a typo. The repair keeps the equation and fixes the prose.

**"`Δ_i ≠ 0` is trivial."** It is elementary. That is the point: a claim graded **VERIFIED**
with "no approximation is made" is refuted by linear independence of gamma matrices. The
triviality is evidence about the grade, not about the result.

**"You proved §18.4 survives with a *textual* test."** Correct, and I will not dress it up.
`C6` checks that §18.4's theorem statement and proof summary quantify only over `η ∈ T*X⁴`
and 4D blocks, naming no normal or vertical component. I did **not** re-derive (a)–(d).
The claim "§18.4 is untouched" is therefore **reconstruction grade, not verified**.

**"Maybe `R_s` should be the contraction image, and then §18.4 *is* damaged."** The
strongest attack, and it is why `REDUCTION-FIDELITY` is declared as an open residual rather
than waved away. §18.4 is well-posed either way — `R_s ⊂ E_s` is fixed by `ker Γ⁴ᴰ`, a 4D
object. What is *not* available, in any gauge, is the bridge "the 4D RS field is the
observation of the 14D RS field". §18.4 does not use that bridge. Anything later that does,
must close this first.

**"Your frame assignment is arbitrary."** `Δ_i ≠ 0` needs only 4 + 10 gammas, the Clifford
relations, and linear independence — all established by B1 for any adapted orthonormal
frame. The specific `(3,1)+(6,4)` split matches the repository's declared carrier split
(B2) but no conclusion depends on it.

## 5. Blast radius — exact, per dependent

7 sites: 1 canon + 6 explorations. **The steward pass said "five explorations"; there are
six** — `no-go-velo-zwanziger-canon-entry-2026-06-23.md` was missed. An 8th site,
`DERIVATION-PROGRESS.md:584`, carries the full V3b+V3c language but is frozen provenance
under its own 2026-08-03 terminal guard and is **not** edited.

| site | consumes | result | action |
|---|---|---|---|
| `canon/no-go-class-relative-map.md:401` | V3a **and** V3c | top-line "(exact, gauge-independent)" is **correct** for V3a; the elaboration "section pullback on H*/N* split is exact, normal RS components are KK scalars not spin-3/2 fields" **loses its ground** | **PROPOSED DIFF ONLY** (§6) |
| `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` §18.3/§16/§18.4/frontmatter | origin | grade split; V3b, V3c refuted | **REPAIRED** — `CORRECTION VZ4-01` appended, original text struck not deleted, grade + both summary rows + frontmatter corrected |
| `explorations/vz-evasion/no-go-velo-zwanziger-canon-entry-2026-06-23.md:171` | V3a + V3c | identification survives; KK clause refuted | **REPAIRED** |
| `explorations/analytic-index-fredholm/g2-kk-zero-mode-unitarity-2026-06-23.md:49` | V3a + V3c | `s*(Γ¹⁴ᴰ)|_{horizontal} = Γ⁴ᴰ` **survives** (it already carried the restriction); KK clause + "H*/N* splitting is exact" refuted; **not load-bearing** for G2's fibre-spectrum question | **REPAIRED** |
| `explorations/vz-evasion/vz1-oq3-gravitational-vz-weyl-tensor-2026-06-23.md:323, :350` | V3a (:323) + V3c (:350) | :323 untouched; :350 refuted but was a redundant restatement, not a premise — the Weyl/gravitational-VZ conclusion stands | **REPAIRED** |
| `explorations/vz-evasion/vz-f5-curvature-check-2026-06-23.md:296` | V3a, **grade-stale** | "This was VERIFIED (OQ3-V1, OQ3-V2, OQ3-V3)" was *already* wrong for V1 since the 2026-06-24 pass; the content is unchanged | **REPAIRED** (grade only) |
| `explorations/vz-evasion/vz-14d-mixed-covectors-2026-06-23.md:269` | V3a only | row is still true | **REPAIRED** (ground note only) |
| `explorations/time-as-finality-crosswalk/h3-gap2-gu-universality-2026-06-23.md:115` | V3a only | **UNTOUCHED — no repair needed.** Separately, it cites `OQ3-V3` for the horizontal Clifford identity, which is `OQ3-V1`'s content. Minor mis-citation, reported not fixed (out of scope) | none |

**Nothing in the VZ verdict moves.** 14D leg: `CONDITIONALLY_EVADED`, unaffected. 4D leg:
`CONDITIONALLY_RESOLVED`, unaffected — and its single open upgrade condition is still
OQ3-V1's curved-background frame-splitting check, because V3a is gauge-independent.

## 6. Proposed canon diff — NOT APPLIED

Repository rule: new findings do not promote themselves to canon, and canon changes require
independent verification. **This pass is the first verification, not the second.** The diff
below is proposed and awaits a second, independent check.

`canon/no-go-class-relative-map.md`, line 401. Replace:

```
OQ3-V3: `R_s = ker Gamma^{4D}` exactly -- section pullback on H*/N* split is
exact, normal RS components are KK scalars not spin-3/2 fields.
```

with:

```
OQ3-V3: `R_s = ker Gamma^{4D}` exactly, and this identification IS
gauge-independent -- but as a statement about the HORIZONTAL SUBBUNDLE
`pi^*(T*X^4)`, on which `s*` is a canonical isomorphism for every section, NOT
as a property of the pullback map. **CORRECTED 2026-08-15 (CORRECTION VZ4-01,
vz-schur §18.3):** the section pullback is a CONTRACTION, not an `H*/N*`
projection -- `(s*psi)_mu = psi_mu + psi_(ab) d_mu g_ab` -- so it equals the
horizontal projection only in the flat-section gauge `d_mu g_ab = 0`. And the
clause "normal RS components are KK scalars not spin-3/2 fields" is REFUTED in
EVERY gauge, flat section included: `Delta_i = (d_mu g_i) gamma^mu_H -
gamma^i_N` is never zero, so `s*(R^{14D})` is the whole 4D one-form bundle,
strictly larger than `R_s`. §18.4's theorem uses only the surviving
identification and is unaffected; the 4D leg's open upgrade condition is still
OQ3-V1's curved-background check. New open residual REDUCTION-FIDELITY: the 4D
RS sector is NOT the observed image of the 14D RS sector, in any gauge.
```

The preceding sentence — "At 4D: OQ3-V2 and OQ3-V3 are RESOLVED (exact, gauge-independent)"
— **needs no change**: for V3a it is correct, and this pass strengthens rather than weakens
it. That is worth stating explicitly, because the obvious repair would have been to strike
"gauge-independent", and that would have been wrong.

## 7. Certificate

`tests/channel-swings/joe_directed_vz4_pullback_contraction.py`

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_vz4_pullback_contraction.py
    → Ran 27 tests, OK, exit 0
_local/cas-venv/bin/python tests/channel-swings/joe_directed_vz4_pullback_contraction.py --selftest
    → SELFTEST PASSED — 10/10 planted controls each drove exit 1, exit 0
```

Repository gates re-run after the repair, all exit 0: `kill_target_claim_audit` (3 red =
scope baseline 3; this artifact is counted among the internal-target kills),
`certificate_shape_audit`, `retracted_claim_citation_audit`, `tests_manifest_count_audit`,
`correction_propagation_audit`, `source_native_comparator_routing_audit` (this artifact
registered in `lab/process/source-native-comparator-routing-registry.json` as
`SOURCE_NATIVE_ROUTE`; UNCLASSIFIED count held at its baseline of 9).
`hostile_review_lens_coverage_audit` fails on `LT-GR4` / `AC-F3` — **pre-existing**, dated
2026-08-05, untouched by this pass and confirmed against the files it names.

Planted controls, each of which must fire:

| control | plants |
|---|---|
| `pullback_is_projection` | `(s*ω)_μ = ω_μ` — **this is literally §18.3's claim** |
| `coordinate_normals_are_kernel` | `s*` annihilates the coordinate normals `du_I` |
| `horizontal_restriction_needs_gauge` | `s* ∘ ι_H ≠ id` on a non-flat section |
| `contrary_control_vacuous` | a **flat** section in the contrary-control slot |
| `clifford_square_sign` | flipped normal-direction sign in `Δ_i²` |
| `delta_vanishes_in_flat_gauge` | `Δ_i = 0` at `K = 0` |
| `flat_gauge_saves_not_larger` | `ker Γ¹⁴ᴰ` carried into `ker Γ⁴ᴰ` at `K = 0` |
| `quote_drift` | a sentence that is not in §18.3 |
| `canon_already_repaired` | canon carries the correction (it must not) |
| `repair_reverted` | a repaired dependent still carries its defective text |

Exactness: Part A is symbolic sympy plus exact `Rational`s; Part B is integer arithmetic
with an explicit `MAG_GUARD = 2⁴⁰` bound asserted on every product, so no overflow and no
float is load-bearing anywhere. Signature facts are asserted from the metric assignment,
never from eigenvalues.

## 8. Claim ceiling, and every imported assumption

**Ceiling.** Kinematic and algebraic. This artifact repairs a grade and its stated ground.
It computes no action, no propagator, no mass, no spectrum; it decides no fork; it moves no
canon entry, ledger row, or current-state surface. `canonical_effect` is
`proposed_diff_pending_second_verification`.

Imported, each load-bearing somewhere:

1. **`Y¹⁴ = Met(X⁴)` with fibre `Sym²(T*_x X⁴)`** — repository-derived, not re-derived here.
2. **`CARRIER-SPLIT` horn: `(3,1) + (6,4)`** — declared, `status: open`. Only B2 uses it, and
   no conclusion depends on it (see Hostile Review).
3. **The observation section is a metric section and the reduction map is `s*`** —
   source-confirmed; `SECTION-VS-OBSERVERSE` is `status: open`.
4. **§18.4's theorem (a)–(d) is correct as an argument about 4D blocks** — assumed, not
   re-derived. Only its *independence from V3b/V3c* is checked here, and that check is
   structural/textual, hence reconstruction grade.
5. **`Cl(9,5)` acts on the RS carrier in the standard way** — the 128-dim complex module is
   the irreducible `Cl(14,ℂ)` module; the repository's `S = ℍ^64` is the real form.
   Kernel-non-preservation is a statement about the Clifford algebra and survives either.

## 9. POSTFLIGHT — five lenses, after the work

**P1 — verdict-inflation auditor.** Did I inflate? The one place I could have is
"§18.4 is untouched", which I have explicitly demoted to reconstruction grade. And I record
that Lens 4's prediction (incomplete upgrade enumeration) was **falsified** by the work.

**P2 — the opposite failure, under-repair.** Did I leave a live defect standing? Yes, two,
both named and neither mine to fix: `DERIVATION-PROGRESS.md:584` (frozen provenance, carries
the full defective language) and the `h3-gap2` mis-citation of V3 for V1's content. Both
reported.

**P3 — over-repair auditor.** Did I edit a site that did not need it? `h3-gap2` uses only
V3a and was deliberately left alone; `C5b` asserts it stays unedited, so over-repair is now
a test failure, not a judgement call.

**P4 — canon-boundary auditor.** No file under `canon/` was written. `C4` asserts the canon
site still carries its original wording and that `CORRECTION VZ4-01` is **absent** from it;
control `canon_already_repaired` proves that check can fire. No file under the six
concurrently-owned directories was touched (`C8`).

**P5 — reader-of-the-future.** The single sentence a later reader most needs: **the pullback
is not a projection, and restricting to the horizontal subbundle — not fixing a gauge — is
what makes `R_s = ker Γ⁴ᴰ` true.** Anyone who "repairs" this by adding the condition
`d_μ g_ab = 0` will have made the claim weaker than it is and will still not have fixed V3c.

## 10. Did I over- or under-state the damage? — blunt

**I under-stated it relative to nothing and over-stated it relative to nothing; but the
*shape* of the damage is not what the routing said, and that matters more than the size.**

The steward pass and `AR-1` both framed VZ-4 as "holds only in the flat-section gauge."
That framing is **half right and half wrong**, in a way that would have produced a bad
repair. It is right that V3b needs `d_μ g_ab = 0`. It is wrong that the flat gauge is the
condition under which §18.3 works, because (i) the surviving conclusion V3a needs **no**
gauge condition — the honest repair *removes* a condition rather than adding one, and (ii)
the KK-scalar clause V3c is false **in the flat gauge too**. An agent who had taken the
routing at face value would have written "VERIFIED in constant-coefficient gauge", which
would have been simultaneously too weak (V3a is unconditional) and too strong (V3c is false
there). I nearly did exactly that: my own Lens 4 predicted the upgrade enumeration was now
incomplete, and it was not.

On magnitude: I do **not** think the VZ chain is damaged, and I have resisted the pull to
say so, because a two-day-old "highest severity" finding creates an expectation that
something big falls. Nothing falls. Six of seven dependent sites keep their results; the
one canon sentence keeps its top-line grade; §18.4's theorem is untouched. What actually
changes is a **grade**, a **stated ground**, and a **corollary that should never have been
written** — plus one genuinely new open residual (`REDUCTION-FIDELITY`) that is small today
and would be load-bearing the moment anyone argues from "the 4D RS field is the observation
of the 14D RS field."

Where I am most likely to be wrong: the claim that §18.4 needs only V3a. I checked it
structurally, not by re-deriving (a)–(d). If a later pass finds that the Schur split
`E_s = R_s ⊕ Q_s` is imported from a 14D splitting rather than constructed in 4D, then V3c's
failure reaches the theorem and my blast radius is too small by exactly one entry. That is
the check I would run next, and it is the only one I would call urgent.
