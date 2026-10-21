#!/usr/bin/env python3
"""Exact moving-complex-structure repair, using all four actual source types."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1879-rotating-observation-connection-repair.json'
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']
def mat(x):
 M=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']: M[i,j]=s.Rational(v)
 return M
def produce():
 en,src,old=[json.loads((ROOT/p).read_text()) for p in INPUTS]
 D=list(map(mat,src['target_D']));d=[x/24 for x in D];J=D[0]*D[1]*D[2];I=s.eye(4)
 checks={};signs=[]
 def ck(n,v): checks[n]=bool(v);assert v,n
 def zero(M):return all(s.expand(x)==0 for x in M)
 for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
  A=list(map(mat,er['matrices']));H=mat(er['H']);T=list(map(mat,sr['T']));L=mat(er['J'])
  sign=1 if T[0]*L==J*T[0] else -1;L=sign*L;signs.append(sign)
  ck(f'complex_transport_{ix}',L*L==-s.eye(16) and all(t*L==J*t for t in T))
  ck(f'energy_commutant_{ix}',H*L+L.T*H==s.zeros(16) and all(L*a==a*L for a in A))
  C0,B0,S0=[mat(kr['repairs'][0][z]) for z in ['C','B','S']]
  for ir,r in enumerate([s.Rational(0),s.Rational(1,3),s.Rational(2)]):
   U=((1-r*r)*I-2*r*J)/(1+r*r);W=((1-r*r)*s.eye(16)-2*r*L)/(1+r*r);Wi=((1-r*r)*s.eye(16)+2*r*L)/(1+r*r)
   ck(f'unitary_and_leading_{ix}_{ir}',U*U.T==I and W.T*H*W==H and all(U*t*Wi==t for t in T))
   Cr=W*C0*Wi;Br=U*B0*U.T;Sr=U*S0*Wi
   tt,*g=s.symbols('t g1 g2 g3');h=s.symbols('h0:9')
   # Mixed time-space and symmetric spatial jets of one scalar phase.
   tm=list(h[:3]);hh=[[h[3],h[4],h[5]],[h[4],h[6],h[7]],[h[5],h[7],h[8]]]
   C=Cr+(tt*s.eye(16)+sum((g[j]*A[j] for j in range(3)),s.zeros(16)))*L/2
   B=Br+(tt*I+sum((g[j]*d[j] for j in range(3)),s.zeros(4)))*J/2
   S=Sr+sum((g[j]*T[j]*L/2 for j in range(3)),s.zeros(4,16))
   ck(f'first_order_{ix}_{ir}',all(zero(T[j]*C-B*T[j]+S*A[j]-d[j]*S) for j in range(3)))
   Ci=[g[i]*(-L*Cr+Cr*L)/2+(tm[i]*s.eye(16)+sum((hh[i][j]*A[j] for j in range(3)),s.zeros(16)))*L/2 for i in range(3)]
   St=tt*(-J*Sr+Sr*L)/2+sum((tm[j]*T[j]*L/2 for j in range(3)),s.zeros(4,16))
   Si=[g[i]*(-J*Sr+Sr*L)/2+sum((hh[i][j]*T[j]*L/2 for j in range(3)),s.zeros(4,16)) for i in range(3)]
   ck(f'zeroth_order_all_jets_{ix}_{ir}',zero(sum((T[j]*Ci[j]-d[j]*Si[j] for j in range(3)),s.zeros(4,16))+S*C-St-B*S))
   ck(f'conservative_{ix}_{ir}',zero(H*C+C.T*H) and zero(B+B.T))
  B1,B2=[mat(z['B']) for z in kr['repairs']]
  ck(f'mass_rotation_{ix}',J*B1-B1*J==-2*B2 and J*B2-B2*J==2*B1)
  alpha=s.Rational(sr['alpha']);ck(f'constant_mass_gram_gap_{ix}',S0*H.inv()*S0.T==576*alpha*I)
 basis=[J]+[x*J for x in d];gram=s.Matrix(4,4,lambda i,j:s.trace(basis[i].T*basis[j]))
 ck('connection_orthogonal_Gram',gram==s.diag(4,s.Rational(1,144),s.Rational(1,144),s.Rational(1,144)))
 B1,B2=[mat(z['B']) for z in old['blocks'][0]['repairs']]
 ck('connection_orthogonal_mass',all(s.trace(x.T*b)==0 for x in basis for b in [B1,B2]))
 w,v=s.symbols('omega v',real=True);F=w*(-v*I+d[0])*J/2
 ck('travelling_connection_norm',zero(s.Matrix([s.trace(F.T*F)-w*w*(v*v+s.Rational(1,576))])))
 return {'result_id':'K1879','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','source_complex_signs':signs,'coefficients':{'generator':'-J/2','connection_factor':'1/2','target_speed':'1/24','constant_mass_gram_gap':'576*alpha*R^2'},'scope':{'fixed_principal_symbols':True,'fixed_leading_observation':True,'added_target_connection':True,'pure_mass_rotating_lift':False,'native_GU_identification':False,'nonzero_mass_full_L2_observation_range':True,'periodic_even_winding_only_same_domain':True},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1879',len(v['checks']),'exact algebra groups;',len(v['inputs']),'pins')
