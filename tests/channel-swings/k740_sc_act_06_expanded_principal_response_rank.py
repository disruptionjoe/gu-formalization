#!/usr/bin/env python3
"""K740: exact expanded-parent derivative-only principal response ranks.

The map is the K77 first-order connection response

    J_q(u) = Shiab(q wedge u),

followed by the already-certified real K-lift.  The K-lift is an invertible
coordinate identification of the degree-13 equation carrier, so it preserves
rank.  Every computation is over exact rational coefficients in the pinned
real u(64,64) basis.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
API_PATH = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
PATHS = {
    "api": API_PATH,
    "bank": ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json",
    "k737": ROOT / "lab/process/k737-sc-act-06-expanded-parent-dimension-threshold.json",
    "k739": ROOT / "lab/process/k739-sc-act-06-expanded-action-parent-ownership.json",
}
OUTPUT = ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json"
SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}


def load_api():
    spec = importlib.util.spec_from_file_location("k740_k77_api", API_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compute_case(api, core, q_form: dict[int, dict[int, tuple[Fraction, Fraction]]]) -> dict[str, dict[str, int]]:
    def factor(mask: int):
        return api.ONE if mask.bit_count() in SKEW_GRADES else api.I

    def direction(form_index: int, mask: int):
        return {1 << form_index: {mask: factor(mask)}}

    def gdiv(left, right):
        denominator = right[0] * right[0] + right[1] * right[1]
        if not denominator:
            raise ZeroDivisionError(right)
        return (
            (left[0] * right[0] + left[1] * right[1]) / denominator,
            (left[1] * right[0] - left[0] * right[1]) / denominator,
        )

    def k_lift(equation):
        out: dict[tuple[int, int], Fraction] = {}
        for equation_form, element in equation.items():
            receiver_form = core.full ^ equation_form
            if receiver_form.bit_count() != 1:
                continue
            form_index = receiver_form.bit_length() - 1
            for mask in element:
                test = direction(form_index, mask)
                coefficient = gdiv(core.pair(test, equation), core.pair(test, core.hodge(test)))
                if coefficient[1] != 0:
                    raise AssertionError("K-lift left the pinned real basis")
                if coefficient[0]:
                    out[(form_index, mask)] = coefficient[0]
        return out

    def reduce_column(value: dict[tuple[int, int], Fraction], pivots: dict[tuple[int, int], dict[tuple[int, int], Fraction]]):
        value = dict(value)
        while value:
            pivot = min(value)
            if pivot not in pivots:
                lead = value[pivot]
                pivots[pivot] = {key: coefficient / lead for key, coefficient in value.items()}
                return
            lead = value[pivot]
            basis = pivots[pivot]
            for key, coefficient in basis.items():
                updated = value.get(key, Fraction(0)) - lead * coefficient
                if updated:
                    value[key] = updated
                else:
                    value.pop(key, None)

    pivots = {"selected_low_grade": {}, "grade_saturated_spin": {}, "full_connection": {}}
    zero_columns = {key: 0 for key in pivots}
    domains = {"selected_low_grade": 0, "grade_saturated_spin": 0, "full_connection": 0}
    for form_index in range(14):
        for mask in range(1 << 14):
            column = k_lift(core.shiab(core.wedge_raw(q_form, direction(form_index, mask))))
            memberships = ["full_connection"]
            if mask.bit_count() in SKEW_GRADES:
                memberships.append("grade_saturated_spin")
            if mask.bit_count() in (1, 2):
                memberships.append("selected_low_grade")
            for name in memberships:
                domains[name] += 1
                if not column:
                    zero_columns[name] += 1
                reduce_column(column, pivots[name])
    return {
        name: {
            "domain_dimension": domains[name],
            "rank": len(pivots[name]),
            "nullity": domains[name] - len(pivots[name]),
            "zero_columns": zero_columns[name],
        }
        for name in pivots
    }


def build() -> dict[str, Any]:
    api = load_api()
    bank = api.load_bank()
    core = api.K77Core(bank.signature, bank.channels)
    plus = next(i for i, sign in enumerate(bank.signature) if sign == 1)
    minus = next(i for i, sign in enumerate(bank.signature) if sign == -1)
    nonnull = {1 << plus: {0: api.ONE}}
    native_null = core.fadd(nonnull, {1 << minus: {0: api.ONE}})
    cases = []
    for name, q_norm, q_form in (
        ("native_nonnull", 1, nonnull),
        ("native_null_auxiliary_nonzero", 0, native_null),
    ):
        cases.append({"case": name, "native_q_norm_squared": q_norm, "ranks": compute_case(api, core, q_form)})
    k737 = json.loads(PATHS["k737"].read_text(encoding="utf-8"))
    requirements = k737["exact_thresholds"]
    return {
        "schema_version": "1.0",
        "result_id": "K740-SC-ACT-06-EXPANDED-PRINCIPAL-RESPONSE-RANK",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact derivative-only K77 connection-response rank on the selected low-grade, grade-saturated Spin and action-owned full connection carriers at native nonnull and native-null covectors.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "operator": {
            "principal_map": "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))",
            "zero_order_hodge_kappa_u_included": False,
            "rank_field": "Q_IN_PINNED_REAL_U64_64_BASIS",
            "k_lift_rank_preserving": True,
            "complete_basis_enumeration": True,
        },
        "exact_controls": {
            "cases": cases,
            "required_total_new_rank_nonnull": requirements["minimum_total_new_rank_nonnull"],
            "required_total_new_rank_native_null": requirements["minimum_total_new_rank_native_null"],
            "maximum_unserialized_metric_epsilon_rank": 101,
        },
        "decision": {
            "selected_low_grade_connection_rank": 650,
            "spin_connection_rank": 60594,
            "full_connection_rank": 122864,
            "spin_fails_both_required_thresholds_even_with_maximal_metric_epsilon_grant": True,
            "full_connection_clears_both_required_thresholds_without_metric_epsilon_grant": True,
            "full_connection_middle_exactness_proved": False,
            "actual_hessian_rank_proved_equal_to_response_rank": False,
            "next_exact_input": "Compose the exact response ranks with K720's two I1B symbol strata. Exclude the Spin carrier even under favorable placement; preserve the full action-owned carrier only as threshold-capable until same-background image overlap, residual pairing, gauge and redundancy maps are serialized.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The full response clears a necessary rank threshold but its residual-square Hessian rank, image placement relative to K720 and complete gauge/redundancy complex remain open.",
        "controls": {
            "producer": "tests/channel-swings/k740_sc_act_06_expanded_principal_response_rank.py",
            "probe": "tests/channel-swings/k740_sc_act_06_expanded_principal_response_rank_probe.py",
            "controls_passed": 43,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact derivative-only connection-response ranks. No residual-square Hessian equality, same-background image placement, gauge/redundancy completion, middle exactness, source-status, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    op, c, d = p["operator"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert op["principal_map"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert not op["zero_order_hodge_kappa_u_included"]
    assert op["rank_field"] == "Q_IN_PINNED_REAL_U64_64_BASIS"
    assert op["k_lift_rank_preserving"] and op["complete_basis_enumeration"]
    assert c["required_total_new_rank_nonnull"] == 98470
    assert c["required_total_new_rank_native_null"] == 106634
    assert c["maximum_unserialized_metric_epsilon_rank"] == 101
    expected = {
        "selected_low_grade": (1470, 650, 820),
        "grade_saturated_spin": (113792, 60594, 53198),
        "full_connection": (229376, 122864, 106512),
    }
    assert [row["case"] for row in c["cases"]] == ["native_nonnull", "native_null_auxiliary_nonzero"]
    assert [row["native_q_norm_squared"] for row in c["cases"]] == [1, 0]
    for case in c["cases"]:
        for name, triple in expected.items():
            row = case["ranks"][name]
            assert (row["domain_dimension"], row["rank"], row["nullity"]) == triple
            assert row["domain_dimension"] == row["rank"] + row["nullity"]
            assert 0 <= row["zero_columns"] <= row["nullity"]
    assert d["selected_low_grade_connection_rank"] == 650
    assert d["spin_connection_rank"] == 60594 and d["full_connection_rank"] == 122864
    assert d["spin_fails_both_required_thresholds_even_with_maximal_metric_epsilon_grant"]
    assert d["full_connection_clears_both_required_thresholds_without_metric_epsilon_grant"]
    assert not d["full_connection_middle_exactness_proved"] and not d["actual_hessian_rank_proved_equal_to_response_rank"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
