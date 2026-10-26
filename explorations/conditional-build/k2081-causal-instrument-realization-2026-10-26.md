---
title: "K2081: Causal record bounds and a finite-graph apparatus"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2081_causal_instrument_realization.py
  - tests/channel-swings/k2081_causal_instrument_realization_probe.py
---

# K2081: Causal record bounds and a finite-graph apparatus

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
result: causal record and system-channel error bounds with a finite-graph repair
carrier: complex massive Dirac1408 sea CAR and separately declared finite spatial graph LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert and imported sea state ON=declared_complex_completion
real_structure: complex CAR; source reality unselected
grading: fermion parity, distinct from energy sign
action_owner: repository-construction -- causal apparatus hypothesis and finite graph controls
target: instrument duration, error and complete local circuit MAP-TYPE=intertwiner
```

## 1. Question and scope

[Conditional mathematical result; accepted after independent internal specialist review. No external or proof-assistant certification.]
K2080's compact-mode number projection n_f=a*(f)a(f) lies in a region's even
CAR algebra. This implies commutation with its spacelike exterior, not an
instantaneous physical measurement throughout the region. Here test the actual
record and nonselective-channel requirements. The strongest contrary construction
is an exact, slower finite-graph instrument, not a claim that every measurement
is impossible. Source SC-OP-04 ASSERTS candidate grammar; OP-05 and META-53
remain UNCERTAIN; META-56 DISAVOWS the odd-action prerequisite. LT-SM8/GR6b
and all source, physics-ledger and canon verdicts remain unchanged.

The issue is known: [Sorkin, Impossible Measurements on Quantum Fields](https://arxiv.org/abs/gr-qc/9302018)
shows why projection rules require causal scrutiny. We give the following
CAR-specific argument directly; no scalar-field theorem, novelty or physical
apparatus conclusion is imported.

## 2. Localized record theorem

Assume a fixed apparatus initially independent of the system, causal local joint
dynamics with speed v, and a classical record read in spatial region O at time T.
The pulled-back record effect must belong to the initial system algebra of the
causal past O_(vT). This is an explicit apparatus causality hypothesis, not proved
by K2080's algebra. Internal apparatus entanglement is allowed. Preconditioning
the apparatus on the unknown system input is not allowed.

For normalized compact f the target input-time effect is n_f. Choose a normalized
smooth h supported outside O_(vT), with alpha=<f,h> nonzero, and a second smooth
mode h' in that same exterior, orthogonal to f and h. Infinite local test-space
dimension supplies h'. An even local bilinear rotation swaps occupations of h,h'.
Choose a normal state with one h occupied and all other relevant finite modes
empty; its swapped state has h' occupied. Their target click probabilities are
|alpha|^2 and zero. Every causal record has the same distribution on the two inputs,
because the swap commutes with its pulled-back effect. Hence uniform binary record
TV error epsilon on all normal states obeys

    epsilon >= |alpha|^2/2.

Smooth compact tests are dense in the exterior L2 space (take the causal-past
boundary of measure zero, or use the open spacelike exterior). Taking the supremum
there gives

    epsilon >= ||1_exterior f||^2/2.                   (1)

In particular exact measurement requires f to vanish in that exterior. A point
readout cannot collect arbitrarily distant support in arbitrarily short time.
Distributed records and sufficiently long collection times remain possible.

Normal witness states are legitimate in the imported sea representation. A finite
CAR subalgebra is a matrix algebra with multiplicity, so its mode-vacuum projection
has a nonzero range in any faithful representation. More specifically, K2060
excludes a nonzero compact mode in either pure massive energy sign; on any finite
span of compact modes the compressed sea covariance therefore has spectrum strictly
between0 and1. Its finite-mode state is faithful. Conditioning the sea onto the
finite-mode vacuum and creating h gives a normal state, and the local swap gives
the second. No efficient preparation or uniform energy budget for these witnesses
is claimed. Equation(1) is not a lower bound for just the selected Gaussian input.

## 3. Whole-instrument signal inside the support region

For R=I-2n_f, the complete binary nonselective channel is
Phi(rho)=(rho+R rho R)/2. Let h_A and g_B be normalized compact tests in separated
regions A,B with alpha=<f,h_A>, beta=<f,g_B> nonzero. Use h'_A orthogonal to f,h_A
and the local swap above. On the one-h_A input versus one-h'_A input, Bob's n_g
output differs exactly by

    Delta=2|alpha|^2 |beta|^2.                          (2)

Indeed R acts on the one-particle subspace by r=I-2|f><f|; <g,h_A>=0 and
<g,r h_A>=-2<g,f><f,h_A>. The identity half contributes zero and the reflected
half contributes(2). The swapped mode has zero contribution in both halves.
If a physical channel cannot signal from A to B within its duration, uniform
system-output TV error epsilon is at least Delta/2. This is a different accuracy
requirement from matching the detector record alone.

For a literal endpoint target Phi on identical spatial input/output labels,
vT<dist(A,B) suffices for the causal exclusion. If the target is free evolution
composed with Phi, transport Bob's test as well: its support expands by vT, and
2vT<dist(A,B) is a sufficient condition. An interaction-picture change cannot
silently retain the original support gap. This does not contradict K2080's exact
no-signalling to the exterior of the WHOLE detector region.

## 4. Constructive finite-regulator repair

On a finite connected graph with N CAR modes and a supplied spanning tree, any
normalized complex vector f can be mapped to root mode e0 by local even controls.
First choose on-site phases making its amplitudes nonnegative. Eliminate leaves
in postorder. For parent amplitude a and child b, the two-site rotation

    [[a/r,b/r],[-b/r,a/r]], r=sqrt(a^2+b^2),

zeros the child; skip r=0. At most N-1 such rotations suffice. Each is generated
by an even nearest-neighbor number-conserving bilinear. Let U f=e0 and let Gamma(U)
be its exterior-power Fock implementation. Then

    Gamma(U) n_f Gamma(U)* = n_0.

A genuinely local two-state pointer at the root, initialized in0, can implement
U_ptr=(I-n0) tensor I+n0 tensor X, followed by ordinary pointer readout.
Apply Gamma(U), measure the root, then Gamma(U)*. The two Kraus operators are
EXACTLY n_f and I-n_f on the entire finite Fock space. Forgetting the reverse
rotations gives a different instrument. Both outcomes are retained; no species
index is substituted for a shared memory.

With mixing coefficient bound J>0, each angle lies in[0,pi/2], so forward plus
reverse mixing duration is <=pi(N-1)/J, plus separately supplied phase/readout
durations. This gives an explicit finite apparatus and a resource scaling, not
an optimal time theorem. Continuous-time finite-range lattice Hamiltonians have
Lieb-Robinson tails, not a strict continuum light cone; a causal circuit requires
explicit gate transmission times. N-dependent resources, continuum convergence,
field/apparatus energy and point-local relativistic implementation remain unproved.

### Mesh-independent duration on Cartesian regulators

The N-dependent sequential bound is not necessary. This supplied control model
allows piecewise-constant gates with drift absent or compensated. Smooth switching
at the same amplitude cap requires slack or a larger constant. On a Cartesian grid with
side counts L1,...,Ld, first funnel every line along axis1 in parallel onto the
face x1=0. Then funnel axis2 lines within that face, and so on. Sweep each line
from its far end toward zero. At each layer the edges are disjoint; all their
angles lie in[0,pi/2] and can be executed simultaneously in pi/(2J), with a
smaller coefficient on a smaller-angle edge. The procedure takes
S=sum_j(Lj-1) layers, independently of N=product_j Lj. Positivity of accumulated
amplitudes proves inductively that it maps f to the corner. Complex input uses
the same initial on-site phases. Reversing both the axis order and each gate preserves the full
instrument as above, not only its effects.

For on-site phase rate also bounded by J, principal phases in[-pi,pi] take at
most pi/J per pass. Including a supplied root pointer duration Tptr gives

    T <= pi*(S+2)/J + Tptr.

At mesh h, set J=kappa/h and physical side lengths Rj=(Lj-1)*h. Then

    T <= pi*sum_j Rj/kappa + 2*pi*h/kappa + Tptr.

Thus an exact single-mode finite-regulator instrument has a duration bound
uniform under refinement of a fixed box. Each layer's one-particle generator
norm is at most J (disjoint 2x2 blocks); the norm diverges as h tends to zero.
The usual finite-range propagation scale is Jh=kappa, with lattice tails;
this is neither an exact relativistic causal cone nor convergence to a
specified continuum Hamiltonian. No uniform total Fock/control energy or
continuum instrument limit is proved. The new result removes a gate-count
objection, and isolates the genuine continuum domain and energy question.

## 5. Verification and useful next test

The independent finite probe builds Jordan-Wigner matrices and exterior-power
unitaries. It tests local occupation swaps, the symmetric-weight signal, a phase-only
countercontrol that misses the signal, two complex/zero-amplitude tree examples,
and equality of the full Kraus operators. Two exact Cartesian controls (3x3 and2x2x2) also verify disjoint nearest-neighbor
layers, unitarity and corner concentration. Six faults change coefficients, swap,
reverse circuit or remove a grid layer and fail actual assertions. Finite controls do not establish the
causal hypothesis or a continuum limit; sections2--4 provide the general argument.

The next apparatus attempt must specify its record region, duration and accuracy
class before discretization. A continuum approximation needs a uniform propagation
and energy/resource estimate, not just more finite sites. Prepared-state-only
instruments are a distinct possible route and are not excluded by the all-state bound.
