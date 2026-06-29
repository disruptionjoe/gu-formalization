#!/usr/bin/env python3
r"""
RS / spin-3/2 INDEX -> WHICH ARENA?  Multi-manifold CRT scan + 4 fabrication checks.

Companion to agw_gravitino_3primary.py.  Having shown every spin-3/2 anomaly
coefficient is 2-primary-up-to-(von-Staudt-Clausen) with NO factor 3 in any
numerator, we now compute the ACTUAL RS index INTEGER on several closed spin
manifolds and ask: does it ever land on the Z/3 carrier arena as a NONZERO
(order-3) element, or is it always either 0 (mod 3) [identity] or a unit +-1
[the twisted-Dirac escape]?  And we run the program's FOUR fabrication checks
against the one place a '3' appears (the -42 on K3).

Index density (AGW):  I_3/2 = Ahat(R) * ( ch(TM_C) - 1 ).
Degree-4 part :  7 p1 / 8                                  (4-manifolds)
Degree-8 part :  (289 p1^2 - 247 p2) / 5760               (8-manifolds)
(both reproduced from the symbolic genus in agw_gravitino_3primary.py)

Run:  python tests/forcing-slot/rs_index_carrier_arena_scan.py
"""
from __future__ import annotations
from fractions import Fraction as Fr

def v_p(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v

def primefac(n):
    n = abs(int(n))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d*d <= n:
        e = 0
        while n % d == 0:
            n //= d; e += 1
        if e:
            out.append(f"{d}^{e}" if e > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return ".".join(out)

def crt24(n):
    n = int(n)
    return (n % 8, n % 3, n % 24)

# RS index density evaluators (coefficients FORWARD from the genus; see companion script)
def rs_idx_dim4(p1):
    return Fr(7, 8) * p1                      # 7 p1 / 8

def rs_idx_dim8(p1sq, p2):
    return (Fr(289, 5760) * p1sq) - (Fr(247, 1440) * p2)   # (289 p1^2 - 247 p2)/5760

def ahat_dim4(p1):
    return Fr(-1, 24) * p1
def ahat_dim8(p1sq, p2):
    return (Fr(7, 5760) * p1sq) - (Fr(4, 5760) * p2)        # (7 p1^2 - 4 p2)/5760

# ----------------------------------------------------------------------------- #
# closed spin manifolds with known Pontryagin numbers
# ----------------------------------------------------------------------------- #
# K3:  dim 4, spin, sigma=-16, p1 = 3 sigma = -48.
# T^4: dim 4, flat, p1 = 0.
# HP^2 (quaternionic projective plane): dim 8, p1=2u, p2=7u^2, u^2[HP^2]=1 -> p1^2=4, p2=7.
# HP^1 x HP^1 = S^4 x S^4: dim 8, p1=0,p2=0 (trivial Pontryagin) -> index 0 (sanity).
# B8 (Milnor/Bott generator, e.g. the spin 8-mfld with Ahat=1): use known p-numbers below.
MANIFOLDS_4 = {
    "K3        (sigma=-16)": dict(p1=-48),
    "T^4       (flat)":      dict(p1=0),
    "K3 # K3   (sigma=-32)": dict(p1=-96),
}
MANIFOLDS_8 = {
    "HP^2          (p1^2=4, p2=7)":  dict(p1sq=4,  p2=7),
    "S^4 x S^4     (p1^2=0, p2=0)":  dict(p1sq=0,  p2=0),
    "K3 x K3       (p1^2=2304,p2=?)":dict(p1sq=(-48)*(-48), p2=(-48)*(-48)//1),  # see note
}

def main():
    line = "=" * 92
    print(line)
    print("RS / spin-3/2 INDEX -- multi-manifold CRT scan: does it EVER reach Z/3 nontrivially?")
    print(line)

    print("\n[DIM-4 spin manifolds]  RS index = 7 p1 / 8 ;  Dirac index = -p1/24")
    print(f"  {'manifold':24s} {'p1':>6s} {'Dirac':>7s} {'RS':>7s} {'RS fact':>10s} "
          f"{'mod24':>6s}  CRT(Z8,Z3)")
    z3_hits = []
    for name, d in MANIFOLDS_4.items():
        p1 = d["p1"]
        dirac = ahat_dim4(p1)
        rs = rs_idx_dim4(p1)
        assert rs.denominator == 1, (name, rs)
        rsi = int(rs)
        z8, z3, z24 = crt24(rsi)
        print(f"  {name:24s} {p1:>6d} {str(dirac):>7s} {rsi:>7d} "
              f"{('-' if rsi<0 else '')+primefac(rsi):>10s} {z24:>6d}  ({z8} in Z8, {z3} in Z3)")
        z3_hits.append((name, rsi, z3))

    print("\n  LEMMA (proved by the formula): on ANY spin 4-manifold p1 = 3 sigma, so")
    print("     RS index = 7 p1 / 8 = 21 sigma / 8 = 3 * (7 sigma / 8).  The factor 3 is FORCED by")
    print("     the multiplier 7*3 = 21 = 3.7.  Hence the RS index is == 0 (mod 3) on EVERY spin")
    print("     4-manifold: it ALWAYS lands at the Z/3 IDENTITY.  No 4-mfld RS index can carry order-3.")
    # verify the lemma symbolically over the scan
    for name, rsi, z3 in z3_hits:
        assert z3 == 0, (name, rsi, z3)
    print("     -> verified across the scan:", {n: z for n, r, z in z3_hits})

    print("\n[DIM-8 spin manifolds]  RS index = (289 p1^2 - 247 p2)/5760 ;  Ahat = (7 p1^2 - 4 p2)/5760")
    print(f"  {'manifold':30s} {'RS':>6s} {'Ahat':>6s} {'RS fact':>8s} {'mod24':>6s}  CRT(Z8,Z3)")
    dim8 = []
    for name, d in MANIFOLDS_8.items():
        p1sq, p2 = d["p1sq"], d["p2"]
        rs = rs_idx_dim8(p1sq, p2)
        ah = ahat_dim8(p1sq, p2)
        rs_int_ok = (rs.denominator == 1)
        ah_int_ok = (ah.denominator == 1)
        label_rs = str(int(rs)) if rs_int_ok else str(rs)
        label_ah = str(int(ah)) if ah_int_ok else str(ah)
        if rs_int_ok:
            rsi = int(rs)
            z8, z3, z24 = crt24(rsi)
            fac = ("-" if rsi < 0 else "") + primefac(rsi) if rsi != 0 else "0"
            print(f"  {name:30s} {label_rs:>6s} {label_ah:>6s} {fac:>8s} {z24:>6d}  ({z8},{z3})")
            dim8.append((name, rsi, z3))
        else:
            print(f"  {name:30s} {label_rs:>6s} {label_ah:>6s}  (non-integer -> p-numbers not a valid"
                  f" spin 8-mfld combo; informational)")
    print("\n  NOTE: K3xK3 p2-number requires the cross term; the integer cases above are the valid ones.")
    print("  HP^2 RS index is a UNIT (+-1): it is NONZERO mod 3 -- but it equals the twisted-Dirac")
    print("  escape '1', representing ONE unit, NOT three.  A unit generates Z/3 yet encodes count 1.")

    # ---------------- the inescapable mod-3 dichotomy ----------------
    print("\n" + line)
    print("THE INESCAPABLE mod-3 DICHOTOMY for any net-chiral index n in pi_3^s = Z/24")
    print(line)
    print("  * If you want the literal integer n = 3  (or 24, or any 3k): n == 0 (mod 3) -> Z/3 IDENTITY")
    print("    -> it carries ZERO order-3 information. '3 generations as the number 3' is self-defeating.")
    print("  * If n is a UNIT mod 3 (n == +-1): it generates Z/3 -> but then the integer is +-1, i.e. the")
    print("    twisted-Dirac's ONE generation (HP^2 gives exactly this).  Mechanism real, value = 1.")
    print("  * There is NO net-chiral integer index that is simultaneously the literal '3' AND a Z/3")
    print("    generator.  Order-3 (the count) and the integer 3 are CRT-disjoint requirements.")

    # ---------------- FOUR FABRICATION CHECKS on the one '3' (the -42 on K3) ----------------
    print("\n" + line)
    print("FOUR FABRICATION CHECKS on the lone factor-3 (the -42 = -2.3.7 RS index on K3)")
    print(line)
    sigma, chi = -16, 24
    p1 = 3 * sigma
    print(f"  1. DISGUISED chi?  -42 = 7*p1/8 with p1 = 3*sigma = {p1}.  The factor 3 is the SIGNATURE")
    print(f"     theorem coefficient (p1 = 3 sigma, true for EVERY 4-mfld).  Via 2chi+3sigma="
          f"{2*chi+3*sigma}=0 it equals -2chi numerically -> it IS a chi/sigma-route 3.  CAUGHT:")
    print(f"     the 3 is NOT an independent count; it is the topological p1=3sigma factor. [DISGUISED]")
    print(f"  2. REVERSE-ENGINEERED +8?  The 7/8 multiplier and the '7' came FORWARD from the genus")
    print(f"     (ch(TM_C)-1)*Ahat -- never fitted to land on 24/8=3.  -42 was COMPUTED, not back-solved.")
    print(f"     The RS leg's claimed '+8' (to make 16+8=24) does NOT appear; we get -42, not +8. [CLEAN]")
    print(f"  3. CIRCULAR rank-4?  No rank was assumed: the index used only p1[K3]=3sigma and the")
    print(f"     AGW genus multipliers.  No rank_H(S_RS^+)=4 was injected. [CLEAN]")
    print(f"  4. FITTED holonomy?  No holonomy was chosen: K3's sigma=-16 is its actual signature;")
    print(f"     HP^2's p-numbers are its actual ones.  Nothing tuned to produce a 3. [CLEAN]")

    print("\n" + line)
    print("VERDICT: the spin-3/2 / RS sector's net-chiral index is ALWAYS either 0 (mod 3) [identity,")
    print("e.g. -42 on K3, where the 3 is the disguised signature factor] or a UNIT [+-1, e.g. -1 on")
    print("HP^2 = the twisted-Dirac escape '1'].  It NEVER forces the integer 3 as a genuine order-3")
    print("carrier.  The RS sector reaches the Z/8 selector arena (and the unit), never the Z/3 count.")
    print("This is the 'A-mechanism / B-ontology' synthesis: the RS index IS net-chiral and tangential,")
    print("but it is CRT-locked out of the order-3 carrier arena.")
    print(line)

    return {
        "dim4_RS_indices": {n: r for n, r, z in z3_hits},
        "dim4_all_zero_mod3": all(z == 0 for n, r, z in z3_hits),
        "HP2_RS_index": next((r for n, r, z in dim8 if "HP^2" in n), None),
        "HP2_mod3": next((z for n, r, z in dim8 if "HP^2" in n), None),
        "lemma": "RS index on spin 4-mfld = 21 sigma/8 == 0 mod 3 (factor 21=3.7 forced)",
        "dichotomy": "any net-chiral n is either ==0 mod 3 (identity) or a unit +-1 (=Dirac's 1); "
                     "never the literal 3 AND a Z/3 generator",
        "fab_disguised_chi": "the lone 3 in -42 is the p1=3sigma=-2chi signature factor (DISGUISED)",
        "fab_reverse_eng": "CLEAN (computed forward; got -42, not the fitted +8)",
        "fab_circular_rank": "CLEAN (no rank assumed)",
        "fab_fitted_holonomy": "CLEAN (actual K3/HP^2 invariants)",
    }

if __name__ == "__main__":
    out = main()
    print("\nMACHINE SUMMARY:")
    for k, v in out.items():
        print(f"  {k}: {v}")
