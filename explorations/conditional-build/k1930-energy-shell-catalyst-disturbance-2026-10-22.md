---
title: "K1930: A sharp uniform catalyst disturbance floor"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact supplied finite energy models; no native GU, novelty or formal proof
scripts:
  - tests/channel-swings/k1930_energy_shell_catalyst_disturbance.py
  - tests/channel-swings/k1930_energy_shell_catalyst_disturbance_probe.py
---

# K1930: A sharp uniform catalyst disturbance floor

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

## 1. Exact endpoint

Use K1929's four-state extreme Schur target, faithful thermal qubit, arbitrary
nondegenerate finite catalyst Hamiltonian and exact additive conservation.
For every initial catalyst sigma and every joint U implementing the full target
exactly, define

    r = sup_rhoS (1/2)||sigma'_A(rhoS)-sigma||_1.

Whenever implementation is feasible,

    r >= 1/2,                                         (1)

and equality is achievable. The infimum over ALL preparations and conserving
unitaries is exactly1/2, independent of catalyst dimension, energy range,
bath temperature (finite beta) and system diagonal energies. The lower bound
allows coherent sigma, population mixing on unoccupied inputs, and final
bath/catalyst or system/catalyst correlations. It is a MARGINAL return bound;
the achieving construction does not return a product catalyst. The system
channel itself is exact for entangled inputs as well.

## 2. Support measurement proves the lower bound

Let S={n:sigma_nn>0}, P=I_B tensor P_S. K1929 proves that each occupied total
energy shell contains exactly ONE active basis vector a_E, with weight w_E>0,
and has dimension2. The weights sum to1. In that shell the two basis-system
inputs j=1,2 have physical output vectors x1,E and x2,E. Positive population
preservation and exact energy conservation place them in that same shell;
extremality forces their Gram matrix to be the target, so they are orthogonal.
They span the shell and

    (|x1,E><x1,E|+|x2,E><x2,E|)/2 = I_E/2.

P has rank1 in each occupied shell. Therefore for the system input that mixes
j1 and j2 equally, the final probability of A belonging to its ORIGINAL
support S is EXACTLY1/2. Initially it is1. A two-outcome support measurement
then gives trace distance at least1/2. At least one of the two pure basis inputs
also has support probability at most1/2, hence return distance at least1/2.

Coherence between catalyst levels does not evade this proof. P commutes with
total environment energy, so all cross-shell terms have zero contribution to
Tr(P Omega'). Positivity confines sigma to S, and the shell blocks of tau_B
 tensor sigma are still diagonal rank1. This is a physical support measurement
on A alone; inaccessible purification information is not substituted for it.

## 3. Matching construction for every diagonal feasible preparation

Choose any allowed S and any diagonal sigma supported there, including K1929's
preparation optimum. In each occupied two-dimensional shell choose a partner
basis vector b_E outside P, and define the isometry W_E by

    W_E e0=(a_E+b_E)/sqrt2,
    W_E e1=(a_E-b_E)/sqrt2.

Map the active input a_E to W_E v_j and extend to a full shell unitary for each
j. Their controlled direct sum is exactly conserving and realizes all entries
of C. The occupied-basis probabilities of W_E v_j are

    c1=c2=c4=1/2, c3=1.

Tracing B removes the a_E/b_E cross term because they have different bath
levels (and different A energies). Summing all shells gives

    sigma'_A(|j><j|)=c_j sigma+(1-c_j) omega,

where omega is a normalized diagonal state supported outside S, independent
of j. Hence the return distance is1-c_j. For arbitrary system inputs,
tracing S removes the control cross terms, and convexity gives r=1/2.
Any external reference has no effect on this marginal assertion. This supplies
a matching minimax protocol, not only a lower bound or one selected prior.
For a ladder with bath excited probability q=t/(1+t),

    omega_n=(1-q)sigma_(n+1)+q sigma_(n-1),             (2)

with out-of-range entries zero. Internal support ensures normalization.
For d=5,t=1/2,sigma=(0,4/5,0,1/5,0),

    omega=(8/15,0,2/5,0,1/15).

The catalyst is unchanged on basis input j3 but changes by1/2 on j1,j2,j4;
that is compatible with K1925's information-consumption obstruction. On the
half j1/j2 prior the total environment entropy increases ln2. Energy can
move between A and B; no claim of ln2 CATALYST entropy increase is made here.

## 4. Rank-one shell bottleneck and qutrit extension

The lower-bound argument needs only: every occupied shell of tau_B tensor
sigma has rank1; P=I_B tensor P_S has rank1 there; and the target has two
orthogonal Gram vectors. It still gives r>=1/2 when shell dimension is greater
than2, because the projector onto two orthogonal outputs has expectation at
most1 on any rank-one P. The matching construction works whenever one can
choose a basis partner outside S in each occupied shell, with a different bath
label. For nondegenerate A, two distinct states at the same total energy
necessarily have different bath labels, so this condition is automatic.
For diagonal feasible sigma the same c_j construction attains1/2.

In particular take a thermal THREE-level bath with energies0,Delta,2Delta,
and A's d-level equal ladder. Shell dimensions are at most3; the extreme rank2
condition forces every occupied shell to have rank1. Exact feasible support
is S subset{1,...,d-2}, with any two elements separated by AT LEAST3.
The endpoints are excluded by the unique lowest/highest shells; separation
follows from the three-level convolution windows. Conversely these conditions
satisfy every shell rank constraint, including the two-dimensional edges.
The same greedy argument gives S_*={1,4,...,1+3(M-1)}, M=floor(d/3), and

    p_* = t(1-t^(3M))/[(1+t+t^2)(1-t^d)].              (3)

The preparation minima are -ln p_* and1-p_*, and r_min=1/2 for every d>=3.
Thus merely replacing the qubit with a qutrit does not release small return.
A bath/catalyst architecture with occupied shell rank at least2 is necessary
to escape THIS bottleneck; it is not by itself sufficient for vanishing r.
The first such possibility for rank2 needs a shell dimension at least4.

## 5. What this closes and what remains

K1928 allows arbitrary small return with degenerate H_A=H_B=0. The present
specified nondegenerate, fixed-small-bath model has exact optimum1/2 even with
unbounded ladder length. This identifies the role of shell geometry, rather
than treating dimension alone as a resource certificate. Exact detuning can
remove feasibility altogether (K1929); zero gap merges shells. Neither result
is a finite-error continuity bound. In particular a small nonzero channel
error may alter exact support ranks. An approximate-channel extension must
replace the rank argument with quantitative tomography/leakage estimates;
no such uniform extension is claimed here.

Strongest contrary route: degenerate A restores large shell ranks and permits
K1928. Coherent sigma is covered by the support-measurement lower proof; the
matching diagonal construction proves the global minimum without needing to
optimize coherences. Nonextreme/diagonal-unitary channels are countercontrols
to a universal channel prohibition. Exact tensor targets of rank>=4 cannot be
implemented at all with qubit or qutrit B and nondegenerate A. Fresh baths,
multiple bath cells, approximate conservation and local-control synthesis are
separate models, not implicit resources in this theorem.

The proofs reuse K1923's exact shell criterion and the orthogonal physical
outputs underlying K1925, with a new constrained minimax construction.
[Ng et al.](https://arxiv.org/abs/1405.3039) already study limits of catalytic
thermodynamics, and [vom Ende](https://arxiv.org/abs/2207.11189) studies bath
resonance. No general novelty claim follows from these exact model calculations.
SC-META-53 remains UNCERTAIN and the GU-native physical quotient is not supplied.
LT-SM8, LT-GR6b and AC-F1 do not move. No expert, formal-proof, infinite-bath,
sharp finite-error, total-work or native GU claim is made.

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
