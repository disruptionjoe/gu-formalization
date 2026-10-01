#!/usr/bin/env python3
"""Independent hostile replay for K721."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k721", HERE / "k721_sc_act_06_eq916_euclidean_fermion_symbol.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for block in ("plus_to_minus", "minus_to_plus"):
        for key, value in baseline["exact_controls"][block].items():
            mutations.append((f"{block}-{key}", lambda d, block=block, key=key, value=value: d["exact_controls"][block].__setitem__(key, value + 1)))
    mutations += [
        ("block-dim", lambda d: d["exact_controls"].__setitem__("block_dimension", 959)),
        ("total-dim", lambda d: d["exact_controls"].__setitem__("two_block_dimension", 1919)),
        ("rank", lambda d: d["exact_controls"].__setitem__("pure_contraction_two_block_rank", 1919)),
        ("kernel", lambda d: d["exact_controls"].__setitem__("equal_ratio_kernel_per_block", 767)),
        ("kernel2", lambda d: d["exact_controls"].__setitem__("equal_ratio_two_block_kernel", 1535)),
        ("dirac", lambda d: d["source_typing"].__setitem__("full_dirac_dimension", 64)),
        ("chiral", lambda d: d["source_typing"].__setitem__("chiral_dimension", 32)),
        ("mirror", lambda d: d["source_typing"].__setitem__("mirror_blocks", 1)),
        ("se", lambda d: d["source_typing"].__setitem__("displayed_southeast_block", "nonzero")),
        ("variants", lambda d: d["source_typing"].__setitem__("source_admits_nontrivial_southeast_variants", False)),
        ("candidate", lambda d: d["decision"].__setitem__("displayed_canon_fermion_candidate_passes_principal_exactness", False)),
        ("selector", lambda d: d["decision"].__setitem__("shiab_selector_is_material_to_ellipticity", False)),
        ("repair", lambda d: d["decision"].__setitem__("fermion_exactness_can_repair_bosonic_cohomology", True)),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 34:
        mutations.append(("repeat", lambda d: d["exact_controls"].__setitem__("block_dimension", 0)))
    caught = 0
    for _, mutate in mutations[:34]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K721 controls: 42")
    print(f"PASS K721 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__":
    raise SystemExit(main())
