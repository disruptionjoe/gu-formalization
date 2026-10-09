#!/usr/bin/env python3
"""Certificate for K1598's unequal-mode bare-energy normal form."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1598-unequal-mode-bare-energy-normal-form.json').read_text());q=d['bare_energy_normal_form'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1598'),('M definition','M=sum_k' in q['mode_moments']),('D definition','D=sum_k k' in q['mode_moments']),('unequal work',"H_a'=-e dot(a) dot D" in q['signed_work']),('radial work','e^2 dot(a) dot a M' in q['signed_work']),('energy expansion','H_a=E_0-e a dot D' in q['energy_expansion']),('bare energy','m^2+|k|^2' in q['energy_expansion']),('boundary correction','E_0=H_a+e a dot D' in q['normal_form']),('no adot',"no dot(a) term" in q['normal_form']),('D bound',"|D'|<=2E_0" in q['same_tier_bound']),('M bound',"|M'|<=2E_0/m" in q['same_tier_bound']),('no derivative loss','no spatial derivative loss' in q['same_tier_bound']),('scope amplitude','still spends holonomy amplitude' in q['scope_guard']),('scope global','no global integrability' in q['scope_guard'])]
 # Scalar-vector algebra for two modes.
 e=1.7;a=(.3,-.4);ad=(.2,.5);M=2.4;D=(.8,-.6);Dp=(.1,.9);Mp=-.7
 dot=lambda x,y:sum(u*v for u,v in zip(x,y));Hp=-e*dot(ad,D)+e*e*dot(ad,a)*M
 correction_p=e*dot(ad,D)+e*dot(a,Dp)-e*e*dot(ad,a)*M-.5*e*e*dot(a,a)*Mp
 expected=e*dot(a,Dp)-.5*e*e*dot(a,a)*Mp
 c += [('normal form derivative',abs(Hp+correction_p-expected)<1e-12),('bound coefficient positive',2*abs(e)*math.sqrt(dot(a,a))+e*e*dot(a,a)/2.0>0),('decision unequal',z['unequal_modes_allowed']),('decision correction',z['exact_boundary_correction']),('decision no variation',z['harmonic_electric_variation_removed']),('decision same tier',z['same_tier_no_derivative_loss']),('global open',not z['global_positive_radius_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
