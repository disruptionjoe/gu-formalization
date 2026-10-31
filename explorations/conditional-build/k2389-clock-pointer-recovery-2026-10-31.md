---
title: "K2389 A noisy QND clock qubit: classical records versus coherent recovery"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-channel mathematics; no native GU or measured apparatus verdict
scripts:
  - tests/channel-swings/k2389_clock_pointer_recovery_probe.py
---

# K2389 A noisy QND clock qubit: classical records versus coherent recovery

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
result: K2389
carrier: K2383 four dual-rail code, final occupation flags, one fresh clock qubit and arbitrary untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and reference-aware half-diamond distance ON=declared_carrier
real_structure: complex amplitudes with real matched loss and pointer dephasing rates
grading: occupied/vacuum pairs and classical extracted binary survivor; clock either measured or retained
action_owner: repository-construction -- supplied number-selective clock coupling and shaped matched Markov loss
target: complete specified noisy instrument and optimal final recovery for two separately declared resource classes MAP-TYPE=evaluation
```

## Result and semantic boundary

K2386 assumed a time-label instrument. Here a specified finite-duration, bit-blind
coupling constructs a noisy timing instrument. One clock qubit suffices for a
strict improvement with a classical readout. Keeping that qubit coherent gives
a different, stronger instrument: in the noiseless limit it attains the idle
two-erasure floor without an exact classical timestamp. Neither construction
recovers quantum information erased by two losses. No emitted bath mode, erased
rail bit or pre-shared reference is supplied to recovery.

For the supplied single-circle fixture, write w=pq and let 0<=nu<=1 be the
clock's equatorial visibility. The exact complete optimal half-diamond errors are

    e_classical = w(3-nu/2)/4,
    e_coherent  = w(3-nu)/4.                            (1)

The classical optimum allows every POVM on the clock and every final CPTP
decoder of its classical outcome and the surviving system. The clock must be
measured independently of the survivor, as an ordinary timing readout; allowing
joint coherent operations changes the resource class. A fixed equatorial
projective measurement attains the bound. Even allowing the readout POVM to
condition on the already classical survivor sign does not improve it, by the
same per-sign Bloch-vector bound below. The coherent optimum allows every final
CPTP decoder on the survivor and unmeasured clock. These are supplied apparatus
models, not claims of hardware construction or GU dynamics. SC-META-53 remains
UNCERTAIN; LT-GR6b stays open.

## Finite-slew full-circle loss fixture

Use the K2383 code, final erasure flags and transparent Hamiltonian h=0,
H_system(t)=g(t)Z_ET. Pair0 loses only in an early interval [0,a], with total
loss probability p. Pair1 cannot lose there. Thereafter pair0's rate is zero;
only pair1 can lose. Pairs2,3 are lossless. Prepare the clock before the late
interval starts, in |+>; its preparation time and error are costs below.

On the late interval u in [0,tau], choose a nonnegative continuous pulse g,
with g(0)=g(tau)=0 and integral g du=pi. Put

    s(u) = (1/pi) integral_0^u g(v)dv,
    eta1(u)=1-q s(u),
    k1(u)=q g(u)/[pi(1-q s(u))],
    theta(u)=2pi s(u).                                 (2)

For 0<p,q<1 the rate is bounded. The sole two-loss flag is {0,1}; its
unnormalized second-loss measure is pq ds=w dtheta/(2pi). There are no
three/four-loss branches. Logical U(T)=-I, and the presecond-loss analysis
axis is n(theta)=(cos theta,-sin theta,0). Thus K2386's uniform-circle law is
preserved by a finite-slew time reparameterization. This requires engineering
the displayed loss rate along with the drive; a constant loss rate does not
produce this measure.

Let both g and the clock coupling below have amplitude cap G and slew cap V,
where G,V are the smaller available caps for the two separate controls. A
triangle or trapezoid of area pi realizes (2) in

    tau_min = 2 sqrt(pi/V),        pi<=G^2/V,
              pi/G+G/V,          pi>=G^2/V.            (3)

It is shortest within the stipulated nonnegative zero-endpoint pulse class:
any such pulse lies below min(Vu,V(tau-u),G); integration gives (3).
The maximal pair1 rate is at most qG/[pi(1-q)]. This prices the newly supplied
number-selective coupling, which transparent code controls alone do not grant.

## A joint Markov instrument, with no hidden timing observation

Let N1 be pair1 occupation: eigenvalue1 on either encoded rail bit and0 on
vacuum. Couple a fresh clock a by

    H_meter(u)=-g(u) N1 tensor Z_a.                    (4)

Take all physical loss operators L_(i,b)=sqrt(k_i)|vac><b| on pair i tensor
identity on the clock, b=0,1. Add independent clock dephasing

    L_a=sqrt(gamma(u)/2) I tensor Z_a.                 (5)

These, the physical H_system and (4), define the entire storage/exposure
Lindblad generator. The physical loss rates are stipulated to remain the displayed
Markov rates under the coupling; deriving that assumption from a microscopic bath
is a separate physical requirement. In particular the clock is not an oracle attached to an
endpoint channel.

N1 commutes with every transparent-control term, is the identity on both rail
bits, and is scalar on each occupied/vacuum trajectory sector. The effective
no-jump physical attenuation is scalar within each such sector because the
two rail rates match. The Markov bath carries orthogonal time and rail records, which are traced;
the argument uses their trajectory instrument, not a coherent sum of distinct
paths. Consequently every physical jump/no-jump trajectory
factors into the original physical trajectory and a clock rotation. If pair1
loses at u, the clock's accumulated angle is -2 integral_0^u g=-theta(u);
its coupling vanishes after that loss. If pair1 survives, its angle is -2pi,
which is a global phase. Independent dephasing commutes with all these clock
rotations. Tracing the clock therefore returns exactly the K2383 physical
channel, including coherences and arbitrary references. Bit blindness is
essential; replacing N1 by a single-rail projector would entangle the clock
with the logical rail and invalidates this factorization.

At readout after total pointer dephasing exposure Gamma, let nu=exp(-Gamma).
The conditional clock state is

    A_theta = [I+nu(cos theta X_a-sin theta Y_a)]/2.   (6)

This includes all clock dephasing during exposure and any commuting waiting
interval before readout. Imperfect initial equatorial visibility nu0 multiplies
nu. Noise during noncommuting preparation/recovery gates is a separate cost;
it cannot be folded into Gamma without another proof.

For the two-loss branch K2380 extraction leaves an X-classical survivor sign
z=+1 or-1. For input rho=(I+r.sigma)/2 the unnormalized joint instrument is

    J_z(rho)=w integral [(1+z n(theta).r)/2] A_theta dtheta/(2pi)
            =w/4 [I+z nu(r_x X_a+r_y Y_a)/2].        (7)

Both signs have probability w/2 independent of rho; J is CP because its first
line is a positive measure-and-prepare integral. All no/two/single-loss flags
are retained; zero/one-loss branches remain perfectly recoverable and have
total weight1-w. Normalization is therefore exact, with no postselection.

## Optimal classical timing readout

Write each clock POVM effect E_y=(alpha_y I+b_y.sigma)/2. Positivity gives
||b_y||<=alpha_y and completeness gives sum alpha_y=2, sum b_y=0. Let
b_parallel be its xy projection. From (6), the outcome kernel is

    c_y(theta)=(alpha_y+nu b_y.n(theta))/2.

Its unnormalized time mass and vector moment are

    p_y=w alpha_y/2,
    m_y=w nu b_parallel/4.                           (8)

The K2383 per-record Bell bound applies directly, giving maximum complete Bell
overlap (1-w)+(w+sum_y||m_y||)/4. Since sum_y||b_parallel||<=2,
sum_y||m_y||<=w nu/2. Equatorial rank-one projective measurement saturates it.
The resulting complete channel is a Pauli mixture whose Bell-complement
weight is w(3-nu/2)/4, so the Bell lower bound is also the half-diamond upper
bound. This proves the first optimum in (1), not merely its fidelity.

For X readout y=+/- the survivor can be retained; apply Z to it iff y=-.
No arbitrary optimal-axis synthesis is needed in this fixture. A binary
readout flip with probability epsilon replaces nu by nu|1-2epsilon| in this
attained error after optimal relabeling. At epsilon=1/2 the readout conveys no
usable timing information. For arbitrary POVM readout noise use its actual
classical stochastic map; do not assume the binary formula generalizes.

If a POVM is chosen after learning z, use effects E_(y|z) separately. The
unnormalized branch probabilities have Bloch coefficients z w nu b/8;
optimizing prepared output vectors and summing ||b_parallel||<=2 for each z
again yields Bell overlap at most (1+nu/2)/4 on the normalized two-loss branch.
A coherent joint operation is not such a classical timing measurement.

## Retaining the pointer changes the instrument and improves recovery

In (7), apply Z_a conditional on z=-; Z flips both equatorial components.
Discard the sign and use the clock as output. This yields the normalized
unital Pauli channel

    T_nu: r -> (nu r_x/2, nu r_y/2, 0),
    q_I=(1+nu)/4, q_X=q_Y=1/4, q_Z=(1-nu)/4.         (9)

At nu=1 this is still entanglement breaking, with half-diamond error1/2 on the
two-loss branch. It achieves the same optimum as an idle two-erasure branch;
it does not achieve identity or restore erased quantum information.

For completeness, this recovery is optimal over ALL CPTP decoders. Conditional
sign correction is invertible and reduces each equal-weight sign branch to
T_nu. For any subsequent CPTP map R with Kraus operators R_j, define

    f_P=(1/4) sum_j |tr(R_j P)|^2, P in {I,X,Y,Z}.

The f_P are nonnegative and sum to1 by Pauli Hilbert-Schmidt completeness and
sum_j R_j^dagger R_j=I. Bell overlap of R T_nu is sum_P q_P f_P, at most
max_P q_P=q_I. The identity decoder attains it. Allowing different CPTP maps
for the two classical sign sectors cannot improve that bound. Good flags
contribute at most1; thus complete Bell overlap is at most1-w+w q_I.
The achieved complete Pauli channel has matching half-diamond error
w(1-q_I), proving the second formula in (1). No reference-dependent decoder,
coherent bath access or erased-rail readout was used.

For p=q=1/2 and nu=1, the no-clock error is3/16, this classical clock gives5/32, and the coherent clock gives1/8. K2386's ideal two-bin detector gives (3-2/pi)/16, which is smaller than5/32: the new noisy classical clock is not a better two-label encoder. Its explicit apparatus and the separate coherent-access result are the gains.

This is compatible with K2386's impossibility of removing the finite-classical-
label circle penalty. A retained quantum pointer is not a classical B-label
record. Classical environment-assisted recovery is broader literature context
([Gregoratti and Werner](https://arxiv.org/abs/quant-ph/0209025)); these supplied
channel specializations are proved here without a novelty claim.

## A stronger noiseless endpoint without uniform-angle rate engineering

Keep the same endpoint U(T)=-I and the same bit-blind pointer phase tracking,
but let mu be ANY input-independent normalized distribution of the second-loss
angle for the sole two-loss flag. Its mass is still w; its density need not be
uniform. Define in the xy plane

    m=integral n(theta) dmu,
    M=integral n(theta)n(theta)^T dmu.                (14)

M is positive semidefinite with trace1. The joint instrument becomes

    J_z(rho)=w/4[(1+z m.r)I+nu(m+z M r).sigma].      (15)

In contrast to the uniform case, the sign probabilities can now depend on the
input. Nevertheless the same sign-controlled Z flips the entire pointer plane;
after summing the signs the mean m cancels, leaving

    T_(mu,nu): r -> nu M r
             =nu integral D_n(rho)dmu+(1-nu)Depol(rho). (16)

Here D_n=(id+Ad_(n.sigma))/2 and M acts as zero on the perpendicular axis.
The displayed decoder's half-diamond error is exactly (3-nu)/4 on the
normalized two-loss branch: it is a mixture of identity of weight(1+nu)/4
and traceless-unitary errors, and a Bell input attains the complement weight.
This proves an ACHIEVABLE complete error w(3-nu)/4 for every such mu.

At nu=1 this is also the all-CPTP optimum, namely w/2. Indeed the original
integral instrument is entanglement breaking: each theta,z term measures the
input effect (I+z n.sigma)/2 and prepares a pointer state with a classical
sign. Its output-reference Bell overlap after any local recovery is at most1/2.
Together with the good flags this yields the matching complete lower bound.
Thus a noiseless coherent pointer reaches the idle erasure floor for arbitrary
loss-angle weighting, including the angle laws produced by ordinary supplied
bounded rates. The uniform construction supplies the two optima in(1); the known-law
results below relax it for coherent access. It is not required for this noiseless endpoint.

There is also an exact noisy worst-case result. Fix w and nu and allow all
input-independent angle laws mu, including the physically supplied uniform
fixture. The same decoder in(16) requires no knowledge of mu and has the same
error for each law. The uniform law supplies the matching lower bound for
every decoder by(9). Consequently

    inf_(R independent of mu) sup_mu e(R I_mu,id)=w(3-nu)/4.             (17)

This is the robust minimax value for the declared family, not a pointwise
optimality theorem for each nonuniform law. A smaller family that excludes the
uniform law needs its own lower bound. It makes the noisy decoder useful when
the angle distribution is unknown, without assigning GU or hardware credit.

For nu<1, (16) is not generally optimal. A constant loss axis gives the
survivor a complete dephased logical component; ignoring the pointer already
attains w/2, even when nu=0. This countercontrol forbids promoting the uniform
noisy optimum to arbitrary mu. Abstract atomic angle measures are valid
mathematical controls; their physical realization must be supplied separately.
Some atoms can arise from finite-duration constant-axis plateaus, without
instantaneous loss impulses. A different drive endpoint requires the
corresponding final logical U(T) correction and its costs. Nothing here
licenses unpriced arbitrary three-dimensional pointer steering: the fixed Z
sign correction works because the axes lie in one plane.

## Useful followthrough: speed, aliasing and complete implementation costs

With constant pointer dephasing gamma>0, nu=exp(-gamma tau) before extra waiting.
Equation(3) therefore gives the best visibility and both exact errors within
the stipulated pulse class and rate co-design. At any finite gamma tau>0 the
coherent error is strictly above w/2. At gamma=0 it reaches that floor even
with finite amplitude and slew. This is a concrete control/decoherence
tradeoff rather than an assumed error budget for an undefined instrument.

Faster pointer winding is not automatically better: replace (4) by
-m g N1 Z_a for integer m. If m=0 or |m|>=2, the first angular harmonic of
A_theta vanishes against n(theta), and the joint instrument (7) becomes
input-independent. Both resource classes then have two-loss error3/4.
m=-1 retains the first harmonic with a reflection, removable on the output
by a known Pauli rotation. A known constant phase offset is removable by a
known rotation; averaging an unknown uniformly random offset destroys the
first harmonic. These are changed-instrument controls, not evidence against
(1).

The following is an explicit sufficient implementation account. It assumes
K2380's supplied X,H,CX/syndrome alphabet AND the separate coupling (4).
Clock preparation uses one H on a fresh zero qubit; that preparation and its
waiting error are charged. The original flag measurements still number four.
In the two-loss branch, K2380 uses at most16 gates including extraction and
routing to its output f. Classical X clock readout adds one H and one
measurement; the conditional Z_f can use H X H, adding three gates. Thus the
old overall21-gate recovery maximum still bounds the classical case, with
at most five measurements. Coherent recovery uses H_f to turn its X sign
into a computational bit, controlled-Z_(f,a)=H_a CX_(f,a) H_a, then three-CX
SWAP_(f,a) to route the clock state to f: seven additional gates, so a23-gate
recovery maximum and four measurements suffice. The original zero/one-loss
branches discard the unused clock and retain their existing decoder.

With a supplied gate-time bound t_g, measurement time t_m, and feedback bound
t_fb, padded recovery durations can therefore be taken as

    T_rec,class <=21 t_g+5 t_m+t_fb,
    T_rec,coh   <=23 t_g+4 t_m+t_fb.                 (10)

Add one clock-preparation gate, its fresh-qubit/reset cost, and the exposure
(3). The clock coupling is concurrent with the late physical drive; do not
charge its duration twice. Classical readout needs one classical bit storage;
coherent recovery instead needs one clock-qubit storage and coherent output
routing through (10). K2380's12-gate encoder, its errors and all syndrome,
preparation, gate, feedback and rate costs remain. Equations(1) already include
storage loss and pointer dephasing; do not count those intervals again as
new storage errors. Finite-gate noise and extra physical loss during recovery
are bounded separately using the SAME expanded apparatus, including the clock.

For a completely specified additional output-noise fixture, apply depolarization
D_d after recovery in a separate padded interval, with 0<=d<=1. The achieved
complete channel is Pauli, so its exact error is

    e_actual=d e_(classical/coherent)+(1-d)3/4.       (11)

If D_d is generated by dot rho=kappa(I tr rho/2-rho), then d=exp(-kappa T).
This is a noise channel on the designated recovered output, not a model of
all physical errors during gate synthesis. Against an ideal no-pointer
baseline e0=3w/4, writing G=e0-e, this explicitly noisy device improves iff

    (1-d)3(1-w)/4 < d G.                             (12)

Here G=w nu/8 for ideal classical readout, or w nu/4 for coherent access.
Equation(12) accounts for degradation of good as well as two-loss branches.
Ignoring good branches gives a false advantage at sufficiently small d.

For a more general implementation, establish a complete-instrument distance
delta from this exact model, including preparation, synthesis, readout,
noncommuting noise, rate and coupling mismatch. Then e_implementation<=e+delta
(or (11)+delta when (11) is included in the reference). To compare actual
baseline and actual pointer implementations use delta_base+delta_pointer<G;
a difference of error bounds does not compare their actual errors.

One direct mismatch certificate on the joint clock+system generator is

    delta <= integral sum_(i,b) |k_(i,b)-k'_(i,b)| du
             + integral |g_meter-g'_meter| du       (13)

plus separately bounded disjoint error sources. Here loss lowering operators
have norm1, the common physical Hamiltonian is fixed, and the second term
bounds the difference in the coefficient of N1 Z_a. Duhamel, CP contractivity
and ||D[L]||_diamond<=2||L||^2 prove (13) for the JOINT instrument; final
measurement and recovery are contractions. A changed physical drive requires
its own Hamiltonian term. This deliberately avoids treating an endpoint-only
physical bound as a record-resolved instrument bound.

## Scope, tests and continuation

Layer0 distinguishes the inherited lost-time physical channel, classical
clock-record instrument, and retained-coherent-clock instrument. They have
different accessible carriers; only explicit maps above transfer results.
Preflight lenses are information resource, trajectory factorization, positivity,
noise ownership and controller cost. Postflight lenses are reference-aware
optimality, first-harmonic aliasing, full-instrument comparison and inherited
claim ceilings. The exact probe checks matrix units, clock sign and channel
moments, complete Pauli probabilities, and changed-instrument countercontrols.
Analytic arguments provide the universal bounds; finite tests do not certify
apparatus realization. Internal review is not external-expert or Lean proof.

The useful next physical condition is a calibrated number-selective, rail-blind
coupling and a measured joint record/clock instrument with all costs above.
A further mathematical extension can optimize noisy coherent recovery for a
specified nonuniform trajectory measure; the uniform noisy optimum and the
arbitrary-law noiseless optimum above do not settle that problem. Neither task requires relabeling this conditional apparatus
as a native GU physical quotient.

## Exact noisy recovery for a known aligned-mean angle law

A larger class closes the pointwise noisy question. Choose the first axis along
the mean and assume it is an eigenvector of the second moment:

    m=(a,0), M=diag(lambda,1-lambda),
    0<=a,  a^2<=lambda<=1.                           (18)

The mean can be made nonnegative by naming its axis; m=0 permits any principal
axis. This class includes every zero-mean law and every biased antipodal law.
It is not all nonuniform laws: a mean not aligned with an eigenvector is outside
(18). Its moments are realizable. For lambda>0 choose the four unit axes
(+-sqrt(lambda),+-sqrt(1-lambda)), with an independent symmetric second sign
and first-sign mean a/sqrt(lambda). The limiting lambda0 case has a=0. These
are probability-law constructions, not automatically calibrated loss schedules.

Let A=nu lambda and B=nu(1-lambda). Define

    F(a,lambda,nu)=nu,                         a^2<=nu^2 lambda,
      a sqrt[1+B^2/(a^2-A^2)],                 a^2>nu^2 lambda. (19)

The second branch has a strictly positive denominator. The exact complete
all-CPTP optimum for the declared instrument is

    e_aligned=w[3-F(a,lambda,nu)]/4.                 (20)

This includes nu0 (F=a), a0 (F=nu), and lambda1
(F=max(a,nu)). At a=nu=0 use the first branch. These are ideal recovery
optima for a specified noisy clock instrument; additional recovery synthesis
and reset costs below are not optimized by(19).

### Why this is an all-CPTP optimization

The original sign block(15), before sign correction, is

    J_z(rho)=1/4[(1+z a r_x)I
                +nu(a+z lambda r_x)X
                +z nu(1-lambda)r_y Y].             (21)

The weight w is omitted in this local calculation. The original blocks obey
J_-(rho)=J_+(Z rho Z). Bell overlap is invariant under conjugating both the
input and the output by the same Pauli. Thus averaging two candidate decoder
maps with their corresponding transformed maps loses no objective, and allows
one map R on both blocks, followed by output Z on the minus block. Equivalently,
after doing the original sign correction first, the two decoders must be
R and Ad_Z R Ad_Z. Applying the same nonunital R after the sign correction
would be a different, generally incorrect decoder.

Further average R with Ad_X R Ad_X. The channel(21) has this covariance, so
this kills translations transverse to X and mixed X/Y or X/Z Bloch entries
without changing the objective. Averaging also with the map having complex-
conjugate Kraus operators kills the remaining Y/Z mixed entries. This is an
average of two CPTP maps, not an implementation of an antiunitary operation.
We may therefore optimize a decoder with translation (t,0,0) and diagonal
Bloch matrix diag(x,y,zeta). Its objective is

    F=a t+A x+B y.                                  (22)

The two sign outputs together are unital with diagonal Bloch entries
(a t+A x, B y, 0). Translations from the two sign sectors cancel.

Signs of t,x,y can be made nonnegative without reducing(22): channel Pauli
conjugations flip t alone, x with zeta, or y with zeta as needed. Complete
positivity of this diagonal translated channel is exactly the two Choi-block
conditions, including their diagonal positivity:

    1+-x>=|t|,
    (1+-x)^2>=t^2+(y+-zeta)^2.                     (23)

For fixed nonnegative t,x, the maximum permitted y is

    y=[sqrt((1+x)^2-t^2)+sqrt((1-x)^2-t^2)]/2,
    zeta=[sqrt((1+x)^2-t^2)-sqrt((1-x)^2-t^2)]/2.

Increasing y helps or leaves(22) unchanged. On this boundary y zeta=x and
(1-y^2)(1-zeta^2)=t^2. Write

    y=cos u, zeta=cos v, x=cos u cos v,
    t=sin u sin v,       0<=u<=v<=pi/2.             (24)

If a<A, (22) is at most A+B=nu, attained by the identity decoder.
For a>=A, maximizing over v at fixed u is compatible with v>=u and gives,
with c=cos u,

    max_v F=B c+sqrt[a^2-(a^2-A^2)c^2], 0<=c<=1.   (25)

Let d=a^2-A^2. When d>0 this function is concave, with derivative
B-d c/sqrt(a^2-d c^2). Its maximum is at c1 iff d<=AB, equivalent to
 a^2<=nu^2 lambda. Otherwise the interior solution is

    c*=a B/sqrt[d(d+B^2)],
    cos v*=AB/d,                                   (26)

and its value is the second branch of(19). Formula(26) also covers B0 by
c*=cos v*=0; the decoder then prepares the positive-X state before the
sign-conditioned output flip. The d0 and zero-parameter cases are the
endpoint branches specified above. This derives the maximum over all CPTP
maps, without relying on a numerical optimizer or a restricted decoder ansatz.

The attained sign-paired channel is unital and diagonal, with nonnegative
first and second entries whose sum is F and third entry zero. As a CPTP map
it is a Pauli mixture with identity weight(1+F)/4. The Bell lower bound therefore
matches its half-diamond upper bound. Good flags add weight1-w of the identity,
proving(20).

### Concrete recovery and costs

The boundary decoder is an explicit two-Kraus channel. In coordinates with
translation along the third axis, set alpha=(v-u)/2, beta=(v+u)/2 and use

    K0=diag(cos alpha,cos beta),
    K1=[[0,sin beta],[sin alpha,0]].                 (27)

Their squared sum is I, and the Bloch map has translation sin u sin v along
the third axis and contractions (cos u,cos v,cos u cos v). A fixed cyclic
axis rotation puts it in the convention of(24). One fresh qubit supplies an
isometry |0> -> cos alpha|0,0>+sin alpha|1,1>,
|1> -> cos beta|1,0>+sin beta|0,1>, followed by tracing the ancilla. For example
this extends to the unitary

    exp{-i[(v/2) X tensor Y-(u/2) Y tensor X]},       (28)

on the data and a zero ancilla; the two Pauli products commute. This is a
finite conditional construction, not an available free gate. It adds a fresh
reset qubit, calibrated angle-dependent operations and basis rotations. The
23-gate budget for the previous identity-pointer decoder does not automatically
cover it. Evaluate its complete synthesis/noise/reset cost using the existing
instrument error accounting before claiming an actual-device improvement.
Original sign correction follows R in this implementation.

A genuinely interior exact fixture has a=nu=lambda=1/2, realizable as an
angle law with masses1/2 at+X and1/4 at each of+Y,-Y. The optimizer is

    t=4/(3sqrt3), x=1/(3sqrt3), y=1/sqrt3, zeta=1/3,
    F=1/sqrt3 > max(a,nu)=1/2.                      (29)

Both Choi determinants vanish and their diagonals are nonnegative. Thus
combining known angle imbalance and clock coherence can strictly beat BOTH
ignoring the clock and using the distribution-robust identity-pointer decoder.
The improved ideal complete error is w(3-1/sqrt3)/4. A finite plateau-based
loss schedule can realize the three angle masses, but its extra duration,
physical rates and clock dephasing must be priced; the moment law alone is
not such a timing budget.

### Exact corollaries and failure-capable controls

For m0, (19) gives F=nu for any second-moment anisotropy. Equivalently the
sign-corrected channel has Pauli weights(1+nu)/4,
[1+nu(2lambda-1)]/4, [1-nu(2lambda-1)]/4 and(1-nu)/4;
its identity weight is maximal, giving the independent Parseval check.

For axes+X,-X with probabilities(1+a)/2,(1-a)/2, lambda1 gives
F=max(|a|,nu), allowing either sign convention for a. The joint carrier is
commuting and its clock-X readout probabilities are

    P(z,y|rho)=[1+y nu a+z(a+y nu)r_x]/4.

An arbitrary decoder only assigns output states to these four outcomes. Its
Bloch-matrix trace is at most sum_(z,y)|z(a+y nu)/4|=max(|a|,nu), attained by
the X output sign z sign(a+y nu). Thus coherent retention gives no extra
advantage in this particular commuting subclass. At |a|>nu ignoring the clock
is optimal; at nu>|a| the product of survivor and clock signs is optimal.
The two-point law can use finite-duration theta0 and theta pi loss plateaus:
for total loss probability q their hazard integrals are
-log[1-q(1+a)/2] and -log[(1-q)/(1-q(1+a)/2)]. Loss-free finite-slew phase
segments complete the circle. Plateau durations count in the actual nu.

The tests include the interior fixture, zero visibility, zero mean, antipodal
limits, threshold continuity, the actual Kraus/Choi conditions and an incorrect
sign-correction ordering. The nonaligned-mean case remains a finite qubit
recovery optimization; (19) is not asserted there. Known-law ideal gains must
still survive complete implemented-channel costs and do not change the source
claim ceilings.
