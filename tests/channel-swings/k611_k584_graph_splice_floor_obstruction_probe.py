#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K611."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k611_k584_graph_splice_floor_obstruction.py"
ARTIFACT = ROOT / "lab/process/k611-k584-graph-splice-floor-obstruction.json"


def load():
    spec = importlib.util.spec_from_file_location("k611_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    payload = module.build()
    module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    a = payload["rejected_candidate_arithmetic"]
    s = payload["same_domain_audit"]
    r = payload["dependency_reconciliation"]
    d = payload["decision"]
    checks = [
        a["proposed_total"] == "87/100",
        not a["operator_norm_product_is_well_typed"],
        not s["free_energy_graph_has_finite_chart_contraction"],
        not s["particle_number_graph_has_finite_core_bound"],
        not s["quarter_graph_has_complete_core_bound"],
        s["all_positive_diagonal_weight_graphs_ruled_out"],
        r["K462_existential_complete_sector_semibound_preserved"],
        r["K581_existential_noncyclic_floor_preserved"],
        r["K609_uniform_leakage_preserved"],
        not d["named_complete_sector_floor_emitted"],
    ]
    mutations = [
        lambda p: p["rejected_candidate_arithmetic"].__setitem__("proposed_core_resolvent_piece", "2/3"),
        lambda p: p["rejected_candidate_arithmetic"].__setitem__("operator_norm_product_is_well_typed", True),
        lambda p: p["rejected_candidate_arithmetic"].__setitem__("candidate_floor_certified", True),
        lambda p: p["same_domain_audit"].__setitem__("free_energy_graph_has_finite_chart_contraction", True),
        lambda p: p["same_domain_audit"].__setitem__("particle_number_graph_has_finite_core_bound", True),
        lambda p: p["same_domain_audit"].__setitem__("quarter_graph_has_complete_core_bound", True),
        lambda p: p["same_domain_audit"].__setitem__("all_positive_diagonal_weight_graphs_ruled_out", False),
        lambda p: p["same_domain_audit"].__setitem__("non_diagonal_or_cancellation_adapted_domains_ruled_out", True),
        lambda p: p["dependency_reconciliation"].__setitem__("K462_existential_complete_sector_semibound_preserved", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K609_reused_as_floor_evidence", True),
        lambda p: p["dependency_reconciliation"].__setitem__("K139_or_K156_retracted", True),
        lambda p: p["decision"].__setitem__("named_complete_sector_floor_emitted", True),
        lambda p: p["decision"].__setitem__("K473_released", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload)
        mutate(changed)
        try:
            module.validate(changed)
        except AssertionError:
            rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K611 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K611 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
