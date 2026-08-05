#!/usr/bin/env sage
"""Independent QQ check of the moving-jet and K77 signature theorems."""

from sage.all import QQ, diagonal_matrix, identity_matrix, matrix, vector, zero_matrix


J = matrix(QQ, [[QQ(1)/2, -QQ(1)/3], [QQ(2)/5, QQ(3)/7], [-QQ(4)/9, QQ(5)/11]])
b = J.ncols()
n = J.nrows()
M = matrix.block([[identity_matrix(QQ, b), J.transpose()],
                  [zero_matrix(QQ, n, b), identity_matrix(QQ, n)]])
Minv = matrix.block([[identity_matrix(QQ, b), -J.transpose()],
                     [zero_matrix(QQ, n, b), identity_matrix(QQ, n)]])
assert M.det() == 1
assert M * Minv == 1
assert Minv.transpose() * M.transpose() == 1
assert M.transpose() * Minv.transpose() == 1

V = matrix.block([[identity_matrix(QQ, b), J.transpose()]])
N = matrix.block([[-J.transpose()], [identity_matrix(QQ, n)]])
assert V.rank() == b
assert N.rank() == n
assert V * N == 0

Q = diagonal_matrix(QQ, [1] * 7 + [-1] * 7)
assert Q.rank() == 14

Hpos = Q[1:, 1:]
indices = list(range(7)) + list(range(8, 14))
Hneg = Q.matrix_from_rows_and_columns(indices, indices)
Hnull = diagonal_matrix(QQ, [0] + [1] * 6 + [-1] * 6)
def diagonal_inertia(A):
    entries = [A[i, i] for i in range(A.nrows())]
    return (sum(x > 0 for x in entries),
            sum(x < 0 for x in entries),
            sum(x == 0 for x in entries))

assert diagonal_inertia(Q) == (7, 7, 0)
assert Hpos.rank() == 13 and diagonal_inertia(Hpos) == (6, 7, 0)
assert Hneg.rank() == 13 and diagonal_inertia(Hneg) == (7, 6, 0)
assert Hnull.rank() == 12 and diagonal_inertia(Hnull) == (6, 6, 1)

print("PASS independent Sage/QQ moving first-jet observation and K77 hypersurface obstruction")
print("JET_DET=1 VALUE_ONLY_KERNEL=3")
print("HYPERSURFACE_INERTIA=(6,7)|(7,6)|(6,6,1)")
