#!/usr/bin/env python3
"""Exact finite GKLS cascade, encoded CAR embedding and information-disturbance controls."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT='lab/process/k1894-semicausal-quantum-dynamics.json'
INPUTS=['lab/process/k1892-causal-observation-algebra.json','explorations/conditional-build/k115-k114-feed-forward-nonequilibrium-detector-wave-2026-09-03.md']
def comm(a,b):return a*b-b*a
def zero(a):return all(s.simplify(x)==0 for x in a)
def generator(H,ls,X):return s.I*comm(H,X)+sum((l.H*X*l-(l.H*l*X+X*l.H*l)/2 for l in ls),s.zeros(X.rows))
def dual(H,ls,r):return -s.I*comm(H,r)+sum((l*r*l.H-(l.H*l*r+r*l.H*l)/2 for l in ls),s.zeros(r.rows))
def enc(a):return {'rows':a.rows,'columns':a.cols,'entries':[[i,j,str(a[i,j])] for i in range(a.rows) for j in range(a.cols) if a[i,j]]}
def produce():
    checks={}
    def ck(k,v):
        checks[k]=bool(v)
        if not v:raise AssertionError('FAIL '+k)
    I=s.eye(2);lo=s.Matrix([[0,1],[0,0]]);Z=s.diag(1,-1);X=lo+lo.H;kron=s.kronecker_product
    a,b=s.symbols('a b',real=True);A=a*kron(lo,I);B=b*kron(I,lo);L=A+B;H=(B.H*A-A.H*B)/(2*s.I)
    ck('Hermitian_H',H.H==H)
    for i in range(2):
        for j in range(2):
            x=s.zeros(2);x[i,j]=1;emb=kron(x,I)
            ck(f'all_matrix_units_autonomous_{i}{j}',zero(generator(H,[L],emb)-kron(generator(s.zeros(2),[a*lo],x),I)))
            ck(f'positive_dissipation_{i}{j}',zero(generator(H,[L],emb.H*emb)-generator(H,[L],emb.H)*emb-emb.H*generator(H,[L],emb)-comm(L,emb).H*comm(L,emb)))
    # Opposite sign and omission both create reverse influence.
    ck('wrong_sign_detected',not zero(generator(-H,[L],kron(X,I))-kron(generator(s.zeros(2),[a*lo],X),I)))
    ck('dissipator_alone_not_cascade',not zero(generator(s.zeros(4),[L],kron(X,I))-kron(generator(s.zeros(2),[a*lo],X),I)))
    hh=H.subs({a:1,b:1});ll=L.subs({a:1,b:1});t=s.symbols('t',nonnegative=True);e=s.eye(4);v=e[:,2]-t*e[:,1]
    rho=s.exp(-t)*v*v.H+(1-(1+t*t)*s.exp(-t))*e[:,0]*e[:,0].T
    ck('exact_cascade_master_solution',zero(s.diff(rho,t)-dual(hh,[ll],rho)))
    ck('initial_excited_visible',rho.subs(t,0)==e[:,2]*e[:,2].T)
    ck('trace_one',s.simplify(s.trace(rho))==1)
    ck('positive_ground_weight_derivative',s.simplify(s.diff(1-(1+t*t)*s.exp(-t),t)-(t-1)**2*s.exp(-t))==0)
    ck('visible_decay',s.simplify(rho[2,2]+rho[3,3]-s.exp(-t))==0)
    ck('transfer_peak',s.simplify(s.diff(t*t*s.exp(-t),t)-t*(2-t)*s.exp(-t))==0)
    ck('hidden_transfer',s.simplify(rho[1,1]+rho[3,3]-t*t*s.exp(-t))==0)
    ck('entanglement_PT_minor',s.simplify(-rho[1,2]*rho[2,1]+t*t*s.exp(-2*t))==0)
    # Informative center-only repair: Z is protected, X loses coherence.
    az=kron(Z,I);bz=kron(I,lo);lz=az+bz;hz=(bz.H*az-az.H*bz)/(2*s.I)
    ck('center_protected',zero(generator(hz,[lz],kron(Z,I))))
    ck('coherence_cost',generator(hz,[lz],kron(X,I))==-2*kron(X,I))
    forward=generator(hz,[lz],kron(I,X));ck('forward_readout_nonzero',forward[0,0]==-2 and forward[2,2]==2)
    gamma=comm(lz,kron(X,I)).H*comm(lz,kron(X,I));ck('disturbance_bound_saturated',gamma==4*s.eye(4))
    # Fermionic realization using two dual-rail modes per logical qubit, all jumps even.
    z=s.diag(1,-1);cs=[kron(*([z]*i+[lo]+[I]*(3-i))) for i in range(4)];ns=[c.H*c for c in cs]
    af=cs[0].H*cs[1];bf=cs[2].H*cs[3];lf=af+bf;hf=(bf.H*af-af.H*bf)/(2*s.I)
    # Logical |0>=|10>, |1>=|01> in each factor.
    U=s.zeros(16,4)
    for j,idx in enumerate([10,9,6,5]):U[idx,j]=1
    ck('dualrail_isometry',U.H*U==s.eye(4))
    ck('dualrail_exact_jump',lf*U==U*ll and lf.H*U==U*ll.H)
    ck('dualrail_exact_H',hf*U==U*hh)
    parity=kron(z,z,z,z);ck('CAR_even',zero(comm(parity,lf)) and zero(comm(parity,hf)))
    ck('dualrail_reducing',zero(comm(U*U.H,lf)) and zero(comm(U*U.H,hf)))
    # Nonlocal target hopping jump: even remote pair preparation changes an immediate local rate.
    nf,ng,nh=ns[:3];hop=cs[0].H*cs[1];rate=generator(s.zeros(16),[hop],nf)
    ck('nonlocal_jump_rate',rate==ng*(s.eye(16)-nf))
    ck('even_pair_remote_signal',rate[0,0]==0 and rate[6,6]==1 and parity[0,0]==parity[6,6]==1)
    ck('nonlocal_jump_even',zero(comm(hop,parity)))
    return dict(result_id='K1894',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',cascade={'H':enc(hh),'L':enc(ll),'rho':'exp(-t)(|10>-t|01>)(<10|-t<01|)+(1-(1+t^2)exp(-t))|00><00|','visible_excitation':'exp(-t)','hidden_excitation':'t**2*exp(-t)','partial_transpose_minor':'-t^2 exp(-2t)','source_to_hidden':True,'hidden_to_source':False},rigidity={'unitary_factor_marginal':'all jumps in factor commutant; Hamiltonian splits','approximate':'sum ||[Lk,U]psi||^2 <= 2 epsilon for observed unitary U and unit psi under uniform generator error epsilon','center_exception':'Z observable unchanged; X,Y decay at rate2; hidden X derivative -2 for Z+ and +2 for Z-'},fermionic_encoding=enc(U),scope={'GKLS_imported':True,'finite_factor':True,'bounded_nonlocal_continuum_extension':True,'local_spacetime_interacting_model':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads((ROOT/OUT).read_text()),'FAIL report drift'
    print('PASS K1894',len(d['checks']),'exact matrix/symbolic controls;',len(INPUTS),'pins')
