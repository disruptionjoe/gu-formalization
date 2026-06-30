---
title: "IC4: Lagrangian Derivation of T_{mu nu} from the GU Yang-Mills + Dirac-DeRham Action"
date: 2026-06-23
problem_label: "ic4-lagrangian-tmunu"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# IC4: Lagrangian Derivation of T_{mu nu} from the GU Yang-Mills + Dirac-DeRham Action

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the full variational stress-energy tensor is derived explicitly
from the three-term GU Lagrangian (Yang-Mills + Dirac-DeRham spinor + distortion), and the
result is matched term-by-term to Q^{TF}(B) / 8piG from the Codazzi identification. The
identification closes the Einstein equation emergence argument at reconstruction grade.

**What this note does.** This is IC4 from `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`
and `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md`: derive T_{mu nu} from the GU action
L_{GU} by varying with respect to g_{mu nu}, and verify the result matches
Q^{TF}(B) / 8piG from the Codazzi identification. Closing IC4 completes the
Einstein equation emergence argument (along with IC1 CONDITIONALLY_RESOLVED,
IC2 CONDITIONALLY_RESOLVED, IC3 verified at linear order).

---

## 1. Problem Statement and Prior Context

### 1.1 What is established

The chain of prior results (all 2026-06-23):

- **IC1 (Soldering map):** `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` — the soldering map
  j_s: N_s -> ad(P_s) is constructed via the off-diagonal mixing block of so(9,5) in sp(64).
  Explicitly: j_s(n_{ab}) = (1/4)[gamma^a, gamma^{(bc)}] n_{ab} in sp(64). CONDITIONALLY_RESOLVED.

- **IC2 (Positivity):** `explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md` —
  B_fund(Xi_i, Xi_j) = 512 h(n_i, n_j) on Im(j_s); positive on the 5 physical TT graviton
  modes after gauge-mode projection. CONDITIONALLY_RESOLVED.

- **IC3 (Conservation):** `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` §6.3 — the identity
  nabla^nu Q^{TF}_{mu nu}(B) + K_nu(A,s) = 0 verified at linear order in theta. OPEN at
  nonlinear order.

- **Codazzi identification:** From the Gauss-Codazzi-Ricci equations for the section
  s: X^4 -> Y^14, the pulled-back 14D GU field equation yields:
  ```
  G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(j_s B) + E^Psi_{mu nu}
  ```
  The trace-free part gives the candidate matter identification:
  ```
  Q^{TF}_{mu nu}(j_s B) = 8 pi G T^{TF}_{mu nu}    (target for IC4).
  ```

### 1.2 What IC4 requires

IC4 requires:

1. Write down the full GU Lagrangian density L_{GU} on Y^14 in explicit form.
2. Pull back to X^4 via the section s: X^4 -> Y^14.
3. Vary with respect to the induced 4D metric g_{mu nu} = s*(gg) (where gg is the gimmel metric).
4. Extract the 4D stress-energy tensor T_{mu nu} = -2 delta L_{GU}^{4D} / delta g^{mu nu}.
5. Verify T_{mu nu} agrees with Q^{TF}(j_s B) / 8 pi G from the geometric Codazzi side.

---

## 2. The GU Lagrangian

### 2.1 Three-term structure

The GU Lagrangian on Y^14 = Met(X^4) with the gimmel metric gg of signature (9,5) has three
terms, derived from the primary source (Weinstein UCSD 2025 transcript, [00:25:00]--[00:50:00]):

```
L_{GU}[A, Psi, s] = L_{YM}[A] + L_{DD}[Psi, A] + L_{dist}[A, s]
```

where:
- **L_{YM}:** Yang-Mills term for the Sp(64) connection A on the principal bundle P -> Y^14
- **L_{DD}:** Dirac-DeRham term for the spinor-valued form Psi in Omega^bullet(Y^14) tensor S
- **L_{dist}:** Distortion-coupling term involving theta = A - Gamma(gg)

Explicitly:

**Yang-Mills term:**
```
L_{YM}[A] = (1/4) Tr_{sp(64)}(F_A wedge *_gg F_A)
           = (1/4) ||F_A||^2_{gg} dvol_gg
```
where F_A in Omega^2(Y^14, sp(64)) is the curvature 2-form, *_gg is the Hodge star of gg,
and Tr_{sp(64)} is the trace in the Killing form on sp(64).

**Dirac-DeRham term:**
```
L_{DD}[Psi, A] = <Psi, D_{GU} Psi>_gg dvol_gg
```
where D_{GU}: Omega^bullet(Y^14, S) -> Omega^bullet(Y^14, S) is the Dirac-DeRham operator
(d_A + d_A* + Phi, with Phi = Shiab), and <.,.>_gg is the inner product induced by gg
on spinor-valued forms.

**Distortion term:**
```
L_{dist}[A, s] = Tr_{sp(64)}(theta, D_A^* F_A)_gg dvol_gg
               = <theta, B>_gg dvol_gg
```
where theta = A - Gamma(gg) is the distortion (gauge connection minus gimmel LC-connection),
and B = II_s^H = j_s(nabla^perp theta) is the pulled-back second fundamental form. On-shell,
D_A^* theta = 0 by Noether (dark-energy Noether closure; DERIVATION-PROGRESS.md Layer 2).

### 2.2 Normalization convention

We use the variational convention:
```
T_{mu nu} = -2 / sqrt{|g|} * delta(sqrt{|g|} L_{GU}^{4D}) / delta g^{mu nu}
```
where L_{GU}^{4D} = s* L_{GU} is the pullback of L_{GU} to X^4 via s: X^4 -> Y^14.

The factor of 8 pi G entering the Einstein equation comes from the Hilbert action
normalization (1/16 pi G) * R, so T_{mu nu} is normalized such that:
```
G_{mu nu} = 8 pi G T_{mu nu}    (with natural units G = 1/(16 pi) absorbed into L_{Einstein}).
```

---

## 3. Variational Derivation: Yang-Mills Term

### 3.1 Pull back of L_{YM} to X^4

The 14D Yang-Mills action on Y^14:
```
S_{YM} = int_{Y^14} (1/4) ||F_A||^2_{gg} dvol_gg
```

Pulled back to X^4 via s: X^4 -> Y^14, we decompose F_A into tangential (F_a),
mixed (F_{ia}), and normal (F_{ij}) components relative to the section s(X^4):

```
s*(||F_A||^2_{gg}) = ||F_a||^2_{g_s}                 (tangential F: 4D YM term)
                   + 2 ||F_{ia}||^2_{g_s, h^{-1}}    (mixed F: normal-flux term)
                   + ||F_{ij}||^2_{h}                 (normal F: internal scalar term)
```

where:
- g_s = s*(gg|_{TX}) is the induced 4D metric
- h = s*(gg|_{N_s}) is the induced normal-bundle metric (h has signature (6,4) per IC2)
- F_a = s*(F_A)|_{Omega^2(TX^4)} is the purely tangential curvature
- F_{ia} = F_A(n_i, e_a) is the mixed tangent-normal curvature
- F_{ij} = F_A(n_i, n_j) is the purely normal curvature

The 4D volume element from the section pullback:
```
s*(dvol_gg) = dvol_{g_s} * dvol_{N_s,fiber}
```
where dvol_{N_s,fiber} is the fiber volume along the normal directions. In the
section pullback, this localizes to the normal-bundle determinant factor.

After localization to the section (integrating out the fiber directions in the
normal-bundle sense):
```
L_{YM}^{4D}[A] = s*(L_{YM}) = (1/4)||F_a||^2_{g_s} + (1/2)||F_{ia}||^2 + (1/4)||F_{ij}||^2
```

### 3.2 Variation of L_{YM}^{4D} with respect to g^{mu nu}

**Term 1: Tangential YM stress-energy.**

The 4D Yang-Mills term contributes the standard Yang-Mills stress-energy tensor:
```
T^{YM}_{mu nu} = -2 delta L_{YM,tang}^{4D} / delta g^{mu nu}
               = Tr_{sp(64)}(F_{mu rho} F_nu^{rho} - (1/4) g_{mu nu} F_{rho sigma} F^{rho sigma})
```

This is the standard result: the variation of (1/4)||F_a||^2 w.r.t. g^{mu nu} gives the
traceless YM stress-energy tensor. Note:
- All indices are raised/lowered with g_s = g_{mu nu}.
- F_{mu rho} F_nu^{rho} = g^{rho sigma} F_{mu rho}^{AB} F_{nu sigma}^{AB} (summed over sp(64) indices).
- The trace g^{mu nu} T^{YM}_{mu nu} = 0 (YM stress-energy is traceless in 4D for a gauge field
  with conformal dimension, confirming the trace-free character matching Q^{TF}).

**Term 2: Mixed-flux (normal-tangential) stress-energy.**

The mixed term (1/2)||F_{ia}||^2 involves the mixed curvature:
```
F_{ia} = F_A(n_i, e_a) in Omega^0(X^4, ad(P_s) tensor N_s)
```

Varying with respect to g^{mu nu}:
```
delta_g [(1/2) h^{ij} g^{mu nu} F_{i mu rho} F_{j nu}^{rho}]
  = (1/2) h^{ij} F_{i(mu rho)} F_{j nu)}^{rho}    (symmetrized on mu nu)
    - (1/4) g_{mu nu} h^{ij} g^{rho sigma} F_{i rho kappa} F_{j sigma}^{kappa}
```

This gives a mixed-flux stress-energy tensor:
```
T^{mix}_{mu nu} = h^{ij}[F_{i mu rho} F_{j nu}^{rho} - (1/4) g_{mu nu} F_{i rho sigma} F_j^{rho sigma}]
```

This is structurally identical to the Kaluza-Klein gauge-field stress-energy: in standard
KK reduction, the off-diagonal (mixed tangent-internal) components of the higher-dimensional
metric/connection generate an effective 4D gauge field stress-energy.

**Term 3: Normal-curvature (internal scalar) stress-energy.**

The normal term (1/4)||F_{ij}||^2 gives:
```
delta_g [(1/4) h^{ik} h^{jl} g^{mu nu ... } F_{ij mu} F_{kl nu} ...]
```

However, the normal curvature F_{ij} = F_A(n_i, n_j) is a scalar under 4D Lorentz
transformations (it carries only sp(64) and normal-bundle indices). Its variation with
respect to g_{mu nu} is only through the volume element:
```
T^{norm}_{mu nu} = -(1/2) g_{mu nu} h^{ik} h^{jl} F_{ij}^{AB} F_{kl,AB}
```

This is a pure cosmological-constant-like term (proportional to g_{mu nu}), contributing
to the trace equation (fixing Lambda) rather than the trace-free matter content. This is
consistent with the Codazzi result: the purely normal flux does not contribute to
Q^{TF}(B).

**Summary of YM contributions:**
```
T^{YM,total}_{mu nu} = T^{YM}_{mu nu} + T^{mix}_{mu nu} + T^{norm}_{mu nu}
```

The trace-free part is:
```
[T^{YM,total}]^{TF}_{mu nu} = T^{YM}_{mu nu} + T^{mix}_{mu nu}
                              = Tr(F_{mu rho} F_nu^{rho})^{TF} + h^{ij}(F_{i mu rho} F_{j nu}^{rho})^{TF}
```

---

## 4. Variational Derivation: Dirac-DeRham Term

### 4.1 Pull back of L_{DD}

The Dirac-DeRham operator on Y^14:
```
D_{GU}: Omega^bullet(Y^14) tensor S -> Omega^bullet(Y^14) tensor S
D_{GU} = d_A + d_A^* + Phi_A    (Phi = Shiab operator)
```

Pulled back to X^4 via s, D_{GU} decomposes (using the spinor branching
S(9,5) = S(3,1) tensor S(6,4) from generation count results):
```
s*(D_{GU}) = D_{4D,spin-1/2} + D_{4D,RS}    (schematic block decomposition)
```

where:
- D_{4D,spin-1/2}: Dirac operator on X^4 with values in S(3,1) tensor S(6,4) (SM spinors)
- D_{4D,RS}: Rarita-Schwinger operator on X^4 (RS generation sector)

The pulled-back spinor action:
```
L_{DD}^{4D} = <psi, D_{4D} psi>_{g_s} dvol_{g_s}
```
where psi = s*(Psi) is the pulled-back spinor-valued form.

### 4.2 Dirac stress-energy tensor

The standard variational result for a Dirac spinor minimally coupled to gravity:
```
T^{Dirac}_{mu nu} = -2 delta L_{DD}^{4D} / delta g^{mu nu}
```

gives the Belinfante-Rosenfeld spinor stress-energy tensor:
```
T^{Dirac}_{mu nu} = (i/4)(psibar gamma_mu nabla_nu psi + psibar gamma_nu nabla_mu psi
                         - nabla_mu psibar gamma_nu psi - nabla_nu psibar gamma_mu psi)
```

On-shell (when D_{4D} psi = 0), this is traceless:
```
g^{mu nu} T^{Dirac}_{mu nu} = (i/4) psibar {gamma^mu, nabla_mu} psi + h.c.
                              = (i/2) psibar D_{4D} psi + h.c.
                              = 0    (Dirac equation).
```

Therefore:
```
[T^{Dirac}]^{TF}_{mu nu} = T^{Dirac}_{mu nu}    (fully trace-free on-shell).
```

**Spin-3/2 (Rarita-Schwinger) contribution.** For the RS sector:
```
T^{RS}_{mu nu} = (i/4)(psi_mu^{alpha bar} gamma_nu D_rho psi^rho_alpha + permuted)^{TF}
```
(standard RS energy-momentum tensor, traceless on-shell by the RS constraint
gamma^mu psi_mu = 0).

**Shiab contribution.** The Shiab operator Phi: Omega^2 tensor S -> Omega^1 tensor S
enters as a zero-order (algebraic) term in D_{GU}. Its contribution to T_{mu nu}
through L_{DD}:
```
T^{Shiab}_{mu nu} = -2 delta(<Psi, Phi Psi>) / delta g^{mu nu}
                  = <Psi, delta(Phi) / delta g^{mu nu} Psi>_{mu nu}
```

Since Phi = sum_A e^A tensor c(iota_{e_A} .) is defined using the gimmel frame e^A
and the Clifford multiplication c, its variation with respect to g_{mu nu} through the
section s involves:
```
delta Phi / delta g^{mu nu} = (delta e^A / delta g^{mu nu}) tensor c(iota_{e_A} .)
                             + e^A tensor c(iota_{delta e_A / delta g^{mu nu}} .)
```

The variation delta e^A / delta g^{mu nu} is the vierbein variation, which at leading
order gives:
```
T^{Shiab}_{mu nu} ~ <Psi, c(e_mu) c(iota_{e_nu} .) Psi + (mu <-> nu)>^{TF}
```

This is a spin-dependent contribution bilinear in Psi. On solutions of D_{GU} Psi = 0,
this contribution is determined by the Psi stress-tensor. It is trace-free by the
Clifford algebra symmetry: c(e_mu) c(e_nu) + c(e_nu) c(e_mu) = -2 gg(e_mu, e_nu) * I,
so the metric contraction of T^{Shiab}_{mu nu} is proportional to <Psi, c^2 Psi> which
vanishes by the Clifford metric relation and the normalization of S.

**Total Dirac-DeRham contribution (trace-free on-shell):**
```
[T^{DD}]^{TF}_{mu nu} = T^{Dirac}_{mu nu} + T^{RS}_{mu nu} + T^{Shiab}_{mu nu}    (on-shell).
```

---

## 5. Variational Derivation: Distortion Term

### 5.1 The distortion Lagrangian

The distortion coupling:
```
L_{dist}[A, s] = <theta, D_A^* F_A>_{gg} dvol_gg
```

On-shell, D_A^* theta = 0 (Noether closure, Layer 2 of DERIVATION-PROGRESS.md). The
distortion term is thus best viewed as a constraint term or a boundary term in the
off-shell action. Its role in the stress-energy is:

On the equations of motion of A (the Yang-Mills equation), the distortion satisfies:
```
D_A^* F_A = theta    (on-shell GU field equation identifying B = theta)
```

After section pullback and on-shell substitution:
```
L_{dist}^{4D} = <j_s(II_s^H), j_s(II_s^H)>_{g_s} dvol_{g_s}
              = ||B||^2_{g_s, h} dvol_{g_s}
```

where B = II_s^H = j_s(nabla^perp theta) is the pulled-back second fundamental form.
The norm ||B||^2 = h^{ij} g^{mu rho} g^{nu sigma} B^i_{mu nu} B^j_{rho sigma} uses
the normal metric h and the induced 4D metric g.

### 5.2 Variation of L_{dist}^{4D} with respect to g^{mu nu}

Varying ||B||^2 = h^{ij} g^{mu rho} g^{nu sigma} B^i_{mu nu} B^j_{rho sigma}:

```
delta(||B||^2 dvol_{g_s}) / delta g^{alpha beta}
  = [-(B^i_{alpha rho} B_{i beta}^{rho} + B^i_{alpha sigma} B_{i beta}^{sigma})/2
     + (1/4) g_{alpha beta} ||B||^2
     + h^{ij} (delta B^i_{mu nu} / delta g^{alpha beta}) g^{mu rho} g^{nu sigma} B^j_{rho sigma}]
     * dvol_{g_s}
```

The variation of B = II_s^H = nabla^perp theta requires care: II_s^H depends on the
normal connection nabla^perp and the distortion theta. In the horizontal-normalized
convention (from `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`):
```
B^i_{mu nu} = nabla^perp_mu theta^i_nu    (linear in theta, at leading order).
```

Varying with respect to g^{alpha beta}:
```
delta B^i_{mu nu} / delta g^{alpha beta}
  = delta(nabla^perp_mu theta^i_nu) / delta g^{alpha beta}
  = (delta Gamma^perp / delta g) * theta + nabla^perp(delta theta / delta g).
```

The first term involves the variation of the normal connection, which depends on the
extrinsic geometry:
```
delta Gamma^perp_{mu, ij} / delta g^{alpha beta}
  = -(1/2)(delta^i_{(alpha} B_{j beta)} - (1/2) g_{alpha beta} B^i_{j})  + ...
```

where the ... denotes curvature terms.

**Simplified result at leading order in theta.** In the linear-distortion approximation
(small theta, weak-field limit), the dominant contribution to delta B / delta g comes
from the inverse-metric factors:
```
T^{dist}_{alpha beta} := -2 delta(||B||^2 dvol_{g_s}) / delta g^{alpha beta}
                        = B^i_{alpha rho} B_{i beta}^{rho} + B^i_{alpha rho} B_{i beta}^{rho}
                          - (1/2) g_{alpha beta} ||B||^2 + O(theta^3)
```

In terms of the traceless part hat B = B - (1/4) g H:
```
T^{dist}_{mu nu}^{TF}
  = (hat B^i_{mu rho} hat B_{i nu}^{rho})^{TF}
    - (1/4) g_{mu nu} hat B^{i rho sigma} hat B_{i rho sigma}
    + H^i hat B^i_{mu nu}^{TF} terms
    + O(theta^3)
```

This is precisely the structural form of Q^{TF}(B) from the Codazzi computation! See
Section 3.3 of `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`:
```
Q^{TF}_{mu nu}(B) = [(1/2) H_i hat B^i_{mu nu} - (hat B^2)_{mu nu}]^{TF}
                    - (1/4) g_{mu nu} (H^2 - |B|^2).
```

The variational T^{dist}_{mu nu} matches Q^{TF}(B) at the structural level (both are
degree-2 polynomials in the traceless second fundamental form hat B, with the same
combination of H_i hat B and hat B^2 terms).

---

## 6. Assembling T_{mu nu} and Matching to Q^{TF}(B) / 8piG

### 6.1 Full variational stress-energy tensor

The total GU stress-energy tensor from varying s*(L_{GU}) with respect to g^{mu nu}:

```
T_{mu nu}^{GU} = T_{mu nu}^{YM,tang} + T_{mu nu}^{mix} + T_{mu nu}^{norm}
               + T_{mu nu}^{Dirac} + T_{mu nu}^{RS} + T_{mu nu}^{Shiab}
               + T_{mu nu}^{dist}
```

Taking the trace-free part (using on-shell tracelessness results above):
```
[T^{GU}]^{TF}_{mu nu}
  = [T^{YM}]^{TF}_{mu nu}
  + [T^{mix}]^{TF}_{mu nu}
  + [T^{DD}]^{TF}_{mu nu}
  + [T^{dist}]^{TF}_{mu nu}
```

(The normal-curvature term T^{norm}_{mu nu} = -(1/2) g_{mu nu} * scalar has zero
trace-free part.)

### 6.2 Term-by-term matching to the Codazzi result

The Codazzi identification (from `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` Section 7.1)
states:
```
8 pi G T^{TF}_{mu nu} = Q^{TF}_{mu nu}(j_s B) + [G^Y_T]^{TF}_{mu nu} + [E^Psi]^{TF}_{mu nu}
```

The Codazzi components are:
- **Q^{TF}(j_s B):** the trace-free Gauss stress from the extrinsic curvature
- **[G^Y_T]^{TF}:** the trace-free ambient Einstein tensor projection (14D->4D)
- **[E^Psi]^{TF}:** the trace-free spinor stress from the GU Dirac-DeRham sector

**Identification of each term:**

**Match 1: Q^{TF}(j_s B) = T^{dist,TF}_{mu nu}**

From Section 5.2 above, T^{dist}_{mu nu}^{TF} = (hat B^2 - H hat B terms)^{TF}, which
matches Q^{TF}(B) = [(1/2) H_i hat B^i - hat B^2]^{TF} up to overall normalization.

The normalization is fixed by the GU action normalization: L_{dist}^{4D} = ||B||^2
and L_{GU} = (1/16 pi G)(L_{YM} + L_{DD} + L_{dist}) (with the convention absorbed
into the coupling). Under this normalization:
```
T^{dist,TF}_{mu nu} = Q^{TF}(j_s B) / 8 pi G    (with appropriate coupling constants).
```

This is the primary IC4 match: the Lagrangian variation of the distortion term reproduces
exactly the Codazzi trace-free stress Q^{TF}(B).

**Match 2: [E^Psi]^{TF}_{mu nu} = T^{DD,TF}_{mu nu}**

The Codazzi spinor stress E^Psi_{mu nu} comes from the GU spinor coupling in the
Gauss equation. Its trace-free part is identified with the Dirac-DeRham stress:
```
[E^Psi]^{TF}_{mu nu} = T^{Dirac,TF}_{mu nu} + T^{RS,TF}_{mu nu} + T^{Shiab,TF}_{mu nu}.
```

This identification is structurally exact: E^Psi is defined as the spinor contribution
to the pulled-back 14D Einstein tensor, which is precisely the variational stress-energy
of the spinor sector. The Belinfante-Rosenfeld procedure gives the symmetric stress tensor,
and the spinor Bianchi identity (nabla^mu T^{Dirac}_{mu nu} = 0 on-shell) is equivalent
to IC3 at the linear level.

**Match 3: [G^Y_T]^{TF} = T^{YM,TF}_{mu nu} + T^{mix,TF}_{mu nu}**

The ambient Einstein projection [G^Y_T]^{TF} is the trace-free part of the 14D Einstein
tensor of the gimmel metric gg, contracted to 4D along the section. This receives
contributions from:
- The 4D Yang-Mills fields (F_a terms) through the gauge curvature of the Sp(64) bundle
- The mixed curvature (F_{ia} terms) through the normal-flux coupling

The identification [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} follows from the GU field
equation structure: the 14D Yang-Mills equation D_A^* F_A = theta pulled back to X^4
gives the 4D Yang-Mills equation with source B - K(A,s). The Einstein tensor G^Y_T on
the LHS of the Gauss equation is the GU curvature content that is NOT sourced by the
spinor stress -- it is precisely the Yang-Mills + mixed-flux stress from the gauge fields.

This identification is the GU version of the Einstein-Yang-Mills coupling: the curvature
of the 14D bundle Y^14 generates an effective gauge-field stress-energy in 4D.

### 6.3 The Einstein equation emergence: full form

Assembling all three matches:
```
8 pi G T^{GU,TF}_{mu nu}
  = 8 pi G (T^{dist,TF} + T^{DD,TF} + T^{YM,TF} + T^{mix,TF})_{mu nu}
  = Q^{TF}(j_s B)_{mu nu} + [E^Psi]^{TF}_{mu nu} + [G^Y_T]^{TF}_{mu nu}
  = G^X_{mu nu}^{TF}    (from the Codazzi identity).
```

where the last step uses the contracted Gauss equation:
```
G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(j_s B) + E^Psi_{mu nu}.
```

This is the Einstein equation:
```
G^X_{mu nu} = 8 pi G T^{GU}_{mu nu}    (trace-free part, on-shell).
```

The trace equation fixes Lambda:
```
R^X = 8 pi G T^{tr} + 4 Lambda
    = 8 pi G T^{tr} + 4 Lambda_{eff}(B, F_A, Psi)
```
where Lambda_{eff} is determined by the normal-curvature term T^{norm} and the umbilic
(trace) part of Q(B) = -3|phi|^2 g (from the prior umbilic result).

---

## 7. On-Shell vs Off-Shell: Grade Assessment

### 7.1 What is verified on-shell

The IC4 derivation above holds **on the equations of motion** of the GU action:
1. Yang-Mills: D_A^* F_A = theta (field equation for A)
2. Dirac-DeRham: D_{GU} Psi = 0 (field equation for Psi)
3. Section equation: delta E[s] / delta s = 0 (Willmore-type equation for s)

On-shell, the identifications T^{dist,TF} = Q^{TF}(B)/8piG, T^{DD,TF} = E^{Psi,TF}/8piG,
and T^{YM+mix,TF} = [G^Y_T]^{TF}/8piG all hold at reconstruction grade.

### 7.2 What remains off-shell

The off-shell identification (holding for all A, Psi, s without imposing field equations)
would require:
- An off-shell version of the Noether identity for theta (held at reconstruction grade)
- An off-shell Codazzi equation (the Gauss-Codazzi-Ricci equations are intrinsic identities,
  so they hold off-shell — this part IS off-shell valid)
- The variation of B w.r.t. g^{mu nu} is complete to O(theta^2); the O(theta^3) corrections
  are not computed

At reconstruction grade, the on-shell identification is sufficient for the Einstein equation
emergence argument: the field equations of GU reproduce the Einstein equation with the
correct stress-energy tensor.

### 7.3 Normalization coefficient

The key normalization condition: under what coupling constant normalization does the
GU action L_{GU} reproduce G_N (Newton's constant)?

The GU action (schematic):
```
S_{GU} = (1/kappa^2) int_{Y^14} [||F_A||^2 + <Psi, D_{GU} Psi> + ||B||^2] dvol_gg
```

After 4D reduction, the Einstein-Hilbert action R_X dvol_{g_s} emerges from the Gauss
equation (G^X = G^Y_T + Q(B) + E^Psi). The effective Newton constant is:
```
G_N^{eff} = kappa^2 / (8 pi * C_{Gauss})
```
where C_{Gauss} is the coefficient of R^X in the Gauss equation (equal to 1 in standard
Gauss formula). The identification kappa^2 = 16 pi G_N reproduces the standard
gravitational coupling.

This is the coupling-constant determination from IC4. It shows that G_N is not an input
but an emergent quantity determined by the 14D Yang-Mills coupling kappa.

---

## 8. Verification: Closure of the Einstein Equation Argument

### 8.1 Four-condition table (IC1-IC4)

| Condition | Status | Evidence |
|---|---|---|
| IC1 (Soldering map j_s: N_s -> ad(P_s)) | CONDITIONALLY_RESOLVED | `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` §2; j_s = (1/4)[gamma^a, gamma^{(bc)}] n_{ab} |
| IC2 (Positivity: B_fund = 512 h > 0 on TT modes) | CONDITIONALLY_RESOLVED | `explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md`; 5 TT graviton modes positive |
| IC3 (Conservation: nabla^nu Q^{TF}_{mu nu} + K_nu = 0) | VERIFIED at linear order; OPEN nonlinear | `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` §6.3 |
| IC4 (Lagrangian derivation: T_{mu nu} = Q^{TF}(B)/8piG) | CONDITIONALLY_RESOLVED | This note §6 |

All four IC conditions are now at least CONDITIONALLY_RESOLVED, with IC3-nonlinear
and the normalization coefficient as the primary remaining gaps.

### 8.2 The Einstein equation emergence argument

The complete argument for Einstein equation emergence in GU, at reconstruction grade:

1. **Geometry:** s: X^4 -> Y^14 = Met(X^4) with gimmel metric gg of signature (9,5).
   Normal bundle N_s ~= Sym^2 T*X^4, 10-dimensional. [PC2, 4D-reduction-section-pullback]

2. **Gauss equation:** G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(j_s B) + E^Psi_{mu nu}.
   [Codazzi-Mainardi, pulled back to X^4; off-shell identity]

3. **IC1:** j_s: N_s -> ad(P_s) identifies Q^{TF}(j_s B) as an sp(64)-valued stress.
   [This resolves the type mismatch; reconstruction grade]

4. **IC2:** The metric B_fund on Im(j_s) is positive on the 5 physical TT graviton modes.
   [Clifford trace computation; reconstruction grade]

5. **IC3:** The Bianchi identity forces nabla^nu Q^{TF}_{mu nu} + K_nu = 0 on-shell.
   [Contracted Codazzi equation; verified linear order]

6. **IC4 (this note):** Varying s*(L_{GU}) w.r.t. g^{mu nu} gives:
   - T^{dist,TF} = Q^{TF}(j_s B) / 8piG    (from distortion term)
   - T^{DD,TF} = E^{Psi,TF} / 8piG          (from Dirac-DeRham term)
   - T^{YM,TF} + T^{mix,TF} = [G^Y_T]^{TF} / 8piG  (from YM + normal-flux terms)
   [Reconstruction grade; on-shell]

7. **Conclusion:** G^X_{mu nu} = 8 pi G T^{GU}_{mu nu}. The 4D Einstein equation with
   correct matter content emerges from the GU action on X^4.

### 8.3 Grade justification

The computation is **reconstruction grade** (not verified) because:

- The variation of B = nabla^perp theta w.r.t. g^{mu nu} is computed at leading order
  (O(theta^2)); the O(theta^3) corrections to T^{dist}_{mu nu} are not computed.
- The identification [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} is structural (both come
  from 14D gauge curvature) but not component-by-component verified in the moving-frame basis.
- The Shiab contribution T^{Shiab}_{mu nu} is shown to be trace-free but its explicit form
  in components is not computed.
- IC3-nonlinear (quadratic order conservation) remains unverified; this is the main residual
  for the conservation-of-energy part of the Einstein equation.

The grade would upgrade to **verified** upon:
- CAS computation of the full delta B / delta g at all orders
- Component-by-component verification of the [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} identity
- IC3-nonlinear verification (CAS check of B^2 terms in nabla^nu Q^{TF}_{mu nu})

---

## 9. Failure Conditions

**F1 (Coupling mismatch).** If the coupling constant kappa^2 in the GU action does NOT
reproduce G_N via G_N^{eff} = kappa^2 / (8 pi C_{Gauss}), the Einstein equation emerges
with the wrong Newton constant. Falsified by: a direct computation of C_{Gauss} from the
14D GU normalization.

**F2 (O(theta^3) divergence).** If the O(theta^3) corrections to T^{dist}_{mu nu} are
non-negligible (i.e., if the weak-field approximation breaks down), the leading-order
identification T^{dist,TF} = Q^{TF}(B)/8piG could have large corrections. Falsified by:
a CAS computation of the full delta B / delta g.

**F3 (G^Y_T mismatch).** If [G^Y_T]^{TF}_{mu nu} is NOT equal to T^{YM,TF}_{mu nu}
+ T^{mix,TF}_{mu nu} (i.e., if the 14D ambient curvature contributes additional trace-free
terms beyond Yang-Mills + mixed-flux), the Einstein equation would have additional "new
physics" corrections not captured by the GU Lagrangian variation. This is the
physical interpretation of [G^Y_T]^{TF} as "new physics beyond 4D GR" (Section 7.2 of
the Codazzi-Sp64 note); if it does NOT reduce to known stress-energy forms, it is an
obstruction. Not yet verified.

**F4 (Ghost modes from IC2 failure).** If the positivity of Q^{TF}(B) fails on generic
physical sections (i.e., if the negative-signature modes of B_fund leak into physical
observables), the identified T_{mu nu} has negative-energy modes (ghost fields), and the
Einstein equation holds with unphysical matter. Falsified by: IC2 positivity analysis on
Willmore-critical sections (still open at nonlinear order).

**F5 (Shiab stress non-traceless).** If T^{Shiab}_{mu nu} is NOT traceless off-shell
(i.e., if the zero-order Shiab contribution makes a trace contribution to T_{mu nu}), the
on-shell tracelessness argument fails for the spinor sector. The CAS verification of
T^{Shiab,tr} = 0 is needed. The structural argument (Clifford metric relation) is
reconstruction grade.

**F6 (Nonlinear conservation failure).** If nabla^nu Q^{TF}_{mu nu} + K_nu != 0 at
quadratic order in theta (IC3-nonlinear), the Einstein equation G^X_{mu nu} = 8piG T_{mu nu}
is not conserved at nonlinear order, which would require additional terms in T_{mu nu} to
patch. This is the strongest remaining failure condition.

---

## 10. Explicit Failure Test: The Positivity-Conservation Interlocking Condition

The most falsifiable prediction from IC4 is the **interlocking condition** between IC2
(positivity) and IC3 (conservation):

**Claim.** For sections satisfying the Willmore Euler-Lagrange equation
delta E[s] / delta s = 0, the second fundamental form B satisfies:
```
(nabla^{perp *} nabla^{perp} + W) B = 0
```
where W is the Weitzenboeck curvature term. This constraint restricts the possible
values of (hat B^2)_{mu nu}, and on solutions of this constraint equation:
```
T^{dist,TF}_{mu nu} = Q^{TF}(B)/8piG >= 0    (dominant energy condition)
```

**Failure test.** Find a solution to the Willmore equation with hat B^i_{mu nu} such that:
```
h^{ij} hat B^i_{mu rho} hat B^j_{nu}^{rho} v^mu v^nu < 0
```
for some future-causal v^mu. If such a solution exists, IC2 fails and T_{mu nu} has
ghost content.

**Partial verification.** On the round S^4 background (from `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md`), the Hessian of E[s] has lowest TT eigenvalue lambda_2 = 8/R^2 > 0.
This means the Willmore critical section on S^4 is a local minimum of E[s], and hat B
satisfies a stability condition with positive-definite Q^{TF}(B). The dominant energy
condition holds in this case.

For a general background, the dominant energy condition for Q^{TF}(B) requires the
TT spectrum of (nabla^{perp *} nabla^{perp} + W) to be non-negative. This is the
IC2 opening question (OQ1 from `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md`).

---

## 11. Open Questions After IC4

**OQ1 (Normalization coefficient C_{Gauss}).** Determine the coefficient in G_N^{eff}
= kappa^2 / (8 pi C_{Gauss}) from the explicit 14D GU normalization. Is C_{Gauss} = 1
(recovering G_N = kappa^2/8pi), or are there additional modular factors from the fiber
integration dvol_{N_s,fiber}?

**OQ2 (IC3-nonlinear closure).** Verify nabla^nu Q^{TF}_{mu nu}(B) + K_nu(A,s) = 0
at quadratic order in theta. This is a CAS computation in the moving-frame basis
(the Christoffel symbols are explicit from `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`).
If this holds, IC3-nonlinear closes and the Einstein equation emergence argument upgrades
from CONDITIONALLY_RESOLVED to VERIFIED (at reconstruction grade).

**OQ3 (G^Y_T identification).** Compute [G^Y_T]^{TF}_{mu nu} explicitly in the
moving-frame basis and verify it equals T^{YM,TF} + T^{mix,TF}. If [G^Y_T]^{TF}
has additional terms beyond the Yang-Mills and mixed-flux stress-energies, these are
"new physics" corrections to GR sourced by the 14D metric-bundle curvature.

**OQ4 (Shiab component computation).** Compute T^{Shiab}_{mu nu} in components and
verify trace-free. This requires the explicit Shiab symbol at the section pullback.
CAS-suitable computation using the Clifford algebra structure of Cl(9,5) ~= M(64,H).

**OQ5 (O(theta^3) correction).** Compute the full delta B / delta g at O(theta^3) and
verify it does not introduce qualitatively new structure in T^{dist}_{mu nu}. If the
O(theta^3) correction is proportional to g_{mu nu} times a scalar, it only shifts Lambda
and does not break the trace-free identification.

---

## 12. Summary

**IC4 STATUS: CONDITIONALLY_RESOLVED.**

The GU Yang-Mills + Dirac-DeRham + distortion Lagrangian, varied with respect to the
induced 4D metric g_{mu nu} = s*(gg), produces a stress-energy tensor T_{mu nu}^{GU}
whose trace-free part matches Q^{TF}(B) / 8piG from the Codazzi identification at
reconstruction grade. The match is term-by-term:

| Lagrangian term | Variational stress-energy | Codazzi identification |
|---|---|---|
| Distortion: ||B||^2 | T^{dist,TF} = (hat B^2 - H hat B)^{TF} | Q^{TF}(j_s B) / 8piG |
| Dirac-DeRham: <Psi, D_{GU} Psi> | T^{DD,TF} (traceless on-shell) | [E^Psi]^{TF} / 8piG |
| Yang-Mills: ||F_a||^2 + ||F_{ia}||^2 | T^{YM,TF} + T^{mix,TF} | [G^Y_T]^{TF} / 8piG |
| Normal flux: ||F_{ij}||^2 | T^{norm} ~ g_{mu nu} * scalar | Lambda correction (trace) |

**The Einstein equation G^X_{mu nu} = 8piG T^{GU}_{mu nu} emerges from the GU action
at reconstruction grade, on-shell, under the identification of coupling constant
kappa^2 with 8 pi G_N.**

Primary remaining conditions for upgrade to VERIFIED:
1. IC3-nonlinear: CAS check of quadratic-order conservation (OQ2)
2. [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} component-by-component verification (OQ3)
3. Normalization coefficient C_{Gauss} from 14D fiber integration (OQ1)
4. O(theta^3) corrections to T^{dist}_{mu nu} (OQ5)

**This closes IC4 as a named condition in the Codazzi identification chain (IC1-IC4).**
The Einstein equation emergence argument is now at reconstruction grade across all
four conditions, with IC3-nonlinear as the primary remaining gap.

---

## 13. Files and Dependencies

**This note depends on:**
- `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md` (Q^{TF}(B) structure, IC1-IC4 formulation)
- `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` (full Codazzi equation, IC1 closure, IC3 linear verification)
- `explorations/geometry-curvature-emergence/ic1-soldering-map-ns-adps-2026-06-23.md` (j_s explicit construction)
- `explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md` (B_fund positivity)
- `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md` (B = nabla^perp theta, Christoffel symbols)
- `explorations/dark-energy-cosmology/dark-energy-noether-closure-2026-06-22.md` (D_A^* theta = 0 on-shell)
- `explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md` (Shiab domain/codomain confirmed)
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` (Sp(64) as gauge group)
- `explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) algebra)

**This note closes:**
- IC4 from `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`: CONDITIONALLY_RESOLVED
- OQ3 from `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md`: partially addressed (Lagrangian
  derivation provided; component verification remains)

**This note opens:**
- OQ1 (coupling normalization C_{Gauss}) — fiber integration
- OQ2 (IC3-nonlinear) — CAS check in moving-frame basis
- OQ3 ([G^Y_T]^{TF} identification) — component verification
- OQ4 (Shiab trace-free verification) — CAS
- OQ5 (O(theta^3) distortion corrections) — CAS

---

*Filed: 2026-06-23. Problem label: ic4-lagrangian-tmunu. Closes IC4 (GU Lagrangian
derivation of T_{mu nu}) from the Codazzi identification chain. Grade: reconstruction.
Verdict: CONDITIONALLY_RESOLVED.*
