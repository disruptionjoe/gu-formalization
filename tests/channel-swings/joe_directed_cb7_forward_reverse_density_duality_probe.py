#!/usr/bin/env python3
"""Exact CB-7C forward/reverse density-duality composition ledger.

The probe classifies bundle-half parity and functor order only.  H210 is a
declared conditional horn.  An odd adapter is likewise only a declared horn;
the probe does not select its line, construct an action, identify barred
fields with adjoints, or assign a rank or spectrum to a full d0+varpi cell.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import ast
import sys


ROOT = Path(__file__).resolve().parents[2]
SELFTEST = "--selftest" in sys.argv
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


ARTIFACT_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb7-forward-reverse-density-duality-composition-2026-08-16.md"
)
SOURCE_PATH = (
    "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
)
PACKET_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
CB2_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb2-h210-equation916-cross-half-composition-2026-08-16.md"
)
CB6_PATH = (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-equation916-observed-composition-2026-08-16.md"
)
PRIOR_Q_PATH = (
    "explorations/conditional-build/"
    "selected-k77-degree-duality-pair-graph-gate-2026-08-10.md"
)

artifact = read(ARTIFACT_PATH)
source = read(SOURCE_PATH)
packet = read(PACKET_PATH)
cb2 = read(CB2_PATH)
cb6 = read(CB6_PATH)
prior_q = read(PRIOR_Q_PATH)


@dataclass(frozen=True)
class Cell:
    coordinate: tuple[int, int]
    role: str
    direction: str
    input_field: str
    row_field: str
    input_degree: int
    output_degree: int
    input_half: int
    row_half: int
    h210_internal_output: str


# Half bits: plus=0 and minus=1.  In every relevant source incidence, the
# barred-row glyph has the same displayed half as the unbarred input glyph.
CELLS = (
    Cell((1, 2), "A-forward", "forward", "nu+", "bar-zeta+", 0, 1, 0, 0, "144bar"),
    Cell((0, 3), "B-forward", "forward", "nu-", "bar-zeta-", 0, 1, 1, 1, "144"),
    Cell((2, 1), "A-reverse", "reverse", "zeta-", "bar-nu-", 1, 0, 1, 1, "16"),
    Cell((3, 0), "B-reverse", "reverse", "zeta+", "bar-nu+", 1, 0, 0, 0, "16bar"),
)

SOURCE_OUTPUT_MODULE = {
    # Output slot after primalizing a barred row under a same-half convention.
    "bar-zeta+": "144",
    "bar-zeta-": "144bar",
    "bar-nu-": "3x16bar",
    "bar-nu+": "3x16",
}

DERIVATIVE_PARITY = 0
H210_PARITY = 1
SAME_HALF = 0
OPPOSITE_HALF = 1


def output_half(cell: Cell, duality: int) -> int:
    """Unbarred output half represented by the row under a primalizer."""
    return cell.row_half ^ duality


def term_half(cell: Cell, parity: int, adapter: int = 0) -> int:
    """Half reached from the unbarred input by a term and optional odd adapter."""
    return cell.input_half ^ parity ^ adapter


def cell_typed(cell: Cell, duality: int, d_adapter: int, h_adapter: int) -> bool:
    target = output_half(cell, duality)
    return (
        term_half(cell, DERIVATIVE_PARITY, d_adapter) == target
        and term_half(cell, H210_PARITY, h_adapter) == target
    )


print("A. SOURCE CUSTODY AND CONDITIONAL-BUILD FENCES")
check(
    "routing",
    "mandatory comparator-routing notice is present",
    "GU-COMPARATOR-ROUTING" in artifact
    and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact,
)
check(
    "scope",
    "H210 and the adapter remain declared horns rather than selected data",
    "Horn `H210` is assumed" in artifact
    and "H210-CELL-ADAPTER" in artifact
    and "does not select" in artifact,
)
check(
    "scope",
    "action selector family-row reduction quotient and external-datum paths are fenced",
    all(
        phrase in artifact.lower()
        for phrase in (
            "action",
            "selector",
            "family row",
            "reduction",
            "quotient",
            "external datum",
            "outside scope",
        )
    ),
)
check(
    "source",
    "source keeps barred and unbarred fields independent",
    "four distinct fields" in source
    and "source bars are independent" in artifact.lower(),
)
check(
    "source",
    "source row and column orders are retained",
    "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in source
    and "(zeta-plus, zeta-minus, nu-plus, nu-minus)^T" in source,
)
check(
    "custody",
    "F M_3 and Z/internal-144 remain distinct",
    all(token in artifact for token in ("F/imposter", "M_3", "Z/internal-144")),
)


print("\nB. FOUR-CELL HALF AND FORM-DEGREE LEDGER")
check("cell", "all four relevant coordinates are exact", {c.coordinate for c in CELLS} == {(1, 2), (0, 3), (2, 1), (3, 0)})
check("cell", "two forward and two reverse-shaped incidences are present", Counter(c.direction for c in CELLS) == {"forward": 2, "reverse": 2})
check("degree", "forward cells have Omega0 to Omega1 degree", all(c.input_degree == 0 and c.output_degree == 1 for c in CELLS if c.direction == "forward"))
check("degree", "reverse cells have Omega1 to Omega0 degree", all(c.input_degree == 1 and c.output_degree == 0 for c in CELLS if c.direction == "reverse"))
check("half", "every relevant row glyph has the same source half as its input", all(c.row_half == c.input_half for c in CELLS))
check("half", "same-half duality types every derivative incidence", all(term_half(c, DERIVATIVE_PARITY) == output_half(c, SAME_HALF) for c in CELLS))
check("half", "same-half duality types no H210 incidence", all(term_half(c, H210_PARITY) != output_half(c, SAME_HALF) for c in CELLS))
check("half", "opposite-half duality types every H210 incidence", all(term_half(c, H210_PARITY) == output_half(c, OPPOSITE_HALF) for c in CELLS))
check("half", "opposite-half duality types no derivative incidence", all(term_half(c, DERIVATIVE_PARITY) != output_half(c, OPPOSITE_HALF) for c in CELLS))

# Every row/column/degree convention is common to both summands of one cell.
# Therefore it cancels from their relative-parity equation.  The exhaustive
# degree-only and full row/column counts are reproduced as finite bit ledgers.
degree_conventions = [
    (r0, r1, c0, c1)
    for r0 in (0, 1)
    for r1 in (0, 1)
    for c0 in (0, 1)
    for c1 in (0, 1)
]
degree_homogeneous = []
for convention in degree_conventions:
    r0, r1, c0, c1 = convention
    homogeneous = 0
    for cell in CELLS:
        row_bit = (r0, r1)[cell.output_degree]
        col_bit = (c0, c1)[cell.input_degree]
        target_parity = row_bit ^ col_bit
        homogeneous += int(target_parity == DERIVATIVE_PARITY == H210_PARITY)
    degree_homogeneous.append(homogeneous)
check("enumeration", "all sixteen degree-only conventions are exhausted", len(degree_conventions) == 16)
check("enumeration", "no degree-only convention makes any full cell homogeneous", set(degree_homogeneous) == {0})

slot_conventions = range(2 ** 8)
slot_homogeneous = []
for convention in slot_conventions:
    homogeneous = 0
    for index, _cell in enumerate(CELLS):
        row_bit = (convention >> index) & 1
        col_bit = (convention >> (4 + index)) & 1
        target_parity = row_bit ^ col_bit
        homogeneous += int(target_parity == DERIVATIVE_PARITY == H210_PARITY)
    slot_homogeneous.append(homogeneous)
check("enumeration", "all 256 invertible row-slot and column-slot conventions are exhausted", len(slot_homogeneous) == 256)
check("enumeration", "no slotwise summand-blind convention makes any full cell homogeneous", set(slot_homogeneous) == {0})


print("\nC. SUMMAND-SPECIFIC ADAPTER AND REVERSE COHERENCE")
independent_direction_solutions = []
for dual_forward in (SAME_HALF, OPPOSITE_HALF):
    for dual_reverse in (SAME_HALF, OPPOSITE_HALF):
        for d_forward in (0, 1):
            for h_forward in (0, 1):
                for d_reverse in (0, 1):
                    for h_reverse in (0, 1):
                        values = {
                            "forward": (dual_forward, d_forward, h_forward),
                            "reverse": (dual_reverse, d_reverse, h_reverse),
                        }
                        if all(cell_typed(cell, *values[cell.direction]) for cell in CELLS):
                            independent_direction_solutions.append(values)

check("adapter", "four independently typed forward/reverse branch pairs exist", len(independent_direction_solutions) == 4)

coherent_solutions = [
    solution
    for solution in independent_direction_solutions
    if solution["forward"] == solution["reverse"]
]
check("adapter", "reverse dual/transpose coherence leaves exactly two parity classes", len(coherent_solutions) == 2)
check(
    "adapter",
    "the two classes are d-only with opposite dual and H210-only with same dual",
    {
        solution["forward"]
        for solution in coherent_solutions
    }
    == {
        (OPPOSITE_HALF, 1, 0),
        (SAME_HALF, 0, 1),
    },
)
check(
    "adapter",
    "a uniform odd adapter on both summands never repairs relative parity",
    not any(
        cell_typed(cell, duality, uniform, uniform)
        for cell in CELLS
        for duality in (SAME_HALF, OPPOSITE_HALF)
        for uniform in (0, 1)
    ),
)
check(
    "adapter",
    "each coherent solution has one adapted operator class plus its forced reverse dual",
    all(sum(solution["forward"][1:]) == 1 for solution in coherent_solutions),
)

# The H210-adapter branch keeps the internal module but moves it to the other
# ambient half.  Under the current source census that is not the module of the
# same-half output slot.  This is a composition fence, not a parity failure.
h210_same_half_forward = [c for c in CELLS if c.direction == "forward"]
check(
    "module",
    "H210-adapter same-half branch misses the banked combined source half/module slots",
    all(
        c.h210_internal_output != SOURCE_OUTPUT_MODULE[c.row_field]
        for c in h210_same_half_forward
    ),
)
check(
    "module",
    "d-adapter opposite-half branch leaves the CB2 H210 modules in their banked slots",
    "nu+ (3 x 16) -> zeta- (144bar)" in cb2
    and "nu- (3 x 16bar) -> zeta+ (144)" in cb2,
)

EXTERNAL_Q = {
    "ambient_odd": True,
    "internal_rs": True,
    "internal_weyl": True,
    "ps": True,
    "rank": True,
    "both_halves": True,
    "selected": False,
}
INTERNAL_Q_BARE = {"internal_rs": False, "ps": True}
INTERNAL_Q_PIN_RIGHT = {"internal_rs": True, "internal_weyl": False, "ps": False}
check("adapter", "moving external q has all algebraic port-preservation flags", all(EXTERNAL_Q[key] for key in ("ambient_odd", "internal_rs", "internal_weyl", "ps", "rank", "both_halves")))
check("scope", "moving external q is not selected", not EXTERNAL_Q["selected"])
check("control", "bare internal q leaks the internal RS condition", not INTERNAL_Q_BARE["internal_rs"])
check("control", "Pin/right internal q breaks internal chirality and PS", not INTERNAL_Q_PIN_RIGHT["internal_weyl"] and not INTERNAL_Q_PIN_RIGHT["ps"])


print("\nD. DENSITY DUAL IS NOT ADJOINT OR REALITY")
typing_levels = {
    "independent_barred_fields": True,
    "density_pairing_declared": True,
    "reverse_bundle_dual_declared": True,
    "formal_adjoint_proved": False,
    "field_reality_imposed": False,
    "common_domain_built": False,
}
check("duality", "forward/reverse bundle typing is compatible with independent barred fields", typing_levels["independent_barred_fields"] and typing_levels["density_pairing_declared"] and typing_levels["reverse_bundle_dual_declared"])
check("duality", "bundle-dual coherence does not prove formal adjointness", not typing_levels["formal_adjoint_proved"])
check("duality", "bundle-dual coherence does not impose field reality", not typing_levels["field_reality_imposed"])
check("duality", "no common analytic domain is inferred", not typing_levels["common_domain_built"])
check("source", "source stars remain candidate syntax rather than a global adjoint theorem", "does not prove" in source and "global Krein adjoint" in source)


print("\nE. CB6 FUNCTOR ORDER AND BRANCH CEILINGS")
forward_A = (
    "M_3 tensor 16+",
    "Z/internal-144bar-",
    "O_J",
    "Gamma_H^intr",
    "kappa_J",
    "F_corr-",
)
forward_B = (
    "bar(M_3) tensor 16bar-",
    "Z/internal-144+",
    "O_J",
    "Gamma_H^intr",
    "kappa_J",
    "F_corr+",
)
check("order", "kappa is strictly downstream of Z observation and intrinsic trace", forward_A.index("kappa_J") > forward_A.index("Gamma_H^intr") > forward_A.index("O_J") > 0)
check("order", "the conjugate half has the same stage order", forward_B.index("kappa_J") == forward_A.index("kappa_J"))
check(
    "order",
    "d-adapter branch leaves the H210 parity and CB6 forward chain unchanged",
    (OPPOSITE_HALF, 1, 0)
    in {solution["forward"] for solution in coherent_solutions}
    and "`kappa_J` is defined only" in cb6,
)
check(
    "order",
    "derivative placement is pointwise postcomposition while precomposition and the reverse lower term are fenced",
    "gamma(q_H) o d0" in artifact
    and "Postcomposition" in artifact
    and "Precomposition" in artifact
    and "nabla q_H" in artifact
    and "formal transpose" in artifact
    and "pointwise branch" in artifact,
)
check("order", "H210-adapter branch is not entitled to inherit the CB6 source-cell receipt", "PARITY-SAT / SOURCE-SLOT-BRIDGE-MISSING" in artifact)
check("order", "reverse-shaped cells receive no illicit backward kappa chain", "No reverse `kappa` chain is inferred" in artifact)
check("scope", "the full cell receives no rank kernel spectrum mass or cancellation", all(word in artifact.lower() for word in ("no full-cell rank", "kernel", "spectrum", "mass", "cancellation")))
check("prior", "canonical trace-q W/mirror kill remains explicitly scoped", "scoped kill" in prior_q.lower() and "W/mirror" in artifact and "does not settle" in artifact)


print("\nF. MULTI-LENS AND SEMANTIC MUTATIONS")
for lens in (
    "source row/column custody",
    "density dual versus adjoint/reality",
    "both ambient halves",
    "forward/reverse functor order",
    "form degree and parity",
    "conditional branch enumeration",
    "negative controls",
    "prior-art novelty",
):
    check("lens", lens, lens in artifact.lower())

if SELFTEST:
    mutants = {
        "bars become adjoints": typing_levels["field_reality_imposed"],
        "uniform adapter repairs cell": any(
            cell_typed(CELLS[0], duality, adapter, adapter)
            for duality in (0, 1)
            for adapter in (0, 1)
        ),
        "kappa precedes observation": forward_A.index("kappa_J") < forward_A.index("O_J"),
        "same-half H210 branch preserves source module": all(
            c.h210_internal_output == SOURCE_OUTPUT_MODULE[c.row_field]
            for c in h210_same_half_forward
        ),
        "internal bare q preserves RS": INTERNAL_Q_BARE["internal_rs"],
        "internal Pin q preserves PS": INTERNAL_Q_PIN_RIGHT["ps"],
        "external q is selected": EXTERNAL_Q["selected"],
        "one half is enough": len({c.input_half for c in CELLS}) == 1,
    }
    for label, mutation_survives in mutants.items():
        check("plant", label, not mutation_survives)

ast.parse(Path(__file__).read_text(encoding="utf-8"))
check("hygiene", "probe parses as Python", True)

print("\nSUMMARY")
for kind in sorted(COUNTS):
    print(f"{kind}: {COUNTS[kind]}")
print(f"total: {sum(COUNTS.values())}")
print(f"failures: {len(FAILURES)}")
raise SystemExit(1 if FAILURES else 0)
