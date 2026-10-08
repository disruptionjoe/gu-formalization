#!/usr/bin/env python3
"""Controls for K1508's quantitative fourth-chaos total-variation rate."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1508-fourth-chaos-total-variation-rate.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 m,q=D['malliavin_stein'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1508'),('normalization','E(X_N^2)=1' in m['normalized_variable']),('three contractions','r=1,2,3' in m['fourth_cumulant']),('positive combination','positive universal' in m['fourth_cumulant']),('TV theorem','d_TV(X_N,Z)' in m['fixed_chaos_bound']),('cumulant root','sqrt(E(X_N^4)-3)' in m['fixed_chaos_bound']),('input square rate','N^(-3)' in m['input_rate']),('input logs','log N)^8' in m['input_rate']),('TV rate','N^(-3/2)' in m['conclusion']),('TV logs','log N)^4' in m['conclusion']),('rate proved',q['quantitative_total_variation_rate_proved']),('bounded tests',q['bounded_measurable_tests_transfer']),('unbounded fenced',not q['unbounded_tests_transfer_without_truncation']),('constant fenced',not q['rate_constant_optimized']),('protected fenced',not q['protected_status_change'])]
 vals=[]
 for t in (20,40,80,160): vals.append(math.exp(-1.5*t)*(1+t)**4)
 checks += [('sample rate decreases',all(vals[i+1]<vals[i] for i in range(len(vals)-1))),('sample rate vanishes',vals[-1]<1e-90)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
