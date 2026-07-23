---
title: "HQW-LEAD credibility pass: premise-flag map + per-claim GU-dependency table"
status: review-support
doc_type: review
paper: "located-not-forced-generation-count-2026-06-29"
team: "QW-LEADPAPER (HQW-LEAD)"
date: "2026-07-14"
grade: "review-support (no science change; credibility/honesty audit + referee-facing dependency table)"
method: "five personas inline (author-editor, hostile referee, rep-theory checker, reproducibility engineer, honesty auditor), then synthesis"
---

# HQW-LEAD credibility pass (2026-07-14)

Two register quick wins for the repo's strongest paper (`located-not-forced`, arXiv-ready,
GU-independent theorem core):

- **H04** -- premise-flag map: confirm every "located"/count locus carries the load-bearing premise flag
  (the torsion-count premise / `Hom(Z/3,Z)=0` / external-datum caveat), so no sentence overstates.
- **H05** -- per-claim GU-dependency table: mark each substantive claim
  FULLY-GU-INDEPENDENT / CONDITIONAL-ON-GU / GU-MOTIVATION-ONLY, making the RESEARCH-POSTURE credibility
  case ("the paper survives GU falling away") explicit for a referee.

Binding: honest grading; no science/canon change; no external action; no promotion (arXiv submission
is Joe-gated). Line numbers reference the `.tex` submission source as of this pass.

Reproducibility anchors run this pass (reproducibility-engineer persona, real exit status):
`reproduce_all.py` -> **31/31 load-bearing checks, exit 0** (150.8s);
`tests/W177_connection_curvature_c2.py` -> **17/17, exit 0** (the GU-native-curvature reinforcement).

---

## H04 -- Premise-flag map

"Premise flag" = the sentence carries at least one of: (a) the torsion-count premise ("located, not forced"
holds only under the torsion-theoretic reading; a literal integer-index reading would *forbid* an odd count);
(b) the algebraic sharpening `Hom(Z/3,Z)=0` (a torsion class cannot *be* an integer count); (c) the
external-datum / open-residual caveat ("external by structure, modulo the function-space APS/end + family-index
residual"); or (d) an explicit grade tag (reconstruction-grade / open / exploration-grade). A locus is **Y**
if the load-bearing statement it makes is not stronger than what the flag licenses.

| # | Locus (line) | What it states | Flag present? | Which flag | Fix |
|---|---|---|---|---|---|
| L1 | Title (60-62) | "Two-Primary Obstructions **Cannot Force** the count" | Y | The title *is* the located-not-forced claim; "cannot force" does not overstate | none |
| L2 | Boxed disclaimer (75-91) | Five load-bearing caveats stated up front | Y | (a)+(b)+(c)+(d), maximal | none |
| L3 | Abstract "locates the order-3 slot without filling" (113-115) | order-3 carrier locates | Y | (a)+(b): "interpretive gloss under the torsion-count premise"; "by Hom(Z/3,Z)=0 the located class cannot itself be a count" | none |
| L4 | Abstract "external by structure" (126-128) | count external | Y | (c): "modulo the open function-space APS/end residual" | none |
| L5 | Abstract "located, not forced ... contingent" (134-139) | verdict statement | Y | (a)+(b): "contingent on treating the obstruction data torsion-theoretically"; "made algebraically explicit by Hom(Z/3,Z)=0" | none |
| L6 | Intro item 2, CRT reading (172-178) | 2-primary no-go cannot force odd count | Y | (a): "under the torsion-count reading; see Corollary cor:arenas" | none |
| L7 | Intro item 3 "On present evidence ... external" (179-190) | count external | Y | (c)+(d): "linear leg theorem-grade, antilinear leg closed over the null-eigenspace class (function-space extension open)" | none |
| L8 | Intro item 4, located carrier (191-194) | Λ²₊ framing locates | Y | (a): "'locates' is an interpretive gloss under the torsion-count reading, not an additional computed quantity" | none |
| L9 | Multiplicity section, "located, not forced" rep form (280-281) | native three is a multiplicity, not a chiral count | Y | self-flagging: "locates a genuine three (as a multiplicity) and does not force a three (as a chirality)" | none |
| L10 | Corollary cor:arenas + follow (348-360) | question is arithmetically ill-posed | Y | (a): "Under the torsion-count reading"; explicit integer-index counter-reading | none |
| L11 | Thm 2 §, "external by structure" (522-535) | no interior operator forces odd count | Y | (c): "(Modulo the function-space APS/end + family-index residual)" | none |
| L12 | Carrier §, "locates but does not fill" (575-586) | carrier locates | Y | (a)+(b): "interpretive gloss under the torsion-count premise"; "by Hom(Z/3,Z)=0 the located class cannot itself be an integer count" | none |
| L13 | Decider §, carrier-mass "located-vs-forced reduces to one term" (636-646) | both mass branches give net chiral 0 | Y | bounded computed statement; count-forcing needs the unbuilt selector | none |
| L14 | Decider §, "Located, not forced holds under both readings" (628-634) | robustness across order-3 and 2+1 readings | Y | states both readings; "2+1 is numerology across disjoint frameworks" | none |
| L15 | Open-conjecture § (672-710) | order-3 class -> integer 3 is the single open bridge | Y | (b) maximal: Hom(Z/3,Z)=0, Hom(Z/24,Z)=0, Hom(Z/2,Z)=0; "candidate category error"; gated on unbuilt Y14 index | none |
| L16 | Status-of-claims table (758-784) | per-claim grades | Y | (d): every row carries an explicit grade; external-by-structure row carries residual | none |
| L17 | Conclusion (786-817) | located, does not fill; external | Y | (a)+(b)+(c): "interpretive summary under the torsion-count premise; Hom(Z/3,Z)=0 blocks any literal class-to-count identification"; "modulo the open ... residual" | none |

**H04 result: 17/17 loci carry the premise flag. No overstating sentence was found; zero caveat clauses had
to be added.** The paper has already been through multiple adversarial credibility passes (v2.5.1, the
hostile-referee pass noted in the Acknowledgments), and the flagging is exhaustive: the torsion-count premise,
the `Hom(Z/3,Z)=0` sharpening, and the external/open-residual caveat are attached at every count/located
locus, including the title framing, the abstract, each contribution item, both theorem sections, the carrier
section, the decider, the open-conjecture section, the status table, and the conclusion.

**Rep-theory checker (persona 3) sign-off on the premise itself.** The load-bearing conditional is correctly
stated. `Hom(Z/3,Z)=0` is correct (no nonzero homomorphism from a torsion group to a torsion-free one), and
its use is correct: it blocks identifying the *absolute* torsion class with an integer count, while leaving a
*relative/equivariant/rank* invariant (integer-by-construction, geometry-dependent) as the only well-typed
home -- exactly the unbuilt twisted RS index. The CRT split `Z/24 = Z/8 ⊕ Z/3` with the one-sided homs
vanishing is standard and correctly deployed. The escalation `Hom(Z/24,Z)=0`, `Hom(Z/2,Z)=0` in the
open-conjecture section is also correct. The premise is a genuine premise (not a smuggled result): the paper
states, correctly, that under a literal integer-index reading the same obstructions would *forbid* an odd
count outright (net index 0 forces count 0), so "located, not forced" is contingent, not derived.

**Hostile referee (persona 2) residual concern (logged, not a defect).** The strongest referee pushback is
not that a sentence overstates -- none does -- but that the whole "located, not forced" verdict *depends on
choosing* the torsion-count reading over the integer-index reading, and the paper does not *derive* that
choice. The paper handles this honestly: it flags the choice as a load-bearing premise (Corollary
`cor:arenas`), states the competing integer-index reading explicitly, and files the class-to-count bridge as
the single named open conjecture. This is the correct honest posture for a draft requesting external review;
no edit is warranted.

**One reinforcement applied (not a fix to an overstatement).** The external-datum framing (loci L4, L7, L11,
L17) is *reinforced* by a 2026-07-14 exploration result and now cited as an exploration-grade remark after the
"external by structure" paragraph (`.tex` Section `sec:thm2`): GU's own metric-compatible connection curvature
`F_A` on `Y^{14}=Met(X^4)` is `so(9,5)`-valued, hence leakage-free on `ker Γ`, hence provably cannot move the
sector-interior chiral datum from inside -- so a GU-native geometric background of this kind cannot force an
odd count, and the forcing datum must be external and non-metric. This strengthens rather than changes the
verdict; it is marked exploration-grade with the real test exit status (`tests/W177_connection_curvature_c2.py`,
17/17, exit 0; record `explorations/W177-build-connection-curvature-c2-2026-07-14.md`) and carries no
verdict/grade/claim change.

---

## H05 -- Per-claim GU-dependency table

Category key:
- **FULLY-GU-INDEPENDENT (FGI)** -- holds as mathematics (rep theory / index / Krein / homotopy / bordism)
  whether or not GU is correct; survives GU falling away.
- **CONDITIONAL-ON-GU (CoG)** -- the *content* depends on a GU-specific object (reconstruction-grade or gated
  on GU's unbuilt data). These are exactly the paper's already-marked reconstruction-grade / open items.
- **GU-MOTIVATION-ONLY (GMO)** -- GU supplies provenance / choice of setting only; the mathematical content
  is standard and would stand under any equivalent setting.

| # | Substantive claim | Category | Why | Machine check (persona 4) |
|---|---|---|---|---|
| C1 | Two-primary meta-theorem (Thm 1): no enumerated obstruction is an odd-prime congruence; class-C completeness | **FGI** | Arithmetic of the Clifford--RS sector's own invariants; no GU input | `reproduce_all.py` 31/31 exit 0; `tests/generation-sector/` |
| C2 | Table-free parity backstop: every covariant interior count is even (centrality + Schur + even-dim irreps) | **FGI** | Pure rep theory of the carrier | `R1_kill_odd_index_isotypic.py`, exit 0 (per status table) |
| C3 | CRT two-arena structure `π₃ˢ=Z/24=Z/8⊕Z/3`, summands disjoint; the inverse "no-go lives in Z/8" reading | **FGI** | Standard primary decomposition + Adams image-of-J; the *reading* is the contribution, still GU-free | `canon/two-arena-rep-theory-core-RESULTS.md` (Lean-backed) |
| C4 | `Hom(Z/3,Z)=0` sharpening (class-to-count is ill-typed) | **FGI** | Pure algebra | analytic; standard |
| C5 | Index-conservation theorem (Thm 2): linear Krein-isometric operators conserve net chiral index 0 on the (96,96) cross-chirality carrier | **FGI** | Finite-dim linear algebra (definite subspace transverse to complementary Lagrangians); holds for any (96,96) cross-chirality carrier. The specific carrier is GU-motivated, the theorem is not | `net_chiral_index_invariant.py`; `canon/core-theorems-symbolic-proof-RESULTS.md` (sympy) |
| C6 | Necessary antilinear escape (Wigner dichotomy; class-CII type) | **FGI** | Wigner's theorem | `ghost_parity_krein.py`; corollary + machine-verified |
| C7 | Antilinear index-nullity theorem over the null-eigenspace class (strictly larger than Krein-compatible) | **FGI** | Krein-space linear algebra; a K-null re-graded chirality pair keeps index 0 | `tests/antilinear-bound/`; `canon/antilinear-bound-RESULTS.md`, `canon/antilinear-nonkrein-admissibility-RESULTS.md` (incl. Cl(7,7)) |
| C8 | Function-space extension: net chiral spectral flow 0 for Krein-self-adjoint chirality-odd Fredholm families | **FGI (conditional on an *analytic* residual, not on GU)** | Fredholm/Krein; the open APS/end + family-index residual is analytic, not GU-dependent | `canon/function-space-index-conservation-RESULTS.md`, `...-residual-closure-RESULTS.md` |
| C9 | Class-level structural no-go: no interior operator forces an odd count -> count external by structure | **FGI** | Explicitly reopened GU-independently; the paper's strongest GU-free statement | `tests/gu-independent/`; `canon/external-by-structure-synthesis-RESULTS.md` |
| C10 | External chiral background produces chirality: net chiral index = flux number (2D Wilson--Dirac) | **FGI** | Atiyah--Singer / Aharonov--Casher; standard | `canon/external-topological-index-flux-RESULTS.md` |
| C11a | e-invariant facts: tangential Λ²₊ framing carries `e_R = 1/12`, order 3 | **FGI** | Adams e-invariant + Kirby--Melvin framing degree; homotopy facts | standard (Adams, Kirby--Melvin); controls in `tests/boundary-eta/` |
| C11b | Identification of *GU's* Λ²₊ twist with that natural tangential framing | **CoG** | reconstruction-grade GU identification (explicitly marked in the paper) | n/a (reconstruction) |
| C12 | Carrier is vectorlike and homotopy-fixed (locates, does not fill) | **FGI** | Computed facts about the carrier (tangentiality, net chiral 0, homotopy-fixedness); "locates" is interpretive under the premise | `tests/generation-sector/` |
| C13 | Spinor 2-smoothness (Lemma 1) + "three is the canonical odd multiplicity" | **FGI** | Rep theory of SO(m) spinors + Spin(10) commutant enumeration inside Spin(14) | `leg3_family_embedding_enumeration.py` |
| C14 | Native multiplicity three exists (192-dim j=1 triplet; Spin(10) Casimir = 16) | **FGI (GU-motivated framing)** | Rep theory of the Cl(p,q) sector; holds for any oriented 4-base's self-dual geometry; the p+q=14 / 16-of-Spin(10) setting is GU-motivated | `h1_selfdual_family_kill.py` |
| C15 | `Hom_{Spin(9,5)}(S⁺⊗S⁺,Λ⁰)=0` (no invariant same-chirality Majorana scalar mass) | **FGI** | Explicit Cl(9,5) rep theory | `tests/chase/MOVE-4/move4_spinor_square_forms.py` + `verify/indep_check.py`; `canon/two-arena-rep-theory-core-RESULTS.md` fact (A), exit 0 |
| C16 | GU-native metric curvature cannot force the count (reinforcement remark) | **FGI about GU's object** | `F_A` is `so(9,5)`-valued hence leakage-free; a theorem-grade closure result, exploration-grade as folded here | `tests/W177_connection_curvature_c2.py`, 17/17, exit 0 |
| C17 | Global anomaly layer: SM boundary data does not pin the count in the mod-3 arena (`Ω^Spin_5(BG_SM)⊗Z_(3)=0`) | **FGI** | Spin-bordism / Anderson--Brown--Peterson; color triality | exploration-grade (R2 per status table) |
| C18 | The literal net-chiral generation integer on GU's *actual* 14-manifold | **CoG (open / gated)** | Gated on GU's unbuilt stabilized twisted RS source action; the one genuinely GU-dependent open item | ten Atiyah--Singer routes computed, none = 16; `tests/decider/` |
| C19 | "Only unconditionally computable generation integer in this program is 1" (Pati--Salam Spin(7,7) chain) | rep-theory core **FGI**; chain selection **GMO** | The 16-of-Spin(10) -> one anomaly-free SM generation is standard GUT rep theory; the choice of GU's Spin(7,7) chain is chain-relative (GU-motivated) | `pati_salam_chain_verification.py` + `verify_clifford_explicit.py`; App A; in `reproduce_all.py` |
| C20 | The sector identification itself (Y14=Met(X4), vector-spinor, 4+10 split, 16 of Spin(10)) | **GMO** | GU provenance / setting; reconstruction-grade | n/a (setup) |
| C21 | `order-3 class -> integer 3` bridge | **not claimed / open**; statement-that-it-is-ill-typed is **FGI**; a resolution would be **CoG** | Ill-typed by `Hom(Z/3,Z)=0` (FGI); resolving it needs GU's Y14 relative index (CoG) | analytic; `tests/decider/`, open |

### Counts per category

- **FULLY-GU-INDEPENDENT: 15** substantive claims (C1--C10, C12, C13, C15, C16, C17), plus the GU-independent
  *cores* of C14 (native multiplicity), C19 (16 -> one SM generation), and C21 (ill-typedness of the bridge).
- **CONDITIONAL-ON-GU: 2** (C11b the Λ²₊-twist identification, reconstruction-grade; C18 the literal integer,
  open/gated on GU's unbuilt source action), plus the resolution half of C21.
- **GU-MOTIVATION-ONLY: 2** (C20 the sector provenance; C19's chain selection).

**H05 result: the entire theorem-grade and computed-grade core is FULLY-GU-INDEPENDENT.** The only
GU-dependent items are (i) the sector *provenance* (GMO, C20/C19-chain), and (ii) two items the paper already
marks reconstruction-grade or open (CoG, C11b/C18). Nothing that the paper asserts as *established* is
conditional on GU being correct. This makes the RESEARCH-POSTURE credibility case explicit for a referee: the
paper survives GU falling away, because the surviving content is rep-theoretic, index-theoretic,
Krein-space-kinematic, and homotopy/bordism-theoretic, and the GU-specific steps are confined to provenance
and to the explicitly-flagged open bridge.

---

## Honesty auditor (persona 5) sign-off

- The premise flag is present at all 17 count/located loci; no clause was added because none was missing, and
  none was removed. No overstatement was manufactured or masked.
- The single `.tex` edit is a *reinforcement* (GU-native curvature cannot force the count), marked
  exploration-grade with a real exit status, changing no verdict/grade/claim. It does not upgrade any result.
- The GU-dependency categories are conservative: where a claim's core is GU-independent but its *setting* is
  GU-motivated (C14, C19), the split is stated rather than rounded up to FGI.
- The two CoG items (C11b, C18) match exactly the paper's own reconstruction-grade / open markings; the
  dependency table introduces no new dependency and hides none.
- No canon change, no science change, no external action, no promotion. Zero em dashes.
