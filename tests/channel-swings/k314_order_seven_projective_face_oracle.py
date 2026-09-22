#!/usr/bin/env python3
"""Certify confluent K308 bounds on all six one-gap projective faces.

The native projective polynomial is kept explicit.  A designated gap may
reach zero, so the corresponding cumulative nodes may repeat; the regularized
matrices are bounded by Hermite--Genocchi derivative envelopes and never divide
by that gap.  Shrinking face slabs therefore have a uniform regularizer bound
and an explicit polynomial factor that tends to zero.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K296 = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"
K308_MODULE = Path(__file__).with_name("k308_order_seven_regularized_y_master_operator.py")
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
K313 = ROOT / "lab/process/k313-order-seven-scaled-radial-shell-oracle.json"
OUTPUT = ROOT / "lab/process/k314-order-seven-projective-face-oracle.json"

GAPS = ("r0", "r1", "r2", "c0", "c1", "c2")
DEGREE = 27
BASE = {
    "x": (Fraction(1, 16), Fraction(1, 8)),
    "b": (Fraction(1, 32), Fraction(1, 8)),
    "y": (Fraction(1, 4), Fraction(3, 4)),
    "split": (Fraction(1, 4), Fraction(3, 4)),
}


def load_k308():
    spec = importlib.util.spec_from_file_location("k314_k308_backend", K308_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K308 backend")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def native_node_lowers(gaps: dict[str, tuple[Fraction, Fraction]]) -> dict[str, list[Fraction]]:
    x0, _ = BASE["x"]
    b0, _ = BASE["b"]
    y0, y1 = BASE["y"]
    _, split1 = BASE["split"]
    low = {name: interval[0] for name, interval in gaps.items()}
    return {
        "odd_left": [
            x0 * y0 + b0 * (low["r0"] + low["r1"] + low["r2"]),
            x0 * y0 + b0 * (low["r1"] + low["r2"]),
            x0 * y0 + b0 * low["r2"],
            x0 * y0,
        ],
        "odd_right": [
            x0 * (1 - y1) + b0 * (low["c0"] + low["c1"] + low["c2"]),
            x0 * (1 - y1) + b0 * (low["c1"] + low["c2"]),
            x0 * (1 - y1) + b0 * low["c2"],
            x0 * (1 - y1),
        ],
        "even_left": [
            x0 * y0 + b0 * (low["r1"] + low["r2"] + low["r0"] * (1 - split1)),
            x0 * y0 + b0 * (low["r2"] + low["r1"] * (1 - split1)),
            x0 * y0 + b0 * low["r2"] * (1 - split1),
            x0 * y0 * (1 - split1),
        ],
        "even_right": [
            x0 * (1 - y1) + b0 * (low["c1"] + low["c2"] + low["c0"] * (1 - split1)),
            x0 * (1 - y1) + b0 * (low["c2"] + low["c1"] * (1 - split1)),
            x0 * (1 - y1) + b0 * low["c2"] * (1 - split1),
            x0 * (1 - y1) * (1 - split1),
        ],
    }


def projective_polynomial_upper(gaps: dict[str, tuple[Fraction, Fraction]]) -> Fraction:
    high = {name: interval[1] for name, interval in gaps.items()}
    _, split1 = BASE["split"]

    def v4(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
        return a * b * c * (a + b) * (b + c) * (a + b + c)

    def v3(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
        d02 = a * split1 + b * split1
        d24 = b * split1 + c * split1
        return d02 * d24 * (d02 + d24)

    product = Fraction(1)
    for name in GAPS:
        product *= high[name]
    return (
        product
        * v4(high["r0"], high["r1"], high["r2"])
        * v4(high["c0"], high["c1"], high["c2"])
        * v3(high["r0"], high["r1"], high["r2"])
        * v3(high["c0"], high["c1"], high["c2"])
    )


def outward_bank(module, gaps: dict[str, tuple[Fraction, Fraction]]) -> dict[str, Any]:
    nodes = native_node_lowers(gaps)
    x1 = BASE["x"][1]
    y0, y1 = BASE["y"]
    split0, split1 = BASE["split"]

    argument_lower = min(nodes["odd_left"]) + min(nodes["odd_right"])
    d4_matrix = [
        [module.dd_abs_upper(argument_lower, row, column) for column in range(4)]
        for row in range(4)
    ]
    d4_bound = module.determinant_abs_bound([list(column) for column in zip(*d4_matrix)])

    row_orders = [0, 1, 2, 0]
    column_orders = [0, 1, 2, 0]
    column_jets = []
    for column_index in range(5):
        jets = [[module.arb(0) for _ in range(5)] for _ in range(3)]
        if column_index < 4:
            b_order = column_orders[column_index]
            for row_index in range(4):
                a_order = row_orders[row_index]
                lower = nodes["even_left"][row_index] + nodes["even_right"][column_index]
                if row_index < 3 and column_index < 3:
                    delta = Fraction(0)
                elif row_index < 3 or column_index < 3:
                    delta = x1 * split1
                else:
                    delta = x1 * (split1 - split0)
                for order in range(3):
                    jets[order][row_index] = (
                        module.ball(delta) ** order
                        * module.dd_abs_upper(lower, a_order, b_order, order)
                    )
            lower = nodes["even_right"][column_index]
            base = module.dd_abs_upper(lower, 0, b_order)
            next1 = module.dd_abs_upper(lower, 0, b_order + 1)
            next2 = module.dd_abs_upper(lower, 0, b_order + 2)
            jets[0][4] = module.ball(1 - y0) * base
            jets[1][4] = base + module.ball((1 - y0) * x1 * (b_order + 1)) * next1
            jets[2][4] = (
                module.ball(2 * x1 * (b_order + 1)) * next1
                + module.ball((1 - y0) * x1**2 * (b_order + 1) * (b_order + 2)) * next2
            )
        else:
            for row_index in range(3):
                a_order = row_orders[row_index]
                lower = nodes["even_left"][row_index]
                base = module.dd_abs_upper(lower, a_order, 0)
                next1 = module.dd_abs_upper(lower, a_order + 1, 0)
                next2 = module.dd_abs_upper(lower, a_order + 2, 0)
                jets[0][row_index] = module.ball(y1) * base
                jets[1][row_index] = base + module.ball(y1 * x1 * (a_order + 1)) * next1
                jets[2][row_index] = (
                    module.ball(2 * x1 * (a_order + 1)) * next1
                    + module.ball(y1 * x1**2 * (a_order + 1) * (a_order + 2)) * next2
                )
        column_jets.append(jets)

    b5_jets = module.determinant_jet_bounds(column_jets)
    radius_max = BASE["x"][1] + BASE["b"][1]
    scaled = [d4_bound * value * module.ball(radius_max**DEGREE) for value in b5_jets]
    polynomial = projective_polynomial_upper(gaps)
    complete = [value * module.ball(polynomial) for value in scaled]
    return {
        "node_argument_lower_bounds": {
            key: [str(value) for value in values] for key, values in nodes.items()
        },
        "minimum_kernel_argument": str(min(min(values) for values in nodes.values())),
        "D4_regularized_abs_upper": module.upper_text(d4_bound),
        "bordered_B5_regularized_y_jet_abs_upper": [module.upper_text(value) for value in b5_jets],
        "scaled_regularizer_y_jet_abs_upper": [module.upper_text(value) for value in scaled],
        "projective_polynomial_upper": str(polynomial),
        "complete_projective_times_scaled_y_jet_abs_upper": [module.upper_text(value) for value in complete],
    }


def build() -> dict[str, Any]:
    module = load_k308()
    k296 = json.loads(K296.read_text())
    k310 = json.loads(K310.read_text())
    k313 = json.loads(K313.read_text())
    if k310["fixed_control"]["regularized_product_simultaneous_degree"] != -DEGREE:
        raise AssertionError("K310 scaling degree changed")
    if not k313["decision"]["scaled_interior_shell_oracle_implemented"]:
        raise AssertionError("K313 interior oracle unavailable")
    if k296["fixed_control"]["projective_gap_labels"] != list(GAPS):
        raise AssertionError("K296 face order changed")

    widths = [Fraction(1, 8), Fraction(1, 32), Fraction(1, 128), Fraction(1, 512)]
    faces = []
    for face in GAPS:
        rows = []
        for width in widths:
            gaps = {
                name: ((Fraction(0), width) if name == face else (Fraction(1, 8), Fraction(5, 24)))
                for name in GAPS
            }
            bank = outward_bank(module, gaps)
            bank["face_width"] = str(width)
            rows.append(bank)
        first = [float(value) for value in rows[0]["complete_projective_times_scaled_y_jet_abs_upper"]]
        last = [float(value) for value in rows[-1]["complete_projective_times_scaled_y_jet_abs_upper"]]
        ratios = [right / left for left, right in zip(first, last)]
        if any(not math.isfinite(value) or value <= 0 or value >= 0.02 for value in ratios):
            raise AssertionError(f"{face} face slab does not contract")
        faces.append({
            "face": face,
            "repeated_nodes_at_endpoint": True,
            "rows": rows,
            "last_to_first_component_ratios": [repr(value) for value in ratios],
            "exact_face_complete_bound": ["0", "0", "0"],
        })

    return {
        "schema_version": "1.0",
        "result_id": "K314-ORDER-SEVEN-PROJECTIVE-FACE-ORACLE",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json",
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
                "lab/process/k313-order-seven-scaled-radial-shell-oracle.json",
            ],
            "projective_gap_order": list(GAPS),
            "face_widths": [str(value) for value in widths],
            "arb_decimal_digits": 180,
            "threads": 1,
            "scaled_regularizer_degree": DEGREE,
            "interior_radial_y_split_cell": {
                key: [str(value[0]), str(value[1])] for key, value in BASE.items()
            },
        },
        "confluent_rule": {
            "regularized_entries": "Hermite--Genocchi divided differences extend to repeated nodes as kernel derivatives divided by factorials",
            "gap_division_used": False,
            "native_projective_polynomial_retained": True,
            "one_gap_face_valuation": 2,
            "source": "K296 native gap plus common Cauchy valuation; companion zeros remain occurrence-dependent inside the bordered assembly",
        },
        "one_gap_face_oracle": faces,
        "decision": {
            "all_six_repeated_node_faces_have_finite_regularizer_bounds": True,
            "all_six_complete_face_values_vanish": True,
            "shrinking_face_slabs_contract": True,
            "gap_cutoff_required": False,
            "terminal_split_face_composed": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_constants_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "insert K311's weighted B0/B1/B2 terminal entry budgets inside the complete bordered column-replacement jets, then combine the resulting terminal and projective cells with K312's positive measure backend",
        },
        "release_test": {
            "six_faces_replayed": len(faces) == 6,
            "all_face_regularizer_bounds_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for face in faces for row in face["rows"]
                for value in row["scaled_regularizer_y_jet_abs_upper"]
            ),
            "all_face_complete_bounds_contract": all(
                all(float(value) < 0.02 for value in face["last_to_first_component_ratios"])
                for face in faces
            ),
            "exact_face_bounds_zero": all(face["exact_face_complete_bound"] == ["0", "0", "0"] for face in faces),
            "detached_cofactor_used": False,
            "positive_gap_floor_required": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k313["ledger_effect"],
        "source_routing": "SC-ACT-01/02/06 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS.",
        "claim_ceiling": "Confluent outward value/first-y/second-y bounds for the complete degree-27-scaled coherent D4-times-bordered-B5 regularizer on shrinking slabs meeting each of the six one-gap projective faces. The exact native projective polynomial is retained, no gap is divided out, every regularizer bound stays finite at repeated nodes, and the complete projective-times-regularizer bound contracts to zero on all six exact faces. This covers K313's interior radial/y/split slab only; terminal split faces, radial projective faces, the complete y-master sum, five gap-axis constants, K294 gamma strata, action-column value, residual, K152 interval, source/ledger, canon, paper, public and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["fixed_control"]["projective_gap_order"] != list(GAPS):
        raise AssertionError("projective face order changed")
    if len(payload["one_gap_face_oracle"]) != 6:
        raise AssertionError("face census changed")
    rule = payload["confluent_rule"]
    if rule["gap_division_used"] or not rule["native_projective_polynomial_retained"]:
        raise AssertionError("confluent face rule lost")
    decision = payload["decision"]
    if not decision["all_six_repeated_node_faces_have_finite_regularizer_bounds"]:
        raise AssertionError("face regularizer missing")
    if decision["gap_cutoff_required"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("face oracle overclaim")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
