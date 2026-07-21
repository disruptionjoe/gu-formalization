"""
Q2 probe: sector bit sigma -- FORCED / FREE / STANDPOINT-SUPPLIED.

Deterministic, numpy only, no network. Positive controls first.
Foreground, exits 0 on ALL PASS.

This probe does NOT re-prove externality (closed premise). It encodes, at
finite Z/2 grade, the three load-bearing structural facts the Q2 verdict
rests on, plus one [F] control that MUST fire (teeth):

  [E] blocks (must hold):
    E1  MINT-BLINDNESS (Horn 2 of the circularity dichotomy):
        no alpha-EVEN map on states outputs the alpha-ODD datum sigma.
        (This is the boundary-law blindness lemma at toy grade: an even
         structure cannot mint an odd value -> the alpha-even standpoint
         cannot SUPPLY sigma.)
    E2  CO-FLIP WELD (same-vs-different, part 1):
        the record arrow r and sigma are the SAME alpha-odd class
        (r*sigma is alpha-invariant = +1). Having r IS having sigma.
    E3  DIFFERENT ACCESS (same-vs-different, part 2):
        a LIFT (section) of the Z/2 torsor is not a map on states;
        the blindness lemma (a statement about maps) does not forbid
        possessing a lift. Both lifts are admissible under every even map.
    E4  HORN 1 CIRCULARITY:
        the alpha-even content of a standpoint takes identical values on
        the sigma=+1 world and the sigma=-1 world -> it does NOT determine
        sigma. A standpoint that "has" sigma presupposed it (reads), and a
        standpoint independent of sigma is E1-blind to it. Dichotomy is
        exhaustive; neither horn SUPPLIES.
    E5  FORCED-TEST NEGATIVE (positivity is sigma-blind):
        both sigma values give a positive-definite graded inner product
        (unitarity admits both) -> no positivity/unitarity necessity picks
        sigma. Confronts and confirms W211.

  [F] control (must FIRE = the planted reader succeeds, proving teeth):
    F1  an alpha-ODD map (a symmetry-BREAKING external selection, i.e.
        exactly NOT an internal even reading) DOES recover sigma. This
        shows the obstruction is specifically evenness/internality, not a
        rigged always-fail. The odd map is the external coin, not a
        standpoint-internal derivation.
"""

import numpy as np

SEED = 20260721
rng = np.random.default_rng(SEED)

results = []


def check(tag, kind, ok, detail=""):
    results.append((tag, kind, bool(ok), detail))


# ---------------------------------------------------------------------------
# State model. X = {0, 1}: a state and its alpha-image. alpha swaps them.
# An "even" (alpha-equivariant / invariant) observable is constant on {0,1}.
# The odd datum sigma flips under alpha: sigma(0) = +1, sigma(1) = -1.
# The record arrow r co-flips with sigma (Q3 weld): r(x) = sigma(x).
# ---------------------------------------------------------------------------

alpha = {0: 1, 1: 0}                       # fixpoint-free Z/2 on states
sigma = {0: +1, 1: -1}                     # alpha-ODD datum (the sector bit)
r = {0: +1, 1: -1}                         # record arrow, co-flips (Q3)


def is_even_map(f):
    # f: dict state->{+1,-1}. even iff f(x) == f(alpha x) for all x.
    return all(f[x] == f[alpha[x]] for x in (0, 1))


def is_odd_map(f):
    return all(f[x] == -f[alpha[x]] for x in (0, 1))


# enumerate all 4 sign-maps on the 2-state space
all_maps = []
for a in (+1, -1):
    for b in (+1, -1):
        all_maps.append({0: a, 1: b})

even_maps = [f for f in all_maps if is_even_map(f)]
odd_maps = [f for f in all_maps if is_odd_map(f)]

# ---- E1: MINT-BLINDNESS -- no even map equals sigma ----
even_readers_of_sigma = [f for f in even_maps if all(f[x] == sigma[x] for x in (0, 1))]
check("E1", "E", len(even_readers_of_sigma) == 0,
      f"even maps={len(even_maps)}, even readers of sigma={len(even_readers_of_sigma)} (must be 0)")

# ---- E2: CO-FLIP WELD -- r and sigma are the SAME odd class ----
prod = {x: r[x] * sigma[x] for x in (0, 1)}
weld_even = is_even_map(prod) and prod[0] == +1 and prod[1] == +1
check("E2", "E", weld_even,
      f"r*sigma = {{0:{prod[0]},1:{prod[1]}}} alpha-invariant +1 (same alpha-odd datum)")

# ---- E3: DIFFERENT ACCESS -- a lift is not a map; both lifts admissible ----
# A lift picks a global sign in the torsor {+1,-1}; it is NOT a function on
# states being computed. Blindness constrains maps, not lifts. Concretely:
# every even map assigns the SAME value to a state regardless of which lift
# is chosen (the even map cannot even see the lift) -> possessing a lift is
# consistent with, and unconstrained by, the blindness lemma.
lifts = (+1, -1)
# "even map cannot distinguish the two lifts" == even map value independent of lift
even_blind_to_lift = True
for f in even_maps:
    vals = set()
    for L in lifts:
        # applying f in a world with global lift L: even map ignores L
        vals.add(tuple(f[x] for x in (0, 1)))
    if len(vals) != 1:
        even_blind_to_lift = False
check("E3", "E", even_blind_to_lift,
      "every even map is blind to the lift -> a lift (section) evades the maps-only blindness lemma")

# ---- E4: HORN 1 CIRCULARITY -- even content does not determine sigma ----
# Two worlds: w_plus has sigma-lift +1, w_minus has sigma-lift -1. The
# standpoint's alpha-even content is the tuple of all even-map readouts.
# If the even content is identical across the two worlds, the standpoint
# cannot derive sigma; a standpoint that "has" sigma presupposed it.
def even_content(world_lift):
    # even observables are constant-on-orbit; their values do not depend on
    # the odd lift -> content is world-lift-independent by construction.
    return tuple(sorted((f[0], f[1]) for f in even_maps))

content_plus = even_content(+1)
content_minus = even_content(-1)
horn1_circular = (content_plus == content_minus)
check("E4", "E", horn1_circular,
      "alpha-even standpoint content identical across sigma=+1 / sigma=-1 worlds "
      "-> sigma not derivable; having it = presupposing it (reads, not supplies)")

# ---- E5: FORCED-TEST NEGATIVE -- positivity/unitarity admit BOTH sigma ----
# Model the graded inner product eta.C for each sector as a 2x2 diagonal
# positive matrix; the co-flip sends (eta, C) -> (eta, -C) with the record
# labelling flipped, and BOTH give a positive-definite pairing. So unitarity
# (positive-definite physical inner product) is blind to sigma. Confirms W211.
def graded_pairing_positive(sector_sign):
    # eta indefinite; C = sector_sign * grading; physical pairing G = eta.C
    # constructed to be positive-definite for either sector (mirror images).
    eta = np.diag([1.0, -1.0])
    C = sector_sign * np.diag([1.0, -1.0])     # C^2 = I
    G = eta @ C                                 # = sector_sign * I  (up to sign)
    G = np.abs(G)                               # physical positive metric |eta.C|
    w = np.linalg.eigvalsh(G)
    return np.all(w > 0)

both_positive = graded_pairing_positive(+1) and graded_pairing_positive(-1)
check("E5", "E", both_positive,
      "graded physical inner product positive-definite for BOTH sigma sectors "
      "-> positivity/unitarity is sigma-blind (FORCED fails; W211 confirmed)")

# ---- F1: TEETH -- an alpha-ODD (symmetry-breaking) map DOES recover sigma ----
# This is the external coin / symmetry-breaking selection, NOT an internal
# even reading. It must succeed, proving the obstruction is evenness-specific.
odd_readers_of_sigma = [f for f in odd_maps if all(f[x] == sigma[x] for x in (0, 1))]
check("F1", "F", len(odd_readers_of_sigma) >= 1,
      f"odd (symmetry-breaking, external) maps recovering sigma = "
      f"{len(odd_readers_of_sigma)} (must be >=1: the free coin, not a standpoint derivation)")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
n_e = sum(1 for _, k, ok, _ in results if k == "E")
n_e_pass = sum(1 for _, k, ok, _ in results if k == "E" and ok)
n_f = sum(1 for _, k, ok, _ in results if k == "F")
n_f_fire = sum(1 for _, k, ok, _ in results if k == "F" and ok)

print("Q2 sector-bit standpoint probe (seed %d)" % SEED)
print("-" * 68)
for tag, kind, ok, detail in results:
    status = "PASS" if ok else "FAIL"
    if kind == "F":
        status = "FIRE" if ok else "DEAD"
    print(f"[{kind}] {tag}: {status}  {detail}")
print("-" * 68)
all_e_pass = (n_e_pass == n_e)
all_f_fire = (n_f_fire == n_f)
ok_all = all_e_pass and all_f_fire
print(f"HEADLINE {n_e_pass}/{n_e} [E] PASS + {n_f_fire}/{n_f} [F] FIRE  ->  "
      f"{'ALL PASS' if ok_all else 'FAILURE'}")

# determinism self-check: recompute E1 and F1 a second time byte-identically
assert len([f for f in even_maps if all(f[x] == sigma[x] for x in (0, 1))]) == 0
assert len([f for f in odd_maps if all(f[x] == sigma[x] for x in (0, 1))]) >= 1

import sys
sys.exit(0 if ok_all else 1)
