---
title: "BET-2PLUS1: actual time-jet reconstruction and infrared conditioning"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: BET-2PLUS1
tier: T2
expected_delta: "Resolve dynamic observation and propagation requirements on the held raw model."
actual_delta: "First time jets recover nonzero modes exactly; zero modes and low-frequency instability remain; no conserved family inference."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# BET-2PLUS1: actual time-jet reconstruction and infrared conditioning

**Result.** On unrestricted solutions of the fixed raw model, literal
pullback plus its first actual time derivative recovers the hidden normal sum
at every nonzero spatial momentum. The exact residual gain is proportional to
|p|, so inversion loses infrared stability. A finite observation history does
not cure that loss. Reconstruction retains the inherited Jordan dynamics;
it is not a positive physical quotient or a conserved family decomposition.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: conditional observation transfer on the original fixed-plane raw equation
carrier: K2236 real1920 parent and C768 quotient, complexified Fourier modes LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: auxiliary Euclidean observation norm; not inherited raw Green or physical probability ON=declared_carrier
real_structure: original real Cl77 representation, complex Fourier conjugation with p mapped to minus p
grading: ambient trace/remainder/scalar provenance, not physical family or observed Weyl grading
action_owner: repository-construction -- unchanged raw contraction and original mass return; no new action
target: literal fixed-plane pullback, time jets and explicitly restricted Fourier data MAP-TYPE=intertwiner
```

## Native scope and reused evidence

program_target: BET-2PLUS1
tier: T2
expected_delta: Complete a typed observation/dynamics seam; no physical count.
actual_delta: Conditional observation and propagation result; bet remains active.

SC-GEN-01 DISAVOWS simple triplication; SC-GEN-02/03 ASSERTS the hedged
2+1 proposal; SC-FER-04/05 ASSERTS algebraic branching labels. SC-GEN-52 is
UNCERTAIN about the spoken trace/kernel terminology. SC-CHI-01/51 ASSERTS
non-chiral total/effective observed splitting. SC-OP-04 ASSERTS only candidate
operator grammar; SC-OP-05 admits an UNCERTAIN southeast rival. These source
polarities and ledger0.263 RA-F1/AC-F1/LT-SM8 remain unchanged.

This is K2236's supplied real Cl(7,7) unbarred raw contraction, not the source's
uniquely chosen four-field operator, K95 real form or a physical state space.
Observation is contraction on O={0,7,8,9}; all ten normal derivatives are absent.
Normalize as K2236: zeta_a=eta_a gamma_a u_a, nu=Wbar h,
Wbar=(3I+J)/2, J²=I. V consists of the nine spinor-sized hidden normal
sum-zero slots. On its complementary C write
u=(a,b1,b2,b3,v,h), v=sum_normal(u_r)/10. Literal observed output is
q=(a,b1,b2,b3,h). Spinor size s=128 real upstairs, complex dimension128
after complexification. Counts below are linear dimensions, never families.

K2034 owns the V/C split and common pointwise positive256 inside C; K2236
owns the minimum pointwise dynamic refinement, one-axis Jordan growth and
original mass formula. K2239 owns graph-pullback refinement. The August11
[polarization result](selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md)
already owns ker(symbol-square) and its onto observation rank640; neither the
constraint nor that rank is rediscovered here. The earlier
[provenance result](bet-2plus1-provenance-observation-2026-11-11.md) owns minimum
static separators and their principal mixing. We now compute actual time
measurements and the explicit constrained observed dynamics, including the
original mass term, on these held objects.

## 1. Original symbols and actual measurements

Let C_j=gamma0 gamma_j for observed j=7,8,9, now numbered1,2,3. They are
Hermitian involutions with {C_j,C_k}=2delta_jk. Fourier convention is
partial_j -> i p_j. Put C(p)=sum p_j C_j and rho=|p|².
The quotient evolution is

`partial_t u + i A(p)u + m D u=0`,
`A(p)=sum p_j T_j tensor C_j`,
`D=diag(-Z,Z,Z,Z,Z,H)`, `Z=gamma0 J`, `H=Z Wbar²/2`.

Z*=-Z, Z²=-I, {Z,C_j}=0, [J,C_j]=0. Mass m is real and constant;
m=0 suffices for the history and growth statements below. T_j are derived
from original15-slot M0^-1 Mj, not fitted to a desired output.
Let E_q insert q with v=0; B=Q A E_q, D_q=diag(-Z,Z,Z,Z,H).
Then the measurable residual satisfies

`r=-partial_t q-iBq-mD_q q=iF(p)v`,
`F_a=0`, `F_bj=10p_j C_j-(5/6)C(p)`, `F_h=10C(p)`.

This uses the actual derivative of q. K2236's algebraic QD0 response is a
different instrument and is not substituted for a time measurement.

## 2. Exact inverse, range and conditioning

With the stated equal Euclidean weighting of residual channels,

`F*F=(2225/12) rho I`.

Indeed sum_j F_bj*F_bj has coefficient
100-50/3+25/12=1025/12, while F_h*F_h contributes100.
Thus for p!=0

`v=-i F*r / ((2225/12)rho)`.

The residual must satisfy the exact consistency condition
`Pi_F r=r`, where `Pi_F=FF*/((2225/12)rho)` is an orthogonal projector.
This is a left inverse on realizable data and a least-squares inverse on
noisy residuals. Its operator norm is exactly
`sqrt(12/2225)/|p|`. Scalar h-derivative recovery alone uses
`v=-i C(p)r_h/(10rho)`; it is sufficient but has a larger residual-noise gain
under this channel norm. This comparison fixes residual noise, not the noise
of q and its numerical differentiation. No physical detector metric is supplied.

For p!=0 the first jet identifies all of C; the complete raw history kernel
is exactly V. At p=0 every time jet misses vS as well as V: A(0)=0 and D is
slot diagonal, so hidden v remains hidden for any constant mass m. A torus
therefore has a genuine invisible homogeneous component. On R3 an L2 field
supported only at p=0 vanishes, giving injectivity modulo V almost everywhere,
but no bounded inverse in equal-order inhomogeneous Sobolev norms.

An explicit countersequence is v_epsilon(x)=epsilon^(3/2)phi(epsilon x)
for a fixed nonzero Schwartz spinor phi. Its L2 norm is fixed while
||F(D)v_epsilon||_2=epsilon sqrt(2225/12)||grad phi||_2.
A gap |p|>=kappa makes the residual inverse bounded by
sqrt(12/2225)/kappa. Equivalently the full residual controls the homogeneous
one-derivative seminorm exactly; it does not control the homogeneous mode.

For fixed |t|<=T in the massless model, A(p)=O(|p|), Qe_v=0, and
`Q exp(-itA(p)) e_v=O_T(|p|)` uniformly near0, by the convergent exponential
series. Pure hidden data localized in an epsilon Fourier ball therefore have
bounded initial norm but full finite-time observed history O_T(epsilon).
Waiting over a fixed finite window does not repair infrared conditioning.
This claim uses full spatial observation, not a point receiver or partial aperture.

## 3. Released dynamical consumer: what recovered output retains

The inherited defect has the exact universal identity

`N(p)=A(p)^2-rho I`, `N(p)^2=0`,
`N(p)[a,v]=(55/6)rho I`.

The companion note supplies its complete factorization. This is the
unchanged Jordan structure already present in the raw model, now checked
for every nonzero observed momentum. Set r0=|p| and
`S=A/r0 (I-N/(2rho))`. Then S²=I and

`exp(-itA)=(cos(r0 t)I-i sin(r0 t)S)(I-it S N/(2r0))`.

All normalized matrices are continuous on the direction sphere. The first
factor and inverse have uniform bounds; the displayed nonzero N block gives
a uniform nonzero witness for the second. Hence the full3D massless propagator
is bounded H^s -> H^(s-1), and unbounded H^s -> H^s at every t!=0. This extends
the held one-axis consumer; it does not assert a massive or variable-coefficient
propagator estimate. Localizing Fourier data in small cones gives ordinary
R3 countersequences; torus modes give the corresponding discrete example.

In the massless model, every Fourier output O(p) retaining q and admitting closed first-order time
evolution on the whole C space must be injective: ker O is A-invariant and
inside ker Q=vS, but Q A e_v=F(p) is injective at p!=0. Its induced generator
on im O is therefore similar to A. Derivative-valued or nonlocal coordinates
cannot supply a positive-definite time-independent conserved Fourier energy
on this full output: such an energy would make A similar to a Hermitian
matrix, contradicting the nonzero square-zero defect. An arbitrary unbounded
coordinate map can change Sobolev norms, so the previous norm estimate is not
transported by similarity alone. Time-dependent metrics and restrictions on
initial data are different premises; the companion note executes the latter.

## Evidence and ceiling

Universal arguments are written above; polynomial Clifford identities are
checked exactly, with genuine coefficient faults. No finite pass count proves
a continuum theorem. No guessed action, physical observation device, gauge
quotient, chirality or family count is supplied. Time reconstruction determines
algebraic provenance of the current state, not conservation of its labels.

[Exact probe](../../tests/program-focus/bet_2plus1_observation_jets_probe.py) ·
[Evidence](../../lab/process/bet-2plus1-observation-jets.json) ·
[Constrained evolution](bet-2plus1-polarized-observed-evolution-2026-11-11.md).
