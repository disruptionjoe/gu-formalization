---
title: "K2392 Optimal noisy-clock recovery for arbitrary planar angle laws"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2392_nonaligned_clock_recovery_probe.py
---

# K2392 Optimal noisy-clock recovery for arbitrary planar angle laws

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2392
carrier: K2389 flagged loss instrument, classical survivor sign, coherent clock qubit and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert pairing and half-diamond channel distance ON=declared_carrier
real_structure: complex qubit channels and real planar first/second moments
grading: good flags and two-loss sign blocks
action_owner: repository-construction -- supplied K2389 QND clock/loss instrument
target: all-CPTP optimum for a known arbitrary angle law MAP-TYPE=evaluation
```

## General pointwise optimum

[K2389](k2389-clock-pointer-recovery-2026-10-31.md) solves uniform/minimax and aligned-mean angle laws. Here the mean need not be a principal axis of the second moment. The exact all-CPTP optimum reduces to a four-by-four Choi semidefinite program, and its Bell optimum equals the half-diamond optimum. An exact criterion determines when the identity-pointer decoder is already optimal. A nonaligned law supplies a strict counterexample to transferring the aligned formula.

These are finite-channel mathematical results for the supplied clock instrument. SC-META-53 remains UNCERTAIN; LT-GR6b and ledger0.263 remain unchanged. No native GU quotient, measured clock, loss law or hardware performance is certified.

Rotate the pointer plane to xz and let n be a unit planar random axis with known law. Set m=E n, M=E nn^T. Thus M>=0, tr M=1 and M-mm^T>=0; m is in range M even at singular endpoints. These premises hold for the actual angle law; this note does not infer a law from estimated moments. Let 0<=nu<=1 be pointer visibility, and w the complete probability of the two-loss flag. Good flags of total weight1-w are perfectly recovered as in K2389.

On the normalized two-loss sector, the unnormalized sign blocks are

    J_z(rho)=1/4[(1+z m·r)I+nu(m+z M r)·sigma], z=+1,-1.     (1)

They are completely positive by the underlying integral of positive measure-and-prepare maps. The sign probabilities are generally input-dependent; do not replace them by1/2. Equation(1), including its traces, is the starting instrument.

## Exact primal and dual

For a decoder R with Bloch form r->t+A r, define F=m·t+nu tr(A M). Use the unnormalized Choi matrix J_R, output tensor input order, with tr_out J_R=I. In xz coordinates, let

    C=1/2[(m·sigma) tensor I
          +nu sum_ij M_ij sigma_i tensor sigma_j^T].

Then the exact optimization is

    F_* = max tr(C J), J>=0, tr_out J=I
        = min tr(Y), I tensor Y-C>=0, Y=Y†.                  (2)

The primal is strictly feasible at J=I4/2; the dual is strictly feasible at sufficiently large scalar Y. Compactness of the channel set and strict dual feasibility give attainment and no gap. This is a fixed finite optimization problem, not a numerical optimum claim. Standard Choi/SDP background is described by [Watrous, Semidefinite programs for completely bounded norms](https://cs.uwaterloo.ca/~watrous/Papers/SDPforCBnorms.pdf); the instrument-specific reduction and equality below are proved here.

The complete optimal error is

    e_*=w(3-F_*)/4.                                           (3)

For any exact feasible primal/dual pair, L=tr(CJ)<=F_*<=U=tr Y. These bounds license w(3-U)/4<=e_*<=w(3-L)/4 after the physical symmetry/polar recovery below. Floating solver values alone license neither bound; verify positivity, trace preservation and all matrix conventions on actual certificate bytes.

## Why the fidelity program solves half-diamond distance

Let P=Y Pauli, which negates xz components. Equation(1) obeys J_-(rho)=J_+(P rho P). Bell overlap is invariant under conjugating both input and output by P. Averaging any two sign decoders with their transformed partners permits a single decoder R on each original pointer block, followed by P on the negative sign output, without decreasing the Bell objective. The output flip is AFTER R; applying the same nonunital R after pointer sign correction is not equivalent.

First average R with its channel of complex-conjugated Kraus operators in the computational basis. This is a mixture of two CPTP maps. It is not an implemented antiunitary. Since X,Z are real, it preserves t in the plane and A within the plane, hence preserves F. It removes perpendicular translation and mixed perpendicular/planar entries. Sign pairing alone would not remove perpendicular translation; the reflection step is essential.

The resulting paired channel is unital, with zero perpendicular input column and planar Bloch block

    B=t m^T+nu A M.                                          (4)

Its Bell overlap is (1+tr B)/4. Every O in O(2) is available as a physical output unitary, by lifting it to diag(O,det O) in SO(3). Choose O from the polar decomposition so OB is symmetric positive semidefinite and tr(OB)=||B||_*>=tr B. This remains a permitted decoder; at an optimum it cannot increase F beyond F_*. A common input/output basis rotation diagonalizes OB, preserving comparison to identity. The paired channel is then a Pauli channel with nonnegative planar contractions and third contraction0. Its identity Pauli weight is (1+F_*)/4.

For any decoder the Bell input supplies the lower bound half-diamond error>=1-Bell overlap. For this attained Pauli channel the error is exactly its nonidentity Pauli weight: convexity gives the upper bound and orthogonal Bell outputs give equality. Adding the flagged identity part multiplies error by w. Thus (3) holds over arbitrary CPTP decoders, including reference-entangled inputs, not just a chosen axis or fidelity ansatz.

## Closed-form identity-optimality region

Assume nu>0. The decoder R=identity gives F=nu. It is pointwise optimal if and only if

    m^T M^+ m <= nu^2,                                      (5)

where M^+ is the Moore-Penrose inverse and m belongs to range M. The latter follows from actual moments: v^T Mv=E(v·n)^2=0 implies v·m=0. It must still be checked on supplied numerical moment inputs.

Proof: let |I>> be the unnormalized maximally entangled vector. Complementary slackness at J_id=|I>><<I| forces (I tensor Y-C)|I>>=0. Symmetry of M and tr M=1 imply sum M_ij sigma_i sigma_j=I; consequently the only possible dual is

    Y_id=[nu I+(m·sigma)^T]/2.                              (6)

It has trace nu. Write m=(a,b), M=[[lambda,c],[c,mu]], lambda+mu=1. On the orthonormal Bell complement (|X>>,|Z>>,|iY>>), normalized by sqrt2, the slack is

    H=[[nu mu, -nu c, -b],
       [-nu c, nu lambda, a],
       [-b, a, nu]].                                        (7)

It vanishes on |I>>. The top block is nu times the planar adjugate of M. Schur complement, with its range condition at singular M, gives (5). Conversely (5) makes (6) feasible, matching the identity primal. Necessity follows because any optimal dual must obey the forced complementarity relation. A violated inequality makes identity strictly suboptimal, by compact attainment and strong duality.

At nu=0 the pointer is maximally mixed and only the sign carries information; maximizing m·t gives F_*=||m|| by preparing the pure state along m, followed by the output sign flip. Thus zero visibility is treated directly, without dividing by nu. At nu1, moment feasibility gives m^T M^+m<=1, so identity is always optimal, recovering K2389's arbitrary-law noiseless result. At m0 it is optimal for every visibility. Every two-point nonantipodal planar law with two positive masses has m^T M^-1m=1, so identity is strictly suboptimal whenever nu<1. Antipodal/singular laws instead obey the range-aware form and reduce to the aligned case.

## Exact nonaligned failure of scalar formula transfer

Let the axis law assign masses3/4 to+X and1/4 to+Z; m=(3/4,1/4), M=diag(3/4,1/4), nu=19/20. The mean is not an eigenvector. If one wrongly uses only a²=||m||²=5/8 and lambda=mhat^T M mhat=7/10 in K2389's aligned formula, then a²<nu²lambda=2527/4000, falsely predicting F_*=nu.

In fact m^T M^-1m=1>361/400, and the determinant of (7) is -2223/128000. An explicit better feasible decoder uses translation axis k=(X+Z)/sqrt2. In the (k,k_perp,perpendicular) frame the projected parameters are a=1/sqrt2 and lambda=1/2. Choose the valid diagonal-translated channel

    cos u=19/sqrt439, cos v=361/439,
    y=cos u, zeta=cos v, x=cos u cos v,
    t=sin u sin v=1560sqrt2/(439sqrt439).

Its planar contractions along (k,k_perp) are (x,y) and translation is t along k. The offdiagonal moment in this frame does not enter tr(AM), because this chosen A is diagonal. Direct substitution yields

    F=20/sqrt439 >19/20,
    F²-nu²=1521/175600.                                    (8)

The two-Kraus construction and commuting two-qubit dilation of K2389 implement this map after basis rotation. Its B need not already be symmetric PSD. Apply the permitted output polar rotation before asserting a Pauli/diamond upper bound; this can improve F further. Equation(8) is an exact feasible lower bound on F_*, not a claimed full optimum. It decisively rejects the scalar aligned-formula transfer while preserving K2389's correct aligned theorem.

## An executed rational near-optimal certificate

The companion probe supplies a fully rational feasible decoder and dual for the nonaligned law above. Four rational half-angle tangents, in its explicitly documented input/output rotation convention, are 547/1772, 203/4413, 22184/9189 and -19065/8629. The probe constructs the Choi matrix, checks trace preservation and all fifteen principal minors exactly. Its dual is Y=a I+b X+c Z, with a=50405768/105445577+1/10000000, b=56236105/160093158, c=77233853/750908558. Every principal minor of I tensor Y-C is nonnegative by rational arithmetic.

The resulting objective enclosure is, as decimal display only,

    0.95605275917 < F_* < 0.95605297024.

The saved report contains the exact rational endpoints and their gap, which is strictly less than one millionth. These exact checks certify the interval; the numerical optimization used to discover the coefficients is not acceptance evidence. Thus e_*/w lies between (3-U)/4 and (3-L)/4, and the rational decoder followed by its physical polar output rotation improves strictly on the identity-pointer decoder. The exact polar rotation need not be rational and is not silently priced as a free operation. This is a near-optimal certificate, not a closed-form exact optimum.

## Robustness, synthesis and remaining problem

For two moment/visibility descriptions, any qubit CPTP decoder obeys ||t||<=1 and ||A||_op<=1 (the latter by trace-distance contraction). Hence

    |F_*(m,M,nu)-F_*(m',M',nu')|
       <= ||m-m'||_2+||nu M-nu' M'||_* .                    (9)

This follows uniformly from the objective difference, then taking maxima. It is a stability bound on optimum values. Performance loss from reusing a decoder selected for approximate moments is at most twice that RHS in Bell objective, before a correctly chosen final output rotation. A moment bound does not price physical implementation error or guarantee the true conditional law. For a fixed implemented full channel whose half-diamond error from the ideal complete recovered channel is at most epsilon, triangle inequality gives actual complete error<=e_*+epsilon. Strict improvement over the identity-pointer design requires epsilon and all differing apparatus/control costs fit within its explicit ideal margin; a comparison of two noisy devices needs both error budgets.

Any qubit decoder needs at most four Kraus operators and a four-dimensional reset environment for a Stinespring realization. Choi spectral decomposition supplies this finite construction once an optimizer is specified. It does not supply gate durations, control precision, reset energy, bath engineering or a free polar rotation. Those remain priced separately from K2389's simple decoder gate budget.

The arbitrary-law elementary closed form remains open. Equation(2) closes the exact finite optimization formulation and (5) the identity-optimality decision; it is not a stored optimal J for every input law. The supplied nonaligned fixture now has a rigorous near-matching primal/dual pair. Next derive an elementary arbitrary-law formula or supply a physically justified nonaligned law and price its complete decoder and clock. Source, ledger and canon remain unchanged.

## Verification

Universal statements use the written arguments and independent specialist/cross-review. The companion probe checks Choi normalization, all relevant exact moment/duality matrices, singular and uniform controls, the nonaligned fixture's complete positivity and strict gain, and changed-assumption failures. Finite matrix checks are not independent proofs or hardware observations. No external-expert or proof-assistant certification is claimed.
