#!/usr/bin/env python3
"""Exact local fermionic routing, physical future-input witness and resource bounds."""
import sympy as s
from fractions import Fraction as F
FAULTS=['ordinary_swap','missing_onsite','wrong_generator_sign','omit_routing','wrong_pulse_area','wrong_future_input']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    I=s.eye(2);N=s.diag(0,1);X=s.zeros(4);X[1,2]=X[2,1]=1
    FF=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]])
    if fault=='ordinary_swap':FF[3,3]=1
    G=s.kronecker_product(N,I)+s.kronecker_product(I,N)-X
    if fault=='missing_onsite':G=-X
    if fault=='wrong_generator_sign':G=s.kronecker_product(N,I)+s.kronecker_product(I,N)+X
    ck('generator_actual_fswap',G==s.eye(4)-FF)
    ck('generator_minimal_polynomial',G*G==2*G)
    ck('spectrum',G.eigenvals()=={s.Integer(0):2,s.Integer(2):2})
    NN=s.kronecker_product(N,I)+s.kronecker_product(I,N)
    ck('number_conservation',G*NN==NN*G)
    # Because G^2=2G, this polynomial is exp(-i alpha G) at pi/2 or pi.
    gate=s.eye(4)-G if fault!='wrong_pulse_area' else s.eye(4)
    ck('actual_pulse_unitary',gate==FF)
    # Full occupation basis signs of an adjacent bubble versus the fermion permutation.
    for K in [2,3,4]:
        labels=list(range(K-1,-1,-1));edges=[]
        for k in range(1,K):
            start=K-1-k
            for e in range(start,K-1):edges.append(e);labels[e],labels[e+1]=labels[e+1],labels[e]
        ck('routing_temporal_order_'+str(K),labels==list(range(K)))
        ck('routing_gate_count_'+str(K),len(edges)==K*(K-1)//2)
        actual_edges=edges[:-1] if fault=='omit_routing' else edges
        for mask in range(2**K):
            bits=[(mask>>(K-1-i))&1 for i in range(K)];orig=bits[:];sign=1
            for e in actual_edges:
                sign*=int(FF[3,3]) if bits[e] and bits[e+1] else 1
                bits[e],bits[e+1]=bits[e+1],bits[e]
            occ=sum(orig);expected=(-1)**(occ*(occ-1)//2)
            ck('fock_permutation_'+str((K,mask)),bits==orig[::-1] and sign==expected)
    c=s.Rational(3,5);t=s.Rational(4,5);U=s.eye(4);U[1,1]=U[2,2]=c;U[1,2]=U[2,1]=-s.I*t
    plus=s.ones(2)/2;bath=s.diag(s.Rational(4,5),s.Rational(1,5))
    final=[]
    for q in [0,1]:
        inp=s.diag(1-q,q) if fault!='wrong_future_input' else s.diag(1,0)
        rho=s.kronecker_product(inp,plus,bath);V=s.kronecker_product(I,U);Z=s.kronecker_product(FF,I)
        rho=V*rho*V.H;rho=Z*rho*Z.H;rho=V*rho*V.H
        marg=s.Matrix(2,2,lambda a,b:sum(rho[4*a+j,4*b+j] for j in range(4)))
        target=s.Matrix([[s.Rational(173,250),(-1)**q*s.Rational(3,10)],[(-1)**q*s.Rational(3,10),s.Rational(77,250)]])
        ck('actual_future_input_marginal_'+str(q),s.simplify(marg-target)==s.zeros(2));final.append(marg)
    ck('future_input_trace_distance',sum(abs(x)*m for x,m in (final[0]-final[1]).eigenvals().items())/2==s.Rational(3,5))
    ck('causal_triangle_floor',F(3,5)/2==F(3,10))
    ck('gate_area_budget',45*2*F(5,10**6)==F(45,100000))
    off=2000000*F(1,10**13)*45*F(22,7)
    ck('residual_hopping_budget',off<F(28286,10**9))
    ck('complete_consumer',F(4501,10**6)+F(45,100000)+off<F(5,1000))
    ck('site_count',2000001+10-1==2000010)
    return out

RESULT='K2252'
REPORT='lab/process/k2252-adaptive-reset-interface.json'
DEPS=['explorations/conditional-build/k2252-adaptive-reset-interface-2026-10-29.md','explorations/conditional-build/k2250-quantum-stream-interface-2026-10-29.md']
EVIDENCE='Finite exact algebra and rational arithmetic; general circuit/causality proofs are written mathematics. Hash checks report integrity.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    args=argparse.ArgumentParser();args.add_argument('--write',action='store_true');a=args.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected mathematical input fault',fault)
        faults[fault]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'certificate drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
