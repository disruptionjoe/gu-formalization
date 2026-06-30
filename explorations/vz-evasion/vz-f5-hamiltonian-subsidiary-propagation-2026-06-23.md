---
title: "VZ F5: Full Constrained-Hamiltonian Analysis of Subsidiary-Condition Propagation under Sp(64) Gauge Curvature"
date: 2026-06-23
problem_label: "vz-f5-hamiltonian-subsidiary-propagation"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ F5: Constrained-Hamiltonian Subsidiary-Condition Propagation

## 1. Problem Statement

**What is being computed.** The VZ evasion at the 4D principal-symbol level (OQ3-V1/V2/V3,
VERIFIED) and the zero-order curvature non-reintroduction check (vz-f5-curvature-check,
CONDITIONALLY_RESOLVED) establish that the effective RS operator `S_R^{4D,full}` has
causal characteristics. These are symbol-level statements.

The open gate in the no-go canon (canon/no-go-class-relative-map.md, F5 row) is:

> **The constrained-Hamiltonian propagation of the subsidiary condition `Gamma^{4D} psi = 0`
> in an Sp(64) background: residual open at full dynamical level.**

This asks: in the Dirac-Bergmann constrained Hamiltonian framework applied to the 4D
effective RS dynamics, does the subsidiary condition (gamma-trace constraint)
`Gamma^{4D} Psi_R = 0` remain preserved under time evolution when `F_A != 0`?

**Clear failure condition.** If the secondary Dirac-Bergmann consistency condition
(preservation of primary constraints under H_GU evolution) fails when `F_A != 0`, then
the VZ evasion holds at the principal-symbol level but fails at the dynamical level.
This would be a genuine GENUINE_OBSTRUCTION.

**Why this is distinct from the prior curvature check.** The prior F5 file
(vz-f5-curvature-check) showed that curvature terms are zero-order in the RS field and
do not affect the principal symbol. But the Dirac-Bergmann question is different: even
zero-order terms (entering the Hamiltonian as potentials) can prevent constraint surfaces
from being invariant under the Hamiltonian flow if those zero-order terms produce
nonvanishing Poisson brackets with the constraints.

---

## 2. Established Context

**Results this builds on:**

- `vz-schur-complement-2026-06-23.md` §17-19: 4D VZ evasion CONDITIONALLY_RESOLVED at principal-symbol
  level. The 4D gamma-trace constraint `Gamma^{4D}` is intrinsic to the Clifford module
  structure; the RS sub-bundle `R_s = ker Gamma^{4D}` is defined by a Clifford algebraic
  condition, not an external Lagrange multiplier.

- `vz-f5-curvature-check-2026-06-23.md`: All curvature terms (Weyl, Riemann, Sp(64)
  gauge curvature F_A, second fundamental form II_s) are zero-order operators in the 4D
  field. They contribute to the Hamiltonian as potential terms.

- `vz-oq2-lower-order-curvature-2026-06-23.md`: The GU RS sector is a sub-bundle, not
  a standalone field. The gamma-trace constraint is domain-defining. The classical VZ
  lower-order mechanism requires a secondary equation derived by acting with a differential
  operator on an externally-imposed subsidiary condition; this structure is absent in GU.

- `canon/no-go-class-relative-map.md` §2.5: F5 row explicitly states the constrained-
  Hamiltonian propagation is "residual open at full dynamical level."

---

## 3. Dirac-Bergmann Framework Setup for the GU RS Sector

### 3.1 The Classical VZ Constraint Propagation Mechanism

In the **classical VZ setup**, the Rarita-Schwinger field `psi_mu` (a spinor-valued
1-form on X^4) has the following structure:

1. **Primary constraint (subsidiary condition):** `phi_1 = gamma^mu D_mu psi_0 approx 0`
   (from the E-L equations of the RS Lagrangian; this is the subsidiary condition).
2. **Consistency condition:** `{phi_1, H_RS} approx 0` (preservation under RS Hamiltonian
   flow; this generates a secondary constraint `phi_2`).
3. **VZ obstruction:** `phi_2` contains `F_{mu nu}` terms at first order in the
   derivatives of `psi`, making `phi_2` a genuine new constraint. For non-abelian
   `F_{mu nu}`, `phi_2` is inconsistent with `phi_1` (the constraint surface is empty),
   producing the VZ pathology.

The key structural feature of classical VZ: the subsidiary condition `phi_1` is
**derived** from the RS Lagrangian via the E-L equations. It is an **external**
constraint imposed on top of the dynamics. The Dirac-Bergmann consistency requires it
to be preserved by the Hamiltonian; the gauge coupling `F_{mu nu}` enters in the
consistency check at first order because acting with a derivative on `phi_1` generates
a commutator `[D_mu, D_nu] psi = F_{mu nu} psi`.

### 3.2 The GU Hamiltonian Structure

The GU 4D effective Hamiltonian is derived from the 4D operator `D_GU^{4D}` by
3+1 decomposition. Let `X^4 = R x Sigma` (or a globally hyperbolic slicing of the
physical 4D spacetime) with time coordinate `t` and spatial slice `Sigma`.

**3+1 decomposition of `D_GU^{4D}`:**

Choose a future-directed timelike unit vector field `n^mu` (the unit normal to the
spatial slices). The 4D Dirac operator decomposes as:

```
D_GU^{4D} = gamma^0 (partial_t + A_0 + omega^{4D}_0) + gamma^i (nabla^{4D}_i)
           + (Shiab pullback terms)
           + (zero-order curvature terms)
```

where:
- `gamma^0 = c_s(n)` is the Clifford action of the unit normal
- `gamma^i` are the spatial Clifford elements
- `A_0, omega^{4D}_0` are the temporal components of the Sp(64) connection and spin
  connection respectively

The **GU Hamiltonian density** for the spinor field `Psi` is:

```
H_GU = Psi^dagger [-(gamma^0)^{-1}(gamma^i nabla^{4D}_i + A_0 + omega^{4D}_0
       + Shiab + V_curv)] Psi
```

where `V_curv` is the zero-order potential from gauge and Riemann curvature.

For the RS sector specifically, `Psi_R in Gamma(R_s)` where `R_s = ker Gamma^{4D}`.

### 3.3 The Subsidiary Condition as a Dirac-Bergmann Constraint

**Critical structural point:** In GU, the gamma-trace constraint `Gamma^{4D} Psi = 0`
is **not** derived from an RS Lagrangian via E-L equations. It is the **definition** of
the RS sub-bundle:

```
R_s = ker Gamma^{4D} = {Psi in Gamma(E_s) : Gamma^{4D} Psi = 0}
```

This is a **kinematic** constraint, not a **dynamical** constraint. In Dirac-Bergmann
language, this is a **primary kinematic constraint** that holds by definition for all
configurations in the state space of the RS sector -- not as an equation of motion.

**The Dirac-Bergmann analysis applies to dynamical constraints** (constraints that arise
as consistency conditions for the E-L equations, not constraints that define the field
content). The GU RS constraint `Gamma^{4D} Psi_R = 0` is of the kinematic type.

This is the structural key that we now make precise.

---

## 4. The Constrained-Hamiltonian Analysis

### 4.1 Two Types of Constraints in the Dirac-Bergmann Framework

Recall the Dirac-Bergmann classification:

- **Kinematic/configuration-space constraints:** Restrict which configurations are
  physically admissible. These constrain the field content before dynamics is specified.
  They are not preserved or violated by the Hamiltonian -- they define the phase space.
- **Dynamical/first-class constraints:** Arise from the E-L equations (primary
  constraints) or their consistency conditions (secondary constraints). These must be
  preserved under Hamiltonian evolution, generating the Dirac-Bergmann consistency chain.

The VZ obstruction is a failure at the level of **dynamical constraints**: the
subsidiary condition of the RS Lagrangian (the gamma-trace of the E-L equations) is a
dynamical constraint that fails to be preserved when `F_{mu nu} != 0`.

**In GU:**

The gamma-trace `Gamma^{4D} Psi_R = 0` is a **configuration-space constraint** -- it
defines which fields `Psi` are RS fields. It does not arise as an equation of motion.
There is no separate RS Lagrangian from which it is derived.

The **dynamical constraint** in GU (the constraint that must be preserved by `H_GU`)
is the **field equation** `D_GU^{4D} Psi = 0` itself, restricted to initial data
satisfying the kinematic constraint.

### 4.2 Phase Space of the GU RS Sector

The phase space of the GU RS sector is:

```
Gamma_RS = {(Psi_R, pi_R) : Psi_R in Gamma(R_s), pi_R in Gamma(R_s^*)}
```

where `pi_R = (partial L_GU / partial (partial_t Psi_R))` is the conjugate momentum.

**The kinematic constraint `Gamma^{4D} Psi_R = 0` is satisfied identically on `Gamma_RS`
by definition.** There is no condition to preserve -- it is built into the definition of
the phase space.

**Proof.** For any `Psi_R in Gamma(R_s)`, we have `Gamma^{4D} Psi_R = 0` by definition
of `R_s = ker Gamma^{4D}`. Time evolution by `H_GU` maps `Psi_R(t)` to `Psi_R(t + dt)`.
For the constraint to be preserved, we need:

```
Gamma^{4D} Psi_R(t + dt) = 0
```

This holds if and only if `Psi_R(t + dt) in Gamma(R_s)`, i.e., if time evolution maps
the RS sub-bundle to itself.

### 4.3 Does `H_GU` Preserve the RS Sub-Bundle `R_s`?

This is the central Dirac-Bergmann question for GU. We ask: does time evolution under
`D_GU^{4D}` (equivalently, under `H_GU`) map RS configurations to RS configurations?

**The GU time evolution equation:**

```
partial_t Psi = -(gamma^0)^{-1}(gamma^i nabla_i + A_0 + ...) Psi    [GU field eq]
```

For `Psi_R in Gamma(R_s)` (with `Gamma^{4D} Psi_R = 0`), the question is whether

```
Gamma^{4D} (partial_t Psi_R) = 0
```

**Computation:**

```
Gamma^{4D} (partial_t Psi_R)
= Gamma^{4D} [-(gamma^0)^{-1}(gamma^i nabla_i + A_0 + V_curv) Psi_R]
= -(gamma^0)^{-1} Gamma^{4D} [gamma^i nabla_i + A_0 + V_curv] Psi_R   (*)
```

where in (*) we use the fact that `Gamma^{4D}` and `(gamma^0)^{-1}` commute (both are
Clifford module operations, and Clifford multiplication is associative).

**The key commutator:**

```
[Gamma^{4D}, D_GU^{4D}] Psi_R
= Gamma^{4D}(D_GU^{4D} Psi_R) - D_GU^{4D}(Gamma^{4D} Psi_R)
= Gamma^{4D}(D_GU^{4D} Psi_R) - D_GU^{4D}(0)
= Gamma^{4D}(D_GU^{4D} Psi_R)
```

If `D_GU^{4D} Psi_R = 0` (i.e., `Psi_R` is a solution to the field equation), then

```
Gamma^{4D}(partial_t Psi_R) = 0
```

**automatically**, independent of `F_A`.

### 4.4 The Commutator `[Gamma^{4D}, D_GU^{4D}]` at Operator Level

For **arbitrary** `Psi_R in Gamma(R_s)` (not necessarily satisfying the field equation),
we need to compute whether the constraint is preserved dynamically.

The question becomes: does `D_GU^{4D}` map `Gamma(R_s)` to `Gamma(R_s)`?

**Answer: No, by construction.** The operator `D_GU^{4D}` maps sections of `E_s` to
sections of `E_s`, and `R_s subset E_s` is a sub-bundle, but `D_GU^{4D}` generically
maps RS sections to non-RS sections. This is the **off-diagonal coupling** B and C in
the block decomposition.

The GU field equation `D_GU^{4D} Psi = 0` is the full constraint. For a solution
`Psi = Psi_R + Psi_Q` (RS + non-RS components), the field equation mixes both components:

```
A Psi_R + B Psi_Q = 0   [RS equation]
C Psi_R + E Psi_Q = 0   [non-RS equation]
```

Initial data that is purely RS (`Psi_Q = 0` at t=0) does NOT remain purely RS under
evolution: the RS equation requires `A Psi_R + B Psi_Q = 0`, so if `Psi_Q = 0` then
`A Psi_R = 0`. For non-null covectors this forces `Psi_R = 0` (by the Clifford identity).

**This is correct physics:** a purely RS configuration at t=0 does not exist as an
on-shell solution unless `Psi_R = 0`. The physical content of the RS sector lives in
the interplay between `Psi_R` and `Psi_Q` coupled by D_GU^{4D}. The kinematic
separation `Psi = Psi_R + Psi_Q` is an algebraic decomposition, not a physical sector
separation.

### 4.5 Resolution via Schur Complement: The Correct Constraint Structure

The correct Hamiltonian analysis for the GU RS sector is not the preservation of
`Gamma^{4D} Psi_R = 0` as an independent dynamical constraint, but rather the analysis
of the **Schur complement dynamics** for the RS sector after eliminating `Psi_Q`.

**Step 1: Eliminate `Psi_Q` via the non-RS equation.**

From `C Psi_R + E Psi_Q = 0` (the Q-sector field equation), for non-null covectors where
`E` is invertible:

```
Psi_Q = -E^{-1} C Psi_R
```

**Step 2: Substitute into the RS equation.**

```
A Psi_R + B(-E^{-1} C Psi_R) = 0
(A - B E^{-1} C) Psi_R = 0
S_R Psi_R = 0
```

where `S_R = A - B E^{-1} C` is the Schur complement. This is the **dynamical equation
for `Psi_R`** after elimination of the non-RS sector.

**Step 3: Hamiltonian form of the Schur complement dynamics.**

The 3+1 decomposition of `S_R Psi_R = 0` gives:

```
partial_t Psi_R = H_RS Psi_R
```

where `H_RS` is the effective RS Hamiltonian derived from the 4D form of `S_R`:

```
H_RS = -(gamma^0_R)^{-1}(gamma^i_R nabla_i + (B E^{-1} C)^{(1)}_i nabla^i + V_RS)
```

Here:
- `(gamma^0_R)^{-1}` is the time Clifford element restricted to the RS sector
- `(B E^{-1} C)^{(1)}_i` is the first-order part of the Schur complement (from spatial
  derivatives in the B and C blocks)
- `V_RS` is the zero-order effective potential for the RS sector (includes F_A, R_{g_s},
  II_s contributions -- all zero-order in Psi_R, as established in vz-f5-curvature-check)

**Step 4: The constraint structure in the Schur complement framework.**

In the Schur complement description, there is **no subsidiary condition** to preserve.
The RS field `Psi_R in Gamma(R_s)` lives in the sub-bundle `R_s = ker Gamma^{4D}` by
definition. The Schur complement equation `S_R Psi_R = 0` is the complete dynamics on
`Gamma(R_s)`. There are no additional Dirac-Bergmann constraints to check.

The Dirac-Bergmann consistency chain terminates at the first step: there are no
primary dynamical constraints (only the kinematic constraint `Gamma^{4D} Psi_R = 0`,
which is satisfied by definition), and therefore no secondary constraints are generated.

### 4.6 The `F_A != 0` Case

Now we address the central question: when `F_A != 0`, does anything change in the above
analysis?

**F_A enters the Hamiltonian in two places:**

**(a) In the connection term `A_0`:** The temporal component `A_0^{Sp(64)}` of the
Sp(64) connection enters `H_GU` as a first-order coupling. Under time evolution:

```
partial_t Psi_R = ... - (gamma^0_R)^{-1} A_0^{Sp(64)} Psi_R
```

This contributes to `Gamma^{4D}(partial_t Psi_R)` as:

```
Gamma^{4D}(-(gamma^0_R)^{-1} A_0 Psi_R) = -(gamma^0_R)^{-1} [Gamma^{4D}, A_0] Psi_R
                                           - (gamma^0_R)^{-1} A_0 (Gamma^{4D} Psi_R)
                                           = -(gamma^0_R)^{-1} [Gamma^{4D}, A_0] Psi_R
```

since `Gamma^{4D} Psi_R = 0`. The commutator `[Gamma^{4D}, A_0]` is:

```
[Gamma^{4D}, A_0] = Gamma^{4D} A_0 - A_0 Gamma^{4D}
```

`Gamma^{4D} = gamma^mu_H n^{4D}_mu` (the contracted gamma-trace operator). `A_0` acts
on the gauge (Sp(64)) indices. **These act on different index sets:** `Gamma^{4D}` acts
on Clifford (spinor-vector) indices, while `A_0` acts on the Sp(64) gauge indices of
the same section.

For sections of `E_s = S tensor ad(P_s)`:

```
[Gamma^{4D}, A_0](Psi_R) = Gamma^{4D}(A_0 . Psi_R) - A_0 . (Gamma^{4D} Psi_R)
```

The gauge action `A_0 . Psi_R` is via the Sp(64) representation on `S tensor ad(P_s)`:
it acts as `(Id_S tensor ad(A_0)) Psi_R`. The gamma-trace `Gamma^{4D}` acts on the
`S` factor. Since `Id_S tensor ad(A_0)` acts only on the gauge index and `Gamma^{4D}`
acts only on the spinor index, **they commute:**

```
[Gamma^{4D}, A_0] = 0
```

**Therefore:**

```
Gamma^{4D}(-(gamma^0_R)^{-1} A_0 Psi_R) = 0
```

The temporal gauge connection term does not violate the constraint, regardless of F_A.

**(b) In the zero-order potential `V_RS` (from F_A via Shiab):**

The Shiab contribution `Phi(s*(F_A) tensor Psi_R)` at zero order acts as:

```
Shiab: Psi_R mapsto sum_a e^a tensor c(iota_{e_a} s*(F_A)) . Psi_R
```

This is a Clifford multiplication by `s*(F_A)` on the Clifford index, combined with
the gauge action. The gamma-trace of this term:

```
Gamma^{4D}(Phi(F_A tensor Psi_R))
= Gamma^{4D}(sum_a e^a tensor c(iota_{e_a} F_A) . Psi_R)
= sum_a (Gamma^{4D} e^a) tensor c(iota_{e_a} F_A) . Psi_R
  + sum_a e^a tensor Gamma^{4D}(c(iota_{e_a} F_A) . Psi_R)    (*)
```

In (*), the first term vanishes since `Gamma^{4D}` acts on sections (not on form labels),
and the second term involves `Gamma^{4D}(c(iota_{e_a} F_A) . Psi_R)`.

By the Leibniz rule for Clifford multiplication:

```
Gamma^{4D}(c(F) . psi) = [Gamma^{4D}, c(F)] psi + c(F) . Gamma^{4D} psi
```

The second term vanishes since `Gamma^{4D} Psi_R = 0`. The first term is the Clifford
commutator `[Gamma^{4D}, c(F)]`, which by the Clifford algebra relations equals a
combination of Clifford multiplications by contractions of `F` with the gamma-trace
covector. This is a zero-order operator (no derivatives of `Psi_R`). It is generically
nonzero.

**The Shiab commutator with `Gamma^{4D}`:**

```
[Gamma^{4D}, c(iota_{e_a} F_A)] = Gamma^{4D} c(iota_{e_a} F_A) - c(iota_{e_a} F_A) Gamma^{4D}
```

Using the Clifford relation `{c(alpha), c(beta)} = 2g(alpha, beta)` (anticommutator):

```
Gamma^{4D} = gamma^mu_H n_mu    [contracted gamma-trace]
c(iota_{e_a} F_A) = gamma^{mu nu}_H F_{a,mu nu}    [Clifford product of F]
```

The commutator `[gamma^mu_H n_mu, gamma^{rho sigma}_H F_{rho sigma}]` in the Clifford
algebra is:

```
[gamma^mu, gamma^{rho sigma}] = gamma^mu gamma^{rho sigma} - gamma^{rho sigma} gamma^mu
= g^{mu rho} gamma^sigma - g^{mu sigma} gamma^rho    [by Clifford relations]
```

(schematically; the exact form follows from the Clifford algebra `{gamma^mu, gamma^nu} = 2g^{mu nu}`).

**This is a nonzero Clifford element in general.** Therefore:

```
[Gamma^{4D}, Phi(F_A tensor .)] Psi_R != 0    (generically when F_A != 0)
```

This means the Shiab term in `partial_t Psi_R` produces a component that does NOT lie
in `ker Gamma^{4D}`, i.e., the time derivative of an RS field leaves the RS sub-bundle.

**Honest reading of this result (do not skip).** In the CLASSICAL VZ analysis, this exact
fact — the gamma-trace constraint is not preserved under time evolution once `F_A != 0`
— **is the obstruction signature.** Non-preservation of the subsidiary condition under
gauge coupling is precisely what generates the inconsistent secondary constraint and the
acausal/ill-posed characteristic surface. The present file does not make this result
disappear; it **reinterprets** it as benign in §4.7 and §4.11. That reinterpretation is
valid **only if** the Schur-complement system (RS field with `Psi_Q` slaved, no standalone
RS Lagrangian and hence no externally-imposed subsidiary condition to propagate) is the
correct and complete dynamics of the GU RS sector. That premise is exactly **FC1** (no
standalone GU RS Lagrangian), and **FC1 is OPEN**: the file establishes only that no such
Lagrangian has been *identified* (§7, FC1), which is absence of identification, not proof
of absence. Consequently the §4.6(b) non-preservation result is the obstruction signature
under the classical reading and is benign only under the FC1-conditional Schur-complement
reading. The verdict of this file is therefore **assumption-conditional on FC1**, not a
free-standing derivation. Every "automatically / by construction / by definition /
trivially" escape phrase below presupposes the Schur-complement reframing and therefore
inherits this FC1-conditionality.

### 4.7 Resolution: This is Not a VZ Obstruction (Conditional on FC1)

**The above result (4.6(b)) IS the VZ obstruction signature under the classical reading,
and is benign ONLY IF the Schur-complement system is the correct dynamics — which is FC1,
and FC1 is open.** Here is the conditional argument:

**The Schur complement is the correct framework — IF FC1 holds.** The conclusion from §4.5 is that the
GU RS sector is described not by `Gamma(R_s)` alone but by the Schur complement dynamics
on `Gamma(R_s)`. The Schur complement `S_R Psi_R = 0` already incorporates the coupling
to the non-RS sector (the Psi_Q sector via the B and C blocks).

**The `Psi_Q` component is slaved to `Psi_R`:** In the Schur complement description,
`Psi_Q = -E^{-1} C Psi_R` is determined algebraically by `Psi_R`. The full field
`Psi = Psi_R + Psi_Q = Psi_R - E^{-1} C Psi_R` satisfies `D_GU^{4D} Psi = 0`
if and only if `S_R Psi_R = 0`.

**Under time evolution of the full field `Psi`:**

```
partial_t Psi = H_GU Psi
partial_t (Gamma^{4D} Psi) = Gamma^{4D} partial_t Psi = Gamma^{4D}(H_GU Psi)
```

For a solution `Psi` to the full field equation `D_GU^{4D} Psi = 0`:

The 3+1 split of `D_GU^{4D} Psi = 0` is:

```
gamma^0 partial_t Psi = -gamma^i nabla_i Psi - (A_0 + V) Psi
partial_t Psi = -(gamma^0)^{-1}(gamma^i nabla_i + A_0 + V) Psi
```

Taking the gamma-trace of the equation `D_GU^{4D} Psi = 0`:

```
Gamma^{4D}(D_GU^{4D} Psi) = 0
```

This is automatically zero if `D_GU^{4D} Psi = 0` (trivially). The gamma-trace of a
solution is preserved by the field equation. Now decompose:

```
0 = Gamma^{4D}(D_GU^{4D} Psi)
  = Gamma^{4D}(gamma^0 partial_t Psi) + Gamma^{4D}(gamma^i nabla_i Psi) + ...
```

This gives a consistency relation between `partial_t(Gamma^{4D} Psi)` and spatial
derivatives of `Gamma^{4D} Psi`, of the form:

```
partial_t(Gamma^{4D} Psi) = (spatial terms in Gamma^{4D} Psi) + (other terms)
```

If `Gamma^{4D} Psi = 0` at t=0, then `partial_t(Gamma^{4D} Psi)` at t=0 involves
spatial derivatives of `Gamma^{4D} Psi` (which vanish) plus additional terms.

**The additional terms: what are they?**

The additional terms come from commuting `Gamma^{4D}` through `D_GU^{4D}`:

```
Gamma^{4D}(D_GU^{4D} Psi) = [Gamma^{4D}, D_GU^{4D}] Psi + D_GU^{4D}(Gamma^{4D} Psi)
```

If `Gamma^{4D} Psi = 0`, this becomes:

```
0 = [Gamma^{4D}, D_GU^{4D}] Psi   (since D_GU^{4D}(0) = 0)
```

**The commutator `[Gamma^{4D}, D_GU^{4D}]` is the constraint propagation operator.**
If this commutator is zero (or proportional to `Gamma^{4D}`), then the constraint is
automatically propagated. If it is nonzero and acts nontrivially, then new constraints
arise.

### 4.8 Computing `[Gamma^{4D}, D_GU^{4D}]`

The 4D operator is:

```
D_GU^{4D} = gamma^mu_H nabla^{4D}_mu + Phi(s*(F_A) tensor .) + V_{curv,0}
```

where `nabla^{4D}_mu = partial_mu + omega^{4D}_mu + A_mu^{Sp(64)}` and `V_{curv,0}`
is the zero-order curvature potential.

**The commutator decomposes as:**

```
[Gamma^{4D}, D_GU^{4D}]
= [Gamma^{4D}, gamma^mu_H nabla^{4D}_mu] + [Gamma^{4D}, Phi(F_A)]
  + [Gamma^{4D}, V_{curv,0}]
```

**Term 1: `[Gamma^{4D}, gamma^mu_H nabla^{4D}_mu]`**

`Gamma^{4D} = n_nu gamma^nu_H` (where `n_nu` is the unit normal covector to the spatial
slice). Using the Clifford anticommutator `{gamma^mu, gamma^nu} = 2g^{mu nu}`:

```
[n_nu gamma^nu, gamma^mu nabla_mu]
= n_nu gamma^nu gamma^mu nabla_mu - gamma^mu n_nu nabla_mu gamma^nu   (*)
```

Since `nabla_mu gamma^nu = 0` (spin connection compatible with Clifford structure in
the Riemannian/Lorentzian sense: `nabla_mu(c(e^nu)) = c(nabla_mu e^nu)` by the
definition of the spin connection), and `nabla_mu n_nu = K_{mu nu}` (the extrinsic
curvature of the slice), we get:

```
[Gamma^{4D}, gamma^mu nabla_mu] = n_nu(gamma^nu gamma^mu - gamma^mu gamma^nu) nabla_mu
                                   + terms involving nabla_mu n_nu
= n_nu [gamma^nu, gamma^mu] nabla_mu + K_{mu nu} gamma^mu gamma^nu
= 2n_nu (g^{nu mu} - gamma^nu gamma^mu) nabla_mu + ... (by Clifford)
```

More precisely, using `gamma^nu gamma^mu = g^{nu mu} - (1/2)[gamma^mu, gamma^nu]`:

```
[n_nu gamma^nu, gamma^mu nabla_mu]
= n_nu (g^{nu mu} - gamma^nu gamma^mu + gamma^mu gamma^nu) nabla_mu + ...
= n_nu g^{nu mu} nabla_mu - n_nu [gamma^nu, gamma^mu] nabla_mu + ...
```

**Algebra-grade caveat.** The first attempt above (the two lines ending in `+ ...`) was
incomplete: it dropped the `nabla_mu n_nu = K_{mu nu}` term and mis-ordered the Clifford
factors. The corrected computation follows. This commutator algebra is reconstruction
grade and has NOT been independently re-derived or CAS-checked; the corrected form below
is used in §4.9–§4.10, so any sign or ordering error there propagates into the propagation
equation (**) and hence into the FC3 (extrinsic-curvature `K_{mu nu}`) analysis. Treat the
`K_{mu nu}` coefficient as unverified at reconstruction grade.

The commutator `[AB, C]` where `B = gamma^nu` and
`C = gamma^mu nabla_mu` is:

```
[n_nu gamma^nu, gamma^mu nabla_mu]
= n_nu gamma^nu gamma^mu nabla_mu - gamma^mu n_nu nabla_mu gamma^nu - gamma^mu gamma^nu nabla_mu n_nu
= n_nu (2g^{nu mu} - gamma^mu gamma^nu) nabla_mu - gamma^mu gamma^nu K_{mu nu}    [using {gamma^nu, gamma^mu} = 2g^{nu mu}]
= 2n^mu nabla_mu - n_nu gamma^mu gamma^nu nabla_mu - gamma^mu gamma^nu K_{mu nu}
= 2n^mu nabla_mu - n_nu (2g^{mu nu} - gamma^nu gamma^mu) nabla_mu - K_{mu nu} gamma^mu gamma^nu
= 2n^mu nabla_mu - 2 n^mu nabla_mu + n_nu gamma^nu gamma^mu nabla_mu - K_{mu nu} gamma^mu gamma^nu
= Gamma^{4D} gamma^mu nabla_mu - K_{mu nu} gamma^mu gamma^nu
```

So `[Gamma^{4D}, gamma^mu nabla_mu] = Gamma^{4D}(gamma^mu nabla_mu) - K_{mu nu} gamma^mu gamma^nu`,
which when acting on `Psi_R in ker Gamma^{4D}` gives:

```
[Gamma^{4D}, gamma^mu nabla_mu] Psi_R
= Gamma^{4D}(gamma^mu nabla_mu Psi_R) - K_{mu nu} gamma^mu gamma^nu Psi_R
```

The first term `Gamma^{4D}(gamma^mu nabla_mu Psi_R)` is not zero in general (it is the
gamma-trace of the spatial derivative term). However, this enters the **Hamiltonian
constraint preservation as follows:**

The field equation constraint is `D_GU^{4D} Psi = 0`. The consistency check asks:
if `Psi = Psi_R + Psi_Q` satisfies this at t=0, does it continue to do so? This is
automatically true by virtue of `D_GU^{4D} Psi = 0` being the field equation -- it
holds at all times for a solution.

**The question is whether the constraint `Gamma^{4D} Psi = 0` (which holds at t=0 for
the initial data `Psi_R` in the RS sub-bundle) continues to hold.**

The 4D propagation theorem states that for the GU operator `D_GU^{4D}` of real principal
type (established in vz-f5-curvature-check §3.5, Argument 1), the gamma-trace constraint
propagates along characteristics. More precisely:

**Claim (Constraint Propagation Theorem):** If `D_GU^{4D} Psi = 0` and
`Gamma^{4D} Psi|_{t=0} = 0`, then `Gamma^{4D} Psi = 0` for all t.

**Proof sketch:** Apply `Gamma^{4D}` to the field equation:

```
Gamma^{4D}(D_GU^{4D} Psi) = 0
[Gamma^{4D}, D_GU^{4D}] Psi + D_GU^{4D}(Gamma^{4D} Psi) = 0
```

Let `phi = Gamma^{4D} Psi`. Then:

```
D_GU^{4D} phi = -[Gamma^{4D}, D_GU^{4D}] Psi    (**)
```

This is an inhomogeneous equation for `phi = Gamma^{4D} Psi`. If the right-hand side
of (**) can be expressed as a zero-order function of `phi` (i.e., the commutator
`[Gamma^{4D}, D_GU^{4D}]` maps sections in `ker Gamma^{4D}` to sections proportional
to `Gamma^{4D} Psi` or zero), then the equation (**) becomes a homogeneous equation
for `phi` with initial condition `phi|_{t=0} = 0`. By uniqueness of solutions to
symmetric hyperbolic systems, `phi = 0` for all t.

### 4.9 The Commutator `[Gamma^{4D}, D_GU^{4D}]` on `ker Gamma^{4D}`

We now compute `[Gamma^{4D}, D_GU^{4D}] Psi_R` for `Psi_R in ker Gamma^{4D}`.

**Key Clifford algebra identity.** In any Clifford module, for the gamma-trace operator
`Gamma = gamma^mu n_mu` (where `n_mu` is a covector):

```
Gamma(gamma^nu u) = gamma^mu n_mu gamma^nu u
= (2g^{mu nu} n_mu - gamma^nu gamma^mu n_mu) u    [Clifford anticommutator]
= 2n^nu u - gamma^nu Gamma u
```

Therefore:

```
[Gamma, gamma^nu] u = Gamma(gamma^nu u) - gamma^nu(Gamma u)
= 2n^nu u - gamma^nu Gamma u - gamma^nu Gamma u
= 2n^nu u - 2 gamma^nu Gamma u
```

When `Gamma u = 0` (u in `ker Gamma`), this simplifies to:

```
[Gamma, gamma^nu] u = 2n^nu u
```

**Applying to the first-order part of `D_GU^{4D}`:**

```
[Gamma^{4D}, gamma^mu nabla_mu] Psi_R
= gamma^mu [Gamma^{4D}, nabla_mu] Psi_R + [Gamma^{4D}, gamma^mu] nabla_mu Psi_R
= gamma^mu [Gamma^{4D}, nabla_mu] Psi_R + 2n^mu nabla_mu Psi_R    [using Gamma^{4D} Psi_R = 0]
```

The term `[Gamma^{4D}, nabla_mu] Psi_R` involves commuting the gamma-trace with the
covariant derivative. This produces curvature terms:

```
[Gamma^{4D}, nabla_mu] Psi_R = [n_nu gamma^nu, nabla_mu] Psi_R
= n_nu [gamma^nu, nabla_mu] Psi_R + (\nabla_mu n_nu) gamma^nu Psi_R
= n_nu c(R_{mu}^nu) Psi_R + K_{mu nu} gamma^nu Psi_R
```

where `R_mu^nu` is the curvature 2-form (acting via the Clifford representation) and
`K_{mu nu}` is the extrinsic curvature of the spatial slice. These are zero-order.

**Therefore:**

```
[Gamma^{4D}, D_GU^{4D}] Psi_R
= 2n^mu nabla_mu Psi_R + (zero-order terms in Psi_R)
  + [Gamma^{4D}, Phi(F_A)] Psi_R + [Gamma^{4D}, V_{curv,0}] Psi_R
```

The `2n^mu nabla_mu Psi_R` term is the **normal derivative** of `Psi_R` (the time
derivative in the 3+1 split). This is a first-order operator.

**Does this invalidate constraint propagation?** No, because this appears in equation
(**) as:

```
D_GU^{4D} phi = -2n^mu nabla_mu Psi_R - (zero-order terms) - [Gamma^{4D}, Phi(F_A)] Psi_R
```

where `phi = Gamma^{4D} Psi`. The right-hand side involves `Psi_R`, which satisfies
the field equation `S_R Psi_R = 0` (the Schur complement). We need to check whether
this source term makes `phi` grow from zero initial data.

**The source term `2n^mu nabla_mu Psi_R`:** Since `Psi_R` satisfies the Schur
complement field equation `S_R Psi_R = 0`, the normal derivative `n^mu nabla_mu Psi_R`
is determined by the spatial derivatives of `Psi_R` via:

```
n^mu nabla_mu Psi_R = -(gamma^0_R)^{-1}(gamma^i nabla_i + V_RS) Psi_R
```

This is determined by `Psi_R` and its spatial derivatives, not by `phi = Gamma^{4D} Psi`.

### 4.10 The Propagation Equation for `phi = Gamma^{4D} Psi`

The equation (**) becomes, using the computation from §4.9:

```
D_GU^{4D} phi = -2 n^mu nabla_mu Psi_R + (zero-order in Psi_R and Psi_Q)
```

Now, `phi = Gamma^{4D} Psi = Gamma^{4D}(\Psi_R + \Psi_Q)`. Since `\Psi_R in ker Gamma^{4D}`,
we have `phi = Gamma^{4D} \Psi_Q`. The equation becomes:

```
D_GU^{4D} (Gamma^{4D} Psi_Q) = -2n^mu nabla_mu Psi_R + (zero-order terms)
```

This is a sourced wave equation for `Gamma^{4D} Psi_Q`. If the initial data has
`Gamma^{4D} Psi|_{t=0} = 0` (i.e., `Psi_Q` is also in `ker Gamma^{4D}` at t=0,
which holds for the RS initial data), the source at t=0 is:

```
source|_{t=0} = -2n^mu nabla_mu Psi_R|_{t=0} + zero-order
```

This is not zero in general. So `phi = Gamma^{4D} Psi` does not remain zero for all t.

**What does this mean physically?** It means that time evolution of the full field
`Psi` starting from RS initial data `Psi_R|_{t=0}` (with `Psi_Q|_{t=0} = 0`) does not
remain in `ker Gamma^{4D}`. The full field develops non-RS components.

**The two readings of this result.** This non-preservation of `Gamma^{4D} Psi = 0` is
the same algebraic fact that, in classical VZ, drives the secondary-constraint
inconsistency and the acausal characteristic surface. Whether it is benign or fatal in
GU depends entirely on which dynamics is correct:

- **Classical/standalone reading (if FC1 fails — a standalone RS Lagrangian exists):**
  `Gamma^{4D} Psi_R = 0` is an externally-imposed subsidiary condition that the dynamics
  must propagate. Its failure to be preserved when `F_A != 0` is the VZ obstruction. This
  would be a GENUINE_OBSTRUCTION.
- **Schur-complement reading (if FC1 holds — no standalone RS Lagrangian):** the gamma-trace
  is a kinematic projector, `Psi_Q` is slaved to `Psi_R`, and on-shell solutions require
  both components. Then the non-preservation is benign: it is just the statement that a
  purely-RS configuration is not on-shell.

**This is the correct and expected behavior ONLY UNDER the Schur-complement reading,
i.e. only if FC1 holds:** the Schur complement dynamics shows that on-shell solutions
require both `Psi_R` and `Psi_Q` components coupled together. The initial condition
`Psi_Q = 0` is inconsistent with the Schur complement field equation unless `Psi_R = 0`
(as shown in §4.4). FC1 (no standalone GU RS Lagrangian) is **open** — see §7 — so this
benign reading is an assumption, not a derivation.

### 4.11 Correct Dirac-Bergmann Statement for GU RS Sector

The Dirac-Bergmann analysis for the GU RS sector must be applied to the **correct
phase space**, which is NOT `{Psi : Gamma^{4D} Psi = 0}` with dynamics generated by
a pure RS Hamiltonian. Instead:

**Phase space:** `Gamma(E_s)` (the full 4D spinor bundle, including both RS and non-RS
components).

**Primary constraints (conditional on FC1):** IF no standalone RS Lagrangian exists (FC1),
then none from the RS sector — the field equation `D_GU^{4D} Psi = 0`
is the full dynamics and there are no additional constraints to preserve. This claim is
load-bearing on FC1, which is open.

**Subsidiary condition (conditional on FC1):** Under FC1, `Gamma^{4D}` is not a primary
constraint in the Dirac-Bergmann sense; it is a **kinematic projector** that defines the
RS sub-bundle algebraically. If FC1 fails, `Gamma^{4D} Psi_R = 0` is instead an
externally-imposed subsidiary condition and the §4.6(b)/§4.10 non-preservation is the VZ
obstruction.

**The RS sector observables** are computed via the Schur complement: physical RS
amplitudes are matrix elements of `S_R(Psi_R, Psi_R')` for `Psi_R, Psi_R'` in the
initial RS data. These are well-defined for initial data in `Gamma(R_s)`, and the
Schur complement `S_R` has causal characteristics (CONDITIONALLY_RESOLVED at 4D, constant-coefficient gauge; OQ3-V1 CONDITIONALLY_RESOLVED, V2/V3 RESOLVED).

**Conclusion (conditional on FC1):** IF FC1 holds, the Dirac-Bergmann consistency chain
for the GU RS sector does not generate the VZ secondary constraint, because there is no
primary dynamical constraint to propagate, and the subsidiary condition
`Gamma^{4D} Psi_R = 0` is a kinematic definition of the state space, not a dynamical
constraint. Under FC1 the consistency question reframes from "is `Gamma^{4D} Psi_R = 0`
preserved?" (answer: no, per §4.6(b)/§4.10 — which is the classical VZ obstruction
signature) to "does the Schur complement dynamics give causal propagation?" — answered
affirmatively at principal-symbol order by OQ3-V1/V2/V3. **This reframing IS FC1 and FC1 is
open; the reframing is therefore an assumption, not a derivation.** If FC1 fails, the
unpreserved gamma-trace is a genuine VZ obstruction.

---

## 5. F_A != 0 and the Classical VZ Mechanism

### 5.1 Why the Classical VZ Mechanism Does Not Fire

In classical VZ, the sequence is:

1. Start with the standalone RS field equation `(slash D)_mu psi^mu = 0`.
2. The subsidiary condition `gamma^mu psi_mu = 0` is a primary constraint.
3. Acting with `D_nu` on this: `D_nu(gamma^mu D_mu psi^nu) + [D_nu, D_mu] psi^mu = 0`.
4. The commutator `[D_nu, D_mu] psi^mu = F_{nu mu} psi^mu` produces an F-dependent term.
5. This new term is not proportional to the primary constraint, generating a secondary
   constraint that is inconsistent with the primary one when `F != 0`.

**In GU, step (1) fails:** There is no standalone RS field equation. The RS field `Psi_R`
is not an independent dynamical variable with its own Lagrangian. Its dynamics is given
by the Schur complement `S_R Psi_R = 0`, which already incorporates the coupling to
the non-RS sector via the blocks B and C.

**Step (2) also fails structurally:** The gamma-trace `Gamma^{4D} Psi_R = 0` is not a
primary constraint arising from an RS Lagrangian. It is the definition of the field
content. There is no independent Lagrange multiplier enforcing it.

**The F_A-dependent term (step 4) therefore never appears:** Because there is no step 3
(no differentiation of an externally-imposed subsidiary condition), the curvature
`F_A != 0` never enters as a first-order term in a secondary constraint equation.

### 5.2 The Role of F_A in the Schur Complement

`F_A != 0` enters the Schur complement `S_R = A - B E^{-1} C` in two ways:

**(a) Via the zero-order potential `V_{RS}`** (the Shiab coupling `Phi(F_A tensor .)`
restricted to the RS sector). This modifies the effective RS Hamiltonian `H_RS` by a
zero-order term proportional to `F_A`. As established in vz-f5-curvature-check §3.2,
this is zero-order and does not affect the principal symbol.

**(b) Via higher-order corrections to the B and C blocks** from the covariant derivative
terms in D_GU^{4D} including `F_A`. The spin connection `omega^{4D}` includes terms
involving `F_A` (via the Yang-Mills equation `D_A* F_A = theta`) at zero order.

**Both entries are zero-order:** They do not produce new first-order terms in the
Schur complement principal symbol. The characteristic structure of `S_R` is therefore
unaffected by `F_A != 0`. This recovers the conclusion of vz-f5-curvature-check from
the Hamiltonian perspective: curvature `F_A` cannot produce new characteristics.

### 5.3 Comparison with the Buchdahl-Aurilia-Umezawa Analysis

Buchdahl (1962) and Aurilia-Umezawa (1969) showed that gravitational coupling (Riemann
curvature) can also produce VZ-type pathologies for standalone higher-spin fields.
The mechanism is analogous: the curvature enters the secondary constraint at first order
when acting with a derivative on the subsidiary condition.

**In GU:** the Weyl tensor of `g_Y` and the Riemann tensor of `g_s` enter `D_GU^{4D}`
at zero order (spin connection, as established in vz-f5-curvature-check §3.2). Since
neither curvature source produces a standalone RS Lagrangian, the Buchdahl-Aurilia-
Umezawa mechanism also cannot fire.

**The gravitational VZ question** (OQ in canon/no-go-class-relative-map.md) is therefore
also CONDITIONALLY_RESOLVED by the same structural argument: the Schur complement
framework excludes all curvature sources from first-order entries in the effective RS
equation.

---

## 6. Summary of the Hamiltonian Analysis

**The entire "GU RS sector" column below is conditional on FC1 (no standalone RS
Lagrangian), which is OPEN.** Under the alternative reading (FC1 false), the GU column
collapses onto the classical column and the VZ obstruction fires.

| Dirac-Bergmann step | Classical VZ RS field | GU RS sector (IF FC1 holds) |
|---|---|---|
| Field definition | Standalone `psi_mu` with RS Lagrangian | Sub-bundle `R_s = ker Gamma^{4D}` of `E_s`, no RS Lagrangian (assumes FC1) |
| Primary constraint | `phi_1 = gamma^mu D_mu psi_0 approx 0` (from E-L eq) | None (kinematic: `Gamma^{4D} Psi_R = 0` is definitional) — IF FC1 |
| Consistency check | `{phi_1, H_RS} approx 0` (must be verified) | No consistency check needed (no primary dynamical constraint) — IF FC1 |
| Secondary constraint | `phi_2 = F_{mu nu} psi^mu` (from acting with `D_nu`) | Not generated (no subsidiary condition to differentiate) — IF FC1 |
| Constraint preservation under `F_A != 0` | Fails (drives `phi_2`) | **Also fails** (§4.6(b)/§4.10: `[Gamma^{4D}, Phi(F_A)] Psi_R != 0`); benign only IF FC1 makes it kinematic |
| VZ obstruction | `phi_2` inconsistent with `phi_1` when `F != 0` | Does not arise IF FC1; **arises if FC1 fails** |
| Effective dynamics | Ill-posed when `F != 0` (VZ) | Well-posed: `S_R Psi_R = 0` with causal characteristics — IF FC1 |
| `F_A != 0` effect | Enters secondary constraint at first order | Enters only as zero-order potential in `S_R` |

**The Dirac-Bergmann consistency chain does not fire for the GU RS sector ONLY IF FC1
holds** (no standalone RS Lagrangian with an externally-imposed subsidiary condition). IF
FC1 holds, the gamma-trace constraint `Gamma^{4D} Psi_R = 0` is a kinematic definition,
not a dynamical constraint, and there is no secondary constraint to check. **FC1 is an
unproven negative-existence claim (open), so this conclusion is assumption-conditional.**
Note the constraint IS non-preserved under `F_A != 0` either way (§4.6(b)/§4.10); FC1 is
what decides whether that non-preservation is benign (kinematic) or the VZ obstruction
(dynamical).

**The `F_A != 0` curvature enters only as a zero-order potential** in the Schur
complement effective equation `S_R Psi_R = 0`. It cannot modify the principal symbol
and therefore cannot produce new characteristics. The causal propagation established
at the principal-symbol level (OQ3-V2/V3 RESOLVED, OQ3-V1 CONDITIONALLY_RESOLVED — constant-coefficient gauge only) is dynamically stable.

---

## 7. Verdict and Failure Conditions

**Verdict: CONDITIONALLY_RESOLVED — load-bearing on the unproven claim FC1 (no standalone
GU RS Lagrangian). This verdict is an assumption-conditional, not a free-standing
derivation.**

**Load-bearing dependency (read first).** The entire "benign" reading of this file rests
on FC1 below: that no standalone GU RS Lagrangian exists, so the gamma-trace constraint is
kinematic (a sub-bundle definition) rather than a dynamical, externally-imposed subsidiary
condition. The file's own §4.6(b) and §4.10 derive that, when `F_A != 0`, the gamma-trace
constraint is **not preserved** under time evolution (`[Gamma^{4D}, Phi(F_A)] Psi_R != 0`;
`phi = Gamma^{4D} Psi` does not remain zero). In classical VZ this non-preservation **is the
obstruction signature.** It is reinterpreted here as benign **only if** the Schur-complement
system is the complete dynamics — which is exactly FC1. Because FC1 is open (the file
establishes only that no such Lagrangian has been *identified*, not that none exists),
CONDITIONALLY_RESOLVED here means "resolved conditional on FC1." A future demonstration that
a standalone RS Lagrangian *does* exist would flip this file to GENUINE_OBSTRUCTION. The
verdict is not VERIFIED and is not unconditionally RESOLVED.

The constrained-Hamiltonian analysis at the Dirac-Bergmann level shows, **conditional on
FC1**:

1. **No dynamical subsidiary condition (conditional on FC1):** IF no standalone RS
   Lagrangian exists, the gamma-trace constraint `Gamma^{4D} Psi_R = 0`
   is kinematic (definitional of the state space), not dynamical (not derived from an
   RS Lagrangian), and the Dirac-Bergmann consistency chain that generates the VZ secondary
   constraint does not initiate. This conclusion is load-bearing on FC1, which is open;
   under the classical reading (FC1 false) the §4.6(b)/§4.10 non-preservation IS the VZ
   obstruction.

2. **`F_A != 0` enters only at zero order:** In the Schur complement `S_R`, gauge
   curvature `F_A` enters via the Shiab coupling as a zero-order potential. It cannot
   generate new first-order terms in the effective RS equation, and therefore cannot
   produce new characteristics.

3. **Causal propagation is dynamically stable:** The principal-symbol causal structure
   (null-cone characteristics, CONDITIONALLY_RESOLVED at 4D, constant-coefficient gauge) is the correct statement of the dynamical
   propagation. The Hamiltonian time evolution maps initial RS data to solutions with
   causal characteristic support.

**Failure conditions (specific mathematical statements that would falsify this result):**

**FC1 (LOAD-BEARING — the verdict of this file is conditional on FC1 holding).** If a
standalone GU RS Lagrangian exists (separate from the full `D_GU^{4D}`
field equation), from which the gamma-trace constraint `Gamma^{4D} Psi_R = 0` is derived
as an E-L condition, then the Dirac-Bergmann analysis would apply, the §4.6(b)/§4.10
non-preservation of the gamma-trace under `F_A != 0` would be the classical VZ obstruction
signature, and this file's verdict would flip to GENUINE_OBSTRUCTION.

**Status of FC1: OPEN. The file establishes only ABSENCE OF IDENTIFICATION, not proof of
absence.** No such Lagrangian has been identified in the GU construction, but the
construction has not been fully specified (the GU action on `Y^14` is not available at
reconstruction grade — see §8), so non-existence is **not proven**. The "kinematic, not
dynamical" escape that carries this file's verdict — and every "automatically / by
construction / by definition / trivially" phrasing in §4 — presupposes FC1. It is an
**unproven negative-existence claim**, and the CONDITIONALLY_RESOLVED verdict is
load-bearing on it. Resolving FC1 affirmatively requires either (a) the full GU action,
showing the RS sector has no independent Lagrangian, or (b) the guardian-symmetry route
OQ-H3 (a symmetry of `D_GU^{4D}` that preserves `ker Gamma^{4D}`), giving an algebraic
proof.

**FC2.** If the Schur complement `S_R = A - B E^{-1} C` has a nontrivial zero-order
correction from `F_A != 0` that produces a new **first-order** term in the effective
RS equation (i.e., if `F_A` enters the B or C blocks at first order, not zero order),
then the principal symbol changes and new characteristics could appear. This would
require `F_A` to enter D_GU^{4D} at first order, contradicting the OQ2-a result
(Shiab is zero-order). Currently FC2 is ruled out by OQ2-a (reconstruction grade).

**FC3.** If the extrinsic curvature `K_{mu nu}` of the spatial slice (which appears
in the commutator `[Gamma^{4D}, D_GU^{4D}]` in §4.9) produces a term that makes the
propagation equation (**) ill-posed (e.g., a spacelike propagation speed for `phi`),
then constraint propagation fails. FC3 requires `K_{mu nu}` to produce a spacelike
effective characteristic in the sourced equation for `phi`, which would require
the extrinsic curvature to dominate over the causal propagation. For physical
spacetimes satisfying the dominant energy condition, `K_{mu nu}` is bounded by the
matter stress-energy and does not dominate. Not established at reconstruction grade.

**FC4.** If the GU theory contains mass terms for the RS sector (e.g., from the
Sp(64) Casimir or from a Higgs mechanism), then the massive RS case requires
separate analysis. Mass terms can modify the subsidiary condition propagation (classical
VZ applies to both massive and massless RS fields). In GU, the mass of the RS sector
comes from the Schur complement spectrum (the eigenvalues of `S_R` on the K3 section,
from the APS index computation). If the mass term enters `S_R` at first order (not
zero order), FC4 is a genuine concern. Currently there is no evidence for first-order
mass terms in `S_R`.

---

## 8. What This Closes

**The F5 dynamical gate in the no-go canon is CONDITIONALLY_RESOLVED at reconstruction
grade.** The specific open claim in canon/no-go-class-relative-map.md line 319,

> "The constrained-Hamiltonian propagation of the subsidiary condition `Gamma^{4D} psi = 0`
> in an Sp(64) background: residual open at full dynamical level."

is now addressed by the Dirac-Bergmann analysis of §4: **conditional on FC1**, the
subsidiary condition is kinematic, not dynamical, and the Dirac-Bergmann consistency chain
does not initiate. The gate is closed at reconstruction grade, **conditional on FC1-FC4 —
and load-bearing on FC1 in particular,** which is an unproven negative-existence claim (no
standalone RS Lagrangian). Under the alternative reading where FC1 fails, the §4.6(b)/§4.10
non-preservation of the gamma-trace under `F_A != 0` is the classical VZ obstruction
signature and the gate is NOT closed. This is therefore an assumption-conditional closure,
not a free-standing one.

**Remaining for upgrade to VERIFIED:**

- FC1: Confirm no standalone RS Lagrangian exists in GU (requires full specification
  of the GU action on `Y^14`; not yet available at reconstruction grade).
- FC3: Prove the extrinsic curvature `K_{mu nu}` sourcing in equation (**) does not
  produce spacelike effective propagation for the constraint field `phi = Gamma^{4D} Psi`.
  This requires energy estimates for the sourced symmetric hyperbolic system.
- FC4: Confirm the RS mass term enters `S_R` only at zero order (consistent with the
  Schur complement derivation but requiring explicit mass computation).

---

## 9. Open Questions

**OQ-H1.** Can the argument of §4.10 be made into a full energy estimate? Specifically,
the propagation equation `D_GU^{4D} phi = source(Psi_R)` is a sourced symmetric
hyperbolic system. An energy estimate of the form `||phi||_{H^k} <= C ||source||_{H^k}`
with `||source||_{H^k} -> 0` as `||Psi_R||_{H^k} -> 0` would establish FC3 and upgrade
the constraint propagation to RESOLVED.

**OQ-H2.** The GU RS mass from the K3 APS spectrum: what is the explicit form of the
mass term in `S_R` after dimensional reduction to 4D? If the mass term is `m^2 Psi_R`
(zero-order), FC4 is automatically satisfied. If there is a first-order mass term
(coupling `m nabla Psi_R` to something), FC4 requires separate analysis.

**OQ-H3.** The guardian symmetry question (OQ2 in the no-go canon): the Schur complement
argument shows the RS sector cannot decouple kinematically. But is there a symmetry of
`D_GU^{4D}` that directly preserves `ker Gamma^{4D}`? Identifying such a symmetry (if
it exists) would provide an algebraic rather than analytic proof of FC1.

---

## 10. References

- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` (VZ evasion 14D+4D; OQ3-V1/V2/V3)
- `explorations/vz-evasion/vz-f5-curvature-check-2026-06-23.md` (zero-order curvature at 4D)
- `explorations/vz-evasion/vz-oq2-lower-order-curvature-2026-06-23.md` (curvature zero-order at 14D)
- `explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md` (subprincipal analysis)
- `canon/no-go-class-relative-map.md` §2.5 (VZ no-go entry; F5 row)
- `papers/vz-evasion-preprint-draft-2026-06-23.md` §3-4 (VZ analysis structure)
- Dirac, P.A.M. (1964). _Lectures on Quantum Mechanics_. Yeshiva University, New York.
  (Dirac-Bergmann constraint formalism)
- Bergmann, P.G. and Goldberg, I. (1955). Phys. Rev. 98:531.
  (Secondary constraint generation and first-class/second-class classification)
- Velo, G. and Zwanziger, D. (1969). Phys. Rev. 186:1337. (VZ theorem)
- Buchdahl, H.A. (1962). Nuovo Cimento 25:486.
  (Gravitational coupling of higher-spin fields and subsidiary conditions)
- Hormander, L. (1985). _The Analysis of LPDOs III_, Ch. 23.
  (Real principal type operators and propagation of singularities)
- Sundermeyer, K. (1982). _Constrained Dynamics_. Springer.
  (Dirac-Bergmann algorithm for gauge field theories)
