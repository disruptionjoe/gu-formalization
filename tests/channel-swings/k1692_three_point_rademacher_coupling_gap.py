#!/usr/bin/env python3
"""Algebraic and deterministic quadrature controls for K1692."""
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def scalar_j(points, probs, u, q, order=96):
    if q == 0.0:
        return 0.0
    t = math.sqrt(q / u)
    nodes, weights = np.polynomial.hermite.hermgauss(order)
    z = math.sqrt(2.0) * nodes
    total = 0.0
    sqrt_t = math.sqrt(t)
    noise = math.sqrt(1.0 - t)
    for x, px in zip(points, probs):
        y = sqrt_t * x + noise * z
        logw = []
        for point, prob in zip(points, probs):
            logw.append(math.log(prob) - (y - sqrt_t * point) ** 2 / (2.0 * (1.0 - t)))
        stack = np.vstack(logw)
        shift = np.max(stack, axis=0)
        posterior = np.exp(stack - shift)
        posterior /= np.sum(posterior, axis=0)
        mean = np.sum(posterior * np.asarray(points)[:, None], axis=0)
        score = sqrt_t / (1.0 - t) * (mean - sqrt_t * y)
        total += px * float(np.sum(weights * score * score) / math.sqrt(math.pi))
    return total


def golden_minimum(objective, upper):
    left, right = 0.0, upper
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    x1, x2 = right - phi * (right - left), left + phi * (right - left)
    f1, f2 = objective(x1), objective(x2)
    for _ in range(80):
        if f1 < f2:
            right, x2, f2 = x2, x1, f1
            x1 = right - phi * (right - left)
            f1 = objective(x1)
        else:
            left, x1, f1 = x1, x2, f2
            x2 = left + phi * (right - left)
            f2 = objective(x2)
    q = (left + right) / 2.0
    return q, objective(q)


def main():
    data = json.loads((ROOT / "lab/process/k1692-three-point-rademacher-coupling-gap.json").read_text())
    p = (15.0 + math.sqrt(105.0)) / 60.0
    u_star = (math.sqrt(105.0) - 9.0) / 2.0
    star_points = [0.0, 1.0 / math.sqrt(p), -1.0 / math.sqrt(p)]
    star_probs = [1.0 - p, p / 2.0, p / 2.0]
    r_points, r_probs, u_r = [1.0, -1.0], [0.5, 0.5], 2.0

    exact_gap = 432 * (Fraction(31, 60) - Fraction(1, 4))
    # The numerical objective below has A=tau/4=1 and ell=1, hence tau=4.
    exact_fixed_shape_gap = exact_gap / 16
    numerical = []
    for g in (0.001, 0.002, 0.004):
        q_r, f_r = golden_minimum(lambda q: scalar_j(r_points, r_probs, u_r, q) - g * q, 0.04)
        q_s, f_s = golden_minimum(lambda q: scalar_j(star_points, star_probs, u_star, q) - g * q, 0.04)
        numerical.append((g, q_r, q_s, f_r - f_s))

    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1692"),
        ("three-point moment", abs(sum(w * x * x for x, w in zip(star_points, star_probs)) - 1.0) < 1e-14),
        ("three-point kappa6", abs(1.0 / p**2 - 15.0 / p + 30.0) < 1e-12),
        ("exact cubic gap", exact_gap == Fraction(576, 5)),
        ("manifest gap", "(576/5)" in data["coefficients"]["difference"]),
        ("fixed-shape strict", data["decision"]["strict_for_each_fixed_shape_and_sufficiently_small_positive_g"] is True),
        ("global shape open", data["decision"]["strict_after_global_shape_optimization_proved"] is False),
        ("finite strength open", data["decision"]["finite_strength_scalar_optimizer_identified"] is False),
        ("R optimizer scale", all(abs(q_r / g - 3.0) < 0.2 for g, q_r, _, _ in numerical)),
        ("star optimizer scale", all(abs(q_s / g - 3.0) < 0.2 for g, _, q_s, _ in numerical)),
        ("numerical strictness", all(delta > 0.0 for _, _, _, delta in numerical)),
        ("cubic scale", abs(numerical[0][3] / numerical[0][0] ** 3 - float(exact_fixed_shape_gap)) < 2.0),
        ("scope guard", "not uniform over C" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, (label, numerical)
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
