#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSTRUCTION swing -- PRONG 2 (DYNAMICAL): sigma as a dynamical fixed point.
Prereg: explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md (P3)
Artifact: explorations/construction-prong2-dynamical-2026-07-21.md

MODE: CONSTRUCTION. The POSIT is DECLARED, never reported as derived.

  POSIT (P3): sigma is CONSTITUTED as the self-consistent FIXED POINT of the
  evolving record-issuance loop S->I->O->S -- supplied by the dynamics as the
  loop closes, NOT read from a static state. Model record-issuance as a
  dynamical SELF-MAP Phi (one full loop traversal / closure), sigma = a fixed
  point of Phi (the closure orientation the loop settles on self-consistently).

DECISIVE CONSTRUCTION QUESTION (Lawvere / point-surjectivity): how many fixed
points does Phi have?
    UNIQUE   -> dynamics SELF-SUPPLIES sigma (static "can't-supply" overturned;
                sigma FORCED, not free).
    MULTIPLE -> loop admits both closures; sigma still a free/external choice.
    NONE     -> Godel/diagonal obstruction; consistent with external, no supply.

WHAT THE MODEL IS (faithful finite dynamical loop, two isospectral closures)
  * State token = (shard_type in {S,I,O}, orientation in {+1,-1},
                   record_dir in {+1,-1}, gen_count, issuance_index).
  * Rewrite steps S->I, I->O, O->S mint a FRESH token each (the acyclic HELIX;
    issuance_index strictly increases -- the one global arrow).
  * The O->S seam is the NULL STRATUM (q<0, K_S null, ~8% of ends): the place a
    fresh record is minted and the CLOSURE is applied. Two isospectral closures:
       NO-FLIP (trivial holonomy h=0):  orientation, record_dir unchanged.
       FLIP    (holonomy h=1 = alpha):  orientation, record_dir co-flip together
                                        (Q3 co-flip weld), gen_count invariant.
  * Phi := orientation map induced by ONE full S->I->O->S traversal.

READOUTS
  1. count_fixed_points(Phi) for each closure; assert NEVER == 1 (never UNIQUE).
  2. Co-flip weld: FLIP negates (orientation, record_dir) together; product is
     alpha-EVEN (invariant); gen_count alpha-EVEN.  (=> sigma is alpha-odd.)
  3. Z/2 local-system section count = fixed-point count: holonomy h=0 -> 2
     sections (MULTIPLE), h=1 -> 0 sections (NONE). A rank-1 Z/2 local system
     has NO unique global section => UNIQUE is structurally impossible.
     (This IS the TI H^1(finality sheaf) computation: fixed point exists iff
     H^1 obstruction vanishes iff holonomy trivial.)
  4. PUSH vs PULL vs SELF-CONSTITUTE discriminator.

PLANTED CONTROL (must be CAUGHT): a DETERMINISTIC CLOSED dynamics with sigma
NOT in the initial state, claiming to self-supply sigma via a "unique fixed
point." Back-gate: a genuine supplier must be alpha-EQUIVARIANT (output
co-varies with the true sigma); a closed deterministic default is alpha-EVEN
(constant) -> zero mutual information with the true sigma -> supplier_fires =
False.  TEETH: a genuine external ORACLE (equivariant) DOES fire -> shows the
gate registers real supply, and that supply is EXTERNAL (push/pull), not closed
self-supply.

Deterministic, pure enumeration, no RNG, no network. Exit 0 iff all pass.
"""

import sys
from itertools import count as _count

_ids = _count()


def fresh():
    return next(_ids)


# ---------------------------------------------------------------------------
# the faithful finite S->I->O->S rewriting loop, orientation-carrying
# ---------------------------------------------------------------------------

TYPES = ("S", "I", "O")
NEXT = {"S": "I", "I": "O", "O": "S"}


def seed(orientation, record_dir=+1, gen_count=3):
    return dict(t="S", o=orientation, r=record_dir, g=gen_count,
                idx=fresh(), tok=fresh())


def step(state, closure):
    """
    One rewrite. Mints a FRESH token (helix). At the O->S seam (null stratum)
    apply `closure` to the orientation/record_dir co-pair.
    closure in {"noflip","flip"}.
    """
    t = state["t"]
    nt = NEXT[t]
    o, r, g = state["o"], state["r"], state["g"]
    if t == "O":  # the seam: closure is applied here (null-stratum mint)
        if closure == "flip":
            o, r = -o, -r          # Q3 co-flip weld: sector + record arrow flip
        # gen_count g is left invariant either way (alpha-even)
    return dict(t=nt, o=o, r=r, g=g, idx=fresh(), tok=fresh())


def traverse_once(orientation, closure):
    """Phi: run a full S->I->O->S loop, return the resulting orientation."""
    s = seed(orientation)
    start_idx = s["idx"]
    for _ in range(3):            # S->I, I->O, O->S
        s = step(s, closure)
    # s["t"] is back to "S"; the issuance index strictly advanced (helix)
    assert s["t"] == "S"
    assert s["idx"] > start_idx   # monotone global arrow, closure-independent
    return s["o"]


def Phi(closure):
    """The induced orientation self-map on Z/2 = {+1,-1}."""
    return {o: traverse_once(o, closure) for o in (+1, -1)}


def count_fixed_points(selfmap):
    return sum(1 for o, fo in selfmap.items() if fo == o)


# ---------------------------------------------------------------------------
# Z/2 local-system sections (the H^1(finality sheaf) view)
# ---------------------------------------------------------------------------

def section_count(holonomy):
    """
    Global sections of a rank-1 Z/2 local system on the loop with the given
    holonomy h in {0 (=noflip), 1 (=flip)}.  A section assigns a value in
    {+1,-1} consistent around the loop: v == (-1)^h * v.
      h=0 -> v==v : both values are sections (2).
      h=1 -> v==-v: no value is a section (0).
    Equivalently: fixed points of Phi.  NEVER 1 for a Z/2 fiber.
    """
    if holonomy == 0:
        return 2      # H^1 obstruction vanishes; MULTIPLE sections
    return 0          # H^1 obstruction nonzero; NO section


# ---------------------------------------------------------------------------
# alpha-parity of internal read maps  (PULL: opaque token)
# ---------------------------------------------------------------------------

def all_maps_Z2_to_Z2():
    """The four maps {+1,-1} -> {+1,-1}."""
    vals = (+1, -1)
    maps = []
    for a in vals:
        for b in vals:
            maps.append({+1: a, -1: b})
    return maps


def is_alpha_even(m):
    """alpha-even (internal / third-person-available): f(-o) == f(o)."""
    return m[+1] == m[-1]


def reads_sigma(m):
    """A reader recovers the orientation: f(o) == o for all o (equivariant id)."""
    return m[+1] == +1 and m[-1] == -1


# ---------------------------------------------------------------------------
# PLANTED CONTROL: deterministic closed dynamics, sigma NOT in seed
# ---------------------------------------------------------------------------

def deterministic_closed_default(true_sigma, hardcoded=+1, steps=9):
    """
    A DETERMINISTIC, CLOSED rule that does NOT put sigma in its initial state:
    the seed orientation is UNSET (symmetric); the rule always drives toward a
    HARDCODED default. `true_sigma` is the actual external world-bit -- the rule
    never sees it. Returns the orientation the closed dynamics "outputs".
    """
    o = 0                      # UNSET / symmetric seed: sigma NOT in the state
    for _ in range(steps):
        o = hardcoded          # deterministic closed drive to the default
    return o                   # constant in true_sigma by construction


def external_oracle(true_sigma):
    """TEETH: a genuine EXTERNAL supplier -- reads the world-bit (equivariant)."""
    return true_sigma


def mutual_info_bit(fn):
    """
    1 bit iff fn's output DISTINGUISHES the two true-sigma worlds
    (alpha-equivariant supplier); 0 iff constant (alpha-even / blind).
    """
    return 1 if fn(+1) != fn(-1) else 0


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------

def main():
    print("=" * 74)
    print("CONSTRUCTION PRONG 2 (DYNAMICAL) -- sigma as a loop fixed point")
    print("POSIT (declared): sigma = self-consistent fixed point of Phi (loop closure)")
    print("=" * 74)

    results = {}

    # ---- 1. fixed-point COUNT of Phi for each isospectral closure ----------
    print("\n[1] FIXED-POINT COUNT of Phi = one full S->I->O->S traversal")
    phi_noflip = Phi("noflip")
    phi_flip = Phi("flip")
    n_noflip = count_fixed_points(phi_noflip)
    n_flip = count_fixed_points(phi_flip)
    print(f"    NO-FLIP closure (holonomy h=0): Phi = {phi_noflip}  fixed points = {n_noflip}  -> MULTIPLE")
    print(f"    FLIP    closure (holonomy h=1): Phi = {phi_flip}  fixed points = {n_flip}  -> NONE")
    print(f"    UNIQUE (==1) EVER? {n_noflip == 1 or n_flip == 1}")
    results["noflip_MULTIPLE"] = (n_noflip == 2)
    results["flip_NONE"] = (n_flip == 0)
    results["never_UNIQUE"] = (n_noflip != 1 and n_flip != 1)

    # ---- 2. co-flip weld: sigma is alpha-odd; product & gen_count alpha-even
    print("\n[2] CO-FLIP WELD (Q3): FLIP negates (orientation, record_dir) together")
    s0 = seed(+1, record_dir=+1, gen_count=3)
    s1 = s0
    for _ in range(3):
        s1 = step(s1, "flip")
    weld_ok = (s1["o"] == -s0["o"] and s1["r"] == -s0["r"])
    prod_even = (s1["o"] * s1["r"] == s0["o"] * s0["r"])   # product alpha-EVEN
    gen_even = (s1["g"] == s0["g"])                        # gen count alpha-EVEN
    print(f"    orientation +1 -> {s1['o']},  record_dir +1 -> {s1['r']}  (co-flip): {weld_ok}")
    print(f"    product orientation*record_dir invariant (alpha-EVEN): {prod_even}")
    print(f"    gen_count invariant (alpha-EVEN): {gen_even}")
    results["coflip_weld"] = weld_ok
    results["product_alpha_even"] = prod_even
    results["gencount_alpha_even"] = gen_even

    # ---- 3. Z/2 local-system sections = fixed-point count (H^1 view) --------
    print("\n[3] Z/2 LOCAL SYSTEM (TI H^1 finality sheaf): sections == fixed points")
    sec0, sec1 = section_count(0), section_count(1)
    print(f"    holonomy h=0: sections={sec0}  (== noflip fixed pts {n_noflip})  H^1 obstruction VANISHES")
    print(f"    holonomy h=1: sections={sec1}  (== flip   fixed pts {n_flip})  H^1 obstruction NONZERO")
    print(f"    a rank-1 Z/2 local system has NO UNIQUE section (never 1): {sec0 != 1 and sec1 != 1}")
    results["sections_match_fixedpoints"] = (sec0 == n_noflip and sec1 == n_flip)
    results["Z2_never_unique_section"] = (sec0 != 1 and sec1 != 1)

    # ---- 4. PUSH vs PULL vs SELF-CONSTITUTE --------------------------------
    print("\n[4] PUSH vs PULL vs SELF-CONSTITUTE")
    # SELF-CONSTITUTE: needs a UNIQUE fixed point that ALSO reads sigma
    # (alpha-equivariant). Fixed-point structure is alpha-symmetric in BOTH
    # closures, and count is never 1 -> self-constitution does not fire.
    self_constitute_fires = (n_noflip == 1 or n_flip == 1)
    # PULL: orientation is CARRIED as a token but internal (alpha-even) reads
    # cannot recover it.
    even_maps = [m for m in all_maps_Z2_to_Z2() if is_alpha_even(m)]
    even_readers = [m for m in even_maps if reads_sigma(m)]
    pull_opaque = (len(even_readers) == 0)   # no internal reader; token opaque
    # PUSH: an external seed sets orientation; the loop transports it (noflip)
    pushed_plus = traverse_once(+1, "noflip")
    pushed_minus = traverse_once(-1, "noflip")
    push_transports = (pushed_plus == +1 and pushed_minus == -1)
    print(f"    SELF-CONSTITUTE fires (unique+equivariant fixed pt)? {self_constitute_fires}")
    print(f"    PULL: internal alpha-even readers of sigma = {len(even_readers)} (token opaque): {pull_opaque}")
    print(f"    PUSH: external seed +/-1 transported by loop unchanged: {push_transports}")
    print("    VERDICT: NOT self-constituted; value is PUSHED (seed) + PULLED (opaque token).")
    results["self_constitute_does_not_fire"] = (self_constitute_fires is False)
    results["pull_opaque"] = pull_opaque
    results["push_transports"] = push_transports

    # ---- 5. PLANTED CONTROL: deterministic closed, sigma NOT in seed -------
    print("\n[5] PLANTED CONTROL -- deterministic CLOSED dynamics, sigma NOT in seed")
    ctrl_fn = lambda tsig: deterministic_closed_default(tsig, hardcoded=+1)
    ctrl_info = mutual_info_bit(ctrl_fn)
    ctrl_supplier_fires = (ctrl_info == 1)
    print(f"    output in sigma=+1 world: {ctrl_fn(+1)};  in sigma=-1 world: {ctrl_fn(-1)}")
    print(f"    mutual info with true sigma: {ctrl_info} bit  (constant => alpha-EVEN => blind)")
    print(f"    control 'self-supplies' sigma? {ctrl_supplier_fires}  -> CAUGHT: {not ctrl_supplier_fires}")
    results["CONTROL_caught"] = (ctrl_supplier_fires is False)

    # ---- 6. TEETH: a genuine external ORACLE DOES fire ---------------------
    print("\n[6] TEETH -- genuine EXTERNAL oracle (equivariant) must FIRE")
    oracle_info = mutual_info_bit(external_oracle)
    oracle_fires = (oracle_info == 1)
    print(f"    oracle output +1-world: {external_oracle(+1)}, -1-world: {external_oracle(-1)}")
    print(f"    mutual info: {oracle_info} bit -> supplier fires: {oracle_fires}")
    print("    (real supply exists -- but it is EXTERNAL/push, not closed self-supply)")
    results["TEETH_oracle_fires"] = (oracle_fires is True)

    # ---- verdict -----------------------------------------------------------
    print("\n" + "-" * 74)
    expected = {
        "noflip_MULTIPLE": True,
        "flip_NONE": True,
        "never_UNIQUE": True,
        "coflip_weld": True,
        "product_alpha_even": True,
        "gencount_alpha_even": True,
        "sections_match_fixedpoints": True,
        "Z2_never_unique_section": True,
        "self_constitute_does_not_fire": True,
        "pull_opaque": True,
        "push_transports": True,
        "CONTROL_caught": True,
        "TEETH_oracle_fires": True,
    }
    ok = all(results.get(k) == v for k, v in expected.items())
    print("=" * 74)
    for k, v in expected.items():
        got = results.get(k)
        print(f"  {'PASS' if got == v else 'FAIL'}  {k}: expected {v}, got {got}")
    print("=" * 74)
    n_e = sum(1 for k in expected if k not in ("CONTROL_caught", "TEETH_oracle_fires"))
    print(f"HEADLINE: {n_e} [E] + 2 [F] = {len(expected)} :: "
          f"FIXED-POINT COUNT never UNIQUE (MULTIPLE|NONE) -> "
          f"dynamics does NOT self-supply sigma; PUSH+PULL, not SELF-CONSTITUTE")
    print(f"CLASSIFIER BEHAVED AS DESIGNED (control caught, teeth fire): {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
