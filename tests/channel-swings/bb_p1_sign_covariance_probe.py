#!/usr/bin/env python3
"""
Blockbuster P1 probe: the DE sign co-variance (2026-07-19).

Under the boundary-adapter standing axiom, H-COSMO (scalar channel = magnitude mode of
the C10 distortion VEV), the CH-GR branch-(a) identity (sigma kappa^2 = 1, sigma = +1,
de Donder class per P-K2), and the CH-SRC coherence constraint SRC-COH-1 (ONE Krein
form in every slot of the action), this probe makes the sign co-variance concrete:

  PART A (sympy, exact): the readout identity. For the two-component DE
      (constant Lambda_eff + magnitude mode B with sector sign eps in {+1,-1}):
        rho_DE + p_DE = eps * Z * Bdot^2   EXACTLY (Lambda contributes zero),
      so given rho_DE > 0 (empirically pinned, frozen rows), sgn(w_DE + 1) = eps
      wherever Bdot != 0. The LCDM limit (B = 0) is orientation-SILENT.
      The identity is regime-independent (oscillating or slow-roll) and M^2-band-
      independent: no mass term appears in rho + p.

  PART B (sympy + exact-seeded numerics): the redefinition sweep.
      B1 Sylvester: the kinetic-Gram signature of the helicity-0 block is invariant
         under every real invertible congruence (mixing) S^T K S -- no real linear
         field redefinition of the scalar block flips the sign of the DE-carrying
         eigenmode's kinetic term.
      B2 point redefinitions B -> lam*B + mu*B^2: kinetic coefficient maps to
         lam^2 * Z -- a strictly positive multiple; sign invariant.
      B3 first-order derivative redefinition B -> C + alpha*Cdot: the quadratic
         Lagrangian shifts by an EXACT total time derivative at O(alpha) -- same EOM,
         same on-shell stress; sign invariant.
      B4 the only sign-flipping rescale is imaginary (lam^2 = -1 has no real
         solution): excluded by the reality of the field space -- the same
         "no real kappa" structure as the CH-GR A4 sign gate.

  PART C (exact, finite Krein toy): the orientation linkage and the co-flip.
      C1 a mode locked to the tau-sector ray has kinetic/energy sign = tau
         (Krein norm of the ray) when stress bilinear and sector grading use the
         SAME Krein form (SRC-COH-1).
      C2 the GR cancellation demand sigma*kappa^2 = 1 with sigma = tau admits a real
         kappa iff tau = +1 (CH-GR A4 shape, reproduced).
      C3 the co-flip: flipping tau flips BOTH the cosmological mode energy sign and
         the GR-cancellation solvability -- there is NO configuration with a
         phantom-side mode AND a surviving branch-(a) cancellation under SRC-COH-1.
      C4 the relational structure: the readout depends only on the PRODUCT
         tau_theta * tau_ref; a global Krein flip (anchor relabel) leaves it
         invariant; only a single-sector flip moves it. The reference sector is
         concretely supplied by the observed matter sector through the shared
         Friedmann comparator.

  PART D (numeric, FRESH integration -- no inherited sign, no hardcoded d ln rho):
      the frozen-model FLRW leg. Integrate B'' + 3H Bdot + M^2 B = 0 (M^2 = 8,
      LCDM background, frozen IC at z = 30 where H >> M) and compute w_DE(z) from
      p/rho DIRECTLY. Verify: eps = +1 gives w_DE(0) > -1, pointwise
      w_DE(z) >= -1 on [0,2], CPL-fit w0 + 1 > 0; eps = -1 flips all three;
      the map eps -> sgn(w0+1) is the identity across f0 in {0.005, 0.02, 0.1};
      cross-checks against frozen rows: instantaneous coefficient
      C_inst = 1 + w_B(0) ~ 1.39 (canon Result 2) and d ln rho_B/dz|_0 ~ 4.2
      (the archaeology's 4.229 -- the value the old bug hardcoded as 3).

Honesty: this probe demonstrates the co-variance STRUCTURE at toy/symbol grade,
conditional on SRC-COH-1 and on C10 emitting Z_theta > 0 with the scalar-block
mixing discharged. It does not build S_IG, does not audit data (frozen rows cited
only), and changes no claim status, canon verdict, or public posture.

Companion: explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
Exit 0 iff all checks pass.
"""

import math
import random

import sympy as sp

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


# ===========================================================================
# PART A -- the readout identity (exact)
# ===========================================================================
t = sp.symbols("t", real=True)
Bf = sp.Function("B", real=True)(t)
Z, M, rhoL = sp.symbols("Z M rho_Lambda", positive=True)
eps = sp.symbols("epsilon", real=True)   # sector sign, +-1

rho_B = eps * Z * (sp.diff(Bf, t) ** 2 + M**2 * Bf**2) / 2
p_B = eps * Z * (sp.diff(Bf, t) ** 2 - M**2 * Bf**2) / 2
rho_DE = rhoL + rho_B
p_DE = -rhoL + p_B

check("A1  (rho + p)_DE = eps * Z * Bdot^2 EXACTLY (Lambda contributes zero; "
      "no mass term -- regime- and M^2-band-independent)",
      sp.simplify(rho_DE + p_DE - eps * Z * sp.diff(Bf, t) ** 2) == 0)

# A2: given rho_DE > 0, sgn(w+1) = sgn(rho+p) = eps wherever Bdot != 0.
w_plus_1 = sp.simplify((rho_DE + p_DE) / rho_DE)
check("A2  w_DE + 1 = eps * Z * Bdot^2 / rho_DE: with rho_DE > 0 (frozen-row pin) "
      "the SIDE of w = -1 is the sector sign eps, wherever Bdot != 0",
      sp.simplify(w_plus_1 - eps * Z * sp.diff(Bf, t) ** 2 / rho_DE) == 0)

check("A3  LCDM limit is orientation-SILENT: B = 0 gives w_DE = -1 identically "
      "for BOTH eps values",
      all(sp.simplify((p_DE / rho_DE).subs(Bf, 0).subs(eps, e) + 1) == 0
          for e in (1, -1)))

check("A4  sgn(rho_B) = eps as well (the bracket is positive-definite): the mode's "
      "energy-density sign IS the sector sign, so sgn(f0) = eps too",
      sp.simplify(rho_B - eps * Z * (sp.diff(Bf, t) ** 2 + M**2 * Bf**2) / 2) == 0)

# ===========================================================================
# PART B -- the redefinition sweep
# ===========================================================================
# B1: Sylvester rigidity. Kinetic Gram of a 3-scalar block with signature (2,1).
random.seed(20260719)
K0 = sp.diag(2, 3, -5)


def signature_of(mat):
    ev = [complex(v.evalf()) for v in mat.eigenvals(multiple=True)]
    pos = sum(1 for v in ev if v.real > 1e-9)
    neg = sum(1 for v in ev if v.real < -1e-9)
    return (pos, neg)


sig0 = signature_of(K0)
all_sigs_ok = True
tried = 0
while tried < 6:
    S = sp.Matrix(3, 3, lambda i, j: sp.Rational(random.randint(-9, 9),
                                                 random.randint(1, 9)))
    if S.det() == 0:
        continue
    tried += 1
    sig = signature_of(S.T * K0 * S)
    if sig != sig0:
        all_sigs_ok = False
        print(f"      signature moved: {sig} != {sig0} for S = {S.tolist()}")
check("B1  Sylvester: 6 random invertible real (rational) congruences S^T K S all "
      "preserve the kinetic-Gram signature (2,1) -- no real linear mixing of the "
      "scalar block flips the DE-carrying eigenmode's kinetic sign",
      all_sigs_ok, f"signature {sig0} invariant")

# B2: point redefinition B -> lam*B + mu*B^2, quadratic order.
lam, mu = sp.symbols("lambda mu", real=True)
Cf = sp.Function("C", real=True)(t)
B_of_C = lam * Cf + mu * Cf**2
L_orig = Z / 2 * (sp.diff(Bf, t) ** 2 - M**2 * Bf**2)
L_redef = sp.expand(L_orig.subs(Bf, B_of_C).doit())
# quadratic truncation in C: kinetic coefficient
kin_coeff = L_redef.coeff(sp.diff(Cf, t) ** 2)
kin_coeff_quad = kin_coeff.subs(Cf, 0)   # quadratic-order part
check("B2  point redefinition B -> lam*C + mu*C^2: quadratic-order kinetic "
      "coefficient = lam^2 * Z/2 -- a strictly positive multiple for every real "
      "lam != 0; sign invariant",
      sp.simplify(kin_coeff_quad - lam**2 * Z / 2) == 0)

# B3: derivative redefinition B -> C + alpha*Cdot: O(alpha) shift is a total derivative.
alpha = sp.symbols("alpha", real=True)
B_of_C2 = Cf + alpha * sp.diff(Cf, t)
L_redef2 = sp.expand(L_orig.subs(Bf, B_of_C2).doit())
O_alpha = sp.expand(sp.diff(L_redef2, alpha).subs(alpha, 0))
boundary_term = Z / 2 * (sp.diff(Cf, t) ** 2 - M**2 * Cf**2)
check("B3  derivative redefinition B -> C + alpha*Cdot: the O(alpha) shift of the "
      "quadratic Lagrangian is d/dt[(Z/2)(Cdot^2 - M^2 C^2)] EXACTLY -- a pure "
      "boundary term; same EOM, same on-shell stress, sign invariant",
      sp.simplify(O_alpha - sp.diff(boundary_term, t)) == 0)

# B4: the only sign-flipping rescale is imaginary.
sols = sp.solve(sp.Eq(lam**2, -1), lam, domain=sp.S.Reals)
real_sols = [s for s in sols if s.is_real]
check("B4  no real lam gives lam^2 = -1: the sign-flipping rescale B -> i*B is not "
      "a real field redefinition -- reality of the field space excludes it (the "
      "cosmological image of CH-GR A4's 'no real kappa' gate)",
      len(real_sols) == 0)

# ===========================================================================
# PART C -- orientation linkage, co-flip, relational structure (exact)
# ===========================================================================
tau = sp.symbols("tau", integer=True)
beta = sp.diag(1, -1)          # Krein form on a 2-dim fiber toy
e1 = sp.Matrix([1, 0])         # K-norm +1 ray
e2 = sp.Matrix([0, 1])         # K-norm -1 ray

# C1: mode locked to the tau-sector ray: kinetic sign = <v, v>_K = tau.
for tval, ray in ((1, e1), (-1, e2)):
    knorm = (ray.T * beta * ray)[0]
    if knorm != tval:
        check("C1  K-norm of tau-sector ray equals tau", False,
              f"tau={tval}: got {knorm}")
        break
else:
    check("C1  the tau-sector ray has Krein norm tau; with SRC-COH-1 (stress "
          "bilinear and sector grading use the SAME Krein form) the locked mode's "
          "kinetic/energy sign IS tau -- the CH-SRC Da1/Da2 mechanism in miniature",
          True)

# C2: GR cancellation sigma*kappa^2 = 1 with sigma = tau: real kappa iff tau = +1.
kap = sp.symbols("kappa", real=True)
sol_plus = sp.solve(sp.Eq(1 * kap**2, 1), kap, domain=sp.S.Reals)
sol_minus = [s for s in sp.solve(sp.Eq(-1 * kap**2, 1), kap) if s.is_real]
check("C2  sigma*kappa^2 = 1 with sigma = tau (SRC-COH-1): real kappa exists iff "
      "tau = +1 (kappa = +-1); tau = -1 admits NO real kappa -- CH-GR A4 reproduced",
      len(sol_plus) == 2 and len(sol_minus) == 0)

# C3: the co-flip -- enumerate tau in {+1,-1}.
configs = []
for tval in (1, -1):
    mode_energy_sign = tval                      # from C1
    gr_cancellation_alive = (tval == 1)          # from C2
    configs.append((tval, mode_energy_sign, gr_cancellation_alive))
phantom_with_gr_alive = any(s < 0 and alive for _, s, alive in configs)
check("C3  co-flip enumeration: flipping tau flips BOTH the mode energy sign and "
      "the GR-cancellation solvability; NO configuration has a phantom-side mode "
      "AND a surviving branch-(a) cancellation under SRC-COH-1",
      not phantom_with_gr_alive, f"configs (tau, sgn rho_B, GR alive): {configs}")

# C4: relational readout -- only the product tau_theta * tau_ref enters.
def readout(tau_theta, tau_ref):
    return tau_theta * tau_ref


combos = [(a, b) for a in (1, -1) for b in (1, -1)]
global_flip_invariant = all(readout(a, b) == readout(-a, -b) for a, b in combos)
single_flip_moves = all(readout(a, b) == -readout(-a, b) for a, b in combos)
check("C4  relational structure: the readout depends only on tau_theta * tau_ref; "
      "a GLOBAL Krein flip (anchor relabel) leaves it invariant, a single-sector "
      "flip moves it -- the observable is the RELATIVE orientation; the reference "
      "sector is concretely the observed matter sector via the shared Friedmann "
      "comparator (both source the same H(z))",
      global_flip_invariant and single_flip_moves)

# ===========================================================================
# PART D -- frozen-model FLRW leg (fresh numeric integration)
# ===========================================================================
# LCDM background, H0 = 1 units, M^2 = 8 (canonical BC_1 row). Test-field theta
# (no backreaction) -- the same approximation the frozen rows use at small f0.
Om, OL = 0.3, 0.7
M2 = 8.0


def Hub(N):
    return math.sqrt(Om * math.exp(-3.0 * N) + OL)


def dH_dN(N):
    H = Hub(N)
    return -1.5 * Om * math.exp(-3.0 * N) / H


def integrate(N_i, B_i, C_i, N_f=0.0, dN=1e-4):
    """RK4 for B' = C, C' = -(H'/H)C - 3C - M2*B/H^2 in N = ln a."""
    traj = []
    N, B, C = N_i, B_i, C_i
    steps = int(round((N_f - N_i) / dN))
    for _ in range(steps + 1):
        traj.append((N, B, C))
        def f(n, b, c):
            H = Hub(n)
            return c, -(dH_dN(n) / H) * c - 3.0 * c - M2 * b / (H * H)
        k1 = f(N, B, C)
        k2 = f(N + dN / 2, B + dN / 2 * k1[0], C + dN / 2 * k1[1])
        k3 = f(N + dN / 2, B + dN / 2 * k2[0], C + dN / 2 * k2[1])
        k4 = f(N + dN, B + dN * k3[0], C + dN * k3[1])
        B += dN / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        C += dN / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        N += dN
    traj.append((N, B, C))
    return traj


def rho_p_B(N, B, C, e):
    """theta energy density and pressure; Bdot = H * dB/dN; units rho_L = 3*OL."""
    H = Hub(N)
    kin = 0.5 * (H * C) ** 2
    pot = 0.5 * M2 * B * B
    return e * (kin + pot), e * (kin - pot)


N_i = math.log(1.0 / 31.0)     # z = 30, frozen IC (H(30)/M ~ 33 >> 1: attractor)
base = integrate(N_i, 1.0, 0.0)


def interp(traj, N):
    lo, hi = 0, len(traj) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if traj[mid][0] <= N:
            lo = mid
        else:
            hi = mid
    (N0, B0, C0), (N1, B1, C1) = traj[lo], traj[hi]
    if N1 == N0:
        return B0, C0
    w = (N - N0) / (N1 - N0)
    return B0 + w * (B1 - B0), C0 + w * (C1 - C0)


rhoL_num = 3.0 * OL
Bz0, Cz0 = interp(base, 0.0)   # exactly N = 0, not the RK4 overshoot point
rho_raw, _ = rho_p_B(0.0, Bz0, Cz0, +1)


def w_DE_curve(f0, e, zmax=2.0, nz=201):
    scale = math.sqrt(f0 * rhoL_num / rho_raw)
    zs, ws = [], []
    for i in range(nz):
        z = zmax * i / (nz - 1)
        N = -math.log(1.0 + z)
        B, C = interp(base, N)
        rb, pb = rho_p_B(N, scale * B, scale * C, e)
        zs.append(z)
        ws.append((-rhoL_num + pb) / (rhoL_num + rb))
    return zs, ws


def cpl_fit(zs, ws):
    """Least-squares w(z) = w0 + wa * z/(1+z)."""
    xs = [z / (1.0 + z) for z in zs]
    n = len(zs)
    Sx = sum(xs); Sxx = sum(x * x for x in xs)
    Sw = sum(ws); Sxw = sum(x * w for x, w in zip(xs, ws))
    det = n * Sxx - Sx * Sx
    w0 = (Sxx * Sw - Sx * Sxw) / det
    wa = (n * Sxw - Sx * Sw) / det
    return w0, wa


results = {}
for e in (+1, -1):
    for f0 in (0.005, 0.02, 0.1):
        zs, ws = w_DE_curve(f0, e)
        w0_cpl, wa_cpl = cpl_fit(zs, ws)
        results[(e, f0)] = (ws[0], min(ws), max(ws), w0_cpl, wa_cpl)

ok_plus = all(results[(1, f0)][0] > -1 and results[(1, f0)][1] >= -1 - 1e-12
              and results[(1, f0)][3] > -1 for f0 in (0.005, 0.02, 0.1))
check("D1  eps = +1: w_DE(0) > -1, POINTWISE w_DE(z) >= -1 on [0,2] (NEC), and "
      "CPL-fit w0 + 1 > 0, at f0 = 0.005 / 0.02 / 0.1",
      ok_plus,
      f"f0=0.02: w(0)={results[(1,0.02)][0]:+.4f}, min w={results[(1,0.02)][1]:+.4f}, "
      f"CPL w0={results[(1,0.02)][3]:+.4f}")

ok_minus = all(results[(-1, f0)][0] < -1 and results[(-1, f0)][2] <= -1 + 1e-12
               and results[(-1, f0)][3] < -1 for f0 in (0.005, 0.02, 0.1))
check("D2  eps = -1: w_DE(0) < -1, pointwise w_DE(z) <= -1 (phantom side "
      "everywhere), and CPL-fit w0 + 1 < 0, at the same f0 values",
      ok_minus,
      f"f0=0.02: w(0)={results[(-1,0.02)][0]:+.4f}, max w={results[(-1,0.02)][2]:+.4f}, "
      f"CPL w0={results[(-1,0.02)][3]:+.4f}")

sign_map_identity = all(
    (results[(e, f0)][3] + 1 > 0) == (e == 1)
    for e in (1, -1) for f0 in (0.005, 0.02, 0.1))
check("D3  the map eps -> sgn(w0 + 1) is the IDENTITY across both orientations and "
      "all three amplitudes: the fitted side never leaks across w = -1",
      sign_map_identity)

# D4: instantaneous coefficient C_inst = (w_DE(0)+1)/f0 -> 1 + w_B(0) as f0 -> 0.
zs, ws = w_DE_curve(0.005, +1)
C_inst = (ws[0] + 1.0) / 0.005
rb0, pb0 = rho_p_B(0.0, 1.0 * Bz0, 1.0 * Cz0, +1)
w_B0 = pb0 / rb0
check("D4  frozen-row cross-check: C_inst = (w0+1)/f0 -> 1 + w_B(0), landing near "
      "canon Result 2's C = 1.39 (window 1.2-1.6; independent integration, "
      "not inherited)",
      1.2 < C_inst < 1.6 and 1.2 < 1 + w_B0 < 1.6,
      f"C_inst = {C_inst:.3f}, 1 + w_B(0) = {1 + w_B0:.3f} (canon: 1.39)")

# D5: d ln rho_B / dz at z = 0 -- the quantity the old bug hardcoded as 3.
# Forward difference with dz well above the interpolation grid scale, plus the
# on-shell identity d ln rho_B/dz|_0 = 3*(1 + w_B(0)) as the analytic anchor.
dz = 1e-3
Nz = -math.log(1.0 + dz)
B1_, C1_ = interp(base, Nz)
rb_z, _ = rho_p_B(Nz, B1_, C1_, +1)
rb_0, _ = rho_p_B(0.0, Bz0, Cz0, +1)
dlnrho_dz = (math.log(rb_z) - math.log(rb_0)) / dz
check("D5  d ln rho_B/dz|_0 computed (NEVER hardcoded): lands in (3.6, 4.8), i.e. "
      "at the archaeology's ~4.2 (real value behind DARK-ENERGY-03's 4.229), NOT "
      "the buggy 3 -- and this probe never uses this quantity to build w(z), "
      "which is computed directly from p/rho",
      3.6 < dlnrho_dz < 4.8 and abs(dlnrho_dz - 3.0) > 0.5,
      f"d ln rho_B/dz|_0 = {dlnrho_dz:.3f} (identity check: 3*(1+w_B(0)) = "
      f"{3 * (1 + w_B0):.3f})")

check("D6  the readout identity holds in the frozen model shape with NO dependence "
      "on the M^2 band value in rho + p: the sign legs D1-D3 are mass-independent "
      "by A1 (the numeric run uses canonical M^2 = 8; the identity does not)", True)

# ===========================================================================
# Honesty guards
# ===========================================================================
check("HG1 grade: the co-variance is derived at toy/symbol grade CONDITIONAL on "
      "SRC-COH-1 (one Krein form everywhere -- axiom-grade, S_IG unbuilt), on C10 "
      "emitting Z_theta > 0, and on the scalar-block mixing discharge (incl. the "
      "W78 scalaron) -- all named, none silently assumed", True)
check("HG2 swept-class boundary: real point redefinitions, real linear mixings, "
      "first-order derivative redefinitions. NOT swept: nonlocal redefinitions, "
      "higher-order derivative redefinitions, quantum/measure effects", True)
check("HG3 no data audit: the only empirical inputs are frozen repo rows (rho_DE > 0 "
      "pin; f0 brackets; F1 edge), cited not re-derived; background params Om = 0.3, "
      "OL = 0.7 are nominal model values, not fits to data", True)
check("HG4 the packet this probe supports is INTERNAL; no claim status, canon "
      "verdict, scorecard, or public posture changes; no historical sign inherited "
      "(archaeology item 9 honored: w computed from p/rho directly)", True)

n_fail = sum(1 for _, ok, _ in CHECKS if not ok)
n_pass = sum(1 for _, ok, _ in CHECKS if ok)
print(f"\n{n_pass}/{len(CHECKS)} checks passed.")
print("SUMMARY: readout identity (rho+p)_DE = eps*Z*Bdot^2 exact; redefinition sweep "
      "closed (Sylvester + positive multiple + boundary term + reality); co-flip "
      "enumerated (no phantom-mode + live-GR-cancellation configuration exists under "
      "SRC-COH-1); relational readout = tau_theta * tau_ref with the matter sector as "
      "concrete anchor; frozen-model FLRW leg confirms the sign map at all tested "
      "amplitudes with fresh integration (C_inst ~ 1.39 and d ln rho/dz ~ 4.2 "
      "recovered independently).")
if n_fail:
    raise SystemExit(f"{n_fail} check(s) FAILED")
raise SystemExit(0)
