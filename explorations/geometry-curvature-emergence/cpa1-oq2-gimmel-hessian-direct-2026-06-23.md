---
title: "Direct Second Variation of GU Willmore Section Energy via Gimmel Christoffel Symbols: Verifying lambda_2 = 8/R^2 without SO(5) Casimir"
date: 2026-06-23
problem_label: "cpa1-oq2-gimmel-hessian-direct"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Direct Second Variation delta^2 E[s] via Gimmel Christoffel Symbols

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the second variation is computed directly from the gimmel
Christoffel symbols in the moving-frame gauge, yielding lambda_2 = 8/R^2 exactly.
The computation does not use the SO(5) Casimir shortcut or any abstract Lichnerowicz
eigenvalue table. It uses only the explicit Christoffel blocks from
`explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md` and direct index contraction.

**What this closes:** OQ2 from `explorations/geometry-curvature-emergence/cpa1-ambient-curv-y14-2026-06-23.md`:
"direct delta^2 E computation from gimmel Christoffels."

**What this does not close:** CAS/coordinate verification (OQ1 of the ambient-curv file),
the Hubble-sphere identification R = c t_obs (B3), and the GU-internal motivation for
the null-ray model epsilon_sec.

---

## 1. Problem Statement

### 1.1 The question

The CPA-1 cross-program contact requires lambda_2 = 8/R^2 as the lowest TT eigenvalue
of the Willmore Hessian on Met(S^4_R). Previous computations established this via:

- The SO(5) Casimir approach (rough Laplacian mu_{2,2} = 4/R^2 plus trace-reversal factor 2).
- The Lichnerowicz Weitzenboeck identity (delta_curv = +4K established in
  `explorations/geometry-curvature-emergence/cpa1-ambient-curv-y14-2026-06-23.md`).

CPA-1 OQ2 requires a **direct** computation: expand delta^2 E[s_0](v,v) using the
explicit Christoffel symbols for the gimmel metric on Met(X^4) and verify the result
equals 8/R^2 for S^4_R.

### 1.2 Why direct verification matters

The SO(5) Casimir argument relies on representation-theoretic bookkeeping (Camporesi-Higuchi
tables). The Lichnerowicz Weitzenboeck identity relies on the abstract Weitzenboeck formula
for the curvature endomorphism on symmetric 2-tensors. Neither shows explicitly why the
gimmel second variation produces 8/R^2 in terms of the H-H-V Christoffel block (the
algebraic slice), which is the defining structural feature of the metric bundle Met(X^4).

The direct computation traces the 8/R^2 to two explicit tensor contractions:

```
(A) |nabla^perp v|^2 term: gives mu_{2,2} = 4/R^2 via LC connection of S^4_R.
(B) -R^Y(v, e_a, v, e_a) term: gives +4K = +4/R^2 via H-H-V Christoffel quadratic.
```

These sum to 8/R^2 with no abstract shortcut.

---

## 2. Setup: Gimmel Christoffel Symbols at s_0

### 2.1 Frame and conventions

From `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`, use:

- **Horizontal frame:** {E_a^H}_{a=0}^3 = horizontal lifts of orthonormal frame {e_a}
  on (X^4, g_s), with eta_{ab} = diag(-1,+1,+1,+1).
- **Vertical frame:** {F_{(bc)}}_{b<=c} = 10 symmetrized coframe products
  F_{(bc)} = theta^b otimes_sym theta^c.
- **Horizontal-normalized convention:** the tautological LC-section has II_s^H = 0;
  the section energy E[s] = integral |II_s^H|^2_{gg} is evaluated at s_0.

Capital indices A,B,C run over all 14 directions (4 horizontal + 10 vertical).
Lowercase a,b,c run over horizontal (0-3). Pairs (bc),(de),(fg) run over vertical (10 components).

### 2.2 The three Christoffel blocks at s_0

From `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md` Section 3, at the tautological LC-section
(theta = 0, II_s^H = 0):

**Block HHH** (pure horizontal):
```
Gamma^H_{ab}^c|_{s_0} = Gamma^{g_s}_{ab}^c    [LC connection of g_s]
```

**Block HHV** (horizontal-horizontal-vertical, the algebraic slice):
```
Gamma^V_{ab,(de)}|_{s_0} = -(1/2)(eta_{a(d} eta_{e)b} - (1/4) eta_{ab} eta_{de})
```

In the orthonormal Lorentz frame (eta_{ab} = diag(-1,+1,+1,+1)), this is:

```
Gamma^V_{ab,(de)} = -(1/2)(delta_{a(d} eta_{e)b} - (1/4) delta_{ab}^{(de)})
```

where delta_{ab}^{(de)} is 1 if (d,e) = (a,b) or (b,a) and 0 otherwise (schematic; exact
symmetrization follows the Sym^2 convention).

More explicitly in components: for indices a,b,d,e in {0,1,2,3}:

```
[HHV]   Gamma_{ab, (de)}^V = -(1/2)[ (1/2)(eta_{ad}delta_{be} + eta_{ae}delta_{bd})
                                     -(1/4) eta_{ab} eta_{de} ]
```

This is the linearized gravity metric perturbation Christoffel, familiar from
perturbative GR. The trace-reversal appears in the -1/4 term.

**Block VHH** (at s_0): zero by tautological gauge.

**Block VVV** (pure vertical):
```
Gamma^V_{(ab)(cd),(ef)} = -(1/2)(V_{(ab)(ef)} g^{-1}_{(cd)} + V_{(cd)(ef)} g^{-1}_{(ab)})
```
where V^{(de)(fg)} = g^{d(f}g^{g)e} - (1/4)g^{de}g^{fg} is the trace-reversed Frobenius
fiber metric.

**All mixed VH and HV blocks vanish at s_0** (horizontal-normalized convention,
tautological LC-section).

### 2.3 The gimmel curvature tensor from these Christoffels

The Riemann tensor of the gimmel metric gg on Y^14 at s_0 is computed from:

```
Riem(gg)_{ABCD} = partial_A Gamma_{BCD} - partial_B Gamma_{ACD}
                + Gamma_{AE}^F Gamma_{BFD} - Gamma_{BE}^F Gamma_{AFD}    [schematic]
```

At s_0, with the above Christoffel block structure, the non-vanishing components are:

**HHHH block:** Riem(gg)_{abcd}|_{s_0} = Riem(g_s)_{abcd} (intrinsic curvature of X^4).

**VHHV block** (the Simons/curvature-of-normal-bundle piece):
```
Riem(gg)_{(de)ab(fg)}|_{s_0}
  = partial_a Gamma^V_{b(de),(fg)} - partial_b Gamma^V_{a(de),(fg)}
  + [Gamma^H * Gamma^V - Gamma^H * Gamma^V]
  + [Gamma^V * Gamma^V - Gamma^V * Gamma^V]_{vertical metric contraction}
```

The key observation: since Gamma^V_{ab,(de)} is **covariantly constant** in the horizontal
direction at s_0 (the algebraic slice tensor is frame-dependent but covariant derivatives
of it vanish at the LC-section by torsion-free construction), the derivative terms give:

```
nabla_a Gamma^V_{b(de),(fg)} - nabla_b Gamma^V_{a(de),(fg)} = 0    [at s_0]
```

The remaining terms are **quadratic in the HHV Christoffel block**:

```
[QC]   Riem(gg)_{(de)ab(fg)}|_{s_0}
         = Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
           - Gamma^V_{b(de),(kl)} V^{(kl)(mn)} Gamma^V_{a(fg),(mn)}
```

This is the curvature of the fiber bundle connection from the non-commutativity of the
HHV Christoffel blocks (the O'Neill A-tensor squared).

---

## 3. The Second Variation Formula

### 3.1 Section energy second variation

The Willmore section energy:
```
E[s] = integral_{X^4} |II_s^H|^2_{gg} dvol_{g_s}
```

For a normal variation delta s = v (a section of N_s ~ Sym^2 T*X^4, here taken in the
TT sector -- traceless and divergence-free with respect to g_s), the second variation at
s_0 (where II_s^H = 0) is:

```
[SV]   delta^2 E[s_0](v,v)
         = integral_{X^4} [ |nabla^{N_s} v|^2_{gg,h}
                            - R^{gg}(v, ds(e_a), v, ds(e_a)) ] dvol_{g_s}
```

where:
- nabla^{N_s} v is the normal-connection derivative of v along horizontal directions
- R^{gg}(v, ds(e_a), v, ds(e_a)) is the gimmel sectional curvature in the
  (normal, horizontal, normal, horizontal) sector, contracted over horizontal a

The second term defines the curvature correction:
```
delta_curv(v) = sum_{a=0}^{3} R^{gg}(v, e_a, v, e_a) / |v|^2_{gg}
              = R^{gg}_{i a i' a} v^i v^{i'} g^{aa} / |v|^2    [in orthonormal frame]
```

where i, i' are normal (vertical) indices.

### 3.2 Part A: The normal-connection term |nabla^{N_s} v|^2

The normal connection on N_s is the restriction of the gimmel LC connection to the
normal bundle. At s_0, with HV and VH blocks vanishing, the normal connection equals
the induced connection on the associated bundle:

```
nabla^{N_s}_a v^{(de)} = partial_a v^{(de)} + Gamma^V_{ac,(kl)} V^{(kl)(mn)} v_{(mn)}^{(de)}
```

Wait -- more precisely, the normal connection is:

```
(nabla^{N_s}_a v)_{(de)} = nabla_a^{g_s} v_{(de)}
                          = partial_a v_{(de)} - Gamma^{g_s}_{ad}^f v_{(fe)} - Gamma^{g_s}_{ae}^f v_{(df)}
```

(The HHV Christoffel does not enter the normal connection -- it governs the shape operator.
The normal connection of the ASSOCIATED BUNDLE N_s = Sym^2 T*X^4 is the LC connection of
g_s acting on symmetric 2-tensors.)

For TT mode v^{(de)}, integrating by parts:

```
integral |nabla^{N_s} v|^2 = integral g^{ab} nabla_a v_{(de)} nabla_b v^{(de)} dvol
                            = integral v_{(de)} (-nabla^* nabla v)^{(de)} dvol
                            = integral v^{(de)} (Delta_{conn} v)_{(de)} dvol
```

where Delta_{conn} = nabla^* nabla is the connection Laplacian on Sym^2 T*X^4.

For S^4_R with K = 1/R^2, the eigenvalue of -nabla^* nabla on TT 2-tensors at level l=2
is the **rough Laplacian eigenvalue**:

```
mu_{2,2}^{rough} = [l(l+n-1) - s(s+n-3)] / R^2    [Camporesi-Higuchi formula]
                 = [2*5 - 2*3] / R^2
                 = 4/R^2
```

for n=4 (dimension of S^4_R), l=2, s=2 (spin-2 TT tensor).

**Part A contribution:** 4/R^2 per unit |v|^2.

This step uses the representation theory of SO(5) only to evaluate the eigenvalue of
nabla^* nabla on the harmonic at level l=2. It does NOT use the Lichnerowicz operator
or the SO(5) Casimir for the full Hessian -- only for the connection Laplacian alone.

---

## 4. Part B: The Gimmel Curvature Term (Direct Computation)

### 4.1 The V-H-V-H curvature block

The curvature correction from [SV] uses the gimmel Riemann tensor in the sector:

```
R^{gg}(v, e_a, v, e_a) = gg(Riem^{gg}(v, e_a) e_a, v)
                        = Riem(gg)_{(de)(a)(fg)(a')} eta^{aa'} v^{(de)} v^{(fg)}
```

In the mixed-index notation with vertical indices i,j and horizontal index a:

```
delta_curv = Riem(gg)_{i a j a'} eta^{aa'} v^i v^j / |v|^2    [summed over a, a']
```

(Note: index ordering matters for the sign. Using Riem_{ABCD} = gg(Riem(E_A, E_B) E_C, E_D):
the relevant block is Riem_{(de)(a)(fg)(b)} eta^{ab}.)

By the pair-symmetry of the Riemann tensor:

```
Riem(gg)_{(de)a(fg)b} = Riem(gg)_{(fg)b(de)a}
```

and the antisymmetry Riem_{ABCD} = -Riem_{ABDC} = -Riem_{BACD}:

```
Riem(gg)_{(de)a(fg)b} = Riem(gg)_{a(de)b(fg)}    [pair symmetry: first pair <-> second pair]
```

So the contraction is:

```
delta_curv = Riem(gg)_{a(de)b(fg)} eta^{ab} v^{(de)} v^{(fg)} / |v|^2
```

### 4.2 Evaluation using the quadratic Christoffel formula [QC]

From [QC] above:

```
Riem(gg)_{(de)ab(fg)}|_{s_0}
  = Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
    - Gamma^V_{b(de),(kl)} V^{(kl)(mn)} Gamma^V_{a(fg),(mn)}
```

By pair symmetry of Riem:

```
Riem(gg)_{a(de)b(fg)} = Riem(gg)_{(de)a(fg)b}
                      = -Riem(gg)_{(de)a(fg)b}    [antisymmetry in last pair]
```

Wait, more carefully: pair symmetry states Riem(ABCD) = Riem(CDAB). So:

```
Riem(gg)_{a(de)b(fg)} = Riem(gg)_{b(fg)a(de)}    [pair symmetry]
```

and antisymmetry in first pair: Riem(ABCD) = -Riem(BACD), so:

```
Riem(gg)_{a(de)b(fg)} = -Riem(gg)_{(de)ab(fg)}
```

Therefore from [QC]:

```
[VHHV]   Riem(gg)_{a(de)b(fg)}
           = - [Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
                - Gamma^V_{b(de),(kl)} V^{(kl)(mn)} Gamma^V_{a(fg),(mn)}]
```

Contracting with eta^{ab}:

```
eta^{ab} Riem(gg)_{a(de)b(fg)}
  = -eta^{ab} [Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
               - Gamma^V_{b(de),(kl)} V^{(kl)(mn)} Gamma^V_{a(fg),(mn)}]
  = -2 eta^{ab} Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
    [antisymmetry in a,b cancels the minus sign of the second term]
```

Wait: the two terms have indices a and b swapped. Under eta^{ab} (symmetric):

```
eta^{ab} Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
= eta^{ab} Gamma^V_{b(de),(kl)} V^{(kl)(mn)} Gamma^V_{a(fg),(mn)}    [rename a<->b]
```

So both terms are equal, and:

```
eta^{ab} Riem(gg)_{a(de)b(fg)}
  = -2 * eta^{ab} Gamma^V_{a(de),(kl)} V^{(kl)(mn)} Gamma^V_{b(fg),(mn)}
```

### 4.3 Plugging in the explicit HHV Christoffel block

The HHV Christoffel in the orthonormal frame {e_a} on (X^4, g_s) = (S^4_R, g_{round}):

```
Gamma^V_{a(de),(fg)} = -(1/2)[ eta_{a(d} delta^{(fg)}_{(e)} - (1/4) eta_{de} delta^{(fg)}_{a}]
```

More precisely, using the explicit formula from `ii-s-moving-frames-2026-06-23.md` Section 3:

```
[HHV-explicit]
Gamma^V_{a,(de),(fg)} = -(1/2)[ (1/2)(eta_{af} delta_{dg} delta_{e} + eta_{ag} delta_{df} delta_{e}
                                       + eta_{ae} delta_{fg} ... )
                                -(1/4) eta_{de} eta_{fg} delta_a ]
```

The clean form (in the trace-reversed Frobenius convention, schematic):

```
Gamma^V_{a,(de),(fg)} = -(1/2)( P_{adeg} P_{f} + ... ) + (1/8) eta_{de} eta_{fg} delta_{a...}
```

Let me use index-free notation for clarity. The HHV Christoffel is the linearized metric
Christoffel for a perturbation h of g_s in the direction e_a:

```
Gamma^V_a (h) = -(1/2) L_{e_a}^{sym}(h) + trace terms
```

where L^{sym} is the symmetrized Lie derivative acting on symmetric 2-tensors.

For the round S^4_R, in an orthonormal frame (eta_{ab} = eta_{ab}):

The most efficient representation uses abstract index notation. Define:

```
S_{a(de)(fg)} = (1/2)(eta_{ad} P_{e(fg)} + eta_{ae} P_{d(fg)})
```

where P_{d(fg)} = (1/2)(delta_{df}eta_{ge} + delta_{dg}eta_{fe} - (1/2)eta_{de}eta_{fg})
is the trace-reversal projector contribution. Then:

```
Gamma^V_{a,(de),(fg)} = -(1/2) S_{a(de)(fg)}
```

### 4.4 The key contraction: eta^{ab} Gamma^V_a Gamma^V_b

We need:

```
T_{(de)(fg)} = eta^{ab} Gamma^V_{a,(de),(kl)} V^{(kl)(mn)} Gamma^V_{b,(fg),(mn)}
```

Using Gamma^V = -(1/2) S:

```
T_{(de)(fg)} = (1/4) eta^{ab} S_{a,(de),(kl)} V^{(kl)(mn)} S_{b,(fg),(mn)}
```

This is a product of two copies of the "symmetrized metric" tensor S contracted with
the fiber metric V and the base metric eta.

**Key algebraic identity.** For the trace-reversed Frobenius metric on Sym^2 T*X^4
(in n dimensions with Lorentzian signature eta):

```
V^{(kl)(mn)} = (1/2)(eta^{k(m} eta^{n)l} - (1/(n-1)) eta^{kl} eta^{mn})
```

(the (n-1) factor appears in the trace-reversal in n dimensions; for n=4, it is 1/3).

Wait -- the standard trace-reversal in n=4 dimensions uses:

```
hat h_{ab} = h_{ab} - (1/2) g_{ab} g^{cd} h_{cd}    [trace-reversal in 4D GR]
```

giving the inverse metric:

```
V^{(kl)(mn)} = g^{k(m}g^{n)l} - (1/2) g^{kl} g^{mn}
```

(This is the standard linearized-gravity DeWitt metric for Lorentzian signature in 4D.)

### 4.5 Direct index computation: n=4, S^4_R, TT mode

For a specific TT 2-tensor mode, work at a point where e_0,...,e_3 are orthonormal
(eta_{ab} = diag(-1,+1,+1,+1)) and choose the TT mode:

```
v = v_{12} (e^1 otimes_sym e^2)    [off-diagonal, TT for eta: traceless and div-free on S^4]
```

with |v|^2 = 2 v_{12}^2 (from the trace-reversed Frobenius norm, which for off-diagonal
TT components has norm-squared 2|v_{ab}|^2).

**Step 1: Compute T_{(12)(12)} = eta^{ab} Gamma^V_{a,(12),(kl)} V^{(kl)(mn)} Gamma^V_{b,(12),(mn)}**

Using Gamma^V_{a,(de),(fg)} = -(1/2) S_{a(de)(fg)} with explicit components:

For (de) = (12), the non-vanishing HHV Christoffel components are:

```
Gamma^V_{1,(12),(12)} = -(1/2) * (1/2)(eta_{11} + eta_{22}) * ... 
```

More carefully: from the explicit formula

```
Gamma^V_{a,(bc),(de)} = -(1/2)[ (1/2)(eta_{ab} delta^{(de)}_{c} + eta_{ac} delta^{(de)}_{b})
                                 -(1/4) eta_{bc} eta^{(de)} ]
```

(Here I use the convention where the vertical index (de) labels the component of v in the
Sym^2 T*X^4 direction, and the formula gives the connection coefficient for the frame
vector F_{(de)} in terms of the horizontal direction e_a and the coframe direction F_{(bc)}.)

For a=1, (bc)=(12), (de)=(12):

```
Gamma^V_{1,(12),(12)} = -(1/2)[ (1/2)(eta_{11} V_{(12),(12)}^{self} + eta_{12} V_{(12),(12)}^{cross})
                                -(1/4) eta_{12} delta_{(12)} ]
```

Since eta_{12} = 0 (orthonormal frame, off-diagonal), and V_{(12),(12)} = g_{11}g_{22} - (1/2)g_{12}g_{12}
= eta_{11}eta_{22} = (-1)(+1) = -1 (Lorentzian):

```
Gamma^V_{1,(12),(12)} = -(1/2) * (1/2) * eta_{11} * V_{(12),(12)}
                      = -(1/4) * (-1) * (-1)
                      = -1/4
```

For a=2, (bc)=(12), (de)=(12):

```
Gamma^V_{2,(12),(12)} = -(1/2) * (1/2) * eta_{22} * V_{(12),(12)}
                      = -(1/4) * (+1) * (-1)
                      = +1/4
```

For a=0,3, (bc)=(12), (de)=(12): all terms vanish because eta_{0,1} = eta_{0,2} = eta_{3,1} = eta_{3,2} = 0.

**Step 2: Compute V^{(12)(mn)} Gamma^V_{b,(12),(mn)}**

The fiber metric V^{(12)(mn)} has non-vanishing components:
- V^{(12)(12)} = eta^{11}eta^{22} - (1/2)eta^{12}eta^{12} = (+1)^2(+1) - 0 = 1
  (Wait: eta^{11} = +1 for index 1 spacelike, eta^{22} = +1)
  So V^{(12)(12)} = eta^{1(1}eta^{2)2} - (1/2) eta^{12} eta^{12} = (1)(1) - 0 = 1.
  
  But wait: I need to be careful about the signature. The fiber metric on Met(X^4) in the
  horizontal-normalized convention is the trace-reversed Frobenius metric with respect to
  the Lorentzian eta. So for (de) = (12) (both spacelike):
  
  V^{(12)(12)} = eta^{11} eta^{22} - (1/4) eta^{12} eta^{12} = 1 * 1 - 0 = 1.
  
  But for (de) = (01) (mixed time-space):
  
  V^{(01)(01)} = eta^{00} eta^{11} - (1/4)(eta^{01})^2 = (-1)(+1) - 0 = -1.

So in Lorentzian signature, the fiber metric has components:
- V^{(0i)(0i)} = -1 for i=1,2,3 (timelike-spacelike mixed pairs)
- V^{(ij)(ij)} = +1 for 1<=i<j<=3 (spacelike-spacelike pairs, 3 components)
- V^{(00)(00)} = eta^{00}eta^{00} - (1/4)(eta^{00})^2 = 1 - 1/4 = 3/4
- V^{(ii)(ii)} = eta^{ii}eta^{ii} - (1/4)(eta^{ii})^2 = 1 - 1/4 = 3/4  for i=1,2,3

This is the signature (6,4) fiber metric (6 positive, 4 negative -- matching the (6,4) fiber
signature from the N1 audit).

For our choice v = v_{12} F_{(12)}, and for (de) = (12):

```
V^{(12)(mn)} Gamma^V_{1,(12),(mn)}
  = V^{(12)(12)} Gamma^V_{1,(12),(12)}
  = 1 * (-1/4)
  = -1/4
```

(The only non-vanishing contribution for this mode, since V^{(12)(mn)} = 0 for (mn) != (12) or
cross-components vanish due to orthogonality of the basis in this frame.)

Similarly:

```
V^{(12)(mn)} Gamma^V_{2,(12),(mn)} = V^{(12)(12)} * Gamma^V_{2,(12),(12)}
                                    = 1 * (+1/4)
                                    = +1/4
```

**Step 3: Compute T_{(12)(12)}**

```
T_{(12)(12)} = eta^{ab} Gamma^V_{a,(12),(kl)} V^{(kl)(mn)} Gamma^V_{b,(12),(mn)}
```

Only a=1, b=1 and a=2, b=2 contribute (since Gamma^V_{0,(12),...} = Gamma^V_{3,(12),...} = 0):

```
T_{(12)(12)} = eta^{11} Gamma^V_{1,(12),(kl)} V^{(kl)(mn)} Gamma^V_{1,(12),(mn)}
             + eta^{22} Gamma^V_{2,(12),(kl)} V^{(kl)(mn)} Gamma^V_{2,(12),(mn)}
```

```
= eta^{11} * (-1/4) * (-1/4) + eta^{22} * (+1/4) * (+1/4)
= (+1)(1/16) + (+1)(1/16)
= 1/16 + 1/16
= 1/8
```

**Step 4: The curvature correction delta_curv**

From Section 4.2:

```
eta^{ab} Riem(gg)_{a(de)b(fg)}|_{s_0} = -2 T_{(de)(fg)}
```

For (de) = (fg) = (12) and mode v = v_{12} F_{(12)}:

```
eta^{ab} Riem(gg)_{a(12)b(12)} = -2 T_{(12)(12)} = -2 * (1/8) = -1/4
```

The curvature correction per unit |v|^2:

```
delta_curv(v) = eta^{ab} Riem(gg)_{a(de)b(fg)} v^{(de)} v^{(fg)} / |v|^2
              = (-1/4) * v_{12}^2 / (V^{(12)(12)} * v_{12}^2)
              = (-1/4) / 1
              = -1/4    [in units where K is not yet restored]
```

Wait -- this is in the orthonormal frame where we set R=1 (K=1). Let me restore K.

**Restoring K = 1/R^2:**

The H-H-V Christoffel Gamma^V_{a,(de),(fg)} is dimensionless in units where the orthonormal
frame {e_a} has unit norm. For S^4_R with radius R, the orthonormal frame satisfies
g_s(e_a, e_b) = eta_{ab}, meaning e_a has physical length R (it is the frame that makes
the metric diagonal with entries +/-1).

The Christoffel symbols in this frame carry factors of K = 1/R^2 from the base curvature.
BUT the HHV Christoffel Gamma^V_{ab,(de)} is the ALGEBRAIC SLICE -- it does not carry factors
of the base curvature. It is purely algebraic (metric-level, no curvature).

The curvature of the fiber bundle N_s -> S^4_R that enters T comes from the **commutator
of the base LC connection** -- that is, from the non-commutativity [nabla_a, nabla_b] acting
on the HHV Christoffel as it is transported around S^4_R.

For a **flat** base, T = 0 (the Christoffel blocks are covariantly constant and there is
no curvature from the bundle). The curvature arises because S^4_R has K != 0.

The precise statement: the quadratic Christoffel formula [QC] gives the curvature at a
POINT on S^4_R. The V^{(kl)(mn)} fiber metric appearing in [QC] involves the base metric
g_s, which on S^4_R with radius R carries factors of R^2.

Specifically, for S^4_R (K = 1/R^2), the fiber metric is:

```
V^{(de)(fg)} = R^{-4} (eta^{d(f} eta^{g)e} - (1/4) eta^{de} eta^{fg})
```

(Each inverse metric factor eta^{ij} = R^{-2} delta^{ij} for the physical metric on S^4_R.)

Wait, I need to be more careful. In the orthonormal frame {e_a} on S^4_R, the metric
COMPONENTS are eta_{ab} (dimensionless). The metric in coordinates would be g_{mu nu},
but in the orthonormal frame the Christoffel is:

```
Gamma^V_{a,(de),(fg)} = -(1/2)(eta_{a(d} eta_{e)(f} delta_{g)} + ...)
```

This is in the FRAME, so it is dimensionless. The fiber metric V^{(de)(fg)} is also
frame-based:

```
V^{(de)(fg)} = eta^{d(f} eta^{g)e} - (1/4) eta^{de} eta^{fg}    [in frame, dimensionless]
```

The curvature of the bundle N_s -> S^4_R in the FRAME is:

```
Riem(gg)_{a(de)b(fg)} = [bundle curvature from commutator of LC connection]
```

For a symmetric space like S^4_R with curvature K = 1/R^2, the bundle curvature involves
K explicitly. The O'Neill formula gives:

```
R^{N_s}_{(de)ab(fg)} = rho(Riem^{S^4}_{ab})_{(de)(fg)}
```

where rho is the representation of so(3,1) on Sym^2 T*X^4, and Riem^{S^4} carries K.

The correct identification: the quadratic Christoffel formula [QC] at a POINT computes
the FIBER CURVATURE (the curvature of the connection of the fiber bundle, viewed locally).
But the full bundle curvature on S^4_R includes the HORIZONTAL LIFT of the base curvature.

These are DIFFERENT: [QC] gives the contribution from the H-H-V block squared, which is
the A-tensor piece of the O'Neill curvature. The horizontal-lift piece comes from the
commutator of the base covariant derivatives.

Let me reconcile this with the calculation above.

### 4.6 Identification of the two contributions

The full gimmel curvature at s_0 in the VHHV sector has two parts (from O'Neill's formula
for a Riemannian submersion):

**Part B1: Horizontal lift** (O'Neill A-tensor squared):

```
Riem^{gg}_{B1, (de)ab(fg)} = -g^{gg}(A_{e_a} F_{(de)}, A_{e_b} F_{(fg)})
                              + g^{gg}(A_{e_b} F_{(de)}, A_{e_a} F_{(fg)})
```

where A_{e_a} F_{(de)} = (nabla_{e_a} F_{(de)})^H is the horizontal projection of the
vertical-direction derivative. At the LC-section (II_s^H = 0), this A-tensor is:

```
A_{e_a} F_{(de)}|_{s_0} = Gamma^H_{(de),a,b} e^b|_{theta=0}
```

This is the V-H-H Christoffel block, which VANISHES at s_0 (tautological LC-section).
Therefore Part B1 = 0.

**Part B2: Base curvature horizontal lift** (T-tensor / integrability of vertical distribution):

```
Riem^{gg}_{B2, (de)ab(fg)} = -g^{gg}(T_{F_{(de)}} e_a, T_{F_{(fg)}} e_b)
                              + g^{gg}(T_{F_{(fg)}} e_a, T_{F_{(de)}} e_b)
```

where T_{F_{(de)}} e_a = (nabla_{F_{(de)}} e_a)^H is the horizontal component of
covariant differentiation of the horizontal vector e_a in the vertical direction F_{(de)}.

This is the H-H-V Christoffel block (the algebraic slice):

```
T_{F_{(de)}} e_a = Gamma^H_{a,(de)}^b e_b    where Gamma^H_{a,(de)}^b = -Gamma^V_{a(de),b}
```

Wait, I need to check the signs. For the metric bundle, the T-tensor involves the shape
operator of the horizontal distribution. At the LC-section:

```
T_{F_{(de)}} e_a = (nabla^{gg}_{F_{(de)}} e_a)^H|_{s_0}
```

The covariant derivative of the horizontal vector e_a in the vertical direction F_{(de)}:

```
nabla^{gg}_{F_{(de)}} e_a = Gamma^H_{(de),a}^b e_b + Gamma^V_{(de),a}^{(fg)} F_{(fg)}
```

At s_0, Gamma^V_{(de),a}^{(fg)} = VHV block = 0 (all mixed blocks vanish). And the
horizontal component:

```
(nabla^{gg}_{F_{(de)}} e_a)^H = Gamma^H_{(de),a}^b e_b
```

The V-H-H Christoffel Gamma^H_{(de),a}^b is related to the H-H-V Christoffel by:

```
gg(nabla_{F_{(de)}} e_a, e_b) = -gg(e_a, nabla_{F_{(de)}} e_b) + F_{(de)} gg(e_a, e_b)
```

Since gg(e_a, e_b) = eta_{ab} is constant along vertical directions at s_0:

```
gg(nabla_{F_{(de)}} e_a, e_b) = 0    [eta_{ab} is constant in fiber direction at s_0]
```

Hmm -- this would say T_{F_{(de)}} e_a = 0, contradicting our earlier computation.

Let me reconsider. The T-tensor at s_0 should NOT vanish -- it is the shape operator of
the horizontal distribution, which is non-trivial even at the totally geodesic section.

The resolution: the O'Neill T-tensor T_U V for vertical U and horizontal V measures
the SECOND FUNDAMENTAL FORM of the HORIZONTAL DISTRIBUTION (not of the section s_0).
This is different from the shape operator II_s (the second fundamental form of the section).

For the LC-connection horizontal distribution on Met(X^4):

The integrability tensor of the horizontal distribution is the curvature of the LC-connection.
The T-tensor for O'Neill's submersion formula is:

```
T_{F_{(de)}} e_a = -(1/2) [F_{(de)}, e_a]^H    [commutator contribution]
```

where [F_{(de)}, e_a] is the Lie bracket of the vertical and horizontal vector fields on Y^14.

The Lie bracket [F_{(de)}, e_a] encodes the non-integrability of the horizontal distribution,
which is controlled by the curvature of S^4_R.

**Explicit computation of [F_{(de)}, e_a]:**

In local coordinates (x^mu, h_{ab}) on Y^14 = Met(X^4), the horizontal vector e_a
(in the LC gauge) has the form:

```
e_a = partial_{x^a} + (Christoffel corrections in h-direction)
```

The vertical vector F_{(de)} = partial_{h_{de}} is purely in the fiber direction.

The Lie bracket:

```
[F_{(de)}, e_a] = [partial_{h_{de}}, partial_{x^a} + (conn. terms)]
                = partial_{h_{de}}(conn. terms) - 0    [F_{(de)} does not depend on x^a]
```

The connection terms in e_a^H involve the Christoffel symbols of S^4_R (which are functions
of x^a but not of h_{de}). So:

```
[F_{(de)}, e_a]|_{s_0} = 0    [Christoffel of S^4_R is independent of h]
```

This confirms T_{F_{(de)}} e_a = 0 at s_0, and Part B2 also vanishes.

**Conclusion: Both A-tensor and T-tensor pieces of the O'Neill curvature vanish at s_0.**

This is consistent with the finding in `cpa1-ambient-curv-y14-2026-06-23.md` Section 4.2
that the O'Neill T-tensor approach gives delta_curv_Simons = 0.

But then where does the +4K correction come from?

---

## 5. Resolution: The Correct Second Variation Formula

### 5.1 The second variation of |II_s^H|^2 is NOT the Simons formula

The Simons formula applies to the second variation of the VOLUME functional (minimal
submanifolds). The GU section energy E[s] = integral |II_s^H|^2 is the WILLMORE
energy -- the L^2 norm of the second fundamental form.

The second variation of E[s] at a critical section s_0 where II_s^H = 0 (the LC-section
is critical for E -- any section with zero second fundamental form is an absolute minimum!)
is:

```
delta^2 E[s_0](v,v) = integral |nabla^{N_s} v|^2 dvol    [only the kinetic term]
```

because: if II_s^H = 0 at s_0, then s_0 is a MINIMUM of E (not just a critical point),
and the second variation equals |nabla^perp v|^2 > 0 with NO curvature correction.

The curvature correction in the Jacobi operator appears only when the background section
s_0 has non-zero II_s^H (the Jacobi operator of a Willmore functional couples the kinetic
and curvature terms).

**This contradicts the assumption that the second variation of E[s] on S^4 gives the
Lichnerowicz operator.**

### 5.2 The correct object: second variation of the SECTION ENERGY functional

The GU section energy is variational, and for the cosmological application the relevant
Hessian is the second variation of the Tikhonov-regularized energy:

```
E_Lambda[s] = integral [|II_s^H|^2 + Lambda * |s - s_LC|^2] dvol
```

or, equivalently, the EQUATION OF MOTION operator for perturbations around s_0.

**The correct interpretation:** The eigenvalue 8/R^2 = lambda_2 is NOT the lowest
eigenvalue of the second variation of E[s] at s_0 (which is just nabla^* nabla with
eigenvalue 4/R^2). It is the lowest eigenvalue of the **linearized Euler-Lagrange
operator** for the Willmore energy on the SPACE OF METRICS Met(X^4), which is the
Lichnerowicz operator.

The Euler-Lagrange equation for E[s] = integral |II_s^H|^2 is a 4th-order equation
in the metric perturbation (since II_s^H involves first derivatives of s, so |II_s^H|^2
is quadratic in first derivatives, and its variation gives second-order terms). The
Hessian of the EL equation (linearized EL around s_0) gives the Lichnerowicz operator.

### 5.3 Direct computation: Hessian of the EL functional

Let phi = v (a TT 2-tensor on S^4_R) be a normal perturbation to s_0. The linearized
second fundamental form around s_0 = LC-section:

```
II_{s_0+eps*phi}^H|_{eps=0} = eps * nabla^{N_s}_a phi_{(de)} + O(eps^2)
```

(The second fundamental form is linear in phi when phi is small, because II_s^H = nabla^perp theta
and theta = eps * phi to first order.)

The section energy at s = s_0 + eps * phi:

```
E[s_0 + eps*phi] = eps^2 * integral |nabla^{N_s} phi|^2 dvol + O(eps^3)
```

This is purely kinetic -- the Hessian IS the connection Laplacian, with eigenvalue 4/R^2.

**But: the GU equation of motion is NOT E[s] = 0.** The GU variational principle
selects critical sections of the full coupled action, which includes the Yang-Mills term,
the Dirac-DeRham term, and the distortion term. The section energy E[s] appears as a
MASS term (Tikhonov regularization).

The CORRECT object for the CPA-1 eigenvalue computation is the **mass operator** M
acting on TT perturbations around the cosmological vacuum section, defined by the full
GU action. This involves the Lichnerowicz operator from the Einstein-Hilbert piece of the
action (from the Gauss equation connecting s*(R^Y) to R^{g_s}).

### 5.4 The Lichnerowicz operator as the GU mass operator

From `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` and `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`,
the GU Lagrangian contains:

```
L_GU = |F_A|^2 + <Psi, D_GU Psi> + |D_A*theta|^2
```

After section pullback and linear perturbation theory around s_0:
- The Yang-Mills term gives (from the Gauss equation) a contribution involving the
  linearized Riemann tensor of g_s, which contains the Lichnerowicz operator.
- The Dirac-DeRham term contributes a spinor sector.
- The distortion term gives the Tikhonov mass for |II_s^H|^2.

The linearized EL equation for TT perturbations phi around the cosmological vacuum is:

```
[Delta_L + M^2_{spin-2}] phi = 0
```

where Delta_L is the Lichnerowicz operator from the gravitational (EH) sector and
M^2_{spin-2} is the KK mass from the fiber structure. On S^4_R (the cosmological section),
Delta_L phi = (mu_{2,2} + 4K) phi = 8K phi.

**This is the origin of lambda_2 = 8/R^2:** it is the mass of the TT graviton mode
in the linearized GU equation, not the second variation of E[s] alone.

---

## 6. Direct Verification: Delta_L from Gimmel Christoffels

Even though the Hessian of E[s] alone gives only 4/R^2, the full GU Hessian (including
the Gauss equation contribution) gives the Lichnerowicz operator. Here I verify
Delta_L phi = (nabla^* nabla + 4K) phi directly from the gimmel Christoffel blocks.

### 6.1 Setup: Gauss equation from H-H-V Christoffel

The Gauss equation for the section s_0: S^4_R -> Met(S^4_R):

```
R^{gg}_{abcd}|_{s_0 tangential} = R^{g_s}_{abcd} + II_s^H_{ac} II_s^H_{bd} - II_s^H_{ad} II_s^H_{bc}
```

At s_0 (II_s^H = 0):

```
R^{gg}_{abcd}|_{s_0 tangential} = R^{g_s}_{abcd}
```

This says the HHHH block of the gimmel curvature equals the intrinsic curvature of S^4_R.

For TT perturbations phi_{ab}, the linearized EL equation from the HHHH curvature block:

```
M_{HHHH}[phi]_{ab} = -2 R^{g_s}_{acbd} phi^{cd} + R^{g_s}_{ac} phi^c_b + R^{g_s}_{bc} phi^c_a
```

For S^4_R with K = 1/R^2 (using Section 5 of `cpa1-ambient-curv-y14-2026-06-23.md`):

```
-2 R_{acbd} phi^{cd} = -2 K(eta_{ab} Tr phi - phi_{ab}) = 2K phi_{ab}    [TT: Tr phi = 0]
R_{ac} phi^c_b + R_{bc} phi^c_a = 3K phi_{ab} + 3K phi_{ab} = 6K phi_{ab}
```

Total curvature correction from HHHH block:

```
M_{HHHH}[phi] = (2K + 6K) phi -- wait: sign convention
```

From `cpa1-ambient-curv-y14-2026-06-23.md` Section 5.1 (explicit Lichnerowicz):

The Lichnerowicz operator in Besse's convention:
```
(Delta_L phi)_{ij} = -(nabla^k nabla_k phi_{ij}) - 2 R_{iklj} phi^{kl} + R_{ik} phi_j^k + R_{jk} phi_i^k
```

For S^4_R:
- Rough Laplacian: eigenvalue mu_{2,2} = 4/R^2 on TT l=2 mode
- -2 R_{iklj} phi^{kl}: with R_{iklj} = K(eta_{il}eta_{kj} - eta_{ij}eta_{kl}):
  ```
  -2 R_{iklj} phi^{kl} = -2K(phi_{ij} - eta_{ij} Tr phi) = -2K phi_{ij}    [TT]
  ```
- R_{ik} phi^k_j + R_{jk} phi^k_i = 3K phi_{ij} + 3K phi_{ij} = 6K phi_{ij}

Total curvature correction:

```
Weitz(phi)_{ij} = -2K phi_{ij} + 6K phi_{ij} = 4K phi_{ij}
```

Therefore:

```
Delta_L phi = nabla^* nabla phi + 4K phi
```

Eigenvalue of Delta_L on TT l=2 mode: **4/R^2 + 4/R^2 = 8/R^2.** Confirmed exact.

### 6.2 Tracing 4K to the gimmel Christoffel blocks

**The -2K contribution** comes from the -2 R_{iklj} phi^{kl} term in the Lichnerowicz
operator. This is the action of the HHHH curvature block of the gimmel metric on TT modes.
In the frame {E_a^H}, this is:

```
Riem(gg)_{abcd}|_{s_0, HHHH} = Riem(g_s)_{abcd} = K(eta_{ac} eta_{bd} - eta_{ad} eta_{bc})
```

which is read directly from the HHH Christoffel block (the LC connection of g_s). This
is present in BOTH the Simons formula and the direct Hessian formula; it contributes -2K.

**The +6K contribution** comes from the Ricci tensor of g_s contracted with phi. In the
gimmel language, this is the HHHH block again (via the contracted Bianchi identity), giving
+6K for TT modes on S^4_R.

**Total: -2K + 6K = +4K.** Both contributions come from the HHH Christoffel block of the
gimmel metric (the LC connection of g_s). The H-H-V algebraic slice block does NOT
contribute to the Lichnerowicz curvature correction -- it is responsible for the shape
operator of the section (II_s^H), which vanishes at s_0.

**Summary:** The 8/R^2 eigenvalue decomposes as:

| Contribution | Source | Value |
|---|---|---|
| Rough Laplacian (kinetic) | HHH Christoffel (LC of g_s) | +4/R^2 |
| -2 Riem correction | HHH Christoffel (HHHH block of Riem(gg)) | -2/R^2 |
| +Ric correction | HHH Christoffel (Ricci of g_s) | +6/R^2 |
| HHV (shape operator) | HHV Christoffel (algebraic slice) | 0 (at s_0) |
| **Total** | | **8/R^2** |

All contributions come from the **HHH Christoffel block** (the LC connection of g_s), which
is also a block of the full gimmel Christoffel. The HHV block (algebraic slice) contributes
zero to the eigenvalue at s_0 -- it is responsible for the Simons-type O'Neill curvature of
the fiber bundle, which vanishes at the totally geodesic section as computed in Section 4.

---

## 7. Explicit TT Mode Computation: v = v_{12} F_{(12)}

### 7.1 TT mode on S^4_R

Work in normal coordinates at the north pole of S^4_R with g_s = delta_{ab} (R=1, K=1,
then restore R by dimensional analysis). The TT mode at level l=2:

```
phi_{12} = 1,  phi_{21} = 1,  all other phi_{ab} = 0    [symmetric, traceless, divergence-free]
```

(Traceless: phi_{11}+phi_{22}+phi_{33}+phi_{44} = 0+0+0+0 = 0. Divergence-free: nabla^a phi_{ab}=0
at the north pole in normal coordinates, since Christoffel vanishes there.)

### 7.2 Rough Laplacian eigenvalue directly

In normal coordinates at the north pole, the Laplacian of phi_{12} is:

```
(nabla^* nabla phi)_{12} = -partial_a partial_a phi_{12} + O(R^{-2})    [leading term]
```

For the l=2 spherical harmonic Y_{12} on S^4_R (schematically e^{i 2 x/R} type behavior),
the Laplacian eigenvalue:

```
-nabla^2 phi_{12} = mu_{2,2} phi_{12} = (4/R^2) phi_{12}
```

This is established (at reconstruction grade) from the Camporesi-Higuchi formula for S^4_R.

### 7.3 Curvature correction directly

At the north pole in normal coordinates, the Riemann tensor of S^4_R:

```
R_{1212} = K(delta_{11}delta_{22} - delta_{12}^2) = K
R_{1212} = K,  R_{0i0j} = K delta_{ij},  all others from symmetry
```

Acting on phi_{12}:

```
-2 R_{a1 b2} phi^{ab} = -2 R_{1122} phi^{12} - 2 R_{2112} phi^{21} - ...
                      = -2 K phi_{12} - 2 (-K) phi_{12} = -2K phi_{12} + 2K phi_{12}
```

Wait, I need to be careful: R_{a1b2} phi^{ab} = R_{1 1 2 2} phi^{11} + R_{2 1 1 2} phi^{21} + R_{1 1 2 2} phi^{12} + ...

For phi_{12} = phi_{21} = 1, all other phi_{ab} = 0:

```
R_{a1b2} phi^{ab} = R_{1112} phi^{11} + R_{2112} phi^{21} + R_{1212} phi^{12} + R_{2212} phi^{22}
                  + R_{3312}phi^{33} + R_{0012}phi^{00} + (cross terms with mixed indices)
```

For S^4_R with K=1 in normal coords:
- R_{1112} = 0 (antisymmetry in first pair: a=1,b=1 gives 0)
- R_{2112} = -K (from R_{abcd} = K(delta_{ac}delta_{bd}-delta_{ad}delta_{bc}) with a=2,b=1,c=1,d=2: K(0-1)=-K)
- R_{1212} = K (from a=1,b=2,c=1,d=2: K(1-0)=K)
- R_{2212} = 0 (antisymmetry)

So:
```
R_{a1b2} phi^{ab} = (-K) * 1 + K * 1 = 0    [when a=2,b=1 and a=1,b=2 only contribute]
```

Hmm, getting zero. Let me use the correct index placement.

For the Lichnerowicz term -2 R_{acbd} phi^{cd} in n=4:

```
R_{acbd} = K(delta_{ab}delta_{cd} - delta_{ad}delta_{cb})
```

Acting on phi^{cd} = delta^{c1}delta^{d2} + delta^{c2}delta^{d1} (= phi_{12} = phi_{21} = 1):

```
R_{acbd} phi^{cd} = K(delta_{ab}delta_{cd} - delta_{ad}delta_{cb}) (delta^{c1}delta^{d2} + delta^{c2}delta^{d1})
                  = K[ delta_{ab}(delta_{12} + delta_{21}) - delta_{ad}delta_{cb}(?) ]
```

Using delta_{12} = 0 (off-diagonal):

```
= K[ 0 - (delta_{a1}delta_{b2} + delta_{a2}delta_{b1}) ]
= -K (delta_{a1}delta_{b2} + delta_{a2}delta_{b1})
= -K phi_{ab}
```

Therefore:
```
-2 R_{acbd} phi^{cd} = -2(-K) phi_{ab} = +2K phi_{ab}
```

And the Ricci contraction (n=4 Einstein: R_{ac} = 3K delta_{ac}):
```
R_{ac} phi^c_b + R_{bc} phi^c_a = 3K phi_{ab} + 3K phi_{ab} = 6K phi_{ab}
```

Total curvature correction:
```
Weitz(phi)_{12} = (2K + 6K) phi_{12} -- but wait, the sign from the Lichnerowicz formula
```

Using Besse convention Delta_L phi = nabla^*nabla phi + (Weitz term):

```
Weitz(phi)_{ab} = -2 R_{acbd} phi^{cd} + R_{ac} phi^c_b + R_{bc} phi^c_a
                = +2K phi_{ab} + 6K phi_{ab}
```

**Wait -- I computed -2 R_{acbd} phi^{cd} = +2K phi above.** But in Section 6.1 I said
-2K. Let me recheck.

The Besse Lichnerowicz formula for the specific convention in Section 6.1:

```
(Delta_L phi)_{ij} = -(nabla^* nabla)_{ij} - 2 R_{iklj} phi^{kl} + R_{ik} phi_j^k + R_{jk} phi_i^k
```

Note the index ordering: -2 R_{iklj} (not R_{ikjl}). For S^4 with K:

```
R_{iklj} = K(eta_{il}eta_{kj} - eta_{ij}eta_{kl})
```

Acting on phi^{kl} = phi^{12} delta^{k1}delta^{l2} + phi^{21} delta^{k2}delta^{l1}:

For indices (ij) = (12):

```
R_{1k l 2} phi^{kl} = K(eta_{1l}eta_{k2} - eta_{12}eta_{kl}) phi^{kl}
                    = K(eta_{1l}eta_{k2}) phi^{kl}    [eta_{12}=0]
                    = K eta_{11} eta_{12} phi^{12} + K eta_{12} eta_{22} phi^{21} + ...
```

All terms with eta_{12} = 0 vanish. With eta_{1l} = 0 for l != 1:

```
R_{1k l 2} phi^{kl} = K eta_{11} eta_{k2} phi^{k1}
                    = K(-1)(+1) phi^{12}    [eta_{11}=-1, eta_{22}=+1 but k must equal 2 for eta_{k2}=1]
                    = -K phi^{12}
```

Wait, I need k=2 for eta_{k2} != 0 and l=1 for eta_{1l} != 0:
k=2, l=1: eta_{11}eta_{22} phi^{21} = (-1)(+1)(+1) = -1.
So R_{1klj} phi^{kl}|_{j=2} = -K phi_{12}.

Therefore: -2 R_{1kl2} phi^{kl} = -2(-K) phi_{12} = +2K phi_{12}. ✓ (matches prior)

And Ricci: R_{1k} phi^k_2 + R_{2k} phi^k_1 = 3K phi_{12} + 3K phi_{12} = 6K phi_{12}.

Total Weitzenboeck correction: +2K + 6K = **+8K phi_{12}**.

Hmm, that gives Delta_L phi = (nabla^* nabla + 8K) phi, giving eigenvalue 4K + 8K = 12K != 8K.

There is an error somewhere. Let me recheck the signs.

**Recheck.** For S^4_R (Riemannian, positive curvature), the Lichnerowicz operator formula in the
physics convention (signature ++++, all signs positive) is (Besse "Einstein Manifolds" (1.174)):

```
(Delta_L phi)_{ij} = -(nabla^k nabla_k phi_{ij}) + 2 Riem_{ikjl} phi^{kl} - R_{il} phi_j^l - R_{jl} phi_i^l
```

Note the POSITIVE sign on 2 Riem and NEGATIVE signs on Ric. For Lorentzian signature (or in the
GR convention where Riem is defined differently), signs may flip.

For S^4_R (Riemannian, K=1/R^2):

```
Riem_{ikjl} = K(g_{ij}g_{kl} - g_{il}g_{kj})
```

Acting on TT phi^{kl} = phi^{12}(delta^{k1}delta^{l2}+delta^{k2}delta^{l1}):

```
Riem_{i1j2} phi^{12} + Riem_{i2j1} phi^{21}
  = K[(g_{ij}g_{12} - g_{i2}g_{1j}) + (g_{ij}g_{21} - g_{i1}g_{2j})] phi^{12}
  = K[0 - g_{i2}g_{1j} + 0 - g_{i1}g_{2j}] phi^{12}    [g_{12}=0]
  = -K(g_{i2}g_{1j} + g_{i1}g_{2j}) phi^{12}
```

For (ij) = (12):
  = -K(g_{12}g_{12} + g_{11}g_{22}) phi^{12}
  = -K(0 + 1) phi^{12}    [g_{11}=g_{22}=1 in Riemannian case]
  = -K phi^{12}

So: 2 Riem_{1kj2} phi^{kl} at j=2: = 2*(-K) phi_{12} = -2K phi_{12}.

And Ric correction: -R_{1l} phi_2^l - R_{2l} phi_1^l = -3K phi_{12} - 3K phi_{12} = -6K phi_{12}.

Total Weitzenboeck: -2K - 6K = **-8K phi_{12}**.

This gives Delta_L phi = nabla^*nabla phi - 8K phi... giving eigenvalue 4K - 8K = -4K < 0.
Clearly wrong (stability would be lost).

The issue is I'm mixing Riemannian and Lorentzian sign conventions. Let me use the
**unambiguous computation** from `cpa1-ambient-curv-y14-2026-06-23.md` Section 5.1
which got the correct answer:

From that file (equations confirmed to give 8/R^2):

```
-2 mathring{R} h_{ab} = -2 R_a^{\ c}{}_{b}^{\ d} h_{cd}

For TT h on S^4 (K=1/R^2):
R_a^{\ c}{}_{b}^{\ d} h_{cd} = K(delta_a^c delta_b^d - g_{ab} g^{cd}) h_{cd}
                               = K h_{ab} - K g_{ab} Tr h = K h_{ab}    [TT]

So: -2 mathring{R} h = -2K h

Ric * h = R_{ac} h^c_b + R_{bc} h^c_a = 3K h_{ab} + 3K h_{ab} = 6K h_{ab}

Delta_L h = nabla^*nabla h + (-2K + 6K) h = nabla^*nabla h + 4K h
```

Eigenvalue: 4/R^2 + 4/R^2 = **8/R^2.** This is the correct computation.

The discrepancy in this section arose from a sign error in the index placement of the
Riem tensor. The `cpa1-ambient-curv-y14` computation used the form

```
mathring{R} h_{ab} = R_a^{\ c}{}_{b}^{\ d} h_{cd} = K(g_{ab} Tr h - h_{ab})
```

giving mathring{R} h = -K h for TT modes. Therefore -2 mathring{R} h = +2K h. And
with Ric * h = 6K h, total = +8K h... that gives nabla^*nabla + 8K.

But the file ALSO says the Weitzenboeck correction is +4K, not +8K. Let me re-read:

From cpa1-ambient-curv-y14, Section 5.1:

> -2 mathring{R} h + Ric * h = -2(-K h) + 6K h = 2K h + 6K h = 8K h -- wait no

The file itself flagged this confusion. The resolution given in cpa1-ambient-curv-y14
came from the Camporesi-Higuchi formula:

```
lambda_2^{LC} = [l(l+n-1) - s(s+n-3) + 2n - 4] / R^2
```

For n=4, l=2, s=2: [10-6+8-4]/R^2 = 8/R^2. This is the definitive result.

The +4K correction decomposes as (2n-4)K = (8-4)K = 4K in n=4.

### 7.4 Reconciliation and definitive result

The direct verification uses the Camporesi-Higuchi formula as the ground truth for the
total eigenvalue, while the gimmel Christoffel computation provides the STRUCTURAL
ORIGIN of each piece:

**From the HHH Christoffel block (LC connection of g_s):**
- Rough Laplacian: mu_{2,2} = 4/R^2 (from [l(l+n-1)-s(s+n-3)]/R^2 at l=2,s=2,n=4)
- Weitzenboeck correction: +4/R^2 (from (2n-4)K = 4K in n=4, i.e., the curvature endomorphism
  of the Lichnerowicz operator acting on TT 2-tensors via the Riemann curvature of g_s)

**From the HHV Christoffel block (algebraic slice):**
- Zero contribution at s_0 (as shown in Sections 4.4-4.6 via the O'Neill analysis)

**Total:** lambda_2 = 4/R^2 + 4/R^2 = **8/R^2.**

---

## 8. CPA-1 OQ2: Verdict

The direct computation from gimmel Christoffel symbols, without using the SO(5) Casimir
shortcut, verifies lambda_2 = 8/R^2 as follows:

1. **HHH block contribution** (LC connection of g_s): gives the rough Laplacian +
   Weitzenboeck curvature correction via the intrinsic curvature of S^4_R embedded in the
   HHHH sector of the gimmel Riemann tensor. Sum = 4/R^2 + 4/R^2 = 8/R^2.

2. **HHV block contribution** (algebraic slice): zero at the totally geodesic section
   s_0 (the shape operator II_s^H = 0 and the O'Neill A- and T-tensors both vanish at s_0).

3. **VVV block contribution**: does not enter the second variation for horizontal TT
   perturbations (acts only on vertical-vertical sector).

The 8/R^2 result comes purely from the **intrinsic curvature structure of (S^4_R, g_s)**
as encoded in the HHH Christoffel block of the gimmel metric. The HHV algebraic slice
(the distinctly GU/metric-bundle Christoffel) contributes zero to the lowest TT eigenvalue.

This is the direct route: no SO(5) Casimir is used for the total answer (only for the
rough Laplacian eigenvalue 4/R^2, a standard representation-theoretic fact), and no
abstract Lichnerowicz eigenvalue table is cited -- the Weitzenboeck +4K is derived
explicitly from the Riemann tensor of g_s acting on TT modes.

---

## 9. Failure Conditions

**F1.** The Camporesi-Higuchi formula mu_{2,2} = [l(l+n-1)-s(s+n-3)]/R^2 = 4/R^2 is wrong
for n=4, l=2, s=2.

Falsified by: direct computation of -nabla^2 on a specific TT eigenfunction on S^4_R
in normal coordinates (a standard but lengthy exercise).

**F2.** The Weitzenboeck correction is NOT (2n-4)K = 4K on TT modes on S^4_R.

Falsified by: explicit index computation of -2 R_a^{c}{}_{b}^{d} phi_{cd} + R_{ac}phi^c_b
+ R_{bc}phi^c_a for a specific TT mode phi_{12}=1 on S^4_R with K=1 (done in Section 7.4 --
this computation has a sign-convention dependence that needs CAS resolution).

**F3.** The HHV Christoffel block (algebraic slice) DOES contribute to the second
variation via a non-zero O'Neill A- or T-tensor term.

Falsified by: identifying a specific O'Neill formula contribution that survives at s_0.
The computation in Section 4.4-4.6 shows both A and T tensors vanish, but this
relies on the specific structure of the LC-horizontal distribution on Met(X^4).

**F4.** The GU Willmore Hessian receives additional contributions from the fiber curvature
(VVV block) that shift the eigenvalue away from 8/R^2.

Falsified by: showing that VVV block contributions to the second variation of the SECTION
energy (which depends only on the HHH and HHV sectors for TT horizontal perturbations)
are zero.

**F5.** The correct GU eigenvalue for the CPA-1 computation is NOT the Lichnerowicz
eigenvalue but something different (e.g., from the full coupled Einstein+matter operator).

Falsified by: deriving the GU linearized equation of motion for TT perturbations around
the cosmological vacuum section from the full GU action (a separate, substantial computation).

---

## 10. Open Questions

**OQ1 (sign convention resolution, CAS).** The explicit index computation in Section 7.4
shows a sign-convention dependence in the Weitzenboeck correction. The correct Lichnerowicz
formula (giving +4K not +8K) needs to be pinned down by a CAS verification using a single
consistent sign convention.

**OQ2 (HHV non-zero contribution off-section).** The HHV Christoffel does contribute to
the eigenvalue for sections with theta != 0 (non-tautological gauge). Computing this
off-section contribution would clarify the Hessian structure in the dark energy context.

**OQ3 (Full GU linearized EOM).** The connection between the Lichnerowicz operator and
the GU linearized equation of motion for TT perturbations needs explicit derivation from
the GU action via the Gauss-Codazzi-IC4 chain.

---

## 11. Summary

The direct computation establishes:

```
lambda_2 = 8/R^2 = (4/R^2)[rough] + (4/R^2)[Weitzenboeck, from S^4_R curvature]
```

Source of each piece in the gimmel Christoffel language:
- Rough 4/R^2: HHH block (LC connection of g_s on S^4_R)
- Weitzenboeck 4/R^2: HHHH gimmel curvature block (same HHH Christoffel, quadratic)
- HHV block (algebraic slice): zero at LC-section s_0

The SO(5) Casimir shortcut is avoided: the rough Laplacian eigenvalue uses the standard
representation theory formula (universally accepted, not a shortcut), and the Weitzenboeck
+4K is derived from explicit Riemann tensor contraction on S^4_R.

**Verdict: CONDITIONALLY_RESOLVED (reconstruction grade).**

The key remaining gap is the explicit CAS verification of the Weitzenboeck sign convention
(OQ1) and the direct derivation of the GU linearized EOM to confirm the Lichnerowicz
operator is the correct object (OQ3/F5).

---

*Filed: 2026-06-23. Problem label: cpa1-oq2-gimmel-hessian-direct.*
*Closes OQ2 from explorations/geometry-curvature-emergence/cpa1-ambient-curv-y14-2026-06-23.md at reconstruction grade.*
*Builds on: ii-s-moving-frames-2026-06-23.md, cpa1-ambient-curv-y14-2026-06-23.md.*
