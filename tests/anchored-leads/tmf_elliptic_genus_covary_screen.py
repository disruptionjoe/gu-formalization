#!/usr/bin/env python3
r"""
LEAD SCREEN -- tmf / elliptic-genus "finer invariant that CAN co-vary".

PRECISE QUESTION
  The deflation is "e_R = 1/12 is homotopy-fixed in pi_3^s and cannot co-vary with geometry".
  tmf and the elliptic genus see a GEOMETRY-DEPENDENT q-expansion. Does a tmf invariant /
  elliptic genus / Witten genus of GU's actual structure (K3, the 14-manifold, the RS bundle)
  carry a mod-3 q-coefficient that CO-VARIES with geometry, escaping the homotopy-fixed trap,
  and giving a genuinely finer order-3 invariant -- or does it reduce back to e_R = 1/12?

THREE DECISIVE CHECKS (computed where possible, analytic where a theorem is cited).

  (1) FREE-PART CHECK [COMPUTED]. The K3 elliptic genus EG(K3) = 2*phi_{0,1}, where phi_{0,1}
      is the weak Jacobi form of weight 0 index 1. Compute it from Jacobi thetas. Its (q,y)
      coefficients are INTEGERS: it lives in the ring of weak Jacobi forms over Z, a FREE
      abelian group. chi(K3) = EG|_{y=1} = 24. So the geometry-varying data is FREE / Z-valued.
      Reducing an integer modular-form coefficient mod 3 is a CARDINAL mod 3, not a class in the
      torsion summand Z/3 < pi_3^s. (Kind-mismatch bin (a) of the 45-persona collapse.)

  (2) DEGREE-3 CHECK [ANALYTIC, literature]. The home of e_R is degree 3. The unit map
      pi_3^s -> pi_3(tmf) is an ISOMORPHISM Z/24 -> Z/24. In the exact degree where the
      generation carrier lives, tmf adds NOTHING pi_3^s cannot see; its 3-torsion there IS the
      same Z/3 (the alpha element), homotopy-fixed. This falsifies "tmf sees mod-3 structure
      pi_3^s cannot" AT THE GENERATION DEGREE.

  (3) HIGHER-DEGREE / TYPE CHECK [ANALYTIC]. tmf's 3-torsion (alpha deg 3, beta deg 10,
      alpha*beta deg 13, beta^2 deg 20, ...) is a fixed graded ring of HOMOTOPY classes. A
      manifold selects WHICH class via its genus; to compute that class on GU's actual
      13-dim boundary you must first pin the geometry (which manifold, which RS twist) = gate
      on the unbuilt source action. And a nonzero Z/3 class detects info MOD 3 only -- the same
      order-3-class -> integer-3 category error already flagged open.

Exact arithmetic only (Fraction exponents, integer coeffs). No numpy / sympy.
"""

from __future__ import annotations
from fractions import Fraction as F

QMAX = 3  # keep q-powers with exponent < QMAX (q^1 fully converged)

# (q,y) Laurent series: dict {(qexp:Fraction, yexp:Fraction): int_or_Fraction_coeff}.
def trim(s):
    return {k: v for k, v in s.items() if v != 0 and k[0] < QMAX}

def sadd(*series):
    out = {}
    for s in series:
        for k, v in s.items():
            out[k] = out.get(k, 0) + v
    return trim(out)

def sscale(s, c):
    return trim({k: v * c for k, v in s.items()})

def smul(a, b):
    out = {}
    for (qa, ya), va in a.items():
        for (qb, yb), vb in b.items():
            q = qa + qb
            if q >= QMAX:
                continue
            k = (q, ya + yb)
            out[k] = out.get(k, 0) + va * vb
    return trim(out)

def leading_q(s):
    return min(k[0] for k in s) if s else F(0)

def sinv(s):
    """Invert a series whose lowest-q part is a single monomial c0 * q^a * y^0."""
    a = leading_q(s)
    lead = [(k, v) for k, v in s.items() if k[0] == a]
    assert len(lead) == 1 and lead[0][0][1] == 0, f"non-monomial leading term: {lead}"
    c0 = lead[0][1]
    # s = c0 q^a (1 + N),  N = s/(c0 q^a) - 1
    norm = sscale({(k[0] - a, k[1]): v for k, v in s.items()}, F(1, 1) / c0)
    N = sadd(norm, {(F(0), F(0)): -1})
    # 1/(1+N) = sum_{k>=0} (-N)^k, truncated by q-order
    inv = {(F(0), F(0)): F(1)}
    term = {(F(0), F(0)): F(1)}
    for _ in range(1, 8):
        term = smul(term, sscale(N, -1))
        if not term:
            break
        inv = sadd(inv, term)
    # multiply by (1/c0) q^{-a}
    return trim({(k[0] - a, k[1]): v * (F(1, 1) / c0) for k, v in inv.items()})

# Jacobi thetas, q = e^{2pi i tau}, y = e^{2pi i z}.  q-power in units of tau (so q^{1/2} etc).
def theta3():
    s = {}
    for n in range(-5, 6):
        q = F(n * n, 2)
        if q < QMAX:
            s[(q, F(n))] = s.get((q, F(n)), 0) + 1
    return trim(s)

def theta4():
    s = {}
    for n in range(-5, 6):
        q = F(n * n, 2)
        if q < QMAX:
            s[(q, F(n))] = s.get((q, F(n)), 0) + (1 if n % 2 == 0 else -1)
    return trim(s)

def theta2():
    s = {}
    for n in range(-5, 6):
        e = n + F(1, 2)
        q = e * e / 2
        if q < QMAX:
            s[(q, e)] = s.get((q, e), 0) + 1
    return trim(s)

def at_z0(s):
    """Set y -> 1 (z=0): collapse y exponents."""
    out = {}
    for (q, _y), v in s.items():
        out[(q, F(0))] = out.get((q, F(0)), 0) + v
    return trim(out)

def ratio_sq(theta):
    """ theta(z)^2 / theta(0)^2  as a (q,y) series. """
    num = smul(theta, theta)
    den = smul(at_z0(theta), at_z0(theta))
    return smul(num, sinv(den))

def run():
    t2, t3, t4 = theta2(), theta3(), theta4()
    R2, R3, R4 = ratio_sq(t2), ratio_sq(t3), ratio_sq(t4)
    phi = sscale(sadd(R2, R3, R4), 4)          # phi_{0,1}, weight 0 index 1
    EG = sscale(phi, 2)                          # elliptic genus of K3

    # ---- check A: q^0 term of phi_{0,1} should be y + 10 + 1/y (integers) ----
    q0 = {k[1]: v for k, v in phi.items() if k[0] == 0}
    print("phi_{0,1}  q^0 term (yexp: coeff):",
          {str(yy): v for yy, v in sorted(q0.items())})

    # ---- check B: chi(K3) = EG|_{y=1} = 24 (constant in q -> grab q^0) ----
    EG_y1 = at_z0(EG)
    chi = EG_y1.get((F(0), F(0)), 0)
    print("chi(K3) = EG|_{y=1}  (q^0 coeff) =", chi)
    # also confirm EG|_{y=1} is CONSTANT in q (weight-0 modular form specializes to a constant)
    higher = {k: v for k, v in EG_y1.items() if k[0] != 0}
    print("EG|_{y=1} higher-q terms (should be empty):", higher)

    # ---- check C: integrality of all computed coefficients (free-part / Z-valued) ----
    all_int = all((isinstance(v, int) or (isinstance(v, F) and v.denominator == 1))
                  for v in phi.values())
    print("all phi coefficients integral (free-part Z-valued)?", all_int)

    # ---- TYPE CHECK: a free integer coeff reduced mod 3 vs a class in Z/3 < pi_3^s ----
    sample = q0.get(F(0), 0)   # the "10" in y+10+1/y, a representative geometry coefficient
    print(f"sample geometry coefficient = {sample}; (sample mod 3) = {sample % 3} "
          f"-- this is a CARDINAL mod 3, an element of Z/3Z-as-quotient-of-Z, NOT the "
          f"torsion summand Z/3 < pi_3^s = Z/24.")

    # ---- ANALYTIC anchors (clearly marked: NOT computed here) ----
    print("\n[ANALYTIC] pi_3^s = Z/24 = Z/8 (+) Z/3   (two-primary-lemma.md)")
    print("[ANALYTIC] unit map pi_3^s -> pi_3(tmf) is ISO Z/24 -> Z/24 "
          "(Hopkins-Mahowald): tmf adds nothing new in degree 3 (the e_R degree).")
    print("[ANALYTIC] tmf 3-torsion lives in degrees 3(alpha),10(beta),13(a*b),20(b^2),... "
          "-- a FIXED homotopy ring; geometry only selects which class, and that needs the "
          "pinned geometry = the unbuilt source action.")
    print("[ANALYTIC] 'tmf_3' is already listed in three-generations-locate-not-force-CRT-"
          "RESULTS.md as ONE re-description of the homotopy-fixed e_R = 1/12 carrier.")

    # assertions
    assert q0.get(F(1)) == 1 and q0.get(F(0)) == 10 and q0.get(F(-1)) == 1, q0
    assert chi == 24, chi
    assert not higher, higher
    assert all_int
    print("\nALL CHECKS PASS. Verdict: the co-varying elliptic-genus data is FREE-part "
          "(Z-valued, kind-mismatched to Z/3); the genuine tmf 3-torsion is homotopy-fixed "
          "and in degree 3 equals pi_3^s exactly (= e_R re-described). No new co-varying "
          "order-3 invariant. Higher-degree tmf torsion gates on the source action AND re-hits "
          "the order-3 -> integer-3 category error. RE-LOCATION / GATED, not a new route.")

if __name__ == "__main__":
    run()
