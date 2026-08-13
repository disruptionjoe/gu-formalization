---
title: "The carrier NET-SD frame charge is EXACTLY 24*sqrt(2): the integer content is 24, the sqrt(2) is generator normalization, and the Class B escapes leave the integral locus"
artifact_type: exploration_result
created: 2026-08-09
status: FRAME_CHARGE_IS_EXACTLY_24_ROOT_2__NETSD_OVER_ROOT2_MINUS_24_IS_0.000e+00__C2_OVER_BARE_IS_SQRT_7_TO_8.4e-15__ESCAPES_ARE_OFF_LATTICE__NON_QUANTIZATION_FINDING_SHARPENED_NOT_OVERTURNED
grade: "COMPUTED, exact to machine precision, on the verified Cl(9,5) = M(64,H) substrate via the existing
  frame_charge_split machinery. Two exact identities. The INTERPRETATION (that sqrt(2) is generator
  normalization) is reconstruction-grade and is the one thing here that needs hostile checking."
canon_verdict_change: none
follows:
  - explorations/run-monodromy-frame-charge-preflight-hostile-2026-08-09.md
  - explorations/lens-mechanism-salvage-scored-2026-08-09.md
probes:
  - tests/gu-independent/frame_active_antilinear_chiralizer_hunt.py
---

# `NET-SD = 24 sqrt(2)`, exactly

> ## RETRACTED 2026-08-09 (same day) — DO NOT CITE THE INTERPRETATION
>
> The **arithmetic** below stands: `NET-SD = 24 sqrt(2)` exactly. The **interpretation is REFUTED.**
>
> A gamma-scramble test (six-move workflow, hostile-verified, every number independently reproduced) shows
> **NET-SD is a pure DIMENSION COUNT with ZERO Dirac content.** It equals `n_SD * sqrt(DIM) = 3 * sqrt(128)`
> **analytically**, and is **bit-identical under every gamma scramble -- including replacing all 14 gammas
> with zero matrices.**
>
> And this file's proposed reading is refuted specifically: **the `sqrt(2)` is NOT generator normalization.**
> It is the leftover of `sqrt(128) = 8 sqrt(2)`. The "integer content is 24" claim is therefore **dead** --
> the 24 is `3 x 8`, i.e. `n_SD` times a spinor-dimension factor, with no geometric Dirac content whatsoever.
>
> **`step7_integer_freeness.py`'s verdict stands unchallenged**: no honest scale-invariant integer with Dirac
> content exists in the bridge data. This file briefly appeared to be a counterexample. It is not one.
>
> Also recorded: the workflow found this observation was **already in the repo**. Sixth false-novelty claim
> of the session.

## The computation

Re-run of the existing reference in `frame_active_antilinear_chiralizer_hunt.py`, printed at full precision
instead of 3 dp:

```
NET-SD (carrier su(2)_+, Lambda^2_+)  = 33.941125496954285
NET-SD / sqrt(2)                      = 24.0
NET-SD / sqrt(2) - 24                 = 0.000e+00
NET-SD^2                              = 1152.0000000000002      (= 24^2 * 2)

bare                                  = 58.72150807160918
C2                                    = 155.36250696815043
C2 / bare                             = 2.645751311064599
sqrt(7)                               = 2.6457513110645907
C2 / bare - sqrt(7)                   = 8.438e-15
```

**Two exact identities:** `NET-SD = 24 sqrt(2)` and `C2 = bare * sqrt(7)`.

## Why this matters

Canon describes this channel as *"3-primary, where a count would live."* It has been quoted throughout the
program as `33.94` — a real number with no evident structure. It is not. **It is an integer times a
normalization factor, and the integer is 24.**

`24` is the program's recurring integer: `pi_3^s = Z/24`, `|Im J_3| = 24`, the `-p_1/24` channel,
`chi(K3) = 24`, and the CRT split `Z/24 = Z/8 (+) Z/3` that the whole two-arena structure lives in.

**Most likely reading (reconstruction-grade, needs hostile check):** the `sqrt(2)` is **generator
normalization**, not content. Orthonormal self-dual 2-forms carry the standard `(e1^e2 + e3^e4)/sqrt(2)`
factor, so a single `sqrt(2)` from the `sd_gens` / `asd_gens` normalization is exactly what one expects.
Divide it out and the frame charge is the integer **24**.

## What this does to the non-quantization finding — sharpens it, does NOT overturn it

The salvage note recorded (Tier 1, lens 10) that the Class B escape's NET-SD is continuous and non-monotone,
therefore not an index. That stands, and this result makes it sharper rather than weaker:

| object | NET-SD | `/sqrt(2)` |
|---|---|---|
| carrier `su(2)_+` (undressed) | `33.941125` | **24.0 exactly** |
| B: `exp(0.3 su2_+) . C_GU` | `5.988` | `4.234` |
| B: `exp(0.7 su2_+) . C_GU` | `14.789` | `10.457` |
| B: `exp(1.2 su2_+) . C_GU` | `13.307` | `9.409` |

**The natural, undressed object sits exactly on the integral locus. Every escape candidate is off it.**

So the correct statement is not "frame charge is a continuum quantity." It is: **there is a quantized value
sitting right there — 24 — and the frame-dressing escape route walks away from it.** The escape does not
merely fail to be an index; it *leaves the integral locus* in order to become net-chiral.

That is a materially better-typed statement of the same kill, and it is the first place in this session where
a continuum-looking quantity in this program resolved to a meaningful integer.

## What is NOT claimed

- **Not** that the count is 24, or that 24 has anything to do with the generation number. The `-p_1/24`
  channel *divides* by 24; an appearance of 24 in a numerator is not a count.
- **Not** that the `sqrt(2)` interpretation is established. That is the reconstruction-grade step and the one
  a hostile reviewer should attack first: confirm the normalization of `sd_gens`/`asd_gens` directly rather
  than inferring it.
- **Not** a claim that the escapes are wrong — they are computed and clean. Only that they are off-lattice.
- All `(9,5)` arithmetic on a live but undetermined horn.

## Next check (cheap)

Read the `sd_gens` / `asd_gens` construction and confirm the `sqrt(2)`. If it is normalization, restate the
channel as **integer-valued** everywhere it is quoted, and re-ask whether any escape candidate can be
constructed *on* the integral locus rather than off it. That is a sharper form of the escape hunt than the
one already run.
