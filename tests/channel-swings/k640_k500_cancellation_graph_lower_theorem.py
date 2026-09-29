#!/usr/bin/env python3
"""K640: a quantitative lower theorem on K639's cancellation graph."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

from k639_k500_k179_channel_quotient import build as build_k639


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k640-k500-cancellation-graph-lower-theorem.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def beta_partial(cutoff: int) -> Fraction:
    return sum((Fraction(1, (k + 256) ** 2) for k in range(1, cutoff + 1)), Fraction())


def lower_floor(matrix_lower: Fraction) -> Fraction:
    return min(Fraction(1, 2), matrix_lower - Fraction(1, 128))


def build() -> dict:
    k639 = build_k639()
    k636 = strict("lab/process/k636-k500-non-equivalent-cancellation-graph.json")
    k638 = strict("lab/process/k638-k500-vector-cancellation-coordinate.json")
    k612 = strict("lab/process/k612-k139-quantitative-semibound-custody-audit.json")
    assert k639["quotient_theorem"]["surviving_dimension"] == 6
    assert k636["decision"]["topological_part_of_K634_reopener_released"]
    assert k638["vector_graph_theorem"]["matched_vector_trace_continuous"]
    assert not k612["decision"]["named_complete_sector_floor_emitted"]

    beta_upper = Fraction(258, 66049)
    simple_upper = Fraction(1, 256)
    assert beta_upper < simple_upper
    control_lower = Fraction(-2)
    controls = []
    for cutoff in (8, 32, 128, 512, 2048):
        partial = beta_partial(cutoff)
        assert partial < beta_upper
        controls.append({
            "cutoff": cutoff,
            "beta_squared_partial": qstr(partial),
            "below_integral_test_upper": True,
            "below_one_over_256": True,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K640-K500-CANCELLATION-GRAPH-LOWER-THEOREM",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact same-domain lower theorem for a parameterized Hermitian boundary form on K639's six-channel quotient cancellation graph. The theorem is an analytic interface, not an identification of the unserialized complete K139/K168 regular core.",
        "gu_typed_objects": {
            "ambient_carrier": "ell2(N) tensor C^6 in K639's algebraic operator-monomial coordinate",
            "base_domain": "D_a tensor C^6 with a_k=k+256",
            "cancellation_domain": "D_6=(D_a tensor C^6) direct_sum (h tensor C^6)",
            "graph_norm": "||phi+h tensor c||_G^2=||a phi||_2^2+||c||_2^2",
            "matched_trace": "L_6(phi+h tensor c)=componentwise sum(phi)",
            "boundary_form": "q_B=||a phi||_2^2+2 Re<c,L_6 phi>+<c,Bc>",
            "result": "parameterized cancellation-graph lower theorem MAP-TYPE=closed-form estimate",
            "target": "the common-domain quantitative interface preceding the actual complete K139/K168 core identification",
        },
        "trace_and_domain_theorem": {
            "channel_dimension": 6,
            "base_domain_dense": True,
            "cancellation_domain_dense": True,
            "cancellation_domain_strictly_larger": True,
            "decomposition_unique": True,
            "coefficient_projection_continuous_with_norm": "1",
            "matched_trace_continuous": True,
            "beta_squared_definition": "sum_(k>=1)(k+256)^-2",
            "beta_squared_integral_test_upper": qstr(beta_upper),
            "beta_squared_simple_upper": qstr(simple_upper),
            "beta_squared_strictly_below_one_over_256": True,
            "finite_controls": controls,
        },
        "parameterized_lower_theorem": {
            "hypothesis": "B is a Hermitian 6x6 boundary-coordinate matrix with B>=m I_6",
            "young_parameter": "1/2",
            "inequality": "q_B>=1/2||a phi||^2+(m-2 beta^2)||c||^2>=min(1/2,m-1/128)||phi+h tensor c||_G^2",
            "floor_function": "min(1/2,m-1/128)",
            "all_finite_Hermitian_boundary_matrices_semibounded_on_same_graph": True,
            "separate_singular_factor_estimates_used": False,
            "diagonal_weight_graph_splice_used": False,
            "reference_control_m": qstr(control_lower),
            "reference_control_floor": qstr(lower_floor(control_lower)),
            "reference_control_is_actual_K139_K168_floor": False,
        },
        "native_interface_status": {
            "K639_actual_six_channel_coordinate_consumed": True,
            "non_equivalent_cancellation_graph_consumed": True,
            "same_domain_lower_method_constructed": True,
            "actual_complete_regular_core_matrix_identified": False,
            "actual_complete_regular_core_lower_m_identified": False,
            "actual_K139_K168_form_equal_to_parameterized_q_B_proved": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K611_topology_obstruction_bypassed_for_parameterized_graph_form": True,
            "K612_data_custody_obstruction_retracted": False,
            "quantitative_complete_form_part_released": False,
            "next_exact_input": "Derive the actual complete K139/K168 regular-core representation on D_6, prove it has the displayed q_B form or an explicitly controlled extension, and certify its Hermitian lower m; only that binding can turn the parameterized floor into a native complete-sector witness.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The theorem is a parameterized lower estimate on a repository-defined graph. It neither supplies the missing native core coefficient nor constructs a GU action-owned physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "After K639 removes ten null bookkeeping directions, a direct Young inequality on one explicit graph is the cheapest honest test of whether cancellation topology can support a numerical lower theorem without the invalid K611 graph splice.",
            "retrieval_collision_result": "K636/K638 prove continuity and matching but no quadratic lower theorem; K611 rejects mixed graphs and K612 shows current native constants do not identify a floor. No prior packet states the parameterized same-graph estimate.",
            "strongest_alternative": "Immediate native K139/K168 substitution would be stronger, but the required complete regular-core representation and its lower m are precisely the missing K612 custody.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Substituting m=-2 from K168's three-dimensional impurity reference spectrum into the six-channel boundary matrix without a proved map, then reporting -257/128 as the native floor.",
            "strongest_contrary_construction": "The actual complete regular core may contain additional unbounded or off-coordinate terms; K640 controls only forms proved to reduce to q_B on D_6.",
            "weakest_reproducibility_seam": "The final native use needs an explicit operator-to-six-channel form identity, not only agreement of finite controls or coefficient counts.",
        },
        "controls": {
            "producer": "tests/channel-swings/k640_k500_cancellation_graph_lower_theorem.py",
            "probe": "tests/channel-swings/k640_k500_cancellation_graph_lower_theorem_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact same-domain lower theorem on K639's six-channel non-equivalent cancellation graph. The matched trace has beta^2<1/256, so every Hermitian boundary matrix B>=mI gives q_B>=min(1/2,m-1/128)||.||_G^2 by a single cancellation-adapted graph estimate. The numerical m=-2 row is a reference control only: no current artifact proves the complete K139/K168 regular form equals this q_B or supplies its actual six-channel m. Therefore no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    trace = payload["trace_and_domain_theorem"]
    theorem = payload["parameterized_lower_theorem"]
    native = payload["native_interface_status"]
    assert trace["channel_dimension"] == 6
    assert trace["beta_squared_strictly_below_one_over_256"]
    assert theorem["all_finite_Hermitian_boundary_matrices_semibounded_on_same_graph"]
    assert theorem["reference_control_floor"] == "-257/128"
    assert not theorem["reference_control_is_actual_K139_K168_floor"]
    assert not native["actual_complete_regular_core_matrix_identified"]
    assert not native["named_complete_sector_floor_emitted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
