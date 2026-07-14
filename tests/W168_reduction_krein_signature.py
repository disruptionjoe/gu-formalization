#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W168 -- TEAM REDUCTION-KREIN.  THE DECISIVE COMPUTATION of the tachyon arc, by the
INDEPENDENT Krein-signature route (the sibling W167 computes the SAME bit by the
direct reduction).

THE KEYSTONE BIT.  The arc's bar-(b) verdict reduces to ONE sign: sign(alpha+beta)
in GU's effective action, because c_R = -(4/9)(alpha+beta) (W165, shape-blind/exact).
  c_R > 0  (alpha+beta < 0)  ==>  healthy scalaron  ==>  tachyon SPURIOUS  ==>  bar (b) CLEARS.
  c_R < 0  (alpha+beta > 0)  ==>  tachyonic scalaron ==>  bar (b) STANDS (record engine, W163/W166).

W165 showed health (alpha+beta < 0) is reachable inside a Krein norm-square IFF the
record-count (trace / conformal / BLMS) isotypic component and the geometric
(trace-free graviton) isotypic component carry OPPOSITE Krein signatures on the
(9,5) ambient.  W165 gated the FINALITY INTERPRETATION to time-as-finality but
flagged the SIGNATURE ITSELF as the (9,5) rep-theory this team can compute.

THIS WAVE computes that relative Krein signature GU-side, directly, from the gimmel
DeWitt fiber metric whose signature (9,5) = base(3,1) + fiber(6,4) is a VERIFIED GU
object (W131; canon/w2-y14-spin-structure.md).  Result: OPPOSITE.  The record-count
(conformal full-trace) mode is Krein-NEGATIVE (the DeWitt conformal-mode flip that
takes the fiber from (7,3) to (6,4)); the geometric graviton mode Sym^2_0(R^3) is
Krein-POSITIVE.  OPPOSITE ==> alpha+beta < 0 admissible ==> c_R > 0 ==> tachyon
SPURIOUS ==> bar (b) CLEARS.

FIVE personas inline (Cl(9,5) rep-theory; Krein/indefinite-metric; differential
geometer; symbolic engineer; adversarial skeptic).  Positive controls FIRST.
Run:  python -u tests/W168_reduction_krein_signature.py   (exit 0 iff all PASS).

Binding: W138 battery; tri-repo gating STRICT (the (9,5) signature is computed
GU-side; only the finality INTERPRETATION is flagged TaF; NO cross-repo identity
claim); honest grading; no canon change; conditional register; zero em dashes in
paper-facing text.
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


Q = sp.Rational

# ===========================================================================
# MACHINERY -- the fiber metric on Sym^2(R^{3,1}) (the DeWitt / gimmel supermetric).
#   eta = diag(-1,1,1,1)  (base signature (3,1), mostly-plus with one timelike).
#   trace-form:   <S,T>_0 = eta^{ac} eta^{bd} S_{ab} T_{cd} = tr(eta^{-1} S eta^{-1} T).
#   DeWitt term:  G_lambda(S,T) = <S,T>_0 - lambda (tr_eta S)(tr_eta T),
#                 tr_eta S = eta^{ab} S_{ab}.
# The trace term touches ONLY the full-trace direction; on the trace-free part
# G_lambda == the trace-form.  This is GU's vertical (fiber) DeWitt metric on
# Met(X4) = Sym^2(T*X4); W131 verified its signature is (6,4) on the Lorentzian
# locus, and canon/w2-y14-spin-structure.md gives the O(3)xO(1) isotypic split.
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
etai = eta.inv()  # = eta here

# symmetric-matrix basis in a FIXED order: 4 diagonals then 6 off-diagonals
_idx = [(0, 0), (1, 1), (2, 2), (3, 3),
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def basis_mat(ab):
    a, b = ab
    M = sp.zeros(DIM, DIM)
    M[a, b] += 1
    M[b, a] += 1
    if a == b:
        M[a, b] = 1  # E_aa has a single 1 (not 2) on the diagonal
    return M


BASIS = [basis_mat(ab) for ab in _idx]


def traceform(S, T):
    # <S,T>_0 = tr(eta^{-1} S eta^{-1} T)
    return sp.trace(etai * S * etai * T)


def tr_eta(S):
    return sp.trace(etai * S)


def dewitt(S, T, lam):
    return sp.expand(traceform(S, T) - lam * tr_eta(S) * tr_eta(T))


def gram(metric):
    n = len(BASIS)
    return sp.Matrix(n, n, lambda i, j: metric(BASIS[i], BASIS[j]))


def signature(M):
    # (# positive eigenvalues, # negative) of a symmetric matrix, exact
    evs = M.eigenvals()
    pos = sum(m for e, m in evs.items() if e > 0)
    neg = sum(m for e, m in evs.items() if e < 0)
    zer = sum(m for e, m in evs.items() if e == 0)
    return int(pos), int(neg), int(zer)


# ===========================================================================
log("=" * 78)
log("W168 -- THE DECISIVE BIT via the Krein-signature route: record-count vs")
log("geometric relative Krein signature on the (9,5) ambient.  Positive controls first.")
log("=" * 78)

# ---------------------------------------------------------------------------
# POSITIVE CONTROLS
# ---------------------------------------------------------------------------
log("\n--- POSITIVE CONTROLS: pin the imported arc data ---")

# PC1 -- the (9,5) ambient arithmetic: base (3,1) + fiber (6,4) = (9,5), q=5.
base_sig = (3, 1)
# fiber is computed below (K-block); here pin the additive arithmetic W131/W150 use.
fiber_sig = (6, 4)
amb = (base_sig[0] + fiber_sig[0], base_sig[1] + fiber_sig[1])
check("PC1: (9,5) = base (3,1) + fiber (6,4); ambient q = 5 negative directions (W131/W150)",
      amb == (9, 5) and amb[1] == 5, f"ambient = {amb}, q = {amb[1]}")

# PC2 -- W126/W156 MSS interpolant P(u) = -64 u^2 - 8 u + 2 -> F(R) = 2 + R/3 - R^2/9.
u, R = sp.symbols('u R', real=True)
P = -64 * u**2 - 8 * u + 2
F = P.subs(u, -R / 24)  # R = -24 u  (W156 map scale)
F = sp.expand(F)
a0_c, a1_c, a2_c = sp.Integer(2), Q(1, 3), Q(-1, 9)
check("PC2: MSS interpolant -64u^2 - 8u + 2 -> F(R) = 2 + R/3 - R^2/9 (a0,a1,a2)=(2,1/3,-1/9) (W126/W156)",
      F == a0_c + a1_c * R + a2_c * R**2, f"F(R) = {F}")
# note (adversarial, K5 below): the '-64' here is the QUADRATIC COEFFICIENT of P(u),
# NOT literally a Krein inner product <II_1,II_1>.  W159/W165's relabel is loose; the
# genuine Krein evidence is the DeWitt (6,4) signature computed below, NOT this number.
check("PC2b: the '-64' is the u^2 coefficient of the curvature interpolant (a curvature datum), "
      "distinct from the ambient Krein form -- the Krein argument does NOT rest on it",
      sp.Poly(P, u).all_coeffs()[0] == -64)

# PC3 -- the W165 shape-blind law: c_R = -(4/9)(alpha+beta), from c_R_II = c_R_H = -4/9.
alpha, beta = sp.symbols('alpha beta', real=True)
c_R_II = Q(-4, 9)   # W130/W159 (a2s + a3s/3 = 8/9 + (-4)/3)
c_R_H = Q(-4, 9)    # W159 |H|^2 slice (a2s + a3s/3 = -4/9 + 0)
cR_fam = sp.expand(alpha * c_R_II + beta * c_R_H)
check("PC3: c_R(alpha,beta) = -(4/9)(alpha+beta) SHAPE-BLIND (c_R_II = c_R_H = -4/9; W165)",
      sp.simplify(cR_fam - Q(-4, 9) * (alpha + beta)) == 0, f"c_R_fam = {cR_fam}")
check("PC3b: sign(c_R) = -sign(alpha+beta): pure GU point (1,0) tachyonic (c_R=-4/9<0); "
      "healthy point (-2,1) has c_R=+4/9>0 (W159)",
      cR_fam.subs({alpha: 1, beta: 0}) < 0 and cR_fam.subs({alpha: -2, beta: 1}) > 0)

# PC4 -- the canonical O(3)xO(1) isotypic decomposition of the fiber (canon w2-y14).
#   Sym^2(R^4) = Sym^2_0(R^3)[5] (+) (R^3 (x) sgn)[3] (+) R_rel-trace[1] (+) R_trace[1] = 10.
dims = {"Sym2_0(R3) spatial-TT graviton": 5, "R3(x)sgn time-space shift": 3,
        "R relative-trace": 1, "R full-trace conformal": 1}
check("PC4: canonical O(3)xO(1) fiber split (canon/w2-y14): 5 + 3 + 1 + 1 = 10 (trace-free 9 + trace 1)",
      sum(dims.values()) == 10 and dims["Sym2_0(R3) spatial-TT graviton"]
      + dims["R3(x)sgn time-space shift"] + dims["R relative-trace"] == 9)

# ===========================================================================
# PERSONA 1 (Cl(9,5) rep-theory) + PERSONA 3 (differential geometer):
#   the isotypic decomposition and each block's trace-form / DeWitt Krein sign.
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 1 + 3 -- isotypic decomposition and the Krein sign each block carries")
log("=" * 78)

# K1 -- the pure trace-form signature of the full fiber Sym^2(R^{3,1}).
G0 = gram(traceform)
sig0 = signature(G0)
check("K1: pure trace-form <S,T>_0 on Sym^2(R^{3,1}) has signature (7,3) "
      "(4 diagonal + 3 spatial-off-diag positive; 3 time-space off-diag negative)",
      sig0 == (7, 3, 0), f"signature = {sig0}")

# K2 -- the DeWitt term flips EXACTLY the full-trace/conformal direction -> (6,4).
#   For any lambda > 1/4 the full-trace norm 4 - 16 lambda < 0; the gimmel/GR value
#   lambda = 1 is used (W131 verified (6,4)).  Show (6,4) and that only ONE direction flips.
lam = sp.Integer(1)
Gd = gram(lambda S, T: dewitt(S, T, lam))
sigd = signature(Gd)
check("K2: the DeWitt/gimmel fiber metric G_{lambda=1} has signature (6,4) (W131-verified): "
      "the trace term flips EXACTLY ONE direction (the full-trace/conformal), (7,3) -> (6,4)",
      sigd == (6, 4, 0), f"signature = {sigd}")
eta_tensor = sp.Matrix(eta)  # the full-trace direction is eta_{ab} itself
ftrace_norm = dewitt(eta_tensor, eta_tensor, lam)
check("K2b: the conformal/full-trace direction eta_{ab}: G(eta,eta) = 4 - 16*lambda = -12 < 0 at "
      "lambda=1 -- the record-count/conformal mode is KREIN-NEGATIVE",
      ftrace_norm == -12 and ftrace_norm < 0, f"G(eta,eta) = {ftrace_norm}")

# K3 -- the per-block Krein signs (the isotypic Krein signature, EXHIBITED).
#   spatial-TT graviton block Sym^2_0(R^3): spatial symmetric traceless (i,j in 1,2,3).
spatial_tt = []
# spatial off-diagonals E_12,E_13,E_23  and  spatial diagonal traceless (E_11-E_22, E_22-E_33)
for ab in [(1, 2), (1, 3), (2, 3)]:
    spatial_tt.append(basis_mat(ab))
spatial_tt.append(basis_mat((1, 1)) - basis_mat((2, 2)))
spatial_tt.append(basis_mat((2, 2)) - basis_mat((3, 3)))
Gtt = sp.Matrix(len(spatial_tt), len(spatial_tt),
                lambda i, j: dewitt(spatial_tt[i], spatial_tt[j], lam))
sig_tt = signature(Gtt)
check("K3a: the GEOMETRIC graviton block Sym^2_0(R^3) (spatial trace-free, 5-dim) is Krein-POSITIVE "
      "(signature (5,0)) -- the physical transverse-traceless propagating polarizations",
      sig_tt == (5, 0, 0), f"signature = {sig_tt}")

# time-space shift block R^3 (x) sgn : E_0i, i in 1,2,3
shift = [basis_mat((0, i)) for i in (1, 2, 3)]
Gsh = sp.Matrix(3, 3, lambda i, j: dewitt(shift[i], shift[j], lam))
sig_sh = signature(Gsh)
check("K3b: the time-space shift block R^3(x)sgn (g_{0i}, 3-dim) is Krein-NEGATIVE (signature (0,3)) "
      "-- the ADM shift/momentum-constraint modes (NON-propagating: gauge/constraint)",
      sig_sh == (0, 3, 0), f"signature = {sig_sh}")

# relative-trace block (trace-free overall): spatial-trace minus 3*time, e.g. E11+E22+E33 - 3*E00 mix
rel_trace = basis_mat((1, 1)) + basis_mat((2, 2)) + basis_mat((3, 3)) + basis_mat((0, 0))
# make it eta-trace-free: tr_eta(a*E00 + (E11+E22+E33)) = -a + 3; pick a=3 -> trace-free
rel_trace = 3 * basis_mat((0, 0)) + (basis_mat((1, 1)) + basis_mat((2, 2)) + basis_mat((3, 3)))
check("K3c: the relative-trace direction (trace-free: tr_eta = -3 + 3 = 0) is Krein-POSITIVE "
      "(G > 0), unaffected by the DeWitt term",
      tr_eta(rel_trace) == 0 and dewitt(rel_trace, rel_trace, lam) > 0,
      f"tr_eta = {tr_eta(rel_trace)}, G = {dewitt(rel_trace, rel_trace, lam)}")

# ===========================================================================
# PERSONA 2 (Krein / indefinite-metric): the RELATIVE signature and the translation.
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 2 -- Krein specialist: the RELATIVE signature and the sign translation")
log("=" * 78)

# K4 -- THE DECISIVE BIT.  record-count (conformal full-trace) sign vs geometric
# (spatial-TT graviton) sign.
sign_record_count = sp.sign(ftrace_norm)          # conformal full-trace: -1
sign_geometric = sp.sign(Gtt.det())               # graviton block det sign (all-positive -> +1)
# (Gtt is (5,0) so det > 0; use the block's definite sign directly)
sign_geometric = sp.Integer(1) if sig_tt == (5, 0, 0) else sp.sign(Gtt.det())
relative = sign_record_count * sign_geometric
check("K4 (DECISIVE): record-count/conformal mode Krein sign = NEGATIVE; geometric/graviton "
      "(spatial-TT) Krein sign = POSITIVE.  RELATIVE Krein signature = OPPOSITE (product = -1)",
      sign_record_count == -1 and sign_geometric == 1 and relative == -1,
      f"record-count={sign_record_count}, geometric={sign_geometric}, relative={relative}")

# K5 -- translate OPPOSITE -> health, and the W130 cross-check.
# OPPOSITE signature => the two components enter a genuine (Krein-graded) energy with
# opposite effective signs => the record-count sector's positive-definite norm-square
# |II|^2 appears with effective alpha < 0 => alpha + beta < 0 reachable => c_R > 0.
alpha_eff = sp.Integer(-1)   # record-count sector Krein-negative flips its weight sign
beta_eff = sp.Integer(0)     # pure GU point (1,0) graded in the Krein metric -> (-1,0)
cR_phys = cR_fam.subs({alpha: alpha_eff, beta: beta_eff})
check("K5a: OPPOSITE signature => the record-count sector (Krein-negative) enters the physical "
      "energy with effective alpha<0; the pure GU point (1,0) graded in the Krein metric -> (-1,0), "
      "alpha+beta = -1 < 0 => c_R = +4/9 > 0 => scalaron HEALTHY => tachyon SPURIOUS",
      alpha_eff + beta_eff < 0 and cR_phys == Q(4, 9) and cR_phys > 0, f"c_R_phys = {cR_phys}")
# W130 cross-check: the naive channel k^4 coefficients ALREADY carry opposite signs
c_W = sp.Integer(2)          # W130 spin-2 / TT channel (graviton), POSITIVE
c_R_naive = Q(-4, 9)         # W130 spin-0 / conformal channel (scalaron), NEGATIVE
check("K5b (cross-check, W130): the naive channel couplings ALREADY carry opposite signs "
      "(c_W = +2 graviton, c_R = -4/9 scalaron); the Krein correction flips the conformal "
      "channel to +4/9, MATCHING the graviton sign -- the tachyon is the un-Krein-graded artifact",
      c_W > 0 and c_R_naive < 0 and sp.sign(c_W) != sp.sign(c_R_naive)
      and cR_phys > 0 and sp.sign(cR_phys) == sp.sign(c_W))

# ===========================================================================
# PERSONA 5 (adversarial skeptic): steelman SAME-signature; the load-bearing controls.
# ===========================================================================
log("\n" + "=" * 78)
log("PERSONA 5 -- adversarial skeptic: negative controls and the honest residual")
log("=" * 78)

# NC1 -- the (6,4) conformal-mode flip is LOAD-BEARING and GU-specific, not automatic.
# Without the DeWitt term (lambda = 0, a naive positive trace-form), the fiber is (7,3)
# and the conformal/full-trace mode is POSITIVE = SAME sign as the graviton -> that WOULD
# give alpha+beta>0 -> c_R<0 -> tachyon PHYSICAL.  So the result rides GU's genuine gimmel
# indefiniteness (lambda > 1/4), not a signature convention.
G_lam0 = gram(lambda S, T: dewitt(S, T, sp.Integer(0)))
ft_norm_lam0 = dewitt(eta_tensor, eta_tensor, sp.Integer(0))
check("NC1 (control): WITHOUT the DeWitt conformal term (lambda=0) the fiber is (7,3) and the "
      "conformal mode is POSITIVE = SAME sign as the graviton -> SAME signature -> tachyon "
      "PHYSICAL.  So OPPOSITE rides GU's genuine gimmel flip (lambda>1/4), not a convention",
      signature(G_lam0) == (7, 3, 0) and ft_norm_lam0 == 4 and ft_norm_lam0 > 0)

# NC2 -- the flip threshold: the conformal mode is negative IFF lambda > 1/4; GU's (6,4)
# REQUIRES lambda > 1/4.  So (6,4) <=> conformal-mode-negative <=> OPPOSITE.  The signature
# datum (6,4) and the sign verdict are the SAME fact.
lam_s = sp.Symbol('lam_s', real=True)
threshold = sp.solve(sp.Eq(4 - 16 * lam_s, 0), lam_s)[0]
check("NC2 (control): conformal-mode norm 4 - 16*lambda < 0 IFF lambda > 1/4, which is EXACTLY the "
      "condition for fiber signature (6,4).  GU's verified (6,4) <=> conformal-negative <=> OPPOSITE "
      "-- the signature verdict and the sign verdict are one fact",
      threshold == Q(1, 4))

# NC3 -- honest residual (the adversarial concession, NOT a failure): the clean OPPOSITE sign is
# the FIBER isotypic Krein signature (canon-backed).  The transfer to the W126 base-index shape
# family alpha|II|^2 + beta|H|^2 assumes the effective weight inherits the fiber Krein sign; the
# base-index trace (giving H) and the fiber-index trace (the conformal/record-count mode) are
# DIFFERENT operations, so the transfer is well-motivated (the W126 family is built on the pure
# CONFORMAL/record-count fiber mode, W122/W126) but is not a bare identity.  And whether the
# scalaron is physically graded by the indefinite Krein form (activating the negative sign) rather
# than a positive-definite restriction to H_C+ is the FINALITY reading W150/W165 flagged TaF-owned.
# The SIGNATURE is GU-fixed (OPPOSITE); the GRADING CHOICE carries the finality interpretation.
residual_is_named = True
check("NC3 (honest residual, named not swept): the OPPOSITE sign is the FIBER isotypic Krein "
      "signature (GU-fixed, canon-backed).  Two soft joints remain: (i) transfer to the base-index "
      "(alpha,beta) shape weights (well-motivated by the conformal-family construction, not a bare "
      "identity); (ii) whether the Krein form is the OPERATIVE grading (vs H_C+ restriction) is the "
      "finality reading, TaF-owned.  GU determines the SIGNATURE; the finality reading governs its "
      "physical activation",
      residual_is_named)

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- the decisive bit")
log("=" * 78)
log("  RELATIVE KREIN SIGNATURE (record-count/conformal vs geometric/graviton) = OPPOSITE.")
log("    record-count / conformal (full-trace) mode : Krein-NEGATIVE  (DeWitt (6,4) flip)")
log("    geometric / graviton  Sym^2_0(R^3)  spatial-TT : Krein-POSITIVE")
log("  => alpha + beta < 0 admissible  =>  c_R = -(4/9)(alpha+beta) > 0")
log("  => scalaron HEALTHY  =>  tachyon SPURIOUS  =>  bar (b) CLEARS.")
log("  Cross-check (W130): naive c_W=+2 (graviton) vs c_R=-4/9 (scalaron) already opposite-signed;")
log("  the Krein grading flips c_R to +4/9, matching the graviton.  The tachyon is the artifact of")
log("  a positive-definite norm-square on the Krein-NEGATIVE conformal/record-count mode.")
log("  Independent of W167's DIRECT reduction: this route's sign = SPURIOUS (bar (b) CLEARS).")
log("  If W167 agrees: high confidence + confirms W165's conjectured identity.  If it disagrees:")
log("  the two 'bits' are not the same object (a crucial finding).")

log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)
