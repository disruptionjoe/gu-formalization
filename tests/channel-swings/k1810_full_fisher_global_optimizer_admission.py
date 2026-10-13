#!/usr/bin/env python3
"""K1810 protected global optimizer admission after slab-two closure."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; ARTIFACT=ROOT/'lab/process/k1810-full-fisher-global-optimizer-admission.json'
def load(n):return json.loads((ROOT/f'lab/process/{n}.json').read_text())
def compute():
 k1794=load('k1794-full-fisher-slab-three-global-stationarity');k1804=load('k1804-full-fisher-deduplicated-boundary-atlas');k1809=load('k1809-full-fisher-slab-two-global-exclusion')
 return {'slab_one_excluded':k1809['decision']['slab_one_complete_sublevel_excluded'],'slab_two_excluded':k1809['decision']['slab_two_complete_sublevel_excluded'],'slab_three_retained_boxes':k1804['certificate']['by_slab']['3'],'slab_three_local_stationary_point_isolated':k1794['decision']['local_interior_stationary_point_isolated'],'slab_three_complete_uniqueness':k1794['decision']['unique_stationary_point_on_complete_slab_three'],'deduplicated_exposed_atomic_faces_total':k1804['certificate']['exposed_atomic_faces'],'deduplicated_exposed_boundary_vertices_total':k1804['certificate']['exposed_boundary_vertices'],'transfer_method':'anchor at the K1787 slab-three stationary score; certify A^2-TB on each of the 78 exact leaves with the K1807 centered jet and K1808 tails; use the uniform closed-box value bounds to discharge each leaf face and vertex'}
def validate(data,got=None):
 got=compute() if got is None else got;c=data['certificate'];return [('schema',data['schema_version']=='1.0'),('claim',data['claim_id']=='K1810'),('inputs',data['inputs']==['K1794','K1804','K1809']),('replay',c==got),('two slabs closed',c['slab_one_excluded'] and c['slab_two_excluded']),('78 remain',c['slab_three_retained_boxes']==78),('slab three withheld',not c['slab_three_complete_uniqueness']),('global withheld',not data['decision']['global_optimizer_proved']),('source guard',not data['decision']['source_owned_physical_theory'])]
def main():
 if not ARTIFACT.exists() or '--print' in __import__('sys').argv:print(json.dumps(compute(),indent=2));return
 checks=validate(json.loads(ARTIFACT.read_text()))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
