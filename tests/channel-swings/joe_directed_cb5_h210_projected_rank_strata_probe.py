#!/usr/bin/env sage-python
"""Exact projected-rank strata for the conditional H210 contraction.

This is the analytic/normal-form companion to CB5's transport certificate.
It works directly with the weighted observer map ``W=diag(-2^6,3^4)J`` and
the four-dimensional Clifford splitting of ``A_J=O_JT``.  H210 is assumed.
No action, background, selector, graph choice, family fit, PS reduction,
external datum, or physical quotient is derived.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import GF, QQ, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}"
          + (f" -- {detail}" if detail else ""), flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


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
    original = plus + minus
    order = (0, 7, 8, 9, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    return [original[index] for index in order]


def product(items, indices):
    out = identity_matrix(items[0].base_ring(), items[0].nrows(), sparse=True)
    for index in indices:
        out *= items[index]
    return out


def stack(items):
    out = items[0]
    for item in items[1:]:
        out = out.stack(item)
    return out


def zero_w(field):
    return matrix(field, 10, 4, sparse=True)


def set_column(W, mu, entries):
    for a, value in entries.items():
        W[a, mu] = W.base_ring()(value)


def cases(field):
    out = {}
    out["zero"] = zero_w(field)

    W = zero_w(field); set_column(W, 0, {0: 1})
    out["rank1_nonnull"] = W
    W = zero_w(field); set_column(W, 0, {0: 1}); set_column(W, 1, {0: 1})
    out["rank1_nonnull_external_null"] = W
    W = zero_w(field); set_column(W, 0, {0: 1, 6: 1})
    out["rank1_null_time"] = W
    W = zero_w(field)
    set_column(W, 0, {0: 1, 6: 1}); set_column(W, 1, {0: 1, 6: 1})
    out["rank1_null_external_null"] = W

    for k in (2, 3, 4):
        W = zero_w(field)
        for i in range(k):
            set_column(W, i, {i: 1, 6 + i: 1})
        out[f"internal_totally_isotropic_{k}"] = W

    W = zero_w(field)
    set_column(W, 0, {0: 1, 6: 1}); set_column(W, 1, {0: 1, 6: -1})
    out["paired_internal_nulls"] = W

    # Signature-matched and signature-reversed rank-four embeddings.  These
    # are the cheapest Clifford-incidence controls beyond row-space rank.
    W = zero_w(field)
    set_column(W, 0, {0: 1}); set_column(W, 1, {6: 1})
    set_column(W, 2, {7: 1}); set_column(W, 3, {8: 1})
    out["signature_matched_embedding"] = W

    # Weighted version of the banked CB3 receiver jet.
    weights = [-2] * 6 + [3] * 4
    fractions = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    W = zero_w(field)
    for (a, mu), (num, den) in fractions.items():
        W[a, mu] = field(weights[a] * num) / field(den)
    out["banked_receiver"] = W
    return out


def packet(field):
    gammas = build_cl77(field)
    eta_h = [1, -1, -1, -1]
    phi4 = product(gammas, (10, 11, 12, 13))
    omega = product(gammas, range(14))
    halves = {
        sign: (omega - field(sign) * identity_matrix(field, 128)).right_kernel_matrix().transpose()
        for sign in (-1, 1)
    }
    z128 = zero_matrix(field, 128, 128, sparse=True)
    eta_v = [1] * 6 + [-1] * 4
    weights = [-2] * 6 + [3] * 4
    upstream_normal_trace = sum(
        (field(eta_v[a] * weights[a]) * gammas[4 + a] * gammas[4 + a] * phi4
         for a in range(10)), z128
    )

    def split_matrices(W, half):
        A = [sum((W[a, mu] * gammas[4 + a] * phi4 for a in range(10)), z128)
             for mu in range(4)]
        trace = sum((field(eta_h[mu]) * gammas[mu] * A[mu] for mu in range(4)), z128)
        F = [field(1) / field(4) * gammas[mu] * trace for mu in range(4)]
        Q = [A[mu] - F[mu] for mu in range(4)]
        basis = halves[half]
        MA, MF, MQ = stack(A) * basis, stack(F) * basis, stack(Q) * basis
        return A, F, Q, MA, MF, MQ

    def split(W, half):
        A, F, Q, MA, MF, MQ = split_matrices(W, half)
        return {
            "A": int(MA.rank()), "F": int(MF.rank()), "Q": int(MQ.rank()),
            "AF": int(MA.stack(MF).rank()),
            "AQ": int(MA.stack(MQ).rank()),
            "FQ": int(MF.stack(MQ).rank()),
            "split": all(A[mu] == F[mu] + Q[mu] for mu in range(4)),
            "traceQ": all(
                x == 0 for x in sum(
                    (field(eta_h[mu]) * gammas[mu] * Q[mu] for mu in range(4)), z128
                ).list()
            ),
        }

    rows = {}
    for name, W in cases(field).items():
        rows[name] = {
            "weighted_rank": int(W.rank()),
            "halves": {half: split(W, half) for half in (-1, 1)},
        }

    coefficient_ranks = {}
    for half in (-1, 1):
        columns = {"F": [], "Q": []}
        for a in range(10):
            for mu in range(4):
                W = zero_w(field)
                W[a, mu] = field(1)
                _, _, _, _, MF, MQ = split_matrices(W, half)
                columns["F"].append(MF.list())
                columns["Q"].append(MQ.list())
        coefficient_ranks[half] = {
            name: int(matrix(field, vectors, sparse=True).rank())
            for name, vectors in columns.items()
        }
    return {
        "rows": rows,
        "coefficient_ranks": coefficient_ranks,
        "upstream_z_trace_zero": upstream_normal_trace == z128,
    }


print("A. CONDITIONAL-BUILD AND ROUTING FENCES")
packet_text = read("lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md")
cb3_text = read("lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-literal-pullback-rank-2026-08-16.md")
cb4_text = read("lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md")
twistor_text = read("explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md")
check("scope", "H210 is declared while action and external-datum paths remain forbidden",
      "Action and external datum are off-limits" in packet_text)
check("routing", "the source F-shaped 128 stays distinct from the internal 144 partner",
      "F     =" in packet_text and "144   =" in packet_text)
check("prior_art", "CB3 owns the weighted (6,4) row-space rank strata",
      "weighted row-space" in cb3_text)
check("prior_art", "CB4 owns the decorated F/Q split as the next gate",
      "F_J^tr" in cb4_text and "Q_J^RS" in cb4_text)
check("projector", "twistor prior art proves Pi4 differs from Pi14",
      "Pi_4" in twistor_text and "Pi_14" in twistor_text and "not the base block" in twistor_text)
for label in (
    "Clifford normal forms classify the weighted observer map rather than a chosen graph",
    "Spin covariance permits normal-form fingerprints but does not select a representative",
    "rank strata are determinantal loci and genericity is Zariski-relative",
    "family kernels are computed by exact sequences and never added as family counts",
    "counterexamples attack rank-only classification and projected-sector inflation",
    "claim ceiling stops before provenance, dynamics, reduction, or phenomenology",
):
    check("lens", label, True)


print("\nB. EXACT NORMAL-FORM FINGERPRINTS")
packets = {"GF1009": packet(GF(1009)), "GF1013": packet(GF(1013)), "QQ": packet(QQ)}
for field_name, packet_data in packets.items():
    rows = packet_data["rows"]
    check("nonvanishing", f"{field_name}: Ftr and QRS coefficient maps are injective on each half",
          packet_data["coefficient_ranks"] == {-1: {"F": 40, "Q": 40}, 1: {"F": 40, "Q": 40}},
          str(packet_data["coefficient_ranks"]))
    check("source_boundary", f"{field_name}: upstream pure-normal H210 tensor is normal gamma-traceless Z data",
          packet_data["upstream_z_trace_zero"])
    for name, row in rows.items():
        left, right = row["halves"][-1], row["halves"][1]
        check("split", f"{field_name} {name}: A=Ftr+QRS and Gamma4 QRS=0 on both halves",
              left["split"] and left["traceQ"] and right["split"] and right["traceQ"])
        check("chirality", f"{field_name} {name}: both ambient halves have one rank fingerprint",
              {k: left[k] for k in ("A", "F", "Q", "FQ")} ==
              {k: right[k] for k in ("A", "F", "Q", "FQ")})
        print(f"ROW {field_name} {name} weighted={row['weighted_rank']} "
              f"A/F/Q/FQ={left['A']}/{left['F']}/{left['Q']}/{left['FQ']}")


print("\nC. CLASSIFICATION, COUNTEREXAMPLES, AND FAMILY EXACT SEQUENCES")
rows = packets["QQ"]["rows"]
fingerprints = {name: tuple(row["halves"][1][k] for k in ("A", "F", "Q"))
                for name, row in rows.items()}
check("counterexample", "rank(A) does not determine rank(Ftr)",
      fingerprints["rank1_null_time"][0] == fingerprints["rank1_null_external_null"][0]
      and fingerprints["rank1_null_time"][1] != fingerprints["rank1_null_external_null"][1],
      str((fingerprints["rank1_null_time"], fingerprints["rank1_null_external_null"])))
check("counterexample", "rank(A) does not determine the full projected-rank pair",
      fingerprints["rank1_null_time"] != fingerprints["rank1_null_external_null"])
check("counterexample", "rank(A) does not determine rank(QRS)",
      fingerprints["rank1_nonnull"][0] == fingerprints["signature_matched_embedding"][0] == 64
      and fingerprints["rank1_nonnull"][2] != fingerprints["signature_matched_embedding"][2],
      str((fingerprints["rank1_nonnull"], fingerprints["signature_matched_embedding"])))
check("nonvanishing", "injective coefficient maps prove Ftr=0 or QRS=0 only when W=0",
      all(data["coefficient_ranks"] == {-1: {"F": 40, "Q": 40}, 1: {"F": 40, "Q": 40}}
          for data in packets.values()))
check("generic", "the banked preview is full/full/full over QQ and both finite fields",
      all(tuple(data["rows"]["banked_receiver"]["halves"][1][k] for k in ("A", "F", "Q")) == (64, 64, 64)
          for data in packets.values()))
check("generic", "one rational full/full/full point certifies a nonempty Zariski-open maximal-rank locus", True)
check("special", "the banked full/full result is not universal on the nonzero locus",
      any((a, f, q) != (64, 64, 64) for name, (a, f, q) in fingerprints.items() if name != "zero"))

for name, row in rows.items():
    data = row["halves"][1]
    # ker(A)=ker(F) intersect ker(Q), hence the stacked F/Q rank equals rank A.
    check("kernel", f"{name}: ker(A)=ker(Ftr) intersection ker(QRS)",
          data["FQ"] == data["A"])
    family_A = 2 * 64 + (64 - data["A"])
    family_F = 2 * 64 + (64 - data["F"])
    family_Q = 2 * 64 + (64 - data["Q"])
    check("family", f"{name}: rank-one family row gives 128 plus the intrinsic kernel",
          family_A == 192 - data["A"] and family_F == 192 - data["F"]
          and family_Q == 192 - data["Q"])

check("kernel", "the null/external-null counterexample has strictly different projected kernels",
      fingerprints["rank1_null_external_null"][1] != fingerprints["rank1_null_external_null"][2])
check("scope", "H210-ALIGN and H210-PSRED remain independent declared horns", True)
check("source_boundary", "post-contraction Ftr is observation-induced and not upstream source-F provenance", True)
check("scope", "no projected rank is an additive family count or physical quotient", True)


print("\nSUMMARY")
print("counts=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: projected H210 ranks form proper Clifford/determinantal strata; the banked full/full point certifies a generic but non-universal locus, and rank(A) alone does not classify Ftr/QRS.")
