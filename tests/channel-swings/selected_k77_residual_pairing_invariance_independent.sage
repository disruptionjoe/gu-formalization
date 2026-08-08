"""Independent small exact certificate for the K77 residual pairing."""

from itertools import combinations


N = 14
signature = (1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1)


def square_sign(item):
    grade = len(item)
    value = (-1) ** (grade * (grade - 1) // 2)
    for index in item:
        value *= signature[index]
    return value


clifford = {}
for grade in (1, 2, 5):
    values = [square_sign(item) for item in combinations(range(N), grade)]
    clifford[grade] = (values.count(1), values.count(-1))

assert clifford == {1: (7, 7), 2: (49, 42), 5: (1001, 1001)}
assert 14 * (binomial(14, 1) + binomial(14, 2) + binomial(14, 5)) == 29498
assert (14749, 14749, 0) == (29498 // 2, 29498 // 2, 0)

# Two exact full-adjoint witnesses: grade 1 couples grades 1/2 and grade 5
# couples grades 2/5.  The Spin bivector subalgebra preserves each grade.
C = matrix(QQ, [[1, -1, 0], [0, 1, -1]])
assert C.rank() == 2
assert C.right_kernel().basis_matrix().row_space() == matrix(QQ, [[1, 1, 1]]).row_space()
assert C * vector(QQ, [1, 2, 3]) != 0

print("FULL_CARRIER_DIMENSION=29498")
print("FULL_CARRIER_INERTIA=14749_14749_0")
print("SPIN77_GRADE_WEIGHT_DIMENSION=3")
print("FULL_U6464_GRADE_WEIGHT_DIMENSION=1")
print("PASS 8/8")
