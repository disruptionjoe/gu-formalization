---
title: Printed differential solvability and the separate evolution obstruction
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T1
expected_delta: Resolve full mixed frozen compatibility and obtain a justified curved linear neighborhood conclusion
actual_delta: Exact scalarization gives frozen local solvability and curved analytic linear solutions at large finite coupling; an explicit real frozen sector excludes every finite-loss physical-time Sobolev estimate
class_covered: Selected low-Phi full-adjoint printed operator with nonzero scalar mass; constant coefficients for exact modes, analytic coherent tangent/spin LC with parallel Phi for curved linear solvability
premises:
- printed-equation-jets-and-symbol-2026-11-27.md owns the complex nonnull symbol and distinguishes W2
- source-prescription-current-2026-11-13.md sections1-2 binds independent g and T to draft sections5-7 and p45eq9.7
- ricci-flat-ambient-source-jets-2026-11-27.md owns the held source-guided coordinate metric
- tests/program-focus/source_action_deep_algebra.py retains primary-minus sharp and the two i-anticommutators
source_bridge:
  status: conditional
  reason: The endpoint template is source-bound but the low-Phi recipe, coherent completion and unrestricted state domain are not source-unique; nonlinear endpoint and physical quotient remain open
kill_condition: Exact system modes with unbounded rates exclude finite-loss evolution for the declared frozen states; failed symbol, real-adapter or domain transfer invalidates that conclusion, not GU
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-FROZEN-PRINTED-FINITE-LOSS-EVOLUTION
internal_target_verdict: excluded for unrestricted declared frozen states; curved nonlinear and physical domains remain open
canon_verdict_change: none
---

# Solutions exist; stable evolution is a different question

program_target: X-P1-P2
tier: T1
expected_delta: Resolve mixed linear compatibility and delimit evolution.
actual_delta: Full frozen scalarizer, curved analytic linear existence and exact frozen growing modes.

The singular symbol does **not** obstruct arbitrary smooth forcing in the
frozen linear printed equation. The coherent analytic curved **linear**
equation also has actual local solutions at every sufficiently large finite
coupling. Neither conclusion gives stable physical-time evolution: an exact
real sector of the frozen operator has rates growing with normal frequency.
Its solutions satisfy every frozen equation, including algebraic constraints.
These are different statements, not a nonlinear solution or a physical ghost verdict.

> **GU-COMPARATOR-ROUTING — scope before inference.** `INTERNAL_STRUCTURAL_ONLY`.
> Printed P, W2 Euler K, wedge GU*, frozen coefficients and the physical
> quotient are distinct. Follow [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> No conventional family, positive-Hilbert, Higgs or projection assumption is
> imported into the nonchiral2+1 source mechanism.

```gu-typed-objects
result: actual printed differential reduction and frozen evolution
carrier: full T*Y tensor End_C(S128); primary-minus real grade1/2 mode subcarrier LAYER=ambient BRIDGE=held-printed-Phi-coherent-LC-conditional CHIRALITY=N/A
pairing: no positive physical pairing assumed; auxiliary Sobolev norms test finite-loss estimates ON=adjoint_valued_forms
real_structure: primary-minus gamma sharp equals minus gamma; K95 q5 and flipped K77 q7 checked separately
grading: exterior Clifford degrees1/2 for the lift, not physical chirality
action_owner: source-print -- selected printed connection equation, not a completed source action
target: linear equation and declared evolution domain MAP-TYPE=intertwiner
```

## 1. Custody and exact object

Basis `95ae6dcbb4e4d630205bcb3f90a9d584940d0ef4`.
[Source prescription](source-prescription-current-2026-11-13.md) §§1–2 pins
draft §§5–7 and p45eq9.7: g and the full connection displacement T are
independent primitives. We retain the existing low-Phi comm/i-anticomm/
i-anticomm recipe and coherent source-guided metric-bundle completion. The
two i factors remain in the authenticated combined sign of the nested-star engine.

    kappa T + S_g + P_g T + Q(T,T) = 0.

We distinguish L_kappa=kappa Id+P_g from this nonlinear equation and its
full derivative L_kappa+V, V=2Q(T0,-). The latter is not automatically
covered. Coherent spin LC B and Phi are used; arbitrary independent varpi
or section-only physical domains are not substituted for them.

The [prior decomposition](printed-equation-jets-and-symbol-2026-11-27.md)
owns the nonnull symbol on complex dimension229376 and the one-direction
nilpotent inverse. Its finite jets did not prove neighborhood solvability.
Older selected1274 curvature-module Spencer and196-component I2B Hessian
tests have different carriers. W2 K and wedge GU* have different symbols.
None is imported here.

## 2. Full differential scalarization

Put q(xi)=g^-1(xi,xi) and

    A={1,12,22,30,36,40,42} union {-1,-2,...,-12},
    m(z,q)=z² product_(a in A)(z²-4a q)
          =sum_(j=0)^19 c_j z^(40-2j)q^j.

The owned nonnull decomposition has size-two zero chains and semisimple
nonzero squares4a q. Hence m(P(xi),q(xi))=0 for nonnull xi. Each entry is
polynomial, so density extends the identity to all real and complex
covectors, including null ones. This is an annihilator;40 is not asserted
to be the sharp null nilpotence order.

For constant nonzero kappa define

    b_r(z)=((-kappa)^r-z^r)/(kappa+z)
          =-sum_(l=0)^(r-1) (-kappa)^l z^(r-1-l),
    B_kappa=sum_j c_j b_(40-2j)(P) Box^j,
    d_kappa(Box)=kappa² product_a(kappa²-4a Box).

For constant coefficients, Box=g^ij partial_i partial_j and all factors
commute. Polynomial division gives

    L_kappa B_kappa=B_kappa L_kappa=d_kappa(Box) Id.       (1)

B has order at most39 and d has order38. Since d is a nonzero polynomial,
Malgrange–Ehrenpreis supplies a distributional fundamental solution E. For
compactly supported smooth f, T=B(E*f) is smooth and LT=f. A cutoff gives
local solvability for every smooth forcing. Analytic forcing has local
analytic solutions too: solve the scalar order38 equation by analytic CK
on a nonnull noncharacteristic hypersurface, then apply B. These are actual
neighborhood solutions at fixed nonzero kappa. No causal inverse or boundary
condition has been selected.

There is no nonzero constant-coefficient polynomial left compatibility
operator C: CL=0 implies Cd=0 by(1), hence C=0 over the polynomial domain.
There is no constant-coefficient polynomial differential inverse either:
the exact complex mass-shell kernel in §4 makes det L vanish, whereas a
polynomial matrix inverse would require a constant nonzero determinant.
A Green operator is not a polynomial differential inverse.

This uses established results: [Malgrange's existence paper](https://aif.centre-mersenne.org/articles/10.5802/aif.65/)
and the theorem/convolution argument in [Gantumur's authored notes](https://www.math.mcgill.ca/gantumur/math580f11/downloads/MalgrangeEhrenpreis.pdf).
No novelty claim is made.

## 3. Actual analytic curved linear solutions

Let the metric and induced bundle connection be analytic coherent LC.
Take P=Phi Alt nabla on E=T*Y tensor End(S), with the signed connection
rough Box. Canonical Clifford tensors are parallel for the tangent/spin LC
pair; metric and orientation compatibility make Hodge parallel. Therefore
the selected Phi is parallel. This is a property of this completion, not
of every independent source connection. Simultaneous gauge dressing of B
and Phi preserves it.

Keep all Box powers on the **right**, and define

    M=sum_j c_j P^(40-2j) Box^j.

Without commuting P through Box, polynomial telescoping gives exactly

    L_kappa B_kappa=d_kappa(Box)-M.                      (2)

M is independent of kappa and has order at most38. Its degree40 principal
symbol vanishes by m. At any point choose geodesic normal coordinates and
a synchronous induced bundle frame. First derivatives of the principal
coefficients of P and Box vanish; the zeroth coefficient of P and the
first-order coefficient of Box vanish there. These exhaust contributions
of order39 in the compositions. Derivatives of lower connection coefficients
need not vanish: they supply curvature at order38 and below. This proves
the order bound at every point. Torsion or nonparallel Phi would invalidate
this proof.

Write c19=product_a(-4a)≠0. At any fixed nonnull real conormal tau, the
order38 normal coefficient of A_kappa=L_kappa B_kappa is

    kappa² c19 q(tau)^19 Id - sigma38(M)(tau).             (3)

The second term is a fixed finite matrix. The sufficient bound
|kappa|² |c19 q(tau)^19|>||sigma38(M)(tau)|| makes(3) invertible at the point
and on a smaller neighborhood. Analytic CK for this square order38 system
then gives local analytic u with A_kappa u=f. Thus T=B_kappa u solves the
**actual variable-coefficient linear equation** LT=f, for each sufficiently
large finite |kappa| and analytic f, including f=-S_g when analytic.

Here d_kappa(Box) is a scalar polynomial in a **bundle** rough operator,
not a componentwise scalar operator on curved E. CK applies to A_kappa,
not directly to singular L. The theorem holds on the stated complex carrier;
a real solution assertion additionally needs the operators and forcing to
preserve the authenticated real form. A real coefficient fixture does not
prove that full adapter. No common neighborhood in kappa, convergent h-series,
smallness of T, global solution, uniqueness of T or prescribed physical
Cauchy data follows. In particular, auxiliary u data do not prescribe T data.

[Analytic CK and noncharacteristic systems](https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf),
§§4–5, provide the analytic theorem used here.

### The nonlinear boundary

Substituting T=B u makes Q(Bu,Bu) generically depend on derivatives of u
through order39, above the order38 left side. A generic zeroth-order V also
makes VB order39. A small coefficient does not remove this order difference.
Thus the proof covers neither the nonlinear endpoint nor its full
linearization. A cancellation, compatible reduction or new estimate is still
needed. This discharges unperturbed curved linear compatibility, not a
complete black-hole lift.

## 4. Exact system modes with unbounded growth

For a complex nonnull covector zeta, set Q0=q(zeta), Gamma=c(zeta) with
raised Clifford index, and

    O_zeta=Phi1-zeta tensor Gamma/Q0,
    V_zeta=Gamma O_zeta.

Covariance of the owned trace seam gives

    P(zeta)O_zeta=-2V_zeta,
    P(zeta)V_zeta=24Q0 O_zeta.                           (4)

At Q0=-kappa²/48 the nonzero v_zeta=kappa O_zeta+2V_zeta obeys
(kappa+P(zeta))v_zeta=0. This is an actual full-system polarization, not
an arbitrary solution of the scalar necessary condition.

Choose unit base physical-time conormal tau and orthogonal normal conormal
eta of the same sign s. K95 has negative base time and negative normal
choices; flipped K77 has positive base time and positive normal choices.
Put

    zeta=lambda tau+i n eta,
    lambda²=n²-s kappa²/48.

For sufficiently large n, lambda>0 and lambda/n tends to1. Therefore
exp(lambda t+i n y)v_zeta solves every equation of the exact frozen massive
system, including its algebraic constraints.

Under primary-minus gamma_a^sharp=-gamma_a, Clifford grades1 and2 are
sharp-skew. O has grade1. The scalar part of Gamma Phi1 is zeta and cancels
the subtraction in V, leaving grade2. Complex coefficients encode Fourier
phases; conjugate Fourier pairs give real coefficient quadratures in u(H).
This authenticates this particular sector, not all complex spectral counts
as real physical counts. Both odd-index ports are checked separately.

For L2/Sobolev states on R13, take smooth Fourier packets supported in
fixed-width balls near n eta and their conjugates. The same mass shell
defines smooth lambda(xi)≥c n there; (4) gives a smoothly normalized nonzero
system amplitude. Inverse transforms are Schwartz at every fixed time and
solve LT=0. At fixed t>0 amplification is at least exp(c n t), whereas any
fixed finite spatial derivative loss or finite collection of initial time
derivatives costs only a polynomial in n. Consequently no estimate

    ||T(t)||_(H^s) <= C sum_(j<=J) ||partial_t^j T(0)||_(H^(s+r_j))

holds on all these solutions with finite J,r_j and frequency-independent C.
Periodic modes are an equivalent norm device, not an imposed GU topology.

## 5. Calibration and transfer limits

An ordinary one-time Dirac Fourier generator -i(n alpha+m beta), with
Hermitian anticommuting alpha,beta, is anti-Hermitian and squares to
-(n²+m²)Id. The exact control preserves its positive norm. The diagnostic
does not label every first-order equation unstable. For the printed trace
sector on a one-time Lorentz comparator, opposite-sign spatial eta gives
lambda²=kappa²/48-n²: bounded low-frequency growth can occur, but the
unbounded high-frequency rates above disappear. No low-mode stability claim
is hidden in that comparison.

[Craig–Weinstein](https://arxiv.org/abs/0812.0210) proves that nonlocal
restrictions can restore Sobolev well-posedness for an ultrahyperbolic scalar
problem. This is a possible mechanism to test, not a supplied GU state rule
or a proved restriction for the coupled nonlinear system. Its coauthor
Steven Weinstein is distinct from Eric Weinstein.

The exact growth proof covers kappa Id+P(partial) only. Freezing actual
connection terms or nonlinear linearization generally adds nonscalar C0;
that operator is not covered automatically. No variable-coefficient growth,
physical admission, negative Hamiltonian, ghost or mass-gap conclusion follows.
The first-order det P is identically zero. The native null cone belongs to
the mass-dependent scalar elimination, not an ordinary full-carrier
first-order hyperbolicity assertion.

## 6. Verification and consequence

[Exact probe](../../tests/program-focus/printed_differential_solvability_probe.py):
83 checks cover polynomial coefficients/telescopes, mixed covector nested-star
identities, exact real-sector massive residuals in both ports, Dirac and
one-time dispersion controls, and moving nilpotency. The last control shows
that N(x)²=0 does not justify the frozen nilpotent inverse truncation when
NN'≠0. In this fixture D=N partial is instead idempotent, so a different
finite inverse exists for kappa≠0,-1. That survivor is checked explicitly;
the control does not exclude all finite differential inverses.

[Lean cores](../../Lean/GUFormalization/PrintedDifferential.lean) cover the
abstract two-channel lift, quadratic quotient, determinant arithmetic and a
scalar perturbation margin. Native geometry, polynomial extension,
fundamental solutions, CK and Sobolev estimates remain written proofs.

| State | Result |
|---|---|
| ESTABLISHED | Frozen local solvability; curved analytic linear solvability at large finite coupling under parallel-Phi LC hypotheses; exact real frozen modes with unbounded rates. |
| RULED OUT | Constant-coefficient polynomial differential inverse and unrestricted finite-loss Sobolev evolution for the declared frozen system. |
| NOT MODELED / UNDETERMINED | Nonlinear curved endpoint, generic C0/V perturbations, selected physical domain, kappa1 and full source/GU* viability. |

The weakest physical link is source state admission and the selected
completion: neither is source-necessary. Class-C representativeness remains
unestablished. No source, canon or physical-ledger verdict changes; no new
action, connection or state rule. Choicebudget10/4/net6/0 selected predictions
is unchanged. The remaining discriminator is nonlinear constraint/domain
compatibility, not further finite-jet matching or unperturbed linear forcing.
