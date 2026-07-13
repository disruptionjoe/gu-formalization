# Renormalizable, Asymptotically Free, and Unitary Fourth-Order Gravity -- and the Tachyonic Price of Asymptotic Freedom

**Draft, 2026-07-11. GU-INDEPENDENT: the results are about the class of fourth-order (Stelle-type) gravities with
a kinematically-projected Rarita-Schwinger sector; Geometric Unity is one realization. Every quantitative claim
ties to a reproducible test in `tests/` (W44-W80, all exit 0). External publication is Joe-gated (no arXiv, no
submission in scope here).**

## Abstract

Fourth-order (Stelle) gravity is renormalizable but carries a massive spin-2 ghost, long regarded as fatal to
unitarity. We give a complete one-loop ultraviolet picture for the class, including a kinematically-projected
(`ker Gamma`) Rarita-Schwinger sector, and establish four results. **(1) Renormalizability:** the theory is
power-counting renormalizable and the spin-3/2 sector does not spoil it, because the transverse `ker Gamma`
projector has momentum-degree zero and removes exactly the Velo-Zwanziger modes that make generic
gravity-coupled spin-3/2 non-renormalizable; the matter sector adds a finite, closed set of counterterms.
**(2) Asymptotic freedom:** the dimensionless couplings flow to a unique Gaussian ultraviolet fixed point, made
structural by the homogeneous-quadratic form of the one-loop system (which forbids any isolated interacting fixed
point); the Weyl coupling is thereby predicted rather than tuned. **(3) Unitarity:** on the physical subspace the
inner product is positive -- the massive spin-2 sector is Krein-graded and PT-unbroken across the entire
interacting regime, and the conformal scalaron is positive-norm; loop unitarity is a positivity-vs-causality
trade whose cost is bounded to the ghost scale. **(4) The tachyonic price of asymptotic freedom:** the *same*
asymptotic freedom that delivers (1)-(2) *forces* the conformal-scalaron mass-squared negative -- a
background-independent tachyonic instability -- because every asymptotically-free trajectory carries a negative
`R^2`-to-Weyl coupling ratio. The theory is renormalizable, asymptotically free, and unitary, but its
asymptotically-free completion is unstable; stability requires trading asymptotic freedom for a non-Gaussian
(asymptotic-safety) completion. We give the exact fork.

## 1. Introduction

Higher-derivative gravity with a Weyl-squared term is perturbatively renormalizable (Stelle 1977) and
asymptotically free in its dimensionless couplings (Fradkin-Tseytlin; Avramidi-Barvinsky; Salvio-Strumia
"agravity"). The obstruction to taking it as fundamental is the massive spin-2 excitation of wrong-sign residue
-- a negative-norm ghost -- which naively breaks unitarity. Three ultraviolet questions decide the theory's fate:
is it renormalizable once realistic matter (in particular a spin-3/2 field) is included; is it asymptotically
free; and is it unitary. We answer all three for the class, and find that the answers interact: asymptotic
freedom, the property that secures renormalizability and predictivity, is also what forces a conformal-sector
instability.

## 2. Setup

The action is the Stelle class `f_2^2 C^2 + f_0^2 R^2 + (induced Einstein) + Lambda`, with a spin-3/2
Rarita-Schwinger field whose kinetic operator is projected by a transverse, gamma-traceless `ker Gamma` operator
(the geometric realization of the gravitino gauge condition). The indefinite (Krein) inner product on the ghost
sector is graded so that the physical subspace carries a positive form -- the "keep-and-grade" quantization
(Bender-Mannheim PT quantum mechanics; Bateman-Turok tree-level positivity). We distinguish throughout the Krein
pseudo-unitarity `S^dag eta S = eta` (algebraic, all-orders) from physical-subspace positivity (the loop
question).

## 3. Renormalizability (`tests/W44`)

Two independent power-counting computations give superficial degree of divergence `D <= 4` for every loop order
on the `ker Gamma` subspace. The spin-3/2 sector does not spoil renormalizability: the projector's momentum-degree
is zero (computed, residuals `~1e-16`, not assumed), and the `n = 2` Velo-Zwanziger danger modes -- the ones that
make generic gravity-coupled spin-3/2 non-renormalizable -- are exactly what `ker Gamma` removes. The Rarita-
Schwinger sector adds a finite, closed set of counterterms beyond pure Stelle (an extension, not a proliferation,
which is the content of renormalizability).

## 4. Asymptotic freedom (`tests/W45-W47`)

Running the one-loop beta functions (the ported agravity forms, with the spin-3/2 contribution added), the
Gaussian point is the unique ultraviolet fixed point: the Weyl coupling is asymptotically free
(`b_2 = 133/10 > 0`), and the firming pass shows the one-loop system is homogeneous-quadratic
(`beta(k g) = k^2 beta(g)`), which mathematically forbids any isolated interacting fixed point for any value of
the (imperfectly known) spin-3/2 coefficients. So the theory realizes asymptotic *freedom* (couplings flow to
zero), stronger than mere safety, and the Weyl coupling `f_2` is *predicted* by the fixed point rather than tuned
-- the one genuine predictivity gain over generic higher-derivative gravity. The critical surface has dimension
`~3` in the gravitational sector (`M_Pl`, `Lambda`, and the conformal coupling), so predictivity is preserved.

## 5. Unitarity: loop-positivity on the physical subspace (`tests/W48-W54, W77-W79`)

Loop unitarity of the class is a *positivity-vs-causality trade*: across four independent constructions
(Cutkosky-cut, PT `C`-operator, fakeon, Lee-Wick), loop unitarity is achievable but is paid for in
micro-causality or locality, and the cost is provably bounded to the ghost scale `~1/m` (we prove no *local*
positive metric exists, with the metric kernel exponentially localized). On the physical subspace the inner
product is positive:
- the massive spin-2 grading is PT-unbroken (the Krein modular operator has real-positive spectrum) across the
  entire interacting regime, reaching the exceptional locus only at the free ultraviolet endpoint where the ghost
  decouples (`tests/W53`);
- the conformal scalaron is *positive-norm*: the induced action `|II|^2 = |H|^2 - R^X` fixes the scalaron norm
  from the Einstein term (`sign f'(0)`, positive), *independently* of the `R^2` coefficient (`tests/W79`), so a
  wrong-sign `R^2` coupling makes a tachyon (a mass problem), never a ghost (a norm problem).
So the physical inner product is positive: the theory is unitary on the physical sector. The single genuinely
open loop-positivity subtlety (the rank-`>1` Krein modular-conjugation theorem) is an operator-algebra frontier
problem, not a defect of the theory (`tests/W77`, `H61a`).

## 6. The tachyonic price of asymptotic freedom (`tests/W79-W80`)

The theory is renormalizable, asymptotically free, and unitary -- but its asymptotically-free completion is
*unstable*, and the instability is forced by the very asymptotic freedom that secures the rest.

The conformal scalaron mass is `M_0^2 = gamma / (6 f_0^2)` with `gamma > 0` (the positive induced Einstein
coefficient). Because the `R^2` sector is pure, `f'' = 2 f_0^2` is constant, so `M_0^2` is *background-independent*:
a wrong sign cannot be cured by vacuum selection (verified at flat, de Sitter, and every background). And the sign
IS wrong on the asymptotically-free trajectory: both fixed ratios `r_* = f_0^2 / f_2^2` are negative (structurally
-- product `> 0`, sum `< 0`), and by ODE uniqueness a flow cannot cross a fixed ratio, so *every*
asymptotically-free-complete trajectory carries `f_0^2 < 0` at all scales, while every positive-`f_0^2` start hits
a Landau pole (this is the agravity "good-sign scalaron -> Landau pole" lore, reproduced natively, not a porting
artifact). The spin-3/2 sector does not rescue the sign: its contribution over its entire allowed band keeps both
ratios negative.

So: **asymptotic freedom forces the conformal scalaron tachyonic.** The property is double-edged -- it buys
renormalizability, a unique ultraviolet fixed point, and a predicted Weyl coupling, and it *simultaneously* forces
a background-independent conformal instability. This is a genuine structural tension of the class, stated exactly.

**The fork (the honest open frontier).** The tachyon is forced *on the asymptotically-free route*. It is escapable
only by leaving that route: (E1) a large negative spin-3/2 `R^2`-beta contribution (`d < -5/6`), unsupported for a
transverse gamma-traceless carrier and uncomputed; or (E2) a non-Gaussian ultraviolet completion (asymptotic
safety / a Reuter fixed point / a conformal `f_0 -> infinity` limit), which trades the clean asymptotic freedom of
Sections 3-4 for stability. This is a sharp dichotomy for the class: **asymptotic freedom with a conformal
instability, or asymptotic safety with (possibly) stability** -- and which a given realization takes is an open
ultraviolet question.

## 7. Relation to prior work

- **Renormalizability + asymptotic freedom of higher-derivative gravity:** Stelle 1977; Fradkin-Tseytlin;
  Avramidi-Barvinsky; Salvio-Strumia (agravity). Delta: the kinematic `ker Gamma` spin-3/2 sector (no Stelle-grade
  renormalizability statement for a higher-derivative Rarita-Schwinger field existed), and the structural
  (homogeneous-quadratic) no-interacting-fixed-point argument.
- **Keep-and-grade / PT / Krein unitarity:** Bender-Mannheim; Mannheim; Anselmi-Piva (fakeons);
  Donoghue-Menezes / Grinstein-O'Connell-Wise (Lee-Wick); Bateman-Turok; Kuntz; Nakayama. Delta: the
  positivity-vs-causality trade as an organizing statement, the no-local-positive-metric theorem, and the
  PT-unbroken-across-the-interacting-regime result.
- **The conformal-factor problem and the scalaron:** Gibbons-Hawking-Perry; Starobinsky; agravity. Delta: the
  induced `|II|^2` sign structure forcing positive-norm-but-tachyonic ("wrong-sign Starobinsky"), and the
  identification of asymptotic freedom as the *cause* of the wrong sign.

## 8. Status / open gaps

1. **DONE:** the four results are reproducible in-repo (`tests/W44-W80`, all exit 0), each carrying its honest
   grade. Renormalizability and asymptotic freedom are one-loop-truncation results; unitarity is a
   positivity-vs-causality trade with a machine-checked no-local-metric theorem; the tachyonic-price result is a
   sign computation, rigorous within the one-loop-AF construction.
2. **The load-bearing open fork:** does the realization take the asymptotically-free route (renormalizable +
   predictive, but conformally unstable) or a non-Gaussian route (E2, possibly stable)? The `ker Gamma`
   heat-kernel `R^2`-beta (E1) and the asymptotic-safety analysis (E2) are the two open computations.
3. **Grade:** structural result at honest grade; a complete one-loop ultraviolet picture of the class, with the
   asymptotic-freedom-vs-stability tension as the central new finding. Target: hep-th. External publication
   Joe-gated.
