#!/usr/bin/env python3
"""Exact boundary construction; continuum proof is in the companion note."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']
OUT='lab/process/k1891-massive-boundary-observation.json'
def mat(d):
    M=s.zeros(d.get('rows',16),d.get('columns',16))
    for i,j,v in d['entries']:M[i,j]=s.Rational(v)
    return M
def enc(M):return dict(rows=M.rows,columns=M.cols,entries=[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]])
def zero(M):return all(s.expand(x)==0 for x in M)
def data():return [json.loads((ROOT/p).read_text()) for p in INPUTS]
def construction(e,o,r,D):
    H=mat(e['H']);A=list(map(mat,e['matrices']));T=list(map(mat,o['T']));C,B,S=[mat(r['repairs'][0][k]) for k in ['C','B','S']]
    K=D[0]*B;plus=(s.eye(4)+K)/2;minus=s.eye(4)-plus;E=H.inv()*T[0].T/s.Rational(138,25);F=H*A[0]
    N=[T[a]-24*D[0]*T[0]*A[a] for a in [1,2]]
    Z=s.Matrix.hstack(*(T[0].col_join(plus*N[0]).col_join(plus*N[1])).nullspace())
    q=Z.T*F*Z;rad=Z*s.Matrix.hstack(*q.nullspace());fast=rad.row_join(Z[:,[0,1]])
    L=fast.row_join(E*s.Matrix.hstack(*plus.columnspace()))
    return H,A,T,C,B,S,K,plus,minus,E,F,N,Z,q,fast,L

def produce():
    en,ob,rep=data();D=list(map(mat,ob['target_D']));checks={};blocks=[];alpha=s.Rational(138,25)
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    p2,p3,R,Rp=s.symbols('p2 p3 R Rp',real=True)
    for j,(e,o,r) in enumerate(zip(en['blocks'],ob['blocks'],rep['blocks'])):
        H,A,T,C,B,S,K,P,M,E,F,N,Z,q,fast,L=construction(e,o,r,D);tag=str(j);ann=s.Matrix.hstack(*L.T.nullspace()).T
        ck('mass_clifford_'+tag,B.T==-B and B*B==-s.eye(4) and all(B*x+x*B==s.zeros(4) for x in D))
        ck('target_boundary_'+tag,K.T==K and K*K==s.eye(4) and P.rank()==M.rank()==2 and P*D[0]*P==M*D[0]*M==s.zeros(4))
        ck('slow_reducing_'+tag,T[0]*E==s.eye(4) and A[0]*E==E*D[0]/24 and C*E==-E*B and T[0]*C==-B*T[0])
        ck('normal_Darboux_'+tag,S==-24*K*T[0] and T[0]*A[0].inv()==24*D[0]*T[0])
        ck('conservative_'+tag,all(H*a==a.T*H for a in A) and H*C+C.T*H==s.zeros(16))
        ck('compatible_fast_dimensions_'+tag,Z.cols==8 and q.rank()==4 and fast.rank()==6 and T[0]*fast==s.zeros(4,6))
        ck('isotropic_fast_'+tag,fast.T*F*fast==s.zeros(6))
        ck('full_maximal_boundary_'+tag,L.rank()==8 and L.T*F*L==s.zeros(8) and (T[0]*L).rank()==2 and M*T[0]*L==s.zeros(4,8))
        ck('tangential_jet_transport_'+tag,all(P*n*L==s.zeros(4,8) for n in N))
        ck('adjoint_fast_trace_'+tag,all(ann*(s.eye(16)-E*T[0])*H.inv()*T[a].T*M==s.zeros(8,4) for a in [1,2]))
        ck('adjoint_Robin_trace_'+tag,all(M*T[0]*H.inv()*T[a].T*M==s.zeros(4) for a in [1,2]))
        ck('profile_derivative_'+tag,T[0]*C==D[0]*S/24 and S*C==B*S)
        ck('full_formal_intertwiner_'+tag,all(T[i]*C-B*T[i]+S*A[i]-D[i]*S/24==s.zeros(4,16) for i in range(3)))
        Z0=s.I*(p2*T[1]+p3*T[2])+R*S;Y0=-s.I*(p2*T[1].T+p3*T[2].T)+R*S.T;hi=H.inv()
        ck('normal_Gram_'+tag,T[0]*hi*T[0].T==alpha*s.eye(4))
        ck('Gram_first_derivative_'+tag,zero(T[0]*hi*Y0-Z0*hi*T[0].T))
        ck('Gram_potential_'+tag,zero(T[0]*hi*(Rp*S.T)+Z0*hi*Y0-alpha*((p2*p2+p3*p3+576*R*R)*s.eye(4)-24*Rp*K)))
        b=s.I*(p2*D[1]+p3*D[2])/24+R*B
        ck('Dirac_square_'+tag,zero(D[0]*b+b*D[0]) and zero(b*b+D[0]*Rp*B/24-(-(p2*p2+p3*p3+576*R*R)*s.eye(4)+24*Rp*K)/576))
        ck('surface_tangent_preservation_'+tag,all(M*x==x*M for x in D[1:]))
        blocks.append(dict(boundary=enc(L),fast_boundary=enc(fast),target_plus=enc(P),target_minus=enc(M),mass_K=enc(K)))
    return dict(result_id='K1891',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',blocks=blocks,alpha=str(alpha),spectrum={'surface':'alpha*|p|^2; multiplicity2','bulk_constant_mass':'alpha*(|p|^2+576R^2+(n*pi/ell)^2); multiplicity4, n>=1','target_surface_frequency':'+/-|p|/24','target_bulk_frequency':'+/-sqrt(|p|^2+576R^2+(n*pi/ell)^2)/24; multiplicity2 per sign','missing_p0_modes':2,'profile_gap_lower':'exp(-2osc(V))*(pi/ell)^2','V':'integral(24R dx)'},scope={'actual_four_coordinate_types':True,'massive_tangential_domain_intertwining':True,'smooth_static_one_coordinate_mass_profile':True,'arbitrary_spatial_mass':False,'source_native_GU':False,'same_as_old_preparation_domain':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    elif d!=json.loads((ROOT/OUT).read_text()):raise AssertionError('FAIL certificate drift')
    print('PASS K1891',len(d['checks']),'exact matrix groups;',len(INPUTS),'input pins')
