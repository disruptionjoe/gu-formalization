#!/usr/bin/env python3
"""Certificate for K1688's matched-defect three-point dominance."""
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite_e import hermegauss

ROOT = Path(__file__).resolve().parents[2]


def moments(points, probabilities, power):
    return sum(probability * point**power for point, probability in zip(points, probabilities))


def fisher(points, probabilities, t, order=160):
    nodes, weights = hermegauss(order)
    weights = weights / math.sqrt(2 * math.pi)
    root_t, sigma = math.sqrt(t), math.sqrt(1 - t)
    result = 0.0
    for x, probability in zip(points, probabilities):
        for z, weight in zip(nodes, weights):
            y = root_t * x + sigma * z
            logs = np.array([
                math.log(prior) - (y - root_t * atom) ** 2 / (2 * (1 - t))
                for atom, prior in zip(points, probabilities)
            ])
            posterior = np.exp(logs - logs.max())
            posterior /= posterior.sum()
            mean = float(sum(atom * mass for atom, mass in zip(points, posterior)))
            score = root_t / (1 - t) * (mean - root_t * y)
            result += probability * weight * score * score
    return result


def main():
    data = json.loads((ROOT / "lab/process/k1688-three-point-channel-dominance.json").read_text())
    claim, decision = data["comparison"], data["decision"]
    root105 = math.sqrt(105)
    p = (15 + root105) / 60
    u_star = (root105 - 9) / 2
    points_star = [-1 / math.sqrt(p), 0.0, 1 / math.sqrt(p)]
    probabilities_star = [p / 2, 1 - p, p / 2]
    kappa4_star = moments(points_star, probabilities_star, 4) - 3
    kappa6_star = moments(points_star, probabilities_star, 6) - 15 * moments(points_star, probabilities_star, 4) + 30
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1688"),
        ("probabilities", math.isclose(sum(probabilities_star), 1.0)),
        ("mean", math.isclose(moments(points_star, probabilities_star, 1), 0.0, abs_tol=1e-14)),
        ("variance", math.isclose(moments(points_star, probabilities_star, 2), 1.0)),
        ("fourth cumulant", math.isclose(kappa4_star, -u_star, abs_tol=1e-13)),
        ("sixth cumulant cancellation", math.isclose(kappa6_star, 0.0, abs_tol=2e-13)),
        ("Rademacher coefficient", math.isclose(1 / 4 + 16**2 / (120 * 2**3), 31 / 60)),
        ("three-point coefficient", math.isclose(1 / 4 + kappa6_star**2 / (120 * u_star**3), 1 / 4, abs_tol=1e-13)),
        ("coefficient gap", math.isclose(31 / 60 - 1 / 4, 4 / 15)),
    ]
    for q in (1e-3, 3e-3, 1e-2):
        t_rademacher = math.sqrt(q / 2)
        t_star = math.sqrt(q / u_star)
        j_rademacher = fisher([-1.0, 1.0], [0.5, 0.5], t_rademacher)
        j_star = fisher(points_star, probabilities_star, t_star)
        checks += [
            (f"matched defect q={q}", math.isclose(2 * t_rademacher**2, u_star * t_star**2, rel_tol=1e-13)),
            (f"strict Fisher ordering q={q}", j_star < j_rademacher),
            (f"positive scaled gap q={q}", (j_rademacher - j_star) / q**3 > 0.1),
        ]
    checks += [
        ("seed declaration", "p_*=(15+sqrt(105))/60" in claim["three_point_seed"]),
        ("cumulant declaration", "kappa_6(X_*)=0" in claim["three_point_cumulants"]),
        ("strict law", "(4/15)q^3" in claim["strict_local_order"]),
        ("local scope", "pointwise weak-channel" in claim["scope_guard"]),
        ("cancellation decision", decision["sixth_cumulant_canceled"]),
        ("local optimum refuted", decision["rademacher_local_scalar_optimality_false"]),
        ("K1682 preserved", decision["k1682_fixed_t_extremality_preserved"]),
        ("global optimizer open", not decision["global_scalar_optimizer_identified"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
