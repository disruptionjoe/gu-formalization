---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-14"
---

# K1816--K1820: the complete leafwise bank isolates a fixed-witness method limit

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

The tracked K1816 artifact embeds all 78 uniform certificates and digests plus
the configuration-bound leaf-53 route scouts. The next useful route is to
compose the existing analytic whole-line tails and prioritize complete
stationary/gradient rejection of the 52-leaf block before spending further on
fixed-witness value subdivision. K1804's 122 exposed atomic faces and 122
exposed vertices remain open. Stationary uniqueness, global optimality,
unrestricted scope and source-owned physics remain withheld.

## Exact resume

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py --resume-bank --parameter-order 8 --cell-half-width 1/4 --observation-order 14 --summary
```

The bank is complete and reuses every configuration-bound checkpoint. The
52-leaf indeterminate block now wakes analytic tail composition and
stationary/gradient rejection outside K1787's local box. Exposed-boundary
closure and protected global admission remain downstream.
