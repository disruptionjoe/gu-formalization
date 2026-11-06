---
title: "K2590 Tensor-pairing reciprocity and the complete boundary-aware detector adjoint"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full coupled TT response reciprocity and compact-detector adjoint for prescribed pressure sources; not reciprocity of every tensor source
scripts:
  - tests/channel-swings/k2590_boundary_aware_response_adjoint_probe.py
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
result: K2590
carrier: trace-controlled radial TT amplitudes and prescribed compact radial-pressure sources on the selected curved product LAYER=toy CHIRALITY=N/A
pairing: actual tensor contraction with invariant density; distinct scalar w2 and TT w5 coefficient densities ON=declared_carrier
real_structure: real order/conjugate-averaged inverse preparation from K2588
grading: source, TT amplitude, six scalar potentials, original metric and compact detector kept distinct
action_owner: repository-construction -- conditional curved-product completion
target: TT source-response reciprocity and full source-to-detector transpose MAP-TYPE=evaluation
```

# The actual tensor pairing resolves the TT reciprocity question

## Result, prior credit and scope

K2588 constructs symmetric scalar inverses but explicitly leaves tensor reciprocity open. The missing tensor Gram operator can now be computed exactly. It makes K2582's trace-tagged decomposition ORTHOGONAL in the actual TT tensor pairing, although it is not orthogonal in scalar L2(w5). The FULL original-metric TT source response is therefore reciprocal under K2588's real preparation, including the overlap trace channel and every angular mode.

A second result evaluates compact conserved detectors on the complete prescribed radial-pressure response: an explicit adjoint includes the cofactor transpose, distinct radial densities, source contact term and boundary trace correction. This does not prove reciprocity of the entire scalar-plus-TT pressure response. K2548's compact adjoint/contact construction and K2578's Einstein-preparation independence were already proved and are reused.

All statements concern the conditional curved-product action completion, not native Met(X), a physical preparation, positivity or causality. SC-ACT-01/GEO-03/GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Source, ledger0.263 LT-GR6b/10/11 and LT-SM8, canon and physical-selection debts do not change. No novelty, external-expert or proof-assistant certification is claimed.

## 1. Compute the tensor Gram, including its boundary form

Use K2552/K2582 notation kappa!=0, K=35kappa^2/3624192, R=1/|kappa|, C=cos(sqrt(K)r), S=sin(sqrt(K)r)/sqrt(K). Let x=KS^2, w2=C^4S^2, w5=C^6S^4, gamma=4C'/C+2S'/S. K2552's actual TT map has observer4/radial1/angular2 eigenvalues

    Rcal(b)=diag(t_b,b,a_b),
    t_b=-SC b'/4+(-3+7x)b/4,
    a_b= SC b'/2+(1-7x/2)b.

The tensor contraction on these block-scalar tensors is 4t_ut_v+uv+2a_ua_v even with the indefinite observer metric: each block identity contracted with itself gives its rank. This positivity on one restricted subspace is not positivity of the full tensor space. Define the reduced radial pairing

    B(u,v)=integral_0^R w2(4t_ut_v+uv+2a_ua_v)dr.

It is per unit invariant observer volume and normalized angular-orbit volume, not a finite full-spacetime integral when observer volume is infinite. Multiplying sources by a tangential cutoff would break their conservation and is not used. Finite B-annulus/angular integrations are retained separately.

Expanding gives p u'v'+q0(u'v+uv')+r0uv, where

    p=3S^2C^2/4,
    q0=7SC(1-3KS^2)/4,
    r0=7(3-14KS^2+21K^2S^4)/4.

Using S'=C, C'=-KS, C^2+KS^2=1 gives

    r0-q0'-(w2'/w2)q0=63KC^2S^2/4.

One integration by parts therefore proves the EXACT identity

    B(u,v)=3/4 <u,(-D5+21K)v>_w5
             +[w2 u(pv'+q0v)]_0^R,             (1)
    D5=partial_r^2+(6C'/C+4S'/S)partial_r.

The tensor Gram is 3/4(-D5+21K) on zero-trace amplitudes, not identity. The trace form in(1) must not be discarded for arbitrary amplitudes.

## 2. Orthogonal trace splitting in the correct pairing

Let q=bpsi from K2582: D5q=21Kq, q(R)!=0, q,q'<0 for r>0. For every smooth regular b0 with b0(R)=0, (1) gives B(b0,q)=0; the center boundary term vanishes by regularity and w2 p=O(r^4), w2 q0=O(r^3). Its own norm is

    Nq=B(q,q)=w2(R)[p q q'+q0 q^2]_R>0.         (2)

Indeed q q'>0, p>0, and q0>0 on the actual tube since 3KS^2<=3KR^2=105/3624192<1. Equivalently the original contraction contains q^2 and is strictly positive. Consequently

    B(b0+a q,c0+d q)
       =3/4 <b0,(-D5+21K)c0>_w5+Nq a d.       (3)

This is a derivative-containing trace-controlled tensor norm, not scalar L2(w5). It neither adds an independent vector to a complete scalar Dirichlet basis nor contradicts K2582's empty-resolvent counterexample for the unmarked enlarged scalar domain.

## 3. Reciprocity of the FULL coupled TT metric response

Let c=970112/(13395kappa), rE=-1144/(15kappa), mu=611557655kappa^2/39953092608. For b=b0+a q, K2582 and K2588 give

    h[b]=Rcal(H_D b0+q H_q a),
    H_D=rE G_E,D+(rE^2/c)G_Q,D,
    H_q=rE G_E,ov+(rE^2/c)G_Q,ov.               (4)

G_Q,D and G_E,D invert D5+Y+mu-21K and D5+Y-16K in the TT Dirichlet radial basis; G_Q,ov and G_E,ov invert Y+mu and Y+5K on the tagged trace channel. Every B inverse uses the REAL conjugate average of K2588, with the same fixed preparation on each use. It is symmetric in the actual B density. The Dirichlet inverses are diagonal in A5=-D5, hence commute with the radial Gram multiplier 3/4(A5+21K). They are not assumed to commute with arbitrary boundary inverses in B.

Equations(3)-(4) now prove

    <Rcal(b1),h[b2]> = <h[b1],Rcal(b2)>         (5)

for compatible smooth tagged TT sources, including all angular modes. Rapid spectral decay and the inherited polynomial bounds justify sums; the finite-mode identity extends by that continuity. This is reciprocity of the selected full original metric response to this source sector, including both forced Einstein and Q channels. It is not full tensor-operator self-adjointness, a positive Hamiltonian, causal propagation or arbitrary-source reciprocity. Scalar and TT radial bases remain distinct.

### Released nonzero trace consumer

Take any nonzero smooth compact B scalar v and set a=(Y+5K)(Y+mu)v, b=q a. The actual fields are

    z=Rcal(q rE(Y+mu)v),
    Q=Rcal(-q rE(Y+5K)v/c),
    h=Rcal(q[rE(Y+mu)+rE^2(Y+5K)/c]v).

Their source equations and h=z-rE Q hold identically. Compact v and its differential images satisfy every homogeneous B boundary preparation, so these are responses of the SAME averaged inverses, not solutions with refitted boundary data. The leading coefficient is rE+rE^2/c=429/(106kappa)!=0; the response is nonzero: if its order-two scalar operator annihilated compact v, angular decomposition and regular B-radial ODE uniqueness would force v=0. The same argument for the order-four source polynomial excludes a zero source. Two such sources obey(5) by formally symmetric commuting real polynomials in Y. Add independently a zero-trace source manufactured from a smooth compatible compact radial/B amplitude eta by (D5+Y-16K)(D5+Y+mu-21K)eta. Its paired solutions are explicit polynomial images of eta and cross pairings with the trace source vanish by(3). The probes check these actual polynomial equations, signs and nonzero constants; the all-mode proof is not a finite matrix test.

## 4. The complete compact-detector adjoint

For an actual compact smooth conserved detector F=EW, K2578's formal Einstein identity gives <F,z>=-rE<W,j>/2. Thus only the Q channel and contact term enter D_W=<F,h>. Keep K2584's original compact radial-pressure source, with t=(4A+3P)/2 (including any supplied B dependence),

    H=(-X-7K)_D^-1, chi=Ht/6,
    b=P/2+gamma chi'+6Kchi, a=b(R)/q(R).

The scalar cofactor Ccof=adj(M)vsrc acts through K2552's actual six-potential tensor realization T. With Rd the real symmetric scalar determinant inverse from K2588, define

    sW=Rd Ccof^dagger T^dagger F.

The differential transpose is taken against compact F in the actual invariant tensor contraction; T's mixed entries contribute twice and skew components are retained through Ccof. F is symmetric, but that does not allow discarding the full cofactor before transposition. This is not a Euclidean transpose of six coefficient slots. Compact support removes differential boundary terms here, BEFORE applying Rd.

For the TT channel define fW=Rcal^dagger F in scalar density w5. Explicitly, after integrating the compact detector over observer/angular-A orbits, let tau_o,tau_a,Frr be its observer/angular traces and radial entry. Set

    aF=SC(-tau_o/4+tau_a/2),
    bF=Frr+(-3+7KS^2)tau_o/4+(1-7KS^2/2)tau_a,
    fW=[w2 bF-(w2 aF)']/w5.                    (6)

The detector is an actual smooth tensor, not three independently prescribed scalar trace functions. At the radial center its smooth angular-orbit average has Frr=n0+O(r^2), tau_a=2n0+O(r^2), tau_o=o0+O(r^2), with smooth even expansions. Thus aF=r(n0-o0/4)+O(r^3), bF=3(n0-o0/4)+O(r^2). Since w2=r^2(1+O(r^2)) and w5=r^4(1+O(r^2)), the leading terms in(6) cancel and its numerator is O(r^4) with smooth even quotient. Compact support away from r=R and B endpoints supplies the spectral compatibility. Arbitrary independent trace profiles without this center condition are outside the theorem.

Let GD=G_Q,D, Gov=G_Q,ov, Pi_q f=integral w5 q f dr, and

    gW=GD fW, etaW=(w5/w2)gW,
    deltaW=Gov Pi_q fW-Pi_q GD fW.              (7)

Transposing the ACTUAL trace-lifted operator GD(b-q a)+q Gov a gives

    D_W=-rE<W,j>/2+rE^2[<sW,chi>_w2
       +(1/c)(<gW,b>_w5+<deltaW,b(R)/q(R)>_B)]. (8)

This evaluates actual compact EW detectors; it does not assert deltaW is nonzero for every such detector. Scalar symmetry alone would miss the last term. Tensor reciprocity(5) and this scalar-coefficient endpoint functional are consistent because(5) uses the different Gram(1).

### Released direct sensitivity to the original pressure source

For compact A,P, chi(R)=P(R)=0. The normalized splitter psi satisfies (X+7K)psi=0, psi(R)=1. Weighted Green identity gives

    chi'(R)=-<psi,t>_w2/[6w2(R)].               (9)

Define Bdag eta=-(w2 gamma eta)'/w2+6Keta and

    LW=H[sW+(1/c)Bdag etaW]/6
        -gamma(R)psi deltaW/[6c w2(R)q(R)].     (10)

At the center gW is regular even, etaW=C^2S^2gW=r^2g0+O(r^4) and gamma=2/r+O(r), so Bdag etaW=-6g0+O(r^2) is regular even. The first-order boundary term is O(r^3) and vanishes. This justifies(10) without treating the r-coordinate center as a regular nonzero-weight endpoint.

Because both H and the Dirichlet response are symmetric in their respective spaces, and chi(R)=0 eliminates the first-order integration boundary, (8) becomes the explicit original-source adjoint

    D_W=-rE<W,j>/2+rE^2[<LW,t>_w2
                         +<etaW,P>_w2/(2c)].   (11)

Substitute t=2A+3P/2 to read off the A and P sensitivities. This retains the contact term, source half factors, weight conversion, cofactor transpose and endpoint correction. It uses no identification of scalar/TT radial eigenbases. Smooth compact detector data and the inherited spectral-compatible source class suffice; extend to point/measure sources only through the existing proved continuity, not through unsupported endpoint traces of arbitrary distributions.

## 5. Contrary constructions and remaining boundary

For a scalar test channel the trace correction in(7) can be nonzero. In the actual curved radial problem let e_sigma be a nonzero regular Dirichlet D5 eigenfunction, D5e=-sigma e, and v compact on B. Put g=e_sigma v and f=(D5+Y+mu-21K)g. Then GD f=g, and Green identity gives

    (-sigma-21K)<q,e_sigma>_w5=w5(R)q(R)e_sigma'(R).

Uniqueness of the regular second-order ODE makes e_sigma'(R)!=0. Hence

    Gov Pi_q f-Pi_q GD f
      =w5(R)q(R)e_sigma'(R)Gov v !=0.

This is a scalar transpose counterexample, not proof that f is Rcal^dagger EW for a compact W. A separate exact flat-interval fixture in the probe checks the same affine transpose algebra with a nonzero residual when the trace term is omitted; it is labeled a control, not curved-source evidence.

Do not extend(5) to all scalar-plus-TT sources: scalar/TT cross pairings can carry boundary terms because chi(R)=0 does not force chi'(R)=0. Equation(11) makes those terms available for the next matched-boundary test. Physical boundary selection, calibrated conserved observation, full-module reciprocity, causality and native displacement remain separate.

[K2588](k2588-real-boundary-response-2026-11-05.md), [K2582](k2582-affine-radial-boundary-response-2026-11-05.md), [K2584](k2584-scalar-spectral-boundary-inverse-2026-11-05.md), [K2552](k2552-localized-source-domain-2026-11-04.md), [K2548](k2548-compact-coupled-metric-detectors-2026-11-04.md), [K2578](k2578-coupled-forcing-adapter-2026-11-05.md), [probe](../../tests/channel-swings/k2590_boundary_aware_response_adjoint_probe.py), [report](../../lab/process/k2590-boundary-aware-response-adjoint.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive defects after proof and control repairs. K2590 passes27 exact supporting checks and12 contrary controls; K2591 passes34 and7. Universal domain/adjoint and all-policy arguments remain distinct from symbolic identities, rational support certificates and finite consumers. No external-expert, proof-assistant, remote-CI or physical certification.
