#!/usr/bin/env python3
"""Controls for K1455's factorial-Gevrey phase boundary."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1455-factorial-gevrey-hierarchy-phase-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
R0=.7
for p in (.25,.5,1,1.5,2):
 a=lambda j:R0**j/math.factorial(j)**p
 for j in (1,3,8): c(f'ratio p={p} n={j}',abs(a(j-1)/a(j)-j**p/R0)<1e-10)
c('sublinear moments',all(j**.5<=j for j in range(1,30))); c('superlinear obstruction',max(j**2/j for j in range(1,30))==29)
Q=D['decision']; c('entire',Q['entire_weight_for_every_positive_p']); c('p<=1',Q['one_radius_absorbs_for_p_at_most_one'])
c('p>1 fenced',not Q['one_radius_absorbs_for_p_greater_than_one']); c('global fenced',not Q['global_positive_radius_from_this_family']); c('other methods open',not Q['all_hierarchy_methods_excluded']); c('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
