#!/usr/bin/env python3
"""Hostile mutations for K835."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
PATH = Path(__file__).with_name("k835_sc_act_06_higher_order_kuranishi_obstruction.py")
SPEC = importlib.util.spec_from_file_location("k835", PATH); MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader; SPEC.loader.exec_module(MODULE)
def main() -> int:
    muts = [
        ("jacobian", lambda x: x["exact_controls"].__setitem__("common_jacobian", [[1,0],[0,1]])),
        ("dimension", lambda x: x["exact_controls"].__setitem__("common_infinitesimal_dimension", 0)),
        ("actual dims", lambda x: x["exact_controls"].__setitem__("all_actual_local_dimensions", [1,0,0])),
        ("quadratic", lambda x: x["exact_controls"].__setitem__("quadratic_obstruction_vanishes_for_orders", [])),
        ("orders", lambda x: x["exact_controls"].__setitem__("first_obstruction_orders", [2,2,2])),
        ("row order", lambda x: x["exact_controls"]["families"][1].__setitem__("first_nonzero_projected_order", 2)),
        ("coefficient", lambda x: x["exact_controls"]["families"][2].__setitem__("first_nonzero_projected_coefficient", 1)),
        ("row dimension", lambda x: x["exact_controls"]["families"][0].__setitem__("actual_local_dimension", 1)),
        ("linear", lambda x: x["theorem"].__setitem__("linearized_kernel_determines_integrability", True)),
        ("quadratic decides", lambda x: x["theorem"].__setitem__("vanishing_quadratic_obstruction_determines_integrability", True)),
        ("finite universal", lambda x: x["theorem"].__setitem__("any_fixed_finite_jet_order_is_universal", True)),
        ("GU map", lambda x: x["decision"].__setitem__("actual_gu_kuranishi_germ_constructed", True)),
    ]
    for name, mutate in muts:
        p=copy.deepcopy(MODULE.build()); mutate(p)
        try: MODULE.validate(p)
        except AssertionError: continue
        raise AssertionError(name)
    print("K835 hostile mutations rejected: 12/12"); return 0
if __name__ == "__main__": raise SystemExit(main())
