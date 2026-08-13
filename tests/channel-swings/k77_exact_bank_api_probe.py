#!/usr/bin/env python3
"""Fast consumer/integrity probe for the versioned K77 exact bank."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
API_PATH = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
FIXTURE = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"

spec = importlib.util.spec_from_file_location("k77_exact_bank_api", API_PATH)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
started = time.perf_counter()
spec.loader.exec_module(api)
import_seconds = time.perf_counter() - started

checks = []


def check(kind, label, condition):
    ok = bool(condition)
    checks.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def write_payload(payload):
    handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    with handle:
        handle.write(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")
    return Path(handle.name)


def rejected(payload, verify_dependencies=True):
    path = write_payload(payload)
    try:
        try:
            api.load_bank(path, verify_dependencies=verify_dependencies)
        except api.BankIntegrityError:
            return True
        return False
    finally:
        path.unlink(missing_ok=True)


source = API_PATH.read_text(encoding="utf-8")
check("exact", "API imports without recursive runpy", "runpy" not in source)
check("exact", "API imports without SymPy or NumPy", "sympy" not in source.lower() and "numpy" not in source.lower())
check("exact", "API module import is bounded", import_seconds < 1.0)

started = time.perf_counter()
bank = api.load_bank()
load_seconds = time.perf_counter() - started
payload = bank.payload
check("exact", "verified bank load is bounded", load_seconds < 2.0)
check("exact", "carrier is exact real K77", bank.signature.count(1) == 7 and bank.signature.count(-1) == 7)
check("exact", "selected Shiab channels are carried", len(bank.channels) == 3)
check("exact", "epsilon tangent has 91 labelled generators", len(payload["carrier"]["epsilon_generators"]) == 91)
check("exact", "grade-two equation dual has 1274 labelled receivers", len(bank.receiver_labels) == 1274)
check("exact", "horizontal/off-slice split is 24 plus 1250",
      len(payload["receivers"]["horizontal_rows"]) == 24
      and len(payload["receivers"]["offslice_rows"]) == 1250)
check("exact", "all three causal coefficient banks are present",
      set(payload["columns"]) == {"timelike", "spacelike", "null"})
check("exact", "each causal bank contains ten metric plus 91 epsilon columns",
      all(len(payload["columns"][name]) == 101 for name in payload["columns"]))
check("exact", "source custody hashes are dependency-owned",
      set(payload["source_revision_hashes"]).issubset(payload["dependency_hashes"]))
check("exact", "construction hash matches canonical payload", api.payload_hash(payload) == payload["construction_hash"])
check("exact", "fixture file hash is stable inside this replay", sha256(FIXTURE.read_bytes()).hexdigest() == api.file_hash(FIXTURE))
check("exact", "epsilon completion fence remains total=fixed with zero moving corrections",
      payload["epsilon_completion"]["complete_equals_fixed_coefficientwise"] is True
      and payload["epsilon_completion"]["lower_cartan_grade2"] == "ZERO"
      and payload["epsilon_completion"]["moving_shiab_grade2"] == "ZERO")
check("exact", "two U32,32 halves are explicitly not ported",
      payload["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED")
check("exact", "full U64,64 is explicitly not ported",
      payload["scientific_scope"]["full_U64_64"] == "NOT_PORTED")

# Select bounded witnesses from the serialized support before invoking the
# independent direct evaluator. This is output-blind with respect to replay.
for causal in ("timelike", "spacelike", "null"):
    selected = None
    for item in payload["columns"][causal][10:]:
        rows = sorted({entry[0] for part in ("constant", "b", "t") for entry in item[part]})
        if rows:
            selected = item, rows[0]
            break
    check("exact", f"{causal} has a preselected nonzero epsilon witness", selected is not None)
    if selected is not None:
        item, row = selected
        direct = bank.direct_epsilon_polynomial(causal, item["index"], row)
        cached = tuple(bank.column(causal, "epsilon", item["index"], part).get(row, 0)
                       for part in ("constant", "b", "t"))
        check("exact", f"{causal} bounded direct epsilon replay equals cache", direct == cached)

mutated = deepcopy(payload)
mutated["columns"]["timelike"][10]["constant"].append([0, 1, 1])
check("planted", "PLANT coefficient mutation without re-signing is rejected", rejected(mutated))

stale = deepcopy(payload)
first_dependency = sorted(stale["dependency_hashes"])[0]
stale["dependency_hashes"][first_dependency] = "0" * 64
stale["construction_hash"] = api.payload_hash(stale)
check("planted", "PLANT re-signed stale dependency is rejected", rejected(stale))

malformed = deepcopy(payload)
malformed["receivers"]["labels"].pop()
malformed["construction_hash"] = api.payload_hash(malformed)
check("planted", "PLANT re-signed wrong receiver count is rejected", rejected(malformed, False))

duplicate_text = '{"schema_version":"1.0","schema_version":"1.0"}'
duplicate_path = Path(tempfile.mkstemp(suffix=".json")[1])
try:
    duplicate_path.write_text(duplicate_text, encoding="utf-8")
    try:
        api.strict_load(duplicate_path)
        duplicate_rejected = False
    except api.BankIntegrityError:
        duplicate_rejected = True
finally:
    duplicate_path.unlink(missing_ok=True)
check("planted", "PLANT duplicate JSON key is rejected", duplicate_rejected)

failures = [label for _, label, ok in checks if not ok]
exact = sum(kind == "exact" for kind, _, _ in checks)
planted = sum(kind == "planted" for kind, _, _ in checks)
print(f"IMPORT_SECONDS={import_seconds:.6f}")
print(f"LOAD_SECONDS={load_seconds:.6f}")
print(f"PASS {len(checks) - len(failures)}/{len(checks)} ({exact} exact + {planted} planted)")
if failures:
    raise SystemExit("; ".join(failures))
