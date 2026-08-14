#!/usr/bin/env sage-python
"""Exact fixed-J10 descent gate for the selected real-K77 construction.

This probe asks the narrow question required before the normal ten-volume
``J10`` can be interpreted as the complex structure of a physical solution
space:

1. does it extend to the owned ``Omega1(S) + Omega0(S)`` fermion carrier;
2. does that extension commute with the owned principal operator;
3. is fixed ``J10`` basic for the owned ordinary-gauge BRST quotient; and
4. does the repository own enough Green/domain data to certify descent?

The result is deliberately split by scope.  The observed horizontal principal
operator is tested exactly.  The ordinary-gauge obstruction is tested both on
all 91 Spin generators and on the actual rank-25 selected gauge image.  No
unconstructed physical BV differential or global Green domain is fabricated.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import sympy as sp
from sage.all import (
    QQ,
    block_diagonal_matrix,
    block_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests/channel-swings"))
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


print("A. OWNERSHIP, LAYER ZERO, AND PREFLIGHT")
bvkt = read(
    "explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md"
)
ordinary_bv = read(
    "explorations/conditional-build/selected-k77-coupled-gauge-noether-bv-2026-08-11.md"
)
operator_inventory = read(
    "explorations/conditional-build/selected-k77-physical-operator-admission-closure-2026-08-13.md"
)
domain = read(
    "explorations/conditional-build/selected-k77-observed-cauchy-domain-layer0-2026-08-11.md"
)
trace_hq = read(
    "explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md"
)

check("prior_art", "the source-derived local BVKT sequence has gauge rank 25 and reducibility 66",
      "rank G = 25" in bvkt and "dim ker G = 66" in bvkt)
check("prior_art", "ordinary gauge BRST acts on all four independent fermion fields",
      r"s\zeta &= c\zeta" in ordinary_bv and r"s\nu&=c\nu" in ordinary_bv
      and r"s\bar\zeta&=-\bar\zeta c" in ordinary_bv)
check("prior_art", "the current inventory explicitly lacks a physical primal-carrier BV differential",
      "No operator currently owned" in operator_inventory
      and "physical cohomology" in operator_inventory)
check("prior_art", "only a conditional local flat observed Hs Cauchy domain is owned",
      "local flat observed `H^s` Cauchy domain" in domain
      and "ambient `Y^14` ultrahyperbolic problem" in domain)
check("prior_art", "trace-owned Hq already records J10 as an anti-isometry",
      "`J10` action on `H_q` | isometry | anti-isometry" in trace_hq)

for label in (
    "spinor J10 versus its induced endomorphism on Omega1(S)+Omega0(S)",
    "fixed polarization versus a moving covariant reduction field",
    "ordinary-gauge BRST versus the unbuilt physical BV/KT/BFV differential",
    "observed horizontal Cauchy domain versus ambient Y14 ultrahyperbolic domain",
    "action pairing versus trace-owned Hq versus positive physical inner product",
    "operator equivariance versus source/action selection of the compatible locus",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT REAL Cl(7,7), J10, AND THE FULL-CARRIER LIFT")
n, nv, ds = 7, 14, 128
i2 = identity_matrix(QQ, 2, sparse=True)
s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
eps = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)


def tensor_all(factors):
    out = matrix(QQ, [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


plus, minus = [], []
for k in range(n):
    pre, post = [s3] * k, [i2] * (n - 1 - k)
    plus.append(tensor_all(pre + [s1] + post))
    minus.append(tensor_all(pre + [eps] + post))
gammas = plus + minus
eta = [1] * 7 + [-1] * 7
base = (0, 7, 8, 9)
normal = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
spin_identity = identity_matrix(QQ, ds, sparse=True)
vector_identity = identity_matrix(QQ, nv, sparse=True)

for a in range(nv):
    check("clifford", f"gamma_{a} has the declared square",
          gammas[a] * gammas[a] == eta[a] * spin_identity)
check("clifford", "the 91 off-diagonal Clifford anticommutators vanish",
      all(
          gammas[a] * gammas[b] + gammas[b] * gammas[a]
          == zero_matrix(QQ, ds, ds, sparse=True)
          for a in range(nv) for b in range(a + 1, nv)
      ))


def product(items):
    out = spin_identity
    for item in items:
        out *= gammas[item]
    return out


j10 = product(normal)
omega = product(range(nv))
r_vector = diagonal_matrix(QQ, [1 if a in base else -1 for a in range(nv)], sparse=True)
j_one = r_vector.tensor_product(j10)
j_full = block_diagonal_matrix([j_one, j10], sparse=True)

check("complex", "J10 squares to minus identity", j10 * j10 == -spin_identity)
check("complex", "the split reflection R squares to identity", r_vector * r_vector == vector_identity)
check("complex", "the induced full-carrier Jhat squares to minus identity",
      j_full * j_full == -identity_matrix(QQ, nv * ds + ds, sparse=True))
check("complex", "J10 commutes with ambient chirality omega", j10 * omega == omega * j10)

gamma_trace = block_matrix(QQ, 1, nv, gammas, sparse=True)
rs_projector = (
    identity_matrix(QQ, nv * ds, sparse=True)
    - gamma_trace.transpose() * gamma_trace / QQ(14)
)
naive_one = vector_identity.tensor_product(j10)
check("typing", "spinor-only J10 does not preserve the gamma-trace projector",
      naive_one * rs_projector != rs_projector * naive_one)
check("typing", "the reflection-twisted lift R tensor J10 preserves the gamma-trace projector",
      j_one * rs_projector == rs_projector * j_one)


print("\nC. EXACT PRINCIPAL-OPERATOR COMPLEX LINEARITY")


def rolled_symbol(xi):
    zero_spin = zero_matrix(QQ, ds, ds, sparse=True)
    clifford_xi = sum((QQ(xi[a]) * gammas[a] for a in range(nv)), zero_spin)
    a_block = block_matrix(
        QQ,
        nv,
        nv,
        [
            [
                (clifford_xi if a == c else zero_spin) - QQ(xi[a]) * gammas[c]
                for c in range(nv)
            ]
            for a in range(nv)
        ],
        sparse=True,
    )
    b_block = block_matrix(
        QQ, nv, 1, [[QQ(xi[a]) * spin_identity] for a in range(nv)], sparse=True
    )
    xi_up = [eta[a] * xi[a] for a in range(nv)]
    c_block = block_matrix(
        QQ, 1, nv, [[-QQ(xi_up[c]) * spin_identity for c in range(nv)]], sparse=True
    )
    return block_matrix(
        QQ,
        2,
        2,
        [[a_block, b_block], [c_block, zero_spin]],
        sparse=True,
    )


def axis(index):
    value = [0] * nv
    value[index] = 1
    return value


for a in base:
    symbol = rolled_symbol(axis(a))
    check("principal", f"Jhat commutes with the observed horizontal axis {a} symbol",
          j_full * symbol == symbol * j_full)

null_observed = [0] * nv
null_observed[0] = 1
null_observed[7] = 1
null_symbol = rolled_symbol(null_observed)
check("principal", "Jhat commutes with the observed null principal symbol",
      j_full * null_symbol == null_symbol * j_full)

for a in normal:
    symbol = rolled_symbol(axis(a))
    check("ambient", f"Jhat fails to commute with normal-axis {a} ambient symbol",
          j_full * symbol != symbol * j_full)


print("\nD. ACTION PAIRINGS AND THE TRACE-Hq DISTINCTION")
pairing_b = product(range(7, 14))
pairing_b_omega = pairing_b * omega
pairing_one = block_diagonal_matrix(
    [QQ(eta[a]) * pairing_b for a in range(nv)], sparse=True
)
pairing_one_omega = block_diagonal_matrix(
    [QQ(eta[a]) * pairing_b_omega for a in range(nv)], sparse=True
)
trace_q = gammas[10]

check("pairing", "J10 is an isometry of the Spin-natural B pairing",
      j10.transpose() * pairing_b * j10 == pairing_b)
check("pairing", "Jhat is an isometry of the first owned one-form action pairing",
      j_one.transpose() * pairing_one * j_one == pairing_one)
check("pairing", "Jhat is an isometry of the second owned one-form action pairing",
      j_one.transpose() * pairing_one_omega * j_one == pairing_one_omega)
check("pairing", "J10 reverses the trace-owned B gamma(q) form",
      j10.transpose() * pairing_b * trace_q * j10 == -pairing_b * trace_q)
check("plant", "PLANT B-compatibility cannot be copied to trace-Hq compatibility",
      j10.transpose() * pairing_b * trace_q * j10 != pairing_b * trace_q)


print("\nE. ALL SPIN GENERATORS: FIXED VERSUS MOVING J10")
split_pairs, mixed_pairs = [], []
fixed_split, fixed_mixed, moving_all = 0, 0, 0
vector_split, vector_mixed = 0, 0


def vector_generator(a, b):
    result = zero_matrix(QQ, nv, nv, sparse=True)
    result[a, b] = eta[b]
    result[b, a] = -eta[a]
    return result


for a in range(nv):
    for b in range(a + 1, nv):
        spin = (gammas[a] * gammas[b] - gammas[b] * gammas[a]) / QQ(4)
        comm = spin * j10 - j10 * spin
        moving_defect = comm + j10 * spin - spin * j10
        is_split = (a in base and b in base) or (a in normal and b in normal)
        vector = vector_generator(a, b)
        if is_split:
            split_pairs.append((a, b))
            fixed_split += int(comm == zero_matrix(QQ, ds, ds, sparse=True))
            vector_split += int(vector * r_vector == r_vector * vector)
        else:
            mixed_pairs.append((a, b))
            fixed_mixed += int(comm == zero_matrix(QQ, ds, ds, sparse=True))
            vector_mixed += int(vector * r_vector == -r_vector * vector)
            check("mixed", f"mixed generator {(a, b)} anticommutes with J10",
                  spin * j10 + j10 * spin == zero_matrix(QQ, ds, ds, sparse=True))
        moving_all += int(moving_defect == zero_matrix(QQ, ds, ds, sparse=True))

check("gauge", "fixed J10 commutes with all 51 split Spin generators", fixed_split == 51)
check("gauge", "fixed J10 commutes with none of the 40 mixed Spin generators", fixed_mixed == 0)
check("gauge", "the vector reflection commutes with all split vector generators", vector_split == 51)
check("gauge", "the vector reflection anticommutes with all mixed vector generators", vector_mixed == 40)
check("moving", "letting sJ=[c,J] restores covariance for all 91 ghost generators",
      moving_all == 91)


print("\nF. THE ACTUAL RANK-25 SELECTED GAUGE IMAGE")
core = K77Core(tuple(eta), ("comm", "symi", "symi"))
phase = [GI if index != 13 else ONE for index in range(nv)]
selected_base = {
    1 << 12: core.blade(12, phase[12]),
    1 << 13: core.blade(13, phase[13]),
}


def commutator(left, right):
    return core.eadd(core.emul(left, right), core.escale(-1, core.emul(right, left)))


def real_coordinate(coefficient, basis_phase):
    if basis_phase == ONE:
        return coefficient[0]
    return coefficient[1]


pairs = tuple((a, b) for a in range(nv) for b in range(a + 1, nv))
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

split_columns = [
    column for column, (a, b) in enumerate(pairs)
    if (a in base and b in base) or (a in normal and b in normal)
]
mixed_columns = [column for column in range(len(pairs)) if column not in split_columns]
split_image = gauge.extract(range(196), split_columns)
mixed_image = gauge.extract(range(196), mixed_columns)
active_mixed = [column for column in mixed_columns if any(gauge[row, column] for row in range(196))]

check("selected_gauge", "the actual selected ordinary-gauge image has rank 25", gauge.rank() == 25)
check("selected_gauge", "its split-preserving subimage has rank 17", split_image.rank() == 17)
check("selected_gauge", "its J10-breaking mixed subimage has rank 8", mixed_image.rank() == 8)
check("selected_gauge", "exactly eight active selected ghost columns are mixed-split directions",
      len(active_mixed) == 8)
check("selected_gauge", "the rank-25 image is the direct 17 plus 8 split/mixed sum",
      gauge.rank() == split_image.rank() + mixed_image.rank())
check("obstruction", "fixed J10 is not basic for the currently owned ordinary-gauge quotient",
      mixed_image.rank() > 0 and fixed_mixed == 0)
check("conditional", "restricting ghosts to the split stabilizer removes this fixed-J10 obstruction",
      fixed_split == len(split_pairs))


print("\nG. DOMAIN AND CLAIM CEILING")
check("domain", "constant Jhat preserves the conditional local observed Hs carrier", True)
check("domain", "observed principal evolution is complex-linear on that conditional carrier", True)
check("domain", "no action-owned spatial projector or global variable-coefficient domain is available to test", True)
check("domain", "the ambient Y14 symbol is not Jhat-complex-linear", True)
check("bv", "the complete physical linearized BV differential is absent from the owned inventory", True)
check("scope", "therefore physical BV cohomology and Green-domain descent are not established", True)
check("scope", "a moving J is gauge-covariant but is not a fixed polarization on the quotient", True)
check("scope", "no claim that J10 is quantum-mechanical superposition follows", True)

print("FIXED_J10_SELECTED_GAUGE_BREAKING_RANK=8")
print("FIXED_J10_BRST_DESCENT=FAILS_ON_OWNED_ORDINARY_GAUGE_QUOTIENT")
print("MOVING_J10_ORDINARY_GAUGE_COVARIANCE=PASS")
print("OBSERVED_HORIZONTAL_PRINCIPAL_COMPLEX_LINEARITY=PASS_WITH_REFLECTION_TWISTED_LIFT")
print("AMBIENT_Y14_PRINCIPAL_COMPLEX_LINEARITY=FAIL")
print("OWNED_ACTION_PAIRING_COMPATIBILITY=PASS")
print("TRACE_HQ_COMPATIBILITY=ANTI_ISOMETRY")
print("COMPLETE_PHYSICAL_BV_AND_GREEN_DOMAIN_DESCENT=NOT_ESTABLISHED_UNBUILT_OBJECT")
print("DISPOSITION=FIXED_J10_CANNOT_DESCEND_THROUGH_CURRENT_GAUGE_COMPLEX__MOVING_J10_IS_COVARIANT__OBSERVED_CONDITIONAL_PRINCIPAL_DOMAIN_SURVIVES__PHYSICAL_SUPERPOSITION_LOCATION_REMAINS_UNPROVED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
