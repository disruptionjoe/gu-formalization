---
title: "GU actual-Y14 Euler receiver ordering: Weinstein/Curt source reinspection"
date: 2026-08-05
status: SOURCE_COLLISION_COMPLETE
grade: "Timestamped source disposition. The public material confirms section pullback of upstairs data and guides a curvature-to-one-form contraction, but does not identify direct pullback of the density-dual 13-form Euler row, primalize-before-observe ordering, an action-image horizontality theorem, or a receiver for the ten normal equations."
---

# GU actual-Y14 Euler receiver ordering source reinspection

## Question

The preceding construction typed the translation Euler row as a density-dual
13-form on the fourteen-dimensional observerse.  What do Weinstein and Curt
actually say about taking that equation to four dimensions?

Layer 0 distinguishes four operations:

1. pull back an upstairs **field** along a metric section;
2. pull back an upstairs **13-form** as a differential form;
3. primalize the density-dual 13-form to an upstairs one-form and then restrict
   that one-form to the section; and
4. integrate a form along the ten-dimensional metric fibre.

These operations are not synonyms.

## Checked source rows

| source | locator | source content | disposition |
| --- | --- | --- | --- |
| Weinstein, UCSD 2025 transcript | local transcript paragraphs 35, 116 and 119 | `Y14` is the quantum arena, `X4` the classical arena; a metric is a section of its bundle; data and spinors upstairs can be pulled back | `SOURCE-CONFIRMS` section/field pullback grammar |
| Weinstein--Jaimungal 2025 | `01:36:35--01:36:56` | Weinstein corrects “projection” to “contraction” and describes an Einstein/GU contraction taking curvature two-forms to a one-form in the Euler--Lagrange equation | `SOURCE-GUIDES` a one-form equation reading; not the Hodge/density or observation formula |
| Weinstein 2021 draft through the primary-source pack | equations `9.1--9.7`, `9.18--9.20` | the action and variation place the translation and fermionic connection contributions in the `d-1` density-dual Euler arena | `SOURCE-CONFIRMS` the upstairs 13-form typing at `d=14` |
| Curt Iceberg | `01:40:01--01:42:55` | after pullback, the gauge potential decomposes into horizontal gauge and vertical scalar-like components | `CURT-RECONSTRUCTS / ERIC-GUIDES`; this is field decomposition, not a proof about the Euler dual |
| Weinstein, UCSD 2025 | local transcript paragraph 161 | the vertical tangent space is ten-dimensional, the horizontal cotangent contribution is four-dimensional, and the Frobenius fibre metric is trace-reversed | `SOURCE-CONFIRMS` the `10+4` geometry and trace reversal |

The checked public sources do **not** say:

- that `s*:Omega13(Y)->Omega13(X)` is the physical equation receiver;
- that the Hodge/Krein primalizer is applied before or after observation;
- that the action Euler image is horizontal along the observation section;
- that the ten conormal equation components are gauge or constrained;
- that a fibre pushforward supplies the observed one-form; or
- that the resulting section image is a common closed Green domain.

Those rows are `SOURCE-SILENT`.

## Collision result

The sources correct a tempting but impossible reading.  Ordinary pullback
preserves form degree, so a 13-form pulls back to zero on a four-manifold.  The
source-supported candidate is instead consistent with

\[
\Omega^{13}(Y,E^*)
\xrightarrow{R_{\mathfrak g,B,\mu}}
\Omega^1(Y,E)
\xrightarrow{s^*}
\Omega^1(X,s^*E),
\]

because the draft supplies the density-dual Euler row, the K77 work supplies
the primalizer, and Weinstein's spoken description treats the contracted
Euler object as a one-form.  The *composition* is a reconstruction, not a
source formula.

This route still forgets the conormal part of the one-form.  Neither Weinstein
nor Curt identifies that loss with gauge, proves it absent from the action
image, or supplies a normal receiver.  The correct source disposition is:

- `SOURCE-CONFIRMS`: observerse sections, field pullback, `10+4` decomposition,
  trace reversal, and the upstairs Euler arena;
- `SOURCE-GUIDES`: interpret the contracted/primalized Euler object as a
  one-form before comparing it with a four-dimensional connection equation;
- `SOURCE-SILENT`: ordering as an explicit formula, conormal no-leakage,
  vertical receiver, common domain, and physics identification.

## Construction consequence

Within the ordinary primalize-then-restrict class, the source action now has a
precise burden.  It must either derive

\[
(1-H_s s^*)\,R_Y\Upsilon_T=0
\]

on its actual Euler image for a source/geometrically owned horizontal lift
`H_s`, or retain and type the ten normal receiver components.

There is also a distinct action-level route: pair the ambient density with a
genuine codimension-ten current/induced density and vary the resulting
four-dimensional action.  The previous N3 construction already derived the
first variation of a moving defect, but the checked Weinstein/Curt sources do
not specify the complete weld or its relation to the displayed Euler row.
Literal pullback of the ambient 14-form is no better than literal pullback of
the 13-form: both vanish by degree.  P1, P2 and P3 do not currently supply the
missing functional constraint or density reduction, and no new datum is
invented in this source pass.
