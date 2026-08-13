---
artifact_type: source_reinspection
created: 2026-08-08
status: SOURCE_CORRECTS_DERIVATION_RATIONALE__CONFIRMS_EXPLICIT_K77_USE
source_return: SOURCE-CORRECTS
---

# Signature rationale and Build-branch source reinspection

## Result

The sources say two different things that must both be retained.

1. The 2021 draft explicitly writes `Y^(7,7)`, `Spin(7,7)` and ambient
   chirality labels.  Therefore K77 is the real Clifford carrier the released
   source actually uses.
2. Curt's displayed signature chain uses a negative-first convention.  The
   three independently checkable source pairs `(3,7)`, `(3,6)` and `(4,6)`
   are exact mirrors of the repository's plus-first `(7,3)`, `(6,3)` and
   `(6,4)`.  In that one convention, `(4,6)+(1,3)=(5,9)`, i.e. repository
   `(9,5)`, not `(7,7)`.

The source therefore **asserts/selects** K77 but does not derive K77 from its
displayed block arithmetic.  This corrects the rationale without pretending
the manuscript used K95.

## Locators

- `gu-2021-draft-s11-s12-extraction-2026-08-03.md`, §2.1: the rolled-up
  fermionic complex is explicitly labelled `Spin(7,7)+/-`.
- The same extraction, §4, equations 12.18--12.20: `X^(1,3) -> Y^(7,7)` and
  `TX^(1,3) plus N^(6,4)` are printed together.
- `curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md`,
  `00:39:55--00:42:43` and `00:46:06--00:47:20`: Curt states the vertical
  signatures, declares total K77 and motivates it using the split real spinor
  carrier; he also names `(5,9)` as an alternative.

## Layer 0 disposition

| question | disposition |
| --- | --- |
| Which real Clifford carrier does the released source use? | K77, explicitly. |
| Which inertia follows from the displayed metric blocks under one convention? | K95 in repository plus-first notation. |
| Does the source publish the additional bilinear/sign map making those blocks K77? | No. |
| Is K77 therefore mathematically forbidden? | No; it remains an author-asserted conditional carrier whose geometric owner is unbuilt. |

## Return

`SOURCE-CORRECTS`: replace “K77 derived from exact source arithmetic” with
“K77 explicitly selected by the source, while its displayed block arithmetic
derives K95.”  The source is silent on a consistent additional chimeric
bilinear that would derive K77.
