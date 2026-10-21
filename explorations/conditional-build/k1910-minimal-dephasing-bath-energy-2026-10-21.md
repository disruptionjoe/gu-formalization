---
title: "K1910: Sharp bath excitation cost for prescribed dephasing"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; no native GU identification, novelty, or optimal temporal boundary
scripts:
  - tests/channel-swings/k1910_minimal_dephasing_bath_energy.py
  - tests/channel-swings/k1910_minimal_dephasing_bath_energy_probe.py
---

# K1910: Sharp bath excitation cost for prescribed dephasing

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
result: weighted-Gram spectral energy optimum, robust qubit realization and reset boundary
carrier: finite system population basis and a pure controlled finite-dimensional bath LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: ordinary complex conjugation, no native K/C identification
grading: fixed population labels; not source graded-IG or physical chirality
action_owner: repository-construction -- supplied finite channels and controlled dilations
target: conditional noise discrimination and specified bath resources MAP-TYPE=intertwiner
```


## 1. Specify the resource before minimizing it

[K1905](k1905-causal-quantum-memory-realization-2026-10-21.md) implements
K1903's four-mode channel with a ground-state qubit and final mean energy
omega[p2+(p3+p4)/2], or omega/2 for uniform populations. That is the cost of
its chosen orientation. It is not the minimum among equivalent dilations.
We solve that missing question, including a single design robust to unknown
input populations.

Assume a fixed finite bath Hamiltonian with ordered eigenvalues
`0=epsilon1<=epsilon2<=...<=epsilon_d`, d at least rank(C), an initially
pure ground state |0>, and arbitrary controlled bath unitaries
`sum_j |j><j| tensor U_j`. The system Hamiltonian is diagonal in this basis.
No locality, control-amplitude, duration, reset, transport or thermal reservoir
constraint is included in this optimization. These constraints would define
a different feasible class. Set e_j=U_j|0> so C_jk=<e_k,e_j>.

For input populations p_j, the bath marginal is

    rho_E=sum_j p_j |e_j><e_j|.

It is independent of the input coherences. Let
`M=diag(sqrt(p)) C diag(sqrt(p))`, and let its nonzero eigenvalues in decreasing
order, padded by zeros, be lambda1,...,lambda_d. The exact minimum is

    E_min(C,p;H_E)=sum_a epsilon_a lambda_a.              (1)

This specializes the standard passive-state/ergotropy rearrangement, not a
new thermodynamic principle: Allahverdyan, Balian and Nieuwenhuizen,
[Maximal work extraction from quantum systems](https://arxiv.org/abs/cond-mat/0401574),
2004, equations(5)-(8). The application here fixes the bath spectrum through
the dephasing Gram matrix; no novelty is claimed.

## 2. Proof and actual attainment

The matrix with columns sqrt(p_j)e_j has XX*=rho_E and X*X=M^T, so the
nonzero spectra coincide. All Gram realizations of C are related by an
isometry on their span. Consequently the possible rho_E fill the unitary
orbit of this spectrum in the fixed bath space. Assigning its largest
eigenvalue to the smallest energy minimizes the trace: the squared moduli
of the overlap matrix are doubly stochastic, so a convex combination of
permutations, each bounded below by the oppositely ordered assignment.
The same argument extends a lower-dimensional support by zero eigenvalues.

Rotate all bath vectors by ONE common unitary that makes this assignment.
Every C_jk is unchanged. Each new unit vector extends to a bath unitary
mapping |0> to it; the controlled unitary implements the same channel.
Finite-dimensional unitaries have self-adjoint logarithms and can be driven
by smooth pulses, so this is exact attainment in the unrestricted stated
control class, not just an infimum. Include the free bath evolution through
the interaction-picture conjugation, as in K1905. Since populations and
system energy are unchanged and the interaction vanishes at endpoints,
external control work equals the bath energy increase. It excludes reset,
transport and apparatus cost; it is not a thermal entropy bound.

For a bath with a unique ground and every excited energy at least omega,
(1) gives E>=omega(1-lambda1). Equality holds if the remaining occupied
bath directions all have energy omega. A bath with ground degeneracy at
least rank(C) can implement the channel with zero endpoint excitation.
Thus no positive channel-only energy lower bound exists without a specified
spectrum, and a zero gap does not make preparation or control free.

## 3. Exact four-mode qubit result and robust design

For K1903 choose
`e1=(1,0), e2=(0,1), e3=(1,1)/sqrt(2), e4=(1,-i)/sqrt(2)`.
With H_E=omega|1><1|, the Bloch vector of rho_E is

    r=(p3,-p4,p1-p2).

Hence the population-dependent sharp answer is

    E_min(p)=omega/2 [1-sqrt((p1-p2)^2+p3^2+p4^2)].       (2)

For uniform p this is `omega(1/2-sqrt(2)/8)`, strictly below K1905's
omega/2. One common final rotation extracts omega sqrt(2)/8 from that
original bath orientation while preserving the system channel, even if the
system and bath are correlated. A bath-local unitary always leaves the
system marginal unchanged.

For explicit attainment use the new ground direction in the original bath
coordinates

    g=(1, exp(-i*pi/4))/sqrt(2),
    h=(-exp(i*pi/4),1)/sqrt(2), Q=[g h], R=Q*.

Q is unitary. Replacing every old U_j by R U_j, or appending common R,
leaves all overlaps unchanged. The excitation probabilities become

    (1/2, 1/2, (1-1/sqrt(2))/2, (1-1/sqrt(2))/2).        (3)

This same fixed design also solves the worst-population problem:

    min_dilation max_p E(C,p)=omega/2.                  (4)

Indeed e1 and e2 are orthogonal, so their ground overlaps sum to1. At least
one has excitation at least1/2 for ANY ground orientation, even in a larger
bath with unique ground and gap omega. Equation(3) attains that bound for
all four branches. Thus an extra bath dimension cannot improve(4) under the
same gap assumption. The population-adapted optimum(2) must not be reported
as a single universally optimal design for every p; (3) is optimal for
uniform p and for the worst case, which are different statements.

## 4. Consumers: measurement tolerance, controls and reuse

If every off-diagonal coefficient of an actual correlation D differs from
C by at most delta, for uniform p the absolute row-sum bound gives
`||D/4-C/4||<=3delta/4`. Eigenvalue perturbation then yields the robust
lower bound, for any unique-ground gap-omega pure dilation,

    E >= omega max(0, 1/2-sqrt(2)/8-3delta/4).             (5)

Extra rank in D can require a larger bath; (5) remains a lower bound,
not a claim that a qubit can realize a full-rank perturbation. The inference
uses the stated experimental coefficient error, not a measured bath energy
as a surrogate for channel certification.

Positive controls separate energy from classicality: a rank-one phase channel
needs no excited bath weight; complete four-mode dephasing I4, which IS
classical phase noise, costs3omega/4 for uniform p in a bath with three
excited levels at omega. The nonclassical K1903 channel costs less. Endpoint
excitation is therefore not an ordering or witness of nonclassicality.

A bath-only unitary cannot restore a mixed rho_E to a pure ground state:
its nonzero spectrum is invariant. More strongly, if a controlled pure-bath
dilation returns the bath to the same pure state on EVERY basis input,
then e_j=exp(i theta_j)|0>, so C has rank1 and the channel is a deterministic
phase unitary. Exact noise with a reused pure bath needs an additional sink,
replacement, measurement or restored system coherence. Reversing the joint
unitary restores the input rather than preserving a dephased output. No
Landauer number is asserted without a specified thermal reset protocol.
For C12=0, a proposed protocol leaving EVERY branch with ground probability
strictly greater than1/2 is impossible by the same orthogonality argument
used in(4). This turns the minimax bound into a directly checkable reuse
constraint without an unpriced reservoir assumption.

## 5. Released composition: minimal memory and the start of Markov noise

Apply the same Gram theorem to K1909's actual semigroup F(t). Although its
single collision has a rank-two qubit dilation, **every endpoint t>0 has
rank four**, and therefore needs at least four dimensions for a pure bath.
Indeed

    F(t)=exp(-t) sum_{m>=0} t^m C^{entrywise m}/m!.

Every term is positive semidefinite by its tensor-power Gram realization.
The leading principal minors of J+C+C^{entrywise2} are

    3, 8, 13-6sqrt(2), 35/2-43sqrt(2)/4,

all strictly positive. The first three terms, with positive weights for t>0,
already have trivial common kernel. The remainder is positive, so F(t)>0.
A four-dimensional pure bath is also sufficient by Gram factorization. This
is an endpoint dimension theorem, not a claim that one four-state autonomous
bath realizes the entire irreversible process.

With a bath Hamiltonian having one ground state and three equal excited
levels of gap omega, uniform populations give the exact spectral expression

    E_min(t)=omega[1-lambda_max(F(t))/4].                 (6)

The eigenvalue4 of F(0)=J is simple. Differentiating its normalized
eigenvector equation at0 gives its derivative
`1^T(C-J)1/4`. Since sum_jk C_jk=5+3sqrt(2),

    E_min(t)/omega = [(11-3sqrt(2))/16] t + O(t^2).       (7)

The coefficient is strictly positive. The largest eigenvalue stays isolated
near0, so the remainder is an ordinary finite analytic perturbation remainder,
not an extrapolation of sampled times. The same coefficient is a lower bound
for any larger unique-ground bath with every excited level at least omega.

This linear excitation law rules out a *regular start* with a finite pure bath
and bounded smooth controls. In the interaction picture, let
`A(t)=integral_0^t ||H_int(s)|| ds`. Duhamel gives
`||U(t)-I||<=A(t)`. Starting in the bath ground, its excitation probability
is at most A(t)^2, even for a coherent system input, because the initial
vector lies in the ground projection. In the flat-gap bath the energy is
at most omega A(t)^2, whereas (7) requires a positive linear term.
Consequently A(t) cannot be O(t); for exact realization it must satisfy
`A(t)>=sqrt([(11-3sqrt(2))/16]t+O(t^2))` near0. In particular bounded controls
near0 cannot implement the exact semigroup. This is a necessary integrated
control scaling, not an optimal singular-drive construction. A Hamiltonian
with unequal excited energies also has O(t^2) excitation energy when its
norm and the control are bounded; an infinite unbounded reservoir or repeated
fresh cells changes these assumptions.

Independently, a finite bath and a time-independent total Hamiltonian cannot
realize (1) for all t>=0. Each reduced channel coefficient is a finite sum
of oscillating exponentials. After grouping equal frequencies, its long-time
Cesaro mean squared modulus is the sum of squared coefficient magnitudes.
If that function tends to zero, every coefficient must vanish. But F12(t)
is exp(-t), which tends to zero and equals1 at0. This contradiction excludes
the proposed autonomous finite realization; it does not exclude finite
endpoint dilations, time-dependent controls, approximate finite-time models,
or infinite-reservoir Markov constructions. These consequences distinguish
an energy-optimal endpoint from an unpriced exact dynamical implementation.

## Review and reproducibility

Strongest overclaim: a universal thermodynamic cost or guaranteed optimum
with spatial, amplitude or clock constraints. Equation(1) states the exact
unrestricted finite control class. Strongest counterexample to a
nonclassicality-energy inference: classical I4 costs more. Weakest seam:
conjugation in the Gram spectrum and whether p-dependent rotation is allowed.
The producer and separate probe reconstruct the marginal, explicit unitary,
branch energies, weighted characteristic polynomial and controls separately.
The general rearrangement, minimax and pure-reset arguments are analytic.
Unresolved defects within the stated class: none after these checks.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT the stylized curvature-mass toy. SC-META-53 remains
UNCERTAIN about the unbounded-spectrum problem. None identifies the positive
Hilbert system, bath, controls or accessible algebra used here. LT-SM8,
LT-GR6b and AC-F1, the source register, physics ledger and canon are unchanged.
The full20 injection, separate K/C forms, domain and accessibility remain
independent construction debts. No GU recovery, physical bath identification,
external expert review, novelty or formal proof is claimed.

The analytic arguments carry the universal statements. Exact probes check
polynomial identities, finite matrices and rational inequalities; mutations
of inputs test those checks, while report/pin mutations only test reporting
and provenance. Numerical scouts do not certify a phase law or universal sign.
