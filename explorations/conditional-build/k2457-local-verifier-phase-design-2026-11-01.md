---
title: "K2457 Local phase averaging improves the original coherent verifier"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "INTERNAL_TARGET: a single unbiased basis or a diagonal twirl of the existing conditional test attains a half gap"
claim_ceiling: "full 108-dimensional local verifier gap at least 2/5 and two restricted design limitations; no global local-protocol optimality or measured cost"
---

# K2457 Local phase averaging improves the original coherent verifier

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
result: K2457
carrier: the original ten-string coherent programs on F tensor R tensor B tensor E with dimension 108 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product, complete effect order and exact character-block spectra ON=declared_carrier
real_structure: complex local phases and original positive real amplitudes
grading: three-dimensional coherent flag, two qubits, nine-dimensional environment, stabilizer characters
action_owner: repository-construction -- supplied conditional mathematical programs
target: full local phase-averaged verification effect and exact restricted design obstructions MAP-TYPE=evaluation
```

## Result

A finite random choice of local diagonal phases, followed by the existing
K2454 conditional test, gives a verifier with certified gap at least 2/5 for
both original programs. It improves the prior gaps of about 0.26946 and 0.26342
while preserving single-register operations and classical feedforward.
It adds trusted coherent phase settings; it is not a claim of cheaper hardware.

Two tempting shortcuts fail at exact scope. Changing only one product basis
that is unbiased to the computational basis cannot improve K2454. Moreover,
any mixture of its support test with any target-preserving local diagonal
phase average of its existing conditional test cannot attain gap 1/2 for
these programs. Four invariant off-support companions are the obstruction.
Neither result limits every possible local protocol.

Pure-state verification with two bipartite settings is established
[Li et al.](https://arxiv.org/abs/2112.13638); that result alone does not
prove four-register locality or the present full-carrier bound. No novelty,
physical implementation, GU recovery or source-native identification is
claimed. SC-META-53 remains UNCERTAIN; LT-SM8, ledger 0.263 and canon unchanged.

## 1. Original object and finite local averaging

Use precisely K2454's ten strings x_i=(f,r,b,e), weights mu_i and native-axis
rotation. Put a=1-w, mu0=mu1=a/2; all eight bad weights are positive and sum
to w. Each bad environment label e=1,...,8 has one source triple
(f_e,r_e,b_e). Set (f_0,r_0,b_0)=(0,0,0). The target is
Psi=sum_i sqrt(mu_i)|x_i>, Q its ten-string support projection, and T the
rank 12 conditional test from the Fourier F and X-basis R/B measurements,
followed by the outcome-dependent E projection.

For alpha_f independently in 2pi Z3/3 and tau in 2pi Z5/5 define

    U_F|f>=exp(i alpha_f)|f>,
    U_R|r>=exp(i tau r)|r>, U_B|b>=exp(-i tau b)|b>,
    U_E|e>=exp(-i alpha_f_e-i tau(r_e-b_e))|e>.

Every one of these 135 products fixes every support string. In particular,
for e0 both good strings00 and11 have r-b=0. Thus U Psi=Psi and UQ=Q.
Apply the inverse phases before measuring T to obtain the effect U T U*.
Sample the phases privately and define

    Tbar=average_U U T U*, Omega=Q/4+3*Tbar/4.             (1)

The measurement remains local on each of four registers. Random phases
are additional classical settings; they may be absorbed into corresponding
local bases only with the correctly compensated E operation. The two logical
branches in (1) do not mean two elementary hardware settings.

A computational coordinate (f,r,b,e) has character

    chi=(unit_f-unit_f_e, r-b-r_e+b_e).

The three integer alpha charges lie in {-1,0,1}; their differences lie in
[-2,2], so averaging mod3 identifies precisely equal charges. Tau charges
lie in[-2,2], their differences in[-4,4], so mod5 likewise has no aliases.
Tbar therefore consists of exactly 31 nonempty character blocks on the full
108-dimensional carrier. There is no projection onto the target support.

## 2. Exact blocks reconstructed from the original conditional test

Within a character block define vectors V and W coordinatewise. For e>0,

    V_(f,r,b,e)=sqrt(mu_e),
    W_(f,r,b,e)=(-1)^(b+b_e)*sqrt(mu_e).

Here mu_e denotes the weight of the unique bad string with environment e.
For e=0 set V=sqrt(2a) and W=0. Then

    Tbar_chi=V V*/[2(1+a)]+W W*/[2w].                    (2)

To derive (2), split K2454's twelve conditional columns by R/B outcome
parity. Positive parity gives coefficient V/sqrt(12(1+a)); negative
parity gives W/sqrt(12w), apart from unit-modulus characters common within
each block. Six outcomes have each parity. The exact probe reconstructs
all block entries from the full original local measurement columns and
checks (2), so neither support restriction nor unproved phase cancellation
carries the numerical certificate.

The zero character has dimension 14: the ten original strings and four
companions obtained from the bad r_e=b_e strings by swapping00 and11 at
the same F and E. The original laws have total weight m=w/2 on those four
bad strings. Define u=(x0+x1)/sqrt2, v=sum_bad sqrt(mu_i/w)x_i,
z=sqrt(w)u-sqrt(a)v, and bcomp=sum_comp sqrt(mu_i/m) companion_i.
These last two are orthonormal and orthogonal to Psi. On their span Omega is

    [ (a+1/4)/(1+a),       3sqrt(a/2)/(4(1+a)) ]
    [ 3sqrt(a/2)/(4(1+a)), 3/(8(1+a))          ].         (3)

All other zero-character target-orthogonal eigenvalues are 0 or 1/4.
The largest eigenvalue of (3) is

    [8a+5+sqrt(64a^2+56a+1)]/[16(1+a)].

The slack 3I/5 minus (3) has positive diagonal and determinant

    3(21-64a)/[800(1+a)].                                (4)

The original a values 27/100 and 15/52 are both less than 21/64.
Thus this block is bounded by3I/5.

In every nonzero-character block Q=0. Put A=||V||^2, B=||W||^2,
C=<V,W>. These are rational for the original weights. The two possible
nonzero eigenvalues of Tbar_chi have trace

    t=A/[2(1+a)]+B/(2w)

and product d=(AB-C^2)/[4w(1+a)]. Because they are real and nonnegative,
t<=8/5 and16/25-(4/5)t+d>=0 put both at most4/5. Exact enumeration of all 30
nonzero blocks gives:

|a|max t|min characteristic slack at 4/5|
|---|---|---|
|27/100|3927/3302|1371/41275|
|15/52|761/670|33/670|

Multiplication by3/4 now bounds every such Omega block by3/5. Combined
with (3)--(4),

    Omega <= P_Psi+(3/5)(I-P_Psi).                       (5)

This is the full-carrier gap lower bound2/5. It is neither a numerical
spectral fit nor an assertion that the bound is the exact optimal gap.

## 3. Why two apparent upgrades fail

First keep Q and one conditional test, but use any fixed product FRB basis
unbiased to the computational basis. The F phase cancels in the compression.
Write theta for the total R/B equatorial phase. The compressed conditional
effect has target eigenvalue1 and just one other nonzero eigenvalue

    r_theta=a*(1-a*cos(theta)^2)/(1-a^2*cos(theta)^2).

It is minimized at cos(theta)^2=1, since its derivative with respect to
x=cos(theta)^2 is -a^2*(1-a)/(1-a^2*x)^2<0. The minimum is a/(1+a), exactly
K2454's value. There are two parity classes of support columns, so the compression has
rank at most two. The target is a unit eigenvector; summing the squared
support-column norms gives trace1+r_theta. Since r_theta>0, these identify
the two nonzero eigenvalues. The rank 12 test remains a projection. The two-projection
spectrum gives maximal non-target eigenvalue
[1+sqrt(1-4p(1-p)(1-r_theta))]/2 under mixing pQ+(1-p)T_theta;
p=1/2 is optimal for that fixed pair. Thus changing one such product basis
cannot improve K2454. Random mixtures of inequivalent bases and adaptive
FRB measurements are different classes.

Second consider any target-preserving local diagonal unitary, not only the
finite averaging group above. Since all target amplitudes are positive,
its phase on every original support string must be one common phase.
The good00/11 pair forces the R and B phase increments to cancel. Each
bad E phase is then fixed by its support triple. Consequently the four
companions have that same phase. The compression on (z,bcomp) is invariant
under every permitted conjugation. For Omega_p=pQ+(1-p)average(T), its
compression there is

    [ p+(1-p)a/(1+a), (1-p)sqrt(a/2)/(1+a) ]
    [ same,          (1-p)/(2(1+a))        ].

A half-gap would require this matrix<=I/2. Its slack determinant is

    [p-2p^2-a]/[4(1+a)].                                (6)

But p-2p^2<=1/8, whereas both original a values exceed 1/8. Thus no such
phase average with any p in[0,1] attains gap 1/2. The full verifier in (1)
still improves the gap to at least 2/5. Treating the zero character as only
the ten-string support would erase precisely this obstruction.

## 4. Released consumer and operational boundary

Replace nu in K2450 or K2456 by the rigorous value 2/5 on the same original
programs. The probe composes both certificates with their unchanged,
prospective calibration/leakage/operation allowances and checks the sufficient condition for positive actual mean success
under those allowances. For the common certified gap 2/5, the earlier K2450 assumptions require
433,407 actual uses; the separate K2456 accumulated-budget assumptions
require 934,421. These are sufficient hypothetical counts, not wall-clock cost.
No new source of calibrated routing, coherent custody or trustworthy E
control is created. Sampling 135 labels is cheap classical work only after
the corresponding local phase operations are available and calibrated.

Omitting the E compensation changes the target and can break completeness;
measuring E before its coherent conditional projection remains invalid.
No dephasing or nondisturbing upgrade of an already recorded program is
licensed. The strongest next design is an inequivalent conditional-test
mixture or changed support measurement, with full-carrier validation and
operation costs. The restricted half-gap obstruction cannot be presented
as an impossibility theorem for all local verification.

[Probe](../../tests/channel-swings/k2457_local_verifier_phase_design_probe.py)
and [report](../../lab/process/k2457-local-verifier-phase-design.json).
