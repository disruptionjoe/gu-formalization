---
title: "K1116 mixed-zero-block positivity obstruction"
status: active_research
doc_type: source_hessian_mixed_zero_block_positivity_obstruction
created: 2026-10-05
claim_ceiling: exact local finite-symbol or common-form-domain obstruction
manifest: lab/process/k1116-k128-mixed-zero-block-positivity-obstruction.json
probe: tests/channel-swings/k1116_k128_mixed_zero_block_positivity_obstruction_probe.py
target_claim: K128-T0-I1B-HESSIAN-POSITIVITY
---

# K1116 mixed-zero-block positivity obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This applies exact linear
> algebra to K128's source-native local action Hessian. It is not a global GU
> vacuum, closed-domain or physical-positivity theorem. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact positivity obstruction for the K128 mixed zero block
carrier: horizontal metric variations plus distortion variations LAYER=source-print CHIRALITY=N/A
pairing: self-adjoint source Hessian form ON=common_finite_symbol_or_form_domain
real_structure: source-native real form
grading: metric and distortion blocks
action_owner: source-action -- source-native I1B local T=0 quadratic germ
target: K128 coupled Hessian positivity MAP-TYPE=evaluation
```

Let

```text
H = [[0,A*],[A,C]]
q(x,y)=2 Re<Ax,y>+<Cy,y>.
```

If `Ax != 0`, choose `y=+/- epsilon Ax`. The mixed term is linear in
`epsilon`, changes sign, and dominates the `C` term, which is quadratic, for
sufficiently small `epsilon`. Therefore a self-adjoint `H` is positive
semidefinite exactly when `A=0` and `C>=0`; the negative-semidefinite statement
is the sign-reversed analogue.

The exact scalar fixture `A=2`, `C=5`, `epsilon=1/10` gives
`q(1,+epsilon)=9/20` and `q(1,-epsilon)=-7/20`. K128's nonzero source mixed
block therefore forbids semidefiniteness before any additional constraint or
cohomological reduction. This does not construct that reduction or a closed
operator domain.

The producer passes `10/10`; the hostile probe rejects `10/10` mutations.
