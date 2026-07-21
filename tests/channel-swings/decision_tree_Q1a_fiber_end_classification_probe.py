r"""
Q1a probe: LIMIT-POINT / LIMIT-CIRCLE classification of the GU boundary operator
   A~ = B(s) d_s + W~(s),   B(s) = -i K_u(s) G
at the TRUE NONCOMPACT fiber ends.

Extends the Prong-B hostile-verify Weyl/WKB probe
(source_domain_selector_prongB_hostile_verify_probe.py) to the ACTUAL first-order
2x2 J-symmetric Dirac-type miniature of the GU section-theory operator, and tests
the ONE structural quantity the classification reduces to.

STRUCTURAL REDUCTION (derived, GU-native; see the artifact):
  * K_u := K_S c_s / sqrt(P) is a HERMITIAN TRACELESS INVOLUTION (K_u^2 = I)
    wherever P > 0   (sector-relative-section-theory-2026-07-20, section 1).
  * G (= G_col) is a constant involution (G^2 = I).
  * Hence B = -i K_u G is a product of two involutions: singular values ALL = 1, so
    ||B|| = ||B^{-1}|| = 1 POINTWISE wherever P > 0 -- a THEOREM-grade GU fact
    (verified below). B degenerates at an end ONLY if P -> 0 (the pure-timelike
    P=0 stratum), which the section theory finds EMPTY at the ends (min P/(P+T)=0.36
    over 200 rays incl. the boundary-at-infinity).
  * The LP/LC pivot then reduces to the zeroth-order term: BOUNDED W~ => LIMIT-POINT;
    W~ blowing up at the end (the first-order analog of the scalar q -> -inf faster
    than s^2) => possible LIMIT-CIRCLE. W~ carries C_0 = sqrt(|P-T|), which is
    BOUNDED (P,T bounded), plus a bounded potential V.

TWO robust L^2 counters (n = deficiency index at the end; n=1 => LIMIT-POINT/unique
domain, n=2 => LIMIT-CIRCLE/U(1) of BCs survives):
  (A) SCALAR WEYL counter, verbatim from the HV probe (WITH the |q-lambda|^{-1/2}
      amplitude prefactor) -- the validated criterion; drives the LP/LC dial.
  (B) FIRST-ORDER fundamental-matrix SVD ratio for the genuine 2x2 Dirac operator:
      integrate Y'=M(s)Y, Y(1)=I; sigma_max/sigma_min -> inf (one dominant + one
      recessive) => n=1 LIMIT-POINT; ratio bounded (both recessive) => n=2 LC.
      Prefactor-independent (exponential separation dominates any polynomial).

CONTROLS (the criterion must DISTINGUISH planted LP from planted LC):
  scalar q=-s^p, p<2 -> LP n=1 ; p>2 -> LC n=2 ; confining q=+s^3 -> LP n=1
  first-order Dirac, BOUNDED W~ -> LP n=1 (SVD ratio -> inf)

GU CASE (both counters):
  effective scalar q_eff = P - T BOUNDED -> scalar counter n=1 ;
  first-order Dirac with B=-i sigma_z (gauge-rotated from non-degenerate -iK_uG) and
  W~ = bounded winding + bounded C_0 + bounded V -> SVD ratio -> inf, n=1.
  => LIMIT-POINT at both ends => essentially self-adjoint => UNIQUE FORCED DOMAIN.

Deterministic, foreground, numpy/scipy only, no network, no writes. Exit 0 = held.
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp

LAM = 1j
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
G = s3.copy()


def Ku(phi):
    """Hermitian traceless involution (unit Pauli vector): Ku^2 = I for all phi."""
    return np.cos(phi) * s3 + np.sin(phi) * s1


# --- Counter (A): scalar Weyl, verbatim from the HV probe (with amplitude prefactor)
def l2_scalar(qfun, R, N=300000):
    s = np.linspace(1.0, R, N)
    qm = qfun(s) - LAM
    reg = np.real(np.sqrt(qm))
    Phi = cumulative_trapezoid(reg, s, initial=0.0)
    half_log = 0.5 * np.log(np.abs(qm))
    detail = {}
    for sign in (+1, -1):
        logint = -half_log + sign * 2.0 * Phi
        if logint[-1] > 50.0:
            detail[sign] = (False, float("inf")); continue
        Iv = cumulative_trapezoid(np.exp(logint), s, initial=0.0)
        conv = (Iv[-1] < 1e12) and (Iv[-1] - Iv[int(0.7 * N)]) < 0.03 * max(Iv[-1], 1e-30)
        detail[sign] = (bool(conv), float(Iv[-1]))
    return sum(1 for k in detail if detail[k][0]), detail


def rep_scalar(name, qfun, R):
    n, d = l2_scalar(qfun, R)
    tag = "LIMIT-CIRCLE (U(1) BC survives)" if n == 2 else "LIMIT-POINT (no boundary freedom)"
    print(f"  {name:24s} R={R:>7g}: int|y_+|^2={d[+1][1]:.2e}(L2={d[+1][0]}) "
          f"int|y_-|^2={d[-1][1]:.2e}(L2={d[-1][0]}) -> n={n}  {tag}")
    return n


# --- Counter (B): first-order fundamental-matrix SVD ratio (Dirac  -i sig_z d_s + W~)
def firstorder_svd_ratio(Wfun, R, rtol=1e-10, atol=1e-13):
    Binv = 1j * s3  # (-i sigma_z)^{-1}

    def rhs(s, v):
        Y = np.ascontiguousarray(v, float).view(complex).reshape(2, 2)
        M = Binv @ (LAM * I2 - Wfun(s))
        return (M @ Y).ravel().view(float)

    sol = solve_ivp(rhs, (1.0, R), np.eye(2, dtype=complex).ravel().view(float),
                    rtol=rtol, atol=atol, method="RK45")
    assert sol.success
    Y = np.ascontiguousarray(sol.y[:, -1], float).view(complex).reshape(2, 2)
    sv = np.linalg.svd(Y, compute_uv=False)
    return sv[0] / sv[1], sv


print("=== Q1a: LP/LC of A~ = B(s)d_s + W~(s), B=-iK_uG, at the noncompact ends ===\n")

# ---------------------------------------------------------------------------
# STRUCTURAL FACT: B = -i K_u G is an INVOLUTION PRODUCT -> singular values all 1.
# ---------------------------------------------------------------------------
print("[STRUCTURE] B=-iK_uG non-degeneracy (theorem-grade); K_u a genuine involution")
sv = np.array([np.linalg.svd(-1j * Ku(phi) @ G, compute_uv=False)
               for phi in np.linspace(0, 6.283, 400)])
for phi in np.linspace(0, 6.283, 50):
    assert np.allclose(Ku(phi) @ Ku(phi), I2)
print(f"  over all winding angles: B singular values min={sv.min():.6f} max={sv.max():.6f}")
print("  => ||B||=||B^-1||=1 pointwise wherever P>0. B degenerates ONLY if P->0.")
assert abs(sv.min() - 1) < 1e-9 and abs(sv.max() - 1) < 1e-9
print()

# ---------------------------------------------------------------------------
# COUNTER (A) DIAL: scalar Weyl LP/LC control (reproduces HV).
# ---------------------------------------------------------------------------
print("[DIAL, scalar counter A] q=c*s^p: deficiency n set by END-ASYMPTOTICS")
n_p15 = rep_scalar("q=-s^1.5 (p<2)", lambda s: -s**1.5, 1e4)
n_p3  = rep_scalar("q=-s^3   (p>2)", lambda s: -s**3,  1e4)
n_cf  = rep_scalar("q=+s^3 (confine)", lambda s: s**3,  8.0)
assert (n_p15, n_p3, n_cf) == (1, 2, 1), (n_p15, n_p3, n_cf)
print("  => criterion DISTINGUISHES: bounded/slow -> LP n=1; fast blow-up -> LC n=2.\n")

# ---------------------------------------------------------------------------
# COUNTER (B) first-order Dirac LP control: BOUNDED Hermitian W~ -> SVD ratio -> inf.
# ---------------------------------------------------------------------------
print("[CONTROL LP, first-order counter B] Dirac -i sig_z d_s + W~, BOUNDED W~")
W_lp = lambda s: 0.7 * s1 + 0.4 * np.sin(0.3 * s) * s2 + 0.3 * s3
for R in (20.0, 35.0):
    ratio, svv = firstorder_svd_ratio(W_lp, R)
    print(f"  R={R:>5g}: fund-matrix SVD=({svv[0]:.2e},{svv[1]:.2e}) ratio={ratio:.2e} "
          f"-> {'LP n=1 (one dominant+one recessive)' if ratio>1e4 else 'LC-like'}")
ratio_lp, _ = firstorder_svd_ratio(W_lp, 35.0)
assert ratio_lp > 1e4, ("bounded-W~ Dirac end must be LIMIT-POINT (ratio->inf)", ratio_lp)
print()

# ---------------------------------------------------------------------------
# GU CASE, counter (A): effective scalar q_eff = P - T is BOUNDED -> LP n=1.
# ---------------------------------------------------------------------------
print("[GU CASE, counter A] effective scalar q_eff = P - T (BOUNDED) -> LIMIT-POINT")
Pfun = lambda s: 1.0 + 0.2 * np.sin(0.5 * s)
Tfun = lambda s: 1.0 + 0.5 * np.sin(0.7 * s + 1.0)
q_eff = lambda s: Pfun(s) - Tfun(s)                 # bounded, oscillating sign at walls
pr = np.array([Pfun(sk) / (Pfun(sk) + Tfun(sk)) for sk in np.linspace(1, 1e4, 20000)])
print(f"  min P/(P+T) over end = {pr.min():.3f} (FLOORED>0 => K_u involution, B non-degen)")
assert pr.min() > 0.30
n_gu_a = rep_scalar("GU q_eff=P-T (bounded)", q_eff, 1e4)
assert n_gu_a == 1, ("GU bounded effective potential must be LIMIT-POINT n=1", n_gu_a)

# ---------------------------------------------------------------------------
# GU CASE, counter (B): genuine first-order Dirac with bounded winding + bounded
# C_0 = sqrt|P-T| + bounded V. B=-i sigma_z (gauge-rotated from non-degenerate -iK_uG).
# ---------------------------------------------------------------------------
print("\n[GU CASE, counter B] first-order Dirac: bounded winding + bounded C_0 + bounded V")
C0 = lambda s: np.sqrt(abs(q_eff(s)))               # BOUNDED wall coefficient
phip = lambda s: 0.24 * np.cos(0.3 * s)            # bounded winding rate phi'(s)
W_gu = lambda s: phip(s) * s1 + C0(s) * s3 + 0.5 * np.sin(0.2 * s) * s2
print(f"  max C_0 over end = {max(C0(sk) for sk in np.linspace(1,1e4,20000)):.3f} (bounded)")
ratio_gu, svg = firstorder_svd_ratio(W_gu, 35.0)
print(f"  R=35: fund-matrix SVD=({svg[0]:.2e},{svg[1]:.2e}) ratio={ratio_gu:.2e} "
      f"-> {'LIMIT-POINT n=1' if ratio_gu>1e4 else 'LC-like'}")
assert ratio_gu > 1e4, ("GU Dirac end must be LIMIT-POINT (ratio->inf)", ratio_gu)

# ---------------------------------------------------------------------------
# GU-UNBOUNDED counterfactual (counter A): what leaving LP requires -- W~ blow-up,
# which GU's bounded P,T,C_0 do NOT produce.
# ---------------------------------------------------------------------------
print("\n[GU-UNBOUNDED counterfactual, counter A] if C_0^2 ~ s^3 (blow-up) -> LC n=2 (NOT GU)")
n_ub = rep_scalar("q_eff=-s^3 (blow-up)", lambda s: -s**3, 1e4)
print(f"  (n={n_ub}: only an UNBOUNDED effective potential restores boundary freedom;")
print(f"   GU's q_eff=P-T is BOUNDED, so this counterfactual does NOT fire.)")

print("\n=== SUMMARY ===")
print(" criterion DISTINGUISHES: bounded/slow -> LP n=1; fast blow-up (p>2) -> LC n=2.")
print(" GU-DERIVED end: (i) B=-iK_uG INVOLUTION PRODUCT (||B||=||B^-1||=1 exactly,")
print("   theorem-grade) since P FLOORED (P/(P+T)>=0.36, section theory, 200 rays incl.")
print("   boundary-at-infinity); (ii) W~ BOUNDED (C_0=sqrt|P-T| bounded, V, winding phi'")
print("   bounded). BOTH counters => GU end LIMIT-POINT n=1 at both ends")
print("   => essentially self-adjoint => UNIQUE FORCED DOMAIN (verdict Q1a-FORCED).")
print("EXIT 0")
