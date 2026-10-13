#!/usr/bin/env python3
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'tests/channel-swings/k1810_full_fisher_global_optimizer_admission.py';S=importlib.util.spec_from_file_location('k1810',P);k=importlib.util.module_from_spec(S);S.loader.exec_module(k)
def main():
 d=json.loads(k.ARTIFACT.read_text());got=k.compute();tests=[('claim',lambda x:x.__setitem__('claim_id','K1809')),('boxes',lambda x:x['certificate'].__setitem__('slab_three_retained_boxes',0)),('uniqueness',lambda x:x['certificate'].__setitem__('slab_three_complete_uniqueness',True)),('global inflation',lambda x:x['decision'].__setitem__('global_optimizer_proved',True)),('physics inflation',lambda x:x['decision'].__setitem__('source_owned_physical_theory',True))]
 for i,(label,mut) in enumerate(tests,1):t=copy.deepcopy(d);mut(t);assert not all(v for _,v in k.validate(t,got)),label;print(f'PASS {i:02d}: rejects {label}')
 print(f'RESULT: PASS {len(tests)}/{len(tests)}')
if __name__=='__main__':main()
