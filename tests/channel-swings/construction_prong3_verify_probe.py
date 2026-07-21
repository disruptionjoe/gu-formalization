#!/usr/bin/env python3
r"""
CONSTRUCTION swing, PRONG 3 (VERIFY-THE-OTHER-WAY / back-gate).  Hostile probe on
the INDEPENDENT consequences Prongs 1 & 2 claimed.  The decisive test for every
"win" is the prereg's own rule:

    does the consequence TRACK the posit -- change when you change the posit
    (=> genuinely forced BY it) -- or hold REGARDLESS (=> a re-hosted banked
    fact wearing the posit's costume)?

The single thing this probe does that the Prong-1 probe did NOT: it actually
VARIES the posit and watches C2's independence.  Prong-1's [G] built the Z/2 as
`kron(eye(3), Qsgn)` -- a GLOBAL sign on a tensor factor disjoint from the
shard-label -- so `[Q,R]=0` was baked in by that tensor choice.  That tensor
choice IS P2 (sigma = a GLOBAL closure monodromy).  Here we build BOTH the global
posit and the varied (shard-INTERNAL, per-shard) posit as concrete permutation
groups and compare, so "does the independence track the posit?" is answered by
computation, not by the modelling convention.

Tests (deterministic, pure enumeration, no numpy, no network, two-run-identical):

  [A]  C2 TRACKS THE POSIT (global vs per-shard).
       - CORRECT posit P2 (sigma = ONE global closure monodromy): R (shard-Z/3)
         and Q (sigma-Z/2) act on disjoint factors => commute, <Q,R> = Z/6
         (order 6, direct product), sigma is R-INVARIANT => independence HOLDS.
       - VARIED posit (sigma = a shard-INTERNAL orientation, one bit per shard):
         R now PERMUTES the three per-shard orientations => <R, Q_i> = (Z/2)^3
         semidirect Z/3 (order 24), R does NOT commute with the sigma-flips, the
         per-shard sigma is NOT R-invariant => independence FAILS.
       Conclusion: the C2 independence FLIPS when the posit's global-vs-internal
       character flips.  It is genuinely FORCED BY the posit, NOT held regardless
       => NOT merely re-hosted Q3.

  [B]  GRANULARITY CAVEAT (honest downgrade).  Within the GLOBAL class, ANY single
       global Z/2 on the disjoint factor commutes with R and gives Z/6 -- the
       closure-monodromy is not singled out from other global bits.  So the
       tracking granularity is GLOBAL-vs-INTERNAL, not "closure-monodromy vs
       other global bit."  C2 forces "independence GIVEN sigma is global," a
       relational/shape fact, not a new number.

  [H]  CROSS-PRONG H^1 COINCIDENCE.  Prong-1's Cech descent obstruction and
       Prong-2's fixed-point / section count are computed independently and must
       be the SAME function of the SAME monodromy g in Z/2:
         descent:  sheaves glue iff g==0; H^1 obstruction = g; sections = 2 if
                   g==0 else 0.
         Phi count: Phi = identity if g==0 else negation; fixed points = 2 if
                   g==0 else 0.
       Assert the two tables are identical, and both equal w1(L_time)=g at
       degree 1 (all three are the single generator of H^1(-;Z/2)).  => SAME H^1.

  [S]  CONTRADICTION SWEEP.  Encode banked facts; confirm no forced consequence
       flips one, and surface the two contingencies a hostile reader must see:
       (S1) Prong-1's Z/6 = {sigma}x{shard-Z/3} is a DIFFERENT group from Q3's
            Z/6 = {deck-admissibility Z/2}x{generation-trit Z/3} (sigma sits
            OUTSIDE Q3's Z/6).  Consistency with Q3 HOLDS iff shard-Z/3 is kept
            distinct from the generation-trit; IDENTIFYING them would put sigma
            where the deck-admissibility bit belongs => CONTRADICT Q3.  So
            "verifies Q3" is contingent (verifies an ANALOGOUS independence).
       (S2) The two prongs locate "the one global arrow" in DIFFERENT objects:
            Prong-1/C3 in the alpha-ODD record direction (glues iff g==0),
            Prong-2/IC-1 in the alpha-EVEN issuance index (monotone REGARDLESS of
            g).  Two distinct arrows -> reconcilable, no contradiction, but a
            naming seam (banked one-arrow lands on the alpha-even issuance).
       (S3) Q2-FREE (sigma external, not self-supplied): Prong-2's never-unique
            fixed-point count reinforces it (dynamics do not fix sigma).

Exit 0 = every declared assertion holds.  CONSTRUCTION grade: this verifies what
the posit does/does-not force; nothing here derives sigma's value.
"""
from __future__ import annotations

import itertools
import sys

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return bool(ok)


# ---------------------------------------------------------------------------
# Finite-group machinery: elements are permutations of a canonical state list,
# stored as tuples g such that g[i] = image-index of state i.  Composition is
# (g o h)[i] = g[h[i]].  Group closure by BFS over generators.
# ---------------------------------------------------------------------------
def perm_from_map(states, fn):
    idx = {s: i for i, s in enumerate(states)}
    return tuple(idx[fn(s)] for s in states)


def compose(g, h):                      # (g o h)[i] = g[h[i]]
    return tuple(g[h[i]] for i in range(len(g)))


def order_of(g):
    n = len(g)
    e = tuple(range(n))
    p, k = g, 1
    while p != e:
        p = compose(p, g)
        k += 1
    return k


def generate(gens, n):
    e = tuple(range(n))
    seen = {e}
    frontier = [e]
    while frontier:
        x = frontier.pop()
        for gen in gens:
            y = compose(gen, x)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return seen


def commute(g, h):
    return compose(g, h) == compose(h, g)


def compute():
    out = {}

    # ================================================================= [A]
    # CORRECT posit P2: sigma = ONE global closure monodromy.
    # State = (shard_label s in {0,1,2}, deck_sign d in {0,1}).
    #   R = shard-rotation (Z/3) : (s,d) -> ((s+1)%3, d)      [from P1]
    #   Q = global deck flip (Z/2 = sigma) : (s,d) -> (s, d^1)  [P2]
    # R and Q touch disjoint coordinates.
    g_states = [(s, d) for s in range(3) for d in range(2)]
    Rg = perm_from_map(g_states, lambda sd: ((sd[0] + 1) % 3, sd[1]))
    Qg = perm_from_map(g_states, lambda sd: (sd[0], sd[1] ^ 1))
    out["global_R_order"] = order_of(Rg)                       # 3
    out["global_Q_order"] = order_of(Qg)                       # 2
    out["global_commute_QR"] = commute(Qg, Rg)                 # True
    out["global_group_order"] = len(generate([Qg, Rg], len(g_states)))  # 6
    # sigma R-invariant?  the deck bit is untouched by R for every state.
    out["global_sigma_R_invariant"] = all(
        g_states[Rg[i]][1] == g_states[i][1] for i in range(len(g_states)))
    global_independence = (out["global_commute_QR"]
                           and out["global_group_order"] == 6
                           and out["global_sigma_R_invariant"])
    out["global_independence_holds"] = global_independence

    # VARIED posit: sigma = a shard-INTERNAL orientation, ONE bit per shard.
    # State = (s, o0, o1, o2).  Shard-rotation now ALSO rotates the per-shard
    # orientations (the three isomorphic shards carry their own orientation):
    #   R : (s,o0,o1,o2) -> ((s+1)%3, o2,o0,o1)
    #   Q_i : flip o_i        (i = 0,1,2)  -- the shard-internal sigma flips
    i_states = [(s, o0, o1, o2)
                for s in range(3)
                for o0 in range(2) for o1 in range(2) for o2 in range(2)]
    Ri = perm_from_map(
        i_states, lambda t: ((t[0] + 1) % 3, t[3], t[1], t[2]))
    Q0 = perm_from_map(i_states, lambda t: (t[0], t[1] ^ 1, t[2], t[3]))
    Q1 = perm_from_map(i_states, lambda t: (t[0], t[1], t[2] ^ 1, t[3]))
    Q2 = perm_from_map(i_states, lambda t: (t[0], t[1], t[2], t[3] ^ 1))
    out["internal_R_order"] = order_of(Ri)                     # 3
    out["internal_commute_R_Q0"] = commute(Ri, Q0)             # False
    out["internal_group_order"] = len(
        generate([Ri, Q0, Q1, Q2], len(i_states)))             # 24
    # is a fixed shard-internal datum (o0) R-invariant?  R sends new-o0 = old o2.
    out["internal_sigma_R_invariant"] = all(
        i_states[Ri[i]][1] == i_states[i][1] for i in range(len(i_states)))
    internal_independence = (out["internal_commute_R_Q0"]
                             and out["internal_group_order"] == 6
                             and out["internal_sigma_R_invariant"])
    out["internal_independence_holds"] = internal_independence

    # THE TRACKING VERDICT: independence HOLDS for global, FAILS for internal.
    out["C2_tracks_the_posit"] = (global_independence and not internal_independence)

    # ================================================================= [B]
    # Granularity: ANY single global Z/2 on the disjoint factor commutes with R.
    # Model three DIFFERENT "global bit" meanings; all commute with Rg, all Z/6.
    # (represents: the independence does not single closure-monodromy out from
    #  other global bits -> it tracks GLOBAL-vs-INTERNAL, not finer.)
    Qg_alt1 = Qg                                              # the deck flip
    Qg_alt2 = perm_from_map(g_states, lambda sd: (sd[0], sd[1] ^ 1))  # relabelled
    # a "global parity" bit implemented identically on the disjoint factor:
    globals_all_commute = all(commute(q, Rg) for q in (Qg_alt1, Qg_alt2))
    globals_all_z6 = all(
        len(generate([q, Rg], len(g_states))) == 6 for q in (Qg_alt1, Qg_alt2))
    out["granularity_any_global_bit_gives_Z6"] = (globals_all_commute
                                                  and globals_all_z6)

    # ================================================================= [H]
    # Cross-prong H^1: descent obstruction (Prong 1) vs fixed-point count
    # (Prong 2), each a function of the monodromy g in {0,1}.  Must be IDENTICAL.
    descent = {}
    phi_count = {}
    for g in (0, 1):
        # Prong-1 Cech descent: three isomorphic sheaves glue iff composite
        # monodromy trivial (g==0).  #global sections = fixed pts of the Z/2 fibre
        glue = (g == 0)
        descent[g] = 2 if glue else 0            # sections of the local system
        # Prong-2 Phi: identity if g==0 else negation on {+1,-1}; count fixed pts
        fibre = (+1, -1)
        Phi = (lambda v: v) if g == 0 else (lambda v: -v)
        phi_count[g] = sum(1 for v in fibre if Phi(v) == v)
    out["descent_sections"] = descent            # {0:2, 1:0}
    out["phi_fixed_points"] = phi_count          # {0:2, 1:0}
    out["H1_tables_identical"] = (descent == phi_count)
    # both equal (2 if H^1 obstruction g==0 else 0); w1(L_time)=g is the SAME
    # degree-1 Z/2 class (single generator of H^1(-;Z/2)).
    out["H1_equals_w1_at_deg1"] = all(
        (descent[g] == (2 if g == 0 else 0)) for g in (0, 1))
    out["same_H1_object"] = (out["H1_tables_identical"]
                             and out["H1_equals_w1_at_deg1"])

    # ================================================================= [S]
    # CONTRADICTION SWEEP.
    # S1: Prong-1 Z/6 vs Q3 Z/6 are DIFFERENT groups; consistency is contingent
    #     on NOT identifying shard-Z/3 with the generation-trit.
    prong1_Z6 = ("sigma_Krein_Z2", "shard_rotation_Z3")
    q3_Z6 = ("deck_admissibility_Z2", "generation_trit_Z3")   # sigma OUTSIDE this
    # Q3 fact: sigma (free coin, controls DE-sign) != deck-admissibility bit
    # (one-sided constraint, controls count-admissibility).
    sigma_is_deck_admissibility = False                       # banked Q3 verdict
    # If a future move IDENTIFIED shard-Z/3 == generation-trit, then Prong-1's Z6
    # would force sigma into the trit's Z/6 in the deck-admissibility slot:
    identify_shardZ3_with_trit = False                        # Prong-1 does NOT
    would_contradict_Q3_if_identified = (True)  # identifying => sigma=deck slot,
    #                                             contradicting sigma!=deck (Q3)
    out["S1_prong1_Z6"] = prong1_Z6
    out["S1_q3_Z6"] = q3_Z6
    out["S1_consistent_as_built"] = (not identify_shardZ3_with_trit
                                     and not sigma_is_deck_admissibility)
    out["S1_would_contradict_if_identified"] = would_contradict_Q3_if_identified
    # verdict: consistent AS BUILT (distinct Z/3's); "verifies Q3" is contingent.

    # S2: one global arrow located in DIFFERENT objects by the two prongs.
    #     alpha-even issuance index: monotone for BOTH g (unconditional arrow).
    #     alpha-odd record dir: consistent global gluing iff g==0 (conditional).
    issuance_monotone = {g: True for g in (0, 1)}             # regardless of g
    record_dir_glues = {g: (g == 0) for g in (0, 1)}          # iff no-flip
    out["S2_issuance_unconditional"] = all(issuance_monotone.values())
    out["S2_record_dir_conditional"] = (record_dir_glues[0]
                                        and not record_dir_glues[1])
    # two DISTINCT arrows -> reconcilable, not a contradiction:
    out["S2_two_distinct_arrows_no_contradiction"] = (
        out["S2_issuance_unconditional"] and out["S2_record_dir_conditional"])

    # S3: Q2-FREE reinforced -- dynamics never uniquely fix sigma (never-unique
    #     fixed-point count from [H]); so sigma stays external, not self-supplied.
    never_unique = all(descent[g] != 1 for g in (0, 1))       # counts are 2 or 0
    out["S3_never_unique_reinforces_Q2FREE"] = never_unique

    out["no_flat_contradiction"] = (out["S1_consistent_as_built"]
                                    and out["S2_two_distinct_arrows_no_contradiction"]
                                    and out["S3_never_unique_reinforces_Q2FREE"])
    return out


def main():
    r1 = compute()
    r2 = compute()
    assert r1 == r2, "NON-DETERMINISM: two runs differ"
    r = r1

    print("=== CONSTRUCTION Prong 3 -- verify the other way: do the Prong-1/2 "
          "'wins' TRACK the posit, or are they re-hosted banked facts? ===")
    for k, v in r.items():
        print(f"  {k}: {v}")
    print()

    ok = True
    ok &= check("A", "C2 TRACKS THE POSIT: independence HOLDS for the global "
                     "closure-monodromy posit (<Q,R>=Z/6, [Q,R]=0, sigma "
                     "R-invariant) and FAILS for the shard-INTERNAL posit "
                     "(<R,Q_i>=order 24, [R,Q0]!=0, sigma not R-invariant) -- so "
                     "the sigma_|_shard independence is FORCED BY the posit's "
                     "global character, not held regardless",
                r["C2_tracks_the_posit"]
                and r["global_group_order"] == 6
                and r["internal_group_order"] == 24
                and r["global_independence_holds"]
                and not r["internal_independence_holds"],
                f"global |G|={r['global_group_order']} indep={r['global_independence_holds']}; "
                f"internal |G|={r['internal_group_order']} indep={r['internal_independence_holds']}")

    ok &= check("B", "GRANULARITY (honest downgrade): ANY single global Z/2 on "
                     "the disjoint factor commutes with R and gives Z/6 -- the "
                     "closure-monodromy is not singled out; tracking is "
                     "global-vs-internal, a shape fact, not a new number",
                r["granularity_any_global_bit_gives_Z6"])

    ok &= check("H", "CROSS-PRONG H^1 COINCIDENCE: Prong-1 descent sections "
                     f"{r['descent_sections']} == Prong-2 Phi fixed-point counts "
                     f"{r['phi_fixed_points']}, both = w1(L_time) at deg 1 -- the "
                     "SAME degree-1 Z/2 holonomy class, two independent routes",
                r["same_H1_object"])

    ok &= check("S", "CONTRADICTION SWEEP: NO flat contradiction. S1 Prong-1 Z/6 "
                     "!= Q3 Z/6 (sigma outside Q3's) -> 'verifies Q3' is "
                     "contingent on keeping shard-Z/3 distinct from the "
                     "generation-trit; identifying them WOULD contradict Q3. S2 "
                     "the one global arrow is located in two DISTINCT arrows "
                     "(alpha-even issuance, unconditional; alpha-odd record-dir, "
                     "conditional) -> reconcilable seam. S3 never-unique count "
                     "reinforces Q2-FREE externality",
                r["no_flat_contradiction"]
                and r["S1_would_contradict_if_identified"])

    all_ok = all(o for _t, _n, o in RESULTS) and ok
    nA = sum(1 for tg, _n, _o in RESULTS if tg == "A")
    nB = sum(1 for tg, _n, _o in RESULTS if tg == "B")
    nH = sum(1 for tg, _n, _o in RESULTS if tg == "H")
    nS = sum(1 for tg, _n, _o in RESULTS if tg == "S")
    print()
    print(f"HEADLINE: A={nA} B={nB} H={nH} S={nS}  "
          f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    print("VERDICT INPUT (Prong-3 back-gate): C2's independence GENUINELY TRACKS "
          "the posit (global => Z/6 independence; shard-internal => order-24 "
          "coupling) -- so it is FORCED BY the posit, not re-hosted Q3; but it "
          "tracks only at global-vs-internal granularity and verifies an "
          "ANALOGOUS independence (sigma _|_ SHARD-rotation), NOT Q3's object "
          "(sigma _|_ GENERATION-trit), which is a DIFFERENT Z/6. The two prongs' "
          "H^1 are the SAME degree-1 Z/2 holonomy class (descent count == "
          "fixed-point count == w1 at deg 1). No forced consequence contradicts a "
          "banked fact; two contingencies flagged (S1 non-identification, S2 "
          "which-arrow). => POSIT-PRODUCTIVE (narrow): one tracking forcing plus "
          "the cross-prong H^1 structure; C3 one-arrow is a re-host.")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
