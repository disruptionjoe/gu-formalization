# Independent exact Sage/QQ reconstruction of the full tau_A0 moment-map gate.

checks = 0
failures = []


def check(label, condition):
    global checks
    checks += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    if not ok:
        failures.append(label)


def ad(g, x):
    return g * x * g.inverse()


def jet_mul(x, y):
    g, dg = x
    h, dh = y
    return (g * h, dg * h + g * dh)


def jet_inv(x):
    g, dg = x
    gi = g.inverse()
    return (gi, -gi * dg * gi)


def gauge_action(jet, connection):
    g, dg = jet
    return ad(g, connection) - dg * g.inverse()


def q(connection, jet):
    return connection - gauge_action(jet, connection)


def ig_mul(x, y):
    gj, a = x
    hj, b = y
    return (jet_mul(gj, hj), a + ad(gj[0], b))


def tau(connection, jet):
    return (jet, q(connection, jet))


def theta(connection, omega):
    gj, a = omega
    return ad(gj[0].inverse(), a - q(connection, gj))


def comm(x, y):
    return x * y - y * x


def vec(x):
    return vector(QQ, x.list())


I = identity_matrix(QQ, 2)
Z = zero_matrix(QQ, 2)
A0 = matrix(QQ, [[2, 1], [3, -1]])
g = (matrix(QQ, [[1, 1], [0, 1]]), matrix(QQ, [[1, 0], [2, -1]]))
h = (matrix(QQ, [[2, 0], [1, 1]]), matrix(QQ, [[0, 1], [-1, 2]]))
k = (matrix(QQ, [[1, 0], [-1, 1]]), matrix(QQ, [[2, -1], [0, 1]]))

gh = jet_mul(g, h)
check("nonzero-A0 cocycle", q(A0, gh) == q(A0, g) + ad(g[0], q(A0, h)))
check("tilted graph homomorphism", ig_mul(tau(A0, g), tau(A0, h)) == tau(A0, gh))

translation = matrix(QQ, [[1, 2], [-2, 3]])
omega = (g, translation)
T0 = theta(A0, omega)
left = ig_mul(tau(A0, jet_inv(g)), omega)
check("left quotient canonical representative", left[0] == (I, Z) and left[1] == T0)
check("left tilted invariance", theta(A0, ig_mul(tau(A0, k), omega)) == T0)
check("right tilted adjoint covariance",
      theta(A0, ig_mul(omega, tau(A0, h))) == ad(h[0].inverse(), T0))

pure_d = (I, matrix(QQ, [[0, 1], [-1, 0]]))
check("derivative term is indispensable", q(A0, pure_d) != A0 - ad(I, A0))

P0 = matrix(QQ, [[3, -1], [2, 4]])
xi = matrix(QQ, [[1, 2], [-1, 0]])
mu = comm(T0, P0)
mu_xi = (P0 * comm(T0, xi)).trace()
check("raw residual moment map is live", mu != Z and mu_xi != 0)
Th = ad(h[0].inverse(), T0)
Ph = ad(h[0].inverse(), P0)
check("trace pairing is invariant", (Ph * Th).trace() == (P0 * T0).trace())
check("moment map is equivariant", comm(Th, Ph) == ad(h[0].inverse(), mu))

# Independent differential assembly for Q=U T U^-1 and PI=U P U^-1.
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
    dQ = U0 * dT * Ui
    dPI = Z
    columns.append(vector(QQ, dQ.list() + dPI.list()))
for dP in basis:
    dQ = Z
    dPI = U0 * dP * Ui
    columns.append(vector(QQ, dQ.list() + dPI.list()))
for dU in basis:
    dQ = dU * T0 * Ui - U0 * T0 * Ui * dU * Ui
    dPI = dU * P0 * Ui - U0 * P0 * Ui * dU * Ui
    columns.append(vector(QQ, dQ.list() + dPI.list()))
J = matrix(QQ, columns).transpose()

C = zero_matrix(QQ, 4)
for i in range(2):
    for j in range(2):
        C[2*i+j, 2*j+i] = 1
Z4 = zero_matrix(QQ, 4)
Omega = block_matrix(QQ, [[Z4, -C], [C, Z4]])
Omega_edge = J.transpose() * Omega * J
check("dressed map rank eight", J.rank() == 8)
check("edge form rank eight", Omega_edge.rank() == 8)
check("edge kernel dimension four", Omega_edge.right_kernel().dimension() == 4)

edge_generators = []
raw_generators = []
for E in basis:
    dT = comm(T0, E)
    dP = comm(P0, E)
    raw_generators.append(vector(QQ, dT.list() + dP.list()))
    edge_generators.append(vector(QQ, dT.list() + dP.list() + (U0 * E).list()))
Rraw = matrix(QQ, raw_generators).transpose()
Redge = matrix(QQ, edge_generators).transpose()
check("edge gauge orbit rank four", Redge.rank() == 4)
check("edge gauge orbit equals characteristic kernel",
      Omega_edge * Redge == zero_matrix(QQ, 12, 4)
      and Redge.rank() == Omega_edge.right_kernel().dimension())
check("raw residual action remains charged", Omega * Rraw != zero_matrix(QQ, 8, 4))

frozen = vector(QQ, comm(T0, xi).list() + comm(P0, xi).list() + [0, 0, 0, 0])
check("frozen edge-frame plant remains charged", Omega_edge * frozen != zero_vector(QQ, 12))

# Moving-reference covariance is the algebraic global patch law.
def jet_conjugate(a, b):
    return jet_mul(jet_mul(a, b), jet_inv(a))


def transform_ig(a, value):
    return (jet_conjugate(a, value[0]), ad(a[0], value[1]))


moved_A0 = gauge_action(k, A0)
moved_T = theta(moved_A0, transform_ig(k, omega))
check("moving-reference distortion patches", moved_T == ad(k[0], T0))
check("moving-reference moment map patches",
      comm(moved_T, ad(k[0], P0)) == ad(k[0], mu))
check("scalar Hamiltonian is patch independent",
      (ad(k[0], P0) * comm(moved_T, ad(k[0], xi))).trace() == mu_xi)

check("edge horn and charged horn remain distinct",
      Omega_edge * Redge == zero_matrix(QQ, 12, 4)
      and Omega * Rraw != zero_matrix(QQ, 8, 4))

if failures:
    raise RuntimeError("; ".join(failures))
print("PASS %s/%s" % (checks, checks))
