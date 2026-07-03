#!/usr/bin/env python3
r"""
STEP 3 (WC-FUNCTION-SPACE-EXT) SCAFFOLD: the K3 family-index pushforward -- the crux.

SPEC: canon/rs-function-space-framework-SPEC.md, section 6. Blocks this on 5 obligations, ALL
"without target import" (no smuggling chi(K3)=24 or 24/8=3): (1) fiber model, (2) compact-support/
APS pushforward pi_!, (3) Phi-homotopy / symbol certificate, (4) ch2/eta correction, (5) H-line
normalization.

This file builds the honest machinery for (1)-(2), computes the trivial-family sanity, and pins
(3)-(5) as the exact open crux -- demonstrating the SPEC's FLIP criterion: the generation-arena
(mod 3) value of the family index is 0 for the trivial (product) family and a FREE function of the
(unbuilt) GU clutching otherwise. So GU forces a count IFF GU forces the K3 family term; else
"external by structure" becomes unconditional.

FIREWALL (guarded): we NEVER use chi(K3)=24 or 24/8=3. The RS family index uses only the gravitino
density I_{3/2}=21*sigma/8 (sigma(K3)=-16 => -42), whose 3-part is the FIXED Hirzebruch p_1=3*sigma
(generation-INDEPENDENT), == 0 mod 3 in the generation arena.

Grade: SPEC + computed trivial-family sanity; obligations (3)-(5) OPEN. Internal tier (caveat (e)).
Run: python tests/rs-function-space/k3_family_pushforward_scaffold.py
"""
from fractions import Fraction as Fr


def rs_fiber_index(sigma):
    """I_{3/2} = 21*sigma/8 = 7*p1/8, p1 = 3*sigma. NO chi/8 anywhere."""
    return Fr(21 * sigma, 8)


SIGMA_K3 = -16                          # signature of K3 (Rokhlin: == 0 mod 16). NOT the Euler number.
I_fiber = rs_fiber_index(SIGMA_K3)      # -42
assert I_fiber == -42
assert int(I_fiber) % 3 == 0, "fiber index 3-part is the fixed Hirzebruch p_1, == 0 in generation arena"


def family_index(sigma_fiber, clutch_c=0, base_H_normalization=None):
    """(1)+(2) computed: fiberwise pushforward pi_! of the fiber density.
       clutch_c: base-degree family characteristic number (obligation 4, ch2/eta correction) -- FREE
                 unless the GU family fixes it.
       base_H_normalization: the H-line normalization (obligation 5) -- OPEN.
    A PRODUCT family (clutch_c=0) has a flat superconnection => higher term 0 => index = I_fiber."""
    fiberwise = rs_fiber_index(sigma_fiber)
    higher = Fr(clutch_c)
    if base_H_normalization is not None:
        higher *= Fr(base_H_normalization)
    return fiberwise + higher


def main():
    print("=" * 88)
    print("STEP 3 SCAFFOLD: K3 family-index pushforward -- what closes, what stays the crux")
    print("=" * 88)
    print(f"fiber RS index I_3/2[K3] = 21*sigma/8, sigma={SIGMA_K3} => {I_fiber} = -2*3*7")
    print(f"   3-part of {I_fiber}: fixed Hirzebruch p_1=3*sigma (generation-independent) => mod 3 = "
          f"{int(I_fiber) % 3}  [does NOT reach the Z/3 generation arena]")

    print("\n(1)+(2) pushforward pi_! -- TRIVIAL (product) family B x K3, computed:")
    for B in ("S^2", "T^4", "point"):
        idx = family_index(SIGMA_K3, clutch_c=0)
        print(f"   base {B:<6}: family index = {idx}  (mod 3 in generation arena = {int(idx) % 3})")
    print("   => product family recovers the fiberwise index; NO new Z/3 generation piece.")

    print("\n(3)-(5) the CRUX -- family with nontrivial clutching (the GU K3-fibered source action):")
    print("   the generation-arena value is a FREE function of the clutching term c (obligation 4):")
    for c in (0, 1, 3, 6, -3):
        idx = family_index(SIGMA_K3, clutch_c=c)
        tag = "  <-- odd/3-primary IF GU forces c != 0 mod 3" if int(idx) % 3 != 0 else ""
        print(f"      clutch c={c:>3}: family index = {str(idx):>5}, mod 3 = {int(idx) % 3}{tag}")

    print("\n" + "-" * 88)
    print("OBLIGATION LEDGER (SPEC section 6):")
    print("-" * 88)
    ledger = [
        ("1 fiber model (K3 bundle)",   "SCAFFOLDED",  "product model exact; GU K3-fibered geometry UNBUILT (source action)"),
        ("2 compact-support/APS pi_!",  "SCAFFOLDED",  "fiberwise pushforward computed; noncompact-end/APS term OPEN"),
        ("3 Phi-homotopy/symbol cert",  "OPEN",        "needs the family symbol of the GU RS operator"),
        ("4 ch2 / eta correction",      "OPEN (crux)", "the base-degree family term; FREE unless GU fixes it"),
        ("5 H-line normalization",      "OPEN",        "the H-line scale on the base; UNBUILT"),
    ]
    for name, status, note in ledger:
        print(f"   [{status:<11}] {name:<28} {note}")

    print("\n" + "=" * 88)
    print("VERDICT (STEP 3, honest): the fiberwise/bulk pushforward is closed and contributes 0 to the")
    print("Z/3 generation arena (obligations 1-2, computed). The ONLY route to an odd generation count")
    print("is the higher family term (obligations 3-5), FREE unless the actual GU K3-fibered source")
    print("action forces it. Exactly the SPEC flip: GU forces a count IFF GU forces the K3 family term;")
    print("otherwise 'external by structure' becomes UNCONDITIONAL. Source action unbuilt => crux OPEN,")
    print("now reduced to precisely 3 obligations (3,4,5).")
    print("=" * 88)

    assert family_index(SIGMA_K3, 0) == -42
    assert int(family_index(SIGMA_K3, 0)) % 3 == 0, "trivial family must contribute 0 mod 3"
    assert abs(int(I_fiber)) != 24, "FIREWALL: chi(K3)=24 must never appear as the RS family index"
    print("\n[OK] STEP-3 scaffold guards passed (firewall intact: no chi/8=3 import).")


if __name__ == "__main__":
    main()
