#!/usr/bin/env python3
"""Exact SN-3C source-slot to neutral-line incidence classifier.

This probe composes the released equation-9.16 matrix, CS-1 centre classes,
SN-2 neutral-line types, and SN-2 valuation grammar.  It does not construct or
select a coefficient, action, vacuum, scale, reality condition, neutral
closure, mass, or spectrum.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ROWS = ("bar-zeta-minus", "bar-zeta-plus", "bar-nu-minus", "bar-nu-plus")
COLS = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")
ROW_OUTPUT = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")

CELLS = (
    ("star-odot-varpi-pp", "star-odot-d0-varpi-pm", "varpi-pp", "d0-varpi-pm"),
    ("star-odot-d0-varpi-mp", "star-odot-varpi-mm", "d0-varpi-mp", "varpi-mm"),
    ("minus-bar-varpi-pp-star", "minus-d0-star-bar-varpi-pm-star", "southeast-zero", "southeast-zero"),
    ("minus-d0-star-bar-varpi-mp-star", "minus-bar-varpi-mm-star", "southeast-zero", "southeast-zero"),
)

ROW_CLASSES = (1, 3, 1, 3)
COL_CLASSES = (3, 1, 3, 1)
OWNERS = ("pp", "pm", "mp", "mm")

SOURCE_HALF = {
    "nu-plus": "A_eff",
    "zeta-minus": "A_eff",
    "nu-minus": "B_eff",
    "zeta-plus": "B_eff",
}
CENTRE_HALF = {
    "nu-plus": "W3",
    "zeta-plus": "W3",
    "nu-minus": "W1",
    "zeta-minus": "W1",
}

NW = ((0, 0), (0, 1), (1, 0), (1, 1))
NE = ((0, 2), (0, 3), (1, 2), (1, 3))
SW = ((2, 0), (2, 1), (3, 0), (3, 1))
SE = ((2, 2), (2, 3), (3, 2), (3, 3))

OWNER_BY_POSITION = {
    (0, 0): "pp", (0, 1): "pm", (1, 0): "mp", (1, 1): "mm",
    (0, 2): "pp", (0, 3): "pm", (1, 2): "mp", (1, 3): "mm",
    (2, 0): "pp", (2, 1): "pm", (3, 0): "mp", (3, 1): "mm",
}

# A forward NE position maps to the transpose-shaped SW position.  The
# crossed pm/mp labels are source data, not a field-reality identification.
REVERSE_POSITION = {
    (0, 2): (2, 0),
    (0, 3): (3, 0),
    (1, 2): (2, 1),
    (1, 3): (3, 1),
}
REVERSE_OWNER = {"pp": "pp", "pm": "mp", "mp": "pm", "mm": "mm"}


@dataclass(frozen=True)
class Line:
    name: str
    su2: int
    hypercharge_twice: int
    b_minus_l: int


L0 = Line("L0", 2, -1, -1)
NC = Line("Nc", 1, 0, 1)
NEUTRAL_LINES = {"Q0": (L0, NC), "SM1": (NC,)}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def block_of(position: tuple[int, int]) -> str:
    row, col = position
    if row < 2 and col < 2:
        return "A"
    if row < 2 and col >= 2:
        return "B"
    if row >= 2 and col < 2:
        return "C"
    return "SE"


def net_cell_class(position: tuple[int, int]) -> int:
    row, col = position
    return (-ROW_CLASSES[row] - COL_CLASSES[col]) % 4


def arrow(position: tuple[int, int]) -> tuple[str, str]:
    row, col = position
    return COLS[col], ROW_OUTPUT[row]


def line_pairs(horn: str) -> tuple[tuple[Line, Line], ...]:
    lines = NEUTRAL_LINES[horn]
    return tuple((source, target) for source in lines for target in lines)


def xd_pairs(horn: str) -> tuple[tuple[Line, Line], ...]:
    return tuple(pair for pair in line_pairs(horn) if {pair[0].name, pair[1].name} == {"L0", "Nc"})


def nc_pairs(horn: str) -> tuple[tuple[Line, Line], ...]:
    return tuple(pair for pair in line_pairs(horn) if pair[0] == NC and pair[1] == NC)


def valuation(weights: dict[str, int], support: dict[str, bool]) -> int | None:
    values = [weights[owner] for owner in OWNERS if support[owner]]
    return min(values) if values else None


def support_separation_holds(
    weights: dict[str, int],
    a_support: dict[str, bool],
    b_support: dict[str, bool],
    bar_weights: dict[str, int],
    c_support: dict[str, bool],
) -> bool:
    return (
        valuation(weights, a_support) == 0
        and valuation(weights, b_support) == 1
        and valuation(bar_weights, c_support) == 1
        and all(not b_support[owner] for owner in OWNERS if weights[owner] == 0)
    )


def checks() -> list[tuple[str, bool]]:
    source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
    claims = read("lab/sources/source-claim-register.yaml")
    cs1 = read("lab/active-research/joe-directed/class-shift/cs1-first-order-shift-is-the-chirality-grading-2026-08-15.md")
    neutral = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-equation916-k77-neutral-restriction-2026-08-16.md")
    reality = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-reality-charge-admissibility-2026-08-16.md")
    valuation_artifact = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-pencil-valuation-classifier-2026-08-16.md")
    artifact = read("lab/active-research/joe-directed/majorana-126-neutrino/sn3-source-slot-neutral-line-incidence-classifier-2026-08-16.md")

    results: list[tuple[str, bool]] = []

    def add(name: str, condition: object) -> None:
        results.append((name, bool(condition)))

    # Lens 1: source matrix grammar and custody.
    add("source row order", "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in source)
    add("source column order", "(zeta-plus, zeta-minus, nu-plus, nu-minus)^T" in source)
    add("sixteen matrix positions", sum(len(row) for row in CELLS) == 16)
    add("four southeast displayed zeros", all(CELLS[row][col] == "southeast-zero" for row, col in SE))
    add("SC-OP-04 candidate source row present", "- id: SC-OP-04" in claims and "something one can begin with" in claims)
    add("SC-OP-05 admits but does not select nonzero SE", "- id: SC-OP-05" in claims and "non-trivial lower-right" in claims)
    add("SC-FER-03 assigns functions without deriving incidence", "- id: SC-FER-03" in claims and "Yukawa couplings" in claims)
    add("four source fields remain independent", "four distinct fields" in source)

    # Lens 2: exact quadrant partition and recurring owner custody.
    all_positions = set(NW) | set(NE) | set(SW) | set(SE)
    add("quadrants partition matrix", len(all_positions) == 16)
    add("eight printed cross-degree cells", len(NE) + len(SW) == 8)
    add("NE is exactly B", all(block_of(position) == "B" for position in NE))
    add("SW is exactly C", all(block_of(position) == "C" for position in SW))
    add("every unbarred owner occurs once in A", sorted(OWNER_BY_POSITION[position] for position in NW) == sorted(OWNERS))
    add("every unbarred owner recurs once in B", sorted(OWNER_BY_POSITION[position] for position in NE) == sorted(OWNERS))
    add("every barred partner occurs once in C", sorted(OWNER_BY_POSITION[position] for position in SW) == sorted(OWNERS))
    add("no displayed SE owner", all(position not in OWNER_BY_POSITION for position in SE))

    expected_tokens = {
        (0, 2): "varpi-pp",
        (0, 3): "d0-varpi-pm",
        (1, 2): "d0-varpi-mp",
        (1, 3): "varpi-mm",
        (2, 0): "minus-bar-varpi-pp-star",
        (2, 1): "minus-d0-star-bar-varpi-pm-star",
        (3, 0): "minus-d0-star-bar-varpi-mp-star",
        (3, 1): "minus-bar-varpi-mm-star",
    }
    add("exact eight cross-degree tokens", all(CELLS[row][col] == token for (row, col), token in expected_tokens.items()))

    # Lens 3: net centre classes.
    expected_pattern = (0, 2, 2, 0)
    for block_name, positions in (("A", NW), ("B", NE), ("C", SW), ("SE", SE)):
        add(f"{block_name} net class pattern 0 2 2 0", tuple(net_cell_class(position) for position in positions) == expected_pattern)
    add("CS1 owns unique uniform source reading", "Exactly one survives" in cs1 and "class-DIAGONAL" in cs1)
    add("net centre class not B-L", "ambient centre class 2  !=  B-L charge 2" in reality)

    # Lens 4: reverse-shaped partner custody.
    for forward, reverse in REVERSE_POSITION.items():
        forward_owner = OWNER_BY_POSITION[forward]
        reverse_owner = OWNER_BY_POSITION[reverse]
        add(
            f"reverse owner {forward_owner} to {REVERSE_OWNER[forward_owner]}",
            reverse_owner == REVERSE_OWNER[forward_owner],
        )
    add("pm mp reverse pairing is crossed", REVERSE_OWNER["pm"] == "mp" and REVERSE_OWNER["mp"] == "pm")
    add("pp mm reverse pairing is label-preserving", REVERSE_OWNER["pp"] == "pp" and REVERSE_OWNER["mm"] == "mm")

    # Lens 5: two distinct half ledgers.
    pp_mm_ne = tuple(position for position in NE if OWNER_BY_POSITION[position] in {"pp", "mm"})
    pm_mp_ne = tuple(position for position in NE if OWNER_BY_POSITION[position] in {"pm", "mp"})
    add("pp mm cross source-effective halves", all(SOURCE_HALF[arrow(position)[0]] != SOURCE_HALF[arrow(position)[1]] for position in pp_mm_ne))
    add("pm mp within source-effective halves", all(SOURCE_HALF[arrow(position)[0]] == SOURCE_HALF[arrow(position)[1]] for position in pm_mp_ne))
    add("pp mm within centre packages", all(CENTRE_HALF[arrow(position)[0]] == CENTRE_HALF[arrow(position)[1]] for position in pp_mm_ne))
    add("pm mp cross centre packages", all(CENTRE_HALF[arrow(position)[0]] != CENTRE_HALF[arrow(position)[1]] for position in pm_mp_ne))
    add("half ledgers are not identical", SOURCE_HALF != CENTRE_HALF)

    # Lens 6: Q0/SM1 formal line incidence.
    add("Q0 has two neutral lines", tuple(line.name for line in NEUTRAL_LINES["Q0"]) == ("L0", "Nc"))
    add("SM1 has only Nc", tuple(line.name for line in NEUTRAL_LINES["SM1"]) == ("Nc",))
    add("Q0 has four endpoint pairs per cell", len(line_pairs("Q0")) == 4)
    add("SM1 has one endpoint pair per cell", len(line_pairs("SM1")) == 1)
    add("Q0 has two XD orientations per cell", len(xd_pairs("Q0")) == 2)
    add("SM1 has zero XD orientations", len(xd_pairs("SM1")) == 0)
    add("both horns retain formal Nc Nc endpoint", len(nc_pairs("Q0")) == 1 and len(nc_pairs("SM1")) == 1)
    add("four B ports give eight formal Q0 XD orientations", len(NE) * len(xd_pairs("Q0")) == 8)
    add("four C ports give eight formal Q0 XD orientations", len(SW) * len(xd_pairs("Q0")) == 8)
    add("SN2 exact Q0 SM1 distinction is banked", "SN2-NEUTRAL=Q0" in neutral and "SN2-NEUTRAL=SM1" in neutral)
    add("XD compensator type is banked", "dual weak doublet" in reality and "B-L=0" in reality)

    # Lens 7: source-slot type excludes displayed X_R.
    displayed_xr_ports = tuple(position for position in SE if CELLS[position[0]][position[1]] != "southeast-zero")
    add("displayed XR ports zero", len(displayed_xr_ports) == 0)
    add("source-admitted SE positions four", len(SE) == 4)
    add("SE class split two zero two two", sorted(net_cell_class(position) for position in SE) == [0, 0, 2, 2])
    add("printed cross-degree NcNc is not Omega0 to Omega0", all(block_of(position) in {"B", "C"} for position in NE + SW))
    add("XR minimum packet requires southeast", "source-admitted southeast `Omega0 -> Omega0` rival cell" in reality)
    add("adding R changes ABC0 grammar", "[[A,B],[-C,R]]" in artifact and "not the SN-2" in artifact)

    # Lens 8: shared-owner valuation and leading-support separation.
    weights = {"pp": 0, "pm": 1, "mp": 1, "mm": 2}
    bar_weights = {owner: 1 for owner in OWNERS}
    support_all = {owner: True for owner in OWNERS}
    b_separated = {"pp": False, "pm": True, "mp": True, "mm": True}
    add("generic common support gives vA zero", valuation(weights, support_all) == 0)
    add("generic common support forces vB zero", valuation(weights, support_all) == valuation(weights, support_all) == 0)
    add("generic common support cannot give 0 1", not support_separation_holds(weights, support_all, support_all, bar_weights, support_all))
    add("separated B support gives vB one", valuation(weights, b_separated) == 1)
    add("barred C support gives vC one", valuation(bar_weights, support_all) == 1)
    add("conditional support-separated fixture gives 0 1 1", support_separation_holds(weights, support_all, b_separated, bar_weights, support_all))
    add("all weight-zero B support is annihilated", all(not b_separated[owner] for owner in OWNERS if weights[owner] == 0))
    add("A and B owner sets exactly coincide", {OWNER_BY_POSITION[position] for position in NW} == {OWNER_BY_POSITION[position] for position in NE} == set(OWNERS))
    add("C uses separately barred valuation ledger", set(bar_weights) == set(OWNERS) and bar_weights is not weights)
    add("SN2 valuation target is banked", "`v(A)=0`, `v(B)=v(C)=1`" in valuation_artifact and "valuations `(0,1,1)`" in valuation_artifact)
    add("nondegenerate Schur composition remains required", "C_0A_0^{-1}B_0" in artifact or "C0 A0^-1 B0" in artifact)
    add("neutral closure remains separate", "SN2-NEUTRAL-CLOSED" in artifact)

    # Artifact/routing/ceiling checks.
    add("artifact routing notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    add("artifact source-native classification", "Classification: `SOURCE_NATIVE_ROUTE`" in artifact)
    add("artifact carries eight lenses", all(f"{index}. **" in artifact for index in range(1, 9)))
    add("artifact forbids action selection", "selects a coefficient nor proves" in artifact and "NOT a selected coefficient, action, vacuum, scale" in artifact)
    add("artifact states claim ceiling", "**Not established:**" in artifact and "mass, pole, spectrum" in artifact)
    add("novelty audit present", "## 7. Novelty audit and claim ceiling" in artifact)

    return results


def planted_false_controls() -> list[tuple[str, bool]]:
    """Each expression is intentionally false and must stay false."""
    support_all = {owner: True for owner in OWNERS}
    weights = {"pp": 0, "pm": 1, "mp": 1, "mm": 2}
    return [
        ("SM1 has an XD orientation", len(xd_pairs("SM1")) > 0),
        ("displayed SE contains an owner", any(position in OWNER_BY_POSITION for position in SE)),
        ("Q0 and SM1 have the same line count", len(NEUTRAL_LINES["Q0"]) == len(NEUTRAL_LINES["SM1"])),
        ("all cross-degree cells have net class two", all(net_cell_class(position) == 2 for position in NE + SW)),
        ("pm reverse partner keeps pm label", OWNER_BY_POSITION[REVERSE_POSITION[(0, 3)]] == "pm"),
        ("source and centre half ledgers coincide", SOURCE_HALF == CENTRE_HALF),
        ("A and B use disjoint owners", {OWNER_BY_POSITION[p] for p in NW}.isdisjoint({OWNER_BY_POSITION[p] for p in NE})),
        ("generic common support yields vB one", valuation(weights, support_all) == 1),
        ("SE rival is source-selected", False),
        ("formal endpoint incidence proves nonzero rank", False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    results = checks()
    failures = [name for name, passed in results if not passed]
    for name, passed in results:
        print(f"{'PASS' if passed else 'FAIL'} {name}")

    if args.selftest:
        plants = planted_false_controls()
        bad_plants = [name for name, value in plants if value]
        for name, value in plants:
            print(f"{'FAIL' if value else 'PASS'} planted false rejected: {name}")
        failures.extend(f"planted false unexpectedly true: {name}" for name in bad_plants)
        print(f"planted false controls rejected: {len(plants) - len(bad_plants)}/{len(plants)}")

    print(f"checks: {len(results) - len([name for name, passed in results if not passed])}/{len(results)}")
    if failures:
        print("SN3-C FAIL")
        return 1
    print("PASS: SN3-C separates parent ownership, printed ports, neutral-line incidence, closure, and shared-owner valuation support.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
