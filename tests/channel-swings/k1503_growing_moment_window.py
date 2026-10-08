#!/usr/bin/env python3
"""Controls for K1503's growing Gaussian moment window."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1503-growing-moment-window.json').read_text())
def odd_double_factorial(n):
 out=1
 for k in range(1,n+1,2):out*=k
 return out
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,b,w,q=D['contraction_defect'],D['diagram_bound'],D['window'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1503'),('normalized', 'E X_N^2=1' in a['definition']),('defect rate','N^(-3/2)' in a['bound']),('Gaussian family','whole quartic vertices' in b['gaussian_subfamily']),('nontrivial cut','r=1,2,3' in b['residual_cut']),('pairing formula','(4m-1)!!' in b['pairing_count']),('moment envelope','exp(C m log(m+1))' in b['moment_error']),('window','log N/log log N' in w['definition']),('eta margin','C eta<3/2' in w['eta_condition']),('uniform conclusion','max_(0<=m<=M_N)' in w['conclusion']),('window proved',q['growing_moment_window_proved']),('not optimized',not q['window_constant_optimized']),('TV fenced',not q['total_variation_rate_proved']),('protected fenced',not q['protected_status_change'])]
 for m in range(1,11):checks.append((f'pairing count m={m}',odd_double_factorial(4*m-1)<=(4*m)**(2*m)))
 C,eta=8.0,0.1
 checks += [('sample eta admissible',C*eta<1.5)]
 for t in (1e3,1e4,1e5):
  M=eta*t/math.log(t); exponent=(-1.5*t+4*math.log(t)+C*M*math.log(M+1))/t
  checks.append((f'negative exponent logN={int(t)}',exponent<0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
