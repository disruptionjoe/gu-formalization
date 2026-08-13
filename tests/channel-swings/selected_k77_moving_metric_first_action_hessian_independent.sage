#!/usr/bin/env sage
"""Independent Sage/FLINT replay of the completed K77 metric Hessian ranks."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
checks = []


def check(kind, label, condition):
    ok = bool(condition)
    checks.append((kind, label, ok))
    print("{} [{}] {}".format("PASS" if ok else "FAIL", kind, label))


def strict_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key {}".format(key))
        out[key] = value
    return out


payload = json.loads(FIXTURE.read_text(), object_pairs_hook=strict_pairs)
K = QuadraticField(3, "s")
s = K.gen()
branches = (
    (K(1)/208 - s/312, (-K(2) + s)/208),
    (K(1)/208 + s/312, (-K(2) - s)/208),
)
horizontal = list(payload["receivers"]["horizontal_rows"])
offslice = list(payload["receivers"]["offslice_rows"])


def value(entry):
    return K(entry[1]) / K(entry[2])


def metric_matrix(causal, b_value, t_value):
    result = matrix(K, 1274, 10, sparse=True)
    columns = [item for item in payload["columns"][causal] if item["kind"] == "metric"]
    for column_index, column in enumerate(columns):
        for component, factor in (("constant", K(1)), ("b", b_value), ("t", t_value)):
            for entry in column[component]:
                result[entry[0], column_index] += factor * value(entry)
    return result


records = []
for causal in ("timelike", "spacelike", "null"):
    for branch_index, (b_value, t_value) in enumerate(branches, start=1):
        full = metric_matrix(causal, b_value, t_value)
        ranks = (
            full.rank(),
            full.matrix_from_rows(horizontal).rank(),
            full.matrix_from_rows(offslice).rank(),
        )
        records.append(ranks)
        check("exact", "{} branch {} metric ranks {}".format(causal, branch_index, ranks),
              ranks == (9, 9, 4))

# Independent finite cotangent identity: E_y=R^T E_x and its inhomogeneous
# derivative vanishes only on the stationary covector.
S = PolynomialRing(QQ, names=("z", "e0", "e1"))
z, e0, e1 = S.gens()
R = matrix(S, [[1, z], [0, 1]])
E = vector(S, [e0, e1])
dE = vector(S, [entry.derivative(z).subs({z: 0}) for entry in R.transpose() * E])
check("exact", "cotangent receiver derivative is (0,e0)", dE == vector(S, [0, e0]))
check("exact", "receiver derivative vanishes at stationarity", dE.subs({e0: 0, e1: 0}) == 0)
check("planted", "PLANT receiver derivative is live off shell", dE.subs({e0: 2, e1: 3}) != 0)
check("exact", "all six exact metric rank records agree", set(records) == {(9, 9, 4)})
check("exact", "selected bank is real K77 and not a unitary-parent port",
      payload["carrier"]["real_form"] == "Cl(7,7)"
      and payload["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED"
      and payload["scientific_scope"]["full_U64_64"] == "NOT_PORTED")
check("planted", "PLANT horizontal and off-slice row sets are not interchangeable",
      set(horizontal).isdisjoint(set(offslice)) and len(horizontal) != len(offslice))

failures = [label for _, label, ok in checks if not ok]
exact = sum(kind == "exact" for kind, _, _ in checks)
planted = sum(kind == "planted" for kind, _, _ in checks)
print("PASS {}/{} ({} exact + {} planted)".format(len(checks)-len(failures), len(checks), exact, planted))
if failures:
    raise SystemExit("; ".join(failures))
