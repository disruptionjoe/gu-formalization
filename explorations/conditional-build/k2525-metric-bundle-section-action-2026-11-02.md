---
title: "K2525 Stationary metric-bundle section: full Fourier response and variation boundary"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-ambient section-action mathematics; no native I1 stationary solution or physical propagator
scripts:
  - tests/channel-swings/k2525_metric_bundle_section_action_probe.py
---

# K2525 Full response of the stationary metric-bundle section

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
result: K2525
carrier: literal sections x maps to (x,y(x)) of the fixed coordinate-horizontal K2345 metric bundle, y of inertia(1,3) LAYER=toy CHIRALITY=N/A
pairing: induced observer density and signed vertical DeWitt form ON=declared_carrier
real_structure: real section tensors with vertical inertia(6,4) and total inertia(7,7)
grading: section variation, independent ambient metric variation and source I1 translation are distinct
action_owner: repository-construction -- fixed-ambient alpha normII squared plus beta normH squared section action
target: complete constant-section Fourier Hessian, characteristic degeneracy and receiver inference boundary MAP-TYPE=evaluation
```

## Result, reuse and scope

[K2523](k2523-coupled-receiver-variation-2026-11-02.md) excludes uncancelled bending coefficients at a free receiver when arbitrary ambient normal metric jets are varied. That hypothesis cannot be transferred to a fixed metric-bundle section action. The contrary stationary section and beta=2alpha ratio were ALREADY obtained in [W136](../W136-issuance-declaration-propagation-2026-07-14.md); we reuse them. [W130](../W130-native-graviton-oneloop-block-2026-07-14.md) already found a longitudinal residue for its pure-II action. Neither historical ratio nor absence of gauge covariance is claimed new.

The present result computes the FULL ten-component constant-coefficient Fourier quadratic for the beta=2alpha fixed-ambient section action, including lower derivative terms, its exact degeneracy shells and its failure to carry the intrinsic Einstein gauge quotient. It therefore provides a concrete stationary free-receiver counterroute to the attempted variation transfer, while showing why stationarity plus receiver rank still does not supply the desired Einstein/matter-light response.

SC-GEO-03, SC-ACT-01 and SC-GEO-55 ASSERTS their native metric/action/displacement roles; this coordinate-horizontal continuation and section-only action are repository constructions. SC-META-53 remains UNCERTAIN; LT-GR6b/GR10/GR11 and ledger0.263 do not move. K2345's nonzero selected T=0 translation Euler remains unchanged. W154's larger K95 composite does not gain K77 action ownership; its [later qualification](w154-w229-k77-action-owner-qualification-2026-08-24.md) remains binding. No full native stationarity, physical particle poles, ghosts, tachyon, positivity, common causal domain, or novelty certification is inferred here.

## 1. Exact geometric object and prior stationary section

Use the literal fixed ambient metric of [K2345](k2345-curved-bundle-ricci-obstruction-2026-10-30.md):

    G=diag(y,V_y),
    V_y(A,B)=tr(y^-1 A y^-1 B)-tr(y^-1 A)tr(y^-1 B)/2.

A section is s(x)=(x,y(x)); its actual induced metric is

    gamma_ij=y_ij+V_y(partial_i y,partial_j y).

Choose the induced density mu_gamma and unnormalized mean curvature Hmean=tr_gamma II. Our action is S=(1/2) integral[alpha||II||²+beta||Hmean||²]mu_gamma, with G FIXED, y the varied section, and compactly supported variations. This is not an intrinsic action S_X(gamma) and not the full I1 action.

At y=g=diag(1,-1,-1,-1), all section derivatives vanish. In the standard symmetric-coordinate basis E_A,

    Z_ij^A=II_ij^A=-(1/2)(V^-1)^(AB)(E_B)_ij,
    L(n)_ij=-2 V(Z_ij,n)=n_ij,
    ||II||²=2, ||Hmean||²=-1.                       (1)

The normal receiver is exactly the identity, rank10. The flat constant density is (alpha-beta/2)sqrt(|det y|). At a constant section all Euler terms obtained by differentiating coefficients with respect to x vanish; the complete remaining section covector normalized by mu_y is (2alpha-beta)y^-1/4; its coordinate Euler density includes sqrt(|det y|). Thus beta=2alpha makes every constant Lorentz section stationary. This re-establishes applicability of the W136 result to the explicitly typed K2345 carrier, not a new discovery of the ratio.

K2523 instead varies G through tensors vanishing on the section but with arbitrary normal jets. Those independent G variations are absent here. The section itself moves through a fixed G; its value, derivatives and induced metric are linked. A nonzero stationary section is therefore no contradiction. Conversely, adding independent G variation to this model restores the K2523 normal-jet obstruction. A native relation G(g,s) would need its own full chain rule, not an interpolation between these two variation spaces.

## 2. Full Fourier quadratic at beta=2alpha

Set y(x)=g+epsilon H cos(k_i x^i), for real constant symmetric H and covector k. The local expansion is around a nondegenerate section; use spatial/periodic phase averaging as an algebraic Fourier convention, not a boundary or causal prescription. Define

    w=k^T g^-1 k, a=tr(g^-1 H), d=tr(g^-1 H g^-1 H),
    b=k^T g^-1 H g^-1 k, c=k^T g^-1 H g^-1 H g^-1 k,
    v=d-a²/2.

The phase-averaged epsilon² coefficient of the ACTION DENSITY is alpha Q(H,k)/4, where

    Q=3 w²(d-a²/2)+a b/2-w d/4+w a²/2.             (2)

The conventional Fourier Hessian differs only by the stated common normalization; its zeros and ranks below use Q. Formula(2) includes all derivative orders at this constant stationary background. There is no zeroth-order term: the constant-section family is stationary with identically zero density at this coefficient ratio.

Here is an explicit expansion sufficient to reproduce the formula without an EFT replacement. At phase cos=1, sin=0, write Y=g+epsilon H and q_ij=-epsilon k_i k_j H. The vertical second fundamental form is Z_Y+q. The exact norms at that point are

    normII²=2+epsilon k^T Y^-1 H Y^-1 k
                   +epsilon²(k^T Y^-1 k)² V_Y(H,H),
    normHmean²=-1+epsilon(k^T Y^-1 k)tr(Y^-1 H)
                   +epsilon²(k^T Y^-1 k)² V_Y(H,H).

Multiplying by sqrt(-det Y) and by alpha/2 gives the phase-zero epsilon² coefficient

    alpha/2[-2c-3ab/2-2wd+wa²+3w²v].               (3)

At the quadrature phase, Y=g, p_i=epsilon k_i H, q_ij=0. Use the ambient connection acceleration and subtract its tangent projection in the norm. Its two norm coefficients before density are

    (normII²)_2 = 2c-5wd/4+wa²/2,
    (normHmean²)_2 = 3wd/2+ab-wa²/2.

The baseline combination 2+2(-1) vanishes, so the order-two density correction drops out here. The action coefficient is

    alpha/2[2c+2ab+7wd/4-wa²/2].                   (4)

Averaging(3)-(4) cancels c and gives(2). The probe constructs Z from the metric inverse, uses the actual normal projection and induced inverse correction at the quadrature phase, and checks mixed polarizations. This is not a scalar-curvature surrogate. The written tensor expansion proves arbitrary H,k; exact fixtures challenge the implementation and signs.

Equivalently define C=3w²-w/4, D=-3w²/2+w/2. The symmetric bilinear form is

    Q(H,J)=C tr(g^-1 H g^-1 J)+D tr(g^-1 H)tr(g^-1 J)
                  +[a_H b_J+a_J b_H]/4.            (5)

This defines the entire ten-by-ten matrix in any symmetric basis.

## 3. Released exact degeneracy classification

For w nonzero, decompose symmetric tensors relative to k into transverse traceless5, mixed vector3, and scalar2. The first two blocks are C times their nondegenerate trace form. In a timelike rest frame, scalar coordinates x=H00 and y=H11+H22+H33 give

    Q_scalar=w (x,y) M(w) (x,y)^T,
    M=[[3w/2+3/4,3w/2-3/4],
       [3w/2-3/4,-w/2+5/12]],
    det M=-3w²+5w/2-1/4.                           (6)

The tensor decomposition and polynomial identity extend the non-null rank conclusion to spacelike k; the transverse signatures change, not the root polynomial. Up to a nonzero basis constant the full determinant is

    w^10 (12w-1)^8 (12w²-10w+1).                  (7)

For nonzero real k the exact kernel dimensions are:

| Covector | Kernel dimension |
|---|---:|
| w nonzero off the three listed shells | 0 |
| w=1/12 | 8 |
| w=(5-sqrt(13))/12 or (5+sqrt(13))/12 | 1 |
| w=0, k nonzero | 8 |
| k=0 | 10 |

At null nonzero k one must use(5) directly: Q=ab/2 has rank2 because trace a and null contraction b are independent. Substituting w=0 into a rest-frame decomposition is invalid and would incorrectly report rank0. The massive-looking shells in(7) are FORMAL Fourier degeneracies of this fixed-ambient action, not particle masses or accepted physical modes. No gauge quotient, positive energy or chosen Green prescription has been constructed.

## 4. Principal symbol and the intrinsic-response obstruction

Before setting beta=2alpha, the highest derivative section Hessian is

    sigma4(k)=(alpha+beta) w² V_g.                  (8)

This follows from delta II_ij=partial_i partial_j h at highest order, and delta Hmean=Box_g h; the actual signed contraction gives the same w² V_g in both terms. Lower-order connections and density cannot alter this principal symbol. At beta=2alpha nonzero, it is 3alpha w² V_g, nondegenerate for non-null k, with inertia(6,4) when alpha>0.

At this constant background and alpha nonzero, this excludes a nonzero finite-order local LINEARIZED gauge generator acting only on the section: if H_section R=0 as differential operators, the top symbols obey sigma4(k) sigma_R(k)=0; invertibility on an open set forces the polynomial sigma_R to vanish, contradicting its top order. Repeat after dropping that order. This does not exclude a nonlinear symmetry whose linearization vanishes at this background. A section perturbation k_i v_j+k_j v_i is generically not a kernel direction. Base-coordinate transport would also transform G; it is outside this fixed-G field space. Hence the intrinsic Einstein gauge quotient and the response factorization for an intrinsic S_X(gamma) in K2523 cannot be imported merely from L=Id and section stationarity.

There is also a complete coefficient-class consequence within the UNSUBTRACTED TWO-TERM ACTION: flat stationarity requires beta=2alpha, while cancellation of the fourth-order principal part requires beta=-alpha. Their only intersection is alpha=beta=0. A cosmological subtraction, extra curvature term, coupled ambient variation or a different metric lift changes the class and must be evaluated separately. Indefinite principal pairing is not, by itself, a physical ghost verdict.

## 5. Executed static common-domain source/readout consumer

The full operator permits a concrete conditional matter/light test. Supply the conventional weak metric source coupling and minimally coupled clock/particle/photon probes explicitly; these are imported, not inferred from I1. At linear order delta gamma=h. In the normalization of Q let the static Fourier source be J00=rho(k), all other components zero. It is a prescribed linearized external source, conserved because k0=0; no nonlinear self-supported matter equilibrium is asserted. Fix k=(0,0,0,p), v=p²>0, and solve the FULL ten-component equation M(k) h=J. No variable or contact term is dropped. Put D(v)=v(12v+1)(12v²+10v+1). For a unit source:

    A0=h00=3(8v²+10v+1)/D(v),
    Ap=h11=h22=(4v+1)(6v+1)/D(v),
    Al=h33=(2v+1)/[v(12v²+10v+1)],
    off-diagonal entries=0.                         (9)

An overall nonzero action/source normalization rescales these entries and cancels in the ratio. The static geodesic acceleration is -partial_i h00/2. The first null/eikonal metric variation along a fixed unperturbed spatial unit direction e is proportional to h00+e^i h_ij e^j. Define equally normalized LOCAL metric readouts r_motion=h00 and r_light=h00+e^i h_ij e^j. The isotropic Einstein benchmark has r_light=2 r_motion under these definitions. These readouts are ingredients in motion/light propagation, not an already integrated deflection or time-delay measurement.

For a transverse ray, e perpendicular k, the exact Fourier ratio is

    r_light/r_motion=4(12v²+10v+1)/[3(8v²+10v+1)],
    r_light-2r_motion=-2(10v+1)/D(v).                (10)

It tends to4/3 as v→0+ and to2 as v→infinity, but is strictly below2 at every finite v>0. These are Fourier multiplier limits, not pointwise real-space potential ratios, measured PPN parameters or observational exclusions. The wavelength is in the declared metric's units; no physical ruler is selected.

Rotation gives h_ij=rho[Ap delta_ij+(Al-Ap)n_i n_j], n=k/|k| and Al-Ap=4v/D. Consequently for ONE FIXED e and every nonzero spatial k,

    (r_light-2r_motion)/rho=[-20v-2+4v(n dot e)²]/D < 0.   (11)

This avoids treating the measure-zero plane k dot e=0 as the support of a three-dimensional smooth source. Longitudinal h33 is retained. A physical ray integral must still use its actual propagation and boundary conditions.

### Static domain and explicit Green kernel

First take rho in C_c^infinity of a Fourier annulus 0<p_min<=|k|<=p_max, with rho(-k)=conjugate(rho(k)). All multipliers are smooth there; Fourier inversion gives real Schwartz fields and a common source/readout domain satisfying the complete static equations. The response difference for any nonzero rho cannot vanish identically because(11) never vanishes. Such annular sources need not have positive density and are linear perturbation sources.

The construction also extends to smooth compactly supported REAL-SPACE sources, without an imposed zero total mass. Near k=0 the full tensor multipliers are O(1/|k|²), locally integrable in three dimensions; at infinity they are bounded and decay. After multiplication by the Schwartz transform of rho, all field multipliers are integrable; Fourier inversion and the Riemann-Lebesgue lemma give continuous decaying fields. Polynomially weighted integrability gives smoothness, and they define tempered solutions. The equation holds distributionally because the full symbol identity holds almost everywhere and all products are locally integrable. Select the decaying solution; any tempered homogeneous difference has Fourier support only at k=0 because the symbol is invertible elsewhere, hence is a polynomial in position space and cannot decay. This is a static uniqueness statement in the specified class, not a causal Green theorem.

For example define a=(5-sqrt(13))/12 and b=(5+sqrt(13))/12, both positive. The actual h00 multiplier has exact partial fractions

    A0(v)=3/v-(8/3)/(v+1/12)
          +(-1/6-7sqrt(13)/78)/(v+a)
          +(-1/6+7sqrt(13)/78)/(v+b).               (12)

With Fourier convention inverse(1/(|k|²+m²))=exp(-m R)/(4pi R), equation(12) is an explicit Coulomb/Yukawa Green kernel convolved with the same rho. Each radial kernel solves (-Delta+m²)K=delta distributionally, from the radial equation away from0 and unit flux at0. Thus the physical-space solution decays, generally as1/R; it is not generally Schwartz. The full spatial tensor retains the longitudinal projector, not merely this scalar kernel. The transverse light multiplier simplifies to4[1/v-1/(v+1/12)]. Signs of these coefficients are not a Hamiltonian/ghost diagnosis.

This is a genuine supplied static source/readout response of the derived section action. It fails the GR-like equality on one common domain with the same conserved source. Changing the coupling, readout, action or boundary prescription defines another candidate; no native GU claim is excluded.

## What this closes and what remains

We have a concrete stationary rank-ten fixed-bundle section, an explicit full response symbol, and exact limits on its transfer to Einstein or native GU dynamics. This consumes older structural results and eliminates the proposed shortcut from receiver rank to physical response. The missing full native I1 stationary distortion/section packet, coupled variation and common analytic source/readout domain remain. The executed static inverse and Coulomb/Yukawa kernel give a conditional common-domain response and a nonzero same-source light/motion mismatch. Causal evolution and actual native coupling still require new work; this static inverse cannot repair K2345's independent translation Euler. No source/ledger/canon verdict changes.
