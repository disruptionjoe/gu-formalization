---
title: "Eric/Curt Wave 3C: actual Y14 atlas and Cauchy-domain gate"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
campaign_wave: ECW3-G4-OBSERVATION
registry: lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json
probe: tests/channel-swings/eric_curt_wave3c_y14_atlas_cauchy_domain_probe.py
grade: "EXACT ACTUAL METRIC-BUNDLE VERTICAL TENSOR ATLAS, SPLIT-FRAME GIMMEL CONTROL, AND DECISIVE ORDINARY FULL-AMBIENT CAUCHY KILL; NOT A CONNECTION-FREE NONLINEAR ATLAS OR ANALYTIC DOMAIN THEOREM. GL(4)-induced Sym2 transitions descend the vertical and trace-reversed DeWitt data; the total gimmel and admitted-section-jet packet is exact in affine or connection-adapted frames. Signature (9,5) admits neither a positive thirteen-plane nor a hyperbolic direction for its characteristic quadratic. Section-pullback and genuinely ultrahyperbolic/Krein boundary-value domains remain open."
canon_verdict_change: none
third_lane_promotion: none
---

# Wave 3C actual `Y^14` atlas and Cauchy-domain gate

## Result first

Wave 3C replaces ECW3B's arbitrary rational ambient frames by the transition
forced by the actual Lorentz-metric bundle

\[
Y^{14}=\operatorname{Met}_{3,1}(X),
\qquad
\pi:Y\to X.
\]

If base coordinates change by a Jacobian `A`, a metric and vertical metric
variation transform by the same congruence law:

\[
h' = A^{-T}hA^{-1},
\qquad
k' = A^{-T}kA^{-1}.
\]

The second formula is the induced ten-dimensional `Sym^2(T*X)`
representation. It is not a freely chosen `GL(14)` frame. For every invertible
`A`, cyclicity of trace gives exact invariance of

\[
V_h(k,\ell)
=\operatorname{tr}(h^{-1}kh^{-1}\ell)
-\frac12\operatorname{tr}(h^{-1}k)\operatorname{tr}(h^{-1}\ell).
\]

Thus the base Lorentz metric and trace-reversed DeWitt vertical form descend
tensorially. In affine or connection-adapted frames their block gimmel metric
descends as well. The exact control verifies this on a three-chart affine
cocycle and obtains the native inertias

\[
(3,1)+(6,4)=(9,5).
\]

An admitted section jet also descends. Writing its local derivative as a
`10 x 4` matrix `J`,

\[
J'=\operatorname{Sym}^2(A)JA^{-1},
\]

and the graph tangent map intertwines exactly. This is compatibility of a
section if supplied; it is not a theorem that a global Lorentz section exists.
For a general nonlinear coordinate change the total tangent transition also
contains horizontal--vertical shear from derivatives of the Jacobian. Removing
that shear is not canonical: it uses the declared connection/horizontal split.
ECW3C therefore earns the actual vertical tensor atlas and split-frame gimmel
control, not a connection-free nonlinear block atlas.

## The decisive full-ambient kill

W131 already constructs the actual covariant principal symbol on `Y^14` and
identifies its characteristic variety with the gimmel null quadric at
frame/symbol grade. ECW3C decides whether that quadric can be read as an
ordinary Lorentzian evolution cone.

It cannot.

First, any thirteen-dimensional hyperplane `H` in a `(9,5)` tangent space
intersects a five-dimensional negative subspace `N` in dimension at least

\[
\dim(H\cap N)\ge 13+5-14=4.
\]

So no codimension-one hypersurface in full `Y^14` is positive/spacelike.

Second, let `q` be the `(9,5)` characteristic quadratic and let `e` be any
nonnull candidate hyperbolicity direction. If `q(e)>0`, the orthogonal
complement `e^\perp` has positive index eight, so it contains a positive
`zeta`. If `q(e)<0`, the complement retains negative index four and contains
a negative `zeta`. In either case `zeta` has the same sign as `e` and is
orthogonal to it. The roots of

\[
q(\zeta+t e)=q(\zeta)+t^2q(e)
\]

are nonreal; equivalently its discriminant is
`-4 q(e) q(zeta) < 0`. Null `e` cannot be a hyperbolicity direction. Hence the
full `(9,5)` quadratic is not Gårding-hyperbolic in any direction.

This kills an ordinary full-ambient Lorentzian Cauchy/Hamiltonian domain for
the W131 symbol. It does not prove that every higher-index boundary-value,
Krein, weighted Fredholm, or scattering construction is impossible.

## Primary-source collision (retroactive process repair)

Disposition: `SOURCE-CORRECTS`. At local transcript `01:16:13`--`01:17:35`
and `01:25:01`--`01:25:42`, Weinstein explicitly distinguishes one-time
Hamiltonian/initial-value dynamics from multiple-time ultrahyperbolic
equations, says ordinary codimension-one initial conditions upstairs give way
to boundary conditions, and calls the unresolved dynamics technical debt.
That source corrects the scope if ECW3C is read too broadly: the result kills
the ordinary Lorentzian full-ambient Cauchy route, not every ultrahyperbolic
boundary formulation. The interview does not prove the ECW3C theorem and
supplies no analytic domain; the mathematical result remains repo-constructed.

## Layer-0 boundary

| shared term | objects kept separate | disposition |
| --- | --- | --- |
| `Met(X)` | rank-ten bundle of pointwise metrics; infinite-dimensional space of global sections | `HOMONYM` |
| atlas descent | tensorial chart compatibility; global Lorentz-section and spin-lift existence | `HOMONYM` |
| null cone | higher-index `(9,5)` quadric; one-time Lorentzian causal cone | `HOMONYM` |
| closed domain | pointwise Krein-symmetric symbol; closed/self-adjoint right-`H` domain with global boundary data | `HOMONYM` |

No signature component or codimension is interpreted as a physical mode
count.

## Exact control

The rational probe checks three base Jacobians, their induced `Sym^2`
representations, and the total fourteen-dimensional cocycle. It verifies base,
fibre, and gimmel descent separately, exact inertias on all patches, nonzero
admitted-section-jet and pullback-metric descent, the hypersurface index floor,
and explicit negative hyperbolicity discriminants in both sign sectors.

Result: `59 exact + 13 planted = 72 PASS`.

The planted controls reject arbitrary `GL(14)` frames as metric-bundle charts,
atlas-descent-to-section-existence, `(9,5)`-as-Lorentzian, pointwise Krein
symmetry as analytic closedness, section data as generic ambient data, an
automatic `X` spin structure, common-complex causal selection, premature BFV
reduction, and Curt promotion.

## What is earned and what remains

Earned:

- the actual `GL(4)`/`Sym^2` vertical tensor-atlas contract;
- exact trace-reversed DeWitt and affine/connection-adapted gimmel descent;
- conditional admitted-section-jet descent;
- a decisive kill of ordinary codimension-one Lorentzian evolution on full
  `(9,5)` `Y^14`.

Not earned:

- existence of a global Lorentz metric section on arbitrary `X`;
- `X` spin, the `Y` spin lift, or global right-`H` spinor descent;
- the horizontal split for general nonlinear chart transitions;
- an analytic closed/self-adjoint domain, Green form, propagator, or physical
  BFV phase space.

The local section graph in the exact control remains Lorentzian `(3,1)`. A
three-dimensional Cauchy surface there has codimension eleven in `Y^14`, not
one. Therefore section-pullback is a distinct analytical problem rather than a
disguised ambient Cauchy problem.

## Curt rival and next gate

Curt remains a formally separate rival/checklist track inside the Eric lane.
The literal real `(7,7)` candidate has not supplied its own actual
metric-atlas, pairing, spin/reality, action, domain, or preboundary port. The
common complex algebra selects none of those real causal/analytic data.

The pre-registered rule remains `TG-1 AND TG-2 AND TG-3`. `TG-1` is partial;
`TG-2` and `TG-3` remain open. No third lane is promoted.

The next gate is
`ECW3D-SECTION-PULLBACK-RIGHT-H-GREEN-DOMAIN`: on an explicitly admitted
Lorentz/spin section, construct or kill a common right-`H` closed domain and
Green boundary form for the pulled-back nonlinear Euler/RS packet. A genuinely
ultrahyperbolic ambient boundary-value formulation remains a separate rival,
not an assumed fallback. No physical equation, stationary state, Standard
Model sector, count, cosmology, or theory verdict is claimed.

For completed-wave reproducibility, the campaign retains the legacy
`next_swing=ECW3C` value certified by ECW3B. The live campaign pointer is now
`current_next_swing=ECW3D-SECTION-PULLBACK-RIGHT-H-GREEN-DOMAIN`; ECW3C also
stores that handoff inside its own immutable nested result.
