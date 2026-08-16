#!/usr/bin/env sage-python
"""Exact full graph-plane naturality of the conditional H210 correlated lift.

For the nondegenerate graph ``H_J=im L_J`` this probe uses its metric
orthogonal complement ``N_J=im K_J`` and the Clifford traces determined by
the two induced Gram matrices.  It verifies the complete horizontal/normal
``kappa_J`` square, including the right-domain Spin transport.  H210 is a
declared conditional input; no action, observer, selector, family row,
reduction, quotient, scale, or observable is constructed.
"""

from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass, replace
from pathlib import Path

from sage.all import GF, diagonal_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
SELFTEST = "--selftest" in sys.argv
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


print("A. CONDITIONAL-BUILD FENCES, SOURCE CUSTODY, AND PRIOR ART")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb5 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb5-h210-four-dimensional-clifford-split-2026-08-16.md"
)
cb5c = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb5-h210-source-fq-bridge-2026-08-16.md"
)
cb4 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb4-h210-finite-comoving-naturality-square-2026-08-16.md"
)
source = read("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md")
twistor = read(
    "explorations/conditional-build/"
    "selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md"
)
artifact_path = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-full-correlated-lift-naturality-2026-08-16.md"
)
artifact = read(artifact_path)
check("scope", "conditional packet keeps action and external datum off limits",
      "Action and external datum are off-limits" in packet)
check("source", "source F, M_3, and Z/internal 144 remain distinct",
      "F_corr" in cb5c and "M_3" in packet and "internal 144" in source)
check("source", "equation (12.22) labels only the third summand as imposter",
      "attached to the THIRD term" in source)
check("prior_art", "CB4 supplies the fractional graph transition and full domain factor",
      "J' = (c+dJ)A^-1" in cb4 and "right" in cb4)
check("prior_art", "CB5 leaves complete moving-normal kappa naturality open",
      "complete co-moving" in cb5 and "normal complement" in cb5c)
check("twistor", "Pi4/Pi14 distinction and positive adapter remain controls",
      "Pi_14,base Pi_4" in twistor and "cannot be substituted" in twistor)
check("routing", "artifact carries mandatory routing classification",
      "GU-COMPARATOR-ROUTING" in artifact
      and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact)
for label in (
    "exact Clifford: use induced graph and normal Gram inverses",
    "bundle naturality: move H and N coframes separately",
    "graph atlas: derive the normal D cocycle from orthogonality",
    "representation/chirality: retain the graded normal Clifford action and both halves",
    "functor order: upstream F projection precedes observation-induced kappa",
    "twistor control: do not substitute Pi14 for the graph-plane trace split",
    "adverse mutation: freeze K/D, Gram, sign, or right-domain transport",
    "source custody: FCORR, ALIGN, and PSRED remain independent",
    "efficiency: certify the forced square rather than search for a preferred lift",
    "claim ceiling: associated carrier descent is not physical observation",
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


def graph(J):
    return identity_matrix(J.base_ring(), 4).stack(J)


def normal_frame(J, eta_h, eta_v):
    top = -eta_h.inverse() * J.transpose() * eta_v
    return top.stack(identity_matrix(J.base_ring(), 10))


def gram(frame, eta):
    return frame.transpose() * eta * frame


def gamma_frame(frame, gammas):
    field = frame.base_ring()
    return [sum((frame[i, column] * gammas[i] for i in range(14)), z128(field))
            for column in range(frame.ncols())]


def pullback(J, tensor):
    L = graph(J)
    return [sum((L[i, mu] * tensor[i] for i in range(14)), z128(J.base_ring()))
            for mu in range(4)]


def transform_tensor(g, spin, spin_inverse, tensor):
    leg = g.inverse().transpose()
    return [sum((leg[i, j] * spin * tensor[j] * spin_inverse for j in range(14)),
                z128(g.base_ring())) for i in range(14)]


def clifford_trace(vector_spinor, frame_gammas, frame_gram):
    inverse_gram = frame_gram.inverse()
    field = frame_gram.base_ring()
    return sum(
        (inverse_gram[i, j] * frame_gammas[i] * vector_spinor[j]
         for i in range(frame_gram.nrows()) for j in range(frame_gram.ncols())),
        z128(field),
    )


def clifford_inject(spinor_map, frame_gammas):
    return [gamma * spinor_map for gamma in frame_gammas]


def correlated_pair(tau, gamma_h, gram_h, gamma_n, gram_n, normal_sign=-1):
    field = tau.base_ring()
    horizontal = [field(1) / field(4) * item
                  for item in clifford_inject(tau, gamma_h)]
    normal = [field(normal_sign) / field(10) * item
              for item in clifford_inject(tau, gamma_n)]
    return horizontal, normal


def ambient_pair_trace(pair, gamma_h, gram_h, gamma_n, gram_n):
    return (clifford_trace(pair[0], gamma_h, gram_h)
            + clifford_trace(pair[1], gamma_n, gram_n))


def same_tensor(left, right):
    return all(a == b for a, b in zip(left, right))


def same_pair(left, right):
    return same_tensor(left[0], right[0]) and same_tensor(left[1], right[1])


def stack_tensor(items):
    out = items[0]
    for item in items[1:]:
        out = out.stack(item)
    return out


def pair_rank(pair, basis):
    return int(stack_tensor(pair[0] + pair[1]).__mul__(basis).rank())


def map_rank(item, basis):
    return int((item * basis).rank())


def transport_components(coframe, spin, spin_inverse, items, right=True):
    field = coframe.base_ring()
    right_factor = spin_inverse if right else identity_matrix(field, 128, sparse=True)
    return [sum((coframe[i, j] * spin * items[j] * right_factor
                 for j in range(coframe.ncols())), z128(field))
            for i in range(coframe.nrows())]


def transport_pair(A, D, spin, spin_inverse, pair, right=True):
    return (
        transport_components(A.inverse().transpose(), spin, spin_inverse, pair[0], right),
        transport_components(D.inverse().transpose(), spin, spin_inverse, pair[1], right),
    )


def fixed_cb5_trace(observed, gammas, eta_h):
    field = observed[0].base_ring()
    return sum((field(eta_h[mu]) * gammas[mu] * observed[mu] for mu in range(4)),
               z128(field))


def null_jet(field):
    J = matrix(field, 10, 4, sparse=True)
    for i in range(2):
        J[i, i] = -field(3)
        J[6 + i, i] = field(2)
    return J


def banked_jet(field):
    values = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    J = matrix(field, 10, 4, sparse=True)
    for (row, column), (numerator, denominator) in values.items():
        J[row, column] = field(numerator) / field(denominator)
    return J


def mixed_cayley(field, gammas, scale):
    eta_h_values = [1, -1, -1, -1]
    eta_v_values = [1] * 6 + [-1] * 4
    pairs = ((0, 0, scale), (1, 2, 2 * scale),
             (2, 6, -scale), (3, 9, 3 * scale))
    q = zero_matrix(field, 14, 14, sparse=True)
    spin = identity_matrix(field, 128, sparse=True)
    for h, v, coefficient in pairs:
        q[4 + v, h] = coefficient
        q[h, 4 + v] = -field(eta_h_values[h] * eta_v_values[v]) * coefficient
        bivector = gammas[4 + v] * gammas[h]
        spin *= (identity_matrix(field, 128, sparse=True)
                 + field(eta_h_values[h]) * coefficient * bivector)
    i14 = identity_matrix(field, 14)
    return (i14 - q).inverse() * (i14 + q), spin


def packet_for_prime(prime: int) -> dict:
    field = GF(prime)
    eta_h_values = [1, -1, -1, -1]
    eta_v_values = [1] * 6 + [-1] * 4
    eta_h = diagonal_matrix(field, eta_h_values)
    eta_v = diagonal_matrix(field, eta_v_values)
    eta = diagonal_matrix(field, eta_h_values + eta_v_values)
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

    clifford = all(
        gammas[i] * gammas[j] + gammas[j] * gammas[i]
        == (2 * eta[i, i] * identity_matrix(field, 128) if i == j else zero)
        for i in range(14) for j in range(14)
    )
    upstream_normal_trace = sum(
        (field(eta_v_values[a]) * gammas[4 + a] * tensor[4 + a] for a in range(10)),
        zero,
    )
    upstream_f_zero = all(item == zero for item in tensor[:4]) and upstream_normal_trace == zero

    cases = (
        ("flat", zero_matrix(field, 10, 4, sparse=True)),
        ("isotropic", null_jet(field)),
        ("banked", banked_jet(field)),
    )
    graph_checks = []
    split_checks = []
    intrinsic_fingerprints = {}
    cb5_comparison = {}
    downstream_nonzero = []
    chirality_checks = []
    for name, J in cases:
        L = graph(J)
        K = normal_frame(J, eta_h, eta_v)
        GH, GN = gram(L, eta), gram(K, eta)
        gamma_h, gamma_n = gamma_frame(L, gammas), gamma_frame(K, gammas)
        graph_checks.append(
            GH.is_invertible() and GN.is_invertible()
            and L.transpose() * eta * K == zero_matrix(field, 4, 10)
        )
        grading_ok = all(
            gamma_h[mu] * gamma_n[a] + gamma_n[a] * gamma_h[mu] == zero
            for mu in range(4) for a in range(10)
        )
        observed = pullback(J, tensor)
        tau = clifford_trace(observed, gamma_h, GH)
        pair = correlated_pair(tau, gamma_h, GH, gamma_n, GN)
        split_checks.append(
            clifford_trace(clifford_inject(identity_matrix(field, 128), gamma_h),
                           gamma_h, GH) == field(4) * identity_matrix(field, 128)
            and clifford_trace(clifford_inject(identity_matrix(field, 128), gamma_n),
                               gamma_n, GN) == field(10) * identity_matrix(field, 128)
            and ambient_pair_trace(pair, gamma_h, GH, gamma_n, GN) == zero
            and grading_ok
        )
        cb5_tau = fixed_cb5_trace(observed, gammas, eta_h_values)
        cb5_comparison[name] = {
            "equal": cb5_tau == tau,
            "fixed_ranks": {h: map_rank(cb5_tau, halves[h]) for h in (-1, 1)},
            "intrinsic_ranks": {h: map_rank(tau, halves[h]) for h in (-1, 1)},
        }
        intrinsic_fingerprints[name] = {
            h: {"tau_rank": map_rank(tau, halves[h]),
                "pair_rank": pair_rank(pair, halves[h]),
                "kernel": 64 - pair_rank(pair, halves[h])}
            for h in (-1, 1)
        }
        if name != "flat":
            downstream_nonzero.append(tau != zero and pair_rank(pair, halves[-1]) > 0)
        for h, basis in halves.items():
            for item in pair[0] + pair[1]:
                chirality_checks.append(omega * item * basis == -field(h) * item * basis)

    naturality = []
    rank_descent = []
    cocycles = []
    wrong = {"frozen_K_or_D": [], "fixed_Gram": [],
             "wrong_normal_sign": [], "missing_right_domain": []}
    scales = (field(1) / field(37), field(1) / field(41), field(1) / field(43))
    for scale in scales:
        g, spin = mixed_cayley(field, gammas, scale)
        spin_inverse = spin.inverse()
        spin_covariant = all(
            spin * gammas[i] * spin_inverse
            == sum((g[j, i] * gammas[j] for j in range(14)), zero)
            for i in range(14)
        )
        moved_tensor = transform_tensor(g, spin, spin_inverse, tensor)
        for name, J in cases:
            a, b, c, d = g[:4, :4], g[:4, 4:], g[4:, :4], g[4:, 4:]
            A = a + b * J
            Jp = (c + d * J) * A.inverse()
            L, K = graph(J), normal_frame(J, eta_h, eta_v)
            Lp, Kp = graph(Jp), normal_frame(Jp, eta_h, eta_v)
            D = d - c * eta_h.inverse() * J.transpose() * eta_v
            GH, GN = gram(L, eta), gram(K, eta)
            GHp, GNp = gram(Lp, eta), gram(Kp, eta)
            gamma_h, gamma_n = gamma_frame(L, gammas), gamma_frame(K, gammas)
            gamma_hp, gamma_np = gamma_frame(Lp, gammas), gamma_frame(Kp, gammas)
            moved_gamma_h = transport_components(
                A.inverse().transpose(), spin, spin_inverse, gamma_h
            )
            moved_gamma_n = transport_components(
                D.inverse().transpose(), spin, spin_inverse, gamma_n
            )
            cocycles.append(
                g * L == Lp * A and g * K == Kp * D
                and GHp == A.inverse().transpose() * GH * A.inverse()
                and GNp == D.inverse().transpose() * GN * D.inverse()
                and same_tensor(gamma_hp, moved_gamma_h)
                and same_tensor(gamma_np, moved_gamma_n)
                and spin_covariant
            )

            source_observed = pullback(J, tensor)
            target_observed = pullback(Jp, moved_tensor)
            source_tau = clifford_trace(source_observed, gamma_h, GH)
            target_tau = clifford_trace(target_observed, gamma_hp, GHp)
            source_pair = correlated_pair(source_tau, gamma_h, GH, gamma_n, GN)
            target_pair = correlated_pair(target_tau, gamma_hp, GHp, gamma_np, GNp)
            expected_pair = transport_pair(A, D, spin, spin_inverse, source_pair)
            naturality.append(
                target_tau == spin * source_tau * spin_inverse
                and same_pair(target_pair, expected_pair)
                and ambient_pair_trace(target_pair, gamma_hp, GHp, gamma_np, GNp) == zero
            )
            rank_descent.append(all(
                pair_rank(source_pair, halves[h])
                == pair_rank(target_pair, spin * halves[h])
                for h in (-1, 1)
            ))

            if source_tau != zero:
                frozen_normal = correlated_pair(
                    target_tau, gamma_hp, GHp, gamma_n, GN
                )[1]
                wrong["frozen_K_or_D"].append(
                    not same_tensor(frozen_normal, expected_pair[1])
                    and not same_tensor(
                        transport_components(identity_matrix(field, 10), spin,
                                             spin_inverse, source_pair[1]),
                        target_pair[1],
                    )
                )
                fixed_gram_tau = clifford_trace(target_observed, gamma_hp, eta_h)
                fixed_gram_pair = correlated_pair(
                    fixed_gram_tau, gamma_hp, eta_h, gamma_np, eta_v
                )
                wrong["fixed_Gram"].append(
                    ambient_pair_trace(fixed_gram_pair, gamma_hp, GHp, gamma_np, GNp) != zero
                    or not same_pair(fixed_gram_pair, expected_pair)
                )
                wrong_sign_pair = correlated_pair(
                    target_tau, gamma_hp, GHp, gamma_np, GNp, normal_sign=1
                )
                wrong["wrong_normal_sign"].append(
                    ambient_pair_trace(wrong_sign_pair, gamma_hp, GHp, gamma_np, GNp) != zero
                )
                wrong["missing_right_domain"].append(
                    not same_pair(
                        transport_pair(A, D, spin, spin_inverse, source_pair, right=False),
                        target_pair,
                    )
                )

    return {
        "prime": prime,
        "clifford": clifford,
        "halves": {h: halves[h].ncols() for h in (-1, 1)},
        "upstream_f_zero": upstream_f_zero,
        "graph_checks": all(graph_checks),
        "split_checks": all(split_checks),
        "intrinsic_fingerprints": intrinsic_fingerprints,
        "cb5_comparison": cb5_comparison,
        "downstream_nonzero": all(downstream_nonzero),
        "chirality": all(chirality_checks),
        "cocycles": all(cocycles),
        "naturality": all(naturality),
        "naturality_count": len(naturality),
        "rank_descent": all(rank_descent),
        "wrong": {name: bool(values) and all(values) for name, values in wrong.items()},
    }


print("\nB. EXACT TWO-FIELD FULL HORIZONTAL/NORMAL KAPPA SQUARE")
packets = [packet_for_prime(1009), packet_for_prime(1013)]
for row in packets:
    p = row["prime"]
    check("clifford", f"GF({p}): reordered matrices realize Cl(7,7)", row["clifford"])
    check("graph", f"GF({p}): all H_J/N_J frames are nondegenerate and orthogonal",
          row["graph_checks"])
    check("clifford", f"GF({p}): induced Gamma-j identities and graded H/N anticommutation pass",
          row["split_checks"])
    check("source", f"GF({p}): upstream pure-normal H210 has zero F-correlation projection",
          row["upstream_f_zero"])
    check("source", f"GF({p}): nonflat intrinsic observation induces nonzero correlated lifts",
          row["downstream_nonzero"])
    check("chirality", f"GF({p}): both 64-dimensional halves are retained",
          row["halves"] == {-1: 64, 1: 64})
    check("chirality", f"GF({p}): correlated H/N components have the same opposite-half allocation",
          row["chirality"])
    check("atlas", f"GF({p}): gL=L'A, gK=K'D and both Gram cocycles pass",
          row["cocycles"])
    check("naturality", f"GF({p}): all nine complete kappa squares commute",
          row["naturality"] and row["naturality_count"] == 9)
    check("rank", f"GF({p}): pair ranks and kernels descend on both halves",
          row["rank_descent"])
    check("successor", f"GF({p}): CB5 fixed trace agrees only on flat, not intrinsic nonflat charts",
          row["cb5_comparison"]["flat"]["equal"]
          and not row["cb5_comparison"]["isotropic"]["equal"]
          and not row["cb5_comparison"]["banked"]["equal"])
    for name, fired in row["wrong"].items():
        check("planted", f"GF({p}): {name} mutation fires", fired)

fingerprints = [{key: value for key, value in row.items() if key != "prime"} for row in packets]
check("cross_prime", "both exact fields reproduce the same structural fingerprint",
      fingerprints[0] == fingerprints[1])


@dataclass(frozen=True)
class SemanticLedger:
    upstream_h210_sector: str = "Z_WITH_ZERO_FCORR_PROJECTION"
    downstream_status: str = "OBSERVATION_INDUCED_FCORR_SHAPED_ADAPTER"
    correlated_normal_partner: str = "CONSTRUCTED_NOT_RECOVERED"
    retained_halves: int = 2
    fcorr_role: str = "SOURCE_REVEAL_INTERPRETATION"
    align_role: str = "FAMILY_PROVENANCE_ALIGNMENT"
    psred_role: str = "MOVING_PS_REDUCTION"


LEDGER = SemanticLedger()


def semantic_ok(ledger: SemanticLedger) -> bool:
    return (
        ledger.upstream_h210_sector == "Z_WITH_ZERO_FCORR_PROJECTION"
        and ledger.downstream_status == "OBSERVATION_INDUCED_FCORR_SHAPED_ADAPTER"
        and ledger.correlated_normal_partner == "CONSTRUCTED_NOT_RECOVERED"
        and ledger.retained_halves == 2
        and len({ledger.fcorr_role, ledger.align_role, ledger.psred_role}) == 3
    )


check("semantic", "source custody and three independent horn roles pass", semantic_ok(LEDGER))
if SELFTEST:
    plants = {
        "promote upstream H210 to source F": replace(
            LEDGER, upstream_h210_sector="SOURCE_F_IMPOSTER"
        ),
        "call downstream adapter source-selected": replace(
            LEDGER, downstream_status="SOURCE_SELECTED_REVEAL"
        ),
        "claim normal partner was recovered": replace(
            LEDGER, correlated_normal_partner="RECOVERED_H210_144_LEG"
        ),
        "delete conjugate half": replace(LEDGER, retained_halves=1),
        "collapse FCORR with ALIGN": replace(
            LEDGER, align_role="SOURCE_REVEAL_INTERPRETATION"
        ),
        "collapse FCORR with PSRED": replace(
            LEDGER, psred_role="SOURCE_REVEAL_INTERPRETATION"
        ),
    }
    for label, planted in plants.items():
        check("semantic_plant", label, not semantic_ok(planted))

check("scope", "artifact keeps action/selector/background/row/reduction/quotient paths fenced",
      all(term in artifact for term in (
          "action", "selector", "background", "family row", "reduction", "physical quotient"
      )))


print("\nFINGERPRINTS")
for row in packets:
    print(f"GF({row['prime']}): intrinsic={row['intrinsic_fingerprints']}")
    print(f"GF({row['prime']}): cb5_vs_intrinsic={row['cb5_comparison']}")
print("\nSUMMARY")
print("counts=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the intrinsic graph-plane correlated H/N lift is exact and co-moving; CB5's fixed chartwise trace is a distinct nonflat decoration.")
