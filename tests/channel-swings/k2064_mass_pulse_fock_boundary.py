"""Exact overlap, UV coefficients and derivative identities for the companion proof."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def produce():
 checks=[]
 def ck(name,test):
  if not test:raise AssertionError('FAIL '+name)
  checks.append(name)
 X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]]);I=s.eye(2);k=s.kronecker_product;cs=[k(X,I),k(Z,X),k(Z,Z)];b=-s.I*k(Z,J);one=s.eye(4);zero=s.zeros(4);rows=[]
 for pp,ma,mb in [([3,0,0],4,12),([0,3,4],12,5),([0,0,0],1,2),([1,2,2],3,3),([0,0,3],4,2)]:
  rr=s.Integer(sum(x*x for x in pp));ma=s.Integer(ma);mb=s.Integer(mb);A=sum((s.Integer(x)*c for x,c in zip(pp,cs)),zero);Ea=s.sqrt(rr+ma*ma);Eb=s.sqrt(rr+mb*mb);P=(one+(A+ma*b)/Ea)/2;Q=(one+(A+mb*b)/Eb)/2;nu=(1-(rr+ma*mb)/(Ea*Eb))/2
  ck('change of mass overlap',s.simplify(P*(one-Q)*P-nu*P)==zero)
  ck('projection difference square',s.simplify((P-Q)**2-nu*one)==zero)
  ck('both rank two',P.rank()==Q.rank()==2)
  rows.append(dict(p=pp,masses=[int(ma),int(mb)],nu=str(nu)))
 x,a,b0=s.symbols('x a b',positive=True)
 nu=(1-(1+a*b0*x*x)/s.sqrt((1+a*a*x*x)*(1+b0*b0*x*x)))/2
 uv=s.simplify(s.limit(nu/x**2,x,0));ck('sudden UV coefficient',s.simplify(uv-(a-b0)**2/4)==0)
 r,m,v,acc,jerk=s.symbols('r m v acc jerk',real=True);E=s.sqrt(r*r+m*m)
 def dt(q):return s.diff(q,m)*v+s.diff(q,v)*acc+s.diff(q,acc)*jerk
 f=-r*v/(2*E**2);g=f/(2*E);h=-r*acc/(8*E**4)+3*r*m*v*v/(8*E**6)
 ck('first division coefficient',s.simplify(dt(g)/(2*E)-h)==0)
 hdot=-r*jerk/(8*E**4)+r*(10*m*v*acc+3*v**3)/(8*E**6)-18*r*m*m*v**3/(8*E**8)
 ck('second derivative coefficient',s.simplify(dt(h)-hdot)==0)
 L,t=s.symbols('L t',positive=True)
 f0=L/2-s.sin(2*t*L)/(4*t);f1=L*L/4-L*s.sin(2*t*L)/(4*t)-s.cos(2*t*L)/(8*t*t)+1/(8*t*t)
 ck('density oscillatory integral',s.trigsimp(s.diff(f0,L)-s.sin(t*L)**2)==0)
 ck('energy oscillatory integral',s.trigsimp(s.diff(f1,L)-L*s.sin(t*L)**2)==0)
 ck('density normalization',s.simplify(704*4*s.pi/(2*s.pi)**3/2-176/s.pi**2)==0)
 ck('pair energy normalization',s.simplify(704*4*s.pi/(2*s.pi)**3*2/4-176/s.pi**2)==0)
 # Rational fixtures exercise the absolute bounds used in the C3 proof.
 for rr,mm,vv,aa,jj in [(1,1,2,3,4),(2,-3,-2,1,4),(3,0,1,-2,-3),(5,2,-3,4,1)]:
  sub={r:s.Integer(rr),m:s.Integer(mm),v:s.Integer(vv),acc:s.Integer(aa),jerk:s.Integer(jj)}
  actual=sum(abs(q.subs(sub)) for q in [hdot,h*f,g*f])
  bound=(abs(s.Integer(jj))/8+(10*abs(mm*vv*aa)+3*abs(vv)**3)/s.Integer(8)+18*mm*mm*abs(vv)**3/s.Integer(8)+(abs(aa)+3*abs(mm)*vv*vv)*abs(vv)/s.Integer(16)+s.Rational(vv*vv,8))/rr**3
  ck('smooth remainder bound fixture',s.simplify(actual<=bound)==s.true)
 refs=['lab/process/k2061-common-asymptotic-sector.json','explorations/conditional-build/k1896-local-phase-vacuum-boundary-2026-10-21.md','explorations/conditional-build/k1897-smooth-pulse-energy-2026-10-21.md']
 return dict(scope='imported polarized CAR on conditional massive1408 graph; continuum density differs from total trace',checks=checks,fixtures=rows,positive_fiber_dimension=704,UV_coefficients=dict(number_density='176*lambda^2/pi^2',pair_energy_density='176*lambda^2/pi^2',sudden_overlap='(a-b)^2/4'),smooth_bound=dict(amplitude_order=-3,squared_order=-6,number_radial_order=-4,energy_radial_order=-3,moment_range='0 <= q < 3'),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},proof_only=['nonatomic multiplier noncompactness','thermodynamic density limit','oscillatory asymptotic remainder','lattice sums','feedback-aware smooth bound','fixed-sea intermediate-time obstruction'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce();f=ROOT/'lab/process/k2064-mass-pulse-fock-boundary.json'
 if a.write:f.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(f.read_text())==d
 print('PASS',len(d['checks']),'exact overlaps/coefficients; universal analytic proofs separate')
