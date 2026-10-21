#!/usr/bin/env python3
"""Exact finite CAR controls for the analytic continuum local-noise construction."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT='lab/process/k1895-causal-local-phase-noise.json'
INPUTS=['lab/process/k1892-causal-observation-algebra.json','lab/process/k1894-semicausal-quantum-dynamics.json','explorations/conditional-build/k987-k986-symmetric-compound-poisson-family-2026-10-04.md']
def zero(m): return all(s.simplify(x)==0 for x in m)
def model(sign=1):
    lo=s.Matrix([[0,1],[0,0]]);z=s.diag(1,-1);I=s.eye(2)
    cs=[s.kronecker_product(*([z]*i+[lo]+[I]*(3-i))) for i in range(4)]
    # beta(a_j)=conjugate(u_j) a_j, u=(1,i,1,i).
    V=s.diag(*[s.I**(sign*sum((j>>(3-i))&1 for i in [1,3])) for j in range(16)])
    return cs,V
def produce():
    checks={}
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    cs,V=model();Id=s.eye(16)
    beta=lambda X:V*X*V.H
    K=lambda X:(beta(X)+V.H*X*V)/2-X
    for j,c in enumerate(cs):
        ck('phase_'+str(j),beta(c)==([1,-s.I,1,-s.I][j])*c)
        ck('local_number_fixed_'+str(j),K(c.H*c)==s.zeros(16))
        for k,d in enumerate(cs):
            ck(f'CAR_{j}{k}',c*d.H+d.H*c==(Id if j==k else s.zeros(16)))
    A=cs[0].H*cs[1];B=cs[2].H*cs[3]
    ck('neutral_even_coherence_damped',K(A)==-A and K(B)==-B)
    ck('shared_noise_relative_coherence_fixed',K(A*B.H)==s.zeros(16))
    ck('shared_noise_not_product',not zero(K(A*B.H)-K(A)*B.H-A*K(B.H)))
    ck('pair_different_from_number',not zero(K(cs[0]*cs[1])))
    # An even remote unitary acts trivially on the local even generator image.
    W=Id-2*cs[2].H*cs[2]
    ck('remote_even_intervention',W*K(A)*W==K(A))
    q=s.symbols('q',real=True);t=s.symbols('t',nonnegative=True)
    weights=[(1+q)**2/4,(1-q*q)/4,(1-q)**2/4,(1-q*q)/4]
    ck('cyclic_weights_sum',s.expand(sum(weights))==1)
    for m in range(4):
        f=sum(weights[j]*s.I**(j*m) for j in range(4))
        expected=[1,q,q*q,q][m]
        ck('cyclic_character_'+str(m),s.simplify(f-expected)==0)
    for m in range(4):
        w=weights[m].subs(q,s.exp(-t))
        rhs=(weights[(m-1)%4]+weights[(m+1)%4])/2-weights[m]
        ck('cyclic_master_'+str(m),s.simplify(s.diff(w,t)-rhs.subs(q,s.exp(-t)))==0)
    # Independent clocks on the two disjoint pairs remove the common-noise correlation.
    V1=s.diag(*[s.I**((j>>2)&1) for j in range(16)])
    V2=s.diag(*[s.I**(j&1) for j in range(16)])
    KI=lambda X:sum(((v*X*v.H+v.H*X*v)/2-X for v in [V1,V2]),s.zeros(16))
    ck('independent_clocks_relative_decay',KI(A*B.H)==-2*A*B.H)
    return dict(result_id='K1895',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',
        generator='delta_target + gamma*(beta_u+beta_inverse_u-2*Id)/2',
        causal_speed='1/24',coherence_rate='gamma*(1-cos(theta_f-theta_g))',
        cyclic_weights=[str(x) for x in weights],
        scope=dict(continuum_Cstar_semigroup=True,target_support_causal=True,source_locality=False,Dirac_sea_normality=False,microscopic_bath=False,native_GU=False),
        checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads((ROOT/OUT).read_text()),'FAIL report drift'
    print('PASS K1895',len(d['checks']),'exact finite algebra groups;',len(INPUTS),'input pins; continuum proof in note')
