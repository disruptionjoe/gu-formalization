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
ITEMS = {
    "H1": "Run ELProjectedGRShadowTheorem in the conformal/Bach branch (Bach admits exact Schwarzschild -> likely clears the gravity wall). Cheap, decisive.",
    "H2": "Settle rep-canonicity (9,5) vs (7,7) = the OQ2-A H/II binary, via the J-commutant on the (6,4) DeWitt form. Decides forced-vs-located count, conformal-nativeness, and c_W. THE crux.",
    "H3": "Verify DESI (w0,wa) vs arXiv:2503.14738 Table 3, then re-run the theta INT gravity intersection test with the corrected Willmore residual. Turns the ~3-4 sigma tension into a falsifiable prediction.",
    "H4": "Full higher-codimension Willmore first variation (Simons + normal-bundle, background-subtracted). Settles the H/II binary, signs the O(M^0) Lambda candidate, tests the conformal-invariance question. No new object.",
    "H5": "Run the information-first / entropic-gravity antithesis against the confirmed conformal identification (Bianconi +Lambda meets GU theta). The un-run lens on the geometry-first primitive.",
    "H6": "Ship the GU-independent family-puzzle paper ('forces odd count => nonzero 3-Sylow image'). Credible regardless of GU's fate.",
    "H7": "Match Weinstein's transcript RS '2+1 imposter' generation mechanism (Spin(V+W) product rule) against our carrier A/B structure. Concrete, distinguishing.",
    "H8": "Check whether Weyl^2/Bach + the fiber/gauge terms IS the S_IG spec -- i.e. is the source-action buildbench solving a non-problem now that H-class GU may be a KNOWN theory?",
}

# --- five council ballots: each is a strict preference order, best first ---
# (derived from each archetype's stated values in the council doc; see that doc for the reasoning)
BALLOTS = {
    "orthodox":            ["H3", "H1", "H8", "H4", "H6", "H2", "H7", "H5"],
    "heterodox_rigorous":  ["H2", "H4", "H8", "H1", "H7", "H3", "H6", "H5"],
    "commercial":          ["H1", "H3", "H6", "H8", "H2", "H4", "H7", "H5"],
    "philosopher":         ["H1", "H3", "H5", "H2", "H4", "H8", "H6", "H7"],
    "wild_frontier":       ["H2", "H7", "H4", "H8", "H5", "H1", "H3", "H6"],
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
