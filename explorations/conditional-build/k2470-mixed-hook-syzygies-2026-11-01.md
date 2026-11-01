---
title: "K2470 A full analytic scalar lift from mixed hook syzygies"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional full scalar inverse in the original ordinary kernel; unrestricted joint inverse and nonlinear convergence remain open"
---

# K2470 A full analytic scalar lift from mixed hook syzygies

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
result: K2470
carrier: original fourteen-dimensional split hook carrier and original polar background LAYER=toy CHIRALITY=N/A
pairing: original nondegenerate split-metric hook and ordinary-scalar coefficient pairing ON=declared_carrier
real_structure: original real geometry with exact coefficients in Q(sqrt2)
grading: tensor slots and homogeneous polynomial degree
action_owner: repository-construction -- supplied conditional mathematical models
target: A full analytic scalar lift from mixed hook syzygies MAP-TYPE=evaluation
```

## Result and scope

The original fourteen-coordinate hook bank has a boundary-preserving analytic
right inverse for EVERY scalar forcing in the ordinary-response kernel.
A six-axis differential potential crosses K2467's degree-seven obstruction
and gives an all-degree construction with explicit bound

    ||R_d g||1 <=576*d*(d+5)^5*210^(d-1)*||g||1, d>=4.

Thus scalar analytic forcing on an equal-radius polydisc R lifts on every
concentric equal-radius polydisc r<R/210. The large constant is sufficient,
not optimal. This settles the unrestricted scalar correction problem on this
conditional bank, not the unrestricted joint ordinary-plus-scalar inverse or
nonlinear convergence. Original source ACT01/06 and GEO55 ASSERTS and
META53 UNCERTAIN retain their scopes; ledger0.263 and canon are unchanged.

## 1. Mixed differential hook potential

Use the original coordinates, with A={4,5,6}, B={7,8,9}; all six metric
signs are +1. Define commuting differential vectors, zero outside their set,

    u4=D5^2-D6^2, u5=D6^2-D4^2, u6=D4^2-D5^2,
    v7=D8^2-D9^2, v8=D9^2-D7^2, v9=D7^2-D8^2,
    Pij=ui*vj-vi*uj,
    V_iij=Dj(Pij Phi), V_iji=-V_iij.

Here Di=partial/partial xi; no first-slot derivative is taken. All other slots vanish. The 18 possibly nonzero
coefficients are differential operators of order5. The fixed operator V
has coefficient l1 norm144 counting both antisymmetric slots. Its largest
D5 order is2.

Both u and v have sum zero and weighted-square sum zero. Hence P annihilates
1 and the vector(Di^2). Trace vanishes since sum_i V_iij=Dj sum_i Pij Phi=0.
Ordinary diagonal responses vanish by sum_j Dj^2 Pij=0; off-diagonal
responses cancel by Pij=-Pji. Cyclicity is automatic for repeated hooks.
For each original K column, its repeated entries on the opposite triple
are constant, so Gram polarity follows from the same zero sum. Sigma
polarity vanishes because both same-first-slot two-forms contain that index.
These statements use the original background, not transported coordinates.

The probe reconstructs all original coefficients and verifies these
polynomial identities, including all14 second-order scalar coefficient
polynomials. Those second-order terms cancel identically. The complete
scalar response is therefore a constant-coefficient operator

    Jstar(V(Phi))=Pscalar(D) Phi.

Its exact30 terms are serialized in the report and independently computed
from the original curvature and polarization bank. Its leading monomial is
D4 D5^3 D9^2 with coefficient1/8. Every other monomial has total D5+D9
order at most4. The sum of the absolute other coefficients, divided by1/8,
is35. These finite coefficient identities establish the following universal
construction for arbitrary polynomials, not just sampled degrees.

## 2. Full polynomial inverse in the original boundary ideal

Let Ij integrate from0 to xj and put

    T=8 I4 I5^3 I9^2,
    E=Pscalar*T-1.

On homogeneous degree-n polynomials each nonzero monomial transition of E
strictly increases exponent weight m5+m9, while preserving total degree n.
The weight is at most n, so E^(n+1)=0. No commutation of integration and
differentiation is assumed. Set

    Phi=T sum_(k=0..n)(-E)^k g.

Then Pscalar Phi=g by the finite geometric identity. Phi has a factor x5^3;
since V differentiates x5 at most twice, EVERY field coefficient has a
factor x5. This is an original boundary generator (x5=y2), hence the field
lies in the original boundary ideal. Spectator coordinates are unrestricted. Coefficientwise polarity expands V in
the fixed161 repeated-polar bank; linear coefficient extraction preserves the
common x5 factor, so this is the same K2449 generator/boundary domain.
Phi has degree n+6 and V(Phi) has degree n+1. For the actual degree-d scalar jet J_d=(4/d)Jstar, use
R_d g=(d/4)V(Phi), with d=n+1>=4. Lower degrees have this polynomial identity
but are not automatically admissible replacements for fixed lower jets.

For g=x2^2*x4*x7*x8*x11*x12, the first missing K2467 monomial, the explicit
potential is

    Phi=(1/3)x2^2*x4^2*x5^3*x7*x8*x9^2*x11*x12
        -(1/6)x2^2*x4*x5^4*x7*x8*x9^2*x11*x12.

The scalar is exactly g, the complete ordinary response is zero, and every
coefficient vanishes on the original section. The actual jet normalization
is d/4=2. K2467's 36-PDE obstruction remains correct for its constructed
seven-family sum; it is not an obstruction to this larger differential family.

## 3. Geometric coefficient bound and analytic lifting

For a nonzero differential word, integration then differentiation yields

    D^alpha I^beta x^m = m!/(m+beta-alpha)! * x^(m+beta-alpha).

This is a multi-factorial identity; invalid negative-exponent paths are zero.
In a length-k E word the factorials telescope. Spectators are unchanged,
and active total degree is at most n, so m!/m_final!<=6^n by the multinomial
bound. The sum of absolute coefficient products is at most35^k. Therefore

    ||E^k g||1<=6^n*35^k||g||1,
    ||Phi||1<=8*6^n*sum_(k=0..n)35^k||g||1
             <=16*210^n||g||1.

Five derivatives cost at most(n+6)^5 in coefficient norm. Multiplying by
the full V coefficient norm144 and the actual d/4 factor proves the displayed
576*d*(d+5)^5*210^(d-1) bound. Use an intermediate radius below R for Cauchy
coefficient bounds; the polynomial degree factor is summable whenever210r<R.
Uniform derivative convergence on smaller polydiscs verifies the operator and
boundary identities for the analytic sum.

## 4. Released joint consequence and remaining bottleneck

K2452 already gives a full mixed inverse for compatible ordinary/scalar
forcing with fixed finite passive degree m. Apply it to(Q,0), then add the
new ordinary-null scalar lift for an arbitrary fourteen-variable analytic g.
This solves(Q,g) when Q satisfies K2452's original compatibility conditions
and fixed passive-degree bound, while g now has unrestricted passive degree.
Take the smaller of the two available radii and preserve the same K2449
boundary/generator domain; no other carrier or lower-jet change is needed.

The unrestricted ordinary mixed inverse still has no uniform geometric
estimate as passive degree grows with total degree. K2443 is transverse;
K2452's constants depend on the fixed passive-degree bound. The new scalar
inverse does not remove that ordinary debt. Nonlinear products can increase
passive degree, and a fixed linear inverse with radius loss alone is not a
convergent nonlinear iteration. Next compare an unrestricted ordinary mixed
estimate or a majorant retaining both operator domains against the native
matter/light source-readout construction. More missing-scalar monomial hunts
in this same bank are now unnecessary.

Universal evidence is the differential syzygy, finite-symbol identity,
weighted nilpotence, factorial bound and analytic summation. Finite fixtures
check original tensors and polynomial outputs; reporting checks authenticate
dependencies. Internal review is not external-expert, proof-assistant,
novelty or native-physics certification.

[Probe](../../tests/channel-swings/k2470_mixed_hook_syzygies_probe.py) and
[report](../../lab/process/k2470-mixed-hook-syzygies.json).
