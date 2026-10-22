---
title: "K1929: Exact preparation on a resonant nondegenerate ladder"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact supplied finite energy models; no native GU, novelty or formal proof
scripts:
  - tests/channel-swings/k1929_resonant_ladder_preparation.py
  - tests/channel-swings/k1929_resonant_ladder_preparation_probe.py
---

# K1929: Exact preparation on a resonant nondegenerate ladder

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
result: exact energy-shell preparation and uniform catalyst-return bounds
carrier: finite four-level system, thermal qubit or qutrit, nondegenerate finite catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, relative entropy and half trace distance ON=independent_product_input
real_structure: complex adjoint; coherent catalyst states allowed where stated
grading: total-energy shells and system population labels, not physical chirality
action_owner: repository-construction -- exact additive-energy-conserving unitary
target: supplied extreme Schur channel with a specified bath Hamiltonian MAP-TYPE=intertwiner
```

## 1. Question and exact answer

K1928's zero-energy catalyst can return arbitrarily close while implementing
an exact channel. Here both resource registers have NONZERO fixed gaps.
Fix the four unit vectors

    v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2,
    C_jl=<v_l,v_j>, Phi_C(|j><l|)=C_jl |j><l|.

Their projectors span Hermitian(2), so C is extreme of rank2. H_S is any
diagonal system Hamiltonian. B is a qubit with energies0,Delta, Delta>0,
in its faithful Gibbs state tau_B at finite beta>0. A has NONDEGENERATE
energies E_n and arbitrary initial density matrix sigma, independent of S,B.
Only [U,H_S+H_B+H_A]=0 is allowed. No reset, battery, measurement, extra
ancilla or work reservoir is hidden. A is a resource to be returned approximately;
its preparation cost is NOT the cost of a complete thermodynamic protocol.

Make the resonance graph on the A levels: an edge joins energies differing
by Delta. Each connected component is a finite increasing path. Let S be the
set of levels with sigma_nn>0. An exact implementation exists iff S contains
only INTERNAL vertices of those paths and no two vertices of S are adjacent.
Coherences inside S are allowed. In particular a resonant chain of at least
three levels is necessary and sufficient for existence from some preparation.
A large generic nonresonant spectrum is useless for this exact task.

## 2. Proof and coherent-state scope

Apply K1923 to the composite environment Omega=tau_B tensor sigma, not to
sigma alone. In total-energy shell E the basis is (0,n) with E_n=E and
(1,m) with E_m=E-Delta. Nondegeneracy makes its dimension at most2.
Its pinched density block is diagonal, since tau_B has no offdiagonal terms;
its rank is precisely the number of these catalyst levels belonging to S.
K1923 gives 2 rank(Omega_E)<=dim(E). A singleton shell must be empty,
and a two-dimensional shell contains at most one occupied basis state.
For an occupied catalyst level both bath populations are positive, so it
must have both a predecessor and a successor and cannot have an occupied
neighbor. These conditions are also sufficient. This uses K1923's covariance,
positive-leakage and extreme-Gram proof for arbitrary U; it does NOT assume
a controlled unitary on unused input directions.

Positive sigma with a zero diagonal entry has its entire corresponding row
and column zero by its two-by-two principal minors. Therefore all coherences
are confined to S. They do not change the shell ranks. In an occupied shell
with active input basis a_E choose isometries a_E -> W_E v_j, then extend
them to shell unitaries U_j,E. The controlled direct sum over system j and
energy E conserves energy and realizes C; cross-energy coherences contribute
zero to the system trace. This also supplies an explicit finite existence
construction, without calling the resulting A output unchanged.

## 3. Global preparation optimizer, including coherences

Let tau_A be Gibbs for H_A and let

    p_* = max_(allowed S) sum_(n in S) exp(-beta E_n)/Z_A.

If no allowed nonempty S exists, exact implementation is impossible. Otherwise

    min_sigma D(sigma||tau_A) = -ln p_*,
    min_sigma [F_beta(sigma)-F_beta(tau_A)] = -ln(p_*)/beta,
    min_sigma (1/2)||sigma-tau_A||_1 = 1-p_*.

All minima are attained by sigma_*=P_S tau_A P_S/p_* for a maximizing S.
Dephasing reduces relative entropy and distance to tau_A without invalidating
the support condition. On fixed support the relative entropy decomposes into
a conditional-Gibbs relative entropy minus ln Gibbs mass; a support measurement
bounds trace distance. Thus this is optimization over coherent preparations,
not just a diagonal ansatz. Trace-distance minimizers need not be unique.

On each resonance chain Gibbs weights decrease geometrically, with
 t=exp(-beta Delta) in(0,1). The maximizing independent set is the first,
third, fifth,... INTERNAL vertex, counting from its low-energy endpoint.
To prove it, order the selected internal positions j1<...<jR. Adjacency
exclusion gives ji>=2i-1. The maximum possible R is the number of odd internal
positions; each selected weight is bounded by that of position2i-1. Omitting
an available positive weight cannot improve the sum. Components separate.
This is a weighted independent-set proof, not an enumeration conjecture.

For H_A=Delta diag(0,...,d-1), d>=3, set L=floor((d-1)/2). Then

    S_*={1,3,...,2L-1},
    p_* = t(1-t^(2L))/[(1+t)(1-t^d)].                 (1)

For d=5,t=1/2 this gives p_*=10/31; the optimum probabilities on levels1,3
are4/5,1/5. The preparation cost is ln(31/10), distance21/31. As d grows,
p_* -> t/(1+t), so the infimum cost is ln(1+exp(beta Delta)), strictly
larger than ln2. Cooling at fixed d costs beta Delta+o(1). At beta->0,
p_* -> L/d, but Delta is still nonzero and conservation still resolves shells.
Setting Delta EXACTLY to0 changes their degeneracy and is a different model.

## 4. Resonance, rank and tensor consumers

If the bath gap is m times the A spacing, m a positive integer, the graph
splits into residue classes modulo m. Existence requires d>=2m+1 and the
same independent-set prescription applies on each class. If their gap ratio
is irrational (indeed any noninteger for this equally spaced A), there are
no edges, so exact implementation is impossible from ANY preparation.
This is an exact-conservation statement, not robustness to detuning or finite
interaction duration. Approximations need a quantitative conservation model.

For an extreme rank-k target with k>=3, every shell of B plus nondegenerate A
has dimension at most2, so no preparation realizes it exactly. In particular,
two or more tensor copies of this rank2 extreme target, whose rank is2^N,
cannot be realized with the SAME single qubit bath and any nondegenerate A,
even with unrestricted collective conserving U. This is not a prohibition
on fresh baths, degenerate A, or approximate simulations.

## 5. Hostile review and boundaries

The bath must have both populations nonzero: a zero-temperature pure bath
removes some rank constraints. A support optimizer for arbitrary composite
bath preparation would improperly alter the fixed tau_B tensor sigma product;
our graph optimizer enforces that product. A rank-one unitary target is a
countercontrol to any assertion covering all channels. Degenerate A and
additional baths change shell dimensions. No claim that preparing sigma_* is
free or implementable by the allowed unitary alone is made.

[K1923](k1923-energy-shell-preparation-cost-2026-10-22.md) supplies the reused
extreme shell-rank theorem. [K1930](k1930-energy-shell-catalyst-disturbance-2026-10-22.md)
settles the separate return question; optimal preparation alone says nothing
about repeatability. Related literature: Ng et al.,
[Limits to catalysis](https://arxiv.org/abs/1405.3039), and vom Ende,
[Which Bath-Hamiltonians Matter for Thermal Operations?](https://arxiv.org/abs/2207.11189).
Those works study broader catalytic and resonance questions; no novelty or
exhaustive prior-art claim is made here.

This is independent finite-dimensional mathematics. SC-META-53 remains
UNCERTAIN; it supplies neither this positive Hilbert space nor these energies.
LT-SM8, LT-GR6b and AC-F1 remain unchanged. Native full20/K-C/domain/accessibility
identification remains open. Analytic arguments carry universal scope; exact
finite matrix/combinatorial controls are internal checks, not formal proof or
external expert review. No source, ledger, canon or GU physics verdict changes.

## Reproduction and acceptance

Validation:228+156 finite exact producer controls and34+46 separately
reconstructed controls;6 real mathematical-input faults plus2 report and2 pin
faults rejected after green baselines. Analytic arguments establish universal
scope; finite controls are not formal proof or independent expert acceptance.
A matrix-equality helper error and an immutable-matrix mutation crash were
repaired before final green replay; neither was counted as fault detection.
Run the two scripts in this note's frontmatter with Python3 and SymPy1.14.0;
the producer --write flag refreshes its committed JSON report. The probe
checks report equality and its script digest in addition to the independent
mathematical reconstruction. No certificate claim is made from digest equality.
