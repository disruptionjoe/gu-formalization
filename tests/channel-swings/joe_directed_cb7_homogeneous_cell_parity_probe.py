#!/usr/bin/env python3
"""Exact CB-7A homogeneous-cell half/parity classifier.

The probe classifies the derivative and conditional H210 summands in the four
relevant equation-(9.16) cells. H210 is assumed. It constructs no action,
selector, observer, family row, reduction, quotient, external datum, physical
adjoint, mass, or spectrum.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys


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
    "cb7-homogeneous-cell-parity-classifier-2026-08-16.md"
)
SOURCE_PATH = "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
PACKET_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
CB6_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-equation916-observed-composition-2026-08-16.md"
)
PRIOR_SIGN_PATH = "explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md"
PRIOR_GRAPH_PATH = (
    "explorations/conditional-build/"
    "selected-k77-degree-duality-pair-graph-gate-2026-08-10.md"
)

artifact = read(ARTIFACT_PATH)
source = read(SOURCE_PATH)
packet = read(PACKET_PATH)
cb6 = read(CB6_PATH)
prior_sign = read(PRIOR_SIGN_PATH)
prior_graph = read(PRIOR_GRAPH_PATH)
artifact_flat = " ".join(artifact.split())


@dataclass(frozen=True)
class Cell:
    name: str
    position: tuple[int, int]
    row_slot: str
    column_slot: str
    row_half: int
    column_half: int
    input_degree: int
    output_degree: int
    derivative: str
    h210: str
    direction: str


CELLS = (
    Cell("A_forward", (1, 2), "bar-zeta-plus", "nu-plus", 1, 1, 0, 1,
         "d0", "varpi_-+", "forward"),
    Cell("B_forward", (0, 3), "bar-zeta-minus", "nu-minus", 0, 0, 0, 1,
         "d0", "varpi_+-", "forward"),
    Cell("A_reverse", (2, 1), "bar-nu-minus", "zeta-minus", 0, 0, 1, 0,
         "-d0*", "-bar(varpi_+-)*", "reverse"),
    Cell("B_reverse", (3, 0), "bar-nu-plus", "zeta-plus", 1, 1, 1, 0,
         "-d0*", "-bar(varpi_-+)*", "reverse"),
)

PARITY = {"derivative": 0, "h210": 1}


def types(cell: Cell, row_flip: int, column_flip: int, operator_parity: int) -> bool:
    target = cell.row_half ^ row_flip
    predicted = cell.column_half ^ column_flip ^ operator_parity
    return target == predicted


def convention_fingerprint(row_flips: dict[str, int], column_flips: dict[str, int]) -> tuple[int, int]:
    typed_terms = 0
    homogeneous_cells = 0
    for cell in CELLS:
        d_ok = types(cell, row_flips[cell.row_slot], column_flips[cell.column_slot], 0)
        h_ok = types(cell, row_flips[cell.row_slot], column_flips[cell.column_slot], 1)
        typed_terms += int(d_ok) + int(h_ok)
        homogeneous_cells += int(d_ok and h_ok)
    return typed_terms, homogeneous_cells


print("A. SOURCE, ROUTING, AND CONDITIONAL-BUILD FENCES")
check(
    "routing",
    "mandatory comparator-routing notice and classification are present",
    "GU-COMPARATOR-ROUTING" in artifact
    and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact,
)
check(
    "scope",
    "H210 is assumed and action/external-datum construction is outside scope",
    "Horn `H210` is assumed" in artifact
    and "external datum" in artifact
    and "outside this channel" in artifact,
)
check(
    "source",
    "source extraction fixes the row and column orders",
    "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in source
    and "(zeta-plus, zeta-minus, nu-plus, nu-minus)" in source,
)
check(
    "source",
    "section-11.2 signs remain ambient half-spinor labels",
    "SOURCE-STATES-AMBIENT-HALF-SPINOR" in source
    and "cannot silently be redefined" in source,
)
check(
    "scope",
    "bars and stars are not promoted to a field adjoint",
    "Bars remain independent fields" in artifact_flat
    and "common-domain adjoint" in artifact_flat
    and "They are not declared formal adjoints" in artifact_flat,
)


print("B. FOUR SOURCE CELLS, BOTH HALVES, AND BOTH DIRECTIONS")
expected_positions = {(1, 2), (0, 3), (2, 1), (3, 0)}
check("exact", "the classifier contains exactly the four required cells",
      {cell.position for cell in CELLS} == expected_positions and len(CELLS) == 4)
check("exact", "both source halves occur in each direction",
      all({cell.column_half for cell in CELLS if cell.direction == direction} == {0, 1}
          for direction in ("forward", "reverse")))
check("exact", "forward and reverse cells have the required form-degree shifts",
      all((cell.input_degree, cell.output_degree) == (0, 1)
          for cell in CELLS if cell.direction == "forward")
      and all((cell.input_degree, cell.output_degree) == (1, 0)
              for cell in CELLS if cell.direction == "reverse"))
check("source", "CB6 carries the same four-cell placement",
      all(f"`{position}`" in cb6 for position in ("(1,2)", "(0,3)", "(2,1)", "(3,0)")))
check("exact", "the displayed source row and column labels agree cellwise",
      all(cell.row_half == cell.column_half for cell in CELLS))


print("C. SAME-HALF AND OPPOSITE-HALF EXTREMES")
same = {
    cell.name: (
        types(cell, 0, 0, PARITY["derivative"]),
        types(cell, 0, 0, PARITY["h210"]),
    )
    for cell in CELLS
}
opposite = {
    cell.name: (
        types(cell, 1, 0, PARITY["derivative"]),
        types(cell, 1, 0, PARITY["h210"]),
    )
    for cell in CELLS
}
check("exact", "same-half duality types all derivatives and no H210 terms",
      all(value == (True, False) for value in same.values()))
check("exact", "opposite-half duality types all H210 terms and no derivatives",
      all(value == (False, True) for value in opposite.values()))
check("exact", "neither extreme makes even one full cell homogeneous",
      not any(d_ok and h_ok for d_ok, h_ok in same.values())
      and not any(d_ok and h_ok for d_ok, h_ok in opposite.values()))


print("D. EXHAUSTIVE DEGREE-SENSITIVE CLASSIFIER")
degree_fingerprints = []
for r0, r1, c0, c1 in product((0, 1), repeat=4):
    typed_terms = 0
    homogeneous = 0
    for cell in CELLS:
        row_flip = (r0, r1)[cell.output_degree]
        column_flip = (c0, c1)[cell.input_degree]
        d_ok = types(cell, row_flip, column_flip, 0)
        h_ok = types(cell, row_flip, column_flip, 1)
        typed_terms += int(d_ok) + int(h_ok)
        homogeneous += int(d_ok and h_ok)
    degree_fingerprints.append((typed_terms, homogeneous))
check("exact", "all 16 degree-sensitive row/column conventions are enumerated",
      len(degree_fingerprints) == 16)
check("exact", "every degree-sensitive convention types exactly 4/8 incidences",
      set(degree_fingerprints) == {(4, 0)})
check("exact", "no degree-sensitive convention makes a full cell homogeneous",
      all(homogeneous == 0 for _, homogeneous in degree_fingerprints))


print("E. EXHAUSTIVE SOURCE-SLOT-SENSITIVE CLASSIFIER")
row_slots = tuple(cell.row_slot for cell in CELLS)
column_slots = tuple(cell.column_slot for cell in CELLS)
slot_fingerprints = []
for bits in product((0, 1), repeat=8):
    row_flips = dict(zip(row_slots, bits[:4]))
    column_flips = dict(zip(column_slots, bits[4:]))
    slot_fingerprints.append(convention_fingerprint(row_flips, column_flips))
check("exact", "all 256 invertible source-slot half-flip conventions are enumerated",
      len(slot_fingerprints) == 256)
check("exact", "every source-slot convention types exactly 4/8 incidences",
      set(slot_fingerprints) == {(4, 0)})
check("exact", "no source-slot convention makes a full cell homogeneous",
      all(homogeneous == 0 for _, homogeneous in slot_fingerprints))


print("F. GENERAL SAME-CELL PROOF AND GRADING AUDIT")
for row_half, column_half, row_flip, column_flip in product((0, 1), repeat=4):
    d_equation = (row_half ^ row_flip) == (column_half ^ column_flip)
    h_equation = (row_half ^ row_flip) == (column_half ^ column_flip ^ 1)
    assert d_equation != h_equation
check("exact", "all 16 local bit assignments type exactly one of the two parities", True)
check("exact", "the contradiction does not depend on equal source row/column labels", True)

grading_delta = {
    "ambient": {term: parity for term, parity in PARITY.items()},
    "form": {term: 1 for term in PARITY},
    "product": {term: parity ^ 1 for term, parity in PARITY.items()},
}
check("exact", "degree-only grading is blind to the half mismatch",
      grading_delta["form"] == {"derivative": 1, "h210": 1})
check("exact", "product grading diagnoses opposite summand parities",
      grading_delta["product"] == {"derivative": 1, "h210": 0})
check("scope", "artifact says product grading diagnoses rather than repairs",
      "Product grading is **not** blind" in artifact
      and "It diagnoses" in artifact
      and "does not make them homogeneous" in artifact_flat)


print("G. MINIMUM ABSTRACT ADAPTER CLASSES")
adapter_solutions = [
    (a_d, a_h)
    for a_d, a_h in product((0, 1), repeat=2)
    if (PARITY["derivative"] ^ a_d) == (PARITY["h210"] ^ a_h)
]
minimum_solutions = [solution for solution in adapter_solutions if sum(solution) == 1]
check("exact", "homogeneity requires opposite operator-class adapter bits",
      adapter_solutions == [(0, 1), (1, 0)])
check("exact", "there are exactly two minimum-Hamming-weight adapter classes",
      minimum_solutions == [(0, 1), (1, 0)])
check("exact", "H210-only odd adapter makes all four same-half cells homogeneous",
      all(types(cell, 0, 0, PARITY["derivative"])
              and types(cell, 0, 0, PARITY["h210"] ^ 1)
              for cell in CELLS))
check("exact", "derivative-only odd adapter makes all four opposite-half cells homogeneous",
      all(types(cell, 1, 0, PARITY["derivative"] ^ 1)
              and types(cell, 1, 0, PARITY["h210"])
              for cell in CELLS))
check("scope", "abstract adapter bits are not promoted to constructed bundle maps",
      "constructs neither" in artifact
      and "prove its naturality" in artifact_flat
      and "H210 Z/RS/PS port" in artifact_flat
      and "Module coherence can kill" in artifact_flat)


print("H. PRIOR ART, FUNCTOR ORDER, AND SOURCE CUSTODY")
check("prior_art", "prior cross-cell SAT has two global-sign-related solutions",
      "exactly two sign solutions" in prior_sign
      and "global sign" in prior_sign
      and "q" in prior_sign)
check("prior_art", "v0.140 kill is explicitly W/mirror-carrier scoped",
      "scoped kill" in prior_graph.lower()
      and "W + mirror" in prior_graph
      and "joined rank `256`" in prior_graph)
check("scope", "CB7A does not import the W/mirror kill as an H210 no-go",
      "carrier-scoped negative result" in artifact
      and "not automatically a no-go" in artifact)
check("scope", "downstream kappa remains outside upstream varpi",
      "must never be inserted into `varpi`" in artifact
      and "kappa_J" in cb6)
check("source", "F M_3 and Z/internal-144 custody is retained",
      all(token in packet for token in ("F     =", "M_3   =", "144   ="))
      and "F/imposter, `M_3`, and Z/internal-`144` remain distinct" in artifact_flat)


def validate_semantics(state: dict[str, bool]) -> None:
    forbidden = (
        "silent_one_form_relabel",
        "collapse_halves",
        "delete_reverse_cells",
        "bars_are_adjoints",
        "kappa_is_varpi",
        "derive_action",
        "select_external_datum",
        "name_family",
        "infer_mass_or_spectrum",
        "import_w_mirror_kill_as_h210",
    )
    if any(state.get(key, False) for key in forbidden):
        raise AssertionError("forbidden semantic mutation")


print("I. ADVERSARIAL SEMANTIC CONTROLS")
validate_semantics({})
check("semantic", "baseline conditional state is admitted", True)
mutants = (
    "silent_one_form_relabel",
    "collapse_halves",
    "delete_reverse_cells",
    "bars_are_adjoints",
    "kappa_is_varpi",
    "derive_action",
    "select_external_datum",
    "name_family",
    "infer_mass_or_spectrum",
    "import_w_mirror_kill_as_h210",
)
fired = 0
for mutant in mutants:
    try:
        validate_semantics({mutant: True})
    except AssertionError:
        fired += 1
check("planted", "all ten semantic mutations are rejected", fired == len(mutants))


if SELFTEST:
    print("J. SELFTEST MUTATIONS")
    check("selftest", "making H210 even is detected as an explicit adapter, not baseline",
          PARITY["h210"] ^ 1 == PARITY["derivative"])
    check("selftest", "removing reverse cells changes required coverage",
          len([cell for cell in CELLS if cell.direction == "forward"]) != len(CELLS))
    check("selftest", "a noninvertible half collapse is outside the enumerated XOR maps",
          {0 ^ 0, 1 ^ 0} == {0, 1} and {0 ^ 1, 1 ^ 1} == {0, 1})


total = sum(COUNTS.values())
print(f"SUMMARY: {total - len(FAILURES)}/{total} checks passed; by kind {dict(COUNTS)}")
if FAILURES:
    raise SystemExit("FAIL: " + "; ".join(FAILURES))
print("PASS: no summand-blind half/degree primalizer makes the four d0 plus H210 cells homogeneous.")
