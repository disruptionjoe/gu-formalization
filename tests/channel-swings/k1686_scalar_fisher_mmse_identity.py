#!/usr/bin/env python3
"""Certificate for K1686's exact scalar Fisher/MMSE identity."""
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite_e import hermegauss

ROOT = Path(__file__).resolve().parents[2]


def evaluate(points, probabilities, t, order=120):
    nodes, weights = hermegauss(order)
    weights = weights / math.sqrt(2 * math.pi)
    root_t, sigma = math.sqrt(t), math.sqrt(1 - t)
    fisher = mmse = 0.0
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
            fisher += probability * weight * score * score
            mmse += probability * weight * (x - mean) ** 2
    identity = t / (1 - t) ** 2 * (1 - t - mmse)
    gamma_identity = (t / (1 - t)) * (1 - mmse / (1 - t))
    return fisher, mmse, identity, gamma_identity


def main():
    data = json.loads((ROOT / "lab/process/k1686-scalar-fisher-mmse-identity.json").read_text())
    claim, decision = data["identity"], data["decision"]
    checks = [("schema", data["schema_version"] == "1.0"),
              ("claim", data["claim_id"] == "K1686")]
    seeds = [
        ([-1.0, 1.0], [0.5, 0.5]),
        ([-math.sqrt(2), 0.0, math.sqrt(2)], [0.25, 0.5, 0.25]),
    ]
    for seed_number, (points, probabilities) in enumerate(seeds, 1):
        for t in (0.03, 0.17, 0.41):
            fisher, mmse, identity, gamma_identity = evaluate(points, probabilities, t)
            label = f"seed {seed_number} t={t}"
            checks += [
                (label + " score/MMSE", math.isclose(fisher, identity, rel_tol=2e-10, abs_tol=2e-12)),
                (label + " gamma form", math.isclose(identity, gamma_identity, rel_tol=2e-12, abs_tol=2e-12)),
                (label + " nonnegative", fisher >= -1e-12),
                (label + " Gaussian MMSE ceiling", mmse <= 1 - t + 2e-12),
            ]
    checks += [
        ("channel typed", "centered unit-variance" in claim["channel"]),
        ("posterior score", "E[X|Y_t=y]" in claim["relative_score"]),
        ("MMSE identity", "mmse_X(gamma)" in claim["fisher_mmse"]),
        ("gamma identity", "gamma{1-(1+gamma)" in claim["fisher_mmse"]),
        ("cumulant transport", "t^2 kappa_4(X)" in claim["cumulant_transport"]),
        ("score decision", decision["exact_score_identified"]),
        ("Fisher decision", decision["exact_fisher_mmse_identified"]),
        ("cumulant decision", decision["exact_fourth_cumulant_transport"]),
        ("optimizer open", not decision["global_scalar_optimizer_identified"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
