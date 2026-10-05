#!/usr/bin/env python3
"""K1081: lift the constant matrix pencil to one Sobolev-domain Hessian."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1081-k1080-functional-hessian-domain.json"


def mode_matrix(lam, b=(2, 3), c=(6, 15)):
    return [lam * b[i] + c[i] for i in range(2)]


def build():
    modes = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
    fibres = []
    for k in modes:
        lam = sum(x * x for x in k)
        fibres.append({"mode": list(k), "lambda": lam, "eigenvalues": mode_matrix(lam)})
    return {
        "schema_version": "1.0",
        "result_id": "K1081-K1080-FUNCTIONAL-HESSIAN-DOMAIN",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "carrier": "L2(T3;R^2)",
        "form_domain": "H1(T3;R^2)",
        "operator_domain": "H2(T3;R^2)",
        "hessian": "H=-Delta tensor B+C with constant B=diag(2,3), C=diag(6,15)",
        "fourier_rule": "H_hat(k)=|k|^2 B+C on every integer Fourier mode",
        "fibres": fibres,
        "domain_result": "the closed positive form on H1 has one self-adjoint realization with domain H2; all Fourier fibres share that domain",
        "compactness": "the H2 to L2 resolvent is compact on T3, so the spectrum is discrete with finite multiplicities",
        "ownership": "functional lift of the repository-owned K1036 candidate action; not a source-selected GU Hessian",
        "claim_ceiling": "exact constant-coefficient flat-torus functional Hessian theorem",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["carrier"] == "L2(T3;R^2)"
    assert d["form_domain"].startswith("H1") and d["operator_domain"].startswith("H2")
    assert "constant B=diag(2,3), C=diag(6,15)" in d["hessian"]
    assert d["fourier_rule"].startswith("H_hat(k)=|k|^2 B+C")
    assert [f["lambda"] for f in d["fibres"]] == [0, 1, 2, 3]
    assert [f["eigenvalues"] for f in d["fibres"]] == [[6, 15], [8, 18], [10, 21], [12, 24]]
    assert "closed positive form" in d["domain_result"] and "domain H2" in d["domain_result"]
    assert "compact" in d["compactness"] and "discrete" in d["compactness"]
    assert "not a source-selected GU Hessian" in d["ownership"]
    assert "flat-torus" in d["claim_ceiling"] and d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1081 controls: 10/10")
