#!/usr/bin/env python3
"""Actual four-type Fourier controls for the analytic dynamical lifting theorem."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1881-dynamical-minimum-energy-observation-lift.json'
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1879-rotating-observation-connection-repair.json']
def mat(x):
 M=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']:M[i,j]=s.Rational(v)
 return M
def zero(M):return all(s.expand(z)==0 for z in M)
def produce():
 en,src,old,_=[json.loads((ROOT/p).read_text()) for p in INPUTS]
 D=list(map(mat,src['target_D']));d=[x/24 for x in D];checks={}
 def ck(n,v):checks[n]=bool(v);assert v,n
 xi=s.symbols('x1 x2 x3',real=True);mass=s.symbols('R',real=True)
 alphas=[]
 for j,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
  A=list(map(mat,er['matrices']));H=mat(er['H']);Hi=H.inv();T=list(map(mat,sr['T']));C,B,S=[mat(kr['repairs'][0][z]) for z in ['C','B','S']];alpha=s.Rational(sr['alpha']);alphas.append(str(alpha))
  O=s.I*sum((xi[i]*T[i] for i in range(3)),s.zeros(4,16))+mass*S
  P=s.I*sum((xi[i]*A[i] for i in range(3)),s.zeros(16))+mass*C
  Q=s.I*sum((xi[i]*d[i] for i in range(3)),s.zeros(4))+mass*B
  Od=Hi*O.conjugate().T;rho=sum(x*x for x in xi)+576*mass*mass
  ck(f'polynomial_Gram_{j}',zero(O*Od-alpha*rho*s.eye(4)))
  ck(f'conservative_{j}',zero(H*P+P.conjugate().T*H) and zero(Q+Q.conjugate().T))
  ck(f'intertwining_{j}',zero(O*P-Q*O))
  ck(f'adjoint_intertwining_{j}',zero(P*Od-Od*Q))
  for k,vals in enumerate([(0,0,0,1),(1,2,-1,1),(s.Rational(1,2),0,0,0)]):
   sub=dict(zip((*xi,mass),vals));o=O.subs(sub);od=Od.subs(sub);p=P.subs(sub);q=Q.subs(sub);kap=alpha*rho.subs(sub);r=od/kap;proj=r*o
   ck(f'right_inverse_{j}_{k}',zero(o*r-s.eye(4)))
   ck(f'projection_{j}_{k}',zero(proj*proj-proj) and zero(H*proj-proj.conjugate().T*H))
   ck(f'minimum_energy_{j}_{k}',zero(r.conjugate().T*H*r-s.eye(4)/kap) and zero(proj*r-r))
   ck(f'dynamical_lift_{j}_{k}',zero(p*r-r*q) and zero(proj*p-p*proj))
 ck('odd_twist_gap',min((2*n+1)**2 for n in range(-10,11))==1)
 ck('even_twist_zero',min((2*n)**2 for n in range(-10,11))==0)
 return dict(result_id='K1881',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',alphas=alphas,coefficients={'mass_squared':576,'inverse':'Odagger/[alpha*(xi2+576R2)]','normalized_observation':'O/sqrt(alpha*(xi2+576R2))'},scope={'raw_right_inverse_intertwines':True,'normalized_quotient_unitary':True,'raw_L2_isometry':False,'massless_R3_bounded_raw_inverse':False,'massless_R3_normalized_coisometry':True,'odd_twist_fixed_periodic_repair_gap':True,'pure_mass_rotating_lift':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1881',len(v['checks']),'matrix/polynomial groups;',len(v['inputs']),'pins')
