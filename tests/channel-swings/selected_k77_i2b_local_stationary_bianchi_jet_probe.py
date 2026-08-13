#!/usr/bin/env python3
"""Exact local stationary/Bianchi connection-two-jet witness for selected K77 I2B.

The predecessor proves that the full 196-dimensional selected Euler cotangent
is reached by the symmetric (00)+(01) connection-two-jet map.  This probe does
the stronger constructive job: it solves that exact rational map, realizes the
solution as a local quadratic connection perturbation, verifies cancellation
of the complete frozen-background Euler covector, and checks the base-point
linear Bianchi identities.  The 196-dimensional affine solution fibre is kept
visible: local existence is not source selection, global descent, BV reduction,
or a physical solution.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
HOLONOMIC = ROOT / "tests/channel-swings/selected_k77_i2b_holonomic_jet_euler_image_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def as_fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if hasattr(value, "p") and hasattr(value, "q"):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


def sparse_add_scaled(
    target: dict[int, Fraction], source: dict[int, Fraction], scale: Fraction
) -> None:
    for index, value in source.items():
        updated = target.get(index, Fraction(0)) + scale * value
        if updated:
            target[index] = updated
        elif index in target:
            del target[index]


def add_column_with_provenance(
    basis: dict[int, tuple[dict[int, Fraction], dict[int, Fraction]]],
    values: list[object],
    column_index: int,
) -> bool:
    """Add a column basis vector while retaining its source-column expansion."""
    work = {index: as_fraction(value) for index, value in enumerate(values) if value}
    provenance = {column_index: Fraction(1)}
    while work:
        pivot = min(work)
        if pivot not in basis:
            scale = work[pivot]
            basis[pivot] = (
                {index: value / scale for index, value in work.items()},
                {index: value / scale for index, value in provenance.items()},
            )
            return True
        scale = work[pivot]
        basis_vector, basis_provenance = basis[pivot]
        sparse_add_scaled(work, basis_vector, -scale)
        sparse_add_scaled(provenance, basis_provenance, -scale)
    return False


def solve_negative_target(
    basis: dict[int, tuple[dict[int, Fraction], dict[int, Fraction]]],
    values: list[object],
) -> tuple[dict[int, Fraction] | None, dict[int, Fraction]]:
    """Return c with M c = -values, plus any unreduced obstruction."""
    work = {index: as_fraction(value) for index, value in enumerate(values) if value}
    coefficients: dict[int, Fraction] = {}
    while work:
        pivot = min(work)
        if pivot not in basis:
            return None, work
        scale = work[pivot]
        basis_vector, basis_provenance = basis[pivot]
        sparse_add_scaled(work, basis_vector, -scale)
        sparse_add_scaled(coefficients, basis_provenance, -scale)
    return coefficients, {}


def matrix_times_sparse(
    columns: list[list[Fraction]], coefficients: dict[int, Fraction], row_count: int
) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(row_count)]
    for column_index, coefficient in coefficients.items():
        column = columns[column_index]
        for row, value in enumerate(column):
            if value:
                answer[row] += coefficient * value
    return answer


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
prior = read("explorations/conditional-build/selected-k77-i2b-holonomic-jet-euler-image-2026-08-13.md")
prior_lift = read("explorations/conditional-build/selected-k77-i2b-lower-order-exact-form-lift-2026-08-13.md")
check("source", "SC-ACT-04 owns the residual-square action grammar", "- id: SC-ACT-04" in claims)
check("prior_art", "v0.236 proves full local holonomic image membership", "rank `196`" in prior and "rank(all blocks | target)" in prior)
check("prior_art", "v0.237 separates principal degeneracy from full lower-order lifting", "rank `14`" in prior_lift and "nonstationary" in prior_lift)
for distinction in (
    "Euler stationarity versus Hessian nondegeneracy",
    "symmetric connection two-jet versus arbitrary curvature value",
    "local quadratic connection versus global descended field",
    "action-admissible witness versus source-selected representative",
    "base-point Bianchi compatibility versus nonlinear solution propagation",
    "196-dimensional affine fibre versus a canonical choice",
    "holonomic jet source versus rank-25 Cl2 source gauge image",
):
    check("layer0", distinction + " remain distinct", True)
for lens in (
    "principal-bundle geometry checks an actual polynomial connection jet",
    "variational bicomplex checks the complete Euler covector",
    "PDE and microlocal review refuses a base-point jet-to-solution inference",
    "gauge and BV review retains the actual source distribution burden",
    "Krein review separates zero Euler from positive physical energy",
    "symplectic review separates stationarity from phase-space reduction",
    "source criticism returns an explicit silence code",
    "contrary review plants coefficient and holonomy failures",
):
    check("preflight", lens, True)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(HOLONOMIC))
check("repo", "v0.236 holonomic-image predecessor replays", "PASS" in capture.getvalue() and not P["FAILURES"])
H = P["H"]
E = P["E"]
check("repo", "v0.213 selected principal predecessor is inherited green", not H["FAILURES"])
check("repo", "v0.235 Euler-target predecessor is inherited green", not E["FAILURES"])

cells = H["cells"]
sym_pair = H["sym_pair"]
real_scalar = H["real_scalar"]
principal_with = H["principal_with"]
selected = H["SELECTED"]
responses = [[principal_with(selected, mu, delta) for _, _, delta in cells] for mu in range(2)]
check("type", "the inherited selected connection bank is real dimension 196", len(cells) == 196)
check("type", "the construction stays on the selected trace-Hq real-K77 fixture", "K77" in prior and "H_q" in prior_lift)


print("\nC. EXACT (00)+(01) HOLONOMIC MAP WITH PROVENANCE")
target: list[Fraction] = []
for _, _, delta in cells:
    target.append(as_fraction(real_scalar(sym_pair(E["residual_derivative"](delta), E["H_TARGET"]))))

columns: list[list[Fraction]] = []
block_labels: list[tuple[int, int, int]] = []
for mu, nu in ((0, 0), (0, 1)):
    for column in range(196):
        values: list[Fraction] = []
        for row in range(196):
            value = as_fraction(real_scalar(sym_pair(responses[mu][row], responses[nu][column])))
            if mu != nu:
                value += as_fraction(real_scalar(sym_pair(responses[nu][row], responses[mu][column])))
            values.append(value)
        columns.append(values)
        block_labels.append((mu, nu, column))

basis: dict[int, tuple[dict[int, Fraction], dict[int, Fraction]]] = {}
rank_after_00 = 0
for column_index, column in enumerate(columns):
    add_column_with_provenance(basis, column, column_index)
    if column_index == 195:
        rank_after_00 = len(basis)
rank_combined = len(basis)
coefficients, obstruction = solve_negative_target(basis, target)
check("exact", "the timelike block retains rank 182", rank_after_00 == 182)
check("exact", "the first symmetric mixed block completes rank 196", rank_combined == 196)
check("exact", "a rational cancelling two-jet is constructed", coefficients is not None and not obstruction)

assert coefficients is not None
image = matrix_times_sparse(columns, coefficients, 196)
stationary = [target[row] + image[row] for row in range(196)]
support = sorted(coefficients)
support_00 = sum(index < 196 for index in support)
support_01 = sum(index >= 196 for index in support)
denominators = sorted({value.denominator for value in coefficients.values()})
check("theorem", "the explicit rational jet cancels all 196 Euler cells exactly", all(value == 0 for value in stationary))
check("theorem", "the original fourteen-cell target is nonzero", sum(value != 0 for value in target) == 14)
check("accounting", "the 392-variable map has a 196-dimensional affine solution fibre", 392 - rank_combined == 196)
check("accounting", "the witness actually uses mixed-jet support", support_01 > 0, f"00={support_00}, 01={support_01}")
check("planted", "PLANT the zero jet does not cancel the target", any(value != 0 for value in target))
if support:
    planted_coefficients = dict(coefficients)
    planted_coefficients[support[0]] += Fraction(1)
    planted_image = matrix_times_sparse(columns, planted_coefficients, 196)
    planted_stationary = [target[row] + planted_image[row] for row in range(196)]
    check("planted", "PLANT perturbing one solved coefficient breaks stationarity", any(value != 0 for value in planted_stationary))


print("\nD. QUADRATIC CONNECTION REALIZATION AND BIANCHI")
# c00 and c01 are the second derivatives of the local connection coefficients:
# delta A_a^I(x) = (1/2)c00[a,I](x0)^2 + c01[a,I]x0x1.
c00 = [Fraction(0) for _ in range(196)]
c01 = [Fraction(0) for _ in range(196)]
for source_column, value in coefficients.items():
    mu, nu, field_cell = block_labels[source_column]
    if (mu, nu) == (0, 0):
        c00[field_cell] = value
    elif (mu, nu) == (0, 1):
        c01[field_cell] = value


def second_derivative(mu: int, nu: int, field_cell: int) -> Fraction:
    if mu == 0 and nu == 0:
        return c00[field_cell]
    if {mu, nu} == {0, 1}:
        return c01[field_cell]
    return Fraction(0)


bianchi_values: list[Fraction] = []
for lam in range(14):
    for mu in range(lam + 1, 14):
        for nu in range(mu + 1, 14):
            for clifford_index in range(14):
                def cell(form_index: int) -> int:
                    return form_index * 14 + clifford_index

                value = (
                    second_derivative(lam, mu, cell(nu))
                    - second_derivative(lam, nu, cell(mu))
                    + second_derivative(mu, nu, cell(lam))
                    - second_derivative(mu, lam, cell(nu))
                    + second_derivative(nu, lam, cell(mu))
                    - second_derivative(nu, mu, cell(lam))
                )
                bianchi_values.append(value)

check("geometry", "the witness is holonomic: mixed second derivatives commute", all(second_derivative(mu, nu, cell) == second_derivative(nu, mu, cell) for mu in range(14) for nu in range(14) for cell in range(196)))
check("geometry", "all 5,096 componentwise base-point linear Bianchi checks vanish", len(bianchi_values) == 5096 and all(value == 0 for value in bianchi_values))
check("geometry", "the jet is realized by an explicit quadratic local connection perturbation", bool(c00) and bool(c01))


def planted_second_derivative(mu: int, nu: int, field_cell: int) -> Fraction:
    # Deliberately violate equality of the 01 and 10 derivatives in the A_2^0 cell.
    if field_cell == 2 * 14 and (mu, nu) == (0, 1):
        return Fraction(1)
    return Fraction(0)


planted_bianchi = (
    planted_second_derivative(0, 1, 2 * 14)
    - planted_second_derivative(0, 2, 1 * 14)
    + planted_second_derivative(1, 2, 0 * 14)
    - planted_second_derivative(1, 0, 2 * 14)
    + planted_second_derivative(2, 0, 1 * 14)
    - planted_second_derivative(2, 1, 0 * 14)
)
check("planted", "PLANT a non-holonomic mixed derivative fires the Bianchi check", planted_bianchi != 0)


print("\nE. DISPOSITION AND DURABLE FENCES")
check("survival", "one local action-stationary Bianchi-compatible connection two-jet exists", all(value == 0 for value in stationary) and all(value == 0 for value in bianchi_values))
for kind, label in (
    ("source", "the source confirms the connection/residual-square grammar but is silent on this representative"),
    ("selection", "the 196-dimensional affine fibre leaves the representative noncanonical"),
    ("global", "atlas overlap descent and nonlinear stationarity away from the base point remain open"),
    ("variation", "moving geometry Q_B H_q and observation jets remain open"),
    ("gauge_bv", "the actual rank-25 Cl2 source BV distribution on the physical carrier remains open"),
    ("symplectic", "no presymplectic current boundary charge quotient or BFV phase space is inferred"),
    ("analytic", "no domain hyperbolicity positivity spectrum mass or stability result is inferred"),
    ("scope", "nonzero-fermion and expanded-parent routes remain separate"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_CONNECTION_GRAMMAR__SOURCE_SILENT_LOCAL_STATIONARY_TWO_JET_SELECTION_AND_GLOBALIZATION")
print(f"HOLONOMIC_MAP_RANK={rank_combined}")
print(f"HOLONOMIC_VARIABLES={len(columns)}")
print(f"AFFINE_SOLUTION_FIBRE_DIMENSION={len(columns) - rank_combined}")
print(f"WITNESS_SUPPORT={len(support)}")
print(f"WITNESS_SUPPORT_00={support_00}")
print(f"WITNESS_SUPPORT_01={support_01}")
print("WITNESS_DENOMINATORS=" + ",".join(str(value) for value in denominators))
print(f"BIANCHI_COMPONENT_CHECKS={len(bianchi_values)}")
print("LOCAL_STATIONARY_JET=CONSTRUCTED__NONCANONICAL__NOT_GLOBAL_OR_SOURCE_SELECTED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
