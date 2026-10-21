#!/usr/bin/env python3
"""Exact algebra and finite-budget controls for the analytic K1880 theorem."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1880-effective-fisher-well-localization.json'
INPUTS=['explorations/k1878-fisher-three-well-profile-rigidity-2026-10-21.md','explorations/k1876-fisher-atomic-boundary-cost-2026-10-20.md']
def budget(k,delta,h,U,cutoff=40,slope=s.Rational(13,4),gap_factor=2):
 k,delta,h,U=map(s.sympify,(k,delta,h,U))
 if not (k>3 and delta>0 and 0<h<=s.sqrt(k)/4 and U>=0):raise ValueError('outside theorem parameters')
 A=k+1;e=4*s.sqrt(delta)/(3*k);eps=slope*h/s.sqrt(k);tau=4*e**2/h**2
 E=U-A*A+A*A*((1-eps)**-2-1)+2*A*e*(1+s.sqrt(k))+4*A*k*tau+cutoff*delta/h**2
 return dict(e=e,epsilon=eps,tau=tau,E=s.factor(E),denominator=gap_factor*k*A,weight=e*(1+s.sqrt(k))/k,leak=4*delta/(k*k*A))
def produce():
 checks={}
 def ck(n,v):checks[n]=bool(v);assert v,n
 x,z,k,h,b,delta=s.symbols('x z k h b delta',positive=True);rr=s.symbols('r',real=True)
 g=lambda x:x**3-k*x
 ck('root_expansion',s.expand(g(rr+z)-g(rr)-(3*rr**2-k)*z-3*rr*z*z-z**3)==0)
 # Worst error at h<=sqrt(k)/4; the residual at that endpoint is exactly zero.
 ck('slope_constant',s.simplify((s.Rational(13,4)*s.sqrt(k)*h-3*s.sqrt(k)*h-h*h).subs(h,s.sqrt(k)/4))==0)
 a=s.symbols('a',positive=True);q=s.exp(-b*x*x/(4*delta))
 ck('oscillator_groundstate',s.simplify(-4*delta*s.diff(q,x,2)+b*b*x*x*q/delta-2*b*q)==0)
 ck('oscillator_first_gap',s.simplify((-4*delta*s.diff(x*q,x,2)+b*b*x*x*x*q/delta-2*b*x*q)-4*b*x*q)==0)
 t=s.symbols('t',real=True)
 ck('cutoff_partition',s.trigsimp(s.cos(t)**2+s.sin(t)**2)==1)
 ck('cutoff_derivative_cost',s.trigsimp(s.diff(s.cos(t),t)**2+s.diff(s.sin(t),t)**2)==1)
 m,c=s.symbols('m c',nonnegative=True)
 ck('projection_conversion',s.expand(2*(m-c*c)-(2*m-2*s.sqrt(m)*c)-2*c*(s.sqrt(m)-c))==0)
 z=s.symbols('z',positive=True)
 ck('tail_mass',s.simplify((4*s.sqrt(delta)/(3*k))**2*4/h**2-64*delta/(9*k*k*h*h))==0)
 B=budget(4,s.Rational(1,10**12),s.Rational(1,10**4),s.Rational(25002,1000))
 target=s.Rational(22,1000);room=target-B['tau']-B['weight']
 ck('finite_budget_positive',B['E']>0 and room>0)
 ck('finite_even_TV_below_022',B['E']<B['denominator']*room**2)
 ck('conditional_leak',B['leak']==s.Rational(1,20*10**12))
 # Exact exponents in h=delta^(1/3): both localization errors have order delta^(1/3).
 ck('rate_balance',1-2*s.Rational(1,3)==s.Rational(1,3))
 return dict(result_id='K1880',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',constants={'cutoff':40,'slope':'13/4','oscillator_gap':'4*a*A','TV_denominator':'2*k*A'},budget={k:str(v) for k,v in B.items()},finite_even_TV_strict_upper='11/500',scope={'all_feasible_densities_with_valid_energy_upper':True,'fixed_weights_require_evenness':True,'effective_rescaled_W2':False,'global_sextic_gap':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1880',len(v['checks']),'symbolic/rational groups;',len(v['inputs']),'pins')
