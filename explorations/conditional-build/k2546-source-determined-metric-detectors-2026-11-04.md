---
title: "K2546 Source-determined metric filters and the surviving Weyl channel"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional compact filtered observations; no general metric inverse, physical detector or native GU claim
scripts:
  - tests/channel-swings/k2546_source_determined_metric_detectors_probe.py
---

# K2546 Which observation survives homogeneous ambiguity?

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
result: K2546
carrier: original ambient metric and displacement on the stationary Einstein product; compact smooth detector covectors LAYER=toy CHIRALITY=N/A
pairing: distribution/test duality with invariant volume; positive chart norm only for error estimates ON=declared_carrier
real_structure: real nonzero kappa, product signature (7,7), local smooth fields and distributions
grading: original h, shifted z, symmetric C and skew partner remain distinct
action_owner: repository-construction -- selected I1 completion inherited from K2537
target: source-only filtered observations and exact retained Weyl coupling MAP-TYPE=evaluation
```

## Result and inference boundary

The exact curved tensor sector of [K2544](k2544-constrained-tensor-response-2026-11-04.md) admits a nonempty class of finite **metric-only filtered observations** determined by its source without choosing homogeneous data. The minimal constant-coefficient polynomial in the sector wave operator has degree two. Its source-disjoint value is zero: this construction extracts contact information, not a boundary-free long-range response.

For the actual localized source, full trace elimination retains a Weyl-displacement channel. We prove that no nonzero compact scalar filter annihilates that channel on this product, and give the resulting joint detector; the tensor-sector filter cannot be exported as a metric-only identity for that source. A general adjoint criterion states the remaining construction problem without claiming a closed-range theorem or a global inverse. These conclusions advance the observation demand while preserving K2543/K2544's response ambiguity.

SC-ACT-01 ASSERTS the first-order action, SC-GEO-55 ASSERTS gauge-rotated-Levi-Civita displacement, SC-GEO-03 ASSERTS Met(X), and SC-META-53 remains UNCERTAIN about indefinite spectra. The independent metric and selected completion here are conditional repository objects. Ledger0.263 GR6b/10/11 and source polarities are unchanged. No physical detector, native metric-on-metrics realization, global existence, positivity or novelty claim follows.

## 1. An exact criterion before selecting a Green operator

Let a linear field system be P x=f on a declared distribution space and suppose its solution set is nonempty. For a compact smooth test covector l, the number <x,l> is independent of the solution if and only if

    <y,l>=0 for every homogeneous solution y in ker P.       (1)

Proof: any two solutions differ by y, and x+y is a solution for each allowed y. If a compact smooth test vector q satisfies P* q=l, formal integration by parts gives <x,l>=<f,q>. This is a sufficient constructive test. We assert no converse representation by compact q: the annihilator/range equality depends on topology, supports and closed range, none supplied by a symbol calculation.

For a coupled system x=(h,C,K,...), a sufficient compact-adjoint construction for a metric-only test requires

    P* q=(l_h,0,0,...).                                     (2)

Formal self-adjointness of an action is not a solution to (2). Gauge invariance alone is also insufficient: K2544 gives full homogeneous, gauge-invariant tensor response at fixed source. In a domain restricted by boundary data, ker P changes; (1) must be recomputed on that domain. The compact support of q removes boundary terms, not homogeneous solutions by fiat. If no solution exists, the equality is only a necessary on-shell identity, not a prediction.

## 2. Execute the criterion on the curved TT sector

Use exactly K2544's nonzero curved tensor T=Hess_A f+Kf G_A, with Box_A f=-7Kf. Put D=Box_B, k=kappa!=0, and

    a0=-5k/2288,
    e=175k²/3624192,
    mu=611557655k²/39953092608,
    c=970112/(13395k),
    (D+e)v=J/(6a0), c(D+mu)u=-J/(6a0),
    h=H T, H=v-u/(6a0).

All full equations, including the skew/mixed rows, are already checked for this source class j=J(B)T. No new componentwise inversion is used. Define

    L(D)=(D+e)(D+mu),
    N(D)=429D/(106k)-70547k/60632.

Elimination of u,v yields LH=NJ for every sector solution. Thus for every compact smooth scalar phi on B,

    O_phi=<H,L phi>=<J,N phi>.                              (3)

D and its real constant polynomials are formally self-adjoint with the invariant B volume. Every distribution H acts on Lphi; (3) is finite at fixed phi. On a product chart with T nonzero, choose a compact dual tensor on A normalized to pair to one with T. This realizes <H,Lphi> as a metric test within the sector. This normalization uses a nonzero component, not an indefinite norm. It is a restricted-sector observable, not a claim that this raw tensor test is invariant under every full-system gauge transformation or valid after leaving the sector. H also has a gauge-invariant extraction through E h after the corresponding operator factors are included, as in section4 below.

Both homogeneous sectors occur: H=v for (D+e)v=0, and H=-u/(6a0) for (D+mu)u=0. Nonzero local eigen-germs exist by K2544's analytic construction. If a polynomial p(D) annihilates every such H, then p(-e)=p(-mu)=0. Since e!=mu, L divides p. Conversely L annihilates both sectors. This proves minimality among constant-coefficient polynomials in D, not among all covectors, nonlocal operators or boundary prescriptions.

The identity is nonempty without invoking local solvability on a chart that might be smaller than the detector support. On the whole chosen product chart take J=J0!=0 constant, r=1/(6a0), v=rJ0/e and u=-rJ0/(c mu). These constant amplitudes solve both forced factors everywhere in the chart. Choose compact phi inside it with nonzero integral. Since integral Dphi=0,

    <H,Lphi>=-70547k J0 integral(phi)/60632 !=0.

The gauge-invariant observation in (6) is minus one half this value, also nonzero. The source is not asserted compact in all coordinates; compactness belongs to the detector. There is no positive-definite action or physical energy premise.

## 3. Contact information, error cost and a contrary construction

Locality gives supp(Nphi) subset supp(phi). If supp(phi) is disjoint from supp(J), O_phi=0. This is precisely why annihilating all freely addable homogeneous modes does not recover a nonzero source-disjoint force signal. It does not prove that every invariant observable is contact-supported, or rule out a specified boundary-dependent gravitational response. The full solution space and allowed observation class matter.

In any fixed relatively compact chart choose an auxiliary positive component norm. If a reconstruction error eta in H is bounded by epsilon in L2, then

    |<eta,Lphi>| <= epsilon ||Lphi||_2.                     (4)

This is a mathematical conditioning bound, not an observed noise model. In normal coordinates on seven-dimensional B use a fixed smooth compact profile with D0²phi nonzero and invariant-volume normalization phi_delta=delta^-7 phi(x/delta)/w(x). Smooth coefficient expansion gives

    ||Lphi_delta||_2 = Theta(delta^(-15/2)),
    ||Nphi_delta||_2 = Theta(delta^(-11/2))                  (5)

as delta->0. The leading rescaled operators are D0² and [429/(106k)]D0. For a nonzero compact profile these principal images cannot vanish identically: Fourier transformation of the frozen constant-coefficient operator multiplies an entire transform by a nonzero polynomial; its vanishing forces the profile to be zero. Lower-order masses and density terms do not cancel the leading norm. Constants depend on k, chart and profile. This is the positive auxiliary norm, not the indefinite physical pairing. A smooth fixed source can give a finite contact limit while the error amplification diverges; a delta source has separate contact scaling. No universal signal-to-noise claim or pointwise metric pullback follows.

A contrary control is either homogeneous pole: a first-order factor kills one and retains the other. Choosing only D+e therefore leaves source-independent u information. Erasing the source numerator N also fails on the constant source example. These are altered mathematical objects, not flips of report flags.

## 4. A gauge-invariant implementation inside the TT sector

K2544's Einstein linearization is E(H T)=-(D+e)H T/2. For compact W on the product, <h,E W>=<E h,W> is invariant under linearized diffeomorphisms. Take W=psi_A tensor [(D+mu)phi] with compact A tensor psi_A paired to T with integral one. Then

    <h,E W>=-<H,(D+e)(D+mu)phi>/2
            =-<J,Nphi>/2.                                 (6)

The first equality follows by evaluating E h on the actual TT sector, not by assuming E preserves arbitrary separable test tensors. Formal self-adjointness moves E to h; this avoids missing A derivatives of the compact test. Thus the filtered source contact has a full gauge-invariant test representative and retains both pole cancellations. Applying (6) to an arbitrary radial-pressure source still requires its actual full field identity, which is not the TT identity.

## 5. Follow through to the actual conserved source: retain Weyl

For any full solution with conserved j on the Einstein product define t=tr j, tau=tr C, u=div div C-Box tau and W_C=div div(W C), where W is the product Weyl tensor. K2539 and K2543 give

    R_h=A tau-B t,
    u=q tau+r t,
    c0 u+k Box tau+(4/mH)W_C=0,
    A=41511k/1735888, B=34606/(29589k),
    q=(2515k/2820818)(5k/12),
    r=2515*1144/(2820818*15),
    c0=5082101k/4603456, mH=893k/858.

No source ansatz is used. With Q=k Box+c0 q, elimination produces

    Q R_h+(4A/mH)W_C=-B Q t-A c0 r t.                      (7)

For compact phi this is the source-determined JOINT probe

    <h,L_R* Q phi>+(4A/mH)<C,W* Hess phi>
          =-<t,(B Q+A c0 r)phi>,                           (8)
    L_R*chi=Hess chi-G Box chi-lambda G chi.

W* is the formal algebraic transpose relative to the inherited contraction. The two integrations in div div produce Hess phi with no sign change. All tests are smooth and compact; no inverse, boundary or wavefront pullback is used. R_h and C are invariant under linear diffeomorphisms at this constant-curvature-scalar, zero-displacement background. Equation(8) applies conditionally to the thin, partial-width and fully smoothed conserved sources of K2531/K2543, with their original trace convention t=(4A_epsilon+3P_epsilon)/2 tensor rho_B. It neither proves existence for those sources nor constructs a detector coupling to the C channel.

The residual is essential. For the off-shell curved field C=phi(B)G_A, K2539 gives W_C=-(7lambda/13)Box_B phi, generally nonzero. This is a control on the differential identity, not a conserved-source solution. The TT sector has W_C=0 because div C=tr C=0 and its curvature image is proportional to C; the general actual source has not been placed in that sector. Deleting W_C in (7) is therefore unjustified. This does not prove that no different combination of full equations can ever eliminate C; it identifies the exact unclosed channel of this attempted scalar route.

A physically defined scalar metric detector would need an independent bound or an equation/domain eliminating this Weyl pairing, or would need to admit the joint channel. Knowing t and the old trace identity alone supplies neither. A full inverse remains a distinct, stronger possible route. Repeating the TT calculation cannot resolve that missing input.

## 6. Execute the remaining scalar-filter repair and rule it out

Dividing (7) by k and reducing its rational constants gives

    (Box+f k²)R_h=-B Box t-g k t-(hW/k)W_C,
    f=127052525/309793516032,
    g=5082101/2234087856,
    hW=1618929/17615318.                                   (9)

The residual in the compact detector would disappear for every C if W*(Hess phi)=0. On this actual product W is self-adjoint and its full symmetric-tensor eigenspaces are:

| Space | Dimension | Eigenvalue |
|---|---:|---:|
| Total metric G |1|0|
| Relative volume G_A-G_B |1|14lambda/13|
| Both block-tracefree spaces |54|-7lambda/78|
| Mixed symmetric tensors |49|lambda/13|

These sum to105=dim Sym²(R14). They follow directly from Riem_A C=K[(tr_A C)G_A-C], the same B formula and zero mixed product curvature, subtracting the Einstein constant-curvature term lambda[(tr C)G-C]/13. Thus the kernel is exactly span G, even with indefinite signature.

If W Hess phi=0, Hess phi=chi G. On a connected product coordinate rectangle the mixed Hessian vanishes, so phi=f_A(A)+f_B(B). The A equation forces chi to be independent of B, and the B equation forces it independent of A. Hence chi is constant. Since Box phi=14chi, divergence of the Hessian equation gives 0=d Box phi+lambda dphi=lambda dphi. Nonzero lambda implies phi constant. A compactly supported constant on this open connected chart is zero.

Therefore **no nonzero compact scalar test eliminates the Weyl-displacement channel by this annihilation repair**. This is stronger than merely observing that the product is not conformally flat. It is a statement about the attempted full tensor identity for all C, not about the subspace of C selected by future boundary data. It does not rule out a different coupled adjoint solution, arbitrary tensor detectors, or a physical domain restricting the homogeneous solutions. The original joint contact identity remains valid for the actual source.

## 7. Full adjoint construction and inverse-free sector reconstruction

To make (2) concrete, use K2537 notation P for symmetric projection, E for the Einstein operator and L_Q for the complete reduced displacement operator. Its full equations are

    E z=-j/(12a0), L_Q Q=-P* j/(6a0),
    h=z-PQ/(6a0).

For compact symmetric psi and endomorphism chi, formal self-adjointness gives

    <h,E psi>+<Q,P*E psi/(6a0)+L_Q chi>
        =-<j,psi/(12a0)+P chi/(6a0)>.                      (10)

Thus L_Q chi=-P*E psi/(6a0) is an explicit sufficient compact-adjoint cancellation problem for metric-only observation. It keeps the full hook/vector/skew operator, not only its trace. Finding such a compact chi is not licensed by a pointwise inverse. Equation(10) identifies the actual remaining task after the failed scalar-filter repair.

Within the proved TT sector, the fourth-order equation is equivalent to both forced second-order equations. Let r=1/(6a0), alpha=429/(106k), Delta=mu-e. Given any H satisfying LH=NJ, set

    v=[(D+mu)H-alpha J]/Delta,
    u=[(D+e)H-alpha J]/(Delta r).                           (11)

Then H=v-ru, (D+e)v=rJ and c(D+mu)u=-rJ. Polynomial identities verify all three without a Green operator. Thus the source contact filter has not admitted spurious amplitudes through elimination. This reconstruction is sector-specific; it does not identify K2531's source with J(B)T(A).

## Evidence and next decision

The probe recomputes the two-pole numerator, both uncanceled single-factor controls, original trace elimination, retained-Weyl residual, adjoint coefficients and exact scaling exponents. Analytic support, distribution, gauge and scaling proofs are above; report hashes certify reproducibility, not those universal proofs. Independent internal review is required; no external certification is claimed. The adjoint-range principle is elementary linear duality, not a novelty assertion. A physical local measurement requires a coupling construction beyond these test functionals; compare the distinct quantum-field measurement problem in [Fewster and Verch](https://arxiv.org/abs/1810.06512), whose hypotheses are not imported here.

Next select a physically justified boundary/source-domain and a source-disjoint gauge-invariant readout, or construct the explicit full-system adjoint cancellation (2) for a proposed measurement. The current filters have exhausted their source-only contact payoff; changing them without that input cannot supply a long-range prediction.

[Probe](../../tests/channel-swings/k2546_source_determined_metric_detectors_probe.py), [report](../../lab/process/k2546-source-determined-metric-detectors.json), [full constraints](k2539-covariant-tensor-constraints-2026-11-04.md), [actual-source identity](k2543-localized-source-readout-2026-11-04.md).
