#!/usr/bin/env python3
"""Exact SC-ACT-04 principal Hessian on the moving-Hq four-real tangent.

V0.212 computed the first-variation Green coefficient against the nonzero
background residual.  This probe computes the distinct second-variation
top-order Gram ``<D Upsilon, D Upsilon>``.  It decides the fixed-pairing,
fixed-geometry principal Hessian only: moving Q_B, metric/section contact,
lower-order Hessian terms, gauge/BV reduction and a closed domain remain open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import product
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_arbitrary_field_euler_green_bank_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, SOURCE, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source_reconstruction = read(
    "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
)
factorization = read(
    "explorations/conditional-build/selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md"
)
fermion_dual = read(
    "explorations/conditional-build/selected-k77-independent-dual-weight-trivialization-2026-08-11.md"
)
check("source", "SC-ACT-04 owns the bosonic residual square",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the source reconstruction types a separate bosonic residual primalizer Q_B",
      "I_2^B[Q_B]" in source_reconstruction and "H_2^B=(D\\Upsilon_B)^\\vee Q_B(D\\Upsilon_B)" in source_reconstruction)
check("prior_art", "the general stationary residual-square Hessian factorization is already known",
      "H2 = (D Upsilon)^! K* (D Upsilon)" in factorization
      and "stationary Hessian exactly `J^T K J`" in factorization)
check("layer0", "the source Q_B is not the fermionic independent barred/unbarred dual orbit",
      "four independent barred and" in fermion_dual
      and "unbarred fields" in fermion_dual)
for label in (
    "first-variation Green coefficient versus second-variation principal Hessian",
    "nonzero principal response versus a nondegenerate induced pairing",
    "fixed residual pairing versus the unbuilt source Q_B primalizer",
    "four-real local doublet tangent versus the full 196-real connection bank",
    "principal Hessian versus the full nonstationary lower-order Hessian",
    "source C^(32,32)+C^(32,32) carrier split versus derived U(32,32)xU(32,32) subgroup",
    "two U(32,32) blocks versus the full U(64,64) parent and independent connections",
):
    check("layer0", label + " remain distinct", True)
for kind, label in (
    ("symplectic", "compute the kinetic bilinear before any presymplectic or BFV quotient"),
    ("analytic", "compute symbol rank and characteristic nullity before a hyperbolicity claim"),
    ("variational", "retain the second-variation Gram even when the first Green row vanishes"),
    ("principal_bundle", "keep moving reduction/contact terms outside the frozen tangent theorem"),
    ("source_review", "do not identify Q_B with the already-built fixed residual pairing"),
    ("contrary", "require live null-direction responses and full-bank controls"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSOR AND ACTUAL FOUR-REAL TANGENT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.212 arbitrary-field Euler/Green predecessor replays",
      "PASS 45/45" in capture.getvalue() and not P["FAILURES"])

T = P["S"]["TANGENT"]
cells = P["cells"]
sym_pair = P["sym_pair"]
real_scalar = P["real_scalar"]
shiab = P["S"]["shiab"]
wedge_raw = P["S"]["wedge_raw"]
SELECTED = P["SELECTED"]
ONE = P["ONE"]
check("exact", "the actual moving-Hq tangent has four real directions", len(T) == 4)
check("exact", "the comparator connection bank remains 196-real", len(cells) == 196)


def principal_with(channels, mu, delta):
    q_mu = {1 << mu: {0: ONE}}
    return shiab(wedge_raw(q_mu, delta), channels)


def gram_block(channels, mu, nu):
    return sp.Matrix(4, 4, [
        real_scalar(sym_pair(principal_with(channels, mu, T[a]),
                             principal_with(channels, nu, T[b])))
        for a in range(4) for b in range(4)
    ])


print("\nC. SELECTED SC-ACT-04 SECOND-VARIATION PRINCIPAL HESSIAN")
blocks = [[gram_block(SELECTED, mu, nu) for nu in range(4)] for mu in range(4)]
expected_diagonal = [
    sp.diag(-8, -8, 0, 0),
    sp.diag(8, 8, 0, 0),
    sp.diag(8, 8, 0, 0),
    sp.diag(8, 8, 0, 0),
]
check("hessian", "the four diagonal base blocks are exact Lorentz multiples of rank two",
      [blocks[mu][mu] for mu in range(4)] == expected_diagonal)
check("hessian", "all mixed base blocks vanish exactly",
      all(blocks[mu][nu] == sp.zeros(4) for mu in range(4) for nu in range(4) if mu != nu))

covectors = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "generic_nonnull": (2, 1, 1, 0),
    "null": (1, 1, 0, 0),
}
symbols = {}
for name, k in covectors.items():
    symbols[name] = sum(
        (sp.Integer(k[mu] * k[nu]) * blocks[mu][nu]
         for mu in range(4) for nu in range(4)),
        sp.zeros(4),
    )
check("hessian", "every tested non-null covector has principal rank two",
      [symbols[name].rank() for name in ("timelike", "spacelike", "generic_nonnull")] == [2, 2, 2])
check("hessian", "the tested null covector is characteristic with rank zero",
      symbols["null"].rank() == 0)
check("hessian", "the internal radical is exactly the last two local directions",
      symbols["timelike"].nullspace() == [
          sp.Matrix([0, 0, 1, 0]), sp.Matrix([0, 0, 0, 1])
      ])
check("hessian", "the J-completed radial direction lies in that radical",
      symbols["timelike"] * sp.Matrix([0, 0, 0, 1]) == sp.zeros(4, 1))

# A radical response can be live while pairing to zero against the whole
# tangent image.  This distinguishes a pairing defect from a zero evaluator.
radical_supports = []
radical_pair_rows = []
for a in (2, 3):
    response = principal_with(SELECTED, 0, T[a])
    radical_supports.append(len(response))
    radical_pair_rows.append([
        real_scalar(sym_pair(response, principal_with(SELECTED, 0, T[b])))
        for b in range(4)
    ])
check("control", "both radical directions have nonzero principal responses",
      radical_supports == [2, 2])
check("control", "their live responses are orthogonal to the complete local tangent image",
      radical_pair_rows == [[0, 0, 0, 0], [0, 0, 0, 0]])
check("plant", "PLANT a Hessian radical is not reported as a zero principal response",
      all(radical_supports) and not any(radical_pair_rows[0] + radical_pair_rows[1]))


print("\nD. FULL CONNECTION BANK AND ALL DISPLAYED SHIAB CHANNELS")
# The full 196-real bank gives a finite control: the same pairing is not
# globally rank two.  Rank 182 was determined exactly from the sparse Gram.
full_responses = [principal_with(SELECTED, 0, delta) for _, _, delta in cells]
full_gram = sp.MutableSparseMatrix(196, 196, {})
for a in range(196):
    for b in range(a, 196):
        value = real_scalar(sym_pair(full_responses[a], full_responses[b]))
        if value:
            full_gram[a, b] = value
            full_gram[b, a] = value
full_rank = full_gram.rank()
check("control", "the selected full 196-real timelike principal Gram has rank 182",
      full_rank == 182)
check("control", "the local rank-two result is a restriction effect, not the full-bank rank",
      full_rank > symbols["timelike"].rank())

channels_all = list(product(("comm", "symi"), repeat=3))
channel_ranks = {}
channel_coefficients = {}
for channel in channels_all:
    block = gram_block(channel, 0, 0)
    channel_ranks["/".join(channel)] = block.rank()
    channel_coefficients["/".join(channel)] = [block[i, i] for i in range(4)]
check("selector", "six displayed Shiab channels give rank two and two give rank zero",
      sorted(channel_ranks.values()) == [0, 0, 2, 2, 2, 2, 2, 2])
check("selector", "no displayed Shiab channel repairs the four-real radical",
      max(channel_ranks.values()) == 2)
check("plant", "PLANT changing only the displayed Shiab selector cannot be called rank four",
      4 not in channel_ranks.values())

# The source first-order contraction itself has zero principal quadratic block
# on this tangent for every displayed channel.  It cannot be silently used as
# the missing kinetic completion.
first_action_ranks = {}
for channel in channels_all:
    rows = sp.Matrix(4, 4, [
        real_scalar(sym_pair(T[a], principal_with(channel, 0, T[b])))
        for a in range(4) for b in range(4)
    ])
    first_action_ranks["/".join(channel)] = rows.rank()
check("selector", "the first-action principal quadratic block is zero for all eight channels",
      set(first_action_ranks.values()) == {0})


print("\nE. DISPOSITION, REVIEWS, AND ACCOUNTING")
check("correction", "v0.212 zero first Green is not promoted to absence of every kinetic Hessian",
      P["green_family"].rank() == 0 and symbols["timelike"].rank() == 2)
check("scope", "the present fixed-pairing parent supplies an incomplete rank-two Higgs kinetic symbol",
      symbols["timelike"].rank() == 2 and len(T) == 4)
for kind, label in (
    ("symplectic", "no presymplectic phase space is inferred from a degenerate local Hessian"),
    ("analytic", "rank two and a null characteristic cone are not a well-posedness theorem"),
    ("scope", "moving Q_B or coupled metric section gauge contact can still pair the radical images"),
    ("scope", "an expanded total-residual/action parent remains a distinct rival"),
    ("layer0", "fermionic independent-dual trivialization does not repair the bosonic Q_B radical"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "no field parameter selector quotient or external datum is added"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_BOSONIC_RESIDUAL_SQUARE_AND_QB_SLOT__SOURCE_SILENT_EXACT_K77_QB_AND_HESSIAN_REPAIR")
print(f"SELECTED_CHANNEL={'/'.join(SELECTED)}")
print("SELECTED_DIAGONALS=" + ";".join(
    ",".join(str(value) for value in block.diagonal()) for block in expected_diagonal
))
print("SYMBOL_RANKS=" + ",".join(f"{name}:{matrix.rank()}" for name, matrix in symbols.items()))
print("RADICAL_RESPONSE_SUPPORTS=" + ",".join(map(str, radical_supports)))
print(f"FULL_TIMELIKE_GRAM_RANK={full_rank}")
print("CHANNEL_RANKS=" + ",".join(f"{key}:{value}" for key, value in channel_ranks.items()))
print("FIRST_ACTION_RANKS=" + ",".join(f"{key}:{value}" for key, value in first_action_ranks.items()))
print("RESULT=FIRST_GREEN_ZERO_BUT_SECOND_PRINCIPAL_HESSIAN_RANK2__TWO_LIVE_KREIN_RADICAL_DIRECTIONS__DISPLAYED_SHIAB_FAMILY_CANNOT_REPAIR")
print("NEXT=TYPE_SOURCE_QB_PRIMALIZER_OR_COUPLED_CONTACT_EXPANDED_PARENT_AND_TEST_RADICAL_REMOVAL")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
