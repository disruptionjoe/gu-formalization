---
title: "PRONG II (FLP-EXACT): is GU's 'cannot mint sigma internally' a genuine oracle-RELATIVIZATION theorem or an ANALOGY to FLP? VERDICT II-MIXED. The relativization SHAPE is EXACT and a theorem in the precise LOGIC sense (W211's five-method Godel-independence = a statement independent of GU's internal theory; one added Z/2 axiom decides it = a finite completing oracle) -- GU IS oracle-relative in the independence-plus-completion sense. But the FLP proof MECHANISM (valency/bivalence = pi_0 connectivity of a scheduler-reachability complex) is ANALOGY, not the same obstruction object as GU's Hom(triv,sign)=0 (Schur equivariant-vanishing / the W211 invariant-form dim 1->2 jump); they share the equivariant-selection SCHEMA, not the invariant. The Chandra-Toueg weakest-failure-detector ordering is ANALOGY: an order EXISTS (sigma=1 Hartley bit is the minimal non-trivial oracle, tau=Z/3 strictly larger) but it is cyclic-group cardinality, not a reducibility/emulation lattice, and sigma vs tau are oracles for DIFFERENT tasks, not one task at two strengths. FLP's faulty process is NOT literally the observer's causal future = TaF T19: three distinct mechanisms (asynchrony/unbounded-delay vs causal-past retraction vs self-reference); TaF's own ledger places T19 near Godel/Rice not FLP, and the cross-repo involution-typing-lemma already found the GU/TaF time-face LEG-deep not MECHANISM-deep. Planted FALSE control (GU-obstruction == Byzantine n>3f) REJECTED by the polarity criterion (n>3f is internally solvable by quorum -- the OPPOSITE polarity, no external bit)."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md
outcome: II-MIXED
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
inputs:
  - explorations/council-systems-boundary-meaning-2026-07-21.md (member 5, FLP/distributed)
  - explorations/council-aggregation-condorcet-2026-07-21.md (FLP = cross-lens consensus, top-4 on all 12 ballots)
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - "READ-ONLY time-as-finality: tests/T19-phenomenal-bridge-complexity-separation.md; CLAIM-LEDGER.md; explorations/involution-typing-lemma-2026-07-20.md"
runnable:
  - tests/channel-swings/flp_exact_relativization_probe.py
---

# PRONG II -- FLP-EXACT: theorem or rhyme?

FLP was the most uniformly-agreed council reading (top-4 on every one of the 12
ballots; Condorcet #2 behind INFO, and the *most cross-lens-robust* steelman).
The question this prong answers is not whether FLP is *evocative* -- it plainly
is -- but whether "GU cannot mint sigma internally" is **literally** an
oracle-relativization theorem, and where (if anywhere) the correspondence is only
a shape-match. Truth-seeking, not romantic: a rhyme that scopes honestly is worth
more than an isomorphism claimed on enthusiasm.

**Verdict up front: II-MIXED.** The relativization SHAPE (internal-impossible +
external-oracle-suffices) is EXACT and is a genuine theorem in the precise
*logic* sense. The FLP *mechanism*, the Chandra-Toueg *ordering*, and the
FLP-faulty-process = *causal-future* identification are ANALOGY. GU **is**
oracle-relative -- under one precise reading (logical independence + a finite
completing datum), not under the others (complexity relativization; a literal
failure-detector). Below: the three sub-analyses, the planted-control rejection,
and the exact EXACT-vs-ANALOGY boundary.

Receipt: `tests/channel-swings/flp_exact_relativization_probe.py` -- deterministic
(double-run byte-identical), numpy only, no network, foreground, exit 0. HEADLINE
`13/13 [E] PASS + 5/5 [F] FIRE -> ALL PASS`.

## Method: the discriminator, made operational

The discriminator between EXACT and ANALOGY is **same universal property / same
obstruction object**, versus **merely both being impossibilities**. I split every
correspondence into two independent axes and grade each:

- **The relativization POLARITY (the shape).** `internal_solvable == False` AND a
  finite external oracle resolves it. This is the structural signature of an
  oracle-relative result. It is a *yes/no* property of the correspondence.
- **The obstruction OBJECT (the mechanism).** *Which* invariant vanishes, in
  *which* category, proven *how*. EXACT requires the same object (or a named
  functor identifying them); a shared *schema* with different invariants is
  ANALOGY.

A correspondence is EXACT only if it matches on **both** axes. Matching the
polarity but not the object is precisely II-MIXED.

Three "oracle-relative" senses must be kept apart, because the council's phrase
"the precise complexity/logic sense" silently blends them:

1. **Complexity relativization** -- a Turing machine with an oracle tape,
   relativized classes `P^O`, `NP^O`, a decision problem solvable *relative to* a
   set `O`.
2. **Logical independence + completion** -- a statement `phi` independent of a
   theory `T`; `T + phi` and `T + not-phi` both consistent; adding `phi` as an
   axiom (a 1-bit "oracle" for its truth value) decides it.
3. **Distributed-computing oracle (failure detector)** -- an external device
   supplying hints about failures; an FLP-unsolvable task becomes solvable given a
   sufficiently strong detector, ordered by Chandra-Toueg reducibility.

Keeping these three apart is what makes the verdict precise rather than
impressionistic.

---

## Sub-analysis 1 -- Is "GU cannot mint sigma internally" a genuine relativization theorem?

### 1a. The SHAPE is EXACT, and it is a theorem in sense (2)

The internal-impossibility half is **not a metaphor and not a lean** -- it is
W211, proof-grade. Five independent notions of "compute inside GU"
(counterfactual-invariance R16, Dirac-BRST cohomology R9, Lawvere fixed-point R7,
topos internal logic R12, Helmholtz variational reconstruction R1) each reproduce
the same positive control (the full gauge group forces the ungraded `eta` by
Schur, nulldim 1) and each leave the **same** Z/2 free. "Compute harder inside
GU" is *ruled out by proof*, because each method is a different sense of
internal computation and all five fail identically. In sense (2) this is exactly
a **Godel-independence statement**: the C-grading sign is independent of GU's
good-stable theory -- true in the good model, false in the pathological model of
the *same* self-consistency theory (W208's two genuine fixed points).

The external-oracle-suffices half is equally literal: W211 names precisely two
honest completions -- (a) obtain the sign from TaF, or (b) **posit a
Krein-positivity axiom and state GU's result conditionally.** Path (b) *is* the
independence-plus-completing-axiom structure: one added Z/2 axiom decides sigma
completely. One axiom = one oracle query = one bit.

So on the POLARITY axis the correspondence is EXACT: `internal_solvable = False`
(W211) and a finite external oracle (one Z/2 axiom) resolves it. **GU is
oracle-relative in the precise sense (2): a statement independent of its internal
theory, resolved by a finite external completing datum.** This is a theorem, not
a rhyme. The probe's Part B reproduces both the equivariant-vanishing
(`Hom_{Z/2}(triv,sign)=0`) and the W211 invariant-form dimension jump `1 -> 2`
from tiny matrices (full irreducible group: invariant-form dim 1; conditioned
reducible stabilizer: dim 2 -- the extra dimension *is* the liberated Z/2).

**Is it sense (1) -- complexity relativization?** No, not literally. There is no
Turing machine, no oracle tape, no relativized complexity class, no `P^O` vs
`NP^O` separation. The "computation" in all five W211 methods is *algebraic*
(Schur's lemma, cohomology, fixed points, Heyting semantics, variational
reconstruction), not machine computation over an input length. Reading W211 as a
complexity-relativization theorem is ANALOGY. The council's "complexity/logic
sense" should be read as: **logic yes, complexity no.**

### 1b. The MECHANISM (FLP's proof) is ANALOGY

FLP's obstruction object is **bivalence/valency**: every deterministic 1-crash
async consensus protocol has a bivalent initial configuration, and from any
bivalent configuration the scheduler can force a "critical/hook" step whose
outcome hinges on the order of one process, using the **indistinguishability of a
slow process from a crashed one** to keep the system bivalent forever. Its modern
topological form (Herlihy-Shavit): the protocol complex stays **connected**
while the consensus output complex is **disconnected**, and there is no simplicial
map from a connected complex to a disconnected one respecting the task -- a
**`pi_0` / connectivity** obstruction over a scheduler-reachability complex.

GU's obstruction object is **`Hom_G(triv, sign) = 0`**: with `G = SO(9) x SO(5)`
(the C-commutant / maximal-compact stabilizer), the even reading class is the
trivial rep and sigma is the sign rep; Schur gives no nonzero intertwiner. Its
degree is 0 (invariants / `H^0(G, sign) = sign^G = 0`); it is a
**representation-theoretic vanishing**, no homotopy.

These share a genuine and rather tight **schema** -- "no equivariant /
locally-constant selection from a symmetric object to a symmetry-breaking output"
(both are the Lawvere/diagonal no-fixed-selection pattern; note W208 already
proves GU's half *via* Lawvere). But the **invariants differ** (`pi_0`-connectivity
of a scheduler-reachability complex vs `Hom`-vanishing of finite-group linear
reps), in **different categories** (a homotopy/order invariant vs a linear
intertwiner), proven by **different arguments** (an adversary schedule that
preserves bivalence vs Schur's lemma on inequivalent irreducibles). No functor is
exhibited carrying one to the other. Under the discriminator: **same schema, not
the same obstruction object -> ANALOGY at the mechanism level.**

The probe's Part C stamps exactly this: `shape_match = True`,
`mechanism_match = False` (`pi0_connectivity` != `hom_vanishing`).

**Sub-1 result:** relativization SHAPE = **EXACT theorem (logic sense)**; FLP
proof MECHANISM = **ANALOGY** (shared equivariant-selection schema, distinct
obstruction object). This is the classic MIXED signature.

---

## Sub-analysis 2 -- Chandra-Toueg: is one Z/2 the weakest failure-detector for sigma, tau strictly stronger?

### 2a. What Chandra-Toueg actually asserts

Chandra-Toueg is a *precise* theorem: failure detectors form a partial order
under **algorithmic reducibility** (`D <= D'` if `D` can be emulated using `D'`),
and the **weakest** detector that solves consensus is `Omega` (eventual leader) --
weakest meaning every consensus-solving `D` satisfies `Omega <= D`, and `Omega`
itself solves consensus. The depth is entirely in the **reducibility/emulation**
structure: `Omega` is a specific, non-obvious object whose *instantaneous* output
is unbounded over time (a process id every step forever); "weakest" is about what
can be *extracted from* it, not about its bit-width.

### 2b. What GU has: an order, but the wrong kind

There *is* an order in which sigma sits below tau:

- sigma resolves with **exactly 1 Hartley bit** (`Z/2`, `log2 2 = 1`); it is the
  **minimal non-trivial** oracle -- 0 bits leaves the Godel-independence, so you
  cannot resolve a binary superselection with less. (Probe E1.)
- tau (generations) costs `>= log2 3 ~ 1.585` bits (the info council: `Z/3`,
  independent of sigma), strictly more. (Probe E2.)

So "1 Z/2 is the weakest oracle that resolves sigma, tau strictly stronger" is
**true** and even provable. But it is provable as a **bit-cardinality /
cyclic-group-order** fact (`log2` of the choice-group cardinality), **not** as a
Chandra-Toueg reducibility theorem. It has no emulation content, no analog of
"`Omega` can be extracted from any consensus-solving `D`," no distinguished
non-trivial least element with hidden strength -- the least element is just "1
bit," and strength is just "count the bits."

### 2c. The sharper disanalogy (a category slip in the steelman)

Chandra-Toueg orders oracles **for a single fixed task** (consensus) at different
strengths. GU's sigma and tau are oracles for **different tasks** -- sector sign
vs generation count, explicitly *independent* (Q3). tau is not a "stronger oracle
for the sigma-task"; it is an oracle for a *different* task that happens to cost
more bits. Calling tau "a strictly stronger failure-detector than sigma" conflates
a **cost order across different problems** with a **strength order for one
problem**. Chandra-Toueg is the latter; GU has the former.

**Sub-2 result:** an order EXISTS and the placement (sigma minimal at 1 bit; tau
strictly above) is EXACT-but-elementary (cardinality / cyclic-group order); the
Chandra-Toueg **weakest-failure-detector mechanism** (reducibility lattice,
emulation, a distinguished non-trivial least element like `Omega`) is **ANALOGY**,
and it additionally mis-types sigma vs tau as one-task oracles when they are
different tasks. So: **ANALOGY on the CT structure**, with a trivial-but-true
ordering residue.

---

## Sub-analysis 3 -- Is FLP's faulty process LITERALLY the observer's causal future = TaF T19?

Cross-repo READ-ONLY: TaF `T19`, its `CLAIM-LEDGER` block, and the
`involution-typing-lemma-2026-07-20.md`.

### 3a. The three roles, compared precisely

- **FLP faulty process.** The impossibility hinges on **one** process that may
  crash (`f = 1` suffices). The engine is **asynchrony**: a correct-but-slow
  process is *indistinguishable* from a crashed one because message delay is
  unbounded-but-**finite**. The hidden datum arrives *eventually* (fair
  executions); the impossibility is that no *finite time bound* forces a decision.
  The faulty process is a **peer** (another node), and the axis is **spatial**.
- **TaF T19 causal future.** The observer `R` cannot verify from its accessible
  down-set `A*(R)` whether its own finality is externally witnessed, because the
  witnesses (`e_E1, e_E2`) sit in `R`'s causal **future** up-set -- a **hard
  causal cut**, structurally absent from `A*(R)` (the model raises `ValueError`
  on any future node). The engine is a **causal-past retraction** `pi` (idempotent,
  non-invertible, oriented). The inaccessible thing is `R`'s **own future**, and
  the axis is **temporal**. Multiplicity is `k >= 2` (two independent witnesses).

### 3b. Three distinct mechanisms, not one

| | obstruction engine | direction | multiplicity | decides |
|---|---|---|---|---|
| **FLP** | asynchrony / unbounded-finite delay + valency | none (symmetric adversary) | `f = 1` peer | consensus termination |
| **T19** | causal-past retraction `pi` (oriented idempotent) | strict order (past<future) | `k >= 2` witnesses | self-referential self-verification |
| **GU leg (b)** | `alpha`-even blindness under a fixpoint-free Z/2 flip | involution (order-2 bijection) | `|B| = 2` | sector value sigma |

Two independent, already-filed cross-repo findings make this decisive rather than
impressionistic:

1. **TaF's own ledger places T19 near Godel/Rice, NOT FLP.** T19's results
   section names its closest formal relatives as **Godel incompleteness** and
   **Rice's theorem** (self-reference), and calls the gap "**stronger than
   undecidability**" -- "the required evidence does not exist in the accessible
   region." That is a *self-reference / causal-cut* obstruction, categorically
   unlike FLP's *termination-under-asynchrony* obstruction. FLP is not even TaF's
   own choice of relative.

2. **The involution-typing-lemma already scoped the GU/TaF time-face as LEG-deep,
   not MECHANISM-deep.** It proved (machine-checked, T-REFUTE) that no
   fixpoint-free involution reproduces T19's excluded class: T19's engine is the
   causal-past retraction, strictly more general than a Z/2 flip on **two** axes
   (orbit-cardinality `2^k > 2`, and orientation `pi.pi = pi` vs `alpha.alpha =
   id`). GU's flip and TaF's retraction "are cousins only at `|B| = 2`." FLP's
   asynchrony is a *third* engine again -- neither an involution nor a retraction,
   but a scheduler adversary over delays.

So the identification "FLP faulty process = observer's causal future = T19" links
**three different mechanisms** by a shared *conclusion* ("a fact the system cannot
settle from within its accessible horizon"). The mapping "a peer whose crash-status
is ambiguous" -> "my own causal future" also silently swaps FLP's **spatial**
peer-axis for T19's **temporal** self-axis -- an interpretive overlay, not a
forced identity.

**Sub-3 result: ANALOGY (a conclusion-level rhyme).** The shared conclusion shape
is real and is exactly the boundary-law's first/third-person conclusion; but the
three obstruction engines are distinct in kind, TaF's own analysis points away
from FLP, and the cross-repo lemma already certified the time-face unification as
leg-deep. "Literally T19" is refused.

---

## Planted control (required): the criterion must reject a FALSE correspondence

**Planted false correspondence:** "GU's obstruction is exactly the
Byzantine-agreement bound `n > 3f`." If my EXACT/ANALOGY test cannot reject this,
it has no power.

`n > 3f` is the condition for Byzantine consensus solvability. Apply the
discriminator:

1. **Wrong obstruction type.** `n > 3f` is a **threshold / counting** bound (a
   resource inequality on the honest:faulty ratio), proved by a partition
   (split-brain) argument. GU's is an **equivariant vanishing / independence**
   (a representation-theoretic zero). No functor carries a `Hom`-vanishing to a
   cardinality inequality.
2. **Wrong POLARITY -- the decisive rejection.** `n > 3f` is a **positive
   solvability** condition: with enough honest nodes the problem **is internally
   solvable**, by **quorum**, with **no external oracle**. GU's sigma is
   **unsolvable internally at any internal redundancy** (five methods, all
   internal notions of compute, all fail) and is resolved **only** by an external
   bit. `n > 3f` therefore has the **opposite** polarity to relativization
   (internal-sufficiency-with-redundancy), and carries **no external Z/2 the
   inside cannot mint** -- it carries a headcount.

The probe's Part D encodes this: `n = 3, f = 1` is unsolvable, `n = 4, f = 1` is
solvable **by quorum**; the fix is internal redundancy, so `n>3f` is *not*
oracle-relative. The polarity criterion then **admits** FLP<->GU (both
oracle-relative) and **rejects** `n>3f`<->GU (`D4`, `D5` teeth). Crucially the
rejection is on the *same* polarity axis that is the core of the EXACT claim:
the criterion does not wave through "any distributed-systems impossibility." It
admits FLP's genuine relativization shape and rejects the Byzantine counting bound.
**The test has teeth.**

(Consistency check the control also validates: FLP itself *passes* the polarity
gate -- async consensus is internal-impossible and a failure detector `Omega` /
partial synchrony restores solvability -- which is exactly why FLP is the right
rhyme and `n>3f` is the planted fake. The criterion cleanly separates them.)

---

## Verdict: II-MIXED, with the exact boundary

**GU is oracle-relative in a precise sense -- the LOGIC sense (2): a statement
independent of its internal theory, resolved by a finite external completing
datum (one Z/2 axiom). That half is a theorem (W211, five-method, proof-grade).
The FLP *packaging* around it -- the bivalence proof, the Chandra-Toueg ordering,
the causal-future identification -- is analogy.**

### THEOREM (exact):

1. **sigma is internally undecidable.** W211 Godel-independence, five independent
   methods, proof-grade. The internal-impossibility half is real. (Sense-2
   independence.)
2. **A finite external oracle resolves it.** One added Z/2 axiom
   (Krein-positivity) decides sigma; W211 names this completion explicitly.
   Independence + completing datum = the precise logic-sense relativization.
3. **Therefore GU is oracle-relative (logic sense).** EXACT. Not a lean.
4. **The oracle order places sigma minimal, tau strictly above.** sigma = 1
   Hartley bit (minimal non-trivial); tau `>= log2 3` bits. EXACT but elementary
   (cyclic-group cardinality).

### ANALOGY (shape-rhyme, not identity):

1. **GU's obstruction = FLP's bivalence/valency proof.** ANALOGY. Shared
   equivariant-selection *schema* (Lawvere/diagonal); different obstruction
   *objects* -- `Hom_G(triv,sign)=0` / Schur (rep theory, degree 0) vs
   `pi_0`-connectivity of a scheduler-reachability complex (homotopy/order). No
   identifying functor.
2. **The oracle order is a Chandra-Toueg weakest-failure-detector lattice.**
   ANALOGY. GU's order is bit-cardinality with no emulation/reducibility content
   and no distinguished non-trivial least element; and sigma vs tau are oracles
   for *different tasks*, not one task at two strengths (a category slip in the
   steelman).
3. **FLP's faulty process = the observer's causal future = TaF T19.** ANALOGY.
   Three distinct engines (asynchrony vs causal-past retraction vs Z/2 flip);
   TaF's own ledger places T19 near Godel/Rice; the involution-typing-lemma
   already certified the time-face LEG-deep not MECHANISM-deep; and the mapping
   swaps FLP's spatial peer-axis for T19's temporal self-axis.
4. **GU is oracle-relative in the complexity-theoretic sense (1).** ANALOGY. No
   relativized Turing machine, no oracle tape, no `P^O` separation; the internal
   "computation" is algebraic.

### The one-line boundary

> The **relativization SHAPE** (internal-impossible + external-oracle-suffices) is
> an **EXACT theorem in the logic/independence sense** -- GU genuinely is
> oracle-relative. Every **FLP-specific mechanism** attached to that shape -- the
> valency proof, the Chandra-Toueg ordering, the causal-future = T19
> identification, and the complexity-theoretic relativization reading -- is
> **ANALOGY**: a shared schema or conclusion, never the same obstruction object.

This is the prereg's pre-declared "likely honest outcome" (II-MIXED), reached by
computation, not by preference. It neither inflates the rhyme into an isomorphism
nor discards it: FLP earns its cross-lens-consensus status precisely because the
*shape* it names is exactly true, while its *machinery* is a cousin, not a twin.

---

## Boundary

Exploration tier. One artifact + one foreground probe
(`tests/channel-swings/flp_exact_relativization_probe.py`, exit 0, deterministic,
double-run byte-identical, numpy only, no network). The internal-impossibility
half is *consumed* from W211 (proof-grade, not re-derived here); externality is
the program's closed premise and is nowhere re-opened. The probe is a faithful
tiny model of the two structural facts under test (the relativization polarity;
the `pi_0`-vs-`Hom` obstruction-object mismatch) and the planted-control
rejection; the operator/proof-grade content it stands on lives in the cited W211
/ Q2 / TaF receipts. No edits to LANE-STATE, research-portfolio, NEXT-STEPS, the
decision-tree, or any claim/canon/verdict/ledger/posture file; the cross-repos
(time-as-finality) were read-only; no other agent's artifact was touched. No
commit/push, no external actions. `bar(b)`, `H59`, the count `{1,3}`, and public
posture are unmoved; the sigma value remains the externally posited datum. The
load-bearing seams a hostile reviewer should attack first: (i) whether "logic-sense
relativization" (independence + 1-bit completion) deserves the word
"oracle-relative" at all, or whether that word should be reserved for sense (1)
[the artifact's position: sense (2) is the standard model-theoretic meaning and
W211 satisfies it exactly]; (ii) whether the `pi_0`-vs-`Hom` object distinction is
essential or an artifact of choosing the topological FLP formulation [the shared
Lawvere schema is real, but no functor identifies the invariants, so ANALOGY
stands]; (iii) whether sub-3's three-engine table under-credits a deeper common
"accessible-horizon" object [TaF's own Godel/Rice placement and the
involution-typing T-REFUTE both cut against a deeper identity].
