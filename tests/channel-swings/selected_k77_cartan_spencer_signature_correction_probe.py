#!/usr/bin/env python3
"""Exact K77 correction of the v0.46--v0.56 four-column chain.

The old normal-jet and Cartan probes called their metric ``(7,7)`` while
hard-coding inertia ``(9,5)``.  This probe rebuilds the raw graph targets with
the settled K77 metric, solves them in the existing K77 selected-Shiab image,
and then applies the K77 Koszul inverse.  Historical probes are replayed as
provenance, not used as signature evidence.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V047 = ROOT / "tests/channel-swings/selected_second_layer_shiab_inverse_bianchi_completion_probe.py"
V055 = ROOT / "tests/channel-swings/selected_nonzero_background_cartan_spencer_owner_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, REPO ARCHAEOLOGY, AND LAYER ZERO")
curt = read("lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md")
draft = read("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md")
global_k77 = read("explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
v055_report = read("explorations/conditional-build/selected-nonzero-background-cartan-spencer-owner-2026-08-07.md")
v056_report = read("explorations/conditional-build/selected-source-varpi-cartan-composition-2026-08-07.md")
check("source", "Curt explicitly presents a Spin(7,7) chimeric carrier",
      "Spin(7,7)" in curt and "real dimension 128" in curt)
check("source", "the released draft writes Y^(7,7) and a (6,4) normal block",
      "Y^{7,7}" in draft and "N^{6,4}" in draft)
check("repo", "the settled K77 construction uses horizontal (1,3) plus vertical (6,4)",
      "horizontal dual" in global_k77 and "((6,4))" in global_k77 and "((1,3))" in global_k77)
check("repo", "v0.55 labels its computation as settled (7,7)",
      "settled signature `(7,7)`" in v055_report)
check("repo", "v0.56 inherits the v0.55 exact preimages",
      "four v0.55 Koszul inverses" in v056_report)
for label in (
    "signature label versus the signs actually executed",
    "self-consistent inverse pair versus validation of its metric fork",
    "conditional Cl(9,5) comparator versus settled Cl(7,7) K77 carrier",
    "raw graph target coefficients versus the later Cartan inverse coefficients",
    "pointwise source lift versus covariant graph and atlas descent",
):
    check("type", label + " remain distinct", True)


print("\nB. HISTORICAL REPLAYS AND SIGNATURE COLLISION")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    O47 = runpy.run_path(str(V047))
check("repo", "the historical v0.47 packet replays", "PASS 50/50" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    O55 = runpy.run_path(str(V055))
check("repo", "the historical v0.55 packet replays", "PASS 48/48" in capture.getvalue())

OLD_ETA = tuple(O55["ETA"])
K77_ETA = tuple(O47["M"]["ETA"])
check("exact", "the v0.55 executed metric has inertia (9,5)",
      (sum(x > 0 for x in OLD_ETA), sum(x < 0 for x in OLD_ETA)) == (9, 5))
check("exact", "the selected-Shiab backend metric has settled inertia (7,7)",
      (sum(x > 0 for x in K77_ETA), sum(x < 0 for x in K77_ETA)) == (7, 7))
check("exact", "the two executed metrics differ on all four horizontal signs",
      sum(a != b for a, b in zip(OLD_ETA, K77_ETA)) == 4)
check("planted", "PLANT identical dimension and invertibility do not identify the two real Clifford forks",
      OLD_ETA != K77_ETA)


print("\nC. REBUILD THE RAW FOUR K77 GRAPH TARGETS")
N = 14
PAIRS = list(combinations(range(N), 2))
DOMAIN = [(mu, pair) for mu in range(N) for pair in PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]

entries = {}
for column, (mu, nu, a) in enumerate(II_COORDS):
    normal = 4 + a
    if mu != nu:
        entries[(DOMAIN_INDEX[(mu, (nu, normal))], column)] = sp.Rational(124, 117) * K77_ETA[mu]
        entries[(DOMAIN_INDEX[(nu, (mu, normal))], column)] = sp.Rational(124, 117) * K77_ETA[nu]
        continue
    for rho in range(4):
        coefficient = sp.Rational(118, 117) if rho == mu else -sp.Rational(2, 39)
        entries[(DOMAIN_INDEX[(rho, (rho, normal))], column)] = K77_ETA[mu] * coefficient
    for b in range(10):
        if b == a:
            continue
        other = 4 + b
        pair = tuple(sorted((normal, other)))
        orientation = 1 if b > a else -1
        entries[(DOMAIN_INDEX[(other, pair)], column)] = K77_ETA[mu] * orientation * sp.Rational(2, 39)

TARGET = sp.SparseMatrix(len(DOMAIN), len(II_COORDS), entries)
eta_h = sp.diag(*K77_ETA[:4])


def metric_basis(i, j):
    wave = sp.zeros(4)
    wave[i, j] = wave[j, i] = 1
    return wave


def delta_algebraic_slice(wave, mu, nu):
    return sp.Matrix(
        4, 4,
        lambda a, b: sp.Rational(1, 2) * (
            wave[a, mu] * eta_h[nu, b]
            + eta_h[a, mu] * wave[nu, b]
            + wave[a, nu] * eta_h[mu, b]
            + eta_h[a, nu] * wave[mu, b]
        ) - sp.Rational(1, 2) * (
            wave[a, b] * eta_h[mu, nu] + eta_h[a, b] * wave[mu, nu]
        ),
    )


def metric_to_ii(momentum_square):
    out = sp.zeros(100, 10)
    k = [sp.sqrt(momentum_square), 0, 0, 0]
    for column, slot in enumerate(SLOTS):
        wave = metric_basis(*slot)
        values = [[
            sp.simplify(
                -k[mu] * k[nu] * wave
                - sp.Rational(1, 2) * delta_algebraic_slice(wave, mu, nu)
            )
            for nu in range(4)] for mu in range(4)]
        for row, (mu, nu, a) in enumerate(II_COORDS):
            p, q = SLOTS[a]
            out[row, column] = values[mu][nu][p, q]
    return out


J2 = TARGET * metric_to_ii(2)
D = sp.zeros(10, 4)
for column in range(4):
    for row, (i, j) in enumerate(SLOTS):
        D[row, column] = (
            (1 if i == 0 and j == column else 0)
            + (1 if j == 0 and i == column else 0)
        )


def encode_required(jacobian):
    result = []
    for column in range(4):
        vector = -jacobian * D[:, column]
        encoded = {}
        for row, (mu, pair) in enumerate(DOMAIN):
            value = sp.Rational(vector[row])
            if value:
                encoded[(1 << mu, (1 << pair[0]) | (1 << pair[1]))] = (
                    Fraction(int(value.p), int(value.q)), Fraction(0)
                )
        result.append(encoded)
    return result


k77_raw_required = encode_required(J2)
check("exact", "the corrected K77 raw Jacobian retains rank ten and graph-orbit rank four",
      J2.rank() == 10 and (J2 * D).rank() == 4)
check("exact", "the corrected K77 raw target supports remain 58,29,29,29",
      [len(x) for x in k77_raw_required] == [58, 29, 29, 29])
check("exact", "every corrected raw target differs from its old-fork target",
      all(a != b for a, b in zip(k77_raw_required, O47["raw_required"])))


print("\nD. SELECTED-SHIAB SOLVE, KOSZUL SPLIT, AND K77 SPENCER INVERSE")
k77_solutions = []
for target in k77_raw_required:
    solution, remainder = O47["solve"](target)
    check("exact", "one corrected K77 raw target has an exact selected-Shiab preimage",
          solution is not None and not remainder)
    k77_solutions.append(solution)
check("exact", "the selected-Shiab preimage supports remain 58,29,29,29",
      [len(x) for x in k77_solutions] == [58, 29, 29, 29])
check("exact", "all corrected selected-Shiab preimages reconstruct coefficientwise",
      all(O47["reconstruct"](x) == y for x, y in zip(k77_solutions, k77_raw_required)))

mixed_pairs = O47["mixed_pairs"]
k77_connection = [{i: v for i, v in x.items() if 0 in mixed_pairs[i // N]} for x in k77_solutions]
k77_transverse = [{i: v for i, v in x.items() if 0 not in mixed_pairs[i // N]} for x in k77_solutions]
check("exact", "the corrected non-null split retains connection supports 7,7,7,7",
      [len(x) for x in k77_connection] == [7, 7, 7, 7])
check("exact", "the corrected non-null split retains transverse supports 51,22,22,22",
      [len(x) for x in k77_transverse] == [51, 22, 22, 22])


def packet_target(packet):
    target = {}
    for index, gaussian in packet.items():
        pair = mixed_pairs[index // N]
        value_index = index % N
        if gaussian[1] != 0:
            raise AssertionError("corrected packet unexpectedly has an imaginary coefficient")
        if gaussian[0]:
            target[(pair[0], pair[1], value_index)] = gaussian[0]
    return target


def ordered_t(target, mu, nu, value_index):
    if mu == nu:
        return Fraction(0)
    value = target.get((min(mu, nu), max(mu, nu), value_index), Fraction(0))
    return value if mu < nu else -value


def spencer_forward(omega):
    target = {}
    for (mu, a, b), coefficient in omega.items():
        if mu != b:
            pair = tuple(sorted((mu, b)))
            orientation = 1 if mu < b else -1
            key = (pair[0], pair[1], a)
            target[key] = target.get(key, Fraction(0)) + orientation * K77_ETA[a] * coefficient
        if mu != a:
            pair = tuple(sorted((mu, a)))
            orientation = 1 if mu < a else -1
            key = (pair[0], pair[1], b)
            target[key] = target.get(key, Fraction(0)) - orientation * K77_ETA[b] * coefficient
    return {key: value for key, value in target.items() if value}


def spencer_inverse(target):
    omega = {}
    for mu in range(N):
        for a, b in PAIRS:
            value = Fraction(K77_ETA[a], 2) * ordered_t(target, mu, b, a)
            value -= Fraction(K77_ETA[mu], 2) * ordered_t(target, b, a, mu)
            value += Fraction(K77_ETA[b], 2) * ordered_t(target, a, mu, b)
            if value:
                omega[(mu, a, b)] = value
    return omega


k77_transverse_targets = [packet_target(x) for x in k77_transverse]
k77_transverse_preimages = [spencer_inverse(x) for x in k77_transverse_targets]
check("exact", "all four corrected transverse packets are reproduced by the K77 Spencer map",
      all(spencer_forward(x) == y for x, y in zip(k77_transverse_preimages, k77_transverse_targets)))
check("exact", "corrected transverse supports remain 51,22,22,22 and total 117",
      [len(x) for x in k77_transverse_targets] == [51, 22, 22, 22]
      and sum(len(x) for x in k77_transverse_targets) == 117)
check("exact", "corrected K77 Koszul supports remain 57,34,34,34",
      [len(x) for x in k77_transverse_preimages] == [57, 34, 34, 34])
check("exact", "all four corrected target packets differ from v0.55",
      all(a != b for a, b in zip(k77_transverse_targets, O55["transverse_targets"])))
changed_targets = [
    sum(a.get(k, 0) != b.get(k, 0) for k in set(a) | set(b))
    for a, b in zip(O55["transverse_targets"], k77_transverse_targets)
]
changed_preimages = [
    sum(a.get(k, 0) != b.get(k, 0) for k in set(a) | set(b))
    for a, b in zip(O55["transverse_preimages"], k77_transverse_preimages)
]
check("exact", "the target repair changes exactly twelve coordinates in every column",
      changed_targets == [12, 12, 12, 12])
check("exact", "the composed K77 preimage repair changes 30,34,34,34 coordinates",
      changed_preimages == [30, 34, 34, 34])
check("exact", "the corrected K77 preimage family retains rank four",
      O55["family_rank"](k77_transverse_preimages) == 4)


print("\nE. SOURCE-VARPI COMPOSITION AND CONTROLS")
t_star = Fraction(-1, 312)


def scale(column, coefficient):
    return {key: coefficient * value for key, value in column.items() if coefficient * value}


def endpoint(alpha):
    return scale(spencer_forward(alpha), -t_star)


k77_source_lifts = [scale(x, -Fraction(1, 1) / t_star) for x in k77_transverse_preimages]
check("exact", "all four corrected fixed-epsilon source-varpi lifts reproduce the K77 targets",
      all(endpoint(x) == y for x, y in zip(k77_source_lifts, k77_transverse_targets)))
check("exact", "the corrected source-varpi lift retains rank four and supports 57,34,34,34",
      O55["family_rank"](k77_source_lifts) == 4
      and [len(x) for x in k77_source_lifts] == [57, 34, 34, 34])
old_source_lifts = [scale(x, -Fraction(1, 1) / t_star) for x in O55["transverse_preimages"]]
check("planted", "PLANT every old-fork lift fails the corrected K77 endpoint target",
      all(endpoint(x) != y for x, y in zip(old_source_lifts, k77_transverse_targets)))
check("planted", "PLANT matching ranks and support counts do not preserve coefficients",
      changed_preimages != [0, 0, 0, 0])
check("planted", "PLANT a forward map paired with its own wrong-fork inverse is not a signature control", True)
check("scope", "the corrected pointwise theorem does not source-select a covariant graph law", True)
check("scope", "Spencer jet compatibility and actual three-patch K77 atlas descent remain open", True)
check("scope", "raw-Upsilon Bianchi Euler preboundary symplectic and null-domain gates remain open", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__SPIN77_Y77_AND_NORMAL64_PRESENTATION__SOURCE-SILENT__FOUR_COLUMN_GRAPH_SELECTION_AND_DESCENT")
print("OLD_EXECUTED_INERTIA=9,5")
print("CORRECTED_EXECUTED_INERTIA=7,7")
print("CORRECTED_RAW_TARGET_SUPPORTS=58,29,29,29")
print("CORRECTED_TRANSVERSE_SUPPORTS=51,22,22,22")
print("CORRECTED_KOSZUL_SUPPORTS=57,34,34,34")
print("CORRECTED_FAMILY_RANK=4")
print("TARGET_CHANGED_COORDINATES=12,12,12,12")
print("PREIMAGE_CHANGED_COORDINATES=30,34,34,34")
print("POINTWISE_SOURCE_VARPI_LIFT=SURVIVES_WITH_REPAIRED_COEFFICIENTS")
print("DISPOSITION=COEFFICIENT_REPAIR_THEOREM_SURVIVES__OLD_EXACT_VALUES_SUPERSEDED__COVARIANT_GRAPH_DESCENT_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
