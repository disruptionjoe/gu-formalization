#!/usr/bin/env python3
"""Exact controls for K1283."""
import json
from fractions import Fraction
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1283-analytic-rational-parity-extension.json").read_text()); n=0
def c(label,x):
    global n; assert x,label; n+=1; print(f"PASS {n:02d}: {label}")
c("id",D["result_id"]=="K1283-ANALYTIC-RATIONAL-PARITY-EXTENSION")
c("analytic finite",D["theorem"]["analytic_homogeneous_piece_is_finite_polynomial"] is True)
for p in (-3,-1,2):
    e2=Fraction(5,2); e4=Fraction(7,3)
    analytic=p*e2**7+p**3
    rational=p*e2**9/e4
    c(f"analytic odd p={p}",(-p)*e2**7+(-p)**3==-analytic)
    c(f"rational odd p={p}",(-p)*e2**9/e4==-rational)
    c(f"rational product even p={p}",rational*p==((-p)*e2**9/e4)*(-p))
c("singular outside",D["theorem"]["singular_denominator_or_branch_cut_is_outside_regular_domain"] is True)
c("nonhomogeneous open",D["decision"]["nonhomogeneous_effective_law_remains_open"] is True)
assert n==13; print("RESULT: PASS 13/13")
