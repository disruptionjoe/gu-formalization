#!/usr/bin/env python3
"""Hostile mutations for K855."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k855", HERE / "k855_sc_act_06_cohomology_bundle.py")
M = importlib.util.module_from_spec(SPEC); assert SPEC.loader; SPEC.loader.exec_module(M)
def main() -> int:
    base = M.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"), lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["theorem"].update(base="arbitrary set"), lambda p: p["theorem"].update(complex="unrelated maps"),
        lambda p: p["theorem"].update(constant_rank_hypotheses=[]), lambda p: p["theorem"].update(bundle_conclusion="pointwise spaces"),
        lambda p: p["theorem"].update(rank_formula="rank(H)=dim(B)"), lambda p: p["theorem"].update(projector_formula="P_H=P_ker(J)"),
        lambda p: p["theorem"].update(pointwise_dimensions_alone_are_not_enough=False), lambda p: p["theorem"].update(rank_jumps_forbid_this_bundle_conclusion=False),
        lambda p: p["exact_control"].update(rank_G=1), lambda p: p["exact_control"].update(JG=[[1,0],[0,0]]),
        lambda p: p["exact_control"].update(projector_idempotent=False), lambda p: p["decision"].update(current_flat_packet_complete_cosphere_bundle_established=True),
        lambda p: p["decision"].update(source_owned_repair_maps_constructed=True), lambda p: p["controls"].update(hostile_mutations_rejected=15),
    ]
    rejected = 0
    for mutate in mutations:
        packet = copy.deepcopy(base); mutate(packet)
        try: M.validate(packet)
        except AssertionError: rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K855 hostile mutations rejected: {rejected}/{len(mutations)}"); return 0
if __name__ == "__main__": raise SystemExit(main())
