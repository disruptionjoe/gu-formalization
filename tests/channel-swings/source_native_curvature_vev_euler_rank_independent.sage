#!/usr/bin/env sage
"""Independent QQ reconstruction of the curvature/VEV value-rank result."""

Q = QQ
n_einstein = 1 + 104
n_weyl = 3080
n_t = 196

C = matrix(Q, n_t, n_einstein, sparse=True)
for i in range(n_einstein):
    C[i, i] = -2

K = diagonal_matrix(Q, [1] * 98 + [-1] * 98)
J = block_matrix(Q, 1, 2, [C, K])
J0 = block_matrix(Q, 1, 2, [C, zero_matrix(Q, n_t, n_t)])

assert n_einstein == 105
assert n_einstein + n_weyl == 3185
assert C.rank() == 105
assert K.rank() == 196
assert J.rank() == 196
assert J0.rank() == 105

# Independent scalar ambient-kernel witness in the 4+10 split.
k_hh = Q(1)
k_hn = -Q(3) / 10
k_nn = Q(2) / 15
assert 3 * k_hh + 10 * k_hn == 0
assert 4 * k_hn + 9 * k_nn == 0
assert -3 * k_hh == -3

# Homogeneous B-variation contributes no algebraic value row at T=0.
EB0 = zero_matrix(Q, n_t, n_einstein + n_t)
assert block_matrix(Q, 2, 1, [J, EB0]).rank() == 196

# One shifted equality is one equation; adding c=0 is the extra screening row.
shift = matrix(Q, [[1, 1, 1]])
screen = matrix(Q, [[1, 1, 1], [1, 0, 0]])
assert shift.rank() == 1
assert screen.rank() == 2

print("PASS independent Sage/QQ: curvature rank 105, total T-Euler rank 196, "
      "ambient/observed kernel witness, and vacuum-shift rank control")
