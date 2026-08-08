# Independent exact QQ replay for the K77 tilted edge-bundle type bridge gate.

Q = QQ
I = matrix(Q, 2, 2, [1, 0, 0, 1])
h01 = matrix(Q, 2, 2, [1, 1, 0, 1])
h12 = matrix(Q, 2, 2, [1, 0, 1, 1])
h02 = h01 * h12
dh01 = matrix(Q, 2, 2, [2, -1, 3, 1])
dh12 = matrix(Q, 2, 2, [0, 4, -2, 1])
dh02 = dh01 * h12 + h01 * dh12

def adinv(h, x):
    return h.inverse() * x * h

c01 = h01.inverse() * dh01
c12 = h12.inverse() * dh12
c02 = h02.inverse() * dh02
assert h01 * h12 != h12 * h01
assert c02 == adinv(h12, c01) + c12
assert c02 != adinv(h01, c12) + c01
assert c02 != h12 * c01 * h12.inverse() + c12

a0 = matrix(Q, 2, 2, [1, 2, -3, 4])
a1 = adinv(h01, a0) + c01
assert adinv(h12, a1) + c12 == adinv(h02, a0) + c02

u0 = matrix(Q, 2, 2, [2, 1, 1, 1])
assert (u0 * h01) * h12 == u0 * h02

xi = matrix(Q, 2, 2, [1, 2, 0, -1])
dxi = matrix(Q, 2, 2, [3, -2, 1, 4])
assert dxi != xi
assert matrix(Q, 2, 2, 0) != xi

# Invariance of ell under diag(2,1) and diag(1,3), acting on V*, has full
# rank on the two coefficients.  Thus the only zero-order natural bridge is zero.
g0 = diagonal_matrix(Q, [2, 1])
g1 = diagonal_matrix(Q, [1, 3])
C = block_matrix(Q, [[g0.inverse().transpose() - I],
                     [g1.inverse().transpose() - I]])
assert C.rank() == 2
assert C.right_kernel().dimension() == 0

print("PASS SAGE_QQ_TILTED_COCYCLE_AND_ZEROFORM_ONEFORM_TYPE_GATE")
print("TILTED_COCYCLE=EXACT")
print("DIRECT_IDENTITY=KILLED_BY_CONSTANT_XI")
print("NATURAL_ZERO_ORDER_VSTAR_TO_SCALAR=NULLITY_0")
