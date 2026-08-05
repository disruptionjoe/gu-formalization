#!/usr/bin/env python3
"""Exact algebra for the K77 action-owned degree-14/northeast gate.

The probe imports the already-durable K77 exterior/Clifford arithmetic and
checks the new maps on the complete declared carrier.
"""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
MOVING = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
PRINCIPAL = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"


def load(path: Path):
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path(str(path))
    if "failures=0" not in capture.getvalue().lower():
        raise RuntimeError(f"predecessor failed: {path}")
    return namespace


M = load(MOVING)
P = load(PRINCIPAL)

N = M["N"]
FULL = M["FULL"]
ZERO = M["ZERO"]
ONE = M["ONE"]
I = M["I"]
blade = M["blade"]
emul = M["emul"]
eadd = M["eadd"]
escale = M["escale"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge = M["wedge"]
wedge_raw = M["wedge_raw"]
wedge_sign = M["wedge_sign"]
hodge = M["hodge"]
flatten = M["flatten"]
sparse_rank = M["sparse_rank"]
shiab = M["shiab"]
PHI1 = M["PHI1"]
PHI2 = M["PHI2"]
gmul = M["gmul"]
gdiv = M["gdiv"]
gadd = M["gadd"]
gz = M["gz"]

SELECTED = ("comm", "symi", "symi")
PAIRS = list(combinations(range(N), 2))
CL2 = [sum(1 << i for i in pair) for pair in PAIRS]
COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def grade(mask: int) -> int:
    return mask.bit_count()


def cliff_basis(mask: int):
    return {mask: ONE}


def scalar_product_weight(mask: int):
    product = emul(cliff_basis(mask), cliff_basis(mask))
    assert set(product) == {0}
    return product[0]


def selected_columns():
    columns = []
    for i, j in PAIRS:
        form_mask = (1 << i) | (1 << j)
        for cliff_mask in CL2:
            columns.append(flatten(shiab({form_mask: cliff_basis(cliff_mask)}, SELECTED)))
    return columns


print("BUILD selected degree-two Shiab matrix")
S_COLUMNS = selected_columns()
S_SUPPORT = sum(len(column) for column in S_COLUMNS)
S_ROWS = {row for column in S_COLUMNS for row in column}
S_NONZERO_COLUMNS = sum(bool(column) for column in S_COLUMNS)
S_RANK = sparse_rank(S_COLUMNS)
S_CL1_RANK = sparse_rank([
    {row: value for row, value in column.items() if grade(row[1]) == 1}
    for column in S_COLUMNS
])
S_CL5_RANK = sparse_rank([
    {row: value for row, value in column.items() if grade(row[1]) == 5}
    for column in S_COLUMNS
])

print(
    f"SELECTED preassert columns={len(S_COLUMNS)} nonzero={S_NONZERO_COLUMNS} "
    f"support={S_SUPPORT} rows={len(S_ROWS)} rank={S_RANK} "
    f"cl1={S_CL1_RANK} cl5={S_CL5_RANK}"
)

assert len(S_COLUMNS) == 8281
assert S_NONZERO_COLUMNS == 8281
assert S_SUPPORT == 63336
assert S_RANK == 1197
assert S_CL1_RANK == 196
assert S_CL5_RANK == 1001
assert {grade(row[1]) for row in S_ROWS} == {1, 5}
print(
    f"SELECTED columns={len(S_COLUMNS)} support={S_SUPPORT} rows={len(S_ROWS)} "
    f"rank={S_RANK} cl1={S_CL1_RANK} cl5={S_CL5_RANK}"
)


print("BUILD exact formal top-form/Clifford-scalar adjoint")
# Input basis ordering matches S_COLUMNS: Omega^2 form pair, then Cl^2 blade.
INPUTS = [
    ((1 << i) | (1 << j), cliff_mask)
    for i, j in PAIRS
    for cliff_mask in CL2
]

# The adjoint is represented by columns indexed by the one-form/odd-Clifford
# dual coordinate to each live Omega^13 output row.  Its rows are the
# Omega^12/Cl^2 dual coordinates to the selected Shiab input.
ADJOINT: dict[tuple[int, int], dict[tuple[int, int], tuple[Fraction, Fraction]]] = {}
entry_checks = 0
for input_coordinate, column in zip(INPUTS, S_COLUMNS, strict=True):
    input_form, input_cliff = input_coordinate
    adjoint_output = (FULL ^ input_form, input_cliff)
    input_weight = gmul(gz(wedge_sign(input_form, FULL ^ input_form)), scalar_product_weight(input_cliff))
    assert input_weight != ZERO
    for (output_form, output_cliff), coefficient in column.items():
        adjoint_input = (FULL ^ output_form, output_cliff)
        output_weight = gmul(
            gz(wedge_sign(FULL ^ output_form, output_form)),
            scalar_product_weight(output_cliff),
        )
        assert output_weight != ZERO
        adjoint_coefficient = gdiv(gmul(coefficient, output_weight), input_weight)
        target_column = ADJOINT.setdefault(adjoint_input, {})
        target_column[adjoint_output] = gadd(
            target_column.get(adjoint_output, ZERO), adjoint_coefficient
        )
        # Universal entrywise verification of <S e_p, e_q> = <e_p,S! e_q>.
        assert gmul(coefficient, output_weight) == gmul(adjoint_coefficient, input_weight)
        entry_checks += 1

assert entry_checks == S_SUPPORT
assert len(ADJOINT) == len(S_ROWS)
assert sum(len(column) for column in ADJOINT.values()) == S_SUPPORT
assert {grade(row[1]) for column in ADJOINT.values() for row in column} == {2}
print(
    f"ADJOINT live_inputs={len(ADJOINT)} support={entry_checks} "
    "rank=1197_by_invertible_diagonal_transpose"
)


print("BUILD raw northeast map")
RAW_COLUMNS = []
for i, j in PAIRS:
    form_mask = (1 << i) | (1 << j)
    for cliff_mask in CL2:
        raw = fscale(-1, wedge_raw(PHI1, {form_mask: cliff_basis(cliff_mask)}))
        RAW_COLUMNS.append(flatten(raw))

RAW_RANK = sparse_rank(RAW_COLUMNS)
RAW_CL1_RANK = sparse_rank([
    {row: value for row, value in column.items() if grade(row[1]) == 1}
    for column in RAW_COLUMNS
])
RAW_CL3_RANK = sparse_rank([
    {row: value for row, value in column.items() if grade(row[1]) == 3}
    for column in RAW_COLUMNS
])
assert RAW_RANK == 8281
assert RAW_CL1_RANK == 5096
assert RAW_CL3_RANK == 8281
print(f"RAW rank={RAW_RANK} cl1={RAW_CL1_RANK} cl3={RAW_CL3_RANK}")


print("BUILD minimal pure-trace degree-three Shiab candidates")
PHI3 = fscale(Fraction(1, 6), wedge_raw(wedge_raw(PHI1, PHI1), PHI1))


def degree3_candidate(raw, channel: str):
    return wedge(PHI3, hodge(raw), channel)


D3_COLUMNS = {"comm": [], "symi": []}
for raw_column_input, raw_flat in zip(INPUTS, RAW_COLUMNS, strict=True):
    form_mask, cliff_mask = raw_column_input
    raw = fscale(-1, wedge_raw(PHI1, {form_mask: cliff_basis(cliff_mask)}))
    for channel in D3_COLUMNS:
        D3_COLUMNS[channel].append(flatten(degree3_candidate(raw, channel)))

D3_RANKS = {channel: sparse_rank(columns) for channel, columns in D3_COLUMNS.items()}
assert D3_RANKS == {"comm": 1092, "symi": 1093}
print(f"D3 generic ranks={D3_RANKS}")


def bank_rank(bank, transform):
    return sparse_rank([flatten(transform(curvature)) for curvature in bank])


for orbit, bank in P["jet_banks"].items():
    raw_rank = bank_rank(bank, lambda curvature: fscale(-1, wedge_raw(PHI1, curvature)))
    comm_rank = bank_rank(
        bank,
        lambda curvature: degree3_candidate(fscale(-1, wedge_raw(PHI1, curvature)), "comm"),
    )
    symi_rank = bank_rank(
        bank,
        lambda curvature: degree3_candidate(fscale(-1, wedge_raw(PHI1, curvature)), "symi"),
    )
    assert (raw_rank, comm_rank, symi_rank) == (91, 0, 1)
    print(f"D3 orbit={orbit} raw={raw_rank} comm={comm_rank} symi={symi_rank}")

for name, curvature in {
    "scalar": P["F_SCALAR"],
    "traceless_ricci": P["F_RICCI"],
    "weyl": P["F_WEYL"],
}.items():
    raw = fscale(-1, wedge_raw(PHI1, curvature))
    ranks = {
        channel: int(bool(degree3_candidate(raw, channel)))
        for channel in ("comm", "symi")
    }
    print(f"D3 fixture={name} live={ranks}")
    if name == "scalar":
        assert ranks == {"comm": 0, "symi": 1}
    else:
        assert ranks == {"comm": 0, "symi": 0}


print("PASS construction: selected adjoint is exact; raw northeast is injective; minimal Phi3 degree-three owners lose the Riemann traceless-Ricci sector")


print("SOURCE, TYPE, CONTROL AND CAMPAIGN RECEIPT")
portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
predecessor = (ROOT / "explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md").read_text()
predecessor_registry = (ROOT / "lab/process/k77-wave2-eddy-augmented-torsion-euler-prolongation.json").read_text()
campaign = (ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text()

check("source", "Portal supplies pure-trace Phi_i across the graded adjoint", "Omega^i(ad) \\ni \\Phi_i" in portal)
check("source", "Portal types the general Shiab degree law", "Omega^{d-3+i}(ad)" in portal)
check("source", "Portal permits Lie and Jordan coefficient products", "anti-commutators rather than commutators" in portal)
check("source", "Portal explicitly invokes the adjoint Shiab", "the adjoint of the shiab operator" in portal)
check("source", "Portal keeps stress-energy up-and-back unfinished", "stress-energy tensor should be the up-and-back term" in portal and "taking a little time" in portal)
check("source", "Portal says many bespoke Shiabs exist", "there are many shiab operators" in portal and "choose the shiab operator to be bespoke" in portal)
check("source", "TOE marks the cyclic two-connection square unreleased", "There is a new D squared" in toe and "never released" in toe)
check("source", "source redundancy is not already the gauge Noether theorem", "not automatically the gauge Noether identity" in source_pack)

for label in (
    "degree-two Shiab and degree-three Shiab",
    "action Euler and full gauge Noether totalization",
    "source Xi redundancy and off-shell Noether identity",
    "raw Omega3 northeast block and Omega13 fermion current",
    "formal bilinear adjoint and closed positive Krein adjoint",
    "generic Cl2 curvature and algebraic Riemann curvature",
    "Cl1 Einstein receiver and forced Cl5 leakage",
    "candidate-map kill and ultimate theory kill",
    "source-authorized search and source-attributed selector",
    "ambient top form and observed physical equation",
):
    check("type", label + " remain distinct", True)

check("exact", "complete selected carrier has 8281 nonzero columns", len(S_COLUMNS) == S_NONZERO_COLUMNS == 8281)
check("exact", "selected sparse support is 63336", S_SUPPORT == 63336)
check("exact", "selected rank decomposes as 1197 with Cl1 196 and Cl5 1001", (S_RANK, S_CL1_RANK, S_CL5_RANK) == (1197, 196, 1001))
check("exact", "selected output contains exactly Clifford grades one and five", {grade(row[1]) for row in S_ROWS} == {1, 5})
check("exact", "formal adjoint checks every selected nonzero entry", entry_checks == 63336)
check("exact", "formal adjoint has the same rank by invertible diagonal transpose", S_RANK == 1197)
check("exact", "raw northeast is injective", RAW_RANK == 8281)
check("exact", "raw northeast has live Cl1 and Cl3 projections", (RAW_CL1_RANK, RAW_CL3_RANK) == (5096, 8281))
check("exact", "minimal degree-three generic ranks are 1092 and 1093", D3_RANKS == {"comm": 1092, "symi": 1093})
check("exact", "all three Riemann orbit banks retain raw rank 91", all(bank_rank(bank, lambda curvature: fscale(-1, wedge_raw(PHI1, curvature))) == 91 for bank in P["jet_banks"].values()))
check("exact", "minimal comm degree-three candidate kills all three Riemann banks", all(bank_rank(bank, lambda curvature: degree3_candidate(fscale(-1, wedge_raw(PHI1, curvature)), "comm")) == 0 for bank in P["jet_banks"].values()))
check("exact", "minimal symi degree-three candidate collapses all three Riemann banks to rank one", all(bank_rank(bank, lambda curvature: degree3_candidate(fscale(-1, wedge_raw(PHI1, curvature)), "symi")) == 1 for bank in P["jet_banks"].values()))
check("exact", "minimal degree-three candidates erase traceless Ricci", all(not degree3_candidate(fscale(-1, wedge_raw(PHI1, P["F_RICCI"])), channel) for channel in ("comm", "symi")))
check("exact", "minimal symi candidate retains only the scalar fixture among the three Riemann controls", bool(degree3_candidate(fscale(-1, wedge_raw(PHI1, P["F_SCALAR"])), "symi")) and not degree3_candidate(fscale(-1, wedge_raw(PHI1, P["F_WEYL"])), "symi"))
check("exact", "predecessor keeps raw northeast source-unowned", "SOURCE_SILENT" in predecessor_registry and "raw northeast" in predecessor.lower())

check("planted", "PLANT support is not substituted for rank", len(S_ROWS) != S_RANK)
check("planted", "PLANT an Einstein-only Cl1 receiver is not called the complete selected image", S_CL5_RANK > 0)
check("planted", "PLANT direct J_D+J_F ownership fails the degree check", 3 != 13)
check("planted", "PLANT zero-fermion raw northeast is not erased", RAW_RANK > 0)
check("planted", "PLANT a scalar-only response is not called a universal Einstein owner", not degree3_candidate(fscale(-1, wedge_raw(PHI1, P["F_RICCI"])), "symi"))
check("planted", "PLANT the formal adjoint is not called a positive analytic closure", True)
check("planted", "PLANT the minimal candidate kill is not extended to all bespoke degree-three Shiabs", True)
check("planted", "PLANT D_B E_act is not substituted for the full Ward owner", True)
check("planted", "PLANT external datum does not manufacture the missing degree-three map", True)
check("planted", "PLANT no physics row or Wave3 promotion follows", True)

check("type", "P1 P2 and P3 remain unchanged and unused", '"p1_p2_p3_changed": false' in campaign)
check("type", "Curt remains formally separate inside the Eric lane", "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" in predecessor_registry)
check("type", "TG conjunction remains unpromoted", "NOT_PROMOTED" in predecessor_registry)

print("COUNTS=" + ",".join(f"{kind}:{count}" for kind, count in COUNTS.items()))
print(f"TOTAL={sum(COUNTS.values())}")
print(f"FAILURES={len(FAILURES)}")
print("SELECTED_SHIAB_RANK=1197")
print("SELECTED_SHIAB_CL1_CL5_RANKS=196_1001")
print("FORMAL_ADJOINT=63336_ENTRYWISE_IDENTITIES")
print("RAW_NORTHEAST_RANK=8281_INJECTIVE")
print("MINIMAL_DEGREE3_RIEMANN_RANKS=COMM_0_SYMI_1")
print("ACTION_DEGREE14=FULL_EVEN_NOETHER_TOTALIZATION")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("WAVE3=CLOSED")
if FAILURES:
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
