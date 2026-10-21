#!/usr/bin/env python3
"""Independent Sympy raw-matrix residuals, polynomial jets, and scalar arithmetic."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def mat(x):
 M=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']:M[i,j]=s.Rational(v)
 return M
def load():
 return [json.loads((ROOT/p).read_text()) for p in ['lab/process/k1871-separated-mass-observation.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1832-k77-common-energy-form.json','lab/process/k1840-k77-conservative-variable-observation.json']]
def verify(c,src,eng,old):
 n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg
  n+=1
 D=list(map(mat,src['target_D']));d=[x/24 for x in D];B=[mat(x['B']) for x in old['blocks'][0]['repairs']];I=s.eye(4)
 for ix,(block,rec,en) in enumerate(zip(c['blocks'],src['blocks'],eng['blocks'])):
  T=list(map(mat,rec['T']));A=list(map(mat,en['matrices']));H=mat(en['H']);Hi=H.inv();alpha=s.Rational(rec['alpha']);reps={}
  for q in block['repairs']:
   j,a=q['axis'],q['mass'];C,S=mat(q['C']),mat(q['S']);reps[j,a]=(C,S)
   ck(H*C+C.T*H==s.zeros(16),'conserved source')
   ck(S==-24*D[j]*B[a]*T[j],'axis correction')
   for i in range(3):
    ck(T[i]*C+S*A[i]==B[a]*T[i]+d[i]*S,'first order')
    ck(T[i]*Hi*S.T==S*Hi*T[i].T,'adjoint first order')
   ck(T[j]*C==d[j]*S,'derivative coefficient')
   ck(S*C==B[a]*S,'self quadratic')
   ck(T[j]*Hi*S.T==-24*alpha*D[j]*B[a],'adjoint gradient')
   ck(S*Hi*S.T==576*alpha*I,'adjoint potential')
  for rr in block['cross_residuals']:
   j,l=rr['axes'];R=mat(rr['R']);ck(R.rank()==4,'nonzero cross rank')
   for a in range(2):
    for b in range(2):
     C,S=reps[j,a];Cp,Sp=reps[l,b];actual=S*Cp+Sp*C-B[a]*Sp-B[b]*S
     ck(actual==(R if a==b else s.zeros(4,16)),'mass inner product residual')
  # Independent value-and-derivative jets of two arbitrary profiles.
  for f,g,fp,gp in [(2,3,5,7),(-1,2,3,-4),(0,2,7,0)]:
   C1,S1=reps[0,0];C2,S2=reps[1,1];C=f*C1+g*C2;S=f*S1+g*S2;M=f*B[0]+g*B[1]
   residual=T[0]*(fp*C1)+T[1]*(gp*C2)+S*C-d[0]*(fp*S1)-d[1]*(gp*S2)-M*S
   ck(residual==s.zeros(4,16),'full polynomial jet residual')
   gram=T[0]*Hi*(fp*S1.T)+T[1]*Hi*(gp*S2.T)+S*Hi*S.T
   expected=alpha*(576*(f*f+g*g)*I-24*(fp*D[0]*B[0]+gp*D[1]*B[1]))
   ck(gram==expected,'full adjoint square potential')
 K1=D[0]*B[0];K2=D[1]*B[1]
 for q in c['line_sectors']:
  e1,e2=q['orientations'];P=mat(q['P']);ck(P==((I+e1*K1)*(I+e2*K2))/4,'line projector')
  ck(P.rank()==1 and P*P==P,'line multiplicity')
  ck(D[2]*P==q['D3_eigenvalue']*P,'signed line speed')
 # Resolve budget coefficients against the differentiated integral relation.
 b,J=s.symbols('b J',positive=True);Jprime=(1-1/(2*b))*J-1/b;k=c['line_budget'];F=lambda key:s.Rational(k[key])
 ck(s.expand((F('B_J_b')*b+F('B_J_const'))*J+F('B_constant')-(J+b*Jprime))==0,'line budget recurrence')
 ck(s.expand(F('error_b')*b+(F('error_b2J')*b*b+F('error_bJ')*b)*J+b*b*Jprime)==0,'line error recurrence')
 for sig in [s.Rational(1,7),s.Rational(2),s.Rational(5)]:
  for tau in [s.Rational(1,10),s.Rational(3)]:
   u=s.symbols('u');y=s.Rational(2,3);best=sig*y/(sig*sig+tau)
   ck(s.expand((sig*u-y)**2+tau*u*u-tau*y*y/(sig*sig+tau)-(sig*sig+tau)*(u-best)**2)==0,'frequency minimum')
 math=n
 expected={'separated_orthogonal_mass_profiles':True,'same_mass_arbitrary_separated_profiles':False,'three_nonzero_pairwise_orthogonal_masses':False,'general_44_class_solved':False,'source_owned':False,'physical_chiral_count':False,'double_wall_zero_modes_in_observation_range':False,'shift_beyond_wall_height_gaps_target':True}
 for key,v in expected.items():ck(c['results'][key]==v,'report '+key)
 for p,h in c['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin')
 return math,n-math
def numerical():
 import mpmath as m
 m.mp.dps=35
 for b in [m.mpf('0.001'),m.mpf('0.2'),m.mpf('3')]:
  J=m.sqrt(m.pi)*m.exp(b)*m.erfc(m.sqrt(b))/m.sqrt(b)
  B=2/m.sqrt(m.pi)*m.quad(lambda k:k*k*m.exp(-k*k)/(k*k+b)**2,[0,m.sqrt(b),1,m.inf])
  E=2/m.sqrt(m.pi)*m.quad(lambda k:b*b*m.exp(-k*k)/(k*k+b)**2,[0,m.sqrt(b),1,m.inf])
  assert abs(B-((b+m.mpf('0.5'))*J-1))<m.mpf('1e-28'),'numerical budget'
  assert abs(E-(b-(b*b-b/2)*J))<m.mpf('1e-28'),'numerical error'
 print('PASS 6 numerical integral consistency checks; not rigorous quadrature')
if __name__=='__main__':
 args=load();print('PASS baseline exact math / reporting+pins',verify(*args),flush=True)
 def fault(name,mutate):
  bad=copy.deepcopy(args);mutate(bad)
  try:verify(*bad)
  except AssertionError as e:print('[DETECTED mathematical-input]',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 def alter(x):x['entries'][0][2]=str(s.Rational(x['entries'][0][2])+1)
 fault('C coefficient',lambda x:alter(x[0]['blocks'][0]['repairs'][0]['C']))
 fault('S coefficient',lambda x:alter(x[0]['blocks'][0]['repairs'][0]['S']))
 fault('cross residual',lambda x:alter(x[0]['blocks'][0]['cross_residuals'][0]['R']))
 fault('target D',lambda x:alter(x[1]['target_D'][0]))
 fault('positive H',lambda x:alter(x[2]['blocks'][0]['H']))
 fault('line projector',lambda x:alter(x[0]['line_sectors'][0]['P']))
 fault('line propagation sign',lambda x:x[0]['line_sectors'][0].update(D3_eigenvalue=1))
 fault('budget half',lambda x:x[0]['line_budget'].update(B_J_const='1'))
 fault('error sign',lambda x:x[0]['line_budget'].update(error_b2J='1'))
 for key in ['general_44_class_solved','source_owned','physical_chiral_count','double_wall_zero_modes_in_observation_range']:
  x=copy.deepcopy(args);x[0]['results'][key]=True
  try:verify(*x)
  except AssertionError as e:print('[DETECTED reporting]',key,str(e),flush=True)
  else:raise AssertionError('undetected '+key)
 print('PASS 9 mathematical-input faults;4 reporting faults')
 numerical()
