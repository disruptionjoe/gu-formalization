---
title: "Hostile review: Wave A-2 cosmology and W230-to-FLRW bridge"
status: process
doc_type: hostile-review
created: 2026-08-03
object_under_review: "explorations/de-pipeline-certification-and-bridge-test-2026-08-03.md and tests/de-certification"
verdict_summary: "MUST-FIX absorbed: internal consistency and proxy witnesses survive; C10, M-H13, and the native bridge remain open"
---

# Hostile review: Wave A-2

## Verdict

`A2 = OPEN_REBASE_REQUIRED`. The repaired computations are useful, but none supplies
the missing GU-native record law or connection-to-FLRW map.

## Findings absorbed

1. The FLRW scalar `B` and W230's full connection distortion are `UNCERTAIN` as the
   same object. The observation, pullback, projection, normalization, and equation
   maps have not been composed.
2. W230's `c_kin` and the finite `L` are placeholders for the unbuilt native
   `Z_U=|D_AU|²` contribution. A random fixture is not the action-derived operator.
3. The exact fixed-source ray condition is `Lt` proportional to `Mt`, for
   `t=M^{-1}J`. The planted nonzero choice `L=M` preserves the ray, refuting the
   draft's universal nonzero-stiffness implication.
4. The H44 massless-fibre run retains the normalized `B''` term. It models
   `(c_b,c_f)=(1,0)`, not simultaneous removal of both coefficients.
5. The reported DESI `w0wa` shape is selected from the same data. DE-12 is an
   in-sample consistency check, not an independent positive control, pipeline
   unbiasedness proof, or C10 certification. Its amplitude-only AIC diagnostic omits
   the shape-selection complexity.
6. `rho_X` and the optimization families are external proxies, not a derived record
   law. Positive witnesses prove proxy feasibility; a local optimizer could not prove
   global infeasibility.
7. The H46C A3 ratio correction was missing from the first inverse run. After repair,
   `S(0)=33.500` and the stored `+19.3` gap is reproduced as `19.346`.

## Licensed statement

The likelihood machinery internally reproduces its stored rows, and simple proxy
families—including monotone and `N^p` families—contain curves that recover the shape
target. The native construction burden is therefore sharper: derive the record law
and the connection-to-FLRW coefficient map, then measure their constraint surplus.
No bridge failure, C10 certification, or M-H13 no-go is licensed.
