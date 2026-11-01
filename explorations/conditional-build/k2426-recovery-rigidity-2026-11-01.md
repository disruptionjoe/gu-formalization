---
title: "K2426 Full-channel rigidity from the recovery gap"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional positive-Hilbert channel mathematics; no native GU or device verdict
scripts:
  - tests/channel-swings/k2426_recovery_rigidity_probe.py
---

# K2426 Full-channel rigidity from the recovery gap

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2426
carrier: physical flagged qubit instruments and full complex Choi matrices LAYER=toy CHIRALITY=N/A
pairing: half-diamond channel error and output-first unnormalized Choi trace ON=declared_instrument
real_structure: real planar Bloch data with complex Hermitian positive Choi matrices
grading: good/bad records; planar and perpendicular channel blocks
action_owner: repository-construction -- inherited recorded-instrument model
target: quantitative rigidity of every near-optimal recovery channel MAP-TYPE=evaluation
```

## Result

[K2424](k2424-recovery-saddle-reduction-2026-10-31.md)'s global error bracket
now constrains the **full recovery channels**, including complex Choi directions
and the original unsymmetrized branches. For the same asymmetric two-law
instruments, every globally optimal controller obeys

- each original bad-sign decoder, after the negative-sign alignment: half-diamond distance below2.240e-12 from the certified bad decoder;
- the original good decoder: half-diamond distance below1.202e-13 from the certified good unitary.

These are proximity bounds, not exact uniqueness claims. They use the existing
1e-27 objective gap without computing additional decimals. An actual uncertainty
of1e-8 in the complete flagged-instrument family gives a bad-branch bound
below0.010017 for an actual optimal controller under the assumptions below.
No measured apparatus uncertainty is supplied.

SC-META-53 remains UNCERTAIN. These are conditional positive-Hilbert channel
results; no native GU quotient, empirical calibration, implementation/Kraus
uniqueness, physics-ledger movement or novelty is asserted.

## 1. Full complex supported-channel rigidity

Use output-first unnormalized Choi J, Tr_out J=I2, Tr J=2. Suppose a physical
rank-two J0 and positive dual slack D satisfy

    DJ0=0, ker D=range J0=P, D >= gamma(I-P), gamma>0.

Let T:Herm(P)->Herm(C2) be partial trace, and let its smallest Hilbert-Schmidt
singular value be mu>0. If a CPTP J satisfies Tr(DJ)<=4 epsilon, then

    half-diamond(J,J0) <= (1+sqrt(2)/mu) sqrt(8 epsilon/gamma).    (1)

To prove it, set eta=Tr[(I-P)J]<=4epsilon/gamma and X=PJP. Gentle projection
of J/2 gives ||J-X||1<=2sqrt(2eta). TP implies
T(X-J0)=-Tr_out(J-X). Partial trace contracts trace norm on Hermitian
matrices, so ||X-J0||F<=||J-X||1/mu. Its rank is at most2, hence
||X-J0||1<=sqrt(2)||J-X||1/mu. Finally the diamond norm of a map is at most
the trace norm of its unnormalized Choi matrix. These inequalities give(1).
The Hermitian qualification is essential; arbitrary-matrix trace-norm
contraction is not used.

## 2. A small reproducible conditioning certificate

For rank-two J0 let p=(4-Tr J0^2)/2. Its exact support projection is

    P=(2J0-J0^2)/p.

For F_a=(I,X,Y,Z)/sqrt2, the4x4 real Hermitian Gram

    G_ab=Tr[(I tensor F_a)P(I tensor F_b)P]

is TT*. The Y direction tests imaginary supported perturbations. Positive
leading principal minors certify G>0, and AM-GM on the other three eigenvalues
provides

    mu^2 >= 27 det G/(Tr G)^3.

For rank-two positive D, its positive eigenvalue product divided by their sum
is a lower bound on the smaller eigenvalue:

    gamma >= ((Tr D)^2-Tr D^2)/(2 Tr D).

Physical canonical form and exact complementary slackness provide PSD and
rank upper bounds; interval positivity of the two products supplies rank
lower bounds. Merely enclosing zero in DJ0 would not prove exact rank.

A universal canonical check independently verifies these support formulas.
For planar singulars c,cd, perpendicular d and translation
 t=sqrt((1-c^2)(1-d^2)) along the cd direction,

    det G=t^4/(1-c^2 d^2)^4,
    Tr G=2+2t^2/(1-c^2 d^2)^2.

The probe verifies these identities by exact polynomial reduction. Nonzero
translation gives injectivity, with no real-only extremality shortcut.

For the K2424 radical candidate,256-bit Arb certifies the raw bounds
mu^2>0.0522307 and gamma_raw>0.1658905, with normalization R<1.006608.
Raw slack divides by R in the minimax dual. The report retains full enclosures.

## 3. From a value gap to original controllers

Let L be K2424's feasible dual value and U its common-controller upper bound.
For any nominal minimax controller with error<=U+e, the nonnegative support
gaps sum to at most4 epsilon, where epsilon=U-L+e<1e-27+e.

The reduced bad decoder is the average of J_+ and the output-Y-aligned J_-
with their complex conjugates. D is real. Its support gap is the average of
the two original gaps, each nonnegative. Each aligned original therefore has
Tr(DJ)<=8epsilon. Consequently(1) becomes

    half-diamond(original bad,J0)
      <= (1+sqrt(2)/mu) sqrt(16 R epsilon/gamma_raw).    (2)

Optimality-preserving averaging alone would not prove original-channel
rigidity; the separate nonnegative gaps and full complex conditioning do.
The reduced bad bound is1.584e-12; the valid original bound is2.240e-12.

Before good-channel replacement, the original supporting inequality retains
Tr(D_good J_good)+Tr(D_bad J_bad_average)<=4 R epsilon in raw normalization.
Both terms are nonnegative, and the functional survives both symmetrizations.
The original good channel has its own exposing functional. In the preferred
unitary frame, write r=||s||, h=sum p_i(1-w_i). Its slack has Bell eigenvalues

    0, r+h, 2r, r+h.

For any Hermitian J of trace2, the good functional equals
h(1-A_yy)+r(2-A_xx-A_zz) in the unitary-aligned frame. Exact Bell
diagonalization and all16 Hermitian basis directions verify this identity.
Here h>=r>0. Leakage from its rank-one maximally entangled Choi support is
eta_g<=4epsilon/(2r). Projection plus the supported trace change yields

    half-diamond(original good,U0)<=sqrt(2eta_g)+eta_g/2.       (3)

The implementation uses raw r and multiplies epsilon by R. This certifies
1.202e-13. These bounds concern physical channels; they never identify a
particular Kraus list, environment or hardware implementation.

If an exact optimal dual has these strictly positive gap and conditioning
properties, epsilon=0 forces channel uniqueness (after sign alignment).
The rational near-optimal dual used here proves proximity only.

## 4. A consumer with instrument uncertainty

Suppose the actual and nominal uncertainty sets of **complete flagged
instruments with the same flag interface** are within Hausdorff half-diamond
distance delta. CPTP postprocessing contracts this distance. Therefore their
minimax values differ by at most delta, and an actual e_actual-optimal
controller has nominal error at most U+2delta+e_actual.

Substitute epsilon=1e-27+2delta+e_actual in(2) and(3). For delta=1e-8 and
 e_actual=0, the actual optimal bad branches lie within0.010017 of the
candidate. This is a conditional illustrative budget, not an observed device.
A fixed candidate implemented with complete-channel allowance kappa attains
actual error<=U+delta+kappa and regret<=1e-27+2delta+kappa.

Independent moment errors do not supply this delta: cross-moment consistency,
flags, loss, domain and full-instrument composition must be justified together.

## Verification and limitations

[Probe](../../tests/channel-swings/k2426_recovery_rigidity_probe.py) and
[report](../../lab/process/k2426-recovery-rigidity.json) reconstruct the
original Choi and support slack, test all four complex-Hermitian directions,
certify conditioning and distance bounds, and replay the original K2424
global certificate separately from new checks.

The singular-conditioning control uses P=diag(1,0,0,1): distinct CPTP Choi
matrices supported there have zero leakage, and the partial-trace Gram is
singular. Leakage without injectivity cannot imply rigidity. The sign-factor
comparison is labeled a normalization control; the original-channel extension
rests on the nonnegative-gap proof. Independent internal review checks that
proof and its domain. No external-expert or proof-assistant certification.
