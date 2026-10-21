#!/usr/bin/env python3
"""Independent exact travelling-jet operator tests, not a copied pass-flag audit."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1879-rotating-observation-connection-repair.json'
def mat(z):
 return s.Matrix(z.get('rows',16),z.get('columns',16),lambda i,j:next((s.Rational(v) for a,b,v in z['entries'] if (a,b)==(i,j)),0))
def data():
 return [json.loads((ROOT/('lab/process/'+p+'.json')).read_text()) for p in ['k1832-k77-common-energy-form','k1836-k77-differential-dirac-quotient','k1840-k77-conservative-variable-observation']]
def verify_math(c,only_first=False):
 en,src,old=data();D=list(map(mat,src['target_D']));d=[z/24 for z in D];J=D[0]*D[1]*D[2];n=0
 def ck(v,name):
  nonlocal n
  if not v:raise AssertionError('FAIL '+name)
  n+=1
 for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
  A=list(map(mat,er['matrices']));H=mat(er['H']);T=list(map(mat,sr['T']));L=mat(er['J'])*(1 if ix<2 else -1)*c['source_sign']
  C0,B0,S0=[2*mat(kr['repairs'][0][k]) for k in ['C','B','S']]
  ck(all(T[i]*L==J*T[i] for i in range(3)),'source_complex_transport')
  # A rational unitary at a nonzero phase; derivative from its generator.
  U=(3*s.eye(4)-4*J)/5;W=(3*s.eye(16)-4*L)/5;Wi=W.inv()
  CR=W*C0*Wi;BR=U*B0*U.T;SR=U*S0*Wi
  for v in [s.Rational(0),s.Rational(1,24),s.Rational(-1,24),s.Rational(2)]:
   w=s.Rational(3,5);a=s.Rational(7,11)
   CP=(A[0]-v*s.eye(16))*L/2;BP=(d[0]-v*s.eye(4))*J/2;SP=T[0]*L/2
   C=CR+c['source_connection']*w*CP;B=BR+c['target_connection']*w*BP;S=SR+c['observation_connection']*w*SP
   Cz=w*(-L*CR+CR*L)/2+c['source_connection']*a*CP
   Sz=w*(-J*SR+SR*L)/2+c['observation_connection']*a*SP
   # Evaluate OP-QO on arbitrary exponential spatial jets, coefficients at one point.
   zeta=[s.Rational(2),s.Rational(-3),s.Rational(5)];Tz=sum((zeta[i]*T[i] for i in range(3)),s.zeros(4,16));Az=sum((zeta[i]*A[i] for i in range(3)),s.zeros(16));dz=sum((zeta[i]*d[i] for i in range(3)),s.zeros(4))
   residual=T[0]*Cz+(Tz+S)*(Az+C)-(dz+B)*(Tz+S)+(v*s.eye(4)-d[0])*Sz
   ck(residual==s.zeros(4,16),'operator_exponential_jet')
   ck(H*C+C.T*H==s.zeros(16) and B+B.T==s.zeros(4),'energy_skew')
   ck(s.trace((w*BP).T*(w*BP))==w*w*(v*v+s.Rational(1,576)),'connection_cost')
  alpha=s.Rational(sr['alpha']);Hi=H.inv()
  ck(S0*Hi*S0.T==c['gap']*576*alpha*4*s.eye(4),'massive_Gram_gap')
  ck(all(T[i]*Hi*S0.T-S0*Hi*T[i].T==s.zeros(4) for i in range(3)),'Gram_first_derivative_cancellation')
  for j in range(3):ck(T[j]*Hi*T[j].T==alpha*s.eye(4),'Gram_principal')
  if only_first:break
 return n
def report(v):
 assert v['source_complex_signs']==[1,1,-1,-1],'FAIL signs report'
 assert v['coefficients']=={'generator':'-J/2','connection_factor':'1/2','target_speed':'1/24','constant_mass_gram_gap':'576*alpha*R^2'},'FAIL coefficients report'
 assert v['scope']=={'fixed_principal_symbols':True,'fixed_leading_observation':True,'added_target_connection':True,'pure_mass_rotating_lift':False,'native_GU_identification':False,'nonzero_mass_full_L2_observation_range':True,'periodic_even_winding_only_same_domain':True},'FAIL scope report'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'FAIL input pin'
 return 3+len(v['inputs'])
def main():
 v=json.loads(OUT.read_text());base={k:s.Rational(1) for k in ['source_sign','source_connection','target_connection','observation_connection','gap']}
 n=verify_math(base);r=report(v);caught=[]
 for key,val in [('source_sign',-1),('source_connection',0),('target_connection',0),('observation_connection',0),('gap',2)]:
  c=dict(base);c[key]=val
  try:verify_math(c,True)
  except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(str(e))
  else:raise AssertionError('undetected '+key)
 reports=[]
 for key in ['added_target_connection','pure_mass_rotating_lift','native_GU_identification','periodic_even_winding_only_same_domain']:
  z=copy.deepcopy(v);z['scope'][key]=not z['scope'][key]
  try:report(z)
  except AssertionError as e:assert str(e).startswith('FAIL ');reports.append(str(e))
  else:raise AssertionError('undetected '+key)
 print('PASS K1879 independent',n,'exact operator/Gram controls;',r,'reporting/pins;',len(caught),'math faults;',len(reports),'report faults');print(caught,reports)
if __name__=='__main__':main()
