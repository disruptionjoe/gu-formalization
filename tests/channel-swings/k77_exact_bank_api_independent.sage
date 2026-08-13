#!/usr/bin/env sage
"""Independent exact rank replay from the serialized K77 coefficient bank."""

import hashlib
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
unsigned = dict(payload)
unsigned.pop("construction_hash")
canonical = (json.dumps(unsigned, sort_keys=True, separators=(",", ":")) + "\n").encode()
check("exact", "independent canonical construction hash",
      hashlib.sha256(canonical).hexdigest() == payload["construction_hash"])

K = QuadraticField(3, "s")
s = K.gen()
branches = (
    (K(1)/208 - s/312, (-K(2) + s)/208),
    (K(1)/208 + s/312, (-K(2) - s)/208),
)
horizontal = list(payload["receivers"]["horizontal_rows"])
offslice = list(payload["receivers"]["offslice_rows"])
expected = {
    "full": (9, 91, 97),
    "horizontal": (9, 6, 12),
    "offslice": (4, 88, 89),
}


def rational(entry):
    return K(entry[1]) / K(entry[2])


def evaluated_matrix(causal, b_value, t_value):
    columns = payload["columns"][causal]
    result = matrix(K, 1274, 101, sparse=True)
    for column_index, column in enumerate(columns):
        for component, factor in (("constant", K(1)), ("b", b_value), ("t", t_value)):
            for entry in column[component]:
                result[entry[0], column_index] += factor * rational(entry)
    return result


rank_records = {}
for causal in ("timelike", "spacelike", "null"):
    for branch_index, (b_value, t_value) in enumerate(branches, start=1):
        full = evaluated_matrix(causal, b_value, t_value)
        restrictions = {
            "full": full,
            "horizontal": full.matrix_from_rows(horizontal),
            "offslice": full.matrix_from_rows(offslice),
        }
        record = {}
        for region, block in restrictions.items():
            ranks = (
                block.matrix_from_columns(range(10)).rank(),
                block.matrix_from_columns(range(10, 101)).rank(),
                block.rank(),
            )
            record[region] = ranks
            check("exact", "{} branch {} {} ranks {}".format(causal, branch_index, region, ranks),
                  ranks == expected[region])
        rank_records[(causal, branch_index)] = record

check("exact", "all causal representatives and both exact branches agree",
      len(set(tuple(sorted(record.items())) for record in rank_records.values())) == 1)
check("exact", "serialized receiver partition is disjoint and complete",
      not (set(horizontal) & set(offslice)) and set(horizontal) | set(offslice) == set(range(1274)))
check("exact", "serialized construction retains no unitary-parent port",
      payload["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED"
      and payload["scientific_scope"]["full_U64_64"] == "NOT_PORTED")

# Planted failures are evaluated as assertions that the wrong construction does
# not reproduce the accepted theorem.
sample = evaluated_matrix("timelike", branches[0][0], branches[0][1])
check("planted", "PLANT horizontal rows cannot masquerade as the off-slice block",
      sample.matrix_from_rows(horizontal).rank() != expected["offslice"][2])
check("planted", "PLANT metric-only bank cannot masquerade as combined rank 97",
      sample.matrix_from_columns(range(10)).rank() != expected["full"][2])
check("planted", "PLANT epsilon-only bank cannot masquerade as combined off-slice rank 89",
      sample.matrix_from_rows(offslice).matrix_from_columns(range(10, 101)).rank()
      != expected["offslice"][2])

failures = [label for _, label, ok in checks if not ok]
exact = sum(kind == "exact" for kind, _, _ in checks)
planted = sum(kind == "planted" for kind, _, _ in checks)
print("PASS {}/{} ({} exact + {} planted)".format(len(checks)-len(failures), len(checks), exact, planted))
if failures:
    raise SystemExit("; ".join(failures))
