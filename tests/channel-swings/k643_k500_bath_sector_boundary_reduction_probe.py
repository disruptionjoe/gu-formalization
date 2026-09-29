#!/usr/bin/env python3
"""Independent baseline and hostile controls for K643."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json"


def load_solver():
    path = Path(__file__).with_name("k643_k500_bath_sector_boundary_reduction.py")
    spec = importlib.util.spec_from_file_location("k643_probe_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    replay = data.get("native_replay", {})
    theorem = data.get("sector_reduction_theorem", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    decision = data.get("decision", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if replay.get("term_count") != 2958 or replay.get("family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686":
        bad.append("family")
    for key in ("matched_polarity_for_every_term", "one_bath_creation_and_one_bath_annihilation_per_exchange_monomial", "total_bath_number_preserved_by_every_exchange_monomial", "remaining_variable_arity_equals_order", "K603_all_action_terms_retained"):
        if replay.get(key) is not True:
            bad.append(f"replay:{key}")
    if theorem.get("global_lower_constant") != "m=inf_(n>=0)m_n" or "same m" not in str(theorem.get("uniform_equivalence", "")):
        bad.append("uniform_floor")
    if "tail" not in str(theorem.get("finite_prefix_consequence", "")) or "min" not in str(theorem.get("tail_composition", "")):
        bad.append("tail")
    if controls.get("combined_is_minimum") is not True or controls.get("nonuniform_continuation_has_no_finite_global_lower") is not True:
        bad.append("controls")
    required_false = ("actual_K139_K168_intertwiner_identified", "actual_sector_forms_B_n_identified", "actual_sector_floors_m_n_identified", "uniform_tail_lower_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if decision.get("operator_floor_problem_reduced_to_sector_local_data_plus_uniform_tail") is not True or decision.get("finite_sector_checks_suffice_for_native_global_m") is not False:
        bad.append("decision")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("uniform infimum", "finite prefix", "actual intertwiner", "no native complete-sector floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    replay = data["native_replay"]
    theorem = data["sector_reduction_theorem"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    return [
        ("fresh replay matches", fresh["native_replay"] == replay),
        ("fresh theorem matches", fresh["sector_reduction_theorem"] == theorem),
        ("2958 terms", replay["term_count"] == 2958),
        ("orders two through twelve", replay["orders_present"] == list(range(2, 13))),
        ("family digest", replay["family_sha256"] == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686"),
        ("matched polarity", replay["matched_polarity_for_every_term"] is True),
        ("one create one annihilate", replay["one_bath_creation_and_one_bath_annihilation_per_exchange_monomial"] is True),
        ("number preserved", replay["total_bath_number_preserved_by_every_exchange_monomial"] is True),
        ("arity matches", replay["remaining_variable_arity_equals_order"] is True),
        ("33 signature blocks", replay["K603_signature_blocks_replayed"] == 33),
        ("all action terms", replay["K603_all_action_terms_retained"] is True),
        ("sector projections", "P_n" in theorem["sector_projections"]),
        ("six tensor sector", theorem["coefficient_sector"] == "H_b,n=C^6 tensor H_n"),
        ("orthogonal direct sum", "orthogonal form sum" in theorem["reducing_property"]),
        ("sector floor", "m_n" in theorem["sector_lower_hypothesis"]),
        ("uniform infimum", theorem["global_lower_constant"] == "m=inf_(n>=0)m_n"),
        ("iff same m", "same m" in theorem["uniform_equivalence"]),
        ("bad sector rejects", "rejects" in theorem["single_bad_sector_consequence"]),
        ("finite prefix needs tail", "tail" in theorem["finite_prefix_consequence"]),
        ("tail composition", "min(m_prefix,m_tail)" in theorem["tail_composition"]),
        ("intertwiner constrained", "number-preserving" in theorem["intertwiner_constraint"]),
        ("prefix floor", controls["finite_prefix_floor"] == "-2"),
        ("combined floor", controls["combined_uniform_floor"] == "-2"),
        ("combined minimum", controls["combined_is_minimum"] is True),
        ("sectorwise not uniform", controls["nonuniform_continuation_has_no_finite_global_lower"] is True),
        ("localization proved", native["sector_localization_of_future_B_proved"] is True),
        ("native m withheld", native["native_global_m_identified"] is False),
        ("K473 withheld", native["K473_released"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("drop term", lambda d: d["native_replay"].__setitem__("term_count", 2957)),
        ("change digest", lambda d: d["native_replay"].__setitem__("family_sha256", "bad")),
        ("break polarity", lambda d: d["native_replay"].__setitem__("matched_polarity_for_every_term", False)),
        ("break normal order", lambda d: d["native_replay"].__setitem__("one_bath_creation_and_one_bath_annihilation_per_exchange_monomial", False)),
        ("break number", lambda d: d["native_replay"].__setitem__("total_bath_number_preserved_by_every_exchange_monomial", False)),
        ("break arity", lambda d: d["native_replay"].__setitem__("remaining_variable_arity_equals_order", False)),
        ("lose K603", lambda d: d["native_replay"].__setitem__("K603_all_action_terms_retained", False)),
        ("wrong global floor", lambda d: d["sector_reduction_theorem"].__setitem__("global_lower_constant", "m=m_0")),
        ("erase uniform iff", lambda d: d["sector_reduction_theorem"].__setitem__("uniform_equivalence", "sectorwise")),
        ("erase tail need", lambda d: d["sector_reduction_theorem"].__setitem__("finite_prefix_consequence", "prefix proves global")),
        ("erase tail min", lambda d: d["sector_reduction_theorem"].__setitem__("tail_composition", "prefix only")),
        ("fail exact control", lambda d: d["exact_controls"].__setitem__("combined_is_minimum", False)),
        ("claim uniform nonuniform family", lambda d: d["exact_controls"].__setitem__("nonuniform_continuation_has_no_finite_global_lower", False)),
        ("invent intertwiner", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_intertwiner_identified", True)),
        ("invent sector forms", lambda d: d["native_interface_status"].__setitem__("actual_sector_forms_B_n_identified", True)),
        ("invent sector floors", lambda d: d["native_interface_status"].__setitem__("actual_sector_floors_m_n_identified", True)),
        ("invent tail", lambda d: d["native_interface_status"].__setitem__("uniform_tail_lower_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("deny reduction", lambda d: d["decision"].__setitem__("operator_floor_problem_reduced_to_sector_local_data_plus_uniform_tail", False)),
        ("claim finite suffices", lambda d: d["decision"].__setitem__("finite_sector_checks_suffice_for_native_global_m", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native floor proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K643 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
