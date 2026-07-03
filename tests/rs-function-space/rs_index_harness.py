#!/usr/bin/env python3
# Reusable characteristic-class / RS-index harness for the WC-FUNCTION-SPACE-EXT program.
# Foundation for: the BULK index (Step 2), and the K3 FAMILY index (Step 3). Exact rational
# arithmetic (fractions). Grounded in and cross-checked against the repo's canon values
# (canon/forcing-slot-toy-rs-RESULTS.md): spin-1/2 Dirac index on K3 = 2; spin-3/2 (AGW gravitino/
# Rarita-Schwinger) index on K3 = -42; K3#K3 = -84; T^4 = 0; twisted-by-16 = -672; all == 0 mod 3.
#
# Formulas (4-manifold X, spin): signature sigma, Euler chi, p1 = 3*sigma (Hirzebruch),
#   A-hat[X]         = -sigma/8            (= -p1/24)   -- spin-1/2 Dirac index
#   I_{3/2}[X]       = 21*sigma/8          (= 7*p1/8)   -- spin-3/2 (gravitino/RS) index
#   I_{3/2, twist V} = dim(V)*I_{3/2}[X] + 3*ch2(V)     (V flat => ch2=0)
# Rokhlin (spin 4-manifold): sigma == 0 mod 16, so I_{3/2} = 21*sigma/8 = 42k -> ALWAYS == 0 mod 3.
from fractions import Fraction as F

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m


class FourManifold:
    def __init__(self, name, chi, sigma, spin=True):
        self.name, self.chi, self.sigma, self.spin = name, chi, sigma, spin
        self.p1 = 3 * sigma                                   # Hirzebruch signature theorem

    def a_hat(self):                                          # spin-1/2 Dirac index
        return F(-self.sigma, 8)

    def rs_index(self):                                       # spin-3/2 gravitino/RS index = 7 p1/8
        return F(21 * self.sigma, 8)

    def rs_index_twisted(self, dimV, ch2V=0):
        return dimV * self.rs_index() + 3 * F(ch2V)


MANIFOLDS = [
    FourManifold("K3", 24, -16),
    FourManifold("T^4", 0, 0),
    FourManifold("K3#K3", 46, -32),
    FourManifold("S2xS2", 4, 0),
    FourManifold("CP2", 3, 1, spin=False),                   # NOT spin (sigma=1): Dirac not defined
]

print("=" * 90)
print("RS-index harness: A-hat (spin-1/2), I_{3/2} (spin-3/2/gravitino), and the CRT mod-24 arena")
print("=" * 90)
print("  %-8s %5s %6s %6s | %8s %10s %8s %s" %
      ("X", "chi", "sigma", "p1", "A-hat", "I_3/2", "I mod24", "CRT (Z/8, Z/3)"))
for M in MANIFOLDS:
    ah, rs = M.a_hat(), M.rs_index()
    if M.spin:
        m24 = int(rs) % 24
        crt = "(%d, %d)" % (m24 % 8, int(rs) % 3)
        print("  %-8s %5d %6d %6d | %8s %10s %8d %s%s" %
              (M.name, M.chi, M.sigma, M.p1, str(ah), str(rs), m24, crt,
               "" if int(rs) % 3 == 0 else "  <-- 3-PRIMARY!"))
    else:
        print("  %-8s %5d %6d %6d | %8s %10s   n/a  (not spin -- Dirac undefined)" %
              (M.name, M.chi, M.sigma, M.p1, str(ah), str(rs)))

print()
# --- cross-check against canon values -------------------------------------------------
K3 = MANIFOLDS[0]
check(K3.a_hat() == 2, "spin-1/2 Dirac index on K3 = A-hat = 2 (canon)")
check(K3.rs_index() == -42, "spin-3/2 RS index on K3 = -42 (canon)")
check(MANIFOLDS[1].rs_index() == 0, "spin-3/2 RS index on T^4 = 0 (canon)")
check(MANIFOLDS[2].rs_index() == -84, "spin-3/2 RS index on K3#K3 = -84 (canon)")
check(K3.rs_index_twisted(16, ch2V=0) == -672, "twisted-by-16 (flat) spin-3/2 on K3 = -672 (canon)")
print("  canon cross-checks pass: K3 A-hat=2, I_3/2=-42; T^4=0; K3#K3=-84; twist-16=-672")

# --- BULK-EVEN theorem: I_{3/2} == 0 mod 3 for EVERY spin 4-manifold (Rokhlin) ---------
print()
print("=" * 90)
print("BULK-EVEN: the RS bulk index is 2-primary (Z/8 arena), never 3-primary, for spin 4-manifolds")
print("=" * 90)
worst = 0
for k in range(-6, 7):                                        # Rokhlin: sigma = 16k for spin 4-manifolds
    Mk = FourManifold("spin(sigma=16k)", 0, 16 * k)
    rs = Mk.rs_index()
    check(rs == 42 * k, "I_3/2 = 21*sigma/8 = 42k for sigma=16k")
    check(int(rs) % 3 == 0, "I_3/2 == 0 mod 3 for every spin 4-manifold (sigma=16k)")
    # and every integer twist stays 0 mod 3
    for dimV in (1, 10, 16, 45):
        for ch2V in (-5, 0, 7, 12):
            tw = Mk.rs_index_twisted(dimV, ch2V)
            check(int(tw) % 3 == 0, "twisted I_3/2 == 0 mod 3 for every twist (dimV=%d)" % dimV)
            worst = max(worst, abs(int(tw) % 3))
check(worst == 0, "no twist ever reaches the Z/3 (generation) arena")
print("  I_{3/2} = 42k for sigma = 16k (Rokhlin), so I_{3/2} == 0 mod 3 identically;")
print("  every integer twist dim(V)*I_{3/2} + 3*ch2(V) stays == 0 mod 3.")
print("  => the bulk RS index NEVER carries a 3-primary (generation) piece: it lives entirely in")
print("     the Z/8 selector arena. The '3' in -42 = -2.3.7 is the fixed Hirzebruch p1=3*sigma,")
print("     generation-INDEPENDENT (identical for 1,3,5,... generations); not a count.")

# --- interface stub for Step 3 (K3 family index / pushforward) -------------------------
def family_index_pushforward_stub(fiber, base_ch2=None):
    """Step-3 interface: family index over a base with the given fiber. The fiberwise RS index
    integrates against ch of the index bundle; the K3-fiber pushforward (chi=24) plus the
    ch2/eta correction and H-line normalization go HERE, computed WITHOUT target import."""
    return {"status": "OPEN", "fiber_chi": fiber.chi, "fiber_rs_index": fiber.rs_index(),
            "note": "pushforward + ch2/eta correction + H-line normalization not yet computed"}


print()
print("#" * 90)
print("# HARNESS READY. Bulk (Step 2): I_{3/2}=21*sigma/8, 2-primary by Rokhlin -- DONE here.")
print("#  Family (Step 3): family_index_pushforward_stub() -- the K3 pushforward is the OPEN crux.")
print("#  hard asserts passed: %d" % NASSERT)
print("#" * 90)
