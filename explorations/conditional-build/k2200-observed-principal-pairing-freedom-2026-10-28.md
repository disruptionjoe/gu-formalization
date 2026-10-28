---
title: "K2200 Complete observed principal-pairing classification"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all zeroth-order bilinear pairings for the fixed four observed directions of the raw K1951 operator
scripts:
  - tests/channel-swings/k2200_observed_principal_pairing_freedom_probe.py
---

# K2200 Complete observed principal-pairing classification

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
result: complete bilinear-form classification for the fixed four-direction raw principal operator
carrier: K1951 real1920 one-form plus zero-form full Cl77 spinor carrier LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: initially arbitrary bilinear form G; complete observed centralizer classification ON=declared_carrier
real_structure: real matrix module; complex bilinear and Hermitian variants explicitly separated
grading: zero versus one-form degree and ambient Clifford chirality are distinct
action_owner: repository-construction: fixed four-direction raw principal operator, common form and optional transported lower terms
target: common formal-adjoint principal pairing MAP-TYPE=intertwiner
```

## Preflight and prior ownership

The operative object is exactly K2021's real1920 raw K77 principal operator, restricted to derivative covectors O={0,7,8,9}. It is not the source-selected fermion operator, the full14 derivative system, a physical observation map, or a positive evolution metric. SC-OP-04 ASSERTS candidate grammar only; source bar, reality, contraction and physical-state ownership remain unselected. Relevant routing: T02 (signature), T04 (observation), T09 (actions), T10 (adjoints), T11 (domains), T15 (positivity), T16 (pairing selection). No family, scalar-Higgs or source chirality inference is attempted.

K2199 already proves every full14 pairing is cH, including mixed degrees. K2034 already proves that observed restriction breaks rigidity, gives the V1152/C768 splitting,45 copy-scalar symmetric forms, maximal positive1408 graph and a successful massive1152 construction. K2036 and K2038 already test raw couplings and changed-class action extensions. None of those results is new here. The new result classifies every bilinear pairing on the full observed1920 carrier, with no degree, spinor, form-index, symmetry or nondegeneracy ansatz. It completes the observed commutant left open by K2034 and derives the fixed-operator moving-form condition.

## 1. Exact normalization

Write J=gamma0...gamma13, W=(3I-J)/2, Wbar=(3I+J)/2. Use the normalized fields

    zeta_a=eta_a gamma_a u_a,   nu=Wbar h.

Let R be this invertible block-diagonal change of coordinates. Its inverse blocks are gamma_a and W/2. With F=diag(-I14,2), the raw form becomes

    R^T H R=F tensor B.

For each k in O,

    R^-1 D_k R=M_k tensor Gamma_k,
    Gamma_k=gamma_k Wbar,
    {Gamma_k,Gamma_l}=4 eta_k delta_kl I.

The scalar15-by15 matrix M_k has the following complete entries:

    (M_k)_(a,c)=1 if a,c in0..13 and a,c,k are distinct;
    (M_k)_(k,h)=1;
    (M_k)_(h,k)=-1/2;
    all others0.

Thus M_k^T F=F M_k and Gamma_k^T B=-B Gamma_k. These identities follow directly from the original raw blocks, including the auxiliary signs. The finite probe reconstructs every one of the900 normalized blocks.

Let U={1,2,3,4,5,6,10,11,12,13}. In the15-dimensional scalar factor define V as the9-dimensional sum-zero U subspace, with other coordinates zero. Its F-orthogonal complement C has dimension6 and is spanned by h, the four observed unit vectors and the sum of U unit vectors. K2034's1152/768 splitting is exactly (V tensor S) direct-sum(C tensor S). Every M_k acts as -I on V.

## 2. Every spinor character, including all twisted sectors

Put T=sqrt(2)P_+ +P_- for ambient J projectors. Then

    Gamma_k=sqrt(2) T^-1 gamma_k T,   T^T B T=sqrt(2) B.

Conjugation by the four invertible Gamma_k gives four commuting involutions on End_R(S). Hence every spinor endomorphism splits uniquely into16 simultaneous commutation characters

    Z Gamma_k=epsilon_k Gamma_k Z, epsilon_k in{+1,-1}.

An explicit basis comes from all16384 ordered Clifford blades. For a blade I of degree r, its original character is epsilon_k=(-1)^(r-1_(k in I)); simultaneous conjugation by T preserves that character. A rationally scaled adapted basis is

    Z_I=gamma_I                 if r is even,
    Z_I=gamma_I Wbar            if r is odd.

The odd formulas differ from T^-1 gamma_I T only by the common nonzero factor sqrt(2). Independence is preserved: multiplication by Wbar is invertible on the odd subspace; the even subspace is untouched. The four independent parity equations give1024 basis members in each character. This is a decomposition of ALL End_R(S), not a selected grade ansatz.

For X=H_normalized^-1 G, principal compatibility is [X,M_k tensor Gamma_k]=0. In a fixed character its scalar coefficient A therefore obeys

    A M_k=epsilon_k M_k A.                         (1)

No assumption on the transpose or rank of A has been used.

## 3. Complete scalar intertwiner theorem

For each k, M_k preserves the plane P_k=span(e_k,h) and its13-dimensional coordinate complement. On P_k its matrix is [[0,1],[-1/2,0]], so M_k^2=-I/2. On the complement it is J13-I13, with eigenvalues12 and-1. In particular M_k is invertible. Its plane projector is the exact polynomial

    P_k=(4/867)(M_k^2-144I)(M_k^2-I).

Suppose one epsilon_k=-1. Anticommutation implies A commutes with M_k^2. It therefore preserves the three squared-eigenvalue subspaces. On the12 and-1 eigenspaces, anticommutation forces A=0, because the corresponding negative eigenvalue is absent. Thus A=P_k A P_k. Choose any other observed l. The concrete matrix M_l maps P_k into the coordinate complement of P_k: M_l h=e_l, and M_l e_k is the sum of the one-form unit vectors excluding k,l. Applying (1) to v in P_k gives

    0=A M_l v=epsilon_l M_l A v.

Invertibility of M_l forces A v=0, hence A=0. Every nontrivial character is eliminated, including nonsymmetric, singular and mixed-degree candidates.

Now all epsilon_k=+1. A preserves all P_k. Since their intersection is exactly span(h), A h=c h. The vector h is cyclic on C: M_k h=e_k, while for example M_7 e_0-e_8-e_9 is the U-sum vector. Therefore A=cI on C. The joint -1 eigenspace of all four M_k is exactly V: each such eigenvector has h and every observed coordinate zero by the P_k decomposition, and then its U coordinates sum to zero. Thus A preserves V and is arbitrary there. Conversely every such map commutes with the four M_k.

Consequently the complete scalar algebra is

    Mat9(R) on V  direct-sum R I_C.

The independent exact small-system control solves all16 characters with F-selfadjoint and F-skew conditions: the all-plus dimensions are46 and36, respectively; all other characters have dimension0. The universal proof above explains the result and does not depend on a numerical rank estimate.

## 4. Full bilinear and symmetric classification

Let D denote the1024-dimensional spinor centralizer of all Gamma_k. Every compatible bilinear form, uniquely, is G=H_normalized X where

    X|_(V tensor S) is an arbitrary9-by9 matrix with entries in D,
    X|_(C tensor S)=I_C tensor Z, Z in D,
    all V/C mixed blocks vanish.

Thus the complete bilinear space has real dimension

    (81+1)*1024=83968.

The B-adjoint of an adapted blade is Z_I^*=sigma_r Z_I, where sigma_r=(-1)^(r(r+1)/2). For the central character, either I is an even subset of U or I contains all four observed indices plus an odd subset of U. There are512 of each kind. The B-selfadjoint count is

    binom(10,0)+binom(10,4)+binom(10,8)
      +binom(10,3)+binom(10,7)=496;

the B-skew count is1024-496=528. These signs hold also for the odd adapted basis because Wbar^*=W and W gamma_I=gamma_I Wbar when r is odd.

On V, symmetric copy matrices (dimension45) pair with the496 selfadjoint spinor matrices, and skew copy matrices (dimension36) pair with the528 skew spinor matrices. On C only the scalar copy identity remains. Therefore EVERY real symmetric compatible form is in the exact41824-dimensional space

    45*496+36*528+496=41824.

The V-only contribution41328 strictly extends K2034's45 copy-scalar family. The complementary antisymmetric-form dimension is83968-41824=42144. Every statement here includes degenerate forms.

## 5. Inertia and explicit new witnesses

Every X above commutes with Q=I15 tensor Gamma0. The fixed form has Q^T H_normalized=-H_normalized Q, and Gamma0^2=2I. Thus every symmetric compatible G obeys

    Q^T G Q=-2G.

Congruence preserves inertia, so G has equal positive and negative indices even when degenerate. In particular every nondegenerate real symmetric compatible full form has inertia(960,960). The much larger observed pairing space does not produce a positive formal principal pairing. This is distinct from K2034's positive evolution norm on an invariant1408 graph.

A concrete spinor-sensitive witness beyond the copy-scalar family is Z=gamma1 gamma2 gamma3 gamma4. It lies in D, is B-selfadjoint, satisfies Z^2=I and has trace0. Set X=I on C tensor S and X=I9 tensor(2I+Z) on V tensor S. Its inverse uses (2I-Z)/3; G is compatible, nondegenerate, symmetric and outside the old copy-scalar ansatz.

For a degenerate witness instead use I+Z on V and I on C. The64/64 eigensplit of Z follows by conjugating it with gamma1. The total rank is576+768=1344, radical dimension576 and inertia(672,672). This gives an exact degeneracy control without claiming a physical null or gauge sector.

## 6. Fixed-operator differential consequence

Allow smooth pointwise compatible G(x) for the unchanged constant observed operator L=sum_(k in O)D_k partial_k. Its formal Green coefficient identity (equivalently formal self-adjointness when G is nondegenerate) is, besides principal compatibility,

    sum_k D_k partial_k X=0.                       (2)

Every derivative of X still lies in the classified commutant. The four terms D_k partial_k X occupy distinct spinor commutation characters: the k-th character has+ at k and- at the other three indices. Character independence separates (2) into D_k partial_k X=0. Each D_k is invertible, hence

    partial_k X=0 for all k in O.

On a connected four-dimensional observed patch all compatible forms for the unchanged operator are constant. If ambient normal coordinates remain external parameters, arbitrary dependence on those unused coordinates is allowed; the four-direction operator does not differentiate them. Moving the form along observed coordinates requires corresponding lower-order changes. K2034 already supplies that principle for its copy family; the new statement covers the full83968-dimensional bilinear class.

## Scope, contrary construction and reproducibility seam

Strongest overclaim:41824 formal pairings repair physical positive evolution, select the source's bar, or settle every observed coefficient. None follows. K2034's positive1408 evolution construction and K2036/K2038's changed-coefficient masses/actions are retained as contrary constructions to any GU-wide or all-mass exclusion. Full source-compatible lower-order coupling with a changed observed form remains a separate test; the K2028/K2036 fixed-H coefficient conclusions must not be transplanted to this larger family.

Weakest seam: silently identifying the original gamma blade characters with Gamma=gamma Wbar, or overlooking mixed V/C terms. The explicit T conjugacy, rational adapted basis, all-character scalar theorem and exact normalized original blocks address those seams. The sixteen exact rank systems are independent finite controls of the analytic scalar theorem. Internal calculations and review remain distinct from proof-assistant, external-expert, novelty or publication certification.

Postflight: the source-owned grammar/reality/observation boundary is unchanged; no source claim, hypothesis vote, physics ledger, canon, physical quotient, family count or generation result changes. Next substantive use must name an actual lower coefficient/observed constraint and test it against this full pairing family, or change the principal operator. Searching for another full14 pairing remains closed by K2199.
