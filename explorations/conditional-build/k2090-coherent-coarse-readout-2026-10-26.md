---
title: "K2090: Coherent coarse readout and finite apparatus support cost"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source-selected state, continuum apparatus, GU verdict or external certification
scripts:
  - tests/channel-swings/k2090_coherent_coarse_readout_probe.py
---

# K2090: Coherent coarse readout and finite apparatus support cost

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
result: conditional measurement and state resource theorem with exact finite controls
carrier: supplied positive massive complex CAR and finite apparatus LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Hilbert metric ON=declared_complex_completion
real_structure: supplied antiunitary b reverses H; no source identification
grading: parity, charge and energy signs remain distinct
action_owner: repository-construction -- supplied free dynamics and operational controls
target: conditional operational constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Scope and evidence boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and SC-META-53
remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite.
The supplied positive massive CAR model is not source operator9.16. LT-SM8 and
LT-GR6b, source-register, physics-ledger and canon conclusions remain unchanged.
K2021 local R0/R1 exists; source selection, interacting state and observed algebra
remain open. No novelty, external-expert or proof-assistant certification is claimed.
These are conditional mathematical constraints on reverse-scaffold measurement/state
requirements, not GU predictions. Layer0 separates collective mode operations from
point-local apparatus and a supplied spectral ground criterion from source selection.

## 1. Exact coherent interface

Use [K2089](k2089-distributed-smooth-transfer-2026-10-26.md)'s two selected modes
f,bf, and commuting occupations n_f,n_bf. In lexicographic basis |a,b>=(00,01,10,11),
E=1-(1-n_f)n_bf=diag(1,0,1,1), E_1=E, E_0=1-E. This basis ordering differs from
little-endian probe conventions without changing the operator. Coarse Lueders means
I_j(rho)=E_j rho E_j, including an explicit classical outcome register.

Supply three bosonic qubits initially |0,0,0>, two flags u,v and record r.
Let C copy a,b coherently to u,v by number-controlled X gates. Let G XOR
1-(1-u)v into r. Then U=C* G C gives

    U |a,b,0,0,0> = |a,b,0,0,e(a,b)>.

Thus V=sum_j E_j tensor |00,j> is an exact isometry, and record measurement
has Kraus E_j, for all states and external references. In particular |00><11|
survives the click branch. Omitting C* leaves two distinguishable flags and
tracing them gives refined dephasing. Measuring r before C* is harmless because
the record projectors commute with C*. Tracing/dephasing flags before C* is not.
The controls are even, since n_f and n_bf are even and bosonic flags commute with
CAR. Endpoint particle-hole invariance does not prove microscopic symmetry of
these supplied controls. |00><11| is parity-even, but not gauge-invariant; a
strict extra U(1) restriction would require another operational witness.

This is an explicit conditional interface, not the first finite circuit: K2082
already supplies finite-graph coherent readout. Collective controlled-n_f remains
a supplied operation. K2089's distributed transfer does not turn it into a
point-local continuum Hamiltonian. In a chosen graph implementation where flags
travel to a central gate and return to their original controls for uncomputation,
cleanup needs both outward and return propagation. A record can be ready earlier;
that is not completion of the system instrument. This is a property of that
implementation, not a universal round-trip lower bound.

## 2. Exact apparatus rank theorem for a READABLE instrument

Let E_1,...,E_k be k nonzero orthogonal projections summing to I on a finite
system. Let a finite apparatus of dimension d begin in a fixed density tau of
rank r, uncorrelated with the arbitrary system input. Allow one arbitrary joint
unitary and a projective record measurement on the apparatus. Include ALL
ancillas/record memory in d and tau. No postselection, reset or unaccounted pure
memory is allowed. Then an exact Lueders instrument exists if and only if

    d >= k r.                                                   (1)

Necessity: pick a unit vector x_j in each E_j. The nonselective system output
must be pure |x_j><x_j|. Decompose tau into r positive eigenvalues. Every
U(x_j tensor s) for s in its support therefore lies in x_j tensor A.
Unitarity makes the induced map V_j from supp(tau) an isometry. Deterministic
record j places its r-dimensional range inside the j-th record subspace.
Distinct record subspaces are orthogonal, so their dimensions sum to at least kr.
No extremality of the unrecorded channel was used.

Sufficiency: choose k orthogonal r-dimensional subspaces and isometries from
supp(tau) into them. Extend each isometry to a unitary W_j on A, and use
U=sum_j E_j tensor W_j. Assign the orthogonal output subspaces to their labels
(allocate any unused complement arbitrarily). Taking record j kills every
other branch and leaves E_j rho E_j times an apparatus state of trace1. The
same W_j throughout its sector preserves its entire internal coherence.

For two outcomes the support resource is d>=2r, attained by a pure record qubit
tensored with any rank-r spectator. Faithful finite tau has r=d and cannot give
any nontrivial exact instrument. This is NOT an exclusion of nonselective coarse
dephasing: a maximally mixed qubit, controlled I/Z, implements that channel but
has no distinguishable outcome record. Compare the distinct extreme-Schur-channel
support theorem in [K1912](k1912-faithful-bath-dephasing-boundary-2026-10-21.md):
there extremality forces the rank bound without a record requirement; here readable
sharp records force it even for a nonextreme dephasing channel.

## 3. Quantitative thermal record floor and a saturating repair

Retain exact eigenstate nondemolition, product input, finite d and a faithful
tau with smallest eigenvalue lambda. For two normalized eigenstates in distinct
outcome sectors, final apparatus states have form W_x tau W_x* and W_y tau W_y*,
each at least lambda I. Subtract that common positive part. Their trace distance
T=||tau_x-tau_y||_1/2 is at most1-d lambda. Hence any binary readout has equal-prior
classification error at least d lambda/2. The full recorded instrument's
half-diamond error relative to ideal Lueders is at least this average error:
apply it to those two inputs and discard the system. For a Gibbs state at beta>=0
and finite bandwidth Delta, d lambda>=exp(-beta Delta), so

    epsilon_instrument >= exp(-beta Delta)/2.                   (2)

A SWAP with a faithful qubit apparatus can record a system occupation exactly
while replacing the system by tau; this violates eigenstate nondemolition and
explains why that assumption cannot be dropped.
The record-only argument assumes exact eigenstate nondemolition. A stronger
joint-success argument below removes that hypothesis for FULL instrument error.
No total-work or infinite-bath bound is inferred. Increasing bandwidth or adding
pure resources changes the model.

For two outcomes, tau=diag(1-q,q), 0<=q<=1/2, and
U=E_0 tensor I+E_1 tensor X with computational record measurement yield

    I_0^q=(1-q) I_0+q I_1,  I_1^q=q I_0+(1-q) I_1.

The nonselective channel is exactly coarse dephasing, while the recorded
half-diamond error is exactly q: convexity gives <=q, an eigenstate label gives
>=q. This saturates d lambda/2=q, not generally the weaker exponential bound.
Thus coarse backaction and reliable outcome recording have different resource costs.

## 4. Stronger full-instrument bound without a nondemolition assumption

Sort the apparatus eigenvalues lambda_1>=...>=lambda_d and define
S(l)=sum_(i<=l)lambda_i, S(0)=0. Choose one unit vector x_j in each of k nonzero
outcome sectors. Let the projective record ranks be d_j, sum d_j=d. Correct
joint success means BOTH label j and unchanged pure x_j. Its probability is

    p_j=Tr[(|x_j><x_j| tensor R_j)
           U(|x_j><x_j| tensor tau)U*] <= S(d_j).             (3)

Indeed the output state has eigenvalues those of tau plus zeros, while the
tested projection has rank d_j; expand in an eigenbasis and maximize weights
between0 and1 of fixed sum to obtain the sum of the largest eigenvalues. This
proof allows arbitrary system disturbance and arbitrary joint U.

For ell=floor(d/k), a=d-k ell, discrete concavity of S (decreasing increments)
makes balanced record ranks maximize sum_j S(d_j). Consequently

    epsilon_full >= 1-[(k-a)S(ell)+a S(ell+1)]/k
                 >= d lambda_min (1-1/k).                    (4)

The first inequality uses the uniform ensemble of these eigenstates as a
channel test; ideal success is1, so half-diamond error is at least average failure.
The second follows also directly from p_j<=1-(d-d_j)lambda_min.
For a finite Gibbs bath, epsilon_full>=exp(-beta Delta)(1-1/k), without the
extra nondemolition premise. SWAP does not escape this full-instrument bound:
it succeeds only at the record part of the joint test.

The optimal AVERAGE joint success is attainable for the chosen eigenstate
ensemble: choose balanced record subspaces and controlled W_j mapping the top
d_j eigenvectors of tau into R_j. This says nothing by itself about the
optimal worst-input full-instrument error for arbitrary tau. Zero average
error in(4) is possible precisely when d>=k rank(tau), recovering(1).
For d=k and tau=diag(1-(k-1)lambda,lambda,...,lambda),0<=lambda<=1/k,
controlled cyclic shifts and computational record yield only symmetric label
noise, with full half-diamond error exactly(k-1)lambda. The upper bound is
convexity of the mixture of ideal and cyclically relabeled instruments; any
eigenstate gives the matching lower bound. This also supplies a k=3 saturating
consumer and shows why pure-outcome recording and unchanged backaction differ.

## 5. Acceptance and remaining construction

The exact probe checks the full32-dimensional reversible circuit on all16 system
matrix units, omitted cleanup, a rank-two mixed apparatus with three orthogonal
record ranges, the noisy qubit instrument, the exact balanced-rank spectral bound, and a
three-outcome saturating label channel. Planted faults alter gates, record
maps and bath preparations; the clean baseline runs first. These finite controls
support the written all-dimensional theorem, not a continuum control realization.
Next construct the missing point-local collective readout or prove a physically
scoped resource/error bound. Reuse this rank condition; do not repeat the generic
circuit or mistake K2089 transfer for that missing operation.
