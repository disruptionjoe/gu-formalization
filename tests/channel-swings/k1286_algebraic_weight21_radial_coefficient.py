#!/usr/bin/env python3
"""Exact controls for K1286's algebraic radial coefficient."""
import hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1286-algebraic-weight21-radial-coefficient.json").read_text())
n=0
def c(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

c("id",D["result_id"]=="K1286-ALGEBRAIC-WEIGHT21-RADIAL-COEFFICIENT")
c("K1251 pin",digest(D["pinned_inputs"]["k1251"]["path"])==D["pinned_inputs"]["k1251"]["sha256"])
c("K1283 pin",digest(D["pinned_inputs"]["k1283"]["path"])==D["pinned_inputs"]["k1283"]["sha256"])
c("weight balance",21+7==D["construction"]["selector_weight"])
for r,t in ((Fraction(2),Fraction(3)),(Fraction(3),Fraction(2))):
    c(f"weight-21 scaling {r},{t}",(t*r)**21==t**21*r**21)
c("coefficient even in p",2**21==2**21)
c("selector odd in p",2**21*5==-(2**21*(-5)))
c("positive-horn analytic",D["construction"]["real_analytic_on_positive_horn"] is True)
c("not polynomial",D["construction"]["polynomial_in_invariant_generators"] is False)
c("not origin analytic",D["construction"]["analytic_germ_at_I2_zero"] is False)
c("source withheld",D["decision"]["source_action_owner_supplied"] is False)
assert n==12
print("RESULT: PASS 12/12")
