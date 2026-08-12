---
artifact_type: source_return
created: 2026-08-12
run_id: RUN-20260812-043842-gu-trace-hq-connection-internal-chain
status: SOURCE_CONFIRMS_FULL_UNITARY_PARENT_TRACED_FIBRE_STAGE_PATI_SALAM_U3_2_INTERSECTION_AND_VARPI_HIGGS_ASSIGNMENT__SOURCE_SILENT_ON_HQ_COMPATIBILITY_AND_TRACE_Q_AS_BREAKING_VECTOR
---

# Source return: trace-Hq connection versus the internal chain

## Question

Does the source identify the trace-owned `H_q` as the Hermitian form preserved
by the operative connection, or use trace q as the Pati-Salam/Standard-Model
breaking vector or physical Higgs?

## Return

- `SOURCE-CONFIRMS` (`SC-GRP-01`, `SC-GRP-02`): the authorial parent is the
  full `U(64,64)` bundle; this is not automatically the selected K77
  split-spin connection or two independent `U(32,32)` connections.
- `SOURCE-CONFIRMS` (`SC-GRP-03`): the printed chain already contains
  `Spin(1,3)xSpin(6,3)xSpin(0,1) -> Spin(1,3)xSpin(6,4)`, and locates the
  Standard Model in the intersection of the full Pati-Salam maximal-compact
  and `U(3,2)` reductions.
- `SOURCE-CONFIRMS` (`SC-SIG-52`): choosing the proper trace sign makes the
  full normal `Spin(6,4)` route naturally Pati-Salam `Spin(6)xSpin(4)`.
- `SOURCE-ASSERTS` (`SC-FER-03`, `SC-META-57`) and `SOURCE-DISAVOWS`
  (`SC-GEO-58`): Higgs-like/CKM/Yukawa/gauge functions live in components of
  the ad-valued one-form `varpi`; there is no separate fundamental Higgs.

The checked source does not print `H_q=iB gamma(g/2)`, does not state
`D_varpi H_q=0`, does not identify trace q with the independent `(4,1,2)`
Pati-Salam breaking vector, and does not identify the nine `D H_q` defect
directions with the physical scalar doublet.

## Disposition

```text
SOURCE-CONFIRMS:
  full U(64,64) parent;
  a Spin(6,3)xSpin(0,1) traceless-plus-trace stage;
  full Spin(6,4) Pati-Salam and separate U(3,2) intersection route;
  varpi one-form custody of Higgs-like/Yukawa functions.

SOURCE-SILENT:
  trace H_q as the parent Hermitian form;
  D_varpi H_q=0;
  trace q as the SM-breaking vector;
  the physical identity of the rank-nine connection defect.

REPO-DERIVES:
  fixed-q split-spin compatibility is Spin(1,3)xSpin(6,3);
  D H_q has rank nine and reconstructs the broken connection exactly;
  fixed q removes full Pati-Salam and intersects the existing v_PSB
  stabilizer in dimension nine, not twelve.
```

This is a source-guided correction, not a source contradiction.  The source's
explicit `U(3,2)` intersection becomes mandatory because the fixed-q shortcut
does not recover the Standard Model representation.
