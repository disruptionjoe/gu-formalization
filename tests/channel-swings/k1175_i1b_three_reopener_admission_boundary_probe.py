#!/usr/bin/env python3
"""Hostile mutations for K1175."""
from copy import deepcopy
from k1175_i1b_three_reopener_admission_boundary import build, validate


def main():
    mutations = [
        ("inputs", None, []), ("deficit", "timelike", 98371),
        ("constraint", None, "finite channel already passes"), ("gauge", None, "rank four is enough"),
        ("changed_parent", None, "no Hessian change needed"), ("mixed_repair_rule", None, "resources need not add"),
        ("classes", None, []), ("current", None, 1),
        ("next_condition", None, "take more derivatives"), ("protected_disposition", None, "SC-ACT-06 refuted"),
        ("scope_boundary", None, "global GU no-go"), ("scorable_rows_added", None, 1),
    ]
    caught = 0
    for a, b, v in mutations:
        d = deepcopy(build())
        if a == "deficit": d["best_case_repair_deficits"][b] = v
        elif a in d["single_axis_reopeners"]: d["single_axis_reopeners"][a] = v
        elif a == "classes": d["classes_with_zero_repair_credit"] = v
        elif a == "current": d["current_candidates_meeting_full_packet"] = v
        else: d[a] = v
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1175 hostile probes: 12/12")


if __name__ == "__main__": main()
