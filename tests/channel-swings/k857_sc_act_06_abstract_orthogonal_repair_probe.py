#!/usr/bin/env python3
"""Hostile mutations for K857."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k857",H/"k857_sc_act_06_abstract_orthogonal_repair.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=M.build();ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["construction"].update(hypotheses=[]),lambda p:p["construction"].update(orthonormal_frame="pointwise choices"),lambda p:p["construction"].update(composition="unknown"),lambda p:p["construction"].update(exactness="rank sum only"),lambda p:p["construction"].update(hodge_operator="L=tau"),lambda p:p["construction"].update(uniform_gap=0),lambda p:p["construction"].update(map_norms={"T":2,"R":1}),lambda p:p["construction"].update(k853_radius_exact="1"),lambda p:p["construction"].update(ownership_from_triviality=True),lambda p:p["exact_control"].update(tau_S=[[1,0],[0,0],[0,0]]),lambda p:p["exact_control"].update(hodge_is_identity=False),lambda p:p["exact_control"].update(rank_sum=4),lambda p:p["decision"].update(topological_triviality_selects_GU_maps=True),lambda p:p["decision"].update(current_flat_packet_repaired=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=17)];r=0
 for m in ms:
  p=copy.deepcopy(b);m(p)
  try:M.validate(p)
  except AssertionError:r+=1
 assert r==len(ms)==b["controls"]["hostile_mutations_rejected"];print(f"K857 hostile mutations rejected: {r}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
