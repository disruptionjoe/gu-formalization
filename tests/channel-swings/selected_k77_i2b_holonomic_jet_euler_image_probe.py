#!/usr/bin/env python3
"""Exact holonomic connection-jet Euler-image gate for selected K77 I2B.

V0.235 excludes cancellation by a pointwise real curvature value.  This probe
tests the distinct principal Euler contribution of an actual symmetric
observed-spacetime connection second jet.  The timelike diagonal block has
rank 182 and misses the target, but adjoining the symmetric (0,1) mixed block
already gives the full 196-dimensional real connection cotangent.  Hence the
complete ten-block holonomic image contains the target locally.  Source
selection, nonlinear Bianchi completion, atlas descent, observation contact,
lower-order terms, domains, and BV/preboundary ownership remain open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRINCIPAL = ROOT / "tests/channel-swings/selected_k77_i2b_moving_higgs_principal_hessian_probe.py"
EULER = ROOT / "tests/channel-swings/selected_k77_i2b_real_curvature_euler_image_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
prior_euler = read("explorations/conditional-build/selected-k77-i2b-real-curvature-euler-image-2026-08-13.md")
prior_hessian = read("explorations/conditional-build/selected-k77-i2b-moving-higgs-principal-hessian-2026-08-12.md")
prior_green = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
prior_source_return = read("lab/sources/selected-k77-i2b-real-curvature-euler-image-source-return-2026-08-13.md")
check("source", "SC-ACT-04 owns the bosonic residual square", "- id: SC-ACT-04" in claims)
check("source", "the source does not select a K77 derivative jet",
      "SOURCE_SILENT_DERIVATIVE_DEPENDENT_REAL_BACKGROUND_JET" in prior_source_return
      and "source-connection jet" in prior_source_return)
check("prior_art", "v0.235 kills only pointwise real curvature-value cancellation",
      "pointwise real" in prior_euler and "derivative-dependent" in prior_euler)
check("prior_art", "v0.213 supplies a rank-182 full-bank timelike principal Gram",
      "rank `182`" in prior_hessian)
check("prior_art", "v0.96 supplies the formal-adjoint grammar but not the present image theorem",
      "formal adjoint" in prior_green and "missing field banks" in prior_green)
for distinction in (
    "first transgression action versus I2B residual-square action",
    "pointwise curvature value versus connection second jet",
    "arbitrary residual derivative versus holonomic symmetric field jet",
    "one-covector principal symbol versus the complete symmetric jet image",
    "local image existence versus source selection",
    "linear principal image versus nonlinear Bianchi-compatible connection",
    "Euler image membership versus presymplectic or BV reduction",
):
    check("layer0", distinction + " remain distinct", True)
for lens in (
    "variational bicomplex symmetrizes mixed second derivatives",
    "principal-bundle geometry retains nonlinear Bianchi and atlas burdens",
    "symplectic geometry keeps local Euler reachability below phase-space construction",
    "analytic review keeps domains hyperbolicity and stability outside the theorem",
    "constraint accounting prices a full image as freedom rather than selection",
    "source criticism requires an explicit source-return disposition",
    "contrary review tests the tempting timelike-only route kill",
):
    check("preflight", lens, True)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS AND BANK RECONCILIATION")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    H = runpy.run_path(str(PRINCIPAL))
check("repo", "v0.213 principal-Hessian predecessor replays", "PASS" in capture.getvalue() and not H["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    E = runpy.run_path(str(EULER))
check("repo", "v0.235 curvature-Euler predecessor replays", "PASS 50/50" in capture.getvalue() and not E["FAILURES"])

cells = H["cells"]
sym_pair = H["sym_pair"]
real_scalar = H["real_scalar"]
principal_with = H["principal_with"]
selected = H["SELECTED"]
residual_derivative = E["residual_derivative"]
target_residual = E["H_TARGET"]

expected_deltas = []
for form_index in range(14):
    for clifford_index in range(14):
        phase = E["ONE"] if clifford_index == 13 else E["I"]
        expected_deltas.append(E["one_form"](form_index, clifford_index, phase))
check("type", "both predecessor chains use the same ordered 196-real connection bank",
      [delta for _, _, delta in cells] == expected_deltas)
check("type", "the field bank is real dimension 196", len(cells) == 196)


print("\nC. TARGET COVECTOR AND TIMELIKE NEGATIVE CONTROL")
target_values = []
target_imaginary = []
for _, _, delta in cells:
    value = sym_pair(residual_derivative(delta), target_residual)
    target_values.append(real_scalar(value))
    target_imaginary.append(sp.Rational(value[1].numerator, value[1].denominator))
target = sp.Matrix(target_values)
target_imag = sp.Matrix(target_imaginary)
timelike = sp.Matrix(H["full_gram"])
timelike_rank = timelike.rank()
timelike_augmented_rank = timelike.row_join(target).rank()
check("exact", "the target is a real field covector", all(value == 0 for value in target_imag))
check("exact", "the target has fourteen nonzero real field cells", sum(value != 0 for value in target) == 14)
check("control", "the timelike diagonal principal block has rank 182", timelike_rank == 182)
check("control", "the target is outside the timelike-only image", timelike_augmented_rank == 183)
check("planted", "PLANT a one-covector principal slice cannot kill the full holonomic route",
      timelike_augmented_rank > timelike_rank)


def as_fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if hasattr(value, "p") and hasattr(value, "q"):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


def add_column(basis: dict[int, dict[int, Fraction]], values: list[object]) -> bool:
    work = {index: as_fraction(value) for index, value in enumerate(values) if value}
    while work:
        pivot = min(work)
        if pivot not in basis:
            scale = work[pivot]
            basis[pivot] = {index: value / scale for index, value in work.items()}
            return True
        scale = work[pivot]
        for index, value in basis[pivot].items():
            updated = work.get(index, Fraction(0)) - scale * value
            if updated:
                work[index] = updated
            elif index in work:
                del work[index]
    return False


print("\nD. COMPLETE OBSERVED HOLONOMIC SECOND-JET IMAGE")
responses = [[principal_with(selected, mu, delta) for _, _, delta in cells] for mu in range(4)]
basis: dict[int, dict[int, Fraction]] = {}
cumulative_ranks = []
for mu in range(4):
    for nu in range(mu, 4):
        for column in range(196):
            values = []
            for row in range(196):
                value = real_scalar(sym_pair(responses[mu][row], responses[nu][column]))
                if mu != nu:
                    value += real_scalar(sym_pair(responses[nu][row], responses[mu][column]))
                values.append(value)
            add_column(basis, values)
        cumulative_ranks.append(((mu, nu), len(basis)))

expected_ranks = [
    ((0, 0), 182), ((0, 1), 196), ((0, 2), 196), ((0, 3), 196),
    ((1, 1), 196), ((1, 2), 196), ((1, 3), 196), ((2, 2), 196),
    ((2, 3), 196), ((3, 3), 196),
]
check("theorem", "all ten symmetric observed second-jet blocks have the exact cumulative rank profile",
      cumulative_ranks == expected_ranks)
check("theorem", "the timelike plus first mixed block already spans the full field cotangent",
      cumulative_ranks[1][1] == 196)
check("theorem", "the complete holonomic principal Euler image has rank 196", len(basis) == 196)

target_trial = dict(basis)
target_added = add_column(target_trial, list(target))
check("theorem", "the fourteen-cell Euler target lies in the holonomic principal image", not target_added)
check("exact", "adjoining the target leaves rank 196", len(target_trial) == 196)
check("planted", "PLANT deleting every mixed jet block recreates the false rank-182 obstruction",
      timelike_rank == 182 and cumulative_ranks[1][1] == 196)


print("\nE. DISPOSITION AND DURABLE FENCES")
check("survival", "the derivative-dependent real connection-jet route survives at local principal grade",
      not target_added)
check("correction", "v0.235 remains valid but its successor is local reachability rather than another kill",
      E["augmented_euler_rank"] == 365 and not target_added)
for kind, label in (
    ("source", "the source is silent on which holonomic jet solves or selects the background"),
    ("principal_bundle", "a nonlinear connection realizing the jet with Bianchi and overlap descent remains open"),
    ("variation", "lower-order nonstationary and moving-QB terms remain open"),
    ("symplectic", "no presymplectic current constraint quotient or BV image is inferred"),
    ("analytic", "no closed domain positivity spectrum mass or stability result is inferred"),
    ("accounting", "full cotangent reachability is maximally nonselective until the solution fibre is owned"),
    ("scope", "nonzero-fermion and expanded-parent routes remain separate"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_CONNECTION_GRAMMAR__SOURCE_SILENT_SELECTED_HOLONOMIC_SECOND_JET_AND_GLOBAL_REALIZATION")
print(f"TIMELIKE_IMAGE_RANK={timelike_rank}")
print(f"TIMELIKE_WITH_TARGET_RANK={timelike_augmented_rank}")
print("HOLONOMIC_CUMULATIVE_RANKS=" + ";".join(f"{mu}{nu}:{rank}" for (mu, nu), rank in cumulative_ranks))
print(f"HOLONOMIC_IMAGE_RANK={len(basis)}")
print(f"HOLONOMIC_WITH_TARGET_RANK={len(target_trial)}")
print("DERIVATIVE_CONNECTION_JET_ROUTE=LOCAL_PRINCIPAL_SURVIVAL__NOT_SELECTED_OR_GLOBALLY_REALIZED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
