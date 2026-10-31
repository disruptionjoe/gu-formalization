---
title: "K2348 Even-distortion stationarity and flat-connection action boundary"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2348_even_distortion_stationarity_boundary_probe.py
---

# K2348 Even-distortion stationarity and flat-connection action boundary

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
result: K2348
carrier: selected real Cl(7,7) one-form adjoint on the declared curved metric chart LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace and exterior Hodge bilinear pairing ON=declared_carrier
real_structure: real coefficients; complex Hilbert adjoint where stated
grading: internal Clifford even/odd; exterior degree kept separate
action_owner: repository-construction -- conditional selected native first transgression and separate residual-square second action
target: even translation obstruction and zero-kappa flat-connection counterfamily MAP-TYPE=evaluation
```

## Result and object boundary

[K2345](k2345-curved-bundle-ricci-obstruction-2026-10-30.md) excludes the conditional selected T=0 stationary continuation on its curved metric. A tempting repair is a local flat metric-compatible connection A, with nonzero displacement T=A−B from the Levi-Civita spin connection B. Flat A stationarizes a curvature-square action, but that is not the first action under test. Here an exact parity argument excludes every purely even distortion as a stationary repair when kappa!=0, under the explicitly selected Clifford Shiab/trace convention. At kappa=0, a local frame-jet counterfamily shows that flatness alone still does not solve the first action. Odd/mixed-grade distortions and separately owned terms remain open.

Source SC-ACT-01 ASSERTS its transgression first action; SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, not ordinary torsion. Neither selects every convention used below or asserts that this chart is stationary. SC-META-53 remains UNCERTAIN. Ledger0.263 and source verdicts remain unchanged. This is a conditional obstruction to a proposed repair, not a source-claim falsification.

## Action and nonlinear even-sector theorem

Use the [native action reinspection](../../lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md) distinction, with the same selected Cl(7,7) trace/Hodge realization as the [K129 parity analysis](selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md). Write S for the chosen linear Shiab to13-forms and

    I1=<T,S(Fbar)>+kappa/2<T,*T>,
    Fbar=F_B+(1/2)D_B T+(1/3)T wedge T.           (1)

Products and normalization are those of that reinspection, with T wedge T as its quadratic curvature product. This first action is not the squared printed endpoint and not an unspecified Einstein-Hilbert action. At fixed geometry, B and Shiab coefficients, independent translation variation X gives

    dI1[X]=<X,S(Fbar)>
       +<T,S((1/2)D_B X+(1/3)(X wedge T+T wedge X))>
       +kappa<X,*T>.                              (2)

For concrete controls the selected channel tuple is (comm,symi,symi), with the exact backend and signature pinned in the probe. The two displayed selected-Shiab terms each contain one internally odd Phi1; Phi2=(1/2)Phi1 wedge Phi1 is even. Exterior Hodge and differentiation preserve internal Clifford parity. Each complete Shiab term, in every product/commutator channel, therefore reverses internal parity, irrespective of its scalar coefficients. Scalar Clifford trace pairs only equal internal parity. Assume B and T are even and choose an arbitrary even X. Every argument of S in(2) is even, so both transgression pairings vanish POINTWISE:

    dI1[X]=kappa<X,*T> for every even X.           (3)

The scalar-trace/Hodge pairing restricted to the full even one-form carrier is nondegenerate. Clifford basis blades pair diagonally with nonzero signed squares, as do exterior one-forms; complexification or the chosen real form does not create a radical. Compactly supported arbitrary even tests then imply

    kappa!=0 and full I1 stationarity and T even => T=0.  (4)

Indefiniteness is not positivity and is not a loophole: if <T,*T>=0 for nonzero T, an independently chosen dual X still detects it. The probe includes a null even T with a nonzero dual pairing. Equation(4) is a necessary translation equation; allowing additional epsilon variations cannot repair a failed independent translation equation. If the allowed action tangent is a proper constrained subspace instead, that is a changed premise requiring its own duality test.

## Curved flat-connection repair and zero-kappa escape test

On a contractible orthonormal/spin chart, A=0 defines a flat metric-compatible connection. Its displacement T=−B is grade2/even. Because the K2345 B has nonzero curvature, B cannot vanish identically in the chart. Thus T is not identically zero and(4) excludes this I1 repair for kappa!=0. This excludes more than one ansatz: any purely even T under these premises must vanish. No global parallelizability, flat-bundle or topology assertion follows.

At kappa=0 equation(3) vanishes, but odd translations remain. At a point p choose a normal spin frame with B(p)=0 and choose A=0, so T(p)=0 and dT(p)=−dB(p). Integrating the derivative term in(2) by parts on compactly supported tests gives the local odd Euler pairing

    <X,E>_p=(1/2)<X,S(dB)>_p
             +(1/2)sum_mu <partial_mu B,S(dx^mu wedge X)>_p. (5)

At p, B*T and cubic terms vanish. Derivatives of S, volume or pairing multiply T(p)=0 and also vanish. The first term is half the curvature term. This is the actual first-action derivative, not S(F_A).

Keep the same curved metric and change orthonormal frame by

    g_c=exp[(c/2)(x0)^2 gamma01],
    B_c=g_c^-1 B g_c+g_c^-1 dg_c.

At p=x0=0 the frame, its first derivative, B(p) and curvature are unchanged, but partial0 B0 shifts by c gamma01. Define A_c=0 AFRESH in each frame. These are different flat connections, not gauge descriptions of the same A. For X=dx1 gamma0 the exact selected backend gives

    <dx0 gamma01,S(dx0 wedge dx1 gamma0)>=2.

Consequently(5) shifts by c. At most one member can annul this odd Euler row. Thus flat A does not automatically stationarize I1 even at kappa=0 on the same curved metric. This is a constructive counterfamily, not an exclusion of every specially chosen flat connection or every mixed-grade solution. It avoids recomputing the completed Ricci tensor and pinpoints the derivative datum that a real repair must control.

## Distinct I2 action and executed second-variation consumer

The printed endpoint is U=S(F_A)+kappa*T. Flat A gives U=kappa*T: for kappa!=0 it fails the printed ZERO-residual condition. Nonzero U alone does not prove failure of I2 stationarity. For kappa=0 it gives U=0 and stationarizes the separately declared smooth residual-square I2=(1/2)<U,Q_B U>, including moving coefficients, since every first-variation term contains U. This is an actual conditional positive construction for I2, not I1. [Path-dependency custody](../../lab/process/path-dependencies.md) forbids importing an operator because its residual value happens to agree.

Even for I2 at U=0, the Hessian is <DU[v],Q_B DU[w]> (for the stated symmetric pairing), need not vanish and is not an inherited T=0 frozen I1 Hessian. The probe varies actual polynomial residual U(x)=x+x²: at x0=0 its squared action has zero first derivative and second derivative1. A changed residual U=2x+x² has the same zero value but second derivative4. A moving symmetric coefficient Q(x)=1+x leaves the zero-residual first derivative zero but still contributes at later orders. This finite control demonstrates the exact chain-rule issue; the general identity follows by differentiating the action twice.

For nonstationary I1 candidates, a path's second derivative is Hess I1[v,v]+DI1[a], with acceleration a. Discarding the second-jet term is unjustified. Exact control I(x)=x+x²/2, x(e)=e+c e²/2 gives second derivative1+c, whereas the straight path gives1. K2342 already constructs the actual moving lift and K2345 the nonzero observed scalar87lambda²exp(lambda t)/91; those geometric identities survive but supply no stationary dynamics. Changing A alone leaves the literal ambient metric/receiver untouched.

## Covariance and remaining construction

Under a genuine simultaneous gauge change, A'=g^-1Ag+g^-1dg and T'=g^-1Tg. Starting from A=0 gives A'=g^-1dg, generally not zero. Replacing it by zero again changes the connection, as used explicitly in the counterfamily. Curved B cannot be gauge-equivalent to flat A because curvature transforms covariantly.

K129 already contains linear T=0 parity, and K803 fixed-structure principal invariance; neither supplied this nonlinear even-sector stationarity obstruction or the zero-kappa frame-jet family. The result directs a nonzero-kappa repair toward a mixed/odd distortion with its complete odd and even Euler equations, or an explicitly different complete action. A local I2 residual-zero branch needs its own moving Hessian, receiver, closed domain and physical pairing. No source-owned global stationary vacuum, physical spectrum, stability, positivity or GU falsification is obtained.
