#!/usr/bin/env python3
"""Exact SN-2 local neutral reality/charge admissibility classifier.

This probe composes existing exact receipts; it does not select an action,
coefficient, vacuum, global reality/domain, quotient, or physical mass.  The
source ``zeta/nu`` slots remain Omega1/Omega0 fields and are never relabelled
as four-dimensional ``nu_L/nu_R``.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("SN2_MUTATION", "")
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = None) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        if detail is not None:
            print(f"  detail: {detail}")
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def strict_json(relative: str):
    path = ROOT / relative

    def reject_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def add2(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def mul2(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def trans2(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def neg2(a):
    return [[-x for x in row] for row in a]


def mv2(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))


def conjv(v):
    return tuple(x.conjugate() for x in v)


ZERO = [[0, 0], [0, 0]]
I2 = [[1, 0], [0, 1]]
J2 = [[0, 1], [-1, 0]]


print("A. SOURCE, ROUTING, AND NOVELTY CUSTODY")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
claims = read("lab/sources/source-claim-register.yaml")
routing = read("lab/methods/source-native-comparator-routing.md")
sn1 = read("lab/active-research/joe-directed/majorana-126-neutrino/sn1-observed-neutrino-mass-pencil-2026-08-16.md")
cs1 = read("lab/active-research/joe-directed/class-shift/cs1-first-order-shift-is-the-chirality-grading-2026-08-15.md")
artifact = read("lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-reality-charge-admissibility-2026-08-16.md")
atomic = strict_json("lab/process/resolver-wave-k77a-atomic-particle-crosswalk.json")
pairing = strict_json("lab/process/selected-k77-action-adjoint-weight-classification.json")
graphs = strict_json("lab/process/selected-k77-graded-green-reality-graphs.json")

source_independent = "four distinct fields" in source
if MUT == "source_independence":
    source_independent = False
check("source", "SC-OP-04 keeps barred and unbarred variables four distinct classical fields",
      source_independent and "- id: SC-OP-04" in claims)
check("source", "SC-OP-05 keeps a nonzero southeast rival admitted but unselected",
      "- id: SC-OP-05" in claims and "non-trivial lower-right" in claims)
check("source", "source slots retain Omega0 nu and Omega1 zeta typing",
      "nu, bar-nu     in Omega^0(Y,S)" in source
      and "zeta, bar-zeta in Omega^1(Y,S)" in source)
check("routing", "artifact declares the source-native route and carries the uniform routing notice",
      "Classification: `SOURCE_NATIVE_ROUTE`" in artifact
      and "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Standard Majorana/anomaly/unification diagnostics versus native owners" in routing)
check("novelty", "SN1 already owns undefined Majorana status and the non-hierarchical southeast-zero result",
      "Majorana status: UNDEFINED_WITHOUT_REALITY_MAP" in sn1
      and "a zero corner" in sn1 and "hierarchy mechanism" in sn1)
check("novelty", "CS1 already owns the four corner classes and unique uniform source reading",
      "four corners `3,1,1,3`" in cs1
      and "Exactly one survives" in cs1)


print("\nB. EXACT SOURCE CELL AND Z/4 CENTRE CLASSIFICATION")
# Winning CS1 uniform convention: one-form printed signs are centre labels,
# while barred rows are independent fields in the same bundles.
field_classes = {
    "nu+": 3,
    "nu-": 1,
    "zeta+": 3,  # printed zeta+ is the class-3 Omega1(S-) corner
    "zeta-": 1,
}
if MUT == "centre_formula":
    field_classes["zeta+"] = 1

rows = ("zeta-", "zeta+", "nu-", "nu+")
cols = ("zeta+", "zeta-", "nu+", "nu-")
row_classes = [field_classes[x] for x in rows]
col_classes = [field_classes[x] for x in cols]
D0_CELLS = ((0, 1), (0, 3), (1, 0), (1, 2), (2, 1), (3, 0))
VARPI_CELLS = ((0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (3, 1))
SE_ZERO = ((2, 2), (2, 3), (3, 2), (3, 3))

check("centre", "winning row/column classes are exact",
      row_classes == [1, 3, 1, 3] and col_classes == [3, 1, 3, 1],
      (row_classes, col_classes))
check("source_cells", "identity-grade six derivative, six varpi-only, and four southeast cells partition 4x4",
      len(set(D0_CELLS) | set(VARPI_CELLS) | set(SE_ZERO)) == 16
      and not (set(D0_CELLS) & set(VARPI_CELLS))
      and not (set(D0_CELLS) & set(SE_ZERO))
      and not (set(VARPI_CELLS) & set(SE_ZERO)))
check("centre", "all six derivative cells obey the first-order action class rule",
      all((row_classes[i] + 2 + col_classes[j]) % 4 == 0 for i, j in D0_CELLS))
varpi_net = [(-row_classes[i] - col_classes[j]) % 4 for i, j in VARPI_CELLS]
check("centre", "all six printed varpi-only action cells have net required class zero",
      varpi_net == [0] * 6, varpi_net)

se_net = {(i, j): (-row_classes[i] - col_classes[j]) % 4 for i, j in SE_ZERO}
expected_se = {(2, 2): 0, (2, 3): 2, (3, 2): 2, (3, 3): 0}
if MUT == "se_uniform":
    expected_se = {cell: 2 for cell in SE_ZERO}
check("centre", "southeast zero splits into two net-class-0 and two net-class-2 cells",
      se_net == expected_se and sorted(se_net.values()) == [0, 0, 2, 2], se_net)
se_first_order = [cell for cell in SE_ZERO
                  if (row_classes[cell[0]] + 2 + col_classes[cell[1]]) % 4 == 0]
check("centre", "exactly two southeast cells are first-order class-allowed",
      se_first_order == [(2, 3), (3, 2)], se_first_order)
check("semantic", "ambient centre requirement is not identified with B-L charge",
      "ambient centre class 2  !=  B-L charge 2" in artifact)


print("\nC. OBSERVED NEUTRAL LINES AND CHARGE OBSTRUCTIONS")
charge_rows = {row["row_id"]: row for row in atomic["fermion_charge_dictionary"]}
left_row = charge_rows["neutrino_left"]
right_row = charge_rows["neutrino_right"]
check("charge", "atomic dictionary has exact Q=0 neutral L and N^c rows",
      F(left_row["T3L"]) == F(1, 2) and F(left_row["Y"]) == F(-1, 2)
      and F(left_row["Q_all_left"]) == 0
      and right_row["all_left_state"] == "nu_L_c"
      and F(right_row["T3L"]) == 0 and F(right_row["Y"]) == 0
      and F(right_row["Q_all_left"]) == 0)

L = {"su2": 2, "Y": F(-1, 2), "Q": F(0), "BL": F(-1)}
Nc = {"su2": 1, "Y": F(0), "Q": F(0), "BL": F(1)}
if MUT == "charge_conjugate":
    Nc["BL"] = F(-1)
physical_nu_R_BL = -Nc["BL"]
check("charge", "all-left N^c has B-L=+1 while physical nu_R has B-L=-1",
      Nc["BL"] == 1 and physical_nu_R_BL == -1)

dirac = {"su2": 2, "Y": L["Y"] + Nc["Y"], "Q": L["Q"] + Nc["Q"],
         "BL": L["BL"] + Nc["BL"]}
majorana_r = {"su2": 1, "Y": 2 * Nc["Y"], "Q": 2 * Nc["Q"],
              "BL": 2 * Nc["BL"]}
majorana_l_neutral = {"weak_product": "1+3", "Y": 2 * L["Y"],
                      "Q_component": 2 * L["Q"], "BL": 2 * L["BL"]}

check("charge", "L N^c is Q and B-L neutral but remains a weak doublet of Y=-1/2",
      dirac == {"su2": 2, "Y": F(-1, 2), "Q": 0, "BL": 0}, dirac)
check("charge", "N^c N^c is an SM singlet under SU3xSU2xY but carries B-L=+2",
      majorana_r == {"su2": 1, "Y": 0, "Q": 0, "BL": 2}, majorana_r)
check("charge", "the Q=0 component of L L still has Y=-1 and B-L=-2 with unresolved weak tensor",
      majorana_l_neutral == {"weak_product": "1+3", "Y": -1,
                             "Q_component": 0, "BL": -2}, majorana_l_neutral)
q_zero_means_singlet = MUT == "q_singlet"
check("planted", "PLANT Q=0 does not imply full-SM singlet status",
      not q_zero_means_singlet and L["Q"] == 0 and (L["su2"], L["Y"]) != (1, 0))
check("charge", "Dirac and right-Majorana compensator charges are exact",
      (F(1, 2), 0) == (-dirac["Y"], -dirac["BL"])
      and (0, -2) == (-majorana_r["Y"], -majorana_r["BL"]))


print("\nD. BOTH BANKED PAIRING HORNS AND NONCIRCULAR LOCAL FIXED GRAPHS")
check("receipt", "pairing receipt owns exactly the symmetric/anti and skew/self horns",
      pairing["anti_adjoint_pairing_line"] == [1, 1, 1, 1]
      and pairing["anti_adjoint_pairing_symmetry"] == "SYMMETRIC"
      and pairing["self_adjoint_pairing_line"] == [1, -1, -1, 1]
      and pairing["self_adjoint_pairing_symmetry"] == "SKEW"
      and pairing["pairing_ranks"] == [1920, 1920]
      and pairing["exact_primes"] == [1009, 1013]
      and pairing["directions_checked_each_prime"] == 14)
check("receipt", "graded receipt owns both noncharacteristic reality graphs but no analytic domain",
      set(graphs["action_pairing_horns"]) == {"symmetric_anti_adjoint", "skew_self_adjoint"}
      and all("NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH" == value
              for value in graphs["action_pairing_horns"].values())
      and graphs["analytic_domain"].startswith("OPEN"))

P_sym, A_anti = I2, J2
P_skew, A_self = J2, I2
if MUT == "horn_swap":
    P_skew = I2
check("grassmann", "symmetric P plus P-anti-adjoint A gives alternating P A",
      add2(mul2(P_sym, A_anti), trans2(mul2(P_sym, A_anti))) == ZERO)
check("grassmann", "skew P plus P-self-adjoint A gives alternating P A",
      add2(mul2(P_skew, A_self), trans2(mul2(P_skew, A_self))) == ZERO)
check("graded", "both horns satisfy P^T A + A^T P=0",
      add2(mul2(trans2(P_sym), A_anti), mul2(trans2(A_anti), P_sym)) == ZERO
      and add2(mul2(trans2(P_skew), A_self), mul2(trans2(A_self), P_skew)) == ZERO)


def reality_exchange(P, Pinv, psi, bar):
    return mv2(Pinv, conjv(bar)), mv2(P, conjv(psi))


psi = (1 + 2j, 3 - 1j)
for name, P, Pinv in (("symmetric", P_sym, I2), ("skew", P_skew, neg2(J2))):
    bar = mv2(P, conjv(psi))
    if MUT == "fixed_graph" and name == "symmetric":
        bar = psi
    image = reality_exchange(P, Pinv, psi, bar)
    twice = reality_exchange(P, Pinv, *image)
    check("reality", f"{name} R_P squares to one on independent doubled fields",
          twice == (psi, bar), twice)
    check("reality", f"{name} graph bar=P K psi is exactly fixed",
          image == (psi, bar), image)

check("semantic", "fixed graph is declared from independent fields rather than a presumed dagger",
      "R_P(psi,bar) = (P^-1 K(bar), P K(psi))" in artifact
      and "does not write `bar=psi^dagger`" in artifact)


print("\nE. MINIMUM TYPED DATUM AND CLAIM CEILING")
minimum = {
    "X_D": {
        "source_slot": "declared printed Omega0/Omega1 cross-degree cell",
        "observed_type": "dual weak doublet",
        "Y": F(1, 2),
        "BL": F(0),
        "four_d_type": "opposite-Weyl Lorentz contraction",
        "horn_test": "P-transpose",
        "reality": "R_P covariance",
    },
    "X_R": {
        "source_slot": "declared source-admitted southeast rival cell",
        "net_cell_class_by_position": expected_se,
        "observed_type": "SM singlet",
        "Y": F(0),
        "BL_all_left": F(-2),
        "BL_physical": F(2),
        "four_d_type": "same-Weyl charge-conjugating contraction",
        "horn_test": "P-transpose",
        "reality": "R_P covariance",
    },
}
check("typing", "X_D minimum packet compensates weak/Y but not B-L",
      minimum["X_D"]["observed_type"] == "dual weak doublet"
      and minimum["X_D"]["Y"] == F(1, 2)
      and minimum["X_D"]["BL"] == 0)
check("typing", "X_R minimum packet keeps centre position and both charge conventions explicit",
      sorted(minimum["X_R"]["net_cell_class_by_position"].values()) == [0, 0, 2, 2]
      and minimum["X_R"]["BL_all_left"] == -2
      and minimum["X_R"]["BL_physical"] == 2)
slot_relabel = MUT == "slot_relabel"
check("semantic", "source zeta/nu are not relabelled as nu_L/nu_R",
      not slot_relabel and "zeta = nu_L,       nu = nu_R" in artifact
      and "do **not** say" in artifact)
mass_promotion = MUT == "mass_promotion"
check("ceiling", "local admissibility is not coefficient existence, global reality, mass, or seesaw",
      not mass_promotion
      and "not construct their owner or origin" in artifact
      and "**Not established:**" in artifact
      and "global reality condition or physical quotient" in artifact)
check("scope", "forbidden conventional/action/vacuum work is explicitly fenced",
      "Constructing" in artifact and "an action, vacuum, external selector, conventional scalar owner, or" in artifact
      and "phenomenology is off limits" in artifact)


RESULT = {
    "schema_version": "1.0",
    "run_id": "joe-directed-sn2",
    "branch": "SOURCE_NATIVE_CONDITIONAL_LOCAL_K77",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "neutral_lines": {
        "L": {"SU2": 2, "Y": "-1/2", "Q": "0", "B-L": "-1"},
        "N_c_all_left": {"SU2": 1, "Y": "0", "Q": "0", "B-L": "+1"},
        "nu_R_physical": {"B-L": "-1"},
    },
    "source_corners": {"rows": row_classes, "columns": col_classes},
    "southeast_net_classes": {f"{i},{j}": value for (i, j), value in se_net.items()},
    "pairing_horns": {
        "symmetric_anti_adjoint": "LOCAL_NONCHARACTERISTIC_FIXED_GRAPH",
        "skew_self_adjoint": "LOCAL_NONCHARACTERISTIC_FIXED_GRAPH",
    },
    "dirac": "NOT_EXCLUDED_AFTER_TYPED_SLOT_INCIDENCE__X_D_REQUIREMENT_ONLY__NOT_A_MASS",
    "right_majorana": "NOT_EXCLUDED_AFTER_TYPED_SLOT_INCIDENCE__X_R_REQUIREMENT_ONLY__NOT_A_MASS",
    "bars": "INDEPENDENT_IN_SOURCE__LOCAL_FIXED_GRAPH_ONLY_ON_DECLARED_R_P_HORN",
    "ceiling": "LOCAL_ALGEBRAIC_ADMISSIBILITY_ONLY__NO_ACTION_GLOBAL_DOMAIN_VACUUM_QUOTIENT_MASS_OR_PHYSICS",
}

print("\nSN2 RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))

if "--selftest" in sys.argv:
    mutants = (
        "source_independence",
        "centre_formula",
        "se_uniform",
        "charge_conjugate",
        "q_singlet",
        "horn_swap",
        "fixed_graph",
        "slot_relabel",
        "mass_promotion",
    )
    for mutant in mutants:
        env = dict(os.environ)
        env["SN2_MUTATION"] = mutant
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if completed.returncode == 0:
            raise SystemExit(f"SELFTEST FAILURE: mutant survived: {mutant}")
    print(f"SELFTEST PASS: {len(mutants)}/{len(mutants)} mutations rejected")

print("PASS: SN2 separates source cells, local reality, Grassmann parity, centre class, and observed neutral charges.")
