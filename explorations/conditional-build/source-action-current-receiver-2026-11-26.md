---
title: 'Constraint-mediated matter current and the surviving PT matter domain'
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Test the existing positive matter current on the owned constrained energy receivers and distinguish the existing symmetries from a positivity prescription.
actual_delta: Both roots have a certified nonzero same-injection current on their complete spin6/7 derivative constraint responses, although the tested range receivers vanish. Pure quaternionic conjugation reverses the selected charge; full PT preserves the primary constant-seed positive matter domain without selecting its dispersion. Physical negative-energy excitation remains undetermined.
class_covered: Held W2 K95 fullU SE=-1/2 candidate at both certified kappa1 roots; canonical zero-normal injection and primary constant-seed finite-band matter completion. Pointwise auxiliary receivers use complete spin6/7 inverse certificates; unrestricted compact constrained data additionally require full auxiliary regularity.
premises:
- explorations/conditional-build/source-action-variable-completion-2026-11-25.md
- explorations/conditional-build/source-action-reduced-evolution-2026-11-26.md
- explorations/conditional-build/source-action-graph-domain-2026-11-26.md
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
- lab/active-research/joe-directed/external-results/pt-mannheim-applicability-2026-11-26.md
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-02
- lab/sources/source-claim-register.yaml#SC-META-53
source_bridge:
  status: absent
  reason: The source motivates the action and indefinite-spectrum question but does not select this repaired candidate, its injection, dispersion, physical domain or probability rule. No source-necessary exclusion follows.
kill_condition: Exact signs exclude only identification of coefficient conjugation with a positive fundamental symmetry and invariance of the nonzero positive-charge graph under pure quaternionic conjugation. Receiver failure or success does not settle physical propagation or GU.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-CURRENT-RECEIVER-AND-PT-DOMAIN
internal_target_verdict: Pure quaternionic conjugation is not a symmetry of the chosen positive-charge graph; full PT is a surviving symmetry of its primary constant-seed member. The exact auxiliary current receiver is nonzero at both roots.
canon_verdict_change: none
---

# Constraint-mediated matter current and the surviving PT matter domain

## Result and ceiling

**The constraints expose a matter-current channel missed by the direct range-amplitude test.** At both existing coupling-one roots, the direct tested receiver vanishes, while its complete derivative-induced auxiliary response has a certified nonzero current. The result survives the actual allowed cross-Gram normalization, with the same injection and tube. It is a pointwise variational coupling result, not a negative-energy propagator or runaway theorem.

There is also a constructive distinction. The existing pure quaternionic operation reverses the selected positive charge, but adding the already-owned full spacetime reflection preserves the primary positive matter domain. This uses the same band, tube, injection and arbitrary real dispersion. **PT compatibility does not select a dispersion or cure the coupled bosonic domain.**

```gu-typed-objects
result: actual current receiver and existing symmetry/domain compatibility
carrier: TstarY tensor u64_64 and (TstarY tensor S) plus S LAYER=ambient BRIDGE=physical_observation_unproved CHIRALITY=N/A
pairing: native real trace/form pairing; independent density-dual matter row; existing positive amplitude norm ON=declared_distinct_carriers
real_structure: K95 fullU; imaginary-Clifford connection variations and existing quaternionic Jq
grading: coefficient reality and geometric SO3 weight; neither physical spin nor chiral index
action_owner: repository-construction W2 I1B-style construction with SE=-1/2 and independent bars
target: action-current receiver and selected linear-matter domain MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING.** `INTERNAL_STRUCTURAL_ONLY`; read `lab/methods/source-native-comparator-routing.md`. Canonical energy, pointwise Krein sign, phase charge and quantum probability are different objects. K95/K77, fullU/conditionalSp, contraction/projection and candidate/source remain distinct. No standard three-family, compactification or adjoint-bar assumption enters.

**Source relevance.** SC-ACT-01/02 motivate the reconstructed variational problem. SC-META-53 explicitly records uncertainty about unbounded spectra and a proposed compact shielding mechanism; it does not supply the domain or quantization tested here. Class-C representativeness and source necessity remain unproved. The weakest physical link is an admitted coupled state space, physical quotient and actual propagated response. Full auxiliary regularity remains conditional beyond the certified 1,904 of 49,154 auxiliary components.

## 1. Preflight and fixed objects

Target LB-CLASS, with LT-SM8/LT-GR6b relevance. T2 receiver/domain result; T1 internal symmetry exclusions receive two mathematical reviews, hostile review and a finite Lean core. The explicit directed task takes the existing packet5o test. No new action, parity, state restriction, contour, frequency band or completion is chosen.

Use the **canonical injection** I: observed four one-form spinors and scalar into the ambient field, with all normal one-form components zero. This is `inject` in `source_action_slice_completion_probe.py`, not an arbitrary right inverse of observation. Let q be the same literal adapted contraction, A^t the actual SE=-1/2 time coefficient, and V_s(a) the full connection vertex, including its southeast term. The constant-seed construction supplies F, V and

    N(k) = integral_Omega V A^t F dy,
    Vtilde = N^-1 V,
    ||N/Vol(Omega)-Id||op < 1/2.

The coordinate density is already absorbed in the independent row eta. The paired matter fields have eta=i times the normalized dual and positive phase charge. A different injection or optional oscillatory normal seed is not silently substituted.

## 2. Complete auxiliary receivers at both roots

For a real Clifford-coefficient connection variation u, define the exact section matrix

    B_u = q (A^t)^-1 V_s(u) I.                       (1)

For the physical imaginary variation a=i u, the selected diagonal variational current at the seed section is governed by

    -Herm(N(k)^-1 B_u),                              (2)

not by B_u alone. The minus is the product of the existing +i density-dual phase and the physical i in a. Off-diagonal frequency pairs use their actual polarized kernel.

Reconstruct the complete spin6 kernel and the lowered spin7 kernel using the earlier native bases. Reuse the exact rational inverse centers, Neumann bounds and hashes from the kappa1 certificates. With xi=theta0 and tau=theta3, use

    v_A = K_tau b12,     v_B = K_tau b5,
    n = -M^-1 P K_xi v.                              (3)

The derivative source lies entirely in geometric rotation spin6/7; therefore the completed inverse in (3) requires no lower-spin inverse. These labels are not physical particle spins. Both components are included, rather than retaining only an observed spin6 receiver.

The calculation gives **B_v=0** for both tested range amplitudes. In contrast B_n is nonzero on each real and imaginary component. Representative real-component coefficients, with zero-based observed matrix indices, are:

| Root / range amplitude | B_n entry (row, column, Clifford mask) | Center | Rigorous error upper bound |
|---|---|---:|---:|
| A / K_tau b12 | (3,0,9833) | +7.12225937489e-6 | 3.397626e-6 |
| B / K_tau b5 | (3,0,9785) | -2.93940098371e-4 | 1.661176e-5 |

Acceptance uses the exact rationals in the evidence file; decimals are displays. The imaginary partners have masks10057 and10009 and are separately certified. The inverse columns preserve nonzero geometric weight6. The invariant bilinear self-pair and force-response pair at weight12 vanish, so the real and imaginary components have equal halves of the certified negative derivative-energy form. The probe checks these identities and each negative interval. It does not infer real negative energy from an arbitrary complex current component.

### 2.1. Why the actual Gram cannot erase this receiver

The first naive whole-matrix error estimate was too coarse. It is retained as a failed method control, not a failed current test. An exact structural identity removes that bottleneck.

On the complete real image of the spin6 plus lowered-spin7 auxiliary receiver, there are32 nonzero generating vectors. All528 polarized normalized trace products satisfy

    tr(B_i B_j)=0.

The scalar trace uses the faithful128-dimensional Clifford representation. Distinct blades are orthogonal in its existing positive coordinate Hilbert–Schmidt norm; their squared weights are product |d_a|. Hence every real B in this image, including the exact root-ball receiver, obeys

    Re tr(B^2)=0,
    ||Herm B||F^2 = ||B||F^2/2.                       (4)

This is a finite receiver-class identity, not a numerical ratio at the root center. The root certificate only has to establish B≠0, which the separated coefficient above does.

Write N=c(Id+E), c=Vol(Omega)>0 and ||E||op<1/2. If Herm(N^-1 B)=0, multiplying by N and N† gives

    B+B† = -(B E† + E B†),
    ||Herm B||F <= ||E||op ||B||F < ||B||F/2,

contradicting (4). Thus (2) is nonzero for **every existing allowed cross-Gram**. There is no tube shrinking or new normalization. The Hermitian form has a vector with nonzero diagonal value; continuity in the actual CK kernels gives a local nonzero current. Finite-band amplitudes can realize that local nonzero bilinear by polarization and localization in a positive-measure frequency subset. This is existence of selected-matter current on the named auxiliary test, not a claim about every matter state or an integrated negative-energy packet.

### 2.2. What remains between this result and instability

For a full constrained homogeneous variation, let D=P H_sp|R and d=M^-1 D. Its auxiliary part is -dv, including lower-order and moving-frame terms. The reduced current is the graph pullback

    ell(v-dv),    j_eff = j_R - D† M^-1 j_N,          (5)

with adjoints defined by the same action pairing and integration domain. A nonzero component in (3) does not evaluate all of (5). Even nonzero work on a negative-energy vector would not by itself show negative energy of the forced response: with energy diag(1,-1), source(1,0) pairs with the negative vector(1,2) while forcing only the positive coordinate.

There is also an exact frequency constraint. The held matter band is compact K; because the background and normal kernels are base-translation invariant, its quadratic current has base momentum support in K-K. The existing negative-packet theorem uses a high-frequency principal limit. It has not been shown that the held K-K reaches a negative-energy response with a compatible normal profile. Enlarging K changes the chosen completion member and is not performed here.

**ESTABLISHED:** same-I normalized auxiliary current is nonzero at both roots; direct tested range current is zero; finite root-certified receiver class is not shielded by that normalization. **NOT MODELED / UNDETERMINED:** full inhomogeneous reduced response, accessible negative-energy excitation, physical cohomology, admitted propagation and nonlinear exchange/runaway.

## 3. Existing coefficient conjugation is not a positive fundamental symmetry

Denote the spinor quaternionic map by Jq=C conjugation; reserve I for the observation injection. The induced coefficient involution is tau. The native bosonic pairing is b=-Re tr/128 with the K95 inverse one-form metric. For X_a=i theta_a Id,

    b(X_0,X_0)=+1,     b(X_3,X_3)=-1,
    tau X_a=-X_a,
    b(X_0,tau X_0)=-1, b(X_3,tau X_3)=+1.

Thus using tau to turn this owned pointwise form positive is **RULED OUT**. This form has not been identified with a quantum Wightman norm. No exclusion of every possible physical parity follows.

Nevertheless the bosonic action is tau-invariant: Phi has zero or two explicit i factors, and real trace, geometry and density commute with conjugation. Odd-tau cubic polarizations vanish. For the independent matter row and column, the symmetry is

    a' = C conjugate(a) C^-1,
    psi' = C conjugate(psi),
    eta' = conjugate(eta) C^-1.

Jq commutes with real Clifford generators, so all four native vertices intertwine and eta' V(a') psi'=conjugate(eta V(a)psi). The real interaction is invariant. Deriving eta from psi†H instead would insert an extra minus because Jq reverses the Krein form; that is a different row law.

Without time reflection, Z=integral eta A^t psi is conjugated. Therefore Q=Re(-iZ) changes sign. Since every nonzero state in the held positive graph has Q>0, **pure Jq does not preserve that graph**. This is a scoped internal exclusion, not quantum inconsistency or a source verdict.

## 4. Full PT survives on the primary selected matter domain

Take the already-owned full-base inversion x->-x and U=gamma0123, with Theta=U Jq. The exact inherited square laws are U²=-Id, Jq²=-Id and Theta²=Id. Include the horizontal one-form signs on zeta, with no extra sign on nu.

Full base inversion fixes the metric fibre: (-Id)^-T y (-Id)^-1=y. It fixes the normal CK hypersurface and every existing tube Omega. The induced operator in the adapted analytic trivialization is constant; the central -Id base action commutes with the homogeneous frame construction. Naturality of the actual d_A,delta_A and Clifford maps, and invariance of the entire59-family under this reflection, supply full lower-order covariance. The native probe checks all15 columns for each of14 principal axes and the same q/I seed intertwining. This is not an inference from the square-zero bosonic symbol.

Write Theta_col=T conjugation, Theta_obs=T_o conjugation. These matrices are unitary in the existing coordinate amplitude norm; that fact selects no physical bosonic metric. On the canonical injection and literal readout,

    T conjugate(I)=I T_o,     q T=T_o conjugate(q),
    A^t T=-T conjugate(A^t),
    A^i T=-T conjugate(A^i),  A^normal T=T conjugate(A^normal).

For a different trivialization, retain the corresponding derivative-of-T terms in the lower-order covariance identity. The present argument uses the stated adapted trivialization, not constant matrices in an arbitrary frame.

The Fourier phase exp(i(k.x-omega(k)t)) is unchanged by conjugation together with full base inversion. At the SAME real spectral parameter, uniqueness for the actual analytic CK problems with seeds F=I and V=q(A^t)^-1 gives

    F=T conjugate(F) T_o^-1,
    V=-T_o conjugate(V) T^-1.

The minus in the row equation is forced by the time coefficient. Since the tube is fixed,

    N=T_o conjugate(N) T_o^-1,
    Vtilde=-T_o conjugate(Vtilde) T^-1.

The Gram is not assumed Hermitian. The existing left normalization is essential. Conjugating the +i row phase contributes one minus; the row identity contributes the other. Consequently the existing paired domain maps to itself with amplitude

    a'(k)=T_o conjugate(a(k)).

This is an antiunitary involution, preserving Q and E and reversing the real symplectic form. It works for every held compact K and every bounded real omega(k); neither K=-K nor an even omega is required. Thus this PT test selects **no dispersion**.

The statement covers the primary constant-seed member with canonical I, or another explicitly intertwining seed. An arbitrary right inverse maps to I'=T conjugate(I)T_o^-1 and need not stay fixed. The optional earlier oscillatory normal seed changes its phase c->-c and is not covered by this invariance claim. No paired-profile extension is introduced.

**ESTABLISHED at internal mathematical grade:** full PT preserves the declared primary linear positive matter completion. **NOT MODELED / UNDETERMINED:** invariance of a nonlinear coupled domain, positive bosonic norm, scattering states, spectral propagator and physical probability rule. The unrestricted bosonic graph obstruction remains unchanged.

## 5. Bateman–Turok transfer and continuation

The [Bateman–Turok scalar construction](https://arxiv.org/abs/2607.00096) uses an indefinite quantum state space, covariant process projections and weak ghost symmetry. The [November thesis](https://doi.org/10.7488/era/8017) retains the distinction between tree positivity, optical identities and the unresolved full-gravity extension. Our classical tau or PT identities do not supply those objects. Earlier GU ghost-parity and loop-scope analyses remain evidence; this result tests the newly built candidate rather than claiming the mechanism was undiscovered.

The next concrete receiver question is (5) at transfer frequencies already in K-K, with the existing normal profile, followed by an actual admissible propagation/physical-quotient test. This replaces the inference that another generic nonzero current would settle instability. Higher derived graph domains remain a separate uncovered part of packet5o. No new choice family is added to make either test pass.

## 6. Verification and postflight

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Same-injection current receiver and existing symmetry/domain test.
actual_delta: Nonzero complete derivative auxiliary receiver at both roots; pure J excluded on positive charge; full PT preserves the primary graph and leaves dispersion free.
```

- Exact sparse native probe: same I, q, all four vertices; central identity and omitted-SE negative control; inherited inverse/Gram hashes; complete6/7 derivative response; root-ball nonzero coefficients; realification and polarized trace identity; native PT symbol/injection, independent-bar and charge controls.
- Six Lean lemmas check finite charge signs, the positive-graph contradiction, norm-margin arithmetic, the work/energy counterexample and bounded difference frequency. They do not formalize CK, the full PDE, the physical quotient or the native inverse certificates.
- Independent mathematical and hostile reviews, exact replay and native gates are recorded in the linked review/evidence artifacts. Internal agent review is not external peer review.
- Choice accounting remains10 grouped families,4 grouped viability bundles,bookkeeping net6; no new complete viability bundle, source-selected prediction or GU necessity bound. PT invariance is a newly checked property of an existing bundle, not a new selection law.
- Scientific matrix/source/physics/canon/paper verdicts, program_focus and schedules unchanged. One directed run increments count58->59 and LBCLASS17->18; no shrinkage or bet credit, pending ordinaryLC retained.

[Machine evidence](../../lab/process/source-action-current-receiver.json) · [Probe](../../tests/program-focus/source_action_current_receiver_probe.py) · [Lean finite core](../../Lean/GUFormalization/CurrentReceiver.lean) · [Review](../../lab/process/hostile-reviews/2026-11-26-source-action-current-receiver-review.md)
