#!/usr/bin/env python3
"""Independent exact and hostile controls for K645."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k645-k500-flavor-exchange-covariance.json"


def load_solver():
    path = Path(__file__).with_name("k645_k500_flavor_exchange_covariance.py")
    spec = importlib.util.spec_from_file_location("k645_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    replay = data.get("complete_family_replay", {})
    theorem = data.get("finite_order_theorem", {})
    limit = data.get("limit_interface", {})
    native = data.get("native_interface_status", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if replay.get("terms") != 2958 or replay.get("two_element_orbits") != 1479 or replay.get("fixed_terms") != 0:
        bad.append("orbits")
    if replay.get("output_wedge_phase_counts") != {"-1": 516, "1": 2442}:
        bad.append("phases")
    for key in ("all_partners_present", "swap_is_involutive", "analytic_kernel_bodies_invariant", "CAR_coefficients_transform_by_output_wedge_phase", "naive_sign_preservation_is_false"):
        if replay.get(key) is not True:
            bad.append(f"replay:{key}")
    if "every finite N" not in str(theorem.get("operator_identity", "")) or "bath number" not in str(theorem.get("bath_number_compatibility", "")):
        bad.append("theorem")
    if limit.get("physical_flavor_symmetry_claimed") is not False or limit.get("source_selected_family_interpretation_claimed") is not False:
        bad.append("scope")
    required_false = ("full_native_K139_K168_to_K642_form_identity_proved", "native_parity_floors_identified", "native_uniform_tail_identified", "native_global_m_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("1,479", "516", "not physical family selection", "no parity floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    replay = data["complete_family_replay"]
    theorem = data["finite_order_theorem"]
    extended = data["extended_controls"]
    native = data["native_interface_status"]
    return [
        ("fresh replay", fresh["complete_family_replay"] == replay),
        ("fresh theorem", fresh["finite_order_theorem"] == theorem),
        ("2958 terms", replay["terms"] == 2958),
        ("1479 orbits", replay["two_element_orbits"] == 1479),
        ("no fixed term", replay["fixed_terms"] == 0),
        ("family digest", replay["family_sha256"] == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686"),
        ("all partners", replay["all_partners_present"] is True),
        ("involutive", replay["swap_is_involutive"] is True),
        ("kernel invariant", replay["analytic_kernel_bodies_invariant"] is True),
        ("CAR phase", replay["CAR_coefficients_transform_by_output_wedge_phase"] is True),
        ("negative phases", replay["output_wedge_phase_counts"]["-1"] == 516),
        ("positive phases", replay["output_wedge_phase_counts"]["1"] == 2442),
        ("naive signs rejected", replay["naive_sign_preservation_is_false"] is True),
        ("three monomial orbits", len(replay["monomial_orbit_counts"]) == 3),
        ("all orders represented", replay["orbits_by_order"] == {str(k): v for k, v in {2:3,3:4,4:12,5:16,6:36,7:48,8:96,9:128,10:240,11:320,12:576}.items()}),
        ("automaton theorem", "every finite order" in theorem["automaton_equivariance"]),
        ("kernel theorem", "flavor blind" in theorem["kernel_equivariance"]),
        ("phase theorem", "induced permutation" in theorem["fermionic_phase"]),
        ("coefficient identity", "epsilon_out" in theorem["coefficient_identity"]),
        ("operator identity", "every finite N" in theorem["operator_identity"]),
        ("bath compatible", "bath number" in theorem["bath_number_compatibility"]),
        ("extended order", extended["maximum_order"] == 14),
        ("extended terms", extended["terms_checked"] == 7182),
        ("extended orbits", extended["two_element_orbits"] == 3591),
        ("extended pass", extended["all_controls_pass"] is True),
        ("extended not truth", extended["control_extends_serialized_family_truth"] is False),
        ("conditional scope", data["limit_interface"]["physical_flavor_symmetry_claimed"] is False),
        ("covariance proved", native["equal_coupling_coefficient_covariance_proved"] is True),
        ("native m withheld", native["native_global_m_identified"] is False),
        ("K473 withheld", native["K473_released"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("drop term", lambda d: d["complete_family_replay"].__setitem__("terms", 2957)),
        ("drop orbit", lambda d: d["complete_family_replay"].__setitem__("two_element_orbits", 1478)),
        ("invent fixed", lambda d: d["complete_family_replay"].__setitem__("fixed_terms", 1)),
        ("wrong phases", lambda d: d["complete_family_replay"].__setitem__("output_wedge_phase_counts", {"-1": 0, "1": 2958})),
        ("missing partner", lambda d: d["complete_family_replay"].__setitem__("all_partners_present", False)),
        ("break involution", lambda d: d["complete_family_replay"].__setitem__("swap_is_involutive", False)),
        ("change kernel", lambda d: d["complete_family_replay"].__setitem__("analytic_kernel_bodies_invariant", False)),
        ("erase CAR phase", lambda d: d["complete_family_replay"].__setitem__("CAR_coefficients_transform_by_output_wedge_phase", False)),
        ("claim naive signs", lambda d: d["complete_family_replay"].__setitem__("naive_sign_preservation_is_false", False)),
        ("finite only", lambda d: d["finite_order_theorem"].__setitem__("operator_identity", "order twelve only")),
        ("lose bath", lambda d: d["finite_order_theorem"].__setitem__("bath_number_compatibility", "unknown")),
        ("claim physical symmetry", lambda d: d["limit_interface"].__setitem__("physical_flavor_symmetry_claimed", True)),
        ("claim source selection", lambda d: d["limit_interface"].__setitem__("source_selected_family_interpretation_claimed", True)),
        ("invent form identity", lambda d: d["native_interface_status"].__setitem__("full_native_K139_K168_to_K642_form_identity_proved", True)),
        ("invent parity floors", lambda d: d["native_interface_status"].__setitem__("native_parity_floors_identified", True)),
        ("invent tail", lambda d: d["native_interface_status"].__setitem__("native_uniform_tail_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("wrong routing", lambda d: d.__setitem__("classification", "PHYSICAL")),
        ("wrong direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("erase orbit ceiling", lambda d: d.__setitem__("claim_ceiling", d["claim_ceiling"].replace("1,479", "many"))),
        ("erase phase ceiling", lambda d: d.__setitem__("claim_ceiling", d["claim_ceiling"].replace("516", "some"))),
        ("promote ceiling", lambda d: d.__setitem__("claim_ceiling", "physical flavor symmetry with native floor")),
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
    print(f"K645 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
