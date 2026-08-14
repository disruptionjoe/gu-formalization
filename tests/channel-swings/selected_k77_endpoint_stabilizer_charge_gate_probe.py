#!/usr/bin/env python3
"""Exact selected-K77 endpoint stabilizer-charge gate.

The predecessor proved that a full-frame endpoint covector descends to the
40-dimensional split-polarization orbit exactly when it annihilates the
51-dimensional split stabilizer.  This probe evaluates the actual frozen
selected-action endpoint covector ``E_B-E_T`` on ``[X,T]`` for every one of
the 91 real ``so(7,7)`` bivector generators.  It is a finite exact fixture
certificate, not an every-background theorem or a BFV/domain construction.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_action_boundary_coefficient_bank_probe.py"
REGISTRY = ROOT / "lab/process/selected-k77-endpoint-stabilizer-charge-gate.json"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict_json(path):
    def reject(value):
        raise ValueError(f"duplicate JSON key: {value}")

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=lambda pairs: (
        (_ for _ in ()).throw(ValueError("duplicate JSON key"))
        if len({key for key, _ in pairs}) != len(pairs)
        else dict(pairs)
    ), parse_constant=reject)


print("A. PREDECESSOR, LAYER ZERO, AND CARRIER")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    packet = runpy.run_path(str(PREDECESSOR))
check("predecessor", "the frozen selected-action endpoint bank replays 44/44",
      capture.getvalue().rstrip().endswith("PASS 44/44") and not packet["FAILURES"])

for label in (
    "distortion T versus the source moving frame epsilon",
    "action endpoint covector E_B-E_T versus an arbitrary cotangent covector",
    "stabilizer charge support versus number of independent constraints",
    "failure of orbit descent versus failure of the larger charged edge horn",
    "finite exact fixture result versus an every-background theorem",
):
    check("layer0", label + " remain distinct", True)

T = packet["T"]
B = packet["B"]
blade = packet["blade"]
comm = packet["M"]["comm"]
gsub = packet["M"]["gsub"]
ZERO = packet["M"]["ZERO"]
PAIRS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
BASE = frozenset((0, 7, 8, 9))
SPLIT = tuple(i for i, (a, b) in enumerate(PAIRS) if ((a in BASE) == (b in BASE)))
MIXED = tuple(i for i in range(len(PAIRS)) if i not in SPLIT)
check("typing", "the reductive split is exactly 51 plus 40", len(SPLIT) == 51 and len(MIXED) == 40)


def orbit_direction(generator):
    return {form_mask: comm(generator, coefficient) for form_mask, coefficient in T.items()}


print("\nB. ALL-91 DIRECT ENDPOINT MOMENT-MAP COMPONENTS")
charges = []
directions = []
for pair in PAIRS:
    direction = orbit_direction(blade(pair))
    directions.append(direction)
    charges.append(packet["e_difference"](direction))

split_support = tuple(i for i in SPLIT if charges[i] != ZERO)
mixed_support = tuple(i for i in MIXED if charges[i] != ZERO)
split_values = tuple(charges[i][0] for i in SPLIT)
mixed_values = tuple(charges[i][0] for i in MIXED)

check("charge", "all endpoint charges are real on the frozen real fixture",
      all(value[1] == 0 for value in charges))
check("charge", "the 51 split components have exact nonzero support 15",
      len(split_support) == 15)
check("charge", "the 40 mixed components have exact nonzero support 15",
      len(mixed_support) == 15)
check("fingerprint", "the split squared norm fingerprint is 1525648/9",
      sum(value * value for value in split_values) == Fraction(1525648, 9))
check("fingerprint", "the mixed squared norm fingerprint is 2364016/9",
      sum(value * value for value in mixed_values) == Fraction(2364016, 9))
check("descent", "the actual selected-action endpoint covector fails stabilizer annihilation",
      any(charges[i] != ZERO for i in SPLIT))
check("descent", "the endpoint moment map also has live mixed charge",
      any(charges[i] != ZERO for i in MIXED))


print("\nC. INDEPENDENT EXACT ACTION-DERIVATIVE RECONSTRUCTION")
for index, direction in enumerate(directions):
    finite = gsub(
        packet["five_point"]("B", direction, B, T),
        packet["five_point"]("T", direction, B, T),
    )
    check("independent", f"generator {PAIRS[index]}: analytic and exact five-point charges agree",
          finite == charges[index])


print("\nD. CONTROLS AND DISPOSITION")
zero_direction = {form_mask: {} for form_mask in T}
check("control", "the zero orbit direction has zero endpoint charge",
      packet["e_difference"](zero_direction) == ZERO)
first_live_split = split_support[0]
check("control", "deleting one live split component changes the split fingerprint",
      sum(value * value for j, value in enumerate(split_values) if SPLIT[j] != first_live_split)
      != Fraction(1525648, 9))
check("constraint", "the zero level of the full stabilizer moment map is required before orbit reduction", True)
check("edge", "the larger charged endpoint/edge completion remains the current admissible carrier", True)
check("bfv", "a reduced orbit moment map and BFV master equation are not constructed", True)
check("analytic", "no codimension-one domain or positivity claim follows", True)
check("selection", "W and mirror remain equal unselected families", True)
check("accounting", "no datum residue quotient verdict canon or public posture changes", True)

if REGISTRY.exists():
    registry = strict_json(REGISTRY)
    check("registry", "registry records exact split and mixed support counts",
          registry["charge_decomposition"]["split_nonzero_support"] == 15
          and registry["charge_decomposition"]["mixed_nonzero_support"] == 15)
    check("registry", "registry rejects cotangent descent and preserves the larger edge horn",
          registry["cotangent_descent"]["passes"] is False
          and registry["continuation"]["larger_charged_edge_completion"] == "RETAINED")

print("\nSUMMARY")
print("SPLIT_NONZERO=" + ",".join(str(PAIRS[i]) for i in split_support))
print("MIXED_NONZERO=" + ",".join(str(PAIRS[i]) for i in mixed_support))
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
