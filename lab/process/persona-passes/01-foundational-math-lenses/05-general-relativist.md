---
title: "Persona Pass 05: General Relativist"
status: process
doc_type: persona_pass
updated_at: "2026-05-31"
---

# Persona Pass 05: General Relativist

## (a) Question with clearest leverage

Question 4 (does the construction reproduce GR in the right limit?) is the one my discipline owns. GR is not a generic geometry. It is a very specific dynamical theory of a Lorentzian metric on a 4-manifold whose linearized spectrum has exactly two massless spin-2 polarizations and whose nonlinear sector satisfies the Bianchi identity. Any "unified" construction is GR-compatible only if it produces this exact data in a controlled limit. I will use this as the discriminator.

## (b) Strongest first-principles construction

Starting from a 4-manifold X (no metric assumed), the natural tensor bundle whose total space is 14-dimensional is the bundle of symmetric, signature-(1,3), unit-determinant metrics. Fiber dimension of symmetric 2-tensors on R^4 is 10; restricting determinant and signature still leaves a 10-dim fiber, giving total dimension 14. So an "observerse" = bundle of Lorentzian metrics Y -> X with dim Y = 4 + 10 = 14 is the most natural reading. [speculation] An alternative reading is the frame bundle FX, but that has fiber GL(4) of dimension 16, total 20, not 14. So the metric-bundle reading fits the dimension count and the frame-bundle reading does not.

On Y, the canonical objects are: the tautological symmetric 2-tensor h (each point of Y is a metric on T_{pi(y)}X, and h is its pullback), the vertical bundle V (dim 10), and a connection that splits TY = H + V. With H + V split, one can attempt a Cartan-geometric formulation modeled on (Spin(1,3) ⋉ R^{10}) / Spin(1,3), i.e. an "internal" affine space of metrics with Lorentz structure on the horizontal.

## (c) What fails or is forced

Signature is forced Lorentzian on the horizontal (otherwise no GR). The vertical fiber, however, has its own induced metric from the Wheeler-DeWitt supermetric G^{ijkl} = (1/2)(g^{ik}g^{jl} + g^{il}g^{jk}) - g^{ij}g^{kl}. This supermetric is itself indefinite signature (1,9) on each fiber. So Y inherits signature (2,12) or similar [speculation], not Riemannian and not Lorentzian. This is the first hard obstruction: the natural metric on the observerse is not a spacetime metric in any standard sense.

Dimensional reduction is forced: to recover 4D Einstein equations one needs a section sigma: X -> Y picking a metric, and the pulled-back equations of motion must reduce to G_{munu} = 8 pi T_{munu}. Whether the Y-action reduces this way depends entirely on the action chosen.

## (d) Named obstructions

1. **Supermetric signature obstruction**: Wheeler-DeWitt fiber metric is indefinite; total-space "metric" is not Lorentzian.
2. **Section-existence obstruction**: a global section sigma: X -> Y exists iff X is parallelizable in metric sense (it is, since metric bundles are affine bundles modeled on symmetric 2-tensors, hence always have sections). OK, this one passes.
3. **Palatini coupling obstruction**: independent connection on Y must, in the GR limit, reduce to Levi-Civita of sigma^* h. Generically Palatini-style variations produce nontrivial torsion sourced by fermions (Einstein-Cartan). For pure-geometric GU there is no a priori reason torsion vanishes in the limit; this needs a constraint.
4. **Bianchi identity obstruction**: 14-dim field equations must imply 4D Bianchi (nabla^mu G_{munu} = 0) after pullback. No generic guarantee.
5. **No-go via Lovelock**: in 4D the unique 2nd-order metric theory with diffeo invariance is Einstein-Hilbert + cosmological constant. Anything pulled back from 14D that is 2nd-order and diffeo-invariant on X must equal this, up to coefficients.

## (e) One-sentence verdict

GR-limit feasibility is conditionally plausible: a metric-bundle observerse admits a natural Cartan-geometric structure whose horizontal sector can reduce to Einstein-Hilbert under a Palatini-with-torsion-constraint variation, but the indefinite Wheeler-DeWitt fiber signature and the need to suppress torsion at the section are real obstructions that the construction must explicitly resolve. [speculation]
