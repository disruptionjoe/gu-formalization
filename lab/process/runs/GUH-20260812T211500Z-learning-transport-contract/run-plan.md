---
run_id: GUH-20260812T211500Z-learning-transport-contract
status: complete
repository: gu-formalization
workflow: direct-chat-process-hardening
mode: execute
lane_id: "A"
work_item: LEARNING-TRANSPORT-CONTRACT
starting_revision: e7409a860bf4f83f064633874584fdfef7f1ee5f
opened_at: 2026-08-12T21:15:00Z
completed_at: 2026-08-12T21:28:40Z
claim_status_change: none
canon_change: none
public_posture_change: none
ledger_change: none
---

# Learning-transport contract

## Objective

Make the v0.221 correction durable at the process layer without changing any
scientific verdict: register the `H` homonym, propagate the concrete real-form
correction, remove the stale current-ledger pointer, and require future wave
handoffs to state the structure they inherited and the variational altitude
they reached.

## Layer 0

This run changes process metadata, not the GU construction.  The objects that
must remain distinct are:

- the trace-owned Hermitian form `H_q = i B gamma(q/2)` on the full carrier;
- observer-time `H_u`;
- the generation-hinge carriers `H^- = X(S^+)` and `H^+ = X(S^-)`;
- an abstract Lie algebra label such as `u(p,q)`; and
- a concrete embedded real form, which also depends on carrier, form, real
  involution, grading, signature horn and ambient embedding.

## Planned changes

1. Add the `H_q` / `H_u` / `H^+` / `H^-` collision to `NAMES.md`.
2. Add the v0.221 correction to `correction-registry.yaml`.
3. Add the repeated real-form embedding mistake as a dated path-dependency
   trap and regenerate the rendered view.
4. Advance the operating-contract and Lane work-state pointers from v0.196 to
   v0.221.
5. Add a compact typed-handoff contract: structure fingerprint, variational
   altitude, globalization grade, commutation status, forbidden transfers and
   an adapter-or-Layer-0-reset rule when the fingerprint changes.
6. Add a deterministic process audit with a planted v0.220-style mismatch.

## Acceptance

- the planted trace-`H_q` to B-skew transfer fails without an adapter;
- the same transfer passes only with an explicit adapter receipt or Layer-0
  reset;
- all new paths are documented and parse;
- existing v0.221 science gates remain green;
- no ledger row, canon verdict, residue, quotient, datum or public posture
  changes.

## Write boundary

- `lab/process/NAMES.md`
- `lab/process/correction-registry.yaml`
- `lab/process/path-dependencies.yaml`
- `lab/process/path-dependencies.md` (generated)
- `lab/process/functional-channel-operating-contract-v1.0.{md,json}`
- `lab/process/session-agent-card.md`
- `LANES.yaml`
- `process_gates/learning_transport_contract_audit.py`
- `process_gates/README.md`
- `lab/process/README.md`
- this run record

## Five specialist lenses and System Council disposition

- **Category theory:** a structure fingerprint is an object declaration, not an
  isomorphism.  Transfer still requires an explicit intertwiner/adapter.  This
  is why the contract rejects a changed fingerprint by default.
- **Representation/real-form theory:** `u(p,q)` and dimension do not determine
  the concrete real embedding.  The form, involution, grading and carrier are
  load-bearing fingerprint fields.
- **Variational and symplectic geometry:** pointwise source-realizability is
  below action-owned tangency, Euler admissibility, stationarity and reduced
  phase space.  These are recorded as separate altitudes.
- **Operator/PDE theory:** local equivariance and associated-bundle descent do
  not imply connection-preserved or global analytic descent.  The handoff
  therefore also records globalization grade.
- **Proof/certificate engineering:** the rule needs a firing control.  The new
  audit plants the exact trace-`H_q` to B-skew fingerprint change and rejects it
  without an adapter or Layer-0 reset.

The System Council approved the compact contract with one dissent preserved:
the fingerprint cannot prove mathematical equivalence and must never become a
new proxy for it.  It is a fail-closed routing check, not a theorem prover.  No
dashboard, DSL, new science lane or new approval step was added.

## Hostile review

1. **Summary outruns artifact:** prevented.  The contract says only that a
   transfer is inadmissible without a typed transition; it does not assert the
   two structures are inequivalent in every context.
2. **Rigor defending a superseded object:** prevented.  The v0.220 operator is
   preserved while its B-skew embedding is explicitly superseded for the live
   trace-`H_q` problem.
3. **If this stands, what changes:** future handoffs and current-ledger pointers
   change; ledger rows, canon, scientific verdicts, residue, quotients, datum
   and public posture all survive unchanged.

## Validation and result

- `learning_transport_contract_audit.py`: 4/4 PASS, including the planted
  v0.220-style failure and adapter/reset controls.
- `path_dependency_audit.py`: 7/7 PASS; 6/8 chains; 44 receipts resolve.
- `correction_propagation_audit.py`: 2/2 PASS; only the pre-existing seeded
  `NEEDS_RECHECK` inventory remains.
- `k77_i2b_trace_hq_normal_contact_correction_audit.py`: 23 exact + 4 planted,
  PASS.
- `process_gate_readme_inventory_audit.py`: 407/407 documented, PASS.
- JSON/YAML parse and `git diff --check`: PASS.

The process would now have caught the v0.220 mistake before disposition: its
predecessor and successor fingerprints differ in `pairing_or_form` and
`real_structure`, and no adapter receipt was present.
