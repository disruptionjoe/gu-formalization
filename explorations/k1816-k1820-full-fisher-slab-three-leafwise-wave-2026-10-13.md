---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-16"
---

# K1816--K1820: the value bank stands; corrected gradients exclude nine leaves

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

K1818's first full-objective gradient bank exposed a remainder-domain defect
during hostile review. The Taylor polynomial is centered at K1787, but the
degree-eight derivative enclosure was evaluated only on each target leaf. For
every leaf outside the anchor, Taylor's intermediate point can lie on the
segment between the anchor and leaf, so the derivative enclosure must cover
the complete anchor-to-leaf hull. The ten apparent stationary exclusions are
therefore withdrawn before downstream use. They do not change K1816's value
bank or K1787's local stationary certificate.

The corrected producer uses configuration-distinct checkpoints and the exact
axis-aligned hull of K1787's anchor with each target leaf. The complete replay
rigorously excludes leaves `27`, `28`, `39--42`, `52`, `53`, and `64` by at
least one whole-line gradient component. The other 43 candidates remain
method-indeterminate, including leaf 50 containing K1787's named stationary
box; retention is not evidence of another stationary point. K1804's 122
exposed atomic faces and 122 exposed vertices remain open. Stationary
uniqueness, global optimality, unrestricted scope and source-owned physics
remain withheld.

## Exact replay

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py --resume-bank --summary
```

The command reuses only corrected anchor-hull checkpoints; the invalidated
leaf-only files have distinct names and are ineligible. Leaf-centered
reexpansion or a complete interval-Newton/Krawczyk cover is now required on the
43 retained leaves. Exposed-boundary closure and protected global admission
remain downstream.
