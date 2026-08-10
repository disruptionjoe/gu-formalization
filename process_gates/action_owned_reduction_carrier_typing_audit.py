#!/usr/bin/env python3
"""Governance audit for ledger v0.132 action/carrier typing correction."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


ledger = strict("lab/process/conditional-physics-ledger-v0.132.json")
result = strict("lab/process/selected-k77-action-owned-reduction-carrier-typing.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-action-owned-reduction-carrier-typing-review.md").read_text()
canon = (ROOT / "canon/generation-carrier-identification-scope-correction-2026-08-10.md").read_text()
priority = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()

check("ledger", "v0.132 appends to v0.131", ledger["schema_version"] == "0.132"
      and ledger["predecessor"].endswith("v0.131.json"))
check("ledger", "coverage and verdict counts remain unchanged",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue forks and quotients remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["function_valued_at_least"] == 19
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("result", "bosonic and fermion projectors are typed separately",
      result["layer0"]["P_epsilon"] == "BOSONIC_CONNECTION_COEFFICIENT_PROJECTOR"
      and result["layer0"]["P_W"] == "FERMION_RS_J1_TRIPLET_PROJECTOR"
      and result["layer0"]["bridge"] == "NOT_CONSTRUCTED")
check("result", "local consistency is not promoted to action selection",
      result["disposition"]["bosonic_reduction"]
      == "LOCAL_LINEARIZED_CONSISTENT_TRUNCATION_CANDIDATE__DYNAMIC_SELECTION_OPEN")
check("result", "direct five-way test fails closed until induced odd operator exists",
      result["layer0"]["direct_five_way_discrimination"]
      == "MISTYPED_UNTIL_INDUCED_FERMION_OPERATOR_EXISTS")
check("rows", "all nine rows carry v0.132 evidence",
      all("selected-k77-action-owned-reduction-carrier-typing" in rows[row_id]["evidence"]
          for row_id in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1", "LT-GR1", "LT-GR2b", "LT-GR3")))
check("rows", "fermion rows name an induced operator rather than direct bosonic projection",
      all("induced" in rows[row_id]["distance"].lower()
          for row_id in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")))
check("rows", "gravity rows retain local consistency and open ownership",
      "locally first-order consistent but not selected" in rows["LT-GR1"]["distance"]
      and "compatible but not selected" in rows["LT-GR2b"]["distance"]
      and "non-selecting" in rows["LT-GR3"]["distance"])
check("review", "hostile review narrows the theorem and rejects direct discrimination",
      "LOCAL_LINEARIZED_CONSISTENT_TRUNCATION_CANDIDATE" in review
      and "DIRECT_FERMION_DISCRIMINATION_REJECTED" in review)
check("review", "symplectic and analytic fences are explicit",
      "Symplectic geometry" in review and "Operator/PDE/Krein/analytic" in review)
check("canon", "canon now requires the induced K77 fermion operator",
      "two serial parts" in canon and "Dirac/Rarita--Schwinger operator" in canon)
check("priority", "priority is split into bosonic parent then induced fermion selector",
      "Build A — bosonic action-parent ownership" in priority
      and "Build B — induced fermion selector" in priority)
check("contract", "functional contract points to v0.132 and carries the type fence",
      contract["standing_ledger"]["ref"].endswith("v0.132.json")
      and "BOSONIC_CONNECTION_TYPED" in contract["standing_ledger"]["carrier_selection_directive"])
check("accounting", "P1 P2 P3 and all status postures are unchanged",
      result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
      and all(result[key] == "none" for key in
              ("claim_status_change", "canon_verdict_change", "public_posture_change")))

total = sum(COUNTS.values())
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {total-len(FAILURES)}/{total}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
