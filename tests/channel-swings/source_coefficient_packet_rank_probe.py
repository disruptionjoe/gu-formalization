"""Exact integrity and rank controls for the frozen source coefficient packet."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
REGISTER_PATH = ROOT / "lab/sources/source-claim-register.yaml"
PACKET_PATH = ROOT / "lab/sources/source-coefficient-packet-v0.1.yaml"

CHECKS = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def canonical_row_hash(row):
    payload = json.dumps(
        row,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def matrix_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(a[0])
    for column in range(columns):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][column]
        a[rank] = [value / scale for value in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][column]:
                factor = a[i][column]
                a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


register_bytes = REGISTER_PATH.read_bytes()
register = yaml.safe_load(register_bytes)
packet = yaml.safe_load(PACKET_PATH.read_text())
rows = {row["id"]: row for row in register["claims"]}
selected = packet["selected_rows"]

check(
    "packet pins the exact ratified register edition",
    hashlib.sha256(register_bytes).hexdigest()
    == packet["source_register"]["sha256"],
)
check(
    "every selected row exists exactly once",
    len({entry["id"] for entry in selected}) == len(selected)
    and all(entry["id"] in rows for entry in selected),
)
check(
    "every selected row matches its canonical content hash",
    all(
        canonical_row_hash(rows[entry["id"]]) == entry["row_sha256"]
        for entry in selected
    ),
)
check(
    "the packet carries both assertions and source disavowals",
    {rows[entry["id"]]["polarity"] for entry in selected}
    == {"ASSERTS", "DISAVOWS"},
)

strict = packet["constraint_models"]["strict_source"]
equivariant = packet["constraint_models"]["source_plus_representation_equivariance"]
strict_matrix = [row["coefficients"] for row in strict["equations"]]
equivariant_matrix = [row["coefficients"] for row in equivariant["equations"]]

check(
    "strict source slice supplies zero coefficient equations",
    matrix_rank(strict_matrix) == 0 and len(strict["variables"]) == 4,
)
check(
    "representation exchange has exact rank two",
    matrix_rank(equivariant_matrix) == 2
    and len(equivariant["variables"]) - matrix_rank(equivariant_matrix) == 2,
)
check(
    "representation exchange leaves both owner coordinates free",
    equivariant_matrix == [[1, -1, 0, 0], [0, 0, 1, -1]],
)

silent = set(packet["source_silent_slots"])
check(
    "family covector and independent owner relation remain source-silent",
    {"family_covector", "d54_value", "d210_value", "d54_to_d210_relation"}
    <= silent,
)
check(
    "every reconstruction extension is explicitly non-source",
    all(
        extension["status"] == "declared_non_source"
        for extension in packet["constraint_models"]["reconstruction_extensions"]
    ),
)
check(
    "hostile owner-ratio insertion would change the frozen rank",
    matrix_rank(equivariant_matrix + [[210, 210, -54, -54]]) == 3,
)
check(
    "hostile single-owner selection would change the frozen rank",
    matrix_rank(equivariant_matrix + [[1, 1, 0, 0]]) == 3,
)

print(f"source coefficient packet rank: {len(CHECKS)}/{len(CHECKS)} exact checks passed")
for label in CHECKS:
    print(f"  PASS: {label}")

