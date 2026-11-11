---
title: The native K95 projector stabilizer retains an odd-arrow freedom
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: X-P1-P2
tier: T2
expected_delta: Determine the real-form and same-square transfer requirements for
  the actual quaternionic diagram.
actual_delta: 'Constrained: the actual K95 quaternionic gauge group has a one-parameter
  projector-preserving family that changes the Clifford plane and named Gamma/j arrows.
  Inert-vector and reflected-vector coflip square constraints differ; no full-C weld
  or action witness follows.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The native K95 projector stabilizer retains an odd-arrow freedom

Constrained: the actual K95 quaternionic gauge group has a one-parameter projector-preserving family that changes the Clifford plane and named Gamma/j arrows. Inert-vector and reflected-vector coflip square constraints differ; no full-C weld or action witness follows.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Determine the real-form and same-square transfer requirements for the actual quaternionic diagram.
actual_delta: Constrained: the actual K95 quaternionic gauge group has a one-parameter projector-preserving family that changes the Clifford plane and named Gamma/j arrows. Inert-vector and reflected-vector coflip square constraints differ; no full-C weld or action witness follows.

```gu-typed-objects
result: native real-form projector-to-diagram transfer
carrier: full complex128 Dirac module of real Cl(9,5), quaternionic dimension64, and real V tensor S LAYER=UNTYPED CHIRALITY=N/A
pairing: K=gamma0...gamma8 Hermitian signature64plus64; quaternionic signature32plus32 ON=declared_carrier
real_structure: J=B conjugation, J squared=-I and J gamma_i=gamma_i J
grading: volume Omega eigenspaces; not an observed physical chirality quotient
action_owner: repository-construction -- algebraic structural subclass, no action chosen
target: gamma-trace kernel, projector and named-arrow compatibility MAP-TYPE=intertwiner
```
## 1. What is reused and what is tested

[K1826](k1826-k77-graph-preserving-internal-coefficients-2026-10-20.md)
already owns the even-Clifford commutant method for graph preservation.
[RB3](../rb3-moving-soldering-spinzero-placement-2026-07-30.md)
already supplies the actual complex128 quaternionic K95 fixture and moving
Clifford-plane geometry. Neither is rediscovered here. The new consumer is
[X-P1-P2's diagram condition](x-p1-p2-moving-gauge-naturality-2026-11-11.md):
does preserving the actual real structure, pairing, chirality and RS projector
already preserve the named odd arrows? The answer is no, with an exact native
family. Its same-square coflip consequence depends on the specified vector
map; that fork is executed below.

The [source section9 extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
keeps zero-form and one-form spinors separate. Independent bars are not silently
identified with Hermitian adjoints. The chosen K and J are RB3's declared
algebraic fixture, not a proof that a source action owns them. SC-GEN-02/03/54
retain ASSERTS with their stated 2+1/extension and label scope; SC-CHI-01/51
retain ASSERTS for nonchiral total versus effective chiral splitting. No
ordinary index or this volume grading establishes the observed count.

## 2. Complete fixed-vector stabilizer in the actual real form

Let real V have signature(9,5), dimension14. On the full complex Dirac module
S use gamma_i gamma_j+gamma_j gamma_i=2 eta_i delta_ij. The exact RB3 basis has

K=gamma0...gamma8,
J=(gamma1 gamma3 gamma5 gamma7 gamma10 gamma12) conjugation,
Omega=gamma0...gamma13, P_+=(I+Omega)/2, P_-=(I-Omega)/2.

All gammas are K-selfadjoint. K is a Hermitian involution of complex
signature(64,64); J is antiunitary for the underlying standard Hermitian norm,
J²=-I and J gamma_i=gamma_i J. Omega²=I, Omega†=Omega,
Omega†K=-K Omega and J Omega=Omega J. Thus K pairs the two isotropic volume
summands nondegenerately; it is not positive on each summand.

Define Gamma:V tensor S→S by Gamma(v tensor s)=gamma(v)s and
j(s)=(1/14) sum_i eta_i e_i tensor gamma_i s. Then Gamma j=I and
P_R=I-j Gamma. Let G be the quaternionic K-unitary group, realized as
complex-linear invertible g with gJ=Jg and g†Kg=K. This is the fixture's
Sp(32,32;H), not a group assignment to the separate K77 horn.

**Theorem.** For fixed V action and identical g on every one-form slot,

(I tensor g)ker Gamma=ker Gamma
iff g=aP_+ +a^{-1}P_-, a in R nonzero.

Proof. Gamma is surjective. Kernel preservation gives a unique invertible h
with Gamma(I tensor g)=h Gamma, hence gamma_i g=h gamma_i. Comparing i,j
forces commutation with every gamma_i^{-1}gamma_j and therefore with the
full even Clifford algebra. Over C its commutant on full irreducible Dirac S
is C P_+ plus C P_-: the two chiral irreducible modules are inequivalent.
This standard Clifford-module fact is also the algebraic step reused in
K1826; see [Deligne, Notes on Spinors, Clifford modules](https://publications.ias.edu/sites/default/files/79_NotesOnSpinors.pdf).
Since J preserves the two summands and is antilinear, gJ=Jg forces both
coefficients real. Write them a,b. Pairing invariance, using only cross
pairings between the summands, forces ab=1. Conversely every such g satisfies
all equations, with h=bP_+ +aP_-=g^{-1}. This proves both directions.

Requiring the **same g on the target spinor**, rather than an independently
chosen quotient action h, imposes g=h, thus a=+1 or -1 and g=±I. The same
condition holds for the inclusion arrow j. Kernel preservation alone
therefore cannot supply the named-diagram premise of the fixed-arrow weld.
This is an exact structural subgroup classification, not a class-C exclusion.

## 3. Released native motion: unchanged projector, changed plane

Choose a=2, so g=(5I+3Omega)/4 and g^{-1}=(5I-3Omega)/4. These are exact
rational matrices in G. They preserve J, K and Omega, and

g gamma(v)g^{-1}=(17 gamma(v)+15 Omega gamma(v))/8.

The second term has Clifford grade13. Since the full complex Clifford
representation is faithful and grades1 and13 are independent, it lies outside
the original vector plane for every nonzero v. This is stronger than an
abstract covariance example: the very same native G element fixes the RS
projector while moving the plane.

Transporting all gammas gives
Gamma_g=g² Gamma, j_g=j g^{-2}, hence j_g Gamma_g=j Gamma and P_R(g)=P_R.
All196 gamma-product blocks of the projector numerator are unchanged.
The family a=e^t gives Gamma_t=e^{2t Omega}Gamma and j_t=j e^{-2t Omega}.
The disconnected a<0 component differs by an overall sign; the full
stabilizer theorem includes it.

This does not contradict RB3's Clifford-plane stabilizer. With vector slots frozen, the plane and projector stabilizers are
incomparable. The native Spin rotor gamma0 gamma1 preserves the plane but
changes the projector block gamma0 gamma2 by a sign; its usual geometric
covariance also rotates the vector frame. Our hyperbolic g demonstrates
the reverse implication failure: fixed projector does not imply fixed plane. Restoring
covariance by moving the arrows is valid; treating a moving diagram as the
same frozen diagram is the failed inference. No connection, field equation,
operator support stratum or variational pairing has been selected.

## 4. Released same-square test: two distinct vector maps

An antilinear map must retain its vector action. On real V the following are
unambiguous; on V_C tensor S include conjugation on vector coefficients.

**Inert vector map.** The natural J preserves the kernel and named diagram.
For the classified g, Jg=gJ and (gJ)²=-g². Requiring the same square -I forces
a²=1 and g=±I. Thus the kernel-preserving hyperbolic ratio does not survive
this specified same-square demand.

**Reflected vector map.** Put C0=gamma0 J and let R=diag(1,-1,...,-1) on V.
Then C0²=-I and C0 is K-antiunitary, meaning
(C0u)†K(C0v)=conjugate(u†Kv), with no extra negative sign. For any classified
g let C1=C0 g. Since gamma0 Omega=-Omega gamma0,
C0 g C0^{-1}=g^{-1}; consequently C1²=-I too. Both preserve K antiunitarily.
But their arrows obey

Gamma(R tensor C0)=C0 Gamma,
Gamma(R tensor C1)=C0 g^{-1} Gamma.

Both preserve the kernel with this reflected vector action. The second
quotient action is not C1=C0g unless a²=1. Hence the same square and pairing
still do not imply the same target-arrow equation for a specified reflected
coflip. Dropping R would be wrong: C0 alone with inert V does not preserve
the kernel. Write C0=B0 conjugation. The matrix of any antilinear quotient map
would have to equal H_i=eta_i gamma_i B0 conjugate(gamma_i). The i=0
and i=1 equations give B0 and -B0 respectively, so no common quotient
map exists. The probe checks this stronger kernel test explicitly.

These are constructed coflip controls, not source-selected operators. The
inhomogeneous connection translation has not been assigned a spinor action;
previous native BV work distinguishes its physical tangent from the tilted
gauge image. Nor is a real/global Spin lift or full operator symmetry proved.

## 5. Effect, falsifiers and validation

X-P1-P2 gains an actual real-form transfer test and P2xsymmetry a structural
constraint: projector-level covariance cannot replace odd-arrow data.
An alleged fixed-vector exception in G must violate the complete even
commutant, J or pairing calculation; a reflected-coflip claim must retain R
and its distinct target action. No source/ledger/class-C/canon change follows.

[Probe](../../tests/program-focus/x_p1_p2_real_clifford_transfer_probe.py)
and [report](../../lab/process/x-p1-p2-real-clifford-transfer.json) check the
actual128-complex fixture, all Clifford relations and all projector numerator
blocks. All arithmetic is exact Gaussian dyadic arithmetic in binary64 at
small magnitude, with exact equality and no tolerance; the universal theorem
is the written proof, not a matrix sample or Lean certification. Independent specialist and hostile review completed; the quotient-map probe and
frozen-frame stabilizer comparison were repaired before acceptance.
