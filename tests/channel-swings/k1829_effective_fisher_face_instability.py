#!/usr/bin/env python3
"""Rational all-interval witnesses for the analytic Gaussian-overlap proof."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1829-effective-fisher-face-instability.json'
def produce():
    exp_upper=F(factorial(32),32**32) # exp(-32) < this single-term reciprocal
    cases=[]
    for inv_v,a in [(4096,F(1,128)),(16384,F(1,512))]:
        assert a*inv_v==32 and F(1,inv_v)<a/2
        error=168*inv_v**2*exp_upper
        assert error<F(7,144)
        cases.append({'inverse_v':inv_v,'exponent_coefficient':str(a),'scaled_error_upper':str(error),'half_margin_lower':'7/144','q_lower':str(2*(1-F(1,inv_v))**2)})
    # kappa(1/4)-kappa(1/2) and two error terms certify direction ordering.
    gap=F(39,100)-F(7,36)
    assert 2*F(cases[1]['scaled_error_upper'])<gap/2
    assert 12*(6*F(16,9)+3*F(19,24)+F(7,8))==167<168
    assert F(512**32,factorial(32))>1706*1024*4096**5
    assert 2*6400*4*(2*10**7)+7200*4*10**6 < 2*10**12
    return {'result_id':'K1829','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','constants':{'overlap_constant':168,'exp_minus_32_upper':str(exp_upper),'single_direction_r':'1/2','uniform_direction_r_interval':['1/4','1/2']},'interval_certificates':cases,'results':{'single_direction_derivative_upper':'-7t/(72v^2)','uniform_direction_derivative_upper':'-kappa(r)t/(2v^2)','kappa':'1/(1+r)^2-1/4','z_15_over_16_derivative_less_than_z_3_over_4_on_uniform_interval':True,'boundary_second_variation_lower':'exp(1/(8v))/(1024*v^(3/2))-1706/v^6', 'boundary_second_variation_positive_for_v_le':'1/4096','true_transition_located':False,'explicit_finite_descent_step':'7*v^4*exp(-32/v)/(288*10^12)','uniform_second_derivative_upper':'2*10^12*v^-6*exp(32/v)','minimizing_displacement_identified':False,'global_shape_uniqueness':False,'z_one_face_excluded':False,'physical_or_canon_promotion':False},'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1827-endpoint-fisher-asymptotic.json','lab/process/k1825-global-q-fisher-transfer.json']}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(OUT.read_text())==d,'certificate drift'
    print('PASS K1829: two exact interval witnesses, uniform constant, direction ordering and pinned inputs')
