---
title: "Uniformity hostile verification: single-carrier regularity is numerically supported, but the shared product theorem remains U-OBSTRUCTION"
status: hostile_verification
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (finish and independently check the uniformity execution)"
inputs:
  - explorations/prong1-uniformity-method-scope-2026-07-20.md
  - explorations/prong2-krein-resolvent-literature-2026-07-20.md
  - explorations/uniformity-execution-partial-2026-07-20.md
probe: tests/channel-swings/uniformity_hostile_verify_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Uniformity hostile verification

## Bottom line

The independent check separates two claims that the prior execution had
conflated:

1. **Single-carrier section theorem:** **SINGLE-U-REGULAR-SUPPORTED** at a
   calibrated, two-rung numerical grade. On the grid-resolved matched ladder
   `delta_N ~ |q'(s*)| h_N`, both the gapped and crossing families have
   non-growing weighted resolvent norms, and their resolvent Cauchy differences
   shrink strongly. An analytically singular Jordan control fires in the same
   norm-resolvent metric.
2. **Shared two-paper theorem with product-uniformity:** **U-OBSTRUCTION**.
   The numerical object whose slope was reported as `-0.309` is not the exact
   product constructed in Stage 1 and fails the defining algebra
   `M_2^2=(q_A+q_B)I` by order `10^1`. The product clause therefore has not
   been tested.

This is encouraging for the section-theory paper's per-object open theorem,
but it does **not** greenlight the stronger boundary-law theorem.

## 1. The original negative control was invalid

The committed gaps execution used the exponent-one normalization at fixed
`delta=0.3` and expected its log norm versus `N` to grow. That expectation
does not test `delta -> 0`: at the wall the planted factor is
`|(i delta)^-1|=3.333...` at every grid size, so its analytic `N`-slope is
exactly zero. The committed control result could not discriminate regular
from singular behavior.

The hostile probe then gave that same GU-family normalization its strongest
fair version: a grid-resolved matched ladder in which delta halves as the grid
refines, and measured the actual weighted resolvent Cauchy difference. It
still did not fire:

| family | absolute-norm slope | resolvent-Cauchy slope | reading |
|---|---:|---:|---|
| exponent-one GU normalization | `-0.950` | `-2.922` | rejected as a planted singular control |
| analytic nilpotent Jordan resolvent | `+0.909` | `+0.989` | known singular control fires |

The Jordan control is exact: for `J^2=0` and `A_delta=J/delta`,
`(A_delta-iI)^-1=iI+J/delta`, so its resolvent and Cauchy-difference norms
grow as `delta^-1`. It demonstrates that the metric and slope gate can see a
genuine singularity. It does not convert the rejected GU normalization into
one.

## 2. Corrected matched-window single-carrier result

The probe keeps the existing central-difference, pointwise-lift construction,
the weighted Krein-Mourre norm, and `z=i`. It changes only the variable that
the correction itself required: for each `N`,

```text
delta_lo(N) = |q'(s*)| h_N
delta_hi(N) = 2 delta_lo(N).
```

It measures both `||R_delta_lo||` and
`||R_delta_lo-R_delta_hi||` at `N=65,129`.

| family | `U_w`, N=65 -> 129 | absolute slope | Cauchy difference, N=65 -> 129 | Cauchy slope |
|---|---:|---:|---:|---:|
| gapped | `18.7446 -> 14.7799` | `-0.347` | `0.5684 -> 0.1701` | `-1.760` |
| crossing wall | `13.0093 -> 11.0816` | `-0.234` | `1.1115 -> 0.4451` | `-1.335` |

Both absolute slopes fall within the predeclared `|tau|<0.35` regularity gate,
and both Cauchy differences shrink. The gapped slope is close to the boundary
(`0.003` inside), so this remains a two-rung numerical support result, not a
proof or a robust wide-ladder estimate. Honest grade:
**SINGLE-U-REGULAR-SUPPORTED, quarantined for further verification and exact
Krein analysis.**

## 3. The product computation does not test the constructed product

Stage 1 established an exact commuting-tensor symbol:

```text
M_exact = (M_A tensor I) tensor tau_1
        + (I tensor M_B) tensor tau_3,
```

where the two lifted factors commute, so
`M_exact^2=(q_A+q_B)I`.

The resolvent slope did not use that object. `build_product` uses the cheaper
shared-factor surrogate

```text
M_shared = M_A tensor tau_1 + M_B tensor tau_3.
```

Its square has the extra cross term
`[M_A,M_B] tensor (tau_1 tau_3)`. Direct checks on the actual frozen GU
pointwise matrices give:

| collar point | `||[M_A,M_B]||` | `||M_shared^2-(q_A+q_B)I||` |
|---:|---:|---:|
| `s=0.419402` | `11.67965` | `11.67965` |
| `s=0.569402` | `21.23684` | `21.23684` |
| `s=0.689402` | `34.29530` | `34.29530` |

The mismatch is structural, not tolerance noise. Consequently the committed
product slope `-0.309` cannot support product-uniformity for the exact Stage-1
object.

## 4. Product typing must precede more computation

There are now two distinct product readings, and the papers must select one:

- **Cartesian/direct-sum product of operator objects.** Then
  `R_(A x B)=R_A direct-sum R_B` and its operator norm is the maximum of the
  factor norms. Finite-product boundedness follows from a uniform per-object
  bound; no emergent `q_A+q_B` wall is created.
- **Coupled graded-tensor product.** Then the exact commuting-tensor symbol
  above needs a domain, derivative term, Krein form, and feasible resolvent
  realization. The current 512-block surrogate supplies none of those
  faithfully.

Until this fork is typed, the stronger product-uniform theorem is not a
well-defined completed numerical target. More runs of `build_product` cannot
close it.

## 5. Adjudication

- Per-object wall regularity: **numerically supported at the stated two-rung
  matched-window grade**; exact theorem remains open.
- Product-uniformity: **U-OBSTRUCTION** due to an untyped product fork and an
  algebraically invalid numerical surrogate.
- Shared theorem gating both papers: **not established and not numerically
  supported as a whole**.
- Krein-Mourre remains the candidate analytic route for the per-object
  definite strip. No claim is made that existing machinery proves regularity
  at the wall or supplies the coupled product clause.

## 6. Receipt

Run:

```text
python tests/channel-swings/uniformity_hostile_verify_probe.py
```

Exit `0`; deterministic power iteration (`ITERS=12`); Windows host; one
serialized local compute; no Lean/Lake, network, external action, claim-status
change, canon change, or public-posture change.
