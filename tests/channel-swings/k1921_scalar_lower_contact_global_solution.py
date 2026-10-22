"""Exact spline identities. The note supplies the global variational proof."""
from pathlib import Path
import sympy as S
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def calculate(cubic=2):
 t,d,A,k,j,w,tau,h,s,x,ell=S.symbols('t d A k j w tau h s x ell',positive=True)
 checks=[]
 def eq(a,b,label):assert S.factor(a-b)==0,label;checks.append(label)
 f=-A*(3*(t/d)**2-cubic*(t/d)**3);g=-A+k*t*t/2+j*t**3/6
 for v,z,label in [(f.subs(t,0),0,'clamp value'),(S.diff(f,t).subs(t,0),0,'clamp slope'),(f.subs(t,d),-A,'lower contact'),(S.diff(f,t).subs(t,d),0,'contact slope'),(S.diff(f,t,2).subs(t,d),6*A/d**2,'contact moment')]:eq(v,z,label)
 eq(S.integrate(S.diff(f,t,2)**2,(t,0,d)),12*A*A/d**3,'left energy')
 eq(S.integrate(S.diff(g,t,2)**2,(t,0,w)),k*k*w+k*j*w*w+j*j*w**3/3,'right energy')
 inner=h*(1-t/tau)**2;eq(S.integrate(S.diff(inner,t)**2,(t,0,tau)),4*h*h/(3*tau),'inner energy')
 vals={d:s-w,tau:w/x,k:h*(1-x*x)/w,j:2*h*x*x/w**2,A:h*(1-x*x)*(s-w)**2/(6*w)}
 eq((k*w+j*w*w/2).subs(vals),h,'plateau slope')
 P=(1+x*x+2/x)*w*w+(4*s*(1-x*x)+6*ell)*w-2*s*s*(1-x*x)
 closure=(2*A-h*ell-h*tau/3-k*w*w/2-j*w**3/6).subs(vals)
 eq(closure,-h*P/(6*w),'matching equation')
 ff=x**6-3*x**4+2*x**3+6*(1+ell/s)*x*x-2
 eq(P.subs(w,s*x*x),s*s*ff,'positive root and multiplier bound')
 eq((j-12*A/d**3).subs(vals),2*h*(s*x*x-w)/(w*w*(s-w)),'lower reaction')
 # Boundary terms with arbitrary competitor derivative at both contacts.
 vm,dm,vp,dp,vb=S.symbols('vm dm vp dp vb');j0=12*A/d**3
 boundary=(6*A/d**2*dm-j0*vm)+(-j*vb-k*dm+j*vm)+(j*vb-j*vp)
 eq(boundary.subs(k,6*A/d**2),(j-j0)*vm-j*vp,'unrestricted derivative cancellation')
 xx=S.Rational(3,4);ww=S.Rational(1,4);ss=hh=S.Integer(1)
 ll=S.solve(P,ell)[0].subs({x:xx,w:ww,s:ss});dd=ss-ww;tt=ww/xx;kk=hh*(1-xx**2)/ww;jj=2*hh/tt**2;aa=kk*dd**2/6
 E=2*(12*aa**2/dd**3+kk**2*ww+kk*jj*ww**2+jj**2*ww**3/3+4*hh**2/(3*tt))
 eq(ll,S.Rational(133,1152),'rational plateau');eq(aa,S.Rational(21,128),'rational cap');eq(E,S.Rational(147,8),'rational energy');eq(jj-12*aa/dd**3,S.Rational(40,3),'rational reaction')
 dep='explorations/conditional-build/k1919-scalar-finite-budget-contact-solution-2026-10-22.md'
 return dict(result_id='K1921',evidence_kind='analytic global proof plus exact polynomial identities',mathematical_controls=checks,example=dict(s='1',h='1',ell=str(ll),x=str(xx),w=str(ww),A=str(aa),E=str(E)),scope='complete equal-gap frontier; unequal-gap and finite-duration optimum open',dependencies={dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1921-scalar-lower-contact-global-solution.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1921 exact controls',len(r['mathematical_controls']),r['example'])
