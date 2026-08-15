---
artifact_type: exploration
status: exploration
doc_type: symmetry-protection-gate
created: 2026-08-14
work_item: MJ-5
channel: majorana_126_neutrino_mechanism
title: "MJ-5: B-L is exactly preserved by every SM-preserving VEV available to GU's declared field content. Only Lambda^5 contains an SM-singlet with B-L != 0 (the 126 and 126bar singlets, |B-L| = 2), and neither eps nor $ contains one. So a nu_R Majorana mass is FORBIDDEN BY SYMMETRY, not merely unreachable -- upgrading MJ-2/MJ-4. Spontaneous breaking by a condensate is NOT forbidden and survives. Cross-channel consequence: an unbroken gauged U(1)_{B-L} is exactly channel 2's massless-extra-vector problem."
grade: "EXACT rational arithmetic on integer weight vectors; conventions validated against the 16 (charges, lepton/quark split, unique SM singlet) before being used anywhere else; 28/28. NOT: a dynamical claim, a statement about spontaneous breaking, a gauge-boson mass computation, or any claim-status movement."
disposition: B_MINUS_L_EXACTLY_PRESERVED_BY_ALL_SM_PRESERVING_VEVS_IN_DECLARED_CONTENT__EXPLICIT_MAJORANA_MASS_SYMMETRY_FORBIDDEN__SPONTANEOUS_CONDENSATE_ROUTE_UNTOUCHED__UNBROKEN_GAUGED_BL_HANDED_TO_CHANNEL_2_AS_PROPOSAL
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj3-4-source-vev-channel-and-twenty-lens-hypothesis-2026-08-14.md
  - lab/active-research/pati-salam-chain-verification.md
scripts:
  - tests/channel-swings/joe_directed_majorana_bminusl_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `CONVENTIONAL_COMPARATOR`.

# MJ-5 — B-L is exactly preserved, so the Majorana mass is symmetry-forbidden

## The upgrade under test

MJ-2 and MJ-4 showed the 126 is unreachable in GU's declared content. The
Pati-Salam lens of the MJ-3/MJ-4 council proposed a stronger claim: if `B-L`
survives as an exact `U(1)`, a `nu_R` Majorana mass — which carries
`|Delta(B-L)| = 2` — is **forbidden by symmetry**, not merely unreachable.
That is a materially stronger statement, and it holds.

A VEV can break `B-L` while preserving the Standard Model only if its direction
is an **SM singlet carrying `B-L != 0`**. So the test enumerates every weight of
every relevant representation and looks for exactly that.

Conventions were validated against the 16 before being used: `nu_R` comes out
as the unique SM singlet with `B-L = -1` and `Q = 0`, the 16 splits `4` leptons
with `|B-L| = 1` and `12` quark states with `|B-L| = 1/3`, and every electric
charge lands in `{0, +-1/3, +-2/3, +-1}`.

## Result

> **SM-singlet directions carrying `B-L != 0`, per `Lambda^k(10)`, `k = 0..5`:
> `[0, 0, 0, 0, 0, 2]`.**

Only `Lambda^5` has any: the 126 and `126bar` SU(5)-singlet directions, each
with `|B-L| = 2`. And in GU's declared content:

| field | internal content | SM-singlet directions with `B-L != 0` |
|---|---|---|
| `eps` (the source's declared VEV channel) | `Lambda^2(10) = 45` | **0** |
| `$` (displacement) | `10 (x) 45` | **0** |

Every colour-neutral weight of `eps` has `B-L = 0` outright, and every
colour-neutral `B-L`-charged weight of `$` fails the SM-singlet test.

**Therefore `B-L` is preserved exactly by every SM-preserving VEV available to
GU's declared field content, and an explicit `nu_R` Majorana mass is forbidden
by that residual symmetry.** This upgrades MJ-2/MJ-4 from "no carrier exists"
to "the operator is symmetry-forbidden", which is a stronger and more robust
statement: it survives any repair that adds fields without adding `B-L` charge.

### The near-miss, recorded

The 120 **does** contain colour-neutral, `B-L`-charged weights — the obvious
place to get this wrong, and the route this gate was expected to open, since
`10 (x) 45` contains a 120 and a 120 VEV would give an antisymmetric `M_R`.
It closes: none of those weights is an SM singlet. They carry `Y = -1` exactly
and so break hypercharge. Checked explicitly rather than argued.

## What this does NOT establish

**Spontaneous breaking is untouched.** `B-L` being an exact symmetry of the
Lagrangian does not forbid a condensate from breaking it spontaneously. A
`<nu nu>` condensate in the 126 channel — the H-CONDENSATE route kept alive by
MJ-3's nonzero Fierz coefficient `F[45][126] = -5/32` — requires no
`B-L`-charged elementary field and is **not** excluded by anything here. The
distinction between explicit and spontaneous breaking is the whole content of
this caveat and must not be collapsed.

One consequence sharpens that route rather than closing it: `B-L` sits inside
the gauge algebra, so it is **gauged**. A condensate breaking it spontaneously
therefore yields a massive `Z'_{B-L}` rather than a massless majoron. That is a
distinct, constrained experimental signature, and it is a cleaner discriminator
than the condensate's existence.

**No gauge-boson mass is computed here**, and no claim is made about how GU's
observation mechanism does or does not give mass to anything.

## Cross-channel consequence — proposal only

If `B-L` is gauged and no SM-preserving VEV in the declared content can break
it, then GU-as-declared retains an **unbroken `U(1)_{B-L}` gauge symmetry**, and
with it a massless extra vector — which is phenomenologically excluded. Either

1. GU's gauge-boson masses come from the observation mechanism rather than from
   VEVs, which is a different mechanism than the one tested here; or
2. the extra vector is a genuine problem for GU-as-declared.

That is precisely the decision question of the **photon and extra-vector
spectrum** channel: *does any presently admissible breaking orbit leave exactly
the SM massless gauge sector while making the extra `U(1)` massive or
unphysical?* This result is offered to that channel as evidence and as a
proposal. **Scheduled priority and channel order are unchanged**, and nothing
here selects or reorders work outside this channel.

## Standing of the hypotheses

- **H-DIRAC** is promoted from *selected* to *symmetry-protected*: within GU's
  declared content, neutrinos are Dirac because `B-L` cannot be explicitly
  broken. Falsifier unchanged and still live: observation of neutrinoless
  double beta decay.
- **H-CONDENSATE** survives untouched, and now carries its own discriminator: a
  massive `Z'_{B-L}`.
- **SG4** remains the standing escape — a completion may declare a
  `B-L`-charged field, and canon establishes the field-space declaration as the
  open decider.

## Next in-channel gate

MJ-6: the condensate criterion — compute the critical coupling for the 126
channel and compare it to GU's gauge coupling at the breaking scale. That is
now the *only* remaining route to a Majorana mass inside GU-as-declared, since
the explicit route is symmetry-closed. A negative there closes the channel's
central question; a positive predicts a `Z'_{B-L}` and reopens it dynamically.

---

## Correction recorded by research maintenance (2026-08-14)

**The `$` half of the result above is vacuously true as stated.** Gate MV-2
established that `$` has **no SM-singlet component at all**, not merely none
carrying `B-L`: an SM singlet requires the zero weight, and `10 (x) 45` never
contains it because a single `+-e_i` cannot cancel a two-entry root.

The conclusion is unaffected and in fact **strengthened** — `$` cannot take an
SM-preserving VEV in any direction whatsoever. Only the grounds for the `$`
half change. The `eps` half is sound and non-vacuous, since `eps` genuinely
does have SM singlets.

Recorded rather than silently patched: a vacuously-passing check is the exact
defect `process_gates/certificate_shape_audit.py` exists to flag, and this one
reached a committed artifact.
