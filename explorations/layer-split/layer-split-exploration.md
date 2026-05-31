---
title: "WRK-397 — Layer-Split Framing Exploration"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# WRK-397 — Layer-Split Framing Exploration

## 0. Frame

This is **exploration**, not publication retreat. The brief: 5 personas across the WRK-394 meta-assessment (Anomaly, Network propagation, Distributed systems, Sound engineering, Complexity science) independently surfaced that the bridge work conflated **propagation / decision / anomaly-class / coarse-graining** as if they were one object. The literature on each layer keeps them separate. The hypothesis under test: a layer-split bridge is a more honest, more publishable, and potentially structurally different object — with at least one layer (propagation) likely surviving even though others (decision) fail.

The output is a **per-layer verdict** in the validators' own language, not a publication recommendation. Three verdicts per layer: **HOLDS** (the bridge claim at this layer survives validator scrutiny); **BROKEN-IN-LAYER** (the validator critique kills this specific layer's bridge claim); **NOT-APPLICABLE** (the bridge doesn't make sense at this layer). Plus a cross-layer interaction map.

Dialectic seed: the 5 personas from the card (Network propagation thesis, Distributed-systems theorist thesis, Anomaly theorist thesis, Complexity / coarse-graining antithesis, Honest-verdict gatekeeper synthesis).

---

## 1. Layer definitions (literature-anchored)

Precise definitions before any verdict. Anchors named; `[speculation]` tagging where the cross-field mapping is constructed-here rather than derived.

### 1.1 Propagation layer

**Definition.** The layer of *local state dissemination*: how a per-site contribution becomes visible to neighbors, and how state spreads across the lattice/network without requiring any commitment to a final value. Constituent operations: per-site update rule; neighbor-to-neighbor message exchange; anti-entropy reconciliation; bounded-radius read.

**CS-side anchors.**
- Demers et al. 1987 (epidemic / gossip / anti-entropy algorithms): propagation as monotone information accrual; no commitment until convergence.
- Shapiro-Preguica-Baquero-Zawirski 2011 (CRDT survey): join-semilattice as the propagation-layer object; **append-only** ledger; convergence by commutative-associative join.
- Hellerstein-Alvaro 2020 (CALM): the *propagation* fragment of CALM is the monotone-information part; coordination-freeness applies at this layer.

**Physics-side anchors.**
- Ginsparg-Wilson 1982 / Lüscher 1998: the GW relation `{D, gamma_5} = a D gamma_5 R D` is an *operator-locality constraint* — exponentially-decaying matrix elements `|D(x,y)| <= C exp(-gamma d(x,y)/a)` (Hernandez-Jansen-Luscher 1999).
- Local Dirac propagation: the Dirac operator's exponential locality is precisely a per-site rule with bounded-radius effective support; this is the physics-side propagation primitive.
- Wilson loops as locally-computable observables in lattice gauge theory.

**The bridge claim at this layer (restated precisely).** *Append-only / gossip-style monotone propagation on the CS side is structurally analogous to exponentially-local Dirac-operator propagation on the physics side. Both are "coordination-free local rule application until convergence" with no commitment to a final readout.*

### 1.2 Decision layer

**Definition.** The layer at which the system *commits to a value* — a threshold crossing, a finality decision, a readout decoder applied to converged state. Distinct from propagation in that decisions are *non-reversible* and may require global state to evaluate (threshold across the whole lattice, index across the whole gauge configuration).

**CS-side anchors.**
- Fischer-Lynch-Paterson 1985 (FLP impossibility): asynchronous deterministic consensus is impossible with even one faulty process — the canonical *decision-layer* no-go.
- Paxos / Raft (Lamport 1998 / Ongaro-Ousterhout 2014): consensus protocols for decision-finality under crash failures.
- CALM theorem's *decision* fragment: the consistency claim is about what programs converge to a *fixed final value* without coordination; non-monotone queries fall outside.
- Hahn-Wadler / Bloom / safety-liveness duality (referenced by CS-reviewer persona): separation of "what could be" vs "what is committed."

**Physics-side anchors.**
- Lattice index theorem / Hasenfratz-Laliena-Niedermayer 1998 form: `Q_A = n_+ - n_-` is a global readout requiring access to the full spectrum.
- Atiyah-Singer index on the lattice: the index is a *decision* — an integer commitment given a converged gauge configuration.
- Threshold observables: phase-transition order parameters; chiral susceptibility crossing zero.

**The bridge claim at this layer.** *CALM's class of coordination-free decisions corresponds to GW observables whose readout decoder requires no global aggregation. The canonical axial-charge readout is in the **excluded** class (requires global signed aggregation, threshold crossing).*

**Note.** The decision layer is where WRK-387's falsification lives: `Q(A)=Q(B)=0, Q(A union B)=1` is a decision-layer counterexample (the decision flips non-monotonically), not a propagation-layer counterexample.

### 1.3 Anomaly-class layer

**Definition.** The layer at which the observable carries *topological / cohomological / index-theoretic content* — the layer where the observable's information lives in a discrete invariant of the symmetry algebra rather than in a per-site magnitude. Anomaly inflow, Dai-Freed pairing, 't Hooft anomaly classification.

**Physics-side anchors.**
- 't Hooft 1980 (anomaly matching): anomalies are invariants of the global symmetry algebra; preserved across IR / UV.
- Freed-Hopkins 2016 (anomaly inflow, invertible field theories): anomaly classes are SPT-phase labels.
- Dai-Freed 1994 (eta-invariant pairing): topological invariant living in the cobordism group.
- Atiyah-Singer index theorem (the canonical anomaly-class witness): index = topological-charge for chiral fermions.

**CS-side anchors.** `[speculation]` — there is no off-the-shelf CS analog with comparable depth. Candidate analogs:
- Topos QM / Bohr-topos (Doering-Isham, Heunen-Landsman-Spitters): classifying topos of a quantum system as carrying invariants of the algebra.
- Cohomological obstruction theory in concurrency (work by Mazurkiewicz / Goubault on directed-algebraic-topology for concurrent systems): pure-mathematical analog, not yet wired into CRDT / CALM literature.
- The "exclusion class" of CALM itself, if read as an invariant of the program's monotone-vs-non-monotone signature — but this is a typing-classification, not a cohomological invariant.

**The bridge claim at this layer.** Per the Anomaly theorist (persona 3 in WRK-394): the *correct* bridge target on the physics side is anomaly-class / inflow, not per-observable readout. On the CS side, the *correct* target is the **exclusion class** of CALM — the typed invariant that says "this program needs coordination." `[speculation]` These are both invariants-of-the-classifying-object, not properties-of-individual-observables. Whether they constitute a "bridge" or merely "structural rhyme between two classification invariants" is the open question.

### 1.4 Coarse-graining layer

**Definition.** The layer at which a *macro-observable emerges from micro-state* via projection / RG-flow / order-parameter extraction. The defining feature: coarse-graining generically does *not* commute with local-rule application (the "RG-non-commutation square").

**Physics-side anchors.**
- Wilson 1971 / Kadanoff 1966 (Renormalization Group): coarse-graining as block-spin / momentum-shell integration; emergent macroscale observables.
- Goldenfeld 1992 (lectures on phase transitions): order parameters as coarse-grained macro-observables that change non-monotonically at phase transitions.
- Mehta-Schwab 2014 (RG as deep-learning): RG-flow as projection; loss of micro-information.

**CS-side anchors.**
- Coarse-grained CRDTs: tier-based replication, hierarchical aggregation. Less developed than RG.
- Aggregation hierarchies in stream processing (Apache Beam windowing, watermarks): macro-observable extraction from micro-event-stream. Closer in shape than RG but without the renormalization apparatus.
- `[speculation]` Computational mechanics (Crutchfield / Shalizi): epsilon-machines as coarse-grained projections of stochastic processes; possibly the closest CS-side analog with comparable mathematical depth.

**The bridge claim at this layer.** Per the Complexity-science persona (17 in WRK-394): the Wall theorem may be a *non-commuting-square obstruction in RG flow* — `local-rule + RG != RG + local-rule` for non-monotone observables. `[speculation]` The CALM <-> GW bridge at this layer would say: coarse-graining-vs-local-rule commutation is the *same* obstruction in both fields, manifesting as monotonicity-loss on the CS side and as anomaly / phase-transition non-commutation on the physics side.

---

## 2. Per-layer verdict against validator findings

For each layer: restated bridge claim, evidence/counterexample mapping to validator items (V-1 through V-6), verdict label.

### 2.1 Propagation layer

**Restated claim.** *Append-only / gossip-style monotone propagation on the CS side is structurally analogous to exponentially-local Dirac-operator propagation on the physics side. Both are "coordination-free local rule application until convergence" with no commitment to a final readout.*

**Validator item mapping.**
- **V-5 (epsilon-local CALM extension).** V2's counterexample (`Q(A)=Q(B)=0, Q(A union B)=1`) lives entirely at the **decision** layer — the join operation that flips Q from 0 to 1 is a readout-decoder operation, not a propagation operation. The propagation underlying it (the per-site contributions to gauge state) IS monotone; what's non-monotone is the signed *readout*. **V-5 does not kill the propagation-layer bridge.** [Network propagation persona; confirmed by Distributed systems persona's "exclusion class" reframe.]
- **V-3 (PCP-blindness lemma).** PCP-blindness as stated is a *certificate / readout* claim, not a propagation claim. Gossip propagation does propagate global state via local exchanges (epidemic broadcast convergence); the PCP critique kills a separate claim about local-certs-being-blind-to-global. **V-3 does not bear on the propagation-layer bridge.**
- **V-1 (C_MPR coherence).** The C_MPR construction's `acc` / `read` factorization separates propagation (`acc`) from readout (`read`). The propagation-layer claim is the cleaner `acc`-only sub-claim. V-1's "needs more proof" critique applies to the full tuple; the propagation-sub-tuple is tighter and more defensible.
- **V-2 (BvN generalization).** Lives at the typed-algebra layer (distributive vs orthomodular); orthogonal to propagation.
- **V-4 (HLN universal lifting).** Lives at the cross-substrate-lifting layer; "restrict to axial" leaves the propagation-layer claim intact in the restricted scope.
- **V-6 (prior art).** Substantial prior art on CRDT / gossip / anti-entropy on the CS side; substantial prior art on GW locality (Hernandez-Jansen-Luscher) on the physics side. The propagation-layer bridge is therefore a *constructive cross-field instantiation* of two well-developed local-rule theories. Novelty is the cross-field rhyme, not either side.

**Verdict.** **HOLDS** — but as a *cross-field structural rhyme* rather than a novel mathematical bridge. The validator critiques (V-3, V-5) live at different layers and do not reach this layer. The contribution is real but smaller than the v3 syntheses claimed; the literature on each side is mature.

**Evidence weight.** Network propagation persona (high authority on the CS side). Lattice QFT persona implicitly endorses (locality is the load-bearing physics-side property). Anomaly theorist: defers (anomaly content is not at this layer). `[speculation]` flag: the cross-field rhyme requires explicit work to state mathematically (a propagation-layer-only definition of "local rule with bounded-radius effective support" applicable to both classes); this work has not been done in the v3 syntheses.

### 2.2 Decision layer

**Restated claim.** *CALM-monotone decisions correspond to GW observables whose readout decoder requires no global aggregation. The canonical axial-charge readout sits in CALM's **excluded** class for the same structural reason monotone-counter-with-threshold sits in the excluded class.*

**Validator item mapping.**
- **V-5 (epsilon-local CALM extension).** **Direct, decisive kill.** V2's counterexample IS a decision-layer counterexample: the *join* operation (combining state from A and B) flips the decision non-monotonically. WRK-387's falsification is the same counterexample in physics vocabulary (instanton + antiinstanton in disjoint regions; each carries `Q_A = 0` locally, the union carries `Q_A = 1`). 16/21 personas endorse; Distributed systems persona (natural authority) calls it "the canonical monotone-extension trap" — the very mechanism CALM is designed to *exclude* such observables by.
- **V-3 (PCP-blindness lemma).** Also bears on the decision layer (PCP / IOP / zk-SNARK are certificate systems that *enable* local decisions about global properties; the lemma denying this contradicts the foundational result of TCS proof systems). Decisive on the decision layer.
- **V-1 (C_MPR coherence).** The `read` half of the `acc / read` factorization is precisely the decision-layer object. The validator critique applies most sharply here; C_MPR's `P_O` (protocol) component is undertheorized for the decision layer.
- **V-2 (BvN generalization).** Directly relevant: the Wall theorem says there is no 1-categorical adjunction between distributive (classical-decision) and orthomodular (quantum-decision) value lattices. Survives at the lattice-gauge-internal sub-class for decisions; fails at full generality.
- **V-4 (HLN universal lifting).** Lifting from axial to other quantum numbers is a decision-layer claim; "restrict to axial" concedes the layer.
- **V-6 (prior art).** Bohr-topos / CQM / convex-effect-algebra work has been at the decision-layer classification for 20+ years. The decision-layer bridge as posed in the v3 syntheses is largely a reinvention of known work in lattice-gauge notation.

**Verdict.** **BROKEN-IN-LAYER** — the decision-layer bridge claim, as stated in the v3 syntheses, is killed by V-3 and V-5 jointly, with the additional weight of V-2 restricting the Wall theorem to a sub-class and V-6 noting substantial prior art.

**Evidence weight.** Distributed-systems persona (high authority): "the classic monotone-extension trap, unfixable as stated." CRDT specialist (high authority): "PN-counter merge limitation, well-known." Cryptography persona (decisive on V-3): "the PCP-blindness lemma must be retracted in full." WRK-387's direct counterexample seals it.

**Partial repairs available** (at smaller scope, not rescuing the full claim):
- *Jordan-decomposed signed-CALM* (Statistics persona): split `Q_A` into `(Q_A^+, Q_A^-)` with monotone per-component propagation + non-monotone final subtraction; the subtraction requires coordination, which means the *decision* is still excluded but the *decomposition* is publishable as a TCS extension.
- *Exclusion-class reframe* (Distributed systems persona): publish the negative result — "GW axial charge sits in CALM's exclusion class for structural reasons identical to PN-counter-with-threshold."

### 2.3 Anomaly-class layer

**Restated claim.** The CALM-exclusion class on the CS side and the 't Hooft anomaly classification on the physics side are both *invariants of the classifying object*, not properties of individual observables. The bridge at this layer would say these two invariants exhibit structural correspondence.

**Validator item mapping.**
- **V-5 (epsilon-local CALM extension).** *Mis-targets* the anomaly-class layer. The anomaly is an invariant of the symmetry algebra; V-5's counterexample is at the observable level. The signed-cancellation pathology that V-5 observes IS *the very content* the anomaly classifies — that observation is the Anomaly theorist persona's load-bearing point in WRK-394. **V-5 does not kill the anomaly-class bridge; it's a different claim entirely.**
- **V-3 (PCP-blindness lemma).** Anomaly-class invariants ARE locally witnessable via index density (Chern density, anomaly density) — V1's Chern-number counterexample lands at this layer. The PCP-blindness lemma is wrong AT the anomaly-class layer in a specific way: anomaly density is exactly the kind of local-witnessable global invariant the lemma denies exists. **V-3 kills a claim that doesn't even apply to this layer correctly.**
- **V-1 (C_MPR coherence).** C_MPR doesn't have a clean anomaly-class element. The construction is a value-lattice / readout-decoder / provenance object; relocating the bridge to anomaly-class would require a *different* construction (e.g., Freed-Hopkins-style classification, or a CS-side classifying-topos object). The v3 syntheses do not provide this.
- **V-2 (BvN generalization).** The Wall theorem is about value-lattice adjunctions, not about anomaly classifications. **N/A at this layer.**
- **V-4 (HLN universal lifting).** Lifting between quantum numbers IS partly an anomaly-class question (different anomalies for different symmetries); the "restrict to axial" move is the right scope.
- **V-6 (prior art).** The Freed-Hopkins-Anomaly-Inflow literature, Dai-Freed pairing, and the Bohr-topos / CQM classifying-topos literature on the CS side are mature. An anomaly-class bridge is a *recategorification* exercise on top of two mature classification programs.

**Verdict.** **NOT-APPLICABLE as currently constructed** — the v3 syntheses do not formulate an anomaly-class layer bridge; the validator items do not bear on this layer because the layer is not actively populated. **Conditional HOLDS** if the bridge is *constructed* (Anomaly theorist persona's "repair-and-retry" recommendation): relocating the bridge from observable to anomaly-class would require new work, but the persona judgment is that such a bridge is constructively viable, with the signed-cancellation pathology becoming the content rather than the obstruction.

**Evidence weight.** Anomaly theorist (specialist authority): "relocate the bridge to anomaly-class level; this is publishable as 'we found the wrong target; here is the right one.'" Operator algebraist (concurring): the right home is Heunen-Reyes dagger-categorical work, also a classifying-object move. `[speculation]`: this is a new card's scope, not WRK-397's. Honest gatekeeper: do not claim HOLDS for a bridge that has not been constructed yet. The label NOT-APPLICABLE here means "the layer is real and well-defined, but the validators' kills don't reach a bridge that the v3 syntheses haven't built."

### 2.4 Coarse-graining layer

**Restated claim.** Coarse-graining-vs-local-rule non-commutation on the physics side (RG flow does not commute with local update at phase transitions) is the *same* obstruction as monotonicity-loss at projected readouts on the CS side. The Wall theorem may be a manifestation of this non-commutation rather than a 1-categorical no-go.

**Validator item mapping.**
- **V-5 (epsilon-local CALM extension).** *Partial relocation* — the Complexity-science persona reads V-5 as a *special case* of RG-non-commutation: the join operation is a coarse-graining (combining sub-region states into a unified state), and the readout is a projected order parameter. Coarse-grainings generically fail to commute with local rules at phase transitions; V-5's counterexample is the same phenomenon in distributed-systems vocabulary. **V-5 confirms the coarse-graining-layer claim** in the sense that "monotonicity-loss at projection" is exactly what the layer predicts; it does not falsify it, it instances it.
- **V-3 (PCP-blindness lemma).** RG flow loses micro-information; PCP-style proofs are about *recovering* global information from local certificates via algebraic compression. These are different mechanisms; **V-3 does not bear directly on the coarse-graining layer.**
- **V-1 (C_MPR coherence).** C_MPR's `acc / read` factorization is a coarse-graining structure (`acc` accrues micro-state; `read` projects to macro-observable). The validator critique that C_MPR needs more rigor applies; the coarse-graining-layer reframe gives the factorization a known mathematical home (RG / projection).
- **V-2 (BvN generalization).** The Wall theorem AS A COARSE-GRAINING STATEMENT: the no-go between distributive and orthomodular lattices is structurally identical to the no-go for commuting coarse-graining with local-rule application across a phase transition. `[speculation]`: this reframe is constructed-here; the Complexity persona's recommendation in WRK-394 is to relocate the Wall to "RG-non-commutation for chiral observables on classical substrates."
- **V-4 (HLN universal lifting).** Lifting between quantum numbers is partly a question of which coarse-grainings are RG-compatible. Not killed; restricted scope.
- **V-6 (prior art).** Wilson / Goldenfeld / Mehta-Schwab on RG; Crutchfield / Shalizi on computational-mechanics coarse-graining. Substantial prior art on the physics side; less mature on the CS side. The bridge would be a *new* connection between these two coarse-graining programs.

**Verdict.** **HOLDS [speculation]** — the coarse-graining-layer bridge survives the validator critiques because the validator critiques *instance* rather than *falsify* the predicted non-commutation. However, the claim as stated is partly constructed-here (`[speculation]` tags above) — the v3 syntheses did not articulate this layer, so "HOLDS" here means "the bridge is constructively viable and consistent with the validator findings," not "the bridge has been built and tested." This is the **second most repair-friendly layer** (after propagation).

**Evidence weight.** Complexity-science persona (specialist authority): "the Wall is structurally identical to non-commuting-square obstruction in RG flow." Wolfram-CA persona (concurring frame-shift): the CA-class reframe is adjacent. `[speculation]`: a substantive coarse-graining-layer bridge would need work to formalize the "RG-non-commutation for non-monotone observables" claim mathematically.

---

## 3. Cross-layer interaction map

The four layers are not independent. Three structural dependencies are load-bearing.

### 3.1 Propagation -> Decision dependency

The decision layer *consumes* the converged state from the propagation layer. A decision-layer claim presupposes that propagation has succeeded; you cannot evaluate a readout decoder on un-propagated state.

**Implication.** A propagation-layer-only bridge (the cleanest surviving claim) does not imply a decision-layer bridge. WRK-387's falsification shows that propagation-layer success is **necessary but not sufficient** for decision-layer success. The bridge therefore *factors* (in C_MPR's `acc / read` sense), but only the `acc` half survives.

`[speculation]`: this is also the right reading of CALM itself — CALM's coordination-freeness is a *combined* claim about propagation + decision; the WRK-387 finding shows the combination can break at the decision interface even when each half is well-behaved.

### 3.2 Decision -> Anomaly-class dependency

A decision-layer non-monotonicity is *evidence* of an anomaly-class invariant. The instanton + antiinstanton cancellation that breaks decision-layer monotonicity IS the anomaly content. The Anomaly theorist persona's claim is that the decision-layer "obstruction" is the anomaly-class "signal."

**Implication.** *Fixing the decision layer would erase the anomaly-class content.* This is the deep structural reason no Jordan-decomposed / signed-CALM repair fully rescues the v3 syntheses' original claim: any "repair" that makes the decision layer monotone would, by construction, remove the topological information the observable is supposed to carry. The decision-layer failure and the anomaly-class content are *the same phenomenon*, viewed from different layers.

**Cross-layer prediction.** If a decision-layer bridge ever succeeds (via Jordan decomposition, signed CRDTs, etc.), it will do so by *moving* the anomaly-class content into a separate witness (the sign / phase / index of the decomposition) rather than eliminating it. This is the "proof-carrying provenance" insight from the Cryptography persona in the six-persona dialectic.

### 3.3 Coarse-graining <-> all-other-layers (interaction, not strict dependency)

Coarse-graining is *orthogonal* to propagation / decision / anomaly-class in the sense that it operates on any of them. RG flow can be applied to propagation rules (block-spin renormalization of local updates), to decision functions (effective readout decoder at coarse scale), and to anomaly classes (anomaly matching across UV / IR).

**Implication.** A coarse-graining-layer bridge would *organize* the other three layers as a hierarchy: micro propagation -> micro decision -> micro anomaly invariants, with coarse-graining as the vertical projection. The Wall theorem as RG-non-commutation says: this hierarchy *does not commute* — coarse-graining a propagation rule and then taking the decision is *not* the same as taking the micro-decision and then coarse-graining it. This is exactly the structural feature the v3 syntheses were trying to capture but at the wrong categorical level.

### 3.4 Summary diagram

```
                Propagation layer
                       |
                       v
                  Decision layer  <----- V-3, V-5 KILLS HERE
                       |
                       v
              Anomaly-class layer  <---- decision failure IS the anomaly content

              Coarse-graining layer ---- orthogonal RG projection across the stack;
                                         the Wall may be its non-commutation signature
```

Independence claim: propagation can be assessed without the others (HOLDS verdict above). Decision *cannot* be assessed independently of propagation (presupposes converged state). Anomaly-class is *entangled* with decision (the failure mode IS the invariant content). Coarse-graining is a separate axis that *organizes* but does not strictly depend on the others.

---

## 4. Honest layer-by-layer verdict table

| Layer | Verdict | Validator items that hit this layer | Validator items that miss this layer | Repair scope |
|---|---|---|---|---|
| Propagation | **HOLDS** (as cross-field structural rhyme; smaller than v3 claimed) | (none directly) | V-3, V-5 (live at decision); V-2 (live at value-lattice) | None needed; engage cross-field-rhyme literature explicitly |
| Decision | **BROKEN-IN-LAYER** (V-3 + V-5 jointly decisive) | V-3 decisive, V-5 decisive, V-1 most relevant, V-2 restricts | (none) | Jordan-decomposed sub-scope (Statistics persona); exclusion-class reframe (Distributed systems) |
| Anomaly-class | **NOT-APPLICABLE as constructed** (the v3 syntheses do not build this bridge; layer is real but unpopulated) | V-3 indirectly (the lemma is wrong AT this layer in a different way) | V-2, V-5 (mis-target this layer) | Constructive: relocate bridge here (Anomaly theorist's repair-and-retry) — new card |
| Coarse-graining | **HOLDS [speculation]** (the validator findings *instance* rather than falsify the predicted non-commutation; bridge is constructively viable but not yet built) | V-2 reframable as non-commuting square; V-5 as RG-non-commutation special case | V-3 (different mechanism) | Constructive: formalize RG-non-commutation for non-monotone observables — new card |

**Compact summary.**
- **1 layer HOLDS as-is** (propagation, with smaller scope).
- **1 layer BROKEN-IN-LAYER** (decision, the canonical observable claim is dead).
- **1 layer NOT-APPLICABLE** (anomaly-class, the v3 syntheses do not populate it; constructive bridge is a separate effort).
- **1 layer HOLDS-with-construction-needed** (coarse-graining, structurally consistent with validator findings but requires new formalization).

**Honest reading.** The 5-persona signal in WRK-394 was correct: the bridge work conflated layers the literature keeps separate. Splitting reveals that **one layer survives intact** (propagation), **one layer dies cleanly** (decision), and **two layers are reframeable** as potential homes for a smaller-scope follow-on contribution. The bridge does NOT uniformly collapse, and it does NOT uniformly survive — the layer-split is the right grain.

---

## 5. What this changes (and what it does not)

**Changes.**
- The compact summary "the bridge fails" is too coarse; the compact summary "the bridge fails at the decision layer; the propagation-layer rhyme survives" is the right grain.
- WRK-393 publication-path lock (under separate reopen) should now consider: a single tightly-scoped paper at the *propagation-layer* level (cross-field structural-rhyme paper) + a separately-spawned future card on the *anomaly-class* or *coarse-graining* reframes.
- C_MPR's `acc / read` factorization is **vindicated as a structural move** — the `acc` (propagation) half survives the validator critiques and the `read` (decision) half is precisely what V-3 and V-5 kill. This is *evidence the factorization is doing real work* even though the full tuple needs more rigor.
- The Anomaly theorist's "repair-and-retry" recommendation in WRK-394 is **constructively well-defined**: relocating the bridge from observable to anomaly-class requires a new card to build the bridge there, not just to assess it.

**Does not change.**
- WRK-387's falsification of the *decision-layer* bridge stands. The layer-split does not rescue the original strong claim; it relocates the *surviving* claim to a different layer.
- WRK-394's meta-verdict (validators are partially right but missed structural issues B, C, D) stands. The layer-split exploration confirms issue B (layer conflation) is real and operationally split here.
- The CQM / Bohr-topos prior art issue (WRK-394 issue C) is not addressed by the layer-split. Even at the propagation layer, substantial prior art on CRDT and GW locality means the contribution is a cross-field rhyme, not a novel mathematical bridge.
- Publication path remains a separate decision; this exploration is *input* to WRK-393's reopen, not a publication recommendation.

---

## 6. What Joe walks at validation/4

A 6-item walkthrough (under 15 minutes target):

1. **Are the four-layer definitions correct?** Propagation / decision / anomaly-class / coarse-graining as defined in §1. Each has CS-side and physics-side anchors; the anchors are cited or `[speculation]`-tagged where the cross-field mapping is constructed-here.
2. **Is the layer-split a coherent decomposition?** Section 2 renders one verdict per layer. The 5-persona surfacing in WRK-394 (Anomaly, Network, Distributed systems, Sound, Complexity) is the convergent signal that motivated this exploration; the per-layer verdicts here either confirm or refute that signal.
3. **The per-layer verdicts:** propagation HOLDS, decision BROKEN-IN-LAYER, anomaly-class NOT-APPLICABLE-as-constructed, coarse-graining HOLDS-`[speculation]`. Does Joe agree with each, or push back on any?
4. **The cross-layer interaction map** (§3): propagation -> decision is a strict dependency; decision -> anomaly-class is an *entanglement* (the failure IS the content); coarse-graining is orthogonal projection across the stack. Does this match Joe's prior intuition or surprise him?
5. **What this changes for WRK-393:** the publication-path-lock should consider a single tightly-scoped propagation-layer paper rather than the 3-paper Option II companion set. Decision-layer paper is dead; anomaly-class and coarse-graining are *future* cards. Is this the right input to WRK-393's reopen?
6. **What this does NOT do:** validate bicategorical lift / CA-class frame / Jordan-decomposed signed-CALM (each is its own sibling card per WRK-397 card body). Honest scoping.

Joe's expected decisions at validation/4:
- A. Confirm layer definitions are usable (or push back; re-open).
- B. Confirm per-layer verdicts (or push back; re-explore specific layers).
- C. Confirm the cross-layer map (or push back).
- D. Decide whether to spawn follow-on cards for: (i) anomaly-class bridge construction (Anomaly theorist's repair-and-retry); (ii) coarse-graining bridge construction (Complexity persona's RG-non-commutation reframe); (iii) propagation-layer-only publication path (input to WRK-393 reopen).
- E. Confirm WRK-397 closure at validation/4.

---

## 7. Hard-rule receipts

- Zero writes to `Github Repos/` — confirmed; this artifact lives under `work/drafts/wrk-397-layer-split-exploration/`.
- Zero public push — confirmed; local-only artifact.
- Zero canon writes — confirmed; no `engine/canon/` mutations.
- Zero work.json edits — confirmed; advancement receipt below is appended to this artifact only.
- Joe-notes table cells untouched — confirmed; WRK-397 card body's Joe-notes row was not edited.
- `[speculation]` tagging — applied throughout where the cross-field mapping or layer-bridge construction is constructed-here rather than derived.
- Honest verdict per layer — applied; verdicts include HOLDS, BROKEN-IN-LAYER, NOT-APPLICABLE-as-constructed, and HOLDS-`[speculation]` rather than smuggling a single global verdict.
- PowerShell Move-Item for card moves — N/A at this point; advancement is via card frontmatter edit only (no file move out of `work/`).

---

## 8. v1 Advancement Receipt

**Card:** WORK-397-reputation-gu-layer-split-framing-exploration.md
**From:** implementation/1 + agent (just admitted)
**To:** validation/4 + joe + walkthrough_review
**Date:** 2026-05-31
**Worker:** dispatched WRK-397 single-pass agent
**Duration:** ~1 single dispatched pass (within ~300 min budget per card body)

**Definition of Done — receipts:**
1. ✓ Four layers defined precisely with literature anchors (§1.1–§1.4). Propagation: Demers et al. / Shapiro et al. / CALM-propagation-fragment / GW operator-locality / Lüscher 1998 / HJL 1999. Decision: FLP / Paxos / CALM-decision-fragment / lattice index theorem. Anomaly-class: 't Hooft / Freed-Hopkins / Dai-Freed / Atiyah-Singer / [speculation] for CS-side analogs (CQM, Bohr-topos, concurrency cohomology). Coarse-graining: Wilson / Kadanoff / Goldenfeld / Mehta-Schwab / [speculation] for CS-side analogs (epsilon-machines, tier-replication).
2. ✓ Bridge claim restated per layer + tested against validator findings (§2.1–§2.4). Each layer maps the six validator items (V-1 through V-6) to verdict and evidence.
3. ✓ Validator findings mapped to layers (§2 across all four sub-sections):
   - V-5 (epsilon-local CALM) → decision layer broken; propagation layer untouched; anomaly-class layer mis-targeted; coarse-graining layer instanced (not falsified).
   - V-3 (PCP-blindness) → decision layer broken; propagation layer untouched; anomaly-class layer mis-targeted differently; coarse-graining layer not directly relevant.
   - V-1 (C_MPR coherence) → cuts across; sharpest at decision layer; the `acc / read` factorization is structurally vindicated by the propagation-survives / decision-fails split.
   - V-2 (BvN generalization) → decision layer (Wall) restricted to sub-class; potentially reframable at coarse-graining layer as RG-non-commutation.
   - V-4 (HLN universal lifting) → "restrict to axial" applies across layers.
   - V-6 (prior art) → load-bearing at every layer; propagation has mature CRDT/gossip prior art; decision has CQM/Bohr-topos; anomaly-class has Freed-Hopkins; coarse-graining has Wilsonian RG.
4. ✓ Per-layer verdict rendered honestly (§2 closers + §4 table):
   - Propagation: **HOLDS** (as cross-field structural rhyme; smaller scope)
   - Decision: **BROKEN-IN-LAYER**
   - Anomaly-class: **NOT-APPLICABLE as currently constructed** (constructive bridge is future work)
   - Coarse-graining: **HOLDS [speculation]** (constructively viable; requires formalization)
5. ✓ Cross-layer interactions mapped (§3): propagation→decision strict dependency; decision↔anomaly-class entanglement (failure IS content); coarse-graining as orthogonal RG projection across the stack.

**Hard rules honored:**
- Zero writes to `Github Repos/`
- Zero public push
- Zero canon writes
- Zero work.json edits
- Joe-notes table cells untouched
- [speculation] tagging applied throughout

**Stage advancement (card frontmatter):**
- `stage: implementation` → `stage: validation`
- `sub_stage: 1` → `sub_stage: 4`
- `next_actor: agent` → `next_actor: joe`
- `review_reason:` (empty) → `review_reason: walkthrough_review`
- `verdict: open` (unchanged; this is exploration, not closure)
- `immediate_open: true` (unchanged)

**Next barrier:** Joe walks the per-layer verdicts + cross-layer interaction map; decides whether to spawn follow-on cards for (a) anomaly-class bridge construction, (b) coarse-graining bridge construction, (c) propagation-layer-only publication path as input to WRK-393 reopen; confirms or pushes back on each verdict; greenlights WRK-397 closure.

**Sibling work explicitly NOT done here:**
- Bicategorical lift assessment (separate card)
- CA-class frame assessment (separate card)
- Signed-CALM / Jordan repair assessment (separate card)

---

End of `layer-split-exploration.md` (v1).
