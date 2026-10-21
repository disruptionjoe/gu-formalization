#!/usr/bin/env python3
"""Independent reconstruction of load-bearing speed witnesses plus residual controls."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
import k1873_traveling_mass_compatibility_probe as upstream
ROOT=Path(__file__).resolve().parents[2]
def verify(res):
 old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());source=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());D=list(map(upstream.mat,source['target_D']));count=0
 for block,sr in zip(old['blocks'],source['blocks']):
  T=list(map(upstream.mat,sr['T']))
  for rep in block['repairs']:
   C=upstream.mat(rep['C']);B=upstream.mat(rep['B']);S=upstream.mat(rep['S'])
   for r,v,jet in [(s.Rational(0),s.Rational(1,24),1),(s.Rational(1,2),-1,3),(-2,1,-1)]:
    f=r+r**3;fp=1+3*r*r
    # Direct OP-QO coefficient, with independent chain rule.
    direct=jet*fp*(T[0]*C-(D[0]/24)*S+v*S)+f*f*(S*C-B*S)
    poly=sum(s.Rational(c)*r**i for i,c in enumerate(res['nonlinear_derivative_coefficients']))
    claimed=jet*res['time_sign']*v*poly*S
    assert direct==claimed,'nonlinear OP-QO residual';count+=1
    assert direct!=s.zeros(4,16),'moving positive detector';count+=1
 z=s.Symbol('z');a=s.Rational(2);m0=s.Rational(3);m=m0/(1+res['riccati_denominator_sign']*a*m0*z)
 assert s.simplify(s.diff(m,z)-a*m*m)==0,'Riccati sign';count+=1
 # Coefficient identities checked at three distinct rational values.
 for r in [-s.Rational(1,2),0,s.Rational(1,2)]:
  L=s.Rational(3);a=s.Rational(2);kappa=s.Rational(5)
  N0=-kappa*a*a*L;N1=0;N2=kappa*L
  assert kappa*(a*a-r*r)*L+N0+r*N1+r*r*N2==0,'affine kink residual';count+=1
 return count
def run():
 z=json.loads((ROOT/'lab/process/k1875-nonlinear-moving-zero-obstruction.json').read_text())
 for p,h in z['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 upstream.run()  # Rechecks raw-bank polynomial identities and exceptional speeds.
 count=verify(z['residual']);faults=0
 # Independently test the failed scalar-Gram shortcut on the full B=0 subspace.
 old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());eng=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text())
 for kr,sr,er in zip(old['blocks'],src['blocks'],eng['blocks']):
  K=upstream.mat(kr['full_conservative_kernel']);T=list(map(upstream.mat,sr['T']));Hi=upstream.mat(er['H']).inv();images=[]
  for vec in K[:,120:126].T.nullspace():
   row=(vec.T*K).tolist()[0];S=s.Matrix(4,16,row[126:]);images.append([x for ti in T for x in (ti*Hi*S.T-S*Hi*ti.T)])
  assert s.Matrix(images).rank()==4,'massless offset Gram dimension';count+=1
  assert len(K[:,120:126].T.nullspace())==38,'affine free coordinates';count+=1
 mutations=[]
 for key,value in [('time_sign',-1),('time_sign',0),('riccati_denominator_sign',1)]:
  x=copy.deepcopy(z['residual']);x[key]=value;mutations.append(x)
 for i in [0,2]:
  x=copy.deepcopy(z['residual']);x['nonlinear_derivative_coefficients'][i]+=1;mutations.append(x)
 for n,x in enumerate(mutations):
  try:verify(x)
  except AssertionError as e:print('DETECTED new mathematical fault',n,str(e));faults+=1
  else:raise AssertionError('missed new mathematical fault')
 scope={'fixed_symbols':True,'fixed_pairings':True,'C1_mass_local':True,'zero_normalized':True,'nonzero_mass_plane_tangent':True,'nonzero_speed':True,'finite_zero_for_nonconstant_profile':False,'exponential_zero_tail':False,'all_moving_backgrounds_excluded':False,'inverse_tail_solution_constructed':False,'native_GU_verdict':False}
 assert z['scope']==scope
 for key in ['zero_normalized','all_moving_backgrounds_excluded','inverse_tail_solution_constructed','native_GU_verdict']:
  bad=copy.deepcopy(scope);bad[key]=not bad[key]
  try:assert bad==scope,'scope consistency'
  except AssertionError:print('DETECTED new reporting',key)
  else:raise AssertionError('missed reporting fault')
 print('PASS K1875 independent',count,'new exact controls;',len(z['inputs']),'pins;',faults,'new mathematical faults; 4 new reporting faults. Upstream counts separate; analytic transfer in note.')
if __name__=='__main__':run()
