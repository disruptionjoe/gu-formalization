---
title: "K2570 Which conserved detector survives unstable Cauchy continuation?"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact observation continuity and deterministic recovery on the selected local homogeneous family; no physical detector or preparation selection
scripts:
  - tests/channel-swings/k2570_detector_recovery_probe.py
---

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
result: K2570
carrier: K2568 zero-normal-derivative omega-harmonic homogeneous fields on the same local A7 times B7 tube LAYER=toy CHIRALITY=N/A
pairing: actual compact conserved metric-test duality and explicitly supplied positive coefficient norms ON=declared_carrier
real_structure: real harmonics, real response coefficients and deterministic real noise
grading: gauge-invariant scalar readout, complete field, preparation prior and observation noise remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion
target: specified scalar detector continuity and sharp worst-case readout recovery MAP-TYPE=evaluation
```

# A fixed readout can be recoverable when the complete field is not

## Result and scope

[K2568](k2568-cauchy-preparation-bandwidth-2026-11-05.md) proves unstable continuation of the actual selected homogeneous fields and exhibits one smooth compact conserved detector that sees that instability. It explicitly leaves other detectors open. Here the exact response sequence of ANY specified compact conserved detector gives a necessary and sufficient continuity criterion. On an analytic preparation ball, its exact deterministic-noise minimax error is the support function of the intersection of two stated balls. A bounded scalar readout is uniformly recoverable as the noise vanishes, including at a radius where the complete endpoint field has no uniformly consistent recovery.

This distinction is realized by actual compact conserved tests, not only an abstract sequence model. A nonnegative smooth radial cutoff and exponentially weighted angular harmonics give a sharp preparation threshold fixed by their support and angular smoothing. At equality the scalar readout is recoverable. An executed two-mode conserved-detector consumer has exact minimax error317/100 at the supplied noise/prior bounds, and the general finite-head certificate converges with a certified tail.

All results concern the K2568 family and additive changes to the same localized-source response. They do not select a physical detector, source boundary condition, prior, positive physical energy, causal domain or observed four-dimensional pullback. A readout extension can exist on coefficients for which no complete distributional field on the full tube has been constructed; this is an operational extension from finite solutions, not a field-existence theorem. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS at their actual source scope; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8 retain their native action, domain, observation and physical-quotient debts. No source polarity, physics mapping, canon, novelty or GU verdict changes.

## 1. Actual readout coefficients, with the observation fixed first

Keep K2568's real normalized omega harmonics H_(n-1), n>=1, and complete fields h_n, Q_n, e2_n on the common tube. The zero-normal-derivative scalar amplitudes satisfy v_n(t0)=1 and

    E h_n = C_E v_n(t) H_(n-1)(omega) R(1),
    C_E = -(rE/2)(mu-5K) != 0,
    c_- exp(n d(t)) <= v_n(t) <= c_+ exp(n d(t)),
    d(t)=log[tanh(t/2)/tanh(t0/2)].                 (1)

On any fixed closed subannulus the positive constants can be chosen uniformly in n and t. This is K2568's actual curved-operator estimate, not an exponential substitute for the operator. Its constants are loose but its exponent is exact.

Fix one real smooth compact conserved test F and define q_n=<F,h_n>. For finite-support coefficient vectors a the exact additional reading is

    ell_F(a)=sum q_n a_n.                          (2)

The source response's known baseline can be subtracted; the uncertainty analyzed here is its homogeneous addition. No q is fitted after seeing a or its noisy data. For F=E W, formal self-adjointness and Bianchi give div F=0 and q_n=<W,E h_n>. Compact support removes boundary terms. E annihilates metric gauge, so these readouts are insensitive to adding metric gauge to h_n.

## 2. Necessary and sufficient preparation criterion

Supply the auxiliary preparation norm

    ||a||_(rho,s)^2 = sum n^(2s) exp(2rho n) a_n^2,
    rho>=0, s real.

The finite-solution reading(2) extends continuously to its Hilbert completion EXACTLY when

    Q_(rho,s)^2 = sum q_n^2 n^(-2s) exp(-2rho n) < infinity. (3)

Its norm is Q_(rho,s). Weighted Cauchy-Schwarz proves sufficiency. For necessity, choose the first N coefficients proportional to q_n n^(-2s) exp(-2rho n) and normalize their preparation norm to1; the reading is the square root of the partial sum in(3). This also shows why inspecting only individual q_n bounds is insufficient at an equality threshold: square summability, not just a supremum, is required for a scalar functional.

In particular one finite Sobolev norm controls the readout iff q has at most polynomial growth. If q is polynomially bounded, choose s larger than that degree plus1/2; conversely(3) with rho=0 bounds each q_n by Q n^s. Thus continuity on the smooth rapidly decaying coefficient space is equivalent to polynomial growth. Normalized harmonic derivatives grow polynomially, so every rapidly decaying sequence defines smooth angular input; this statement uses the selected harmonic subspace, not arbitrary boundary jets or other solution families.

## 3. Executed actual-detector construction and sharp threshold

Choose t0<ta<tb<t1 with the closed slab disjoint from the B source point, and a nonzero nonnegative smooth cutoff chi with compact support in(ta,tb), whose support has supremum t*. Select compact A tensor W_A so that its integrated pairing with C_E R(1) is positive. This is possible by nondegeneracy and the nonzero original tensor, as in K2568. Use constant theta dependence and

    g_sigma(omega)=sum exp(-sigma n) H_(n-1)(omega), sigma>0,
    W=chi(t)g_sigma(omega)W_A, F=E W.              (4)

Exponential coefficients dominate every polynomial harmonic derivative, so W and F are smooth and compact on the stated tube. After absorbing positive volume and A factors into the radial weight, the ACTUAL coefficients are

    q_n=exp(-sigma n) I_n,
    I_n=integral f(x) v_n(t(x)) dx > 0,
    x=d(t), b=d(t*)>0, f>=0 smooth compact,
    sup supp f=b.                                 (5)

The cutoff is fixed for every n. Equation(1) gives

    lim_(n->infinity) log(I_n)/n=b.                (6)

For the upper bound use x<=b. For any epsilon>0, positivity supplies a fixed interval with f>0 and x>b-epsilon; the lower comparison in(1) proves liminf>=b-epsilon. Let epsilon decrease to0. No Laplace asymptotic expansion is needed.

There is also crucial endpoint information absent from(6). Smooth compact f is flat at b, so for every integer M>=0, f(x)<=C_M(b-x)^M. Therefore

    I_n <= C'_M exp(bn) integral_0^infinity u^M exp(-nu)du
        = C'_M M! exp(bn) / n^(M+1).              (7)

Constants depend on the fixed cutoff and comparison bound. This is an exact upper estimate, not a claimed asymptotic equivalence. Equations(3),(6),(7) prove, for every fixed real s and rho>=0,

    ell_F is bounded on H_(rho,s) iff rho>=b-sigma, (8)

where a negative right-hand side means every allowed rho qualifies. If rho<b-sigma, the weighted q_n grow exponentially and(3) fails. At equality(7) gives arbitrarily high inverse powers, hence square summability even for negative s. If b>sigma, this smooth compact detector is discontinuous on smooth Cauchy data but bounded on the critical analytic preparation space. If sigma>=b, it is already bounded on every finite Sobolev input space in this selected subspace. Smoothness of F alone neither guarantees stability nor proves instability.

The threshold is tied to an actual detector's radial support and angular coefficients. It does not identify that detector with a source-selected observation. Changes of cutoff, noise model, preparation or harmonic family require their own coefficients. The Bianchi construction supplies conservation; it does not supply physical coupling or positivity.

## 4. Exact worst-case noisy recovery, without a factor-two gap

For clarity take s=0 and w_n=exp(rho n), rho>=0. Suppose(3) holds. Supply ||Wa||_2<=R, R>0, and observe the complete near-amplitude data z=a+e with ||e||_2<=delta. Noise is deterministic; no probability law is assumed. The quantity of interest is the extended scalar ell_F(a), not the complete endpoint field. Define

    Omega(delta,R)=sup{ |ell_F(a)| : ||a||_2<=delta, ||Wa||_2<=R }. (9)

The exact minimax absolute error, over all possibly nonlinear scalar estimators of z and all allowed a,e, equals Omega.

For the lower bound, any a in(9) and -a can both produce z=0 with noise -a and a. At least one error is at least |ell_F(a)|; take the supremum. For the upper bound, at each feasible z consider the bounded scalar range of ell_F over K_z={a:||Wa||<=R, ||a-z||<=delta}. Choose the midpoint of its infimum and supremum. For any a1,a2 in K_z their half-difference belongs to both balls in(9), so the range diameter is at most2Omega. The midpoint has error at most Omega. Infima and suprema need not be attained; their midpoint still exists. Assign any value on infeasible z, which the experiment cannot produce. This proves the identity directly and does not claim an efficient algorithm for arbitrary infinite data.

A usable cutoff estimator is ell_N(z)=sum_(n<=N) q_n z_n. Its guaranteed error is

    delta ||q_(<=N)||_2 + R ||W^-1 q_(>N)||_2.    (10)

The second term tends to0 by(3); with N fixed the first tends to0. Consequently Omega(delta,R)->0 as delta->0 for EVERY scalar functional satisfying(3), including rho=b-sigma in(8) and rho=d(t1) for any such readout at the complete-field critical radius. This does not contradict K2568: its complete endpoint multiplier is noncompact at that radius, while one bounded scalar functional has square-summable weighted tails.

Conversely if(3) fails, for any delta>0 the supremum in(9), initially over finite sums, is infinite. For rho>0 choose a sufficiently high tail so R exp(-rho N)<=delta; within that tail the divergent weighted q norm makes the reading unbounded while preserving both constraints. For rho=0 the two balls reduce to the ball of radius min(delta,R), and the same truncated dual-vector argument applies. Thus no finite worst-case scalar recovery exists for an unbounded specified readout under these assumptions.

This is an elementary specialization of classical optimal-recovery geometry; [Donoho, Statistical Estimation and Optimal Recovery, 1994](https://web.stanford.edu/dept/statistics/cgi-bin/donoho/wp-content/uploads/2018/08/SEOR.pdf) supplies related context. The proof above is self-contained and concerns bounded deterministic noise, not the paper's Gaussian statistical problem or a novelty assertion.

## 5. Executed finite certificates and an actual conserved two-mode consumer

Let Omega_N be(9) restricted to the first N coordinates. Projection preserves both norms, giving the rigorous enclosure

    Omega_N <= Omega <= Omega_N + R ||W^-1 q_(>N)||_2. (11)

Any certified upper bound on the weighted tail makes this a convergent finite procedure. A finite lower bound comes from any feasible vector. For any alpha,beta>=0 with alpha+beta w_n^2>0, weighted Cauchy-Schwarz gives the finite upper bound

    Omega_N^2 <= (alpha delta^2+beta R^2)
                   sum_(n<=N) q_n^2/(alpha+beta w_n^2). (12)

Only this sufficient dual certificate is needed here; no unproved interchange of infinite optimization and limits is invoked.

To realize an exact finite fixture with the original fields, choose one fixed positive radial cutoff as above. Its first two I_n are positive. Replace g_sigma in(4) by the FINITE harmonic combination

    g=(q_1/I_1) H_0 + (q_2/I_2) H_1.

Harmonic orthogonality makes the conserved F=E W have precisely the desired q_1,q_2 and zero response to all other selected harmonics. The normalization integrals are exact definitions, not fitted observations or claimed rational ODE integrals. Select

    w=(2,4), rho=log2,
    a*=(3/10,2/5), delta=1/2, R^2=73/25,
    q=(3/2,34/5)=(I+W^2)a*.

Both constraints are active, and

    q dot a*=317/100=delta^2+R^2,
    sum q_n^2/(1+w_n^2)=317/100.

The feasible vector and alpha=beta=1 certificate(12) agree, so the EXACT minimax error is317/100 for this supplied, realized scalar observation. The same zero datum with truths a* and -a* provides the lower bound. This example also has an explicit optimal LINEAR estimator, avoiding any infinite feasible-set search:

    estimator(z)=(3/10)z_1+(2/5)z_2.

Its noise error is at most delta ||a*||=delta^2, while its bias over the preparation ball is at most R ||W^-1(q-a*)||=R ||Wa*||=R^2 because q-a*=W^2 a*. Their sum is317/100, matching the indistinguishable-input lower bound. At truth a* with noise -a*, both contributions have the same error sign and the bound is attained. Other coordinates are ignored. Omitting either preparation or noise constraint strictly enlarges this example's radius; the exact probe checks both counterclaims. There is no claim that these large rational units are an empirical precision target.

For an independent tail-calculation check, the explicitly labeled sequence consumer q_n=(3/2)^n/n^2 and w_n=(3/2)^n has weighted tail squared sum_(n>N)n^-4<=1/(3N^3). It is a supporting sequence fixture, NOT an asserted closed form for the curved detector integrals(5). Equation(11) then gives error at most R/sqrt(3N^3) beyond the finite optimization. The actual compact detector has its own tail constants from(7).

## Evidence, contrary routes and next condition

Universal weighted-duality, compact-detector threshold and minimax statements use the written proofs. Exact finite algebra, harmonic identities, realized finite-mode consumer and sequence-tail identities are supporting calculations. Predecessor content hashes pin the actual equation/field and finite-detector construction. Report comparison and content pins are provenance checks, not independent proofs. Required independent internal mathematical and hostile review remains a separate acceptance step; no external-expert, proof-assistant, remote-CI or physical certification is claimed.

The strongest contrary routes are preserved: a sufficiently smoothed detector is stable despite growing fields; an insufficiently smoothed detector remains unbounded despite being smooth and conserved; an analytic prior can define a readout without constructing its whole field; and full-field critical-radius noisy failure cannot be transferred to a scalar readout. A boundary-prepared family from K2568 section6 remains a different admissible mathematical repair.

Next obtain an independently justified detector, preparation bound and noise tolerance, then compute or certify ITS response sequence and tail using(3),(9),(11). Alternatively construct an observation map on a larger solution family and test whether this selected-subspace continuity survives. Choosing a convenient detector or repeating a generic boundary instability is not physical selection. The local source-existence and finite-calibration results remain intact.

[K2566](k2566-finite-observation-preparation-2026-11-05.md), [K2568](k2568-cauchy-preparation-bandwidth-2026-11-05.md), [exact probe](../../tests/channel-swings/k2570_detector_recovery_probe.py), [report](../../lab/process/k2570-detector-recovery.json).
