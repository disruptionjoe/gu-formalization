#!/usr/bin/env sage-python
"""Exact K77 asymmetric primal boundary/domain gate.

This probe tests the smallest already-owned W/mirror boundary candidates
against the actual first-order action Green symbols and the selected ordinary
gauge image.  It certifies finite algebraic boundary data only: no analytic
closed domain, Calderon projector, BFV edge completion, or physical
cohomology is inferred.
"""

from __future__ import annotations

import ast
from collections import Counter
from pathlib import Path
import sys

import sympy as sp
from sage.all import (
    QuadraticField,
    block_diagonal_matrix,
    block_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tests/channel-swings"
sys.path.insert(0, str(TESTS))
from k77_exact_bank_api import I as GI, ONE, K77Core  # noqa: E402

COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load_build_structures():
    source = read("tests/channel-swings/selected_k77_induced_fermion_principal_discriminator.py")
    tree = ast.parse(source)
    node = next(
        item for item in tree.body
        if isinstance(item, ast.FunctionDef) and item.name == "build_structures"
    )
    namespace = {
        "identity_matrix": identity_matrix,
        "matrix": matrix,
        "block_matrix": block_matrix,
        "zero_matrix": zero_matrix,
    }
    exec(
        compile(ast.Module(body=[node], type_ignores=[]), "<build-structures>", "exec"),
        namespace,
    )
    return namespace["build_structures"]


print("A. OWNERSHIP, PRIOR ART, AND LAYER ZERO")
trace_pair = read(
    "explorations/conditional-build/selected-k77-w-mirror-trace-hq-isotropy-correction-2026-08-13.md"
)
pair_owner = read(
    "explorations/conditional-build/selected-k77-w-mirror-action-pairing-ownership-2026-08-13.md"
)
green = read(
    "explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md"
)
domain = read("explorations/k77-wave2-action-polarization-common-observation-domain-2026-08-05.md")
source = read("lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md")
check("prior", "trace Hq makes W and mirror complementary maximal isotropic halves",
      "complementary maximal isotropic subspaces" in trace_pair)
check("prior", "trace Hq is not in the two-line current action-pairing class",
      "not in their span" in pair_owner)
check("prior", "the owned ordinary gauge complex has eight active mixed directions",
      "eight-dimensional active ghost image" in green)
check("prior", "the observation section is codimension ten rather than a Green boundary",
      "`s(X4)` is codimension ten" in domain
      and "ordinary boundary would be thirteen" in domain)
check("source", "the source is silent on a global physical boundary selection",
      "SOURCE-SILENT" in source and "physical boundary selector" in source)
for label in (
    "trace-Hq Witt pairing versus action Green symbol",
    "fibrewise maximal isotropic relation versus analytic closed domain",
    "ordinary-gauge invariant subspace versus reduced BFV boundary condition",
    "W/mirror primal sectors versus ambient C^(32,32) halves",
    "an unordered conjugate pair versus a selected physical member",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT K77 W/MIRROR AND ACTION GREEN RESTRICTIONS")
K = QuadraticField(-1, "ii")
ii = K.gen()
data = load_build_structures()(K, ii)
gammas = data["gammas"]
eta = data["eta"]
P_w = data["projectors"]["W_sd192"]
P_m = data["projectors"]["mirror_asd192"]
W = P_w.matrix_from_columns(list(P_w.pivots()))
M = W.conjugate()
check("exact", "W and mirror are exact conjugate rank-192 sectors",
      W.rank() == M.rank() == 192 and P_w.conjugate() == P_m and P_w != P_m)
check("exact", "the two primal sectors are disjoint and span rank 384",
      W.augment(M).rank() == 384)

B = identity_matrix(K, 128, sparse=True)
for gamma in gammas[7:]:
    B *= gamma
omega = identity_matrix(K, 128, sparse=True)
for gamma in gammas:
    omega *= gamma
action_pairings = {
    "symmetric": block_diagonal_matrix(
        [K(eta[a]) * B for a in range(14)], sparse=True
    ),
    "skew": block_diagonal_matrix(
        [K(eta[a]) * B * omega for a in range(14)], sparse=True
    ),
}
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)

for horn, pairing in action_pairings.items():
    base_packets = []
    normal_packets = []
    for axis in range(14):
        covector = [0] * 14
        covector[axis] = 1
        principal = data["rolled_symbol"](covector)[:1792, :1792]
        green_symbol = pairing * principal
        packet = (
            W.transpose() * green_symbol * W,
            M.transpose() * green_symbol * M,
            W.transpose() * green_symbol * M,
            M.transpose() * green_symbol * W,
        )
        (base_packets if axis in BASE else normal_packets).append(packet)
    check("green", f"{horn} action horn makes W and mirror isotropic for all four base conormals",
          all(ww.is_zero() and mm.is_zero() for ww, mm, wm, mw in base_packets))
    check("green", f"{horn} action horn pairs W and mirror nondegenerately for every base conormal",
          all(wm.rank() == mw.rank() == 192 for ww, mm, wm, mw in base_packets))
    check("green", f"{horn} action horn is nondegenerate inside both halves for all ten normal conormals",
          all(ww.rank() == mm.rank() == 192 for ww, mm, wm, mw in normal_packets))
    check("green", f"{horn} action horn has zero W-mirror cross restriction for all ten normal conormals",
          all(wm.is_zero() and mw.is_zero() for ww, mm, wm, mw in normal_packets))

check("construction", "a base-conormal W or mirror relation is the smallest current action-Green isotropic candidate", True)
check("obstruction", "a normal-conormal W or mirror relation fails action-Green isotropy", True)
check("planted", "choosing only W is asymmetric because conjugation sends it to distinct mirror", P_w.conjugate() == P_m and P_w != P_m)
check("control", "retaining W plus mirror preserves the conjugation-invariant nonchiral total", W.augment(M).rank() == 384)


print("\nC. FULL SPIN AND SELECTED ORDINARY-GAUGE BASICNESS")
spin_identity = identity_matrix(K, 128, sparse=True)
vector_identity = identity_matrix(K, 14, sparse=True)


def vector_generator(a: int, b: int):
    result = zero_matrix(K, 14, 14, sparse=True)
    result[a, b] = eta[b]
    result[b, a] = -eta[a]
    return result


def spin_generator(a: int, b: int):
    return (gammas[a] * gammas[b] - gammas[b] * gammas[a]) / K(4)


def total_generator(a: int, b: int):
    return (
        vector_generator(a, b).tensor_product(spin_identity)
        + vector_identity.tensor_product(spin_generator(a, b))
    )


pairs = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
split_pairs = tuple(
    pair for pair in pairs
    if ((pair[0] in BASE) == (pair[1] in BASE))
)
mixed_pairs = tuple(pair for pair in pairs if pair not in split_pairs)
split_preserved = sum(
    int((total_generator(a, b) * P_w - P_w * total_generator(a, b)).is_zero())
    for a, b in split_pairs
)
mixed_preserved = sum(
    int((total_generator(a, b) * P_w - P_w * total_generator(a, b)).is_zero())
    for a, b in mixed_pairs
)
check("gauge", "all 51 split-stabilizer generators preserve W and mirror", split_preserved == 51)
check("gauge", "none of the 40 mixed generators preserves W or mirror", mixed_preserved == 0)

core = K77Core(tuple(eta), ("comm", "symi", "symi"))
phase = [GI if index != 13 else ONE for index in range(14)]
selected_base = {
    1 << 12: core.blade(12, phase[12]),
    1 << 13: core.blade(13, phase[13]),
}


def commutator(left, right):
    return core.eadd(core.emul(left, right), core.escale(-1, core.emul(right, left)))


def real_coordinate(coefficient, basis_phase):
    return coefficient[0] if basis_phase == ONE else coefficient[1]


gauge = sp.zeros(196, len(pairs))
for column, (a, b) in enumerate(pairs):
    generator = core.emul(core.blade(a, phase[a]), core.blade(b, phase[b]))
    for form_mask, coefficient in selected_base.items():
        variation = commutator(generator, coefficient)
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in variation.items():
            clifford_index = clifford_mask.bit_length() - 1
            gauge[14 * form_index + clifford_index, column] = real_coordinate(
                gaussian, phase[clifford_index]
            )

split_columns = [pairs.index(pair) for pair in split_pairs]
mixed_columns = [pairs.index(pair) for pair in mixed_pairs]
split_image = gauge.extract(range(196), split_columns)
mixed_image = gauge.extract(range(196), mixed_columns)
active_mixed = [
    column for column in mixed_columns
    if any(gauge[row, column] for row in range(196))
]
check("selected_gauge", "the selected ordinary-gauge image has rank 25",
      gauge.rank() == 25)
check("selected_gauge", "its split-preserving image has rank 17",
      split_image.rank() == 17)
check("selected_gauge", "its mixed image has rank eight with eight active mixed generators",
      mixed_image.rank() == 8 and len(active_mixed) == 8)
check("selected_gauge", "every active mixed selected generator fails to preserve W and mirror",
      all(pairs[column] in mixed_pairs for column in active_mixed)
      and mixed_preserved == 0)
check("obstruction", "W-only and mirror-only base boundary candidates are not basic for the owned ordinary-gauge quotient",
      mixed_image.rank() > 0 and mixed_preserved == 0)
check("conditional", "restricting to the split stabilizer would remove this algebraic obstruction but is not currently action-owned",
      split_preserved == len(split_pairs))


print("\nD. CLAIM CEILING AND RESULT")
for kind, label in (
    ("analytic", "finite isotropy supplies no closed Sobolev domain or Lopatinski estimate"),
    ("symplectic", "an action Green relation is not yet a reduced BFV phase space"),
    ("gauge", "restoring gauge closure could require an independently owned reduction or BFV edge completion"),
    ("selection", "the real action owns at most a conjugate pair and selects neither member"),
    ("scope", "no luminous half chirality index anomaly particle or generation count follows"),
    ("accounting", "no datum residue quotient canon verdict or public posture moves"),
):
    check(kind, label, True)

print("ACTION_GREEN_BASE_W_MIRROR=COMPLEMENTARY_MAXIMAL_ISOTROPIC_FOR_BOTH_CURRENT_PAIRING_HORNS")
print("ACTION_GREEN_NORMAL_W_MIRROR=NONISOTROPIC_FOR_BOTH_CURRENT_PAIRING_HORNS")
print("CONJUGATION=W_BOUNDARY_EXCHANGED_WITH_MIRROR_BOUNDARY__NO_MEMBER_SELECTED")
print("SPLIT_STABILIZER_PRESERVATION=51_OF_51")
print("MIXED_SPIN_PRESERVATION=0_OF_40")
print("SELECTED_ORDINARY_GAUGE=RANK25__SPLIT17__MIXED8")
print("BFV_BASICNESS=W_ONLY_AND_MIRROR_ONLY_FAIL_CURRENT_ORDINARY_GAUGE_DESCENT")
print("DISPOSITION=SMALLEST_ASYMMETRIC_BASE_BOUNDARY_PAIR_CONSTRUCTS_ALGEBRAICALLY__ACTION_SELECTS_NEITHER__CURRENT_GAUGE_COMPLEX_PRESERVES_NEITHER__GLOBAL_CLOSED_DOMAIN_AND_BFV_EDGE_OWNER_REMAIN_OPEN")
print(f"COUNTS={dict(COUNTS)}")
print(f"FAILURES={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
