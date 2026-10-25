---
title: "K2077: Local controls, remote records and sector conditioning"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional complex-Hilbert theorem; no source-selected detector, GU verdict or novelty claim
scripts:
  - tests/channel-swings/k2077_controlled_detector_response.py
  - tests/channel-swings/k2077_controlled_detector_response_probe.py
---

# K2077: Local controls, remote records and sector conditioning

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: remote response under bounded spatially local control and sector-conditioning boundary
carrier: full massive complex Dirac1408 Hilbert carrier with optional finite ancilla LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 norm and supplied Born probabilities ON=declared_complex_completion
real_structure: complex completion; no source-real/dual identification
grading: free positive and negative energy sectors
action_owner: repository-construction -- bounded Hermitian local matrix perturbation
target: uniform remote record error MAP-TYPE=intertwiner
```

[Conditional mathematical theorem, internal verification.] A bounded spatially local
control has an exponentially small effect on a distant positive-energy-compressed
readout, even when it strongly mixes positive and negative energy. The corresponding
uncompressed local readout is exactly unchanged outside the control's future cone.
Conditioning on positive-sector survival can nevertheless change distant records by
order one. These are three distinct statements on the SAME complex carrier.

## 1. Objects, scope and inherited evidence

Let H0=alpha.D+m beta, m>0, on H=L2(R3,C4 tensor C352), with its self-adjoint H1
domain, U0(t)=exp(-itH0), and P=1_(H0>0). Reuse K2076's dimension-independent
separated-support estimate

    ||E_A P E_B|| <= eta(m dist(A,B)),
    eta(a)=min(1/2, exp(-a)/sqrt(2pi)*(2sqrt(a)+27/(8sqrt(a)))), a>0.   (1)

Its written heat-kernel/Schur proof, with the standard
[NIST Bessel integral representations](https://dlmf.nist.gov/10.32), is inherited,
not new finite-check evidence. Free finite speed is inherited from K2071's full
Dirac argument. No sharp-localization or invariant-local-potential search is repeated:
K2062 already proves that a bounded local exactly P-preserving multiplier must be a
constant Clifford commutant.

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 is UNCERTAIN about
southeast alternatives; SC-META-53 is UNCERTAIN about physical positivity; SC-META-56
DISAVOWS an odd-action prerequisite. None selects this positive Hilbert/Born completion.
LT-SM8/GR6b, source register, ledger and canon remain unchanged. Calibration constraints
on locality motivate a conditional demand; they earn no held-out confirmation.

Let V(s) be a strongly measurable Hermitian matrix multiplier satisfying
V(s)=E_(C_s)V(s)E_(C_s) for almost every s in[0,T], with v(s)=||V(s)|| and
Lambda=integral_0^T v(s)ds finite. The interaction-picture Dyson series converges in
operator norm by the bound Lambda^n/n!, giving a unitary propagator Uv. Boundedness
is in space at each time, with integrable norm in time. No differentiability in space
or preservation of H1 by a rough nonautonomous potential is needed for the bounded
strong integral identities below. For rigor with time supports choose a measurable
support family and a closed set K containing (C_s)_(T-s) for almost every s; null-time
outliers need not enlarge K.

Take ANY effect F=E_G F E_G, 0<=F<=I, with closed essential support G, and set B=PFP.
F may have internal or ancillary matrix structure; it need not be a scalar multiplier.
Assume ell_s=dist(C_s,G)-(T-s)>0 almost everywhere and, for the uniform bound,
ell=dist(K,G)>0. For fixed C at distance d from G, d>T is sufficient and ell=d-T
is a valid conservative gap.

This is a new BOUNDED perturbation class on the same carrier. K2071's Hchi changes
first-order principal coefficients, so Hchi-H0 is not covered. K2073's prepared-state
energy result remains independent. No physical apparatus construction is inferred.

## 2. Remote response without projector preservation

The exact bounded-operator conclusion is

    ||Uv(T,0)* B Uv(T,0) - U0(T)* B U0(T)||
      <= epsilon = min(1, 2 integral_0^T v(s) eta(m ell_s)ds, 4 eta(m ell)).   (2)

If only the pointwise positive gaps are available, omit the last term. For uniform
ell, a simple version is min(1,2 Lambda eta(m ell),4 eta(m ell)). No [Uv,P]=0
assumption occurs.

To prove the integral bound, put F_s=U0(T-s)* F U0(T-s). Free finite propagation
places F_s on BOTH sides inside G_(T-s), including its boundary; closed enlargement
and strong limits handle measurable or unbounded G. Since [U0,P]=0,
B_s=P F_s P. Hence ||V(s)B_s||<=v(s)eta(m ell_s), and
||[V(s),B_s]||<=2v(s)eta(m ell_s). Differentiating the backward-free interaction
quantity, or using its strong integral version, gives

    Uv(T,0)* B Uv(T,0)-U0(T)* B U0(T)
       = i integral_0^T Uv(s,0)* [V(s),B_s] Uv(s,0) ds.             (3)

Unitarity proves the bound. The norm difference of two effects is at most one.

For the strength-independent bound use free-left Duhamel:

    D=Uv(T,0)-U0(T)=-i integral_0^T U0(T-s)V(s)Uv(s,0) ds.

Free finite speed implies D=E_K D, while ||D||<=min(2,Lambda). Thus
||BD||<=eta(m ell)||D||. Expanding the response as
D* B Uv+U0* B D gives 2eta(m ell)min(2,Lambda). This proves the claimed cap
without needing controlled finite speed or small global leakage. It also handles
arbitrarily strong bounded pulses when their causal output region stays separated.

## 3. Exact full-carrier causality and complete remote records

For the uncompressed F, FE_K=0 gives FD=D*F=0. The same expansion proves
Uv* F Uv=U0* F U0 EXACTLY. Positive-energy compression is responsible for the
small tail in(2); this identity does not turn the compressed effect into a local
instrument implementation.

Let {F_j} be finite or countable positive effects with sum_j F_j<=E_G. Use remote
click effects B_j=PF_jP, completed by ONE residual outcome I-sum_j B_j. Every subset
sum of clicks is another supported effect, so(2) bounds its probability difference
by epsilon for every state. A subset containing the residual is the complement of
such a subset. The total variation of the complete record distributions, defined
as the supremum over outcome subsets, is therefore <=epsilon, independent of outcome
count. Countable sums converge strongly and preserve the bound.

The proof is unchanged for H0 tensor I, P tensor I, local matrix controls coupling a
finite detector ancilla, and initial entanglement with arbitrary untouched ancillas.
The output must still be spatially supported, for example F_j=g tensor M_j.
A bare readout I tensor M_j has full spatial support and is not covered without a
separate coupling/readout argument. Splitting the residual into global negative-sector
failure Q=I-P and positive-sector no-click likewise destroys the record-locality
conclusion: Q itself is a global diagnostic.

## 4. Sector leakage, conditioning and a counterexample

The independent commutator identity gives

    ||[Uv(T,0),P]|| <= kappa=min(1,integral_0^T ||[V(s),P]||ds)
                     <=min(1,Lambda).

The cap one follows from the distance of two orthogonal projectors, not a factor-two
unitary triangle estimate. For initial rho=P rho P, the failed-sector probability is
1-q=tr(Q Uv rho Uv*)<=kappa^2. This bound has NO separation factor.

For any B<=P, write n=tr(B Uv rho Uv*), p0=tr(B U0 rho U0*), with q>0. Since
0<=n<=q and |n-p0|<=epsilon,

    |n/q-p0| <= |n-p0|+n*(1-q)/q <=epsilon+1-q.                    (4)

Thus the useful bound is min(1,epsilon+kappa^2). A preliminary ratio estimate with
denominator q is valid but weaker; using n<=q removes that unnecessary denominator.
The same conclusion holds for total variation of the conditioned remote record:
the unconditioned coarse record is q times the success record plus (1-q) at the
residual outcome, at TV distance at most1-q from the success record.

Separation alone supplies no bound tending to zero for the conditioned experiment.
Here is a continuum construction, not a compactly supported positive-energy state.
Choose a smooth beta-positive spinor packet phi_R with momentum width tending to zero
as R grows. The normalized P phi_R differs from phi_R by a norm tending to zero,
since P(p) tends to (I+beta)/2 near p=0. A cutoff chi_R equal to one on a ball
capturing all but a vanishing packet norm gives the local pulse
V=(pi/(2tau))chi_R alpha1. For fixed smooth cutoff and packet, as tau tends to zero,
exp[-i(tau H0+(pi/2)chi_R alpha1)] tends strongly on that packet to
exp[-i(pi/2)chi_R alpha1]. This follows by Duhamel on smooth H1 vectors; its error
is at most tau times the integral of ||H0 exp[-is(pi/2)chi_R alpha1]psi||.
On the captured packet it acts as -i alpha1, changing beta-positive to beta-negative.
Taking the limits in this order makes failed-sector probability tend to one.
Each pulse has finite bounded norm, compact support and fixed integrated strength.

Add a distant translated copy of the original positive packet with equal amplitude.
Translate far enough that the two packets, their cutoff tails and their causal tubes
are disjoint to arbitrarily small norm error, with m ell tending to infinity. A remote
spatial detector captures the second packet. Initially p0 tends to1/2. After the pulse,
the distant numerator still tends to1/2 by(2), but q tends to1/2 because the controlled
packet has flipped sector. The conditioned distant click tends to1. A diagonal choice
of R, cutoff radius, tau and translation makes all errors tend to zero. No exact
compact support for P phi_R is asserted. The exact finite three-state fixture in the
probe checks the probability logic; the wavepacket/strong-limit proof supplies the
continuum realization. Even success bounded near one half does not prevent this effect.

## 5. Follow-through: an actual compact bounded ancilla instrument

Effects alone do not specify their instruments. The following supplies one on the
same carrier with one explicitly added two-state ancillary memory. This changes the
readout from scalar position to that ancillary record and allows small sector leakage;
it does not evade K2067's exact-sector scalar-readout theorem.

Let A be an orthogonal projector on the supplied multiplicity qubit, so[A,H0]=[A,P]=0.
Initialize the ancillary memory in|0>. For smooth compact0<=chi<=1 and T>0 use

    V=(theta/T) chi(x) A tensor sigma_y,    theta=pi/2.           (5)

This is an actual bounded Hermitian local matrix potential, with integrated norm at
most theta. The two Kraus operators on the system are K_j=<j|Uv(T,0)|0>, j=0,1;
unitarity gives sum K_j* K_j=I. Because free evolution never clicks this ancilla,
K_1=<1|(Uv-U0 tensor I)|0>. If C=supp chi, right-free Duhamel gives
K_1=K_1 E_(C_T): V U0(s) can depend only on initial support in C_s, a subset of C_T.
Left-free Duhamel similarly gives K_1=E_(C_T)K_1. Therefore the actual initial click
effect F_click=K_1* K_1 is supported on BOTH sides in C_T. This proves the support
that a bare I tensor |1><1| readout did not supply on its own. Also K_1=K_1 A and
F_click<=A, since A-perpendicular evolves freely with its ancilla still|0>. There
are exactly zero false clicks on that internal subspace. Use F_click as the supported F in the response theorem, and P F_click P as its
compression B.

For accuracy choose chi=1 on B_(L+T), vanishing outside B_(L+T+rho), rho>0. Let a
normalized positive-energy preparation psi have norm tail tau outside B_L. Compare
with the homogeneous reference

    Uref=(U0(T) tensor I) exp(-i theta A tensor sigma_y).

Both bounded local evolutions have speed1. This follows directly from the convergent
Dyson series: multiplication potentials preserve supports, and the free propagation
durations in each term sum to T. For the truncated datum E_(B_L)psi, the reference
solution remains in the plateau for the whole pulse, so Duhamel gives Uv=Uref on
that datum. By unitarity on the remaining tail,

    ||(Uv-Uref)(psi tensor|0>)|| <=2tau.                         (6)

This reuses K2071's causal-tube/truncation method for a different bounded coupling;
no short-pulse approximation or uniform-in-state claim is needed. Uref commutes P.
Consequently the final negative-sector probability is at most4tau^2, and the
complete binary-record TV error relative to ideal A measurement is at most4tau^2.
Indeed the ideal no-click Kraus operator annihilates A psi, so
0<=<A>-p_click=||K_0 A psi||^2<=4||E_(B_L^c)A psi||^2<=4tau^2.
This uses exact zero false positives; the generic state-vector estimate alone would
only give the weaker4tau bound. The reference Kraus operators are U0(T)A
and U0(T)(I-A), so the ideal instrument is the corresponding Lueders measurement
followed by free propagation. These estimates hold uniformly over the prepared
multiplicity subspace, including entanglement with untouched systems. They do not
postselect away sector failure.

Use the K2067 positive Gaussian spinor phi with s=m, WITHOUT its optional backward
free prechirp. The same coordinate-derivative argument for each axis gives
sum_j <X_j^2><=51/(4m^2), hence tau<=sqrt(51)/(2mL)<4/(mL).
Choose L=2000/m, T=1/m, rho=1/m. Then

    control support radius=2002/m,   click input support radius<=2003/m,
    ||V||<=pi*m/2,  integrated norm<=pi/2,
    tau<1/500,  record TV<1/62500,  leakage probability<1/62500.    (7)

These are finite sufficient particle-control resources. They are not a control-field
energy, detector-field implementation or physical preparation theorem. The original
K2073 energy2m applies to this phi as well, but is not needed for(6).

As a further consumer, take two explicitly supplied tensor copies with these spatial
preparations and an entangled pair of internal qubits. Set A_x=(I+n_x.sigma)/2 by
the local control. On the fixed spatial preparation, the qubit click effect is r A_x,
where1-r<=4tau^2: the A_x branch has one common spatial evolution and the other
branch never clicks. The induced +/-1 observable O_x=2r A_x-I is a contraction
and differs from ideal2A_x-I by norm<=8tau^2. A tensor correlation therefore differs
by at most16tau^2, and the four-setting CHSH sum by at most64tau^2. Consequently

    CHSH_actual >=2sqrt(2)-64tau^2
                 >14/5-64/250000=43746/15625>2.                 (8)

Every ancilla outcome is retained. The two apparatus cylinders can be made spacelike
separated by center distance D>2(2002/m)+1/m; D=4006/m suffices. This is a conditional
tensor-system construction, with its own exact tensor-factor no-signalling identity;
it is not a Fock-space/local-field embedding or GU Bell derivation. Extra ancillas,
positive Hilbert states, preparation, tensor composition and Born readout are declared
imports. Equation(2) separately quantifies response of a compressed spatial detector
to another bounded intervention. Do not conflate that one-particle bound with the
tensor experiment's no-signalling identity.

## 6. Consumed resources, review and next boundary

The producer reuses K2076's rational upper envelopes, independently checked in the
probe. For ANY integrated bounded-control strength, m ell=20 gives complete remote
record TV<1/10^7 and m ell=32 gives TV<10^-12. For Lambda=1 and independently
proved leakage probability<=10^-6, the latter gives conditioned TV<1.001*10^-6.
These are sufficient dimension-independent tolerances, not optimal constants or a
physical control-energy budget. Smaller integrated strength improves the first term
of(2); increasing it beyond two does not worsen the cap.

Separate matrix and rational controls challenge support algebra, Duhamel sign,
linear versus quadratic tails, sector-record scope and conditioning. They do not
prove the continuum propagation theorem. Independent internal operator review checks
the written transfer and postselection ceiling. No external or proof-assistant
certification is claimed. The bounded ancilla construction now supplies that instrument in its declared tensor
completion. A physical local-field embedding, source-real/dual compatibility and a
control-field energy account remain unsupplied. The unbounded confined-pointer
generator remains outside this response theorem and requires its own energy-dependent
estimate. None of these additional premises is implied by the finite resource table.
