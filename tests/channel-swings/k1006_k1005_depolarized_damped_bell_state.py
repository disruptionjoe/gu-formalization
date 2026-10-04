#!/usr/bin/env python3
"""K1006: exact spectrum of an isotropically depolarized damped Bell state."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1006-k1005-depolarized-damped-bell-state.json"

def q(x: F) -> str:
    return str(x)

def spectrum(p: F, lam: F) -> list[F]:
    return [(1+p+2*p*lam)/4, (1+p-2*p*lam)/4, (1-p)/4, (1-p)/4]

def build():
    p, lam = F(4, 5), F(2, 5)
    return {
        "schema_version": "1.0",
        "result_id": "K1006-K1005-DEPOLARIZED-DAMPED-BELL-STATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "target_claim": "NONE-NOT-A-KILL",
        "state": "rho_(p,lambda)=p rho_lambda+(1-p)I_4/4",
        "parameter_domain": ["0<=p<=1", "0<=lambda<=1"],
        "state_spectrum": ["(1+p+2p lambda)/4", "(1+p-2p lambda)/4", "(1-p)/4", "(1-p)/4"],
        "correlation_tensor": "p diag(lambda,-lambda,1)",
        "exact_control": {
            "p": q(p), "lambda": q(lam),
            "spectrum": [q(x) for x in spectrum(p, lam)],
            "trace": q(sum(spectrum(p, lam))),
            "correlation_diagonal": [q(p*lam), q(-p*lam), q(p)],
        },
        "ownership": {
            "isotropic_contrast_is_repository_selected": True,
            "gu_action_or_physical_quotient_constructed": False,
            "prediction_or_confirmation": False,
        },
        "claim_ceiling": "Exact density and correlation spectrum for the repository-selected two-parameter noisy K956 control only; no GU-native state, action, detector or empirical claim.",
    }

def validate(x):
    assert x["state"] == "rho_(p,lambda)=p rho_lambda+(1-p)I_4/4"
    assert len(x["state_spectrum"]) == 4
    assert x["correlation_tensor"] == "p diag(lambda,-lambda,1)"
    c = x["exact_control"]
    assert c["p"] == "4/5" and c["lambda"] == "2/5"
    assert c["spectrum"] == ["61/100", "29/100", "1/20", "1/20"]
    assert c["trace"] == "1" and c["correlation_diagonal"] == ["8/25", "-8/25", "4/5"]
    assert x["ownership"]["isotropic_contrast_is_repository_selected"]
    assert not x["ownership"]["gu_action_or_physical_quotient_constructed"]
    assert not x["ownership"]["prediction_or_confirmation"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    x=build(); validate(x); text=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(text)
    elif a.check: assert OUTPUT.read_text()==text
    else: print(text,end="")
    print("K1006 controls: 14/14")

if __name__ == "__main__": main()
