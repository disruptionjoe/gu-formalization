"""Independent Bloch/Gram, rotation and spectrum controls; no producer import."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(d,sign=-1,gap=1):
 n=0
 def ck(ok,label):
  nonlocal n
  assert bool(ok),label
  n+=1
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2)
 projs=[(I+Z)/2,(I-Z)/2,(I+X)/2,(I+sign*Y)/2];gproj=(I+(X-Y)/s.sqrt(2))/2
 ck((gproj*gproj-gproj).applyfunc(s.simplify)==s.zeros(2),'ground rank-one projector')
 for j,P in enumerate(projs):
  ck(P*P==P and s.trace(P)==1,'unit branch projector')
  val=s.simplify(gap*s.trace((I-gproj)*P));ck(s.simplify(val-s.sympify(d['branch_energies_over_gap'][j]))==0,'Bloch branch energy')
 # Orthogonal branches fix a worst-case lower bound, independent of guessed rotation.
 ck(projs[0]+projs[1]==I,'orthogonal pair sum');ck(s.trace(gproj*(projs[0]+projs[1]))==1,'ground overlap budget')
 for p in [(s.Rational(1,4),)*4,(1,0,0,0),(s.Rational(1,2),s.Rational(1,2),0,0),(s.Rational(1,2),s.Rational(1,4),s.Rational(1,8),s.Rational(1,8))]:
  rho=sum((pj*P for pj,P in zip(p,projs)),s.zeros(2));r2=(p[0]-p[1])**2+p[2]**2+p[3]**2
  ck(s.simplify(rho.det()-(1-r2)/4)==0,'independent characteristic discriminant')
  ck(s.simplify(s.trace(rho*rho)-(1+r2)/2)==0,'independent purity')
 ck(d['uniform_energy_over_gap']=='1/2-sqrt(2)/8','uniform report');ck(d['worst_population_energy_over_gap']=='1/2','minimax report')
 # Exhaust finite eigenvalue permutations for a distinct rank-three passive control.
 ev=[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)];energies=[0,2,5]
 ck(min(sum(a*b for a,b in zip(t,energies)) for t in itertools.permutations(ev))==s.Rational(3,2),'passive assignment countercontrol')
 # Equal mixture of orthogonal branches is mixed and cannot be reset unitarily.
 ck(((projs[0]+projs[1])/2).det()==s.Rational(1,4),'reset spectrum witness')
 # Reconstruct a tensor-feature matrix independently: degree0, degree1, degree2.
 a=1/s.sqrt(2);v=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([a,a]),s.Matrix([a,s.I*a])]
 features=s.Matrix.hstack(*(s.Matrix([1]).col_join(z).col_join(s.kronecker_product(z,z)) for z in v))
 ck(features.rank()==4,'endpoint tensor feature rank')
 cc=s.Matrix(4,4,lambda j,k:(v[j].conjugate().T*v[k])[0])
 slope=s.simplify(1-sum(cc)/16)
 ck(s.simplify(slope-s.sympify(d['poisson_initial_energy_slope']))==0,'independent initial spectral slope')
 ck(d['poisson_endpoint_bath_dimension']==4 and not d['bounded_control_regular_start'],'dynamics report scope')
 ck(d['dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1905-causal-quantum-memory-realization-2026-10-21.md').read_bytes()).hexdigest(),'dependency pin')
 ck(d['poisson_dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1909-poisson-phase-classification-2026-10-21.md').read_bytes()).hexdigest(),'Poisson dependency pin')
 return n
if __name__=='__main__':
 data=json.loads((ROOT/'lab/process/k1910-minimal-dephasing-bath-energy.json').read_text());print('BASELINE',check(data),'exact/control/report/pin checks')
 for name in ['bath conjugation','gap','report','pin']:
  d=deepcopy(data)
  if name=='report':d['uniform_energy_over_gap']='1/2'
  if name=='pin':d['dependency_sha256']='0'*64
  try:check(d,sign=1 if name=='bath conjugation' else -1,gap=2 if name=='gap' else 1)
  except AssertionError as e:print('CAUGHT',name,str(e))
  else:raise AssertionError('undetected '+name)
 print('PASS 2 mathematical-input, 1 report and 1 pin faults; no crash catches')
