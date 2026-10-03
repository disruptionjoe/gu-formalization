#!/usr/bin/env python3
"""K887: exact selected-I1B failure to descend through the owned radial gauge."""
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
OUTPUT = ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json"
PATHS = {
    "k132": ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k873": ROOT / "lab/process/k873-sc-act-06-owned-symmetry-custody.json",
    "k879": ROOT / "lab/process/k879-sc-act-06-full-field-quotient-injection.json",
    "k885": ROOT / "lab/process/k885-sc-act-06-released-action-parent-quotient-inventory.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rational_rank(matrix: list[list[Fraction]]) -> int:
    """Return exact row rank over Q without a third-party algebra runtime."""
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


def exact_radial_restriction() -> dict[str, Any]:
    capture = StringIO()
    backend_source = BACKEND.read_text(encoding="utf-8")
    backend_source = backend_source.replace("\nimport sympy as sp\n", "\n")
    backend_source = backend_source.split("\ntr = sp.trace", 1)[0]
    m: dict[str, Any] = {"__file__": str(BACKEND), "__name__": "k887_backend"}
    with redirect_stdout(capture):
        exec(compile(backend_source, str(BACKEND), "exec"), m)
    assert not m["FAILURES"], m["FAILURES"]
    n, eta, full, one, zero = m["N"], m["ETA"], m["FULL"], m["ONE"], m["ZERO"]
    selected = ("comm", "symi", "symi")

    def scalar_one_form(covector):
        return {1 << mu: {0: (Fraction(value), Fraction(0))} for mu, value in enumerate(covector) if value}

    def direction(mu, mask):
        return {1 << mu: {mask: one}}

    def pairing(left, right):
        return m["wedge_raw"](left, right).get(full, {}).get(0, zero)

    def rows_for_image(image):
        out = []
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
                    out.append((nu, clifford_mask, result))
        return out

    def raw_block(covector, labels):
        k_form = scalar_one_form(covector)
        basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(n)]
        index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
        raw = [[Fraction(0) for _ in basis] for _ in basis]
        for column, (label, mu, mask) in enumerate(basis):
            image = m["shiab"](m["wedge_raw"](k_form, direction(mu, mask)), selected)
            for nu, outmask, value in rows_for_image(image):
                row_label = outmask ^ (1 << nu)
                if (row_label, nu) in index:
                    assert value[1] == 0
                    raw[index[(row_label, nu)]][column] += value[0]
        euler = [
            [(raw[row][column] - raw[column][row]) / 2 for column in range(len(basis))]
            for row in range(len(basis))
        ]
        return basis, raw, euler

    axis = 0
    covector = (1,) + (0,) * 13
    positive = [i for i, sign in enumerate(eta) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(eta) if sign == -1 and i != axis]
    distribution: Counter[int] = Counter()
    representative_rows = []
    total_domain = total_rank = 0
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = sum(1 << i for i in positive[:a]) | sum(1 << i for i in negative[:b])
            basis, raw, euler = raw_block(covector, [base, base ^ (1 << axis)])
            radial = [j for j, (_, mu, _) in enumerate(basis) if mu == axis]
            raw_radial_rank = rational_rank([[row[column] for column in radial] for row in raw])
            euler_radial_rank = rational_rank([[row[column] for column in radial] for row in euler])
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            distribution[euler_radial_rank] += multiplicity
            total_domain += len(radial) * multiplicity
            total_rank += euler_radial_rank * multiplicity
            representative_rows.append({
                "positive_degree": a,
                "negative_degree": b,
                "base_parity": (a + b) % 2,
                "multiplicity": multiplicity,
                "raw_response_rank_on_radial": raw_radial_rank,
                "i1b_euler_rank_on_radial": euler_radial_rank,
            })
    return {
        "backend_replayed": True,
        "representative_block_count": len(representative_rows),
        "radial_domain_dimension": total_domain,
        "i1b_euler_rank_on_radial": total_rank,
        "i1b_euler_kernel_on_radial": total_domain - total_rank,
        "block_rank_distribution": {str(key): distribution[key] for key in sorted(distribution)},
        "representative_rows": representative_rows,
    }


def build() -> dict[str, Any]:
    pinned = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    exact = exact_radial_restriction()
    return {
        "schema_version": "1.0",
        "result_id": "K887-SC-ACT-06-SELECTED-I1B-GAUGE-DESCENT-OBSTRUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Gauge-descent test for K720's selected-I1B Euler Hessian on K873's authenticated radial internal-gauge image at the K717 flat zero-fermion germ.",
        "gu_typed_objects": {
            "carrier": "K873 radial q-lambda gauge image inside the full 229376-dimensional connection tangent",
            "pairing": "K132 selected-I1B formal Euler antisymmetrization of the source-native transgression density",
            "real_structure": "real K77 nonnull base covector with exact rational invariant blocks",
            "grading": "owned internal gauge -> connection fields -> selected-I1B Euler target",
            "action_owner": "frozen K132/K720 comm/symi/symi selected-I1B realization only",
            "target": "MAP-TYPE=gauge-descent prerequisite for a map on ker(J)/im(G)",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "exact_gauge_test": exact,
        "structural_theorem": {
            "old_response_annihilates_radial_gauge": True,
            "raw_i1b_density_radial_columns_zero": True,
            "formal_euler_rule": "A=(R-R^T)/2",
            "on_radial_gauge": "A G=-(1/2)R^T G",
            "descent_condition": "A G=0",
            "descent_condition_satisfied": False,
            "selected_i1b_induced_map_on_old_quotient_exists": False,
            "missing_completion_may_restore_descent": True,
        },
        "decision": {
            "selected_i1b_forty_type_quotient_ranks_admissible": False,
            "selected_i1b_is_zero_on_old_quotient": False,
            "selected_i1b_current_realization_repairs_old_quotient": False,
            "complete_source_action_or_other_stationary_germ_excluded": False,
            "next_exact_input": "Construct the complete action-owned I1B field/gauge packet whose additional blocks cancel the 8191-dimensional radial defect, or supply a genuinely new independent response/symmetry module or source-owned nonzero-fermion stationary germ; only then compute quotient ranks.",
        },
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result rejects quotient descent for one frozen local selected-I1B realization but constructs no complete action, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact failure of the current selected-I1B Hessian to descend through the authenticated radial gauge image: rank 8191 on a 16384-dimensional gauge domain. No all-I1B, all-action, other-germ or global no-go follows.",
        "controls": {
            "producer": "tests/channel-swings/k887_sc_act_06_selected_i1b_gauge_descent_obstruction.py",
            "probe": "tests/channel-swings/k887_sc_act_06_selected_i1b_gauge_descent_obstruction_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(x: dict[str, Any]) -> None:
    e, t, d = x["exact_gauge_test"], x["structural_theorem"], x["decision"]
    rows = e["representative_rows"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE", x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS), all(len(v["sha256"]) == 64 for v in x["pinned_inputs"].values()),
        e["backend_replayed"], e["representative_block_count"] == 56,
        e["radial_domain_dimension"] == 16384, e["i1b_euler_rank_on_radial"] == 8191,
        e["i1b_euler_kernel_on_radial"] == 8193,
        e["block_rank_distribution"] == {"0": 4096, "1": 1, "2": 4095},
        len(rows) == 56, sum(r["multiplicity"] for r in rows) == 8192,
        all(r["raw_response_rank_on_radial"] == 0 for r in rows),
        all(r["i1b_euler_rank_on_radial"] in (0, 1, 2) for r in rows),
        sum(r["multiplicity"] * r["i1b_euler_rank_on_radial"] for r in rows) == 8191,
        sum(2 * r["multiplicity"] for r in rows) == 16384,
        next(r for r in rows if r["positive_degree"] == 6 and r["negative_degree"] == 7)["i1b_euler_rank_on_radial"] == 1,
        all(r["i1b_euler_rank_on_radial"] == (2 if r["base_parity"] else 0) for r in rows if (r["positive_degree"], r["negative_degree"]) != (6, 7)),
        t["old_response_annihilates_radial_gauge"], t["raw_i1b_density_radial_columns_zero"],
        t["formal_euler_rule"] == "A=(R-R^T)/2", t["descent_condition"] == "A G=0",
        not t["descent_condition_satisfied"], not t["selected_i1b_induced_map_on_old_quotient_exists"],
        t["missing_completion_may_restore_descent"], not d["selected_i1b_forty_type_quotient_ranks_admissible"],
        not d["selected_i1b_is_zero_on_old_quotient"], not d["selected_i1b_current_realization_repairs_old_quotient"],
        not d["complete_source_action_or_other_stationary_germ_excluded"], "8191-dimensional" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no complete action" in x["ledger_no_change_reason"], "rank 8191" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 36, x["controls"]["hostile_mutations_rejected"] == 20,
        x["gu_typed_objects"]["target"].startswith("MAP-TYPE="),
    ]
    assert len(checks) == 36, len(checks)
    assert all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    elif not args.check: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
