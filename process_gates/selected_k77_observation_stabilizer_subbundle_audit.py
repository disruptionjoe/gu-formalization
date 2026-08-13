#!/usr/bin/env python3
"""Static scope/provenance audit for ledger v0.127."""

from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
checks = []


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


def canonical(payload):
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def check(label, condition):
    ok = bool(condition)
    checks.append((label, ok))
    print(f"{'PASS' if ok else 'FAIL'} {label}")


result = strict("lab/process/selected-k77-observation-stabilizer-subbundle.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.127.json")
bank = strict("tests/fixtures/k77_minimal_tangent_bank_v1.json")
report = (ROOT / "explorations/conditional-build/selected-k77-observation-stabilizer-subbundle-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-observation-stabilizer-subbundle-review.md").read_text()

unsigned = dict(bank)
unsigned.pop("construction_hash", None)
check("tangent bank has canonical current hash",
      sha256(canonical(unsigned)).hexdigest() == bank["construction_hash"])
check("tangent bank dependencies are current",
      all((ROOT / relative).is_file()
          and sha256((ROOT / relative).read_bytes()).hexdigest() == expected
          for relative, expected in bank["dependency_hashes"].items()))
check("bank is the exact sparse rank-594 fiber",
      bank["tangent"]["rank"] == 594 and bank["tangent"]["nnz"] == 1850
      and bank["tangent"]["total_selected_dimension"] == 915)
exact = result["exact_result"]
check("complete observation stabilizer has zero defect",
      exact["stabilizer_generator_count"] == 51
      and exact["so13_generator_count"] == 6
      and exact["so64_generator_count"] == 45
      and exact["stabilizer_quotient_defects"] == 0)
check("full ambient invariance is explicitly rejected",
      exact["mixed_ambient_generator_rank"] == [594, 727]
      and result["layer0"]["full_ambient_spin77_invariance"].startswith("REFUTED"))
check("five natural blocks sum to 594",
      sum(value["intersection"] for value in exact["block_profile"].values()) == 594
      and [value["intersection"] for value in exact["block_profile"].values()]
      == [160, 180, 60, 184, 10])
check("associated subbundle remains conditional on observation reduction",
      result["layer0"]["associated_subbundle"].endswith("OBSERVATION_REDUCTION")
      and result["layer0"]["global_observation_reduction"] == "NOT_CONSTRUCTED"
      and result["layer0"]["global_trivialization"] == "NOT_CLAIMED")
check("unitary parents remain unported",
      result["action_parent_fence"]["two_U32_32_halves"] == "NOT_PORTED"
      and result["action_parent_fence"]["full_U64_64"] == "NOT_PORTED")
check("accounting remains unchanged",
      result["accounting"]["new_coefficients"] == 0
      and result["accounting"]["new_quotients"] == 0
      and result["accounting"]["new_external_datum"] == 0
      and result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("ledger is append-only v0.127 from v0.126",
      ledger["schema_version"] == "0.127"
      and ledger["predecessor"].endswith("conditional-physics-ledger-v0.126.json")
      and len(ledger["migrations"]) == 621
      and [item["row_id"] for item in ledger["migrations"][-6:]]
      == ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"])
check("headline residue and quotient count do not move",
      ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
      and ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return and lower-order fence are visible",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
      and "lower-order and derivative-jet" in report)
check("hostile review preserves all three charges",
      "Charge 1" in review and "Charge 2" in review and "Charge 3" in review
      and "mixed horizontal/normal generator" in review)
check("validation receipts agree",
      result["validation"]["primary"] == "78/78_PASS"
      and result["validation"]["independent_sage_flint"] == "12/12_PASS")
check("no canon or posture movement",
      result["claim_status_change"] == "none"
      and result["canon_verdict_change"] == "none"
      and result["public_posture_change"] == "none")

failures = [label for label, ok in checks if not ok]
print(f"PASS {len(checks)-len(failures)}/{len(checks)}")
if failures:
    raise SystemExit("; ".join(failures))
