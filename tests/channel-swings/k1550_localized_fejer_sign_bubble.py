#!/usr/bin/env python3
"""Controls for K1550's localized Fejer sign bubble."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1550-localized-fejer-sign-bubble.json').read_text())
def moment(m,p):
 L=8*m+1;total=0.0
 for j in range(L):
  t=2*math.pi*(j+.5)/L;den=m*math.sin(t/2);q=(math.sin(m*t/2)/den)**2;total+=q**p
 return total/L
def defect(m):
 a2,a3,a4=(moment(m,p) for p in (2,3,4));return 16*(a2**3-2*a3**3+a4**3)
def main():
 q,d=D['fejer_bubble'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1550'),('Fejer','normalized Fejer' in q['definition']),('degree','sqrt(3)(m-1)<=N' in q['bandlimit']),('bubble','Theta(m^(-3))' in q['sign_geometry']),('defect identity','16int Q_m^2(1-Q_m)^2' in q['defect_identity']),('q2 exact','(m-1)(2m-1)/(3m^3)' in q['upper_scale']),('upper','O(m^(-3))' in q['upper_scale']),('lower','Omega(m^(-3))' in q['lower_scale']),('shell vanishes','O(N^(-3))' in q['shell_consequence']),('scope shell','vanishing, not nonvanishing' in q['scope_guard']),('constructed',d['nonlamellar_bandlimited_example_constructed']),('N-3',d['sign_change_defect_scale_Nminus3_proved']),('shell false',not d['shell_mass_nonvanishing']),('essential',d['phase_balance_hypothesis_essential']),('sharpness open',not d['k1549_exponent_sharpness_proved']),('protected',not d['protected_status_change'])]
 vals=[defect(m)*m**3 for m in (8,16,32,64)]
 checks += [('defects positive',min(vals)>0),('scaled defect stable',max(vals)/min(vals)<2),('nonzero limit scale',vals[-1]>.01)]
 for m in (3,8,21):
  exact=m**-2+(m-1)*(2*m-1)/(3*m**3);checks.append((f'q2 quadrature m={m}',abs(moment(m,2)-exact)<1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
