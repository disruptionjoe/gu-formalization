#!/usr/bin/env python3
"""Hostile mutations for K1494."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1494-uniform-jacobi-tower.json').read_text())
def valid(d):
 a,q=d['uniform_jacobi_tower'],d['decision']
 return all([d['claim_id']=='K1494','Jacobi recurrence' in a['orthonormal_basis'],'sqrt(h_(j+1,N)/h_(j,N))' in a['off_diagonal_identity'],'H_j^(-1/2)' in a['off_diagonal_bounds'],'3^(4j)' in a['diagonal_bounds'],'lambda_min(J_(d,N))<' in a['strict_interlacing'],'epsilon_d>0' in a['uniform_fixed_degree_gap'],q['jacobi_recurrence_constructed'],q['all_fixed_off_diagonal_couplings_uniformly_positive'],q['fixed_degree_diagonals_uniformly_bounded'],q['strict_interlacing_at_every_fixed_degree'],q['uniform_fixed_degree_gap_exists'],not q['gap_sequence_non_summability_proved'],not q['protected_status_change']])
mutations=[
 ('claim',lambda d:d.update(claim_id='K1493')),('recurrence',lambda d:d['uniform_jacobi_tower'].update(orthonormal_basis='none')),('b identity',lambda d:d['uniform_jacobi_tower'].update(off_diagonal_identity='unknown')),('b lower',lambda d:d['uniform_jacobi_tower'].update(off_diagonal_bounds='upper only')),('diagonal',lambda d:d['uniform_jacobi_tower'].update(diagonal_bounds='unknown')),('strict',lambda d:d['uniform_jacobi_tower'].update(strict_interlacing='weak')),('epsilon',lambda d:d['uniform_jacobi_tower'].update(uniform_fixed_degree_gap='zero')),('decision recurrence',lambda d:d['decision'].update(jacobi_recurrence_constructed=False)),('decision coupling',lambda d:d['decision'].update(all_fixed_off_diagonal_couplings_uniformly_positive=False)),('decision diagonal',lambda d:d['decision'].update(fixed_degree_diagonals_uniformly_bounded=False)),('decision strict',lambda d:d['decision'].update(strict_interlacing_at_every_fixed_degree=False)),('decision gap',lambda d:d['decision'].update(uniform_fixed_degree_gap_exists=False)),('claim nonsummable',lambda d:d['decision'].update(gap_sequence_non_summability_proved=True)),('move status',lambda d:d['decision'].update(protected_status_change=True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);assert not valid(x),label;print(f'PASS {i:02d}: rejected {label}')
print(f'RESULT: PASS {len(mutations)}/{len(mutations)}')
