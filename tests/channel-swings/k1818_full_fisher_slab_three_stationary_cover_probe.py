#!/usr/bin/env python3
"""Hostile mutations for K1818's corrected anchor-hull bank."""
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py"
spec = importlib.util.spec_from_file_location("k1818_probe_base", PRODUCER)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
base = json.loads(module.ARTIFACT.read_text())
assert all(ok for _, ok in module.validate_current(base)), "clean baseline"


def redigest(row):
    payload = {k: v for k, v in row.items() if k != "checkpoint_digest"}
    row["checkpoint_digest"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


# Independently specified exact endpoint cases, including zero contact and
# the real leaf-38 display seam. These do not execute any numerical bank.
cases = [
    ("[1 +/- 1]", []),
    ("[-1 +/- 1]", []),
    ("[1.01 +/- 1]", ["z"]),
    ("[-1.01 +/- 1]", ["z"]),
    ("0", []),
    ("1/100000000000000000000", ["z"]),
    ("[8.5288594933649714996656707604440415459e-11 +/- 8.53e-11]", []),
]
for text, expected in cases:
    row = {"certificate": {"whole_line_gradient": {"t": "0", "z": text}}}
    assert module.saved_gradient_exclusions(row) == expected, text
for text in ("[1 +/- -1]", "nan", "[+/- inf]", "[1 +/- 2] trailing"):
    try:
        module.saved_gradient_exclusions({"certificate": {"whole_line_gradient": {"t": text, "z": "0"}}})
    except ValueError:
        pass
    else:
        raise AssertionError(f"malformed enclosure accepted: {text}")
print("PASS: seven exact endpoint controls and four malformed intervals")

# A planted checkpoint with the observed rounding discrepancy must retain
# the leaf while keeping its original payload/digest as auditable evidence.
transport = json.loads((ROOT / "lab/process/k1820-full-fisher-global-optimizer-admission.json").read_text())
rows = copy.deepcopy(transport["stationary_transport_inputs"])
seam = next(row for row in rows if row["leaf"] == 38)
seam["certificate"]["whole_line_gradient"] = {
    "t": "[7.1387396549832194685734224850943022079e-10 +/- 7.30e-10]",
    "z": cases[-1][0],
}
seam["decision"]["stationary_rejected"] = True
seam["decision"]["rejected_by"] = ["z"]
redigest(seam)
before = copy.deepcopy(rows)
assembled = module.artifact_data(rows)
assert rows == before, "assembly mutated original checkpoint"
assert 38 in assembled["certificate"]["stationary_retained_leaf_ids"]
assert assembled["certificate"]["saved_decision_discrepancies"] == [
    {"checkpoint": seam, "saved_rejected_by": []}
]
assert all(ok for _, ok in module.validate_current(assembled)), "conservative assembly"
print("PASS: conservative assembly preserves original rounding-discrepancy evidence")

for name, change in [
    ("forge saved discrepancy sign", lambda d: d["certificate"]["saved_decision_discrepancies"][0].__setitem__("saved_rejected_by", ["z"])),
    ("break discrepancy digest", lambda d: d["certificate"]["saved_decision_discrepancies"][0]["checkpoint"]["decision"].__setitem__("strictly_convex", True)),
    ("break checkpoint digest map", lambda d: d["certificate"]["checkpoint_digests"].__setitem__("38", "0"*64)),
    ("hide retained discrepancy", lambda d: d["certificate"].__setitem__("saved_decision_discrepancies", [])),
    ("omit saved leaf", lambda d: d["certificate"]["saved_gradient_evidence"].pop()),
]:
    mutated = copy.deepcopy(assembled)
    change(mutated)
    assert not all(ok for _, ok in module.validate_current(mutated)), name
    print(f"PASS: reject {name}")

# In the reverse direction, a saved strict sign is usable even if the old
# advisory flag says retained; the contradiction must remain visible.
seam["certificate"]["whole_line_gradient"]["z"] = "[2 +/- 1]"
seam["decision"].update(stationary_rejected=False, rejected_by=[])
redigest(seam)
reverse = module.artifact_data(rows)
assert 38 in reverse["certificate"]["stationary_rejected_leaf_ids"]
assert all(ok for _, ok in module.validate_current(reverse)), "saved strict sign"
reverse["certificate"]["saved_decision_discrepancies"] = []
assert not all(ok for _, ok in module.validate_current(reverse)), "hidden disagreement"
print("PASS: saved strict sign requires visible disagreement with old flag")


def forge_gradient_exclusion(data):
    row = data["certificate"]["stationary_rejection_evidence"][0]
    row["certificate"]["whole_line_gradient"]["t"] = "[-1 +/- 2]"
    row["certificate"]["whole_line_gradient"]["z"] = "[-1 +/- 2]"
    canonical = dict(row)
    canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    row["checkpoint_digest"] = hashlib.sha256(encoded).hexdigest()
    data["certificate"]["checkpoint_digests"][str(row["leaf"])] = row["checkpoint_digest"]

mutations = [
    (
        "drop rejection evidence",
        lambda data: data["certificate"]["stationary_rejection_evidence"].pop(),
    ),
    (
        "misstate stationary exclusions",
        lambda data: data["decision"].__setitem__(
            "stationary_rejected_leaf_count",
            data["decision"]["stationary_rejected_leaf_count"] + 1,
        ),
    ),
    ("forge gradient exclusion", forge_gradient_exclusion),
    (
        "invent stationary cover",
        lambda data: data["decision"].__setitem__("complete_stationary_cover", True),
    ),
    (
        "invent global optimizer",
        lambda data: data["decision"].__setitem__("global_optimizer_proved", True),
    ),
]

for index, (name, change) in enumerate(mutations, 1):
    mutated = copy.deepcopy(base)
    change(mutated)
    assert not all(ok for _, ok in module.validate_current(mutated)), name
    print(f"PASS {index:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
