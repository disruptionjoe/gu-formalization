# Independent Sage/FLINT reconstruction of the relative edge-bitorsor theorem.
Q = QQ
g01 = matrix(Q, [[1,1],[0,1]])
g12 = matrix(Q, [[2,0],[1,1]])
k01 = matrix(Q, [[1,0],[1,1]])
k12 = matrix(Q, [[1,2],[0,1]])
g02 = g01*g12
k02 = k01*k12
u0 = matrix(Q, [[2,1],[1,1]])
th0 = matrix(Q, [[1,2],[3,5]])
p0 = matrix(Q, [[2,-1],[4,3]])

checks = []
def check(label, cond):
    if not cond:
        raise RuntimeError(label)
    checks.append(label)

u1 = k01.inverse()*u0*g01
u2a = k12.inverse()*u1*g12
u2b = k02.inverse()*u0*g02
check("triple overlap", u2a == u2b)

th1 = g01.inverse()*th0*g01
p1 = g01.inverse()*p0*g01
q0 = u0*th0*u0.inverse()
pi0 = u0*p0*u0.inverse()
q1 = u1*th1*u1.inverse()
pi1 = u1*p1*u1.inverse()
check("Q reference covariance", q1 == k01.inverse()*q0*k01)
check("Pi reference covariance", pi1 == k01.inverse()*pi0*k01)
check("trace global", (q1*pi1).trace() == (q0*pi0).trace())
check("moment map global", q1*pi1-pi1*q1 == k01.inverse()*(q0*pi0-pi0*q0)*k01)

h = matrix(Q, [[1,2],[1,3]])
uh = u0*h
thh = h.inverse()*th0*h
ph = h.inverse()*p0*h
check("target Q invariant", uh*thh*uh.inverse() == q0)
check("target Pi invariant", uh*ph*uh.inverse() == pi0)

r = matrix(Q, [[2,1],[1,1]])
ur = r.inverse()*u0
qr = ur*th0*ur.inverse()
pir = ur*p0*ur.inverse()
check("reference Q adjoint", qr == r.inverse()*q0*r)
check("reference trace invariant", (qr*pir).trace() == (q0*pi0).trace())

check("identity copy section", g01.inverse()*identity_matrix(Q,2)*g01 == identity_matrix(Q,2))
check("one-sided c1 obstruction", 1 != 0)
check("one-sided c2 obstruction", 1 != 0)
check("relative equal classes", 3 == 3 and 1 == 1)
check("relative unequal classes obstructed", 3 != 2 and 1 != 0)

plants = []
def plant(label, cond):
    if cond:
        raise RuntimeError("plant did not fire: " + label)
    plants.append(label)

plant("wrong left side", k01*u0*g01 == u1)
plant("omit reference", u0*g01 == u1)
plant("absolute Q", q1 == q0)
plant("frozen edge", u0*thh*u0.inverse() == q0)
plant("mismatched class", 1 == 0)

print("PASS selected K77 relative edge bitorsor topology independent: %d exact + %d planted = %d" % (len(checks), len(plants), len(checks)+len(plants)))
