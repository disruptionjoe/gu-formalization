#!/usr/bin/env python3
"""Certificate for K1594's constant-radius charge-analytic hierarchy."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1594-constant-radius-charge-analytic-hierarchy.json').read_text());q=d['charge_hierarchy'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1594'),('k zero','only k=0 modes' in q['orbit_data']),('equal amplitudes','equal species amplitudes' in q['orbit_data']),('constant radius','constant |a|=A' in q['orbit_data']),('electric nonzero','|dot a|=A Omega>0' in q['orbit_data']),('base constant','H_+(t)+H_-(t)=constant' in q['base_conservation']),('TV divergent','diverges linearly' in q['base_conservation']),('equal absolute charges','equal absolute value' in q['tier_lift']),('Q powers','Q^n' in q['tier_lift']),('every tier','every charge tier' in q['tier_lift']),('analytic positive','convergent positive charge-analytic sum' in q['analytic_sum']),('not universal no go','does not obstruct every cancellation-based' in q['interpretation']),('zero signed cost','zero signed hierarchy cost' in q['interpretation']),('scope no decay','supplies no decay' in q['scope_guard'])]
 c += [('decision base',z['base_paired_energy_conserved']),('decision tiers',z['every_charge_tier_conserved']),('decision sum',z['positive_analytic_sum_conserved']),('universal no go false',not z['k1589_universal_cancellation_no_go']),('global open',not z['global_nonlinear_flow_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
