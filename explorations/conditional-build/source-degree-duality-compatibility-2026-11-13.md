---
title: "Degree-dependent source dualities and joint geometric repairs"
status: exploration
doc_type: structural-result
created: '2026-11-13'
program_target: X-P2-P3
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - complete frozen-duality obstruction and explicit same-carrier alternatives"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Degree-dependent source dualities and joint geometric repairs

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P2-P3
tier: T2
expected_delta: Source-correct weak action and density-duality compatibility
actual_delta: Constrained - complete frozen-duality obstruction and explicit same-carrier alternatives

```gu-typed-objects
result: Degree-dependent source dualities and joint geometric repairs
carrier: full complex Dirac zero- and one-form fields and independent bars, all ambient principal covectors LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: arbitrary nondegenerate degree-preserving row dual; Spin invariant and real-form subcategories separately classified ON=declared_carrier
real_structure: complex Clifford identities; K77 real and K95 quaternionic structures separately typed; finite reduced-Clifford controls only
grading: printed ambient labels versus explicitly changed relative-degree labels
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: density duality, current and weak-compatible propagation MAP-TYPE=intertwiner
```

## 1. Primary custody and hypotheses

Primary: `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`, rendered p.46, eq9.16; p.51 ambient labels are in its successor collision and `gu-2021-draft-s11-s12-extraction-2026-08-03.md`, §2.1. The p.51 reference is SECTION 11.2, not numbered equation11.2 (that numbered equation is a tensor-product spinor formula on p.50).

SC-OP-04 ASSERTS (draft2021 p46, extraction-verified, auxiliary) only a candidate four-independent-field matrix. SC-FER-06 ASSERTS (p51, extraction-verified, auxiliary) ambient half-spinor labels. SC-OP-02 UNCERTAIN (p42, newly-extracted, auxiliary) leaves the historical Shiab selector lost. SC-OP-05 UNCERTAIN (p46, extraction-verified, auxiliary) admits unspecified nonzero-SE rivals. These source claims are not mathematical proofs. SC-GRP-02 ASSERTS and SC-GEO-51 ASSERTS retain U(64,64) as parent; no unconditional Sp parent is substituted. SC-SIG-04 ASSERTS a chosen K77, while SC-SIG-03 UNCERTAIN retains signature choice; K95 is separately typed below. SC-META-56 DISAVOWS demanding an action for the supersymmetry-like graded structure; this test does not impose it.

At a frozen point, let V be 14-dimensional with nondegenerate metric, S=S+⊕S− the COMPLEX full Dirac carrier, J its chirality. E1=V*⊗S, E0=S. Bars are independent, with a nondegenerate density-dual map Bp on each form degree p; they are not set equal to adjoints. Density/Hodge identifications are held and spin-even. An arbitrary linear or antilinear map on the barred slot is allowed, separately for each degree; no positivity or pairing symmetry is assumed.

Write the principal arrows

    dξ ψ = ξ⊗ψ,
    δξ z = iξ z,
    Tξ = a Cξ+c Gξ,
    Cξ z = c(ξ)z−ξ Γz,
    Gξ z = γ(iξ z−c(ξ)Γz).

Here γ is the unnormalized Clifford insertion, Γγ=14I. Coefficients may differ on the two input chiral halves. Both C,G are ambient-spin-odd, d,δ spin-even, and Tξ(ξψ)=0. The test holds arbitrary nonzero chiral weights; it does not select a or c. In particular it includes the already-derived six-spinor locus c±=−a±/12 with a±≠0.

The source row order is (barζ−,barζ+,barν−,barν+), column order (ζ+,ζ−,ν+,ν−). EXACT derivative cells are

| zero-based cell | principal bilinear |
|---|---|
| (0,1) | B1(barζ−,Tξ ζ−) |
| (1,0) | B1(barζ+,Tξ ζ+) |
| (0,3) | B1(barζ−,dξ ν−) |
| (1,2) | B1(barζ+,dξ ν+) |
| (2,1) | −B0(barν−,δξ ζ−) |
| (3,0) | −B0(barν+,δξ ζ+) |

There is ONE output-degree duality B1 used by BOTH NW and NE, and ONE B0 used by SW. This is not six independently chosen cell pairings. The source does not authenticate that common density realization, so the theorem is a structural subfamily test. Every other cell has zero PRINCIPAL coefficient. This does not set its printed connection coefficient to zero. The minus signs on SW do not affect the support theorem and must still be retained in any action/adjoint comparison.

## 2. Complete arbitrary degree-dependent duality theorem

**Theorem.** With unaltered d and δ, printed ambient field labels, and degree-preserving nondegenerate duality maps independent of ξ, the six-cell support is possible iff the NW symbol is ambient-spin-EVEN. In particular no nonzero ambient-spin-ODD NW symbol is possible. This includes arbitrary RS/trace-dependent coefficients, arbitrary reduced-isotropy or tensor-dependent duals, linear/antilinear duals, and BOTH signatures. It is stronger than the old two-uniform-conventions calculation.

Proof. Fix s=±. The absence of the opposite-sign NE cell says

    B1(bar z_s, ξ⊗ψ_−s)=0

for every independent bar z_s, ξ, ψ_−s. Pure tensors ξ⊗ψ span ALL E1,−s, including both its gamma trace and RS parts. Hence B1(bar E1,s,E1,−s)=0. Nondegeneracy makes B1 a perfect pairing between same-label halves. It cannot assign the trace and RS components different effective chirality supports to evade this conclusion.

The forbidden opposite-sign SW cells similarly give B0(bar E0,s,E0,−s)=0, since δξ is onto S for any non-null ξ. Thus B0 is also same-label nondegenerate.

Now decompose Tξ into its even and odd parts. For input E1,s, the odd part lands in E1,−s and is detected nondegenerately by bar E1,−s, precisely the NW cell where the printed matrix has no derivative. Therefore every odd part must vanish. Conversely, any even T, with arbitrary nondegenerate same-label B0,B1, has exactly the allowed support; requiring all six cells nonzero additionally requires the two T restrictions nonzero. QED.

The contradiction cannot be repaired by killing only the trace pairing or by singular row maps: nondegeneracy is an explicit hypothesis and the NE span hits the entire one-form carrier. A restricted covector set, restricted barred field domain, constraint, derivative-dependent duality or nonlocal transformation is a changed category and must name the altered domain.

For the natural two-channel family, T=0 iff a=c=0 on each chirality. For a direct proof take orthonormal distinct directions 1,2,3 and ξ=e1, z=e2⊗ψ. The component3 is −c γ3γ1γ2ψ, an invertible Clifford product times c, so c=0; component2 then gives a γ1ψ, hence a=0. Thus the theorem excludes every nonzero member, including both-channel survivors and every coefficient-degenerate branch except the absent-NW symbol. This is a category result, not finite coefficient fitting.

Six independently chosen block/cell pairings are a genuine excluded alternative. If B_NE and B_NW differ, express them using one invertible density dual as B_NW(bar z,u)=B_NE(bar z,A1 u); the effective NW symbol is then A1 T. When their chirality supports differ, A1 is odd. Thus this alternative is exactly an added operator tensor/changed-arrow grammar, rather than a counterexample to the common-duality theorem. The explicit repair in §5 realizes it. The primary source has not ruled this larger construction category out.

The NE-spanning proof still applies if a degree-dependent duality is constructed from Hodge, chirality, charge conjugation, metric trace or any other fixed tensor. The tensor may change which pairing is available; it cannot make one row both annihilate and detect the same output half while d is unchanged.

## 3. Exact invariant Hom spaces, multiplicities and real forms

Under a fixed Spin(14,C) reduction, the Weyl modules have dimension64 and are dual to each other (D7 has odd rank). The one-form representation decomposes

    E1,+ = R+ ⊕ j S−,     E1,− = R− ⊕ j S+,
    dim R±=832,

with Γ flipping spin chirality. R+ and R− are dual inequivalent irreducibles; neither is isomorphic to a spinor module. Therefore EVERY complex-linear Spin-equivariant, degree-preserving map E→E* has exactly SIX independent complex coefficients: one for each of the two scalar ordered pairings, two trace ordered pairings, and two RS ordered pairings. All pair opposite ambient halves; all six weights must be nonzero for nondegeneracy. No RS↔trace mixing is equivariant, and the independent scalar and gamma trace are not identified. This is broader than the earlier four-scalar pairing family: it includes independent trace/RS weights, without imposing symmetry or formal adjointness.

If form-degree mixing were allowed at the representation level, the two spinor multiplicities would allow two 2×2 matrices plus two RS scalars (ten complex parameters). Those off-degree pairings are NOT degree-preserving row identifications of the source display. The six-parameter result claims completeness only for its stated degree-preserving category; the arbitrary-duality theorem already covers every map within that category.

For Spin(7,7), each Weyl module has a real structure C with C²=+1 and CJ=JC. For Spin(9,5), each Weyl module has a quaternionic structure C with C²=−1 and CJ=JC. Hence anti-linear intertwiners E→E* are obtained by composing the same six complex-linear pairings with C; their chirality support is still opposite. The K77 real-linear family has six real coefficients on the real modules. K95 does NOT acquire the same real64 Weyl carriers: its complex64 Weyl module has underlying real dimension128 and quaternionic commutant. A general real-linear map on the complex carriers splits into complex-linear and anti-linear pieces; varying an independent field by i separates their support constraints, so their sum cannot cancel the obstruction.

The real-form distinction is thus material for dimension/reality and potential adjoints, but irrelevant to the NE-spanning obstruction. No Lorentzian4 conjugation rule is imported into fourteen dimensions.

Full U(64,64) is different: its central U(1) forbids a nonzero invariant complex-bilinear S×S→C, while its fixed Hermitian form supplies an anti-linear duality. A chosen Clifford map, J, trace direction and Spin reduction are not all fixed under the entire parent. Covariance under g∈U means transporting them (e.g. J→gJg⁻¹, c→gcg⁻¹, duals contragrediently), not demanding every tensor remain fixed. The displayed rho(epsilon) wrappers fall under this same simultaneous transport: they do not change the relative parity by conjugation. A position-dependent epsilon contributes derivative-free connection terms when differentiated, which cannot cancel a coefficient of arbitrary first jets. An operation that holds J fixed while changing only one contraction is a changed-arrow test, not simultaneous transport. Simultaneous transport preserves the spanning/parity theorem. This does not prohibit full-parent covariance; it excludes the frozen-arrow support problem on every transported fiber.

## 4. Minimal changed-label repair: complete sign classification

Hold the natural invariant opposite-half pairing and original arrows. Let σp record a global flip of unbarred labels in degree p, and τp the independent flip of barred labels. The six cells impose

    NW: τ1=σ1,
    NE: τ1=−σ0,
    SW: τ0=−σ1.

Consequently

    σ1=τ1=−σ0=−τ0.

There are exactly two solutions, related by a simultaneous global sign change. Thus the UNIQUE relative repair reverses one-form versus scalar labels, with the bars matching their unbarred degree. Relabeling only bars cannot repair it. This recovers G=(−1)^form J, now as a complete independent-bar sign classification, rather than merely an example of a convention that works.

This is a mathematically valid broader-program convention repair. It is NOT a reconciliation preserving SC-FER-06's printed p51 ambient labels. It leaves the physical fields and literal observation untouched if treated solely as renamed notation, but all displayed grading/provenance labels must then be corrected consistently. It does not produce a physical family count or a new propagator.

Equivalently, keeping ambient labels and the invariant pairing, the native NW cells stay in their printed positions but NE and SW derivatives must move to the four other cells: NE to (0,2),(1,3), SW to (2,0),(3,1). This is a precise matrix-support correction alternative; the source has not authorized it as an erratum.

## 5. Minimal added-tensor/changed-arrow repairs

With printed labels and unchanged d,δ, §2 proves NW must become EVEN and the row duals must become same-half. Therefore an added tensor in the DUALITY ALONE cannot work. At least one PRINCIPAL ARROW CLASS must change. Within Spin-equivariant unadorned tensors there is no odd invertible endomorphism S+↔S−; introducing one reduces isotropy or uses transported extra geometric data.

A concrete algebraic repair is available from ONE non-null vector t and A=c(t), A²=g(t,t)I≠0. Let A1=I_V⊗A and A0=A. Given an invariant opposite-half pairing B, define same-half duals

    Bp^t(bar u,v)=Bp(bar u,Ap v).

Replace only the NW principal class by

    Tξ^t=A1 Tξ.

It is spin-even, nonzero when T is nonzero, exterior-input-compatible because Tξ^t(ξψ)=0, and the unchanged d,δ together with Bp^t satisfy ALL SIX printed support cells exactly. This proves the failed category has a concrete one-tensor successor; it does not claim that the source selected this operator or density. The tensor t may be an existing geometric trace direction if its chimeric/actual-normal transport is supplied. The current native metric-fibre trace has norm−4 in the relevant K95 normalization, but this local datum does not itself prove a global normal vector, and is not transferred to K77 by fiat.

The stabilizer is the subgroup preserving t and the retained metric/Clifford data, rather than the entire fixed Spin group. In the standard native normal Spin(6,4) split where SU2_L acts on the negative four-plane, the fixed normal vectors form the positive six-plane. Thus the native negative-norm metric-trace t is NOT a fixed-SU2_L-equivariant repair. Transported covariance is different. Choosing a positive non-null t in the inert six-plane makes A commute with that weak action, but is an extra geometric selection, not the same native metric-trace datum. Under full-parent covariance A and B move as tensors. Null t does not supply the advertised invertible repair: A²=0 and the duality degenerates. This is a necessary non-null control.

A second repair retains the natural opposite-half pairing and the odd NW symbol but replaces BOTH exterior cross arrows by odd tensor-adapted arrows, e.g. d→A1d and δ→A0δ (or the appropriately paired formal adjoint of the first). Then all three principal classes are odd and the source six-cell support works. It changes the literal d/d* cells and therefore is a broader-program operator rival, not a duality-only reading of the printed candidate. Formal adjoint signs and derivatives of a moving A must be checked separately.

These are minimal in clear senses: (i) zero changed arrow classes is impossible even with arbitrary duals; (ii) one changed arrow class suffices when duals may use A; (iii) if natural opposite-half duals are held, BOTH even exterior arrow classes must change. No claim is made about a unique physical tensor or an optimal action. These two repairs DO preserve frozen normalized evolution by exact equivalences below, while their literal scalar field comparison must be transported. A row equivalence alone that transports the dual so the full bilinear stays unchanged in the SAME fields cannot repair support: it merely rewrites the same incompatible bilinear. The concrete equivalences additionally change scalar field coordinates and therefore do not evade the theorem's held-field hypothesis.

### Exact propagation follow-through for both repairs

Freeze A and keep SE=0. In the formulas written below e,g are nonzero scalar weights (including the printed unit derivative coefficients); a±,c± may differ by input chirality. For general chiral cross-coefficient endomorphisms, use LDR itself and retain the induced conjugations of those coefficients: do not commute them past the chirality-odd A. The support and similarity results persist with those explicitly transported coefficients. Set R−=diag(I_E1,A0⁻¹) and L−=diag(A1,I_E0). Because A1 dξ=dξ A0,

    D_NW^t = [[A1T,e dξ],[g δξ,0]] = L− D R−.

For any noncharacteristic time covector τ, normalized evolution satisfies

    E_NW^t(ξ) = (D_NW^t(τ))⁻¹D_NW^t(ξ)
               = R−⁻¹ E(ξ) R−.

Thus invertible time coefficient and frozen strong hyperbolicity are preserved. Let q=(P_H ζ,Γζ,ν) be the full6S observation, and r−=diag(I_observedζ,I_trace,A0⁻¹). Exactly qR−=r−q. Hence if qE=e_obs q, then

    q E_NW^t = r−⁻¹ e_obs r− q.

Both observed one-form and ambient trace are unchanged; the scalar receiver is explicitly transformed by A0⁻¹. Literal scalar provenance is NOT identical across the old/new variable charts. Raw equation-row closure qD is not needed: the transformed raw row selector is qL−⁻¹; normalized evolution is the invariant statement.

For the crossed-arrow repair, set R+=L+=diag(I_E1,A0). Then

    D_cross^t = [[T,e dξ A0],[g A0 δξ,0]] = L+ D R+,
    E_cross^t = R+⁻¹ E R+,
    qR+=diag(I,I,A0)q.

Thus this repair also preserves the established frozen full6S propagation locus c±=−a±/12, with all scalar chiral weights/tensors transported. Neither proof extends automatically to a moving/global closed domain: derivatives of A, the connection and boundary data must be carried. If SE were nonzero it would transform to SE·A⁻¹ in the first construction and A·SE·A in the second; holding an old SE fixed would invalidate these identities.

The two constructions are not two independently authenticated physical operators. Let λ=A²=g(t,t) and B=diag(B1,B0). For the first repair its paired coefficient is

    B^t D_NW^t = B diag(A1,A0) L− D R−
                = λ B R− D R−.

So it is a scaled scalar-coordinate congruence of the original coefficient. Independent barred density-covectors must transform by the matching left factor. The second repair is already a scalar congruence B R+ D R+. This explains how one can transport propagation while changing the apparent grading/cell grammar: the scalar change A±1 is chirality-odd. Transporting the original J along those field coordinates gives scalar grading −J, precisely the relative label issue. Declaring the new scalar's displayed labels to be the original fixed ambient labels instead is a changed grading identification. There is no proof of source selection, unchanged fixed current, or unchanged literal scalar observable hidden in the equivalence.

For the positive inert-six-plane t control, [A,weak]=0 makes these frozen field/row transformations weak-equivariant as well. A non-null horizontal vector is another weak-invariant alternative because horizontal Clifford multiplication commutes with the even normal weak generators; fixing such a vector costs a preferred Lorentz direction (for example a clock choice), rather than a selected normal six-plane direction. This is a conditional joint algebraic witness with extra selected tensor, not a source-native-t joint witness or physical family mechanism.

## 6. Independent current checks; avoiding tautological success

No numerical equality with the source's unbuilt odot current is asserted. The p46 eq9.18 current fixes an alphabet of barνζ, barζν and barζζ, but the extraction explicitly leaves its density/typed contraction unresolved. All displayed SE-zero repairs preserve that alphabet if all new tensors and pairings are independent of the varied connection. The NW repair changes the ζζ coefficient; the changed row dual also changes cross-current coefficients. Alphabet preservation is only a necessary compatibility observation, not authenticated source-current equality.

There is a useful exact independently-fixed control. Suppose one fixes an actual cross-current tensor

    J_NE(bar z,ν;δA)=B1(bar z,ξ⊗ρ(T)ν)

for every ξ,T and independent fields. Replacing B1 by B1' preserves that SAME tensor iff ΔB1 vanishes on V*⊗span{ρ(T)ν}. In particular, if an admitted variation acts invertibly (the central iI in the full U parent is an example), this span is all E1 and B1'=B1. More generally the same conclusion holds whenever the representation images jointly span S. The analogous SW test fixes B0. Proof is pure-tensor spanning and independent polarization. Thus a same-half duality cannot claim to preserve an independently fixed opposite-half cross-current without an actual transformed current specification. This is not the tautology of defining a new current to be the variation of a new bilinear and then calling it equal to the old one.

For moving, connection-dependent A or B, include their δA variations and ∂A/connection lower-order terms; the alphabet claim above is then not automatic. No current coefficient theorem is obtained without the independently held typed tensor. No SE insertion is required by the repair, so the previously proved pure-scalar-current obstruction does not by itself discard it.

## 7. Reproducibility and limits

The proof is exact and representation-theoretic; the finite control is not its certificate. The retained replay includes exact reduced-Cl(3,1) joint controls for BOTH repair factorizations, normalized evolution, q-kernel closure, the raw-row negative control, bilinear congruence and null-adapter degeneracy; these complement rather than prove the dimension-independent identities above. The duality suite reads the primary cell ledger directly, checks all sixteen cells against the six derivative positions, enumerates all16 independent barred/unbarred degree-label flips, verifies precisely the two sign repairs, and checks the parity equations for the two added-tensor repairs and their negative controls. The duality suite uses only the standard library; the other exact suites require SymPy. Run from the repository root:

    python tests/program-focus/source_weak_duality_probe.py

Required controls are explicit: invertibility, both chiralities, all covectors (not just tangential ones), all independent bars, both NW natural channels, no real-form transfer, and connection independence where used. The theorem's span proof fails for a restricted ξ-domain because tangential ξ do not span ambient V*. That is a real changed-domain alternative, not an omitted singular coefficient branch; it does not type the full ambient printed operator automatically. Density powers and Hodge signs cannot repair ambient chirality because they are spin-even here. Parameter scans and a sampled gamma representation are not needed.

Actual delta: the degree-dependent row-duality loophole is CLOSED for the unchanged full ambient arrows and printed ambient labels, including arbitrary multiplicity weights and symmetry-breaking duals; two exact minimal repair categories remain with concrete witnesses and current limits. No source-selected operator, global normal transport, source-selected weak/current identification, action, closed domain, physical chirality, class-C inhabitant or class-wide exclusion is established.

## Evidence and acceptance

- Primary matrix and exact labels: `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` and `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`.
- Full source-shaped carrier and stable locus: `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md`.
- Independent bars, current, coordinate and grade custody: `explorations/conditional-build/source-current-grading-membership-2026-11-12.md`.
- Existing branching and real observation result: `lab/active-research/pati-salam-chain-verification.md` (branching only; its old real/complex count is not reused) and `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md`.
- Paired result: `explorations/conditional-build/source-weak-action-transport-2026-11-13.md`.
- Replay: `tests/program-focus/source_weak_duality_probe.py`; retained evidence: `lab/process/source-weak-duality.json`.

Independent mathematical/source review and exact supporting/contrary controls
support conditional T2 acceptance. Universal claims rest on the written proofs,
not sampled ranks. No Lean, external-expert certification, source/canon verdict,
physical prediction or class-C decision is claimed. Matrix18/18 remains
constrained; its joint realization remains open.
