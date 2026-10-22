---
title: "K1924: A quantitative bound for imperfect energy conservation"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1924_conservation_defect_channel_bound.py
  - tests/channel-swings/k1924_conservation_defect_channel_bound_probe.py
---

# K1924: A quantitative bound for imperfect energy conservation

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
result: weighted energy-shell leakage bound on full-channel approximation
carrier: four-level supplied target and arbitrary finite Gibbs bath LAYER=toy CHIRALITY=N/A
pairing: Gibbs-weighted Hilbert-Schmidt norm and normalized Choi trace ON=finite_product_dilation
real_structure: complex adjoint and shell spectral projections
grading: system population labels and bath energy shells only
action_owner: repository-construction -- arbitrary joint endpoint unitary with measured commutator defect
target: necessary control resources for approximating the supplied Schur channel MAP-TYPE=intertwiner
```

## 1. Replace exact conservation by a measured defect

Reuse K1922's four-level target, B, H=B*B, delta=6-4sqrt2 and h=4+sqrt2.
Set a=delta/(4h), c0=a/4. H_S is diagonal in the target population basis,
tau=exp(-beta H_B)/Z is a finite Gibbs bath and U is now ANY joint unitary.
No exact conservation assumption is made. Define its diagonal system blocks
A_j=U_jj, the bath energy pinching E(X)=sum_e P_e X P_e, D_j=E(A_j), and

    ell_j=1-Tr(tau A_j* A_j),
    q_j=||(A_j-D_j) sqrt(tau)||_F^2,
    pbar=sum_j ell_j/4, Q=sum_j q_j/4.                   (1)

If t is normalized Choi trace distance to the target, then

    sqrt(t)+sqrt(pbar+Q) >= sqrt(a).                     (2)

For full-channel half-diamond error epsilon, t,pbar<=epsilon. Therefore

    epsilon >= f(Q):=(max(a-Q,0))^2/(4a).                (3)

At Q=0 this recovers K1922's dimension-independent floor c0. The quadratic
loss in(3) is a sufficient necessary bound, not a sharp channel-distance
optimum. Q measures off-energy transitions in the population-retaining
blocks. Large energy-nonconserving population transitions are already counted
by pbar. It is neither mean work nor simply a Hamiltonian expectation shift.

## 2. Proof: weighted orthogonality prevents a linear defect loss

Because tau is scalar in every shell, E is an orthogonal projection for
<X,Y>_tau=Tr(tau X*Y). It is unital completely positive, so each D_j is a
contraction. Pythagoras gives

    1-||D_j sqrt(tau)||_F^2=ell_j+q_j.                   (4)

Extend the polar part of D_j to a unitary V_j separately in each shell.
The scalar singular-value inequality (1-s)^2<=1-s^2 for0<=s<=1 yields

    ||(D_j-V_j)sqrt(tau)||_F^2<=ell_j+q_j.              (5)

The tracial shell residual from K1912 is at least delta for these V_j.
Writing W_D=sum_l ||sum_j B_lj D_j sqrt(tau)||_F^2, the triangle inequality
and ||B||^2=h imply

    sqrt(W_D)+sqrt(h sum_j(ell_j+q_j))>=sqrt(delta).

Weighted orthogonality applies also to each B-linear residual, so
W_A=W_D+W_(A-D)>=W_D. The actual normalized Choi effect gives
W_A<=4h t, exactly as in K1913. These prove(2). To solve it when0<=Q<a,
write sqrt(epsilon)+sqrt(epsilon+Q)>=sqrt(a). At equality
sqrt(epsilon)=(a-Q)/(2sqrt(a)); monotonicity proves(3). For Q>=a the bound
is0. No triangle estimate on A_j-D_j is inserted, which would lose the
quadratic structure and give a weaker result.

## 3. Released energy-gap and control-duration consumers

Suppose H_B has at least two distinct energies and minimum distinct-shell gap
g>0. Exact spectral expansion gives

    ||[H_B,A_j]sqrt(tau)||_F^2
       =sum_(e,f) (E_e-E_f)^2 ||P_e A_j P_f sqrt(tau)||_F^2
       >= g^2 q_j.                                     (6)

Define D2=(1/4)sum_j ||[H_B,A_j]sqrt(tau)||_F^2.
Then Q<=D2/g^2, hence epsilon>=f(D2/g^2). No dimension factor appears in
this WEIGHTED measured defect. If H_B is scalar, Q=0 identically and the
original c0 floor holds for a Gibbs bath without any need for g.
A collapsing nonzero gap destroys a bound stated only in energy units; it
must not be ignored when passing to large reservoirs.

For H_tot=H_S tensor I+I tensor H_B and omega=I4/4 tensor tau, diagonal
blocks of [H_tot,U] are [H_B,A_j]. Thus

    D2<=||[H_tot,U]sqrt(omega)||_F^2<=||[H_tot,U]||_op^2. (7)

For a supplied differentiable unitary path U'= -iK(t)U, U(0)=I, integration
of d(U*H_tot U)/dt gives

    ||[H_tot,U(T)]||_op <= J(T):=int_0^T ||[H_tot,K(t)]||_op dt. (8)

Combining (3),(6)-(8), epsilon>=f((J/g)^2). In particular reaching any
specified epsilon0<c0 requires

    J >= g sqrt(a-2 sqrt(a epsilon0)).                   (9)

If ||[H_tot,K(t)]||<=v, v>0, this yields the duration lower bound
T>=g sqrt(a-2sqrt(a epsilon0))/v. At epsilon0=0, J>=g sqrt(a).
For a faithful finite Gibbs bath exact realization is already impossible by
K1912, even with arbitrary drive: the endpoint0 condition here is only a
necessary limiting control condition, not sufficiency or a new exact route.
An arbitrarily large diagonal drive can have J=0; amplitude alone is not the
resource measured by this bound. Units: g is energy, J is energy in hbar=1.

## 4. Released preparation and implementation robustness

Let the actual initial bath rho have half trace distance r from tau. Let the
actual implemented channel be within half-diamond eta of the channel induced
by the specified U and rho. Using the SAME U with tau changes half-diamond
distance by at most r. Consequently

    epsilon_actual+r+eta >= f(Q_tau),                   (10)

and the gap/control versions follow by replacing Q_tau with the upper bounds
above. Q is evaluated with the reference Gibbs state, not an unmentioned
physical-state norm. Formula(10) connects independently supplied purity and
control resources but does not solve their sharp joint optimization.

For a two-level bath, (6) is equality for EVERY matrix A_j because all
nonzero transitions have the same absolute energy gap. A controlled rational
qubit rotation with sine4/5 in one system block has ell=0, q=16/25 for that
block, Q=4/25 and D2=g^2 Q. At g->0 its energy commutator tends to0 while Q
stays fixed as long as g>0: small absolute commutator without a fixed gap is
not a uniform conservation approximation. At g=0 the pinching changes to
one full shell, Q=0, which is a different decomposition.

A second control uses resonant system-population mixing with exact total
energy conservation. It has Q=0 but nonzero pbar, confirming that(2) has not
silently assumed a controlled-unitary ansatz. Weighted residual Pythagoras
is independently checked on noncommuting blocks and a nonuniform Gibbs state.

## 5. Hostile review and limits

The load-bearing transfer is orthogonal pinching in the Gibbs-weighted norm,
not ordinary Frobenius projection with arbitrary rho. Mere commutation of a
nonthermal state with H_B need not make it scalar on degeneracies. K1923's
within-shell purity is an explicit way to change that premise. We never apply
the tracial lower bound directly to such a state. Population leakage, Choi
normalization, complex conjugation in B and energy-gap factors are checked
separately. Report consistency alone is not mathematical verification.

This specializes the existing K1912 tracial witness and K1913 leakage proof
using a finite spectral conditional expectation. It is not a sharp minimum
work, optimal circuit time, bath-temperature tradeoff, catalytic theorem or
claim that small expectation-value work forces small Q. No energy expectation
is substituted for the operator commutator in(8).

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its nonzero southeast rival. SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass
toy; SC-META-53 remains UNCERTAIN about indefinite spectra. None selects
this positive Hilbert channel, bath preparation, Hamiltonian or units.
LT-SM8, LT-GR6b and AC-F1 remain unchanged. Full20 paired injection, separate
K/C, physical domain and accessible algebra remain construction obligations.
No source-register, physics-ledger or canon verdict changes. This is an
independent finite-dimensional mathematical result, with no novelty, native
GU prediction, expert acceptance, infinite-reservoir or formal-proof claim.
Analytic proofs carry universal scope. Finite exact controls test actual
matrices and combinatorics; reporting and dependency checks are separate.
