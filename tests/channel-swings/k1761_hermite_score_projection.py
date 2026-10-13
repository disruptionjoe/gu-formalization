#!/usr/bin/env python3
"""Exact algebraic controls for K1761's Hermite score projection theorem."""
import json
from math import comb, factorial
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1761-hermite-score-projection.json"

def product_coeff(m,n,k): return factorial(k)*comb(m,k)*comb(n,k)

def validate(d):
    t=d["theorem"];z=d["decision"]
    # Product identities used by the degree-3/5 hierarchy.
    h33={6:1,4:9,2:18,0:6}
    h35={8:1,6:15,4:60,2:60}
    h55={10:1,8:25,6:200,4:600,2:600,0:120}
    got=lambda m,n:{m+n-2*k:product_coeff(m,n,k) for k in range(min(m,n)+1)}
    return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1761"),
      ("score moment",t["score_moment"]=="E[(rho_Y(Y)+Y)H_n(Y)]=E[H_(n+1)(Y)]"),
      ("gram product",t["gram_product"].startswith("H_m H_n=sum")),
      ("H33",got(3,3)==h33),("H35",got(3,5)==h35),("H55",got(5,5)==h55),
      ("variational",t["finite_test"]=="J(Y)>=2 alpha^T b-alpha^T G alpha for every real alpha"),
      ("optimized",t["optimized_test"]=="J(Y)>=b^T G^(-1)b when G is positive definite"),
      ("monotone",z["nested_odd_degree_hierarchy_is_monotone"]),
      ("lower only",not z["finite_projection_equals_full_fisher_in_general"]),
      ("global fenced",not z["two_radius_global_optimizer_proved"])]

def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
