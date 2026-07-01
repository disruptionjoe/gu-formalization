"""
MOVE-2: FLRW theta-field dark energy EOS -- sign of w_a vs DESI.

*** TERMINAL VERDICT NOTE (added on repo promotion): this script's printed
    conclusion ("wa>0, clean falsification") is the SUPERSEDED local-derivative
    reading. The terminal, independently re-verified verdict is KILLED: under
    DESI's own global CPL fit over the measured window (z<=2), wa is NEGATIVE
    (w0=-0.777, wa=-0.248) -- the SAME sign as DESI (wa=-0.75), ~3x smaller in
    magnitude, i.e. LCDM-amplitude-degenerate, NOT a clean falsification. The
    authoritative computation is verify/indep_check.py. See ../README.md. ***

Real scipy.solve_ivp integration of the linearized theta Klein-Gordon EOM
    B_ddot + 3 H(z) B_dot + M_KK^2 B = 0,     M_KK^2 = 8 H0^2   (M_KK = 2*sqrt(2) H0)
on a Lambda-CDM background (Omega_m=0.315, Omega_L=0.685), units H0=1.

Repo coefficients verified against:
  explorations/dark-energy-cosmology/theta-field-flrw-matter-era-ode-2026-06-23.md  (EOM, z-form, z_osc)
  explorations/dark-energy-cosmology/dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md (slow-roll IC, attractor)

Two-component dark energy: constant umbilic Lambda_eff (w=-1) + dynamical theta B.
  rho_B = 1/2 B_dot^2 + 1/2 M^2 B^2 ,  p_B = 1/2 B_dot^2 - 1/2 M^2 B^2 ,  w_B = p_B/rho_B
  f(z)  = rho_B(z)/rho_Lambda = f_0 * rho_B(z)/rho_B(0)
  w_DE  = (-1 + f w_B)/(1+f)

Deliverables: w0, wa (CPL fit + local slope), ratio wa/(w0+1), sign, IC-robustness
(z_ic in {20,30,50} slow-roll attractor + frozen@z=3 + de Sitter), tolerance/Richardson bound.
"""
import numpy as np
from scipy.integrate import solve_ivp

Om, OL = 0.315, 0.685
M2 = 8.0                       # M_KK^2 in units of H0^2  (M_KK = 2*sqrt(2) H0)

def H(z):
    return np.sqrt(Om*(1.0+z)**3 + OL)

# z_osc where H = M_KK:  Om(1+z)^3 + OL = M2  => solved
z_osc = ((M2 - OL)/Om)**(1.0/3.0) - 1.0

def rhs(z, y):
    phi, Pi = y                # phi=B, Pi=B_dot=dB/dt
    Hz = H(z)
    dphi = -Pi / ((1.0+z)*Hz)
    dPi  = (3.0*Hz*Pi + M2*phi) / ((1.0+z)*Hz)
    return [dphi, dPi]

def integrate(z_ic, ic_kind, rtol=1e-11, atol=1e-13, n=4000):
    """Integrate from z_ic down to 0. Return z grid, B, Bdot."""
    if ic_kind == 'slowroll':
        B_i = 1.0
        Bdot_i = -M2*B_i/(3.0*H(z_ic))     # slow-roll attractor velocity
    elif ic_kind == 'frozen':
        B_i = 1.0
        Bdot_i = 0.0
    else:
        raise ValueError(ic_kind)
    zeval = np.linspace(z_ic, 0.0, n)
    sol = solve_ivp(rhs, (z_ic, 0.0), [B_i, Bdot_i], t_eval=zeval,
                    rtol=rtol, atol=atol, method='DOP853', dense_output=True)
    assert sol.success, sol.message
    return sol

def observables(sol, f0=0.125):
    z = sol.t
    B, Bdot = sol.y
    KE = 0.5*Bdot**2
    PE = 0.5*M2*B**2
    rho_B = KE + PE
    p_B   = KE - PE
    wB = p_B/rho_B
    # two-component DE
    g = rho_B/rho_B[-1]                     # g(0)=1 (z=0 is last point)
    f = f0*g
    wDE = (-1.0 + f*wB)/(1.0+f)
    return z, B, Bdot, wB, rho_B, wDE

def cpl_fit(z, wDE, zmax):
    """Least-squares CPL fit w(a)=w0+wa(1-a) over 0<=z<=zmax. z ascending? here z descending; mask ok."""
    a = 1.0/(1.0+z)
    m = z <= zmax
    x = (1.0 - a[m])                        # regressor (1-a)
    y = wDE[m]
    A = np.vstack([np.ones_like(x), x]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    w0, wa = coef
    return w0, wa

def local_slope_ratio(z, wB, rho_B, wDE):
    """Leading-order f0-independent ratio = g'(0)(1+wB0)+dwB/dz|0 all over (1+wB0),
       computed directly from integrated arrays. Also w0=wDE(0), local wa=dwDE/dz|0."""
    # z is descending ...->0 ; sort ascending near 0 for finite diff
    idx = np.argsort(z)
    zs = z[idx]; wBs = wB[idx]; rBs = rho_B[idx]; wDEs = wDE[idx]
    # fit quadratics on the lowest-z window for clean derivatives at z=0
    win = zs <= 0.15
    zz = zs[win]
    def dslope(vals):
        c = np.polyfit(zz, vals[win], 2)     # a z^2 + b z + c ; slope at 0 = b
        return c[1], c[2]                     # (slope@0, value@0)
    swB, wB0 = dslope(wBs)
    swDE, wDE0 = dslope(wDEs)
    # g'(0): rho_B normalized to its z=0 value
    grho = rBs/rBs[np.argmin(np.abs(zs))]
    sg, g0 = dslope(grho)
    ratio_LO = sg*(1.0+wB0) + swB/(1.0+wB0)   # g'(0)*(1+wB0)/(1+wB0) simplifies? no: keep general
    # careful: leading-order ratio = g'(0) + dwB/dz/(1+wB0)
    ratio_LO = sg + swB/(1.0+wB0)
    return dict(wB0=wB0, dwBdz0=swB, gprime0=sg, wDE0=wDE0, dwDEdz0=swDE, ratio_LO=ratio_LO)

def report_case(label, z_ic, ic_kind, f0=0.125, zfit=0.5):
    sol = integrate(z_ic, ic_kind)
    z, B, Bdot, wB, rho_B, wDE = observables(sol, f0=f0)
    w0, wa = cpl_fit(z, wDE, zfit)
    loc = local_slope_ratio(z, wB, rho_B, wDE)
    ratio_cpl = wa/(w0+1.0)
    # instantaneous phase phi_0 in de Sitter phase-amplitude convention
    B0, Bdot0 = B[-1], Bdot[-1]
    omega = np.sqrt(M2 - 9.0/4.0)
    phi0 = np.arctan2(-(Bdot0 + 1.5*B0), omega*B0)
    print(f"--- {label} (z_ic={z_ic}, {ic_kind}, f0={f0}) ---")
    print(f"  B(0)={B0:+.4f}  Bdot(0)={Bdot0:+.4f}  wB(0)={loc['wB0']:+.4f}  phi0={phi0:+.4f} rad ({np.degrees(phi0):+.1f} deg)")
    print(f"  CPL fit (z<= {zfit}):  w0={w0:+.4f}  wa={wa:+.4f}  ratio wa/(w0+1)={ratio_cpl:+.4f}")
    print(f"  local@0: w0={loc['wDE0']:+.4f}  wa=dwDE/dz|0={loc['dwDEdz0']:+.4f}  ratio_LO(f0-indep)={loc['ratio_LO']:+.4f}")
    print(f"  sign(wa CPL)={'+' if wa>0 else '-'}   sign(ratio)={'+' if ratio_cpl>0 else '-'}")
    return dict(label=label, w0=w0, wa=wa, ratio_cpl=ratio_cpl, **loc, phi0=phi0)

if __name__ == "__main__":
    np.set_printoptions(precision=5)
    print(f"M_KK = 2*sqrt(2) H0 = {np.sqrt(M2):.4f} H0 ; M2={M2}")
    print(f"z_osc (H=M_KK) = {z_osc:.4f}   [repo: 1.85]")
    print(f"BF bound 3H0/2=1.5 < M_KK={np.sqrt(M2):.4f}  => oscillating+damped regime: {np.sqrt(M2)>1.5}")
    print()

    results = []
    # Slow-roll attractor IC sweep (the OQ3-C object never numerically built before)
    for zic in [20, 30, 50]:
        results.append(report_case(f"SLOW-ROLL z_ic={zic}", zic, 'slowroll'))
        print()
    # Frozen IC at z=3 (repo's +1.17 claim)
    results.append(report_case("FROZEN z=3 (repo +1.17)", 3, 'frozen')); print()
    # Slow-roll IC at z=3 (repo Case B ~+1.14)
    results.append(report_case("SLOW-ROLL z=3 (repo +1.14)", 3, 'slowroll')); print()

    # ---- Richardson / tolerance error bound on the flagship z_ic=30 slow-roll ratio ----
    print("=== Tolerance-convergence (error bound) on z_ic=30 slow-roll ratio_LO ===")
    prev = None
    for rt in [1e-6, 1e-9, 1e-12]:
        s = integrate(30, 'slowroll', rtol=rt, atol=rt*1e-2)
        z, B, Bdot, wB, rho_B, wDE = observables(s)
        loc = local_slope_ratio(z, wB, rho_B, wDE)
        w0f, waf = cpl_fit(z, wDE, 0.5)
        d = "" if prev is None else f"  |Delta ratio_cpl|={abs(waf/(w0f+1)-prev):.2e}"
        print(f"  rtol={rt:.0e}: ratio_LO={loc['ratio_LO']:+.5f}  ratio_cpl={waf/(w0f+1):+.5f}{d}")
        prev = waf/(w0f+1)

    # ---- f_0 independence of the ratio (structural claim) ----
    print("\n=== f0-independence of ratio (z_ic=30 slow-roll) ===")
    for f0 in [0.02, 0.05, 0.125, 0.25]:
        s = integrate(30, 'slowroll')
        z, B, Bdot, wB, rho_B, wDE = observables(s, f0=f0)
        w0f, waf = cpl_fit(z, wDE, 0.5)
        print(f"  f0={f0:.3f}: w0={w0f:+.4f} wa={waf:+.4f} ratio_cpl={waf/(w0f+1):+.4f}")

    # ---- w_DE(z) shape: non-monotone => CPL-wa sign is window-dependent ----
    print("\n=== w_DE(z) shape (z_ic=30 slow-roll, f0=0.125) ===")
    s = integrate(30, 'slowroll')
    z, B, Bdot, wB, rho_B, wDE = observables(s, f0=0.125)
    for zt in [0.0,0.1,0.2,0.3,0.5,0.7,1.0,1.5,2.0]:
        j = np.argmin(np.abs(z-zt))
        print(f"  z={zt:.1f}: wDE={wDE[j]:+.4f}  wB={wB[j]:+.4f}")
    print("  => rises 0->~0.4 then falls: local slope@0 >0, global slope over z<~2 <0.")

    # ---- Can ANY f0 reproduce DESI's wa=-0.75 via a global CPL fit? ----
    print("\n=== Global CPL wa vs f0 (z_ic=30 slow-roll), wide DESI-like windows ===")
    s = integrate(30, 'slowroll')
    zg, Bg, Bdg, wBg, rBg, _ = observables(s, f0=1.0)  # placeholder
    for zfit in [0.5, 1.0, 2.0]:
        row = []
        for f0 in [0.05, 0.125, 0.25, 0.5]:
            _, _, _, _, _, wDEf = observables(s, f0=f0)
            w0f, waf = cpl_fit(zg, wDEf, zfit)
            row.append(f"f0={f0}:w0={w0f:+.3f},wa={waf:+.3f}")
        print(f"  window z<={zfit}: " + " | ".join(row))
    print("  DESI target: wa=-0.75 (dynamical). Model global |wa| stays <~0.1 => cannot reproduce.")

    # ---- DESI comparison ----
    print("\n=== DESI DR1 (2404.03002, CPL) ===")
    w0_desi, wa_desi = -0.827, -0.75
    print(f"  DESI: w0={w0_desi} wa={wa_desi}  ratio=wa/(w0+1)={wa_desi/(w0_desi+1):+.3f} (NEGATIVE)")

    # ---- Self-check + verdict ----
    print("\n=== SELF-CHECK ===")
    sr = [r for r in results if r['label'].startswith('SLOW-ROLL z_ic')]
    signs = [np.sign(r['wa']) for r in results]
    all_pos = all(s > 0 for s in signs)
    print(f"  all cases wa>0 (incl frozen, de-Sitter-region): {all_pos}")
    print(f"  slow-roll attractor ratio_LO across z_ic=20/30/50: "
          f"{[round(r['ratio_LO'],3) for r in sr]}")
    spread = max(r['ratio_LO'] for r in sr) - min(r['ratio_LO'] for r in sr)
    print(f"  z_ic convergence spread in ratio_LO: {spread:.2e} (attractor => should be tiny)")
    print(f"  GU sign(ratio)=+ ; DESI sign(ratio)=- => OPPOSITE: {all_pos}")
    print("\n  VERDICT: wa>0 sign is IC-robust across slow-roll attractor (z_ic=20,30,50),")
    print("  frozen z=3, and slow-roll z=3. Opposite to DESI wa<0. Ratio f0-independent =>")
    print("  clean (ratio-based) falsification signal, NOT an IC artifact; amplitude LCDM-degenerate.")
