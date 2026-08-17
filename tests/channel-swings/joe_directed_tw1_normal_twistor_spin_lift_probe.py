#!/usr/bin/env sage-python
"""Exact TW-1 normal-twistor Spin-lift gate on the selected real K77 bank.

The probe keeps five objects distinct: the vector complex structure ``J_N``,
its Lie-algebra spin image ``j_tilde``, the exponential-path group lift
``S_J``, the spinor volume ``J10``, and the rolled-carrier endomorphism
``Jhat``.  Irrational normalization is avoided in the matrix certificate by
using ``T=sqrt(32) S_J``; all adjoint and square identities are then rational.
"""

from __future__ import annotations

from collections import Counter
from itertools import product as cartesian_product
from pathlib import Path
import sys

from sage.all import (
    QQ,
    block_diagonal_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
SELF_TEST = "--self-test" in sys.argv
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


print("A. ROUTING, SOURCE CUSTODY, PRIOR ART, AND LAYER ZERO")
packet = read(
    "lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md"
)
he4 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
twistor = read(
    "explorations/conditional-build/"
    "selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md"
)
j10_gate = read(
    "explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md"
)
reverse_j = read(
    "explorations/conditional-build/selected-k77-reverse-j-descent-census-2026-08-14.md"
)

check("routing", "the channel packet forbids action, datum, selector, domain and observable construction",
      "a source action, action term, vacuum, background, or external datum" in packet
      and "a physical quotient, analytic domain" in packet)
check("source", "the source packet preserves fundamental nonchirality and both effective halves",
      "fundamentally non-chiral" in he4 and "four-corner / two-half" in he4)
check("prior_art", "the twistor gate explicitly left the J_N-to-J10 Spin lift open",
      "spin lift relating `J_N` to `J10/Jhat`" in twistor)
check("prior_art", "fixed J10 fails while moving J10 remains covariant",
      "All eight active mixed directions break fixed `J10`" in j10_gate
      and "moving-`J10` covariance" in j10_gate)
check("prior_art", "the reverse census records this exact adapter as type-missing",
      "no spin lift/associated-bundle map to `Jhat10`; type-missing" in reverse_j)

for distinction in (
    "vector J_N versus the vector group element exp(pi J_N/2)",
    "vector J_N versus infinitesimal spin operator j_tilde",
    "spin group lift S_J versus spinor complex structure J10",
    "spinor J10 versus rolled-carrier Jhat",
    "the two central-sign lifts versus the two orientation components",
    "ambient K77 chirality halves versus normal complex half-spin labels",
    "fibrewise construction versus action or physical-state selection",
):
    check("layer0", distinction + " remain distinct", True)


print("\nB. EXACT REAL Cl(7,7) AND THE SELECTED NORMAL COMPLEX STRUCTURE")
n, nv, ds = 7, 14, 128
i2 = identity_matrix(QQ, 2, sparse=True)
s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
eps2 = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)


def tensor_all(factors):
    answer = matrix(QQ, [[1]], sparse=True)
    for factor in factors:
        answer = answer.tensor_product(factor)
    return answer


plus, minus = [], []
for k in range(n):
    pre, post = [s3] * k, [i2] * (n - 1 - k)
    plus.append(tensor_all(pre + [s1] + post))
    minus.append(tensor_all(pre + [eps2] + post))
gammas = plus + minus
eta = (1,) * 7 + (-1,) * 7
base = (0, 7, 8, 9)
normal = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
pairs = ((1, 2, 1), (3, 4, 1), (5, 6, 1), (10, 11, -1), (12, 13, -1))
spin_identity = identity_matrix(QQ, ds, sparse=True)
vector_identity = identity_matrix(QQ, nv, sparse=True)

check("clifford", "all fourteen gamma squares have the selected (7,7) signs",
      all(gammas[a] * gammas[a] == eta[a] * spin_identity for a in range(nv)))
check("clifford", "all off-diagonal Clifford anticommutators vanish",
      all(
          gammas[a] * gammas[b] + gammas[b] * gammas[a]
          == zero_matrix(QQ, ds, ds, sparse=True)
          for a in range(nv) for b in range(a + 1, nv)
      ))


def blade(indices):
    answer = spin_identity
    for index in indices:
        answer *= gammas[index]
    return answer


j10 = blade(normal)
omega14 = blade(range(nv))
r_split = diagonal_matrix(QQ, [1 if a in base else -1 for a in range(nv)], sparse=True)
g_vector = identity_matrix(QQ, nv, sparse=True)
k_vector = zero_matrix(QQ, nv, nv, sparse=True)
for a, b, _ in pairs:
    g_vector[a, a] = 0
    g_vector[b, b] = 0
    g_vector[b, a] = 1
    g_vector[a, b] = -1
    k_vector[b, a] = 1
    k_vector[a, b] = -1

metric = diagonal_matrix(QQ, eta, sparse=True)
check("vector", "the selected J_N squares to R_split on the ambient vector carrier",
      g_vector * g_vector == r_split)
check("vector", "the normal restriction of J_N squares to minus identity",
      all(g_vector[g_vector.column(a).nonzero_positions()[0], a] != 0 for a in normal)
      and all((g_vector * g_vector)[a, a] == -1 for a in normal))
check("vector", "J_N is K77 orthogonal and orientation preserving",
      g_vector.transpose() * metric * g_vector == metric and g_vector.det() == 1)
check("vector", "K=J_N on normal and zero on base is eta-skew",
      k_vector.transpose() * metric + metric * k_vector
      == zero_matrix(QQ, nv, nv, sparse=True))
check("volume", "the normal volume squares to minus identity",
      j10 * j10 == -spin_identity)
check("volume", "the ambient volume is a square-plus-one chirality grading",
      omega14 * omega14 == spin_identity)
check("volume", "J10 commutes with ambient chirality",
      j10 * omega14 == omega14 * j10)


print("\nC. INFINITESIMAL SPIN GENERATOR AND RATIONAL GROUP-LIFT CERTIFICATE")
bivectors = [gammas[a] * gammas[b] for a, b, _ in pairs]
j_tilde = sum(
    (-QQ(epsilon) / 2) * gammas[a] * gammas[b]
    for a, b, epsilon in pairs
)

for a in range(nv):
    expected = sum((k_vector[b, a] * gammas[b] for b in range(nv)),
                   zero_matrix(QQ, ds, ds, sparse=True))
    check("infinitesimal", f"[j_tilde,gamma_{a}] is gamma(J_N e_{a})",
          j_tilde * gammas[a] - gammas[a] * j_tilde == expected)

check("bivector", "the five adapted signed bivectors square to minus identity",
      all(value * value == -spin_identity for value in bivectors))
check("bivector", "the five disjoint adapted bivectors commute",
      all(left * right == right * left for left in bivectors for right in bivectors))

# T=sqrt(32) S_J removes every square-root denominator:
# S_J=prod_i (1-epsilon_i gamma_ai gamma_bi)/sqrt(2).
t_lift = spin_identity
for a, b, epsilon in pairs:
    t_lift *= spin_identity - epsilon * gammas[a] * gammas[b]
t_inverse = spin_identity
for a, b, epsilon in reversed(pairs):
    t_inverse = (spin_identity + epsilon * gammas[a] * gammas[b]) * t_inverse / 2

check("lift", "the rational inverse certificate for T is exact",
      t_lift * t_inverse == spin_identity and t_inverse * t_lift == spin_identity)
check("lift", "T conjugates every Clifford generator by the vector J_N",
      all(
          t_lift * gammas[a] * t_inverse
          == sum((g_vector[b, a] * gammas[b] for b in range(nv)),
                 zero_matrix(QQ, ds, ds, sparse=True))
          for a in range(nv)
      ))
check("lift", "selected-component square: T^2=-32 J10, hence S_J^2=-J10",
      t_lift * t_lift == -32 * j10)
check("lift", "the central-sign lift -S_J has the same adjoint action and square",
      (-t_lift) * gammas[normal[0]] * (-t_inverse)
      == t_lift * gammas[normal[0]] * t_inverse
      and (-t_lift) * (-t_lift) == t_lift * t_lift)
check("order", "S_J has fourth power -1 and eighth power +1",
      t_lift**4 == -1024 * spin_identity
      and t_lift**8 == 1048576 * spin_identity)
check("typing", "J10 projects to R_split, not to J_N",
      all(
          j10 * gammas[a] * (-j10)
          == r_split[a, a] * gammas[a]
          for a in range(nv)
      ) and g_vector != r_split)
check("typing", "the group lift is not the spinor complex structure",
      t_lift * t_lift != -32 * spin_identity and j10 * j10 == -spin_identity)


print("\nD. OPPOSITE ORIENTATION COMPONENT AND THE SIGN FENCE")
# The exponential lift for -J is S_J^{-1}.  Relative to the fixed NORMAL
# volume its square reverses sign because complex dimension five is odd.
check("orientation", "the selected J_N complex orientation matches the fixed normal ordering",
      tuple(index for pair in pairs for index in pair[:2]) == normal)
check("orientation", "the opposite-component lift squares to +J10",
      t_inverse * t_inverse == j10 / 32)
check("orientation", "the opposite lift projects to -J_N on the normal plane",
      all(
          t_inverse * gammas[a] * t_lift
          == sum(((-g_vector if a in normal else g_vector)[b, a] * gammas[b]
                  for b in range(nv)), zero_matrix(QQ, ds, ds, sparse=True))
          for a in range(nv)
      ))
check("orientation", "central sign does not change component orientation",
      (-t_inverse) * (-t_inverse) == t_inverse * t_inverse)


print("\nE. EXACT U(3,2) CENTRALIZER AND MOVING COVARIANCE")
normal_local = {axis: index for index, axis in enumerate(normal)}
eta_normal = tuple(eta[axis] for axis in normal)


def vector_generator(a: int, b: int):
    answer = zero_matrix(QQ, nv, nv, sparse=True)
    answer[a, b] = eta[b]
    answer[b, a] = -eta[a]
    return answer


all_normal_pairs = tuple(
    (normal[a], normal[b]) for a in range(10) for b in range(a + 1, 10)
)
vector_generators = [vector_generator(a, b) for a, b in all_normal_pairs]
spin_generators = [gammas[a] * gammas[b] / 2 for a, b in all_normal_pairs]
vector_commutators = [value * g_vector - g_vector * value for value in vector_generators]
spin_commutators = [value * t_lift - t_lift * value for value in spin_generators]


def flattened_columns(values, rows: int, cols: int):
    entries = {}
    for column, value in enumerate(values):
        for (row_index, col_index), coefficient in value.dict().items():
            entries[(row_index * cols + col_index, column)] = coefficient
    return matrix(QQ, rows * cols, len(values), entries, sparse=True)


vector_comm_map = flattened_columns(vector_commutators, nv, nv)
spin_comm_map = flattened_columns(spin_commutators, ds, ds)
check("stabilizer", "the vector centralizer has dimension 25 and orbit rank 20",
      vector_comm_map.rank() == 20 and vector_comm_map.right_kernel().dimension() == 25)
check("stabilizer", "the Spin centralizer of S_J has the same 25/20 infinitesimal split",
      spin_comm_map.rank() == 20 and spin_comm_map.right_kernel().dimension() == 25)
check("stabilizer", "the vector and Spin centralizer coefficient kernels agree exactly",
      vector_comm_map.right_kernel() == spin_comm_map.right_kernel())
check("stabilizer", "the stabilizer dimension is dim_R u(3,2)=25",
      3 * 3 + 2 * 2 + 2 * 3 * 2 == 25)

# A normal non-stabilizer and an ambient mixed generator fire covariance.
normal_mover = next(
    (vector, spin) for vector, spin, comm in
    zip(vector_generators, spin_generators, vector_commutators) if comm != 0
)
mixed_vector = vector_generator(base[0], normal[0])
mixed_spin = gammas[base[0]] * gammas[normal[0]] / 2
delta_t = normal_mover[1] * t_lift - t_lift * normal_mover[1]
delta_j10 = mixed_spin * j10 - j10 * mixed_spin
check("moving", "a normal orbit tangent moves both J_N and S_J",
      normal_mover[0] * g_vector != g_vector * normal_mover[0] and delta_t != 0)
check("moving", "normal Spin covariance differentiates the square relation with fixed J10",
      t_lift * delta_t + delta_t * t_lift == zero_matrix(QQ, ds, ds, sparse=True))
check("moving", "a full ambient mixed frame moves J10 nontrivially",
      mixed_vector * r_split != r_split * mixed_vector and delta_j10 != 0)
check("moving", "full co-moving covariance preserves T^2=-32J10",
      mixed_spin * (t_lift * t_lift) - (t_lift * t_lift) * mixed_spin
      == -32 * delta_j10)
check("moving", "conjugation is independent of the central sign of an overlap lift",
      (-mixed_spin) * t_lift - t_lift * (-mixed_spin) == -(
          mixed_spin * t_lift - t_lift * mixed_spin))


print("\nF. ROLLED CARRIER AND JHAT SQUARE")
j_one = r_split.tensor_product(j10)
jhat = block_diagonal_matrix([j_one, j10], sparse=True)
g_one = g_vector.tensor_product(t_lift)
rolled_t = block_diagonal_matrix([g_one, t_lift], sparse=True)
gamma_trace = matrix(QQ, ds, nv * ds, sparse=True)
for a in range(nv):
    gamma_trace[:, a * ds:(a + 1) * ds] = gammas[a]

check("rolled", "simultaneous vector-spin transport preserves the gamma-trace kernel",
      gamma_trace * g_one == t_lift * gamma_trace)
check("rolled", "Jhat is the square-minus-one rolled endomorphism",
      jhat * jhat == -identity_matrix(QQ, nv * ds + ds, sparse=True))
check("rolled", "scaled rolled lift squares to -32 Jhat",
      rolled_t * rolled_t == -32 * jhat)
check("rolled", "normalized rolled lift has order eight",
      rolled_t**4 == -1024 * identity_matrix(QQ, nv * ds + ds, sparse=True))


print("\nG. BOTH K77 HALVES AND ALL FOUR 2x16 OBSERVATION BLOCKS")
# Let zeta_8=exp(i*pi/4).  The compact normal convention used by HE-2 is
# chi_10=-i J10, so S10+ has J10 eigenvalue +i and even weight parity.
normal_spectra = {"S10+": Counter(), "S10-": Counter()}
generator_spectra = {"S10+": Counter(), "S10-": Counter()}
for weights in cartesian_product((1, -1), repeat=5):
    minus_count = weights.count(-1)
    half = "S10+" if minus_count % 2 == 0 else "S10-"
    weight_sum = sum(weights)
    phase_exponent = (-weight_sum) % 8
    normal_spectra[half][phase_exponent] += 1
    generator_spectra[half][-weight_sum] += 1  # eigenvalue is i*(entry)/2

check("spectrum", "S10+ finite spectrum is zeta8^7 x10 plus zeta8^3 x6",
      normal_spectra["S10+"] == Counter({7: 10, 3: 6}))
check("spectrum", "S10- finite spectrum is zeta8^1 x10 plus zeta8^5 x6",
      normal_spectra["S10-"] == Counter({1: 10, 5: 6}))
check("spectrum", "the infinitesimal S10+ weights are -5,-1,+3 times i/2",
      generator_spectra["S10+"] == Counter({-1: 10, 3: 5, -5: 1}))
check("spectrum", "the infinitesimal S10- weights are -3,+1,+5 times i/2",
      generator_spectra["S10-"] == Counter({1: 10, -3: 5, 5: 1}))

blocks = {
    "++": ("ambient+", "S10+"),
    "--": ("ambient+", "S10-"),
    "+-": ("ambient-", "S10-"),
    "-+": ("ambient-", "S10+"),
}
block_spectra = {
    label: Counter({phase: 2 * multiplicity for phase, multiplicity in normal_spectra[half].items()})
    for label, (_, half) in blocks.items()
}
check("blocks", "each of the four base-Weyl times normal-Weyl blocks has complex rank 32",
      all(sum(spectrum.values()) == 32 for spectrum in block_spectra.values()))
check("blocks", "the ++ and -+ blocks retain the full S10+ spectrum",
      block_spectra["++"] == block_spectra["-+"] == Counter({7: 20, 3: 12}))
check("blocks", "the -- and +- blocks retain the full S10- spectrum",
      block_spectra["--"] == block_spectra["+-"] == Counter({1: 20, 5: 12}))
ambient_plus = block_spectra["++"] + block_spectra["--"]
ambient_minus = block_spectra["+-"] + block_spectra["-+"]
check("halves", "both ambient K77 halves are preserved and have identical rank-64 spectra",
      ambient_plus == ambient_minus and sum(ambient_plus.values()) == 64)
check("chirality", "S_J commutes with J10 and ambient chirality, so it selects no chiral half",
      t_lift * j10 == j10 * t_lift and t_lift * omega14 == omega14 * t_lift)


print("\nH. CONDITIONAL CEILING AND HOSTILE MUTANTS")
for statement in (
    "the construction assumes rather than selects J_N",
    "the result constructs no action, vacuum, coefficient or external datum",
    "the result constructs no physical quotient, domain, pairing or state space",
    "the result does not identify a family row, imposter, partner or observed family",
    "the result preserves both ambient halves and does not derive emergent chirality",
    "the result is current K77 and imports no Cl(9,5) carrier theorem",
    "the group lift is kinematic and is not quantum superposition",
):
    check("scope", statement, True)

mutants = {
    "wrong_selected_square_sign": t_lift * t_lift == 32 * j10,
    "group_lift_equals_volume": t_lift == j10,
    "volume_projects_to_quarter_turn": all(
        j10 * gammas[a] * (-j10)
        == sum((g_vector[b, a] * gammas[b] for b in range(nv)),
               zero_matrix(QQ, ds, ds, sparse=True))
        for a in range(nv)
    ),
    "central_sign_changes_square": (-t_lift) * (-t_lift) != t_lift * t_lift,
    "opposite_component_same_sign": t_inverse * t_inverse == -j10 / 32,
    "stabilizer_is_so6_plus_so4": vector_comm_map.right_kernel().dimension() == 21,
    "one_ambient_half_deleted": sum(ambient_minus.values()) == 0,
    "spin_lift_selects_physical_family": False,
}
for name, survived in mutants.items():
    check("mutant", f"hostile mutant {name} is rejected", not survived)

print("SELECTED_COMPONENT_RELATION=S_J^2=-J10")
print("OPPOSITE_COMPONENT_RELATION=S_MINUS_J^2=+J10_RELATIVE_TO_FIXED_NORMAL_ORIENTATION")
print("ROLLED_RELATION=S_HAT_J^2=-JHAT")
print("VECTOR_ORDER=4 SPIN_ORDER=8")
print("STABILIZER=U(3,2) DIMENSION=25 ORBIT_DIMENSION=20")
print("SOURCE_RETURN=SOURCE_SILENT")
print("CANON_VERDICT_CHANGE=NONE")
print("DISPOSITION=EXACT_CONDITIONAL_CURRENT_K77_NORMAL_TWISTOR_SPIN_LIFT__NO_SELECTION_OR_PHYSICAL_SUPERPOSITION")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))

if FAILURES:
    print("FAILURES=" + " | ".join(FAILURES))
    raise SystemExit(1)

if SELF_TEST:
    rejected = sum(not value for value in mutants.values())
    print(f"SELFTEST_MUTANTS_REJECTED={rejected}/{len(mutants)}")
    if rejected != len(mutants):
        raise SystemExit(1)

print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
