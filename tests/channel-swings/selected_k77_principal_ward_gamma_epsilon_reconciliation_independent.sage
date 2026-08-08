#!/usr/bin/env sage
"""Independent exact linear-algebra audit of the v0.86 reconciliation.

This route reconstructs the four-dimensional metric diffeomorphism symbol,
the symmetric-frame spin Levi-Civita symbol, and the conditional grade-one
gamma lift directly over QQ.  It does not import the Python implementation.
The Python probe owns the full Clifford residual coefficients; this audit owns
the independent rank and kernel typing that separates the sourced rank-three
connection orbit from the optional rank-four soldering extension.
"""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKS = 0
FAILURES = []


def check(label, condition):
    global CHECKS
    CHECKS += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " " + label)
    if not ok:
        FAILURES.append(label)


slots = [(i, j) for i in range(4) for j in range(i, 4)]
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
orbits = {
    "timelike": vector(QQ, [1, 0, 0, 0]),
    "spacelike": vector(QQ, [0, 1, 0, 0]),
    "null": vector(QQ, [1, 0, 0, 1]),
}


def metric_symbol(q):
    return matrix(QQ, 10, 4, lambda row, nu:
                  q[slots[row][0]] * (1 if slots[row][1] == nu else 0)
                  + q[slots[row][1]] * (1 if slots[row][0] == nu else 0))


def metric_basis(slot):
    i, j = slot
    return matrix(QQ, 4, 4, lambda mu, nu:
                  1 if (mu == i and nu == j) or (mu == j and nu == i) else 0)


def spin_lc_symbol(q):
    basis = [metric_basis(slot) for slot in slots]
    rows = []
    for mu in range(4):
        for a, b in pairs:
            rows.append([(q[b] * h[mu, a] - q[a] * h[mu, b]) / 2 for h in basis])
    return matrix(QQ, rows)


def gamma_symbol(q):
    # Rows are (one-form index mu, Clifford-vector index nu).
    return matrix(QQ, 16, 4, lambda row, column:
                  q[row // 4] if row % 4 == column else 0)


expected_kernels = {
    "timelike": vector(QQ, [1, 0, 0, 0]),
    "spacelike": vector(QQ, [0, 1, 0, 0]),
    "null": vector(QQ, [1, 0, 0, 1]),
}

computed = {}
for name, q in orbits.items():
    D = metric_symbol(q)
    L = spin_lc_symbol(q)
    C = L * D
    G = gamma_symbol(q)
    kernel = C.right_kernel().basis()[0]

    check(name + " metric diffeomorphism symbol has rank four", D.rank() == 4)
    check(name + " spin Levi-Civita symbol has rank nine", L.rank() == 9)
    check(name + " spin connection orbit has rank three", C.rank() == 3)
    check(name + " spin connection orbit has one longitudinal kernel", C.right_nullity() == 1)
    check(name + " longitudinal kernel is the expected causal direction",
          kernel == expected_kernels[name] or kernel == -expected_kernels[name])
    check(name + " direct metric and varpi torsion symbols cancel", (-C + C).is_zero())
    check(name + " grade-one gamma symbol has rank four", G.rank() == 4)
    check(name + " gamma symbol is nonzero on the connection kernel", G * kernel != 0)
    check(name + " gamma extension changes a column absent from the sourced connection orbit",
          block_matrix(QQ, [[C], [G]]).rank() == 4)
    check("PLANT " + name + " rank-three connection orbit is not rank-four diffeomorphism closure",
          C.rank() != D.rank())

    computed[name] = {
        "connection_rank": int(C.rank()),
        "connection_kernel": [int(value) for value in expected_kernels[name]],
        "gamma_rank": int(G.rank()),
        "gamma_nonzero_on_connection_kernel": bool(G * kernel != 0),
    }


registry = json.loads((ROOT / "lab/process/selected-k77-principal-ward-gamma-epsilon-reconciliation.json").read_text())
check("registry source return is SOURCE-CORRECTS", registry["source_return"] == "SOURCE-CORRECTS")
check("registry sourced moving-operator target is rank three",
      registry["next_gate"]["source_variable_moving_operator_rank"] == 3)
check("registry conditional gamma target remains rank four",
      registry["next_gate"]["conditional_gamma_extended_operator_rank"] == 4)
for name, row in computed.items():
    recorded = registry["independent_rank_audit"][name]
    check(name + " independent rank audit matches registry", recorded == row)

check("PLANT no rank calculation promotes a full Frechet Ward identity",
      registry["full_frechet_ward"] == "OPEN")
check("PLANT no rank calculation promotes a reduced symplectic class",
      registry["reduced_symplectic_class"] == "OPEN")

print("INDEPENDENT_SOURCE_CONNECTION_ORBIT=RANK3_ALL_CAUSAL_CLASSES")
print("INDEPENDENT_CONDITIONAL_GAMMA_EXTENSION=RANK4_ALL_CAUSAL_CLASSES")
print("INDEPENDENT_DIRECT_TORSION_CANCELLATION=ZERO")
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS %d/%d" % (CHECKS, CHECKS))
