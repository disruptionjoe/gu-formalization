---
title: "WC-FUNCTION-SPACE-EXT residual closure: the three residual items of the conditional section-setting theorem -- (1) gap well-posedness, (2) the APS/noncompact-end eta term, (3) the family-index/higher-topology term -- are each DISCHARGED at computed + independently re-verified grade on faithful stand-in models, by the same cross-chirality sigma_1 (x) B mechanism that carries the interior theorem. Combined with the interior theorem (v2.8) and the external-flux certificate, the residual collapses: within the sector class, net chiral count is conserved at 0 in the section / boundary / family setting; the SOLE source of a nonzero (odd) count is an EXTERNAL topological index (flux / instanton / APS unpaired boundary mode), which is any integer, not 2-primary-constrained, and does not single out 3. The one honest caveat that remains is model -> true-RS-Y14-bundle: the general-bundle statement is the standard APS + family-index machinery applied to the same structure, asserted-by-machinery, not re-derived on Y14."
status: canon
canon_promoted_at: "2026-07-03"
doc_type: result
created: 2026-07-03
grade: "computed + INDEPENDENTLY RE-VERIFIED on faithful low-dimensional stand-in models (1D open-chain Krein-Dirac; class-generic random boundary operators; QWZ Chern-insulator family). Each residual item is discharged by the SAME structural mechanism as the interior theorem -- a chirality-odd, Krein-self-adjoint operator for cross-chirality K = sigma_1 is forced to D = sigma_1 (x) B (B Hermitian), so spec(D) = +- spec(B) is symmetric about 0. NOT a re-derivation on the true RS Y14 bundle: the general-bundle statement is standard APS/family-index machinery applied to this structure. Internal tier (caveat (e)): reproduced + internally re-verified, not externally replicated."
addresses: "WC-FUNCTION-SPACE-EXT (NEXT-STEPS.md, post-publication card) -- the three residual items left explicitly OPEN by canon/function-space-index-conservation-RESULTS.md (the v2.8 conditional theorem)."
depends_on:
  - canon/function-space-index-conservation-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - canon/antilinear-bound-RESULTS.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
scripts:
  - tests/function-space-ext/gap_wellposedness_end.py
  - tests/function-space-ext/aps_end_eta_class_symmetry.py
  - tests/function-space-ext/family_index_bundle.py
  - tests/function-space-ext/flux_index_2d.py
  - tests/function-space-ext/verify/gap_wellposedness_indep_check.py
  - tests/function-space-ext/verify/aps_end_eta_class_symmetry_indep_check.py
  - tests/function-space-ext/verify/family_index_bundle_indep_check.py
  - tests/function-space-ext/verify/flux_index_2d_indep_check.py
---

# WC-FUNCTION-SPACE-EXT: closing the analytic residual

**Card.** WC-FUNCTION-SPACE-EXT (post-publication). The v2.8 conditional theorem
(`canon/function-space-index-conservation-RESULTS.md`) established the **interior / closed,
spectral-gapped** section-setting statement: every norm-continuous family of self-adjoint,
chirality-odd, Krein-self-adjoint, Fredholm operators on the cross-chirality section space has net
chiral spectral flow exactly 0. It left **three residual items explicitly open**:

1. **gap well-posedness** of the physical (negative) spectral projection on a noncompact end;
2. the **APS / noncompact-end eta** correction (could carry an unpaired chiral piece);
3. **family-index / higher-topology** terms over the parameter space (the index bundle).

**Outcome: each item is discharged at computed + independently re-verified grade on faithful
stand-in models. The residual collapses into the paper's own thesis** -- the interior sector
conserves the chiral count at 0 in the section / boundary / family setting, and the *only* place a
nonzero (odd) count can enter is an **external topological index**, which is any integer and is not
2-primary-constrained. The failure conditions did not fire.

## The one mechanism behind all three

For the cross-chirality Krein data (`Gamma = sigma_3 (x) I`, `K = sigma_1 (x) I`), an operator that
is chirality-odd (`{D, Gamma} = 0`) **and** Krein-self-adjoint (`D^dag K = K D`) is algebraically
forced to `D = sigma_1 (x) B` with `B` Hermitian (the v2.8 proof). Therefore
`spec(D) = +- spec(B)` is **symmetric about 0**, every eigenvector is chirality-off-diagonal
`(1, +-1) (x) v`, and the physical (negative) sector is chirality-balanced. Each residual item is
the image of this one symmetry in a different analytic register: a spectral gap (item 1), a boundary
eta (item 2), an index bundle (item 3).

## Item (1): gap well-posedness on a noncompact end

**Certificate `tests/function-space-ext/gap_wellposedness_end.py` (14 asserts, exit 0).** On an
open-chain (noncompact-end stand-in) Krein-Dirac model `D = sigma_1 (x) B`, `B = m_inf I + T`
(hopping bandwidth 1): the 0-gap of `D` equals the distance of the asymptotic spectrum from 0, set
by the **end** value `m_inf`. Gapped end (`m_inf = 1.5 > bandwidth`): the gap is **stable** at
`~= 0.50` across `L = 16..128`, the physical projection `P_<0` is well-defined, and
`tr(Gamma P_<0) = 0` to `~4e-15`. Gapless end (`m_inf = 1.0 = bandwidth`): the gap **closes**
(`0.017 -> 0.0003` over `L = 16..128`), so the filled-sea count is not integer-stable. **Reading:**
well-posedness holds iff the end is gapped -- a standard analytic (weighted / gapped-completion)
hypothesis, exactly as in APS-type index theory -- and *whenever it holds, the count is 0*. The
gapless case is a failure of well-posedness itself, not a chiral leak.
*Independent re-check* `verify/gap_wellposedness_indep_check.py` (24 asserts, exit 0): seeded random
Hermitian `B` at sizes 6..48, gapped by a positive shift vs gapless; `spec(D) = +- spec(B)` to
`1e-9`, `gap = min|eig B|`, `tr(Gamma P_<0) = 0` to `~1e-14` whenever gapped -- model-independent.

## Item (2): the APS / noncompact-end eta term vanishes inside the class

**Certificate `tests/function-space-ext/aps_end_eta_class_symmetry.py` (156 asserts, exit 0).**
Upgrades the earlier hand-picked boundary control (`aps_eta_boundary_control.py`) to a
**class-generic theorem-grade symmetry**: any boundary/end operator *in the class* is `sigma_1 (x) B_bdy`,
so its spectrum is symmetric about 0 and the APS eta-at-0 and half-term `(eta + h)/2` are **exactly
0**. Verified over 30 random class draws (sizes 2..13), max spectral asymmetry `7.1e-15`,
`eta_0 = 0`, half-term `0` on every draw. Control: an **external, out-of-class** unpaired boundary
mode (odd total dimension -- no chirality involution) gives `eta_0 = +-1` and half-term `+-1/2`.
**Reading:** the boundary/end eta cannot introduce a chiral count from *inside* the sector; a nonzero
eta is exactly the external boundary datum the paper already names.
*Independent re-check* `verify/aps_end_eta_class_symmetry_indep_check.py` (50 asserts, exit 0):
different seed, complex-Hermitian and integer-valued real-symmetric `B`, sizes 4..33, and a
basis-free witness -- all **odd spectral moments** `tr(D^{2k+1}) = 0` (max `0.0e+00`) plus
`eta_0 = 0`.
*Actual-bundle corroboration (STEP 2).* This class-generic symmetry is corroborated on the true
Rarita-Schwinger side by `canon/rs-boundary-eta-2primary-RESULTS.md`: the actual RS boundary
operator's reduced eta-bar on the sector's own boundary `RP^3 = L(2;1)` is **2-primary** -- consistent
with (and stronger than) the faithful-model neutrality here, since a 2-primary boundary eta carries no
odd chiral count.

## Item (3): the family-index / index-bundle term vanishes in the class

**Certificate `tests/function-space-ext/family_index_bundle.py` (8 asserts, exit 0).** For the
family `D(t) = sigma_1 (x) B(t)` over a parameter torus, the negative bundle of `D` is
`{upper band of B} (+) {lower band of B}` (each dressed by a constant chirality-off-diagonal
vector), so `c1(E_-(D)) = c1(upper band) + c1(lower band) = 0` -- the Chern numbers of the two
bands of any gapped 2-band Hermitian cancel. Realized on a QWZ Chern-insulator `B(k)` (`m = -1`,
Fukui-Hatsugai-Suzuki Chern): `c1(lower) = -1`, `c1(upper) = +1` (each individually **nonzero** --
non-vacuous), and the `D` negative-bundle Chern is `0` to `1e-6`. **Reading:** the family / higher-
topology term is identically 0 in the class; a nonzero family term needs the negative bundle to keep
a **single** chirality/band -- an out-of-class (external topological) datum.
*Independent re-check* `verify/family_index_bundle_indep_check.py` (4 asserts, exit 0): `m = -1.6`,
grid `Nk = 32`, plus the basis-free reason the bands cancel -- the projector-completeness identity
`P_lower + P_upper = I` pointwise (dev `8.9e-16`), so the total bundle is trivial.

## The external side is already certified (any-integer, odd, not 2-primary)

`tests/function-space-ext/flux_index_2d.py` (+ `verify/flux_index_2d_indep_check.py`): a 2D
magnetic-flux Wilson-Dirac has net chiral index = flux number (Aharonov-Casher / Atiyah-Singer),
including **odd** 1, 3, 5; the flux background **breaks** the interior Krein class; the index is
**any integer -- not 2-primary-constrained and not a selection of 3**. This is the external
topological datum that items (1)-(3) show the interior cannot itself produce.

## What this closes

Combining the interior theorem (v2.8) with items (1)-(3) and the external-flux certificate: **within
the cross-chirality Krein sector class, the net chiral count is conserved at 0 across the section,
boundary, and family settings -- not just the finite carrier.** The three analytic terms that could
a priori have re-introduced a chiral count are each shown to be either identically zero in the class
(items 2, 3) or a well-posedness hypothesis rather than a leak (item 1). The **only** channel that
carries a nonzero (odd) count is an **external** topological index, which is any integer. This is
precisely the paper's "external by structure" conclusion, now with the analytic residual discharged
rather than deferred.

## What this does NOT close (honest residual)

- **Model -> true RS Y14 bundle.** Every certificate here runs on a faithful low-dimensional stand-in
  (1D open chain; 2x2 QWZ family; class-generic finite boundary operators), the same modeling grade
  as the v2.8 interior theorem. The **general Rarita-Schwinger-bundle** statement is the standard APS
  + family-index machinery applied to the same `sigma_1 (x) B` cross-chirality structure -- it is
  **asserted-by-machinery here, not re-derived on Y14**. Discharging *that* (an actual RS eta / family
  index on the noncompact `Y14`) is the residual that remains, and it is a computation, not a
  conceptual gap: the logical role each term plays in the argument is now settled.
- **Internal tier (caveat (e)).** Computed + internally re-verified; not externally replicated or
  peer-reviewed.
- **No number was fitted.** The only integers are chiralities, `0`, Chern numbers `+-1`, and the
  control flux -- none imported from a target.

## What this changes for the paper (pauses for Joe)

The v2.8 Theorem 2 / caveat (d) residual sentence ("the residual is now precisely the APS/end and
family-index analytic terms") can upgrade to: *within the sector class those terms are each
discharged on faithful models -- the section/boundary/family chiral count is conserved at 0, and the
only source of a nonzero count is an external topological index; the remaining residual is the
true-RS-Y14-bundle computation (standard APS/family-index machinery).* This is a one- to two-sentence
scope upgrade -- **not applied here**. Paper edits and `CANON.md` promotion **pause for Joe**.

## Reproduce

```
python tests/function-space-ext/gap_wellposedness_end.py
python tests/function-space-ext/aps_end_eta_class_symmetry.py
python tests/function-space-ext/family_index_bundle.py
python tests/function-space-ext/flux_index_2d.py
python tests/function-space-ext/verify/gap_wellposedness_indep_check.py
python tests/function-space-ext/verify/aps_end_eta_class_symmetry_indep_check.py
python tests/function-space-ext/verify/family_index_bundle_indep_check.py
python tests/function-space-ext/verify/flux_index_2d_indep_check.py
```

All exit 0. Primary asserts: 14 + 156 + 8 (+ flux). Independent re-checks: 24 + 50 + 4 (+ flux).
