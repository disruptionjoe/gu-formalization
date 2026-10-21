#!/usr/bin/env python3
"""Exact algebra for the capped Fisher problem; analytic proofs live in the note."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1874-fisher-sixth-moment-cap.json'
def produce():
 d,t,M=s.symbols('d t M',positive=True);v=1-t;B=d+3*t*t;a2=B/t;w=t*t/B;k=d+3
 m2=v+w*a2;m4=3*v*v+6*v*w*a2+w*a2*a2
 m6=15*v**3+45*v*v*w*a2+15*v*w*a2*a2+w*a2**3
 cap=d*d/t+15*(1+d)-9*d*t-6*t**3;ck={}
 def test(name,expr):ck[name]=bool(expr);assert expr,name
 def eq(name,x,y):test(name,s.simplify(x-y)==0)
 eq('second_moment',m2,1);eq('fourth_moment',m4,k);eq('sixth_moment',m6,cap)
 eq('cap_derivative',s.diff(cap,t),-d*d/t**2-9*d-18*t*t)
 eq('endpoint_atomic_cap',cap.subs(t,1),k*k)
 eq('sharp_upper_limit',s.limit(cap*t/(1-t),t,0),d*d)
 eq('sharp_lower_limit',s.limit(M*d*d/(M-k*k),M,s.oo),d*d)
 eq('projected_score_norm',M-2*k*k+k*k,M-k*k)
 eq('projected_score_pairing',(k-3)-k*0,d)
 eq('weight_complement',1-w,(d+2*t*t)/B)
 eq('fisher_excess_upper',1/v-1,t/(1-t))
 eta=s.symbols('eta',positive=True);eq('accuracy_trial', (t/(1-t)).subs(t,eta/(1+eta)),eta)
 eq('budget_sharp_limit',s.limit(eta*cap.subs(t,eta/(1+eta)),eta,0),d*d)
 test('k4_M100_trial',cap.subs({d:1,t:s.Rational(1,70)})<100)
 eq('k4_M100_upper_excess',(t/(1-t)).subs(t,s.Rational(1,70)),s.Rational(1,69))
 eq('k4_M100_lower_excess',(d*d/(M-k*k)).subs({d:1,M:100}),s.Rational(1,84))
 test('k4_one_percent_trial',cap.subs({d:1,t:s.Rational(1,101)})<131)
 eq('k4_one_percent_necessary', (k*k+d*d/s.Rational(1,100)).subs(d,1),116)
 x,c=s.symbols('x c');logu=c*x**4/8-(c*k+1)*x*x/4
 eq('equality_score',2*s.diff(logu,x),c*(x**3-k*x)-x)
 eq('atomic_outer_weight', (1/k)*k,1)
 eq('atomic_fourth',(1/k)*k*k,k)
 eq('atomic_sixth',(1/k)*k**3,k*k)
 gap,c,slack,D=s.symbols('gap c slack D',positive=True)
 eq('cap_energy_excess',D+c*((M-slack)-M),D-c*slack)
 h,u=s.Function('h')(x),s.Function('u')(x)
 integrand=4*s.diff(h,x)**2+4*s.diff(u,x,2)*h*h/u-4*u*u*s.diff(h/u,x)**2
 eq('ground_state_identity',integrand,4*s.diff(h*h*s.diff(u,x)/u,x))
 return {'result_id':'K1874','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','formula':{'delta':'k-3','cap_coefficients':['1','15','15','-9','-6'],'moment_shift':3,'projection_coefficient':'k','lower_denominator':'M-k^2','sharp_large_cap_coefficient':'(k-3)^2'},'scope':{'k_gt_3':True,'raw_moments':True,'sixth_constraint':'inequality','attained':True,'all_minimizers_saturate_cap':True,'even_minimizer_exists':True,'uniqueness_proved':True,'positive_sextic_multiplier':True,'computed_gap':False,'mixture_fisher_is_exact':False,'GU_physics':False},'checks':ck,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/k1856-fisher-tail-phase-2026-10-20.md','explorations/k1855-fisher-gaussian-endpoint-2026-10-20.md']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1874',len(z['checks']),'symbolic algebra groups;',len(z['inputs']),'pins')
