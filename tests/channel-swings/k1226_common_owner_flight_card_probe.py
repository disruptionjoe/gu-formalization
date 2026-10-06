#!/usr/bin/env python3
"""Hostile mutations for K1226."""
import copy
import k1226_common_owner_flight_card as p
def main():
    edits=[(("decision","protocol_schema_constructed"),False),(("decision","physical_owner_instantiated"),True),
      (("decision","same_channel_assertion_requires_records"),False),(("decision","paper_protocol_is_empirical_evidence"),True),
      (("release_test","both_branches_present"),False),(("release_test","identity_keys_shared"),False),
      (("release_test","raw_records_required"),False),(("release_test","locality_and_systematics_explicit"),False),
      (("ownership","gu_native_effect"),"prediction")]
    n=0
    for path,val in edits:
        x=copy.deepcopy(p.build());d=x
        for k in path[:-1]: d=d[k]
        d[path[-1]]=val
        try:p.validate(x)
        except AssertionError:n+=1
    assert n==len(edits);print(f"K1226 hostile probes: {n}/{len(edits)}")
if __name__=="__main__":main()
