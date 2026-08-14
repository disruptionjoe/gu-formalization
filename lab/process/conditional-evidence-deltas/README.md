# Conditional Evidence Deltas

This directory is the native GU handoff from a focused, durable exploration to
the sequential conditional-physics ledger. It prevents two writers from
guessing the same next ledger number and prevents requester provenance from
silently becoming scientific authority or scheduled priority.

## Contract

Each delta is a JSON file conforming to `delta.schema.json` and indexed in
`index.json`. It records:

- a globally unique semantic `delta_id` and `pending` status;
- the exact base ledger reference and SHA-256;
- the affected ledger row IDs;
- native scientific result references;
- the source disposition and claim ceiling;
- a compact proposed scientific effect;
- conflict keys identifying other deltas or rows that cannot be integrated
  blindly; and
- a null integration record while pending.

A pending delta changes no ledger verdict, canon, current state, or public
posture. It has no future ledger version. Canonical Progress examines pending
deltas beyond its private cursor and records one disposition:
`incorporated`, `duplicate`, `deferred`, or `conflicting`. Only an incorporated
delta receives a canonical ledger reference.

## Boundary

These are scientific evidence artifacts, not execution receipts. Do not store
Run IDs, service Lane IDs, schedules, model/effort, execution claims, or private
receipts here. Same-repository evidence links directly to native artifacts; it
does not use the mailbox to notify GU about itself.

Validate with:

```bash
python process_gates/conditional_evidence_delta_gate.py
```
