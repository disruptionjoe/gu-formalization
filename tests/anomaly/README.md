---
title: "Anomaly Tests"
status: active_research
doc_type: test_manifest
created: 2026-07-06
---

# Anomaly Tests

Standalone anomaly gate scripts.

Boundary: this surface is a frontstage anomaly gate only. It is not an anomaly-cancellation verdict,
does not decide physical fermion content, does not move claim status, does not change verdicts,
and does not update public posture.

| script | supports | note |
|---|---|---|
| `sp1_2primary_gate_validator.py` | `lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md` | Checks the untwisted `BSp(1)` Dai-Freed degree-15 AHSS front page and 2-primary controls. |

Run directly:

```text
python tests/anomaly/sp1_2primary_gate_validator.py
```
