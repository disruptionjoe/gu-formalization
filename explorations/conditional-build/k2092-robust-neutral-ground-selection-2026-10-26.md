---
title: "K2092: Robust neutral ground selection and finite-observable bounds"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source-selected state, continuum apparatus, GU verdict or external certification
scripts:
  - tests/channel-swings/k2092_robust_neutral_ground_selection_probe.py
---

# K2092: Robust neutral ground selection and finite-observable bounds

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

## 1. Uniform, typed approximate premises

Use [K2088](k2088-even-ground-selection-2026-10-26.md)'s self-adjoint H with
spectrum outside(-m,m), m>0, Q=1_(H<0), gauge-invariant quasifree covariance
0<=C<=I commuting STRONGLY with H. Let b be antiunitary reversing H. Retain
b^2=-I when present; it is not needed for the inequality. Suppose

    ||b C b^-1-(I-C)|| <= eta.                                (1)

For EVERY normalized positive-energy f of bounded spectral support, set g=bf
and A=a*(g)a(f), a charge-neutral even observable. Require the uniform absolute
witness tolerance omega(A* [G,A])>=-epsilon, epsilon>=0. It is one normalized
witness tolerance, not homogeneous in arbitrary rescalings of A, not finitely
many sampled laboratory tests, and not thermodynamic passivity.

## 2. Sharp square-root operator bound

Put n=<f,Cf>, r=<g,(I-C)g>, k=<f,CHf>,
l=-<g,(I-C)Hg>. Strong stationarity kills cross-sign contractions. Wick's rule
and the derivation give the real expectation

    omega(A* [G,A])=-kr-nl <= -2m nr.                       (2)

Here k>=mn and l>=mr. Antiunitarity and(1) give |n-r|<=eta. Let z=max(n,r).
If z>=eta, nr>=z(z-eta); otherwise the bound below is automatic. Thus

    ||C-Q|| <= delta := min(1,(eta+sqrt(eta^2+2epsilon/m))/2). (3)

To pass from bounded spectral vectors to the operator norm, use their density
in the positive/negative spectral subspaces; every negative vector is b of a
positive one. C is block diagonal under Q, so the larger positive occupation
and negative hole norm is exactly ||C-Q||. No unbounded k limit is required.

For eta=0 the square-root dependence is sharp already at energies +/-m with
positive occupation n and negative hole n: epsilon=2m n^2. For nonzero eta,
choose occupations n>=r>=0 with n-r=eta and epsilon=2mnr. Example m=1,
n=1/2,r=1/4 gives eta=1/4,epsilon=1/4,delta=1/2 exactly.
For an energy band starting at a>m, the same proof replaces m by a, giving
stronger tail control. For exact complement, a target occupation tolerance
z requires the sufficient witness condition epsilon<=2a z^2 on that band.

## 3. Finite-observable operational consequence

Use T(rho,sigma)=||rho-sigma||_1/2. Choose d TOTAL orthonormal modes, each wholly positive or wholly negative
spectral, not arbitrary mixtures or a claimed compact-local detector. Restrict
the quasifree state to their finite CAR algebra and transform negative modes
to holes. Strong stationarity makes cross-sign C zero; consequently the
excitation state is again gauge-invariant quasifree with covariance

    D = C_positive,compressed direct-sum (I-C_negative,compressed)^T.

The transpose depends on the chosen hole basis and is essential with complex
entries. All eigenvalues lie in[0,delta]. Diagonalize by a finite unitary;
its second quantization leaves the vacuum fixed. The state is a product of
Bernoulli occupations, with vacuum weight p0=det(I-D). Vacuum is an eigenvector,
so its trace distance from the sea restriction is EXACTLY1-p0, not merely a
square-root fidelity estimate. Hence

    T(rho_d,sea_d)=1-det(I-D)<=1-(1-delta)^d<=d delta.      (4)

Every effect on this finite algebra has probability error at most that bound.
A k-outcome fixed measurement's total variation obeys the same bound; outcomes
are not counted as independent evidence. For fixed d this turns a uniformly
small ground-defect test into an operational approximation theorem.

## 4. Infinite volume and stationarity countercontrols

Small operator norm does not give small global state distance, finite total
excitation number or finite total energy. On the actual infinite-volume massive
Dirac spectrum, for epsilon>0 choose a finite positive band[m,M], M>m, and its conjugate negative
band. Set C=Q+t P_[m,M]-t P_[-M,-m], with0<t<=1 and2Mt^2<=epsilon.
Exact complement holds. For any positive f, n<=t, k<=Mn, so the neutral
violation2nk<=2Mt^2 even when f has other spectral components. Both band
projections have infinite rank. Selecting d band modes gives distance
1-(1-t)^d ->1, and total excitations/energy are infinite. Thus uniform witness
control is consistent with global distinguishability. Constant occupation at
ALL energies would fail the uniform epsilon premise and is not this control.

Stationarity is also indispensable. H=diag(1,-1), b=J conjugation,
J=[[0,-1],[1,0]], C=[[1/2,1/2],[1/2,1/2]] obeys exact complement but not[H,C]=0.
Its original gauge-invariant pure state is(|10>+|01>)/sqrt2. Relative to sea |01>
its vacuum probability is1/2 and distance1/sqrt2. Ignoring anomalous particle/hole
contractions would use D=I/2 and falsely predict p0=1/4. No such transfer is made.

Quasifreeness is also load-bearing. On energies(+m,-m), the mixture
(|00><00|+|11><11|)/2 is stationary, gauge invariant and has C=I/2 with
exact complement. All charge-neutral ground tests pass on its two one-dimensional
charge sectors, but C is not Q. Its joint particle/hole occupation is0, whereas
Wick would give1/4. Covariance premises alone cannot replace the state-class premise.

## 5. Reproduction and source ceiling

The finite probe constructs CAR/Fock matrices, computes neutral commutators,
checks exact complement and sharp asymmetric tolerance, and uses a complex
four-mode covariance to test the hole transpose and determinant. A nonstationary
counterexample and finite-volume growth sequence test the scope. Real planted
faults modify covariance, gap, the tested state at fixed covariance, or transpose. The continuum uniform
bound and infinite-rank conclusion rely on the proofs and stated free spectrum,
not finite sampling. A source-selected observed algebra containing these tests,
its state/dynamics and local implementability remain separate unresolved inputs.
