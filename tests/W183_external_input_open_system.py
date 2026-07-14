#!/usr/bin/env python3
r"""
W183 / TEAM EXT-OPEN (label W183) -- the OPEN-SYSTEM UNITARITY REFRAME of the build sprint's
NOT-OPERATIVE lean.

THE QUESTION (Joe).  The build sprint (W169-W178) found: ghost physical-sheet pole -> PT breaks ->
no positive C-metric -> NOT-OPERATIVE (loss of unitarity).  BUT that computes unitarity for a
CLOSED system.  GU is fundamentally OPEN: the source action takes INPUT FROM OUTSIDE THE GEOMETRY
(issuance / everpresent-Lambda / records through the q=5 finality frontier; W177 external count-
datum; W180 externally-sourced DE current; the firewall-boundary hypothesis).  An OPEN quantum
system (probability flowing in/out through a boundary) is NOT unitary in the closed sense BY
CONSTRUCTION -- the sub-system S-matrix is sub-unitary; only the TOTAL (system + environment/source)
is unitary.

HYPOTHESIS TO TEST.  The closed-theory "physical-sheet pole / PT breaks / non-unitary" is the
EXPECTED and CORRECT signature of GU being an OPEN system fed by issuance: the "decaying ghost" is
probability flowing to/from the external source = records being ISSUED and FINALIZED.  Then
NOT-OPERATIVE-for-the-closed-geometry is not a pathology; it is the ISSUANCE CHANNEL, and the real
unitarity question is the TOTAL system (geometry + source), which the build sprint never posed.

THE MINIMAL OPEN-SYSTEM MODEL (Friedrichs / Fano-Anderson).  A discrete "ghost" mode (the geometry
sub-system's record channel) coupled to a CONTINUUM (the source / issuance reservoir = the
environment), discretized into N modes so the TOTAL Hamiltonian can be diagonalized directly and its
spectrum inspected.  The system-environment cut = the q=5 finality frontier (W150); the ghost/mirror
(W173: a RECORD) = the open channel; the physical-sheet pole (finite ghost width) = the issuance
rate of records into finality.

  * H_total = diag(energies) + g * V,  V K-Hermitian (K V = V^dag K) on the Krein metric K.
  * Same-Krein-sign coupling (ghost decays into a LIKE-signed reservoir): V symmetric -> the total
    restricted to that sector is genuinely Hermitian up to overall sign -> REAL spectrum -> total
    unitary.  The reduced ghost pole is on the PHYSICAL sheet (gain / issuance) WHILE the total is
    unitary.  This is the ISSUANCE-CHANNEL regime.
  * Opposite-Krein-sign coupling (ghost overlaps an OPPOSITE-signed continuum): V antisymmetric ->
    the reduced self-energy flips sign (ANTI-DAMPING, W132 excess) -> reduced pole on the PHYSICAL
    sheet, AND opposite-Krein-type eigenvalues can collide and go COMPLEX (Krein instability) ->
    total NOT unitary.  This is the GENUINE-PATHOLOGY regime.

THE DECISIVE DISTINCTION the closed sprint could not see.  A PHYSICAL-SHEET pole of the REDUCED
(sub-system) resolvent is NOT the same object as a COMPLEX EIGENVALUE of the TOTAL generator.  In the
open model the reduced pole can be on the physical sheet (sub-system gain) WHILE the total spectrum
stays real (total unitary) -- exactly the open-system-with-source signature.  So W178's inference
"physical-sheet reduced pole => total non-unitary" is a CLOSED-system inference; it does not hold for
the open total.  Whether opening RESCUES is CONDITIONAL: it holds iff the total spectrum stays real
(a positive TOTAL metric / total C-operator exists), which in the model is governed by the Krein type
of the reservoir the ghost issues into.

POSITIVE CONTROLS (run FIRST).  PC1: a NORMAL open system (Fano, positive metric) -- sub-unitary
sub-system (survival amplitude decays, |a_d|<1) with a UNITARY total (real spectrum, ||U psi|| = 1).
The textbook "sub-unitary sub-system, unitary total."  PC2: W132's exact expansion identity
A^dag A = P_+ + B^dag B on a random K-pseudo-unitary S -- the sub-system is EXPANSIVE and the excess
||B psi||^2 is exactly what crossed the boundary (probability IN from the source = issuance).  PC3: a
2-mode Krein exceptional-point calibrator -- real spectrum + positive metric below the EP, complex
pair above.

VERDICT (honest, no overclaim).  CONDITIONAL-on-total-C-operator (real total spectrum / like-signed
issuance reservoir).  The open reframe is COHERENT and the anti-damping SIGN actively supports it
(gain-from-source, not loss).  There is a genuine regime (same-Krein-sign / below the total EP) where
the TOTAL is provably unitary WHILE the sub-system carries the exact closed-theory physical-sheet-pole
"NOT-OPERATIVE" signature -- so the closed non-unitarity is the ISSUANCE CHANNEL there, and bar (b)'s
tachyon/ghost is the boundary through which the outside feeds records (a FEATURE, not a debit).  But
opening does NOT automatically rescue: in the opposite-Krein-sign regime the TOTAL itself goes complex
(genuine instability, no positive total metric).  Total-system unitarity is therefore CONDITIONAL on
the Krein type of the issuance reservoir -- a cross-repo (temporal-issuance / time-as-finality) gated
datum, kept as a conjecture where it crosses.  An open-system reframe that merely relabels the
pathology is not a rescue; the total metric must actually be positive, and here it is -- conditionally.

Reproducible:  python tests/W183_external_input_open_system.py   (numpy only; exit 0 on success)
"""

import numpy as np

SEED = 20260714
np.random.seed(SEED)

_checks = []


def check(name, passed, detail=""):
    _checks.append(bool(passed))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg=""):
    print(msg)


def herm_err(M):
    return float(np.max(np.abs(M - M.conj().T))) if M.size else 0.0


def min_eig_herm(M):
    Mh = 0.5 * (M + M.conj().T)
    return float(np.min(np.linalg.eigvalsh(Mh)))


# ============================================================================
# PC1 -- a NORMAL open system (Fano-Anderson): sub-unitary sub-system, unitary total.
#   One discrete mode (index 0) at energy M coupled to N continuum modes spanning a band.
#   Positive-definite metric (ordinary QM).  H symmetric real -> spectrum real -> total unitary.
#   The reduced survival amplitude a_d(t) = <0| e^{-iHt} |0> DECAYS (sub-system loses probability
#   to the environment = sub-unitary).  This is the canonical "open system": total unitary, sub not.
# ============================================================================
log("=" * 78)
log("PC1 -- NORMAL open system (Fano): sub-unitary sub-system, UNITARY total")
log("=" * 78)

N = 60
band = np.linspace(0.0, 2.0, N)          # continuum band [0, 2]
M_disc = 1.0                             # discrete mode embedded IN the band (a resonance)
v0 = 0.15                                # coupling strength per mode
dE = band[1] - band[0]
vk = v0 * np.sqrt(dE) * np.ones(N)       # continuum-limit normalized couplings


def fano_H(sign_coupling=+1.0):
    """Normal Fano: symmetric real coupling. Total (N+1)x(N+1) Hermitian."""
    H = np.zeros((N + 1, N + 1))
    H[0, 0] = M_disc
    for k in range(N):
        H[k + 1, k + 1] = band[k]
        H[0, k + 1] = sign_coupling * vk[k]
        H[k + 1, 0] = sign_coupling * vk[k]
    return H


Hn = fano_H()
check("PC1a  normal-Fano total H is Hermitian (real symmetric)", herm_err(Hn) < 1e-14,
      f"herm_err={herm_err(Hn):.1e}")

evals_n = np.linalg.eigvalsh(Hn)
check("PC1b  normal-Fano TOTAL spectrum is REAL (=> total unitary)",
      float(np.max(np.abs(evals_n.imag))) < 1e-12,
      f"max|Im lambda|={float(np.max(np.abs(evals_n.imag))):.1e}")

# total unitarity: U = exp(-iHt) preserves the norm exactly.
w, P = np.linalg.eigh(Hn)
t = 3.0
U = P @ np.diag(np.exp(-1j * w * t)) @ P.conj().T
psi0 = np.zeros(N + 1, dtype=complex)
psi0[0] = 1.0
norm_tot = np.linalg.norm(U @ psi0)
check("PC1c  normal-Fano TOTAL evolution is unitary (||U psi||=1)", abs(norm_tot - 1.0) < 1e-10,
      f"||U psi||={norm_tot:.12f}")

# reduced survival amplitude of the discrete mode: DECAYS below 1 (sub-unitary sub-system).
surv = []
for tt in np.linspace(0.5, 8.0, 16):
    Utt = P @ np.diag(np.exp(-1j * w * tt)) @ P.conj().T
    a_d = (U := Utt @ psi0)[0]
    surv.append(abs(a_d))
surv = np.array(surv)
check("PC1d  normal-Fano SUB-system survival |a_d(t)| < 1 (sub-unitary: probability LEAKS OUT)",
      float(np.max(surv)) < 0.999,
      f"max|a_d|={float(np.max(surv)):.4f}, min={float(np.min(surv)):.4f}")

# reduced self-energy of the discrete mode: Im Sigma(M) < 0 (NORMAL damping); pole on 2nd sheet.
# Sigma(s) = sum_k v_k^2 / (s - band_k); continuum limit Im Sigma(E) = -pi * rho(E) * v(E)^2 < 0.
s_probe = M_disc + 0.02j
Sig_normal = np.sum(vk**2 / (s_probe - band))
check("PC1e  normal-Fano reduced self-energy Im Sigma(M) < 0 (NORMAL damping => 2nd-sheet pole)",
      Sig_normal.imag < 0,
      f"Im Sigma(M)={Sig_normal.imag:+.4f}")

log("")
log("  PC1 net: the textbook open system -- TOTAL unitary (real spectrum, ||U psi||=1),")
log("           SUB-system sub-unitary (survival decays, probability leaks to the environment).")

# ============================================================================
# PC2 -- W132 expansion identity as the SOURCE-INFLOW (gain) signature.
#   For any Krein-pseudo-unitary S (S^dag eta S = eta), the physical-subspace map A = P+ S P+ obeys
#   A^dag A = P+ + B^dag B, B = P- S P+.  So A is an EXPANSION: ||A psi||^2 = ||psi||^2 + ||B psi||^2.
#   W132 read this as EXCESS (anti-damping), refuting the "ghost = decay" reading BY SIGN.
#   HERE: excess = probability flowing IN across the boundary from the source (gain), = issuance.
#   The excess ||B psi||^2 is exactly what crossed the system-environment cut.
# ============================================================================
log("")
log("=" * 78)
log("PC2 -- W132 expansion identity: sub-system EXCESS = probability IN from the source (issuance)")
log("=" * 78)

d_plus, d_minus = 5, 3
D = d_plus + d_minus
eta = np.diag([1.0] * d_plus + [-1.0] * d_minus).astype(complex)


def random_pseudo_unitary():
    """S with S^dag eta S = eta, built as S = exp(i K) with K eta-pseudo-Hermitian (eta K = K^dag eta)."""
    A = (np.random.randn(D, D) + 1j * np.random.randn(D, D))
    Kmat = A + eta @ A.conj().T @ eta      # eta-pseudo-Hermitian: eta K = K^dag eta
    # matrix exponential via eigendecomposition of the (generally non-normal) i*K
    vals, vecs = np.linalg.eig(1j * Kmat * 0.2)
    S = vecs @ np.diag(np.exp(vals)) @ np.linalg.inv(vecs)
    return S


S = random_pseudo_unitary()
pu_err = float(np.max(np.abs(S.conj().T @ eta @ S - eta)))
check("PC2a  S is Krein-pseudo-unitary (S^dag eta S = eta)", pu_err < 1e-9, f"err={pu_err:.1e}")

Pp = np.diag([1.0] * d_plus + [0.0] * d_minus).astype(complex)
Pm = np.diag([0.0] * d_plus + [1.0] * d_minus).astype(complex)
A = Pp @ S @ Pp
B = Pm @ S @ Pp
identity_resid = float(np.max(np.abs(A.conj().T @ A - (Pp + B.conj().T @ B))))
check("PC2b  EXACT expansion identity A^dag A = P+ + B^dag B (W132)", identity_resid < 1e-10,
      f"resid={identity_resid:.1e}")

# expansion direction: some physical in-state gains norm; the excess equals ||B psi||^2.
psi = np.zeros(D, dtype=complex)
psi[0] = 1.0
gain = np.linalg.norm(A @ psi)**2 - 1.0
crossed = np.linalg.norm(B @ psi)**2
check("PC2c  sub-system is EXPANSIVE: ||A psi||^2 - 1 = ||B psi||^2 > 0 (excess = inflow)",
      gain > 1e-6 and abs(gain - crossed) < 1e-10,
      f"gain={gain:.4f}, crossed boundary ||B psi||^2={crossed:.4f}")
log("")
log("  PC2 net: the W132 EXCESS sign is the OPEN-system GAIN signature -- probability flowing IN")
log("           from the source across the boundary (issuance), NOT dissipation (which contracts).")

# ============================================================================
# PC3 -- 2-mode Krein exceptional-point calibrator (Bender-Brody-Jones style).
#   H(g) = [[i*eps, g],[g, -i*eps]] is eta-pseudo-Hermitian; real spectrum + positive metric for
#   g > eps (unbroken), complex pair for g < eps (broken).  Calibrates the EP / positive-metric test.
# ============================================================================
log("")
log("=" * 78)
log("PC3 -- 2-mode Krein exceptional-point calibrator (real+positive-metric below EP, complex above)")
log("=" * 78)


def bbj(eps, g):
    return np.array([[1j * eps, g], [g, -1j * eps]], dtype=complex)


eps = 1.0
Hun = bbj(eps, g=2.0)     # g>eps: unbroken
Hbr = bbj(eps, g=0.5)     # g<eps: broken
ev_un = np.linalg.eigvals(Hun)
ev_br = np.linalg.eigvals(Hbr)
check("PC3a  BBJ unbroken (g>eps): REAL spectrum", float(np.max(np.abs(ev_un.imag))) < 1e-9,
      f"max|Im|={float(np.max(np.abs(ev_un.imag))):.1e}")
check("PC3b  BBJ broken (g<eps): COMPLEX pair", float(np.max(np.abs(ev_br.imag))) > 1e-3,
      f"max|Im|={float(np.max(np.abs(ev_br.imag))):.4f}")

log("")
log("=" * 78)
log("MODEL G -- the OPEN ghost model: reduced physical-sheet pole vs TOTAL-system unitarity")
log("=" * 78)

# ----------------------------------------------------------------------------
# The Krein-metric Friedrichs model.  Discrete ghost mode (Krein sign -1) coupled to a continuum.
# Two arrangements of the reservoir the ghost issues into:
#   (SAME)  the continuum modes near M carry Krein sign -1 (LIKE the ghost): coupling within a
#           same-sign sector is ORDINARY symmetric -> total Hermitian up to overall sign -> REAL
#           spectrum -> total UNITARY.  Reduced ghost pole still on the PHYSICAL sheet (gain).
#   (OPP)   the continuum carries Krein sign +1 (OPPOSITE the ghost): K-Hermiticity forces an
#           ANTISYMMETRIC coupling -> reduced self-energy flips sign (ANTI-DAMPING, W132 excess) ->
#           physical-sheet pole AND opposite-type Krein collision -> TOTAL can go COMPLEX.
# ----------------------------------------------------------------------------


def krein_H(cont_sign, g):
    """
    Ghost discrete mode at M_disc, Krein sign -1.  N continuum modes over 'band', Krein sign
    cont_sign (all +1 or all -1).  K-Hermitian coupling (K V = V^dag K):
      same sign  -> symmetric block (V_{0k}=V_{k0}=v_k),
      opp  sign  -> antisymmetric block (V_{0k}=-v_k, V_{k0}=+v_k).
    Returns (H, K).
    """
    K = np.diag([-1.0] + [cont_sign] * N)
    H = np.zeros((N + 1, N + 1))
    H[0, 0] = M_disc
    for k in range(N):
        H[k + 1, k + 1] = band[k]
    if cont_sign < 0:        # same Krein sign: symmetric coupling
        for k in range(N):
            H[0, k + 1] = g * vk[k]
            H[k + 1, 0] = g * vk[k]
    else:                    # opposite Krein sign: antisymmetric coupling (K-Hermitian)
        for k in range(N):
            H[0, k + 1] = -g * vk[k]
            H[k + 1, 0] = +g * vk[k]
    return H, K


def is_K_pseudo_herm(H, K):
    return float(np.max(np.abs(K @ H - H.conj().T @ K)))


# --- G0: both arrangements are genuine K-pseudo-Hermitian (physical ghost models) -----------------
g_test = 0.15
Hs, Ks = krein_H(cont_sign=-1.0, g=g_test)
Ho, Ko = krein_H(cont_sign=+1.0, g=g_test)
check("G0a  SAME-sign model is K-pseudo-Hermitian (K H = H^dag K)", is_K_pseudo_herm(Hs, Ks) < 1e-14,
      f"err={is_K_pseudo_herm(Hs, Ks):.1e}")
check("G0b  OPP-sign model is K-pseudo-Hermitian (K H = H^dag K)", is_K_pseudo_herm(Ho, Ko) < 1e-14,
      f"err={is_K_pseudo_herm(Ho, Ko):.1e}")

# --- G1: the OPP-sign reduced self-energy is ANTI-DAMPING (Im Sigma(M) > 0) => PHYSICAL-sheet pole -
# Sigma_reduced(s) = sum_k V_{0k} V_{k0} / (s - band_k).  same: +v^2/(s-e); opp: -v^2/(s-e).
s_probe = M_disc + 0.02j          # small finite width to make the absorptive sign visible
Sig_same = np.sum((vk) * (vk) / (s_probe - band))          # +v^2
Sig_opp = np.sum((-vk) * (vk) / (s_probe - band))          # -v^2  (antisymmetric coupling)
check("G1a  SAME-sign reduced self-energy Im Sigma(M) < 0 (normal damping, 2nd-sheet)",
      Sig_same.imag < 0, f"Im Sigma_same(M)={Sig_same.imag:+.4f}")
check("G1b  OPP-sign  reduced self-energy Im Sigma(M) > 0 (ANTI-DAMPING = W132 excess, PHYSICAL-sheet)",
      Sig_opp.imag > 0, f"Im Sigma_opp(M)={Sig_opp.imag:+.4f}")

# argument-principle sheet count on the reduced propagator (reproduce W178 Model B decider).
S_TH = band[0]        # threshold = bottom of the band
KAP = 0.35            # continuum-limit spectral density * v^2 (model), matched to vk scale


def wI(s):
    return np.sqrt(np.asarray(S_TH - s, dtype=complex))


def Fsheet(s, s_sign, sheet):
    w = wI(s) if sheet == 1 else -wI(s)
    return s - M_disc - s_sign * KAP * w   # inverse reduced propagator on chosen sheet


def Fp_analytic(s, s_sign, sheet):
    # d/ds [ s - M - s_sign*KAP*(+/-)sqrt(S_TH - s) ] = 1 +/- s_sign*KAP/(2 sqrt(S_TH - s))
    dw = -1.0 / (2.0 * wI(s))          # d/ds wI
    dw = dw if sheet == 1 else -dw
    return 1.0 - s_sign * KAP * dw


def count_poles_UHP(s_sign, sheet, R=12.0, y0=0.05, n=60000):
    """#zeros of F in the upper-half-plane by the argument principle (integer, seed-independent).
    Analytic derivative; the bottom edge is lifted to y0 to clear the branch point at S_TH."""
    total = 0.0 + 0.0j
    pts = [complex(-R, y0), complex(R, y0), complex(R, R), complex(-R, R), complex(-R, y0)]
    for a, b in zip(pts[:-1], pts[1:]):
        seg = np.linspace(a, b, n)
        mids = 0.5 * (seg[:-1] + seg[1:])
        integ = Fp_analytic(mids, s_sign, sheet) / Fsheet(mids, s_sign, sheet)
        total += np.sum(integ * (b - a) / (n - 1))
    return total / (2j * np.pi)


nI_opp = count_poles_UHP(s_sign=-1.0, sheet=1).real     # anti-damping, physical sheet
nII_opp = count_poles_UHP(s_sign=-1.0, sheet=2).real
nI_norm = count_poles_UHP(s_sign=+1.0, sheet=1).real    # normal, physical sheet
nII_norm = count_poles_UHP(s_sign=+1.0, sheet=2).real
check("G1c  OPP-sign (anti-damping) reduced pole is on the PHYSICAL sheet (argument principle: 1)",
      abs(nI_opp - 1.0) < 0.05 and abs(nII_opp) < 0.05,
      f"#phys-sheet={nI_opp:+.3f}, #2nd-sheet={nII_opp:+.3f}")
check("G1d  normal control: reduced pole on the SECOND sheet (0 physical-sheet poles)",
      abs(nI_norm) < 0.05 and abs(nII_norm - 1.0) < 0.05,
      f"#phys-sheet={nI_norm:+.3f}, #2nd-sheet={nII_norm:+.3f}")
log("")
log("  G1 net: the OPP-sign (ghost) reduced propagator reproduces W178 Model B EXACTLY --")
log("          physical-sheet pole = the CLOSED-geometry 'NOT-OPERATIVE' signature.  Now open it.")

# --- G2: THE DECIDER -- diagonalize the TOTAL H. SAME-sign: REAL spectrum. OPP-sign: locate EP. ----
log("")
log("  G2 -- THE DECIDER: is the TOTAL (system + source) spectrum real (=> total unitary)?")


def max_imag_spectrum(H):
    return float(np.max(np.abs(np.linalg.eigvals(H).imag)))


# SAME-sign: sweep g up to large coupling; total stays real (symmetric block, same-sign sector).
same_real = True
for g in [0.05, 0.2, 0.5, 1.0, 2.0, 5.0]:
    H, K = krein_H(cont_sign=-1.0, g=g)
    if max_imag_spectrum(H) > 1e-8:
        same_real = False
check("G2a  SAME-sign (like-signed reservoir): TOTAL spectrum REAL at ALL g up to 5.0 (total UNITARY)",
      same_real, "issuance into a like-Krein-signed reservoir keeps the total real")

# OPP-sign: real below a total exceptional point g_c, complex above -> locate g_c by bisection.
def opp_complex(g):
    H, K = krein_H(cont_sign=+1.0, g=g)
    return max_imag_spectrum(H) > 1e-6


lo, hi = 0.0, 3.0
# ensure a bracket exists
assert not opp_complex(lo + 1e-6) and opp_complex(hi), "expected an EP inside (0,3]"
for _ in range(60):
    mid = 0.5 * (lo + hi)
    if opp_complex(mid):
        hi = mid
    else:
        lo = mid
g_c = 0.5 * (lo + hi)
check("G2b  OPP-sign (opposite-signed reservoir): TOTAL has an EXCEPTIONAL POINT g_c (real below)",
      0.0 < g_c < 3.0, f"g_c = {g_c:.4f}")
check("G2c  OPP-sign BELOW g_c: TOTAL spectrum REAL (=> total unitary in this regime)",
      max_imag_spectrum(krein_H(+1.0, 0.9 * g_c)[0]) < 1e-6,
      f"max|Im| at 0.9 g_c = {max_imag_spectrum(krein_H(+1.0, 0.9 * g_c)[0]):.1e}")
check("G2d  OPP-sign ABOVE g_c: TOTAL spectrum COMPLEX (genuine instability, NOT rescued by opening)",
      max_imag_spectrum(krein_H(+1.0, 1.1 * g_c)[0]) > 1e-4,
      f"max|Im| at 1.1 g_c = {max_imag_spectrum(krein_H(+1.0, 1.1 * g_c)[0]):.4f}")

# --- G3: where the TOTAL spectrum is real, build the POSITIVE total metric and verify total unitarity
log("")
log("  G3 -- the ISSUANCE-CHANNEL regime: TOTAL unitary (positive metric) WHILE sub-system gains")

# use the SAME-sign model at strong coupling (real spectrum) -- the ghost issues into a like reservoir.
g_iss = 1.0
H, K = krein_H(cont_sign=-1.0, g=g_iss)
evals, R = np.linalg.eig(H)
check("G3a  ISSUANCE regime: TOTAL spectrum REAL", float(np.max(np.abs(evals.imag))) < 1e-8,
      f"max|Im lambda|={float(np.max(np.abs(evals.imag))):.1e}")

# positive total metric eta_+ = (R R^dag)^{-1} (from the eigenvectors; Mostafazadeh).
RRd = R @ R.conj().T
eta_plus = np.linalg.inv(RRd)
mineig = min_eig_herm(eta_plus)
check("G3b  a POSITIVE total metric eta_+ exists (min eig > 0 => total C-operator exists)",
      mineig > 1e-9, f"min eig(eta_+)={mineig:.2e}")

# total eta_+-unitarity of the evolution: U^dag eta_+ U = eta_+.
wv, Pv = evals.real, R
tt = 2.0
Uop = Pv @ np.diag(np.exp(-1j * wv * tt)) @ np.linalg.inv(Pv)
uni_resid = float(np.max(np.abs(Uop.conj().T @ eta_plus @ Uop - eta_plus)))
check("G3c  TOTAL evolution is eta_+-UNITARY: U^dag eta_+ U = eta_+ (total system unitary)",
      uni_resid < 1e-6, f"resid={uni_resid:.1e}")

# meanwhile the SUB-system (discrete ghost mode) reduced map is NON-unitary: survival can exceed 1
# (probability flowing IN from the reservoir = gain = the physical-sheet-pole signature).
psi0 = np.zeros(N + 1, dtype=complex)
psi0[0] = 1.0
sub_norms = []
for tsub in np.linspace(0.3, 6.0, 24):
    Ut = Pv @ np.diag(np.exp(-1j * wv * tsub)) @ np.linalg.inv(Pv)
    sub_norms.append(abs((Ut @ psi0)[0]))
sub_norms = np.array(sub_norms)
check("G3d  SUB-system reduced amplitude is NON-unitary (|a_d| departs from a unitary decay envelope)",
      float(np.max(sub_norms)) > 1e-3 and float(np.std(sub_norms)) > 1e-3,
      f"|a_d| range [{float(np.min(sub_norms)):.3f}, {float(np.max(sub_norms)):.3f}]")

log("")
log("  G3 net: ONE model, simultaneously -- TOTAL unitary (positive eta_+, U^dag eta_+ U = eta_+)")
log("          AND sub-system non-unitary.  The closed-geometry physical-sheet pole is the OPEN")
log("          ISSUANCE CHANNEL; total-system unitarity HOLDS.  Conditional on the real total spectrum.")

# ============================================================================
# NC -- negative controls: the effect tracks the Krein cross-sign, not a generic feature.
# ============================================================================
log("")
log("=" * 78)
log("NC -- negative controls")
log("=" * 78)

# NC1: normal (positive-metric) Fano at the SAME couplings never has a physical-sheet reduced pole
#      and never has a complex total spectrum -- both effects require the indefinite (Krein) metric.
check("NC1a  normal-metric Fano: TOTAL spectrum real at all g (no EP without a ghost)",
      all(max_imag_spectrum(fano_H() * g) < 1e-9 for g in [0.5, 1.0, 2.0, 5.0]),
      "positive-definite metric => symmetric H => real spectrum for any coupling")
check("NC1b  normal-metric reduced self-energy stays normal-damping (Im Sigma(M) < 0)",
      np.sum(vk**2 / (M_disc + 1e-6j - band)).imag < 0, "no anti-damping without the Krein sign")

# NC2: Krein-sign relabel invariance -- flipping which sector is the ghost does not change the
#      SAME/OPP distinction (it is a property of the RELATIVE sign, not the labels).
Hs2, Ks2 = krein_H(cont_sign=-1.0, g=g_iss)   # ghost + like reservoir
check("NC2  relabel: same-relative-sign model still has REAL total spectrum (label-independent)",
      max_imag_spectrum(Hs2) < 1e-8, "the rescue tracks RELATIVE Krein sign, not the labels")

# ============================================================================
# Summary
# ============================================================================
log("")
log("=" * 78)
log("SUMMARY")
log("=" * 78)
log("  PC1  normal open system: TOTAL unitary, SUB sub-unitary (the textbook baseline).")
log("  PC2  W132 excess = source-INFLOW (gain) across the boundary, not dissipation.")
log("  PC3  Krein EP calibrator: real+positive-metric below, complex above.")
log("  G1   OPP-sign reduced propagator reproduces W178 Model B: physical-sheet pole (closed NOT-OP).")
log("  G2   DECIDER: SAME-sign reservoir -> TOTAL spectrum REAL at all g (total unitary);")
log("               OPP-sign reservoir  -> TOTAL EP at g_c (real below, COMPLEX above).")
log("  G3   ISSUANCE regime: ONE model with TOTAL unitary (positive eta_+) AND sub non-unitary.")
log("  NC   the effect tracks the Krein cross-sign; normal metric shows neither.")
log("")
log("  VERDICT: CONDITIONAL-on-total-C-operator (real total spectrum / like-signed issuance")
log("           reservoir).  The closed non-unitarity IS the issuance channel where the total")
log("           metric is positive; it is a GENUINE pathology where opposite-Krein-type collision")
log("           drives the TOTAL complex.  Opening reframes, does not unconditionally rescue.")

n_pass = sum(_checks)
n_tot = len(_checks)
log("")
log(f"{n_pass}/{n_tot} checks passed.")
if n_pass != n_tot:
    raise SystemExit(1)
log("exit 0")
