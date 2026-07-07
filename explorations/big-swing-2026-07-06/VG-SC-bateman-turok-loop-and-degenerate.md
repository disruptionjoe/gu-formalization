---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing VG-SC (rung 0 source intake, supports T9'/V4): Bateman-Turok fine print from the primary texts -- (i) LOOPS: unitarity/optical theorem is claimed TO ALL ORDERS from the Krein spectral property, but POSITIVITY is proved at tree level only; the stated obstacle is collinear IR divergences affecting asymptotic states ('need to be carefully regulated and resummed' = conjecture), while IR-finiteness of loop integrals is delegated to a TO-APPEAR companion [25]; (ii) NO rule for odd-ghost-parity states on internal lines exists anywhere in the paper -- the positivity rule (weak ghost symmetry, null parts dropped from traces) lives at the level of asymptotic projections/observables, so the T9' leak question is genuinely open in the primary source; (iii) BT's PS theory (box^2 phi, double-pole propagator) sits AT the degenerate point where Bender-Mannheim's 0706.0207 similarity transform is singular (sinh formula undefined at omega_1 = omega_2) -- and BM's own companion 0804.4190 says so explicitly (transform 'becomes singular', H_PU 'becomes a Jordan-block operator... no Hermitian counterpart') YET claims unitary evolution survives via nonstationary states, so the two rescues' validity regimes are DISJOINT on current primary texts (BM-0706 needs unequal frequencies; BT's QFT is the equal-frequency case); (iv) conformally-flat remark rests on to-appear ref [27] and in that limit the graviton AND its spin-2 ghost decouple -- the tree positivity theorem covers only the conformal factor; (v) fourth seat: BT say only 'we have also studied gauged versions: the results will be presented elsewhere'; BM say nothing about matter. CITATION-GRAPH CORRECTION: arXiv:0706.0207 was published as Phys. Rev. Lett. 100, 110402 (2008), NOT Phys. Rev. D 78, 025022 (2008); the PRD reference belongs to the equal-frequency companion arXiv:0804.4190; BT's own reference [7] carries this conflation and the repo cross-exam doc inherited it."
grade: "rung-0 SOURCE INTAKE (no computation; no script -- nothing numerical to print). Intake verdicts: T9' loop gate remains OPEN in the primary source = CONSISTENT_UNCOMPUTED for the leg (kill condition 7 neither fired nor defused by BT); degenerate-limit fine print CHECKED against three primary texts; one citation correction issued with provenance. Quote confidence protocol: CHECKED = verbatim text reproduced identically across >= 2 independent fetches of the source; SINGLE-FETCH = extracted once (fetches run through a summarizing model; single-fetch quotes carry residual transcription risk); UNVERIFIED = could not be established from the fetched text. Target-import guard: no counts touched; this route asserts no number."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - explorations/big-swing-2026-07-06/CROSS-EXAM-weinstein-turok-mannheim-first-principles.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
scripts: []
sources:
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096v1 (submitted 30 Jun 2026, 6 pages) -- HTML full text, 4 independent fetches"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator model, arXiv:0706.0207, Phys. Rev. Lett. 100, 110402 (2008) -- ar5iv HTML, 2 independent fetches"
  - "Bender & Mannheim, Exactly solvable PT-symmetric Hamiltonian having no Hermitian counterpart, arXiv:0804.4190, Phys. Rev. D 78, 025022 (2008) -- abstract only (fetched to resolve the citation conflict; full text not needed for this route)"
---

# VG-SC: Bateman-Turok fine print — loops, the odd-state rule, the degenerate limit, and the fourth seat

**Route:** SOURCE ROUTE SC, rung 0 of the adjudication ladder (Section 6.3 of the persona doc). Primary-source
intake on arXiv:2607.00096 (Bateman-Turok) and arXiv:0706.0207 (Bender-Mannheim), extracting exactly the five
items the federation's T9' loop gate and V4/fourth-seat questions depend on. No computation; no outcome of the
parallel swing workflow (R1–R4) is cited — where a finding bears on a gate, the gate is stated as a conditional.

**Method and confidence marks.** arXiv HTML full text of 2607.00096v1 was fetched four times with independent
extraction prompts; ar5iv HTML of 0706.0207 twice; 0804.4190's abstract page once (plus one metadata fetch).
All fetches pass through a summarizing model, so every quote below carries a mark:

- **CHECKED** — verbatim text reproduced identically in ≥ 2 independent fetches, or read directly off the arXiv
  abstract page (stable metadata).
- **SINGLE-FETCH** — extracted once; content consistent with everything else but with residual transcription risk.
- **UNVERIFIED** — could not be established from the fetched text; listed explicitly in Section 7.

---

## 1. What BT say about LOOPS (the stated obstacle; proved vs conjectured)

### 1.1 The claim structure, disaggregated

The single most load-bearing piece of fine print: **BT's "to all orders" claim and their "tree level" claim are
about two different properties.** The abstract (CHECKED, verbatim):

> "We present a counterexample to Ostrogradsky's famous 'no go' theorem as usually interpreted in quantum field
> theory (QFT), namely a four-derivative, UV-complete QFT with a consistent perturbative expansion which describes
> high energy scattering processes. We carefully quantize the theory on an indefinite space of states – a Krein
> space – using covariant methods which ensure perturbative causality and unitarity (in the form of the optical
> theorem) to all orders. We generalize the Born rule to Krein spaces and prove that all tree level transition
> probabilities are positive in spite of the presence of ghosts. A key role in the proof is played by a hidden
> 'ghost parity' symmetry which becomes explicit when the theory is embedded in a two-derivative, two-field
> O(1,1)-symmetric perturbative field theory."

So:

| property | order | status in the paper |
|---|---|---|
| causality + (pseudo-)unitarity / optical theorem | **all orders** | claimed, from the spectral property + Hermitian interaction |
| positivity of transition probabilities | **tree level only** | proved (the paper's theorem) |
| loop-integral IR finiteness | loop level | claimed proven — but in a **to-appear companion** [25] |
| collinear IR divergences of **asymptotic states** | loop level | **open**; "need to be carefully regulated and resummed" (conjecture) |
| loop-level positivity | loop level | **not claimed anywhere** |

Supporting quotes. Section I (SINGLE-FETCH): "Provided the interaction Lagrangian is Hermitian, the spectral
property is sufficient to ensure perturbative causality and unitarity in the form of the optical theorem [18]
(see also [19])." — where [18] is 't Hooft–Veltman, *Diagrammar* (1973) (CHECKED bibliography entry). Section II
(SINGLE-FETCH): "Mathematically, theories based on a Krein space are pseudo-unitary, not unitary." and "Given the
spectral condition, the S-matrix is (pseudo)-unitary, S†S = 1, if the interaction Lagrangian is (pseudo)-Hermitian."

### 1.2 The stated obstacle, in their own words

Section VI, Conclusions (CHECKED — reproduced identically in two fetches, then again inside the full-section quote):

> "The main obstacle to extending the proof to higher orders is that, like QCD, the massless theory has collinear
> infrared divergences which affect asymptotic states. These need to be carefully regulated and resummed."

And Section I (CHECKED — reproduced identically in two fetches):

> "With Anderson and Herzog, we have proven that PS theory is free of IR loop divergences [25]."

Reference [25] (CHECKED bibliography entry): "M. Anderson, S. Bateman, F. Herzog, and N. Turok, Renormalization of
a Four-Derivative Theory (2026a), **to appear**." So the loop-integral IR-finiteness claim is a citation to an
unpublished companion — announced, not available for audit. Provenance status for the federation: the only
loop-level statement in the published record is a promissory note.

("PS" = "perfect square" theory, from the Lagrangian S_φ = −(1/2)∫d⁴x(□φ + λ(∂φ)²)², eq. (2); definition sentence
"Due to the form of its Lagrangian, we call it the perfect square (PS) theory." — SINGLE-FETCH.)

### 1.3 Verdict for the doc's question 1

- **Stated obstacle:** collinear IR divergences affecting asymptotic states (QCD-like), not ghost-loop rules.
  BT frame the loop frontier as an IR/resummation problem, not a ghost-consistency problem.
- **Proved (in-paper):** tree-level positivity; pseudo-unitarity + optical theorem from the spectral condition.
- **Proved (claimed, to-appear):** IR finiteness of loop integrals [25].
- **Conjectured:** that the collinear divergences "can be consistently resummed" (SINGLE-FETCH paraphrase of
  Section I conditional language) and, more broadly (Section VI, CHECKED full-section quote), that "the coupling λ
  becomes strong at large distances, we expect PS theory to generate a mass gap as well as a vev ⟨(∂φ)²⟩ which will
  break scale symmetry dynamically."
- **Never claimed:** positivity beyond tree level.

## 2. Odd-ghost-parity states on internal lines (the T9' leak question)

**No rule exists in the paper.** Across four fetches, no sentence defines what odd-ghost-parity or negative/null
states do on internal propagator lines. What the paper does define (all Section II unless noted):

- The generalized Born rule (SINGLE-FETCH): "When working in an indefinite space of states, including null states,
  meaning ⟨Ψ|Ψ⟩ = 0, conventional Born rule no longer makes sense." An operator A is *weakly ghost symmetric* if
  "A = B + C with B ghost symmetric and C null and orthogonal to B, meaning tr(C†C) = 0 = tr(B†C)"; then
  "If all physical processes A are weakly ghost symmetric, Prob(A) = tr(B†κBκ) ≥ 0, a sufficient condition for an
  indefinite QFT to admit a probabilistic interpretation."
- Section V (SINGLE-FETCH): "a general covariant projection operator in the φ theory maps to a weakly ghost
  symmetric projection in the O(1,1) model." and "the negatively charged operators in Q cannot contribute to the
  trace, that is, Q is null and orthogonal to P."

All of this is a rule about **observables and asymptotic projections** — which questions may be asked of the
S-matrix — not about internal lines. The odd/null sector is *quotiented out of the answers*, not banned from the
propagator. Combined with Section 1: internal-line consistency at loop level is exactly the part delegated to the
to-appear ref [25] plus the unproved resummation step.

**Consequence for T9' and kill condition 7** (stated as a gate, no outcome asserted): the primary source neither
defines the odd-state loop rule whose absence would fire kill condition 7 ("no odd-state loop rule exists that
passes a one-loop optical-theorem check") nor proves one exists. The leak question is genuinely open *in the
literature*, not just in our reconstruction. One sharpening the intake buys: since BT claim the optical theorem to
all orders from the spectral property alone, any leak must live in **positivity/probability** (the Born-rule layer),
not in pseudo-unitarity — the T9' check should target tr-positivity of loop-level processes, not S‡S = 1.

Also relevant (Section III, SINGLE-FETCH): "Note that our construction does not put the amplitude ℳ on-shell, but
rather the squared amplitude |ℳ|² which is differentiated before being put on-shell. This seems an important
novelty of higher derivative QFTs: that only on-shell probabilities, not amplitudes, are physically meaningful."
Any T9' loop check must therefore be phrased at the |ℳ|² level to be commensurable with BT's own construction.

## 3. The degenerate / equal-frequency limit, and the exact scope of the conformally-flat remark

### 3.1 BT sit AT the degenerate point

BT never discuss an "equal-frequency limit" — because their model has no unequal-frequency deformation on the
table. The free theory is massless □²φ. Section I (SINGLE-FETCH):

> "Consider a massless, free four-derivative scalar φ, whose field equation is □²φ = 0. Classically, its
> propagation is perfectly causal. Quantum mechanically, its Feynman propagator is −i/(p² + iϵ)², with double poles
> at p⁰ = ±(|𝐩| − iϵ)."

Double poles = the dipole/degenerate case — per-mode, the ω₁ = ω₂ Pais-Uhlenbeck point (this identification is
standard from-memory physics, flagged as such; the double-pole quote itself is from the source). No fetch found
any BT discussion of Jordan blocks or non-diagonalizability (SINGLE-FETCH negative). Growing modes are said to
"cancel out of scattering cross sections" (SINGLE-FETCH paraphrase).

### 3.2 Bender-Mannheim 0706.0207 is constructed on the OTHER side of that point

The C-operator construction (details in Section 4 below) carries the constraint (CHECKED — quoted identically in
two fetches):

> "β = γ²ω₁²ω₂²α, sinh(√(αβ)) = 2ω₁ω₂/(ω₁² − ω₂²)"

undefined at ω₁ = ω₂. The paper itself never says the construction fails there (verified negative, SINGLE-FETCH:
"The main text never states that the construction fails, diverges, or becomes singular at ω₁ = ω₂"); the only
equal-frequency statement in 0706.0207 is a footnote (CHECKED across two fetches):

> "it was shown that even if one uses the Dirac inner product for the Pais-Uhlenbeck theory, in the equal frequency
> limit (the case relevant to conformal gravity) the states of negative norm decouple from the Hamiltonian."

citing [14] Mannheim & Davidson, hep-th/0001115; [15] Mannheim & Davidson, Phys. Rev. A 71, 042110 (2005);
[16] Mannheim, Found. Phys. 37, 532 (2007) (CHECKED bibliography entries; contents UNVERIFIED — not fetched).

The explicit failure statement lives in the companion paper arXiv:0804.4190 = Phys. Rev. D 78, 025022 (2008),
abstract (CHECKED, verbatim):

> "It is shown that in this limit the similarity transform that was used for the unequal-frequency case becomes
> singular and that H_PU becomes a Jordan-block operator, which is nondiagonalizable and has fewer energy
> eigenstates than eigenvalues. Such a Hamiltonian has no Hermitian counterpart. Thus, the equal-frequency PT
> theory emerges as a distinct realization of quantum mechanics. ... These nonstationary states are needed to
> establish that the Jordan-block Hamiltonian of the equal-frequency Pais-Uhlenbeck model generates unitary time
> evolution."

**The structural finding of this intake:** on current primary texts, the two rescues' validity regimes are
*disjoint on the shared toy*. BM-0706.0207's no-ghost theorem is proved for ω₁ > ω₂ strictly ("without loss of
generality we take ω₁ ≥ ω₂", SINGLE-FETCH; eq. (15) singular at equality); BT's field theory is the equal-frequency
(double-pole) case per mode. The comparison point the federation cares about — the degenerate/Jordan boundary —
is exactly where the BM construction hands off from "similarity-equivalent to a Hermitian theory" to "distinct
realization with no Hermitian counterpart." This makes the R1 identity-or-difference question well-posed rather
than rhetorical, and it locates the interesting regime AT the boundary, not in the interior. (Gate only; R1's
outcome is not cited.)

### 3.3 Exact scope of the conformally-flat remark

Section VI, point 1 (CHECKED — reproduced across two fetches):

> "With Anderson and Herzog we have shown that PS theory describes a specific limit – the conformally flat limit –
> of quadratic gravity (QG), the renormalizable theory of quantum gravity mentioned above [27]. The invariance of
> QG under diffeomorphisms yields a Ward identity guaranteeing that renormalization preserves the special form of
> the PS Lagrangian. In the conformally flat limit, the spin two graviton, its ghost counterpart and a vector mode
> [30] decouple, leaving the conformal factor of the metric as the only interacting degree of freedom."

Fine print, itemized:

1. **The claim rests on a to-appear reference.** [27] = "M. Anderson, S. Bateman, F. Herzog, and N. Turok,
   Conformally Flat Limit of Quadratic Gravity (2026b), to appear" (CHECKED bibliography entry). Like the IR
   claim, unpublished.
2. **"Quadratic gravity", not Mannheim's Weyl²-only conformal gravity.** The identification is with QG generally;
   the bridge to the federation's Mannheim seat is via [30] = Riegert, Phys. Lett. B 134, 56 (1984) on linearized
   *conformal* gravity's particle content (CHECKED bibliography entry) — but BT's own sentence names QG.
3. **The spin-2 ghost is outside the theorem.** In the limit BT quantize, "the spin two graviton, its ghost
   counterpart and a vector mode decouple." The tree-positivity theorem covers the conformal factor only. The
   sector where Mannheim's ghost fight actually lives (the Weyl² spin-2 ghost) is decoupled by construction, so
   nothing in 2607.00096 adjudicates it.
4. Remainder of point 1 (CHECKED, same section quote): de Sitter and anti-de Sitter remain as backgrounds,
   "Quantum gravitational processes can hence be consistently studied in these backgrounds, albeit without
   gravitons [27]"; the long-wavelength classical instability is reinterpreted as "the familiar blowup of the
   cosmological scale factor in de Sitter spacetime," stable "in the usual cosmological sense" once zero modes are
   handled.

One more Section VI item that bears on the federation's breaking story (CHECKED, full-section quote): "we expect
PS theory to generate a mass gap as well as a vev ⟨(∂φ)²⟩ which will break scale symmetry dynamically," with
lattice support attributed to initial investigations "(with P. Morandes)" showing "composite shift-invariant
operators, like (∂φ)² acquire nonzero vacuum expectation values when the coupling λ becomes strong." For T5'
typing: BT's language is **formed-condensate** (a vev turning on), which is the datum the T5' sign-reconciliation
question needs on the BT side.

## 4. Bender-Mannheim's C operator: construction, domain, equal frequency, Krein

- **Construction** (SINGLE-FETCH equations, consistent across the two fetches at sentence level): C satisfies
  "C² = 1, [C, PT] = 0, [C, H] = 0" (eq. 13) with C built from Q = αpq + βxy (eq. 14); the theory is mapped to a
  Dirac-Hermitian one by the similarity transform H̃ = e^{−Q/2} H e^{Q/2} = p²/2γ + q²/(2γω₁²) + (γ/2)ω₁²x² +
  (γ/2)ω₁²ω₂²y² (eq. 17), subject to the eq. (15) constraint quoted in 3.2.
- **Domain of validity:** the operators are defined on "complementary (north, south) Stokes' wedges" in the
  complex-z plane where the ground state "vanishes exponentially rapidly as |z| → ∞" (SINGLE-FETCH); frequencies
  ordered ω₁ ≥ ω₂ with the construction requiring strict inequality via eq. (15).
- **Equal frequency in their own words:** in 0706.0207 itself, only the footnote quoted in 3.2 (negative-norm
  states decouple under the Dirac inner product; "the case relevant to conformal gravity"). The failure-and-
  replacement statement is in 0804.4190's abstract (quoted in 3.2): the transform becomes singular, H_PU becomes
  Jordan-block with no Hermitian counterpart, and unitarity is re-established via nonstationary states.
- **Krein fundamental symmetries:** 0706.0207 makes **no reference** to Krein spaces, indefinite-metric
  quantization as such, or fundamental symmetries beyond PT (CHECKED-negative across two fetches: "Not mentioned").
  The Krein-theoretic reading of the C operator is our (and later literature's) gloss, not BM's own language —
  from-memory context, flagged.
- **Concluding claim** (SINGLE-FETCH, verbatim): "The appearance of a ghost state when one takes the derivative
  operator to be Hermitian on the real z axis is not an indication that there is anything wrong with the theory
  itself, but only with the way it is being analysed. Consequently, if treated properly, higher derivative theories
  such as conformal gravity have the potential to be completely viable as quantum theories of gravity in four
  spacetime dimensions."

## 5. Matter coupling and gauge sectors (the fourth-seat question)

- **BT:** no treatment of matter or gauge coupling. The entirety of the gauge-sector record (Section VI, point 2,
  CHECKED full-section quote): "We have also studied gauged versions: the results will be presented elsewhere."
  Plus the O(N,N) generalization: "we have studied the theory of a N-component, four-derivative dimensionless
  scalar on ℝ×S^(N−1) which embeds in a O(N,N)-invariant model of two-derivative fields" — a scalar family, not a
  gauge sector. The Standard Model appears only as motivation (SINGLE-FETCH negative on any SM coupling).
- **BM:** nothing; "the paper focuses exclusively on the isolated Pais-Uhlenbeck oscillator model" (CHECKED-negative
  in the sense that no fetch surfaced any matter/gauge content).
- **Fourth-seat (T8') consequence, stated as a gate:** neither primary source fills or even addresses the seat.
  The closest future-work pointer in the whole record is BT's one-sentence "gauged versions... presented elsewhere."
  T8' remains a seat nobody fills, now confirmed at rung 0 rather than assumed.

## 6. Corrections to from-memory claims in the repo's federation/cross-exam docs

1. **Citation correction (firm, with provenance).** The cross-exam doc's frontmatter and source list cite
   "Bender & Mannheim, No-ghost theorem..., Phys. Rev. D 78, 025022 (2008), arXiv:0706.0207". Wrong pairing:
   arXiv:0706.0207 was published as **Phys. Rev. Lett. 100, 110402 (2008)** (CHECKED, arXiv abstract page,
   report no. LA-UR-07-3525). **Phys. Rev. D 78, 025022 (2008)** is the *companion* paper arXiv:0804.4190,
   "Exactly solvable PT-symmetric Hamiltonian having no Hermitian counterpart" (CHECKED, both abstract pages).
   The error's origin: **BT's own reference [7]** prints the no-ghost-theorem title with the PRD journal reference
   and the 0706.0207 arXiv id (CHECKED bibliography entry) — the cross-exam doc inherited BT's bibliography
   conflation. Ironically the conflated citation fuses exactly the two papers whose split (unequal-frequency
   C-operator vs equal-frequency Jordan block) is the fine print that matters.
2. **The "C operator fails at the degenerate boundary" expectation, half-corrected.** The cross-exam doc's
   first-principles expectation reads: the two rescues "diverge at the degenerate/Jordan boundary, where the
   C operator fails to exist but the kinematic parity survives." The primary sources confirm the failure half —
   the similarity transform "becomes singular" and H_PU has "no Hermitian counterpart" at ω₁ = ω₂ (0804.4190,
   their own words) — but NOT the abandonment half: BM claim the equal-frequency theory remains a *unitary*
   "distinct realization of quantum mechanics" via nonstationary Jordan-block states. So at the boundary the
   correct statement is "the Hermitian-equivalence route fails and PT quantization continues in a modified,
   non-diagonalizable form," not "the rescue fails." Any boundary-divergence argument must engage 0804.4190's
   surviving construction, not just eq. (15)'s singularity.
3. **"Loops open" (synthesis doc), refined rather than overturned.** True as stated but coarse: pseudo-unitarity/
   optical theorem is claimed to all orders; what is open at loops is *positivity* plus the collinear-IR treatment
   of asymptotic states; loop-integral IR finiteness is claimed proven in the to-appear [25]. The open frontier is
   the Born-rule layer, not the unitarity layer.
4. **"Cite Bender-Mannheim only in passing" (cross-exam doc), confirmed and slightly strengthened.** [7] appears
   in the bibliography; no fetch found any substantive in-text engagement, and no adjudication against PT
   quantization exists anywhere in the text (consistent across fetches). One fetch reported zero in-text
   occurrences outside the bibliography; whether [7] hides inside a group citation bracket is UNVERIFIED, so
   "only in passing" stands as the floor and "bibliography-only" is possible.
5. **"Their toy = the conformally flat limit of quadratic gravity" (both docs), confirmed with a scope caveat.**
   Verbatim supported — but resting on to-appear [27], and with the spin-2 graviton and its ghost decoupled in
   that limit, so the toy's positivity theorem does not touch the Weyl² spin-2 ghost sector where the Mannheim
   seat's fight lives.

## 7. UNVERIFIED remainders

- Contents of to-appear refs [25] (Renormalization of a Four-Derivative Theory) and [27] (Conformally Flat Limit
  of Quadratic Gravity) — announced, not available. The loop-IR and QG-limit claims are promissory until these land.
- Contents of BM's equal-frequency decoupling refs [14] hep-th/0001115, [15] PRA 71 042110, [16] Found. Phys. 37
  532 — cited here only as BM cite them.
- Whether BT's [7] appears inside any in-text group citation bracket (HTML fetch granularity).
- All SINGLE-FETCH quotes above carry residual transcription risk; none is load-bearing alone (each cross-braces
  with at least one CHECKED item).
- Turok's separate 36-field/three-generations claim (TOE interview) — out of scope for this route; remains
  unaudited, as the cross-exam doc already records.

## 8. What this intake hands the executing legs

- **T9' (loop gate):** target the Born-rule/trace-positivity layer at one loop on the PU/PS toy, phrased at the
  |ℳ|² level; pseudo-unitarity is not where the leak can be. Kill condition 7 remains live and undecided by the
  primary source.
- **R1 gate (stated as conditional):** the well-posed comparison is at the degenerate boundary, where BM-0706's
  construction is singular but BM-0804's replacement construction claims survival; identity-vs-difference of the
  rescues must be decided against the Jordan-block realization, not the generic-frequency one.
- **T8' (fourth seat):** confirmed empty at rung 0; BT's "gauged versions" sentence is the only thread.
- **T5' (map/sign):** BT-side condensate language is "formed" (⟨(∂φ)²⟩ turns on at strong coupling), now sourced.
- **Citation hygiene:** all repo docs citing 0706.0207 should carry PRL 100, 110402 (2008); PRD 78, 025022 is
  0804.4190 and is a *different* paper that the federation's degenerate-boundary arguments actually need.
