# Independent Sage/QQ replay of the action/contact Legendre-owner correction.

D = matrix(QQ, [
    [-1, 1, 0, 0],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
])
Rg = block_matrix([[identity_matrix(QQ, 4)], [D]])
K1 = diagonal_matrix(QQ, [-1, 2, 3])
K2 = diagonal_matrix(QQ, [-2, 5, 7])


def contact_hessian(K):
    return block_matrix([
        [D.transpose() * K * D, -D.transpose() * K],
        [-K * D, K],
    ])


H1 = contact_hessian(K1)
H2 = contact_hessian(K2)
assert H1 * Rg == zero_matrix(QQ, 7, 4)
assert H2 * Rg == zero_matrix(QQ, 7, 4)
assert Rg.transpose() * H1 == zero_matrix(QQ, 4, 7)
assert Rg.transpose() * H2 == zero_matrix(QQ, 4, 7)
assert H1.rank() == H2.rank() == 3
t_edge = vector(QQ, [2, -3, 5])
assert K1 * t_edge != K2 * t_edge

PZ.<z> = PolynomialRing(QQ)
C = matrix(QQ, [[0, 1, 2], [-2, 1, 0], [1, -1, 1]])
T = matrix(QQ, [[1, 0, -1], [2, -1, 1], [0, 1, 2]])
L = matrix(QQ, [[1, 1, 0], [0, 2, -1], [1, 0, 1]])
R = matrix(QQ, [[2, 0, 1], [-1, 1, 0], [0, 1, 1]])
kappa = QQ(5) / 7
Cz = C.change_ring(PZ)
Tz = z * T.change_ring(PZ)
Lz = L.change_ring(PZ)
Rz = R.change_ring(PZ)
packet = Cz * Cz + (Cz * Tz + Tz * Cz) / 2 + Tz * Tz / 3
action = (Tz * Lz * packet * Rz).trace() + kappa * (Tz * Tz).trace() / 2
assert action == -QQ(4) / 3 * z^3 + QQ(300) / 7 * z^2 - 5 * z
assert action.degree() == 3


def gradient(direction_function):
    result = zero_matrix(QQ, 3)
    for row in range(3):
        for column in range(3):
            unit = zero_matrix(QQ, 3)
            unit[row, column] = 1
            result[column, row] = direction_function(unit)
    return result


def action_eulers(a):
    t = a * T
    p = C * C + (C * t + t * C) / 2 + t * t / 3

    def e_c(h):
        dp = h * C + C * h + (h * t + t * h) / 2
        return (t * L * dp * R).trace()

    def e_t(h):
        dp = (C * h + h * C) / 2 + (h * t + t * h) / 3
        return (h * L * p * R).trace() + (t * L * dp * R).trace() + kappa * (h * t).trace()

    return gradient(e_c), gradient(e_t)


EC0, ET0 = action_eulers(QQ(0))
EC1, ET1 = action_eulers(QQ(1))
ED0 = EC0 - ET0
ED1 = EC1 - ET1
assert ED0 != zero_matrix(QQ, 3)
assert ED0 != ED1

tvec = vector(QQ, T.list())
target = vector(QQ, ED1.list())
bases = []
for row in range(9):
    for column in range(row, 9):
        b = zero_matrix(QQ, 9)
        b[row, column] = 1
        b[column, row] = 1
        bases.append(b)
fit = matrix(QQ, [list(b * tvec) for b in bases]).transpose()
assert len(bases) == 45
assert fit.rank() == 9
assert 45 - fit.rank() == 36
assert fit.augment(matrix(QQ, 9, 1, list(target))).rank() == fit.rank()

print("PASS independent Sage/QQ action-contact Legendre-owner replay")
