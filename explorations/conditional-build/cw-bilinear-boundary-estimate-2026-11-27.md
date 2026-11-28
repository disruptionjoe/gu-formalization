---
title: Uniform local bilinear control of the one-sided CW boundary
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T2
expected_delta: Decide the ordinary L2 bilinear estimate left open by the smooth-packet boundary survivor
actual_delta: The actual nonlinear phase has a local absolute L2 bilinear bound with threshold tail O(epsilon^1/4); the argument covers all seven positive-factor output thresholds and all signed massive stable input branches, while a negative-factor collinear locus remains untested
class_covered: Selected frozen low-Phi printed K95 descriptor, complex compatible common-CW massive input modes on sufficiently small compact patches, regular positive-factor output threshold coordinates, future boundary relation with independent decaying state
premises:
- Actual descriptor reduction and future relation in cw-one-sided-boundary-2026-11-27.md
- Complete nineteen-factor symbol and compatible common-CW modal domain in cw-fullsystem-domain-2026-11-27.md
- Smooth bounded input polarizations and quadratic vertex on fixed compact patches; ordinary auxiliary coefficient L2 norm
- No source-selected physical state rule or norm; SOURCE template SC-ACT-02 and ultrahyperbolic debt SC-META-52 remain conditional
source_bridge:
  status: conditional
  reason: The source does not uniquely select this printed realization or future boundary law; the result removes a mathematical obstruction to this proposed GU* repair only
kill_condition: Failure of the actual Jacobian/injectivity or descriptor binding withdraws the estimate; no nonlinear manifold or source-GU claim follows from the local quadratic bound
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: T2 survivor evidence on X-P1-P2; no cell or ledger verdict change
---

# A uniform bound, with a precisely located remaining stress test

program_target: X-P1-P2
tier: T2
expected_delta: Decide the actual local ordinary-Sobolev bilinear boundary estimate.
actual_delta: A bounded quadratic boundary map, seven-threshold extension, quantitative forward upper bounds and one explicit uncovered collinear locus.

**ESTABLISHED:** on sufficiently small fixed input patches, the actual one-sided boundary response satisfies

`||B(f,g)||_L2 <= C ||f||_L2 ||g||_L2`.

The constant does not depend on Fourier derivatives of the input amplitudes or on proximity to the output threshold. Its tail on `0<delta<epsilon` is `O(epsilon^(1/4))` in bilinear operator norm. This proves the estimate left open by the [previous wave](cw-one-sided-boundary-2026-11-27.md). On fixed compact frequencies it is also an ordinary finite-order Sobolev estimate, with patch-dependent constants.

The proof extends locally to all seven positive-factor output thresholds and every pair of the38 signed massive input branches in the common stable domain. It uses an actual change of variables, not a frozen-phase approximation or a new carrier census.

**RULED OUT:** a normalized L2 concentration countersequence to this local bound on these patches. This is a consequence of the positive estimate, not a new physical exclusion. The older CW-only instantaneous graph exclusion remains unchanged.

**NOT MODELED / UNDETERMINED:** a complete nonlinear invariant state domain, all generated outputs and negative-factor threshold tangencies, interactions with independent decaying states, a source-selected boundary law or positive physical norm. A specific negative-factor rank-loss example is identified below, without declaring it a failure.

Outcome: **SURVIVES** the local quadratic ordinary-Sobolev boundary test; **INCOMPLETE** as a nonlinear GU* theory or selection law.

```gu-typed-objects
result: ordinary L2 one-sided boundary estimate
carrier: T*Y tensor End_C(S128), full complex compatible massive modes LAYER=ambient BRIDGE=selected-printed-dictionary CHIRALITY=N/A
pairing: auxiliary coefficient L2 norm on compact Fourier patches, not a physical conserved norm ON=declared_complex_modal_carrier
real_structure: K95; owned primary-minus real trace adapter retained; no automatic full real-carrier or K77 transfer
grading: Clifford spectral channels, not physical chirality
action_owner: source-print -- selected low-Phi equation realization; not W2 or corrected wedge Euler action
target: quadratic future boundary relation with independent decaying state MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Bilinear integral inequalities are tools. The source-required object and physical state law are not supplied by the inequality. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md), GEOMETER T02/T11/T13/T15.

## 1. Reuse, decision and source footing

Basis `1f05c3a58819833e1fe1d4d783970dfe9a46676c`. The prior result supplies the full regular threshold state `x'=Nx−VF`, `N²=delta Pi`, with regular companion coordinates

`q'=p−g0`, `p'=delta q−g1`.

For lambda=sqrt(delta)>0, the no-future-growth condition fixes `b=p+lambda q`, with harmonic denominator `lambda−i nu`; q(0) remains free. The actual force receiver is nonzero (104448 at the original pair). All those algebraic facts are reused. No source operator, action or new physical state prescription is constructed here.

SC-ACT-02 (draft p45 eq9.8) supplies the endpoint template, not a unique low-Phi dictionary. SC-META-52 (TOE01:17:10) acknowledges ultrahyperbolic/boundary debt, not this future rule. The fixed smooth-packet result did not control ordinary L2 input data, because its constants used Fourier derivatives. This wave tests exactly that missing premise.

Outcomes were fixed in advance: a uniform bound opens nonlinear-domain work; a normalized counterexample would require a changed topology or a pivot. Actual phase geometry and the new bound supply the positive outcome. Neither makes all of class C or SOURCE GU viable. The strongest independent alternative remains a physical PT/norm test; it also needs a declared domain.

## 2. The actual nonlinear phase and the deciding Jacobian

Use the original kappa12 trace patches around

`k0=(28/3)sigma+3eta`, `l0=−(28/3)sigma+3eta`,

with sigma²=+1, eta²=−1. Their common spatial square703/9 exceeds36. The signed phase and output distance are

`nu(k,l)=omega(k)−omega(l)`, `omega(v)=sqrt(r(v)²−3)`,
`K=k+l`, `delta(K)=−r(K)²−36`.

Write active coordinates `k2=(x,y)=(k_sigma,k_eta)`, `l2=(u,v)`, and the other eleven coordinates as z,w. Keeping k,z,w fixed, the actual map `l2 -> (delta,nu)` has determinant

`J_l=2(k_eta l_sigma−k_sigma l_eta)/omega(l)`.

At the center its derivative matrix and determinant are

`[[0,12],[14/13,9/26]]`, `J_l=−168/13`.

These are derivatives of the actual square-root phase and quadratic output norm. No linearization is substituted into the operator.

Choose sufficiently small convex active l-patches and small compact parameter patches for k,z,w. Continuity makes the derivative uniformly close to this fixed invertible matrix. The segment estimate, after multiplication by its inverse, makes the map uniformly injective on each such l-patch. Its Jacobian absolute value has one lower bound `j0>0` for all parameters. This proves the change-of-variables hypotheses; a nonzero determinant at just one point would not by itself establish global injectivity on an arbitrary patch. No explicit numerical patch radius is asserted.

## 3. An elementary bilinear estimate in all13 spatial variables

Every actual regular-coordinate boundary component has the form

`B(f,g)(K)=integral n(k,K−k,sqrt(delta)) f(k)g(K−k) / (sqrt(delta)−i nu(k,K−k)) dk`,

restricted to the compact output collar `0<delta<D`. The full matrix numerator n, including the actual quadratic vertex and both coordinate forcing terms, is bounded on the chosen patches. Square roots in this bounded numerator cause no difficulty; they are not put into the change-of-variables map.

Let h be an arbitrary L2 output test function. It suffices to bound the absolute trilinear integral. Replace the numerator by its finite bound M and write

`w(d,v)=1_(0<d<D, |v|<L) / sqrt(d+v²)`.

For fixed spectator z,w, apply Cauchy–Schwarz in the four active input variables to the two factors

`|f_z(k2)| w(delta,nu)` and `|g_w(l2)| |h_(z+w)(k2+l2)|`.

For the first squared integral, change l2 to (delta,nu) at fixed k2. Its bound is `j0^−1 ||f_z||²_2 ||w||²_2`. For the second, change k2 to K2=k2+l2 at fixed l2; determinant1 gives `||g_w||²_2 ||h_(z+w)||²_2`. Thus the active integral is at most

`M j0^(−1/2) ||w||_2 F(z)G(w)H(z+w)`,

where F,G,H are the active-slice L2 norms.

The spectator directions cannot be discarded. If E is the bounded projection of the first input patch onto its eleven spectators, then

`integral F(z)G(w)H(z+w) dz dw <= |E|^(1/2) ||F||_2 ||G||_2 ||H||_2`.

Indeed Cauchy–Schwarz in w bounds its inner integral by `||G||_2||H||_2`, and Cauchy–Schwarz on E controls the remaining F integral. These norms are exactly the full13-dimensional norms. Finally,

`||w||²_2 <= integral_0^D integral_R (d+v²)^(-1) dv dd = 2 pi sqrt(D)`.

By L2 duality,

`||B(f,g)||_2 <= M j0^(−1/2) |E|^(1/2) sqrt(2 pi) D^(1/4) ||f||_2||g||_2`.

Vector-valued modes follow by finite-dimensional norm bounds, or componentwise with a finite constant. Actual smooth polarizations on compact compatible modal patches identify their amplitude L2 norms with the relevant coefficient norms; no global high-frequency equivalence is claimed.

The estimate first applies to smooth compact amplitudes and extends uniquely by density to L2. Absolute integrals have an L2 majorant: apply the same bound to increasing bounded kernel truncations and nonnegative input amplitudes, then use monotone convergence. Thus the result is not merely a formal principal-value assignment. Replacing D by epsilon shows convergence of threshold truncations in bilinear operator norm at rate `O(epsilon^(1/4))`.

The earlier double-divisor kernel fails this test: `1/(d+v²)` has nonintegrable square near d0. The one-sided boundary relation and the frequency-locked state remain different operators.

## 4. Extension to every positive-factor threshold

Let `a` be any of `{1,12,22,30,36,40,42}`. Its output threshold is

`r(K)²=−kappa²/(4a)<0`, `delta_a=−r(K)²−kappa²/(4a)`.

Choose any two signed massive input branches in the common CW region `r(k)²,r(l)²>kappa²/4`, with frequencies

`nu=s1 sqrt(r(k)²+kappa²/(4b)) + s2 sqrt(r(l)²+kappa²/(4c))`.

These are smooth and nonzero on compact interior patches. The two l-derivative covectors are proportional respectively to `J K` and `J l`, where J is the spatial signature matrix. They cannot be collinear at the threshold: that would make l proportional to K, contrary to their opposite squared-norm signs. Some two-coordinate minor is therefore nonzero. Use those two coordinates as active variables, and repeat the preceding argument with the other eleven as spectators.

The scalarizer at this shell is `4a kappa²(z²−delta_a) R_a(q)`. Its other factors stay separated near temporal zero. The prior shell-projector chain argument extends every threshold kernel vector to a length-two temporal chain, while the scalar annihilator excludes longer chains. Hence the full regular companion-coordinate construction applies at each such output. No reuse of the a1 normalization as if it held at every a is made; the left-shell factor would be kappa/(2a).

This proves a **local** boundary estimate for every input-branch pair at every positive-factor output threshold, for all bounded actual vertex matrices. There are no uniform constants asserted across the unbounded common-CW domain, near input band edges or across arbitrarily large patches. At a nonzero phase the threshold denominator is already regular; the difficult case is nu0. Complementary resonances away from temporal zero require their own localization.

## 5. Forward response: a quantitative upper bound, not an instability

For the held input pair, choose the regular representative q(0)=0. The forced harmonic solution in the threshold block is

`q(t)=(g1+i nu g0) K_t(lambda,nu)`,
`K_t=(exp(i nu t)−exp(−lambda t))/(lambda²+nu²)`,
`b(t)=(g1+lambda g0) exp(i nu t)/(lambda−i nu)`, `p=b−lambda q`.

The formulas include forcing in the first equation; omitting g0 would change the boundary adapter. Apply the same absolute bilinear estimate with the appropriate scalar kernels. An exact integral gives, for t>=0,

`integral_0^infinity integral_R |K_t(sqrt(d),nu)|² dnu dd = 2 pi t`.

For example, integrate nu first to obtain

`pi[1−(1+2lambda t)exp(−2lambda t)]/(2lambda³)`;

then use dd=2lambda dlambda and one integration by parts. On a finite collar,

`||nu K_t||²_(L2(d,nu)) <= 4 pi sqrt(D)`,
`||lambda K_t||²_(L2(d,nu)) <= 4 pi sqrt(D)`.

Consequently, with patch constants independent of f,g,t,

`||q(t)||_2 <= C(1+sqrt(t)) ||f||_2||g||_2`,
`||p(t)||_2 <= C' ||f||_2||g||_2`.

The second bound follows from b−lambda q and the displayed weighted-kernel controls (lambda nu K_t is also bounded by sqrt(D) times nu K_t). Free decaying q(0) adds `exp(−lambda t)q(0)` and slope `−lambda exp(−lambda t)q(0)`, bounded on the collar. The separated full-descriptor forced components remain bounded when the held phase patches avoid their poles; they are not discarded algebraic equations.

This is an upper bound, not a proof that any solution grows like sqrt(t), nor a nonlinear stability theorem. The prior fixed-smooth-packet forward-uniform bound is stronger in time but uses stronger weighted data. No contradiction arises: the present constants do not use Fourier derivatives. Interactions involving independently populated decaying modes have not been included in this pairwise forced calculation.

## 6. A negative-factor locus where this proof loses its hypothesis

At kappa12 take output factor a=−2 and a positive spatial vector K with K²18. Let

`k=(5/2)K`, `l=−(3/2)K`.

Use input factors b=−1 and c=+1, with opposite temporal signs. Then

`k²=225/2>36`, `l²=81/2>36`,
`omega_b(k)²=omega_c(l)²=153/2`, `nu=0`.

Both inputs are in the full common stable domain and their sum is K. Because k,l,K are collinear, both single-input maps to (delta,nu) have rank1 at this point. Swapping the input used for the change of variables does not restore rank2. The full pair phase map still has rank2, and the relative group velocities differ.

**UNDETERMINED:** whether the actual quadratic vertex has a nonzero projection into this output channel, and whether curvature in the twelve transverse directions restores a bilinear bound. Rank loss is not a counterexample, and freezing those directions is not a valid L2 concentration argument. A convenient exact representative is `K=3(theta1+theta2)`, with input time frequency `3sqrt(34)/2`.

The cheapest next discriminator is the actual vertex projection. A zero projection removes this proposed forcing witness; a nonzero projection justifies a transverse estimate or normalized countersequence. This changes the next action more directly than constructing a full nonlinear manifold before checking its remaining interactions.

## 7. Literature, validation and cost

The primary [Bennett–Bez–Buschenhenke–Cowling–Flock theorem](https://arxiv.org/abs/1811.11052), Theorem1.1, proves a general local nonlinear Brascamp–Lieb inequality for C2 submersions with finite center linear datum; it does not require simplicity. Its five-map formulation independently supports the estimate above, including the eleven spectator directions. The direct change-of-variables proof makes that external theorem unnecessary for the scientific conclusion. No novelty claim is made.

The exact controls authenticate the reused actual descriptor/forcing certificates, differentiate the nonlinear phase, check the two changes of variables, kernel integrals and harmonic reconstruction, verify all seven signs and the uncovered negative-factor kinematics. The full functional-analysis argument is independently reviewed written mathematics, not a Lean-certified theorem. No new Lean claim is made for this T2 result.

No action, physical state law or choice family is adopted. The historical10/4/net6/0 choice budget remains attributed to its candidate, not a universal GU parameter count. The future-law/topology/free-state costs of the proposed repair remain explicit. No source-selected prediction is earned by a bounded mathematical response.

The weakest unproved link is now nonlinear closure across all required interactions and the physical-state/current bridge. The next test is the explicit uncovered negative-factor vertex, with retained-state interactions and global frequency control still required. Auxiliary-field localization and whole-family section tomography are separately ranked considerations; their analogies cannot replace this missing estimate or select a physical law.

[Exact probe](../../tests/program-focus/cw_bilinear_boundary_probe.py) · [certificate](../../lab/process/cw-bilinear-boundary-certificates.json) · [review evidence](../../lab/process/cw-bilinear-boundary.json).
