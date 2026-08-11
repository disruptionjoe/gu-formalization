#!/usr/bin/env python3
"""Fail-closed audit for ledger v0.174."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ledger=json.loads((ROOT/"lab/process/conditional-physics-ledger-v0.174.json").read_text())
packet=json.loads((ROOT/"lab/process/selected-k77-action-adjoint-weight-classification.json").read_text())
report=(ROOT/"explorations/conditional-build/selected-k77-action-adjoint-weight-classification-2026-08-11.md").read_text()
review=(ROOT/"lab/process/hostile-reviews/2026-08-11-selected-k77-action-adjoint-weight-classification-review.md").read_text()
assert ledger["schema_version"]=="0.174" and ledger["predecessor"].endswith("v0.173.json")
assert ledger["progress"]["verdict_counts"]=={"SAME":32,"DIFFERS":19,"NEEDS":26,"OVER_DETERMINED":5}
assert ledger["frontier_delta"]=={"headline_delta":"NONE","conditions_closed":3,"conditions_opened":1,"remaining_named_conditions":4}
assert len(ledger["migration_history"])==6 and {x["from_version"] for x in ledger["migration_history"]}=={"0.173"} and {x["to_version"] for x in ledger["migration_history"]}=={"0.174"}
assert packet["self_adjoint_pairing_line"]==[1,-1,-1,1]
assert packet["anti_adjoint_pairing_line"]==[1,1,1,1]
assert packet["both_grassmann_coefficients_alternating"] and packet["pairing_ranks"]==[1920,1920]
assert packet["weight_equation_rank"]==0 and packet["invariant_parameter_dimension"]==1
assert packet["checks"]=={"total":36,"failures":0}
assert "two `U(32,32)` halves" in report and "full `U(64,64)`" in report
assert "SURVIVES_WITH_SCOPE_REPAIR" in review
assert not packet["verdict_change"] and not packet["booked_residue_change"] and not packet["quotient_change"]
assert not packet["canon_verdict_change"] and not packet["public_posture_change"] and not packet["p1_p2_p3_used"]
print("PASS: v0.174 action-adjoint and weight classification is internally consistent and fail-closed")
