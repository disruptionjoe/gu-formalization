---
title: "K2582 Affine radial boundary response and splitter compatibility"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: trace-lifted TT response and precise fixed-boundary obstruction; no scalar cofactor inverse or physical preparation
scripts:
  - tests/channel-swings/k2582_affine_radial_boundary_response_probe.py
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
result: K2582
carrier: trace-controlled radial TT source module of the selected curved seven-plus-seven system LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor-test duality and auxiliary positive Sobolev norms ON=declared_carrier
real_structure: real data; complex impedance explicitly represents two real quadratures
grading: scalar amplitudes, TT tensor, shifted and original metric, auxiliary grade2 kept distinct
action_owner: repository-construction -- stated conditional model
target: affine boundary lift, paired response and compact interior observation MAP-TYPE=evaluation
```

# Boundary traces change the common-domain question

## Result and scope

The scalar/TT splitter overlap is NOT internal to the homogeneous radial Dirichlet component domains used in K2580. The obstruction is a nonzero boundary trace, not a failure of the bulk equations. Simply adding the overlap eigenfunction to the unmarked radial operator domain removes its entire resolvent. A trace-tagged affine construction repairs the component response without pretending to preserve the old homogeneous component data. It admits an additional source-trace channel with polynomial all-angular bounds on the same B annulus and executes a nonzero source and conserved-observation consumer.

This is conditional mathematics on the selected curved product and action completion. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Source, ledger0.263 LT-GR6b/10/11 and LT-SM8, canon and physical selection are unchanged. K2562/64 already construct full compact-source responses under different preparations. No scalar matrix-cofactor inverse, arbitrary physical tensor source, causal evolution, physical boundary selection or native GU recovery is obtained here.

## 1. A trace discriminator precedes the scalar inverse

Use K2580's nonzero real kappa, K=35 kappa²/3624192, R=1/|kappa|, C=cos(sqrt(K)r), S=sin(sqrt(K)r)/sqrt(K), alpha=C'/C, beta=S'/S. The scalar and TT radial operators are

    X=partial_r²+(4alpha+2beta)partial_r, w2=C^4 S²,
    D5=partial_r²+(6alpha+4beta)partial_r, w5=C^6 S^4.

K2558 proves the unique regular normalized splitter mode

    (X+7K)psi=0, psi(R)=1, psi>1 inside,
    bpsi=psi''+Kpsi, Tpsi=Hess_A psi+Kpsi G_A=R(bpsi),
    D5 bpsi=21K bpsi, bpsi(0)=−4K psi(0)/3.

The symbol R(f) here is K2552's TT tensor map; R without an argument is the outer radius. Every regular splitter is chi_D+a(B)psi. Fixed chi(R,B)=0 therefore forces a=0. Moreover bpsi(R) is strictly negative, with the useful quantitative bound

    bpsi(R)<bpsi(0)<−4K/3.                         (1)

Indeed (w5 bpsi')'=21K w5 bpsi and w5 bpsi' tends to zero at the regular center. While bpsi is negative, its derivative is strictly negative for r>0; a first zero is impossible. The same integral argument gives

    psi'(R)=−7K/w2(R) integral_0^R w2 psi dr <0.    (2)

K2580's positive Dirichlet gap supplies an independent exclusion: if bpsi(R)=0, it would be a nonzero regular eigenfunction of A5=−D5 with eigenvalue−21K<0, contradicting positivity.

Thus neither the scalar splitter displacement psi nor its TT counterpart bpsi is in the corresponding homogeneous Dirichlet amplitude domain. This does NOT exclude the tensor from ordinary weighted L2: the Dirichlet eigenbasis is already complete there. Trace and spectral-domain membership must not be inferred from L2 membership.

## 2. Why an unmarked extra eigenmode destroys uniqueness

Let D_D be D5's regular-center Dirichlet operator domain in L2(w5 dr), and let

    D_ext=D_D+span(bpsi)

carry the SAME differential expression D5. The sum is direct in this trace-controlling graph domain, since bpsi(R) is nonzero. For every complex z outside the Dirichlet spectrum of D5 define

    h_z=bpsi−(D5_D−z)^−1[(21K−z)bpsi].            (3)

Then h_z(R)=bpsi(R) and (D5−z)h_z=0. Thus h_z is nonzero. At a Dirichlet eigenvalue its old eigenfunction already gives a nonzero kernel. Consequently D5 on D_ext has an eigenvector for EVERY complex z and has NO resolvent point. This is an exact operator counterconstruction, not numerical evidence of a small denominator. It is also not a claim that no right inverse with additional normalization can be chosen.

In particular, treating bpsi as an extra orthogonal eigenvector beside an already complete L2 Dirichlet basis is invalid. Adding a boundary degree of freedom requires a trace coordinate or boundary condition, rather than an unmarked enlargement of the same inverse problem.

## 3. A useful trace-tagged source and response construction

For a source amplitude with a well-defined outer trace set

    a(B)=b(R,B)/bpsi(R), b0=b−a bpsi, b0(R,B)=0.    (4)

This decomposition is unique among zero-trace residuals plus a tagged bpsi lift. Equation(1) controls the division by |a|<=3|b(R,B)|/(4K), and the same bound holds for every B derivative norm. On ordinary positive radial Sobolev spaces of order greater than1/2 near the outer endpoint, trace and this lift are continuous. The control grows as K tends to zero; no curvature-uniform claim is made.

For the fully smooth theorem, require b0 and the residual boundary data to satisfy K2580's compatible spectral-smooth conditions, and take a smooth on the closed B annulus and its two angular spheres. This admits nonzero outer source traces. It does NOT include every smooth b merely because b0 vanishes at R: higher Dirichlet powers impose higher compatibility. Finite-order versions retain K2580's auxiliary coefficient estimates; no unproved physical-center regularity is inferred from a negative coefficient order.

Let u0,v0 be the K2580 response of b0. For the tagged trace solve

    (Y+mu) uB=−rE a/c,
    (Y+5K) vB=rE a,                              (5)

where c=970112/(13395 kappa), rE=−1144/(15 kappa), and mu=611557655 kappa²/39953092608. Put

    u=u0+bpsi uB, v=v0+bpsi vB.

Since D5 bpsi=21K bpsi, these solve the ACTUAL TT rows

    (D5+Y+mu−21K)u=−rE b/c,
    (D5+Y−16K)v=rE b.                            (6)

Thus the response outer traces are bpsi(R)uB and bpsi(R)vB. They are supplied/derived affine response data, generally nonzero; they are not K2580's old homogeneous radial boundary data. The tagged coordinate is fixed by the source trace and the chosen B preparation, not a new freely fitted bulk field.

### All angular modes on the SAME annulus

Retain t in[asinh1,asinh2], zeta=sinh²t in[1,4], x=log[tanh(t/2)/tanh(asinh1/2)], length d, J=sinh(t)cosh(t)^(3/2), L=ell(ell+2), n=m+1. For (Y+q)f=F the exact transform y=Jf is

    y''−P_q y=−J zeta F/K,
    P_q=n²+A_q zeta−(L+3/4)zeta/(1+zeta),
    A_q=q/K+35/4.

Here A_Q=mu/K+35/4, A_E=55/4, and Amax=A_Q>A_E>3/8. Set D=4Amax+3/5 and

    kpsi²=1+n²+L+D, Lstar=25Amax−3/4.

Both potentials obey |P|<=kpsi². If L>=Lstar, both are nonincreasing. Otherwise if n²>=(4/5)L, both are nonnegative, since zeta/(1+zeta)<=4/5 and A_q zeta−(3/4)zeta/(1+zeta)>=0. All remaining indices satisfy kpsi²<1+(9/5)Lstar+D=:Kstar². There are only finitely many exceptional harmonic degrees, including their multiplicities.

Give BOTH channels opposite-sign impedance data

    y'(0)+i kpsi y(0)=kpsi g0,
    y'(d)−i kpsi y(d)=kpsi gd.                    (7)

K2576's flux, monotone-energy, positive-potential and bounded-exception proof now applies with these actual constants. For example

    CH=max(sqrt6 exp(d/2),2+d,exp(Kstar d/2)),
    CG=max(CH+sqrt3 CH exp(d/2)+d/4,
           sqrt2 CH exp(Kstar d)).

It gives sup|y|<=CH kpsi |g|+CG kpsi ||forcing||L1 and the derivative estimate from its section3. Weighted square summation over every angular mode gives H^(s+1) endpoint/forcing data to C_x H^s amplitudes and C_x H^(s−1) normal derivatives. Smooth data give smooth solutions. These are fixed, possibly large, polynomial bounds; no efficient condition number or sharp loss is claimed. kpsi is shared between the two added channels, but differs from K2580's radial-eigenvalue normalization. Complex impedance means two real quadratures, not a real self-adjoint Robin domain.

The added forcing pair obeys fE=−c fQ, exactly as required by the same source a. Setting Q=R(u), zfield=R(v), h=zfield−rE Q and e2=−A2^−1 B_aux Q verifies every selected TT, skew, mixed, BB and auxiliary row by the unchanged K2552 intertwiner. This is a trace-tagged coupled TT response, not the scalar-cofactor complement.

## 4. Splitter consistency and the precise boundary price

For a splitter change chi→chi+a psi, b→b−a bpsi, use ONE q solving c(Y+mu)q=a and ONE W solving (Y+5K)W=a, including their common chosen B preparation. The actual six-row scalar matrix obeys M(−7K,Y)v=c(Y+mu)v for v=(K,0,1,0,0,0). Thus its eigenline is solved directly by q: no inversion of the other four cofactor factors is needed on THIS overlap module. K2558's reconstruction with the same W then yields

    Q_s=Q_t=−rE q Tpsi,
    h_s−h_t=−(rE/2) Lie_(W grad_A psi) G.          (8)

The two opposite source corrections cancel; total Q/e2 are unchanged and the original metric changes by this bulk diffeomorphism. Every compact interior conserved metric test annihilates (8). This is an explicit extension of a base prescription to its splitter orbit. It is not an inverse for arbitrary scalar forcing, nor automatic agreement of independently chosen cofactor inverses.

It also does NOT preserve general fixed physical boundary data. At r=R, the vector field has normal component W psi'(R), nonzero wherever W is nonzero by(2). The induced tangential metric shift on the two A tangential blocks is

    delta h_obs=−rE W psi'(R) alpha(R) G_obs,
    delta h_ang=−rE W psi'(R) beta(R) G_ang.        (9)

Here alpha(R)<0 and beta(R)>0. Hence the prescribed bulk gauge shift generally moves the induced metric on that fixed boundary. Compact-support observational invariance and fixed-boundary gauge redundancy are different statements. No impossibility of every other boundary-matching prescription is proved; additional boundary fields or a different synchronized prescription would need their own conditions.

### Exact-field synchronization is an admissible repair

The boundary change in(9) binds the inherited uncorrected scalar S0 prescription, not every possible repair. Add the explicit pure gauge solution

    +(rE/2) Lie_(W grad_A psi)G

to its scalar-overlap Einstein response. Then z_s_corrected=z_t exactly, while Q_s=Q_t and e2_s=e2_t already. Opposite splitter-source corrections now cancel in ALL total fields, so their total boundary data and every defined readout are identical. The correction solves the homogeneous selected equations by their diffeomorphism identity; no source or fitted parameter is added. Equivalently, the same literal overlap source Tpsi may use its identical TT response in both decompositions.

This extends any fixed base response linearly to its regular splitter orbit by exact field matching. It supplies a common scalar/TT OVERLAP response on the annulus while the general scalar complement remains open. Individual component boundary values still change, so this does not put psi or bpsi into the old homogeneous component domains. The preparation choice has been made explicit and no physical selection follows.

## 5. Execute a nonzero source-trace and readout consumer

Take a(B)=1, b=bpsi, b0=0. The actual solutions of(5) constant on B are

    uB=−rE/(c mu), vB=rE/(5K).                    (10)

Use their actual endpoint data from(7) after y=J times each constant. Only the ell=m=0 harmonic occurs; the two ends are generally nonzero. The source is nonzero, has nonzero radial trace and is TT. Equations(6) check directly. For the original metric,

    E h=−(rE/2)(1+rE/c)R(b)−rE(mu−5K)R(u)/2
       =−(rE/2)[1+5K rE/(c mu)]Tpsi.             (11)

The coefficient is nonzero (exact rational check at kappa=1 suffices after its known scaling). Choose a compact dual test near a point where Tpsi is nonzero and set F=E Wtest. Bianchi and formal self-adjointness make F conserved with nonzero readout. This is an existence construction, not a calibrated physical detector.

For the same constant splitter change use q=1/(c mu), W=1/(5K). Equation(8) is nonzero at the radial boundary via(9), while every compact interior conserved detector still gives zero splitter difference. Applying the exact-field gauge correction above makes that total difference identically zero, including at the boundary. Thus the boundary warning and the observational agreement are executed on the SAME actual solution, not on an unrelated flat example.

## Verification and next condition

The probe checks actual intertwiner/spectral constants, both forced channel signs, overlap trace and center recurrences, the resolvent-extension identity, induced-boundary factors and nonzero source/readout consumer. Universal trace, regularity and all-angular synthesis arguments are the proofs above, not their finite checks. Independent internal specialist review is required; no external-expert or proof-assistant certification.

The next scalar-cofactor task must specify its boundary trace map and compatible source class before spectral inversion. The same homogeneous component Dirichlet conditions cannot simply be assumed invariant under splitter changes. The tagged TT construction and K2564's full-source construction survive at their different stated domains. Physical preparation, boundary gauge handling and independently calibrated observations remain open.

[K2580](k2580-radial-angular-source-domain-2026-11-05.md), [K2576](k2576-polynomial-impedance-control-2026-11-05.md), [K2558](k2558-distributional-splitter-overlap-2026-11-05.md), [probe](../../tests/channel-swings/k2582_affine_radial_boundary_response_probe.py), [report](../../lab/process/k2582-affine-radial-boundary-response.json). General [Sturm–Liouville boundary conventions](https://dlmf.nist.gov/1.13) are background; the operator-domain counterconstruction above is explicit.

Independent internal acceptance: field specialists cross-reviewed the concrete proofs and controls, then a distinct integrated hostile review returned no substantive findings. Exact producer/replay and native checks passed at the stated scope; no external or proof-assistant certification.
