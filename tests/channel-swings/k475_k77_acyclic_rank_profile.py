#!/usr/bin/env python3
"""K475 exact acyclic rank-profile compiler for a three-term complex."""

from __future__ import annotations

import argparse
import json


def acyclic_rank_profile(dimensions: list[int]) -> dict:
    if len(dimensions) != 3 or any(not isinstance(n, int) or n < 0 for n in dimensions):
        raise ValueError("three nonnegative integer dimensions required")
    n2, n1, n0 = dimensions
    r2 = n2
    r1 = n1 - r2
    possible = r1 == n0 and 0 <= r1 <= min(n1, n0)
    return {
        "dimensions_C2_C1_C0": dimensions,
        "euler_characteristic": n2 - n1 + n0,
        "required_rank_D2": r2,
        "required_rank_D1": r1,
        "final_boundary_match": r1 == n0,
        "acyclic_rank_profile_possible": possible,
        "rank_recurrence": "r2=n2; r1=n1-r2; require r1=n0",
        "uniqueness": possible,
    }


def homology(dimensions: list[int], ranks: list[int]) -> list[int]:
    if len(dimensions) != 3 or len(ranks) != 2:
        raise ValueError("three dimensions and two ranks required")
    n2,n1,n0=dimensions; r2,r1=ranks
    if min(dimensions+ranks)<0 or r2>min(n2,n1) or r1>min(n1,n0) or r2+r1>n1:
        raise ValueError("invalid dimensions or ranks")
    return [n2-r2, n1-r2-r1, n0-r1]


def demo() -> dict:
    dims=[10752,46592,35840]
    profile=acyclic_rank_profile(dims)
    return {
        "schema_version":"1.0",
        "result_id":"K475-K77-ACYCLIC-RANK-PROFILE",
        "classification":"BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction":"observed_to_native",
        "theorem":{
            "complex":"C2 --D2--> C1 --D1--> C0 with D1 D2=0",
            "homology_dimensions":"[n2-r2, n1-r2-r1, n0-r1]",
            "acyclicity":"forces the unique recurrence r2=n2 and r1=n1-r2=n0",
            "euler_zero_necessary":True,
            "ranks_do_not_supply_action_coefficients":True,
        },
        "K77_profile":profile,
        "controls":{
            "acyclic_homology":homology(dims,[10752,35840]),
            "low_arrow_defect":homology(dims,[10752,35770]),
            "high_arrow_defect":homology(dims,[10731,35840]),
            "nonzero_euler_impossible":acyclic_rank_profile([2,4,3]),
        },
        "native_release":{
            "action_coefficients_present":False,
            "nilpotence_from_coefficients_checked":False,
            "physical_cohomology_emitted":False,
        },
    }


def main()->int:
    argparse.ArgumentParser().parse_args(); print(json.dumps(demo(),indent=2,sort_keys=True)); return 0


if __name__=="__main__": raise SystemExit(main())
