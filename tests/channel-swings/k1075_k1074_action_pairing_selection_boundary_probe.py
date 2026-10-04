#!/usr/bin/env python3
"""Hostile mutations for K1075."""
from copy import deepcopy
from k1075_k1074_action_pairing_selection_boundary import build, validate


def main():
    mutations=[("requirements",[]),("requirements.4.candidate_grade","pass"),("requirements.0.gu_source_owned",True),("counts.mathematical_pass_or_conditional",5),("selection_result","mass one selected"),("circularity_result","candidate energy is independent evidence"),("source_scope.SC-META-53","RESOLVED"),("ledger_effect","LT-SM8 SAME"),("next_condition","score now"),("target_claim","CONFIRMED")]
    caught=0
    for path,value in mutations:
        data=deepcopy(build()); node=data; parts=path.split(".")
        try:
            for part in parts[:-1]: node=node[int(part)] if part.isdigit() else node[part]
            node[parts[-1]]=value
            validate(data)
        except (AssertionError,KeyError): caught+=1
    assert caught==len(mutations); print(f"K1075 hostile probes: {caught}/{len(mutations)}")


if __name__=="__main__": main()
