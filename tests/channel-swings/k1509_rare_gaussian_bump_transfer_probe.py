#!/usr/bin/env python3
"""Hostile mutations for K1509."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1509-rare-gaussian-bump-transfer.json').read_text())
def valid(d):
 b,q=d['bump_trial'],d['decision'];return all([d['claim_id']=='K1509','C_c^1' in b['profile'],'[-1,0]' in b['profile'],'alpha<3/2' in b['radius'],'sqrt(2 alpha log N)' in b['radius'],'N^(-alpha-o(1))' in b['gaussian_mass'],'alpha-3/2' in b['transfer_margin'],'p_N(1+o(1))' in b['cutoff_norm'],'O(R_N epsilon_N)' in b['cutoff_numerator'],'sqrt(2 alpha log N)' in b['quotient'],q['rare_bump_mass_transferred'],q['negative_sqrt_log_multiplication_quotient_proved'],not q['endpoint_alpha_three_halves_transferred'],not q['tail_or_moderate_deviation_asymptotic_proved'],not q['protected_status_change']])
mut=[('claim',lambda d:d.update(claim_id='bad')),('profile',lambda d:d['bump_trial'].update(profile='unbounded')),('support',lambda d:d['bump_trial'].update(profile='C_c^1')),('alpha',lambda d:d['bump_trial'].update(radius='alpha=2')),('radius',lambda d:d['bump_trial'].update(radius='R=N')),('mass',lambda d:d['bump_trial'].update(gaussian_mass='unknown')),('margin',lambda d:d['bump_trial'].update(transfer_margin='unknown')),('norm',lambda d:d['bump_trial'].update(cutoff_norm='unknown')),('numerator',lambda d:d['bump_trial'].update(cutoff_numerator='unbounded')),('quotient',lambda d:d['bump_trial'].update(quotient='fixed')),('deny',lambda d:d['decision'].update(rare_bump_mass_transferred=False)),('endpoint',lambda d:d['decision'].update(endpoint_alpha_three_halves_transferred=True)),('tail',lambda d:d['decision'].update(tail_or_moderate_deviation_asymptotic_proved=True)),('status',lambda d:d['decision'].update(protected_status_change=True))]
for i,(label,f) in enumerate(mut,1):x=copy.deepcopy(D);f(x);assert not valid(x),label;print(f'PASS {i:02d}: rejected {label}')
print(f'RESULT: PASS {len(mut)}/{len(mut)}')
