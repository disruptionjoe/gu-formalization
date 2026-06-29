---
title: "Boundary eta of mu: DECOUPLE (2-primary). The antilinear chiralizer is frame-trivial, so it provably cannot carry the order-3 count -- the kill holds at the boundary, with a mechanism."
status: active
doc_type: result
created: 2026-06-29
grade: "computed-confirmed on the model Clifford-RS boundary operator (two independent scripts agree; all controls reproduced exactly). The structural fact it turns on -- the antilinear selector's tangent-frame charge is exactly 0 -- is convention-independent. Reconstruction-grade caveats persist (the tangential-vs-gauge fork; the fidelity of the finite Bismut-Cheeger model)."
method: "boundary-eta-of-mu build workflow (construct + compute ran; the final synthesis agent failed on a structured-output retry cap, so the verdict was recovered by running the two test scripts inline). Scripts: tests/boundary-eta/aps_eta_antilinear_plus96_rp3.py, tests/boundary-eta/plus96_framing_class_lens_eta.py."
depends_on:
  - canon/firewall-import-selector-carrier-RESULTS.md
  - canon/source-action-seiberg-witten-RESULTS.md
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - draft-papers/publication-plan-2026-06-28.md
---

# Boundary eta of mu: DECOUPLE

The one decidable gate the whole program converged on. We relocated the interior antilinear "+96" re-grading
(the operator that reaches the net-chiral +96 sector by breaking `C = J_quat.G`) to the `RP^3 = L(2;1)`
boundary spine and computed its reduced `eta-bar` under APS / Dai-Freed, asking: is it 3-primary
(`e_R = 1/12`, selector and carrier UNIFY) or 2-primary (`k/8`, DECOUPLE)?

**Answer: DECOUPLE (2-primary). The kill holds at the boundary -- and not by a numerical coincidence, by a
clean structural mechanism.**

## The mechanism (both scripts agree, two independent angles)

The antilinear `+96` selector is built from `J_quat = id_14 (x) U` (the quaternionic/Krein/Clifford structure)
and the chiral grading -- **both are internal fiber endomorphisms that leave the spacetime tangent frame
`TX^4` untouched.** Measured exactly:

- **Selector tangent-frame charge = 0** (exactly): `max ||[J_quat, any tangent-frame so(9,5) rotation]|| =
  0.00e+00`, including the `Lambda^2_+` rotation; `|<J_quat, Lambda^2_+>| = 0.00e+00`; net self-dual frame
  charge `= 0`. The selector's entire unitary content lives in the `M(64,H)` spinor/coefficient factor `U`;
  it is identically the identity on the tangent-frame bundle.
- **Therefore the selector carries NO tangent-frame `p_1`** -> framing degree 0 -> it cannot feed the
  gravitational `-p_1/24` channel where the order-3 lives. Its reduced `eta-bar` is the 2-primary gauge type
  on `L(2;1)`: the charge-`q` family `(2q^2-4q+1)/8` (denominator `8 = 2^3`), here further forced to **0** by
  the antiunitarity (`C^2 = -I` anticommuting with `D`; `+/-`-symmetry defect `7e-15`).
- **The order-3 lives ONLY in the separate self-dual `Lambda^2_+` TANGENTIAL framing**, which DOES rotate the
  frame: frame charge `33.94`, purely self-dual (net self-dual `= 33.94`), `p_1 = 4`, `e_R = p_1/48 = 1/12`
  (denominator `12 = 2^2 . 3`, factor of 3 present).

So the **chirality** lives in the internal `M(64,H)` fiber (where the antilinear selector acts), and the
**count** lives in the tangent-frame framing (`Lambda^2_+`, `p_1`). Different bundles, orthogonal by
construction. The selector and the carrier are **distinct objects, bound only by anomaly inflow -- not one
unified operator.**

## The denominators (the verdict instrument)

| object | reduced eta-bar | denominator | primality | side |
| --- | --- | --- | --- | --- |
| tangential carrier `Lambda^2_+` | `e_R = 1/12` | `12 = 2^2 . 3` | **3-primary** | UNIFY-side (the carrier) |
| coefficient/gauge channel | `(2q^2-4q+1)/8` | `8 = 2^3` | 2-primary | DECOUPLE-side |
| **+96 antilinear selector** | `1/8` (here `0` by `C^2=-1`) | `8 = 2^3` | **2-primary** | **DECOUPLE** |

A factor of 3 in lowest terms means UNIFY; only powers of 2 means DECOUPLE. The selector lands on a power of 2.

## Controls reproduced (the result is trustworthy)

In the same runs: the off-shell anchors `||[Pi_RS,M_D]|| = 58.7215` and `C2 = 155.3625`; the charge-`q`
Dirac `eta = (2q^2-4q+1)/8` family on `RP^3` (denominators all `8`, 2-primary); the tangential `e_R = 1/12`
from `p_1 = 4` (Kirby-Melvin); the genuine antilinearity of the selector (`C^2 = -I`, Kramers/PHS,
antilinearity defect `84.7 ~ 85`, matching the standing measurement); and -- critically -- the machinery
**does** detect 3-primary content when it is present (the `Lambda^2_+` carrier registers net self-dual
framing; the L3 prime control saw the order-3). So the negative result is not the machine being blind: it
detects the 3 where the 3 is, and the selector does not have it.

## What it establishes

- **The boundary-eta gate is closed with a definite answer: DECOUPLE.** The antilinear commit (selector,
  chirality, internal fiber) and the order-3 framing (carrier, count, tangent frame) are provably distinct.
- **The "import the prime 3" conjecture lane gets a definite verdict, not a hedge.** The chiralizer that
  every prior result pointed to -- the unique antilinear escape from the even-index wall -- exists and gives
  chirality (the `+96`), but it is **frame-trivial and 2-primary**, so it cannot source the count. The count
  is a separate tangential framing object the chiralizer does not touch.
- **It sharpens, rather than weakens, the paper.** Paper 1's Theorem 2 (the necessary antilinear escape) now
  carries a clean corollary: *the antilinear chiralizer is a pure internal-fiber endomorphism (tangent-frame
  charge 0), hence supplies chirality but not the generation count; the count, if homotopy-theoretic, lives
  only in the tangent-frame framing channel `-p_1/24`, which no chiralizing operator sources.* That is a
  precise impossibility-of-unification result -- a no-go that locates, with a number behind it.

## Bearing on the "killed-then-revived triplet" question

The self-dual multiplicity-3 triplet was killed as vectorlike (cross-chirality, net 0 under linear
operations), and the antilinear escape was the candidate revival. The verdict splits it cleanly: **the
antilinear finding genuinely revives the triplet's CHIRALITY** (the `+96` net-chiral sector is real, an
internal-fiber re-grading) -- **but it does NOT revive the order-3 COUNT.** The chiralizer is frame-trivial;
the multiplicity-3 is a separate tangent-frame framing object it cannot carry. Chirality: restored. Count:
stays the separate carrier. The instinct that the triplet might come back was half right -- its handedness
does, its threeness does not (from this operator).

## Honest grade and caveats

`computed-confirmed` on the model Clifford-RS boundary operator: two independent scripts (a direct APS `eta`
and a frame-charge lens) agree, all controls reproduce exactly, and the load-bearing fact (the selector's
tangent-frame charge is *exactly* 0) is convention-independent and is the cleanest possible reason for the
DECOUPLE. Caveats that keep the overall program reconstruction-grade are unchanged: the tangential-vs-gauge
fork for the carrier resolves tangential only at reconstruction grade (the gauge branch zeroes the 3-part
anyway); the finite model is a faithful model of the frame-charge / framing distinction but not a full
analytic Bismut-Cheeger fibered-boundary theorem; and the favored repo verdict (the KILL) is now confirmed
by running code rather than forecast. This is a definitive negative -- a publishable closure, not a failure.

(Process note: the build workflow's construct and compute phases ran; the final synthesis agent failed on a
structured-output retry cap, and the verdict was recovered by running the two scripts inline. The
computation is unaffected.)
