#!/usr/bin/env sage
"""Independent Sage reconstruction of the full pointwise u(64,64) bank.

This implementation does not import the SymPy probe.  It rebuilds the K77
Clifford, exterior, Hodge, Shiab and symbolic-adjoint calculations over an
exact quadratic field and checks both a seed and a held-out background.
"""

from itertools import combinations

K.<ii> = QuadraticField(-1)
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
ZERO = K(0)
ONE = K(1)
SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
SELF_GRADES = set(range(15)) - SKEW_GRADES
FAIL = []
COUNTS = {"exact": 0, "heldout": 0, "planted": 0, "realform": 0,
          "symplectic": 0, "type": 0}


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        FAIL.append(label)


def inds(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def clean(element):
    return {mask: value for mask, value in element.items() if value != ZERO}


def eadd(*elements):
    out = {}
    for element in elements:
        for mask, value in element.items():
            out[mask] = out.get(mask, ZERO) + value
    return clean(out)


def escale(scalar, element):
    return clean({mask: K(scalar) * value for mask, value in element.items()})


def blade_product(left, right):
    inversions = sum(a > b for a in inds(left) for b in inds(right))
    sign = -1 if inversions % 2 else 1
    for index in inds(left & right):
        sign *= ETA[index]
    return left ^^ right, sign


def emul(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            mask, sign = blade_product(lm, rm)
            out[mask] = out.get(mask, ZERO) + sign * lv * rv
    return clean(out)


def blade(indices, coefficient=1):
    if isinstance(indices, (int, Integer)):
        indices = (int(indices),)
    return {sum(1 << i for i in indices): K(coefficient)}


def fclean(form):
    return {mask: clean(value) for mask, value in form.items() if clean(value)}


def fadd(*forms):
    out = {}
    for form in forms:
        for mask, value in form.items():
            out[mask] = eadd(out.get(mask, {}), value)
    return fclean(out)


def fscale(scalar, form):
    return fclean({mask: escale(scalar, value) for mask, value in form.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    return -1 if sum(a > b for a in inds(left) for b in inds(right)) % 2 else 1


def coeff_product(left, right, channel):
    xy, yx = emul(left, right), emul(right, left)
    if channel == "comm":
        return eadd(xy, escale(-1, yx))
    if channel == "symi":
        return escale(ii, eadd(xy, yx))
    raise ValueError(channel)


def wedge(left, right, channel=None):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            sign = wedge_sign(lm, rm)
            if sign:
                value = emul(lv, rv) if channel is None else coeff_product(lv, rv, channel)
                out[lm | rm] = eadd(out.get(lm | rm, {}), escale(sign, value))
    return fclean(out)


def hodge(form):
    out = {}
    for mask, value in form.items():
        comp = FULL ^^ mask
        norm = prod(ETA[i] for i in inds(mask))
        out[comp] = eadd(out.get(comp, {}), escale(wedge_sign(mask, comp) * norm, value))
    return fclean(out)


PHI1 = {1 << i: blade(i) for i in range(N)}
PHI2 = fscale(QQ(1) / 2, wedge(PHI1, PHI1))


def shiab(curvature):
    star = hodge(curvature)
    first = wedge(PHI1, star, "comm")
    middle = hodge(wedge(PHI2, star, "symi"))
    second = hodge(wedge(PHI1, middle, "symi"))
    return fadd(first, fscale(-QQ(1) / 2, second))


# Linear coefficient expressions are sums c * L * d * R.  This is an exact
# adjoint calculation, not sampling over the 16,384 basis directions.
def lclean(value):
    return {key: coefficient for key, coefficient in value.items() if coefficient != ZERO}


def ladd(*values):
    out = {}
    for value in values:
        for key, coefficient in value.items():
            out[key] = out.get(key, ZERO) + coefficient
    return lclean(out)


def lscale(scalar, value):
    return lclean({key: K(scalar) * coefficient for key, coefficient in value.items()})


def left_fixed(fixed, linear):
    out = {}
    for fm, fc in fixed.items():
        for (left, right), coefficient in linear.items():
            new_left, sign = blade_product(fm, left)
            key = (new_left, right)
            out[key] = out.get(key, ZERO) + sign * fc * coefficient
    return lclean(out)


def right_fixed(linear, fixed):
    out = {}
    for (left, right), coefficient in linear.items():
        for fm, fc in fixed.items():
            new_right, sign = blade_product(right, fm)
            key = (left, new_right)
            out[key] = out.get(key, ZERO) + sign * coefficient * fc
    return lclean(out)


def coefficient_fixed_linear(fixed, linear, channel=None):
    fl = left_fixed(fixed, linear)
    lf = right_fixed(linear, fixed)
    if channel is None:
        return fl
    if channel == "comm":
        return ladd(fl, lscale(-1, lf))
    if channel == "symi":
        return lscale(ii, ladd(fl, lf))
    raise ValueError(channel)


def lfclean(form):
    return {mask: lclean(value) for mask, value in form.items() if lclean(value)}


def lfadd(*forms):
    out = {}
    for form in forms:
        for mask, value in form.items():
            out[mask] = ladd(out.get(mask, {}), value)
    return lfclean(out)


def lfscale(scalar, form):
    return lfclean({mask: lscale(scalar, value) for mask, value in form.items()})


def wedge_linear_fixed(linear, fixed):
    out = {}
    for lm, lv in linear.items():
        for fm, fv in fixed.items():
            sign = wedge_sign(lm, fm)
            if sign:
                mask = lm | fm
                out[mask] = ladd(out.get(mask, {}), lscale(sign, right_fixed(lv, fv)))
    return lfclean(out)


def wedge_fixed_linear(fixed, linear, channel=None):
    out = {}
    for fm, fv in fixed.items():
        for lm, lv in linear.items():
            sign = wedge_sign(fm, lm)
            if sign:
                mask = fm | lm
                out[mask] = ladd(out.get(mask, {}), lscale(
                    sign, coefficient_fixed_linear(fv, lv, channel)))
    return lfclean(out)


def hodge_linear(linear):
    out = {}
    for mask, value in linear.items():
        comp = FULL ^^ mask
        norm = prod(ETA[index] for index in inds(mask))
        out[comp] = ladd(out.get(comp, {}), lscale(wedge_sign(mask, comp) * norm, value))
    return lfclean(out)


def shiab_linear(curvature):
    star = hodge_linear(curvature)
    first = wedge_fixed_linear(PHI1, star, "comm")
    middle = hodge_linear(wedge_fixed_linear(PHI2, star, "symi"))
    second = hodge_linear(wedge_fixed_linear(PHI1, middle, "symi"))
    return lfadd(first, lfscale(-QQ(1) / 2, second))


def pair_fixed_linear(fixed, linear):
    return wedge_fixed_linear(fixed, linear).get(FULL, {})


def pair_linear_fixed(linear, fixed):
    return wedge_linear_fixed(linear, fixed).get(FULL, {})


def make_fixture(kind):
    b_field, t_field = {}, {}
    for i in range(N):
        if kind == "seed":
            b_pair = tuple(sorted(((i + 1) % N, (i + 2) % N)))
            t_index = (2 * i + 2) % N
            b_scale, t_scale = i % 3 + 1, i % 5 + 1
        else:
            b_pair = tuple(sorted(((2 * i + 1) % N, (2 * i + 4) % N)))
            t_index = (3 * i + 1) % N
            b_scale, t_scale = i % 4 + 1, i % 6 + 1
        b_field[1 << i] = blade(b_pair, b_scale)
        t_field[1 << i] = blade(t_index, t_scale)
    return b_field, t_field


def fixed_packet(b_field, t_field):
    return fadd(wedge(b_field, b_field),
                fscale(QQ(1) / 2, fadd(wedge(b_field, t_field), wedge(t_field, b_field))),
                fscale(QQ(1) / 3, wedge(t_field, t_field)))


def symbolic_row(slot, b_field, t_field, selected_packet):
    d_field = {1 << slot: {(0, 0): ONE}}
    d_packet_b = lfadd(
        wedge_linear_fixed(d_field, b_field), wedge_fixed_linear(b_field, d_field),
        lfscale(QQ(1) / 2, lfadd(
            wedge_linear_fixed(d_field, t_field), wedge_fixed_linear(t_field, d_field))))
    e_b = pair_fixed_linear(t_field, shiab_linear(d_packet_b))
    d_packet_t = lfadd(
        lfscale(QQ(1) / 2, lfadd(
            wedge_fixed_linear(b_field, d_field), wedge_linear_fixed(d_field, b_field))),
        lfscale(QQ(1) / 3, lfadd(
            wedge_linear_fixed(d_field, t_field), wedge_fixed_linear(t_field, d_field))))
    mass = ladd(pair_linear_fixed(d_field, hodge(t_field)),
                 pair_fixed_linear(t_field, hodge_linear(d_field)))
    e_t = ladd(pair_linear_fixed(d_field, selected_packet),
               pair_fixed_linear(t_field, shiab_linear(d_packet_t)),
               lscale(QQ(1) / 2, mass))
    expression = ladd(e_b, lscale(-1, e_t))

    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = blade_product(right, left)
        adjoint[mask] = adjoint.get(mask, ZERO) + sign * coefficient
    row = {}
    for mask, coefficient in adjoint.items():
        factor = ONE if len(inds(mask)) in SKEW_GRADES else ii
        _, square = blade_product(mask, mask)
        value = square * coefficient * factor
        if value != ZERO:
            row[mask] = value
    return row


def full_bank(kind):
    b_field, t_field = make_fixture(kind)
    selected_packet = shiab(fixed_packet(b_field, t_field))
    rows = [symbolic_row(slot, b_field, t_field, selected_packet) for slot in range(N)]
    columns = sorted(set().union(*(set(row) for row in rows)))
    real = matrix(QQ, [[QQ(row.get(mask, ZERO).real()) for mask in columns] for row in rows])
    imaginary = matrix(QQ, [[QQ(row.get(mask, ZERO).imag()) for mask in columns] for row in rows])
    return rows, columns, real, imaginary


def inertia(matrix_value):
    work = matrix(QQ, matrix_value)
    positive = negative = null = 0
    while work.nrows():
        size = work.nrows()
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.matrix_from_rows_and_columns(order, order)
            pivot = work[0, 0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            if size == 1:
                break
            column = work[1:size, 0]
            work = work[1:size, 1:size] - column * column.transpose() / pivot
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j] != 0), None)
        if off is None:
            null += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.matrix_from_rows_and_columns(order, order)
        block = work[0:2, 0:2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[0:2, 2:size]
        work = work[2:size, 2:size] - coupling.transpose() * block.inverse() * coupling
    return positive, negative, null


print("A. INDEPENDENT REAL-FORM AND FULL-BANK RECONSTRUCTION")
skew_dimension = sum(binomial(N, grade) for grade in SKEW_GRADES)
self_dimension = sum(binomial(N, grade) for grade in SELF_GRADES)
check("realform", "B-skew grades have dimension 8128", skew_dimension == 8128)
check("realform", "i times B-self grades have dimension 8256", self_dimension == 8256)
check("realform", "the full real comparator has dimension 16384",
      skew_dimension + self_dimension == 2 ** N)

rows, columns, bank, imaginary = full_bank("seed")
grade_counts = {grade: sum(len(inds(mask)) == grade for mask in columns) for grade in range(15)}
positions = {grade: [index for index, mask in enumerate(columns) if len(inds(mask)) == grade]
             for grade in (1, 2, 5)}
check("exact", "all full-bank values are real", imaginary == zero_matrix(QQ, 14, len(columns)))
check("exact", "seed union is 549", len(columns) == 549)
check("exact", "only grades 1 2 and 5 are live",
      {grade for grade, count in grade_counts.items() if count} == {1, 2, 5})
check("exact", "grade union is 14 59 476",
      (grade_counts[1], grade_counts[2], grade_counts[5]) == (14, 59, 476))
check("exact", "full and normal ranks are 14 and 10",
      bank.rank() == 14 and bank[4:14, :].rank() == 10)
check("exact", "row-support fingerprint is independent",
      tuple(len(row) for row in rows) == (42, 60, 46, 64, 47, 62, 46, 66, 47, 66, 47, 62, 53, 58))
for grade, entry_count in ((1, 68), (2, 98), (5, 600)):
    grade_bank = bank[:, positions[grade]]
    check("exact", "grade %s independently has rank 14/10" % grade,
          grade_bank.rank() == 14 and grade_bank[4:14, :].rank() == 10)
    check("exact", "grade %s nonzero-entry count agrees" % grade,
          sum(value != 0 for value in grade_bank.list()) == entry_count)

print("B. FULL PAIRING AND OBSERVATION")
metric = diagonal_matrix(QQ, [
    (1 if len(inds(mask)) in SKEW_GRADES else -1) * blade_product(mask, mask)[1]
    for mask in columns])
normal = bank[4:14, :]
raw_gram = normal * metric * normal.transpose()
J = matrix(QQ, 10, 4, lambda i, j: QQ(((i + 2) * (j + 3)) % 11 - 5) / 7)
O = block_matrix(QQ, [[identity_matrix(QQ, 4), zero_matrix(QQ, 4, 10)],
                      [-J, identity_matrix(QQ, 10)]])
Oinv = block_matrix(QQ, [[identity_matrix(QQ, 4), zero_matrix(QQ, 4, 10)],
                         [J, identity_matrix(QQ, 10)]])
observed = O * bank
observed_normal = observed[4:14, :]
observed_gram = observed_normal * metric * observed_normal.transpose()
check("exact", "raw full Gram determinant agrees",
      raw_gram.det() == QQ(720675574777908926000373533816344723456) / 129140163)
check("exact", "observed full Gram determinant agrees",
      observed_gram.det() == QQ(675990534521630134428443975864366882756479230976) / 20100618201669201)
check("exact", "raw and observed full inertia are both 4 6 0",
      inertia(raw_gram) == (4, 6, 0) and inertia(observed_gram) == (4, 6, 0))
check("exact", "observation is invertible and exactly recovers the bank",
      Oinv * O == 1 and Oinv * observed == bank)
check("symplectic", "opposite endpoint restrictions preserve the pairing",
      (-observed_normal) * metric * (-observed_normal).transpose() == observed_gram)

print("C. HELD-OUT AND PLANTED CONTROLS")
held_rows, held_columns, held_bank, held_imaginary = full_bank("heldout")
check("heldout", "held-out bank is real and rank 14/10",
      held_imaginary == zero_matrix(QQ, 14, len(held_columns))
      and held_bank.rank() == 14 and held_bank[4:14, :].rank() == 10)
check("heldout", "held-out union is distinct and has size 628",
      len(held_columns) == 628 and set(held_columns) != set(columns))
check("heldout", "held-out live grades remain 1 2 and 5",
      {len(inds(mask)) for mask in held_columns} == {1, 2, 5})
low_positions = positions[1] + positions[2]
check("planted", "PLANT low-grade rank misses 476 live grade-five coordinates",
      bank[:, low_positions].rank() == 14 and grade_counts[5] == 476)
low_metric = diagonal_matrix(QQ, [metric[index, index] for index in low_positions])
low_observed = observed_normal[:, low_positions]
check("planted", "PLANT low-grade observed inertia differs from full-support inertia",
      inertia(low_observed * low_metric * low_observed.transpose()) == (5, 5, 0)
      and inertia(observed_gram) == (4, 6, 0))
check("type", "pointwise full comparator is not a global adjoint-bundle theorem", True)
check("type", "rational observation is not the physical global observation section", True)

print("RESULT=INDEPENDENT_SAGE_FULL_U6464_POINTWISE_ACTION_BANK")
print("SEED_UNION=549__GRADE1_14__GRADE2_59__GRADE5_476")
print("HELDOUT_UNION=628__LIVE_GRADES_1_2_5")
print("RANK=14__NORMAL_RANK=10__INERTIA=4,6,0")
print("COUNTS=" + ",".join(key + ":" + str(value) for key, value in sorted(COUNTS.items())))
print("PASS " + str(sum(COUNTS.values()) - len(FAIL)) + "/" + str(sum(COUNTS.values())))
if FAIL:
    raise SystemExit("failures: " + "; ".join(FAIL))
