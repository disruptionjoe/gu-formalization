---
title: "K2062: All bounded local multipliers and compressed position effects"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: bounded finite-matrix multipliers of the fixed massive free graph; no universal nonlocal or physical-observable prohibition
scripts:
  - tests/channel-swings/k2062_bounded_local_multiplier_rigidity.py
  - tests/channel-swings/k2062_bounded_local_multiplier_rigidity_probe.py
---

# K2062: All bounded local multipliers and compressed position effects

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
result: complete bounded measurable multiplier commutant and strict unsharpness of compressed regions
carrier: complexified real1408 massive observed graph on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive metric and orthogonal free energy projector ON=declared_observed_graph
real_structure: complex matrix multipliers; real skew admissible subalgebra stated separately
grading: energy projection, not source chirality or fermionic parity
action_owner: repository-construction -- K2058 and K2060 fixed massive graph
target: local coefficient and position-effect compatibility MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Let V(x) be ANY essentially bounded measurable finite-matrix multiplier on R3. It commutes with the massive free positive-energy projector exactly when V is almost everywhere constant and that constant commutes with all three spatial Clifford matrices and the mass matrix. No periodicity, integrable decay, continuity or derivative hypothesis is needed. This closes the explicit bounded-nonperiodic gap left in K2060.

A released consequence is exact: every nontrivial spatial region gives a positive but nonprojective compressed position effect on the positive-energy subspace. There is still a normalized position POVM, and there are nonlocal sector-preserving coefficient repairs. Thus the result restricts sharp local multiplication, not every observation or interaction.

## 1. Object and previous scope

Use K2060's fixed positive-metric isometry and H0=C.D+mu beta on L2(R3,C1408), D=-i grad, mu>0, beta=-iM. The Hermitian C_j,beta square to I and mutually anticommute. Put Q=H0/sqrt(-Delta+mu^2), P=(I+Q)/2. Both Q and P are bounded translation-invariant Fourier multipliers. An essentially bounded V need not preserve the domain of H0; the assertion [P,V]=0 is entirely a bounded-operator assertion and has no such hidden domain assumption.

K2060 proved the result for periodic or constant-plus-L1 local coefficients by Fourier coefficient limits. Here convolution regularization and a strong high-frequency limit remove those assumptions. The earlier10624-dimensional real-skew survivor algebra is inherited, not recomputed or relabeled. This conditional graph is not source-selected by SC-OP-04/05, META53 or META56. Source positivity uncertainty, independent dual/parity/quotient and LT-SM8/GR6b debts remain unchanged.

## 2. Smooth bounded coefficients: exact modulation limits

First suppose V is smooth and all its derivatives are bounded. Let n be any unit vector, R>0, and conjugate Q by multiplication with exp(i R n.x): its symbol is

    Q_R(xi) = [C.(Rn+xi)+mu beta]/sqrt(|Rn+xi|^2+mu^2).

For any f in H1,

    Q_R f -> C.n f,
    R(Q_R-C.n)f -> L_n f,
    L_n=C.D-C.n(n.D)+mu beta.                         (1)

The first convergence is strong L2 by bounded symbols and dominated convergence. For the second, expand at each fixed xi and use the uniform estimate

    ||R(Q_R(xi)-C.n)|| <= c (|xi|+mu).

To justify it, for |xi|<=R/2 use the derivative bound for the normalized massive vector; for |xi|>R/2 use ||Q_R-C.n||<=2 and R<2|xi|. This supplies H1 domination, rather than a formal symbol expansion alone.

Commutation of Q and V implies [Q_R,V]=0 because scalar modulation commutes with V. Passing to the leading limit gives [C.n,V]=0 for every n, hence [C_j,V]=0. Apply the second limit to f and Vf for compact smooth f (Vf is in H1). Since the leading commutator is zero, obtain

    mu[beta,V]-i sum_j (C_j-C.n*n_j) partial_j V=0     (2)

as a multiplication identity. Derivatives of V commute with every C_j.

Take n=e1 in(2). With A=[beta,V] and D_j=partial_j V,

    mu A-i(C2 D2+C3 D3)=0.                            (3)

A anticommutes with C2 and C3 because V commutes with them and beta anticommutes. Conjugating(3) by C2 and adding(3) gives -2i C2 D2=0, so D2=0. Conjugating by C3 instead gives D3=0. Taking n=e2 and conjugating by C1 similarly gives D1=0. Finally mu>0 in(2) gives [beta,V]=0. Thus V is constant and commutes with all four generators. Conversely every such constant plainly commutes with Q and P.

This is a matrix argument in dimension three. It does not silently extend to one spatial dimension or to zero mass: the transverse terms and mu>0 were used explicitly.

## 3. Measurable bounded coefficients by convolution

Now let V be only L-infinity. Every translate V_y(x)=V(x-y) commutes with Q, because translations commute with Q. For a compactly supported smooth approximate identity phi_epsilon, V_epsilon=phi_epsilon*V is a bounded smooth matrix function with all derivatives bounded. Its multiplication operator is the weak operator integral of the translated multipliers, and therefore commutes with Q. Section2 makes each V_epsilon a constant matrix A_epsilon commuting with the four generators.

At a common Lebesgue point of the finitely many matrix entries, V_epsilon(x) tends to V(x); hence A_epsilon converges to one matrix A. Approximate-identity convergence then gives V=A almost everywhere. A retains the commutators by continuity. No Fourier transform of V as an integrable function, no uniform continuity, no boundary decay and no derivative of the original V has been assumed.

For the admitted real-skew W with [T,W]=0 and V=-iW, K2060's inherited Clifford/multiplicity decomposition gives exactly

    u(72) + u(72) + 4 u(8), real dimension10624.

Thus removing the spatial regularity/decay restriction creates no additional local surviving directions. For nonautonomous bounded coefficients, preservation by every two-sided propagator U(t,s) forces [P,V(t)]=0 for almost every t by the weak integral evolution equation. Applied time by time, the theorem makes the coefficient spatially constant almost everywhere; measurability in time is sufficient under local integrability of its L-infinity norm. Preservation only at an isolated final time is not covered.

## 4. Position compression: an observable survives, sharpness does not

Let E_A be multiplication by the indicator of a measurable spatial set A. On H_plus=Ran(P), define F_A=P E_A P restricted to H_plus. It is a positive contraction. For disjoint measurable sets, countable additivity holds strongly, and F_R3=I_Hplus, so this is a normalized positive-operator-valued measure (POVM).

Its exact projection defect is

    F_A-F_A^2 = P E_A (I-P) E_A P
              = [(I-P) E_A P]^* [(I-P) E_A P].        (4)

Consequently F_A is a projection iff (I-P)E_A P=0. Since E_A is self-adjoint this is equivalent to [P,E_A]=0. Section3 applied to the scalar multiplier then says 1_A is constant almost everywhere. For any A with both A and its complement of positive measure, F_A is therefore NOT a projection. No positive quantitative lower bound on this defect is asserted uniformly over all sets or states.

The same identity for bounded real 0<=f<=1 reads

    P f P-(P f P)^2 = P(f-f^2)P + P f(I-P)f P.

Both summands are positive. An explicit repair of a bounded Hermitian coefficient V is its block-diagonal compression

    V_diag=P V P+(I-P)V(I-P).

It is bounded Hermitian, commutes with P, and

    ||V-V_diag||=||(I-P)V P||.

The last equality is the norm of the off-diagonal self-adjoint two-block matrix. If V is scalar local and nonconstant, V_diag is generally nonlocal; in any case if V_diag were a bounded local multiplier, section3 would force it to be a constant Clifford commutant. This construction demonstrates a possible conditional sector-preserving repair, but it changes locality and does not establish finite propagation or a source-owned observable/action.

## 5. Released quantitative locality bound

The nonlocal repair is not unconstrained spatial spreading. With the Fourier convention for which -i grad has symbol p, the scalar kernel of (-Delta+mu^2)^(-1/2), away from r=0, is

    g_mu(r)=1/(8*pi^2) integral_0^infinity
                    t^(-2) exp(-mu^2*t-r^2/(4t)) dt.  (5)

This follows directly from the gamma integral for lambda^(-1/2) and the three-dimensional heat kernel (4*pi*t)^(-3/2) exp(-r^2/(4t)). For disjoint spatial supports the identity delta term of P vanishes and its kernel is

    P(x,y)=1/2[-i C.n g_mu'(r)+mu beta g_mu(r)],
    r=|x-y|, n=(x-y)/r.                               (6)

Splitting the exponent into two equal halves and using the arithmetic-geometric mean inequality gives

    mu^2*t+r^2/(4t) >= mu*r/2 + r^2/(8t).

The elementary substitutions u=r^2/(8t) give integrals8/r^2 and64/r^4 for t^(-2) and t^(-3), respectively. Differentiating(5), justified for r>0, therefore yields

    0<g_mu(r)<= exp(-mu*r/2)/(pi^2*r^2),
    |g_mu'(r)|<=4 exp(-mu*r/2)/(pi^2*r^3).            (7)

For the N=1408 carrier, trace of the cross Clifford term is zero. Hence the squared Frobenius norm of(6) is N/4 times [g_mu'(r)^2+mu^2*g_mu(r)^2]. If finite-measure regions A,B are separated by distance at least d>0, their cross-region operator obeys

    ||E_A P E_B||_HS^2 <= N |A| |B| exp(-mu*d)/(4*pi^4)
                              * [16/d^6+mu^2/d^4].   (8)

The ordinary operator norm is no larger than this Hilbert-Schmidt norm. This is a sufficient separated-region decay bound, not compact support, an optimal exponent, a uniform bound for touching sets, or relativistic signaling theory. It supplies a quantitative control for the nonlocal projected observation while preserving the sharp-localization obstruction. The full unprojected hyperbolic evolution keeps K2058's separate finite-propagation theorem.

## 6. Verification and hostile limits

The producer checks Clifford relations, the exact first-order symbol equations and conjugation eliminations in a four-dimensional real Clifford model, including an additional multiplicity factor. A separate probe constructs a complex Pauli representation and independently computes ranks of the full finite jet constraints. It also checks projection-defect and block-repair identities on exact noncommuting fixtures. Mathematical mutations remove the mass term, omit a spatial direction, corrupt the defect sign or its projector, and break off-block removal. The massless control deliberately gains extra constants; it is not passed off as the massive theorem.

The finite linear systems test the load-bearing matrix algebra, not measurable-function classification. The written H1 domination, weak-integral convolution and approximate-identity proof supply that extension. Similarly finite projection fixtures do not prove nonprojectivity for every region; section3 plus(4) does. No independent specialist, proof-assistant, external or novelty certification is claimed.

Strongest contrary routes retained: unbounded multipliers, differential operators, nonlocal coefficients, changing the reference projector, final-time-only echoes, massless or one-dimensional models, and the valid compressed POVM. They are distinct problems, not counterexamples hidden by the theorem. The local bounded class is now settled; further physical selection needs an explicit locality/observable/state requirement and a source-to-graph bridge, not another decay-class census.
