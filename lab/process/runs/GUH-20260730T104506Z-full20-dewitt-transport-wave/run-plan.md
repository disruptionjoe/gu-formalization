---
run_id: GUH-20260730T104506Z-full20-dewitt-transport-wave
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S4-DEWITT-TRANSPORT
starting_revision: 6e9930ac3ed6
opened_at: 2026-07-30T10:45:06Z
closed_at: 2026-07-30T11:01:00Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260730T104506Z-full20-dewitt-transport-wave/run-plan.md
  - explorations/full20-dewitt-loop-transport-wave-2026-07-30.md
  - tests/channel-swings/full20_dewitt_loop_transport_probe.py
  - explorations/README.md
  - tests/README.md
---

# Full-20 DeWitt-loop associated transport wave

## Authorization and exact delta

Joe asked to run the next highest-information swing after the full-20
native-polarization wave.  The exact delta is the first item of that wave's
ordered handoff:

1. carry the twenty constructed thin observer summands around the actual
   \(TX\oplus\operatorname{Sym}^2T^*X\) DeWitt loop;
2. factor raw representation motion from multiplicity-space return;
3. transport the antilinear \(C_\perp=KJ_{\rm obs}\) candidate;
4. demand compatibility with the written
   \(\Gamma,j,P_I,P_R,D_{\mathbf c}\) maps; and
5. compute the returned linear mismatches before reading any slotwise scalar.

This Run extends, rather than duplicates:

- `tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py`, which
  stopped before the associated map on the twenty provenance slots;
- `tests/channel-swings/full20_observer_projector_support_probe.py`, which
  built the twenty complexified thin embeddings but explicitly stopped
  before transport;
- `tests/channel-swings/full20_native_polarization_probe.py`, which built the
  native coarse pairing/formal-action packet but left fine coflip phases open;
  and
- `explorations/sa-y8-majorana-layer0-and-vertical-krein-weld-2026-07-29.md`,
  which built the spinor \(C_\perp\) candidate but left its loop and
  normalized-provenance identifications conditional.

The pre-existing untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` is outside this Run's
write boundary and remains untouched.

## Layer 0

| shared phrase | object tested here | object not identified with it |
| --- | --- | --- |
| loop return | the actual endpoint frame return induced by \(B_t^{-1}\) on \(TX\) and \(E\mapsto B_t^TEB_t\) on \(\operatorname{Sym}^2T^*X\) | an arbitrary sign on twenty labels |
| raw slot return | the non-scalar matrix of an observer-group element inside an irreducible representation | a Schur scalar or an external datum |
| normalized mismatch | \(C_{0,s}^{-1}C_{1,s}\), after both endpoint maps land in the declared mirror bundle | the raw spin/vector holonomy |
| multiplicity return | the matrix on the three isomorphic `S`/`imGamma`/low-`kerGamma` copies after factoring their common observer irrep | three independent scalars assumed in advance |
| coflip extension | an antilinear map on \(S\oplus(V\otimes S)\) that actually intertwines \(\Gamma,j,P_I,P_R\) | the pairing-induced vector duality merely because both use \(KJ_{\rm obs}\) |
| differential compatibility | covariance of the nine written first-order primitives and their actual nonzero observer projections | graph connectivity or support preservation alone |

Layer 0 runs before a twenty-scalar verdict.  If a proposed coflip does not
preserve the `imGamma`/`kerGamma` provenance split, then its endpoint scalar
on those slots is undefined even if its full-carrier mismatch is central.

The construction remains on the program-native
\(TX\oplus\operatorname{Sym}^2T^*X\), `Cl(9,5)`, Krein,
gamma-traceless-RS fork.  The equal-dimensional exterior-ten and
positive-Hilbert comparators are not used.

## Pre-registration status, expectation, kills, and go

Before the formal probe was written, a bounded scratch diagnostic was run
while resolving the Layer-0 object.  It showed that the naive
\(\eta_{9,5}\otimes C_\perp\) vector-spinor extension does not preserve the
full fourteen-dimensional \(P_R\).  This Run therefore does **not** claim a
fully blind preregistration.  The diagnostic, including that it occurred
before this record, is preserved here rather than silently fitted away.
The exact multiplicity matrix, existence/uniqueness of a corrected extension,
all twenty endpoint mismatches, and hostile-control outcomes remain held out.

Preregistered expected verdict after that diagnostic:

```text
PAIRING-ONLY-VECTOR-EXTENSION-FAILS-GAMMA-SPLIT
GAMMA-NATURAL-EXTENSION-UNIQUE-UP-TO-ONE-GLOBAL-PHASE
FULL20-RETURNED-MISMATCH-CENTRAL-MINUS-ONE-LIKELY
INDEPENDENT-SLOT-TWIST-REJECTED-BY-WRITTEN-DIFFERENTIAL-LIKELY
GLOBAL-DOMAIN/PHYSICAL-INDEX/COUNT-UNCHANGED
```

**Semantic kill.**  If neither the pairing-induced extension nor an extension
derived from \(\Gamma\)-naturality maps every constructed slot to its declared
mirror without leakage, stop.  A full-carrier `-I` cannot be reported as a
twenty-slot result.

**Transport kill.**  Kill the present P1/P2 identification if the actual
linear loop transport fails to preserve any thin summand, if
\(\Gamma,j,P_I,P_R\) fail covariance, or if the returned mismatch has a
noncentral isotypic or relative-slot component.

**Differential kill.**  Kill the one-global-phase conclusion if an
independent mirror-pair phase twist both preserves the static ledger and
intertwines every nonzero projection of the written nine-block differential.

**Go condition.**  Advance the finite associated-bundle weld only if:

1. the corrected extension is derived from, not chosen after, the endpoint;
2. it maps all twenty slots to their declared mirrors;
3. the raw non-scalar representation matrices are explicitly separated from
   multiplicity matrices;
4. all returned mismatches are the same central scalar;
5. the written \(\Gamma,j,P_R,D_{\mathbf c}\) maps pass covariance; and
6. a planted relative phase passes static support but fails the actual
   coefficient-level intertwiner test.

## Controls and constraint surplus

- Recompute the actual symmetric-fibre return; do not hard-code the exterior
  ten or the endpoint signs.
- Require the raw slot matrices to be non-scalar on at least one
  positive-dimensional observer irrep.  A test that calls them Schur scalars
  is void.
- Compute the three-copy multiplicity matrices before per-slot mismatch
  scalars.
- Compare the naive pairing extension with the independently
  \(\Gamma\)-natural extension.
- Delete the normal/base-fibre grading from the latter and require
  `imGamma`/`kerGamma` leakage.
- Apply all nine actual formulas to deterministic witnesses over all 136
  independently certified nonzero cells.
- Plant one mirror-pair phase twist.  It must preserve mirror involution and
  static support but fail differential covariance.
- Double the metric loop; its returned mismatch must square to `+1`.

The diagonal vector extension starts with fourteen unit phases.  The fourteen
\(\Gamma\)-intertwining equations must determine all relative phases, leaving
only one global normalization.  The complete nonzero differential graph then
tests the ten mirror-pair phases and may leave at most one common phase.
The endpoint loop sign is held out from both fits.

## Nonclaims

This wave does not construct a common closed domain, nonlinear BV solution,
stationary vacuum, four-dimensional retained spectrum, physical index,
generation count, or P3 map.  It does not promote the compact/finite
associated-bundle calculation to the complete five-field native packet.

## Planned validation

1. Run the new probe and its planted controls.
2. Re-run the actual-fibre, vertical--Krein, full-20 support,
   native-polarization, exact observer-ledger, mirror-orbit, and fail-closed
   native-packet controls.
3. Compile the new Python file.
4. Run repository index gates relevant to changed navigation.
5. Run `git diff --check`.
6. Append the observed result here, write one integrated exploration,
   commit, push, and close with the same scoped session guard.

## Execution and observed result

The formal probe was written and run after the partial-preregistration
disclosure above.  The observed verdict is:

```text
ACTUAL-SYM2-DEWITT-LOOP-RECOMPUTED
PAIRING-ONLY-VECTOR-EXTENSION-FAILS-GAMMA-PROVENANCE
GAMMA-NATURAL-NORMAL-GRADING-FORCED-UP-TO-GLOBAL-PHASE
RAW-20-SLOT-RETURN-NONSCALAR
THREE-COPY-MULTIPLICITY-RETURN-IDENTITY
ALL-20-RETURNED-MISMATCHES-CENTRAL-MINUS-ONE
ALL-136-WRITTEN-COEFFICIENT-INTERTWINERS-EXACT
INDEPENDENT-SLOT-TWIST-REJECTED
P1/P2-ONE-BIT-WELD-CLOSED-AT-FINITE-ASSOCIATED-BUNDLE-GRADE
GLOBAL-NATIVE-DOMAIN/NONLINEAR-BV/P3-OPEN
```

### Layer-0 correction

The preliminary diagnostic was real and load-bearing.  Extending
\(C_\perp\) by the vector-spinor pairing alone gives the exact
`imGamma`/low-`kerGamma` multiplicity involution

```text
[[-3/7, 2*sqrt(10)/7],
 [2*sqrt(10)/7, 3/7]].
```

It therefore has no declared twenty-slot scalar table.  Solving

```text
Gamma C_VS = C_perp Gamma
```

direction by direction forces

```text
C_VS = (N eta_9,5) tensor C_perp
N = diag(+1 on TX, -1 on Sym^2 T*X),
```

up to one common phase.  This corrected extension also intertwines `j`,
`P_I`, and `P_R`, and maps all twenty summands to their declared mirrors.

### Transport and multiplicity

The actual endpoint representation matrices are non-scalar, with maximum
centrality defect `1`, so they are not misreported as Schur phases.  For each
of the four repeated E-types, factoring the common irrep motion gives the
raw multiplicity matrix `I_3`.

Only then are the returned antilinear mismatches formed.  All twenty equal
central `-I`, with maximum centrality defect `3.44e-15` and scalar error
`4.44e-16`.  The four repeated multiplicity matrices are `-I_3`.  The
doubled actual frame/spin loop gives `+I`.

### Differential and hostile control

The actual loop intertwines `Gamma`, `j`, `P_R`, and all nine written
first-order primitives.  Deterministic generic witnesses make every one of
the 136 independently allowed coefficient projections nonzero; the corrected
coflip covariance residual is at most `1.34e-15`.

A planted sign on one mirror pair remains an involution and passes the static
support matcher.  It fails 28 actual coefficient intertwiners with maximum
normalized residual `2`.  Thus the written differential, not support alone,
removes the relative phase.

### Disposition

The P1/P2 weld advances from conditional support/spinor grade to exact finite
associated-bundle and formal first-order-expression grade.  The datum ledger
at this grade is one joint P1/P2 orientation plus the still-separate P3
count/index datum.

The fail-closed native packet is not promoted.  A common global closed
domain, nonlinear BV closure, physical vertical-mass retention, stationary
background, P3 map, physical index, and generation count remain open.  No
claim, canon verdict, or public posture changes.

## Validation

All passed:

- `tests/channel-swings/full20_dewitt_loop_transport_probe.py`;
- `tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py`;
- `tests/channel-swings/vertical_krein_weld_probe.py`;
- `tests/channel-swings/full20_observer_projector_support_probe.py`;
- `tests/channel-swings/full20_native_polarization_probe.py`;
- `tests/shiab_b5_observer_symbol_multiplicity_matrix.py`;
- `tests/shiab_b5_krein_mirror_orbit_reduction.py`;
- `tests/shiab_b5_native_packet_contract.py`;
- `process_gates/explorations_readme_surface_map_audit.py`;
- `process_gates/explorations_top_level_file_boundary_audit.py`;
- `process_gates/tests_manifest_count_audit.py`;
- `process_gates/tests_root_readme_inventory_audit.py`;
- `process_gates/research_posture_audit.py`;
- `process_gates/public_path_hygiene_audit.py`;
- `process_gates/changed_public_path_hygiene_audit.py`;
- Python compilation of the new probe; and
- `git diff --check`.
