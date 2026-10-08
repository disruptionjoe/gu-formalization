#!/usr/bin/env python3
"""Hostile mutations for K1503."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1503-growing-moment-window.json').read_text())
def valid(d):
 a,b,w,q=d['contraction_defect'],d['diagram_bound'],d['window'],d['decision'];return all([d['claim_id']=='K1503','E X_N^2=1' in a['definition'],'N^(-3/2)' in a['bound'],'whole quartic vertices' in b['gaussian_subfamily'],'r=1,2,3' in b['residual_cut'],'(4m-1)!!' in b['pairing_count'],'exp(C m log(m+1))' in b['moment_error'],'log N/log log N' in w['definition'],'C eta<3/2' in w['eta_condition'],'max_(0<=m<=M_N)' in w['conclusion'],q['growing_moment_window_proved'],not q['window_constant_optimized'],not q['total_variation_rate_proved'],not q['protected_status_change']])
mut=[('claim',lambda d:d.update(claim_id='bad')),('normalization',lambda d:d['contraction_defect'].update(definition='unknown')),('rate',lambda d:d['contraction_defect'].update(bound='unknown')),('Gaussian family',lambda d:d['diagram_bound'].update(gaussian_subfamily='all')),('cut',lambda d:d['diagram_bound'].update(residual_cut='r=4')),('count',lambda d:d['diagram_bound'].update(pairing_count='unknown')),('envelope',lambda d:d['diagram_bound'].update(moment_error='unknown')),('window',lambda d:d['window'].update(definition='M_N=N')),('margin',lambda d:d['window'].update(eta_condition='none')),('conclusion',lambda d:d['window'].update(conclusion='fixed m')),('deny',lambda d:d['decision'].update(growing_moment_window_proved=False)),('claim optimal',lambda d:d['decision'].update(window_constant_optimized=True)),('claim TV',lambda d:d['decision'].update(total_variation_rate_proved=True)),('move status',lambda d:d['decision'].update(protected_status_change=True))]
for i,(label,f) in enumerate(mut,1):x=copy.deepcopy(D);f(x);assert not valid(x),label;print(f'PASS {i:02d}: rejected {label}')
print(f'RESULT: PASS {len(mut)}/{len(mut)}')
