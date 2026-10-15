---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-14"
---

# K1816--K1820: complete value and gradient banks narrow the stationary frontier

## Result

K1816 now contains the complete atomic, digest-checked fixed K1787-score bank
on all 78 exact K1796 slab-three leaves. The selected uniform configuration is
parameter order eight, observation order fourteen and 88 rational observation
cells of half-width `1/4`. It proves strict compact margins on exactly 26
leaves: `0--12` and `65--77`. The contiguous block `13--64` is
method-indeterminate, with zero counterexample flags. The worst uniform lower
endpoint occurs on leaf 53 at `-9.2561445289e-25`.

The completed bank changes the route. Raising leaf 53 to observation order
sixteen improves its lower endpoint to `-4.1152250086e-25` but does not close
it. Exact t-only, z-only, depth-two, depth-three and targeted t-by-z scouts
drive the enclosure toward zero while remaining indeterminate. At the exact
rational lower-t/mid-z point, however, the same fixed witness has a strictly
positive margin `8.2260790157e-29`. Thus the negative box endpoints are still
certificate-method limits, not counterexamples, but the vanishingly small
point margin makes deeper value subdivision computationally dominated.

K1818 then composes K1786's analytic whole-line gradient and Hessian tails with
an order-eight full-objective Taylor jet on all 52 value-indeterminate leaves.
It rigorously rejects stationarity on ten leaves: `13`, `27--28`, `39--42`,
`52--53`, and `64`. The other 42 leaves remain method-indeterminate and do not
evidence another stationary point. K1787's known local stationary box lies
inside retained leaf 50, as required. The tracked K1818 artifact indexes all
52 atomic checkpoint digests and embeds the complete evidence for every
stationary rejection.

The next useful route is adaptive subdivision or cancellation-aware interval
Newton on those 42 leaves, explicitly composing the K1787 local box. K1804's
122 exposed atomic faces and 122 exposed vertices remain open. Stationary
uniqueness, global optimality, unrestricted scope and source-owned physics
remain withheld.

## Exact resume

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py --resume-bank --summary
```

Both banks are complete and reuse every configuration-bound checkpoint. The
42-leaf residual now wakes adaptive stationary exclusion outside K1787's local
box. Exposed-boundary closure and protected global admission remain downstream.
