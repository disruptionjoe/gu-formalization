from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

ID='K2128';SLUG='k2128-contact-limit-energy-cost'
INPUTS=['tests/channel-swings/k2127_smooth_collision_locality_probe.py']
SCOPE='Exact analytic integral and actual phase/support controls, separate from universal fractional-energy and full-code proofs.'
import k2127_smooth_collision_locality_probe as smooth
def checks(fault=None):
 ck={};put=lambda k,x:ck.__setitem__(k,bool(x));a,b,e,d,h=s.symbols('a b e d h',positive=True)
 power=2 if fault!='wrong-fractional-kernel' else 1
 # Exact cross-interface region: b between a and2a, a between2e and d/2.
 inner=s.integrate((a+b)**(-power),(b,a,2*a))
 lower=s.integrate(inner,(a,2*e,d/2))
 put('cross-layer-integral',s.simplify(lower-s.log(d/(4*e))/6)==0)
 put('log-divergence',s.limit(lower,e,0,dir='+')==s.oo)
 # Actual three-range energy bounds; omitting a range is a genuine wrong integrand.
 small=s.integrate((h*h/e)/h**2,(h,0,e));middle=s.integrate((h if fault!='omit-middle-range' else 0)/h**2,(h,e,1));large=s.integrate(1/h**2,(h,1,s.oo))
 put('upper-log-integral',s.simplify(small+middle+large-(2-s.log(e)))==0)
 # Full-turn correction localized in layer: min(h²/e,e), plus smooth amplitude.
 full=s.integrate(1/e,(h,0,e))+s.integrate(e/h**2,(h,e,s.oo))
 put('full-turn-uniform-bound',full==2)
 z=s.symbols('z',real=True);bump=(1-z*z)**2
 mass=s.integrate(bump*bump,(z,-1,1))*e;derivative=s.integrate(s.diff(bump,z)**2,(z,-1,1))/e
 put('concentrating-layer-norm',mass==s.Rational(256,315)*e)
 put('concentrating-layer-gradient',derivative==s.Rational(256,105)/e)
 # Phase jumps, not all nonzero theta: integer full turns are an essential exception.
 jump=lambda th:s.simplify(s.expand_complex(abs(s.exp(-s.I*th)-1)**2))
 put('pi-has-jump',jump(s.pi)==4)
 put('full-turn-no-jump',jump(2*s.pi)==0)
 # Fourier coordinate transform derived from exponent px*x+py*y.
 pr,ps,xx,yy=s.symbols('pr ps x y',real=True);rr=xx-yy;ss=(xx+yy)/(1 if fault=='wrong-coordinate-half' else 2)
 exp=pr*rr+ps*ss
 px=s.diff(exp,xx);py=s.diff(exp,yy)
 put('conjugate-momenta',px==pr+ps/2 and py==-pr+ps/2)
 put('positive-proxy-symbol',all(abs(px.subs({pr:p,ps:q}))+abs(py.subs({pr:p,ps:q}))==2*max(abs(p),abs(q)/2) for p,q in product([s.Rational(-3,2),s.Rational(0),s.Rational(2,3)],repeat=2)))
 # Actual smooth/sharp phase mismatch lives in two relative-coordinate strips.
 def step(x):return int(x>0)
 def delta(r,t,eps):
  smoothphase=smooth.profile((r+2*t)/eps)-(0 if fault=='omit-initial-phase' else smooth.profile(r/eps))
  return smoothphase-(step(r+2*t)-step(r))
 tuples=product([F(-3),F(-1,2),F(1,2),F(3)],[F(-1),F(1)], [F(1,10),F(1,4)])
 put('two-slab-localization',all(delta(r,t,eps)==0 for r,t,eps in tuples if abs(r)>eps and abs(r+2*t)>eps))
 M=s.symbols('M',positive=True);rail=F(1,2) if fault!='omit-probe-normalization' else F(1)
 squared=4*2*(2*e*M)*rail
 put('two-slab-code-constant',squared==8*e*M)
 # Plateau operator-norm witness has epsilon-dependent input r=-epsilon/4.
 # F=-1/4 value1/3 for note's smooth central plateau, initial sharp value0.
 phase=s.pi*(1-s.Rational(1,3));sharp=s.pi
 diff=s.simplify(s.expand_complex(abs(s.exp(-s.I*phase)-s.exp(-s.I*sharp))**2))
 put('operator-norm-nonconvergence-witness',diff==1)
 put('completed-error-can-vanish',delta(F(-2),F(2),F(1,2))==0)
 return ck
FAULTS=['wrong-fractional-kernel','omit-middle-range','wrong-coordinate-half','omit-initial-phase','omit-probe-normalization']

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
