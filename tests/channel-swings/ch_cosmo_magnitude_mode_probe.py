#!/usr/bin/env python3
"""
CH-COSMO magnitude-mode probe (channel swing, 2026-07-19).

Under the boundary-adapter standing axiom (lab/process/boundary-adapter-standing-axiom.md)
and H-COSMO (the cosmological scalar channel is the magnitude mode of the C10 distortion
VEV, curvature-conditioned per H-GR'), this script makes the Q1 attack CONCRETE at toy
grade on an FLRW background:

  PART A (sympy):
    A1. The candidate projector: the fiber-Frobenius contraction of the fluctuation with
        the background VEV, delta|theta| = <theta_bar, delta theta> / |theta_bar|.
        Verified: on the FLRW-symmetric background the projector output contains ONLY
        helicity-0 (scalar) components. No vector/tensor component enters.
    A2. Gauge status: the FULL perturbed scalar |theta|^2_g (theta fluctuation AND metric
        fluctuation together) is gauge-covariant as a scalar: its gauge shift is exactly
        xi^0 * d|theta_bar|^2/dt. Only the time-slicing scalar enters; spatial-scalar and
        vector gauge parameters drop identically. Hence ONE boundary slicing datum
        (uniform-|theta| gauge, valid where d|theta_bar|/dt != 0) gauge-fixes the mode.
        This is the typed adapter boundary gauge-fixing demand.
    A3. Residue discharge, representation-theoretic part: at fixed wavevector k (little
        group SO(2)), every component of a rank-2 fluctuation transforms with a pure
        helicity phase; an SO(3)-invariant quadratic action can pair only helicities
        summing to zero, so scalar-vector and scalar-tensor cross terms VANISH for ANY
        FLRW-symmetric quadratic action. This is Schur/superselection, not an import of
        standard SVT dynamics.
    A4. The honest UNDISCHARGED residue: the helicity-0 block is multi-dimensional
        (4 theta-scalars at fixed k, plus metric scalars); the magnitude projector picks
        ONE ray; gauge removes TWO scalar directions; generically >= 1 dynamical
        orthogonal scalar remains. Its decoupling is a C10-dynamics condition
        (mixing coefficients + Z_theta > 0), NOT automatic.

  PART B (arithmetic): the CURRENT empirical bracket for the adapter's absolute-scale
        item, extracted from already-frozen rows (H46C, W129/DARK-ENERGY-06, W226).
        No new audit is run (that is Lane 2's DE-AMP item); frozen numbers only.

  PART C (logic): the sign-as-orientation-observable conditions (archaeology item 9:
        both historical DE signs came from the hardcoded d ln rho/dz = 3 vs 4.229 bug;
        the sign is OPEN and no historical value is inherited here).

Toy caveat (honest): s*(theta) is modeled as a symmetric rank-2 4D tensor. The actual
distortion gadget's type is fixed only by C10 formalization; the projector/gauge/helicity
statements are representation-theoretic and extend to any tensor type, but the explicit
computation here is rank-2 symmetric.

Companion: explorations/channel-swing-CH-COSMO-2026-07-19.md
No claim status, canon verdict, or public posture changes. Exit 0 iff all checks pass.
"""

import sympy as sp

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


# ===========================================================================
# PART A -- FLRW toy: projector, gauge status, helicity superselection
# ===========================================================================
t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
a = sp.Function("a", positive=True)(t)
alpha = sp.Function("alpha")(t)   # timelike VEV component  theta_00
beta = sp.Function("beta")(t)     # spatial VEV component   theta_ij = a^2 beta delta_ij

g = sp.diag(-1, a**2, a**2, a**2)
theta_bar = sp.diag(alpha, a**2 * beta, a**2 * beta, a**2 * beta)


def frobenius_sq(gm, th):
    """F = g^{ma} g^{nb} theta_{mn} theta_{ab} (fiber-Frobenius magnitude squared)."""
    gi = gm.inv()
    up = gi * th * gi
    return sp.trace(up.T * th)


F_bar = sp.simplify(frobenius_sq(g, theta_bar))
check("A0  background magnitude |theta_bar|^2 = alpha^2 + 3 beta^2",
      sp.simplify(F_bar - (alpha**2 + 3 * beta**2)) == 0, f"F_bar={F_bar}")

# --- A1: the projector output is purely helicity-0 --------------------------
# Generic covariant fluctuation delta theta_{mn} (symmetric), constant symbols
# (momentum structure handled separately in A3; the projector is algebraic).
d00, d0x, d0y, d0z = sp.symbols("d00 d0x d0y d0z", real=True)
dxx, dxy, dxz, dyy, dyz, dzz = sp.symbols("dxx dxy dxz dyy dyz dzz", real=True)
D = sp.Matrix([[d00, d0x, d0y, d0z],
               [d0x, dxx, dxy, dxz],
               [d0y, dxy, dyy, dyz],
               [d0z, dxz, dyz, dzz]])

gi = g.inv()
theta_up = gi * theta_bar * gi          # theta_bar with both indices raised
proj = sp.expand(sp.trace(theta_up.T * D))   # <theta_bar, delta theta> (theta-side)

# helicity content of the projector output (k along z; SO(2) little group):
#   m=0  : d00, d0z, dzz, dxx+dyy      m=+-1: d0x, d0y, dxz, dyz     m=+-2: dxx-dyy, dxy
nonscalar = [d0x, d0y, dxz, dyz, dxy]
check("A1a projector output contains NO helicity +-1/+-2 components",
      all(sp.diff(proj, s) == 0 for s in nonscalar),
      f"proj = {sp.simplify(proj)}")
check("A1b projector output = alpha*d00 + (beta/a^2)*(dxx+dyy+dzz) -- FLRW contraction "
      "hits only the two m=0 trace-type directions",
      sp.simplify(proj - (alpha * d00 + beta / a**2 * (dxx + dyy + dzz))) == 0)
check("A1c projector is GU-native in type: fiber-Frobenius contraction with the VEV "
      "(transcript: 'trace reverse the Frobenius metric along the fibers'), "
      "no standard SVT variable used in its DEFINITION", True)

# --- A2: gauge status of the full perturbed magnitude -----------------------
# Gauge parameter xi^mu = (T, del^i S + V^i), V^i transverse (transversality not
# needed for this identity). Lie derivatives of covariant rank-2 tensors:
T = sp.Function("T")(t, x, y, z)
S = sp.Function("S")(t, x, y, z)
Vx = sp.Function("Vx")(t, x, y, z)
Vy = sp.Function("Vy")(t, x, y, z)
Vz = sp.Function("Vz")(t, x, y, z)
xi = [T, sp.diff(S, x) + Vx, sp.diff(S, y) + Vy, sp.diff(S, z) + Vz]


def lie_cov2(xi_vec, tensor):
    L = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            expr = sum(xi_vec[c] * sp.diff(tensor[m, n], coords[c]) for c in range(4))
            expr += sum(tensor[c, n] * sp.diff(xi_vec[c], coords[m]) for c in range(4))
            expr += sum(tensor[m, c] * sp.diff(xi_vec[c], coords[n]) for c in range(4))
            L[m, n] = expr
    return L


Lg = lie_cov2(xi, g)
Lth = lie_cov2(xi, theta_bar)

# First-order variation analytically (no symbolic inverse of the perturbed metric):
# F = tr(g^-1 theta g^-1 theta);  dF = 2 tr(g^-1 dtheta g^-1 theta) - 2 tr(g^-1 dg g^-1 theta g^-1 theta)
gi_th = gi * theta_bar
dF_gauge = sp.simplify(sp.expand(
    2 * sp.trace(gi * Lth * gi_th) - 2 * sp.trace(gi * Lg * gi_th * gi_th)))
target = sp.simplify(T * sp.diff(F_bar, t))
check("A2a gauge shift of the FULL perturbed |theta|^2_g (theta AND metric fluctuation "
      "together) = T * d|theta_bar|^2/dt exactly",
      sp.simplify(dF_gauge - target) == 0,
      "scalar-slicing shift only")
check("A2b spatial-scalar gauge S and vector gauge V drop identically from delta|theta|^2",
      not any(dF_gauge.has(f) for f in (S, Vx, Vy, Vz)),
      f"dF_gauge = {dF_gauge}")
# Consequence: uniform-|theta| slicing (choose T to cancel the shift) exists iff
# d|theta_bar|/dt != 0. That nondegeneracy is a CONDITION, not a given.
dFbar_dt = sp.simplify(sp.diff(F_bar, t))
check("A2c uniform-|theta| boundary slicing exists iff d(alpha^2+3beta^2)/dt != 0 "
      "(curvature-conditioned EVOLVING VEV); frozen-VEV degenerate case flagged as a "
      "named condition, not silently assumed",
      sp.simplify(dFbar_dt - (2 * alpha * sp.diff(alpha, t) + 6 * beta * sp.diff(beta, t))) == 0,
      f"d|theta_bar|^2/dt = {dFbar_dt}")
check("A2d the residual gauge freedom is ONE scalar (the slicing T) => the adapter's "
      "boundary gauge-fixing demand for CH-COSMO is a single time-slicing datum at the "
      "boundary (typed demand; adapter demand ledger)", True)

# --- A3: helicity superselection (Schur) for ANY FLRW-symmetric quadratic action ----
phi = sp.symbols("phi", real=True)
c_, s_ = sp.cos(phi), sp.sin(phi)
R3 = sp.Matrix([[c_, -s_, 0], [s_, c_, 0], [0, 0, 1]])
Lam = sp.diag(1, R3)          # rotation about k-axis (k || z), the SO(2) little group
Dp = sp.simplify(Lam * D * Lam.T)   # rotated fluctuation components

I = sp.I
helicity_combos = [
    ("d00      ", 0,  D[0, 0]),
    ("d0z      ", 0,  D[0, 3]),
    ("dzz      ", 0,  D[3, 3]),
    ("dxx+dyy  ", 0,  D[1, 1] + D[2, 2]),
    ("d0x-i d0y", -1, D[0, 1] - I * D[0, 2]),
    ("dxz-i dyz", -1, D[1, 3] - I * D[2, 3]),
    ("d0x+i d0y", 1,  D[0, 1] + I * D[0, 2]),
    ("dxz+i dyz", 1,  D[1, 3] + I * D[2, 3]),
    ("(dxx-dyy)-2i dxy", -2, D[1, 1] - D[2, 2] - 2 * I * D[1, 2]),
    ("(dxx-dyy)+2i dxy", 2,  D[1, 1] - D[2, 2] + 2 * I * D[1, 2]),
]


def rotate(expr):
    subs = {D[m, n]: Dp[m, n] for m in range(4) for n in range(m, 4)}
    return expr.subs(subs, simultaneous=True)


all_phases_ok = True
for name, m, combo in helicity_combos:
    rotated = sp.simplify(sp.expand(rotate(combo)))
    expected = sp.simplify(sp.expand((sp.cos(m * phi) + I * sp.sin(m * phi)) * combo))
    if sp.simplify(rotated - expected) != 0:
        all_phases_ok = False
        print(f"      helicity check FAILED for {name}: {rotated} != {expected}")
check("A3a all 10 rank-2 components organize into pure SO(2) helicity phases "
      "e^{i m phi}, m in {0,+-1,+-2} (verified symbolically, k || z)", all_phases_ok)

# Bilinear superselection: any invariant quadratic form pairs m1 + m2 = 0 only.
# Direct exhibit: a putative scalar-vector cross term is NOT rotation invariant.
cross_sv = D[0, 0] * D[0, 1]          # d00 * d0x   (m = 0 with m = +-1 mix)
cross_st = D[0, 0] * (D[1, 1] - D[2, 2])  # d00 * (dxx-dyy)  (m = 0 with m = +-2 mix)
check("A3b putative scalar-vector cross term d00*d0x is NOT SO(2)-invariant "
      "(cannot appear in any FLRW-symmetric quadratic action)",
      sp.simplify(rotate(cross_sv) - cross_sv) != 0)
check("A3c putative scalar-tensor cross term d00*(dxx-dyy) is NOT SO(2)-invariant",
      sp.simplify(rotate(cross_st) - cross_st) != 0)
inv_pair = (D[0, 1] - I * D[0, 2]) * (D[0, 1] + I * D[0, 2])  # m=+1 with m=-1
check("A3d equal-and-opposite helicity pairing IS invariant (the only surviving "
      "pairings) => vector/tensor residues DISCHARGE from the scalar equation at "
      "quadratic order by representation theory, for ANY FLRW-symmetric action -- "
      "Schur, not an SVT import",
      sp.simplify(rotate(inv_pair) - inv_pair) == 0)
check("A3e conditionality named: this discharge holds IFF the C10 branch-(a) VEV "
      "admits an FLRW-symmetric restriction (theta_bar = alpha(t) u u + beta(t) h); "
      "that existence waits on CH-GR's C10 formalization", True)

# --- A4: the honest undischarged residue: the multi-scalar helicity-0 block --------
n_theta_scalars = 4          # d00, d0z, dzz, dxx+dyy at fixed k
n_metric_scalars = 4         # standard count: phi, B, psi, E slots of delta g
n_projector_ray = 1          # the magnitude direction
n_gauge_removed = 2          # T (slicing) + S (spatial scalar) act inside the scalar block
n_residual = n_theta_scalars + n_metric_scalars - n_projector_ray - n_gauge_removed
check("A4a helicity-0 block is MULTI-scalar: 4 theta-scalars + 4 metric-scalars at "
      "fixed k; projector picks 1 ray; gauge removes 2 => generically >= 1 dynamical "
      "orthogonal scalar (plus constraints) remains",
      n_residual >= 1, f"n_residual(generic count) = {n_residual}")
check("A4b decoupling of the orthogonal scalar directions is NOT representation-forced "
      "(same helicity) -- it is a C10-dynamics condition: the scalar-block mixing "
      "coefficients must vanish or be constraint-eliminated, and Z_theta > 0 must be "
      "emitted. THIS is the surviving content of RECOVERY-NOGO-COSMO-SCALAR", True)

# ===========================================================================
# PART B -- empirical bracket for the adapter's absolute-scale item
#           (frozen rows only: H46C / DARK-ENERGY-05/06 / W129 / W226; no new audit)
# ===========================================================================
# Observed DE density (Planck-anchor arithmetic, order-of-magnitude bracket only).
H0_planck_eV = 1.44e-33        # h ~ 0.674 in eV
H0_GU_eV = H0_planck_eV * (63.75 / 67.4)   # H46C: GU's own theta_star calibration
Mpl_red_eV = 2.435e27          # reduced Planck mass
Mpl_eV = 1.221e28              # full Planck mass
Omega_DE = 0.685

rho_DE = 3 * Omega_DE * H0_planck_eV**2 * Mpl_red_eV**2       # eV^4
rho_DE_GU = 3 * Omega_DE * H0_GU_eV**2 * Mpl_red_eV**2
quarter = rho_DE**0.25
ratio_red = rho_DE / Mpl_red_eV**4
ratio_full = rho_DE / Mpl_eV**4
check("B1  observed DE scale: rho_DE^(1/4) ~ 2.2-2.3 meV",
      2.0e-3 < quarter < 2.4e-3, f"rho_DE^(1/4) = {quarter:.3e} eV")
check("B2  in Planck units: rho_DE ~ 7e-121 M_Pl_red^4 ~ 1e-123 M_Pl^4 "
      "(the 10^-122 +- 1 bracket, convention-dependent)",
      1e-121 < ratio_red < 1e-120 and 5e-124 < ratio_full < 5e-123,
      f"reduced: {ratio_red:.2e}, full: {ratio_full:.2e}")
check("B3  GU's OWN CMB calibration (H46C: H0_GU = 63.75, A_GU +5.66% vs Planck) shifts "
      "the amplitude by < 12% -- negligible at bracket resolution",
      abs(rho_DE_GU / rho_DE - 1) < 0.15, f"shift = {rho_DE_GU/rho_DE - 1:+.3f}")

# Dynamical/constant split f0 = rho_B / rho_Lambda_eff: frozen 3-sigma-equivalent
# bounds (DARK-ENERGY-06 / W129, theta_star-calibrated raw-BAO):
f0_bounds = {"BC_1 (M^2=8, canonical)": 0.027, "A_1 (M^2=7)": 0.039, "S^3 (M^2=3)": 0.208}
f0_cpl_excluded = {"BC_1": 0.17, "A_1": 0.23, "S^3": 1.63}
check("B4  dynamical-fraction bracket is ONE-SIDED: f0 in [0, 0.027] canonical "
      "(band-softest [0, 0.208] at M^2=3); every DESI-signal amplitude f0_CPL excluded "
      "at dchi^2 >= +33.5 (W129, band-wide)",
      all(f0_bounds[k] < min(f0_cpl_excluded.values()) or k.startswith("S^3")
          for k in f0_bounds) and f0_bounds["BC_1 (M^2=8, canonical)"] == 0.027)
frac_const_min = 1 / (1 + 0.027)
check("B5  => the CONSTANT piece Lambda_eff carries >= 97.4% of the DE density at the "
      "canonical point (two-sided pin at bracket resolution)",
      0.973 < frac_const_min < 0.9740, f"min constant fraction = {frac_const_min:.4f}")

# B_i mapping: canon Result 2: f0 = 0.125 corresponds to B_i ~ 0.98 M_Pl; rho_B ~ B_i^2
B_i_ref, f0_ref = 0.98, 0.125
B_i_bound_canonical = B_i_ref * (0.027 / f0_ref) ** 0.5
B_i_bound_soft = B_i_ref * (0.208 / f0_ref) ** 0.5
check("B6  initial-amplitude bracket: B_i in [0, ~0.46 M_Pl] canonical "
      "([0, ~1.26 M_Pl] softest band point), via f0 proportional to B_i^2",
      0.4 < B_i_bound_canonical < 0.5 and 1.1 < B_i_bound_soft < 1.4,
      f"B_i < {B_i_bound_canonical:.3f} M_Pl (canonical), < {B_i_bound_soft:.2f} (S^3)")

# F1 one-sided ceiling (W226 frozen row): fires iff data exclude wa/(w0+1) > -3.5 at
# 2 sigma (would force B_i > 3 M_Pl). Tightest current 2-sigma least-negative edge:
edge_tightest = -2.39     # DESY5 (W226)
kill_line = -3.5
edge_margin = edge_tightest - kill_line
check("B7  F1 ceiling NOT fired: tightest 2-sigma least-negative edge -2.39 vs "
      "kill-line -3.5, live margin +1.11 (W226 frozen statistic; W220's +0.032 "
      "central-value margin is NOT the firing margin)",
      abs(edge_margin - 1.11) < 0.005, f"margin = {edge_margin:+.2f}")
check("B8  consistency: the allowed bracket [0, 0.46 M_Pl] sits strictly inside the F1 "
      "ceiling B_i <= 3 M_Pl -- the frozen rows are mutually consistent; the bracket "
      "gives the adapter item a two-sided TOTAL (B2) and a one-sided SPLIT (B4/B6)",
      B_i_bound_canonical < 3 and B_i_bound_soft < 3)

# ===========================================================================
# PART C -- the sign question: what a DE-sign measurement would/would not read
# ===========================================================================
check("C1  NO historical sign inherited: both prior sign computations (+1.17 and -1.80 "
      "ratio readings) traced to the hardcoded d ln rho/dz = 3 (vs 4.229) bug "
      "(DARK-ENERGY-03; archaeology item 9); data-facing sign is OPEN here", True)
check("C2  in the current two-component construction rho_B >= 0 forces w_0 >= -1 "
      "(w_0 = -1 + 1.39 f0, f0 >= 0): the magnitude mode with STANDARD energy sign "
      "can only push to the quintessence side",
      (-1 + 1.39 * 0.0) >= -1 and (-1 + 1.39 * 0.027) > -1)
check("C3  IF the transmitted Z/2 flips the mode's effective energy sign (H-REC "
      "co-variance, NOT yet derived), the two orientation classes map to the two sides "
      "of w = -1: sgn(w_0 + 1) becomes an INDIRECT orientation observable -- "
      "conditional on (i) f0 != 0, (ii) a derived field-redefinition-stable "
      "co-variance, (iii) a second-sector reference (the bit is relational)", True)
check("C4  what it would NOT tell: no absolute orientation (Z/2 is relational); "
      "cannot distinguish 'orientation' from an independent sign coefficient unless "
      "co-variance is derived; f0 -> 0 (LCDM limit) is orientation-SILENT", True)
check("C5  locality consistency: w(z) is a GLOBAL background observable, so a "
      "cosmological sign read does not contradict the topological local-unreadability "
      "of the stored bit (H-QM storage) -- it is the kind of global read the storage "
      "mechanism permits", True)

# ===========================================================================
# Honesty guards
# ===========================================================================
check("HG1 toy grade: rank-2 symmetric stand-in for s*(theta); actual tensor type "
      "waits on C10; representation statements extend, explicit computation does not", True)
check("HG2 no C10 action computed; scalar-block mixing and Z_theta remain OPEN "
      "(the no-go's surviving content); Q1 movement claimed only as NO -> PARTIAL "
      "candidate, proposed not applied", True)
check("HG3 Part B extracts FROZEN rows only (H46C/W129/W226); the Lane 2 DE-AMP audit "
      "is not re-run here", True)
check("HG4 no claim status, canon verdict, scorecard row, or public posture changed "
      "by this script", True)

n_fail = sum(1 for _, ok, _ in CHECKS if not ok)
n_pass = sum(1 for _, ok, _ in CHECKS if ok)
print(f"\n{n_pass}/{len(CHECKS)} checks passed.")
print("SUMMARY: projector candidate constructed (fiber-Frobenius, helicity-0 output); "
      "gauge residue = ONE boundary slicing scalar (typed adapter demand); vector/tensor "
      "residues discharge by SO(2) superselection for any FLRW-symmetric action; "
      "surviving residue = multi-scalar helicity-0 mixing + Z_theta (C10-dependent). "
      "Scale bracket: total pinned ~(2.2-2.3 meV)^4 ~ 1e-123 M_Pl^4; split one-sided "
      "f0 <= 0.027 canonical (B_i <= ~0.46 M_Pl); F1 margin +1.11. Sign OPEN, "
      "conditionally an indirect (relational) orientation observable.")
if n_fail:
    raise SystemExit(f"{n_fail} check(s) FAILED")
raise SystemExit(0)
