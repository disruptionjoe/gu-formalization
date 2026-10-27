---
title: "K2118: Locality of an extended quantum controller"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported operator and apparatus mathematics; no constructed local continuum controller, source selection, GU verdict or novelty
scripts:
  - tests/channel-swings/k2118_controller_locality_probe.py
---

# K2118: Locality of an extended quantum controller

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

## 1. A shared finite quantum controller cannot be two local factors

Let A and B be spacelike-separated regions with commuting observable algebras
mathcal A(A), mathcal A(B). If the full controller algebra M_d tensor I is
localized in A, every B-local bounded observable lies in its commutant
I_d tensor B(H_rest). In particular a nonconstant controller coefficient
P tensor J_B, with P a nontrivial projection and J_B nonzero, is not B-local.
This follows either from the matrix-unit commutant or from one X with
[X,P] nonzero. It does not depend on how small the field excitation is.

More generally a shared subalgebra C contained in both local algebras commutes
with itself and hence is abelian. If one local algebra is precisely the full
controller factor, its intersection with the other is scalar. A shared
classical random variable can be represented by commuting copies or a center;
its conjugate quantum observable cannot also be localized in both regions.
This concerns localization assignments of the actual full operator algebra,
not whether spatially separated systems can start entangled.

For a qubit, P=|1><1| and X the swap, the locality defect has a sharp norm:
for bounded selfadjoint J,

    inf_W in (M2 tensor I)' ||P tensor J-W||=||J||/2.  (1)

Proof: [X tensor I,W]=0, while ||[X,P] tensor J||=||J||.
The commutator norm is at most2||P tensor J-W||, giving the lower bound.
W=I tensor J/2 attains it since ||P-I/2||=1/2. This is a bounded finite-factor
norm statement; it is not assigned to an unsmeared unbounded field density.

The general issues of detector causal factorization are established in
[de Ramón, Papageorgiou and Martín-Martínez](https://arxiv.org/abs/2102.03408).
The elementary algebraic specialization here diagnoses the current pulse
interface and makes no novelty claim.

## 2. Commuting interaction densities do not locate the apparatus

For a commuting spacelike field pair j_A,j_B, expressions

    h_A=P tensor j_A, h_B=P tensor j_B

commute, because they share P and [j_A,j_B]=0. That fact alone is insufficient:
if the controller X is accessible in A, then [X tensor I,h_B] is nonzero.
Checking only mutual density commutators misses locality against the rest of
the apparatus algebra. Conversely, if no conjugate control observable is
accessible locally, the object is distributed/encoded control or classical
shared data. That different localization must be stated and supplied.

An exact bounded intervention exposes the operational consequence. Locate a
control qubit at A and a target qubit at spacelike B and propose
U_theta=exp(-i theta P_A tensor Z_B) as an instantaneous operation. Alice
chooses control0 or1; Bob begins in |+>. His outputs are |+> and
exp(-i theta Z)|+>, whose trace distance is |sin theta|. At theta=pi/2
Bob can distinguish them perfectly. Any A-to-B nonsignalling channel N has
the same Bob output for the two preparations, so channel error obeys

    (1/2)||Ad_U_theta-N||diamond >= |sin theta|/2.      (2)

Apply output trace-distance contraction and the triangle inequality to the
two chosen inputs. This is a lower bound, not a claimed optimum over every
causal channel. If theta=pi then U_theta is only a local phase on A and the
witness vanishes, consistently. Pre-setting classical parameters before the
experiment or allowing causal transmission from A changes the hypotheses.

## 3. Distributed repair changes the algebra, not just notation

Place different controller factors c_v at distinct interaction sites. A local
term P_v tensor J_v commutes with observables at the other sites when both
apparatus and field local algebras do. Prepare the controllers in the encoded
cat subspace span{|0...0>,|1...1>} before the measurement. Local controls then
implement the identity in branch0 and the product of local reflections in
branch1. Only the product of the X readouts carries the parity; no one site
is assigned the full logical-qubit algebra. The complete noisy operation is
computed in [K2119](k2119-distributed-controller-errors-2026-10-26.md).

This is a rigorous finite-factor/network repair with supplied local gates.
It does not make finite spatial cells pointlike in a continuum theory. A full
qubit coupled simultaneously over any cell of nonzero spatial extent encounters
the same problem upon finer spacelike subdivision, unless its support is
modeled by causal microscopic degrees of freedom. A lattice circuit can have
an exact graph light cone; continuum propagation and a field Hamiltonian
require their own proof and limiting estimates. The K2115 pulse train theorem
is for fixed finite profiles/matrices and does not give constants uniform in
the number of apparatus cells tending to infinity.

## 4. Causal record and preparation lower bounds

Suppose local outcomes at points x_v occur at times t_v, all influences and
classical messages propagate at speed at most c. Assume the newly supplied classical bits are freely variable and the collector
initial resources are independent of those inputs. Equivalently, the compared
histories differing in an unavailable bit have identical collector past data.
If every bit can change the product while the others are fixed, a deterministic exact
collector at x cannot output the parity before

    t_collect >= max_v (t_v+dist(x,x_v)/c).            (3)

Otherwise changing a bit outside that past cone leaves the collector's
accessible data identical but changes the correct answer. For simultaneous
readouts t_v=t0 and support diameter D, optimizing x still gives
 t_collect-t0>=D/(2c), by the triangle inequality for the farthest two sites.
The max-distance expression is the sharper bound for a specified geometry.
Pre-shared randomness/entanglement alone cannot transmit the missing bit.

For product-initialized controllers on an exact finite-speed local unitary
circuit, preparation of a cat with two sites distance D apart takes at least
D/(2c). If earlier, their backward cones are disjoint, so their output state
factorizes; the cat has <Z_i Z_j>=1 and <Z_i>=<Z_j>=0. This proof assumes
initial product resources throughout the relevant circuit and an exact light
cone. It does not apply to a supplied pre-entangled cat, nor assert an exact
continuum bound for lattice Hamiltonians with only exponentially small tails.
For strictly finite circuit depth, replace distances by graph distances.

These obligations charge preparation and accessible records. They leave the
classical externally driven local Dirac equation and K2115 endpoint estimates
intact. A fixed local physical detector with finite total work has not been
constructed, and no source-selected GU algebra/domain has been supplied.
