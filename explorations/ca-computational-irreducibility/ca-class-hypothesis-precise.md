---
title: "WRK-395 — CA-Class Hypothesis: Precise Statement"
status: exploration
doc_type: synthesis
updated_at: "2026-05-31"
---

# WRK-395 — CA-Class Hypothesis: Precise Statement

**Status.** Local-only artifact. WRK-395 implementation/1 dispatched pass.
**Generated.** 2026-05-31
**Card.** `work/WORK-395-reputation-gu-ca-class-substrate-computational-irreducibility-exploration.md`.
**Hard rules.** Zero writes outside this draft directory. Zero canon writes. Zero `work.json` edits. Zero public push. `[speculation]` tagging throughout.
**Frame.** EXPLORATION, not publication retreat. Honest verdict among COMP-IRRED-IS-DEEPER-OBSTRUCTION / COMP-IRRED-IS-COMPLEMENTARY / COMP-IRRED-IS-ORTHOGONAL.

---

## 0. The CA-class hypothesis in one paragraph

> **[speculation, candidate hypothesis]** The right structural superclass for the GU bridge work is not "monotone-distributed-query systems" (CALM) and not even "categorical projections out of a shadow category" (v3 9-tuple alone) but **local-rule substrates with projected observables**. A *local-rule substrate* is a triple `S = (Σ, N, f)` with `Σ` a finite local alphabet, `N` a fixed local neighborhood (a finite subset of a homogeneous space `X` containing the origin), and `f : Σ^N → Σ` a synchronous local update function. Global state is an element of `Σ^X`; global dynamics is the product update `F : Σ^X → Σ^X`, `F(s)_x = f(s|_{x + N})`. An *observable* is a projection `O : Σ^X → V` for some value space `V` (often `Z`, `R`, `C`, or a more general algebraic object). The hypothesis: **CALM is the corner where `O` is computationally reducible to a monotone aggregate; GW-class observables live in the broader landscape where `O` may be signed-reducible, phase-reducible, or computationally irreducible**.

This is the v2-rr-axis material reframed at the substrate level. The rr-axis (`monotone-reducible / signed-BV / phase-cancellation / comp-irred`) is then a classification of *observables on a fixed local-rule substrate*, not just an abstract typing inside the v3 9-tuple. v3's `arch.r` becomes a CA-class projection out of a CA-class substrate.

---

## 1. Why this is the right superclass to test

Four convergent reasons (from the dialectic and v3 readings):

1. **Wolfram-CA lens (§6 of six-persona dialectic).** Local-rule systems can be exact, structured, and even universal without being monotone. CALM is one tame corner; signed CRDTs, reversible CA, and Class-4 CA all sit outside CALM but inside the local-rule landscape.

2. **WRK-388 v2.1 primitive (signed-readout monotonicity criterion).** The rigorous primitive isn't an anomaly-iff; it's a generator-weight condition on a readout. That criterion is **substrate-agnostic** — it applies to any local-rule substrate with any value group. CA-class is the natural substrate-level home for that primitive.

3. **WRK-389 v3 BvN wall (Birkhoff-von Neumann at value-lattice-distributivity).** The wall says *any classical distributive value lattice* fails to lift to non-commutative GW algebra. CA-class is exactly the classical-distributive-value-lattice substrate landscape. The wall is **stated at the CA-class level**; CALM is a sub-case.

4. **Convergent persona authorities.** The Wolfram-CA persona and Complexity Science persona converge on layer conflation as the structural error in v1; both identify the local-rule substrate as the missing level. The 21-persona meta-verdict's "Issue B" (layer conflation, 5 personas) and "Issue A" (wrong categorical level, 4 personas) both point at the CA-class superclass as the resolution layer.

---

## 2. The four-element formal specification of CA-class substrates

A CA-class substrate is `S = (Σ, X, N, f)`:

- **`Σ`** — finite local alphabet (binary `{0,1}`, finite group `G`, finite field `F_q`, finite ring `Z/nZ`, or any finite set).
- **`X`** — homogeneous space (the lattice; usually `Z^d` for some dimension `d`, but more generally any countable space on which a group `G` acts transitively).
- **`N`** — fixed finite neighborhood `N ⊂ X` containing the identity. For elementary CA: `N = {-1, 0, 1} ⊂ Z`. For Game of Life: `N` is the 8-cell Moore neighborhood in `Z^2`.
- **`f`** — synchronous update `f : Σ^N → Σ`.

Global state space: `Ω = Σ^X`. Global update: `F : Ω → Ω`, `F(s)_x = f((s_{x+n})_{n ∈ N})`.

An observable is `O : Ω → V` with `V` an arbitrary value space (typically with algebraic structure — group, ring, lattice, vector space).

**Three structural sub-classes already exist in the literature:**

- **Reversible CA** (Margolus, Toffoli, Critters rule). `F` is a bijection; admits inverse rule. Equivalent to block CA with reversible block rule on Margolus neighborhood. Often carry **conservation laws** (number-conservation, parity, momentum) by construction.
- **Number-conserving CA** (Boccara, Fukś, Formenti et al.). `O = Σ_x s_x` is preserved by `F`. There is a "continuity-equation" characterization; the local rule decomposes as a sum of "move-left" + "move-right" + "stay" units.
- **Class-4 / universal CA** (Rule 110, Cook 2004; Game of Life, Berlekamp-Conway-Guy 1982). Local rule supports universal computation; emergent gliders and particles propagate signed/phase-like contributions.

The CA-class hypothesis subsumes all three sub-classes plus the un-restricted "generic local rule" case.

---

## 3. CALM as the monotone-reducible corner of CA-class

A CALM-style observable on a CA-class substrate has three features:

1. **Append-only / monotone information order on `Ω`.** Sites accumulate "voted" / "delivered" / "evidence" markers; existing markers never retract.
2. **Aggregator-as-monotone-shortcut for `O`.** The observable `O(s) = ⊕_x g(s_x)` is computed by a commutative-associative monoid operation `⊕` (max, set-union, sum-of-non-negatives) applied to per-site outputs. No global simulation needed; per-site snapshots suffice.
3. **Coordination-freeness corollary.** Because `O` is monotone in the input-set order, distributed sites can compute their local contribution without coordinating with other sites; the aggregator monotonically converges.

In CA-class vocabulary: CALM is the sub-class where (i) `Σ` carries a partial order with append-only update, (ii) `O` is a monoid-aggregate over per-site values, and (iii) the aggregator commutes with the local rule in the input-set order.

**Examples that fit:**
- Vector charge `Q_V = Σ_x ψ̄_x γ^0 ψ_x` on the particle-number-positive sector — non-negative density per site, monotone aggregation, no simulation needed.
- G-counter CRDT — exact CALM analog.

**Examples that don't fit (the rest of CA-class):**
- GW axial charge `Q_A` — signed density per site, instanton/anti-instanton cancellation (Section 4).
- Reversible CA conserved quantities — admit signed decomposition via block-CA structure but the readout depends on phase/parity of the block.
- Class-4 CA emergent invariants (Rule 110 long-range glider count) — no monotone aggregate works.

This sub-class structure is the operational content of the WRK-388 v2.1 signed-readout monotonicity criterion at the CA substrate level.

---

## 4. Relation to v3 9-tuple (compatible, not competing)

The CA-class hypothesis does not replace the v3 9-tuple; it locates one element of the tuple at a sharper substrate level.

| v3 tuple position | CA-class substrate interpretation |
|---|---|
| `C_U` (source category) | the category of CA-class substrates with structure-preserving local-rule maps |
| `U` (source object) | a specific substrate `S = (Σ, X, N, f)` |
| `ρ` (readout) | a CA-class observable `O : Σ^X → V` |
| `ex` (exactness) | whether `O` is literally a categorical object of `C_X` (exact), an ε-limit in a topology (ε-approx), a collapse functor (quotient), or protocol-mediated |
| `rr` (readout-reducibility) | the rr-axis applied to `O` as a CA-class projection: mono-red / signed-BV / phase-cancel / comp-irred |
| `arch = (P_O, E, r)` | CA substrate naturally supplies `E` (per-site state as monotone provenance, or block-CA evidence layer), `r` (the projection `O`), and `P_O` (observer protocol = how a finite observer collects per-site snapshots) |

The v3 9-tuple stays at the **categorical / meta-classification level**; the CA-class hypothesis stays at the **substrate / dynamics level**; the two compose vertically.

**[speculation]** The bet of WRK-395 is that the substrate-level formulation makes the rr-axis empirically testable (you can construct concrete CA, evolve them, measure observables) in ways the categorical statement alone cannot. That bet is tested in `rr-axis-empirical-validation.md`.

---

## 5. What this hypothesis predicts (testable claims)

If CA-class is the right superclass with CALM as monotone-reducible corner, then:

**P1 (testable).** The four rr values should be empirically distinguishable on actual CA observables — concrete CA + concrete observable should classify into exactly one cell.

**P2 (testable).** Reversible CA with conservation laws should sit at `rr = signed-BV` or `rr = monotone-reducible` (depending on whether the conservation is signed-decomposed).

**P3 (testable).** Class-4 CA observables (Rule 110 glider counts, Game of Life population evolution) should sit at `rr = comp-irred`.

**P4 (testable).** The GW axial-charge `Q_A` should admit a recoding as a CA-class observable, and the recoded observable should sit at `rr = signed-BV` (matching WRK-387's falsification).

**P5 (predictive / open).** No-go evasions on the GW bridge should live in `rr ∈ {signed-BV, phase-cancel, comp-irred}` rather than `rr = mono-red`. The BvN wall (WRK-389 v3) and the PCP-blindness (WRK-388 v2.1) should both be readable as CA-class structural obstructions.

P1-P4 are testable within the WRK-395 scope (Sections in `rr-axis-empirical-validation.md`). P5 is structural and tested via the BvN-vs-CI verdict (in `ci-vs-bvn-structural-verdict.md`).

---

## 6. Honest gaps (CA-class hypothesis specific)

- **[speculation]** "Local-rule substrate" generalizes CA but does not yet capture quantum CA (Heunen-Reyes, Arrighi-Nesme), continuous-state CA (coupled map lattices), or stochastic CA. WRK-395 stays within deterministic finite-alphabet CA.
- **[speculation]** The rr-axis is a typing of observables, not yet a proven mutually-exclusive partition. The empirical-test section sharpens the operational distinguishability but does not prove disjointness at the formal level.
- **[speculation]** "Substrate-agnostic" is aspirational. The WRK-388 v2.1 primitive is generator-weight on a fixed value group `G`; CA-class structure adds local-rule constraints. Whether the primitive is *unchanged* under CA-class restriction or *strengthened* is an open question.
- **[speculation]** The CA-class hypothesis does not by itself dissolve the v3 9-tuple's open universal-completeness conjecture; it relocates that conjecture into the substrate layer (does every no-go evasion correspond to some CA-class observable?).
- **No engagement with quantum-CA literature beyond noting it exists.** Heunen-Reyes-style quantum CA (relevant to WRK-389's quantum-escape direction) are out of scope for WRK-395; flagged for a future card.

---

End of `ca-class-hypothesis-precise.md`.
