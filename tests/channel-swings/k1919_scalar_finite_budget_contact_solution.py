#!/usr/bin/env python3
"""Exact polynomial identities; global optimum is proved in the companion note."""
import sympy as s
from pathlib import Path
import hashlib,json,argparse
ROOT=Path(__file__).resolve().parents[2]; REPORT=ROOT/'lab/process/k1919-scalar-finite-budget-contact-solution.json'
def payload():
    h,a,g,d,t,z,l=s.symbols('h a g d t z l',positive=True);D=a**3+g**3;p=h*g/2-g**3*d/D;v=h*a/2-a**3*d/D
    outer=(3*z/l**2-h/l)*t**2+(h/l**2-2*z/l**3)*t**3
    inner=h*t+(3*z/l**2-2*h/l)*t**2+(h/l**2-2*z/l**3)*t**3
    labels=[]
    def eq(x,y,label):assert s.simplify(x-y)==0,label;labels.append(label)
    for f,start,end,tag in [(outer,0,h,'outer'),(inner,h,0,'inner')]:
        eq(f.subs(t,0),0,tag+' initial value');eq(f.subs(t,l),z,tag+' final value')
        eq(s.diff(f,t).subs(t,0),start,tag+' initial slope');eq(s.diff(f,t).subs(t,l),end,tag+' final slope')
        eq(s.integrate(s.diff(f,t,2)**2,(t,0,l)),12*z*z/l**3-12*h*z/l**2+4*h*h/l,tag+' energy')
    eq(p+v,h*(g+a)/2-d,'allocation')
    jg=s.diff(outer,t,3).subs({l:g,z:p});ja=s.diff(inner,t,3).subs({l:a,z:v})
    eq(jg,12*d/D,'outer shear');eq(ja,jg,'matching shear')
    J=lambda L,Z:12*Z*Z/L**3-12*h*Z/L**2+4*h*h/L
    eq(2*(J(g,p)+J(a,v)),2*h*h*(1/g+1/a)+24*d*d/D,'global energy')
    eq(s.diff(outer,t),t*((6*z/l**2-2*h/l)+(3*h/l**2-6*z/l**3)*t),'outer sign factor')
    eq(s.diff(inner,t),(1-t/l)*(h+(6*z/l-3*h)*t/l),'inner sign factor')
    cases=[]
    for A,G,H,ell,delta in [(1,1,1,1,s.Rational(1,4)),(1,2,1,1,s.Rational(3,8)),(2,1,2,3,s.Rational(1,4))]:
        DD=A**3+G**3; dm=s.Rational(H*DD,6*max(A*A,G*G));E0=2*H*H*(s.Rational(1,A)+s.Rational(1,G));Ac=H*(ell+s.Rational(A+G,2))
        assert 0<=delta<=dm,'candidate interval';labels.append('candidate interval')
        cases.append(dict(a=str(A),g=str(G),h=str(H),ell=str(ell),delta=str(delta),A=str(Ac-delta),energy=str(E0+24*delta**2/DD)))
    r=s.symbols('r',positive=True);pp=h*l*(s.Rational(1,2)-1/(6*r**2));tau=l*r
    center=h*(1-t/tau)**2
    eq(s.integrate(s.diff(center,t)**2,(t,0,tau)),4*h*h/(3*tau),'contact interval energy')
    eq(s.integrate(center,(t,0,tau)),h*tau/3,'contact rise')
    eq(s.diff(outer,t,3).subs(z,pp),2*h/tau**2,'contact shear match')
    eq(2*J(l,pp)+8*h*h/(3*tau),h*h/l*(2+2/(3*r**4)+8/(3*r)),'contact full energy')
    eq(outer.subs(z,pp).subs(t,l*(1-r*r)),-h*l*(1-r*r)**3/(6*r*r),'outer negative minimum')
    eq((2+2/(3*r**4)+8/(3*r)).subs(r,s.Rational(1,2)),18,'energy18 example')
    dep='explorations/conditional-build/k1917-scalar-energy-primitive-frontier-2026-10-22.md'
    return dict(result_id='K1919',status='active_research',evidence_kind='analytic variational inequality plus exact symbolic controls',mathematical_controls=labels,cases=cases,energy_formula='E0+24*(Ac-A)^2/(a^3+g^3)',smooth_budget='E0<E<=E1; equal-gap continuation through first lower contact; E<=E0 empty',dependencies={dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()},not_claimed=['all-budget contact classification','finite-duration optimum','native GU','novelty','formal proof'])
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=payload()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'report consistency'
    print('PASS K1919 exact symbolic controls',len(r['mathematical_controls']))
