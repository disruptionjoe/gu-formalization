---
title: "The Signed-Readout Boundary Theorem: A Consolidated Account"
status: active_research
doc_type: synthesis
updated_at: "2026-06-20"
---

# The Signed-Readout Boundary Theorem: A Consolidated Account

This document consolidates the signed-readout boundary theorem line into a single,
self-contained account for an external reader. It states the problem, gives the
definitions cleanly, proves the result that survives, and is explicit about the
stronger result that was attempted and failed. The honest verdict is preserved:
this work establishes a precise *factorization* boundary, not the anomaly
equivalence it originally set out to prove.

---

## 1. The question

The broader project asks whether no-go theorems that forbid chiral structure are
genuinely universal, or whether they only fix a *class* of admissible substrates
and forget richer data when they project a richer object down to a smooth-bundle
shadow. One of those no-go theorems — Nielsen-Ninomiya, on the doubling of lattice
fermions — has a striking structural resemblance to a result in distributed
computing: the CALM theorem (*Consistency As Logical Monotonicity*,
Hellerstein-Alvaro 2020), which characterizes exactly which queries a distributed
system can compute without coordination. CALM says a query is coordination-free
if and only if it is *monotone* in a precise sense: adding more input can only
add to the answer, never retract it.

The signed-readout line started from a specific, falsifiable conjecture about that
resemblance:

> **(Anomaly-iff conjecture, original form.)** A lattice observable lies in the
> coordination-free / monotone (CALM-extension) class **if and only if** it
> carries no 't Hooft anomaly.

If true, this would have been a clean dictionary entry: *anomaly = coordination
obstruction*. Anomaly cancellation — a physics condition — would have been shown
equivalent to a monotonicity criterion — a computer-science condition — for the
canonical chirality-bearing observable on a lattice.

The conjecture is **false as an iff**. What this document records is (i) why it
failed, (ii) the weaker but rigorous criterion that replaced it, and (iii) what
that replacement actually buys. The central object that survives is a
*factorization* of any lattice observable into a monotone provenance layer and a
possibly-signed readout layer, with monotonicity decided entirely at the readout
layer. We call the resulting boundary result the **signed-readout boundary
theorem**.

The reader is assumed to know some lattice gauge theory (the axial charge, the
index theorem, Ginsparg-Wilson fermions) and some distributed-systems vocabulary
(replicas, coordination-freedom, CRDTs), but is *not* assumed to have read any
other document in this repository. Everything needed is defined below.

---

## 2. Definitions

### 2.1 Setting

Fix a vertex-transitive communication graph `G = (V, E)` of finite degree with
graph metric `d`; physically this is the lattice, computationally it is the
network of replicas. A **query** `Q` maps a distributed input multiset (one input
tuple per site) to a scalar. The input carries an **information order**: `I ⊆ I'`
means `I'` has at least as much evidence as `I`. A query is **monotone** (in the
CALM sense) if `I ⊆ I'` implies `Q(I) ≤ Q(I')`; CALM identifies monotone queries
with the coordination-free ones.

### 2.2 The evidence monoid and the signed readout

The cleanest statement of the surviving result is stated in two layers.

**Definition (evidence monoid).** Let `E` be the free commutative monoid generated
by local contribution events, equipped with the information order
`e ≤ e'  iff  e' = e + d` for some `d ∈ E`. The order says only that new evidence
has arrived; `E` is append-only by construction and accumulation in `E` is always
monotone.

**Definition (signed readout).** Let `G` be an ordered abelian group with positive
cone `G₊`. Assign each generator `x` a weight `w(x) ∈ G` and define the scalar
readout
```
R( Σᵢ xᵢ ) = Σᵢ w(xᵢ).
```
This is the map from accumulated evidence to the reported scalar. The readout is
*signed* precisely when some weights lie outside `G₊`.

### 2.3 Jordan-decomposed signed-CALM (JD-CALM)

The physically natural way to keep a signed observable inside a monotone framework
is to split it by sign and accumulate each sign separately — the bounded-variation
generalization of the PN-counter CRDT (two grow-only counters `P`, `N`, value
`P − N`; Shapiro et al. 2011).

**Definition (JD-CALM).** A signed real-valued aggregate `Q` is **JD-CALM** iff
there exist `Q⁺, Q⁻ : 2^Inputs → ℝ₊` such that

- **(J1) Decomposition.** `Q(I) = Q⁺(I) − Q⁻(I)` for every input set `I`.
- **(J2) Per-component monotonicity.** Each of `Q⁺`, `Q⁻` is standard-CALM-monotone
  over the non-negative-real aggregate semilattice `(ℝ₊, +, ≤)`; i.e. `I ⊆ I'`
  implies `Q⁺(I) ≤ Q⁺(I')` and `Q⁻(I) ≤ Q⁻(I')`.
- **(J3) Local sign classification (Jordan-admissibility).** The decomposition
  exists and is unique up to the usual Jordan-Hahn ambiguity (resolved by taking
  `Q⁺`, `Q⁻` mutually singular), and the per-site sign rule
  `sign : site × inputs → {+, −}` is computable from local data without
  coordination.
- **(J4) Readout.** The final scalar is `Q(I) = Q⁺(I) − Q⁻(I)`: two independent
  monotone aggregations followed by a subtraction performed only at read time.

The key feature of JD-CALM is that the *propagation* of `Q⁺` and of `Q⁻` is each
coordination-free; coordination is needed only in the trivial sense that the read
site must wait for both aggregates to settle before subtracting. There is no
inter-site coordination during propagation.

### 2.4 Approximate-consistency CALM (AC-CALM)

A second, complementary repair keeps the readout real-valued but truncates
influence at a finite radius and carries an explicit error bound — the
deterministic-decay analog of probabilistically-bounded staleness (Bailis et al.
2012).

**Definition (AC-CALM).** A query `Q` over an influence-weight-bounded input is
**AC-CALM** iff there is a family `{Q_r}_{r ≥ 0}` with

- **(B1) Metric-cointegration bound.** `|Q(x,I) − Q_r(x,I)| ≤ ε(r)`, where `ε(r)`
  is the integrated tail of an exponentially-decaying influence weight beyond
  radius `r`. For the Ginsparg-Wilson kernel (locality scale `(a, γ)`,
  Hernández-Jansen-Lüscher 1999) this is `ε(r) = (C' a / γ) · exp(−γ r / a)`.
- **(B2) Per-radius monotonicity.** Each fixed-`r` truncated query `Q_r` is a
  standard bounded-radius CALM-monotone aggregate.
- **(B3) Bounded replica disagreement.** Two replicas computing `Q_r` at the same
  `r` agree exactly; two replicas computing the full `Q` agree up to `2 ε(r)`.
- **(B4) Tunable tolerance.** Choosing `r ≥ (a/γ) log( C' a / (γ ε_target) )` hits
  any target tolerance `ε_target`.

AC-CALM has no rounding step, so it never incurs the integer-rounding
non-linearity discussed in §4.

---

## 3. The theorem

### 3.1 The signed-readout monotonicity criterion

The primitive result is elementary and exact.

> **Theorem (Signed-Readout Monotonicity Criterion).** With `E`, `G`, `R` as in
> §2.2, the readout `R : E → G` is monotone with respect to the information order
> if and only if every generator has non-negative weight:
> `R` is monotone  ⇔  `w(x) ∈ G₊` for every generator `x`.

**Proof sketch.** If every weight lies in `G₊`, then passing from `e` to
`e' = e + d` adds `R(d) ∈ G₊`, so `R(e') ≥ R(e)`; the readout cannot decrease.
Conversely, if some generator `x` has `w(x) ∉ G₊`, take `e = 0` and `e' = x`. Then
`e ≤ e'` but `R(e') = w(x)` is not `≥ R(0) = 0`, so monotonicity fails. ∎

Trivial as it is, this criterion is the load-bearing statement: it locates the
entire monotonicity question at the *sign structure of the readout weights*, and
nowhere else.

### 3.2 The factorization boundary theorem

Lifting the criterion onto the lattice substrate gives the result the project
actually stands behind.

> **Theorem (Signed-Readout Boundary / Factorization-Iff Theorem).** Let `Q` be a
> lattice observable on a bounded-degree-graph Ginsparg-Wilson substrate. Then `Q`
> factors as `Q = read ∘ acc`, where
>
> - `acc : inputs → E` is the **monotone-provenance accumulator**: a per-site,
>   bounded-radius, locally-computable, append-only map into the evidence monoid
>   `E`; and
> - `read : E → G` is a fixed **scalar readout** into an ordered abelian group
>   `G` with positive cone `G₊`.
>
> This factorization exists for **every** such observable. The composite `Q` is
> CALM-extension monotone **if and only if** every generator-weight of `read`
> lies in `G₊` — i.e. iff the readout has no negative-weight contributions.
>
> *Physical sub-statement.* For `Q` a conserved charge of a global internal
> continuous symmetry, the canonical mechanism producing negative-weight
> generators is topological-index / 't Hooft-anomaly structure — via the
> Hasenfratz-Laliena-Niedermayer (1998) lattice index theorem for axial-type
> charges, and Atiyah-Patodi-Singer-type index theorems on curved substrates.
> Within this restricted sub-class, "no negative-weight generators" coincides with
> "anomaly-free."

**What the theorem gives you.** Three things, in decreasing generality:

1. *A universal factorization.* Any lattice observable splits into a monotone,
   coordination-free provenance layer and a fixed scalar decode. The provenance
   layer is always CALM-clean; whatever obstruction exists lives entirely in the
   decode. This is unconditional.

2. *A sharp monotonicity criterion.* Coordination-freedom of the composite is
   decided by a single, checkable condition on the readout: are all generator
   weights non-negative? This is exact, not approximate.

3. *A physical reading, but only as a corollary in a sub-class.* For the
   restricted family of internal-Noether charges on the lattice, anomaly/index
   structure is the dominant source of negative weights, so anomaly-freeness is
   *sufficient* (within that family) for monotonicity. It is **not** the iff
   condition in general — see §4.

The original doubly-restricted conjecture (abelian internal symmetry, axial charge
only) is recovered as the special case where physical-anomaly content and
readout-sign content happen to coincide. Outside that case they decouple, and the
correct invariant is the readout sign, not the anomaly.

---

## 4. What failed, and why

The intellectually important part of this line is the failure. It should not be
softened.

### 4.1 The claim that broke

The original ambition was the **anomaly-iff**: monotone/coordination-free
membership *iff* anomaly-freeness. This direction fails in **both** halves.

**Anomaly-freeness is not sufficient.** An anomaly-free observable can still have a
signed readout and therefore be non-monotone. Concrete examples:

- non-abelian vector charges with traceless generators (`Q^a_V = Σ λᵢ nᵢ` with
  mixed-sign `λᵢ`), which are anomaly-free but signed;
- a U(1) charge whose modeled state space includes both positive and negative
  charge sectors;
- any conserved quantity whose readout is a *difference* rather than a count.

So `anomaly-free ⇒ monotone` is false unless one separately imposes that all
readout generators are non-negative — at which point the anomaly hypothesis is
doing no work.

**Anomaly is not necessary.** Signed cancellation, and hence non-monotonicity,
arises without any anomaly at all: signed measures, phase-sensitive amplitudes,
positive-minus-negative bounded variation. So `non-monotone ⇒ anomalous` is false
too.

Both directions of the iff therefore fail. Anomaly is one *mechanism* — an
important and physically canonical one — that produces negative-weight generators
in the lattice-gauge sub-class. It is neither the only such mechanism nor a
sufficient one.

### 4.2 The two counterexamples that killed it

Two distinct failure modes broke the naive criterion, and the repair has to handle
both.

**(a) Signed cancellation under input growth.** Take the Ginsparg-Wilson axial
charge `Q_A = index(D) = n₊ − n₋`. Place an instanton (charge `+1`); the readout is
`1`. Now add an *anti-instanton* far away. The input set has strictly grown, yet
the signed readout *decreases* to `0`. A strictly larger input produced a strictly
smaller answer — a flat violation of monotonicity. This is the signature failure of
treating a signed index as a monotone aggregate.

**(b) Truncation-rounding non-linearity at disjoint supports.** Partition the
lattice into disjoint regions `A` and `B`. Choose configurations whose per-region,
truncated contributions each fall below an integer-rounding threshold, so the
truncated readout reports `Q_ε(A) = Q_ε(B) = 0`, while their union's cumulative
tails cross the threshold and report `Q_ε(A ∪ B) = 1`. The join of two zeros is
`1`: the integer-rounding step destroys the linearity of the join
(`Q_ε(A) ∨ Q_ε(B) = 0 < 1`). This failure is about the *rounding to an integer
index*, not about sign cancellation.

### 4.3 Why the pivot to monotonicity-via-factorization was the right move

JD-CALM (§2.3) exactly resolves failure **(a)**. Adding the distant anti-instanton
grows `Q⁻` by roughly one unit while `Q⁺` is essentially unchanged; both components
grow monotonically, and the signed difference `Q⁺ − Q⁻` is *allowed* to decrease.
Under JD-CALM the instanton/anti-instanton kill is reclassified from "monotonicity
violation" to "expected behavior of a Jordan-decomposed signed aggregate" —
precisely as a PN-counter's value may fall while both of its counters only rise.
This is the structural win: signed-cancellation observables are correctly typed as
*monotone-provenance, non-monotone-readout*, rather than as "non-CALM, full stop."

JD-CALM does **not**, by itself, resolve failure **(b)** when the target is the
integer index. If the readout includes a rounding step `round_ε : ℝ → ℤ`, that step
is orthogonal to the per-sign split, and the disjoint-support violation survives at
the readout level. AC-CALM (§2.4) addresses **(b)** by *abandoning the integer
readout*: it reports a real-valued aggregate with an explicit `ε(r)` bound and no
rounding, so there is no non-linearity to break.

The honest consequence is a **layer split**, and it is the heart of the verdict:

- At the **signed-real-valued readout layer**, the bridge **recovers** under both
  JD-CALM and AC-CALM.
- At the **integer topological-index readout layer**, the bridge **does not
  recover** under any framework tested — integer recovery demands either an
  unbounded `r → ∞` truncation (outside bounded-radius CALM) or a non-CALM rounding
  step.

The pivot — from "anomaly cancellation ⇔ monotonicity" to "every observable
factors through a monotone provenance layer; monotonicity is decided by readout
sign; the signed-real bridge survives and the integer-index bridge does not" — is
the right move because it is *exactly as strong as the evidence supports and no
stronger*. It keeps the real structural insight (the provenance/readout split) and
drops the overclaim (the anomaly equivalence).

---

## 5. Bridge tests

Two independent tests probe whether the surviving criterion actually connects to
the physics it was meant to model.

### 5.1 Ginsparg-Wilson boundary test

The Ginsparg-Wilson axial-charge density `q_A(x) = ψ̄_x γ₅ (1 − a R D)_{xx} ψ_x` is
a signed real number whose sign at each site is a local function of the gauge field
in an exponentially-decaying neighborhood. Two distinct decompositions are in play,
and keeping them apart is the whole game:

- **Local pointwise Jordan split** `q_A(x) = q⁺(x) − q⁻(x)` with
  `q⁺ = max(q_A, 0)`, `q⁻ = max(−q_A, 0)`. Sign classification is local, so this
  maps cleanly to a coordination-free protocol: accumulate `Σ q⁺` and `Σ q⁻`,
  report the difference.
- **Global chirality counts** `(n₊, n₋)`, the dimensions of the positive- and
  negative-chirality zero-mode spaces. These are global topological invariants and
  do **not** map to a coordination-free protocol: deciding which zero mode a site
  belongs to needs global wavefunction information.

The index theorem ties them together only at the level of the *signed sum*:
`Σ_x q_A(x) = n₊ − n₋`. But the local split *over-counts* — `Σ q⁺ > n₊` and
`Σ q⁻ > n₋` in general, because a single zero mode contributes with locally varying
sign across its support, and only the integrated signed sum recovers the index.

The test results are summarized below (an entry of "recovers" means a clean
coordination-free distributed implementation exists):

| Bridge claim | naive ε-local CALM | JD-CALM | AC-CALM |
|---|---|---|---|
| signed-real density `q_A(x)` locally computable | yes | yes | yes |
| signed-real aggregate `Q_A` monotone at provenance layer | no (signed semilattice broken) | yes (Jordan split) | yes (per-`r`) |
| integer index `n₊ − n₋` recoverable as a CALM readout | no | no | per-config yes, uniform no |
| instanton/anti-instanton input growth | no | yes (Jordan-aggregate feature) | yes (silent) |
| disjoint-support truncation-rounding | no | no at integer readout, yes at signed-real | yes (no rounding) |
| **bridge to GW signed-real readout survives** | no | **yes** | **yes** |
| **bridge to GW integer-index readout survives** | no | **no** | **no (uniformly)** |

JD-CALM gives the strongest *structural classification* (it positively types the
signed cancellation as a Jordan-aggregate feature); AC-CALM gives the strongest
*practical bound* (explicit `2 ε(r)` cross-replica consistency). Applied jointly —
per-sign and per-radius — they give both. The combined verdict matches the layer
split of §4.3: signed-real recovers, integer-index does not.

### 5.2 Nielsen-Ninomiya as a distributed protocol contract

A second, more structural test asks whether the *whole* Nielsen-Ninomiya theorem
translates into a distributed-protocol impossibility statement, assumption by
assumption. Restating the theorem over a vertex-transitive communication graph with
identical per-node rules, the seven assumptions translate as follows:

| NN assumption | protocol translation | class-respecting? |
|---|---|---|
| (1) locality (finite-range hopping) | bounded communication radius (LOCAL model; Linial 1992, Naor-Stockmeyer 1995) | yes, exact |
| (2) Hermiticity | reversibility + adjoint-closed channel | partial (reversibility exact; adjoint leg has no clean analog) |
| (3) translation invariance | homogeneous / anonymous-network model (Angluin 1980) | yes, exact |
| (4) exact U(1)_V conservation | CRDT safety invariant (Shapiro et al. 2011) | yes |
| (5) exact on-site U(1)_A | strong per-replica consistency without coordination (CAP "C"; CALM monotonicity) | **yes — load-bearing** |
| (6) free / bilinear action | oblivious protocol | weak (bilinearity is structural, obliviousness informational) |
| (7) discrete spectrum + on-site charge | finite state space + bounded message alphabet | yes, exact |

Five of seven assumptions map *exactly* onto named, published distributed-systems
concepts. The load-bearing one is assumption (5): "chiral symmetry realized exactly
on-site" translates to "strong per-replica consistency with no coordination round,"
and the forgetful operation that demands strict-on-site realization is, in both
languages, *the same functor* —
`ϕ_local : (bulk + boundary + modified algebra) ↦ on-site lattice` on the physics
side equals `ϕ_onsite : (coordination-allowed, bulk-mediated) ↦ coordination-free
CRDT` on the protocol side. Lüscher's explanation of why Ginsparg-Wilson evades
Nielsen-Ninomiya — "the symmetry is realized in a different way than the theorem
assumes" — is exactly the statement that the GW algebra relaxes
strong-consistency-without-coordination by introducing an inter-site coupling while
preserving the global invariant.

The most testable prediction this surfaces is a candidate correspondence between
the **CALM monotonicity hierarchy** and the **Ginsparg-Wilson algebra**: the
protocol-side criterion classifying coordination-free queries would classify
exactly which chiral algebras admit a Lüscher-class evasion rather than collapsing
to a bulk+boundary inflow object. The pilot's own verdict is deliberately bounded:
"theorem-shaped, second-pass justified" — a structured, class-respecting
translation strong enough to deserve theorem-grade work, **not yet a theorem**. The
honest gaps it ships visibly are the partial Hermiticity translation, the weak
bilinearity translation, and the absence of any asynchronous-timing or
Byzantine-fault analog.

---

## 6. Connection to the 2021 paper's effective-chirality claim

The signed-readout line and Geometric Unity's 2021 draft are addressing the *same*
underlying problem — how chirality, which the Standard Model exhibits, can emerge
from a structure that is non-chiral at the fundamental level — but they approach it
from opposite directions.

The 2021 paper (Section 11.4, "effective chirality") argues that the fundamental
theory lives on a higher-dimensional space of indefinite signature and is **not
chiral** at that level; what looks like fundamental chirality in the Standard Model
is an *effective* phenomenon arising in a low-scalar-curvature decoupling limit,
where the non-chiral theory separates into chiral sectors. By the project's own
assessment this is the least rigorous part of the paper: no decoupling scale is
estimated, no precise theorem is stated, and the argument appeals to unspecified
"standard decoupling arguments." It is a *narrative* claim, and it is precisely the
paper's intended answer to the chirality no-go theorems.

The signed-readout work attacks the same boundary from the **lattice / no-go side**
rather than the geometric side. Where the paper proposes that chirality is an
emergent, observer-relative effective property (placing the chirality question on
an emergence axis rather than a substrate axis), the signed-readout theorem
supplies a precise vocabulary for what "emergent, not fundamental" can mean
operationally: an observable can have a perfectly *monotone provenance* — every
contribution accumulated locally and append-only — while its *scalar readout* is
signed and non-monotone, so that the net chiral quantity is a readout-layer
artifact rather than a substrate-layer invariant. The two pictures line up
suggestively: the paper's "globally non-chiral, locally effectively chiral" is, in
the signed-readout language, "monotone-provenance substrate, signed-readout
decode."

The relationship is a *parallel*, not a derivation. Neither establishes the other.
The paper's mechanism remains under-specified, and the signed-readout theorem is a
lattice/distributed-systems result, not a statement about the Observerse. The honest
summary is that they are two independent attempts to make "chirality is effective,
not fundamental" precise — one geometric and narrative, one combinatorial and
proved-but-narrow — and that the signed-readout factorization is the sharper of the
two about *where* the apparent chirality enters (the readout) even though it says
nothing about the specific geometric decoupling the paper invokes.

---

## 7. Open questions and falsification

The result is deliberately modest, and several concrete things remain open. Each is
stated with what would settle it.

**The CALM ↔ Ginsparg-Wilson functor.** The strongest claim in the protocol
analogy is a proposed equivalence between the category of CRDT-style protocols with
conserved observables and the category of lattice-fermion algebras with
anomaly-inflow data. This functor is named structurally but **not constructed**.
The decisive check: take the Ginsparg-Wilson modified symmetry generator and test
whether the query "what is the global axial charge?" is CALM-monotone in the
precise logic-programming sense. *If it is not monotone in any precise sense, the
load-bearing translation collapses and the protocol analogy drops from
"theorem-shaped" to "structured-but-metaphor."* This is the sharpest available
falsifier of the whole line.

**The integer-index layer.** The bridge is dead at the integer topological-index
readout under every framework tested, because integer recovery needs an unbounded
truncation or a non-CALM rounding step. Open question: is there a *genuinely
different* readout discipline (not Jordan splitting, not radius truncation) that
recovers the integer index coordination-free, or is the integer-index obstruction
provably permanent? A permanence proof would be a clean negative theorem worth
stating on its own.

**Asynchronous and fault-tolerant analogs.** The protocol translation fixes
synchronous timing and a fault-free model. Two open second-pass questions: (i) does
an asynchronous Protocol-NN inherit an FLP-class (Fischer-Lynch-Paterson 1985)
impossibility for a richer class of observables, yielding a lattice-fermion
impossibility with no published physics-side statement? (ii) Is there a Byzantine
fault-tolerance threshold below which a conserved chiral charge can still be
extracted, giving a fault-tolerance reading of anomaly cancellation? Both are
currently conjectural.

**The curved-substrate sub-statement.** The physical sub-statement invokes
Atiyah-Patodi-Singer-type index structure on curved substrates, but the
curved-lattice substrate is not formally constructed. The gravitational case is
"plausible modulo substrate," not proved.

**Scope of the anomaly corollary.** Within the abelian internal-Noether sub-class
the anomaly reading is rigorous; the claim that anomaly is the *dominant* source of
negative-weight generators across the broader lattice-gauge family is asserted, not
exhaustively verified. A counterexample — a natural lattice-gauge observable whose
readout sign is set by some non-anomaly mechanism that the framework mistypes —
would narrow the corollary further.

**What would falsify the approach as a whole.** The signed-readout boundary theorem
itself (the factorization plus the monotonicity criterion) is elementary and is not
seriously at risk. What is at risk is its *relevance*: the claim that this
factorization captures something real about chirality emergence rests on the
CALM ↔ GW correspondence. If the direct CALM check on the Ginsparg-Wilson generator
comes back negative, the theorem survives as a fact about signed aggregates but
loses its bridge to the physics, and the line should be demoted accordingly. That
is the intended honest exit, and it is concrete and bounded.

---

## Appendix — Status and provenance

This document consolidates a multi-stage research line whose internal record
included an early anomaly-centered conjecture, its falsification, and a pivot to
the factorization criterion. The earlier stages are preserved separately as
provenance; this account supersedes their strategic conclusions but not their
honesty. The standing verdict is **PARTIAL**: the factorization and the
signed-readout monotonicity criterion hold rigorously; the anomaly-iff fails in
general and survives only as a restricted corollary; the GW bridge recovers at the
signed-real readout layer and fails at the integer-index layer; and the
Nielsen-Ninomiya protocol analogy is theorem-shaped but not yet a theorem.

Cited external literature: Hellerstein & Alvaro 2020 (CALM); Ameloot et al. 2013;
Shapiro et al. 2011 (CRDTs / PN-counter); Bailis et al. 2012 (bounded staleness);
Hasenfratz, Laliena & Niedermayer 1998 (lattice index theorem); Neuberger 1997 and
Lüscher 1998 (Ginsparg-Wilson / overlap); Hernández, Jansen & Lüscher 1999 (GW
locality); Nielsen & Ninomiya 1981; Atiyah-Singer and Atiyah-Patodi-Singer index
theorems; Angluin 1980, Linial 1992, Naor-Stockmeyer 1995 (LOCAL model / anonymous
networks); Fischer, Lynch & Paterson 1985 (FLP).
