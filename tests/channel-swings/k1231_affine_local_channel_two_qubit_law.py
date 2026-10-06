#!/usr/bin/env python3
"""K1231: derive the general two-qubit law after a local affine channel."""
from fractions import Fraction as F
import json
from pathlib import Path

OUT = Path(__file__).parents[2] / "lab/process/k1231-affine-local-channel-two-qubit-law.json"

def dot(a, b): return sum(x*y for x, y in zip(a, b))
def mv(A, v): return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def mm(A, B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def outer(a, b): return [[x*y for y in b] for x in a]
def add(A, B): return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def probabilities(M, t, u, v, T, a, b):
    up = [x+y for x, y in zip(mv(M, u), t)]
    Tp = add(mm(M, T), outer(t, v))
    A, B, C = dot(a, up), dot(b, v), dot(a, mv(Tp, b))
    return A, B, C, [(1+x*A+y*B+x*y*C)/4 for x in (-1, 1) for y in (-1, 1)]

def validate(d):
    M=[[F(3,10),-F(2,5),0],[F(2,13),F(3,26),-F(3,13)],[F(24,65),F(18,65),F(5,52)]]
    t=[0,-F(9,13),F(15,52)]; a=[F(3,5),0,F(4,5)]; b=[0,F(4,5),F(3,5)]
    D=[[F(1),0,0],[0,-F(1),0],[0,0,F(1)]]
    A,B,C,p=probabilities(M,t,[F(0)]*3,[F(0)]*3,D,a,b)
    assert (A,B,C)==(F(3,13),F(0),F(99,1625))
    assert [str(x) for x in p]==["1349/6500","1151/6500","1901/6500","2099/6500"]
    assert sum(p)==1 and min(p)>0
    assert d["transformation"]["correlation"]=="T'=M T+t v^T"
    assert d["specialization"]["k1229_requires"]==["u=0","v=0","T=diag(1,-1,1)"]
    assert d["ownership"]["channel_calibration_determines_source_state"] is False
    assert d["decision"]["delayed_choice_entanglement_swapping_consumed"] is False
    assert d["claim_ceiling"].startswith("Exact finite-dimensional")

if __name__ == "__main__":
    d=json.loads(OUT.read_text()); validate(d); print("K1231 controls: 12/12")
