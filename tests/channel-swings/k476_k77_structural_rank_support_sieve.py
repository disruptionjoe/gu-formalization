#!/usr/bin/env python3
"""K476 bipartite-support structural-rank and Hall-deficiency sieve."""

from __future__ import annotations

import argparse
import json


def maximum_matching(source_size:int,target_size:int,edges:list[list[int]])->dict:
    if source_size<0 or target_size<0 or len(edges)!=source_size:
        raise ValueError("invalid bipartite support dimensions")
    if any(any((not isinstance(v,int)) or v<0 or v>=target_size for v in row) for row in edges):
        raise ValueError("support index outside target")
    match=[-1]*target_size
    def aug(u,seen):
        for v in sorted(set(edges[u])):
            if v in seen: continue
            seen.add(v)
            if match[v]<0 or aug(match[v],seen):
                match[v]=u; return True
        return False
    rank=sum(aug(u,set()) for u in range(source_size))
    matched_sources={u for u in match if u>=0}
    return {"source_size":source_size,"target_size":target_size,
            "structural_rank":rank,"unmatched_source_count":source_size-len(matched_sources),
            "unmatched_target_count":target_size-rank,
            "full_column_rank_possible":rank==source_size,
            "full_row_rank_possible":rank==target_size,
            "matching_target_to_source":match}


def assess(required_rank:int,source_size:int,target_size:int,edges:list[list[int]])->dict:
    if required_rank<0 or required_rank>min(source_size,target_size):
        raise ValueError("required rank outside matrix dimensions")
    m=maximum_matching(source_size,target_size,edges)
    return {**m,"required_rank":required_rank,
            "support_can_reach_required_rank":m["structural_rank"]>=required_rank,
            "hall_deficiency":max(0,required_rank-m["structural_rank"]),
            "actual_rank_proved":False,
            "nilpotence_proved":False,
            "action_custody_proved":False}


def demo()->dict:
    full=assess(3,3,4,[[0,1],[1,2],[2,3]])
    deficient=assess(3,3,4,[[0],[0],[1,2,3]])
    square=assess(3,4,3,[[0],[0,1],[1,2],[2]])
    return {"schema_version":"1.0","result_id":"K476-K77-STRUCTURAL-RANK-SUPPORT-SIEVE",
            "classification":"BRIDGE_OR_SEMANTIC_BOUNDARY","direction":"observed_to_native",
            "theorem":{"structural_rank":"maximum bipartite matching size of the coefficient support graph",
                       "hall_use":"structural rank below the required K475 rank is a coefficient-independent rejection",
                       "ceiling":"sufficient support does not prove numerical rank, nilpotence, domain preservation or action custody"},
            "controls":{"full_column_support":full,"hall_deficient_support":deficient,"full_row_support":square},
            "K77_application":{"D2_required_rank":10752,"D2_required_support_property":"matching covers every C2 source",
                               "D1_required_rank":35840,"D1_required_support_property":"matching covers every C0 target",
                               "native_D2_support_present":False,"native_D1_support_present":False,
                               "native_packet_accepted":False}}


def main()->int:
    argparse.ArgumentParser().parse_args();print(json.dumps(demo(),indent=2,sort_keys=True));return 0


if __name__=="__main__":raise SystemExit(main())
