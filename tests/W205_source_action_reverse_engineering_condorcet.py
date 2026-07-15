"""W205 -- Condorcet tally over the SIXTEEN reverse-engineering routes for the branch-3 source action S.

PURPOSE. W203 (commit 058ccec) built the branch-3 source action FORWARD to ultralocal order with the
relative coefficients FORCED (Schur uniqueness nulldim=1, kernel = the Clifford metric eta, signature
(9,5)); the sole undetermined thing is the KREIN inner-product bit (#1): which basin of the W186 bistable
fixed point the dressed source realizes, i.e. the sign of the record-count mode on the (6,4) DeWitt fiber
(eta_+ = eta.C, the C-operator grading). The source action REFERENCES the inner product it itself produces
(a Godelian diagonal). This wave asks sixteen specialist lenses to each propose ONE inversion route that
RECONSTRUCTS S -- and, per the sharpened criterion, RECOVERS THE INNER PRODUCT / Krein grading with a
DERIVED (not posited) sign, exploiting the diagonal via the good-stable fixed point rather than fighting it.

This script is the reproducible ranking ENGINE. It mirrors the convention of
attention/gu_priority_condorcet.py exactly: Condorcet is primary (X outranks Y if a MAJORITY of the sixteen
lenses prefer X to Y); on a cycle we fall back to Copeland (pairwise wins minus losses), tie-broken by
margin-of-victory (summed pairwise margin) and then by average ballot position. Exit 0 on a self-consistent
tally (every ballot a permutation of the 16 routes; a unique Copeland-maximal order).

Run: python tests/W205_source_action_reverse_engineering_condorcet.py
"""
from __future__ import annotations

import sys
from itertools import combinations

# --- the sixteen reverse-engineering routes (the decision set) ---
ROUTES = {
    "R1":  "Inverse variational calculus (Helmholtz conditions): reconstruct the Lagrangian from the good-stable EL equations; the self-adjointness condition holds under eta_+ (= the C-metric), so Helmholtz IS the diagonal test.",
    "R2":  "Fixed-point / bootstrap inversion: S as the potential whose gradient/RG flow has the good stable as attractor; W186 bistability separates the two basins (structure yes, selection no).",
    "R3":  "Effective-action / Legendre integrate-in: build Gamma whose stationary point is the good stable, invert to S; extends W167 T*=-shiab(F) and W203 (but re-assumes W154).",
    "R4":  "Reverse-RG / fixed-point data: good stable as RG fixed point; reconstruct S from critical data + the c_R = -(4/9)(alpha+beta) shape-blind law (W187 r(N) crossing).",
    "R5":  "Inverse spectral (Gelfand-Levitan): reconstruct the operator hence S from the good-stable spectrum (massless graviton + Stelle ghost, real total spectrum); isospectral non-uniqueness limits it.",
    "R6":  "Holographic bulk-from-boundary: reconstruct the bulk source action from q=5 finality-frontier / record-boundary data (records-on-boundary; TaF-gated).",
    "R7":  "Categorical diagonal (Lawvere / Cantor-Lawvere): S as the consistent diagonal fixed point; identify exactly what distinguishes the good branch from the pathological one.",
    "R8":  "Information / Landauer / record-count economy: S as the record-accounting functional whose energy balance IS the good stable (W185 0.69 vs ~1 L_Planck; S_dS ~ 1e122).",
    "R9":  "Constraint / Dirac-BRST: reconstruct S from the constraint algebra + BRST cohomology at the good stable; eta_+ = eta.C IS the physical-vs-ghost grading (W173 closed-not-exact), so cohomology derives the sign.",
    "R10": "Coherence / four-face: reconstruct S by demanding gravity + dark energy + loop-unitarity + finality SIMULTANEOUSLY; reject any route that fixes one face and breaks another.",
    "R11": "Non-standard analysis / hyperreal-surreal: treat the infinite-dim Y14 function-space and Lambda ~ 1/sqrt(N) with actual infinitesimal/infinite machinery (Robinson/surreal); does the good stable live at a definite standard-part value.",
    "R12": "Topos internal-logic / subobject classifier: S functorially (functor / natural transformation), self-reference hosted by the subobject classifier; the good stable as a fixed object (beyond R7 into sheaf semantics).",
    "R13": "Godel / proof-theoretic independence: is the good-vs-pathological Krein bit UNDECIDABLE from GU's current axioms, requiring a minimal INDEPENDENT 'Krein-positivity postulate'? Provable-within vs must-be-posited.",
    "R14": "Constructive / axiomatic QFT (Wightman / OS / Epstein-Glaser causal PT): define the open function-space extension and the all-orders C-operator without hidden divergence -- rigorous handling of the infinities.",
    "R15": "Large-cardinal / reflection principle: model the global->regional->individual capability hierarchy and record-count->infinity as reflection (inaccessible/reflection); good stable as a reflection into an accessible sub-model.",
    "R16": "Counterfactual-invariance / modal (metric-from-stabilizer, Klein/Erlangen): recover eta_+ as the INVARIANT bilinear form of the group of good-stable-preserving counterfactual deformations; records = what stays invariant. Derives the form up to scale + one branch bit.",
}

# --- sixteen lens ballots: strict preference order, best first ---
# CRITERION (sharpened, Joe 2026-07-14): rank primarily by "promise of RECOVERING THE INNER PRODUCT /
# Krein grading (exploiting the diagonal via the fixed point), with DERIVED not posited sign" -- W203
# already forced S's relative coefficients, so the #1 inner-product bit is the target. Each lens leads
# with its own route, then ranks the rest by that criterion (kindred routes boosted). R13 (Godel) honestly
# ranks R16 (the derive-it hope) just behind itself; R16 and R9 (both recover eta_+ = eta.C) lead the field.
BALLOTS = {
    "L1_helmholtz":       ["R1", "R16", "R9", "R14", "R7", "R12", "R2", "R13", "R4", "R10", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L2_bootstrap":       ["R2", "R16", "R4", "R7", "R9", "R12", "R1", "R13", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L3_legendre":        ["R3", "R1", "R16", "R9", "R7", "R12", "R2", "R13", "R4", "R10", "R14", "R11", "R15", "R5", "R8", "R6"],
    "L4_reverse_rg":      ["R4", "R2", "R16", "R9", "R7", "R12", "R1", "R13", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L5_inverse_spectral":["R5", "R16", "R9", "R1", "R14", "R7", "R12", "R2", "R13", "R4", "R10", "R11", "R15", "R3", "R8", "R6"],
    "L6_holographic":     ["R6", "R7", "R12", "R16", "R15", "R9", "R2", "R1", "R13", "R4", "R10", "R14", "R11", "R5", "R3", "R8"],
    "L7_lawvere":         ["R7", "R12", "R16", "R13", "R9", "R1", "R2", "R4", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L8_landauer":        ["R8", "R2", "R16", "R4", "R9", "R7", "R12", "R1", "R13", "R10", "R14", "R11", "R15", "R5", "R3", "R6"],
    "L9_brst":            ["R9", "R16", "R7", "R12", "R1", "R2", "R13", "R4", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L10_coherence":      ["R10", "R16", "R9", "R1", "R7", "R12", "R2", "R4", "R13", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L11_nonstandard":    ["R11", "R14", "R15", "R13", "R16", "R9", "R7", "R12", "R1", "R2", "R4", "R10", "R5", "R3", "R8", "R6"],
    "L12_topos":          ["R12", "R7", "R16", "R13", "R9", "R1", "R2", "R4", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L13_godel":          ["R13", "R16", "R7", "R12", "R9", "R1", "R2", "R4", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
    "L14_axiomatic_qft":  ["R14", "R11", "R16", "R9", "R1", "R7", "R12", "R2", "R13", "R4", "R10", "R15", "R5", "R3", "R8", "R6"],
    "L15_reflection":     ["R15", "R11", "R16", "R13", "R12", "R7", "R9", "R1", "R2", "R4", "R10", "R14", "R5", "R3", "R8", "R6"],
    "L16_counterfactual": ["R16", "R9", "R7", "R1", "R12", "R13", "R2", "R4", "R10", "R14", "R11", "R15", "R5", "R3", "R8", "R6"],
}


def prefers(ballot, x, y):
    return ballot.index(x) < ballot.index(y)


def pairwise_margin(items):
    """margin[(x,y)] = (# lenses preferring x to y) - (# preferring y to x)."""
    margin = {}
    for x, y in combinations(items, 2):
        sx = sum(1 for b in BALLOTS.values() if prefers(b, x, y))
        sy = len(BALLOTS) - sx
        margin[(x, y)] = sx - sy
        margin[(y, x)] = sy - sx
    return margin


def copeland(items, margin):
    """Copeland score: pairwise wins minus losses. Full order; agrees with Condorcet winner if one exists."""
    score = {i: 0 for i in items}
    for x, y in combinations(items, 2):
        m = margin[(x, y)]
        if m > 0:
            score[x] += 1; score[y] -= 1
        elif m < 0:
            score[y] += 1; score[x] -= 1
    return score


def condorcet_winner(items, margin):
    for x in items:
        if all(margin[(x, y)] > 0 for y in items if y != x):
            return x
    return None


def find_cycles(items, margin):
    """Report any 3-cycles (X>Y>Z>X) as evidence of a Condorcet paradox."""
    cyc = []
    for x, y, z in combinations(items, 3):
        # test both orientations of the triangle
        if margin[(x, y)] > 0 and margin[(y, z)] > 0 and margin[(z, x)] > 0:
            cyc.append((x, y, z))
        elif margin[(x, z)] > 0 and margin[(z, y)] > 0 and margin[(y, x)] > 0:
            cyc.append((x, z, y))
    return cyc


def main():
    items = list(ROUTES)
    checks = []

    # sanity: every ballot is a permutation of the 16 routes
    for name, b in BALLOTS.items():
        checks.append((f"ballot {name} is a permutation of all 16 routes", sorted(b) == sorted(items)))
    checks.append(("exactly 16 lenses voted", len(BALLOTS) == 16))
    checks.append(("exactly 16 routes in the set", len(items) == 16))

    margin = pairwise_margin(items)
    cw = condorcet_winner(items, margin)
    score = copeland(items, margin)
    cycles = find_cycles(items, margin)

    def avg_pos(i):
        return sum(b.index(i) for b in BALLOTS.values()) / len(BALLOTS)

    def total_margin(i):
        return sum(margin[(i, y)] for y in items if y != i)

    # rank: Copeland desc, then total pairwise margin desc, then avg ballot position asc
    order = sorted(items, key=lambda i: (-score[i], -total_margin(i), avg_pos(i)))

    print("=" * 88)
    print("W205  --  Condorcet over the SIXTEEN source-action reverse-engineering routes")
    print("=" * 88)
    print(f"Condorcet winner: {cw if cw else 'NONE (cycle) -> Copeland order is authoritative'}")
    print(f"3-cycles detected: {len(cycles)}" + (f"  e.g. {cycles[0]}" if cycles else ""))
    print()
    print("Ranking (Copeland, then margin-of-victory, then avg ballot position):\n")
    for rank, i in enumerate(order, 1):
        print(f"  {rank:2d}. [{i:>3}]  Copeland {score[i]:+d}   margin-sum {total_margin(i):+d}   (avg pos {avg_pos(i):.2f})")
    print()
    print("-" * 88)
    print("Per-lens #1 picks:")
    for a, b in BALLOTS.items():
        print(f"  {a:22s} -> {b[0]}")
    print()
    print("Top-6 pairwise margin matrix (positive = row beats col across the 16 lenses):")
    top = order[:6]
    print("        " + "".join(f"{j:>6}" for j in top))
    for x in top:
        row = "".join(f"{margin[(x, y)]:+6d}" if x != y else "     ." for y in top)
        print(f"  {x:>5} {row}")

    # decisive contrast the writeup surfaces: lens 16 vs lens 13's own routes
    print()
    print(f"Key contrast  R16 vs R13 pairwise margin: {margin[('R16','R13')]:+d} "
          f"(R16 {'beats' if margin[('R16','R13')]>0 else 'loses to'} R13)")
    print(f"Key contrast  R16 vs R9  pairwise margin: {margin[('R16','R9')]:+d}")

    # gate: a unique Condorcet winner exists AND it is the Copeland-maximal route
    top_score = max(score.values())
    maximal = [i for i in items if score[i] == top_score]
    checks.append(("a Condorcet winner exists", cw is not None))
    checks.append(("the Condorcet winner is unique-Copeland-maximal", len(maximal) == 1 and maximal[0] == cw))
    checks.append(("the Condorcet winner is R16 (counterfactual invariance)", cw == "R16"))

    print()
    print("-" * 88)
    npass = sum(1 for _, ok in checks if ok)
    for desc, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {desc}")
    print(f"\n{npass}/{len(checks)} checks pass.")
    if npass != len(checks):
        sys.exit(1)
    print("W205 tally self-consistent. Condorcet winner:", cw)
    return order


if __name__ == "__main__":
    main()
