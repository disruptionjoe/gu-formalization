#!/usr/bin/env python3
"""Hostile mutations for K839's finite-cutoff limit gate."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k839_sc_act_06_finite_cutoff_limit_gate.py")
SPEC = importlib.util.spec_from_file_location("k839", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("input pin", lambda x: x["pinned_inputs"]["k831"].__setitem__("sha256", "0" * 64)),
        ("carrier", lambda x: x["governance"].__setitem__("carrier", "C^N")),
        ("pairing", lambda x: x["governance"].__setitem__("pairing_or_form", "indefinite")),
        ("action ownership", lambda x: x["governance"].__setitem__("action_owner", "GU action")),
        ("section invertibility", lambda x: x["finite_cutoff_limit_certificate"]["finite_section"].__setitem__("all_positive_integer_cutoffs_invertible", False)),
        ("section inverse norm", lambda x: x["finite_cutoff_limit_certificate"]["finite_section"].__setitem__("inverse_norm_rule", "1")),
        ("capped convergence", lambda x: x["finite_cutoff_limit_certificate"]["capped_full_space_cutoff"].__setitem__("operator_norm_convergence_to_T", False)),
        ("capped error", lambda x: x["finite_cutoff_limit_certificate"]["capped_full_space_cutoff"].__setitem__("operator_norm_error_rule", "1/(N+1)")),
        ("sample inverse norm", lambda x: x["finite_cutoff_limit_certificate"]["samples"]["inverse_norms"].__setitem__(3, "7")),
        ("uniform inverse bound", lambda x: x["finite_cutoff_limit_certificate"].__setitem__("uniform_inverse_bound", True)),
        ("limit kernel", lambda x: x["limit_certificate"].__setitem__("kernel_dimension", 1)),
        ("limit injectivity", lambda x: x["limit_certificate"].__setitem__("injective", False)),
        ("dense range", lambda x: x["limit_certificate"].__setitem__("range_dense", False)),
        ("witness preimage", lambda x: x["limit_certificate"].__setitem__("formal_preimage_in_ell2", True)),
        ("surjectivity", lambda x: x["limit_certificate"].__setitem__("range_surjective", True)),
        ("closed range", lambda x: x["limit_certificate"].__setitem__("range_closed", True)),
        ("fredholm", lambda x: x["limit_certificate"].__setitem__("fredholm", True)),
        ("negative stability", lambda x: x["exact_controls"]["negative_control"].__setitem__("inverse_norms_uniformly_bounded", True)),
        ("positive instability", lambda x: x["exact_controls"]["positive_control"].__setitem__("inverse_norms_uniformly_bounded", False)),
        ("positive nonfredholm", lambda x: x["exact_controls"]["positive_control"].__setitem__("limit_fredholm", False)),
        ("false implication", lambda x: x["gate"].__setitem__("finite_cutoff_invertibility_plus_operator_norm_convergence_implies_limit_fredholmness", True)),
        ("finite cutoff accepted", lambda x: x["decision"].__setitem__("k838_closed_global_fredholm_row_satisfied_by_finite_cutoffs", True)),
        ("GU family invented", lambda x: x["decision"].__setitem__("actual_gu_cutoff_family_or_limit_domain_constructed", True)),
        ("source ledger changed", lambda x: x.__setitem__("source_and_ledger_effect", "CHANGED")),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(MODULE.build())
        mutate(candidate)
        try:
            MODULE.validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K839 hostile mutations rejected: 24/24")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
