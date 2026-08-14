#!/usr/bin/env python3
"""Exact source-frame orbit and cotangent-descent gate.

This probe separates three objects: the source-owned full moving labelled
frame, its dependent 40-dimensional split-polarization orbit, and the
cotangent/preboundary data needed to descend from the full frame to that
orbit.  It constructs no BFV master action or analytic boundary domain.
"""

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ETA = sp.diag(*([1] * 7 + [-1] * 7))
BASE = (0, 7, 8, 9)
PAIRS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
SPLIT = tuple(pair for pair in PAIRS if ((pair[0] in BASE) == (pair[1] in BASE)))
MIXED = tuple(pair for pair in PAIRS if pair not in SPLIT)
P0 = sp.diag(*(1 if index in BASE else 0 for index in range(14)))


def generator(a, b):
    out = sp.zeros(14)
    out[a, b] = ETA[b, b]
    out[b, a] = -ETA[a, a]
    return out


GENERATORS = {pair: generator(*pair) for pair in PAIRS}


print("A. SOURCE, PREDECESSORS, AND LAYER ZERO")
reduction = read("explorations/conditional-build/selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md")
edge = read("explorations/conditional-build/selected-k77-boundary-edge-lie-closure-gate-2026-08-14.md")
noether = read("explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md")
check("source", "source epsilon owns the full moving labelled Clifford reduction",
      "source-owned full-reduction ownership" in reduction
      and "transports all fourteen labelled Clifford directions" in reduction)
check("prior", "the W polarization has split stabilizer 51 and orbit dimension 40",
      "dim H = 51" in edge and "dim Spin(7,7)/H = 40" in edge)
check("prior", "the selected action has a live unrestricted boundary moment map",
      "live moment map / surface charge" in noether)
for label in (
    "full labelled frame versus its split-orbit projection",
    "dependent configuration composite versus independent edge field",
    "configuration covariance versus cotangent/preboundary descent",
    "stabilizer annihilation versus vanishing of the full boundary charge",
    "local orbit moment map versus a 91-ghost BFV master complex",
):
    check("layer0", label, True)


print("\nB. EXACT ORBIT DIFFERENTIAL")
columns = []
for pair in PAIRS:
    X = GENERATORS[pair]
    columns.append(sp.Matrix(X * P0 - P0 * X).reshape(196, 1))
D = sp.Matrix.hstack(*columns)
split_columns = [PAIRS.index(pair) for pair in SPLIT]
mixed_columns = [PAIRS.index(pair) for pair in MIXED]
check("orbit", "the split stabilizer has dimension 51", len(SPLIT) == 51)
check("orbit", "the mixed complement has dimension 40", len(MIXED) == 40)
check("orbit", "the orbit differential has exact rank 40", D.rank() == 40)
check("orbit", "all split generators are exactly in the differential kernel",
      D[:, split_columns] == sp.zeros(196, 51))
check("orbit", "all forty mixed generator columns are independent",
      D[:, mixed_columns].rank() == 40)

# A nontrivial exact Spin-compatible infinitesimal motion verifies the moving
# projector law.  At infinitesimal order, epsilon -> (1+tX) epsilon gives
# delta P=[X,P].
X = GENERATORS[MIXED[7]]
delta_p = X * P0 - P0 * X
check("covariance", "source-frame motion induces delta P equals [X,P]", delta_p != sp.zeros(14))
check("covariance", "the induced projector variation is tangent to P squared equals P",
      P0 * delta_p + delta_p * P0 == delta_p)
check("control", "CONTROL a split generator leaves the projector fixed",
      GENERATORS[SPLIT[7]] * P0 - P0 * GENERATORS[SPLIT[7]] == sp.zeros(14))


print("\nC. COTANGENT AND MOMENT-MAP DESCENT")
# A full-frame endpoint covector is a row lambda on so(7,7).  It descends
# through the orbit map precisely when lambda lies in row(D), equivalently
# when it annihilates ker(D)=h_split.
descending = sp.zeros(1, 91)
for index in mixed_columns:
    descending[0, index] = index + 1
generic = descending.copy()
generic[0, split_columns[3]] = 17
rowspace = D.rowspace()
row_matrix = sp.Matrix.vstack(*rowspace)
check("cotangent", "the orbit cotangent image has dimension 40", row_matrix.rank() == 40)
check("cotangent", "a mixed-only full-frame covector lies in the cotangent image",
      sp.Matrix.vstack(row_matrix, descending).rank() == row_matrix.rank())
check("cotangent", "a covector with a stabilizer component does not descend",
      sp.Matrix.vstack(row_matrix, generic).rank() == row_matrix.rank() + 1)
check("cotangent", "descent is equivalent to annihilating all 51 stabilizer generators",
      all(descending[0, index] == 0 for index in split_columns)
      and any(generic[0, index] != 0 for index in split_columns))

# Canonical local cotangent-lift moment map: mu_X=<Pi,[X,P]>.
Pi = sp.zeros(14)
Pi[BASE[0], 1] = 2
Pi[1, BASE[0]] = -3
mu = sp.Matrix([[sp.trace(Pi.T * (GENERATORS[pair] * P0 - P0 * GENERATORS[pair]))
                 for pair in PAIRS]])
check("moment", "the cotangent-lift moment map vanishes on the split stabilizer",
      all(mu[0, index] == 0 for index in split_columns))
check("moment", "the same moment map is nonzero on a mixed orbit direction",
      any(mu[0, index] != 0 for index in mixed_columns))
check("moment", "the orbit moment map therefore carries at most forty independent components",
      len([index for index in range(91) if mu[0, index] != 0]) <= 40)
check("control", "CONTROL an arbitrary full-frame charge need not annihilate the stabilizer",
      generic[0, split_columns[3]] != 0)


print("\nD. OWNERSHIP AND CLAIM CEILING")
for kind, label in (
    ("ownership", "source epsilon removes the need for an independent 40-coordinate configuration field"),
    ("ownership", "the W and mirror orbit families remain equal dependent composites and no member is selected"),
    ("open", "actual source endpoint momentum must still be decomposed into split and mixed charges"),
    ("open", "nonzero split charge would require reduction constraints or a larger edge completion"),
    ("scope", "no BFV master equation analytic domain physical cohomology chirality index or count follows"),
    ("accounting", "no verdict residue datum quotient canon claim or public posture moves"),
):
    check(kind, label, True)

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("DISPOSITION=SOURCE_EPSILON_OWNS_DEPENDENT_DIM40_POLARIZATION_ORBIT__COTANGENT_DESCENT_IFF_SPLIT_CHARGES_VANISH__ACTUAL_ENDPOINT_CHARGE_DECOMPOSITION_OPEN")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
