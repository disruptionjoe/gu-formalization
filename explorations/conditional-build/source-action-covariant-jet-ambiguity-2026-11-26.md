---
title: Covariant bulk freedom survives every finite section calibration
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Prove or refute all-history finite-normal-jet uniqueness and quantify an explicit Lorentz-equivariant hidden solution space.
actual_delta: Every finite section-normal-jet kernel contains infinitely many equivariant copies of arbitrary analytic histories. Three algebraically independent trace seeds give an exact weighted filtration. Finite section calibration cannot uniquely select a covariant bulk extension.
class_covered: Linear analytic first-order column systems with Lorentz-equivariant operator and injection, noncharacteristic trace-normal CK surface and unrestricted analytic seed germs in the canonical homogeneous metric-fibre frame. Includes the actual held K95 fullU SE=-1/2 operator at both invariant kappa1 roots. Not all class C, physical Hilbert states or coupled solutions.
premises:
- explorations/conditional-build/source-action-rotation-rigidity-2026-11-26.md
- explorations/conditional-build/source-action-variable-completion-2026-11-25.md
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md
- lab/sources/source-claim-register.yaml#SC-GEO-03
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- lab/sources/source-claim-register.yaml#SC-META-53
source_bridge:
  status: absent
  reason: The source has not selected this repaired operator, unrestricted analytic column domain or completion rule. Its observation and field grammar motivate the test but do not make this solution class physically necessary.
kill_condition: Exclude uniqueness of the bulk extension from Lorentz covariance plus any finite-order section-local calibration within the stated unrestricted analytic class. Not a kill of observed predictivity, physical quotients, GU or class C.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-FINITE-SECTION-CALIBRATION-UNIQUENESS
canon_verdict_change: none
---

# Covariance and finite section data cannot select the bulk

**For every finite number of normal derivatives, there are infinitely many bulk solutions, organized in Lorentz-covariant families, that agree on all those derivatives throughout the observed spacetime history.** This holds for the actual analytic column equation, with its variable coefficients and lower terms retained. An explicit part of this freedom has an exact counting formula.

This is a theorem about **recovering a bulk extension**, not a claim that hidden particles exist or that a four-dimensional observational quotient cannot be predictive. A source-supported physical restriction could eliminate the witnesses; none is derived here. No new physical completion is adopted.

```gu-typed-objects
result: covariant finite-section-jet ambiguity and exact invariant seed filtration
carrier: analytic sections of (TstarY tensor S) plus S; observed (TstarX tensor S) plus S LAYER=ambient BRIDGE=physical_domain_unproved CHIRALITY=N/A
pairing: no positive or physical inner product assumed ON=declared_carriers
real_structure: real eta-self-adjoint metric-fibre matrices; complex K95 fullU column spinors and independent dual row kept separate
grading: polynomial normal order only; not chirality or generation count
action_owner: repository-construction held W2 SE=-1/2 column operator at invariant roots
target: analytic CK extension and complete normal-jet restriction MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING.** Classification: `INTERNAL_STRUCTURAL_ONLY`. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). K95/K77, fullU/additionalSp, independent row/physical adjoint and literal observation/physical quotient remain separate. The three polynomial generators below have no relation to three generations or the source's 2+1 mechanism.

## 1. Selection, exact hypotheses and prior coverage

Mandatory basis: Joe's request for a novel proof. Target LB-CLASS, internal T1 scoped uniqueness exclusion. Mathematical breadth: all linear analytic first-order systems satisfying the structural hypotheses below, including the held actual operator. Source relevance is separately **absent** for necessity of that class. Class-C representativeness remains unproved. Shared prerequisite: the existing trace-plane noncharacteristic CK theorem and actual operator covariance. The strongest eligible alternative is the matched weak inverse response, whose physical domain bridge remains open. No new action, coefficient, seed selection or positive norm is introduced.

Use the exact frame and operator custody of [rotation rigidity](source-action-rotation-rigidity-2026-11-26.md), sections 1–2 and 5. Let eta=diag(1,1,1,-1), S be eta-self-adjoint, r=tr(S)/4, and Q=S-rI. The observation section is S=0; the seed hypersurface is

    H = {S : r=0} = {S : tr S=0},

identified with the nine-dimensional traceless Q-space by S=Q on H. Q is traceless for every S; tracelessness of Q is not an additional equation defining H.

The canonical constant injection J has zero normal one-form slots; q0 J=Id. Literal observation is q psi(x)=q0 psi(x,0). Both J and q0 intertwine the isotropy representations. The trace conormal has native coordinate norm -1/16, so the full repaired symbol is invertible there. This is the K95/SE=-1/2 native fact, not a positive-comparator transfer.

The held equation is linear and analytic, with all spin, covector, displacement, moving-frame and lower terms present. It can be solved locally as

    partial_r psi = sum_i B^i(r,Q) partial_Qi psi
                  + sum_mu C^mu(r,Q) partial_xmu psi + L(r,Q) psi.       (1)

The proof also permits analytic x-dependence. The actual operator, H and J are Lorentz-equivariant in the homogeneous frame, at both certified roots and the invariant displacement family. We use local analytic solution/history germs. For spinors, Lorentz covariance means equivariance under the connected spin cover, with its Lorentz projection acting on x and Q. Individual solutions need not be Lorentz-invariant. Group identities mean equality after pullback and restriction to common smaller neighbourhoods; no single Lorentz-invariant box, uniform existence radius, global continuation or Hilbert norm is claimed.

**What was already known:** [dynamics and continuation](source-action-dynamics-and-continuation-2026-11-25.md) gave finite-jet initial data agreeing now and diverging later. [Slice completion](source-action-slice-completion-2026-11-25.md) gave a whole-history literal-q kernel using noncovariant coordinate seeds. [Rotation rigidity](source-action-rotation-rigidity-2026-11-26.md) gave a covariant constant-seed right inverse admitting every analytic history. The new result combines **all-history invisibility, every finite complete normal jet, covariance, and exact invariant multiplicities**.

## 2. First-order CK preserves normal vanishing order

Let I be the ideal generated by the nine Q-coordinates in analytic functions on H, with arbitrary analytic x-dependent coefficients. For analytic seed s(x,Q), let K(s) be its unique CK extension solving (1). If s lies in I^d, then

    partial_r^j partial_Q^beta K(s)(x,0)=0 whenever j+|beta|<d.          (2)

This is an identity for every x in the local history; arbitrary additional base derivatives also vanish.

**Proof retaining the full equation.** Set u_j=partial_r^j psi|r=0. Differentiating (1) j times gives

    u_(j+1) = sum_(k=0)^j binom(j,k) [
        (partial_r^(j-k) B^i)|0 partial_Qi u_k
      + (partial_r^(j-k) C^mu)|0 partial_xmu u_k
      + (partial_r^(j-k) L)|0 u_k ].                                  (3)

Equivalently u_j=T_j s, where T_j is a differential operator in Q,x whose Q-derivative order is at most j. This follows by induction: composition with one Q derivative raises that order by at most one; x derivatives, multiplication and derivatives of analytic coefficients do not. Thus u_j belongs to I^(d-j) for j<d. Differentiating by beta of length <d-j and setting Q=0 proves (2). Analyticity supplies the actual CK solution; the order induction itself is exact and does not discard lower terms. Terms of normal order below d vanish, rather than merely being numerically small. Q-dependent analytic frame changes preserve this zero-jet property.

**Sharpness.** If s=P_d(Q)Jf(x), with nonzero homogeneous polynomial P_d of degree d and nonzero history germ f, some Q derivative of order d gives a nonzero constant times Jf on H. Applying q0 recovers that constant times f. Therefore the first nonzero complete normal jet occurs at exactly degree d. It is already detectable by q0 applied to a tangential Q derivative; physical availability of such measurements is not assumed.

The first-order premise matters: u_r=u_ss with seed s^d can create a term r s^(d-2), of total normal degree d-1. Such a system is outside (1). The finite probe includes this contrary control.

## 3. An explicit three-generator hidden space

Define invariant scalar polynomials on H:

    p2(Q)=tr(Q^2),    p3(Q)=tr(Q^3),    p4(Q)=tr(Q^4).

They are invariant under Q -> hQh^-1 by cyclicity of trace. No diagonalization of arbitrary indefinite-self-adjoint matrices is assumed.

### Algebraic independence

Test only the explicit subspace Q=diag(a,b,c,-a-b-c). At (a,b,c)=(1,2,3),

    d(p2,p3,p4)/d(a,b,c) =
        [  14   16   18 ]
        [-105  -96  -81 ]
        [ 868  896  972 ],              determinant = 24192 != 0.     (4)

The inverse function theorem makes the image contain an open set, so a polynomial relation among p2,p3,p4 must be zero. Scaling the evaluation point by epsilon scales the determinant by epsilon^6, giving such open image patches arbitrarily near Q=0. Thus the independence holds for polynomial and analytic germ identifications, not only far from the section. We do not need or claim that these generate the full Lorentz invariant ring.

Let A=R[p2,p3,p4], with weights 2,3,4. For a,b,c>=0 and analytic observed history f, define

    E_abc(f) = K(p2^a p3^b p4^c Jf).                                 (5)

Every E_abc is linear, injective and Lorentz-equivariant. Injectivity follows by restriction to H and polynomial nonvanishing. Equivariance follows because the transformed solution and the extension of transformed data solve the same analytic Cauchy problem: H and the seed polynomial are invariant, J intertwines, D is natural, and CK uniqueness applies.

The images of all E_abc form an **algebraic direct sum** of full history spaces. For a finite relation, restrict to H and use polynomial independence; the coefficients are history germs, so independence holds componentwise at each x and hence as germs. No summability or convergence of an arbitrary infinite sum is asserted. The polynomial algebra acts on seeds and may be transported through K; pointwise multiplication of solutions by p2 need not preserve D psi=0.

Let J_N denote the complete normal jet through order N along the section, known throughout local spacetime. On this explicit CK image,

    ker J_N = K( direct_sum_(2a+3b+4c>N) p2^a p3^b p4^c J H_obs ).     (6)

Equation (2) proves inclusion. Conversely, if any lower weighted homogeneous seed component is nonzero, its first nonzero degree is detected by a Q derivative on H. Components of larger degree cannot cancel it. This proves equality. The same equality holds if q0 is applied to every normal derivative in J_N, since all seeds are scalar multiples of J. It is not a formula for the entire solution-space kernel.

**ESTABLISHED:** every fixed finite normal-jet kernel contains countably many independent equivariant copies of arbitrary observed histories. These copies are infinite-dimensional spaces of mathematical fields, not particle multiplicities or new choice-budget categories.

## 4. Exact size of this explicit filtration

The multiplicity of history copies first detected at degree d is

    h_d = [t^d] 1 / ((1-t^2)(1-t^3)(1-t^4)).                          (7)

The number detected through N within the explicit polynomial seed space is

    H(N) = sum_(c=0)^floor(N/4) sum_(b=0)^floor((N-4c)/3)
                (1+floor((N-4c-3b)/2)).                              (8)

| N | 0 | 2 | 4 | 6 | 8 | 12 | 20 | 24 | 32 |
|---|---|---|---|---|---|---|---|---|---|
| H(N) | 1 | 2 | 5 | 9 | 15 | 34 | 108 | 169 | 351 |

These are multiplicities of full history spaces, not dimensions of a physical state space. For a polynomial seed cutoff D>=N, the invisible multiplicity is exactly H(D)-H(N).

For completeness, the weighted simplex {a,b,c>=0:2a+3b+4c<=N} has volume N^3/144. It is contained in the union of unit cubes anchored at the counted integer triples, while those cubes lie in the simplex of radius N+9. Therefore

    N^3/144 <= H(N) <= (N+9)^3/144,
    H(N)=N^3/144+O(N^2).                                              (9)

This quantifies a lower part of the available freedom without claiming a complete invariant classification.

## 5. No finite section calibration selects a unique covariant extension

E_000 is the earlier constant-seed right inverse, q E_000=Id. For d=2a+3b+4c>N, d>0,

    E_alpha = E_000 + alpha E_abc                                    (10)

is another equivariant right inverse, and J_N E_alpha=J_N E_000 for every history f. Nonzero alpha gives a distinct operator. Thus any proposed criterion that depends only on those section jets, even throughout time and even nonlinearly or with additional base derivatives, has the same value on these extensions. If the baseline passes such a criterion, the others pass too. Any nonempty fibre of this finite-jet measurement map likewise has an affine translate of the infinite hidden space.

A sharper functional version does not depend on formal infinite sums. For any convergent analytic germ G(u,v,w), set

    F(u,v,w)=1+u^m G(u,v,w),    2m>N,
    E_F(f)=K(F(p2,p3,p4)Jf).                                         (11)

This is analytic CK data. Each E_F is an equivariant observation right inverse with the same normal N-jet as E_000. Distinct G give distinct extension operators, by the local independence in (4) and restriction to H. An arbitrary analytic function therefore remains inside every such finite-calibration fibre. This exposes existing seed-profile freedom; F is a counterfamily witness, not a newly chosen physical law.

The simple p2^m subfamily supplies an exact first-detection certificate. Along Q=s diag(1,-1,0,0), p2=2s^2, so

    q0 partial_s^(2m) E_m(f)|S=0 = (2m)! 2^m f.                       (12)

**RULED OUT:** unique bulk-extension selection by covariance plus finite section-normal-jet information in this unrestricted analytic class.

**Not ruled out:** selecting a law for the visible f, a legitimate quotient identifying observationally equivalent solutions, or imposing a physical restriction on seeds. In particular, the already selected constant-seed E_000 image is injectively observed and contains none of these nonzero hidden seeds. The obstruction applies before adopting that restriction, not after forgetting it was imposed.

## 6. Gauge, analytic and physical boundaries

**Ordinary local gauge is not an automatic explanation.** The already-proved [local gauge-identity lemma](source-action-physical-dynamics-2026-11-25.md), section 1, applies to this fixed linear column background. If D R=0 identically for a finite-order local differential gauge generator R with unrestricted local parameters, then its leading symbol obeys sigma(D)sigma(R)=0. Sigma(D) is invertible on the open set of nonnull covectors, so the polynomial sigma(R) vanishes there and hence identically. Descending the order gives R=0. Our hidden solution maps depend on analytic histories by CK; they are not nonzero generators of that excluded local kind. This reuses an existing theorem and is not counted as a new gauge result.

This does not settle source super-IG/BRST cohomology, gauge changes that alter the background, constrained-parameter or nonlocal transformations, physical quotients, or actual coupled propagation. The invisible modes have not been shown to survive those tests.

**Infinite jets are different.** If two analytic solution germs have every normal derivative equal along the section, their normal Taylor series agree, hence the germs agree. There is no nonzero analytic perturbation invisible to all orders simultaneously. The quantifiers are “for every finite N there exist invisible fields,” not “there exists a nonzero analytic field invisible for every N.” Smooth nonanalytic flat functions are outside the class.

**Other information can distinguish the witnesses.** Conditions on an open bulk region, boundary/asymptotic data, integrated fibre norms, nonlocal readouts, positivity and a paired-state relation do not factor through a fixed section-normal jet. Their power is undetermined here. No physical measuring apparatus for normal derivatives has been specified.

Source custody: SC-GEO-03 asserts the metric arena, SC-GEO-51 the fullU fork, and SC-OP-04 the independent four-field candidate grammar. SC-OP-05 leaves the southeast cell uncertain; SE=-1/2 is the held repository repair. SC-META-53 remains uncertain as a positivity mechanism. None supplies the unrestricted analytic seed as the physical state space, or selects F in (11). The candidate identity and physical-domain bridge are the weakest unproved links. K77 is not identified with K95; this does not test the 2+1 generation/chirality claims. LT-SM8 and LT-GR6b retain their verdicts.

## 7. Novelty and epistemic status

- **ESTABLISHED within the hypotheses:** equations (2)–(12), equivariant all-history finite-jet ambiguity, exact explicit seed filtration and counts.
- **RULED OUT within the hypotheses:** unique bulk extension from covariance plus finite section calibration; ordinary unrestricted-parameter finite-order local gauge as an automatic removal mechanism.
- **NOT MODELED / UNDETERMINED:** physical admissibility, BRST quotient, coupled quantum theory, source-selected dynamics, hidden particles, agents/minds or server/client ontology.

The novelty claim is **new to the inspected repository and its held candidate**, not a claim of a new general CK theorem or worldwide priority. A bounded search found related classical CK polynomial-extension methods: [Brackx–De Schepper–Lavicka–Soucek (2011)](https://arxiv.org/abs/1101.4516) study initial data, compatibility and dimension counts in Hermitean Clifford analysis; [De Martino–Guzman Adan (2025)](https://arxiv.org/abs/2501.12265) study harmonic generalized CK extensions. Neither inspected abstract establishes this actual variable-coefficient Lorentz-equivariant finite-section-jet application. This limited comparison is not an exhaustive literature novelty certificate. The new synthesis is the typed application and exact filtration, while its mathematical tools are standard.

## 8. Verification, effect and continuation

The 488 exact native checks cover the trace conormal inverse, all fifteen rolled slots, leading CK extensions of the five observed injection slots, rational rotations/boosts, trace-polynomial Jacobian, and independently enumerated weighted counts. A separately labeled variable-coefficient scalar control tests the vanishing-order recurrence and a second-order mutation; it is not substituted for the actual equation. Thirteen finite Lean lemmas certify algebraic and filtration consequences. CK existence, actual naturality, analytic uniqueness and the full written proof receive internal mathematical and hostile review; they are not wholly Lean-formalized.

Choice budget stays **10 grouped families /4 grouped viability bundles /bookkeeping net6 /0 source-selected predictions**. Many mathematical witnesses occur within one existing seed family; they are not counted as new adopted choices or physical obligations met. Scientific matrix verdicts, source/physics ledgers, canon, papers, governance and scheduled priorities remain unchanged. One directed count62→63 /LBCLASS21→22; pending ordinary LC retained.

The useful next discriminator remains a source-supported physical restriction or quotient: what selects an observed law, and which bulk distinctions must actually count as physically different? Finite section calibration and covariance alone now have a proved limitation; repeating them as uniqueness fixes adds no evidence. The matched weak inverse response remains separately diagnostic and needs its physical-domain bridge.

## Postflight

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Test finite all-history section-jet uniqueness and count a covariant hidden seed space.
actual_delta: Uniqueness excluded within the unrestricted analytic class; infinite equivariant hidden history copies and exact 2/3/4 weighted filtration established. No source or physical verdict changes.
```

[Exact evidence](../../lab/process/source-action-covariant-jet-ambiguity.json) · [Probe](../../tests/program-focus/source_action_covariant_jet_ambiguity_probe.py) · [Lean](../../Lean/GUFormalization/CovariantJetAmbiguity.lean) · [Review](../../lab/process/hostile-reviews/2026-11-26-source-action-covariant-jet-ambiguity-review.md).
