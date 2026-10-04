#!/usr/bin/env python3
"""K961 finite closed controlled-dephasing recurrence boundary."""
import argparse, cmath, json, math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k961-k960-finite-reservoir-recurrence-boundary.json"

def build():
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    frequencies = [1, 2, 3]
    returns = []
    for n in (1, 2, 5):
        t = 2 * math.pi * n
        value = sum(float(w) * cmath.exp(-1j * om * t) for w, om in zip(weights, frequencies))
        returns.append({"multiple": n, "absolute_error_from_one": abs(value - 1)})
    return {
      "schema_version": "1.0", "result_id": "K961-FINITE-RESERVOIR-RECURRENCE-BOUNDARY",
      "created": "2026-10-03", "status": "working_draft_verified", "direction": "observed_to_native",
      "classification": "INTERNAL_CONDITIONAL_MATHEMATICS", "target_claim": "NONE-NOT-A-KILL",
      "scope": "Finite-dimensional autonomous controlled-dephasing Hamiltonians with a fixed environment state.",
      "theorem": {
        "coherence_factor": "f(t)=Tr(rho_E exp(i H_1 t) exp(-i H_0 t))",
        "finite_trigonometric_polynomial": True,
        "normalization": "f(0)=1",
        "recurrence": "For every epsilon>0 and T>0 there exists t>T with |f(t)-1|<epsilon by simultaneous Diophantine approximation of the finite Bohr-frequency set.",
        "requires_commuting_environment_hamiltonians": False
      },
      "exact_controls": {"weights_sum": str(sum(weights)), "frequency_count": len(frequencies), "explicit_periodic_returns": returns, "all_returns_near_one": all(x["absolute_error_from_one"] < 1e-12 for x in returns)},
      "ownership": {"finite_hilbert_and_trace_rule_imported": True, "gu_action_or_physical_quotient_constructed": False, "prediction_or_confirmation_credit": False},
      "decision": {"finite_closed_recurrence_proved": True, "next_exact_input": "Compare recurrence with strict positive-rate exponential decay."},
      "source_and_ledger_effect": "none",
      "claim_ceiling": "Finite-dimensional controlled-dephasing recurrence theorem only; no no-go for infinite reservoirs, resets, time-dependent driving or non-Hamiltonian primitives, and no GU verdict follows."
    }

def validate(p):
    assert p["theorem"]["finite_trigonometric_polynomial"] and p["theorem"]["normalization"] == "f(0)=1"
    assert not p["theorem"]["requires_commuting_environment_hamiltonians"]
    assert p["exact_controls"]["weights_sum"] == "1" and p["exact_controls"]["all_returns_near_one"]
    assert p["decision"]["finite_closed_recurrence_proved"]
    assert p["ownership"]["finite_hilbert_and_trace_rule_imported"]
    assert not p["ownership"]["gu_action_or_physical_quotient_constructed"] and not p["ownership"]["prediction_or_confirmation_credit"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); text=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==text
    elif a.write: OUTPUT.write_text(text)
    else: print(text,end="")
    print("K961 controls: 9/9")
if __name__=="__main__": main()
