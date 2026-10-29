---
title: "K2263 Bounded local preparation and the cost of remote readout"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional model only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2263_bounded_local_preparation_probe.py
---

# K2263 Bounded local preparation and the cost of remote readout

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2263 Bounded local preparation and the cost of remote readout
carrier: K2261 constrained1280 fields on R13, reflected compact-band quotient M, and1024-component preparation potentials LAYER=toy CHIRALITY=N/A
pairing: positive supplied G norm on M and ordinary L2 norm on preparation potentials ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: copy, occupation and record labels; not physical chirality
action_owner: repository-construction -- supplied mathematical model
target: actual bounded preparation map, singular-cost spectrum and distance-sensitive readout MAP-TYPE=intertwiner
```

## 1. Density does not give uniformly cheap access

[K2261](k2261-band-quotient-local-observation-2026-10-29.md) proves density of local constrained representatives in the supplied [K2258 quotient](k2258-variable-local-preparation-2026-10-29.md). Here the cost is explicitly the L2 norm of the1024-component preparation POTENTIAL phi. It is not an apparatus-energy norm or the quotient-state norm. We retain the actual degree-two Clifford parametrizer P, raw constraints S=T=0, reflection Pi, compact band B and positive G of those notes.

For bounded nonempty open O, extend phi by zero with E_O and define, in unitary Fourier normalization,

    A_O phi = Pi [P(xi) F(E_O phi)(xi)],
    A_O: L2(O;C1024) -> M_G.                         (1)

Only the band-restricted multiplier is meant in (1). General L2 inputs need not give P(D)E_O phi in the original L2 kernel K: globally this may be only a constrained H^-2 distribution. Formula(1) is the bounded completion. For phi in Cc∞(O), it agrees with the genuine compact smooth representative followed by Pi. Thus completed singular minimizers below are not automatically physically smooth minimizers.

Put

    H_O²=(2pi)^(-13)|O| integral_B tr(P*G P) dxi.      (2)

Before reflection, the integral kernel is (2pi)^(-13/2)P(xi)exp(-ix·xi); its exact Hilbert-Schmidt norm squared into the band G space is(2). Since reflection is G-unitary, Pi is G-orthogonal on the constrained band, and

    ||A_O||_HS <= H_O < infinity.                    (3)

G need not preserve K as an ambient operator: only its positive form on K and reflection covariance are used. K2261 gives dense range already on smooth inputs; M is infinite dimensional, so A_O has positive singular values s_n decreasing to0 and a complete left singular system u_n in M_G. Standard compact-operator facts are summarized in [Hart's Hilbert-space lecture](https://sites.math.washington.edu/~hart/m556/Lecture7.pdf); the object-specific kernel and bounds are derived here, with no novelty claim.

## 2. Exact and approximate access cost, including a capacity consequence

Choose right singular vectors v_n in ker(A_O)^perp. For y=sum y_n u_n, exact completed preparation exists iff sum |y_n|²/s_n² is finite. Its least-norm input is sum (y_n/s_n)v_n. Tikhonov minimization of ||A_O phi-y||_G²+alpha||phi||², alpha>0, gives the unique

    phi_alpha=sum [s_n y_n/(s_n²+alpha)] v_n,
    error²=sum alpha² |y_n|²/(s_n²+alpha)²,
    cost²=sum s_n² |y_n|²/(s_n²+alpha)².              (4)

These follow by completing the square in each singular coordinate; the kernel coefficient vanishes. Finite singular truncations prove arbitrary approximation. Smooth inputs approximate completed inputs in L2(O), hence also their outputs under bounded A_O, but do not necessarily attain the same exact minimum.

If ||A_O phi-u_n||_G<=epsilon<1, then

    ||phi||2 >= (1-epsilon)/s_n.                     (5)

Take the u_n coefficient and use Cauchy-Schwarz with A_O* u_n=s_n v_n. Thus even fixed nonzero error below1 permits no finite uniform input budget over the unit sphere. This is an actual resource restriction on the supplied map, not a rejection of density.

**Finite access-capacity consequence.** If n orthonormal quotient targets each have an input of norm<=C and error<=epsilon, then

    n(1-epsilon)² <= C² ||A_O||_HS² <= C² H_O².      (6)

For each target y_j, ||A_O* y_j|| >= (1-epsilon)/C; sum over the orthonormal set and use the Hilbert-Schmidt trace. Inputs need not be mutually orthogonal. This bounds the number of accurately accessible orthogonal directions, not quantum channel capacity or physical information bits.

## 3. Explicit geometric hierarchy, beyond generic compactness

If O is contained in a ball of radius L about x_c and Omega=sup_B|xi|, Taylor-expand exp(-i(x-x_c)·xi) through degree N. The resulting operator has rank at most

    r_N=1024 binomial(N+13,13).

Each input component and spatial multi-index contributes one moment; multiplication by P and projection Pi cannot increase this rank. The REAL-phase integral remainder has magnitude at most (L Omega)^(N+1)/(N+1)!, without an exp(L Omega) factor. Its Hilbert-Schmidt error is bounded by H_O times that remainder. The variational characterization of singular values then gives

    s_(r_N+1) <= H_O (L Omega)^(N+1)/(N+1)!,
    cost(u_(r_N+1),epsilon)
      >= (1-epsilon)(N+1)!/[H_O(L Omega)^(N+1)].     (7)

This is a rigorous worst-direction hierarchy, not an asymptotic formula for the actual spectrum. Moving x_c does not change this upper bound, although reflection can change individual singular values.

An entirely specified band constant is available. In the inherited signed-permutation Clifford representation choose m=1, kappa=2, and B the two closed radius1/8 balls about ±2e10. Then Omega<=17/8, lambda>=5-1/2-1/64=287/64, ||H||<=4Omega+1<=19/2, so G<=g_max I with g_max=6063/574. The eight free-copy blocks of P each consist of dI, -D M_a and -dI+D M_a. Bounds |d|<=Omega², ||D||,||M_a||<=2Omega give

    tr(P*P) <=1024(1+16+25)Omega^4=43008 Omega^4.

Using |B|=256 pi^6/(135135·8^13), obtain

    H_O² <= |O| ·1344 g_max(17/8)^4/(135135 pi^7 8^13). (8)

For |O|<=1, pi>3 gives H_O²<10^-13, as verified by rational arithmetic. Thus every unit target approximated to error1/2 requires input norm greater than10^6 (a deliberately weakened consequence of1-epsilon<=||A_O phi||_G<=H_O||phi||2). This is in the stipulated coordinate/input units; rescaling P, band or input norm changes the price and is not a physical invariant. The small Fourier volume is an actual contributor to this example's cost.

## 4. Exact exterior sensitivity and distance-cost tradeoff

For ell_y(z)=<y,z>_G, the correct input readout kernel is

    h_y=F^-1[P*G yhat],
    sup_(||phi||L2(E)<=1) |ell_y(A_E phi)|=||1_E h_y||2. (9)

Pi disappears from the pairing because y is in its G-orthogonal range. The equality follows by the L2 Riesz theorem, and extends to arbitrary measurable E through the bounded band map. Omitting G is wrong when y is the G-Riesz representative. Consequently sensitivity to unit-cost inputs outside radius R tends to zero for each fixed readout. K2261's quotient-norm-relative theorem is a different statement.

For ||y||_G=1 and yhat smooth compactly supported in the interior of B, set a_y=P*G yhat and

    C_N(y)²=sum_(|alpha|=N) [N!/alpha!] ||partial^alpha a_y||2².

Plancherel and the multinomial theorem give || |x|^N h_y||2=C_N(y), so if O lies outside radius R,

    ||A_O phi-y||_G<=epsilon<1
    implies ||phi||2 >=(1-epsilon)R^N/C_N(y).        (10)

The proof pairs with y and bounds the tail of h_y by R^-N C_N. Such nonzero smooth constrained reflected y exist by applying P to a smooth bump within one ball, then symmetrizing. Every N is available, with target-dependent derivative constants. No target-independent exponential rate is asserted. In fact a nonzero compact-band h cannot have an exterior L2 tail Ce^-aR for all R with a>0: it would have exponential weighted L2 integrability for any smaller exponent, giving an analytic Fourier extension; compact support plus analytic uniqueness would force h=0.

K2076/K2063's exponential locality estimates concern a different unbounded-spectrum massive Dirac carrier on R3. They are not reused for this reflected compact band on R13. The present result closes the inference from dense local classes to efficient arbitrary local preparation. It supplies a computable norm formula and regularization rule; numerical spectrum, actual implementation-energy cost, nonlinear observation algebra and alternative noncompact/source-owned quotients remain independent constructions.

## Scientific ceiling and reproduction

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. Ledger0.263 (88 active targets/91 stored rows), LT-SM8/LT-GR6b/AC-F1, source/canon verdicts, full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings are unchanged. These results do not supply a source action, physical quotient, physical chiral carrier or held-out prediction.

The universal assertions are written mathematical proofs. The accompanying finite exact controls and deliberately changed-input tests check algebra, constants and counterexamples; they do not certify continuum completeness, arbitrary-dimensional controllability or a physical realization. Internal independent review is distinct from Lean, external-expert, novelty and remote-CI certification. Run the listed script; `--write` regenerates the hash-bound report.
