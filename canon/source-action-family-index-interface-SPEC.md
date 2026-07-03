---
title: "Interface crosswalk: what the GU source action (absorbed/gu-source-action) must expose to CLOSE the RS family-index crux (STEP 3 of WC-FUNCTION-SPACE-EXT). Maps the source-action SPEC's three global objects 5(i)-(iii) onto the rs-function-space harness's open obligations, records that STEP 2 (boundary eta) already lands the source-action's 'single decisive object' on the eta=0 / 2-primary branch, and states the exact pass criterion: a families-pushforward index N over the metric fiber GL(4,R)/O(3,1) with N != 0 mod 3, WITHOUT importing chi (honest ch2(S_X)[K3] = -5376, not 24)."
status: staged
doc_type: spec
created: 2026-07-03
grade: "SPEC / crosswalk. No new number; ties two existing campaigns (gu-formalization RS family index + absorbed/gu-source-action) through one interface. The honest data it rests on (ch2=-5376, APS eta=0, RS boundary eta 2-primary) is computed/exact and target-import-safe. Internal tier (caveat (e))."
depends_on:
  - canon/rs-function-space-framework-SPEC.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/firewall-boundary-hypothesis.md
scripts:
  - tests/rs-function-space/k3_family_pushforward_scaffold.py
  - tests/rs-function-space/family_generation_arena_probe.py
---

# Source-action <-> family-index interface (closing the STEP 3 crux)

The RS function-space residual (`rs-function-space-framework-SPEC.md`) and the GU source-action build
(`absorbed/gu-source-action/SPEC.md`) point at the SAME missing object from two sides. This note wires
them through one interface so the source-action build, when it lands, plugs straight into the
family-index harness -- and states exactly what it must deliver.

## The crosswalk

| RS family-index obligation (STEP 3) | source-action global object (SPEC 5) | status |
|---|---|---|
| (1) fiber model: `K3`-fibered bundle | 5(i) families pushforward over the metric fiber `GL(4,R)/O(3,1)` | both UNBUILT; harness product-model scaffolded |
| (2) compact-support / APS pushforward `pi_!` | 5(i) + 5(ii) | fiberwise `pi_!` scaffolded; noncompact end OPEN |
| (STEP 2) boundary / APS eta on `L(2;1)` | 5(ii) Y14 boundary holonomy / spectral section | **DONE, 2-primary** (`rs-boundary-eta-2primary-RESULTS.md`) |
| (3) `Phi`-homotopy / symbol certificate | 5(iii) BV-to-boundary-Dirac map (symbol family of the GU RS op) | OPEN |
| (4) `ch2` / eta correction -- THE CRUX | 5(iii) tying the Koszul-Tate differential to a geometric boundary Dirac whose APS section connects to `C2` | OPEN; honest `ch2(S_X)[K3] = -5376` |
| (5) `H`-line normalization | the `H`-line scale on the base | OPEN |

**Convergence already banked.** The source-action campaign's own "single decisive object"
(`absorbed/gu-source-action/DERIVATION-PROGRESS.md`) is: replace the auxiliary spectral-flow strength
`t` by the a-priori Y14 boundary connection (5(ii)) and ask whether the geometry selects a *flowing*
breaker (nonzero eta) or the `M_D`-symmetric (`eta = 0`) one. **STEP 2 answers the analog for the
sector's own boundary: the RS boundary operator sits in the `eta = 0`, 2-primary class** (net self-dual
frame charge `0`; `rs-boundary-eta-2primary-RESULTS.md`). That is evidence for the `eta=0` branch, not
the flowing one -- i.e. the boundary does not source a count.

## What the source action MUST expose to the harness (the interface)

To compute obligation (4) through `tests/rs-function-space/` (rather than rebuild machinery), a valid
`S_IG` must hand over, all **without importing chi**:

1. **Vertical bundle + clutching** over the metric fiber `GL(4,R)/O(3,1)` -- the actual `K3`-fibered
   family (5(i)), as a bundle with connection, not a product. (Feeds obligation 1.)
2. **The a-priori Y14 boundary connection** replacing the auxiliary `t` -- so the APS spectral section
   is geometric, not a free strength (5(ii)). (Feeds obligation 2 + the STEP-2 boundary term.)
3. **The family symbol** of the GU RS operator -- a `Phi`-homotopy or symbol certificate (5(iii)).
   (Feeds obligation 3.)
4. **The `ch2` / eta correction** as an actual families-index number `N`, plus the **`H`-line
   normalization** scale (5(iii) + obligation 5). (Feeds obligation 4 + 5 -- the crux.)

## Pass / fail criterion (the hard bar, firewall-guarded)

> The families-pushforward index `N` over the metric fiber must satisfy **`N != 0 mod 3`** (so
> `e = N/24` keeps a factor of 3 and reaches the order-3 generation arena) -- and it must do so
> **WITHOUT** using `chi(K3)=24`, the `/8` normalization, `Ahat=3`, or `contractible-fiber => 1`
> (all DEAD-ENDS.md automatic fails).

On ALL existing honest data the value is `0 mod 3` (`family_generation_arena_probe.py`: `-42, -672,
-5376, 0` are every one `== 0 mod 3`; honest `ch2 = -5376`, not `24`). So:

- **If** the geometric families pushforward forces `N != 0 mod 3` without a chi-import: GU forces the
  count internally -- the firewall-boundary hypothesis is **falsified** for this sector, and
  "external by structure" would NOT be needed.
- **If** it stays `0 mod 3` (or `N` is free): the count is **not** internally sourced -- "external by
  structure" becomes unconditional and the firewall-boundary reading is supported. The SPEC's hard bar
  (`ch2 = -5376`, `APS eta = 0`) currently points here, and warns this may be the unreachable outcome.

Either way the crux is now a single, well-posed, firewall-guarded integer question, and the two
campaigns share one interface to attack it. Staged, not CANON.md-promoted; pauses for Joe.
