#!/usr/bin/env python3
"""Hostile mutations for K1508."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1508-fourth-chaos-total-variation-rate.json').read_text())
def valid(d):
 m,q=d['malliavin_stein'],d['decision'];return all([d['claim_id']=='K1508','E(X_N^2)=1' in m['normalized_variable'],'r=1,2,3' in m['fourth_cumulant'],'positive universal' in m['fourth_cumulant'],'sqrt(E(X_N^4)-3)' in m['fixed_chaos_bound'],'N^(-3)' in m['input_rate'],'N^(-3/2)' in m['conclusion'],q['quantitative_total_variation_rate_proved'],q['bounded_measurable_tests_transfer'],not q['unbounded_tests_transfer_without_truncation'],not q['rate_constant_optimized'],not q['protected_status_change']])
mut=[('claim',lambda d:d.update(claim_id='bad')),('norm',lambda d:d['malliavin_stein'].update(normalized_variable='raw')),('orders',lambda d:d['malliavin_stein'].update(fourth_cumulant='r=4')),('sign',lambda d:d['malliavin_stein'].update(fourth_cumulant='unknown')),('theorem',lambda d:d['malliavin_stein'].update(fixed_chaos_bound='none')),('input',lambda d:d['malliavin_stein'].update(input_rate='none')),('rate',lambda d:d['malliavin_stein'].update(conclusion='qualitative')),('deny',lambda d:d['decision'].update(quantitative_total_variation_rate_proved=False)),('bounded deny',lambda d:d['decision'].update(bounded_measurable_tests_transfer=False)),('unbounded claim',lambda d:d['decision'].update(unbounded_tests_transfer_without_truncation=True)),('optimal claim',lambda d:d['decision'].update(rate_constant_optimized=True)),('status',lambda d:d['decision'].update(protected_status_change=True))]
for i,(label,f) in enumerate(mut,1):x=copy.deepcopy(D);f(x);assert not valid(x),label;print(f'PASS {i:02d}: rejected {label}')
print(f'RESULT: PASS {len(mut)}/{len(mut)}')
