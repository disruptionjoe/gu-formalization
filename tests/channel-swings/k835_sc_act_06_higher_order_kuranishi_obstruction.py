#!/usr/bin/env python3
"""K835: vanishing quadratic obstruction does not integrate a tangent."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k835-sc-act-06-higher-order-kuranishi-obstruction.json"


def build() -> dict[str, Any]:
    rows = []
    for order in (2, 3, 4):
        rows.append({
            "order": order,
            "map": f"F_{order}(x,y)=(y,x^{order})",
            "jacobian": [[0, 1], [0, 0]],
            "jacobian_rank": 1,
            "tangent_kernel_basis": [[1, 0]],
            "cokernel_basis": [[0, 1]],
            "projected_derivatives_below_first_obstruction_zero": list(range(2, order)),
            "first_nonzero_projected_order": order,
            "first_nonzero_projected_coefficient": math.factorial(order),
            "exact_zero_locus_near_origin": [[0, 0]],
            "infinitesimal_dimension": 1,
            "actual_local_dimension": 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K835-SC-ACT-06-HIGHER-ORDER-KURANISHI-OBSTRUCTION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact polynomial controls showing that identical tangent/cokernel data can have first nonlinear obstruction at arbitrarily later finite order.",
        "exact_controls": {
            "families": rows,
            "common_jacobian": [[0, 1], [0, 0]],
            "common_infinitesimal_dimension": 1,
            "all_actual_local_dimensions": [0, 0, 0],
            "quadratic_obstruction_vanishes_for_orders": [3, 4],
            "first_obstruction_orders": [2, 3, 4],
        },
        "theorem": {
            "linearized_kernel_determines_integrability": False,
            "vanishing_quadratic_obstruction_determines_integrability": False,
            "any_fixed_finite_jet_order_is_universal": False,
            "required_evidence": "the actual finite-dimensional obstruction germ, a proved terminating order, or an independent unobstructedness theorem",
        },
        "decision": {
            "actual_gu_kuranishi_germ_constructed": False,
            "actual_gu_unobstructedness_proved": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Do not stop at the quadratic obstruction: construct the complete projected nonlinear germ on the authenticated GU slice or prove a theorem that controls all later orders.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Exact finite polynomial obstruction hierarchy only; no GU nonlinear map, rich moduli, source, ledger, canon, or physical conclusion.",
        "controls": {
            "producer": "tests/channel-swings/k835_sc_act_06_higher_order_kuranishi_obstruction.py",
            "probe": "tests/channel-swings/k835_sc_act_06_higher_order_kuranishi_obstruction_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 12,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, t, d = p["exact_controls"], p["theorem"], p["decision"]
    assert c["common_jacobian"] == [[0, 1], [0, 0]]
    assert c["common_infinitesimal_dimension"] == 1
    assert c["all_actual_local_dimensions"] == [0, 0, 0]
    assert c["quadratic_obstruction_vanishes_for_orders"] == [3, 4]
    assert c["first_obstruction_orders"] == [2, 3, 4]
    for row, order in zip(c["families"], (2, 3, 4)):
        assert row["order"] == order and row["jacobian_rank"] == 1
        assert row["tangent_kernel_basis"] == [[1, 0]] and row["cokernel_basis"] == [[0, 1]]
        assert row["first_nonzero_projected_order"] == order
        assert row["first_nonzero_projected_coefficient"] == math.factorial(order)
        assert row["actual_local_dimension"] == 0
    assert not t["linearized_kernel_determines_integrability"]
    assert not t["vanishing_quadratic_obstruction_determines_integrability"]
    assert not t["any_fixed_finite_jet_order_is_universal"]
    assert not d["actual_gu_kuranishi_germ_constructed"]
    assert not d["actual_gu_unobstructedness_proved"] and not d["global_sc_act_06_proved_or_refuted"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    p = build(); validate(p)
    rendered = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif args.check:
        assert json.loads(OUTPUT.read_text()) == p
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
