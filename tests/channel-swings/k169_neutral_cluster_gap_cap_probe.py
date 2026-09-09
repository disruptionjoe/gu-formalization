#!/usr/bin/env python3
"""Independent invariants and hostile mutations for K169."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = ROOT / "lab/process/k169-neutral-cluster-gap-cap-wave.json"


def _load():
    path = HERE / "k169_neutral_cluster_gap_cap.py"
    spec = importlib.util.spec_from_file_location("k169_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K169 = _load()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    cluster = data.get("neutral_cluster", {})
    complement = data.get("finite_trial_complement", {})
    chart = data.get("K139_chart_transport", {})
    transfer = data.get("K168_transfer_disposition", {})
    control = data.get("direct_reference_positive_control", {})
    replay = data.get("native_K152_replay", {})
    source = data.get("source_and_physics", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if cluster.get("cluster_charge") != [0, 0] or cluster.get("neutral_cluster_energy_infimum") != "5/2":
        failures.append("neutral_cluster")
    if cluster.get("fixed_total_charge_preserved") is not True or cluster.get("first_threshold_identified") is not False:
        failures.append("threshold_scope")
    if cluster.get("local_reference_extension_changes_escape_cost") is not False:
        failures.append("escape_cost_scope")
    if complement.get("universal_margin_upper") != "5/2":
        failures.append("margin_cap")
    if complement.get("finite_codimension_Weyl_sequence_survives_projection") is not True:
        failures.append("finite_codimension")
    if complement.get("applies_to_every_finite_K162_trial_space") is not True:
        failures.append("K162_scope")
    if chart.get("regular_metric") != "M=S* S" or chart.get("gap_cap_preserved_under_chart") is not True:
        failures.append("chart")
    if chart.get("free_Hilbert_complement_substituted") is not False:
        failures.append("complement_type")
    if transfer.get("neutral_cluster_gap_cap") != "5/2" or transfer.get("K168_shape_oscillation") != "3":
        failures.append("transfer_inputs")
    if transfer.get("strict_transfer_condition_attainable") is not False:
        failures.append("transfer_verdict")
    if transfer.get("direct_base_to_reference_gap_transfer") is not False or transfer.get("direct_reference_specific_K152_route_open") is not True:
        failures.append("route_disposition")
    if control.get("ground_to_next_gap") != "2" or control.get("gap_exceeds_three") is not False:
        failures.append("positive_control_gap")
    if control.get("M_orthogonal_complement_inertia") != [0, 0, 2] or control.get("full_pencil_inertia") != [1, 0, 2]:
        failures.append("positive_control_inertia")
    if control.get("exactly_one_below_threshold") is not True or control.get("native_K139_data") is not False:
        failures.append("positive_control_scope")
    if replay.get("three_unit_transfer_route") != "KILLED_BY_NATIVE_NEUTRAL_CLUSTER_GAP_CAP" or replay.get("direct_reference_route") != "OPEN":
        failures.append("replay_route")
    if replay.get("native_same_form_packet_complete") is not False or replay.get("native_K152_interval_emitted") is not False:
        failures.append("native_overclaim")
    if source.get("SC_META_53_polarity") != "UNCERTAIN" or any(source.get(key) != "NEEDS" for key in ("LT_SM8_verdict", "RA_F1_verdict", "AC_F1_verdict")):
        failures.append("source_ledger")
    if any(source.get(key) is not False for key in (
        "ledger_changed", "source_register_changed", "physical_or_source_selection",
        "Born_prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move",
    )):
        failures.append("claim_ceiling")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("5/2", "three-unit", "M-orthogonal", "direct", "no native K152"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def baseline() -> list[tuple[str, bool]]:
    demo = K169.demo()
    cluster = demo["neutral_cluster"]
    complement = demo["finite_trial_complement"]
    chart = demo["K139_chart_transport"]
    transfer = demo["K168_transfer_disposition"]
    control = demo["direct_reference_positive_control"]
    replay = demo["native_K152_replay"]
    rejected = []
    for args, token in (((0,), "positive"), ((Fraction(5, 4), -2, -1), "cannot lie below")):
        try:
            if len(args) == 1:
                K169.neutral_cluster_threshold(*args)
            else:
                K169.finite_trial_complement_cap(*args)
        except K169.CertificateError as exc:
            rejected.append(token in str(exc))
        else:
            rejected.append(False)
    return [
        ("particle-hole neutral", cluster["cluster_charge"] == [0, 0]),
        ("two escape particles", cluster["cluster_particle_number"] == 2),
        ("mass gap", cluster["single_escape_energy_infimum"] == "5/4"),
        ("neutral energy", cluster["neutral_cluster_energy_infimum"] == "5/2"),
        ("threshold membership", "belongs" in cluster["HVZ_threshold_membership"]),
        ("not first threshold", cluster["first_threshold_identified"] is False),
        ("local extension inert at infinity", cluster["local_reference_extension_changes_escape_cost"] is False),
        ("finite projection survives", complement["finite_codimension_Weyl_sequence_survives_projection"] is True),
        ("all finite K162 spaces", complement["applies_to_every_finite_K162_trial_space"] is True),
        ("margin cap", complement["universal_margin_upper"] == "5/2"),
        ("complement floor not identified", complement["identifies_actual_complement_floor"] is False),
        ("M metric", chart["regular_metric"] == "M=S* S"),
        ("M complement", "perp_M" in chart["regular_coordinate_complement"]),
        ("no free complement paste", chart["free_Hilbert_complement_substituted"] is False),
        ("chart preserves cap", chart["gap_cap_preserved_under_chart"] is True),
        ("five halves below three", Fraction(transfer["neutral_cluster_gap_cap"]) < Fraction(transfer["K168_shape_oscillation"])),
        ("transfer unattainable", transfer["strict_transfer_condition_attainable"] is False),
        ("direct route open", transfer["direct_reference_specific_K152_route_open"] is True),
        ("nonidentity metric control", control["metric"] != [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]),
        ("sub-three valid gap", control["ground_to_next_gap"] == "2" and control["gap_exceeds_three"] is False),
        ("zero residual", control["matched_residual"] == ["0", "0", "0"]),
        ("positive M complement", control["M_orthogonal_complement_inertia"] == [0, 0, 2]),
        ("one below threshold", control["exactly_one_below_threshold"] is True),
        ("control fenced", control["native_K139_data"] is False),
        ("transfer route killed", replay["three_unit_transfer_route"].startswith("KILLED")),
        ("native packet closed", replay["native_same_form_packet_complete"] is False),
        ("no interval", replay["native_K152_interval_emitted"] is False),
        ("no physical selection", demo["physical_or_source_selection"] is False),
        ("no Born credit", demo["Born_prediction_or_confirmation_credit"] is False),
        ("bad inputs rejected", all(rejected)),
    ]


def selftest(data: dict) -> int:
    updates = (
        ("charge_leak", lambda d: d["neutral_cluster"].__setitem__("cluster_charge", [1, 0])),
        ("wrong_energy", lambda d: d["neutral_cluster"].__setitem__("neutral_cluster_energy_infimum", "3")),
        ("claim_first", lambda d: d["neutral_cluster"].__setitem__("first_threshold_identified", True)),
        ("extension_changes_mass", lambda d: d["neutral_cluster"].__setitem__("local_reference_extension_changes_escape_cost", True)),
        ("erase_weyl", lambda d: d["finite_trial_complement"].__setitem__("finite_codimension_Weyl_sequence_survives_projection", False)),
        ("inflate_cap", lambda d: d["finite_trial_complement"].__setitem__("universal_margin_upper", "7/2")),
        ("use_free_complement", lambda d: d["K139_chart_transport"].__setitem__("free_Hilbert_complement_substituted", True)),
        ("break_chart", lambda d: d["K139_chart_transport"].__setitem__("gap_cap_preserved_under_chart", False)),
        ("invent_transfer", lambda d: d["K168_transfer_disposition"].__setitem__("strict_transfer_condition_attainable", True)),
        ("close_direct", lambda d: d["K168_transfer_disposition"].__setitem__("direct_reference_specific_K152_route_open", False)),
        ("inflate_control_gap", lambda d: d["direct_reference_positive_control"].__setitem__("gap_exceeds_three", True)),
        ("break_complement", lambda d: d["direct_reference_positive_control"].__setitem__("M_orthogonal_complement_inertia", [1, 0, 1])),
        ("promote_control", lambda d: d["direct_reference_positive_control"].__setitem__("native_K139_data", True)),
        ("invent_packet", lambda d: d["native_K152_replay"].__setitem__("native_same_form_packet_complete", True)),
        ("invent_interval", lambda d: d["native_K152_replay"].__setitem__("native_K152_interval_emitted", True)),
        ("move_source", lambda d: d["source_and_physics"].__setitem__("SC_META_53_polarity", "ASSERTS")),
        ("move_ledger", lambda d: d["source_and_physics"].__setitem__("LT_SM8_verdict", "SAME")),
        ("promote", lambda d: d["source_and_physics"].__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = baseline()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K169 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
