#!/usr/bin/env python3
"""Independent compact-support controls and hostile boundary mutations."""
import copy
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "tests/channel-swings/k1819_full_fisher_slab_three_boundary_cover.py"
s = importlib.util.spec_from_file_location("k1819_probe_base", P)
m = importlib.util.module_from_spec(s)
sys.modules[s.name] = m
s.loader.exec_module(m)
base = json.loads(m.ARTIFACT.read_text())
got = m.compute()
count = 0


def passed(label):
    global count
    count += 1
    print(f"PASS {count:02d}: {label}")


# This direct finite-measure calculation is independent of the box consumer.
# It checks the Cauchy Gram identity, arbitrary signed scores and support loss.
for weights, scores, witness, selected in [
    ([F(1, 2), F(1, 2)], [1, 1], [1, -1], [True, False]),
    ([F(2, 7), F(1, 7), F(4, 7)], [-2, 3, 1], [4, -1, 2], [True, False, True]),
    ([F(3), F(5)], [-2, 4], [-2, 4], [True, True]),
]:
    h = [F(v) if keep else F(0) for v, keep in zip(witness, selected)]
    j = sum(w * v * v for w, v in zip(weights, scores))
    a = sum(w * v * u for w, v, u in zip(weights, scores, h))
    b = sum(w * u * u for w, u in zip(weights, h))
    gram = sum(weights[i] * weights[k] * (scores[i]*h[k] - scores[k]*h[i])**2
               for i in range(len(weights)) for k in range(i + 1, len(weights)))
    assert j*b - a*a == gram and gram >= 0 and b > 0
passed("exact weighted compact-support Cauchy identity, signed and unnormalized controls")
assert F(1, 2)**2 / F(1, 2) == F(1, 2)
assert F(1, 2)*1*1 + F(1, 2)*1*(-1) == 0
passed("untruncated witness cancellation is not the compact witness margin")

boxes = {0: (F(0), F(1), F(0), F(1)), 1: (F(1), F(2), F(0), F(1))}
faces, vertices = m.boundary_rows(boxes, {0})
assert len(faces) == len(vertices) == 6
assert sum(bool(r['value_witness_leaves']) for r in faces) == 3
assert sum(bool(r['value_witness_leaves']) for r in vertices) == 4
assert not any(r['face'][0] == 'v' and r['face'][1] == '1' for r in faces)
passed("shared internal edge removed; closed endpoint inheritance retained")
assert m.interval_lower('[1e-9 +/- 2e-9]') < 0
passed("positive midpoint alone does not certify a positive bound")

mutations = [
    ("inflate face closure", lambda d: d["certificate"].__setitem__("certified_exposed_atomic_faces", 115)),
    ("inflate vertex closure", lambda d: d["certificate"].__setitem__("certified_exposed_boundary_vertices", 115)),
    ("conflate two-slab atlas", lambda d: d["certificate"].__setitem__("exposed_atomic_faces", 122)),
    ("erase boundary cover", lambda d: d["decision"].__setitem__("all_slab_three_faces_and_vertices_certified", False)),
    ("invent global", lambda d: d["decision"].__setitem__("global_optimizer_proved", True)),
    ("alter exact threshold", lambda d: d["certificate"].__setitem__("whole_line_value_threshold", "1")),
    ("invent face witness", lambda d: d["certificate"]["faces"][0].__setitem__("value_witness_leaves", [50])),
]
for name, change in mutations:
    d = copy.deepcopy(base)
    change(d)
    assert not all(ok for _, ok in m.validate(d, got)), name
    passed("reject " + name)

rows = m.load("k1816-full-fisher-slab-three-leafwise-score-bank")["certificate"]["leaves"]
for field, value in [("threshold", "1"), ("window", "[-10,10]"), ("anchor", {"t": "0", "z": "0"})]:
    bad = copy.deepcopy(rows)
    bad[0]["certificate"][field] = value
    payload = dict(bad[0]); payload.pop("checkpoint_digest")
    bad[0]["checkpoint_digest"] = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    try:
        m.value_evidence(bad, got["input_partition_digest"])
    except ValueError:
        passed("reject rehashed " + field + " mismatch")
    else:
        raise AssertionError(field)

topology = m.load("k1771-interior-survivor-topology")["topology"]
first = m.load("k1791-full-fisher-three-slab-tail-cover")
second = m.load("k1796-full-fisher-retained-box-enclosure-bank")
actual_boxes = {row['leaf']: tuple(map(F, row['box'])) for row in rows}
for name, edit in [
    ("missing terminal cell", lambda d: d['partition'].__setitem__('unresolved_leaves', 1)),
    ("unproved pruning", lambda d: d['decision'].__setitem__('every_pruned_leaf_has_positive_bernstein_lower_bound', False)),
    ("wrong topology", lambda d: d['partition'].__setitem__('input_topology_digest', 'wrong')),
]:
    bad = copy.deepcopy(first); edit(bad)
    try:
        m.close_boundary([], [], actual_boxes, topology, bad, second)
    except ValueError:
        passed('reject ' + name)
    else:
        raise AssertionError(name)

# The closure lemma alone must not certify an outer-domain face or endpoint.
slab = topology['slabs'][2]
ta = slab['t'][0]; za, zb = slab['z']
outer_face = [{'face': ['v', ta, za, zb], 'incident_leaf': 0, 'value_witness_leaves': []}]
outer_vertex = [{'vertex': [ta, za], 'value_witness_leaves': []}]
m.close_boundary(outer_face, outer_vertex, actual_boxes, topology, first, second)
assert outer_face[0]['closure'] == outer_vertex[0]['closure'] == 'open'
passed('outer-domain boundary requires an independent direct witness')
print(f"RESULT: PASS {count}/{count}")
