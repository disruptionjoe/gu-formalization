#!/usr/bin/env python3
"""Hostile mutations for K1505."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1505-quantitative-variational-rate.json').read_text())
def valid(d):
 s,r,q=d['scale_comparison'],d['variational_rate'],d['decision'];return all([d['claim_id']=='K1505','log N/log log N' in s['degree'],'4d_N' in s['chaos_ceiling'],'O(N d_N)' in s['free_cost'],'sigma_N/2' in s['interaction_gain'],'sqrt(d_N)' in s['interaction_gain'],'N^(3/2)' in s['dominance'],'N^(5/2)' in s['dominance'],'sqrt(log N/log log N)' in r['energy_bound'],'sqrt(log N/log log N)' in r['ratio_bound'],q['explicit_divergent_rate_proved'],q['rate_is_one_sided_variational'],not q['rate_is_sharp'],not q['matching_ground_energy_lower_bound_proved'],not q['protected_status_change']])
mut=[('claim',lambda d:d.update(claim_id='bad')),('degree',lambda d:d['scale_comparison'].update(degree='d_N=N')),('chaos',lambda d:d['scale_comparison'].update(chaos_ceiling='unknown')),('free',lambda d:d['scale_comparison'].update(free_cost='unknown')),('gain',lambda d:d['scale_comparison'].update(interaction_gain='zero')),('dominance',lambda d:d['scale_comparison'].update(dominance='unknown')),('energy',lambda d:d['variational_rate'].update(energy_bound='qualitative')),('ratio',lambda d:d['variational_rate'].update(ratio_bound='qualitative')),('deny',lambda d:d['decision'].update(explicit_divergent_rate_proved=False)),('deny one-sided',lambda d:d['decision'].update(rate_is_one_sided_variational=False)),('claim sharp',lambda d:d['decision'].update(rate_is_sharp=True)),('claim lower',lambda d:d['decision'].update(matching_ground_energy_lower_bound_proved=True)),('move status',lambda d:d['decision'].update(protected_status_change=True))]
for i,(label,f) in enumerate(mut,1):x=copy.deepcopy(D);f(x);assert not valid(x),label;print(f'PASS {i:02d}: rejected {label}')
print(f'RESULT: PASS {len(mut)}/{len(mut)}')
