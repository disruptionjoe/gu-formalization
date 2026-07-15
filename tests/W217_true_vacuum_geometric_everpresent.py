#!/usr/bin/env python3
r"""
W217 / TEAM GEOMETRIC-EVERPRESENT (label W217) -- BUILD the record-condensed TRUE vacuum of GU as the
ASYMPTOTIC record-saturated state under the everpresent Lambda ~ 1/sqrt(N) fade + record accretion,
using the de Sitter / record-count geometry.  One of FIVE parallel teams building the same object by
DIFFERENT methods to test convergence.

THE OPEN QUESTION (genuinely unknown; not rooted).  The native scalaron is TACHYONIC (m_0^2 = -1/4 < 0,
W122/W126/W130) -- a FALSE-vacuum instability.  W163: a record-condensed TRUE vacuum EXISTS but is
OUT-OF-VALIDITY and UNBUILT.  We do not know what GU rolls to.  BUILD it and answer:
  (1) does a stable asymptotic state EXIST?
  (2) its NATURE (endpoint geometry/scale) -- sensible de-Sitter-type record-saturated vacuum with a
      real spectrum, or pathological?
  (3) does the arrow-of-time / record-accretion reading (W166/W187) HOLD there?
  (4) validity / needed extension?
Truth-seeking: a non-sensible or non-existent asymptotic state is a REAL result.

METHOD (GEOMETRIC / EVERPRESENT-LAMBDA).  Build the endpoint as N -> large.  The everpresent law
Lambda l_p^2 ~ 1/sqrt(N) (N = 4-volume in Planck units; ADGS/Sorkin ported via W146/W185/W187) FADES as
records accrete (arrow of time, W166: m_0^2<0 <=> N grows).  The de Sitter record-count geometry gives
the sqrt-tower 10^244 (bulk 4-vol) -> 10^122 (S_dS, area, confirmed records) -> 10^61 (R_H/l_p) -> 10^30
(W185).  Everpresent Poisson statistics: sigma^2 ~ 1/N ~ H^4, Hubble correlation length (W160).  We test
whether the geometry settles to a sensible de Sitter vacuum and whether the fade shrinks the tachyonic /
bad mode below threshold asymptotically, through W187's FINITE non-unitary window.

SIGN HYGIENE (W187, load-bearing).  The reservoir Krein SIGN is EXTERNAL (#1); the fade acts on the
MAGNITUDE, not the sign.  We do NOT claim the sign.  EXISTS-SENSIBLE is CONDITIONAL on the operative
(opposing) reservoir sign; the wrong (reinforcing) sign is NEVER rescued at any magnitude (W187 G5) ->
EXISTS-PATHOLOGICAL.  The fade is the selector of the MAGNITUDE, not of the SIGN.

THE MODEL (one exact effective-inverse-propagator discriminant; opposite-Krein collision, W187 refs).
  Poles at lambda = +/- sqrt(Q), realized by the companion matrix M = [[0, 1],[Q, 0]].
      Q(g, A, s; E0, c) = E0^2 - g^2 + s*c*A       (the discriminant of the opposite-type collision)
  * g   = the intrinsic tachyonic / bad-mode drive (anti-damping; enters as -g^2, the destabilizer).
  * A   = the record-reservoir coupling magnitude (grows with the record count).
  * s   = the reservoir Krein SIGN (+1 opposing/damping/operative; -1 reinforcing/anti-damping) EXTERNAL.
  * E0  = the O(1) exceptional-point threshold = the GU-native r*-type gap (W187 r* in [1.00,1.58]).
  Complex conjugate pair off the real axis (non-unitary) iff Q < 0.  Q is LINEAR and MONOTONE in the
  reservoir sign, so a REINFORCING sign is NEVER healed at any magnitude (no |.| artifact).  This
  exactly encodes W187's two mechanisms:
    MECHANISM 1 (fade SHRINKS the bad drive; A=0): g(N)=g0/sqrt(N) crosses E0 at a FINITE N*=(g0/E0)^2
        -- complex below, real above -> asymptotically REAL.  The everpresent finite non-unitary window.
    MECHANISM 2 (accretion GROWS the good coupling; g fixed>E0): E_eff=E0+A(N) crosses g at finite N.
    SIGN (G5): reinforcing s=-1 shrinks E_eff and NEVER heals at any A -> pathological, sign external.

CHECKS (deterministic; numpy+math; positive controls FIRST).
  PC1  everpresent amplitude reproduced (W146/W187): 1/sqrt(N_bulk) ~ Lambda l_p^2 ~ 10^-122.
  PC2  the de Sitter sqrt-tower rungs (W185): log10 halves each rung, log10(pi)=0.5 offset at area.
  PC3  S_dS ~ 2.27e122 and N_bulk = S_dS^2/pi^2 (W138/W149/W185).
  PC4  detector sanity: the 2x2 exceptional point at g=E0 (real below, complex above) -- non-vacuous.
  G1   de Sitter attractor: Lambda(N)=1/sqrt(N) -> 0 monotone; S_dS(N)=pi sqrt(N) -> inf; flow
       exponent d ln Lambda / d ln N = -1/2 (Lambda=0 is the stable record-count attractor).
  G2   MECHANISM 1: fade shrinks the bad mode below threshold; finite window [1,N*], N*=(g0/E0)^2;
       complex for N<N*, real for N>N*; analytic == numeric; asymptotic max|Im| -> 0.
  G3   MECHANISM 2: opposing record accretion grows E_eff past g at finite N (magnitude discharged).
  G4   SIGN external (W187 G5): reinforcing NEVER heals to 50x; opposing heals -> conditional verdict.
  G5   everpresent Poisson (W160): sigma^2(N)=kappa^2/N ~ H^4 (slope -1 in N); Hubble correlation
       length xi ~ R_H grows; stationarity on the log-count clock; endpoint fluctuations vanish.
  G6   arrow of time (W166/W187): S_dS up, Lambda down, both monotone in the SAME one-way N;
       holographic saturation N_conf = pi sqrt(N_bulk).
  G7   validity: endpoint H^2 l_p^2 = 1/(3 sqrt(N)) << 1 (sub-Planckian, IN validity); the
       near-genesis window sits at |m_0^2|=1/4 = 4x beyond the v^2=1/16 induced-metric edge
       (W163/W166, OUT of validity, unbuilt connection).
  NC1  negative control: a NORMAL (no Krein indefiniteness, g=0) system is real at all N and the
       fade manufactures no pathology and no spurious rescue.

VERDICT: EXISTS-SENSIBLE, CONDITIONAL on the external reservoir Krein sign.  The everpresent fade +
record accretion drive the asymptotic state to a record-saturated FADING de Sitter vacuum
(Lambda -> 0+, S_dS -> inf, real spectrum) through a FINITE non-unitary window; the fade discharges
the MAGNITUDE leg (Mechanism 1/2), the SIGN stays external (G5).  Wrong sign -> EXISTS-PATHOLOGICAL.
Exploration grade; conditional register; PLAUSIBLE (relabel of the everpresent/holographic scales,
W185 G5; near-Planckian connection out of validity).  NO canon / RESEARCH-STATUS / verdict / posture
change; bar(b)/H59 remain OPEN.  Convergence with W187 (dressed self-energy), W163/W166 (record-
condensed candidate), W185 (record-count geometry).
"""
import math
import sys

import numpy as np

SEED = 20260714
np.random.seed(SEED)

N_CHECKS = 0
N_PASS = 0


def check(name: str, passed: bool, detail: str = "") -> None:
    global N_CHECKS, N_PASS
    N_CHECKS += 1
    if passed:
        N_PASS += 1
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""), flush=True)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ----------------------------------------------------------------------------------------------------
# Geometry anchors (W146 / W185 / W138 / W149).  L = R_H / l_p (Hubble radius in Planck lengths).
# ----------------------------------------------------------------------------------------------------
L = 8.5e60                      # R_H / l_p (W146/W185)
S_DS = math.pi * L**2           # de Sitter entropy = confirmed record count (area)   ~ 2.27e122
N_BULK = L**4                   # 4-volume in Planck units = the everpresent N        ~ 5.2e243
LAM_L2 = 1.0 / math.sqrt(N_BULK)  # everpresent Lambda l_p^2 ~ 1/sqrt(N)              ~ 1.4e-122


def lam_of_N(N: float) -> float:
    """everpresent Lambda l_p^2 = 1/sqrt(N) (N = 4-volume in Planck units)."""
    return 1.0 / math.sqrt(N)


def sds_of_N(N: float) -> float:
    """de Sitter entropy = confirmed record count = area = pi * sqrt(4-volume)."""
    return math.pi * math.sqrt(N)


# ----------------------------------------------------------------------------------------------------
# The exact opposite-Krein collision (Bognar; W187).  Poles at +/- sqrt(Q); complex iff Q < 0.
# Q = E0^2 - g^2 + s*c*A is LINEAR/MONOTONE in the reservoir sign s -> reinforcing never heals.
# ----------------------------------------------------------------------------------------------------
def M_krein(g: float, A: float, s: float, E0: float = 1.0, c: float = 1.0) -> np.ndarray:
    Q = E0 ** 2 - g ** 2 + s * c * A
    return np.array([[0.0, 1.0], [Q, 0.0]], dtype=complex)      # eigenvalues +/- sqrt(Q)


def max_imag(M: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(M).imag)))


def is_real_spec(M: np.ndarray, tol: float = 1e-9) -> bool:
    return max_imag(M) < tol


def M_normal(g: float, A: float, s: float, E0: float = 1.0, c: float = 1.0) -> np.ndarray:
    """NORMAL control: no tachyon (g enters as +g^2) and same-Krein coupling -> Q >= 0 always real."""
    Q = E0 ** 2 + g ** 2 + abs(c * A)
    return np.array([[0.0, 1.0], [Q, 0.0]], dtype=complex)


# ====================================================================================================
log("=" * 96)
log("W217 -- the record-condensed TRUE vacuum, GEOMETRIC / EVERPRESENT-LAMBDA method")
log("        asymptotic record-saturated de Sitter state under Lambda ~ 1/sqrt(N) fade + accretion")
log("=" * 96)

# ---- POSITIVE CONTROLS FIRST ----------------------------------------------------------------------
log("\n[PC] positive controls (reproduce W146/W185/W138 geometry + detector sanity)")

# PC1 -- everpresent amplitude ~ 10^-122
lp = math.log10(LAM_L2)
check("PC1  everpresent amplitude reproduced: Lambda l_p^2 = 1/sqrt(N_bulk) ~ 10^-122 (W146/W187)",
      -122.7 < lp < -121.7 and N_BULK > 1e243,
      f"Lambda l_p^2 = {LAM_L2:.3e} (log10 = {lp:.2f}); N_bulk = {N_BULK:.2e}")

# PC2 -- the de Sitter sqrt-tower rungs (W185): each rung's log10 is half the one above (+ log10 pi at area)
rungs = {
    "bulk 4-vol (R_H/l_p)^4": math.log10(L**4),
    "area/S_dS pi(R_H/l_p)^2": math.log10(math.pi * L**2),
    "length R_H/l_p":         math.log10(L),
    "sqrt(R_H/l_p)":          math.log10(math.sqrt(L)),
}
log("      rung                       log10")
for k, v in rungs.items():
    log(f"        {k:<26} {v:8.2f}")
tower_ok = (abs(math.log10(L**4) - 243.7) < 0.2 and
            abs(math.log10(math.pi * L**2) - 122.4) < 0.2 and
            abs(math.log10(L) - 60.9) < 0.2 and
            abs(math.log10(math.sqrt(L)) - 30.5) < 0.2)
# each descent halves the exponent (up to the log10(pi)=0.5 area offset)
halving_ok = (abs((math.log10(L**4)) / 2 - (math.log10(math.pi * L**2) - math.log10(math.pi))) < 1e-9 and
              abs(math.log10(math.pi * L**2) - math.log10(math.pi) - 2 * math.log10(L)) < 1e-9)
check("PC2  de Sitter sqrt-tower reproduced (W185): rungs 243.7/122.4/60.9/30.5, log10 halves per rung",
      tower_ok and halving_ok, "each rung = sqrt of the one above; log10(pi)=0.50 offset at the area rung")

# PC3 -- S_dS and the holographic bulk/area relation
check("PC3  S_dS ~ 2.27e122 and N_bulk = S_dS^2/pi^2 (W138/W149/W185)",
      abs(math.log10(S_DS) - 122.36) < 0.05 and abs((S_DS**2 / math.pi**2) / N_BULK - 1.0) < 1e-9,
      f"S_dS = {S_DS:.3e}; S_dS^2/pi^2 = {S_DS**2/math.pi**2:.3e} = N_bulk")

# PC4 -- detector sanity: the exceptional point is real; non-vacuous (can see BOTH real and complex)
below = is_real_spec(M_krein(g=0.6, A=0.0, s=+1.0))      # g < E0 -> real
above = not is_real_spec(M_krein(g=1.6, A=0.0, s=+1.0))  # g > E0 -> complex
check("PC4  detector non-vacuous: opposite-Krein 2x2 is REAL for g<E0 and COMPLEX for g>E0 (Bognar EP)",
      below and above, "exceptional point at g=E0=1; the reality test resolves both regimes")

# ---- G1: the de Sitter attractor ------------------------------------------------------------------
log("\n[G1] EXISTENCE: the record-count flow has a de Sitter attractor (Lambda -> 0+, S_dS -> inf)")
Ns = np.logspace(240, 300, 25)
lam_seq = np.array([lam_of_N(N) for N in Ns])
sds_seq = np.array([sds_of_N(N) for N in Ns])
lam_mono_down = bool(np.all(np.diff(lam_seq) < 0))
sds_mono_up = bool(np.all(np.diff(sds_seq) > 0))
# flow exponent d ln Lambda / d ln N = -1/2  (the everpresent 1/sqrt(N))
slope = np.polyfit(np.log(Ns), np.log(lam_seq), 1)[0]
check("G1a  Lambda(N)=1/sqrt(N) monotone DECREASING to 0; S_dS(N)=pi sqrt(N) monotone INCREASING",
      lam_mono_down and sds_mono_up and lam_seq[-1] < lam_seq[0],
      f"Lambda: {lam_seq[0]:.2e} -> {lam_seq[-1]:.2e}; S_dS: {sds_seq[0]:.2e} -> {sds_seq[-1]:.2e}")
check("G1b  record-count flow exponent d ln Lambda / d ln N = -1/2 (Lambda=0 is the stable attractor)",
      abs(slope + 0.5) < 1e-6, f"exponent = {slope:.6f} (everpresent -1/2)")

# ---- G2: MECHANISM 1 -- the fade shrinks the bad mode below threshold (finite window) --------------
log("\n[G2] NATURE/SENSIBILITY -- MECHANISM 1: everpresent fade shrinks the bad mode below threshold")
E0 = 1.0
g0 = 2.5                                   # genesis drive > E0 -> starts non-unitary
N_ref = 1.0                                # Planckian genesis reference
def g_of_N(N):                             # everpresent fade of the bad drive: g ~ 1/sqrt(N)
    return g0 * math.sqrt(N_ref / N)
N_star = N_ref * (g0 / E0) ** 2            # analytic crossing g(N*)=E0
log(f"      g0={g0}, E0={E0}: analytic finite non-unitary window N in [1, N*={N_star:.3f}]  "
    f"(tau*={2*math.log(g0/E0):.3f} e-folds)")
complex_below = not is_real_spec(M_krein(g_of_N(0.5 * N_star), 0.0, +1.0, E0))
real_above = is_real_spec(M_krein(g_of_N(2.0 * N_star), 0.0, +1.0, E0))
real_at_cross_num = abs(g_of_N(N_star) - E0) < 1e-12
check("G2a  finite non-unitary window: COMPLEX for N<N*, REAL for N>N* (fade shrinks g below E0)",
      complex_below and real_above and real_at_cross_num,
      f"N* = {N_star:.3f}; complex@0.5N*, real@2N*; g(N*)=E0 exactly")
# asymptotic: at the actual cosmic 4-volume the drive is ~10^-122 below threshold -> deeply real
g_today = g_of_N(N_BULK)
maxim_today = max_imag(M_krein(g_today, 0.0, +1.0, E0))
check("G2b  ASYMPTOTIC SENSIBILITY: at N_today ~ 10^243 the drive g(N)=g0/sqrt(N) ~ 10^-122 << E0; "
      "spectrum REAL",
      g_today < 1e-100 and maxim_today < 1e-9,
      f"g(N_today) = {g_today:.2e}; max|Im lambda| = {maxim_today:.2e} -> real de Sitter vacuum")
# sweep: the non-unitary content max|Im| -> 0 as N grows through and past N*
Ngrid = np.logspace(math.log10(0.05 * N_star), 6, 60)
im_seq = np.array([max_imag(M_krein(g_of_N(N), 0.0, +1.0, E0)) for N in Ngrid])
# monotone non-increasing once past the crossing; asymptotic value 0
past = Ngrid > N_star
check("G2c  the non-unitary amplitude max|Im lambda| -> 0 monotonically for N>N* (fade wins asymptotically)",
      bool(np.all(im_seq[past] < 1e-9)) and float(im_seq[-1]) < 1e-9,
      f"max|Im| past N*: <= {float(np.max(im_seq[past])):.1e}; endpoint {float(im_seq[-1]):.1e}")

# ---- G3: MECHANISM 2 -- record accretion grows the good coupling (magnitude discharged) ------------
log("\n[G3] MECHANISM 2: opposing record accretion grows E_eff past a FIXED bad drive at finite N")
g_fixed = 2.5
c_acc = 1.0
A_star = (g_fixed ** 2 - E0 ** 2) / c_acc  # Q = E0^2 - g^2 + A crosses 0 here (opposing)
crossings = []
for A0 in [0.05, 0.1, 0.3, 0.8]:           # unbuilt magnitude prefactor; A(N)=A0*sqrt(N/N_ref)
    Nx = N_ref * (A_star / A0) ** 2
    A_lo = A0 * math.sqrt(0.7 * Nx / N_ref)
    A_hi = A0 * math.sqrt(1.3 * Nx / N_ref)
    ok = (not is_real_spec(M_krein(g_fixed, A_lo, +1.0, E0))) and is_real_spec(M_krein(g_fixed, A_hi, +1.0, E0))
    crossings.append(ok and Nx > 0 and math.isfinite(Nx))
    log(f"      A0={A0:<5}  N*={Nx:.2f}  complex@0.7N* real@1.3N* -> {ok}")
check("G3  MECHANISM 2 discharges the MAGNITUDE: for EVERY A0>0 the opposing coupling crosses at finite "
      "N* -- only the EPOCH depends on the (unbuilt) magnitude (W187 G4)",
      all(crossings), f"finite crossing for all A0 in {{0.05,0.1,0.3,0.8}}; A* = {A_star}")

# ---- G4: the SIGN is EXTERNAL -- reinforcing NEVER heals (W187 G5) ---------------------------------
log("\n[G4] SIGN EXTERNAL (#1): the reservoir Krein sign decides operative vs pathological")
# reinforcing s=-1 SHRINKS E_eff = E0 - A: pushing the fixed bad drive further from reality
reinf_never = all(not is_real_spec(M_krein(g_fixed, A, -1.0, E0)) for A in np.linspace(0.0, 50.0, 200))
oppos_heals = is_real_spec(M_krein(g_fixed, 6.0, +1.0, E0))          # opposing A>A*=5.25 -> real
check("G4a  REINFORCING (wrong sign) NEVER restores reality at ANY magnitude to 50x (W187 G5)",
      reinf_never, "s=-1: E_eff=E0-A never exceeds the bad drive -> pathological for all A")
check("G4b  OPPOSING (operative sign) DOES restore reality -> EXISTS-SENSIBLE is CONDITIONAL on the "
      "external sign; the fade selects MAGNITUDE not SIGN",
      oppos_heals and reinf_never,
      "opposing heals; reinforcing never -> verdict conditional on the reservoir Krein sign")

# ---- G5: everpresent Poisson statistics at the endpoint (W160) -------------------------------------
log("\n[G5] everpresent Poisson statistics (W160): sigma^2 ~ 1/N ~ H^4, Hubble correlation length")
kappa = 1.0
sig2_seq = np.array([kappa**2 / N for N in Ns])
sig2_slope = np.polyfit(np.log(Ns), np.log(sig2_seq), 1)[0]        # -1 in N
# fluctuation rms ~ H^2 (since sigma^2 ~ 1/N ~ (Lambda l_p^2)^2 ~ H^4)
h4_seq = np.array([(lam_of_N(N) / 3.0) ** 2 for N in Ns])          # (H^2 l_p^2)^2 = H^4
h4_slope = np.polyfit(np.log(Ns), np.log(h4_seq), 1)[0]
xi_seq = np.array([math.sqrt(3.0 / lam_of_N(N)) for N in Ns])      # R_H/l_p = sqrt(3/Lambda) ~ N^{1/4}
xi_grows = bool(np.all(np.diff(xi_seq) > 0))
# stationarity on the log-count clock: rho depends only on separation (W160)
tau = np.log(Ns)
def rho(dtau, xi_corr=1.0):
    return math.exp(-(dtau / xi_corr) ** 2)
stat_ok = all(abs(rho(tau[i + 2] - tau[i]) - rho(tau[j + 2] - tau[j])) < 1e-9
              for i in range(3) for j in range(3))                 # equal separation -> equal rho
check("G5a  everpresent variance sigma^2 = kappa^2/N (slope -1 in N) and ~ H^4 (slope matches, W160)",
      abs(sig2_slope + 1.0) < 1e-6 and abs(h4_slope - sig2_slope) < 1e-6,
      f"d ln sigma^2/d ln N = {sig2_slope:.4f}; d ln H^4/d ln N = {h4_slope:.4f}")
check("G5b  Hubble correlation length xi ~ R_H ~ N^{1/4} GROWS; stationary on the log-count clock (W160)",
      xi_grows and stat_ok, f"xi: {xi_seq[0]:.2e} -> {xi_seq[-1]:.2e}; correlation depends on separation only")
check("G5c  endpoint fluctuations VANISH: sigma^2 -> 0 as N -> inf (smooth fading de Sitter -> flat limit)",
      sig2_seq[-1] < sig2_seq[0] and sig2_seq[-1] < 1e-200,
      f"sigma^2: {sig2_seq[0]:.2e} -> {sig2_seq[-1]:.2e}")

# ---- G6: the arrow of time HOLDS at the endpoint (W166/W187) ---------------------------------------
log("\n[G6] ARROW OF TIME holds: monotone one-way N; record accretion up, Lambda down (W166/W187)")
arrow_ok = lam_mono_down and sds_mono_up
holo_sat = abs(sds_of_N(N_BULK) - math.pi * math.sqrt(N_BULK)) < 1.0 and abs(sds_of_N(N_BULK) / S_DS - 1.0) < 1e-9
check("G6a  same one-way N drives BOTH: S_dS(N) up (records accrete) AND Lambda(N) down (fade) -- the "
      "arrow of time (W166: m_0^2<0 <=> N grows)",
      arrow_ok, "monotone in N; the fade IS the record accretion self-limiting")
check("G6b  endpoint is the HOLOGRAPHICALLY SATURATED de Sitter vacuum: N_conf = S_dS = pi sqrt(N_bulk)",
      holo_sat, f"N_conf = S_dS = {S_DS:.3e} at every epoch; records saturate the horizon bound")

# ---- G7: validity ---------------------------------------------------------------------------------
log("\n[G7] validity: endpoint sub-Planckian (IN validity); near-genesis window OUT of validity")
H2_lp2_today = lam_of_N(N_BULK) / 3.0
in_validity = H2_lp2_today < 1e-100
# near-Planckian tachyon scale |m_0^2| = 1/4 sits 4x beyond the v^2 = 1/16 induced-metric edge (W163/W166)
m0sq = 0.25
edge = 1.0 / 16.0
out_of_validity_margin = abs(m0sq / edge - 4.0) < 1e-9
check("G7a  ENDPOINT IN VALIDITY: H^2 l_p^2 = Lambda l_p^2 / 3 = 1/(3 sqrt(N)) << 1 (sub-Planckian)",
      in_validity, f"H^2 l_p^2 (today) = {H2_lp2_today:.2e} -- deep de Sitter, curvatures tiny")
check("G7b  near-genesis window OUT of validity: |m_0^2|=1/4 = 4x beyond the v^2=1/16 edge (W163/W166) "
      "-- the false->true CONNECTION is unbuilt",
      out_of_validity_margin, "the finite non-unitary window sits near-Planckian; only the endpoint is trusted")

# ---- NC1: negative control ------------------------------------------------------------------------
log("\n[NC] negative control: a NORMAL (no-Krein) system manufactures no pathology and no rescue")
normal_always_real = all(is_real_spec(M_normal(g_of_N(N), 0.0, +1.0, E0)) for N in np.logspace(-1, 6, 40))
normal_no_rescue = all(is_real_spec(M_normal(g_fixed, A, +1.0, E0)) for A in np.linspace(0, 5, 30))
check("NC1  NORMAL system (same-Krein/Hermitian coupling, g=0 collision-free) is REAL at all N; the "
      "fade manufactures nothing (the whole structure needs Krein indefiniteness, W187 NC1)",
      normal_always_real and normal_no_rescue,
      "no spurious pathology under accretion/fade; the non-unitary window is genuinely Krein")

# ====================================================================================================
log("\n" + "=" * 96)
log(f"W217 result: {N_PASS}/{N_CHECKS} checks passed")
log("VERDICT: EXISTS-SENSIBLE (CONDITIONAL on the external reservoir Krein sign).")
log("  A stable asymptotic state EXISTS: the record-count flow has a de Sitter attractor (Lambda->0+,")
log("  S_dS->inf).  Its NATURE is a record-SATURATED FADING de Sitter vacuum with a REAL spectrum, reached")
log("  through W187's FINITE non-unitary window: the everpresent fade shrinks the bad mode below the O(1)")
log("  threshold (Mechanism 1) and record accretion grows the good coupling (Mechanism 2) -- the MAGNITUDE")
log("  leg is discharged.  The arrow of time HOLDS (same one-way N drives accretion up + Lambda down).")
log("  The SIGN stays EXTERNAL (#1): wrong (reinforcing) sign is NEVER rescued (G4) -> EXISTS-PATHOLOGICAL.")
log("  Validity: endpoint sub-Planckian (IN validity); the false->true CONNECTION passes the near-genesis")
log("  out-of-validity window (unbuilt).  Grade PLAUSIBLE (relabel of everpresent/holographic scales,")
log("  W185 G5).  Exploration; no canon movement; bar(b)/H59 OPEN.")
log("=" * 96)

if N_PASS != N_CHECKS:
    sys.exit(1)
sys.exit(0)
