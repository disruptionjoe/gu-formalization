#!/usr/bin/env python3
"""Independent and hostile controls for K657."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k657_k500_boundary_weyl_base_floor_certificate.py")
MANIFEST = ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k657_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K657 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def failures(data: dict) -> list[str]:
    out: list[str] = []
    theorem = data.get("ordinary_boundary_triple_theorem", {})
    gate = data.get("fail_closed_admission", {})
    native = data.get("native_interface_status", {})
    if theorem.get("equivalence") != "A_W>=lambda iff D_W(lambda)>=0":
        out.append("equivalence")
    if "Theorem A.7(i)" not in theorem.get("theorem_basis", ""):
        out.append("theorem-basis")
    if "A-lambda I" not in theorem.get("scalar_shift", ""):
        out.append("scalar-shift")
    if "Friedrichs extension" not in theorem.get("reference_premise", ""):
        out.append("friedrichs-reference")
    if "M(lambda) is bounded" not in theorem.get("boundary_space_premise", ""):
        out.append("bounded-weyl")
    for key in ("common_free_form_domain_required", "finite_impurity_denominator_sufficient", "native_sign_convention_may_be_inferred"):
        if theorem.get(key) is not False:
            out.append(key)
    for key in ("missing_any_field_rejects", "pointwise_sector_samples_reject", "finite_impurity_only_reject"):
        if gate.get(key) is not True:
            out.append(key)
    if gate.get("synthetic_controls_are_native_evidence") is not False:
        out.append("control-scope")
    denied = (
        "actual_native_s_identified", "actual_native_denominator_serialized",
        "actual_native_denominator_nonnegative", "actual_native_base_floor_r0_identified",
        "actual_native_target_b_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        out.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("conditional ordinary-boundary-triple", "complete spectator-Fock", "r0=-s", "No native s"):
        if token not in ceiling:
            out.append(f"ceiling:{token}")
    return out


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["ordinary_boundary_triple_theorem"]
    controls = data["exact_controls"]
    rows = controls["rows"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("sign convention is explicit", "D_W(lambda)=W-M(lambda)" in theorem["sign_convention"]),
        ("primary theorem basis is named", "Theorem A.7(i)" in theorem["theorem_basis"]),
        ("real-level scalar shift is explicit", "A-lambda I" in theorem["scalar_shift"]),
        ("symmetric semibound premise is explicit", "semibounded below" in theorem["symmetric_operator_premise"]),
        ("Friedrichs reference is explicit", "Friedrichs extension" in theorem["reference_premise"]),
        ("reference resolvent premise is explicit", "rho(A_F)" in theorem["reference_premise"]),
        ("bounded Weyl value is explicit", "M(lambda) is bounded" in theorem["boundary_space_premise"]),
        ("complete boundary space is required", "full spectator-Fock" in theorem["boundary_space_premise"]),
        ("floor equivalence is exact", theorem["equivalence"] == "A_W>=lambda iff D_W(lambda)>=0"),
        ("non-strict kernel boundary is admitted", "strict positivity is not required" in theorem["kernel_boundary"]),
        ("common free form is not required", not theorem["common_free_form_domain_required"]),
        ("finite impurity is insufficient", not theorem["finite_impurity_denominator_sufficient"]),
        ("three controls are present", len(rows) == 3),
        ("two controls accept", controls["accepted_rows"] == 2),
        ("one control rejects", controls["rejected_rows"] == 1),
        ("zero margin accepts", rows[1]["denominator_margin"] == "0" and rows[1]["certificate_accepts"]),
        ("negative margin rejects", rows[2]["denominator_margin"] == "-1/8" and not rows[2]["certificate_accepts"]),
        ("K656 target is composed", rows[0]["k656_target_b"] == "-7"),
        ("native floor remains absent", not data["decision"]["native_floor_supplied"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("break-equivalence", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("equivalence", "false")),
        ("erase-basis", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("theorem_basis", "unknown")),
        ("erase-shift", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("scalar_shift", "unknown")),
        ("erase-friedrichs", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("reference_premise", "self-adjoint reference")),
        ("erase-bounded-weyl", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("boundary_space_premise", "full spectator-Fock boundary space")),
        ("require-free-form", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("common_free_form_domain_required", True)),
        ("accept-impurity", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("finite_impurity_denominator_sufficient", True)),
        ("infer-sign", lambda d: d["ordinary_boundary_triple_theorem"].__setitem__("native_sign_convention_may_be_inferred", True)),
        ("allow-missing", lambda d: d["fail_closed_admission"].__setitem__("missing_any_field_rejects", False)),
        ("allow-samples", lambda d: d["fail_closed_admission"].__setitem__("pointwise_sector_samples_reject", False)),
        ("allow-impurity", lambda d: d["fail_closed_admission"].__setitem__("finite_impurity_only_reject", False)),
        ("promote-control", lambda d: d["fail_closed_admission"].__setitem__("synthetic_controls_are_native_evidence", True)),
        ("invent-s", lambda d: d["native_interface_status"].__setitem__("actual_native_s_identified", True)),
        ("invent-denominator", lambda d: d["native_interface_status"].__setitem__("actual_native_denominator_serialized", True)),
        ("invent-positive", lambda d: d["native_interface_status"].__setitem__("actual_native_denominator_nonnegative", True)),
        ("invent-r0", lambda d: d["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True)),
        ("invent-b", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-k473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-k152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "Native positivity proved.")),
    )
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    manifest_failures = failures(data)
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K657 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
