---
title: "WC-FUNCTION-SPACE-EXT: a CONDITIONAL section-setting index-conservation theorem. The paper's finite-dimensional Theorem 2 (linear Krein-isometric operators conserve the net chiral index at 0 on the cross-chirality carrier) and the antilinear null-eigenspace bound EXTEND to a genuine differential-operator / spectral-flow setting: every norm-continuous family of self-adjoint, chirality-odd (Dirac), Krein-self-adjoint (cross-chirality K) Fredholm operators has net chiral spectral flow EXACTLY 0. The residual -- explicitly NOT closed -- is the APS / noncompact-end eta correction, family-index / higher-topology terms, and gap well-posedness of the physical projection."
status: staged
doc_type: result
created: 2026-07-02
grade: "computed + INDEPENDENTLY RE-VERIFIED conditional theorem on an explicit 1D lattice Dirac section model. The structural core -- a Gamma-odd, Krein-self-adjoint (K = sigma_1) operator is sigma_1 (x) B, so its spectrum is symmetric about 0 and the negative (physical) sector is chirality-balanced -- is a short finite-dimensional (per-t) linear-algebra proof with machine-certified premises. Numerics: tests/function-space-ext/dirac_spectral_flow_section.py (20 asserts; central-difference momentum; n_-(t) = 0 through 20 genuine crossings; spectrum symmetric to 0.0) + verify/dirac_spectral_flow_indep_check.py (129 asserts; SPECTRAL/Fourier momentum, different seed, non-degenerate B giving per-eigenvector chirality-neutrality EXACTLY at 8e-14, analytic spec(D) = +-spec(B), control). NOT a full function-space theorem: it is the interior/closed, spectral-gapped statement; the analytic residual below is open."
addresses: "WC-FUNCTION-SPACE-EXT (NEXT-STEPS.md, post-publication card); the residual named by reviewer criticisms #2 and #3 and by the paper's Theorem 2 finite-dimensional scope."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/antilinear-bound-RESULTS.md
  - canon/antilinear-nonkrein-admissibility-RESULTS.md
  - explorations/analytic-index-fredholm/function-space-index-conservation-first-probe-2026-07-02.md
scripts:
  - tests/function-space-ext/dirac_spectral_flow_section.py
  - tests/function-space-ext/verify/dirac_spectral_flow_indep_check.py
---

# The function-space extension: a conditional section-setting index-conservation theorem

**Card.** WC-FUNCTION-SPACE-EXT (post-publication). It asks whether the paper's finite-dimensional
Theorem 2 (and, now, the antilinear null-eigenspace bound) survive for actual Rarita-Schwinger
**sections** -- Krein-isometric operators on L^2-sections, Fredholm indices, spectral flow -- or
whether a precise obstruction should be documented. **Outcome: a conditional theorem, with the
residual sharply localized.**

## Framework

The section Krein space `H = L^2(S^1; C^2) (x) C^N` (a faithful, computable 1D stand-in for the
RS-section setting), with chirality `Gamma = sigma_3 (x) I`, cross-chirality Krein form
`K = sigma_1 (x) I` (`K Gamma = -Gamma K`), and the genuine differential operator `P = -i d/dx`
(central-difference / spectral momentum). This is the section analog of the paper's finite
`(+96,-96)` cross-chirality carrier.

## Theorem (conditional)

*Let `D(t)` be a norm-continuous family of operators on `H` that are (i) self-adjoint, (ii)
**chirality-odd** (`D Gamma = -Gamma D` -- a Dirac / chirality operator), (iii) **Krein-self-adjoint**
for the cross-chirality `K` (`D^dag K = K D`), and (iv) **Fredholm** (a spectral gap at `0` off
isolated crossings). Then the net chiral spectral flow `SF_chi({D(t)}) = 0`.*

**Proof (structural; finite-dimensional at each `t`; premises machine-certified).** Conditions
(ii)+(iii) with `K = sigma_1` force the off-diagonal form `D = [[0,B],[C,0]]` with `C = B^dag`
(self-adjointness) and `B = C^dag` (Krein-self-adjointness), i.e. `B` Hermitian and
`D = sigma_1 (x) B`. Hence (1) the spectrum is symmetric about `0` (eigenvalues `+-b` for each
eigenvalue `b` of `B`), and (2) every eigenvector is `(1,+-1) (x) v_b`, of chirality
`(|1|^2 - |+-1|^2)/2 = 0`. So the negative (Dirac-sea / physical) spectral subspace has net chirality
`n_-(t) = tr(Gamma P_{<0}(t)) = 0` for all `t`, and no zero crossing carries net chirality: the net
chiral spectral flow is `0`. This is the section analog of the finite theorem -- the physical sector
is chirality-balanced precisely because `K` is cross-chirality. QED (interior, gapped).

## Certificates

- `tests/function-space-ext/dirac_spectral_flow_section.py` (20 asserts): the family
  `D(t) = sigma_1 (x) B(t)` is self-adjoint, chirality-odd, Krein-self-adjoint along the path;
  `n_-(t) = 0` (range `~1e-12`) through **20 genuine zero crossings** (non-vacuous); spectrum
  symmetric about `0` to `0.0`; the negative half chirality-balanced. Control: a Fredholm family
  with **nonzero** integer net chiral spectral flow is exhibited -- and it necessarily violates
  Krein-self-adjointness (residual `~0.9`) and is `Gamma`-even (not a chirality operator).
- `verify/dirac_spectral_flow_indep_check.py` (129 asserts): independent substrate -- **spectral
  (Fourier) momentum**, a different seed, and a **non-degenerate** `B` (distinct-magnitude spectrum)
  so that the mechanism is confirmed at the **per-eigenvector** level (`max |<Gamma>| = 8e-14`,
  every mode neutral), with the analytic identity `spec(sigma_1 (x) B) = +- spec(B)` at `2.5e-14`;
  net chiral spectral flow `0`; the control again needs breaking Krein.

## What this changes for the paper (pauses for Joe)

Theorem 2's finite-dimensional scope caveat (and caveat (d)'s function-space residual) can upgrade
from "function-space extension open" to: **the index conservation extends to the section /
spectral-flow setting under the stated Fredholm + Krein-self-adjoint hypotheses (a conditional
theorem, computed + independently re-verified in a 1D Dirac model); the residual is now precisely
the APS / noncompact-end and family-index analytic terms.** This is a one- to two-sentence scope
upgrade of Theorem 2 / caveat (d) / the status table -- **not applied here** (paper edits pause for
Joe; this note is staged, not CANON.md-promoted).

## The residual (honest; NOT closed)

The theorem is the **interior / closed, spectral-gapped** statement. The genuine analytic frontier
remains open, and is now precisely three items:

1. **Gap well-posedness.** The physical (negative) spectral projection needs the Fredholm spectral
   gap to be well-defined in infinite dimensions; without a gap (continuous spectrum through `0` on
   noncompact ends) the count is not well-posed. Genuine analytic input.
2. **APS / noncompact-end eta correction.** On a manifold **with boundary** or noncompact ends, an
   Atiyah-Patodi-Singer eta / end term can supply an **unpaired** chiral contribution even when the
   interior flow is `K`-paired. This is exactly where a nonzero physical chiral count would have to
   come from -- consistent with the paper's "external on present evidence" conclusion (the boundary
   datum is external to the interior sector). Not computed here.
3. **Family-index / higher-topology terms** over the parameter space (index bundle), not seen by the
   1D interior model.

## Honest caveats

- The 1D lattice Dirac model is a faithful but simplified stand-in for the RS-section setting; the
  structural core (`sigma_1 (x) B` form => symmetric spectrum => chirality-balanced physical sector)
  is dimension- and model-robust (it is the same cross-chirality mechanism as the finite theorem),
  but a genuine RS-bundle / APS statement is the residual above.
- Internal tier (caveat (e)): computed + internally re-verified, not externally replicated.
- No number was fitted; the only integers are the carrier's own chiralities and `0`, and the
  control's honest nonzero flow.
