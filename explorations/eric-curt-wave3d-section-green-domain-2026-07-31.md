---
title: "Eric/Curt Wave 3D-A: admitted-section right-H Green-domain gate"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
campaign_wave: ECW3-G4-OBSERVATION
registry: lab/process/eric-curt-wave3d-section-green-domain.json
probe: tests/channel-swings/eric_curt_wave3d_section_green_domain_probe.py
grade: "COMPUTED EXACT FINITE RS SECTION-SYMBOL AND RIGHT-H GREEN-TRACE PACKET; DECISIVE DOMAIN-SELECTION NON-UNIQUENESS, NOT AN ANALYTIC CLOSED-DOMAIN THEOREM. On one explicitly admitted flat Lorentz/spin section, the W131 ker-Gamma symbol restricts to Cl(3,1), has the Lorentz null characteristic cone, and emits a nondegenerate balanced (832,832) Green trace. Both opposite maximal-definite spectral sectors are right-H invariant, so the native principal/Krein/right-H algebra does not select a unique boundary domain."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
third_lane_promotion: none
---

# Wave 3D-A admitted-section right-`H` Green-domain gate

## Result first

ECW3C killed ordinary codimension-one Lorentzian evolution on the full
signature `(9,5)` ambient `Y^14`. ECW3D-A tests the open section branch on one
explicitly admitted flat Lorentz/spin section. In an adapted gimmel frame its
tangent directions have signature `(3,1)`. Restricting the verified W131
Clifford/Rarita--Schwinger packet to those covectors gives an exact
`Cl(3,1)` principal symbol on the complex rank-1664 bundle `ker Gamma`.

The pullback has the expected Lorentz characteristic split: nonnull
spacelike and timelike section covectors are noncharacteristic, while a
Lorentz-null covector is characteristic. The native antilinear quaternionic
generator preserves `ker Gamma`, and the restricted principal symbol remains
right-`H` linear.

For a timelike boundary with a spacelike conormal `n`, the formal Green trace
matrix

\[
 B_n(u,v)=u^\dagger K\,\sigma(n)v
\]

is Hermitian, nondegenerate, and balanced:

\[
 \operatorname{inertia}(B_n)=(832,832,0).
\]

Both opposite spectral trace sectors are right-`H` invariant, distinct, and
exhaust the trace space. They carry opposite definite Green-flux signs. Thus
the principal/Krein/right-`H`/Green algebra supplies compatible trace data but
does **not** select a unique boundary sector. This is the decisive result of
the swing: analytic boundary/domain input remains irreducible.

## Layer-0 boundary

| shared term | objects kept separate | disposition |
| --- | --- | --- |
| Lorentz section | one supplied flat Lorentz/spin section; existence on arbitrary `X` | `HOMONYM` |
| section pullback | restriction of the W131 principal symbol; ambient `Y^14` propagator | `HOMONYM` |
| Green domain | finite Green trace matrix; closed/self-adjoint Sobolev realization | `HOMONYM` |
| right-`H` compatible | right-`H` coefficients and selected trace subspaces; every possible boundary condition | `HOMONYM` |

No signature component, gamma-trace rank, or Green inertia is interpreted as
a particle, field, or generation count.

## Construction

Let `e_0,...,e_13` be the repository's verified signed Jordan--Wigner
generators for `Cl(9,5)`, and let

\[
 \Gamma=[e_0\ \cdots\ e_{13}],\qquad
 \Pi=1-\Gamma^\dagger\Gamma/14.
\]

W131 proves that `Pi` is parallel for every metric-compatible ambient
connection and that the ambient Krein structure is parallel. ECW3D-A does not
reprove that wave. It takes the adapted section tangent block

\[
 (e_0,e_1,e_2,e_9),\qquad (+,+,+,-),
\]

and restricts

\[
 \sigma_s(\xi)=\Pi\bigl(1_{14}\otimes c_s(\xi)\bigr)\Pi
 \quad\text{to }\ker\Gamma.
\]

The probe verifies the `Cl(3,1)` relations, first-order linearity,
nonnull/null characteristic split, and right-`H` intertwining on the full
1,664-dimensional gamma-traceless carrier. It then constructs `B_n` rather
than importing RB3c's one-dimensional planted Green fixture.

This construction is conditional on the admitted section, its spin lift, and
the adapted horizontal split. It is a section trace theorem at finite
principal-algebra grade, not a global section-existence theorem.

## Exact control

The deterministic full-carrier probe passes:

- ambient gamma-trace closure and rank 1664;
- nondegenerate Hermitian ambient Krein form;
- quaternionic `J conjugate(J)=-1` and preservation of `ker Gamma`;
- exact section signature `(3,1)` and `Cl(3,1)` relations;
- spacelike/timelike noncharacteristic and null characteristic controls;
- right-`H` linearity of the pulled symbol;
- Hermitian Green trace with inertia `(832,832,0)`; and
- right-`H` invariance, opposition, and completeness of the two Green
  spectral trace sectors.

Result: `24 exact + 10 planted = 34 PASS`.

The planted controls reject automatic global section existence, resurrection
of ambient `(9,5)` hyperbolicity, Green-form-to-closed-domain inference,
unique selection of either spectral sector, automatic right-`H` invariance of
arbitrary boundary data, nonlinear Euler closure, physical BFV reduction,
Curt real-domain transport through complexification, and third-lane promotion.

## Constraint/parameter surplus

The algebraic compatibility constraints all pass. Domain surplus is not yet
computable. At least one boundary-sector choice remains unselected, while the
full space of closed extensions has not been enumerated. Neither the analytic
constraint rank nor the domain-parameter rank is defined until a
variable-coefficient section operator, trace space, regularity class, and
boundary condition are frozen. Physical surplus therefore remains
`UNCOMPUTABLE`.

## Non-regression matrix

| family | disposition |
| --- | --- |
| gravity | no section Einstein equation or stationary background is claimed |
| gauge | W131 metric-connection compatibility is retained; no closed gauge quotient is built |
| odd matter | the RS principal/Green trace packet advances; the Einstein--Dirac action remains open |
| Higgs/Yukawa | untouched |
| quantum/domain | formal Green trace advances; closedness, propagator, and BFV remain open |
| cosmology | untouched |
| `P1/P2/P3` | unconsumed |

## Curt rival and promotion gate

Curt remains a formally separated `CURT_CANDIDATE` track inside the Eric
lane. The literal real `(7,7)` proposal still owes its own actual atlas,
right-structure, action, section symbol, Green trace, and common-domain
discriminator. The common complex Clifford algebra does not transport those
real analytic data.

The pre-registered rule remains `TG-1 AND TG-2 AND TG-3`. `TG-1` is partial;
`TG-2` and `TG-3` remain open. No third lane is promoted.

## What is earned and what remains

Earned:

- an exact `Cl(3,1)` section pullback of the W131 principal packet on one
  explicitly admitted section;
- preservation of the native right-`H` structure;
- a nondegenerate balanced Green trace on `ker Gamma`; and
- a decisive non-selection theorem: the exact algebra admits two opposite
  right-`H` trace sectors and chooses neither.

Not earned:

- a global Lorentz/spin section for arbitrary `X`;
- variable-coefficient Sobolev or graph-domain closedness;
- maximal dissipativity, self-adjointness, or a selected polarization;
- nonlinear Euler/constraint propagation on the chosen domain;
- a propagator or physical BFV phase space.

The next gate is
`ECW3D-B-VARIABLE-COEFFICIENT-RIGHT-H-CLOSED-DOMAIN`: freeze one explicit
boundary polarization and variable-coefficient section geometry, define the
Sobolev/graph domain, and prove or kill closedness plus right-`H` and
constraint preservation. The campaign's broader live ECW3D pointer remains
unchanged for completed-wave regression compatibility.
