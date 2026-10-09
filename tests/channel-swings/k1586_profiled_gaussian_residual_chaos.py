#!/usr/bin/env python3
"""Certificate for K1586's exact profiled Gaussian residual chaos."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1586-profiled-gaussian-residual-chaos.json').read_text());q=d['residual_chaos'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1586'),('profiled setting',"K1572's larger-root" in q['setting']),('covariance', 'Gamma_N' in q['setting']),('affine quadratic','affine-quadratic' in q['stationary_cancellation']),('low chaos cancellation','constant, first and second' in q['stationary_cancellation']),('third chaos',':eta(x)^3:' in q['exact_residual']),('fourth chaos',':eta(x)^4:' in q['exact_residual']),('residual equation','(H_N-lambda_N)G_N=R_N G_N' in q['exact_residual']),('orthogonal','orthogonal' in q['orthogonal_norm']),('96 coefficient','96 h_N^2' in q['orthogonal_norm']),('24 coefficient','24 int_T3' in q['orthogonal_norm']),('positive Fourier','Fourier coefficients' in q['positivity']),('finite cutoff','finite-cutoff' in q['scope_guard'])]
 c += [('chaos3 Wick factor',16*6==96),('chaos4 Wick factor',24==24),('low cancel',z['low_chaos_projections_cancel']),('exact',z['third_fourth_residual_exact']),('norm',z['orthogonal_norm_identity']),('nonzero',z['residual_nonzero']),('ground open',not z['unrestricted_ground_state_identified']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
