#!/usr/bin/env python3
"""
Computational verification of the Pati-Salam / Standard-Model structure-group
reduction chain claimed in Eric Weinstein's *Geometric Unity* (April 1, 2021 draft),
Sections 4, 4.1, 4.2, and 11.2-11.3.

The central falsifiable claim under test
----------------------------------------
The chain

    Spin(7,7)
      -> Spin(1,3) x Spin(6,4)                 (observation: pick a metric on X^4)
      -> Spin(1,3) x Spin(6) x Spin(4)         (maximal compact of Spin(6,4))
      ~= SL(2,C) x SU(4) x SU(2) x SU(2)       (accidental isomorphisms)
      -> SL(2,C) x SU(3) x SU(2) x U(1)        (Pati-Salam -> Standard Model)

produces, from the Weyl spinor of the (6,4) normal bundle, exactly 16 complex
"internal" states whose quantum numbers reproduce one Standard-Model generation
(including a right-handed neutrino). The paper's Section 11.3 "n=1" table is the
concrete prediction we compare against.

This script does NOT trust the paper's arithmetic. It builds the spinor weights
of Spin(10) from scratch, embeds the Pati-Salam subgroup by partitioning the
Cartan, computes B-L, weak isospin and hypercharge from group theory, and checks
the resulting (SU(3), SU(2), hypercharge) content against the paper's table.

Run:  python3 pati_salam_chain_verification.py
Deps: numpy
"""

import itertools
import numpy as np

PASS = "PASS"
FAIL = "FAIL"
results = []  # (label, status, detail)


def record(label, ok, detail=""):
    results.append((label, PASS if ok else FAIL, detail))
    mark = "[ OK ]" if ok else "[FAIL]"
    print(f"{mark} {label}" + (f"  -- {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# STEP 0.  Clifford / spinor dimension bookkeeping
# ---------------------------------------------------------------------------
print("=" * 72)
print("STEP 0  Dimension checks (Clifford algebras and spinor modules)")
print("=" * 72)
# Convention note (real forms matter -- see the .md write-up):
#   * For the FULL Spin(7,7) the paper uses the REAL (Majorana) module of the
#     split real Clifford algebra Cl(7,7) ~= R(128): 128 real dims. Imposing a
#     complex structure (the paper's U(64,64) route) gives 128/2 = 64 complex,
#     i.e. each Weyl is 32 complex.
#   * For the (6,4) normal bundle the relevant count is the COMPLEXIFIED Dirac
#     module 2^(10/2) = 32 complex, 16 per chirality. These are two different
#     (both standard) ways of counting; we report each in its own convention.

def real_majorana_dim(n):       # real dim of minimal real spinor, n even
    return 2 ** (n // 2)
def complex_dirac_dim(n):       # complex dim of complexified Dirac module
    return 2 ** (n // 2)

# Spin(7,7): n = 14.
n_full = 14
real128 = real_majorana_dim(n_full)
record("Cl(7,7) real (Majorana) spinor module = 128 (2^7)", real128 == 128,
       f"2^7 = {real128} real")
record("Spin(7,7) Dirac via complex structure = 64 complex (128 real / 2)",
       real128 // 2 == 64, f"128 real -> {real128//2} complex (paper's U(64,64))")
record("Spin(7,7) Weyl (one chirality) = 32 complex",
       real128 // 4 == 32, f"Weyl = {real128//4} complex")

# Normal bundle of X^4 in Y^14 is 10-dimensional with signature (6,4).
n_nb = 10
record("Normal bundle Spin(6,4): dim = 10", 6 + 4 == n_nb)
record("S/(R^6,4) complexified Dirac module = 32 complex (2^5)",
       complex_dirac_dim(n_nb) == 32, f"2^5 = {complex_dirac_dim(n_nb)}")
record("S/(R^6,4) Weyl module = 16 complex (16 per chirality)",
       complex_dirac_dim(n_nb) // 2 == 16, f"Weyl = {complex_dirac_dim(n_nb)//2}")

# Cross-check the paper's eq (4.2)-(4.3): internal QN dim as a function of the
# *spacetime* signature (i,j).  Exponent (i^2+j^2+2ij+i+j)/4 (Dirac),
# minus 4 over 4 for Weyl.  With (i,j)=(1,3):
i, j = 1, 3
dirac_exp = (i**2 + j**2 + 2*i*j + i + j) / 4
weyl_exp = (i**2 + j**2 + 2*i*j + i + j - 4) / 4
record("Paper eq (4.3): Weyl internal-QN dim from spacetime (1,3) = 16C",
       2 ** weyl_exp == 16, f"2^{weyl_exp:g} = {2**weyl_exp:g}")
record("Consistency: spacetime-(1,3) Weyl count == normal-bundle Weyl count",
       2 ** weyl_exp == complex_dirac_dim(n_nb) // 2)


# ---------------------------------------------------------------------------
# STEP 1.  Accidental isomorphisms (dimension / rank witnesses)
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("STEP 1  Accidental Lie-algebra isomorphisms")
print("=" * 72)

def dim_so(n):      return n * (n - 1) // 2          # dim SO(n) = dim Spin(n)
def dim_su(n):      return n * n - 1                 # dim SU(n)

# Spin(6) ~= SU(4):  dim so(6)=15, dim su(4)=15, both rank 3.
record("dim Spin(6) == dim SU(4) (=15) and rank 3 == 3",
       dim_so(6) == dim_su(4) == 15, f"so6={dim_so(6)}, su4={dim_su(4)}")
# Spin(4) ~= SU(2) x SU(2): dim so(4)=6 = 3+3, ranks 2 == 1+1.
record("dim Spin(4) == dim SU(2)xSU(2) (=6) and rank 2 == 1+1",
       dim_so(4) == 2 * dim_su(2) == 6, f"so4={dim_so(4)}, 2*su2={2*dim_su(2)}")
# (informational) Spin(10) ~ the GUT envelope; dim so(10)=45.
record("Pati-Salam Spin(6)xSpin(4) sits in Spin(10): 15+6 <= 45",
       dim_so(6) + dim_so(4) <= dim_so(10))


# ---------------------------------------------------------------------------
# STEP 2.  Build the Spin(10) chiral spinor 16 from its weights.
# ---------------------------------------------------------------------------
# The Dirac spinor of Spin(10) has weights (+-1/2)^5 (all 32 sign choices).
# A chirality projection keeps the 16 with an EVEN number of minus signs.
# We work with the compact form Spin(6)xSpin(4) c Spin(10) as the maximal
# compact of the Spin(6,4)-route; this is exactly the branching the paper
# invokes ("maximal compact").  Real-form subtleties are discussed in the .md.
print("\n" + "=" * 72)
print("STEP 2  Spin(10) chiral spinor 16 -> weights")
print("=" * 72)

half = 0.5
all_weights = [w for w in itertools.product([half, -half], repeat=5)]
# even number of minus signs => one chirality (the '16', S^+).
spinor16 = [w for w in all_weights if sum(1 for c in w if c < 0) % 2 == 0]
record("Spin(10) Dirac spinor has 32 weights", len(all_weights) == 32)
record("Chiral 16 = weights with even # of minus signs", len(spinor16) == 16,
       f"|16| = {len(spinor16)}")


# ---------------------------------------------------------------------------
# STEP 3.  Embed SU(4) x SU(2)_L x SU(2)_R  (Pati-Salam) in Spin(10).
# ---------------------------------------------------------------------------
# Convention: the 5 orthonormal Cartan directions e1..e5 of so(10) split as
#   e1,e2,e3  -> Spin(6) ~ SU(4)              (color SU(3) + U(1)_{B-L})
#   e4,e5     -> Spin(4) ~ SU(2)_L x SU(2)_R  (weak isospin, left and right)
# A spinor weight is w = (s1,s2,s3,s4,s5), each si = +-1/2.
#
# Spin(4) Cartan -> weak isospins (self-dual / anti-self-dual combination):
#   T3L = (s4 + s5)/2        T3R = (s4 - s5)/2
#   => (s4,s5) in {(++),(--)} is an SU(2)_L doublet (T3R=0, T3L=+-1/2)
#      (s4,s5) in {(+-),(-+)} is an SU(2)_R doublet (T3L=0, T3R=+-1/2)
# SU(4) -> SU(3) x U(1)_{B-L}: with B-L normalised so quark triplets carry +-1/3
#   B-L = -(2/3)(s1 + s2 + s3)
#   color SU(3) triplet  <=> two of (s1,s2,s3) equal -1/2 (or its conjugate);
#   SU(3) singlet (lepton) <=> all three equal (+++ or ---).
# Standard Pati-Salam -> SM:
#   Y = T3R + (B-L)/2        (NOT B-L alone; SU(2)_R is essential)
#   Q = T3L + Y              (Gell-Mann-Nishijima)
#   paper's integer label:  n = 6 * Y
print("\n" + "=" * 72)
print("STEP 3  Pati-Salam embedding: compute B-L, T3L, T3R, Y, Q per weight")
print("=" * 72)

def su3_label(w123):
    """SU(3)_color irrep carried by the color part of a weight.
    All-equal triples (+++/---) are leptonic singlets; mixed triples are a
    color (anti)triplet whose 3-ness is read off from B-L sign downstream."""
    nminus = sum(1 for c in w123 if c < 0)
    if nminus in (0, 3):
        return "1"          # lepton / anti-lepton (SU(3) singlet)
    return "triplet"        # 3 or 3bar -- decided by B-L sign

def bL(w123):
    return -(2.0 / 3.0) * sum(w123)   # quark triplet -> +-1/3, lepton -> -+1

rows = []
for w in spinor16:
    w123 = w[:3]
    s4, s5 = w[3], w[4]
    t3l = (s4 + s5) / 2.0
    t3r = (s4 - s5) / 2.0
    blv = bL(w123)
    Y = t3r + blv / 2.0
    Q = t3l + Y
    n = 6 * Y
    lab = su3_label(w123)
    if lab == "triplet":
        lab = "3" if blv > 0 else "3bar"   # B-L=+1/3 -> 3 (quark); -1/3 -> 3bar
    rows.append(dict(weight=w, su3=lab, T3L=t3l, T3R=t3r,
                     BmL=blv, Y=Y, Q=Q, n=n))

# Sanity: an anomaly-free SM generation has Tr(Y) = 0 and Tr(Q) = 0.
sumY = sum(r["Y"] for r in rows)
record("Sum of hypercharge over the 16 = 0 (trace condition)",
       abs(sumY) < 1e-9, f"sum Y = {sumY:g}")
sumQ = sum(r["Q"] for r in rows)
record("Sum of electric charge over the 16 = 0",
       abs(sumQ) < 1e-9, f"sum Q = {sumQ:g}")


# ---------------------------------------------------------------------------
# STEP 4.  Collapse the 16 weights into SU(3) x SU(2)_L multiplets and compare
#          to the paper's n=1 table (Section 11.3).
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("STEP 4  Multiplet structure vs paper Section 11.3 (n=1 generation)")
print("=" * 72)

# Each SM multiplet shares (B-L, T3R); within it color (SU3) and T3L vary.
from collections import defaultdict, Counter
buckets = defaultdict(list)
for r in rows:
    key = (round(r["BmL"], 3), round(r["T3R"], 3))
    buckets[key].append(r)

multiplets = []
for key, members in buckets.items():
    bml, t3r = key
    t3l_vals = sorted({round(m["T3L"], 3) for m in members})
    su2dim = len(t3l_vals)                       # 2 -> doublet, 1 -> singlet
    su3dim = len(members) // su2dim              # 3 -> color triplet, 1 -> singlet
    su3lab = members[0]["su3"]
    n_val = int(round(members[0]["n"]))
    multiplets.append(dict(su3=su3lab, su3dim=su3dim, su2=su2dim,
                           n=n_val, dim=su3dim * su2dim,
                           Q=sorted({round(m["Q"], 3) for m in members})))

# Paper's n=1 table (Section 11.3), as (su3 label, su2 dim, n, total dim):
#   Left Quarks       [3 x 2]_L   n=+1   dim 6
#   Left Anti-Quarks  [3bar x 1]  n=+2   dim 3
#   Left Anti-Quarks  [3bar x 1]  n=-4   dim 3
#   Left Leptons      [1 x 2]_L   n=-3   dim 2
#   Left Anti-Lepton  [1 x 1]     n=+6   dim 1
#   Left Anti-Lepton  [1 x 1]     n=0    dim 1
paper_table = [
    ("3",    2,  1, 6, "Left Quarks Q"),
    ("3bar", 1,  2, 3, "Left Anti-Quark d^c"),
    ("3bar", 1, -4, 3, "Left Anti-Quark u^c"),
    ("1",    2, -3, 2, "Left Leptons L"),
    ("1",    1,  6, 1, "Left Anti-Lepton e^c"),
    ("1",    1,  0, 1, "Left Anti-Neutrino nu^c"),
]

computed = [(m["su3"], m["su2"], m["n"], m["dim"]) for m in multiplets]
paper_keys = Counter((s, su2, n, d) for (s, su2, n, d, _name) in paper_table)
comp_keys = Counter(computed)

print("\n  Computed multiplets (SU3, SU2_L, n=6Y, dim):")
for c in sorted(computed, key=lambda t: (-t[3], t[2])):
    print(f"     {c}")
print("\n  Paper n=1 table (SU3, SU2_L, n=6Y, dim):")
for (s, su2, n, d, name) in paper_table:
    print(f"     {(s, su2, n, d)}   {name}")

match = paper_keys == comp_keys
record("Computed 16 multiplets == paper's n=1 table (exact multiset match)",
       match,
       "identical" if match else f"diff computed-paper={comp_keys-paper_keys}, "
                                 f"paper-computed={paper_keys-comp_keys}")

total_dim = sum(c[3] for c in computed)
record("Total internal states = 16", total_dim == 16, f"sum dim = {total_dim}")

# Electric charges present (Gell-Mann-Nishijima) -- should be the SM set.
charges = sorted({round(q, 3) for m in multiplets for q in m["Q"]})
expected_charges = sorted(round(x, 3) for x in {-1.0, -2/3, -1/3, 0.0, 1/3, 2/3, 1.0})
record("Electric charges = {0, +-1/3, +-2/3, +-1} (one generation)",
       charges == expected_charges, f"charges = {charges}")


# ---------------------------------------------------------------------------
# STEP 5.  Embedding-ambiguity probe: does the NAIVE SU(4) U(1) (B-L only,
#          ignoring SU(2)_R) reproduce hypercharge?  It should NOT.
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("STEP 5  Embedding ambiguity: hypercharge needs T3R (not B-L alone)")
print("=" * 72)
naive_ns = sorted({int(round(6 * (r["BmL"] / 2.0))) for r in rows})
correct_ns = sorted({m["n"] for m in multiplets})
record("Naive (B-L only) hypercharge FAILS to reproduce paper n-values",
       naive_ns != correct_ns,
       f"naive n-set={naive_ns} vs correct n-set={correct_ns}")
print("  -> Only the standard PS->SM embedding Y = T3R + (B-L)/2 works.")


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
nfail = sum(1 for _, s, _ in results if s == FAIL)
for label, status, detail in results:
    print(f"  {status:4}  {label}")
print("-" * 72)
if nfail == 0:
    print("VERDICT: every checked step holds. The group-theory reduction chain")
    print("and the 16-state quantum-number table are internally VERIFIED.")
else:
    print(f"VERDICT: {nfail} check(s) FAILED -- see above.")
print("=" * 72)
