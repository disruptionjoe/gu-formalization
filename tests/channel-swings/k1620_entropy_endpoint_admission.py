#!/usr/bin/env python3
"""Certificate for K1620 protected admission and pinned dependencies."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
 d=json.loads((ROOT/'lab/process/k1620-entropy-endpoint-admission.json').read_text());c=[('claim',d['claim_id']=='K1620')]
 for key,rec in d['pinned_inputs'].items():c.append((f'pin {key}',sha(rec['path'])==rec['sha256']))
 x=d['census'];c += [('rows',x['rows']==335),('sum',x['satisfied']+x['conditional']+x['excluded']+x['missing']==x['rows']),
   ('ledger',x['physics_ledger']=={'SAME':33,'DIFFERS':22,'NEEDS':31,'OVER_DETERMINED':2}),('scorable',x['k1145_k1150_scorable_rows']=='0/7')]
 for key,val in d['protected_boundaries'].items():c.append((f'protected {key}',val is False))
 c += [('wakes',len(d['next_wakes'])==3),('information','label-dependent covariances' in d['next_wakes'][0]),('source action','source-owned action' in d['next_wakes'][2])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
