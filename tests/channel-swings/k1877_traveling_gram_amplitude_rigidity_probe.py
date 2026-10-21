#!/usr/bin/env python3
"""Independent differential-operator coefficient controls and planted faults."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def matrix(d):
 rows=d.get('rows',16);cols=d.get('columns',16);out=[[s.Integer(0) for _ in range(cols)] for _ in range(rows)]
 for i,j,x in d['entries']:out[i][j]=s.Rational(x)
 return s.Matrix(out)
def check_math(c=None):
 c={'Vp':-24,'Vm':-24,'time':-1,'radial':-192,'constant':-4,'speed':s.Rational(1,24)} if c is None else c
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());Ds=[matrix(d) for d in src['target_D']];J=Ds[0]*Ds[1]*Ds[2];old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());B0,B1=[matrix(r['B']) for r in old['blocks'][0]['repairs']];n=0
 def ck(x,name):
  nonlocal n
  if not x:raise AssertionError('FAIL '+name)
  n+=1
 z=s.Symbol('z',real=True);lam=s.symbols('l0:3');alpha=s.Rational(3,2);speed=s.Rational(2,7);a=[s.Rational(1,3),s.Rational(-2,5),s.Rational(4,7)];b=s.Rational(5,9)
 # Polynomial B and u test all two-component jets through direct operator action.
 p=1+2*z+3*z*z;q=2-3*z+5*z*z;B=p*B0+q*B1;u=3+7*z+11*z*z
 G=[a[i]*J+b*Ds[i]*J for i in range(3)]
 V=u*s.eye(4)+c['Vp']*alpha*Ds[0]*s.diff(B,z)+c['Vm']*sum((a[i]*Ds[i]*B*J for i in range(3)),s.zeros(4))
 F=sum((c['speed']*Ds[i]*lam[i] for i in range(3)),s.zeros(4))+B
 symbol=-alpha*sum(x*x for x in lam)*s.eye(4)+sum((G[i]*lam[i] for i in range(3)),s.zeros(4))+V
 # Q acting on K(exp(lambda.x)e), minus K acting on Q(exp(lambda.x)e).
 QK=c['time']*speed*s.diff(symbol,z)+c['speed']*Ds[0]*s.diff(symbol,z)+F*symbol
 KQ=-alpha*(sum(x*x for x in lam)*F+2*lam[0]*s.diff(F,z)+s.diff(F,z,2))+sum((G[i]*(lam[i]*F+(s.diff(F,z) if i==0 else s.zeros(4))) for i in range(3)),s.zeros(4))+V*F
 residual=(QK-KQ).applyfunc(s.expand)
 for val in residual:
  for ll in lam:ck(s.diff(val,ll)==0,'first differential order cancels')
 ck(s.expand(s.trace(residual)-c['constant']*speed*s.diff(u,z))==0,'scalar conservation trace')
 ck(s.expand(s.trace(Ds[0]*residual)-s.diff(u,z)/6-c['radial']*alpha*(p*s.diff(p,z)+q*s.diff(q,z)))==0,'radial conservation trace')
 # Differential-operator identity for positive circular Gram, independently of a factorization.
 w=s.Rational(3,7);theta=w*z;Bc=s.cos(theta)*B0+s.sin(theta)*B1;Gc=-alpha*w*J
 ck((2*alpha*s.diff(Bc,z)+Bc*Gc-Gc*Bc).applyfunc(s.simplify)==s.zeros(4),'circular first order')
 ck((alpha*s.diff(Bc,z,2)-Gc*s.diff(Bc,z)).applyfunc(s.simplify)==s.zeros(4),'circular zero order')
 for xi in [s.Rational(-2),s.Rational(0),s.Rational(1,3),s.Rational(5)]:
  ck((xi-w/2)**2>=0 and (xi+w/2)**2>=0,'positive circular Fourier eigenvalues')
 return n

def check_bank(doc):
 n=0;src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());D=[matrix(x) for x in src['target_D']];J=D[0]*D[1]*D[2]
 for ix,(sr,er,kr) in enumerate(zip(src['blocks'],en['blocks'],old['blocks'])):
  T=[matrix(x) for x in sr['T']];A=[matrix(x) for x in er['matrices']];H=matrix(er['H']);Hi=H.inv();K=matrix(kr['full_conservative_kernel'])
  triples=[]
  for row in K.tolist():
   skew=s.zeros(16);irow=iter(row[:120])
   for i in range(16):
    for j in range(i+1,16):skew[i,j]=next(irow);skew[j,i]=-skew[i,j]
   C=Hi*skew;B=s.zeros(4);irow=iter(row[120:126])
   for i in range(4):
    for j in range(i+1,4):B[i,j]=next(irow);B[j,i]=-B[i,j]
   S=s.Matrix(4,16,row[126:]);assert H*C+C.T*H==s.zeros(16),'FAIL source conservation'
   gs=[t*Hi*S.T-S*Hi*t.T for t in T]
   aa=[s.trace(J.T*g)/4 for g in gs];bb=[s.trace((D[i]*J).T*gs[i])/4 for i in range(3)]
   assert bb[0]==bb[1]==bb[2],'FAIL common Gram coefficient'
   assert all(gs[i]==aa[i]*J+bb[0]*D[i]*J for i in range(3)),'FAIL Gram decomposition'
   assert all(T[i]*C-B*T[i]+S*A[i]-D[i]*S/24==s.zeros(4,16) for i in range(3)),'FAIL pointwise bank'
   triples.append((C,B,S));n+=4
  wl=s.zeros(128,1)
  for ii,value in doc['offset_dual_witnesses'][ix]:wl[ii]=s.Rational(value)
  C1,C2=[matrix(z['C']) for z in kr['repairs']];B1,B2=[matrix(z['B']) for z in kr['repairs']];S1,S2=[matrix(z['S']) for z in kr['repairs']]
  target=s.Matrix(list(-S2)+list(S1));evaluations=[]
  for C,B,S in triples:
   values=s.Matrix(list(S*C1+S1*C-B1*S)+list(S*C2+S2*C-B2*S));evaluations.append((wl.T*values)[0])
  massless=s.Matrix.hstack(*K[:,120:126].T.nullspace())
  assert s.Matrix([evaluations])*massless==s.zeros(1,massless.cols),'FAIL offset annihilator'
  assert (wl.T*target)[0]==1,'FAIL offset contradiction'
  n+=2
 return n

def reporting(doc):
 assert doc['identities']['Gram_span_dimension']==4,'FAIL Gram dimension reporting'
 for k in ['fixed_positive_pairings','fixed_symbols_and_leading_observation','nonzero_speed','target_two_mass_plane']:assert doc['scope'][k],'FAIL scope '+k
 for k in ['all_moving_backgrounds_excluded','rotating_observation_lift_constructed','native_GU_verdict']:assert not doc['scope'][k],'FAIL scope '+k
 for p,h in doc['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'FAIL pin'
 return 8+len(doc['inputs'])
if __name__=='__main__':
 doc=json.loads((ROOT/'lab/process/k1877-traveling-gram-amplitude-rigidity.json').read_text());n=check_math();bn=check_bank(doc);rn=reporting(doc)
 base={'Vp':-24,'Vm':-24,'time':-1,'radial':-192,'constant':-4,'speed':s.Rational(1,24)}
 for key in base:
  bad=dict(base);bad[key]+=1
  try:check_math(bad)
  except AssertionError as e:assert str(e).startswith('FAIL ');print('DETECTED mathematical',key,str(e))
  else:raise AssertionError('FAIL missed fault '+key)
 muts=[('identities','Gram_span_dimension',0),('scope','nonzero_speed',False),('scope','all_moving_backgrounds_excluded',True),('scope','rotating_observation_lift_constructed',True),('scope','native_GU_verdict',True)]
 for section,key,v in muts:
  bad=copy.deepcopy(doc);bad[section][key]=v
  try:reporting(bad)
  except AssertionError as e:assert str(e).startswith('FAIL ');print('DETECTED reporting',key,str(e))
  else:raise AssertionError('FAIL missed reporting fault')
 print('PASS K1877 probe',n,'differential/positive controls;',bn,'reconstructed bank controls;',rn,'reporting/pins;',len(base),'math faults;',len(muts),'reporting faults')
