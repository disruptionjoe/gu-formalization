#!/usr/bin/env python3
"""K1063: recover the linear response coefficient on each four-mode horn."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1063-k1062-quadratic-response-recovery.json"
MODES = [3.0, 8.0, 15.0, 24.0]


def solve(matrix, vector):
    a = [row[:] + [value] for row, value in zip(matrix, vector)]
    for col in range(len(vector)):
        pivot = max(range(col, len(vector)), key=lambda row: abs(a[row][col]))
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        assert abs(scale) > 1e-14
        a[col] = [value / scale for value in a[col]]
        for row in range(len(vector)):
            if row != col:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [a[i][-1] for i in range(len(vector))]


def response_row(mu):
    xs = [math.sqrt(lam + mu) for lam in MODES]
    columns = [[1.0] * 4, MODES, xs]
    gram = [[sum(a * b for a, b in zip(left, right)) for right in columns] for left in columns]
    selector = solve(gram, [0.0, 0.0, 1.0])
    return [sum(selector[j] * columns[j][i] for j in range(3)) for i in range(4)]


def build():
    rows = {str(mu): response_row(mu) for mu in (1, 4)}
    return {
        "schema_version": "1.0",
        "result_id": "K1063-K1062-QUADRATIC-RESPONSE-RECOVERY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "modes": [3, 8, 15, 24],
        "response_rows": rows,
        "mass_one_exact_row": ["-41/20", "33/20", "37/20", "-29/20"],
        "component_error_amplification": {key: sum(abs(v) for v in row) for key, row in rows.items()},
        "recovery_rule": "g_hat=r_mu dot y; for a correct horn and |e_i|<=eta, abs(g_hat-g)<=eta*||r_mu||_1",
        "nonzero_certificate": "after horn feasibility is established, abs(g_hat)>eta*||r_mu||_1 certifies nonzero linear response",
        "conditioning_warning": "the mass-four response row amplifies component error more strongly than the mass-one row",
        "scope": "coefficient recovery inside the supplied four-mode quadratic model; no physical calibration ownership",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["modes"] == [3, 8, 15, 24]
    assert data["mass_one_exact_row"] == ["-41/20", "33/20", "37/20", "-29/20"]
    for mu in (1, 4):
        row = data["response_rows"][str(mu)]
        xs = [math.sqrt(lam + mu) for lam in MODES]
        assert abs(sum(row)) < 1e-11
        assert abs(sum(a * b for a, b in zip(row, MODES))) < 1e-11
        assert abs(sum(a * b for a, b in zip(row, xs)) - 1.0) < 1e-11
    assert abs(data["component_error_amplification"]["1"] - 7.0) < 1e-11
    assert 10.22 < data["component_error_amplification"]["4"] < 10.23
    assert "abs(g_hat-g)<=eta*||r_mu||_1" in data["recovery_rule"]
    assert data["nonzero_certificate"].startswith("after horn feasibility")
    assert data["conditioning_warning"].startswith("the mass-four")
    assert data["scope"].startswith("coefficient recovery inside")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1063 controls: 13/13")
