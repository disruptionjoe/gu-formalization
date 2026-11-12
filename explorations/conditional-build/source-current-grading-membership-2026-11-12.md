---
title: "Source current, hidden field coordinates and grading compatibility"
status: exploration
doc_type: structural-result
created: 2026-11-12
program_target: X-P2-P3
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - fixed-current discriminator, natural zero-SE survivor and geometric coordinate alternative"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Source current, hidden field coordinates and grading compatibility

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P2-P3
tier: T2
expected_delta: Complete source-category compatibility test
actual_delta: Conditional full-symbol, current and coordinate constraints; no class decision

```gu-typed-objects
result: Source current, hidden field coordinates and grading compatibility
carrier: independent barred and unbarred one-form and scalar spinors with a specified section split LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: specified nondegenerate connection-independent density dual; K95 tensor form for optional coordinate control ON=declared_carrier
real_structure: complex Clifford identities, with explicit native K95 controls; no signature transfer inferred
grading: source ambient labels, auxiliary odd grading and observed weak grading separately transported
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: source-field current and grading compatibility MAP-TYPE=intertwiner
```

## 1. Source custody and novelty

The operative primary extraction is lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md, rendered page46 eqs9.16–9.20. SC-OP-04 ASSERTS the displayed four-independent-field candidate; SC-OP-05 UNCERTAIN leaves nonzero SE alternatives admitted but unspecified. The unbarred carriers are Ω1(Y,S)⊕Ω0(Y,S), full Dirac S, with barred rows independent. Equation9.18's connection-current component is schematically barν ζ + barζ ν + odot(barζ,ζ), under its displayed outer star. It has no pure barνν term. The fixed field definitions, density dual, connection being varied and representation must be held before interpreting that alphabet. The primary extraction explicitly leaves the density lift unbuilt: the theorem assumes a specified nondegenerate, connection-independent density-dual realization of the displayed bilinear, and does not claim the source already supplied it.

Prior B2C9 (explorations/eric-curt-wave3d-b2c9-offdiagonal-total-current-preboundary-2026-08-01.md) explicitly found a pure barνν monomial from nonzero SE only in a scalarized finite comparator and left the typed current identity open. The theorem below replaces the scalarized coefficient with the actual representation-valued current and states exactly which assumptions make it unavoidable. It does NOT infer that an unspecified source-admitted SE rival must preserve the displayed SE-zero current unchanged.

The same extraction retains a source sign collision: the printed §11.2 ambient-half labels and the selected gamma contraction/d arrows do not yet share a justified uniform duality convention. Do not solve it by silently relabeling form parity.

## 2. Independent-field tensor-current theorem

Fix the spacetime/background metric, epsilon wrappers, Clifford map and density during variation of the source connection A. Let ν be a section of a nontrivial representation bundle S, and let barν vary independently in its actual density-dual row bundle. No conjugation/positivity assumption is made. Suppose a proposed SE kinetic block is

 L_A = t c^μ(∂_μ+ρ(A_μ))+B_0,

with fixed t≠0 and B_0 independent of the varied connection. This is a test of the source's bilinear operator grammar, not a chosen full C action. The SE contribution to its connection Euler covector is, by definition,

 J_SE(δA)=∫ barν [t c^μ ρ(δA_μ)]ν.

On the off-shell locus ζ=barζ=0, every monomial in the displayed9.18 SE-zero alphabet vanishes. Equality with that fixed current for all independent ν,barν and compactly supported δA therefore requires

 t c^μ ρ(T)=0

for every admitted Lie algebra variation T and each μ. This is not a trace-of-matrix criterion: polarization of the independent row/column pairing detects every entry of the endomorphism. Choose a non-null coordinate/coframe direction, for which c^μ is invertible. If some admitted T acts nontrivially on ν, the equation is impossible. Thus the SAME-connection, nontrivially charged Dirac SE block cannot leave the FIXED off-shell SE-zero current alphabet unchanged.

This proof applies to each stated real form with its actual representation. It does not import a compact group or assume a chiral total. A nondegenerate bundle/density identification and an invertible outer Hodge map do not make a nonzero representation-valued Euler covector vanish. If only a restricted current projection or restricted independent field subspace is retained, that is a different hypothesis requiring its actual annihilator test.

### Complete algebraic counterterm criterion

Allow a zero-order SE block B(A) smooth in the pointwise connection, with the principal coefficients still fixed and no derivatives of A in B. Then the pure scalar current vanishes identically iff

 d_A B[δA]=−t c^μρ(δA_μ).

On a connected affine connection patch this integrates exactly to

 B(A)=−t c^μρ(A_μ)+B_*.

Hence the whole SE operator is independent of the VARIED connection. Covariance for charged fields then requires another supplied connection/inhomogeneous datum hidden in B_*, or a different transformation rule; it does not emerge from deleting the connection term. This is the complete pointwise zero-order repair in the stated fixed-principal grammar. If principal coefficients, field definitions, wrappers or density depend on A, their derivative terms must be included; the theorem is not a license to omit them.

### Why common shortcuts do not repair the fixed off-shell identity

- Adding a genuine total divergence to the action changes no compact-support connection Euler derivative. The object here is an Euler covector, not a Noether current modulo improvements.
- Terms proportional to fermion equations can vanish on shell but do not vanish on the independent off-shell test jets used by the theorem.
- Multiplying fermion equations by an invertible row matrix is not by itself an action equivalence. If it is induced by a barred-variable redefinition, the connection Euler covector must be transformed too. An A-dependent field redefinition contributes chain-rule terms proportional to field Euler derivatives; discarding them changes the off-shell statement.
- Setting bars equal to an adjoint before varying changes the source's independent-field variational problem and cannot be used to null the tensor test without a specified admissible reality reduction.

## 3. Trace-scalar redefinitions and the actual observation

Use the fixed nondegenerate split V*=H*⊕N*, Γ=Γ_H+Γ_N, j=gamma/n with Γj=1, and literal observation Q(ζ,ν)=(P_Hζ,ν). Here Γ_N is onto and P_Hj is injective. Consider every scalar-coefficient transformation in the minimal full-Spin Γ/j arrow grammar,

 ζ'=a ζ+j(bΓζ+cν),   ν'=dΓζ+eν.

This includes arbitrary trace/scalar 2x2 mixing and a scalar on the RS remainder. If Q(ζ',ν')=Q(ζ,ν) for all independent ζ,ν, then

 a=e=1, b=c=d=0.

Proof: independent ν fixes e=1; arbitrary Γζ fixes d=0. The upper observation equation on ζ=0 forces c=0 by injectivity of P_Hj. For ζ in R=kerΓ, P_H(R)=H*⊗S, so a=1. The remaining arbitrary Γζ then forces b=0. Thus every nontrivial trace-scalar mixing in this grammar changes literal observation or its scalar provenance.

In particular the change ψ=Γζ used in the full-Clifford repair is not the source's independent ν just because both have spinor dimension. Identifying ν with Γζ reduces the independent field carrier, or must exhibit an additional spectator/constraint and its action/domain; it is not an invertible coordinate change of Ω1S⊕Ω0S to R⊕S because their dimensions differ by one spinor.

### Broader hidden shifts are a real surviving alternative

Do NOT claim the preceding restricted theorem forbids every observation-preserving field redefinition. In the unrestricted linear category, ζ'=ζ+Kν can preserve both P_Hζ and Γζ whenever imK⊂kerΓ_N in normal slots; independent barred hidden shifts can similarly create compensating scalar bilinears after transformation. Such maps may also alter other principal arrows. A row/field transformation preserving Q conjugates any already existing autonomous quotient evolution, so it cannot turn its Jordan quotient into a Dirac one by relabeling; it may change a chosen displayed SE block while the compensating blocks retain the invariant obstruction.

In the unadorned split-isotropy category, K must belong to Hom_{Spin(H)×Spin(N)}(S,kerΓ_N). This Hom vanishes for the native h=4,m=10 spin representation: normal gamma-traceless vector-spinors have the 144/144bar normal factors, while S has 16/16bar; inequivalent irreducibles have no intertwiner. Thus no such hidden scalar shift exists WITHOUT extra symmetry-breaking tensor/background data. This is not a full gauge-covariance prohibition: an actual nonparallel/background-dependent θ, moving section jet or source connection can reduce isotropy and furnish extra maps. The old covariance-versus-fixed-arrow lesson applies. Those possibilities require an actual typed K, its barred partner and transformed current, not a dimension argument.

## 4. Relation to the propagated principal survivor

The previous projected-RS/scalar category has δ=a*sSE/(e*g), with nonzero a,e,g. Its unique nonsingular Dirac-equivalent locus isδ=−3 at ambient14. A zero SE stays δ=0 under separate nonzero block rescalings; reachingδ−3 changes an arrow or uses a nontrivial mixing which must carry all other maps and observables.

The source-admitted nonzero SE rival may have a changed current; that is permitted by its unspecified status. What fails is trying to claim simultaneously: same fixed source variables and observation, same exact SE-zero current, nontrivial same-connection SE Dirac kinetic term, and no additional pure-scalar contribution. These assumptions are incompatible at the displayed tensor level. This is a precise membership discriminator, not a source falsification or proof that C is empty.

Surviving alternatives: actual source SE option with its changed current; a separate admitted/background connection; specified connection-independent principal data; compensating pure-scalar dependence with full covariance accounted for; a source-owned constrained/reality/current projection; or a genuine field redefinition with transported observation/provenance and a verified action/graded equivalence. None is selected by this calculation.

## Principal defects and current cancellation are distinct tests

With the principal symbol, carriers and observation fixed, an added zero-order connection/mass coefficient cannot cancel a nonzero coefficient of an arbitrary first derivative in qD−dq, nor change the frozen high-frequency evolution Jordan invariant. This follows by comparing independent first jets (or scaling a covector): the principal defect is homogeneous of degree 1, whereas the added term has degree 0. The assertion concerns unchanged first-order realization and unrestricted jets; a new constrained carrier, derivative-valued observation, nonlocal elimination or changed principal block is a different problem.

It is nevertheless FALSE that zero-order counterterms cannot cancel the extra connection current. The explicit B(A)=−t cρ(A)+B_* counterterm does so exactly at the stated algebraic scope. Its effect is to remove dependence on the varied connection from the whole SE block; retaining covariance then requires a different supplied connection/inhomogeneous datum or changed field transformation. Thus principal propagation repair, gauge covariance and source-current matching must be tested together. Matter Euler/current changes belong to an admissible rival's specification; their presence is not a contradiction of the source's permission for a different SE operator.

## Released southeast-zero survivor lies in the natural spinorial map family

Use the full-symbol derivation's COMPLETE exterior-compatible raw NW span

 Cξ z=cξ z−ξΓz,
 Gξ z=gamma iξz−gamma cξΓz,
 Tξ=a Cξ+c Gξ.

Both Cξξ and Gξξ vanish, so this is an exterior-input contraction grammar. These maps are not a new guessed action. The existing B2C4 family (explorations/eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md, §§1–2) has actual conventions

 A_contract=ξΓ−cξ=−Cξ,
 A_wedge=Cξ−Gξ,

where its wedge is the grade-three Clifford map. Thus EXACTLY

 Tξ=−(a+c) A_contract−c A_wedge.

On each ambient half, its two real right-H natural coefficients are (c_half,w_half)=(-(a+c),-c), with the source/target half types retained. Equal pairs on the two halves give the present scalar-coefficient family; B2C4's four real parameters are broader. This is a positive membership statement in that repository-owned natural spinorial family, not an assertion that the source selected this member or authenticated its density/adjoints.

The complete raw 6S propagation relation supplied by the full-symbol derivation admits SE=0 at c=−a/(n−2), with a,e,g nonzero. At n=14 its B2C4 weights are

 contract=−11a/12, wedge=a/12.

So the zero-SE survivor is NOT disallowed by naturality or by Schur multiplicity alone. It uses both existing invariant channels. Source §8 admits a family and says its historical selecting computation is unavailable; nothing in that extraction supplies the above ratio or forbids it.

### What the old wedge selector does and does not exclude

Direct Clifford calculation gives

 iξ Tξ=(a+c)(cξ iξ−g(ξ,ξ)Γ).

A LEFT principal Ward/divergence identity iξTξ=0 therefore selects c=−a, the pure wedge line, in this span. At the zero-SE survivor a+c=a(n−3)/(n−2), nonzero for n=14. Likewise the fixed tensor Krein pairing used by B2C4 selects the wedge line among real scalar contract/wedge coefficients; ordinary coefficient adjoint comparison gives T^sharp=T only at c=−a.

These are genuine incompatibilities WITH THOSE ADDITIONAL PREDICATES. They are not source laws. B2C4 explicitly says its spinorial divergence/Ward analogue is not the source's missing bosonic Bianchi proof, and its chosen K pairing is not the independent-bar action already supplied by the primary. A full coupled Noether identity also does not follow from or reduce to the isolated NW left identity. In particular the invertible-time full raw principal system cannot carry a nonzero finite-order arbitrary-parameter fermion-only gauge syzygy; charged matter need not have such an inhomogeneous fermion-only gauge symmetry, and a full boson/fermion gauge identity is a different object.

### Current and grade consequences

Changing only the NW contraction preserves the TYPES of the fixed 9.18 current alphabet: its connection response remains barζ*(changed Shiab/current map)*ζ, while NE and SW give the two cross bilinears. With SE=0 there is no SE-generated pure barνν current. This is alphabet compatibility, not equality of the source's unbuilt typed odot/current coefficients, and it does not establish action ownership.

Both contract and wedge channels have odd Clifford degree (one and three); NE d and SW d* are spin-even in the held source grammar. The existing §9.16/§11.2 ambient-half-label collision therefore persists for the mixed ratio. Passing propagation/current-alphabet tests does not silently resolve grading or reality.

This changes the practical discriminator: a fixed-source-current requirement can reject an unaccompanied same-connection SE Dirac insertion, yet a southeast-zero mixed-Shiab route survives that particular test. It must now be tested against the actual source pairing/duality, full differential/current identities and declared observation; it should not be discarded by reinstating the old wedge-only filter as authorial truth.

### Concrete native-metric loophole supplied by independent review

Independent geometric review identified a specific existing geometric tensor, so the preceding full-Spin(H)×Spin(N) Hom-zero control must not be treated as the actual geometry's complete isotropy. In the adapted metric-fibre model N=Sym²T*X, the metric trace direction t=g is already available. For the native DeWitt normalization its squared norm is4−(1/2)16=−4. Define

 K_t ψ=t⊗ψ−(1/m)gamma_N c(t)ψ, m=10.

Then Γ_NK_t=0 and P_HK_t=0. It preserves ambient spin chirality (the first term is spin identity and the second is degree two). Its inherited pairing is

 K_t^sharp K_t=(1−1/m)g(t,t) I.

Thus non-null t makes this a nonzero injective hidden-RS map, supplied by a retained native tensor rather than an arbitrary new field. It evades the larger-isotropy Hom-zero statement precisely because t is not invariant under that full normal Spin group. The actual covariance group must transport t as well. At a moving section, the identification of the metric-fibre trace direction with the actual normal subbundle and its transport must be supplied; the formula above does not prove that bridge globally.

Consequently observation/provenance-preserving hidden shifts are a concrete surviving candidate, not merely a formal loophole. The next section carries the frozen barred-field, current and evolution transport explicitly; actual source gauge selection and global moving-domain compatibility remain open. This is a correction of the inference scope, not a source-selected repair or a family-count claim.

## Executed algebraic consequence: a nonzero SE block can be a coordinate effect

This supplies the strongest countercontrol to reading an SE coefficient alone as an invariant. Hold the native K95 tensor pairing and the scalar K pairing only to define the coordinate adjoint; bars remain independent. For the actual hidden map K_t above and real scalar k, let

 F=[[I,k K_t],[0,I]],
 unbarred_old=F unbarred_new,
 barred_old=barred_new F^sharp.

Both maps are invertible. This is an allowed change of independent variables in the bilinear, not an imposed reality condition. F preserves literal field observation AND ambient trace: (P_Hζ,Γζ,ν)F=(P_Hζ,Γζ,ν).

For a tangent covector and the exterior-compatible raw symbol

 D=[[T,eξ],[g iξ,0]],
 T=a(cξ−ξΓ)+c gamma(iξ−cξΓ),

one has iξK_t=0, ΓK_t=0, K_t^sharp ξ=0 and cξK_t=K_t cξ, so T K_t=a cξK_t. The transformed bilinear operator is D'=F^sharp D F, with exact blocks

 NW'=T,
 NE'=eξ+k a cξK_t,
 SW'=g iξ+k a K_t^sharp cξ,
 SE'=k² a K_t^sharp K_t cξ=−(18/5)k² a cξ.

Thus a nonzero SE Dirac PRINCIPAL block can appear without changing the observed fields or trace provenance. The accompanying hidden NE/SW arrows are mandatory. Dropping them changes the operator and invalidates any comparison with the previous restricted scalar-arrow delta classifier. In particular the transformation does not select a new physics parameter k; all k here are coordinate gauges of the same supplied bilinear, with all fields/maps transformed.

For a differential operator, D'=F^sharp D F includes D acting on F and therefore every derivative of K_t. If the connection varies while metric/epsilon/K_t are fixed, its exact Euler current is J'=F^sharp J F. Pure scalar monomials now arise from the old cross and barζζ terms evaluated on ζ_old=kK_tν_new and its independent barred counterpart. They do not contradict the fixed-variable current theorem; the algebraic field coordinates and current expression have changed. If K_t depends on the varied datum, additional chain-rule terms must also be included.

For any noncharacteristic time symbol, normalized evolution transforms as E'=F^{-1}EF; the left factor F^sharp cancels. Since QF=Q for the six-spinor field observation Q=(P_H,Γ,scalar), an already established autonomous observed evolution is unchanged. Neither its Jordan defect nor its stable propagation is repaired by this coordinate change.

The equation-output projection is a separate issue: it must transport by (F^sharp)^{-1}; generally QF^sharp≠Q. Do not state that the same raw equation-output arrow is preserved. The theorem concerns the action bilinear under an invertible variable change and the unchanged field-observable evolution. It is not a source-selected hidden shift, global gauge-covariant construction, or identification of the independent source scalar with gamma trace.

## Grading and physical-count limits on the retained carrier

With ambient spin chiralityχ, τ=Γζ has oppositeχ toζ, while sourceν has its own
ambient label. Thus Oaug naturally has gradingdiag(χ,−χ,χ) if the original
source carrier is gradeddiag(χ,χ) and the trace coordinate is transported
honestly. The source principal D is NOT uniformly odd in that source grading:
Tξ flipsχ, while ξν and iξζ preserve it. This is the already known parity
collision, now displayed on the minimum observation carrier rather than hidden
by collapsingτ withν.

A coherent auxiliary odd grading on the full raw source carrier is
Gsrc=diag(χ onζ,−χ onν). Its output lift is
Gaug=diag(χ onb,−χ onτ,−χ onν). Under this gradingτ andν may mix, includingσ.
The change is a rival interpretation of source form/ambient labels; it cannot
be attributed to the §11.2 printed ambient field glyphs without a typed
source/duality explanation. No choice of nonzero coefficient or phase alters
these parity facts. A degree-sensitive duality or an extra odd background
covector can change the map category, as already established in the Aug04
reconciliation; neither is supplied by relabeling.

The minimum 6s output can be decomposed algebraically into horizontalRS plus
three spinor-sized outputs, becauseH*⊗S=kerΓH⊕j_HS. Its ranks are3s+s+s+s.
These are representation/provenance blocks, NOT three physical families.
Whether any form an invariant submodule of the actual weak interaction,
selected positive physical carrier, or common closed dynamics is unproved.
The previous 5s survivor has already discarded an actual scalar output
combination; its 'Dirac copies' cannot retrospectively authenticate2+1.


The metric-trace hidden shift is ambient-even. Its triangular field transform
commutes with the source ambient label grading diag(χ,χ), but generally does
not commute with the auxiliary odd-operator grading diag(χ,−χ). The latter
must transform to R^-1 G R, including its off-diagonal term. Preserving source
half labels does not preserve the old diagonal auxiliary grading unchanged.
These facts supply no actual observed weak-current intertwiner and no physical
two-plus-one count.

## Evidence and acceptance

- Primary fields, candidate matrix, current and southeast rival:
  `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`,
  SC-OP-04/05; source labels also in the section11–12 extraction.
- Existing natural-family and extra-filter calculation:
  `explorations/eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md`.
- Prior projected category and its separate delta=-3 theorem:
  `explorations/conditional-build/native-rs-observed-compatibility-2026-11-11.md`.
- Companion full-symbol and observation proof:
  `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md`.
- Replay: `tests/program-focus/source_operator_membership_probe.py`;
  `lab/process/source-operator-membership.json`.

Independent mathematical cross-review supports conditional T2 acceptance.
Written Clifford identities and coefficient elimination carry the universal
claims; finite exact controls are supporting and contrary tests, not a class-C
decision or proof-assistant certification. Neither source register nor physics
ledger changes. The joint class-C intersection remains open.
