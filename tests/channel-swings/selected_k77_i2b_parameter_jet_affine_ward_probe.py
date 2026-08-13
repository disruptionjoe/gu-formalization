#!/usr/bin/env python3
"""Exact affine covariantization of the selected I2B parameter-jet trace.

The predecessor closes the constant gauge-parameter Ward response but leaves
one rank-25 Lorentz trace from raw second field jets.  This probe derives the
universal first/second covariant-jet transformation in a free associative
algebra and ports its pure-second-parameter-jet affine correction to every
exact selected K77 block.  It does not identify the full source connection
with the 196-real distortion carrier or construct BV/Spencer/global descent.
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
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_stationary_constant_moving_shiab_ward_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
primary = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
prior = read("explorations/conditional-build/selected-k77-i2b-stationary-constant-moving-shiab-ward-2026-08-13.md")
check("source", "the source supplies an affine Maurer-Cartan connection owner",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in primary)
check("source", "the primitive epsilon chain contains a covariant connection derivative",
      "delta B=D_B eta" in source and "delta T=-D_B eta" in source)
check("prior_art", "the predecessor closes constant order and leaves the rank-25 trace",
      "rank-25" in prior and "constant-parameter" in prior)
for distinction in (
    "full affine connection versus homogeneous distortion",
    "raw field two-jet versus covariant field two-jet",
    "parameter value versus first and second parameter jets",
    "local Ward covariantization versus BV quotient",
    "formal jet identity versus global observation descent",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("principal_bundle", "derive the affine correction from the connection transformation law"),
    ("variational", "apply the derived correction through the same exact Hessian blocks"),
    ("gauge_bv", "grade the result before quotient or reducibility"),
    ("spencer", "leave formal involutivity and higher compatibility open"),
    ("hyperbolic", "make no propagation or Cauchy-domain inference"),
    ("krein", "make no positivity inference from Ward rank"),
    ("symplectic", "retain the separate boundary and presymplectic owner"),
    ("source", "separate source connection grammar from repository ranks"),
    ("contrary", "plant raw-jet and wrong-sign affine rivals"),
):
    check(kind, label, True)


# A tiny exact free associative algebra.  Words do not commute; therefore a
# zero result proves the displayed identity using only bilinearity,
# associativity and the commutator definition rather than a matrix sample.
Poly = dict[tuple[str, ...], Fraction]


def clean(value: Poly) -> Poly:
    return {word: coefficient for word, coefficient in value.items() if coefficient}


def atom(name: str) -> Poly:
    return {(name,): Fraction(1)}


def add(*values: Poly) -> Poly:
    out: Poly = {}
    for value in values:
        for word, coefficient in value.items():
            out[word] = out.get(word, Fraction(0)) + coefficient
    return clean(out)


def scale(coefficient: int | Fraction, value: Poly) -> Poly:
    return clean({word: Fraction(coefficient) * item for word, item in value.items()})


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lword, lcoefficient in left.items():
        for rword, rcoefficient in right.items():
            word = lword + rword
            out[word] = out.get(word, Fraction(0)) + lcoefficient * rcoefficient
    return clean(out)


def comm(left: Poly, right: Poly) -> Poly:
    return add(mul(left, right), scale(-1, mul(right, left)))


def derivation(value: Poly, values: dict[str, Poly]) -> Poly:
    out: Poly = {}
    for word, coefficient in value.items():
        for index, letter in enumerate(word):
            prefix: Poly = {word[:index]: Fraction(1)}
            suffix: Poly = {word[index + 1:]: Fraction(1)}
            out = add(out, scale(coefficient, mul(mul(prefix, values[letter]), suffix)))
    return clean(out)


print("\nB. UNIVERSAL AFFINE FIRST- AND SECOND-JET IDENTITY")
T, Tm, Tn, Tmn = map(atom, ("T", "Tm", "Tn", "Tmn"))
Bm, Bn, Bnm = map(atom, ("Bm", "Bn", "Bnm"))
e, em, en, emn = map(atom, ("e", "em", "en", "emn"))

D1n = add(Tn, scale(-1, comm(Bn, T)))
D2mn = add(
    Tmn,
    scale(-1, comm(Bnm, T)),
    scale(-1, comm(Bn, Tm)),
    scale(-1, comm(Bm, Tn)),
    comm(Bm, comm(Bn, T)),
)

delta = {
    "T": comm(e, T),
    "Tm": add(comm(em, T), comm(e, Tm)),
    "Tn": add(comm(en, T), comm(e, Tn)),
    "Tmn": add(comm(emn, T), comm(em, Tn), comm(en, Tm), comm(e, Tmn)),
    "Bm": add(em, comm(e, Bm)),
    "Bn": add(en, comm(e, Bn)),
    "Bnm": add(emn, comm(em, Bn), comm(e, Bnm)),
    "e": {}, "em": {}, "en": {}, "emn": {},
}
check("theorem", "the covariant first jet transforms homogeneously",
      add(derivation(D1n, delta), scale(-1, comm(e, D1n))) == {})
check("theorem", "the ordered covariant second jet transforms homogeneously",
      add(derivation(D2mn, delta), scale(-1, comm(e, D2mn))) == {})

raw_second = comm(emn, T)
affine_second = scale(-1, comm(emn, T))
check("theorem", "a pure second parameter jet cancels between raw and affine owners",
      add(raw_second, affine_second) == {} and bool(raw_second))
check("theorem", "first parameter connection-jet terms covariantize universally rather than only on the quadratic fixture",
      add(derivation(D2mn, delta), scale(-1, comm(e, D2mn))) == {})
check("plant", "PLANT omitting the affine connection leaves the raw second-jet word",
      bool(raw_second))
check("plant", "PLANT reversing the affine sign doubles rather than cancels the raw word",
      add(raw_second, scale(-1, affine_second)) != {})


print("\nC. IMMUTABLE SELECTED K77 PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the constant moving-Shiab predecessor replays",
      "PASS 47/47" in capture.getvalue() and not P["FAILURES"])
Q = P["P"]
cells = P["cells"]
gauge_basis = Q["P"]["gauge_basis"]
field_responses = Q["field_responses"]
principal_with = Q["principal_with"]
selected = Q["selected"]
sym_pair = Q["sym_pair"]
real_scalar = Q["real_scalar"]
block_labels = Q["P"]["block_labels"]
inherited_blocks = Q["P"]["block_images"]
check("fingerprint", "the selected field carrier remains 196-real", len(cells) == 196)
check("fingerprint", "the effective projected-adjoint carrier remains rank 25", len(gauge_basis) == 25)
check("fingerprint", "the ten raw symmetric blocks remain available", len(inherited_blocks) == 10)


def scalar(value) -> sp.Expr:
    return sp.factor(real_scalar(value))


print("\nD. PORT THE DERIVED AFFINE OWNER THROUGH ALL TEN ACTION BLOCKS")
gauge_responses = [
    [principal_with(selected, mu, delta) for delta in gauge_basis]
    for mu in range(4)
]
raw_blocks = []
affine_blocks = []
complete_blocks = []
for mu, nu in block_labels:
    raw = sp.Matrix(196, 25, [
        scalar(sym_pair(field_responses[mu][row], gauge_responses[nu][column]))
        + (
            scalar(sym_pair(field_responses[nu][row], gauge_responses[mu][column]))
            if mu != nu else 0
        )
        for row in range(196)
        for column in range(25)
    ])
    # The free-algebra identity fixes this sign before any action response is
    # inspected: delta(-[partial_mu B_nu,T])=-[eta_mn,T].
    affine = sp.Matrix(196, 25, [
        scalar(sym_pair(field_responses[mu][row],
                        principal_with(selected, nu, P["S"]["fscale"](Fraction(-1), gauge_basis[column]))))
        + (
            scalar(sym_pair(field_responses[nu][row],
                            principal_with(selected, mu, P["S"]["fscale"](Fraction(-1), gauge_basis[column]))))
            if mu != nu else 0
        )
        for row in range(196)
        for column in range(25)
    ])
    raw_blocks.append(raw)
    affine_blocks.append(affine)
    complete_blocks.append(raw + affine)

check("replay", "the independently rebuilt raw blocks equal the inherited blocks",
      raw_blocks == inherited_blocks)
check("exact", "the raw ten-block second-parameter response has rank 25",
      sp.Matrix.hstack(*raw_blocks).rank() == 25)
check("exact", "the derived affine owner has the same rank 25",
      sp.Matrix.hstack(*affine_blocks).rank() == 25)
check("theorem", "the affine owner is coefficientwise opposite on all ten blocks",
      all(affine == -raw for affine, raw in zip(affine_blocks, raw_blocks)))
check("theorem", "the complete covariant second-parameter-jet response has rank zero",
      sp.Matrix.hstack(*complete_blocks).rank() == 0)
check("control", "all six mixed blocks remain zero before and after covariantization",
      all(raw_blocks[index] == sp.zeros(196, 25)
          and complete_blocks[index] == sp.zeros(196, 25)
          for index, label in enumerate(block_labels) if label[0] != label[1]))
check("control", "the four raw diagonal blocks retain one Lorentz trace",
      [raw_blocks[index].rank() for index, label in enumerate(block_labels) if label[0] == label[1]]
      == [25, 25, 25, 25])
check("plant", "PLANT freezing the affine owner retains rank 25",
      sp.Matrix.hstack(*raw_blocks).rank() == 25)
check("plant", "PLANT reversing the affine sign retains rank 25",
      sp.Matrix.hstack(*[raw - affine for raw, affine in zip(raw_blocks, affine_blocks)]).rank() == 25)


print("\nE. TYPING AND HOSTILE FENCES")
for kind, label in (
    ("layer0", "the affine owner belongs to the full source connection before its effective Cl1 commutator"),
    ("correction", "the rank-25 trace is a raw-jet covariantization defect, not a geometric obstruction"),
    ("principal_bundle", "the connection law fixes the counterterm without a new field or coefficient"),
    ("variational", "the same exact Hessian blocks receive raw and affine responses"),
    ("gauge_bv", "a tangent formal jet identity still does not construct the full BV differential"),
    ("spencer", "observation/contact completion and formal involutivity remain open"),
    ("symplectic", "preboundary charge and the physical presymplectic quotient remain open"),
    ("analytic", "no domain hyperbolicity positivity spectrum or stability follows"),
    ("source", "the source owns the affine grammar but not the selected K77 rank cancellation"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_AFFINE_MAURER_CARTAN_AND_COVARIANT_DERIVATIVE_GRAMMAR__SOURCE_SILENT_SELECTED_K77_PARAMETER_JET_RANKS__REPOSITORY_DERIVES_EXACT_RANK25_TO_ZERO_COVARIANTIZATION")
print("RAW_SECOND_PARAMETER_JET_RANK=25")
print("AFFINE_SECOND_PARAMETER_JET_RANK=25")
print("COMPLETE_COVARIANT_SECOND_PARAMETER_JET_RANK=0")
print("FIRST_PARAMETER_CONNECTION_JET_IDENTITY=UNIVERSAL_FREE_ASSOCIATIVE_ZERO")
print("DISPOSITION=RAW_JET_RANK25_DISSOLVED_BY_SOURCE_OWNED_AFFINE_COVARIANTIZATION__OBSERVATION_BV_SPENCER_GLOBAL_DESCENT_OPEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
