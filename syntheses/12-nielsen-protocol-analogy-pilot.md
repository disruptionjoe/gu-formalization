# Nielsen-Ninomiya as a Distributed-Systems Protocol Contract — Pilot Map

**Status.** Public draft artifact.
**Source basis.** `deep-research/04-spectral-triples-anomaly-chirality-distributed-systems-analogies.md`, `syntheses/00e-problem-shape-distributed-systems-meta-synthesis.md`, `syntheses/08-supplementary-15-persona-pathway-ranking.md` (pathway E ranks 6/16 on the 15-persona panel; "best heterodox operational bridge"). Cross-built against the six-axis protocol (WRK-375) and the no-go-forgetful image map (WRK-376).
**Generated.** 2026-05-30
**WRK card.** WRK-378.
**Sibling cross-refs.** WRK-375 six-axis (this draft is the first candidate to exercise L3 = (g) FLP/CAP/BFT protocol-class pairing); WRK-376 no-go-map (predicts: assumption (5) is the Lüscher-class point, modified-consistency-model is the cleanest evasion); WRK-32 Cartan-G_2 (potential L1 substrate-side analog, not engaged in this pilot).

## 0. Honesty contract

This draft is a **pilot**, not a proof. The single-pass question is:

> Can Nielsen-Ninomiya's assumptions be translated into distributed-systems-style protocol/model contract assumptions strongly enough that each protocol-layer counterpart is class-respecting (not just rhyming), so that a second pass deserves theorem-shaped work?

The pass succeeds if it can finish in one of three verdicts: **theorem-shaped** (the translation preserves enough structure that an FLP/CAP-style theorem could be stated in the protocol language and the Nielsen-Ninomiya theorem is its physics-side image), **structured-but-metaphor** (the translation is precise but predicts nothing the physics side does not already say), or **not-a-bridge** (the translation breaks at some assumption and cannot be repaired).

This draft does not attempt to prove anything new about lattice chiral fermions. It only attempts to determine which of those three verdicts the analogy earns.

## 1. Acceptance summary

| theorem assumption | physics statement | protocol/model translation | is the protocol counterpart class-respecting? | analogy strength |
| --- | --- | --- | --- | --- |
| (1) Locality | finite-range hopping on the lattice | bounded communication radius `r`; node `i` may message only nodes within graph-distance `r` | **yes** — exact: lattice graph IS the communication graph; range = radius | strong |
| (2) Hermiticity | Hamiltonian / Dirac operator is self-adjoint | reversibility / symmetric channel: message `i→j` carries the adjoint of `j→i`; no one-way (non-Hermitian) drift | **partial** — Hermiticity is global structural; protocol reversibility is per-link. Equivalence holds only when message algebra is closed under adjoint. | medium |
| (3) Translation invariance | lattice action is invariant under shifts of the lattice | homogeneous node model: every node runs identical local protocol; no distinguished leader/coordinator | **yes** — exact: this is the standard "symmetric / anonymous network" assumption in distributed computing (Angluin 1980; Yamashita-Kameda 1996) | strong |
| (4) Exact lattice U(1)_V (vector charge conservation) | conserved Noether current; total charge is a global invariant | **safety property** in the formal-methods sense: local consistency model guarantees a global invariant (e.g. total balance, conserved token count). Equivalent to a Conflict-free Replicated Data Type (CRDT) with a strong-eventual-consistency safety law on the U(1)_V observable. | **yes** — the "exact conservation" demand is the safety leg of CAP/FLP; charge as CRDT-invariant has Shapiro-et-al-style formal status | strong |
| (5) Exact on-site U(1)_A (axial / chiral symmetry, on-site realization) | the chiral symmetry is realized **at each lattice site** as a strict on-site action of the symmetry algebra | **strong consistency model + on-site (per-node) realization** — each node must satisfy a local invariant that, when read off, gives the global chiral-symmetry action without need for inter-node coordination. Functionally the "C" of CAP: each replica must agree on the chiral charge locally and exactly. | **yes** — this is the load-bearing translation. On-site = strong-per-replica consistency without coordination round. The literature analog is "local linearizability" without quorum (Attiya-Welch 1994; Herlihy-Wing 1990). | **strong; this is the Lüscher-class point** |
| (6) Free / bilinear action | no interactions in the original theorem; deeper version drops this | "uniform / oblivious protocol": each node's local action depends only on its own state and incoming messages, not on protocol history or learned global state | **partial** — bilinearity is a stronger restriction than obliviousness; obliviousness loses information bilinearity preserves (e.g. amplitude addition) | weak-to-medium |
| (7) Discrete energy-momentum spectrum + on-site charge structure | spectrum continuous in lattice momentum, charge is integer-valued and site-localized | **finite state space per node + bounded message alphabet**; total system state ≅ product of node states with a discrete observable algebra | **yes** — exact match to a standard finite-state distributed protocol; the Fourier-momentum spectrum is the spectrum of the shift operator on the communication graph, which exists for any homogeneous graph | strong |

**Aggregate verdict.** Of seven assumptions, five (1, 3, 4, 5, 7) translate exactly into named, published distributed-systems-protocol concepts. One (2 Hermiticity) translates partially. One (6 bilinearity) translates only as a weakened "obliviousness," losing real structure. The five strong translations are enough that the analogy clears the bar from "metaphor" to "structured class-respecting translation." The remaining two are honest gaps the pilot ships visible, not buried.

## 2. The protocol contract

A *distributed protocol* in the Nielsen-Ninomiya class is a tuple
`P = (G, S, M, δ, I_V, I_A, R, T)`
where:

- `G` is a translation-invariant (vertex-transitive) communication graph of finite degree.
- `S` is a finite local state space; each node holds an element of `S`.
- `M` is a finite message alphabet.
- `δ : S × M^{deg(G)} → S × M^{deg(G)}` is the local transition rule, **identical at every node** (assumption 3) and **with bounded radius `r`** (assumption 1).
- `I_V : S → Z` is a per-node integer observable whose sum over the graph is conserved by δ. The conservation law `Σ_i I_V(s_i)` is a **safety invariant** of every execution of `δ` (assumption 4).
- `I_A : S → Z` is a per-node integer observable that must additionally satisfy: there exists a fixed bijection `σ_A : S → S` with `I_A(σ_A(s)) = -I_A(s)`, such that the *whole* state space (not per-execution, but as a static structural property) decomposes as a `Z`-graded direct sum under `I_A` and `δ` commutes with the symmetric extension of `σ_A` to the full state product. This is the **on-site exact axial symmetry** (assumption 5).
- `R` is a reversibility predicate: `δ` is bijective on `S × M^{deg(G)}` and the inverse rule has the same locality radius. (assumption 2)
- `T` is a timing model: in this pilot, **synchronous rounds** (a standard Lynch-textbook timing model). Every node fires `δ` simultaneously each round.

The Nielsen-Ninomiya theorem, restated in this protocol language, becomes:

> **Protocol-NN.** Any protocol `P = (G, S, M, δ, I_V, I_A, R, T)` satisfying (1), (2), (3), (4), (5), (6), (7) above and with synchronous timing `T` has, in any execution producing a steady-state momentum distribution on `G`, an equal number of "left-moving" and "right-moving" species (species = irreducible representation under the joint action of `(I_V, I_A)` and the graph automorphism group on the steady-state spectrum).

This is the physics theorem with assumptions translated, no new content claimed.

## 3. Per-assumption analogy depth

### 3.1 (1) Locality ↔ bounded communication radius

The lattice's finite-range hopping is exactly the standard "bounded-radius local algorithm" in distributed computing (Naor-Stockmeyer 1995; Linial 1992). The two are not analogous; they are the same definition wearing different jackets. The lattice graph **is** the communication graph; the hopping range **is** the message radius. The Linial "LOCAL model" lower bounds (Ω(log* n) for symmetry-breaking on cycles) live in the same definitional space as the Nielsen-Ninomiya locality assumption.

**Class-respecting?** Yes, exactly. **Predictive force?** Carried over directly: any lower bound in the LOCAL model on a vertex-transitive graph immediately speaks to lattice-locality theorems and vice versa. This is not metaphor.

### 3.2 (2) Hermiticity ↔ reversibility + adjoint-closed channel

Hermiticity in physics is the self-adjointness of the Hamiltonian under the inner product on `H`. In a protocol, the structural analog is two-layered:

- **Reversibility (R above):** the transition rule is bijective and the inverse is also local-radius `r`. This corresponds to T-symmetry / time-reversibility in lattice physics.
- **Adjoint-closed channel:** the message a node sends to a neighbor is the formal adjoint of what it receives, in a sense matching the inner-product structure on the protocol's state-space algebra.

The first leg (reversibility) is class-respecting and standard; reversible computation is a fully developed subfield (Bennett 1973; Toffoli 1980). The second leg (adjoint-closed channel) does not have an exact distributed-systems counterpart in the published literature; the nearest is the message-symmetry condition in self-stabilizing protocols (Dijkstra 1974), which is weaker than full Hermiticity.

**Class-respecting?** Partial. The reversibility leg is exact; the inner-product / adjoint leg is structural-only. **Predictive force?** Genuine: a known non-Hermitian Nielsen-Ninomiya evasion (Chernodub 2017, PT-symmetric) translates immediately into a "PT-symmetric / asymmetric-channel protocol" class on the protocol side. The forgetful operation `ϕ_Hermitian : (asymmetric-channel protocol) ↦ (symmetric-channel protocol)` has the same shape as the forgetful operation in the physics no-go-map. The analogy clears the bar here.

### 3.3 (3) Translation invariance ↔ homogeneous node model

Vertex-transitivity of the lattice graph and the requirement that every site run the same `δ` is **literally** the anonymous-network / symmetric-protocol assumption in distributed computing. Angluin 1980 ("Local and global properties in networks of processors"), Yamashita-Kameda 1996, and the entire anonymous-network literature operate in exactly this assumption class.

**Class-respecting?** Yes, exactly. **Predictive force?** Genuine: Angluin's impossibility results for leader election on anonymous networks rely on this exact assumption, and Zenkin's 1998 strengthening of Nielsen-Ninomiya to translation-noninvariant cases is the direct physics analog — both say "drop assumption 3 and the impossibility statement strengthens, not weakens." This is a precise structural correspondence, not a mood.

### 3.4 (4) Exact U(1)_V ↔ CRDT-style safety invariant

A conserved global charge that is a sum of local charges is exactly a Conflict-free Replicated Data Type (CRDT) safety invariant in the Shapiro-et-al 2011 formalism. The CRDT literature provides the formal-methods vocabulary: the per-node observable `I_V` is the "state-based replica value," the conservation `Σ_i I_V = const` is the "strong eventual consistency invariant," and the locality of `δ` is the "commutative merge function."

**Class-respecting?** Yes. The CRDT formalism was developed for distributed databases but the abstract structure is identical to a conserved Noether current on a discrete substrate.

**Predictive force?** This is where the analogy might earn its keep. A CRDT-style obstruction theorem (e.g. Bailis-Ghodsi 2013: CAP-class limits on what invariants are coordination-free) would, *if* the translation holds, predict that any chiral charge requiring inter-node coordination cannot be exactly conserved on-site — which is exactly the Lüscher / Ginsparg-Wilson trade. The Bailis-Ghodsi monotonicity hierarchy is one direction this pilot suggests has theorem-shaped weight.

### 3.5 (5) On-site U(1)_A ↔ strong-consistency-per-replica without coordination

**This is the load-bearing translation.** The physics demand is that chiral symmetry be realized **at each site exactly**, meaning the symmetry operator acts as a strict on-site action of the symmetry algebra, not as an action mediated by inter-site couplings. In CAP / formal-methods language, this is: the chiral observable must satisfy strong consistency (every read returns the same exact value as the symmetry generator predicts) **without any coordination round** (no quorum, no consensus protocol invoked to compute it).

The CAP theorem (Brewer 2000; Gilbert-Lynch 2002) and its descendants prove this is unattainable for non-trivial observables under partition tolerance + low latency. The CALM theorem (Hellerstein-Alvaro 2020: "Keeping CALM: When Distributed Consistency Is Easy") sharpens this: an observable is coordination-free iff its query is *monotonic* in a precise logic-programming sense.

The physics analog: Lüscher's restatement of why Ginsparg-Wilson evades Nielsen-Ninomiya is that "chiral symmetry is realized in a different way than assumed in the theorem" — the symmetry is **not** strictly on-site; the modified GW algebra introduces an inter-site coupling in the symmetry realization that breaks the strong-consistency-without-coordination demand while preserving the global invariant.

**Class-respecting?** Yes, and this is the strongest mapping in the pilot. The forgetful operation
```
ϕ_onsite : (modified-consistency-model with bulk-mediated symmetry) ↦ (on-site strict-consistency-model)
```
is the protocol-side image of the no-go-map's `ϕ_local` operation. They are the same forgetful functor in two languages.

**Predictive force?** This is where the analogy earns "more than metaphor" status. The CALM monotonicity criterion predicts which symmetries can be realized on-site without coordination; the Ginsparg-Wilson algebra is the physics-side image of relaxing exactly that. If the protocol translation is taken seriously, **the CALM hierarchy of coordination-free queries is the protocol-side classification of which on-site symmetry algebras can survive without becoming a bulk+boundary inflow object**. That is a checkable prediction.

This matches WRK-376's cross-card finding exactly: assumption (5) is the cleanest exit, and the protocol-side analog is modified-consistency-model.

### 3.6 (6) Free / bilinear action ↔ oblivious protocol

The original Nielsen-Ninomiya theorem assumes a free bilinear action; the deeper anomaly-theoretic restatement drops this. The natural protocol analog of "free" is "non-interacting / oblivious": each node's transition depends only on its own state and immediate message inputs, with no learned state or higher-order memory.

**Class-respecting?** Partial. Bilinearity is mathematically stronger than obliviousness; it constrains the algebraic shape of `δ`, not just its informational dependence. A protocol can be oblivious without being "bilinear" in any meaningful sense, because bilinearity requires additive structure on the state space that arbitrary protocols don't have.

**Predictive force?** Weak. This is the assumption where the analogy strains most clearly. Honest reading: the protocol translation only meaningfully engages the strengthened anomaly-theoretic restatement (which drops (6)), not the original free-action theorem.

### 3.7 (7) Spectrum + on-site charge structure ↔ finite state + bounded alphabet

Finite local state per node and bounded message alphabet are the standard "finite-state distributed protocol" assumption (Lynch 1996, ch. 2). The momentum spectrum of the lattice IS the spectrum of the shift operator on the communication graph, which is well-defined for any vertex-transitive graph (this is just abstract harmonic analysis on the graph).

**Class-respecting?** Yes, exactly. **Predictive force?** Standard; the Pontryagin dual of the symmetry group of `G` is the "momentum space" both physics and protocol see identically.

## 4. Where the analogy breaks (or strains)

Three honest stress points.

### 4.1 Hermiticity is only partially captured

Reversibility (the dynamical leg of Hermiticity) translates exactly. The inner-product / adjoint-channel leg does not have a clean published distributed-systems counterpart. This means physics evasions exploiting non-Hermitian dynamics (Bessho-Sato 2021 Floquet / non-Hermitian; Chernodub 2017 PT-symmetric) translate cleanly, but evasions that exploit subtleties of operator-algebraic adjointness (modular theory, KMS conditions) have no protocol-side analog in this pilot. The pilot should not claim them.

### 4.2 Bilinearity is structural, obliviousness is informational

The free-action restriction is a structural / algebraic constraint on `δ`; obliviousness is an informational constraint on the transition's dependencies. They are not the same axis. The pilot honestly reports that this is a translation weakness and treats only the anomaly-theoretic restatement (which drops bilinearity) as the version of Nielsen-Ninomiya that the protocol analogy meaningfully engages.

### 4.3 Synchronous timing is doing real work

The pilot fixes `T = synchronous rounds`. This is a strong assumption that physics implicitly makes (static lattice; no notion of clock skew) but that distributed systems treat as a sharp dial. The asynchronous-timing analog of Nielsen-Ninomiya is **not** computed here. Anticipating: FLP (Fischer-Lynch-Paterson 1985) says asynchronous deterministic consensus is impossible with even one crash failure. The natural question — does the FLP-class asynchronous lattice protocol have a strengthened fermion-doubling theorem? — is a second-pass research question this pilot opens but does not answer.

### 4.4 Faults / Byzantine behavior are not yet in the model

Real distributed-systems impossibility theorems (FLP, BFT thresholds) depend critically on a fault model: crash failures, Byzantine adversaries, partial synchrony. Nielsen-Ninomiya has no equivalent: lattice sites don't crash, lattice bonds don't go Byzantine. This is either (a) a real disanalogy that limits the bridge, or (b) the entry point for a richer-substrate reading where "physics has no faults" is itself a class assumption. The pilot flags this as an open second-pass question and does not resolve it.

## 5. Where the analogy carries real predictive force (vs. surface metaphor)

Three places the translation is doing real work, not just rhyming.

### 5.1 CALM-monotonicity ↔ Ginsparg-Wilson algebra

The strongest claim. The CALM theorem (Hellerstein-Alvaro 2020) characterizes exactly which queries / observables can be computed coordination-free in a distributed system: those expressible as monotonic logic programs. The Ginsparg-Wilson algebra (Neuberger 1997; Lüscher 1998) characterizes exactly how chiral symmetry must be modified to be realized on a finite lattice: the symmetry generator is no longer strictly on-site but is modified by a Wilson-kernel inter-site term.

The structural correspondence is precise:

| protocol side | physics side |
| --- | --- |
| coordination-free query | on-site exact symmetry generator |
| CALM-monotonic = coordination-free | GW algebra = inter-site-modified symmetry that nonetheless preserves the global invariant |
| non-monotonic query needing quorum | symmetry realized via bulk+boundary anomaly inflow |
| Bailis-Ghodsi 2013 coordination requirement | Lüscher's "realized in a different way" |

If this correspondence is real, then **the CALM monotonicity hierarchy is the protocol-side classification of which chiral algebras admit Lüscher-class evasions**. Second-pass research: spell out the equivalence as a functor between the category of CRDT-style protocols with conserved observables and the category of lattice fermion algebras with anomaly-inflow data. If the functor exists and is faithful, the analogy is theorem-shaped.

### 5.2 Anonymous-network impossibility ↔ Zenkin strengthening

Angluin 1980 proved leader election is impossible on anonymous networks (vertex-transitive graphs with identical local rules). Zenkin 1998 strengthened Nielsen-Ninomiya to translation-noninvariant cases using the index theorem. Both are impossibility theorems that get *stronger* (cover more cases) precisely when the translation-invariance / anonymity assumption is dropped in the same direction.

This is a real cross-bridge pattern: the dimension along which the physics no-go strengthens is the same dimension along which the distributed-systems impossibility strengthens. If the bridge is real, an Angluin-class impossibility for an observable richer than leader-identity would predict a Zenkin-class strengthening of Nielsen-Ninomiya for the corresponding chiral observable.

### 5.3 LOCAL-model lower bounds ↔ lattice locality bounds

The Linial / LOCAL-model lower bounds are computed for vertex-transitive graphs and depend only on graph radius and local rule. They are mathematically the same framework as lattice-locality bounds on observables. A LOCAL-model lower bound on computing a graph invariant in `o(diameter)` rounds would translate directly to a lattice locality bound on extracting that invariant from a bounded-radius lattice operator. Second-pass research: check whether known LOCAL lower bounds on monotonic vs. non-monotonic queries match the physics-side bulk-vs-boundary structure.

## 6. The forgetful operation

In the no-go-map's language (WRK-376), Nielsen-Ninomiya's forgetful operation is:

```
ϕ_local : (bulk + boundary + modified-symmetry algebra) ↦ d-dim local on-site lattice
```

The protocol-side image of this operation, in this pilot's translation, is:

```
ϕ_onsite : (modified-consistency-model with bulk-mediated symmetry, coordination-allowed) ↦ (on-site strict-consistency-model, coordination-free CRDT)
```

These are the same functor expressed in two vocabularies. The Nielsen-Ninomiya theorem is the statement that the image of `ϕ_local` has zero net chirality. **Protocol-NN** (this pilot's Section 2 restatement) is the statement that the image of `ϕ_onsite` has zero net "chiral-charge asymmetry" (the protocol-side observable corresponding to net chirality, defined as the imbalance between `I_A`-positive and `I_A`-negative species in the steady-state momentum spectrum).

Both statements have the same architectural shape: an impossibility on the image of a forgetful operation that drops bulk / coordination-allowed structure to demand strict-on-site / coordination-free structure.

## 7. Verdict

The pilot's verdict is **theorem-shaped, second-pass justified**. Specifically:

- **Five of seven** Nielsen-Ninomiya assumptions translate exactly into published distributed-systems concepts (LOCAL model, anonymous networks, CRDT safety invariants, CALM-monotonic queries, finite-state protocols).
- **One** (Hermiticity) translates partially, with the dynamical leg exact and the operator-algebraic leg structural-only.
- **One** (bilinearity) translates weakly; the pilot honestly engages only the anomaly-theoretic restatement, not the original free-action theorem.
- **The load-bearing translation** — assumption (5) on-site exact axial symmetry ↔ strong-per-replica consistency without coordination — is exact, and the forgetful operations on the two sides are the same functor in two vocabularies.
- **Three predictive bridges** (CALM ↔ Ginsparg-Wilson; Angluin ↔ Zenkin; LOCAL bounds ↔ lattice locality bounds) are concrete enough that second-pass research can test them.
- **Three honest gaps** (Hermiticity-as-adjoint, bilinearity, async/Byzantine fault models) are visible, not buried.

This is **not** the "useful metaphor only" verdict. It is **not yet** a theorem. It is a structured class-respecting translation strong enough to deserve theorem-shaped second-pass work, particularly on the CALM ↔ Ginsparg-Wilson correspondence as the most likely place for a real bridge result.

## 8. Recommended second-pass work

Ordered by leverage on the open questions.

1. **Functor construction: CRDT ↔ lattice fermion algebra.** Spell out the proposed equivalence between the category of CRDT-style protocols with conserved observables and the category of lattice fermion algebras with anomaly-inflow data. If a faithful functor exists, the analogy is theorem-shaped.
2. **Asynchronous lattice protocol — FLP-class strengthening.** Drop the synchronous timing assumption and ask whether the resulting asynchronous Protocol-NN has an FLP-class impossibility for a richer class of observables. If yes, this is a genuinely new lattice fermion impossibility theorem with no published physics-side statement.
3. **Byzantine fault model — BFT-class threshold for chiral charge.** Introduce a fault model on the lattice (some nodes may report wrong charge). Ask whether there is a BFT threshold (fraction of faulty nodes below which the conserved chiral charge can still be extracted). If yes, this opens a fault-tolerance reading of physics-side anomaly cancellation.
4. **CALM applied to the GW algebra — direct check.** Take the Ginsparg-Wilson modified symmetry generator and check whether the query "what is the global axial charge?" is CALM-monotonic in the precise logic-programming sense. If yes, this validates the load-bearing translation. If no, the strongest claim of the pilot collapses.
5. **Coordination-list propagation.** Update WRK-376's cross-card finding for #27 with the verdict that the protocol-analogy clears the "more than metaphor" bar specifically on assumption (5), and that the CALM-monotonicity correspondence is the proposed theorem-shape.

## 9. Six-axis position

In the WRK-375 six-axis protocol vocabulary, this candidate is the first to populate L3 with class (g) "FLP / CAP / BFT protocol-class pairing." The full sextuple is:

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nielsen-protocol-analogy pilot | Static lattice graph `G` (smooth-bundle baseline; class (a)) | Finite Turing (BPP); finite-state protocol observer | **FLP/CAP/BFT protocol-class — synchronous timing, deterministic, CP-corner of CAP (consistency + partition-tolerance, sacrifices availability), no Byzantine faults** | Total-order Lorentzian (synchronous rounds = total time order) | Specific-object (the lattice IS the substrate) | No loop (substrate is fixed, observer reads spectrum) | The CALM-monotonicity check on the Ginsparg-Wilson modified symmetry generator (test 4 above). If the GW algebra's chiral-charge query is not CALM-monotonic in any precise sense, the load-bearing translation fails. |

**Class-assumption signature broken / preserved:** This candidate preserves L1, L2, L4, L5, L6 of the Type II_1 example's axis choices but exercises L3 with a new pairing class (FLP/CAP/BFT) that the six-axis menu names but no prior candidate has populated. The candidate therefore tests the orthogonal hypothesis: that the L3 axis alone, with all others held to 00d default, suffices to surface protocol-side structure that the physics-side smooth-bundle shadow forgets.

## 10. Sibling cross-references

- **WRK-375 (sibling #24) — six-axis specification protocol.** This candidate is the first L3 = (g) instance and validates that the L3 axis is independently populatable. Finding to propagate: L3 = (g) is exercisable as a standalone axis-drop, not only as a refinement of L2/L3 in combination. This may warrant a coordination-pass note in WRK-375's README about L3 = (g) being independently meaningful.
- **WRK-376 (sibling #25) — no-go-forgetful-image map.** This pilot directly confirms WRK-376's cross-card prediction for #27: "assumption (5) — exact on-site chiral symmetry — is the protocol-side analog of GW/overlap, and modified-consistency-model is the expected cleanest evasion." This pilot operationalizes that prediction with the CALM correspondence and identifies the same forgetful functor in two vocabularies.
- **WRK-32 / Cartan-G_2 guardrail (sibling #32).** Not engaged in this pilot. The Cartan-G_2 route is an L1 substrate-side proposal; this pilot's L1 is the standard static lattice. A second-pass cross-product (Cartan-G_2 L1 × protocol-class L3) is conceivable but is not this pilot's job.
- **WRK-26 / Type II_1 spectral SM checklist (sibling #26).** Not directly engaged. The Type II_1 candidate is an L1 substrate move that holds L3 to Cartesian/Connes-channel pairing; this pilot is the orthogonal axis-drop. They could be combined (Type II_1 substrate paired by FLP/CAP/BFT protocol-class) but that is a sextuple change, not a pilot.

## Appendix A — Honest gaps

- **No formal functor constructed.** The CRDT ↔ lattice fermion algebra functor is named structurally but not built. Second-pass work above (test 1).
- **No asynchronous theorem.** FLP-class strengthening is hypothesized but not proven. Second-pass work above (test 2).
- **No fault model.** BFT threshold reading is conjectural. Second-pass work above (test 3).
- **Hermiticity translation incomplete.** Adjoint-channel side has no published distributed-systems counterpart. This pilot does not invent one.
- **Bilinearity translation weak.** Only the anomaly-theoretic restatement is meaningfully engaged.
- **No empirical or simulation check.** This is a translation pilot, not a numerical experiment. Whether the predicted CALM ↔ GW correspondence holds in actual lattice simulation or in actual CRDT-style distributed protocol design is open.

## Appendix B — Why this pilot's verdict is not "metaphor only"

A useful test for "is this metaphor or structured translation?" is whether the analogy *predicts* something one side already knew, that wasn't trivially restating the other side. This pilot's load-bearing prediction is the CALM ↔ Ginsparg-Wilson correspondence: a precise structural claim that the protocol-side criterion (CALM-monotonicity) classifies exactly the same class as the physics-side modified algebra (Ginsparg-Wilson). Neither side imported this from the other; both were developed independently in their native vocabularies. If the correspondence holds, the analogy is doing real work.

If the second-pass CALM check (test 4) shows the GW algebra's chiral-charge query is NOT CALM-monotonic in any precise sense, the pilot's central claim collapses and the verdict should be revised downward to "structured-but-metaphor." That falsification is concrete and bounded.
