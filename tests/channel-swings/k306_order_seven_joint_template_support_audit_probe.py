#!/usr/bin/env python3
"""Independent replay and hostile controls for K306."""

from __future__ import annotations

import importlib.util
import json
import sys
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("k306_order_seven_joint_template_support_audit.py")
MANIFEST = ROOT / "lab/process/k306-order-seven-joint-template-support-audit.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k306_probe_target", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K306 module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    fresh = module.build()
    support = stored["support_preservation"]
    numerical = stored["numerical_closure_audit"]
    checks = {
        "fresh_replay": fresh == stored,
        "one_gap_cover": stored["fixed_control"]["one_gap_faces"] == 6,
        "codim_two_cover": stored["fixed_control"]["codimension_two_faces"] == 15,
        "endpoint_cover": stored["fixed_control"]["endpoint_rows"] == 3,
        "master_count": stored["fixed_control"]["master_functionals"] == 72,
        "one_gap_valuation": support["one_gap_native_plus_cauchy_valuation"] == [2],
        "face_margin": support["worst_projective_second_derivative_margin"] == 1,
        "endpoint_margin": support["worst_endpoint_second_derivative_margin"] == 2,
        "finiteness": support["qualitative_global_remainder_finite"],
        "numerical_boundary_honest": not numerical["radial_integrability_numerically_certified"],
        "gamma_not_released": not stored["decision"]["k294_gamma_join_released"],
        "subtraction_not_promoted": not stored["decision"]["analytic_subtraction_promoted"],
    }
    def rejected(change) -> bool:
        candidate = deepcopy(stored)
        change(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            return True
        return False

    hostile = {
        "lost_common_zero_rejected": rejected(lambda p: p["support_preservation"].__setitem__("one_gap_native_plus_cauchy_valuation", [1])),
        "lost_endpoint_margin_rejected": rejected(lambda p: p["support_preservation"].__setitem__("worst_endpoint_second_derivative_margin", 0)),
        "premature_gamma_rejected": rejected(lambda p: p["decision"].__setitem__("k294_gamma_join_released", True)),
        "lost_finiteness_rejected": rejected(lambda p: p["support_preservation"].__setitem__("qualitative_global_remainder_finite", False)),
        "numerical_overclaim_rejected": rejected(lambda p: p["decision"].__setitem__("complete_numerical_norms_emitted", True)),
        "subtraction_promotion_rejected": rejected(lambda p: p["decision"].__setitem__("analytic_subtraction_promoted", True)),
        "k152_overclaim_rejected": rejected(lambda p: p["release_test"].__setitem__("native_K152_interval_emitted", True)),
    }
    if not all(checks.values()) or not all(hostile.values()):
        raise AssertionError({"checks": checks, "hostile": hostile})
    print(f"K306 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
