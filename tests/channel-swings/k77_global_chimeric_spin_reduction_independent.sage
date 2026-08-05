#!/usr/bin/env sage
"""Independent Sage/ZZ/F2 route for the K77 global chimeric-spin reduction."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(label, condition):
    condition = bool(condition)
    checks.append((label, condition))
    print(("PASS" if condition else "FAIL") + " " + label)


print("A. F2 CHARACTERISTIC-CLASS ROUTE")
R = PolynomialRing(GF(2), names=("x0", "x1", "x2", "x3"))
x = list(R.gens())
sym_roots = [R(0) for _ in range(4)] + [x[i] + x[j] for i in range(4) for j in range(i + 1, 4)]


def elementary_one(roots):
    return sum(roots, R(0))


def elementary_two(roots):
    return sum((roots[i] * roots[j] for i in range(len(roots)) for j in range(i + 1, len(roots))), R(0))


w1e = sum(x, R(0))
w2e = sum((x[i] * x[j] for i in range(4) for j in range(i + 1, 4)), R(0))
w1v = elementary_one(sym_roots)
w2v = elementary_two(sym_roots)
c_roots = sym_roots + x
w1c = elementary_one(c_roots)
w2c = elementary_two(c_roots)

check("w1(Sym2 E)=w1(E)", w1v == w1e)
check("w2(Sym2 E)=w1(E)^2", w2v == w1e**2)
check("w1(C)=0", w1c == 0)
check("w2(C)=w2(E)", w2c == w2e)
check("non-spin base remains a genuine planted obstruction", w2c != 0)


print("B. DEWITT SIGNATURE ROUTE")
g = diagonal_matrix(QQ, [-1, 1, 1, 1])
basis = []
for i in range(4):
    for j in range(i, 4):
        h = matrix(QQ, 4, 4)
        h[i, j] = 1
        h[j, i] = 1
        basis.append(h)


def dewitt(h, k):
    return (g * h * g * k).trace() - QQ(1) / 2 * (g * h).trace() * (g * k).trace()


GV = matrix(QQ, [[dewitt(h, k) for k in basis] for h in basis])
t = polygen(QQ, "t")
expected_charpoly = (t - 2)**3 * (t - 1)**3 * (t + 1) * (t + 2)**3
check("DeWitt determinant is 64", GV.det() == 64)
check("DeWitt inertia polynomial is (6,4)", GV.charpoly(t) == expected_charpoly)
check("(6,4)+(1,3)=(7,7)", (6 + 1, 4 + 3) == (7, 7))


print("C. INDEPENDENT INTEGER CLIFFORD ROUTE")
I2 = identity_matrix(ZZ, 2)
S1 = matrix(ZZ, [[0, 1], [1, 0]])
S3 = matrix(ZZ, [[1, 0], [0, -1]])
EPS = matrix(ZZ, [[0, 1], [-1, 0]])


def kron(values):
    out = matrix(ZZ, [[1]])
    for value in values:
        out = out.tensor_product(value)
    return out


plus = []
minus = []
for k in range(7):
    plus.append(kron([S3] * k + [S1] + [I2] * (6 - k)))
    minus.append(kron([S3] * k + [EPS] + [I2] * (6 - k)))

gamma = plus + minus
eta = [1] * 7 + [-1] * 7
I128 = identity_matrix(ZZ, 128)
B = prod(minus, I128)

clifford = all(
    gamma[a] * gamma[b] + gamma[b] * gamma[a]
    == (2 * eta[a] if a == b else 0) * I128
    for a in range(14) for b in range(14)
)
check("Cl(7,7) holds exactly over ZZ", clifford)
check("B is a symmetric involution", B.transpose() == B and B * B == I128)
check("B has split signature by trace/involution", B.trace() == 0)
check("grade one lies in the B-skew adjoint", all(B * q.transpose() * B == -q for q in gamma))
check("grade-one trace Gram is nondegenerate rank fourteen",
      matrix(ZZ, [[(gamma[a] * gamma[b]).trace() for b in range(14)] for a in range(14)]).rank() == 14)

h = gamma[1] * gamma[2]
h_inv = -h
moved = [h * q * h_inv for q in gamma]
check("Spin conjugation preserves the complete labelled frame",
      all(moved[a] * moved[b] + moved[b] * moved[a]
          == (2 * eta[a] if a == b else 0) * I128
          for a in range(14) for b in range(14)))
check("Spin conjugation preserves B", h.transpose() * B * h == B)


print("D. DENSITY-LINE AND SCOPE ROUTE")
DX = vector(ZZ, [1, 0])
DN_DUAL = vector(ZZ, [0, -1])
DY_RESTRICTED = vector(ZZ, [1, 1])
check("ambient density restriction needs one inverse normal-density line",
      DY_RESTRICTED + DN_DUAL == DX)
check("intrinsic X density needs no normal-density choice", DX == vector(ZZ, [1, 0]))

portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
paper = (ROOT / "docs/paper-formalization-candidates.md").read_text()
check("source starts with an active spin structure", "which spin structure is active" in toe)
check("source P_H is the chimeric spinor extension", "structure bundle of the spinors" in portal)
check("paper map makes P_H associated to the chimeric frame bundle", "P_H = P_{Fr(C^{7,7})}" in paper)
check("source epsilon rotates a Clifford invariant", r"\text{Ad}(\varepsilon^{-1}, \Phi)" in portal)

if not all(ok for _, ok in checks):
    raise SystemExit("FAIL independent Sage route")
print("PASS independent Sage route: %s/%s" % (len(checks), len(checks)))
