---
title: "K2298 Enlarged native companion: odd obstruction and even completion"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
claim_ceiling: selected flat T0 quadratic germ only; no physical source or global-domain conclusion
scripts:
  - tests/channel-swings/k2298_enlarged_native_companion_probe.py
---

# K2298 Enlarged native companion: odd obstruction and even completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This uses the selected K77 I1B trace/Hodge quadratic operator. Its metric source is constructed algebraically, not supplied by physical matter or an observed action. No Einstein action is silently substituted. See [source-native routing](../../lab/methods/source-native-comparator-routing.md).

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: K2298 Enlarged native companion
carrier: real K77 Clifford-valued ambient one-form distortions and horizontal symmetric metric variations LAYER=ambient CHIRALITY=N/A
pairing: scalar Clifford trace and fourteen-dimensional Hodge wedge ON=declared_carrier
real_structure: selected real Cl(7,7) coefficients
grading: all Clifford grades; symmetric metric rank2 is not Clifford grade2
action_owner: source-action -- I1B grammar with repository-selected Shiab and flat T0 germ
target: full coupled linear metric and distortion Euler covectors MAP-TYPE=evaluation
```

## Result and exact object

Extra odd distortion grades do not repair [K2297](k2297-symmetric-shiab-companion-2026-10-30.md)'s horizontal symmetric lift. A small exact receiver projection preserves its full curl constraint and annihilates every possible grade5 correction, including normal derivatives. However, the full ambient distortion carrier admits a repair with a necessary even-grade correction: an explicit polynomial metric/distortion pair solves the complete unsourced companion equation with a nonzero conserved metric-row source. Thus the restricted-lift obstruction cannot be extended to the complete selected quadratic system.

Use eta=(+---,++++++,----), flat T=0, selected Shiab(comm,symi,symi), and K129's Hessian [[0,A*],[A,C]], C=kappa K+E(D). K is the Hodge flat map; the first-order Euler coefficient is skew, E_t(v,u)=(<v,S(dx^t wedge u)>-<u,S(dx^t wedge v)>)/2. K2297 proves A h=-2*j14(G'14 h). These are fixed definitions, not a uniquely source-selected Shiab. SC-ACT-01/02 ASSERTS their action/equation and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. Their polarities and ledger0.263 remain unchanged; no full GU conclusion follows.

## 1. Why the odd-grade repair fails

K132's complete grade graph has the component 1--2--5--6--9--10--13--14. The grade2 Euler output can receive first-order input only from grades1 and5; grade3 is in the other component. A grade2 algebraic kappa K term is absent if T has only odd grades.

For a basis input dx^mu gamma_J let its Clifford/form XOR label be J xor{mu}. Each derivative coefficient in direction t changes this label to J xor{mu} xor{t}. This follows term by term from the selected Shiab's wedge, Hodge and Clifford contractions, as recorded in [K132](selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md). In the first Shiab term, the frame index wedged into *(dx^t wedge dx^mu) is t or mu, leaving the other as receiver index. In the second term phi2 must occupy {t,mu}, while the outer phi1 index equals the missing receiver index and cancels from the label. Clifford mask multiplication is XOR, proving the stated support rule. Clifford trace pairs equal masks; the transpose obeys the same rule. It is a coefficient identity, not a rank inference at a chosen covector.

K2297's symmetric lift j(u), with u depending on four horizontal coordinates, has 64 nonzero grade2 first-jet receiver rows: 52 repeated-index receivers dx^i gamma_ab with i in {a,b}, and 12 distinct-index receivers from the four horizontal triples a<b<c. Repeated-index receiver labels have cardinality1. A grade5 input label has cardinality4 or6 and after one derivative cardinality3,5 or7. It cannot reach these 52 rows.

For a horizontal triple a<b<c write r=(r_a,r_b,r_c) for receivers (a,bc),(b,ac),(c,ab). Every grade5 first-jet input reaching these rows is along

    r=lambda(eta_a,-eta_b,eta_c).                            (1)

There are exactly 4*11*10=440 candidate columns: derivative t outside the triple, input form index mu outside the triple and t, and Clifford blade J={a,b,c,t,mu}. The probe evaluates all three actual forward-minus-transpose pairings for every column. All other input columns vanish by the label rule. This includes all14 derivative directions, not just horizontal ones.

Therefore the two rows

    eta_b r_a+eta_a r_b,  eta_c r_a-eta_a r_c                 (2)

annihilate every grade5 contribution. Combine them with the 52 repeated rows. The resulting60-row projection P on K2297's40 symmetric first jets has rank20, equal to the full grade2 first-jet map. Since P is a row projection, its kernel is exactly that of the full map. The repeated rows alone have rank12 and would not prove this result.

For T=j(u)+T3+T5+... with no even grades and no additional grade1 component, an unsourced grade2 companion consequently forces curl(u)=0. On the contractible smooth flat horizontal patch of K2297, u is a scalar Hessian and A*j(u)=0. Higher Clifford grades pair orthogonally to A, so the metric source is zero. The argument covers arbitrary first jets and null directions; it uses no division by k². It does not cover a more general grade1 lift, even-grade distortion, curved coefficients, distributional sources or a global domain.

## 2. Even grades give an exact full-companion escape

Assume kappa!=0 and set L0=K^-1 E(D). It is a constant-coefficient first-order operator and lowers polynomial degree. For any polynomial V, (kappa+L0)^-1 V is a finite Neumann sum. In particular, choose

    h11=(x0)^4/24, other horizontal metric components zero,
    V=K^-1 A h=(x0)²/2 V0,
    V0=sum_{i=2}^{13} dx^i gamma_i.

Then

    T=-V/kappa+L0 V/kappa²-L0² V/kappa³                    (3)

satisfies A h+C T=0 exactly, because L0³V=0. This construction enlarges the grade1 support to include ten vertical diagonal components as well as allowing even grades. It does not show that even grades alone repair the original horizontal grade1 ansatz. The first correction is grade2 and linear in x0; the last is constant with grades1 and/or5. Every ambient receiver is retained. This is not a perturbative inverse or an infinite convergence claim. For general polynomial degree d, the finite inverse terminates after at most d+1 derivatives. It gives a polynomial companion solution for every polynomial Ah when kappa!=0; it says nothing about bounded inverses on a function space.

The metric source is

    J_g=A*T=kappa^-1 diag(0,-12,-11,-11).                   (4)

Only -V/kappa contributes, since A* has two derivatives and the other terms have degree at most1. Direct native pairings <V0,A(e_ii)> are (0,12,11,11). Ten vertical diagonal curvature receivers contribute to these values; dropping them would incorrectly give2 and1. The source is constant and divergence-free, but it is constructed, not identified with a physical stress tensor. In particular its time component is zero and negative spatial components cannot be called ordinary positive matter without another construction.

The probe constructs L0 sparsely: for input dx^mu gamma_J, direction t, and candidate output form index nu, the sole possible Clifford mask is J xor{mu} xor{t} xor{nu}. Its coefficient is the exact Euler pairing divided by <dx^nu gamma_M,*dx^nu gamma_M>. Exhausting14 nu values retains the entire output for that input. The actual polynomial residual is zero; deleting the even correction is not a solution.

## 3. What changed and what remains

The odd-only enlarged class is obstructed, while the full-grade polynomial class has an explicit escape with kappa!=0. These are different hypotheses and neither erases K2297. The useful next question is a physically selected joint source/readout and closed-domain realization of this full operator, or a controlled nonpolynomial/curved extension. A polynomial particular solution may grow without bound and need not satisfy decay, finite energy, a chosen boundary condition or physical causality. No global Green operator, nonlinear solution, matter/light ratio or GU acceptance is established.

## Verification

Exact rational firstjet projection, all440 possible grade5 columns, sparse full-grade polynomial residual and native ambient curvature pairings are checked. Universal extension uses the label support identity and finite polynomial-degree argument. Countercontrols include missing even correction, wrong Neumann sign, missing vertical terms and inadequate receiver projection; errors in the operator are distinguished from report hashes. Internal specialist review is not Lean, external-expert or novelty certification.
