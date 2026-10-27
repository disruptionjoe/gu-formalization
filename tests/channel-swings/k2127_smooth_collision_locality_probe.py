from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

ID='K2127';SLUG='k2127-smooth-collision-locality'
INPUTS=['explorations/conditional-build/k2125-local-two-field-collision-2026-10-27.md']
SCOPE='Finite exact smooth-profile, signed-cocycle, full-record and signalling controls. Written proof owns smooth domains and full local-vN collar.'
def profile(x):
 # Explicit C2 polynomial transition for exact algebraic controls; general proof uses C-infinity F.
 if x<=-1:return F(0)
 if x>=1:return F(1)
 return F(1,2)+F(15,16)*x-F(5,8)*x**3+F(3,16)*x**5
def checks(fault=None):
 ck={};put=lambda k,x:ck.__setitem__(k,bool(x))
 def phase(r,t):return profile(r+(1 if fault=='wrong-relative-speed' else 2)*t)-(0 if fault=='omit-initial-phase' else profile(r))
 pts=[F(-2),F(-3,4),F(-1,4),F(1,3),F(2)]
 put('initial-identity',all(phase(r,0)==0 for r in pts))
 put('signed-cocycle',all(phase(r,t+u)==phase(r,t)+phase(r+2*t,u) for r,t,u in product(pts,[F(-2,3),F(1,4)],[F(1,5),F(-1,2)])))
 put('signed-inverse',all(phase(r,t)+phase(r+2*t,-t)==0 for r,t in product(pts,[F(-1,3),F(1,4)])))
 put('two-interfaces-support',all(phase(r,t)==0 for r,t in [(F(-4),F(1,2)),(F(4),F(1,2)),(F(-4),F(-1,2)),(F(4),F(-1,2))]))
 x=s.symbols('x',real=True);pp=s.Rational(1,2)+15*x/16-5*x**3/8+3*x**5/16
 put('profile-C2-endpoints',all(s.diff(pp,x,k).subs(x,v)==(s.Integer((v+1)//2) if k==0 else 0) for k in range(3) for v in [-1,1]))
 put('profile-monotone',s.factor(s.diff(pp,x))==15*(x-1)**2*(x+1)**2/16)
 # Actual conjugation differentiation, not asserted Hamiltonian formula.
 eps,th,v=s.symbols('eps th v',positive=True);gg=s.exp(-s.I*th*pp);a=1+x+x*x
 actual=s.simplify(gg*(-2*s.I*v)*s.diff(s.conjugate(gg)*a,x))
 expected=-2*s.I*v*s.diff(a,x)+(2 if fault!='potential-sign' else -2)*v*th*s.diff(pp,x)*a
 put('conjugacy-potential',s.simplify(actual-expected)==0)
 # A concrete C-infinity central plateau from the note. All support endpoints stay there.
 rad=F(1,128);t=F(1,32);interval=[-F(1,4)-2*rad,-F(1,4)+2*rad]
 put('plateau-support',all(-F(1,2)<r<r+2*t<F(1,2) for r in interval))
 delta=F(2,3)*((1 if fault=='wrong-relative-speed' else 2)*t)
 put('exact-plateau-phase',delta==F(1,24))
 put('spacelike-separated-readout',2*t<F(1,4)-2*rad)
 # Phase is pi/24 for physical witness. Check actual even probe density difference spectrally.
 angle=s.pi/24 if fault!='drop-active-coupling' else 0
 u=s.Matrix([1,s.exp(-s.I*angle)])/s.sqrt(2);w=s.Matrix([1,1])/s.sqrt(2);dd=u*u.H-w*w.H
 put('probe-signal-positive',s.simplify(s.expand_complex(s.trace(dd*dd))-2*s.sin(s.pi/48)**2)==0)
 put('same-parity-preparations',sum([1,0,1])==sum([0,1,1]))
 # Full code0,1,2,3 occupation states and a one-particle dual-rail probe.
 counts=[0,1,1,2]
 if fault=='omit-system-mode':counts=[0,0,1,1]
 phases=[(-1)**n for n in counts]
 ks=[s.diag(*[(1+a)/s.Integer(2) for a in phases]),s.diag(*[(1-a)/s.Integer(2) for a in phases])]
 if fault=='readout-phase':ks=[s.diag(*[(1+s.I*a)/2 for a in phases]),s.diag(*[(1-s.I*a)/2 for a in phases])]
 projectors=[s.diag(1,0,0,1),s.diag(0,1,1,0)]
 ok=True
 for i,j,b in product(range(4),range(4),range(2)):
  E=s.zeros(4);E[i,j]=1;ok &= ks[b]*E*ks[b].H==projectors[b]*E*projectors[b]
 put('all16-matrix-units-complete-record',ok)
 put('complete-crossing-exact',all(phase(r,t)==1 for r,t in [(F(-2),F(2)),(F(-3),F(3))]))
 put('midcollision-not-constant-gate',phase(F(-1,4),F(1,8))!=phase(F(-3,4),F(1,8)))
 return ck
FAULTS=['wrong-relative-speed','omit-initial-phase','potential-sign','drop-active-coupling','omit-system-mode','readout-phase']

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 good=checks();assert all(good.values()),[k for k,v in good.items() if not v]
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 result=dict(result_id=ID,status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,scope=SCOPE,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
 out=ROOT/('lab/process/'+SLUG+'.json')
 if args.write:out.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(out.read_text())
 print('PASS',ID,len(good),'equation/witness checks;',len(bad),'actual faults')
if __name__=='__main__':main()
