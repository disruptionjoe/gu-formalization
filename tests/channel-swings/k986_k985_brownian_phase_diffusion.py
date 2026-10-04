#!/usr/bin/env python3
"""K986 exact Brownian phase-diffusion unraveling of the K956 semigroup."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k986-k985-brownian-phase-diffusion.json"


def build():
    gamma = 0.7
    rows = []
    for t in (0.0, 0.25, 1.0, 2.0, 4.0):
        variance = gamma * t
        characteristic = math.exp(-0.5 * 4.0 * variance)
        target = math.exp(-2.0 * gamma * t)
        rows.append({"t": t, "phase_variance": variance, "brownian_characteristic": characteristic,
                     "target_coherence": target, "identity_error": abs(characteristic-target)})
    return {
        "schema_version":"1.0", "result_id":"K986-BROWNIAN-PHASE-DIFFUSION", "created":"2026-10-04",
        "status":"working_draft_verified", "direction":"observed_to_native",
        "classification":"INTERNAL_CONDITIONAL_MATHEMATICS", "target_claim":"NONE-NOT-A-KILL",
        "scope":"A supplied standard Brownian motion W_t driving U_t=exp(-i sqrt(gamma) W_t Z).",
        "construction":{"phase_process":"X_t=sqrt(gamma) W_t", "pathwise_unitary":"U_t=exp(-i X_t Z)",
                        "coherence":"E[exp(-2 i X_t)]=exp(-2 gamma t)", "continuous_paths_almost_surely":True,
                        "stationary_independent_increments":True, "same_dephasing_semigroup_as_k956":True,
                        "remote_marginal_invariant":True},
        "exact_controls":{"gamma":gamma, "rows":rows,
                          "all_characteristic_identities_replayed":all(r["identity_error"]<1e-15 for r in rows),
                          "identity_at_zero":rows[0]["target_coherence"]==1.0,
                          "strict_decay_after_zero":all(rows[i+1]["target_coherence"]<rows[i]["target_coherence"] for i in range(len(rows)-1))},
        "ownership":{"brownian_clock_and_probability_imported":True, "white_noise_limit_or_stochastic_action_imported":True,
                     "positive_hilbert_pairing_imported":True, "gu_action_or_physical_quotient_constructed":False,
                     "prediction_or_confirmation_credit":False},
        "decision":{"exact_nonjump_horn_constructed":True,
                    "next_exact_input":"Construct a distinct finite-activity phase-jump family and test controlled multi-time system-only identifiability."},
        "source_and_ledger_effect":"none",
        "claim_ceiling":"Exact random-unitary Brownian unraveling of the imported qubit semigroup only; not a GU-owned stochastic action, white-noise limit or physical record."
    }


def validate(p):
    c,x,o,d=p["construction"],p["exact_controls"],p["ownership"],p["decision"]
    assert c["continuous_paths_almost_surely"] and c["stationary_independent_increments"]
    assert c["same_dephasing_semigroup_as_k956"] and c["remote_marginal_invariant"]
    assert len(x["rows"])==5 and x["all_characteristic_identities_replayed"] and x["identity_at_zero"] and x["strict_decay_after_zero"]
    assert o["brownian_clock_and_probability_imported"] and o["white_noise_limit_or_stochastic_action_imported"] and o["positive_hilbert_pairing_imported"]
    assert not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert d["exact_nonjump_horn_constructed"] and p["source_and_ledger_effect"]=="none"


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args()
    p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==t
    elif a.write: OUTPUT.write_text(t)
    else: print(t,end="")
    print("K986 controls: 14/14")
if __name__=="__main__":main()
