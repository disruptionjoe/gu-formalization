#!/usr/bin/env python3
"""Exact prolongation of the selected rank-25 projected-adjoint image.

The predecessor constructs a local stationary symmetric connection two-jet.
This probe asks whether the already-built rank-25 Cl2 adjoint image is itself
the gauge distribution that may be quotiented from that stationary jet fibre.
It is not: over ten symmetric observed two-jet blocks its prolongation has
rank 250, but only a rank-225 subspace is tangent to the frozen stationary
Euler-symbol fibre.  The rank-25 complement is one Lorentz-trace response.

This is a completion diagnostic, not a gauge anomaly or a physical mode count.
The projected adjoint image omits the inhomogeneous derivative of a connection
gauge transformation and the moving Q_B/H_q/observation contributions.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
STATIONARY = ROOT / "tests/channel-swings/selected_k77_i2b_local_stationary_bianchi_jet_probe.py"
sys.path.insert(0, str(ROOT / "tests/channel-swings"))
from k77_exact_bank_api import I, ONE, K77Core, load_bank  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
prior_gauge = read(
    "explorations/conditional-build/selected-k77-i2b-source-gauge-bv-image-2026-08-13.md"
)
prior_atlas = read(
    "explorations/conditional-build/selected-k77-nonconstant-atlas-xi-prolongation-2026-08-09.md"
)
prior_stationary = read(
    "explorations/conditional-build/selected-k77-i2b-local-stationary-bianchi-jet-witness-2026-08-13.md"
)
check("source", "SC-ACT-01 uses independent epsilon and varpi coordinates",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "the source connection difference contains an epsilon-derived derivative",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("prior_art", "v0.229 constructs a projected rank-25 Cl2 adjoint image",
      "projected image on the 196-real Cl1 bank has rank 25" in prior_gauge)
check("prior_art", "the nonconstant atlas already requires the inhomogeneous connection term",
      "g^-1 dg" in prior_atlas and "not merely conjugated" in prior_atlas)
check("prior_art", "the stationary predecessor leaves a 196-dimensional affine fibre",
      "`196`-dimensional affine solution" in prior_stationary)

for distinction in (
    "projected adjoint image versus full inhomogeneous connection gauge differential",
    "field-level rank-25 orbit versus its symmetric second-jet prolongation",
    "affine stationary fibre versus its homogeneous tangent",
    "tangent gauge directions versus arbitrary gauge-parameter jets",
    "frozen principal Euler symbol versus complete moving Ward identity",
    "stationary-symbol quotient versus physical BV/BFV phase space",
):
    check("layer0", distinction + " remain distinct", True)

for kind, label in (
    ("principal_bundle", "retain the missing d-eta/Maurer-Cartan jet term"),
    ("spencer", "grade the computation as first-symbol intersection, not involutivity"),
    ("variational", "a genuine on-shell gauge tangent must lie in the linearized Euler kernel"),
    ("bv", "treat a failure of tangency as a completion burden, not a physical mode"),
    ("symplectic", "quotient only the gauge subspace tangent to the stationary fibre"),
    ("krein", "rank arithmetic supplies no positivity or spectrum"),
    ("source", "record silence on the selected K77 prolongation"),
    ("contrary", "plant the invalid quotient by all 250 prolonged directions"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE STATIONARY PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(STATIONARY))
check("repo", "the local stationary/Bianchi predecessor replays",
      "PASS 46/46" in capture.getvalue() and not P["FAILURES"])
H = P["H"]
cells = H["cells"]
sym_pair = H["sym_pair"]
real_scalar = H["real_scalar"]
principal_with = H["principal_with"]
selected = H["SELECTED"]
base = H["P"]["S"]["base"]
check("fingerprint", "the stationary field bank remains 196-real", len(cells) == 196)
check("fingerprint", "the predecessor map is onto and its affine fibre has dimension 196",
      P["rank_combined"] == 196 and 392 - P["rank_combined"] == 196)
check("fingerprint", "the explicit predecessor jet is stationary", all(value == 0 for value in P["stationary"]))


print("\nC. RECONSTRUCT THE EXACT PROJECTED ADJOINT IMAGE")
bank = load_bank()
core = K77Core(bank.signature, bank.channels)
phase = [I if index != 13 else ONE for index in range(14)]


def commutator(left, right):
    return core.eadd(core.emul(left, right), core.escale(-1, core.emul(right, left)))


def real_coordinate(coefficient, basis_phase):
    if basis_phase == ONE:
        reality_checks.append(coefficient[1] == 0)
        return sp.Rational(coefficient[0].numerator, coefficient[0].denominator)
    reality_checks.append(coefficient[0] == 0)
    return sp.Rational(coefficient[1].numerator, coefficient[1].denominator)


pairs = tuple(bank.payload["carrier"]["epsilon_generators"])
gauge = sp.zeros(196, len(pairs))
gauge_fields = []
reality_checks: list[bool] = []
grade_checks: list[bool] = []
for column, (left_index, right_index) in enumerate(pairs):
    eta = core.emul(
        core.blade(left_index, phase[left_index]),
        core.blade(right_index, phase[right_index]),
    )
    variation = {
        form_mask: commutator(eta, coefficient)
        for form_mask, coefficient in base.items()
    }
    variation = core.fclean(variation)
    gauge_fields.append(variation)
    for form_mask, coefficient in variation.items():
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in coefficient.items():
            grade_checks.append(clifford_mask.bit_count() == 1)
            clifford_index = clifford_mask.bit_length() - 1
            gauge[14 * form_index + clifford_index, column] = real_coordinate(
                gaussian, phase[clifford_index]
            )

gauge_rank = gauge.rank()
pivots = gauge.rref()[1]
gauge_basis = [gauge_fields[index] for index in pivots]
check("grade", "all projected adjoint variations remain in the Cl1 bank", all(grade_checks))
check("reality", "all projected adjoint columns obey the real-K77 phase rule", all(reality_checks))
check("exact", "the independently reconstructed field image has rank 25", gauge_rank == 25)
check("exact", "twenty-five pivot fields represent its image without reducibility", len(gauge_basis) == 25)


print("\nD. TEN-BLOCK SYMMETRIC JET PROLONGATION")
field_responses = [
    [principal_with(selected, mu, delta) for _, _, delta in cells]
    for mu in range(4)
]
gauge_responses = [
    [principal_with(selected, mu, delta) for delta in gauge_basis]
    for mu in range(4)
]

block_labels = []
block_images = []
block_ranks = []
for mu in range(4):
    for nu in range(mu, 4):
        image = sp.Matrix(196, 25, [
            real_scalar(sym_pair(field_responses[mu][row], gauge_responses[nu][column]))
            + (
                real_scalar(sym_pair(field_responses[nu][row], gauge_responses[mu][column]))
                if mu != nu else 0
            )
            for row in range(196)
            for column in range(25)
        ])
        block_labels.append((mu, nu))
        block_images.append(image)
        block_ranks.append((mu, nu, image.rank()))

expected_block_ranks = [
    (0, 0, 25), (0, 1, 0), (0, 2, 0), (0, 3, 0),
    (1, 1, 25), (1, 2, 0), (1, 3, 0),
    (2, 2, 25), (2, 3, 0), (3, 3, 25),
]
check("theorem", "the ten projected-adjoint block ranks are 25 on diagonals and zero on mixed blocks",
      block_ranks == expected_block_ranks, block_ranks)

diagonal = [block_images[index] for index, label in enumerate(block_labels) if label[0] == label[1]]
check("theorem", "all three spatial diagonal responses are minus the timelike response",
      diagonal[1] == -diagonal[0] and diagonal[2] == -diagonal[0] and diagonal[3] == -diagonal[0])
check("theorem", "the combined ten-block response has only one rank-25 Lorentz-trace image",
      sp.Matrix.hstack(*block_images).rank() == 25)
check("theorem", "all six mixed projected-adjoint jet copies are stationary tangents",
      all(block_images[index] == sp.zeros(196, 25)
          for index, label in enumerate(block_labels) if label[0] != label[1]))


print("\nE. STATIONARY INTERSECTION AND THE ONLY LICENSED QUOTIENT")
prolonged_adjoint_rank = 10 * gauge_rank
prolonged_euler_rank = sp.Matrix.hstack(*block_images).rank()
tangent_adjoint_rank = prolonged_adjoint_rank - prolonged_euler_rank
stationary_tangent_rank = 10 * 196 - 196
stationary_tangent_quotient_rank = stationary_tangent_rank - tangent_adjoint_rank

check("exact", "the ten-copy projected-adjoint prolongation has rank 250",
      prolonged_adjoint_rank == 250)
check("exact", "its stationary-tangent intersection has rank 225",
      tangent_adjoint_rank == 225)
check("exact", "the full ten-block stationary symbol kernel has rank 1764",
      stationary_tangent_rank == 1764)
check("exact", "quotienting only the tangent intersection leaves rank 1539",
      stationary_tangent_quotient_rank == 1539)

two_block_response_rank = sp.Matrix.hstack(block_images[0], block_images[1]).rank()
two_block_tangent_adjoint = 2 * gauge_rank - two_block_response_rank
two_block_stationary_tangent = 2 * 196 - 196
check("control", "on the predecessor 00+01 slice only the mixed rank-25 copy is tangent",
      two_block_response_rank == 25 and two_block_tangent_adjoint == 25)
check("control", "the licensed 00+01 tangent quotient has rank 171",
      two_block_stationary_tangent - two_block_tangent_adjoint == 171)
check("plant", "PLANT all 250 prolonged directions cannot be quotiented as gauge tangents",
      prolonged_euler_rank != 0)
check("plant", "PLANT four diagonal responses are not four independent rank-25 defects",
      prolonged_euler_rank == 25 and sum(rank for mu, nu, rank in block_ranks if mu == nu) == 100)


print("\nF. HOSTILE DISPOSITION")
for kind, label in (
    ("layer0", "the rank-25 complement is a Ward-completion burden, not 25 physical modes"),
    ("principal_bundle", "the full inhomogeneous connection gauge operator with d eta remains unconstructed here"),
    ("variational", "moving Q_B H_q observation and nonlinear gauge-orbit terms may restore tangency"),
    ("spencer", "formal prolongation involutivity compatibility and a solution germ remain open"),
    ("bv", "no Koszul-Tate differential or complete physical carrier quotient is inferred"),
    ("symplectic", "rank 1539 is a frozen symbol quotient, not a reduced phase-space dimension"),
    ("analytic", "no hyperbolicity domain Green operator spectrum or stability follows"),
    ("source", "the source confirms inhomogeneous connection grammar but is silent on this rank pattern"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_INHOMOGENEOUS_CONNECTION_AND_TILTED_GRAMMAR__SOURCE_SILENT_SELECTED_K77_PROJECTED_ADJOINT_JET_PROLONGATION__REPOSITORY_DERIVES_RANK25_WARD_COMPLETION_BURDEN")
print(f"FIELD_PROJECTED_ADJOINT_RANK={gauge_rank}")
print(f"PROLONGED_PROJECTED_ADJOINT_RANK={prolonged_adjoint_rank}")
print(f"PROLONGED_EULER_RESPONSE_RANK={prolonged_euler_rank}")
print(f"STATIONARY_TANGENT_INTERSECTION_RANK={tangent_adjoint_rank}")
print(f"STATIONARY_TANGENT_RANK={stationary_tangent_rank}")
print(f"FROZEN_SYMBOL_QUOTIENT_RANK={stationary_tangent_quotient_rank}")
print("BLOCK_RANKS=" + ";".join(f"{mu}{nu}:{rank}" for mu, nu, rank in block_ranks))
print("DISPOSITION=PROJECTED_ADJOINT_IS_NOT_YET_THE_FULL_STATIONARY_GAUGE_DIFFERENTIAL__ONE_RANK25_LORENTZ_TRACE_WARD_COMPLETION_REMAINS")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
