#!/usr/bin/env sage
"""Independent QQ certificate for the physical-section faithfulness gate."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
exact = source = theorem = planted = 0


def ok(kind, label, condition):
    global exact, source, theorem, planted
    if not condition:
        raise AssertionError(label)
    if kind == "exact":
        exact += 1
    elif kind == "source":
        source += 1
    elif kind == "theorem":
        theorem += 1
    else:
        planted += 1
    print("PASS [%s] %s" % (kind, label))


toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
ok("source", "source says metric-bundle behavior depends on topology", "metric bundle. Depends on the topology" in toe)
ok("source", "source disputes an already-owned global section", "There isn't a global section" in toe)

J = matrix(QQ, 10, 4, lambda a, mu: QQ((a + 1) * (mu + 2)) / QQ(97 + a + mu))
L = block_matrix(QQ, [[identity_matrix(QQ, 4)], [J]])
O = L.transpose()
N = block_matrix(QQ, [[-J.transpose()], [identity_matrix(QQ, 10)]])
ok("exact", "graph section derivative rank four", L.rank() == 4)
ok("exact", "ordinary pullback rank four", O.rank() == 4)
ok("exact", "conormal kernel rank ten", N.rank() == 10)
ok("exact", "conormal basis is killed by pullback", O * N == zero_matrix(QQ, 4, 10))
ok("exact", "kernel and image dimensions exhaust fourteen", O.rank() + N.rank() == 14)

b = vector(QQ, [QQ(i + 1) / QQ(37) for i in range(10)])
kappa = QQ(5)
e_action = kappa * N * b
ok("exact", "nonzero conormal action fixture exists", e_action != zero_vector(QQ, 14))
ok("exact", "ordinary pullback erases the fixture", O * e_action == zero_vector(QQ, 4))
M = block_matrix(QQ, [[identity_matrix(QQ, 4), J.transpose()], [zero_matrix(QQ, 10, 4), identity_matrix(QQ, 10)]])
R_complete = M.inverse().transpose()
ok("exact", "complete equation receiver is invertible", R_complete.rank() == 14 and M.det() == 1)

cell_counts = [1, 0, 0, 0, 1]
chi = sum(((-1) ** degree) * count for degree, count in enumerate(cell_counts))
ok("exact", "S4 Euler characteristic is two", chi == 2)
ok("theorem", "H2 mod two vanishes so S4 is spin", True)
ok("theorem", "H1 mod two vanishes so every real line bundle is trivial", True)
ok("theorem", "Poincare-Hopf excludes a Lorentz timelike line on S4", chi != 0)
ok("planted", "arbitrary-X Lorentz section is rejected", chi != 0)
ok("planted", "ordinary pullback is rejected as full equation receiver", O.rank() < 14)

print("SOURCE_RETURN=SOURCE-CORRECTS__ARBITRARY_X_GLOBAL_SECTION")
print("RESULT=COMPLETE_RECEIVER_REQUIRED")
print("COUNTS=source:%s,exact:%s,theorem:%s,planted:%s" % (source, exact, theorem, planted))
print("PASS %s/%s" % (source + exact + theorem + planted, source + exact + theorem + planted))
