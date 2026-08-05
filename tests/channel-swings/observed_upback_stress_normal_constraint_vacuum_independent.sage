#!/usr/bin/env sage
"""Independent exact route for the observed stress/constraint/vacuum gate."""

Q = QQ
eta = diagonal_matrix(Q, [-1, 1, 1, 1])
pairs = [(i, j) for i in range(4) for j in range(i, 4)]


def sym_matrix(values):
    out = matrix(Q, 4, 4, 0)
    for value, (i, j) in zip(values, pairs):
        out[i, j] = value
        out[j, i] = value
    return out


def sym_vector(tensor):
    return vector(Q, [tensor[i, j] for i, j in pairs])


def trace_reversed_gram():
    out = matrix(Q, 10, 10, 0)
    for a in range(10):
        av = vector(Q, 10)
        av[a] = 1
        A = sym_matrix(av)
        for b in range(10):
            bv = vector(Q, 10)
            bv[b] = 1
            B = sym_matrix(bv)
            tr = sum(eta[i, j]*B[i, j] for i in range(4) for j in range(4))
            reverse_B = B - Q(1)/2*eta*tr
            raised = eta*reverse_B*eta
            out[a, b] = sum(A[i, j]*raised[i, j]
                            for i in range(4) for j in range(4))
    return out


def gauge_symbol(k_values):
    k = vector(Q, k_values)
    columns = []
    for index in range(4):
        ghost = vector(Q, 4)
        ghost[index] = 1
        h = matrix(Q, 4, 4, lambda i, j: k[i]*ghost[j] + k[j]*ghost[i])
        columns.append(sym_vector(h))
    return matrix(Q, 10, 4, lambda i, j: columns[j][i])


def harmonic_symbol(k_values):
    k = vector(Q, k_values)
    raised = eta*k
    out = matrix(Q, 4, 10, 0)
    for column in range(10):
        basis = vector(Q, 10)
        basis[column] = 1
        h = sym_matrix(basis)
        tr = sum(eta[i, j]*h[i, j] for i in range(4) for j in range(4))
        for nu in range(4):
            out[nu, column] = (sum(raised[mu]*h[mu, nu] for mu in range(4))
                               - Q(1)/2*k[nu]*tr)
    return out


def einstein_symbol(k_values):
    k = vector(Q, k_values)
    raised = eta*k
    k2 = k*raised
    columns = []
    for column in range(10):
        basis = vector(Q, 10)
        basis[column] = 1
        h = sym_matrix(basis)
        tr = sum(eta[i, j]*h[i, j] for i in range(4) for j in range(4))
        ric = matrix(Q, 4, 4, 0)
        for mu in range(4):
            for nu in range(4):
                kh_nu = sum(raised[rho]*h[rho, nu] for rho in range(4))
                kh_mu = sum(raised[rho]*h[rho, mu] for rho in range(4))
                ric[mu, nu] = Q(1)/2*(k[mu]*kh_nu + k[nu]*kh_mu
                                      - k2*h[mu, nu] - k[mu]*k[nu]*tr)
        scalar = sum(eta[i, j]*ric[i, j] for i in range(4) for j in range(4))
        columns.append(sym_vector(ric - Q(1)/2*eta*scalar))
    return matrix(Q, 10, 10, lambda i, j: columns[j][i])


# Independent finite common-action radial-transgression calculation.
A1 = matrix(Q, [[1, 2, 0], [2, -1, 1], [0, 1, 3]])
A2 = matrix(Q, [[0, 1, -2], [1, 2, 0], [-2, 0, 1]])
q = vector(Q, [2, -3, 5])
metric_euler = vector(Q, [Q(1)/2*(q*A1*q), Q(1)/2*(q*A2*q)])
V = matrix(Q, 2, 3, lambda i, j: (q*A1 if i == 0 else q*A2)[j])
assert V*q == 2*metric_euler
assert Q(1)/2*(V*q) == metric_euler

W = trace_reversed_gram()
x = polygen(Q, 'x')
assert W.rank() == 10
assert W.charpoly('x') == (x - 2)^3*(x - 1)^3*(x + 1)*(x + 2)^3

k = (1, 1, 0, 0)
G = einstein_symbol(k)
J = block_matrix(Q, [[zero_matrix(Q, 10), G.transpose()*W],
                     [W*G, Q(2)*W]])
D = block_matrix(Q, [[gauge_symbol(k)], [zero_matrix(Q, 10, 4)]])
H = block_matrix(Q, [[harmonic_symbol(k), zero_matrix(Q, 4, 10)]])
stacked = block_matrix(Q, [[J], [H]])
assert J.rank() == 10 and J.right_nullity() == 10
assert stacked.rank() == 14 and stacked.right_nullity() == 6
assert H*D == 0 and D.rank() == 4

plus_h = matrix(Q, 4, 4, 0)
plus_h[2, 2] = 1
plus_h[3, 3] = -1
cross_h = matrix(Q, 4, 4, 0)
cross_h[2, 3] = cross_h[3, 2] = 1
plus = vector(Q, list(sym_vector(plus_h)) + [0]*10)
cross = vector(Q, list(sym_vector(cross_h)) + [0]*10)
assert stacked*plus == 0 and stacked*cross == 0
span = block_matrix(Q, [[D, matrix(Q, 20, 1, plus), matrix(Q, 20, 1, cross)]])
assert span.rank() == 6

z, kappa = PolynomialRing(Q, names=('z', 'kappa')).gens()
tt = matrix(Q['z,kappa'].fraction_field(), [[0, z], [z, kappa]])
assert tt.det() == -z^2
assert tt.inverse()[0, 0] == -kappa/z^2

# The unshifted quadratic vacuum is unique but indefinite; an independent
# source is transmitted through the inverse Gram rather than screened.
gain = Q(3)/2
assert (gain*W).rank() == 10
source = vector(Q, [1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
v1 = -(gain*W).inverse()*source
v2 = -(gain*W).inverse()*(2*source)
assert v2 == 2*v1 and v1 != 0

print("PASS independent Sage/QQ: action radial stress, (6,4) trace reversal, constrained 10->6->2 plus/cross quotient, double-pole response, and shift tracking")
print("RADIAL_STRESS=EXACT NULL_QUOTIENT=2 PROPAGATOR_POLE_ORDER=2 VACUUM_SHIFT=TRACKED")
