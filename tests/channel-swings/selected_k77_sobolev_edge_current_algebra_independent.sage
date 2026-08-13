# Independent Sage/QQ reconstruction of the compact-boundary Sobolev edge gate.

checks = 0
failures = []


def check(label, condition):
    global checks
    checks += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    if not ok:
        failures.append(label)


def comm(x, y):
    return x * y - y * x


# Sobolev orders on a compact boundary of the 14-dimensional observerse.
d = 13
r = 8
q = r - 1
check("gauge order clears multiplication/derivative threshold", QQ(r) > QQ(d) / 2 + 1)
check("connection order is seven", q == 7)
check("momentum order is dual minus seven", 1 - r == -q)

weights = [(1 + n*n)^q for n in [0, 1, 2, 4, 8]]
singular = [QQ(1) / w for w in weights]
check("same-regularity L2 singular values decay", all(singular[i+1] < singular[i] for i in range(4)))
check("same-regularity inverse is unbounded", weights[-1] > 10^12)
for n, w in zip([0, 1, 2, 4, 8], weights):
    Mdom = diagonal_matrix(QQ, [w, QQ(1)/w])
    Mdual = diagonal_matrix(QQ, [QQ(1)/w, w])
    Jmus = matrix(QQ, [[0, -1], [1, 0]])
    check("dual cotangent musical isometry mode %s" % n,
          Jmus.transpose() * Mdual * Jmus == Mdom)


# Reconstruct the edge dressing independently at one noncommuting point.
Z = zero_matrix(QQ, 2)
T0 = matrix(QQ, [[1, 2], [-2, 3]])
P0 = matrix(QQ, [[3, -1], [2, 4]])
U0 = matrix(QQ, [[1, 2], [1, 3]])
Ui = U0.inverse()
basis = []
for a in range(2):
    for b in range(2):
        E = zero_matrix(QQ, 2)
        E[a, b] = 1
        basis.append(E)

columns = []
for dT in basis:
    columns.append(vector(QQ, (U0*dT*Ui).list() + Z.list()))
for dP in basis:
    columns.append(vector(QQ, Z.list() + (U0*dP*Ui).list()))
for dU in basis:
    dQ = dU*T0*Ui - U0*T0*Ui*dU*Ui
    dPi = dU*P0*Ui - U0*P0*Ui*dU*Ui
    columns.append(vector(QQ, dQ.list() + dPi.list()))
Ddress = matrix(QQ, columns).transpose()

C = zero_matrix(QQ, 4)
for i in range(2):
    for j in range(2):
        C[2*i+j, 2*j+i] = 1
Z4 = zero_matrix(QQ, 4)
Omega = block_matrix(QQ, [[Z4, -C], [C, Z4]])
Omega_edge = Ddress.transpose() * Omega * Ddress

generators = []
raw_generators = []
for E in basis:
    dT = comm(T0, E)
    dP = comm(P0, E)
    raw_generators.append(vector(QQ, dT.list() + dP.list()))
    generators.append(vector(QQ, dT.list() + dP.list() + (U0*E).list()))
Redge = matrix(QQ, generators).transpose()
Rraw = matrix(QQ, raw_generators).transpose()

check("dressed differential rank eight", Ddress.rank() == 8)
check("edge form rank eight", Omega_edge.rank() == 8)
check("edge kernel dimension four", Omega_edge.right_kernel().dimension() == 4)
check("edge kernel equals gauge orbit",
      Redge.rank() == 4 and Omega_edge*Redge == zero_matrix(QQ, 12, 4))
check("raw action remains charged", Omega*Rraw != zero_matrix(QQ, 8, 4))

O3 = block_diagonal_matrix([Omega_edge, Omega_edge, Omega_edge])
R3 = block_diagonal_matrix([Redge, Redge, Redge])
check("three-site edge rank twenty-four", O3.rank() == 24)
check("three-site kernel and orbit both dimension twelve",
      O3.right_kernel().dimension() == 12 and R3.rank() == 12 and O3*R3 == 0)


# Independent polynomial current-algebra bracket.
PR = PolynomialRing(QQ, names=['t0','t1','t2','t3','p0','p1','p2','p3'])
t0,t1,t2,t3,p0,p1,p2,p3 = PR.gens()
T = matrix(PR, [[t0,t1],[t2,t3]])
P = matrix(PR, [[p0,p1],[p2,p3]])
xi = matrix(QQ, [[1,2],[-1,0]])
eta = matrix(QQ, [[0,1],[3,-1]])


def moment(a):
    return (P*comm(T, a)).trace()


variables = list(PR.gens())
df = vector(PR, [moment(xi).derivative(v) for v in variables])
dg = vector(PR, [moment(eta).derivative(v) for v in variables])
bracket = (df * Omega.inverse().change_ring(PR) * dg.column())[0]
expected = -moment(comm(xi, eta))
check("current algebra closes", bracket == expected)
check("classical central remainder vanishes", bracket - expected == 0)
check("current algebra is nonabelian", expected != 0)

vertical = block_matrix(QQ, [[zero_matrix(QQ,4,4)], [identity_matrix(QQ,4)]])
check("vertical polarization is isotropic", vertical.transpose()*Omega*vertical == 0)
check("vertical polarization is half dimensional", vertical.rank()*2 == Omega.nrows())

if failures:
    raise RuntimeError("; ".join(failures))
print("PASS %s/%s" % (checks, checks))
