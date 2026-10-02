#!/usr/bin/env python3
"""Hostile mutations for K834."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k834_sc_act_06_rich_moduli_admission_compiler.py")
SPEC = importlib.util.spec_from_file_location("k834", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("family count", lambda x: x["compiler"].__setitem__("family_row_count", 17)),
        ("post count", lambda x: x["compiler"].__setitem__("post_symbol_row_count", 6)),
        ("total count", lambda x: x["compiler"].__setitem__("total_row_count", 24)),
        ("elliptic implies rich", lambda x: x["compiler"].__setitem__("elliptic_complex_implies_rich_moduli", True)),
        ("synthetic rejected", lambda x: x["exact_controls"].__setitem__("synthetic_rich_moduli_admitted", False)),
        ("missing nonlinear not elliptic", lambda x: x["exact_controls"].__setitem__("missing_nonlinear_elliptic_admitted", False)),
        ("missing nonlinear rich", lambda x: x["exact_controls"].__setitem__("missing_nonlinear_rich_moduli_admitted", True)),
        ("GU missing hidden", lambda x: x["exact_controls"].__setitem__("current_gu_missing_row_count", 0)),
        ("GU elliptic", lambda x: x["exact_controls"].__setitem__("current_gu_elliptic_admitted", True)),
        ("GU rich", lambda x: x["exact_controls"].__setitem__("current_gu_rich_moduli_admitted", True)),
        ("family invented", lambda x: x["decision"].__setitem__("actual_source_relative_family_constructed", True)),
        ("global verdict", lambda x: x["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True)),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(MODULE.build())
        mutate(candidate)
        try:
            MODULE.validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K834 hostile mutations rejected: 12/12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
