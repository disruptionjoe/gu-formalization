---
title: "K2115: Exact global excitation bounds for synchronized local Dirac pulses"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive Dirac pulse theorem; no source selection, collective gate or controller energy budget
scripts:
  - tests/channel-swings/k2115_exact_pulse_excitation_bound_probe.py
---

# K2115: Exact global excitation bounds for synchronized local Dirac pulses

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
result: conditional operational and analytic mathematics
carrier: supplied complex Hilbert CAR, finite code and ordinary external tensor reference LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: CAR adjoint; no source-selected reality or barred-field identification
grading: fermion parity; energy sign, charge and source grades remain separate
action_owner: repository-construction -- supplied CAR and free massive Dirac dynamics
target: finite-factor instruments or specified free-Dirac scattering MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and prior-result boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
The imported positive CAR/Dirac construction is not source operator9.16.
K2021 local R0/R1 maps do not select its state, algebra or dynamics.
LT-SM8/LT-GR6b retain their action/observation/quotient/positivity debts.
Source register, ledger0.263 and canon verdicts remain unchanged. These results
answer reverse-scaffold coherence and causal-transfer demands; no GU recovery,
new substrate pathway, novelty or external certification is claimed.

## 1. Exact synchronized-family result

Use the SAME imported rank-four massive Dirac operator and second species as
[K2112](k2112-positive-mode-local-capture-2026-10-26.md):

    H=L2(R3,C4) tensor C2, h=(-i alpha.grad+beta m) tensor I2,
    m>0, Dom(h)=H1, E=|h|, Q=sgn(h), P_+/-=(I+/-Q)/2.

Let a in C_c^infinity(0,1;R), rho in C_c^infinity(R3;R), T>=1, and

    V_T(t,x)=T^-1 a(t/T) rho(x/T) tensor sigma_y.        (1)

Let U_T be the ACTUAL common-H1-domain unitary propagator and
S_T=exp(iTh)U_T(T,0). For r>=0 define the particle PLUS hole moment

    J_r(S)=||E^(r/2) P_+ S P_-||_HS^2
            +||E^(r/2) P_- S P_+||_HS^2.              (2)

For every integer N>r/2+3/2 there is a finite T-independent constant C_N,r with

    J_r(S_T) <= C_N,r T^(3-2N).                        (3)

Thus every fixed one-particle excitation-energy moment decays faster than any
inverse power. This is an exact all-order result, not a Born coefficient.
The area condition integral a=pi/2 is needed for the swap consumer, not for(3).
The mass and profiles are fixed; no uniformity as m tends to0 is asserted.
K1897 fixed-pulse finiteness and K2112 first-order bounds remain valid but do
not prove(3). The following proof exposes the missing uniform global estimate.
No novelty or proof-assistant certification is claimed.

## 2. A Fourier-kernel calculus charging spatial volume

Use the unitary transform on vectors and the UNNORMALIZED profile transform
rhohat(k)=integral exp(-ik.x)rho(x)dx. A multiplication kernel in momentum space
is (2pi)^-3 T^3 rhohat(T(p-q)). E_p=sqrt(|p|^2+m^2) is a scalar.

For integer k>=0, A_T is in K_k when, for every needed real shift s, a
nonnegative F_s in L1 intersection L2, independent of T and time, bounds

    ||E_p^(s+k) Ahat_T(p,q) E_q^-s||
        <= T^3 F_s(T(p-q)).                           (4)

Norms inside(4) are finite matrix operator norms. Notation epsilon^j K_k means
the normalized operator epsilon^-j A has such uniform majorants. Fixed finite
sums and integrals with common majorants are allowed. Constants can depend on
mass, profiles, finite derivative order and iteration depth.

The normalized initial potential T V_T belongs to K0: the ratio of energy
weights is at most C_m,s <p-q>^|s| <= C_m,s <T(p-q)>^|s|, and rhohat is
Schwartz. Time derivatives add T^-1 for each derivative.

Here are all closure rules used below, derived directly from(4).

* Products K_k K_l lie in K_(k+l). Insert the intermediate weights with shifts
  s+l for the first factor and s for the second. The convolution identity is
  integral T^3 F(T(p-z)) T^3 G(T(z-q)) dz
  =T^3(F*G)(T(p-q)). Young inequalities preserve L1 intersection L2.
* Q and P_+/- on either side preserve the bounds. They commute with E and
  have bounded matrix norm. K_k embeds in K0 with factor m^-k.
* For X in K0, exp(X)-I is majorized by sum_(j>=1) F_s^(*j)/j! at EACH FIXED
  shift s. L1 convergence is exponential; L2 convergence follows from
  ||F^(*j)||2 <= ||F||2 ||F||1^(j-1). For X in K_k retain its smoothing using
  exp(X)-I=X integral_0^1 exp(uX)du. Conjugating K_l uses the fixed shifts
  s+l and s, never shifts growing with the exponential-series index.
* Schur's test gives ||E^s A E^-s||op <= ||F_s||1 for A in K0.
* If A in K_k, u>=0, k-u>3/2, fiber dimension d, then

    ||E^u A||HS^2 <= d T^3 ||F_0||2^2 I_(k-u),
    I_b = integral_R3 E_p^(-2b) dp
        = pi^(3/2) m^(3-2b) Gamma(b-3/2)/Gamma(b).     (5)

For the last statement, take s=0 in(4), multiply by E_p^(u-k), square, use
matrix HS norm squared <=d times operator norm squared, and integrate first
in q. The T^3 factor survives. An operator-norm adiabatic estimate alone would
not give this trace bound. Finite many time derivatives of exponential factors
are handled by their exact Duhamel derivative formula and these same fixed-shift
product estimates. At any fixed iteration depth only finitely many such orders
are required; the profiles supply all of them.

## 3. Exact free-gap inverse and changes of variables

For bounded selfadjoint Q-offdiagonal O in K_k, as all terms below are, define

    K=integral_0^infinity exp(-uE) O exp(-uE) du,
    X=-QK.                                            (6)

The free mass gap makes this norm-convergent. Its kernel is O(p,q)/(E_p+E_q).
Hence K and X gain one smoothing degree: K_k maps to K_(k+1), since
E_p/(E_p+E_q)<=1. Also K*=K, QK=-KQ, X*=-X and

    [h,X]=-EK-KE=-O.                                  (7)

These equalities hold on H1 and extend as bounded commutators. The kernel
estimates at shift1 preserve H1; there is no assumption about an instantaneous
spectral gap of h+V_T.

Set epsilon=1/T, A0=V_T, split A_k=D_k+O_k by Q diagonal/offdiagonal parts,
and construct X_k from O_k by(6). Define the transformed Hamiltonian EXACTLY:

    h+A_(k+1)=exp(-X_k)(h+A_k)exp(X_k)
                 -i exp(-X_k) d_t exp(X_k).           (8)

All transformations are unitary and preserve H1. With A_(k+1)=D_k+R_k,

    R_k= integral_0^1 exp(-uX_k)[A_k,X_k]exp(uX_k)du
       - integral_0^1(1-u)exp(-uX_k)[O_k,X_k]exp(uX_k)du
       - i integral_0^1 exp(-uX_k)dot(X_k)exp(uX_k)du.  (9)

The second term's sign follows from(7). Formula(9) is the integral remainder
identity for conjugation, not a truncated Baker-Campbell-Hausdorff expansion.
For every finite derivative order ell needed in a fixed construction,

    d_t^ell A_k in epsilon^(1+ell) K0,
    d_t^ell O_k in epsilon^(k+1+ell) K_k,
    d_t^ell X_k in epsilon^(k+1+ell) K_(k+1),
    d_t^ell R_k in epsilon^(k+2+ell) K_(k+1).           (10)

Induction: the base follows from(1). The Sylvester inverse is time independent.
The first commutator in(9) has size epsilon^(k+2) and smoothing k+1. The second
has size epsilon^(2k+2) and at least k+1 smoothing, no larger since epsilon<=1.
The time derivative term gains one epsilon. Differentiating exact exponentials
inserts derivatives of X with the matching additional epsilon factors. Uniform
convolution majorants close every term. Because D_k commutes with Q, the next
offdiagonal term is off_Q(R_k), giving the next line of the induction.

The compact smooth switch and all its derivatives vanish near the time endpoints.
Every A_k and X_k therefore vanishes there as well; in particular X_k(0)=X_k(T)=0.
After ANY finite N changes of variables the endpoint propagator is unchanged.
No asymptotic-series convergence is asserted or needed.

## 4. Exact weighted propagation and the global bound

Choose u=r/2 and N>u+3/2. Let F_N,0 be a uniform majorant of
normalized epsilon^(-N-1) O_N in K_N. Equation(5) gives

    ||E^u O_N(t)||HS <= sqrt(8) epsilon^(N+1) T^(3/2)
                         ||F_N,0||2 sqrt(I_(N-u)).     (11)

From(10), ||E^u A_N(t)E^-u||op<=c_N,u epsilon uniformly. The free evolution
commutes with E, so the interaction-picture integral equation and Gronwall
bound ||E^u U_N(t,s)E^-u||op by exp(c_N,u) for0<=s<=t<=T.
The exact commutator Duhamel identity then gives

    ||E^u[Q,S_T]||HS
        <=2 exp(c_N,u) integral_0^T ||E^u O_N(t)||HS dt. (12)

Indeed [Q,A_N]=2QO_N; the left propagator is bounded in the weighted norm,
and the right propagator is unitary in the unweighted norm. Smooth cutoffs
or bounded spectral truncation followed by HS convergence justify the identity
on the common domain. The two offdiagonal blocks are HS-orthogonal and

    J_r(S_T)=(1/4)||E^(r/2)[Q,S_T]||HS^2.

Combining this with(11)--(12) proves(3), for example with

    C_N,r=8 exp(2c_N,r/2) ||F_N,0||2^2 I_(N-r/2).      (13)

These constants are recursively constructible from profile convolution norms.
They have not been evaluated as laboratory resource budgets. Their independence
of T, not a guessed numerical size, is the conclusion.

## 5. Released global vacuum and capture consequences

In the doubled free-sea CAR representation, endpoint HS offdiagonal blocks
supply the polarized implementation used in K1897. For its sea vector Psi_T,

    <N_exc>=J0(S_T),   <H_exc>=J1(S_T).                 (14)

This follows from the transformed covariance S_T P_- S_T*: particle and hole
occupations are respectively P_+ S_T P_- S_T* P_+ and
P_- S_T P_+ S_T* P_-. Energy weights commute with the free projections.
Since N_exc>=I-|Omega><Omega|, the pure-state trace distance satisfies

    D(Psi_T,Omega) <= sqrt(min(1,J0(S_T))).             (15)

Thus the GLOBAL doubled sea returns in trace norm, and its mean total free
excitation energy tends to zero, faster than every inverse power. The global
phase of the implementing unitary has no effect on(15). Higher J_r are
one-particle energy moments, not automatically higher powers of total Fock energy.
No norm convergence of the whole field channel or uniform all-input energy
bound follows from this vacuum statement.

Take rho equal1 on B_A with A>1 and integral a(t)dt=pi/2. The K2112 finite
positive-code tail theorem and(3) then hold for the SAME family, without
retuning its profiles separately. Every fixed finite positive code has capture
error <=pi sum_j t_j((A-1-eta)T), eta in(0,A-1); independently the initially
empty doubled sea satisfies(14)--(15). Moment-localized code frames give the
previous explicit tail rates. This combines actual selected-code accuracy and
quiet global vacuum endpoints. It does not assert global sea return for an
arbitrary excited input or pay the energy cost of a collective gate.

Any fixed finite pulse train T^-1 sum_j a_j(t/T)rho_j(x/T)M_j, with fixed
smooth compact real profiles and fixed Hermitian matrices M_j, obeys the same
proof on a fixed rescaled interval, including overlapping pulses. Constants
depend on the train. No uniformity in pulse count growing with T is claimed.
The forward/return field pulses can therefore share the bound; inserting an
arbitrary collective gate still requires its own controlled domain/resource.

### Entire-field finite-code output with fixed vacuum spectators

The vacuum theorem releases a stronger consumer than K2112's restricted output.
Let F=(f_j) be a fixed finite orthonormal positive-energy frame. Prepare its
entire Fock code over the doubled sea vacuum, with all spectator excitations
absent. This is a FIXED preparation isometry J_F, not an arbitrary extension
of the same code marginal. Let G=(g_j) be the ideal positive-energy captured
frame in the calibrated scattering picture, and delta_j=||S_T f_j-g_j||.
Then the actual and ideal channels into the ENTIRE field Fock space obey

    (1/2)||Ad_(Uhat_T J_F)-Ad_(J_G)||diamond
       <= min(1, sqrt(2 J0(S_T))+(pi/2)sum_j delta_j).   (16)

All external references are allowed. For the K2112 local pulse delta_j<=2t_j,
so the right side is at most sqrt(2J0)+pi sum_j t_j, capped by1. This combines
the same-family global-vacuum and fixed-code tail estimates without assuming
positive modes compactly supported. It asserts neither arbitrary spectator
input restoration nor convergence uniform in a growing code dimension.

Proof. Reuse K2111's auxiliary d-mode CAR memory b_j and its even swaps W_F,
with W_F* b_j W_F=a_ext(f_j). In the memory-first representation,
b=b tensor I and a_ext=P_memory tensor a_field. Since F is empty in Omega,

    W_F*(psi tensor Omega)=|0>_memory tensor J_F psi.

This choice of the adjoint fixes the creation-basis signs. Extend the field
implementer as I_memory tensor Uhat_T. It fixes b and conjugates a_ext(f) to
a_ext(S_T f), so it intertwines W_F* with W_(S_T F)*. This identity uses no
field-parity assumption on the chosen implementing unitary. Also a(S_T f_j)
annihilates Uhat_T Omega, so the auxiliary memory empties in the actual output.

K2111's product-exponential estimate gives
||W_(S_T F)-W_G|| <=(pi/2)sum delta_j. Choose the irrelevant implementing phase
so the vacuum overlap is nonnegative. If a0=|<Omega,Uhat_T Omega>|, then
1-a0^2<=J0 and ||Uhat_T Omega-Omega||^2=2(1-a0)<=2J0.
The triangle inequality on the two preparation isometries now bounds their
operator-norm difference by the right side of(16) before capping. This bound
is unchanged by tensoring an arbitrary reference. Pure output trace distance
is at most the vector distance; purification and contraction extend it to all
inputs, proving(16). The auxiliary memory is a proof device, not a newly
implemented physical detector.

## 6. Exclusions and acceptance

The proof does not apply as written to m=0, nonsmooth switching, nonvanishing
endpoint dressings or fixed-duration growing-aperture pulses. K2112's positive
linear Born coefficient for the latter family remains intact. The apparatus
volume and elapsed time grow; small field excitation energy is not small total
controller work or a bounded-size detector construction.

Finite controls test the actual Sylvester inverse and sign, offdiagonal cancellation,
exact transformed two-level Hamiltonian, time-derivative connection, Fourier
volume scaling and massive radial integral. They cannot certify the continuum
or universal estimates. Those rest on the written kernel/induction/Duhamel proof
and independent specialist review. The useful next gate is the actual local
collective reflection with controlled energy and causal record, or the strongest
source-selected observation/domain alternative; do not repeat the Born-only test.
