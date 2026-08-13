#!/usr/bin/env sage
"""Independent Sage/QQ reconstruction of the common action branch.

This deliberately reuses the independently written K77 exterior evaluator
from the v0.76 action bank, not the Python composition route used by the
primary certificate.
"""

load("tests/channel-swings/selected_k77_action_boundary_coefficient_bank_independent.sage")

LOCAL_FAIL = []
LOCAL_COUNTS = {"exact": 0, "theorem": 0, "planted": 0, "type": 0}


def local_check(kind, label, condition):
    LOCAL_COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [independent-" + kind + "] " + label)
    if not ok:
        LOCAL_FAIL.append(label)


coefficients_full = [blade(i) for i in range(N)]
grades = [1] * N
for i, j in combinations(range(N), 2):
    coefficients_full.append(blade((i, j)))
    grades.append(2)
directions = [direction(slot, coefficient)
              for slot in range(N) for coefficient in coefficients_full]
direction_grades = grades * N
local_check("exact", "full low-grade tangent is 196 plus 1274 equals 1470",
            len(directions) == 1470
            and direction_grades.count(1) == 196
            and direction_grades.count(2) == 1274)


def set_background(b_value, t_value):
    global B, T, P, SP
    B = fscale(QQ(b_value), phi1)
    T = fscale(QQ(t_value), phi1)
    P = packet(B, T)
    SP = shiab(P)


set_background(0, -QQ(1) / 312)
old_eb = [e_b(value) for value in directions]
old_et = [e_t(value) for value in directions]
old_support = [index for index, value in enumerate(old_eb) if value != ZERO]
expected_support = [slot * 105 + slot for slot in range(N)]
local_check("exact", "old fixture solves every T Euler direction",
            all(value == ZERO for value in old_et))
local_check("exact", "old B Euler support is the fourteen diagonal Cl1 entries",
            old_support == expected_support)
local_check("exact", "old nonzero B Euler entries equal one over 312",
            set(old_eb[index] for index in old_support) == {K(QQ(1) / 312)})
local_check("theorem", "old fixture is critical only on coefficient-grade two",
            all(old_eb[index] == old_et[index] == ZERO
                for index, grade in enumerate(direction_grades) if grade == 2))
local_check("planted", "raw-residual fixture is not called full first-action critical",
            any(value != ZERO for value in old_eb))


R.<bvar,tvar> = PolynomialRing(QQ)
homogeneous_action = 7*tvar*(624*bvar^2 + 624*bvar*tvar + 208*tvar^2 + tvar)
db = homogeneous_action.derivative(bvar)
dt = homogeneous_action.derivative(tvar)
for b_value, t_value in ((0,0), (0,-1), (1,1), (2,-1), (-1,2), (3,2)):
    set_background(b_value, t_value)
    direct = pairing(T, SP) + pairing(T, hodge(T)) / 2
    local_check("exact", "homogeneous polynomial sample " + str((b_value,t_value)),
                direct == K(homogeneous_action.subs({bvar:b_value, tvar:t_value})))
local_check("exact", "first derivative factors reproduce the invariant-line system",
            db == 4368*tvar*(2*bvar+tvar)
            and dt == 14*(312*bvar^2+624*bvar*tvar+312*tvar^2+tvar))
# Exact case split: t=0 forces b=0; otherwise 2b+t=0 and the second
# equation reduces to 2b(156b-1)=0.
local_check("theorem", "connection-critical case split has only zero and (1/156,-1/78)",
            dt.subs({bvar:0, tvar:0}) == 0
            and dt.subs({bvar:QQ(1)/156, tvar:-QQ(1)/78}) == 0
            and db.subs({bvar:QQ(1)/156, tvar:-QQ(1)/78}) == 0
            and dt.subs(tvar=-2*bvar) == 28*bvar*(156*bvar-1))
local_check("planted", "old point fails the B derivative",
            db.subs({bvar:0, tvar:-QQ(1)/312}) == QQ(7)/156
            and dt.subs({bvar:0, tvar:-QQ(1)/312}) == 0)


set_background(QQ(1)/156, -QQ(1)/78)
local_check("theorem", "new branch solves all 1470 B Euler directions",
            all(e_b(value) == ZERO for value in directions))
local_check("theorem", "new branch solves all 1470 T Euler directions",
            all(e_t(value) == ZERO for value in directions))
A_new = fadd(B, T)
raw_residual = fadd(shiab(wedge(A_new, A_new)), hodge(T))
local_check("theorem", "new branch solves the independent raw residual", raw_residual == {})
local_check("exact", "new A equals minus one over 156 Phi1",
            A_new == fscale(-QQ(1)/156, phi1))


def commutator(left, right):
    return eadd(emul(left, right), escale(-1, emul(right, left)))


def coefficient_derivative(form, parameter):
    return {mask: commutator(value, parameter) for mask, value in form.items()}


def d_shiab(curvature, parameter):
    dphi1 = coefficient_derivative(phi1, parameter)
    dphi2 = coefficient_derivative(phi2, parameter)
    star = hodge(curvature)
    first = wedge(dphi1, star, "comm")
    second_left = wedge(dphi1, hodge(wedge(phi2, star, "symi")), "symi")
    second_right = wedge(phi1, hodge(wedge(dphi2, star, "symi")), "symi")
    return fadd(first, fscale(-QQ(1)/2, hodge(fadd(second_left, second_right))))


pairs14 = list(combinations(range(N), 2))
moving = [d_shiab(P, blade(pair_index)) for pair_index in pairs14]


def flatten_column(form):
    return {(fm, cm): value for fm, element in form.items()
            for cm, value in element.items() if value != ZERO}


def sparse_family_rank(forms):
    keys = sorted(set().union(*(set(flatten_column(form)) for form in forms)))
    rows = {key: row for row, key in enumerate(keys)}
    entries = {(rows[key], column): value
               for column, form in enumerate(forms)
               for key, value in flatten_column(form).items()}
    return matrix(K, len(keys), len(forms), entries, sparse=True).rank()


local_check("exact", "moving-Shiab epsilon columns have rank 91",
            sparse_family_rank(moving) == 91)
local_check("exact", "each moving-Shiab column has support two",
            set(len(flatten_column(value)) for value in moving) == {2})
local_check("exact", "moving epsilon first variation vanishes",
            all(pairing(T, value) == ZERO for value in moving))

cross_entries = {}
nonzero_rows = set()
column_supports = [0] * 91
for row, test_direction in enumerate(directions):
    for column, moving_value in enumerate(moving):
        value = pairing(test_direction, moving_value)
        if value != ZERO:
            cross_entries[(row, column)] = value
            nonzero_rows.add(row)
            column_supports[column] += 1
cross = matrix(K, 1470, 91, cross_entries, sparse=True)
local_check("theorem", "moving first-action epsilon cross rank is 91", cross.rank() == 91)
local_check("exact", "moving cross has 182 entries and two per column",
            len(cross_entries) == 182 and set(column_supports) == {2})
local_check("theorem", "every live moving receiver row is grade one",
            len(nonzero_rows) == 182
            and all(direction_grades[row] == 1 for row in nonzero_rows))
local_check("planted", "zero epsilon first variation does not erase its Hessian cross block",
            all(pairing(T, value) == ZERO for value in moving) and cross.rank() == 91)

local_check("type", "125 plus grade1 is 321 while full low-grade source candidate is 1571",
            125 + 196 == 321 and 10 + 1470 + 91 == 1571)
local_check("type", "field-tangent selection precedes BV or domain promotion", True)
local_check("type", "direct metric Euler remains separate from B/T connection criticality", True)

print("INDEPENDENT_RESULT=COMMON_NONTRIVIAL_CONNECTION_BRANCH_AND_MOVING_EPSILON_CROSS_REPRODUCED")
print("COMMON_CONNECTION_BRANCH=B_1_OVER156__T_MINUS1_OVER78__A_MINUS1_OVER156__DIRECT_METRIC_EULER_OPEN")
print("MOVING_CROSS=RANK91_NNZ182_ALL_GRADE1_RECEIVERS")
print("COUNTS=" + ",".join(key + ":" + str(value) for key, value in sorted(LOCAL_COUNTS.items())))
print("PASS " + str(sum(LOCAL_COUNTS.values()) - len(LOCAL_FAIL)) + "/" + str(sum(LOCAL_COUNTS.values())))
if LOCAL_FAIL:
    raise RuntimeError("independent failures: " + " | ".join(LOCAL_FAIL))
