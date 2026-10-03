#!/usr/bin/env python3
"""Hostile mutations for K856."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k856",H/"k856_sc_act_06_s13_stable_triviality.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
    b=M.build();ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["theorem"].update(base="S^12"),lambda p:p["theorem"].update(clutching_degree=13),lambda p:p["theorem"].update(classification_group="pi_13(O(h))"),lambda p:p["theorem"].update(stable_range_condition="h>=13"),lambda p:p["theorem"].update(stable_group="pi_12(O)=Z"),lambda p:p["theorem"].update(conclusion="all ranks trivial"),lambda p:p["theorem"].update(rank_13_status="trivial"),lambda p:p["theorem"].update(complex_bundles_are_not_being_classified=False),lambda p:p["exact_controls"].update(stable_h14=False),lambda p:p["exact_controls"].update(twelve_mod_eight=3),lambda p:p["exact_controls"].update(current_lower_bound=90123),lambda p:p["decision"].update(high_rank_S13_bundle_has_topological_clutching_obstruction=True),lambda p:p["decision"].update(abstract_triviality_implies_source_ownership=True),lambda p:p["controls"].update(hostile_mutations_rejected=15)]
    r=0
    for m in ms:
        p=copy.deepcopy(b);m(p)
        try:M.validate(p)
        except AssertionError:r+=1
    assert r==len(ms)==b["controls"]["hostile_mutations_rejected"];print(f"K856 hostile mutations rejected: {r}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
