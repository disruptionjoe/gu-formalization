#!/usr/bin/env python3
"""Exact algebra supporting the analytic all-parameter Fisher gap proof."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1872-fisher-global-deficit-modulus.json'
def produce():
 d,k,y,b,F=s.symbols('delta k y b F',positive=True);checks={}
 def ck(n,v): checks[n]=bool(v);assert v,n
 a=F-2*b*k;E=2*F-b*k
 ck('virial_Q',s.expand(a*y+b*y*y-E-(b*(y*y-2*k*y+k)+F*(y-2)))==0)
 ck('secant_bound',s.simplify((8/d-F)/(d/2)-(16/d**2-2*F/d))==0)
 v=s.symbols('v',positive=True)
 ck('mixture_moment',s.expand(3*v*v+6*v*(1-v)+(1-v)**2-(1+4*v-2*v*v))==0)
 ck('mixture_inverse',s.simplify(1/(1-s.sqrt(1-d/2))-2*(1+s.sqrt(1-d/2))/d)==0)
 ck('tail_polynomial_at_9',9**2-6*9+3==30)
 ck('tail_translation',s.Poly(s.expand((y+9)**2-6*(y+9)+3),y).all_coeffs()==[1,12,30])
 ck('compact_absolute_polynomial',16**2+2*3*16+3==355)
 ck('compact_absolute_linear',max(2,16-2)==14)
 ck('compact_Q_constants',16*355/4==1420 and 4*14/4==14)
 ck('compact_kappa',1420+14*2==1448 and 1448<40**2)
 ck('B_prefactor',s.Rational(3)*s.Rational(7,2)*4==42)
 ck('exponential_margin',sum(s.Rational(4)**j/s.factorial(j) for j in range(7))>43)
 ck('gap_exponent',12*40+8==488)
 ck('TV_exponent',488/2==244)
 ck('a_error_bound',4*2+2*16*3==104)
 ck('sobolev_constant',2*3**2*16+8*2==304)
 ck('sobolev_distance_factor',2*304==608)
 return {'result_id':'K1872','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','parameters':{'delta_open_interval':['0','2'],'F_upper_numerator':4,'b_upper_numerator':16,'R':3,'L':4,'kappa_numerator':40,'gap_exponent_numerator':488,'TV_exponent_numerator':244,'a_error_numerator':104,'b_error_numerator':16,'Sobolev_numerator':608},'claims':{'all_parities':True,'balance_required':False,'fixed_delta_vanishing_deficit':True,'uniform_positive_endpoint_gap':False,'practical_tunneling_constant':False,'entropy_bound':False,'native_GU_credit':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/k1843-unrestricted-fisher-variational-gap-2026-10-20.md','explorations/k1849-fisher-effective-gap-2026-10-20.md','explorations/k1853-fisher-practical-gap-2026-10-20.md','explorations/k1868-fisher-two-well-instability-2026-10-20.md']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();result=produce()
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1872',len(result['checks']),'symbolic/algebra controls;',len(result['inputs']),'dependency pins')
