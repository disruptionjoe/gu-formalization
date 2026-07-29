---
run_id: GUH-20260729T211122Z-three-route-construction-wave
status: completed
repository: gu-formalization
workflow: joe-directed-science-council-wave
mode: execute
run_type: progress
lane_id: "1"
work_item: THREE-ROUTE-CONSTRUCTION-WAVE
starting_revision: f29e610fe76c
opened_at: 2026-07-29T21:11:22Z
completed_at: 2026-07-29T21:33:34Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260729T211122Z-three-route-construction-wave/run-plan.md
  - explorations/bott-krein-full-carrier-admission-2026-07-29.md
  - tests/channel-swings/bott_krein_full_carrier_admission_probe.py
  - explorations/vertical-source-action-reduction-and-hessian-start-2026-07-29.md
  - tests/channel-swings/vertical_source_action_reduction_probe.py
  - explorations/actual-fibre-cperp-b5-naturality-start-2026-07-29.md
  - tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py
  - explorations/three-route-construction-wave-synthesis-2026-07-29.md
  - explorations/README.md
  - tests/README.md
---

# Three-route construction wave

## Authorization and purpose

Joe directly requested a coordinated wave to give each science-council approach
a concrete start.  This is a Lane-1 North-Star construction wave, not a
hardening sweep.  Its purpose is to produce one discriminating executable
foothold for each of the three live routes:

1. full-carrier Bott--Krein admission;
2. vertical source-action reduction and vacuum dynamics; and
3. actual-metric-fibre `C_perp` / B5 naturality.

The completed but untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` receipt is outside the
write boundary and must remain untouched.

## Shared construction discipline

Layer 0 runs before any structural or numerical inference.  In particular:

- a linear right-quaternionic Bott deck grading is not an antilinear
  contragredient coflip merely because both carry a sign;
- clutching degree, quaternionic index, complex index, physical chiral index,
  and multiplicity are different objects;
- a vertical universal-connection component is not automatically a dynamical
  four-dimensional scalar;
- Krein-line monodromy, an associated-bundle duality, and normalized B5 slot
  phases are different objects until their maps are built.

The load-bearing fork is program-native:

| object | program-native construction used | hostile/standard control |
| --- | --- | --- |
| state pairing | indefinite Krein pairing, composed into the bilinear | positive-Hilbert pairing |
| carrier | full `Cl(9,5)=M(64,H)` / RS carrier | a chosen single `H` line |
| metric fibre | `S^2 T*X` with DeWitt/gimmel metric | `Lambda^2 + Lambda^3` exterior ten |
| count | physical Fredholm/chiral index, still open | multiplicity or clutching degree |
| mass | paired projected vertical connection coupling | freely added scalar/matrix multiplet |

No kill is accepted until the lane states which fork it lives on and whether
the other fork changes the result.  No multiplicity or decomposition may be
reported as a count.

## Common return contract

Each lane must return:

1. an explicit Layer-0 object/map table;
2. a minimal executable probe with at least one planted discriminating control;
3. a typed `PASS`, `KILL`, or `OPEN-AT-NAMED-MAP` verdict;
4. a predeclared parameter/choice count sufficient to say whether constraint
   surplus is positive, nonpositive, or currently uncomputable; and
5. the smallest source-owned next construction.

The wave is successful if every lane produces a reusable start, even when the
scientific verdict is a kill.  It does not require any route to pass.

## Lane A — full-carrier Bott--Krein admission

### Decision question

Can the existing GU carrier support a canonical Bott mass and native linear
deck action without choosing one quaternionic coordinate, importing a new
doubling, or confusing clutching degree with physical index?

### Required first gates

Construct or fail closed on

```text
S_nat = C_perp J_H
S_nat^2 = 1
[S_nat, R_H] = 0
S_nat M(q) S_nat^-1 = M(-q)
```

and test RS preservation/gap on the full available carrier.  The lane must
separately report the natural diagonal `H^64` multiplicity and any claimed
Clifford--Morita reduction.

### Preregistered expectation and kills

Expected verdict:
`FULL-CARRIER-UNIT-CLASS-OPEN-OR-OBSTRUCTED`, with the degree-one `H`-line
control surviving but no canonical native reduction from 64 copies to one.

Kill the unit-class/P3 weld if degree one requires a rank-one `H` projector,
if the only natural lift remains 64-fold with no pre-existing functorial
Morita map, if the Bott doubling is not an existing GU mirror pair, or if RS
compression leaks/closes the gap.  Do not repair `S_nat^2=-1` with a freely
inserted complex `i`.

## Lane B — vertical source-action reduction and Hessian

### Decision question

Does the written T1+T2 action actually retain a dynamical vertical field
`Phi_i`, and what is the first source-owned Hessian/closure statement one can
derive before positing a new T10 sector?

### Required first gates

Write the reduction

```text
A = A0 + a_parallel + Phi_i eta^i
F_A = F0 + D0 Phi + Phi wedge Phi + non-holonomic terms
M_Phi = Pi_RS K sum_i c(e_i) rho(Phi_i) Pi_RS
```

and distinguish the vertical connection carrier, the `S^2T*X` metric/Hessian
fluctuation, and the C10 distortion response.  Establish whether the
integration/pullback arena keeps or erases `Phi`.  Build the smallest exact
finite comparator that detects an omitted mixed term, a non-closed scalar
truncation, or gauge-null Hessian directions.

### Preregistered expectation and kills

Expected verdict:
`VERTICAL-CARRIER-EXISTS-DYNAMICAL-HESSIAN-UNDERDETERMINED`.

Kill the native vertical-Higgs reading if pullback removes `Phi`, if the
restricted Euler--Lagrange derivative leaks outside the proposed scalar
sector, or if the physical Hessian is nonnegative/flat with no source-owned
selection.  A flat or degenerate branch is not a global kill: it licenses the
external-datum branch-selection reading and, only after a loop-adequate
regulator exists, a T2 effective-potential attempt.

## Lane C — actual-fibre `C_perp` / B5 naturality

### Decision question

Does the verified metric loop on the actual
`TX + S^2T*X` DeWitt carrier transport the full paired reality structure and
all 20 B5 slot maps by one central sign/local-system character?

### Required first gates

Start from `g_t = B_t^T eta B_t`; construct its induced action on
`TX + S^2T*X`, and transport as much as the repository data canonically fixes
of `K`, `J_obs`, `J_H`, chirality, both RS projectors, and the 20 provenance
slots.  Form the returned mismatch

```text
C0 = K0 J0
C1 = returned K1 J1
U = C0^-1 C1
```

and report whether `U` is one central scalar or has residual
block/family/provenance moduli.

### Preregistered expectation and kills

Expected verdict:
`K-LINE-MONODROMY-EXACT-C_PERP-ASSOCIATED-MAP-OPEN`.

Kill the one-bit P1/P2 merger if the induced `S^2` loop maps trivially or
differently into the `(9,5)` frame carrier, if `J_obs` has no global
lift/connection-independent return, if admissible lifts change relative slot
phases, or if either RS projector or any special-edge support is not
preserved.

## Integration rule

The full-carrier gate is a bounded preflight, not a substitute for the source
action.  If it passes, Lane B should test dynamics inside the admitted Bott
sector.  If it fails, Lane B continues with the ordinary vertical orbit and
Lane C may still support a P1/P2 orientation weld.  P3 remains separate unless
an actual physical index map is constructed.

## Planned validation

- Run each new probe and its planted controls.
- Re-run the nearest existing vertical-Krein, B5 habitat, and clutching
  controls without overlapping heavy builds.
- Compile all new Python probes.
- Run `git diff --check`.
- Integrate the three dispositions without collapsing dissent.
- Commit and push the coherent wave; close with the scoped session-sync guard.

## Execution and result

### Lane A — direct Bott--Krein admission killed

The exact factorized `Cl(9,5)` probe constructs

```text
S_nat = C_perp J_H.
```

It is a complex-linear, Krein-unitary involution with balanced complex
eigenspaces `64+64`, and its induced signed vector action preserves
`ker Gamma`.  It anti-commutes with the quaternionic structure and therefore
is not right-`H`-linear.  Multiplication by `i` restores right-`H`-linearity
but changes the square to `-1`.  No allowed phase satisfies both gates.

The conventional doubled `H`-line Bott control remains self-adjoint,
right-`H`-linear, deck-equivariant, and unit-gapped.  Its natural diagonal
`H^64` lift scales the nonzero local clutching density by exactly 64.  A
planted single-coordinate projector returns one copy only by failing a
carrier-mixing naturality control.

Verdict:

```text
KILL-S_NAT-H-LINEAR-DECK
FULL-CARRIER-BOTT-OPEN-AT-NATIVE-MIRROR-AND-MORITA-MAP
```

No clutching multiplicity is reported as an index.  No physical index is
computed.

### Lane B — ambient curvature built; physical reduction not supplied

Layer 0 separates the ambient connection
`A_Y in Omega^1(Y,ad P)` from the displayed source-action field
`A_X in Omega^1(X,ad P_X)`.  Literal section pullback annihilates a vertical
one-form on a horizontal section or folds it into an `X4` one-form; it does
not retain an independent scalar `Phi_i`.

The lane writes the complete non-holonomic curvature blocks

```text
F_AB = F0_AB + D0_A a_B - D0_B a_A
      + [a_A,a_B] - C_AB^C a_C
```

and the formal ambient Yang--Mills Hessian.  The exact comparator catches an
omitted frame-structure term, an omitted vertical derivative, a nonclosed
scalar truncation, and a planted lifting of a gauge-null direction.

Verdict:

```text
VERTICAL-CARRIER-EXISTS
X4-DYNAMICAL-RETENTION-MAP-UNBUILT
FORMAL-AMBIENT-HESSIAN-BUILT
PHYSICAL-HESSIAN-UNDERDETERMINED
```

No vacuum, VEV, unbroken algebra, or mass spectrum is claimed.

### Lane C — actual DeWitt lift built; normalized slot map remains

For the real metric loop `h_t=B_t^T eta B_t`, the actual induced gimmel frame
is

```text
B_t^-1 on TX
E -> B_t^T E B_t on Sym^2T*X.
```

The endpoint reverses `(1 positive,1 negative)` base legs and
`(2 positive,2 negative)` DeWitt legs.  The full `(9,5)` return therefore
reverses three positive and three negative legs, giving exact Krein-line
monodromy `-1`; the doubled loop gives `+1`.

A reference Clifford lift returns the distinct `J_obs` and `J_H`, preserves
both gamma-traceless projectors with ranks `12` and `288`, and gives the
central irreducible-spinor mismatch `C0^-1 C1=-I`.  This does not fix the
normalized 20-slot transport.  The sign-only support commutant still admits
`2^10` mirror-pair assignments, or `2^9` relative classes after one global
sign.  A planted noncentral member passes a permissive support matcher and
fails the strict centrality test.

Verdict:

```text
K-LINE-MONODROMY-EXACT
C_PERP-ASSOCIATED-MAP-OPEN
```

The P1/P2 one-bit weld remains conditional.

## Integrated handoff

The lanes meet at one next packet rather than three unrelated hardening
campaigns:

```text
source-owned Y14-to-X4 reduction or explicit ambient-action decision
  -> written first-order RS differential
  -> normalized transport on all 20 B5 bundles
  -> possible native mirror pair for a different Bott admission.
```

The next construction is
`SOURCE-OWNED-REDUCTION-TRANSPORT-PACKET`:

1. freeze the action arena;
2. compute `D_A0^*F_A0` for the W177 background before interpreting its
   Hessian physically;
3. build and test a gauge-covariant mode/reduction datum and full
   Euler--Lagrange closure;
4. use the same differential to derive normalized slot transport and the
   formal-adjoint sign; and
5. reopen Bott only if that transport supplies a dimension-matched,
   right-`H`-linear native mirror involution and RS-preserving mass.

P3 remains a separate physical-index datum.  `T10` is not required merely to
exhibit the algebraic mass carrier, but this run does not show that a new
dynamical term is unnecessary if the reduction and T1/T2 dynamics fail.

## Validation

All passed:

- `tests/channel-swings/bott_krein_full_carrier_admission_probe.py`;
- `tests/channel-swings/vertical_source_action_reduction_probe.py` (`11/11`);
- `tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py`;
- `tests/channel-swings/vertical_krein_weld_probe.py`;
- `tests/channel-swings/sig_b5_habitat_probe.py`;
- `tests/channel-swings/fredholm_end_clutching_gate.py`;
- `tests/shiab_b5_observer_symbol_multiplicity_matrix.py`;
- Python compilation for all three new probes;
- exact `channel-swings` inventory count `125`;
- repository navigation checks for the new artifacts; and
- `git diff --check`.

Every new candidate carries a Layer-0 map and the ratified L1--L7
classification.  The controls distinguish program-native Krein/DeWitt
objects from the positive-Hilbert, one-`H`-line, and exterior-ten controls.

## Receipt

- Result vocabulary:
  `KILL-S_NAT-H-LINEAR-DECK + X4-RETENTION-MAP-UNBUILT + K-LINE-MONODROMY-EXACT-C_PERP-ASSOCIATED-MAP-OPEN`.
- Service outcome: `completed`.
- First residual: the source-owned reduction-and-transport packet above.
- Scientific grade: exact finite/frame algebra where stated; construction
  and comparator grade for the ambient curvature/Hessian; reconstruction
  for the missing reduction, normalized slot transport, and Bott/Morita
  bridge.
- Claim, canon, verdict, count, paper, portfolio, and public-posture changes:
  none.
- P1/P2 merger: conditional and not booked.
- P3: separate and unmoved.
- Unrelated dirty artifact
  `GUH-20260729T131135Z-b5-native-packet-source-audit` preserved untouched.
