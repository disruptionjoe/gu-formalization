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
    # H1/H4/H8/H9/H11 COLLAPSED (Wave 2 reflection) onto a single decidable fork -> H15.
    "H15": "THE GRAVITY FORK (collapses H1/H4/H8/H9/H11 + the OQ2-A functional + the ghost onto ONE decidable object): does GU's forced geometry (shiab, RS source, YM fiber) generate an Einstein-Hilbert scalar-curvature R term -> Stelle-type R+Weyl^2 (distinct massive ghost, Bateman-Turok-ready, ghost CLEARS) -- or leave gravity pure conformal Bach box^2 (degenerate coincident-pole, ghost parity non-canonical, ghost NOT cleanly solved)? H9 showed the whole gravity+ghost story reduces to this fork.",
    "H2": "Settle rep-canonicity (9,5) vs (7,7) = the OQ2-A H/II binary, via the J-commutant on the (6,4) DeWitt form. Decides forced-vs-located COUNT, conformal-nativeness, and c_W. Distinct from H15 (which is the gravity/ghost fork); this is the count-crux. Mildly coupled (the O(1,1) vs O(96,96) Krein distinction).",
    "H5": "Run the information-first / entropic-gravity antithesis against the confirmed conformal identification (Bianconi +Lambda meets GU theta). The un-run lens on the geometry-first primitive. Unaffected by Wave 2.",
    "H6": "Ship the GU-independent family-puzzle paper ('forces odd count => nonzero 3-Sylow image'). Credible regardless of GU's fate.",
    "H7": "Match Weinstein's transcript RS '2+1 imposter' generation mechanism (Spin(V+W) product rule) against our carrier A/B structure. Concrete, distinguishing.",
    "H10": "Weak-field-with-MATTER / PPN test (light bending, perihelion): vacuum-Schwarzschild-exists (H1) does NOT establish solar-system compatibility. Does GU gravity pass the real weak-field bar? [orthodox/philosopher]",
    "H14": "Is the generation COUNT a conformal invariant under the Bach/so(4,2) structure? Links the signature question to the conformal identification from the geometry side. [wild]",
    # --- NEW from the Wave-2 (H9) reflection (2026-07-11) ---
    "H16": "Is the 'good branch' (Stelle R+Weyl^2 + Bateman-Turok-graded massive ghost) actually physically VIABLE -- loop-level unitarity (BT prove tree only), empirical acceptability of the massive ghost, the contested Mannheim degenerate-case program -- or does it relocate the problem into a contested corner? The real falsification bar. [philosopher]",
    "H17": "Does GU's full O(96,96) Krein/fiber structure canonically SELECT the ghost parity at the degenerate Bach point (box^2), where the naive per-mode O(1,1) cannot (commutant jumps 2->4)? Would turn the box^2 degeneracy from a bug into the reason the fiber structure is needed. [wild]",
}

# --- five council ballots: strict preference order, best first ---
# GENERATIVE re-rank after Wave 2 (H9). The council reflected and found H1/H4/H8/H9/H11 COLLAPSE onto one
# fork (H15: pure Bach box^2 vs Stelle R+Weyl^2), and drafted H16 (viability bar) + H17 (does the O(96,96)
# fiber fix the degeneracy). H15 is the decisive gate that settles ~5 prior items at once.
BALLOTS = {
    "orthodox":            ["H15", "H16", "H10", "H2", "H17", "H14", "H6", "H7", "H5"],
    "heterodox_rigorous":  ["H15", "H2", "H17", "H16", "H14", "H10", "H7", "H6", "H5"],
    "commercial":          ["H15", "H16", "H6", "H2", "H10", "H17", "H14", "H7", "H5"],
    "philosopher":         ["H16", "H15", "H10", "H5", "H2", "H17", "H14", "H6", "H7"],
    "wild_frontier":       ["H17", "H15", "H2", "H14", "H16", "H5", "H7", "H10", "H6"],
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
