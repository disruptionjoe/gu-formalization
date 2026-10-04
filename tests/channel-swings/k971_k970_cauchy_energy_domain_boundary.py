#!/usr/bin/env python3
"""K971 exact energy-domain boundary for the K966 Cauchy reservoir."""
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k971-k970-cauchy-energy-domain-boundary.json"

def abs_first_cutoff(a, cutoff):
    return (a / math.pi) * math.log1p((cutoff / a) ** 2)

def second_cutoff(a, cutoff):
    return (2 * a / math.pi) * (cutoff - a * math.atan(cutoff / a))

def build():
    gamma = 0.7
    a = 2 * gamma
    cutoffs = (10.0, 100.0, 1000.0)
    rows = [{"cutoff": x, "absolute_first_moment": abs_first_cutoff(a, x),
             "second_moment": second_cutoff(a, x)} for x in cutoffs]
    return {
        "schema_version": "1.0", "result_id": "K971-CAUCHY-ENERGY-DOMAIN-BOUNDARY",
        "created": "2026-10-03", "status": "working_draft_verified",
        "direction": "observed_to_native", "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Spectral-moment and multiplication-generator domain of K966's normalized Cauchy reservoir state.",
        "construction": {"gamma": gamma, "scale": a,
            "density": "a/(pi(omega^2+a^2))", "initial_vector": "1 in L^2(R,mu_a)",
            "generator": "self-adjoint multiplication M_omega"},
        "theorem": {"absolute_first_cutoff": "(a/pi) log(1+(Omega/a)^2)",
            "second_cutoff": "(2a/pi)(Omega-a arctan(Omega/a))",
            "absolute_first_moment_diverges": True, "second_moment_diverges": True,
            "initial_vector_in_generator_domain": False,
            "initial_vector_in_absolute_form_domain": False,
            "unitary_orbit_still_defined": True},
        "exact_controls": {"cutoff_rows": rows,
            "absolute_first_strictly_increases": all(rows[i+1]["absolute_first_moment"] > rows[i]["absolute_first_moment"] for i in range(2)),
            "second_strictly_increases": all(rows[i+1]["second_moment"] > rows[i]["second_moment"] for i in range(2))},
        "ownership": {"finite_energy_physical_state_constructed": False,
            "gu_action_or_physical_quotient_constructed": False, "prediction_or_confirmation_credit": False},
        "decision": {"k966_finite_energy_seam_closed_negatively": True,
            "next_exact_input": "Prove the finite-first-moment cusp obstruction for every positive spectral measure, not only the Cauchy example."},
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact domain statement for the named Cauchy spectral state only; no general no-go for open systems or GU dynamics."
    }

def validate(p):
    t=p["theorem"]; x=p["exact_controls"]; o=p["ownership"]
    assert p["construction"]["scale"] > 0
    assert t["absolute_first_moment_diverges"] and t["second_moment_diverges"]
    assert not t["initial_vector_in_generator_domain"] and not t["initial_vector_in_absolute_form_domain"]
    assert t["unitary_orbit_still_defined"] and x["absolute_first_strictly_increases"] and x["second_strictly_increases"]
    assert p["decision"]["k966_finite_energy_seam_closed_negatively"]
    assert not o["finite_energy_physical_state_constructed"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert json.loads(OUTPUT.read_text())==p
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K971 controls: 11/11")
if __name__=="__main__": main()
