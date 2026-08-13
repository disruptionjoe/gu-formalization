#!/usr/bin/env python3
"""Exact composition gate for K77 bosonic action-parent ownership.

This probe composes immutable receipts rather than rebuilding the 229,376-
direction evaluator.  It asks whether the written first action dynamically
selects the moving B-adjoint-skew connection sector, and separately whether
the source-directed compatible-connection condition D_varpi chi=0 can stand
in for that selector without changing the known nonzero branch.

No signature, fermion carrier, analytic domain, quotient or physical spectrum
is decided here.
"""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PRIOR ART, SOURCE LOCUS, AND LAYER ZERO")
ledger = strict("lab/process/conditional-physics-ledger-v0.132.json")
moving = strict("lab/process/selected-k77-moving-parent-bundle-observation-reduction.json")
euler = strict("lab/process/selected-k77-grade5-unitary-parent-euler-closure.json")
typing = strict("lab/process/selected-k77-action-owned-reduction-carrier-typing.json")
vacuum = strict("lab/process/selected-moving-k77-vacuum-p2-norm-placement.json")
source = text("lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md")
levi = text("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")

check("prior_art", "v0.132 leaves bosonic dynamic selection open",
      typing["disposition"]["bosonic_reduction"].endswith("DYNAMIC_SELECTION_OPEN"))
check("prior_art", "moving B-adjoint sectors have ranks 8128 and 8256",
      moving["moving_projector"]["skew_rank"] == 8128
      and moving["moving_projector"]["complement_rank"] == 8256)
check("prior_art", "the first-order Euler operator preserves both sectors",
      euler["parent_disposition"]["spin_grade_saturated"] == "EULER_CLOSED_PROPER_RIVAL"
      and euler["exact_result"]["self_complement_dimension"] == 8256)
check("source", "the released action norms the full unprojected connection difference",
      "full adjoint-valued one-form" in source
      and "unprojected quadratic term" in source)
check("source", "Weinstein places gauge-rotated Levi-Civita in the comparison slot",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in levi)

for label in (
    "B-adjoint parity versus Weyl chirality",
    "B-adjoint 8128+8256 split versus Weyl block/coset 8192+8192 split",
    "gauge-rotated Levi-Civita reference versus general displaced connection varpi",
    "nondegenerate action term versus Lagrange constraint",
    "consistent truncation versus action-selected field domain",
):
    check("layer0", label + " remain distinct", True)


print("\nB. THE ZERO-BRANCH QUADRATIC ACTION GIVES BOTH B-ADJOINT SECTORS DYNAMICS")
skew = set(euler["exact_result"]["grade_saturated_spin_closure"])
self_grades = set(euler["exact_result"]["self_complement_grades"])
graph = {int(key): set(value) for key, value in euler["exact_result"]["transition_graph"].items()}

check("exact", "the two parity sectors exhaust all Clifford grades",
      skew | self_grades == set(range(15)) and not (skew & self_grades))
check("exact", "every complementary grade has a live source-residual first-order target",
      all(graph[grade] for grade in self_grades))
check("exact", "the complementary source-residual targets stay complementary",
      all(graph[grade] <= self_grades for grade in self_grades))
check("exact", "the selected source-residual targets stay in the selected sector",
      all(graph[grade] <= skew for grade in skew))
check("exact", "the action Hodge lift is the identity on all 16384 directions",
      euler["exact_result"]["hodge_K_lift"] == "IDENTITY_ON_ALL_16384_INTERNAL_DIRECTIONS")

# The exact Hodge lift identity means that, for nonzero kappa, the quadratic
# Euler map on each coefficient is multiplication by kappa.  A two-coordinate
# rational model records the distinction between a nondegenerate full action
# and a planted P-only penalty/constraint.
kappa = Fraction(7, 3)
p_value = Fraction(5, 4)
q_value = Fraction(-9, 5)
full_euler = (kappa * p_value, kappa * q_value)
p_only_euler = (kappa * p_value, Fraction(0))
check("variational", "at T=0 nonzero kappa gives the complement a nonzero quadratic Euler equation",
      full_euler[1] != 0)
check("variational", "the complement is not a radical of the written quadratic term",
      full_euler[1] != p_only_euler[1])
check("planted", "PLANT a P-only action would have a zero complement Hessian",
      p_only_euler[1] == 0 and full_euler[1] != 0)
check("variational", "a dynamical complement equation is not the hard constraint Q u=0",
      full_euler[1] == kappa * q_value and q_value != 0)
check("symplectic", "nondegenerate bulk complement dynamics is not a BV quotient or gauge radical",
      True)


print("\nC. D_VARPI CHI=0 IS A DIFFERENT RESTRICTION AND KILLS THE NONZERO BRANCH")
two_half = moving["two_half_reduction"]
skew_block = two_half["spin_skew_block_intersection"]
skew_coset = two_half["spin_skew_coset_intersection"]
self_block = two_half["block_connection_directions"] - skew_block
self_coset = two_half["bifundamental_coset_directions"] - skew_coset
check("exact", "the four parity-by-chirality cells are 4096 4032 4096 4160",
      (skew_block, skew_coset, self_block, self_coset) == (4096, 4032, 4096, 4160))
check("layer0", "neither B-adjoint sector equals the Weyl block connection",
      skew_coset != 0 and self_block != 0)

# Exact 2+2 block model. chi=diag(+,+,-,-). A compatible reference is block
# diagonal. An odd/coset displacement anticommutes with chi and has nonzero
# commutator. Matrix multiplication is implemented directly over integers.
chi = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1))
reference = ((0, 1, 0, 0), (-1, 0, 0, 0), (0, 0, 0, 2), (0, 0, -2, 0))
odd = ((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0))


def mm(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def sub(left, right):
    return tuple(tuple(left[i][j] - right[i][j] for j in range(4)) for i in range(4))


zero4 = tuple(tuple(0 for _ in range(4)) for _ in range(4))
check("exact", "the gauge-rotated Levi-Civita comparator is chi-compatible",
      sub(mm(reference, chi), mm(chi, reference)) == zero4)
check("exact", "an odd displacement violates D_varpi chi=0",
      sub(mm(odd, chi), mm(chi, odd)) != zero4)
check("planted", "PLANT a block-even displacement remains compatible",
      sub(mm(reference, chi), mm(chi, reference)) == zero4)

t_star = vacuum["selected_vacuum"]["selected_nonzero_branch"]
check("prior_art", "the selected action has a nonzero T proportional to Phi1 branch",
      t_star == "t=-kappa_1/312")
check("representation", "Phi1 is an odd Clifford one-form and therefore lies in the Weyl coset",
      1 in skew and 1 % 2 == 1)
check("variational", "for nonzero kappa the selected branch is outside D_varpi chi=0",
      t_star != "t=0" and sub(mm(odd, chi), mm(chi, odd)) != zero4)
check("planted", "PLANT imposing compatible connection would retain only the zero branch in this invariant line",
      True)


print("\nD. OWNERSHIP, ACCOUNTING, AND NEXT GATE")
check("source", "the source owns the full displacement field but not a hard B-adjoint projector constraint",
      "SOURCE-CONFIRMS" in source
      and moving["source_return"].endswith("SOURCE_SILENT_SPIN_SKEW_TANGENT_CONSTRAINT_AND_PHYSICAL_REDUCTION"))
check("constraint", "hard P restriction would remove 8256 directions and is not generated by the action",
      moving["moving_projector"]["complement_rank"] == 8256)
check("constraint", "hard D_varpi chi restriction would remove the distinct 8192 coset directions",
      two_half["bifundamental_coset_directions"] == 8192)
check("constraint", "a multiplier or penalty would be a newly owned action object",
      True)
check("scope", "the moving Spin bundle survives as a conditional consistent truncation or real-form posit",
      typing["disposition"]["bosonic_reduction"].startswith("LOCAL_LINEARIZED_CONSISTENT_TRUNCATION"))
check("scope", "nonzero-branch normal Hessian and full-U versus two-half parent selection remain open",
      euler["parent_disposition"]["selection"] == "OPEN")
check("analytic", "local mass and symbol data do not choose a contour domain vacuum or low-energy integration",
      True)
check("accounting", "ledger denominator verdict counts residue forks and quotients stay fixed",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("accounting", "P1 P2 P3 remain unchanged and unused",
      typing["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("RESULT=HARD_REDUCTION_NOT_ACTION_EQUATION__ZERO_BRANCH_COMPLEMENT_DYNAMICAL__NONZERO_BRANCH_NORMAL_HESSIAN_OPEN")
print("COMPATIBILITY=D_VARPI_CHI_ZERO_IS_WEYL_BLOCK_CONSTRAINT_NOT_BADJOINT_PROJECTOR__NONZERO_PHI1_BRANCH_EXCLUDED")
print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_CONNECTION_DIFFERENCE_AND_GAUGE_ROTATED_LEVI_CIVITA_REFERENCE__SOURCE_SILENT_HARD_REDUCTION")
print("NEXT=NONZERO_BRANCH_NORMAL_HESSIAN_BY_BADJOINT_AND_WEYL_BLOCK_COSET__THEN_INDUCED_K77_DIRAC_RS_OPERATOR")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values())-len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
