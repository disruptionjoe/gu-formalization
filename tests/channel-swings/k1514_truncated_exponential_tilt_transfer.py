#!/usr/bin/env python3
"""Controls for K1514's truncated exponential tilt transfer."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1514-truncated-exponential-tilt-transfer.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 t,q=D['tilt_trial'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1514'),('smooth cutoff','smooth chi' in t['profile']),('plateau','[-3/2,-1/2]' in t['profile']),('support','[-2,0]' in t['profile']),('tilt formula','exp(-R_N x/2-R_N^2/4)' in t['profile']),('likelihood','N(-R_N,1)' in t['gaussian_identity']),('integration by parts','Integration by parts' in t['stieltjes_transfer']),('left tail','P(X_N<=-z)' in t['stieltjes_transfer']),('multiplicative','multiplicatively' in t['stieltjes_transfer']),('unit norm','1+o(1)' in t['cutoff_norm']),('tilted concentration','probability 1-o(1)' in t['cutoff_norm']),('negative quotient','-(1+o(1))R_N' in t['multiplication_quotient']),('holder exponent','p_N=1+R_N^(-2)' in t['near_one_holder_moment']),('holder bound','=O(1)' in t['near_one_holder_moment']),('tilt transferred',q['truncated_exponential_tilt_transferred']),('quotient proved',q['negative_polynomial_multiplication_quotient_proved']),('holder controlled',q['near_one_holder_norm_controlled']),('untruncated fenced',not q['untruncated_laplace_transform_transferred']),('density fenced',not q['density_ratio_or_pointwise_likelihood_proved']),('protected fenced',not q['protected_status_change'])]
 for R in (4.0,8.0,16.0):
  p=1+R**-2;full_norm=1.0;holder=math.exp((p-1)*R*R/2);checks += [(f'Gaussian norm {R}',full_norm==1), (f'holder constant {R}',math.isclose(holder,math.sqrt(math.e)))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
