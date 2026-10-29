---
title: "K2233 Full raw Green pairings: curvature obstruction and flat transport"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all smooth local bilinear formal Green pairings for one supplied observed raw connection; no source action, physical quotient or positive-state exclusion
scripts:
  - tests/channel-swings/k2233_degree_dependent_raw_pairing_probe.py
---

# K2233 Full raw Green pairings distinguish curvature from positive evolution

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete smooth full raw Green pairing classification and curved positive-sector counterconstruction
carrier: supplied real1920 Cl77 observed-four raw carrier with invariant V1152 and complement C768 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: arbitrary smooth real bilinear formal Green G; separate positive reduced L2 current ON=declared_carrier
real_structure: ordinary conjugation in fixed real Clifford basis
grading: zero/one-form degree and Clifford parity; no physical chirality or family count
action_owner: repository-construction -- fixed observed principal matrices and shared raw lower coefficients
target: formal Green identity, flat transport and holonomy MAP-TYPE=intertwiner
```

Carrier: real1920 = (14 one-form slots plus one zero-form slot) tensor the fixed real128 Cl77 spinor. Four derivative coordinates O={0,7,8,9}; U denotes the ten unobserved slot indices. Pairings are arbitrary smooth real bilinear forms on this full raw carrier, including degree mixing, nonsymmetry and singularity. Normalized form H=Fcopy tensor B, Fcopy=diag(-I14,2). Real structure is ordinary real Clifford conjugation. Zero/one-form degree, Clifford parity, and formal-adjoint pairing are distinct from physical chirality, the positive evolution norm and a source bar. Action owner: repository construction. Target: exact formal Green coefficient identity under fixed coordinate measure and compactly supported tests. No source-selected operator or quotient.

## 1. Why this is a new question

K2199 already exhausts every full14 principal pairing: G=cH. Enlarging its degree ansatz does nothing. K2230's optional same-spinor parallel+normal-trace theorem also tensor-extends to a repeated full-slot carrier and cannot be escaped merely by renaming spinor G as a slot matrix. Neither theorem addresses the ACTUAL formal Green identity for K2230's shared raw lower coefficient on the observed-four derivative system. K2200 gives the complete principal-compatible family; K2206 classifies its constant mass-only members, leaving moving forms explicitly open. We consume those results and keep the actual raw returns.

Fix a smooth nowhere-zero real mass m on a connected open coordinate domain D in R4, using the fixed global raw/Clifford trivialization (constant nonzero m is sufficient). Put A=gamma0 J, T=product_U gamma_r, Cj=gamma0 gamma_j, Xj=Cj T. For an arbitrary smooth real one-form

    alpha=b dt + sum_(j=7,8,9) a_j dxj,

set

    Omega0=m A+sum a_j Xj, Omega7=b X7,
    Omega_k=0 for k not in {0,7}.
    L=sum_(k in O) D_k partial_k + K,
    K=sum D_k diag(Omega_k,...,Omega_k).

The scalar off-sector returns stay K[14,c]=-eta_c Omega_c; southeast remains zero. The same Omega acts in all fifteen slots; neither the lower adjoint nor the desired reduced equation is fitted separately. The normalized V1152=sum-zero U subspace and its Fcopy-orthogonal C768 complement are preserved by every coefficient. On V,

    L_V=-Gamma0 E_alpha,
    E_alpha=partial_t+sum Cj partial_j+mA-sum a_j Cj T-bT.

All coefficients retain K2230's B-normal trace identities. Positive Euclidean current on V is conserved for every alpha because its evolution potential is real-transpose skew. This does NOT assert that B is parallel or that a full raw Green form exists.

## 2. Complete smooth formal Green classification

Write the normalized arbitrary principal-compatible pairing as G=H X. K2200 proves, without an ansatz,

    X_V in Mat9(Dspin), X_C=I6 tensor Z, Z in Dspin,
    X_VC=X_CV=0,

where Dspin is the 1024-dimensional centralizer of all four Gamma_k=gamma_k Wbar. Formal Green compatibility is exactly

    sum D_k partial_k X = X K - K^sharp X.                 (1)

Each derivative has its distinct Clifford conjugation character chi_k, with + at k and - at the other three observed directions. The mass raw blocks have only characters ++++ and ----. Each coefficient a_j has character chi_j; b has chi_0. Their H-adjoints have the same characters. Here is an explicit full-block proof. Let M_k be K2200's scalar15-by15 principal matrices, E=JW, F=JWbar, and s0=-1 with all other one-form s_c=+1. The mass blocks are

    Kmass_ac=M0_ac s_c E (c<14), Kmass_ah=M0_ah F.

Both E,F are linear combinations of I,J. For a flavor generator Xj let sigma_c^(j)=-1 for c in U union {0,j}, and +1 otherwise, including auxiliary h. Since Xj is even and commutes with J, direct normalization gives R_c^-1 Xj R_c=sigma_c^(j) Xj. Therefore all original blocks are

    Ka_j_ac=M0_ac sigma_c^(j) Gamma_j T,
    Kb_ac=M7_ac sigma_c^(7) Gamma0 T.

The identities Gamma0 Xj=Gamma_j T and Gamma7 X7=Gamma0 T supply these expressions. T commutes with every Gamma_k, so Gamma_j T has exactly derivative character chi_j. Taking sharp transposes only the scalar slots and takes the B-adjoint; (Gamma_j T)^star=Gamma_j T. Thus sharp preserves the character. This proves the claim for ALL225 normalized original blocks, including the auxiliary returns. The six distinct characters separate (1).

The mass equation is exactly K2206's algebraic classification at every point, since m never vanishes (no derivatives of m occur: K is a zeroth-order coefficient in the formal Green identity):

    X_C=0, X_V in Mat9(Dodd), Dodd={Z in Dspin: ZJ=-JZ}.  (2)

In particular C768 is always the radical of a maximal-rank form, and is contained in every radical. Arbitrary mixed-degree/slot pairings cannot hide it. The remaining four equations, evaluated on V, are precisely

    partial_t X_V=b[T,X_V],
    partial_j X_V=a_j[T,X_V].                            (3)

Conversely (2)-(3) satisfy every full raw block of (1): all lower coefficients preserve the V/C split, and on V the exact raw transfer gives the displayed reduced operator. No other constraints occur.

A direct sign derivation: K_V=-Gamma0 N with N=mA-sum a_j CjT-bT, Gamma_k^star=-Gamma_k, T^star=-T, (CjT)^star=CjT, and X commutes with Gamma_k and hence with Cj. The a_j part of XK-Ksharp X is -Gamma_j a_j[T,X]; the b part is -Gamma0 b[T,X]. This matches the derivative side, whose coefficients are -Gamma_k.

## 3. Curvature kills formal pairings, while flat transport supplies all of them

The 512 adapted basis elements of Dodd are gamma_I Wbar, where I contains all four observed indices and an ODD subset of the ten normals. T commutes with each observed gamma and Wbar and anticommutes with every normal gamma. Therefore EVERY X in Mat9(Dodd) obeys

    {T,X}=0, [T,X]=2TX.                                  (4)

In particular commutation with T forces X=0. Taking crossed derivatives of (3) gives

    (d alpha)_(mu,nu) [T,X]=0.

If d alpha is nonzero at even one point, (4) forces X to vanish there. Along each piecewise smooth path, (3) is a homogeneous linear ODE with invertible conjugation transport, so zero propagates through the connected domain. Hence the ZERO FORM IS THE ONLY smooth local full raw Green pairing defined on the entire connected domain whenever d alpha is nonzero somewhere. Nonzero solutions can still exist on proper flat subdomains; the statement concerns extension across the full connected domain.

If alpha=dtheta, all pairings are

    X_V=e^(theta T) X0 e^(-theta T),
    X0 in Mat9(Dodd), X_C=0.                            (5)

The transport is H-congruence: T^star=-T and U=e^(theta T) preserves H on V, so Gtheta=U^(-T)G0 U^-1. It preserves symmetry, rank and inertia. Thus the solution spaces have real dimensions41472 for bilinear forms,20592 for symmetric forms and20880 for antisymmetric forms. Maximum rank is1152; every symmetric form has balanced inertia, with maximal inertia(576,576). These counts reuse K2206, while existence for the actual moving raw operator is the new result.

A maximal-rank witness is X0=I9 tensor Z*, Z*=gamma0 gamma7 gamma8 gamma9 gamma1 gamma2 gamma3 Wbar. It is B-selfadjoint, squares to2I and lies in Dodd. Since {T,Z*}=0, this witness genuinely moves for nonconstant theta. theta=epsilon sin(t)sin(x7) gives K2230's massive moving-observation operator and explicit nonzero full raw Green forms on it; these forms are necessarily singular and distinct from the positive reduced norm.

On a nonsimply-connected domain, assume d alpha=0. Transport along a loop of period p is X -> e^(pT)X e^(-pT)=e^(2pT)X. Since T^2=-I,

    e^(2pT)-I=(cos(2p)-1)I+sin(2p)T

is invertible unless p is in pi Z: its real inverse exists whenever (cos(2p)-1)^2+sin(2p)^2 is nonzero. Thus any nonzero global form exists iff EVERY period of alpha lies in pi Z. When this holds the entire local family descends, even though the spinor frame U can change sign around a loop. A half-angle-period example on a punctured observed plane is alpha=(1/2)dphi: its period is pi and all transported forms are single-valued while U has sign holonomy. alpha=(1/4)dphi has period pi/2 and kills all global forms, although nonzero local forms exist. This is a flat-bundle transport statement, not a claim that the global R3 spectral/domain result transfers to the punctured domain.

## 4. Strongest contrary construction: nonflat positive evolution still survives

Take b=0, a8=sin(x7), a7=a9=0 and constant nonzero m on R time x R3. Then (d alpha)78=cos(x7), so no nonzero full raw formal Green pairing exists. Nevertheless

    H_alpha=-i sum Cj partial_j -i mA +i sin(x7) C8 T

is the free selfadjoint H1 Hamiltonian plus a bounded Hermitian potential; its evolution is unitary and obeys the positive local current. The constant real orthogonal projector

    P=(I+gamma1 gamma2 gamma3 gamma4)/2

commutes with Cj,A,T and hence the entire reduced Hamiltonian. It has spin-rank64/V-rank576 (its Clifford involution is traceless). Thus nonzero, positive, conservative observed dynamics and a reducing projector survive despite complete absence of raw formal Green forms. No formal radical is being called gauge and no local projector is being called a positive-energy selector.

There is also a familiar variational countercontrol AFTER restricting to V and left-normalizing by -Gamma0. For commuting complex test fields u with compactly supported variations, the real quadratic functional

    S[u]=integral [(i/2)(u† partial_t u-(partial_t u†)u)-u† H_alpha u]

has Euler equation i partial_t u=H_alpha u, by independent variation of u and its conjugate and integration by parts. The spatial integrated term is real by formal selfadjointness of H_alpha. This is merely the ordinary complex Hamiltonian action for the already supplied positive subsystem; it chooses neither fermionic statistics nor a source four-field action. It is not a full1920 Green pairing, and it does not extend this subsystem functional to the original16cell grammar. The zero-form theorem is consequently not a no-action theorem after restriction and left normalization.

The nonflat theorem therefore cannot be promoted to failure of unitarity or GU. It instead shows exactly why a raw action pairing, a reduced positive current, connection parallelism, trace-Hq compatibility and a reducing observation require separate typed bridges.

## 5. Acceptance seams and controls

Weakest seam: proving that the complete raw flavor and b coefficients have derivative characters, not merely their restrictions, so the mass equations cannot be cancelled by derivatives. Check each normalized original raw block and sharp block for each generator m,a7,a8,a9,b. Check original bottom returns and V/C invariance. Then verify full225 Green equation with the independent Z* witness and derivative [T,Z*], checking mass, all three flavor directions, and b independently. Enumerate all512 Dodd adapted blades and verify T anticommutation; the written parity proof supplies universality, not the enumeration alone. Check a rational T-frame and moving full Green form, symmetry/rank witness, nonflat commutator defect, and P rank/current conditions. Useful genuine mutations: wrong raw return; lower coefficient order reversed; b sign; transport sign; drop curvature or halve the commutator; replace odd witness by even I; falsely accept pi/2 holonomy. Full14 cH exhaustion and tensor extension of K2230 are inherited controls, not novelty.

The scientific preflight compared the exhausted full14 degree-pairing route, a tensor renaming of the optional spinor same-G condition, and the actual observed raw Green identity. The last changes the mathematical question and produces the complete classification above. The hostile postflight challenged derivative cancellation, a hidden degree block, singular forms, global holonomy, and the false inference from formal-pairing failure to nonunitarity or absence of a subsystem action. The explicit flat/curved constructions and the separate pairing types preserve those countercontrols.

The exact native probe is `tests/channel-swings/k2233_degree_dependent_raw_pairing_probe.py`; its default execution checks a certificate bound to this note, the probe and reused dependencies. `--write` refreshes that certificate after review. Nine planted faults change raw return, coefficient order, temporal sign, transport sign, curvature factor, witness parity, loop holonomy, normal-volume input or projector grade. Each must fail an unchanged check after a green baseline. The original scratch construction checked full225 Green identities for all5 coefficient generators and all512 odd-blade anticommutations. Independent internal mathematical review of the actual proof found no blocker and required the full raw character controls before acceptance. Native numerical/control validation is distinct from the universal written proofs and independent review.

SC-OP-04 remains ASSERTS at candidate four-field grammar strength; SC-OP-05 and SC-META-53 remain UNCERTAIN. Source register loci: draft section9 extraction lines33 and116; TOE transcript01:22:30. No source-selected bar/action, source observation/section pullback, gauge quotient, empirical/family credit, ledger or canon change. No proof-assistant, external-expert or novelty certification. A changed principal/normal frame or changed raw returns remain outside this fixed raw theorem. Conditional next construction should test a genuinely changed principal/action class or a source-selected observation rather than seek another degree-dependent pairing inside the exhausted family.
