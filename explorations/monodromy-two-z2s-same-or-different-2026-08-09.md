---
title: "The two Z/2's: is the H^1(F;Z/2) Mobius monodromy the same Z/2 as the ghost parity? A well-posed question with a decisive, cheap test — and a Layer-0 disambiguation that must come first"
artifact_type: exploration_result
created: 2026-08-09
status: AMENDED_SAME_DAY__MOBIUS_DOUBLE_COVER_READING_IS_DEAD_BY_COMPUTATION__THE_ACTING_Z2_IS_pi0_O31_TIME_REFLECTION_NOT_pi1_SO__LAYER_0_HOMONYM_CONFIRMED__GHOST_PARITY_IDENTIFICATION_STILL_OPEN_BUT_PRIOR_SHIFTED
grade: "QUESTION + TRIAGE as originally filed, AMENDED same day by execution -- see the amendment banner
  and the investigation receipt. The original body's 'no computation was run' applied to the note as first written;
  a computation HAS since been run and its outcome is folded in at the top. Every fact quoted is already in the repository; the
  contribution is (a) noticing that two independently-established Z/2 structures have identical symptoms,
  (b) naming the decisive test, and (c) flagging that a Layer-0 disambiguation gates it. NOT a claim that
  the two classes are the same, and NOT a claim about the generation count."
canon_verdict_change: none
follows:
  - explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md
  - explorations/mh9-tier0-and-register-triage-2026-08-08.md
  - explorations/complexification-existence-check-2026-08-08.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
---

# The two `Z/2`'s

> ## AMENDMENT 2026-08-09 (same day) — the Mobius half is ANSWERED, and negatively
>
> Run receipt: `explorations/run-monodromy-frame-charge-preflight-hostile-2026-08-09.md`.
> `tests/dc-h1/dc_h1_orbit_sign_monodromy_probe.py` re-run, ALL CHECKS PASSED.
>
> **The `Z/2` that generates `w != 0` in `H^1(F;Z/2)` is `pi_0` of the Lorentz stabilizer `O(3,1)` — the
> `O(1)` TIME REFLECTION. It is a REFLECTION `Z/2`, not a double-cover `Z/2`.**
>
> The spinor double cover is **provably inert**: `chi` is quadratic in the Clifford lift, so it descends to
> `SO` and is blind to the covering — the deck element `-I` of `Spin -> SO` has `chi = +1`, and
> `pi_1(SO(3)) = Z/2` **does not move a single orbit sign**. The probe's own words: *"The two share a group
> order and nothing else: Layer-0 HOMONYM."*
>
> So the Mobius / `4pi`-spinor reading of this monodromy — the motivating intuition for this note — **is
> dead by computation**, and dead in exactly the way the pre-flight predicted: a `Z/2 = Z/2` number-match,
> which the governing hypothesis note had already typed as the weakest evidence class and forbidden as an
> argument.
>
> **What remains open, with a shifted prior.** Whether the *ghost parity* is the monodromy class is still
> not settled — Run A identifies the monodromy's mechanism, not the ghost parity. But the "honest prior
> tilts toward DIFFERENT" reasoning below **no longer holds as stated**: it leaned on the frame-triviality
> wall, and the same run session showed that wall is **evadable** (Class B: `exp(theta . su2_+) . C_GU`,
> antilinear, `C^2 = -1`, chirality-preserving, carrier leakage `2.56e-13`, NET-SD frame charge nonzero).
> Frame-triviality therefore no longer automatically separates the two `Z/2`'s.
>
> **A new kill applies to the escape, however:** the escaping NET-SD is **continuously tunable and
> non-monotone** (`+5.988 / +14.789 / +13.307` at `theta = 0.3 / 0.7 / 1.2`), so it is **not an index** and
> cannot carry a count. Read the sections below with this amendment in force.

## The observation

The repository has established, independently and by different routes, two `Z/2` structures whose symptoms
are indistinguishable.

### `Z/2` #1 — the metric-fiber monodromy (base side)

Under `C -> -C` the even and breaking subspaces **exchange**, `d -> 136 - d`, i.e. `58 <-> 78`, and

> this sign is a nontrivial holonomy class `w != 0` in `H^1(F;Z/2)` **with no global section**. Only the
> unordered pair is loop-invariant.

`H^1(-; Z/2)` is where `w_1` lives; a nonzero class there is exactly the Mobius / orientation-reversing
monodromy. Elsewhere the same degree-1 class is identified as `w_1(L_time)` — a **non-orientable time line
bundle** (`descent-sections == Phi-fixed-points == w_1(L_time)`).

The complex-analytic cause is recorded and is worth quoting because it explains *why* rather than *that*:

> The monodromy is not an accident of the loop chosen — **it is what happens when a real invariant is
> transported through a space where that invariant does not exist.**

### `Z/2` #2 — the ghost parity (internal side)

On the 192-dim `j=1` carrier the Krein form has signature `(+96, -96, 0)` with both chirality halves
totally isotropic, so the form is pure cross-pairing: 96 hyperbolic (generation, mirror) pairs. The ghost
parity is the `Z/2` swapping `u <-> v`, and its even/odd eigenspaces label physical vs ghost.

## Why they look like the same thing

Four separately-computed statements, one shape:

| statement | source |
|---|---|
| "Only the **unordered pair** is loop-invariant" | the `H^1(F;Z/2)` monodromy |
| The form pairs a generation **only** with its mirror; each half totally isotropic | Krein signature `(+96,-96,0)` |
| Net chiral asymmetry **identically zero**, every signature | rep-theory theorem |
| Every GU-native core is **spectrally sign-blind**, every eigenspace exactly `K`-balanced | ghost-parity 2026-07-06 update |

Each says: **the pair is well defined; the labelling of its members is not.** That is the defining property
of a `Z/2` monodromy — on a Mobius band the two sides are not globally distinguishable, only the unordered
pair is.

If they are the same class, four things stop being separate puzzles and become one topological fact
(`w != 0` ⇒ no global section):

1. why no **derived** ghost-parity operator arises — you cannot derive a global section that does not exist;
2. why the dynamics is **sign-blind** — locally the two sheets are identical, which is what a double cover is;
3. why the selector must be **imported** — no global section means the choice is made, not found;
4. why the endpoint looks like a **boundary** — a section that cannot exist globally must be fixed at a cut.

That would be the firewall-boundary hypothesis arriving from pure topology rather than from physics.

## Why they may well NOT be the same — the known obstruction

`Z/2` #1 lives on `F`, the **metric fiber** `GL(4,R)/O(3,1)` — tangent/base-side topology.
`Z/2` #2 lives on the **192-dim Clifford carrier** — internal fiber, inside `M(64,H)`.

There is a standing computed wall between those two places: **internal-fiber endomorphisms have
tangent-frame charge exactly `0`.** It is the same wall that strands `Spin(8)` triality
(`canon/three-generations-locate-not-force-CRT-RESULTS.md`), and it is exact, not approximate.

**And there is already a directly relevant number.** The single-decider computed the frame charge of the
antilinear chiralizer `C = J_quat . G` as **exactly `0.00e+00`** — structural and convention-independent,
since any `id_14 (x) U` is traceless on the frame factor. *If* the ghost parity is that operator, it is
frame-trivial and therefore decoupled from `H^1(F;Z/2)`, and the two `Z/2`'s are **different**.

## The Layer-0 step that gates everything (do this first)

**Before any computation**, disambiguate. At least three operators in this program are referred to with
overlapping language and may or may not be one object:

- the **ghost parity** `P`, described as the **Cartan involution of `so(9,5)`** (`[P, S] = 0`);
- the **`C`-operator** of PT/Krein theory, whose existence and uniqueness is the 2026-07-06 near-closed
  negative;
- the **antilinear chiralizer** `C = J_quat . G`, whose frame charge is the computed `0.00e+00`;
- and the `C` in the `C -> -C` monodromy of `Z/2` #1.

**These share a letter. They may not share an object.** This repository's Layer-0 precondition exists for
exactly this, and the same conflation has already been made twice this month on the
`SIGNATURE-AMBIENT` / `REAL-CLIFFORD-FORM` pair. Resolving the letters is reading, not computing, and it is
cheap.

## The decisive test, once the letters are resolved

```
Compute the net self-dual TANGENT-FRAME CHARGE of the ghost-parity operator.

  charge = 0        -> internal-fiber, frame-trivial, decoupled from H^1(F;Z/2).
                       The two Z/2's are DIFFERENT, and the symptom-matching is a
                       coincidence that itself needs explaining.
  charge != 0       -> the parity has a diagonal (tangent (x) fiber) component.
                       Then compute whether its class pulls back from w in H^1(F;Z/2).
```

The machinery exists — `tests/anchored-leads/spin8_triality_lefschetz.py` already computes frame charge of
`id_14 (x) M` and returns exactly 0. This is a small evaluation on an existing substrate, not a build.

**Note the structural echo:** this is the *same* question as triality's `P3` (is the order-3 `g` internal-only,
or diagonal with nonzero tangent-frame charge?). Two different discrete symmetries, one shared decider.
That is worth knowing on its own — it suggests "internal-only vs diagonal" is the program's real recurring
fork, not `Z/2`-vs-`Z/3`.

## Honest prior

**The existing evidence tilts toward DIFFERENT.** The frame-triviality wall is exact and has already
stranded one order-3 candidate; the `0.00e+00` for `C = J_quat . G` is computed. The interesting outcome
would be the other one, which is a reason to be careful rather than a reason to expect it.

If the answer is **different**, the finding is not nothing: two independent `Z/2`'s producing four identical
symptoms is a coincidence that wants explaining, and the most likely explanation — that "no global section"
is a generic consequence of indefinite structure rather than of any particular bundle — would itself be
worth stating.

## Scope

Does not claim the classes are the same. Does not claim anything about the generation count. Does not move
any verdict. All `(9,5)`-substrate numbers quoted are valid on a live but undetermined horn
(`SIGNATURE-AMBIENT` is OPEN), and the frame-charge argument would need re-running on `(7,7)`, where
`J_quat` does not exist.
