#!/usr/bin/env python3
"""Hostile mutations for K1493."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1493-polynomial-krylov-top-chaos.json").read_text())


def valid(d):
    a, q = d["polynomial_top_chaos"], d["decision"]
    return all([
        d["claim_id"] == "K1493", "P_(4j)" in a["top_chaos_identity"],
        "4(j-1)" in a["top_chaos_identity"], "(4!)^j" in a["symmetrization_lower_bound"],
        "nonnegative" in a["symmetrization_lower_bound"], "h_(j,N)>=1" in a["residual_lower_bound"],
        "(2j-1)^(4j)" in a["hypercontractive_upper_bound"],
        q["all_fixed_degrees_constructed"], q["top_chaos_projection_survives_lower_polynomials"],
        q["monic_residual_squared_norm_lower"] == 1, not q["finite_degree_residual_can_collapse"],
        not q["unbounded_coefficient_growth_proved"], not q["protected_status_change"],
    ])


mutations = [
    ("wrong claim", lambda d: d.update(claim_id="K1492")),
    ("erase top projection", lambda d: d["polynomial_top_chaos"].update(top_chaos_identity="none")),
    ("erase degree separation", lambda d: d["polynomial_top_chaos"].update(top_chaos_identity="P_(4j)")),
    ("erase block count", lambda d: d["polynomial_top_chaos"].update(symmetrization_lower_bound="nonnegative")),
    ("erase positivity", lambda d: d["polynomial_top_chaos"].update(symmetrization_lower_bound="(4!)^j")),
    ("remove residual bound", lambda d: d["polynomial_top_chaos"].update(residual_lower_bound="unknown")),
    ("remove upper bound", lambda d: d["polynomial_top_chaos"].update(hypercontractive_upper_bound="unknown")),
    ("deny all degrees", lambda d: d["decision"].update(all_fixed_degrees_constructed=False)),
    ("deny top survival", lambda d: d["decision"].update(top_chaos_projection_survives_lower_polynomials=False)),
    ("weaken lower", lambda d: d["decision"].update(monic_residual_squared_norm_lower=0)),
    ("allow collapse", lambda d: d["decision"].update(finite_degree_residual_can_collapse=True)),
    ("claim unbounded", lambda d: d["decision"].update(unbounded_coefficient_growth_proved=True)),
    ("move status", lambda d: d["decision"].update(protected_status_change=True)),
]

for i, (label, mutate) in enumerate(mutations, 1):
    x = copy.deepcopy(D); mutate(x)
    assert not valid(x), label
    print(f"PASS {i:02d}: rejected {label}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
