---
title: "Second adapter contract (directed arrows) + the one-posit terminus: the whole bit reduces to 'final = positive-norm'"
status: exploration
doc_type: cross-repo-adapter-contract
created: 2026-07-15
grade: "adapter #2 HOLDS at structural grade (lighter than #1's Harary theorem -- a structural correspondence, flagged for hardening). Is-the-arrow-canonical: AXIS canonical (given finality irreversibility/T18; T57 caveat), POLARITY not canonical. Terminus: the value reduces to exactly ONE irreducible posit = Krein positivity. Identity now Joe-RATIFIABLE (>=2 contracts met); still Joe's gate."
provenance: "Joe, chat 2026-07-15: authorized moving the gated identity forward; run the second adapter contract + is-the-arrow-canonical test."
depends_on:
  - explorations/time-as-finality-crosswalk/adapter-contract-three-object-signed-graph-2026-07-15.md
  - explorations/time-as-finality-crosswalk/ti-question-finality-orientation-as-krein-sign-2026-07-15.md
runnable:
  - explorations/time-as-finality-crosswalk/adapter2_directed_arrow.py
verdict: "Adapter #2 holds (structural). Axis canonical, polarity is the one free Z/2 = 'final = positive-norm' = Krein positivity, reached constructively. >=2 adapter contracts now proven -> the identity bar(b) = finality orientation is Joe-RATIFIABLE."
---

# Second adapter contract + the one-posit terminus

## (A) Adapter #2 — the directed arrows are one object (structural)

Adapter #1 fused the **undirected** consistency objects. The value lives in the **directed** finality arrow.
Modelling both **TI `Ext_S`** (directed extension morphisms) and **TaF T18** (finalization increases a D1
dimension; reverse impossible; acyclic) as an **acyclic DAG with a monotone potential** (a finality poset):

```
instances: 300 | canonical monotone axis exists (acyclic): 300/300
```

Both instantiate the same object: **a finality poset with an intrinsic increasing axis.** So **adapter #2
HOLDS at structural grade.**

**Honest weighting.** This is *lighter* than adapter #1. #1 was Harary's balance theorem verified by three
independent algorithms (720/720) — a named theorem. #2 is a **structural correspondence** ("both are
acyclic-monotone finality posets"), not a deep theorem. It genuinely meets the tri-repo "second adapter
contract" bar in letter, but a hostile reviewer would want it hardened (an explicit functor `Ext_S -> T18`
preserving the monotone). Flagged.

## (B) Is-the-arrow-canonical — AXIS yes, POLARITY no

- **Axis: canonical (derived).** Acyclicity gives a monotone; the increasing direction is intrinsic. The
  computation is honest that *bare topology is flip-symmetric* — the asymmetry ("which way is final") comes
  from the monotone **semantics** (T18 "reverse impossible" / D1-increase), which is finality
  **irreversibility**, a physically robust fact. (Caveat: TaF's own **T57** flags a residual open question on
  the source/target arrow direction; so "axis canonical" is *given T18's monotone*, with T57 as the honest
  edge.)
- **Polarity: NOT canonical (the free bit).**

```
BOTH polarities (final=+ AND final=-) structurally admissible: 200/200
unique-genesis instances: 200 | of those, polarity STILL free: 200/200
```

Both sign conventions (final=+ vs final=−) satisfy every structural predicate, and **even a unique genesis**
fixes only *where* to anchor, not the anchor's sign. So the map (axis → ℤ/2 sign) carries **exactly one free
ℤ/2**.

## The terminus

The whole chain now closes:

> **consistency** (no domains) = shared object, proven (adapter #1) ·
> **finality axis** (the direction) = shared object + derived from irreversibility (adapter #2 + T18) ·
> **polarity** (which end is positive-norm) = **exactly one irreducible posit** = **Krein positivity**,
> i.e. "the final / settled direction is positive-norm."

Everything except that single posit is **derived or shared across the three repos.** This is W211's
"posit positivity, everything else forced" and persona-20's ceiling ("which sign given positivity") — now
reached **constructively**, with the posit *located* (the polarity on the finality axis) rather than merely
asserted.

**What this means honestly.** The generation-count sign is **not** arbitrary numerology, **not** a free
parameter, and **not** derived-from-nothing. It is **one physically meaningful choice** — final = positive-
norm — with literally everything else (consistency, the finality axis, the tri-repo structure) forced. That
is the honest answer to "what is this bit."

## Governance

`>= 2` adapter contracts are now proven (signed-graph consistency #1 + directed finality poset #2), so the
tri-repo precondition for the cross-repo identity is **met**. The identity

> **bar(b) (Krein sign) = the polarity of the finality axis**

is therefore **Joe-RATIFIABLE** — no longer premature on the contract count. It remains **Joe's gate** (a
verdict flip). Two honest riders for the ratification decision: (i) adapter #2 is structural-grade and lighter
than #1 (hardening available); (ii) the residual posit (Krein positivity) is **not** discharged by the
identity — it is *located*, not derived (`Issue[S]^physical=false`; generation number still source-action-
gated).
