---
artifact_type: exploration
status: exploration
doc_type: conditional-carrier-gate
created: 2026-08-14
work_item: MJ-2
channel: majorana_126_neutrino_mechanism
title: "MJ-2 the 126 has no native carrier in GU's stated field content: the 126 occurs in NO Lambda^k(10) except k=5, and neither bosonic GU field reaches it -- eps (Omega^0 (x) ad) gives Lambda^2(10)=45 and $ (Omega^1 (x) ad) gives 10 (x) 45 = 10+120+320, both with 126-multiplicity exactly zero. The elementary-carrier route is killed; the nu-nu condensate route survives."
grade: "EXACT integer representation theory: Racah/Klimyk multiplicities over the full 1920-element Weyl group of D5, weight multisets enumerated from scratch, highest weights certified by the Weyl dimension formula, 34/34 checks, no floating point and no external character table. NOT: a statement about SG4's undeclared completion, a kill of the 126 mechanism itself, or a kill of neutrino mass in GU."
disposition: NO_NATIVE_ELEMENTARY_126_CARRIER__126_MULTIPLICITY_ZERO_IN_BOTH_GU_BOSONIC_FIELDS__TILTED_GROUP_ROBUST__CONDENSATE_ROUTE_NOT_YET_FALSIFIED__SG4_COMPLETION_OUT_OF_SCOPE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md
  - docs/paper-formalization-candidates.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/shiab-existence-cl95.md
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
scripts:
  - tests/channel-swings/joe_directed_majorana_126_carrier_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `CONVENTIONAL_COMPARATOR`.

# MJ-2 — the 126 has no carrier in GU's stated field content

## Decision question

MJ-1 established that the SU(5)-singlet direction of the 126 gives an exact,
symmetric, rank-one Majorana block on `nu_R` alone. That result is conditional
on a VEV. **Does GU's own field content contain anything that could carry
one?**

**Answer: no, for every bosonic field GU declares.** The elementary-carrier
route is killed. This converts MJ-1's conditional mechanism into a located
structural gap, which is the more useful object.

## Setup

GU's native field content (paper 5.1-5.2; repo candidate 2B) is the 2x2 table

|      | `Omega^0`           | `Omega^1`                |
|------|---------------------|--------------------------|
| `ad` | `eps` (gauge field) | `$` (displacement)       |
| `S/` | `nu` (Dirac)        | `zeta` (Rarita-Schwinger) |

A Lorentz-scalar VEV cannot carry a free 4d index, so every form index must be
internal. That fixes the only available Lorentz-scalar internal content:

- `eps`: `Lambda^2(10) = 45`, the internal adjoint;
- `$`: `Lambda^1(10) (x) Lambda^2(10) = 10 (x) 45`.

`nu` and `zeta` are 4d spinors; an elementary VEV for either breaks Lorentz
invariance, so they are excluded on Lorentz grounds and appear below only as
composites.

## Result

Exact multiplicities by the Racah/Klimyk formula over the full 1920-element
Weyl group of `D5`, with weight multisets enumerated from scratch and every
highest weight independently certified by the Weyl dimension formula:

| target | content | mult(126) | mult(126bar) |
|---|---|---|---|
| `eps` | `Lambda^2(10) = 45` | **0** | **0** |
| `$` | `10 (x) 45 = 10 + 120 + 320` | **0** | **0** |

And the structural reason, verified rather than asserted:

> **The 126 occurs in no `Lambda^k(10)` for any `k` except `k = 5`.**
> Multiplicity profile over `k = 0..5`: `[0, 0, 0, 0, 0, 1]`.

So the 126 has a unique wedge home, and only a genuine **internal 5-form** can
carry it. GU's bosonic fields reach internal tensor degree at most three
(`10 (x) 45`), and that product decomposes as `10 + 120 + 320` with no 126
anywhere in it.

**Tilted-group robustness.** GU's structure group is tilted, and the exact
subgroup is not needed here: for any `H` inside `Spin(7,7)`, `ad(H)` is a
subrepresentation of `Lambda^2(V_14)`, whose Lorentz-scalar internal part is
`Lambda^2(10)`. Multiplicity is monotone under subrepresentation, so
`mult(126) = 0` there forces `mult(126) = 0` for every such `ad(H)`. The
negative does not depend on resolving the tilt.

**Fork robustness.** As in MJ-1, every statement is a complexified-internal
statement about `Spin(6,4)`, which both horns of SIGNATURE-AMBIENT share.

## What this kill targets, and what it does not

Per the claim-indexed verdict doctrine, the target claim is stated exactly:

**Killed:** *that GU's stated field content contains an elementary carrier for
a 126 VEV, and hence that the MJ-1 Majorana mechanism can be switched on from
GU-as-declared.* This is a **candidate kill of the elementary-carrier route**,
exact and tilted-group robust.

**Not killed, and not addressed:**

1. **The MJ-1 mechanism itself.** The block is still exact, symmetric,
   rank-one, and SM-preserving. Nothing here touches it.
2. **Neutrino mass in GU.** This is one route among several; a route kill would
   additionally require excluding condensates, higher-dimension operators, and
   radiative mechanisms.
3. **Whatever SG4 declares.** `canon/gu-forces-field-space-declaration-RESULTS.md`
   establishes that GU-as-stated does not force a unique completion and leaves
   a measured 2-bit residual, and that **SG4 -- the source action's field-space
   declaration -- is the open decider**. An SG4 completion is free to declare
   fields outside the 2B table. This artifact is scoped to GU's *stated*
   content and says nothing about that freedom.
4. **The condensate route.** See below.

## The surviving route (hands to MJ-3)

The one route this does not touch is a **composite**: a `nu (x) nu` condensate
in the 126 direction would supply the VEV dynamically without any elementary
5-form field. That route is not speculative here — MJ-1 computed exactly this
bilinear and showed it reaches the 126 with the right symmetry, rank, and
support. So the two gates compose:

- MJ-1: the `nu (x) nu -> 126` channel exists, is symmetric, is rank one on
  `nu_R`, and is SM-preserving.
- MJ-2: no elementary field can source it.
- MJ-3 (next): can the `nu (x) nu` condensate itself, or a
  higher-dimension/radiative operator, supply the scale — and does GU's action
  contain anything that could drive it?

MJ-3 is the honest next in-channel gate. Selection stays inside this channel;
repository-wide GU priority is unchanged, the superposition / source-residual
workstream is untouched, and no ledger, canon, or current-state surface moves.
