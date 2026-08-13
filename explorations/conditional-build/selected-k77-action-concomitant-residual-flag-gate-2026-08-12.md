---
artifact_type: conditional_build_result
created: 2026-08-12
status: SELECTED_LORENTZ_INVARIANT_ACTION_CONCOMITANTS_EXACTLY_NONSELCTING__NONHOMOGENEOUS_SUCCESSOR_LIVE
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_GEOMETRIC_REDUCTION_AND_GAUGE_ROTATED_CONNECTION_INGREDIENTS__SOURCE_SILENT_ON_ACTION_DERIVED_HQ_SELECTOR__SOURCE_CORRECTS_ANY_CLAIM_THAT_FAILURE_OF_THIS_BACKGROUND_REFUTES_SC_GRP_03
ledger: lab/process/conditional-physics-ledger-v0.190.json
canon_verdict_change: none
---

# Selected K77 action-concomitant residual-flag gate

## Result in plain English

The action and geometry already built do not select the remaining
complex--Cartan flag on the current Lorentz-invariant stationary background.
They distinguish the one-dimensional metric-trace direction from the
nine-dimensional traceless metric directions, but nothing finer.

This is an exact scoped result, not a global no-go.  The curvature and complete
second-fundamental tensor on a nonhomogeneous stationary solution can break the
large Lorentz stabilizer and remain live.  The separate compatibility map from
the full `U(64,64)` connection, or Curt's possible two `U(32,32)` halves, to the
fourteen-dimensional K77 connection also remains open.

## Pre-wave and Layer 0

- No residual flag, pairing horn, parent-unitary projection or external datum
  is assumed.
- The search is wholesale only for natural zero-order endomorphism words on
  the current Lorentz-invariant background.
- No fitted rank, basis, spectral threshold, complex structure or frame is
  admitted.
- `H` is an endomorphism concomitant, not the physical action Hessian.
- `Q=[H_a,H_b]` is not charge conjugation, a Dirac operator or a supplied `J`.
- `A^P` is affine connection data; its curvature and `N=nabla P` are tensorial.
- The constant section is not assumed totally geodesic.  Its full nonzero
  second-fundamental contribution is included by the commutant theorem.

## Exact construction

On `V=Sym^2(T^*X)` the probe constructs the six Lorentz generators and solves
the complete 100-variable centralizer problem.  The centralizer has dimension
two:

```text
End_SO(1,3)(V) = span{I, P_trace} = span{I, T_trace}.
```

Consequently every natural self-adjoint word made from the invariant
distortion, curvature or full second-fundamental tensor has one eigenvalue on
the trace line and one on the traceless nine-plane.  A gapped sign projector
therefore has rank only `0,1,9,10`, never the rank four required by the RB5
coarse-flag recovery grammar.

The native trace-reversed DeWitt form has inertia `(6,4)` and a negative trace
line.  Direct contraction, rather than coefficient assignment, gives

```text
H_T = I,
H_F = 9 I.
```

The general Lorentz-natural `H_II` is retained with independent trace and
traceless eigenvalues.  All commutators among these words vanish exactly, so
`Q=0` and the polar formula `J=Q(-Q^2)^(-1/2)` has no invertible branch.

The certificate passes `42/42`: fifteen exact algebra checks, one explicit
geometry fence, two bundle checks, two spectral checks, one polar check, four
prior-art checks, one source check, four type checks, nine scope checks and
three planted failures.  The plants reject a hand-selected rank-four
projector, a supplied complex structure and promotion of an affine connection
value to a tensorial selector.

## What this closes and what remains

Closed:

- the current Lorentz-invariant natural `H,Q` selector class;
- the idea that trace-centering those same words creates a finer anisotropy;
- use of `A^P` itself, rather than curvature or `nabla P`, as a tensorial
  selector.

Open:

- the smallest action-stationary nonhomogeneous reduced-curvature plus full-`II`
  orbit;
- a rank-four spectral gap and invertible positive-real polar `Q` there;
- stabilizer comparison with the desired residual flag;
- full-unitary/two-half projection to the K77 vector connection;
- lower-order Riccati, barred-adjoint and BV/KT closure after flag ownership.

No ledger verdict, residue, quotient, P1/P2/P3 assignment, canon verdict or
public posture moves.

## Next gate

Construct the smallest target-blind action-stationary nonhomogeneous orbit
carrying reduced curvature and the complete second-fundamental tensor.  Re-run
the exact centralizer, spectral-gap, polar and stabilizer tests.  If the orbit
still has only the trace/traceless algebra, the action route narrows again; if
it emits a noncommuting gapped pair, test whether its flag is the required one
without fitting it.
