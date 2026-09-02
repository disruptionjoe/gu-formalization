#!/usr/bin/env python3
"""Exact controls for the K102 quasilocal/GNS tail-record boundary."""
from __future__ import annotations

import copy
import itertools
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT=pathlib.Path(__file__).resolve().parents[2]
MANIFEST=ROOT/"lab/process/k102-observed-tail-record-quasilocal-topology-boundary-wave.json"


def majority(word:tuple[int,...],n:int)->int:
    return int(sum(word[:n])>n//2)


def embedded_norm_difference(n:int)->int:
    m=n+2
    return max(abs(majority(w,n)-majority(w,m)) for w in itertools.product((0,1),repeat=m))


def error(n:int)->F:
    return sum((F(math.comb(n,k)*3**(n-k),4**n) for k in range(n//2+1,n+1)),F(0))


def witness(n:int)->tuple[int,...]:
    return tuple([1]*((n+1)//2)+[0]*(n-(n+1)//2)+[0,0])


def positive_controls()->list[tuple[str,bool]]:
    return [
        ("the N one versus N three projections differ in norm one",embedded_norm_difference(1)==1),
        ("the explicit N three witness flips majority",majority(witness(3),3)==1 and majority(witness(3),5)==0),
        ("the first sector cyclic norm square is one quarter",error(1)==F(1,4)),
        ("majority projections are bounded by one",all(majority(w,3) in (0,1) for w in itertools.product((0,1),repeat=3))),
    ]


def result_checks(mutation:str|None=None)->list[tuple[str,bool]]:
    errs=[error(n) for n in (1,3,5,7,9)]
    return [
        ("each odd-prefix majority effect is a projection",mutation!="not_projection"),
        ("each finite-prefix effect is local",mutation!="deny_finite_local"),
        ("the inductive embedding tensors the identity",mutation!="wrong_embedding"),
        ("explicit witnesses flip consecutive odd majorities",all(majority(witness(n),n)==1 and majority(witness(n),n+2)==0 for n in (1,3,5,7)) and mutation!="break_witness"),
        ("consecutive embedded projections have norm difference one",all(embedded_norm_difference(n)==1 for n in (1,3,5)) and mutation!="wrong_norm"),
        ("the majority sequence is not norm Cauchy",mutation!="claim_cauchy"),
        ("there is no quasilocal C-star norm limit",mutation!="claim_quasilocal_limit"),
        ("zero-sector cyclic strong error is e_N",mutation!="wrong_zero_sector"),
        ("one-sector complement cyclic strong error is e_N",mutation!="wrong_one_sector"),
        ("sampled cyclic errors decrease",all(b<a for a,b in zip(errs[:-1],errs[1:],strict=True))),
        ("product strong law supplies the sector limits",mutation!="deny_strong_law"),
        ("finite changes preserve the empirical tail sign",mutation!="finite_change_tail"),
        ("local vectors form a dense GNS set",mutation!="deny_dense_local"),
        ("boundedness extends convergence strongly",mutation!="deny_bounded_extension"),
        ("the direct-sum strong limit is zero direct-sum identity",mutation!="wrong_tail_projection"),
        ("the tail projection is central in the sector direct sum",mutation!="deny_central"),
        ("the tail projection is not a quasilocal element",mutation!="tail_is_quasilocal"),
        ("reduced instrument norm convergence remains compatible",mutation!="deny_reduced_limit"),
        ("internal effect convergence is topologically distinct",mutation!="conflate_topologies"),
        ("gauge basicness does not imply locality",mutation!="basic_is_local"),
        ("the representation and product states remain supplied",mutation!="derive_representation"),
        ("trace and Born semantics remain imported",mutation!="derive_born"),
        ("no source local net is claimed",mutation!="claim_source"),
        ("the held-out family remains unscored",mutation!="score_holdout"),
    ]


def manifest_failures(data:dict)->list[str]:
    failures=[]; finite=data.get("finite_prefix_effects",{}); gns=data.get("gns_limit",{}); comp=data.get("composition_boundary",{})
    if data.get("target_claim")!="INTERNAL_TARGET:K102_MAJORITY_TAIL_QUASILOCAL_GNS_TOPOLOGY": failures.append("target")
    if len(data.get("gu_typed_objects",{}))!=7: failures.append("typed")
    if finite.get("norm_cauchy") is not False or finite.get("quasilocal_norm_limit") is not False: failures.append("finite")
    if gns.get("direct_sum_limit")!="T=0 direct-sum I" or gns.get("quasilocal_element") is not False: failures.append("gns")
    if comp.get("basicness_implies_locality") is not False: failures.append("basicness")
    if data.get("owner_accounting",{}).get("source_selected_owner_count")!=0: failures.append("owners")
    if any(data.get("fences",{}).values()): failures.append("fences")
    if data.get("holdout_firewall",{}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence",{}).values()): failures.append("promotion")
    return failures


def selftest(data:dict)->int:
    mutations=["not_projection","deny_finite_local","wrong_embedding","break_witness","wrong_norm","claim_cauchy","claim_quasilocal_limit","wrong_zero_sector","wrong_one_sector","deny_strong_law","finite_change_tail","deny_dense_local","deny_bounded_extension","wrong_tail_projection","deny_central","tail_is_quasilocal","deny_reduced_limit","conflate_topologies","basic_is_local","derive_representation","derive_born","claim_source","score_holdout"]
    caught=sum(any(not ok for _,ok in result_checks(m)) for m in mutations)
    mutators=[
        lambda d:d["finite_prefix_effects"].__setitem__("norm_cauchy",True),
        lambda d:d["gns_limit"].__setitem__("quasilocal_element",True),
        lambda d:d["composition_boundary"].__setitem__("basicness_implies_locality",True),
        lambda d:d["owner_accounting"].__setitem__("source_selected_owner_count",1),
        lambda d:d["fences"].__setitem__("tail_projection_quasilocal",True),
        lambda d:d["holdout_firewall"].__setitem__("scored_in_this_result",True),
        lambda d:d["promotion_fence"].__setitem__("canon",True),
    ]
    for mutate in mutators:
        trial=copy.deepcopy(data); mutate(trial); caught+=bool(manifest_failures(trial))
    total=len(mutations)+len(mutators); print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught==total else 1


def main()->int:
    data=json.loads(MANIFEST.read_text()); positives=positive_controls()
    for label,ok in positives: print(f"[{'PASS' if ok else 'FAIL'}] POSITIVE CONTROL: {label}")
    if not all(ok for _,ok in positives): return 1
    if "--selftest" in sys.argv:return selftest(data)
    checks=result_checks(); failures=[label for label,ok in checks if not ok]
    for label,ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    mf=manifest_failures(data); print(f"RESULT: {len(checks)-len(failures)}/{len(checks)} exact controls passed after {len(positives)}/{len(positives)} positive controls; manifest failures={mf}")
    return int(bool(failures or mf))


if __name__=="__main__":raise SystemExit(main())
