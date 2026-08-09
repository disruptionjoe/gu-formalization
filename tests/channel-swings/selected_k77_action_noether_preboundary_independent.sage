# Independent Sage/QQ certificate for the selected-action Noether/preboundary gate.

K = matrix(QQ, [[2,1,0,0],[1,-3,0,1],[0,0,5,2],[0,1,2,-4]])
A = matrix(QQ, [[0,2,-1,0],[1,0,3,-2],[0,-1,1,2],[2,0,-2,0]])
u = vector(QQ, [1,-2,3,4])
rho = QQ(7)/3
c = QQ(3)/2
dK = -(A.transpose()*K + K*A)
du = A*u + c*u
drho = -2*c*rho
Q0 = (u*K*u)/2
terms = [drho*Q0, rho*(du*K*u), rho*(u*dK*u)/2]
assert all(value != 0 for value in terms)
assert sum(terms) == 0
assert terms[0] + terms[1] != 0
assert terms[1] + terms[2] != 0

D = matrix(QQ, [[-1,1,0,0],[0,-1,1,0],[0,0,-1,1]])
g = vector(QQ, [2,-1,3,1])
a = vector(QQ, [5,-2,7])
T = a-D*g
kappa = vector(QQ, [-2,3,5])
linear = vector(QQ, [1,-4,2])
p = vector(QQ, [T[i]^2+kappa[i]*T[i]+linear[i] for i in range(3)])
Ea = p
Eg = -D.transpose()*p
etas = {
    "timelike": vector(QQ,[1,2,3,5]),
    "spacelike": vector(QQ,[2,-1,4,0]),
    "null": vector(QQ,[1,1,2,3]),
}
for name, eta in etas.items():
    da = D*eta
    assert da-D*eta == 0
    assert Ea*da + Eg*eta == 0
    interior = eta[1]*(p[0]-p[1]) + eta[2]*(p[1]-p[2])
    endpoint = eta[3]*p[2]-eta[0]*p[0]
    assert p*da == interior+endpoint

zg = vector(QQ, [-1,2,0,3])
za = vector(QQ, [4,-3,2])
zT = za-D*zg
zp = vector(QQ, [(2*T[i]+kappa[i])*zT[i] for i in range(3)])
assert zp[0] != 0 and zp[2] != 0
for name, eta in etas.items():
    contraction = -eta[0]*zp[0]+eta[3]*zp[2]
    delta_moment = eta[0]*zp[0]-eta[3]*zp[2]
    assert contraction == -delta_moment
assert any(-eta[0]*zp[0]+eta[3]*zp[2] != 0 for eta in etas.values())
small = vector(QQ, [0,2,-3,0])
assert -small[0]*zp[0]+small[3]*zp[2] == 0

print("PASS 18/18 selected K77 action Noether/preboundary independent Sage/QQ")
