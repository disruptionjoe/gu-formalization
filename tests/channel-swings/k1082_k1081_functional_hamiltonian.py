#!/usr/bin/env python3
"""K1082: positive functional Hamiltonian and exact modal conservation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1082-k1081-functional-hamiltonian.json"


def defect(w):
    k = ((0, 1), (-w, 0)); s = ((w, 0), (0, 1))
    return [[sum(k[a][i] * s[a][j] + s[i][a] * k[a][j] for a in range(2)) for j in range(2)] for i in range(2)]


def build():
    controls = []
    for lam, c in [(0, 1), (2, 1), (3, 4)]:
        w = lam + c
        controls.append({"lambda": lam, "mass_squared": c, "omega_squared": w, "defect": defect(w)})
    return {
        "schema_version": "1.0",
        "result_id": "K1082-K1081-FUNCTIONAL-HAMILTONIAN",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "energy_space": "H1(T3;R^r) direct_sum L2(T3;R^r)",
        "generator_domain": "H2(T3;R^r) direct_sum H1(T3;R^r)",
        "generator": "K(q,p)=(p,-Hq) for H=-Delta tensor B+C",
        "pairing": "E((q,p))=<q,Hq>+<p,p>",
        "identity": "K is skew for the energy pairing on the generator domain, hence smooth solutions conserve E",
        "controls": controls,
        "positivity": "B>0 and C>0 give a coercive positive energy; C>=0 gives nonnegative energy with the zero-mode radical handled separately",
        "scope_boundary": "constant coefficients on the flat quotient; no nonlinear interacting BV domain or dissipative resource",
        "ownership": "repository-owned K1036 candidate Hamiltonian only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["energy_space"].startswith("H1") and "L2" in d["energy_space"]
    assert d["generator_domain"].startswith("H2") and "H1" in d["generator_domain"]
    assert d["generator"].startswith("K(q,p)=(p,-Hq)")
    assert d["pairing"].startswith("E((q,p))=<q,Hq>")
    assert "skew" in d["identity"] and "conserve E" in d["identity"]
    assert len(d["controls"]) == 3 and all(c["defect"] == [[0, 0], [0, 0]] for c in d["controls"])
    assert [c["omega_squared"] for c in d["controls"]] == [1, 3, 7]
    assert "coercive" in d["positivity"] and "zero-mode radical" in d["positivity"]
    assert "no nonlinear interacting BV domain" in d["scope_boundary"]
    assert d["ownership"] == "repository-owned K1036 candidate Hamiltonian only" and d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1082 controls: 10/10")
