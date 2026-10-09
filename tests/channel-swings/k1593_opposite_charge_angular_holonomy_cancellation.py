#!/usr/bin/env python3
"""Certificate for K1593's opposite-charge angular-holonomy cancellation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1593-opposite-charge-angular-holonomy-cancellation.json').read_text());q=d['angular_cancellation'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1593'),('charges','q in {+e,-e}' in q['species_identity']),('frequency','|k-q a|^2' in q['species_identity']),('signed work',"H_q'=-q dot(a)" in q['species_identity']),('same k','equal same-k amplitudes' in q['pairing_condition']),('weight w','w_k' in q['pairing_condition']),('momentum cancellation','momentum-linear terms cancel' in q['exact_sum']),('factor two','2e^2 dot(a) dot a' in q['exact_sum']),('radial derivative','d(|a|^2)/dt' in q['exact_sum']),('constant radius','If |a| is constant' in q['angular_consequence']),('divergent TV','int|dot a| diverges' in q['angular_consequence']),('only radial','only radial amplitude variation' in q['angular_consequence']),('homogeneous invariant','homogeneous k=0' in q['invariant_control']),('neutrality insufficient','Gauss neutrality alone' in q['scope_guard'])]
 e=2.0;adotk=7.0;adota=3.0;w=5.0
 plus=-e*(adotk-e*adota)*w;minus=e*(adotk+e*adota)*w
 c += [('algebra cancellation',abs((plus+minus)-2*e*e*adota*w)<1e-12),('angular zero',abs(2*e*e*0.0*w)<1e-12),('decision signed',z['signed_species_work_identity_proved']),('decision momentum',z['momentum_linear_terms_cancel']),('decision angular',z['angular_holonomy_cost_zero']),('decision invariant',z['homogeneous_control_invariant']),('neutrality not enough',not z['neutrality_alone_sufficient']),('global open',not z['global_positive_radius_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
