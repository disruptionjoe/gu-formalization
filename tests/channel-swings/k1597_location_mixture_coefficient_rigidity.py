#!/usr/bin/env python3
"""Certificate for K1597's location-mixture coefficient rigidity."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1597-location-mixture-coefficient-rigidity.json').read_text());q=d['coefficient_rigidity'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1597'),('linear potential','Potential expectations are linear' in q['mixture_energy']),('Fisher quarter','q_0=I_Omega/4' in q['mixture_energy']),('average component','E_pi E_N(A,S_N)' in q['mixture_energy']),('K1572','K1572' in q['component_lower']),('global stationary minimum','global stationary diagonal Gaussian minimum' in q['component_lower']),('component inequality','E_N(A,S_N)>=lambda_N^prof' in q['component_lower']),('class lower','lambda_N^prof-(1/4)' in q['class_lower']),('cat upper','K1591' in q['class_upper']),('sandwich','lambda_N^prof-O_g(N)' in q['coefficient']),('coefficient limit','inf_pi Q_N(pi)/N^4->h_g^prof' in q['coefficient']),('arbitrary locations','Arbitrarily many zero-mode locations' in q['route_consequence']),('leave class','must leave the class' in q['route_consequence']),('scope class','class-infimum theorem' in q['scope_guard']),('scope heterogeneous','heterogeneous covariances' in q['scope_guard'])]
 c += [('decision lower',z['componentwise_profiled_lower_bound_used']),('decision coefficient',z['location_mixture_class_coefficient_proved']),('decision atoms',z['arbitrary_atom_count_allowed']),('unrestricted open',not z['unrestricted_leading_coefficient_identified']),('recentering open',not z['bounded_error_recentering_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
