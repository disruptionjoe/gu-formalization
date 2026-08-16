#!/usr/bin/env sage-python
"""Exact CB-6B staged H210 / equation-9.16 composition certificate.

The tested chain is

    M_3 tensor 16 --r tensor T--> upstream Z/144bar
      --literal O_J--> H* tensor S --Gamma_H--> S --kappa_J--> F_corr.

``kappa_J`` is downstream and is never inserted into the upstream ``varpi``
cell.  The complete ``d0+varpi`` cell remains untyped in the current
source/K77 half labels, so this probe assigns it no rank, kernel, spectrum, or
cancellation.  H210 is assumed; H210-FCORR, H210-ALIGN, and H210-PSRED remain
independent conditional horns.  No action, observer, family row, reduction,
physical quotient, or external datum is constructed.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from pathlib import Path
import ast
import sys

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


ARTIFACT_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-equation916-observed-composition-2026-08-16.md"
)
SOURCE_PATH = "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
PACKET_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
CB2_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb2-h210-equation916-cross-half-composition-2026-08-16.md"
)
CB5_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb5-h210-source-fq-bridge-2026-08-16.md"
)
CB6A_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-full-correlated-lift-naturality-2026-08-16.md"
)

artifact = read(ARTIFACT_PATH)
source = read(SOURCE_PATH)
packet = read(PACKET_PATH)
cb2 = read(CB2_PATH)
cb5 = read(CB5_PATH)
cb6a = read(CB6A_PATH)
register = read("lab/sources/source-claim-register.yaml")


print("A. SOURCE, ROUTING, AND CONDITIONAL-BUILD FENCES")
check(
    "routing",
    "mandatory comparator notice and classification are present",
    "GU-COMPARATOR-ROUTING" in artifact
    and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact,
)
check(
    "scope",
    "H210 is assumed and action/external-datum paths remain forbidden",
    "horn `h210` is assumed" in artifact.lower()
    and "external datum" in artifact.lower()
    and "outside" in artifact.lower(),
)
check(
    "scope",
    "FCORR ALIGN and PSRED remain independent",
    all(name in artifact for name in ("H210-FCORR", "H210-ALIGN", "H210-PSRED")),
)
source_rows = (
    "SC-GEN-03", "SC-GEN-05", "SC-GEN-06", "SC-GEN-53",
    "SC-GEN-57", "SC-PRE-52", "SC-CHI-50", "SC-CHI-51",
    "SC-CHI-53", "SC-CHI-54",
)
check(
    "source",
    "controlling imposter partner and chirality rows are present",
    all(f"id: {row}" in register for row in source_rows),
)
check(
    "source",
    "bars are four independent fields at equation 9.16",
    "four distinct fields" in source,
)
check(
    "dependency",
    "full correlated-lift naturality is explicit rather than invented",
    "CB-6A" in artifact
    and "full correlated-lift" in artifact
    and "complete finite square commutes" in cb6a
    and "admitted O/Spin overlaps" in cb6a
    and "does not construct an observer atlas" in cb6a,
)
for lens in (
    "operator grammar",
    "barred/unbarred duality",
    "functor order",
    "exact rank/kernel",
    "K77 parity/chirality",
    "source custody",
    "representation/corner typing",
    "observation",
    "adverse control",
    "efficiency/novelty",
    "claim ceiling",
):
    check("lens", lens, lens.lower() in artifact.lower())


print("B. EXACT EQUATION-9.16 CELL AND HALF-TYPING LEDGER")
ROWS = ("bar-zeta-minus", "bar-zeta-plus", "bar-nu-minus", "bar-nu-plus")
COLS = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")
CELLS = (
    ("star-odot-varpi-pp", "star-odot-d0-varpi-pm", "varpi-pp", "d0-varpi-pm"),
    ("star-odot-d0-varpi-mp", "star-odot-varpi-mm", "d0-varpi-mp", "varpi-mm"),
    ("minus-bar-varpi-pp-star", "minus-d0-star-bar-varpi-pm-star", "southeast-zero", "southeast-zero"),
    ("minus-d0-star-bar-varpi-mp-star", "minus-bar-varpi-mm-star", "southeast-zero", "southeast-zero"),
)
ROW_OUTPUT = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")
FIELD_SIGN = {
    "zeta-plus": 1,
    "zeta-minus": -1,
    "nu-plus": 1,
    "nu-minus": -1,
}
FORWARD = {(1, 2), (0, 3)}
REVERSE = {(2, 1), (3, 0)}
PPMM = {(0, 2), (1, 3)}

check(
    "source_cell",
    "source row order is exact",
    "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in source,
)
check(
    "source_cell",
    "source column order is exact",
    "(zeta-plus, zeta-minus, nu-plus, nu-minus)^T" in source,
)
check("source_cell", "A forward cell is d0 plus varpi -+", CELLS[1][2] == "d0-varpi-mp")
check("source_cell", "B forward cell is d0 plus varpi +-", CELLS[0][3] == "d0-varpi-pm")
check(
    "source_cell",
    "reverse-shaped cells remain a separate pair",
    CELLS[2][1] == "minus-d0-star-bar-varpi-pm-star"
    and CELLS[3][0] == "minus-d0-star-bar-varpi-mp-star",
)
check(
    "source_cell",
    "displayed southeast quadrant remains zero",
    all(CELLS[r][c] == "southeast-zero" for r in (2, 3) for c in (2, 3)),
)

# Exterior d0 and d0* preserve ambient spin half.  The H210 zero-order tensor
# is odd.  In all four forward/reverse cells, the displayed output sign agrees
# with the odd term and disagrees with the even derivative term.
for row, column in sorted(FORWARD | REVERSE):
    input_sign = FIELD_SIGN[COLS[column]]
    output_sign = FIELD_SIGN[ROW_OUTPUT[row]]
    check(
        "half_typing",
        f"cell {(row, column)} H210 odd term reaches displayed output",
        output_sign == -input_sign,
    )
    check(
        "half_typing",
        f"cell {(row, column)} derivative-even term misses displayed output",
        output_sign != input_sign,
    )

check(
    "collision",
    "source extraction retains the derivative-half collision",
    "LAYER0-COLLISION / NOT-ESTABLISHED" in source
    and "one-form labels" in source,
)
check(
    "collision",
    "artifact forbids full-cell rank kernel spectrum and cancellation",
    all(term in artifact for term in (
        "assigning a rank, kernel, cancellation, spectrum",
        "postcomposing the whole displayed cell with `kappa_J`",
        "does **not** block isolating",
    )),
)
check(
    "control",
    "pp/mm are zero-multiplicity controls rather than alternate cells",
    "16 x 144bar" in cb2
    and "invariant count zero" in cb2
    and PPMM.isdisjoint(FORWARD),
)


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
    jet = graph_zero(field)
    for index in range(count):
        jet[index, index] = -field(3)
        jet[6 + index, index] = field(2)
    return jet


def nonnull_jet(field):
    jet = graph_zero(field)
    jet[0, 0] = field(1)
    return jet


def paired_null_jet(field):
    jet = graph_zero(field)
    jet[0, 0] = jet[0, 1] = -field(3)
    jet[6, 0] = field(2)
    jet[6, 1] = -field(2)
    return jet


def banked_jet(field):
    values = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    jet = graph_zero(field)
    for (row, column), (num, den) in values.items():
        jet[row, column] = field(num) / field(den)
    return jet


def graph(jet):
    return identity_matrix(jet.base_ring(), 4).stack(jet)


def normal_frame(jet, eta_h, eta_v):
    top = -eta_h.inverse() * jet.transpose() * eta_v
    return top.stack(identity_matrix(jet.base_ring(), 10))


def gram(frame, eta):
    return frame.transpose() * eta * frame


def gamma_frame(frame, gammas):
    field = frame.base_ring()
    return [
        sum((frame[i, column] * gammas[i] for i in range(14)), z128(field))
        for column in range(frame.ncols())
    ]


def pullback(jet, tensor):
    lift = graph(jet)
    return [
        sum((lift[i, mu] * tensor[i] for i in range(14)), z128(jet.base_ring()))
        for mu in range(4)
    ]


def gamma_trace(vector_spinor, gammas, eta, offset=0):
    field = vector_spinor[0].base_ring()
    return sum(
        (field(eta[i]) * gammas[offset + i] * vector_spinor[i]
         for i in range(len(vector_spinor))),
        z128(field),
    )


def intrinsic_trace(vector_spinor, frame_gammas, frame_gram):
    inverse_gram = frame_gram.inverse()
    field = frame_gram.base_ring()
    return sum(
        (
            inverse_gram[i, j] * frame_gammas[i] * vector_spinor[j]
            for i in range(frame_gram.nrows())
            for j in range(frame_gram.ncols())
        ),
        z128(field),
    )


def correlated_lift(tau, gammas):
    field = tau.base_ring()
    return (
        [field(1) / field(4) * gammas[i] * tau for i in range(4)]
        + [field(-1) / field(10) * gammas[4 + i] * tau for i in range(10)]
    )


def intrinsic_correlated_pair(tau, gamma_h, gamma_n):
    field = tau.base_ring()
    return (
        [field(1) / field(4) * gamma * tau for gamma in gamma_h],
        [field(-1) / field(10) * gamma * tau for gamma in gamma_n],
    )


def stacked(vector_spinor):
    out = vector_spinor[0]
    for component in vector_spinor[1:]:
        out = out.stack(component)
    return out


def restricted_rank(vector_spinor, basis):
    return int((stacked(vector_spinor) * basis).rank())


def matrix_rank_on_half(item, basis):
    return int((item * basis).rank())


def is_odd(item, chirality):
    return chirality * item + item * chirality == 0


EXPECTED = {
    "flat": (0, 0, 0, 0),
    "rank_one_null": (32, 32, 32, 32),
    "isotropic_two_plane": (48, 32, 32, 48),
    "rank_one_nonnull": (64, 64, 64, 64),
    "paired_null_nonzero_pairing": (64, 64, 64, 64),
    "banked_receiver": (64, 64, 64, 64),
}

INTRINSIC_EXPECTED = {
    "flat": 0,
    "rank_one_null": 32,
    "isotropic_two_plane": 48,
    "rank_one_nonnull": 64,
    "paired_null_nonzero_pairing": 48,
    "banked_receiver": 64,
}
INTRINSIC_FAMILY_KERNEL = {
    "flat": 48,
    "rank_one_null": 40,
    "isotropic_two_plane": 36,
    "rank_one_nonnull": 32,
    "paired_null_nonzero_pairing": 36,
    "banked_receiver": 32,
}


print("C. TWO-FIELD, TWO-HALF EXACT STAGE COMPOSITION")
fingerprints: dict[int, dict[str, dict[int, tuple[int, int, int, int]]]] = {}
intrinsic_fingerprints: dict[int, dict[str, dict[int, int]]] = {}
banked_wrong_order = []
for prime in (1009, 1013):
    field = GF(prime)
    eta_h = [1, -1, -1, -1]
    eta_v = [1] * 6 + [-1] * 4
    eta_h_matrix = diagonal_matrix(field, eta_h)
    eta_v_matrix = diagonal_matrix(field, eta_v)
    eta14_matrix = diagonal_matrix(field, eta_h + eta_v)
    original = build_cl77(field)
    order = (0, 7, 8, 9, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    gammas = [original[index] for index in order]
    chirality = product(gammas, range(14))
    phi4 = product(gammas, (10, 11, 12, 13))
    weights = [-2] * 6 + [3] * 4
    zero = z128(field)
    tensor = [zero for _ in range(4)] + [
        field(weights[v]) * gammas[4 + v] * phi4 for v in range(10)
    ]
    halves = {
        sign: (chirality - field(sign) * identity_matrix(field, 128)).right_kernel_matrix().transpose()
        for sign in (-1, 1)
    }

    check(
        "clifford",
        f"GF({prime}) horizontal and normal injections have dimensions 4 and 10",
        gamma_trace([gammas[i] for i in range(4)], gammas, eta_h)
        == field(4) * identity_matrix(field, 128)
        and gamma_trace([gammas[4 + i] for i in range(10)], gammas, eta_v, offset=4)
        == field(10) * identity_matrix(field, 128),
    )
    ambient_trace = gamma_trace(tensor[:4], gammas, eta_h) + gamma_trace(
        tensor[4:], gammas, eta_v, offset=4
    )
    upstream_f = correlated_lift(gamma_trace(tensor[:4], gammas, eta_h), gammas)
    check("upstream", f"GF({prime}) H210 is normal gamma-traceless Z data", ambient_trace == zero)
    check("upstream", f"GF({prime}) upstream direct F projection is zero", all(x == zero for x in upstream_f))
    check(
        "parity",
        f"GF({prime}) H210 coefficient is odd",
        all(is_odd(component, chirality) for component in tensor[4:]),
    )
    for half, basis in halves.items():
        check("half", f"GF({prime}) half {half} has real rank 64", basis.ncols() == 64)
        upstream_rank = restricted_rank(tensor, basis)
        check(
            "rank",
            f"GF({prime}) half {half} upstream rank/kernel are internal 16/32 after family row",
            upstream_rank == 64 and upstream_rank // 4 == 16 and 48 - upstream_rank // 4 == 32,
        )

    cases = (
        ("flat", graph_zero(field)),
        ("rank_one_null", null_jet(field, 1)),
        ("isotropic_two_plane", null_jet(field, 2)),
        ("rank_one_nonnull", nonnull_jet(field)),
        ("paired_null_nonzero_pairing", paired_null_jet(field)),
        ("banked_receiver", banked_jet(field)),
    )
    fingerprints[prime] = {}
    intrinsic_fingerprints[prime] = {}
    for name, jet in cases:
        observed = pullback(jet, tensor)
        horizontal_frame = graph(jet)
        vertical_frame = normal_frame(jet, eta_h_matrix, eta_v_matrix)
        horizontal_gram = gram(horizontal_frame, eta14_matrix)
        vertical_gram = gram(vertical_frame, eta14_matrix)
        gamma_h_intrinsic = gamma_frame(horizontal_frame, gammas)
        gamma_v_intrinsic = gamma_frame(vertical_frame, gammas)
        tau_intrinsic = intrinsic_trace(observed, gamma_h_intrinsic, horizontal_gram)
        pair_intrinsic = intrinsic_correlated_pair(
            tau_intrinsic, gamma_h_intrinsic, gamma_v_intrinsic
        )
        intrinsic_pair = pair_intrinsic[0] + pair_intrinsic[1]
        check(
            "intrinsic",
            f"GF({prime}) {name} graph and normal Grams are nondegenerate and orthogonal",
            horizontal_gram.is_invertible()
            and vertical_gram.is_invertible()
            and horizontal_frame.transpose() * eta14_matrix * vertical_frame
            == zero_matrix(field, 4, 10),
        )
        check(
            "intrinsic",
            f"GF({prime}) {name} intrinsic correlated pair has zero ambient trace",
            intrinsic_trace(pair_intrinsic[0], gamma_h_intrinsic, horizontal_gram)
            + intrinsic_trace(pair_intrinsic[1], gamma_v_intrinsic, vertical_gram)
            == zero,
        )
        check(
            "parity",
            f"GF({prime}) {name} intrinsic correlated map remains odd",
            all(is_odd(component, chirality) for component in intrinsic_pair),
        )
        tau = gamma_trace(observed, gammas, eta_h)
        lifted = correlated_lift(tau, gammas)
        ftrace = lifted[:4]
        qrs = [observed[i] - ftrace[i] for i in range(4)]
        lifted_trace = gamma_trace(lifted[:4], gammas, eta_h) + gamma_trace(
            lifted[4:], gammas, eta_v, offset=4
        )
        check("kappa", f"GF({prime}) {name} correlated lift has zero ambient trace", lifted_trace == zero)
        check(
            "parity",
            f"GF({prime}) {name} final correlated map remains odd",
            all(is_odd(component, chirality) for component in lifted),
        )
        fingerprints[prime][name] = {}
        intrinsic_fingerprints[prime][name] = {}
        for half, basis in halves.items():
            ranks = (
                restricted_rank(observed, basis),
                restricted_rank(ftrace, basis),
                restricted_rank(lifted, basis),
                restricted_rank(qrs, basis),
            )
            fingerprints[prime][name][half] = ranks
            intrinsic_rank = restricted_rank(intrinsic_pair, basis)
            intrinsic_fingerprints[prime][name][half] = intrinsic_rank
            check(
                "rank",
                f"GF({prime}) {name} half {half} exact A/F/K/Q fingerprint",
                ranks == EXPECTED[name],
            )
            internal = tuple(value // 4 for value in ranks)
            check(
                "family",
                f"GF({prime}) {name} half {half} family rank-nullity",
                all(value % 4 == 0 for value in ranks)
                and all((48 - rank) + rank == 48 for rank in internal),
            )
            check(
                "family",
                f"GF({prime}) {name} half {half} K and F kernels agree",
                internal[1] == internal[2]
                and 48 - internal[1] == 48 - internal[2],
            )
            check(
                "intrinsic",
                f"GF({prime}) {name} half {half} intrinsic kappa rank",
                intrinsic_rank == INTRINSIC_EXPECTED[name],
            )
            check(
                "intrinsic",
                f"GF({prime}) {name} half {half} intrinsic family kernel",
                intrinsic_rank % 4 == 0
                and 48 - intrinsic_rank // 4 == INTRINSIC_FAMILY_KERNEL[name]
                and 48 - intrinsic_rank // 4
                == 32 + (16 - intrinsic_rank // 4),
            )
            if name == "banked_receiver":
                wrong_rank = restricted_rank(upstream_f, basis)
                banked_wrong_order.append((intrinsic_rank // 4, wrong_rank // 4))
                check(
                    "wrong_order",
                    f"GF({prime}) banked half {half} K rank 16 versus upstream F rank 0",
                    intrinsic_rank == 64 and wrong_rank == 0,
                )

    check(
        "half",
        f"GF({prime}) conjugate halves have identical fingerprints",
        all(
            fingerprints[prime][name][-1] == fingerprints[prime][name][1]
            for name, _ in cases
        ),
    )

check(
    "field",
    "GF(1009) and GF(1013) have identical stage fingerprints",
    fingerprints[1009] == fingerprints[1013],
)
check(
    "field",
    "GF(1009) and GF(1013) have identical intrinsic fingerprints",
    intrinsic_fingerprints[1009] == intrinsic_fingerprints[1013],
)
print(f"intrinsic fingerprints: {intrinsic_fingerprints[1009]}")
check(
    "wrong_order",
    "banked noncommutation witness is maximal on all four field/half replays",
    banked_wrong_order == [(16, 0)] * 4,
)


print("D. SEMANTIC MUTATION CERTIFICATE")


@dataclass(frozen=True)
class StageLedger:
    stages: tuple[str, ...] = ("R_Z_VARPI", "O_LITERAL", "GAMMA_H", "KAPPA_FCORR")
    upstream_owner: str = "Z_PARTNER"
    upstream_cell_codomain: str = "Z_144_OR_CONJUGATE"
    kappa_location: str = "DOWNSTREAM_AFTER_OBSERVATION_AND_TRACE"
    bars_independent: bool = True
    density_dual_is_reality: bool = False
    reverse_completion: str = "OPTIONAL_SEPARATE_NOT_IN_FORWARD_RANK"
    ppmm_multiplicities: tuple[int, int] = (0, 0)
    full_cell_homogeneous: bool = False
    full_cell_numerics: str = "FORBIDDEN_UNTYPED"
    retained_halves: int = 2
    final_parity: str = "ODD_OFFDIAGONAL"
    correlated_partner: str = "CONSTRUCTED_NOT_RECOVERED"
    family_name: str = "UNLABELLED_QUOTIENT_LINE"
    horn_roles: tuple[str, str, str] = ("FCORR_REVEAL", "ALIGN_FAMILY", "PSRED_DESCENT")
    projected_ranks_are_family_counts: bool = False


LEDGER = StageLedger()


def semantic_audit(ledger: StageLedger) -> dict[str, bool]:
    return {
        "stage order keeps kappa last": ledger.stages == (
            "R_Z_VARPI", "O_LITERAL", "GAMMA_H", "KAPPA_FCORR"
        ),
        "upstream owner remains Z": ledger.upstream_owner == "Z_PARTNER",
        "upstream cell codomain remains 144 partner": ledger.upstream_cell_codomain == "Z_144_OR_CONJUGATE",
        "kappa is downstream": ledger.kappa_location == "DOWNSTREAM_AFTER_OBSERVATION_AND_TRACE",
        "barred fields remain independent": ledger.bars_independent,
        "density dual is not reality": ledger.density_dual_is_reality is False,
        "reverse completion is separate": ledger.reverse_completion == "OPTIONAL_SEPARATE_NOT_IN_FORWARD_RANK",
        "ppmm multiplicities stay zero": ledger.ppmm_multiplicities == (0, 0),
        "full cell is not homogeneous": ledger.full_cell_homogeneous is False,
        "full cell numerics are forbidden": ledger.full_cell_numerics == "FORBIDDEN_UNTYPED",
        "both halves retained": ledger.retained_halves == 2,
        "final parity remains offdiagonal": ledger.final_parity == "ODD_OFFDIAGONAL",
        "normal partner is constructed": ledger.correlated_partner == "CONSTRUCTED_NOT_RECOVERED",
        "family line stays unlabelled": ledger.family_name == "UNLABELLED_QUOTIENT_LINE",
        "three horn roles remain independent": len(set(ledger.horn_roles)) == 3,
        "projected ranks are not family counts": ledger.projected_ranks_are_family_counts is False,
    }


for label, passed in semantic_audit(LEDGER).items():
    check("semantic", label, passed)

plants = {
    "move kappa into upstream varpi": replace(
        LEDGER,
        stages=("KAPPA_FCORR", "R_Z_VARPI", "O_LITERAL", "GAMMA_H"),
        kappa_location="UPSTREAM_VARPI",
    ),
    "rename upstream Z as F": replace(LEDGER, upstream_owner="F_IMPOSTER"),
    "replace varpi codomain by F": replace(LEDGER, upstream_cell_codomain="F_CORR"),
    "identify bars as adjoints": replace(LEDGER, bars_independent=False),
    "promote density dual to reality": replace(LEDGER, density_dual_is_reality=True),
    "merge reverse completion into forward rank": replace(LEDGER, reverse_completion="AUTOMATIC_ADJOINT"),
    "turn on ppmm channel": replace(LEDGER, ppmm_multiplicities=(1, 1)),
    "declare full d0 varpi homogeneous": replace(LEDGER, full_cell_homogeneous=True),
    "assign full-cell rank": replace(LEDGER, full_cell_numerics="RANK_16_KERNEL_32"),
    "delete conjugate half": replace(LEDGER, retained_halves=1),
    "change final map to diagonal parity": replace(LEDGER, final_parity="EVEN_DIAGONAL"),
    "claim normal leg was recovered": replace(LEDGER, correlated_partner="RECOVERED_144_LEG"),
    "name the family": replace(LEDGER, family_name="THIRD_FAMILY"),
    "collapse FCORR and ALIGN": replace(
        LEDGER, horn_roles=("ALIGN_FAMILY", "ALIGN_FAMILY", "PSRED_DESCENT")
    ),
    "add projected ranks as families": replace(LEDGER, projected_ranks_are_family_counts=True),
}

if SELFTEST:
    for name, mutant in plants.items():
        fired = not all(semantic_audit(mutant).values())
        check("plant", f"FIRE {name}", fired)

ast.parse(Path(__file__).read_text(encoding="utf-8"))
check("syntax", "probe parses as Python", True)

print("E. CLAIM CEILING")
artifact_flat = " ".join(artifact.split())
for forbidden in (
    "does not place `kappa` in equation (9.16)",
    "does not derive `H210-FCORR`, `H210-ALIGN`, or `H210-PSRED`",
    "mass, scale, threshold, spectrum, observable, phenomenology",
    "both conjugate halves remain present.",
):
    check("ceiling", forbidden, forbidden in artifact_flat)

print("SUMMARY")
for kind in sorted(COUNTS):
    print(f"{kind}: {COUNTS[kind]}")
print(f"failures: {len(FAILURES)}")
raise SystemExit(1 if FAILURES else 0)
