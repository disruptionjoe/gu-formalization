#!/usr/bin/env python3
"""K447 exact Galerkin-defect census on the K163 one-to-two-cell control."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def _load_k163():
    path = HERE / "k163_galerkin_regular_pullback_commutation_obstruction.py"
    spec = importlib.util.spec_from_file_location("k447_k163", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K163 = _load_k163()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def exact_rank(matrix) -> int:
    work = [row[:] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        pivot_value = work[row][column]
        work[row] = [entry / pivot_value for entry in work[row]]
        for i in range(row + 1, len(work)):
            if work[i][column]:
                factor = work[i][column]
                work[i] = [left - factor * right for left, right in zip(work[i], work[row], strict=True)]
        row += 1
    return row


def rational_ldl_inertia(matrix) -> tuple[int, int, int]:
    rational = []
    for row in matrix:
        if any(entry.b for entry in row):
            raise AssertionError("the physical refinement defect must descend from Q(sqrt(2)) to Q")
        rational.append([entry.a for entry in row])
    size = len(rational)
    lower = [[Fraction(i == j) for j in range(size)] for i in range(size)]
    diagonal: list[Fraction] = []
    for i in range(size):
        pivot = rational[i][i] - sum(lower[i][k] ** 2 * diagonal[k] for k in range(i))
        if pivot == 0:
            raise AssertionError("zero-free exact LDL pivot order expected")
        diagonal.append(pivot)
        for j in range(i + 1, size):
            lower[j][i] = (
                rational[j][i]
                - sum(lower[j][k] * lower[i][k] * diagonal[k] for k in range(i))
            ) / pivot
    return sum(v > 0 for v in diagonal), sum(v < 0 for v in diagonal), 0


def defect(charge: tuple[int, int], field: str):
    root_two = K163.Q2(Fraction(0), Fraction(1))
    coarse = K163.regular_pullback([2], [root_two], charge, 4)
    fine = K163.regular_pullback([1, 3], [1, 1], charge, 4)
    _, _, injection = K163.local_refinement(charge)
    coarse_form = K163.unnormalized_form(coarse, field, root_two)
    fine_form = K163.unnormalized_form(fine, field, K163.Q2.of(1))
    return K163.add(K163.congruence(fine_form, injection), K163.scale(-1, coarse_form))


def packet(charge: tuple[int, int]) -> dict:
    raw = defect(charge, "raw")
    regular = defect(charge, "regular")
    size = len(raw)
    raw_diagonal = [raw[i][i].exact() for i in range(size)]
    return {
        "charge": list(charge),
        "coarse_dimension": size,
        "raw_defect": {
            "rank": exact_rank(raw),
            "support_count": sum(bool(entry) for row in raw for entry in row),
            "diagonal": raw_diagonal,
            "inertia_positive_negative_zero": list(rational_ldl_inertia(raw)),
        },
        "regular_defect": {
            "rank": exact_rank(regular),
            "support_count": sum(bool(entry) for row in regular for entry in row),
            "diagonal_support_count": sum(bool(regular[i][i]) for i in range(size)),
            "inertia_positive_negative_zero": list(rational_ldl_inertia(regular)),
            "entries_are_rational": all(not entry.b for row in regular for entry in row),
        },
    }


def demo() -> dict:
    sectors = [packet(charge) for charge in ((0, 0), (1, 0), (0, 1))]
    return {
        "schema_version": "1.0",
        "result_id": "K447-K152-CHARGE-SECTOR-GALERKIN-DEFECT-CENSUS",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "refinement": "one width-two cell to its width-one children with exact point-coupling scaling",
        "sectors": sectors,
        "decision": {
            "raw_defect_full_rank_in_every_sector": all(row["raw_defect"]["rank"] == row["coarse_dimension"] for row in sectors),
            "regular_defect_full_rank_in_every_sector": all(row["regular_defect"]["rank"] == row["coarse_dimension"] for row in sectors),
            "q10_q01_signatures_match": all(
                sectors[1][family][field] == sectors[2][family][field]
                for family in ("raw_defect", "regular_defect")
                for field in ("rank", "support_count", "inertia_positive_negative_zero")
            ),
            "finite_control_is_limiting_native_form": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
