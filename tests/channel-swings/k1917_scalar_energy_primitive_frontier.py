#!/usr/bin/env python3
"""Exact finite algebra for K1917; universal scope belongs to the note's proof."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1917-scalar-energy-primitive-frontier.json'
def exact():
    t,h,e,D=s.symbols('t h e D',positive=True);tau=3*e/h;A=s.symbols('A',positive=True)
    rise=h*(t/tau)**2;fall=h*(1-t/tau)**2;bump=-6*A*t*(D-t)/D**3
    checks=[]
    def eq(a,b,label):
        assert s.simplify(a-b)==0,label
        checks.append(label)
    eq(s.integrate(rise,(t,0,tau)),e,'rising area')
    eq(s.integrate(fall,(t,0,tau)),e,'falling area')
    eq(s.integrate(s.diff(rise,t)**2,(t,0,tau)),4*h**3/(9*e),'rising energy')
    eq(s.integrate(s.diff(fall,t)**2,(t,0,tau)),4*h**3/(9*e),'falling energy')
    eq(rise.subs(t,0),0,'rise starts zero');eq(rise.subs(t,tau),h,'rise ends h')
    eq(fall.subs(t,0),h,'fall starts h');eq(fall.subs(t,tau),0,'fall ends zero')
    eq(s.integrate(bump,(t,0,D)),-A,'connector area')
    eq(s.integrate(s.diff(bump,t)**2,(t,0,D)),12*A**2/D**3,'connector energy')
    z=t*(D-t)*(t-D/2)
    eq(s.integrate(z,(t,0,D)),0,'zero-area perturbation')
    eq(s.integrate(s.diff(z,t)*s.diff(bump,t),(t,0,D)),0,'connector variational orthogonality')
    u=s.symbols('u',real=True);F=(1-u*u)**2*(2+u);phi=s.diff(F,u)
    Fo=(F+F.subs(u,-u))/2;po=(phi-phi.subs(u,-u))/2
    eq(s.diff(Fo,u),po,'reflection derivative sign')
    eq(Fo.subs(u,-1),0,'reflected endpoint')
    delta=s.integrate(s.diff(phi,u)**2-s.diff(po,u)**2,(u,-1,1))
    assert delta>0,'strict energy improvement for nonsymmetric input';checks.append('strict reflection energy contraction')
    g,ell=s.symbols('g ell',positive=True);A0=h*ell/2;C=16*h**3/9
    E=C/e+24*(A0+e)**2/(g-3*e/h)**3
    eq(s.limit(e*E,e,0,dir='+'),C,'sharp leading energy constant')
    eq(s.diff(t**3,t,4),0,'free cubic Euler equation')
    assert s.diff(t**4,t,4)!=0,'quartic is not free Euler solution';checks.append('contrary quartic')
    return checks

def payload():
    controls=exact();dep='explorations/conditional-build/k1915-scalar-pulse-duration-limits-2026-10-21.md'
    return {'result_id':'K1917','status':'active_research','evidence_kind':'analytic proof plus exact finite symbolic controls; no formal proof',
      'mathematical_controls':controls,'dependencies':{dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()},
      'formulas':{'A0':'theta*ell/4','C':'2*theta**3/9','construction':'C/epsilon+24*(A0+epsilon)**2/(g-3*epsilon/h)**3','joint_limit':'4*theta**3/(9*c)'},
      'scope':'symmetric interval and symmetric equal-length plateaux, arbitrary common real phase; smooth infimum asymptotics; relaxed finite-budget characterization',
      'not_claimed':['all-budget explicit optimum','finite-duration exact peak optimum','native GU','novelty','external expert review','formal proof']}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=payload()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'report consistency'
    print('PASS K1917 exact symbolic controls:',len(r['mathematical_controls']),'; report/pin checks separate')
