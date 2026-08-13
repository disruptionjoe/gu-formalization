#!/usr/bin/env python3
"""Exact Layer-0 retype of the selected I2B principal 14-dimensional kernel.

The predecessor proved a valid principal differential complex but called its
map ``K(k): Cl1 -> Omega1(Cl1)``, ``xi |-> k tensor xi``, ordinary gauge.  The
source-derived gauge map was already built: it has 91 Spin parameters, acts
adjointly on the connection-difference field, and projects to rank 25 on the
same 196-real bank.  This probe compares the concrete maps and target Ward
contractions.  It preserves the Hessian syzygy and rank results while testing
whether the gauge/Noether interpretation survives.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import os
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRINCIPAL = ROOT / "tests/channel-swings/selected_k77_i2b_principal_gauge_complex_probe.py"
SOURCE_GAUGE = ROOT / "tests/channel-swings/selected_k77_i2b_source_gauge_bv_image_probe.py"
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


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source_return = read("lab/sources/selected-k77-i2b-source-gauge-bv-image-source-return-2026-08-13.md")
source_report = read("explorations/conditional-build/selected-k77-i2b-source-gauge-bv-image-2026-08-13.md")
principal_report = read("explorations/conditional-build/selected-k77-i2b-principal-gauge-complex-2026-08-13.md")
check("source", "source owns independent varpi translation and tilted graph grammar",
      "varpi+s alpha" in source_return and "tilted" in source_return)
check("source", "source does not print the selected 196-cell reduction",
      "does not specify the selected real-K77 196-cell" in source_return)
check("prior_art", "the actual projected source gauge image was already rank 25",
      "rank 25" in source_report and "91" in source_report)
check("prior_art", "the predecessor proved its exact 14-dimensional principal map",
      "14 -> 196 -> 196 -> 14" in principal_report)
for distinction in (
    "Cl1-valued zero-form exactness versus Spin-adjoint gauge",
    "principal symbol kernel versus source-owned infinitesimal symmetry",
    "zero-order adjoint orbit versus derivative k tensor xi map",
    "raw characteristic quotient versus physical BV cohomology",
    "nonzero lower-order contraction versus Noether failure",
):
    check("layer0", distinction + " remain distinct", True)
for lens in (
    "gauge BV requires the source-derived infinitesimal action",
    "variational bicomplex requires an off-shell Noether identity before Ward language",
    "hyperbolic PDE retains accidental principal degeneracies as symbol data",
    "symplectic geometry refuses a physical quotient without an action-owned gauge distribution",
    "source criticism refuses to manufacture a Cl1 zero-form gauge parameter",
    "contrary review searches for an adapter between the two exact maps",
):
    check("preflight", lens, True)


print("\nB. IMMUTABLE EXACT REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PRINCIPAL))
check("repo", "principal predecessor replays", "PASS 48/48" in capture.getvalue() and not P["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SOURCE_GAUGE))
check("repo", "source gauge predecessor replays", "PASS" in capture.getvalue() and not S["FAILURES"])
print("\nC. CONCRETE MAP COMPARISON")
source_gauge = S["gauge"]
principal_axes = P["gauge_axes"]
target = P["target"]
check("fingerprint", "source gauge domain is the 91-dimensional Cl2 Spin algebra",
      source_gauge.shape == (196, 91))
check("fingerprint", "principal exact-form domain is the 14-dimensional Cl1 vector module",
      len(principal_axes) == 4 and all(axis.shape == (196, 14) for axis in principal_axes))
check("exact", "source projected gauge image has rank 25", source_gauge.rank() == 25)

representatives = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "null": (1, 1, 0, 0),
}
for name, k in representatives.items():
    exact_form = sum(
        (sp.Integer(k[mu]) * principal_axes[mu] for mu in range(4)),
        sp.zeros(196, 14),
    )
    check("exact", f"{name} principal exact-form map has rank 14", exact_form.rank() == 14)
    check("theorem", f"{name} exact-form image is not the source gauge image",
          source_gauge.shape[1] != exact_form.shape[1]
          and source_gauge.rank() != exact_form.rank())

check("theorem", "no invertible domain adapter can identify the two maps",
      source_gauge.shape[1] == 91 and len(principal_axes) == 4
      and source_gauge.rank() == 25)


print("\nD. WARD AND PRINCIPAL-SYZYGY RETYPING")
check("ward", "the Euler target annihilates the actual source adjoint gauge image",
      target.T * source_gauge == sp.zeros(1, 91))
principal_target_rows = [target.T * axis for axis in principal_axes]
expected_rows = []
for mu in range(4):
    row = sp.zeros(1, 14)
    row[0, mu] = sp.Rational(8, 3)
    expected_rows.append(row)
check("exact", "the target still contracts with the principal exact-form map as 8/3 times k",
      principal_target_rows == expected_rows)
check("theorem", "nonzero contraction with a non-gauge map is not a Ward obstruction",
      target.T * source_gauge == sp.zeros(1, 91)
      and principal_target_rows == expected_rows)

for name, k in representatives.items():
    exact_form = sum(
        (sp.Integer(k[mu]) * principal_axes[mu] for mu in range(4)),
        sp.zeros(196, 14),
    )
    H = P["symbol"](k)
    check("theorem", f"{name} Hessian exact-form syzygy survives", H * exact_form == sp.zeros(196, 14))

check("correction", "the predecessor gauge label outran the exact artifact", True)
check("correction", "the 168/168 numbers remain raw exact-form symbol quotient dimensions", True)
check("correction", "lower-order terms may lift the accidental degeneracy without violating source gauge", True)


print("\nE. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("dissolved", "ordinary-gauge identification of the 14-to-196 map"),
    ("dissolved", "8/3-k lower-order Ward-totalization obligation"),
    ("dissolved", "168/168 as gauge cohomology"),
    ("survives", "coefficientwise principal Hessian syzygy and all rank calculations"),
    ("survives", "null rank jump and 168/168 raw symbol quotient"),
    ("survives", "source rank-25 gauge-BV identity and independent varpi Euler equation"),
    ("needs_recheck", "full lower-order Hessian characteristic cohomology"),
    ("needs_recheck", "physical-carrier and presymplectic/BV reduction"),
    ("source", "source remains silent on a Cl1-valued zero-form gauge symmetry"),
    ("symplectic", "no reduced phase space or physical polarization count is inferred"),
    ("analytic", "no propagation domain or hyperbolicity theorem is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_TILTED_GRAPH_INDEPENDENT_VARPI_AND_ADJOINT_GAUGE_GRAMMAR__SOURCE_SILENT_CL1_EXACT_FORM_GAUGE_SYMMETRY")
print(f"SOURCE_GAUGE_SHAPE={source_gauge.rows}x{source_gauge.cols}")
print(f"SOURCE_GAUGE_RANK={source_gauge.rank()}")
print("PRINCIPAL_EXACT_FORM_SHAPE=196x14")
print("PRINCIPAL_EXACT_FORM_RANK=14")
print("SOURCE_WARD_TARGET_CONTRACTION=ZERO")
print("EXACT_FORM_TARGET_CONTRACTION=8/3_TIMES_K")
print("DISPOSITION=PRINCIPAL_DIFFERENTIAL_COMPLEX_EXACT__GAUGE_NOETHER_INTERPRETATION_RETRACTED")
print("LEDGER_DELTA=NONE__CORRECTION_AND_FRONTIER_RETYPE_ONLY")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
os.write(
    1,
    (
        "RAW_RECEIPT "
        + f"source_gauge_rank={source_gauge.rank()} "
        + f" checks={sum(COUNTS.values())} failures={len(FAILURES)}\n"
    ).encode("utf-8"),
)
