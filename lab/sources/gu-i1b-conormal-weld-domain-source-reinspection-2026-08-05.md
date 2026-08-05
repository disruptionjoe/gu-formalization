---
title: "Source reinspection: I1B conormal symbol, observation weld and domain"
date: 2026-08-05
status: source_collision_receipt
lane: 1
source_collision: SOURCE_CONFIRMS_UPSTAIRS_ACTION_FIXED_EPSILON_TRANSLATION_AND_PULLBACK_OBSERVATION__SOURCE_GUIDES_NO_DUPLICATE_WELD__SOURCE_SILENT_ON_PREFERRED_SHIAB_NORMAL_DENSITY_NORMALIZATION_AND_DOMAIN
---

# Source reinspection: I1B conormal symbol, observation weld and domain

## Question

When the first-order K77 `I1B` action is observed on the four-dimensional
section, does the source instruct us to add a localized copy of the bulk
action, and does it supply enough information to compute the normal first-jet
coefficient or choose a common analytic domain?

## Findings

| source window | source content | disposition |
| --- | --- | --- |
| 2021 draft equations 9.1--9.7, transcribed in the primary-source pack | `I1B` contains `F_B + 1/2 d_B T + 1/3[T,T]`, and the displayed translation variation moves `varpi` by `s alpha` at fixed `epsilon` | `SOURCE-CONFIRMS`: the derivative-only `T` principal symbol is owned by the action grammar; a preferred Shiab is not selected |
| Portal/Oxford `01:41:26--01:44:16` | augmented torsion is the difference of two individually non-invariant connection objects with the same failure; it is combined with Shiab-curvature in the equation | `SOURCE-CONFIRMS`: vary the covariant difference, not one connection owner in isolation |
| Portal/Oxford `02:04:18--02:05:04` | work has been done on `U/Y`; “all the action” is upstairs, and the next question is what pulled-back fields look like on `X` | `SOURCE-GUIDES`: observation is an equation/field receiver, not an instruction to add the same action again |
| Portal/Oxford `02:19:57--02:22:27` | there are fields on both spaces; most fields live on `Y` and are observed by pullback “as if” on `X`, while rarer fields may live directly on `X` | `SOURCE-GUIDES`: keep bulk fields/actions upstairs and admit only independently owned direct-`X` terms as defect actions |
| TOE 2025 `00:29:45--00:30:49` | the observerse is the package of bundles, relations and pullbacks; most GU work and the new action are on `Y14` | `SOURCE-CONFIRMS` the same ownership direction |
| TOE 2025 `00:41:50--00:43:38` | GU has an Einstein--Dirac layer and a second Lagrangian/action layer adding Yang--Mills--Higgs | `SOURCE-CORRECTS` any one-layer flattening, but does not say either layer is a localized duplicate of the other |
| checked source corpus | no complete admissible `(epsilon,varpi)` domain, no preferred Shiab selector, no normal-density normalization/transverse profile, and no Green/BFV boundary domain | `SOURCE-SILENT` |

## Layer-0 consequences

1. **Fixed-`epsilon` translation symbol versus dependent-`epsilon` symbol.**
   The draft explicitly owns the first. The second still has to compose
   `D_epsilon B`, the moving Shiab, Hodge, density and soldering owners.
2. **Pullback versus action duplication.** Pulling fields or equations back to
   `X` does not create a second variational owner. Adding `Loc_s(I1B)` beside
   `I1B` is a new reconstruction with a transverse-normalization debt.
3. **Direct-`X` term versus restricted bulk term.** The source allows both
   spaces to carry fields, but only a term with an independent `X` owner is a
   defect term without duplicating the bulk law.
4. **Two action layers versus two strata.** Einstein--Dirac and
   Yang--Mills--Higgs are source-stated Lagrangian layers. The statement does
   not identify one with a bulk term and the other with a localized copy.
5. **Preferred Shiab versus source family.** The action grammar can determine
   its principal symbol as a formula in `Shiab_epsilon`; it cannot supply a
   coefficient table until a family member is selected.

## Source verdict

`SOURCE_CONFIRMS_UPSTAIRS_ACTION_FIXED_EPSILON_TRANSLATION_AND_PULLBACK_OBSERVATION__SOURCE_GUIDES_NO_DUPLICATE_WELD__SOURCE_SILENT_ON_PREFERRED_SHIAB_NORMAL_DENSITY_NORMALIZATION_AND_DOMAIN`

The source-compatible primary construction is therefore:

```text
bulk source action(s) on Y
+ only independently owned direct-X action terms
+ pullback/equation receiver for observation
- no second localized copy of the same bulk density
```

This is a source-guided reconstruction choice, not a uniqueness theorem. A
localized-bulk rival remains admissible only if it supplies the missing normal
density/transverse profile, controls double counting, and passes the same
Ward/domain tests.
