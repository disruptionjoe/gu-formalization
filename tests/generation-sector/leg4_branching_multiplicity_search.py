#!/usr/bin/env python3
"""LEG 4 -- adversarial BREAK attempt on the Multiplicity Theorem via BRANCHING MULTIPLICITY.

Mandate: find ANY GU-native, signature-class invariant that fixes the generation multiplicity to a
specific number -- ideally 3 -- WITHOUT import. If a GU-native rep contains exactly 3 copies of one SM
generation (the 16 of Spin(10)) robustly, the theorem BREAKS.

This is pure weight combinatorics on the COMPLEXIFIED GU structure group Spin(14) = D7 (the group whose
real forms are Spin(9,5)/Spin(7,7) -- both branch identically because branching multiplicities are a
property of the complexified root data, i.e. they are SIGNATURE-CLASS invariants, exactly the object the
mandate targets). The GU-native spinor is the 128 of Cl(14); the GU-native matter rep is its half-spinor
64 (one chirality). The SM generation = the 16 (positive-chirality spinor of Spin(10) = D5), the standard
SO(10) GUT generation that the verified Pati-Salam chain produces exactly one of.

We count: how many copies of the Spin(10) 16 appear in each GU-native rep, under every GU-native maximal
subgroup chain Spin(14) -> Spin(10) x (commutant). The multiplicity is the dimension of the commutant
"flavor" rep. We search ALL of them for a robust 3.

No bridge anchors are touched; this is rep theory orthogonal to the Clifford-norm anchors (58.72/155.36),
which the parity tests own. Run: python tests/generation-sector/leg4_branching_multiplicity_search.py
"""
from __future__ import annotations

import itertools
from collections import Counter

# ---------------------------------------------------------------------------
# Spinor weights of D_n (Spin(2n)) in the standard e_i basis: (+-1/2)^n.
# Positive chirality = even number of minus signs; negative = odd.
# ---------------------------------------------------------------------------

def spinor_weights(n, chirality):
    """Weights of a half-spinor of Spin(2n). chirality in {+1,-1}. Returns list of n-tuples of +-1/2."""
    out = []
    for signs in itertools.product((0.5, -0.5), repeat=n):
        nminus = sum(1 for s in signs if s < 0)
        chi = +1 if nminus % 2 == 0 else -1
        if chi == chirality:
            out.append(signs)
    return out


def full_spinor_weights(n):
    return [s for chi in (+1, -1) for s in spinor_weights(n, chi)]


def vector_weights(n):
    """Weights of the 2n vector of Spin(2n): +-e_i."""
    out = []
    for i in range(n):
        for sgn in (+1.0, -1.0):
            w = [0.0] * n
            w[i] = sgn
            out.append(tuple(w))
    return out


def adjoint_weights(n):
    """Nonzero roots of D_n: +-e_i +-e_j (i<j), plus n zero weights (Cartan)."""
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            for si in (+1.0, -1.0):
                for sj in (+1.0, -1.0):
                    w = [0.0] * n
                    w[i] = si
                    w[j] = sj
                    out.append(tuple(w))
    out += [tuple([0.0] * n)] * n  # rank-n Cartan
    return out


# ---------------------------------------------------------------------------
# Branch a list of D14-weights to a Levi/maximal-rank subgroup D5 x D_k x ...
# by SPLITTING the 7 orthonormal coordinates into blocks. Multiplicity of the
# Spin(10)=D5 positive spinor 16 = number of weights whose FIRST-5 block is a
# D5 positive-spinor weight, grouped by the COMPLEMENT block (the flavor weight).
# ---------------------------------------------------------------------------

def d5_pos_spinor_set():
    return set(spinor_weights(5, +1))   # the 16


def d5_neg_spinor_set():
    return set(spinor_weights(5, -1))   # the 16-bar


def count_16_multiplicity(weights, gen_set):
    """Given D7 weights (7-tuples), count how the D5(first 5) gen_set appears, keyed by complement (last 2)."""
    flavor = Counter()
    for w in weights:
        head = tuple(round(x / 0.5) * 0.5 for x in w[:5])
        tail = w[5:]
        if head in gen_set:
            flavor[tail] += 1
    return flavor


def report_rep(name, weights):
    gen16 = d5_pos_spinor_set()
    gen16bar = d5_neg_spinor_set()
    f16 = count_16_multiplicity(weights, gen16)
    f16bar = count_16_multiplicity(weights, gen16bar)
    n16 = sum(f16.values())
    n16bar = sum(f16bar.values())
    # the multiplicity of one full 16 = number of distinct flavor weights carrying a complete 16
    mult16 = len(f16)          # how many copies of the 16 (each complement weight = one copy)
    mult16bar = len(f16bar)
    print(f"  {name:34} dim={len(weights):4}  "
          f"#16-slots={n16:3} (mult {mult16})   #16bar-slots={n16bar:3} (mult {mult16bar})   "
          f"net_chiral_16 = {mult16 - mult16bar}")
    return mult16, mult16bar


# ---------------------------------------------------------------------------
def primes(n):
    n = abs(int(n)); f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def main():
    print("=" * 100)
    print("LEG 4: BRANCHING-MULTIPLICITY SEARCH for a GU-native, signature-class multiplicity = 3")
    print("Complexified GU structure group Spin(14)=D7; SM generation = 16 (pos spinor of Spin(10)=D5).")
    print("Branching multiplicities depend only on the root data -> SIGNATURE-CLASS invariants.")
    print("=" * 100)

    n = 7  # D7 = Spin(14)

    print("\n[1] GU-native reps branched to Spin(10) x Spin(4)  (D5 x D2, the standard SO(10)-GUT commutant):")
    print("    multiplicity of one 16 = dimension of the Spin(4)=SU(2)xSU(2) flavor rep it sits in.")
    half_pos = spinor_weights(n, +1)        # 64, GU-native matter half-spinor
    half_neg = spinor_weights(n, -1)        # 64-bar
    full = full_spinor_weights(n)           # 128, GU-native Dirac spinor (the bridge DIM)
    vec = vector_weights(n)                 # 14, the observerse vector
    adj = adjoint_weights(n)                # 91, gauge/adjoint

    results = {}
    results['half_pos_64'] = report_rep("half-spinor 64 (one chirality)", half_pos)
    results['half_neg_64'] = report_rep("half-spinor 64-bar (other chir.)", half_neg)
    results['full_128'] = report_rep("full Dirac spinor 128 (bridge DIM)", full)
    results['vector_14'] = report_rep("vector 14 (observerse)", vec)
    results['adjoint_91'] = report_rep("adjoint 91 (gauge)", adj)

    print("\n[2] EXHAUSTIVE search over ALL GU-native maximal-rank subgroup splits Spin(10) x H,")
    print("    H = commutant from putting D5 on ANY 5 of the 7 coordinates; flavor = remaining 2 coords.")
    print("    Looking for ANY rep whose 16-multiplicity (or net chiral 16-count) is exactly 3:")
    gen16 = d5_pos_spinor_set()
    gen16bar = d5_neg_spinor_set()
    found3 = []
    reps = {'half64': half_pos, 'half64bar': half_neg, 'full128': full, 'vec14': vec, 'adj91': adj}
    for coords in itertools.combinations(range(n), 5):
        comp = tuple(c for c in range(n) if c not in coords)
        for rname, W in reps.items():
            mult = Counter()
            multbar = Counter()
            for w in W:
                head = tuple(w[c] for c in coords)
                tail = tuple(w[c] for c in comp)
                if head in gen16:
                    mult[tail] += 1
                if head in gen16bar:
                    multbar[tail] += 1
            m, mb = len(mult), len(multbar)
            net = m - mb
            if 3 in (m, mb, abs(net)) or m == 3 or mb == 3 or abs(net) == 3:
                found3.append((coords, rname, m, mb, net))
    if found3:
        print(f"    *** FOUND multiplicity/net 3 in {len(found3)} (split, rep) cases: ***")
        for c, r, m, mb, net in found3[:20]:
            print(f"      D5 on coords {c}, rep {r}: mult16={m}, mult16bar={mb}, net={net}")
    else:
        print("    NONE. No GU-native maximal-rank D5 split of any GU-native rep gives multiplicity or")
        print("    net chiral count = 3. Every multiplicity is a power of 2 (1,2,4) -- the Spin(4) flavor")
        print("    rep dimension -- never the odd prime 3.")

    print("\n[3] Why 3 is structurally excluded (the C-04 mechanism, re-derived for branching):")
    print("    A GU-native generation multiplicity = dim of a SPINOR rep of the commutant Spin(2k).")
    print("    Spinor dims of Spin(2k) are 2^(k-1): {1,2,4,8,...} -- powers of 2. The odd prime 3 is")
    print("    never a half-spinor dimension, so it can never be a GU-native branching multiplicity.")
    for k in range(0, 5):
        sdim = 2 ** (k - 1) if k >= 1 else 1
        print(f"      commutant Spin({2*k}): half-spinor dim = {sdim}  primes={sorted(primes(sdim)) if sdim>1 else '[]'}")

    print("\n[4] Dimension-spectrum reconfirm (C-04, signature-independent):")
    for label, d in [("spinor 128", 128), ("half 64", 64), ("RS space 14*128", 14 * 128),
                     ("ker Gamma 1664", 1664), ("adjoint Spin14 91", 91), ("|Weyl(D7)|", 2**6 * 5040)]:
        f = primes(d)
        flag = "  <-- contains 3 !" if 3 in f else ""
        print(f"      {label:22} = {d:7}  primes={sorted(f)}{flag}")

    print("\n[5] SHARPEST BREAK ATTEMPT: shrink the gauge group so the commutant grows to rank 3,")
    print("    which could host a HORIZONTAL SU(3) with the families in its fundamental 3.")
    print("    - Minimal even-orthogonal group holding ONE 16: Spin(10) (spinor 16). Spin(8) spinor=8<16,")
    print("      so the 16 cannot fit in any Spin(2k<10): Spin(10) is FORCED, using 5 of 7 coordinates.")
    print("    - Spin(10) x Spin(4) is then forced (5+2 coords); the family group is exactly the Spin(4)")
    print("      commutant. On a Spin(14) spinor the module factorizes spinor(D5) (x) spinor(D2), so the")
    print("      family rep IS a Spin(4) half-spinor = the 2. A horizontal SU(3) (rank 2, dim 8) does NOT")
    print("      embed in Spin(4)=su(2)+su(2) (dim 6), so no GU-native horizontal SU(3) commutes with the")
    print("      16-generating Spin(10): the '3 of SU(3)_family' route is NOT GU-native.")
    su3_in_spin4 = (8 <= 6)  # dim su(3)=8 cannot fit in dim su(2)+su(2)=6
    fits16_below10 = any(2 ** (k - 1) >= 16 for k in range(1, 5))  # Spin(2k<10) half-spinor >=16?
    print(f"      SU(3) fits in Spin(4) commutant? {su3_in_spin4}.  16 fits in some Spin(2k<10)? {fits16_below10}.")
    print("    - Net chirality of the flat 64 under Spin(10): #16 - #16bar = 2 - 2 = 0 (vector-like).")
    print("      The family index is non-chiral at rep level -- matching C-05 (metric connections give 0):")
    print("      chirality is NOT a branching multiplicity at all, so '3' cannot be read off the rep.")

    print("\n[6] de Rham of the GU fiber GL(4,R)/O(3,1) ~ RP^3 x R+ (homotopy RP^3); Betti over Q:")
    print("      b0=1, b1=0, b2=0, b3=1  -> Euler char 0, total dim 2. No 3 in the fiber cohomology.")

    print("\n[7] VERDICT")
    any3 = bool(found3)
    print(f"    Any GU-native rep with a robust multiplicity-3 of the SM generation? {any3}")
    print("    Branching multiplicities found: 16 sits in Spin(4) doublets -> multiplicity 2 (or 4 in the")
    print("    full Dirac 128); the verified Pati-Salam chain isolates exactly ONE. Never 3.")
    print("    The ONLY place 3 appears is |Weyl(D7)| = 2^10 * 3^2 * 5 * 7 -- a GROUP-ORDER factor, not a")
    print("    rep multiplicity; it counts Weyl chambers, not generations, and cannot be read as a count.")
    return results, found3


if __name__ == "__main__":
    main()
