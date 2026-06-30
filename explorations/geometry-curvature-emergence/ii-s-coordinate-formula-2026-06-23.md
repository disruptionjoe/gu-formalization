---
title: "II_s Coordinate Formula for the Gimmel Metric"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "LOCAL_COORDINATE_FORMULA_CLOSED; CONVENTION_CHOICE_REMAINS"
depends_on:
  - "DERIVATION-PROGRESS.md"
  - "NEXT-STEPS.md"
  - "explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md"
  - "explorations/persona-and-dialectic/4d-reduction-62-persona-steelman-hegelian-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md"
---

# II_s Coordinate Formula for the Gimmel Metric

**Status.** Bounded exploration note. This closes the local-coordinate part of OQ-2 at
formula level. It does not derive the Sp(64) Codazzi equation, the Einstein equation,
or an off-shell proof of `s*(theta) = II_s`.

**Purpose.** Make the second fundamental form of a section

```text
s: X^4 -> Y^14 = Met(X^4),    s(x) = (x, g_{ab}(x))
```

explicit enough that the next Codazzi computation can use fixed symbols rather than
schematic "second derivatives of g" language.

---

## 1. Coordinate Gauge and Gimmel Metric

Work on a local coordinate chart `x^mu` on `X^4`, and use the induced fiber coordinates
`h_{ab} = h_{ba}` on `Y^14`. Indices:

```text
mu,nu,rho,sigma = 0,...,3       base directions
ab,cd,ef                         symmetric fiber-pair directions
```

At a point `(x,h)`, identify

```text
T_(x,h)Y ~= T_x X plus Sym^2(T_x^*X).
```

In this product coordinate gauge, the gimmel metric is block diagonal:

```text
Gcal((u,k),(v,l)) = h(u,v) + V_h(k,l),
```

where `u,v in T_x X`, `k,l in Sym^2(T_x^*X)`, and the trace-reversed Frobenius metric is

```text
V_h(k,l)
  = tr(h^{-1} k h^{-1} l)
    - (1/2) tr(h^{-1} k) tr(h^{-1} l).
```

In components,

```text
Gcal_{mu nu} = h_{mu nu},        Gcal_{mu,ab} = 0,

V_{ab,cd}(h)
  = h^{a(c} h^{d)b} - (1/2) h^{ab} h^{cd},

V^{ab,cd}(h)
  = h_{a(c} h_{d)b} - (1/2) h_{ab} h_{cd},
```

where parentheses mean symmetrization with weight `1/2`, e.g.

```text
h^{a(c} h^{d)b} = (1/2)(h^{ac}h^{db} + h^{ad}h^{cb}).
```

The vertical signature is `(6,4)`, and the horizontal signature is `(3,1)`, so `Gcal` has
signature `(9,5)`, matching the PC2/N1 convention.

**Scope convention.** The formula below is local and uses the coordinate product splitting.
For a global formula, replace ordinary derivatives of `h_{ab}` by derivatives covariant
with respect to the chosen horizontal connection on `Y -> X`.

---

## 2. Ambient Christoffel Symbols

Let `delta^{ab}_{mu nu}` denote the symmetric-pair Kronecker tensor:

```text
delta^{ab}_{mu nu} = (1/2)(delta^a_mu delta^b_nu + delta^a_nu delta^b_mu).
```

The nonzero Levi-Civita symbols of `Gcal` in the coordinate gauge are:

```text
Gamma^rho_{mu,ab}
  = Gamma^rho_{ab,mu}
  = (1/2) h^{rho lambda} delta^{ab}_{mu lambda},
```

```text
Gamma^{ab}_{mu nu}
  = -(1/2) V^{ab,cd} delta^{cd}_{mu nu}
  = -(1/2)( h_{a(mu}h_{nu)b} - (1/2)h_{ab}h_{mu nu} ),
```

and the purely vertical Christoffel symbol, best written operationally, is

```text
Gamma^V_h(k,l)_{ab}
  = -(1/2)( k_{ar} h^{rs} l_{sb} + l_{ar} h^{rs} k_{sb} ).
```

Equivalently, for the coordinate basis tensors `E_cd` and `E_ef`,

```text
Gamma^{ab}_{cd,ef}
  = -(1/2)( (E_cd)_{ar} h^{rs} (E_ef)_{sb}
           +(E_ef)_{ar} h^{rs} (E_cd)_{sb} ).
```

All other symbols vanish in this coordinate gauge:

```text
Gamma^rho_{mu nu} = 0,
Gamma^rho_{ab,cd} = 0,
Gamma^{ab}_{mu,cd} = 0.
```

Coordinate-free mnemonic:

```text
Gamma^H(u,k) = (1/2) h^{-1}( k(u,-) ),

Gamma^V(u,v) = -(1/2)( u^flat_h sym v^flat_h - (1/2)h(u,v)h ),

Gamma^V(k,l) = -(1/2)( k h^{-1} l + l h^{-1} k ).
```

Here `sym` is the symmetric product with weight `1/2`.

**Derivation check.** The vertical connection formula follows from Koszul's formula on the
open fiber of nondegenerate metrics. For constant vertical tensors `k,l,m`,

```text
2 V_h(Gamma^V(k,l),m)
  = d_k V(l,m) + d_l V(k,m) - d_m V(k,l),
```

using `d_k(h^{-1}) = -h^{-1} k h^{-1}`. The trace-reversal term cancels in dimension four,
in the inverse metric and leaves the same affine-invariant connection rule
`Gamma^V(k,l) = -1/2(kh^{-1}l + lh^{-1}k)`.

---

## 3. Graph Section Data

For the graph section `s(x) = (x,g_{ab}(x))`, define

```text
g_mu := partial_mu g        in Sym^2(T^*X),
g_{mu nu}^{(2)} := partial_mu partial_nu g.
```

The tangent basis of the graph is

```text
T_mu = ds(partial_mu)
     = partial_mu + (partial_mu g_{ab}) partial/partial h_{ab}.
```

The metric induced from the literal graph immersion is

```text
gbar_{mu nu}
  = Gcal(T_mu,T_nu)
  = g_{mu nu} + V_g(g_mu,g_nu),
```

and its Christoffel symbols are

```text
gbar_Gamma^lambda_{mu nu}
  = (1/2) gbar^{lambda kappa}
      (partial_mu gbar_{nu kappa}
       + partial_nu gbar_{mu kappa}
       - partial_kappa gbar_{mu nu}).
```

**Important convention flag.** Older 4D-reduction notes often write `s*(Gcal)=g`. That is
true only after projecting to the horizontal part, or after choosing a horizontal connection
for which the section has zero vertical slope. For the literal graph immersion, the induced
metric is `gbar = g + V_g(partial g, partial g)`.

---

## 4. Second Fundamental Form

For an immersion, the second fundamental form is

```text
II_s(T_mu,T_nu)
  = nabla^Gcal_{T_mu} T_nu - ds(nabla^gbar_{partial_mu} partial_nu).
```

In components,

```text
II_s(T_mu,T_nu)
  = B^rho_{mu nu} partial_rho
    + B_{mu nu,ab} partial/partial h_{ab},
```

with horizontal component

```text
B^rho_{mu nu}
  = (1/2) g^{rho lambda}
      ( (partial_mu g)_{nu lambda}
       +(partial_nu g)_{mu lambda} )
    - gbar_Gamma^rho_{mu nu},
```

and vertical component

```text
B_{mu nu,ab}
  = partial_mu partial_nu g_{ab}
    - gbar_Gamma^lambda_{mu nu} partial_lambda g_{ab}

    - (1/2)( g_{a(mu}g_{nu)b} - (1/2)g_{ab}g_{mu nu} )

    - (1/2)(
        (partial_mu g)_{ar} g^{rs} (partial_nu g)_{sb}
       +(partial_nu g)_{ar} g^{rs} (partial_mu g)_{sb}
      ).
```

Equivalently, using symmetric product notation,

```text
B^V_{mu nu}
  = partial_mu partial_nu g
    - gbar_Gamma^lambda_{mu nu} partial_lambda g
    - (1/2)( e_mu^flat sym e_nu^flat - (1/2)g_{mu nu}g )
    - (1/2)( g_mu g^{-1} g_nu + g_nu g^{-1} g_mu ).
```

This is the explicit coordinate formula needed for later Codazzi work.

The first line is the graph Hessian term. The second line is the algebraic contribution
from the horizontal metric `Gcal_{mu nu}=h_{mu nu}` depending on the fiber coordinate. The
third line is the fiber-geometry contribution from the trace-reversed Frobenius metric.

---

## 5. Normal-Bundle Representative

The vector `B^rho partial_rho + B_{ab} partial_{h_ab}` is normal by construction when
`gbar_Gamma` is the Levi-Civita connection of `gbar`. Because the graph tangent has vertical
slope, the normal vector is not generally purely vertical in these coordinates.

A useful identification of the normal bundle with `Sym^2 T^*X` is:

```text
q in Sym^2 T^*X
  |-> N(q) = q^V - g^{rho mu} V_g(q,g_mu) partial_rho.
```

This satisfies `Gcal(N(q),T_mu)=0`. Under this identification, `B^V_{mu nu}` is the vertical
representative of `II_s`:

```text
II_s(T_mu,T_nu) = N(B^V_{mu nu}).
```

So Codazzi can be written either in full ambient components `(B^rho,B^V)` or in the vertical
representative `B^V`, with the normal connection induced by the lift `N`.

---

## 6. Immediate Consequences and Checks

### 6.1 Constant sections are not automatically totally geodesic

If `partial g = 0` in this local trivialization, then

```text
B^V_{mu nu,ab}
  = -(1/2)( g_{a(mu}g_{nu)b} - (1/2)g_{ab}g_{mu nu} ).
```

Thus a constant metric slice is not totally geodesic for the literal gimmel metric. This is
not an algebra error: it comes from `partial_{h_ab} Gcal_{mu nu} != 0`. If the intended GU
normalization requires flat spacetime to have `II_s=0`, the later formalism must either:

```text
(a) use a horizontal-projected pullback rather than the literal graph immersion, or
(b) subtract this canonical algebraic slice curvature as a reference term.
```

This point should be fixed before interpreting `II_s` numerically as dark energy.

### 6.2 Small-slope expansion

When `V_g(partial g,partial g)` is treated as second order, `gbar_Gamma` may be replaced
to first order by the Levi-Civita symbols `Gamma(g)`. In the covariantized version of the
graph-Hessian term, this gives

```text
B^V_{mu nu,ab}
  = nabla^g_mu nabla^g_nu g_{ab}
    - (1/2)( g_{a(mu}g_{nu)b} - (1/2)g_{ab}g_{mu nu} )
    + O((partial g)^2).
```

Since `nabla^g g = 0`, this expansion collapses to the algebraic slice-curvature term plus
quadratic slope corrections if the same metric `g` is used for the base connection. This
again signals that the literal graph formula and the "LC-compatible horizontal section"
convention are not the same object.

### 6.3 Codazzi input

For the next Codazzi calculation, the stable inputs are:

```text
normal representative:  B^V_{mu nu,ab}
normal lift:            N(q) = q^V - g^{rho mu}V_g(q,g_mu) partial_rho
ambient symbols:        Gamma^rho_{mu,ab}, Gamma^{ab}_{mu nu}, Gamma^{ab}_{cd,ef}
induced metric:         gbar_{mu nu} = g_{mu nu} + V_g(g_mu,g_nu)
```

The Codazzi tensor should be computed as

```text
(nabla^perp_mu B^V_{nu sigma}
 -nabla^perp_nu B^V_{mu sigma})
 - (R^Gcal(T_mu,T_nu)T_sigma)^perp,
```

where `nabla^perp` is the normal connection induced by `N`. The formula above supplies the
Christoffel data needed to compute both terms.

---

## 7. Relationship to Distortion

DD1 establishes that GU's distortion `theta` is not generic torsion; it is a gauge-equivariant
connection-difference object on the 14D bundle. The 4D reduction notes use the reconstruction
claim

```text
s*(theta) = II_s
```

in the canonical case `A = nabla_Gcal`.

This note sharpens the right-hand side. Under the literal graph convention, the object
identified with `s*(theta)` is not simply "second derivatives of the metric"; it is the
normal-valued tensor with vertical representative

```text
B^V = Hessian_graph(g)
      + algebraic horizontal-slice term
      + vertical Frobenius-connection quadratic term.
```

Whether GU intends this literal object or a horizontally normalized variant is now a precise
choice rather than a schematic ambiguity.

---

## 8. Closure Condition

OQ-2 should count as locally closed, at exploration grade, once downstream work chooses one
of the two conventions:

```text
Literal graph convention:
  use gbar, B^V, and N exactly as above.

Horizontal-normalized convention:
  replace partial_mu g by D_mu g for the chosen horizontal connection and specify whether
  the algebraic slice-curvature term is retained or subtracted.
```

The Codazzi computation should state this convention explicitly before any physical
interpretation of `II_s` as dark energy, torsion, or the source term in the pulled-back
field equation.
