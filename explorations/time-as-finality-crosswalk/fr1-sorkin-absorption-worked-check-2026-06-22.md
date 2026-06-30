---
title: "FR1 — Sorkin Absorption Test: Worked Check on Example-02"
status: exploration
doc_type: research
updated_at: "2026-06-22"
---

# FR1 — Sorkin Absorption Test: Worked Check on Example-02

**Status:** Exploration-grade worked check. Not canon. Not active research. Executes task FR1 from `NEXT-STEPS.md`: take the Sorkin causal-set observer (example-02 of the six-axis examples) and determine whether the maximum issuance rate `lambda_max` — the maximum rate at which new causal-set elements can be added to the observer's past cone while preserving the finality relation — is determined entirely by L4 (Sorkin partial order) + L2 (finite Turing observer class), or whether it requires a new field in the observer-finality sub-protocol.

**Provenance:** Run 1 (GU Formalist), "Heterodox next step," and the "Recommended Next Step" of `five-run-issuance-rate-observer-contact-2026-06-22.md`. The five-run synthesis flagged this as the bounded test that produces a clean yes/no on the absorption question for the Sorkin lane.

**Method:** This is a derivation, not a survey. We fix the example-02 sextuple, define `lambda_max` operationally on the causal-set substrate, and attempt to derive it from L4 and L2 alone. If the derivation closes, `lambda_max` is absorbed. If it requires a parameter not supplied by L4 or L2, that parameter is the new field.

---

## 1. Fixing the Example-02 Sextuple

From `lab/specifications/six-axis/examples/example-02-sorkin-causal-set.md`, the candidate is:

| axis | filling |
|---|---|
| L1 substrate | Sorkin causal-set `(C, prec)`, locally finite poset |
| L2 observer | Finite Turing (BPP / BQP) |
| L3 pairing | Cauchy-slice-linearization (smooth approximant via sprinkling fidelity) |
| L4 causal order | Sorkin partial order `prec` (L1 and L4 coupled) |
| L5 emergence | Specific-object substrate |
| L6 coordination loop | No loop |

The observer-finality sub-protocol fields (from `observer-finality-layer.md`), instantiated for this candidate:

| field | example-02 instantiation |
|---|---|
| record-bearing observer class | finite Turing machine reading finite chunks of `C` |
| record type | finalized combinatorial invariants of a finite sub-causal-set (chains, antichains, interval-abundance counts) |
| causal accessibility | the observer can finalize a record of element `x` only once all elements of the past `J^-(x) = { y : y prec x }` relevant to the invariant are present |
| finality relation | a record of `x` is final when `x`'s past set within the observer's window is order-complete (no later-arriving element can change `x`'s already-computed invariants) |
| readout target | causal-set chirality invariant (Cauchy-slice-linearization image) |
| failure mode | a sprinkling-fidelity inconsistency: an invariant the observer finalized changes when a later element is revealed to belong to a past it had already closed |

This last failure-mode row is the load-bearing one for the absorption test. `lambda_max` is, by definition, the largest element-addition rate at which the failure mode is **not** triggered.

---

## 2. Operational Definition of `lambda_max` for a Causal Set

We must define `lambda_max` without importing TaF vocabulary. Use only causal-set-native and observer-class-native quantities.

**Element addition.** The substrate is grown (or revealed to the observer) by adding elements to `C`. In the Rideout-Sorkin classical sequential growth (CSG) frame, elements are born one at a time; element `n+1` is added to the future of some subset of the existing `n` elements (an order-preserving birth). For the observer-revelation reading (substrate fixed, observer scanning it), "addition" means a new element of the fixed `C` enters the observer's accessible window.

Either reading gives the same kinematic object: a sequence of elements `x_1, x_2, ...` arriving at the observer, each carrying its set of order-relations to already-present elements.

**Issuance rate.** Let the observer operate on a discrete tick clock (its own computational step counter — an L2-native quantity, not a substrate time). Let `lambda` be the number of new elements arriving per observer tick. We seek the maximum `lambda` such that the observer's finalized records remain valid, i.e., the failure mode is never triggered.

**The finality relation, made precise.** The observer finalizes the record of element `x` when, for the invariant `I` being read out, the value `I(x)` computed from the currently-present past `J^-(x) cap W` (where `W` is the observer's window) equals the value that would be computed from the true full past `J^-(x)`. Finality means: **no later-arriving element can land in `x`'s past and change `I(x)`.**

`lambda_max` is the supremum of `lambda` for which every finalized record is permanently valid.

---

## 3. Derivation Attempt: Is `lambda_max` Fixed by L4 + L2?

We now try to pin `lambda_max` using only (i) the Sorkin partial order `prec` (L4) and (ii) the finite-Turing observer's per-tick compute budget (L2). We proceed by isolating the two independent constraints that bound `lambda` from above, and check whether their minimum **is** `lambda_max` or leaves a residual.

### 3.1 Constraint A — the causal-order constraint (pure L4)

**Claim A.** The Sorkin partial order alone imposes a finalization constraint, but it is a *completeness* constraint, not a *rate* constraint.

The finality of `x`'s record depends on whether `x`'s past is order-complete in the observer's window. In a locally finite poset, every element has a **finite** past: `|J^-(x)| < infinity`. So for any fixed `x`, there is a finite number `p(x) = |J^-(x)|` of elements that must be present before `x`'s record can be final.

Crucially: whether `x`'s past is complete is a **predicate on the order**, not a function of how fast elements arrive. Element `x`'s record becomes final at the arrival tick of the **last** element of `J^-(x)`, regardless of the rate. If elements arrive fast, the past completes in few ticks; if slow, in many ticks. **The order determines *which* arrivals matter; it does not determine a maximum rate.**

This reproduces, on the Sorkin substrate, the structural finding of the rate-independence worked check (`rate-independence-worked-check-2026-06-22.md`): the order relation `e <= e'` is rate-blind. Here `prec` is likewise rate-blind: completeness of `J^-(x)` is a fact about `prec`, evaluated whenever the relevant elements happen to be present.

**Therefore L4 alone yields no finite `lambda_max`.** L4 yields a *correctness condition* ("do not finalize `x` until `J^-(x) cap W` is order-complete for the invariant"), which is a **gating rule**, not a rate ceiling. An observer that obeys the gating rule never triggers the failure mode *at any arrival rate* — it simply waits. So if the observer is permitted to defer finalization, `lambda_max = infinity` from L4's standpoint: any rate is safe because the observer finalizes only complete pasts.

This is a sharp and slightly surprising sub-result: **the causal order does not cap the issuance rate at all, as long as the observer is allowed to hold records open until their pasts complete.** The cap, if any, must come from somewhere else: the observer's finite capacity to hold open records.

### 3.2 Constraint B — the observer-capacity constraint (pure L2)

**Claim B.** The finite-Turing observer (L2) *does* impose a finite rate ceiling, and it comes from bounded memory / bounded per-tick compute, not from the order.

The observer must hold, at each tick, the set of **open** (not-yet-final) records — every element `x` whose past is not yet order-complete in the window. Call this the *open frontier* `O(t)` at tick `t`. Each open record costs storage (the partial past accumulated so far) and per-tick compute (re-checking, on each new arrival, whether any open record's past has just completed).

Let:
- `mu` = the observer's per-tick finalization throughput: the number of records it can complete-and-finalize per tick, bounded by its compute budget `B` divided by the worst-case per-record finalization cost `w`. So `mu = B / w`, an L2-native quantity.
- `lambda` = arrivals per tick.

Each arrival opens (at most) one new record and may complete some open ones. By a Little's-Law / queue-stability argument (and this is exactly the M/M/1-style bound Run 2 flagged, here *derived* from L2 rather than imported):

```
The open frontier |O(t)| stays bounded   <=>   lambda <= mu = B / w.
```

If `lambda > mu`, the open frontier grows without bound: the observer accumulates open records faster than it can finalize them. Since the observer has finite memory `M`, once `|O(t)| > M / (storage per open record)`, the observer must drop open records. A dropped open record can never be finalized correctly — its past may complete after it has been evicted — and **this is precisely the failure mode**: the observer reports a record (or fails to report one) inconsistent with the true past.

**Therefore the rate ceiling is**

```
lambda_max = mu = B / w
```

an entirely **L2-native** quantity: `B` is the observer's compute/memory budget, `w` is the worst-case per-record finalization cost. No new field is needed to express it; it is `compute-budget(O) / w`, the bound Run 2 and Run 5 already anticipated.

### 3.3 Where does `w` come from? (The one place L4 re-enters)

The per-record cost `w` is not a free parameter. It is set by the *complexity of the finality check*, which is itself determined by the order `prec`. Specifically, `w` is the worst-case cost of verifying that `J^-(x) cap W` is order-complete and computing the invariant on it. For an invariant computable in time polynomial in `p(x) = |J^-(x)|` (true for chain/antichain/interval-abundance counts — all in P), we have

```
w = poly( max_x |J^-(x) cap W| ).
```

The quantity `max_x |J^-(x) cap W|` — the largest relevant past in the window — is a property of `prec` (L4). So:

```
lambda_max  =  B / poly( max-past-size(prec, W) )
            =  (L2 budget) / poly( L4 structure ).
```

**Both inputs are accounted for: the numerator is L2, the denominator is L4. There is no third input.**

---

## 4. The Verdict on Absorption

**`lambda_max` is fully absorbed by L4 + L2. No new field is required in the observer-finality sub-protocol.**

The derivation closes with exactly two inputs:

| quantity | source axis | role |
|---|---|---|
| `B` (compute/memory budget) | L2 (finite Turing class) | numerator of the rate ceiling |
| `max-past-size(prec, W)` (largest relevant past) | L4 (Sorkin partial order) | sets per-record cost `w` (denominator) |

```
lambda_max  =  B / poly( max-past-size(prec, W) ).
```

There is no residual quantity. The finite Turing observer's budget over the order-determined per-record cost gives the rate ceiling exactly. Adding a `cadence` field to the sub-protocol to name `lambda_max` would be **redundant**: it would be a defined function of fields the protocol already determines via L2 and L4.

### 4.1 The sharpened structural reason

The deeper reason the absorption is clean: **the causal order is rate-blind and the observer is rate-limited.** These two facts decompose the issuance-rate question with no remainder:

- L4 answers *which* elements must be present for a record to be final (a completeness predicate, rate-blind). It imposes no rate ceiling on its own — a patient observer is safe at any rate.
- L2 answers *how many* open records the observer can carry and finalize per tick (a capacity, rate-limited). It imposes the entire rate ceiling.

The issuance rate is therefore a derived quantity: it is the point at which L2's finite capacity, loaded with L4's order-determined per-record cost, saturates. It is not a primitive of either axis and not a new primitive of its own.

### 4.2 Relation to Run 1's conditional theorem-claim

Run 1 stated a conditional theorem-claim candidate: *"For any L2 observer class with finite Turing complexity and L4 = Sorkin partial order, the maximum finalization cadence is bounded above by the observer's causal horizon width. If TaF's `lambda_max` coincides with this bound, D2 adds no new constraint; if `lambda_max` is strictly tighter, D2 adds a new formal obligation."*

This worked check **discharges the conditional in the "no new constraint" direction, but corrects the bounding quantity.** Run 1 guessed the bound was "causal horizon width." The derivation shows the bound is actually `B / poly(max-past-size)` — a ratio of L2 budget to L4 past-size, not a horizon width per se. (In a Lorentzian approximant the past-size does scale with the past-cone volume, so "horizon width" is a coarse proxy, but the exact bound is the compute-budget-over-past-cost ratio.) The correction matters: it shows the cap is genuinely a *joint* L2-and-L4 quantity, not a pure-L4 geometric quantity. There is no room for a TaF-specific `lambda_max` that is "strictly tighter," because any tightening would have to enter through `B` or through `w`, both already named.

### 4.3 The one escape hatch, and why it is closed for example-02

The derivation assumed the observer **may defer finalization** (hold a record open until its past completes). If instead the protocol **forced** the observer to finalize each record within a fixed number of ticks of the element's arrival — a *hard deadline* — then a genuinely new parameter (the deadline) would enter, and `lambda_max` could be tighter than `B/w`. But:

1. Example-02's L6 is "No loop" and its finality relation is *completeness-gated*, not *deadline-gated*. There is no deadline in the candidate.
2. Imposing a deadline would be adding a new field — but it would be a **coordination-loop (L6)** field, not an L4 or L2 field, and it would move the candidate off the "No loop" L6 setting.

So the escape hatch confirms rather than undermines the verdict: *within example-02 as specified* (completeness-gated finality, no loop), `lambda_max` is absorbed by L4+L2. The only way to make `lambda_max` independent is to **change L6** — which is exactly what FR4 tests. This worked check therefore hands a sharp question to FR4: does a cadence/deadline field, added at L6, produce a failure mode that L4's completeness-gating does not already cover?

---

## 5. Failure Modes That Would Have Overturned This Verdict

For audit transparency, the verdict would have been "new field required" if any of the following had held:

1. **If the finality check cost `w` depended on a quantity outside `prec` and `B`** — e.g., on the arrival schedule itself. It does not: `w` is the cost of an order-completeness predicate plus a poly-time invariant, both functions of `prec`.
2. **If the order `prec` imposed its own rate ceiling** independent of observer capacity. It does not: completeness is rate-blind (Section 3.1).
3. **If a deferred-finalization observer could still trigger the failure mode at low rates.** It cannot: a patient, completeness-gated observer never finalizes an incomplete past, so it is correct at any rate below its capacity ceiling.

None held. The verdict is robust within the stated candidate.

---

## 6. Verdict Summary

| question | answer |
|---|---|
| Is `lambda_max` defined for the Sorkin example-02 observer? | Yes: `lambda_max = B / poly(max-past-size(prec, W))`. |
| Is it determined entirely by L4 + L2? | **Yes.** Numerator = L2 budget; denominator = L4 order structure. No third input. |
| Does it require a new field in the observer-finality sub-protocol? | **No.** It is a derived function of fields L2 and L4 already supply. |
| Does the causal order alone cap the rate? | **No** — surprising sub-result: `prec` is rate-blind; a patient observer is safe at any rate. The cap is entirely an L2 capacity effect, loaded with L4-determined per-record cost. |
| What is the only route to a non-absorbed `lambda_max`? | Change L6 from "No loop" to a deadline/cadence loop. Handed to FR4. |

**FR1 verdict: ABSORBED (confirmed, not conditional).** The five-run analysis' suspected L4+L2 absorption is now derived for the Sorkin lane, with the bounding quantity corrected from "causal horizon width" to `B / poly(max-past-size)`. The D2/issuance-rate note's Sorkin contact can be closed as absorbed. The residual question (does a cadence field at L6 add a distinct failure mode?) is the subject of FR4.

---

## Cross-References

- Task source: `NEXT-STEPS.md` (FR1) and "Recommended Next Step" of `five-run-issuance-rate-observer-contact-2026-06-22.md`
- Example-02 sextuple: `lab/specifications/six-axis/examples/example-02-sorkin-causal-set.md`
- Observer-finality sub-protocol: `explorations/time-as-finality-crosswalk/observer-finality-layer.md`
- Rate-independence worked check (rate-blindness of the order): `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`
- Hands the L6 question to: FR4 (`fr4-l6-cadence-parameterization-2026-06-22.md`)
- Six-axis template (L6 = coordination loop): `lab/specifications/six-axis/six-axis-template.md`
