"""Independent Sage/QQ audit of the K77 coupled-complex scope gate."""

from sage.all import *


checks = 0
failures = []


def check(label, condition):
    global checks
    checks += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    if not ok:
        failures.append(label)


DIM = 4
eta = diagonal_matrix(QQ, [-1, 1, 1, 1])
slots = [(i, j) for i in range(DIM) for j in range(i, DIM)]
slot_index = {pair: index for index, pair in enumerate(slots)}
A = QQ(15376) / 13689
B = -QQ(340) / 4563
C4 = QQ(14356) / 13689
mass2 = QQ(1922) / 3589


def basis(i, j):
    result = zero_matrix(QQ, DIM)
    result[i, j] = 1
    result[j, i] = 1
    return result


def vertical_pair(left, right):
    return (eta * left * eta * right).trace() - QQ(1) / 2 * (eta * left).trace() * (eta * right).trace()


def delta_algebraic_slice(wave, mu, nu):
    return matrix(QQ, DIM, DIM, lambda a, b:
        QQ(1) / 2 * (
            wave[a, mu] * eta[nu, b]
            + eta[a, mu] * wave[nu, b]
            + wave[a, nu] * eta[mu, b]
            + eta[a, nu] * wave[mu, b]
        )
        - QQ(1) / 2 * (wave[a, b] * eta[mu, nu] + eta[a, b] * wave[mu, nu]))


def delta_ii(wave, value):
    return [[
        -(value if mu == 0 and nu == 0 else 0) * wave
        - QQ(1) / 2 * delta_algebraic_slice(wave, mu, nu)
        for nu in range(DIM)] for mu in range(DIM)]


def selected_bilinear(left, right, value):
    dleft = delta_ii(left, value)
    dright = delta_ii(right, value)
    full = QQ(0)
    for mu in range(DIM):
        for nu in range(DIM):
            full += eta[mu, mu] * eta[nu, nu] * vertical_pair(dleft[mu][nu], dright[mu][nu])
    trace_left = sum((eta[mu, mu] * dleft[mu][mu] for mu in range(DIM)), zero_matrix(QQ, DIM))
    trace_right = sum((eta[mu, mu] * dright[mu][mu] for mu in range(DIM)), zero_matrix(QQ, DIM))
    return A * full + B * vertical_pair(trace_left, trace_right)


metric_basis = [basis(*pair) for pair in slots]
raw_two = matrix(QQ, 10, 10, lambda i, j: selected_bilinear(metric_basis[i], metric_basis[j], QQ(2)))
raw_zero = matrix(QQ, 10, 10, lambda i, j: selected_bilinear(metric_basis[i], metric_basis[j], QQ(0)))
H2 = raw_two - raw_zero

D = zero_matrix(QQ, 10, 4)
for column in range(4):
    for row, (i, j) in enumerate(slots):
        D[row, column] = (1 if i == 0 and j == column else 0) + (1 if j == 0 and i == column else 0)

check("independent second-layer metric block is symmetric rank ten", H2.is_symmetric() and H2.rank() == 10)
check("independent metric gauge map has rank four", D.rank() == 4)
check("independent second-layer Ward defect has rank four", (H2 * D).rank() == 4)

plus = vector(QQ, 10)
plus[slot_index[(1, 1)]] = 1
plus[slot_index[(2, 2)]] = -1
cross = vector(QQ, 10)
cross[slot_index[(1, 2)]] = 1
expected_tt = 2 * C4 * 2 * (2 + mass2)
check("independent plus mode reproduces the selected TT value", plus * H2 * plus == expected_tt)
check("independent cross mode reproduces the selected TT value", cross * H2 * cross == expected_tt)

P = identity_matrix(QQ, 10) - D * (D.transpose() * D).inverse() * D.transpose()
check("independent gauge-basic projector has rank six", P.is_symmetric() and P.rank() == 6)
check("independent gauge-basic projector annihilates gauge", P * D == zero_matrix(QQ, 10, 4))
check("gauge-basic addition cannot repair the actual defect", (H2 + QQ(7) / 5 * P) * D == H2 * D)

sym_basis = []
for row in range(10):
    for column in range(row, 10):
        item = zero_matrix(QQ, 10)
        item[row, column] = 1
        item[column, row] = 1
        sym_basis.append(item)
ward_map = matrix(QQ, 40, 55, lambda row, column: (sym_basis[column] * D).list()[row])
target = vector(QQ, (-H2 * D).list())
check("independent symmetric Ward map has rank 34", ward_map.rank() == 34)
check("independent formal Ward cancellation is solvable", ward_map.augment(matrix(QQ, 40, 1, target)).rank() == 34)
check("independent completion family has affine dimension 21", 55 - ward_map.rank() == 21)

G = block_matrix(QQ, [[D], [zero_matrix(QQ, 24, 4)]])
H1_control = identity_matrix(QQ, 34) - G * (G.transpose() * G).inverse() * G.transpose()
H2_embed = block_diagonal_matrix(H2, zero_matrix(QQ, 24))
check("Ward-basic 34-variable control has gauge-only kernel", H1_control.rank() == 30 and H1_control * G == 0)
check("naive actual metric-block addition breaks control Ward rank four", ((H1_control + H2_embed) * G).rank() == 4)

check("PLANT a 21-parameter formal fit is not unique", 55 - ward_map.rank() != 0)
check("PLANT the retained ten are not a closed Ward complex", H2 * D != 0)

print("RESULT=COUPLED_COMPLEX_REQUIRED__FORMAL_COMPLETION_DIMENSION21")
print("CHECKS=%d" % checks)
if failures:
    raise RuntimeError("FAILURES: " + "; ".join(failures))
print("PASS %d/%d" % (checks, checks))
