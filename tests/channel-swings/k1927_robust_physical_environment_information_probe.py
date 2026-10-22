"""Separate finite reconstruction; imported producer is used only for fault tests."""
from pathlib import Path
import importlib.util,json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def reconstruct():
 labels=[]
 def eq(a,b,n):
  z=a-b
  assert (z.applyfunc(s.simplify)==s.zeros(*z.shape) if isinstance(z,s.MatrixBase) else s.simplify(z)==0),n
  labels.append(n)
 # Recover arbitrary linear map coordinates by solving the tomography system.
 pts=[s.Matrix([[1,0],[0,0]]),s.Matrix([[0,0],[0,1]]),s.Matrix([[1,1],[1,1]])/2,s.Matrix([[1,s.I],[-s.I,1]])/2]
 coord=s.Matrix.hstack(*[p.reshape(4,1) for p in pts])
 coeffs=coord.inv()
 for a in range(2):
  for b in range(2):
   E=s.zeros(2);E[a,b]=1;c=coeffs*E.reshape(4,1)
   eq(sum((c[j]*pts[j] for j in range(4)),s.zeros(2)),E,f'solved matrix unit {a}{b}')
 # Singular-value block norm of a rank-one positive state, not a scalar proxy.
 for v in [s.Matrix([1,2,2,4])/5,s.Matrix([3,0,0,4])/5,s.Matrix([1,s.I,1,-s.I])/2]:
  rho=v*v.H;B=rho[:2,2:];d0=s.trace(rho[:2,:2]);d1=s.trace(rho[2:,2:]);norm=s.sqrt(s.trace(B.H*B))
  eq(norm**2,d0*d1,'offdiagonal Cauchy equality');assert 2*norm<=1;labels.append('offdiagonal sum bounded')
 # Holevo/entropy bookkeeping at exact target with a mixed spectator.
 p=s.Rational(2,5);spect=[p,1-p]
 H=lambda vals:-sum(x*s.log(x) for x in vals if x)
 initial=H(spect);average=H([x/2 for x in spect for _ in range(2)])
 eq(s.expand_log(average-initial,force=True),s.log(2),'physical entropy increase')
 # Mixture of orthogonal target system labels has conditional entropy zero.
 joint=H([x/2 for x in spect for _ in range(2)])
 eq(joint-average,0,'conditional entropy accounting')
 # The fourth complex direction cannot be inferred from three real probes.
 Y=s.Matrix([[0,-s.I],[s.I,0]])
 for p0 in pts[:3]:eq(s.trace(Y*p0),0,'three real projectors miss Y')
 eq(s.trace(Y*pts[3]),-1,'fourth projector detects Y')
 return labels
def reject_bad_report(bad,expected):
 try:
  assert bad==expected,'report or dependency pin mismatch'
 except AssertionError as exc:
  print('CAUGHT reporting assertion:',exc)
 else:
  raise AssertionError('report fault escaped')
if __name__=='__main__':
 labels=reconstruct();spec=importlib.util.spec_from_file_location('prod',HERE/'k1927_robust_physical_environment_information.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 base=m.calculate();faults=0
 for kw in [{'phase':1},{'cross_sign':-1}]:
  try:m.calculate(**kw)
  except AssertionError as exc:
   print("CAUGHT mathematical assertion:",str(exc) or "exact reconstructed equality");faults+=1
  else:raise AssertionError('mathematical fault escaped')
 path=ROOT/'lab/process/k1927-robust-physical-environment-information.json';report=json.loads(path.read_text());assert report==base
 bad=json.loads(json.dumps(report));bad['tomography_diamond_coefficient']=9;reject_bad_report(bad,base)
 for p,h in report['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 bad=json.loads(json.dumps(report));key=next(iter(bad['dependencies']));bad['dependencies'][key]='0'*64;reject_bad_report(bad,base)
 print('PASS K1927 separate exact controls',len(labels),'math faults',faults,'report/pin faults 1/1')
