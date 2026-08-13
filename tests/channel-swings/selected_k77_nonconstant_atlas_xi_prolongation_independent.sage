from sage.all import *


checks = []


def check(label, condition):
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    checks.append(ok)


K.<a> = NumberField(x^2 - 3)
R = PolynomialRing(K, names=("x0", "x1", "x2"))
x0, x1, x2 = R.gens()
coords = (x0, x1, x2)

b_plus = K(1)/208 - a/312
t_plus = -K(1)/104 + a/208
b_minus = K(1)/208 + a/312
t_minus = -K(1)/104 - a/208


def upsilon(b, t):
    return 312*(b+t)^2 + t


def metric(b, t):
    return 624*(b^2+b*t+t^2/3) + t


check("two algebraic branches solve Upsilon", upsilon(b_plus, t_plus) == 0 and upsilon(b_minus, t_minus) == 0)
check("two algebraic branches solve metric trace", metric(b_plus, t_plus) == 0 and metric(b_minus, t_minus) == 0)
check("branches are conjugate", b_plus.galois_conjugate() == b_minus and t_plus.galois_conjugate() == t_minus)
check("plus branch lies on invariant f family", b_plus^2 == t_plus^2/3)
check("plus branch lies on invariant u family", 2*b_plus*t_plus == -t_plus/312 - 4*t_plus^2/3)

G = [
    matrix(R, [[0, 1], [1, 0]]),
    matrix(R, [[1, 0], [0, -1]]),
    matrix(R, [[0, 1], [-1, 0]]),
]
I2 = identity_matrix(R, 2)
Z2 = zero_matrix(R, 2)


def comm(left, right):
    return left*right - right*left


def dmat(value, i):
    return value.apply_map(lambda entry: entry.derivative(coords[i]))


def transform_connection(connection, g):
    gi = g.inverse()
    return [gi*connection[i]*g + gi*dmat(g, i) for i in range(3)]


def transform_form(form, g):
    gi = g.inverse()
    return [gi*value*g for value in form]


def curvature(connection):
    return {(i,j): dmat(connection[j], i) - dmat(connection[i], j)
            + comm(connection[i], connection[j])
            for i in range(3) for j in range(i+1, 3)}


def covariant(connection, form):
    return {(i,j): dmat(form[j], i) - dmat(form[i], j)
            + comm(connection[i], form[j]) - comm(connection[j], form[i])
            for i in range(3) for j in range(i+1, 3)}


B0 = [b_plus*value for value in G]
T0 = [t_plus*value for value in G]
F0 = curvature(B0)
U0 = covariant(B0, T0)
check("homogeneous F is b squared commutator", all(F0[i,j] == b_plus^2*comm(G[i],G[j]) for i,j in F0))
check("homogeneous DBT is 2bt commutator", all(U0[i,j] == 2*b_plus*t_plus*comm(G[i],G[j]) for i,j in U0))

Np = matrix(R, [[0,1],[0,0]])
Nm = matrix(R, [[0,0],[1,0]])
g01 = I2 + x0*Np
g12 = I2 + x1*Nm
g02 = g01*g12
check("transitions are nonconstant and noncommuting", g01*g12 != g12*g01)

B1 = transform_connection(B0, g01)
B2s = transform_connection(B1, g12)
B2d = transform_connection(B0, g02)
T1 = transform_form(T0, g01)
T2s = transform_form(T1, g12)
T2d = transform_form(T0, g02)
check("affine connection triple overlap closes", B2s == B2d)
check("distortion triple overlap closes", T2s == T2d)

F1 = curvature(B1)
U1 = covariant(B1, T1)
check("curvature transforms covariantly", all(F1[k] == g01.inverse()*F0[k]*g01 for k in F0))
check("DBT transforms covariantly", all(U1[k] == g01.inverse()*U0[k]*g01 for k in U0))

B1_bad = transform_form(B0, g01)
F1_bad = curvature(B1_bad)
check("omitting affine term fires", any(F1_bad[k] != g01.inverse()*F0[k]*g01 for k in F0))
check("reversed cocycle order fires", transform_connection(B0, g12*g01) != B2s)

print("BRANCHES=t=(-2+-sqrt3)/208")
print("ATLAS=NONCONSTANT_AFFINE_EXACT")
print("XI=REDUNDANT_BY_SOURCE_DISPLAY")
print("PASS %s/%s" % (sum(checks), len(checks)))
if not all(checks):
    raise SystemExit(1)
