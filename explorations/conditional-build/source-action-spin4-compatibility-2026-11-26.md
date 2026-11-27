---
title: Reached spin4 auxiliary compatibility at both stationary backgrounds
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Decide whether the two actual reached spin4 sources lie in the native auxiliary image at both certified W2 roots
actual_delta: Both actual reached spin4 sources have native auxiliary preimages throughout both certified kappa1 root boxes, in an exact282-dimensional envelope invariant under all59 background maps. This candidate necessary condition survives; GU is not falsified.
class_covered: Held W2/K95 action, pairing and time kernel; a source-containing finite envelope over all59 affine background coefficients, evaluated at both kappa1 roots
premises:
- 'source-normal-tensor-class-2026-11-26.md sections6.1–6.7: actual full-R connection and two reached spin4 sources'
- 'source-action-weak-response-2026-11-26.md: native M, time-kernel projector, completed spin5/6/7 receivers'
- 'source-adjoint-spinless-placement-2026-11-26.md: primary-minus/plus-comparator custody correction retained'
source_bridge:
  status: conditional
  reason: These are genuine sources for differentiable full-range auxiliary elimination on the directed W2 reconstruction; neither W2 nor unrestricted full-R elimination is source-required.
kill_condition: Only a genuine native adjoint-kernel obstruction at an actual certified root would exclude the stated candidate realization; missing old-envelope coverage is not an obstruction.
---

# Reached spin4 auxiliary compatibility

program_target: LB-CLASS
tier: T2
expected_delta: True native image membership or a certified incompatibility for the two reached sources
actual_delta: Both actual reached spin4 sources have native auxiliary preimages throughout both certified kappa1 root boxes, in an exact282-dimensional envelope invariant under all59 background maps. This candidate necessary condition survives; GU is not falsified.

```gu-typed-objects
result: native reached-spin4 auxiliary image test
carrier: W2 K95 endomorphism-valued one-forms and N=ker K_dt LAYER=ambient BRIDGE=held-candidate-equations CHIRALITY=S-FULL-DIRAC
pairing: native nondegenerate indefinite form defining P and M ON=declared_carrier
real_structure: inherited W2 Clifford conjugation; no positive physical norm or source Sp identification
grading: imaginary Clifford degrees0,3 mod4; rotation highestweight4 is not physical particle spin or a family count
action_owner: repository-construction source-action W2 at fixed kappa1 stationary roots
target: M=N-to-N auxiliary map and actual connection-generated source MAP-TYPE=homomorphism
```

## Scope and selection

Basis: fetched clean `3e8fa792e93e8a58e804364c842080a7e6c72810`. Joe's continuing falsification direction selects a fresh compatibility condition. Source relevance remains conditional and class-C representativeness unproved. The strongest source-facing alternative—physical weak/chiral readout—still lacks an admitted common domain, normalization and propagation law. This calculation uses owned finite data and does not wait for or invent those inputs.

The source-specific2+1 distinction, imposter gamma-trace placement, independent fields, observation by contraction, K77 versus derived K95 and total versus physical grading remain unchanged. The printed source minus/conjugation correction is retained: the fixed normal optional-C class is4R, not the plus comparator's zero class. W2 already used its stated minus pairing; the common sign does not authenticate W2 as the source action.

## 1. Actual sources, not missing coverage mistaken for failure

Let P be the native pairing-orthogonal projector onto N=ker K_dt, R=I−P, and J_T=I+2N(T,·). The auxiliary operator is M_T=PJ_TP restricted to N. The59-dimensional affine background family and its two certified stationary boxes are unchanged.

For j=5,12, start from the owned Q7 vector V_j=K_dt b_j and the actual boost rho(H03). Define

    W6_j = (56−Casimir)/14 · R rho(H03)V_j,
    L4_j = Pi4 P K^5 W6_j.

Exact native reconstruction verifies W6 Casimir42, L4 Casimir20, highestweight4, the raising equation, P L4=L4 and K_dt L4=0. W6 supports are128/192; L4 supports344/472. The displayed coefficients are `(form1,Clifford759)=−i/18` and `(form1,Clifford5735)=4/15`. Axis8 gives i times axis5. These are the actual previously exhibited connection-generated sources. Solving them is a necessary condition for the full-R construction, not sufficient construction of it.

## 2. Why covariance does not solve this automatically

Assume [rho(A),K_b]=K_(A·b), PK_bP=0, [rho(A),J]=0 and PK_bV=MY with Y in N. Direct expansion gives

    P K_b R rho(A)V = M P rho(A)Y
      + P J R rho(A)Y − P rho(A)R JY
      − P K_(A·b)V + P rho(A)R K_bV.

The two J terms are P{J,[rho(A),P]}Y: an **anticommutator**, not a commutator. For the spin4 projection and old spin5 solution Y5, the K_(A·b) term vanishes by rotation weights, but the remaining cross terms need not cancel. The numerical covariance trial at root0/source0 has relative residual about0.02117 after the old full-native solve residual is below5e−16. This declines a shortcut; it is not evidence that L4 lies outside the image.

A small exact countercontrol makes the logical limit explicit. Take a Lorentz space H and F=Sym²(H*)⊕H*, with K_b(S,v)=(b⊙v,−i_(b#) S). For timelike tau, N is spatial Sym². Set J_S S=S−(1/3)g tr_g S and J_H=I. J is invertible and Lorentz-equivariant, but its compression M removes the spatial trace. V=(0,tau) has all old PK_bV=0. After a boost taking the covector tau to e^1 and b=e^1, the new source e^1⊗e^1 has nonzero spatial trace and is not in imageM. Thus the stated covariance hypotheses alone cannot transport solvability. This is a general finite counterexample, not a counterexample to W2 or GU.

## 3. Exact source-containing envelope

Numerical solves are used only to propose a4032-coordinate support. Exact simultaneous kernel elimination for K_dt, weight4 and the raising operator on that support has constraint rank3750 and dimension282. Both exact sources reduce into the resulting echelon basis. The complete highestweight4 multiplicity in the full admissible carrier is2604; the282-dimensional envelope is not claimed to exhaust it.

For every basis vector and each of59 background directions, compute the **full native** image A_k v=2PN(T_k,v) and reduce it against the basis. Zero remainder proves invariance. This uses all16638 exact reductions; it is not a projection of images with discarded remainders. The identity preserves the envelope, so M_T does too for the entire affine family.

**PASS:** all282×59=16638 full-image reductions vanish exactly. The envelope is invariant over the entire affine59 family.

## 4. Root-box certification

A floating inverse is only a proposal for a rational matrix B. Exact Gaussian-rational arithmetic checks eta0=||I−BM(center)||_infinity, using abs(real)+abs(imag) coordinate bounds. For the certified uniform59-coordinate radius r, bound the perturbation by

    eta_delta = r max_i sum_j |B_ij| sum_(k,l) |(A_k)_jl|.

If eta=eta0+eta_delta<1, a finite-dimensional Neumann argument proves M_T invertible on the envelope throughout the box. Thus every source in that envelope, including both exact L4_j, has a true native preimage. This does not require M to be invertible on allN, nor does it assume a physical positive pairing.

**PASS at both roots.** Exact rational bounds are in the certificate; displayed decimals are summaries.

| Root | Neumann bound eta | Sources with certified preimages |
|---|---:|---:|
| 0 | 1.39333e-06 | 2/2 |
| 1 | 1.58449e-05 | 2/2 |

Both bounds are below1 throughout the owned boxes. This is a positive range-membership result, so these sources do not supply a candidate obstruction.

## 5. Exact implementation and verification

The optimized engine changes arithmetic representation only. With L=lcm|d_a|=48, Dphi=2L²=4608 and Dadj=2L=96, the three cubic terms have common denominator6Dphi du dv. Fusing2PN uses denominator3Dphi du dv. Gaussian-integer pairs replace intermediate Fraction operations; rational output is restored exactly. The native projector remains P=Z G^−1 ZᵀW on each28-coordinate time block. Separately denominator-cleared Z, G^−1 and ZᵀW are applied as three sparse integer matvecs. No dense approximate projector, changed domain or altered pairing is introduced.

The first closure column matches the original native exact engine for all59 maps. Arithmetic controls and independent review are recorded below. Data-only certificates are stored in [certificate bundle](../../lab/process/source-action-spin4-certificates.json); the [probe](../../tests/program-focus/source_action_spin4_compatibility_probe.py) checks byte bindings and rejects incomplete closure. Local scratch caches are reproducible outputs, not additional source truth.

Controls:161 integer-cubic,190 native-projection and2856 covariance premise checks;14 exact Neumann/parser controls. Native basis replay checks4×282=1128 equations plus independent echelon pivots and both source memberships. Independent T2 mathematical/source review passed. Native gates are recorded in the evidence.

### Repeated-test tools

From the repository root, use the existing Python/NumPy/SciPy environment and a local cache. Run heavy modes serially.

```sh
python tests/program-focus/source_action_spin4_compatibility_probe.py --repo . --cache _local/spin4 --mode unpack
python tests/program-focus/source_action_spin4_compatibility_probe.py --repo . --cache _local/spin4 --mode controls
python tests/program-focus/source_action_spin4_compatibility_probe.py --repo . --cache _local/spin4 --mode certify
python tests/program-focus/source_action_spin4_compatibility_probe.py --repo . --cache _local/spin4 --mode status
```

`certify` rechecks native basis/source equations and exact inverse bounds using frozen rational preconditioners; it does not rerun numerical discovery. `integer-closure --steps N` resumes N additional columns only when all implementation/input bindings match; use0 for all remaining columns. To reproduce closure from scratch, unpack into a fresh cache and remove only its generated closure record before replay. `benchmark` compares identical native and optimized2PN maps. `--generate-candidates` is an explicit discovery option; never required for ordinary replay.

Warm benchmark on three actual background directions: 64.35× faster on this machine (0.130s versus 0.002s), with exact equality. Timing is hardware-dependent. The reusable `IntegerScaledN`, `IntegerKernelProjection` and `projected_cubic` helpers retain immutable prepared inputs; altering a prepared input invalidates that API contract.

## 6. Three-state result and continuation

- **ESTABLISHED:** Both actual reached spin4 sources have native auxiliary preimages throughout both certified kappa1 root boxes, in an exact282-dimensional envelope invariant under all59 background maps. This candidate necessary condition survives; GU is not falsified.
- **RULED OUT:** automatic inference of compatibility from covariance alone, under the explicitly displayed general hypotheses. No GU or source-required class exclusion.
- **NOT MODELED / UNDETERMINED:** full-R auxiliary solvability, remaining first-jet source components, physical admission/quotient/normalization/propagation, and source necessity of this W2 reconstruction.

The two reached spin4 source tests are consumed. The next ready discriminator checks the two horizontal Nomizu spin4 representatives against E4 and the actual spin5 remainder against E5, followed by a bounded census of the generated first-jet sources modulo E4/E5/N6/N7. Prove the chosen representatives span the actual source maps before declaring completeness. A nonzero quotient is an uncovered source, not a cokernel obstruction. This does not authorize automatic inversion of lower blocks. The physical weak-readout alternative retains its exact missing-input condition.

No scientific matrix cell, source/physics/canon/class-C verdict or paper changes. Choice budget remains10 grouped choices/4 obligation bundles/net6/zero source-selected predictions; these are candidate bookkeeping counts, not a lower bound for GU. The20 mathematical descriptions, including category theory and number theory, are one quick reassessment pass, not20 independent experts or a vote. Concrete derivation and independent review are separately identified in the evidence.

## Later prioritization consideration

The Nov26 memo usefully emphasizes fresh response/stability content and avoiding repeated floor proofs. Kappa1 existence is already certified at two roots in the59-dimensional fixed family; a certified path from the smallh branch to those roots remains unproved. The present local tests do not need that path. Source-necessary class tests remain eligible when supplied; a single candidate is not GU. Concrete errors must still be corrected when found. This consideration changes no program_focus policy, schedule, canon or publication.
