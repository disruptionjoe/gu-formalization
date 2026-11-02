---
title: "K2512 Finite-memory implementation and robust two-setting calibration"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied finite-Hilbert model; no hardware calibration, native GU realization or model-free two-setting certification"
---

# K2512 Finite-memory implementation and robust two-setting calibration

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
result: K2512
carrier: original C108 verifier times retained qutrit E with supported E0 dimension2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace ON=declared_carrier
real_structure: complex adjoint with real rotation fixtures
grading: original Q/T sectors and retained memory support
action_owner: repository-construction -- explicitly supplied finite quantum circuit
target: joint implementation and robust two-setting full-record calibration MAP-TYPE=evaluation
```

## Result and scope

An explicit retained-qutrit circuit supplies exact joint preparation/readout, supported effects, leakage and generator bounds. Its structural two-setting certificate has much smaller pooled weight than the generic five-sector protocol. The result extends to nonzero trusted full-carrier implementation errors and a declared anisotropic drift box, and composes with the original complete-record guarantee. A memory rotation invisible in one gap can change later records; the exact controls preserve that distinction.

This is conditional supplied-model mathematics. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain physical quotient and domain debts. Source polarities, ledger0.263, canon and native matter/light obligations remain unchanged. No measured apparatus, novelty, external-expert or proof-assistant certification is claimed. The angular and record theorems from K2510/K2508/K2506 are reused, not counted as new.

## 1. Complete finite circuit

Let H=C108 with unchanged original verifier projectors Q,T. Reuse orthonormal vectors A,B in the existing joint sectors (Q,T)=(1,0),(0,1); their plane reduces both projectors. Define Y_AB=-i|A><B|+i|B><A| on this plane and zero on its orthogonal complement. R_theta=exp(-i theta Y_AB) rotates A to cos(theta)A+sin(theta)B and acts identically on the complement. X_AB swaps A and B and acts identically on the complement.

Retain E=C3 throughout deployment. E0=span(e0,e1), P0=|0><0|+|1><1|; support S=I_H⊗P0 has d=216. Qbar=Q⊗I3,Tbar=T⊗I3. E2 is a known retained out-of-support level, never traced or reset between gaps. There is no extra classical/coherent controller: G=1. All unmodeled retained registers are excluded by the explicit model premise.

Let B_beta rotate memory 1,2 (identity on0), and W_phi=exp(-i M phi Y_01) rotate memory0,1 (identity on2). M is any fixed real number. Put

C_theta = I_H⊗|0><0| + R_theta⊗|1><1| + X_AB⊗|2><2|,
V_(theta,beta,phi)=(I_H⊗W_phi)(I_H⊗B_beta) C_theta.

All three factors are explicit unitaries, hence Xi=Ad_V is CPTP. Only fresh readout/reset ancillas are discarded. The plane's orthogonal complement remains present, so this is an embedded 324-dimensional circuit, not a replacement two-dimensional verifier. It retains coherent memory and has dangerous behavior on the explicitly declared unsupported level.

Pairing positive Hilbert trace; real structure complex adjoint (matrices R,B,W may be chosen real); grading verifier sectors plus memory support; action owner supplied circuit; target calibration of the original Q/T records. No physical Hamiltonian or unit system is inferred.

## 2. Exact supported effects and generator correction

Since B,W act only on memory,

S Xi*(Qbar) S = Q⊗|0><0| + R_theta* Q R_theta⊗|1><1|,
S Xi*(Tbar) S = T⊗|0><0| + R_theta* T R_theta⊗|1><1|.

The rank-two difference on the AB plane has square sin²(theta) I_AB, so

epsilon(theta,beta,phi)=max_R ||S Xi*(Rbar)S-Rbar_S||=|sin theta|.

Moreover

L(theta,beta,phi)=S V*(I-S)V S=sin²(beta) I_H⊗|1><1|,
ell=sin² beta.

Proof: W preserves S, B_beta maps e1 partly into e2, and C_theta preserves each memory population. These operator equalities include coherent memory states and arbitrary untouched references. Scalar mixtures preserve the corresponding operator bounds uniformly over actual and proof-hybrid histories.

For output-frame generators, suppress identities and write G_a=i(partial_a V)V*:

G_theta = W B [Y_AB⊗|1><1|] B* W*,
G_beta = W [I_H⊗Y_12] W*,
G_phi = M I_H⊗Y_01.

For F=Qbar,Tbar, projected cross-block norms are exactly (1,0,0) in coordinates(theta,beta,phi). For support P=S they are

|| (I-S)G_theta S ||=|sin beta cos beta|,
|| (I-S)G_beta S ||=1,
|| (I-S)G_phi S ||=0.

The distinction is essential: the support cross block of G_theta is not zero at nonzero beta. The downstream B conjugation mixes memory1/2. Its uniform bound is1/2 (or the supremum over the declared beta interval). K2510's ambient angular support theorem is valid but loose here. Theta-independence of the compressed leakage follows from the exact L identity; it must not be justified by falsely zeroing the ambient generator. A beta with cos=3/5,sin=4/5 gives cross norm12/25 and is an explicit contrary fixture.

Phi is globally invisible to all three one-gap compressed effects for every M, although it changes memory and later record laws. This removes it only from the per-gap calibration cover, not from physical process identity.

For any two parameter values, direct identities sharpen coverage to

||A_R(theta)-A_R(theta')||=|sin(theta-theta')|,
|arcsin sqrt(ell(beta))-arcsin sqrt(ell(beta'))|<=|beta-beta'|,

where the first equality follows by a unitary conjugation of the AB rank-one projector and the second uses the triangular-wave1-Lipschitz function arcsin|sin beta|. Consequently center allowances epsilon<=a,ell<=b imply throughout a rectangular cell of radii h_theta,h_beta

epsilon<=a+sin(min(h_theta,pi/2)),
ell<=sin²(min(pi/2,arcsin sqrt(b)+h_beta)).

For first formula with large h use sin(min(h,pi/2)); equality above applies actual angular difference but no monotonicity beyondpi/2 is assumed. The phi radius is unrestricted. Support mesh never needs to pay the theta contribution when using the exact compressed identity. This is a genuine structural improvement over merely inserting the ambient norm-sum into K2510.

## 3. Explicit preparation and readout

Generic five-setting preparations can now be implemented on the declared complete D=H⊗E, rather than named abstractly. For R=Q,T choose any fixed known orthonormal basis f_(R,s,j) of its s eigenspace. Their ranks on H are10,98,12,96. Uniformly prepare f_(R,s,j)⊗e_m with m=0,1, giving P_(R,s)⊗P0/(2 rank P_(R,s)). Uniformly prepare all H basis states and m=0,1 for S/216.

A full reset/preparation to any target sigma=Σ_j p_j |v_j><v_j| is explicitly the channel P_sigma(X)=sigma Tr X, with Kraus K_jn=sqrt(p_j)|v_j><z_n| for a complete orthonormal basis z_n of D. Σ_jn K_jn* K_jn=I_D. On any entangled D/reference state it gives sigma⊗rho_reference exactly. A swap with a fresh register prepared in sigma is a unitary dilation; the old contents leave in a discarded register that is never reused. This is assumed available trusted control in the mathematical implementation, not a laboratory inference. It resets all declared retained device memory between calibration shots, but is never inserted between deployment gaps.

Read any projector F=Qbar,Tbar,S using a fresh pointer qubit initially0 and the explicit unitary U_F=F⊗X_pointer+(I-F)⊗I_pointer. Computational pointer readout yields exactly the original Lüders instrument (F rho F,(I-F)rho(I-F)). Discard only the fresh pointer. Private setting selection is made after the frozen map/model parameter has been fixed; the device receives no setting label side channel. All retained D is reset by the preparation, so joint conditional decoupling is actual algebra in this model.

### Structural two-setting implementation

Because the complete circuit family is promised, one prepared state suffices: |A,e1>. Setting E reads Qbar after the gap and marks Q=0 wrong; setting L reads S and marks outside support wrong. They have exact probabilities

p_E=sin² theta=epsilon²,
p_L=sin² beta=ell.

No coherent tomography is needed; both Q and T errors are determined by the same declared AB rotation. This relies on the model, not an inference from two test statistics.

With desired center allowances a,b, put c_E=1/a²,c_L=1/b,W=c_E+c_L and sample setting i with q_i=c_i/W. The pooled wrong bit has

W mu=epsilon²/a²+ell/b.

Thus the inherited fixed-map zero-count confidence rule U_n=1-alpha^(1/n), or its specified anytime version, gives both center bounds when W(U_n+eta_eff)<=1. For N predeclared centers use alpha/N and the standard union bound. With v=1/W-eta_eff>0, a sufficient all-zero count per center is ceil(log(N/alpha)/[-log(1-v)]). This is prospective passing-data effort; it is not a predicted transcript and does not certify model membership.

For comparison, the generic five-sector protocol on the same full supported carrier has W_generic=2d/a²+d/b=432/a²+216/b. It tolerates arbitrary full-carrier maps covered by the effect theorem and costs more because it does not assume this exact defect plane. The structural two-setting reduction does not replace that universal theorem.

## 4. Honest deployment example and anisotropic benefit

To make calibration non-redundant, allow unknown fixed offsets theta0,beta0 in the specified gate family; their exact values are not supplied. Let deployment use theta=theta0+x,beta=beta0+y with declared bounds |x|<=h_theta,|y|<=h_beta, arbitrary phi. The center map uses x=y=0. Parameter stationarity/model membership and the control drift bounds are supplied independent premises. The center calibration determines the two effect/leakage allowances; it does not determine those premises.

Set epsilon_D=ell_D=10^-6, a=epsilon_D/2, b=ell_D/4, h_theta=epsilon_D/2=1/2000000, h_beta=sqrt(ell_D)/2=1/2000. On the one simultaneous center event,

epsilon_D bound: a+sin h_theta<=epsilon_D;
leakage bound: arcsin sqrt(b)+h_beta<=arcsin sqrt(ell_D),

using arcsin(z)-arcsin(z/2)>=z/2. This admits support-angle drift1000 times the effect-angle drift, and unlimited phi range. One anisotropic calibration cell covers the entire declared drift box. An isotropic single-cell choice constrained by effect error would allow beta drift only1/2000000, so it would lose this factor1000 of valid control range. Do not inflate this into a globally optimal net claim.

Here

W=4,000,004,000,000,
W_generic=1,728,000,864,000,000,

so the structural protocol reduces the pooled weight by a factor strictly between431 and432. At zero bias, alpha=1/100, N=1, log100<5 gives the simple sufficient integer count n=5W=20,000,020,000,000. The generic analogous count is8,640,004,320,000,000. These are enormous sufficient passing-data counts, not viable hardware forecasts. If all angles including offsets were already known exactly, the operator identities would certify them directly and no samples would be mathematically necessary; say this explicitly.

For a general rectangular parameter region of side lengths L_theta,L_beta, a conservative endpoint grid with spacings h_theta,h_beta has N<=(ceil(L_theta/h_theta)+1)(ceil(L_beta/h_beta)+1), independent of phi. All its centers still need to pass their respective allowance tests. The broad [0,1] angle box cannot honestly pass uniformly at epsilon_D=10^-6 because it contains theta=1. Net cardinality alone is not a feasible uniform certificate.

With unchanged original Q/T instruments/flags, full retained E and every actual/hybrid gap in the stated family or convex hull, the two-gap complete-record consumer gives

E_record<=1024epsilon_D+1024sqrt(epsilon_D ell_D)+ell_D=2049/10^6.

If ideal acceptance>=1/2 and ideal bad-and-accepted mass0, conditional error<=2049/497951<1/200. Confidence failurealpha is separate from this within-event record error. Neither postselecting a passing transcript nor treating probability1-alpha as conditional confidence is licensed. For arbitrary retained memory evolution the full-carrier operator guarantee, not a memory-reset fiction, supplies history coverage.

## 5. Contrary controls and follow-through

1. **Invisible one-gap phi is not record invisibility.** Set beta=0; initial A⊗e0. First gap with arbitrary theta followed by Q gives Q=1 exactly; W_phi creates cos(Mphi)e0+sin(Mphi)e1. In the second gap the controlled R_theta makes Q=0 probability sin²(Mphi)sin²theta. The second W is memory-only and cannot alter this Q marginal. Thus two choices of phi have identical one-gap effect operators and calibration data but different two-gap records. At theta=pi/2 and Mphi=pi/2 the change is total. Uniform per-gap bounds still apply; never claim process equality.

2. **Unsupported memory matters.** Set theta=phi=0; initial A⊗e1. First gap has exact supported Q/T effects, but leaks with probability sin²beta. A Q test remains1. The next C_theta applies the A/B swap on e2, so second Q wrong probability is exactly sin²beta. Tracing E or declaring it freshly reset would miss this. It supplies a concrete consumer for the support-leakage budget.

3. **Two settings require the structural promise.** Select u in Q=1 and v in Q=0 orthogonal to A,B (possible from original ranks). A unitary swapping u,v and fixing A,B and E leaves both structural calibration test probabilities zero at center, but has full supported Q effect defect1. The generic five-sector protocol detects it. This refutes any model-free dimension-independent claim for two tests.

4. **Suffix support bound.** At beta with cos3/5,sin4/5, the ambient theta support cross norm is12/25, not zero, even though compressed leakage is theta-independent. This directly tests the weakest proof seam.

5. **Unknown model/generator drift.** Agreeing with the supplied circuit during calibration then swapping A/B in deployment remains undetectable from calibration data alone. Similarly a settings side channel invalidates pooled common-map identification. Neither is ruled out by the finite matrices.

6. **Reset versus deployment.** Verify the full reset channel removes D/reference correlations; then explicitly omit it between the repeated-memory control gaps. Resetting deployment would give a different process and erase the intended contrary example.

The immediately released robust extension is proved below.

## 6. Follow-through: robust two-setting certificate with nonzero full-carrier perturbation

The two-setting savings extend to an explicitly bounded neighborhood of the circuit family. It retains the spectator rejection control and prices an independently trusted norm bound.

At the center, let the actual unitary U_c on the complete324-dimensional retained carrier satisfy ||U_c-V_(theta0,beta0,phi0)||<=eta_c. For each actual or proof-hybrid deployment history, its actual unitary U_d obeys ||U_d-V_(theta0+x,beta0+y,phi)||<=eta_d, with |x|<=h_theta,|y|<=h_beta and arbitrary phi. These are trusted full-carrier norm bounds uniform over the relevant histories, independently supplied rather than inferred from two settings. Initial support and original instruments remain unchanged. The center actual map is fixed before the private setting draw. No extra retained environment is silently excluded.

Let p_E_actual and p_L_actual be the two actual wrong probabilities on psi=A⊗e1. Projection contractivity and the reverse triangle inequality give

|sin theta0|=||(I-Qbar)V_c psi||<=sqrt(p_E_actual)+eta_c,
|sin beta0|=||(I-S)V_c psi||<=sqrt(p_L_actual)+eta_c.

For any projector F and unitaries U,V, ||U*FU-V*FV||<=min(1,||U-V||). Proof: for any unit vector psi, the absolute probability difference is bounded by half trace distance of Upsi,Vpsi, which is sqrt(1-|<Upsi,Vpsi>|²)<=||Upsi-Vpsi||; take the supremum of the Hermitian quadratic form. The same holds after support compression and reference amplification. This avoids the unnecessary2eta effect triangle bound.

Therefore if the pooled actual data certifies p_E_actual<=a² and p_L_actual<=b, every deployment history satisfies

epsilon_actual <= a+eta_c+sin(min(h_theta,pi/2))+eta_d
                 <= a+eta_c+eta_d+h_theta,

sqrt(ell_actual) = ||(I-S)U_d S||
                 <= ||(I-S)V_d S||+eta_d
                 = |sin(beta0+y)|+eta_d
                 <= sqrt(b)+eta_c+eta_d+h_beta.

Square the last quantity and cap by1. The final leakage step uses |sin u-sin v|<=|u-v| and the reverse triangle for |sin|; no arcsin branch needs to be reconstructed from data. Uniform actual channels may also be historywise classical mixtures of unitaries satisfying these bounds, by positivity and linearity of the effects. No single actual-unitary description is needed for that convex extension.

Pooling still uses W=1/a²+1/b, now for the actual wrong means. Keep trusted joint preparation/readout probability bias xi_eff separate from eta_c/d: statistical margin is1/W-xi_eff; norm perturbation is charged in the deployment allowances. Counting the same imperfection twice is unnecessary only if its ownership is explicitly identified. Never call the norm-bound premise a consequence of two-setting calibration.

### Concrete nonzero-perturbation consumer

Set epsilon_D=ell_D=10^-6, a=epsilon_D/2,b=ell_D/4, eta_c=eta_d=epsilon_D/16, h_theta=epsilon_D/4,h_beta=sqrt(ell_D)/4. Then

a+eta_c+eta_d+h_theta=7epsilon_D/8 < epsilon_D,

sqrt(b)+eta_c+eta_d+h_beta=3/4000+1/8000000=6001/8000000<1/1000,

ell_actual<=36012001/64000000000000<10^-6.

The same W=4,000,004,000,000 and sufficient zero-bias count20,000,020,000,000 atalpha=.01 apply. The unchanged complete-record and postselection ceilings2049/10^6 and2049/497951 therefore hold on the confidence event. This example has strictly nonzero perturbations, so it is not merely the exact-family theorem relabeled robust.

The spectator swap remains the strongest rejection control: relative to the center modeled identity on its spectator subspace it has operator distance2, even though both test bits remain zero. Thus it violates any small full-carrier eta promise. An actual perturbation confined to spectators can be invisible to the two settings; it is bounded only through the trusted eta assumption. A small spectator rotation of anglez instead has norm distance2|sin(z/2)| and supported Q defect|sin z|, illustrating a nonzero tolerated unobserved defect.

Next condition after this follow-through: obtain independent physical evidence for full-memory reset/readout and the full-carrier perturbation/drift bounds, or build a stronger test that certifies a stated restricted perturbation class without assuming its norm bound. No two-setting dataset alone can control arbitrary spectator dynamics. Native GU realization remains a separate construction.

## Evidence and remaining limits

The exact probe checks reducing-plane matrices, full reset and pointer instruments, retained-memory countercontrols and rational resource margins. The written reducing-subspace and operator arguments cover the full324-dimensional model and untouched references; finite fixtures do not establish arbitrary apparatus behavior. Independent internal review checks the actual arguments and probes. Statistical confidence failure remains distinct from within-event record error.

[Exact probe](../../tests/channel-swings/k2512_finite_memory_implementation_probe.py), [saved report](../../lab/process/k2512-finite-memory-implementation.json), [K2510 angular theorem](k2510-effect-path-calibration-2026-11-02.md), [K2508 full-carrier coverage](k2508-controller-coverage-2026-11-02.md), [K2506 record consumer](k2506-calibration-deployment-transfer-2026-11-02.md).
