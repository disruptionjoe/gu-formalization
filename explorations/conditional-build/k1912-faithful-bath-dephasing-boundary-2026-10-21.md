---
title: "K1912: Faithful bath limits, support cost and thermal repairs"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; no native GU identification, total thermodynamic cost, or novelty
scripts:
  - tests/channel-swings/k1912_faithful_bath_dephasing_boundary.py
  - tests/channel-swings/k1912_faithful_bath_dephasing_boundary_probe.py
---

# K1912: Faithful bath limits, support cost and thermal repairs

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
result: extreme-channel bath support theorem and quantitative thermal witness
carrier: four-level system and specified finite-dimensional environment LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: ordinary complex conjugation; native K/C not identified
grading: population labels; no source graded-IG identification
action_owner: repository-construction -- explicit controlled unitary interactions
target: conditional coherence dynamics and bath resource constraints MAP-TYPE=intertwiner
```


## 1. Which environment preparations can realize the endpoint?

[K1903](k1903-quantum-dephasing-witness-2026-10-21.md)'s rank-two C is an
extreme correlation matrix: its four unit-vector projectors span Hermitian2.
A pure qubit bath realizes it. A finite-temperature Gibbs state is faithful
(full rank), so it changes the realization problem. We do not assume a
thermal-operation or energy-conserving dilation; arbitrary bath unitaries
are allowed. Even with that freedom there is an obstruction.

Let a d-dimensional bath begin in rho, of rank r, and let the endpoint
be a controlled unitary U=sum_j |j><j| tensor U_j. Its Schur coefficients are

    D_jk=Tr(rho U_k* U_j).                                (1)

For ANY extreme correlation C of rank k, exact realization D=C obeys

    d >= k r.                                            (2)

Conversely (2) is sufficient for such a controlled realization with any
prescribed rho of rank r. This is an exact dimension/support condition,
not an energy or entropy equality.

Proof of necessity: every unit vector psi in the support S of rho can appear
with positive weight in an ensemble for rho, since rho is strictly positive
on S. Equation(1) is the same convex mixture of the pure-state correlation
matrices. Extremality forces every one to equal C. Polarization then gives

    P_S U_k*U_j P_S=C_jk I_S.                             (3)

The subspaces U_j S therefore have a tensor-product Gram representation:
the linear map e_j tensor psi -> U_j psi is an isometry from a k*r-dimensional
space, using bath vectors with <e_k,e_j>=C_jk. Hence (2).
For sufficiency, embed C^k tensor S isometrically into the bath and map each
psi in S to e_j tensor psi. Each map is an isometry on S and extends to a
unitary of C^d. Formula(1) is C for every density on S.

For this target k=2, a faithful finite bath has r=d and is impossible.
A mixed but nonfaithful bath is allowed: a pure qubit tensor an arbitrary
r-state spectator has d=2r and saturates (2). Mixedness alone is not the
obstruction. A necessary entropy condition is S(rho)<=log(floor(d/2));
it is not sufficient, since a faithful state can have arbitrarily small
positive entropy. The exact condition is support rank.

The faithful exclusion extends beyond an assumed controlled ansatz. Write
an arbitrary joint endpoint unitary in system blocks U_ab. Exact preservation
of each population basis state implies Tr(rho U_ab*U_ab)=0 for a!=b.
For faithful rho, every off-diagonal block vanishes, so the joint unitary is
controlled. For nonfaithful rho this only restricts the populated support;
the general support proof still applies because its basis-input images are
product states on that support. Initial system-bath correlations and
nonunitary joint processes are not included.

A finite sequence of unitary interactions with fresh faithful cells is also
excluded from reaching C exactly: combine all cells into one finite bath,
whose product state is faithful, and apply the same endpoint argument.
This includes arbitrary intermediate system population mixing if the final
channel preserves populations exactly. The conclusion concerns the extreme
endpoint C, not the nonextreme Poisson semigroup endpoints F(t).
For Gibbs cells at a common beta with bandwidths Delta_l, the combined
version of (8) uses total bandwidth sum_l Delta_l. A growing number of cells
can increase that resource; there is no fixed-total-resource floor when the
total bandwidth is allowed to grow without bound.

Extremality is essential. The four Pauli operations I,X,Y,Z on a maximally
mixed qubit have normalized-trace correlation I4, the complete dephasing
channel. Here d=2, rank(rho)=2 and rank(I4)=4, so applying (2) without
extremality would be false. Complete dephasing is a classical mixture;
K1910's four-dimensional lower bound was explicitly for a PURE bath.

Nonfactorizable Schur maps are established prior art: see
[Haagerup and Musat, Corollary2.3 and Example3.2](https://arxiv.org/abs/1009.0778).
Their tracial factorization framework must not be identified with every
nontracial bath dilation. We give the elementary support argument and the
following explicit witness for the present finite bath class; no novelty
claim is made.

## 2. A dimension-uniform quantitative witness

Keep K1903's B and H=B*B:

    B=[-1 -1 sqrt2 0; -1 i 0 sqrt2], delta=6-4sqrt2.

For D from(1),

    Tr(H D)=Tr(rho R1*R1)+Tr(rho R2*R2),
    R1=sqrt2 U3-U1-U2, R2=sqrt2 U4-U1+iU2.               (4)

For normalized trace tau=Tr/d, the exact lower bound is

    tau(R1*R1+R2*R2) >= delta.                            (5)

To prove it, multiply all unitaries on the left by U1*, then diagonalize
W=U1*U2. Let its eigenvalues be w_l, |w_l|=1. For any unitary V and diagonal
A, expansion of the Frobenius norm and |V_ll|<=1 gives

    ||sqrt2 V-A||_F^2 >= sum_l (sqrt2-|A_ll|)^2.

Use A=I+W and I-iW. The right side of the sum of the two inequalities is
at least d delta by K1903's scalar arbitrary-phase inequality, applied to
each w_l and the individually minimizing phases. Scalar multiples of the
identity with z=(1,1,1,(1-i)/sqrt2) attain delta. Thus(5) is sharp for
tracial baths of every dimension, not merely a numerical unitary search.

If lambda_min(rho)=lambda, positivity of the residual in(4) implies

    Tr(H D) >= d lambda delta.                           (6)

The target C has witness0. If D is a correlation matrix and every off-diagonal
entry differs from C by at most epsilon, the exact off-diagonal absolute
coefficient sum of H is10sqrt2. Therefore

    epsilon >= d lambda delta/(10sqrt2).                 (7)

Also ||D-C||_1>=d lambda delta/(4+sqrt2), giving output trace-distance
at least d lambda delta/[8(4+sqrt2)] on the equal-superposition input.
This is a necessary approximation floor for population-fixing channels;
we have not proved a robust reduction for channels with population leakage.
The factor d lambda in(6)-(7) is valid, but sharpness is asserted only for
(5), not for arbitrary rho or the entrywise error constant.

For a Gibbs bath rho=exp(-beta H_E)/Z, beta>=0 and spectral bandwidth
Delta=Emax-Emin, d lambda>=exp(-beta Delta). Thus achieving entry tolerance
epsilon requires, whenever the right side is positive,

    beta Delta >= log[delta/(10sqrt2 epsilon)].           (8)

At fixed finite beta and bounded bandwidth, enlarging d does not remove this
floor. Increasing bandwidth, cooling, nonfaithful preparation or changing the
model can change the conclusion. No infinite-dimensional theorem with
lambda_min=0 is inferred from (6).

## 3. Explicit thermal repair, and why thermal is not classical

Use the actual qubit unitaries

    U1=I, U2=X,
    U3=[1 -1;1 1]/sqrt2,
    U4=[1 -i;-i 1]/sqrt2.

Their ground columns are the e_j in K1911. For rho_q=diag(1-q,q),
0<=q<=1/2, the endpoint is

    C_q=(1-q)C+q C_exc,                                  (9)

where C_exc is the Gram channel from the excited columns. Direct exact
calculation gives Tr(H C_exc)=4 and

    ||C_exc-C||_max=sqrt2,
    Tr(H C_q)=4q, ||Phi_Cq-Phi_C||_diamond<=2q.            (10)

C_q is still nonclassical whenever q<delta/4, since every classical phase
law has witness at least delta. Thus a faithful bath can produce nonclassical
noise. What it cannot produce exactly is this extreme endpoint C.
For a qubit gap Delta, q=1/(1+exp(beta Delta)); (9) supplies an explicit
sufficient cooling bound to complement the general necessary bound(8).
These bounds need not coincide, and no temperature optimum is claimed.

## 4. Released process and finite-circuit consumer

Replacing each Poisson collision C by C_q gives the exact abstract semigroup
T_t^q=exp[t(Phi_Cq-Id)]. Duhamel and channel contractivity give

    ||T_t^q-T_t||_diamond<=2tq.                          (11)

Equivalently couple each Poisson event to the wrong collision with probability
q. This is an ideal externally timed collision model, not yet a bounded
continuous spatial coupling.

At t=1/110, K1909's output separation greater than1/176000 survives for
q<1/1600, equivalently beta Delta>log1599. This is a conservative sufficient
thermal process threshold, not the onset of nonclassicality.

For a fully finite controlled construction, take an independent pure event
flag in sqrt(1-h)|0>+sqrt(h)|1> and the thermal qubit rho_q. Apply U_j only
in the event-flag1 sector. This gives (1-h)Id+h Phi_Cq exactly with a
four-dimensional cell of rank2; preparation of the pure flag is an explicit
extra resource. Combining(4) of K1911 with(11) gives at grid time t=nh

    half-diamond error from T_t <= t(h+q).                (12)

For example t=1/110, n=30, h=1/3300, q=1/6400 obey
h+q<1/1600, so a finite30-cell circuit still yields a nonclassical endpoint.
The thermal qubit has beta Delta=log6399. The composite cell is nonfaithful
because of the pure flag, so this construction does not evade(2) or prove a
faithful-cell exact realization. Transport, flag preparation, clock, reset
and continuum sea energy remain separately unpriced.

## 5. Hostile review

Strongest overclaim: all faithful quantum noise is classical, refuted by(9).
Strongest contrary construction: mixed spectator tensor pure qubit saturates
the exact support bound, showing why full rank matters. Weakest seam:
noncommuting rho cannot be diagonalized simultaneously with the unitaries.
The proof uses rho>=lambda I only after forming a positive residual; the
spectral reduction is performed solely in the tracial comparison. The
producer checks target extremality, residual identities, exact repair and
coefficients; the probe independently forms Kraus/column correlations and
support-saturating dilations. Universal dimension and unitary claims are
carried by the analytic argument, not those finite examples.


## Source and verification boundary

SC-OP-04 ASSERTS a candidate four-field operator grammar, SC-MAS-01 and
SC-CHI-02 ASSERT the stylized curvature-mass toy, and SC-META-53 remains
UNCERTAIN about unbounded spectra. None selects these positive Hilbert bath
models, their accessible algebra, coupling, clock, spectrum or physical units.
LT-SM8, LT-GR6b and AC-F1 remain unchanged. Full20 injection, separate K/C,
physical domain and accessibility are independent construction debts.
No source/physics-ledger/canon verdict, GU recovery, novelty, external expert
review or formal proof is claimed. General statements rest on the analytic
arguments above; exact probes check finite matrices and identities, while
report and pin faults test only consistency and provenance.
