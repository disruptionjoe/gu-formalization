---
run_id: GUH-20260729T194945Z-vertical-krein-weld
status: completed
repository: gu-formalization
workflow: repo-progress-run
mode: execute
run_type: progress
lane_id: "1"
work_item: VERTICAL-KREIN-WELD
starting_revision: 3ea2186a31f2ed30c55d4ef20413aa09cdc7fd36
opened_at: 2026-07-29T19:49:45Z
completed_at: 2026-07-29T20:24:44Z
claim_status_change: none
canon_change: none_planned
public_posture_change: none_planned
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260729T194945Z-vertical-krein-weld/run-plan.md
  - explorations/sa-y8-majorana-layer0-and-vertical-krein-weld-2026-07-29.md
  - explorations/README.md
  - explorations/source-action-term-by-term-against-the-spec-2026-07-29.md
  - explorations/krein-paired-bilinear-chirality-2026-07-29.md
  - explorations/b5-chirality-orientation-audit-2026-07-29.md
  - explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md
  - explorations/layer0-pass-on-the-2plus1-count-claim-2026-07-29.md
  - tests/channel-swings/vertical_krein_weld_probe.py
  - tests/README.md
  - NEXT-STEPS.md
  - LANE-STATE.yaml
  - lab/process/research-portfolio.json
---

# Vertical--Krein weld

## LaneSelection

- **Owner/scope:** `gu-formalization`, repository-local scientific truth.
- **Lane:** Lane 1, Observerse/GU truth status.
- **Manifest digest:** `sha256:a0348a5b7977d32fe927d765fe9cab8315dacc770079d79b14ecfa7f1178c8b7`.
- **Definition/control revision:** Lane definition revision `2`; control revision `2`; manifest revision `3`.
- **Selected work and basis:** Joe authorized execution after a deep repository review. The supplied handoff
  fixes the order: resolve the live `SA-Y8` contradiction at Layer 0; identify whether the corrected physical
  bilinear `K e_vertical` reaches the `Lambda^0` channel required by `SA-Y1`; then determine what, if anything,
  the same construction says about the B5 `P2` datum.
- **Context capsule:** Rung 1 makes index grading-determined; Rung 2 makes the wall sector supplied; the
  corrected Krein probe shows that the pairing is load-bearing and reverses the bare-operator chirality
  verdict. The current B5 packet audit is complete and blocked because none of five native packet fields is
  independently fixed. The run must construct before hardening and must not infer count from multiplicity.
- **Effective permission:** Joe-directed Progress inside the declared write boundary; no scientific-status
  transition, canon promotion, non-GitHub external action, or cross-repository write.
- **Emergency revocation evidence:** Lane 1 is active with `continue_current`; the repository writer-lock path
  was absent at admission; scoped session sync passed while preserving the unrelated completed B5 run receipt.

## Construction fork

The load-bearing construction is program-native: `Cl(9,5) = M(64,H)`, the Krein pairing is part of the
physical bilinear, and the vertical carrier is the symmetric metric fibre `S^2 T*X`, not the exterior
`Lambda^2 + Lambda^3` comparator. Standard positive-Hilbert and complex-representation calculations may be
used only as named controls. Any kill must state whether it survives the other construction.

## Decision sequence

1. **Layer 0 / `SA-Y8`.** Compare the exact mathematical objects denoted by “Majorana block” in the
   Seiberg--Witten source-action canon and in `SHIAB-05`. Mark each shared term
   `SAME-OBJECT`, `HOMONYM`, or `UNCERTAIN`; name the relating map.
2. **Channel / `SA-Y1`.** Compose the physical pairing before asking the channel question. Determine whether
   `Psi^dagger K c(a_perp) Psi` is merely a scalar-valued bilinear after a supplied vertical vector, or an
   invariant `Spin(9,5)` `Lambda^0` carrier of the type required by the source-action row.
3. **B5 / `P2`.** If the same frozen construction acts on the B5 coefficient orbits, test whether it fixes or
   constrains the four X-sector orbits or the signed phase sum. Do not infer a phase/domain packet from support
   multiplicities.

## Preregistered expected verdicts

- **`SA-Y8`:** expected `HOMONYM`, specifically that one use of “Majorana block” is an endomorphism or
  moment-map block preserving a doubled/source grading, while `SHIAB-05` concerns a same-Weyl-chirality
  invariant scalar bilinear. This expectation is killed if the SW source explicitly constructs the same
  `Spin(9,5)` map `S+ tensor S+ -> Lambda^0`.
- **`SA-Y1`:** expected `PAIRING-REMOVES-CHIRALITY-OBSTRUCTION-BUT-CHANNEL-REMAINS-SPURION-RELATIVE`. The
  expectation is killed positively if a basis-independent equivariant reduction identifies the term with
  the required invariant `Lambda^0` carrier without an undeclared vertical direction; it is killed negatively
  if the paired bilinear vanishes or fails four-dimensional scalar covariance.
- **`P2`:** expected `NOT-YET-TYPED`. A nontrivial result requires the same independently frozen construction
  to constrain X-sector phases or the B5 signed phase sum; merely producing a scalar mass bilinear is
  insufficient.

These are preregistered expectations, not conclusions.

## Kill and stop conditions

- If Layer 0 returns `SAME-OBJECT`, record a real repository contradiction and identify which claim lacks its
  construction; do not reconcile by terminology.
- If `K c(a_perp)` is not a nonzero four-dimensional scalar, stop the minimal-coupling-as-Yukawa route.
- If scalarity requires a supplied vertical direction, count that direction and its orbit as external
  parameters before computing any constraint surplus.
- If the B5 phase/domain packet is not independently produced, leave `P2` open and do not choose phases.
- No decomposition or multiplicity result may discharge an index/count row.

## Boundary expansion

After the construction produced a result, the write boundary was expanded only
to append provenance-preserving correction notices to the five same-day notes
whose live `SA-Y1`, `SA-Y8`, or `P2` language it supersedes. Their original run
text remains intact. No canon, claim ledger, or scientific-status surface was
added.

## Planned validation

- Re-run the SHIAB-05 and corrected Krein-pairing probes.
- Add a planted-control probe that distinguishes a scalar-valued bilinear from an invariant scalar carrier
  and refuses a B5 conclusion when the five-field packet is absent.
- Compile the new probe, run relevant regressions, and run `git diff --check`.
- Reconcile navigation/state only to the degree the scientific result actually warrants.

## Execution and result

### 1. `SA-Y8`: Layer-0 homonym

The two uses of “Majorana block” are not the same mathematical object:

```text
SHIAB-05:
  S+ tensor S+ -> Lambda^0_14
  same-Weyl scalar bilinear

SW construction:
  S+ tensor S- -> Lambda^2, then c(mu) in End(S)
  cross-chirality moment map producing an even endomorphism
```

They differ in domain, codomain, form degree, and predicate. Verdict:
`HOMONYM`. The SW `T3` term does not satisfy conditional `SA-Y8` merely
because its endomorphism was called “Majorana.” The exact SHIAB-05 absence and
cross-Weyl scalar control were rerun unchanged.

### 2. `SA-Y1`: physical scalar bridge

The ambient and physical scalar questions were kept separate:

```text
Spin(9,5):                  Lambda^1_14 is not Lambda^0_14
Spin(3,1) x Spin(6,4):     Lambda^1_14 -> (4,1) + (1,10)
```

All ten vertical `K c(e_i)` bilinears are exact 4D Lorentz scalars, nonzero,
Hermitian, and cross-chirality. An observer-compatible internal connection
factor preserves scalarity; a planted mixed base--vertical factor breaks it.
Thus existing `T1 + T2` can host `SA-Y1` at physical-channel grade. A separate
`T10` is not required merely to create the carrier. The vertical background,
stable vacuum, orbit, sign, magnitude, texture, hierarchy, and dynamical
subalgebra closure remain open.

### 3. `P2`: vertical projected RS symbol

The exact B5 support matrix separates into horizontal and vertical
contributions. All ten special mirror edges, including all four X edges, are
vertical-only. Signature-correct gamma-traceless projectors have ranks
`12` and `288`; the projected vertical symbol is nonzero and gamma-traceless
on both product-rule X families:

```text
RS4 tensor S10
S4 tensor RS10.
```

Therefore `P2` is typed as the phase/orientation of the canonical vertical
projected RS symbol on X.

### 4. Conditional `P1`--`P2` one-bit weld

The bare observer reality `J_obs` flips base and internal chirality together,
so it is not the B5 normal-only mirror. An internal-only conjugation has the
desired label action but fails Lorentz covariance, firing the planted control.

Composing the pairing again produces:

```text
C_perp = K J_obs.
```

Exact finite-matrix results:

- `C_perp` is an antilinear involution;
- it fixes 4D chirality, flips internal chirality, and flips total chirality;
- it obeys contragredient observer covariance exactly;
- it has the declared B5 dual-slot support action;
- its induced maps preserve both gamma-traceless RS projectors;
- horizontal Clifford symbols are coflip-even, while all ten vertical
  directions are coflip-odd; and
- both X product families inherit that same relative vertical parity.

Since all ten special B5 edges are vertical-only, this one whole-module
construction relates their relative algebraic parity. Conditional on
identifying `C_perp` with the metric-fibre loop coflip and with the actual
first-order differential, `P2` is not independent of `P1`: the ledger becomes
one global `P1/P2` orientation plus the still-separate `P3` chiral-index
datum.

### 5. Boundary that remains

The existing metric-fibre habitat probe was inspected and rerun. It transports
`K` and proves `K -> -K` around the generator loop, but it does not transport
`J_obs`, the factorized RS projectors, or the 20 B5 slot maps. Therefore it
does not yet prove the loop coflip equals `+/- C_perp`.

The fail-closed packet still lacks:

1. a transported loop-to-`C_perp` identification and normalized 20-slot
   pairing table;
2. the formal-adjoint sign of the written first-order differential;
3. a program-native Green boundary form; and
4. one common closed, symmetry-compatible domain.

No absolute `delta_e`, signed phase sum, B5 constraint surplus, count, vacuum,
mass prediction, or physical quotient is selected.

## Validation

All passed:

- `tests/channel-swings/vertical_krein_weld_probe.py`, repeatedly;
- `tests/chase/MOVE-4/move4_spinor_square_forms.py`;
- `tests/yukawa-scoping/yukawa_trilinear_channels.py`;
- `tests/channel-swings/krein_paired_bilinear_chirality_probe.py`;
- `tests/channel-swings/sig_b5_habitat_probe.py`;
- `tests/shiab_b5_observer_symbol_multiplicity_matrix.py`;
- `tests/shiab_b5_krein_mirror_orbit_reduction.py`;
- `tests/shiab_b5_native_packet_contract.py`;
- the B5 phase-sum and chirality-orientation audit probes;
- Python compilation; and
- `git diff --check`.

Controls that fired or discriminated as intended:

- same-object Layer-0 copy recognized;
- horizontal one-form fails scalarity;
- mixed base--vertical connection fails scalarity;
- identity pairing leaves the bare vertical action chirality-preserving;
- internal-only reality has the right chirality labels but fails Lorentz
  covariance;
- horizontal symbol has the opposite coflip parity from the vertical symbol;
- complete B5 support contains horizontal cells even though all special edges
  are vertical-only; and
- the incomplete native packet is rejected.

## RerankNextWork

Within Lane 1, `B5-INDEPENDENT-RECONSTRUCTION` remains the lead. The next
bounded construction is no longer another carrier or coflip search:

```text
transport J_obs around the verified metric-fibre generator loop
  -> compare the returned K J_obs with +/- C_perp
  -> write the first-order B5 differential
  -> derive its 20-slot pairing phases and one formal-adjoint sign
  -> compute the ten absolute delta_e values and signed sum
  -> build Green form/common domain only if the algebraic signs cohere.
```

`ANOMALY-DESCENT-HARDENING` remains the parallel Lane-1 alternative. No result
here supplies a cross-lane priority change, Joe priority signal, or paper-seed
proposal, so the machine-owned portfolio and lane state are left for Lane-A
stewardship rather than rewritten in this Progress run.

## Receipt

- Result vocabulary:
  `L0-HOMONYM + 4D-SCALAR-BRIDGE + P2-VERTICAL-SYMBOL-TYPED + CONDITIONAL-P1-P2-ONE-BIT-WELD`.
- Service outcome: completed.
- First residual: loop transport of `J_obs` and identification with
  `+/- C_perp`, followed by the written differential's slot pairings and
  formal-adjoint sign.
- Scientific grade: exact finite algebra and support; reconstruction for the
  loop/differential identification.
- Claim, canon, verdict, count, paper, portfolio, and public-posture changes:
  none.
- Unrelated dirty artifact
  `GUH-20260729T131135Z-b5-native-packet-source-audit` preserved untouched.
