---
title: The printed nonzero Shiab endpoint cannot be an exact Euler covector in its fixed-linear family
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Remove action-ansatz and unique-Phi-selection prerequisites from the whole fixed-linear
  endpoint exclusion.
actual_delta: Any C2 functional with the prescribed full-translation Euler covector forces S=0. Every
  nonzero well-typed member of the displayed invariant-Phi family is excluded from that exact variational
  correspondence, without selecting its unresolved coefficients.
class_covered: 'Dimension14 full Dirac128 and full real u(H), Spin-compatible nondegenerate Hermitian
  form, ordinary matrix connection, fixed pointwise real-linear full-Spin S: adjoint2forms to adjoint13forms,
  fixed nondegenerate trace/topform pairing. Exact endpoint R0+a S d_B T+b S(T wedge T)+J T with both
  scalar coefficients nonzero and J symmetric, on any open full primitive-translation field neighborhood.'
premises:
- explorations/conditional-build/full-shiab-variational-consistency-2026-11-27.md
- explorations/conditional-build/riemann-realform-transfer-2026-11-27.md
- explorations/conditional-build/source-prescription-current-2026-11-13.md
- explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-02
source_bridge:
  status: conditional
  reason: The literal fixed-Phi first-action/9.7 correspondence supplies the premises for its well-typed
    nonzero members. Unique Phi/product selection is not needed for this universal implication. Exhaustiveness
    over broader faithful GU constructions or mere equation-zero-set formulations is not established.
kill_condition: A nonzero S cannot be the exact Euler endpoint under all stated premises. A changed tangent,
  pairing outside sections6.1–6.2, symmetry, field-dependent map, multiplier outside sections6.1–6.2 or changed endpoint is a different claim,
  not a tested repair.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-NONZERO-PRINTED-FIXED-SHIAB-EXACT-EULER-COVECTOR
internal_target_verdict: Excluded for all C2 actions in the declared full-tangent architecture; source-facing
  candidate finding only.
canon_verdict_change: none
matrix_or_ledger_effect: No verdict changes; evidence-only versionless delta proposed.
---

# The printed endpoint, independently of an action ansatz

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Remove action-ansatz and unique-Phi-selection prerequisites.
actual_delta: Exact common-S endpoint and every fixed invertible zero-order multiplier force S=0.
```

**The obstruction now concerns every sufficiently differentiable action with the same exact endpoint, not just the printed action coefficients or the W2 reconstruction.** On the declared full field space, a nonzero fixed linear Spin-equivariant Shiab cannot have the printed curvature-plus-mass expression as its Euler covector.

The unresolved invariant-Phi and product choices cannot repair this within the displayed family: the theorem quantifies every such well-typed map. It does not reconstruct a uniquely selected source operator. A zero map is variationally allowed but supplies no Shiab curvature response.

| Three-state result | Scope |
|---|---|
| **ESTABLISHED** | The class corollary below; the source premise table; existing nonzero witness attribution. |
| **RULED OUT** | Every nonzero well-typed fixed-Phi member satisfying the exact first-action variation claim on full translations. Changing nonzero scalar weights, the action ansatz, or any fixed invertible zero-order multiplier does not help. |
| **NOT MODELED / UNDETERMINED** | Corrected or genuinely different GU dynamics, a different physical variation space/pairing outside sections6.1–6.2, nonlocal multipliers, and necessity of this architecture for all GU. No global GU falsification. |

This is an internally reviewed source-facing **candidate finding**, not a source-register verdict or external expert certification. External expert checking is flagged before any paper release; it creates no research waiting condition or contact authority. No world-novelty claim is made.

```gu-typed-objects
result: exact-Euler endpoint obstruction independent of the action ansatz
carrier: dimension14 full Dirac128 and full real u(H) adjoint one-form translations; owned complexification gl128 LAYER=ambient CHIRALITY=N/A
pairing: fixed nondegenerate matrix trace and top-form variation pairing with one-form first ON=adjoint_valued_forms
real_structure: Spin-compatible Hermitian H; polynomial complexification with complex-bilinear trace, not a positive Hilbert pairing
grading: exterior degrees only; no physical chirality or generation count
action_owner: source-action exact endpoint tested against any C2 functional claiming this exact fixed-S primitive translation Euler covector
target: common fixed Shiab map on all curvature inputs MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Source printed family, W2 actual Euler system, full-U and optional Sp tangents, K77 and K95, and ambient versus observed physics remain distinct. No conventional Higgs, three-identical-family or positive-Hilbert assumption is imported. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Exact corollary

Fix a local14D patch, full real u(H), ordinary fixed connection B and the trace/top-form pairing. Let S be fixed in the primitive translation T, pointwise real-linear and full-Spin-equivariant from adjoint2forms to adjoint13forms. Fixed smooth coefficients and nonvanishing density are allowed. Let J be a fixed symmetric zero-order map (the kappa-Hodge mass is an example), R0 a fixed covector, and a,b nonzero real constants. Set

    E(T) = R0 + a S(d_B T) + b S(T wedge T) + J T.

Suppose a C2 functional I on any nonempty open full-translation neighborhood has exactly

    dI(T)[v] = integral Tr(v wedge E(T))

for all compact local variations v. It suffices that each compact W permits T*+tW for sufficiently small t and that mixed second variations commute. Then **S=0**.

This is about the actual variational covector, not only the zero set E=0. Locality of I is not assumed; a putative nonlocal functional with this exact derivative still obeys Hessian symmetry. No global topology, boundary at infinity or Fredholm domain is required for this local statement.

## 2. Proof: separate the Hessians, reuse the complete classification

Write P=S d_B and L_T v=S(T wedge v+v wedge T). Commuting second variations give

    integral Tr(u wedge (aP+bL_T+J)v)
      = integral Tr(v wedge (aP+bL_T+J)u).

At an admitted T*, subtract this identity from the identity at T*+tW. The entire fixed differential operator P cancels, as do J and R0. This cancellation includes coefficient and density derivatives in the formal adjoint. Divide by tb and use arbitrary compact tests to get pointwise symmetry of L_W.

That is exactly the hypothesis used by the [complete Shiab proof](full-shiab-variational-consistency-2026-11-27.md), sections3–7: full central variations remove central output on commutators; repeated exterior slots vanish; distinct slots give three cyclic maps; centerlessness and the scalar quasicentroid of sl128 reduce them to an alternating external3tensor; full Spin forces that tensor to vanish. Consequently S kills every traceless curvature input. No matrix classification is repeated here.

Every bracket is traceless, so L_T=0 for all T, including T*. Subtract the symmetric J from the original Hessian and divide by a: P is formally symmetric. Since d_B preserves tracelessness, P kills every traceless one-form. Formal symmetry forces its output to be central. Independently, the central-output component of S on central inputs is a Spin map from scalar2forms to scalar13forms. The complex minus-identity has opposite parity on these degrees, so this component vanishes. All S outputs, and hence P outputs, are therefore traceless. Thus P=0. Its symbol is S(xi wedge v); decomposable inputs span all2forms, yielding S=0.

The same proof works for fixed smooth a(x),b(x) wherever neither vanishes: b divides out pointwise and the symmetric differential operator is aS d_B, including derivatives of a. If a curvature degree is absent, or a different nonscalar map is used for each degree, this corollary does not apply.

The real-form step is inherited from the [owned transfer](riemann-realform-transfer-2026-11-27.md), not a silent K77=K95 identification. The wedge order remains1form then13form. The proof needs an open neighborhood, not an origin: the two-background subtraction handles any T*.

## 3. Why coefficient and reference-connection audits no longer defer this test

On a star-shaped neighborhood containing0, radial integration of the specified derivative would force

    I(T)-I(0) = <T,R0> + (a/2)<T,P T>
                + (b/3)<T,S(T wedge T)> + (1/2)<T,J T>.

Thus the familiar1/2 and1/3 are consequences of the prescribed derivative's homogeneity. The proof above needs neither this ansatz nor those printed coefficients. A sign or nonzero factor in the bracket does not rescue it.

Nor does it require identifying every historical use of the letter B. On the held source slice, A(varpi)=nabla0+varpi and T=varpi-c(epsilon,g). Hence A=B'+T with fixed B'=nabla0+c, whether or not a separate notation audit identifies B' with a printed B. Ordinary curvature then supplies F_(B'+T)=F_B'+d_B'T+T wedge T. The exact endpoint uses this common S. This is an affine identity from the primitive definitions, not a new source connection choice.

## 4. Source-premise registry for this headline

Primary source: [Weinstein2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf). Page numbers below are printed pages (PDF index is one less). Source assertion is custody, not independent mathematical truth.

| Premise | Status and exact custody |
|---|---|
| Full adjoint primitive translations | **Source-fixed:** section3.6 fullU frame group, section5 translation space; p45eq9.7 varies varpi at held epsilon and metric. SC-GEO-51, SC-ACT-01; [primitive audit](source-prescription-current-2026-11-13.md). Optional quaternionic Sp is not substituted. |
| Pointwise linear, held S | **Source-fixed for the displayed tree:** p43eq9.2–9.3 uses fixed invariant Phi, Hodge and products, linear in curvature xi. Metric/epsilon dependence is held in this variation; it is not genuine varpi dependence. |
| Full Spin intertwining | **Source-fixed for the displayed tree:** p42Definition8.1/eq8.7 invariant Phi. Hodge, wedge and admitted coefficient products intertwine; common epsilon conjugation transports the representation. Additional transformed tensors describe a broader family, not hidden supplied data. |
| Trace/top-form pairing | **Source-fixed for the first action:** p44eq9.4 explicitly expands with matrix trace. A center-degenerate Killing pairing or positive Hilbert pairing would change that expression. |
| Common curvature endpoint, symmetric mass | **Source-fixed displayed claim:** p45eq9.7 asserts the first-action derivative is paired with S F_A plus kappa-Hodge T;9.8–9.10 describe its gravity role (SC-ACT-02). Both curvature degrees follow from the affine source connection. |
|1/2,1/3 and bracket normalization | **Source-fixed but no longer needed as independent premises:**9.4 and12.4, with [K77-B](../resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md). Nonzero scalar alternatives covered. |
| Smooth action/mixed derivative symmetry | **Mathematical consequence for the displayed polynomial local first action** with compact variations. A nondifferentiable prescription would not establish the asserted classical variation. |
| K77 and K95 | **Distinct:** source asserts K77; displayed-block arithmetic yields K95. The theorem transfers through each compatible full-u(H) real form; it does not derive one from the other. |
| Phi vector/product selector | **Source-constrained, unresolved:** p41eq8.1 and p66eq12.26–12.27 allow products; p42section8.2/p43footnote10 do not supply the remembered selector. Quantified by the theorem; no chosen member is promoted. |
| A particular nonzero realization | **Repository-instantiated, not source-selected:** exact witness below. Nonzero curvature response is required for the displayed curvature-recovery role; this is not proof every broader GU mechanism requires it. |
| Exhaustiveness over all GU | **UNDETERMINED:** no source-wide or class-C representativeness claim. Both width witnesses remain uncertified. |

**Action-owner correction retained:**9.7 is the first-action variation.9.12 differentiates the second action I2B=norm-square of Upsilon. It is not a second copy of9.7 and is not a premise of this result.

## 5. Nonzero witness and the universal family conclusion

The owned [K77-B audit](../resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md), sections2,4,5, supplies the low-Phi comm/comm/comm member:

    Phi1 = sum e^i gamma_i;  Phi2=(1/2)Phi1 wedge Phi1,
    unhalved commutator at every product node.

Its fixture index1 (the second fixture) gives direct cubic variation0 and unit endpoint−512, proving that the **total map**, not just one summand, is nonzero. The original executable's `phi_low`, `raw_shiab_parts`, `pair_top`, `T_FIXTURES[1]` and `exactness_rows` own the calculation. It is reused, not freshly executed and not source-selected.

Six low-grade channels had nonvacuous mismatches. Two others vanished on that bank only; they were never certified global zero maps or variational survivors. The new universal theorem resolves the logical fork without another census: if a well-typed displayed member is nonzero it fails the exact endpoint correspondence; if zero it provides no Shiab curvature response. Low/high Phi coefficients, product choices and the ambient Einstein ratio are not extra gaps in this implication.

The raw associative-product reading separately fails the advertised real-adjoint codomain in the owned audit. Keep that type failure separate from the well-typed bracket-family variational obstruction.

## 6. Source-facing candidate finding and escapes

> In the displayed fixed-Phi, full-adjoint translation construction, a nonzero Shiab curvature endpoint cannot be the exact first-action Euler covector claimed in9.7. This conclusion covers unresolved invariant/product choices and is independent of the particular action ansatz. It does not exclude GU with a changed equation or a construction outside those premises.

**RULED OUT within the class:** another nonzero fixed-linear full-Spin S; nonabelian distortion or central-curvature tuning through that same S; nonzero scalar coefficient/sign changes; extra action terms that leave the exact Euler covector unchanged. Separate metric/epsilon equations cannot repair an incorrect diagonal translation Hessian.

**NOT MODELED / UNDETERMINED as repairs:** genuinely translation-dependent/nonlinear S with its extra derivative terms; a symmetry-reducing tensor; restricted physical variations; a changed pairing or multiplier outside sections6.1–6.2; a different Euler covector with the same solutions; second-action dynamics or a different gravity mechanism. None is established viable by falling outside the theorem. A changed action alone cannot preserve the same exact endpoint within the class.

W2 remains a diagnostic carrier with correctly differentiated stationary branches. Its root and small-h endpoint failures cannot be promoted to source-GU failures. Conversely, those candidate-specific failures are unnecessary for this class-level finding.

## 6.1 Fixed equivariant zero-order multipliers are excluded too

Let M be any fixed smooth pointwise invertible full-Spin-equivariant map on adjoint13form covectors. Keep the same full translation space and pairing. If a C2 functional has exact Euler covector **M E(T)**, then S=0. This includes scalar normalization and the broader fixed equivariant multiplier class; no assumption that M times the mass map is symmetric is required.

Set S'=M S. The two-background Hessian subtraction still kills S' on every traceless curvature input by the inherited cubic classification. Formal symmetry of the remaining first-order operator `a S' d_B + M J` implies, in the same pairing-normalized coordinates, that its leading differential symbol A(x,xi) is **skew-transpose**. Coefficient/density derivatives and the zero-order M J cannot change this leading relation. This is the differential sign, not the finite-matrix self-adjointness shortcut corrected in T10.

A kills every traceless one-form input. Skew-transpose symmetry therefore forces its image to be central: for traceless u, `<u,A v>=-<v,A u>=0`. Since decomposable xi wedge v span the curvature domain, S' sends central inputs to central outputs. Full Spin parity kills the remaining scalar2form-to13form map; together with the already killed traceless inputs this gives S'=0. Pointwise injectivity of M gives S=0. Smooth nonzero a(x) merely scales the same leading symbol.

Thus no classification or enumeration of such multipliers is needed. T-dependent or differential multipliers, a non-equivariant extra tensor, or noninvertible projection/changed tangent are outside this corollary, not certified escapes. The source does not select any of these as a replacement for9.7. Multipliers act on the covector/form carrier as stated; a proposed different state norm must be connected to that map before this theorem applies.

## 6.2 The multiplier need not preserve Spin symmetry

The preceding exclusion extends to **every** fixed smooth pointwise invertible real-linear zero-order multiplier M on the same covector carrier, even if M does not commute with Spin. The original S remains full-Spin-equivariant. No symmetry or positivity of M, or symmetry of the multiplied mass, is assumed.

Complexify using the owned real-form adapter, and put S'=M S. Sections3–6 of the inherited proof use only the Hessian identity and full matrix algebra, before imposing Spin. They therefore give

    S' restricted to (Lambda2 V tensor sl128) = C tensor Id_sl128,
    C: Lambda2 V -> Lambda13 V,

where C is determined by an alternating external3tensor. Since M is invertible, the restricted kernels of S' and S coincide. The latter is invariant under the original diagonal Spin action. Thus `ker C tensor sl128` is Spin-invariant. For a spin element g, its conjugation acts invertibly on sl128; applying a nonzero linear functional to that factor shows g preserves ker C itself.

Now Lambda2 of the14D vector representation is the irreducible91-dimensional adjoint representation of complex so14. But C takes values in a14-dimensional space, so its kernel is nonzero. An invariant subspace of this irreducible module is either zero or the whole module; therefore C=0. Hence S' and S both kill every traceless curvature input, without any equivariance assumption on M.

The leading-symbol argument in section6.1 still applies to S'd_B plus the arbitrary fixed zero-order multiplied mass. It forces S'(central curvature) into the14-dimensional central13form output. Invertible M preserves rank. The original S on central curvature is a Spin-equivariant map with irreducible91-dimensional domain Lambda2 V, so its rank is either0 or91. The bound rank<=14 forces rank0. Combining central and traceless inputs gives **S=0**.

All steps are fibrewise, so smooth position dependence of fixed M causes only lower-order derivatives, already irrelevant to the leading-symbol argument. An arbitrary real invertible M complexifies to an invertible complex map. This theorem does not assume the source selects such a multiplier; it excludes the whole declared repair category. A fixed nondegenerate pointwise change of the variational pairing is included when represented by such an M on the same full carrier.

Still outside: T-dependent multipliers, differential/nonlocal maps, noninvertible projections, changed physical tangent/domain, changed equations, or loss of full Spin equivariance of the original S. Their physical relevance and source selection remain undetermined. A PT construction changing its Hilbert domain is not ruled out merely by this finite-order pairing result.

## 7. Ranking and process consequences

This wave resolves the source-premise opener before broad new computation. The existing assumption view already owns shared inputs; no second ledger, automated process rule or new schedule is created. The registry above is attached to the result it qualifies. The existing versionless-delta route receives evidence for LT-GR1, with verdict unchanged; other pillar claims are not bundled without their own scope audit.

The proposed fixed invertible zero-order multiplier classification is **consumed by sections6.1–6.2**, even without multiplier equivariance or symmetric multiplied mass. No further source-variation or fixed-multiplier census is justified. Rerank toward an independent source/observation consequence: the source-necessary finite-normalization composition or the observation/embedding condition behind the conditional kinematic fits. Their physical necessity and carrier premises must be tested rather than repeating already-proved representation/anomaly arithmetic. Genuinely field-dependent or differential multipliers remain outside this proof, without source-selection or viability credit.

The source-state law, physical quotient/norm and native observation/grading remain shared burdens, not identical missing objects. Their absence in audited text means not supplied in that coverage, not mathematically impossible. No inference that all six physics pillars have been excluded follows from a compact map.

**Correction retrospective:** the previous citation drift arose by grouping two derivatives by notation instead of action owner. This artifact records page, equation and owning functional together. The local preventive check is precise custody in each source-sensitive result, using the existing convention gate; no governance amendment. Claimed efficiency gains are one avoided coefficient audit and one avoided Phi/product census; elapsed/token savings are unmeasured.

## 8. Verification limits

The complete matrix-unit/quasicentroid, real-form and Spin proof and its33 grouped exact controls/512 trace triples/64 cyclic residuals are inherited from the accepted whole-Shiab artifact, not freshly rerun. The new finite Lean kernels check subtraction of two affine Hessian pairings with nonzero coefficient and the arithmetic implication rank<=14 plus rank in{0,91} implies rank0. Irreducibility and kernel invariance are written proof premises, not formalized by that arithmetic. Smooth field openness, fundamental lemma, source identification and the universal operator proof remain written and independently reviewed. This is not a full formalization of the no-go.

Two specialist reviews and one hostile review, dependency hashes, targeted Lean and native gates are recorded in [evidence](../../lab/process/printed-shiab-endpoint-audit.json). No source, canon, physics-ledger or class-C verdict changes; no new choices or source-selected predictions. Candidate bookkeeping remains10 families/4 grouped obligations/net6/0 predictions, not a lower bound on independent source-required choices.
