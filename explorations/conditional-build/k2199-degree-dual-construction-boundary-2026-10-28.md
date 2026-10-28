---
title: "K2199 Rigidity of all common principal pairings"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all zeroth-order bilinear pairings for the fixed full fourteen-direction K1951 principal operator
scripts:
  - tests/channel-swings/k2199_degree_dual_construction_boundary_probe.py
---

# K2199 Rigidity of all common principal pairings

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete bilinear-form classification for the fixed raw principal operator
carrier: K1951 real1920 one-form plus zero-form full Cl77 spinor carrier LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: initially arbitrary bilinear form G; conclusion cH ON=declared_carrier
real_structure: real matrix module; complex bilinear and Hermitian variants explicitly separated
grading: zero versus one-form degree and ambient Clifford chirality are distinct
action_owner: repository-construction: fixed raw principal operator, common form and optional transported lower terms
target: common formal-adjoint principal pairing MAP-TYPE=intertwiner
```

## Result and prior construction

[K2021](k2021-common-degree-dual-operator-2026-10-24.md) already constructs
explicit R0/R1 maps, all sixteen principal-cell labels and the moving-density
Green identity. That construction is reused, not an unfilled input. The new
result is a complete classification: every real bilinear form G satisfying
D_k^T G+G D_k=0 for ALL FOURTEEN fixed principal matrices is cH. No symmetry,
Spin invariance, degree preservation or form-index ansatz is assumed.
Nondegeneracy requires c nonzero, and symmetry then follows automatically.
Every nonzero real form has inertia(960,960), so this fixed full principal
operator admits no positive definite form satisfying these formal-adjoint identities. The exact spectral
projection in section2 forces degree preservation, closing mixed-degree
pairings too. The claim concerns local zeroth-order forms, not different
operators, an observed-four-direction restriction or a physical quotient.

SC-OP-04 ASSERTS candidate four-field grammar, not this raw contraction or its
pairing. SC-META-53 remains UNCERTAIN. No source/ledger0.263, physical quotient,
LT-SM8/LT-GR6b/AC-F1, native2+1/chirality or canon change. No novelty or
proof-assistant/external-expert claim.

## 1. Full principal classification

Use K2021's exact real gamma matrices, eta with seven positive and seven
negative entries, J=gamma0...gamma13, W=(3I-J)/2, B=gamma7...gamma13,
and H=diag(eta_a B,B). Write E=(V* tensor S) direct-sum S. In block form,

    D_k = [[A_k, e_k],[-eta_k e_k^T,0]],
    (A_k)_ac=eta_a gamma_a gamma_k gamma_c W

when a,k,c are distinct, and zero otherwise; e_k injects S in slot k.
K2021 establishes D_k^T H=-H D_k. Hence, with X=H^-1 G,

    D_k^T G+G D_k=0  iff  [X,D_k]=0.

Degree preservation says X=diag(U,Z), with U initially an arbitrary
1792-by1792 matrix and Z an arbitrary128-by128 matrix. The upper-right
block gives U e_k=e_k Z for EVERY k. Therefore U_ak=delta_ak Z:
all form-index mixing is eliminated by the injection, not assumed away.
The upper-left block now states

    [Z,T_I W]=0 for every triple I, T_I=gamma_i gamma_j gamma_l.

J anticommutes with each odd triple, and J²=I. Thus

    (T_I W)(T_L W)=2 T_I T_L.

For any i!=j choose a,b distinct from i,j; triples (a,b,i),(a,b,j)
have product -eta_a eta_b gamma_i gamma_j. Z therefore commutes with
all bivectors. Products of bivectors span the even Clifford algebra.
In the full real Cl(7,7) module its centralizer is span_R{I,J}. This can
also be checked without a representation classification: in the faithful
ordered-blade basis, commuting with gamma_i gamma_j requires the two
membership bits of every nonzero blade to agree for all i,j; only the
empty and full sets survive. Consequently Z=alpha I+beta J. Commuting
with one invertible odd T_I W forces beta=0. This proves G=alpha H.
The zero form is included; no invertibility of G was used.

Over complex matrices the same proof gives cH with c complex for bilinear
forms. For Hermitian forms the real D_k have D_k^*=D_k^T, so c is real.
Neither complexification nor a nonsymmetric bilinear ansatz produces a new
compatible degree-preserving pairing for these fixed principal matrices.

## 2. Released successor: degree preservation follows from the equations

Drop the degree-preserving assumption on G and X entirely. Define

    Q=sum_(k=0)^13 eta_k D_k^2,
    C_ab=eta_a gamma_a gamma_b on V* tensor S.

The original block matrices give the EXACT identity

    Q=diag(264 C+47 I, -14 I),  C^2=14 C.                (8)

The mixed blocks vanish because A_k e_k=e_k^T A_k=0. The lower block is
sum eta_k(-eta_k I)=-14I. For an upper diagonal entry there are13*12
products of reversed triples, each contributing +2 after the outer eta_k
weight, and the injection contributes-1. Thus the diagonal is311I.
For a!=b there are12*11 products, each2 eta_a gamma_a gamma_b, giving264C_ab.
Since C_aa=I this is264C+47I. The sign of the reversed triple product is
positive; replacing it with the square of one ordered triple is incorrect.
The identity C²=14C follows directly from sum_b eta_b gamma_b²=14I.

It follows WITHOUT diagonalizing any1920-by1920 matrix that

    E0=(Q-47I)(Q-3743I)/229177=diag(0,I128).              (9)

Indeed the upper polynomial is264² C(C-14I)=0 and the lower value is
(-14-47)(-14-3743)=229177. Every arbitrary X commuting all D_k commutes
Q and E0, hence has zero mixed-degree blocks. Section1 then proves X=cI
and therefore G=cH. This closes ALL real bilinear pairings, including
nonsymmetric and degenerate ones. The complex and Hermitian conclusions
follow identically. The faithful gamma-trace factorization C=F G with
G F=14I128 also gives spectral multiplicities3743:128,47:1664,-14:128;
these are checks of the projector, not assumptions about an unknown pairing.

## 3. Coordinate and density consequences

For any smooth invertible C, let A_k=C^-1 D_k C.
A compatible bilinear form g has transformed form
C^-T g C^-1=cH, hence g=c C^T H C pointwise. Degree-compatible C includes K2021's odd
zero-form map and full one-form map; it is not a relabeling of external
ambient halves. A scalar density may be included in c.

If the full operator L is already formally self-adjoint for h and its
principal symbol is C^-1 D_k C, then replacing only h by c(x)h changes
its adjoint by

    L^(dagger_ch)-L = +c^-1 sum (partial_k c) A_k.

Thus the unchanged full operator is self-adjoint for the new form exactly
when D(dc)=0. Its upper-right injection is dc tensor I, so dc=0.
On a connected patch c is constant. This statement does not prohibit a
moving density with the corresponding lower-order half-density correction:
K2021 already supplies that different full operator.

When **all** operator, core injection and energy-form data are transported
by C, K2028's real fixed-core zero-only classification and separate complex
phase/vector image are invariant under that change of coordinates. Varying
R0/R1 within this fully transported class does not evade it. Arbitrary C
preserves the algebraic statement; preserving the source cell/ambient labels
additionally requires the declared compatible C. A changed core, contraction,
full lower coefficient or reality condition is a distinct branch with its
own reconstruction test. A mixed-degree pairing alone is now excluded too.

## 4. Earlier mixed-degree discriminator retained as a control

For a general X=[[U,p],[q,Z]], commutation instead yields

    q_k=-eta_k p_k,
    U e_k=A_k p+e_k Z,
    q A_k-eta_k Z e_k^T=-eta_k e_k^T U,
    [U,A_k]=eta_k p e_k^T+e_k q.

The injection argument alone no longer proves p=q=0. One plausible
Clifford-equivariant candidate p_a=s eta_a gamma_a W,
q_a=-s gamma_a W forces U_ac=24s eta_a gamma_a gamma_c for a!=c.
For k!=c, row k of A_k is zero, whereas
(U A_k)_kc=288s gamma_c W and the required right side is
q_c=-s gamma_c W. Thus289s=0. This calculation alone rejects only that ansatz. The separate spectral
projector proof in section2 now excludes every mixed-degree commutant.

## Verification and next condition

The probe checks exact Clifford signs and triple-product reduction, the
complete16384-blade even-centralizer census, the odd exclusion, injection
relations, density injectivity and the mixed candidate's289 obstruction.
These finite algebraic checks support the written universal block proof;
they are not a numerical1920-dimensional centralizer rank calculation.
Baseline-first mutations alter contraction/reality factors and must trigger
actual failed checks. K2021/K2028 banks are reused at unchanged dependencies.
Next work must genuinely change the principal/core or other load-bearing
dynamical data; searching another pairing for this same full principal
operator is settled. Fewer observed directions define a different problem.
