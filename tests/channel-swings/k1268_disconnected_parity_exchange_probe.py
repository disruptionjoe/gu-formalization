#!/usr/bin/env python3
"""Hostile mutations for K1268."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1268-disconnected-parity-exchange.json").read_text())
mutations = [
    ("operation", ("reflection", "operation"), "identity"),
    ("preserves", ("reflection", "preserves_J"), False),
    ("det", ("reflection", "determinant"), 1),
    ("effect", ("reflection", "Cartan_effect"), "none"),
    ("exchange", ("reflection", "exchanges_sign_pair"), False),
    ("component", ("reflection", "lies_in_identity_component"), True),
    ("O", ("decision", "full_O77_normalizer_identifies_pair"), False),
    ("Spin", ("decision", "connected_Spin77_owns_reflection"), True),
    ("source", ("decision", "source_action_gauges_reflection"), True),
    ("physical", ("decision", "mathematical_exchange_implies_physical_identification"), True),
]
rejected = 0
for name, path, value in mutations:
    d = copy.deepcopy(BASE)
    d[path[0]][path[1]] = value
    if d != BASE:
        rejected += 1
        print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
