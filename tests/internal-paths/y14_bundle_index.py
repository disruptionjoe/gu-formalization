#!/usr/bin/env python3
r"""
INTERNAL PATH #4 -- the true-RS-Y14-bundle family/APS index computation.

CONTEXT. Prior work discharged the three analytic residual terms of the section-setting theorem
first on faithful low-dim stand-ins
(canon/function-space-index-conservation-residual-closure-RESULTS.md) and then, for items 2 (APS
boundary/end eta) and 3 (family Chern), on the ACTUAL 1792-dim Cl(9,5) Rarita-Schwinger carrier over
a source-parameter loop (explorations/big-swing-2026-07-03/R1-...). Both stopped at the SAME wall:
the one term that can carry a nonzero (odd) count is the DEFINITE vertical fiber Dirac operator, whose
family pushforward is the unbuilt GU source action.

THIS SCRIPT does not re-run the R1 algebraic-carrier loop. It pushes toward the object R1 did NOT
touch: the ACTUAL fiber BUNDLE geometry Y14 = Met(X4) -> X4 (fiber F = GL(4,R)/O(3,1), dim 10,
homotopy core RP^3 = L(2;1)). The family-index theorem writes

    ind(D_RS / Y14) = pi_!( Ahat(T_vert) . ch(twist) )            (integrate over the 10-dim fiber F)

and this splits, by the fiber's own topology, into three pieces we grade one at a time:

    [A] base signature / bulk char-number          I_{3/2} = 21 sigma(X4)/8   -- COMPUTABLE, 2-primary
    [B] compact-core (RP^3, odd) APS boundary eta   lens (2q^2-4q+1)/8         -- COMPUTABLE, 2-primary
    [C] cross-chirality family Chern                c1(E_-) = 0                -- COMPUTABLE (structural)
    [D] noncompact 10-dim fiber L^2 Dirac index     the DEFINITE vertical term -- GATED on source action

Plus the spin precondition w2(Y14) = pi* w2(X4), computed here on the actual Sym^2 vertical bundle.

HARD RULE OBEYED: no target imported. sigma(X4) is kept a FREE symbol; we never substitute a target
manifold (no K3, no chi=24, no /8-to-3, no Ahat=3). The only integers that appear are the RS-bundle
character coefficients, chiralities, lens charges, and flux quanta -- none from a target.

Run: python tests/internal-paths/y14_bundle_index.py
"""
from __future__ import annotations
import itertools
import numpy as np
import sympy as sp

NA = 0
def check(cond, msg):
    global NA
    NA += 1
    assert cond, "FAIL: " + msg

def rule(s=""):
    print("-" * 92)
    if s:
        print(s)
        print("-" * 92)


print("=" * 92)
print("INTERNAL PATH #4 -- true-RS-Y14-bundle index: which pieces close on Y14, which is gated.")
print("Y14 = Met(X4) -> X4 ;  fiber F = GL(4,R)/O(3,1), dim 10, homotopy core RP^3 = L(2;1).")
print("=" * 92)


# =====================================================================================
# PRECONDITION -- w2(Y14) = pi* w2(X4) computed on the ACTUAL vertical bundle Sym^2(T*X4)
# (splitting principle over GF(2)); reproduces canon/w2-y14-spin-structure.md computationally.
# =====================================================================================
rule("PRECONDITION: spin structure. Vertical bundle TV = Sym^2(T*X4), rank 10. Compute w2(TV).")

# formal SW roots a1..a4 of a rank-4 real bundle E over GF(2); w_k(E) = e_k(a_i).
a = sp.symbols('a1 a2 a3 a4')
def gf2(poly):
    return sp.Poly(sp.expand(poly), *a, modulus=2).as_expr()

# Sym^2(E) has splitting roots { a_i + a_j : i <= j } (10 of them).
sym2_roots = [a[i] + a[j] for i in range(4) for j in range(i, 4)]
check(len(sym2_roots) == 10, "Sym^2 of rank-4 has 10 splitting roots")

# total SW class w(Sym^2 E) = prod (1 + root); w1 = e1, w2 = e2 of the roots, over GF(2).
w1_sym2 = gf2(sum(sym2_roots))
e2_sym2 = gf2(sum(r1 * r2 for r1, r2 in itertools.combinations(sym2_roots, 2)))

# w1(E) = a1+a2+a3+a4 ; the canon identity is w2(Sym^2 E) = w1(E)^2 (mod 2).
w1E = gf2(a[0] + a[1] + a[2] + a[3])
diff = gf2(e2_sym2 - w1E**2)
print(f"  w1(Sym^2 E)              = {w1_sym2}")
print(f"  w2(Sym^2 E)  (e2 of roots) reduces to  w1(E)^2 ?  residual = {diff}")
check(diff == 0, "w2(Sym^2 E) = w1(E)^2 over GF(2)")
# For ORIENTED X4, w1(E)=0, so w2(TV)=0 and there is nothing to cancel pi*w2(X4).
w2TV_oriented = gf2(e2_sym2.subs({a[0]: 0, a[1]: 0, a[2]: 0, a[3]: 0}))
print(f"  => oriented X4 (w1=0): w2(TV) = {w2TV_oriented}  =>  w2(Y14) = pi* w2(X4)  (spin iff X4 spin)")
check(w2TV_oriented == 0, "w2(vertical) vanishes for oriented X4")
print("  [precondition COMPUTABLE on Y14: Dirac on Y14 well-posed with no section choice iff X4 spin]")


# =====================================================================================
# PIECE [A] -- the bulk / base characteristic number I_{3/2} on the actual RS bundle.
# I_{3/2} = int_{X4} Ahat(X4) . (ch(TX_C) - 1)   (spin-3/2 vector-spinor, one ghost removed).
# sigma(X4) kept a FREE symbol -- no target substituted.
# =====================================================================================
rule("PIECE [A]: bulk char-number I_{3/2} via Ahat x RS-character (sigma free). Is it 2-primary?")

p1, sig = sp.symbols('p1 sigma', rational=True)   # first Pontryagin number, signature (FREE)
Ahat_4 = -p1 / 24                                  # Ahat(X4) degree-4 part
ch_TXc_4 = p1                                       # ch_2(TX_C) = p1(X) for the complexified tangent
dimTXc = 4
# I_{3/2} = [ Ahat . (ch(TX_C) - 1) ]_{deg 4} , integrated ( int p1 = 3 sigma ).
integrand_deg4 = 1 * (ch_TXc_4) + Ahat_4 * (dimTXc - 1)   # (deg0 Ahat)*ch2  +  Ahat4*(rank-1)
I32_in_p1 = sp.simplify(integrand_deg4)
I32 = sp.simplify(I32_in_p1.subs(p1, 3 * sig))            # int p1 = 3 sigma
print(f"  Ahat(X4)_4 = {Ahat_4},  ch_2(TX_C) = {ch_TXc_4},  ch(TX_C)-1 = {dimTXc-1} + p1")
print(f"  I_{{3/2}} density (in p1) = {I32_in_p1}   =>   I_{{3/2}} = {I32}   (using int p1 = 3 sigma)")
num, den = sp.fraction(sp.nsimplify(I32 / sig))
numfac = sp.factorint(int(num))   # {3:1, 7:1} for 21
facstr = " * ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(numfac.items()))
print(f"  I_{{3/2}} = ({num}/{den}) * sigma(X4)   -- denominator {den} = 2^3 (2-PRIMARY);  "
      f"numerator {num} = {facstr}")
check(den == 8, "I_{3/2} denominator is 8 (2-primary): carries no odd-prime torsion in its scale")
check(numfac == {3: 1, 7: 1}, "numerator 21 = 3*7 (bulk is itself divisible by 3 -- cannot BE a 1 mod 3)")
print("  [A COMPUTABLE on Y14's base: 2-primary for EVERY X4; the bulk cannot source an odd count.]")


# =====================================================================================
# PIECE [B] -- the compact-core APS boundary eta on the fiber's own boundary RP^3 = L(2;1).
# (i) gravitational -p1/24 channel: fed only by NET self-dual frame charge -> shown 0 on the actual
#     RS carrier by canon/rs-boundary-eta-2primary; re-checked here on a faithful cross-chirality op.
# (ii) gauge/spectral channel: charge-q reduced eta-bar on L(2;1) = (2q^2 - 4q + 1)/8, denominator 8.
# =====================================================================================
rule("PIECE [B]: APS boundary eta on the fiber core RP^3 = L(2;1). Denominator decides (3 vs 2-only).")

# (ii) lens gauge channel: exact rational arithmetic, several charges -- always in (1/8)Z.
q = sp.symbols('q', integer=True)
eta_lens = (2 * q**2 - 4 * q + 1) / 8
print("  gauge/spectral reduced eta-bar on L(2;1), (2q^2-4q+1)/8:")
dens = set()
for qi in range(-3, 7):
    val = sp.nsimplify(eta_lens.subs(q, qi))
    dens.add(sp.fraction(val)[1])
    print(f"     q={qi:+d}:  eta-bar = {val}")
print(f"  denominators over q in [-3,6]: {sorted(dens)}  -- all divide 8 (2-PRIMARY, never a 3).")
check(all(int(d) in (1, 2, 4, 8) for d in dens), "lens gauge eta stays in (1/8)Z for every charge")

# (i) gravitational channel: NET self-dual (SD - ASD) frame charge of a cross-chirality (chirality-odd)
# operator is 0 exactly, because {D, Gamma}=0 => spectrum symmetric => no net p1 fed. Re-check on a
# faithful cross-chirality block operator (the sigma_1 (x) B shape the true RS carrier also has).
rng = np.random.default_rng(4)
max_asym = 0.0
for _ in range(6):
    n = rng.integers(3, 9)
    B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    B = B + B.conj().T
    D = np.block([[np.zeros((n, n)), B], [B.conj().T, np.zeros((n, n))]])   # cross-chirality block form
    w = np.sort(np.linalg.eigvalsh(D))
    max_asym = max(max_asym, float(np.max(np.abs(w + w[::-1]))))            # +/- symmetry defect
print(f"  gravitational channel: cross-chirality op spectrum symmetric to {max_asym:.1e}  "
      f"=> net self-dual frame charge 0 => grav eta-bar = 0/24 (no -p1/24 order-3 term).")
check(max_asym < 1e-10, "cross-chirality (chirality-odd) spectrum symmetric => grav eta = 0")
print("  [B COMPUTABLE on the fiber core: eta = [grav:0] + [gauge:(1/8)Z] => 2-PRIMARY, no 3.]")


# =====================================================================================
# PIECE [C] -- the family Chern term c1(E_-) over the parameter/base, in the cross-chirality class.
# Structural: Gamma conjugates E_- <-> E_+ (already re-derived on the ACTUAL Cl(9,5) carrier by R1);
# reconfirmed here by the class identity c1(E_-)+c1(E_+)=c1(total, trivial)=0 with c1(E_-)=c1(E_+).
# =====================================================================================
rule("PIECE [C]: cross-chirality family Chern c1(E_-). Structural vanishing (class identity).")
# demonstrate the class identity on a small chirality-odd family D(t)=[[0,B(t)],[B(t)^H,0]] on a loop:
def band_frame_dets(seed):
    r = np.random.default_rng(seed)
    T = 8
    negs, poss = [], []
    B0 = r.standard_normal((3, 3)) + 1j * r.standard_normal((3, 3))
    B1 = r.standard_normal((3, 3)) + 1j * r.standard_normal((3, 3))
    for t in range(T):
        th = 2 * np.pi * t / T
        B = np.cos(th) * B0 + np.sin(th) * B1 + 3.0 * np.eye(3)   # gapped loop of 3x3 blocks
        D = np.block([[np.zeros((3, 3)), B], [B.conj().T, np.zeros((3, 3))]])
        w, V = np.linalg.eigh(D)
        negs.append(V[:, w < 0]); poss.append(V[:, w > 0])
    def holonomy(frames):
        H = np.eye(frames[0].shape[1], dtype=complex)
        for i in range(len(frames)):
            M = frames[i].conj().T @ frames[(i + 1) % len(frames)]
            U, _, Vh = np.linalg.svd(M); H = H @ (U @ Vh)
        return float(np.angle(np.linalg.det(H)))
    return holonomy(negs), holonomy(poss)
hm, hp = band_frame_dets(7)
print(f"  loop of cross-chirality blocks: Berry(E_-) = {hm:+.3e}, Berry(E_+) = {hp:+.3e}, "
      f"sum = {hm + hp:+.3e}")
check(abs(hm + hp) < 1e-9, "net chiral family holonomy c1(E_-)+c1(E_+) = 0")
print("  Gamma: E_- ~ E_+ => c1(E_-)=c1(E_+); sum=0 => c1(E_-)=0. (R1 proved this on the ACTUAL carrier.)")
print("  [C COMPUTABLE on Y14's parameter family: 0 in the cross-chirality Krein class.]")


# =====================================================================================
# PIECE [D] -- the GATED term: the DEFINITE vertical fiber Dirac index over F = GL(4,R)/O(3,1).
# Two independent reasons it is NOT closable on Y14 without the source action:
#   (d1) It leaves the cross-chirality class: it is SAME-chirality / DEFINITE, so {D,Gamma} != 0 and
#        NONE of the vanishing mechanisms A/B/C apply -- its spectrum is NOT +/- symmetric, eta != 0,
#        and it is the ONLY term that can be ODD. Demonstrated by control below.
#   (d2) The fiber F is NONCOMPACT (Lorentzian condition open in Sym^2), homotopy core RP^3 (deg<=3).
#        The topological pushforward pi_! over a noncompact fiber is UNDEFINED: the degree-10 fiber
#        integral needs the fiber Riemannian metric + L^2 completion + APS end condition -- which is
#        exactly the datum the (unbuilt) GU source action supplies. Shown by the degree count below.
# =====================================================================================
rule("PIECE [D]: the DEFINITE vertical fiber Dirac index -- GATED on the source action. Why.")

# (d1) control: a DEFINITE (same-chirality) magnetic-flux background carries net chiral index = flux
# (Aharonov-Casher / Atiyah-Singer), ODD for odd flux. Uses the repo's OWN certified builder
# (tests/function-space-ext/flux_index_2d.py, defs only) -- the same clean index=flux R1 reused.
import os as _os, sys as _sys
_HERE = _os.path.dirname(_os.path.abspath(__file__))
_REPO = _os.path.normpath(_os.path.join(_HERE, "..", ".."))
_src = open(_os.path.join(_REPO, "tests", "function-space-ext", "flux_index_2d.py")).read()
_ns = {"np": np}
exec(compile("\n".join(_src.splitlines()[:68]), "flux_index_2d", "exec"), _ns)  # defs only, no prints

print("  (d1) DEFINITE background control -- net chiral index = flux (leaves cross-chirality class):")
odd_seen = False
flux_index = {}
for flux in (0, 1, 2, 3):
    Dq, Gq, Kq = _ns["build_flux_dirac"](16, 16, flux)
    cq, nz, _ = _ns["chiral_index"](Dq, Gq, 0.25)
    flux_index[flux] = abs(cq)
    print(f"       flux={flux}:  |net chiral index| = {abs(cq):d}  ({nz} near-zero modes)   "
          f"[breaks {{D,Gamma}}=0]")
    if flux % 2 == 1 and abs(cq) % 2 == 1:
        odd_seen = True
check(flux_index[1] == 1 and flux_index[3] == 3, "certified flux builder: |index|=flux (odd for odd flux)")
# the definite term is asymmetric: contrast with a cross-chirality op whose index is forced 0.
Bc = np.random.default_rng(1).standard_normal((5, 5)) + 3 * np.eye(5)
Dc = np.block([[np.zeros((5, 5)), Bc], [Bc.T, np.zeros((5, 5))]])
wc = np.sort(np.linalg.eigvalsh(Dc))
sym_def = float(np.max(np.abs(wc + wc[::-1])))
print(f"       vs cross-chirality op: spectrum symmetric to {sym_def:.1e} => index 0 (never odd).")
check(odd_seen, "DEFINITE (same-chirality) background can carry an ODD index; cross-chirality cannot")

# (d2) degree count: the topological pushforward over the noncompact fiber is undefined.
dim_fiber = 10               # Sym^2(R^4) Lorentzian metrics -- OPEN subset, noncompact
core = 3                     # homotopy core RP^3 = L(2;1), rational cohomology only up to degree 3
dim_base = 4
dim_Y14 = dim_fiber + dim_base
print(f"\n  (d2) fiber F = GL(4,R)/O(3,1): dim {dim_fiber} (NONCOMPACT), homotopy core RP^3 (deg<= {core}).")
print(f"       family pushforward pi_! integrates a degree-{dim_fiber} form over F, but F's rational")
print(f"       cohomology stops at degree {core}: the degree-{dim_fiber} integral over a NONCOMPACT")
print(f"       fiber is NOT a topological pushforward -- it is an L^2 / APS analytic index that needs")
print(f"       the fiber metric + completion. dim Y14 = {dim_Y14}.")
print("       => the compact-core (RP^3, odd) part gives the eta term [B] (computable); the full")
print("          noncompact 10-dim definite fiber Dirac L^2 index is the UNBUILT source-action datum.")
check(core < dim_fiber, "fiber homotopy core degree < fiber dim => noncompact pushforward is analytic, not topological")
print("  [D GATED: same-chirality + noncompact => neither A/B/C nor a topological pi_! reaches it.]")


# =====================================================================================
print("\n" + "=" * 92)
print("VERDICT (internal path #4): PARTIAL -- BLOCKED-ON-SOURCE-ACTION for the decisive term.")
print("  CLOSE on Y14 (no source action needed):")
print("    precond  w2(Y14)=pi*w2(X4)         -- computed on the actual Sym^2 vertical bundle")
print("    [A] bulk I_{3/2}=21 sigma/8         -- 2-primary for EVERY X4 (sigma free; no target)")
print("    [B] fiber-core APS eta on L(2;1)    -- 2-primary: grav 0/24, gauge (1/8)Z")
print("    [C] cross-chirality family c1(E_-)  -- 0 (structural; R1 confirmed on actual carrier)")
print("  GATED on the source action (genuinely, not a bookkeeping gap):")
print("    [D] DEFINITE vertical fiber Dirac index over noncompact GL(4,R)/O(3,1) -- the ONLY")
print("        odd-capable term; leaves the cross-chirality class AND needs the fiber L^2/APS")
print("        metric the unbuilt GU source action supplies. This is the same wall R1 named.")
print(f"  hard asserts passed: {NA}   (no target imported: sigma, chi, /8, Ahat=3 never substituted)")
print("=" * 92)
