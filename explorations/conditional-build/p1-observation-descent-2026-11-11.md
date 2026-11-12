---
title: 'Observed chirality: selectors, symmetry and local reduction'
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P1xfields
tier: T2
expected_delta: Derive nontrivial conditional requirements for the remaining P1/P2
  cells
actual_delta: P1 fields, symmetry, order_locality and variational constrained at declared
  structural scope
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Observed chirality: selectors, symmetry and local reduction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P1xfields
tier: T2
expected_delta: Conditional constraints for open matrix cells
actual_delta: P1 fields, symmetry, order_locality and variational constrained at declared structural scope

```gu-typed-objects
result: Observed chirality: selectors, symmetry and local reduction
carrier: surjective observed bundle quotient of a fixed native 4+10 vector-spinor split, plus declared linearized local operators LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: declared density-dual Hermitian forms, not inferred physical positivity ON=declared_carrier
real_structure: separately stated real or complex category; K77/K95 never silently identified
grading: upstairs selector versus observed weak projectors; neither is presumed the other
action_owner: N/A -- structural tests, no guessed action or class-C inhabitant
target: actual observation and declared analytic realization MAP-TYPE=restriction
```

## Scope and source typing
These are lane-B statements about structurally defined subclasses of class C. They do not exhibit a class-C action, assert C nonempty, identify a physical weak current, or derive a generation count. P1 is observed weak orientation; it is not ambient chirality, trace/remainder provenance, or P3's integer. Source SC-CHI-01/51 asserts a nonchiral total with effective chiral worlds; SC-GEN-01 disavows three simply repeated families; SC-FER-04/05 gives the gamma product-rule and chirality-correlated labels, while SC-GEN-52 leaves the live second-family trace/kernel wording uncertain.

## A. P1 x fields: which proposed selectors survive literal observation?
Let q:E→O be a surjective linear map over characteristic zero. For an endomorphism A of E, a unique observed endomorphism a with aq=qA exists iff A(ker q)⊂ker q. Proof: a[qx]=[qAx] is well-defined iff qAk=0 for all k∈ker q. If A²=A or A²=1, the descended a has the same identity. Thus the obstruction is the concrete map δ_A=qA|ker q, not a dimension count. This applies pointwise to smooth bundle maps of constant rank; the induced map is smooth. It does not supply action, dynamics, pairing or physical meaning.

For the native fixed nondegenerate split V*=H*⊕N*, dimH=4, dimN=10, A=(H*⊕N*)⊗S, literal q=P is (b,v)↦b. Let ΓY=ΓH+ΓN and metric-normalized jY=(2/7 jH,5/7 jN), ΓHjH=ΓNjN=1. For the ambient gamma-trace projector T=jYΓY,

δ_T(v)=P T(0,v)=(2/7)jHΓN v.

ΓN is onto and jH injective, hence rank δ_T=dim S=s, with kernel kerΓN of dimension9s. The complementary remainder projector has δ_(1-T)=-δ_T. Neither the gamma-trace/remainder selector nor its involution 2T-1 descends through literal observation. This is a full-rank spinor obstruction, including the actual 4+10 dimensions, not merely one witness. It is not a chirality no-go: an ambient spinor involution χ acting identically on every one-form slot DOES descend since P(1⊗χ)=(1⊗χ)P. Its relation to observed four-dimensional weak chirality remains a separate bridge.

Useful additional theorem: every linear augmentation Q=(P,L):A→B⊕W which makes T descend requires dimW≥s. Indeed kerQ⊂kerP and T-invariance force TkerQ⊂im(T)∩kerP=0, so kerQ⊂kerΓN. Thus L|kerP must separate the quotient kerP/kerΓN≅S. At dimW=s, exactly L(b,v)=Mb+A0ΓNv with A0 invertible works. This re-derives the pointwise minimum theorem independently of today's bet and gives a matrix-level necessary condition for the structural subclass which uses the ambient provenance selector. It does not require every GU mechanism to use that selector.

Pairing warning: descent of A is not descent of an action/current bilinear form B. A bilinear form factors through q in BOTH slots iff kerq lies in BOTH radicals of B. A Hermitian form needs its single radical condition. If B is nondegenerate and kerq≠0, literal bilinear descent fails even when A descends; physical reduction may instead restrict before quotient or use a different induced pairing. This distinction is reusable from existing Green-descent work, not claimed as novel.

Matrix requirement: For a subclass implementing observed orientation/chirality through an upstairs field selector A, its selector must preserve the actual observation/physical-quotient kernel. Literal 4+10 pullback has a rank-s obstruction for the ambient gamma-trace/remainder selectors, although slotwise spinor chirality descends. A linear augmentation retaining that provenance needs at least one spinor-sized extra output; this is not a requirement that all GU P1 realizations use provenance or an augmented receiver. Actual weak representation, pairing and dynamics remain unproved.

## B. P1 x symmetry: physical mirror symmetry, not charge conjugation
Let H=HL⊕HR be the actual observed complex carrier, with projections PL,PR. Let ρ:g→End(H) be the actual weak Lie-algebra action, commuting with PL,PR. A completely one-sided weak coupling means ρ(g)PR=0 for every g and ρ(g)PL≠0 for at least one g. Suppose an invertible linear S on H exchanges PL and PR and normalizes the actual weak action: Sρ(g)S^-1=ρ(αg), where α is a surjective Lie-algebra automorphism. Conjugating ρ(g)PR=0 yields ρ(αg)PL=0 for every g. Surjectivity of α then makes the left action zero as well, a contradiction. More generally the left and right weak modules are isomorphic up to α. No positivity, choice of specific action or assumption of a nonzero bulk index was used.

Consequently a C subfamily claiming genuinely one-sided observed weak coupling must not retain such a mirror normalizer on the full observed diagram. A background, observation, quotient, domain, or actual weak representation may remove it. Merely having equal ambient half-spin dimensions or an antilinear charge-conjugation map does not provide S. In particular antiparticle conjugation is not silently equated with a parity symmetry preserving the weak-current identification. If a bulk S is to descend, it must preserve kerq; if an unbounded physical operator/domain is invoked, S must preserve that SAME domain. Covariance relating different external backgrounds is not a fixed-background symmetry.

Exact controls: H=C², PL=diag(1,0), PR=diag(0,1), S=[[0,1],[1,0]]. Balanced current ρ(1)=I is S-invariant but not one-sided. Chiral current ρ(1)=diag(1,0) is left-only and nonzero but SρS^-1=diag(0,1)≠ρ; therefore allowed when mirror normalizer absent. This u(1) algebra control is not an SM or C action witness. Real charge conjugation K in this basis preserves both PL/PR, so no mirror criterion follows just from real matrices.

Matrix requirement: A nontrivial one-sided observed weak action excludes an invertible symmetry of the same observed carrier/domain that exchanges its left/right projectors while normalizing the weak representation. An ambient balanced or charge-conjugate pairing is insufficient to invoke this obstruction; the symmetry must descend through the actual observation/physical quotient and preserve the background, domain and weak-current identification. External orientation can break the fixed-background symmetry without violating covariance.

## Prior evidence / novelty map
- Aug30 observation-sector-obstruction: native real pairing + gamma-kernel leakage witness. Reuse its scope and algebra; full defect rank/selector descent and matrix implication are sharpening.
- Nov11 BET provenance observation: minimum linear separator classification. Reused and re-derived structurally; no bet status imported into matrix. It labels provenance, not P1 chirality.
- K2236 raw quotient and Nov11 BET mixing: actual operator closure is independent of provenance separation. Do not generalize its particular operator to C.
- Nov11 X-P2-P3 phase-domain-index: already proves phase does not select index and domains matter. The companion domain/index theorem concerns hidden/observed exact complexes rather than phase or domain restriction; do not claim Fredholm homotopy novelty.
- Aug07 source-graph-basicness: covariance of framed data is not fixed-quotient descent. Supports B's need to type a genuine observed normalizer.


## Local observed equations and variational descent are different requirements

Weak-current chirality does not require conserved chirality during massive propagation. The autonomy tests below apply only to a proposed exact autonomous observed sector; they do not impose that mechanism on every P1 realization. Covariant Dirac anticommutation with chirality is not the evolution commutator test.

These are structural tests for a linearized local quadratic subfamily, not a
postulated action in C. Freeze the actual background and real/complex pairing;
no bosonic quadratic criterion is silently transferred to Grassmann Hessians.
For a smooth surjection q:E→O and first-order evolution operator
D=A^μ∂μ+B on E, a first-order d=a^μ∂μ+b with qD=dq exists exactly when

    q A^μ = a^μ q,
    q B = a^μ (∂μ q) + b q.

Necessity is coefficient comparison on arbitrary section jets. Conversely these
identities give qD=dq by the product rule. Constant rank permits local smooth
right inverses, so a^μ and b, if they exist, are unique and patch. For coordinate-constant q in the chosen frames,
the test is invariance of ker q under every A^μ and B. Principal invariance alone
misses the second equation; moving observation adds ∂q even when fixed-plane
coefficients passed. No condition forces q to preserve an ambient chirality;
an observed grading must separately descend or be supplied on O. Unbounded
operators still require the actual closed-domain relation.

Choose nondegenerate Hermitian pairings on E and O, including the density, and let H denote the Hessian operator, not the pairing. For its formal selfadjointness,
consider the sesquilinear quadratic form Q(u)=<u,Hu>, H formally selfadjoint,
on compactly supported test sections. Literal off-shell descent through q means
Q(u+k)=Q(u) for EVERY u and EVERY compactly supported k in ker q. Polarization
shows this iff Hk=0 distributionally for every such k. In finite fibres or in
a chosen local smooth splitting, this is equivalent to H=q† h q for a formally
selfadjoint h on O. Proof: all mixed terms vanish, so only the observed-observed
block remains; use the splitting to construct h. The conclusion concerns
ordinary Hermitian forms and their declared pairing, not an undeclared
fermionic bilinear convention. It does not require positive H.

Thus a full quadratic form with zero radical on the stated test-section space cannot be pushed through a noninjective
q by simply forgetting hidden fields. This is NOT an obstruction to effective
observed dynamics: solving hidden equations is a different operation. For a
constant-coefficient block operator on a frozen local patch, work in the
commutative polynomial symbol ring R=C[p1,...,pd]. Write its blocks as

    H(p) = [[A(p), B(p)], [C(p), E(p)]], det E not identically zero.

On the rational-symbol locus det E≠0, eliminating the hidden component gives
S=A-B E^-1 C. S is a finite-order constant-coefficient differential symbol iff
every entry of B adj(E) C is divisible by det E in R. This follows entrywise
from the adjugate formula, since A is polynomial. Locality alone does not bound
order: if the claimed observed model is also required to retain the native principal-order bound, the resulting
polynomial must separately obey that degree bound. Nor does cancellation prove
an inverse on a global domain: zeros of det E, homogeneous hidden solutions,
boundary conditions and causal inverses remain separate.

Exact diagnostic matrices illustrate necessity, not C action candidates:
E=p²+1,B=C=1 has residual 1/(p²+1), so local input blocks do not force local
observed elimination. E=p²+1,B=C=E cancels exactly. E=1,B=C=p² is polynomial
but introduces degree4 in S when A has degree≤2, showing that successful
polynomial cancellation is not the order check. These are countercontrols for
the general theorem; no search over Lagrangians or coefficients is performed.

The class-C order bound applies to the native action; an effective observed action need not inherit that bound or locality.

P1xorder_locality: any subfamily claiming local autonomous observed propagation
must pass both coefficient equations; any subfamily using hidden elimination
must pass symbol cancellation plus the intended order/domain constraints.
P1xvariational: literal quadratic quotient needs ker q in the radical; a Schur
reduction or constrained physical quotient must state its distinct operation
and justify the actual hidden inverse/domain. Failure of literal descent alone
does not exclude the source's effective chiral-world claim.

## Evidence, acceptance and residual

Universal proofs above are separate from finite exact supporting/contrary controls in
[the probe](../../tests/program-focus/matrix_remaining_constraints_probe.py) and
[the report](../../lab/process/matrix-remaining-constraints.json). Independent internal
specialist review checks mathematics and source scope; this is not external review
or a Lean-certified class decision. RA-F1, AC-F1 and LT-SM8 remain NEEDS under physics
ledger0.263. Source register, class C, all canon and physical prediction grades are
unchanged. A constrained matrix entry records a useful necessary condition within
its explicit structural category; it does not establish that C inhabits that
category or settle all possible realizations.
