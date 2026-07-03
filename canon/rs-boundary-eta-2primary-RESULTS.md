---
title: "STEP 2 of WC-FUNCTION-SPACE-EXT closed at computed grade: the FULL Rarita-Schwinger boundary operator's reduced eta-bar on the sector's own boundary RP^3 = L(2;1) is 2-PRIMARY. The net self-dual tangent-frame charge of D_RS = E + E^dag (and of Pi, M_D) is 0 (computed, two independent angles) -- so it carries no tangent-frame p_1 and cannot feed the gravitational -p_1/24 channel where the order-3 lives; the only residue is the charge-q lens type (2q^2-4q+1)/8, denominator 8, 2-primary for every integer charge, with the RS boundary spectral eta = 0 (cross-chirality +96,-96 balance). Therefore an odd generation count CANNOT enter through the sector's own boundary -- it must come from an EXTERNAL topological background (the STEP 3 K3 / flux route). This extends canon/boundary-eta-of-mu-RESULTS.md from the single +96 selector to the full RS boundary operator."
status: staged
doc_type: result
created: 2026-07-03
grade: "computed-confirmed on the model RS boundary operator (two independent scripts agree: net self-dual frame charge 0 under a rotated frame basis AND a random fiber similarity; independent signature/eta = 0). The load-bearing fact -- the RS operator's NET self-dual (SD-ASD) tangent-frame charge is exactly 0 while the Lambda^2_+ positive control registers 33.94 (the machine detects a 3 when present) -- is convention-independent. Same finite-model reconstruction caveats as boundary-eta-of-mu-RESULTS.md (a faithful model of the frame-charge / framing distinction, not a full analytic Bismut-Cheeger fibered-boundary theorem). Internal tier (caveat (e))."
depends_on:
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/rs-function-space-framework-SPEC.md
  - canon/function-space-index-conservation-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
scripts:
  - tests/rs-function-space/rs_boundary_eta_l21.py
  - tests/rs-function-space/verify/rs_boundary_eta_indep_check.py
---

# STEP 2: the RS boundary eta on L(2;1) is 2-primary (the sector's own boundary cannot source a count)

The one residual keeping "external by structure" from being unconditional is the actual
Rarita-Schwinger operator on sections: `ind(D_RS) = [bulk] + [APS boundary/end eta] + [family-index]`.
The **bulk** term was already closed (2-primary by Rokhlin: `I_{3/2} = 21*sigma/8 ≡ 0 mod 3`;
`rs-function-space-framework-SPEC.md` §4). This note closes the **boundary/APS** term.

## The question

Does the reduced eta-bar of the full RS boundary operator on the sector's own boundary
`RP^3 = L(2;1)` carry a factor of 3 (an order-3 piece, so an odd count could enter at the boundary),
or only powers of 2 (2-primary, so it cannot)? **Denominator decides.**

## The computation (two legs, reusing the validated boundary-eta machinery)

**Leg 1 -- gravitational `-p_1/24` channel (the only route to a 3).** This channel is fed only by a
**net self-dual** tangent-frame `p_1`. Computing the net self-dual frame charge (`SD - ASD`) of the
full RS boundary operator `D_RS = E + E^dag` (with `E = Q.M_D.Pi`) and its building blocks:

| operator | \|frame\| | SD | ASD | net (SD-ASD) |
|---|---|---|---|---|
| `Pi` (gamma-trace projector) | 3.4286 | 1.7143 | 1.7143 | **0** |
| `M_D` (hermitian part) | 0.0000 | 0 | 0 | **0** |
| `D_RS = E + E^dag` | 4.9418 | 2.4709 | 2.4709 | **0** |
| `Lambda^2_+` carrier (positive control) | 33.94 | 33.94 | 0 | **+33.94** |

The RS operator is **non-chiral** (net self-dual `= 0`): it carries no tangent-frame `p_1`, so
`e_R(grav) = 0/24`. The `Lambda^2_+` control (net self-dual `33.94`, `e_R = 1/12`) confirms the machine
**does** see a 3 when one is present -- the null result is not blindness.

**Leg 2 -- gauge/spectral `k/8` channel.** The charge-`q` twisted Dirac reduced eta-bar on `L(2;1)` is
`(2q^2 - 4q + 1)/8` -- denominator `8` for **every** integer charge, so any internal-charge residue
stays in `(1/8)Z` (2-primary). The RS boundary Dirac `D_RS` is chiral/off-diagonal, so its spectrum is
`+/-`-symmetric and its **spectral eta = 0** (symmetry defect `1.2e-14`); the RS sector is
cross-chirality balanced (`Tr(chirality | RS) = 0`, the `(+96,-96)`).

## Result

> `eta-bar(D_RS on L(2;1)) = [grav -p_1/24 : 0] + [gauge/spectral : (1/8)Z]` -- **NO factor of 3 =>
> 2-PRIMARY / EVEN.**

**The sector's own boundary cannot carry the order-3 generation count.** An odd count must enter through
an **external topological background** -- exactly the STEP 3 K3 family-index / flux route
(`external-topological-index-flux-RESULTS.md` already shows the external flux datum realizes any integer
index, odd for odd flux).

## Independent re-check

`verify/rs_boundary_eta_indep_check.py` reproduces net self-dual `= 0` under (a) a rotated `SO(3)`
frame basis (`-4e-16`), (b) a random unitary fiber similarity (`0`), and (c) an independent
signature count of `D_RS` (`0`), with the `Lambda^2_+` control still firing (`+28.62`). Agrees.

## Bearing on the paper

Tightens the "external by structure" story: with the **bulk** even (Rokhlin) and now the **boundary**
even (this note), the entire interior + boundary of the sector's own RS operator is 2-primary. The
only remaining place a `Z/3` generation count could live is the **K3 family-index pushforward** (STEP 3,
the crux) -- which requires the (unbuilt) GU source-action fiber geometry. This is a `computed`-grade
strengthening; it does not by itself close WC-FUNCTION-SPACE-EXT (STEP 3 remains open) and does not
change any published claim. Internal tier; staged, not CANON.md-promoted. Pauses for Joe.
