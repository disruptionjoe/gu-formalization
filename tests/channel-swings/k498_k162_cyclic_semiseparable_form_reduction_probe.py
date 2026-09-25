#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k498", HERE / "k498_k162_cyclic_semiseparable_form_reduction.py")
K498 = importlib.util.module_from_spec(spec); spec.loader.exec_module(K498)


def checks(payload):
    theorem = payload["theorem"]; control = payload["exact_control"]; decision = payload["decision"]
    return [
        payload["result_id"] == "K498-K162-CYCLIC-SEMISEPARABLE-FORM-REDUCTION",
        payload["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        theorem["structure"].startswith("symmetric rank-one semiseparable"),
        theorem["metric_diagonal"].startswith("M(u_j,u_k)"),
        control["formula_matches_dense_congruence"] is True,
        len(control["contrast_M_norms"]) == 3,
        len(control["transformed_form"]) == 3,
        control["transformed_metric"][0][1] == "0",
        decision["K492_basis_composed_with_K491_form"] is True,
        decision["dense_cyclic_Gram_required"] is False,
        decision["native_infinite_cyclic_floor_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
        "No native infinite cyclic floor" in payload["claim_ceiling"],
    ]


def selftest():
    rejected = 0
    bad_inputs = [
        dict(word_masses=[2, 1], shifted_free_diagonal=[1, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
        dict(word_masses=[1, 0], shifted_free_diagonal=[1, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
        dict(word_masses=[1, 1], shifted_free_diagonal=[2, 1], regular_core_diagonal=[-1, 0], shape_diagonal=[0, 1]),
        dict(word_masses=[1], shifted_free_diagonal=[1], regular_core_diagonal=[-1], shape_diagonal=[0]),
    ]
    for kwargs in bad_inputs:
        try: K498.compile_reduction(**kwargs)
        except K498.CertificateError: rejected += 1
    for mutate in [
        lambda p: p["exact_control"].__setitem__("formula_matches_dense_congruence", False),
        lambda p: p["decision"].__setitem__("dense_cyclic_Gram_required", True),
        lambda p: p["decision"].__setitem__("native_infinite_cyclic_floor_emitted", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "moved"),
        lambda p: p.__setitem__("target_claim", "SC-ACT-01"),
        lambda p: p["theorem"].__setitem__("structure", "dense only"),
    ]:
        payload = copy.deepcopy(K498.build()); mutate(payload); rejected += int(not all(checks(payload)))
    return rejected == 10


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--selftest",action="store_true");args=parser.parse_args()
    if args.selftest:
        ok=selftest();print("K498 SELFTEST", "PASS 10/10" if ok else "FAIL");return 0 if ok else 1
    result=checks(K498.build());print(f"K498 controls: {sum(result)}/{len(result)}");return 0 if all(result) else 1


if __name__ == "__main__": raise SystemExit(main())
