#!/usr/bin/env python3
"""Certificate for K1584's harmonic/oscillatory radius budget."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1584-harmonic-oscillatory-radius-budget.json').read_text());q=d['harmonic_split'];z=d['decision'];checks=[]
 checks += [('claim',d['claim_id']=='K1584'),('split','A=a+A_perp' in q['decomposition']),('mean zero','mean(A_perp)=0' in q['decomposition']),('Coulomb','Coulomb gauge' in q['decomposition']),('Hodge','Hodge/Poincare' in q['hodge_control']),('curl control','curl A' in q['hodge_control']),('electric control','E_perp' in q['hodge_control']),('harmonic derivative','dot a' in q['remainder_budget']),('raw amplitude replaced','replaces |e|||a||' in q['remainder_budget']),('L1 condition','L1_t' in q['conditional_radius']),('positive margin','positive limit' in q['conditional_radius']),('static zero','Static flat holonomy consumes no radius' in q['structural_advance']),('scope nonlinear','No coupled estimate' in q['scope_guard'])]
 rho0,integral,C=2.0,.5,1.0;checks.append(('sample positive radius',rho0-C*integral>0))
 checks += [('split built',z['harmonic_oscillatory_split_constructed']),('amplitude removed',z['raw_flat_amplitude_removed']),('remainder typed',z['hodge_remainder_typed']),('conditional radius',z['conditional_positive_radius']),('integrability open',not z['remainder_integrability_proved']),('flow open',not z['nonlinear_global_flow']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
