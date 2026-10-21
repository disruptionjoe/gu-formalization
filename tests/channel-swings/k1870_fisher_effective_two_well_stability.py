#!/usr/bin/env python3
"""Exact constants behind the analytic localized-oscillator proof (not a PDE proof)."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1870-fisher-effective-two-well-stability.json'
def produce():
 r,d,v,t=s.symbols('r d v t',positive=True); checks={}
 def ck(k,x): checks[k]=bool(x);assert x,k
 ck('feasible_gaussian_fourth',s.expand((1-v)**2+6*(1-v)*v+3*v*v)==1+4*v-2*v*v)
 ck('trial_delta',s.simplify((4*v-2*v*v)-2*(1-(1-v)**2))==0)
 ck('rationalized_trial_energy',s.simplify((2*(1+(1-v))/(4*v-2*v*v))-1/v)==0)
 a=(1-r/2)**-2
 # a-1 <= (14/9)r for 0<r<=1/2: the difference has positive factors.
 slack=s.factor(s.Rational(14,9)*r-(a-1))
 ck('moment_slack_factor',s.simplify(slack-r*(1-2*r)*(20-7*r)/(9*(2-r)**2))==0)
 ck('cutoff_energy',s.simplify((1+1/r)*4*(r**3)**2/r**4-4*r-4*r*r)==0)
 ck('energy_constant',s.Rational(1,4)+4+2+2+s.Rational(7,18)==s.Rational(311,36))
 ck('energy_roundup',s.Rational(311,36)<9)
 ck('deficit_roundup',s.Rational(3,2)/16<=s.Rational(1,8))
 psi=s.exp(-t*t/4)
 ck('oscillator_ground',s.simplify(-s.diff(psi,t,2)+t*t*psi/4-psi/2)==0)
 ck('oscillator_first_gap',s.simplify(-s.diff(t*psi,t,2)+t*t*(t*psi)/4-s.Rational(3,2)*t*psi)==0)
 ck('simple_even_constant',8+12==20)
 ck('simple_mean_zero_constant',s.Rational(41,2)<21)
 ck('accuracy_example',21*s.Rational(1,10000)+s.Rational(1,10000)==s.Rational(11,5000))
 ck('four_product_accuracy',4*s.Rational(11,5000)<s.Rational(1,100))
 ck('sqrt_energy_example',s.Rational(1,50000000)/2==s.Rational(1,10000)**2)
 return {'result_id':'K1870','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','constants':{'delta_max':'1/8','cutoff_radius':'delta^(1/3)','lost_mass_factor':4,'oscillator_defect_radius_factor':9,'oscillator_defect_energy_factor':'1/8','even_TV_radius_factor':20,'mean_zero_TV_radius_factor':21,'TV_energy_sqrt_factor':'1/2','example_delta_max':'1/10^24','example_scaled_energy_slack':'1/50000000','example_TV':'11/5000','example_product_count':4},'scope':{'effective_endpoint_TV':True,'fixed_delta_deficit_modulus':False,'entropy_bound':False,'sharp_gap':False,'source_owned':False,'novelty_claim':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1858-fisher-two-well-profile.json','lab/process/k1868-fisher-two-well-instability.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1870',len(v['checks']),'exact mathematical checks;',len(v['inputs']),'dependency pins')
