---
title: "Draft Goal: Primary GU Action/Operator Specification"
date: 2026-06-24
status: exploration/draft_goal
doc_type: goal_draft
verdict: "DRAFT_GOAL_NOT_PROOF_CLOSURE"
owned_path: "explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md"
depends_on:
  - "explorations/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/vz-principal-symbol-convention-reconciliation-2026-06-24.md"
  - "explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
  - "RESEARCH-STATUS.md"
---

# Draft Goal: Primary GU Action/Operator Specification

## Status

This is a draft goal, not a proof and not a canon promotion.

The proposed work is worth doing because several live GU lanes now fail for the same
reason: the repo has strong local reconstructions, but it does not yet have one
authoritative typed action/operator object that all downstream gates can test.

The honest current posture is:

```text
typed operator spine:        canonical proposal, not proof-grade
VZ 14D:                      conditionally evaded, gated on the actual operator
exact GR / Schwarzschild:    open action gate
FLRW theta xi:               open action gate for GU provenance
RS generation index:         open background-dependent / missing physical symbol data
IG variation:                blocked unless beta variation is fixed, constrained, or dynamical
claim governance:            active status discipline, not evidence
```

## Goal Statement

Produce a primary GU action/operator specification that fixes, in one typed document, the
actual objects to be varied and tested:

```text
D_GU       the primary rolled-up operator on the relevant 0/1 and RS sectors
S_GU       the primary action functional
fields     s, A, epsilon, beta, Psi, and any required auxiliary or multiplier fields
geometry   X, Y = Met_Lor(X), g_Y, P -> Y, S, section pullback, II_s^H
IG status  fixed, constrained, or dynamical variation rule for epsilon,beta
```

The goal is not to make GU true by declaration. The goal is to write the missing object
sharply enough that the major live claims can either compute against it or demote cleanly.

Success means future workers can point to a single specification and say:

```text
This is the operator whose principal symbol is being tested.
This is the action whose Euler-Lagrange equations are being reduced.
This is the variation space for IG variables.
This is where lower-order curvature, section, and source terms live.
This is the normalization used for Newton constants, xi_eff, and RS index data.
```

## Why This Matters

The repo is no longer blocked mainly by lack of clever ideas. It is blocked by object
identity.

The VZ lane needs to know whether the true first-order operator contains

```text
Phi_d := Phi_2 o d_A
```

with the advertised coefficient, or only a zero-order curvature insertion

```text
Phi_F := Phi_2(F_A tensor -).
```

The action lane needs to know whether `epsilon,beta` are free fields, constrained
Stueckelberg geometry, fixed background data, or dynamical IG variables. Without that,
the bare `|theta|^2` branch either kills nonzero theta by free beta variation or leaves
the advertised source equation underived.

The exact GR and FLRW lanes need the full Euler-Lagrange tuple, not a weak-field slogan:

```text
(E_s, E_A, E_epsilon, E_beta, E_Psi) = 0.
```

The RS generation-count lane needs the physical gauge-fixed GU RS symbol class, not raw
projector ranks and not a target index imported after the fact.

The broader governance layer needs a single object that prevents status laundering: controls,
ansatz states, host constructions, and conditional symbol checks must not be cited as
derived physics unless the primary operator/action actually supplies the needed data.

## Current Repo Evidence

The current evidence supports this goal as a necessary consolidation step.

`gu-typed-operator-action-spine-2026-06-24.md` supplies a coherent proposed carrier:

```text
Y = Met_Lor(X), signature(g_Y) = (9,5)
G = Sp(64), P -> Y, S = S^+ plus S^-
s: X -> Y, A, epsilon,beta, theta, Psi
D_roll(u,psi) = (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u,psi)
```

It explicitly does not prove that the actual GU action forces this operator.

`gu-minimal-action-spec-2026-06-24.md` specifies a minimal action branch with:

```text
S_YM + S_DD + S_theta + S_W + S_IG-dyn/open + S_boundary
```

and shows that the missing IG-sector variation is load-bearing for exact GR and FLRW
claims.

`gu-closed-loop-action-ig-branch-2026-06-24.md` chooses Branch 2A as the strongest current
candidate:

```text
A-independent constrained IG / Stueckelberg geometry
```

but records that no branch yet derives `xi_eff < -0.319` or exact Schwarzschild/Kerr
solutions.

`vz-principal-symbol-convention-reconciliation-2026-06-24.md` resolves a notation conflict:
`Phi_2` is zero-order, `Phi_d` is first-order, `Phi_F` is zero-order, and the VZ `F_xi`
block is coherent only if the actual operator contains `Phi_d`.

`generation-count-rs-k3-symbol-index-attempt-2026-06-24.md` shows that the currently
defensible raw K3 RS symbol classes give other indices in the flat-F branch and leave the
physical GU gauge-fixed RS complex open/background-dependent.

`live-claim-dag-fault-finality-ledger-2026-06-24.md` identifies the same central dependency
under node names:

```text
VZ-OPERATOR, IG-VARIATION, ACTION-GR, THETA-XI, RS-SYMBOL
```

and requires that downstream claims not inherit stronger status than those nodes allow.

`RESEARCH-STATUS.md` reinforces the same discipline: VZ is conditional, generation count is
open, weak-field Schwarzschild is bounded, and theta-FLRW cosmology is not a GU-derived
negative-xi result.

## Exact Deliverables

The goal should produce the following artifacts.

1. A primary typed operator specification.

   It must define `D_GU` on the relevant 0/1 sector and the RS sector, including domain,
   codomain, chirality, bundle coefficients, gauge coupling, and principal symbol.

   It must state whether the one-form block contains:

   ```text
   + lambda_d Phi_2(d_A psi)
   ```

   and must fix `lambda_d`. If `lambda_d != 1`, all VZ E-block coefficients must be marked
   for rederivation. If `lambda_d = 0`, the current VZ `F_xi` block is not the primary
   operator's block.

2. A lower-order term ledger.

   It must separate, by name and order:

   ```text
   Phi_2                  algebraic zero-order shiab
   Phi_d := Phi_2 o d_A   first-order differential composite
   Phi_F := Phi_2(F_A tensor -)   zero-order curvature insertion
   F_xi := sigma_1(Phi_d)(xi)     principal-symbol block
   Z_A                    all lower-order operator terms
   ```

   `Z_A` must list spin/gimmel connection terms, mass terms, curvature insertions,
   section-pullback terms, IG/theta terms, boundary terms, and any gauge-fixing or
   constraint terms.

3. A primary action specification.

   It must write `S_GU` as an actual variational functional, not only as prose. It must say
   which terms are present, which are absent in the baseline branch, and which terms are
   primary-sourced optional branches.

   At minimum it must account for:

   ```text
   S_YM[A]
   S_DD[A,Psi;D_GU]
   S_theta[A,epsilon,beta]
   S_W[s]
   S_IG or constraint/multiplier branch
   S_cross if primary-sourced
   S_boundary
   ```

4. A variation-status table.

   It must state, for each object, whether it is fixed, derived, constrained, or varied:

   ```text
   X, Y, g_Y, P, S, Phi_2, s, A, F_A, epsilon, beta, theta, Psi, II_s^H
   ```

   The table must make it impossible to vary `beta` freely while also claiming nonzero
   theta from only the bare theta norm.

5. A full Euler-Lagrange tuple.

   The specification must derive or at least explicitly stage:

   ```text
   E_s = 0
   E_A = 0
   E_epsilon = 0
   E_beta = 0
   E_Psi = 0
   ```

   If `epsilon,beta` are fixed, `E_epsilon,E_beta` must be omitted intentionally and the
   gauge/Noether cost must be stated. If they are constrained, multiplier equations must
   be included. If they are dynamical, the source equation must be rewritten as a
   total-current law rather than bare `D_A^*F_A = theta`.

6. A normalization ledger.

   It must fix:

   ```text
   sign conventions for curvature and metric
   g_A and c_theta normalization
   soldering map j_s and any Clifford trace factor such as 512
   horizontal-normalized II_s^H rather than raw II_s, or an explicit branch change
   volume/fiber normalization for 4D reductions
   canonical scalar normalization B = sqrt(Z_theta) b_raw
   ```

7. A downstream gate map.

   It must state exactly how the specification feeds:

   ```text
   VZ principal-symbol gate
   exact Schwarzschild/Kerr gate
   FLRW theta xi_eff gate
   RS K3/gauge-fixed symbol-index gate
   CHSH / observer-finality physical-forcing gate
   Type II_1 host/selector comparison
   ```

   Each gate must say what is supplied, what remains open, and what would count as
   demotion.

8. A machine-checkable or script-checkable companion, if feasible.

   This can be modest. It need not prove the mathematics. It should prevent status drift by
   checking branch labels, forbidden inputs, and required fields/sections in the spec.

## Acceptance Criteria

The draft goal is achieved only if the resulting specification satisfies all of these.

1. One authoritative object exists.

   A worker can cite one file for the primary `D_GU` and `S_GU` definitions rather than
   stitching them from multiple explorations.

2. Operator order is unambiguous.

   The spec clearly distinguishes `Phi_2`, `Phi_d`, `Phi_F`, and `F_xi`, and states whether
   the VZ first-order block is actually present in `D_GU`.

3. Variation status is non-contradictory.

   The treatment of `epsilon,beta` avoids the free-beta collapse or explicitly accepts
   `theta = 0` as the outcome. No branch may keep nonzero theta by silence.

4. The Euler-Lagrange tuple is sufficient for reduction work.

   Exact Schwarzschild/Kerr and FLRW reductions can begin from written equations rather
   than inferred slogans.

5. Normalizations are auditable.

   No result may depend on silently dropping the `j_s` normalization, changing the
   `Phi_d` coefficient, switching raw `II_s` for `II_s^H`, or reading off `xi_eff` before
   canonical field normalization.

6. Downstream status remains honest.

   The spec does not upgrade VZ, generation count, exact GR, FLRW xi, CHSH, or Type II_1
   selector claims by existing. It only supplies a test object.

7. Failure is usable.

   If the action/operator fails a gate, the spec is sharp enough to say which claim demotes
   and why.

8. No target values are used as inputs.

   The spec may compare against `xi_eff < -0.319`, exact black-hole recovery, or a desired
   generation count only after the relevant object is derived. It may not choose ghost
   complexes, curvature couplings, constraints, or normalizations because they hit the
   target.

## Failure And Demotion Criteria

The work should demote cleanly under the following conditions.

1. No primary `Phi_d` term.

   If the actual `D_GU` contains only `Phi_F` and no `Phi_2(d_A psi)` term in the relevant
   one-form block, the current VZ `F_xi` E-block is not a computation of the primary
   operator. VZ remains conditional and the E-block must be redone.

2. Coefficient drift.

   If the primary action gives `lambda_d != 1`, the existing VZ coefficients such as
   `1/14` and `13/98` may not be imported without a new derivation.

3. Free beta plus bare theta norm.

   If `beta` is freely varied and the only IG term is the bare theta norm, then
   `E_beta` forces `theta = 0`. Nonzero theta, theta dark energy, and the bare source
   equation fail in that branch.

4. Constraint invented only to save theta.

   If the IG constraint is not primary-sourced or geometrically forced, Branch 2A remains a
   reconstruction convenience, not a GU action result.

5. Dynamical IG without source-language update.

   If IG dynamics are added, but downstream prose continues to claim
   `D_A^*F_A = theta` when the actual equation is `D_A^*F_A = theta_eff`, the source claim
   demotes for status drift.

6. Exact black-hole failure.

   If Schwarzschild or Kerr fail the full written vacuum EL tuple, then exact nonlinear GR
   recovery fails or becomes a modified-gravity branch. The weak-field `O(M/r)` result
   remains bounded but cannot be promoted.

7. FLRW xi failure.

   If the reduction gives no scalar theta mode, no `R[g] B^2` term, `xi_eff >= -0.319`, or
   a negative `xi` only by hand insertion, the GU provenance of the DESI-sign theta lane
   fails.

8. RS symbol remains missing or gives another index.

   If the primary operator/action still does not determine the gauge-fixed RS symbol class,
   the generation count remains open. If the computed class gives an incompatible index,
   the generation-count claim must update or fail rather than renormalize the answer.

9. Hidden matter relabeling.

   If exact GR recovery requires treating a section residual, gauge residual, or
   `Q^TF(B_s)` term as matter in a branch advertised as vacuum, the vacuum gate fails.

10. Stale downstream promotion.

   If any canon-facing or roadmap-facing text cites the specification as proof closure,
   the governance layer should reject the upgrade. This goal produces a primary object,
   not automatic success of the gates.

## Dependencies

Hard dependencies:

```text
primary GU source text or transcript passages defining the action/operator
typed carrier conventions from the GU typed operator/action spine
SC1/canon shiab map Phi_2
horizontal-normalized section convention II_s^H
IG variation branch decision or primary-sourced constraint/dynamics
VZ notation reconciliation: Phi_2 / Phi_d / Phi_F / F_xi
RS symbol-index contract and K3 characteristic-class discipline
claim DAG status/finality labels
```

Soft dependencies:

```text
exact Q-sector projectors for VZ
gauge-fixing/BRST convention for physical RS fields
boundary/APS conventions if compact-with-boundary models are used
Pati-Salam finite reduction map for CHSH gates
Type II_1 finite-control bridge if selector/host claims are compared
```

Non-dependencies:

```text
three generations as an input
xi approximately -0.6 as an input
exact Schwarzschild/Kerr as assumed solutions
Bell states inserted by hand as GU evidence
cardinality-three Type II_1 toys as selectors
```

## First Three Concrete Work Packets

### Packet 1: Operator Closure Packet

Write the primary `D_GU` 0/1-sector definition with full typing:

```text
domain, codomain, chirality
d_A^* block
d_A block
Phi_d block and coefficient
Phi_F and all lower-order curvature terms
Z_A ledger
principal symbol sigma_1(D_GU)(xi)
```

Output:

```text
one operator spec section
one table separating Phi_2, Phi_d, Phi_F, F_xi
one explicit decision: VZ current E-block applies / must be rescaled / must be redone
```

Immediate pass/fail:

```text
PASS if the first-order block is fixed and typed.
FAIL/DEMOTE-VZ if the primary operator lacks the assumed Phi_d block.
```

### Packet 2: IG Variation And Action Branch Packet

Resolve the variation status of `epsilon,beta` in the primary action.

Test exactly four branches:

```text
Branch 1: fixed/background Stueckelberg data
Branch 2A: A-independent constrained IG variables
Branch 2B: A-dependent constrained IG variables
Branch 3: dynamical IG / total current
```

Reject the bare free-beta norm branch unless `theta = 0` is intended.

Output:

```text
one action formula S_GU for the chosen branch
variation-status table
E_A, E_epsilon, E_beta source-law statement
explicit source equation: D_A^*F_A = theta or D_A^*F_A = theta_eff
```

Immediate pass/fail:

```text
PASS if nonzero theta is allowed by a primary/geometric variation rule.
FAIL if free beta plus only |theta|^2 is the actual branch.
```

### Packet 3: Reduction Readiness Packet

Derive the reduction-ready equations and normalization ledger.

Output:

```text
full EL tuple
boundary conditions for Schwarzschild/Kerr and FLRW
II_s^H convention and j_s normalization
canonical scalar normalization path for theta FLRW mode
RS symbol data required by the K3/gauge-fixed index gate
downstream gate map with no status upgrades
```

Immediate pass/fail:

```text
PASS if exact black-hole, FLRW xi, and RS index workers can start from equations.
FAIL if any gate still depends on an unspecified action term, hidden variation, or target value.
```

## What This Would Lead To

If successful, this specification would turn the current research surface from a set of
parallel reconstructions into a single falsifiable program.

The immediate follow-on work would be:

```text
1. Recompute the VZ E-block from the actual D_GU and close or demote FC-VZ-1.
2. Run exact Schwarzschild and Kerr against the full EL tuple.
3. Reduce the written action on FLRW and compute Z_theta, C_Rtheta, xi_eff.
4. Construct the physical GU RS gauge-fixed symbol class and compute the K3/APS index.
5. Decide whether CHSH states/observables can be derived from GU zero modes or remain controls.
6. Test Type II_1 proposals against the finite-control shadow supplied by the same spec.
```

The best possible outcome is not a rhetorical upgrade. It is a clean split:

```text
some gates close,
some gates fail,
and every surviving claim knows exactly which primary object it depends on.
```

That would be a major improvement even if several advertised GU outcomes demote. A sharp
failure of the primary action/operator is more valuable than another plausible branch with
undefined variation status.

## Bottom Line

The ambitious goal is:

```text
Write the primary GU action/operator specification strongly enough that the project can stop
arguing about which object is being tested.
```

It should be treated as a root specification for downstream proofs and failures, not as proof
closure itself.

The correct status after drafting it should still be conservative:

```text
primary object specified: possible upgrade if completed
physics claims closed: no, not without the downstream gates
```

## Sources Read

- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/vz-principal-symbol-convention-reconciliation-2026-06-24.md`
- `explorations/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md`
- `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `RESEARCH-STATUS.md`
