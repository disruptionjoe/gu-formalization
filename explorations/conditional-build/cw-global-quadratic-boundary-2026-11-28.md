---
title: 'CW quadratic boundary: global-input control, all-output obstruction and finite regularity price'
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: X-P1-P2
tier: T1
expected_delta: Decide the global quadratic boundary estimate in inherited modal inputs and intrinsic output topology
actual_delta: Global inputs are bounded into compact output; actual full-dimensional packets exclude unweighted all-output L2; a conservative tame45 derivative bound survives
class_covered: Selected frozen printed low-Phi K95 full bosonic descriptor, common-CW massive modal inputs, intrinsic paired boundary fields in coefficient Sobolev norms
premises:
- Actual P and Phi, all19 factors and compatible H_modal amplitudes from cw-fullsystem-domain-2026-11-27.md
- Paired polynomial residues and auxiliary coefficient norms from cw-edge-decay-and-global-norm-2026-11-28.md
- Future-only boundary law remains a GU* candidate, not a source-selected physical domain
source_bridge:
  status: conditional
  reason: SC-ACT-02 draft p45 eq9.8 supplies the printed endpoint template; SC-META-52 names an ultrahyperbolic debt, but neither selects this realization or its physical state norm
kill_condition: Actual normalized full13D compatible packets have unbounded all-output intrinsic boundary L2 norm; excludes this mapping claim only
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Scoped auxiliary boundary-topology exclusion and positive tame bound; no whole-C or ledger verdict change
---

# Result and scope

program_target: X-P1-P2
tier: T1
expected_delta: Settle the final budgeted global quadratic boundary test.
actual_delta: A global positive estimate with a real regularity cost; the unweighted all-output claim fails.

**ESTABLISHED:** Arbitrarily high-frequency actual common-CW modal inputs give a bounded quadratic future-boundary response on every fixed compact output set. The estimate is uniform to input edges and all19 output thresholds. A stronger estimate controls every output frequency with a conservative45-derivative tame bound.

**RULED OUT:** A bounded global `H_modal L2 × H_modal L2 -> coefficient L2` map into the intrinsic boundary quantity `Y=(N+lambda Pi)x`. Actual primary-minus packets give growth at least `R^(13/2)`. This is not a claim about every global state norm or a physical ghost.

**NOT MODELED / UNDETERMINED:** A full nonlinear invariant domain, global free-decay state norm and lifting from Y to the full descriptor state, a source-selected physical state/current, and transfer to variable coefficients, K77 or the corrected wedge equation. GU is not falsified. The strong positive estimate does not permit a contraction iteration that loses derivatives at each step.

```gu-typed-objects
result: global quadratic future-boundary bounds and intrinsic-output norm obstruction
carrier: Clifford-valued bosonic oneforms, dimension229376, actual massive compatible kernels LAYER=ambient BRIDGE=conditional-printed-low-Phi CHIRALITY=N/A
pairing: fixed auxiliary positive coefficient Hermitian norm; not native physical Krein current ON=ambient-bosonic-oneforms
real_structure: frozen K95 spatial signature(9,4); primary-minus real grade1/2 packet subset; K77 transfer absent
grading: symbol channels, not family/physical weak grading
action_owner: source-print -- selected low-Phi endpoint realization, neither W2 nor corrected wedge Euler equation
target: modal input to intrinsic future-boundary field MAP-TYPE=restriction
```

**Custody:** GU basis `9838ba1e3723b5f9673a84f1e8cb142dc07093f6`. [Probe](../../tests/program-focus/cw_global_quadratic_boundary_probe.py), [certificate](../../lab/process/cw-global-quadratic-boundary-certificates.json), [finite Lean cores](../../Lean/GUFormalization/CWQuadraticBoundary.lean), [evidence](../../lab/process/cw-global-quadratic-boundary.json), [independent reviews](../../lab/process/hostile-reviews/2026-11-28-cw-global-quadratic-boundary-review.md). The92 exact controls and six Lean cores check finite algebra, not integration, norm completion or the full packet proof.

## 1. Reuse, source custody and output typing

Reuse [the full descriptor](cw-fullsystem-domain-2026-11-27.md), [future-only boundary coordinates](cw-one-sided-boundary-2026-11-27.md), [all local thresholds](cw-all-threshold-boundary-estimate-2026-11-28.md) and [paired polynomial residues](cw-edge-decay-and-global-norm-2026-11-28.md). The selected equation is `A_t T'+C(k)T=-F`, `A_t=P(tau)`, `C=kappa+P(ik)`, `tau²=-1`, with actual algebraic `Q(v,w)=Phi(v wedge w+w wedge v)`. Its factor set is `{1,12,22,30,36,40,42,-1,...,-12}`. Put `q_a=kappa²/(4a)`, `Q_sp(k)=k^T D k`, `Omega={Q_sp(k)>kappa²/4}`, and `omega_a²=Q_sp(k)+q_a`. H_modal is the direct sum of actual shell-vector coefficient L2 norms, optionally weighted by `<k>^s`.

Layer0 distinguishes modal amplitudes, regular companion coordinates, ordinary synthesized coefficient norm, physical Krein/current norm and section observation. Routes T02/T09/T11/T13/T15 prevent their identification. No observed family or positivity statement is tested here. [Craig–Weinstein](https://arxiv.org/abs/0812.0210v3) is a scalar comparison, not a proof of this nonlinear matrix boundary law. Polar integration, polynomial residues and dyadic estimates are standard; no novelty claim is made.

For each output factor c, `delta_c=-Q_sp(K)-q_c`, `lambda_c=sqrt(delta_c)>0`. Owned polynomial remainders give `Pi_c=V_c A_t`, `N_c=U_c A_t`, `deg U<=39`, `deg V<=38`, `N_c²=delta_c Pi_c`. Their denominators are nonzero constants. Polynomial identities established on the open stable region extend to every K. This continuation is a statement about the displayed matrices, not a converse theorem reconstructing every full descriptor solution.

For `x_c=Pi_c T`, define the **intrinsic** coefficient-valued quantity `Y_c=(N_c+lambda_c Pi_c)x_c`. Applying the paired identities to the actual forced equation yields

`Y_c'=lambda_c Y_c-(U_c+lambda_c V_c)F`.

Future removal of its growing homogeneous part therefore requires

`Y_c(0,K)=integral_0^infinity exp(-lambda_c t)(U_c+lambda_c V_c)F(t,K) dt`.

For a signed pair of stable inputs, `nu=s_a omega_a(k)+s_b omega_b(l)`, the boundary kernel is

`B_c(f,g)(K)=integral [(U_c(K)+lambda_c V_c(K))Q(f(k),g(K-k))]/[lambda_c-i nu] dk`.

On held compact regular frames it is equivalent to `b=p+lambda q`; globally it is not asserted equivalent to the whole initial state or global free-q0 norm. Y annihilates the independent free decay and its lifting is another problem. Its definition adds no physical metric or state choice.

## 2. Uniform compact-output pushforward for every nonzero k

Fix k !=0, let `n=Jk/|k|`, and write the invariant linear coordinate as

`u=<Jk,K>`.

Let E_+ be the 9-dimensional positive coordinate subspace. Choose a Euclidean two-plane

`V subset E_+ intersect k_+^perp`.

This is always possible because the intersection has dimension at least eight. V is Euclidean-orthogonal to n. Moreover J acts as identity on V, so V is Q-orthogonal to its entire Euclidean orthogonal complement. Complete n and a Euclidean orthonormal basis of V to a Euclidean orthonormal coordinate system. Then uniquely

`K=alpha n+v+z`, with `v in V`, `z in (span(n) direct-sum V)^perp`, `dim z=10`,

and

`u=|k| alpha`,

`Q(K)=|v|^2+Q(alpha n+z)`.

The change is Euclidean orthogonal, hence has absolute determinant one. On the ball `|K|<=R`, alpha and each of the ten z coordinates lie in [-R,R]. For every nonnegative measurable Psi, polar integration over the full positive v-plane gives

`integral_(|K|<=R) Psi(Q(K),u(K)) dK`

`<= pi (2R)^10 / |k| * integral_R2 Psi(q,u) dq du`.                         (1)

To see the bound, first enlarge only the v-domain to its whole two-plane. For fixed alpha,z, its polar integral is

`pi integral_(Q(alpha n+z))^infinity Psi(q,|k|alpha)dq`

and is bounded by the full q integral. Integrate the ten z coordinates over their bounded box and change alpha to u. No continuity in the choice of V is needed: (1) is a pointwise-in-k bound with the same constant. There is no Lorentz-frame growth, near-null exception, missing spectator volume, or inversion multiplicity.

### Convert to the actual phase

Put `A=Q(k)`, `l=K-k`, and `W=omega_b(l)>0`. Then

`Q(l)=A+q-2u`,

`W^2=A+q-2u+kappa^2/(4b)`,

`nu=s_a omega_a(k)+s_b W`.

For fixed q and k, the chosen W>0 branch is one-to-one and

`|du/dnu|=W`, `|dq/ddelta|=1`.

The actual stable-input cutoff on l depends only on q,u and k and can be retained throughout this change. On the image of the held output ball,

`W^2<=|l|^2+kappa^2/4 <= (|k|+R)^2+kappa^2/4`.

Since `k in Omega_kappa` implies `|k|>|kappa|/2`,

`W/|k| <= M_(kappa,R) := sqrt[(1+2R/|kappa|)^2+1]`.

Consequently, for every nonnegative measurable Phi,

`sup_(k in Omega_kappa) integral_(K in O, K-k in Omega_kappa)`

`          Phi(delta(K),nu(k,K-k)) dK`

`<= C_push integral_R2 Phi(d,s) dd ds`,

`C_push=pi(2R)^10 M_(kappa,R)`.                                      (2)

One must retain the output-ball image when using the upper bound for W, then enlarge its invariant-coordinate image after replacing W/|k| by its uniform bound. This avoids an invalid bound on W over all invariant coordinates.

Both temporal signs only change a translation and orientation of nu. All 19 branch values obey `|kappa^2/(4b)|<=kappa^2/4`. No positive lower bound on W is used. The density factor tends to zero at W=0, so truncation followed by the uniform estimate covers limits to the input edge. There is also no nonnull or noncollinearity assumption on K in this pushforward theorem.

### The global-input bilinear bound

Let f and g be actual coefficient-vector amplitudes of the two chosen input branches, supported anywhere in Omega_kappa. Taking their pointwise coefficient norms, define

`w(d,s)=1_(0<d<D)/sqrt(d+s^2)`.

There is no temporal-frequency cutoff:

`||w||_L2(R2)^2 = integral_0^D pi/sqrt(d) dd = 2pi sqrt(D)`.

Against an output test h supported in O, apply Cauchy–Schwarz on the full `(k,K)` space to

`|f(k)| w(delta(K),nu(k,K-k))`

and

`|g(K-k)| |h(K)|`.

By (2), the first squared integral is at most `C_push ||f||_2^2 ||w||_2^2`. The second is at most `||g||_2^2 ||h||_2^2`, using the determinant-one change `(k,K)->(K-k,K)`. Therefore

`||1_O 1_(0<delta<D) B(f,g)||_2`

`<= N sqrt(2pi C_push) D^(1/4) ||f||_2 ||g||_2`.                     (3)

The proof is absolute and also defines the integral almost everywhere. Removing `0<delta<epsilon` has bilinear operator-norm error `O(epsilon^(1/4))`. Input threshold truncations can be removed by L2 convergence and the same bound. Summing the finite 38 input branches gives the corresponding H_modal bilinear estimate, with a finite branch-count factor. Each of the 19 separated output clusters has its own bounded regular-coordinate map; on a fixed compact union, their finite sum is also controlled.

Thus no normalized global H_modal pair can force this particular compact regular output boundary map to blow up, even by escaping to arbitrarily large near-null momenta or concentrating anisotropically. A proposed unweighted countersequence for this target must fail one of the stated hypotheses, not merely exploit a small denominator.


The result applies to intrinsic Y as well as held regular output rows: the polynomial numerator is bounded on any fixed output ball. Inputs can approach the common-CW edge because their actual vector amplitudes, not inverse polarization coordinates, carry the norm. Neither a lower bound on W nor smooth global frames is required.

## 3. Global output extension for the intrinsic boundary variable

The following stronger consequence controls all output frequencies, with an explicit and deliberately coarse derivative cost. It concerns the intrinsic boundary functional, not an already reconstructed full state.

For each factor c, the paired scalarizer construction gives polynomial matrices `U_c(K),V_c(K)` of degrees at most 39 and 38. Define

`Pi_c=V_c A_t`, `N_c=U_c A_t`, `delta_c=C_c-Q(K)`.

The identities obtained on the open common-CW set are polynomial in K and therefore extend to every real K. In particular,

`Pi_c^2=Pi_c`, `Pi_c N_c=N_c Pi_c=N_c`, `N_c^2=delta_c Pi_c`,

`Pi_c V_c=V_c`, `N_c V_c=U_c`, `N_c U_c=delta_c V_c`.

The relevant scalarizer denominators are constants: modulo `z^2-delta_c`, the covector square is exactly `kappa^2/(4c)`. Different factors have distinct such values at fixed kappa !=0. Thus this polynomial continuation does not cross a hidden frequency-dependent denominator or require an inverse of the singular time matrix.

For the actual forced equation `A_t T'+C(K)T=-F`, the cluster field `x=Pi_c T` obeys

`x'=N_c x-V_c F`.

This is a projected identity for an actual solution, using `V_c C=-N_c`. Conversely, the boundary functional below can be defined directly from the two stable input amplitudes. Nothing here asserts that arbitrary solutions of this projected equation satisfy every algebraic row of the full descriptor system, or that an arbitrary Y_c can be lifted to a globally controlled full solution.

On `delta_c>0` set `lambda=sqrt(delta_c)` and define the intrinsic field

`Y_c=(N_c+lambda Pi_c)x`.

Then exactly

`Y_c'=lambda Y_c-(U_c+lambda V_c)F`.

The future condition `lim_(t->infinity) exp(-lambda t)Y_c(t)=0` consequently imposes

`Y_c(0)=integral_0^infinity exp(-lambda t)(U_c+lambda V_c)F(t)dt`.

For two stable input characters this gives the multiplier

`(U_c+lambda V_c) Q(f,g)/(lambda-i nu)`.

This is the intrinsic boundary functional requested here. No division by lambda, singular growing projector, selected global Jordan frame, or inverse modal synthesis has been inserted. Its values satisfy the appropriate growing eigenspace relation because `(N_c-lambda Pi_c)(U_c+lambda V_c)=0`.

### Ball bound and a negative-Sobolev global output

For R>=1 and |K|<=R,

`lambda<=sqrt(|C_c|+R^2)<=C_kappa R`,

`||U_c+lambda V_c||<=C_kappa R^39`.

In the uniform pushforward proof, `sqrt(C_push)<=C_kappa R^(11/2)`. Taking `D=|C_c|+R^2`, the kernel L2 norm is at most `C_kappa R^(1/2)`. Therefore

`||1_(|K|<=R) Y_c(f,g)||_2 <= C_kappa R^45 ||f||_Hmodal ||g||_Hmodal`.       (4)

The exponent is exactly `39+11/2+1/2=45`; no spatial-dimension factor is added a second time. The fixed-radius construction defines a consistent measurable output on increasing balls. Summing dyadic annuli gives

`||Y_c(f,g)||_H^(-s) <= C_(kappa,s) ||f||_Hmodal ||g||_Hmodal`, for s>45.

The strict inequality here is appropriate to the coarse ball-growth estimate; an endpoint H^(-45) claim is not inferred.

### Tame positive-Sobolev output with 45 derivatives

Let `Hmodal^m` weight each actual input shell amplitude by `<k>^m`. On the output annulus `2^j<=|K|<2^(j+1)`, at least one input has Euclidean magnitude at least `2^(j-1)`. Split the bilinear expression exactly as

`B(f,g)=B(f_hi,j,g)+B(f_lo,j,g_hi,j)`

on that annulus; the omitted low-low term has no Fourier support there. Apply (4) with ball radius `2^(j+1)`. It gives

`||Y_c(f,g)||_(L2 annulus j)`

`<= C_kappa 2^(45j) [||f_hi,j||_2 ||g||_2 + ||f||_2 ||g_hi,j||_2]`.       (5)

Retain the high-frequency tails before summing rather than replace every tail by one uniform weighted norm. For every m>0,

`sum_(j>=0) 2^(2mj) ||f_(|k|>=2^(j-1))||_2^2 <= C_m ||f||_Hmodal^m^2`.

This follows by exchanging the nonnegative sum and integral: for fixed k the geometric sum over `2^(j-1)<=|k|` is bounded by a constant times `<k>^(2m)`. Taking m=s+45 in the squared annular estimate (5), and treating the unit output ball separately, proves for s>=0

`||Y_c(f,g)||_H^s`

`<= C_(kappa,s) [||f||_Hmodal^(s+45) ||g||_Hmodal`

`                  + ||f||_Hmodal ||g||_Hmodal^(s+45)]`.                 (6)

This is a sufficient derivative cost, not an optimal derivative count. The finite branch and output-factor sums only change constants. The estimate is consistent with a possible failure of an all-output unweighted L2 bound; the upper estimate alone does not prove that negative claim. Sections4–5 supply the separate actual countersequence.

### Scope after the extension

Equations (4)–(6) remove the all-output gap for this **quadratic intrinsic future-boundary functional**. They do not by themselves reconstruct a global full field from Y_c, estimate the free retained-decay data, control complete forcing histories, give a contraction at one fixed Sobolev index, or produce a nonlinear invariant domain. In particular a derivative-losing tame estimate is not an ordinary Banach fixed-point theorem. Any required inverse or reconstruction map must be separately typed and bounded. No new physical norm or source state law is adopted.
## 4. Exact actual high-frequency fixture

Use held K95 axes tau=theta0, sigma=theta1 and eta=theta10, with squares
-1,+1,-1. For R>6 and kappa12 set

```
k=2R sigma+R eta, l=-2R sigma+R eta,
xi1=omega tau+k, xi2=-omega tau+l,
omega²=3R²+36, K=k+l=2R eta, delta=4R²-36.
```

Both spatial input squares are3R²>36; both are actual factor1 CW modes.
The output factor1 decay rate is lambda=sqrt(delta), comparable to R.
This is far from an output threshold, not a small-divisor fixture.

Let

```
beta1=theta3 gamma3-theta4 gamma4,
beta2=theta3 gamma3-theta5 gamma5,
v_i=12 beta_i+2 c(i xi_i) beta_i.
```

These are true H1 transverse hook polarizations. The native hook identities
give `(12+P(i xi_i))v_i=0`. Their exact coefficient norms are

`||v_i||²=64(R²+9)`.

Hence w_i=v_i/[8 sqrt(R²+9)] are unit **actual modal field vectors**.
The actual full polarized force before this normalization is

`F=Phi(v1 wedge v2+v2 wedge v1)`
` =32(R²-36) Phi1-64(R²-36) theta3 gamma3`.

This identity follows directly from the Clifford products: the mixed
kappa/Gamma commutators vanish, and
`Phi(theta^i wedge theta^j gamma_i gamma_j)=2 sum_(a!=i,j)theta^a gamma_a`
on these positive spectator axes. The exact probe checks it with
Engine.Phi, rather than importing a W2 or trace-channel surrogate.

The proper positive rotation3->4,4->-3 preserves output momentum and the
actual operator. Its odd projection of F is f beta, where

`beta=beta1`, `f=32(36-R²)`.

Put A=c(tau)beta and B=12beta+2i c(K)beta. On this projected source the
**actual full resolvent** has the simple numerator

`U beta=B/4`, `V beta=A/2`.

The native identities checking this are
`A_t V beta=beta`, `C V beta+A_t U beta=0`,
`C U beta=-delta beta`. Therefore
`L(z)^(-1) beta=(B/4+z A/2)/(z²-delta)` exactly; no omitted complementary
channel is involved in this projected receiver.

The fixed bounded coefficient row

`ell_A(Z)=(-Z_(theta3,gamma0 gamma3)+Z_(theta4,gamma0 gamma4))/2`

satisfies ell_A(A)=1, ell_A(B)=0. Its odd symmetry means it sees precisely
the projected source above. Since nu=0, the unit-input intrinsic future
response has

`ell_A Y(0,K)=(36-R²)/(4(R²+9)) -> -1/4`.

This is an actual normalized nonzero receiver, not growth caused by an
unnormalized polarization. The native probe verifies the actual kernel, compact/native binding, norms, full polarized force, proper-rotation odd projection, three resolvent identities and fixed receiver.

## 5. Full thirteen-dimensional packet proof

A pointwise receiver alone is insufficient. The following gives a bounded
route from that fixture to an actual global L2 countersequence.

Write k=R u,l=R v and epsilon=1/R. Near the fixed centers
u0=2sigma+eta and v0=-2sigma+eta, both spatial squares stay strictly
positive, and -(u+v)² stays strictly positive. Thus the scaled input
frequencies and output lambda/R are real analytic in epsilon and the
thirteen-dimensional variables u,v; lambda/R has a positive lower bound.
In particular the future denominator

`(lambda-i nu)/R`

is bounded away from zero in modulus on a fixed small product neighborhood.

Construct actual hook charts without dividing by the vanishing scaled
mass-shell norm. Project the spectator vectors3,4 (or3,5) into the spatial
k-perpendicular space using k², and perform positive Gram–Schmidt there.
Since k²/R² is bounded below near3, these operations are analytic with
uniformly bounded coefficients in u. The resulting two orthonormal positive
spatial vectors are also perpendicular to time. Their tracefree symmetric
form/Clifford tensor beta(u) is a true H1 hook for every corresponding
zeta, and equals the displayed seed at the center. Normalize
`12 beta(u)+2c(i xi(Ru))beta(u)` by its coefficient norm. This gives unit
actual kernel vectors analytic in epsilon,u, including epsilon0; their
leading coefficient is nonzero. Do the same for the second input.

The actual operators U_a,V_a are polynomials in K of degrees at most39,38.
Thus the fixed-row kernel

`M_R(u,v)=ell_A [(U_a+lambda V_a)Q(w1,w2)/(lambda-i nu)]`

is Laurent analytic in epsilon with a **finite** pole order at most38,
uniformly on the fixed product neighborhood. No assertion that the entire
symbol has order0 is needed. Let p be its highest nonidentically-zero power
of R there. The exact central receiver tending to -1/4 proves p>=0; p>0
may vanish exactly at the central fixture. Choose a nearby pair where this
leading coefficient is nonzero. After a fixed complex phase rotation and
shrinking product patches, its real part is bounded below by c>0 throughout
those patches. The Laurent expansion then gives the same sign and a bound
`Re M_R >= c R^p` for all sufficiently large R.

Take nonnegative smooth bumps phi,psi supported in these fixed scaled input
patches, positive on smaller patches. Define actual modal input amplitudes

```
f_R(k)=R^(-13/2) phi(k/R) w1(1/R,k/R),
g_R(l)=R^(-13/2) psi(l/R) w2(1/R,l/R).
```

Their H_modal L2 norms are fixed. For output K=R Z in a fixed scaled
subpatch of the sum, the convolution integral has a common positive-volume
subregion where both bumps are bounded below. The input factors R^-13
cancel the integration Jacobian R^13, giving

`Re ell_A Boundary(f_R,g_R)(R Z) >= c' R^p`.

The output subpatch has full thirteen-dimensional volume proportional to
R^13. Hence

`||Boundary(f_R,g_R)||_L2 >= c'' R^(13/2+p)`, with p>=0.

This rules out a bounded global H_modal L2 x H_modal L2 -> coefficient-L2
map for the intrinsic Y. All packets are smooth and full-dimensional;
neither plane-wave delta distributions nor frozen transverse widths are
used. Finite-R future integrals converge because lambda>0.

The real and imaginary quadratures remain primary-minus sharp-skew grades1
and2 under the real spatial frame construction. Append conjugate patches
at opposite frequencies. Other pair sums can be separated from the chosen
output patch; the real-field norms change only by fixed factors. Thus the
countersequence has a real primary-minus subset, with no full real-carrier
census or individually Theta-fixed-state assertion.

## 6. Price and limits

Derivative accounting must specify its convention. This family requires

- d1+d2 >=13/2+p for Hmodal^d1 x Hmodal^d2 -> L2;
- s>=13/2+p for Hmodal^s x Hmodal^s -> H^s;
- r>=13/2+p for unweighted modal inputs -> H^(-r).

Only the lower bounds with p>=0 are asserted; p is not computed and no
sharpness is claimed. The balanced first inequality gives each input at
least13/4 only when equal losses are imposed. A conservative polynomial
weighted-output upper estimate can coexist with this failure.

The unweighted global-input to **fixed compact output** theorem is not
contradicted: this countersequence sends its output support to infinity.
Nor does the test prove a global full-state obstruction in every possible
norm: Y contains the frequency-dependent boundary operator N+lambda Pi,
and the remaining decaying free state is not measured by it. Full nonlinear
invariance, global propagation, physical state selection and a source-GU
verdict remain outside the proved mapping claim.

## 7. Decision, retained survivors and budget pivot

The result closes the proposed unweighted global mapping claim and supplies a positive global tame boundary functional. For the tame one-high-input convention, the necessary cost is at least13/2 and the sufficient bound is45; these are not sharp. For two equally weighted inputs to L2, only the necessary per-input bound13/4 follows. The analytic proof never claims p=0. A fixed-coefficient convolution control has the same dimensional scaling, while a zero vertex gives zero response: this is a calibrated mapping test, not a GU-unique physical instability.

The earlier local stable/decay results, H_modal linear unitarity, and coefficient linear loss window[1,39] remain. The new global theorem concerns stable×stable forced boundary data. A global norm for independently retained decays, full forced-state reconstruction, complementary resonant/algebraic components and nonlinear iteration remain unbuilt. The source has not selected any of these auxiliary completions. No new physical choice is adopted; the historical candidate grouping remains10 choice families /4 obligations /net6 /0 source-selected predictions, not a count for all GU or the SM.

The fifth/final CW2b wave is consumed. The bounded investigation is complete; nonlinear predictability is **INCOMPLETE with named burdens**, not declared solved or impossible. Under the existing counter127 cadence the next run is LC-BETS; the next ordinary B step is the already-queued classical antilinear/PT realization test on the actual declared sector. It must reuse the accepted Theta/time-direction distinction, Jordan2 and norm costs rather than re-prove them or substitute W2's quaternionic structure. No schedule, governance, canon, source or ledger verdict changes.
