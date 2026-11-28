#!/usr/bin/env python3
"""Exact nonlinear FLRW controls; global ODE/asymptotic proofs remain written and reviewed."""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/bet-cosmology-nonlinear-roll-certificates.json'
PINS={'lab/process/bet-cosmology-wedge-growth-certificates.json': '9766c614e66f9e470a0ded0217713aba3051f60e3f9254ca25c961c8e3baf2f2', 'lab/process/wedge-shiab-einstein-reduction-certificates.json': '03d12c9e8480a05aea5444fb1151118ba7a4918813cadb802c2a30febbda3023', 'explorations/conditional-build/wedge-shiab-einstein-reduction-2026-11-27.md': '53b7e9b536c28f6bfd4877e69f3bd97a60b6e8cbcfd8f8dc2a71e64fbf1dad6a', 'explorations/conditional-build/bet-cosmology-wedge-growth-2026-11-27.md': '8e008c19655afb8b43267bcf214d628efd20c0430ff0b3787e5c8e89fda516f6', 'explorations/conditional-build/sibling-import-adjudication-2026-11-27.md': 'fdbed367c43712738284f64d5e61f60c44c4bf565e11fd8c3fe912f009d9fd57'}

def build():
 checks=[]
 def ck(n,v):assert v,n;checks.append(n)
 deps=dict(PINS)
 for p in PINS:
  if p.endswith('.json'):deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
 for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 a,b,c,F,H,P=s.symbols('a b c F H P',positive=True);D=4*b*c-a*a;Fs=D/a;mu=a/(6*b);U=(F+a)**2/(4*b)-c
 Hd=(F+a)/(12*b)-2*H**2;Pd=mu*(F-Fs)-3*H*P
 C=3*F*H**2-U/2+3*H*P
 Cd=s.diff(C,H)*Hd+s.diff(C,F)*P+s.diff(C,P)*Pd
 ck('full Friedmann constraint propagation',s.factor(Cd+4*H*C)==0)
 R=(F+a)/(2*b);ck('Legendre F relation',s.expand(2*b*R-a-F)==0)
 ck('Legendre U relation',s.expand(R*F-(b*R**2-a*R+c)-U)==0)
 ck('trace driving term',s.simplify(mu*(F-Fs)-(a*R-2*c)/3)==0)
 ck('unique deS curvature',s.simplify(R.subs(F,Fs)-2*c/a)==0)
 ck('deS full constraint',s.simplify(C.subs({F:Fs,P:0,H:s.sqrt(c/(6*a))}))==0)
 h,m0,m1,m2=s.symbols('h m0 m1 m2',positive=True)
 av=99*h*m1/4;bv=17*h*m0/12;cv=2115*h*m2/16;Dv=s.expand(4*bv*cv-av**2)
 ck('actual discriminant',s.expand(Dv-3*h**2*(3995*m0*m2-3267*m1**2)/16)==0)
 ck('moment-cone discriminant decomposition',s.expand(3995*m0*m2-3267*m1**2-(3995*(m0*m2-m1**2)+728*m1**2))==0)
 ck('fixed coefficient ratio',s.simplify(av**2/(4*bv*cv)/(m1**2/(m0*m2)))==s.Rational(3267,3995))
 ck('owned mass scale',s.simplify(av/(6*bv))==99*m1/(34*m0))
 d=s.symbols('d',real=True)
 ric2=9*(d+H**2)**2+3*(d+3*H**2)**2;rs=6*(d+2*H**2);riem2=12*((d+H**2)**2+H**4);gb=24*H**2*(H**2+d)
 ck('FLRW Weyl identically zero',s.expand(riem2-2*ric2+rs**2/3)==0)
 ck('Euler density',s.expand(riem2-4*ric2+rs**2-gb)==0)
 ck('Ricci to R2 Euler identity',s.expand(ric2-rs**2/3+gb/2)==0)
 ck('FLRW Euler boundary derivative',s.expand(8*(3*H*H**3+3*H**2*d)-gb)==0)
 V=U/(2*F**2);ck('Einstein potential',s.factor(V-(1+2*a/F-D/F**2)/(8*b))==0)
 ck('potential unique maximum derivative',s.factor(s.diff(V,F)-(D-a*F)/(4*b*F**3))==0)
 ck('potential maximum value',s.factor(V.subs(F,Fs)-c/(2*D))==0)
 ck('potential plateau excess',s.factor(V-1/(8*b)-(2*a*F-D)/(8*b*F**2))==0)
 alpha=s.sqrt(s.Rational(2,3));Vp=alpha*F*s.diff(V,F)
 ck('Einstein scalar mass at maximum',s.factor((alpha*F*s.diff(Vp,F)).subs(F,Fs)+mu/Fs)==0)
 HE,p,z=s.symbols('HE p z',real=True);Fp=alpha*F*p;pp=-3*HE*p-Vp
 ck('energy dissipation',s.factor(p*pp+s.diff(V,F)*Fp+3*HE*p**2)==0)
 zd=s.expand(Fp*p+F*pp);expected=-(3*HE-alpha*p)*F*p+alpha*a/(4*b)*(1-Fs/F)
 ck('rescaled momentum exact equation',s.factor(zd-expected)==0)
 Hi=1/s.sqrt(24*b);zi=alpha*a/(12*b*Hi);vi=s.simplify(alpha*zi)
 ck('late F prime',s.simplify(vi-a/(18*b*Hi))==0)
 ck('late Jordan F coefficient',s.simplify(vi**2/4-a*a/(54*b))==0)
 ck('late Jordan H coefficient',s.simplify(vi*Hi/2-a/(36*b))==0)
 ck('late Jordan R coefficient',s.simplify(vi**2/(8*b)-a*a/(108*b*b))==0)
 ck('late wkin coefficient',s.simplify(-2/(3*(a/(36*b)))+4/mu)==0)
 # Native Jordan versus Einstein transformed full constraint, not just a trace potential.
 HEj=(H+P/(2*F))/s.sqrt(F);pj=s.sqrt(s.Rational(3,2))*P/F**s.Rational(3,2)
 ck('frame Friedmann equivalence',s.factor(3*HEj**2-pj**2/2-V-C/F**2)==0)
 # At F0 the original Jordan system is polynomial and the constraint is finite.
 v=s.symbols('v',real=True)
 ck('Fzero crossing constraint',s.factor(C.subs({F:0,P:-v})-(D/(8*b)-3*H*v))==0)
 ck('Fzero Hdot finite',s.simplify(Hd.subs(F,0)-(a/(12*b)-2*H**2))==0)
 ck('upper-cone P boundary',s.factor(Pd.subs(P,0)-mu*(F-Fs))==0)
 ck('expanding H boundary',s.simplify(Hd.subs(H,0)-(F+a)/(12*b))==0)
 # Exact constraint-admitted controls on both sides of the same cone member.
 for sign in [-1,1]:
  eps=s.Rational(sign,10);H0=s.sqrt(s.Rational(1,6));F0=3+eps;P0=H0*eps+eps**2/(24*H0)
  ck('admitted cone fixture '+str(sign),s.simplify(C.subs({a:1,b:1,c:1,H:H0,F:F0,P:P0}))==0 and s.sign(P0)==sign)
 ck('fixture lies in actual moment cone',s.Rational(1,4)<s.Rational(3267,3995))
 # Conventional control: A>0 in A R+bR²−2AΛ gives positive scalar mass A/(6b).
 A,L=s.symbols('A L',positive=True);rr=s.symbols('rr',real=True);f=A*rr+b*rr**2-2*A*L;ff=s.diff(f,rr)
 ck('healthy-sign comparator deS',s.simplify((ff*rr-2*f).subs(rr,4*L))==0)
 ck('healthy-sign comparator mass',s.simplify((ff-rr*s.diff(ff,rr))/(3*s.diff(ff,rr))-A/(6*b))==0)
 return {'schema':'gu-cosmology-nonlinear-roll-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'exact_results':{'constraint_derivative':'-4H*C','D':'3h²(3995m0m2-3267m1²)/16','left_crossing':'H*(-Fdot)=D/(24b)','right_limits':{'F/tJ²':'a²/(54b)','HJ/tJ':'a/(36b)','RJ/tJ²':'a²/(108b²)','HJdot':'a/(36b)','tJ²(wkin+1)':'-24b/a'},'source_selected_prediction':False},'limits':['Finite controls and Lean do not formalize global ODE continuation, comparison, invariant manifold or asymptotic convergence.','Leading positive-reference local4D vacuum FLRW only, not full14D, sourceGU, physicalNewton or DESI/CMB.','Fzero is a scalar-frame boundary, not automatically a Jordan metric singularity.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
 print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t}))
