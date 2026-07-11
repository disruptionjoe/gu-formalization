"""THREAD A2 -- an INDEPENDENT NUMERICAL diff-geo oracle for the gimmel/DeWitt metric.

Purpose. The gimmel-metric ambient Riemann R^Y and the O'Neill A-tensor norm |A|^2 used in the
alpha_W / Willmore arc were computed SYMBOLICALLY from CLOSED-FORM Christoffel symbols that were
transcribed by hand from ii-s-coordinate-formula-2026-06-23.md section 2
(tests/one-residual/willmore_curved_ambient_term.py and willmore_geometric_ii_and_ambient_curvature.py).
A transcription or sign error in those closed forms would silently corrupt every downstream number.

This oracle is a SECOND, INDEPENDENT derivation. It NEVER uses the closed-form Christoffels. It builds
ONLY the metric tensor G (from the DeWitt/gimmel DEFINITION -- block-diagonal base (+) trace-reversed
Frobenius fiber) as an mpmath function of the fiber coordinates, then runs the GENERIC Levi-Civita
machinery numerically:

    Gamma^A_{BC} = (1/2) G^{AD} ( d_B G_{DC} + d_C G_{DB} - d_D G_{BC} )
    R^A_{BCD}    = d_C Gamma^A_{DB} - d_D Gamma^A_{CB} + Gamma^A_{CE} Gamma^E_{DB} - Gamma^A_{DE} Gamma^E_{CB}

with all metric partial derivatives obtained by HIGH-PRECISION FINITE DIFFERENCES (mpmath.diff, 40 dps).
The Christoffel derivatives d_C Gamma are assembled ANALYTICALLY from the finite-differenced first and
second metric partials (via d_C G^{AE} = -G^{AP}(d_C G_{PQ})G^{QE}), so there is exactly one FD layer on
the metric -- no fragile nested differencing.

WHAT THE ORACLE FOUND (honest -- it is an audit, not a rubber stamp). Run in BOTH the geometrically
correct 'doubled' coordinate basis (d/dh_ab = E_ab+E_ba for a<b -- the genuine tangent vector, since the
single coordinate h_ab=h_ba drives both matrix entries) and the symbolic tests' non-doubled basis:

  CONFIRMED (convention-robust; two independent derivations agree):
    * DIAGONAL-fiber R^Y = +/-1/4, sectional = -1/2; the by-hand R^Y = -1/4;  DIAGONAL |A_00|^2=|A_11|^2=1/8;
    * R^Y is NONZERO and Krein-signed (both signs present) -- the alpha_W ambient term stays a real object.

  CORRECTED (the adversarial finding): the symbolic tests' OFF-DIAGONAL magnitudes -- the -5/8 sectional in
    willmore_curved_ambient_term.py and |A_12|^2=1/16 in willmore_geometric_ii_and_ambient_curvature.py --
    match NEITHER consistent convention. They come from MIXING the non-doubled metric V_low (for index
    lowering) with closed-form Christoffels of a different pair-normalization. In the honest coordinate basis
    the invariants are: mixed sectional = -1/8 off-diagonal (so Met has UNIFORMLY non-positive curvature
    {-1/2, -1/8}, cleaner than -5/8) and |A|^2 = 1/8 uniformly (Krein sign). No alpha_W/Willmore CONCLUSION
    depends on the off-diagonal magnitude, so nothing breaks -- the qualitative story is strengthened.

This is exactly what a second independent derivation is for: it ratifies the robust content and localizes a
normalization artifact in the off-diagonal numbers. The test EXITS 0 by asserting this verified picture.

NOTHING is fit to a target: the only input is the DeWitt metric DEFINITION. No 24, no 8, no chi.

Run: python tests/threads/A_numerical_diffgeo_oracle.py
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
TOL = mp.mpf(10) ** (-8)

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def close(val, rational, tol=TOL):
    target = mp.mpf(int(sp.numer(rational))) / mp.mpf(int(sp.denom(rational)))
    return abs(mp.mpf(val) - target) < tol


# ===========================================================================
# Generic gimmel/DeWitt metric builder for a DIM-dimensional base.
# Coordinates: DIM base coords (metric is base-independent) + Sym^2 fiber pairs h_ab (a<=b).
# G_{mu nu} = h_{mu nu};  G_{mu,(ab)} = 0;  G_{(ab),(cd)} = h^{a(c}h^{d)b} - (1/2) h^{ab}h^{cd}.
# ===========================================================================
def _tr(M):
    return sum(M[i, i] for i in range(M.rows))


def _Smat(DIM, a, b):
    """The tangent vector d/dh_{ab} as an element of Sym(DIM): the HONEST coordinate basis.

    For a<b the single fiber coordinate h_{ab}=h_{ba} controls BOTH off-diagonal matrix entries, so
    d/dh_{ab} = E_{ab}+E_{ba}. For a==b it is E_{aa}. This 'doubling' is the crux of the convention audit.
    """
    M = mp.zeros(DIM, DIM)
    M[a, b] += 1
    M[b, a] += 1
    if a == b:
        M[a, b] = mp.mpf(1)
    return M


def make_model(DIM, doubled=True):
    """DeWitt/gimmel metric on DIM-base -> Sym^2 fiber.

    doubled=True  : the geometrically HONEST metric -- fiber-fiber block = V_h(S_ab, S_cd) on the true
                    coordinate tangent vectors S (off-diagonal directions doubled). This is the correct
                    Riemannian metric on the space of metrics in the {h_ab : a<=b} chart.
    doubled=False : the NON-doubled 'tensor-component' form V_{ab,cd}(h) = h^{a(c}h^{d)b} - (1/2)h^{ab}h^{cd}
                    used by the existing symbolic tests (treats each symmetric-pair index as independent).
                    Kept as a switch so the oracle can exhibit BOTH conventions and identify which the
                    symbolic closed-form numbers correspond to.
    """
    pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
    NF = len(pairs)
    N = DIM + NF

    def hmat_from_pt(pt):
        h = mp.zeros(DIM, DIM)
        for k, (a, b) in enumerate(pairs):
            v = pt[DIM + k]
            h[a, b] = v
            h[b, a] = v
        return h

    def G_component(pt, D, E):
        # base-base block: G_{mu nu} = h_{mu nu} -> the corresponding fiber coordinate
        if D < DIM and E < DIM:
            a, b = min(D, E), max(D, E)
            return pt[DIM + pairs.index((a, b))]
        # cross block vanishes
        if (D < DIM) ^ (E < DIM):
            return mp.mpf(0)
        # fiber-fiber block
        h = hmat_from_pt(pt)
        hinv = h ** -1
        (a, b) = pairs[D - DIM]
        (c, d) = pairs[E - DIM]
        if doubled:
            SA = _Smat(DIM, a, b)
            SB = _Smat(DIM, c, d)
            return _tr(hinv * SA * hinv * SB) - mp.mpf(1) / 2 * _tr(hinv * SA) * _tr(hinv * SB)
        sym = mp.mpf(1) / 2 * (hinv[a, c] * hinv[d, b] + hinv[a, d] * hinv[c, b])
        return sym - mp.mpf(1) / 2 * hinv[a, b] * hinv[c, d]

    return pairs, NF, N, G_component


# ===========================================================================
# Finite-difference metric partials via mpmath.diff (single FD layer on the metric).
# Base-direction derivatives are exactly 0 (metric is base-independent) -- set analytically.
# ===========================================================================
def build_partials(pt, DIM, N, G_component):
    """Return dG[c][d][e] = d_c G_{de} and ddG[(c1,c2)][d][e] = d_c1 d_c2 G_{de} at pt.

    Only fiber directions (>= DIM) can be nonzero; base directions return 0.
    All derivatives via mpmath.diff (Richardson-extrapolated central differences).
    """
    pt = [mp.mpf(v) for v in pt]

    # first partials dG[c][d][e]
    dG = [[[mp.mpf(0)] * N for _ in range(N)] for _ in range(N)]
    for c in range(DIM, N):  # fiber directions only
        for d in range(N):
            for e in range(d, N):
                def f(x, d=d, e=e, c=c):
                    q = list(pt)
                    q[c] = x
                    return G_component(q, d, e)
                val = mp.diff(f, pt[c])
                dG[c][d][e] = val
                dG[c][e][d] = val

    # second partials ddG[(c1,c2)][d][e], symmetric in (c1,c2) and (d,e)
    ddG = {}
    fiber = list(range(DIM, N))
    for i, c1 in enumerate(fiber):
        for c2 in fiber[i:]:
            for d in range(N):
                for e in range(d, N):
                    if c1 == c2:
                        def f(x, d=d, e=e, c=c1):
                            q = list(pt)
                            q[c] = x
                            return G_component(q, d, e)
                        val = mp.diff(f, pt[c1], 2)
                    else:
                        def f(x1, x2, d=d, e=e, a=c1, b=c2):
                            q = list(pt)
                            q[a] = x1
                            q[b] = x2
                            return G_component(q, d, e)
                        val = mp.diff(f, (pt[c1], pt[c2]), (1, 1))
                    ddG[(c1, c2, d, e)] = val
                    ddG[(c1, c2, e, d)] = val
                    ddG[(c2, c1, d, e)] = val
                    ddG[(c2, c1, e, d)] = val
    return dG, ddG


# ===========================================================================
# Assemble Christoffel, its derivative, and Riemann from the FD metric partials.
# ===========================================================================
def diffgeo(pt, DIM, N, G_component):
    Gmat = mp.matrix(N, N)
    for d in range(N):
        for e in range(N):
            Gmat[d, e] = G_component(pt, d, e)
    Ginv = Gmat ** -1
    dG, ddG = build_partials(pt, DIM, N, G_component)

    def Gam(A, B, C):
        s = mp.mpf(0)
        for E in range(N):
            s += Ginv[A, E] * (dG[B][E][C] + dG[C][E][B] - dG[E][B][C])
        return mp.mpf(1) / 2 * s

    # cache Gamma
    Gamma = [[[Gam(A, B, C) for C in range(N)] for B in range(N)] for A in range(N)]

    def dGinv(c, A, E):
        # d_c G^{AE} = - G^{AP} (d_c G_{PQ}) G^{QE}
        s = mp.mpf(0)
        for P in range(N):
            for Q in range(N):
                s += Ginv[A, P] * dG[c][P][Q] * Ginv[Q, E]
        return -s

    def dGamma(c, A, D, B):
        # d_c Gamma^A_{DB}
        s = mp.mpf(0)
        for E in range(N):
            inner = dG[D][E][B] + dG[B][E][D] - dG[E][D][B]
            dinner = (ddG.get((c, D, E, B), mp.mpf(0))
                      + ddG.get((c, B, E, D), mp.mpf(0))
                      - ddG.get((c, E, D, B), mp.mpf(0)))
            s += dGinv(c, A, E) * inner + Ginv[A, E] * dinner
        return mp.mpf(1) / 2 * s

    def Riem_up(A, B, C, D):
        s = dGamma(C, A, D, B) - dGamma(D, A, C, B)
        for E in range(N):
            s += Gamma[A][C][E] * Gamma[E][D][B] - Gamma[A][D][E] * Gamma[E][C][B]
        return s

    def Riem_low(A, B, C, D):
        s = mp.mpf(0)
        for E in range(N):
            s += Gmat[A, E] * Riem_up(E, B, C, D)
        return s

    return Gmat, Ginv, Gamma, Riem_low


def sectional(Rlow, Gmat, mu, K):
    return Rlow(mu, K, mu, K) / (Gmat[mu, mu] * Gmat[K, K])


# ===========================================================================
# PART 1 -- ambient Riemann R^Y of the 9D faithful model (3D base -> 6D fiber).
#   Run BOTH conventions consistently: the geometrically HONEST 'doubled' coordinate basis and the
#   NON-doubled 'tensor-component' basis the symbolic tests use for index lowering. This is an
#   adversarial audit, not a copy: we let the numbers decide which reported values are convention-robust.
# ===========================================================================
print("=" * 78)
print("PART 1: numerical R^Y of the gimmel metric (9D faithful model), FD from the metric")
print("=" * 78)

DIM = 3
h0 = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (0, 1): 0, (0, 2): 0, (1, 2): 0}

pairs3, _, N3, G3H = make_model(DIM, doubled=True)     # HONEST coordinate basis
_, _, _, G3N = make_model(DIM, doubled=False)          # non-doubled (symbolic-test convention)
pt = [mp.mpf(0)] * DIM + [mp.mpf(h0[p]) for p in pairs3]
GmatH, _, _, RlowH = diffgeo(pt, DIM, N3, G3H)
GmatN, _, _, RlowN = diffgeo(pt, DIM, N3, G3N)

# what the symbolic willmore_curved_ambient_term.py REPORTS (raw R^Y_{mu K mu K} and sectional):
sym_raw = {
    (0, (0, 0)): sp.Rational(1, 4), (1, (1, 1)): sp.Rational(-1, 4), (2, (2, 2)): sp.Rational(-1, 4),
    (0, (0, 1)): sp.Rational(-5, 16), (0, (0, 2)): sp.Rational(-5, 16), (1, (0, 1)): sp.Rational(5, 16),
    (1, (1, 2)): sp.Rational(-5, 16), (2, (0, 2)): sp.Rational(5, 16), (2, (1, 2)): sp.Rational(-5, 16),
}

print("\n  mixed sectional curvature  K(d_mu, fiber) -- HONEST(doubled) vs NON-doubled vs symbolic-report:")
print("    (a symmetric-pair fiber direction (a,b), a<b, is DIAGONAL if a==b else OFF-DIAGONAL)")
diag_ok = True
honest_secs = set()
nond_offdiag_pos = True
for mu in range(DIM):
    for kpair in pairs3:
        K = DIM + pairs3.index(kpair)
        if abs(RlowH(mu, K, mu, K)) < mp.mpf(10) ** (-7):
            continue
        secH = sectional(RlowH, GmatH, mu, K)
        secN = sectional(RlowN, GmatN, mu, K)
        is_diag = (kpair[0] == kpair[1])
        symsec = (sym_raw[(mu, kpair)] / (GmatN[mu, mu] * GmatN[K, K])) if (mu, kpair) in sym_raw else None
        honest_secs.add(mp.nstr(secH, 6))
        tag = "DIAG " if is_diag else "OFF  "
        print(f"    mu={mu} {tag}{kpair}:  honest={mp.nstr(secH, 6):>9}   nondoubled={mp.nstr(secN, 6):>9}   "
              f"symbolic-report={symsec}")
        if is_diag and not close(secH, sp.Rational(-1, 2)):
            diag_ok = False
        if (not is_diag) and secN <= 0:
            nond_offdiag_pos = False

# (1) convention-ROBUST content: the DIAGONAL-fiber raw components and the by-hand value.
K11 = DIM + pairs3.index((1, 1))
byhandH = RlowH(1, K11, 1, K11)
byhandN = RlowN(1, K11, 1, K11)
check("PART 1a: DIAGONAL-fiber raw R^Y = +/-1/4 and sectional = -1/2 in BOTH conventions (convention-robust; "
      "confirms the symbolic diagonal values)",
      diag_ok and close(byhandH, sp.Rational(-1, 4)) and close(byhandN, sp.Rational(-1, 4)),
      f"by-hand R^Y(d1,E11,d1,E11) = {mp.nstr(byhandH, 8)} (honest) = {mp.nstr(byhandN, 8)} (nondoubled)")

# (2) the honest geometry: mixed sectional uniformly NEGATIVE, exactly {-1/2 diag, -1/8 off-diag}
honest_neg_uniform = honest_secs == {mp.nstr(mp.mpf(-1) / 2, 6), mp.nstr(mp.mpf(-1) / 8, 6)}
check("PART 1b: HONEST (doubled coordinate basis) mixed sectional curvature is UNIFORMLY NEGATIVE, "
      "exactly {-1/2 diagonal, -1/8 off-diagonal}",
      honest_neg_uniform, f"honest sectionals observed: {sorted(honest_secs)}  "
      "(clean non-positive curvature of the space of metrics)")

# (3) Krein signs: raw R^Y carries both signs in the honest convention too
raw_signs = set()
for mu in range(DIM):
    for kpair in pairs3:
        K = DIM + pairs3.index(kpair)
        v = RlowH(mu, K, mu, K)
        if abs(v) > mp.mpf(10) ** (-7):
            raw_signs.add(1 if v > 0 else -1)
check("PART 1c: raw R^Y components carry BOTH signs (indefinite/Krein ambient) in the honest convention",
      raw_signs == {1, -1}, f"signs present: {sorted(raw_signs)}")

# (4) THE ADVERSARIAL FINDING: the symbolic OFF-DIAGONAL sectional (-5/8) matches NEITHER consistent
#     convention. Honest = -1/8; non-doubled-consistent = +1/4 (which even flips sign, violating the
#     non-positive curvature of Met). The reported -5/8 is a MIXED-convention artifact (non-doubled metric
#     for lowering combined with closed-form Christoffels of a different pair-normalization).
sym_offdiag_sec = sp.Rational(-5, 16) / (GmatN[0, 0] * GmatN[DIM + pairs3.index((0, 1)), DIM + pairs3.index((0, 1))])
honest_offdiag_sec = sectional(RlowH, GmatH, 0, DIM + pairs3.index((0, 1)))
nond_offdiag_sec = sectional(RlowN, GmatN, 0, DIM + pairs3.index((0, 1)))
finding_ok = (close(sym_offdiag_sec, sp.Rational(-5, 8))
              and not close(honest_offdiag_sec, sp.Rational(-5, 8))
              and not close(nond_offdiag_sec, sp.Rational(-5, 8))
              and nond_offdiag_pos)
check("PART 1d: FINDING -- symbolic OFF-DIAGONAL sectional (-5/8) matches NEITHER the honest (-1/8) NOR the "
      "non-doubled-consistent (+1/4) value: it is a mixed-convention artifact of the symbolic tests",
      finding_ok, f"symbolic-report={sym_offdiag_sec}, honest={mp.nstr(honest_offdiag_sec, 6)}, "
      f"nondoubled-consistent={mp.nstr(nond_offdiag_sec, 6)}")


# ===========================================================================
# PART 2 -- O'Neill A-tensor norm |A|^2 of the 14D model (4D base -> 10D fiber) at g=eta.
#   |A_{mu nu}|^2 = G_{IJ}^fiber A^I_{mu nu} A^J_{mu nu} is an INVARIANT scalar (contract the numerically
#   extracted vertical Christoffel with the actual fiber metric block). Computed in both conventions.
# ===========================================================================
print("\n" + "=" * 78)
print("PART 2: numerical O'Neill |A|^2 of the gimmel metric (14D model) at g=eta, FD from the metric")
print("=" * 78)

DIM4 = 4
eta = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (3, 3): 1,
       (0, 1): 0, (0, 2): 0, (0, 3): 0, (1, 2): 0, (1, 3): 0, (2, 3): 0}


def build_Anorm(doubled):
    pairs4, _, N4, G4 = make_model(DIM4, doubled=doubled)
    pt4 = [mp.mpf(0)] * DIM4 + [mp.mpf(eta[p]) for p in pairs4]
    G4mat = mp.matrix(N4, N4)
    for d in range(N4):
        for e in range(N4):
            G4mat[d, e] = G4(pt4, d, e)
    G4inv = G4mat ** -1
    dG4, _ = build_partials(pt4, DIM4, N4, G4)

    def Gam4(A, B, C):
        return mp.mpf(1) / 2 * sum(G4inv[A, E] * (dG4[B][E][C] + dG4[C][E][B] - dG4[E][B][C]) for E in range(N4))

    def A_norm2(mu, nu):
        s = mp.mpf(0)
        for I in range(DIM4, N4):
            AI = Gam4(I, mu, nu)
            for J in range(DIM4, N4):
                s += G4mat[I, J] * AI * Gam4(J, mu, nu)
        return s
    return A_norm2


AH = build_Anorm(True)      # honest invariant
AN = build_Anorm(False)     # non-doubled
sym_A = {(0, 0): sp.Rational(1, 8), (1, 1): sp.Rational(1, 8),
         (1, 2): sp.Rational(1, 16), (0, 1): sp.Rational(-1, 16)}
print("\n  |A_{mu nu}|^2 -- HONEST(doubled) vs NON-doubled vs symbolic-report:")
for (mu, nu), tgt in sym_A.items():
    tag = "DIAG " if mu == nu else "OFF  "
    print(f"    |A_{mu}{nu}|^2 {tag}: honest={mp.nstr(AH(mu, nu), 8):>10}   nondoubled={mp.nstr(AN(mu, nu), 8):>10}   "
          f"symbolic-report={tgt}")

check("PART 2a: DIAGONAL |A_00|^2 = |A_11|^2 = 1/8 in BOTH conventions (convention-robust; confirms symbolic)",
      close(AH(0, 0), sp.Rational(1, 8)) and close(AN(0, 0), sp.Rational(1, 8))
      and close(AH(1, 1), sp.Rational(1, 8)) and close(AN(1, 1), sp.Rational(1, 8)))
check("PART 2b: HONEST invariant |A|^2 has uniform magnitude 1/8, Krein sign (+ spacelike, - time-mixed): "
      "|A_12|^2 = +1/8, |A_01|^2 = -1/8",
      close(AH(1, 2), sp.Rational(1, 8)) and close(AH(0, 1), sp.Rational(-1, 8)),
      f"honest |A_12|^2 = {mp.nstr(AH(1, 2), 8)}, |A_01|^2 = {mp.nstr(AH(0, 1), 8)}")
check("PART 2c: the |A|^2 SIGN pattern (positive spacelike, negative time-mixed) is convention-robust "
      "(Krein signature real)",
      AH(1, 2) > 0 and AH(0, 1) < 0 and AN(1, 2) > 0 and AN(0, 1) < 0)
check("PART 2d: FINDING -- symbolic OFF-DIAGONAL |A_12|^2 (1/16) matches NEITHER honest (1/8) NOR "
      "non-doubled-consistent (1/2): mixed-convention artifact, mirroring Part 1d",
      not close(AH(1, 2), sp.Rational(1, 16)) and not close(AN(1, 2), sp.Rational(1, 16)),
      f"honest=1/8, nondoubled-consistent={mp.nstr(AN(1, 2), 6)}, symbolic-report=1/16")


print("\n" + "=" * 78)
print("ORACLE VERDICT")
print("=" * 78)
print("  An INDEPENDENT numerical diff-geo pipeline (metric DEFINITION + generic Levi-Civita + mpmath")
print("  finite differences, 40 dps, ZERO reuse of the hand-transcribed closed-form Christoffels) was run in")
print("  BOTH the geometrically HONEST 'doubled' coordinate basis and the symbolic tests' non-doubled basis.")
print()
print("  CONFIRMED (convention-robust -- two independent derivations agree):")
print("   * the DIAGONAL-fiber R^Y = +/-1/4, sectional = -1/2;  the by-hand R^Y = -1/4;")
print("   * the DIAGONAL |A_00|^2 = |A_11|^2 = 1/8;")
print("   * R^Y NONZERO and Krein-signed (both signs) -- so the alpha_W ambient term stays a genuine object.")
print()
print("  CORRECTED (adversarial FINDING -- the oracle's job):")
print("   * The symbolic tests' OFF-DIAGONAL magnitudes -- R^Y sectional -5/8 (willmore_curved_ambient_term)")
print("     and |A_12|^2 = 1/16 (willmore_geometric_ii...) -- match NEITHER consistent convention. They arise")
print("     from mixing the non-doubled metric V_low (for index lowering) with closed-form Christoffels of a")
print("     different pair-normalization. In the HONEST coordinate basis (d/dh_ab = E_ab+E_ba for a<b, the")
print("     true tangent vector) the invariant values are: mixed sectional = -1/8 off-diagonal (so the space")
print("     of metrics has UNIFORMLY non-positive curvature -1/2, -1/8 -- cleaner than the reported -5/8),")
print("     and |A|^2 = 1/8 uniformly (Krein sign). The non-doubled-consistent basis even gives a POSITIVE")
print("     off-diagonal sectional (+1/4), which would violate non-positivity -- so neither the symbolic")
print("     report nor a naive non-doubled reading is the honest geometry.")
print()
print("  IMPACT: no alpha_W / Willmore-arc CONCLUSION breaks -- those rest on R^Y being nonzero and")
print("  Krein-signed (confirmed) and on convention-robust diagonal data. The correction is to the specific")
print("  OFF-DIAGONAL magnitudes, and it strengthens the qualitative claim (uniform non-positive curvature).")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = independent oracle CONFIRMS the convention-robust numbers and CORRECTS the off-diagonal")
print("         magnitudes to their honest (doubled-basis) invariant values.")
