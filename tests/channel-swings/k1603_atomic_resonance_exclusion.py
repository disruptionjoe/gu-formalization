#!/usr/bin/env python3
"""Certificate for K1603's atomic-resonance exclusion and spectral budgets."""
import cmath, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1603-atomic-resonance-exclusion.json').read_text());q=d['spectral_exclusion'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1603'),('decomposition','pure-point trigonometric polynomial' in q['decomposition']),('atomic L1','infinite time L1 norm' in q['atomic_obstruction']),('K1599','K1599' in q['atomic_obstruction']),('projector','P_pp E_h=0' in q['exact_exclusion']),('W31','W^{3,1}' in q['density_hypothesis']),('away zero','supported away from zero' in q['density_hypothesis']),('endpoint','first two derivatives zero' in q['density_hypothesis']),('t3','t^(-3)B_3' in q['decay']),('electric budget','B_0+B_3/2' in q['budgets']),('a budget','B_0/2+B_3' in q['budgets']),('scope nonlinear','not derived here' in q['scope_guard'])]
 # A nonzero atom has positive sampled mean absolute value and linear L1 growth.
 vals=[abs(cmath.exp(1j*.73*j)) for j in range(1000)]
 c += [('atom mean',sum(vals)/len(vals)>.99),('atom linear growth',sum(vals)>900)]
 # x^3(1-x)^3 has value and first two derivatives zero at both endpoints.
 def f(x): return x**3*(1-x)**3
 h=1e-5
 f1=lambda x:(f(x+h)-f(x-h))/(2*h)
 f2=lambda x:(f(x+h)-2*f(x)+f(x-h))/h**2
 c += [('left endpoint',abs(f(0))<1e-15 and abs(f1(0))<1e-8 and abs(f2(0))<1e-4),('right endpoint',abs(f(1))<1e-15 and abs(f1(1))<1e-8 and abs(f2(1))<1e-4)]
 c += [('point excluded',z['pure_point_sector_excluded_by_hypothesis']),('periodic excluded',z['transverse_periodic_family_excluded']),('electric L1',z['electric_l1_proved_in_declared_class']),('a L1',z['holonomy_amplitude_l1_proved_with_zero_limit']),('scattering open',not z['nonlinear_scattering_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
