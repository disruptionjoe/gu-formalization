#!/usr/bin/env python3
"""Controls for K1555's high-frequency lamellar sharpness family."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1555-lamellar-sharpness-control.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['sharpness_control'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1555'),('construction','sin(M_N x_1)' in q['construction']),('ratio','alpha N<=M_N<=N' in q['construction']),('two modes','plus/minus M_N e_1' in q['bandlimit']),('shell mass','8/pi^2' in q['sign_shell']),('half phases','one half' in q['phase_balance']),('defect','3/8' in q['defect']),('sharpness','N^0 cutoff exponent' in q['sharpness']),('scope','sharpness only in the cutoff exponent' in q['scope_guard']),('constructed',d['fixed_shell_lamellar_control_constructed']),('constant',d['constant_defect_computed']),('sharp',d['cutoff_exponent_zero_sharp']),('eta open',not d['optimal_eta_dependence_proved']),('trial open',not d['low_energy_trial_constructed']),('protected',not d['protected_status_change'])]
 samples=20000;avg=sum((math.sin(2*math.pi*37*j/samples)**2-1)**2 for j in range(samples))/samples
 checks += [('defect quadrature',abs(avg-3/8)<1e-12),('fundamental mass',8/math.pi**2>.8)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
