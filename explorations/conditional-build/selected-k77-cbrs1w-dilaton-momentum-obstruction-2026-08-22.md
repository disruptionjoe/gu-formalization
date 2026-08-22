---
title: "Selected-K77 CBRS-1W action-owned dilaton momentum obstruction"
status: active_research
doc_type: exact_formal_local_dilaton_primitive_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1w-dilaton-momentum-obstruction.json
probe: tests/channel-swings/selected_k77_cbrs1w_dilaton_momentum_obstruction_probe.py
grade: "EXACT RECONSTRUCTION-GRADE FORMAL-LOCAL OBSTRUCTION TO THE MINIMAL ACTION-OWNED ONE-DILATON PRIMITIVE-MOMENTUM CLASS; NOT A NO-GO FOR ISOTROPIZING MULTIPLETS OR TYPED ODD-CLIFFORD OWNERS"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_DERIVES_THE_MINIMAL_ACTION_OWNED_DILATON_MOMENTUM_OBSTRUCTION__SOURCE_SILENT_ON_THE_COMPENSATOR_CLASS_AND_OBSTRUCTION
canon_verdict_change: none
---

# Selected-K77 CBRS-1W action-owned dilaton momentum obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1W exact formal-local obstruction to the minimal action-owned one-dilaton primitive-momentum completion
carrier: complete selected-first-action T plus independent Spin connection four real Grassmann-even coframe scalars and one repository-constructed real dimensionless compensator chi near the unit base-J4 body LAYER=toy CHIRALITY=N/A
pairing: exp(-2 chi)-weighted selected K77 scalar-density pairing plus fixed internal Lorentz coframe kinetic pairing and positive one-half scalar kinetic pairing ON=primitive_cancelling_homothetic_disformal_base_J4_candidate
real_structure: real base-J4 radical pair with fixed same-signature internal Lorentz form and real scalar chi
grading: inherited Clifford grades one and three for the unrestricted momentum; chi is Z2-even and supplies a non-gauge radial dilation weight rather than a Spin-grade-two derivation
action_owner: repository-construction
target: simultaneous T connection primitive-epsilon coframe compensator and intrinsic MET(X) local Euler completion MAP-TYPE=evaluation
```

## Result first

The smallest action-owned completion of CBRS-1V's missing radial direction can
cancel the primitive divergence, but it cannot solve its own complete Euler
system.

Add one real dimensionless scalar `chi` and freeze the target-blind action

```text
L_W = exp(-2 chi) [C3(T)+rho Q2(T)]
      +(1/2) g^{-1} eta(dPhi,dPhi)+(rho-1)^2/4
      +(1/2) g^{-1}(dchi,dchi).
```

The exponent, kinetic coefficient and unit scale are fixed before solving.
There is no scalar potential in the minimal class. The exponent `-2` is not a
fit to the J4 density: it is the unique scalar weight that can neutralize the
already exact homogeneity `M(rho)=rho^2 M0` while retaining the nonzero
`T=rho T0` branch.

The weighted unrestricted momentum is

```text
M_W = exp(-2 chi) rho^2 M0.
```

At the unit-spacelike coframe orbit, the nonzero positive-norm active row makes
primitive cancellation require

```text
dchi=d log(rho),       chi=log(rho)
```

after fixing `chi=0` at `rho=1`. This is a genuine non-gauge grade-one/three
return. It is not a naked Weyl connection: `chi` carries the field equation

```text
-box_g chi - 2 exp(-2 chi)[C3(T)+rho Q2(T)] = 0.
```

Primitive cancellation is therefore real. It is also insufficient.

## The full metric row and its unique disformal candidate

Because `dPhi` is invertible, use the four `Phi^A` as local coordinates. Then
`rho=eta_AB Phi^A Phi^B`, `Phi^A=y^A`, and `chi=log(rho)` without selecting an
observed frame. Put

```text
B=eta_AB dPhi^A tensor dPhi^B=eta,
p=dchi,
V(rho)=I_base rho+(rho-1)^2/4.
```

The complete intrinsic metric row is

```text
B+p tensor p-g L_W=0.
```

Tracing it and using
`L_W=(1/2)tr_g(B+p tensor p)+V` forces `L_W=-V`. Thus every regular solution
in the frozen class must use the unique disformal metric

```text
g=-(eta+dchi tensor dchi)/V.
```

At the unit-spacelike body its numerator is `diag(-1,5,1,1)`, with determinant
`-5`; the metric candidate is regular Lorentzian because `I_base<0`.

The remaining Euler rows nevertheless fail exactly. Direct divergence in the
disformal numerator gives

```text
box_h chi = 108/25,
box_h Phi_active = -16/25.
```

After the conformal factor `c=-V`, the unit-body values are

```text
box_g chi = -88 I_base/25,
box_g Phi_active = 26 I_base/25.
```

The action requires `box_g chi=-2 I_base` and
`box_g Phi_active=6 I_base`. Hence the exact residuals are

```text
E_chi = 38 I_base/25 != 0,
E_Phi_active = 124 I_base/25 != 0.
```

Both base-J4 signs share the same nonzero density and the same obstruction.

## Arbitrary smooth-potential hostile control

A potential added after this mismatch would be a new class, but it is useful
to test whether that obvious rescue even exists. Write
`w0=W(0)` and `w1=W'(0)` before solving. Simultaneous unit-body coframe and
compensator Euler closure uniquely requires

```text
w0=-I_base,       w1=14 I_base.
```

The first condition makes the metric scale
`c=-(I_base+W(0))` exactly zero. The supposedly rescued metric is singular.
Therefore no regular smooth scalar potential rescues this one-dilaton class;
the failure is not merely the choice `W=0`.

## Hostile return and ceiling

- **Strongest positive control:** the new scalar really does make
  `exp(-2chi)rho^2 M0` constant. Calling CBRS-1W another primitive-divergence
  failure would be false.
- **Strongest dropped-owner failure:** primitive cancellation does not imply
  the `chi`, coframe or intrinsic metric equations. The last two exact rows
  close the class.
- **Strongest potential rescue:** arbitrary unit-body potential jets can cancel
  both displayed Euler residuals only by collapsing the metric scale.
- **Strongest coordinate trap:** `Phi=y` uses the already invertible coframe as
  local coordinates. It is not a branch-selected physical frame or boundary.
- **Strongest extension overclaim:** an internally indefinite multiplet or a
  typed odd-Clifford primitive can carry rank-four stress and independent odd
  return. Neither is contained in this one-scalar action.
- **Strongest source overclaim:** this compensator is repository-constructed.
  The source confirms the action grammar, not this new field or obstruction.

No stabilizer, spectrum, ledger verdict, canon, source ownership, residue,
particle assignment, prediction, confirmation or public posture changes.

## Reverse-scaffold consequence

Continue with `CBRS-1X`: freeze the smallest target-blind action-owned
**isotropizing** primitive-momentum owner with an independent non-gauge
grade-one/grade-three return. Decide the internally indefinite multiplet versus
typed odd-Clifford-field fork structurally before reading a J4 density, and
require the complete field, primitive and intrinsic `MET(X)` equations. Do not
add a fitted scalar potential, branch-selected frame, boundary or multiplier,
and do not advance to CBRS-2 or compute a spectrum before an actual local
solution exists.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1w_dilaton_momentum_obstruction_probe.py
```

The exact probe passes after native propagation.
