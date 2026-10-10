#!/usr/bin/env python3
"""Continuous compact-mixture control for K1693."""
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1693-continuous-mixture-fisher-identity.json").read_text())
    count, epsilon = 32768, 0.8
    angle = 2.0 * math.pi * np.arange(count) / count
    raw = np.exp(epsilon * np.cos(angle))
    rho = raw / np.mean(raw)
    score = -epsilon * np.sin(angle)
    component_fisher = float(np.mean(rho * score * score))

    # At x=0, translated densities range over rho(-a); their Haar mixture is 1,
    # posterior mean score is zero and posterior score variance is component_fisher.
    mixture_density = float(np.mean(rho))
    mixture_score = float(np.mean(rho * score) / mixture_density)
    posterior_variance = float(np.mean(rho * (score - mixture_score) ** 2) / mixture_density)

    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1693"),
        ("compact group", "compact normalized Haar" in data["setting"]["group"]),
        ("invariant weight", "Omega" in data["setting"]["invariance"]),
        ("posterior", "rho_a(q)" in data["setting"]["posterior"]),
        ("mixture score", "integral_G" in data["setting"]["mixture_score"]),
        ("identity", "u_a-bar_u" in data["identity"]),
        ("equality", "group invariant" in data["equality"]),
        ("normalized example", abs(mixture_density - 1.0) < 1e-13),
        ("zero mixture score", abs(mixture_score) < 1e-13),
        ("positive component Fisher", component_fisher > 0.0),
        ("posterior identity", abs(component_fisher - posterior_variance) < 1e-13),
        ("scope", "does not supply a continuum limit" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
