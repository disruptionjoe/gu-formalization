#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k491", HERE / "k491_k139_cyclic_tail_kernel_form.py")
K491 = importlib.util.module_from_spec(spec); spec.loader.exec_module(K491)


def checks(payload):
    t = payload["exact_theorem"]; d = payload["decision"]; c = payload["exact_control"]
    return [
        payload["result_id"] == "K491-K139-CYCLIC-TAIL-KERNEL-FORM",
        payload["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        t["metric_entries"] == "M_ij=B_max(i,j), B_j=sum_(n>=j)a_n",
        t["base_cross"] == "R0(e0,t)=E1/B0",
        t["q00_shape_specialization"] == "+3O/A",
        t["q10_shape_specialization"] == "-3O/A",
        c["identities_verified"] is True,
        c["metric_matrix"][0][1] == c["tail_masses"][1],
        c["base_cross_identity"] == "E1/A",
        c["combined_cross_identity"].startswith("(E1+"),
        d["cancellation_safe_base_cross_reduced"] is True,
        d["separate_auxiliary_piece_absolute_values_used"] is False,
        d["native_scalar_tail_numerically_evaluated"] is False,
        payload["source_and_ledger_effect"] == "none",
        "no full K162 complement" in payload["claim_ceiling"],
    ]


def selftest():
    bad = 0
    for kwargs in [
        dict(word_masses=[2, 1], shifted_free_diagonal=[1, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
        dict(word_masses=[1, 0], shifted_free_diagonal=[1, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
        dict(word_masses=[1, 1], shifted_free_diagonal=[2, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
    ]:
        try: K491.compile_cyclic_form(**kwargs)
        except K491.CertificateError: bad += 1
    payload = K491.build()
    for mut in [
        lambda p: p["decision"].__setitem__("cancellation_safe_base_cross_reduced", False),
        lambda p: p["decision"].__setitem__("separate_auxiliary_piece_absolute_values_used", True),
        lambda p: p["exact_control"].__setitem__("identities_verified", False),
        lambda p: p["exact_theorem"].__setitem__("q00_shape_specialization", "-3O/A"),
        lambda p: p.__setitem__("source_and_ledger_effect", "moved"),
    ]:
        q = copy.deepcopy(payload); mut(q); bad += int(not all(checks(q)))
    return bad == 8


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--selftest",action="store_true"); a=parser.parse_args()
    if a.selftest:
        ok=selftest(); print("K491 SELFTEST", "PASS 8/8" if ok else "FAIL"); return 0 if ok else 1
    result=checks(K491.build()); print(f"K491 controls: {sum(result)}/{len(result)}"); return 0 if all(result) else 1


if __name__ == "__main__": raise SystemExit(main())
