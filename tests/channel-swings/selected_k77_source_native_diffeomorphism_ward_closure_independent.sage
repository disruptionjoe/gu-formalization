#!/usr/bin/env sage
"""Independent exact certificate for the source-native physical Ward graph.

This extends the independent Sage/QQ(i) K77 Clifford/exterior construction,
not the Python implementation under test.  It adds the physical metric owner
and the full Cartan connection column on every matched causal covector.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
load(str(ROOT / "tests/channel-swings/selected_k77_kosmann_moving_shiab_rank3_independent.sage"))

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


physical = {}
for name, q in orbits.items():
    chis = [eta(q, nu) for nu in range(4)]
    principals = [principal(q, chi) for chi in chis]
    metric = [form_scale(-1, value) for value in principals]
    complete = []
    frozen = []
    missing_moving = []
    missing_lower = []
    for chi, dg, first in zip(chis, metric, principals):
        lower_t = coefficient_derivative(T, chi)
        delta_varpi = form_add(first, lower_t)
        moving = hodge(d_shiab(F, chi))
        varpi = form_add(hodge(shiab(curvature(q, delta_varpi))), delta_varpi)
        varpi_frozen = form_add(hodge(shiab(curvature(q0, delta_varpi))), delta_varpi)
        complete.append(form_add(dg, varpi, moving))
        frozen.append(form_add(dg, varpi_frozen, moving))
        missing_moving.append(form_add(dg, varpi))
        missing_lower.append(
            form_add(dg, hodge(shiab(curvature(q, first))), first, moving)
        )

    check(family_rank(principals) == 3)
    check(family_rank(metric) == 3)
    check(family_rank(complete) == 0)
    check(family_rank(missing_moving) == 3)
    check(family_rank(missing_lower) == 3)
    check((family_rank(frozen) == 0) == (name == "timelike"))
    physical[name] = {
        "physical_jacobian_rank": 4,
        "spin_connection_rank": 3,
        "complete_ward_defect_rank": family_rank(complete),
        "frozen_q0_defect_rank": family_rank(frozen),
    }

# A grade-one gamma column is neither introduced nor needed anywhere above.
check(all(row["complete_ward_defect_rank"] == 0 for row in physical.values()))

print("SAGE_INDEPENDENT_K77_SOURCE_NATIVE_PHYSICAL_WARD_PASS")
print("MATCHED_Q_PHYSICAL_WARD=ZERO_TIMELIKE_SPACELIKE_NULL")
print("FROZEN_Q0=TIMELIKE_ONLY__SPACELIKE_NULL_FAIL")
print("GRADE1_GAMMA=ABSENT")
print("CHECKS=%s" % checks)
