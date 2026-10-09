#!/usr/bin/env python3
"""Certificate for K1604's conditional spectral analytic-radius budget."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1604-spectral-analytic-radius-budget.json').read_text());q=d['spectral_budget'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1604'),('BE','B_E=B_0+B_3/2' in q['definitions']),('Ba','B_a=B_0/2+B_3' in q['definitions']),('a square','int|a|^2<=B_E B_a' in q['definitions']),('bare exponent','2|e|B_a+(e^2/m)B_E B_a' in q['bare_energy']),('remainders','curvature' in q['remainder'] and 'current' in q['remainder']),('BA bound','B_A(t)<=|e||a(t)|+R(t)' in q['remainder']),('rho formula','rho_infinity>=rho_0' in q['radius']),('positive condition','<rho_0' in q['positive_budget']),('scope conditional','conditional on the spectral representation' in q['scope_guard'])]
 B0,B3,e,m,Cm,BR,rho0=1.0,.5,.7,2.0,1.2,.1,1.0;BE=B0+B3/2;Ba=B0/2+B3;expo=2*abs(e)*Ba+(e*e/m)*BE*Ba;spend=(Cm/4)*(abs(e)*Ba+BR)
 c += [('bare finite',math.exp(expo)<20),('radius positive',rho0-spend>0),('D M conditional',z['d_prime_m_prime_budget_closed_conditionally']),('energy conditional',z['bare_energy_uniform_bound_proved_conditionally']),('radius conditional',z['positive_limiting_radius_proved_conditionally']),('remainders open',not z['curvature_current_remainders_derived']),('flow open',not z['source_owned_global_flow_constructed']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
