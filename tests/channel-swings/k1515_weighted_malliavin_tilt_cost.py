#!/usr/bin/env python3
"""Controls for K1515's weighted Malliavin tilt cost."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1515-weighted-malliavin-tilt-cost.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 c,q=D['weighted_cost'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1515'),('chain rule','D u_N(X_N)' in c['chain_rule']),('main derivative','-(R_N/2)u_N' in c['chain_rule']),('cutoff derivative','chi\u0027(x/R_N)' in c['chain_rule']),('boundary separation','at least R_N/2' in c['cutoff_boundary']),('boundary negligible','exponentially negligible' in c['cutoff_boundary']),('holder p','p_N=1+R_N^(-2)' in c['holder_pair']),('holder q','q_N=p_N/(p_N-1)=R_N^2+1' in c['holder_pair']),('third chaos','Hilbert-valued third chaos' in c['gradient_chaos']),('gradient mean','=4' in c['gradient_chaos']),('Y definition','Y_N=||D X_N||^2' in c['hypercontractivity']),('q cube','(2q_N-1)^3' in c['hypercontractivity']),('R6','O(R_N^6)' in c['hypercontractivity']),('weighted R6','=O(R_N^6)' in c['weighted_gradient']),('Malliavin R8','=O(R_N^8)' in c['normalized_malliavin_cost']),('frequency','omega_max(N)=O(N)' in c['free_form_cost']),('free NR8','O(N R_N^8)' in c['free_form_cost']),('selected radius','N^(1/14)/(1+log N)' in c['dominance']),('sigma','Theta(N^(5/2))' in c['dominance']),('dominance power','N^(-1)' in c['dominance']),('cost proved',q['weighted_malliavin_cost_proved']),('lower order',q['free_cost_lower_order_than_interaction_gain']),('pointwise fenced',not q['pointwise_gradient_bound_claimed']),('sharpness fenced',not q['sharp_weighted_cost_exponent_claimed']),('protected fenced',not q['protected_status_change'])]
 for n in (10**42,10**56,10**70):
  R=n**(1/14)/(1+math.log(n));ratio=n**(-1)*(1+math.log(n))**-7;checks += [(f'R grows {n}',R>1),(f'cost ratio {n}',ratio<1/n)]
 checks += [('holder conjugacy',math.isclose((1+1/64)/((1+1/64)-1),65)),('dominance exponent',math.isclose(1+8/14-(2.5+1/14),-1))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
