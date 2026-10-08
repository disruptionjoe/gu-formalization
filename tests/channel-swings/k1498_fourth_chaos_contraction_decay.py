#!/usr/bin/env python3
"""Controls for K1498's fourth-chaos contraction power count."""
import hashlib, json, itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1498-fourth-chaos-contraction-decay.json").read_text())


def connected(vertices, edges):
    seen = {vertices[0]}
    while True:
        nxt = seen | {v for a, b, _ in edges for v in (a, b) if a in seen or b in seen}
        if nxt == seen:
            return len(seen) == len(vertices)
        seen = nxt


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["contraction_power_count"], D["decision"]
    checks += [
        ("schema", D["schema_version"] == "1.0"),
        ("claim", D["claim_id"] == "K1498"),
        ("orders", a["contraction_orders"] == [1, 2, 3]),
        ("four vertices", a["vertices"] == 4),
        ("eight edges", a["edges"] == 8),
        ("five loops", a["loop_rank"] == 5),
        ("degree seven", a["full_superficial_degree"] == 7),
        ("proper pair degrees", a["proper_two_vertex_degrees"] == [-1, 1, 3]),
        ("proper triple bound", a["proper_three_vertex_degree_upper"] == 2),
        ("graph upper", "N^7" in a["graph_sum_upper"]),
        ("variance order", "N^10" in a["variance_square_order"]),
        ("normalized decay", "N^-3" in a["normalized_contraction_upper"]),
        ("all vanish", q["all_nontrivial_contractions_vanish"]),
        ("criterion ready", q["fixed_chaos_fourth_moment_criterion_ready"]),
        ("degree fenced", not q["growing_polynomial_degree_controlled"]),
        ("lower fenced", not q["ground_energy_lower_bound_proved"]),
        ("protected fenced", not q["protected_status_change"]),
    ]
    vertices = ["A", "B", "C", "D"]
    for r in (1, 2, 3):
        mult = {("A", "B"): r, ("C", "D"): r, ("A", "C"): 4-r, ("B", "D"): 4-r}
        edges = [(x, y, m) for (x, y), m in mult.items()]
        E = sum(mult.values())
        checks += [
            (f"r{r} connected", connected(vertices, edges)),
            (f"r{r} edge count", E == 8),
            (f"r{r} loop rank", E-len(vertices)+1 == 5),
            (f"r{r} overall degree", 3*(E-len(vertices)+1)-E == 7),
            (f"r{r} max multiplicity", max(mult.values()) == max(r, 4-r)),
        ]
        for subset in itertools.combinations(vertices, 3):
            es = sum(m for (x, y), m in mult.items() if x in subset and y in subset)
            if es:
                checks.append((f"r{r} triple {''.join(subset)}", 3*(es-2)-es <= 2))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
