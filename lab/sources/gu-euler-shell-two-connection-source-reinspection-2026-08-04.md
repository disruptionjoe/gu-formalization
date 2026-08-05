---
artifact_type: source_reinspection
created: 2026-08-04
title: "Source reinspection: Euler shell and the unreleased two-connection complex"
---

# Source reinspection: Euler shell and two connections

## Question

Does the checked Weinstein material identify the difference of the two
connections with the primalized Euler derivative of the released first-order
bosonic action?

## Receipt

| source surface | source statement | classification | consequence |
|---|---|---|---|
| `lab/sources/transcripts/toe-weinstein-gu-40-years.md` | gives `d_A,-F_B,1,-d_B`, two second-column minus signs, and says that on shell “a complex is birthed” | `SOURCE-CONFIRMS` | establishes the four-block target and on-shell motivation |
| same TOE passage | says the cyclic construction was created but never released | `SOURCE-CONFIRMS-ABSENCE` | reverse engineering cannot be attributed as the published formula |
| `portal-special-gu-first-look-2020-04-02.md` | one inhomogeneous-gauge element yields two connections; their difference is an honest ad-valued one-form/augmented torsion | `SOURCE-CONFIRMS` | a connection difference is the right geometric carrier |
| rendered draft equations 9.4--9.6 | `dI_1^B=(Upsilon,Xi)` in degrees `d-1,d` and generally `Xi=D Upsilon` | `SOURCE-CONFIRMS` | the action row is density-dual; the second row is described as redundant |
| rendered draft equations 9.7--9.10 | swervature/displasion endpoint presentation | `SOURCE-CONFIRMS-ADVERTISED-ENDPOINT` | source target exists but is not automatically the written action's actual noncyclic derivative |
| K77-B3 plus action/Ward rendezvous | noncyclic full-domain endpoint differs from the actual symmetrized derivative | `REPO-CORRECTS-USE` | the lift must use `E_T^{B,act}`, not substitute the advertised endpoint |
| RB1 current musical | `sharp_conn=*^{-1} kappa^sharp` maps degree-13 coadjoint densities to degree-1 adjoint forms | `REPO-CONFIRMS` | required carrier conversion already exists |
| K77 moving primalizer packet | exact moving inverse and transition naturality | `REPO-CONFIRMS` | K77 port has inherited infrastructure |
| all checked source surfaces | no formula `A-B=sharp_conn(E_T^{act})` and no faithful coefficient-module theorem | `SOURCE-SILENT` | the present lift is a conditional reconstruction |

## Layer-0 ruling

The following are not identified by source language:

1. IG augmented torsion `A_IG-B_IG`;
2. the unreleased TOE two-connection difference;
3. the primalized advertised `Upsilon`;
4. the primalized actual action Euler covector; and
5. a connection difference after a physical/BV quotient.

The construction in this wave uses item 4 and labels the relation to item 2
`SOURCE-COMPATIBLE-CONDITIONAL`, not `SOURCE-CONFIRMS`.

## Source result

```text
SOURCE-CONFIRMS: ingredients, carrier, action degrees, on-shell motivation
SOURCE-CORRECTS: use actual noncyclic Euler derivative in the lift
SOURCE-SILENT: Euler-primalized pair identification and faithful physical module
```
