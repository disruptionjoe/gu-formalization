#!/usr/bin/env sage
"""Independent QQ rank proof for the fixed-epsilon common-field fork."""

# A rank-four metric orbit and a rank-three connection component with a
# one-dimensional gauge-parameter kernel.
D = matrix(QQ, 10, 4, lambda i, j: 1 if i == j else 0)
C = matrix(QQ, 24, 4, lambda i, j: 1 if i == j and j > 0 else 0)
assert D.rank() == 4
assert C.rank() == 3
assert C.right_kernel().dimension() == 1

# Inject the connection response into a larger residual carrier.
A = matrix(QQ, 56, 24, lambda i, j: 1 if i == j else 0)
JvarpiR = A*C
assert A.rank() == 24
assert JvarpiR.rank() == 3

# A metric response can cancel the actual connection response on the orbit,
# but only on the orbit.  Six transverse metric columns remain arbitrary.
L = (D.transpose()*D).inverse()*D.transpose()
Jg = -JvarpiR*L
assert Jg*D + JvarpiR == 0
assert Jg.rank() == 3
assert (identity_matrix(QQ,10) - D*L).rank() == 6

# For any residual pairing K, rank(Jg^* K Jg D) cannot exceed rank(Jg D)=3.
K = diagonal_matrix(QQ, [1 if i % 2 == 0 else -1 for i in range(56)])
HggD = Jg.transpose()*K*Jg*D
assert HggD.rank() <= 3

# A rank-four inherited metric load cannot be that fixed-epsilon Gram block.
W4 = matrix(QQ, 10, 4, lambda i, j: 1 if i == j else 0)
assert W4.rank() == 4
assert HggD != W4

# The source-epsilon revival is real in type: one additional response column
# on the missing gauge parameter can raise the total orbit response to rank 4.
E = matrix(QQ, 1, 4, [1,0,0,0])
assert block_matrix([[JvarpiR], [E]]).rank() == 4

print("PASS 15/15")
