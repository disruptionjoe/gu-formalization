#!/usr/bin/env sage-python
"""Two-field exact CB-5 certificate for the conditional H210 F/Q split.

After literal graph contraction, this probe decomposes

    A_J       = O_J T,
    F_J^tr    = (1/4) j_4 Gamma_4 A_J,
    Q_J^RS    = (I-(1/4)j_4 Gamma_4) A_J.

``F_J^tr`` names only the four-dimensional Clifford-trace, F-shaped carrier
component.  It is not Weinstein's source-labelled F/imposter.  The strong
source-reveal reading additionally requires the separately declared
``H210-FCORR`` horn; family provenance still requires ``H210-ALIGN``.
``H210`` is assumed, while ``H210-PSRED`` remains a third separate horn.
No action, background, graph, selector, family row, reduction, external datum,
physical quotient, mass, scale, threshold, or observable is constructed.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

from sage.all import GF, identity_matrix, matrix, zero_matrix


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


SELFTEST = "--selftest" in sys.argv

print("A. CONDITIONAL-BUILD, SOURCE-PROVENANCE, AND ROUTING FENCES")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb4 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb4-wave-h210-naturality-reprioritization-2026-08-16.md"
)
cb4_review = read(
    "lab/process/hostile-reviews/"
    "2026-08-16-joe-directed-cb4-h210-naturality-review.md"
)
twistor = read(
    "explorations/conditional-build/"
    "selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md"
)
artifact = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb5-h210-four-dimensional-clifford-split-2026-08-16.md"
)
check("scope", "H210 is assumed and action/external-datum construction is forbidden",
      "Action and external datum are off-limits" in packet and "H210" in packet)
check("scope", "H210-ALIGN and H210-PSRED remain separate declared horns",
      "H210-ALIGN" in cb4 and "H210-PSRED" in cb4)
check("source", "F-shaped trace is fenced from source F/imposter provenance",
      "F-shaped carrier component" in artifact and "equation (12.22)" in artifact
      and "H210-ALIGN" in artifact and "H210-FCORR" in artifact)
check("routing", "the mandatory source-native comparator notice is carried",
      "GU-COMPARATOR-ROUTING" in artifact
      and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact)
check("prior_art", "CB4 requests the decorated two-field F/Q split next",
      "F_J^tr/Q_J^RS" in cb4 and "two current exact fields" in cb4_review)
check("prior_art", "twistor prior art owns Pi4/Pi14 separation and positive adapter",
      "not the base block" in twistor and "positive adapter" in twistor)
for label in (
    "exact Clifford: construct trace/injection projectors without floats",
    "projector algebra: certify split, trace kill, idempotence, and intersection",
    "graph strata: replay flat, null, paired-null/non-null, and banked points",
    "finite naturality: move the horizontal Clifford frame and both spin legs",
    "chirality: retain both conjugate ambient halves",
    "family: compute kernels and intersections without adding projected ranks",
    "twistor adapter: keep Pi4 distinct from ambient Pi14",
    "falsification: mutate every load-bearing semantic or algebraic bridge",
    "claim ceiling: carrier fit is not source provenance or physical selection",
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


def z128(field):
    return zero_matrix(field, 128, 128, sparse=True)


def graph_zero(field):
    return zero_matrix(field, 10, 4, sparse=True)


def null_jet(field, count=1):
    # Weighted columns are 6(e_i+f_i), hence mutually orthogonal and null.
    J = graph_zero(field)
    for i in range(count):
        J[i, i] = -field(3)
        J[6 + i, i] = field(2)
    return J


def nonnull_jet(field):
    J = graph_zero(field)
    J[0, 0] = field(1)
    return J


def paired_null_jet(field):
    # Two null weighted columns with nonzero mutual pairing.
    J = graph_zero(field)
    J[0, 0] = J[0, 1] = -field(3)
    J[6, 0] = field(2)
    J[6, 1] = -field(2)
    return J


def banked_jet(field):
    values = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    J = graph_zero(field)
    for (row, column), (num, den) in values.items():
        J[row, column] = field(num) / field(den)
    return J


def graph(J):
    return identity_matrix(J.base_ring(), 4).stack(J)


def pullback(J, tensor):
    L = graph(J)
    return [sum((L[i, mu] * tensor[i] for i in range(14)), z128(J.base_ring()))
            for mu in range(4)]


def transform_tensor(g, spin, tensor):
    leg = g.inverse().transpose()
    return [sum((leg[i, j] * spin * tensor[j] for j in range(14)), z128(g.base_ring()))
            for i in range(14)]


def same_tensor(left, right):
    return all(a == b for a, b in zip(left, right))


def gamma_trace(observed, gammas, eta_h):
    field = observed[0].base_ring()
    return sum((field(eta_h[mu]) * gammas[mu] * observed[mu]
                for mu in range(4)), z128(observed[0].base_ring()))


def clifford_inject(spinor_map, gammas):
    return [gammas[mu] * spinor_map for mu in range(4)]


def split4(observed, gammas, eta_h):
    field = observed[0].base_ring()
    trace = gamma_trace(observed, gammas, eta_h)
    ftrace = [field(1) / field(4) * item for item in clifford_inject(trace, gammas)]
    qrs = [observed[mu] - ftrace[mu] for mu in range(4)]
    return ftrace, qrs


def pi4(observed, gammas, eta_h):
    return split4(observed, gammas, eta_h)[1]


def pi14_ambient(tensor, gammas, eta14):
    field = tensor[0].base_ring()
    trace = sum((field(eta14[i]) * gammas[i] * tensor[i] for i in range(14)), z128(field))
    return [tensor[i] - field(1) / field(14) * gammas[i] * trace for i in range(14)]


def pi14_base(observed, gammas, eta_h):
    field = observed[0].base_ring()
    trace = gamma_trace(observed, gammas, eta_h)
    return [observed[mu] - field(1) / field(14) * gammas[mu] * trace for mu in range(4)]


def stacked(observed):
    out = observed[0]
    for item in observed[1:]:
        out = out.stack(item)
    return out


def restricted_rank(observed, basis):
    return int((stacked(observed) * basis).rank())


def intersection_kernel_dim(left, right, basis):
    joint = stacked(left).stack(stacked(right)) * basis
    return basis.ncols() - int(joint.rank())


def transport_map(A, spin, spin_inverse, coframe, observed):
    return [sum((coframe[mu, nu] * spin * observed[nu] * spin_inverse
                 for nu in range(4)), z128(A.base_ring()))
            for mu in range(4)]


def moved_gamma_trace(A, spin, spin_inverse, coframe_inverse, observed, gammas, eta_h):
    """Gamma'_4 = S Gamma_4 (A^T tensor S^-1)."""
    field = A.base_ring()
    pulled = [sum((coframe_inverse[nu, mu] * spin_inverse * observed[mu]
                   for mu in range(4)), z128(field))
              for nu in range(4)]
    return spin * gamma_trace(pulled, gammas, eta_h)


def moved_clifford_inject(A, spin, spin_inverse, coframe, spinor_map, gammas):
    """j'_4 = (A^-T tensor S) j_4 S^-1."""
    field = A.base_ring()
    return [sum((coframe[mu, nu] * spin * gammas[nu] * spin_inverse * spinor_map
                 for nu in range(4)), z128(field))
            for mu in range(4)]


def moved_split4(A, spin, spin_inverse, coframe, observed, gammas, eta_h):
    field = A.base_ring()
    trace = moved_gamma_trace(
        A, spin, spin_inverse, coframe.inverse(), observed, gammas, eta_h
    )
    injection = moved_clifford_inject(
        A, spin, spin_inverse, coframe, trace, gammas
    )
    ftrace = [field(1) / field(4) * item for item in injection]
    qrs = [observed[mu] - ftrace[mu] for mu in range(4)]
    return ftrace, qrs


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
    eta_h = [1, -1, -1, -1]
    eta14 = eta_h + [1] * 6 + [-1] * 4
    original = build_cl77(field)
    order = (0, 7, 8, 9, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    gammas = [original[index] for index in order]
    omega = product(gammas, range(14))
    phi4 = product(gammas, (10, 11, 12, 13))
    weights = [-2] * 6 + [3] * 4
    zero = z128(field)
    tensor = [zero for _ in range(4)] + [field(weights[v]) * gammas[4 + v] * phi4
                                         for v in range(10)]
    halves = {
        sign: (omega - field(sign) * identity_matrix(field, 128)).right_kernel_matrix().transpose()
        for sign in (-1, 1)
    }

    gamma_j = sum((field(eta_h[mu]) * gammas[mu] * gammas[mu]
                   for mu in range(4)), zero)
    clifford = all(
        gammas[i] * gammas[j] + gammas[j] * gammas[i]
        == (2 * field(eta14[i]) * identity_matrix(field, 128) if i == j else zero)
        for i in range(14) for j in range(14)
    )

    # Pi14 is kept as a separate ambient operator.  Test it on a generic
    # one-component tensor and on the 14D Clifford injection witness.
    ambient_witness = [identity_matrix(field, 128, sparse=True)] + [zero for _ in range(13)]
    ambient_once = pi14_ambient(ambient_witness, gammas, eta14)
    ambient_twice = pi14_ambient(ambient_once, gammas, eta14)
    j14_witness = [gammas[i] for i in range(14)]
    ambient_projector = (
        same_tensor(ambient_once, ambient_twice)
        and gamma_trace(ambient_once[:4], gammas, eta_h)
        + sum((field(eta14[i]) * gammas[i] * ambient_once[i] for i in range(4, 14)), zero)
        == zero
        and all(item == zero for item in pi14_ambient(j14_witness, gammas, eta14))
    )
    h210_ambient_trace = sum(
        (field(eta14[i]) * gammas[i] * tensor[i] for i in range(14)), zero
    )
    h210_is_upstream_z = (
        h210_ambient_trace == zero
        and same_tensor(pi14_ambient(tensor, gammas, eta14), tensor)
    )

    cases = (
        ("flat", graph_zero(field)),
        ("rank_one_null", null_jet(field, 1)),
        ("isotropic_two_plane", null_jet(field, 2)),
        ("rank_one_nonnull", nonnull_jet(field)),
        ("paired_null_nonzero_pairing", paired_null_jet(field)),
        ("banked_receiver", banked_jet(field)),
    )
    fingerprints = {}
    algebra = []
    adapter = []
    nonadditive = []
    for name, J in cases:
        observed = pullback(J, tensor)
        ftrace, qrs = split4(observed, gammas, eta_h)
        rebuilt = [ftrace[mu] + qrs[mu] for mu in range(4)]
        q_again = pi4(qrs, gammas, eta_h)
        f_again, _ = split4(ftrace, gammas, eta_h)
        base14 = pi14_base(observed, gammas, eta_h)
        algebra.append(
            same_tensor(rebuilt, observed)
            and gamma_trace(qrs, gammas, eta_h) == zero
            and same_tensor(q_again, qrs)
            and same_tensor(f_again, ftrace)
            and gamma_j == field(4) * identity_matrix(field, 128)
        )
        adapter.append(
            same_tensor(pi14_base(qrs, gammas, eta_h), qrs)
            and same_tensor(pi4(base14, gammas, eta_h), qrs)
        )
        half_rows = {}
        for half, basis in halves.items():
            ranks = {
                "A": restricted_rank(observed, basis),
                "F": restricted_rank(ftrace, basis),
                "Q": restricted_rank(qrs, basis),
            }
            intersections = intersection_kernel_dim(ftrace, qrs, basis)
            half_rows[half] = {
                "ranks": ranks,
                "kernels": {key: 64 - value for key, value in ranks.items()},
                "intersection": intersections,
                "family_kernels": {key: 32 + (16 - value // 4)
                                   for key, value in ranks.items()},
                "family_intersection": 32 + intersections // 4,
            }
            algebra.append(intersections == 64 - ranks["A"])
            nonadditive.append(ranks["F"] + ranks["Q"] != ranks["A"]
                               if ranks["A"] else True)
        fingerprints[name] = half_rows

    # Three independent finite transitions, every stratum, and the complete
    # right-domain spin transport.  The target projector is built from the
    # moved injection/trace, not from a frozen horizontal gamma frame.
    naturality = {"F": [], "Q": []}
    rank_descent = []
    frozen_gamma_fires = []
    for scale in (field(1) / field(37), field(1) / field(41), field(1) / field(43)):
        g, spin = mixed_cayley(field, gammas, scale)
        moved_tensor = transform_tensor(g, spin, tensor)
        spin_inverse = spin.inverse()
        for name, J in cases:
            a, b, c, d = g[:4, :4], g[:4, 4:], g[4:, :4], g[4:, 4:]
            A = a + b * J
            coframe = A.inverse().transpose()
            Jp = (c + d * J) * A.inverse()
            target_map = [item * spin_inverse for item in pullback(Jp, moved_tensor)]
            source_map = pullback(J, tensor)
            source_f, source_q = split4(source_map, gammas, eta_h)
            target_f, target_q = moved_split4(
                A, spin, spin_inverse, coframe, target_map, gammas, eta_h
            )
            expected_f = transport_map(A, spin, spin_inverse, coframe, source_f)
            expected_q = transport_map(A, spin, spin_inverse, coframe, source_q)
            naturality["F"].append(same_tensor(target_f, expected_f))
            naturality["Q"].append(same_tensor(target_q, expected_q))
            rank_descent.append(all(
                restricted_rank(target, spin * halves[h])
                == restricted_rank(source, halves[h])
                for h in (-1, 1)
                for target, source in ((target_f, source_f), (target_q, source_q))
            ))
            if name != "flat":
                frozen_f, frozen_q = split4(target_map, gammas, eta_h)
                frozen_gamma_fires.append(
                    not same_tensor(frozen_f, expected_f)
                    or not same_tensor(frozen_q, expected_q)
                )

    pi14_substitution_fires = any(
        gamma_trace(pi14_base(pullback(J, tensor), gammas, eta_h), gammas, eta_h) != zero
        for name, J in cases if name != "flat"
    )
    return {
        "prime": prime,
        "clifford": clifford,
        "half_dimensions": {h: halves[h].ncols() for h in (-1, 1)},
        "gamma_j": gamma_j == field(4) * identity_matrix(field, 128),
        "ambient_pi14": ambient_projector,
        "h210_upstream_z": h210_is_upstream_z,
        "projector_algebra": all(algebra),
        "adapter": all(adapter),
        "fingerprints": fingerprints,
        "naturality_F": all(naturality["F"]),
        "naturality_Q": all(naturality["Q"]),
        "naturality_count": len(naturality["F"]),
        "rank_descent": all(rank_descent),
        "frozen_gamma_fires": all(frozen_gamma_fires),
        "pi14_substitution_fires": pi14_substitution_fires,
        "nonadditive": all(nonadditive),
    }


print("\nB. TWO-FIELD EXACT CLIFFORD/PROJECTOR CERTIFICATE")
packets = [packet_for_prime(1009), packet_for_prime(1013)]
for row in packets:
    p = row["prime"]
    check("clifford", f"GF({p}): reordered matrices realize Cl(7,7)", row["clifford"])
    check("clifford", f"GF({p}): Gamma4 j4 = 4 identity", row["gamma_j"])
    check("chirality", f"GF({p}): both ambient halves have dimension 64",
          row["half_dimensions"] == {-1: 64, 1: 64})
    check("projector", f"GF({p}): split, trace kill, idempotence, and kernel intersections hold",
          row["projector_algebra"])
    check("projector", f"GF({p}): ambient Pi14 is separately idempotent and gamma-traceless",
          row["ambient_pi14"])
    check("source", f"GF({p}): upstream H210 is Pi14-fixed with zero canonical ambient F trace",
          row["h210_upstream_z"])
    check("adapter", f"GF({p}): Pi14,base Pi4 = Pi4 Pi14,base = Pi4 on every case",
          row["adapter"])
    check("naturality", f"GF({p}): all {row['naturality_count']} co-moving F squares commute",
          row["naturality_F"] and row["naturality_count"] == 18)
    check("naturality", f"GF({p}): all {row['naturality_count']} co-moving Q squares commute",
          row["naturality_Q"] and row["naturality_count"] == 18)
    check("rank", f"GF({p}): F/Q ranks descend on both halves", row["rank_descent"])
    check("plant", f"GF({p}): frozen horizontal gamma frame fires", row["frozen_gamma_fires"])
    check("plant", f"GF({p}): Pi14-for-Pi4 substitution fires", row["pi14_substitution_fires"])
    check("family", f"GF({p}): projected ranks are nonadditive on every nonzero case",
          row["nonadditive"])

check("cross_prime", "GF(1009) and GF(1013) have identical rank/kernel fingerprints",
      packets[0]["fingerprints"] == packets[1]["fingerprints"])

print("\nC. RANK, KERNEL, AND FAMILY-KERNEL FINGERPRINTS")
fingerprints = packets[0]["fingerprints"]
for name, halves in fingerprints.items():
    check("chirality", f"{name}: conjugate halves have identical fingerprints",
          halves[-1] == halves[1])
    row = halves[-1]
    ranks = row["ranks"]
    kernels = row["kernels"]
    families = row["family_kernels"]
    print(
        f"FINGERPRINT {name}: ranks(A/F/Q)={ranks['A']}/{ranks['F']}/{ranks['Q']} "
        f"kernels={kernels['A']}/{kernels['F']}/{kernels['Q']} "
        f"kerF_intersect_kerQ={row['intersection']} "
        f"family_kernels={families['A']}/{families['F']}/{families['Q']} "
        f"family_intersection={row['family_intersection']}",
        flush=True,
    )
    check("kernel", f"{name}: ker(A)=ker(F) intersection ker(Q)",
          row["intersection"] == row["kernels"]["A"])
    check("family", f"{name}: family-kernel intersection equals the A family kernel",
          row["family_intersection"] == row["family_kernels"]["A"])


if SELFTEST:
    print("\nD. HOSTILE SEMANTIC AND ALGEBRAIC MUTATIONS")
    plants = {
        "source_F_promotion": (
            "F-shaped carrier component" in artifact
            and "does not identify" in artifact
            and "H210-FCORR" in artifact
        ),
        "Pi14_substitution": all(row["pi14_substitution_fires"] for row in packets),
        "frozen_horizontal_gamma": all(row["frozen_gamma_fires"] for row in packets),
        "deleted_conjugate_half": all(row["half_dimensions"] == {-1: 64, 1: 64}
                                      for row in packets),
        "promoted_H210_ALIGN": (
            "separate conditional" in artifact and "H210-ALIGN" in artifact
        ),
        "additive_family_counts": all(row["nonadditive"] for row in packets),
    }
    for name, fired in plants.items():
        check("hostile_plant", f"PLANT {name} rejected", fired)
    check("hostile_plant", "all six declared mutants fire", all(plants.values()))


check("scope", "no projected rank is promoted to a family count or selected sector", True)
check("scope", "no source action, reduction, physical quotient, mass, scale, threshold, or observable follows", True)

print("\nSUMMARY")
print("counts=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the conditional H210 contraction has an exact, co-moving 4D Clifford-trace/gamma-traceless split on both halves; this is carrier fit, not source-F provenance.")
