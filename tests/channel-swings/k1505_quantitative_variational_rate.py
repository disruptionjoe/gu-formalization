#!/usr/bin/env python3
"""Controls for K1505's quantitative variational rate."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1505-quantitative-variational-rate.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 s,r,q=D['scale_comparison'],D['variational_rate'],D['decision']
 checks += [('claim',D['claim_id']=='K1505'),('degree','log N/log log N' in s['degree']),('chaos','4d_N' in s['chaos_ceiling']),('free','O(N d_N)' in s['free_cost']),('gain','sigma_N/2' in s['interaction_gain'] and 'sqrt(d_N)' in s['interaction_gain']),('dominance','N^(3/2)' in s['dominance'] and 'N^(5/2)' in s['dominance']),('energy rate','sqrt(log N/log log N)' in r['energy_bound']),('ratio rate','sqrt(log N/log log N)' in r['ratio_bound']),('rate proved',q['explicit_divergent_rate_proved']),('one sided',q['rate_is_one_sided_variational']),('not sharp',not q['rate_is_sharp']),('lower fenced',not q['matching_ground_energy_lower_bound_proved']),('protected fenced',not q['protected_status_change'])]
 vals=[]
 for N in (10**3,10**6,10**12,10**24):
  d=math.log(N)/math.log(math.log(N));vals.append(math.sqrt(d)/N**1.5)
 checks += [('free/gain sample decreases',all(vals[i+1]<vals[i] for i in range(len(vals)-1))),('free/gain sample small',vals[-1]<1e-30)]
 rates=[math.sqrt(math.log(N)/math.log(math.log(N))) for N in (10**3,10**6,10**12,10**24)]
 checks += [('rate grows',all(rates[i+1]>rates[i] for i in range(len(rates)-1)))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
