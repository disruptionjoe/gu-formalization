# Independent Sage/QQ replay of the group-edge dressing gate.

Q = QQ
I2 = identity_matrix(Q, 2)
Z2 = zero_matrix(Q, 2)

x = matrix(Q, [[2, 1], [1, 1]])
p = matrix(Q, [[3, -1], [2, 4]])
u = matrix(Q, [[1, 2], [1, 3]])
h = matrix(Q, [[2, 1], [1, 1]])

q = x * u.inverse()
pi = p * u.transpose()
assert (x*h) * (u*h).inverse() == q
assert (p*h.inverse().transpose()) * (u*h).transpose() == pi

# Exact Jacobian of (x,p,u) -> (x u^-1, p u^T) at the rational fixture.
R = PolynomialRing(Q, names=["x0","x1","x2","x3","p0","p1","p2","p3","u0","u1","u2","u3"])
v = R.gens()
F = R.fraction_field()
X = matrix(F, 2, 2, v[0:4])
P = matrix(F, 2, 2, v[4:8])
U = matrix(F, 2, 2, v[8:12])
Qm = X * U.inverse()
PIm = P * U.transpose()
outputs = list(Qm.list()) + list(PIm.list())
J = matrix(F, [[f.derivative(z) for z in v] for f in outputs])
vals = list(x.list()) + list(p.list()) + list(u.list())
ev = {v[i]: vals[i] for i in range(12)}
J0 = matrix(Q, [[entry.subs(ev) for entry in row] for row in J.rows()])
Ocan = block_matrix(Q, [[zero_matrix(Q,4), identity_matrix(Q,4)], [-identity_matrix(Q,4), zero_matrix(Q,4)]])
O = J0.transpose() * Ocan * J0
assert J0.rank() == 8
assert O.rank() == 8
assert O.transpose() == -O

cols = []
for a in range(2):
    for b in range(2):
        E = zero_matrix(Q, 2)
        E[a,b] = 1
        dx = x*E
        dp = -p*E.transpose()
        du = u*E
        cols.append(vector(Q, list(dx.list()) + list(dp.list()) + list(du.list())))
G = matrix(Q, 12, 4, lambda i,j: cols[j][i])
assert G.rank() == 4
assert O*G == zero_matrix(Q,12,4)
assert O.right_kernel().dimension() == 4

# Base Maurer--Cartan affine law and noncommuting triple overlap.
du0 = matrix(Q, [[2,-1],[3,1]])
dh = matrix(Q, [[0,4],[-2,1]])
a = u.inverse()*du0
assert (u*h).inverse()*(du0*h + u*dh) == h.inverse()*a*h + h.inverse()*dh

h01 = matrix(Q, [[1,1],[0,1]])
h12 = matrix(Q, [[1,0],[1,1]])
dh01 = matrix(Q, [[2,-1],[3,1]])
dh12 = matrix(Q, [[0,4],[-2,1]])
h02 = h01*h12
dh02 = dh01*h12 + h01*dh12
u1 = u*h01
du1 = du0*h01 + u*dh01
assert h01*h12 != h12*h01
assert u1*h12 == u*h02
assert du1*h12 + u1*dh12 == du0*h02 + u*dh02

# Maurer--Cartan curvature vanishes for commuting mixed base derivatives.
du1b = matrix(Q, [[1,2],[0,1]])
du2b = matrix(Q, [[2,0],[-1,3]])
d12 = matrix(Q, [[4,-2],[1,5]])
ui = u.inverse()
a1 = ui*du1b
a2 = ui*du2b
d1a2 = -ui*du1b*ui*du2b + ui*d12
d2a1 = -ui*du2b*ui*du1b + ui*d12
assert d1a2-d2a1+a1*a2-a2*a1 == Z2

print("PASS independent Sage/QQ group-edge dressing replay")
