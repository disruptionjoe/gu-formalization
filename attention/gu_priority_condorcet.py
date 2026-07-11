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
    "H2": "Settle rep-canonicity (9,5) vs (7,7) = the OQ2-A H/II binary, via the J-commutant on the (6,4) DeWitt form. Decides forced-vs-located count, conformal-nativeness, and c_W. THE count-crux.",
    "H4": "Full higher-codimension Willmore first variation (Simons + normal-bundle, background-subtracted). GATES THE GRAVITY CLEAR (H1): does GU's functional equal Bach on all sectors / annihilate the trace mode? Also signs the O(M^0) Lambda, settles the H/II binary.",
    "H5": "Run the information-first / entropic-gravity antithesis against the confirmed conformal identification (Bianconi +Lambda meets GU theta). The un-run lens on the geometry-first primitive.",
    "H6": "Ship the GU-independent family-puzzle paper ('forces odd count => nonzero 3-Sylow image'). Credible regardless of GU's fate.",
    "H7": "Match Weinstein's transcript RS '2+1 imposter' generation mechanism (Spin(V+W) product rule) against our carrier A/B structure. Concrete, distinguishing.",
    "H8": "Is GU just Bach? Check whether Weyl^2/Bach + fiber/gauge IS the S_IG spec. H1 showed Bach gravity passes the exact-vacuum gate, so 'GU = a known conformal theory' is live and could moot the source-action buildbench.",
    # --- NEW hypotheses drafted by the council's Wave-1 reflection (2026-07-11) ---
    "H9": "Ghost audit of the H-class/Bach sector -- SHARPENED: a ghost-free 4-derivative completion EXISTS and is published (Bateman-Turok 'Escape from Ostrogradsky via Hidden Ghost Parity', arXiv:2607.00096; ghosts graded on a Krein space), and GU's own Krein form IS that ghost parity (canon/ghost-parity-krein-synthesis.md, implements the so(9,5) Cartan involution). So H9 is NOT 'does a completion exist' but 'does GU's Bach action INSTANTIATE Bateman-Turok': is [P_ghost, S]=0 for the H-class action? Decisive; the Krein structure we compute everywhere is the candidate mechanism. [orthodox/commercial]",
    "H10": "Weak-field-with-MATTER / PPN test (light bending, perihelion): vacuum-Schwarzschild-exists (H1) does NOT establish solar-system compatibility. Does GU-Bach pass the real weak-field bar? [orthodox/philosopher]",
    "H11": "Structural unification test: are {H4 conformal-invariant functional, H8 GU=Bach, H2 (6,4)-signature} actually ONE datum? If so the gravity+count story closes or falls together. [heterodox]",
    "H14": "Is the generation COUNT a conformal invariant under the Bach/so(4,2) structure? The count-side of H11 -- links the signature question to the conformal identification from the geometry side. [wild]",
}

# --- five council ballots: strict preference order, best first ---
# GENERATIVE re-rank after Wave 1: the council first reflected (3 questions) and DRAFTED new hypotheses
# (H9,H10,H11,H14), THEN voted over the enlarged set. The Wave-1 lesson (gravity is Bach-class, clears the
# vacuum gate conditional on the conformal-invariant functional) pushes the REAL physical bars (ghost H9,
# PPN H10) and the unification/functional questions (H4,H8,H11) up; "vacuum-clear may not be the right bar"
# (philosopher) weights H9/H10 heavily.
BALLOTS = {
    "orthodox":            ["H9", "H10", "H8", "H4", "H2", "H6", "H11", "H14", "H7", "H5"],
    "heterodox_rigorous":  ["H11", "H2", "H4", "H8", "H14", "H9", "H10", "H7", "H6", "H5"],
    "commercial":          ["H8", "H9", "H4", "H6", "H10", "H2", "H11", "H14", "H7", "H5"],
    "philosopher":         ["H9", "H10", "H4", "H5", "H8", "H2", "H11", "H14", "H6", "H7"],
    "wild_frontier":       ["H14", "H11", "H2", "H4", "H8", "H5", "H9", "H7", "H10", "H6"],
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
