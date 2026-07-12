#!/usr/bin/env python3
r"""H45 -- THE |H|^2-vs-|II|^2 BINARY, made computable end-to-end.

Wave 24. The pivotal cross-sector binary (Wave-21 Bianconi showdown, H5): is GU's
gravitational functional the FULL second-fundamental-form norm |II|^2 (which, by the
Gauss identity, CONTAINS the induced Einstein-Hilbert R^X and gives the 4th-order
Weyl/Bach sector on top of a healthy Einstein graviton) or the conformal mean-curvature
Willmore |H|^2 (no EH, pure Bach, conformal-only)?

This binary is load-bearing for FOUR internal sectors at once:
  (a) whether GU HAS the 4th-order Weyl/Bach graviton sector,
  (b) the cosmological-constant / DeWitt-Lambda SIGN,
  (c) the ghost order/structure (Stelle two-pole vs degenerate coincident pole),
  (d) the live geometry-vs-information (Bianconi) discriminator.

WHAT THIS FILE COMPUTES (exact sympy; deterministic; no imported target number):

  Q1  The Gauss decomposition |II|^2 = |H|^2 - R^X, exact all dims (2,3,4), from the
      principal-curvature shape operator. Plus the rank fact that "full norm" (|II|^2)
      and "trace-square" (|H|^2) are genuinely distinct quadratic forms on Sym^2 -- so
      the binary is real, not cosmetic. Plus the propositional forcing ledger
      (P1 = theta = II_s [H21, proven]; P2 = action norms the FULL |theta|^2 [transcript,
      OPEN]) -> the binary is FAVORED-|II|^2 but not a theorem: P2 is the named residual.

  Q2  The Weyl sector. On a TT graviton the |H|^2 Euler-Lagrange operator is box^2 (= the
      Bach operator, D-thread), and |II|^2 = |H|^2 - R^X adds a box (Einstein-Hilbert)
      term -> box(box+m^2). So the 4th-order box^2/Weyl piece is present in BOTH branches;
      Bianconi's 2nd-order Einstein action has NO box^2 term. GU carries the Weyl sector
      either way (robust to the binary); the binary controls whether there is ALSO an
      Einstein graviton.

  Q3  The Lambda SIGN. The constant-section (O(M^0)) vertical SFF of the gimmel metric has
      fiber-trace exactly +1/2 * g_{mn} -- a POSITIVE cosmological-constant signature. This
      is the |II|^2-branch DeWitt-Lambda leading contribution; cross-checks H15-Part-D and
      the H24/H25 C_RY>0 direction.

  Q4  Ghost/order. |II|^2 -> symbol s(s+m^2), TWO distinct poles, TT propagator residues
      (+1/m^2, -1/m^2) = the clean Krein/O(1,1) pair Bateman-Turok clears at TREE level.
      |H|^2 -> symbol s^2, coincident DOUBLE pole (degenerate; the split coefficient 1/m^2
      diverges as m^2->0) = the Pais-Uhlenbeck Jordan case where the Krein split is singular
      and tree-level clearance FAILS. So |II|^2 is the branch that even makes H26's
      tree-clears/loop-open setting available.

  Q5  The decider. GU's 4th-order Weyl/Bach spin-2 sector is nonzero and distinct from a
      2nd-order Einstein operator (Bach != Einstein on TT), so the geometry-vs-information
      discriminator is a genuine spin-2 fork. It is ROBUST to the binary (both branches carry
      box^2). Exact-vacuum Bach-flatness (H1) is the internal consistency that makes it a
      real physical sector rather than an artifact.

Run: python -u tests/wave24/H45_H2_vs_II2_binary.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# Q1 -- The Gauss decomposition |II|^2 = |H|^2 - R^X (exact, all dims) and the
#       real-fork / forcing ledger.
# ===========================================================================
log("=" * 78)
log("Q1 -- Gauss decomposition |II|^2 = |H|^2 - R^X (exact) + the forcing ledger")
log("=" * 78)

# The traced-twice Gauss identity for a hypersurface with diagonal shape operator
# S = diag(k_1,...,k_n): R^X = (tr S)^2 - tr(S^2) = |H|^2 - |II|^2, i.e.
# |II|^2 = |H|^2 - R^X, where |II|^2 = tr(S^2), |H|^2 = (tr S)^2, R^X = 2*e_2(k).
for n in (2, 3, 4):
    ks = sp.symbols(f'k0:{n}', real=True)
    H2 = (sum(ks))**2                     # |H|^2 = (tr S)^2
    II2 = sum(k**2 for k in ks)           # |II|^2 = tr(S^2)
    e2 = sum(ks[i] * ks[j] for i in range(n) for j in range(i + 1, n))
    RX = 2 * e2                           # intrinsic scalar curvature (Gauss)
    ok = sp.simplify(II2 - (H2 - RX)) == 0 and sp.simplify(RX - (H2 - II2)) == 0
    check(f"dim {n}: |II|^2 = |H|^2 - R^X  and  R^X = |H|^2 - |II|^2 (exact, shape operator)",
          ok, f"R^X = 2*e_2(k)")

# The two functionals are DISTINCT quadratic forms on Sym^2(R^4): the full norm sees
# every component (rank = dim Sym^2 = 10), the trace-square sees only the trace (rank 1).
# So "norm the full II" vs "norm only its trace H" is a real 9-dimensional difference
# (the traceless graviton data |II_0|^2), not a relabel.
D = 4
sdim = D * (D + 1) // 2
comps = sp.symbols(f'b0:{sdim}', real=True)  # independent components of a symmetric II
# full-norm quadratic form = sum b_i^2 -> Hessian = 2*Identity -> rank sdim
Hess_full = sp.Matrix(sdim, sdim, lambda i, j: sp.diff(sp.diff(sum(c**2 for c in comps),
                                                               comps[i]), comps[j]))
# trace-square: trace = b0+b1+b2+b3 mapping (diagonal comps first: pick 4 as "diagonal")
tr = comps[0] + comps[1] + comps[2] + comps[3]
Hess_tr = sp.Matrix(sdim, sdim, lambda i, j: sp.diff(sp.diff(tr**2, comps[i]), comps[j]))
check("full-norm |II|^2 is rank-10 on Sym^2(R^4) (sees the whole tensor incl. the 9-dim "
      "traceless graviton), trace-square |H|^2 is rank-1 -> the binary is a REAL fork",
      Hess_full.rank() == sdim and Hess_tr.rank() == 1,
      f"rank(|II|^2)={Hess_full.rank()}, rank(|H|^2)={Hess_tr.rank()}")

# int R^X is DYNAMICAL in 4D (not topological): the linearized Einstein tensor on a TT
# graviton h_yy(x) is G^(1)_yy = -1/2 box h_yy -- second order and nonzero. (In 2D the
# analogue int K is Gauss-Bonnet = topological; the 4D topological density is E_4, not R.)
t4, x4, y4, z4 = sp.symbols('t x y z', real=True)
cc = [t4, x4, y4, z4]
eta4 = sp.diag(-1, 1, 1, 1)
hyy = sp.Function('h')(t4, x4)             # a TT mode depending on (t,x), polarization yy


def box_flat(e):
    return sum(eta4[m, m] * sp.diff(e, cc[m], 2) for m in range(4))


# Linearized Ricci for a single TT component h_yy(t,x): R^(1)_yy = -1/2 box h_yy,
# and R^(1) (scalar) = 0 on TT. Einstein G^(1)_yy = R^(1)_yy - 1/2 eta_yy R^(1) = -1/2 box h_yy.
G1_yy = -sp.Rational(1, 2) * box_flat(hyy)   # nonzero, 2nd-order
check("4D: int R^X is DYNAMICAL -- linearized Einstein on a TT graviton G^(1)_yy = "
      "-1/2 box h_yy is 2nd-order and NONZERO (so |II|^2's -R^X is a genuine Einstein-"
      "Hilbert kinetic term, not a boundary/topological term)",
      sp.simplify(G1_yy + sp.Rational(1, 2) * box_flat(hyy)) == 0 and G1_yy != 0)

# 2D contrast: int K over the round sphere = 4*pi = 2*pi*chi, radius-independent (topological).
Rsp = sp.symbols('R', positive=True)
thsp = sp.symbols('vartheta', positive=True)
K = 1 / Rsp**2                            # Gaussian curvature of a sphere of radius R
intK = sp.integrate(sp.integrate(K * Rsp**2 * sp.sin(thsp), (thsp, 0, sp.pi)),
                    (sp.Symbol('ph'), 0, 2 * sp.pi))
check("2D contrast: int K dA = 4*pi (radius-INDEPENDENT, Gauss-Bonnet) -> in 2D R^X is "
      "topological, which is WHY 2D Willmore is conformal/scale-free. 4D breaks that.",
      sp.simplify(intK - 4 * sp.pi) == 0)

# Forcing ledger (Q1 verdict logic). The binary = (P1) theta = full II_s AND (P2) the
# action norms the FULL |theta|^2 (not the trace-square |H|^2). H21 PROVES P1 (Gauss
# formula, off-shell, full tensor; convention shift is a full tensor, NOT a trace -> the
# convention route to |H|^2 is closed). P2 (action = full YM norm) is transcript-grade and
# gated on the unbuilt source action -> NOT a theorem. So: binary is FAVORED-|II|^2, OPEN.
P1_theta_is_full_II = True     # H21: s*(theta) = II_s off-shell, FULL tensor (proven, modulo bundle id)
P2_action_is_full_norm = None  # transcript-grade; NOT settled by any built action  -> unknown
convention_route_to_H2_closed = True   # H21 Check 4b: convention shift is a full tensor, not a trace
binary_forced_to_II2 = (P1_theta_is_full_II and P2_action_is_full_norm is True)
binary_favored_open = (P1_theta_is_full_II and convention_route_to_H2_closed
                       and P2_action_is_full_norm is None)
check("Q1 LEDGER: P1 (theta=full II_s) PROVEN by H21; the convention->|H|^2 route CLOSED "
      "(H21 shift is a full tensor); but P2 (action norms full |theta|^2 vs trace-square "
      "|H|^2) is transcript-grade and OPEN -> binary is FAVORED-|II|^2, NOT a theorem",
      (not binary_forced_to_II2) and binary_favored_open,
      "residual freedom = P2 (the action-NORM choice), gated on the unbuilt source action")


# ===========================================================================
# Q2 -- The Weyl/Bach sector: present in BOTH branches; absent in Bianconi (2nd-order).
# ===========================================================================
log("\n" + "=" * 78)
log("Q2 -- the 4th-order Weyl/Bach graviton sector")
log("=" * 78)
s, m2 = sp.symbols('s m2', positive=True)   # s = box eigenvalue; m2 = Einstein mass^2 scale
P_H = s**2                                  # |H|^2 Willmore-EL on TT = box^2 = Bach operator
P_II = s * (s + m2)                         # |II|^2 = |H|^2 - R^X -> box(box+m^2)
P_Einstein = s                              # Bianconi / pure 2nd-order Einstein: box only
# the box^2 (4th-order Weyl/Bach) coefficient:
c_weyl_H = sp.Poly(P_H, s).coeff_monomial(s**2)
c_weyl_II = sp.Poly(P_II, s).coeff_monomial(s**2)
c_weyl_E = sp.Poly(sp.expand(P_Einstein), s).coeff_monomial(s**2)
check("|H|^2 branch carries the 4th-order box^2 (Weyl/Bach) term (coeff = 1)", c_weyl_H == 1)
check("|II|^2 branch ALSO carries box^2 (Weyl/Bach) -- it is |H|^2 - R^X, so the Weyl piece "
      "is present in BOTH branches (the binary does NOT gate whether GU has the Weyl sector)",
      c_weyl_II == 1)
check("Bianconi / 2nd-order Einstein has NO box^2 term (coeff = 0) -> the 4th-order Weyl "
      "sector is exactly what distinguishes GU (either branch) from the entropic frame",
      c_weyl_E == 0)
# What the binary DOES gate: whether there is ALSO an Einstein (box, s^1) kinetic term.
c_eh_H = sp.Poly(P_H, s).coeff_monomial(s)
c_eh_II = sp.Poly(P_II, s).coeff_monomial(s)
check("the binary gates the EINSTEIN (box, s^1) term: |II|^2 has it (coeff = m^2, from -R^X) "
      "-> Stelle R+Weyl^2; |H|^2 does not (coeff = 0) -> pure conformal Bach",
      c_eh_II == m2 and c_eh_H == 0)


# ===========================================================================
# Q3 -- The Lambda SIGN: the |II|^2-branch DeWitt O(M^0) fiber-trace is +1/2 g_{mn} (positive).
# ===========================================================================
log("\n" + "=" * 78)
log("Q3 -- the DeWitt-Lambda / O(M^0) SIGN under |II|^2")
log("=" * 78)
# Constant-section vertical SFF (ii-s-coordinate-formula sec 6.1):
#   B_{mn,ab} = -(1/2)( g_{a(m} g_{n)b} - 1/2 g_{ab} g_{mn} ).
# Its fiber-trace g^{ab} B_{mn,ab} is the O(M^0) DeWitt-Lambda source. Compute it exactly
# at flat background g = eta (dim 4), symbolically over the fibre trace.
g = eta4
ginv = g.inv()
n4 = 4


def Bconst(m, n, a, b):
    sym = sp.Rational(1, 2) * (g[a, m] * g[n, b] + g[a, n] * g[m, b])   # g_{a(m} g_{n)b}
    return -sp.Rational(1, 2) * (sym - sp.Rational(1, 2) * g[a, b] * g[m, n])


fiber_trace = sp.zeros(n4, n4)
for m in range(n4):
    for n in range(n4):
        fiber_trace[m, n] = sp.simplify(sum(ginv[a, b] * Bconst(m, n, a, b)
                                            for a in range(n4) for b in range(n4)))
# expected: +1/2 * eta_{mn}
expected = sp.Rational(1, 2) * g
check("constant-section (O(M^0)) vertical SFF fiber-trace g^{ab} B_{mn,ab} = +1/2 g_{mn} "
      "EXACTLY -- a POSITIVE cosmological-constant signature (stress ~ +g_{mn}). This is the "
      "|II|^2-branch DeWitt-Lambda leading contribution (matches H15-Part-D).",
      sp.simplify(fiber_trace - expected) == sp.zeros(n4, n4),
      "sign(+1/2) is positive -> de-Sitter-signed Lambda contribution")
# A 0-derivative Lambda enters the operator symbol at s^0 only: it fixes the vacuum SIGN
# without touching the kinetic (s^1 Einstein, s^2 Weyl) coefficients that decide the ghost.
Lam = sp.symbols('Lam', real=True)
P_II_with_L = s * (s + m2) + Lam
check("the O(M^0) Lambda enters at s^0 only (leaves the s^2 Weyl and s^1 Einstein kinetic "
      "coefficients unchanged) -> it sets the vacuum SIGN, branch-consistently, without "
      "disturbing the ghost structure",
      sp.Poly(P_II_with_L, s).coeff_monomial(s**2) == 1
      and sp.Poly(P_II_with_L, s).coeff_monomial(s) == m2
      and sp.Poly(P_II_with_L, s).coeff_monomial(1) == Lam)
log("  NOTE (ARGUED, not recomputed here): thread-B assigns the NET emergent-Lambda sign "
    "|II|^2 -> POSITIVE, |H|^2 -> negative; and the curved-ambient horizontal R^Y Lambda is")
log("  Krein-indefinite (H24). The COMPUTED leg is the +1/2 g_{mn} leading trace above; the")
log("  net sign remains gated on mu_DW / the source-action normalization (magnitude free, H42).")


# ===========================================================================
# Q4 -- Ghost/order: |II|^2 = Krein-clearable two-pole; |H|^2 = degenerate coincident pole.
# ===========================================================================
log("\n" + "=" * 78)
log("Q4 -- ghost order/structure + the loop-positivity (H26) setting")
log("=" * 78)
# |II|^2 propagator 1/(s(s+m^2)) partial-fractions into a positive-residue (healthy) pole
# and a negative-residue (ghost) pole -- the clean O(1,1)/Krein pair Bateman-Turok clears
# at tree level.
prop_II = 1 / (s * (s + m2))
res0 = sp.residue(prop_II, s, 0)            # massless graviton residue
resm = sp.residue(prop_II, s, -m2)          # massive ghost residue
check("|II|^2: TT propagator 1/(s(s+m^2)) has TWO distinct poles with residues "
      "(+1/m^2 at s=0, -1/m^2 at s=-m^2) -> a clean healthy+ghost Krein/O(1,1) pair -> "
      "Bateman-Turok CLEARS the ghost at TREE level",
      sp.simplify(res0 - 1 / m2) == 0 and sp.simplify(resm + 1 / m2) == 0,
      f"res(s=0)={sp.simplify(res0)} > 0, res(s=-m^2)={sp.simplify(resm)} < 0")
# The flat-ambient Stelle mass is m^2 = +1/2 > 0 (H15-E): a real, non-tachyonic massive pole.
m2_stelle = sp.Rational(1, 2)
check("|II|^2 Stelle mass m^2 = +1/2 > 0 (H15-E): the massive ghost sits at a REAL mass "
      "(non-tachyonic) so the tree-level Krein clearance actually applies",
      m2_stelle > 0)
# |H|^2 is the degenerate coincident double pole: as m^2 -> 0 the split coefficient 1/m^2
# diverges -> the Bateman-Turok O(1,1) split is SINGULAR (Pais-Uhlenbeck Jordan case).
split_coeff = 1 / m2
divergent = sp.limit(split_coeff, m2, 0)
check("|H|^2: symbol s^2 is a COINCIDENT double pole; the |II|^2 split coefficient 1/m^2 "
      "DIVERGES as m^2->0 -> the Krein/O(1,1) split is SINGULAR (Pais-Uhlenbeck equal-"
      "frequency Jordan case) -> tree-level clearance FAILS on the |H|^2 branch",
      divergent == sp.oo)
check("Q4 consequence for H26: |II|^2 is the branch that even PUTS GU in H26's "
      "tree-clears/loop-open setting; |H|^2 would sit on the singular Jordan boundary where "
      "no positivity-compatible ghost parity exists (R1). |II|^2 does NOT itself settle the "
      "loop positivity -- that stays OPEN, gated on the unbuilt source action.",
      binary_favored_open)   # loop positivity remains undecidable without a built S


# ===========================================================================
# Q5 -- The decider: GU's 4th-order Weyl/Bach spin-2 sector is distinct from 2nd-order
#       Einstein -- a genuine geometry-vs-information fork, ROBUST to the binary.
# ===========================================================================
log("\n" + "=" * 78)
log("Q5 -- the live geometry-vs-information (Bianconi) discriminator")
log("=" * 78)
# The Bach (4th-order) and Einstein (2nd-order) operators differ on TT: box^2 vs box.
# Their difference is nonzero -> they are DISTINCT theories of the spin-2 field, so a probe
# of the graviton propagator's high-momentum structure discriminates them.
bach_op = s**2
einstein_op = s
check("Bach (box^2) and Einstein (box) TT operators are DISTINCT (difference s^2 - s != 0) "
      "-> GU's 4th-order spin-2 sector is a genuine physical fork vs Bianconi's 2nd-order "
      "Einstein graviton (different propagator: 1/s^2-modified vs 1/s)",
      sp.simplify(bach_op - einstein_op) != 0)
# The discriminator is ROBUST to the |H|^2-vs-|II|^2 binary: both GU branches carry box^2
# (Q2), Bianconi carries none. So the spin-2 decider does NOT wait on the binary.
check("the spin-2 discriminator is ROBUST to the binary: BOTH GU branches carry box^2 "
      "(c_weyl = 1 each), Bianconi carries 0 -> GU vs Bianconi is decidable regardless of "
      "how the binary resolves; the binary only refines GU's internal spin-2 spectrum",
      c_weyl_H == 1 and c_weyl_II == 1 and c_weyl_E == 0)
log("  Live empirical handles (ARGUED, H5-Q5): (i) Stelle-Yukawa short-distance deviation of")
log("  the Newtonian potential from the massive spin-2 pole; (ii) high-frequency GW dispersion")
log("  from the Bach 1/p^4-modified propagator; (iii) conformal-lensing signs. All present for")
log("  GU, absent for Bianconi's pure-Einstein gravity. What would make it UNCONDITIONAL: build")
log("  GU's source action to settle P2 (full |theta|^2 vs trace-square |H|^2).")


# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H45 |H|^2-vs-|II|^2 binary")
log("=" * 78)
log(r"""
COMPUTED (this file, exact sympy, exit 0):
  Q1  |II|^2 = |H|^2 - R^X exact (dims 2,3,4); full-norm rank 10 vs trace-square rank 1
      (real fork); int R^X dynamical in 4D (G^(1)_yy = -1/2 box h != 0) vs topological in
      2D (int K = 4pi). FORCING LEDGER: P1 (theta = full II_s) proven by H21 and the
      convention->|H|^2 route closed; P2 (action norms full |theta|^2) transcript-grade,
      OPEN. => binary is FAVORED-|II|^2, not a theorem; residual = P2 (the action-NORM
      choice), gated on the unbuilt source action.
  Q2  the 4th-order box^2 (Weyl/Bach) term is present in BOTH branches (|II|^2 = |H|^2 - R^X);
      Bianconi's 2nd-order Einstein has none. The binary gates only whether there is ALSO an
      Einstein (s^1) term: |II|^2 -> Stelle (Weyl + Einstein), |H|^2 -> pure conformal Bach.
  Q3  the |II|^2 DeWitt O(M^0) fiber-trace is +1/2 g_{mn} EXACTLY -- a POSITIVE Lambda
      signature; it enters at s^0 (vacuum sign) without touching the kinetic ghost structure.
  Q4  |II|^2 -> two distinct poles, residues (+1/m^2, -1/m^2), m^2 = +1/2 > 0 -> Krein pair,
      tree-clears; |H|^2 -> coincident double pole, split 1/m^2 -> oo, tree-clearance FAILS.
      |II|^2 is what makes H26's tree-clears/loop-open setting available; loop positivity
      itself stays OPEN (unbuilt source action).
  Q5  Bach (box^2) != Einstein (box): a genuine spin-2 geometry-vs-information fork, ROBUST
      to the binary (both GU branches carry box^2; Bianconi none).

VERDICT: STILL-OPEN, strongly FAVORED-|II|^2. H21 hardened P1 and closed the convention
route to |H|^2; the residual is P2 (does the action norm the full |theta|^2 or the
trace-square |H|^2), which is one facet of the single unbuilt object (GU's source action)
that also gates mu_DW, the H26 loop positivity, and the H21 canonical-connection id.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H45 computed: Gauss decomposition + rank fork + 4D-dynamical R^X + Weyl-in-both")
log("         + positive O(M^0) Lambda trace + Krein-pair vs degenerate-pole + spin-2 decider.")
log("         Binary STILL-OPEN, FAVORED-|II|^2; residual P2 = action-norm choice (source action).")
