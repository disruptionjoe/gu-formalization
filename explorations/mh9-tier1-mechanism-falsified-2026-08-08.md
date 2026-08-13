---
artifact_type: exploration_result
created: 2026-08-08
status: MH9_ENDPOINT_MECHANISM_FALSIFIED_AT_TIER1__SIGNATURE_AMBIENT_HAS_NO_NAMED_RESOLVER
grade: "EXACT, preregistered, frame-independent. tests/mh9_tier1_cperp_character_no_flip.py
  is green with all residuals 0.00e+00. The expectation was preregistered before
  running and the result contradicts it, so the assertions pin the falsification
  rather than the hypothesis."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/mh9-tier0-and-register-triage-2026-08-08.md
---

# M-H9 Tier 1: the endpoint mechanism is falsified

## Result

Tier 0 (2026-08-08) showed the base commuting real structure flips character
between the horns — `J.conj(J) = +I` at `(3,1)`, `-I` at `(1,3)` — with the
`(6,4)` fibre unchanged. That confirmed the *ingredient*.

Tier 1 asks whether that flip survives into the object that actually carries the
`delta_e` sign, `C_perp = K . J_obs` on the 128-dimensional spinor module.

```text
[1] DeWitt fibre signature -- the premise that the horns differ only in the base
    (3,1) base : dewitt_metric inertia = (6,4), zero 0   CONFIRMED
    (1,3) base : dewitt_metric inertia = (6,4), zero 0   CONFIRMED

[2] C_perp involution character
    (3,1) base : C_perp conj(C_perp) = +1 I   residual 0.00e+00
    (1,3) base : C_perp conj(C_perp) = +1 I   residual 0.00e+00

[3] SAME -> the base flip does NOT reach C_perp
    VERDICT: CPERP-CHARACTER-DOES-NOT-FLIP__MH9-ENDPOINT-MECHANISM-FALSIFIED
```

**Preregistered expectation was OPPOSITE characters. The result is the same
character on both bases.** The certificate's assertions pin the falsification.

## Why it cancels

`C_perp = K . J_obs`, and both factors move with the base:

- `J_obs = J_4 (x) J_10` — the base factor `J_4` flips, exactly as Tier 0 showed.
- `K` is the product of the positive-signature gammas. In the base block that is
  **three** gammas at `(3,1)` and **one** at `(1,3)`.

The change in `J_4`'s character and the change in the Krein product's length
compensate. The flip is real and it is cancelled downstream.

## The premise was not the problem

The `(6,4)` fibre claim is confirmed exactly on both bases by the repository's own
`dewitt_metric` — the trace-reversed Frobenius Gram
`G_ij = tr(A_i A_j) - (1/2) tr(A_i) tr(A_j)`. So the horns really do differ only
in the base, and the mechanism still fails.

## Consequence: the depth-10 fork has no named resolver

`SIGNATURE-AMBIENT` — `(9,5)` vs `(7,7)`, `open`, `UNDER-DETERMINED`, high
fan-out, **stack depth 10 over threshold** — was recorded on 2026-08-07 as having
a named resolver in `M-H9`, the B5 signature test. That resolver rested on the
prediction that the eleven `(58,78) ... (78,58)` pairs collapse to the two
endpoints and that the horns select opposite endpoints.

The first half stands: `full20_dewitt_loop_transport_probe.py` (green since
2026-07-30) forces all ten `delta_e` equal, so `k` is restricted to `{0,10}`.

**The second half does not.** The quantity that would flip `k` between horns does
not flip. So `M-H9` does not discriminate the fork, and as of 2026-08-08
`SIGNATURE-AMBIENT` has **no named resolver at all**, while ten dispositions are
stacked on it and `process_gates/fork_depth_audit.py` reports it every run.

That is a worse position than the registry recorded yesterday, and it is the
honest one.

## Scope, stated precisely

**Frame-independent, and this matters.** `C_perp` is assembled from the gamma
matrices only. The hardcoded `DEWITT_FRAME`, `mixed_rotation`'s
`timelike_leg = 3`, and the mostly-plus diagonal/off-diagonal bases never enter
this computation. The artefact risk flagged for a frame re-derivation — that
relabelling rather than re-deriving yields a spurious sign — therefore does not
apply. This result is more robust than a frame-dependent one, not less.

**What is NOT established.** The DeWitt loop transport itself was not re-run
under `(1,3)`; that still requires re-deriving the frame and the boost generator
rather than re-indexing them. So whether the 2026-07-30 all-ten-equal result
*transfers* to the other base is open. If it does not transfer, `k` is not even
confined to `{0,10}` on the `(7,7)` side and the eleven-pair residual returns
there.

**What would revive M-H9.** A different sign-carrying object that does flip, or a
demonstration that `C_perp`'s character is the wrong indicator for `delta_e`. The
certificate asserts `a == b` precisely so that a future change fails loudly and
re-opens the item.

## Honest note on the two tiers

Tier 0 confirmed a real ingredient and read as encouraging. Tier 1 shows the
ingredient does not survive composition. Reporting Tier 0 alone would have
overstated, which is the failure mode this repository's two-sided review charge
exists to catch — recorded here because the gap between the two runs was about
an hour and the temptation to stop at the positive one was real.
