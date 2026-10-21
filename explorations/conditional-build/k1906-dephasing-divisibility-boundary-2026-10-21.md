---
title: "K1906: Dephasing divisibility and a robust unreachable endpoint"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum and controlled-environment mathematics; no native GU or continuum bath identification
scripts:
  - tests/channel-swings/k1906_dephasing_divisibility_boundary.py
  - tests/channel-swings/k1906_dephasing_divisibility_boundary_probe.py
---

# K1906: Dephasing divisibility and a robust unreachable endpoint

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
result: Hadamard factorization, tensor-rank rigidity and integrated Lindblad metric
carrier: four-dimensional positive logical density matrices and Schur channels LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and state expectation ON=conditional_target
real_structure: complex conjugation and CAR star; no native K/C identification
grading: finite occupation sectors and even fermion parity
action_owner: repository-construction -- supplied finite interactions or quantum channels
target: conditional coherence, causal implementation and memory demands MAP-TYPE=intertwiner
```

## Exact endpoint: a stronger question than finite-environment recurrence

K961 already proves recurrence for finite autonomous environments. The
K1905 protocol is driven and finite-duration, so that theorem does not decide
it. Here the object is a continuous family of population-fixing channels,
Phi_t(rho)=C(t) entrywise-times rho, starting at the identity channel J
(the all-ones correlation matrix). CP divisibility means Phi_t=V_t,s Phi_s
with V_t,s completely positive and trace preserving for every s<=t.

Every such V fixes each pure basis projection: Phi_s(Pj)=Phi_t(Pj)=Pj.
A channel fixing all Pj has diagonal Kraus operators, since every Kraus image
of |j> must lie in span |j>. Therefore V is itself a Schur channel and

    C(t)=D(t,s) entrywise-times C(s),                         (1)

with D a correlation matrix. This argument does not assume invertibility.

We prove that K1903's C admits no nontrivial Hadamard factorization C=A o B:
one factor must have rank1. Gram-factor A and B by unit vectors a_j,b_j;
then C is the Gram matrix of w_j=a_j tensor b_j. Its rank2 and entries force

    w1 perpendicular w2,
    w3=(w1+w2)/sqrt2,
    w4=(w1+i w2)/sqrt2,                                     (2)

up to a common isometry and the declared Gram convention. A sum of two
nonzero simple tensors with independent first AND second factors has tensor
rank2. Since w3 is simple, either a1,a2 are parallel or b1,b2 are parallel.
The entire two-dimensional span in(2) then shares that factor. Every w_j
belongs to the span; uniqueness of a nonzero simple-tensor factorization
forces the corresponding factor of every w_j to be parallel. Thus A or B
has rank1. The argument already follows from the first three columns; it
is not a restatement of the four-mode nonclassicality witness.

Suppose a continuous CP-divisible dephasing path reaches C at time T.
By continuity there is a time s with 0<|C12(s)|<1, since the modulus starts
at1 and ends at0. C(s) cannot have rank1. Applying the factorization theorem
to C=C(s) o D forces D to have rank1, and hence |D12|=1. Equation(1) then
gives |C12|=|C12(s)|>0, a contradiction. Therefore NO continuous CP-divisible
population-fixing path reaches this endpoint. This includes singular rates
or noninvertible intermediate channels if the path remains continuous.
It does not exclude a path that changes the preferred populations in between,
postselection, a discontinuous reset, or approximation to C.

## Released classification of every rank-two endpoint

The tensor argument settles a larger class without another matrix search.
For a rank-two correlation matrix, count distinct rays among its unit Gram
vectors (parallel vectors count once). A continuous CP-divisible dephasing
path from the identity reaches this matrix **if and only if there are at
most two distinct rays**.

For necessity, any third distinct ray is a linear combination of two
independent representatives with both coefficients nonzero. The same
simple-tensor argument forces one factor of every Hadamard decomposition to
have rank1. Choose a pair with final modulus r<1. Continuity supplies an
intermediate modulus strictly between r and1. Its correlation matrix is not
rank1, so the remaining factor must be rank1; this would preserve that
intermediate modulus to the endpoint, a contradiction. This proof needs no
zero entry and no differentiability assumption.

For sufficiency, remove diagonal phases and separate the indices into their
two ray groups. The target is1 within each group and a common real overlap
r in[0,1) between groups, after a further group phase. Let
f(t)=1-(1-r)t/T on[0,T], and let the removed diagonal phases grow linearly
from zero to their target values. The group correlation matrix with cross
entry f(t) is positive because it is the pullback of [[1,f],[f,1]]. For
s<t<T, its intervening channel has cross factor f(t)/f(s) in[0,1],
so it is CP; endpoint and diagonal-phase compositions preserve this. If r=0,
include the endpoint cross factor0 and hold the channel constant thereafter.
The path is continuous and CP divisible but its instantaneous damping rate
diverges at T. If r>0, f stays positive and its logarithmic rate has finite
integral; constant exponential damping also realizes the endpoint. Thus a
regular finite-integrated-rate rank-two endpoint additionally requires
nonzero cross-group overlap. Rank1 endpoints are diagonal unitaries.

In particular K1903's three-mode principal restriction is a classical phase
mixture (K1903's dimension-three theorem), yet its three distinct Gram rays
already forbid continuous CP-divisible dephasing. Classical single-time
noise and dynamical CP divisibility are independent requirements; the
four-mode witness is needed for nonclassical phase-mixture exclusion, not
for this divisibility obstruction. This eliminates a misleading inference
that only a genuinely quantum bath could produce this kind of memory.

Schur-product decomposition and channel divisibility are established research
subjects; see [Lovitz, On decomposable correlation matrices](https://arxiv.org/abs/1812.01449)
and [Wolf and Cirac, Dividing Quantum Channels](https://arxiv.org/abs/math-ph/0611057).
The elementary proof above supplies the stated restricted classification;
no claim of novelty or a classification of arbitrary quantum channels is made.

## Quantitative exclusion for regular dephasing dynamics

For an absolutely continuous time-local diagonal GKSL evolution with
integrable finite coefficients, write diagonal Lindblad entries l_alpha,j(t)
and diagonal Hamiltonian entries h_j(t). The modulus obeys

    -log |D_jk(T)| = (1/2) integral sum_alpha
                        |l_alpha,j(t)-l_alpha,k(t)|^2 dt.   (3)

The imaginary terms and Hamiltonian only affect phases. Thus
sqrt(-log |D_jk|) is an ordinary Hilbert-space distance between the time-
integrated coefficient vectors, and satisfies the triangle inequality.
This also proves no entry vanishes at finite integrated rate; a zero entry
requires an infinite exponent. That simpler fact is weaker than the exact
continuous-divisibility obstruction above.

If all entries of D approximate C to complex absolute error epsilon<1/sqrt2,
then |D12|<=epsilon and |D13|,|D23|>=1/sqrt2-epsilon. The triangle inequality
in(3) forces

    epsilon >= (1/sqrt2-epsilon)^4.                         (4)

The equation e=(1/sqrt2-e)^4 has a unique root e_* in(0,1/sqrt2): the
left minus right is strictly increasing. Every such regular dephasing
endpoint has entrywise distance at least e_* from C. The root is specified
by this exact equation, not by a numerical solver. In particular e_*>1/10,
proved by exact substitution. The same lower bound holds in the entrywise
closure of this class by continuity. No claim is made that e_* is the exact
optimal four-mode distance; the remaining entries and phases can raise it.
This is a structural approximation obstruction, not merely an infinite-rate
cost to obtain one zero while all other entries are ignored.

A sharp three-point METRIC control is supplied by diagonal real Lindblad
entries (-1,1,0) and time T=log2. Equation(3) gives
D13=D23=1/sqrt2 and D12=1/4, saturating the metric triangle. It demonstrates
why arbitrary independent pairwise damping rates would give a false answer.
It does not attain(4)'s optimal four-mode distance.

## Positive controls and useful repair

Complete dephasing of a qubit can be approached by finite-rate phase damping,
but is reached only as integrated rate diverges. A finite coherent unitary
system-memory interaction can hit zero exactly at finite time without being
a regular time-local dephasing semigroup. K1905 provides the stronger
four-mode endpoint under explicit causal ordering. Its reduced path is
continuous and population fixing, so the theorem proves that somewhere it
fails CP divisibility; no time-local generator needs to be guessed.

Conversely a legitimate continuous semigroup can be constructed from ANY
Schur channel, including C, by the compound-Poisson generator L=Phi_C-id:

    F_jk(t)=exp[t(C_jk-1)],
    Phi_F(t)=exp(-t) sum_n t^n/n! Phi_C^n.                  (5)

Each term is a channel, and the norm-convergent sum is CPTP and a semigroup.
It generally does not equal C at any positive finite time; F12=exp(-t)>0.
Its existence prevents the mistaken inference that using a quantum channel
as a collision step inherently forbids Markov dynamics. No assertion that
F(t) is nonclassical is needed or inferred from the generator alone.
The continuous-time quantum memory, the random collision law and the
population-fixing observation remain distinct models.

These results turn the finite witness into a choice of dynamical assumptions:
a realization of C in this basis must leave continuous CP-divisible dephasing,
while the explicit K1905 protocol does so without backwards signalling.
Finite-channel divisibility is neither a theorem about GU nor a proof that
all physical open-system evolution has accessible memory.

## Source ceiling and validation

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN.
These supplied positive-Hilbert constructions identify none of their missing
native full20 injection, separate K/C forms, accessibility or physical state.
LT-SM8, LT-GR6b and AC-F1, source polarities, physics-ledger and canon verdicts
remain unchanged. The result has independent quantum-mathematical scope.
No novelty, external expert acceptance, formal proof, continuum field energy,
microscopic bath selection, GU prediction or GU falsification is claimed.

The analytic proof carries general statements. Exact producer controls and a
separate probe rederive finite matrices, partial traces, generator identities
and bounds. Mathematical input faults are tested after a passing baseline;
report and dependency-pin faults are counted separately. Inline hostile review
checks the strongest overclaim, a contrary construction and the weakest
transfer/reproducibility seam. A finite control does not establish the general
spectral, tensor-factorization or continuity argument by itself.
