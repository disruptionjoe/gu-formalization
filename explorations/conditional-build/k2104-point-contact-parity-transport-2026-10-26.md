---
title: "K2104: Point-contact parity transport and its smooth limit"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, stable massive apparatus, GU verdict or novelty
scripts:
  - tests/channel-swings/k2104_point_contact_parity_transport_probe.py
---

# K2104: Point-contact parity transport and its smooth limit

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
result: conditional mathematical construction and exact scope boundaries
carrier: chiral L2 line with finite memory-pointer internal space LAYER=toy CHIRALITY=N/A
pairing: standard L2 positive metric ON=declared_positive_Hilbert_space
real_structure: ordinary complex conjugation and adjoint, no source-selected reality
grading: number-controlled even memory jumps and bosonic pointer
action_owner: repository-construction -- self-adjoint transmission boundary condition
target: finite-duration point-contact instrument and resolvent convergence MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and object boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. The supplied
positive Hilbert/CAR and apparatus models below are not source operator9.16.
K2021 supplies local R0/R1 without selecting an observed positive algebra,
state or dynamics. LT-SM8/LT-GR6b, source-register, ledger and canon remain
unchanged. Native2+1, total/observed chirality, full20 and K/C accessibility
remain distinct debts. No new substrate pathway, novelty or external
certification is asserted. The calculation supplies a reverse-scaffold
operational constraint or conditional construction, not physical recovery.

## 1. Replace finite interaction zones by actual point contacts

[K2102](k2102-travelling-parity-readout-2026-10-26.md) gives smooth finite-zone
transport. A single point register coupled to a whole zone is not strictly
point-local. This note instead defines a point-contact Hamiltonian by its
domain. It does NOT call a delta distribution a bounded multiplication operator.

Let H0=-iv partial_x on H1(R,C^D), v>0. For contacts x1<x2 choose unitaries

    U_j=exp[-i(pi/2)n_j(I-X)],
    G(x)=I (x<x1), U1 (x1<x<x2), U2 U1 (x>x2).

Define

    H=G H0 G*,  Dom H=G H1(R,C^D).                    (1)

G is unitary multiplication, so H is self-adjoint. Its domain consists of
piecewise H1 functions with transmission traces

    Psi(xj+)=U_j Psi(xj-).                            (2)

It acts as -iv partial_x away from contacts. Boundary current is conserved
because U_j is unitary. This is a genuine mathematical point-contact model
with localized registers; no finite zone simultaneously addresses them.
G is a proof equivalence, NOT a physical instantaneous operation executed
across space.

The exact propagator is

    (exp(-itH)Psi)(x)=G(x)G(x-vt)* Psi(x-vt).          (3)

Its spatial support propagates at speed v; along a characteristic it applies each encountered
jump in causal order. A packet wholly before x1 initially and wholly beyond x2
finally receives U2U1, yielding the full coherent parity instrument of K2102.
Arbitrary references are retained. A pointer local to the outgoing packet is
read only after arrival; (3) supplies no early remote record. Spatial support
propagation and ordered contacts do not by themselves prove a full local-net
no-signalling theorem for arbitrary memory interventions. The diagonal
memory drift can be factored/calibrated as before because it commutes with
all jumps. Noncommuting memory dynamics require their own evolution.

## 2. Smooth approximation on a common Hilbert space

Choose nonnegative smooth kappa_j,e supported in shrinking disjoint intervals
around xj with integral pi v/2. Let

    A_j,e(x)=integral_(-infinity)^x kappa_j,e(y)dy/v,
    G_e(x)=product_j exp[-i n_j A_j,e(x)(I-X)].

Then G_e'=-(i/v)V_e G_e and

    H_e=G_e H0 G_e*=H0+V_e on H1.                    (4)

The G_e derivatives are bounded for each fixed e, though not uniformly as
e->0. G_e agrees with G outside the union E_e of transition zones, whose
length tends to zero. Dominated convergence gives strong G_e->G and likewise
for adjoints, hence strong convergence of propagators for each fixed t. For a
fixed initial packet entirely before the zones and a final translated packet
entirely beyond them, the completed outputs already agree EXACTLY once the
zones are small enough. This is stronger than an asymptotic instrument bound
on that prepared class.

## 3. Norm-resolvent bound, but no norm-dynamics limit

For Im z nonzero, the scalar kernel of R0(z)=(H0-z)^(-1) has modulus
v^(-1) exp[-|Im z||x-y|/v] on one of the two half-lines, and zero on the other.
Thus for an indicator M_E, including D internal coordinates,

    ||M_E R0(z)||_HS² = D |E|/(2v|Im z|),
    ||R0(z) M_E||_HS² = D |E|/(2v|Im z|).             (5)

Since ||G_e-G|| pointwise<=2 and it vanishes outside E_e,

    ||(H_e-z)^(-1)-(H-z)^(-1)||
       <=sqrt(8 D |E_e|/(v|Im z|)).                   (6)

Expand G_e R0 G_e* - G R0 G* into two terms and apply(5). This is genuine
norm-resolvent convergence, not just strong resolvent convergence.

The D factor is unnecessary for the operator norm. Vector-valued
Cauchy--Schwarz on the scalar kernel gives
||R0(z)f(x)|| <= (2v|Im z|)^(-1/2)||f||. Integrate this over E_e
and use ||G_e-G||<=2; each of the two resolvent terms is at most
sqrt(2|E_e|/(v|Im z|)). Thus the sharper dimension-independent bound is

    ||R_e(z)-R(z)|| <= sqrt(8 |E_e|/(v|Im z|)).        (6a)

This is a uniform operator estimate; the Hilbert--Schmidt calculation(5)
remains a separate exact control with its correct D dependence.

It does NOT imply operator-norm convergence of the unitary dynamics at fixed
nonzero t. For one contact at0, fix ONE even nonnegative rho in C-infinity_c(-1,1)
with integral1, and set kappa_e(x)=pi v rho(x/e)/(2e). Take the internal
eigenvector n=1,X=-1. Choose normalized wavepackets
supported on(-e²,-e²/2). Their initial cumulative smooth area tends pi/4,
while the sharp jump has not occurred. For fixed t>0, the final packet has
passed the contact. Sharp phase is -1; smooth accumulated phase tends -i.
Therefore

    liminf_(e->0) ||exp(-itH_e)-exp(-itH)|| >=sqrt2.   (7)

Uniformity fails on inputs concentrating within the shrinking transition
layer. Each fixed L2 input still converges strongly. The finite probe uses a
symmetric polynomial profile as an exact C1 control of this mechanism; the
existence statement above uses a fixed rescaled smooth symmetric profile.
Continuity of its cumulative area at zero suffices. An arbitrary e-dependent
shape can concentrate inside e², so symmetry and support alone are insufficient. No finite sample proves the limit.

## 4. Spectral and physical boundary

Both H and H_e are unitarily equivalent to H0 and have spectrum R. Thus point
locality has not repaired the unbounded-below chiral energy spectrum. The
singular limit also requires ||kappa_e||_infinity growing at least as1/|E_e|:
no fixed amplitude budget produces exact zero-width contacts. It is a different
resource limit from the bounded smooth gate. A semibounded massive mediator,
a physically controlled preparation budget, and an actual local interface from the massive sea
to the registers remain unconstructed. This result cannot be composed with
K2101 merely because both formulas contain the same memory label.

The domain construction is a conditional self-adjoint apparatus model, not a
physical GU action, vacuum or source observation. It resolves the finite-zone
mathematical locality seam while preserving the harder spectrum/capture gaps.

## 5. Released test: positive momentum is not a free locality repair

The simplest attempted repair is to retain only the positive-momentum sector
P_plus of the free chiral H0, making its energy nonnegative. For any smooth
compactly supported Hermitian matrix multiplier V, however,

    [P_plus,V]=0 implies V=0.                         (8)

Proof: in Fourier variables, multiplication has kernel V_hat(p-k). The
negative-output/positive-input block samples p<0,k>0 and therefore every
q=p-k<0. If that block vanishes, its continuous kernel vanishes there;
Hermiticity gives the conjugate positive q values. Continuity at zero then
makes V_hat identically zero. The Fourier transform is injective, so V=0.
Equivalently test against compact Fourier wavepackets around arbitrary such
p,k to justify the kernel implication. P_plus preserves Dom H0, so asking
it to reduce H0+V is exactly this commutation condition.

The compressed P_plus V P_plus is a DIFFERENT, nonlocal operator on the
positive-momentum space; it is not the same local multiplication interaction.
It DOES give a valid self-adjoint semibounded Hamiltonian
H_plus=H0 restricted to P_plus + P_plus V P_plus, bounded below by-||V||.
For the nonnegative profiles and V>=0 used above it is nonnegative. Thus
this repair succeeds spectrally while changing the interaction and localization
hypotheses. Nonlocal compression or absence of compact states alone is not
a proof of operational superluminal signalling.
Noncompact constant V is a countercontrol: it commutes with P_plus, so the
compact-support hypothesis matters. This is a restriction on this particular
repair, not an exclusion of all semibounded local quantum field apparatuses.

A nonzero compactly supported L2 wavepacket also cannot have exclusively
positive momentum. Compact support makes it L1 and its Fourier transform
entire; vanishing on the open negative real half-line forces it identically
zero by the identity theorem. Thus the exact compact-packet finite-traversal
hypothesis cannot silently survive that positive-momentum projection. Tail
budgets from K2102 remain available for approximate packets.

H's OWN positive spectral subspace is G P_plus G*, and does exist. It differs
from the free P_plus; selecting it transports the nonlocal spectral projection.
It too contains no nonzero compactly supported packet: G* preserves spatial
support, so such a packet would give a compactly supported vector in P_plus,
contradicting the same entire-Fourier argument.
Neither its compatible local intervention algebra nor a physical preparation
budget has been constructed here. This prevents mistaking(8) for a denial of
the spectral theorem or for a universal stable-detector obstruction.

A finite Fourier control uses multiplication by cos(x) on half-integer modes:
it couples k=1/2 to p=-1/2 with coefficient1/2. This periodic smooth example
is a diagnostic of crossing, not a compact-line proof; (8) is the proof above.
A genuine line-L2 control is also exact: any normalized f with Fourier support
in(1/4,3/4) satisfies ||P_minus cos(x) P_plus f||=1/2, since the two Fourier
translates have disjoint supports and only the minus-one translate is negative.

## 6. Verification

Written unitary conjugation and kernel estimates prove domain/self-adjointness
and norm-resolvent statements. Exact finite controls check the occupied-register transmission
block (the full two-memory coherence check is in K2102), jump order for general noncommuting matrices, the gauge sign,
resolvent half-line integral, and the boundary-layer phase limit. Genuine faults
alter jump unitary, gauge sign, kernel decay, the initial gauge factor,
or the actual positive/negative Fourier coupling.
No finite lattice or symbolic Boolean is presented as proof of a continuum
domain theorem. The strongest contrary construction is(7); the weakest seam is
confusing resolvent convergence with uniform dynamical or energy convergence.
