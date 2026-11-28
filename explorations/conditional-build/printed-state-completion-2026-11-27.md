---
title: Resonant printed interactions obstruct regular slaving of the hidden response
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T1
expected_delta: Decide whether an off-band auxiliary response repairs the previously excluded strict cutoff, and identify the exact nonlinear completion class
actual_delta: The actual mixed force has a nonzero massive left-cokernel receiver at resonance; regular equivariant quadratic slaving fails, while nonresonant and secular forced responses survive
class_covered: Selected frozen zero-source low-Phi printed equation in primary-minus K95; C2 translation-equivariant solution graphs or declared state graphs admitting the tested trace modes and excluding an independent resonant hook state
premises:
- The actual selected printed P and Q, not reconstructed W2 dynamics, are used
- Fourier characters or a pointwise smooth quadratic Fourier kernel are admitted
- The graph has a finite mixed coefficient and satisfies the stated invariance equation
- No physical state-domain or source-unique completion bridge is assumed
source_bridge:
  status: conditional
  reason: Source supplies a printed endpoint and full primitive translations but does not require this frozen state space, selected completion, or smooth slaving rule
kill_condition: A failed left-null identity or zero actual forcing receiver invalidates the graph exclusion; a surviving forced response is retained and is not a physical instability claim
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Resonant printed interactions and state completion

program_target: X-P1-P2
tier: T1
expected_delta: Test off-band auxiliary completion beyond the strict cutoff.
actual_delta: A true resonant obstruction to regular quadratic slaving, with nonresonant and secular response controls.

**ESTABLISHED:** the two previously tested oscillatory modes generate a
resonant forcing that cannot be represented by a stationary, same-frequency
auxiliary field. More generally it obstructs the regular, equivariant
quadratic graphs specified below. The obstruction persists at every
nonzero coupling by scaling.

**It does not make the equations insoluble.** A nonresonant pair has an
exact bounded-in-time response. The resonant pair has a polynomial-in-time
response, and its forced coefficient necessarily has a secular linear
functional. This constrains elimination of a hidden degree of freedom;
it is not a physical ghost or source-GU falsification.

```gu-typed-objects
result: Printed nonlinear state completion
carrier: T*Y tensor End_C(S128), with primary-minus real Fourier quadratures LAYER=ambient BRIDGE=held-printed-product-dictionary-conditional CHIRALITY=N/A
pairing: original indefinite spin pairing H; algebraic left-null functional, not a positive norm ON=End_C(S128)
real_structure: normalized frozen K95, gamma-sharp=-gamma; real grade1/2 fields, complex Fourier coefficients paired by conjugation
grading: Clifford degree and trace/hook symbol channels, not physical chirality
action_owner: source-print -- selected P,Q frozen comparison, distinct from I1B Euler and W2
target: massive left-cokernel versus actual polarized quadratic forcing MAP-TYPE=intertwiner
```

## 1. Source custody, prior results and prior art

The [previous nonlinear transfer](printed-nonlinear-transfer-2026-11-27.md)
excluded a strict all-field stable-frequency cutoff admitting the tested
pair. It expressly retained forced fields outside that cutoff. The present
calculation tests that escape; it does not repeat support leakage.

We use `Lκ=κ+P(∂)` and `Q(T,U)=Phi(T∧U+U∧T)/2` on the **zero-source,
constant-coefficient comparison equation**. The native metric-bundle
curvature source and curved lower-order terms are not asserted to vanish.
The owned [full symbol](printed-equation-jets-and-symbol-2026-11-27.md)
and [two-sided scalarizer](printed-differential-solvability-2026-11-27.md)
are reused.

[Source prescription](source-prescription-current-2026-11-13.md) §§1–2
binds full fixed-g translations to draft §§5–7, eqs6.22/7.3 and p45eq9.7.
SC-ACT-02 concerns p45eqs9.8–9.10; SC-ACT-01 and SC-ACT-04 are distinct
variational objects. SC-ACT-06, p65 itemx, concerns a reduced Euclidean
complex, not the state graph tested here. SC-META-52 (TOE01:17:10,
transcript338) and SC-META-53 (01:22:30, transcript366) leave boundary and
indefinite-spectrum mechanisms uncertain. Primitive variation freedom is
not physical state admission.

The normal-form method is established prior art. The parameterization
method treats both the embedding and reduced dynamics, with external
nonresonance conditions; see [Cabré–Fontich–de la Llave, Part I](https://web.mat.upc.edu/xavier.cabre/docs/indi1jour.pdf).
[Haller–Ponsioen](https://arxiv.org/abs/1602.00560) develops spectral
submanifold reductions under its own spectral/dissipative hypotheses.
We import neither theorem's hypotheses into this descriptor PDE. The
necessary quadratic equation below is derived directly. Existing repo
K1435/36 and K1442/43 already use related divisors for a different
scalar-electrodynamics construction. No novelty claim is made.

## 2. The actual resonant force and a left-null certificate

Use orthonormal K95 with `τ²=η²=−1`, `σ²=+1`, pairwise orthogonal;
τ is base time, η is normal, σ is ordinary spatial. At κ12 let

`ξ+=2τ+4σ+3η`, `ξ−=−2τ−4σ+3η`.

Both have `ξ²=3` and real time frequencies±2. Their authenticated trace
polarizations are `v(iξ)=12O(iξ)+2c(iξ)O(iξ)`, with
`O(ζ)=Phi1−ζ⊗c(ζ)/ζ²`. Real fields use these amplitudes together with
the conjugate-frequency coefficients. Each is oscillatory in this trace
channel; no claim of simultaneous stability across all19 symbol channels
is made.

The summed frequency is `K=6η`, with total time frequency zero. Therefore
`q(iK)=36`. The full symbol squares are `4a q`, where
`a∈{1,12,22,30,36,40,42}∪{−1,…,−12}`. The massive operator
`L0=12+P(iK)` resonates in the `a=1` hook channel. Resonance alone would
not suffice: the actual force must pair nontrivially with a **left** null
functional.

Let `Y_(a,C)` denote the coefficient at form leg a and Clifford blade C.
In coordinates τ=θ0, σ=θ1, η=θ10 define

`ell(Y)=Y_(0,1)−Y_(1,0)−iY_(0,1·10)+iY_(1,0·10)`.

Exact native Clifford algebra gives

`ell L0=0`,
`F=Phi(v+∧v−+v−∧v+)`, `ell F=104448`.

For a direct two-channel derivation, let
`beta=theta0 gamma1−theta1 gamma0` and `Gamma=−6i gamma10`.
The transverse symmetric off-diagonal hook coordinates are
`a=(Y_(0,1)−Y_(1,0))/2` and
`b=(Y_(0,1·10)−Y_(1,0·10))/(12i)`.
The owned hook formula gives the massive block
`(a,b) -> (12a−72b, −2a+12b)`; `ell=2a+12b` annihilates it.
The actual force has `a=52224,b=0`. The invariant hook decomposition
and the exhaustive receiver-column check authenticate this row on the
full carrier, not just on the displayed two-channel input.

All26 input columns capable of reaching these four receivers by Clifford
XOR are checked; the other columns are identically absent. The written
hook decomposition independently gives the same left-null row. Thus
`L0 W=−F` has no solution in the full complexified carrier, even allowing
arbitrary off-band values of W. This is not a restricted ansatz rank test.
Realification retains this nonzero mixed coefficient: only the two ordered
input pairs reach the summed frequency.

Scaling κ and all frequencies by `s=κ/12` scales each polarization by s
and F by s²; the left-null functional is unchanged. Consequently

`ell Fκ=(2176/3)κ² ≠0` for every real κ≠0.

The tested interaction cannot avoid the resonance merely by changing the
nonzero scalar coupling. K77 and the curved native operator require their
own transfer; this theorem is explicitly K95 frozen.

## 3. Which nonlinear graphs are excluded?

### Equivariant solution graph

Suppose a real C² parameterization of solutions is tangent to these two
linear Fourier directions. Require translation equivariance under the
linear character action on the modal parameters, including time translations,
and a finite
mixed quadratic coefficient at their sum, and a space in which these
characters and coefficient evaluation are defined. Differentiating the
printed equation twice forces

`L0 H12=−F`.

The certified receiver contradicts this equation. Allowing H12 arbitrary
Clifford components or off-band frequencies does not repair the failure
at the required sum coefficient.

This includes analytic/periodic/almost-periodic character-admitting
categories and a quadratic Fourier multiplier whose kernel is pointwise
smooth at this pair. **A C² map on an R13 Sobolev space alone does not
imply such a smooth multiplier kernel.** Singular distributional kernels,
wave-packet estimates and nonlocal history maps need a separate analysis.
No measure-zero Fourier argument is promoted to an all-Sobolev no-go.

### State graph allowing nonlinear reduced dynamics

The conclusion need not assume that reduced dynamics stays linear. Let
`A_t=P(τ)` and write the descriptor equation

`A_t ∂tT+L_sp T+Q(T,T)=0`.

A proposed instantaneous state graph has
`Ψ(a)=Ja+H(a,a)/2+…`, with reduced vector field
`g(a)=A_c a+g2(a,a)/2+…`. Its invariance equation is

`A_t DΨ(a)g(a)+L_sp Ψ(a)+Q(Ψ(a),Ψ(a))=0`.

Let its base contain the tested stable trace directions and have no base
state at the excluded spatial sum `6η`. Spatial translation covariance
then makes `g2(a+,a−)=0` at that frequency. The quadratic normal equation
again reduces to `L0H12=−F`. Nonlinear base dynamics cannot cancel this
**external** resonance. An enlarged base already containing the resonant
hook state is outside this exclusion.

This is a necessary obstruction conditional on the displayed descriptor
invariance equation and mode-admitting state realization. It does not
construct a physical state space or assume that the singular descriptor
has a globally well-posed evolution generator.

## 4. Nonresonant and resonant responses: controls and survivors

### A nonresonant auxiliary response exists

Choose `ξ±=±9τ±10σ+4η`, still at κ12 and `ξ²=3`. The sum is `8η`,
so `q(iK)=64`. Resonance would require `a=9/16`, absent from the complete
symbol list. The zero-symbol Jordan blocks are also invertible after
adding κ. Thus the **full** massive operator is invertible.

The probe constructs `W=−L(i8η)^{-1}F` exactly and verifies the full
native residual. This stationary spatial Fourier response is bounded in
time. An out-of-band source is therefore not automatically an instability.
A compatible forcing at the resonant frequency is also constructed and
solved, calibrating the left-null test against a genuine survivor.

### The slaving coefficient has a pole at the resonant pair

An analytic rational family connecting the two fixtures is

`ω(n)=(5n−11)/(5−n)`, `p(n)=(n²−5n+14)/(5−n)`,
`p²−ω²−n²=3`.

Let G(n) be the projection of its actual mixed force onto the hook
massive eigenvalue `12−4n`. For n≠3 near3, the unique response in that
channel is `G(n)/[4(n−3)]`. Its `θ0γ1` residue is6528 and its ell
residue is26112. These nonzero residues prevent a pointwise smooth
quadratic frequency-slaving kernel from crossing the resonance. This
is not, without a separate multiplier estimate, a theorem against every
singular nonlocal operator on a Sobolev space.

### A secular response exists at resonance

Write a response at spatial frequency K as W(t). Its exact forced
coefficient equation is

`A_t W'(t)+L0W(t)=−F`.

Applying ell gives

`d/dt ell(A_t W(t))=−104448`.

Hence every differentiable response has a linearly drifting functional;
none is uniformly bounded for all time in a finite-dimensional coefficient
norm. Homogeneous additions change only the integration constant in this
identity.

Nevertheless a response exists. The owned two-sided scalarizer satisfies
`Lκ Bκ=dκ(Box)`, with
`dκ(z)=κ²∏a(κ²−4az)`. At q36 its zero is simple. For physical-time
sign `sτ=−1`,

`u(t)=−t²F/[2sτ dκ'(36)]`

satisfies `dκ(Box)u=−F`, because
`Box(t²F)=36t²F+2sτF` and higher second-derivative corrections vanish.
Then `W=Bκu` is a degree-at-most-two polynomial in t satisfying the full
forced system. The probe verifies this directly with the actual Pτ and
P(iK), independently of merely trusting the scalar eliminant.

This is the order-two coefficient forced by the specified first-order
modes. The perturbation expansion need not be uniform for arbitrarily
long time. **No finite-amplitude nonlinear instability, negative energy,
runaway exchange or physical-GU conclusion follows.**

### Benign-resonance calibration

The smooth system `x'=−ωy`, `y'=ωx`, `z'=x²+y²` has the exact solution
`x=r cos(ωt)`, `y=r sin(ωt)`, `z=z0+r²t`. It is well-posed, yet the
zero-frequency z response cannot be replaced by a stationary quadratic
function on the full oscillator orbit. This control prevents equating a
slaving obstruction or secular term with ill-posedness. The printed
calculation has its own authenticated vertex and left-null row; the
control does not supply a physical prescription.

## 5. What moved and what remains open

- **ESTABLISHED:** a genuine external quadratic resonance for the selected
  printed interaction at every nonzero κ; a regular slaving obstruction;
  a nonresonant auxiliary survivor; and a resonant secular response with
  an exact drifting functional.
- **RULED OUT:** the specified regular equivariant solution graph and
  instantaneous state graph retaining the pair while eliminating the
  independent resonant state; a bounded all-time quadratic response to
  this resonant coefficient forcing.
- **NOT MODELED / UNDETERMINED:** actual source physical admission,
  quotients or constraints removing the receiver; an enlarged dynamic
  state; singular/history-dependent completion; full nonlinear stability;
  and transfer to the native curved branch.

The forced resonant state may be retained dynamically, or an actual
source-supported restriction may exclude or identify it. Neither option
is adopted here. No new choice family is added and no source prediction
is credited. Choice budget stays10/4/net6/0.

This bears on the concrete memory/selection burden behind H2, but supplies
no records, relational commitment, observer-as-mind or metaphysical model.
H2 remains interpretation. H1/H3 receive no new bridge from this result.

[Exact probe](../../tests/program-focus/printed_state_completion_probe.py),
[certificate](../../lab/process/printed-state-completion-certificates.json),
[evidence and reviews](../../lab/process/printed-state-completion.json), and
[Lean finite cores](../../Lean/GUFormalization/PrintedStateCompletion.lean)
contain108 exact checks and four Lean finite cores. They separate algebraic
verification from the written graph/PDE proofs.
