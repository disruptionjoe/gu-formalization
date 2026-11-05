---
title: "K2576 Polynomial all-angular impedance control and scalar forcing"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-annulus scalar Sobolev inverse under supplied complex impedance; no full coupled inverse or physical selection
scripts:
  - tests/channel-swings/k2576_polynomial_impedance_control_probe.py
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
result: K2576
carrier: actual K2564 product completion with all theta and omega harmonic multiplicities LAYER=toy CHIRALITY=N/A
pairing: coefficient Sobolev norms and compact conserved Einstein tests ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms; complexification only where explicit
grading: all angular modes with monotone, nonnegative and bounded exceptional classes
action_owner: repository-construction -- stated conditional model
target: polynomial all-angular scalar impedance inverse MAP-TYPE=evaluation
```

# Actual turning structure removes the analytic-data requirement

## Result and scope

K2574 proves homogeneous all-angular existence with analytic boundary data. Its general real barrier/well control does not prove that analytic regularity is necessary for the ACTUAL potential. Here the actual high-theta potential is monotone; the remaining nonpositive nonmonotone cases have bounded angular degrees. This gives an explicit polynomial uniform estimate, a full-angular Sobolev homogeneous preparation, and an executed inhomogeneous SCALAR inverse on the same fixed annulus. No per-mode spectral gap or numerical scan is assumed.

The conditional product completion, complex two-real-quadrature boundary preparation and auxiliary positive coefficient norms remain supplied. This is not physical boundary selection, a self-adjoint realization, causal time propagation, an inverse for the full coupled source equations, or native GU recovery. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8, source, canon, observation and physical-quotient debts are unchanged. No sharp-loss, novelty or empirical certification is claimed.

## 1. Exact operator, partition and actual counterexample

Keep K2574's actual transformation and all real harmonic multiplicities:

    t0=asinh1, t1=asinh2,
    x=log[tanh(t/2)/tanh(t0/2)], 0<=x<=d,
    d=log[((sqrt5−1)/2)/(sqrt2−1)],
    z=sinh²t in[1,4], y=Jv, J=sinh(t)cosh(t)^(3/2),
    y''=P y, P=n²+A z−(L+3/4)z/(1+z),
    A=121366223/77168, L=ell(ell+2), n=m+1>=1,
    D=606773239/96460, nu²=1+n²+L, k²=nu²+D.

K2574 establishes |P|<=k². The decisive derivative is

    P_z=A−(L+3/4)/(1+z)².

Thus L>=Lstar:=25A−3/4=3034097699/77168 makes P nonincreasing. Since z increases with x, this is monotonicity in the actual ODE coordinate as well. Partition by the following ordered cases:

1. L>=Lstar: monotone P, with at most one crossing from positive to negative.
2. Otherwise, n²>=(4/5)L: P>=0 throughout the interval.
3. Otherwise, L<Lstar and n²<(4/5)L, hence k²<Kstar²:=1+(9/5)Lstar+D.

The last class has finitely many degree pairs and finite multiplicities. A single explicit constant handles it; no search for small Dirichlet denominators is used. The exact infinite turning family ell=5j,n=4j,j>=40 from K2574 lies in the monotone class.

The finite exception is substantive. The actual ell=100,n=60 mode satisfies

    P(1)=5585285/77168>0,
    P(2)=−2121869/38584<0,
    P(4)=166915639/96460>0.

It contains a double-turning well. Therefore a claim that every actual mode is monotone is false. The generic barrier/well counterexample remains valid for arbitrary potentials, but cannot be copied into an unbounded-degree obstruction for this actual family.

## 2. Uniform homogeneous polynomial bound

Prescribe the SAME opposite-sign complex impedance data as K2574:

    y'(0)+iky(0)=k g0, y'(d)−iky(d)=k gd,
    Z=(y,y'/k), G²=|g0|²+|gd|².

Conservation of Im(y' conjugate(y)) gives

    ||Z(0)||²+||Z(d)||²=G².                       (1)

Zero data imply zero Cauchy jet, hence uniqueness and invertibility of the finite two-boundary map for each mode. This is two coupled real quadratures; it is not an ordinary real Robin condition.

For monotone P with a nonpositive suffix[a,d], put q=−P>=0 and

    F=|y'|²+(1+q)|y|².

Then q'>=0 and

    F'=q'|y|²+2Re(y' conjugate(y))>=−F.

Integrating BACKWARD yields F(x)<=exp(d−x)F(d)<=exp(d)(1+k²)G². The factor1+k² follows by bounding the two endpoint coefficients against the normalized jet in(1), rather than adding separate endpoint upper bounds. It controls y and y' at the turn. On the positive prefix, |y|² is convex and is bounded by its endpoint values. Also

    E=|y'|²−P|y|², E'=−P'|y|²>=0,

so E(x)<=E(a)=|y'(a)|². Combining the two regions gives

    sup ||Z||<=sqrt3 exp(d/2)sqrt(1+k²)G
              <=sqrt6 exp(d/2)kG.                       (2)

If the suffix is the whole interval, use its estimate directly. If it is empty, P>=0 and use the next argument; no nonexistent turning point is introduced.

For ANY nonnegative P, convexity gives |y|<=G. Integrating y''=Py from zero gives |y'|/k<=(1+dk)G. Hence sup||Z||<=(2+d)kG. For the bounded exceptional class, K2574's two-ended Gronwall estimate gives sup||Z||<=exp(Kstar d/2)G. Therefore

    C_H=max(sqrt6 exp(d/2),2+d,exp(Kstar d/2)),
    sup_x ||Z(x)||<=C_H k G                             (3)

holds for EVERY mode and multiplicity. C_H is fixed by the annulus and operator; it may be very large. This proves one conservative derivative loss, not its sharpness or a practical condition number.

## 3. Released scalar forcing inverse

Now solve exactly y''−P y=f with the same impedance conditions. This changes the SCALAR equation. The old homogeneous full-field reconstruction cannot be applied to arbitrary f without checking the coupled source equations anew.

Let u(0)=1,u'(0)=−ik and v(d)=1,v'(d)=ik. Their constant Wronskian W=uv'−u'v is nonzero by homogeneous uniqueness. The kernel

    K(x,tau)=u(min(x,tau))v(max(x,tau))/W

has first-derivative jump1 and zero boundary impedances in x. The normalized homogeneous boundary responses are h0=kv/W and hd=−ku/W. Equation(3) implies |u/W|,|v/W|<=C_H.

For monotone P, apply the shifted energy argument to v on its nonpositive suffix. Its terminal jet is(1,ik), so |v(x)|<=sqrt3 exp(d/2)k there. Whenever max(x,tau) belongs to that suffix,

    |K(x,tau)|<=C_H sqrt3 exp(d/2)k.

If both points lie in the positive prefix, write the kernel as Dirichlet interpolation of its values at0,a plus the Dirichlet Green kernel on[0,a]. At zero, |K(0,tau)|=|h0(tau)|/k<=C_H; at a use the suffix bound. For P>=0 the interpolation basis is nonnegative with sum<=1, and the absolute Dirichlet Green kernel is dominated by that of the free negative second derivative, with supremum a/4. This last comparison follows from the one-dimensional maximum principle, including the distributional positive point source. It proves the required polynomial bound throughout the prefix.

Everywhere-positive modes use the same Dirichlet argument on[0,d]. Exceptional modes use |v|<=sqrt2 exp(Kstar d) from its fixed terminal jet and the bounded first-order coefficient. One uniform choice is

    C_G=max(C_H+C_H sqrt3 exp(d/2)+d/4,
            sqrt2 C_H exp(Kstar d)),
    sup_(x,tau)|K(x,tau)|<=C_G k.

Thus zero-boundary forcing gives sup|y|<=C_G k ||f||_L1. No homogeneous flux identity is incorrectly imposed on the forced solution: the kernel uses homogeneous fundamental solutions.

For the normal derivative choose an available forward or backward interval of length h=min(d/2,1/k) from each x. Integrated Taylor's formula gives

    |y'(x)| <= [2/h+(h/2)k²]sup|y|+||f||_L1
             <=(4/d+5k/2)sup|y|+||f||_L1.             (4)

Consequently y'/k has the same O(k) forcing bound. Combining with(3) gives a bounded scalar solution operator for arbitrary supplied boundary data and integrable forcing, with constants independent of angular mode. Existence is by the explicit kernel plus homogeneous solution; uniqueness follows from(1).

## 4. Execute full-angular Sobolev synthesis and observation

Since k is uniformly comparable to nu, summation over all harmonic multiplicities with weight nu^(2s), followed by Minkowski for the forcing integral, gives

    (g0,gd,f) in H^(s+1) x H^(s+1) x L1_x H^(s+1)
       -> y in C_x H^s, y_x in C_x H^(s−1).           (5)

These are angular Sobolev spaces on the declared compact product factors, and L1 in the finite x interval. Finite harmonic sums and the uniform bound establish convergence and strong continuity by density; the integral equation gives continuity of y_x for L1 forcing. The equation holds distributionally, with second derivative in L1_x H^(s−2). Smooth data and forcing yield the corresponding smooth solutions by iteration. Modewise nonresonance alone would not justify this synthesis; the uniform polynomial estimate is the new dependency.

For HOMOGENEOUS data, the unchanged J^-1 multiplication and h reconstruction preserve the scalar regularity; the auxiliary e2 still costs its declared differential order. Compact smooth conserved detectors pair continuously with h, with a Lipschitz bound in the H1 boundary norm at s=0. Real and imaginary components form the two real solutions dictated by the coupled control. No positivity, physical boundary selection, original-metric source adapter for arbitrary f, or closed full coupled realization follows from(5).

K2574's analytic preparation remains valid but is no longer the strongest sufficient data class on this fixed actual annulus. The result does not settle arbitrary annuli uniformly, remove K2572's Dirichlet resonance, or assert that a one-derivative loss is necessary.

## 5. Exact forced consumer and adversarial controls

For the independent fixture P=0,f=1 and arbitrary positive k,d, the exact zero-impedance solution is

    y(x)=x(x−d)/2−i d/(2k).

Both boundary conditions vanish and y''=1. Integrating the corresponding explicit Wronskian kernel gives the same expression, checking the forcing sign, normalization and jump independently. This is a scalar fixture, not the actual P=0 claim for every angular mode. A same-sign impedance rule instead admits e^(−ikx) when P=−k², showing why changing the far sign invalidates uniqueness. The actual ell100,n60 well rejects global monotonicity; K2574's generic barrier/well rejects extension to arbitrary real potentials. The exact probe verifies these altered-object controls alongside actual constants, shifted-energy identities and the infinite turning family.

Universal energy, comparison, Green-kernel and density proofs carry the all-angular claim; finite checks support the algebra and consumers. The next coupled-source adapter must derive every source equation under nonzero f before claiming a full response inverse. Independently justified physical control/observation and sharper finite-exception/turning estimates remain meaningful alternatives. No further source or ledger verdict follows from this mathematical preparation.

[K2574 predecessor and actual coefficients](k2574-angular-cone-domains-2026-11-05.md), [K2572 resonance boundary](k2572-boundary-preparation-robustness-2026-11-05.md), [probe](../../tests/channel-swings/k2576_polynomial_impedance_control_probe.py), [report](../../lab/process/k2576-polynomial-impedance-control.json).
