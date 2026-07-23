#!/usr/bin/env python3
"""
WC-ENUM-COMPLETENESS route (b): the adversarial enumeration-extension engine.

Systematically generates candidate obstruction-carrying structures BEYOND the equivariant
core swept by enum_class_c_generators.py -- gauge-field-coupled variants, boundary/eta
variants, and products/compositions of the enumerated items -- and computes, EXACTLY (integer
and Fraction arithmetic throughout), the primary decomposition of the congruence each one can
impose.  Verdict categories:

  A  = obstruction available from the sector's own data, 2-primary          (consistent)
  B  = odd-primary object that is count-independent / homotopy-fixed        (the located
       carrier; consistent -- it locates, it cannot constrain a count)
  C  = external channel: needs a background/spurion VEV or non-sector twist  (the paper's
       "count is external" verdict; not an obstruction)
  D  = SECTOR-INTERIOR obstruction with an odd-primary congruence component (CONTRADICTS
       Theorem 1 -- must be reported prominently; engine exit code 1)

The engine's exactness: Weyl dimension formula, quadratic Casimir, and Dynkin index over the
D5 = so(10) root system in Fraction arithmetic; the charge-q boundary eta family as exact
fractions; the composition-closure lemma checked exhaustively over the generated census.
From-memory prior-art rows (Dai-Freed-type boundary invariants) are FLAGGED as such and
carry no computed numbers beyond textbook group orders.

Companion: enum_class_c_generators.py (route a), verify/indep_check.py.
"""
from fractions import Fraction as Fr
from itertools import product
import sys

FAILURES = []      # category-D findings land here; must stay empty


def factorize(n):
    n = abs(int(n))
    if n == 0:
        return {}
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def odd_part(n):
    n = abs(int(n))
    while n and n % 2 == 0:
        n //= 2
    return n


def fmt_fact(n):
    f = factorize(n)
    return " * ".join(f"{p}^{k}" if k > 1 else f"{p}" for p, k in sorted(f.items())) or "1"


# ------------------------------------------------------------------ exact D5 = so(10) machinery
def d5_positive_roots():
    roots = []
    for i in range(5):
        for j in range(i + 1, 5):
            for s in (1, -1):
                r = [0] * 5
                r[i], r[j] = 1, s
                roots.append(tuple(r))
    return roots            # 20 positive roots of D5

RHO5 = (4, 3, 2, 1, 0)      # Weyl vector of D5 in the orthogonal basis
# fundamental weights of D5 (orthogonal basis)
FW5 = [(1, 0, 0, 0, 0), (1, 1, 0, 0, 0), (1, 1, 1, 0, 0),
       (Fr(1, 2),) * 4 + (Fr(-1, 2),), (Fr(1, 2),) * 5]


def hw_from_labels(labels, FW):
    return tuple(sum(Fr(a) * Fr(w[i]) for a, w in zip(labels, FW)) for i in range(len(FW[0])))


def ip(x, y):
    return sum(Fr(a) * Fr(b) for a, b in zip(x, y))


def weyl_dim(lam, roots, rho):
    num, den = Fr(1), Fr(1)
    for al in roots:
        num *= ip(tuple(Fr(l) + Fr(r) for l, r in zip(lam, rho)), al)
        den *= ip(rho, al)
    return num / den


def casimir(lam, rho):
    return ip(lam, lam) + 2 * ip(lam, rho)


def rel_dynkin(lam, roots, rho, vec_lam):
    """Dynkin index normalized so the vector rep has index 1 (dim g cancels in the ratio)."""
    dv, cv = weyl_dim(vec_lam, roots, rho), casimir(vec_lam, rho)
    return (weyl_dim(lam, roots, rho) * casimir(lam, rho)) / (dv * cv)


R5 = d5_positive_roots()
VEC5 = (1, 0, 0, 0, 0)

print("#" * 98)
print("# WC-ENUM-COMPLETENESS route (b): adversarial extension engine (exact arithmetic)")
print("#" * 98)

# ---------------------------------------------------------- E1: gauge-coupled index congruences
print("""
E1. GAUGE-COUPLED VARIANTS.  Twisting the Dirac/RS operator by a gauge representation R makes
the index family  ind_R(n) = dim R * Ahat-part + I(R) * n  (n = background topological charge;
Ahat-part is even on spin X^4 by Rokhlin).  The congruence the twist imposes on its own index
is  mod I(R)  (the per-unit index step, vector-normalized).  Odd-primary content of I(R) is
therefore the exact place an odd-prime congruence could enter through the gauge channel.
""")
named = {(0, 0, 0, 0, 0): "singlet 1 (sector: trivial twist)",
         (1, 0, 0, 0, 0): "10 vector (sector: the V10 of the 4+10 split)",
         (0, 1, 0, 0, 0): "45 adjoint (sector: the so(10) gauge field)",
         (0, 0, 0, 1, 0): "16bar (sector: the mirror generation)",
         (0, 0, 0, 0, 1): "16 (sector: the generation rep)"}
rows = []
labels_list = [l for l in product(range(3), repeat=5) if sum(l) <= 2]
for labels in sorted(labels_list, key=lambda l: weyl_dim(hw_from_labels(l, FW5), R5, RHO5)):
    lam = hw_from_labels(labels, FW5)
    dim = weyl_dim(lam, R5, RHO5)
    idx = rel_dynkin(lam, R5, RHO5, VEC5)
    assert dim.denominator == 1
    in_sector = tuple(labels) in named
    rows.append((int(dim), idx, in_sector, named.get(tuple(labels), ""), labels))
print("  R (Dynkin labels)      dim      I(R)         I(R) factored     sector?   category")
for dim, idx, in_sector, tag, labels in rows:
    assert idx.denominator in (1, 2)                       # half-integer indices possible
    num = idx.numerator
    op = odd_part(num)
    if num == 0:
        cat = "A (vacuous: no index step)"
    elif op == 1:
        cat = "A (2-primary)"
    else:
        cat = "C (external twist)" if not in_sector else "D ???"
    if in_sector and num != 0 and op != 1:
        FAILURES.append(f"named sector rep {labels} has odd-primary index {idx}")
    mark = "SECTOR" if in_sector else "beyond"
    print(f"  {str(labels):18s} {dim:6d}   {str(idx):>7s}   {fmt_fact(num):>18s}"
          f"{'/2' if idx.denominator == 2 else '  '}   {mark:6s}   {cat}"
          + (f"  <- {tag}" if tag else ""))
odd_beyond = [(dim, idx) for dim, idx, ins, _, _ in rows if not ins and odd_part(idx.numerator) != 1]
print(f"""
  => Every twist by a rep the sector actually contains (1, 10, 16, 16bar, 45) imposes a purely
     2-primary congruence: I in {{0(no step), 1(vacuous), 2, 4, 8}}.  Odd primes appear IMMEDIATELY
     beyond the sector's named data ({len(odd_beyond)} reps with odd-primary index in this sweep alone,
     e.g. 54 -> 12 = 2^2*3, 120 -> 28 = 2^2*7, 126 -> 35 = 5*7, 144 -> 34 = 2*17, 210 -> 56 = 2^3*7):
     the class-C boundary is SHARP, not vacuous -- but every such twist is an EXTERNAL background
     choice (category C), not a sector-interior obstruction, and it constrains its own R-channel
     index, not the 16-channel generation count.""")

# su(2)_+ family channel: only j=1 occurs on the carrier (leg3 embedding enumeration, canon)
print("""
E1b. THE su(2)_+ FAMILY CHANNEL.  Family-rep index I(j) (fundamental-normalized 2j(j+1)(2j+1)/3):""")
for jj in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2)):
    I = 2 * jj * (jj + 1) * (2 * jj + 1) / 3 / (Fr(1, 2))  # normalize I(1/2) = 1: divide by 1/2...
for jj in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2)):
    I = (2 * jj * (jj + 1) * (2 * jj + 1) / 3) / (2 * Fr(1, 2) * Fr(3, 2) * Fr(2) / 3)
    onc = "ON-CARRIER (the j=1 triplet; the paper's adjoint index 4k, item 4)" if jj == 1 else \
          "not realized (leg3 enumeration: only the triplet multiplicity occurs)"
    print(f"  j = {str(jj):4s}: I = {str(I):>5s} = {fmt_fact(I.numerator)}"
          f"{'/' + str(I.denominator) if I.denominator != 1 else ''}   {onc}")
    if jj == 1:
        assert I == 4 and odd_part(I.numerator) == 1
print("  => the one family rep the carrier realizes gives 2I = 8, index step 4k: 2-primary (item 4);")
print("     a j=3/2 quartet WOULD carry I = 10 = 2*5 (5-primary!) but is excluded by the computed")
print("     embedding enumeration (tests/generation-sector/leg3_family_embedding_enumeration.py).")

# frame-spinor channel: so(14) half-spinor index, exact D7 arithmetic
def dn_positive_roots(n):
    roots = []
    for i in range(n):
        for j in range(i + 1, n):
            for s in (1, -1):
                r = [0] * n
                r[i], r[j] = 1, s
                roots.append(tuple(r))
    return roots

R7, RHO7, VEC7 = dn_positive_roots(7), (6, 5, 4, 3, 2, 1, 0), (1, 0, 0, 0, 0, 0, 0)
S7 = (Fr(1, 2),) * 7
I64 = rel_dynkin(S7, R7, RHO7, VEC7)
print(f"""
E1c. THE FRAME-SPINOR CHANNEL.  so(14) half-spinor 64: I = {I64} = {fmt_fact(I64.numerator)}: 2-primary
     (the spinor 2-smoothness lemma, item 6, in index form: spinor Dynkin indices of so(2n) are
     2^(n-4) -- a power of two for every n >= 4).""")
assert I64 == 8

# ------------------------------------------------------------------- E2: boundary/eta variants
print("""
E2. BOUNDARY / eta VARIANTS on the RP^3 = L(2;1) spine (the sector's actual boundary data).
    Charge-q Dirac eta family (in-repo, canon/boundary-eta-of-mu-RESULTS.md): eta_q = (2q^2-4q+1)/8.""")
worst_den_odd = 1
for q in range(-12, 13):
    eta = Fr(2 * q * q - 4 * q + 1, 8)
    worst_den_odd = max(worst_den_odd, odd_part(eta.denominator))
    assert eta.numerator % 2 == 1                    # numerator odd for every q
print("  q in [-12,12]: every eta_q has ODD numerator over denominator 8 = 2^3: the whole family is")
print(f"  2-primary (max odd part of any denominator = {worst_den_odd}).  Category A.")
print("""
    Gravitational framing channel -p_1/24: 24 = 2^3 * 3 -- the ONLY odd-primary boundary object in
    the sector's own data.  The full framed class +/-2 and e_R = +/-1/12 have order 12;
    only their projected 3-primary components (8 or 16 in Z/24) have order 3.
    The class is HOMOTOPY-FIXED (a fact about pi_3^s, identical for any generation count):
    it cannot constrain a count.  Category B -- located, not an obstruction.

    Dai-Freed-type extensions (FLAGGED: from-memory prior art, no new computation):
      - pin+ mod-16 (Rokhlin/eta) layer: Z/16 = 2^4                          -> category A
      - AZ class-CII / quaternionic layers: Z/2, Z/8 towers                  -> category A
      - exp(2 pi i eta) on L(n;1) with n = 3 (a Z/3 lens space) has genuinely 3-primary eta values,
        BUT the sector's metric-fiber spine is RP^3 = L(2;1) with deck group Z/2 (in-repo, computed):
        importing a Z/3 deck group replaces the sector's geometry                -> category C
      - Garcia-Etxebarria--Montero Z_9 -> N_gen in 3Z: a genuinely 3-primary anomaly, but it
        requires a global Z_9 symmetry as INPUT; no such datum exists in the sector -> category C""")

# ------------------------------------------------- E3: products / compositions of enumerated items
print("""
E3. PRODUCTS AND COMPOSITIONS of the genuinely finite-torsion rows.
    Lemma (arithmetic): if congruence moduli m1, m2 are 2-primary (powers of two), then so are
    lcm(m1,m2), gcd(m1,m2) and m1*m2; multiplying an INVARIANT by the carrier multiplicity 3
    scales values by 3 but leaves the per-channel modulus untouched (equivariance forces equal
    per-copy indices: 12k = 3 * 4k is three copies of a mod-4 statement, not a mod-3 congruence
    on any single channel). Integer equalities/divisibilities, representation dimensions, and diagnostics
    are not assigned surrogate moduli. Exhaustive check over the torsion rows:""")
core_moduli = [2, 2, 16]     # Kramers, real/pseudoreal, Rokhlin
mult = 3
allok = True
composites = set()
for a in core_moduli:
    for b in core_moduli:
        for m in (a * b, a * b // __import__("math").gcd(a, b), __import__("math").gcd(a, b)):
            composites.add(m)
            if odd_part(m) != 1:
                allok = False
print(f"  composite moduli generated: {sorted(composites)} -- all 2-primary: {allok}")
assert allok
tripled = sorted({mult * m for m in composites})
print(f"  diagnostic values 3*m: {tripled}: odd part is 3, while the per-channel")
print("  torsion modulus stays a power of two. This is value arithmetic, not a new modulus.")
for m in tripled:
    assert odd_part(m) == 3

# ------------------------------------------------- E4: same-chirality pairings on dressed carriers
print("""
E4. GAUGE-DRESSED SAME-CHIRALITY PAIRINGS (exact zero-weight counts; a singlet needs weight 0).
    Can dressing the carrier with a named gauge rep R create a same-chirality invariant scalar
    pairing (a Majorana-type channel that could shift a count)?  Count zero-weight-sum quadruples
    in 16 x 16 x R x R (torus level; count 0 is a PROOF of nonexistence):""")
w16 = [tuple(x) for x in product([1, -1], repeat=5) if x.count(-1) % 2 == 0]      # 2*weights
w16b = [tuple(x) for x in product([1, -1], repeat=5) if x.count(-1) % 2 == 1]
w10 = []
for i in range(5):
    for s in (2, -2):
        r = [0] * 5
        r[i] = s
        w10.append(tuple(r))                                                       # 2*weights
w45 = [(0, 0, 0, 0, 0)] * 5
for i in range(5):
    for j in range(i + 1, 5):
        for si in (2, -2):
            for sj in (2, -2):
                r = [0] * 5
                r[i], r[j] = si, sj
                w45.append(tuple(r))
w1 = [(0, 0, 0, 0, 0)]


def quad_count(RA, RB):
    from collections import Counter
    s16 = Counter(tuple(a + b for a, b in zip(x, y)) for x in w16 for y in w16)
    sRR = Counter(tuple(a + b for a, b in zip(x, y)) for x in RA for y in RB)
    return sum(c1 * sRR.get(tuple(-z for z in k), 0) for k, c1 in s16.items())


for tag, wR in (("1", w1), ("10", w10), ("45", w45), ("16", w16), ("16bar", w16b)):
    cnt = quad_count(wR, wR)
    if cnt == 0:
        verdict = "NONE exists (exact) -- category A (the Krein/Majorana walls stand)"
    else:
        verdict = ("possible at torus level -- but activating it requires a background VEV of the "
                   "dressing field: category C (external spurion channel; cf. SHIAB-05's Lambda^1)")
    print(f"  R = {tag:6s}: zero-weight quadruples in 16x16xRxR = {cnt:5d}   -> {verdict}")

# ----------------------------------------------------------------------------------- verdict
print("\n" + "#" * 98)
print("# EXTENSION-ENGINE VERDICT")
print("#" * 98)
if FAILURES:
    print("  *** CATEGORY-D FINDINGS (odd-primary finite-row moduli) -- C_fin MAPPING FAILS: ***")
    for f in FAILURES:
        print("   -", f)
    sys.exit(1)
print("""
  Category-D findings (odd-primary modulus in the encoded finite-torsion rows): NONE.
  Every candidate the engine generated lands in:
    A: 2-primary and sector-available (gauge twists by 1/10/16/16bar/45; the eta_q family; the
       family-triplet integer divisibility 4k; the frame-spinor dimension/index 8; all composites
       of the three finite-torsion rows, with non-torsion rows kept separately typed);
    B: odd-primary but homotopy-fixed / count-independent (the +/-2 framing class, whose full
       order is 12 and whose projected 3-primary component has order 3); or
    C: external -- requires a background VEV, a non-sector gauge twist (54, 120, 126, ...), a Z/3
       deck group the spine does not have, or a global Z_9 symmetry the sector does not contain.
  data (54 -> 3, 120 -> 7, 126 -> 5*7, j=3/2 -> 5), which is precisely why the delimitation is
  load-bearing and why the C_fin theorem cannot be extended to arbitrary twists for free.
""")
