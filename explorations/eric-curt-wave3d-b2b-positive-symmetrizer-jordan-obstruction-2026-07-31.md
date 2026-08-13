---
title: "Eric/Curt Wave 3D-B2B: Jordan obstruction kills the full positive symmetrizer cone"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: historical-investigation
registry: lab/process/eric-curt-wave3d-b2b-positive-symmetrizer-jordan-obstruction.json
probe: tests/channel-swings/eric_curt_wave3d_b2b_positive_symmetrizer_jordan_obstruction_probe.py
canon_verdict_change: none
third_lane_promotion: none
---

# Wave 3D-B2B: the positive simultaneous-symmetrizer cone is empty

## Result first

B2A killed the native W131 time flux and its canonical absolute-value
majorant as positive energies, but left open a completely general positive
right-`H` simultaneous symmetrizer. B2B now closes that finite cone on the
same admitted `(3,1)` section and unreduced gamma-traceless carrier.

Let

\[
 C_j=A_t^{-1}A_j,
 \qquad N_\xi=C(\xi)^2-|\xi|^2I.
\]

For `y`, `x`, `z`, and the generic direction `(1,2,3)`, the actual
1,664-dimensional W131 calculation gives

\[
 N_\xi\ne0,\qquad \operatorname{rank}N_\xi=128,\qquad N_\xi^2=0.
\]

For the `y` direction, both characteristic roots `-1` and `+1` have geometric
multiplicity 768. The nonzero square-zero remainder proves that the minimal
polynomial has a repeated root. Thus `C_y` is not diagonalizable even though
its characteristic roots are real.

If a positive matrix `H` satisfied

\[
 H C_y=C_y^\dagger H,
\]

then `H^(1/2) C_y H^(-1/2)` would be Hermitian. It would therefore be
diagonalizable, and so would `C_y`. Contradiction. The full positive
simultaneous-symmetrizer cone is empty before right-`H` is imposed; its
positive right-`H` subcone is empty a fortiori.

The linear symmetrizer equations themselves are not inconsistent. The native
Krein time flux still symmetrizes every `C_j` exactly, but its inertia is the
balanced `(832,832)` found in B2A. The obstruction is positivity, now at the
stronger diagonalizability precondition rather than at one chosen majorant.

## Layer-0 and scope

Three notions that often travel under “hyperbolic” are different here:

1. the characteristic roots are the real Lorentz-null roots;
2. strong hyperbolicity also requires a diagonalizable generator with a
   controlled eigenbasis; and
3. symmetric hyperbolicity requires one positive simultaneous symmetrizer.

The first survives. The latter two fail on the unreduced W131 system.

This is not yet a theorem about the final physical carrier. The current object
is gamma-traceless, not a constructed source- and dynamics-justified
constraint/gauge quotient. A quotient could in principle remove the rank-128
generalized characteristic chains. It must be derived rather than selected
because strong hyperbolicity is desired, must be invariant under the native
dynamics, must preserve the right-`H` and observation structures, and must be
rerun through the Jordan and positive-symmetrizer gates.

The result also does not decide anisotropic or pseudodifferential energies for
a changed/reduced system, variable coefficients, nonlinear Euler constraint
propagation, maximal dissipativity, a propagator, BFV reduction, or the
full-ambient ultrahyperbolic boundary problem.

## Primary-source collision

Disposition: `SOURCE-SILENT`. At local transcript `01:16:13`--`01:17:35` and
`01:25:01`--`01:25:42`, Weinstein distinguishes familiar one-time
Hamiltonian/initial-value methods from the multiple-time ultrahyperbolic
upstairs problem and calls the latter technical debt. He supplies no W131
Jordan computation, positive symmetrizer, constraint quotient, or
record/finality repair. The source fixes context and attribution; it is not
mathematical evidence for the B2B obstruction.

## Constraint and parameter surplus

A general complex Hermitian `1664 x 1664` matrix has `1664^2 = 2,768,896`
real parameters before right-`H` and the three symmetrizer equations are
imposed. B2B does not enumerate that cone or mistake a restricted ansatz for
the whole search. Instead it applies a parameter-free necessary condition:
positive symmetrization implies diagonalizability. One computed generator
violates it. The full semidefinite search is therefore pruned exactly, and the
surplus is negative at the diagonalizability precondition.

## Record/finality candidate

Joe's record/consensus/finality idea remains a `JOE_CANDIDATE_CONTROL`, not an
Eric datum or a third lane. B2B kills it as a selector for the unchanged W131
principal system: assigning an order arrow cannot remove a fixed Jordan block.
It may re-enter only after an independently justified constraint/gauge
quotient or changed principal dynamics is constructed, while continuous
Lorentz time remains distinct from the derived order arrow.

## Curt rival and third-lane gate

Curt's literal real `(7,7)` rival still owes its own principal carrier,
constraint/gauge quotient, Jordan test, positive symmetrizer, domain, and
same-space discriminator. Common complexification does not transport the
Eric-lane W131 result. `TG-1 AND TG-2 AND TG-3` remains false, so Curt stays a
formally separated rival inside the Eric lane and no third lane is promoted.

## Probe and next gate

The executable probe records `31 exact + 13 planted = 44 PASS`. It tests the
three coordinate directions plus `(1,2,3)`, the rank/square-zero Jordan
certificate, the exact indefinite symmetrizer, provenance, Layer-0 scope,
record/finality boundary, campaign handoff, and planted overclaims.

The next gate is
`ECW3D-B2C-CONSTRAINT-GAUGE-QUOTIENT-JORDAN-REMOVAL`: construct the actual
invariant constraint/gauge quotient, determine whether it removes every
rank-128 generalized characteristic chain, and only then rerun the positive
right-`H` symmetrizer and boundary maximal-dissipativity tests.
