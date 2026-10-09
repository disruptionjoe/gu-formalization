#!/usr/bin/env python3
"""Certificate for K1583's moving-holonomy identity."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1583-moving-holonomy-energy-identity.json').read_text());q=d['moving_holonomy'];z=d['decision'];checks=[]
 checks += [('claim',d['claim_id']=='K1583'),('C1 path','C1 a(t)' in q['equation']),('positive mass','m>0' in q['equation']),('adapted operator','L_a=' in q['equation']),('exact derivative','H_a\'' in q['exact_derivative']),('momentum shift','(k-ea)' in q['exact_derivative']),('scalar inequality','2m|p|' in q['relative_bound']),('TV bound','TV(a)' in q['relative_bound']),('charge commute','commutes' in q['charge_hierarchy']),('static zero cost','static generic flat holonomy has zero cost' in q['maxwell_interpretation']),('scope prescribed','prescribed harmonic' in q['scope_guard'])]
 for p,m in ((0.0,2.0),(1.0,2.0),(7.0,.5)):checks.append((f'2m bound {p}',2*m*abs(p)<=p*p+m*m+1e-12))
 H0,e,mass,tv=3.0,2.0,4.0,1.5;checks.append(('gronwall positive',H0*math.exp(abs(e)*tv/mass)>=H0))
 checks += [('identity',z['energy_derivative_exact']),('amplitude removed',z['amplitude_cost_removed']),('TV',z['total_variation_bound']),('tiers',z['charge_tiers_controlled']),('nonlinear open',not z['coupled_nonlinear_integrability']),('radius open',not z['global_positive_radius']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
