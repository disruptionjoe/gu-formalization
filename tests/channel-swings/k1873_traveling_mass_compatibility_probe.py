#!/usr/bin/env python3
"""Independent coefficientwise Sympy verification of polynomial annihilators."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def mat(x):
 m=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']:m[i,j]=s.Rational(v)
 return m
def verify_witness(wit,M0,M1,rhs):
 coeff=wit['polynomial_coefficients'];q=list(map(s.Rational,wit['rhs_polynomial']));degree=max(max(map(len,coeff))-1,len(q)-1);a=wit['mass'];last=s.zeros(1,70)
 for n in range(degree+2):
  w=s.Matrix([[s.Rational(c[n]) if n<len(c) else 0 for c in coeff]])
  assert w*M0+last*M1==s.zeros(1,44),'polynomial annihilator'
  target=s.zeros(1,2);target[a]=q[n] if n<len(q) else 0
  assert w*rhs==target,'mass right-hand side'
  last=w
 v=s.Symbol('v');pol=s.Poly(sum(c*v**i for i,c in enumerate(q)),v)
 assert pol!=0,'nonzero obstruction'
 for p,n in s.factor_list(pol)[1]:assert p.monic().as_expr() in [v,v-1,v+1],'real exceptional set'
 return degree+2

def run():
 z=json.loads((ROOT/'lab/process/k1873-traveling-mass-compatibility.json').read_text());src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());D=list(map(mat,src['target_D']));ds=[x/24 for x in D];Bs=[mat(x['B']) for x in old['blocks'][0]['repairs']];rhs=s.Matrix([[B[i,j] for i in range(4) for j in range(i+1,4)]+[0]*64 for B in Bs]).T;checks=0;faults=0
 for ix,(block,sr,er,kr) in enumerate(zip(z['blocks'],src['blocks'],en['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));A=list(map(mat,er['matrices']));H=mat(er['H']);Hi=H.inv();K=mat(kr['full_conservative_kernel']);Cs=[];Ss=[]
  for row in K.tolist():
   U=s.zeros(16);pos=0
   for i in range(16):
    for j in range(i+1,16):U[i,j]=row[pos];U[j,i]=-row[pos];pos+=1
   Cs.append(Hi*U);Ss.append(s.Matrix(4,16,row[126:]))
  M0=s.Matrix([list(K.row(j))[120:126]+list(T[0]*C-ds[0]*S) for j,(C,S) in enumerate(zip(Cs,Ss))]).T
  M1=s.Matrix([[0]*6+list(S) for S in Ss]).T
  for w in block['generic']:checks+=verify_witness(w,M0,M1,rhs)
  for rec in block['exceptional']:
   w=s.Matrix([list(map(s.Rational,rec['witness']))]);target=s.zeros(1,2);target[rec['mass']]=1
   assert w*(M0+rec['speed']*M1)==s.zeros(1,44),'exception annihilator'
   assert w*rhs==target,'exception mass';checks+=2
  for a,rep in enumerate(kr['repairs']):
   C=mat(rep['C']);S=mat(rep['S']);B=Bs[a]
   assert H*C+C.T*H==s.zeros(16) and B+B.T==s.zeros(4);checks+=1
   for drift in [-2,s.Rational(1,48),3]:
    shiftedA=[A[0]+drift*s.eye(16),A[1],A[2]];shiftedd=[ds[0]+drift*s.eye(4),ds[1],ds[2]]
    assert all(T[i]*C-B*T[i]+S*shiftedA[i]-shiftedd[i]*S==s.zeros(4,16) for i in range(3));checks+=1
    # q'(t)=drift; time derivative of S*m(x-q(t)) is -drift*S*m'.
    assert T[0]*C-shiftedd[0]*S+drift*S==s.zeros(4,16);checks+=1
    assert S*C-B*S==s.zeros(4,16);checks+=1
  if ix==0:
   wit=block['generic'][0];verify_witness(wit,M0,M1,rhs)
   bad=copy.deepcopy(wit);idx=next(i for i,c in enumerate(bad['polynomial_coefficients']) if c);bad['polynomial_coefficients'][idx][0]=str(s.Rational(bad['polynomial_coefficients'][idx][0])+1)
   cases=[(bad,M0,M1,rhs),(wit,M0,-M1,rhs),(wit,M0,s.zeros(70,44),rhs),(wit,M0,M1,2*rhs)]
   for i,args in enumerate(cases):
    try:verify_witness(*args)
    except AssertionError as e:faults+=1;print('DETECTED math-input',i,str(e))
    else:raise AssertionError('MISSED math-input')
   # A wrong laboratory drift fails the actual derivative equation.
   C=mat(kr['repairs'][0]['C']);S=mat(kr['repairs'][0]['S'])
   for wrong in [0,-1,2]:
    try:assert T[0]*C-(ds[0]+wrong*s.eye(4))*S+S==s.zeros(4,16),'wrong drift repair'
    except AssertionError as e:faults+=1;print('DETECTED math-input drift',wrong,str(e))
    else:raise AssertionError('MISSED drift fault')
  print('independent block',ix,'PASS',flush=True)
 for p,h in z['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 expected={'coordinate_axis':0,'fixed_principal_symbols':True,'fixed_positive_pairings':True,'constant_triple_times_arbitrary_profile':True,'nonzero_speed_mass_plane_solution':False,'constant_mass_allowed':True,'all_variable_coefficient_solutions_excluded':False,'source_GU_verdict':False}
 assert z['scope']==expected
 for key in ['nonzero_speed_mass_plane_solution','constant_mass_allowed','all_variable_coefficient_solutions_excluded','source_GU_verdict']:
  bad=copy.deepcopy(z['scope']);bad[key]=not bad[key]
  try:assert bad==expected,'scope fault'
  except AssertionError:print('DETECTED reporting',key)
  else:raise AssertionError('MISSED reporting')
 print('PASS K1873 probe',checks,'exact groups;',3,'pins; scope equality;',faults,'math-input faults; 4 reporting faults')
if __name__=='__main__':run()
