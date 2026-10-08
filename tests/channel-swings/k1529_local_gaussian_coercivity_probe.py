#!/usr/bin/env python3
"""Hostile mutations for K1529."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1529-local-gaussian-coercivity.json').read_text())
def valid(x):
 q,d=x['local_coercivity'],x['decision']
 return all([x['claim_id']=='K1529','b_N(x)^T S b_N(x)>=0' in q['field_data'],'6v(2C-v)' in q['mean_optimization'],'3(v-C)^2+6C^2' in q['mean_optimization'],'6(sqrt(3)-1)' in q['uniform_coercivity'],'local-variance spikes cannot evade' in q['spike_guard'],'Tr(Lambda S)' in q['integrated_consequence'],'does not impose stationarity or diagonal covariance' in q['scope_guard'],d['arbitrary_mean_included'],d['spatially_varying_variance_included'],not d['variance_spike_escape_exists'],not d['nongaussian_moment_bound_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1528'),(('local_coercivity','field_data'),'constant variance'),(('local_coercivity','mean_optimization'),'one branch'),(('local_coercivity','uniform_coercivity'),'zero constant'),(('local_coercivity','spike_guard'),'spikes escape'),(('local_coercivity','integrated_consequence'),'no trace'),(('local_coercivity','scope_guard'),'stationary only'),(('decision','arbitrary_mean_included'),False),(('decision','spatially_varying_variance_included'),False),(('decision','variance_spike_escape_exists'),True),(('decision','nongaussian_moment_bound_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
