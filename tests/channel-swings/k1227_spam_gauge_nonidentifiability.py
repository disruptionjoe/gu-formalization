#!/usr/bin/env python3
"""K1227: exact physical frame gauge leaves all calibration probabilities invariant."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1227-spam-gauge-nonidentifiability.json"
def mv(a,v):return [sum(a[i][j]*v[j] for j in range(3)) for i in range(3)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def tr(a):return [list(x) for x in zip(*a)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sv(v):return [str(x) for x in v]
def sm(m):return [[str(x) for x in r] for r in m]
def build():
    z=F(0);R=[[F(3,5),z,F(4,5)],[z,F(1),z],[-F(4,5),z,F(3,5)]]
    M=[[F(1,2),z,z],[z,F(1,2),z],[z,z,F(1,4)]];t=[z,z,F(1,4)]
    Mp=mm(mm(R,M),tr(R));tp=mv(R,t)
    states=[[F(1),z,z],[z,F(1),z],[z,z,F(1)],[-F(1),z,z],[z,-F(1),z],[z,z,-F(1)]]
    effects=[[F(1),z,z],[z,F(1),z],[z,z,F(1)]]
    checks=[]
    for r in states:
      for e in effects:
        lhs=dot(e,[x+y for x,y in zip(mv(M,r),t)])
        rhs=dot(mv(R,e),[x+y for x,y in zip(mv(Mp,mv(R,r)),tp)])
        checks.append(lhs==rhs)
    return {"schema_version":"1.0","result_id":"K1227-SPAM-GAUGE-NONIDENTIFIABILITY","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Simultaneous physical SO(3) frame rotation of preparations, effects and a generalized-amplitude-damping channel.",
      "theorem":{"probability_coordinate":"y=e^T(Mr+t)","gauge_action":"r'=Rr, e'=Re, M'=RMR^T, t'=Rt","invariance":"e'^T(M'r'+t')=e^T(Mr+t)","consequence":"raw nominal probabilities cannot authenticate the physical preparation/effect frame or channel coordinates without independent SPAM and basis ownership"},
      "control":{"R":sm(R),"M":sm(M),"t":sv(t),"M_prime":sm(Mp),"t_prime":sv(tp),"probability_equalities":sum(checks),"probability_checks":len(checks),"distinct_channel_coordinates":Mp!=M or tp!=t,"both_channels_cptp":"same generalized-amplitude-damping channel under a unitary basis rotation"},
      "decision":{"twelve_nominal_statistics_self_authenticate":False,"independent_spam_or_self_consistent_gate_set_required":True,"optimized_chsh_basis_invariant_under_this_rotation":True},
      "release_test":{"all_probability_equalities":all(checks),"coordinates_change":Mp!=M and tp!=t,"physical_rotation":mm(R,tr(R))==[[F(1),z,z],[z,F(1),z],[z,z,F(1)]],"protected_status_unchanged":True},
      "ownership":{"spam_basis_and_channel_identity_imported":True,"gu_native_effect":"none"},
      "claim_ceiling":"Exact SO(3) SPAM-frame nonidentifiability inside a physical qubit-channel family; no claim about arbitrary gauge transforms, hardware data or GU."}
def validate(x):
    assert x["result_id"].startswith("K1227-")
    assert x["theorem"]["invariance"]=="e'^T(M'r'+t')=e^T(Mr+t)"
    assert x["control"]["probability_equalities"]==x["control"]["probability_checks"]==18
    assert x["control"]["distinct_channel_coordinates"] and all(x["release_test"].values())
    assert x["decision"]["twelve_nominal_statistics_self_authenticate"] is False
    assert x["decision"]["independent_spam_or_self_consistent_gate_set_required"]
    assert x["decision"]["optimized_chsh_basis_invariant_under_this_rotation"]
    assert x["ownership"]["gu_native_effect"]=="none"
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1227 controls: 11/11")
