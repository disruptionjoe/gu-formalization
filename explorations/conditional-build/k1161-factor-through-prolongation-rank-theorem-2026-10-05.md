---
title: "K1161 factor-through prolongation rank theorem"
status: active_research
doc_type: fixed_symbol_factorization_rank_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional fixed-covector theorem; no source operator or functional realization
manifest: lab/process/k1161-factor-through-prolongation-rank-theorem.json
probe: tests/channel-swings/k1161_factor_through_prolongation_rank_theorem_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1161 factor-through prolongation rank theorem

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> fixed-symbol theorem used on the source-epsilon target later. It does not
> identify that finite target with the K132 bulk carrier or construct a
> boundary differential.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: factor-through fixed-symbol rank ceiling
carrier: finite symbol fibre K inside V LAYER=toy CHIRALITY=N/A
pairing: none required for factorization theorem ON=fixed-covector
real_structure: real or complex finite coefficient space
grading: one base constraint channel and its descendant stack
action_owner: comparator -- source ownership required separately for every map
target: rank of a stacked differential symbol MAP-TYPE=evaluation
```

Let `q:V->W` and suppose that, at one fixed covector, every proposed
descendant has the form `Q_j=A_j q`. The stack factors as

```text
Q=(Q_1,...,Q_m)=S q,   S(w)=(A_1w,...,A_mw).
```

Therefore, for every subspace `K subset V`,

```text
rank(Q|K) <= rank(q|K) <= dim W.                         (1)
```

For ordinary scalar differential prolongations,
`sigma(D_j q)(xi)=p_j(xi)sigma(q)(xi)`. If some multiplier is nonzero, the
whole finite stack has exactly the same kernel as the base symbol; if all
multipliers vanish, its rank is zero. Derivative order, jet count and the
nominal dimension of the restacked target do not create new fixed-symbol
information.

This mechanism is held prior art inside the repository: K792 proves the
specific released redundancy `Xi=D_omega Upsilon` factors through the direct
`Upsilon` response at one flat zero-locus germ, and K880 proves its induced map
on the old quotient is zero. K1161 is the general finite-stack theorem needed
to test the different epsilon target; it is not a rediscovery claim.

An exact rank-two control remains rank two after three scalar descendants and
after a nontrivial operator-valued restacking. This theorem says nothing about
variable-coefficient lower terms, boundary traces, domains, or genuinely
independent principal symbols. Producer and probe pass `11/11` and `12/12`.
