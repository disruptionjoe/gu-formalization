---
title: 'Symmetry selects the extension geometry, but not observed dynamics'
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Classify which constant-hyperplane observation seeds can support nonconstant covariant states and decide whether covariance selects observed dynamics.
actual_delta: Non-invariant seed hyperplanes force base-constant solutions. Lorentz covariance uniquely leaves the trace hyperplane within this class; it admits every analytic observed history through an equivariant local right inverse.
class_covered: Analytic first-order column systems in the homogeneous equivariant exponential metric-fibre frame, with invertible nonnull rolled symbol, literal observation and constant injective seed on a linear normal hyperplane. The full metric-fibre symbol obeys diagonal horizontal scaling A_h^mu(diag s)=exp(s_mu)A_mu; complete lower coefficients obey central trace-shift covariance. Includes the held K95 fullU SE=-1/2 operator at both invariant roots and the invariant displacement family; not all source actions or all extension rules.
premises:
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
- explorations/conditional-build/source-action-variable-completion-2026-11-25.md
- explorations/conditional-build/source-action-paired-response-2026-11-26.md
- lab/sources/source-claim-register.yaml#SC-GEO-03
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-META-53
source_bridge:
  status: absent
  reason: The source asserts the metric-bundle arena and candidate four-field grammar, but does not select this repaired operator, exponential-frame constant seed or physical domain. Observed covariance motivates the diagnostic; no source-necessary contradiction follows.
kill_condition: Exclude nonconstant naturally covariant states only within the specified constant-seed operator class. A non-invariant seed cannot be repaired by restricting polarizations, changing dispersion or changing its norm. Different extensions, physical quotients and source GU remain outside.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-CONSTANT-SEED-COVARIANCE
canon_verdict_change: none
---

# Symmetry fixes where to extend, not what happens

**Within the declared constant-hyperplane seed class, Lorentz covariance forces a unique geometric location: the fixed-volume metric hypersurface. Yet the surviving local extension admits every analytic observed spacetime history.** Covariance therefore does not supply the missing law governing those histories.

The previously used off-diagonal seed is excluded more strongly than before: even rotations in one spatial plane leave it no nonzero rotation-stable spatial-L2 subspace. Arbitrary momentum-dependent polarizations, a relativistic dispersion, PT restrictions or a different positive norm cannot repair that same field space. The result does not establish a physical ghost or falsify GU.

```gu-typed-objects
result: symmetry rigidity and covariant observation right inverse
carrier: analytic sections of (TstarY tensor S) plus S; observed (TstarX tensor S) plus S LAYER=ambient BRIDGE=physical_domain_unproved CHIRALITY=N/A
pairing: no positivity assumption; native trace-reversed vertical metric used only for conormal typing ON=declared_carriers
real_structure: real metric-fibre matrices and complex K95 fullU spinors; independent dual row remains separate
grading: tensor and Clifford structures, not observed chirality or family count
action_owner: repository-construction held W2 SE=-1/2 column operator; homogeneous invariant displacements
target: Lorentz-equivariant analytic history right inverse MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING.** Classification: `INTERNAL_STRUCTURAL_ONLY`. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). The metric-fibre trace direction is not a four-dimensional physical conformal ghost. K95/K77, fullU/additionalSp, literal contraction/physical quotient and independent row/physical adjoint stay distinct. No standard generation or chirality mechanism is substituted.

## 1. Exact class and source relevance

The mandatory basis is the request for a profound new proof. Target LB-CLASS; internal T1 exclusion and constructive classification. Mathematical breadth: every permitted lower operator and every linear seed hyperplane under the hypotheses below, not a neighboring root or coefficient set. Source necessity and class-C representativeness remain unproved. LT-SM8/LT-GR6b motivate covariance and physical-domain questions but retain their verdicts.

The strongest alternative was the matched weak inverse-response calculation. This class theorem decides the physical interpretation of its entire held column domain first. The previously proved invariant-probability classification was checked and rejected as duplicate work. No new action, parameter family, physical completion or norm is adopted.

Write eta=diag(1,1,1,-1) and let N be the ten-dimensional space of eta-self-adjoint real matrices S. Use

    g(S)=exp(S),      y(S)=g(S)^(-T) eta g(S)^(-1).

The canonical homogeneous tangent/cotangent/spin frame is transported by g(S). This is the frame explicitly used by the preceding paired-current calculation. A different normal-dependent trivialization with newly constant components can define a different physical seed and is outside this identification.

The actual column equation is

    D psi = sum_mu A_h^mu(S) partial_mu psi
          + sum_alpha A_n^alpha(S) partial_alpha psi + C(S) psi = 0.

All lower spin, covector, displacement and formal-divergence terms are retained in C. The canonical constant injection J has zero normal one-form slots and qJ=Id for literal section observation. It intertwines the natural isotropy action. Nonnull covectors have invertible full rolled symbol; this is the held SE=-1/2 factorization, not an assertion about the source's unselected southeast cell.

Work on a connected normal germ. Fields are analytic in S and C1 in base x; local group/seed identities hold on a common smaller product neighborhood. The held global-x finite-band states satisfy this condition. The existence result in section 5 uses analytic base histories as well. Spatial L2 is used only for the final zero-state corollary, not for the rigidity proof.

## 2. Why the full lower operator obeys the needed identity

Central affine dilation is the actual metric-total-space isometry

    (x,S) -> (exp(r)x, S+r Id).

The exponential frame transforms with identity component map because exp(S+r Id)=exp(r)exp(S). Native naturality consequently gives

    A_h^mu(S+r Id)=exp(r) A_h^mu(S),
    C(S+r Id)=C(S).                                      (1)

This is not conformal invariance of a fixed four-dimensional theory, nor an assumption that the selected states are dilation-invariant. Both base and fibre change under the geometric isometry.

**C is not assumed constant in general S.** The normal Maurer-Cartan form g^-1 dg and its isotropy part can depend on shape. They are unchanged under a central shift, since `(exp(r)g)^-1 d_S(exp(r)g)=g^-1 d_Sg`. Invariant Nomizu coefficients, normal contractions, spin/form connections and transported displacement components are unchanged as well. More directly, apply naturality of the complete D to arbitrary constant-component test sections: derivative terms vanish, proving the C identity without dropping any term. In log coordinates the density scales by exp(-4r); its logarithmic derivatives are unchanged, consistent with the formal-divergence identity. No independent dual row is identified with a physical adjoint.

Custody: [homogeneous geometry](source-action-homogeneous-analytic-vacuum-2026-11-25.md), sections A1–A3, proves the actual affine isometry, operator naturality and invariant transport. [Root construction](source-action-dynamics-and-continuation-2026-11-25.md), “Generated span” and “Target normalization,” checks all six Lorentz generators on the complete 59-dimensional family and extends both roots as invariant sections. Thus (1) covers both roots without new root arithmetic. Stationarity is not needed for the structural obstruction; any homogeneous invariant displacement has the required covariance.

## 3. Rigidity of the existing seed, with arbitrary state restrictions

Let H={S01=0}, the previous axis8 seed. Let V be **any collection** of actual solution fields, not necessarily linear, satisfying

    psi(x,T)=J f(x) for every T in H,     f(x)=q psi(x,0),

and closed under the natural rotations in the spatial 01 plane. This includes arbitrary measurable polarization restrictions and frequency-correlated subsets of the earlier completion; neither a Fourier argument nor regularity of a polarization bundle is needed.

### Rotation saturation

The component lift R(h) is independent of S in the exponential frame, and R(h)J=J R_obs(h). Apply the same seed rule to h.psi and undo the rotation. It follows that psi(x,S)=Jf(x) on every rotated H.

The union of small rotated H contains an open normal set. At T=t diag(1,-1,0,0), with t nonzero and arbitrarily small, the rotation generator K01 gives `[K01,T]01=±2t`, transverse to H. The map `(theta,T)->h_theta T h_theta^-1` therefore has full-rank derivative. The inverse-function theorem gives an open image. Analytic uniqueness in S yields

    psi(x,S)=J f(x) throughout the connected normal germ. (2)

For full rotations on an invariant normal ball, diagonalizing the spatial block gives direct saturation; even an SO2 quarter-turn reverses S01, so an intermediate rotation sets it to zero. This direct version does not require normal analyticity. The analytic proof is used for the general classification below.

### Geometry forces all spacetime derivatives to vanish

Use (2) in D at S and S+r Id. By (1), subtraction gives

    sum_mu A_h^mu(S) J partial_mu f = 0,     C(S)Jf=0.   (3)

For diagonal S, the horizontal frame is `exp(s_mu) partial_mu`, so `A_h^mu(S)=exp(s_mu) A_mu`. Compare (3) at S=0 and at S=s E_jj. For each of the four base coordinates,

    (exp(s)-1) A_j J partial_j f=0.

Every coordinate covector is nonnull, hence every A_j is invertible. J is injective. Therefore **partial_j f=0 for every j, including time**.

**RULED OUT:** nonconstant base histories in any such rotation-stable same-seed solution collection. A remaining constant must also satisfy C(S)Jf=0; its existence is not asserted. On R3 with spatial-L2 section data, the constant is zero. No nonzero rotationally covariant subcompletion of the held finite-band image survives.

This is stronger than the previous full-component Lorentz test. It needs neither unrestricted 640-component amplitudes, boost covariance, a mass shell, positivity, nor a linear state set. The original noncovariant diagnostic solutions and their positive charge remain mathematically valid.

## 4. Classification of every linear seed hyperplane

Let H_ell=ker ell for any nonzero real normal covector ell. Suppose the solution collection is naturally covariant under connected G=SO(3) or SO+(3,1).

If the covector line is not invariant, some generator K has `ell composed with ad_K` not proportional to ell. Choose T in ker ell with ell([K,T]) nonzero. The orbit map G×H_ell→N has derivative containing H_ell and this transverse vector, hence full rank. It has an open image arbitrarily near zero. The analytic argument in section 3 again forces normal constancy, and (1)–(3) force base constancy.

Thus **nonconstant covariant states require an invariant covector line**. Here invariant lines are fixed lines: connected SO(3) has no nontrivial positive real character by compactness; the Lorentz Lie algebra is perfect, so a one-dimensional character vanishes on all generators and connectedness makes it trivial. The exact probe verifies that Lie brackets span each native Lie algebra; a fixed-space count alone would not justify this step.

Using the nondegenerate invariant pairing tr(TS), fixed covectors correspond to eta-self-adjoint matrices commuting with the group. Spatial rotations force T=diag(a,a,a,b). Boosts force a=b. Consequently:

| Required covariance | Necessary constant-seed normal |
|---|---|
| Spatial SO(3) | span of spatial trace and temporal diagonal component; two dimensions |
| Connected Lorentz SO+(3,1) | proportional to tr(S); one line |

This is a complete classification of the **eligible linear hyperplane directions in the stated frame**, not of all nonlinear seed surfaces, all observation rules or all physical completions.

The native vertical metric is b(A,B)=4tr(AB)-2tr(A)tr(B). The dual of raw ell=tr is −Id/4, with squared norm −1. For the native coordinate z4=tr(S)/4, the dual norm is −1/16. Both define the same noncharacteristic plane. Since

    det y(S)=det eta * exp(-2 tr S),

that plane is the **fixed-volume metric hypersurface**: the pointwise metric volume density is fixed, not an integrated global volume. Continuation is transverse in logarithmic metric volume density. Its negative vertical metric sign is not a physical ghost diagnosis.

## 5. Sharp positive half: the surviving symmetry does not select dynamics

Take H_tr={tr S=0}. Its conormal is nonnull, so the full repaired column equation is analytic and noncharacteristic there. For **every analytic observed spacetime history f(x)**, the existing Cauchy–Kowalevski theorem gives a unique analytic local solution germ E(f) with data Jf on H_tr. Literal observation satisfies qE(f)|S=0=f.

The actual homogeneous operator, H_tr and J are Lorentz-equivariant. Consequently h.E(f) and E(h.f) solve the same Cauchy problem. Uniqueness gives

    h.E(f)=E(h.f)                                        (4)

after restriction to a common local germ. Existence radii may depend on f; no common boost-invariant box, global domain, Sobolev estimate or physical Hilbert completion is asserted.

**ESTABLISHED:** observation has an equivariant right inverse on the complete local analytic history space in this column category. This reuses the owned CK result; it neither adopts a new seed as source truth nor constructs a positive or interacting replacement.

**No local evolution law follows from these assumptions alone.** At a base point, any prescribed finite jet of f is realized by a polynomial history, which lifts through E. Therefore a finite-order differential relation `P(x,j^N f)=0` holding for every history in this unrestricted image must be an identity on all allowed jets. A chosen mass, dispersion, causal evolution or other nontrivial observed differential equation would require an additional restriction. This does not deny that physical reality, paired-state conditions or full interactions could supply one; those are not established here.

The precise synthesis is: **covariance forces a geometric location for the seed, but still leaves the local observed history unrestricted.** It is more informative than either “the old seed fails” or “the action is incomplete.”

## 6. Counterexamples, source boundary and continuation

- **Frozen metric control:** for null xi, take psi_spin=slash(xi), zeta_mu=xi_mu psi_spin, nu=0. The native frozen symbol annihilates this nonzero vector-spinor. The actual anisotropic fibre variation destroys that null cancellation. Thus a fixed four-dimensional Dirac model is not contradicted.
- **Lower-term control:** an abstract trace-dependent C(S)=−m A_h^time(S) can support normal-constant exp(mt) fields. It violates (1). General nonhomogeneous backgrounds are outside the theorem.
- **Invariant plane control:** H_tr is not moved into an open normal set by Lorentz transformations. The CK lift above is the sharp contrary case, not a claimed physical survivor.
- **Changed seed/readout/quotient:** a normal-dependent seed, a different non-equivariant frame reinterpreted as constant data, nonliteral observation or symmetry only modulo a physical quotient changes a premise. No such escape is certified by being named.
- **Source custody:** SC-GEO-03 ASSERTS Y=Met(X); SC-OP-04 ASSERTS the four-field operator at candidate strength; SC-GEO-51 ASSERTS fullU(64,64); SC-META-53 is UNCERTAIN about physical positivity. None selects this seed or the repaired southeast coefficient. The source's 2+1 and chirality mechanisms are not tested by this theorem.

The next load-bearing question is which source-supplied physical relation restricts the **covariant analytic history space** enough to derive an observed law. Do not seek a rescuing polarization inside the old A01 image. The matched weak response remains a separate diagnostic; any inference to physical energy transfer must first name a compatible domain. The new trace-germ result does not inherit the old finite-band positive norm, current certificates or propagation claims without a bridge.

Choice inventory remains 10 grouped families /4 grouped viability bundles /bookkeeping net6 /0 source-selected predictions. The seed family is constrained; no family is added or silently counted as a newly solved physical obligation. No scientific matrix cell/intersection, source/physics ledger, canon, paper, program_focus or scheduled priority changes. One directed count61→62 and LBCLASS20→21; pending ordinary LC retained.

## Postflight

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Classify covariant constant-hyperplane seeds and test covariance as a selection law.
actual_delta: Non-invariant seeds force base-constant fields; trace seed uniquely supports Lorentz-equivariant analytic history lifting, with every finite observed jet still free.
```

## Verification

The native exact probe checks 306 identities and contrary controls: two/one-dimensional fixed-covector spaces, Lie-algebra perfection, rotation transversality, central geometry, the full 15-column symbol on all four base axes and the trace normal, and the frozen-null failure. Nine Lean lemmas check finite cancellation, injectivity, transversality, conormal arithmetic and null unmasking. Analytic orbit saturation, full operator naturality, CK existence and physical-source interpretation are distinct written obligations, not Lean-certified PDE results. Two mathematical checks and a hostile review are recorded separately; these are internal agent reviews, not external-expert certification.

[Exact evidence](../../lab/process/source-action-rotation-rigidity.json) · [Probe](../../tests/program-focus/source_action_rotation_rigidity_probe.py) · [Lean](../../Lean/GUFormalization/RotationRigidity.lean) · [Review](../../lab/process/hostile-reviews/2026-11-26-source-action-rotation-rigidity-review.md).
