#!/usr/bin/env python3
"""Independent K239 90-monomial weighted integration and hostile measure control."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
import json
from math import log

from k239_order_six_projected_quartic_cube_moment import OUT


def add(*polys):
    return tuple(sum((p[k] if k < len(p) else Q() for p in polys), Q())
                 for k in range(max(map(len, polys))))


def mul(a, b):
    return tuple(sum((a[i]*b[k-i] for i in range(max(0,k-len(b)+1),min(k,len(a)-1)+1)),Q())
                 for k in range(len(a)+len(b)-1))


def raw_centered_integrals(row):
    m0 = Q(row["m0"])
    m1 = (Q(row["m1_constant"]), Q(row["m1_log_coefficient"]))
    m2 = Q(row["m2"])
    b = tuple(map(Q,row["center_b_coefficients_in_log_q"]))
    centered0 = (m0,)
    centered1 = add(m1,tuple(-m0*v for v in b))
    centered2 = add((m2,), tuple(-2*v for v in mul(b,m1)),
                    tuple(m0*v for v in mul(b,b)))
    assert centered1 == (Q(),Q())
    return (centered0,centered1,centered2)


def enumerate_P(moments, diagonal_weight=Q(1)):
    total = (Q(),)
    def term(coefficient, powers):
        p = (coefficient,)
        for degree in powers:
            p = mul(p,moments[degree])
        return p
    for i,j in combinations(range(6),2):
        powers=[0]*6; powers[i]=powers[j]=2
        total=add(total,term(diagonal_weight,powers))
    for i in range(6):
        for j,k in combinations([r for r in range(6) if r!=i],2):
            powers=[0]*6; powers[i]=2; powers[j]=powers[k]=1
            total=add(total,term(-Q(1,2),powers))
    for indices in combinations(range(6),4):
        total=add(total,term(Q(1),[int(i in indices) for i in range(6)]))
    return total


def check():
    result=json.loads(OUT.read_text())
    assert result["classification"]=="INTERNAL_STRUCTURAL_ONLY"
    for row in result["cubes"]:
        q=row["q"]; T=log(q)
        s=Q(q*q-1,2*q)
        c=Q(q*q+1,2*q)
        assert Q(row["m0"])==s and Q(row["cosh_T"])==c
        assert Q(row["m1_constant"])==s*c/2
        assert Q(row["m2"])==s+s**3/3
        moments=raw_centered_integrals(row)
        exact=enumerate_P(moments)
        expected=tuple(map(Q,row["weighted_six_coordinate_P_moment_coefficients_in_log_q"]))
        assert exact==expected
        assert enumerate_P(moments,Q())!=expected  # hostile dropped m22
        numerical=sum(float(v)*T**k for k,v in enumerate(expected))
        assert numerical>0
        # Wrong uniform-c density would give M0=cosh(T)-1, not sinh(T).
        assert s!=c-1
    print("[PASS] K239 independent weighted 90-monomial integration, q=4,5")


if __name__=="__main__":
    check()
