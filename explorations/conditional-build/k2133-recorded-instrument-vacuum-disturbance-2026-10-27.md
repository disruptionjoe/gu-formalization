---
title: "K2133: Complete recorded measurements from vacuum disturbance"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional local-operator bounds and exact parity distance; no microscopic apparatus or GU recovery
scripts:
  - tests/channel-swings/k2133_recorded_instrument_vacuum_disturbance_probe.py
---

# K2133: Complete recorded measurements from vacuum disturbance

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete channel approximation from global vacuum loss and parity energy consequence
carrier: supplied positive Hilbert local von Neumann algebra and finite code with arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: complex operator adjoint
grading: binary system parity with compatible reference; no GU grading identification
action_owner: repository-construction -- bounded local Kraus instrument; optional supplied gapped Hamiltonian
target: full recorded instrument and global vacuum fidelity MAP-TYPE=intertwiner
```

## 1. What is new and what is reused

[K2108](k2108-local-detector-tradeoffs-2026-10-26.md) already proves exact
vacuum-preserving local instruments are trivial for a separating vacuum.
[K2130](k2130-stable-empty-vacuum-locality-2026-10-27.md) already gives a finite-code
bound for a single effect. Here the controlled object is the ENTIRE output
state and classical record, uniformly with references. We turn approximate
global vacuum preservation into approximate identity with an independent random
record, then consume that bound in the full parity instrument.

This is conditional operator mathematics, not construction of a stable local
nonlinear detector. Local bounded Kraus membership is a hypothesis; a causal
interaction density realizing it is still missing. General dilation continuity
is standard [Kretschmann--Schlingemann--Werner](https://arxiv.org/abs/quant-ph/0605009).
We give the elementary proof for this specific code/preparation estimate and
make no novelty claim. Conventional vacuum assumptions are discussed by
[Fewster--Rejzner](https://arxiv.org/abs/1904.04051); they are not derived from GU.

## 2. Complete-instrument estimate

Let M act on H, let Omega be a unit vector, and let K_i in M be a finite or
countable family with sum K_i* K_i=I strongly. Partition i into recorded outcomes
r. The instrument maps rho to sum_r |r><r| tensor sum_(i in r) K_i rho K_i*.
Set c_i=<Omega,K_i Omega>, s=||c|| and

    d=1-s²=1-<Omega, Phi(|Omega><Omega|) Omega>.         (1)

Here d is GLOBAL unread vacuum fidelity loss, not false-click probability or
change of the vacuum restriction to M. For code isometry V:C^n->H assume
B'_j in M' with sum_j||Ve_j-B'_j Omega||²<=delta² and
C²=sum_j||B'_j||². These constants are supplied and tied to this code and region.
A separating vacuum makes M' cyclic, so finite approximants exist, but does
not bound their norms uniformly. The inequality itself only requires the
stated approximants, not separation as a separate axiom.

For d<1 define p_r=sum_(i in r)|c_i|²/(1-d). Let R_p preserve the embedded code
state and independently generate this record. Then

    (1/2)||J_V-R_p,V||_diamond
      <= min(1, C sqrt(d)+(1+sqrt(1-d))delta+1-sqrt(1-d)). (2)

The norm compares maps from the finite code to the FULL output H and record;
no unproved code-invariance of J is assumed. For d=1 only the trivial bound1
is claimed and any p can be used.

Proof: W psi=sum_i K_i psi tensor |i> is an isometry. Put
D=W-I tensor c. Then ||D Omega||²=d and ||D||<=1+s.
Since B'_j commutes with each K_i,
D B'_j Omega=(B'_j tensor I)D Omega. Thus the Hilbert--Schmidt bound on the
finite code columns implies ||DV||<=C sqrt(d)+(1+s)delta.
Replace c by c/s; the change in isometry on V has norm1-s. For two isometries
U1,U2 and an arbitrary pure code/reference input, trace distance of outputs is
at most ||(U1-U2) tensor I||. Mixed inputs follow by purification and tracing.
Apply the SAME channel that reads r and discards the remaining Kraus environment.
This proves(2), including countable Kraus families by the convergent isometry.
There is no postselection or conditional branch renormalization in this bound.

## 3. Exact distance to a recorded binary Lüders instrument

On a code with nonzero orthogonal P+ and P-, P++P-=I, define
I(rho)=sum_r |r><r| tensor P_r rho P_r. For unrestricted code states and
references,

    inf_(0<=p<=1) (1/2)||I-R_p||_diamond=1/sqrt(2).     (3)

For a pure input/reference with x=||P+psi||² and independent + record
probability p, blockwise rank-two trace norms give

    f(x,p)=(sqrt((x-p)²+4p x(1-x))
          +sqrt((x-p)²+4(1-p)x(1-x)))/2.               (4)

For p=1/2 this is sqrt(1/4+x-x²)<=1/sqrt2, proving the universal upper bound.
For x=1/2, f=(sqrt(p²+1/4)+sqrt((1-p)²+1/4))/2; convexity and symmetry show
its minimum occurs at p=1/2 and equals1/sqrt2. This proves the lower bound.
Convexity/purification makes pure inputs sufficient; ranks of P± do not matter.
A total-even reference witness can correlate system +/- with reference +/-.
If the allowed inputs instead exclude ALL cross-sector system/reference
coherence, the corresponding restricted optimum is1/2. The domain is essential.
K2121's Gaussian approximation floor is a different comparison class and is
not replaced by(3).

If J_V approximates the full parity instrument to half-diamond error epsilon,
triangle inequality and(2),(3) imply

    C sqrt(d)+2delta+1-sqrt(1-d)>=1/sqrt2-epsilon.       (5)

Let q0=(1/sqrt2-epsilon-2delta)_+. For C>=0 define

    z0=[sqrt(C²+2q0-q0²)-C(1-q0)]/(1+C²).

Solving the increasing scalar function C z+1-sqrt(1-z²)=q0 gives

    d>=z0² >= [q0/(C+1)]².                            (6)

At q0=0 the first formula is zero. The root has nonnegative right-hand side
1-q0+Cz when squared, since q0<=1/sqrt2. Equation(6) is a necessary lower
bound from(5), not a claim of optimal physical attainability. The sharper
coefficient of delta in(2) can be used directly when useful.

If additionally H-E0>=Delta(I-|Omega><Omega|), Delta>0, then outgoing vacuum
field energy, interpreted as an extended positive expectation, obeys

    Tr[(H-E0)Phi(|Omega><Omega|)]>=Delta d>=Delta z0².   (7)

This is excitation energy of the field, not total apparatus work. A gap or
uniform C,delta is not supplied by locality. No gap means no positive energy
floor follows from d alone. Finite output energy must be established separately.

## 4. Exact controls, resource escape and causal meaning

Use Omega=sqrt(lambda)|00>+sqrt(1-lambda)|11>, 0<lambda<1,
M=M2 tensor I, local projectors K0=|0><0| tensor I and K1=|1><1| tensor I.
The two-dimensional code spans |00>,|10>. Exact commutant preparations are
B'_0=I tensor |0><0|/sqrt(lambda) and
B'_1=I tensor |0><1|/sqrt(1-lambda), so

    delta=0, C²=1/lambda+1/(1-lambda), d=2lambda(1-lambda).

This local instrument is exact binary Lüders measurement on the code and
preserves the reduced vacuum on M, but disturbs its global coherence.
For the supplied H=Delta(I-|Omega><Omega|), energy=Delta d exactly.
This finite Hamiltonian is a control, not a relativistic causal field.
As lambda tends to0, d tends to0 while C diverges; perfect recording does not
imply a code-independent positive disturbance or energy floor. A scalar
random-identity instrument has d=0 with arbitrary noisy outcomes, demonstrating
why baseline probability is not(1). A nonlocal operation can preserve Omega
while acting elsewhere; locality of effects alone does not establish the Kraus
commutation needed in(2). A supplied gapless two-level family scales energy
to zero with d fixed, demonstrating the spectral-gap necessity.

K_i in M implies the unread channel fixes every B' in M':
sum_i K_i* B' K_i=B'. This is external-algebra nonsignalling for any initial
state, including vacuum correlations. It does not prove that an arbitrary
local channel can be generated by a bounded-energy causal interaction density.
The remaining constructive target is such an interaction plus a recorded
readout satisfying the explicit code/region/error/resource budget.

## 5. Acceptance and scope

The probe checks exact finite Stinespring residuals, reference output blocks,
commutant preparations, global/reduced vacuum distinction and gapped energy.
Actual changed matrices, probabilities, coefficient formulas and record labels
produce failing checks after a passing clean baseline. Universal code-channel
and parity-distance bounds are the written proofs, independently reviewed;
finite examples do not prove the continuum theorem. No external-expert or
proof-assistant certification is claimed.

SC-OP-04 ASSERTS candidate grammar; SC-OP-05/SC-META-53 remain UNCERTAIN;
SC-META-56 DISAVOWS an odd-action prerequisite. LT-SM8/LT-GR6b, source,
ledger0.263 and canon remain unchanged. Conditional quantum instruments and
a supplied vacuum algebra do not establish GU interacting positivity.
