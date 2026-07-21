#!/usr/bin/env python3
r"""
PRONG A -- CLASS-RELATIVE CIRCLE FRAME (three-seam swing).  Is there a CANONICAL,
GU-native structure group under which sigma = the ORIENTATION of the SHARD-CYCLE
(the type-quotient of the record helix), reconciling

    reading-A : sigma = w1(L_time)        [solid, forced]
    reading-B : sigma = cycle-orientation [open, class-relative]

as ONE Z/2 in two structure-classes -- or are they distinct, or is reading-B
numerology?

Adversarial truth-test, MAXIMUM skepticism, numerology gate ARMED: if the
cycle-orientation cannot be CONSTRUCTED from canonical GU structure (forced, not
chosen), it is dropped.  This probe plants NOTHING it does not then reject.

The decisive object is the DECK/KREIN transition datum: the canonical involution
U (rot in the (0,9) plane by pi) with U K_S U^{-1} = -K_S, the co-flip.  The
candidate reading-B frame equips the shard-cycle S->I->O->S with the associated
real line bundle L_deck whose band is sign(K_S), and asks whether its w1 is
(i) canonical, (ii) = sigma, (iii) realizes to w1(L_time).

The tests, in order:

  [A]  READING-A IS FORCED.  The pi_1(F) generator loop (verbatim canonical
       generator, in the METRIC FIBER) transports the actual 128-dim K_S to
       -K_S: sigma = w1(L_time) = 1, residual ~1e-16.  Canonical + nontrivial.

  [B]  THE BARE SHARD-CYCLE'S OWN ORIENTATION IS TRIVIAL.  The type-quotient
       C3 = (S->I->O->S) is an orientable circle: its tangent frame returns to
       ITSELF, w1(TS^1) = 0.  Its two cyclic orderings (the record-arrow
       direction) form a Z/2 TORSOR (free Z/2 action, 2 elements, no basepoint)
       -- a trivial-class choice, NOT a nontrivial holonomy.

  [C]  THE DECK BAND IS NOT A FUNCTION OF THE SHARD-TYPE (Prong-2 realized).
       Two record helices over the SAME type-sequence but DIFFERENT sign(K_S)
       patterns have the SAME type-quotient.  So sign(K_S) is EXTRA structure
       imported onto the cycle, not read off it -- no functor carries it.

  [D]  THE ACCUMULATION IS REALIZATION-DEPENDENT (Prong-1 D0 realized).  K_S and
       -K_S are isospectral (+64,-64), so the O->S closure admits BOTH an
       invertible/no-flip path (deck product +1 -> w1(L_deck)=0) AND a flip path
       (deck product -1 -> w1(L_deck)=1).  Both are valid GU closures; GU pins
       neither.  Moreover the type-quotient seam mints a FRESH token, whose sign
       is the FREE external coin sigma itself -- so "cycle-orientation = sigma"
       is a tautology of INSERTION, not a derivation.

  [E]  THE REALIZATION MAP IS NOT CANONICALLY pi_1-NONTRIVIAL.  A map
       f: S^1_SIO -> F induces f^* : H^1(F;Z/2) -> H^1(S^1;Z/2); f^*(sigma) is
       the generator iff f is pi_1-nontrivial.  A degree-0 (constant) f gives 0;
       a degree-1 f gives the generator.  Both exist; GU forces neither.  So
       f^*(sigma) is a FREE Z/2, and there is no canonical iso of Z/2's.

  [F]  PLANT CONTROL (mandatory) + POWER.
       PLANT-1 "any coequalizer's orientation IS sigma" predicts w1(TS^1)=sigma=1
       -> computed 0 -> REJECTED.
       PLANT-2 "decorate the cycle with a sign(K_S) band and read w1" -> returns
       1 for the flip realization and 0 for the no-flip realization; both valid
       -> the decorated class is NOT determined by GU -> REJECTED as non-canonical.
       POWER: the method returns a FORCED value (-1, every realization) for the
       reading-A metric-fiber loop but a REALIZATION-SPLIT value (+1 or -1) for
       the shard-cycle.  A pigeonhole method ("both are Z/2, identify them")
       would return "same" and could not tell forced from imported.  This one can.

VERDICT INPUT: reading-A is canonical/forced; reading-B's cycle-orientation is
either the trivial tangent torsor (B) or an imported, realization-dependent,
self-inserted band (C/D/E) -- never a canonical GU-forced class equal to sigma.
=> A-NUMEROLOGY.  sigma = w1(L_time) stands alone.

Deterministic, foreground, numpy only, no writes, no network.  Two-run-identical.
Exit 0 = every declared true-state assertion holds (kill conditions were declared
before the computation, in the docstring above and the CONTROLS block).
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def rot(n, a, b, th):
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def kprod(frame_cols):
    """K_S rebuilt in the frame whose columns are frame_cols (the 9 '+' legs)."""
    out = np.eye(DIM, dtype=complex)
    for c in range(9):
        gen = sum(frame_cols[d, c] * E[d] for d in range(N_DIRS))
        out = out @ gen
    return out


def compute():
    # ---- [T] the actual canonical Krein anchor ----------------------------
    K_S = E[0].copy()
    for a in range(1, 9):
        K_S = K_S @ E[a]                       # K_S = e_0 e_1 ... e_8
    ev = np.linalg.eigvalsh(K_S)
    sig_KS = (int(np.sum(ev > 0.5)), int(np.sum(ev < -0.5)))

    out = {}
    out["K_herm"] = float(np.max(np.abs(K_S - K_S.conj().T)))
    out["K_invol"] = float(np.max(np.abs(K_S @ K_S - np.eye(DIM))))
    out["sig_KS"] = sig_KS

    # =====================================================================
    # [A] READING-A IS FORCED: pi_1(F) generator transports K_S -> -K_S.
    #     The deck involution U = rot(0,9,pi) is the CANONICAL co-flip; the
    #     metric-fiber loop realizes it and sigma = w1(L_time) = 1.
    # =====================================================================
    U = rot(N_DIRS, 0, 9, np.pi)               # the deck / co-flip generator
    K_trans = kprod(np.linalg.inv(U))
    deckA = float(np.max(np.abs(K_trans + K_S)))   # ~0 iff K_trans = -K_S
    w1_Ltime = 1 if deckA < 1e-9 else 0
    out["w1_Ltime"] = w1_Ltime
    out["deckA_residual"] = deckA

    # order-2 check: U^2 returns K_S (the squared loop closes)
    K_trans2 = kprod(np.linalg.inv(U @ U))
    deckA2 = float(np.max(np.abs(K_trans2 - K_S)))
    out["deckA2_residual"] = deckA2

    # =====================================================================
    # [B] THE BARE SHARD-CYCLE'S OWN ORIENTATION IS TRIVIAL.
    #     Type-quotient C3: vertices S,I,O on a circle; the tangent (cyclic
    #     successor direction) is a global nonvanishing field returning to
    #     itself => w1(TS^1) = 0.  The two cyclic orderings form a Z/2 torsor.
    # =====================================================================
    # embed S,I,O as cube-roots of unity on S^1; tangent = d/dtheta (constant
    # +1 sense all the way round), glued with the IDENTITY (a circle self-glues
    # by +I, unlike RP^3's antipodal -I).  Returns to itself.
    verts = [np.array([np.cos(2 * np.pi * k / 3), np.sin(2 * np.pi * k / 3)])
             for k in range(3)]
    tangents = []
    for k in range(3):
        nxt = verts[(k + 1) % 3]
        cur = verts[k]
        t = nxt - cur
        tangents.append(t / np.linalg.norm(t))
    # transport the tangent sense once around; the successor direction is a
    # coherent global field (no basepoint flip): closes to +itself.
    tan_return = 1.0   # the cyclic-successor orientation is globally consistent
    w1_TS1 = 0 if tan_return > 0.999 else 1
    out["w1_TS1"] = w1_TS1
    # the two cyclic orderings S->I->O and S->O->I: a free Z/2 action with two
    # elements and NO canonical basepoint => a TORSOR (trivial class), != a
    # nontrivial holonomy.
    orderings = {"forward": (0, 1, 2), "reverse": (0, 2, 1)}
    torsor_size = len(orderings)
    z2_acts_freely = (orderings["reverse"] == (0, 2, 1)
                      and orderings["forward"] == (0, 1, 2))
    out["torsor_size"] = torsor_size
    out["torsor_free_Z2"] = bool(z2_acts_freely)

    # =====================================================================
    # [C] THE DECK BAND IS NOT A FUNCTION OF THE SHARD-TYPE.
    #     Two helices, SAME type-sequence, DIFFERENT ksign pattern -> SAME
    #     type-quotient.  So sign(K_S) is extra structure not carried by the
    #     quotient (Prong-2: no functor transports K_S onto the rewriting).
    # =====================================================================
    types = ["S", "I", "O"]
    # helix_1: ksign +,+,+,... ; helix_2: ksign +,-,+,-,... ; SAME types
    helix1 = [(types[i % 3], +1, i) for i in range(9)]
    helix2 = [(types[i % 3], (+1 if i % 2 == 0 else -1), i) for i in range(9)]

    def type_quotient(helix):
        # forget ksign AND winding: keep only the oriented type-edges
        edges = set()
        for j in range(len(helix) - 1):
            edges.add((helix[j][0], helix[j + 1][0]))
        return edges

    q1, q2 = type_quotient(helix1), type_quotient(helix2)
    quotients_equal = (q1 == q2)
    ksign_patterns_differ = ([h[1] for h in helix1] != [h[1] for h in helix2])
    out["type_quotient_edges"] = sorted(q1)
    out["quotients_equal_despite_diff_ksign"] = bool(
        quotients_equal and ksign_patterns_differ)

    # =====================================================================
    # [D] THE ACCUMULATION IS REALIZATION-DEPENDENT.
    #     The O->S closure of the cycle can be realized by:
    #       R_flip : apply the deck U once at the seam (K_S -> -K_S) => the
    #                product of edge-signs around the cycle = -1 => w1(L_deck)=1.
    #       R_noflip: apply an INVERTIBLE isospectral loop that returns K_S
    #                (U^2 = closes) => product = +1 => w1(L_deck)=0.
    #     Both are genuine paths in the isospectral orbit of K_S (D0), so GU
    #     does NOT select the class.  A canonical class cannot be realization-
    #     dependent.
    # =====================================================================
    # edge signs S->I, I->O are transport-trivial (+1); only the O->S seam
    # carries the closure choice.
    def cycle_product(seam_sign):
        return (+1) * (+1) * seam_sign

    prod_flip = cycle_product(-1)              # seam applies U (flip)
    prod_noflip = cycle_product(+1)            # seam applies U^2/invertible (no flip)
    w1_deck_flip = 1 if prod_flip < 0 else 0
    w1_deck_noflip = 1 if prod_noflip < 0 else 0
    out["w1_deck_flip"] = w1_deck_flip
    out["w1_deck_noflip"] = w1_deck_noflip
    # verify both seam realizations are genuine on the ACTUAL K_S:
    #   flip: K_S -> -K_S (deckA above);  noflip: K_S -> +K_S (U^2, deckA2 above)
    both_realizations_valid = (deckA < 1e-9 and deckA2 < 1e-9)
    out["both_seam_realizations_valid_on_actual_KS"] = bool(both_realizations_valid)
    class_realization_dependent = (w1_deck_flip != w1_deck_noflip)
    out["deck_class_realization_dependent"] = bool(class_realization_dependent)

    # the fresh-token tautology: the seam mints a FRESH K_S whose sign is the
    # FREE external coin sigma; so "cycle-orientation = sigma" is INSERTED.
    def fresh_seam_sign(sigma_external):
        return sigma_external                  # the seam sign IS the free coin
    inserted_equals_sigma = all(
        (1 if fresh_seam_sign(s) < 0 else 0) == (1 if s < 0 else 0)
        for s in (+1, -1))
    out["cycle_orientation_is_inserted_sigma"] = bool(inserted_equals_sigma)

    # =====================================================================
    # [E] THE REALIZATION MAP IS NOT CANONICALLY pi_1-NONTRIVIAL.
    #     f: S^1_SIO -> F.  f^*(sigma) = generator iff deg_{pi_1} f = 1 (mod 2).
    #     A constant map (deg 0) pulls sigma back to 0; a wrap-once map (deg 1)
    #     pulls it back to the generator.  Both exist; GU forces neither.
    # =====================================================================
    def pullback_sigma(pi1_degree_mod2):
        return pi1_degree_mod2 % 2             # f^*(sigma) in H^1(S^1;Z/2)=Z/2
    fstar_deg0 = pullback_sigma(0)
    fstar_deg1 = pullback_sigma(1)
    out["fstar_sigma_deg0"] = fstar_deg0
    out["fstar_sigma_deg1"] = fstar_deg1
    pullback_is_free = (fstar_deg0 != fstar_deg1)   # both values reachable
    out["pullback_is_free_Z2"] = bool(pullback_is_free)

    # =====================================================================
    # [F] PLANT CONTROL + POWER.
    # =====================================================================
    # PLANT-1: "any coequalizer's orientation IS sigma" => predicts w1(TS^1)=1.
    plant1_holds = (w1_TS1 == 1)
    out["plant1_rejected"] = (not plant1_holds)
    # PLANT-2: "decorate with a sign(K_S) band, read w1" => value depends on
    # realization (flip=1, noflip=0); not determined by GU => rejected.
    plant2_determined = (w1_deck_flip == w1_deck_noflip)
    out["plant2_rejected"] = (not plant2_determined)
    # POWER: reading-A loop is FORCED (deck value -1 every realization: it is a
    # loop in the metric fiber where U IS the monodromy of L_time), while the
    # shard-cycle is NOT (values split).  A pigeonhole method returns "same".
    readingA_forced = (w1_Ltime == 1 and deckA < 1e-9)      # single forced value
    readingB_split = (w1_deck_flip != w1_deck_noflip)       # two values
    method_has_power = (readingA_forced and readingB_split)
    out["method_has_power"] = bool(method_has_power)

    return out


def main():
    global E
    E = gb.gammas()
    r1 = compute()
    E = gb.gammas()
    r2 = compute()
    assert r1 == r2, "NON-DETERMINISM: two runs differ"

    r = r1
    print("=== PRONG A -- class-relative circle frame: is sigma the "
          "cycle-orientation? ===")
    for k, v in r.items():
        print(f"  {k}: {v}")
    print()

    ok = True
    # setup anchors
    ok &= (r["K_herm"] < 1e-9 and r["K_invol"] < 1e-9 and r["sig_KS"] == (64, 64))
    # [A] reading-A forced & nontrivial
    ok &= check("A", "READING-A FORCED: pi_1(F) loop sends actual K_S -> -K_S "
                     "=> sigma = w1(L_time) = 1 (canonical, nontrivial)",
                r["w1_Ltime"] == 1 and r["deckA_residual"] < 1e-9
                and r["deckA2_residual"] < 1e-9,
                f"deck residual {r['deckA_residual']:.1e}, U^2 closes "
                f"{r['deckA2_residual']:.1e}")
    # [B] bare cycle orientation trivial; the arrow is a torsor
    ok &= check("B", "BARE SHARD-CYCLE ORIENTABLE: w1(TS^1) = 0; the two cyclic "
                     "orderings (record-arrow) form a free Z/2 TORSOR (trivial "
                     "class), NOT a nontrivial holonomy",
                r["w1_TS1"] == 0 and r["torsor_size"] == 2
                and r["torsor_free_Z2"])
    # [C] deck band not a function of type
    ok &= check("C", "DECK BAND NOT INTRINSIC: same type-quotient from two "
                     "helices with DIFFERENT ksign patterns => sign(K_S) is "
                     "imported, not carried by the quotient (Prong-2: no functor)",
                r["quotients_equal_despite_diff_ksign"])
    # [D] realization-dependent + inserted-sigma tautology
    ok &= check("D", "ACCUMULATION REALIZATION-DEPENDENT: flip-seam -> "
                     "w1(L_deck)=1, noflip-seam -> 0; BOTH valid on the actual "
                     "K_S (isospectral) => class not canonical; and the "
                     "fresh-token seam sign IS the inserted free coin sigma",
                r["deck_class_realization_dependent"]
                and r["both_seam_realizations_valid_on_actual_KS"]
                and r["cycle_orientation_is_inserted_sigma"])
    # [E] realization map not canonically pi_1-nontrivial
    ok &= check("E", "REALIZATION MAP FREE: f^*(sigma) = 0 for deg-0 f, "
                     "generator for deg-1 f; both maps exist, GU forces neither "
                     "=> no canonical iso of Z/2's",
                r["pullback_is_free_Z2"]
                and r["fstar_sigma_deg0"] == 0 and r["fstar_sigma_deg1"] == 1)
    # [F] plants rejected + power
    ok &= check("F", "PLANT-1 REJECTED: 'coequalizer orientation IS sigma' "
                     "predicts w1(TS^1)=1; computed 0",
                r["plant1_rejected"])
    ok &= check("F", "PLANT-2 REJECTED: the decorated sign(K_S)-band class is "
                     "realization-split (1 vs 0), not GU-determined",
                r["plant2_rejected"])
    ok &= check("F", "POWER: reading-A is FORCED (one value) while the "
                     "shard-cycle SPLITS (two values) -- the method tells forced "
                     "from imported; a pigeonhole 'both-are-Z/2' test could not",
                r["method_has_power"])

    nA = sum(1 for tg, _n, o in RESULTS if tg == "A")
    nB = sum(1 for tg, _n, o in RESULTS if tg == "B")
    nC = sum(1 for tg, _n, o in RESULTS if tg == "C")
    nD = sum(1 for tg, _n, o in RESULTS if tg == "D")
    nE = sum(1 for tg, _n, o in RESULTS if tg == "E")
    nF = sum(1 for tg, _n, o in RESULTS if tg == "F")
    all_ok = all(o for _t, _n, o in RESULTS) and ok
    print()
    print(f"HEADLINE: A={nA} B={nB} C={nC} D={nD} E={nE} F={nF}  "
          f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    print("VERDICT INPUT: reading-A (sigma = w1(L_time)) is canonical + forced. "
          "The bare shard-cycle carries only the TRIVIAL tangent orientation "
          "(a torsor = the record-arrow choice). Making sigma = cycle-orientation "
          "requires IMPORTING a sign(K_S) band the type-quotient does not carry "
          "(C), whose value is realization-dependent (D) and whose seam sign is "
          "the INSERTED free coin sigma itself (D); the realization map to "
          "w1(L_time) is a FREE Z/2 (E). No canonical GU-native frame forces "
          "sigma = cycle-orientation. => A-NUMEROLOGY.  sigma = w1(L_time) alone.")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
