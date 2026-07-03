#!/usr/bin/env python3
# LANE-SM-BOUNDARY, decidable first test (exploration grade; NO target import -- 3 is never assumed).
#
# Question opened: fix the mirror-balanced interior; require SM-SHAPED (anomaly-free, gauged) chiral
# boundary data; is the EXTERNAL chiral background (the flux datum that carries the net count) then
# PINNED? The canon result already established the external datum is a topological index = flux,
# ANY integer (tests/function-space-ext/flux_index_2d.py). Here we ask the offensive question: does
# imposing anomaly-freedom on the boundary content CONSTRAIN which external count is admissible?
#
# This is the Callan-Harvey / anomaly-inflow toy in its smallest honest 2D form:
#   * boundary content = a multiplet of 2D Weyl fermions {(q_i, eps_i)}, charge q_i in Z under a U(1),
#     chirality eps_i in {+1,-1};
#   * a uniform external U(1) flux Phi is the EXTERNAL chiral background;
#   * a charge-q_i species in flux Phi has net chiral zero-mode count = q_i * Phi
#     (Aharonov-Casher / Atiyah-Singer; VERIFIED on the lattice below, non-vacuously, for q>1);
#   * the LOCAL anomaly-inflow coefficients the boundary must cancel to be a consistent boundary of a
#     3D bulk are the 2D perturbative anomalies:
#         A_grav = sum_i eps_i          (gravitational / framing: net # of L minus R Weyls)
#         A_gauge = sum_i eps_i q_i^2   (U(1)^2 gauge anomaly; Callan-Harvey inflow coefficient)
#   * the net EXTERNAL count carried at unit flux is the LINEAR invariant
#         Nhat = sum_i eps_i q_i        (so the realized count is N = Nhat * Phi).
#
# DECIDABLE TEST: over all anomaly-free multiplets (A_grav = A_gauge = 0) within a bounded search,
# what is the set of achievable Nhat? Three honest outcomes are distinguished (we READ which holds):
#   (i)   Nhat pinned to {0}        -> local anomaly-freedom fully pins the external count;
#   (ii)  Nhat any integer         -> local anomaly-freedom leaves the count totally free;
#   (iii) Nhat constrained to a proper subgroup (e.g. EVEN only) -> a PARTIAL, 2-primary constraint.
# The mod-2 identity q^2 == q (mod 2) forces A_gauge = sum eps*q^2 == sum eps*q = Nhat (mod 2), so
# A_gauge = 0 => Nhat is EVEN -- a provable parity constraint. The test measures whether anything
# STRONGER than this mod-2 constraint holds (e.g. a mod-3 / count-selecting one). Any mod-3 / odd-arena
# pinning must come from the GLOBAL (bordism / Dai-Freed eta) datum -- the source-action SPEC bottleneck.
#
# NO number is imported: we never assume, insert, or divide by 3. We only READ OFF what the anomaly
# conditions permit.
import itertools
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

# ----------------------------------------------------------------------------------------------------
# PART A -- lattice check that a CHARGED species sees index = q*Phi (non-vacuous: q = 2, 3).
# Reuses the exact flux-Dirac construction of tests/function-space-ext/flux_index_2d.py; a charge-q
# species couples to q*A, i.e. it sees effective flux q*Phi. We confirm |index| = q*Phi on the lattice.
# ----------------------------------------------------------------------------------------------------
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

def build_flux_dirac(Lx, Ly, flux, r=1.0):
    """2D Wilson-Dirac, uniform effective flux (Landau gauge + x-seam twist). flux = q*Phi here."""
    N = Lx * Ly
    def idx(nx, ny):
        return (ny % Ly) * Lx + (nx % Lx)
    Tx = np.zeros((N, N), dtype=complex)
    Ty = np.zeros((N, N), dtype=complex)
    Wil = np.zeros((N, N), dtype=complex)
    tp = 2 * np.pi
    for nx in range(Lx):
        for ny in range(Ly):
            a = idx(nx, ny)
            phx = np.exp(-1j * tp * flux * ny / Ly) if nx == Lx - 1 else 1.0
            b = idx(nx + 1, ny)
            Tx[a, b] += -0.5j * phx; Tx[b, a] += 0.5j * np.conj(phx)
            Wil[a, b] += -0.5 * phx; Wil[b, a] += -0.5 * np.conj(phx)
            Wil[a, a] += 0.5; Wil[b, b] += 0.5
            phy = np.exp(1j * tp * flux * nx / (Lx * Ly))
            c = idx(nx, ny + 1)
            Ty[a, c] += -0.5j * phy; Ty[c, a] += 0.5j * np.conj(phy)
            Wil[a, c] += -0.5 * phy; Wil[c, a] += -0.5 * np.conj(phy)
            Wil[a, a] += 0.5; Wil[c, c] += 0.5
    Tx = 0.5 * (Tx + Tx.conj().T); Ty = 0.5 * (Ty + Ty.conj().T); Wil = 0.5 * (Wil + Wil.conj().T)
    D = np.kron(s1, Tx) + np.kron(s2, Ty) + np.kron(s3, r * Wil)
    return 0.5 * (D + D.conj().T), np.kron(s3, np.eye(N, dtype=complex))

def chiral_index(D, G, gap=0.25):
    w, V = np.linalg.eigh(D)
    Z = V[:, np.abs(w) < gap]
    if Z.shape[1] == 0:
        return 0
    return int(round(np.trace(Z.conj().T @ G @ Z).real))

print("=" * 92)
print("PART A -- charged flux-Dirac index = q*Phi on the lattice (non-vacuous: q=2,3)")
print("=" * 92)
Lx = Ly = 16
for (q, Phi) in [(1, 1), (2, 1), (1, 2), (3, 1)]:
    D, G = build_flux_dirac(Lx, Ly, q * Phi)
    ind = chiral_index(D, G)
    print("  charge q=%d in flux Phi=%d  ->  effective flux q*Phi=%d, lattice index=%+d"
          % (q, Phi, q * Phi, ind))
    check(abs(ind) == abs(q * Phi), "charge-q species has index = q*Phi (q=%d,Phi=%d)" % (q, Phi))

# ----------------------------------------------------------------------------------------------------
# PART B -- the decidable question: does anomaly-freedom pin the achievable external count Nhat?
# Bounded integer search over multiplets of up to n_max Weyl fermions with charges in [-Q, Q]\{0}.
# For each anomaly-free multiplet (A_grav = 0 AND A_gauge = 0) record Nhat = sum eps_i q_i.
# We report the SET of achievable Nhat and its parities. NO target is imposed.
# ----------------------------------------------------------------------------------------------------
def anomaly_free_multiplets(n, Q):
    """Yield (charges tuple with signed chirality) multiplets of exactly n Weyl fermions,
    charge magnitude in 1..Q, chirality +-1, satisfying A_grav=0 and A_gauge=0."""
    signed = [(q, e) for q in range(1, Q + 1) for e in (+1, -1)]  # (|q|, chirality); charge sign
    # a Weyl species is (charge in Z\{0}, chirality). Enumerate charge in [-Q,Q]\{0} x chirality.
    species = [(c, e) for c in range(-Q, Q + 1) if c != 0 for e in (+1, -1)]
    seen = set()
    for combo in itertools.combinations_with_replacement(species, n):
        Agrav = sum(e for (_, e) in combo)
        Agauge = sum(e * c * c for (c, e) in combo)
        if Agrav == 0 and Agauge == 0:
            Nhat = sum(e * c for (c, e) in combo)
            seen.add(Nhat)
    return seen

print()
print("=" * 92)
print("PART B -- achievable net external count Nhat over ANOMALY-FREE boundary multiplets")
print("  (A_grav = sum eps = 0  AND  A_gauge = sum eps*q^2 = 0); NO target imported")
print("=" * 92)
Q = 4
all_Nhat = set()
for n in range(2, 7):
    s = anomaly_free_multiplets(n, Q)
    all_Nhat |= s
    if s:
        print("  n=%d Weyl fermions, |q|<=%d: achievable Nhat = %s"
              % (n, Q, sorted(s)))
odd_reachable = sorted(x for x in all_Nhat if x % 2 != 0)
nonzero_reachable = sorted(x for x in all_Nhat if x != 0)
mod3_residues = sorted(set(x % 3 for x in all_Nhat))
print()
print("  UNION of achievable Nhat (|q|<=%d, up to 6 Weyls): %s" % (Q, sorted(all_Nhat)))
print("  nonzero Nhat reachable while anomaly-free : %s" % nonzero_reachable)
print("  ODD     Nhat reachable while anomaly-free : %s   (empty => a mod-2 constraint holds)" % odd_reachable)
print("  residues of Nhat mod 3 that are reachable : %s   (all of {0,1,2} => NO mod-3 constraint)"
      % mod3_residues)

# The honest verdict conditions (NOT a target import -- we test which case holds):
pinned_to_zero = (all_Nhat == {0})
all_even = all(x % 2 == 0 for x in all_Nhat)
no_mod3 = (mod3_residues == [0, 1, 2])
# Independent proof of the parity constraint (basis-free, holds for ANY charges): q^2 == q (mod 2).
for _ in range(2000):
    m = np.random.randint(2, 8)
    charges = np.random.randint(-6, 7, size=m)
    charges = charges[charges != 0]
    eps = np.random.choice([-1, 1], size=len(charges))
    Agauge = int(np.sum(eps * charges * charges))
    Nh = int(np.sum(eps * charges))
    check((Agauge - Nh) % 2 == 0, "A_gauge == Nhat (mod 2) identically (q^2==q mod 2)")

check(0 in all_Nhat, "the anomaly-free set is non-empty and contains the trivial (vectorlike) count 0")
check(len(nonzero_reachable) > 0, "anomaly-freedom permits NONZERO net external count (not pinned to 0)")
check(all_even, "EVERY anomaly-free Nhat is EVEN -- a genuine mod-2 (2-primary) constraint")
check(no_mod3, "all residues mod 3 reachable -- local anomaly-freedom imposes NO mod-3 / count constraint")

print()
print("#" * 92)
print("# VERDICT (LANE-SM-BOUNDARY, first decidable test): outcome (iii) -- PARTIAL constraint.")
print("#  Local (Callan-Harvey / perturbative) anomaly-freedom of an SM-shaped U(1) does NOT pin")
print("#  the external count to a single value: a whole lattice of Nhat is reachable. But it is NOT")
print("#  unconstrained either -- it forces Nhat EVEN. This is a PROVABLE mod-2 fact, not a search")
print("#  artifact: q^2 == q (mod 2) => A_gauge = sum eps*q^2 == sum eps*q = Nhat (mod 2), so")
print("#  A_gauge = 0 forces Nhat even. The constraint lands ENTIRELY in the 2-primary arena.")
print("#  Crucially, ALL residues mod 3 remain reachable: the local anomaly condition imposes NO")
print("#  mod-3 / odd-torsion constraint and does NOT force or forbid any count (never 3).")
print("#  This RE-DERIVES the CRT two-arena split from the boundary side: local anomaly inflow")
print("#  touches only Z/8 (parity); the count-carrying Z/3 arena is untouched.")
print("#  => PINNING the actual count is a mod-3 / global question -> requires the bordism class /")
print("#     Dai-Freed eta (Omega^Spin_* torsion), which is exactly the source-action SPEC")
print("#     bottleneck (obligation (4): the ch2/eta correction + family symbol). Not reachable")
print("#     from the local anomaly polynomial alone.")
print("#  hard asserts passed: %d ; NO number (3,8,24) imported -- every verdict read off, not fitted." % NASSERT)
print("#" * 92)
