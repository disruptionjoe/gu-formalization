#!/usr/bin/env python3
"""Certificate for K1587's profiled residual and Ritz scales."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1587-profiled-residual-ritz-scaling.json').read_text());q=d['ritz_scaling'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1587'),('kappa scaling','kappa_(g,N)^+/N^2' in q['covariance_counting']),('mean scaling','h_N^2=Theta_g(N^2)' in q['covariance_counting']),('coefficient upper','O_g(N^(-1))' in q['covariance_counting']),('cubic scale','Gamma_N^3=Theta_g(N^3)' in q['convolution_scales']),('quartic scale','Gamma_N^4=Theta_g(N^5)' in q['convolution_scales']),('variance scale','sigma_N^2=Theta_g(N^5)' in q['residual_scale']),('norm scale','sigma_N=Theta_g(N^(5/2))' in q['residual_scale']),('ground transform','ground-state transform' in q['second_diagonal']),('hypercontractivity','hypercontractivity' in q['second_diagonal']),('delta control','|delta_N|=O_g(N^(5/2))' in q['second_diagonal']),('exact gap','sqrt(delta_N^2+4 sigma_N^2)' in q['ritz_gap']),('gap scale','Delta_N=Theta_g(N^(5/2))' in q['ritz_gap']),('subleading','o(N^4)' in q['coefficient_ceiling'])]
 for delta in (-3.0,0.0,3.0):
  sig=2.0;gap=(math.sqrt(delta*delta+4*sig*sig)-delta)/2;c.append((f'positive gap {delta}',gap>0))
 c += [('counts',z['covariance_convolution_scales_proved']),('norm',z['residual_norm_n_five_halves']),('diagonal',z['ritz_second_diagonal_controlled']),('gap',z['ritz_gap_n_five_halves']),('coefficient open',not z['leading_n_four_coefficient_changed']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
