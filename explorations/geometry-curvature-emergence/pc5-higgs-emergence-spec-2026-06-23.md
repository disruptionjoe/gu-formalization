---
title: "PC5 — Higgs-like Scalar from Inner Fluctuations of the Distortion Tensor: Specification and Connes-Chamseddine Comparison"
date: 2026-06-23
problem_label: "pc5-higgs-emergence-spec"
status: exploration
verdict: CONDITIONALLY_RESOLVED
---

# PC5 — Higgs Emergence from Inner Fluctuations of the Distortion Tensor theta

## 1. Problem Statement

**What is being computed.** Lay out the first bounded specification for how a Higgs-like
scalar can emerge from inner fluctuations of the distortion tensor theta in the GU framework,
using the now-established:

- PC1 spinor decomposition: S = H^{64}, Cl(9,5) bimodule, S as coefficient bundle (not sub-bundle of Lambda^bullet)
- PC2 section pullback: s*(theta) = II_s^H (horizontal-normalized second fundamental form)

The computation compares the structural role to the Connes-Chamseddine (CC) inner-fluctuation
mechanism and identifies the precise representation-theoretic gate that must be cleared
for the Higgs to be a scalar under SU(2)_L x U(1)_Y.

**Why it matters.** GU is supposed to derive the Higgs sector geometrically, not impose it
by hand. The CC mechanism provides a mathematical template: the Higgs appears as an inner
fluctuation of the Dirac operator in a spectral triple, transforming as a scalar under the
gauge group and gaining a Mexican-hat potential from the spectral action. The question is
whether GU's distortion tensor theta, after section pullback, admits an analogous decomposition
in which a singlet scalar under SU(2)_L x U(1)_Y emerges.

**Scope.** This is a first-pass specification at exploration grade. The goal is to:
(1) State the candidate GU Higgs field in terms of theta and II_s^H.
(2) Identify its SU(2)_L x U(1)_Y transformation properties via the PC1 branching.
(3) Compare the structural mechanism to Connes-Chamseddine.
(4) State the precise representation-theoretic gate (the open condition blocking a verdict).

**Dependencies satisfied before this computation.**
- PC1 (CONDITIONALLY_RESOLVED): S = H^{64}, Cl(9,5) bimodule; S^+ branches under Spin(9,5) -> Spin(3,1) x Spin(6,4) as S(3,1) tensor S(6,4); S(6,4) = C^{16} branches under Pati-Salam -> SM as one generation; no natural map S -> Lambda^bullet (S is a coefficient bundle).
- PC2 (CONDITIONALLY_RESOLVED): s*(theta) = II_s^H; Codazzi equation [CodEq-Explicit] derived; soldering map j_s: N_s -> ad(P_s) constructed (IC1); IC2-IC4 Einstein equation emergence CONDITIONALLY_RESOLVED.
- HC1 (CONDITIONALLY_RESOLVED): theta decomposes as theta^(1) + theta^(2) + theta^(3) under SO(1,3) irreducibles; coupling coefficients k_i^{GU} = 512 P^(i).
- IC4 (CONDITIONALLY_RESOLVED): The GU Lagrangian term ||theta||^2 = ||B||^2 contributes to T^{dist,TF} and theta's vacuum dynamics are governed by D_A*theta = 0 (Noether).

---

## 2. Established Context

This computation builds on the following resolved results:

- **SM branching** (N5, generation-count-sm-branching-closure-2026-06-22.md):
  S(6,4) = C^{16} -> (4,2,1) + (4bar,1,2) under SU(4) x SU(2)_L x SU(2)_R (Pati-Salam)
  -> under SU(3) x SU(2)_L x U(1)_Y gives one SM generation:
  Q_L(3,2,1/6) + L_L(1,2,-1/2) + u_R_bar(3bar,1,-2/3) + d_R_bar(3bar,1,+1/3) + e_R_bar(1,1,+1) + nu_R(1,1,0).

- **PC2 section pullback** (4d-reduction-section-pullback-2026-06-22.md, ii-s-moving-frames-2026-06-23.md):
  s*(theta) = II_s^H in the horizontal-normalized convention; II_s^H = nabla^perp theta
  in the linear-distortion regime. Codazzi equation: nabla^perp II_s^H = R^{g_s}_{...} theta.

- **Soldering map** (ic1-soldering-map-ns-adps-2026-06-23.md):
  j_s: N_s -> ad(P_s) via j_s(n_i) = epsilon_i c(e^a) c(n_i) in sp(64); image is 10-dim
  (graviton TT 5 + vector 4 + dilaton 1) sub-bundle of sp(64); SO(1,3)-equivariant.

- **HC1 irreducible decomposition** (hc1-sl2c-bianchi-spinor-2026-06-23.md, hc1-coupling-coefficients-2026-06-23.md):
  theta decomposes as theta = theta^(1) + theta^(2) + theta^(3):
    theta^(1): traceless-tensor piece (type (3/2,1/2)+(1/2,3/2), 16 d.o.f.)
    theta^(2): trace-vector piece (type (1/2,1/2)_vector, 4 d.o.f.)
    theta^(3): axial piece (type (1/2,1/2)_axial, 4 d.o.f.)
  All three survive as irreducibles under SO(1,3).

- **PC4 torsion-for-Lambda** (pc4-torsion-lambda-derivation-2026-06-23.md):
  Lambda_eff = (1/8piG)(|theta^(1)|^2 + |theta^(3)|^2), with theta^(2) canceling in the
  canonical Gauss frame (alpha_2 = 1). theta has a scalar norm action ||theta||^2.

- **PC1 spinor structure** (pc1-spin77-spinor-decomp-2026-06-23.md):
  S is a coefficient bundle; Lambda^bullet acts on S via Clifford but S does not embed in
  Lambda^bullet. The bigraded complex Omega^bullet tensor S carries S throughout.

---

## 3. Computation

### 3.1 The Candidate GU Higgs Field

**Starting point: the distortion theta and its scalar singlet components.**

The distortion theta = A - Gamma is a Lie(Sp(64))-valued 1-form on Y^{14} (or on X^4 after
section pullback). Under the section pullback s*, we have:

    s*(theta) = II_s^H in Omega^1(X^4, ad P_s)

where P_s is the Sp(64) principal bundle over X^4 induced by the section s.

Under SM gauge group G_SM = SU(3) x SU(2)_L x U(1)_Y, the adjoint representation of Sp(64)
decomposes into SM-charged and SM-neutral pieces. The candidate Higgs must transform as a
scalar (0-form on X^4) in the fundamental representation (2, +1/2) of SU(2)_L x U(1)_Y.

**The inner fluctuation structure.**

In the Connes-Chamseddine template, inner fluctuations of the Dirac operator D -> D + A + JAJ*
(where J is the real structure of the spectral triple and A is a self-adjoint 1-form in the
algebra A) produce a field that, after the spectral action computation, decomposes into:
- A gauge field (1-form piece transforming in the adjoint)
- A scalar field (0-form piece transforming in the bifundamental between two algebras)
  which is the Higgs doublet under SU(2)_L x U(1)_Y.

The GU analog is: the distortion theta, after section pullback to X^4, decomposes according
to the Lorentz group SO(1,3) into:

    s*(theta) = II_s^H in Omega^1(X^4, ad P_s)

This is a 1-form on X^4 valued in ad(P_s) = Lie(Sp(64)) at the section. The candidate
scalar (Higgs-like) piece arises by further decomposing this 1-form under the SM gauge group
and picking out the scalar-under-SO(1,3) components.

**Step 1: The 0-form (scalar) component of II_s^H.**

II_s^H is an element of Omega^1(X^4, N_s*) where N_s* = Sym^2 T*X^4 is the conormal bundle
(the space of normal directions of the section s: X^4 -> Y^{14}).

Decomposing the 1-form II_s^H as a tensor:

    II_s^H in Gamma(T*X^4 tensor Sym^2 T*X^4 tensor ad P_s)   [schematically]

Under SO(1,3), the T*X^4 factor (a 4-vector) and the Sym^2 T*X^4 factor (the normal bundle
direction, which is the SM-sector) give a product representation.

In index notation:
    (II_s^H)_{mu; ab}  [mu = spacetime 1-form index; ab = normal bundle indices from Sym^2 T*X^4]

Contracting the T*X^4 and Sym^2 T*X^4 factors using the 4D metric g_{s,mu nu}:

    phi_{ab} = g_s^{mu nu} (II_s^H)_{mu; nu(a)} e_b  [naive trace contract]

This is not the right contraction; it mixes the 1-form index with the normal-bundle index.
The correct scalar extraction is via the trace of the normal-bundle piece. Let us be precise.

**Step 2: Normal bundle decomposition and scalar identification.**

The normal bundle N_s = Sym^2 T*X^4 has dimension 10. Under SO(1,3), it decomposes as:

    Sym^2(R^{3,1}) = R (trace = scalar) + Sym^2_0(R^{3,1}) (traceless)

where R is the 1-dimensional trace piece (the dilaton direction) and Sym^2_0 has dimension 9
(which further decomposes as the graviton TT piece and the Ricci/scalar piece).

The scalar piece (trace of the normal bundle) corresponds to:

    phi_scalar = Tr_{g_s}(II_s^H)  (the mean curvature scalar, trace of the second fundamental form)

This is a scalar field on X^4 (a 0-form), valued in ad(P_s) restricted to the scalar
direction in N_s. Specifically:

    phi_scalar in Gamma(X^4, ad(P_s)|_{scalar normal direction})

**Step 3: The Sp(64) representation content of phi_scalar.**

The scalar-direction in N_s corresponds to the conformal-factor fluctuation of the section.
Under the j_s soldering map (IC1 file):

    j_s: N_s -> ad(P_s) subset sp(64)

The 1-dimensional trace piece of N_s (the dilaton direction n_0 = g_{ab} n^{ab} / sqrt(4))
maps to:

    j_s(n_0) = epsilon_0 c(e^a) c(n_0) in sp(64)

This is a specific element of sp(64) = Lie(Sp(64)). As a representation of Spin(9,5), it
transforms in the adjoint of Sp(64).

Under the SM branching (step by step via Pati-Salam):

    Sp(64) -> [embedding via Spin(6,4) -> SU(4) x SU(2) x SU(2)] -> SU(3) x SU(2)_L x U(1)_Y

The adjoint representation of Sp(64) decomposes under G_SM. To find the Higgs, we need to
identify which component of adj(Sp(64)) contains the (1, 2, 1/2) representation of G_SM.

**Step 4: The representation-theoretic gate.**

This is the precise gate that must be cleared for the Higgs to emerge as a scalar under
SU(2)_L x U(1)_Y.

The question is:

  [GATE-H1]: Does the adjoint representation of Sp(64), decomposed under the SM gauge
  subgroup (embedded via S(6,4) -> one Pati-Salam generation), contain a piece transforming
  as (1, 2, +1/2) under SU(3) x SU(2)_L x U(1)_Y?

We can reason about this as follows:

**Sp(64) adjoint content under Sp(2n) -> U(n) branching.**

The adjoint of Sp(2n) (= Sp(n) in the convention Sp(n) = U(n, H)) decomposes under U(n) as:
    adj(Sp(2n)) = Sym^2(C^n) + conj(Sym^2(C^n))   [reconstruction, standard branching]

where n = 64 in our case (Sp(64) with spinor module S = H^{64}).

More concretely, the spinor module S = H^{64} over H, viewed over C, gives S_C = C^{128}.
The Sp(64) fundamental acts on H^{64} = C^{128} and the adjoint = Sym^2_H(H^{64}) over H,
which over C is Sym^2_C(C^{128}) with a quaternionic reality condition.

For the Higgs branching, the critical sub-group is NOT the full U(64) but rather the
SM-embedded subgroup G_SM sitting inside Sp(64) via the Pati-Salam chain:

    Sp(64) -> ... -> SU(4) x SU(2)_L x SU(2)_R -> SU(3) x SU(2)_L x U(1)_Y

The Higgs doublet (2, +1/2) under SU(2)_L x U(1)_Y can arise from the bifundamental
representation (2_L, 2_R) under SU(2)_L x SU(2)_R, which decomposes under SU(2)_L x U(1)_Y
(with Y = T_{3R}) as (2, +1/2) + (2, -1/2) = Higgs doublet + conjugate.

**Step 5: The SU(2)_L x SU(2)_R bifundamental from theta.**

In the Pati-Salam framework, the Higgs doublet transforms as:

    H in (1, 2, 2) under SU(4) x SU(2)_L x SU(2)_R

which breaks down to (1, 2, +1/2) + (1, 2, -1/2) under G_SM.

For this to come from theta, we need:

    theta (or a component thereof), after section pullback and SM branching, to have a
    (1, 2, 2) component under the Pati-Salam subgroup of Sp(64).

**Step 6: The distortion theta in the Pati-Salam decomposition.**

The gauge field A in the Sp(64) bundle, after section pullback, decomposes under the
SM embedding. The distortion theta = A - Gamma also decomposes. In the SM vacuum (where
Gamma is the LC connection):

    s*(theta) = II_s^H = nabla^perp_A theta_LC_approx

The piece of theta transforming as (1, 2, 2) under Pati-Salam would be an off-diagonal
block of the Sp(64) gauge field connecting the SU(2)_L doublet sector to the SU(2)_R
doublet sector within the S(6,4) = C^{16} fiber.

In the Pati-Salam decomposition S(6,4) = (4, 2, 1) + (4bar, 1, 2):

    adj(Sp(64))|_{Pati-Salam} contains: [among other pieces]
    Hom((4,2,1), (4bar,1,2)) = (4 x 4bar, 2, 2) = (singlet+adjoint, 2_L, 2_R)

The (1, 2, 2) component of Hom((4,2,1), (4bar,1,2)) is the singlet-of-SU(4) piece:
    (1, 2, 2) under SU(4) x SU(2)_L x SU(2)_R   [reconstruction]

This is precisely the Higgs bidoublet.

Therefore:

    CANDIDATE: phi_Higgs = s*(theta)_{(1,2,2) Pati-Salam component}

This is the component of the pullback distortion theta that transforms as the Higgs bidoublet.

### 3.2 Comparison with Connes-Chamseddine Inner Fluctuation

**CC mechanism (Connes-Chamseddine, 1996 and subsequent).**

In the CC noncommutative geometry (NCG) approach:

1. **Spectral triple**: A = C^infty(M) tensor (C + H + M_3(C)), H = Hilbert space of SM fermions, D = Dirac operator.

2. **Inner fluctuations**: D -> D_A = D + A + epsilon' J A J* where A = a[D,b] for a,b in A, and J is the real structure (charge conjugation).

3. **Field content**: The inner fluctuations produce:
   - A gauge boson sector (from the commutative part A = C^infty(M)): the SM gauge fields.
   - A scalar sector (from the finite-dimensional part of A = C + H + M_3(C)): the Higgs doublet.
   The scalar emerges because the finite algebra A contains inter-summand (off-diagonal) elements.

4. **Higgs as off-diagonal inner fluctuation**: The (C -> H) transition in A = C + H + M_3(C) produces an off-diagonal fluctuation. Acting on the SM Hilbert space H, this gives a field transforming in the (1, 2, 2) of the Pati-Salam algebra (equivalently (2, +1/2) of SU(2)_L x U(1)_Y after weak hypercharge assignment).

5. **Mexican hat potential**: The spectral action S_b[D_A] = Tr(f(D_A^2/Lambda^2)) expanded in powers of D_A produces, after the heat-kernel expansion, a quartic-plus-quadratic potential for the Higgs scalar with the correct Mexican-hat shape.

**GU analog (this computation).**

The structural parallel:

| CC mechanism | GU analog |
|---|---|
| Algebra A = C + H + M_3(C) | Gauge group Sp(64) (containing SM embedding) |
| Inner fluctuation A = a[D,b] | Distortion theta = A - Gamma |
| J real structure (charge conjugation) | Quaternionic structure J: H^{64} -> H^{64} (J^2 = -1) |
| D -> D + A + JAJ* | D_GU already contains both A and the Clifford coupling to Gamma via theta |
| Off-diagonal A in algebra | Off-diagonal theta in Sp(64) relative to Pati-Salam block structure |
| Higgs = off-diagonal finite-algebra part | phi_Higgs = theta_{(1,2,2) Pati-Salam block} |
| Spectral action gives Mexican hat | GU distortion action ||theta||^2 gives ||phi_Higgs||^2 + (mass term) |
| Higgs mass from D^2 heat kernel | Higgs mass from Willmore energy E[s] = integral ||II_s||^2 |

**Key structural difference: GU Higgs comes from geometry, not algebra.**

In CC, the Higgs arises from the finite-dimensional algebra A (an input). In GU, the Higgs
candidate arises from the second fundamental form II_s^H of the section s: X^4 -> Y^{14}.
This is a geometric origin:

    phi_Higgs ~ (II_s^H)_{(1,2,2)} = (geometric curvature of embedding)_{Higgs block}

This is the precise GU alternative to CC: instead of an algebraic inner fluctuation A, the
Higgs comes from the geometric inner fluctuation of the section (a change in how X^4 sits
inside Y^{14}).

**The J real structure parallel.**

In CC, the inner fluctuation A + epsilon' J A J* (with epsilon' = +1 for even spectral triple)
uses J to produce a "doubled" field. In GU, the quaternionic structure J: S = H^{64} -> H^{64}
(with J^2 = -1, the quaternionic imaginary) plays an analogous role:

    J: H^{64} -> H^{64}, J^2 = -1, J anti-commutes with Clifford action [reconstruction]

This gives the pseudoreal structure that is the origin of the Sp(64) gauge group (as opposed
to U(64, C)). The distortion theta, as an element of sp(64) = Lie(Sp(64)), respects this
J-structure: theta in sp(64) means J theta J^{-1} = theta* (theta is J-anti-Hermitian).

The J-doubling in CC corresponds in GU to the quaternionic reality condition on theta.
The Higgs bidoublet (1, 2, 2) is the off-diagonal (between SU(2)_L and SU(2)_R) component
that is J-invariant (it maps the (4,2,1) part of S(6,4) to the (4bar,1,2) part).

### 3.3 The Representation-Theoretic Gate: Scalar Under SU(2)_L x U(1)_Y

**GATE-H1: Does the (1, 2, 2) Pati-Salam component of adj(Sp(64)) exist?**

For the Higgs to arise from the distortion, the component:

    theta_{(1,2,2)} in (1, 2, 2) of SU(4) x SU(2)_L x SU(2)_R subset Sp(64)

must exist in adj(Sp(64)). This is a concrete question about the branching rule:

    adj(Sp(64)) |_{G_{PS}} = ?   where G_{PS} = SU(4) x SU(2)_L x SU(2)_R

**Partial resolution at exploration grade.**

The adjoint of Sp(64) under the SM embedding via S(6,4) = (4,2,1) + (4bar,1,2):

The Sp(64) spinor module is S = H^{64} = C^{128} (over C). The S(6,4) piece contributes
C^{16} = (4,2,1) + (4bar,1,2) (8+8 complex dimensions). The adjoint of Sp(64) contains
the symmetric tensor Sym^2_H(H^{64}) which over C includes Sym^2_C(C^{128}).

Under the Pati-Salam embedding, Sym^2_C(C^{128}) contains:

    Sym^2((4,2,1) + (4bar,1,2)) = Sym^2(4,2,1) + Sym^2(4bar,1,2) + (4,2,1) tensor (4bar,1,2)

The last term:
    (4,2,1) tensor (4bar,1,2) = (4 x 4bar, 2, 2) = (1 + 15, 2, 2) under SU(4) x SU(2)_L x SU(2)_R

The singlet-of-SU(4) piece:
    (1, 2, 2) in (4 x 4bar, 2, 2)

This (1, 2, 2) IS present in adj(Sp(64)) restricted to the Pati-Salam subgroup
embedded via S(6,4).   [reconstruction]

Therefore GATE-H1 is CONDITIONALLY RESOLVED at reconstruction grade:

    phi_Higgs = theta_{(1,2,2)} in (1, 2, 2) of G_{PS} exists as a component of adj(Sp(64))

**GATE-H2: Does phi_Higgs survive as (1, 2, +1/2) under SU(2)_L x U(1)_Y after Pati-Salam breaking?**

Under the Pati-Salam -> SM breaking SU(4) -> SU(3) x U(1)_{B-L} and SU(2)_R x U(1)_{B-L} -> U(1)_Y:

    (1, 2, 2) under SU(4) x SU(2)_L x SU(2)_R
    = (1, 2, +1/2) + (1, 2, -1/2) under SU(3) x SU(2)_L x U(1)_Y

where the decomposition under SU(2)_R x U(1)_{B-L} -> U(1)_Y gives the doublet of SU(2)_R
(2_R) -> (+1/2)_Y + (-1/2)_Y by the Gell-Mann-Nishijima formula Y = T_{3R} + (B-L)/2.

For the singlet (B-L = 0 from the SU(4)-singlet piece): Y = T_{3R}, so the SU(2)_R doublet
gives Y = +1/2 and Y = -1/2.

    phi_Higgs|_{H1} = theta_{(1,2,+1/2)} in (1, 2, +1/2) of SU(3) x SU(2)_L x U(1)_Y

This IS the Higgs doublet quantum numbers.   [reconstruction]

GATE-H2: CONDITIONALLY_RESOLVED at reconstruction grade.

**GATE-H3: Is phi_Higgs a 0-form (Lorentz scalar) on X^4?**

The distortion theta = A - Gamma is a 1-form on X^4 valued in sp(64). The Pati-Salam
(1, 2, 2) component is a 1-form:

    theta_{(1,2,2)} in Omega^1(X^4) tensor (1, 2, 2)_{sp(64)}

This is a 1-form (a vector boson), NOT a scalar. For a Higgs scalar (0-form), we need
a different mechanism.

**Resolution: the scalar comes from the internal degree-of-freedom, not the spacetime index.**

The correct identification: the SCALAR Higgs is the internal-space component, not the
spacetime component. In the CC framework, the inner fluctuation scalar arises from the
finite-algebra direction (which is "0-form in spacetime" because the finite algebra has
no spacetime index). In GU, the analogous construction is:

The normal bundle N_s = Sym^2 T*X^4 contains a scalar component: the trace direction
n_0 = g^{ab} n_{ab} / sqrt(4) (the dilaton mode, as identified in the IC1/IC2 files and
the rfail-umbilic analysis).

However, the dilaton (1, 1, 0) under G_SM is NOT the Higgs (1, 2, +1/2). For the Higgs
to be a scalar, we need to find a different mechanism.

**The correct mechanism: theta contracted along the fiber direction.**

The section pullback s*(theta) = II_s^H is a 1-form on X^4. However, the GU distortion
also has a component along the FIBER direction of Y^{14} -> X^4. Specifically:

Consider the normal-fiber component of theta at the section:
    theta^{vert} = (theta valued in the vertical tangent space of Y^{14} at the section)
    = (theta evaluated on vertical vector fields at s(X^4))

The vertical tangent space of Y^{14} at s(X^4) is the tangent space to the fiber
GL(4,R)/O(3,1) at the point s(x) = g_s(x). This is a 10-dimensional space (isomorphic
to Sym^2_0(R^4) + R via the trace decomposition).

For 0-forms on X^4, we need the spacetime-scalar part: a field that has no free spacetime
index mu but may have fiber indices.

**Theta's fiber component as the GU Higgs candidate.**

Define:
    phi^{(1,2,2)}_H = (theta evaluated on the fiber-Pati-Salam-off-diagonal direction)

More precisely, using the frame {E_a^H, F_{(bc)}} (horizontal and vertical frame vectors
on Y^{14} from the ii-s-moving-frames file), evaluate theta on the vertical frame:

    phi_{(bc)} = theta(F_{(bc)})  in sp(64)   for b <= c (normal-bundle components)

This is a map from the normal-bundle indices (b,c) of the fiber to sp(64). After decomposing
under Pati-Salam, the (1, 2, 2) component:

    phi_H = phi_{(bc)}|_{(1,2,2)}  in Omega^0(X^4) tensor (1, 2, 2)_{sp(64)}

This IS a scalar field on X^4 (no spacetime index mu, because we evaluated theta on a
vertical = normal-to-section direction).   [reconstruction]

This is the GU analog of the CC inner fluctuation scalar:

    CC: phi_H arises from the finite-algebra (non-spacetime) inner fluctuation direction.
    GU: phi_H arises from the fiber (normal-to-section) component of theta.

GATE-H3: CONDITIONALLY_RESOLVED at reconstruction grade.

**GATE-H4 (the representation-theoretic master gate): The Pati-Salam-to-SM Higgs branching in sp(64).**

The definitive check is:

Given the SM embedding G_SM = SU(3) x SU(2)_L x U(1)_Y -> Sp(64) constructed via:

    Cl(9,5) -> Cl(6,4) = M(16,C) -> SU(4) x SU(2)_L x SU(2)_R acting on S(6,4) = C^{16}

the adjoint of Sp(64) restricted to G_SM contains the representation (1, 2, +1/2) of G_SM.

**This is the precise statement to verify by explicit branching computation.**

The branching chain:
    adj(Sp(64)) |_{Sp(16)} -> adj(Sp(16)) + (Sym^2(H^{16})/adj(Sp(16))) + ...
    adj(Sp(16)) |_{SU(4) x SU(2)_L x SU(2)_R} -> [Pati-Salam branching]
    [Pati-Salam piece] |_{SU(3) x SU(2)_L x U(1)_Y} -> ... + (1, 2, +1/2) + ...

At exploration grade, we have established:
- The (1, 2, 2) piece exists in adj(Sp(64)) via the S(6,4) tensor product structure (Step 3.3).
- Under Pati-Salam breaking, (1, 2, 2) -> (1, 2, +1/2) + (1, 2, -1/2).
- The Higgs doublet (1, 2, +1/2) is present.

The representation-theoretic gate that must be cleared for RESOLVED status:

[GATE-H4]: The explicit branching computation of adj(Sp(64)) |_{G_SM} = ?
  specifically: does (1, 2, +1/2) appear with multiplicity >= 1?

From the exploration-grade argument above: YES, at reconstruction grade.

A CAS computation (LiE, SageMath) of the branching
    adj(Sp(32)) |_{SU(4) x SU(2) x SU(2)}  (for the Sp(16) subset of Sp(64) acting on S(6,4))
would confirm this and upgrade from reconstruction to verified.

### 3.4 The GU Mexican Hat Potential

**From the GU distortion action.**

The PC4 derivation (pc4-torsion-lambda-derivation-2026-06-23.md) gives:

    Lambda_eff = (1/8piG)(|theta^(1)|^2 + |theta^(3)|^2) + O(nabla theta)

The Higgs field phi_H is the (1, 2, +1/2) component of theta in the fiber direction.
The GU action includes ||theta||^2 = ||phi_H||^2 + (other components). The potential
for phi_H is:

    V(phi_H) = lambda_1 ||phi_H||^4 + mu^2 ||phi_H||^2 + (cross terms from other theta pieces)

where lambda_1 and mu^2 are coefficients inherited from the GU Lagrangian.

For the Mexican hat shape, we need mu^2 < 0. In the CC framework, this arises from the
spectral action's quadratic term with a specific sign. In GU:

The mass term mu^2 for phi_H is determined by the Willmore energy Hessian at the vacuum
section. From the CPA-1 computation (cpa1-tobs-coefficient-2026-06-23.md, Lichnerowicz
eigenvalue lambda_2 = 8/R^2):

    mu^2 ~ -8/R^2 (negative mass squared, tachyonic direction at the vacuum s_LC)

Wait -- the sign requires care. The Lichnerowicz eigenvalue lambda_2 = 8/R^2 > 0 is the
STABILITY eigenvalue (the section is a minimum of E[s] in TT directions). But for the Higgs
to have a Mexican hat, we need the Higgs direction to be an UNSTABLE direction (negative Hessian).

**Identification of the Higgs tachyonic direction.**

The Willmore energy E[s] = integral ||II_s^H||^2 is minimized by the tautological section
s_LC (with II_s^H = 0 for the LC section). The Hessian around s_LC has eigenvalues:

- Positive: TT graviton modes (lambda_2 = 8/R^2, Lichnerowicz modes)
- Zero: zero modes (Killing vectors, section symmetries)
- Negative (potential): modes corresponding to the internal scalar components

For the Higgs to have a Mexican hat, the (1, 2, +1/2) direction in the fiber must be a
direction of negative curvature of E[s] around s_LC. This is NOT guaranteed by the
Willmore energy alone; it requires a contribution from the GU spinor mass term
(Dirac-DeRham coupling) or from the gauge curvature term.

**The mass-from-gauge-coupling mechanism (CC-analog).**

In CC, the Higgs mass (negative mass squared) comes from the coupling:
    D^2_{Higgs} = (partial + A)^2 -> -mu^2 |phi|^2 from the finite-space D^2 term.

In GU, the Dirac-DeRham operator D_GU couples to phi_H through the spinor:
    <Psi, D_GU Psi> = <Psi, c(theta) Psi> + ... = phi_H * (fermion bilinear) + ...

The fermion bilinear gives a Coleman-Weinberg-type contribution to the Higgs potential.
At one loop:

    Delta V(phi_H) ~ -(N_f / 16pi^2) m_f^4 log(m_f^2/mu^2)

where m_f is the fermion mass from the Yukawa coupling in the GU Lagrangian.

For a large top-quark Yukawa coupling (as in the SM), Delta V produces a negative mass
squared for phi_H: the radiative symmetry breaking mechanism. In GU, the Yukawa coupling
comes from the (Psi^dag, c(phi_H), Psi) term in the Dirac-DeRham action. The coefficient
is fixed by the Sp(64) Clifford algebra and the Pati-Salam branching -- it is determined by
the representation-theoretic structure, not a free parameter.

This is the GU analog of the CC spectral action Higgs mass term. Status: exploration grade.

### 3.5 Structural Summary: GU vs CC

| Item | Connes-Chamseddine | GU analog | Status |
|---|---|---|---|
| Mathematical arena | Spectral triple (A, H, D) | Geometry of s: X^4 -> Y^{14} with D_GU | established |
| Source of Higgs | Finite-algebra inner fluctuation | Fiber component of theta = A - Gamma | exploration |
| J-structure role | Real structure J, JAJ* doubling | Quaternionic J: H^{64} -> H^{64} in Sp(64) | reconstruction |
| Higgs quantum numbers | (1, 2, +1/2) from algebra | (1, 2, +1/2) from adj(Sp(64)) branching | reconstruction |
| Mexican hat mass | Spectral action quadratic term | Willmore Hessian + radiative correction | exploration |
| Mexican hat quartic | Spectral action quartic term | ||theta||^4 in GU distortion action | exploration |
| Symmetry breaking | D^2 spectral computation | GU section selection + fermion loop | exploration |
| Yukawa couplings | Off-diagonal D finite-space elements | c(phi_H) Dirac-DeRham coupling | exploration |
| Uniqueness | Determined by (A, H, D) | Gated on GATE-H4 branching | open |

---

## 4. Result

### 4.1 Verdict

**VERDICT: CONDITIONALLY_RESOLVED**

The first bounded specification for the GU Higgs emergence mechanism is established at
exploration/reconstruction grade. The candidate Higgs field is:

    phi_H = (fiber component of theta in the (1,2,2) Pati-Salam direction of adj(Sp(64)))
           = s*(theta)^{vert}_{(1,2,+1/2)}   (fiber-pullback, Higgs block)

The structural mechanism parallels Connes-Chamseddine with the substitution:
    finite-algebra inner fluctuation -> fiber component of the distortion theta.

The representation-theoretic gate that must be cleared (GATE-H4):

    adj(Sp(64))|_{G_SM} contains (1, 2, +1/2)

is CONDITIONALLY_RESOLVED at reconstruction grade from the explicit Pati-Salam tensor
product decomposition (Section 3.3, Step 6). A CAS branching computation would confirm.

### 4.2 Explicit Failure Conditions

**F1 (GATE-H4 fails: no Higgs block in adj(Sp(64))).**
If the (1, 2, +1/2) representation does NOT appear in adj(Sp(64))|_{G_SM}, then the
distortion theta cannot produce a Higgs doublet. This would require the Pati-Salam
(4,2,1) x (4bar,1,2) -> (1,2,2) branching to be absent from Sym^2_C(C^{128}), contradicting
the tensor product rule (4 x 4bar contains 1). F1 is very unlikely but requires explicit CAS confirmation.

**F2 (No scalar 0-form: all theta components are 1-forms).**
If the fiber component of theta (the "vertical" piece evaluated on normal-bundle vectors)
does not transform as a 0-form on X^4, the Higgs would be a vector boson, not a scalar.
The fiber component is 0-form by construction (it has no free spacetime 1-form index);
this is the key step requiring verification (that "evaluating theta on vertical vectors"
is well-defined at the section, which requires the connection-evaluation map to be smooth
at the section s(X^4)).

**F3 (Yukawa coupling wrong sign or zero).**
If the Dirac-DeRham coupling <Psi, c(phi_H) Psi> has the wrong sign or vanishes at the
Pati-Salam (1,2,2) block, no symmetry breaking occurs from the fermion loop. This would
require an explicit computation of the (1,2,2) Clifford matrix element in Sp(64) -> 0.

**F4 (Mexican hat potential does not emerge).**
If the GU scalar potential for phi_H is monotone (no Mexican hat) -- either because the
quartic term is absent or the mass^2 is positive -- then electroweak symmetry breaking
does not occur. This requires a full CAS computation of the GU effective potential.

**F5 (Pati-Salam breaking not geometric).**
If the GU construction does not provide a mechanism for SU(4) -> SU(3) x U(1)_{B-L}
breaking, the Pati-Salam (1, 2, 2) does not become the SM (1, 2, +1/2). This is a
separate step from Higgs emergence; it requires a second Higgs-like field (a (1, 1, 0)
under G_SM with a B-L charge) to trigger Pati-Salam breaking, which GU has not yet specified.

**F6 (J-invariance condition fails).**
If the quaternionic structure J: H^{64} -> H^{64} does not preserve the (1, 2, +1/2)
block in the sense that phi_H is not a J-invariant element of adj(Sp(64)), then the Sp(64)
reality condition forces phi_H to vanish. This requires explicit J-action computation on
the Higgs block.

### 4.3 Open Questions

**OQ1 (CAS branching: GATE-H4).** Compute adj(Sp(16))|_{SU(4) x SU(2) x SU(2)} explicitly
using LiE or SageMath and confirm that (1, 2, +1/2) appears with multiplicity >= 1 after
the Pati-Salam -> SM breaking. This is the single highest-priority computation for PC5.

**OQ2 (Fiber-component construction).** Make precise the construction "theta evaluated on
vertical vectors at the section." The correct formulation uses the connection 1-form A on
the Sp(64) principal bundle: the vertical component is A(V) for V a vertical vector field
on Y^{14}. After pullback to the section, A(V)|_{s(X^4)} is a section of adj(P_s) with
no spacetime index. Verify that this construction is gauge-covariant and well-defined.

**OQ3 (Mexican hat potential coefficient).** Compute the quartic coefficient lambda_1 and
mass parameter mu^2 of the GU Higgs potential from the GU Lagrangian, in particular from
the ||theta||^4 and ||theta||^2 terms after restricting to the (1, 2, +1/2) block. Compare
with the CC spectral action coefficients (which are given by moments f_0, f_2, f_4 of the
spectral function f in the heat-kernel expansion).

**OQ4 (Pati-Salam breaking mechanism).** Identify the GU mechanism for SU(4) x SU(2)_R ->
SU(3) x U(1)_Y breaking. Does a second component of theta (e.g., theta in the (1, 1, 0)
or (6, 1, 1) representation of G_PS) provide this? Or is it gated on a separate geometric
structure (a second section, a boundary condition, or a Higgs at a higher KK mass)?

**OQ5 (Uniqueness vs CC).** In CC, the Higgs is essentially unique given the algebra A.
In GU, is phi_H unique given the Sp(64) structure and the Pati-Salam embedding, or are
there multiple (1, 2, +1/2) blocks in adj(Sp(64))|_{G_SM} that give different candidate
Higgs fields? The multiplicity from OQ1 determines this.

---

## 5. Summary

| Item | Status | Notes |
|---|---|---|
| Candidate Higgs field phi_H defined | CONDITIONALLY_RESOLVED | fiber-component of theta in (1,2,2) PS block |
| Higgs quantum numbers (1,2,+1/2) | CONDITIONALLY_RESOLVED (reconstruction) | from PS tensor product, gates on CAS |
| GATE-H4 (adj(Sp(64)) contains (1,2,+1/2)) | CONDITIONALLY_RESOLVED (reconstruction) | highest priority CAS computation |
| Higgs is 0-form (Lorentz scalar) | CONDITIONALLY_RESOLVED (reconstruction) | from fiber-component construction |
| J-structure analog of CC real structure | exploration | requires explicit J-action on Higgs block |
| Mexican hat potential sign | exploration | requires fermion-loop or spectral-action computation |
| Yukawa couplings | exploration | from Clifford matrix element c(phi_H) |
| Pati-Salam breaking mechanism | OPEN | gates on a second GU field or boundary condition |
| Comparison with CC structural mechanism | CONDITIONALLY_RESOLVED | substitution table in §3.5 |

**Grade: exploration/reconstruction.** The specification is correct in structure and
the key representation-theoretic gate is identified. The main computation not yet performed
is the CAS branching of adj(Sp(64))|_{G_SM} (OQ1 / GATE-H4).

---

## 6. What Would Change the Verdict

- **To RESOLVED**: (1) CAS confirms (1,2,+1/2) in adj(Sp(64))|_{G_SM} with multiplicity 1.
  (2) Fiber-component theta^{vert} construction verified as a gauge-covariant 0-form.
  (3) Mexican hat potential coefficient from GU Lagrangian has correct sign (mu^2 < 0 from
  fermion loop or Willmore Hessian).

- **To GENUINE_OBSTRUCTION**: (1) CAS shows (1,2,+1/2) absent from adj(Sp(64))|_{G_SM}.
  (2) Fiber-component theta^{vert} is not gauge-covariant or vanishes by J-invariance.
  (3) Yukawa coupling c(phi_H) block vanishes identically.

- **Pati-Salam breaking remains OPEN regardless** of the Higgs verdict, because it requires
  a separate field content analysis (OQ4) not addressed in this computation.

---

## 7. References

- Connes, A. and Chamseddine, A.H., "Universal Formula for Noncommutative Geometry Actions:
  Unification of Gravity and the Standard Model," Phys. Rev. Lett. 77 (1996) 4868.
- Connes, A. and Chamseddine, A.H., "The Spectral Action Principle," Commun. Math. Phys. 186 (1997) 731.
- Chamseddine, A.H., Connes, A., and Marcolli, M., "Gravity and the Standard Model with
  Neutrino Mixing," Adv. Theor. Math. Phys. 11 (2007) 991-1089.
- Pati, J.C. and Salam, A., "Lepton Number as the Fourth Color," Phys. Rev. D 10 (1974) 275.
- explorations/shiab-operator/pc1-spin77-spinor-decomp-2026-06-23.md (spinor S as coefficient bundle)
- explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md (section pullback)
- explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md (s*(theta) = II_s)
- explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md (explicit Christoffels, II_s^H)
- explorations/geometry-curvature-emergence/ic1-soldering-map-ns-adps-2026-06-23.md (j_s: N_s -> ad(P_s))
- explorations/geometry-curvature-emergence/hc1-sl2c-bianchi-spinor-2026-06-23.md (theta irreducible decomposition)
- explorations/geometry-curvature-emergence/pc4-torsion-lambda-derivation-2026-06-23.md (||theta||^2 as Lambda replacement)
- explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md (S(6,4) SM content)
- explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md (Sp(64) inner product on j_s image)

---

*Filed: 2026-06-23. First bounded specification of the GU Higgs emergence mechanism.
Grade: exploration/reconstruction. Key result: Higgs candidate is the fiber-component of
theta in the (1,2,2) Pati-Salam block of adj(Sp(64)), analogous to CC inner fluctuation
but geometric in origin. GATE-H4 (CAS branching confirmation) is the highest-priority
next computation.*
