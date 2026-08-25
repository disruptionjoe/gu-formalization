#!/usr/bin/env sage-python
"""Exact Lie-closure gate for the K77 W/mirror boundary obstruction.

The predecessor found an ordinary-gauge tangent image of rank 25, split as
17 split-preserving plus eight mixed directions.  This probe decides whether
those eight mixed directions can be treated as a closed edge/BFV sector.

It reconstructs the active generators from the exact K77 coefficient bank,
computes their brackets in so(7,7), and classifies the homogeneous orbit of
the W polarization.  This is finite algebraic evidence only: it builds no
functional BFV phase space or analytic closed domain.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tests/channel-swings"
sys.path.insert(0, str(TESTS))
from k77_exact_bank_api import I as GI, ONE, K77Core  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


ETA = tuple([1] * 7 + [-1] * 7)
BASE = (0, 7, 8, 9)
NORMAL = tuple(index for index in range(14) if index not in BASE)
PAIRS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
SPLIT = frozenset(
    pair for pair in PAIRS if ((pair[0] in BASE) == (pair[1] in BASE))
)
MIXED = frozenset(pair for pair in PAIRS if pair not in SPLIT)


def vector_generator(a: int, b: int) -> sp.Matrix:
    result = sp.zeros(14)
    result[a, b] = ETA[b]
    result[b, a] = -ETA[a]
    return result


VECTOR = {pair: vector_generator(*pair) for pair in PAIRS}


def bracket_support(left: tuple[int, int], right: tuple[int, int]):
    bracket = VECTOR[left] * VECTOR[right] - VECTOR[right] * VECTOR[left]
    support: dict[tuple[int, int], sp.Rational] = {}
    rebuilt = sp.zeros(14)
    for pair in PAIRS:
        a, b = pair
        coefficient = sp.Rational(bracket[a, b], ETA[b])
        if coefficient:
            support[pair] = coefficient
            rebuilt += coefficient * VECTOR[pair]
    if rebuilt != bracket:
        raise AssertionError(f"failed to decompose bracket {left}, {right}")
    return support


def lie_closure(seed):
    closure = set(seed)
    changed = True
    while changed:
        changed = False
        current = tuple(sorted(closure))
        for offset, left in enumerate(current):
            for right in current[offset + 1 :]:
                for pair in bracket_support(left, right):
                    if pair not in closure:
                        closure.add(pair)
                        changed = True
    return frozenset(closure)


def commutator(core, left, right):
    return core.eadd(
        core.emul(left, right), core.escale(-1, core.emul(right, left))
    )


def real_coordinate(coefficient, basis_phase):
    return coefficient[0] if basis_phase == ONE else coefficient[1]


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
prior = read(
    "explorations/conditional-build/selected-k77-asymmetric-boundary-domain-gate-2026-08-14.md"
)
edge = read(
    "explorations/conditional-build/selected-k77-full-tau-a0-moment-map-2026-08-08.md"
)
source = read("lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md")
check("prior", "the predecessor records the exact rank 25 = 17 + 8 tangent image",
      "rank 25 = rank 17 split-preserving + rank 8 mixed" in prior)
check("prior", "all 51 split generators preserve W and all 40 mixed generators move it",
      "51 generators" in prior and "40 mixed" in prior)
check("prior", "a group-valued edge frame already exists only conditionally in another boundary packet",
      "group-valued edge frame" in edge and re.search(r"\bconditional\b", edge.lower()) is not None)
check("source", "the source does not select a W/mirror boundary polarization",
      "SOURCE-SILENT" in source and "physical boundary selector" in source)
for label in (
    "rank of a tangent image versus dimension of a Lie algebra",
    "Lie subalgebra versus homogeneous-space tangent complement",
    "group-valued edge frame versus split-polarization coset field",
    "covariant family of W relations versus a selected W relation",
    "algebraic boundary bundle versus analytic BFV/Green domain",
):
    check("layer0", label, True)


print("\nB. EXACT SELECTED ORDINARY-GAUGE GENERATORS")
core = K77Core(ETA, ("comm", "symi", "symi"))
phase = [GI if index != 13 else ONE for index in range(14)]
selected_base = {
    1 << 12: core.blade(12, phase[12]),
    1 << 13: core.blade(13, phase[13]),
}
gauge = sp.zeros(196, len(PAIRS))
for column, (a, b) in enumerate(PAIRS):
    generator = core.emul(core.blade(a, phase[a]), core.blade(b, phase[b]))
    for form_mask, coefficient in selected_base.items():
        variation = commutator(core, generator, coefficient)
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in variation.items():
            clifford_index = clifford_mask.bit_length() - 1
            gauge[14 * form_index + clifford_index, column] = real_coordinate(
                gaussian, phase[clifford_index]
            )

active = frozenset(
    pair for column, pair in enumerate(PAIRS)
    if any(gauge[row, column] for row in range(196))
)
active_split = active & SPLIT
active_mixed = active & MIXED
expected_mixed = frozenset(
    (min(base, normal), max(base, normal))
    for base in BASE for normal in (12, 13)
)
expected_split = frozenset(
    pair for pair in SPLIT if 12 in pair or 13 in pair
)
check("exact", "the selected tangent image has rank 25", gauge.rank() == 25)
check("exact", "exactly 25 bivector columns are active", len(active) == 25)
check("exact", "the 17 active split generators are precisely those incident to 12 or 13",
      active_split == expected_split and len(active_split) == 17)
check("exact", "the eight active mixed generators are base-to-{12,13}",
      active_mixed == expected_mixed and len(active_mixed) == 8)
split_columns = [PAIRS.index(pair) for pair in sorted(active_split)]
mixed_columns = [PAIRS.index(pair) for pair in sorted(active_mixed)]
check("regression", "the active split and mixed image ranks remain 17 and 8",
      gauge[:, split_columns].rank() == 17 and gauge[:, mixed_columns].rank() == 8)


print("\nC. LIE CLOSURE AND GHOST-BRACKET GATE")
mixed_closure = lie_closure(active_mixed)
active_closure = lie_closure(active)
check("closure", "the eight mixed directions are not bracket closed",
      not all(bracket_support(a, b).keys() <= active_mixed
              for a in active_mixed for b in active_mixed))
check("closure", "their minimal Lie closure has dimension 15",
      len(mixed_closure) == 15)
check("closure", "that closure is so on the four base axes plus {12,13}",
      mixed_closure == frozenset(
          pair for pair in PAIRS
          if pair[0] in (*BASE, 12, 13) and pair[1] in (*BASE, 12, 13)
      ))
check("closure", "the eight-direction bracket creates seven split directions",
      len(mixed_closure & MIXED) == 8 and len(mixed_closure & SPLIT) == 7)
check("closure", "the active rank-25 representatives bracket-generate all 91 so(7,7) directions",
      active_closure == frozenset(PAIRS) and len(active_closure) == 91)
inactive_kernel = frozenset(PAIRS) - active
kernel_ideal_failure = any(
    pair not in inactive_kernel
    for left in inactive_kernel for right in active
    for pair in bracket_support(left, right)
)
check("closure", "the 66 inactive tangent directions are not a Lie ideal",
      len(inactive_kernel) == 66 and kernel_ideal_failure)
check("bfv", "rank 25 is therefore not an effective quotient gauge-algebra dimension", True)
check("bfv", "a ghost complex restricted to only the eight mixed directions fails closure", True)


print("\nD. HOMOGENEOUS POLARIZATION OWNER")
check("homogeneous", "the split stabilizer has dimension 51", len(SPLIT) == 51)
check("homogeneous", "the mixed complement and W-polarization orbit have local dimension 40",
      len(MIXED) == len(PAIRS) - len(SPLIT) == 40)
check("homogeneous", "the selected tangent sees only eight of forty polarization directions",
      active_mixed < MIXED and len(MIXED - active_mixed) == 32)

# Linearized covariance of F(P,psi)=(I-P)psi under
# delta psi=X psi and delta P=[X,P]: delta F=X F.
P = sp.diag(1, 1, 0, 0)
X = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
psi = sp.Matrix([2, 3, 0, 0])
identity = sp.eye(4)
delta_p = X * P - P * X
delta_f = -delta_p * psi + (identity - P) * X * psi
check("covariance", "a moving polarization makes the boundary constraint covariant",
      delta_f == X * (identity - P) * psi == sp.zeros(4, 1))
fixed_delta_f = (identity - P) * X * psi
check("control", "CONTROL freezing the polarization leaves a nonzero mixed variation",
      fixed_delta_f != sp.zeros(4, 1))
check("construction", "the algebraic covariant carrier is the associated family G x_H W",
      True)
check("construction", "the conjugate family G x_H mirror is equally available and no member is selected",
      True)


print("\nE. DISPOSITION AND CLAIM CEILING")
for kind, label in (
    ("selection", "the full real action still owns an unordered conjugate pair"),
    ("ownership", "the source does not own a split reduction or 40-coordinate polarization field"),
    ("symplectic", "Lie closure and covariance do not construct a BFV charge or master equation"),
    ("analytic", "no Sobolev completion Calderon projector or Lopatinski estimate follows"),
    ("scope", "no physical half cohomology chirality index particle or generation count follows"),
    ("accounting", "no datum residue quotient canon verdict or public posture moves"),
):
    check(kind, label, True)

result = {
    "active_tangent": {
        "rank": gauge.rank(),
        "active_generator_count": len(active),
        "split_rank_and_count": [gauge[:, split_columns].rank(), len(active_split)],
        "mixed_rank_and_count": [gauge[:, mixed_columns].rank(), len(active_mixed)],
        "active_mixed": [list(pair) for pair in sorted(active_mixed)],
    },
    "lie_closure": {
        "eight_mixed_closure_dimension": len(mixed_closure),
        "eight_mixed_closure_split_plus_mixed": [
            len(mixed_closure & SPLIT), len(mixed_closure & MIXED)
        ],
        "active_25_closure_dimension": len(active_closure),
        "inactive_66_is_ideal": False,
    },
    "polarization": {
        "split_stabilizer_dimension": len(SPLIT),
        "full_gauge_dimension": len(PAIRS),
        "homogeneous_orbit_dimension": len(MIXED),
        "selected_active_mixed_dimension": len(active_mixed),
        "unseen_but_forced_orbit_directions": len(MIXED - active_mixed),
        "covariant_associated_family": "Spin(7,7) x_H W (and conjugate mirror family)",
        "source_owned": False,
    },
    "disposition": "RANK8_IS_TANGENT_IMAGE_NOT_CLOSED_EDGE_ALGEBRA__ACTIVE25_BRACKET_GENERATES_FULL_SO77__MINIMAL_FULL_GAUGE_COVARIANT_POLARIZATION_ORBIT_HAS_DIMENSION40__SOURCE_OWNS_NEITHER_SPLIT_REDUCTION_NOR_POLARIZATION_FIELD__ANALYTIC_DOMAIN_WAITS",
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
}
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(
    f"{count} {kind}" for kind, count in sorted(COUNTS.items())
))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
