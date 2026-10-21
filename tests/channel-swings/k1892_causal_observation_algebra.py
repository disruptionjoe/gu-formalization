#!/usr/bin/env python3
"""Exact transfer, causal-generator and hidden-speed leakage controls."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1881-dynamical-minimum-energy-observation-lift.json']
OUT='lab/process/k1892-causal-observation-algebra.json'
def mat(d):
    M=s.zeros(d.get('rows',16),d.get('columns',16))
    for i,j,v in d['entries']:M[i,j]=s.Rational(v)
    return M
def zero(M):return all(s.expand(v)==0 for v in M)
def enc(M):return dict(rows=M.rows,columns=M.cols,entries=[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]])
def produce():
    en,ob,rep,_=[json.loads((ROOT/p).read_text()) for p in INPUTS];D=list(map(mat,ob['target_D']));alpha=s.Rational(138,25);checks={};witness=[]
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    x=s.symbols('x1 x2 x3',real=True);R=s.symbols('R',real=True);rho=sum(v*v for v in x)+576*R*R
    Q=s.I*sum((x[i]*D[i]/24 for i in range(3)),s.zeros(4))+R*mat(rep['blocks'][0]['repairs'][0]['B'])
    ck('target_Klein_Gordon_square',zero(Q*Q+rho*s.eye(4)/576))
    ck('target_flux_bound',sum((x[i]*D[i] for i in range(3)),s.zeros(4))**2==sum(v*v for v in x)*s.eye(4))
    for j,(e,o,r) in enumerate(zip(en['blocks'],ob['blocks'],rep['blocks'])):
        H=mat(e['H']);hi=H.inv();A=list(map(mat,e['matrices']));T=list(map(mat,o['T']));C,B,S=[mat(r['repairs'][0][k]) for k in ['C','B','S']]
        O=s.I*sum((x[i]*T[i] for i in range(3)),s.zeros(4,16))+R*S
        P=s.I*sum((x[i]*A[i] for i in range(3)),s.zeros(16))+R*C;Od=hi*O.conjugate().T
        ck('input_Gram_'+str(j),zero(O*Od-alpha*rho*s.eye(4)))
        ck('generator_transfer_'+str(j),zero(O*P-Q*O) and zero(P*Od-Od*Q))
        Tgrad=sum((x[i]*T[i] for i in range(3)),s.zeros(4,16))
        ck('local_scalar_closure_rigidity_'+str(j),zero(Tgrad*hi*Tgrad.T-alpha*sum(v*v for v in x)*s.eye(4)))
        ck('first_unequal_time_moment_'+str(j),zero(O*P*Od-alpha*rho*Q))
        ck('second_unequal_time_moment_'+str(j),zero(O*P*P*Od-alpha*rho*Q*Q))
        # Use the actual fast characteristic vector: leakage has support speed1.
        rfast=(A[0]-s.eye(16)).nullspace()[0];norm=(rfast.T*H*rfast)[0];u=s.eye(4)[:,0];leak=u*rfast.T*H
        ck('invisible_fast_source_'+str(j),T[0]*rfast==s.zeros(4,1) and norm>0)
        ck('leakage_covariance_'+str(j),leak*hi*leak.T==norm*u*u.T and T[0]*hi*leak.T==s.zeros(4))
        ck('leakage_speed_'+str(j),leak*A[0]==leak and (D[0]/24)*u!=u)
        # A normalized, bounded multiplier cannot be a local constant multiplier.
        at0=Od.subs({x[0]:0,x[1]:0,x[2]:0,R:1})/(24*s.sqrt(alpha))
        at1=Od.subs({x[0]:1,x[1]:0,x[2]:0,R:1})/s.sqrt(577*alpha)
        ck('normalized_map_nonconstant_'+str(j),at0!=at1)
        Z=s.Matrix.hstack(*T[0].col_join(T[1]).col_join(T[2]).nullspace())
        J=s.zeros(4);J[0,1]=1;J[1,0]=-1;W=Z*J*Z.T*H
        ck('local_hidden_dimension_'+str(j),Z.cols==4 and Z.rank()==4)
        ck('local_hidden_potential_'+str(j),W.rank()==2 and H*W+W.T*H==s.zeros(16) and all(t*W==s.zeros(4,16) for t in T) and S*W==s.zeros(4,16))
        witness.append(dict(fast_vector=enc(rfast),energy_norm_squared=str(norm),leak=enc(leak),local_hidden_basis=enc(Z),protected_local_potential=enc(W)))
    return dict(result_id='K1892',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',alpha=str(alpha),causal_speed='1/24',identities={'normalized_covariance':'V U_s(t) Vdagger = U_t(t)','raw_covariance':'O U_s(t) Odagger = alpha*(-Delta+576R^2)*U_t(t)','retarded_response':'O exp(-tP_s) J = exp(-tP_t) OJ','state_extension':'j Q_target jdagger + Q_hidden on orthogonal reducing sectors'},scope={'conditional_CAR_imported':True,'observed_even_algebra_causal':True,'local_source_embedding':False,'unique_physical_vacuum':False,'all_source_interventions_slow_causal':False,'source_native_GU':False},leakage_witnesses=witness,checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    elif d!=json.loads((ROOT/OUT).read_text()):raise AssertionError('FAIL certificate drift')
    print('PASS K1892',len(d['checks']),'exact matrix groups;',len(INPUTS),'pins')
