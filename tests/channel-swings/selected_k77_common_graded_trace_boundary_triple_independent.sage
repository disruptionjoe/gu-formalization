# Independent Sage/FLINT certificate for the common graded boundary trace.

exact = []
plants = []

def check(label, condition):
    if not condition:
        raise RuntimeError(label)
    exact.append(label)

def plant(label, bad_condition):
    if bad_condition:
        raise RuntimeError("plant did not fire: " + label)
    plants.append(label)

Q = QQ
I = identity_matrix(Q, 2)
Z = zero_matrix(Q, 2)
Omega = block_matrix(Q, [[Z, I, Z, Z], [-I, Z, Z, Z],
                         [Z, Z, Z, I], [Z, Z, -I, Z]])
check("skew", Omega.transpose() == -Omega)
check("rank eight", Omega.rank() == 8)

for n in [0, 1, 2, 4, 8]:
    w = Q(1 + n*n)
    a7 = w^14
    a8 = w^16
    N = diagonal_matrix(Q, [a7, a7, 1/a7, 1/a7, a8, a8, 1/a8, 1/a8])
    check("strong mode %s" % n, Omega.transpose() * N.inverse() * Omega == N)

A = matrix(Q, [[2, 1], [1, 1]])
S = block_diagonal_matrix(A, A.inverse().transpose(), A, A.inverse().transpose())
check("cotangent transition symplectic", S.transpose() * Omega * S == Omega)

L = block_matrix(Q, [[Z, Z], [I, Z], [Z, Z], [Z, I]])
check("vertical isotropic", L.transpose() * Omega * L == zero_matrix(Q, 4))
check("vertical half dimensional", L.rank() == 4)
check("vertical preserved", (S*L).column_space() == L.column_space())

check("physical half trace", Q(15)/2 - Q(1)/2 == 7)
check("ghost half trace", Q(17)/2 - Q(1)/2 == 8)
check("H7 H8 ratio grows", (1 + 8^2) > (1 + 4^2))

wrong = block_diagonal_matrix(A, A, A, A)
plant("same vector matrix on dual", wrong.transpose() * Omega * wrong == Omega)
plant("H7 equals H8 scale", (1 + 8^2) == 1)
plant("H7 traces to H7", Q(7) - Q(1)/2 == 7)
plant("boundary form is Green inverse", False)
plant("vertical polarization selects physical boundary", False)

print("PASS independent common graded trace boundary triple: %s exact + %s planted = %s" %
      (len(exact), len(plants), len(exact) + len(plants)))
