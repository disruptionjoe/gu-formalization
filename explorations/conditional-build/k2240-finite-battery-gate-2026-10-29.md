---
title: "K2240 Finite coherent battery for energy-conserving gate compilation"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite supplied coherent battery and engineered positive autonomous clock approximate fixed-gap qubit gates; no exact finite nonconserving unitary channel, free catalyst, indefinite reuse, gap-ramp implementation, laboratory apparatus or GU realization
scripts:
  - tests/channel-swings/k2240_finite_battery_gate_probe.py
---

# K2240 Finite coherent battery for energy-conserving gate compilation

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`; target `NONE-NOT-A-KILL`.

```gu-typed-objects
result: finite ladder gate lift, reference-uniform error, coherence resource and autonomous compilation
carrier: positive fixed-gap qubits, finite nonnegative equally spaced battery, finite clock and arbitrary retained reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: qubit occupation, integer battery energy and clock position
action_owner: repository-construction -- supplied coherent packet and engineered energy-shell gates
target: approximate gate channel and exact additive-energy conservation MAP-TYPE=intertwiner
```

## Preflight, operative objects and actual increment

The startup prerequisites are owner AGENTS, GEOMETER-VS-PHYSICS-OBJECTS
(T15/T16/T17), comparator routing, Layer 0, current state, research posture,
verification/contribution rules and the path-dependency index. The operative
objects are ordinary positive finite quantum apparatus, not the source's
indefinite geometric form or a derived physical quotient. K2238's clock requires
its gates to commute with the data Hamiltonian. Here an explicit finite battery
turns a supplied fixed-gap qubit gate into such a gate on the enlarged carrier.
K2229's variable-gap reset protocol and K2235's fresh thermal supply remain
different constructions. No source claim, ledger grade, hypothesis vote or
canon changes. These elementary resource-theory constructions and estimates
make no priority or novelty claim; all needed identities are proved below.
Background is Aberg, [Catalytic Coherence](https://arxiv.org/abs/1304.1060),
and Bedkihal, Vaccaro and Barnett, [Comment on Catalytic Coherence](https://arxiv.org/abs/1603.00003).
The latter motivates retaining accumulated correlations explicitly; neither
reference is used as a proof of the finite bounds below.

Preflight compared leaving K2238's noncommuting-gate boundary unchanged,
using an unbounded formal translation reference, and supplying a finite
buffered ladder. The finite ladder is selected because it changes that exact
premise while exposing the coherence, energy range, boundary and reuse costs.
Its strongest tempting overclaim is an exactly catalytic finite coherent gate;
Sections 4--7 rule that out and quantify the actual approximation.

## 1. Exact shell lift on a finite nonnegative battery

Let H_S=E|1><1|, E>0. Let B have basis |n>, 0<=n<=N, and
H_B=E sum_n n|n><n|. Fix a supplied two-by-two unitary U=(U_ij), i,j in{0,1}.
For every total-occupation shell k=1,...,N, define V_U to be the matrix U in
ordered basis (|0,k>, |1,k-1>). On the one-dimensional edge shells |0,0>
and |1,N>, define V_U as identity. The shells are mutually orthogonal and
exhaust S tensor B, so V_U is unitary and

    [V_U,H_S+H_B]=0.                                           (1)

No cyclic boundary identification is used. The battery spectrum is finite and
bounded below. On every |j,n> with 1<=n<=N-1,

    V_U|j,n> = sum_i U_ij |i,n+j-i>.                           (2)

The sign j-i matters: exciting S lowers B by one. Globally replacing that
translation by a cyclic shift gives a unitary but violates (1) at the wrap.
Using U tensor I preserves neither (1) nor the energy budget for noncommuting U.

Supply the pure coherent packet

    |b,L> = L^(-1/2) sum_(n=b)^(b+L-1) |n>,
    L>=2, b>=1, b+L-1<=N-1.                                  (3)

It is initially independent of S and every retained reference F. Denote its
one-step translations by |beta_d>, d in{-1,0,1}, with |beta_0>=|b,L>.
The translations are defined only on the supported packet, inside the finite
ladder; no impossible globally unitary semibounded translation is assumed.
Their overlaps are

    <beta_d|beta_e> = max(0,1-|d-e|/L).                        (4)

The global input-state hypothesis is essential. A battery marginal with
uncontrolled correlations is not a channel implementation premise.

## 2. Joint approximation and improved discarded-battery bound

Let J_U map |psi>_SF to V_U(|psi>_SF tensor |beta_0>), with the obvious tensor
ordering, and J_0 map it to (U tensor I_F)|psi> tensor |beta_0>. Write
|psi>=|0>|psi_0>+|1>|psi_1>. Then

    (J_U-J_0)|psi>
      = U_10 |1>|psi_0>(|beta_-1>-|beta_0>)
        + U_01 |0>|psi_1>(|beta_+1>-|beta_0>).                 (5)

The two terms have orthogonal S factors, and unitarity of a two-by-two U gives
s:=|U_01|=|U_10|. Since each translated difference has squared norm2/L,

    ||J_U-J_0|| = s sqrt(2/L).                               (6)

This is also true after tensoring any reference. The half trace distance
between normalized pure states is at most their vector distance; purifying
mixed inputs and tracing the purifying reference proves

    (1/2)||Gamma_U - (Ad_U tensor preparation_beta)||_diamond
        <= min(1, s sqrt(2/L)),                              (7)

where Gamma_U retains B. Thus battery disturbance and system-battery
correlations are bounded jointly, not just by a marginal comparison.

There is a sharper sufficient bound if B is discarded. The output battery
levels m=b+1,...,b+L-2 have identical Kraus operator U/sqrt(L). The four
remaining operators, each divided by sqrt(L), are

    m=b-1:      U_10 |1><0|,
    m=b:        diag(U_00,U_11)+U_10|1><0|,
    m=b+L-1:    diag(U_00,U_11)+U_01|0><1|,
    m=b+L:      U_01 |0><1|.                                (8)

For L=2 the interior list is empty, and the four boundary levels are still
distinct. Completeness of the full dilation shows that the four unscaled
operators in (8) have sum K* K =2I; this also follows by expanding U*U=I.
Consequently

    Phi_U = (1-2/L) Ad_U + (2/L) Psi_U,
    Psi_U a CPTP map,
    (1/2)||Phi_U-Ad_U||_diamond <= min(1,2/L).                 (9)

This is a sufficient bound, not the exact diamond norm or a universal optimum.
The full matrix-unit formula is independently useful:

    Phi_U(|j><l|)
      = sum_(i,k) U_ij conjugate(U_kl)
        max(0,1-|(j-i)-(l-k)|/L) |i><k|.                    (10)

Eq.(9) cannot replace (7) for repeated use of the SAME battery: a reduced
channel description has discarded precisely the correlations carried into
later gates. Separate fresh batteries would permit telescoping the 2/L
bounds but consume a new coherent packet at every gate.

## 3. A sine packet improves the retained-battery resource scaling

The flat packet is useful for the exact discarded-channel decomposition but
has abrupt edges. With the same support and one-level margin, put theta=pi/(L+1)
and supply instead

    |eta> = sqrt(2/(L+1)) sum_(j=1)^L sin(j theta)|b+j-1>.     (11)

The elementary sine-square sum gives norm one. Let A be the path adjacency
matrix on L sites. The recurrence sin((j-1)theta)+sin((j+1)theta)
=2 cos(theta) sin(j theta), with zero endpoints, gives

    <eta|T_+ eta> = cos(theta),
    d_eta := ||T_+ eta-eta|| = ||T_- eta-eta||
      = 2 sin(theta/2) <= pi/(L+1).                          (12)

Here T_+/- again denote translations of the supported vector inside B.
Replacing the flat packet in (5) by eta proves the EXACT operator-norm
identity ||J_U-J_0||=s d_eta and the joint half-diamond upper bound s d_eta.
No constant-Kraus interior exists for this packet, so the flat2/L reduced
bound is not asserted for it. Discarding B always preserves the joint bound.

The sine profile optimizes this particular adjacent-translation defect among
all normalized complex vectors on L consecutive levels. A direct proof avoids
assuming an unproved global optimization: write w_j=sin(j theta)>0, and for
any x in C^L expand

    sum_(j=1)^(L-1) w_j w_(j+1)
       |x_j/w_j-x_(j+1)/w_(j+1)|^2
      = 2 cos(theta) sum_j |x_j|^2
        -2 Re sum_(j=1)^(L-1) conjugate(x_j)x_(j+1).         (13)

The endpoint recurrence makes the diagonal terms exact. Nonnegativity shows
Re< x,T_+ x ><=cos(theta) for normalized x. Equality for L>=2 requires all
x_j/w_j equal. Thus (11), up to global phase, uniquely minimizes the defect
for this support class. This is not an optimal channel-diamond norm, general
battery protocol, energy distribution or thermodynamic preparation theorem.

The sine packet is symmetric, so <H_B>=E[b+(L-1)/2] and
Var(H_B)<=E^2(L-1)^2/4 by its support. Its energy-coherence entropy is
-sum_j p_j log p_j, p_j=2 sin^2(j theta)/(L+1), not log L except at L=2.
The packet's purity, phases and width remain supplied resources. The remaining
flat-specific exact formulas explicitly retain the symbol |b,L>.

## 4. Energy statistics and coherence are separate supplied resources

For (3),

    <H_B> = E[b+(L-1)/2],
    Var(H_B) = E^2(L^2-1)/12,
    energy range = NE.                                      (14)

Dephasing the packet in the energy basis leaves these energy statistics
unchanged. It changes its relative entropy of energy coherence from log L
to zero: the pure packet has entropy zero and its dephasing has L equal
nonzero eigenvalues. This reports the prepared state resource; it is neither
minimal preparation work nor a per-gate amount irreversibly consumed.

If an initially independent battery state commutes with H_B, every
energy-preserving joint unitary induces a time-translation covariant channel
on S. Proof: move exp(-it(H_S+H_B)) through V, use stationarity of the battery,
and trace B. Therefore |0><0| has an energy-diagonal output. For the supplied
Hadamard target U|0>=(|0>+|1>)/sqrt2, its half trace distance from ANY diagonal
state is at least1/2, because the eigenvalues of the difference are
plus/minus sqrt((p-1/2)^2+1/4). Large average battery energy and variance do
not repair missing coherence. More generally the same argument gives the
lower bound |U_00 U_10| on this one input.

Exact conservation gives, for every actual input,

    Delta <H_B> = -Delta <H_S>.                              (15)

By (9), the difference between the actual supplied battery energy transfer
and the target system energy increase is at most E min(1,2/L). This uses the
spectral RANGE E of H_S and half trace distance, not ||H_B|| times a
mistaken claim of work convergence. For the input |0>, the excitation
probability is exactly |U_10|^2 even at finite L, so the mean battery decrease
is exactly E|U_10|^2; the approximation defect is in coherence. No entropy
sink, temperature or thermal free-energy optimum is supplied by this battery.

## 5. Exact all-input nonconserving unitary implementation is impossible here

A broader finite-energy statement clarifies the approximation. Let S be
finite with fixed H_S, let a finite B start in an arbitrary fixed state sigma_B
independent of S, and let V commute with H_S+H_B. If the reduced channel on S
is exactly Ad_U on ALL inputs, then [U,H_S]=0.

Proof: purify sigma_B with an untouched F. The resulting Stinespring isometry
for a unitary channel must have the form |psi> -> U|psi> tensor |eta>_BF
with one fixed |eta>. To see this directly, pure outputs for basis inputs
force product vectors; preservation of every basis superposition forces all
environment vectors to be the same up to phases absorbed into U. Hence the
battery's final energy is independent of |psi>. Energy conservation implies

    <psi|(U*H_SU-H_S)|psi> = c

for all normalized |psi>, so U*H_SU-H_S=cI. Its finite-dimensional trace
vanishes, whence c=0. The argument allows battery consumption and final
correlations in principle; an EXACT all-input unitary channel itself forces
the requisite decoupling. It does not forbid exact action on one known input,
energy-preserving gates, approximate gates with growing resources, an
external control, or formal references whose energy expectations are undefined.

Thus (7)--(9) must not be promoted to an exact universal finite coherent gate.
Nor does a small joint trace error imply negligible mean battery transfer
when the battery range grows: the general energy-continuity bound involves NE.

## 6. Finite reuse with explicit correlation and buffer accounting

Apply m gates U_r to specified fixed-gap qubits (possibly repeatedly to the
same qubit), using the same B. Other qubits and retained history are part of F.
Let s_r=|(U_r)_01|. Choose b>=m and b+L-1<=N-m, for example

    b=m, N=L+2m-1, d_B=L+2m.                                 (16)

Every battery translation path through at most m gates stays in0,...,N.
At each pre-gate step its support is in1,...,N-1, so Eq.(2) applies throughout.
Hybrid replacement of the r-th exact lifted gate by U_r tensor I_B gives

    complete joint half-trace/half-diamond error
      <= min(1, sqrt(2/L) sum_r s_r)
      <= min(1, m sqrt(2/L)).                                (17)

In the hybrid proof the state just before the replaced gate has the ideal
packet independent of the system/reference; all subsequent actual gates are
CPTP and contract the error. Each bound therefore uses (7) legitimately,
without assuming the actual correlated battery becomes fresh again.
The buffer in (16) additionally proves the explicit translation-path
interpretation; it is a convenient sufficient choice, not a minimal
requirement for the hybrid inequality. For a target joint error epsilon,
L>=2m^2/epsilon^2 is sufficient for the flat packet. For the sine packet the
same hybrid proof improves (17) to d_eta sum_r s_r <= pi*m/(L+1), so
L+1>=pi*m/epsilon suffices. The prepared energy mean and range price these
constructions. No indefinite-use or globally optimal scaling theorem follows.

An exact special cancellation prevents an exaggerated degradation claim:
on one and the same qubit, without intervening operations,

    V_(U_m) ... V_(U_1) = V_(U_m ... U_1)                     (18)

on the entire finite carrier, including its identity edge shells. Repeated
inverse gates can restore the battery and undo the operation exactly. This
special group representation is not fresh-channel composition for distinct
qubits or arbitrary intervening maps.

A concrete correlation countercontrol uses X gates on two different qubits
and the same packet with L>=4 and margin2. The input operator |00><11| maps
to |11><00| multiplied by <beta_+2|beta_-2>=1-4/L. Fresh independent packets
would instead multiply it by (1-2/L)^2. The difference4/L^2 is nonzero.
For the physical input (|00>+|11>)/sqrt2 the reduced output density matrices
therefore differ by half trace distance2/L^2. Battery reuse changes the joint
channel even though each isolated X channel has the advertised one-use bound.

## 7. K2238 now compiles the enlarged energy-preserving circuit

Take data D to comprise all operated qubits and B, with H_D the sum of their
nonnegative fixed-gap Hamiltonians. Each V_(U_r) commutes with H_D. Feed these
exact gates, followed by R identity gates, into K2238's clock with
M=m+R, clock dimension M+1 and g>0:

    H = I_C tensor H_D + gM I
       + g sum_(k=0)^(M-1) sqrt((k+1)(M-k))
         (|k+1><k| tensor gate_(k+1) + h.c.).                 (19)

The K2238 gauge proof applies unchanged: H>=0, the programmed term has
spectrum0,2g,...,2gM, and it commutes with H_D. At T=pi/(2g), the exact
endpoint is the lifted circuit followed by exp(-iT H_D), with clock |M>.
After discarding the clock, at t=T+delta its half-diamond deviation from the
same-time free-drifting completed lifted circuit is at most

    epsilon_clock <= min(1, C(M,R+1)(g delta)^(2R+2)).        (20)

Combining the reuse bound and (20) gives a reference-uniform joint
qubits+battery error at most epsilon_clock+d_packet sum s_r, capped at1,
where d_packet=sqrt(2/L) for the flat packet and d_eta for the sine packet. The ideal battery here
is exp(-it H_B)|beta_0>, and the ideal qubit circuit is followed by its
exp(-it H_S,total) free evolution. Calling the battery unchanged in the
Schrodinger picture would be false. An interaction-picture gate is obtained
by declaring this known free drift, or by programming a compensating
energy-commuting phase. A fixed-time target across a window needs its own
free-drift error, as K2238 already states.

For m=2,R=2,M=4, take the sine packet with L=629,b=2,N=632 and
|g delta|<=1/100. The sufficient joint battery/circuit error is

    2*pi/630 < (44/7)/630 = 22/2205 < 1/100,

using pi<22/7. The clock error is <=4*10^-12, and exact rational arithmetic gives
22/2205+4/10^12<1/100. Thus complete error is <1/100 relative to the
same-time free-drifting target. Battery
dimension is633, mean energy316E, variance at most
(628^2/4)E^2=98596E^2; no exact variance is claimed. Clock dimension
is5, bandwidth8g, mean programmed energy4g and variance4g^2. This is an
explicit sufficient finite consumer, not a practical or globally optimal
resource claim. The flat packet would require L=80000 for the same simple
two-gate joint bound, illustrating why packet shape matters. No large Hilbert
matrix is constructed by the probe; resource reporting uses exact rational
arithmetic and the written trigonometric inequalities.

The clock removes supplied per-gate switching during this finite circuit,
not initialization, engineering, readout or recycling. At2T it reverses the
circuit as before; no permanent halt appears. K2229's externally changed
gaps, unequal-gap Gibbs bank, continuum detector operations and arbitrary
adaptive controls are not compiled by a fixed equal-spacing qubit ladder.
A gap-control register, matching energy offsets and its own initialization
would require a new explicit construction. K2235's fresh-Gibbs and finite
entropy-sink bounds are unchanged; coherent work storage is not bath renewal.

## Postflight, falsifiers and reproduction

The strongest counterconstructions are explicitly retained: energy-diagonal
stock has the same energy statistics but fails the coherent gate; cyclic
translation makes a unitary while breaking energy conservation; inverse gates
on one qubit can restore the packet; distinct-qubit reuse carries correlations;
and exact all-input unitary action is incompatible with nonconservation for a
finite independent battery. These distinguish actual resource costs from
one-sided no-go rhetoric. The weakest seam is substituting the reduced2/L
bound into a correlated repeated-use argument; (17) instead uses the joint
Stinespring bound.

The finite probe checks rational unitary blocks, all four qubit matrix units,
Gram overlaps, Kraus completeness, shell-energy conservation, exact group
composition, reuse correlations and the explicit consumer. Its fault cases
change a gate, gap, initial coherence, initial support, boundary translation,
reuse resource or composition order and run the same predicates. Finite checks
are not proofs for arbitrary references or dimensions; those proofs are
Sections1--7. The certificate binds this note, probe and K2238/K2235/K2229.
Run `python tests/channel-swings/k2240_finite_battery_gate_probe.py`;
`--write` refreshes its certificate after review. No laboratory, proof-assistant,
external-expert, source-action, physical-recovery or novelty certification.

Independent internal mathematical review checked the actual note and code: finite-shell
conservation, boundary Kraus decomposition, sine optimality, exact-unitary
obstruction, correlated reuse and same-time clock target. It found no blocking
mathematical issue. Serialized native exact controls pass; this is internal
conditional acceptance, not external certification. The next useful construction is a
specified finite gap-control register and commensurate-energy battery circuit
for the variable-gap reset. It is not supplied by relabeling this fixed-gap
gate or by the now-proved improvement in packet shape.
