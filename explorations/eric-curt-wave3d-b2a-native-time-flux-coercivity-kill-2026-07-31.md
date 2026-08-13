---
title: "Eric/Curt Wave 3D-B2A: native time flux does not supply a coercive energy"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: historical-investigation
registry: lab/process/eric-curt-wave3d-b2a-native-time-flux-coercivity-kill.json
probe: tests/channel-swings/eric_curt_wave3d_b2a_native_time_flux_coercivity_probe.py
canon_verdict_change: none
third_lane_promotion: none
---

# Wave 3D-B2A: native time flux and coercive energy

## Result first

The admitted Lorentzian section does have a perfectly good continuous local
time coordinate: its W131 time symbol is invertible, with singular values
between `6/7` and `1`. What fails is the next inference. The native Krein time
flux is not a positive energy. Its exact computed spectrum is

\[
-1\ (768),\quad -6/7\ (64),\quad 6/7\ (64),\quad 1\ (768),
\]

so its inertia is balanced `(832,832)`.

The most canonical repair also fails. Taking the spectral absolute value
`H_t=|E_t|` produces a positive, right-`H`-compatible matrix with spectrum
`6/7` (multiplicity 128) and `1` (multiplicity 1536). But a positive matrix is
an evolution energy only if it symmetrizes every spatial evolution matrix
`C_j=A_t^{-1}A_j`. It does not: the three Hermiticity defects are approximately
`0.1694`, `0.1652`, and `0.1834` for `y,x,z`.

Therefore the native time flux and its canonical spectral majorant do not
supply a positive coercive symmetric-hyperbolic energy. Maximal dissipativity
is not reached for this candidate because the positive-energy gate fails
first. This does **not** kill every possible positive symmetrizer, anisotropic
energy, or variable-coefficient domain.

## What this says about time

Three different objects must stay separate:

1. `t` is a continuous Lorentz coordinate on the admitted `(3,1)` section.
2. Upstairs `Y^14` has several temporal directions and an ultrahyperbolic
   boundary problem rather than this ordinary one-time initial-value problem.
3. An arrow induced by records, consensus, or finality would be an additional
   ordering/orientation structure, not the Lorentz coordinate itself.

The calculation shows why an arrow alone is not yet enough: even choosing the
spectral sign and making the time flux positive does not symmetrize the spatial
dynamics. A record/finality proposal can still be useful, but it must construct
a full right-`H` positive symmetrizer rather than merely label one direction
“future.”

## Primary-source collision

Disposition: `SOURCE-SILENT`. At local transcript `01:16:13`--`01:17:35` and
`01:25:01`--`01:25:42`, Weinstein explicitly distinguishes zero-, one-, and
multiple-time equations. He says one time supports familiar Hamiltonian and
initial-value methods, while the multiple-time upstairs theory is
ultrahyperbolic, uses boundary conditions, and remains technical debt.

That statement confirms the importance and intended scope of the problem. It
does not supply the W131 time-flux spectrum, a positive symmetrizer,
maximal-dissipative data, nonlinear constraint propagation, or a
record/finality arrow. The B2A computation is a repo addition, and the source
is not mathematical evidence for it.

The same collision retroactively corrects ECW3C: ECW3C killed the ordinary
full-ambient Lorentzian Cauchy reading, not every ultrahyperbolic boundary
formulation.

## Construction and computation

On the same admitted stationary slab used in B1, restrict the ambient W131
operator to `ker Gamma` and write its principal equation as

\[
A_t\partial_t u+A_y\partial_y u+A_x\partial_x u+A_z\partial_z u=0.
\]

Let `K` be the inherited Krein form. Formal Krein symmetry makes each
`E_mu=K A_mu` Hermitian. The time energy candidate is `E_t`. It is invertible
but indefinite. Its spectral sign `Theta_t=sign(E_t)` is a right-`H`-compatible
Hermitian involution, and

\[
H_t=\Theta_t E_t=|E_t|>0.
\]

For a symmetric-hyperbolic energy, however, every `H_t C_j` must be Hermitian.
The exact carrier computation finds a nonzero defect for all three spatial
directions. Thus positivity of `|E_t|` is a majorant only in the static Krein
sense; it is not an evolution symmetrizer for this first-order system.

The probe records `27 exact + 12 planted = 39 PASS` when the registry and
campaign handoff agree.

## Boundary, constraint, and surplus limits

The native `y`-normal Green form remains Hermitian, balanced, and right-`H`
compatible, so the opposite trace sectors from ECW3D-A still exist. But they
cannot be promoted to maximal-dissipative incoming/outgoing data for the
failed positive-energy candidate.

The candidate chose one time function and one canonical spectral majorant. It
fails the simultaneous spatial symmetrizer constraints, so its surplus is
negative. The general parameter/constraint surplus is still uncomputable
until the positive right-`H` symmetrizer cone is solved or shown empty.

Pointwise `ker Gamma` and right-`H` preservation remains distinct from
nonlinear Euler constraint propagation. No propagator or physical BFV phase
space is obtained.

## Curt rival and third-lane gate

Curt's literal real `(7,7)` construction still owes its own time/boundary
form, positive symmetrizer, domain, and same-space discriminator. Nothing in
the common complex carrier transports this B2A result.

The pre-registered gate remains `TG-1 AND TG-2 AND TG-3`. `TG-1` is partial;
`TG-2` and `TG-3` are open. No third lane is promoted. Joe's record/finality
idea is retained as a `JOE_CANDIDATE_CONTROL` inside the next Eric-lane test,
not promoted to a lane or treated as author-supplied input.

## Next gate

`ECW3D-B2B-POSITIVE-RIGHT-H-SYMMETRIZER-SEARCH` should solve the finite linear
matrix constraints

\[
H>0,\qquad HJ=J\bar H,\qquad HC_j=(HC_j)^\dagger
\quad(j=y,x,z),
\]

before returning to variable coefficients. If the feasible cone is nonempty,
test its boundary flux and maximal dissipativity; if an explicit
record/finality selector is proposed, require it to land in that cone without
target-sign labeling. Only after that should the nonlinear Euler constraints
be tested.

Still open: a global Lorentz/spin section, any full-ambient ultrahyperbolic
domain, a general section energy symmetrizer, maximal dissipativity, nonlinear
constraint propagation, a propagator, and physical BFV reduction.
