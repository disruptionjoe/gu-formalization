"""Independent Sage/QQ reconstruction of the BV-TT and FLRW gate."""

from sage.all import QQ, PolynomialRing, FractionField, Matrix, diagonal_matrix, identity_matrix, block_diagonal_matrix


eta = diagonal_matrix(QQ, [-1, 1, 1, 1])
pairs = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]


def symmetric_basis(column):
    mu, nu = pairs[column]
    h = Matrix(QQ, 4, 4, 0)
    h[mu, nu] = 1
    h[nu, mu] = 1
    return h


def lc_symbol(k):
    out = Matrix(QQ, 64, 10, 0)
    for column in range(10):
        h = symmetric_basis(column)
        for rho in range(4):
            for mu in range(4):
                for nu in range(4):
                    row = (rho * 4 + mu) * 4 + nu
                    out[row, column] = QQ(1) / 2 * sum(
                        eta[rho, sigma] * (
                            k[mu] * h[nu, sigma]
                            + k[nu] * h[mu, sigma]
                            - k[sigma] * h[mu, nu]
                        )
                        for sigma in range(4)
                    )
    return out


assert lc_symbol((1, 0, 0, 0)).rank() == 10
assert lc_symbol((0, 1, 0, 0)).rank() == 10
assert lc_symbol((1, 0, 0, 1)).rank() == 10

epsilon = Matrix(QQ, [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
adjoint = block_diagonal_matrix([epsilon.transpose().tensor_product(epsilon.inverse()) for _ in range(4)])
assert (adjoint * lc_symbol((1, 0, 0, 1))).rank() == 10

k = (1, 0, 0, -1)
diffeo = Matrix(QQ, 10, 4, 0)
for column in range(4):
    for row, (mu, nu) in enumerate(pairs):
        diffeo[row, column] = (
            (k[mu] if nu == column else 0)
            + (k[nu] if mu == column else 0)
        )

plus = Matrix(QQ, 10, 1, 0)
plus[pairs.index((1, 1)), 0] = 1
plus[pairs.index((2, 2)), 0] = -1
cross = Matrix(QQ, 10, 1, 0)
cross[pairs.index((1, 2)), 0] = 1
tt = plus.augment(cross)
assert diffeo.rank() == 4
assert tt.rank() == 2
assert diffeo.augment(tt).rank() == 6

PR = PolynomialRing(QQ, names=("alpha", "b", "a", "beta", "kappa", "rho"))
alpha, b, a, beta, kappa, rho = PR.gens()
F = FractionField(PR)
alpha, b, a, beta, kappa, rho = map(F, (alpha, b, a, beta, kappa, rho))

K = Matrix(F, [[alpha, 1], [1, 0]])
mass = Matrix(F, [[0, 0], [0, b]])
L = K.inverse() * mass
m2 = alpha * b
parity = identity_matrix(F, 2) + 2 * L / m2
majorant = K * parity
massless = Matrix(F, [[1], [0]])
partner = Matrix(F, [[1], [-alpha]])

assert L * massless == Matrix(F, 2, 1, 0)
assert L * partner == -m2 * partner
assert (massless.transpose() * K * massless)[0, 0] == alpha
assert (partner.transpose() * K * partner)[0, 0] == -alpha
assert parity * parity == identity_matrix(F, 2)
assert parity * L == L * parity
assert parity.transpose() * K == K * parity
assert majorant[0, 0] == alpha
assert majorant.det() == 1

R4 = 2 * rho / a
t = -2 * beta * rho / (a * kappa)
E_t = beta * R4 + kappa * t
trace_constant = -(a + beta * t) * R4 - kappa * t * t + 2 * rho
assert E_t == 0
assert trace_constant == 0
assert R4.derivative(rho) == 2 / a
assert t.derivative(rho) == -2 * beta / (a * kappa)

# With t=-beta*R/kappa, the complete trace is
# -a R-3 beta^2 box(R)/kappa+2 rho=0.  Constant box(R)=0 returns R=2 rho/a.
assert R4 == 2 * rho / a
assert not R4.numerator().divides(PR(beta))

print("SAGE_INDEPENDENT_BV_TT_FLRW_PASS")
print("LEVI_CIVITA_ORBIT_RANKS=10,10,10")
print("MASSIVE_PARTNER_EVEN_BV_TT_CLASSES=2")
print("SPECTRAL_PARITY_SQUARE=1__MAJORANT_DET=1")
print("R4=2*rho/a")
print("t=-2*beta*rho/(a*kappa)")
