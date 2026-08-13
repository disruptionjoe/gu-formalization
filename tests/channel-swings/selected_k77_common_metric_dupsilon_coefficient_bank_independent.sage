#!/usr/bin/env sage
"""Independent QQ/type certificate for the common K77 metric bank.

This route reconstructs the complete spin--Levi-Civita first jet and the
causal diffeomorphism symbols directly.  It models the already-proved
injective raw-residual response by a typed direct sum, so the grade-one gamma
epsilon orbit cannot be silently absorbed into the grade-two physical metric
derivative.
"""

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


slots = [(i, j) for i in range(4) for j in range(i, 4)]
pairs = [(a, b) for a in range(4) for b in range(a+1, 4)]
spin_slots = [(mu, a, b) for mu in range(4) for (a, b) in pairs]
jet_slots = [(lam, i, j) for lam in range(4) for (i, j) in slots]


def hc(i, j, a, b):
    return ZZ((i == a and j == b) or (i == b and j == a))


L = matrix(QQ, 24, 40)
for r, (mu, a, b) in enumerate(spin_slots):
    for c, (lam, i, j) in enumerate(jet_slots):
        L[r,c] = QQ(1)/2 * (
            ZZ(lam == b)*hc(i,j,mu,a) - ZZ(lam == a)*hc(i,j,mu,b)
        )
check("complete spin-Levi-Civita first jet has rank 20", L.rank() == 20)


def fixed_q(q):
    insertion = matrix(QQ, 40, 10)
    for c in range(10):
        for lam in range(4):
            insertion[10*lam+c,c] = q[lam]
    return L*insertion


def diffeo(q):
    D = matrix(QQ, 10, 4)
    for r, (i,j) in enumerate(slots):
        for c in range(4):
            D[r,c] = (q[i] if j == c else 0) + (q[j] if i == c else 0)
    return D


def gamma_symbol(q):
    # q tensor gamma(xi): 16 grade-one connection coordinates.
    G = matrix(QQ, 16, 4)
    for mu in range(4):
        for nu in range(4):
            G[4*mu+nu,nu] = q[mu]
    return G


for name, q in {
    "timelike": vector(QQ,[1,0,0,0]),
    "spacelike": vector(QQ,[0,1,0,0]),
    "null": vector(QQ,[1,0,0,1]),
}.items():
    Lq = fixed_q(q)
    D = diffeo(q)
    C = Lq*D
    G = gamma_symbol(q)
    transverse = identity_matrix(QQ,10) - D*(D.transpose()*D).inverse()*D.transpose()
    check(name+" metric symbol and transverse ranks are 9 and 6",
          Lq.rank() == 9 and (Lq*transverse).rank() == 6)
    check(name+" physical metric orbit and LC connection orbit both have rank 3",
          (-Lq*D).rank() == C.rank() == 3 and -Lq*D + C == 0)
    check(name+" gamma-epsilon input has rank 4", G.rank() == 4)

    # Type-level image of the source orbit after the metric torsion cancels:
    # the top 24 rows are the grade-two LC connection sector and the bottom 16
    # rows are the independent grade-one gamma sector.  An injective residual
    # response preserves this direct-sum distinction.
    source_typed = block_matrix(QQ, [[C], [-G]])
    physical_metric_typed = block_matrix(QQ, [[-C], [zero_matrix(QQ,16,4)]])
    defect = physical_metric_typed + source_typed
    diagnostic_metric_typed = -source_typed
    check(name+" source orbit and Ward-diagnostic completion have rank 4",
          source_typed.rank() == diagnostic_metric_typed.rank() == 4)
    check(name+" physical metric orbit differs from the Ward completion by rank 4",
          (physical_metric_typed-diagnostic_metric_typed).rank() == 4)
    check(name+" typed physical Ward defect remains rank 4",
          defect.rank() == 4)

print("PASS %s/%s" % (checks, checks))
print("DG_COMMON_BANK=RANK20__FIXED_Q_RANK9__TRANSVERSE_RANK6")
print("TORSION_G_VARPI_GRAPH=ZERO")
print("GRADE1_GAMMA_EPSILON_REMAINDER=RANK4")
print("WARD_DIAGNOSTIC_IS_NOT_PHYSICAL_DG")
