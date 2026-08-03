---
title: PW2F-R2B2B2E — conditional principal quadratic-distortion U4 ceiling
date: 2026-08-03
status: CONDITIONAL_ACTIVE_CANONICAL_COFRAME_PRINCIPAL_Z1_QUADRATIC_DISTORTION_U4_CEILING_ZERO
lane: Eric-guided Lane 1; source, active reconstruction, and Curt comparator kept separate
run: RUN-20260803-120315-gu-formalization-pw2fr2b2b2e-actual-u4-jet-realizability
registry: lab/process/pw2fr2b2b2e-actual-u4-jet-realizability-registry.json
probe: tests/channel-swings/pw2fr2b2b2e_actual_u4_jet_realizability_probe.py
---

# Outcome

The missing quartic return in the conditional active quadratic-distortion
slot is now constructed at the level that matters for `C4`: it is zero.

This does not come from declaring `U4=0`. It comes from an exact nonlinear
two-wave Zorro metric, the correct symmetric-coframe Levi--Civita spin
connection, and a dependency-complete max-degree proof. For every one of the
ten metric owners and every independent pair of observed-base conormals in
the declared graph,

\[
\deg D T\le 2,\qquad
\deg D^2T\le 3,\qquad
\deg D R\le 1,\qquad
\deg D^2R\le 2.
\]

Therefore the normal return `DT-DT` can reach degree four, while every
background-distortion and moving-pairing return stops at degree three or
below. On this branch,

\[
U_4=0,
\qquad
M^{\rm slot}_4=M^{\rm normal}_4.
\]

The predecessor's complete 35-monomial normal bank consequently survives as
the complete `C4` coefficient of this reconstructed slot. Its live direct
entry remains `-8/25`. This is not yet the complete `I1` bank because the
distinct transgression/moving-Shiab bank `A4` and active `kappa1`
normalization remain open.

# Layer 0 and source disposition

The objects remain typed as follows:

- `epsilon_src`: the source gauge transformation in `omega`;
- `epsilon_act`: the conditional active `Spin(9,5)` rotor occupying that slot
  in this reconstruction;
- `h=exp(u)`: the repository graph/gauge object; and
- `epsilon_red`: the reduction/soldering field.

No pair is identified.

- `SOURCE-CONFIRMS`: the 2021 manuscript types
  `I1^B : G x MET -> R`, places `(kappa1/2)T_omega` in that action, and
  measures `T_omega` against a distinguished Levi--Civita/spin reference. Its
  displayed `varpi+s alpha` derivative fixes the metric and source epsilon
  only for that derivative.
- `REPOSITORY-DERIVES`: the active `(9,5)` rotor and Zorro graph, symmetric
  coframe, background policy, all metric/connection/distortion jets, the
  universal degree ledger, `U4=0`, and the lower-order liveness fixture.
- `SOURCE-SILENT`: a selected background or `varpi` policy, a joint
  metric/omega variation domain, the active derivative/pairing port, the `U4`
  verdict, and the value or normalization of `kappa1`.

The 2021 action manuscript uses the `Y^(7,7)/Spin(7,7)` presentation. Modern
Weinstein states the trace-reversed-fibre premise, while the repository derives
the active `(6,4)+(3,1)=(9,5)` carrier. That does not port the old action's
Hodge star, pairing, Shiab map, density, or normalization.

This `U4` is the quadratic-distortion pullback return inside conditional
active `I1`. The manuscript `I2B` object is a distinct residual-square action
and receives no coefficient or cancellation from this result.

# Nonlinear construction

For two physical metric waves

\[
g(r,s,x)=g_0+r h_i e^{\xi\cdot x}+s h_j e^{\zeta\cdot x},
\]

the executable builds the exact mixed jet of

\[
G_Y=
\begin{pmatrix}
g+C^T D_gC&-C^TD_g\\
-D_gC&D_g
\end{pmatrix},
\qquad C_\mu=\partial_\mu g,
\]

with the trace-reversed DeWitt fibre metric `D_g`. In the point-orthonormal
coordinates it constructs the symmetric coframe

\[
E=(I+\eta(G_Y-\eta))^{1/2},\qquad G_Y=E^T\eta E,
\]

and uses the correct transformed connection

\[
\omega=E\Gamma E^{-1}-(dE)E^{-1}.
\]

The frame identity and unprojected condition
`omega^T eta + eta omega = 0` pass through mixed order. All ten symbolic
owners reproduce the accepted `Z1` metric tangent, and all ten full owner
graphs reproduce the accepted principal LC-spin tangent on a dense panel.
Three off-diagonal owner pairs with independent conormals pass as held-outs.

At fixed `epsilon_act`, the connection-derived part obeys

\[
DT=(1-\operatorname{Ad}_{\epsilon_{\rm act}^{-1}})D\Gamma,
\qquad
D^2T=(1-\operatorname{Ad}_{\epsilon_{\rm act}^{-1}})D^2\Gamma.
\]

A repository-selected nonzero off-shell witness is realized by declaring
`varpi0=T0+q(g0)`. It is a liveness background, not a source-selected datum.
Fixed moving-frame and fixed-coordinate representatives are distinct
policies; the latter adds only algebraic frame jets of degrees one and two, so
it cannot alter the `U4` ceiling. Independently varied `varpi` is a different,
unselected branch.

# Exact Hessian and degree result

For owner directions `i,j`, the quadratic-slot Hessian is

\[
\frac{1}{\kappa_1}D^2S_{ij}=
\langle T_i,R_0T_j\rangle+
\langle T_0,R_0T_{ij}\rangle+
\langle T_i,R_jT_0\rangle+
\langle T_j,R_iT_0\rangle+
\frac12\langle T_0,R_{ij}T_0\rangle.
\]

The executable propagates homogeneous degrees through every inverse, product,
horizontal derivative, coframe, connection, external-frame conversion,
distortion, and density node. It obtains route maxima

\[
(4,3,3,3,2).
\]

This max-plus certificate is universal within the declared nonlinear Zorro
dependency graph and fixed-background policies; it is not an extrapolation
from the numeric panel. An artificial degree-four `T_rs` plant is detected.

Separately, the probe constructs

\[
T(r,s)=T_0+rT_r+sT_s+rsT_{rs},
\]

forms `S=1/2 rho(r,s)<T(r,s),T(r,s)>`, and differentiates it directly with
Sympy. That independent result equals the five-family chain rule
coefficientwise. In the primary liveness fixture the non-normal coefficients
by common conormal degree are

\[
(-3,\ 92/25,\ 0,\ -14/25,\ 0).
\]

Only the final zero is promoted. The lower coefficients depend on the chosen
canonical-coframe/background fixture. The live cubic `-14/25` is carried to
the future `C3` ledger.

# Correction to R2B2B2D

R2B2B2D's `U4=0` and `U4=-M4_normal` objects are valid relaxed algebraic
constraint-ledger completion witnesses. They are not realized geometric jets,
so they did not prove geometric non-identifiability. R2B2B2E supplies the
missing nonlinear construction and selects the first outcome for this
conditional active principal slot by an order theorem, not by a fit.

# Boundaries and next gate

The result does not cover global/source epsilon, independently varied
`varpi`, another real form, vertical or mixed conormals, partial `Z1`, section
tangents, or the unported 2021 action. In the canonical orthonormal coframe the
active Hodge, Krein form, and lowerers are frozen; coordinate density `rho`
carries the remaining realized pairing motion.

No new `C4` adjoint is needed because `U4=0`, but the inherited normal bank
still has only a frozen native-ray Green check. A full four-dimensional
multi-index/Krein Green identity remains open. The live `C3` return also
requires its proper odd-order formal-adjoint and moving-coefficient terms.

Resume at
`PW2F-R2B2B2F-I1-TRANSGRESSION-A4-AND-KAPPA1-PROPORTIONALITY`:

1. construct the distinct `A4` transgression/moving-Shiab bank;
2. reconcile the full `I1` `C4` family by a four-dimensional Green identity;
3. run the coefficientwise `NONE/ANY/UNIQUE(kappa1)` classifier; and
4. only then assemble the separate admitted `I2B` `C4` bank.

P1/P2/P3 remain unchanged and unused. Curt remains
`FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. `TG-1 AND TG-2 AND TG-3` remains
`NOT_PROMOTED`. No characteristic, domain, quotient, observation, Standard
Model, GR, cosmology, or physics equation is claimed.

# Evidence

- Main final replay: `12 exact + 2 source + 19 type + 3 planted = 36` PASS.
- Universal degree maxima: `G=(1,2)`, `dG=(2,3)`, `T=(2,3)`, normal `C4`,
  non-normal ceiling `C3`.
- Primary fixture: normal `C4=-8/25`, conditional `U4=0`, live background
  `C3=-14/25`.
- Held-outs: three off-diagonal owner pairs with independent conormals,
  `U4=0`, metricity `15/15`.
- Hostile reviews: exact geometry, variational/PDE, and source/Layer 0 all
  `PASS_AFTER_REPAIR` at the conditional active canonical-coframe grade.
