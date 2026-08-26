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
| `cb_c_anomaly_rank.py` | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md` | Reproduces the exact local anomaly-rank checks for the frozen CB-C construction packet; it does not select the physical fermion content or move an anomaly verdict. |
| `sp1_2primary_gate_validator.py` | `lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md` | Checks the untwisted `BSp(1)` Dai-Freed degree-15 AHSS front page and 2-primary controls. |

Run directly:

```text
python tests/anomaly/cb_c_anomaly_rank.py
python tests/anomaly/sp1_2primary_gate_validator.py
```
