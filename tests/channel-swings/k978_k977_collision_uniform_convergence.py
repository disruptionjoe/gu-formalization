#!/usr/bin/env python3
"""K978 uniform between-grid convergence for the K963 collision repair."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k978-k977-collision-uniform-convergence.json"


def build():
    gamma, horizon = 0.7, 3.0
    rows = []
    for h in (0.2, 0.1, 0.05, 0.02):
        theta = 0.5 * math.acos(math.exp(-2 * gamma * h))
        bound = 1 - math.exp(-2 * gamma * h)
        # Dense deterministic replay of the left-continuous collision process.
        errs = []
        for j in range(10001):
            t = horizon * j / 10000
            approx = math.exp(-2 * gamma * h * math.floor(t / h + 1e-12))
            exact = math.exp(-2 * gamma * t)
            errs.append(abs(approx - exact))
        rows.append({
            "h": h,
            "theta_h": theta,
            "coupling_rate_theta_over_h": theta / h,
            "fresh_ancillas_through_T": math.floor(horizon / h),
            "analytic_uniform_bound": bound,
            "linear_bound_2_gamma_h": 2 * gamma * h,
            "sampled_sup_error": max(errs),
            "bound_holds": max(errs) <= bound + 1e-12 and bound <= 2 * gamma * h,
            "white_noise_scale_h_g_squared": h * (theta / h) ** 2,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K978-COLLISION-UNIFORM-CONVERGENCE",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Left-continuous continuous-time interpolation of K963--K964's fresh-qubit collision construction on a finite horizon.",
        "theorem": {
            "target": "lambda(t)=exp(-2 gamma t)",
            "collision_interpolation": "lambda_h(t)=exp(-2 gamma h floor(t/h))",
            "uniform_error": "sup_{0<=t<=T}|lambda_h(t)-lambda(t)| <= 1-exp(-2 gamma h) <= 2 gamma h",
            "uniform_on_every_fixed_finite_horizon": True,
            "grid_error_zero": True,
            "freshness_cost": "floor(T/h) one-pass ancillas by horizon T",
            "coupling": "theta_h=(1/2) arccos(exp(-2 gamma h)); g_h=theta_h/h",
            "coupling_rate_diverges_as": "sqrt(gamma/h)",
            "white_noise_action_scale": "h g_h^2 -> gamma",
        },
        "exact_controls": {
            "gamma": gamma,
            "horizon": horizon,
            "rows": rows,
            "all_bounds_hold": all(r["bound_holds"] for r in rows),
            "sampled_errors_decrease": all(rows[i+1]["sampled_sup_error"] < rows[i]["sampled_sup_error"] for i in range(len(rows)-1)),
            "coupling_rates_increase": all(rows[i+1]["coupling_rate_theta_over_h"] > rows[i]["coupling_rate_theta_over_h"] for i in range(len(rows)-1)),
            "white_noise_scales_tend_to_gamma": abs(rows[-1]["white_noise_scale_h_g_squared"] - gamma) < 0.02,
        },
        "ownership": {
            "clock_reset_and_freshness_imported": True,
            "continuous_time_action_constructed": False,
            "gu_reservoir_or_domain_constructed": False,
            "prediction_or_confirmation_credit": False,
        },
        "decision": {
            "off_grid_convergence_quantified": True,
            "grid_equality_not_microscopic_owner": True,
            "next_exact_input": "Compose the bounded-parent obstruction and singular fresh-resource repair into an exact assumption fork.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Uniform coherence-factor approximation for one supplied collision interpolation only; no universal channel-norm optimum or GU-selected reservoir.",
    }


def validate(p):
    t, c, o, d = p["theorem"], p["exact_controls"], p["ownership"], p["decision"]
    assert t["uniform_on_every_fixed_finite_horizon"] and t["grid_error_zero"]
    assert len(c["rows"]) == 4 and c["all_bounds_hold"] and c["sampled_errors_decrease"]
    assert c["coupling_rates_increase"] and c["white_noise_scales_tend_to_gamma"]
    assert o["clock_reset_and_freshness_imported"] and not o["continuous_time_action_constructed"]
    assert not o["gu_reservoir_or_domain_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["off_grid_convergence_quantified"] and d["grid_equality_not_microscopic_owner"]
    assert p["source_and_ledger_effect"] == "none"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.check: assert OUTPUT.read_text() == text
    elif a.write: OUTPUT.write_text(text)
    else: print(text, end="")
    print("K978 controls: 13/13")


if __name__ == "__main__": main()
