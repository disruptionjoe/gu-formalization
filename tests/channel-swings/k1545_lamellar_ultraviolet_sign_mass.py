#!/usr/bin/env python3
"""Controls for K1545's ultraviolet sign-mass tradeoff."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1545-lamellar-ultraviolet-sign-mass.json').read_text())
def shell(R,alpha):return 8/math.pi**2*sum(1/(2*r+1)**2 for r in range(R+1) if alpha*(2*R+1)<=2*r+1<=2*R+1)
def main():
 q,d=D['shell_tradeoff'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1545'),('actual sign','sgn(sin(Mx_1))' in q['actual_sign']),('shell coefficient','8/pi^2' in q['exact_shell_mass']),('shell window','alpha(2R+1)' in q['exact_shell_mass']),('R scale','Theta_alpha(1/(R+1))' in q['shell_scale']),('M scale','Theta_alpha(M/N)' in q['shell_scale']),('coupling','c_alpha H_' in q['coupled_tradeoff']),('all exact signs','every degree-N' in q['coupled_tradeoff']),('quartic consequence','Omega(N^4)' in q['fixed_shell_consequence']),('scope exact class','exact one-coordinate lamellar' in q['scope_guard']),('outer decision',d['outer_shell_mass_computed']),('tradeoff decision',d['interaction_shell_tradeoff_proved']),('quartic decision',d['fixed_shell_mass_forces_quartic_interaction']),('inverse fenced',not d['universal_inverse_theorem_proved']),('protected',not d['protected_status_change'])]
 for R in (8,32,128):checks.append((f'shell positive R{R}',shell(R,.5)>0))
 checks.append(('shell inverse-R sample',shell(128,.5)<shell(32,.5)<shell(8,.5)))
 ratios=[]
 for R in range(1,513):
  tail=1-8/math.pi**2*sum(1/(2*r+1)**2 for r in range(R+1)); ratios.append(tail/shell(R,.5))
 checks.append(('uniform tail/shell stress',min(ratios)>.1))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
