#!/usr/bin/env python3
"""Independent controls and hostile mutations for K476."""

from __future__ import annotations

import copy

from k476_k77_structural_rank_support_sieve import assess,demo,maximum_matching


def checks(p):
    t,c,k=p["theorem"],p["controls"],p["K77_application"]
    f,d,r=c["full_column_support"],c["hall_deficient_support"],c["full_row_support"]
    return [p["result_id"]=="K476-K77-STRUCTURAL-RANK-SUPPORT-SIEVE",
            p["classification"]=="BRIDGE_OR_SEMANTIC_BOUNDARY",
            "matching" in t["structural_rank"],"coefficient-independent" in t["hall_use"],
            "does not prove" in t["ceiling"],
            f["structural_rank"]==3,f["full_column_rank_possible"] is True,
            f["actual_rank_proved"] is False,d["structural_rank"]==2,
            d["support_can_reach_required_rank"] is False,d["hall_deficiency"]==1,
            r["structural_rank"]==3,r["full_row_rank_possible"] is True,
            k["D2_required_rank"]==10752,"every C2" in k["D2_required_support_property"],
            k["D1_required_rank"]==35840,"every C0" in k["D1_required_support_property"],
            k["native_D2_support_present"] is False,k["native_D1_support_present"] is False,
            k["native_packet_accepted"] is False]


def main()->int:
    p=demo();base=checks(p)
    muts=[lambda d:d.__setitem__("classification","PHYSICAL"),
          lambda d:d["theorem"].__setitem__("structural_rank","numerical determinant"),
          lambda d:d["theorem"].__setitem__("hall_use","optional"),
          lambda d:d["theorem"].__setitem__("ceiling","proves action"),
          lambda d:d["controls"]["hall_deficient_support"].__setitem__("support_can_reach_required_rank",True),
          lambda d:d["controls"]["hall_deficient_support"].__setitem__("hall_deficiency",0),
          lambda d:d["controls"]["full_column_support"].__setitem__("actual_rank_proved",True),
          lambda d:d["K77_application"].__setitem__("native_packet_accepted",True)]
    rejected=0
    for m in muts:
        c=copy.deepcopy(p);m(c);rejected+=not all(checks(c))
    invalid=0
    for fn,args in ((maximum_matching,(-1,2,[])),(maximum_matching,(2,2,[[0],[2]])),
                    (assess,(3,2,2,[[0],[1]]))):
        try: fn(*args)
        except ValueError: invalid+=1
    print(f"K476 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K476 HOSTILE MUTATIONS: {rejected}/{len(muts)} rejected")
    print(f"K476 INVALID INPUTS: {invalid}/3 rejected")
    return 0 if all(base) and rejected==len(muts) and invalid==3 else 1


if __name__=="__main__":raise SystemExit(main())
