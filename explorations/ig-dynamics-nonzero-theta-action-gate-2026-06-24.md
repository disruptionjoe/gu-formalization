---
title: "IG Dynamics Nonzero Theta Action Gate"
date: 2026-06-24
status: exploration
doc_type: research_note
problem_label: "ig-dynamics-nonzero-theta-action-gate"
verdict: "BARE_FREE_BETA_THETA_NORM_STRUCTURALLY_BROKEN"
owned_path: "explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
depends_on:
  - "explorations/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/dark-energy-assumption3-variational-2026-06-23.md"
  - "canon/dark-energy-theta-divergence-free.md"
  - "canon/theta-field-flrw-dark-energy-eos.md"
  - "explorations/dark-energy-w-window-mechanism-2026-06-23.md"
  - "explorations/codazzi-sp64-bundle-2026-06-23.md"
  - "explorations/codazzi-general-non-umbilic-2026-06-23.md"
  - "explorations/4d-reduction-section-pullback-2026-06-22.md"
---

# IG Dynamics Nonzero Theta Action Gate

## Verdict

The bare action story

```text
S_YM[A] - (c_theta/2) int_Y |theta|^2,
theta = A - Gamma(eps) - Ad(eps^-1) beta,
```

is structurally broken if `beta` is an independently varied auxiliary field. The
`A` variation gives the desired source term, but the `beta` variation sets the same
source to zero. Therefore a nonzero dark-energy theta sector requires one of three
extra choices:

1. `eps,beta` are background/Stueckelberg data and are not independently varied.
2. `eps,beta` are varied only on a constrained IG submanifold.
3. `eps,beta` are genuine dynamical fields with their own kinetic or first-order
   term.

Only branch 1 and the A-independent version of branch 2 preserve the advertised
vacuum equation `D_A^* F_A = theta` without extra terms. Branch 3 is the most honest
way to make theta a real dynamical dark-energy field, but it generically changes the
connection equation to `D_A^* F_A = theta - J_IG` or an equivalent total-current law.

Recommended action branch: pursue branch 2 first, with an A-independent
Stueckelberg/geometric constraint on `(eps,beta)`. If no primary GU source supports
such a constrained variation, switch to branch 3 and explicitly revise the canon
claim from "theta is the source" to "theta plus the IG dynamical current is the
source."

## 1. Baseline Variation and the Blocker

Write

```text
C(eps,beta) = Gamma(eps) + Ad(eps^-1) beta
theta       = A - C(eps,beta).
```

Use the sign convention

```text
S_0[A,eps,beta]
  = S_YM[A] - (c_theta/2) int_Y <theta,theta>.
```

The sign can be flipped with a corresponding flip in the source equation; the
`beta` obstruction is unchanged.

For fixed `eps,beta`,

```text
delta_A theta = delta A,
delta_A S_0 = int_Y <g_A^-2 D_A^* F_A - c_theta theta, delta A>.
```

Thus

```text
E_A = g_A^-2 D_A^* F_A - c_theta theta = 0.
```

With normalization `g_A^2 c_theta = 1`, this is the desired vacuum equation

```text
D_A^* F_A = theta.
```

Now vary `beta` with `A,eps` fixed. Since

```text
delta_beta theta = - Ad(eps^-1) delta beta,
```

Ad-invariance of the pairing gives

```text
delta_beta S_0
  = c_theta int_Y <Ad(eps) theta, delta beta>.
```

Therefore

```text
E_beta = c_theta Ad(eps) theta = 0
        <=> theta = 0
```

when `beta` is freely varied. The `eps` equation is then either automatically
satisfied in this sector or adds further restrictions, but it cannot rescue nonzero
theta after `E_beta` has fired.

So the minimal action has the following incompatible pair:

```text
E_A wants:    D_A^* F_A = theta
E_beta gives: theta = 0
```

The result is not a sign convention issue and not a normalization issue. It is the
ordinary auxiliary-field consequence of putting an unconstrained algebraic variable
inside a positive or negative quadratic norm.

## 2. Branch 1: Background or Stueckelberg Variables

### 2.1 Variation Rule

Declare

```text
delta eps = 0,
delta beta = 0
```

in the action principle. The only IG-sector contribution to the connection equation
is then

```text
E_A^{theta} = - c_theta theta.
```

The field equations contain no `E_beta` equation, so nonzero theta is allowed:

```text
D_A^* F_A = theta          after g_A^2 c_theta = 1.
```

This is the cleanest way to keep the transcript-style field equation.

### 2.2 Gauge/Noether Consequence

There is a subtlety. If `(eps,beta)` are fixed external spurions that transform
with the gauge group so that `theta` is covariant, the Noether identity for
`S_theta` contains the omitted background variations. It does not by itself imply

```text
D_A^* theta = 0.
```

Instead, the divergence-free property must come from the connection equation:

```text
D_A^* F_A = theta
```

together with the Yang-Mills integrability identity

```text
D_A^* D_A^* F_A = 0
```

in the chosen curvature/sign convention. Equivalently, branch 1 preserves
`D_A^* theta = 0` only after the source equation is imposed, or by an extra
background-selection condition.

If the fixed `(eps,beta)` are not transformed as spurions, local gauge invariance is
broken and the Noether route to `D_A^* theta = 0` is unavailable.

### 2.3 Dark-Energy Support

Branch 1 can support a nonzero theta source, but it is weak as a dark-energy
action story. The theta mode is not an independent IG field. It is the connection
distortion relative to fixed Stueckelberg/background data:

```text
theta = A - C_background.
```

Any 4D scalar dark-energy mode must then come from the remaining `A` and section
dynamics after reduction. This is possible in principle, because the Yang-Mills
term supplies derivatives for `A`, and the section/Codazzi reduction can turn
normal components into `s^*theta` modes. But the branch has not derived:

```text
S_eff[B,g] contains
  -1/2 (partial B)^2
  -1/2 (M_KK^2 + xi R) B^2
```

or the needed `xi < -0.319` window. It preserves the source equation better than it
explains the dark-energy dynamics.

### 2.4 Branch 1 Verdict

```text
nonzero theta:              YES
D_A^* F_A = theta:          YES, by normalization
D_A^* theta = 0:            YES on shell if D_A^*D_A^*F_A=0 is verified
dark-energy theta field:    POSSIBLE but not derived
cost:                       eps,beta are not true variational IG fields
```

## 3. Branch 2: Constrained IG Variables

### 3.1 General A-Independent Constraint

Let `(eps,beta)` be restricted by constraints

```text
Phi_I(eps,beta,s) = 0,
```

with Lagrange multipliers `lambda^I`, and assume first that `Phi_I` is independent
of `A`. The action is

```text
S = S_YM[A]
    - (c_theta/2) int_Y |theta|^2
    + int_Y <lambda^I, Phi_I(eps,beta,s)>.
```

The Euler-Lagrange equations are schematically

```text
E_A:
  g_A^-2 D_A^* F_A - c_theta theta = 0,

E_beta:
  c_theta Ad(eps) theta + (D_beta Phi)^* lambda = 0,

E_eps:
  c_theta L_eps^* theta + (D_eps Phi)^* lambda = 0,

E_lambda:
  Phi(eps,beta,s) = 0.
```

Here `L_eps^* theta` denotes the adjoint of the linearized map

```text
delta eps |-> delta_eps Gamma + delta_eps(Ad(eps^-1) beta).
```

The key point is that `E_beta` no longer implies `theta=0` if `(D_beta Phi)^*`
has enough image to balance `Ad(eps) theta`. Equivalently, the restricted
variation says only:

```text
projection of theta onto allowed IG variations = 0.
```

If the allowed `beta` variations are all of `Omega^1(Y,ad P)`, the projection is
the identity and the old obstruction returns. If the constraint fixes `beta` to a
geometric/Stueckelberg submanifold, theta may lie in the normal directions to that
constraint surface and remain nonzero.

Examples of constraints that do not immediately kill theta:

```text
beta = beta_0(eps,s)                    A-independent geometric relation
beta in im(tau^+_eps) or a finite IG orbit slice
P_perp(beta,eps,s) = 0                  projection to an admissible subbundle
```

In all of these, the multiplier solves the missing `beta` equation rather than
forcing `theta` itself to vanish.

### 3.2 A-Dependent Constraints

If the constraint depends on `A`,

```text
Phi = Phi(A,eps,beta,s),
```

the connection equation becomes

```text
g_A^-2 D_A^* F_A - c_theta theta + (D_A Phi)^* lambda = 0.
```

Then the advertised equation is replaced by

```text
D_A^* F_A = g_A^2 c_theta theta - g_A^2 (D_A Phi)^* lambda.
```

This is not the desired `D_A^* F_A = theta` unless the multiplier term vanishes
on the branch being studied.

Important special case:

```text
Phi = D_A^* theta = 0
```

does enforce the divergence-free condition directly, but it is A-dependent. Its
`A` variation adds derivative multiplier terms to `E_A`. This branch protects
`D_A^* theta = 0` by construction, but it does not preserve the bare source
equation without extra cancellations.

### 3.3 Dark-Energy Support

Branch 2 is the best conservative salvage of the current action. It keeps the
same `A` equation when the constraint is A-independent, while avoiding the
free-auxiliary-field collapse.

It can support a dark-energy theta field if the constraint surface selects a
nonzero geometric mode whose reduction gives the canonical FLRW scalar:

```text
B(t) = scalar amplitude of s^*theta,

S_eff[B,g] contains
  -1/2 (partial B)^2
  -1/2 (M_KK^2 + xi R[g]) B^2.
```

However, the branch does not automatically supply the crucial DESI-sign coupling.
The next reduction must still compute

```text
xi_eff = C_Rtheta / Z_theta
```

and check whether

```text
xi_eff < -0.319
```

with the reconstruction-grade target near `xi_eff ~= -0.6`.

### 3.4 Branch 2 Verdict

```text
nonzero theta:              YES, if the constraint removes free beta variations
D_A^* F_A = theta:          YES for A-independent constraints
D_A^* theta = 0:            YES on shell from source equation plus integrability,
                             or directly if imposed at the cost of modifying E_A
dark-energy theta field:    PLAUSIBLE, still requires FLRW reduction
cost:                       constraint must be primary-sourced or geometrically
                             justified, not invented to save the model
```

## 4. Branch 3: Dynamical IG Variables

### 4.1 Second-Order Kinetic Term

Let

```text
U = Ad(eps^-1) beta,
theta = A - Gamma(eps) - U.
```

A representative dynamical branch is

```text
S = S_YM[A]
    - (c_theta/2) int_Y |theta|^2
    - (Z_U/2) int_Y |D_A U|^2
    - int_Y V(U,eps).
```

Then the equations have the schematic form

```text
E_A:
  g_A^-2 D_A^* F_A - c_theta theta + J_U = 0,

E_U:
  c_theta theta - Z_U D_A^* D_A U - V_U = 0,

E_eps:
  c_theta L_eps^* theta + Z_U K_eps(D_A U) + V_eps = 0.
```

The `U` equation gives

```text
theta = c_theta^-1 (Z_U D_A^* D_A U + V_U),
```

so nonzero theta is allowed. But the connection equation is no longer the clean
source equation. It is

```text
D_A^* F_A = g_A^2(c_theta theta - J_U).
```

Here `J_U` is the gauge current from the kinetic term, schematically

```text
J_U ~ Z_U [U, D_A U]
```

plus terms from the `eps` dependence of the reference connection if that
dependence is gauged.

The conserved object is therefore the total source:

```text
D_A^*(c_theta theta - J_U) = 0
```

on the full equations, not generally

```text
D_A^* theta = 0.
```

The only ways to recover the old equation are special:

```text
J_U = 0                       commuting/abelian/singlet sector
J_U is higher order           perturbative truncation
J_U = alpha theta             source renormalization
```

None is automatic for an Sp(64)-valued IG field.

### 4.2 First-Order Parent Term

A first-order version introduces a momentum-like field `P`:

```text
S_IG-dyn =
  int_Y <P, D_A U>
  - (1/2Z_U) int_Y |P|^2
  - int_Y V(U,eps)
  - (c_theta/2) int_Y |theta|^2.
```

The equations are

```text
E_P:
  D_A U - Z_U^-1 P = 0,

E_U:
  -D_A^* P + V_U + c_theta theta = 0,

E_A:
  g_A^-2 D_A^* F_A - c_theta theta + [U,P] = 0.
```

After eliminating `P`, this is equivalent to the second-order branch. Before
eliminating `P`, the obstruction is especially visible: the first-order term
adds the canonical IG current `[U,P]` to the connection equation. Thus it permits
nonzero theta but generically replaces the source by a total current.

### 4.3 Kinetic Term for Theta Itself

One might try

```text
S_theta-dyn =
  - (c_theta/2) int_Y |theta|^2
  - (Z_theta/2) int_Y |D_A theta|^2.
```

The `beta` equation now becomes wave-like rather than algebraic:

```text
c_theta theta - Z_theta D_A^* D_A theta + nonlinear commutator terms = 0,
```

so nonzero theta is allowed. But because `theta` contains `A`, the `A` equation
also gains higher-derivative and commutator terms. Again, the simple
`D_A^* F_A = theta` equation is lost unless one works in a special truncation.

### 4.4 Dark-Energy Support

Branch 3 is the strongest dark-energy branch. It can naturally produce a
canonical reduced mode:

```text
S_eff[B,g] =
  int_X sqrt(-g) [
    -1/2 (partial B)^2
    -1/2 (M_KK^2 + xi R[g]) B^2
    ...
  ].
```

It is also the branch most capable of deriving, rather than inserting, the
curvature coupling needed by the DESI-sign mechanism:

```text
xi_eff < -0.319,
target xi_eff ~= -0.6.
```

The cost is conceptual but large: the canon equation should no longer be stated
as a bare theta source. It becomes a coupled current equation:

```text
D_A^* F_A = theta_eff,
theta_eff = c_theta theta - J_IG,
```

with the divergence-free law applying to `theta_eff`, not automatically to
`theta` alone.

### 4.5 Branch 3 Verdict

```text
nonzero theta:              YES
D_A^* F_A = theta:          GENERICALLY NO
D_A^* theta = 0:            GENERICALLY NO; total current is conserved
dark-energy theta field:    BEST physical route
cost:                       must rewrite the action-level canon around theta_eff
```

## 5. Comparison Matrix

| Branch | Nonzero theta? | Preserves `D_A^*F_A=theta`? | Preserves `D_A^*theta=0`? | Dark-energy support | Main cost |
|---|---:|---:|---:|---:|---|
| Free `beta` with only `|theta|^2` | No | No nonzero source | Trivial only | No | Forces `theta=0` |
| 1. Background/Stueckelberg, not varied | Yes | Yes | On shell if YM double-divergence identity is verified | Possible, not derived | IG variables are not dynamical |
| 2. A-independent constrained IG | Yes | Yes | On shell from source equation; or by added constraint with cost | Plausible | Constraint needs real GU origin |
| 2. A-dependent constraint, e.g. `D_A^*theta=0` | Yes | Usually no | Yes by construction | Plausible | Multiplier modifies `E_A` |
| 3. Dynamical IG kinetic/first-order | Yes | Usually no | Conserves total current, not theta alone | Strongest | Canon source equation must be revised |

## 6. Recommended Branch

The immediate action branch should be:

```text
Branch 2A:
  eps,beta are constrained Stueckelberg/geometric variables;
  the constraint Phi(eps,beta,s)=0 is independent of A;
  beta is not a free auxiliary field;
  the A equation remains D_A^*F_A = theta.
```

This branch keeps the largest amount of the existing reconstruction:

```text
D_A^* F_A = theta,
s^*theta ~ II_s^H,
D_a^* F_a + K(A,s) = s^*theta,
```

while avoiding the immediate `theta=0` collapse.

The branch is acceptable only if the constraint is not decorative. It must be one
of:

```text
primary-sourced from a written GU action or IG construction;
forced by the tau^+ / double-coset geometry;
forced by the section-pullback geometry, e.g. beta = beta_0(eps,s);
forced by gauge reduction/BRST as a true Stueckelberg slice.
```

If no such constraint exists, the honest next branch is branch 3. In that case the
project should stop trying to keep the bare equation `D_A^*F_A=theta` as exact and
should instead derive a total IG current:

```text
D_A^*F_A = theta_eff,
D_A^*theta_eff = 0,
theta_eff = c_theta theta - J_IG.
```

That would be a fundamentally different IG dynamics, but it is structurally
healthier than hiding a free auxiliary field that kills theta.

## 7. Biggest Proof Obligation

The largest unresolved proof obligation is:

```text
Derive the allowed variation space of (eps,beta) from a written GU action or from
the tau^+ / IG geometry.
```

Everything turns on this. If `(eps,beta)` are free coordinates on

```text
IG = G semidirect Omega^1(Y,ad P),
```

then the bare `|theta|^2` term kills theta and the current action idea fails. If
they are constrained Stueckelberg coordinates, the desired source equation can
survive. If they are dynamical fields, the dark-energy branch can survive, but the
source equation and canon divergence-free claim must be rewritten for a total
current.

The second proof obligation, downstream of the first, is the FLRW reduction:

```text
Compute Z_theta, M_KK, and xi_eff for the surviving branch.
```

The dark-energy window is not decided by nonzero theta alone. It requires the
reduced scalar mode and, for the DESI-sign mechanism currently on the table,

```text
xi_eff < -0.319,
preferably xi_eff ~= -0.6.
```

## Sources Read

- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/dark-energy-assumption3-variational-2026-06-23.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `explorations/dark-energy-w-window-mechanism-2026-06-23.md`
- `explorations/codazzi-sp64-bundle-2026-06-23.md`
- `explorations/codazzi-general-non-umbilic-2026-06-23.md`
- `explorations/4d-reduction-section-pullback-2026-06-22.md`
