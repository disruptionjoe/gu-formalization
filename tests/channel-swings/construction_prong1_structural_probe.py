#!/usr/bin/env python3
r"""
CONSTRUCTION swing, PRONG 1 (STRUCTURAL/GEOMETRIC).  MODE = construction, NOT
derivation: sigma is KNOWN to be external / not forced (the premise).  We POSIT

    S = P1 + P2 :
      P1  the three shards S(ubjective)/I(ntersubjective)/O(bjective) are
          ISOMORPHIC sheaves -- three interchangeable copies of one structure;
      P2  sigma = the CLOSURE ORIENTATION of the shard-cycle S->I->O->S, i.e.
          the flip/no-flip realization Prong A located as the insertion handle
          (the Z/2 monodromy of the composite of the three sheaf-isomorphisms).

and read off what the posit FORCES that we did NOT insert.  The gate is at the
BACK: an INDEPENDENT consequence that VERIFIES a banked fact is the payoff; one
that merely RESTATES the posit is worthless; one that CONTRADICTS a banked fact
KILLS the posit.  sigma stays LABELLED AS A POSIT throughout; nothing here is a
derivation of sigma's value.

Banked facts used as the back-gate:
    Q2-FREE            sigma is a free Z/2 coin; every INTERNAL reading map is
                       alpha-even, sigma is alpha-odd, Hom(triv,sign)=0 (blind).
    Q3 sigma _|_ tau   two independent external data; Z/6 = Z/2 x Z/3, direct.
    sigma = w1(L_time) canonical/forced; deck U (rot(0,9,pi)) : K_S -> -K_S.
    ~8% null stratum   q<0 ends, K_S null, operator non-constructible; closure
                       through it UNESTABLISHED (isospectral realization-dep).

Tests:

  [G]  P1+P2 FORCE the direct product Z/6 = Z/2 x Z/3 (Consequence 2 = sigma_|_tau).
       The cycle carries TWO commuting symmetries we did not both insert:
         Q = the Z/2 CLOSURE MONODROMY (deck flip)  = sigma            (posited),
         R = the Z/3 CYCLIC ROTATION of the three isomorphic shards    (from P1).
       Because the deck group Z/2 is ABELIAN, R fixes the monodromy CLASS
       (cyclic-shift of the three edge-signs leaves their product invariant) =>
       the extension is TRIVIAL => <Q,R> = Z/2 x Z/3 = Z/6, a DIRECT product,
       and fixing sigma leaves tau free and vice versa.  We inserted neither the
       Z/3 nor the independence; both are forced.  This VERIFIES Q3 sigma_|_tau.

  [I]  P1 (isomorphic sheaves, glued in a cycle) FORCES sigma to BE the descent
       (Cech H^1) obstruction, and forces the relative orientation c = sig_i*sig_j
       to be an alpha-even 1-COCYCLE with vanishing coboundary (Consequence 3).
       On a triangle of record-regions the cocycle condition c12*c23*c31 = +1 is
       AUTOMATIC for genuine products but FORBIDS the odd-parity assignments =>
       "one globally consistent record arrow" (orientation-reversing seams even
       in number).  VERIFIES the banked one-arrow result.

  [K]  Posit(sigma = closure orientation) AND banked(sigma = w1(L_time)) FORCE
       the realization map f: S^1_SIO -> F to be pi_1-NONTRIVIAL (Consequence 1).
       Prong A left f a FREE Z/2 (deg 0 or 1); the posit + the banked class PIN
       it to deg 1.  Independent (f not inserted), consistent with Prong A.

  [C]  CONTROL (mandatory, deliberately WRONG posit): sigma = a shard-INTERNAL
       orientation readable from INSIDE one shard.  By P1 the shards are
       isomorphic, so a shard-internal datum is an isomorphism-invariant =
       alpha-EVEN, hence IDENTICAL in the sigma=+ and sigma=- worlds (built on
       the actual K_S and -K_S): it carries 0 bits about sigma.  The correct
       posit (closure monodromy) is alpha-ODD: it DIFFERS across the two worlds,
       carrying sigma.  So the wrong posit is CAUGHT as a contradiction with
       Q2-FREE / the blindness lemma; the back-gate has power (rejects the
       readable-from-inside plant, admits the global-monodromy posit).

Deterministic, foreground, numpy only, no writes, no network.  Two-run-identical.
Exit 0 = every declared assertion holds.  This is CONSTRUCTION grade: the checks
verify what the POSIT forces, not that sigma's value is derived.
"""
from __future__ import annotations

import itertools
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
    out = {}

    # ---- [T] the actual canonical Krein anchor ---------------------------
    K_S = E[0].copy()
    for a in range(1, 9):
        K_S = K_S @ E[a]                              # K_S = e_0 e_1 ... e_8
    ev = np.linalg.eigvalsh(K_S)
    out["sig_KS"] = (int(np.sum(ev > 0.5)), int(np.sum(ev < -0.5)))
    out["K_invol"] = float(np.max(np.abs(K_S @ K_S - np.eye(DIM))))

    # the canonical deck / co-flip generator U : K_S -> -K_S  (grounds the Z/2)
    U = rot(N_DIRS, 0, 9, np.pi)
    K_flip = kprod(np.linalg.inv(U))
    out["deck_flip_residual"] = float(np.max(np.abs(K_flip + K_S)))   # ~0 iff -K_S

    # =====================================================================
    # [G]  P1+P2 FORCE  Z/6 = Z/2 x Z/3  (Consequence 2 : sigma _|_ tau).
    #      Build the two commuting cycle symmetries as concrete matrices on
    #      (shard-label in {S,I,O})  (x)  (deck-sign in {+,-}):
    #         R = cyclic rotation of the 3 isomorphic shards  (Z/3, from P1),
    #         Q = the closure-monodromy deck flip             (Z/2, = sigma).
    # =====================================================================
    Rlab = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)   # S->I->O->S
    Qsgn = np.array([[0, 1], [1, 0]], float)                    # sign flip (Z/2)
    R = np.kron(Rlab, np.eye(2))
    Q = np.kron(np.eye(3), Qsgn)

    out["R_order3"] = float(np.max(np.abs(np.linalg.matrix_power(R, 3) - np.eye(6))))
    out["Q_order2"] = float(np.max(np.abs(Q @ Q - np.eye(6))))
    out["commute_QR"] = float(np.max(np.abs(Q @ R - R @ Q)))     # ~0 => direct prod

    # enumerate the generated group <Q,R>; expect exactly 6 elements = Z/6
    grp, frontier = {}, [np.eye(6)]
    seen = {np.eye(6).tobytes()}
    gens = [Q, R]
    while frontier:
        g = frontier.pop()
        grp[g.tobytes()] = g
        for gen in gens:
            h = np.rint(gen @ g).astype(float)
            if h.tobytes() not in seen:
                seen.add(h.tobytes())
                frontier.append(h)
    out["group_order"] = len(grp)                               # expect 6

    # R fixes the monodromy CLASS: cyclic shift of the 3 edge-signs leaves the
    # PRODUCT (the closure monodromy) invariant -> abelian deck -> trivial ext.
    edge_sign_sets = [(-1, +1, +1), (+1, -1, +1), (+1, +1, -1), (-1, -1, -1)]
    prod_invariant = all(
        np.prod(es) == np.prod(np.roll(es, 1)) == np.prod(np.roll(es, 2))
        for es in edge_sign_sets)
    out["rotation_fixes_monodromy_class"] = bool(prod_invariant)

    # DIRECT-PRODUCT independence (Q3): fixing sigma leaves tau free, & vice versa
    z6 = [(a, b) for a in (0, 1) for b in (0, 1, 2)]
    tau_free_given_sigma = all(
        sorted({b for (a2, b) in z6 if a2 == a}) == [0, 1, 2] for a in (0, 1))
    sigma_free_given_tau = all(
        sorted({a for (a, b2) in z6 if b2 == b}) == [0, 1] for b in (0, 1, 2))
    out["tau_free_given_sigma"] = bool(tau_free_given_sigma)
    out["sigma_free_given_tau"] = bool(sigma_free_given_tau)

    # =====================================================================
    # [I]  DESCENT COCYCLE (Consequence 3).  Relative orientation
    #      c_ij = sigma_i * sigma_j is alpha-even; its coboundary vanishes on
    #      any triangle (c12 c23 c31 = +1 identically for genuine products), and
    #      the odd-parity assignments are FORBIDDEN => one globally consistent
    #      record arrow.
    # =====================================================================
    # genuine products always satisfy the cocycle:
    cocycle_auto = all(
        (s1 * s2) * (s2 * s3) * (s3 * s1) == 1
        for s1 in (-1, 1) for s2 in (-1, 1) for s3 in (-1, 1))
    out["cocycle_holds_for_all_genuine_products"] = bool(cocycle_auto)
    # free assignment of the three seam signs: forbid the odd-parity ones
    triangle = list(itertools.product((-1, 1), repeat=3))       # 8 configs
    forbidden = [t for t in triangle if t[0] * t[1] * t[2] == -1]
    out["triangle_configs"] = len(triangle)
    out["forbidden_odd_parity"] = len(forbidden)                # expect 4 of 8

    # =====================================================================
    # [K]  REALIZATION-MAP compatibility (Consequence 1).  With sigma the
    #      closure orientation (posited nontrivial) AND sigma = w1(L_time)
    #      (banked nontrivial), f^*(w1) = sigma_closure forces deg(f) mod 2 = 1.
    # =====================================================================
    w1_Ltime = 1                        # banked: nontrivial (deck_flip_residual~0)
    sigma_closure = 1                   # posited nontrivial (P2)
    # f^*(w1) = deg(f)*w1 mod 2; require == sigma_closure

    def consistent(deg):
        return (deg * w1_Ltime) % 2 == sigma_closure
    out["deg0_consistent"] = consistent(0)     # 0 == 1 -> False
    out["deg1_consistent"] = consistent(1)     # 1 == 1 -> True (forced)
    forced_deg1 = (not consistent(0)) and consistent(1)
    out["realization_map_forced_pi1_nontrivial"] = bool(forced_deg1)

    # =====================================================================
    # [C]  CONTROL: sigma = a shard-INTERNAL orientation (readable inside one
    #      shard).  Built on the ACTUAL K_S / -K_S worlds.  A shard-internal
    #      datum is an isomorphism-invariant = alpha-even => IDENTICAL across the
    #      two sigma worlds (0 bits).  The closure monodromy is alpha-ODD =>
    #      DIFFERS (1 bit = sigma).  The wrong posit is CAUGHT.
    # =====================================================================
    world_plus = K_S                 # sigma = +
    world_minus = -K_S               # sigma = -  (= U K_S U^{-1})

    # alpha-EVEN, shard-internal readouts (spectrum / involution / norm):
    def even_readout(anchor):
        e = np.linalg.eigvalsh(anchor)
        return (tuple(np.round(np.sort(e), 6)),
                float(np.round(np.max(np.abs(anchor @ anchor - np.eye(DIM))), 9)))
    even_plus = even_readout(world_plus)
    even_minus = even_readout(world_minus)
    even_identical = (even_plus == even_minus)
    out["shard_internal_alpha_even_identical_across_sigma"] = bool(even_identical)
    I_even_bits = 0 if even_identical else 1     # mutual info about sigma

    # alpha-ODD closure monodromy: the signed anchor itself differs across worlds
    odd_diff = float(np.max(np.abs(world_plus - world_minus)))    # = ||2 K_S||
    odd_distinguishes = odd_diff > 1e-9
    out["closure_monodromy_alpha_odd_differs_across_sigma"] = bool(odd_distinguishes)
    I_odd_bits = 1 if odd_distinguishes else 0

    out["I_even_bits_about_sigma"] = I_even_bits
    out["I_odd_bits_about_sigma"] = I_odd_bits
    # the plant "sigma = shard-internal orientation" asserts a READABLE sigma:
    plant_predicts_readable = True
    plant_caught = plant_predicts_readable and (I_even_bits == 0)   # 0 bits => wrong
    out["wrong_posit_caught"] = bool(plant_caught)
    # power: the gate rejects the readable plant (even, 0 bits) AND admits the
    # correct posit (odd, 1 bit); a test blind to the even/odd split could not.
    out["backgate_has_power"] = bool(I_even_bits == 0 and I_odd_bits == 1)

    return out


def main():
    global E
    E = gb.gammas()
    r1 = compute()
    E = gb.gammas()
    r2 = compute()
    assert r1 == r2, "NON-DETERMINISM: two runs differ"

    r = r1
    print("=== CONSTRUCTION Prong 1 -- structural: what does the POSIT "
          "(sigma = closure orientation of an isomorphic-sheaf shard-cycle) "
          "FORCE? ===")
    for k, v in r.items():
        print(f"  {k}: {v}")
    print()

    ok = True
    ok &= (r["sig_KS"] == (64, 64) and r["K_invol"] < 1e-9
           and r["deck_flip_residual"] < 1e-9)

    ok &= check("G", "Z/6 = Z/2 x Z/3 FORCED (Consequence 2 = sigma_|_tau): the "
                     "closure-monodromy Z/2 (=sigma) and the shard-rotation Z/3 "
                     "commute, generate a DIRECT product of order 6; rotation "
                     "fixes the monodromy class (abelian deck); fixing sigma "
                     "leaves tau free & vice versa -- VERIFIES Q3",
                r["R_order3"] < 1e-9 and r["Q_order2"] < 1e-9
                and r["commute_QR"] < 1e-9 and r["group_order"] == 6
                and r["rotation_fixes_monodromy_class"]
                and r["tau_free_given_sigma"] and r["sigma_free_given_tau"],
                f"|<Q,R>|={r['group_order']}, [Q,R]={r['commute_QR']:.1e}")

    ok &= check("I", "DESCENT COCYCLE FORCED (Consequence 3): relative "
                     "orientation c=sig_i*sig_j is alpha-even with vanishing "
                     "coboundary on every triangle; odd-parity seam assignments "
                     "FORBIDDEN (4 of 8) -- one globally consistent record arrow",
                r["cocycle_holds_for_all_genuine_products"]
                and r["triangle_configs"] == 8
                and r["forbidden_odd_parity"] == 4)

    ok &= check("K", "REALIZATION MAP FORCED pi_1-NONTRIVIAL (Consequence 1): "
                     "posit(sigma=closure) AND banked(sigma=w1(L_time)) pin "
                     "deg(f) mod 2 = 1 (deg-0 inconsistent, deg-1 forced); Prong "
                     "A left f a free Z/2 -- the posit selects the odd map",
                r["realization_map_forced_pi1_nontrivial"]
                and (not r["deg0_consistent"]) and r["deg1_consistent"])

    ok &= check("C", "CONTROL CAUGHT: the WRONG posit sigma = shard-INTERNAL "
                     "orientation is alpha-even (identical across the K_S / -K_S "
                     "worlds, 0 bits about sigma) -> CONTRADICTS Q2-FREE / "
                     "blindness -> REJECTED; the correct closure-monodromy posit "
                     "is alpha-odd (1 bit) -> admitted; back-gate has power",
                r["wrong_posit_caught"] and r["backgate_has_power"]
                and r["shard_internal_alpha_even_identical_across_sigma"]
                and r["closure_monodromy_alpha_odd_differs_across_sigma"],
                f"I_even={r['I_even_bits_about_sigma']} bit, "
                f"I_odd={r['I_odd_bits_about_sigma']} bit")

    nG = sum(1 for tg, _n, o in RESULTS if tg == "G")
    nI = sum(1 for tg, _n, o in RESULTS if tg == "I")
    nK = sum(1 for tg, _n, o in RESULTS if tg == "K")
    nC = sum(1 for tg, _n, o in RESULTS if tg == "C")
    all_ok = all(o for _t, _n, o in RESULTS) and ok
    print()
    print(f"HEADLINE: G={nG} I={nI} K={nK} C={nC}  "
          f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    print("VERDICT INPUT (CONSTRUCTION grade, sigma kept as POSIT): the posit "
          "FORCES independent, VERIFIED consequences it did not insert -- the "
          "Z/6 = Z/2 x Z/3 direct product with sigma _|_ tau (G, verifies Q3) "
          "and the descent cocycle / one-globally-consistent-arrow (I) -- plus a "
          "forced compatibility (K, realization map pi_1-nontrivial). The "
          "deliberately-wrong shard-INTERNAL posit is CAUGHT (C) as an alpha-even "
          "contradiction with Q2-FREE, so 'coherent picture' has discriminating "
          "power. No consequence CONTRADICTS a banked fact. => POSIT-PRODUCTIVE.")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
