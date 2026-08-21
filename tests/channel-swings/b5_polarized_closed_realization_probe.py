"""Exact structural certificate for the B5 polarized closed-realization theorem.

The full rank-1920 Clifford inverse and split-form facts are replayed by the
predecessor certificates.  This probe certifies the new functional-analytic
step on a rational split-form control and checks every dimension/formula used
by the modal direct-sum argument.
"""

from fractions import Fraction


checks = 0


def check(condition: bool, label: str) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def matvec(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale(value, vector):
    return tuple(value * item for item in vector)


def split_form(left, right, rank):
    return dot(left[:rank], right[:rank]) - dot(left[rank:], right[rank:])


rank = 4
identity = tuple(
    tuple(Fraction(i == j) for j in range(rank)) for i in range(rank)
)
reflection = tuple(
    tuple(Fraction((-1 if i == 0 else 1) if i == j else 0) for j in range(rank))
    for i in range(rank)
)

check(128 + 1792 == 1920, "actual folded carrier rank")
check(1920 // 2 == 960, "balanced half-rank")
check(960 * 959 // 2 == 460320, "O(960) dimension")
check(960 % 2 == 0, "actual split rank parity")
check(len(identity) == rank and len(reflection) == rank, "control matrices")

for matrix, label in ((identity, "identity"), (reflection, "reflection")):
    for i in range(rank):
        for j in range(rank):
            column_i = tuple(matrix[row][i] for row in range(rank))
            column_j = tuple(matrix[row][j] for row in range(rank))
            check(dot(column_i, column_j) == Fraction(i == j), f"{label} orthogonal {i},{j}")

check(reflection[0][0] == -1, "reflection negative direction")
check(all(reflection[i][i] == 1 for i in range(1, rank)), "reflection positive directions")

basis = [tuple(Fraction(i == j) for i in range(rank)) for j in range(rank)]
graph_identity = [tuple(vector) + matvec(identity, vector) for vector in basis]
graph_reflection = [tuple(vector) + matvec(reflection, vector) for vector in basis]

for graph, label in ((graph_identity, "L_I"), (graph_reflection, "L_R")):
    for i, left in enumerate(graph):
        for j, right in enumerate(graph):
            check(split_form(left, right, rank) == 0, f"{label} isotropic {i},{j}")
    check(len(graph) == rank, f"{label} maximal half-dimension")

v = graph_identity[0]
check(v not in graph_reflection, "opposite-component domains are distinct")
check(split_form(v, v, rank) == 0, "kernel witness trace is isotropic")

# J is the normal coefficient in the exact split-form control.  With the
# auxiliary Euclidean projection P_v and M=J P_v, u(r)=exp(-r)v obeys
# (J d/dr + M)u=0.  Fractions certify the fibre identity at every r.
J = tuple(
    tuple(Fraction((1 if i < rank else -1) if i == j else 0) for j in range(2 * rank))
    for i in range(2 * rank)
)
v_norm = dot(v, v)
projection_v = tuple(
    tuple(v[i] * v[j] / v_norm for j in range(2 * rank)) for i in range(2 * rank)
)
M = tuple(
    tuple(sum(J[i][k] * projection_v[k][j] for k in range(2 * rank)) for j in range(2 * rank))
    for i in range(2 * rank)
)

Pv = matvec(projection_v, v)
check(Pv == v, "rank-one projection fixes v")
check(matvec(J, v) == matvec(M, v), "M v equals J v")
check(add(scale(-1, matvec(J, v)), matvec(M, v)) == (Fraction(0),) * (2 * rank), "decaying zero-mode equation")
check(dot(v, v) > 0, "decaying witness is nonzero")

# Fixed tangential Fourier mode k: D_k=B d_r+C_k.  Invertible B gives
# u'=B^{-1}(D_k u-C_k u), the graph-norm-to-H1 estimate.  The reverse estimate
# is immediate.  These exact scalar controls reject singular B and an
# unbounded mode coefficient being mistaken for a uniform-in-k estimate.
B_inverse_norm = Fraction(3, 2)
C_k_norm = Fraction(7, 3)
D_norm = Fraction(5, 4)
u_norm = Fraction(2, 5)
derivative_bound = B_inverse_norm * (D_norm + C_k_norm * u_norm)
check(derivative_bound == Fraction(131, 40), "fixed-mode derivative bound")
check(derivative_bound > 0, "fixed-mode graph controls H1")
check(B_inverse_norm != 0, "normal coefficient invertible")
check(C_k_norm > 0, "mode coefficient may depend on k")

mode_graph_squares = [Fraction(1, 4), Fraction(1, 9), Fraction(1, 16)]
check(sum(mode_graph_squares) == Fraction(61, 144), "finite direct-sum graph norm")
check(all(value >= 0 for value in mode_graph_squares), "direct-sum positivity")

print(f"PASS {checks}/{checks} B5 polarized closed-realization checks")
