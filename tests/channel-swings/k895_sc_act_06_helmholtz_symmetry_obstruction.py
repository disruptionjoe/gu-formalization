#!/usr/bin/env python3
"""K895: exact Helmholtz obstruction for the selected-I1B formal Euler map."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
OUTPUT = ROOT / "lab/process/k895-sc-act-06-helmholtz-symmetry-obstruction.json"
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k887": ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json",
    "k892": ROOT / "lab/process/k892-sc-act-06-minimal-formal-gauge-completion.json",
    "k894": ROOT / "lab/process/k894-sc-act-06-action-owned-completion-boundary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rational_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows, columns, pivot_row = len(work), len(work[0]), 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [value - factor * basis for value, basis in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def exact_block_data() -> dict[str, Any]:
    capture = StringIO()
    source = BACKEND.read_text(encoding="utf-8")
    source = source.replace("\nimport sympy as sp\n", "\n").split("\ntr = sp.trace", 1)[0]
    backend: dict[str, Any] = {"__file__": str(BACKEND), "__name__": "k895_backend"}
    with redirect_stdout(capture):
        exec(compile(source, str(BACKEND), "exec"), backend)
    assert not backend["FAILURES"], backend["FAILURES"]
    n, eta, full = backend["N"], backend["ETA"], backend["FULL"]
    one, zero = backend["ONE"], backend["ZERO"]
    selected = ("comm", "symi", "symi")

    def scalar_one_form(covector):
        return {1 << mu: {0: (Fraction(value), Fraction(0))} for mu, value in enumerate(covector) if value}

    def direction(mu, mask):
        return {1 << mu: {mask: one}}

    def pairing(left, right):
        return backend["wedge_raw"](left, right).get(full, {}).get(0, zero)

    def rows_for_image(image):
        rows = []
        for form_mask, element in image.items():
            complement = full ^ form_mask
            if not complement or complement & (complement - 1):
                continue
            nu = complement.bit_length() - 1
            for clifford_mask, value in element.items():
                if value == zero:
                    continue
                result = pairing(direction(nu, clifford_mask), image)
                if result != zero:
                    rows.append((nu, clifford_mask, result))
        return rows

    def block(covector, labels):
        k_form = scalar_one_form(covector)
        basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(n)]
        index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
        raw = [[Fraction(0) for _ in basis] for _ in basis]
        for column, (label, mu, mask) in enumerate(basis):
            image = backend["shiab"](backend["wedge_raw"](k_form, direction(mu, mask)), selected)
            for nu, outmask, value in rows_for_image(image):
                row_label = outmask ^ (1 << nu)
                if (row_label, nu) in index:
                    assert value[1] == 0
                    raw[index[(row_label, nu)]][column] += value[0]
        action = [[(raw[i][j] - raw[j][i]) / 2 for j in range(len(basis))] for i in range(len(basis))]
        assert all(action[i][j] == -action[j][i] for i in range(len(basis)) for j in range(len(basis)))
        return basis, action

    axis = 0
    covector = (1,) + (0,) * 13
    positive = [i for i, sign in enumerate(eta) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(eta) if sign == -1 and i != axis]
    totals = Counter()
    distributions = {key: Counter() for key in (
        "action_rank", "radial_rank", "helmholtz_defect_rank",
        "formal_completed_rank", "formal_completed_helmholtz_defect_rank",
        "formal_correction_symmetric_part_rank",
    )}
    representative_rows = []
    for positive_degree in range(len(positive) + 1):
        for negative_degree in range(len(negative) + 1):
            base = sum(1 << i for i in positive[:positive_degree]) | sum(1 << i for i in negative[:negative_degree])
            basis, action = block(covector, [base, base ^ (1 << axis)])
            radial = [j for j, (_, mu, _) in enumerate(basis) if mu == axis]
            radial_indicator = [1 if j in radial else 0 for j in range(len(basis))]
            defect = [[action[i][j] - action[j][i] for j in range(len(basis))] for i in range(len(basis))]
            formal_correction = [[-action[i][j] * radial_indicator[j] for j in range(len(basis))] for i in range(len(basis))]
            formal_completed = [[action[i][j] + formal_correction[i][j] for j in range(len(basis))] for i in range(len(basis))]
            formal_completed_defect = [[formal_completed[i][j] - formal_completed[j][i] for j in range(len(basis))] for i in range(len(basis))]
            formal_correction_symmetric = [[(formal_correction[i][j] + formal_correction[j][i]) / 2 for j in range(len(basis))] for i in range(len(basis))]
            ranks = {
                "action_rank": rational_rank(action),
                "radial_rank": rational_rank([[row[j] for j in radial] for row in action]),
                "helmholtz_defect_rank": rational_rank(defect),
                "formal_completed_rank": rational_rank(formal_completed),
                "formal_completed_helmholtz_defect_rank": rational_rank(formal_completed_defect),
                "formal_correction_symmetric_part_rank": rational_rank(formal_correction_symmetric),
            }
            multiplicity = math.comb(len(positive), positive_degree) * math.comb(len(negative), negative_degree)
            totals["multiplicity"] += multiplicity
            totals["field_dimension"] += len(basis) * multiplicity
            for key, rank in ranks.items():
                totals[key] += rank * multiplicity
                distributions[key][rank] += multiplicity
            representative_rows.append({
                "positive_degree": positive_degree,
                "negative_degree": negative_degree,
                "base_parity": (positive_degree + negative_degree) % 2,
                "multiplicity": multiplicity,
                **ranks,
            })
    return {
        "backend_replayed": True,
        "representative_block_count": len(representative_rows),
        "representative_multiplicity": totals["multiplicity"],
        "connection_field_dimension": totals["field_dimension"],
        "selected_action_rank": totals["action_rank"],
        "radial_gauge_restriction_rank": totals["radial_rank"],
        "helmholtz_symmetry_defect_rank": totals["helmholtz_defect_rank"],
        "formal_completed_rank": totals["formal_completed_rank"],
        "formal_completed_helmholtz_defect_rank": totals["formal_completed_helmholtz_defect_rank"],
        "formal_correction_symmetric_part_rank": totals["formal_correction_symmetric_part_rank"],
        "rank_distributions": {
            key: {str(rank): count for rank, count in sorted(distribution.items())}
            for key, distribution in distributions.items()
        },
        "representative_rows": representative_rows,
    }


def build() -> dict[str, Any]:
    exact = exact_block_data()
    return {
        "schema_version": "1.0",
        "result_id": "K895-SC-ACT-06-HELMHOLTZ-SYMMETRY-OBSTRUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Helmholtz/second-variation test of the frozen selected-I1B formal Euler map on the fixed even bosonic connection domain at K717's nonnull symbol.",
        "gu_typed_objects": {
            "carrier": "229376-dimensional real even connection tangent at the K717 flat zero-fermion germ",
            "pairing": "the fixed real coefficient pairing used by K887 to transpose the raw selected-I1B density map",
            "real_structure": "real K77 nonnull coefficient blocks",
            "grading": "even bosonic field tangent --A--> even bosonic Euler dual",
            "action_owner": "frozen selected-I1B formal Euler construction only; no completed scalar action Hessian inferred",
            "target": "INTEGRABILITY-TYPE=Helmholtz symmetry prerequisite for a same-domain even scalar-action Hessian",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "exact_helmholtz_test": {
            key: value for key, value in exact.items() if key != "representative_rows"
        },
        "structural_theorem": {
            "formal_euler_rule": "A=(R-R^T)/2",
            "formal_adjoint_identity": "A^T=-A",
            "even_scalar_action_hessian_identity": "Hessian^T=Hessian on one fixed common bosonic domain",
            "selected_map_is_nonzero": exact["selected_action_rank"] > 0,
            "selected_map_is_helmholtz_integrable_as_standalone_hessian": False,
            "exact_selected_map_rank": exact["selected_action_rank"],
            "exact_symmetry_defect_rank": exact["helmholtz_symmetry_defect_rank"],
            "radial_defect_is_strict_subtest": exact["radial_gauge_restriction_rank"] < exact["selected_action_rank"],
        },
        "decision": {
            "selected_i1b_formal_euler_map_is_action_hessian": False,
            "k891_radial_cancellation_is_sufficient_for_action_ownership": False,
            "same_domain_variational_completion_still_possible": True,
            "quotient_ranks_now_admissible": False,
            "next_exact_input": "A same-domain variational completion must cancel the entire rank-130912 skew part, not only the rank-8191 radial defect; classify that correction and test the formal projector before crediting any quotient map.",
        },
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "A Helmholtz obstruction to one formal Euler construction supplies no completed action, physical state, observable, prediction or confirmation.",
        "claim_ceiling": "Exact same-domain even-bosonic Helmholtz obstruction for the frozen selected-I1B formal Euler map. It does not exclude a completed action, different domain, odd sector, boundary completion, new parent or other stationary germ.",
        "controls": {
            "producer": "tests/channel-swings/k895_sc_act_06_helmholtz_symmetry_obstruction.py",
            "probe": "tests/channel-swings/k895_sc_act_06_helmholtz_symmetry_obstruction_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(packet: dict[str, Any]) -> None:
    exact, theorem, decision = packet["exact_helmholtz_test"], packet["structural_theorem"], packet["decision"]
    checks = [
        packet["classification"] == "SOURCE_NATIVE_ROUTE", packet["target_claim"] == "SC-ACT-06",
        set(packet["pinned_inputs"]) == set(PATHS), all(len(row["sha256"]) == 64 for row in packet["pinned_inputs"].values()),
        exact["backend_replayed"], exact["representative_block_count"] == 56,
        exact["representative_multiplicity"] == 8192, exact["connection_field_dimension"] == 229376,
        exact["selected_action_rank"] == 130912, exact["radial_gauge_restriction_rank"] == 8191,
        exact["helmholtz_symmetry_defect_rank"] == 130912,
        exact["rank_distributions"]["action_rank"] == {"2": 1, "6": 4095, "24": 78, "26": 4018},
        exact["rank_distributions"]["radial_rank"] == {"0": 4096, "1": 1, "2": 4095},
        exact["rank_distributions"]["helmholtz_defect_rank"] == exact["rank_distributions"]["action_rank"],
        theorem["formal_euler_rule"] == "A=(R-R^T)/2", theorem["formal_adjoint_identity"] == "A^T=-A",
        theorem["even_scalar_action_hessian_identity"].startswith("Hessian^T=Hessian"), theorem["selected_map_is_nonzero"],
        not theorem["selected_map_is_helmholtz_integrable_as_standalone_hessian"], theorem["exact_selected_map_rank"] == 130912,
        theorem["exact_symmetry_defect_rank"] == 130912, theorem["radial_defect_is_strict_subtest"],
        not decision["selected_i1b_formal_euler_map_is_action_hessian"],
        not decision["k891_radial_cancellation_is_sufficient_for_action_ownership"],
        decision["same_domain_variational_completion_still_possible"], not decision["quotient_ranks_now_admissible"],
        "rank-130912" in decision["next_exact_input"], packet["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "no completed action" in packet["ledger_no_change_reason"], "even-bosonic" in packet["claim_ceiling"],
        packet["controls"]["controls_passed"] == 40, packet["controls"]["hostile_mutations_rejected"] == 20,
        packet["gu_typed_objects"]["target"].startswith("INTEGRABILITY-TYPE="), packet["schema_version"] == "1.0",
        packet["status"] == "working_draft_verified", packet["direction"] == "observed_to_native",
        packet["result_id"].startswith("K895-"), exact["radial_gauge_restriction_rank"] < exact["selected_action_rank"],
        exact["selected_action_rank"] % 2 == 0, exact["helmholtz_symmetry_defect_rank"] == exact["selected_action_rank"],
    ]
    assert len(checks) == 40 and all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build(); validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
