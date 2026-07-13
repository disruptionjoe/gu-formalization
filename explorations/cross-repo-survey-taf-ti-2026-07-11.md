# Cross-Repo Survey: time-as-finality (TaF) and temporal-issuance (TI)

Survey date: 2026-07-13 (filename per dispatch spec). Read-only survey of the two sibling
repos as input for a GU cross-repo synthesis. Grades below are the repos' OWN recorded
grades, carried with their caveats. Nothing here promotes any claim in any repo.

Standing cross-repo facts (ratified by Joe 2026-07-02, recorded in both repos):

- **Tri-repo division of labor:** TaF owns the *capability measure* (bounded-region
  capability object C(R), equality/screening-off certificates, region-indexed capability
  discriminator); **GU owns boundary content** (what the boundary must supply, in exact
  mathematics; the firewall-boundary attack); TI owns the *source question* (issuance vs
  disclosure; effect-typing `Issue[S]/Project[O]/Finalize[R]/Lose[K]`; the D-FORK).
- **Shared structural residue**, arrived at independently by all three: "A bounded system,
  complete and self-consistent in itself, provably cannot supply one specific thing from
  inside — and the missing thing lives at its boundary. The honest ledger for that boundary
  is what the region can do, not what it can see." TaF: read-vs-ignore moves zero process
  statistics (T395); capability profiles admit no scalar ranking (T407, finite-witness,
  partially absorbed by T398). GU: interior matter geometry is vectorlike; chirality /
  generation count enters as external boundary data. TI: an interior cannot precontain its
  own genuine extension.
- **The identity claim ("one object, three shadows") is explicitly NOT made.** Gated: no
  identity before at least two adapter contracts prove out. Current status recorded as
  "same shape, three independent arrivals, identity untested." Single-process caution is
  standing: all three repos are maintained by the same research process, so convergence is
  weak evidence; adapter tests are the only cure.
- **Verification-tier overlay** (cross-repo vocabulary): recorded / internally established /
  externally established. No internal step can reach tier 3.
- **One-way rule:** cross-repo material is stress-test input, never support. GU is never
  cited as evidence for TaF/TI claims and vice versa.

---

## Repo 1: time-as-finality (TaF)

`C:\Users\joe\JB\CapacityOS\repos\public\time-as-finality`

### North Star

Two-level. **Motivating intuition** (North Star - README): observers in recursively nested
structures; accessible worlds expand through stabilized records; time may correspond to
increasing finality within observer-accessible sections — explicitly "an aspirational
intuition, not a claim"; the math's job is to find which pieces survive. **v0.8 Maximal
Geometry Vision** (Vision - North Star.md): "Find the geometry whose shadows are physics.
Then prove it or break it." Layered target: `X^4` observed base + higher capability
structure `E→X` + bundles/connections/curvature/spin + records `R` + observer profile `O` +
observer-shadow projection `pi_O` + capability object `Cap_O`. Capability Projection
(projection sufficiency for typed capability objects) is the lead audit line; Time as
Finality is the lead line of attack (record stabilization + temporal direction). Candidate
theorem shape: `pi_O` is capability-sufficient exactly when it preserves the minimal
geometric data for transport, access, representation, boundary, record, and operation
structure. Empirical drift recorded in the North Star itself: away from a shared hidden
substrate, away from a privileged global object, toward observer-relative sections where
the *obstruction to global sections* is the most informative result.

### Main research lines

1. **FinaliEvent / temporal-reconstruction spine (C1, D1, D1-Field).** Project definition:
   for an embedded record-processing system, can a temporal partial order be reconstructed
   from the causal partial order and stabilization frontiers of accessible records? T48–T57
   build the finite event-finality partial-order program: FinaliEvent structures with
   record-dependency partial order and spacelike incomparability (T48); reconstruction
   without background time on a 2-axis (causal, info) order (T49); Axis Monotonicity
   Theorem (T50); multi-observer colimits with phantom incomparability (T51/T52);
   observer-colimit descent boundary — valid colimits do NOT determine a unique canonical
   completion (T53); Finite Finality Descent Theorem giving exact finite conditions
   (identity, overlap, record compatibility, profile agreement, definable maps, AM) for
   canonical reconstruction (T54, `poly_decider`); conflict-enriched descent (T55);
   apparent/event finality gap object `G(U)=A(U)−F(U)` and its Finality Reflection
   Property (T56/T57).
2. **Projection-Obstruction / typed-transport machinery (PO1, IPT, TTN, D1Cat,
   LossKernel).** The repo's most reusable formal layer: `D1RestrictionSystem` (finite
   graph-indexed restriction with projection, gluing, morphisms, T26); PO1 finite
   projection-obstruction schema extracted from T27, validated on hostile non-physics
   cases (Git, financial risk, translator/poet; chained projection with emergent
   obstruction — Spectre); PO1 compresses to a four-principle basis; CSP reframing — PO1
   gluing obstruction = binary {-1,1} parity-conflict CSP, with typed projection and
   admissibility as genuinely new structure beyond CSP (T39, `poly_decider` for the
   parity fragment); D1Cat is a proper category, PO1 is not a Boolean functor on it (T34);
   TypedTransportNetwork with path-dependent admissibility and LossKernel
   forgotten-structure annotation (T33/T73); Measurement Asymmetry (T45) and PO1-DAG
   (T47) theorems.
3. **Capability measure C(R) — the tri-repo leg.** T392/T393 equality-certificate and
   screening-off toolkit; T395 (read vs ignore moves zero process statistics); T407
   capability profiles admit no scalar ranking and are not determined by declared
   statistics (finite-witness; partially absorbed the next day by T398 at the
   resource-preorder level — carried caveat). Primary open problem:
   `open-problems/region-indexed-capability-discriminator.md` — a nontrivial task where
   crossing the boundary is *forced* by the physical/finality setup, not merely admitted.
   T399–T403 progressively cleared task-shape burdens but each was absorbed (enlarged
   state; joint-record completion; causal-domain completion; explicit finality-state
   completion). Remaining burden: a physically typed finality-lock substrate whose
   provisional/sealed state is not stipulated and survives fixed-accounting resource,
   provenance, control, and boundary absorbers.
4. **Arrow of time (H7) — weakened to conditional.** Paper-facing physical-arrow reading
   demoted (T148). Retained: finite constructor theorem (T18, D1-monotone admissibility
   induces acyclic direction) and the negative theorem T110. Open problem: physically
   typed deletion substrate clearing the fixed-accounting absorber gate; the E2
   computational-finality arrow attempt got a REDESIGN verdict (T419/T420, still open).
5. **S1 spacetime aggregation — narrowed; source-law search live.** The spacetime
   finite-colimit route was **killed by T223**. Current Track-1 frontier (T531–T537):
   source-law family search with hostile anti-target-import controls; T537 selected the
   `descent_obstruction_resolution_family` (source variables: local record cover,
   restriction maps, compatible local sections, descent obstruction witness, refinement
   steps, resolution depth) with a predeclared falsifier; ordering-fraction target-fit and
   Lorentzian-reference-import families explicitly BLOCKED as target import. A
   `stabilization_certificate_filtration_family` is held as REVIEW_ONLY (underdeclared).
6. **Quantum branch (Q1) — demoted; TWL active scaffold.** Q1 split into four branches
   (T101), all currently null/blocked/dormant: Q1A absorbed by provenance-aware Quantum
   Darwinism + Spectrum Broadcast Structure (bookkeeping_only); Q1B externally blocked
   (needs real signed pre-event detector manifest + event-level packet); Q1C dormant; Q1D
   guardrail. RSPS (record-stability pointer selection) is an active but modest fixed-H
   null-model boundary — explicitly NOT Born-rule or collapse evidence. **TWL**
   (three-wall nonlocality ladder, T514–T516, active): entanglement < 2-shareability <
   CGLMP nonlocality as three nested walls, reconstructed with one calibrated toolchain
   at d=2,3,4 — graded by the repo as executable **reconstruction of known QI** (Johnson–
   Viola shareability closed form, CGLMP thresholds, monogamy of nonlocality), not new
   physics; finality role is scaffolding for a monogamy↔quantum-secret-sharing strut.
7. **Distributed-systems finality crosswalk (A1, active).** Consensus finality collapse
   maps (T17), one verified proof-preserving theorem transfer with boundaries (T20),
   bounded impossibility witness for D1/progress finality tradeoffs (FLP/CAP-family,
   executable, bounded), open causal scarcity vs closed synchronization boundary (T46),
   Bell/CHSH local finality without global section (T21).

### Strongest results (repo's own grades)

Canon Index headline, verbatim in spirit: **"no top-line claim is a proven general
theorem."** The only `theorem_backed` results (COMPLEXITY-LEDGER, reconciled through T138):

- **T110 Finite-Permutation Monotone Obstruction** (`theorem_backed`, general but
  NEGATIVE): finite closed reversible dynamics cannot carry a strict scalar finality
  monotone (orbit argument; edgewise nondecrease on a finite cycle forces constancy).
  Sits under the *weakened* H7. Arguably the repo's single strongest result: general,
  proved, and load-bearing — it forces any finality arrow to be conditional, open-system,
  or coarse-grained.
- **T45 obstructed-source lemma + T47 PO1-DAG Theorem** (`theorem_backed`): PO1-admissible
  morphisms form an acyclic bipartite depth-≤1 graph between unobstructed and obstructed
  systems. Repo's own guardrail: "GENERAL but elementary" order-properties of the
  *partially-supported* PO1 schema, inheriting its ceiling, with "ZERO temporal or
  empirical content."
- **Finite-witness supported** (real evidence on 3–8-element hand-built witnesses, no
  general proof): the FinaliEvent spine's interesting temporal content — **Anti-Scalar
  result (T49/T50)** (no total preorder replicates a partial order with incomparable
  elements; AM is the exact condition for finality-axis dominance = record-dependency
  order) and **observer-colimit repair (T51/T52)** (bounded access produces phantom
  incomparability; colimit restores event finality). T54 descent theorem is
  `poly_decider` at finite scale.
- Repo-wide caveat carried verbatim: "Confirmed"/"supported"/"Theorem" in report titles
  almost always means **confirmed on a finite witness**, not a proven general theorem.

### Open hypotheses / live questions

- Region-indexed capability discriminator (primary open problem; see line 3).
- H5 spacetime aggregation: open formal target; post-T223, the source-law family search
  (T537 descent-obstruction family) is the live route.
- H6 phenomenal bridge formal-gap: is the first-person/third-person gap a *formal*
  obstruction (type/complexity/fixed-point)? Open target (T92 gives conditional finite
  restriction closure only).
- H7 conditional arrow: physically typed deletion substrate; E2 period-hardness redesign.
- TTN upward recovery propagation: once a cross-level morphism accumulates forgotten_dims,
  no defined operation detects downstream obstruction clearing — a known structural
  incompleteness of the transport formalism.
- Capability-boundary mode taxonomy (E0 declared / E1 asymptotic / E2 hardness / E3
  structural-symmetry) adopted as an organizing frame, not a claim; the first E3
  GU-adjacent adapter swing (T421) closed to a **logged disanalogy** (see GU hooks).
- Open-problem shelf directly relevant to synthesis: gap-presheaf classification,
  observer-shadow category, cross-domain shadow-protection theorem, finality as anomaly
  cancellation, finality gauge theory and gravity, finite-to-smooth shadow bridge,
  proof-carrying record finality, obstruction relocation / reconstruction debt.

### GU hooks recorded in TaF

1. **GU as hostile testbed, not claim promotion**
   (`explorations/gu-effect-typed-witness-transport-stress-test-2026-06-25.md`, verdict
   `USE_GU_AS_HOSTILE_TESTBED_NOT_TAF_CLAIM_PROMOTION`). Shared candidate object
   `EffectTypedWitnessTransport` with effect tags `Issue[S] / Project[O] / Finalize[R] /
   Lose[K]`. TaF→GU: IPT, TTN, RecordFinality, projection/obstruction discipline, ledgers.
   GU→TaF stressors: VZ actual-operator certificates, RS quotient, QFT Gram positivity,
   H-linear quotient loss, CHSH/readout gates. Explicit no-claim-movement rule.
2. **Reciprocal bridge contract**
   (`open-problems/gu-ti-taf-reciprocal-bridge-contract.md`): any future TaF/TI/GU bridge
   claim must supply a typed source object, GU six-axis table (L1–L6), same-neighbor-data
   freeze, H-fixed/H-growing split, and **double-diagram separation** — do not collapse
   TaF colimits and GU/TI filtrations into one construction; horizontal = observer-domain
   descent/gluing, vertical = record/source filtration. The named theorem-shaped target:
   `S : Compat_G^MLTT -> FiltSh(C)`, `R : FiltSh(C) -> ReadoutValues`, plus a witness
   where `R` depends on a transient `H^1(X, F_tau)` class not determined by the final
   sheaf alone. **This is the filtration↔section-map dependency GU's path-4/path-5 work
   records.** Also: no global commit order — finality/issuance language must stay local /
   cover-relative.
3. **Observerse notes (2026-07-10, Joe-direct, exploration grade).**
   `explorations/observerse-protocol-stack-2026-07-10.md`: collapse-prevention as a
   protocol STACK (Bitcoin analog) — issuance at `lambda*(s)`, finality-records as
   proof-of-work/Sybil resistance, admissibility as no-double-spend, consensus layer
   **identified with S1** (shared spacetime), difficulty adjustment, governance
   (meta-issuance), incentive alignment. Structural prediction: **SG4 (GU's unbuilt
   source action) is a protocol stack, not a term.** Re-reads the records-as-rows
   negative as "S1 can only emerge as one layer of the full stack, never alone."
   Companion predeclared model `observerse_issuance_dynamics.py`: 4/4 predictions
   (interior optimum lambda*, holonomy necessity, goal necessity, deflationary issuance)
   hold — graded **ILLUSTRATION, not validation**.
4. **E3 adapter swing T421 — logged disanalogy:** TaF operational recoverability and GU
   physics metric/grading selection "did not type-check as one functor." The tri-repo
   adapter contract remains gated; no GU/TI claim, identity, or support relation earned.
   (Recorded in Lead Research Line, 2026-07-02 frame section.)
5. **Sheaf/gluing/obstruction machinery** ready for GU pairing: T26 restriction systems,
   T16 finite gluing + obstruction witnesses for S1, T56 gap object `G=A−F`
   (restriction-closed in the tested model; automatic complement closure refuted;
   arrow-direction circularity open), T59 finite-to-infinite boundary audit (T39 parity
   criterion survives the Möbius boundary only as a transition-aware Z2 special case —
   a coefficient-blind scalar encoding produces a *false global section*), T53/T54
   descent conditions. H5 "partially supported as finite descent data, not full sheaf
   machinery" (T53) is the honest ceiling.
6. **Holonic / multi-scale structure:** Holarchy lab (T41: holonic emergence confirmed
   finite-witness; cross-level AC5 necessary for holonic PO1), TTN minimal multiscale
   transport (H1+ = TTN + CompressionRecord + EmergenceRecord as smallest justified
   formalism).
7. **CAP/FLP-style impossibility:** executable bounded theorem check for D1/progress
   finality tradeoffs (consensus-finality impossibility report), theorem-transfer test
   between consensus and physical record finality (T20), Bell/CHSH local-finality-
   without-global-section (T21). All bounded/finite-witness.
8. **Observer/record/filtration for GU's observer-structure results:** the whole D1-Field
   line (observer-indexed finality profiles, colimit descent, conflict descent) plus the
   T537 `stabilization_certificate_filtration_family` (REVIEW_ONLY) are the natural
   TaF-side partners for GU's filtration↔section machinery.

---

## Repo 2: temporal-issuance (TI)

`C:\Users\joe\JB\CapacityOS\repos\public\temporal-issuance`

### North Star

(NORTH-STAR.md, constitutional HYPOTHESIS.md vNext, approved by Joe, RUN-0038.) "Reality
is a shared, distributed, observer-participatory process that remains open-ended because
of ongoing issuance: the continual introduction of new possibility into the shared
process. Temporal order and finality are downstream observer-side reconstructions from
records." Organizing question moved from "Why does time flow?" to **"Why does reality
remain capable of producing genuinely new structure?"** Long-range physical target
(explicitly unearned, under adversarial pressure as TI-C019): whether issuance connects
non-circularly to energy, cosmological expansion, and structure formation. Layering:
shared process → issuance → energy/cosmology → observers → records → temporal
reconstruction. Explicit misreadings ruled out: not finality-first physics, not a
thermodynamic-arrow derivation, not causal-set growth renamed, not simulation theory, not
a hidden universal clock. The prior "monotone realization of constraint" framing survives
only as the downstream reconstruction layer (TI-C001, weakened).

### Main research lines

1. **The source question / D-FORK (TI-C019, formalizing — the program pivot).** Is
   issuance a property of reality itself, or of bounded observers receiving partial
   projections from a richer fixed structure? (PP-3, "the deepest unresolved fork in the
   program.") Sharpened to a single structural bit: is the operative source's effective
   type space **self-generating (Gödelian)** or **fixed-finite (FTS)**? TI-C019
   source-side issuance is TRUE iff Gödelian; it reduces to bounded projection disclosure
   iff finite. Primary discriminator target: expressiveness-threshold fixture — can the
   operative source encode its own admissibility predicate (Robinson-Q analog)? H8 work
   (E171) produced FTS/Gödelian *signature bundles* but explicitly is NOT a D-FORK
   decision procedure.
2. **OnlineIssuance^LC formalization (Lean 4).** The formal core of the source question:
   online constructibility with no-anticipation (NAA), diagonalization against present
   enumerators, and staged admissibility. E120 core encoding + E121 derivation swing
   (see strongest results). `Compat_G^MLTT` is the current strongest formal source
   candidate (crosses the expressiveness threshold as a formal staged-construction
   model; physical source question unresolved).
3. **Issuance measure mu (TI-C021, speculative but discriminated).** Subadditivity Axiom
   (SAX): mu strictly subadditive in realized structure size, distribution-free
   size-concavity — formally distinct and logically independent from Shannon/entropy
   subadditivity (E043 Disjoint-Independent Discriminator, both directions; standing
   entropy objection DEFEATED). Regime-pinned: SAX is the FTS-regime signature; Gödelian
   regime permits sustained marginal issuance. Companion: optimal issuance rate curve
   `lambda*(s) = argmax[N − C − K]`.
4. **Shared-process continuity / quorum legitimacy (TI-C022, speculative, survives).**
   A D4 event is genuine shared-process issuance iff its record propagates to a quorum
   within a *continuing valid shared process*. E044 Permanent-Fork Discriminator: a >f
   Byzantine fork (or eternal partition) satisfies BFT/TCB record integrity on each
   branch while neither satisfies the continuity condition — so TI-C022 = BFT integrity
   + a global continuity predicate BFT is silent about. Open: is that predicate just
   eventual-synchrony liveness restated?
5. **Physics bridges — mostly closed, honestly.** The energy-momentum route is doubly
   path-killed (BDO RUN-0028 + ICO RUN-0029 cover the full LorHist object-specification
   space; `Ext_S` invariants cannot reach `p^mu`); the conditional Lorentzian realization
   theorem (E008) is recorded as *formally sound with an unsatisfiable antecedent*;
   BMS/celestial route survives only conditionally on a new independently-specified
   boundary category `CelExt` (TI-C013/C016); holonomy is formal residue unless a
   C-typed admissibility predicate derives the transport functor A (TI-C012). The one
   explicitly UN-pressured energy route: **cost-of-finality (Landauer thermodynamics of
   record commitment)** — flagged as not covered by the BDO/ICO archive (E023 Idea 2,
   E140).
6. **Driving hypothesis: observer-level issuance** (DRIVING-HYPOTHESIS-OBSERVER-
   ISSUANCE.md — the explicit tri-repo integrator, incubated in TI with a spin-out
   trigger). Three-layer pipeline: (1) **GU layer** — fixed substrate/possibility-space
   observers access and project from but do not author; (2) **TI layer** — each observer
   a distinct local source with a *differential counterfactual repertoire*
   (bind/select, never author; not self-certifiable from inside, Gödel-type limit);
   (3) **TaF layer** — private bindings become shared facts via rising reversal cost
   across distinct holders; shared world = global section of finalized bindings,
   existing iff **Cech H1 of the finality sheaf vanishes**. H0 falsifiable spine: a
   single reversal-cost measure `mu` decomposable into thermodynamic (Landauer) +
   computational-irreducibility cost. `mu` is named "the central missing object."
   Framing discipline: coherent issuance, not a clock ("time is the commit log, not a
   column"); E097 absorber gauntlet found causal-order-alone does NOT absorb the
   clock-free cadence fixture, but fixed-site sheaf compatibility, fixed-H filtering,
   and fixed-latent-source-plus-changing-access DO — resurrection burden is nonfixed
   admissibility / site / observable algebra.
7. **Completion-barrier theorem target (frontier, 2026-07-12, E165–E175).** Repeated
   completion-absorption converted into a bounded, killable theorem target
   (`bounded_adapter_p_completion_barrier`): a candidate does not establish source
   issuance unless it supplies a new concrete H7-admitted packet defeating all completion
   channels (value, name, provenance/action, capability), the H6/H8 stops, and
   whole-family completion — with an explicit 10-obligation counterexample contract.
   Explicitly blocked overclaims: universal physical no-go NOT ready; physical source
   theorem blocked; D-FORK decision from H8 blocked.

### Strongest results (repo's own grades)

- **Kernel-checked Lean suite (E120/E121)** — the repo's strongest formal artifact and
  the tri-repo overlay's named strong sub-case of "internally established": G1 diagonal
  productivity (`diagName_not_mem`, zero hypotheses), G2 self-encoding admissibility
  (`issue_lc_all_derived` from the single hypothesis `EnumeratorPresent`, plus
  `no_universal_self_encoding` as a proved obstruction bound), G3 comparator
  (`diagSem_escapes`: no countable total Nat-indexed family internally indexes its own
  diagonal — derived, model-relative, axiom-free). No `sorry`, no axioms beyond
  propext/Classical.choice/Quot.sound; hostile RELOCATION verification applied. Caveat
  carried: proofs machine-verified; *modeling faithfulness remains internal*; formal NAA
  derivation does NOT establish source-side issuance (RUN-0045: constructive type theory
  partially absorbs online constructibility — contextual type formation supplies the
  no-reference rule).
- **Discriminator survivals** (claims stay `speculative` by the repo's own ledger):
  E043 SAX vs entropy (TI-C021 not absorbed — a genuine narrowing of the mu candidate
  space); E044 Permanent-Fork vs BFT/TCB (TI-C022 surplus identified precisely).
- **Strong negative results:** BDO+ICO double no-go on the `Ext_S`→energy-momentum route
  (TI-C009/C010 archived to NULL-SURVIVOR, with the recorded narrowness caveat that
  Landauer/cost-of-finality was never tested); W008/W009 bridge-tree verdict "current TI
  primitives do not derive physics" (TI-C015, archived); E097 absorber gauntlet on
  clock-free cadence; bare `<=_S` killed as an independent source primitive (TI-C006).
- Note the grade asymmetry: TI's positives are formal/conditional; its confident results
  are mostly kills and discriminators. The ledger's own required posture: generate the
  strongest surviving version, then attempt to destroy it.

### Open hypotheses / live questions

- **D-FORK** (Gödelian vs FTS) — the program pivot; expressiveness-threshold fixture is
  the named primary next artifact.
- **E119 retyped adapter burden (TI's tri-repo obligation):** find an `Ext_S` rule that
  changes a region-indexed observer task menu in a way TaF's capability-typed readout
  cannot express — **pre-committed to the archive branch** if every capability change is
  TaF-expressible boundary relocation.
- Cost-of-finality Landauer fixture (untested energy route; E140 opened it).
- TI-C022 continuity predicate: formalize as order-theoretic clock-free liveness; test
  reduction to eventual-synchrony liveness.
- TI-C020 (physical universe as OnlineSchemaSys): entirely unearned; requires the
  source/projection split first; holographic boundary theories flagged as the sharpest
  absorber.
- `mu` (driving-hypothesis H0): the central missing object — build it and H1 of the
  finality sheaf becomes computable and the idea gains a falsifier.
- Completion-barrier theorem: prove the bounded contract or admit a counterexample packet.

### GU hooks recorded in TI

1. **Tri-repo leg** (TRI-REPO-DIVISION-OF-LABOR.md): TI's `Issue[S]^LC`
   no-hidden-future-oracle condition = "the interior cannot precontain its own
   extension" — the TI face of the shared boundary residue whose GU face is
   vectorlike-interior/external chirality-count. One-way rule and identity gate as above.
2. **GU as method absorber, not claim source** (`absorbers/gu-formalization.md`): GU
   consulted for six-axis specification protocol, class-relative no-go map,
   specify-before-defend discipline, `R_fail`-style failure tensors. "Do not import GU
   claims into Temporal Issuance."
3. **Driving hypothesis layer 1 IS the GU layer:** the fixed
   substrate/possibility-space (task-space / richer substrate) observers project from
   but do not author. This is TI's most explicit structural slot for GU content — GU's
   arena/value and observer-structure results would instantiate the substrate layer of
   the three-layer pipeline, with TaF's Cech-H1 finality sheaf as layer 3.
4. **E080 effect-typed witness transport** (TI side of the TaF/GU bridge note) and
   **E007/RUN-0025 TI-GU mass-energy steelman** — the latter is the honest record of the
   killed `Ext_S`→GU→mass-energy route (BDO/ICO). Any GU synthesis reusing TI's
   extension-category residue should carry: extension categories provably carry
   non-order morphism invariants (formal advance), but with no earned physical
   mass-energy interpretation.
5. **Adapter_P work (E150–E152, E163, E167, frontier):** the D-FORK adapter no-go
   synthesis and completion-aware admission contract are the concrete gate any
   GU-sourced "physical issuance candidate" packet must pass; E172/E173 give the bounded
   theorem contract and counterexample obligations.
6. **Sheaf/gluing machinery in TI:** E054 Cech H3 fixture, E059–E061 filtered source
   functor Q and Ehresmannian bridge obligations, E143 Cech-H3 functor negative half —
   TI's own filtration→sheaf work feeding the same `FiltSh(C)` target named in TaF's
   reciprocal bridge contract.
7. **Issuance/admissibility concepts for GU:** SAX-constrained mu, the lambda* issuance
   curve, and TI-C022's quorum/continuity legitimacy predicate are the TI-native
   formal objects the Observerse protocol-stack notes (TaF side) map onto GU's SG4
   source-action slot.

---

## Synthesis-facing summary (what pairs with GU's arena/value + observer-structure work)

- **Formal structure of finality/irreversibility:** TaF's D1 profiles, FinaliEvent
  partial orders, Anti-Scalar theorem (no scalar time), and T110 (no scalar monotone in
  closed reversible dynamics) jointly say: finality is observer-indexed, componentwise,
  and only conditional arrows exist. Any GU pairing must respect the no-global-commit-
  order contract clause.
- **Observers/records/filtrations:** TaF descent conditions (T54) give the exact finite
  conditions under which multi-observer reconstruction is canonical; the bridge
  contract's `S: Compat_G^MLTT → FiltSh(C)` + transient-`H^1` witness is the agreed
  filtration↔section theorem target across all three repos.
- **Impossibility machinery:** TaF's bounded FLP/consensus crosswalk + PO1-DAG; TI's
  BDO/ICO no-go and diagonal-escape theorems — all bounded/model-relative by their own
  grading, none universal.
- **Holonic/multi-scale:** TaF holarchy lab + TTN (with the known upward-recovery gap);
  TI's per-observer issuance multiplicity; Observerse stack prediction that SG4 is a
  layered protocol stack with S1 as its consensus layer.
- **Grade discipline for the synthesis:** nothing above is externally established;
  strongest general theorems are TaF T110/T45/T47 (one negative, two elementary) and
  TI's axiom-free Lean diagonal suite (model-relative). Everything temporal-content-
  bearing is finite-witness. Identity claims across repos remain gated behind adapter
  contracts; the only adapter actually swung (T421, E3) logged a disanalogy.
