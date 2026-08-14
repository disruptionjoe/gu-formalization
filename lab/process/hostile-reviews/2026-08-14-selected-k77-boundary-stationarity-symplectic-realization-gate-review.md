---
title: "Hostile review: K77 boundary stationarity and symplectic realization"
created: 2026-08-14
status: PASS_AFTER_LOCAL_GLOBAL_AND_OWNERSHIP_NARROWING
subject: explorations/conditional-build/selected-k77-boundary-stationarity-symplectic-realization-gate-2026-08-14.md
---

# Hostile review

## Findings

1. **Overclaim: the 98-dimensional model is the smallest equivariant edge
   theory.** Rejected. The proof establishes the lower bound for a symplectic
   realization over an open regular Lie--Poisson neighborhood and exhibits a
   sharp local split model. It does not globalize the model or prove
   `Spin(7,7)` equivariance. The report now bounds the unknown global
   equivariant minimum between 98 and the 182-dimensional cotangent fallback.

2. **Hidden assumption: stationarity locks the existing nonzero charge.**
   Rejected. Free bare-action stationarity sets the endpoint momenta and charge
   to zero, so the tested nonzero fixture is excluded. Dirichlet data kills the
   variation without killing momentum. A nonzero locking graph requires an
   added boundary functional and seven independent tangency conditions.

3. **Contrary construction: a source-derived boundary functional could select
   one nonzero orbit.** Survives. Nothing here excludes it. No such functional
   is presently source-owned or derived, and choosing one to reproduce the
   desired invariants would be fitting.

4. **Reproducibility seam: the dimension theorem could be only numerology.**
   Corrected. The report gives the Poisson-submersion lower-bound argument,
   the `84+2*7=98` local split construction and the `2*91=182` cotangent
   control. The probe imports the exact predecessor rank/corank and exercises
   planted boundary-graph and claim-ceiling controls.

5. **Physical seam:** no boundary dynamics, trace space, global BFV phase
   space, polarization, positive pairing, domain or cohomology is constructed.
   This remains explicit.

## Lens disposition

- Variational bicomplex: pass; free, fixed and generated boundary classes are
  separated.
- Symplectic/Poisson geometry: pass after local/global narrowing.
- Lie/invariant theory: pass; all seven regular invariant differentials remain
  load-bearing.
- BFV: scoped pass; zero charge, charged symmetry and edge cancellation remain
  distinct horns.
- Source criticism: pass; boundary functional and edge carrier are unowned.
- Analytic/PDE: open by design; no domain conclusion is inferred.
- Philosophy of science: pass; mathematical availability is not reported as
  physical derivation.

## Verdict

Pass at exact local variational/Poisson grade. The bare-action nonzero-locking
horn is rejected; the 98-dimensional local realization and 182-dimensional
global fallback are valid. The smallest global equivariant carrier, physical
boundary choice and analytic theory remain open.
