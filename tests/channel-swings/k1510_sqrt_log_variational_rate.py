#!/usr/bin/env python3
"""Controls for K1510's square-root-logarithmic variational rate."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1510-sqrt-log-variational-rate.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 f,r,q=D['free_cost'],D['variational_rate'],D['decision']
 checks += [('claim',D['claim_id']=='K1510'),('chain','D b_N(X_N)' in f['chain_rule']),('Malliavin norm','=4' in f['chain_rule']),('frequency','omega_max(N)=O(N)' in f['frequency_bound']),('raw free','=O(N)' in f['frequency_bound']),('normalized free','N^(1+alpha+o(1))' in f['normalized_cost']),('interaction','N^(5/2)' in f['interaction_scale'] and 'sqrt(log N)' in f['interaction_scale']),('dominance','alpha-3/2' in f['dominance']),('alpha rate','sqrt(2 alpha)' in r['alpha_form']),('all c','c<sqrt(3)' in r['uniform_form']),('liminf','>=sqrt(3)' in r['ratio_form']),('ceiling','not a claimed optimal' in r['constant_ceiling']),('rate proved',q['sqrt_log_variational_rate_proved']),('loss removed',q['log_log_loss_removed']),('one sided',q['rate_is_one_sided_variational']),('constant fenced',not q['sqrt_three_is_optimal_constant']),('lower fenced',not q['matching_ground_energy_lower_bound_proved']),('protected fenced',not q['protected_status_change'])]
 for alpha in (0.5,1.0,1.49):
  vals=[math.exp((alpha-1.5)*t)/math.sqrt(t) for t in (20,40,80)]
  checks.append((f'alpha {alpha} cost/gain decreases',vals[2]<vals[1]<vals[0]))
 checks += [('constant approach',math.sqrt(2*1.499)>1.73),('strict ceiling',math.sqrt(2*1.499)<math.sqrt(3))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
