# Independent Sage/QQ reconstruction of the pre-Shiab Gauss defect action.
#
# This file deliberately does not import the SymPy certificate.  It rebuilds
# the ambient-kernel witness, trace-reversed pairing, observed Einstein symbol,
# gauge tangent and repaired Hessian over QQ.

Q = QQ
eta = diagonal_matrix(Q, [-1, 1, 1, 1])
pairs = [(i, j) for i in range(4) for j in range(i, 4)]


def sym_matrix(vector):
    out = matrix(Q, 4, 4, 0)
    for value, (i, j) in zip(vector, pairs):
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
            tr = sum(eta[i, j] * B[i, j] for i in range(4) for j in range(4))
            reverse_B = B - Q(1)/2 * eta * tr
            raised = eta * reverse_B * eta
            out[a, b] = sum(A[i, j] * raised[i, j]
                            for i in range(4) for j in range(4))
    return out


def gauge_symbol(k_values):
    k = vector(Q, k_values)
    columns = []
    for ghost_index in range(4):
        ghost = vector(Q, 4)
        ghost[ghost_index] = 1
        H = matrix(Q, 4, 4, lambda i, j:
                   k[i] * ghost[j] + k[j] * ghost[i])
        columns.append(sym_vector(H))
    return matrix(Q, 10, 4, lambda i, j: columns[j][i])


def bianchi_symbol(k_values):
    k = vector(Q, k_values)
    raised = eta * k
    out = matrix(Q, 4, 10, 0)
    for column in range(10):
        basis = vector(Q, 10)
        basis[column] = 1
        tensor = sym_matrix(basis)
        for nu in range(4):
            out[nu, column] = sum(raised[mu] * tensor[mu, nu]
                                  for mu in range(4))
    return out


def einstein_symbol(k_values):
    k = vector(Q, k_values)
    raised = eta * k
    k2 = k * raised
    columns = []
    for column in range(10):
        basis = vector(Q, 10)
        basis[column] = 1
        h = sym_matrix(basis)
        tr = sum(eta[i, j] * h[i, j] for i in range(4) for j in range(4))
        Ric = matrix(Q, 4, 4, 0)
        for mu in range(4):
            for nu in range(4):
                kh_nu = sum(raised[rho] * h[rho, nu] for rho in range(4))
                kh_mu = sum(raised[rho] * h[rho, mu] for rho in range(4))
                Ric[mu, nu] = Q(1)/2 * (
                    k[mu] * kh_nu + k[nu] * kh_mu
                    - k2 * h[mu, nu] - k[mu] * k[nu] * tr
                )
        scalar = sum(eta[i, j] * Ric[i, j]
                     for i in range(4) for j in range(4))
        G = Ric - Q(1)/2 * eta * scalar
        columns.append(sym_vector(G))
    return matrix(Q, 10, 10, lambda i, j: columns[j][i])


def operator_basis(k_values):
    k = vector(Q, k_values)
    raised = eta * k
    k2 = k * raised
    operators = []
    for term_index in range(5):
        columns = []
        for column in range(10):
            basis = vector(Q, 10)
            basis[column] = 1
            h = sym_matrix(basis)
            tr = sum(eta[i, j] * h[i, j] for i in range(4) for j in range(4))
            khk = sum(raised[rho] * raised[sigma] * h[rho, sigma]
                      for rho in range(4) for sigma in range(4))
            output = matrix(Q, 4, 4, 0)
            for mu in range(4):
                for nu in range(4):
                    kh_nu = sum(raised[rho] * h[rho, nu] for rho in range(4))
                    kh_mu = sum(raised[rho] * h[rho, mu] for rho in range(4))
                    terms = [
                        k2 * h[mu, nu],
                        k[mu] * kh_nu + k[nu] * kh_mu,
                        k[mu] * k[nu] * tr,
                        eta[mu, nu] * khk,
                        eta[mu, nu] * k2 * tr,
                    ]
                    output[mu, nu] = terms[term_index]
            columns.append(sym_vector(output))
        operators.append(matrix(Q, 10, 10, lambda i, j: columns[j][i]))
    return operators


def repaired(k_values, gain):
    G = einstein_symbol(k_values)
    W = trace_reversed_gram()
    J = block_matrix(Q, [[zero_matrix(Q, 10), G.transpose() * W],
                         [W * G, gain * W]])
    D = block_matrix(Q, [[gauge_symbol(k_values)], [zero_matrix(Q, 10, 4)]])
    return J, D


# Independent ambient Ricci-flat / observed-curvature witness.
g_h = diagonal_matrix(Q, [-1, 1, 1, 1] + [0] * 10)
g_n = diagonal_matrix(Q, [0] * 4 + [1] * 6 + [-1] * 4)
g14 = g_h + g_n
g14_inv = g14.inverse()


def kn(A, B, a, b, c, d):
    return (A[a, c] * B[b, d] + A[b, d] * B[a, c]
            - A[a, d] * B[b, c] - A[b, c] * B[a, d])


def kernel_R(a, b, c, d):
    return (Q(1)/2 * kn(g_h, g_h, a, b, c, d)
            - Q(3)/10 * kn(g_h, g_n, a, b, c, d)
            + Q(1)/15 * kn(g_n, g_n, a, b, c, d))


Ric14 = matrix(Q, 14, 14, lambda b, d: sum(
    g14_inv[a, c] * kernel_R(a, b, c, d)
    for a in range(14) for c in range(14)))
assert Ric14 == zero_matrix(Q, 14)

g4 = g_h[:4, :4]
g4_inv = g4.inverse()
Ric4 = matrix(Q, 4, 4, lambda b, d: sum(
    g4_inv[a, c] * kernel_R(a, b, c, d)
    for a in range(4) for c in range(4)))
scalar4 = sum(g4_inv[i, j] * Ric4[i, j]
              for i in range(4) for j in range(4))
G4 = Ric4 - Q(1)/2 * scalar4 * g4
assert G4 == -3 * g4

# Five-coefficient uniqueness.
constraints = []
for k_values in [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 1, 0), (2, 1, 0, 0)]:
    ops = operator_basis(k_values)
    d0 = gauge_symbol(k_values)
    C = bianchi_symbol(k_values)
    constraints.extend([matrix(Q, 40, 5, lambda i, j: (ops[j] * d0).list()[i]),
                        matrix(Q, 40, 5, lambda i, j: (C * ops[j]).list()[i])])
A = block_matrix(Q, [[item] for item in constraints])
assert A.rank() == 4
assert A.right_kernel().basis_matrix().row_space() == matrix(Q, [[-1, 1, -1, -1, 1]]).row_space()

W = trace_reversed_gram()
assert W.rank() == 10
x = polygen(Q, 'x')
print("TRACE_REVERSED_CHARPOLY", W.charpoly('x').factor())
assert W.charpoly('x') == (x - 2)^3 * (x - 1)^3 * (x + 1) * (x + 2)^3

for k_values in [(1, 0, 0, 0), (0, 1, 0, 0)]:
    G = einstein_symbol(k_values)
    d0 = gauge_symbol(k_values)
    C = bianchi_symbol(k_values)
    J, D = repaired(k_values, Q(2))
    assert G.rank() == 6
    assert d0.rank() == 4
    assert G * d0 == zero_matrix(Q, 10, 4)
    assert C * G == zero_matrix(Q, 4, 10)
    assert J.is_symmetric()
    assert J.rank() == 16
    assert J * D == zero_matrix(Q, 20, 4)
    assert D.transpose() * J == zero_matrix(Q, 4, 20)
    assert J.right_kernel().basis_matrix().row_space() == D.transpose().row_space()
    assert J.column_space() == D.transpose().right_kernel()

J0, D0 = repaired((1, 0, 0, 0), Q(0))
assert J0.rank() == 12
assert J0.right_nullity() == 8 > D0.rank()

Gnull = einstein_symbol((1, 1, 0, 0))
Jnull, Dnull = repaired((1, 1, 0, 0), Q(2))
assert Gnull.rank() == 4
assert Jnull.rank() == 10
assert Jnull.right_nullity() - Dnull.rank() == 6
assert Jnull * Dnull == zero_matrix(Q, 20, 4)

print("PASS independent Sage/QQ: current-I1B kernel witness, unique Einstein line, trace-reversed (6,4) pairing, non-null exact 4-20-20-4 BV symbol complex, zero-gain and null controls")
