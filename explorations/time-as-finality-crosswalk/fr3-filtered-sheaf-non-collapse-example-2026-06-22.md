---
title: "FR3 — Filtered-Sheaf Non-Collapse: An Explicit Toy Example"
status: exploration
doc_type: research
updated_at: "2026-06-22"
---

# FR3 — Filtered-Sheaf Non-Collapse: An Explicit Toy Example

**Status:** Exploration-grade worked example. Not canon. Not active research. Executes task FR3 from `NEXT-STEPS.md`: construct a minimal toy example where a sheaf `F` over a record space is assembled in filtration steps `F_tau`, and determine whether a transient apparent obstruction during assembly is structurally distinct from the final obstruction `H^1(X, F)`. The prior attempt (`filtered-sheaf-temporal-obstruction-2026-06-22.md`) concluded **collapse in all toy cases examined**, with the explicit condition for re-opening: *a non-collapse toy example.* This document supplies one.

**Provenance:** Run 4 (Topologist / Sheaf Theorist) of `five-run-issuance-rate-observer-contact-2026-06-22.md`; the filtered-sheaf formalization attempt; FR3 in `NEXT-STEPS.md`.

**Headline:** A non-collapse example **exists**. The prior verdict ("partially absorbed; collapses in all toy cases") is **overturned at the level of toy existence** — but, importantly, the non-collapse is a property of the *filtration by subsheaves over a fixed space*, not of *spatial assembly* (growing the space). This distinction is the actual content, and it sharpens rather than reverses the strategic conclusion.

---

## 1. The Gap in the Prior Collapse Argument

The prior document tested non-collapse with two examples:
- `X = R` (real line) assembled left-to-right: each stage `(-infinity, tau)` is contractible, so `O(tau) = 0` always. (Trivial.)
- `X = S^1` assembled as a growing arc `A(tau) subset S^1`: contractible until closure, obstruction appears only at closure. (Late-appearance, not transient.)

**Both examples assemble by growing the underlying space** — at stage `tau` the cohomology is computed over a *sub-space* `A(tau) subset X`. The candidate definition, however, was a *subsheaf* over the **fixed** space `X`:

```
O(tau) = H^1(X, F_tau),     F_tau subset F  a subsheaf over all of X.
```

These are **not the same construction.** Computing `H^1(A(tau), F)` over a growing subspace is governed by the topology of `A(tau)` (and collapses, as shown). Computing `H^1(X, F_tau)` over the *fixed* `X` with a *subsheaf* `F_tau` is governed by the inclusion of sheaves `F_tau hookrightarrow F`, and the induced map on cohomology **need not be injective or surjective.** Subsheaf inclusions have kernels and cokernels; the long exact sequence of the quotient `F / F_tau` controls them. The prior argument's "the obstruction is determined by the final sheaf" is true for the *final* sheaf's own cohomology but says nothing about whether the *subsheaf's* cohomology vanishes when the full sheaf's does.

**This is the gap.** A subsheaf of a sheaf with vanishing `H^1` can have non-vanishing `H^1`. We now build one explicitly.

---

## 2. The Toy Example

### 2.1 The space and the final sheaf

Let `X = S^1`, the circle, with its usual topology. Let `F = C` be a **flasque (flabby) resolution target** — concretely, take

```
F  =  the sheaf of C-valued functions on S^1 that are locally constant EXCEPT possibly
       with arbitrary values (the "discontinuous sections" sheaf, i.e. the sheaf of all
       set-theoretic functions U -> C).
```

This `F` is **flasque**: every section over an open set extends to all of `X` (just extend the function arbitrarily). Flasque sheaves are acyclic: `H^k(X, F) = 0` for all `k >= 1`. In particular

```
H^1(S^1, F) = 0.       (no final obstruction)
```

So `F` is a final assembled record with **no global coherence obstruction whatsoever**. Any collection of local sections glues (after arbitrary extension). This is the regime the prior document said could not host a transient obstruction.

### 2.2 The filtration by subsheaves

Now filter `F` by subsheaves indexed by assembly depth `tau`. Let assembly proceed by *imposing continuity constraints progressively*: the more the observer has assembled, the more its records are required to be locally consistent (continuous), until at the end the constraint is dropped and arbitrary extension is allowed.

Concretely, define a **two-stage** filtration (`tau in {1, 2}`, with `F_2 = F`):

```
F_1  =  the constant sheaf  C_{S^1}   (locally constant C-valued functions),
F_2  =  F  (all functions),       F_1 subset F_2 = F.
```

`F_1 = C_{S^1}` is the genuine constant sheaf on the circle. Its cohomology is the classical computation:

```
H^0(S^1, C_{S^1}) = C,      H^1(S^1, C_{S^1}) = C  (!= 0).
```

The `H^1(S^1, C) = C` is the standard circle obstruction (the circle is not simply connected; the constant sheaf has a degree-1 class).

### 2.3 The temporal obstruction does not collapse

Apply the candidate definition `O(tau) = H^1(X, F_tau)`:

```
O(1)  =  H^1(S^1, F_1)  =  H^1(S^1, C_{S^1})  =  C   != 0,
O(2)  =  H^1(S^1, F_2)  =  H^1(S^1, F)        =  0.
```

**This is exactly the non-collapse scenario the prior document defined and failed to find:**

```
O(tau_0) != 0   at the intermediate stage tau_0 = 1,
O(tau_1) =  0   at the final stage     tau_1 = 2,         tau_0 < tau_1.
```

A transient obstruction is **present at assembly depth 1 and resolved at assembly depth 2.** The partially assembled record (the locally-constant-constrained subsheaf `F_1`) is globally obstructed; the fully assembled record (the unconstrained sheaf `F`) is not. **Non-collapse confirmed by explicit computation.**

### 2.4 Why this happens (the exact sequence)

The mechanism is the long exact cohomology sequence of

```
0 -> F_1 -> F -> Q -> 0,      Q = F / F_1   (the quotient sheaf).
```

giving

```
... -> H^0(F) -> H^0(Q) --d--> H^1(F_1) -> H^1(F) -> ...
```

Since `F` is flasque, `H^1(F) = 0`, so the connecting map `d : H^0(Q) -> H^1(F_1)` is **surjective**. The intermediate obstruction `H^1(F_1) = C` is the image of global sections of the quotient `Q` that fail to lift to global sections of `F_1` even though they lift to `F`. In assembly terms: at stage 1 the observer's records are required to be locally constant, and a globally-consistent locally-constant record on the circle has a monodromy obstruction (`H^1 = C`); at stage 2 the observer is allowed arbitrary (discontinuous) extension, which kills the obstruction. The obstruction is genuinely transient — it is created by the *constraint* `F_1` and destroyed by *relaxing* it to `F`.

---

## 3. What the Non-Collapse Example Does and Does Not Establish

This is the crucial part. The example overturns the *toy-existence* claim but the careful reading **sharpens** the strategic verdict rather than reversing it.

### 3.1 It DOES establish

1. **A transient temporal obstruction exists as a well-defined formal object.** `tau |-> H^1(X, F_tau)` is a non-constant function of assembly depth, with a non-trivial value at an intermediate stage and zero at the final stage. The prior document's non-collapse condition is met. The filtered-sheaf temporal obstruction is **not** always absorbed into `H^1(X, F)`.

2. **The obstruction is sensitive to the assembly order, not just the final state.** Two observers with the same final sheaf `F` but different filtrations `F_tau` (different sequences of constraints) see different obstruction functions `O(tau)`. This is genuine assembly-dependence, formally realized.

3. **The mechanism is exact and general:** any filtration `F_tau subset F` where `F` is acyclic but some `F_tau` is not produces non-collapse, controlled by the connecting map `H^0(F/F_tau) -> H^1(F_tau)`. This is a reproducible recipe, not a one-off.

### 3.2 It does NOT establish

1. **The non-collapse is a property of *filtration by subsheaves*, not of *issuance rate*.** The filtration index `tau` here is the *amount of constraint imposed* (constant → arbitrary), not a *rate* of patch addition. The original issuance-rate story was about adding patches *faster or slower*; this example is about *which subsheaf* the observer's records currently satisfy. The rate `lambda` does not appear. So the example does **not** resurrect the issuance rate `lambda` as a structural parameter — it resurrects the *filtration* as a structural parameter. These are different: a filtration is a structural (order-theoretic) datum; a rate is a dynamical one. **The rate-independence finding survives intact** — the obstruction depends on the filtration's *content* (which constraints, in which order), not on the *speed* of assembly.

2. **The "assembly" here runs constraint-decreasing, which is physically backwards for a record-accumulating observer.** A record-bearing observer *accumulates* information: its records get *more* constrained (more consistency required) as it assembles, not less. The non-collapse example has `F_1` (more constrained) *before* `F` (less constrained) — i.e., the observer *relaxes* constraints over time. For an information-accumulating observer the natural filtration runs the other way (`F_tau` increasing in *content*, hence the sections become a *larger* subsheaf as `tau` grows). Whether non-collapse survives under the physically-correct *increasing* filtration is the sharper question, addressed next.

### 3.3 The physically-correct direction: does non-collapse survive?

For an information-accumulating observer, model the filtration as an **increasing** family of subsheaves `F_1 subset F_2 subset ... subset F` where `F_tau` is the subsheaf of records *finalized by stage tau* and `F = colim F_tau` is the fully assembled record. Now ask: can `H^1(X, F_tau) != 0` for some finite `tau` while `H^1(X, F) = 0`?

**Yes — the same example works, read forward.** Take `F_1 = C_{S^1}` (the observer's early records are locally constant — the cheapest consistent records), and let later stages *add* discontinuous sections until `F_tau` reaches the flasque `F`. Then `H^1(X, F_1) = C != 0` and `H^1(X, F) = 0`, with the increasing filtration `C_{S^1} subset F`. The obstruction is present early (when only locally-constant records exist) and is killed as richer (discontinuous-extension) records are admitted. This is non-collapse under an *increasing*, information-accumulating filtration. **Confirmed: non-collapse survives in the physically-correct direction.**

The general statement:

> **Non-collapse criterion (FR3).** A filtered record sheaf `{F_tau}` exhibits a genuine transient temporal obstruction iff the colimit sheaf `F = colim F_tau` is more acyclic than some finite stage, i.e. iff the inclusion `F_tau hookrightarrow F` induces a **non-injective** map `H^1(X, F_tau) -> H^1(X, F)` for some `tau` (equivalently, the connecting map from `H^0(X, F/F_tau)` hits a non-zero class in `H^1(X, F_tau)` that dies in `H^1(X, F)`). For `F` acyclic this is automatic whenever any `F_tau` has `H^1 != 0`.

### 3.4 So what is the residual after the sharpening?

The prior document's residual was: *"the temporal obstruction is process-level (dynamical), not structural; admissible at L6 as a parameter but not a new topological invariant."* The non-collapse example **revises** this:

- The transient obstruction `O(tau) = H^1(X, F_tau)` **is** a genuine, well-defined family of *topological* invariants (cohomology groups of honest subsheaves), **not** a mere dynamical label. The prior claim that it "does not add topological information beyond `H^1(X, F)`" is **false as stated** — it adds exactly the cohomology of the intermediate subsheaves, which is not determined by `H^1(X, F)`.
- **BUT** the indexing parameter is a *filtration* (a structural/order datum: a chain of subsheaves), **not a rate**. So the correct home is **not** L6 (coordination-loop dynamics, where rates live) but rather a refinement of **L1/L2**: the observer's record sheaf is filtered, and the filtration is part of the substrate-observer data. The temporal obstruction is the cohomology of this filtered object.

This is a real upgrade in understanding: the filtered-sheaf obstruction is **structural** (it is sheaf cohomology of subsheaves), but it is **not the issuance rate** (which remains a dynamical, rate-independent-confirmed concept). The two were conflated in Run 4's original framing. FR3 separates them.

---

## 4. Verdict

**FR3 verdict: NON-COLLAPSE EXAMPLE CONSTRUCTED. The prior collapse verdict is overturned at toy-existence level, with a sharpening that reassigns the object.**

Precise sub-claims:

1. **A transient temporal obstruction exists** (`O(1) = H^1(S^1, C) = C != 0`, `O(2) = H^1(S^1, F) = 0`), under both the constraint-decreasing and the physically-correct information-accumulating (increasing-subsheaf) filtration. The prior document's re-opening condition is satisfied.

2. **It is a structural object, not a dynamical one.** It is the cohomology of honest subsheaves over a fixed space. It carries information not determined by `H^1(X, F)`. This **corrects** the prior document's claim that the concept "does not add topological information."

3. **It is NOT the issuance rate.** The indexing parameter is the filtration (which subsheaf / which constraints), a structural datum, not the rate `lambda` of patch addition. **The rate-independence finding is untouched** — speed of assembly still does not enter; only the *content and order* of the filtration does.

4. **Therefore the home is a filtered refinement of L1/L2, not L6.** The filtered-sheaf temporal obstruction is admissible as a structural enrichment of the substrate-observer record sheaf (a filtered sheaf is more data than a sheaf), distinct from both the rate concept (L6, per FR4) and the bare topological obstruction (`H^1(X,F)`).

5. **GU-relevance remains exploration-grade and unproven.** No GU theorem currently consumes a filtered record sheaf. To earn active-research status, one would need (per the prior document's Section 7, criterion 3) a GU result that changes depending on the intermediate `O(tau)` — e.g., a chirality/anomaly readout that is sensitive to the observer's record *filtration* and not only to the final record. That construction does not yet exist. But the **formal object is now real**: a filtered observer-record sheaf with a non-trivial transient obstruction is a well-defined exploration target, no longer a concept that "collapses in all toy cases."

### 4.1 Why the sharpening matters (no overclaim)

It would be an overclaim to say "the issuance rate found a structural home in GU via filtered sheaves." It did not. What found a structural home is the **filtration** — a different object. The honest statement:

> The filtered-sheaf temporal obstruction is a genuine structural invariant (cohomology of intermediate subsheaves) that is *not* absorbed by `H^1(X, F)`. It is indexed by a filtration (structural), not by a rate (dynamical). It is therefore a candidate new exploration object in GU's record-sheaf formalism, **decoupled** from the issuance-rate concept, which remains rate-independent and absorbed/L6-bound per FR1, FR2, FR4.

This keeps every prior negative finding intact (rate-independence; `lambda_max` absorption) while honestly recording that the *filtered-sheaf* branch — contrary to the prior toy-case verdict — **does** host a genuine, computable, non-collapsing obstruction.

---

## 5. Verdict Summary

| question | answer |
|---|---|
| Does a non-collapse toy example exist? | **Yes.** `X = S^1`, `F_1 = C_{S^1}` (constant sheaf, `H^1 = C != 0`), `F = F_2` flasque (`H^1 = 0`). `O(1) != 0`, `O(2) = 0`. |
| Is the transient obstruction structural or merely dynamical? | **Structural.** It is the cohomology of honest subsheaves; not determined by `H^1(X, F)`. Corrects the prior document. |
| Does it survive the physically-correct (information-accumulating) filtration direction? | **Yes** — read forward as `C_{S^1} subset F` increasing. |
| Does it resurrect the issuance rate as a structural parameter? | **No.** The index is a *filtration* (structural), not a *rate* (dynamical). Rate-independence finding untouched. |
| Where does the object belong? | A **filtered refinement of L1/L2** (filtered record sheaf), distinct from the L6 rate concept (FR4) and from the bare `H^1(X,F)`. |
| Is it GU-relevant / promotable? | **Exploration-grade.** Formal object now real and computable; needs a GU result sensitive to `O(tau)` before active-research status. |

**FR3 verdict: NON-COLLAPSE CONFIRMED; OBJECT REASSIGNED.** The prior "collapses in all toy cases" verdict is overturned by explicit computation, and the object is correctly separated from the issuance rate: a genuine structural (filtration-indexed) transient obstruction exists, while the rate concept remains rate-independent and absorbed. This is a clean upgrade of the filtered-sheaf branch from "process-level, collapses" to "structural, non-collapsing, decoupled from rate, exploration-grade."

---

## Cross-References

- Task source: `NEXT-STEPS.md` (FR3)
- Prior attempt (collapse verdict, re-opening condition): `explorations/time-as-finality-crosswalk/filtered-sheaf-temporal-obstruction-2026-06-22.md`
- Run 4 origin: `explorations/time-as-finality-crosswalk/five-run-issuance-rate-observer-contact-2026-06-22.md`
- Rate-independence (untouched; the index here is a filtration not a rate): `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`
- L6 rate concept (distinct object): `explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`
- Promotion criteria (Section 7 of prior attempt): `explorations/time-as-finality-crosswalk/filtered-sheaf-temporal-obstruction-2026-06-22.md`
