#!/usr/bin/env python3
"""AC-E1 independent recomputation: Omega^Spin_5(BG) via the Atiyah-Hirzebruch
spectral sequence, for the four global forms of the Standard Model gauge group
G_n = (SU(3) x SU(2) x U(1))/Z_n, n in {1,2,3,6}, plus controls.

METHOD (all inputs named; nothing fitted):

 (I1) Omega^Spin_j(pt) for j = 0..5 = Z, Z/2, Z/2, 0, Z, 0    [Milnor/ABP; standard]
 (I2) AHSS  E^2_{p,q} = H_p(X; Omega^Spin_q(pt)) ==> Omega^Spin_{p+q}(X)
 (I3) The two bottom d_2 differentials of the spin-bordism AHSS are duals of Sq^2:
        d_2 : E^2_{p,1} = H_p(X;Z/2) -> E^2_{p-2,2} = H_{p-2}(X;Z/2)   is (Sq^2)^dual
        d_2 : E^2_{p,0} = H_p(X;Z)   -> E^2_{p-2,1} = H_{p-2}(X;Z/2)   is rho_2 then (Sq^2)^dual
      [standard; this is the one IMPORTED lemma of the derivation]
 (I4) H^*(BG_n; Z) as a polynomial ring on Chern classes (Borel):
        n=1: BSU(3) x BSU(2) x BU(1)        Z[c2,c3] (x) Z[c2'] (x) Z[t]
        n=2: BSU(3) x BU(2)                 Z[c2,c3] (x) Z[c1',c2']
        n=3: BU(3)   x BSU(2)               Z[c1,c2,c3] (x) Z[c2']
        n=6: BS(U(3)xU(2))                  Z[c1,c2,c3,c1',c2']/(c1 + c1')
      All four are TORSION-FREE and concentrated in EVEN degree.
 (I5) Wu formula mod 2:  Sq^2(c_j) = c_1 c_j + (j-1) c_{j+1}.
      Sq^1 = 0 on every generator (mod-2 reduction of an integral class), hence
      Sq^1 = 0 on the whole algebra, hence Sq^2 is a DERIVATION here (Cartan).

The only E^2 entry in total degree 5 is (p,q) = (4,1); every other is checked zero.
So Omega^Spin_5(BG) = ker(d_2 out of E_{4,1}) / im(d_2 into E_{4,1}), an F_2 vector space.

Exit 0 on all asserts.
"""
from __future__ import annotations
from itertools import product

# ---------------------------------------------------------------- mod-2 algebra

class Alg:
    """Z/2 polynomial algebra on named even-degree generators, with Sq^2."""

    def __init__(self, gens, sq2):
        # gens: list of (name, degree); sq2: name -> polynomial (set of monomials)
        self.names = [g for g, _ in gens]
        self.deg = {g: d for g, d in gens}
        self.sq2gen = {g: frozenset(p) for g, p in sq2.items()}
        for g in self.names:
            assert g in self.sq2gen, f"no Sq^2 given for {g}"
            assert self.deg[g] % 2 == 0, "odd-degree generator not supported"

    # a monomial is a tuple of names, sorted, with repetition
    def mdeg(self, m):
        return sum(self.deg[x] for x in m)

    def basis(self, d):
        """All monomials of total degree d (sorted tuples)."""
        out = []

        def rec(i, cur, rem):
            if rem == 0:
                out.append(tuple(cur))
                return
            if i == len(self.names):
                return
            g = self.names[i]
            k = 0
            while k * self.deg[g] <= rem:
                rec(i + 1, cur + [g] * k, rem - k * self.deg[g])
                k += 1

        rec(0, [], d)
        return sorted(out)

    @staticmethod
    def add(p, q):
        return frozenset(p ^ q)  # symmetric difference == mod-2 sum

    def mul_mono(self, m, p):
        return frozenset(tuple(sorted(m + n)) for n in p)

    def sq2(self, m):
        """Sq^2 of a monomial, via the derivation property (Sq^1 == 0)."""
        res = frozenset()
        for i, g in enumerate(m):
            rest = m[:i] + m[i + 1:]
            res = self.add(res, self.mul_mono(rest, self.sq2gen[g]))
        return res


def matrix_sq2(A, dsrc, rels=None):
    """Matrix of Sq^2 : H^dsrc -> H^{dsrc+2} over F_2, plus the two bases."""
    src = A.basis(dsrc)
    tgt = A.basis(dsrc + 2)
    if rels is not None:
        src = [m for m in src if m not in rels]
        tgt = [m for m in tgt if m not in rels]
    ti = {m: i for i, m in enumerate(tgt)}
    M = [[0] * len(src) for _ in tgt]
    for j, m in enumerate(src):
        for n in A.sq2(m):
            if rels is not None and n in rels:
                continue
            M[ti[n]][j] ^= 1
    return M, src, tgt


# ------------------------------------------------------------- F_2 linear algebra

def rank(M):
    M = [row[:] for row in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c]:
                M[i] = [a ^ b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def transpose(M):
    if not M:
        return []
    return [list(col) for col in zip(*M)]


# ------------------------------------------------------------------- the spaces

t = ("t", 2)  # c_1 of the U(1) / of the U(3) factor, mod 2

SPACES = {}

# n = 1 : BSU(3) x BSU(2) x BU(1)
SPACES["G_1 = SU(3)xSU(2)xU(1)"] = Alg(
    [("c2", 4), ("c3", 6), ("d2", 4), ("t", 2)],
    {  # SU(3): c1 = 0 -> Sq^2 c2 = c3 ; Sq^2 c3 = c1 c3 = 0
        "c2": {("c3",)},
        "c3": set(),
        # SU(2): c1 = c3 = 0 -> Sq^2 c2' = 0
        "d2": set(),
        # U(1): Sq^2 t = t^2
        "t": {("t", "t")},
    },
)

# n = 2 : BSU(3) x BU(2)   (t = c_1 of the U(2))
SPACES["G_2 = (SU(3)xSU(2)xU(1))/Z_2 = SU(3)xU(2)"] = Alg(
    [("c2", 4), ("c3", 6), ("d2", 4), ("t", 2)],
    {
        "c2": {("c3",)},          # SU(3)
        "c3": set(),
        "d2": {("t", "d2")},      # U(2): Sq^2 c2' = c1' c2' + c3' = t d2
        "t": {("t", "t")},
    },
)

# n = 3 : BU(3) x BSU(2)   (t = c_1 of the U(3))
SPACES["G_3 = (SU(3)xSU(2)xU(1))/Z_3 = U(3)xSU(2)"] = Alg(
    [("c2", 4), ("c3", 6), ("d2", 4), ("t", 2)],
    {
        "c2": {("c3",), ("t", "c2")},   # U(3): Sq^2 c2 = c1 c2 + c3
        "c3": {("t", "c3")},            # U(3): Sq^2 c3 = c1 c3  (c4 = 0)
        "d2": set(),                    # SU(2)
        "t": {("t", "t")},
    },
)

# n = 6 : BS(U(3)xU(2)) ,  c1' = -c1 -> t mod 2 shared
SPACES["G_6 = (SU(3)xSU(2)xU(1))/Z_6 = S(U(3)xU(2))"] = Alg(
    [("c2", 4), ("c3", 6), ("d2", 4), ("t", 2)],
    {
        "c2": {("c3",), ("t", "c2")},   # U(3)
        "c3": {("t", "c3")},
        "d2": {("t", "d2")},            # U(2)
        "t": {("t", "t")},
    },
)

# ---- controls (published values known independently: GEM 1808.00009 eqs 36/51/57)
CONTROLS = {
    "BSU(2)  [expect Z/2 = Witten]": Alg([("d2", 4)], {"d2": set()}),
    "BU(1)   [expect 0]": Alg([("t", 2)], {"t": {("t", "t")}}),
    "BSU(3)  [expect 0]": Alg([("c2", 4), ("c3", 6)], {"c2": {("c3",)}, "c3": set()}),
}

PUBLISHED = {  # Davighi-Gripaios-Lohitsiri 1910.11277 Table 1 ; GEM 1808.00009
    "G_1 = SU(3)xSU(2)xU(1)": 1,
    "G_2 = (SU(3)xSU(2)xU(1))/Z_2 = SU(3)xU(2)": 0,
    "G_3 = (SU(3)xSU(2)xU(1))/Z_3 = U(3)xSU(2)": 1,
    "G_6 = (SU(3)xSU(2)xU(1))/Z_6 = S(U(3)xU(2))": 0,
    "BSU(2)  [expect Z/2 = Witten]": 1,
    "BU(1)   [expect 0]": 0,
    "BSU(3)  [expect 0]": 0,
}


def omega_spin_5(name, A):
    # --- E^2 entries in total degree 5 other than (4,1) are zero, by construction:
    #   (5,0): H_5(X;Z) = 0        (cohomology torsion-free and even -> H_odd = 0)
    #   (3,2): H_3(X;Z/2) = 0      (H_3(;Z)=0 and H_2(;Z) free -> Tor term = 0)
    #   (2,3): Omega^Spin_3(pt) = 0
    #   (1,4): H_1(X;Z) = 0        (X = BG, G connected)
    #   (0,5): Omega^Spin_5(pt) = 0
    assert A.basis(5) == [] and A.basis(3) == [] and A.basis(1) == [], "odd degree not empty"

    M_2_4, b2, b4 = matrix_sq2(A, 2)   # Sq^2 : H^2 -> H^4
    M_4_6, b4b, b6 = matrix_sq2(A, 4)  # Sq^2 : H^4 -> H^6
    assert b4 == b4b

    d_out = transpose(M_2_4)   # H_4(;Z/2) -> H_2(;Z/2)
    d_in = transpose(M_4_6)    # H_6(;Z/2) -> H_4(;Z/2)

    n4 = len(b4)
    dim_ker = n4 - rank(d_out)
    dim_im = rank(d_in)

    # d_2 . d_2 = 0  <=>  Sq^2 Sq^2 = Sq^3 Sq^1 = 0 (Sq^1 = 0 here). Check numerically.
    comp = [[sum(M_4_6[i][k] * M_2_4[k][j] for k in range(len(b4))) % 2
             for j in range(len(b2))] for i in range(len(b6))]
    assert all(all(v == 0 for v in row) for row in comp), "d_2^2 != 0"

    assert dim_im <= dim_ker, "image not inside kernel"
    d = dim_ker - dim_im
    print(f"  {name}")
    print(f"    H^2 basis {list(b2)}")
    print(f"    H^4 basis {list(b4)}")
    print(f"    H^6 basis {list(b6)}")
    print(f"    dim ker(d_2 : E_4,1 -> E_2,2) = {dim_ker}   dim im(d_2 : E_6,0 -> E_4,1) = {dim_im}")
    print(f"    ==> Omega^Spin_5 = {'0' if d == 0 else '(Z/2)^%d' % d}")
    return d


print("=" * 74)
print("AC-E1  independent AHSS recomputation of Omega^Spin_5(BG)")
print("=" * 74)
print("\nCONTROLS (published values available independently):")
ok = True
for name, A in CONTROLS.items():
    d = omega_spin_5(name, A)
    match = (d == PUBLISHED[name])
    ok &= match
    print(f"    published: (Z/2)^{PUBLISHED[name]}   MATCH={match}\n")

print("\nTHE FOUR STANDARD-MODEL GLOBAL FORMS:")
results = {}
for name, A in SPACES.items():
    d = omega_spin_5(name, A)
    results[name] = d
    match = (d == PUBLISHED[name])
    ok &= match
    print(f"    DGL 1910.11277 Table 1: (Z/2)^{PUBLISHED[name]}   MATCH={match}\n")

# ------------------------------------------------------- the SM-content pairing
print("=" * 74)
print("Does the SM fermion content pair to zero against the surviving Z/2?")
print("=" * 74)
# The surviving Z/2 for n in {1,3} is generated by the class dual to c_2(SU(2)):
# it IS the Witten SU(2) anomaly, evaluated by (number of SU(2) doublets) mod 2.
DOUBLETS_PER_GEN = {"Q (3 colours x 1 doublet)": 3, "L": 1}
n_doublets = sum(DOUBLETS_PER_GEN.values())
print(f"  SU(2)_L doublets in one SO(10) 16 (== one SM generation + nu_R): {n_doublets}")
assert n_doublets == 4
print(f"  Witten class = {n_doublets} mod 2 = {n_doublets % 2}  -> pairing VANISHES")
for ng in (1, 2, 3):
    assert (ng * n_doublets) % 2 == 0
print("  and for 1, 2, 3 generations alike (4, 8, 12 doublets: all even).")

# ------------------------------------------- the Spin-Z/4 (B-L) refinement, exact
print("=" * 74)
print("Spin x_{Z/2} Z/4 refinement (B-L as a Z/4): the Z/16 saturation arithmetic")
print("=" * 74)
Z16 = 16  # Omega^{Spin x_{Z2} Z4}_5(pt) = Z/16  ~=  Omega^{Pin+}_4(pt) = Z/16 (Smith)
for label, weyl in (("15 (no nu_R)", 15), ("16 (with nu_R, = SO(10) 16)", 16)):
    for ng in (1, 2, 3):
        v = (ng * weyl) % Z16
        print(f"  content {label:28s}  n_gen={ng}  anomaly = {ng*weyl} mod 16 = {v:2d}"
              f"   {'CANCELS' if v == 0 else 'ANOMALOUS'}")
assert (3 * 15) % 16 == 13 and (1 * 15) % 16 == 15
assert all((ng * 16) % 16 == 0 for ng in (1, 2, 3))
print("  => 'saturated' is EXACT only for the 16 (right-handed neutrino present):")
print("     16 == 0 mod 16 fills the modulus exactly; 15 does NOT cancel at any n_gen")
print("     (15, 14, 13, 12, ... mod 16 never 0 for n_gen = 1..15).")
for ng in range(1, 16):
    assert (ng * 15) % 16 != 0

print()
print("=" * 74)
print("ALL CHECKS PASS" if ok else "MISMATCH WITH PUBLISHED VALUES")
print("=" * 74)
raise SystemExit(0 if ok else 1)
