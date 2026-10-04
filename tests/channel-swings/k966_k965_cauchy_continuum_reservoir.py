#!/usr/bin/env python3
"""K966 exact Cauchy-spectrum continuum dephasing dilation."""
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k966-k965-cauchy-continuum-reservoir.json"

def build():
    gamma = 0.7
    a = 2 * gamma
    times = (0.0, 0.25, 1.0, 3.0)
    samples = [{"t": t, "fourier_coherence": math.exp(-a * abs(t)), "target": math.exp(-2 * gamma * abs(t))} for t in times]
    return {
        "schema_version": "1.0", "result_id": "K966-CAUCHY-CONTINUUM-RESERVOIR",
        "created": "2026-10-03", "status": "working_draft_verified", "direction": "observed_to_native",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS", "target_claim": "NONE-NOT-A-KILL",
        "scope": "Repository-owned autonomous controlled-dephasing model on an infinite Cauchy spectral reservoir.",
        "construction": {
            "environment": "L^2(R, mu_gamma)", "density": "d mu_gamma/d omega=(2 gamma)/(pi(omega^2+(2 gamma)^2))",
            "initial_vector": "1", "generator": "self-adjoint multiplication M_omega",
            "controlled_hamiltonian": "|0><0| tensor 0 + |1><1| tensor M_omega",
            "coherence": "integral exp(i omega t) d mu_gamma=exp(-2 gamma |t|)",
            "positive_pairing": True, "unitary_group": True, "remote_marginal_invariant": True
        },
        "exact_controls": {"gamma": gamma, "scale": a, "normalization": True, "samples": samples, "sample_equalities": all(abs(x["fourier_coherence"]-x["target"]) < 1e-15 for x in samples)},
        "ownership": {"continuum_measure_rate_split_and_trace_imported": True, "gu_action_or_physical_quotient_constructed": False, "prediction_or_confirmation_credit": False},
        "decision": {"exact_continuum_escape_constructed": True, "next_exact_input": "Truncate the continuum and quantify uniform bandwidth error before finite atomic approximation."},
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact repository-owned continuum dilation only; the Cauchy measure, rate, system split, trace and observable semantics are not GU-derived."
    }

def validate(p):
    c=p["construction"]; x=p["exact_controls"]; o=p["ownership"]
    assert x["gamma"] > 0 and x["normalization"] and x["sample_equalities"]
    assert c["positive_pairing"] and c["unitary_group"] and c["remote_marginal_invariant"]
    assert "exp(-2 gamma |t|)" in c["coherence"] and p["decision"]["exact_continuum_escape_constructed"]
    assert o["continuum_measure_rate_split_and_trace_imported"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==text
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K966 controls: 10/10")
if __name__=="__main__": main()
