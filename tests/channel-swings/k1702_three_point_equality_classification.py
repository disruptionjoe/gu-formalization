#!/usr/bin/env python3
"""Exact algebraic controls for K1702."""
import json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1702-three-point-equality-classification.json").read_text())
    f, c, q = d["family"], d["classification"], d["decision"]
    s = math.sqrt(105)
    p_lo, p_star = (15-s)/60, (15+s)/60
    def k4(p): return 1/p-3
    def k6(p): return 1/p**2-15/p+30
    checks = [("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1702"),
        ("law", "p^(-1/2)" in f["law"]), ("variance", "E X^2=1" in f["moments"]),
        ("fourth moment", "E X^4=1/p" in f["moments"]), ("sixth moment", "E X^6=1/p^2" in f["moments"]),
        ("cumulants", "1/p^2-15/p+30" in f["cumulants"]), ("negative iff", "p>1/3" in f["negative_kurtosis"]),
        ("root equation", "y^2-15y+30=0" in c["root_equation"]), ("two roots", "15-sqrt(105)" in c["algebraic_roots"]),
        ("low root", 0 < p_lo < 1/3), ("star root", 1/3 < p_star < 1),
        ("roots cancel sixth", abs(k6(p_lo)) < 1e-10 and abs(k6(p_star)) < 1e-10),
        ("sign split", k4(p_lo) > 0 and k4(p_star) < 0),
        ("u star", math.isclose(-k4(p_star), (s-9)/2)), ("attainment", "c_*=1/4" in c["consequence"]),
        ("unique family", q["three_point_negative_kurtosis_equality_unique"]),
        ("not all unique", not q["all_distribution_equality_unique"]),
        ("finite open", not q["finite_strength_optimizer_identified"]),
        ("scope", "only inside the symmetric three-point family" in d["scope_guard"])]
    for n,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
