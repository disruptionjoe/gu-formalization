---
title: "Selected-K77 CBRS-1X indefinite mirror-multiplet obstruction"
status: active_research
doc_type: exact_formal_local_indefinite_mirror_multiplet_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1x-indefinite-mirror-multiplet-obstruction.json
probe: tests/channel-swings/selected_k77_cbrs1x_indefinite_mirror_multiplet_obstruction_probe.py
grade: "EXACT RECONSTRUCTION-GRADE RANK-MINIMAL POINTWISE FORMAL MIRROR-MULTIPLET SOLUTION AND LOCAL HOMOTHETIC OBSTRUCTION; NOT A NO-GO FOR NONHOMOTHETIC SIGMA-MODEL OR TYPED ODD-CLIFFORD OWNERS"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_DERIVES_THE_RANK_MINIMAL_INDEFINITE_MIRROR_MULTIPLET_AND_ITS_LOCAL_HOMOTHETIC_OBSTRUCTION__SOURCE_SILENT_ON_THE_MULTIPLET_CLASS_AND_OBSTRUCTION
canon_verdict_change: none
---

# Selected-K77 CBRS-1X indefinite mirror-multiplet obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1X exact rank-minimal pointwise formal opposite-signature mirror-multiplet solution and local homothetic obstruction
carrier: complete selected-first-action T plus independent Spin connection four real Grassmann-even coframe scalars and four repository-constructed real Grassmann-even mirror scalars near the unit base-J4 body LAYER=toy CHIRALITY=N/A
pairing: s^(-2)-weighted selected K77 scalar-density pairing plus fixed internal Lorentz coframe kinetic pairing eta and opposite internal Lorentz mirror kinetic pairing kappa=-eta ON=primitive_cancelling_homothetic_base_J4_candidate
real_structure: real base-J4 radical pair with fixed opposite Lorentz forms eta and kappa=-eta and real mirror norm R=2/3
grading: inherited Clifford grades one and three for the unrestricted momentum; Psi is Z2-even and supplies a non-gauge invariant-weight return rather than a Spin-grade-two derivation or odd-Clifford source field
action_owner: repository-construction
target: simultaneous T connection primitive-epsilon coframe mirror-multiplet and intrinsic MET(X) unit-body plus local homothetic Euler completion MAP-TYPE=evaluation
```

## Result first

The smallest isotropizing action owner can cancel CBRS-1W's primitive
divergence and solve every Euler row at the unit body. The inherited unit-orbit
potential prevents that solution from extending along its first natural local
homothetic branch.

Add four real Grassmann-even fields `Psi^a`, freeze the opposite internal
Lorentz form `kappa=-eta`, and put

```text
s = kappa_ab Psi^a Psi^b,

L_X = s^(-2) [C3(T)+rho Q2(T)]
      +(1/2) g^(-1) eta(dPhi,dPhi)+(rho-1)^2/4
      +(1/2) g^(-1) kappa(dPsi,dPsi).
```

The action, real forms, exponent, kinetic coefficients and potential are fixed
before a J4 density is read. There is no multiplier, fitted coefficient,
branch-selected frame or odd-Clifford pairing hidden in the definition.

On the homothetic mirror ray

```text
Phi=y,       Psi=sqrt(R) Phi,       s=-R rho,
```

the two independent multiplet Euler equations uniquely fix

```text
R=2/3.
```

This number is independent of `I_base`: the coframe equation has eigenvalue
`6J`, the mirror equation has eigenvalue `4J/R`, and equality gives `R=2/3`.
The same-signature class would require `R=-2/3` and therefore has no real
homothetic branch. Opposite inertia is an Euler consequence, not a spacetime
signature switch chosen after seeing the base-J4 sign.

## Why this fork is structurally first

If `N` real first jets are assembled into a `4 by N` matrix, their pullback
Gram tensor has rank at most `N`. A nonzero tensor proportional to a
four-dimensional Lorentz metric has rank four, so an isotropizing first-jet
owner needs at least four real fields. The selected multiplet attains that
bound.

The contrary odd-Clifford route is real but not smaller at this gate. The live
primitive row already has `18` supported grade-one/grade-three cells inside
the `78`-dimensional receiver reached by the unrestricted connection map. A
typed odd field would additionally require its real involution, action pairing,
kinetic sign and Hilbert-stress map. None is source-supplied. Deferring it is a
carrier-minimality decision, not a claim that odd-Clifford owners cannot work.

## Exact primitive cancellation and unit-body stationarity

On `T=rho T0`, the unweighted point action and momentum are

```text
C3(T)+rho Q2(T)=I_base rho^3,
M(rho)=rho^2 M0.
```

Because `s=-R rho`, the weighted quantities become

```text
s^(-2) I_base rho^3 = J rho,
s^(-2) rho^2 M0 = R^(-2) M0,
J=I_base/R^2=(9/4)I_base.
```

Thus `d log(abs(s))=d log(rho)` makes the unrestricted momentum exactly
constant. At `R=2/3`, the coframe and mirror pullbacks are

```text
B=eta,       K=-(2/3)eta,       B+K=(1/3)eta.
```

The complete intrinsic metric equation fixes

```text
g=-eta/(3U),
U(rho)=J rho+(rho-1)^2/4.
```

At `rho=1`, this is the regular Lorentz metric

```text
g=-4 eta/(27 I_base).
```

For `g=c(rho)eta` in four dimensions,

```text
box_g y^A = 2 c'(rho)/c(rho)^2 y^A = 6 U'(rho)y^A.
```

At the unit body `U'=J`, so both independent multiplet equations require and
receive `box_g Phi=6J Phi` and `box_g Psi=6J Psi`. The `T`, independent Spin
connection, weighted primitive-epsilon and all ten intrinsic `MET(X)` rows
also vanish. This is an exact pointwise formal two-jet solution for both
base-J4 radical signs.

## The local homothetic obstruction

The same identity exposes the omitted local condition. For the inherited
potential `V=(rho-1)^2/4`, the metric requires

```text
box_g y = 6[J+(rho-1)/2] y.
```

The coframe and mirror equations instead require

```text
box_g Phi = [6J+(rho-1)] Phi,
box_g Psi = 6J Psi.
```

Their exact residuals are therefore

```text
E_Phi = -2(rho-1) Phi,
E_Psi = -3(rho-1) Psi.
```

They vanish at the unit body but not on any open neighborhood where the
coframe makes `rho` nonconstant. The pointwise formal solution is not an
actual local vacuum.

For an arbitrary smooth replacement `V(rho)`, the two residual coefficients
are `-4V'(rho)` and `-6V'(rho)`. Both vanish on an open interval only when
`V` is constant there. A constant potential permits the homothetic local
equations but releases the unit `rho` orbit instead of selecting it. Hence a
post-result potential fit does not rescue the frozen unit-orbit class; it
changes the selection problem.

## Retrieval, controls and hostile review

Mechanism-level retrieval found CBRS-1T's same-signature coframe owner,
CBRS-1W's scalar weight, conventional mirror-multiplet mentions, indefinite
Krein carriers and the existing odd grade-one/three receiver. None combines
the opposite-signature rank minimum, `s^(-2)` primitive completion,
density-blind `R=2/3` solve and complete local Euler residuals recorded here.

- **Strongest positive control:** the mirror owner genuinely makes the
  weighted momentum `(9/4)M0` constant and closes every unit-body Euler row.
- **Strongest overclaim:** exact unit-body closure is only a pointwise formal
  two-jet result. The nonzero `rho-1` residuals forbid the displayed local
  homothetic vacuum.
- **Strongest same-signature control:** identical internal inertia forces the
  impossible real norm `R=-2/3`; the opposite form is selected before the J4
  density and is not a frame relabeling.
- **Strongest potential rescue:** arbitrary smooth `V` closes the local ray
  only at `V'=0`, which removes rather than implements unit-orbit selection.
- **Strongest odd-field contrary route:** a directly typed odd-Clifford field
  may carry the required receiver and a different stress map. This result does
  not test or exclude it.
- **Strongest source overclaim:** both `Psi` and its action are repository
  constructions. The source confirms the action grammar, not this field.
- **Weakest reproducibility seam:** the conformal d'Alembertian and the sign of
  the mirror Euler source are derived independently in the exact probe.

No stabilizer, spectrum, ledger verdict, canon, source ownership, residue,
particle assignment, prediction, confirmation or public posture changes.

## Reverse-scaffold consequence

Continue with `CBRS-1Y`: freeze the smallest target-blind **nonhomothetic**
sigma-model metric or directly typed odd-Clifford primitive owner capable of
preserving unit-orbit selection while closing the complete local Euler system.
The next class must state its real pairing, action coefficient, grading and
stress map before solving. Do not tune a potential, multiplier, frame,
boundary or sector after the result, and do not compute a spectrum or advance
to CBRS-2 before an actual local solution exists.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1x_indefinite_mirror_multiplet_obstruction_probe.py
```

The exact probe passes after native propagation.
