#!/usr/bin/env python3
"""Independent controls and hostile mutations for K475."""

from __future__ import annotations

import copy

from k475_k77_acyclic_rank_profile import acyclic_rank_profile,demo,homology


def checks(p):
    t,k,c,n=p["theorem"],p["K77_profile"],p["controls"],p["native_release"]
    return [p["result_id"]=="K475-K77-ACYCLIC-RANK-PROFILE",
            p["classification"]=="BRIDGE_OR_SEMANTIC_BOUNDARY",
            "D1 D2=0" in t["complex"],"n2-r2" in t["homology_dimensions"],
            "unique" in t["acyclicity"],t["euler_zero_necessary"] is True,
            t["ranks_do_not_supply_action_coefficients"] is True,
            k["euler_characteristic"]==0,k["required_rank_D2"]==10752,
            k["required_rank_D1"]==35840,k["final_boundary_match"] is True,
            k["acyclic_rank_profile_possible"] is True,k["uniqueness"] is True,
            c["acyclic_homology"]==[0,0,0],c["low_arrow_defect"]==[0,70,70],
            c["high_arrow_defect"]==[21,21,0],
            c["nonzero_euler_impossible"]["acyclic_rank_profile_possible"] is False,
            n["action_coefficients_present"] is False,n["nilpotence_from_coefficients_checked"] is False,
            n["physical_cohomology_emitted"] is False]


def main()->int:
    p=demo(); base=checks(p)
    muts=[lambda d:d.__setitem__("classification","PHYSICAL"),
          lambda d:d["theorem"].__setitem__("complex","vector spaces"),
          lambda d:d["theorem"].__setitem__("euler_zero_necessary",False),
          lambda d:d["theorem"].__setitem__("ranks_do_not_supply_action_coefficients",False),
          lambda d:d["K77_profile"].__setitem__("required_rank_D2",0),
          lambda d:d["K77_profile"].__setitem__("required_rank_D1",0),
          lambda d:d["controls"].__setitem__("low_arrow_defect",[0,0,0]),
          lambda d:d["controls"].__setitem__("high_arrow_defect",[0,0,0]),
          lambda d:d["native_release"].__setitem__("physical_cohomology_emitted",True)]
    rejected=0
    for m in muts:
        c=copy.deepcopy(p);m(c);rejected+=not all(checks(c))
    invalid=0
    for f,args in ((acyclic_rank_profile,[1,2]),(acyclic_rank_profile,[1,-1,0]),
                   (homology,([1,2,1],[2,0])),(homology,([1,2,1],[1,2]))):
        try: f(*args) if isinstance(args,tuple) else f(args)
        except ValueError: invalid+=1
    print(f"K475 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K475 HOSTILE MUTATIONS: {rejected}/{len(muts)} rejected")
    print(f"K475 INVALID INPUTS: {invalid}/4 rejected")
    return 0 if all(base) and rejected==len(muts) and invalid==4 else 1


if __name__=="__main__": raise SystemExit(main())
