#!/usr/bin/env python3
"""Exact Clifford-word identities for positive Riemannian RS symbols.

Exact local controls only. The L2 spectral conclusion uses the analytic
proof in homogeneous-localization-comparator-2026-11-24.md, not this probe.
"""
from fractions import Fraction as F
import json


def add(*terms):
    out = {}
    for term in terms:
        for word, coefficient in term.items():
            out[word] = out.get(word, F(0)) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def scale(value, scalar):
    return {word: coefficient * scalar for word, coefficient in value.items()
            if coefficient * scalar}


def left_gamma(index, value):
    """e_i e_j + e_j e_i = -2 delta_ij, ordered exterior bit words."""
    out = {}
    bit = 1 << index
    for word, coefficient in value.items():
        swaps = (word & (bit - 1)).bit_count()
        sign = -1 if swaps % 2 else 1
        if word & bit:
            sign = -sign
        out[word ^ bit] = out.get(word ^ bit, F(0)) + sign * coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def gamma_trace(field):
    return add(*(left_gamma(a, value) for a, value in enumerate(field)))


def project(field):
    n = len(field)
    trace = gamma_trace(field)
    return [add(value, scale(left_gamma(a, trace), F(1, n)))
            for a, value in enumerate(field)]


def j_map(spinor, n):
    raw = [{} for _ in range(n)]
    raw[0] = spinor
    return project(raw)


def q_symbol(field):
    return project([left_gamma(0, value) for value in field])


def check_dimension(n):
    one = {0: F(1)}
    j = j_map(one, n)
    alpha = F(n - 2, n)
    assert not gamma_trace(j)
    assert q_symbol(j) == [scale(value, alpha)
                           for value in j_map(left_gamma(0, one), n)]
    assert j[0] == scale(one, F(n - 1, n))
    for b in range(n):
        raw = [{} for _ in range(n)]
        raw[b] = one
        field = project(raw)
        assert not gamma_trace(field)
        assert project(field) == field
        assert not gamma_trace(q_symbol(field))
        square = q_symbol(q_symbol(field))
        correction = j_map(field[0], n)
        for a in range(n):
            assert not add(square[a], field[a], scale(correction[a], F(-4, n)))
    spin_rank = 2 ** (n // 2)
    return {"n": n, "spin_rank": spin_rank, "rs_rank": (n - 1) * spin_rank,
            "longitudinal_rank": spin_rank, "transverse_rank": (n - 2) * spin_rank,
            "reduced_symbol_factor": str(alpha), "reduced_square": str(alpha * alpha),
            "elliptic": n > 2, "identities": "exact Clifford word algebra"}



def reconciliation_controls():
    import sympy as sp
    from collections import Counter
    def e(i,j):
        a=sp.zeros(4);a[i,j]=1;return a
    sl=[e(i,j) for i in range(4) for j in range(4) if i!=j]
    sl += [e(i,i)-e(3,3) for i in range(3)]
    eta=sp.diag(1,1,1,-1)
    def dims(sigma):
        fixed=sp.Matrix.hstack(*[(sigma(x)-x).reshape(16,1) for x in sl])
        anti=sp.Matrix.hstack(*[(sigma(x)+x).reshape(16,1) for x in sl])
        return [15-fixed.rank(),15-anti.rank()]
    wrong=dims(lambda x:eta*x*eta)
    metric=dims(lambda x:-eta*x.T*eta)
    assert wrong==[9,6] and metric==[6,9]
    cartan=sl[-3:]
    assert len(cartan)==3
    assert all(x==x.T and -eta*x.T*eta==-x for x in cartan)
    assert all(a*b==b*a for a in cartan for b in cartan)
    roots=[]
    for i in range(4):
        for j in range(i+1,4):
            v=[0]*4;v[i]=1;v[j]=-1;roots.append(v)
    rho=[sum(v[i] for v in roots)*sp.Rational(1,2) for i in range(4)]
    assert rho==[sp.Rational(3,2),sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(3,2)]
    assert sum(v*v for v in rho)==5
    h=[1,0,0,-1]
    weights=Counter(h[i]-h[j] for i in range(4) for j in range(4) if h[i]>h[j])
    assert dict(weights)=={1:4,2:1} and dict(weights)!={1:7,2:1}
    sym=[e(i,i) for i in range(4)]+[e(i,j)+e(j,i) for i in range(4) for j in range(i+1,4)]
    def form(g,u,v):return sp.trace(g*u*g*v)-sp.Rational(1,2)*sp.trace(g*u)*sp.trace(g*v)
    def signature(g):
        gram=sp.Matrix([[form(g,u,v) for v in sym] for u in sym])
        eig=gram.eigenvals()
        return [sum(mult for val,mult in eig.items() if val>0),sum(mult for val,mult in eig.items() if val<0)]
    assert signature(eta)==[6,4]
    assert signature(sp.eye(4))==[9,1]
    assert form(eta,eta,eta)==-4
    # Failure control: elliptic full symbol does not ensure elliptic compression.
    p=sp.diag(1,0);d=sp.Matrix([[0,1],[1,0]])
    assert d.det()!=0 and p*d*p==sp.zeros(2)
    assert p.rank()==1 and len(p.nullspace())==1
    # A finite Fredholm complex with index0 and paired kernels.
    a=sp.diag(0,1)
    kernel=len(a.nullspace());cokernel=len(a.T.nullspace())
    assert kernel==cokernel==1 and kernel-cokernel==0
    return {'wrong_involution_fixed_anti':wrong,'metric_involution_fixed_anti':metric,
            'metric_split_cartan_dimension':3,'ordinary_Cartan_ranks':[3,2],
            'positive_A3_roots':len(roots),'rho':[str(v) for v in rho],
            'rho_squared_root_length2_normalization':5,'line_positive_weights':dict(weights),
            'native_scale_norm':-4,'trace_reversed_signatures':{'Lorentz_base':[6,4],'Euclidean_base':[9,1]},
            'failure_controls':['wrong involution does not fix so31','rank-one multiplicities are not7,1',
                                'elliptic symbol can have zero compressed symbol','index0 permits paired zero modes'],
            'ceiling':'finite algebra only; rho norm is not a physical spectral gap'}


def run():
    results=[check_dimension(n) for n in (2,9,10,14)]
    assert all(not value for value in q_symbol(j_map({0:F(1)},2)))
    assert any(j_map({0:F(1)},2))
    # On the full vector-spinor space the complement of P is a spurious zero sector.
    for n in (9,10,14):
        inclusion=[scale(left_gamma(a,{0:F(1)}),F(-1,n)) for a in range(n)]
        assert gamma_trace(inclusion)=={0:F(1)}
        assert all(not v for v in project(inclusion))
    return {'status':'PASS','rs_symbol_cases':results,'reconciliation':reconciliation_controls(),
            'ceiling':'Exact local algebra; analytic theorem and domain proof are in the result artifact. No native spectral gap or P3 decision.'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
