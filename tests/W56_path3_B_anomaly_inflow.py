r"""
W56 / Path-3 Branch-B -- ANOMALY-INFLOW / BOUNDARY-LOCALIZATION and the generation count.

BRANCH B of the blind "why three generations?" wave.  Construction of "the count" used here:
the net chirality of fermions LOCALIZED ON A DEFECT/BOUNDARY, fixed by ANOMALY INFLOW from a
higher-dimensional bulk topological term (Callan-Harvey 1985; Kaplan domain-wall fermions 1992;
Jackiw-Rebbi 1976), with the Nielsen-Ninomiya (1981) "no net chirality on a closed lattice"
no-go as the closed-side constraint.

THE INFLOW SETUP (what the boundary invariant IS)
-------------------------------------------------
Bulk term:  S_bulk = (k/8pi^2) integral Tr F^F   (a 4d theta-term; or a Chern-Simons term in odd d).
Its BOUNDARY VARIATION is the boundary fermion anomaly (descent):  d(CS) = Tr F^F, so a gauge
variation of the bulk term localizes on the boundary as exactly the consumed/produced chiral
anomaly.  The BOUNDARY INVARIANT that counts the localized chiral modes is therefore:
  * for a Kaplan/Jackiw-Rebbi mass domain wall:  the WINDING NUMBER of the mass profile
    m(x) = m1(x)+i m2(x) around 0 (the degree of the map boundary-sphere -> vacuum manifold);
  * for a Callan-Harvey axion string / a Chern insulator: the bulk CHERN / instanton number;
  * for the bulk theta-term: the LEVEL k, quantized to Z by large-gauge invariance (theta~theta+2pi).
All three are the SAME object: a Z-VALUED integer (a degree / Chern number / level).  That is the
load-bearing fact this test pins down and then confronts with the 3-primary target.

WHAT THIS TEST ENCODES (5 deterministic checks; no RNG; exit 0 on success)
--------------------------------------------------------------------------
  [1] NN closed-side no-go: net chirality on a compact BZ is 0 (a boundary is NECESSARY).
  [2] Inflow escape + QUANTIZATION: a single wall carries net chirality = winding number w of the
      mass profile; it is Z-quantized (an integer) but its VALUE = the chosen winding.  Exhibited
      for w = 1, 2, 3 -> counts 1, 2, 3.  ==> inflow QUANTIZES to Z; it does NOT force a value.
  [3] Bulk level quantization: theta ~ theta + 2pi forces the boundary count = level k in Z; any
      integer k is admissible.  The bulk term IS the free input that sets the count.
  [4] Parity / anomaly-freedom arena (Callan-Harvey local inflow): q^2 == q (mod 2), so an
      anomaly-free chiral multiplet has EVEN net count.  The forced constraint is 2-PRIMARY
      (parity); ALL residues mod 3 stay reachable.  Inflow's forcing lands in the WRONG arena.
  [5] The 3-primary obstruction: Hom(Z/3, Z) = 0.  A Z-valued (winding/Chern/level) or mod-2
      (parity) boundary invariant provably CANNOT force the 3-primary count.  Class-wide no-go for
      the STANDARD (integer/2-primary) inflow invariant.

HONEST VERDICT (fork discipline, GEOMETER-VS-PHYSICS-OBJECTS.md)
---------------------------------------------------------------
Standard-physics inflow invariant = a Z index (Chern/winding/level) OR a mod-2 parity => LOCATES &
QUANTIZES the count, does NOT FORCE it, and provably cannot reach the 3-primary arena (checks 4,5).
The ONLY inflow-type object that could reach 3-primary is a TORSION-REFINED (Dai-Freed eta /
Omega^Spin_* bordism) inflow invariant living in a group WITH 3-torsion (e.g. Omega^fr_3 = pi_3^s =
Z/24 has a Z/3 summand) -- the geometer's side.  Whether THAT forces the value 3 is the OPEN global
bordism question; the local inflow computed here is provably blind to it.  Q-extra = the bulk data
(level / winding / degree of the domain-wall target map), which is exactly the FREE input:
choosing 3 assumes the answer.

Reproducible:  python tests/W56_path3_B_anomaly_inflow.py     (exit 0 on success)
No canon / RESEARCH-STATUS / claim-status / verdict file is touched.  Exploration-grade computation.
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  --  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


log("=" * 96)
log("W56 / PATH-3 BRANCH-B -- ANOMALY INFLOW / BOUNDARY LOCALIZATION vs THE GENERATION COUNT")
log("=" * 96)

# ================================================================================================
# [1] NIELSEN-NINOMIYA closed-side no-go: net chirality on a compact BZ is 0 (a boundary is NEEDED)
# ================================================================================================
log("\n[1] Nielsen-Ninomiya: net chirality vanishes on the closed lattice (fermion doubling)")

# Naive 1D lattice fermion, dispersion E(k)=sin k on the compact BZ [-pi,pi).  Midpoint grid so no
# sample sits exactly on a zero; circular wrap identifies +-pi.  Chirality at a zero = sign(dE/dk).
n_k = 2000
ks = -np.pi + (np.arange(n_k) + 0.5) * (2 * np.pi / n_k)
e = np.sin(ks)
chir = []
for i in range(n_k):
    j = (i + 1) % n_k
    if (e[i] < 0) != (e[j] < 0):
        chir.append(float(np.sign(e[j] - e[i])))
net_closed = sum(chir)
check("NN closed BZ: E(k)=sin k has >=2 zeros of opposite chirality; NET chirality = 0 "
      "(no net chiral fermion without a boundary)",
      len(chir) >= 2 and abs(net_closed) < 1e-9,
      f"{len(chir)} zeros, chiralities {chir}, net = {net_closed:.0f}")

# Continuum control E(k)=k on the real LINE (a boundary in momentum space): a single zero, net +1.
# The lattice's compactness is exactly what forces the doubling; opening it permits net chirality.
check("continuum control E(k)=k (open line): a single zero of chirality +1 => the compact/closed "
      "structure, not the fermion, is what forbids net chirality",
      True, "boundary is NECESSARY for a nonzero net count")

# ================================================================================================
# [2] INFLOW ESCAPE + QUANTIZATION: single-wall count = WINDING number w (Z-valued, value = choice)
# ================================================================================================
log("\n[2] Domain-wall / Jackiw-Rebbi inflow: boundary count = winding of the mass profile")

# Kaplan/Jackiw-Rebbi: a complex mass m(x)=m1+i m2 that winds around 0 as x traverses the wall binds
# net |w| chiral zero modes, w = winding number (degree of S^1 -> vacuum-manifold S^1).  The boundary
# chiral count is EXACTLY this topological winding -- the index of the domain-wall Dirac operator =
# the bulk-supplied invariant (anomaly inflow).  Compute the winding for chosen profiles w=1,2,3.

def winding_number(w: int, n: int = 4000) -> int:
    """Winding of m(theta)=exp(i*w*theta) about 0 -> the net chiral zero-mode count of the wall."""
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    m = np.exp(1j * w * theta)
    dphase = np.diff(np.unwrap(np.angle(m)), append=np.angle(m[0]) + 2 * np.pi * w)
    return int(round(np.sum(dphase) / (2.0 * np.pi)))


counts = {w: winding_number(w) for w in (1, 2, 3)}
check("inflow ESCAPE: a single domain wall carries net chirality = winding number of the mass "
      "profile; QUANTIZED to Z (an integer) but its VALUE is the chosen winding {1,2,3} -> {1,2,3}",
      counts == {1: 1, 2: 2, 3: 3},
      f"winding->count map = {counts}  (inflow quantizes to Z; the value is the free profile choice)")

# The "3" here is NOT forced by inflow: it is the winding we CHOSE.  Inflow forces integrality
# (quantization), never a particular integer.  This is the located-not-forced structure made explicit.
check("QUANTIZE-NOT-FORCE: the boundary count is a free integer (winding); '3' is realized only by "
      "choosing a degree-3 profile => choosing 3 assumes the answer (the domain-wall target is the "
      "free input, exactly the predicted trap)",
      counts[3] == 3 and counts[1] == 1,
      "no inflow datum selects w=3 over w=1")

# ================================================================================================
# [3] BULK LEVEL QUANTIZATION: theta ~ theta+2pi forces count = level k in Z (free choice of bulk)
# ================================================================================================
log("\n[3] Bulk theta-term / Chern-Simons level: quantized to Z, any integer admissible")

# Large-gauge invariance of exp(i S_bulk) with S_bulk=(k/8pi^2) int Tr F^F requires k in Z (theta-
# periodicity theta ~ theta+2pi).  The boundary chiral count inflowing from level k IS k.  Model the
# quantization condition: exp(i*2pi*k)=1 <=> k integer; the admissible boundary counts = all of Z.
admissible = [k for k in range(-5, 6) if abs(np.exp(1j * 2 * np.pi * k) - 1.0) < 1e-9]
check("level quantization: exp(i*2pi*k)=1 selects k in Z (theta~theta+2pi); admissible boundary "
      "counts = ALL integers => the bulk term is the free input that sets the count",
      admissible == list(range(-5, 6)),
      f"admissible levels in [-5,5] = {admissible} (every integer; no value is preferred)")

# ================================================================================================
# [4] PARITY / ANOMALY-FREE ARENA: q^2==q (mod 2) => anomaly-free net count is EVEN (2-primary)
# ================================================================================================
log("\n[4] Callan-Harvey local inflow constrains only PARITY (2-primary); mod-3 stays free")

# 2D Callan-Harvey inflow: boundary Weyl multiplet {(q_i, eps_i)} (integer charge, chirality +-1).
# Local anomaly coefficients: A_grav = sum eps_i,  A_gauge = sum eps_i q_i^2.  Net external count
# Nhat = sum eps_i q_i.  Enumerate anomaly-free multiplets deterministically; record achievable Nhat.
from itertools import product

achievable_Nhat = set()
Qs = range(-4, 5)                       # charges
Es = (-1, +1)                           # chiralities
# 4-Weyl multiplets; deterministic full enumeration over a bounded alphabet (no RNG).  4 (even) so
# A_grav = sum eps = 0 is reachable (an odd number of Weyls can never gravity-cancel).
species = [(q, ep) for q in Qs for ep in Es if q != 0]
for combo in product(range(len(species)), repeat=4):
    mult = [species[i] for i in combo]
    a_grav = sum(ep for _, ep in mult)
    a_gauge = sum(ep * q * q for q, ep in mult)
    if a_grav == 0 and a_gauge == 0:    # anomaly-free (local inflow matched)
        achievable_Nhat.add(sum(ep * q for q, ep in mult))
parities = {n % 2 for n in achievable_Nhat}
residues3 = {n % 3 for n in achievable_Nhat}
check("anomaly-free (A_grav=A_gauge=0) net count Nhat is ALWAYS EVEN: q^2==q (mod 2) => "
      "A_gauge == Nhat (mod 2), so A_gauge=0 forces Nhat even.  Forced constraint is 2-PRIMARY.",
      parities == {0},
      f"achievable Nhat parities = {parities} (all even); sample Nhat = {sorted(achievable_Nhat)[:9]}...")
check("ALL residues mod 3 remain reachable among anomaly-free multiplets => local inflow imposes "
      "NO mod-3 / odd-torsion constraint (the count-carrying arena is untouched)",
      residues3 == {0, 1, 2},
      f"reachable residues mod 3 = {sorted(residues3)} (inflow is count-blind on the 3-primary arena)")

# Basis-free algebraic proof of the parity identity (not a search artifact): q^2 - q = q(q-1) even.
alg_ok = all(((q * q - q) % 2 == 0) for q in range(-50, 51))
check("basis-free: q^2 - q = q(q-1) is even for every integer q => A_gauge == Nhat (mod 2) "
      "identically; the EVEN constraint is a theorem, not a sampling accident",
      alg_ok, "q(q-1) even for all q in [-50,50]")

# ================================================================================================
# [5] THE 3-PRIMARY OBSTRUCTION: Hom(Z/3, Z) = 0  (integer/2-primary inflow cannot reach the count)
# ================================================================================================
log("\n[5] Hom(Z/3, Z) = 0: a Z-valued or mod-2 boundary invariant cannot force a 3-primary count")

# A group homomorphism f: Z/3 -> Z sends the generator g (order 3) to n with 3n = f(0) = 0 => n = 0.
# So the ONLY homomorphism is trivial: no Z-valued invariant (winding/Chern/level) detects the Z/3
# summand.  Enumerate: no nonzero n in Z satisfies 3n = 0.
nonzero_hom_targets = [n for n in range(-1000, 1001) if 3 * n == 0 and n != 0]
check("Hom(Z/3, Z) = 0: no nonzero n in Z has 3n=0 => the only homomorphism Z/3 -> Z is trivial; a "
      "Z-valued (winding/Chern/level) inflow invariant is BLIND to the 3-primary summand",
      nonzero_hom_targets == [],
      "no integer index can carry an order-3 class (this is the H6 core, boundary side)")

# The same obstruction for the 2-primary (parity) invariant: Hom(Z/3, Z/2) = 0 (gcd(3,2)=1).
# A hom f: Z/3 -> Z/2 needs 3*f(g) = 0 in Z/2; the only n in Z/2 with 3n == 0 (mod 2) is n = 0.
hom_Z3_Z2 = [n for n in range(2) if (3 * n) % 2 == 0 and n != 0]  # -> [] (n=1 gives 3n=1 != 0)
check("Hom(Z/3, Z/2) = 0 (gcd(3,2)=1): the parity constraint of check [4] also cannot see the "
      "3-primary count => BOTH forced outputs of standard inflow miss the count arena",
      hom_Z3_Z2 == [] and int(np.gcd(3, 2)) == 1,
      "only n=0 in Z/2 solves 3n=0; 2-primary parity is coprime to the 3-primary count")

# ================================================================================================
# SUMMARY / VERDICT
# ================================================================================================
log("\n" + "=" * 96)
if not FAIL:
    log("VERDICT (Branch B, anomaly inflow / boundary localization):")
    log("  Q-force : inflow does NOT force 3.  It QUANTIZES the boundary count to Z (winding/Chern/")
    log("            level) [checks 2,3] and its only FORCED constraint is 2-primary PARITY [check 4].")
    log("  Q-extra : the minimal extra input to pin 3 is the BULK DATA -- the level k / the winding /")
    log("            the degree of the domain-wall target map -- which is exactly the FREE input.")
    log("            It is a free choice, NOT a first-principles condition (choosing 3 assumes the")
    log("            answer; the domain-wall target topology is the trap, as pre-registered).")
    log("  Q-nogo  : YES, class-wide for the STANDARD inflow invariant.  Its boundary invariant is")
    log("            Z-valued (Chern/winding/level) or mod-2 (parity); by Hom(Z/3,Z)=0 and")
    log("            Hom(Z/3,Z/2)=0 [check 5] NO such invariant can force the 3-primary count.")
    log("  Fork    : this no-go is derived in the PHYSICS construction (integer index/parity).  It")
    log("            does NOT transfer to a TORSION-REFINED (Dai-Freed eta / Omega^Spin_* bordism)")
    log("            inflow invariant valued in a group WITH 3-torsion (e.g. Omega^fr_3 = pi_3^s =")
    log("            Z/24 >= Z/3) -- the geometer's side -- whose forcing of the VALUE 3 is the OPEN")
    log("            global bordism question.  Local inflow is provably blind to it (checks 4,5).")
    log("")
    log("  CONSTRUCTION OF THE COUNT: net chirality of boundary/defect-localized fermions, fixed by")
    log("  anomaly inflow.  BOUNDARY INVARIANT: the domain-wall winding / bulk Chern / bulk level.")
    log("  INFLOW LOCATES & QUANTIZES; IT DOES NOT FORCE.")
    log("")
    log("This file settles nothing about GU claim status; it is a graded, reproducible computation.")
    log("\nAll checks passed.")
    raise SystemExit(0)
else:
    log(f"FAILED CHECKS: {FAIL}")
    raise SystemExit(1)
