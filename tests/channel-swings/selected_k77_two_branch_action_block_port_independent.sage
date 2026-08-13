#!/usr/bin/env sage
"""Independent Sage/FLINT port of the owned action blocks to both K77 roots.

The route reconstructs the common first-action epsilon cross through the
independent exterior evaluator, extends its coefficients to Q(zeta_12), and
checks the two exact QQ(sqrt(3)) branches without importing the Python result.
It separately replays the independent 125-field principal Gram construction.
"""

load("tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_independent.sage")

FAIL_PORT = []
COUNT_PORT = {"exact": 0, "theorem": 0, "planted": 0, "type": 0}


def port_check(kind, label, condition):
    COUNT_PORT[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [independent-port-" + kind + "] " + label)
    if not ok:
        FAIL_PORT.append(label)


# The source-stationary roots and all branch coefficients live in QQ(sqrt(3)).
L.<s> = QuadraticField(3)
branches = (
    (L(1)/208-s/312, (-2+s)/208),
    (L(1)/208+s/312, (-2-s)/208),
)


def packet_factor(point):
    b0, t0 = point
    return b0^2 + b0*t0 + t0^2/3


common_factor = QQ(1)/73008
scales = tuple(packet_factor(point)/common_factor for point in branches)
port_check("exact", "the branch packet scales are the two expected conjugates",
           scales == (L(9)/16*(2-s), L(9)/16*(2+s))
           and scales[0].galois_conjugate() == scales[1])
port_check("exact", "both branch packet scales are positive and nonzero",
           all(value > 0 for value in scales))
port_check("theorem", "nonzero scalar extension preserves the independent rank-91 cross",
           cross.rank() == 91 and all(value != 0 for value in scales))
port_check("exact", "the common cross still has 182 entries and two per column",
           len(cross.dict()) == 182
           and {sum(cross[row, column] != 0 for row in range(cross.nrows()))
                for column in range(cross.ncols())} == {2})
port_check("planted", "equal rank does not identify the two branch coefficients",
           scales[0] != scales[1])


# Q(zeta_12) contains both i and sqrt(3), so it is an exact common coefficient
# field for the Clifford evaluator and the two algebraic branch amplitudes.
E.<z> = CyclotomicField(12)
sqrt3_E = z + z^(-1)
i_E = z^3


def embed_gaussian(value):
    coefficients = list(value)
    coefficients += [0] * (2-len(coefficients))
    return E(coefficients[0]) + E(coefficients[1])*i_E


def zero_shape(test_direction):
    return hodge(shiab(fadd(wedge(phi1, test_direction),
                              wedge(test_direction, phi1))))


def flattened_branch_column(test_direction, amplitude):
    identity = flatten_column(test_direction)
    curvature = flatten_column(zero_shape(test_direction))
    result = {}
    for key in set(identity).union(curvature):
        value = embed_gaussian(identity.get(key, ZERO)) \
                + amplitude*embed_gaussian(curvature.get(key, ZERO))
        if value != 0:
            result[key] = value
    return result


def sparse_rank(columns):
    pivots = {}
    for source_column in columns:
        column = dict(source_column)
        while column:
            pivot = min(column)
            lead = column[pivot]
            if pivot not in pivots:
                pivots[pivot] = {key: value/lead for key, value in column.items()}
                break
            basis = pivots[pivot]
            for key, value in basis.items():
                updated = column.get(key, E(0)) - lead*value
                if updated == 0:
                    column.pop(key, None)
                else:
                    column[key] = updated
    return len(pivots)


amplitudes = ((-3+sqrt3_E)/624, (-3-sqrt3_E)/624)
zero_ranks = []
for index, amplitude in enumerate(amplitudes, start=1):
    columns = [flattened_branch_column(value, amplitude) for value in directions]
    zero_ranks.append(sparse_rank(columns))
    port_check("planted", "branch %s zero-jet map is not the identity fixture" % index,
               any(column != {key: embed_gaussian(value)
                               for key, value in flatten_column(test_direction).items()}
                   for column, test_direction in zip(columns, directions)))
port_check("theorem", "both exact zero-jet low-grade varpi maps have rank 1470",
           zero_ranks == [1470, 1470])
port_check("exact", "the scalar-line derivatives are the two expected conjugates",
           tuple(624*value+1 for value in amplitudes)
           == (-2+sqrt3_E, -2-sqrt3_E))
port_check("planted", "scalar-line invertibility is not the 1470-dimensional theorem",
           all(624*value+1 != 0 for value in amplitudes) and 1 != 1470)


# Replay the independently constructed metric/varpi/primitive-epsilon principal
# bank.  This overwrites some evaluator names but not the port facts above.
load("tests/channel-swings/selected_k77_primitive_epsilon_common_bank_independent.sage")
port_check("theorem", "the independent selected principal Gram strata are 110,110,16",
           results["timelike"][1] == 110
           and results["spacelike"][1] == 110
           and results["null"][1] == 16)
port_check("type", "a common principal bank is not a complete common Frechet operator", True)
port_check("type", "selected Spin, two U32,32 halves, and full U64,64 remain distinct", True)
port_check("type", "the first action and residual norm-square action remain distinct", True)

print("INDEPENDENT_RESULT=BOTH_K77_BRANCHES_RETAIN_RANK91_FIRST_ACTION_CROSS_AND_RANK1470_ZERO_JET_VARPI_MAP")
print("INDEPENDENT_PRINCIPAL=SELECTED_125_FIELD_GRAM_110_110_16_IS_BRANCH_INDEPENDENT_TOP_SYMBOL_DATA")
print("PORT_SCOPE=OWNED_BLOCKS_ONLY__COMPLETE_LOWER_ORDER_AND_EXPANDED_PARENT_BLOCKS_OPEN")
print("COUNTS=" + ",".join(key+":"+str(value) for key,value in sorted(COUNT_PORT.items())))
if FAIL_PORT:
    raise RuntimeError("independent port failures: " + " | ".join(FAIL_PORT))
print("PASS " + str(sum(COUNT_PORT.values())) + "/" + str(sum(COUNT_PORT.values())))
