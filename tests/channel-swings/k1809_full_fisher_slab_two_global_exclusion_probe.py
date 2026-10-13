#!/usr/bin/env python3
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; P=ROOT/'tests/channel-swings/k1809_full_fisher_slab_two_global_exclusion.py'
S=importlib.util.spec_from_file_location('k1809',P); k=importlib.util.module_from_spec(S); S.loader.exec_module(k)
def main():
 d=json.loads(k.ARTIFACT.read_text()); got=k.compute(); tests=[
  ('claim',lambda x:x.__setitem__('claim_id','K1808')),
  ('count',lambda x:x['certificate'].__setitem__('slab_two_retained_leaf_count',6)),
  ('composition',lambda x:x['certificate'].__setitem__('retained_rectangle_strictly_above_threshold',False)),
  ('boundary',lambda x:x['decision'].__setitem__('all_slab_two_faces_and_corners_covered_by_uniform_value_bound',False))]
 for i,(label,mut) in enumerate(tests,1):
  t=copy.deepcopy(d);mut(t);assert not all(v for _,v in k.validate(t,got)),label;print(f'PASS {i:02d}: rejects {label}')
 print(f'RESULT: PASS {len(tests)}/{len(tests)}')
if __name__=='__main__':main()
