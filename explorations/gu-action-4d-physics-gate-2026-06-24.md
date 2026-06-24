---
title: "GU Action to 4D Physics Gate"
date: 2026-06-24
status: exploration/reconstruction
verdict: "OPEN_ACTION_GATE"
---

# GU Action to 4D Physics Gate

## Verdict

The current repo evidence does **not** yet derive actual 4D physics from a written GU
action. It supports two bounded reconstruction-grade statements:

1. Linearized Schwarzschild / weak-field recovery passes at `O(M/r)` under the current
   `R_fail` bookkeeping.
2. The theta-field dark-energy lane has viable DESI-sign dynamics only if the reduced
   action generates a sizable negative non-minimal curvature coupling.

The exact nonlinear 4D-GR question remains open and sharp. Under the current
Willmore-only section-action reading, exact Schwarzschild and Kerr are genuine
obstructions as vacuum solutions. That obstruction is not removed by the weak-field
pass; it can only be removed by the full coupled GU action and its Euler-Lagrange
equations.

## Minimal Object Needed Next

The next object must be a written variational principle, not another reconstructed field
equation slogan. Minimal acceptable object:

```text
S_GU[s, A, epsilon, B, psi]
  = integral L_GU(g_gimmel, s, II_s^H, A, F_A, theta, epsilon, B, psi, ...)
```

with:

- all terms, signs, normalizations, and cross-terms stated, especially `|II_s^H|^2`,
  `|F_A|^2`, `|theta|^2`, possible `theta * F_A`, curvature-theta, torsion-theta, and
  fermion-source terms;
- the independent fields and allowed variations stated: at minimum section `s: X4 -> Y14`,
  Sp(64) connection `A`, IG variables `(epsilon, B)`, and spinors `psi`;
- the full Euler-Lagrange tuple
  `(E_s, E_A, E_epsilon, E_B, E_psi) = 0`;
- the 4D section-pullback / reduction dictionary producing an effective 4D action
  `S_eff[g, theta, ...]`, including the normalization convention for the homogeneous
  theta mode used in the FLRW files.

This object is also the upgrade gate for dark-energy Assumption 3: the repo currently has
a reconstruction-grade route where `S_IG = integral |theta|^2` gives
`delta S_IG / delta A = 2 theta` and hence `D_A* theta = 0`, but the canon still requires
verification against a primary written GU action.

## Exact Nonlinear GR vs Weak-Field Recovery

These must stay separate.

**Weak-field recovery:** `canon/schwarzschild-weak-field-rfail.md` and
`explorations/rfail-schwarzschild-oq2-weak-field-2026-06-23.md` support a bounded claim:
for a linearized Schwarzschild section, the combined `R_fail` vanishes at `O(M/r)`.
The mechanism is the exact Gauss identity plus quadraticity of `Q(B)`, while the standard
4D Schwarzschild Einstein residual is zero by definition. This is a reconstruction-grade
solar-system pass, conditional on the named linearized Willmore/Yang-Mills/CAS gates.

**Exact nonlinear recovery:** `explorations/rfail-non-umbilic-schwarzschild-2026-06-23.md`
states a stronger obstruction for the current section action: exact Schwarzschild is not
Willmore-critical, and Kerr is expected to fail for the same non-conformally-flat vacuum
reason. This is a full-solution question, not a leading-order PPN question. A theory can
pass the weak-field gate and still fail exact black-hole/vacuum GR recovery.

## Binary Gate A: Schwarzschild/Kerr as Full Coupled GU Solutions

For each target metric `g` in `{Schwarzschild, Kerr}`, run the following check against the
written `S_GU`.

**PASS iff** there exists a smooth vacuum field configuration
`(s_g, A, epsilon, B, psi = 0)` on the relevant exterior domain, with the standard
asymptotic mass/angular-momentum data, such that:

```text
s_g^*(g_gimmel) = g                 up to diffeomorphism/gauge
E_s = 0
E_A = 0
E_epsilon = 0
E_B = 0
E_psi = 0
T_matter = 0
Lambda = 0 or the stated asymptotic Lambda sector
```

and the cancellation is internal to the GU vacuum equations, not a relabeling of
`Q^{TF}(B)` as matter stress.

**FAIL iff** no such coupled vacuum configuration exists for Schwarzschild or Kerr after
including the full action's connection, theta, curvature, and cross-term contributions.

Consequences:

- If PASS for both Schwarzschild and Kerr: the current exact-vacuum obstruction is removed;
  next work is deriving the PPN/2PN limits and strong-field observables from the same fields.
- If PASS only weak-field: keep the weak-field canon, but do not claim nonlinear GR recovery.
- If FAIL: GU as written does not reproduce exact black-hole vacuum GR. The options are
  action revision, explicit modified-gravity/strong-field predictions, or the nonstandard
  interpretation that black-hole geometries are embedding-sourced rather than vacuum.

## Binary Gate B: Does Reduction Generate the Needed `xi R theta^2` Term?

Reduce the same written `S_GU` to the homogeneous FLRW theta mode in the same normalization
as `dark-energy-w-window-mechanism-2026-06-23.md`:

```text
S_eff superset integral sqrt(-g) [
  -1/2 (partial B)^2
  -1/2 (M_KK^2 + xi R) B^2
  - Lambda_eff
  + ...
]
```

where `B` is the scalar FLRW amplitude of `s*(theta)` and the equation of motion contains
`+ xi R B`.

**PASS iff** the coefficient is generated by GU geometry, with the same normalization, and
satisfies approximately:

```text
xi < -0.319
```

with `xi ~ -0.6` the current reconstruction-grade value that matches the DESI-sign and
magnitude window. This pass also requires that the scalar-mode reduction of `theta` and the
`M_KK = 2 sqrt(2) H_0` input survive their own open checks.

**FAIL iff** the reduced action has no `R theta^2` term, or gives minimal/conformal/nonnegative
or insufficiently negative coupling, e.g. `xi = 0`, `xi = +1/6`, or `xi >= -0.319`.

Consequences:

- If PASS: the dark-energy sign problem moves from "wrong-sign minimal theta" to a genuine GU
  geometry prediction; next work is full `w_0,w_a` likelihood fitting and error-controlled
  FLRW integration.
- If FAIL: the only currently identified mechanism that reaches the DESI-sign window is not
  GU-admissible, so the theta-field dark-energy lane shifts toward a structural sign/magnitude
  obstruction unless a fourth GU-derived mechanism is found.

## Outcome Matrix

| Gate A: exact Schwarzschild/Kerr | Gate B: `xi R theta^2` | Meaning |
|---|---|---|
| PASS | PASS | GU has a plausible written-action route to both nonlinear vacuum GR and viable theta dark energy. Promote only after independent verification. |
| PASS | FAIL | Nonlinear GR lane survives; dark-energy Candidate D needs a new GU-generated mechanism or demotion. |
| FAIL | PASS | Cosmological theta dynamics may survive; exact black-hole/vacuum GR recovery fails for the written action. |
| FAIL | FAIL | The current action is not viable as the actual 4D physics engine without revision. |
| ACTION UNWRITTEN | ACTION UNWRITTEN | No promotion. The correct status remains exploration/reconstruction. |

## Sources Read

- `RESEARCH-STATUS.md` canon promotion sweep and dark-energy/Schwarzschild entries.
- `CANON.md`, `canon/dark-energy-theta-divergence-free.md`,
  `canon/schwarzschild-weak-field-rfail.md`, and
  `canon/theta-field-flrw-dark-energy-eos.md`.
- `NEXT-STEPS.md` testable-predictions and dark-energy sections.
- `explorations/rfail-non-umbilic-schwarzschild-2026-06-23.md`.
- `explorations/rfail-schwarzschild-oq2-weak-field-2026-06-23.md`.
- `explorations/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md`.
- `explorations/dark-energy-assumption3-variational-2026-06-23.md`.
- `explorations/theta-field-flrw-matter-era-ode-2026-06-23.md`.
- `explorations/dark-energy-w-window-mechanism-2026-06-23.md`.
- `explorations/gu-testable-predictions-2026-06-23.md`.
