---
title: "K2065: Position measurement compatibility, interference and Bell resources"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive1408 graph and imported measurement rules; no source-selected apparatus or physical quotient
scripts:
  - tests/channel-swings/k2065_position_measurement_compatibility.py
  - tests/channel-swings/k2065_position_measurement_compatibility_probe.py
---

# K2065: Position measurement compatibility, interference and Bell resources

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
result: common-position-parent Bell limitation with interference and explicit multiplicity measurement extension
carrier: complexified real1408 massive observed graph on R3 or declared torus LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Hilbert metric and imported Born probabilities ON=declared_observed_graph
real_structure: complex Hilbert completion; multiplicity observables not asserted to preserve a source real structure
grading: energy projector, not source chirality or fermionic parity
action_owner: repository-construction -- fixed massive graph inherited from K2060 and K2062
target: compressed position and imported tensor-copy observations MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Scalar postprocessings of one compressed position
POVM are jointly measurable. They cannot violate any Bell inequality when they form
all of one party's settings, even though two explicit such effects do not commute.
The same readout displays phase-dependent interference on normalized positive-energy
torus states. A quantitative bound measures the departure from this setting class
needed for CHSH violation. Constant internal multiplicity observables supply a
concrete extension on this same graph: they attain CHSH magnitude 2 sqrt(2), remain
sector-preserving, and have exact distance 1/2 from the scalar-position class.

This is a measurement-resource distinction, not an exclusion of positive-energy
physics. General common-parent/Bell principles are established. The contribution is
the explicit graph application, witnesses and resource comparison, not a novelty
claim for joint measurability or Bell's inequality.

## 1. Frozen objects and inference limits

Use [K2062](k2062-bounded-local-multiplier-rigidity-2026-10-25.md)'s positive-metric
isometry, Hermitian Clifford generators C1,C2,C3,beta, and

    H(p)=C.p+mu beta, E_p=sqrt(|p|^2+mu^2),
    q(p)=(p,mu)/E_p, P(p)=(I+q(p).Gamma)/2, mu>0.

The Hilbert space is L2(R3,C1408), Hplus=Ran P; each positive fiber has dimension704.
For real measurable 0<=f<=1 let F_f=P M_f P restricted to Hplus. K2062 already owns
normalized position POVM existence and nonprojectivity of nontrivial regions.
Those are inherited, not new results here. Observation pullback in the source is
not identified with this spectral compression.

SC-OP-04 ASSERTS only candidate four-field grammar; SC-OP-05 is UNCERTAIN about an
unselected southeast alternative; SC-META-53 is UNCERTAIN about physical positivity;
SC-META-56 DISAVOWS an odd-action prerequisite. None selects the present projector,
Born rule, tensor copies, apparatus, preparation or multiplicity measurements.
LT-SM8 and LT-GR6b retain their physical quotient and domain debts. The two admitted
interference/Bell anchors constrain a conditional interface; fitting them earns no
prediction or confirmation. Source, ledger v0.263 and canon do not change.

## 2. Common parent and Bell locality

For finitely many settings f_x define, for binary outcome strings a,

    G_a=P M_{product_x f_x^(a_x)(1-f_x)^(1-a_x)} P.

Positivity of the multiplying function implies G_a>=0. The pointwise product
identity gives sum_a G_a=I_Hplus and each marginal sum=F_fx. Thus all these effects
have a joint measurement. More general finite-output stochastic response functions
work identically. The construction needs no commutativity after compression.

Take an imported tensor product Hplus tensor HB and any positive trace-one state
rho. For each parent outcome a, form the positive unnormalized Bob state

    tau_a=Tr_A[(sqrt(G_a) tensor I) rho (sqrt(G_a) tensor I)].

The traces sum to one. Conditional on a, Alice's output for any setting is the
corresponding coordinate (or stochastic response) and Bob's distribution is Born
readout on tau_a/Tr tau_a. Zero-weight outcomes can be assigned arbitrarily. This is
one local hidden-variable model for all the stipulated settings and arbitrary Bob
POVMs. Entanglement and infinite-dimensional Hplus do not evade it; positivity,
trace-class cyclicity and a finite parent suffice.

In particular A_x=2F_fx-I and self-adjoint contractions B0,B1 satisfy

    |Tr rho [A0 tensor(B0+B1)+A1 tensor(B0-B1)]| <= 2.       (1)

For each parent outcome (a,b) in {+1,-1}^2 the conditional Bob expression is one of
+/-2B0 or +/-2B1. Averaging proves (1). A setting-independent preprocessing channel
preserves the parent by its unital positive Heisenberg map. Setting-dependent
preprocessing need not do so. All outcomes must be retained; normalized
postselection changes the experiment.

## 3. Noncommuting effects on the actual massive graph

For k!=0 set A=P M_exp(ik.x) P. Put f=(1+cos(k.x))/2 and g=(1+sin(k.x))/2. Then

    F_f=I/2+(A+A*)/4, F_g=I/2+(A-A*)/(4i),
    [F_f,F_g]=(i/8)[A,A*].                                  (2)

Clifford anticommutation gives the universal sandwich identity

    P(p)P(r)P(p)=[1+q(p).q(r)] P(p)/2.                       (3)

To see it, write Q=q.Gamma, R=r.Gamma, with Q^2=I and QR+RQ=2(q.r)I;
then P R P=(q.r)P, and expand P(I+R)P/2. No dimension-specific fit is used.
In Fourier space A sends psi(p) to P(p)psi(p-k), so

    [A,A*](p)=[q(p).q(p-k)-q(p).q(p+k)] P(p)/2.             (4)

At p=k the bracket is mu/E_k-(2|k|^2+mu^2)/(E_k E_2k)<0: squaring the positive
quantities leaves 4|k|^4>0. Continuity makes it nonzero on an open set, proving a
nonzero L2 operator, rather than a statement at an isolated momentum. With mu=1,
|k|=1, (2) has coefficient i(1/sqrt(2)-3/sqrt(10))/16 at p=k. The four effects
PfgP, Pf(1-g)P, P(1-f)gP and P(1-f)(1-g)P still give their common parent.
Thus noncommutativity alone does not supply Bell-incompatible settings.

## 4. A normalized interference witness

On a three-torus of volume V take nonzero reciprocal-lattice k and unit
u0 in Ran P(0). Put c=(1+mu/E_k)/2 and uk=P(k)u0/sqrt(c). Equation (3) gives
||uk||=1 and u0*uk=sqrt(c). Distinct Fourier modes are orthogonal, so

    psi_phi(x)=[u0+exp(i(k.x+phi)) uk]/sqrt(2V)

is normalized and belongs to Hplus. Its position density is

    ||psi_phi(x)||^2=[1+sqrt(c) cos(k.x+phi)]/V.              (5)

The fringe visibility is sqrt(c), for example 2/sqrt(5) at mu=3,|k|=4.
The parent position measurement therefore detects a coherent relative phase while
remaining Bell-local under the setting restriction. These are distinct tests of
one interface. On R3, plane waves are not normalized states; (5) is expressly a
torus construction, not a distribution passed off as an L2 vector.

## 5. Robust departure from the common-position class

If actual effects E_x satisfy ||E_x-F_fx||<=epsilon_x for x=0,1, set
Delta A_x=2(E_x-F_fx). In addition to the elementary triangle bound
2+4(epsilon0+epsilon1), the CHSH magnitude obeys

    S <= 2+4 sqrt(epsilon0^2+epsilon1^2).                    (6)

Indeed the perturbation factors as the row [Delta A0 tensor I,Delta A1 tensor I]
times the column [I tensor(B0+B1); I tensor(B0-B1)]. The row norm is at most
2 sqrt(epsilon0^2+epsilon1^2); the squared column norm is
2(B0^2+B1^2)<=4I. Combine with (1). Thus every common-position approximation must
have Euclidean error at least (S-2)/4. At S=2sqrt(2), this is
(sqrt(2)-1)/2. This bound is not claimed sharp.

## 6. Constructive same-graph extension and exact distance

The four Clifford generators represent the simple complex algebra Cl4(C)=M4(C),
so a fixed unitary basis identifies C1408=C4 tensor C352. They act as the standard
four-dimensional matrices tensor I352. Consequently Hplus=H_D,+ tensor C352.
As 352=2*176, choose Pauli X,Z on a C2 multiplicity factor and identity on C176.
These constant Hermitian operators commute with H and P. They are legitimate
bounded conditional Hilbert observables, but no source real/T compatibility or
apparatus implementation is inferred.

Take two copies with normalized positive Dirac wavepackets, fixed C176 vectors,
and a singlet of the two multiplicity qubits. Alice Z,X and Bob
-(Z+X)/sqrt(2), -(Z-X)/sqrt(2) give CHSH=2sqrt(2). Complete tensor-local measurement
instruments preserve the other factor's marginal. Thus the positive graph itself
supports this imported extension; the restriction in section2 is a readout class.

Its binary effect E_X=(I+X)/2 has exact distance 1/2 from the scalar-position class:
every F_f has form T_f tensor I352. On the same normalized Dirac packet tensored
with +/-X eigenvectors, F_f has the same expectation t, while E_X has expectations
1 and0. Hence ||E_X-F_f||>=max(|1-t|,|t|)>=1/2. Choosing f=1/2 attains equality.
The same holds for Z. This supplies an explicit measurement resource and its cost,
not merely the statement that an unspecified repair might exist.

## 7. Compatibility does not fix the instrument

For a finite countercontrol let v0=(1,0), v1=(-1/2,sqrt(3)/2),
v2=(-1/2,-sqrt(3)/2), and G_j=(2/3)v_j v_j*. Their sum is I2; the matrix J whose
rows are sqrt(2/3)v_j* is an isometry and G_j=J*|j><j|J, a literal compressed PVM.
F=G0 and G=G1 are compatible binary effects with nonzero commutator norm sqrt(3)/9.
The nonselective binary Lueders channel of F nevertheless gives

    sqrt(F) G sqrt(F)+sqrt(I-F) G sqrt(I-F)-G
       = (sqrt(3)-1) X/6.                                 (7)

The +X state changes its G expectation by this positive amount. This is finite
sequential disturbance, not a massive-graph spatial apparatus or a spacelike signal.
For genuine tensor factors every complete Alice instrument instead obeys
sum_j(K_j* tensor I)(I tensor B)(K_j tensor I)=I tensor B whenever sum_j K_j*K_j=I.
The algebraic no-signalling fact was already used in earlier imported tensor
models; identifying physical spacelike laboratories remains additional work.

## 8. Evidence, prior art and next scientific condition

The producer has57 exact Clifford, sandwich, shift, parent, interference and Bell
controls, with four genuine formula faults. A separate finite implementation has28 controls checking
trine compression/instrument disturbance, deterministic CHSH extrema and complete
versus incomplete tensor instruments. Its controls do not prove a continuum theorem:
sections2-6 provide the mathematical arguments, and K2062 supplies the actual graph.
An independent internal proof review checked signs, positive-measure transfer,
tensor assumptions, robustness and the multiplicity extension. This is no external,
proof-assistant or novelty certification.

The general connection is established in [Wolf, Perez-Garcia and Fernandez,
2009](https://arxiv.org/abs/0905.2998); noncommuting joint-measurement distinctions
also appear in [Andersson, Barnett and Aspect,2005](https://arxiv.org/abs/quant-ph/0509133).
Only their general principle is reused; the calculations above are explicit.
K1892's imported CAR local algebra uses a different16-to4 carrier, and K1038's
quotient tensor instruments do not supply the present apparatus. No transfer is
made from either by a shared name.

A source-facing successor needs a source-compatible independent-dual/real structure,
actual physical state and apparatus/setting implementation, or a constrained
setting-dependent control whose resource is measurable against (6). Repeating
POVM existence, generic noncommutativity, transitionless dynamics or generic
no-signalling would add no new condition. Neither successful calibration nor
failure of one measurement class adjudicates GU.
