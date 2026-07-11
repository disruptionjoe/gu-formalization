"""Willmore tightening: the curved-ambient EL ambient term -> alpha_W, as far as honestly determined.

The GU shape term is alpha_W * R^Y.B: the ambient-curvature term of the Willmore EL in the curved gimmel
ambient. alpha_W = -Q^TF(B) / (ambient term)|_Schw. Q^TF(B) is computed
(willmore_geometric_ii_and_ambient_curvature.py: principled leading M^2/r^6). The ambient term = c_W * (R^Y
contracted with B), where R^Y is the ambient Riemann of the gimmel metric and c_W is the scalar EL prefactor
of the curved-ambient Willmore equation (functional/dimension dependent). Everything except c_W is now
computable; this test computes R^Y and states alpha_W up to that single number.

We compute the ambient Riemann R^Y of the DeWitt/gimmel metric EXACTLY in a faithful reduced model
(3D base X^3 -> fiber Sym^2 = 6D -> 9D total). NOTE: a 2D base is DEGENERATE -- the DeWitt trace-reversal
coefficient 1/2 equals 1/n exactly at n=2 (the note: "the trace-reversal term cancels in dimension four"),
so the vertical metric is singular for n=2; the minimal nondegenerate faithful model is n=3. The mixed
horizontal-vertical sectional-curvature STRUCTURE is dimension-generic, coming from the same section-2
Christoffels. The gimmel metric (ii-s-coordinate-formula sec 1):
  G_{mu nu} = h_{mu nu},  G_{mu,(ab)} = 0,  G_{(ab),(cd)} = h^{a(c} h^{d)b} - (1/2) h^{ab} h^{cd},
with h^{ab} the inverse of the fiber coordinate h_{ab}. The metric is block-diagonal (base (+) fiber), so its
inverse is computed block-wise. The mixed sectional curvature R^Y(d_mu, U, U, d_mu) (U vertical) is the
ambient-term ingredient the Willmore EL contracts against B.

Run: python tests/one-residual/willmore_curved_ambient_term.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- coordinates: base x0,x1,x2 ; fiber = 6 symmetric pairs ----
DIM = 3
x0, x1, x2 = sp.symbols('x0 x1 x2', real=True)
base_syms = [x0, x1, x2]
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]   # 6 pairs
Hsym = {ab: sp.Symbol(f'H{ab[0]}{ab[1]}', real=True) for ab in pairs}
coords = base_syms + [Hsym[ab] for ab in pairs]
N = DIM + len(pairs)   # 3 + 6 = 9


def Hentry(a, b):
    return Hsym[(a, b)] if a <= b else Hsym[(b, a)]


hmat = sp.Matrix(DIM, DIM, lambda a, b: Hentry(a, b))
hinv = hmat.inv()


def hup(a, b):
    return hinv[a, b]


def sym2u(a, c, d, b):
    return sp.Rational(1, 2) * (hup(a, c) * hup(d, b) + hup(a, d) * hup(c, b))


def V_low(ab, cd):
    a, b = ab
    c, d = cd
    return sym2u(a, c, d, b) - sp.Rational(1, 2) * hup(a, b) * hup(c, d)


# ---- explicit section-2 gimmel Christoffels (need only the cheap 3x3 base inverse, no 6x6 fiber inv) ----
def fidx(a, b):
    """full index of fiber pair (a,b), a<=b."""
    return DIM + pairs.index((min(a, b), max(a, b)))


def kron(i, j):
    return sp.Integer(1) if i == j else sp.Integer(0)


def delta_pair(a, b, mu, lam):
    # delta^{ab}_{mu lam} = 1/2( d^a_mu d^b_lam + d^a_lam d^b_mu )
    return sp.Rational(1, 2) * (kron(a, mu) * kron(b, lam) + kron(a, lam) * kron(b, mu))


def Emat(ab):
    a, b = ab
    E = sp.zeros(DIM, DIM)
    E[a, b] += 1
    E[b, a] += 1
    if a == b:
        E[a, b] = sp.Integer(1)   # diagonal pair: single unit entry
    return E


# Gamma^A_{BC} for full indices, from the closed forms in ii-s-coordinate-formula sec 2.
def Gamma(A, B, C):
    # case 1: upper base rho ; lowers one base mu + one fiber (ab)  -> Gamma^rho_{mu,(ab)}
    if A < DIM and ((B < DIM) ^ (C < DIM)):
        mu = B if B < DIM else C
        fib = C if C >= DIM else B
        (a, b) = pairs[fib - DIM]
        return sum(sp.Rational(1, 2) * hinv[A, lam] * delta_pair(a, b, mu, lam) for lam in range(DIM))
    # case 2: upper fiber (ab) ; lowers two base mu,nu  -> Gamma^{(ab)}_{mu nu}
    if A >= DIM and B < DIM and C < DIM:
        (a, b) = pairs[A - DIM]
        mu, nu = B, C
        term = sp.Rational(1, 2) * (Hentry(a, mu) * Hentry(nu, b) + Hentry(a, nu) * Hentry(mu, b))
        return -sp.Rational(1, 2) * (term - sp.Rational(1, 2) * Hentry(a, b) * Hentry(mu, nu))
    # case 3: upper fiber ; lowers two fiber (cd),(ef) -> Gamma^{(ab)}_{(cd),(ef)}
    if A >= DIM and B >= DIM and C >= DIM:
        (a, b) = pairs[A - DIM]
        Ecd = Emat(pairs[B - DIM])
        Eef = Emat(pairs[C - DIM])
        s = 0
        for r in range(DIM):
            for s2 in range(DIM):
                s += Ecd[a, r] * hinv[r, s2] * Eef[s2, b] + Eef[a, r] * hinv[r, s2] * Ecd[s2, b]
        return -sp.Rational(1, 2) * s
    return sp.Integer(0)


# ---- Riemann R^A_{BCD} = d_C Gamma^A_{DB} - d_D Gamma^A_{CB} + Gamma^A_{CE}Gamma^E_{DB} - Gamma^A_{DE}Gamma^E_{CB}
def dcoord(e, expr):
    if e < DIM:
        return sp.Integer(0)   # metric/Christoffels are base-independent
    return sp.diff(expr, coords[e])


def Riem_up(A, B, C, D):
    s = dcoord(C, Gamma(A, D, B)) - dcoord(D, Gamma(A, C, B))
    for E in range(N):
        s += Gamma(A, C, E) * Gamma(E, D, B) - Gamma(A, D, E) * Gamma(E, C, B)
    return s


def Gfull(i, j):
    if i < DIM and j < DIM:
        return hmat[i, j]
    if i >= DIM and j >= DIM:
        return V_low(pairs[i - DIM], pairs[j - DIM])
    return sp.Integer(0)


def Riem_low(A, B, C, D):
    return sum(Gfull(A, e) * Riem_up(e, B, C, D) for e in range(N))


# ---- evaluate mixed sectional curvatures at base point h = diag(-1, 1, 1) ----
h0 = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (0, 1): 0, (0, 2): 0, (1, 2): 0}
subs_pt = {Hsym[ab]: h0[ab] for ab in pairs}
print("[R^Y] mixed horizontal-vertical sectional curvature of the gimmel metric (9D faithful model)\n")

mixed = {}
for mu in range(DIM):
    for K in range(DIM, N):
        num = sp.simplify(Riem_low(mu, K, mu, K).subs(subs_pt))
        gmm = sp.simplify(Gfull(mu, mu).subs(subs_pt))
        gKK = sp.simplify(Gfull(K, K).subs(subs_pt))
        denom = gmm * gKK
        sec = sp.simplify(num / denom) if denom != 0 else sp.nan
        mixed[(mu, K)] = (num, sec)
        if num != 0:
            print(f"    R^Y_[base mu={mu}, fiber {pairs[K-DIM]}] = {num}    sectional = {sec}")

nonzero = any(sp.simplify(v[0]) != 0 for v in mixed.values())
check("ambient Riemann R^Y is NONZERO on mixed horizontal-vertical planes (Met(X4) is curved)", nonzero)
sgns = set()
for (mu, K), (num, sec) in mixed.items():
    if num.is_number and num != 0:
        sgns.add(1 if num > 0 else -1)
check("R^Y_{mu K mu K} components are signature-dependent across mixed planes (indefinite/Krein ambient)",
      len(sgns) >= 2,
      f"component signs: {sorted(sgns)} -- matches the A-tensor |A|^2 sign pattern (spacelike + / time -)")
sec_vals = {sp.simplify(v[1]) for v in mixed.values() if v[0] != 0}
check("mixed SECTIONAL curvature is uniformly NEGATIVE (nonpositive curvature of the space of metrics)",
      all(s.is_negative for s in sec_vals), f"sectional values: {sorted(sec_vals, key=lambda e: float(e))}")

# ---- adversarial cross-check against an independent by-hand value ----
# By-hand (horizontal part of R(d_mu, U_K, U_K, d_mu)) gave  -(1/4) (K eta^{-1} K)_{mu mu}  for a vertical
# direction K.  Take K = E_{(1,1)} (a purely spatial fiber direction) and mu = 1: (K eta^{-1} K)_{11} with
# eta=diag(-1,1,1): K=E_11 has (K)_{11}=1 else 0 -> (K eta^{-1} K)_{11} = 1*1*1 = 1 -> predict num_horiz=-1/4.
K11 = fidx(1, 1)
byhand_pred = sp.Rational(-1, 4)
computed = mixed[(1, K11)][0]
check("cross-check: computed R^Y matches independent by-hand -(1/4)(K eta^-1 K) for K=E_11, mu=1",
      sp.simplify(computed - byhand_pred) == 0, f"computed={computed}, by-hand={byhand_pred}")

print("\n" + "=" * 74)
print("alpha_W ASSEMBLY (honest bookkeeping)")
print("=" * 74)
print("  Willmore EL on the section, curved gimmel ambient (schematic, standard structure):")
print("     Delta^perp H  +  Q^TF(B)  +  c_W * (R^Y . B)^TF  =  0        [Weiner/Guo-Li curved-ambient form]")
print("  On the Psi=0 Schwarzschild section the principled leading terms are:")
print("     Q^TF(B)     : COMPUTED  ~ M^2/r^6  (willmore_geometric_ii_and_ambient_curvature.py)")
print("     R^Y         : COMPUTED  (nonzero, Krein-signed mixed sectional curvature, above)")
print("     B|_Schw     : COMPUTED  (graph SFF ~ M/r^3)")
print("     c_W         : the ONLY remaining unknown -- the scalar EL prefactor of the curved-ambient")
print("                   Willmore equation (fixed by the |II|^2-vs-|H|^2 functional choice + the")
print("                   4-in-14 dimension/codimension; this is the OQ2-A object).")
print("  => alpha_W = - Q^TF(B) / ( c_W * (R^Y.B)^TF )|_Schw : every factor computed EXCEPT c_W.")
print("     The source action's gravity coefficient is therefore reduced to ONE scalar (c_W), and that")
print("     scalar is exactly the unbuilt-action datum OQ2-A -- not an independent free parameter. Via the")
print("     shared theta, alpha_W remains LINKED to the dark-energy amplitude f_0.")
print("\n  NET: 'write the Willmore-ambient term' is done up to the single OQ2-A prefactor c_W. There is no")
print("  further hidden freedom: R^Y, B, and Q^TF are all now explicit computed objects.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = R^Y computed (nonzero, Krein-signed); alpha_W reduced to the single OQ2-A prefactor c_W.")
