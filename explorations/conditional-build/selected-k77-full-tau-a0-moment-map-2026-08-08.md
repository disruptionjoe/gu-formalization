---
artifact_type: construction_and_composition_result
created: 2026-08-08
status: FULL_NONZERO_A0_TILTED_ALGEBRAIC_EDGE_DESCENT_EXACT_ON_CONDITIONAL_SPIN_NATIVE_PARENT__CHARGED_BOUNDARY_HORN_AND_ANALYTIC_BFV_REMAIN_OPEN
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 full `tau_A0` moment-map descent

## Result in plain English

The flat-reference shortcut is no longer needed. The full tilted construction
with a nonzero distinguished connection `A0` now composes exactly with the
selected boundary action.

First quotient by the left tilted subgroup. This converts the two raw
inhomogeneous-gauge coordinates into the homogeneous distortion
`Theta_A0`. The remaining right tilted action is ordinary adjoint transport.
With the selected action trace, that residual action has a genuine boundary
moment map: before edge completion it is charged and cannot be called gauge.

Add the already-built group-valued edge frame and dress both the distortion
and its cotangent momentum. Then the same residual orbit is exactly the
characteristic kernel. The full derivative cocycle, nonzero `A0`, moment map,
edge cancellation and moving-reference patch law all agree.

This closes the **global algebraic associated-bundle** gate on the
conditionally selected Spin-native action parent. It does not select that
parent from the source, select gauge over charged boundary symmetry, or build
the global analytic BFV phase space. The charged horn remains equally
consistent until boundary observables, polarization and domain are supplied.

## 1. Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| active gauge action | derivative-bearing `tau_A0` double action | passive change of local trivialization |
| left tilted quotient | canonical distortion `Theta_A0` | ordinary affine connection quotient |
| residual right action | homogeneous adjoint action on `Theta_A0` | the original affine action |
| raw moment map | `[Theta_A0,P]` on the unextended phase space | a characteristic gauge kernel |
| edge completion | dressed variables using a group-valued frame | a boundary condition or new bulk field |
| global algebraic descent | cocycle, conjugation and trace patching | completed functional BFV phase space |
| selected action parent | Spin-native grade `1+2+5` carrier | the two-`U(32,32)` or full-`U(64,64)` parents |

The main trap is to call the source's full principal group the symmetry of the
selected residual. It is not: the selected 2,107-dimensional carrier is
Spin-native, while the two-half and full-unitary actions require the already
computed 16,382- and 16,383-dimensional carrier expansions.

## 2. Source return and prior art

Weinstein supplies the distinguished Levi-Civita/Zorro connection, the
inhomogeneous gauge group, bi-connection, tilted homomorphism and two-sided
double-coset grammar. The source does not print a boundary moment map, edge
completion, BFV polarization or operative residual action parent.

```text
SOURCE-CONFIRMS:
  full tilted double action and distinguished A0.

SOURCE-SILENT:
  boundary moment map, edge completion, action-parent selection,
  polarization and analytic BFV domain.
```

The nonzero-`A0` cocycle itself is prior art inside the repository: G1 already
proved the derivative cocycle, tilted graph, moving-reference covariance and
left/right quotient laws. The new result is their composition with the actual
selected action trace and boundary edge geometry. It must not be described as
a fresh derivation of `tau_A0`.

## 3. Full tilted quotient and residual charge

Using the repository's left convention,

\[
q_{A_0}(g)=A_0-g\boldsymbol\cdot A_0,
\qquad \tau_{A_0}(g)=(g,q_{A_0}(g)).
\]

The derivative term makes `tau_A0` a group homomorphism. For an
inhomogeneous-gauge point `omega=(g,a)`, the left quotient is

\[
\Theta_{A_0}(g,a)=\operatorname{Ad}_{g^{-1}}
  (a-q_{A_0}(g)).
\]

It is left-tilted invariant and transforms under the residual right copy as
`Theta -> Ad(h^-1)Theta`. With cotangent momentum transforming in the same
adjoint representation, cyclicity of the selected trace gives the Hamiltonian

\[
\mu_\xi=\operatorname{Tr}(P[\Theta,\xi]),
\qquad \mu=[\Theta,P].
\]

The exact fixture has `mu != 0`. Omitting the derivative term, using the raw
affine translation, or replacing `mu` by a scalar trace all fail planted
checks.

## 4. Edge completion and characteristic kernel

Let the edge frame transform by `u -> u h`, and define

\[
Q=u\Theta u^{-1},\qquad \Pi=uPu^{-1}.
\]

Both are invariant. On the exact noncommuting rational fixture, the dressed
map has rank eight. Pulling back the canonical trace symplectic form produces

```text
extended coordinate dimension: 12
presymplectic rank: 8
characteristic-kernel dimension: 4
residual gl(2) orbit rank: 4
kernel equals residual orbit: yes
```

Freezing the edge frame leaves the action charged. Thus the cancellation is
not a property of the raw trace or of the tilted quotient by itself; it is the
edge completion doing exactly the work it was introduced to do.

Moving `A0`, `Theta`, `P` and the generator together conjugates the moment-map
section and leaves its scalar Hamiltonian unchanged. This is the associated-
bundle patch law. It is representation-independent once an invariant trace
and preserved carrier are declared.

## 5. Action-parent fence

| parent | preserves the selected carrier? | present disposition |
| --- | --- | --- |
| `Spin(7,7)` | yes; dimension 2,107 | operative conditional build |
| `U(32,32) x U(32,32)` | no; closure dimension 16,382 | rival parent |
| `U(64,64)` | no; closure dimension 16,383 | rival parent |

The algebraic moment-map theorem extends to either large group on its proper
expanded carrier. This wave does not silently perform that expansion and does
not use the full group to claim invariance of the selected action.

## 6. What closes and what remains

Closes:

- full nonzero-`A0` tilted double action composed with the boundary problem;
- left quotient to the homogeneous distortion;
- exact action-trace residual moment map;
- conditional edge cancellation and kernel equality;
- moving-reference/associated-bundle algebraic patching.

Remains:

- source selection among the three action parents;
- physical selection between edge gauge and charged boundary symmetry;
- a global functional space, topology and BFV charge algebra;
- boundary polarization and admissible boundary conditions;
- common closed Green/Krein domain, positivity and quantum measure;
- reduced stress, Einstein recovery and phenomenology.

## 7. Specialist and hostile review

- **Symplectic geometry:** the raw commutator moment map is live; the edge
  frame, not the bulk quotient, makes its orbit characteristic.
- **Differential geometry:** the cocycle and conjugation laws define an
  associated-bundle section, but do not prove existence of every global
  physical section.
- **Representation theory:** the result is exact only relative to a preserved
  carrier. The source's two halves and full group cannot be collapsed.
- **Variational PDE:** no boundary condition or differentiable domain is
  selected by an algebraic moment-map cancellation.
- **Analytic/path-integral:** no completion, polarization, contour,
  determinant, positivity or measure follows.
- **Constraint accounting:** no field, coefficient, datum, quotient or residue
  is added. The parent and physical-boundary forks remain visible.

Hostile verdict:
`FULL_TAU_A0_ALGEBRAIC_EDGE_DESCENT_SURVIVES__PHYSICAL_BOUNDARY_AND_ANALYTIC_BFV_SELECTION_REJECTED`.

## 8. Progress and next gate

```text
Ledger v0.102 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 4
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

No verdict, residue, quotient, datum, canon or public posture changes.
P1/P2/P3 remain unused.

Next:

`GLOBAL_FUNCTIONAL_BFV_COMPLETION_AND_POLARIZATION_ON_CONDITIONAL_EDGE_HORN_VERSUS_CHARGED_BOUNDARY_CHARGE_ALGEBRA__THEN_COMMON_GREEN_KREIN_DOMAIN`.

Evidence: main exact probe `55/55 PASS`; independent Sage/QQ `20/20 PASS`.
