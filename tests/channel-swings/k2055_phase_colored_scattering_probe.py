"""Independent exact Gaussian-rational force substitution and barrier replay."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def power(z,n):
 r=(F(1),F(0))
 for _ in range(n):r=mul(r,z)
 return r
def scale(c,z):return tuple(c*x for x in z)
def conj(z):return(z[0],-z[1])
def norm(z):return sum(x*x for x in z)
def replay(r):
 count=0;coeff=r['coefficients']
 for m in [2,3,4]:
  wd=[((F(1),F(0)),1),((F(0),F(1)),(-1)**m)]
  if m%2==0:wd.append(((F(1),F(1)),(-1)**(m//2)))
  for direction,base_sign in wd:
   for x,y in [(1,2),(-2,1),(0,3),(2,0)]:
    z=(F(x),F(x));w=scale(F(y),direction);sig=base_sign;g=F(1,2)
    zv=mul((F(0),F(1)),mul(conj(z),power(w,2*m)))
    wu=scale(-g,mul((F(0),F(1)),mul(power(z,2),power(conj(w),2*m-1))))
    assert zv==scale(sig*norm(w)**m,z),'complex z tangency'
    assert wu==scale(g*sig*norm(z)*norm(w)**(m-1),w),'complex w tangency'
    assert 2*mul(conj(z),zv)[0]==coeff['density_factor']*sig*norm(z)*norm(w)**m,'density derivative'
    assert -2*mul(conj(w),wu)[0]==coeff['reverse_u_sign']*2*g*sig*norm(z)*norm(w)**m,'reversed characteristic'
    count+=1
 for c in r['barrier_controls']:
  m=c['m'];g=F(c['gamma']);C=2*g*(m-coeff['reciprocal_shift']);a=F(3,2);b=F(2,3)
  bs=2*g*a*b**m;ar=-2*a*b**m
  assert (1-m)*b**(-m)*bs==-C*a,'reciprocal exponent'
  assert -C*ar==2*(m-1)*bs,'mixed derivative invariant'
  h,K,e=map(F,[c['h'],c['K_safe'],c['epsilon']]);x=h+C
  assert K>=(m-1)*max(F(1),x*x)+2*(m-1),'safe derivative bound'
  assert 0<e<=h and e<=(F(m-1)/(K+1))**(m-1),'safe barrier'
 order=list(map(tuple,r['grid_order']));assert set(order)=={(i,j) for i in range(2) for j in range(3)},'grid coverage'
 for ix,(i,j) in enumerate(order):
  assert i==0 or (i-1,j) in order[:ix],'incoming left wave';assert j==0 or (i,j-1) in order[:ix],'incoming right wave'
 assert r['phase_signs']==[[1,-1,1],[-1,1,-1]],'phase lattice'
 c=r['criterion_failure'];m=c['m'];eta=2*F(c['gamma'])*(m-1)*F(c['amplitude'])**(2*m)*F(c['point_b_squared'])**(m-1)*F(c['bump_squared_integral'])
 assert eta==F(c['eta_lower'])>=1,'uniform criterion failure'
 return count
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2055-phase-colored-scattering.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE exact complex fixtures',replay(r),flush=True);caught=[]
 for n in ['density','reverse','reciprocal','barrier','grid','phase','failure']:
  b=copy.deepcopy(r)
  if n=='density':b['coefficients']['density_factor']=1
  elif n=='reverse':b['coefficients']['reverse_u_sign']=1
  elif n=='reciprocal':b['coefficients']['reciprocal_shift']=0
  elif n=='barrier':b['barrier_controls'][0]['epsilon']='2'
  elif n=='grid':b['grid_order'].reverse()
  elif n=='phase':b['phase_signs'][0][1]=1
  else:b['criterion_failure']['eta_lower']='0'
  try:replay(b)
  except AssertionError as e:assert str(e);caught.append([n,str(e)])
  else:raise AssertionError('missed '+n)
 print('PASS coefficient/structure faults',caught)
