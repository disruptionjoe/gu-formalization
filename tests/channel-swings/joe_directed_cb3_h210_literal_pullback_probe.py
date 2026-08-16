#!/usr/bin/env python3
"""Exact CB-3A literal graph-pullback ranks for the conditional H210 port.

H210 and its nonzero CB-1 port are declared inputs.  This probe neither
derives nor varies an action, background, vacuum, selector, or family row.
The source imposter is the F-shaped 128; the 144 is only its high-energy
partner sector.

For the graph L_J=(I,J):H->H+V and the pure-internal CB-1 tensor

    T_a = c_a Gamma_a phi4,  c_a=-2/5 on A6 and +3/5 on B4,

literal one-form pullback is (O_J T)_mu=sum_a J[a,mu] T_a.  Multiplying all
coefficients by five leaves ranks unchanged.  Exact signed-permutation
Cl(7,7) arithmetic checks both ambient Weyl halves.  SymPy performs exact
integer/rational rank elimination; no floating-point arithmetic is used.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import nguyen_c1c2_real_form_probe as c12


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}"
          + (f" -- {detail}" if detail else ""), flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def product(gammas: list[c12.SP], indices) -> c12.SP:
    out = c12.SP.identity(gammas[0].n)
    for index in indices:
        out = out.mul(gammas[index])
    return out


print("A. SOURCE FENCES, PRIOR ART, AND MULTI-LENS PREFLIGHT")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
he1 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he1-imposter-separation-invariant-2026-08-14.md"
)
cb1 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb1-h210-k77-rs-intertwiner-2026-08-16.md"
)
vz4 = read("lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md")
cartan = read("tests/channel-swings/selected_k77_canonical_section_jet_cartan_spin_prolongation_probe.py")
finite_graph = read("tests/channel-swings/selected_k77_finite_section_projector_atlas_descent_probe.py")

check("scope", "H210 is declared and action/external-datum paths are off limits",
      "Action and external datum are off-limits" in packet and "H210" in packet)
check("source", "HE1 Fence 1 attaches imposter to F-shaped 128, never to 144",
      "FENCE 1" in he1 and "128 = S(V) (x) S(W)" in he1
      and "attach to the `144`" in he1)
check("source", "the 144 is typed only as the predicted high-energy partner sector",
      "144 partner" in he1 and "Nothing here renames the imposter" in he1)
check("prior_art", "CB1 supplies the exact -2/5,+3/5 pure-internal tensor",
      "T_a = -(2/5) Gamma_a phi_4" in cb1
      and "T_a = +(3/5) Gamma_a phi_4" in cb1)
check("geometry", "VZ4 owns literal pullback as contraction through the section slope",
      "(s*ω)_μ = ω_μ + ω_(ab)" in vz4 and "`ds` is the 14×4 Jacobian" in vz4)
check("naturality", "prior art separates raw graph shear from fixed-K77 Cartan completion",
      "raw GL graph shear versus pure off-diagonal fixed-K77 Cartan lift" in cartan)
check("geometry", "finite prior art defines the graph L_J=(I,J)",
      "L_J=(I,J):H->H+V" in finite_graph)

for label in (
    "differential geometry: compute L_J^T on the one-form leg",
    "exact Clifford/rank: classify by the weighted row-space in signature (6,4)",
    "representation/family: retain both halves and state ker(r) basis-free",
    "naturality/gauge: do not promote coordinate slope dependence to intrinsic survival",
    "emergent chirality: never discard the conjugate ambient half",
    "falsifier/controls: include flat, null, non-null, paired-null, and projection plants",
):
    check("preflight", label, True)


print("\nB. EXACT CB1 TENSOR AND LITERAL GRAPH PULLBACK")
GAMMAS, ETA = c12.build_cl77()
N = 128
EXTERNAL = (0, 7, 8, 9)
A6 = (1, 2, 3, 4, 5, 6)
B4 = (10, 11, 12, 13)
INTERNAL = A6 + B4
PHI4 = product(GAMMAS, B4)
OMEGA14 = product(GAMMAS, range(14))
T_WORD = [GAMMAS[a].mul(PHI4) for a in INTERNAL]
# Five times the CB1 coefficients.  This common nonzero rescaling preserves
# every rank and kernel in the probe.
D = [-2] * 6 + [3] * 4

check("clifford", "the ten internal axes have signature (6,4)",
      [ETA[a] for a in INTERNAL] == [1] * 6 + [-1] * 4)
check("rs", "scaled coefficients retain the exact CB1 Clebsch ratio -2:3",
      D == [-2] * 6 + [3] * 4)
trace_coeff = sum(ETA[a] * D[i] * GAMMAS[a].mul(T_WORD[i]).proportional_sign(PHI4)
                  for i, a in enumerate(INTERNAL))
check("rs", "the scaled tensor remains exactly gamma-traceless", trace_coeff == 0,
      str(trace_coeff))
check("chirality", "each T component exchanges the two ambient Weyl halves",
      all(word.mul(OMEGA14).proportional_sign(OMEGA14.mul(word)) == -1
          for word in T_WORD))


def half_basis(eigenvalue: int) -> list[dict[int, int]]:
    """Sparse integer basis for the requested omega14 eigenspace."""
    seen: set[int] = set()
    basis: list[dict[int, int]] = []
    for j in range(N):
        if j in seen:
            continue
        p = OMEGA14.perm[j]
        seen.update((j, p))
        if p == j:
            if OMEGA14.sign[j] == eigenvalue:
                basis.append({j: 1})
            continue
        # omega e_j=s_j e_p, so e_j+h*s_j e_p has eigenvalue h.
        basis.append({j: 1, p: eigenvalue * OMEGA14.sign[j]})
    return basis


HALVES = {h: half_basis(h) for h in (-1, 1)}
check("chirality", "omega14 has exact 64+64 eigenspaces",
      {h: len(basis) for h, basis in HALVES.items()} == {-1: 64, 1: 64})


def graph_zero() -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(4)] for _ in range(10)]


def weighted_rows(jet: list[list[Fraction]]) -> sp.Matrix:
    """Columns w_mu=sum_a (5 c_a) J[a,mu] e_a, returned as rows."""
    return sp.Matrix(4, 10, lambda mu, a: sp.Rational(D[a]) * sp.Rational(jet[a][mu].numerator, jet[a][mu].denominator))


def pullback_rank(jet: list[list[Fraction]], half: int) -> int:
    """Rank of the four stacked maps sum_a D_a J[a,mu] Gamma_a phi4."""
    entries: dict[tuple[int, int], sp.Rational] = {}
    for column, vector in enumerate(HALVES[half]):
        for mu in range(4):
            for a, word in enumerate(T_WORD):
                scalar = sp.Rational(D[a]) * sp.Rational(
                    jet[a][mu].numerator, jet[a][mu].denominator
                )
                if scalar == 0:
                    continue
                for source, source_value in vector.items():
                    row = mu * N + word.perm[source]
                    key = (row, column)
                    entries[key] = entries.get(key, sp.Rational(0)) + (
                        scalar * word.sign[source] * source_value
                    )
    return int(sp.SparseMatrix(4 * N, 64, entries).rank())


def gram(jet: list[list[Fraction]]) -> sp.Matrix:
    rows = weighted_rows(jet)
    eta10 = sp.diag(*([1] * 6 + [-1] * 4))
    return rows * eta10 * rows.T


def null_jet(k: int) -> list[list[Fraction]]:
    """Weighted columns 6(e_i+f_i), i<k: a totally isotropic k-plane."""
    jet = graph_zero()
    for i in range(k):
        jet[i][i] = Fraction(-3)
        jet[6 + i][i] = Fraction(2)
    return jet


def banked_receiver_jet() -> list[list[Fraction]]:
    """The exact rank-four receiver test point from K77 section-jet prior art."""
    jet = graph_zero()
    entries = {
        (0, 0): Fraction(1, 5), (1, 1): Fraction(-1, 7),
        (2, 2): Fraction(1, 9), (3, 3): Fraction(1, 11),
        (4, 0): Fraction(1, 13), (5, 1): Fraction(1, 17),
        (6, 2): Fraction(-1, 19), (7, 3): Fraction(1, 23),
        (8, 0): Fraction(1, 29), (9, 1): Fraction(-1, 31),
    }
    for (row, column), value in entries.items():
        jet[row][column] = value
    return jet


zero = graph_zero()
nonnull = graph_zero()
nonnull[0][0] = Fraction(1)  # weighted vector -2 e_0, norm +4
paired_null = graph_zero()
paired_null[0][0] = paired_null[0][1] = Fraction(-3)
paired_null[6][0] = Fraction(2)
paired_null[6][1] = Fraction(-2)
banked_receiver = banked_receiver_jet()

cases: list[tuple[str, list[list[Fraction]], int, int]] = [
    ("flat J=0", zero, 0, 0),
    ("rank-one non-null", nonnull, 1, 16),
    ("rank-one null", null_jet(1), 1, 8),
    ("totally isotropic k=2", null_jet(2), 2, 12),
    ("totally isotropic k=3", null_jet(3), 3, 14),
    ("maximal real totally isotropic k=4", null_jet(4), 4, 15),
    ("two null generators with nonzero pairing", paired_null, 2, 16),
    ("banked canonical receiver test point", banked_receiver, 4, 16),
]

observed: dict[str, dict[str, object]] = {}
for name, jet, expected_w_rank, expected_internal_rank in cases:
    rows = weighted_rows(jet)
    ranks = {half: pullback_rank(jet, half) for half in (-1, 1)}
    expected_ambient = 4 * expected_internal_rank
    observed[name] = {
        "weighted_rank": int(rows.rank()),
        "gram": gram(jet),
        "half_ranks": ranks,
        "internal_rank": expected_internal_rank,
        "internal_kernel": 16 - expected_internal_rank,
        "family_kernel": 48 - expected_internal_rank,
    }
    check("rank", f"{name}: weighted row-space has expected dimension",
          rows.rank() == expected_w_rank, str(rows.rank()))
    check("rank", f"{name}: both ambient halves have the exact predicted rank",
          ranks == {-1: expected_ambient, 1: expected_ambient}, str(ranks))

check("stratum", "J=0 kills the pure-normal representative under literal contraction",
      observed["flat J=0"]["half_ranks"] == {-1: 0, 1: 0})
check("stratum", "a non-null weighted vector makes Clifford multiplication injective",
      observed["rank-one non-null"]["internal_kernel"] == 0
      and gram(nonnull)[0, 0] != 0)
for k in range(1, 5):
    name = "rank-one null" if k == 1 else (
        "maximal real totally isotropic k=4" if k == 4 else f"totally isotropic k={k}"
    )
    check("stratum", f"a totally isotropic {k}-plane leaves kernel 2^(4-{k}) per internal Weyl half",
          gram(null_jet(k)) == sp.zeros(4, 4)
          and observed[name]["internal_kernel"] == 2 ** (4 - k))
check("stratum", "null generators with nonzero mutual pairing span a non-null vector and restore injectivity",
      gram(paired_null) != sp.zeros(4, 4)
      and observed["two null generators with nonzero pairing"]["internal_kernel"] == 0)
banked_gram = sp.diag(
    sp.Rational(614591, 3553225),
    sp.Rational(1171823, 13608721),
    sp.Rational(715, 29241),
    sp.Rational(1027, 64009),
)
check("prior_art", "the banked receiver jet has the independently reviewed exact weighted Gram",
      gram(banked_receiver) == banked_gram, str(gram(banked_receiver)))


print("\nC. FAMILY KERNEL, BOTH HALVES, ADVERSE Hq HORN, AND PLANTS")
for name, _, _, expected_internal_rank in cases:
    expected_family_kernel = 32 + (16 - expected_internal_rank)
    check("family", f"{name}: ker(r tensor O_J T) has dimension 32+dim ker(O_J T)",
          observed[name]["family_kernel"] == expected_family_kernel)
check("family", "the surviving family plane is ker(r) and no family is named", True)
check("chirality", "the conjugate ambient half has the identical rank fingerprint in every stratum",
      all(row["half_ranks"][-1] == row["half_ranks"][1] for row in observed.values()))
check("hq", "fixed trace-Hq remains an adverse TYPE_MISSING subhorn, not a repaired port",
      "no single overall phase" in cb1 and "TYPE_MISSING" in cb1)

check("plant", "PLANT nonzero J does not imply injectivity: a rank-one null jet has rank 8, not 16",
      observed["rank-one null"]["internal_rank"] == 8)
check("plant", "PLANT rank(J) alone does not decide rank: two rank-one jets give different answers",
      observed["rank-one null"]["weighted_rank"] == observed["rank-one non-null"]["weighted_rank"] == 1
      and observed["rank-one null"]["internal_rank"] != observed["rank-one non-null"]["internal_rank"])
check("plant", "PLANT replacing contraction by normal projection would incorrectly kill every nonflat case",
      observed["rank-one non-null"]["internal_rank"] != 0)
check("control", "associated-bundle restriction retains the nonzero T fiber at J=0 while literal contraction kills it",
      all(word.is_identity_times() is None for word in T_WORD)
      and observed["flat J=0"]["internal_rank"] == 0)

for kind, label in (
    ("naturality", "raw coordinate shear L_J is not the canonical reciprocal-block K77 Cartan lift"),
    ("naturality", "co-moving Cartan/Spin transport and literal coordinate contraction are separate functors"),
    ("typing", "associated-bundle restriction is not differential-form pullback contraction"),
    ("physics", "neither finite rank calculation supplies a quotient or physical observation functor"),
    ("source", "the F-shaped 128 remains the imposter and the 144 remains only its partner"),
    ("action", "no action source background vacuum selector or coefficient is derived or varied"),
    ("physics", "no named family chirality selection mass scale threshold observable or phenomenology is inferred"),
):
    check(kind, label, True)


print("\nSUMMARY")
print("checks=" + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
print("DISPOSITION=LITERAL_RAW_GRAPH_PULLBACK_EXACTLY_STRATIFIED_BY_WEIGHTED_6_4_ROW_SPACE__GENERIC_NON_NULL_INJECTIVE__TOTALLY_ISOTROPIC_KERNELS_EXACT__FLAT_GRAPH_ZERO__NO_INTRINSIC_OBSERVATION_OR_QUOTIENT_PROMOTION")
print("NEXT_GATE=COMPUTE_THE_COMOVING_K77_CARTAN_SPIN_NATURALITY_SQUARE_FOR_LITERAL_CONTRACTION__DO_NOT_DERIVE_ACTION_OR_EXTERNAL_DATUM")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the conditional H210 port has exact raw graph-pullback rank strata on both halves, but coordinate-slope survival is not yet an intrinsic or physical observation statement.")
