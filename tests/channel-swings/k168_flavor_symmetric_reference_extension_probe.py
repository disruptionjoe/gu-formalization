#!/usr/bin/env python3
"""Independent invariants and hostile mutations for K168."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = ROOT / "lab/process/k168-flavor-symmetric-reference-extension-wave.json"


def _load():
    path = HERE / "k168_flavor_symmetric_reference_extension.py"
    spec = importlib.util.spec_from_file_location("k168_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K168 = _load()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    ref = data.get("reference_extension", {})
    compat = data.get("native_compatibility", {})
    form = data.get("fixed_chart_form_consequences", {})
    seed = data.get("representative_seed_boundary", {})
    replay = data.get("native_K152_replay", {})
    source = data.get("source_and_physics", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if ref.get("diagonal") != ["-2", "1", "1"] or ref.get("trace") != "0":
        failures.append("reference")
    if any(ref.get(key) is not True for key in ("Hermitian", "non_scalar", "flavor_symmetric", "primitive_integer_normalization")):
        failures.append("reference_properties")
    if ref.get("physical_selection") is not False:
        failures.append("reference_ownership")
    if any(compat.get(key) is not True for key in (
        "hard_core_C3_complete", "preserves_q1_q2_charge_blocks",
        "preserves_K162_dyadic_domains", "bounded_form_perturbation",
        "signed_flavor_swap_intertwines",
    )):
        failures.append("compatibility")
    if form.get("complete_form_order") != "R_0-2M<=R_ref<=R_0+M":
        failures.append("form_order")
    if form.get("every_ordered_generalized_eigenvalue_shift_interval") != ["-2", "1"]:
        failures.append("spectral_order")
    if form.get("maximum_absolute_change_of_a_relative_gap") != "3":
        failures.append("gap_bound")
    if form.get("matched_shape_residual_increment_M_dual_norm_upper") != "3*||u||_M":
        failures.append("residual_bound")
    if form.get("base_gap_at_most_three_certifies_positive_reference_gap") is not False:
        failures.append("gap_overclaim")
    if form.get("base_complement_margin_at_most_three_certifies_reference_positivity") is not False:
        failures.append("complement_overclaim")
    if seed.get("finite_control_commutator_nonzero") is not True or seed.get("dressed_K139_trial_extension_value_equals_bare_seed_value_in_general") is not False:
        failures.append("dressed_seed_boundary")
    if replay.get("reference_declaration_complete") is not True or replay.get("native_same_form_packet_complete") is not False:
        failures.append("replay")
    if len(replay.get("missing_native_references", [])) != 6:
        failures.append("missing_native_fields")
    if replay.get("native_ground_count_emitted") is not False or replay.get("native_K152_interval_emitted") is not False:
        failures.append("native_overclaim")
    if source.get("SC_META_53_polarity") != "UNCERTAIN" or any(source.get(key) != "NEEDS" for key in ("LT_SM8_verdict", "RA_F1_verdict", "AC_F1_verdict")):
        failures.append("source_ledger")
    if any(source.get(key) is not False for key in (
        "ledger_changed", "source_register_changed", "physical_or_source_selection",
        "Born_prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move",
    )):
        failures.append("claim_ceiling")
    ceiling = data.get("claim_ceiling", "")
    for token in ("diag(-2,1,1)", "-2M", "R0", "residual", "complement", "no physical"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def baseline() -> list[tuple[str, bool]]:
    demo = K168.demo()
    ref = demo["reference_extension"]
    finite = demo["finite_K155_control"]
    replay = demo["native_K152_replay"]
    bad_calls = []
    for values, token in (((-1, 1, 1), "zero scalar"), ((-2, 1, 2), "flavor"), ((0, 0, 0), "non-scalar"), ((-4, 2, 2), "primitive")):
        try:
            K168.reference_extension(values)
        except K168.CertificateError as exc:
            bad_calls.append(token in str(exc))
        else:
            bad_calls.append(False)
    return [
        ("complete C3 declaration", ref["dimension"] == 3),
        ("trace zero", ref["trace"] == "0"),
        ("non-scalar", ref["non_scalar"] is True),
        ("flavor symmetric", ref["flavor_symmetric"] is True),
        ("conditional only", ref["physical_selection"] is False),
        ("vacuum value", K168.impurity_value(0) == Fraction(-2)),
        ("d1 value", K168.impurity_value(1) == Fraction(1)),
        ("d2 value", K168.impurity_value(2) == Fraction(1)),
        ("finite pullback exact", finite["pullback_identity"] == "R_ref=R_0+S*W_ref*S"),
        ("finite lower order", finite["lower_slack_inertia"][0] == 0),
        ("finite upper order", finite["upper_slack_inertia"][0] == 0),
        ("noncommuting shape", finite["extension_commutes_with_boundary_map"] is False),
        ("finite control fenced", finite["finite_regulator_control_only"] is True),
        ("flavor intertwiner", demo["native_compatibility"]["signed_flavor_swap_intertwines"] is True),
        ("spectral shift interval", demo["fixed_chart_form_consequences"]["every_ordered_generalized_eigenvalue_shift_interval"] == ["-2", "1"]),
        ("gap oscillation", demo["fixed_chart_form_consequences"]["maximum_absolute_change_of_a_relative_gap"] == "3"),
        ("residual increment", demo["fixed_chart_form_consequences"]["matched_shape_residual_increment_M_dual_norm_upper"] == "3*||u||_M"),
        ("bare seed fenced", demo["representative_seed_boundary"]["dressed_K139_trial_extension_value_equals_bare_seed_value_in_general"] is False),
        ("reference gate closed", replay["reference_declaration_complete"] is True),
        ("six native fields remain", len(replay["missing_native_references"]) == 6),
        ("native packet remains closed", replay["native_same_form_packet_complete"] is False),
        ("no count", replay["native_ground_count_emitted"] is False),
        ("no interval", replay["native_K152_interval_emitted"] is False),
        ("no physical selection", demo["physical_or_source_selection"] is False),
        ("no Born credit", demo["Born_prediction_or_confirmation_credit"] is False),
        ("bad declarations rejected", all(bad_calls)),
    ]


def selftest(data: dict) -> int:
    updates = (
        ("scalarize", lambda d: d["reference_extension"].__setitem__("non_scalar", False)),
        ("break_trace", lambda d: d["reference_extension"].__setitem__("trace", "1")),
        ("break_flavor", lambda d: d["reference_extension"].__setitem__("flavor_symmetric", False)),
        ("invent_selection", lambda d: d["reference_extension"].__setitem__("physical_selection", True)),
        ("break_charge", lambda d: d["native_compatibility"].__setitem__("preserves_q1_q2_charge_blocks", False)),
        ("break_domain", lambda d: d["native_compatibility"].__setitem__("preserves_K162_dyadic_domains", False)),
        ("break_intertwiner", lambda d: d["native_compatibility"].__setitem__("signed_flavor_swap_intertwines", False)),
        ("erase_order", lambda d: d["fixed_chart_form_consequences"].__setitem__("complete_form_order", "unknown")),
        ("tighten_shift", lambda d: d["fixed_chart_form_consequences"].__setitem__("every_ordered_generalized_eigenvalue_shift_interval", ["-1", "1"])),
        ("invent_gap", lambda d: d["fixed_chart_form_consequences"].__setitem__("base_gap_at_most_three_certifies_positive_reference_gap", True)),
        ("invent_complement", lambda d: d["fixed_chart_form_consequences"].__setitem__("base_complement_margin_at_most_three_certifies_reference_positivity", True)),
        ("erase_commutator", lambda d: d["representative_seed_boundary"].__setitem__("finite_control_commutator_nonzero", False)),
        ("reuse_bare_seed", lambda d: d["representative_seed_boundary"].__setitem__("dressed_K139_trial_extension_value_equals_bare_seed_value_in_general", True)),
        ("reopen_reference", lambda d: d["native_K152_replay"].__setitem__("reference_declaration_complete", False)),
        ("invent_packet", lambda d: d["native_K152_replay"].__setitem__("native_same_form_packet_complete", True)),
        ("invent_count", lambda d: d["native_K152_replay"].__setitem__("native_ground_count_emitted", True)),
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
    print(f"K168 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
