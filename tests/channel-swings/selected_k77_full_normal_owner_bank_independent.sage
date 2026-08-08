#!/usr/bin/env sage
"""Independent Sage/QQ check of the ten-normal K77 geometry and split fence."""

from sage.all import QQ, block_diagonal_matrix, diagonal_matrix, matrix, vector, zero_matrix


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


def inertia_symmetric(value):
    work = matrix(QQ, value)
    positive = negative = null = 0
    while work.nrows():
        size = work.nrows()
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.matrix_from_rows_and_columns(order, order)
            pivot = work[0, 0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            if size == 1:
                break
            column = work[1:, 0]
            work = work[1:, 1:] - column * column.transpose() / pivot
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j] != 0), None)
        if off is None:
            null += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.matrix_from_rows_and_columns(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = work[2:, 2:] - coupling.transpose() * block.inverse() * coupling
    return positive, negative, null


gv = dewitt(g4i)
G = block_diagonal_matrix([g4, gv])
dG = [block_diagonal_matrix([h, d_dewitt(h)]) for h in basis]
assert len(slots) == 10 and sum(i == j for i, j in slots) == 4
assert gv.det() == 64
assert inertia_symmetric(gv) == (6, 4, 0)
assert inertia_symmetric(G) == (7, 7, 0)

# Rebuild the flattened bank columnwise to avoid relying on storage order.
flat = matrix(QQ, 14 * 14, 10)
for column, value in enumerate(dG):
    for i in range(14):
        for j in range(14):
            flat[14 * i + j, column] = value[i, j]
assert flat.rank() == 10

Gi = G.inverse()
K = [Gi * value for value in dG]
A = [-QQ(1)/2 * value for value in K]
rho = [QQ(1)/2 * value.trace() for value in K]
assert all(dG[i] + A[i].transpose() * G + G * A[i] == 0 for i in range(10))
assert all(rho[i] + A[i].trace() == 0 for i in range(10))
assert matrix(QQ, 1, 10, rho).rank() == 1

x = vector(QQ, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
for i in range(10):
    fixed = dG[i] * x
    moving_coefficient = dG[i] + A[i].transpose() * G + G * A[i]
    target_frame = A[i].transpose() * G * x
    field_frame = G * (-A[i] * x)
    assert fixed != 0
    assert moving_coefficient == 0
    assert target_frame + fixed == field_frame

print("PASS independent Sage/QQ ten-normal K77 geometry and owner-split fence")
print("K77_INERTIA=(7,7) NORMAL_BANK_RANK=10 DENSITY_BANK_RANK=1")
print("OWNER_SPLIT=TRIVIALIZATION_DEPENDENT TOTAL_COVECTOR_TRANSPORT=EXACT")
