"""
INDEPENDENT re-verification of MOVE-2.

Different formulation from BOTH the chaser (theta_flrw_wa.py) and the repo test:
  - independent variable: N = ln(a)  (e-folds), NOT redshift z, NOT cosmic time t
  - SECOND-ORDER ODE integrated directly (not the repo's [B,Pi] first-order z-form)
  - integrator: Radau (implicit) AND RK45, cross-checked (chaser used DOP853)
  - CPL fit done in BOTH (1-a) basis and z/(1+z) basis (the true CPL regressor)

Physics (same model, the only thing we are testing):
  KG: B_ddot + 3H B_dot + M2 B = 0,  M2 = 8 H0^2 (M_KK = 2 sqrt(2) H0), H0=1.
  Background pure LCDM: H^2 = Om a^-3 + OL,  Om=0.315, OL=0.685.
  Two-component DE: w_DE = (-1 + f wB)/(1+f),  f = f0 * rhoB(z)/rhoB(0).

In e-folds N=ln a (a=1/(1+z)):
  B_dot = H B_N ;  B_ddot = H^2 B_NN + H H_N B_N
  => B_NN + (3 + H_N/H) B_N + (M2/H^2) B = 0
  with 2 H H_N = dH^2/dN = -3 Om a^-3  => H_N/H = -1.5 Om a^-3 / H^2.
"""
import numpy as np
from scipy.integrate import solve_ivp

Om, OL, M2 = 0.315, 0.685, 8.0

def H2(a):   return Om*a**-3 + OL
def H(a):    return np.sqrt(H2(a))
def HN_over_H(a):  return -1.5*Om*a**-3 / H2(a)   # (dH/dN)/H

def rhs_N(N, y):
    a = np.exp(N)
    B, BN = y
    Hh = H(a)
    BNN = -(3.0 + HN_over_H(a))*BN - (M2/H2(a))*B
    return [BN, BNN]

def integrate(z_start=30.0, method="Radau"):
    a_start = 1.0/(1.0+z_start)
    N_start = np.log(a_start)
    B0 = 1.0
    # slow-roll attractor: B_dot = -M2/(3H) B  => H B_N = -M2/(3H) B => B_N = -M2/(3 H^2) B
    BN0 = -M2/(3.0*H2(a_start))*B0
    Ns = np.linspace(N_start, 0.0, 6000)
    sol = solve_ivp(rhs_N, (N_start, 0.0), [B0, BN0], t_eval=Ns,
                    rtol=1e-11, atol=1e-13, method=method, dense_output=True)
    assert sol.success, sol.message
    return sol

def observables(sol, f0=0.125):
    N = sol.t
    a = np.exp(N)
    z = 1.0/a - 1.0
    B, BN = sol.y
    Bdot = H(a)*BN                      # cosmic-time derivative
    KE = 0.5*Bdot**2
    PE = 0.5*M2*B**2
    rhoB = KE+PE
    wB = (KE-PE)/(KE+PE)
    # z=0 is where a=1 (last point). normalize rhoB there.
    i0 = np.argmin(np.abs(z))
    f = f0*rhoB/rhoB[i0]
    wDE = (-1.0 + f*wB)/(1.0+f)
    return z, a, B, Bdot, wB, rhoB, wDE

def cpl_fit(z, wDE, zmax, basis="one_minus_a"):
    a = 1.0/(1.0+z)
    m = z <= zmax
    if basis == "one_minus_a":
        x = 1.0 - a[m]                 # w = w0 + wa*(1-a): CPL exact
    else:
        x = z[m]/(1.0+z[m])            # equals 1-a; identical regressor
    y = wDE[m]
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, y, rcond=None)
    return w0, wa

def local_wa(z, wDE):
    """dw_DE/dz at z=0 via quadratic fit on small window (= CPL wa if w were CPL)."""
    i = np.argsort(z)
    zs, ws = z[i], wDE[i]
    w = zs <= 0.15
    c = np.polyfit(zs[w], ws[w], 2)     # c2 z^2 + c1 z + c0
    return c[1]                          # slope at z=0

if __name__ == "__main__":
    for method in ("Radau", "RK45"):
        sol = integrate(30.0, method=method)
        z, a, B, Bdot, wB, rhoB, wDE = observables(sol, f0=0.125)
        i0 = np.argmin(np.abs(z))
        print(f"=== method={method} (e-folds formulation, z_start=30, f0=0.125) ===")
        print(f"  B(0)={B[i0]:+.4f} Bdot(0)={Bdot[i0]:+.4f} wB(0)={wB[i0]:+.4f}")
        print(f"  wDE(0)={wDE[i0]:+.4f}")
        lw = local_wa(z, wDE)
        print(f"  LOCAL dwDE/dz|0 (=local wa) = {lw:+.4f}  sign={'+' if lw>0 else '-'}")
        for zmax in (0.5, 1.0, 1.5, 2.0):
            w0, wa = cpl_fit(z, wDE, zmax)
            print(f"  GLOBAL CPL fit z<={zmax}: w0={w0:+.4f} wa={wa:+.4f}  sign(wa)={'+' if wa>0 else '-'}")
        print()

    # w_DE(z) shape (non-monotone check) -- find the peak
    sol = integrate(30.0, method="Radau")
    z, a, B, Bdot, wB, rhoB, wDE = observables(sol, f0=0.125)
    i = np.argsort(z); zs, ws = z[i], wDE[i]
    mask = zs <= 1.0
    jmax = np.argmax(ws[mask])
    print(f"w_DE peak within z<=1: z_peak={zs[mask][jmax]:.3f} wDE_peak={ws[mask][jmax]:+.4f}")
    print(f"w_DE(z=0)={ws[0]:+.4f}  w_DE(z=1)~{np.interp(1.0,zs,ws):+.4f}  w_DE(z=2)~{np.interp(2.0,zs,ws):+.4f}")
    print(f"NON-MONOTONE (rises from z=0 to shallow peak, then falls): "
          f"{ws[mask][jmax] > ws[0] and np.interp(1.0,zs,ws) < ws[0]}")

    # f0-independent LOCAL ratio wa/(w0+1) via tiny-f0 limit (independent of chaser's LO formula)
    print("\n=== local ratio wa/(w0+1) as f0->0 (should be f0-independent) ===")
    for f0 in (1e-1, 1e-2, 1e-3):
        z, a, B, Bdot, wB, rhoB, wDE = observables(sol, f0=f0)
        i0 = np.argmin(np.abs(z))
        w0 = wDE[i0]
        wa = local_wa(z, wDE)
        print(f"  f0={f0:.0e}: w0={w0:+.5f} local_wa={wa:+.5f} ratio={wa/(w0+1):+.4f}")

    # DESI comparison
    print("\nDESI DR1: w0=-0.827, wa=-0.75 (wa NEGATIVE).")
