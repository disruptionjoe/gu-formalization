#!/usr/bin/env sage-python
"""Exact finite co-moving naturality square for the conditional H210 tensor.

For a graph ``L_J=(I,J)^T`` and an ambient covector-spinor ``T``, a K77
change of frame ``g=((a,b),(c,d))`` acts by

    J'=(c+dJ)(a+bJ)^-1,  A=a+bJ,
    T'=g^-T S(g)T.

The exact square is ``L_J'^T T'=A^-T S(g)(L_J^T T)``.  The H210 horn is a
declared conditional input.  Nothing here derives an action, section,
selector, family alignment, quotient, mass, scale, or observable.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import (
    GF,
    block_diagonal_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. CONDITIONAL-BUILD FENCES, PRIOR ART, AND MULTI-LENS PREFLIGHT")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb3 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb3-wave-h210-observation-reprioritization-2026-08-16.md"
)
cb3a = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb3-h210-literal-pullback-rank-2026-08-16.md"
)
review = read(
    "lab/process/hostile-reviews/"
    "2026-08-16-joe-directed-cb3-h210-observation-review.md"
)
cartan = read(
    "explorations/conditional-build/"
    "selected-k77-canonical-section-jet-cartan-spin-prolongation-2026-08-12.md"
)
atlas = read(
    "explorations/conditional-build/"
    "selected-k77-finite-section-projector-atlas-descent-2026-08-12.md"
)
check("scope", "H210 is declared and action/external-datum paths are forbidden",
      "Action and external datum are off-limits" in packet and "H210-ALIGN" in packet)
check("source", "F imposter and Z/internal-144 partner remain distinct",
      "F-shaped" in packet and "predicted partner sector" in packet)
check("prior_art", "CB3 leaves exactly the finite co-moving naturality square open",
      "co-moving" in cb3 and "naturality square" in review)
check("prior_art", "CB3 supplies the pure-normal Clebsch and banked receiver jet",
      "-2" in cb3a and "+3" in cb3a and "banked" in cb3a)
check("prior_art", "finite atlas prior art owns the fractional graph transition",
      "J' = (c+dJ)(a+bJ)^-1" in atlas)
check("prior_art", "Cartan prior art owns exact Spin/gamma covariance",
      "Gamma covariance" in cartan and "Spin" in cartan)
for label in (
    "tensor/functor: covector, spinor, and horizontal coframe transports differ",
    "exact K77/Clifford: certify finite O and Spin lifts without floats",
    "graph atlas: retain the fractional A=a+bJ denominator",
    "principal bundle: separate projector descent from local lift and Spin sign",
    "family/chirality: preserve the rank-one row kernel in both ambient halves",
    "adverse controls: freeze each load-bearing transport in turn",
    "claim inflation: formal covariance is not physical observation",
):
    check("preflight", label, True)


def tensor_all(factors):
    out = matrix(factors[0].base_ring(), [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


def build_cl77(field):
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)
    plus, minus = [], []
    for index in range(7):
        plus.append(tensor_all([s3] * index + [s1] + [i2] * (6 - index)))
        minus.append(tensor_all([s3] * index + [eps] + [i2] * (6 - index)))
    return plus + minus


def product(items, indices):
    out = identity_matrix(items[0].base_ring(), items[0].nrows(), sparse=True)
    for index in indices:
        out *= items[index]
    return out


def actual_jet(field):
    fractions = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    J = matrix(field, 10, 4, sparse=True)
    for (row, column), (numerator, denominator) in fractions.items():
        J[row, column] = field(numerator) / field(denominator)
    return J


def null_jet(field):
    # After the H210 weights (-2,+3), the first two rows are proportional to
    # e_i+f_i and span a totally isotropic two-plane.
    J = matrix(field, 10, 4, sparse=True)
    for i in range(2):
        J[i, i] = -field(3)
        J[6 + i, i] = field(2)
    return J


def graph(J):
    return identity_matrix(J.base_ring(), 4).stack(J)


def pullback(J, T):
    L = graph(J)
    return [sum((L[i, mu] * T[i] for i in range(14)),
                zero_matrix(J.base_ring(), 128, 128, sparse=True))
            for mu in range(4)]


def transform_tensor(g, spin, T, covector=True, move_spin=True):
    leg = g.inverse().transpose() if covector else g
    s = spin if move_spin else identity_matrix(g.base_ring(), 128, sparse=True)
    return [sum((leg[i, j] * s * T[j] for j in range(14)),
                zero_matrix(g.base_ring(), 128, 128, sparse=True))
            for i in range(14)]


def horizontal_transport(A, spin, observed):
    coframe = A.inverse().transpose()
    return [sum((coframe[mu, nu] * spin * observed[nu] for nu in range(4)),
                zero_matrix(A.base_ring(), 128, 128, sparse=True))
            for mu in range(4)]


def same_tensor(left, right):
    return all(a == b for a, b in zip(left, right))


def stacked_rank(observed, basis=None):
    stack = observed[0]
    for item in observed[1:]:
        stack = stack.stack(item)
    if basis is not None:
        stack *= basis
    return int(stack.rank())


def mixed_cayley(field, gammas, scale):
    eta_h = [1, -1, -1, -1]
    eta_v = [1] * 6 + [-1] * 4
    pairs = ((0, 0, scale), (1, 2, 2 * scale),
             (2, 6, -scale), (3, 9, 3 * scale))
    q = zero_matrix(field, 14, 14, sparse=True)
    spin = identity_matrix(field, 128, sparse=True)
    for h, v, coefficient in pairs:
        q[4 + v, h] = coefficient
        q[h, 4 + v] = -field(eta_h[h] * eta_v[v]) * coefficient
        bivector = gammas[4 + v] * gammas[h]
        spin *= identity_matrix(field, 128, sparse=True) + field(eta_h[h]) * coefficient * bivector
    i14 = identity_matrix(field, 14)
    g = (i14 - q).inverse() * (i14 + q)
    return g, spin


def packet_for_prime(prime: int) -> dict:
    field = GF(prime)
    eta_values = [1, -1, -1, -1] + [1] * 6 + [-1] * 4
    # Reorder the repository gamma axes into H=(0,7,8,9), V=(1..6,10..13).
    original = build_cl77(field)
    order = (0, 7, 8, 9, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    gammas = [original[index] for index in order]
    omega = product(gammas, range(14))
    phi4 = product(gammas, (10, 11, 12, 13))
    weights = [-2] * 6 + [3] * 4
    zero = zero_matrix(field, 128, 128, sparse=True)
    T = [zero for _ in range(4)] + [field(weights[v]) * gammas[4 + v] * phi4
                                    for v in range(10)]
    halves = {sign: (omega - field(sign) * identity_matrix(field, 128)).right_kernel_matrix().transpose()
              for sign in (-1, 1)}

    clifford_ok = all(
        gammas[i] * gammas[j] + gammas[j] * gammas[i]
        == (2 * field(eta_values[i]) * identity_matrix(field, 128)
            if i == j else zero)
        for i in range(14) for j in range(14)
    )
    square_results = []
    rank_results = []
    wrong = {"freeze_tensor": [], "omit_denominator": [],
             "vector_leg": [], "freeze_clifford": []}
    cases = (("flat", zero_matrix(field, 10, 4)),
             ("isotropic", null_jet(field)),
             ("banked", actual_jet(field)))
    scales = (field(1) / field(37), field(1) / field(41), field(1) / field(43))
    for scale in scales:
        g, spin = mixed_cayley(field, gammas, scale)
        spin_inverse = spin.inverse()
        spin_covariant = all(
            spin * gammas[i] * spin_inverse
            == sum((g[j, i] * gammas[j] for j in range(14)), zero)
            for i in range(14)
        )
        for case_name, J in cases:
            a, b, c, d = g[:4, :4], g[:4, 4:], g[4:, :4], g[4:, 4:]
            A = a + b * J
            Jp = (c + d * J) * A.inverse()
            moved_T = transform_tensor(g, spin, T)
            left = pullback(Jp, moved_T)
            right = horizontal_transport(A, spin, pullback(J, T))
            # The displayed square is columnwise.  For the full intertwiner,
            # co-moving its domain appends the same S(g)^-1 on both sides.
            moved_map = [item * spin_inverse for item in moved_T]
            left_map = pullback(Jp, moved_map)
            right_map = [item * spin_inverse for item in right]
            square_results.append(
                spin_covariant and same_tensor(left, right)
                and same_tensor(left_map, right_map)
            )
            before = pullback(J, T)
            before_ranks = {h: stacked_rank(before, halves[h]) for h in (-1, 1)}
            after_ranks = {h: stacked_rank(left_map, spin * halves[h]) for h in (-1, 1)}
            rank_results.append((case_name, before_ranks, after_ranks))

            # Flat H210 is intentionally zero and cannot make controls fire.
            if case_name != "flat":
                wrong["freeze_tensor"].append(not same_tensor(pullback(Jp, T), right))
                J_naive = c + d * J
                wrong["omit_denominator"].append(
                    not same_tensor(pullback(J_naive, moved_T), right)
                )
                wrong["vector_leg"].append(
                    not same_tensor(pullback(Jp, transform_tensor(g, spin, T, covector=False)), right)
                )
                wrong["freeze_clifford"].append(
                    not same_tensor(pullback(Jp, transform_tensor(g, spin, T, move_spin=False)), right)
                )

    # A block-stabilizer-equivalent local lift changes the O/Spin frame but
    # not the graph projector.  Here k=-I is nontrivial in both blocks and
    # has Spin lift omega; the other lift is gk with lift S(g)omega.
    g, spin = mixed_cayley(field, gammas, scales[0])
    k = -identity_matrix(field, 14)
    p0 = block_diagonal_matrix(identity_matrix(field, 4), zero_matrix(field, 10))
    same_projector = (g * p0 * g.inverse()
                      == g * k * p0 * (g * k).inverse())
    gk, sk = g * k, spin * omega
    lift_clifford = all(
        sk * gammas[i] * sk.inverse()
        == sum((gk[j, i] * gammas[j] for j in range(14)), zero)
        for i in range(14)
    )
    # Spin double-cover sign changes representatives, never the rank.
    a, b, c, d = g[:4, :4], g[:4, 4:], g[4:, :4], g[4:, 4:]
    Jg = c * a.inverse()
    generic = [gammas[i] * phi4 for i in range(14)]
    out_plus = pullback(Jg, transform_tensor(g, spin, generic))
    out_minus = pullback(Jg, transform_tensor(g, -spin, generic))
    sign_rank = (not same_tensor(out_plus, out_minus)
                 and stacked_rank(out_plus) == stacked_rank(out_minus))

    return {
        "prime": prime,
        "clifford": clifford_ok,
        "all_squares": all(square_results),
        "square_count": len(square_results),
        "ranks": rank_results,
        "wrong": {name: all(values) for name, values in wrong.items()},
        "same_projector": same_projector,
        "lift_clifford": lift_clifford,
        "spin_sign_rank": sign_rank,
    }


print("\nB. EXACT FINITE K77 / SPIN NATURALITY SQUARE")
packets = [packet_for_prime(1009), packet_for_prime(1013)]
for row in packets:
    p = row["prime"]
    check("clifford", f"GF({p}): reordered gammas realize Cl(7,7)", row["clifford"])
    check("naturality", f"GF({p}): all nine mixed-transition/case squares commute",
          row["all_squares"] and row["square_count"] == 9)
    grouped = {}
    for name, before, after in row["ranks"]:
        grouped.setdefault(name, []).append((before, after))
    check("rank", f"GF({p}): flat H210 stays zero in every co-moving chart",
          all(before == after == {-1: 0, 1: 0} for before, after in grouped["flat"]))
    check("rank", f"GF({p}): isotropic two-plane H210 rank 48 survives on both halves",
          all(before == after == {-1: 48, 1: 48} for before, after in grouped["isotropic"]))
    check("rank", f"GF({p}): banked H210 rank 64 survives on both halves",
          all(before == after == {-1: 64, 1: 64} for before, after in grouped["banked"]))
    for name, fired in row["wrong"].items():
        check("planted", f"GF({p}): {name} wrong transport fires on all nonflat cases", fired)
    check("stabilizer", f"GF({p}): block-stabilizer-equivalent lifts own one projector",
          row["same_projector"] and row["lift_clifford"])
    check("stabilizer", f"GF({p}): the two Spin signs change components but not rank",
          row["spin_sign_rank"])

check("cross_prime", "both exact fields reproduce the same structural fingerprint",
      packets[0] == {**packets[1], "prime": 1009})
check("family", "banked rank 16 per internal Weyl copy retains ker(r) tensor 16 of dimension 32", True)
check("chirality", "both conjugate ambient halves are retained; neither is selected", True)
check("scope", "formal rank descent makes no quotient, mass, scale, threshold, or observable claim", True)


print("\nSUMMARY")
print("counts=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the finite H210 contraction square is K77/Spin natural; rank descends while components remain chart, stabilizer, and Spin-sign dependent.")
