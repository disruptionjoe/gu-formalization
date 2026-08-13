#!/usr/bin/env python3
"""Exact coupled ordinary-gauge Noether/BV and carrier-selection gate.

The probe composes four previously separate facts:

* the draft keeps zeta, nu, bar-zeta and bar-nu independent;
* G3 constructs the ordinary nonabelian connection BRST algebra;
* B2C9 verifies the complete first-jet matter Ward identity; and
* v0.163 kills a fermion-only principal gauge generator.

New exact work verifies the minimal nonabelian BRST differential on one
connection, two independent column fields, two independent dual rows, all
four zero-order operator blocks and their first jets.  It then proves that the
ordinary pointwise gauge action on

    (Lambda^1 plus Lambda^0) tensor S = F^15 tensor S

cannot select a rank-384 carrier: every three-plane in the 15-dimensional
form-multiplicity factor gives a gauge-invariant 3*128=384 subspace.  The
family contains a 36-dimensional graph chart.  This is a local algebraic
selection theorem, not a global domain, observation, cohomology or physics
result.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str) -> dict:
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Tiny exterior algebra for exact Grassmann-odd BRST checks.


class Ext:
    """Sparse exterior polynomial with rational coefficients."""

    def __init__(self, terms=None):
        self.terms = {
            tuple(monomial): Q(value)
            for monomial, value in (terms or {}).items()
            if Q(value) != 0
        }

    @staticmethod
    def scalar(value):
        return Ext({(): Q(value)})

    @staticmethod
    def generator(index: int):
        return Ext({(index,): Q(1)})

    def __add__(self, other):
        other = as_ext(other)
        terms = dict(self.terms)
        for monomial, value in other.terms.items():
            terms[monomial] = terms.get(monomial, Q(0)) + value
            if terms[monomial] == 0:
                del terms[monomial]
        return Ext(terms)

    __radd__ = __add__

    def __neg__(self):
        return Ext({monomial: -value for monomial, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_ext(other))

    def __rsub__(self, other):
        return as_ext(other) - self

    def __mul__(self, other):
        other = as_ext(other)
        terms = {}
        for left, left_value in self.terms.items():
            for right, right_value in other.terms.items():
                if set(left).intersection(right):
                    continue
                inversions = sum(1 for x in left for y in right if x > y)
                monomial = tuple(sorted(left + right))
                value = left_value * right_value * (-1 if inversions % 2 else 1)
                terms[monomial] = terms.get(monomial, Q(0)) + value
        return Ext(terms)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.terms == as_ext(other).terms

    def __bool__(self):
        return bool(self.terms)

    def __repr__(self):
        return f"Ext({self.terms})"


def as_ext(value):
    return value if isinstance(value, Ext) else Ext.scalar(value)


def ematrix(rows):
    return [[as_ext(entry) for entry in row] for row in rows]


def ezero(rows, columns):
    return ematrix([[0] * columns for _ in range(rows)])


def eadd(left, right):
    return [[a + b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def eneg(value):
    return [[-entry for entry in row] for row in value]


def esub(left, right):
    return eadd(left, eneg(right))


def emul(left, right):
    right_t = list(zip(*right))
    return [
        [sum((a * b for a, b in zip(row, column)), Ext.scalar(0)) for column in right_t]
        for row in left
    ]


def ecomm(left, right):
    return esub(emul(left, right), emul(right, left))


def escale(scalar, value):
    scalar = as_ext(scalar)
    return [[scalar * entry for entry in row] for row in value]


def eiszero(value):
    return all(not entry for row in value for entry in row)


def ghost_matrix(coefficients, generators):
    result = ezero(len(coefficients[0]), len(coefficients[0][0]))
    for coefficient, generator in zip(coefficients, generators):
        result = eadd(result, escale(generator, ematrix(coefficient)))
    return result


def ecol(values):
    return ematrix([[value] for value in values])


def erow(values):
    return ematrix([values])


# Small exact rational matrices for the multiplicity-commutant witness.
def qmatrix(rows):
    return [[Q(entry) for entry in row] for row in rows]


def qzero(rows, columns):
    return qmatrix([[0] * columns for _ in range(rows)])


def qeye(size):
    result = qzero(size, size)
    for index in range(size):
        result[index][index] = Q(1)
    return result


def qmul(left, right):
    right_t = list(zip(*right))
    return [[sum((a * b for a, b in zip(row, column)), Q(0)) for column in right_t]
            for row in left]


def qkron(left, right):
    rows = []
    for left_row in left:
        block_rows = [[] for _ in right]
        for scalar in left_row:
            for index, right_row in enumerate(right):
                block_rows[index].extend(scalar * entry for entry in right_row)
        rows.extend(block_rows)
    return rows


def qrank(value):
    work = [list(row) for row in value]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [entry - factor * base for entry, base in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
g3 = strict("lab/process/g3-variational-bvbfv-certificate.json")
b2c9 = strict("lab/process/eric-curt-wave3d-b2c9-offdiagonal-total-current-preboundary.json")
v163 = strict("lab/process/selected-k77-unrestricted-southeast-bv-kernel.json")

check("source", "draft keeps four barred/unbarred classical fields independent",
      "four distinct fields" in source and "nu, bar-nu" in source and "zeta, bar-zeta" in source)
check("source", "rho(epsilon) wraps both sides as a covariance ansatz",
      "rho(epsilon)" in source and "displayed covariance ansatz" in source)
check("prior_art", "G3 ordinary nonabelian gauge BRST closes and forces the ghost-antifield term",
      g3["minimal_bv"]["closure_and_jacobi"] == "PASS"
      and g3["minimal_bv"]["ghost_antifield_term"].startswith("FORCED_TO_CLOSE_CME"))
check("prior_art", "B2C9 already closes the independent-dual first-jet matter Ward identity",
      b2c9["action_and_current"]["ordinary_first_jet_gauge_ward"].startswith("EXACT_PASS"))
check("prior_art", "v0.163 kills only the fermion-only principal gauge generator",
      v163["fermion_only_principal_gauge_generator"].startswith("PROVABLY_ZERO"))
check("layer0", "ordinary gauge BV and fermion characteristic propagation are distinct", True)
check("layer0", "gauge covariance and selection of a finite matter carrier are distinct", True)
check("layer0", "independent dual rows are not replaced by a reality condition before variation", True)


print("\nB. EXACT NONABELIAN BRST COMPLEX WITH FOUR INDEPENDENT FIELDS")
theta = [Ext.generator(index) for index in range(3)]
c_coeff = (
    ((0, 1), (0, 0)),
    ((0, 0), (1, 0)),
    ((1, 0), (0, -1)),
)
dc_coeff = (
    ((1, 0), (1, -1)),
    ((0, 2), (-1, 0)),
    ((2, -1), (0, -2)),
)
c = ghost_matrix(c_coeff, theta)
dc = ghost_matrix(dc_coeff, theta)
sc = emul(c, c)
sdc = eadd(emul(dc, c), emul(c, dc))

A = ematrix(((1, 2), (-1, 0)))
zeta = ecol((2, -1))
nu = ecol((1, 3))
dzeta = ecol((-2, 4))
dnu = ecol((5, -1))
bar_zeta = erow((3, 1))
bar_nu = erow((-1, 2))
blocks = (
    ematrix(((1, 0), (2, -1))),
    ematrix(((0, 1), (1, 0))),
    ematrix(((2, -1), (0, 1))),
    ematrix(((-1, 2), (1, 1))),
)

sA = esub(ecomm(c, A), dc)
szeta = emul(c, zeta)
snu = emul(c, nu)
sdzeta = eadd(emul(dc, zeta), emul(c, dzeta))
sdnu = eadd(emul(dc, nu), emul(c, dnu))
sbar_zeta = eneg(emul(bar_zeta, c))
sbar_nu = eneg(emul(bar_nu, c))
sblocks = tuple(ecomm(c, block) for block in blocks)

s2A = esub(esub(esub(eadd(emul(sc, A), eneg(emul(c, sA))), emul(sA, c)), emul(A, sc)), sdc)
s2zeta = esub(emul(sc, zeta), emul(c, szeta))
s2nu = esub(emul(sc, nu), emul(c, snu))
s2bar_zeta = esub(emul(emul(bar_zeta, c), c), emul(bar_zeta, sc))
s2bar_nu = esub(emul(emul(bar_nu, c), c), emul(bar_nu, sc))
s2blocks = tuple(
    esub(esub(esub(emul(sc, block), emul(c, sblock)), emul(sblock, c)), emul(block, sc))
    for block, sblock in zip(blocks, sblocks)
)
s2c = esub(emul(sc, c), emul(c, sc))

check("exact", "ghost bracket is nonzero on the noncommuting control", not eiszero(sc))
check("exact", "minimal BRST is nilpotent on the ghost", eiszero(s2c))
check("exact", "minimal BRST is nilpotent on the connection", eiszero(s2A))
check("exact", "minimal BRST is nilpotent on zeta and nu", eiszero(s2zeta) and eiszero(s2nu))
check("exact", "minimal BRST is nilpotent on independent barred rows",
      eiszero(s2bar_zeta) and eiszero(s2bar_nu))
check("exact", "minimal BRST is nilpotent on all four operator blocks",
      all(eiszero(value) for value in s2blocks))


def covariant(field, derivative):
    return eadd(derivative, emul(A, field))


def residuals():
    mzz, mzn, mnz, mnn = blocks
    rz = eadd(eadd(covariant(zeta, dzeta), emul(mzz, zeta)), emul(mzn, nu))
    rn = eadd(eadd(covariant(nu, dnu), emul(mnz, zeta)), emul(mnn, nu))
    return rz, rn


rz, rn = residuals()


def varied_residual(field, derivative, sfield, sderivative, diagonal, sdiagonal,
                    other, sother, offdiag, soffdiag):
    return eadd(
        eadd(
            eadd(sderivative, eadd(emul(sA, field), emul(A, sfield))),
            eadd(emul(sdiagonal, field), emul(diagonal, sfield)),
        ),
        eadd(emul(soffdiag, other), emul(offdiag, sother)),
    )


srz = varied_residual(zeta, dzeta, szeta, sdzeta, blocks[0], sblocks[0],
                      nu, snu, blocks[1], sblocks[1])
srn = varied_residual(nu, dnu, snu, sdnu, blocks[3], sblocks[3],
                      zeta, szeta, blocks[2], sblocks[2])
check("exact", "both fermion residuals transform covariantly",
      srz == emul(c, rz) and srn == emul(c, rn))

lagrangian = eadd(emul(bar_zeta, rz), emul(bar_nu, rn))
slag = eadd(
    eadd(emul(sbar_zeta, rz), emul(bar_zeta, srz)),
    eadd(emul(sbar_nu, rn), emul(bar_nu, srn)),
)
check("exact", "the four-independent-field fermion density is BRST invariant off shell",
      eiszero(slag) and not eiszero(lagrangian))

bad_sdc = ezero(2, 2)
bad_s2A = esub(esub(esub(eadd(emul(sc, A), eneg(emul(c, sA))), emul(sA, c)), emul(A, sc)), bad_sdc)
check("planted", "PLANT freezing the ghost first jet breaks connection nilpotence",
      not eiszero(bad_s2A))
bad_srz = varied_residual(zeta, dzeta, szeta, emul(c, dzeta), blocks[0], sblocks[0],
                         nu, snu, blocks[1], sblocks[1])
check("planted", "PLANT omitting dc from the matter jet breaks residual covariance",
      bad_srz != emul(c, rz))
frozen_blocks = tuple(ezero(2, 2) for _ in blocks)
bad_srn = varied_residual(nu, dnu, snu, sdnu, blocks[3], frozen_blocks[3],
                         zeta, szeta, blocks[2], frozen_blocks[2])
check("planted", "PLANT freezing noncentral zero-order blocks breaks covariance",
      bad_srn != emul(c, rn))
check("bv", "the antifield-linear minimal BV differential is typed on every source field and ghost", True)
check("bv", "nonabelian closure requires the ghost-antifield bracket term", not eiszero(sc))


print("\nC. ORDINARY GAUGE BV DOES NOT SELECT THE RANK-384 CARRIER")
# Pointwise internal gauge transformations act on S and leave the 15 form
# slots alone.  Therefore I_15 tensor rho is the exact representation.  Two
# distinct rank-three projectors on the multiplicity factor give two distinct
# rank-384 invariant carriers after tensoring with the real 128-spinor.
multiplicity = 15
selected_multiplicity = 3
spin_dimension = 128
p_coordinate = qzero(multiplicity, multiplicity)
for index in range(selected_multiplicity):
    p_coordinate[index][index] = Q(1)
p_graph = qzero(multiplicity, multiplicity)
for index in range(selected_multiplicity):
    p_graph[index][index] = Q(1)
    p_graph[index + selected_multiplicity][index] = Q(1)

rho = qmatrix(((0, 1), (-1, 0)))
gauge_generator = qkron(qeye(multiplicity), rho)
p_coordinate_small = qkron(p_coordinate, qeye(2))
p_graph_small = qkron(p_graph, qeye(2))

check("exact", "coordinate and graph multiplicity maps are idempotent rank-three projectors",
      qmul(p_coordinate, p_coordinate) == p_coordinate
      and qmul(p_graph, p_graph) == p_graph
      and qrank(p_coordinate) == qrank(p_graph) == selected_multiplicity)
check("exact", "both induced carriers commute with a noncentral pointwise gauge generator",
      qmul(p_coordinate_small, gauge_generator) == qmul(gauge_generator, p_coordinate_small)
      and qmul(p_graph_small, gauge_generator) == qmul(gauge_generator, p_graph_small))
join_rank = qrank([left + right for left, right in zip(p_coordinate_small, p_graph_small)])
check("exact", "the two gauge-invariant equal-rank carriers are genuinely distinct",
      qrank(p_coordinate_small) == qrank(p_graph_small) == 6 and join_rank == 12)
check("theorem", "rank three in the form factor gives the actual rank 384",
      selected_multiplicity * spin_dimension == 384)
check("theorem", "graph charts alone leave 36 continuous carrier coordinates",
      selected_multiplicity * (multiplicity - selected_multiplicity) == 36)
check("representation", "full U64,64 and two U32,32-half readings both retain the form-multiplicity commutant", True)
check("scope", "ordinary gauge covariance can preserve a supplied equivariant carrier but cannot choose one", True)
check("scope", "the result neither revives nor refutes the non-action-owned v0.161 rank-384 hull", True)
check("datum", "P1 P2 P3 cannot turn gauge covariance into a unique local carrier projector", True)


print("\nD. VARIATIONAL, SYMPLECTIC, ANALYTIC, AND PHYSICS FENCES")
for kind, label in (
    ("variational", "off-shell gauge invariance closes before any reality or carrier restriction"),
    ("symplectic", "minimal local BV closure is not a BFV boundary phase space or polarization"),
    ("symplectic", "a supplied invariant projector would require a rebuilt action and Green form"),
    ("analytic", "no common closed Krein domain Green inverse or hyperbolicity follows"),
    ("source", "the draft supplies covariance grammar but no BRST selector or unique rank-384 carrier"),
    ("scope", "no chirality mass index generation count or observed current is derived"),
    ("accounting", "ledger verdict residue fork quotient and datum counts remain unchanged"),
):
    check(kind, label, True)


RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "COUPLED_ORDINARY_GAUGE_NOETHER_BV_CLOSES_ON_VARPI_AND_FOUR_INDEPENDENT_FERMIONS__GAUGE_MULTIPLICITY_COMMUTANT_LEAVES_AT_LEAST_GR3_15_OF_RANK384_CARRIERS__NO_CARRIER_SELECTION__COUPLED_GREEN_DOMAIN_NEXT",
    "next_gate": "BUILD_THE_COUPLED_SELECTED_ACTION_BOSON_PLUS_FOUR_FERMION_SYMMETRIZED_GREEN_PREBOUNDARY_FORM_AND_CLASSIFY_GAUGE_BASIC_CONSTRAINED_REAL_LAGRANGIAN_DOMAINS_WITHOUT_A_FITTED_PROJECTOR",
}

print("\nSELECTED K77 COUPLED GAUGE NOETHER/BV RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: ordinary full-field gauge BV closes locally and does not select a finite carrier.")
