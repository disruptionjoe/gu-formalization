#!/usr/bin/env python3
"""K743: pairing-independent image cap for the full-carrier residual square.

Run with ``sage -python``.  The computation reuses K132's exact invariant
28/56-dimensional all-grade blocks.  If ``J`` is the complete derivative-only
residual response, every residual-square Hessian has the form ``J^T Q J`` and
therefore has image contained in ``im(J^T)`` for every pairing ``Q``.  The
rank of ``[E_I1B | J^T]`` is consequently an exact, pairing-independent upper
bound for the combined Euler image.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import math
import os
import runpy
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

try:
    from sage.all import QQ, diagonal_matrix, matrix
except ModuleNotFoundError:
    if __name__ == "__main__":
        os.execvp("sage", ["sage", "-python", *sys.argv])
    raise

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
OUTPUT = ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json"
PATHS = {
    "backend": BACKEND,
    "k132": ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
}
SELECTED = ("comm", "symi", "symi")
SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
METRIC_SLOTS = [(p, q) for p in range(4) for q in range(p, 4)]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_algebra() -> dict[str, Any]:
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        algebra = runpy.run_path(str(BACKEND))
    if "failures=0" not in capture.getvalue().lower():
        raise AssertionError("K77 exact algebra backend did not replay")
    return algebra


def sqm(value) -> Any:
    return matrix(
        QQ,
        value.rows,
        value.cols,
        {key: QQ(item.p) / QQ(item.q) for key, item in value.todok().items()},
        sparse=True,
    )


def scalar_one_form(M: dict[str, Any], covector: tuple[int, ...]) -> dict:
    return {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(covector)
        if value
    }


def direction(M: dict[str, Any], mu: int, mask: int, real_basis: bool = False) -> dict:
    coefficient = M["ONE"] if (not real_basis or mask.bit_count() in SKEW_GRADES) else M["I"]
    return {1 << mu: {mask: coefficient}}


def pairing(M: dict[str, Any], left: dict, right: dict):
    return M["wedge_raw"](left, right).get(M["FULL"], {}).get(0, M["ZERO"])


def rows_for_image(M: dict[str, Any], image: dict) -> list[tuple[int, int, tuple[Fraction, Fraction]]]:
    out = []
    for form_mask, element in image.items():
        complement = M["FULL"] ^ form_mask
        if not complement or complement & (complement - 1):
            continue
        nu = complement.bit_length() - 1
        for clifford_mask, value in element.items():
            if value == M["ZERO"]:
                continue
            coefficient = pairing(M, direction(M, nu, clifford_mask), image)
            if coefficient != M["ZERO"]:
                out.append((nu, clifford_mask, coefficient))
    return out


def raw_block(M: dict[str, Any], covector: tuple[int, ...], labels: list[int]):
    q_form = scalar_one_form(M, covector)
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(M["N"])]
    index = {(label, mu): i for i, (label, mu, _mask) in enumerate(basis)}
    entries: dict[tuple[int, int], Any] = {}
    for column, (_label, mu, mask) in enumerate(basis):
        image = M["shiab"](M["wedge_raw"](q_form, direction(M, mu, mask)), SELECTED)
        for nu, outmask, value in rows_for_image(M, image):
            row_label = outmask ^ (1 << nu)
            if (row_label, nu) not in index:
                continue
            if value[1]:
                raise AssertionError("I1B raw block left the pinned basis")
            key = (index[(row_label, nu)], column)
            entries[key] = entries.get(key, QQ(0)) + QQ(value[0].numerator) / QQ(value[0].denominator)
    raw = matrix(QQ, len(basis), len(basis), entries, sparse=True)
    return basis, raw, (raw - raw.transpose()) / 2


def form_sign(M: dict[str, Any], mask: int) -> int:
    value = 1
    for index in M["indices"](mask):
        value *= M["ETA"][index]
    return value


def response_data(M: dict[str, Any], covector: tuple[int, ...], labels: list[int]):
    """Return the complete real response matrix and full-trace diagonal signs."""
    q_form = scalar_one_form(M, covector)
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(M["N"])]
    columns: list[dict[tuple[int, int], tuple[Fraction, Fraction]]] = []
    coordinates: set[tuple[int, int]] = set()
    for _label, mu, mask in basis:
        equation = M["shiab"](
            M["wedge_raw"](q_form, direction(M, mu, mask, real_basis=True)), SELECTED
        )
        column = {
            (form_mask, clifford_mask): value
            for form_mask, element in equation.items()
            for clifford_mask, value in element.items()
            if value != M["ZERO"]
        }
        columns.append(column)
        coordinates.update(column)
    ordered = sorted(coordinates)
    phases: dict[tuple[int, int], int] = {}
    for key in ordered:
        values = [column[key] for column in columns if key in column]
        has_real = any(value[0] for value in values)
        has_imag = any(value[1] for value in values)
        if has_real == has_imag:
            raise AssertionError(f"mixed or zero real phase at {key}")
        phases[key] = 1 if has_real else -1  # square of 1 or i
    position = {key: i for i, key in enumerate(ordered)}
    entries = {}
    for column_index, column in enumerate(columns):
        for key, value in column.items():
            scalar = value[0] if phases[key] == 1 else value[1]
            entries[(position[key], column_index)] = QQ(scalar.numerator) / QQ(scalar.denominator)
    response = matrix(QQ, len(ordered), len(columns), entries, sparse=True)
    signs = [
        form_sign(M, form_mask)
        * M["blade_product"](clifford_mask, clifford_mask)[1]
        * phases[(form_mask, clifford_mask)]
        for form_mask, clifford_mask in ordered
    ]
    return basis, response, signs


def signature_mask(indices: list[int], count: int) -> int:
    return sum(1 << index for index in indices[:count])


def case_blocks(M: dict[str, Any], case: str):
    if case == "native_nonnull":
        axis = next(i for i, sign in enumerate(M["ETA"]) if sign == 1)
        covector = tuple(1 if i == axis else 0 for i in range(M["N"]))
        positive = [i for i, sign in enumerate(M["ETA"]) if sign == 1 and i != axis]
        negative = [i for i, sign in enumerate(M["ETA"]) if sign == -1 and i != axis]
        rows = []
        for a in range(len(positive) + 1):
            for b in range(len(negative) + 1):
                base = signature_mask(positive, a) | signature_mask(negative, b)
                rows.append(
                    ([base, base ^ (1 << axis)], math.comb(len(positive), a) * math.comb(len(negative), b))
                )
        return covector, (axis,), rows
    if case == "native_null_auxiliary_nonzero":
        plus = next(i for i, sign in enumerate(M["ETA"]) if sign == 1)
        minus = next(i for i, sign in enumerate(M["ETA"]) if sign == -1)
        covector = tuple(1 if i in (plus, minus) else 0 for i in range(M["N"]))
        positive = [i for i, sign in enumerate(M["ETA"]) if sign == 1 and i != plus]
        negative = [i for i, sign in enumerate(M["ETA"]) if sign == -1 and i != minus]
        rows = []
        for a in range(len(positive) + 1):
            for b in range(len(negative) + 1):
                base = signature_mask(positive, a) | signature_mask(negative, b)
                labels = [base, base ^ (1 << plus), base ^ (1 << minus), base ^ (1 << plus) ^ (1 << minus)]
                rows.append((labels, math.comb(len(positive), a) * math.comb(len(negative), b)))
        return covector, (plus, minus), rows
    raise ValueError(case)


def metric_basis_value(slot: tuple[int, int], i: int, j: int) -> int:
    p, q = slot
    return int((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_riemann(covector: tuple[int, ...], slot: tuple[int, int]):
    def tensor(i: int, j: int, a: int, b: int) -> int:
        h = lambda x, y: metric_basis_value(slot, x, y)
        k = covector
        return (
            k[i] * k[a] * h(j, b)
            - k[i] * k[b] * h(j, a)
            - k[j] * k[a] * h(i, b)
            + k[j] * k[b] * h(i, a)
        )
    return tensor


def spin_curvature_injection(M: dict[str, Any], tensor) -> dict:
    out = {}
    for i, j in combinations(range(M["N"]), 2):
        coefficient = {}
        for a, b in combinations(range(M["N"]), 2):
            value = M["ETA"][a] * M["ETA"][b] * tensor(i, j, a, b)
            if value:
                coefficient = M["eadd"](
                    coefficient,
                    M["escale"](value, M["emul"](M["blade"](a), M["blade"](b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def curvature_columns(M: dict[str, Any], covector: tuple[int, ...]):
    columns = []
    for slot in METRIC_SLOTS:
        output = M["shiab"](spin_curvature_injection(M, principal_riemann(covector, slot)), SELECTED)
        columns.append({(mask ^ (1 << nu), nu): value for nu, mask, value in rows_for_image(M, output)})
    return columns


def distortion_census(M: dict[str, Any], case: str):
    covector, _toggle_axes, blocks = case_blocks(M, case)
    totals = Counter()
    types = Counter()
    for labels, multiplicity in blocks:
        _basis, _raw, euler = raw_block(M, covector, labels)
        _basis2, response, _signs = response_data(M, covector, labels)
        image_cap = euler.augment(response.transpose()).rank()
        key = (euler.rank(), response.rank(), image_cap)
        types[key] += multiplicity
        totals["euler_rank"] += multiplicity * key[0]
        totals["response_rank"] += multiplicity * key[1]
        totals["image_cap_rank"] += multiplicity * key[2]
    return covector, totals, types


def coupled_image_cap(M: dict[str, Any], case: str, distortion_cap: int):
    covector, toggle_axes, _blocks = case_blocks(M, case)
    columns = curvature_columns(M, covector)
    support = {label for column in columns for label, _nu in column}
    labels = set()
    for label in support:
        for bits in range(1 << len(toggle_axes)):
            moved = label
            for j, axis in enumerate(toggle_axes):
                if bits & (1 << j):
                    moved ^= 1 << axis
            labels.add(moved)
    labels = sorted(labels)
    basis, _raw, euler = raw_block(M, covector, labels)
    basis2, response, _signs = response_data(M, covector, labels)
    if basis != basis2:
        raise AssertionError("local coupled basis mismatch")
    index = {(label, mu): i for i, (label, mu, _mask) in enumerate(basis)}
    entries = {}
    for column_index, column in enumerate(columns):
        for (label, nu), value in column.items():
            if value[1]:
                raise AssertionError("metric column left real basis")
            entries[(index[(label, nu)], column_index)] = QQ(value[0].numerator) / QQ(value[0].denominator)
    mixed = matrix(QQ, euler.nrows(), len(METRIC_SLOTS), entries, sparse=True)
    coupled = matrix.block(QQ, [[matrix(QQ, 10, 10), mixed.transpose()], [mixed, euler]])
    response_dual = matrix.block(QQ, [[matrix(QQ, 10, response.nrows())], [response.transpose()]])
    local_cap = euler.augment(response.transpose()).rank()
    coupled_cap = coupled.augment(response_dual).rank()

    gauge = matrix(QQ, coupled.nrows(), 4, sparse=True)
    for row, (a, b) in enumerate(METRIC_SLOTS):
        for vector_index in range(4):
            gauge[row, vector_index] = (
                (covector[a] if b == vector_index else 0)
                + (covector[b] if a == vector_index else 0)
            )
    return {
        "local_label_count": len(labels),
        "local_image_cap_rank": local_cap,
        "metric_coupled_image_cap_rank": coupled_cap,
        "metric_rank_increment": coupled_cap - local_cap,
        "total_coupled_image_cap_rank": distortion_cap - local_cap + coupled_cap,
        "gauge_rank": gauge.rank(),
        "euler_times_gauge_rank": (coupled * gauge).rank(),
        "redundancy_times_euler_rank": (gauge.transpose() * coupled).rank(),
    }


def build() -> dict[str, Any]:
    M = load_algebra()
    cases = []
    for case in ("native_nonnull", "native_null_auxiliary_nonzero"):
        _covector, totals, types = distortion_census(M, case)
        coupled = coupled_image_cap(M, case, totals["image_cap_rank"])
        middle_lower = 229386 - coupled["total_coupled_image_cap_rank"] - coupled["gauge_rank"]
        cases.append(
            {
                "case": case,
                "distortion_i1b_euler_rank": totals["euler_rank"],
                "full_residual_response_rank": totals["response_rank"],
                "distortion_universal_image_cap_rank": totals["image_cap_rank"],
                "block_types": [
                    {
                        "i1b_euler_rank": key[0],
                        "response_rank": key[1],
                        "image_cap_rank": key[2],
                        "multiplicity": multiplicity,
                    }
                    for key, multiplicity in sorted(types.items())
                ],
                **coupled,
                "bosonic_middle_cohomology_lower_bound": middle_lower,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K743-SC-ACT-06-RESIDUAL-SQUARE-IMAGE-CAP",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Pairing-independent exact image cap for every residual-square Hessian factored through the complete K740 derivative response on K720's frozen I1B background.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "image_theorem": {
            "hessian_form": "H_Q=J^T Q J",
            "universal_inclusion": "IMAGE(H_Q)_SUBSET_IMAGE(J^T)",
            "combined_inclusion": "IMAGE(E_I1B+H_Q)_SUBSET_IMAGE(E_I1B)+IMAGE(J^T)",
            "pairing_selection_required_for_cap": False,
            "relative_weight_required_for_cap": False,
            "complete_invariant_block_enumeration": True,
        },
        "exact_controls": {"field_dimension": 229386, "owned_metric_diffeomorphism_rank": 4, "cases": cases},
        "decision": {
            "every_same_response_residual_pairing_fails_middle_exactness": True,
            "full_carrier_rank_threshold_survival_reversed_by_exact_image_overlap": True,
            "unitary_pairing_fork_selected": False,
            "next_exact_input": "Compose the universal bosonic obstruction with the displayed exact fermion diagonal, then seek a genuinely different action-owned principal response or stationary background; no pairing on the same K740 response can repair K720.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This closes the same-background residual-square repair class for K740's response, not every stationary germ or action-owned principal packet.",
        "controls": {
            "producer": "tests/channel-swings/k743_sc_act_06_residual_square_image_cap.py",
            "probe": "tests/channel-swings/k743_sc_act_06_residual_square_image_cap_probe.py",
            "controls_passed": 48,
            "hostile_mutations_rejected": 40,
        },
        "claim_ceiling": "Exact pairing-independent finite principal-symbol image obstruction on the frozen realization. No unique residual pairing, symmetry parent, global domain, all-background no-go, source-status, prediction, confirmation or physical verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    theorem = packet["image_theorem"]
    controls = packet["exact_controls"]
    decision = packet["decision"]
    assert packet["result_id"] == "K743-SC-ACT-06-RESIDUAL-SQUARE-IMAGE-CAP"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["direction"] == "observed_to_native"
    assert packet["status"] == "working_draft_verified"
    assert packet["target_claim"] == "SC-ACT-06"
    assert theorem["hessian_form"] == "H_Q=J^T Q J"
    assert theorem["universal_inclusion"] == "IMAGE(H_Q)_SUBSET_IMAGE(J^T)"
    assert theorem["combined_inclusion"] == "IMAGE(E_I1B+H_Q)_SUBSET_IMAGE(E_I1B)+IMAGE(J^T)"
    assert not theorem["pairing_selection_required_for_cap"]
    assert not theorem["relative_weight_required_for_cap"]
    assert theorem["complete_invariant_block_enumeration"]
    assert controls["field_dimension"] == 229386
    assert controls["owned_metric_diffeomorphism_rank"] == 4
    cases = {row["case"]: row for row in controls["cases"]}
    nonnull = cases["native_nonnull"]
    null = cases["native_null_auxiliary_nonzero"]
    assert (nonnull["distortion_i1b_euler_rank"], null["distortion_i1b_euler_rank"]) == (130912, 122746)
    assert nonnull["full_residual_response_rank"] == null["full_residual_response_rank"] == 122864
    assert nonnull["distortion_universal_image_cap_rank"] == null["distortion_universal_image_cap_rank"] == 131068
    assert (nonnull["total_coupled_image_cap_rank"], null["total_coupled_image_cap_rank"]) == (131074, 131071)
    assert (nonnull["metric_rank_increment"], null["metric_rank_increment"]) == (6, 3)
    assert (nonnull["local_label_count"], null["local_label_count"]) == (8, 12)
    assert (nonnull["local_image_cap_rank"], null["local_image_cap_rank"]) == (104, 96)
    assert (nonnull["metric_coupled_image_cap_rank"], null["metric_coupled_image_cap_rank"]) == (110, 99)
    assert (nonnull["bosonic_middle_cohomology_lower_bound"], null["bosonic_middle_cohomology_lower_bound"]) == (98308, 98311)
    for name, row in cases.items():
        assert row["gauge_rank"] == 4
        assert row["euler_times_gauge_rank"] == 0
        assert row["redundancy_times_euler_rank"] == 0
        expected_blocks = 8192 if name == "native_nonnull" else 4096
        assert sum(item["multiplicity"] for item in row["block_types"]) == expected_blocks
    assert decision["every_same_response_residual_pairing_fails_middle_exactness"]
    assert decision["full_carrier_rank_threshold_survival_reversed_by_exact_image_overlap"]
    assert not decision["unitary_pairing_fork_selected"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
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
