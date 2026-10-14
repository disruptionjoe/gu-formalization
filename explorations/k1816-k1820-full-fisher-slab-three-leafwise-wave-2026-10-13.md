---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-13"
---

# K1816--K1820: leafwise recentering restores a strict compact margin

## Result

K1816 implements atomic, digest-checked checkpoints for the fixed K1787-score
Cauchy witness on each of K1796's 78 exact slab-three leaves. On leaf zero,
sixth order remains indeterminate: its compact cross-margin lower endpoint is
`-7.7208260863e-23`, with an absolute degree-six remainder
`7.9165379542e-23`. Raising the same leaf to order eight proves a strict
positive compact margin `1.9355631591e-24`; its degree-eight remainder is only
`2.1555519979e-26`.

The cheaper order-seven route also succeeds. Leaves zero and one have strict
compact lower margins `6.2357805699e-25` and `5.6871461288e-25`, with
degree-seven remainders `1.3335406221e-24` and `1.3309315190e-24`. K1817's
independent order-eight test on the complete first K1794 parent remains
indeterminate at `-2.5128123483e-20`, so higher order without subdivision is
not enough. The decisive scale change is exact leafwise recentering.

K1818 therefore selects order seven for the restart-safe production bank and
reserves order eight as a per-leaf fallback. The serial backend measured about
18 minutes per order-seven leaf. Two leaves are complete and 76 remain, an
estimated 23 serial hours. The ignored local checkpoints survive interruption;
the committed K1816 artifact embeds every completed certificate and digest.

This is a successful method calibration, not a complete value cover. Analytic
whole-line tails have not yet been composed with all leaves; complete
interval-Newton/Krawczyk rejection and K1804's 122 exposed atomic faces and 122
exposed vertices remain open. K1819 and K1820 preserve those obligations and
withhold stationary uniqueness, global optimality, unrestricted scope and
source-owned physics.

## Exact resume

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py --resume-bank --parameter-order 7 --summary
```

Any order-seven leaf without a strict positive margin switches locally to
order eight. Completion of the compact bank then wakes analytic tail
composition, stationary rejection outside K1787's local box, exposed-boundary
closure and only then protected global admission.
