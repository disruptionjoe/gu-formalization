---
artifact_type: exploration
status: exploration
doc_type: conditional-obstruction-gate
created: 2026-08-14
work_item: PV-1
channel: photon_and_extra_vector_spectrum
title: "PV-1: over the ENTIRE SM-preserving adjoint orbit space the unbroken dimension takes values {13,15,19,25} and never 12 -- every available orbit retains at least one extra massless vector. The one vacuum class that would give exactly the SM (rank-one v_PSB in (10bar,1,3), cycle1/CB-A A8) sits inside the 126, which channel-3 gates MJ-2 and MJ-5 show is unavailable in GU's declared field content. Channel evidence endpoint reached: OBSTRUCTION."
grade: "EXACT rational arithmetic on integer root/weight vectors, 21/21. Re-verifies CB-A row A4 independently as a control. NOT: a new stabilizer theorem (cycle1/CB-A A8 owns that), a gauge-boson mass computation from the observation mechanism, a source action, or any claim-status movement."
disposition: NO_AVAILABLE_SM_PRESERVING_ORBIT_LEAVES_EXACTLY_TWELVE__MINIMUM_UNBROKEN_DIMENSION_THIRTEEN__EXACT_SM_ORBIT_REQUIRES_126_WHICH_IS_UNAVAILABLE__OBSERVATION_MECHANISM_UNTESTED
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/pati-salam-chain-verification.md
scripts:
  - tests/channel-swings/joe_directed_extra_vector_stabilizer_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `CONVENTIONAL_COMPARATOR`.

# PV-1 — every available orbit keeps an extra massless vector

## What is prior art, and what is new

This gate builds directly on work the repository already owns, and the
distinction matters:

- **CB-A row A4 (prior):** exactly two SM-singlet `(1,1,0)` directions survive
  in the internal adjoint — `U(1)_Y` and `U(1)_X` — and the extra
  `U(1)_{B-L}` is *forced by the rank of the carrier, not chosen*.
  Re-verified here independently as a control.
- **CB-A row A8 / cycle1 (prior):** a **conditional** stabilizer theorem — given
  a rank-one `v_PSB` in `(10bar,1,3)`, the identity-component stabilizer has
  Lie algebra `su(3) + su(2)_L + u(1)`, i.e. exactly the SM. CB-A marks this
  `NEEDS-U1`, "not selected". **This artifact does not re-derive that theorem
  and claims no novelty for it.**

**New here:** CB-A leaves the vacuum *unselected*. This gate asks the different
question — is that vacuum **available at all** in GU's declared field content?
— and computes the unbroken dimension for the orbits that are.

## Result

Sweeping the entire two-dimensional space of SM-preserving adjoint VEV
directions:

> **unbroken dimensions = `{13, 15, 19, 25}`. The Standard Model's 12 never
> occurs. The minimum is exactly 13 = SM + one extra `U(1)`.**

Individual points: pure `B-L` leaves `su(3)+u(1)+su(2)_L+su(2)_R = 15`; the
`SU(5)` direction (the `(1,1,1,1,1)` combination) leaves `su(5)+u(1) = 25`; a
generic point leaves exactly 13.

The general argument covering **both** GU bosonic fields, not just the adjoint:
an SM-preserving VEV lies along an SM-singlet direction, and MJ-5 established
that **no SM-singlet direction in `eps` or `$` carries `B-L != 0`**. So any such
VEV is `B-L`-neutral, `B-L` stays unbroken, and the unbroken algebra contains
`SM + u(1)_{B-L}`, dimension at least 13. The adjoint sweep above is the
explicit verification; the `$` case rests on MJ-5 rather than on its own sweep,
and is scoped that way deliberately.

## The obstruction

The one vacuum class that *would* give exactly the SM is cycle1's rank-one
`v_PSB` in `(10bar,1,3)`. That block sits inside the **126**:
`126 = (6,1,1) + (10,3,1) + (10bar,1,3) + (15,2,2)`, verified. And the
channel-3 gates show the 126 is unavailable:

- **MJ-2:** the 126 has multiplicity **exactly zero** in `eps` (`Lambda^2(10)=45`)
  and in `$` (`10 (x) 45`), tilted-group robustly.
- **MJ-5:** the `v_PSB` direction is the unique SM-singlet with `B-L = -2`, and
  no such direction exists in either field.

**So the antecedent of the conditional stabilizer theorem is unsatisfiable in
GU's declared field content.** That is this channel's declared evidence
endpoint — *an obstruction showing that the available orbit classes retain
unwanted light vectors* — reached in the negative direction.

## Claim ceiling

**This tests the Higgs-VEV mechanism only.** GU's characteristic move is that
breaking comes from **observation** — a choice of metric section — which is a
reduction of structure group, not a Higgs mechanism, and which this gate does
**not** model. Two readings survive and are not decided here:

1. GU's gauge-boson masses come from the observation mechanism rather than from
   VEVs, in which case the extra vector may be lifted by machinery outside this
   computation; or
2. the extra massless vector is a genuine phenomenological problem for
   GU-as-declared.

Deciding between them requires a mass computation for the observation
mechanism, which no artifact in the repository currently owns. That is the
honest next gate, and it is where this channel's real difficulty sits.

**Also not claimed:** any statement about SG4's undeclared completion, which
canon establishes as the open decider on field space; and any selection of the
action-owned vacuum, which this channel's own boundary assigns to ordinary
Lane 1 and does not duplicate.

## Next in-channel gate

PV-2: can the observation mechanism — reduction of `Spin(6,4)` to its maximal
compact by a choice of section — give mass to gauge directions at all, and if
so to which? A negative there converts PV-1 from "the Higgs route fails" into a
genuine light-vector obstruction for GU. A positive relocates the whole
question outside the VEV framing, and would equally relocate the channel-3
Majorana result.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
