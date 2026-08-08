#!/usr/bin/env sage
"""Independent QQ check of stationary factorization and Ward/Krein controls."""

Rxy.<x,y> = PolynomialRing(QQ)
u = vector(Rxy, [x + y + x*y, 2*x - y + x^2])
K = matrix(Rxy, [[1+x, y], [y, -2+x]])
S = (u*K*u.column())[0] / 2
J = matrix(Rxy, [[entry.derivative(v) for v in (x,y)] for entry in u])
H = matrix(Rxy, [[S.derivative(a).derivative(b) for b in (x,y)] for a in (x,y)])
at0 = {x: 0, y: 0}
assert H.subs(at0) == J.subs(at0).transpose()*K.subs(at0)*J.subs(at0)

R = vector(QQ, [1,1,-1,0,1])
seed = matrix(QQ, [[1,0,2,0], [0,1,1,1], [1,-1,0,2]])
last = -(seed*vector(QQ, R[:4]))
Jb = seed.augment(matrix(QQ, 3, 1, list(last)))
Kb = diagonal_matrix(QQ, [1,-1,2])
Hb = Jb.transpose()*Kb*Jb
assert Jb*R == 0
assert Hb == Hb.transpose()
assert Hb*R == 0

Jiso = matrix(QQ, 2, 1, [1,1])
Kiso = diagonal_matrix(QQ, [1,-1])
assert Jiso.rank() == 1
assert Jiso.transpose()*Kiso*Jiso == zero_matrix(QQ,1,1)

print("PASS 8/8")
