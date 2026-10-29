#!/usr/bin/env python3
"""Finite tensor channels, coherent controls and actual correlated-stock faults."""
import sympy as s
from fractions import Fraction as F
FAULTS=['wrong_area','wrong_donor','coherent_donor','omit_F_phase','correlated_stock','reuse_spent']
def trace_keep(M,keep,n):
    keep=list(keep);drop=[i for i in range(n) if i not in keep]
    def idx(a,b):
        bits=[0]*n
        for j,k in enumerate(keep):bits[k]=(a>>(len(keep)-1-j))&1
        for j,k in enumerate(drop):bits[k]=(b>>(len(drop)-1-j))&1
        return sum(v<<(n-1-i) for i,v in enumerate(bits))
    return s.Matrix(2**len(keep),2**len(keep),lambda a,c:sum(M[idx(a,b),idx(c,b)] for b in range(2**len(drop))))
def embed(U,sites,n):
    ans=s.zeros(2**n)
    for b in range(2**n):
        bits=[(b>>(n-1-j))&1 for j in range(n)];src=sum(bits[k]<<(len(sites)-1-j) for j,k in enumerate(sites))
        for a in range(2**len(sites)):
            bb=bits.copy()
            for j,k in enumerate(sites):bb[k]=(a>>(len(sites)-1-j))&1
            dest=sum(v<<(n-1-j) for j,v in enumerate(bb));ans[dest,b]+=U[a,src]
    return ans

def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    simp=lambda M:M.applyfunc(s.simplify)
    p=s.Rational(1,5);tau=s.diag(1-p,p);don=tau.copy()
    if fault=='wrong_donor':don=s.diag(s.Rational(7,10),s.Rational(3,10))
    if fault=='coherent_donor':don[0,1]=don[1,0]=s.Rational(1,10)
    FF=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]])
    gate=FF.copy()
    if fault=='wrong_area':gate=s.eye(4)
    if fault=='omit_F_phase':gate[3,3]=1
    G=s.eye(4)-gate;N=s.diag(0,1,1,2);X=s.Matrix([[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,0]])
    ck('positive_generator_identity',G==N-X);ck('generator_square',G*G==2*G);ck('number_conservation',G*N==N*G)
    ck('exact_F_gate',gate==FF)
    for i in range(2):
        for j in range(2):
            E=s.zeros(2);E[i,j]=1;z=gate*s.kronecker_product(E,don)*gate.H
            ck('complete_matrix_unit_'+str((i,j)),trace_keep(z,[0],2)==tau*int(i==j))
    bell=s.Matrix([1,0,0,1])/s.sqrt(2);rho=bell*bell.H
    # Order S,R,B; the gate touches S and B, preserving a true external reference.
    U=embed(gate,[0,2],3);z=U*s.kronecker_product(rho,don)*U.H
    ck('entangled_complete_reset',simp(trace_keep(z,[0,1],3))==s.kronecker_product(tau,s.eye(2)/2))
    plus=s.Matrix([1,1])/s.sqrt(2);inp=plus*plus.H;z=gate*s.kronecker_product(inp,don)*gate.H
    spent=trace_keep(z,[1],2);want=s.Matrix([[s.Rational(1,2),s.Rational(3,10)],[s.Rational(3,10),s.Rational(1,2)]])
    ck('spent_dephased_input',spent==want)
    fresh=spent if fault=='reuse_spent' else don
    vac=s.diag(1,0);z=gate*s.kronecker_product(vac,fresh)*gate.H
    ck('next_slot_fresh_reset',trace_keep(z,[0],2)==tau)
    corr=s.diag(1-p,0,0,p);prod=s.kronecker_product(tau,tau)
    ck('correlated_marginals',trace_keep(corr,[0],2)==tau and trace_keep(corr,[1],2)==tau)
    ck('joint_freshness_counterexample',sum(abs(corr[i,i]-prod[i,i]) for i in range(4))/2==s.Rational(8,25))
    stock=corr if fault=='correlated_stock' else prod
    # S1,S2,B1,B2: vacuum inputs expose stock joint output exactly.
    initial=s.kronecker_product(vac,vac,stock);U=embed(gate,[1,3],4)*embed(gate,[0,2],4)
    ck('product_stock_joint_reset',trace_keep(U*initial*U.H,[0,1],4)==prod)
    # Coherent first input; tester uses first delivered output to control next input.
    initial=s.kronecker_product(inp,vac,prod);U1=embed(gate,[0,2],4);U2=embed(gate,[1,3],4)
    cnot=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]);V=embed(cnot,[0,1],4)
    actual=trace_keep(U2*V*U1*initial*U1.H*V.H*U2.H,[0,1],4)
    # Independent ideal replacement removes each input and tensors tau; tester-controlled second input is then erased.
    ideal_after1=s.kronecker_product(tau,vac);tested=cnot*ideal_after1*cnot.H
    ideal=s.kronecker_product(trace_keep(tested,[0],2),tau)
    ck('causal_adaptive_fixture',actual==ideal)
    # Exact off-target area channel, all matrix units, independent reduced formula.
    c=s.Rational(3,5);ss=s.Rational(4,5);phase=c-s.I*ss
    Ua=s.diag(1,1,1,phase**2);Ua[1,1]=Ua[2,2]=phase*c;Ua[1,2]=Ua[2,1]=phase*s.I*ss
    ck('partial_gate_unitary',simp(Ua.H*Ua)==s.eye(4))
    for i in range(2):
        for j in range(2):
            E=s.zeros(2);E[i,j]=1;got=trace_keep(Ua*s.kronecker_product(E,tau)*Ua.H,[0],2)
            tr=s.trace(E);qq=c*c*E[1,1]+ss*ss*p*tr
            expected=s.Matrix([[tr-qq,(c+s.I*ss)*c*E[0,1]],[(c-s.I*ss)*c*E[1,0],qq]])
            ck('partial_GAD_'+str((i,j)),simp(got-expected)==s.zeros(2))
    ck('1000_full_dilation_budget',F(1,10000)+1000*2*F(1,1000000)+F(1,10000)==F(11,5000))
    ck('1000_reduced_channel_budget',1000*(F(1,2000000)+F(4,5)*F(1,1000000)**2)+F(2,10000)<F(701,1000000))
    for K in [1,2]:
        thermal=tau if K==1 else s.kronecker_product(tau,tau)
        choi=s.kronecker_product(s.eye(2**K),thermal)
        ck('actual_Choi_rank_'+str(K),choi.rank()==4**K)
    for K in range(1,7):
        ck('Choi_rank_formula_arithmetic_'+str(K),(2**K)**2==4**K)
        ck('one_fewer_donor_insufficient_'+str(K),(2**(K-1))**2<4**K)
    return out

RESULT='K2256'
REPORT='lab/process/k2256-causal-fresh-resource-reset.json'
DEPS=['explorations/conditional-build/k2256-causal-fresh-resource-reset-2026-10-29.md', 'explorations/conditional-build/k2252-adaptive-reset-interface-2026-10-29.md', 'explorations/conditional-build/k2249-finite-density-chain-reset-2026-10-29.md']
EVIDENCE="Finite exact algebra, changed-input faults and rational resource controls; universal proofs are written separately. Hashes check reporting integrity."

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    root=Path(__file__).resolve().parents[2];checks=controls()
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected input fault',f);faults[f]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'report drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
