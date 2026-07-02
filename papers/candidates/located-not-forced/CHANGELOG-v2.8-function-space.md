# Changelog v2.8 -- function-space extension: conditional section-setting theorem (2026-07-02)

Trigger: the "bigger swing" (Joe-authorized) at WC-FUNCTION-SPACE-EXT -- the residual that both reviewer #2 and
#3 point to, and Theorem 2's finite-dimensional scope. Worked from an exploration-grade first probe to a
**computed + independently re-verified conditional theorem** (`canon/function-space-index-conservation-RESULTS.md`).
Both copies edited in sync. **No core claim, number, or grade changed; Theorem 2 and the antilinear bound are
untouched -- only their function-space SCOPE upgrades from "open" to "conditional theorem with a precisely
localized residual."**

## The result folded in

On a genuine 1D lattice Dirac section model (cross-chirality Krein space, `Gamma = sigma_3`, `K = sigma_1`,
`P = -i d/dx`): every norm-continuous family of self-adjoint, chirality-odd (Dirac), Krein-self-adjoint Fredholm
operators takes the form `sigma_1 (x) B`, so its spectrum is symmetric about 0 and the negative (physical)
sector is chirality-balanced -- **net chiral spectral flow exactly 0** (through genuine zero crossings;
non-vacuous). A control shows nonzero net chiral spectral flow requires leaving the class (breaking
Krein-self-adjointness; a `Gamma`-even, non-chirality operator). This EXTENDS Theorem 2 and the antilinear
null-eigenspace bound to the section / spectral-flow setting under stated hypotheses.

**Certificates.** `tests/function-space-ext/dirac_spectral_flow_section.py` (20 asserts; central-difference
momentum) + `tests/function-space-ext/verify/dirac_spectral_flow_indep_check.py` (129 asserts; spectral/Fourier
momentum, different seed, non-degenerate `B` confirming per-eigenvector chirality-neutrality EXACTLY, analytic
`spec(sigma_1 (x) B) = +- spec(B)`, control). Grade: computed + independently re-verified conditional theorem.

**Residual (explicitly OPEN, now precisely localized):** the APS / noncompact-end eta correction, family-index /
higher-topology terms, and gap well-posedness of the physical projection -- the genuine analytic frontier.

## EDITS APPLIED (v2.8, both copies)

1. **Theorem 2 scope remark** ("no Fredholm theory is needed" / Scope): "extension to a function-space setting
   ... a separate, named open problem" -> "now holds as a conditional theorem (net chiral spectral flow 0 for
   Krein-self-adjoint chirality-odd Fredholm families; computed + independently re-verified); residual = the APS/
   end and family-index analytic terms."
2. **Caveat (d)**: "the function-space setting remains open" -> "the function-space extension now holds as a
   conditional section-setting theorem (residual: APS/end + family-index)."
3. **Abstract antilinear-leg summary (.tex)** + intro/abstract body: function-space "remains open" -> conditional
   theorem; also corrected a v2.7 miss in the .tex abstract summary (antilinear class stated as
   "Krein-compatible ... admissibility itself fails" -> the null-eigenspace class, matching v2.7).
4. **Section 6 residual**: the function-space residual now names the conditional theorem + the APS/end +
   family-index residual.
5. **Status-table row** (Theorem 2 / antilinear leg): "function-space extension open" -> "conditional
   section-setting theorem, residual APS/end + family-index."
6. **Conclusion**: function-space "remains open" -> conditional theorem; also corrected a v2.7 miss in the .md
   conclusion ("delimited Krein-compatible operator class" -> "null-eigenspace class").
7. **Version bookkeeping**: .tex header -> v2.8; .md version marker + version-history paragraph.

## NOT CHANGED

- Theorem 2, the antilinear index-nullity theorem, Theorem 1, the CRT structure, and every integer are untouched.
  This pass only upgrades the function-space SCOPE (from open to conditional-theorem-with-localized-residual).
- The enumeration-completeness "unrestricted / function-space theory" residual (a different open problem) is left
  as-is.
- Internal tier unchanged (caveat (e)). `canon/function-space-index-conservation-RESULTS.md` is staged, **not
  CANON.md-promoted**. The APS/end + family-index residual is genuinely open, not closed.

## STATUS

Publication remains **DEFERRED** (Joe). The paper's biggest finite-dimensional caveat now reads as a conditional
theorem with a precisely-localized analytic residual rather than an open extension. Publication flips only on
Joe's review and the CANON.md-promotion decision. This does not gate publication (WC-FUNCTION-SPACE-EXT was the
post-publication card); it is a strengthening.
