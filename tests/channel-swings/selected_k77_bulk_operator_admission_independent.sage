#!/usr/bin/env sage
"""Independent exact reconstruction of the K77 mixed-order admission bound."""

from pathlib import Path
import json
from itertools import product

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append(ok)
    print(("PASS" if ok else "FAIL") + " " + label)


def strict(relative):
    return json.loads((ROOT / relative).read_text(), object_pairs_hook=lambda pairs: _strict(pairs))


def _strict(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate key " + key)
        out[key] = value
    return out


fields = ("g", "varpi", "epsilon")
m1 = vector(ZZ, [2, 1, 1])
m2 = vector(ZZ, [1, 1, 1])
H1 = matrix(ZZ, 3, 3, lambda i, j: m1[i] + m1[j])
H2 = matrix(ZZ, 3, 3, lambda i, j: m2[i] + m2[j])
check("first-action safe Euler bound", H1 == matrix(ZZ, [[4,3,3],[3,2,2],[3,2,2]]))
check("stationary residual-square bound", H2 == matrix(ZZ, 3, 3, [2]*9))

admissible = []
for w in product(range(5), range(5), range(5)):
    if all(H1[i,j] <= w[i] + w[j] for i in range(3) for j in range(3)):
        admissible.append(tuple(ZZ(x) for x in w))
minimal = [w for w in admissible if not any(v != w and all(v[i] <= w[i] for i in range(3)) for v in admissible)]
check("unique minimal DN weight", minimal == [(2,1,1)])
check("uniform one rejected", (1,1,1) not in admissible)
check("uniform two compatible but nonminimal", (2,2,2) in admissible and (2,2,2) not in minimal)

parents = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
trace = strict("lab/process/selected-k77-common-graded-trace-boundary-triple.json")
gram = strict("lab/process/selected-k77-stationary-gram-boundary-strata.json")
check("full pointwise direction count", parents["exact_result"]["varpi_pointwise_direction_count"] == 14*16384)
check("even plus odd parent split", parents["exact_result"]["block_even_dimension"] + parents["exact_result"]["half_exchanging_odd_dimension"] == 16384)
check("parent remains unselected", not parents["exact_result"]["parent_selected"])
check("partial Gram is 34 fields", gram["exact_result"]["field_dimension"] == 10+24)
check("complete operator unowned", trace["boundary_triple_readiness"]["complete_action_owned_gauge_fixed_bulk_operator"] == "UNOWNED")
check("Dmax Dmin unowned", trace["boundary_triple_readiness"]["closed_Dmax_Dmin"] == "UNOWNED")
check("trace carrier not graph domain", trace["layer0"]["boundary_trace_space"] == "not_a_bulk_graph_domain")

# Plants mirror the errors the primary gate is designed to catch.
check("PLANT pointwise does not imply functional tangent", not parents["exact_result"]["functional_tangent_complete"])
check("PLANT H7 and H8 are not uniformly identical", not trace["graded_trace"]["H7_H8_uniform_identification"])
check("PLANT observed X4 is not ambient domain", trace["domain_routes"]["observed_X4_defect_domain_as_ambient_domain"] == "TYPE_ERROR")

if not all(checks):
    raise SystemExit("independent admission gate failed")
print("PASS %d/%d" % (len(checks), len(checks)))
