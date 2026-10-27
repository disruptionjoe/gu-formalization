---
title: "K2119: Exact errors and resources of distributed cat control"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported operator and apparatus mathematics; no constructed local continuum controller, source selection, GU verdict or novelty
scripts:
  - tests/channel-swings/k2119_distributed_controller_errors_probe.py
---

# K2119: Exact errors and resources of distributed cat control

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

## 1. Actual distributed apparatus state and complete instrument

Take n>=2 local factors, nontrivial Hermitian reflections R_v, and
R=product_v R_v on their tensor product. Require R to have both eigenvalues.
The local factors may be parity-even encoded CAR factors as in K2114; no
spacelike odd CAR operation is inferred. Local controls are supplied exact
unitaries on co-located apparatus and system factors. Their construction as
continuum Hamiltonians remains open.

In the cat subspace ordered (|0^n>,|1^n>), prepare the actual density matrix

    tau=[[p,z],[conj(z),1-p]],
    0<=p<=1, |z|^2<=p(1-p).                            (1)

Each site applies control-R_v and measures its apparatus in the X basis.
For x=(x_1,...,x_n), q=product x_v. Contracting the normalized X bras gives

    I_x(rho)=2^-n [p rho+(1-p)R rho R
                         +q(z rho R+conj(z)R rho)].   (2)

There are2^(n-1) strings per q. Thus the COMPLETE parity-record instrument is

    I_q(rho)=1/2 [p rho+(1-p)R rho R
                         +q(z rho R+conj(z)R rho)].   (3)

For p=z=1/2 this equals P_q rho P_q. Equation(3) is derived from the actual
positive apparatus state, so it is completely positive, including on arbitrary
external references. It is not a fitted outcome-probability map. If fine
strings are retained, conditional on q they are uniform with identical
quantum maps; adding or discarding them changes neither the error below nor
within-sector disturbance. Proper subsets of X records are uniformly
uninformative since summing one unobserved x_v cancels the q term.

This generalizes the supplied pure Bell-resource computation of
[K2116](k2116-distributed-coherent-readout-2026-10-26.md) to mixed distributed
control with the exact same complete recorded-output criterion. Standard cat
measurement techniques are not claimed new.

## 2. Sharp full-instrument error for every cat-subspace state

Let tau_plus=|cat+><cat+| and

    d=p-1/2, w=z-1/2, e=sqrt(d^2+|w|^2).

The half-diamond distance between(3) and the ideal recorded Lueders instrument
is EXACTLY

    e = (1/2)||tau-tau_plus||1.                       (4)

Upper bound: the same fixed circuit applied to two apparatus states cannot
increase their trace distance, including arbitrary input/reference states.
Thus e bounds every output error. The difference tau-tau_plus has eigenvalues
+/-e, giving the right side.

For equality take normalized eigenvectors u,v of R with eigenvalues+1,-1 and
input psi=(u+v)/sqrt2. In the ordered two-dimensional output span(u,v),
the q-block difference is

    Delta_q=1/2 [[q Re(w), d-i q Im(w)],
                 [d+i q Im(w), -q Re(w)]].           (5)

Its eigenvalues are+/-e/2, so ||Delta_q||1=e. The two orthogonal classical
record blocks add to trace norm2e. This proves equality with no reference
needed, while the upper bound covers every reference. If R is scalar the
lower witness is absent and formula(4) need not be attained.

The unread channel and label channel have different errors:

    sum_q I_q = p Ad_I+(1-p)Ad_R,
    unread halfdiamond error=|p-1/2|,
    label-only halfdiamond error=|Re(z)-1/2|.          (6)

The unread statement follows from the difference d(Id-Ad_R), whose diamond
norm is2|d| because a balanced eigenvector superposition distinguishes R
from I. For labels, the outcome-probability error is q Re(w)Tr(R rho);
an eigenstate attains|Re(w)|. With a reference, each difference block is
+/-Re(w) A, where A=Tr_system[(R tensor I)rho]=A_+-A_-. The operators
A_+/- are positive partial traces of the two spectral blocks and have total
trace1, so ||A||1<=1. This proves the same reference-stable bound. Consequently balanced fully dephased cat control (p=1/2,z=0)
has PERFECT unread map but full-record error1/2. Outcome probabilities or
unread field channels alone do not certify coherent measurement.

## 3. Phase and extensive apparatus noise

For local coherent branch phases theta_v, let Theta=sum_v theta_v. A balanced
cat initially gives z=exp(-i Theta)/2. Equations(4)--(6) yield

    complete recorded error=|sin(Theta/2)|,
    label-only error=sin^2(Theta/2), unread error=0.    (7)

Only the total phase matters for this circuit; correlated compensating local
phases can cancel. A bound on each site's unconditioned channel gives no bound
on Theta. This is the physical phase debt of
[K2117](k2117-coherent-pulse-phase-2026-10-26.md), not an error in its
unconditioned antecedent.

If each local qubit independently dephases with real visibility eta_v in[0,1],
then p=1/2 and z=(product eta_v)/2. Hence

    complete recorded error=(1-product eta_v)/2.       (8)

For equal eta and required error <=epsilon<1/2 this protocol needs
eta>=(1-2epsilon)^(1/n). Equivalently if independent phase flips have probability
r<=1/2, eta=1-2r and r<=[1-(1-2epsilon)^(1/n)]/2.
For fixed epsilon and large n the latter is
 -log(1-2epsilon)/(2n)+O(n^-2).
The pure cat also has one ebit across every nontrivial bipartition. Starting
from product states with two-site unitary gates requires at least n-1 gates
connecting sites: a disconnected interaction graph leaves a product across
some cut, whereas a pure cat is entangled across every cut. Preexisting
entanglement changes this preparation premise.

This is an exact protocol resource scaling, not a universal lower bound on
fault-tolerant devices; error correction or different resources change it.
Independence is essential. Perfectly correlated random phase flips multiply
visibility differently: the total phase is n times the shared phase.

Suppose a particular regulated apparatus covers an aperture of volume
v (A T)^3 by cells of volume at most ell^3, with fixed ell. It requires
n>=v(A T)^3/ell^3 cells. For this uncorrected independent phase-flip model,
per-cell r must then scale as O(T^-3) to hold fixed error below1/2. K2115
allows field excitation to vanish while this separate apparatus coherence
burden grows. The covering and noise assumptions are explicit; nothing here
proves a universal total work or energy divergence.

## 4. Robust composition and causal collection

Let the prepared apparatus have leakage probability ell_out outside the cat
subspace, Q the cat projector and tau=Q sigma Q/(1-ell_out) the normalized
inside state. For ell_out<1, purification and projection give
D(sigma,tau)<=sqrt(ell_out), including possible coherent leakage. Thus a
conservative full instrument bound is

    error <=min(1,sqrt(ell_out)+e(tau)+sum_v epsilon_v), (9)

provided local actual versus intended controls have compatible complete
channel bounds epsilon_v on all intermediate states actually produced.
The sum follows from telescoping composition and contraction, not from
adding outcome probabilities. An estimate restricted to one preparation
subspace cannot be reused after earlier gates leave it unless its isometry
hypotheses are established there. Leakage=1 leaves tau undefined and the
trivial bound1 applies. Correlated apparatus-field inputs fall outside this
independent apparatus preparation model.

For spatially separated readouts the q record becomes accessible at one site
only after information from every necessary bit can reach it, possibly as
aggregated partial products. The record input/side-information assumptions of
K2118 must hold; a collector given the answer in advance is excluded. Apply K2118's
max_v(t_v+dist(x,x_v)/c) bound. Pre-distributing a cat can pay preparation
latency before the experiment; it does not remove record latency. Local
outcomes and gates are a finite network realization, not a local continuum
controller. Bounded field excitation, finite circuit algebra and a formal
spacetime interaction density together still do not supply its phase-fixed
Hamiltonian, domain, continuum limit or controller energy budget.

The next substantial construction must address that actual interface, or
move to the stronger source-specific observation/domain contender; another
ideal Bell/cat circuit or another unconditioned pulse estimate would repeat
completed work.
