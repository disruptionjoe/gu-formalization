---
title: "K2076: Dimension-free locality bounds for separated detectors"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical result only; no GU source verdict, canon promotion or novelty certification
scripts:
  - tests/channel-swings/k2076_separated_detector_locality.py
  - tests/channel-swings/k2076_separated_detector_locality_probe.py
---

# K2076: Dimension-free locality bounds for separated detectors

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: exponential cross-region operator bound and specified operation disturbance
carrier: full complex massive Dirac1408 Hilbert carrier and fixed positive spectral subspace LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 pairing and imported Born probabilities ON=declared_complex_completion
real_structure: complex Hilbert completion; source real and independent dual not identified
grading: free energy sign and supplied multiplicity, not source parity
action_owner: repository-construction -- fixed H0 and specified effect-generated instruments
target: separated compressed scalar position effects MAP-TYPE=intertwiner
```

[Conditional mathematical theorem, internal verification.] Let H0=alpha.D+m beta,
m>0, on L2(R3,C1408), and P=(I+H0/sqrt(H0^2))/2. For scalar effects0<=f,g<=1
with essential supports separated by d>0, put a=m*d. Then

    ||f P g|| <= eta(a),
    eta(a)=min(1/2,exp(-a)/sqrt(2*pi)*(2*sqrt(a)+27/(8*sqrt(a)))).       (1)

This estimate is independent of carrier dimension and support volume; even unbounded
separated regions are allowed. It gives quantitative control for specified operations
on the positive-energy subspace, without asserting exact locality or a GU field model.

## 1. Reuse, question and scope

[K2062 section5](k2062-bounded-local-multiplier-rigidity-2026-10-25.md) already supplies
a finite-volume Hilbert-Schmidt estimate with factor1408*|A|*|B| and kernel decay
exp(-m*d/2). Its kernel is reused. The new work is a volume/dimension-independent
operator-norm bound at exponent exp(-m*d), followed through into operations rather
than another sharp-localization obstruction. K2065 already proves compatibility of
common compressed-position postprocessings; noncommutation alone is not Bell
incompatibility. K2071/73 retain their separate full-carrier finite-speed and
prepared-state energy theorems. No bound here establishes control-field energy,
physical preparation, fixed-sea implementability or a source-real detector algebra.

SC-OP-04 ASSERTS the candidate four-field operator grammar; SC-OP-05 is UNCERTAIN
about the southeast alternative; SC-META-53 is UNCERTAIN about physical positivity;
SC-META-56 DISAVOWS an odd-action prerequisite. None supplies this positive Hilbert,
Born or instrument completion. LT-SM8/GR6b, source register, physics ledger and canon
remain unchanged. The source indefinite pairing and physical quotient are different
objects. K1892's exact local even-CAR algebra uses a different16-to4 carrier; its
result cannot be imported by matching names.

## 2. Actual continuum kernel and Schur transfer

The reused heat-kernel formula gives, away from r=0,

    h_m(r)=m*K1(m*r)/(2*pi^2*r),
    P(x,y)=[m*beta*h_m(r)-i*alpha.n*h_m'(r)]/2.        (2)

The identity delta distribution vanishes between the separated supports. Since
alpha.n and beta are anticommuting Hermitian involutions, direct squaring of the
matrix's adjoint product gives norm(m*h+|h'|)/2. An upper triangle bound alone also
suffices. Operator-valued Schur integration over r>=d yields

    T(a)=1/pi integral_a^infinity[z*K1(z)+z*K0(z)+2*K1(z)] dz,
    ||fPg||<=T(a).                                  (3)

This uses whole-space row/column integrals of a scalar norm majorant and therefore
needs no finite region volume and no multiplicity factor. The factor4*pi*r^2 from
three-dimensional integration is included. The Bessel representations/derivatives
are standard, checked against [NIST DLMF10.32](https://dlmf.nist.gov/10.32) and
[DLMF10.29](https://dlmf.nist.gov/10.29); no novelty is asserted for those identities.

Let c=sqrt(pi/2). The integral K0(z)=integral_0^infinity exp(-z*cosh u)du and
cosh u>=1+u^2/2 give K0(z)<=c*exp(-z)/sqrt(z). Also

    K1(z)=z integral_1^infinity exp(-z*t)*sqrt(t^2-1)dt.

Writing t=1+s and using sqrt(2s+s^2)<=sqrt(2s)*(1+s/4), then integrating the two
Gamma moments, gives K1(z)<=c*exp(-z)/sqrt(z)*(1+3/(8z)). These inequalities hold
for every z>0. K0'=-K1 and (z*K1)'=-z*K0 transform(3) exactly into

    T(a)=[(a+2)K0(a)+a*K1(a)+integral_a^infinity K0(z)dz]/pi.

The remaining integral is at most c*exp(-a)/sqrt(a). Substituting yields(1)'s
exponential expression. Independently, fPg=f(P-I/2)g and ||P-I/2||=1/2, since
fg=0. This proves the cap1/2. No finite-node computation certifies this continuum
argument; it is a written integral and operator proof.

## 3. Operation-specific consequences

On Hplus=Ran(P), let A=PfP and B=PgP. These are positive contractions and
||AB||<=eta, so ||[A,B]||<=2eta. All bounds persist with an untouched ancilla.

**Unitary operations.** Double Duhamel gives

    ||exp(isA)exp(itB)-exp(itB)exp(isA)||<=2*|s*t|*eta.

For any density state and final effect, the elementary operator sandwich bound
therefore limits the order-dependent probability difference to min(1,4*|s*t|*eta).
This conservative consequence does not assume a relativistic signaling model.

**Binary Lueders measurement.** For the specified nonselective channel,

    L_A(B)=sqrt(A) B sqrt(A)+sqrt(I-A) B sqrt(I-A),
    ||L_A(B)-B||<=3*eta.                              (4)

To prove it, set C=sqrt(I-A) and D=I-C=A(I+C)^(-1). Since D commutes with A and
||(I+C)^(-1)||<=1, ||DB||,||BD||<=||AB||<=eta. Further
CBC-B=-DB-CBD has norm<=2eta. The positive first term sqrt(A)B sqrt(A) has the
same nonzero spectrum as AB, so its norm is at most||AB||<=eta. Add the bounds.
This proves the unconditioned binary probability disturbance for every state.
Arbitrary instruments with the same effects need not obey it; postselection can
amplify errors by dividing by a small event probability.

**Sequential records.** Each ordered click-click effect lies between0 and eta*I,
so each click-click probability and the difference of the two orders are at most eta.
Write the four probabilities using the two binary marginals and their click-click
probability. Reversing order changes each affected marginal by at most3eta via(4),
and the joint click by at most eta. The triangle inequality gives total variation
at most min(1,8eta). This is a record-distribution statement for these specific
Lueders operations, not exact commutation, arbitrary detector dynamics or tensor-
factor no-signalling. Tensor-factor instruments on distinct systems obey their own
exact no-signalling identity even when this one-particle localization question differs.

## 4. Consumed separation resources and strictly nonzero tails

The manifest certifies six integer separations by rational arithmetic. For integer
a>=1, replace sqrt(a) by its upper integer bound and1/sqrt(a) by the reciprocal
lower integer bound; use pi>3 and exp(a)>sum_(k=0..80)a^k/k!. These substitutions
provide rigorous upper bounds without floating Bessel evaluations. In particular,

    m*d=20 gives3*eta<1/20000000,
    m*d=32 gives3*eta<1/10^12.

The constants are sufficient, not optimal. They supply explicit unconditioned
measurement-error/separation requirements, compatible with fixed mass and arbitrary
ancilla size. They do not certify an implementation's spatial support or duration.
The following free-evolution argument supplies a precisely limited unequal-time
extension; controlled and interacting evolution still require their own proof.

Exact tails remain: choose nonnegative nonzero smooth bumps in separated regions and
a constant unit beta-positive spinor u. Anticommutation implies u*alpha_j*u=0.
Their cross matrix element from(2) is m/2 times the integral of the two bumps and
h_m(|x-y|), which is strictly positive. Thus some cross-region coupling persists at
all finite separations. This witness proves fPg is nonzero for these positive bumps;
it does NOT prove every compressed commutator is nonzero. Small nonlocality and
exact microcausality are different assertions.

## 5. Follow-through: freely evolved detectors at different times

Let U(t)=exp(-it*H0), and A_t=P U(t)* f U(t) P, B_s=P U(s)* g U(s) P.
Full-carrier free Dirac propagation has speed1 by the inherited K2071 domain and
propagation argument; importantly [U(t),P]=0. If r=|t-s|<d, let F be the closed
essential support of f and F_r its CLOSED radius-r enlargement. Then

    E_F U(t-s)=E_F U(t-s) E_(F_r),
    ||A_t B_s||<=||f U(t-s) P g||
                <=||E_(F_r) P E_G||<=eta(m*(d-|t-s|)).       (5)

For measurable unbounded supports use closed essential supports and include the
enlargement boundary. If finite propagation is stated with strict separation,
apply it outside radius r+1/n and pass to the strong limit. No finite-volume or
smooth-boundary assumption is needed. Unitary multiplication on the left/right
reduces the product to P f U(t-s) P g P; the displayed support identity then proves
the bound. All section3 operation bounds follow with this effective gap, since the
two effects remain positive contractions.

The exact resource examples m=1,d=30,|t-s|=10 and m=2,d=20,|t-s|=4 reproduce the
20 and32 effective-gap tolerance rows. At d<=|t-s| this proof supplies no positive
separation. These are free Heisenberg effects with the STIPULATED instruments;
the proof does not establish physical localization of their implementation at the
nominal times. It does not transfer to Hchi controlled propagation merely from its
speed bound: that evolution need not commute with P. Approximate free bounds do
not constitute exact relativistic microcausality.

## 6. Verification and next boundary

Finite symbolic controls check heat/Bessel constants, Clifford singular values and
rational envelopes. Numerical quadrature and finite matrix controls are labeled
corroboration, not whole-domain certification. Actual mutations of normalization,
Bessel derivative, resource coefficients and operation scope are rejected after a
passing baseline. Independent internal operator review checks the continuum kernel,
Schur transfer and specified-instrument proof. No external or proof-assistant
certification or novelty claim is made. The remaining source-facing step is an
actual detector-field/preparation/instrument bridge; controlled and interacting
locality estimates require their own domains and projector compatibility. Exact thermal equality
in K2075 remains an independent fixed-bath result, not another physical confirmation.
