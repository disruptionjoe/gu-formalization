---
artifact_type: construction_result_and_scope_correction
created: 2026-08-06
status: ACTION_SPIN_LC_RANK9__STATIONARY_SELECTED_METRIC_HESSIAN_EXACT__DIFFEO_WARD_RESIDUAL_OPEN
source_return: SOURCE-CONFIRMS_AND_SOURCE-SILENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_stationary_spin_lc_hessian_probe.py
registry: lab/process/selected-action-stationary-spin-lc-hessian.json
---

# Stationary selected-action spin-Levi-Civita Hessian

## Result first

The first actual selected-action metric coefficient is now exact, and it
corrects an earlier scope error.

The previous rank-ten statement concerned the **coordinate Christoffel
symbol**. The selected action carries the induced **symmetric-frame spin
connection**. Its principal metric map has rank nine, not ten, on timelike,
spacelike and null covectors. Its unique kernel is the longitudinal metric
direction `h=k tensor k`.

Pulling the exact selected-action Hessian at the fully stationary algebraic
branch `T*=-(kappa_1/312) Phi1` through this spin-connection map gives a
nonzero symmetric metric coefficient. For positive `kappa_1` its exact
rank/inertia is

```text
timelike:  rank 9, inertia (3,6,1)
spacelike: rank 9, inertia (6,3,1)
null:      rank 6, inertia (3,3,4)
```

The isolated block is not diffeomorphism-radical: three of the four
diffeomorphism-symbol directions couple on every orbit. Therefore this is a
real action coefficient but not yet a physical gravitational Hessian. Direct
curvature/full-`II`/defect and observation terms must cancel or retain the
exact rank-three Ward residual before BV/BFV or Einstein interpretation.

No field, coefficient, quotient or datum is added.

## Layer 0 correction

| phrase | exact object | not identified with |
| --- | --- | --- |
| coordinate Levi-Civita symbol | `D_g Gamma^rho_{mu nu}` in the affine tangent connection | the action's spin-valued connection coefficient |
| action spin-Levi-Civita map | `D_g omega_{mu ab}` in symmetric frame | a rank-ten affine receiver |
| connection gauge | `d chi` in the Lorentz/adjoint connection | spacetime diffeomorphism `h=L_xi g` |
| stationary Hessian | `D2 I_selected(T*)` pulled through `D_g omega` | the off-shell nonlinear Euler equation |
| observed coefficient | invertible first-germ congruence of the local Hessian | a reduced BV/BFV physical form |

The v0.28 rank-ten calculation remains correct for its affine Christoffel
object. What is retracted is the inference that it supplies all ten directions
of the spin-valued action map. This is an append-only scope correction, not a
rewrite of the earlier artifact.

## Source collision

Weinstein's sources explicitly require a gauge-rotated Levi-Civita connection
in the contorsion comparison slot and type augmented torsion as a difference
of connections. They do not state whether the local rank calculation should
be performed on Christoffel coefficients or their induced spin image, nor do
they publish the Hessian or Ward ranks below.

```text
SOURCE-CONFIRMS: gauge-rotated Levi-Civita and two-connection route
SOURCE-SILENT:   coordinate/spin rank, stationary Hessian coefficients,
                 diffeomorphism radical and direct completion
```

The coefficients and correction are repository-derived.

## The rank-nine action map

For a symmetric metric perturbation `h` and covector `k`, the action carrier
uses

\[
 L^{\rm spin}_k(h)_{\mu ab}
 =\frac12(k_bh_{\mu a}-k_ah_{\mu b}). \tag{1}
\]

The exact matrix from `Sym2(R^4*)` into
`R^4* tensor Lambda2(R^4*)` has

\[
 \operatorname{rank}L^{\rm spin}_k=9,
 \qquad
 \ker L^{\rm spin}_k=\operatorname{span}\{k\otimes k\} \tag{2}
\]

for the timelike, spacelike and null orbit representatives. Equation (2) is
also immediate from (1): inserting `h_{mu nu}=k_mu k_nu` makes the two terms
equal.

By contrast, the coordinate Christoffel derivative retains the affine pure-
diffeomorphism connection component and had rank ten in v0.28. That component
cannot be transferred silently into the spin-valued selected action.

## Exact selected-action coefficient

The selected intrinsic action is

\[
 I(T)=\frac13\langle T,\mathscr S(T\wedge T)\rangle
      +\frac{\kappa_1}{2}\langle T,*T\rangle. \tag{3}
\]

The predecessor proved that

\[
 T_*= -\frac{\kappa_1}{312}\Phi_1 \tag{4}
\]

has zero full algebraic gradient, not merely zero radial derivative. The
metric coefficient computed here is

\[
 H_g(k)=
 (L^{\rm spin}_k)^T\,D^2I(T_*)\,L^{\rm spin}_k. \tag{5}
\]

Every entry of (5) is rational at `kappa_1=1`, and the matrix scales linearly
with `kappa_1`. The factorized characteristic polynomials are

\[
\begin{aligned}
\chi_t(\lambda)&=\frac{\lambda(117\lambda+31)^2
(117\lambda+62)^3(234\lambda-59)^3(234\lambda+53)}
{65734405323005654352},\\
\chi_s(\lambda)&=\frac{\lambda(117\lambda-62)(117\lambda-31)^2
(117\lambda+55)^2(234\lambda-59)^2(234\lambda-53)(234\lambda+59)}
{65734405323005654352},
\end{aligned} \tag{6}
\]

where each displayed line is a product, not a sum: the line breaks in (6)
should be read as continuous multiplication. The executable certificate is
authoritative. For the null orbit,

\[
 \chi_n(\lambda)=\frac{\lambda^4(18252\lambda^2-3493)
 (27378\lambda^2+13572\lambda-83)^2}{13680875742768}. \tag{7}
\]

Equations (6)--(7) give the rank/inertia table above. Reversing the sign of
`kappa_1` swaps positive and negative counts.

## Second jets and observation

For a nonlinear lift `F`,

\[
 D^2(I\circ F)=D^2I[DF,DF]+DI[D^2F]. \tag{8}
\]

At (4), `DI=0` on the full algebraic carrier. Hence the nonzero second
spin-Levi-Civita and observation jets constructed in v0.29 carry zero
coefficient in this **stationary Hessian**. They remain necessary off shell
and in the stationary cubic, where `D2F` pairs with `D2I`.

The complete first-germ observation map is invertible, so it acts by
congruence on (5) and preserves rank and inertia. This uses the previously
proved complete equation dual. It does not turn the unreduced Hessian into a
physical quotient.

## Diffeomorphism and symplectic obstruction

Let

\[
 D_k(\xi)_{\mu\nu}=k_\mu\xi_\nu+k_\nu\xi_\mu. \tag{9}
\]

The exact `10 x 4` symbol has rank four. But

```text
rank(H_g D_k)       = 3  on timelike, spacelike and null orbits;
rank(D_k^T H_g D_k) = 3, 3 and 2 respectively.
```

Only the `xi` direction producing `k tensor k` is already in the radical.
Thus the isolated spin-Levi-Civita coefficient violates the required
diffeomorphism radical. The missing direct curvature/full-`II`/defect and
observation/compensator blocks are not optional hardening: they are demanded
by this exact residual.

The symplectic disposition is consequently “unreduced coefficient, Ward
totalization required.” No presymplectic characteristic quotient, BFV phase
space or physical transition is inferred.

## What this changes

Five ledger distances move with a scope correction. Verdicts, reason kinds,
residue, quotient count and external data do not:

```text
Ledger v0.30 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

The next gate is sharply smaller: assemble the direct curvature, full-`II`,
defect and observation contributions with (5), then test whether their sum
cancels or retains the exact rank-three diffeomorphism residual. Only the
totalized block may proceed to odd BV, global Krein/Green domain and BFV.

## Seven-axis disposition

- **Layer 0:** Christoffel/spin, connection/diffeomorphism gauge and
  Hessian/Euler/BFV objects are separated.
- **L1 syntactic:** the action spin map and selected stationary Hessian are
  explicit.
- **L2 type:** the longitudinal kernel is typed as `span{k tensor k}`.
- **L3 algebraic:** causal-orbit ranks, characteristic polynomials, inertias
  and Ward restrictions are exact.
- **L4 geometric:** local observed Lorentz principal symbol only.
- **L5 variational/symplectic:** stationary Hessian closes; diffeomorphism
  radical, direct totalization and BV/BFV remain open.
- **L6 analytic:** no common Green/Krein or hyperbolic domain claim.
- **L7 physical:** no Einstein, cosmology, Q1, particle or unitarity claim.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new selectors: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.
