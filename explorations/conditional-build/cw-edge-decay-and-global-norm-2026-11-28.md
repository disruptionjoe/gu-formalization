---
title: 'CW completion: local decay and band-edge bounds, global coefficient regularity cost'
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: X-P1-P2
tier: T1
expected_delta: Settle retained-state local closure and the global ordinary coefficient-norm question without changing the state prescription
actual_delta: All three local quadratic input types are bounded through band edges in inherited modal/free-decay norms; same-order global coefficient evolution is excluded, while finite derivative loss at most39 survives
class_covered: Selected frozen low-Phi printed K95 full bosonic descriptor at kappa12, compatible common-CW Fourier core, ordinary coefficient Sobolev norms; compact-patch retained decaying states separately
premises:
- cw-fullsystem-domain-2026-11-27.md supplies actual P, the degree40 scalarizer, compatible modes and H_modal
- cw-one-sided-boundary-2026-11-27.md supplies regular threshold coordinates and independent decaying data
- cw-all-threshold-boundary-estimate-2026-11-28.md supplies the full transverse-density bound
- The selected low-Phi realization and auxiliary coefficient norm are not a source-selected physical state/current
source_bridge:
  status: conditional
  reason: SC-ACT-02 draft p45 eq9.8 supplies the endpoint template and SC-META-52 acknowledges the ultrahyperbolic debt; neither selects this realization or its physical norm
kill_condition: Actual full-dimensional compatible packets violate same-order coefficient Hs propagation at fixed time; this excludes that topology only, not H_modal or derivative-loss completions
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Scoped auxiliary evolution-topology exclusion; no whole-C cell or ledger verdict change
---

# Result and scope

program_target: X-P1-P2
tier: T1
expected_delta: Close local retained-state/edge estimates, then test global evolution in the inherited ordinary coefficient norm.
actual_delta: Positive local closure and an actual global norm-cost theorem; finite-loss linear propagation survives.

**ESTABLISHED:** On fixed finite spatial-frequency patches, the quadratic future-boundary map is bounded for stable×stable, stable×decay and decay×decay inputs, including approach to the common-CW input edge. Stable inputs use the already-declared sum of shell-field L2 norms; free decays use regular q0 L2. This does not replace either by a uniformly equivalent ordinary initial-field norm.

**RULED OUT:** A bounded fixed-time solution operator on one ordinary coefficient H^s, extending all compactly supported compatible CW packets of the selected printed descriptor. An exact actual hook channel gives amplification proportional to spatial frequency despite fixed temporal frequency10 and a fixed distance from all input edges. It requires at least one derivative of loss in that coefficient topology.

**ESTABLISHED survivor:** The same actual scalarizer gives a conservative global linear estimate from H^(s+39) to H^s, uniform as input temporal frequencies approach zero. The sufficient loss39 is not sharp. The pre-existing H_modal evolution remains unitary. No physical state law is adopted.

**NOT MODELED / UNDETERMINED:** The sharp coefficient derivative loss, global nonlinear boundary closure in the inherited norms, a nonlinear invariant domain, physical energy/quotient/current, curved or K77 transfer. GU itself is not falsified. These auxiliary norms are not an observed particle count, positive energy or source-selected prediction.

```gu-typed-objects
result: retained-decay local estimates and global CW coefficient-norm cost
carrier: T*Y tensor End_C(S128), dimension229376, with actual compatible massive kernels LAYER=ambient BRIDGE=conditional-printed-low-Phi CHIRALITY=N/A
pairing: ordinary positive coefficient Hermitian norm for estimates; distinct from held native Krein pairing ON=ambient-bosonic-oneforms
real_structure: frozen K95, spatial signature(9,4); actual primary-minus grade1/2 real subset; no K77 transfer
grading: symbol/exterior channels, not physical family grading
action_owner: source-print -- selected low-Phi endpoint realization, not W2 and not corrected wedge Euler equation
target: Fourier-compatible state evolution and future boundary MAP-TYPE=restriction
```

**Custody.** Basis `ad6e4384809fd12d2cc2ff0da06d730b0fc67035`. [Exact controls](../../tests/program-focus/cw_edge_decay_global_probe.py), [certificate](../../lab/process/cw-edge-decay-global-certificates.json), [Lean arithmetic](../../Lean/GUFormalization/CWGlobalNorm.lean), [evidence](../../lab/process/cw-edge-decay-global.json), [independent reviews](../../lab/process/hostile-reviews/2026-11-28-cw-edge-decay-global-review.md). The finite controls do not formalize integration, Fourier multiplier extension or the full-dimensional packet proof.

## 1. Reuse and the norm distinction

Use the owned full [printed descriptor](cw-fullsystem-domain-2026-11-27.md)
`A_t T' + C(k)T = 0`, where `A_t=P(tau)`, `C=kappa+P(ik)` and `tau²=-1`.
The19 factors are `{1,12,22,30,36,40,42,-1,...,-12}`. The common stable set is
`Omega={k:r(k)²>kappa²/4}`, with38 frequencies `±omega_a`,
`omega_a²=r(k)²+kappa²/(4a)`.

The compatible finite subspace is the sum of the actual kernels of these temporal pencils, not arbitrary full-carrier initial values. The inherited `H_modal` is the direct sum of L2 norms of those actual field amplitudes. A finite sum synthesizes them into an ordinary field with a bounded map. Inverse synthesis was proved only on compact interior patches. The current test settles its global failure; it does not retract the modal theorem.

Layer0: modal coefficient norm, regular companion q/p norm, physical Krein/current norm and ordinary initial-field coefficient norm are different objects. Source observation is a contraction, not this Fourier decomposition. Routes T02/T09/T11/T13/T15 apply. The source does not identify any of these auxiliary norms with physical admissibility.

The old unrestricted printed-equation finite-loss obstruction used exponentially growing modes removed by Omega. The old instantaneous nonlinear graph and two-sided history exclusions have different hypotheses. W2 has a different equation owner. None settles the present stable-domain estimate.

[Craig–Weinstein](https://arxiv.org/abs/0812.0210v3) supplies a scalar nonlocal-constraint comparison, not this matrix descriptor's norm equivalence or nonlinear closure. Fourier synthesis and paired residues are standard tools; no novelty claim is made.

## 2. Retained decays really are actual compatible fields

Reuse the regular threshold cluster `Pi=V A_t`, `N=U A_t`, `N²=delta Pi`. In a smooth local frame `(N e,e)`, `N(q,p)=(p,delta q)`. For `mu=sqrt(delta)>=0`,

`T_free(t,k)=exp(-mu t) (N-mu Pi)e q0(k)`.

Indeed `N(N-mu Pi)=-mu(N-mu Pi)`. This is a full descriptor-compatible homogeneous state. At mu0 its embedding is `N e`, injective on the fixed frame. On a small compact collar the embedding and its inverse on this free graph are bounded. It uses no division by mu.

The actual quadratic vertex is the fixed finite-dimensional bilinear map
`Q(T1,T2)=Phi(T1 wedge T2+T2 wedge T1)`.
Composing Q with these bounded embeddings and output regular forcing rows yields bounded numerators. Smoothness in k across a square root is not needed; boundedness and measurability suffice. This authenticates the applicability of the estimate below without a new polarization census.

## 3. Decay×decay: the simultaneous corner is integrable

Set `C_i=-kappa²/(4a_i)`, `mu_i²=C_i-r(k_i)²>=0` and output `delta=C_out-r(k+l)²>=0`. The future boundary combination has denominator

`lambda+mu1+mu2`, where `lambda=sqrt(delta)`.

Fix a nonnull k, `A=k²`, and write `l=alpha k+y`, `y perpendicular k`, `q=y²`. Then

`delta=C_out-A(1+alpha)²-q`,
`v=mu2²=C2-A alpha²-q`,
`det partial(delta,v)/partial(alpha,q)=2A`.

The inverse is `alpha=(C_out-C2-A-delta+v)/(2A)`, `q=C2-v-A alpha²`.
The measure factor after invariant coordinates is `1/(2sqrt(abs(A)))`. The12 transverse directions have signature(8,4) for A>0 and(9,3) for A<0; each contains a positive two-plane. The same polar integration as in the all-threshold proof bounds the compact quadratic pushforward density even at its critical point. Actual branch and compact-support cutoffs are retained before extending integration domains.

On a held output collar `0<delta<D` and a bounded decay input `0<v<E`, drop mu1 from the denominator. Its squared majorant integrates as

`integral_0^D integral_0^E (sqrt(delta)+sqrt(v))^-2 dv ddelta`
`=4 integral_0^sqrt(D) integral_0^sqrt(E) xy/(x+y)² dy dx`
`<=sqrt(D E)`.

Full26-dimensional Cauchy–Schwarz, pairing `|f(k)|` with this kernel and `|g(l) h(k+l)|` with the determinant-one sum coordinates, gives the actual bilinear L2×L2→L2 boundary estimate. Its norm has a factor `(DE)^(1/4)` times the bounded vertex/density constants. Restricting the output collar to delta<epsilon gives an epsilon^(1/4) tail. All transverse widths are integrated; a lower-dimensional delta-supported model is not an admissible counterexample.

At a null k, `mu1²=C1`. Because all factors and kappa are nonzero, either C1>0 and mu1 is locally bounded below, or C1<0 and no decay state is admitted sufficiently near this point. In the admitted case the denominator is bounded below and compact convolution controls the map. Finite covers therefore handle arbitrary held compact input sets. A uniform epsilon-tail exponent is asserted for the nonnull invariant-coordinate estimate; the null patch also has a vanishing tail by bounded compact-output measure. No unbounded-momentum constant is inferred.

The suggested factor(-4,-4)→(-1) control at k=l=3 positive axis is exactly a simultaneous zero of all three thresholds. The negative-axis factor(+1,+1)→(+1) control also meets all three. The estimate covers both without treating a small divisor as failure.

## 4. Band-edge completion in the inherited modal norm

**Stable×decay:** the denominator is `lambda+mu-i omega`, up to the stable sign. Its modulus is at least `lambda+mu`. The preceding invariant-coordinate bound applies with stable k, A>=kappa²/4, even as omega tends to zero. A positive frequency lower bound is unnecessary.

**Stable×stable:** the preceding all-threshold proof used the invariant map `(alpha,q)->(delta,nu)` with density `W/sqrt(A)`, where `W=omega_b(l)>0`. On a fixed finite Euclidean frequency ball this density stays bounded as W tends to zero; it vanishes rather than diverges. Apply the estimate first for W>=epsilon and then pass by dominated/truncated L2 extension. A>=kappa²/4 remains bounded away from zero. There is no division by W in the final integral.

Use actual vector-valued shell amplitudes and the fixed bilinear Q. No derivative of a polarization frame enters the estimate, so collapsing eigen-coordinates do not create a numerator singularity. These statements are uniform toward the edge for this already-declared H_modal norm. They do not identify a stable regular momentum with bounded separate modal amplitudes when omega vanishes. Output regular frames are held on separated compact threshold collars; complementary forced resonances and global all-output closure are not settled here.

## 5. Actual high-frequency countersequence away from every edge

At kappa12, take negative spatial axis10 and, for R>0,

`k_R=(R+16/R)theta1+(R-16/R)theta10`, so `k_R²=64`.

Let `beta=theta3 gamma3-theta4 gamma4` and `c(tau)=-gamma0`.
Beta is an actual transverse degree1 hook for both covectors
`zeta±=±10i tau+i k_R`. Their square is36. Native Phi and the independently owned compact symbol agree and give

`P_zeta beta=-2 c(zeta)beta`, `P_zeta(c(zeta)beta)=-2q beta`.

Thus the actual a=+1 modes are

`v±=12 beta+2i c(k_R)beta ±20i c(tau)beta`,
`(12+P_zeta±)v±=0`.

Both lie in common-CW support with fixed margin `64-36=28`. No exponential input or threshold singularity is used. The full native solution is

`T_R(t)=[exp(10it)v+ - exp(-10it)v-]/(40i)`
`       =cos(10t)c(tau)beta + sin(10t)[12beta+2i c(k_R)beta]/20`.

The exact probe checks both sine/cosine coefficients directly in the descriptor equation. At `t*=pi/20`, the squared amplification in the fixed positive coefficient norm is

`||T_R(t*)||²/||T_R(0)||² = R²/50+9/25+128/(25R²)`,
`||T_R(0)||²=2`.

Every other fixed positive coefficient norm is equivalent in this finite-dimensional fibre and gives the same unboundedness. This is cancellation between large opposite temporal-mode amplitudes at t0, followed by loss of that cancellation. It is not a negative-energy or runaway-exchange test.

### Full13-dimensional packets and derivative cost

For each R the two kernels extend smoothly over a sufficiently small open ball about k_R by the owned shell projectors; roots are distinct and nonzero there. Extend the displayed vectors, take their normalized difference as initial data and evolve with their actual nearby frequencies. Continuity gives a smaller open ball on which the initial norm stays between fixed positive constants and the t* amplification is at least cR. The ball may shrink with R; choose it inside radius1 and inside Omega.

Multiply by an arbitrary smooth compact bump in that ball and normalize its initial H^s norm. Input and output have the same Fourier support, so the Sobolev weights cancel pointwise up to fixed comparability; |k| is comparable to R. This gives full-dimensional Schwartz packets with

`||T_R(t*)||_Hs >= c R ||T_R(0)||_Hs`.

If the input norm is H^(s+d), the ratio is at least c R^(1-d). Consequently any such global estimate requires d>=1; no same-order H^s bounded evolution can extend this core. The claim is at the displayed fixed time, which suffices to exclude a C0 group on that H^s. It is not an assertion that one derivative is sufficient.

The native primary-minus real adapter is also checked: the real and imaginary quadratures occupy its allowed sharp-skew grades1/2. P is real on this held coefficient basis. Add the conjugate packet at -k, disjoint from the original support. Both squared norms double, preserving the ratio. This is a real-field subset, not a full real-carrier census.

**The observed-Lorentz core does not remove this cost.** A proper positive-plane rotation `theta1->theta4`, `theta4->-theta1` fixes tau and sends the same witness to `k_R=(R+16/R)theta4+(R-16/R)theta10`, `beta=theta3 gamma3-theta1 gamma1`. This is a computational ambient rotation, not an observed Lorentz transformation mixing horizontal and normal directions. Native kernels, coefficient norm ratio and primary-minus quadratures are separately checked. Here `N(k)=sum_(j=4)^13 D_j k_j²`; only the explicit support condition `N>36` is used. The rotated invariant is exactly `N=64>36`, with horizontal spatial momentum zero. No discovery-bet mass-gap or physical verdict is imported. Full-dimensional neighborhoods may be shrunk to stay in the already-owned branch-complete [Lorentz core](bet-mass-gap-cw-symmetry-domain-2026-11-27.md). Thus core support alone does not restore a same-order coefficient estimate if these compatible polarizations remain admitted. Additional polarization or state restrictions are not excluded or selected here.

In H_modal the two initial amplitudes already have size proportional to R. Their separate norms are conserved, so this example does not violate modal unitarity. It proves that globally replacing that norm by the ordinary synthesized-field norm is an invalid shortcut.

## 6. Positive global finite-loss bound from paired roots

The same actual scalarizer gives a positive statement, so this is not the old unrestricted no-finite-loss obstruction. Write

`m(u,q)=u² product_a(u²-4a q)`,
`B_kappa=b_kappa(P,q)`,
`b_kappa(u,q)=[m(-kappa,q)-m(u,q)]/(kappa+u)`.

The quotient is polynomial, with total differential degree at most39, and
`L B=B L=d_kappa(q)I`, `d_kappa(q)=kappa² product_a(kappa²-4a q)`.
For each a set `q_a=kappa²/(4a)`, `delta_a=-r²-q_a` and
`R_a(q)=product_(b!=a)(kappa²-4bq)`.
Modulo `z²-delta_a`, `q(z tau+ik)=q_a`, so reduce

`B_kappa(z tau+ik)/(4a kappa² R_a(q_a)) = U_a(k)+z V_a(k)`

modulo that quadratic. All denominators are nonzero constants. Polynomial reduction preserves total degree: `deg U_a<=39`, `deg V_a<=38`. These bounds may greatly overestimate the actual reduced entries.

Paired residues give `Pi_a=V_a A_t`, `N_a=U_a A_t`,
`N_a²=delta_a Pi_a`; distinct clusters annihilate each other and sum to identity on the compatible finite subspace. There is no inversion of the singular A_t. On Omega,

`T(t,k)=sum_a[cos(omega_a t)Pi_a+sin(omega_a t)/omega_a N_a]T0(k)`.

The quotient `sin(omega t)/omega` has limit t and absolute value at most |t|. Polynomial bounds and Plancherel therefore give

`||T(t)||_Hs <= C_kappa(1+|t|) ||T0||_H^(s+39)`.

This holds first on the smooth compact compatible core and extends by this bound to its indicated coefficient-norm completion. That completion is not automatically H_modal: individual modal amplitudes can diverge near the edge while their paired finite-time expression remains controlled. No such extension is adopted as a physical domain here. The bound is linear on a Sobolev scale with loss, not a bounded group on one H^s or a nonlinear fixed-point theorem.

Thus the available sufficient/necessary derivative-loss window is `[1,39]`, with the lower and upper statements scoped as above. A global finite-loss survivor is a real difference from the unrestricted unstable system. Source physical regularity remains unselected.

## 7. Follow-through and choice accounting

This closes the finite-band stable/decay local boundary questions and the ordinary same-order global coefficient-norm hypothesis. No new state law, weight, physical quotient or action is added. The historical candidate accounting remains10 choice families /4 obligations /net6 /0 source-selected predictions; it is not a count of Standard Model parameters or all GU freedom.

One step2b wave remains. Its decisive question is global quadratic closure in an inherited modal/free-decay topology, retaining the actual high-frequency vertex and paired projectors, or a precisely priced finite-loss iteration. The current upper39 cannot be silently used in a contraction argument that loses derivatives each iteration. A sharper algebraic bound can be useful only if it decides that nonlinear gate. If that gate cannot be settled within the remaining wave, preserve the exact burden and advance the queued antilinear/PT test; no new neighboring-shell census or W2 continuation.

The covered successor registry and progress map retain H_modal, finite-loss linear evolution, all local quadratic boundary estimates and the unresolved physical bridge together. No source-level incompleteness stronger than those named missing inputs is claimed.
