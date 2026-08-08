import os
from pathlib import Path

# ``sage -c load(...)`` rebases ``__file__`` to Sage's launcher on macOS.
# PWD remains the caller's repository root and keeps the source receipts pinned.
ROOT = Path(os.environ.get("PWD", Path.cwd())).resolve()
Q = QQ
eta = diagonal_matrix(Q, [-1, 1, 1, 1])
pairs = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]
checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)
    print("PASS " + label)


J = matrix(Q, 10, 4, lambda a, mu: Q(((a + 2) * (mu + 1) - 7)) / 11)
F = block_matrix(Q, [[identity_matrix(Q, 4), zero_matrix(Q, 4, 10)],
                     [J, identity_matrix(Q, 10)]])
L = F[:, :4]
N = block_matrix(Q, [[-J.transpose()], [identity_matrix(Q, 10)]])
check("complete field map rank fourteen", F.rank() == 14 and F.det() == 1)
check("ordinary pullback kills conormal ten", L.transpose() * N == 0)
check("complete dual retypes conormal as metric equations",
      F.transpose() * N == block_matrix(Q, [[zero_matrix(Q, 4, 10)], [identity_matrix(Q, 10)]]))


def symmetric_basis(column):
    h = matrix(Q, 4, 4, 0)
    mu, nu = pairs[column]
    h[mu, nu] = 1
    h[nu, mu] = 1
    return h


def metric_complex(k_values):
    k = vector(Q, k_values)
    kup = eta * k
    k2 = k * kup
    D = matrix(Q, 10, 4, 0)
    G = matrix(Q, 10, 10, 0)
    W = matrix(Q, 4, 10, 0)
    for row, (mu, nu) in enumerate(pairs):
        for rho in range(4):
            D[row, rho] = k[mu] * eta[nu, rho] + k[nu] * eta[mu, rho]
    for column in range(10):
        h = symmetric_basis(column)
        trace = sum(eta[mu, nu] * h[mu, nu] for mu in range(4) for nu in range(4))
        kkh = sum(kup[mu] * kup[nu] * h[mu, nu] for mu in range(4) for nu in range(4))
        output = matrix(Q, 4, 4, 0)
        for mu in range(4):
            for nu in range(4):
                ricci = Q(1)/2 * (
                    k[mu] * sum(kup[rho] * h[rho, nu] for rho in range(4))
                    + k[nu] * sum(kup[rho] * h[rho, mu] for rho in range(4))
                    - k2 * h[mu, nu] - k[mu] * k[nu] * trace)
                output[mu, nu] = ricci - Q(1)/2 * eta[mu, nu] * (kkh - k2 * trace)
        for row, (mu, nu) in enumerate(pairs):
            G[row, column] = output[mu, nu]
    for column, (mu, nu) in enumerate(pairs):
        for rho in range(4):
            W[rho, column] = ((kup[mu] if nu == rho else 0)
                              + (kup[nu] if mu == rho and nu != mu else 0))
    return D, G, W


for label, k in [("timelike", (1, 0, 0, 0)), ("spacelike", (0, 1, 0, 0))]:
    D, G, W = metric_complex(k)
    check(label + " ranks 4 6 4", (D.rank(), G.rank(), W.rank()) == (4, 6, 4))
    check(label + " gauge complex closes", G * D == 0)
    check(label + " Bianchi complex closes", W * G == 0)
    check(label + " complex exact", D.rank() == 10 - G.rank() and G.rank() == 10 - W.rank())

D0, G0, W0 = metric_complex((1, 0, 0, 1))
check("null ranks 4 4 4", (D0.rank(), G0.rank(), W0.rank()) == (4, 4, 4))
check("null complex closes", G0 * D0 == 0 and W0 * G0 == 0)
check("null field and equation cohomology dimensions two",
      (10 - G0.rank() - D0.rank(), 10 - W0.rank() - G0.rank()) == (2, 2))

portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
iti = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
check("source metric section and rank ten",
      "10-dimensional metric along the fibers" in portal and
      "A metric is a section of its own bundle of metrics" in iti)

print("RESULT=TEN_METRIC_EQUATIONS_RETAINED")
print("PASS %s/%s" % (checks, checks))
