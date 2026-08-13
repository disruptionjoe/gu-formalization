from sage.all import *


checks = []


def check(label, condition):
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    checks.append(ok)


R = PolynomialRing(QQ, names=("f", "u", "t", "b", "r", "s"))
f, u, t, b, r, s = R.gens()
upsilon = 312 * (f + u + t**2) + t
metric = 624 * (f + u / 2 + t**2 / 3) + t
M = matrix(QQ, [[312, 312], [624, 312]])

check("independent equation rank is two", M.rank() == 2)
check("independent equation determinant is minus 97344", M.det() == -97344)

solved_f = t**2 / 3
solved_u = -t / 312 - 4 * t**2 / 3
check("independent family kills Upsilon", upsilon(f=solved_f, u=solved_u) == 0)
check("independent family kills metric trace", metric(f=solved_f, u=solved_u) == 0)
check("independent local freedom is one", 3 - M.rank() == 1)

t0 = QQ(-1) / 104
b0 = QQ(1) / 208
r0 = QQ(1) / 129792
s0 = QQ(0)
f0 = b0**2 + r0
u0 = 2 * b0 * t0 + s0
check("v0108 f lies on family", f0 == solved_f(t=t0))
check("v0108 u lies on family", u0 == solved_u(t=t0))
check("v0108 source residual is zero", upsilon(f=f0, u=u0, t=t0) == 0)
check("v0108 metric trace is zero", metric(f=f0, u=u0, t=t0) == 0)

t1 = QQ(2) / 39
b1 = QQ(7) / 31
f1 = solved_f(t=t1)
u1 = solved_u(t=t1)
r1 = f1 - b1**2
s1 = u1 - 2 * b1 * t1
check("alternate split preserves f", b1**2 + r1 == f1)
check("alternate split preserves u", 2 * b1 * t1 + s1 == u1)
check("normal gauge violates independent B equation", t1 != 0)

G = [
    matrix(QQ, [[0, 1], [1, 0]]),
    matrix(QQ, [[1, 0], [0, -1]]),
    matrix(QQ, [[0, 1], [-1, 0]]),
]


def comm(x, y):
    return x * y - y * x


K = {(i, j): comm(G[i], G[j]) for i in range(3) for j in range(i + 1, 3)}
F = {(i, j): f1 * K[i, j] for i, j in K}
U = {(i, j): u1 * K[i, j] for i, j in K}


def oriented(bank, i, j):
    if i < j:
        return bank[i, j]
    if i > j:
        return -bank[j, i]
    return zero_matrix(QQ, 2)


dB = {(i, j): oriented(F, i, j) / 2 for i in range(3) for j in range(3)}
dT = {(i, j): oriented(U, i, j) / 2 for i in range(3) for j in range(3)}
check("radial B jet reconstructs F", all(dB[i, j] - dB[j, i] == F[i, j] for i, j in F))
check("radial T jet reconstructs DBT", all(dT[i, j] - dT[j, i] == U[i, j] for i, j in U))

g01 = matrix(QQ, [[1, 1], [0, 1]])
g12 = matrix(QQ, [[1, 0], [1, 1]])
g02 = g01 * g12


def transform(bank, g):
    return {key: g.inverse() * value * g for key, value in bank.items()}


check("constant transitions are noncommuting", g01 * g12 != g12 * g01)
check("curvature triple overlap closes", transform(transform(F, g01), g12) == transform(F, g02))
check("distortion triple overlap closes", transform(transform(U, g01), g12) == transform(U, g02))
check("zero amplitude remains a family member", solved_f(t=0) == solved_u(t=0) == 0)

print("FAMILY=f=t^2/3__u=-t/312-4t^2/3")
print("LOCAL_FREEDOM=1")
print("V0108=REPRESENTATIVE")
print("PASS %s/%s" % (sum(checks), len(checks)))
if not all(checks):
    raise SystemExit(1)
