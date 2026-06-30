---
title: "Codazzi Equation for the Sp(64) Bundle"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "NORMAL_FLUX_AND_EINSTEIN_FAILURE_TENSORS_IDENTIFIED"
depends_on:
  - "DERIVATION-PROGRESS.md"
  - "NEXT-STEPS.md"
  - "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md"
  - "explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md"
  - "explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md"
---

# Codazzi Equation for the Sp(64) Bundle

**Status.** Exploration-grade bounded derivation. This note formulates the
Gauss-Codazzi-Ricci system for a section

```text
s: X^4 -> Y^14 = Met(X^4)
```

and for the associated Sp(64) bundle over \(Y^14\). It does not claim that GU
derives Einstein's equations. It isolates the precise correction term that must
vanish or be identified with physical stress-energy for the 4D Einstein equation
to be recovered.

**Verdict.** The Codazzi/Sp(64) blocker is not an anomaly or dimension issue. The
Sp(64) and tau+ construction survives the (9,5) correction. The blocker is the
**normal-flux / Sp(64)-curvature residual** created when the 14D field equation is
pulled back along a section. In formulas:

```text
s*(D_A^* F_A) = D_a^* F_a + K(A,s),
```

where \(a=s^*A\). The extra term \(K(A,s)\) is the normal Codazzi correction:

```text
K_nu(A,s)
  = H^i F_{i nu} + B^{i mu}{}_{nu} F_{mu i}
    - (D_A^{perp *} F^{perp T})_nu.
```

If \(K(A,s)\) is not zero, or is not exactly the divergence of an accepted 4D
stress-energy term, the 14D Yang-Mills/distortion equation does **not** reduce to
the 4D Einstein equation. If it vanishes and the contracted Gauss residual below
has the Einstein form, the reduction can pass this bounded test.

---

## 1. Setup and Notation

Let \(Y=Y^14=Met(X^4)\) carry the gimmel metric \(\mathfrak g\) of signature
(9,5), as in the PC2 and N1 notes. Let

```text
Sigma = s(X^4) subset Y^14
```

be the embedded image of a section. Write:

- \(g=s^*\mathfrak g\), the induced Lorentzian metric on \(X^4\).
- \(e_mu=ds(partial_mu)\), tangent frame along \(\Sigma\).
- \(n_i\), local normal frame, \(i=1,...,10\).
- \(N_s\), the normal bundle of \(\Sigma\) in \(Y\).

From the section-pullback note:

```text
N_s ~= Sym^2 T*X^4.
```

Let \(B=II_s\) be the second fundamental form:

```text
B(e_mu,e_nu) = B^i_{mu nu} n_i,
B in Gamma(Sym^2 T*X^4 tensor N_s).
```

Let \(H\) be the mean-curvature vector:

```text
H^i = g^{mu nu} B^i_{mu nu}.
```

Let \(P -> Y\) be the principal Sp(64)-bundle and \(A\) an Sp(64) connection with
curvature \(F_A\). Its pullback is:

```text
P_s = s*P -> X^4,
a = s*A,
F_a = F_{s*A} = s*F_A.
```

The last identity is exact for any principal connection; it is just naturality of
connection pullback.

The tautological/Levi-Civita part of the Sp(64) connection is denoted \(A^0\): it
is the spin lift of the gimmel Levi-Civita connection through

```text
Spin(9,5) -> Sp(64).
```

For a general Sp(64) connection, write

```text
A = A^0 + Psi,
F_A = F_{A^0} + D_{A^0} Psi + Psi wedge Psi.
```

The term \(D_{A^0}Psi + Psi wedge Psi\) is the genuinely Sp(64) gauge curvature
beyond the tautological spin/Levi-Civita geometry.

**Type convention.** \(B=II_s\) is normal-bundle-valued, while \(theta\) and
\(D_A^*F_A\) are \(ad(P_s)\)-valued. The shorthand \(s*(theta)=B\) only type-checks
after choosing the tautological soldering map

```text
j_s: N_s -> ad(P_s)
```

induced by the off-diagonal \(TX^4 <-> N_s\) block of
\(rho_*: so(9,5) -> sp(64)\). If this map is not part of the chosen Sp(64)
associated-bundle data, the 4D reduction fails at the level of types before any
Einstein-equation comparison begins. In the formulas below, \(B\) may mean
\(j_s(B)\) when it is compared with an adjoint-valued 1-form.

---

## 2. Gauss-Codazzi-Ricci for the Tautological Section

Use the standard convention:

```text
R(U,V)W = nabla_U nabla_V W - nabla_V nabla_U W - nabla_[U,V] W.
```

Changing curvature sign conventions flips all curvature terms consistently but
does not change the residual identified in this note.

### 2.1 Gauss Equation

For tangent vectors \(u,v,w,z in TX^4\):

```text
<R^Y(u,v)w,z>
  = <R^X(u,v)w,z>
    + <B(u,z),B(v,w)> - <B(u,w),B(v,z)>.
```

Equivalently:

```text
R^X_{mu nu rho sigma}
  = R^Y_{mu nu rho sigma}
    - B^i_{mu rho} B_{i nu sigma}
    + B^i_{mu sigma} B_{i nu rho}.
```

This is the precise version of the schematic equation in the prior 4D-reduction
note:

```text
s*(R_gimmel) = R_g + II_s . II_s.
```

### 2.2 Codazzi-Mainardi Equation

For \(u,v,w in TX^4\):

```text
(R^Y(u,v)w)^perp
  = (nabla^perp_u B)(v,w) - (nabla^perp_v B)(u,w).
```

In components:

```text
R^Y_{mu nu rho}{}^i
  = (nabla^perp_mu B)^i_{nu rho}
    - (nabla^perp_nu B)^i_{mu rho}.
```

Contracting \(mu\) and \(rho\) gives the useful form:

```text
(nabla^perp_mu B)^{i mu}{}_{nu} - (nabla^perp_nu H)^i
  = g^{mu rho} R^Y_{mu nu rho}{}^i.
```

This is the first place where the Einstein reduction can fail: if the right-hand
side has an unaccounted normal projection, the divergence of the extrinsic
curvature source is not the divergence expected from a 4D Einstein equation.

### 2.3 Ricci Equation

Let \(S_xi\) be the shape operator for a normal vector \(\xi\), defined by:

```text
g(S_xi u,v) = <B(u,v),xi>.
```

For normal vectors \(\xi,\eta in N_s\):

```text
<R^Y(u,v)xi,eta>
  = <R^perp(u,v)xi,eta> + <[S_xi,S_eta]u,v>.
```

In components:

```text
R^Y_{mu nu i j}
  = R^perp_{mu nu i j}
    + B_{i mu rho} B_j{}^rho{}_{nu}
    - B_{j mu rho} B_i{}^rho{}_{nu}.
```

The Ricci equation controls the curvature of the normal bundle
\(N_s ~= Sym^2 T*X^4\). It matters because the distortion \(s*(theta)\) is being
identified with \(B=II_s\), which is normal-bundle-valued.

---

## 3. Sp(64) Associated-Bundle Form

The previous equations are tangent-bundle equations. For the Sp(64) associated
bundle, the same structure appears after applying the spin representation

```text
rho_*: so(9,5) -> sp(64).
```

Along the section, the tautological connection \(A^0\) has the block form induced
by

```text
TY|_Sigma = TX^4 plus N_s.
```

In an adapted frame:

```text
nabla^Y =
[ nabla^X       -S      ]
[ B             nabla^perp ].
```

Therefore its curvature has the schematic block decomposition:

```text
rho_*(F_{A^0}) =
[ Gauss block       -Codazzi* block ]
[ Codazzi block      Ricci block    ].
```

More explicitly:

```text
rho_*(F_{A^0})_{mu nu}
  =
  [ R^X_{mu nu} - S wedge B        -D B^*_{mu nu}       ]
  [ D B_{mu nu}                    R^perp_{mu nu}+B wedge S ].
```

Equating this with the ambient curvature \(rho_*(R^Y_{mu nu})\) gives exactly
the Gauss, Codazzi, and Ricci equations in Section 2.

For a general Sp(64) connection \(A=A^0+Psi\), define the Sp(64) curvature
residual:

```text
F^Psi = s*(D_{A^0} Psi + Psi wedge Psi).
```

Then the block equations become:

```text
Gauss:    tangent block = R^X + B.B + pr_T(F^Psi)
Codazzi: mixed block   = D^perp B + pr_mixed(F^Psi)
Ricci:   normal block  = R^perp + B.B + pr_N(F^Psi)
```

This is the precise Sp(64) version. The Sp(64) gauge curvature does not break the
standard identities; it adds projected curvature terms to each block.

**Important correction to the earlier schematic language.** For an arbitrary
principal Sp(64) connection, the pullback curvature satisfies

```text
F_a = s*F_A
```

with no \(II_s wedge II_s\) term. The \(II_s wedge II_s\) term appears only after
one identifies the Sp(64) connection with the tautological spin/Levi-Civita
connection, or with an adapted connection whose so(9,5) part is \(A^0\).

---

## 4. Contracted Gauss Equation and the Einstein Tensor

Contracting the Gauss equation gives:

```text
Ric^X_{nu sigma}
  = g^{mu rho} R^Y_{mu nu rho sigma}
    + H_i B^i_{nu sigma}
    - B^i_{nu rho} B_i{}^rho{}_{sigma}.
```

Define the tangential ambient Einstein projection:

```text
G^Y_T{}_{mu nu}
  =
  g^{rho sigma} R^Y_{rho mu sigma nu}
  - (1/2) g_{mu nu}
      g^{alpha beta} g^{rho sigma} R^Y_{rho alpha sigma beta}.
```

Define the extrinsic Gauss stress:

```text
Q_{mu nu}(B)
  =
  H_i B^i_{mu nu}
  - B^i_{mu rho} B_i{}^rho{}_{nu}
  - (1/2) g_{mu nu}
      (H_i H^i - B^i_{rho sigma} B_i{}^{rho sigma}).
```

Then:

```text
G^X_{mu nu}
  = G^Y_T{}_{mu nu} + Q_{mu nu}(B)
```

for the pure tautological connection.

For a general Sp(64) connection \(A=A^0+Psi\), there is an additional contracted
curvature term:

```text
G^X_{mu nu}
  = G^Y_T{}_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu},
```

where

```text
E^Psi_{mu nu}
  = Ricci-contraction of pr_T(F^Psi)
    - (1/2) g_{mu nu} scalar-contraction of pr_T(F^Psi).
```

This is the symmetric 2-tensor part of the Sp(64) curvature residual that lands in
the Lorentz/tangent block after the section is chosen.

---

## 5. The Normal-Flux Correction to the Field Equation

The prior dark-energy note gives the 14D on-shell equation:

```text
theta = D_A^* F_A.
```

The section-pullback note identifies, in the canonical case:

```text
s*(theta) = II_s = B.
```

The missing step is the comparison between the ambient codifferential \(D_A^*F_A\)
and the 4D codifferential \(D_a^*F_a\). They are not equal in general.

Decompose \(F_A\) along the section:

```text
F_{mu nu} = F_A(e_mu,e_nu)      tangent-tangent
F_{mu i}  = F_A(e_mu,n_i)       tangent-normal
F_{ij}    = F_A(n_i,n_j)        normal-normal
```

Then the tangent component of the ambient Yang-Mills divergence is:

```text
s*(D_A^* F_A)_nu
  = (D_a^* F_a)_nu + K_nu(A,s),
```

where the Codazzi/normal-flux correction is:

```text
K_nu(A,s)
  =
  H^i F_{i nu}
  + B^{i mu}{}_{nu} F_{mu i}
  - (D_A^{perp *} F^{perp T})_nu.
```

Here:

```text
(D_A^{perp *} F^{perp T})_nu
  = h^{ij} (nabla^A_{n_i} F_A)(n_j,e_nu)
```

in invariant notation; equivalently it is the normal divergence of the mixed
curvature component \(F_{i nu}\). The first two terms are the mean-curvature and
shape-operator contractions created by taking the ambient divergence in a frame
adapted to the embedded section.

So the pulled-back GU equation is not:

```text
D_a^* F_a = B.
```

It is:

```text
D_a^* F_a + K(A,s) = B.
```

This is the bounded Codazzi result.

---

## 6. Exact Recovery / Failure Condition for 4D Einstein

The 4D Einstein equation has the form:

```text
G^X_{mu nu} = 8 pi G T_{mu nu} + Lambda g_{mu nu}.
```

From the contracted Gauss equation, GU's section pullback can recover this only if:

```text
G^Y_T{}_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}
  = 8 pi G T_{mu nu} + Lambda g_{mu nu}.
```

Equivalently, the failure tensor is:

```text
R_fail_{mu nu}
  =
  G^Y_T{}_{mu nu}
  + Q_{mu nu}(B)
  + E^Psi_{mu nu}
  - 8 pi G T_{mu nu}
  - Lambda g_{mu nu}.
```

The Einstein reduction passes this bounded test iff:

```text
R_fail_{mu nu} = 0
```

and the normal-flux correction \(K(A,s)\) either vanishes or is exactly the 4D
covariant divergence of the stress term being used.

In vacuum with only a cosmological term, the condition is sharper:

```text
tracefree( G^Y_T + Q(B) + E^Psi ) = 0,
trace( G^Y_T + Q(B) + E^Psi ) fixes Lambda.
```

For a totally umbilic section

```text
B^i_{mu nu} = phi^i g_{mu nu},
```

the extrinsic stress is proportional to the metric:

```text
Q_{mu nu}(B) = -3 <phi,phi> g_{mu nu}
```

up to the global sign convention for \(R\). This can play the role of a
cosmological constant. For a generic section, \(Q(B)\) has a nonzero trace-free
part and therefore behaves like anisotropic stress, not like \(\Lambda g\).

---

## 7. Bounded Verdict

**What is established in this note.**

1. The Gauss-Codazzi-Ricci equations for the tautological section are standard and
   have the expected normal bundle \(N_s ~= Sym^2T*X^4\).
2. The Sp(64) version is obtained by embedding the tautological Spin(9,5) connection
   into Sp(64). A general Sp(64) connection contributes projected residual curvature
   terms \(pr_T(F^Psi)\), \(pr_mixed(F^Psi)\), and \(pr_N(F^Psi)\).
3. The precise correction between the 14D field equation and the 4D pulled-back
   equation is the normal-flux/Codazzi term \(K(A,s)\).
4. The precise correction between the contracted Gauss equation and the Einstein
   equation is the failure tensor \(R_fail\).

**What remains open.**

The program still needs an independent computation showing one of:

- \(K(A,s)=0\) and \(R_fail=0\) for the physically selected section; or
- \(K(A,s)\) and \(R_fail\) equal the stress-energy/matter terms produced by the
  spinor and gauge sectors; or
- a concrete counterexample where the trace-free part of
  \(G^Y_T + Q(B) + E^Psi\) is nonzero, in which case the 4D Einstein recovery fails.

This is the exact bounded target for the next computation. The anomaly audit and
IG-dimension notes remove Sp(64) consistency objections; they do not remove this
Codazzi/normal-flux residual.

---

*Filed: 2026-06-23. Task 3 of 5: Codazzi equation for the Sp(64) bundle. Shared
roadmap/status documents intentionally not updated.*
