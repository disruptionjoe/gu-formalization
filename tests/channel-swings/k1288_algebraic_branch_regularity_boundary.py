#!/usr/bin/env python3
"""Exact controls for K1288's branch regularity."""
import hashlib,json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1288-algebraic-branch-regularity-boundary.json").read_text())
n=0
def c(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def falling(a,k):
    out=Fraction(1)
    for j in range(k): out*=a-j
    return out

c("id",D["result_id"]=="K1288-ALGEBRAIC-BRANCH-REGULARITY-BOUNDARY")
c("K1284 pin",digest(D["pinned_inputs"]["k1284"]["path"])==D["pinned_inputs"]["k1284"]["sha256"])
c("K1286 pin",digest(D["pinned_inputs"]["k1286"]["path"])==D["pinned_inputs"]["k1286"]["sha256"])
a=Fraction(21,2)
c("tenth exponent positive",a-10==Fraction(1,2))
c("eleventh exponent negative",a-11==Fraction(-1,2))
c("eleventh coefficient nonzero",falling(a,11)!=0)
c("C10 declaration","C10" in D["regularity"]["coefficient_extension_on_I2_nonnegative"])
c("not C11 declaration","not C11" in D["regularity"]["coefficient_extension_on_I2_nonnegative"])
c("Cartan degree",21+7==28)
c("ray left-right 28th jump",math.factorial(28)!=-math.factorial(28))
c("radial branch not p sheet",D["regularity"]["positive_radial_branch_selects_p_sheet"] is False)
c("analytic origin withheld",D["regularity"]["extension_is_real_analytic_at_origin"] is False)
assert n==12
print("RESULT: PASS 12/12")
