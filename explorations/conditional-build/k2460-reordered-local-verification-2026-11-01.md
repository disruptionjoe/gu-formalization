---
title: "K2460 Changing the last measured register improves local verification"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "INTERNAL_TARGET: the convex hull of these five fixed local effects attains gap1/2"
claim_ceiling: "rigorous complete-carrier gap at least9/20 for two supplied programs; no all-local optimum or measured hardware advantage"
---

# K2460 Changing the last measured register improves local verification

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
result: K2460
carrier: original ten-string coherent programs on F tensor R tensor B tensor E of total dimension108 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and complete effect order ON=declared_carrier
real_structure: complex Fourier phases and original positive real amplitudes
grading: three-valued flag, two qubits, nine-valued environment and target-stabilizer characters
action_owner: repository-construction -- supplied conditional programs
target: four-register local changed-last-register verifier MAP-TYPE=evaluation
```

## Result

The original K2454 programs admit a four-register local verifier with
rigorously certified gap at least9/20. It combines E-last, B-last and R-last
conditional tests, after the existing finite local phase average. This
improves K2457's2/5 bound by leaving its restricted single-test family.
It does not contradict K2457's half-gap obstruction for that family, nor
prove that1/2 is attainable or impossible for arbitrary local protocols.

The proof uses all108 coordinates, including all four off-support companions
in the14-dimensional invariant block. Every one of31 blocks for both
original laws has a rigorous positive interval LDL certificate. Numerical
search only suggested the rational mixing weights; it does not certify them.
SC-META-53 remains UNCERTAIN; LT-SM8, ledger0.263 and canon unchanged.
No novelty, measured cost or native GU quantum-state identification is claimed.

## 1. Same target, different local measurements

Use exactly K2454's ordered strings x_i=(f_i,r_i,b_i,e_i), weights mu_i,
and its native-axis rotation. Psi=sum_i sqrt(mu_i)|x_i>; Q projects onto
its ten computational strings. The logical rotation is a trusted local
basis change, not free apparatus calibration.

The existing E-last test measures F in the3-point Fourier basis and R,B
in their X bases, then E in the normalized conditional target direction.
For the new B-last test measure F,R,E in their3-point Fourier, X and9-point
Fourier bases. With omega=exp(2pi i/3), zeta=exp(2pi i/9), let

    a_ksl(f,r,e)=omega^(kf)*(-1)^(sr)*zeta^(le)/sqrt54,
    c_ksl(b)=sum_(i:b_i=b) sqrt(mu_i)*conj(a_ksl(f_i,r_i,e_i)),
    p_ksl=sum_b |c_ksl(b)|^2,
    v_ksl(f,r,b,e)=a_ksl(f,r,e)*c_ksl(b)/sqrt(p_ksl).      (1)

Here k=0,1,2; s=0,1; l=0,...,8. Conditional B projection onto
c/sqrt(p) gives effect T_B=sum v v*. If p=0, reject that outcome.
For both original laws all54 probabilities are certified strictly positive.
Interchange R and B in (1) to define the R-last projection T_R.
The E-last projection T_E has12 outcomes.

The measured-register product basis is orthonormal, so the normalized full
columns are orthonormal even though the final conditional states vary.
Thus each T is a projection. Expansion of Psi in the measured basis gives
Psi=sum a tensor c and directly proves T Psi=Psi. This analytical argument,
not an interval residual containing zero, establishes exact completeness.
All operations are local to a single register with classical feedforward.
Measuring E early here is valid because the subsequent test is reconstructed
for that order. It is not E dephasing followed by the old E-last test,
and does not upgrade a measured resource for later use. Test rounds are consumed.

## 2. Finite local phase average and full-carrier inequality

Apply K2457's135 target-preserving local diagonal products to each T.
Their character on a computational coordinate is

    chi(f,r,b,e)=(unit_f-unit_f_e, r-b-r_e+b_e).

Its mod3,mod5 character labels have no aliases on this carrier; averaging
retains exactly equal-character entries. Every support string has character
zero. The proof of locality, target invariance and the no-alias bound in
K2457 is reused unchanged. Define

    Omega=Q/8+Tbar_E/2+Tbar_B/4+Tbar_R/8.                (2)

This is a perfectly complete local test, with private branch/phase choices.
The weights are rational and do not depend on a tested record.
The probe reconstructs the original conditional columns using Arb/acb at
256-bit precision. All roots, phases, normalizations and matrix products
are interval-enclosed. On every complete character block it forms

    H=(11/20)I+P_Psi-Omega

and proves positive definiteness by Hermitian LDL elimination with every
pivot interval strictly positive. Taking the real part of a diagonal
preserves a rigorous enclosure because the exact matrix is Hermitian;
no numerical center or rounded eigenvalue is used as a pivot bound.
The smallest certified pivot for each block is recorded in the report.

Since Omega Psi=Psi and Omega is Hermitian, Psi-perp is invariant. H>0
on that subspace implies Omega<11I/20 there, so

    Omega <= P_Psi+(11/20)(I-P_Psi).                    (3)

The conservative certified gap is9/20. The target direction of H has
positive eigenvalue11/20, avoiding a singular interval factorization.
Four invariant companion coordinates are retained. Wrong Fourier
conjugation and omitted feedforward fail on the original target;
an inflated3/4-gap assertion fails the actual block factorization.
These controls are distinct from the analytic proof and full-carrier certificate.

## 3. Released obstruction: retuning all Fourier last-register choices cannot reach half gap

The improved family itself has a certified limit. In the zero-character
block, take each original law's explicit fourteen-integer vector u recorded
in the report and form w=u-P_Psi*u. This lies exactly in Psi-perp by the
normalized target identity, not by numerical subtraction tolerance. Also construct T_F by measuring R,B,E in product Fourier bases,
then projecting F onto its target-conditional direction; all36 conditional
probabilities are positive on each original law. This fifth candidate is
a tested alternative, not a component of (2). All
five actual effects satisfy, by rigorous interval evaluation,

    <w,Qw>, <w,Tbar_E w>, <w,Tbar_B w>, <w,Tbar_R w>, <w,Tbar_F w>
                        > (13/25)*<w,w> > 0.            (4)

Every convex mixture of these five fixed effects therefore has a
non-target Rayleigh quotient above13/25. Its gap is strictly below12/25,
and in particular cannot reach1/2. This excludes retuning weights in this
specific five-effect hull. It proves neither their optimal mixture nor an
upper bound for all local protocols, changed bases or further tests.
The witness seeds were found numerically and rounded to integers; (4)
uses only their explicit integers, interval-enclosed original effects and
an analytic target-orthogonal projection. No optimizer or approximate
spectral value carries the conclusion. The obstruction releases the next
design question: a half-gap improvement needs an effect outside this hull.

## 4. Released statistical consumer and operational cost

Compose gap9/20 with K2459, retaining K2456's existing independent budget
B=10^-6 and pi=eta=1/2, alpha=.05, calibration beta_bar=10^-8,
completed-operation error kappa=10^-6, ideal heralding qherald=1/4,
C_out=2, output target tau=.01. The report gives384,822 as the sufficient integer
actual-use count and checks its preceding integer fails that declared bound.
The positive actual-success sufficient condition is checked separately.
This is a hypothetical design calculation; no device data or successful
experiment is asserted. The original K2450 and K2456 certificates remain
valid under their respective assumptions.

The branch costs are now explicit: Q has computational support readout;
T_E needs12 conditional coherent E projections; T_B and T_R each require
54 conditional qubit projections and a coherent nine-level Fourier E
measurement, plus the135 phase labels when twirled. The average does not
mean135 simultaneous tests, and a larger gap does not by itself mean less
hardware time, error or total cost. Native-axis rotation, calibration,
coherent custody, storage and test/use separation must be justified.

The remaining useful design question compares a genuinely simpler calibrated
protocol with this larger proved gap. A half-gap design requires an effect outside the proved five-effect hull.
A full local optimality theorem remains open; numerical search supplies none.
Independent internal review is not external-expert or proof-assistant acceptance.

[Probe](../../tests/channel-swings/k2460_reordered_local_verification_probe.py) and [report](../../lab/process/k2460-reordered-local-verification.json).
