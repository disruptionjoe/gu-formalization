#!/usr/bin/env python3
"""Controls for K1523's coherent-state Wick-square boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1523-coherent-wick-square-boundary.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['coherent_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1523'),('real coordinates','real standard Gaussian coordinates' in q['q_space_trial']),('normalized density','N(alpha,I)' in q['q_space_trial']),('free quarter','(1/4)sum_j omega_j alpha_j^2' in q['free_cost']),('free positive','>=0' in q['free_cost']),('mean formula','sqrt(lambda_j) alpha_j' in q['field_mean']),('variance unchanged','unchanged point variance C_N' in q['field_mean']),('W formula','6C_N^2+int h(x)^4' in q['wick_expectation']),('coherent bottom','at least 6gC_N^2' in q['coherent_infimum']),('vacuum equality','vacuum alpha=0 attains exactly 6gC_N^2' in q['coherent_infimum']),('N4 scale','Theta(N^4)' in q['scale']),('scope coherent','covariance-preserving coherent shifts only' in q['scope_guard']),('decision bottom',d['coherent_sector_exact_bottom']=='6gC_N^2'),('no N2',not d['coherent_order_N2_trial_exists']),('Gaussian fenced',not d['arbitrary_gaussian_classified']),('asymptotic fenced',not d['full_ground_energy_asymptotic_proved']),('protected',not d['protected_status_change'])]
 for C,h in ((2.0,0.0),(3.0,1.5),(7.0,-2.0)):
  raw=h**4+6*h*h*C+3*C*C-6*C*(h*h+C)+9*C*C
  checks.append((f'fourth moment C={C} h={h}',math.isclose(raw,6*C*C+h**4)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
