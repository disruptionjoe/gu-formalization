---
artifact_type: exploration
status: exploration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "VERTICAL-VEV CHIRALITY BRIDGE: verdict BRIDGE-FAILS. A vev of the IG connection perturbation in the fibre (vertical) directions PRESERVES 4D chirality -- 10/10 fibre directions commute with omega_4 on the verified Cl(9,5) representation, stable across every alternative base/fibre index assignment -- so it CANNOT supply the cross-chirality Dirac mass channel SA-Y1 requires. The mechanism is parity: a vertical gamma anticommutes with each of the FOUR base gammas, an even number, hence commutes with their product; the planted odd-size base block flips the behaviour, confirming it is the even count and not an artifact. The only directions that DO flip omega_4 are the four base directions, and a vev there breaks 4D Lorentz invariance. Consequence: the Layer-0 bridge is CLOSED NEGATIVE, SA-Y1 stands as a genuine UNMET FORCED row, and T10 -- an explicit Lambda^0 Yukawa carrier -- IS REQUIRED."
grade: "EXACT on the verified in-repo Cl(9,5) representation, with Clifford relations re-verified, split-choice independence tested on three alternative assignments, and a planted odd-block control that fires. SCOPE: tests the Clifford/chirality obstruction ONLY -- does not exclude a mass via a composite operator, a derivative coupling, or the seesaw block structure. Closes one named route."
probe: tests/channel-swings/vertical_vev_chirality_bridge_probe.py
closes: explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md
construction: "program-native Cl(9,5) = M(64,H) carrier from the verified representation. No positive-Hilbert substitution."
canon_verdict_change: none
outcome: "BRIDGE-FAILS"
---

# The vertical-vev chirality bridge

Closes the open bridge from the Layer-0 pass on the two "Higgs" objects, which
returned `HOMONYM-WITH-NAMED-BRIDGE` and left exactly one computation standing.

## The question

`SA-Y1`'s Higgs is the `Lambda^0` carrier — dim Hom 1, **opposite** chirality,
the Dirac-Yukawa mass channel. Weinstein's *"the Higgs is an illusion"* object is
the IG connection perturbation `a`, which the same channel table lists as
`Lambda^1` — dim Hom 1, **same** chirality, "not a Lorentz scalar."

Under `14D -> 4D`, `Lambda^1(V14)` gives `Lambda^1(V4)` plus **ten 4D scalars**,
the fibre directions. And 4D chirality is not 14D chirality. So the bridge:

> Does a vertical vev of `a` supply a 4D **opposite**-chirality Dirac mass?

## Result

**No, and the reason is parity.**

| directions | behaviour under `omega_4` |
|---|---|
| **fibre** (10) | **preserve** `omega_4` — 10/10 |
| **base** (4) | **flip** `omega_4` — 4/4 |

A 4D Dirac mass must **flip** `omega_4`. A vertical vev preserves it. So the
connection perturbation cannot supply the Dirac mass channel by this route.

The mechanism is not accidental: a vertical gamma anticommutes with each of the
**four** base gammas, an even number, so it commutes with their product. Control
`N2` gives the base block an **odd** size and the behaviour flips — every outside
direction then anticommutes — which confirms the effect is the even count rather
than a feature of the representation.

`omega_14 = omega_4 . omega_10` was verified up to phase, and the fibre
directions flip `omega_10` (10/10) and hence `omega_14`. So the coupling is
14D-chirality-flipping while remaining 4D-chirality-preserving — exactly the
mismatch the channel table's "same chirality, not a Lorentz scalar" was
recording.

**The other route is closed too, for a different reason.** The four base
directions do flip `omega_4`, so a base vev would be a mass — but a vev there
breaks 4D Lorentz invariance. Both routes are shut, by independent obstructions.

## Consequence for the build

- **`SA-Y1` stands as a genuine UNMET FORCED row.**
- **`T10` — an explicit `Lambda^0` Yukawa carrier — is REQUIRED.** It was in
  limbo pending this computation; it is now confirmed necessary.
- The term-by-term pass's missing-term finding is upheld rather than dissolved.

**What is not touched.** Weinstein's Mexican-hat mechanism from `||F_A||^2` may
still supply the **potential** and the symmetry breaking — the quartic from
`||a ^ a||^2`, the quadratic from `2<F_{A_0}, a ^ a>` with its sign set by the
background curvature. This result says only that the same object does not also
supply the fermion **mass** channel. Those were always two jobs, and the standard
Higgs does both; here they separate.

## Controls

- `P1` Clifford relations re-verified on the representation;
  `omega_14 = omega_4 . omega_10` up to phase.
- `N1` split-choice independence: the fibre-preserves-`omega_4` result holds on
  three alternative base/fibre index assignments, so it depends on the counts,
  not the choice.
- `N2` planted odd-size base block flips the behaviour, 11/11.

## Scope, binding

This tests the **Clifford/chirality obstruction only**. It does not exclude a
fermion mass arising through a composite operator, a derivative coupling, or the
seesaw block structure Weinstein describes separately — *"you want a zero in a
self-adjoint operator … to get wildly different eigenvalues."* Each of those is a
distinct route and none is addressed here. What is closed is the vertical-vev
route, which was the one the Layer-0 pass named.

## What moved

Nothing in canon, verdict, count, priority, or posture. One open bridge is
closed negative, one FORCED row's status is settled, and one term is confirmed
required. That is the first row-status resolution the build has produced.

---

> **RETRACTION (2026-07-29, same day) — the `BRIDGE-FAILS` verdict above is
> WRONG and is withdrawn.**
>
> This investigation measured **the operator** `e_vertical` against `omega_4` and found it
> chirality-preserving. That arithmetic is correct. **The question was wrong.**
> A mass term is not an operator, it is a **bilinear** `<Psi, M Psi>_K`, and in
> a Krein setting the pairing carries chirality structure of its own.
>
> GU's Krein form is documented as *"purely cross-chirality"* and the explicit
> computation confirms it: **`K` anticommutes with `omega_4`.** So the composite
> `K . e_vertical` — chirality-crossing times chirality-preserving — is
> **cross-chirality**, on all ten fibre directions and every split tested.
>
> Corrected verdict: **`BRIDGE-SUCCEEDS`**. A vertical vev of the IG connection
> perturbation **can** supply a cross-chirality mass bilinear, and `T10` is
> **not** established as required. See
> `explorations/krein-paired-bilinear-chirality-2026-07-29.md`.
>
> Credit where due: the correction came from Joe, reasoning from the
> Bateman-Turok / Mannheim ghost-parity position that one works *with* the
> indefinite structure rather than removing it — so the pairing is not inert
> bookkeeping and must be composed in.
>
> Text above retained as the investigation record.
