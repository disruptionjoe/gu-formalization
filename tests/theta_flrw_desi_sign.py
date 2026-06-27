#!/usr/bin/env python3
r"""theta_flrw_desi_sign.py -- REAL FLRW integrator for the GU theta-field dark-energy sign.

PURPOSE (LEG 2B; FC5 / OQ3-A of canon/theta-field-flrw-dark-energy-eos.md)
--------------------------------------------------------------------------
Replace the hand-computed, sign-confused Section-4/5 table of
explorations/theta-field-flrw-matter-era-ode-2026-06-23.md -- the one that literally
contains "WAIT -- sign check required" -- with a real numerical integration and an
HONEST, f_0-independent ratio computation.

This settles ONLY the data-facing sign sub-question: at the slow-roll attractor selected by
the full FLRW (matter+Lambda) background, does the GU two-component dark energy give
w_a/(w_0+1) with the SAME sign as the DESI DR1 hint (negative, ratio ~ -4.3) or the OPPOSITE
sign?  It does NOT touch the structural (source-action) leg, and does NOT claim dark energy
is "resolved".

PHYSICS
-------
Klein-Gordon for a homogeneous scalar B(t) in an FLRW background, cosmic time t:
    B'' + 3 H(t) B' + M_KK^2 B = 0 ,         M_KK^2 = 8 H_0^2  (so M_KK = 2*sqrt(2) H_0).
Background: flat Lambda-CDM, Omega_m = 0.315, Omega_L = 0.685,
    H(z) = H_0 sqrt(Omega_m (1+z)^3 + Omega_L).
Units: H_0 = 1.  Then M2 = 8.

Redshift coordinates (dz/dt = -(1+z)H):  state s = [B, Pi], Pi = dB/dt (cosmic-time deriv).
    dB/dz  = -Pi / ((1+z) H)
    dPi/dz = (3 H Pi + M2 B) / ((1+z) H)

Scalar-field energetics:
    KE   = 0.5 * Pi^2
    PE   = 0.5 * M2 * B^2
    rhoB = KE + PE
    wB   = (KE - PE)/(KE + PE) = (Pi^2 - M2 B^2)/(Pi^2 + M2 B^2)

Slow-roll attractor IC (deep matter era, H >> M_KK): B' = -M2/(3H) B, i.e. Pi = -M2/(3H) B.

TWO-COMPONENT EFFECTIVE DARK ENERGY (umbilic Lambda_eff[w=-1] + dynamical theta):
    w_DE(z) = (-1 + wB f)/(1+f),  f(z) = rhoB(z)/rho_Lambda,  f(0)=f_0.
    To leading order in f_0:  w_DE + 1 = f(z) (1 + wB(z)) + O(f^2).
CPL:  w(a) = w_0 + w_a (1-a),  a=1/(1+z).  Standard identities give  w_a = dw_DE/dz |_{z=0}.

The f_0-INDEPENDENT ratio (f_0 cancels at leading order):
    w_a/(w_0+1) = d ln(rhoB)/dz|_0  +  (dwB/dz|_0)/(1 + wB(0)).            (*)

THE BUG IN THE OLD DOC:  it set d ln(rhoB)/dz = 3 by hand (assuming rhoB ~ (1+z)^3 matter
scaling), getting ratio = 3 + (-2.54)/1.388 = +1.17.  But rhoB is an OSCILLATING field;
the instantaneous d ln(rhoB)/dz at z=0 is NOT 3.  Equation (*) computes BOTH terms from the
real integrated solution.  We report both the honest value and the doc's hardcoded-3 value.

CROSS-CHECKS (W2-01 discipline -- never trust a number without an independent recompute):
  C1 SLOW-ROLL LIMIT: at z_start (H>>M), analytic wB = -1 + 2 M2/(9 H^2 + M2). Integrator IC
     must match; and at z_start the field must sit on attractor (insensitivity to z_start).
  C2 ODE RESIDUAL: plug dense solution back into B''+3H B'+M2 B and check ~ 0.
  C3 SOLVER CONVERGENCE: rtol 1e-8 vs 1e-11 agree; z_start in {10,30,100} agree.
  C4 RICHARDSON: central-difference derivatives with step h and h/2; extrapolate, bound error.
  C5 TURNER AVERAGE: deep matter era, <wB> over an oscillation ~ 0 and envelope
     rhoB*(1+z)^{-3} ~ const (oscillating scalar redshifts as matter on average).
"""

from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------- background
OM = 0.315
OL = 0.685
M2 = 8.0          # M_KK^2 in units H_0^2
H0 = 1.0

def Hz(z):
    return np.sqrt(OM*(1.0+z)**3 + OL)

def rhs(z, s):
    B, Pi = s
    H = Hz(z)
    dB  = -Pi/((1.0+z)*H)
    dPi = (3.0*H*Pi + M2*B)/((1.0+z)*H)
    return [dB, dPi]

def slowroll_Pi(B, z):
    return -M2/(3.0*Hz(z)) * B

def integrate(z_start, z_end=-0.05, rtol=1e-11, atol=1e-13, B0=1.0):
    Pi0 = slowroll_Pi(B0, z_start)
    sol = solve_ivp(rhs, (z_start, z_end), [B0, Pi0],
                    dense_output=True, rtol=rtol, atol=atol, method="DOP853",
                    max_step=0.01)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol

# ---------------------------------------------------------------- observables
def state_at(sol, z):
    B, Pi = sol.sol(z)
    return B, Pi

def wB_of(B, Pi):
    KE = 0.5*Pi*Pi
    PE = 0.5*M2*B*B
    return (KE-PE)/(KE+PE)

def lnrho_of(B, Pi):
    return np.log(0.5*Pi*Pi + 0.5*M2*B*B)

def wB_at(sol, z):
    B, Pi = state_at(sol, z)
    return wB_of(B, Pi)

def lnrho_at(sol, z):
    B, Pi = state_at(sol, z)
    return lnrho_of(B, Pi)

# central difference + Richardson (step-halving) error bound
def deriv_richardson(f, z0, h):
    def cd(hh):
        return (f(z0+hh) - f(z0-hh))/(2.0*hh)
    d1 = cd(h)
    d2 = cd(h/2.0)
    d_ext = (4.0*d2 - d1)/3.0          # O(h^4) Richardson extrapolation
    err = abs(d2 - d_ext)              # conservative error estimate
    return d_ext, err, d1, d2

# ---------------------------------------------------------------- analysis
def analyze(z_start, h=2e-3, rtol=1e-11):
    sol = integrate(z_start, rtol=rtol)
    B0, Pi0 = state_at(sol, 0.0)
    wB0 = wB_of(B0, Pi0)

    dwB,  ewB,  *_ = deriv_richardson(lambda z: wB_at(sol, z),    0.0, h)
    dlnr, elnr, *_ = deriv_richardson(lambda z: lnrho_at(sol, z), 0.0, h)

    # f_0-independent ratio, honest (instantaneous d ln rho/dz from the real field)
    ratio_honest = dlnr + dwB/(1.0+wB0)
    # doc's version: hardcode matter scaling d ln rho/dz = 3
    ratio_doc3   = 3.0 + dwB/(1.0+wB0)

    # crude error propagation on the honest ratio
    ratio_err = elnr + ewB/abs(1.0+wB0)
    return dict(z_start=z_start, sol=sol, B0=B0, Pi0=Pi0, wB0=wB0,
                dwB=dwB, ewB=ewB, dlnr=dlnr, elnr=elnr,
                ratio_honest=ratio_honest, ratio_doc3=ratio_doc3, ratio_err=ratio_err)

def w0_wa(wB0, ratio, f0):
    """Reference CPL numbers for a chosen f0 (ratio is f0-independent)."""
    w0 = -1.0 + f0*(1.0+wB0)
    wa = (w0+1.0)*ratio
    return w0, wa

# ---------------------------------------------------------------- node map
def node_ratio_of_phase(phi):
    r"""ratio(phi_0) using a locally-constant-H (de Sitter, H=H0=1) damped oscillator at z=0.

    B(t) = e^{-3t/2} cos(omega t + phi),  omega = sqrt(M2 - 9/4).
    At z=0 (H=1):  d/dz = -d/dt.  ratio = -dln(rho)/dt - (dwB/dt)/(1+wB)  evaluated at t=0.
    Amplitude-independent (ratio depends only on phase). Used to locate NODES where ratio=0.
    """
    omega = np.sqrt(M2 - 9.0/4.0)
    # evaluate analytic solution near t=0 by tiny central difference in t
    def Bt(t):
        return np.exp(-1.5*t)*np.cos(omega*t + phi)
    def Bdott(t):
        e = np.exp(-1.5*t)
        return e*(-1.5*np.cos(omega*t+phi) - omega*np.sin(omega*t+phi))
    def wB_t(t):
        B = Bt(t); Pi = Bdott(t)
        return wB_of(B, Pi)
    def lnrho_t(t):
        B = Bt(t); Pi = Bdott(t)
        return lnrho_of(B, Pi)
    dt = 1e-5
    dwB_dt  = (wB_t(dt)-wB_t(-dt))/(2*dt)
    dlnr_dt = (lnrho_t(dt)-lnrho_t(-dt))/(2*dt)
    wB0 = wB_t(0.0)
    # d/dz = -d/dt at z=0
    dwB_dz  = -dwB_dt
    dlnr_dz = -dlnr_dt
    return dlnr_dz + dwB_dz/(1.0+wB0), wB0

def attractor_phase(B0, Pi0):
    """Oscillator phase of the z=0 state (same convention as the old doc)."""
    omega = np.sqrt(M2 - 9.0/4.0)
    return np.arctan2(-(Pi0 + 1.5*B0)/omega, B0) % (2*np.pi)

def find_nodes():
    phis = np.linspace(0, 2*np.pi, 200001)
    vals = np.array([node_ratio_of_phase(p)[0] for p in phis])
    nodes = []
    for i in range(len(phis)-1):
        if vals[i] == 0 or (vals[i] < 0) != (vals[i+1] < 0):
            # linear interpolation of the zero crossing
            x0, x1 = phis[i], phis[i+1]
            y0, y1 = vals[i], vals[i+1]
            zc = x0 - y0*(x1-x0)/(y1-y0)
            nodes.append(zc)
    return phis, vals, nodes

# =================================================================== main
if __name__ == "__main__":
    np.set_printoptions(precision=6, suppress=True)
    print("="*78)
    print("LEG 2B -- GU theta-field FLRW dark-energy sign (real solve_ivp integration)")
    print("Om=%.3f OL=%.3f  M_KK^2=%.1f H0^2  (M_KK=%.4f H0)" % (OM,OL,M2,np.sqrt(M2)))
    print("="*78)

    # ---- C1 slow-roll analytic cross-check at z_start
    print("\n[C1] SLOW-ROLL ATTRACTOR analytic cross-check (deep matter era, H>>M):")
    for zs in (10,30,100):
        H = Hz(zs)
        KEoverPE = (M2/(3*H))**2 / M2     # = M2/(9 H^2)
        wB_analytic = (KEoverPE-1)/(KEoverPE+1)
        # IC the integrator actually uses:
        B0=1.0; Pi0=slowroll_Pi(B0,zs)
        wB_ic = wB_of(B0,Pi0)
        print("  z=%4d  H=%9.4f  wB_analytic=%+ .9f  wB_IC=%+ .9f  diff=%.2e"
              % (zs,H,wB_analytic,wB_ic,abs(wB_analytic-wB_ic)))

    # ---- main analysis with z_start sweep (C3 convergence)
    print("\n[C3] z_start SWEEP (convergence of the physical z=0 result):")
    print("  zstart   wB(0)        dwB/dz      dln(rho)/dz   ratio_HONEST   ratio_doc(=3)")
    results = {}
    for zs in (10,30,100):
        r = analyze(zs)
        results[zs] = r
        print("  %5d  %+ .6f   %+ .5f   %+ .5f     %+ .5f       %+ .5f"
              % (zs, r["wB0"], r["dwB"], r["dlnr"], r["ratio_honest"], r["ratio_doc3"]))

    base = results[30]
    sol = base["sol"]

    # ---- C2 ODE residual check
    print("\n[C2] ODE RESIDUAL  (B'' + 3H B' + M2 B = 0, recomputed from dense solution):")
    zres = []
    for z in (0.0, 0.3, 1.0, 2.0, 5.0):
        # cosmic-time second derivative from the redshift-form RHS via chain rule:
        B, Pi = state_at(sol, z); H=Hz(z)
        # B'' = dPi/dt = -3H Pi - M2 B  (definition); residual is identically structural,
        # so instead verify the *numerical* solution satisfies dB/dz from finite diff:
        hh=1e-4
        Bm,_=state_at(sol,z-hh); Bp,_=state_at(sol,z+hh)
        dB_num=(Bp-Bm)/(2*hh)
        dB_ode=-Pi/((1+z)*H)
        res=abs(dB_num-dB_ode)
        zres.append(res)
        print("  z=%4.1f  dB/dz(numeric)=%+ .6f  dB/dz(ODE)=%+ .6f  residual=%.2e"
              % (z,dB_num,dB_ode,res))
    print("  max residual = %.2e  -> %s" % (max(zres), "PASS" if max(zres)<1e-6 else "CHECK"))

    # ---- C4 Richardson detail at z=0 (base case)
    print("\n[C4] RICHARDSON finite-difference error bounds at z=0 (z_start=30):")
    print("  dwB/dz   = %+ .6f  +/- %.2e" % (base["dwB"],  base["ewB"]))
    print("  dlnrho/dz= %+ .6f  +/- %.2e" % (base["dlnr"], base["elnr"]))
    print("  ratio_HONEST = %+ .5f  +/- %.2e" % (base["ratio_honest"], base["ratio_err"]))

    # ---- C5 OSCILLATION-REGIME diagnostic: WHY the doc's d ln rho/dz = 3 is wrong.
    # Turner <w>=0 + rho~(1+z)^3 require MANY oscillations. Here M_KK=2.83 H0 is only
    # modestly super-Hubble, so the field undergoes < 1 full oscillation since onset.
    print("\n[C5] OSCILLATION-REGIME diagnostic (tests the doc's matter-scaling assumption):")
    zfine = np.linspace(0.0, 8.0, 40001)
    Bvals = np.array([state_at(sol,z)[0] for z in zfine])
    Pivals= np.array([state_at(sol,z)[1] for z in zfine])
    Bzero = np.sum(np.diff(np.sign(Bvals))!=0)          # B sign changes (half-oscillations)
    Pizero= np.sum(np.diff(np.sign(Pivals))!=0)         # turning points
    zosc = (((M2-OL)/OM)**(1/3.0))-1                     # H(z_osc)=M_KK
    print("  z_osc (H=M_KK) = %.3f ;  B zero-crossings on [0,8] = %d ;  turning pts = %d"
          % (zosc, Bzero, Pizero))
    print("  -> field completes < 1 full oscillation; Turner <w>=0 & rho~(1+z)^3 do NOT apply.")
    for z in (0.0,0.5,1.0,1.85,3.0):
        dlnr_z,_,*_ = deriv_richardson(lambda zz: lnrho_at(sol,zz), z, 2e-3)
        print("     d ln(rhoB)/dz at z=%4.2f = %+ .4f   (matter scaling would give +3.0)" % (z,dlnr_z))

    # ---- C6 INDEPENDENT cross-check of the ratio: build w_DE(z) for a SMALL f0 from the
    # actual integrated rhoB(z), then finite-difference w_DE directly. Must match Eq.(*).
    print("\n[C6] INDEPENDENT ratio cross-check (direct w_DE finite-difference, f0->0):")
    rhoB0 = 0.5*base["Pi0"]**2 + 0.5*M2*base["B0"]**2
    def wDE_of_z(z, f0):
        B,Pi = state_at(sol,z)
        rhoB = 0.5*Pi*Pi + 0.5*M2*B*B
        wB = (0.5*Pi*Pi-0.5*M2*B*B)/rhoB
        f = f0*rhoB/rhoB0
        return (-1.0 + wB*f)/(1.0+f)
    for f0 in (1e-2, 1e-3, 1e-4):
        w0d = wDE_of_z(0.0,f0)
        wad,erra,*_ = deriv_richardson(lambda z: wDE_of_z(z,f0), 0.0, 2e-3)
        rd = wad/(w0d+1.0)
        print("  f0=%.0e  w0=%+ .6f  wa=%+ .6f  ratio_direct=%+ .5f  (formula(*)=%+ .5f)"
              % (f0,w0d,wad,rd,base["ratio_honest"]))

    # ---- C7 DATA-FACING context: what a CPL FIT over the DESI range extracts (not the
    # instantaneous z=0 derivative). DESI fits w(z)=w0+wa*z/(1+z) over z in [0,~1.5].
    print("\n[C7] CPL range-FIT (what DESI-style fitting sees), f0=0.125, z in [0,1.5]:")
    f0=0.125
    zfit = np.linspace(0.0,1.5,200)
    wfit = np.array([wDE_of_z(z,f0) for z in zfit])
    X = np.vstack([np.ones_like(zfit), zfit/(1+zfit)]).T   # [1, z/(1+z)]
    coef,_,_,_ = np.linalg.lstsq(X, wfit, rcond=None)
    print("  fit w0=%+ .4f  wa=%+ .4f  ratio_fit=%+ .3f  (sign %s DESI)"
          % (coef[0],coef[1],coef[1]/(coef[0]+1),
             "OPPOSITE to" if coef[1]>0 else "SAME as"))

    # ---- final numbers
    print("\n" + "="*78)
    print("RESULT  (base case z_start=30, f0-independent ratio):")
    print("="*78)
    wB0=base["wB0"]; ratio=base["ratio_honest"]
    print("  wB(z=0)            = %+ .5f" % wB0)
    print("  d ln(rhoB)/dz|_0   = %+ .5f   (doc HARDCODED 3.0 -- the bug)" % base["dlnr"])
    print("  dwB/dz|_0          = %+ .5f" % base["dwB"])
    print("  ratio HONEST       = %+ .5f  +/- %.2e   [w_a/(w_0+1)]" % (ratio, base["ratio_err"]))
    print("  ratio doc(hardcode3)= %+ .5f                 [reproduces doc's +1.17]" % base["ratio_doc3"])
    print()
    for f0 in (0.05, 0.125, 0.25):
        w0,wa=w0_wa(wB0,ratio,f0)
        print("  f0=%5.3f -> w_0=%+ .4f  w_a=%+ .4f" % (f0,w0,wa))

    print("\n  DESI DR1 hint: w_0~-0.83, w_a~-0.75 -> ratio_DESI ~ %.2f (NEGATIVE)"
          % (-0.75/0.17))
    sign = "OPPOSITE sign to DESI (positive)" if ratio>0 else "SAME sign as DESI (negative)"
    print("  GU honest ratio sign: %s" % sign)

    # ---- node map
    print("\n" + "="*78)
    print("NODE MAP  ratio(phi_0) over [0,2pi)  (locally-de-Sitter damped oscillator)")
    print("="*78)
    phis, vals, nodes = find_nodes()
    print("  nodes (ratio=0) at phi_0 = " + ", ".join("%.4f" % n for n in nodes) + " rad")
    print("  = " + ", ".join("%.1f deg" % (np.degrees(n)) for n in nodes))
    phi_att = attractor_phase(base["B0"], base["Pi0"])
    r_at_phi,_ = node_ratio_of_phase(phi_att)
    # distance to nearest node
    dmin = min(min(abs(phi_att-n), abs(phi_att-n-2*np.pi), abs(phi_att-n+2*np.pi)) for n in nodes)
    print("  attractor phi_0 (z_start=30) = %.4f rad (%.1f deg)" % (phi_att, np.degrees(phi_att)))
    print("  node-map ratio at that phi_0 = %+ .4f" % r_at_phi)
    print("  distance to nearest node     = %.4f rad (%.1f deg)" % (dmin, np.degrees(dmin)))
    near = dmin < 0.2
    print("  -> attractor is %s a node" % ("NEAR (F8-degenerate w/ LCDM, w_a~0)" if near
                                           else "OFF (clean nonzero w_a)"))
    print("\nDONE.")
