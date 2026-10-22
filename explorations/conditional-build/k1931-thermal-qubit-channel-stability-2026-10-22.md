---
title: "K1931: The thermal-qubit return obstruction is stable at small channel error"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conservative supplied finite-model bound; no sharp modulus or native GU claim
scripts:
  - tests/channel-swings/k1931_thermal_qubit_channel_stability.py
  - tests/channel-swings/k1931_thermal_qubit_channel_stability_probe.py
---

# K1931: The thermal-qubit return obstruction is stable at small channel error

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: uniform approximate-channel catalyst-return and preparation lower bounds
carrier: four-state system, thermal qubit, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, diamond norm, relative entropy ON=independent_product_input
real_structure: complex adjoint; arbitrary coherent catalyst preparation
grading: additive energy shells, not chirality
action_owner: repository-construction -- exact conserving joint unitary
target: supplied extreme Schur channel MAP-TYPE=intertwiner
```


## Statement

S is four-dimensional, with any Hamiltonian diagonal in the displayed basis. The target is the Schur channel with v1=(1,0), v2=(0,1), v3=(1,1)/sqrt(2), v4=(1,i)/sqrt(2) and C_jl=<v_l,v_j>. B has energies 0,Delta with Delta>0 and faithful diagonal Gibbs weights 1-q,q, 0<q<=1/2. A is finite and its Hamiltonian has nondegenerate energies. Its initial sigma is arbitrary, including coherent and rank deficient, independent of S,B. U is any unitary commuting with the additive total Hamiltonian. Population leakage and all final correlations are allowed.

Let epsilon=||Phi-Phi_C||diamond/2. Define delta=6-4sqrt(2), h=4+sqrt(2), c0=delta/(16h), and eta0=min(1,epsilon/(q c0)). For the SINGLE fixed input rho12=(|1><1|+|2><2|)/2, the catalyst marginal return obeys

    D(sigma'_A(rho12),sigma) >= max(0, 1/2 - 2(1+sqrt(2))*sqrt(h epsilon) -5epsilon -(5/2)eta0).

Consequently the same lower bound holds for worst-case marginal return. At fixed q>0 it implies liminf r>=1/2 as epsilon->0 uniformly over catalyst dimension, bandwidth, spectrum and system diagonal energies. Constants are deliberately conservative and neither a sharp modulus nor novelty is claimed.

## 1. The physical measurements ignore initial energy coherences

Set E=B tensor A, Omega=tau_B tensor sigma and A_j=<j|U|j>. Conservation gives [A_j,H_E]=0, and each A_j is a contraction. Hence the retained Gram coefficients Tr(Omega A_j* A_l), all quadratic residual norms in A_j, and leakage ell_j=Tr(Omega(I-A_j*A_j)) depend only on the energy pinching Omega_d=tau_B tensor diag(p), p_n=sigma_nn. Nondegeneracy of H_A is used here to identify this pinching with diagonal p.

For ANY diagonal catalyst projector P_S and fixed basis input j, the observable I_S tensor I_B tensor P_S commutes with H_tot. Its conjugate by U also commutes. Thus the final probability of P_S for this input depends only on Omega_d. The same holds for rho12. Initial Tr(P_S sigma)=sum_S p_n. We use this genuine catalyst measurement to lower-bound trace distance; we do NOT replace the physical catalyst by a purifying reference or assert equality of its whole coherent output state with a dephased calculation.

## 2. Scalar shell weight is small

Each H_E shell has dimension1 or2. In a two-dimensional shell with adjacent catalyst levels m,n (E_n=E_m+Delta), Omega_d has diagonal entries a=(1-q)p_n and b=q p_m. Split it as min(a,b)I_2 plus a positive rank-one excess. A singleton shell is entirely scalar. Let alpha be the total trace of all these scalar parts. This is a positive decomposition Omega_d=Omega_sc+Omega_ex, not a convex mixture of independently chosen physical preparations.

The K1912/K1922 normalized-trace witness, for the +i target convention, is B=[-1,-1,sqrt2,0; -1,-i,0,sqrt2], H=B*B, ||H||=h. Complex conjugation of the older -i witness changes no constant. Put

    W=Tr(Omega_d sum_l (sum_j B_lj A_j)* (sum_j B_lj A_j)).

If alpha=0, the scalar-mass bound is immediate. For alpha>0, normalize
Omega_sc/alpha; polar completion inside each shell gives

    sqrt(W_sc/alpha)+sqrt(h sum_j ell_sc,j/alpha) >= sqrt(delta).

This is exactly the scalar-shell tracial lemma; it does not assume zero population leakage. Multiplying by sqrt(alpha), then using positivity of both residuals and I-A_j*A_j on the excess component, yields

    sqrt(W)+sqrt(h sum_j ell_j) >= sqrt(alpha delta).

The positive normalized-Choi witness gives W<=4h epsilon. Each population leakage ell_j<=epsilon, so sum_j ell_j<=4epsilon. Therefore

    alpha <=16h epsilon/delta = epsilon/c0.

The Choi witness is load-bearing: distance of a convex mixture to an extreme point cannot simply be bounded component by component.

## 3. Weighted graph rounding

The resonance graph on A is a union of finite paths, with edges at energy difference Delta. Remove every path endpoint (both occurrences of an isolated vertex are treated as one vertex). For each edge also remove an endpoint of smaller p weight; ties can be fixed deterministically. Let S be the remaining vertices and eta=sum_(n notin S) p_n. S is internal and independent, so each occupied shell arising from a catalyst level in S is two-dimensional and has exactly one basis vector in I_B tensor P_S.

The sum of weights removed at endpoints is at most the scalar singleton mass divided by q: the low endpoint appears in a singleton with factor1-q>=q, the high endpoint with q, and an isolated vertex has total singleton mass p_n. The sum of the smaller p endpoint over edges is at most the scalar two-dimensional mass divided by2q, since min((1-q)p_n,q p_m)>=q min(p_n,p_m). Taking a union only reduces removed weight. Thus

    eta <= alpha/q <= epsilon/(q c0), and eta<=1.

This is a constructive dimension-independent rounding argument; no discontinuous rank inference is made from approximate data.

## 4. Rank-one support bound with actual leakage

Index the environment basis inputs selected by S with a, of weights w_a=(tau_B)_b p_n. Their total weight is m=1-eta. Write x_j,a=A_j a inside a's two-dimensional shell, n_j,a=||x_j,a||^2<=1, and z_a=<x_1,a,x_2,a>. Define

    r3,a=x_3,a-(x_1,a+x_2,a)/sqrt2,
    r4,a=x_4,a-(x_1,a+i x_2,a)/sqrt2,
    Rk=sum_selected w_a ||rk,a||^2.

Since W includes all inputs, R3+R4<=W/2<=2h epsilon. Put k=1+sqrt2. The norms of (x1+x2)/sqrt2 and (x1+i x2)/sqrt2 are at most sqrt2. Comparing each with x3 or x4, whose norm is at most1, gives the pointwise inequalities

    (Re z_a)_+ <= (2-n_1,a-n_2,a)/2 + k ||r3,a||,
    (-Im z_a)_+ <= (2-n_1,a-n_2,a)/2 + k ||r4,a||.

Here u_+=max(u,0). The total weighted deficit in either right side is at most epsilon. Cauchy--Schwarz bounds each weighted residual norm by sqrt(Rk), since selected mass<=1.

Let Z=sum_selected w_a z_a. The FULL retained channel coefficient between labels1,2 has target zero and absolute value at most2epsilon. The discarded component has absolute value at mosteta since ||xj||<=1. Thus |Z|<=2epsilon+eta. Applying |u|=2u_+-u to Re z and -Im z, then |Re Z|+|Im Z|<=2|Z|, gives

    sum_selected w_a |z_a|
       <=2k(sqrt(R3)+sqrt(R4))+4epsilon+2|Z|
       <=4k sqrt(h epsilon)+8epsilon+2eta.             (*)

The support projector I_B tensor P_S has rank1 in every selected shell. The largest eigenvalue of |x1><x1|+|x2><x2| equals the largest eigenvalue of their 2x2 Gram matrix, and is at most1+|z_a| (diagonal entries<=1, Gershgorin). Thus the population-retaining contribution to the support probability for rho12 is at most m/2+(sum w|z|)/2. Other system-population outputs add at mostepsilon. Discarded initial inputs add at mosteta. No cross-shell or selected/discarded coherence contributes to this energy-commuting measurement.

Initially the support probability is m. Its drop is therefore at least

    m - [m/2 +(sum w|z|)/2 +epsilon+eta]
      >=1/2 -2k sqrt(h epsilon)-5epsilon-(5/2)eta,

using (*). Replace eta by its upper bound eta0 and clip at zero. The two-outcome catalyst measurement contracts trace distance, proving the statement for rho12.

## 5. Preparation and resonance consumers

Let tau_A be Gibbs and let p_* be K1929's maximum Gibbs mass over internal independent sets of the resonance graph. The rounded S has p(S)>=1-eta0 and tau_A(S)<=p_*. Whenever 1-eta0>=p_*>0, binary measurement and relative entropy monotonicity give

    D(sigma||tau_A) >= d_bin(1-eta0 || p_*),
    D_trace(sigma,tau_A) >= max(0,1-eta0-p_*).

Otherwise use the nonnegative zero relative-entropy bound. The monotonicity in both binary arguments requires the displayed ordering; do not use this expression unconditionally. Hence the exact preparation minima are continuous lower limits as epsilon->0 at fixed q and spectrum, even though exact support rank is not continuous. For a varying ladder at fixed beta Delta, its explicit p_* may be substituted without altering the proof.

If no internal independent vertex exists, rounding forces eta=1, so epsilon>=q c0. For a completely nonresonant spectrum all shells are singleton and alpha=1, giving the stronger epsilon>=c0. Neither statement assumes a faithful catalyst. If q tends to zero jointly with epsilon, this bound may become vacuous; finite-temperature uniformity means q is fixed or bounded away from zero. A degenerate A or a larger bath invalidates the <=2D shell geometry and is a distinct model.

## 6. Controls and limits

At epsilon=0, alpha=eta=0 and the bound exactly reproduces K1930's1/2 floor. The factor1/q in graph rounding cannot be removed: on a two-vertex path with all catalyst probability at its high endpoint, alpha=q and eta=1. A controlled identity channel gives large target error and is not ruled out. A nonextreme target does not have this witness. The +i versus -i fourth vector requires conjugating B. True degeneracy and exactly zero gaps change shell dimensions; they are not limits covered by the uniform statement. Exact additive conservation remains essential. No GU claim, native physical identification, sharp-error theorem, independent expert acceptance, formal proof or novelty is asserted.

## Evidence, context and reproduction

The reused scalar-shell witness is derived in
[K1912](k1912-faithful-bath-dephasing-boundary-2026-10-21.md) and the population-leakage extension in [K1922](k1922-energy-conserving-thermal-channel-floor-2026-10-22.md);
see the exact source paths below if following this result. The exact reference
endpoints are [K1929](k1929-resonant-ladder-preparation-2026-10-22.md) and
[K1930](k1930-energy-shell-catalyst-disturbance-2026-10-22.md).
[K1932](k1932-four-level-bath-catalyst-return-2026-10-22.md) constructs an actual
larger-bath escape; its hypotheses violate this theorem's qubit condition.
The entropy preparation bound is a binary-measurement/data-processing
consumer, not a new optimizer. There is no exact-rank continuity assumption.

SC-META-53 remains UNCERTAIN; the positive Hilbert space, energies and channel
are supplied independent mathematics. LT-SM8,LT-GR6b,AC-F1, source ledgers and
canon do not change. Neither this theorem nor K1932 supplies GU-native
full20/K-C/domain/accessibility data. Known catalytic constraints such as
[Ng et al.](https://arxiv.org/abs/1405.3039) are relevant background; no
novelty or full literature review is claimed.

Run both frontmatter scripts with Python3 and SymPy1.14.0; producer --write
refreshes JSON. Producer6541 exact checks include3258 weighted graph cases;
independent probe744 controls include separately optimized support,
coherent physical measurement, nonzero leakage, all16 complex matrix units
and the wrong-phase negative control. After a green baseline it rejects3
mathematical input faults plus1 report and1 pin fault. These finite checks
are supplementary; the universal theorem is the analytic argument above.
Internal independent derivation and review are not external expert acceptance
or formal proof. An unavailable-SymPy interpreter was replaced before tests;
no import failure was counted as a mathematical fault detection.
