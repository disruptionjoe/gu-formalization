---
title: "K2288 A certified finite-frequency tensor consumer"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or empirical acceptance
scripts:
  - tests/channel-swings/k2288_finite_frequency_tensor_bound_probe.py
---

# K2288 A certified finite-frequency tensor consumer

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2288 A certified finite-frequency tensor consumer
carrier: complex prepared canonical tensor modes on the fixed real FLRW history LAYER=toy CHIRALITY=N/A
pairing: declared real tensor or positive complex Hilbert pairing ON=declared_carrier
real_structure: real metric histories or complex Hilbert adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: uniform propagation error MAP-TYPE=evaluation
```

## Result and inference ceiling

[K2286](k2286-quadratic-tensor-propagation-2026-10-30.md)'s geometric-optics ratio has a rigorous finite-frequency consumer. For comoving k/H_*>=10^10 and the explicitly prepared canonical incoming data v=1,v'=-ik at z=2.33, the propagation-only inverse-amplitude ratio lies between0.6349 and0.6352. This uses the unchanged K2283 background and its existing continuum certificate, without a new trajectory search. It is not a binary waveform, a screened-source calculation, a scalar-stability result or a GU prediction. SC-COS-50/51/54 ASSERTS and ledger0.263 remain unchanged.

## 1. Exact wave potential and Duhamel estimate

Let P=a_c sqrt F, q=P''/P and alpha_M=dot F/(HF). The vacuum spatial metric equation is ddot F=H dot F-2F dot H. Direct differentiation gives

    q=a_c²[dot H+2H²+(3/2)H dot F/F
                     +(1/2)ddot F/F-(1/4)(dot F/F)²]
     =a_c²H²[2+2alpha_M-alpha_M²/4].                  (1)

The use of the vacuum spatial equation is explicit. It must be changed for a matter-completed background. It avoids computing second derivatives of numerical data.

On the finite eta interval, v''+k²v=qv with the stated initial data obeys

    v(eta)=exp[-ik(eta-eta_i)]
           + integral_eta_i^eta sin[k(eta-u)]q(u)v(u)/k du.

For J=integral |q|deta, Gronwall gives |v|<=exp(J/k), and substitution yields

    |v-v_free|<=exp(J/k)-1=epsilon.                   (2)

No adiabatic derivative expansion is assumed. If epsilon<1, |v| is between1-epsilon and1+epsilon. Consequently the inverse-amplitude comparison lies in[Xi/(1+epsilon),Xi/(1-epsilon)]. These bounds apply to the complex test solution with the specified matching, not arbitrary initial wave mixtures. Spherical geometric dilution is factored out in defining this transfer.

## 2. Reuse the actual continuous tube, not sampled nodes

The K2283 interval recurrence checks its first-exit boxes on every cell: U>1 and |V|<4, with t<=T=(3.33)³<37. Thus U<2+4(T-1)<146<216 and |p|=|tV|<148. The endpoint certificate F(S)>123 and the exact integrating factor I of K2283 imply, for0<=s<=S=log T,

    F(s)>=F(S) I(S)/I(s),
    I(S)/I(s)=(U(s)/U(S))^(1/3)
             exp[integral_s^S a/(36U^(4/3))dq]
             > (1/6)exp[-(S-s)] >=1/(6*37).

Here a=-33.8>-36, U>1 and I F decreases because Delta=a²-2r>0. Therefore F>123/222>1/2 throughout the path. Endpoint positivity alone would not imply this without the integrating-factor identity.

Since Delta=1144.44<1145, the same identity gives

    |F_s/F| <148/3+1+1145/18<114,
    |alpha_M|<342,
    |2+2alpha_M-alpha_M²/4|<30000.

Physical H=H_* U^(2/3), a_c=1/(1+z), and |deta|=dz/H. Hence

    J/H_* <30000*36*integral_0^2.33 dz/(1+z)²
           <1,080,000.                              (3)

Every inequality covers the whole path. This conservative bound is not an optimized frequency threshold. It follows from already certified interval hypotheses and exact identities; no finite samples or guessed smoothness enter.

## 3. A numerical consequence with rational error budget

For k/H_*>=10^10, x=J/k<27/250000=.000108. The series inequality exp(x)<=1/(1-x),0<=x<1, gives

    epsilon <27/249973 <109/10^6.

Combining with0.63506<Xi<0.63509 gives

    .6349 < Xi/(1+epsilon) <= transfer <= Xi/(1-epsilon) <.6352.

H_* remains an unfixed dimensional scale; this is a ratio condition on the prescribed test-wave frequency, not an asserted instrumental band. The bound does not require monotone q or F. A source/environment construction may invalidate the endpoint matching while leaving all this test-wave mathematics intact.

## Verification and next question

The probe independently differentiates P twice, substitutes the spatial equation, validates the exact rational chain and interval endpoint transport, and includes a nonzero constant-potential finite-wave control and altered-sign/Jacobian/missing-term controls. The Duhamel theorem and inherited continuum tube carry the universal claim; finite oscillatory examples only exercise the implementation. K2283 dependency hashes and its source/probe/report identity are checked without rerunning unchanged heavy certificates. Next meaningful physics work must supply source/environment/matter matching or a different independent observable; improving this already sufficient loose bound alone is not needed for the stated consumer. Internal review is not proof-assistant or external-expert certification.
