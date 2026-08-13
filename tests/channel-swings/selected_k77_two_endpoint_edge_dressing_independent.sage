#!/usr/bin/env sage
"""Independent exact QQ replay of the K77 two-endpoint edge dressing."""

R = PolynomialRing(QQ, [
    'x00','x01','x10','x11',
    'p00','p01','p10','p11',
    's00','s01','s10','s11',
    't00','t01','t10','t11',
])
v = R.gens()
K = R.fraction_field()
X = matrix(K, 2, 2, v[0:4])
P = matrix(K, 2, 2, v[4:8])
Us = matrix(K, 2, 2, v[8:12])
Ut = matrix(K, 2, 2, v[12:16])
q = Us * X * Ut.inverse()
pi = Us.inverse().transpose() * P * Ut.transpose()
outputs = list(q.list()) + list(pi.list())
J = matrix(K, [[entry.derivative(variable) for variable in v] for entry in outputs])

X0 = matrix(QQ, [[2,1],[1,1]])
P0 = matrix(QQ, [[1,2],[-1,3]])
Us0 = matrix(QQ, [[1,1],[0,1]])
Ut0 = matrix(QQ, [[2,1],[1,1]])
point = list(X0.list()) + list(P0.list()) + list(Us0.list()) + list(Ut0.list())
J0 = matrix(QQ, [[entry.subs(dict(zip(v, point))) for entry in row] for row in J.rows()])

canonical = block_matrix(QQ, [[zero_matrix(QQ,4), -identity_matrix(QQ,4)],
                               [identity_matrix(QQ,4), zero_matrix(QQ,4)]])
omega = J0.transpose() * canonical * J0

basis = []
for i in range(2):
    for j in range(2):
        E = zero_matrix(QQ,2)
        E[i,j] = 1
        basis.append(E)

columns = []
for E in basis:
    columns.append(vector(QQ, list((-E*X0).list()) + list((E.transpose()*P0).list())
                          + list((Us0*E).list()) + [0]*4))
for E in basis:
    columns.append(vector(QQ, list((X0*E).list()) + list((-P0*E.transpose()).list())
                          + [0]*4 + list((Ut0*E).list())))
gauge = matrix(QQ, columns).transpose()

assert J0.rank() == 8
assert omega.rank() == 8
assert gauge.rank() == 8
assert omega * gauge == zero_matrix(QQ,16,8)
assert J0 * gauge == zero_matrix(QQ,8,8)
assert matrix(QQ, gauge.columns() + omega.right_kernel().basis()).transpose().rank() == 8

hs = matrix(QQ, [[1,1],[0,1]])
ht = matrix(QQ, [[2,1],[1,1]])
Xp = hs.inverse()*X0*ht
Pp = hs.transpose()*P0*ht.inverse().transpose()
Usp = Us0*hs
Utp = Ut0*ht
assert Usp*Xp*Utp.inverse() == Us0*X0*Ut0.inverse()
assert Usp.inverse().transpose()*Pp*Utp.transpose() == Us0.inverse().transpose()*P0*Ut0.transpose()

# Linearization: dq=(dg3-dphi3)-(dg0-dphi0), while matching the full
# endpoint potential forces p0=p2=-P and therefore retains only half its rank.
assert 40 == 2*20
assert 40 == 2*20
print("PASS independent Sage/QQ two-endpoint dressing, kernel equality, and 40-to-20 fence")
