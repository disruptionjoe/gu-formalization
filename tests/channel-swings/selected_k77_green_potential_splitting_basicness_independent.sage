#!/usr/bin/env sage
"""Independent Sage check of cotangent splitting naturality and K77 firing."""

from sage.all import (
    QQ,
    block_diagonal_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    vector,
    zero_matrix,
)


# A nonlinear two-normal/three-field splitting over a polynomial ring.
ring = QQ["n0,n1,y0,y1,y2,pn0,pn1,py0,py1,py2"]
n0, n1, y0, y1, y2, pn0, pn1, py0, py1, py2 = ring.gens()
normal = vector(ring, [n0, n1])
field = vector(ring, [y0, y1, y2])
pn = vector(ring, [pn0, pn1])
py = vector(ring, [py0, py1, py2])
frame = matrix(ring, [[1, n0, n0*n1], [0, 1, n1], [0, 0, 1]])
qnew = vector(ring, list(normal) + list(field))
qold = vector(ring, list(normal) + list(frame * field))


def jacobian(expressions, variables):
    return matrix(ring, len(expressions), len(variables),
                  lambda i, j: expressions[i].derivative(variables[j]))


tangent = jacobian(qold, qnew)
pv = frame.transpose().inverse() * py
dframe0 = matrix(ring, 3, 3, lambda i, j: frame[i, j].derivative(n0))
dframe1 = matrix(ring, 3, 3, lambda i, j: frame[i, j].derivative(n1))
shift = vector(ring, [(pv * dframe0 * field), (pv * dframe1 * field)])
pold = vector(ring, list(pn - shift) + list(pv))
pnew = vector(ring, list(pn) + list(py))
assert tangent.det() == 1
assert tangent.transpose() * pold == pnew

znew = vector(ring, list(qnew) + list(pnew))
zold = vector(ring, list(qold) + list(pold))
phase = jacobian(zold, znew)
i5 = identity_matrix(ring, 5)
omega5 = zero_matrix(ring, 10)
omega5[:5, 5:] = -i5
omega5[5:, :5] = i5
assert phase.transpose() * omega5 * phase == omega5

partial_pold = vector(ring, list(pn) + list(pv))
partial_phase = jacobian(vector(ring, list(qold) + list(partial_pold)), znew)
assert tangent.transpose() * partial_pold != pnew
assert partial_phase.transpose() * omega5 * partial_phase != omega5


# Independent reconstruction of the ten K77 infinitesimal splitting columns.
g4 = diagonal_matrix(QQ, [1, -1, -1, -1])
g4i = g4.inverse()
slots = [(i, j) for i in range(4) for j in range(i, 4)]
basis = []
for i, j in slots:
    value = zero_matrix(QQ, 4)
    value[i, j] = 1
    value[j, i] = 1
    basis.append(value)


def dewitt(inverse):
    return matrix(QQ, 10, 10, lambda i, j:
        (inverse * basis[i] * inverse * basis[j]).trace()
        - QQ(1)/2 * (inverse * basis[i]).trace() * (inverse * basis[j]).trace())


def d_dewitt(h):
    di = -g4i * h * g4i
    return matrix(QQ, 10, 10, lambda i, j:
        (di * basis[i] * g4i * basis[j]).trace()
        + (g4i * basis[i] * di * basis[j]).trace()
        - QQ(1)/2 * (
            (di * basis[i]).trace() * (g4i * basis[j]).trace()
            + (g4i * basis[i]).trace() * (di * basis[j]).trace()))


gv = dewitt(g4i)
g = block_diagonal_matrix([g4, gv])
dg = [block_diagonal_matrix([h, d_dewitt(h)]) for h in basis]
a = [-QQ(1)/2 * g.inverse() * value for value in dg]
k77_field = vector(QQ, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
k77_momentum = vector(QQ, [47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107])
shifts = vector(QQ, [k77_momentum * value * k77_field for value in a])
assert all(value != 0 for value in shifts)

cross = matrix(QQ, 14, 10, lambda i, j: (a[j] * k77_field)[i])
transition = block_diagonal_matrix([identity_matrix(QQ, 10), identity_matrix(QQ, 14)])
transition[10:, :10] = cross
assert transition.det() == 1 and transition.rank() == 24

i24 = identity_matrix(QQ, 24)
omega24 = zero_matrix(QQ, 48)
omega24[:24, 24:] = -i24
omega24[24:, :24] = i24
cotangent = block_diagonal_matrix([transition, transition.transpose().inverse()])
partial = block_diagonal_matrix([transition, i24])
assert cotangent.transpose() * omega24 * cotangent == omega24
assert partial.transpose() * omega24 * partial != omega24

print("PASS independent Sage/QQ Green-potential splitting/basicness gate")
print("NONLINEAR_COTANGENT_LIFT=EXACT PARTIAL_POTENTIAL_DEFECT=LIVE")
print("K77_NORMAL_MOMENTUM_SHIFTS=10_OF_10_NONZERO SYMPLECTIC_TRANSPORT=EXACT")
