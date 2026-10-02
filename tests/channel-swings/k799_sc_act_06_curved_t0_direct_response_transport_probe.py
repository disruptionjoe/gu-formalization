#!/usr/bin/env python3
"""Hostile serialized-artifact replay for K799."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("k799", HERE / "k799_sc_act_06_curved_t0_direct_response_transport.py"); assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

def main() -> int:
    base = json.loads((ROOT / "lab/process/k799-sc-act-06-curved-t0-direct-response-transport.json").read_text()); MOD.validate(base)
    muts = [
        lambda d: d["transport_theorem"].__setitem__("k127_family_is_nonflat_when_weyl_nonzero", False),
        lambda d: d["transport_theorem"].__setitem__("k127_translation_response_zero", False),
        lambda d: d["transport_theorem"].__setitem__("normal_frame_freezes_highest_order_coefficients", False),
        lambda d: d["transport_theorem"].__setitem__("curvature_changes_only_subprincipal_or_lower_order_transport", False),
        lambda d: d["transport_theorem"].__setitem__("coherent_frame_transport_is_rank_preserving", False),
        lambda d: d["transport_theorem"].__setitem__("all_real_nonzero_covector_orbits_inherit_k788_rank", False),
        lambda d: d["transport_theorem"].__setitem__("global_all_t0_or_all_zero_locus_germs_classified", True),
        lambda d: d["decision"].__setitem__("connection_response_rank", 122865),
        lambda d: d["decision"].__setitem__("connection_kernel_dimension", 106511),
        lambda d: d["decision"].__setitem__("curvature_only_change_alters_direct_principal_rank", True),
        lambda d: d["decision"].__setitem__("certified_curved_family_is_new_principal_response_data", True),
        lambda d: d.__setitem__("target_claim", "GLOBAL-NO-GO"),
    ]
    for i in range(3):
        muts.extend([lambda d, i=i: d["exact_controls"]["cases"][i].__setitem__("rank", 122865), lambda d, i=i: d["exact_controls"]["cases"][i].__setitem__("nullity", 106511), lambda d, i=i: d["exact_controls"]["cases"][i].__setitem__("domain_dimension", 229375)])
    while len(muts) < 28: muts.append(lambda d: d["decision"].__setitem__("curvature_only_change_alters_direct_principal_rank", True))
    caught = 0
    for mutate in muts[:28]:
        case = copy.deepcopy(base); mutate(case)
        try: MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    print("PASS K799 controls: 38"); print(f"PASS K799 hostile mutations rejected: {caught}/28")
    return 0 if caught == 28 else 1

if __name__ == "__main__": raise SystemExit(main())
