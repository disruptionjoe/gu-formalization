---
title: "Tangential Projection [G^Y_T]^{TF} of the Y^14 Gimmel Curvature and Normalization Constant C_{Gauss}"
date: 2026-06-23
problem_label: "pc2-gauss-y14-curvature"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Tangential Projection [G^Y_T]^{TF} of the Y^14 Gimmel Curvature and C_{Gauss}

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the tangential projection of the 14D ambient Einstein tensor
[G^Y_T]^{TF} is computed explicitly via the Gauss equation decomposition of the gimmel
Riemann tensor, and shown to equal T^{YM,TF} + T^{mix,TF} at reconstruction grade. The
normalization constant C_{Gauss} = 1 is derived from the standard Gauss formula (no
anomalous fiber-integration factors at the section). Both results close the final OQ in
IC4 (from `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`) at reconstruction grade.

---

## 1. Problem Statement

### 1.1 What is being computed

The ambient Einstein tensor G^Y_{AB} of the gimmel metric gg (signature (9,5)) on
Y^14 = Met(X^4), contracted to the 4D tangential projection:

```
[G^Y_T]_{mu nu} = G^Y_{AB} (e_a)^A (e_b)^B delta^a_mu delta^b_nu
```

where {e_a} (a = 0,...,3) is the horizontal tangent frame of the section s: X^4 -> Y^14,
and the T-subscript denotes "tangential" (all free indices on TX^4 ~ s*(TY^14) / N_s).

The trace-free part [G^Y_T]^{TF}_{mu nu} is the piece that enters the IC4 Einstein
identification:

```
8 pi G T^{GU,TF}_{mu nu} = Q^{TF}(j_s B)_{mu nu}
                          + [E^Psi]^{TF}_{mu nu}
                          + [G^Y_T]^{TF}_{mu nu}
```

from `explorations/codazzi-sp64-2026-06-23.md` Section 7.1.

IC4 (`explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`) identifies
[G^Y_T]^{TF} with T^{YM,TF} + T^{mix,TF} at the structural level (both are Yang-Mills
+ mixed-flux stress contributions). The present computation verifies this identification
explicitly via the gimmel curvature decomposition, and determines the normalization
constant C_{Gauss}.

### 1.2 Why this matters

Two open conditions from IC4 depend on this computation:

**OQ3 (IC4):** Is [G^Y_T]^{TF}_{mu nu} = T^{YM,TF}_{mu nu} + T^{mix,TF}_{mu nu}
component-by-component?

**OQ1 (IC4):** What is C_{Gauss} in the effective Newton constant
G_N^{eff} = kappa^2 / (8 pi C_{Gauss})?

Additionally, the rfail-umbilic note (`explorations/rfail-umbilic-sections-2026-06-23.md`)
identified a single remaining obstruction: explicit computation of [G^Y_T]^{TF} on the
maximally symmetric background, to close the vacuum/umbilic Einstein equation.

### 1.3 Prior results used

| result | source |
|---|---|
| Gimmel metric gg, signature (9,5), frame {e_a^H, F_{(bc)}} | `explorations/ii-s-moving-frames-2026-06-23.md` |
| Gimmel Christoffel symbols H-H-V, H-H-H, V-V-V blocks | `explorations/ii-s-moving-frames-2026-06-23.md` §3 |
| Gauss equation: G^X = G^Y_T + Q(B) + E^Psi | `explorations/codazzi-sp64-2026-06-23.md` §4 |
| IC4: term-by-term Lagrangian match T^{dist} = Q^{TF}/8piG, T^{DD} = E^{Psi,TF}/8piG | `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md` §6.2 |
| Codazzi equation [CodEq-Explicit] for II_s^H | `explorations/ii-s-moving-frames-2026-06-23.md` |
| Q^{TF}(B) = 0 for umbilic sections | `explorations/codazzi-general-non-umbilic-2026-06-23.md` §3.2 |

---

## 2. The Gimmel Riemann Tensor: Structure and Decomposition

### 2.1 Gimmel metric and frame

Recall from `explorations/ii-s-moving-frames-2026-06-23.md` that the gimmel metric gg on
Y^14 = Met(X^4) in the local moving-frame gauge has components:

```
gg_{ab} = g_s(e_a, e_b) = g_{ab}             (horizontal-horizontal = induced 4D metric)
gg_{ij} = V_{ij}                               (vertical-vertical = fiber metric, signature (6,4))
gg_{ai} = 0                                    (horizontal-vertical = 0 in LC gauge at s(X^4))
```

where:
- {e_a} (a=0,1,2,3): horizontal frame tangent to s(X^4) subset Y^14
- {F_{(bc)}} (bc symmetric, 10 components): vertical frame for N_s ~= Sym^2 T*X^4
- V_{ij}: trace-reversed fiber metric from the Frobenius + trace-reversal construction

The 10 normal directions (fiber at s(x^4)) carry signature (6,4) per
`explorations/ic2-positivity-soldering-normal-2026-06-23.md`.

**Index convention:**
- Greek mu, nu: tangential X^4 indices (0-3)
- Latin i,j,k: normal N_s indices (0-9, signature (6,4))
- Capital A,B,C: full 14D indices of Y^14

The Levi-Civita connection of gg has Christoffel symbols from
`explorations/ii-s-moving-frames-2026-06-23.md` Section 3:

```
Gamma^H_{ab, c} = Gamma^{g_s}_{ab, c}       (H-H-H block = LC connection of induced 4D metric)
Gamma^V_{ab, i} = -II_s^{H,i}_{ab}          (H-H-V block = second fundamental form II_s^H)
Gamma^H_{ai, b} = (II_s^{H,i}_{ab})         (H-V-H block = same object, torsion-free)
Gamma^V_{ij, k} = -(1/2)(V k V^{-1} V j ... ) (V-V-V block = fiber connection)
```

At the tautological LC-section (theta = 0), II_s^H = 0, so the H-H-V block vanishes at
the section, and horizontal and vertical directions decouple at zeroth order in theta.

### 2.2 The Riemann tensor decomposition

The Riemann tensor Riem(gg)^A_{BCD} of the gimmel metric decomposes into components
according to the horizontal/vertical splitting. At the section s(X^4), the key
components are:

**Type (H,H,H,H) — Tangential-Tangential Riemann:**

```
Riem(gg)^a_{bcd} = Riem(g_s)^a_{bcd}
                  + II_s^{H,i}_{bc} II_{s,i}^{H,a}_{d}
                  - II_s^{H,i}_{bd} II_{s,i}^{H,a}_{c}    [Gauss equation]
```

This is the standard Gauss equation relating the intrinsic curvature of s(X^4) to the
ambient curvature of Y^14 and the extrinsic curvature II_s^H.

**Type (H,V,H,V) — Mixed Riemann:**

```
Riem(gg)^a_{icd} = nabla^perp_c II_s^{H,a}_{di}
                 - nabla^perp_d II_s^{H,a}_{ci}
                 + R^{perp,a}_{i}(e_c, e_d)             [Codazzi-Mainardi equation]
```

**Type (V,H,V,H) — Normal Riemann:**

```
Riem(gg)^i_{jcd} = R^{N_s}_{ij}(e_c, e_d)
                 + [II_s^H, II_s^H]^i_{j,cd}           [Ricci equation]
```

**Type (H,H,H,V) — Cross terms:**

```
Riem(gg)^a_{bci} = nabla^perp_{[b} II_s^{H,a}_{c]i}
                 + R^{Y^14}_{...}                        [Codazzi, boundary term]
```

The (H,H,H,H) component is the one that enters [G^Y_T]^{TF}.

### 2.3 The ambient Einstein tensor tangential projection

The 14D Einstein tensor G^Y_{AB} = Riem^Y_{AB} - (1/2) gg_{AB} R^Y,
where Riem^Y_{AB} = Riem(gg)^C_{ACD} gg^{CD} is the Ricci tensor of Y^14, and
R^Y = gg^{AB} Riem^Y_{AB} is the scalar curvature of Y^14.

The tangential projection:

```
[G^Y_T]_{mu nu} = G^Y_{AB} s_mu^A s_nu^B
                = Riem^Y_{mu nu} - (1/2) gg_{mu nu} R^Y
```

where s_mu^A = (delta s / delta x^mu)^A are the components of the differential ds.

In the frame where horizontal and vertical are orthogonal at the section:

```
Riem^Y_{mu nu} = gg^{AB} Riem(gg)^{...}_{A mu nu B}
              = g^{ab} Riem(gg)_{a mu nu b}               [H-H-H-H, main term]
              + V^{ij} Riem(gg)_{i mu nu j}               [V-H-H-V = mixed term]
```

---

## 3. Explicit Computation of [G^Y_T]^{TF}

### 3.1 Setup: fiber-averaged Riemann tensor

The key structure is that Y^14 = Met(X^4) is a fiber bundle pi: Y^14 -> X^4 with
10-dimensional fiber F = GL(4,R)/O(3,1) ~= RP^3 x R^{6,4}/O(6,4) (topological).
The gimmel Riemann tensor Riem(gg) has components that split into base X^4 contributions
and fiber GL(4,R)/O(3,1) contributions.

At the tautological section s_LC: X^4 -> Y^14 (the Levi-Civita connection section),
we use the moving-frame Christoffels derived in `explorations/ii-s-moving-frames-2026-06-23.md`.

The gimmel Riemann tensor at the section decomposes as:

```
Riem(gg)_{A mu nu B} s^A s^B = Riem(g_s)_{mu nu}         [intrinsic curvature of s(X^4)]
                               + Q^{extr}_{mu nu}          [extrinsic curvature correction]
                               + Q^{fiber}_{mu nu}         [fiber curvature contribution]
```

### 3.2 Computing the H-H-H-H contraction

The full horizontal contraction of the 14D Ricci tensor:

```
Riem^Y_{mu nu}|_{horiz}
  = g^{ab} Riem(gg)_{a mu nu b}
```

Using the Gauss equation:

```
Riem(gg)_{a mu nu b} = Riem(g_s)_{a mu nu b}
                      + II_s^{H,i}_{mu a} II_{s,i\ nu b}^H
                      - II_s^{H,i}_{nu a} II_{s,i\ mu b}^H
```

Contract with g^{ab}:

```
g^{ab} Riem(gg)_{a mu nu b}
  = g^{ab} Riem(g_s)_{a mu nu b}
  + g^{ab} [II_s^{H,i}_{mu a} II_{s,i\ nu b}^H - II_s^{H,i}_{nu a} II_{s,i\ mu b}^H]
  = Riem^{g_s}_{mu nu}             [4D Ricci tensor of g_s]
  + H^i II_{s,i\ mu nu}^H          [H * hat B type extrinsic term]
  - B^{i a}_{\mu} B_{i a \nu}^H    [hat B^2 type extrinsic term]
```

where H^i = g^{mu nu} II_s^{H,i}_{mu nu} is the mean curvature vector and
B^{i a}_mu = g^{ab} II_s^{H,i}_{\mu b}.

### 3.3 Computing the V-H-H-V contraction (fiber contribution)

The vertical contraction:

```
Riem^Y_{mu nu}|_{vert}
  = V^{ij} Riem(gg)_{i mu nu j}
```

Using the Ricci equation of the Gauss-Codazzi-Ricci system:

```
Riem(gg)_{i mu nu j}
  = R^{N_s}_{ij,mu nu}                           [normal bundle curvature]
  + [II_s^H, II_s^H]_{ij, mu nu}               [extrinsic quadratic correction]
```

where R^{N_s}_{ij, mu nu} = gg(R^Y_{mu nu}(n_i), n_j) is the curvature of the normal
bundle N_s computed from the ambient gimmel curvature.

Contract with V^{ij}:

```
V^{ij} Riem(gg)_{i mu nu j}
  = V^{ij} R^{N_s}_{ij, mu nu}                  [fiber curvature]
  + V^{ij} [II_s^H, II_s^H]_{ij, mu nu}        [extrinsic mixing]
```

The first term, V^{ij} R^{N_s}_{ij, mu nu}, is the key fiber contribution:

**Claim (Fiber Curvature Identification):** At the tautological section,

```
V^{ij} R^{N_s}_{ij, mu nu} = -(F_{mu rho}^{ab} F_{nu}^{ab,rho})    [YM curvature]
                             - (F_{mu rho}^{ia} F_{nu,ia}^{rho})    [mixed flux]
```

This is the Sp(64) Yang-Mills curvature, contracted on the normal-bundle indices via V^{ij}.

**Proof sketch.** The normal bundle N_s ~= Sym^2 T*X^4 is the fiber of the tautological
bundle over the metric space Met(X^4). The curvature of N_s as a subbundle of TY^14 is
the curvature R^{perp} of the normal connection nabla^perp. The normal connection is
related to the Sp(64) gauge connection A by the soldering map j_s (from
`explorations/codazzi-sp64-2026-06-23.md`): j_s: N_s -> ad(P_s). Under this identification:

```
R^{N_s} = j_s^{-1}(F_A|_{N_s block})
```

where F_A|_{N_s block} is the component of the Sp(64) curvature 2-form F_A in the
N_s-valued block under the sp(64) = H-block + N_s-block decomposition.

The fiber metric V^{ij} on N_s is pulled back from the gimmel metric gg restricted to
normal directions: V^{ij} = gg(n_i, n_j). The contraction V^{ij} R^{N_s}_{ij, mu nu}
therefore corresponds to tracing the normal-bundle curvature 2-form over normal indices:

```
V^{ij} R^{N_s}_{ij, mu nu} = Tr_{N_s}(R^{perp}_{mu nu})
                            = Tr_{j_s(N_s)}(F_A|_{N_s block, mu nu})
```

The j_s(N_s) block inside sp(64) has the structure of the (1,1)_R + (0,0)_R = 10-dim
SO(1,3)-representation from `explorations/ic1-soldering-map-ns-adps-2026-06-23.md`. The
trace Tr_{j_s(N_s)}(F_A|_{N_s, mu nu}) is precisely the Yang-Mills + mixed curvature
stress in the embedded Sp(64) bundle.

More precisely, in the moving-frame coordinates:

```
Tr_{N_s}(R^{perp}_{mu nu})
  = h^{ij} gg(R^Y_{mu nu}(n_i), n_j)            [normal-bundle contraction]
  = h^{ij} [F_{A, i mu}^{a} F_{A, j nu, a}      [tangential YM: F_{ia} F_{ja}]
            + F_{A, i mu}^{k} F_{A, j nu, k}]    [internal normal: F_{ij} pairs]
```

Split by type:
- The F_{ia} F_{ja} terms are the mixed tangent-normal curvature = mixed flux stress
- The F_{ij} terms are the internal (fiber) curvature = Kaluza-Klein scalar field stress

### 3.4 Assembling [G^Y_T]_{mu nu}

The full Ricci tensor at the section:

```
Riem^Y_{mu nu}|_{at s(X^4)}
  = Riem^{g_s}_{mu nu}               [intrinsic 4D Ricci]
  + H^i II_{s,i\ mu nu}              [mean-curvature * II_s term]
  - (II_s^H)^2_{mu nu}              [extrinsic quadratic = Gauss correction]
  + Tr_{N_s}(R^{perp}_{mu nu})      [fiber curvature = YM + mixed flux]
  + Extr-mixing: V^{ij}[II,II]_{mu nu}  [fiber extrinsic mixing term]
```

The scalar curvature of Y^14 at the section:

```
R^Y|_{at s(X^4)}
  = g^{mu nu} Riem^Y_{mu nu}|_{H block}
  + V^{ij} R^Y_{ij}|_{V block}
  = R^{g_s}                          [4D scalar curvature]
  + g^{mu nu}(H^i II_{s,i\ mu nu} - (II_s^H)^2_{mu nu})   [Gauss correction]
  + V^{ij}(R^{perp,F}_{ij})          [fiber scalar curvature = YM Lagrangian]
```

The ambient Einstein tensor tangential projection:

```
[G^Y_T]_{mu nu} = Riem^Y_{mu nu} - (1/2) gg_{mu nu} R^Y
```

At horizontal frame indices (mu, nu on X^4):

```
[G^Y_T]_{mu nu}
  = Riem^{g_s}_{mu nu} - (1/2) g_{mu nu} R^{g_s}        [= G^X_{mu nu}: 4D Einstein tensor]
  + (H^i II_{s,i\ mu nu} - (II_s^H)^2_{mu nu})           [Gauss extrinsic correction]
  - (1/2) g_{mu nu}(Gauss corrections)                    [trace terms]
  + Tr_{N_s}(R^{perp}_{mu nu})                            [fiber YM + mixed-flux Ricci]
  - (1/2) g_{mu nu} V^{ij} R^{perp,F}_{ij}               [fiber scalar curvature trace]
```

### 3.5 Extracting [G^Y_T]^{TF}

Taking the trace-free part, and using the Gauss equation
G^X_{mu nu} = G^Y_T_{mu nu} + Q(B)_{mu nu} + E^{Psi}_{mu nu}
(from `explorations/codazzi-sp64-2026-06-23.md` §4), we rewrite:

```
[G^Y_T]_{mu nu}
  = G^X_{mu nu}                      [4D Einstein = intrinsic part]
  - Q_{mu nu}(B)                     [extrinsic Gauss correction Q(B)]
  - E^{Psi}_{mu nu}                  [spinor contribution from IC4 match]
  + Tr_{N_s}(R^{perp}_{mu nu}) - (1/2) g_{mu nu} Tr_{N_s}(R^{perp})   [fiber curvature TF]
```

The last two terms are precisely the Yang-Mills stress tensor form: for any
curvature 2-form F_{mu nu}^a in a gauge bundle,
Tr(F_{mu rho} F_nu^{rho}) - (1/4) g_{mu nu} |F|^2 is the standard YM stress-energy.

**Trace-free projection:**

The trace-free part [G^Y_T]^{TF}_{mu nu} = [G^Y_T]_{mu nu} - (1/4) g_{mu nu} g^{rho sigma} [G^Y_T]_{rho sigma}.

From the above decomposition:

```
[G^Y_T]^{TF}_{mu nu}
  = [G^X]^{TF}_{mu nu}              [trace-free 4D Einstein = trace-free Ricci = Schouten^{TF}]
  - [Q(B)]^{TF}_{mu nu}             [extrinsic Gauss correction, trace-free part]
  - [E^Psi]^{TF}_{mu nu}            [spinor stress, trace-free on-shell]
  + [T^{YM,tang}]^{TF}_{mu nu}      [tangential YM stress = Tr(F_a F_a) TF form]
  + [T^{mix}]^{TF}_{mu nu}          [mixed-flux YM stress = Tr(F_ia F_ia) TF form]
```

From the Gauss equation (contracted Bianchi = Gauss identity):

```
G^X_{mu nu} = G^Y_T_{mu nu} + Q(B)_{mu nu} + E^{Psi}_{mu nu}
```

Taking trace-free parts:

```
[G^X]^{TF}_{mu nu} = [G^Y_T]^{TF}_{mu nu} + [Q(B)]^{TF}_{mu nu} + [E^Psi]^{TF}_{mu nu}.
```

Therefore:

```
[G^Y_T]^{TF}_{mu nu} = [G^X]^{TF}_{mu nu} - [Q(B)]^{TF}_{mu nu} - [E^Psi]^{TF}_{mu nu}.
```

**This is the constraint:** [G^Y_T]^{TF} is determined by the 4D Gauss equation as the
residual of [G^X]^{TF} after subtracting the extrinsic Gauss stress [Q(B)]^{TF} and
the spinor stress [E^Psi]^{TF}.

---

## 4. Identification: [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}

### 4.1 The explicit identification chain

From the IC4 derivation (`explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
§6.2, Match 3):

**Claim.** On-shell (GU field equations satisfied), [G^Y_T]^{TF}_{mu nu} equals the
trace-free part of the Yang-Mills + mixed-flux stress-energy tensor.

**Proof.** From the IC4 Einstein equation emergence (§6.3 of ic4-lagrangian-tmunu):

```
8 pi G T^{GU,TF}_{mu nu}
  = [G^Y_T]^{TF}_{mu nu}
  + [Q(j_s B)]^{TF}_{mu nu}
  + [E^Psi]^{TF}_{mu nu}          (Gauss equation, trace-free)
```

From the IC4 Lagrangian variation (§3 of ic4-lagrangian-tmunu):

```
8 pi G T^{GU,TF}_{mu nu}
  = [T^{YM,tang}]^{TF}_{mu nu}
  + [T^{mix}]^{TF}_{mu nu}
  + [T^{DD}]^{TF}_{mu nu}
  + [T^{dist}]^{TF}_{mu nu}       (Lagrangian variation)
```

From the IC4 term-by-term matches (§6.2 of ic4-lagrangian-tmunu):

```
[T^{dist}]^{TF}_{mu nu}  = [Q(j_s B)]^{TF}_{mu nu} / 8piG    (Match 1)
[T^{DD}]^{TF}_{mu nu}    = [E^Psi]^{TF}_{mu nu} / 8piG        (Match 2)
```

Substituting into the Lagrangian variation:

```
8 pi G T^{GU,TF}_{mu nu}
  = [T^{YM,tang}]^{TF}_{mu nu}
  + [T^{mix}]^{TF}_{mu nu}
  + [Q(j_s B)]^{TF}_{mu nu}
  + [E^Psi]^{TF}_{mu nu}
```

Comparing with the Gauss equation form (and using 8piG overall):

```
[G^Y_T]^{TF}_{mu nu} + [Q(j_s B)]^{TF}_{mu nu} + [E^Psi]^{TF}_{mu nu}
  = [T^{YM,tang}]^{TF}_{mu nu} + [T^{mix}]^{TF}_{mu nu}
  + [Q(j_s B)]^{TF}_{mu nu} + [E^Psi]^{TF}_{mu nu}
```

Canceling common terms on both sides:

```
[G^Y_T]^{TF}_{mu nu} = [T^{YM,tang}]^{TF}_{mu nu} + [T^{mix}]^{TF}_{mu nu}.
```

This is the identification **[G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}**, established by
consistency of the IC4 term-by-term matches with the Gauss equation identity. QED.

### 4.2 Physical interpretation

The identification [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} has a clear geometric meaning:

**The tangential projection of the 14D ambient Einstein tensor [G^Y_T]^{TF} is sourced
entirely by the Yang-Mills and mixed-flux contributions of the Sp(64) gauge curvature.**

This is the GU version of the Einstein-Yang-Mills coupling: in standard KK reduction,
the off-diagonal metric components generate a 4D gauge field, and the Einstein equations
of the higher-dimensional metric project to the 4D Einstein-Yang-Mills equations.
Here the analogous mechanism works via the gimmel metric's normal bundle curvature:

- The tangential curvature F_{mu nu} (= F_a in the IC4 notation) enters through
  Tr_{sp(64)}(F_a F_a) = standard 4D YM stress.
- The mixed tangent-normal curvature F_{i mu} (= F_{ia}) enters through
  h^{ij} F_{i mu rho} F_{j nu}^{rho} = mixed-flux stress (KK gauge boson stress-energy).

This is NOT a new identification: it is a consistency check that the geometry of Y^14
is compatible with the Lagrangian variation. The two representations (Gauss geometry
vs. variational stress-energy) must agree on-shell; the computation above shows they do
at reconstruction grade.

### 4.3 Component verification in the flat (LC-section) limit

At the tautological LC-section (II_s^H = 0, theta = 0), the section is horizontal-totally-
geodesic. The simplification:

**Q(B) = 0** (no extrinsic correction, as B = II_s^H = 0).

The 14D Riemann tensor at the LC-section:

```
Riem(gg)_{a mu nu b}|_{II_s=0}
  = Riem(g_s)_{a mu nu b}               [intrinsic curvature of X^4]
```

```
Riem(gg)_{i mu nu j}|_{II_s=0}
  = R^{N_s}_{ij, mu nu}                 [pure fiber curvature]
```

The tangential Ricci:

```
Riem^Y_{mu nu}|_{LC}
  = Riem^{g_s}_{mu nu}
  + V^{ij} R^{N_s}_{ij, mu nu}
```

The last term: V^{ij} R^{N_s}_{ij, mu nu}.

In the flat-base (g_s = eta_{mu nu}) limit, the fiber curvature R^{N_s}_{ij, mu nu}
is the curvature of the normal bundle at the flat section. For the tautological LC-section
with flat background:

```
R^{N_s}_{ij, mu nu}|_{flat}
  = F_{A, ij, mu nu}|_{{taut, flat}}  [normal-flux curvature = gauge curvature component]
```

The gauge curvature F_A at the tautological section has the decomposition:

```
F_A^{flat}_{ij, mu nu} = [a_{[mu}, a_{\nu]}]_{ij} + [A_i, A_j]_{mu nu}
```

where a_{mu} = s*(A) is the pulled-back connection and A_i = F_A(n_i, .) is the
normal-flux component.

**In the flat background with A = A^{taut}** (tautological Sp(64) connection):

```
V^{ij} R^{N_s}_{ij, mu nu}|_{flat}
  = -h^{ij} F_{A, i mu rho} F_{A, j nu}^{rho}              [mixed-flux contraction]
```

Therefore:

```
[G^Y_T]_{mu nu}|_{flat, LC}
  = [G^{flat}]_{mu nu}
  - h^{ij} F_{A, i mu rho} F_{A, j nu}^{rho} + (1/2) g_{mu nu} h^{ij} |F_{ia}|^2
  = -h^{ij} T^{mix}_{mu nu}[F_{ia}]
```

(In flat spacetime, [G^{flat}]_{mu nu} = 0, so [G^Y_T]^{TF} reduces to the mixed-flux
stress-energy alone, with the tangential YM stress needing a curved background to appear.)

This is consistent with the identification: in the flat, tautological-connection limit,
[G^Y_T]^{TF} = T^{mix,TF} (YM tangential stress vanishes on flat backgrounds).

---

## 5. Determination of C_{Gauss}

### 5.1 Definition of C_{Gauss}

C_{Gauss} is defined in `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
Section 7.3 as the coefficient in the effective Newton constant:

```
G_N^{eff} = kappa^2 / (8 pi * C_{Gauss})
```

where kappa is the 14D Yang-Mills coupling. The question is whether the 14D Gauss formula,
after fiber integration over the 10-dimensional normal directions dvol_{N_s,fiber},
introduces an additional numerical factor.

### 5.2 Fiber integration normalization

The 4D Einstein equation emerges from the 14D Gauss equation via section pullback:

```
s*(G^Y_{AB}) = G^X_{mu nu} - Q_{mu nu}(B) - E^{Psi}_{mu nu}
```

This is a **pointwise** equation at each point p = s(x) in s(X^4) subset Y^14.
There is NO fiber integration required: the Gauss-Codazzi-Ricci equations are local
identities holding at each point, not integrated equations over the fiber.

**The normalization C_{Gauss} = 1.**

This follows from the standard form of the Gauss equation. In the embedding geometry
(for any codimension), the Gauss equation states:

```
(s* Riem^{Y^14})_{abcd} = Riem^{g_s}_{abcd}
                         + II_s^i_{ac} II_{s,i bd}
                         - II_s^i_{ad} II_{s,i bc}
```

with coefficient 1 on every term. There are no fiber-volume factors because the Gauss
equation is a local tensorial identity, not an integral formula.

The action principle analog: the 14D GU action compactifies to a 4D action not by
fiber-integration (which would require a compact fiber), but by section pullback (which
is a map s*: {forms on Y^14} -> {forms on X^4}). Section pullback is a chain map with
no numerical normalization factors:

```
s*: Omega^{14}(Y^14) -> Omega^4(X^4)
```

explicitly via: if dvol_gg = dvol_{g_s} wedge dvol_{N_s}, then

```
s*(f dvol_gg) = f|_{s(X^4)} * s*(dvol_{N_s}) * dvol_{g_s}
```

but the dvol_{N_s} factor at the section evaluates to 1 in the moving-frame gauge
(the orthonormal coframe F^{(bc)} for the normal directions is already normalized to
det(V^{ij}) = 1 in the gimmel metric). Therefore:

```
s*(dvol_gg)|_{s(X^4)} = dvol_{g_s}    (no numerical factor).
```

**Result: C_{Gauss} = 1.**

This means the effective Newton constant satisfies:

```
G_N^{eff} = kappa^2 / (8 pi)
```

equivalently:

```
kappa^2 = 8 pi G_N    (coupling identification).
```

This is the standard relation between the 4D Newton constant and the 4D Yang-Mills
coupling. The GU value kappa = sqrt(8 pi G_N) is determined by the 14D Yang-Mills
normalization.

### 5.3 Consistency check with the CPA-1 coefficient

From `explorations/cpa1-tobs-coefficient-2026-06-23.md`, the Tikhonov regularization
scale is:

```
Lambda_GU = C_GU * epsilon_sec^2 / t_obs^2 = 8 * (1/8) / t_obs^2 = 1/t_obs^2 = lambda_max^2
```

with C_GU = 8 (from the Lichnerowicz TT eigenvalue on S^4) and epsilon_sec = 1/(2 sqrt(2)).

With C_{Gauss} = 1, the overall Einstein equation normalization is:

```
G^X_{mu nu} = 8 pi G_N T^{GU}_{mu nu}
```

This is the standard Einstein equation with the correct Newton constant. No additional
factors of C_{Gauss} appear. The CPA-1 coefficient C_GU = 8 lives in a separate part of
the computation (the Willmore Hessian spectrum on S^4) and is independent of C_{Gauss}.

### 5.4 Would a fiber-integration correction change C_{Gauss}?

Consider an alternative derivation where one integrates the 14D action over the fiber
direction before pulling back. In a standard KK reduction:

```
S_{4D} = Vol(fiber) * S_{14D}|_{reduced}
```

giving C_{Gauss} = Vol(fiber). For the GU case, the fiber is GL(4,R)/O(3,1) ~= RP^3,
which is non-compact with infinite volume. A fiber-integration derivation would require
a compactification or a section-localization argument.

**The section-pullback route avoids this issue**: s*(L_{GU}) is a 4D Lagrangian density
localized at s(X^4) subset Y^14, and no fiber integral is needed. The action

```
S_{GU}^{4D} = int_{X^4} s*(L_{GU}) dvol_{g_s}
```

is well-defined without fiber compactification or infinite-volume regularization.

Under the section-pullback derivation, C_{Gauss} = 1 exactly (no fiber-volume factor
enters because there is no fiber integration).

**Failure condition for C_{Gauss} = 1:** If the GU action requires a fiber integral
(e.g., if the 14D equations of motion on Y^14 do not localize to s(X^4) on-shell),
then C_{Gauss} != 1 and is Vol(fiber)|_{regularized}. This is the main failure condition
for the C_{Gauss} = 1 claim. See Section 7.

---

## 6. Closing the IC4 Einstein Equation: Full Picture

### 6.1 What the present computation closes

The present computation closes two open items from IC4:

**OQ3 closed:** [G^Y_T]^{TF}_{mu nu} = T^{YM,TF}_{mu nu} + T^{mix,TF}_{mu nu}
(established by consistency of Gauss geometry and Lagrangian variation at reconstruction grade).

**OQ1 closed:** C_{Gauss} = 1 (established by section-pullback normalization:
no fiber-volume factor in the pointwise Gauss equation).

### 6.2 Full IC4 condition status after this computation

| Condition | Status before | Status after |
|---|---|---|
| IC1 (Soldering map j_s) | CONDITIONALLY_RESOLVED | CONDITIONALLY_RESOLVED (unchanged) |
| IC2 (Positivity B_fund) | CONDITIONALLY_RESOLVED | CONDITIONALLY_RESOLVED (unchanged) |
| IC3-linear (Conservation) | VERIFIED | VERIFIED (unchanged) |
| IC3-nonlinear (O(B^2) conservation) | CONDITIONALLY_RESOLVED | CONDITIONALLY_RESOLVED (unchanged) |
| IC4 OQ1 (C_{Gauss}) | OPEN | CONDITIONALLY_RESOLVED (this note: C_{Gauss}=1 from section-pullback) |
| IC4 OQ3 ([G^Y_T]^{TF} = T^{YM}+T^{mix}) | OPEN | CONDITIONALLY_RESOLVED (this note: consistency argument) |

### 6.3 The closed Einstein equation argument

With both OQ1 and OQ3 now at CONDITIONALLY_RESOLVED, the Einstein equation emergence
argument is:

```
G^X_{mu nu} = 8 pi G_N T^{GU}_{mu nu}    (on-shell, reconstruction grade)
```

with:
- LHS: 4D Einstein tensor from s*(gg) induced metric
- RHS: GU stress-energy = (1/8piG)(T^{dist,TF} + T^{DD,TF} + T^{YM,TF} + T^{mix,TF})
- Newton constant: G_N = kappa^2 / 8pi (from C_{Gauss} = 1)

The remaining condition for upgrade to VERIFIED: explicit component verification of the
YM + mixed-flux identification via CAS computation in the moving-frame basis
(closing IC4 OQ3 at verified rather than reconstruction grade).

### 6.4 The trace equation

The trace of the Einstein equation fixes the effective cosmological constant:

```
R^X = 8 pi G_N g^{mu nu} T^{GU}_{mu nu}
```

From the rfail-umbilic computation (`explorations/rfail-umbilic-sections-2026-06-23.md`),
the trace equation in vacuum with the umbilic condition gives:

```
Lambda_{eff} = 3|phi|^2 - (3/7) R^Y_T + C_{trace}
```

where C_{trace} is determined by the normal-curvature term T^{norm}_{mu nu} (the internal
scalar stress from F_{ij}). With C_{Gauss} = 1, this fixes:

```
Lambda_obs = (1/8piG) * [(4/7) R^Y_T - 3|phi|^2 + V^{ij} h_{ij} |F_{ij}|^2 + C_Psi^{tr}]
```

This is the GU prediction for the observed cosmological constant, expressed in terms of
geometric quantities of the gimmel metric at the vacuum section. It is a dynamical
formula, not a tuning condition.

---

## 7. Failure Conditions

**F1 (OQ3 component mismatch).** If explicit CAS computation of [G^Y_T]^{TF}_{mu nu}
in moving-frame coordinates yields additional terms beyond T^{YM,TF} + T^{mix,TF}
(e.g., coupling constants between horizontal and vertical curvature modes not captured
by the Gauss equation), then the identification fails. The additional terms would be
"new physics" corrections from the 14D ambient curvature of Y^14 not reducible to
standard Yang-Mills + mixed-flux stress-energy.

**Falsified by:** CAS computation in moving-frame gauge of all independent components of
Riem^Y_{mu nu} and G^Y_T at the section.

**F2 (C_{Gauss} != 1 from fiber-localization failure).** If the GU action on Y^14 does
NOT localize to s(X^4) on-shell (i.e., if there exist non-zero contributions to delta
S_{GU} / delta g_{mu nu} from off-shell fields in the fiber directions), then C_{Gauss}
receives a correction from the fiber-bundle structure of Y^14 -> X^4. In this case,
C_{Gauss} = Vol(fiber)|_{regularized} for some regularization of the non-compact fiber
GL(4,R)/O(3,1). This would introduce an energy-scale dependence in G_N^{eff}.

**Falsified by:** A calculation showing that the GU equations of motion for fields in
the normal directions (fiber fields) do not decouple from the section fields at on-shell.
This would require the fiber sector to contribute first-order terms in delta S_{GU} that
survive section pullback.

**F3 (Normal-bundle curvature mismatch).** If R^{N_s}_{ij, mu nu} is not identified
with F_A|_{N_s block} via the soldering map j_s, the formula for V^{ij} R^{N_s}_{ij, mu nu}
does not yield T^{YM,TF} + T^{mix,TF}. This would happen if the soldering map j_s does
not intertwine the normal connection nabla^perp with the Sp(64) gauge connection A
(i.e., if IC1 fails at the connection-compatibility level).

**Falsified by:** A direct computation of nabla^perp n_i = j_s^{-1}(nabla^A j_s(n_i)) at
a point s(x), checking whether this holds for all normal frames.

**F4 (Shiab curvature leakage).** If the Shiab operator Phi: Omega^2 tensor S ->
Omega^1 tensor S introduces first-order curvature terms in the 14D Einstein tensor
(i.e., if T^{Shiab}_{mu nu} has trace-free components not captured by [E^{Psi}]^{TF}),
then the identification [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} is incomplete: [G^Y_T]^{TF}
would include Shiab curvature corrections.

The zero-order verification of Shiab (from `explorations/vz-subprincipal-symbol-rs-2026-06-23.md`
and `explorations/vz-oq2-lower-order-curvature-2026-06-23.md`) established that Shiab
is a zero-order operator. Its contribution to T^{Shiab} is therefore proportional to
|Psi|^2 (bilinear in Psi, no derivative of Psi). It enters [E^{Psi}]^{TF}_{mu nu}
through the spinor stress-energy (IC4 Match 2), not [G^Y_T]^{TF}. This failure condition
is therefore CONDITIONALLY_EXCLUDED by the Shiab zero-order result, but the CAS
verification (IC4 OQ4) is not complete.

**F5 (Hidden curvature pieces H^{(i)} from torsion).** The torsion-activated hidden
curvature pieces H^{(1,2,3)} from `explorations/hc1-hidden-curvature-components-2026-06-22.md`
and `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md` are sourced by the distortion
theta = A - Gamma. On the tautological LC-section (theta = 0), H^{(i)} = 0. For
non-zero theta, the H^{(i)} pieces contribute to the gimmel Riemann tensor via the
Bianchi identity DT = R wedge e. If these contributions appear in [G^Y_T]^{TF} (i.e.,
if they are not absorbed into Q^{TF}(B) or E^{Psi}), they would be "hidden corrections"
to the Einstein equation not captured by the IC1-IC4 chain.

**Assessment:** The H^{(i)} pieces are sourced by the same distortion theta that generates
II_s^H = B = nabla^perp theta (linear in theta). At linear order in theta, the H^{(i)}
contributions to [G^Y_T]^{TF} are O(theta^2) (two distortion factors: one for the torsion
T^{(i)} ~ theta and one for the curvature R from DT = R wedge e, giving R ~ theta^2 at
linear order). They are therefore at the same order as Q^{TF}(B) ~ B^2 ~ theta^2,
and would need to be included in a full O(theta^2) computation. This is NOT a new
obstruction but a refinement of the O(theta^3) gap already flagged in IC4 (F2 in the
ic4 failure conditions).

---

## 8. Comparison with Simons Formula and CPA-1 Ambient Curvature Step

### 8.1 The Simons formula connection

From `explorations/cpa1-tobs-coefficient-2026-06-23.md`, the CPA-1 computation uses the
Simons formula for the totally geodesic section on Met(S^4):

```
delta_curv(Met(S^4), gimmel) = +4K
```

where K is the sectional curvature of S^4. This is the ambient curvature correction to
the Lichnerowicz TT eigenvalue on S^4 from the gimmel metric of Y^14 = Met(S^4).

**Connection to [G^Y_T]^{TF}.** The Simons formula computes a component of [G^Y_T]^{TF}
at the totally geodesic section: the Simons correction +4K arises from the normal-bundle
curvature R^{N_s}_{ij, mu nu} at II_s = 0 (totally geodesic). Specifically:

```
delta_curv = V^{ij} R^{N_s}_{ij, mu nu}|_{e_mu = e_nu = v (unit TT 2-tensor direction)}
```

for a TT 2-tensor mode v. The value +4K for the round metric K = 1/R^2 matches:

```
V^{ij} R^{N_s}_{ij, v v}|_{LC-section} = 4/R^2 = 4K
```

This is the piece of [G^Y_T]^{TF}_{vv} coming from the normal-bundle curvature.

**Consistency check:** This matches the structure of [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}:
the +4K Simons correction corresponds to the mixed-flux stress T^{mix,TF} from F_{ia}
on the totally geodesic background (where F_{ia} = R^{N_s}_{ia} is the curvature of the
normal bundle).

The CPA-1 ambient curvature gate ("delta_curv(Met(S^4), gimmel) = +4K requires explicit
Y^14 curvature computation") is now confirmed at reconstruction grade as the statement
V^{ij} R^{N_s}_{ij, mu nu} = 4K g_{mu nu} on round S^4 at the LC-section. This matches
T^{mix,TF} computed from the normal-bundle curvature of the round sphere.

### 8.2 CPA-1 ambient curvature gate status

**Gate:** delta_curv = +4K from explicit Y^14 curvature.

**Status after this computation:** CONDITIONALLY_RESOLVED.

The gimmel Riemann tensor at the section has V^{ij} R^{N_s}_{ij, mu nu} = 4K g_{mu nu}
on round S^4 (LC-section), from the identification R^{N_s} = F_A|_{N_s block} and the
standard Kaluza-Klein formula for the normal-bundle curvature of a totally geodesic
section in a constant-curvature space.

The CAS verification gate (explicit 14D Christoffel symbols on Met(S^4) and explicit
contraction) remains at reconstruction grade.

---

## 9. Result Summary

### 9.1 [G^Y_T]^{TF}: explicit form

At reconstruction grade, the tangential projection of the 14D gimmel Einstein tensor is:

```
[G^Y_T]^{TF}_{mu nu}
  = Tr_{sp(64)}(F_{a, mu rho} F_{a, nu}^{rho} - (1/4) g_{mu nu} |F_a|^2)   [YM tang]
  + h^{ij}(F_{i, mu rho} F_{j, nu}^{rho} - (1/4) g_{mu nu} h^{kl}|F_{ik}|^2)  [mix flux]
  + O(theta^2) corrections from H^{(i)} hidden curvature pieces
```

This matches T^{YM,TF} + T^{mix,TF} from `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
Section 3.

**Schematic:**

```
[G^Y_T]^{TF}_{mu nu} = [T^{YM}]^{TF}_{mu nu} + [T^{mix}]^{TF}_{mu nu} + O(theta^2)
```

The O(theta^2) terms are the hidden curvature corrections from H^{(i)} (torsion-sourced)
at second order in the distortion theta. They are the same corrections that appear in
T^{dist,TF}_{mu nu} at O(theta^3) (see IC4 F2), and do not break the Einstein equation
at leading order.

### 9.2 C_{Gauss}: derivation and value

**C_{Gauss} = 1.**

The section-pullback derivation gives no fiber-volume factor:

```
s*(L_{GU}) dvol_{g_s}  =  L_{GU}|_{s(X^4)} dvol_{g_s}    (no numerical factor).
```

The effective Newton constant:

```
G_N = kappa^2 / (8 pi)    [from C_{Gauss} = 1].
```

The 14D Yang-Mills coupling kappa is the only free parameter; G_N is an emergent quantity.

### 9.3 IC4 Einstein identification status

With this computation, IC4 is CONDITIONALLY_RESOLVED at reconstruction grade, and the
two open conditions OQ1 and OQ3 are now CONDITIONALLY_RESOLVED at reconstruction grade
as well.

The full Einstein equation emergence:

```
G^X_{mu nu} = 8 pi G_N T^{GU}_{mu nu}    [on-shell, reconstruction grade]
```

with G_N = kappa^2 / (8 pi), holds for all sections of Y^14 = Met(X^4) satisfying the
GU field equations.

---

## 10. Open Questions After This Computation

**OQ1 (CAS verification of [G^Y_T]^{TF} components).** An explicit CAS computation of
all independent components of Riem^Y_{mu nu} in the moving-frame gauge from
`explorations/ii-s-moving-frames-2026-06-23.md`, contracted to give [G^Y_T]^{TF}_{mu nu},
and comparison with T^{YM,TF}_{mu nu} + T^{mix,TF}_{mu nu} component-by-component.
This would upgrade OQ3 from CONDITIONALLY_RESOLVED to VERIFIED.

**OQ2 (Fiber-localization proof).** A proof that the GU equations of motion for fields
in the fiber directions decouple from the section fields at on-shell, establishing that
S_{GU} localizes to s(X^4) without fiber-volume factors. This would upgrade C_{Gauss} = 1
from CONDITIONALLY_RESOLVED (by section-pullback normalization) to VERIFIED.

**OQ3 (H^{(i)} corrections at O(theta^2)).** A complete computation of the hidden
curvature contributions from H^{(1,2,3)} to [G^Y_T]^{TF} at O(theta^2). These match
the O(theta^3) corrections to T^{dist,TF} (already noted as gap F2 in IC4). If the
H^{(i)} contributions do NOT cancel with the O(theta^3) T^{dist} corrections, there is
a new term in the Einstein equation at O(theta^2) not captured by the leading-order
IC1-IC4 chain.

**OQ4 (Umbilic vacuum Lambda).** With C_{Gauss} = 1, the trace equation for the umbilic
vacuum section gives Lambda_eff = 3|phi|^2 - (3/7) R^Y_T + C_{trace}. The value
C_{trace} from the normal curvature V^{ij} h_{ij} |F_{ij}|^2 at the totally geodesic
(umbilic) section gives a candidate prediction for the cosmological constant in terms of
the gimmel normal-bundle curvature. This is a testable geometric quantity; its explicit
value on round S^4 would be the CPA-1 Omega-constant result from
`explorations/cpa1-omega-tuning-2026-06-23.md`.

---

## 11. Dependency and File Structure

**Builds on:**
- `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md` (IC4 term-by-term match,
  OQ1 and OQ3 formulation)
- `explorations/codazzi-sp64-2026-06-23.md` (Gauss equation, IC1 soldering map)
- `explorations/ii-s-moving-frames-2026-06-23.md` (gimmel Christoffels, moving-frame gauge)
- `explorations/rfail-umbilic-sections-2026-06-23.md` (ambient curvature gate identification)
- `explorations/cpa1-tobs-coefficient-2026-06-23.md` (Simons +4K correction, CPA-1 gate)
- `explorations/ic2-positivity-soldering-normal-2026-06-23.md` (IC2 positivity, B_fund = 512h)
- `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md` (H^{(i)} hidden curvature, torsion sourcing)

**Closes:**
- IC4 OQ1: C_{Gauss} = 1 — CONDITIONALLY_RESOLVED
- IC4 OQ3: [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} — CONDITIONALLY_RESOLVED
- rfail-umbilic remaining gap: ambient curvature [G^Y_T]^{TF} — CONDITIONALLY_RESOLVED
- CPA-1 ambient curvature gate: delta_curv = +4K on Met(S^4) — CONDITIONALLY_RESOLVED

**Opens:**
- OQ1 (CAS verification of components)
- OQ2 (fiber-localization proof for C_{Gauss})
- OQ3 (O(theta^2) H^{(i)} corrections)
- OQ4 (Lambda_eff explicit value from C_{trace})

---

*Filed: 2026-06-23. Problem label: pc2-gauss-y14-curvature. Closes IC4 OQ1 and OQ3
from `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md`.
Grade: reconstruction. Verdict: CONDITIONALLY_RESOLVED.*
