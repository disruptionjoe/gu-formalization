---
artifact_type: construction_result
created: 2026-08-06
status: SECOND_JETS_AND_NONLINEAR_FORMAL_ADJOINT_OWNER_EXACT__DIRECT_SELECTED_ACTION_COEFFICIENT_EXPANSION_OPEN
source_return: SOURCE-CONFIRMS_AND_SOURCE-SILENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_second_soldering_observation_jets_probe.py
registry: lab/process/selected-action-second-soldering-observation-jets.json
---

# Selected-action second soldering and observation jets

## Result first

The second local geometric derivatives required by the nonlinear physical
chain now exist as exact tensors. The symmetric-frame spin
Levi-Civita connection has a nonzero, symmetric second metric jet. The
complete first-jet observation map is affine in the section jet, so its pure
section Frechet second derivative is exactly zero, but its section--field
cross derivative is nonzero. A spatial second section jet enters through
total differentiation rather than through a new observation datum.

These facts close the owner problem for the nonlinear formal-adjoint Euler
term and its preboundary companion. They do **not** yet expand the actual
selected action's metric, Hodge, Shiab, Krein, density and observation
coefficients on those owners. Full selected-action stationarity, BV, global
domain and BFV therefore remain open.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| second Levi-Civita jet | second metric derivative of the symmetric-frame spin connection used by the fermionic/action carrier | merely the coordinate Christoffel second derivative |
| pure observation second jet | Frechet `D_J^2` of the affine complete-germ map | the spatial derivative `dJ`, i.e. the section's second spacetime jet |
| cross observation jet | `D_J D_a(M(J)a)` | a new field or external datum |
| nonlinear Euler owner | chain-rule plus formal-adjoint location of all second-jet terms | their coefficients in the full selected action |
| preboundary owner | Cartan/Green boundary coefficient before reduction | a BFV phase space or charge |

The distinction between Christoffel and spin connections is load-bearing.
The selected action couples through the symmetric-frame spin connection. A
Christoffel-only calculation would have computed a related but mistyped
object.

## Source collision

The source says that augmented torsion is a difference of connections and
that a gauge-rotated Levi-Civita connection occupies the contorsion slot. It
also corrects a naive pullback-only reading of observation. This confirms the
geometric route and owner class. The source does not supply the second spin
connection jet, the affine/cross observation Hessian, or the nonlinear
formal-adjoint and Cartan identities.

```text
SOURCE-CONFIRMS: gauge-rotated Levi-Civita, two-connection augmented torsion,
                 richer-than-naive observation
SOURCE-SILENT:   exact second jets, nonlinear Euler/preboundary owner,
                 expanded selected-action coefficients and BV/BFV closure
```

## Exact second Levi-Civita jets

For a background metric `eta`, variations `h,l` with Fourier covectors
`p,q`, and

\[
 C(h,p)_{\mu\nu\sigma}
 =p_\mu h_{\nu\sigma}+p_\nu h_{\mu\sigma}
  -p_\sigma h_{\mu\nu},
\]

the mixed coordinate-connection derivative is

\[
 D^2\Gamma[h,p;l,q]^\rho{}_{\mu\nu}
 =-\frac12\left[(\eta^{-1}h\eta^{-1})^{\rho\sigma}
 C(l,q)_{\mu\nu\sigma}
 +(\eta^{-1}l\eta^{-1})^{\rho\sigma}
 C(h,p)_{\mu\nu\sigma}\right]. \tag{1}
\]

An independent symbolic inverse-metric differentiation reproduces (1), and
the exact TT witness is nonzero and symmetric in `(h,p)` and `(l,q)`.

The selected-action object is the spin connection in the moving symmetric
frame. Write a two-parameter frame square root

\[
 e=I+\tfrac12\eta h\,t+\tfrac12\eta l\,u
 -\tfrac18\bigl[(\eta h)(\eta l)+(\eta l)(\eta h)\bigr]tu. \tag{2}
\]

The probe verifies through mixed order that `e^T eta e=g`, constructs the
exact inverse, and evaluates

\[
 \omega_\mu=(e\Gamma_\mu-\partial_\mu e)e^{-1}. \tag{3}
\]

Equation (3) satisfies the tetrad postulate and is `eta`-skew coefficient by
coefficient. Its linear term is exactly the already-used selected-cubic owner

\[
 \omega_{\mu ab}^{(1)}
 =\tfrac12(k_b h_{\mu a}-k_a h_{\mu b}), \tag{4}
\]

while its mixed second coefficient is nonzero and symmetric. Gauge rotation
then applies an invertible adjoint action; motion of the gauge element adds a
connection-gauge image and does not erase this owner.

## Exact observation Hessian

For the complete first-germ map

\[
 M(J)=\begin{pmatrix}I&J^T\\0&I\end{pmatrix}, \tag{5}
\]

the dependence on the section jet `J` is affine:

\[
 D_J^2 M=0. \tag{6}
\]

But the observed field is the product `M(J)a`, whose mixed derivative is

\[
 D^2(M(J)a)[(j_1,a_1),(j_2,a_2)]
 =D M(j_1)a_2+D M(j_2)a_1, \tag{7}
\]

and the exact rational witness is nonzero. The equation dual is likewise
affine in `J`. Separately, a spacetime derivative of (5) contains `dJ`, the
second spacetime jet of the observation section. Thus the nonlinear chain
needs second section jets but no new datum.

## Variational and symplectic owner

If `A(g,\partial g)` denotes the soldered connection and `I(A)` the action,
then the nonlinear metric Euler term has the typed chain-rule form

\[
 E_g(I\circ A)
 =D_gA^!E_A(I)+\text{terms from }D_g^2A,
 \qquad
 \Theta_g=\Theta_{\rm direct}+\Theta_A+\Theta_{\rm obs}. \tag{8}
\]

The scalar exact control `A=g_1/g_0`, `L=A^2/2` verifies (8) by two independent
routes. The direct composite Euler derivative equals the chain-rule formal
adjoint, contains the second spatial jet `g_2`, and has the same Cartan
coefficient as the soldered preboundary term. Deleting total derivatives
fails the planted control.

This owns the locations and derivative orders of the nonlinear contributions.
It does not compute the full matrix of coefficients obtained after inserting
the selected metric, Hodge, Shiab, Krein pairing, density and observation
maps.

## What this changes

Five ledger distances move and no verdict, reason kind, residue, quotient or
datum changes:

```text
Ledger v0.29 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

The next gate is now coefficient assembly rather than owner discovery:
expand the actual selected action's metric/Hodge/Shiab/Krein/density and
observation coefficients on this exact second-jet packet. Only after that
should the lane claim the full nonlinear Euler/presymplectic class and proceed
to diffeomorphism/odd BV, global domain and unrestricted BFV.

## Seven-axis disposition

- **Layer 0:** Christoffel/spin connection, Frechet/spatial jets, owner/full
  coefficient and preboundary/BFV are separated.
- **L1 syntactic:** every required second derivative has an explicit owner.
- **L2 type:** frame, connection, section and field slots are distinct.
- **L3 algebraic:** all identities are exact over rationals; planted freezes
  fail.
- **L4 geometric:** local Lorentz symmetric-frame germ only; global descent
  is excluded.
- **L5 variational:** nonlinear formal-adjoint and preboundary owners close;
  direct selected-action coefficient expansion and BV/BFV remain open.
- **L6 analytic:** no closed Green/Krein or maximal domain claim.
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

## K118 successor closure — 2026-08-15

These second jets supply part of the required chain-rule data, but they do not
by themselves select the action layer or the full observed-to-native map.
K118 also exhibits four unfixed entries in the first-order pencil after the
known `hh` and `vv` projections are imposed.  Consequently the next operation
is K119 action-layer/scalar-lift selection, followed by complete coefficient
assembly only after that typed map is fixed.

## K120 successor refinement — 2026-08-15

K120 composes this second spin-Levi-Civita jet with the source-coordinate map
`T=varpi-B_LC(g)`, closing `I1B` custody for the two TT columns and their
nonlinear metric second jet. The remaining map defect is no longer the full
two-jet: it is the one-dimensional identification
`theta_Isc -> lambda theta Phi1`. K121 must select that scalar bridge before
coefficient assembly.
