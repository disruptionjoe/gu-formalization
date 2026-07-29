---
run_id: GUH-20260729T231156Z-source-owned-reduction-transport-packet
status: completed
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-REDUCTION-TRANSPORT-PACKET
starting_revision: 2e0fc773c91abb7ad943537f359c0c0e46aa8de9
opened_at: 2026-07-29T23:11:56Z
completed_at: 2026-07-29T23:33:12Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260729T231156Z-source-owned-reduction-transport-packet/run-plan.md
  - explorations/source-owned-reduction-transport-packet-2026-07-29.md
  - tests/channel-swings/w177_ym_residual_and_mode_closure_probe.py
  - tests/channel-swings/b5_normalized_transport_from_differential_probe.py
  - explorations/README.md
  - tests/README.md
---

# Source-owned reduction-and-transport packet

## Authorization and purpose

Joe said “Go” after the completed three-route construction wave identified one
integrated next packet. This run attacks that packet in dependency order:

1. freeze the action arena;
2. test the W177 background against the Yang--Mills Euler--Lagrange equation;
3. attempt retained-mode closure only if the stationarity/type gates permit it;
4. derive as much normalized B5 transport as the same written differential
   actually fixes.

This is a Lane-1 construction run. It is not a source-action status promotion,
a vacuum claim, a physical index computation, or permission to choose missing
B5 phases.

The completed untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` receipt is outside the
write boundary and remains untouched.

## Layer 0: action arena and object identity

The run admits one explicit conditional branch:

```text
arena: Y14 = Met(X4)
action: S_YM[A] = alpha integral_Y <F_A,F_A>
candidate background: A0 = spin-lift(nabla^gimmel)
```

The identification of the Yang--Mills IG connection with the gimmel
Levi--Civita spin connection is a declared candidate identification, not a
derived equality:

| shared term | object in W131/W177 | object in the source action | mark |
| --- | --- | --- | --- |
| `A` | metric-compatible `so(9,5)` connection on the tangent/spin/RS bundle | IG gauge connection varied in `T1` | **HOMONYM, conditionally identified for this candidate** |
| `F_A` | Riemann curvature represented on the RS bundle | Yang--Mills curvature of the varied IG field | **SAME only under the conditional identification** |
| `D_A^*F_A` | divergence of the represented Riemann curvature | Yang--Mills Euler--Lagrange residual | **SAME only on the ambient candidate branch** |
| source action | ambient `Y14` Yang--Mills sector assumed in dark-energy canon | displayed Seiberg--Witten candidate integral on `X4` | **HOMONYM; no descent asserted** |
| vertical scalar | vertical coefficient of an ambient tensorial connection fluctuation | independent `X4` Lorentz scalar | **HOMONYM until a mode reduction is built** |

No result on this branch transfers automatically to the written `X4` action.
Literal pullback is already known not to retain an independent scalar.

## Construction fork

Program-native objects are used where load-bearing:

- the actual `TX + Sym^2T*X` gimmel carrier, not the exterior numerical ten;
- the indefinite `(9,5)`/Krein pairing, not a positive-Hilbert replacement;
- the gamma-traceless RS bundle and its written first-order differential;
- physical index, multiplicity, Krein-line monodromy, and B5 phase remain
  distinct codomains.

The standard differential-geometric control is the Levi--Civita Yang--Mills
identity: the frame connection is Yang--Mills exactly when the represented
curvature has zero covariant divergence. For Levi--Civita curvature this is
equivalent to the Ricci tensor being Codazzi:

```text
(D_A0^* F_A0)_{MJ,L}
  = nabla_M Ric_{LJ} - nabla_J Ric_{LM}
```

up to the fixed sign convention for the codifferential. Zero versus nonzero
is convention-independent.

## Ratified protocol contract

Layer 0 is above. L1--L7 for this candidate are:

| axis | class |
| --- | --- |
| L1 substrate | smooth principal/associated bundle on the specific smooth `Y14` |
| L2 observer | no computational observer; an `X4` section/mode projector is not admitted until built |
| L3 pairing | smooth gauge pairing with gimmel/Krein invariant forms |
| L4 causal order | ambient multi-time `(9,5)` pseudo-Riemannian arena; no global single-time order claimed |
| L5 emergence | specific object, no RG/universality claim |
| L6 coordination loop | none |
| L7 positivity | indefinite gimmel/Krein; no positive-state quotient or probability rule supplied |

The construction does not claim a substrate-class escape from a chirality or
anomaly no-go.

## Preregistered expectations and kills

Expected first verdict:
`W177-YM-STATIONARITY-OPEN-UNTIL-COMPUTED`.

Controls and dispositions are frozen before computation:

1. Compute the residual at the exact deterministic W177 point over several
   independent finite-difference scales.
2. Require Ricci symmetry, metric compatibility, contracted-Bianchi
   agreement, and a planted parallel-Ricci zero control before reading the
   residual.
3. Require a planted non-Codazzi symmetric tensor to return nonzero.
4. If the residual is robustly nonzero, kill the interpretation of the W177
   quadratic form as a physical mass Hessian. Do not kill the ambient
   connection carrier or the algebraic vertical--Krein channel.
5. If the residual vanishes, test the full vertical/horizontal Hessian
   off-diagonal block and gauge nulls before reading any restricted
   eigenvalue.
6. If the action/background type identification itself fails, report
   `L0-HOMONYM-NOT-CLOSED` rather than a stationarity verdict.
7. Normalized B5 transport may be reported only from an explicit
   connection/differential on the twenty bundles. A support permutation,
   frame orientation, or central irreducible-spinor return cannot select the
   nine relative signs.

## Constraint-surplus precommitment

- Stationarity test: no fitted parameter; the W177 point, gimmel metric, and
  Levi--Civita connection are frozen. The zero residual is a positive-surplus
  consequence, not a fit.
- A reduced `X4` mode theory remains `SURPLUS-UNCOMPUTABLE` until its section,
  mode space, measure/domain, gauge subalgebra, and closure map are written.
- B5 support transport begins with nine relative binary choices and zero
  source-owned relative-phase equations. Any reduction of that freedom must
  come from the written differential, not from selecting a favorable
  extension.

## Planned validation

- Run the new stationarity/closure probe and every planted control.
- If a B5 transport probe is warranted, run it with a planted noncentral
  support-preserving assignment.
- Re-run W177, the vertical reduction comparator, actual-fibre transport, and
  native packet fail-closed controls.
- Compile new Python probes without writing cache files into the repository.
- Update only the navigation indexes needed for new artifacts.
- Run `git diff --check`, commit, push, and close through scoped session sync.

## Completion receipt

The packet returned two independent gates and one sharpened construction
target:

1. `W177-AMBIENT-YM-NONSTATIONARY`. At the exact deterministic W177 point,
   the orthonormal-frame residual norms are
   `3.19904935`, `3.19904137`, and `3.19903939` across the three derivative
   scales. Relative spread is `3.11e-6`; signal/control-floor separation is
   `858.6`. The physical-Hessian interpretation at that background is killed,
   and retained-mode closure did not run.
2. `B5-NORMALIZED-TRANSPORT-NOT-DETERMINED-BY-W131-DIFFERENTIAL`.
   Layer 0 identifies W131 as a proper suboperator on 12/20 slots. Even its
   optimistic 40-cell carrier envelope leaves `2^4` relative endpoint-sign
   classes. A planted noncentral return passes that envelope and is rejected
   by the complete graph.
3. The complete 136-cell graph is connected. An exact search shows that at
   least four formal-adjoint/mirror symbol orbits must be added to the W131
   envelope merely to connect all twenty slots. This is a lower-bound target
   for the next written chimeric/BV differential, not a selected coefficient
   table.

Integrated result:
`TWO-GATES-FAIL; ONE-CONSTRUCTION-TARGET-SHARPENED`.

No claim, canon verdict, source-action row, physical index, count, B5 phase,
vacuum, or public posture changed.

Validation receipt:

- both new probes pass every predeclared and planted control;
- original W177 curvature/C2 carrier: `17/17` pass in the shared
  NumPy/SciPy research environment;
- vertical source-action reduction comparator: `11/11` pass;
- actual-fibre `C_perp`/B5 naturality start: all checks pass;
- native B5 packet ingress remains fail-closed and passes its contract; and
- both new probes compile with repository bytecode redirected outside the
  worktree; `git diff --check` passes.
