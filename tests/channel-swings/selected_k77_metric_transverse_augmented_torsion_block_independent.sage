# Independent QQ certificate for the ten-to-six metric/Levi-Civita theorem.

Q = QQ
slots = [(i, j) for i in range(4) for j in range(i, 4)]
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
orbits = {
    "timelike": vector(Q, [1, 0, 0, 0]),
    "spacelike": vector(Q, [0, 1, 0, 0]),
    "null": vector(Q, [1, 0, 0, 1]),
}
checks = 0
failures = []


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        failures.append(label)


def metric_symbol(q):
    D = matrix(Q, 10, 4)
    for row, (i, j) in enumerate(slots):
        for nu in range(4):
            D[row, nu] = (q[i] if j == nu else 0) + (q[j] if i == nu else 0)
    return D


def levi_civita_symbol(q):
    L = matrix(Q, 24, 10)
    for column, (i, j) in enumerate(slots):
        h = matrix(Q, 4, 4)
        h[i, j] = 1
        h[j, i] = 1
        for mu in range(4):
            for pair_index, (a, b) in enumerate(pairs):
                L[6*mu + pair_index, column] = (q[b]*h[mu, a] - q[a]*h[mu, b])/2
    return L


for name, q in orbits.items():
    D = metric_symbol(q)
    L = levi_civita_symbol(q)
    left_inverse = (D.transpose()*D).inverse()*D.transpose()
    P = identity_matrix(Q, 10) - D*left_inverse
    C = L*D
    kernel = vector(Q, [q[i]*q[j] for i, j in slots])

    check(name + " D rank four", D.rank() == 4)
    check(name + " transverse projector rank six", P.rank() == 6)
    check(name + " transverse kills orbit", P*D == 0)
    check(name + " L rank nine", L.rank() == 9)
    check(name + " q tensor q is L kernel", L*kernel == 0 and L.right_kernel().dimension() == 1)
    check(name + " L kernel is orbit", P*kernel == 0)
    check(name + " L transverse rank six", (L*P).rank() == 6)
    check(name + " connection orbit rank three", C.rank() == 3)
    check(name + " no transverse loss", (L*P).rank() == P.rank())
    check(name + " planted orbit is not transverse", D.column_space() != P.column_space())

if failures:
    raise RuntimeError("; ".join(failures))
print("PASS %s/%s" % (checks, checks))
