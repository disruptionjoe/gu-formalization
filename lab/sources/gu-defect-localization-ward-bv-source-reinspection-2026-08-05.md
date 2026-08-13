---
title: "GU defect localization, moving section and Ward/BV source reinspection"
date: 2026-08-05
status: source_receipt
named_gate: K77_FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_MOVING_SECTION_WARD_BV_DESCENT
---

# Defect localization and Ward/BV source reinspection

## Question

When the K77 action is read on a moving four-dimensional observation section,
which parts of the localization, first variation and symmetry descent are
actually supplied by Weinstein, which are already constructed in the repo,
and which remain new reconstruction work?

## Source ledger

| source | locator | source statement | disposition for this wave |
| --- | --- | --- | --- |
| 2021 working draft as transcribed in `weinstein-gu-primary-source-pack-2026-07-30.md` | `WGS-01`, draft (9.1)--(9.7) | `I1B` contains `F_B + (1/2)d_BT + (1/3)[T,T]` paired with the full `T in Omega1(Y,ad P)`, and displays the translation first variation | `SOURCE-CONFIRMS` a first-order ambient action and therefore a normal-jet question; it does not give a defect localization |
| same | `WGS-03` | the eddy/Chern--Simons completion is required for exactness | `SOURCE-CONFIRMS` that the complete density, not a curvature-only shortcut, is the localization target |
| same | `WGS-04`, draft (9.5)--(9.6) | `Xi=D Upsilon` is a displayed redundancy | `SOURCE-CORRECTS`: this is not automatically an off-shell Noether identity or BV master equation |
| Portal/Oxford transcript | `01:41:26--01:45:53` | the curvature/Shiab and augmented-torsion objects compensate their common tilted-gauge failure | `SOURCE-CONFIRMS` intended even equivariance of the completed pair, not a complete global Ward proof |
| Portal/Oxford transcript | `01:48:59--01:51:50`, `02:32:38--02:33:13` | augmented torsion is the difference of two connection operators | `SOURCE-CONFIRMS` that both connection owners must move in the Ward identity |
| Portal/Oxford transcript | `02:04:18--02:05:04` | the construction is upstairs on `U^14` and must be read through a section/pullback on `X^4` | `SOURCE-CONFIRMS` the observation obligation; `SOURCE-SILENT` on the measure-theoretic localization operation |
| TOE 2025 as recorded in the source pack addendum | `01:43:43--01:44:14` | an action for the odd super-extension is declined as unnecessary for doing GU | `SOURCE-CORRECTS` the inherited assumption that a full odd Ward/BV action is a default prerequisite |
| N1 source/datum packet | Layer-0 register and field maps | the packet uses the current measure `mu_Y+s_*mu_X`, distinguishes coefficient restriction from pullback, and already defines the bulk-plus-defect carrier | `REPO-CONFIRMS` the current language and warns against pretending the defect is a smooth ambient density |
| N3 variational emission map | moving-defect derivative | intrinsic variation and support motion are separate; `delta_s(s^*A)=s^*(i_VF_A)+D_A(s^*i_VA)` | `REPO-CONFIRMS` the moving-current chain rule; this wave extends it to first jets and induced-density motion |
| Wave-2 action/Ward rendezvous | sections 3 and 6 | `B(epsilon)`, moving Shiab, connection, background and current owners all enter the even Ward contraction | `REPO-CONFIRMS` the complete-owner burden; localization may preserve such an identity but cannot manufacture omitted transformations |

## Layer 0

| phrase | object used here | object not identified with it |
| --- | --- | --- |
| pullback | restriction of fields/forms by `s` | integration of an ambient top density over a codimension-ten defect |
| defect localization | evaluate the scalar coefficient of an ambient density on `j^1s` and multiply by the induced section density | literal `s*` of a fourteen-form |
| vertical density | orientation-free measure factor/current normalization | a chosen vertical volume form or P1 |
| first-jet trace | values of all ambient first derivatives along the section | the zero-jet four-plus-ten coefficient field |
| Ward identity | contraction of every Euler owner with one complete even symmetry generator | `Xi=D Upsilon` alone |
| even BV descent | standard minimal BV construction for a written closed nilpotent even action | an odd super-IG action, physical BFV phase space or Green domain |
| localized source action | the localization functor applied to the complete written density | a decision to replace the bulk action or add a second copy with a selected relative normalization |

## Verdict

1. `SOURCE-CONFIRMS`: the complete ambient action is first order and uses the
   full augmented-torsion one-form; the completed curvature/torsion pair is
   intended to be even-equivariant; observation on `X` is required.
2. `SOURCE-CORRECTS`: `Xi=D Upsilon` is not the needed off-shell Ward/BV
   identity, and a full odd action is not a default source prerequisite.
3. `SOURCE-SILENT`: the canonical induced-density defect localization, its
   normal-dipole Euler distribution, moving-section shape equation, patch
   descent, actual conormal Legendre coefficient, bulk/defect relative
   normalization and common domain.
4. `REPO-CONFIRMS`: the current map and moving-support derivative already
   exist, so the new work must extend them rather than rediscover them.

The source review therefore licenses an even localization/descent
construction, not a shortcut. It also forces the next coefficient test: does
the actual moving K77 Shiab/I1B density have a nonzero conormal Legendre
symbol, or does its completed structure factor through the section jet?
