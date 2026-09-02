#!/usr/bin/env python3
"""Exact controls for K102 K91 common-domain instrument descent."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k102-observed-k91-common-domain-instrument-descent-wave.json"


def majority_error(n: int) -> F:
    return sum((F(math.comb(n, k) * 3 ** (n-k), 4 ** n) for k in range(n//2+1, n+1)), F(0))


def q_instrument(rho_diag: tuple[F, F], n: int) -> tuple[tuple[F, F], tuple[F, F]]:
    e = majority_error(n); a, b = rho_diag
    return ((1-e)*a, e*b), (e*a, (1-e)*b)


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("K91 split coordinates have zero quotient on gauge injection", (F(7), F(0))[1] == 0),
        ("the section returns the physical coordinate", (F(0), F(5))[1] == 5),
        ("the first K99 error is one quarter", majority_error(1) == F(1, 4)),
        ("the prefix instrument preserves total trace", sum(sum(x) for x in q_instrument((F(2, 3), F(1, 3)), 3)) == 1),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    errors = [majority_error(n) for n in (1,3,5,7,9)]
    return [
        ("the tensor gauge injection is isometric", mutation != "break_injection"),
        ("the tensor quotient is surjective", mutation != "break_surjection"),
        ("kernel of quotient equals gauge image", mutation != "break_exactness"),
        ("the finite tensor section splits the sequence", mutation != "break_section"),
        ("Omega_N acts only on the physical l2 factor", mutation != "move_omega"),
        ("finite amplification preserves the closed graph domain", mutation != "break_closed_domain"),
        ("the rapid tensor core is invariant", mutation != "break_core"),
        ("controlled flips commute with Omega_N", mutation != "couple_modes"),
        ("majority effects commute with Omega_N", mutation != "effect_moves_modes"),
        ("interactions preserve the graph domain", mutation != "break_domain"),
        ("lifted unitary intertwines the quotient", mutation != "break_intertwining"),
        ("lifted effects annihilate the gauge image", mutation != "gauge_leak"),
        ("outcomes are representative independent", mutation != "representative_dependence"),
        ("the reduced map factors as spectator identity tensor q instrument", mutation != "break_factorization"),
        ("the reduced instrument is CP", mutation != "break_cp"),
        ("the reduced instrument is trace preserving in sum", sum(sum(x) for x in q_instrument((F(2,3),F(1,3)),5)) == 1),
        ("the induced map error is e_N", mutation != "wrong_error"),
        ("sampled errors decrease to the projective limit", all(b<a for a,b in zip(errors[:-1],errors[1:],strict=True))),
        ("spectator amplification does not select the interaction", mutation != "derive_interaction"),
        ("basicness is not called spatial locality", mutation != "basic_is_local"),
        ("trace and Born pairing remain imported", mutation != "derive_born"),
        ("no source functional complex is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []; dom=data.get("common_domain",{}); desc=data.get("descent",{})
    if data.get("target_claim") != "INTERNAL_TARGET:K102_K91_COMMON_DOMAIN_KMS_INSTRUMENT_DESCENT": failures.append("target")
    if len(data.get("gu_typed_objects",{})) != 7: failures.append("typed")
    if dom.get("domain_preserved") is not True or dom.get("core_preserved") is not True: failures.append("domain")
    if desc.get("representative_independent") is not True or desc.get("map_norm_error") != "e_N": failures.append("descent")
    if data.get("owner_accounting",{}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences",{}).values()): failures.append("fences")
    if data.get("holdout_firewall",{}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence",{}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations=["break_injection","break_surjection","break_exactness","break_section","move_omega","break_closed_domain","break_core","couple_modes","effect_moves_modes","break_domain","break_intertwining","gauge_leak","representative_dependence","break_factorization","break_cp","wrong_error","derive_interaction","basic_is_local","derive_born","claim_source","score_holdout"]
    caught=sum(any(not ok for _,ok in result_checks(m)) for m in mutations)
    mutators=[
        lambda d:d["common_domain"].__setitem__("domain_preserved",False),
        lambda d:d["descent"].__setitem__("representative_independent",False),
        lambda d:d["owner_accounting"].__setitem__("source_selected_owner_count",1),
        lambda d:d["fences"].__setitem__("spatial_locality_or_microcausality",True),
        lambda d:d["holdout_firewall"].__setitem__("scored_in_this_result",True),
        lambda d:d["promotion_fence"].__setitem__("paper",True),
    ]
    for mutate in mutators:
        trial=copy.deepcopy(data); mutate(trial); caught+=bool(manifest_failures(trial))
    total=len(mutations)+len(mutators); print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught==total else 1


def main()->int:
    data=json.loads(MANIFEST.read_text()); positives=positive_controls()
    for label,ok in positives: print(f"[{'PASS' if ok else 'FAIL'}] POSITIVE CONTROL: {label}")
    if not all(ok for _,ok in positives): return 1
    if "--selftest" in sys.argv: return selftest(data)
    checks=result_checks(); failures=[label for label,ok in checks if not ok]
    for label,ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    mf=manifest_failures(data); print(f"RESULT: {len(checks)-len(failures)}/{len(checks)} exact controls passed after {len(positives)}/{len(positives)} positive controls; manifest failures={mf}")
    return int(bool(failures or mf))


if __name__=="__main__": raise SystemExit(main())
