---
artifact_type: exploration
status: exploration
doc_type: mechanism-scope-gate
created: 2026-08-14
work_item: PV-2
channel: photon_and_extra_vector_spectrum
title: "PV-2: observation reduces Spin(6,4) to its maximal compact, which addresses exactly the 24 directions of p -- the ones carrying the OPPOSITE Killing signature. The Standard Model's 12 sit entirely inside k, and exactly 9 non-SM directions (6 leptoquarks + 2 W_R + 1 Z') remain inside k, untouched by the reduction. Observation therefore cannot close PV-1's gap: the surviving extra vectors need a VEV, and PV-1 showed none is available."
grade: "EXACT integer matrix computation of the Cartan decomposition of so(6,4) and the Killing-form signature on each summand, 22/22. NOT: a quantization or ghost-removal argument, a connection variation, a source action, a statement about SG4's completion, or any claim-status movement."
disposition: OBSERVATION_ADDRESSES_ONLY_THE_24_NONCOMPACT_DIRECTIONS__NINE_NON_SM_COMPACT_DIRECTIONS_SURVIVE_UNTOUCHED__PV1_ESCAPE_ONE_CLOSED__GHOST_REMOVAL_STILL_A_QUANTIZATION_QUESTION
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - canon/shiab-existence-cl95.md
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
scripts:
  - tests/channel-swings/joe_directed_observation_reduction_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# PV-2 — observation cannot reach the extra vectors

## The question PV-1 left open

PV-1 showed no available SM-preserving VEV leaves exactly the SM massless
gauge sector — the minimum unbroken dimension is 13, never 12 — and stated its
own ceiling honestly: GU does not break by a Higgs VEV but by **observation**,
a choice of metric section, which reduces the structure group
`Spin(6,4) -> Spin(6) x Spin(4)`. That mechanism was unmodelled. This gate
models it.

No connection variation is needed. Reduction to the maximal compact **is** the
Cartan decomposition, and the physical content is fixed by the Killing-form
signature plus where the Standard Model sits.

## Result

> **`so(6,4) = 45 = k(21) (+) p(24)`, with the Killing form NEGATIVE on every
> direction of `k` and POSITIVE on every direction of `p`.**

Verified structurally, not asserted: `k` is a subalgebra and splits
block-diagonally as `so(6) (dim 15) + so(4) (dim 6)`; `p` is purely
block-off-diagonal, the `6 x 4 = 24` mixed directions; and `[p,p]` lands back
in `k`, the symmetric-space structure.

`k ~ su(4) (+) su(2)_L (+) su(2)_R` is the Pati-Salam algebra, and **the
Standard Model's 12 generators sit entirely inside `k`** — every SM direction
is compact. Therefore:

| | dimension | reached by the reduction? |
|---|---|---|
| `p`, the non-compact directions | 24 | **yes** — opposite Killing signature |
| SM inside `k` | 12 | no |
| **non-SM directions inside `k`** | **9** | **no** |

Those nine are the standard Pati-Salam remainder: 6 leptoquarks, 2 `W_R`, and
1 `Z'`.

## Consequence — PV-1's first escape is closed

PV-1 offered two readings: either GU's gauge-boson masses come from observation
rather than VEVs, or the extra massless vector is a genuine problem. **The
first reading fails.** The residual `U(1)` PV-1 found, and its eight companions,
live in `k` — precisely the summand the reduction does not touch. Observation
removes only the 24 non-compact directions of `p`.

So the surviving nine still require a genuine mass, obtainable only from a VEV,
and PV-1 showed the vacuum that would supply it (`v_PSB` in `(10bar,1,3)`, a
sub-block of the 126) is unavailable in GU's declared field content — MJ-2 gives
the 126 multiplicity exactly zero in both bosonic fields, MJ-5 shows no
SM-singlet with `B-L != 0` exists in either.

**Composed result: within GU's declared field content, nine non-Standard-Model
gauge bosons remain massless, and neither of GU's two breaking mechanisms can
give them mass.**

## What this does NOT establish

**The `p` directions are shown to carry the opposite Killing signature, not to
be successfully removed.** Wrong-sign kinetic terms make them ghost-like, and
the channel's decision question does allow extra directions to be made
"massive **or unphysical**" — but whether a wrong-sign sector is consistently
removed is a quantization question about the physical state space, not a
group-theoretic one. The repository has live work bearing on exactly that
(`W173` BRST cohomology mirror sector, `W132` graded optical theorem physical
subspace), and **this artifact does not decide it and does not claim the 24 are
disposed of.** The result above is independent of that question, because it
concerns the 9 directions in `k`, which are unambiguously healthy-sign.

**No claim about SG4.** Canon establishes the field-space declaration as the
open decider; a completion may declare a field that supplies the missing VEV.
This is a statement about GU-as-declared.

**No mass matrix is computed.** The claim is that the reduction leaves the nine
untouched, which is a statement about which summand they occupy, not about the
size of any mass they might acquire from machinery not modelled here.

## Standing after PV-1 and PV-2

The channel's decision question — *does any presently admissible
symmetry-breaking orbit leave exactly the SM massless gauge sector while making
the extra `U(1)` and other non-SM directions massive or unphysical?* — is
answered **no for GU-as-declared**, by both available mechanisms:

- **VEV route:** minimum unbroken dimension 13, never 12 (PV-1).
- **Observation route:** reaches only `p`; all 9 non-SM compact directions
  survive (PV-2).

This is the channel's declared evidence endpoint: *an obstruction showing that
the available orbit classes retain unwanted light vectors*. It is reached, and
it is stronger than PV-1 alone because it closes the mechanism PV-1 could not
model.

## Next in-channel gate

PV-3: the honest remaining question is whether the wrong-sign `p` sector is
consistently removable at all — the quantization question above. If it is not,
the problem is worse than nine extra massless vectors, since 24 ghost-like
directions would also need disposal; if it is, the machinery that removes them
may or may not extend to `k`. That gate should reuse `W173`/`W132` rather than
restart, and it belongs to whoever owns the physical-state-space work.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
