#!/usr/bin/env python3
"""Certificate for K1609's shifted normal form and radius composition."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1609-primitive-radius-composition.json').read_text());q=d['primitive_composition'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1609'),('shift q','q_(sigma,k)=k-sigma e a_infinity' in q['shifted_normal_form']),('normal form','E_infinity=H_a' in q['shifted_normal_form']),('no adot','E_infinity\'=e tilde a' in q['shifted_normal_form']),('relative bound','2|e||tilde a|' in q['bare_energy']),('BG budgets','B_a=B_G0+B_G2' in q['bare_energy']),('adapted','B_A(t)<=|e||tilde a(t)|+R(t)' in q['adapted_radius']),('positive','<rho_0' in q['positive_budget']),('conditional','conditional on the atom-free' in q['scope_guard'])]
 # Scalar expansion check for one signed mode around a nonzero reference holonomy.
 k,e,ainf,at,mass,w=2.3,.7,.8,.25,1.2,1.4;q0=k-e*ainf
 H=.5*((q0-e*at)**2+mass**2)*w;E=.5*(q0*q0+mass**2)*w;D=q0*w;M=w
 c += [('shift expansion',abs(E-(H+e*at*D-.5*e*e*at*at*M))<1e-12)]
 BG0,BG2,BR,Cm,rho0=0.4,0.2,0.1,1.1,1.0;Ba=BG0+BG2;Ba2=BG0*Ba;expo=2*abs(e)*Ba+e*e/mass*Ba2;spend=Cm/4*(abs(e)*Ba+BR)
 c += [('energy finite',math.exp(expo)<5),('radius positive',rho0-spend>0),('normal form proved',z['shifted_normal_form_proved']),('static absorbed',z['static_asymptotic_holonomy_absorbed']),('energy conditional',z['bare_energy_uniform_bound_proved_conditionally']),('radius conditional',z['positive_limiting_radius_proved_conditionally']),('no E L1',not z['electric_l1_required']),('remainders open',not z['curvature_current_remainders_derived']),('flow open',not z['source_owned_global_flow_constructed']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
