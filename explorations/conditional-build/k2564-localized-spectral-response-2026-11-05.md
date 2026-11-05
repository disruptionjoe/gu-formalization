---
title: "K2564 Actual localized-source response by an elliptic companion"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: full compact-radial point-source distributional existence in a supplied space-form completion; no physical preparation, unique readout or native GU certification
scripts:
  - tests/channel-swings/k2564_localized_spectral_response_probe.py
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
result: K2564
carrier: actual compact conserved radial source times compact B distributions on the selected curved A7 times B7 completion LAYER=toy CHIRALITY=N/A
pairing: positive auxiliary spectral Hilbert norm and original distributional metric-test duality ON=declared_carrier
real_structure: real kappa nonzero, B signature3,4 and real source distributions
grading: scalar potentials, TT potentials, original metric and auxiliary field remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion
target: full localized-source existence and preparation-dependent observations MAP-TYPE=evaluation
```

# K2564 Close the compact-source localization gap without a Cauchy claim

## Result and preflight

For the actual K2531/K2552 compact smooth radial pressure, including its full cutoff region and cancelling scalar/TT tails, there is a distributional response to the invariant B point source. More generally every compact B distribution is admitted. The construction uses the actual positive-curvature B space form, one explicitly supplied global completion, a positive elliptic companion to its indefinite Laplacian, and K2562's Borel radial response family. No integrable expansion into eigen-distributions is assumed. Orthogonal spectral calculus supplies the missing distributional synthesis.

This is a conditional existence theorem for the selected independent ambient product/action/source. It does not identify Met(X), change SC-ACT-01/GEO-03/GEO-55 ASSERTS or SC-META-53 UNCERTAIN, move ledger0.263, or select physical boundary/causal data. It closes a mathematical localization debt, not GU acceptance. The global completion and radial choices are part of the supplied preparation.

Preflight compared K2556's finite-radial distributional construction, K2558's overlap, K2560's compact bounded-mode construction and K2562's polynomial radial bounds. None supplies the elliptic companion or admits the actual compact-radial times delta source. A mere self-adjoint extension of an arbitrary ultrahyperbolic chart is insufficient: its spectral graph norm need not control ordinary distributions. The companion below addresses that precise seam. No general essential-self-adjointness assertion about pseudo-Riemannian Casimirs is needed.

## 1. An actual completion of the curved B geometry

Fix K=35 kappa^2/3624192>0. In flat R^(4,4) with metric du.du-dv.dv take

    B={ (u,v): |u|^2-|v|^2=K^-1 }.

The unit normal is sqrt(K)(u,v), of positive squared norm1. Its shape operator is a sign times sqrt(K) times the identity, so the flat ambient Gauss identity gives sectional curvature K. The induced signature is(3,4), exactly the second space-form factor in K2519/K2552. The completion is diffeomorphic to S3 times R4 and any sufficiently small original B chart has a local isometry into it. Choosing this completion preserves the local equation; it is additional global preparation.

Put u=K^-1/2 cosh(t)theta, v=K^-1/2 sinh(t)omega, with theta,omega in S3 and t>=0. Then

    G_B=K^-1[-dt^2+cosh^2(t)dOmega_theta^2-sinh^2(t)dOmega_omega^2],
    dvol_B=K^-7/2 cosh^3(t)sinh^3(t) dt dtheta domega.

The omega sphere collapses smoothly at t=0; it is not a boundary. With Ltheta=-Delta_S3 and Lomega=-Delta_S3,

    Y/K=-partial_t^2-(3tanh t+3coth t)partial_t
         -sech^2(t)Ltheta+csch^2(t)Lomega.             (1)

For the nonsingular global coordinates y=sinh(t)omega in R4, let a=I+y y^T and m=1+|y|^2. Then, up to the fixed volume constant,

    dvol_B=m dy dtheta,
    Y/K=-m^-1 div_y(m a grad_y)-m^-1 Ltheta,
    m^-1 div_y(m a grad_y)=a_ij partial_i partial_j+7y_i partial_i. (2)

These signs keep all three positive and four negative directions. No Euclidean replacement of Y occurs.

## 2. A positive elliptic companion with proved strong commutation

On H=L2(B,|dvol_B|) define the quadratic form initially on C_c^infinity(B):

    q[f]=integral m [ |f|^2+(grad_y f)^* a grad_y f
                          +(2-m^-1)|grad_theta f|^2 ] dy dtheta.

Here a>=I and 1<=2-m^-1<2. The smooth local coefficients and positive density make this densely defined form closable: distributional derivatives of an L2-zero sequence cannot have a nonzero energy-norm limit. Close it and let Q>=1 be its Friedrichs self-adjoint operator. On compact smooth functions,

    Q=1+Y/K+2Ltheta.                                 (3)

Q is elliptic everywhere, including y=0. It is an auxiliary positive operator, not the indefinite physical energy.

For precision, expand only the compact theta sphere in its ordinary complete spherical harmonics. Its l-th harmonic eigenvalue is ell_l=l(l+2), l>=0. Orthogonal projections onto these harmonics commute with the form: coefficients depend only on y, the theta term is scalar, and harmonic orthogonality removes all cross terms. They therefore reduce the closed form and its representing operator. Thus

    Q=direct_sum_l Q_l,  Q_l>=1+ell_l,

with the finite harmonic multiplicities retained. This proves strong commutation of Q and Ltheta, not merely a commutator on a core. Define

    Ycal=direct_sum_l K(Q_l-1-2ell_l).                (4)

Each summand and the direct sum are self-adjoint with their natural maximal domains. Formula(2) holds on C_c^infinity; hence Ycal is a specified self-adjoint realization of the actual Y. We do not claim it is the only realization or that a general formal commutator guarantees (4).

In the joint spectral variables q,ell,nu, q>=1+ell and nu/K=q-1-2ell. Therefore

    |nu|<=K(q-1)<=Kq.                                (5)

For example q-1-nu/K=2ell>=0 and q-1+nu/K=2(q-1-ell)>=0 prove both sides. The elliptic scale controls every polynomial power of the indefinite spectral parameter. Q and Ycal preserve real data by conjugation.

The functional-analysis inputs are the closed positive form representation and Borel spectral calculus, as stated in [Bal's functional-analysis notes](https://www.stat.uchicago.edu/~guillaumebal/COURSES/Lecture-Notes-TPM.pdf). The compact-harmonic reduction above proves the commutation hypothesis required here. It does not assume a positive-Hilbert spectral theorem for an unspecified indefinite differential domain.

## 3. Point distributions belong to the companion's negative scale

Write H_Q^s=Dom Q^(s/2), with norm ||Q^(s/2)f||, and define negative orders by Hilbert duality. Since Q is smooth and elliptic on each compact chart, local elliptic regularity iterated twice gives

    ||f||_(H4(U))<=C_U ||Q^2 f||_H,

for U compactly contained in a chart and f in Dom Q^2. Nested interior estimates absorb the intermediate Qf and f norms because Q>=1. The seven-dimensional Sobolev embedding H4_loc into continuous functions then gives

    |f(b0)|<=C_b0 ||Q^2 f||_H,
    delta_b0 in H_Q^-4.                              (6)

This is the invariant point distribution evaluated using the displayed volume density. The normalization is not an extra coordinate Lebesgue delta. Every compactly supported distribution has finite order, so the same argument at sufficiently high even order places it in H_Q^-s for some finite s. [Interior elliptic regularity and its iteration](https://www.math.cmu.edu/~gautam/c/2026-632/notes/elliptic-equations.html) apply because all companion coefficients and the density are smooth and uniformly elliptic on each compact chart.

Negative-scale elements are genuine distributions: for compact test phi, ||Q^j phi||_H is bounded by a finite ordinary test seminorm since Q^j is a differential operator of order2j. In particular H_Q^-2j embeds continuously into H_loc^-2j. This also shows that spectral Y acting on the negative scale equals distributional Y, by testing against C_c^infinity. No trace of a general distribution onto the observer is taken.

## 4. Consume K2562 by orthogonal spectral synthesis

For the fixed actual smooth compact radial source and its unchanged Dirichlet split chi_D,b_D, K2562 constructs real radial potentials f_nu=(v_nu,u_nu,w_nu,U_nu), Borel in every real nu. They solve all four actual scalar equations, including the full mixed determinant d(X,nu), and have polynomial bounds in every required radial Sobolev norm. They need not be continuous in nu. Their root order and switched outer conditions remain fixed supplied choices.

Let E be a radial Hilbert Sobolev space and suppose one of these Borel response multipliers obeys

    ||f_nu||_E<=C(1+|nu|)^p.                         (7)

In the joint direct-integral representation of Q,Ycal, define the response by multiplying each spectral fiber of rho by the E-valued vector f_nu. Formula(5) gives

    ||f(Ycal)rho||_(E tensor H_Q^(-s-2p))
        <=C(1+K)^p ||rho||_(H_Q^-s).                (8)

This follows by integrating the squared fiber norms: q^-p(1+|nu|)^p<=(1+K)^p. It is an orthogonal Hilbert synthesis, not an absolute L1 expansion into prescribed eigen-distributions. Thus (6) admits the original delta source without asserting the earlier moment condition on an unconstructed eigenfamily.

For a fully explicit conservative ceiling one may use E=H30 of the respective auxiliary radial ball, p=86 from K2562, and s=4. Then all scalar potentials lie in H30_rad tensor H_Q^-176. K2562's unchanged full cofactor/tensor reconstruction uses at most26 B derivatives and26 radial derivatives. The resulting original fields therefore exist distributionally, with the safe local B regularity H^-202 after those explicit derivatives. This deliberately overcounts possible losses; it is not an optimal regularity statement. The auxiliary dimensions3 and5 both satisfy30>26+dimension/2, so regular radial center reconstruction is valid before passing to B distributions.

For a rigorous equation passage, set `rho_n=1_[1,n](Q)rho`. The sequence lies in H and converges to rho in H_Q^-s. Since Q and Ycal strongly commute, |Ycal|<=Kn on this truncation. The direct-integral radial equations hold there, retaining the source half, mixed determinant, skew, auxiliary and original-metric rows of K2552. The bounds at sufficiently high finite derivative orders pass every equation to the distributional limit. The limit source is exactly j_A(r)rho(B), including the actual compact cutoff. Real parts give real fields. No Cauchy estimate, causal Green operator, or change to the noncompact cancelling split is involved.

The formula uses R(v),R(u),S0(w) and adj(M)vsrc(U) exactly as in K2552/K2562, then h=z-rE sym(Qfield), e2=-A2^-1 BQfield. Here Qfield denotes the displacement tensor; the positive companion Q above is a different typed object.

## 5. Executed successor: overlap descent at the former spectral poles

The new base response permits the actual compact source, while K2558's overlap algebra accepts arbitrary local B distributions. Use that algebra rather than dividing the new spectrum by nu+mu or nu+5K.

On a sufficiently small common B chart choose the justified local non-Cauchy distributional inverses

    c(Y+mu)q=rho, (Y+5K)W=rho,
    R4(Y)V=q,

with the four factors of R4 solved in order. K2556/K2558 prove these local inverses using the real-principal-type scalar symbol and absence of compact adjoint kernel by analytic noncharacteristic uniqueness; their norm constants are allowed to depend on the fixed factors. No global spectral inverse at a pole is asserted.

For the regular splitter difference a psi, (X+7K)psi=0 and Tpsi=R(b_psi), the exact identities

    d(-7K,Y)=c(Y+mu)R4(Y),
    adj(M(-7K,Y))v=R4(Y)v

make Qfield_s=Qfield_t=-rE q Tpsi. The Einstein overlap satisfies

    z_s-z_t=-(rE/2) Lie_(W grad_A psi)G.

Add these coordinated overlap responses to the constructed base, with the opposite source signs. The original source is unchanged, Qfield and e2 are unchanged, and h changes only by the displayed distributional diffeomorphism. Every compact conserved smooth metric test therefore gives the same value for all regular splitters. This construction includes the two formerly excluded spectral pole values because no single-eigenspace division occurs. It restricts the completed response to the common local B chart, and is a supplied extension of the base prescription, not automatic agreement of independently selected inverses.

## 6. Follow through to the actual source-disjoint ambiguity

K2558's independent homogeneous field survives unchanged:

    (Y+mu-21K)u=0, Qfield_H=u R(1), z_H=0,
    h_H=-rE u R(1), e2_H=-A2^-1 BQfield_H.

A nonzero real analytic local u exists by its noncharacteristic analytic construction. The full Einstein linearization satisfies

    E h_H=-(rE/2)(mu-5K)u R(1),
    mu-5K=(67736495/4439232512)kappa^2>0.

It is nonzero in a patch away from the B source point. Choose compact smooth Wtest in that patch with c_W=<E h_H,Wtest>!=0 and set F=E Wtest. Formal self-adjointness and linearized Bianchi make F conserved. For the newly constructed actual compact-source response h0,

    <F,h0+a h_H>=<F,h0>+a c_W, a in R.

The same actual prescribed compact radial times delta source therefore permits every real value of this finite source-disjoint gauge-invariant measurement unless independent preparation restricts the homogeneous freedom. This no longer depends on replacing the source by a finite radial polynomial. It does not compare responses satisfying identical complete boundary data; that stronger claim is not proved.

## Postflight, controls and remaining condition

Exact checks recompute the hyperquadric metric inverse, volume, full B Laplacian, positive companion coefficients, compact-harmonic joint bounds, regularity arithmetic and actual overlap/curvature constants. Changed-input controls reject dropping the angular repair, halving it to a degenerating companion, replacing the indefinite operator by a Euclidean one, treating its graph norm as elliptic, or dropping the spectral regularity loss. These finite checks support the displayed formulas; they do not certify the universal spectral/domain proof.

The actual compact-source localization debt is closed in this supplied completion and domain. Mathematical existence and compact-test splitter consistency survive; a physical boundary/causal selection, homogeneous restriction, observer distribution restriction and native Met(X) bridge remain independent. The next useful question is an independently justified preparation/readout with those exact debts, not another eigenfamily existence step. Internal specialist and independent hostile review remain acceptance requirements; no external-expert, proof-assistant, novelty or empirical certification is asserted.

[K2562 radial family](k2562-parameter-dependent-response-2026-11-05.md), [K2558 overlap](k2558-distributional-splitter-overlap-2026-11-05.md), [K2556 local inverses](k2556-distributional-source-response-2026-11-05.md), [probe](../../tests/channel-swings/k2564_localized_spectral_response_probe.py), [report](../../lab/process/k2564-localized-spectral-response.json).
