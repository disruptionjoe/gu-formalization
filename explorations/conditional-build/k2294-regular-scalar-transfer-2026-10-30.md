---
title: "K2294 Finite-frequency constrained scalar transfer"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied models only; no native GU, empirical or hardware acceptance
scripts:
  - tests/channel-swings/k2294_regular_scalar_transfer_probe.py
---

# K2294 Finite-frequency constrained scalar transfer

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2294 Finite-frequency constrained scalar transfer
carrier: complex prepared canonical scalar modes on the fixed real vacuum FLRW history LAYER=toy CHIRALITY=N/A
pairing: Fourier complexification of the declared real constrained scalar quadratic action ON=declared_carrier
real_structure: Fourier conjugation with Q(-k)=conj(Q(k)) for the real scalar field
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: uniform finite-frequency scalar propagation bound MAP-TYPE=evaluation
```

## Result and scope

The negative instantaneous constrained mass found in [K2291](k2291-rolling-scalar-applicability-2026-10-30.md) is compatible with controlled finite-frequency propagation. On the SAME K2283 vacuum history, a specifically prepared scalar mode with k/H_*>=10^9 has canonical amplitude within0.004666 of unit free propagation throughout0<=z<=2.33. This is a full-interval evolution estimate, not a sign test. It establishes neither long-wavelength stability nor a sourced, observed scalar signal.

The action remains supplied metric f(R)=alpha R+R²/2-rho_v. SC-COS-50/51/54 ASSERTS, source-native bridges and ledger0.263 remain unchanged. K2292's matter extension is a different background/perturbation problem; this vacuum scalar estimate is not transported to it.

## 1. Regular coefficients and a canonical oscillator

Use K2291's Einstein frame g_E=(F/Fref)g, M²=C Fref, phi=sqrt(3/2)M log(F/Fref), b=dot F/(HF), beta=1+b/2 and j=b/(b+2). The vacuum00 relation strengthens the regularity statement:

    beta²=(b/2)²+(FR-f)/(6FH²),
    1+b=(FR-f)/(6FH²)>0.

Thus b>-1,beta>1/2 and |j|<1 wherever the certified F>0 history exists; FR-f=R²/2+rho_v>0. No division by dot phi is required, and scalar turning points are allowed.

For the regular flat-gauge perturbation Q, the canonical variable v=a_E Q obeys

    v''+(k²-q_S)v=0,
    q_S=a_E''/a_E-a_E² mu_Q²,
    mu_Q²=V_phi_phi+3dot phi²/M²
           +2dot phi V_phi/(M²H_E)-dot phi^4/(2M^4H_E²).

Dots in the last formula are Einstein proper time; primes are common conformal time. Let D=alpha²+2rho_v (unrelated to pump D). In H_* units and a_J=1/(1+z), substitution gives exactly

    q_S/(a_J² H_*²)=h² beta²(2-21j²+18j⁴)
                      -2j(alpha-D/F)+(alpha-2D/F)/3.  (1)

Here h=H/H_*; q_S has units H_*². This uses the constrained mass, not potential curvature alone. It follows from dot H_E/H_E²=-3j², a_E H_E=a_J H beta, and K2291's x=sqrt(6)j,y,w formulas. The normalization Fref and action scale cancel. The polynomial in j² has minimum-33/8 at j²=7/12 and endpoint values2,-1, so its absolute value is at most33/8 on|j|<=1.

## 2. Reuse certified whole-path bounds

[K2288](k2288-finite-frequency-tensor-bound-2026-10-30.md) derives from K2283's continuum tube

    U>1, U<146, |p|<148, F>1/2, |b|<342,
    1<H/H_*<36, alpha=33.8<34, D=1144.44<1145.

These are global interval/analytic bounds, not sampled points. Together with beta>1/2,beta<172 and|j|<1, equation(1) gives

    |q_S|/(a_J²H²)
      <(33/8)*172²+2*(34+2290)+(34+4580)/3
      =128220 <129000.                           (2)

In(2), H has physical units in the ratio; the lower bound H/H_*>1 controls the last two terms. Common conformal time satisfies |deta|=dz/H. Hence

    J_S=integral |q_S|deta
       <129000*36 H_* integral_0^2.33 dz/(1+z)²
       <4644000 H_* .                               (3)

The endpoint F bound and integrating factor behind F>1/2 remain essential. A new matter path must establish its own tube and coupled scalar problem.

## 3. A finite-frequency consumer with explicit initial data

At z=2.33 prepare v_i=1,v_i'=-ik. Duhamel with the exact scalar potential gives

    v(eta)=exp[-ik(eta-eta_i)]
             +integral sin[k(eta-u)]q_S(u)v(u)/k du.

Gronwall yields sup|v-v_free|<=exp(J_S/k)-1. For k/H_*>=10^9,

    J_S/k<1161/250000,
    epsilon<1161/248839<.004666.

Thus1-epsilon<|v|<1+epsilon throughout the interval. For Q itself, the corresponding endpoint ratio is

    (a_Ei/a_Ef)(1-epsilon) < |Q_f/Q_i|
                               < (a_Ei/a_Ef)(1+epsilon).

The scale factor cannot be omitted: canonical v and Q are different amplitudes. This is one specified complex incoming solution; it is not an arbitrary standing-wave mixture, detector response, matter mode or superhorizon growing-mode claim. H_* remains unfixed dimensionally. A constant negative mass can amplify low frequencies while allowing controlled high frequencies, so no contradiction with K2291 exists.

## 4. All initial data in a declared phase-space norm

A useful extension controls the full two-dimensional canonical transfer, without requiring the incoming-wave phase. Set Y=(v,v'/k) and let T map Y_i to Y(eta). Its generator is

    Y'=(k J+B)Y, J=[[0,1],[-1,0]], B=[[0,0],[q_S/k,0]].

The free transfer R=exp(k J Delta eta) is unitary in the Euclidean norm on complex two-vectors. In its interaction picture the perturbation still has norm |q_S|/k. Gronwall and Duhamel therefore give

    ||T-R||_2<=exp(J_S/k)-1<.004666,
    exp(-J_S/k)||Y_i||_2<=||Y||_2<=exp(J_S/k)||Y_i||_2.

The lower bound follows by applying the same argument to reverse propagation. The generator has trace zero, so det T=1 exactly. This is a transfer bound for ALL initial data in the explicitly scaled (v,v'/k) norm; it does not bound relative v amplitude near a node, nor replace the separate one-wave bound above. It remains a high-frequency, vacuum, canonical-scalar result, not physical source matching or low-frequency stability.

## 5. Turning points and remaining physics

The exact long-wave adiabatic solution Q proportional to dot phi/H_E, hence to j, is a consistency check. A second solution written Q_1 integral dt_E/(a_E³Q_1²) is legitimate only where Q_1 is nonzero; turning points forbid using that division as a global regularity proof. The Q,v equations above remain regular there. A global low-frequency transfer needs actual initial data and evolution, and matter requires the coupled system identified in K2292. Positive kinetic/gradient signs, negative instantaneous mass, high-frequency control and long-wave stability are distinct claims.

Verification independently simplifies the constrained mass into(1), checks the polynomial extremum and rational whole-path chain, and tests constant-potential exact oscillatory and tachyonic controls. The inherited continuum is hash-verified, not regenerated. Written Duhamel and interval bounds establish the uniform claim; finite controls are not continuum proofs. Standard perturbation background: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928). No empirical, novelty, Lean or external-expert certification.
