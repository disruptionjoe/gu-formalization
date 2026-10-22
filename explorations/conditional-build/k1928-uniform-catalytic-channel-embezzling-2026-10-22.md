---
title: "K1928: Uniform catalytic channel simulation and dimension cost"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite positive Hilbert models; no native GU, novelty or formal proof
scripts:
  - tests/channel-swings/k1928_uniform_catalytic_channel_embezzling.py
  - tests/channel-swings/k1928_uniform_catalytic_channel_embezzling_probe.py
---

# K1928: Uniform catalytic channel simulation and dimension cost

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
result: quantified physical information and finite catalytic resource construction
carrier: finite four-level system, physical environment and optional purifying reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, diamond norm and entropy in nats ON=independent_product_input
real_structure: complex adjoint; no native reality identification
grading: system population labels; not physical chirality
action_owner: repository-construction -- joint unitary; additive conservation explicitly imposed for thermal consumers
target: supplied extreme Schur channel and approximate return MAP-TYPE=intertwiner
```

## 1. Exact full-channel construction from a known staircase spectrum

Let C be any rank-k correlation matrix with k>=2, with unit vectors v_j in C^k.
The rank-one case is already a system unitary and needs no catalyst.
Take a k-level bath B with H_B=0, hence tau_B=I_k/k at every beta>0.
Let H_A=H_S=0 as well. Fix an integer a>=1, d=k^a and
D=1+(k-1)a. Prepare the d-level catalyst in the diagonal state

    p1=k/D,
    pi=(k/D) k^(-ceil(log_k i)), 2<=i<=d/k,
    pi=0, i>d/k.                                       (1)

For a=1 this is the pure state p1=1. Define

    r=(k-1)/D,
    q1=p1-r=1/D,
    qi=pi, 2<=i<=d/k,
    qi=r/(d-d/k)=k/(d D), i>d/k.                       (2)

These are the known optimal pure-state-extraction spectra of
[Ng, Mancinska, Cirstoiu, Eisert and Wehner, equations2--3](https://arxiv.org/pdf/1405.3039).
This note claims neither that discovery nor a new optimal state-catalysis
result. It makes the full-channel, uniform-return and consumption transfer
explicit and compares it with K1927's approximate-channel lower bound.

A stronger fact needed for our chosen implementation is exact SPECTRAL
EQUALITY: the positive eigenvalues of diag(p) tensor I_k/k are exactly q.
Indeed the leading p1/k=1/D has k copies. For each shell
k^(ell-1)<i<=k^ell, 1<=ell<=a-1, the value pi/k=1/(D k^ell)
has k*(k^ell-k^(ell-1)) copies. These are precisely q's next shell; the
remaining zeros match q tensor |0><0|. Normalization follows by counting
one first weight and a-1 shells, each of total weight (k-1)/D.
Thus a PERMUTATION unitary P on the SAME A tensor B satisfies

    P(diag(p) tensor I_k/k)P*=diag(q) tensor |0><0|.     (3)

There is no hidden pure flag, reset or extra pure ancilla. The initial
catalyst is not faithful, and this is explicitly accounted for. All
unitaries conserve the declared zero Hamiltonian.

Choose k-by-k unitary U_j with first column v_j and then apply
U_ctrl=sum_j |j><j| tensor U_j on S,B. The complete unitary
U_ctrl(I_S tensor P) implements, for every input including reference
entanglement, the exact joint S,A channel

    X -> Phi_C(X) tensor diag(q).                      (4)

The catalyst is uncorrelated with S and its reference, its output is
input-independent, and D(diag(q),diag(p))=r. The full target is exact,
not merely its population map or one prior. The bath output is discarded
and need not return. The half-diamond distance of the S,A channel from
X -> Phi_C(X) tensor diag(p) is exactly r.
This is approximate catalyst return, not unchanged or indefinitely reusable
catalysis. It is compatible with K1925's exact-return obstruction.

## 2. Exact consumption and asymptotically matching dimension

Equation(3) preserves entropy, so S(q)-S(p)=ln k EXACTLY. At H_A=0,
beta(F(p)-F(q))=ln k: small trace disturbance consumes a finite resource.
For the four-state rank2 extreme target, k=2 and

    d=2^a, r=1/(a+1), r ln d=(a/(a+1))ln2 -> ln2.      (5)

K1927 proves the matching universal lower asymptotic liminf r ln d>=ln2
for arbitrary finite Gibbs baths and joint unitaries with the stated zero
bandwidth limits, even when channel error only tends to0. Thus the leading
log-dimension cost is sharp for this target in this class.
The finite-dimension optimum for arbitrary channel implementations is NOT
claimed: Ng's finite optimum concerns pure-state extraction, a sufficient
protocol here, and need not optimize every channel-specific realization.
To achieve return r<=rho, choose a>=ceil(1/rho-1); dimensions are
exponential in 1/rho. For r<=1/100, a=99 and d=2^99 suffice exactly.
The construction is an explicit finite permutation rule, not a materialized
2^99-size circuit or a practical/local/strength-limited implementation.

## 3. Faithful harmonic alternative: both errors tend to zero

To check the rank-deficient endpoint's significance, take any d divisible by
k and use the faithful catalyst p_i=1/(i H_d), H_d=sum_(i=1)^d 1/i.
Order the dk eigenvalues of p tensor I_k/k as
lambda_n=1/(k H_d ceil(n/k)), n=1,...,dk. A permutation places these into
basis order (b,i), n=bd+i, b=0,...,k-1 and i=1,...,d. Call the resulting
diagonal state omega_AB. Compare it with p_A tensor |0><0|_B.
For n<=d, lambda_n<=p_n; beyond d the target weights vanish. Hence exactly

    D(omega_AB,p tensor |0><0|)=r_h=1-H_(d/k)/H_d.       (6)

Apply the same controlled target unitary. Trace-norm contractivity, even
with an arbitrary input reference, gives joint S,A half-diamond error at
most r_h from Phi_C tensor p. The catalyst marginal is

    q_i=sum_(b=0)^(k-1) 1/[k H_d ceil((bd+i)/k)].        (7)

It is independent of EVERY system input: partial trace over S removes the
control cross terms, and each remaining unitary acts only on B. Thus its
return distance is at most r_h, uniformly on inputs. System error is at
most r_h as well. The bath has probability1-r_h in |0>, so its marginal
realizes the explicit mixture of the desired first-column Schur channel
and the other column Schur channels. This does not give an exact channel
for a faithful finite bath-plus-catalyst; it approaches the exact channel.

The preparation state is classical, with H(B)<=h2(r_h)+r_h ln(k-1).
Its total entropy is S(p)+ln k and classical I(A:B) lies between0 and H(B),
therefore

    ln k-H(B)<=S(q)-S(p)<=ln k.                         (8)

The catalyst marginal is unchanged by U_ctrl. Since r_h tends to0 for fixed
k, the consumption tends to ln k. For k=2, r_h ln d tends to ln2; K1927
then forces the actual return r_A to have the same leading coefficient
because r_A<=r_h and the channel error tends to0. This is a second,
faithful family attaining the leading dimension cost, not an exact faithful
implementation. The harmonic idea is established embezzling prior art;
(6)--(8) explicitly account for the thermal register and uniform channel.

## 4. Released tensor and sequential-use consumers

For N exact uses of the rank2 target, a one-shot simulator applies (1)--(4)
with k=2^N and d=k^a. The full tensor target, including correlated inputs,
is exact, return r=(k-1)/(1+(k-1)a), consumption=N ln2, and
r ln d -> N ln2 as a grows. The bath has dimension2^N, initially maximally
mixed; no claim of efficient spatial control is made.

For sequential reuse of the rank2 construction with a fresh thermal bath
per step, define its channel on S,A. On the designated initial catalyst p
it is within r of the ideal Phi_C tensor p in half-diamond norm. A hybrid
argument replaces uses one at a time; each ideal prefix restores p and
the remaining physical suffix is contractive. Therefore N uses have joint
system/reference/catalyst distance at most min(1,Nr) from the ideal product
channel with returned p, even with correlated system inputs or adaptive
intermediate CPTP processing. This bound compares complete processes; it
does not pretend the actual catalyst resets to p after each use.
For fixed d this is a finite accuracy budget, not infinite free repetition.
An N-use accuracy alpha is ensured by a>=ceil(N/alpha-1). Entropy and
free-energy consumption and reset costs are not erased by the trace bound.

## 5. Hostile review and reproducibility

Independent exact probes reconstruct the multisets and an explicit permutation
for small k,a, then evaluate the full complex four-state Gram action on all
16 system matrix units, including S,A factorization and catalyst output.
They also reconstruct faithful harmonic q, errors and entropy accounting.
Input faults alter staircase shell weights, permutation assignments and the
complex target column; clean baselines precede fault checks. Entropy examples
using floating logarithms are illustrations, not certified asymptotic proofs.
Spectral equality, contractivity and entropy identities prove universal scope.
The rank-deficient exact construction defeats a broad all-input impossibility
inference from K1925's bath-free example. The separate bath is essential:
it absorbs information and is not returned. Nonzero Hamiltonians, locality,
bounded controls and the optimal finite joint-error/return tradeoff remain open.

## Reproduction

Run with Python and SymPy installed, from the repository root:

```sh
python tests/channel-swings/k1928_uniform_catalytic_channel_embezzling.py
python tests/channel-swings/k1928_uniform_catalytic_channel_embezzling_probe.py
```

The producer recomputes and compares its committed JSON report; use `--write`
only when deliberately regenerating that report. 68 producer and73 separately reconstructed exact controls;3 mathematical faults
are detected after a green baseline, with1report and1dependency-pin fault
checked separately. Assertion failures are distinguished from crashes.
No unchanged predecessor certificate bank is replayed.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the southeast rival; SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass toy;
SC-META-53 remains UNCERTAIN about indefinite spectra. None selects these
positive Hilbert channels, bath, apparatus, energies or units. LT-SM8,
LT-GR6b and AC-F1 remain unchanged. K1828 raw-column completion and K1892
imported CAR do not supply the paired full20/K/C/domain/accessibility bridge.
No source-register, physics-ledger or canon verdict changes. Universal scope
rests on the analytic arguments; finite exact controls and numerical entropy
illustrations are supplementary. No novelty, independent expert, formal-proof,
physical GU, infinite-reservoir or total-work claim.
