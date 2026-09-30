#!/usr/bin/env python3
"""Independent and hostile controls for K651."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k651_k500_parity_tail_prefix_nonidentifiability.py")
MANIFEST = ROOT / "lab/process/k651-k500-parity-tail-prefix-nonidentifiability.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k651_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K651 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    prefix = data.get("k179_prefix", {})
    theorem = data.get("prefix_nonidentifiability_theorem", {})
    native = data.get("native_interface_status", {})
    if prefix.get("orders") != list(range(2, 13)) or prefix.get("term_count") != 2958:
        failures.append("prefix-custody")
    if prefix.get("all_order_tail_serialized") is not False:
        failures.append("invented-tail")
    required_true = ("preserves_K650_relative_interface", "preserves_total_parity_reduction")
    if any(theorem.get(key) is not True for key in required_true):
        failures.append("interface")
    required_false = (
        "uses_separately_singular_raw_rows", "finite_prefix_determines_uniform_tail",
        "finite_prefix_plus_qualitative_semiboundedness_determines_numeric_tail",
        "fixed_native_operator_has_no_floor", "future_all_order_estimate_excluded",
    )
    if any(theorem.get(key) is not False for key in required_false):
        failures.append("ceiling")
    if len(data.get("exact_controls", [])) != 4 or any(not row.get("prefixes_identical") for row in data.get("exact_controls", [])):
        failures.append("controls")
    if native.get("actual_uniform_parity_tails_identified") is not False or native.get("native_global_m_identified") is not False:
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("orders two through twelve", "do not determine", "does not deny", "No native m"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    rows = data["exact_controls"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("K179 prefix ends at twelve", data["k179_prefix"]["maximum_order"] == 12),
        ("K179 prefix has 2,958 terms", data["k179_prefix"]["term_count"] == 2958),
        ("four depths are tested", len(rows) == 4),
        ("every family agrees through the prefix", all(row["prefixes_identical"] for row in rows)),
        ("every family preserves total parity", all(row["parity_covariant"] for row in rows)),
        ("every family stays on one same domain", all(row["same_domain"] == "C^2 in every bath/parity sector" for row in rows)),
        ("relative coupling vanishes in the controls", all(row["relative_coupling_rho"] == "0" for row in rows)),
        ("residual coupling vanishes in the controls", all(row["residual_coupling_kappa"] == "0" for row in rows)),
        ("positive controls retain tail seven quarters", all(row["positive_complete_tail_floor"] == "7/4" for row in rows)),
        ("adverse floors decrease without bound across controls", [row["adverse_complete_tail_floor_at_most"] for row in rows] == ["-2", "-9", "-65", "-1025"]),
        ("finite prefix is not promoted to a tail", not data["prefix_nonidentifiability_theorem"]["finite_prefix_determines_uniform_tail"]),
        ("native floor is not denied", not data["prefix_nonidentifiability_theorem"]["fixed_native_operator_has_no_floor"]),
        ("all-order repair remains live", not data["prefix_nonidentifiability_theorem"]["future_all_order_estimate_excluded"]),
        ("K650 interface is consumed", data["dependency_reconciliation"]["K650_cancelled_quadrant_interface_consumed"]),
        ("K612 is preserved", not data["dependency_reconciliation"]["K612_data_custody_obstruction_retracted"]),
        ("no native tail is claimed", not data["native_interface_status"]["actual_uniform_parity_tails_identified"]),
        ("no native m is claimed", not data["native_interface_status"]["native_global_m_identified"]),
        ("K473 stays closed", not data["native_interface_status"]["K473_released"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("extend-prefix", lambda d: d["k179_prefix"].__setitem__("orders", list(range(2, 14)))),
        ("invent-terms", lambda d: d["k179_prefix"].__setitem__("term_count", 2959)),
        ("invent-tail", lambda d: d["k179_prefix"].__setitem__("all_order_tail_serialized", True)),
        ("erase-interface", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("preserves_K650_relative_interface", False)),
        ("erase-parity", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("preserves_total_parity_reduction", False)),
        ("use-raw", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("uses_separately_singular_raw_rows", True)),
        ("promote-prefix", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("finite_prefix_determines_uniform_tail", True)),
        ("promote-qualitative", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("finite_prefix_plus_qualitative_semiboundedness_determines_numeric_tail", True)),
        ("invent-no-floor", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("fixed_native_operator_has_no_floor", True)),
        ("kill-repair", lambda d: d["prefix_nonidentifiability_theorem"].__setitem__("future_all_order_estimate_excluded", True)),
        ("erase-controls", lambda d: d.__setitem__("exact_controls", d["exact_controls"][:3])),
        ("break-prefix-match", lambda d: d["exact_controls"][0].__setitem__("prefixes_identical", False)),
        ("invent-native-tail", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native operator is unbounded below.")),
    )
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K651 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
