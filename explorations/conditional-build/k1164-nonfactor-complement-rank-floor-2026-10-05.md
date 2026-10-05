---
title: "K1164 nonfactor complement rank floor"
status: active_research
doc_type: source_epsilon_nonfactor_complement_necessity
created: 2026-10-05
claim_ceiling: exact necessary independent-rank floor; no repair or source coupling constructed
manifest: lab/process/k1164-nonfactor-complement-rank-floor.json
probe: tests/channel-swings/k1164_nonfactor_complement_rank_floor_probe.py
target_claim: SC-ACT-06
---

# K1164 nonfactor complement rank floor

> **GU-COMPARATOR-ROUTING — scope before inference.** The base epsilon
> channel is granted maximal favorable rank. The complementary map remains
> hypothetical and does not become source-owned through this bound.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: irreducibly new rank required beyond a finite epsilon channel
carrier: K132 Hessian kernel at one causal covector LAYER=source-print CHIRALITY=N/A
pairing: K132 source Hessian ON=causal-covector-strata
real_structure: native real variables with ranks after complexification
grading: base epsilon channel plus hypothetical complementary constraint
action_owner: source-action -- complement unowned
target: radical capture by a combined constraint MAP-TYPE=restriction
```

For maps `q,R` on a subspace `K`, rank-nullity gives the exact split

```text
rank((q,R)|K)
  = rank(q|K) + rank(R|(K intersect ker q)).               (1)
```

Thus a required total rank `t` forces the genuinely new part to obey

```text
rank(R|(K intersect ker q)) >= t-rank(q|K).                (2)
```

If `R=Aq`, its restriction to `K intersect ker q` is zero. Applied to K132,
even granting the full 91 ranks to the moment map, a combined repair must add
at least `98379/98379/106543` independent nonnull/spacelike/null directions
invisible to that channel. Starting from the seven-invariant lock requires
`98463/98463/106627`.

These are necessary floors only. They do not supply ownership, `Qd=0`,
negative capture, propagation, radical equality, common domains, closed
range, uniform positivity or a maximal boundary generator. Producer and probe
pass `10/10` and `10/10`.
