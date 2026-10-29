---
title: "K2241 Complex canonical-mode detector compilation on a causal finite network"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite oscillator gate network; no retained-drift continuum local apparatus or GU realization
scripts:
  - tests/channel-swings/k2241_local_mode_detector_network_probe.py
---

# K2241 Complex canonical-mode detector compilation on a causal finite network

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complex finite canonical-mode active compilation with finite spectral detector error and causal depth
carrier: M site oscillators with full infinite bosonic Fock space, finite record and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form, canonical CCR and supplied positive free-energy form ON=declared_carrier
real_structure: real site quadratures, complex coefficients and Hilbert adjoint
grading: oscillator occupation and record outcome; not chirality
action_owner: repository-construction -- externally supplied finite-duration local Gaussian and spectral gates
target: complete recorded channel on a fixed canonical mode MAP-TYPE=intertwiner
```

## Preflight: the nonduplicated question

K2225 already constructs adjacent gather/process/ungather for a real canonical
smear with positive additive controls and retained finite-chain drift. Merely
restating that construction would add nothing. K2228 treats a more general
Bogoliubov mode with direct nonlocal controls. K2234/K2237 quantify what a
causal replacement cannot do before communication. Here the new finite-network
construction handles arbitrary COMPLEX Bogoliubov coefficient vectors,
identifies the necessary second active mode, and couples the exact compiler
to a finite-rank spectral approximation and an exact graph latency bound.

Layer0 distinguishes site oscillators from physical KG annihilation modes,
and strict discrete-circuit causal support from continuous finite-range
Hamiltonian dynamics. The latter need not have strict compact propagation.
The actual gate endpoints below are supplied; their strength, duration,
drift compensation and hardware synthesis are assumptions. The theorem does
not retain an uncontrolled KG drift, derive a continuum limit, or implement
K2219's optimum. T11/T15/T16 apply. No source verdict, ledger, L1--L7 candidate,
physical quotient, Born or empirical credit changes.

Standard background: [Braunstein, Squeezing as an irreducible resource](https://arxiv.org/abs/quant-ph/9904002) establishes the Bloch--Messiah passive/squeeze decomposition. The normal form below is proved directly for the one output mode and is not claimed as a new general Gaussian synthesis theorem.

## 1. An explicit two-active-mode normal form

Use the coefficient convention

    b = sum_j (u_j a_j + v_j a_j^*),
    ||u||²-||v||²=1,       n=||v||²,       m=sum_j u_j v_j.

The product in m is BILINEAR, not a Hermitian inner product. Set

    nu0=sqrt((n+1/2)²-|m|²),
    tanh(2r)=2|m|/(2n+1),  r>=0,
    phi=arg m (phi=0 when m=0),
    sinh²t=nu0-1/2,        t>=0.

Cauchy--Schwarz gives |m|²<=n(n+1); hence nu0>=1/2 and the
argument of tanh is strictly below one. All parameters are finite. Put

    d=cosh(r)b-exp(i phi)sinh(r)b*,
    u'=cosh(r)u-exp(i phi)sinh(r)bar(v),
    v'=cosh(r)v-exp(i phi)sinh(r)bar(u).

Direct expansion gives

    u' dot v'=0, ||v'||²=nu0-1/2=sinh²t,
    ||u'||²=cosh²t, d=cosh(t)A+sinh(t)B*,
    b=cosh(r)d+exp(i phi)sinh(r)d*.                         (1)

Here A=(u' dot a)/cosh(t) and, for t>0,
B=(bar(v') dot a)/sinh(t). They are orthogonal physical modes:
[A,A*]=[B,B*]=1 and [A,B*]=u' dot v'/(cosh(t)sinh(t))=0.
For t=0 use only A; no auxiliary B is needed. In particular M=1 always
has t=0. These are genuine field modes, not a declaration that b's vacuum
is the physical vacuum. The physical vacuum has <b*b>=n and <bb>=m.

For clarity, the cancellation in (1) is
u' dot v'=exp(i phi)[|m|cosh(2r)-(n+1/2)sinh(2r)]=0.
The occupancy is
||v'||²=(n+1/2)cosh(2r)-|m|sinh(2r)-1/2=nu0-1/2.

Let a passive P gather A,B to sites 1,2, so P* a1 P=A and
P* a2 P=B. Let a two-mode squeeze T satisfy
T* a1 T=cosh(t)a1+sinh(t)a2*, and let an onsite phase-oriented squeeze R
satisfy R* a1 R=cosh(r)a1+exp(i phi)sinh(r)a1*.
Then the collection unitary is U=R T P and

    U* a1 U=b.                                             (2)

Finite-mode metaplectic implementers exist on the complete Fock space;
phases cancel from the channels. No finite occupation truncation is used
in (1)--(2). The order R T P is essential.

### Why passive collection followed by one onsite squeeze is insufficient

Such a circuit could only produce b=C A+z S A*, so
|m|²=n(n+1), equivalently nu0=1/2. Conversely this equality sets t=0
in (1) and that architecture suffices. Therefore nu0>1/2 is an EXACT
obstruction to that restricted architecture, not to Gaussian compilation.
The two-mode squeeze supplies its constructive repair. A particularly simple
counterexample is b=(5/3)a1+(4/3)a2*: n=16/9, m=0, nu0=41/18.
Dropping the creation term or treating arbitrary u,v as one passive mode
changes both the target number operator and the vacuum statistics.

## 2. Adjacent gate compilation and complete target

On an M-site path, any two orthonormal coefficient rows can be gathered by
at most (M-1)+(M-2)=2M-3 adjacent complex Givens rotations for M>=2.
Eliminate the first row from site M toward site1. Unitarity then makes the
second row zero at site1; eliminate it within sites2,...,M. Onsite phases
can be absorbed in the two-site gates except for one final onsite phase
layer. Thus a safe sequential depth is D_P<=2M-2. The inverse uses the
same depth. This gives an explicit gate count, not an optimal routing claim.
On a connected graph first choose a path covering the supported sites when
available; otherwise routing along a spanning tree gives a separate finite
SWAP overhead and is not bounded by the path formula.

The record starts at site1 independently of the input. A supplied local
instrument has Kraus L_l=S_l sqrt(e_l(n1)), finite outcomes, sum_l e_l(k)=1,
0<=e_l(k)<=1, and finite positive quadrature squeeze factors s_l.
Apply U, that local instrument, then U*. Read or dephase the outcome record
in its designated basis; the recorded channel is classical on that register.
A coherent, unpinched record is a different output specification. Its recorded Kraus maps are

    U* L_l U = S_l(b) sqrt(e_l(b*b)).                        (3)

This includes all untouched field modes and arbitrary reference correlations.
The target is exactly the same b, not a proxy physical annihilation mode.
Outcome feedback need only act at site1 while the mode is collected.
All gates in the collection/inverse collection are Gaussian; nonlinearity
is confined to the local number-dependent record gate.

Assign each adjacent or onsite operation one slot of duration tau>0; permit
parallel operations only on disjoint supports. A complete local instrument
is treated as one supplied onsite operation. Equations(2)--(3) give
D<=2(D_P+2)+1<=4M+1 slots for M>=2. This is an exact **slotted-network**
causal implementation with a specified latency tau D. It is not a theorem
that a whole continuous-time Hamiltonian has an exact light cone at every
intermediate time. Nor does it bound the strength needed to put an arbitrary
squeeze or spectral operation into a slot. Duration must be increased if
hardware strength constraints require it.

## 3. Exact recorded-output latency obstruction

At slot boundaries a depth-D nearest-neighbor circuit's record observable
at site1 pulls back into the graph ball of radius D. This follows by induction
on local gates, also with input-independent entangled apparatus ancillas.
Thus input changes at a site j with dist(1,j)>D cannot alter its outcome law.

Suppose some e_l(k) is nonconstant and (u_j,v_j) is nonzero. A site-j Weyl
unitary changes b by alpha=u_j z+v_j bar(z), where the sign convention for
z is fixed by W_j* a_j W_j=a_j+z. At least one nonzero real line of alpha
is available. If e_l(b*b) were invariant under every such displacement,
it would commute with one nonzero quadrature's Weyl group. Since it also
commutes with exp(i theta b*b), conjugating by rotations gives invariance
under every quadrature Weyl group. Oscillator irreducibility would force
it to be scalar, contrary to the nonconstant effect.

Therefore a site-j intervention changes the target record law for some
state. The difference is a nonzero bounded selfadjoint operator, so density
of finite-particle vectors supplies a finite-mean-energy witness. Its Weyl
translate also has finite energy. Consequently exact implementation of the
complete recorded instrument with record kept at site1 requires

    D >= max_{j:(u_j,v_j) != (0,0)} dist(1,j).               (4)

A constant-effect outcome-squeeze instrument need not satisfy this particular
record bound; field-output signalling is a separate test. Shared randomness
or prior apparatus entanglement does not transmit an unknown input and cannot
bypass (4). Distributed records with only later classical aggregation are a
different output specification. This statement proves necessity, while (3)
proves finite-network sufficiency at an explicit generally larger depth.

## 4. Dimension-independent number and supplied energy bounds

Write N=sum n_j, G=N+1, and Gamma=exp(2(r+t)). Passive P preserves G.
The two-mode squeeze multiplies its two-mode quadratic energy
n1+n2+1 by at most exp(2t); the one-mode squeeze multiplies n1+1/2
by at most exp(2r). Spectator number is positive, so

    U* G U <= Gamma G,    U G U* <= Gamma G.                (5)

This bound also holds at intermediate angles along the stated squeeze paths.
It has no artificial M/2 zero-point term. A finite positive free Hamiltonian
H=dGamma(w), w_min I<=w<=w_max I, supplies
<N>_in<=E/w_min. This is an energy ruler; off-diagonal w is not automatically
local and its drift is not added to the prescribed gate model.

Let R_s=max_l max(s_l,1/s_l). The local instrument has
sum_l L_l* G L_l<=R_s² G: use
S_l*(n1+1/2)S_l<=R_s²(n1+1/2), commute e_l(n1) through n1,
and sum the effects. Spectator expectations remain unchanged. Thus

    <G>_out, and every gate-endpoint prefix <G>, <= Gamma² R_s²(E/w_min+1),
    <H>_out <= w_max[Gamma² R_s²(E/w_min+1)-1].            (6)

These are unconditional mean bounds; a rare outcome can have much larger
conditional energy. They are sufficient resource upper bounds, not necessary
work costs or an optimal physical energy. Gaussian pumps, switching work,
record preparation, clock and reset remain supplied. With bounded-strength
quadratic generators a squeeze of size r or t requires its corresponding
integrated coupling; the gate model does not assign that coupling for free.

For any exact unitary collector satisfying U* a1 U=b, the physical vacuum
Omega has <U Omega,n1 U Omega>=<Omega,b*b Omega>=n. Thus its output
free energy obeys E_collect>=w_min n, independent of how the complementary
modes are completed. This is a necessary endpoint excitation, not total
apparatus work.

For the explicit U=R T P, passive P leaves Omega unchanged; T produces
sinh²t quanta in each of its two output modes. R changes the first-site
occupancy to n and leaves the second unchanged. Spectators stay in vacuum.
Consequently the achieved total vacuum occupation is exactly

    <N>_collect = n+sinh²t = n+nu0-1/2,
    w_min n <= E_collect <= w_max(n+nu0-1/2).              (6a)

For isotropic H=omega0 N the achieved energy is exactly
omega0(n+nu0-1/2). No optimal Gaussian-completion or total-work assertion
is made. The upper formula is evaluated from the compiled Bogoliubov
creation block; its first row is the actual v and its second has norm²
sinh²t. In the complex fixture the necessary unit-frequency energy is
625/144, while the explicit collector uses881/144.

## 5. Finite spectral detector, with a complete-reference error

For the binary case write theta_k=asin sqrt(e_1(k)). Replace the full
number function by the finite-rank operator

    Theta_K=sum_{k=0}^K theta_k |k><k|,                     (7)

on the collected site, and use exp(-i Theta_K tensor sigma_y) with an
initial zero record, followed by outcome-basis readout or pinching after the
controlled squeezes. On k>K this emits outcome0 with unit probability.
It exactly matches the target measurement on k<=K. The same conditional
squeezes and ungather are then applied to both constructions. Equation(7)
is a bounded onsite spectral control of norm<=pi/2 with K+1 supplied levels.
Adding (pi/2)I makes its field-record generator positive without changing
the channel. This is a finite spectral specification, not a claim that
low-degree polynomial or few-photon interactions implement it efficiently.

For an arbitrary reference input rho let p=Tr[rho 1_(b*b>K)]. The gentle
projection estimate ||rho-P rho P||_1<=2sqrt(p), P=1_(b*b<=K), and channel
contractivity show the complete recorded half trace distance is at most
2sqrt(p). Explicitly, the two channels agree on P rho P; their difference
on the remainder has norm at most twice the remainder norm. This remains
valid when the number projection acts only on the field tensor arbitrary
reference. Applying common outcome squeezes and ungather cannot increase it.

A concrete recorded-tail check prevents dropping this factor without proof.
Take a superposition of one admitted low number and one omitted high number,
with high probability p, and the target effect zero on low and one on high.
The default-tail approximation always records zero. In outcome0 the difference
has matrix [[0,-sqrt(p(1-p))],[-sqrt(p(1-p)),-p]]; outcome1 contributes
trace norm p. The complete half trace distance is therefore
(p+sqrt(4p-3p²))/2, equal to (1+sqrt13)/8>sqrt(p) at p=1/4.
This is an actual recorded instrument countercontrol, not an assertion
that the sufficient factor2 is sharp.

Set beta=(||u||+||v||)². The annihilation/creation estimates give

    ||b psi|| <= ||u|| ||N^(1/2)psi||
                +||v|| ||(N+1)^(1/2)psi||,
    <b*b> <= beta <N+1> <= beta(E/w_min+1).

Markov's inequality therefore proves the reference-uniform bound

    delta_E <= min(1, 2sqrt(beta(E/w_min+1)/(K+1))).         (8)

No energy variance or occupation cutoff on the physical input is assumed.
For any epsilon>0, K+1>=4 beta(E/w_min+1)/epsilon² suffices. This is the
cost in programmed spectral levels, not the number of elementary gates or
bandwidth needed to resolve those levels. Unlike a hard truncation of the
whole oscillator, (7) is a valid bounded operation on the entire Fock space.
Replacing the outcome effects this way retains completeness and (6).

If each collected-site operation additionally has complete-reference error
eta on the relevant input energy bound, add eta by channel contractivity.
For multiple approximate gates, use a telescoping sum with the distinct
ideal gate-endpoint prefix bound (6); do not reuse an initial energy budget without transport.

## 6. Exact complex consumer and proposed fault controls

Take orthonormal physical modes
A=(3a1+4i a2)/5, B=(4i a1+3a2)/5. Choose cosh(r)=5/4,
sinh(r)=3/4, cosh(t)=5/3, sinh(t)=4/3, exp(i phi)=i.
Thus r=log2, t=log3 and Gamma=36. Build
b=(5/4)[(5/3)A+(4/3)B*]+(3i/4)[(5/3)A*+(4/3)B].
The exact coefficients are

    u=(9/20, 34i/15),       v=(-7i/12, 2).

They give ||u||²-||v||²=1, n=625/144, m=205i/48,
nu0=41/18, and the canonical desqueezing recovers
u'=(1,4i/3), v'=(-16i/15,4/5).
The two active modes are necessary because nu0>1/2.
Cauchy--Schwarz gives beta<=2(||u||²+||v||²)=697/36<20.
For w_min=w_max=1, E<=1, and K+1=16000,
(8) is strictly below1/10 (indeed delta²<=697/72000).
With supplied s0=2/3,s1=7/5, R_s=3/2, (6) gives
<G>_out<=5832. This loose bound illustrates supplied finite resources,
not efficiency. The path construction uses at most9 slots for M=2;
nonconstant effects require at least1 slot for the site2-to-site1 record.

Exact controls verify coefficient conjugations, CCR, anomalous
covariance cancellation, recovery of both physical modes, gate order,
necessity counterexample, bounds (5)--(8), and support-ball induction on a
finite path. Mathematical faults change bilinear m to a Hermitian
product; omit the conjugation in u'; omit the two-mode squeeze; reverse the
collection order; delete the actual creation coefficient vector; change an adjacent gate to
a nonlocal edge; or omit the last admitted spectral level. A separate exact
recorded-channel counterexample shows that the generic gentle factor2 cannot
be replaced by1: for rare probability p=1/4, the target number-record
measurement and its tail-default approximation have half trace distance
(1+sqrt(13))/8>sqrt(p). This compares actual channels, not an altered
expected reporting constant. Finite checks support this derivation;
they do not prove metaplectic implementation, all-reference bounds or
continuum causal dynamics.

## Hostile postflight and exact ceiling

The strongest overclaim is that (3) solves the continuum causal apparatus
problem. It does not: physical KG a(k) modes are not point-site local, a
finite lattice factorization is a different carrier, and exact supplied
gates do not prove retained-drift or strength-limited implementation. The
finite-energy constants need w_min,w_max and may not survive a continuum
limit. The explicit normal form itself applies to arbitrary finite coefficient
support; it gives no uniform spatial localization of the physical A,B modes
under a continuum identification. K2237's short-time lower bound is untouched.

The strongest counterconstruction to an unjustified one-squeeze compiler
is nu0>1/2. The weakest reproducibility seam is claiming hardware from
finite-rank spectral data: (7) specifies an onsite interaction, not a design
from a restricted experimental Hamiltonian set. To go further one must supply
that set, strength/bandwidth bounds, a localized continuum carrier and drift,
and quantitative error in the SAME target and energy norm. No external-expert,
proof-assistant, novelty or physical-realization certification is claimed.


## Reproduction

Run `python tests/channel-swings/k2241_local_mode_detector_network_probe.py`.
Default execution checks the exact baseline and seven mathematical input
faults, then rejects stale note/probe/dependency hashes in the report.
`--write` refreshes the certificate after integration; `--controls-only`
executes finite controls without reading or writing a certificate. The
operator and channel theorems rely on the written proofs, independently
reviewed internally, rather than finite checks.

Independent internal review checked the actual complex normal form, full recorded
channel, number/energy transport, tail estimate, graph support and probe. It
required explicit record pinching and gate-endpoint qualifiers. The accepted
claim remains conditional finite-network mathematics.
