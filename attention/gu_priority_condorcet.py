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
    # Wave 5: H21 PROVEN (s*(theta)=II_s off-shell, fork does NOT re-open) + H16 CONTESTED-CORNER (antigravity
    # kill retired). BOTH collapse gravity's residual onto ONE object: A = spin-lift(grad^gimmel) = the source
    # action. Gravity is HARD-clear MODULO that object. -> H23 (attempt it) + H24 (the R^Y firm-up).
    # H23 RESOLVED (Wave 8) -> PARTIAL: the spin-lift is canonical AS A MAP + the Krein [P,S]=0 holds (ghost
    # clears structurally); but the SOLDERING (pinning theta to the spin-lift image, codim-8165) is NOT forced
    # -- a single honest postulate. Gauge group sharpened to NON-COMPACT Sp(32,32;H). Gravity = a CONDITIONAL
    # THEOREM (tree-level Stelle-clear, positive decoupled ghost) modulo {the soldering postulate + mu_DW}.
    "H27": "The SOLDERING CARRIER -- the single move that upgrades gravity PARTIAL -> UNCONDITIONAL. Does a first-order/Palatini variation of S=|theta|^2 drive the connection pi onto the metric-compatible spin-lift on-shell, WITHOUT collapsing to the acausal theta=0 (DEAD-ENDS)? H23 proved the spin-lift is canonical as a map and the ghost clears; this is the one remaining bosonic gravity object. Second: mu_DW. [heterodox/wild]",
    "H26": "Does the Krein ghost-parity [P,S]=0 (H23 showed it HOLDS structurally, Bateman-Turok positivity) survive RENORMALIZATION (loop-level unitarity)? The hard generic-Stelle-shared frontier; needs the source-action dynamics. Narrowed by H23 (structural version confirmed). [philosopher]",
    "H22": "Assemble/update the One Residual flagship with the Wave 1-5 results: gravity HARD-clears modulo one object (Stelle R^X+Weyl^2 + DeWitt Lambda, antigravity kill retired, ghost BT-cleared at tree) + dark energy (DESI ~3-4 sigma honest tension) + SM (conjugate) + QM (Krein) + located count. The complete picture at structural/existence grade, all conditional premises flagged. [commercial]",
    "H10": "Weak-field-with-MATTER / PPN test (light bending, perihelion): does GU-Stelle pass the real solar-system bar? [orthodox/philosopher]",
    "H19": "Search GU's base-pullback / observerse tautological structure for a term LINEAR in g -- the SOLE remaining decider of the (9,5)/(7,7) signature. Ties to the X4/Y14 architecture-vs-capability lens. [heterodox]",
    "H14": "Is the generation COUNT a conformal invariant under Bach/so(4,2)? (likely signature-blind -- lowered). [wild]",
    "H6": "Ship the GU-independent family-puzzle paper ('forces odd count => nonzero 3-Sylow image'). Credible regardless of GU's fate.",
    "H7": "Match Weinstein's RS '2+1 imposter' generation mechanism against our carrier A/B structure. [wild]",
    "H5": "Information-first / entropic-gravity antithesis. Does NOT rise (Branch A / II-class confirmed).",
}

# --- five council ballots: strict preference order, best first ---
# GENERATIVE re-rank after Wave 7 (H25). Gravity's geometry leg CLEARS at tree level (H25: C_RY>0, sign
# confirmed by two methods, KILL excluded by sign). No new hypotheses -- H25 closed the last geometry gate.
# Remaining gravity gates (mu_DW, loop [P,S]=0, normalization) collapse onto the source action -> back at the
# construct-vs-ship fork (H23 vs H22), now with gravity's geometry fully cleared -> H22 (ship the strong
# picture) rises for commercial/philosopher; H23 (construct) holds heterodox/wild/orthodox. Expect a close
# 3-2 split -> a genuine Joe decision point.
BALLOTS = {
    "orthodox":            ["H22", "H27", "H10", "H19", "H26", "H14", "H6", "H7", "H5"],
    "heterodox_rigorous":  ["H27", "H22", "H19", "H26", "H10", "H14", "H7", "H6", "H5"],
    "commercial":          ["H22", "H6", "H27", "H10", "H19", "H26", "H14", "H7", "H5"],
    "philosopher":         ["H22", "H27", "H10", "H26", "H5", "H19", "H14", "H6", "H7"],
    "wild_frontier":       ["H27", "H22", "H19", "H14", "H26", "H5", "H7", "H10", "H6"],
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
