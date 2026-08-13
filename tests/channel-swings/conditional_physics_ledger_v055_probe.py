#!/usr/bin/env python3
from pathlib import Path
import json

R = Path(__file__).resolve().parents[2]
load = lambda p: json.loads((R / p).read_text())
o = load("lab/process/conditional-physics-ledger-v0.54.json")
n = load("lab/process/conditional-physics-ledger-v0.55.json")
r = load("lab/process/selected-nonzero-background-cartan-spencer-owner.json")
O = {x["id"]: x for x in o["rows"]}
N = {x["id"]: x for x in n["rows"]}
M = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert o["schema_version"] == "0.54" and n["schema_version"] == "0.55"
assert set(O) == set(N) and o["denominator"] == n["denominator"]
assert {x for x in O if O[x] != N[x]} == M
assert all((O[x]["verdict"], O[x]["reason_kind"]) ==
           (N[x]["verdict"], N[x]["reason_kind"]) for x in O)
assert o["progress"]["verdict_counts"] == n["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert o["residue"] == n["residue"]
assert {m["row_id"] for m in n["migrations"] if m.get("from_version") == "0.54"} == M
assert r["exact_result"]["cartan_spencer_rank"] == 1274
assert r["exact_result"]["transverse_support"] == 117
assert r["exact_result"]["levi_civita_transverse_intersection"] == 0
assert r["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
print("PASS 12/12: v0.55 owns transverse 117 on the unrestricted Cartan/Spencer carrier, excludes Levi-Civita alone, and freezes verdicts, residue, quotients and datum")
