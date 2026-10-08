#!/usr/bin/env python3
"""Controls for K1509's rare Gaussian bump transfer."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1509-rare-gaussian-bump-transfer.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 b,q=D['bump_trial'],D['decision']
 checks += [('claim',D['claim_id']=='K1509'),('compact profile','C_c^1' in b['profile'] and '[-1,0]' in b['profile']),('alpha range','alpha<3/2' in b['radius']),('radius','sqrt(2 alpha log N)' in b['radius']),('mass','N^(-alpha-o(1))' in b['gaussian_mass']),('margin','alpha-3/2' in b['transfer_margin']),('margin tends zero','tends to zero' in b['transfer_margin']),('norm transfer','p_N(1+o(1))' in b['cutoff_norm']),('bounded numerator','O(R_N epsilon_N)' in b['cutoff_numerator']),('quotient','sqrt(2 alpha log N)' in b['quotient']),('mass transferred',q['rare_bump_mass_transferred']),('quotient proved',q['negative_sqrt_log_multiplication_quotient_proved']),('endpoint fenced',not q['endpoint_alpha_three_halves_transferred']),('moderate deviations fenced',not q['tail_or_moderate_deviation_asymptotic_proved']),('protected fenced',not q['protected_status_change'])]
 for alpha in (0.25,0.75,1.25,1.49):
  ratios=[]
  for t in (10_000,100_000,1_000_000):
   R=math.sqrt(2*alpha*t);log_eps=-1.5*t+4*math.log1p(t);log_p=-alpha*t-R-1
   ratios.append(log_eps-log_p)
  checks.append((f'alpha {alpha} transfer improves',ratios[-1]<ratios[0] and ratios[-1]<-1))
 checks.append(('endpoint not decaying',(-1.5*1600+4*math.log1p(1600))-(-1.5*1600-math.sqrt(3*1600)-1)>0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
