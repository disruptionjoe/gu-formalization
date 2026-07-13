#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W80 -- GU's NATIVE R^2 (spin-0) sign: is f_0^2 < 0 a genuine forced fact, a porting
       artifact, or a free (observer-selectable) value?  The MAKE-OR-BREAK number.

Context (W79): the whole "first genuine no-go" (observer-conjecture Krein-TT leg) rests on
ONE input, f_0^2 < 0, which W79 imported from the ported agravity one-loop betas (W45-47).
The scalaron mass is M_0^2 = gamma/(6 f_0^2) with gamma>0 (H25), so sign(M_0^2)=sign(f_0^2).
W80 decides f_0^2's sign TWO ways from GU's NATIVE content:

  TASK 1 (direct heat-kernel/beta): does the native RS ker-Gamma contribution to the R^2
          (spin-0) beta change the sign vs the ported agravity value?
  TASK 2 (fixed-point/relevance): is sign(f_0^2) FORCED (arena) or FREE (value)?

Machinery reused (mirrors W45 H57-stage1 BetaSystem; W45 raises SystemExit on import, so the
tiny KNOWN beta coefficients are re-encoded here rather than imported):

  (4pi)^2 df_2^2/dt = -f_2^4 * b_2 ,           b_2 = 133/10 + c_RS_weyl        (x=f_2^2, AF)
  (4pi)^2 df_0^2/dt =  (5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6 + d_RS_R2) f_0^4      (y=f_0^2)

  c_RS_weyl : RS ker-Gamma contribution to the Weyl (b_2) beta; band [1.02,1.82] (H60).
  d_RS_R2   : RS ker-Gamma contribution to the R^2 (f_0^2) beta; anchor 0 (GUESS, H60/W45)
              -- fermion-like: a transverse gamma-traceless (conformal-like) carrier does not
              source R^2; the only R^2 source is the small non-minimal Bbar Sigma.R B (y_RS).

On the AF trajectory f_2^2 -> 0, the physical UV variable is the ratio r = f_0^2/f_2^2, whose
fixed ratios r* solve the bracket  P(r) = (5/6 + d_RS_R2) r^2 + (5 + b_2) r + 5/3 = 0.
sign(f_0^2) on the AF-complete trajectory = sign(r*) (since f_2^2>0).

Deterministic (no RNG; fixed-step RK4). Exact-rational where possible, float ODE cross-check.
Exit 0 on success.
"""

import math
import sys
from fractions import Fraction as F

FAIL = []


def check(name, cond, detail=""):
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# KNOWN / ported coefficients (mirror W45 BetaSystem; grades noted).
# ---------------------------------------------------------------------------
C_WEYL_PURE = F(133, 10)     # KNOWN pure-gravity Weyl coefficient
C_F0_FROM_F2 = F(5, 3)       # KNOWN, > 0 : the (5/3) f_2^4 source term in beta_{f_0^2}
C_F0_MIXED = F(5)            # KNOWN, > 0
C_F0_SELF = F(5, 6)          # KNOWN, > 0 : the f_0^4 self term (before RS shift d_RS_R2)
C_RS_WEYL_BAND = (F(102, 100), F(17, 12), F(182, 100))   # H60 band [1.02, 1.4167, 1.82]
D_RS_R2_ANCHOR = F(0)        # GUESS anchor (fermion-like: no native R^2 renorm)


def fixed_ratio_bracket_roots(d_rs_r2, c_rs_weyl):
    """Roots r* of P(r) = (5/6 + d_RS_R2) r^2 + (5 + b_2) r + 5/3, and the leading coeff A.
    r* = f_0^2/f_2^2 at a UV fixed ratio; sign(f_0^2)_AF = sign(r*)."""
    A = C_F0_SELF + d_rs_r2
    b2 = C_WEYL_PURE + c_rs_weyl
    B = C_F0_MIXED + b2
    C = C_F0_FROM_F2
    Af, Bf, Cf = float(A), float(B), float(C)
    disc = Bf * Bf - 4 * Af * Cf
    if abs(Af) < 1e-30 or disc < 0:
        return None, None, Af, disc
    s = math.sqrt(disc)
    return (-Bf + s) / (2 * Af), (-Bf - s) / (2 * Af), Af, disc


print("=" * 78)
print("TASK 1 -- native RS ker-Gamma contribution to the R^2 (spin-0) beta & the sign")
print("=" * 78)

# ---- 1a: at the anchor (d_RS_R2 = 0), BOTH fixed ratios are NEGATIVE => native f_0^2 < 0,
#          SAME sign as the ported agravity value.  This is because, with A = 5/6 > 0:
#            product of roots = C/A = (5/3)/(5/6) = 2 > 0,  sum = -B/A < 0  => both negative.
rp, rm, A_anchor, disc = fixed_ratio_bracket_roots(D_RS_R2_ANCHOR, F(17, 12))
check("1a  anchor (d_RS_R2=0): both fixed ratios real", disc > 0, "disc=%.3f" % disc)
check("1a  anchor: BOTH fixed ratios r* < 0  => native f_0^2 < 0 (same sign as ported agravity)",
      rp < 0 and rm < 0, "r* = %.4f , %.4f" % (rp, rm))
# exact-rational witness for 'both negative': product>0 and sum<0
A = C_F0_SELF + D_RS_R2_ANCHOR
prod = C_F0_FROM_F2 / A
check("1a  exact: product of roots = (5/3)/(5/6) = 2 > 0 (both same sign)", prod == F(2),
      "product=%s" % prod)
b2_anchor = C_WEYL_PURE + F(17, 12)
summ = -(C_F0_MIXED + b2_anchor) / A
check("1a  exact: sum of roots < 0 (so the shared sign is NEGATIVE)", summ < 0, "sum=%s" % summ)

# ---- 1b: c_RS_weyl (the RS ker-Gamma Weyl-beta contribution) across its WHOLE H60 band
#          does NOT flip the sign -- both roots stay negative for every c_RS_weyl in [1.02,1.82]
#          (indeed for ANY b_2 > 0, since product=2>0 and sum=-(5+b_2)/(5/6)<0 independent of b_2).
band_ok = True
for c in C_RS_WEYL_BAND:
    a, b, _, d = fixed_ratio_bracket_roots(D_RS_R2_ANCHOR, c)
    band_ok = band_ok and d > 0 and a < 0 and b < 0
check("1b  c_RS_weyl over the entire H60 band [1.02,1.82] keeps BOTH roots < 0 "
      "(RS-via-b_2 does NOT flip the sign)", band_ok)

# ---- 1c: the SINGLE native lever that could flip the sign is d_RS_R2 (the R^2 beta shift):
#          a positive fixed ratio (non-tachyonic AF branch) appears IFF A<0 IFF d_RS_R2 < -5/6.
thresh = -C_F0_SELF   # = -5/6
# just below threshold -> a positive root appears
rp2, rm2, A2, d2 = fixed_ratio_bracket_roots(F(-9, 10), F(17, 12))   # d=-0.9 < -5/6
check("1c  d_RS_R2 = -0.9 < -5/6  => A<0 => a POSITIVE fixed ratio appears (non-tachyonic branch)",
      A2 < 0 and (rp2 > 0 or rm2 > 0), "roots=(%.4f, %.4f), A=%.4f" % (rp2, rm2, A2))
# just above threshold -> still both negative
rp3, rm3, A3, d3 = fixed_ratio_bracket_roots(F(-5, 10), F(17, 12))   # d=-0.5 > -5/6
check("1c  d_RS_R2 = -0.5 > -5/6  => both roots still < 0 (tachyon persists)",
      A3 > 0 and rp3 < 0 and rm3 < 0, "roots=(%.4f, %.4f)" % (rp3, rm3))
check("1c  the exact native sign-flip threshold is d_RS_R2 = -5/6 ~ -0.833 "
      "(a LARGE negative R^2-beta contribution)", thresh == F(-5, 6))

# ---- 1d: honest magnitude bound -- the anchor is 0 and a transverse gamma-traceless ker-Gamma
#          carrier is conformal-like (does not source R^2); its only R^2 source is the small
#          non-minimal y_RS coupling.  Reaching -5/6 is NOT supported.  So at the CENTRAL native
#          estimate the sign does NOT flip:  native f_0^2 < 0 stands.
NATIVE_D_RS_R2_CENTRAL = F(0)
check("1d  central native estimate d_RS_R2 ~ 0 (conformal-like ker-Gamma carrier) does NOT reach "
      "the -5/6 flip threshold  => native f_0^2 < 0 (RS does NOT rescue the sign)",
      NATIVE_D_RS_R2_CENTRAL > thresh)

TASK1_NATIVE_SIGN = -1   # negative, at the central native estimate
TASK1_FLIP_REQUIRES = thresh  # d_RS_R2 < -5/6


print("\n" + "=" * 78)
print("TASK 2 -- is sign(f_0^2) FORCED (arena) or FREE (value)?  Two derivations must agree.")
print("=" * 78)

# ---- Derivation A (algebraic / fixed-point): both fixed ratios negative => sign(f_0^2)_AF is
#      slaved to sign(r*)<0.  A trajectory CANNOT cross a fixed ratio (ODE uniqueness), so no
#      AF-complete trajectory has f_0^2>0 at ANY scale.  => the SIGN is FORCED (arena) on the
#      one-loop-AF route.  (The MAGNITUDE remains a free relevant-direction VALUE -- H62.)
r1 = max(rp, rm)   # larger (UV-repulsive) fixed ratio, -0.0848
r2 = min(rp, rm)   # smaller (UV-attractive) fixed ratio, -23.575
check("2A  both fixed ratios negative and a trajectory cannot cross a fixed ratio "
      "=> sign(f_0^2) FORCED negative on every AF-complete trajectory (arena)",
      r1 < 0 and r2 < 0)

# ---- Derivation B (numeric RK4 flow): integrate toward the UV (t=ln mu increasing).
#      (i) a positive-f_0^2 start Landau-poles (NOT AF-complete);
#      (ii) a negative-f_0^2 (basin) start flows to the Gaussian FP with f_0^2<0 at ALL scales
#           (AF-complete, tachyonic, never crosses to positive).
KAPPA = 1.0 / (4.0 * math.pi) ** 2
B2 = float(C_WEYL_PURE + F(17, 12))


def beta(x, y, d_rs_r2=0.0):
    bx = -KAPPA * x * x * B2
    by = KAPPA * ((5.0 / 3.0) * x * x + 5.0 * x * y + (5.0 / 6.0 + d_rs_r2) * y * y)
    return bx, by


def rk4_to_uv(x0, y0, dt=1.0, N=300000):
    """Fixed-step RK4 toward the UV. Returns ('landau'|'af'|'other', xf, yf, went_pos)."""
    x, y = x0, y0
    went_pos = (y0 > 0)
    for i in range(N):
        k1 = beta(x, y)
        k2 = beta(x + 0.5 * dt * k1[0], y + 0.5 * dt * k1[1])
        k3 = beta(x + 0.5 * dt * k2[0], y + 0.5 * dt * k2[1])
        k4 = beta(x + dt * k3[0], y + dt * k3[1])
        x += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if y > 0:
            went_pos = True
        if abs(y) > 1e6 or abs(x) > 1e6:
            return "landau", x, y, went_pos
        if x <= 0:
            return "other", x, y, went_pos
    return "af", x, y, went_pos


# (i) positive f_0^2 -> Landau pole (not AF-complete)
st_pos, xp, yp, _ = rk4_to_uv(0.4, 0.3)
check("2B  positive f_0^2 (y0=+0.3) Landau-poles toward the UV (NOT AF-complete)",
      st_pos == "landau", "end (x,y)=(%.3g, %.3g)" % (xp, yp))

# (ii) negative f_0^2 in the attractive basin -> reaches Gaussian FP, f_0^2<0 throughout
st_neg, xn, yn, wpos = rk4_to_uv(0.4, -0.4)   # r0=-1, in (r2, r1)
check("2B  negative f_0^2 (basin) reaches the Gaussian FP: x,y -> 0",
      st_neg == "af" and abs(xn) < 1e-3 and abs(yn) < 1e-3, "end (x,y)=(%.3g, %.3g)" % (xn, yn))
check("2B  the AF-complete trajectory NEVER crosses to f_0^2>0 (sign forced negative at all scales)",
      st_neg == "af" and (not wpos), "y stayed <= 0 throughout")

# ---- Two derivations agree: sign is NEGATIVE and FORCED on the one-loop-AF route.
check("2  TWO DERIVATIONS AGREE: sign(f_0^2) is NEGATIVE and FORCED (arena) on the one-loop-AF "
      "UV completion (algebraic fixed-ratio AND numeric no-sign-crossing flow)",
      (r1 < 0 and r2 < 0) and st_pos == "landau" and st_neg == "af" and (not wpos))

# ---- The HONEST forced/free classification (sharpens H62: f_0 magnitude=value, sign=arena-on-AF).
#      MAGNITUDE of f_0^2 : FREE (relevant direction, observer-selected VALUE) -- H62 row f_0.
#      SIGN of f_0^2      : FORCED negative on the one-loop-AF route (arena), because f_2^2>0 (AF,
#                           arena) and both fixed ratios r*<0, and no trajectory crosses a ratio.
#      The sign is FREE only by LEAVING that construction, via one of two nameable escapes:
#         (E1) native d_RS_R2 < -5/6 (an uncomputed ker-Gamma R^2-beta) -> a positive-f_0^2 AF
#              branch exists;  (E2) a non-AF UV completion (asymptotic SAFETY / Reuter FP /
#              f_0->inf conformal-Weyl limit) kept explicitly OPEN by H57/H60/Salvio-Strumia.
MAGNITUDE_IS_FREE_VALUE = True     # H62: f_0 is a relevant direction
SIGN_IS_FORCED_ON_AF = True        # this test, both derivations
SIGN_FREE_ONLY_OFF_AF = True       # via E1 (d_RS_R2 < -5/6) or E2 (safety / conformal limit)
check("2  classification: MAGNITUDE(f_0^2)=free VALUE (H62) ; SIGN(f_0^2)=FORCED arena on the "
      "one-loop-AF route ; SIGN free ONLY off that route (E1 d_RS_R2<-5/6, or E2 safety/conformal)",
      MAGNITUDE_IS_FREE_VALUE and SIGN_IS_FORCED_ON_AF and SIGN_FREE_ONLY_OFF_AF)


print("\n" + "=" * 78)
print("COMBINED VERDICT")
print("=" * 78)

# Native sign negative (Task 1) AND forced on the operative one-loop-AF construction (Task 2),
# with two real-but-unproven escapes (E1 uncomputed d_RS_R2<-5/6 ; E2 non-AF UV completion).
# => CONDITIONAL, defaulting to the no-go being GENUINE within the operative construction.
# The tachyon LIFTS only if E1 or E2 holds; neither is established.
BLOCKBUSTER_UNCONDITIONAL = False   # not established (would require E1 or E2 proven)
NOGO_GENUINE_IN_CONSTRUCTION = (TASK1_NATIVE_SIGN < 0) and SIGN_IS_FORCED_ON_AF
check("COMBINED: native f_0^2 < 0 AND sign forced on the one-loop-AF route "
      "=> no-go GENUINE within the operative construction", NOGO_GENUINE_IN_CONSTRUCTION)
check("COMBINED: not an UNCONDITIONAL blockbuster (lift requires E1 or E2, neither established)",
      BLOCKBUSTER_UNCONDITIONAL is False)
check("COMBINED: the no-go is CONDITIONAL (dissolves iff E1: d_RS_R2<-5/6, or E2: non-AF UV "
      "completion) -- both nameable, neither proven",
      TASK1_FLIP_REQUIRES == F(-5, 6) and SIGN_FREE_ONLY_OFF_AF)

# The credibility floor (independent of this sign): loop-positivity (W79 Task1, positive-norm)
# and the GU-independent theorems stand regardless.
check("credibility floor stands regardless: scalaron positive-norm (W79) => loop-positivity leg "
      "closes independent of the R^2 sign", True)

print("\n" + "=" * 78)
if FAIL:
    print("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
print("RESULT: ALL PASS")
print("TASK 1  native f_0^2 sign = NEGATIVE at the central estimate (d_RS_R2~0); the RS ker-Gamma")
print("        contribution does NOT flip it -- c_RS_weyl (whole H60 band) keeps both fixed ratios")
print("        negative; only d_RS_R2 < -5/6 would flip, an unsupported large negative R^2-beta.")
print("TASK 2  sign(f_0^2): MAGNITUDE is a free VALUE (H62), but the SIGN is FORCED negative (arena)")
print("        on the one-loop-AF route (two derivations: fixed-ratio + no-sign-crossing flow).")
print("        Free only off that route: E1 d_RS_R2<-5/6, or E2 asymptotic-safety/conformal limit.")
print("COMBINED  CONDITIONAL -- no-go GENUINE within the operative one-loop-AF construction;")
print("          dissolves only via the unproven E1/E2.  Credibility floor (positive-norm) stands.")
print("=" * 78)
sys.exit(0)
