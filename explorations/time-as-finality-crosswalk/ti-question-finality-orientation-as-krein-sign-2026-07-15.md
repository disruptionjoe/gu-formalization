---
title: "TI thread: is the Krein sign bar(b) the finality orientation of issuance? (the precise cross-repo question the gate pipeline isolated)"
status: exploration
doc_type: cross-repo-question
created: 2026-07-15
grade: "a precise, falsifiable cross-repo QUESTION (not an identity claim). Grounded in temporal-issuance/FORMAL-OBJECT.md. The identification is Joe-gated; TI's own verdict Issue[S]^physical=false means any answer stays conditional on TI's formal residue."
provenance: "Joe, chat 2026-07-15: after the gate pipeline reduced bar(b) to one external bit = the issuance/finality orientation, open the TI thread."
depends_on:
  - explorations/time-as-finality-crosswalk/gate-pipeline-conclusion-2026-07-15.md
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md
ti_anchors:
  - "temporal-issuance/FORMAL-OBJECT.md: Iss_n (directed source-extension step); Finality_mu (reversal/deletion cost); <=_S (realization-dependency order); Ext_S as a category with directed morphisms e: S -> S'; Q: Mor(ExtCat) -> [0,inf) (nonneg magnitude); global dR KILLED (RUN-0012/0019), survivor is observer-LOCAL issuance + gluing G_ij/Omega_ij"
  - "W211: names the bit's source as the 'TI/TaF finality-reservoir SIGNATURE'"
verdict: "OPEN QUESTION. Candidate identification: bar(b) = the ORIENTATION (Z/2) of the issuance/finality arrow. Promising terminological + structural match; four crisp sub-obstructions below. Not an identity; Joe-gated."
---

# Is bar(b) the finality orientation of issuance?

## Why this is the precise question

The gate pipeline reduced `bar(b)` to **one external bit** whose value, in the H1 reading, is **the
orientation of the issuance/finality arrow** (see `gate-pipeline-conclusion`). Temporal-issuance is where that
arrow lives. W211 already names the bit's source as the **"TI/TaF finality-reservoir SIGNATURE"** — and
"signature" is exactly sign-shaped. So the candidate identification is:

> **bar(b) (Krein grading sign) ≟ the ℤ/2 orientation of issuance/finality** — the binary "toward
> settled/final" direction shared by all issuance events.

## Why TI is a genuine candidate (what its formal object supplies)

Unlike the earlier failed search for a `U(16)` boundary holonomy (`record-issuance-boundary-selector`, which
found NO carrier), this asks only for a **single ℤ/2 orientation**, and TI is intrinsically directional:

- `Iss_n` is a **directed** source-extension step `Gamma_n -> Gamma_{n+1}` (you issue, you do not un-issue).
- `Finality_mu` is a **reversal/deletion cost** — a forward/reverse **asymmetry**, whose sign is a natural ℤ/2.
- `Ext_S` is a **category with directed morphisms** `e: S -> S'`; `<=_S` its thin reflection.

So a binary "finality orientation" (forward = lower reversal cost = toward settled) is a plausible TI-native
ℤ/2, and it is observer-independent in the sense that all issuance shares one arrow.

## The four sub-obstructions (each a crisp yes/no the TI side can attack)

1. **Is the finality arrow genuinely ℤ/2, or a magnitude/preorder?** `Finality_mu` and `Q` are non-negative
   **magnitudes** in `[0,inf)`, and `<=_S` is a **preorder/partial order**, not obviously a binary. The
   identification needs a genuine two-valued orientation, not a scalar. *Question: does TI carry a ℤ/2
   orientation invariant (a forward/reverse parity), distinct from the magnitude `mu`/`Q` and from the order
   `<=_S`?*
2. **Is there a GLOBAL, observer-independent orientation?** TI **killed the global frontier `dR`**
   (RUN-0012/0019); the surviving object is **observer-LOCAL** issuance patches plus gluing (`G_ij`,
   `Omega_ij`). So a *universal* orientation is not a current TI primitive — it would be a **gluing outcome**.
   *This closes the loop with Gate 2a:* IF each observer's local issuance carries a finality orientation
   (a per-observer / vertex datum), THEN Gate 2a's coboundary result says the gluing **forces** a single
   consistent global orientation with no domains. *Question: do TI's `G_ij`/`Omega_ij` reconcile local
   finality orientations as a coboundary (consistent) or can they be frustrated?*
3. **Does per-observer local finality reproduce the vertex-sourced (passing) branch?** Gate 2a passes iff the
   sign is vertex-sourced. TI's local-issuance-patch structure is literally per-observer. *Question: is the
   local finality orientation a property of each observer's own issuance (vertex 0-cochain) rather than of
   pairwise relations (edge 1-cochain)? If vertex, the pipeline's PASS branch is instantiated.*
4. **Physicality caveat (does not block the structural answer, but bounds it).** TI's own ledger has
   `Issue[S]^physical = false`; the strongest survivor is the class-relative **formal** residue
   `OnlineIssuance^LC` (Lean-hardened, not physical). So even a clean identification makes `bar(b)` conditional
   on TI's **formal** finality object, not a physical derivation. *This is the same grade honesty as the GU
   side: a reduction to a named object, not a derivation of nature.*

## What a positive answer would (and would not) buy

- **Would:** complete W211 path (a) at **structural/formal grade** — `bar(b)` = the finality orientation, a
  single ℤ/2 supplied by TI, made universal by gluing (Gate 2a), with no domains. A clean tri-repo closure of
  the *structure* of the bit.
- **Would NOT:** derive the generation **number** (still source-action-gated), establish physical issuance
  (TI's own `Issue[S]^physical=false`), or discharge the Joe-gated identity. The value would be "the finality
  orientation," conditional on TI's formal object.

## Scoping result (2026-07-15): TI already built the machinery, and it converges

Two **prior** TI results — E155 (2026-07-09) and E160 (2026-07-10), both **predating this session**, so this
is not manufactured convergence — resolve sub-obstructions 1-3 at formal grade:

- **#1 (is there a ℤ/2?): YES, as a well-posed object.** E160 built exactly `A: ExtCat -> B(ℤ/2)`. Findings:
  bare loops do **not** derive holonomy; a consistency rule derives **trivial (identity)** transport; a
  **nontrivial** ℤ/2 is derivable **iff C-typed admissibility carries a composition-compatible (functorial)
  ℤ/2 label**. So the orientation is a named target with a named condition (source-side + functorial), not yet
  constructed.
- **#2 (coboundary or frustrate?): DECISIVELY.** E155: `Ext_S` reconciliation is **confluent**
  (order-independent = coboundary-consistent) **exactly OFF the SBP fork locus**, and non-confluent **exactly
  ON** the fork set (`phi` vs `not-phi`, opposite polarity, no common successor) — which is **exactly the
  source-side issuance witness set**. Reconciliation glues consistently everywhere except at the source events
  (the polarity choices) themselves.
- **#3 (vertex vs edge): SUPPORTED.** The fork is a per-**site** polarity choice (a 0-cochain), not a pairwise
  relation -> **vertex-sourced** in TI's own formalism.

**The convergence.** Both repos produce the **same structure from opposite ends**: the ℤ/2 sign is a
per-site / per-observer **source polarity (0-cochain)**, issued at forks, with **trivial (coboundary /
confluent) transport off them** — **not** a nontrivial loop holonomy. This matches the GU walk-back exactly
(the H1 loop-holonomy does not carry the value; it is a vertex source). E160's "nontrivial holonomy needs a
functorial source label" plus E155's "the ℤ/2 lives at the non-confluent fork" together say **TI does not
derive it as a loop holonomy either** — it derives it as a source-side polarity choice. Fully consistent, and
independently arrived.

**The one decisive question that remains (sharpened — this is where the VALUE lives).** Confluent gluing makes
any per-site polarity assignment globally **consistent** (no domains) but leaves **one free global bit**:
which orientation is "+". The value of `bar(b)` is **determined iff TI's finality supplies a directional bias
on the fork** — a preferred polarity = the arrow of finality (all forks resolve toward "settled"). That is
exactly `Finality_mu` (reversal/deletion cost): if resolving toward final is cheaper than reversing, that
asymmetry **is** the preferred polarity = the value. So the next probe is precise: **does `Finality_mu`'s
reversal-cost asymmetry induce a globally-aligned ℤ/2 bias on the polarity fork?** Consistency (no domains) is
already secured by E155; only the **bias** determines the value.

## TaF cross-check (2026-07-15): a THIRD independent arrival + the finality-direction object

Scanning time-as-finality (which owns the finality/capability leg) is even more productive than TI:

- **Three-way independent convergence on the ℤ/2 signed-graph structure.** TaF **T39** (CSP reframing) proves
  its finality-gluing patch language is a **binary {-1,+1} CSP**, with the gluing obstruction **exactly a
  parity-conflicting binary CSP (signed-graph 2-colorability / negative cycle)**; global satisfiability =
  absence of negative cycles. That is the **same object** as GU **Gate 2a** (XOR-SAT / frustration) and TI
  **E155** (fork = opposite-polarity non-confluence). Three repos, three independent derivations, one object:
  a ℤ/2 signed-graph whose obstruction is parity frustration. This substantially **de-risks the
  manufactured-convergence guard** — the three were built separately (T39, Gate 2a, E155/E160).
- **TaF has a finality-DIRECTION object (T18).** "Finality-Induced Direction": a transformation is admissible
  iff no D1 dimension decreases; strict finalization increases a D1 dimension; **the reverse of every strict
  finalization is impossible**; finalization edges form an **acyclic partial order**. So TaF derives a
  **one-way finality arrow** inside its model — the candidate directional bias that would fix the free global
  bit. The 4th D1 dimension is literally **C = graph reversal cost** (the reversal asymmetry we hypothesized in
  TI's `Finality_mu`), confidence "formal only."
- **TaF has the UNDERDETERMINATION phenomenon (T53/T54).** "descent-underdetermined: multiple non-isomorphic
  completions fit the same observer views." This is exactly "confluent gluing leaves one free global bit,"
  observed directly (T53 classified underdetermined).
- **The honest wall, flagged by TaF itself (T57).** "FRP ... does **not derive the direction of source/target
  finality arrows**; the T56 circular-risk question remains open." So T18's direction is "only inside the
  stated model," reversal cost is "formal only," and the fine-grained arrow direction that would FIX `bar(b)`'s
  sign is **explicitly open** in TaF — the same formal-grade wall as TI (`Issue[S]^physical=false`) and GU
  (source action).

**Net.** A finality direction/bias EXISTS (T18); consistency / no-domains is **triple-secured**
(T39 = Gate 2a = E155); but the global orientation can remain **underdetermined** (T53) and its arrow
**direction is TaF-flagged open** (T57). So `bar(b)`'s value is **not yet fixed** — the same formal-grade open
across all three repos. What genuinely strengthened is the **structure** (three-way convergence) and the
**location** of the remaining bit (the finality-arrow direction, T18/T57), not its determination.

## Status

OPEN. This is a **question**, not a claim. The identification bar(b) = finality orientation is **Joe-gated**
(a cross-repo identity; tri-repo rule: no identity before adapter contracts prove out). Filed to the
temporal-issuance mailbox for the TI side to attack sub-obstructions 1-3.
