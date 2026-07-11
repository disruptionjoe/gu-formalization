"""GU attention priority: Condorcet ranking over the science-advisory council's five archetypes.

PURPOSE. This is the ranking ENGINE for the GU work card (JoeOps WI-068). Joe does not read the card; when
he has attention to give to GU, he wants a prioritized list of what to work on. That list is produced by a
Condorcet vote across the five council archetypes over the current hypothesis/next-move set
(explorations/science-advisory-council-full-picture-2026-07-11.md).

Condorcet is the PRIMARY ranking mode: item X outranks item Y if a MAJORITY of the five archetypes prefer X
to Y. When a strict Condorcet order exists it is used; when there is a cycle (Condorcet paradox) we fall back
to Copeland scores (count of pairwise wins minus losses), which always yields a full order and agrees with the
Condorcet winner when one exists. This makes ties and cycles explicit rather than hidden.

RE-RANKING AFTER A SWING (lightweight, per Joe's spec). After a significant swing toward one hypothesis:
  - if the swing RESOLVED it (cleared/killed): set its ballot rank to 'done' in every archetype (drop it), OR
    remove it from ITEMS; re-run.
  - if the swing STRENGTHENED/WEAKENED it: nudge its position up/down in the 1-2 archetypes whose stated
    values that swing served, and re-run. Do NOT re-elicit all five from scratch -- only move what moved.
The re-rank is just: edit BALLOTS below, run `python attention/gu_priority_condorcet.py`, paste the output
list onto the card. Cheap and reproducible by design.

Run: python attention/gu_priority_condorcet.py
"""
from __future__ import annotations

from itertools import combinations

# --- the candidate hypotheses / next moves (the council's decision set) ---
# RESOLVED in Wave 1 (2026-07-11), dropped from the live set:
#   H1 -> gravity CLEARS in the Bach branch (Bach tensor of exact Schwarzschild = 0 all orders; Kerr
#         Ricci-flat), REDUCED to the conformal-invariance datum. tests/wave1/H1_bach_flat_exact_vacua.py.
#   H3 -> DESI verified vs arXiv:2503.14738 (recall was correct; GU ~3-4 sigma on wa, a standing FALSIFIER);
#         the theta INT gravity over-determination WEAKENS under the corrected M^2/r^6 residual (f0 not
#         pinned by gravity). tests/wave1/H3_desi_verified_and_intersection.py.
# Both Wave-1 results point at the H-class / conformal reading -> H4 and H8 elevated below.
ITEMS = {
    # Wave 4: H18 RESOLVED -> II-class FORCED (structural grade) -> GRAVITY LEG CLEARS (conditional on P1/P2).
    # -> H16 (viability) becomes the top gravity bar; H21 (prove P1) is the hardening upgrade.
    "H16": "GRAVITY IS NOW THE VIABILITY QUESTION (H18 structurally cleared it -> Stelle R^X+Weyl^2 + DeWitt Lambda, BT-graded massive ghost m^2=+1/2>0). Is that branch actually physically VIABLE -- loop-level unitarity (BT prove tree only), the empirical scale of the massive ghost, the induced-R^X sign once ambient DeWitt R^Y is included (H15 Part E), the contested Mannheim program -- or a relocated problem in the Stelle-Mannheim corner? The real falsification bar. [orthodox/philosopher]",
    "H21": "Prove P1: s*(theta) = II_s OFF-SHELL, convention-fixed (ii-s-coordinate-formula sec 6.3 Codazzi / section-pullback). This is one of the two reconstruction-grade premises H18's II-class forcing rests on; proving it upgrades gravity from STRUCTURAL-clear to HARD-clear. The single hardening move. [heterodox]",
    "H19": "Search GU's base-pullback / observerse tautological structure for a term LINEAR in g carrying the timelike-norm sign -- the SOLE remaining decider of the (9,5)/(7,7) signature (conformal sector is structurally barred). Ties to the X4-architecture / Y14-capability-projection lens. [heterodox]",
    "H10": "Weak-field-with-MATTER / PPN test (light bending, perihelion): does GU-Stelle gravity pass the real solar-system bar? [orthodox/philosopher]",
    "H20": "Does the Clifford EVEN/ODD split organize the WHOLE |II|^2-on-Y14 action into gravity (even: R^X+Weyl^2+Lambda) + matter/source (odd: the Clifford-odd shiab, H18 Part 3) -- Weinstein's 'square and square-root / second-order = the square of the first-order'? The full-unification probe. [wild]",
    "H22": "Update the One Residual flagship (papers/candidates/one-residual-complete-picture) with the gravity-structurally-clears result: the complete picture -- gravity (Stelle+Lambda) + dark energy + SM (conjugate) + QM (Krein) + located count -- now assembled at existence/structural grade. Honest grades, conditional premises flagged. [commercial]",
    "H14": "Is the generation COUNT a conformal invariant under Bach/so(4,2)? (likely signature-blind too -- lowered). [wild]",
    "H6": "Ship the GU-independent family-puzzle paper ('forces odd count => nonzero 3-Sylow image'). Credible regardless of GU's fate.",
    "H7": "Match Weinstein's transcript RS '2+1 imposter' generation mechanism against our carrier A/B structure. [wild]",
    "H5": "Information-first / entropic-gravity antithesis (Bianconi +Lambda meets GU theta). Does NOT rise on Branch A (II-class); only would on Branch B.",
}

# --- five council ballots: strict preference order, best first ---
# GENERATIVE re-rank after Wave 4 (H18). Gravity structurally CLEARS (II-class forced). So the gravity
# question becomes VIABILITY (H16, now top bar) + HARDENING (H21, prove P1). New: H22 (assemble the complete
# picture, now that gravity clears) + H20 sharpened (Clifford even/odd = boson/fermion unification). H5 does
# NOT rise (Branch A). Philosopher's caution: "structural clear inheriting Stelle+massive-ghost" may be a
# contested corner -> weights H16 (the bar) high.
BALLOTS = {
    "orthodox":            ["H16", "H10", "H21", "H22", "H19", "H20", "H14", "H6", "H7", "H5"],
    "heterodox_rigorous":  ["H21", "H16", "H19", "H20", "H10", "H22", "H14", "H7", "H6", "H5"],
    "commercial":          ["H22", "H16", "H6", "H21", "H10", "H19", "H20", "H14", "H7", "H5"],
    "philosopher":         ["H16", "H10", "H21", "H5", "H19", "H22", "H20", "H14", "H6", "H7"],
    "wild_frontier":       ["H20", "H21", "H16", "H19", "H14", "H22", "H5", "H7", "H10", "H6"],
}


def prefers(ballot, x, y):
    return ballot.index(x) < ballot.index(y)


def pairwise_margin(items):
    """margin[(x,y)] = (# archetypes preferring x to y) - (# preferring y to x)."""
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


def main():
    items = list(ITEMS)
    margin = pairwise_margin(items)
    cw = condorcet_winner(items, margin)
    score = copeland(items, margin)
    # rank by Copeland, break ties by average ballot position (lower = better)
    def avg_pos(i):
        return sum(b.index(i) for b in BALLOTS.values()) / len(BALLOTS)
    order = sorted(items, key=lambda i: (-score[i], avg_pos(i)))

    print("=" * 78)
    print("GU ATTENTION PRIORITY  --  Condorcet over the 5-archetype council")
    print("=" * 78)
    print(f"Condorcet winner: {cw if cw else 'NONE (cycle) -> Copeland order below is authoritative'}\n")
    print("Prioritized list (what to hand Joe when he has GU attention):\n")
    for rank, i in enumerate(order, 1):
        print(f"  {rank}. [{i}]  Copeland {score[i]:+d}  (avg ballot pos {avg_pos(i):.1f})")
        print(f"       {ITEMS[i]}")
    print("\n" + "-" * 78)
    print("Per-archetype #1 picks:")
    for a, b in BALLOTS.items():
        print(f"  {a:20s} -> {b[0]}")
    # a couple of decisive pairwise checks for transparency
    print("\nKey pairwise margins (positive = row beats col across the 5 archetypes):")
    top = order[:4]
    hdr = "        " + "".join(f"{j:>6}" for j in top)
    print(hdr)
    for x in top:
        row = "".join(f"{margin[(x, y)]:+6d}" if x != y else "     ." for y in top)
        print(f"  {x:>5} {row}")
    return order


if __name__ == "__main__":
    main()
