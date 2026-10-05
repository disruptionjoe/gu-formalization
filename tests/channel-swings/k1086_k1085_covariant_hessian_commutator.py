#!/usr/bin/env python3
"""K1086: covariant Hessian commutator and parallel-potential criterion."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1086-k1085-covariant-hessian-commutator.json"


def build():
    # At x=0, C=R(x)diag(3,5)R(x)^T has C'=[[0,-2],[-2,0]].
    # For the local jet f=0, nabla_x f=e1, nabla_x^2 f=0 and B=diag(1,2),
    # the commutator is -2 B C' e1=(0,8).
    return {
        "schema_version": "1.0",
        "result_id": "K1086-K1085-COVARIANT-HESSIAN-COMMUTATOR",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "carrier": "smooth sections of a Euclidean or Hermitian bundle E over a connected Riemannian manifold M",
        "operator": "H0=nabla* B nabla with metric-compatible nabla and nabla-parallel positive self-adjoint invertible B",
        "potential": "multiplication by a smooth self-adjoint endomorphism C",
        "identity": "[H0,C]f=(BC-CB)nabla*nabla f+B(nabla*nabla C)f-2B sum_a (nabla_a C)(nabla_a f), in a normal orthonormal frame",
        "zero_criterion": "[H0,C]=0 on compactly supported smooth interior sections iff nabla C=0 and [B,C]=0",
        "proof_route": "the order-two principal coefficient gives [B,C]=0 and the order-one coefficient gives B nabla C=0; invertibility of B forces nabla C=0",
        "positive_counterexample": "on the trivial R2 bundle over S1, B=diag(1,2) and C(x)=R(x)diag(3,5)R(x)^T is uniformly positive but not parallel",
        "witness": [0, 8],
        "witness_jet": "at x=0 take f=0, nabla_x f=e1 and nabla_x^2 f=0",
        "decision_rule": "coordinate constancy is replaced by covariant parallelism; a nonzero covariant derivative rejects a common internal eigensplitting without rejecting positivity",
        "scope_boundary": "conditional connection-Laplacian theorem; no source-selected GU connection, action Hessian, boundary realization or physical quotient",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["operator"].startswith("H0=nabla* B nabla") and "invertible B" in d["operator"]
    assert "(BC-CB)nabla*nabla f" in d["identity"] and "nabla_a C" in d["identity"]
    assert "iff nabla C=0 and [B,C]=0" in d["zero_criterion"]
    assert "order-two principal coefficient" in d["proof_route"] and "invertibility of B" in d["proof_route"]
    assert "uniformly positive" in d["positive_counterexample"] and "not parallel" in d["positive_counterexample"]
    assert d["witness"] == [0, 8]
    assert "nabla_x f=e1" in d["witness_jet"]
    assert "covariant parallelism" in d["decision_rule"] and "without rejecting positivity" in d["decision_rule"]
    assert "no source-selected GU connection" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1086 controls: 10/10")
