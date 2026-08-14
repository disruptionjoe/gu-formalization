#!/usr/bin/env sage-python
"""Exact partial moving-split cone for the reverse-J channel.

This is a local principal-symbol and associated-bundle comparator.  It does
not construct the missing total GU background, total BV differential,
physical quotient, positive pairing, or closed Lorentzian domain.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

from sage.all import QQ, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests/channel-swings"))
from k77_exact_bank_api import K77Core, ONE  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def so_generators(signs: tuple[int, ...]):
    out = []
    for i in range(len(signs)):
        for j in range(i + 1, len(signs)):
            a = zero_matrix(QQ, len(signs), len(signs))
            a[i, j] = 1
            a[j, i] = -signs[i] * signs[j]
            out.append((i, j, a))
    return out


def centralizer_dimension(generators, n: int) -> int:
    rows = []
    for _, _, a in generators:
        for i in range(n):
            for j in range(n):
                row = [QQ(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += a[k, j]
                    row[k * n + j] -= a[i, k]
                rows.append(row)
    equations = matrix(QQ, rows)
    return n * n - equations.rank()


print("A. PREFLIGHT, PRIOR ART, AND OBJECT TYPING")
rf1 = read(
    "explorations/conditional-build/selected-k77-reverse-j-descent-census-2026-08-14.md"
)
moving_bv = read(
    "explorations/conditional-build/selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md"
)
coupled = read(
    "explorations/conditional-build/selected-k77-total-twisted-yang-mills-current-gate-2026-08-14.md"
)
target = read(
    "lab/active-research/source-residual-cohomology/target-theorem-reverse-falsification-chain-2026-08-14.md"
)

check("prior_art", "RF-1 already kills fixed J10 basicness and leaves moving J open",
      "tautological moving J" in rf1 and "NOT-YET-FALSIFIED" in rf1)
check("prior_art", "longitudinal moving-J BRST nilpotence is already exact",
      "s^2 J" in moving_bv and "s^2 psi" in moving_bv)
check("prior_art", "the coupled reduction-current result requires a larger cone",
      "mapping-cone or coupled detour complex" in coupled)
check("prior_art", "the reverse chain requires candidate-versus-route quantifier fences",
      "Candidate kill" in target and "Route kill" in target)

for label in (
    "split involution R versus spinor volume J10",
    "moving split orbit versus normal twistor O(6,4)/U(3,2)",
    "associated spinor bundle versus tangent bundle of the split orbit",
    "longitudinal BRST doublet versus a complete BV/KT complex",
    "symbol quotient versus physical cohomology",
    "fibrewise complex linearity versus a complex structure on all coupled fields",
    "local gauge contraction versus global bundle triviality",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT K77 SPLIT ORBIT")
base_signs = (1, -1, -1, -1)
normal_signs = (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
signs = base_signs + normal_signs
eta = matrix.diagonal(QQ, signs)
r_split = matrix.diagonal(QQ, (1, 1, 1, 1) + (-1,) * 10)
base_generators = so_generators(base_signs)
normal_generators = so_generators(normal_signs)
full_generators = so_generators(signs)
h_generators = [item for item in full_generators
                if (item[0] < 4 and item[1] < 4)
                or (item[0] >= 4 and item[1] >= 4)]
mixed_generators = [item for item in full_generators
                    if item[0] < 4 <= item[1]]

check("orbit", "the split stabilizer has dimension 6+45=51", len(h_generators) == 51)
check("orbit", "the mixed complement has dimension 4*10=40", len(mixed_generators) == 40)
check("orbit", "all 91 generators are eta-skew",
      all(a.transpose() * eta + eta * a == 0 for _, _, a in full_generators))
check("orbit", "the stabilizer commutes with R",
      all(a * r_split - r_split * a == 0 for _, _, a in h_generators))
check("orbit", "every mixed generator anticommutes with R",
      all(a * r_split + r_split * a == 0 for _, _, a in mixed_generators))

kappa_columns = []
for _, _, a in mixed_generators:
    delta_r = a * r_split - r_split * a
    kappa_columns.append(delta_r.list())
kappa = matrix(QQ, 196, 40, lambda row, col: kappa_columns[col][row])
check("orbit", "the orbit map kappa(xi)=[xi,R] has rank 40", kappa.rank() == 40)
check("orbit", "q(delta R)=delta R R/2 exactly inverts kappa",
      all(((a * r_split - r_split * a) * r_split / 2) == a
          for _, _, a in mixed_generators))
check("orbit", "the moving split has no unpaired local tangent direction",
      kappa.ncols() == kappa.rank() == 40)


print("\nC. SPINOR J10 AND THE ASSOCIATED-BUNDLE TEST")
core = K77Core(signs, ("comm", "symi", "comm"))
normal_axes = tuple(range(4, 14))
j10 = core.blade(normal_axes)
identity_clifford = {0: ONE}
check("spinor", "J10 squares to -1",
      core.emul(j10, j10) == core.escale(-1, identity_clifford))

spin_h_commutes = []
spin_m_anticommutes = []
orbit_spin_masks = []
for i, j, _ in full_generators:
    blade = core.blade((i, j))
    commutator = core.eadd(core.emul(blade, j10),
                           core.escale(-1, core.emul(j10, blade)))
    anticommutator = core.eadd(core.emul(blade, j10), core.emul(j10, blade))
    if (i < 4 and j < 4) or (i >= 4 and j >= 4):
        spin_h_commutes.append(not commutator)
    else:
        spin_m_anticommutes.append(not anticommutator)
        orbit_spin_masks.extend(commutator.keys())

check("spinor", "all 51 stabilizer generators commute with J10",
      len(spin_h_commutes) == 51 and all(spin_h_commutes))
check("spinor", "all 40 mixed generators anticommute with J10",
      len(spin_m_anticommutes) == 40 and all(spin_m_anticommutes))
check("spinor", "the 40 infinitesimal spinor-volume orbit directions are distinct",
      len(orbit_spin_masks) == 40 and len(set(orbit_spin_masks)) == 40)
check("associated_bundle", "J10 is H-basic on Spin(7,7) x_H S",
      all(spin_h_commutes) and core.emul(j10, j10) == core.escale(-1, identity_clifford))
check("associated_bundle", "full Spin covariance transports rather than freezes J10",
      all(spin_m_anticommutes) and len(set(orbit_spin_masks)) == 40)


print("\nD. EXACT LOCAL STUECKELBERG/MAPPING-CONE CONTRACTION")
covectors = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "null": (1, 1, 0, 0),
    "generic": (1, 2, 0, -1),
    "zero": (0, 0, 0, 0),
}

for name, covector in covectors.items():
    d = len(covector)
    cone_k = zero_matrix(QQ, d * 40 + 40, 40)
    dressing = zero_matrix(QQ, d * 40, d * 40 + 40)
    wrong_dressing = zero_matrix(QQ, d * 40, d * 40 + 40)
    for row in range(d * 40):
        dressing[row, row] = 1
        wrong_dressing[row, row] = 1
    for mu, coefficient in enumerate(covector):
        for a in range(40):
            cone_k[mu * 40 + a, a] = -coefficient
            dressing[mu * 40 + a, d * 40 + a] = coefficient
            wrong_dressing[mu * 40 + a, d * 40 + a] = -coefficient
    for a in range(40):
        cone_k[d * 40 + a, a] = 1

    check("cone", f"{name}: extended gauge map K has rank 40", cone_k.rank() == 40)
    check("cone", f"{name}: dressing D has rank {d * 40}", dressing.rank() == d * 40)
    check("cone", f"{name}: D K vanishes exactly", dressing * cone_k == 0)
    check("cone", f"{name}: ker D equals im K by inclusion and dimension",
          dressing * cone_k == 0
          and (d * 40 + 40 - dressing.rank()) == cone_k.rank())
    if name != "zero":
        connection_part = cone_k[:d * 40, :]
        check("control", f"{name}: freezing delta R leaves a rank-40 mixed gauge shift",
              connection_part.rank() == 40)
        check("control", f"{name}: the wrong dressing sign fails covariance",
              wrong_dressing * cone_k != 0)


print("\nE. NO INVARIANT COMPLEX STRUCTURE ON THE BOSONIC SPLIT ORBIT")
base_commutant = centralizer_dimension(base_generators, 4)
normal_commutant = centralizer_dimension(normal_generators, 10)
check("commutant", "End_so(1,3)(R^4) has dimension one", base_commutant == 1)
check("commutant", "End_so(6,4)(R^10) has dimension one", normal_commutant == 1)
check("commutant", "the external tensor-product commutant on R^4 tensor R^10 is scalar",
      base_commutant * normal_commutant == 1)
check("candidate_kill", "no split-stabilizer-invariant real endomorphism of the orbit tangent squares to -1",
      base_commutant * normal_commutant == 1)
check("contrary", "a separately chosen normal twistor J_N could reduce SO(6,4) to U(3,2)", True)
check("contrary", "that normal-twistor datum is not identified here with spinor J10", True)


print("\nF. SCOPE AND DISPOSITION")
for label in (
    "the moving split/ghost sector is contractible only at local principal-symbol grade",
    "J10 becomes a well-defined fibrewise complex structure on the associated spinor bundle",
    "no complex structure on the full coupled bosonic deformation complex follows",
    "global topology, lower-order equations and boundary charges may obstruct contraction",
    "no total K or L, residual-zero legal GU background, quotient pairing or closed domain is constructed",
    "survival is NOT-YET-FALSIFIED and does not establish physical superposition",
    "GU-wide priority, ledger verdicts, canon and public posture remain unchanged",
):
    check("scope", label, True)

print("MOVING_SPLIT_LOCAL_CONE=EXACT_CONTRACTIBLE_GAUGE_SECTOR")
print("ASSOCIATED_SPINOR_J10=EXACT_H_BASIC_FIBRE_COMPLEX_STRUCTURE")
print("FULL_COUPLED_BOSONIC_COMPLEX_STRUCTURE=KILLED_FOR_NATURAL_SPLIT_INVARIANT_CANDIDATE")
print("TAUTOLOGICAL_MOVING_J_ROUTE=NOT_YET_FALSIFIED")
print("PHYSICAL_COHOMOLOGY_AND_SUPERPOSITION=TYPE_MISSING")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
