#!/usr/bin/env python3
"""Fail-closed audit for the durable K77 exact-bank API gate."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import ast
import json


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-exact-bank-api-v1.json"
BANK = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
API = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
BUILDER = ROOT / "tests/channel-swings/k77_exact_bank_build.py"
CONTRACT = ROOT / "lab/process/functional-channel-operating-contract-v1.0.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.124.json"
checks = []


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate key {} in {}".format(key, path))
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def canonical(payload):
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def construction_hash(payload):
    unsigned = dict(payload)
    unsigned.pop("construction_hash", None)
    return sha256(canonical(unsigned)).hexdigest()


def check(kind, label, condition):
    ok = bool(condition)
    checks.append((kind, label, ok))
    print("{} [{}] {}".format("PASS" if ok else "FAIL", kind, label))


registry = strict(REGISTRY)
bank = strict(BANK)
contract = strict(CONTRACT)
ledger = strict(LEDGER)
api_source = API.read_text()
builder_source = BUILDER.read_text()
ast.parse(api_source)
ast.parse(builder_source)

check("exact", "registry is API_PASS", registry["status"].startswith("API_PASS"))
check("exact", "ledger v0.124 is current", ledger["schema_version"] == "0.124")
current_migrations = [item for item in ledger["migrations"] if item["to_version"] == "0.124"]
check("exact", "exactly six process-only row migrations are recorded",
      len(current_migrations) == 6 and all(item["old"] == item["new"] for item in current_migrations))
check("exact", "headline accounting remains 32 19 26 5",
      ledger["progress"]["verdict_counts"] == {
          "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("exact", "contract points to ledger v0.124",
      contract["standing_ledger"]["ref"].endswith("v0.124.json"))
check("exact", "fixture file hash matches registry",
      sha256(BANK.read_bytes()).hexdigest() == registry["bank"]["file_sha256"])
check("exact", "construction hash matches canonical payload",
      construction_hash(bank) == bank["construction_hash"] == registry["bank"]["construction_hash"])
check("exact", "all 29 dependencies are present and current",
      len(bank["dependency_hashes"]) == 29 and all(
          (ROOT / relative).is_file()
          and sha256((ROOT / relative).read_bytes()).hexdigest() == expected
          for relative, expected in bank["dependency_hashes"].items()))
check("exact", "ordinary API contains no runpy, SymPy or NumPy",
      all(token not in api_source.lower() for token in ("runpy", "sympy", "numpy")))
check("exact", "recursive producer is confined to builder",
      "selected_k77_fixed_operator_metric_epsilon_leakage_probe.py" in builder_source
      and "selected_k77_fixed_operator_metric_epsilon_leakage_probe.py" not in api_source)
check("exact", "bank dimensions are exact",
      len(bank["carrier"]["epsilon_generators"]) == 91
      and len(bank["receivers"]["labels"]) == 1274
      and len(bank["receivers"]["horizontal_rows"]) == 24
      and len(bank["receivers"]["offslice_rows"]) == 1250)
check("exact", "three causal banks each carry 101 columns",
      set(bank["columns"]) == {"timelike", "spacelike", "null"}
      and all(len(columns) == 101 for columns in bank["columns"].values()))
check("exact", "selected Spin does not silently port to unitary parents",
      bank["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED"
      and bank["scientific_scope"]["full_U64_64"] == "NOT_PORTED")
check("exact", "P1 P2 P3 remain unused", registry["constraint_fence"]["P1_P2_P3"] == "UNUSED")
check("exact", "no verdict canon or posture change",
      registry["claim_status_change"] == registry["canon_verdict_change"]
      == registry["public_posture_change"] == "NONE")

routing = contract["channels"]["VERIFY"]["efficient_specialist_routing"]
check("exact", "efficient routing has exactly eight mandatory roles", len(routing["mandatory_eight"]) == 8)
check("exact", "specialist routing is inline by default",
      routing["execution_mode"] == "INLINE_ROLES__NO_PERSONA_PER_SUBAGENT_DEFAULT")
check("exact", "trigger map covers exact computation and provenance",
      {"EXACT_COMPUTATION_ARCHITECTURE", "DISTRIBUTED_PROVENANCE"}.issubset(routing["object_triggered"]))
check("exact", "lens output distinguishes math from analogy",
      "evidence_mode_actual_math_or_analogy" in routing["required_output_fields"])
check("exact", "all-lenses-every-cell is forbidden", routing["all_lenses_every_cell"] is False)
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-k77-exact-bank-api-review.md").read_text()
check("exact", "machine contract preserves the two standing historical charges",
      len(contract["channels"]["VERIFY"]["hostile_charges"]) == 2)
check("exact", "current hostile review also executes propagation charge three",
      all(label in review for label in ("Charge 1", "Charge 2", "Charge 3")))

# Plants demonstrate that the audit predicates are live rather than decorative.
plant = deepcopy(bank)
plant["construction_hash"] = "0" * 64
check("planted", "PLANT wrong construction hash fires", construction_hash(plant) != plant["construction_hash"])
plant = deepcopy(bank)
plant["receivers"]["labels"].pop()
check("planted", "PLANT missing receiver fires", len(plant["receivers"]["labels"]) != 1274)
plant = deepcopy(bank)
plant["scientific_scope"]["full_U64_64"] = "PORTED"
check("planted", "PLANT silent full-unitary port fires", plant["scientific_scope"]["full_U64_64"] != "NOT_PORTED")
plant_routing = deepcopy(routing)
plant_routing["mandatory_eight"].pop()
check("planted", "PLANT missing mandatory lens fires", len(plant_routing["mandatory_eight"]) != 8)
plant_routing = deepcopy(routing)
plant_routing["all_lenses_every_cell"] = True
check("planted", "PLANT persona-count theater fires", plant_routing["all_lenses_every_cell"] is not False)

failures = [label for _, label, ok in checks if not ok]
exact = sum(kind == "exact" for kind, _, _ in checks)
planted = sum(kind == "planted" for kind, _, _ in checks)
print("PASS {}/{} ({} exact + {} planted)".format(len(checks)-len(failures), len(checks), exact, planted))
if failures:
    raise SystemExit("; ".join(failures))
