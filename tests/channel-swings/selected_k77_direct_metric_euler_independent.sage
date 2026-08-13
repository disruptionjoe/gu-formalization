#!/usr/bin/env sage
"""Independent QQ certificate for the direct K77 metric trace covector."""

from itertools import combinations


COUNTS = {"exact": 0, "control": 0, "planted": 0}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        FAILURES.append(label)


def matrix_trace(value):
    return sum(value[i, i] for i in range(value.nrows()))


def sym2_basis():
    slots = []
    basis = []
    for i in range(4):
        for j in range(i, 4):
            h = matrix(QQ, 4, 4)
            h[i, j] = 1
            h[j, i] = 1
            slots.append((i, j))
            basis.append(h)
    return tuple(slots), tuple(basis)


def dewitt(inverse, basis):
    return matrix(QQ, len(basis), len(basis), [
        matrix_trace(inverse * left * inverse * right)
        - QQ(1)/2 * matrix_trace(inverse * left) * matrix_trace(inverse * right)
        for left in basis for right in basis
    ])


def d_dewitt(inverse, h, basis):
    dinverse = -inverse * h * inverse
    return matrix(QQ, len(basis), len(basis), [
        matrix_trace(dinverse * left * inverse * right)
        + matrix_trace(inverse * left * dinverse * right)
        - QQ(1)/2 * (
            matrix_trace(dinverse * left) * matrix_trace(inverse * right)
            + matrix_trace(inverse * left) * matrix_trace(dinverse * right)
        )
        for left in basis for right in basis
    ])


g4 = diagonal_matrix(QQ, [1, -1, -1, -1])
g4i = g4.inverse()
slots, basis = sym2_basis()
dv = dewitt(g4i, basis)
gt = block_diagonal_matrix(g4, dv)
normal_bank = tuple(block_diagonal_matrix(h, d_dewitt(g4i, h, basis)) for h in basis)
densities = tuple(QQ(1)/2 * matrix_trace(gt.inverse() * h) for h in normal_bank)
expected_density = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)

check("exact", "independent DeWitt matrix has determinant eight-squared with split total signature",
      gt.det() == -64 and QuadraticForm(QQ, gt).signature() == 0)
check("exact", "independent all-ten density covector agrees coefficientwise",
      densities == expected_density)
check("exact", "density equals minus twice the base metric trace in all ten directions",
      all(densities[k] == -2 * matrix_trace(g4i * basis[k]) for k in range(10)))
check("exact", "density row has rank one and kernel dimension nine",
      matrix(QQ, 1, 10, densities).rank() == 1
      and matrix(QQ, 1, 10, densities).right_kernel().dimension() == 9)

b, t = PolynomialRing(QQ, names=("b", "t")).gens()
lagrangian = 7*t*(624*b^2 + 624*b*t + 208*t^2 + t)
branch = {b: QQ(1)/156, t: -QQ(1)/78}
action_value = lagrangian.subs(branch)
check("exact", "independent action polynomial is critical at the repaired branch",
      lagrangian.derivative(b).subs(branch) == 0
      and lagrangian.derivative(t).subs(branch) == 0)
check("exact", "independent repaired-branch action value is seven over 18252",
      action_value == QQ(7)/18252)

normalized = tuple(action_value * value for value in densities)
coordinate = tuple(8 * value for value in normalized)
expected = (-QQ(7)/9126, 0, 0, 0, QQ(7)/9126, 0, 0, QQ(7)/9126, 0, QQ(7)/9126)
check("exact", "independent normalized metric Euler covector agrees exactly",
      normalized == expected)
check("exact", "independent coordinate-volume covector is eight times normalized",
      coordinate == tuple(8 * value for value in expected))
check("control", "trivial branch has zero action and zero metric Euler",
      lagrangian.subs({b: 0, t: 0}) == 0)
check("planted", "PLANT the nontrivial branch is not a zero-action saddle",
      action_value != 0 and matrix(QQ, 1, 10, normalized).rank() == 1)
check("planted", "PLANT the six off-diagonal directions are not counted as missing rows",
      len([k for k, slot in enumerate(slots) if slot[0] != slot[1] and densities[k] == 0]) == 6)

print("ACTION_VALUE=" + str(action_value))
print("DENSITIES=" + str(densities))
print("NORMALIZED_EULER=" + str(normalized))
print("CHECKS=" + " ".join(kind + ":" + str(COUNTS[kind]) for kind in sorted(COUNTS)))
if FAILURES:
    raise RuntimeError("FAILURES: " + "; ".join(FAILURES))
print("PASS " + str(sum(COUNTS.values())) + "/" + str(sum(COUNTS.values())))
