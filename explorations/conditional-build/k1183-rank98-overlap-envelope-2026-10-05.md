---
title: "K1183 rank-98 overlap envelope"
status: active_research
doc_type: exact_sequential_complement_overlap_boundary
created: "2026-10-05"
claim_ceiling: sharp dimension-only overlap interval; the rank-98 K132 transport remains unowned
manifest: lab/process/k1183-rank98-overlap-envelope.json
probe: tests/channel-swings/k1183_rank98_overlap_envelope_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1183 rank-98 overlap envelope

K1173 favorably grants the finite epsilon moment map plus seven-invariant lock
a joint rank `98` on the K132 kernel. That transport is not source-owned or
measured, so its overlap with K1182's native `J` cannot be guessed.

For subspaces of ranks `a` and `b`, the second sequential complement lies in
`[max(0,b-a),b]`, and both endpoints are sharp. Therefore `J` contributes:

| stratum | `rank(J|ker H)` | new rank after prior 98 | residual repair floor |
| --- | ---: | ---: | ---: |
| timelike / spacelike | 162 | `[64,162]` | `[98210,98308]` |
| null | 8323 | `[8225,8323]` | `[98213,98311]` |

The lower residual is the most favorable disjoint placement; the upper
residual is the strongest possible overlap. Without the unowned rank-98 grant,
the measured native residual is exactly `98308/98308/98311`.

This is an overlap firewall, not a common-coupling measurement. The hostile
probe rejects `11/11` mutations, and no protected status moves.
