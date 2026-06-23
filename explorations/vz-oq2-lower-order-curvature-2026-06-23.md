---
title: "VZ OQ2: Lower-Order Curvature Terms in D_GU and Light-Cone Preservation"
date: 2026-06-23
problem_label: "vz-oq2-curvature"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ OQ2: Lower-Order Curvature Terms in D_GU and Light-Cone Preservation

## 1. Problem Statement

The principal-symbol analysis in `explorations/vz-schur-complement-2026-06-23.md` established
(reconstruction grade) that VZ is evaded for the D_GU operator: the effective RS principal
symbol `D_RS_eff(xi) = S_R(xi)` has trivial kernel for all non-null 14D covectors. The proof
relied entirely on the Clifford identity `sigma_D(xi)^2 = g_Y(xi,xi) Id_E`.

**OQ2 asks:** Does VZ evasion survive when lower-order terms in D_GU are included?

Specifically: the gimmel metric `g_Y` on `Y^{14}` has a nonzero Weyl tensor (it is a curved
pseudo-Riemannian manifold). The operator `D_GU` written in local coordinates includes:

1. A principal (first-order symbol) term `sigma_D(xi)` -- this is what the Schur complement
   analysis handled.
2. Zero-order terms from the connection: curvature of the spin connection, Ricci tensor
   contractions, the Weyl tensor of the gimmel metric.
3. The Sp(64) gauge background via the distortion `theta = A - Gamma`.

The classical VZ theorem (Velo-Zwanziger 1969, Johnson-Sudarshan 1961) proved that
**even after the principal-symbol (free) equations are causal**, the *constraint equations*
derived by acting with subsidiary conditions on the RS field equation can develop acausal
characteristics when lower-order curvature terms are present. This is the curvature VZ
mechanism: not the principal propagation but the constraint propagation becomes spacelike.

**The question in coordinates.** Let `Psi_A` be the RS section of `E_1 = Omega^1(Y^{14}) tensor S`
constrained by `Gamma^{14D}(Psi) = 0`. The full equation of motion including lower-order terms is:

```
P_R D_GU Psi = 0
```

where `D_GU = sigma_D(D) + lower-order`. The constraint `Gamma^{14D} Psi = 0` is maintained
by the principal symbol (as established in vz-schur-complement). The question is whether
lower-order curvature terms in the commutator `[D_GU, Gamma^{14D}]` reintroduce a
propagation speed exceeding the light cone.

---

## 2. Established Context

**Setup from prior explorations:**

- `Cl(9,5) ~= M(64,H)`, `S = H^{64}` (N1, reconstruction)
- Principal symbol: `sigma_D(xi)^2 = g_Y(xi,xi) Id_E` (exact at the symbol level)
- RS projection: `R^{14D} = ker Gamma^{14D}`, `dim R^{14D} = 13 * 256 = 3328` over R
- VZ evasion at principal-symbol level: `ker S_R(xi) = 0` for `xi^2 != 0` (reconstruction)
- OQ1 resolved (vz-oq1): `S_R^2 != xi^2 Id` as exact matrix identity; `A S_R = xi^2 Id` is
  the correct statement. The RS sub-bundle is NOT a sub-Clifford-module.
- HC1 (hc1-hidden-curvature-components-2026-06-22.md): The gimmel metric curvature has a
  6-piece decomposition `W + S_0 + R + H^(1) + H^(2) + H^(3)`. The three "hidden" pieces
  `H^(i)` are activated by the distortion torsion components `T^(1,2,3)`.
- HC1 SL(2,C) refinement (hc1-sl2c-bianchi-spinor-2026-06-23.md): `H^(1)` carries
  `(3/2,1/2) + (1/2,3/2)` (16 real components), `H^(2)` and `H^(3)` each carry `(1/2,1/2)`.

**The classical VZ lower-order mechanism (reference: Velo-Zwanziger 1969 §4).**

For a generic spin-3/2 field `psi_mu` in a gauge background `A_mu`, the equation of motion is
(schematically in 4D notation for comparison):

```
(gamma^mu d/dx_mu) psi_nu - d/dx_nu (gamma^mu psi_mu) + m psi_nu = 0
```

Acting with `d/dx^nu` and using the gauge-background field strength `F_mu_nu`:

```
(box psi_nu + F_{nu mu} psi^mu + R_{nu mu} psi^mu + ...) = 0
```

The curvature term `R_{nu mu} psi^mu` appears in the *secondary* equation derived from the
*constraint* `gamma^mu psi_mu = 0`. This secondary propagation equation has characteristics
determined by the EFFECTIVE metric `G_eff^{mu nu}` which acquires corrections from `R_{mu nu}`
or `F_{mu nu}` and can become acausal (having solutions with real characteristics in spacelike
directions).

The question for GU is whether the analogous mechanism operates in 14D for D_GU.

---

## 3. Structure of D_GU at Sub-Leading Order

### 3.1 The Rolled-Up Operator

D_GU acts on sections of `E = (Omega^0 tensor S+) direct-sum (Omega^1 tensor S-)`.
In a local frame `{e^A}` on `Y^{14}` (with `g_Y(e^A, e^B) = eta^{AB}` the flat (9,5) metric):

```
D_GU = gamma^A nabla_A + Phi(F_A tensor .)
```

where `nabla_A = d_{e_A} + omega_A` is the spin connection derivative, `omega_A` is the
spin connection of the gimmel metric `g_Y`, and `Phi(F_A tensor .)` is the Shiab term
involving the curvature of the gauge connection `A`.

Expanded to sub-leading order in a Riemann normal coordinate system for `g_Y`:

```
D_GU = gamma^A (d/dx^A) + gamma^A omega_A + (Shiab correction)
                   [principal]   [sub-leading, O(curvature)]
```

The sub-leading term `gamma^A omega_A` involves the spin connection `omega_A` which is
`O(curvature * distance)` in Riemann normal coordinates. Explicitly:

```
omega_A = (1/4) R_{ABCD} x^B gamma^{CD} + O(|x|^2 curvature)
```

near a point, where `R_{ABCD}` is the Riemann tensor of `g_Y`.

### 3.2 Lower-Order Terms in the RS Block

The RS constraint equation (on a section `Psi` satisfying `Gamma^{14D} Psi = 0`) is:

```
P_R D_GU Psi = 0.
```

Expanding `D_GU = D_0 + D_1` where `D_0 = gamma^A d_A` (principal, zero-connection) and
`D_1 = gamma^A omega_A + (Shiab)` (sub-leading):

```
P_R D_0 Psi + P_R D_1 Psi = 0.
```

The principal part `P_R D_0` is what was analyzed in the Schur complement computation.
The sub-leading part `P_R D_1 Psi` involves:

1. **Spin-connection term:** `gamma^A omega_A Psi`, which is a zero-order (multiplication)
   operator on sections. It does NOT change the principal symbol.

2. **Shiab curvature term:** `Phi(F_A tensor Psi)` where `F_A` is the Sp(64) gauge
   curvature. This is also a zero-order term (multiplication by `F_A` followed by Clifford
   contraction). It does NOT change the principal symbol.

**Key observation:** Lower-order terms are multiplication operators (zero-order differential
operators). They do NOT contribute to the principal symbol at all. The principal symbol is
determined solely by the leading (first-order) derivative terms.

---

## 4. The Classical VZ Lower-Order Mechanism: Does It Apply to D_GU?

### 4.1 The Classical Mechanism

In the original VZ analysis, the acausality arises as follows:

**Step 1.** Write the RS field equation as `L psi = 0` where L is first-order with
principal symbol `sigma_L(xi)`.

**Step 2.** Apply a subsidiary condition operator S (e.g., `d/dx^nu`) to derive a secondary
equation.

**Step 3.** Analyze the secondary equation. Its principal symbol is `sigma_L(xi) sigma_S(xi)`,
and if the combined operator has a wider characteristic cone than the original, acausality results.

**Step 4.** In the curvature background, the commutator `[L, S]` (or equivalently, the
substitution of the constraint into the field equation) introduces curvature terms that
modify the secondary equation at the level of the **leading symbol** of the secondary equation.

**The crucial distinction:** The sub-leading terms in `L` (curvature) become **leading terms**
in the secondary equation (the equation obtained by differentiating the constraint). This
is why lower-order curvature in the original equation can produce acausality in the derived
constraint propagation.

### 4.2 The GU Situation: No Standalone Subsidiary Condition

**The VZ lower-order mechanism requires the constraint to be an EXTERNAL subsidiary condition.**

In the standard spin-3/2 analysis, the constraint `gamma^mu psi_mu = 0` is IMPOSED as a
separate algebraic condition on the RS field, and then the field equation propagates. The
question is whether this imposed constraint is preserved under time evolution (i.e., whether
the constraint is a first-class or second-class constraint in the Dirac-Bergmann sense).

In the GU setup, the constraint `Gamma^{14D} Psi = 0` is NOT an external condition imposed
separately from the field equation. It is built into the structure of the operator D_GU via
the RS projection:

```
P_R D_GU Psi = 0,   with P_R the RS projector.
```

The RS sector is defined as `R^{14D} = ker Gamma^{14D}`, and the field `Psi in Gamma(R^{14D})`
takes values in this sub-bundle by construction. The "constraint" `Gamma^{14D} Psi = 0`
is a tautology, not an additional condition.

**Consequence:** There is no secondary equation derived by acting with `Gamma^{14D}` (or
its derivative) on the field equation, because `Gamma^{14D} Psi = 0` is satisfied
identically by assumption of the field configuration space, not by the dynamics.

This is the structural difference from the standalone RS field. For standalone RS:

```
(RS Lagrangian for psi_mu) => E.L. equation for psi_mu, PLUS constraint gamma^mu psi_mu = 0 from E.L.
```

and the two equations together produce inconsistency in a background with curvature (VZ).

For GU RS sector:

```
(D_GU Psi = 0 for Psi in Gamma(E)) restricted to RS sub-bundle => P_R D_GU Psi = 0.
```

There is one equation, not two. The constraint is not derived; it defines the domain.

### 4.3 The Propagation of the Constraint by D_GU

One might object: even if `Gamma^{14D} Psi = 0` is in the domain of the field `Psi`, the
time evolution under `D_GU` might take `Psi` OUT of the constraint surface
`{Psi : Gamma^{14D} Psi = 0}`. If so, the constraint is not preserved and one must analyze
the propagation of the constraint violation.

**The key commutator.** The question is whether:

```
D_GU : Gamma(R^{14D}) -> Gamma(R^{14D})
```

i.e., whether `D_GU` preserves the RS sub-bundle.

**Computation.** For `Psi in Gamma(R^{14D})` (so `Gamma^{14D} Psi = 0`), compute
`Gamma^{14D} (D_GU Psi)`:

```
Gamma^{14D} D_GU Psi = Gamma^{14D} (gamma^A nabla_A Psi) + Gamma^{14D} (Shiab term)
```

**Principal (free) part:**
```
Gamma^{14D} gamma^A d_A Psi = gamma^B gamma^A d_A Psi_B.
```

Using `{gamma^A, gamma^B} = 2 g_Y^{AB}`:
```
gamma^B gamma^A = 2 g_Y^{AB} - gamma^A gamma^B.
```

So:
```
gamma^B gamma^A d_A Psi_B = 2 g_Y^{AB} d_A Psi_B - gamma^A gamma^B d_A Psi_B
                           = 2 (div Psi) - gamma^A d_A (gamma^B Psi_B)
                           = 2 (div Psi) - gamma^A d_A (Gamma^{14D} Psi)
                           = 2 (div Psi)           [since Gamma^{14D} Psi = 0]
```

where `div Psi = g_Y^{AB} d_A Psi_B` is the divergence (a zero-order operation after the
derivative acts on the index).

Wait, this computation must account for the fact that `Psi_A` is spinor-valued. Specifically:

`Gamma^{14D}(D_0 Psi) = gamma^B (D_0 Psi)_B`

where `(D_0 Psi)_A = gamma^B d_B Psi_A - d_A (gamma^B Psi_B)` (from the D_0 formula).

Let me redo using the explicit principal symbol formula:
```
sigma_{D_0}(xi)(0, Psi)_A = xi_A (Gamma^{14D} Psi) - gamma(xi) Psi_A.
```

So `D_0 Psi` acting on the one-form field `Psi in Omega^1 tensor S` gives:

```
(D_0 Psi)_A = (d_A)(Gamma^{14D} Psi) - gamma^B d_B Psi_A.
```

Wait -- in the full operator sense, D_GU maps `(phi, Psi) in E_0 direct-sum E_1` to
`E_0 direct-sum E_1`. The one-form sector feeds the scalar sector and vice versa. For `Psi`
in the one-form sector:

```
D_GU(0, Psi) = (d^* Psi,  dA*dA Psi + shiab(F_A tensor Psi))
```

schematically. The scalar output is `d^* Psi = gamma^A nabla_A Psi^A` (the divergence).
The one-form output is `D_{1->1}(Psi)`.

The gamma-trace of the one-form output:
```
Gamma^{14D}(D_{1->1}(Psi)) = gamma^A (D_{1->1} Psi)_A.
```

For the principal (spin-connection-free) part `D_0`:
```
(D_{0,1->1}(Psi))_A = xi_A (g_Y^{BC} xi_B Psi_C) - gamma(xi) Psi_A
```
at the symbol level. So:
```
Gamma^{14D}(sigma_{D_0}(xi)(0,Psi))_A = gamma^A [(xi^B Psi_B) xi_A - gamma(xi) Psi_A]
= (xi^B Psi_B) gamma(xi) - gamma(xi) gamma^A Psi_A
= (xi^B Psi_B) gamma(xi) - gamma(xi) Gamma^{14D}(Psi).
```

For `Psi in R^{14D}`, `Gamma^{14D}(Psi) = 0`:
```
Gamma^{14D}(sigma_{D_0}(xi)(0,Psi)) = (xi^A Psi_A) gamma(xi).
```

This is the C-block output `chi * gamma(xi)` -- exactly the off-diagonal coupling C that
was computed in the Schur complement analysis. It is nonzero for generic `Psi in R^{14D}`.

So the principal-symbol-level answer is: `D_0` does NOT preserve `R^{14D}`. The image
of `D_0` acting on RS sections has a nonzero gamma-trace component `chi * gamma(xi)`.

**This is expected.** The entire Schur complement analysis was precisely about this coupling:
the off-diagonal C block maps RS -> Q (gamma-trace sector). The B block maps Q -> RS. The
effective RS dynamics are given by the Schur complement `A - B E^{-1} C`, which eliminates
the non-RS (Q) sector.

The point is that `D_GU` is NOT block-diagonal in the RS/non-RS decomposition. Its coupling
from RS to non-RS (via C) and back (via B) is the mechanism by which VZ is evaded at the
principal-symbol level. The "constraint `Gamma^{14D} Psi = 0`" is not preserved by `D_GU`
in a single step -- instead, it is maintained in the sense that the effective Schur complement
dynamics keep the RS sector's characteristic cone causal.

### 4.4 Lower-Order Terms and Constraint Propagation

**What the lower-order terms do.** At the full (non-principal) operator level:

```
Gamma^{14D}(D_GU Psi) = Gamma^{14D}(D_0 Psi) + Gamma^{14D}(D_1 Psi)
```

where `D_1 = gamma^A omega_A + Phi(F_A)` is the sub-leading part.

For `Psi in Gamma(R^{14D})`:

**Term 1** (computed above at symbol level):
```
Gamma^{14D}(D_0 Psi)|_A = (xi^B Psi_B) gamma(xi)    [zero unless we specify xi = d]
```
In the actual operator sense: `Gamma^{14D}(D_0 Psi) = chi * gamma(d)` where `chi = g_Y^{AB} nabla_A Psi_B`.

**Term 2** (spin connection):
```
Gamma^{14D}(gamma^A omega_A Psi) = gamma^B gamma^A omega_{A,cd} gamma^{cd} Psi_B / 4
```

where `omega_{A,cd}` are the spin-connection components. Using `gamma^B gamma^A = 2 g_Y^{BA} - gamma^A gamma^B`:

```
= 2 g_Y^{BA} omega_{A,cd} gamma^{cd} Psi_B / 4 - gamma^A (gamma^B omega_{A,cd} gamma^{cd} Psi_B) / 4
```

The first term involves `g_Y^{BA} omega_A` which is the trace of the spin connection (a
zero-order curvature term). The second term involves `gamma^A` acting on the spin-connection
operator applied to `Gamma^{14D} Psi = 0`, giving zero.

So:
```
Gamma^{14D}(gamma^A omega_A Psi) = (1/2) g_Y^{BA} omega_A (gamma^{cd} Psi_B) + zero.
```

This is proportional to the spin connection (and hence to the Riemann tensor of `g_Y`).
It is a zeroth-order curvature term multiplied by `Psi`.

**Term 3** (Shiab gauge curvature):
```
Gamma^{14D}(\Phi(F_A tensor Psi)) = gamma^B \Phi(F_A tensor Psi)_B
```

where `\Phi(F_A tensor Psi)_B = sum_C e^C_B c(\iota_{e_C} F_A) Psi_B` (Clifford contraction of F_A on Psi). This involves `F_A` (the Sp(64) gauge curvature) and the Clifford algebra action.

The output `Gamma^{14D}(\Phi(F_A tensor Psi))` is again a zero-order term (multiplication
by `F_A` and curvature) acting on `Psi`.

**Summary.** The constraint propagation equation:

```
Gamma^{14D}(D_GU Psi) = 0   (the condition for D_GU to map RS to RS)
```

has the form:

```
nabla^A Psi_A + (curvature of g_Y) * Psi + (F_A) * Psi = 0.
```

This is a first-order ODE for `Psi in Gamma(R^{14D})` (the divergence term is first-order,
the rest are zero-order). Its characteristic polynomial is determined by the divergence term:

```
sigma_{div}(xi) Psi = xi^A Psi_A = g_Y(xi, Psi).
```

This is a scalar (in S) at each point, and its characteristics are `{xi : g_Y(xi, Psi) = 0 for all Psi_A}` -- which requires `xi = 0` or `Psi = 0`. There are no finite spacelike characteristics.

**But this is misleading** -- the constraint propagation equation is not a standalone field
equation for `Psi`. It is the integrability condition for the system `(P_R D_GU Psi = 0, Gamma^{14D} Psi = 0)`. The true VZ analysis must look at the coupled system.

---

## 5. Hamiltonian Analysis of the Constrained System

### 5.1 Setup

Let `(x^0, x^i)` be a splitting of `Y^{14}` into time-like and spacelike directions (using
a Cauchy foliation with respect to `g_Y`). Write `Psi = (\Psi_0, \Psi_i)` (time and space
components of the RS 1-form spinor).

The full D_GU equation restricted to RS:

```
P_R D_GU Psi = 0                                              (E)
Gamma^{14D}(\Psi) = gamma^0 \Psi_0 + gamma^i \Psi_i = 0     (C)
```

(E) is the field equation; (C) is the constraint maintained in the initial data.

### 5.2 Cauchy Problem

**Initial data:** Specify `\Psi|_{t=0}` satisfying the constraint `C` at `t=0`.

**Evolution:** The time derivative `d\Psi/dt` is determined by the field equation `(E)`,
which (using `D_GU`) gives:

```
gamma^0 nabla_0 Psi + gamma^i nabla_i Psi + D_1 Psi = 0.
```

The RS projection `P_R` applied to this gives the evolution equation for `Psi in R^{14D}`.

### 5.3 Constraint Propagation

**Does (C) propagate?** Apply `Gamma^{14D}` to the time derivative of (C):

```
d/dt [Gamma^{14D} Psi] = Gamma^{14D} (d\Psi/dt).
```

From (E) (solving for `d\Psi/dt`):

```
gamma^0 d\Psi/dt = - gamma^i nabla_i Psi - D_1 Psi + (B-block coupling from Q sector).
```

The B-block coupling term is the key: it involves `B E^{-1} C \Psi`, which at the
principal level contributes a first-order spatial derivative term, and at the sub-leading
level contributes curvature corrections.

**The critical question:** Does the sub-leading curvature in `B E^{-1} C` (at the full
operator level, not just the symbol level) produce acausal propagation in the constraint
propagation?

### 5.4 Sub-Leading Corrections to the Schur Complement

At the full operator level, the Schur complement becomes:

```
S_R^{full} = A^{full} - B^{full} (E^{full})^{-1} C^{full}
```

where:
```
A^{full} = A^{(0)} + A^{(1)}    (principal + curvature correction)
B^{full} = B^{(0)} + B^{(1)}    (principal + curvature correction)
C^{full} = C^{(0)} + C^{(1)}    (principal + curvature correction)
E^{full} = E^{(0)} + E^{(1)}    (principal + curvature correction)
```

where the superscript `(1)` denotes zero-order (curvature) corrections.

The effective operator for the RS sector:

```
S_R^{full} = [A^{(0)} + A^{(1)}] - [B^{(0)} + B^{(1)}] [E^{(0)} + E^{(1)}]^{-1} [C^{(0)} + C^{(1)}].
```

Expanding `[E^{(0)} + E^{(1)}]^{-1} = (E^{(0)})^{-1} - (E^{(0)})^{-1} E^{(1)} (E^{(0)})^{-1} + ...`:

```
S_R^{full} = S_R^{(0)} + [A^{(1)} - B^{(0)} (E^{(0)})^{-1} C^{(1)}
                         - B^{(1)} (E^{(0)})^{-1} C^{(0)}
                         + B^{(0)} (E^{(0)})^{-1} E^{(1)} (E^{(0)})^{-1} C^{(0)}] + ...
```

where `S_R^{(0)} = A^{(0)} - B^{(0)} (E^{(0)})^{-1} C^{(0)}` is the principal Schur complement.

**Key observation.** All the correction terms `A^{(1)}, B^{(1)}, C^{(1)}, E^{(1)}` are
ZERO-ORDER operators (multiplication by curvature). Therefore:

- `B^{(0)} (E^{(0)})^{-1} C^{(1)}` involves a first-order operator `B^{(0)} (E^{(0)})^{-1}`
  followed by a zero-order multiplication `C^{(1)}`. The result is first-order.
- `B^{(1)} (E^{(0)})^{-1} C^{(0)}` involves a zero-order `B^{(1)}` followed by
  `(E^{(0)})^{-1} C^{(0)}` which is first-order. The result is first-order.
- All other terms are similar.

So the correction to `S_R` is a first-order differential operator. But its PRINCIPAL SYMBOL
is determined by the first-order part of the correction, which comes from the composition
of `(E^{(0)})^{-1}` (a pseudodifferential operator of order -1) with the first-order
part of the Schur complement.

**The principal symbol of S_R^{full} is the same as that of S_R^{(0)}.**

Why? The sub-leading terms in the expansion are:

```
A^{(1)} = zero-order    =>  sigma(A^{(1)}) = 0  (zero-order ops have zero principal symbol)
B^{(1)} = zero-order    =>  sigma(B^{(1)}) = 0
C^{(1)} = zero-order    =>  sigma(C^{(1)}) = 0
E^{(1)} = zero-order    =>  sigma(E^{(1)}) = 0
```

All sub-leading contributions to `S_R^{full}` are COMPOSITIONS of zero-order and
first-order operators, giving at most first-order operators -- but their leading symbol
comes from the first-order part, which is the SAME as `S_R^{(0)}`.

More precisely: the total principal symbol of `S_R^{full}` is `sigma_1(S_R^{full}) = sigma_1(S_R^{(0)})`,
since the correction is a pseudodifferential operator of the same order whose leading symbol
is zero (all sub-leading terms involve zero-order corrections composed with the pseudo-inversion
of a first-order operator, giving back a first-order operator with the SAME leading symbol as
the original).

**Formal statement.** For a first-order differential operator `L = L_1 + L_0` (where L_1 is the
principal part and L_0 is zero-order), the principal symbol `sigma_1(L) = sigma(L_1)` is
unaffected by `L_0`. Similarly, for the full Schur complement `S_R^{full} = S_R^{(0)} + (corrections)`,
the principal symbol of `S_R^{full}` equals that of `S_R^{(0)}`, since all corrections are zero-order
in the D_GU connection terms.

---

## 6. The Gimmel Weyl Tensor: Does It Generate Acausal Sub-Leading Structure?

### 6.1 Weyl Tensor Contributions

The gimmel metric `g_Y` on `Y^{14}` has a Weyl tensor `W_{ABCD}` (the traceless part of the
Riemann tensor). In 14D, the Weyl tensor contributes to the connection via:

```
R_{ABCD} = W_{ABCD} + (Ricci contributions).
```

The spin connection `omega_A` contains `R_{ABCD}` as a sub-leading curvature. In the RS
field equation, the Weyl tensor appears in the commutator:

```
[nabla_A, nabla_B] Psi_C = R_{ABCd} Psi^d (in the tangent index) + F_{AB}(gauge) Psi_C.
```

For the RS sector in D_GU, the relevant term is when we compute:

```
[D_{GU}, Gamma^{14D}] Psi
```

for `Psi in Gamma(R^{14D})`.

### 6.2 Computing [D_GU, Gamma^{14D}]

The commutator of D_GU with the gamma-trace operator:

```
[D_GU, Gamma^{14D}] Psi_A = D_GU(Gamma^{14D} Psi)_A - Gamma^{14D}(D_GU Psi)_A
```

For `Psi in R^{14D}` (so `Gamma^{14D} Psi = 0`), the first term vanishes, and:

```
[D_GU, Gamma^{14D}] Psi_A = - Gamma^{14D}(D_GU Psi)_A.
```

This is what we computed in §4.4 above. The commutator:

**Principal part:**
```
[D_0, Gamma^{14D}] Psi_A = - sigma_{D_0}(\nabla)(Gamma^{14D} Psi) + Gamma^{14D}(D_0 Psi)
                           = Gamma^{14D}(D_0 Psi)   [since Gamma^{14D} Psi = 0]
                           = (nabla^A Psi_A) gamma^B Psi_B / ...
```

Wait -- let me be explicit. Writing `D_0 = gamma^A nabla_A` acting on 1-form spinors:

```
(D_0 Psi)_B = gamma^A (nabla_A Psi_B) - (d_A^* Psi) delta_B^C ...
```

Actually, the D_GU operator in the `(E_0, E_1)` decomposition mixes sectors. For a purely
one-form input `Psi in E_1`:

```
D_0 Psi = (scalar part: d^* Psi, one-form part: F_nabla Psi)
```

where `d^* Psi = nabla^A Psi_A` (divergence) and `F_nabla Psi = F_{nabla}(Psi)` is the
first-order part of the curvature operator.

The key point: `Gamma^{14D}(F_nabla Psi)` picks up a curvature term via the commutator
`[nabla_A, nabla_B]`. Explicitly:

```
Gamma^{14D}(F_{nabla} Psi)_B
= gamma^B (gamma^A nabla_A Psi_B - nabla_B (nabla^A Psi_A))
= [gamma^B, gamma^A] nabla_A Psi_B + gamma^A gamma^B nabla_A Psi_B - nabla_B nabla^A Psi_A.
```

Using `[gamma^B, gamma^A] = 2 g_Y^{BA} - 2 gamma^A gamma^B`:

Wait, let me use the commutator identity in the Clifford algebra:

`{gamma^A, gamma^B} = 2 g_Y^{AB}`, so `gamma^A gamma^B = g_Y^{AB} - (1/2)[gamma^A, gamma^B]`.

The trace:
```
gamma^B gamma^A nabla_A Psi_B = g_Y^{AB} nabla_A Psi_B - (1/2)[gamma^B, gamma^A] nabla_A Psi_B
= nabla^A Psi_A + (1/2) gamma^{AB} [nabla_A, nabla_B] Psi   (schematic)
```

where the commutator `[nabla_A, nabla_B]` introduces the Riemann tensor. Specifically:

```
Gamma^{14D}(F_nabla Psi) = nabla^A Psi_A + (1/4) R_{ABCD} gamma^{AB} gamma^{CD} Psi + ...
```

The Riemann tensor term `R_{ABCD} gamma^{AB} gamma^{CD} Psi` involves the full curvature
(including Weyl). This is a **zero-order term** (multiplication by `R_{ABCD}`).

**The Weyl tensor contribution to `Gamma^{14D}(D_GU Psi)`:**

```
Gamma^{14D}(D_GU Psi)|_{Weyl} = W_{ABCD} gamma^{AB} gamma^{CD} Psi + (Ricci terms) + (gauge F)
```

This is a zero-order (multiplication) operator on `Psi`. Its contribution to the
characteristic analysis of the RS system is:

**A correction to the ZERO-ORDER part of S_R^{full}**, NOT to its principal symbol.

---

## 7. Characteristic Analysis of the Full Constrained System

### 7.1 The Effective RS Operator Including Curvature

The effective RS equation, after eliminating the Q sector via the Schur complement:

```
S_R^{full} Psi_R = 0
```

where `S_R^{full} = S_R^{(0)} + (zero-order curvature corrections)`.

The **characteristics** of this equation are determined by the principal symbol of `S_R^{full}`,
which equals the principal symbol of `S_R^{(0)}` (as argued in §5.4).

**The characteristic set of S_R^{full}** is:

```
Char(S_R^{full}) = {xi in T*Y^{14} : det(sigma_1(S_R^{full})(xi)) = 0}
                 = {xi in T*Y^{14} : det(sigma_1(S_R^{(0)})(xi)) = 0}
                 = {xi in T*Y^{14} : g_Y(xi,xi) = 0}   [by the OQ-vz-schur result]
```

This is the **null cone** of the gimmel metric `g_Y`. All propagation is at most at the
speed of light in the gimmel metric.

**VZ acausality would require:**

```
Char(S_R^{full}) ⊃ {xi : g_Y(xi,xi) > 0}   (spacelike covectors as characteristics)
```

Since the characteristic set of `S_R^{full}` is exactly the null cone (same as principal
symbol, which is unchanged by zero-order curvature), spacelike characteristics are absent.

### 7.2 The Weyl Tensor Cannot Enlarge the Characteristic Cone

**Theorem (characteristic stability under zero-order perturbations).**

For a first-order differential operator `L = L_1 + L_0` (principal `L_1`, zero-order `L_0`),
the characteristic cone is determined solely by `L_1`:

```
Char(L) = Char(L_1) = {xi : det(sigma(L_1)(xi)) = 0}.
```

Adding zero-order terms `L_0` does not change the principal symbol and hence does not
change the characteristic cone.

**Proof.** By definition, `sigma_1(L) = sigma_1(L_1 + L_0) = sigma_1(L_1) + sigma_1(L_0) = sigma_1(L_1)`,
since `sigma_1(L_0) = 0` for a zero-order operator `L_0`. The characteristic set depends
only on the principal symbol. QED.

**Application.** The curvature corrections to `D_GU` (spin connection, Riemann tensor, Weyl
tensor of `g_Y`, Sp(64) gauge curvature `F_A`) are all zero-order in the sense that they
multiply `Psi` without taking additional derivatives (they appear in the sub-leading term
`D_1` of `D_GU`). Therefore, they cannot change the characteristic set, which remains the
null cone.

**The Weyl tensor of the gimmel metric** `g_Y` enters the RS dynamics only at zero order
(via the spin connection and the commutator identity for the Riemann tensor). It does NOT
introduce new first-order derivative terms in the effective RS operator. Therefore, it cannot
produce spacelike characteristics.

### 7.3 Why This Differs from the Classical VZ Mechanism

**Classical VZ (standalone RS in a gauge background):**

- The RS field has a standalone Lagrangian with a Lorentz invariance constraint.
- The constraint `gamma^mu psi_mu = 0` is derived from varying the Lagrangian.
- The propagation equation and the constraint are coupled but SEPARATE equations.
- Acting on the propagation equation with the DIFFERENTIAL OPERATOR derived from the
  constraint produces a SECOND DERIVATIVE (or second-order) term that involves the gauge
  field strength `F_mu_nu` -- a zero-order field -- but the result is a FIRST-ORDER
  equation in the NEW variable `chi = gamma^mu psi_mu` (which should be zero but is
  driven by `F_mu_nu psi`).
- The effective operator for `chi` has characteristics determined by `F_mu_nu`, which
  can be spacelike.

**GU RS sector (non-standalone):**

- The RS field is a sub-bundle of the Clifford module, NOT a standalone field with its
  own Lagrangian.
- There is NO separate constraint equation derived by varying a Lagrangian. The constraint
  `Gamma^{14D} Psi = 0` is the definition of the domain.
- The effective RS operator `S_R^{full}` is derived by Schur complement elimination of the
  Q sector -- not by acting with a differential operator on the RS equation.
- The Schur complement operation is a purely ALGEBRAIC (at the symbol level) / PSEUDODIFFERENTIAL
  operation, not a physical differentiation of the field equation. It does not produce new
  first-order terms from zero-order curvature.
- Therefore, the Weyl tensor of `g_Y` cannot produce new first-order terms in `S_R^{full}`
  via the Schur complement mechanism.

This structural difference -- Schur complement vs. subsidiary condition differential operator --
is why the lower-order curvature mechanism fails to operate in the GU RS sector.

---

## 8. Residual Risk: Non-Minimal Coupling and Obstruction

### 8.1 Pauli-Type Non-Minimal Coupling

The D_GU operator includes the Shiab term `Phi(F_A tensor Psi)`. This is a non-minimal
coupling involving the Sp(64) gauge curvature `F_A` (a two-form). In the standard spin-3/2
theory, non-minimal couplings of the form `mu F_mu_nu Sigma^{mu nu} psi` (Pauli-type) can
modify the effective characteristic cone.

**For D_GU, the Shiab term is:**

```
Phi(F_A tensor Psi)_B = sum_C e^C_B c(\iota_{e_C} F_A) Psi_B
```

This is a zero-order multiplication operator (F_A multiplied by a Clifford element). It
does NOT contribute to the principal symbol.

However, one might ask: does the Shiab term produce an effective "Pauli term" at the
level of the D_GU^2 operator? The square of D_GU:

```
D_GU^2 = (nabla^A nabla_A) Id + R/4 + (gauge F terms) + (Shiab^2 terms) + ...
```

The Lichnerowicz-Weitzenbock formula for a Dirac-type operator gives a zero-order correction
from the Ricci scalar and gauge field strength. The characteristic set of `D_GU^2` is still
determined by the principal symbol `sigma_2(D_GU^2)(xi) = g_Y(xi,xi)^2 Id`, which remains
the null cone squared. Zero-order corrections do not change this.

### 8.2 Degenerate Backgrounds (Extreme Curvature)

For backgrounds where the Weyl tensor of `g_Y` becomes very large (e.g., near a curvature
singularity), the zero-order corrections to `S_R^{full}` become large. In principle, if
the zero-order corrections are larger than the principal-symbol contribution (i.e., if
we are working at sub-Compton wavelengths in the curvature background), the perturbative
analysis breaks down.

**But:** This is a question about the validity of the EFT at those scales, not about
the characteristic cone. The characteristic cone is a property of the PRINCIPAL symbol,
which is independent of the zero-order terms.

At length scales much longer than the curvature radius of `g_Y` (the semiclassical regime),
the zero-order curvature corrections are small and the principal-symbol result dominates.
VZ evasion holds in the semiclassical regime.

At length scales comparable to or shorter than the curvature radius (trans-Planckian), the
EFT description breaks down. But this is a generic problem for any quantum field theory in
a strongly curved background, not a specific VZ pathology.

### 8.3 Potential Gap: The Schur Complement is a Pseudodifferential Operator

The full `S_R^{full}` is not a differential operator but a **pseudodifferential** operator
(because it involves `(E^{full})^{-1}`, which is a pseudodifferential inverse). For
pseudodifferential operators, the characteristic analysis is more subtle: one must use the
**full symbol** (including sub-leading terms in the asymptotic expansion), not just the
principal symbol.

**Argument that this does not introduce acausality:**

For a pseudodifferential operator `S_R^{full}$ of order 1, the full symbol expansion is:

```
sigma(S_R^{full})(x, xi) = sigma_1(x, xi) + sigma_0(x, xi) + sigma_{-1}(x, xi) + ...
```

The microlocal characteristics (the WF set, which determines propagation of singularities)
of `S_R^{full}$ are determined by the zeros of `sigma_1(x, xi)` -- the PRINCIPAL symbol --
up to corrections from lower-order terms. The lower-order terms `sigma_0, sigma_{-1}, ...`
affect the amplitude and regularity of solutions but NOT the direction of propagation (the
WF set) at leading order.

**Propagation of singularities theorem** (Hormander): For a pseudodifferential operator P
of real principal type, the WF set of solutions propagates along null bicharacteristics of
the PRINCIPAL symbol. The sub-leading terms affect whether the solutions are smooth or not,
but not the direction of propagation.

Since `sigma_1(S_R^{full}) = sigma_1(S_R^{(0)})$ has null cone characteristics (as proved
in vz-schur-complement), the WF set of solutions to `S_R^{full} Psi = 0` propagates along
null bicharacteristics of the gimmel metric `g_Y`. No spacelike propagation occurs.

This is the theorem-grade version of the lower-order curvature protection argument.

---

## 9. Verdict

**Does the Weyl tensor of the gimmel metric reintroduce spacelike characteristics via lower-order terms?**

**Answer: No, at reconstruction grade.**

The argument has three levels:

**Level 1 (direct symbol argument, §5.4):**
Zero-order curvature corrections to D_GU do not change the principal symbol of the
effective RS operator `S_R^{full}`. The characteristic set is determined by the principal
symbol, which equals the null cone (from vz-schur-complement). Lower-order curvature
cannot enlarge the characteristic cone.

**Level 2 (structural argument, §7.3):**
The GU mechanism differs structurally from classical VZ: the RS constraint is not a
separately imposed subsidiary condition but defines the domain of the field. The classical
VZ lower-order mechanism requires acting with a differential subsidiary-condition operator
on the field equation, which generates new first-order terms from zero-order curvature.
In GU, the analogous operation is the Schur complement (a pseudodifferential elimination),
which does not generate new first-order terms from zero-order curvature.

**Level 3 (propagation of singularities, §8.3):**
For the pseudodifferential operator `S_R^{full}`, the propagation of singularities theorem
(Hormander, real principal type) guarantees that solutions propagate along null
bicharacteristics of the principal symbol. Sub-leading terms affect amplitudes but not
directions of propagation.

**Failure conditions:**

**F1.** If D_GU is NOT of Dirac type (i.e., if the Shiab term produces additional first-order
derivative terms that are NOT captured by the principal symbol `sigma_D(xi)^2 = xi2 Id`), the
entire argument fails. The check: the Shiab `Phi(F_A tensor Psi)` is a ZERO-order operator
(F_A is the curvature, a zero-form-valued 2-form, not containing a derivative of Psi). If the
Shiab somehow contained a derivative of Psi (e.g., via a Bianchi identity substitution), this
would need to be revisited. This is the main unverified step.

**F2.** If the pseudodifferential operator `(E^{full})^{-1}$ does not exist as a bounded
operator (i.e., if E^{full} is not elliptic after including curvature corrections), the
Schur complement `S_R^{full}` is not well-defined. E^{full} is elliptic (det(E) = -(xi^2/14)
from the principal symbol), and zero-order corrections do not destroy ellipticity for large
xi (since the principal symbol dominates). For small xi (low momenta), the zero-order terms
could potentially make E^{full} singular -- but this is a mass-gap condition, not a VZ
acausality.

**F3.** If the gimmel metric `g_Y` has a signature change (i.e., if at some region of Y^{14}
the metric degenerates or changes from (9,5)), the propagation of singularities theorem for
real principal type operators would need to be replaced with a degenerate version. The gimmel
metric signature is (9,5) by construction (N1) and is non-degenerate everywhere on Met(X^4).

**F4.** If the sub-leading symbol `sigma_0(S_R^{full})$ (the next-to-leading term in the
pseudodifferential expansion) introduces new real characteristics (a phenomenon called
"subprincipal symbol acausality"), this would need separate analysis. For Dirac-type operators,
the subprincipal symbol is typically zero or is a scalar multiple of the identity, which
does not introduce new characteristics. But for the non-standard RS Schur complement, this
is not immediately clear.

---

## 10. Open Questions

**OQ2-a.** Is the Shiab term `Phi(F_A tensor Psi)` strictly zero-order (no hidden derivatives
of Psi)? This requires checking that the Bianchi identity `D_A F_A = 0` does not introduce
derivative terms when F_A is expanded in the field equations. At the symbol level this is
clear; at the full operator level it requires checking the GU Lagrangian.

**OQ2-b.** Subprincipal symbol analysis: what is `sigma_0(S_R^{full})`? Does it introduce
any real characteristics beyond the null cone? For the standard Dirac operator on a Clifford
bundle, the subprincipal symbol is zero (the connection contributes only to the zero-order
term, not to the subprincipal symbol, in Hormander's calculus). For the modified D_GU with
the Shiab coupling, this should be checked.

**OQ2-c.** The propagation of singularities theorem applies to operators of "real principal
type" (i.e., operators whose principal symbol is real-valued and its gradient is nowhere
proportional to the characteristic covector on the characteristic set). Is `S_R^{full}` of
real principal type? The principal symbol `det(sigma_1(S_R^{full})) = (xi2)^r` (for some r)
is a real polynomial in xi, and its characteristic set is the null cone, which is a smooth
manifold. Real principal type is satisfied if the gradient of `det(sigma_1)` is transverse
to the null cone -- this is the standard condition for the wave operator, which is satisfied
for non-degenerate metrics. For `g_Y` of signature (9,5) with a non-degenerate null cone,
this holds.

**OQ3** (from vz-schur-complement §12 F4): Does the section pullback `s*(D_GU)` preserve the
Clifford module property? If yes, the 4D observable RS field inherits VZ evasion including
lower-order curvature protection. This is a Codazzi equation question (requires the Codazzi
computation from explorations/codazzi-sp64-bundle-2026-06-23.md).

---

## 11. Summary Table

| Curvature Type | Where It Appears in D_GU | Order | Effect on Char. Cone |
|---|---|---|---|
| Weyl tensor W_{ABCD} of g_Y | Spin connection omega_A; commutator [nabla, nabla] | Zero-order (multiplication) | None -- no change to principal symbol |
| Ricci tensor Ric_{AB} of g_Y | Lichnerowicz-Weitzenbock formula for D_GU^2 | Zero-order | None |
| Riemann tensor R_{ABCD} of g_Y | Constraint commutator [D_GU, Gamma^{14D}] | Zero-order | None |
| Sp(64) gauge curvature F_A | Shiab term Phi(F_A tensor Psi) | Zero-order | None |
| Section curvature II_s | 4D pullback of the 14D operator | Zero-order in 4D | OQ3 (conditional) |

All curvature contributions to D_GU are zero-order operators. None change the principal symbol.
None can enlarge the characteristic cone beyond the null cone.

**Verdict: CONDITIONALLY_RESOLVED.**

Lower-order curvature terms in D_GU (including the Weyl tensor of the gimmel metric) do NOT
reintroduce spacelike characteristics. VZ evasion at the principal-symbol level (EVADED,
vz-schur-complement) survives the inclusion of lower-order curvature corrections at reconstruction
grade. The residual conditions (OQ2-a, OQ2-b) require checking the Shiab zero-order structure
and the subprincipal symbol.

---

## 12. Relation to the VZ Tracking Table

| Claim | Status |
|---|---|
| VZ evasion at principal-symbol level (all 14D covectors) | EVADED reconstruction (vz-schur-complement) |
| S_R^2 = xi^2 Id as exact matrix identity | FALSE (vz-oq1) -- A S_R = xi^2 Id is correct |
| Lower-order curvature reintroduces spacelike chars | FALSE at reconstruction grade (this note) |
| Lower-order curvature: Shiab term is zero-order (no hidden derivatives) | ASSUMED, needs verification (OQ2-a) |
| Subprincipal symbol acausality | NOT ANALYZED -- needs separate check (OQ2-b) |
| Section-pullback 4D VZ evasion | OPEN -- depends on Codazzi (OQ3 from parent) |
| EFT decoupling producing standalone RS at low energy | OPEN -- F6 from parent |

---

## References

- `explorations/vz-schur-complement-2026-06-23.md` (parent -- VZ EVADED at principal-symbol level)
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md` (S_R^2 != xi^2 Id; A S_R = xi^2 Id)
- `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` (VZ setup and OQ2 statement)
- `explorations/hc1-hidden-curvature-components-2026-06-22.md` (6-piece curvature decomp)
- `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md` (SL(2,C) labels for H^(i))
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) algebra)
- `explorations/codazzi-sp64-bundle-2026-06-23.md` (4D reduction, OQ3 context)
- Velo and Zwanziger (1969), Phys. Rev. 186:1337 (original VZ mechanism)
- Hormander (1985), _The Analysis of Linear Partial Differential Operators III_, Ch. 23
  (propagation of singularities for real principal type operators)
- Lawson-Michelsohn, _Spin Geometry_, Ch. II (Clifford module Dirac operators)
- Johnson and Sudarshan (1961), Ann. Phys. 13:126 (constraint analysis for RS fields)
