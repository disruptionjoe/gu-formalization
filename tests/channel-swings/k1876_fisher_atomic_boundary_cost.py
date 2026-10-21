#!/usr/bin/env python3
"""Exact algebra for the atomic-boundary Fisher theorem; continuum proof is in the note."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1876-fisher-atomic-boundary-cost.json'
def produce():
 checks={}
 def ck(n,v):checks[n]=bool(v);assert v,n
 x,k,a,t,y=s.symbols('x k a t y',positive=True)
 g=x**3-k*x;psi=(x*x-a)/(x*x+a)*g
 L=k+(k-3*a)*x*x/(k+a)
 R=2*(a*(5*a+3*k)+(3*a+k)*x*x)/((a+k)*(a+x*x)**2)
 ck('test_remainder',s.factor(s.diff(psi,x)-L-x*g*R)==0)
 ck('test_square_domination',s.factor(g*g-psi*psi-4*a*x*x*g*g/(x*x+a)**2)==0)
 ck('R_majorant',s.factor(2*(5*a+3*k)/((a+k)*(a+x*x))-R-4*x*x/(a+x*x)**2)==0)
 ck('sqrt_bound_square',s.expand((a+x*x)**2-4*a*x*x-(x*x-a)**2)==0)
 ck('atomic_expectation',s.simplify((1-1/k)*s.diff(psi,x).subs(x,0)+s.diff(psi,x).subs(x,s.sqrt(k))/k-(k+1-4*a/(k+a)))==0)
 w=(1-t)/(y-t/2)
 m2=(1-w)*t+w*(y+t/2)
 m4=3*(1-w)*t*t+w*(y*y+3*y*t+s.Rational(3,4)*t*t)
 m6=15*(1-w)*t**3+w*(y**3+s.Rational(15,2)*y*y*t+s.Rational(45,4)*y*t*t+s.Rational(15,8)*t**3)
 F=(1-t)*y*y+(3*t-k)*y+k*t/2-9*t*t/4+3*t**3/4
 ck('second_moment',s.factor(m2-1)==0)
 ck('fourth_constraint',s.factor((m4-k)*(y-t/2)-F)==0)
 ck('implicit_jacobian',s.diff(F,y).subs({t:0,y:k})==k)
 yp=k-s.Rational(7,2)
 ck('root_derivative',s.simplify((s.diff(F,t)+s.diff(F,y)*yp).subs({t:0,y:k}))==0)
 ck('sixth_slack_derivative',s.simplify((s.diff(m6,t)+s.diff(m6,y)*yp).subs({t:0,y:k})-k*(k+1))==0)
 ck('cost_leading',s.simplify((1+w).subs({t:0,y:k})*k*(k+1)-(k+1)**2)==0)
 # Optimal leading allocation for central and outer variance coefficients c0,c1.
 c0,c1=s.symbols('c0 c1',positive=True);p0=1-1/k;p1=1/k
 gap=s.factor((p0/c0+p1/c1)*(p0*k*k*c0+p1*4*k*k*c1)-(k+1)**2)
 ck('allocation_identity',s.factor(gap-(k-1)*(c0-2*c1)**2/(c0*c1))==0)
 # Exact narrow value bracket at k=4, M=16+10^-12. Root enclosure, not float rounding.
 tt=s.Rational(1,20001000000000);dd=s.Rational(1,10**12);lo=4+tt/2-10*tt*tt;hi=4+tt/2+10*tt*tt
 ff=lambda yy:F.subs({k:4,t:tt,y:yy})
 ck('root_left',ff(lo)<0);ck('root_right',ff(hi)>0)
 ck('root_monotone',2*(1-tt)*lo+3*tt-4>0)
 wl=(1-tt)/(hi-tt/2);wh=(1-tt)/(lo-tt/2)
 ck('weights',0<wl<wh<1)
 # All positive Gaussian moment terms: independent interval enclosure is intentionally loose.
 m6up=15*tt**3+wh*(hi**3+s.Rational(15,2)*hi*hi*tt+s.Rational(45,4)*hi*tt*tt+s.Rational(15,8)*tt**3)
 ck('budget_feasible',m6up<16+dd)
 ck('scaled_upper',dd*(1+wh)/tt<s.Rational(12501,500))
 aa=s.Rational(1,10000)
 lower=5-4*aa/(4+aa)-(5*aa+12)/(4+aa)*s.sqrt(dd/aa)
 ck('scaled_lower',lower>s.Rational(9999,2000))
 return {'result_id':'K1876','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','coefficients':{'atomic_cost':'(k+1)^2','slack_derivative':'k*(k+1)','variance_ratio':2,'remainder_bound':'(5*a+3*k)/((a+k)*sqrt(a))'},'finite_example':{'k':'4','slack':'1/1000000000000','t':str(tt),'scaled_value_lower':'99980001/4000000','scaled_value_upper':'12501/500'},'scope':{'k_gt_3':True,'raw_second_one':True,'sixth_inequality':True,'continuum_proof':'analytic note, not certified by symbolic pass count','exact_optimizer_coefficients_computed':False,'native_GU_verdict':False,'novelty_claim':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/k1874-fisher-sixth-moment-cap-2026-10-20.md','lab/process/k1874-fisher-sixth-moment-cap.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1876',len(v['checks']),'symbolic/rational groups;',len(v['inputs']),'pins')
