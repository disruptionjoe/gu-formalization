#!/usr/bin/env python3
"""Independent controls and hostile mutations for K419."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k419_k77_frozen_stratum_linearized_kt_complex.py")
MANIFEST = ROOT / "lab/process/k419-k77-frozen-stratum-linearized-kt-complex.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k419_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K419 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K419 = load_solver()


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K419.demo()
    bases = result["bases"]
    primal = result["primal_exact_sequence"]
    dual = result["dual_exact_sequence"]
    kt = result["linearized_kt_fixture"]
    manifest_complex = data.get("finite_complex", {})
    manifest_kt = data.get("linearized_kt_fixture", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", result["schema_version"] == "1.0" and data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data.get("direction") == "native_to_native"),
        ("gauge dimension", bases["gauge_dimension"] == 91 and manifest_complex.get("gauge_dimension") == 91),
        ("stabilizer dimension", bases["stabilizer_dimension"] == 21 and manifest_complex.get("stabilizer_dimension") == 21),
        ("orbit dimension", bases["orbit_dimension"] == 70 and manifest_complex.get("orbit_dimension") == 70),
        ("dimension split", bases["stabilizer_dimension"] + bases["orbit_dimension"] == bases["gauge_dimension"]),
        ("inclusion rank", primal["inclusion_rank"] == 21),
        ("action rank", primal["action_rank"] == 70),
        ("kernel dimension", primal["action_kernel_dimension"] == 21),
        ("action surjective", primal["action_surjective"] is True),
        ("primal composition", primal["composition_zero"] is True),
        ("Euler zero", primal["euler_characteristic"] == 0),
        ("dual inclusion", dual["dual_inclusion_rank"] == 70),
        ("relation projection", dual["relation_projection_rank"] == 21),
        ("dual kernel", dual["projection_kernel_dimension"] == 70),
        ("dual composition", dual["composition_zero"] is True),
        ("constraints", kt["constraint_generators"] == 91 and manifest_kt.get("constraint_generators") == 91),
        ("independent constraints", kt["independent_linearized_constraints"] == 70 and manifest_kt.get("independent_linearized_constraints") == 70),
        ("relations", kt["first_stage_relations"] == 21 and manifest_kt.get("first_stage_relations") == 21),
        ("finite exact", kt["finite_complex_exact"] is True and manifest_kt.get("finite_complex_exact") is True),
        ("nonlinear fence", boundaries.get("nonlinear_kt_properness_proved") is False),
        ("functional fence", boundaries.get("functional_bfv_or_common_domain_constructed") is False),
        ("ledger fence", boundaries.get("source_ledger_canon_paper_public_or_physical_effect") is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    baseline = checks(data)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K419 controls")
        return 0
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "observed_to_native"),
        lambda d: d["finite_complex"].__setitem__("gauge_dimension", 90),
        lambda d: d["finite_complex"].__setitem__("stabilizer_dimension", 20),
        lambda d: d["finite_complex"].__setitem__("orbit_dimension", 71),
        lambda d: d["linearized_kt_fixture"].__setitem__("constraint_generators", 70),
        lambda d: d["linearized_kt_fixture"].__setitem__("independent_linearized_constraints", 91),
        lambda d: d["linearized_kt_fixture"].__setitem__("first_stage_relations", 0),
        lambda d: d["linearized_kt_fixture"].__setitem__("finite_complex_exact", False),
        lambda d: d["boundaries"].__setitem__("nonlinear_kt_properness_proved", True),
        lambda d: d["boundaries"].__setitem__("functional_bfv_or_common_domain_constructed", True),
        lambda d: d["boundaries"].__setitem__("source_ledger_canon_paper_public_or_physical_effect", True),
    ]
    caught = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        caught += int(any(not ok for _, ok in checks(trial)))
    if caught != len(mutations):
        print(f"FAIL hostile selftest caught {caught}/{len(mutations)}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
