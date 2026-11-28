---
title: All local CW thresholds survive the quadratic boundary estimate
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: X-P1-P2
tier: T2
expected_delta: Resolve the negative-factor collinear gap in the actual future-boundary estimate and close covered
  local threshold tests
actual_delta: The full transverse quadratic pushforward has bounded density, extending the local L2 bilinear estimate
  and epsilon^1/4 threshold tail to all nineteen output factors and all signed common-CW massive input branches.
  One calibrated actual A1/H9 vertex has zero output-minus2 projection.
class_covered: Selected frozen low-Phi printed K95 descriptor; compatible complex massive inputs on compact common-CW
  patches, bounded regular-coordinate quadratic vertex, single separated output threshold
premises:
- Full symbol, scalarizer and regular threshold coordinates from cw-fullsystem-domain and cw-one-sided-boundary
- "Spatial signature(9,4), nonzero real kappa; each common-CW input has positive square above kappa\xB2/4"
- Auxiliary coefficient L2 norm and local bounded polarization frames; no source physical norm or nonlinear invariant
  domain
source_bridge:
  status: conditional
  reason: SC-ACT-02 endpoint template and SC-META-52 ultrahyperbolic debt do not select this low-Phi realization
    or future state law.
kill_condition: Failure of native channel binding or uniform compact pushforward density withdraws the affected
  claim; rank loss or a lower-dimensional toy is not a counterexample. No physical/source kill follows.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: T2 quadratic survivor evidence on X-P1-P2; no cell or ledger verdict change
---

# The missing transverse integration repairs the estimate

program_target: X-P1-P2
tier: T2
expected_delta: Decide the uncovered collinear negative-factor boundary estimate using the actual full-system channels.
actual_delta: All19 local output thresholds satisfy the same ordinary-L2 quadratic boundary estimate; one calibrated actual fixture has a zero resonant projection.

**ESTABLISHED:** the future boundary combination satisfies `L2 x L2 -> L2` locally through every one of the19 output thresholds, for every pair among38 signed massive common-CW input branches. The threshold-tail operator norm is `O(epsilon^(1/4))`. The proof keeps all13 spatial variables and works at the formerly problematic collinear points. It requires only a bounded actual regular-coordinate numerator, so no polarization census is necessary.

**RULED OUT:** a normalized L2 countersequence to this local estimate on the declared compact patches. This is the consequence of a positive bound, not a physical exclusion. One exact input-polarization fixture has a zero output-channel projection; no general cancellation theorem is asserted.

**NOT MODELED / UNDETERMINED:** global high-frequency estimates, input band-edge limits, interactions involving independently retained decaying states, a complete nonlinear invariant domain, source state/quotient/current, physical positivity and curved/K77 transfer.

Outcome: **SURVIVES** all local oscillatory-input quadratic threshold-boundary tests just specified; **INCOMPLETE** as a physical GU* selection law. The earlier two-sided tempered-history obstruction remains separately scoped LC context and is not re-derived or promoted into a B verdict here.

```gu-typed-objects
result: full-transverse actual CW boundary estimate
carrier: T*Y tensor End_C(S128), full complex compatible massive modes LAYER=ambient BRIDGE=selected-printed-dictionary CHIRALITY=N/A
pairing: ordinary coefficient L2 on compact modal patches, auxiliary and not physical energy ON=declared_complex_modal_carrier
real_structure: K95; exact primary-minus A1/H9 real quadrature controls, no general K77 transfer
grading: Clifford spectral channels; not physical weak chirality or family counting
action_owner: source-print -- selected low-Phi endpoint realization, not W2 or wedge Euler dynamics
target: future boundary combination with independent decaying state MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md), and Geometer T02/T09/T11/T13/T15. The auxiliary norm and a spectral channel do not identify physical energy, an observed gauge state or the source observation contraction.

## 1. Custody, selection and outcome logic

Basis `523eaeb084769e3c5f8aa6bc43c5a33b9c888096`. Ordinary B counter124; quick-win step2b wave3/5. Reuse [full-system symbol/domain](cw-fullsystem-domain-2026-11-27.md), [regular future relation](cw-one-sided-boundary-2026-11-27.md) and [prior positive-threshold estimate](cw-bilinear-boundary-estimate-2026-11-27.md). The uncovered inputs have factors(-1,+1), distinct from the earlier trace shell a=-12. The previous handoff correction is preserved.

SC-ACT-02 (draft p45 eq9.8) supplies the endpoint template; SC-META-52 (TOE01:17:10) acknowledges ultrahyperbolic/boundary debt. Neither uniquely selects this dictionary or future law. Mathematical breadth and source necessity remain separate. The strongest alternative is a physical-norm/PT test, which needs a declared physical domain; closing the existing local quadratic gate has lower cost and clearer decision value.

Advance outcomes: zero actual projection retains that fixture as a null control; nonzero would require a full-dimensional estimate, not a rank-loss verdict. Reconnaissance found an estimate valid for every bounded numerator, so extending it directly decides more than a larger vertex census. No new action, state prescription, norm or choice family is adopted.

The relevant primary general method is [nonlinear Brascamp–Lieb](https://arxiv.org/abs/1811.11052v2), already considered in the earlier estimate. Its public status was rechecked November28. Here the critical-center rank loss is handled by an elementary exact pushforward and Cauchy–Schwarz proof; no applicability claim for that general theorem is required and no novelty claim is made.

## 2. Held point and notation

The13 spatial variables have K95 signature(9,4), with quadratic form r². At kappa12, the output factor c=-2 has threshold

`K²=18`, `delta=18-r(K)²`.

The inputs are

`k=(5/2)K`, `l=-(3/2)K`,
`a=-1`, `b=+1`, opposite temporal signs,

with

`k²=225/2>36`, `l²=81/2>36`,
`omega_a(k)²=omega_b(l)²=153/2`.

Both input patches can be chosen compactly inside the common CW domain. The phase is `nu=omega_a(k)-omega_b(l)`. The ordinary two-active-coordinate Jacobian vanishes at this point because k,l,K are collinear. The full pair phase map still has rank2. Neither fact alone is the estimate.

We test the actual future boundary kernel

`B(f,g)(K)=integral n(k,K,sqrt(delta)) f(k)g(K-k)`
`                            /(sqrt(delta)-i nu(k,K-k)) dk`

on `0<delta<D`, with bounded actual smooth matrix numerator n on the held compact patches. Nonzero n is not required for an upper bound. The regular descriptor frame is essential; no singular growing/decaying eigenprojector is inserted.

## 3. Exact invariant coordinates for fixed k

The argument works for arbitrary input factors a,b and signs s_a,s_b. Fix k and put

`A=r(k)²>0`, `l=alpha k+y`, `y perpendicular k`, `q=r(y)²`.

Because the spatial signature is(9,4), the transverse form on k-perp has signature(8,4) and dimension12. Write

`omega_a(k)=sqrt(A+kappa²/(4a))`,
`W=omega_b(l)=sqrt(A alpha²+q+kappa²/(4b))>0`.

For any output factor c define `C_c=-kappa²/(4c)`. Then

`delta=C_c-A(1+alpha)²-q`,
`nu=s_a omega_a(k)+s_b W`.

The exact Jacobian is

`det partial(delta,nu)/partial(alpha,q) = -s_b A/W`.  (1)

At the held signs s_b=-1 this is A/W, not zero. The original derivative loses rank because dq vanishes at y0, not because the invariant-coordinate map fails.

There is also an explicit inverse on the selected W>0 branch:

`W=s_b(nu-s_a omega_a(k))`,
`B_l=W²-kappa²/(4b)`,
`alpha=(C_c-delta-A-B_l)/(2A)`,
`q=B_l-A alpha²`.

Thus no multiplicity or local injectivity assumption is hidden in (1). In a metric-orthonormal frame whose first vector is k/sqrt(A), Lebesgue measure is

`dl=sqrt(A) d alpha dy`.

The frame has absolute determinant1 in the original spatial coordinates. After the (alpha,q) change, the density factor is therefore `W/sqrt(A)`.

## 4. The critical transverse pushforward is bounded

Choose local metric-orthonormal frames depending smoothly on k. On a compact k patch, the original compact l patch is contained in a uniformly bounded box in `(alpha,y)` coordinates. This is ordinary finite-dimensional compactness; no global frame on the entire CW domain is required.

Split two positive transverse coordinates from the other ten:

`y=(u,z)`, `u in R²`, `z in R10`,
`q=|u|²+Q10(z)`.

For every nonnegative measurable phi and fixed z, polar coordinates give

`integral_(R²) phi(|u|²+Q10(z)) du`
`   =pi integral_(Q10(z))^infinity phi(s) ds`
`   <=pi integral_R phi(s) ds`.

If the remaining ten coordinates lie in `[-R,R]^10`, then

`integral_(held y box) phi(Q12(y)) dy`
`   <=pi(2R)^10 integral_R phi(s) ds`.  (2)

Thus the compact12-dimensional indefinite quadratic form has a uniformly bounded pushforward density, including q0. This retains all transverse variables; it does not freeze them, replace them by delta functions, or assume Q12 is positive definite. Two positive directions suffice for the polar integration, and the remaining ten are genuinely integrated over a bounded set.

On compact common-CW input patches, A is bounded below by a positive number and W is bounded above and away from zero. Keep those actual branch/patch cutoffs when applying (2), before extending integration domains. Combining (1)-(2), for every nonnegative measurable function Psi of delta,nu,

`sup_(k in input patch) integral_(l in input patch)`
`                Psi(delta(k+l),nu(k,l)) dl`
` <= C_push integral_(R²) Psi(d,s) dd ds`,  (3)

where one possible bound is

`C_push=pi(2R)^10 sup_(patches) W/sqrt(A)`.

The precise harmless box constant is unimportant; its uniform finiteness is the point.

## 5. Full26-dimensional Cauchy–Schwarz

Set

`w(d,s)=1_(0<d<D, |s|<L)/sqrt(d+s²)`.

As before,

`||w||_2² <= 2pi sqrt(D)`.  (4)

For an output test function h, take absolute values and bound the numerator by N. Apply Cauchy–Schwarz on the full pair space `(k,l) in R26` to

`|f(k)| w(delta(k+l),nu(k,l))`

and

`|g(l)| |h(k+l)|`.

By (3), the first squared factor is at most

`C_push ||f||_2² ||w||_2²`.

The second is at most `||g||_2² ||h||_2²`, by the determinant-one change `(k,l)->(k+l,l)`. Hence

`||1_(0<delta<D) B(f,g)||_2`
` <= N sqrt(C_push) sqrt(2pi) D^(1/4) ||f||_2 ||g||_2`.  (5)

The estimate is absolute; it requires no Cauchy principal value, Hilbert-transform cancellation, smoothness of f,g, or nonzero actual interaction. It applies to bounded finite-dimensional matrix numerators using coefficient Hilbert norms. The corresponding positive absolute integral defines an L2 output almost everywhere. Threshold truncations converge in bilinear operator norm, with an O(epsilon^(1/4)) tail.

Therefore no normalized L2 countersequence on these fixed sufficiently small patches can blow up this future boundary output. A proposed one-dimensional logarithm must lose input normalization or transverse integration; (5) controls arbitrary anisotropic concentrations and correlations in all13 coordinates.

## 6. Generalization: all local massive threshold pairs

Nothing in (1)-(5) uses the sign of c or the collinearity at the selected point. It uses only:

- common-CW input k²>kappa²/4>0;
- nonzero smooth input frequencies on compact patches;
- the12-dimensional transverse signature(8,4);
- bounded actual regular-coordinate numerator;
- a single separated output threshold with its denominator `sqrt(delta_c)-i nu`.

These conditions hold locally for every one of the19 distinct output factors and every pair among the38 signed massive input branches in the common CW domain, whenever that pair reaches the considered output neighborhood. Compatible input polarization bundles can be trivialized locally; all actual Q coefficients are then bounded. The argument does not require a polarization or vertex census.

The output regular Jordan2/scalarizer construction is inherited: the other factor roots are separated at each fixed nonzero-kappa threshold. Different output thresholds can be treated in separate neighborhoods. A zero vertex is a null control; a nonzero vertex remains useful calibration but cannot defeat this local upper bound.

This is a stronger local coverage statement than the old two-coordinate-minor proof. It does **not** yield one global constant on the unbounded common-CW domain, including approaches to its input boundary, nor global high-frequency control, all-output nonlinear closure, or interactions with independently retained decaying states.


## 7. Actual full-symbol fixture and calibrated zero

At κ12 choose `K=3(theta1+theta2)`, `omega=3sqrt(34)/2`,

`xi1=omega tau+(15/2)(theta1+theta2)`,
`xi2=-omega tau-(9/2)(theta1+theta2)`.

The symbol covectors ζj=iξj have squares(-36,+36), respectively, so the input factors are(-1,+1). Both spatial squares225/2 and81/2 exceed36. Let `M=gamma6...gamma13` and use transverse seeds

`Aseed=theta3 gamma5-theta5 gamma3` (A1=im E),
`Hseed=theta3 gamma3 M-theta4 gamma4 M` (odd H9 hook).

The hook's exterior and contraction traces vanish exactly. Direct native Phi checks give `Pζ² seed=144 seed`; therefore `vj=(12-Pζj)seedj` are nonzero actual kernels of `12+Pζj`. The compact-symbol adapter agrees with native Phi, and both real quadratures satisfy the held primary-minus real form. No trace-shell substitution is made.

At output ζ0=iK, Γ=c(ζ0), q0=-18. The only factor−2 block is the odd p11 B11=im J block, with `CJ=3`. Split transverse grade11/12 coefficients as `beta+Gamma beta'` and set `b=C beta`, `c=C beta'`. The owned exact block is

`P(beta,beta')=(4q0 beta',-2beta)`.

Thus every grade10 coefficient of `b+6c` is a left-null receiver of `12+P`. The probe constructs the transverse Clifford projectors explicitly and calibrates them on a nonzero Jw:

`receiver(Jw)=3w`, `receiver(Gamma Jw)=18w`,
`P Jw=-2Gamma Jw`, `P Gamma Jw=4q0 Jw`.

The actual mixed force `F=Phi(v1 wedge v2+v2 wedge v1)` has24 nonzero terms, but its complete B11 receiver vector iszero for this fixture. The receiver also annihilates `(12+P)F`, as required. This tests the static B11 left/shell projection, not the entire temporal-cluster forcing or vanishing on a neighboring packet. It is an authenticated polarization-level null, not an all-A1/H9 or all-channel selection rule. Its locality and normalization are useful controls; the all-threshold upper bound is independent of whether other fixtures are nonzero.

## 8. Forward response and what this does not solve

The inherited regular companion equations are `q'=p-g0`, `p'=delta q-g1`. For q(0)=0 the actual harmonic response uses

`K_t(lambda,nu)=(exp(i nu t)-exp(-lambda t))/(lambda²+nu²)`,
`q(t)=(g1+i nu g0)K_t`,
`b(t)=(g1+lambda g0)exp(i nu t)/(lambda-i nu)`, `p=b-lambda q`.

The new pushforward estimate accepts any square-integrable function of(delta,nu), so the previously verified scalar identities apply at all local thresholds:

`||K_t||²_(L2(delta>0,nu))=2pi t`,
`||nu K_t||²`, `||lambda K_t||² <=4pi sqrt(D)` on a finite collar.

Consequently every such local quadratic response has `||q(t)||_2<=C(1+sqrt(t))||f||_2||g||_2`, while p has a uniform upper bound for t>=0. This is an upper estimate, not observed growth or nonlinear stability. The free decaying state is still retained; interactions in which that state itself is an input are not covered by an oscillatory-input proof. Complementary descriptor components stay separate and require avoiding their poles on the held phase patch.

Local compact constants do not establish a uniform bound on the unbounded common-CW domain or as input frequencies approach zero at band edges. Local polarization frames are bounded, but that alone does not give a global physical state norm. Nor does a quadratic boundary estimate construct a nonlinear invariant manifold. These remain exact remaining burdens, not hidden assumptions in a claimed complete theory.

## 9. Validation and continuation

The probe carries68 exact checks: authenticated prior dependencies, all four signed Jacobians/inverses, spatial/transverse signatures, polar-density normalization, kernel integrals and threshold arithmetic, plus22 actual native channel/receiver controls. A one-positive-direction countercontrol has unbounded quadratic pushforward density, distinguishing the actual two-positive-direction integration from a dimension-free assertion. Written uniformity, measure domination, duality and density-extension arguments are independently reviewed. No new Lean or full PDE formalization is claimed for this T2 estimate.

The inline20-lens check emphasized PDE/harmonic analysis, microlocal geometry, differential geometry, indefinite geometry, representation/Clifford blocks, operator domains, measure theory, topology, dynamical systems, control, symplectic structure, algebraic rank strata, numerical exactness, proof engineering, QFT and probability, with category-theoretic map typing and number-theoretic exact shell labels. It was a quick reasoning pass, not20 independent reviewers or a vote. Its useful change was to integrate the transverse variables before declaring the rank-loss point dangerous.

No further stable-oscillatory pair census can refute the proved local bound under the same premises. The next useful gate is the retained-decaying-state interaction needed by the future-only repair, followed by global/high-frequency and nonlinear closure according to decision value. The concrete two-decay triple-threshold option and alternatives are recorded in the accompanying evidence; no denominator-only failure is asserted.

Historical candidate choice budget10/4/net6/0 source-selected predictions remains attributed and unchanged. No matrix-cell, physics-ledger, source, canon, class-C or scheduler verdict changes. B evidence advances the mathematical survivor; source physical selection remains open.

[Probe](../../tests/program-focus/cw_all_threshold_boundary_probe.py) · [Certificate](../../lab/process/cw-all-threshold-boundary-certificates.json) · [Review evidence](../../lab/process/cw-all-threshold-boundary.json).
