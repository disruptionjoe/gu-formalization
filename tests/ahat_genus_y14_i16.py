#!/usr/bin/env python3
r"""[A-hat(TY14)]_16 — the pure-gravitational anomaly density for a chiral field on Y^14.

CONTEXT (roadmap/meaningful-next-steps-2026-06-26.md, step 1; CORRECTION ANOMALY-01)
------------------------------------------------------------------------------------
The GU anomaly polynomial is I_16 = [A-hat(TY14) . ch_R(F)]_16. Its PURE-GRAVITATIONAL
part is [A-hat(TY14)]_16, a universal degree-16 characteristic form (a polynomial in the
Pontryagin classes p1..p4 of TY14), independent of the gauge group, the chiral module, and
the unwritten GU source action. It is the GU analog of the d=10 "tr R^8 must cancel" term.
This file computes it EXACTLY (rational coefficients) and verifies it two independent ways.

METHOD (no sympy, no numpy — exact Fraction arithmetic only)
------------------------------------------------------------
A-hat is the multiplicative genus with characteristic series Q(x) = (x/2)/sinh(x/2).
With u = x^2,  sinh(x/2)/(x/2) = sum_{m>=0} u^m / (4^m (2m+1)!) =: h(u), so
  log A-hat = sum_i log Q(x_i) = sum_i ( -log h(x_i^2) ) = sum_{k>=1} g_k * P_k,
where g(u) = -log h(u) = sum_k g_k u^k and P_k = sum_i (x_i^2)^k is the k-th power sum of
the Chern roots squared. Newton's identities turn P_k into the Pontryagin classes
p_j = e_j(x_i^2). Exponentiating and grading by weight (wt(p_j)=j, form-degree 4j):
  weight 1 -> [A-hat]_4,  weight 2 -> [A-hat]_8,  weight 3 -> [A-hat]_12,  weight 4 -> [A-hat]_16.

CROSS-CHECKS (the W2-01 discipline: never trust a coefficient without an independent recompute)
  (1) ALGORITHM: the SAME code must reproduce the canonical lower coefficients
        [A-hat]_4  = -p1/24
        [A-hat]_8  = (7 p1^2 - 4 p2)/5760
        [A-hat]_12 = (-31 p1^3 + 44 p1 p2 - 16 p3)/967680
      (universally tabulated; if these match, the engine is correct and [A-hat]_16 follows).
  (2) END-TO-END INDEX: integrating [A-hat]_16 over (K3)^4 must give the Dirac index
        A-hat[(K3)^4] = A-hat[K3]^4 = 2^4 = 16
      using the exact Pontryagin numbers of (K3)^4. This validates the degree-16 coefficients
      themselves (not just the lower ones) against a known integer index.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import factorial

WMAX = 4  # max weight kept (weight w <-> form-degree 4w); 4 -> degree 16

# Monomials in (p1,p2,p3,p4) keyed by exponent tuple; weight = e1 + 2e2 + 3e3 + 4e4.
KEY0 = (0, 0, 0, 0)


def wt(k):
    return k[0] + 2 * k[1] + 3 * k[2] + 4 * k[3]


def padd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pscale(a, c):
    return {k: v * c for k, v in a.items() if v * c != 0}


def pmul(a, b, wmax=WMAX):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = (ka[0] + kb[0], ka[1] + kb[1], ka[2] + kb[2], ka[3] + kb[3])
            if wt(k) <= wmax:
                out[k] = out.get(k, F(0)) + va * vb
    return {k: v for k, v in out.items() if v != 0}


# Newton: power sums P_k of the x_i^2 in terms of Pontryagin classes p_j = e_j(x_i^2).
P = {
    1: {(1, 0, 0, 0): F(1)},
    2: {(2, 0, 0, 0): F(1), (0, 1, 0, 0): F(-2)},
    3: {(3, 0, 0, 0): F(1), (1, 1, 0, 0): F(-3), (0, 0, 1, 0): F(3)},
    4: {(4, 0, 0, 0): F(1), (2, 1, 0, 0): F(-4), (1, 0, 1, 0): F(4),
        (0, 2, 0, 0): F(2), (0, 0, 0, 1): F(-4)},
}


def g_coeffs():
    """g_k for g(u) = -log h(u), h(u) = sum_m u^m/(4^m (2m+1)!), up to u^WMAX."""
    h = [F(1, 4 ** m * factorial(2 * m + 1)) for m in range(WMAX + 1)]  # h[0]=1
    # w = h - 1 (no constant term); log(1+w) = w - w^2/2 + w^3/3 - w^4/4
    w = [F(0)] + h[1:]  # length WMAX+1, w[0]=0

    def smul(a, b):  # series product truncated at u^WMAX
        r = [F(0)] * (WMAX + 1)
        for i in range(WMAX + 1):
            if a[i] == 0:
                continue
            for j in range(WMAX + 1 - i):
                r[i + j] += a[i] * b[j]
        return r

    logh = [F(0)] * (WMAX + 1)
    wn = [F(1)] + [F(0)] * WMAX  # w^0
    for n in range(1, WMAX + 1):
        wn = smul(wn, w)
        coef = F((-1) ** (n + 1), n)
        for i in range(WMAX + 1):
            logh[i] += coef * wn[i]
    return [F(0)] + [-logh[k] for k in range(1, WMAX + 1)]  # g[0]=0, g[1..WMAX]


def ahat_graded():
    """Return {weight: poly} for [A-hat]_{4*weight}, weight 0..WMAX."""
    g = g_coeffs()
    L = {}
    for k in range(1, WMAX + 1):
        L = padd(L, pscale(P[k], g[k]))
    # exp(L) = sum_n L^n / n!, truncated at weight WMAX
    acc = {KEY0: F(1)}
    Lpow = {KEY0: F(1)}
    for n in range(1, WMAX + 1):
        Lpow = pmul(Lpow, L)
        acc = padd(acc, pscale(Lpow, F(1, factorial(n))))
    graded = {w: {} for w in range(WMAX + 1)}
    for k, v in acc.items():
        graded[wt(k)][k] = v
    return graded


MONO = {(4, 0, 0, 0): "p1^4", (2, 1, 0, 0): "p1^2 p2", (0, 2, 0, 0): "p2^2",
        (1, 0, 1, 0): "p1 p3", (0, 0, 0, 1): "p4"}


def main():
    graded = ahat_graded()
    a4, a8, a12, a16 = graded[1], graded[2], graded[3], graded[4]

    print("=" * 78)
    print("[A-hat(TY14)]_16  —  pure-gravitational anomaly density (exact rationals)")
    print("=" * 78)

    # ---- CROSS-CHECK 1: canonical lower coefficients (validates the engine) ----
    exp4 = {(1, 0, 0, 0): F(-1, 24)}
    exp8 = {(2, 0, 0, 0): F(7, 5760), (0, 1, 0, 0): F(-4, 5760)}
    exp12 = {(3, 0, 0, 0): F(-31, 967680), (1, 1, 0, 0): F(44, 967680),
             (0, 0, 1, 0): F(-16, 967680)}
    assert a4 == exp4, f"[A-hat]_4 mismatch: {a4}"
    assert a8 == exp8, f"[A-hat]_8 mismatch: {a8}"
    assert a12 == exp12, f"[A-hat]_12 mismatch: {a12}"
    print("CROSS-CHECK 1 (canonical [A-hat]_4,8,12): PASS")
    print(f"   [A-hat]_4  = -p1/24")
    print(f"   [A-hat]_8  = (7 p1^2 - 4 p2)/5760")
    print(f"   [A-hat]_12 = (-31 p1^3 + 44 p1 p2 - 16 p3)/967680")

    # ---- the result ----
    print("\n[A-hat(TY14)]_16  (the GU pure-gravitational box term):")
    # find common denominator for readable display
    from math import gcd
    dens = [v.denominator for v in a16.values()]
    L = 1
    for d in dens:
        L = L * d // gcd(L, d)
    terms = []
    for k in sorted(a16, key=lambda kk: list(MONO).index(kk) if kk in MONO else 99):
        num = a16[k] * L
        assert num.denominator == 1
        terms.append(f"{int(num):+d} {MONO.get(k, str(k))}")
    print(f"   [A-hat]_16 = ( {'  '.join(terms)} ) / {L}")
    print("   coefficients:")
    for k in MONO:
        print(f"     {MONO[k]:9s}: {a16.get(k, F(0))}")

    # ---- CROSS-CHECK 2: end-to-end Dirac index on (K3)^4 = 2^4 = 16 ----
    # Pontryagin numbers of (K3)^4 (a_i = p1(K3_i), a_i^2=0, int a1a2a3a4 = A^4, A=int p1[K3]=-48):
    #   int p1^4 = 24 A^4, int p1^2 p2 = 12 A^4, int p2^2 = 6 A^4, int p1 p3 = 4 A^4, int p4 = A^4
    A = -48
    pont = {(4, 0, 0, 0): 24, (2, 1, 0, 0): 12, (0, 2, 0, 0): 6,
            (1, 0, 1, 0): 4, (0, 0, 0, 1): 1}
    integral = sum(a16.get(k, F(0)) * mult for k, mult in pont.items()) * (A ** 4)
    print(f"\nCROSS-CHECK 2 (end-to-end index on (K3)^4):")
    print(f"   int_(K3)^4 [A-hat]_16 = {integral}   (must equal A-hat[K3]^4 = 2^4 = 16)")
    assert integral == 16, f"index mismatch: got {integral}, expected 16"
    print("   PASS")

    # ---- CROSS-CHECK 3: second, independent index on HP^2 x HP^2 = A-hat[HP^2]^2 = 0 ----
    # HP^2: p1=2u, p2=7u^2, int u^2=1 (signature check: (7*7-2^2)/45 = 1 OK; A-hat[HP^2]=0).
    # Product HP^2 x HP^2 Pontryagin numbers (int u^2 v^2 = 1, u^3=v^3=0):
    pont2 = {(4, 0, 0, 0): 96, (2, 1, 0, 0): 88, (0, 2, 0, 0): 114,
             (1, 0, 1, 0): 56, (0, 0, 0, 1): 49}
    integral2 = sum(a16.get(k, F(0)) * mult for k, mult in pont2.items())
    print(f"\nCROSS-CHECK 3 (independent index on HP^2 x HP^2):")
    print(f"   int_(HP^2)^2 [A-hat]_16 = {integral2}   (must equal A-hat[HP^2]^2 = 0)")
    assert integral2 == 0, f"index mismatch: got {integral2}, expected 0"
    print("   PASS  (a different linear combination of the 5 coeffs -> independently pins them)")

    print("\n" + "=" * 78)
    print("RESULT: [A-hat(TY14)]_16 computed exactly; engine validated on the canonical")
    print("[A-hat]_4,8,12 and the degree-16 coefficients confirmed by TWO independent indices")
    print("((K3)^4 -> 16, HP^2xHP^2 -> 0). This is the universal GRAVITATIONAL density only;")
    print("it is NOT an anomaly-cancellation statement: the full I_16 multiplies it by the")
    print("chiral content ch_R(F) (Sp(64)/S=H^64) and the global eta/bordism leg stays OPEN.")
    print("=" * 78)
    return a16


if __name__ == "__main__":
    main()
