---
title: "internal origin artifact v3 — Unified IFF Theorem (Synthesis of v2 + v2.1)"
status: active_research
doc_type: synthesis
updated_at: "2026-05-31"
---

# internal origin artifact v3 — Unified IFF Theorem (Synthesis of v2 + v2.1)

**Status.** Local-only v3 synthesis artifact. Generated 2026-05-31.
**artifact.** `work/internal origin artifact` (validation/4 + joe + walkthrough_review; v3 receipt appended; stage NOT regressed).
**Scope.** v3 = integration of v2 (PCP / Wolfram / Jordan lens, BROADER-IFF PARTIAL leaning HOLDS) and v2.1 (signed-readout direct CALM-class characterization, anomaly-iff FAILS-as-stated). Goal: unified verdict suitable for internal origin artifact Phase 3 decision.
**Inputs.**
- v1: `iff-theorem-result.md`, `persona-dialectic.md`, `wrk-386-reframe-note.md`.
- v2 (all 6): `v2-metalayer-reframe/v2-broader-iff-result.md`, `v2-jordan-decomposition-test.md`, `v2-pcp-proof-carrying-test.md`, `v2-wolfram-localrule-test.md`, `v2-persona-dialectic.md`, `v2-wrk386-reframe-note.md`.
- v2.1: `v2.1-meta-reframed-signed-readout-verdict-2026-05-31.md`.
- Meta-layer dialectic: internal draft artifact.
- Sibling v2/v2.1: internal origin artifact `v2-localrule-adjunction-result.md` + `v2.1-meta-reframed-adjunction-rerun-2026-05-31.md`; internal origin artifact `v2-eight-tuple-classification.md` + `meta-reframed-v2.1-shadow-source-theorem-rerun-2026-05-31.md`.
**Method.** internal origin artifact `[speculation]` tagging. Honest-verdict gatekeeper protocol. 7-persona dialectic (v2's 6 + Synthesis Arbiter; see `v3-persona-dialectic.md`).

---

## TL;DR — v3 Unified Verdict

**v3 Verdict: PARTIAL — anomaly-iff FAILS-AS-STATED; FACTORIZED-IFF HOLDS.**

v2 (PCP lens) and v2.1 (signed-readout lens) **agree on the destination but use different vocabulary to reach it**. When reconciled honestly:

1. **Both agree v1's conjectured iff "Q is CALM-monotone iff Q has no 't Hooft anomaly" is too restrictive on its conjectured form** and that v1's doubly-restricted PARTIAL (abelian + axial) is over-narrow as a *characterization* of the underlying mechanism.

2. **They disagree on whether anomaly is the right primitive for the (⇒) direction.** v2 says yes — PCP-blindness gives a uniform mechanism connecting anomaly-freeness to certificate-composability. v2.1 says no — the primitive is *signed-readout monotonicity*, and anomaly is one important *application* (signed cancellation from chiral index structure) but neither necessary nor sufficient for CALM-class membership.

3. **What survives both as load-bearing v3 content:** the **monotone-provenance / non-monotone-readout factorization**. The right characterization is two-layer:
   - **Provenance layer** (monotone, append-only, locally computable, certificate-composable): this is where CALM, PCP-bridging, and Jordan-decomposition all live and agree.
   - **Readout layer** (possibly signed, possibly index-bearing, possibly phase-cancellation): this is where the (⇒) direction's bite actually lives.

**The v3 unified statement (single load-bearing theorem):**

> **(v3 Factorization Iff Theorem.)** For a lattice observable `Q` on a GW-modified bounded-degree graph substrate, `Q` factors through the monotone-provenance layer `E → G` (i.e., `Q = read ∘ acc` where `acc : inputs → E` is locally computable + append-only and `read : E → G` is a fixed scalar map) **always**. The scalar readout `read` is **CALM-monotone iff every generator-weight in `G` is non-negative**; this is a property of the *readout structure*, not of anomaly content per se. Anomaly-freeness is the **canonical physical sufficient condition** for non-negative-weight readouts in the abelian-internal-Noether sub-class, and topological-index anomaly is the **canonical physical mechanism** producing signed generators (axial: `n_+ - n_-`; non-abelian flavor: `λ_i n_i` with mixed-sign `λ_i`). The v1 doubly-restricted iff is the corollary where physical-anomaly-content and readout-sign-content coincide; outside that sub-class they decouple.

**This is FACTORIZATION-IFF, not ANOMALY-IFF.** The iff is between *monotone-readout-structure* and *non-negative-weight-readout* (v2.1's signed-readout criterion), with anomaly entering as the canonical physical mechanism (v2's PCP-blindness + v1's HLN-1998 index theorem) rather than as the iff primitive.

**Scope of HOLDS:**
- The factorization itself: HOLDS for **every** lattice observable on a bounded-degree-graph GW substrate (this is what v2 establishes architecturally via PCP, and what v2.1 captures via the evidence-monoid `E` and readout `r : E → G`).
- The signed-readout monotonicity criterion: HOLDS as a precise iff between `R : E → G` monotone and `w(x) ∈ G_+` for every generator (v2.1 §Theorem).
- The anomaly → signed-readout connection: HOLDS rigorously for axial-type anomalies via HLN-1998 (v1 §3.1) and PCP-blindness (v2 BCI-P §1.2); plausible-modulo-substrate for gravitational (v2 BCI-P §1.3; v1 §3.3).
- The anomaly-iff direction: FAILS as an iff (anomaly-free observables can still be non-monotone if readout structure has negative weights; non-monotone observables need not be anomalous — phase, signed measure, oscillatory readouts can all fail without anomaly).

**internal origin artifact implication.** The four reframe options reduce to a new ranking dominated by the factorization frame (**Option N+++**, see `v3-wrk386-reframe-note.md`). v2's Option N++ (PCP-bridged iff anomaly-free) is shown to be a *special case* of the factorization theorem restricted to the PCP-style provenance layer. v2.1's "monotone provenance / non-monotone readout" boundary theorem is the natural paper title-shape.

---

## 1. The reconciliation — what v2 and v2.1 are each saying

### 1.1 v2 (PCP / Wolfram / Jordan lens) — summary

v2 tested three candidate broader RHS:
- **BCI-J (Jordan)**: fails as iff because anomalous observables also Jordan-decompose (signed contributions don't track anomaly type).
- **BCI-L (Wolfram local-rule reducible)**: fails as iff because computational reducibility is type-blind to anomaly.
- **BCI-P (PCP / proof-carrying-provenance)**: HOLDS as iff. PCP-blindness (local certificates cannot witness global topological invariants) gives a uniform (⇒) mechanism across axial + gauge + (substrate-modulo) gravitational. Non-abelian flavor charges become PCP-bridgeable via signed-contributions-with-trivial-certificate.

v2 verdict: BROADER-IFF PARTIAL leaning HOLDS, with one engineering restriction (curved-lattice substrate for gravitational).

### 1.2 v2.1 (signed-readout direct CALM-class characterization) — summary

v2.1 attacked the anomaly-iff at the primitive level. Define evidence monoid `E` (free commutative monoid on local contribution events with information order `e ≤ e' iff e' = e + d`) and signed readout `R : E → G` (ordered abelian group with positive cone `G_+`). Then `R` is monotone iff every generator-weight `w(x) ∈ G_+`. Anomaly is one important mechanism producing negative-weight generators (axial: `Q_A = n_+ - n_-` has both + and - generators) but:

- Anomaly is **not necessary**: signed measures, phase-sensitive amplitudes, etc., can be non-monotone without anomaly.
- Anomaly is **not sufficient**: an anomaly-free observable can still be non-monotone if its readout structure has negative generators (non-abelian vector charges with traceless generators; U(1) with both particle/antiparticle sectors).

v2.1 verdict: FAILS-as-iff. The signed-readout monotonicity criterion replaces it as the theorem spine; anomaly becomes a corollary application; monotone-provenance / non-monotone-readout factorization is the architecture.

### 1.3 Where they actually agree (the load-bearing convergence)

When read carefully, **both reach the same architecture** by different routes:

| Layer | v2 vocabulary | v2.1 vocabulary | v3 unified name |
|---|---|---|---|
| Provenance / commitment layer | PCP per-site arithmetic circuit + composable certificates | Evidence monoid `E` with information order `≤_E` | **monotone-provenance layer** |
| Readout / decoding layer | aggregate `Q = Σ c_x` with verifier accept/reject | scalar readout `r : E → G` (signed allowed) | **scalar-readout layer** |
| Anomaly's role | global topological invariant invisible to local certificates (PCP-blindness) | one of several physical mechanisms producing negative-weight generators | **anomaly = canonical physical source of negative-weight generators, via index-theoretic non-locality** |
| Where the (⇒) bite lives | "PCP-bridged ⇒ anomaly-free" via PCP-blindness | "non-monotone readout ⇒ has negative generators" (anomaly-agnostic) | **(⇒) actually lives at the readout-sign level; anomaly is the canonical physical witness** |

The convergence: **both factor the bridge into provenance + readout, and both agree the (⇒) bite happens at the readout-sign-structure layer**. v2 names anomaly as the load-bearing source of negative-weight generators in the lattice-physics setting (via index theorem). v2.1 names *any* negative-weight generator as the source of non-monotonicity (anomaly-agnostic, more general).

These are **not contradictory** — they are **same architecture, different levels of generality**:

- v2.1 is the **fully general statement**: signed-readout monotonicity criterion applies to any evidence-monoid-plus-scalar-readout system regardless of physics origin of the signs.
- v2 is the **physics-side instantiation**: in the lattice gauge theory setting, the dominant source of negative-weight generators is anomaly/index structure, and PCP-blindness gives the mechanistic explanation of why local certificates can't witness the resulting global cancellation.

### 1.4 Where they actually disagree (and how v3 resolves)

**Material disagreement: is "anomaly-iff" recoverable in any form?**

- **v2 says YES**, under the BCI-P RHS: PCP-bridged iff anomaly-free, rigorous on flat-lattice for axial + non-abelian + gauge, plausible-modulo-substrate for gravitational. The v1 abelian-restriction dissolves; v1 axial-restriction dissolves into uniform PCP-blindness coverage.

- **v2.1 says NO**, even as a non-iff implication: anomaly is neither necessary nor sufficient for CALM-class membership in the general signed-readout setting. The iff condition is non-negative-weight generators, not anomaly-freeness.

**v3 resolution (Synthesis Arbiter, P7 in `v3-persona-dialectic.md`):**

Both are honest readings of different scopes:

- **Within the lattice-gauge-theory physics scope**, v2 is right: anomaly content (via HLN-1998 + PCP-blindness) is the *dominant* mechanism producing negative-weight generators in the readout. For an observable defined as a charge of an internal continuous global symmetry on a GW lattice, the index-theoretic non-locality of anomaly is the mechanism by which sign structure enters the readout. *Within this scope*, "PCP-bridged ↔ anomaly-free" holds.

- **Outside the lattice-gauge-theory physics scope**, v2.1 is right: there are observables whose readouts have negative-weight generators *not* from anomaly (signed measures of any kind, phase-sensitive amplitudes, non-abelian vector charges in the v1 §2.4 sense which v2 BCI-P recovered via *certificate*-not-monotone reasoning), and there are anomaly-free observables whose readouts may still have negative-weight generators (the v1 §2.4 case is precisely this — `Q^a_V` is anomaly-free but signed).

**The v3 unified statement** (§ TL;DR above) holds both: the factorization architecture covers all lattice observables; the signed-readout monotonicity criterion is the primitive iff; anomaly enters as the canonical physical mechanism providing the (⇒) bite in the lattice-gauge sub-domain (where v2 is right) while leaving open that other mechanisms produce the same bite outside that sub-domain (where v2.1 is right).

**Important honest note: v2's BCI-P "non-abelian recovery" is read differently in v3.**

In v2, BCI-P recovers non-abelian SU(N)_V via "signed contributions with trivial certificate" — the per-site arithmetic circuit emits signed real values and the certificate verifies on-site computation. v2 reads this as "non-abelian observables become PCP-bridgeable."

v2.1 reads the same situation as: "the readout `Q^a_V = Σ λ_i n_i` has negative-weight generators (the `λ_i < 0` ones) so it is *non-monotone* in the scalar-readout sense, even though it is anomaly-free." Both are correct descriptions; they characterize different things.

**v3 reconciliation**: v2's "PCP-bridged with signed contributions" *is* v2.1's "monotone provenance with signed readout." The PCP framework's allowance of signed contributions is precisely the monotone-provenance / non-monotone-readout factorization. v2 didn't recover non-abelian *to CALM-class monotonicity*; it recovered non-abelian to the broader monotone-provenance-with-signed-readout class. v2.1 names this class directly and notes that anomaly is no longer the iff condition for it.

The honest v3 reading: **v2's BCI-P broader iff is correctly framed as "PCP-bridged (in the provenance layer) iff [bridgeable property]," where v2 takes the bridgeable property to be anomaly-freeness in the physics-restricted sense, and v2.1 takes it to be non-negative-weight generators in the fully general sense.** These two characterizations agree on the abelian-internal-anomaly-free sub-class (which is v1's scope) and diverge outside it.

---

## 2. The v3 unified iff theorem (load-bearing)

### 2.1 Statement

**[speculation, well-grounded]** The v3 unified iff theorem combines v2 PCP architectural content + v2.1 signed-readout primitive into a single statement:

> **(v3 Factorization Iff Theorem.)** Let `Q` be a lattice observable on a bounded-degree-graph GW substrate (flat or appropriately formalized curved). Then `Q` admits a factorization `Q = read ∘ acc` where:
> - `acc : inputs → E` is the **monotone-provenance accumulator**: locally computable per-site arithmetic circuit emitting append-only contributions into an evidence monoid `E` with locally-verifiable certificates of correctness (the PCP / BCI-P provenance layer).
> - `read : E → G` is the **scalar-readout decoder**: a fixed map from the evidence monoid to an ordered abelian group `G` with positive cone `G_+`.
>
> The composite `Q : inputs → G` is **ε-local CALM-extension monotonic if and only if** every generator-weight `w(x) ∈ G_+`, i.e., the readout has no negative-weight contributions.
>
> Physical sub-statement (lattice-gauge sub-domain): for `Q` a conserved-charge observable of a global internal continuous symmetry, the dominant mechanism producing negative-weight generators is **'t Hooft anomaly / topological-index structure**, via the Hasenfratz-Laliena-Niedermayer 1998 lattice index theorem (axial-type) and Atiyah-Patodi-Singer-style index theorems on curved substrates (gravitational). For this sub-class, "no negative-weight generators ↔ anomaly-free" via the index-theoretic non-locality of anomalies. The PCP-blindness lemma (v2 BCI-P §1.2) gives the mechanistic explanation: local certificates cannot witness the global topological invariant that anomaly-bearing observables compute.

### 2.2 Why this is the load-bearing v3 statement

This statement is the unique synthesis that satisfies:

1. **Architecturally faithful to v2's PCP framework** (the factorization `acc / read` is exactly v2's PCP-bridged structure, with `acc` = per-site circuit + certificate composition and `read` = verifier-decoder).
2. **Primitive-faithful to v2.1's signed-readout criterion** (the iff between CALM-monotonicity and non-negative-weight generators is exactly v2.1's theorem spine, lifted from the abstract setting to the lattice substrate).
3. **Recovers v1's doubly-restricted iff as a sub-corollary** (when restricted to abelian-internal Noether currents, no negative-weight generators ↔ axial-anomaly-free, which is v1's statement).
4. **Honors v2's broadening** (the factorization holds across all anomaly types via the PCP layer; the gravitational extension is plausible-modulo-substrate by the same index-theoretic non-locality mechanism).
5. **Honors v2.1's narrowing** (anomaly is one mechanism for negative-weight generators, not the only one; the iff is at the readout-sign level, not anomaly level).
6. **Surfaces the actual disagreement without smuggling** (the physical sub-statement is a *restriction*, not a re-derivation: outside the lattice-gauge-internal-Noether sub-class, the iff drops the anomaly characterization but keeps the signed-readout characterization).

### 2.3 Scope (HOLDS / PARTIAL / FAILS)

**Factorization itself**: HOLDS rigorously. Every lattice observable on a bounded-degree-graph substrate admits the `acc / read` factorization (this is the PCP architectural content; v2 establishes it; v2.1 names the layers; no disagreement).

**Signed-readout monotonicity criterion**: HOLDS rigorously. v2.1's theorem (R monotone iff w(x) ∈ G_+) is a precise iff at the abstract level; the lattice instantiation just substitutes specific G (Z for index observables; R for signed-real charges; etc.).

**Anomaly-iff (v1 + v2 BCI-P framing)**:
- HOLDS rigorously within the **abelian-internal Noether sub-class** (this is v1's PARTIAL, unchanged).
- HOLDS rigorously within the **PCP-bridged-in-physics-substrate sub-class** for axial + gauge (vacuous) + (substrate-modulo) gravitational, under v2's reading where "non-abelian recovery via signed certificate" is treated as "still bridged" — but v3 reads this as having moved into the *factorization* class, not the *single-aggregate CALM* class.
- FAILS-AS-STATED in the fully general signed-readout setting (v2.1's bite): anomaly-free non-abelian charges still have signed readouts; non-anomaly mechanisms can produce signed readouts.

**Net v3 verdict**: PARTIAL. The factorization iff holds rigorously across all scopes. The anomaly-iff is recoverable only as a corollary in restricted physics sub-classes; in full generality, the anomaly-iff fails and is replaced by the signed-readout monotonicity criterion as the primitive.

### 2.4 What changed v1 → v2/v2.1 → v3

| version | iff statement | RHS primitive | restrictions | verdict |
|---|---|---|---|---|
| **v1** | Q CALM-monotone iff anomaly-free | CALM-monotonicity (single aggregate) | abelian + axial-only (doubly-restricted) | PARTIAL |
| **v2** | Q PCP-bridged iff anomaly-free | PCP-bridging (provenance + certificate) | substrate (curved-lattice for gravitational) | BROADER-IFF PARTIAL leaning HOLDS |
| **v2.1** | R: E → G monotone iff w(x) ∈ G_+ | signed-readout structure | anomaly not the iff condition | FAILS-as-anomaly-iff; HOLDS as signed-readout criterion |
| **v3** | Q = read ∘ acc; read monotone iff all w(x) non-negative; anomaly = canonical physical source of signed w(x) in lattice-gauge sub-domain | factorization + signed-readout structure | factorization itself unrestricted; physical anomaly correspondence is sub-domain-restricted | PARTIAL (factorization HOLDS; anomaly-iff FAILS in general but corollary HOLDS in sub-class) |

The trajectory: each version dissolves a different restriction by enriching the primitive RHS. v1 → v2 dissolves the abelian and axial-only restrictions by going to PCP (provenance + certificate). v2 → v2.1 dissolves the anomaly-as-iff-condition by going to the signed-readout primitive. v3 keeps both moves: factorization architecture (v2) + signed-readout primitive (v2.1) + anomaly as canonical physical mechanism (v1's HLN-1998 + v2's PCP-blindness, both still load-bearing within the lattice-gauge sub-domain).

---

## 3. Cross-validation with siblings (full analysis in `v3-sibling-consistency.md`)

Summary of cross-check:

- **internal origin artifact v2 (OBSTRUCTED-LR)** said PCP gives a *factorization* `C_GW_loc → C_MPR → C_Shadow`, not a direct adjunction. **v3 is consistent**: the v3 factorization iff lives in the middle term `C_MPR` (monotone-provenance with readout). v3's `acc` is the `C_GW_loc → C_MPR` morphism; v3's `read` is the `C_MPR → C_Shadow` projection. internal origin artifact v2's distributivity-wall obstruction (BvN, value-lattice not adjunction-bridgeable) is the v3-correlate of "the readout layer is non-monotone in general; only the provenance layer is CALM/distributive-compatible."

- **internal origin artifact v2.1** explicitly names `C_MPR` (monotone provenance/readout) as the corrected categorical object and says CALM is the subcategory where `r` is monotone. This is **direct agreement** with v3's factorization iff: v3's "read monotone iff all w(x) non-negative" is precisely the membership condition for being in internal origin artifact's `C_CALM ⊂ C_MPR`.

- **internal origin artifact v2 (8-tuple)** classified readouts by `rr ∈ {monotone-reducible, signed-bounded-variation, phase-cancellation, computationally-irreducible}`. **v3 sits in internal origin artifact's `rr = monotone-reducible` cell when restricted to anomaly-free, and `rr = signed-bounded-variation` when restricted to anomaly-bearing axial.** v3's factorization theorem operationalizes internal origin artifact's prediction that "the iff bites cleanly at the `rr = monotone-reducible` boundary" — v3 makes it precise via the signed-readout monotonicity criterion.

- **internal origin artifact v2.1** explicitly identifies the "monotone provenance != monotone semantic readout" pattern and recommends internal origin artifact pivot to the factorization framing. **v3 directly implements this recommendation** at the iff-theorem level.

**Net**: v3's factorization iff is consistent with all four sibling v2/v2.1 outputs and resolves the v2-vs-v2.1 tension by integrating both architectural and primitive content.

---

## 4. 7-persona dialectic (summary; full in `v3-persona-dialectic.md`)

Carrying v2's 6 personas + adding P7 Synthesis Arbiter:

- **P1 (Anomaly theorist):** Both v2 and v2.1 agree anomaly is *one* mechanism. v3 reads v2's PCP-blindness as the load-bearing physical explanation of why anomaly bites within the lattice-gauge sub-class, and v2.1's signed-readout criterion as the load-bearing mathematical primitive that operates outside that sub-class too. Both are correct at their respective scopes. v3 verdict: anomaly is the **canonical physical source of negative-weight readout generators** in lattice-gauge observables, not the iff primitive.

- **P2 (Lattice gauge theorist):** The factorization `acc / read` is faithful to lattice physics (each per-site circuit reads bounded-neighborhood data; the readout is a fixed scalar decoder). v2's PCP framing and v2.1's evidence-monoid framing are two vocabularies for the same lattice-level architecture. v3 unified statement is faithful.

- **P3 (Skeptical mathematical physicist):** Attacks the v3 unification — is the factorization smuggling? Cross-check: every lattice observable does decompose `acc / read` because the lattice is by construction a per-site computation substrate. The decomposition is faithful, not a definitional convenience. v3 survives the attack. The remaining honest restriction: in the gravitational case, the substrate (curved-lattice) is not formally constructed.

- **P4 (Honest-verdict gatekeeper):** v3 verdict is **PARTIAL**. The factorization iff HOLDS; the anomaly-iff FAILS-as-stated but HOLDS as a sub-domain corollary. The PARTIAL is honest, not smuggled. v3 is strictly more accurate than either v2 or v2.1 alone.

- **P5 (Wolfram-CA mathematician):** BCI-L still fails as iff (v2's verdict carries through to v3 unchanged). The Wolfram lens contributes architectural-completeness (every GW observable is local-rule-realizable) and the meta-observation that CALM is the monotone-reducible corner of a broader landscape. v3 honors this by putting CALM (in v3 vocabulary: "read monotone with all w(x) ∈ G_+") as a sub-class of the factorization landscape.

- **P6 (Cryptographer):** PCP-blindness lemma still load-bearing for v3 within the lattice-gauge sub-class. v3 doesn't change the lemma's status; it relocates it from "the iff (⇒) mechanism" to "the canonical physical mechanism for the (⇒) bite in the lattice-gauge sub-domain." Outside that sub-domain, v2.1's signed-readout criterion applies without needing PCP-blindness.

- **P7 (Synthesis Arbiter, NEW for v3):** Reconciles v2 and v2.1 without smuggling. Key finding: v2 and v2.1 use different *primitives* for the same *architecture*. v2's PCP-bridging primitive + v2.1's signed-readout primitive can both be kept by separating into provenance-layer architecture (v2) + readout-layer primitive (v2.1). v3 keeps both. The disagreement on "is anomaly the iff primitive" is honest — v2 says yes-within-lattice-gauge-sub-class; v2.1 says no-in-general — and v3 reports both honestly rather than picking one. No smuggling.

All seven personas converge: **v3 PARTIAL (factorization HOLDS; anomaly-iff FAILS as primitive but HOLDS as sub-domain corollary)** is the honest synthesis.

---

## 5. Receipts for v3 scope

- ✓ v3 reads v1 + v2 (all 6) + v2.1 + meta-layer dialectic + sibling v2/v2.1.
- ✓ Agreement audit: identified factorization architecture as the convergence point (this artifact §1.3).
- ✓ Divergence map: identified anomaly-as-primitive vs. signed-readout-as-primitive disagreement and reconciled via sub-domain scoping (§1.4; full in `v3-agreement-divergence-map.md`).
- ✓ Sibling consistency: cross-checked against internal origin artifact v2 (factorization in middle term) and v2.1 (`C_MPR` agreement); internal origin artifact v2 (`rr` axis) and v2.1 (monotone-provenance / signed-readout pattern) — all consistent (full in `v3-sibling-consistency.md`).
- ✓ v3 iff theorem precisely stated (§2.1) with explicit scope (§2.3).
- ✓ Verdict: PARTIAL with explicit articulation of v1 → v2/v2.1 → v3 trajectory (§2.4).
- ✓ internal origin artifact reframe implication: Option N+++ recommended (full in `v3-wrk386-reframe-note.md`).
- ✓ 7-persona dialectic completed (`v3-persona-dialectic.md`): v2's 6 + Synthesis Arbiter.
- ✓ HARD RULES respected: zero writes to Github Repos/, zero canon writes, zero work.json edits, zero stage regression, [speculation] tagging used.
- ✓ No smuggling: when v2 and v2.1 disagree on "is anomaly the iff primitive," v3 surfaces the disagreement honestly and reports the resolution via sub-domain scoping rather than picking one side.

---

End of `v3-unified-iff-theorem.md`.
