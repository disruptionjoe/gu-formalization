---
title: "FR4 — L6 Issuance-Rate Parameterization: Cadence Field Spec and Failure-Mode Verdict"
status: exploration
doc_type: specification
updated_at: "2026-06-22"
---

# FR4 — L6 Issuance-Rate Parameterization: Cadence Field Spec and Failure-Mode Verdict

**Status:** Exploration-grade filled six-axis specification plus a failure-mode verdict. Not canon. Not active research. Executes task FR4 from `NEXT-STEPS.md`: if a six-axis candidate uses an observer-finality sub-protocol, test whether adding `cadence` as a new field (rate of record finalization) produces a different failure mode than L4 already captures.

**Provenance:** FR4 in `NEXT-STEPS.md`; the escape-hatch question handed forward by FR1 (`fr1-sorkin-absorption-worked-check-2026-06-22.md`, Section 4.3). FR1 showed that within example-02 as specified (completeness-gated finality, "No loop" at L6) `lambda_max` is fully absorbed by L4+L2, and that the only route to a non-absorbed rate is to change L6 from "No loop" to a deadline/cadence loop. FR4 tests exactly that change.

**Method:** Fill a six-axis candidate that is example-02 modified at a single axis — L6 changed from "No loop" to a cadence/deadline coordination loop — with the `cadence` field populated in the finality sub-protocol. Then ask whether the candidate's failure mode is **new** (not reachable under L4's completeness-gating) or **the same** failure mode L4 already captures. The verdict turns on whether deadline-gated finality is structurally distinct from completeness-gated finality.

---

## 1. The Candidate: Example-02-D (Deadline-Cadence Variant)

A single-axis modification of example-02 on L6.

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sorkin causal-set, deadline-cadence | Sorkin causal-set | Finite Turing (BPP/BQP) | Cauchy-slice-linearization | Sorkin partial order | Specific-object | **Dijkstra-style self-stabilizing finalization loop with a hard cadence deadline `Delta`** | Show a sprinkling-fidelity inconsistency that occurs *only* under deadline-forced finalization and *cannot* occur under completeness-gating; if every deadline-induced inconsistency is also reachable by completeness-gating, the cadence field adds no failure mode. |

L1-L5 are identical to example-02. The only change is L6: from "(a) No loop" to "(f) Dijkstra self-stabilizing protocol" specialized to a finalization loop with a hard deadline.

### 1.1 The finality sub-protocol, with the new `cadence` field

We instantiate the observer-finality sub-protocol fields (from `observer-finality-layer.md`) and **add the candidate `cadence` row**:

| field | example-02 (completeness-gated) | example-02-D (deadline-cadence) |
|---|---|---|
| record-bearing observer class | finite Turing machine | finite Turing machine |
| record type | finalized combinatorial invariant of a finite sub-causal-set | same |
| causal accessibility | finalize `x` once `J^-(x) cap W` is order-complete for the invariant | same accessibility, but finalization is **forced** by deadline (see cadence) |
| finality relation | `x` final when its relevant past is order-complete (**completeness-gated**) | `x` final at tick `arrival(x) + Delta`, whether or not its past is complete (**deadline-gated**) |
| readout target | causal-set chirality invariant | same |
| **`cadence` (new field)** | (absent; finalization deferred indefinitely until complete) | **`Delta` = max ticks a record may stay open before forced finalization** (rate of forced finalization = 1 record per `Delta` ticks of its lifetime) |
| failure mode | sprinkling-fidelity inconsistency: a finalized invariant changes when a later element is revealed in an already-closed past | **same surface symptom, but now reachable by a new mechanism — see Section 3** |

The `cadence` field `Delta` is the new degree of freedom. It is a *coordination-loop parameter*: it governs the dynamics that close records, which is exactly the L6 remit ("the feedback or dynamics that makes observer extraction well-defined").

---

## 2. Why This Is the Right Place to Test the Cadence Field

FR1 established two facts that jointly localize the cadence field to L6:

1. **The Sorkin order `prec` (L4) is rate-blind.** Completeness of `J^-(x)` is a predicate on the order, evaluated whenever the relevant elements are present. L4 imposes a *gating rule*, not a rate.
2. **The observer (L2) imposes a capacity ceiling**, `lambda_max = B / w`, but a *patient* (completeness-gated) observer never finalizes an incomplete past and so is correct at any rate below capacity.

Together these say: **the only thing that can make the issuance rate a load-bearing parameter is a rule that forces finalization before completeness.** Such a rule is neither an order property (L4) nor an observer-budget property (L2). It is a *coordination-loop policy*: "finalize within `Delta` ticks." That policy lives at L6. So if the cadence field has any non-redundant content, it must show up here, as a distinct failure mode of example-02-D versus example-02.

---

## 3. The Failure-Mode Analysis

We compare the failure modes of the two candidates.

### 3.1 Completeness-gated failure mode (example-02, recap)

Under completeness-gating, the observer finalizes `x` only when `J^-(x) cap W` is order-complete for the invariant. The failure mode (from FR1) is triggered **only by eviction under capacity overload**: if `lambda > lambda_max`, the open frontier overflows memory, an open record is evicted, and its past later completes after eviction — producing an inconsistency.

Key property: **at any `lambda <= lambda_max`, the completeness-gated observer has NO failure mode.** It is exactly correct. The only failure is the L2-capacity eviction, already absorbed by FR1.

### 3.2 Deadline-gated failure mode (example-02-D)

Under deadline-gating with cadence `Delta`, the observer finalizes `x` at tick `arrival(x) + Delta` **whether or not `J^-(x)` is complete**. Define the *late-past event*: an element `y` with `y prec x` that arrives at the observer *after* tick `arrival(x) + Delta`. When a late-past event occurs:

- The observer has already finalized `I(x)` from an **incomplete** past `J^-(x) cap W_{arrival(x)+Delta}`.
- The true invariant `I(x)` computed from the complete past `J^-(x)` differs.
- **The finalized record is wrong, even though the observer was operating below its capacity ceiling `lambda_max` and never evicted anything.**

This is a **structurally new failure mode.** It is not an eviction effect. It is a *premature-commitment* effect: the deadline forced a finalization on an incomplete past.

### 3.3 The decisive structural distinction

**Claim (FR4 core).** The deadline-gated failure mode is NOT reachable under completeness-gating, and is NOT captured by L4. Therefore the cadence field `Delta` produces a genuinely distinct failure mode.

**Proof of non-reachability under completeness-gating.** Under completeness-gating, a record of `x` is finalized only when no later-arriving element can land in `J^-(x)`. By construction, a completeness-gated finalization is never invalidated by a late-past event — there are no late-past events relative to a complete past, because completeness *is* the absence of future past-elements. So the premature-commitment failure mode has empty extension under completeness-gating. It is reachable only when finalization can occur before completeness, i.e., only under a deadline. QED.

**Proof that L4 does not capture it.** L4 supplies the partial order `prec` and the completeness predicate. The completeness predicate evaluates to false at the moment of a deadline-forced finalization on an incomplete past — but the deadline policy *overrides* the predicate. The failure is produced by the override (an L6 policy), not by the order. L4 has no parameter that forces finalization; the forcing is `Delta`, an L6 field. Therefore L4 does not contain the failure mode; it only contains the predicate that the L6 policy chose to violate. QED.

### 3.4 Sharpened: the cadence field changes the *type* of the failure, not just its trigger

Under completeness-gating the only failure is **capacity overload** (a quantitative L2 effect: too many open records). Under deadline-gating a new failure appears: **premature commitment** (a qualitative L6 effect: a finalized record that contradicts its own completed past). These are different in type:

| | trigger | controlling axis | symptom |
|---|---|---|---|
| capacity overload | `lambda > B/w` | L2 (budget) | open frontier overflows; record evicted then past completes |
| premature commitment | a late-past event after deadline `Delta` | L6 (cadence policy) | record finalized on incomplete past; later contradicted |

Crucially, **premature commitment can occur at arbitrarily low `lambda`.** Even a single element arriving slowly can have a late-past event if `Delta` is shorter than the gap to its last past-element. So the new failure mode is not a high-rate phenomenon (unlike capacity overload). It is a *mismatch between the deadline `Delta` and the order's past-completion latency*. This is a genuinely new degree of freedom: the relationship between `Delta` (L6) and the order's completion latency (L4) is not fixed by either axis alone.

---

## 4. The Verdict

**FR4 verdict: the `cadence` field `Delta` DOES produce a distinct failure mode — but it is an L6 field, not a repair of L4, and it does NOT overturn the FR1 absorption result.**

Three precise sub-claims:

1. **Cadence is a real, non-redundant L6 field.** Adding `Delta` introduces the premature-commitment failure mode, which is structurally absent under completeness-gating and not captured by L4. So `Delta` is not a redundant relabeling of an L4 or L2 quantity. It earns a place in the observer-finality sub-protocol **as an L6 field**, conditional on the candidate using a deadline-gated (not completeness-gated) finality relation.

2. **This does NOT contradict FR1.** FR1 showed that `lambda_max` — the *capacity-overload* threshold — is absorbed by L4+L2. FR4 shows that a *different* quantity — the deadline `Delta` and its mismatch with the order's completion latency — is a new L6 field. These are different objects: `lambda_max` is a rate ceiling (L2 capacity); `Delta` is a finalization-deadline policy (L6 coordination loop). FR1's "absorbed" verdict stands for `lambda_max`; FR4's "new field" verdict is for `Delta`. The five-run synthesis' Run 5 was right that the issuance-rate family, where it has non-redundant content, **belongs to L6** — FR4 confirms this with a concrete distinct failure mode.

3. **But the new field is exploration-grade and does not yet change any GU result.** The premature-commitment failure mode is real for the example-02-D candidate, but:
   - It is a failure of the *observer's record protocol*, not of the substrate or of any no-go theorem. It tells the observer "do not deadline-gate finality on a Sorkin substrate unless `Delta` exceeds the worst-case past-completion latency."
   - No GU theorem (signed-readout criterion, no-go class-relative map) changes value depending on `Delta`. Consistent with the rate-independence negative finding, the *structural* theorems remain `Delta`-independent; `Delta` only governs whether the observer's *record-construction process* succeeds.
   - Therefore `cadence`/`Delta` is admissible as an **exploration-grade L6 sub-protocol field**, useful as a falsification scaffold (it catches a real protocol error), but it is **not** a candidate for canon and does not bypass any no-go theorem.

### 4.1 The promotion condition for the cadence field

Per `observer-finality-layer.md`, the sub-protocol can move toward canon "only after at least two worked six-axis examples show that the added fields catch real errors or produce useful falsification tests." The `cadence` field now has **one** such worked example (example-02-D: it catches the premature-commitment error). A second worked example, on a non-Sorkin substrate (e.g., a CALM-monotonic L4 or a Type II_1 L1 candidate that uses deadline-gated rendering), would be required before the cadence field could be proposed for the canonical sub-protocol. Until then it is an exploration-grade field.

---

## 5. The Filled Spec Row (Contract Form)

For the repo's navigation contract, the filled candidate is:

```
candidate:               Sorkin causal-set, deadline-cadence (example-02-D)
L1 substrate:            Sorkin causal-set
L2 observer:             Finite Turing (BPP/BQP)
L3 pairing:              Cauchy-slice-linearization
L4 causal order:         Sorkin partial order
L5 emergence:            Specific-object
L6 coordination loop:    Dijkstra self-stabilizing finalization loop, hard cadence deadline Delta
cadence (sub-protocol):  Delta = max open-record lifetime in observer ticks
first falsification:     Exhibit a late-past event after Delta that contradicts a finalized
                         record (premature commitment). Confirmed reachable; NOT reachable
                         under completeness-gating. => cadence is a non-redundant L6 field.
new failure mode:        Premature commitment (finalize incomplete past), distinct in type
                         from capacity overload; occurs at any lambda when Delta < past-
                         completion latency.
GU-relevance:            None at present. No GU theorem depends on Delta. Exploration-grade
                         L6 field; catches a real protocol error; not canon; bypasses no
                         no-go theorem.
```

---

## 6. Verdict Summary

| question | answer |
|---|---|
| Does adding a `cadence` field produce a different failure mode than L4 captures? | **Yes.** Deadline-gating introduces *premature commitment*, structurally absent under L4's completeness-gating. |
| Is `cadence`/`Delta` a redundant relabeling of an L4 or L2 quantity? | **No.** It is a distinct L6 coordination-loop policy; the new failure occurs at any rate, controlled by the `Delta`-vs-completion-latency mismatch. |
| Does this overturn the FR1 absorption verdict? | **No.** FR1's absorbed object is `lambda_max` (L2 capacity ceiling). FR4's new object is `Delta` (L6 deadline policy). Different quantities; both verdicts stand. |
| Does any GU result change with `Delta`? | **No.** Structural theorems remain rate/deadline-independent (consistent with the rate-independence finding). `Delta` governs only the observer's record-construction process. |
| Status of the cadence field? | **Exploration-grade L6 sub-protocol field.** One worked example (catches premature commitment); needs a second non-Sorkin example before any promotion. Not canon; bypasses no no-go theorem. |

**FR4 verdict: NEW FIELD CONFIRMED AT L6 (cadence/`Delta`), with a distinct failure mode (premature commitment), but exploration-grade only and with no current GU-result dependence.** This precisely confirms Run 5's structural placement of the issuance-rate family at L6 while respecting the rate-independence negative finding: the field is real at the *process* layer (record construction) and absent at the *structural* layer (GU theorems).

---

## Cross-References

- Task source: `NEXT-STEPS.md` (FR4)
- Predecessor handing forward the L6 question: `fr1-sorkin-absorption-worked-check-2026-06-22.md` (Section 4.3)
- Observer-finality sub-protocol (fields + promotion condition): `explorations/time-as-finality-crosswalk/observer-finality-layer.md`
- Example-02 base candidate: `specifications/six-axis/examples/example-02-sorkin-causal-set.md`
- Six-axis template (L6 menu, item (f) Dijkstra self-stabilizing): `specifications/six-axis/six-axis-template.md`
- Rate-independence (structural theorems stay rate/deadline-independent): `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`
- Run 5 L6 placement claim: `explorations/time-as-finality-crosswalk/five-run-issuance-rate-observer-contact-2026-06-22.md`
