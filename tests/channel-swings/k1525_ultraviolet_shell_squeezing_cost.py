#!/usr/bin/env python3
"""Controls for K1525's ultraviolet-shell squeezing cost."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1525-ultraviolet-shell-squeezing-cost.json').read_text())
def shell_sums(N,mass=1.0):
 total=shell=0.0
 for x in range(-N,N+1):
  for y in range(-N,N+1):
   for z in range(-N,N+1):
    w=math.sqrt(mass*mass+x*x+y*y+z*z);lam=1/(2*w);total+=lam
    if max(abs(x),abs(y),abs(z))*2>=N:shell+=lam
 return total,shell
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['shell_cost'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1525'),('shell ratio','N/2<=|k_j|_infinity<=N' in q['shell']),('mode count','Theta(N^3)' in q['shell']),('frequency','omega_j=Theta(N)' in q['shell']),('covariance','lambda_j=(2omega_j)^(-1)=Theta(N^-1)' in q['shell']),('positive fraction','C_(S,N)=sum_(S_N)lambda_j>=kappa C_N' in q['shell']),('low threshold','(kappa/2)C_N' in q['low_variance_deficit']),('deficit N2','=Theta(N^2)' in q['low_variance_deficit']),('Cauchy','Cauchy gives' in q['weighted_cauchy']),('dual O1','=O(1)' in q['dual_shell_bound']),('free N4','>=cN^4' in q['free_cost_consequence']),('high N4','c C_N^2=cN^4' in q['high_variance_consequence']),('scope stationary','stationary translation-invariant diagonal covariance' in q['scope_guard']),('decision N4',d['order_one_variance_suppression_cost']=='N^4'),('shell required',d['ultraviolet_shell_required']),('log loss avoided',d['logarithmic_global_cauchy_loss_avoided']),('full fenced',not d['arbitrary_trial_lower_bound_proved']),('protected',not d['protected_status_change'])]
 for N in (4,6,8):
  total,shell=shell_sums(N);checks.append((f'positive shell fraction N={N}',shell/total>0.5))
 # finite weighted-Cauchy controls with signed deficits and nonuniform squeezes
 for ss in ((0.5,0.75,0.9),(0.2,1.1,0.6),(0.8,0.4,1.2)):
  ws=(8.0,9.0,10.0);ls=tuple(1/(2*w) for w in ws)
  delta=sum(l*(1-s) for l,s in zip(ls,ss));a=sum(w*(1-s)**2/s for w,s in zip(ws,ss));b=sum(l*l*s/w for l,s,w in zip(ls,ss,ws))
  checks.append((f'weighted Cauchy {ss}',delta*delta<=a*b+1e-15))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
