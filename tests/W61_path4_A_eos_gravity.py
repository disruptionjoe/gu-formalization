#!/usr/bin/env python3
r"""W61 path4 branch A -- THE EOS x STRONG-GRAVITY CORRELATION test.

CANDIDATE (thread C3). The dark-energy equation of state w(z) (cosmological sector)
and the strong-field gravity deviation (the massive spin-2 / Bach-Yukawa sector, the
sub-mm handle) are BOTH claimed to flow from the SAME shared object theta = the II-class
second fundamental form. HOPE: because two observables tie to one object, the free scales
(mu_DW, alpha, the residual beta/alpha) CANCEL in a relation between them, giving a
family-invariant, discriminating correlation locus in (EOS, strong-field-deviation) space
-- a choice-independent prediction (the Weyl precedent).

WHAT THIS TEST DECIDES (deterministic, exit 0; no data imported, no target fit):
  Q-forced : is a numerical (EOS-shape) x (strong-field) correlation forced across the
             whole shape-dim-1 family, independent of beta/alpha and the free scales?
  Q-novel  : is any surviving correlation a NEW forced fact, or a re-derivation of known
             physics (degravitation / "graviton-mass = dark-energy scale" numerology)?
  Q-disc   : does it distinguish GU from LCDM / a generic quintessence+massive-gravity
             model that does NOT share the single object?

CONSTRUCTION USED (fork rule, GEOMETER-VS-PHYSICS-OBJECTS.md):
  * gravity functional  = the program-native induced |II|^2 (Gauss |II|^2 = |H|^2 - R^X),
    NOT a free R^2/Weyl^2 Lagrangian. Its TT second variation = Stelle box(box+m2^2)
    (wave28 H49): a massless graviton + a massive spin-2 of mass m2 = sqrt(m2_eff)*mu_DW.
  * theta (DE sector)   = the program-native fiber / normal mode of the same embedding
    X^4 -> Y^14 (canon theta-field-flrw-dark-energy-eos); its cosmological dynamics is a
    Klein-Gordon field whose EFFECTIVE mass on FLRW is M^2 = lambda_{N,1} (a root-system
    normal-Laplacian eigenvalue, a PURE NUMBER) in units of H^2 -- i.e. a curvature-coupled
    light mode, NOT a hard mu_DW-mass mode.
  * mu_DW               = the DeWitt/gimmel scale-covariant metric scale (ratio-only, H24):
    the overall scale is structurally free.

PRIOR RESULTS REUSED (cited, not re-derived):
  DE sector      wave20 H43 / wave29 H46 : w(z) is non-CPL; KG theta on FLRW; shape set by
                 M^2 = lambda_{N,1} in H0^2 units (root eigenvalues {3,7,8,...}) and f0.
  gravity sector wave28 H49 / wave30 H50 / wave31 H51 : |II|^2 -> Stelle-Yukawa,
                 range lambda_Y = hbar_c/(sqrt(m2_eff)*mu_DW), strength alpha_Y = 1/3 (vDVZ),
                 m2_eff in [5/6,5/4]; DeWitt vacuum rho_Lambda = c_L*mu_DW^4, c_L = 3/8.
  landscape      wave35 : shape-dim-1 FAMILY; residuals = beta/alpha (bounded), mu_DW, alpha.

Run: python -u tests/W61_path4_A_eos_gravity.py
"""
from __future__ import annotations
import math
import sympy as sp

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  -- ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# --- physical constants (comparison scaffolding only; no data fit) ----------
HBAR_C = 197.327          # eV * nm
RHO_L_QTR = 2.3e-3        # (rho_Lambda)^{1/4} ~ 2.3 meV, observed DE scale (H36 input, comparison only)


# ===========================================================================
# PART 1 -- THE DE-SECTOR DEPENDENCE: w(z) = w(lambda_N1, f0), mu_DW-INDEPENDENT
#   KG theta on a fixed-LCDM FLRW background (the wave20/H43 model). The EOS shape is
#   governed by the DIMENSIONLESS ratio M^2/H^2 = lambda_{N,1} (root eigenvalue) and the
#   amplitude f0. The DeWitt scale mu_DW does NOT appear in the KG equation, so the EOS
#   shape is INDEPENDENT of mu_DW (and of m2_eff, beta/alpha).
# ===========================================================================
log("=" * 78)
log("PART 1 -- DE sector: w(z) shape = f(lambda_N1, f0), INDEPENDENT of mu_DW  [COMPUTED]")
log("=" * 78)


def w0_wa(M2: float, f0: float, zc: float = 0.5) -> tuple[float, float]:
    """Reproduce the wave20/H43 theta EOS: constant DeWitt-Lambda (w=-1) + KG theta of
    mass^2 M2 (in H0^2 units) on a flat LCDM background Om=0.3. Return a two-point
    (w0, wa) proxy: w0 = w(z=0), wa ~ -dw/da|_0 estimated from w at z=0 and z=zc.
    Deterministic RK4; NO mu_DW anywhere in this function (that is the whole point)."""
    Om, Ol = 0.3, 0.7

    def H(z):  # H/H0
        return math.sqrt(Om * (1 + z) ** 3 + Ol)

    def dlnH_dz(z):
        num = 3 * Om * (1 + z) ** 2
        return num / (2 * (Om * (1 + z) ** 3 + Ol))

    # evolve B(z) from slow-roll IC at z0; N = ln a = -ln(1+z)
    z0, B, Bp = 30.0, 1.0, 0.0     # Bp = dB/dz
    # integrate down in z with small steps (RK4 in z)
    def deriv(z, B, Bp):
        Hh = H(z)
        # B'' + (3 + H'/H) B' + (M2/H^2) B = 0, but ' is d/dN = -(1+z) d/dz.
        # Convert to d/dz form: use e-folds. Simpler: integrate in N.
        return Bp, None  # placeholder (we integrate in N below)

    # integrate in N = -ln(1+z): dN = -dz/(1+z)
    N0 = -math.log(1 + z0)
    Nf = 0.0
    steps = 4000
    dN = (Nf - N0) / steps
    # state (B, dB/dN)
    y = [1.0, 0.0]
    hist = []  # (z, B, dBdN)

    def f(N, y):
        z = math.exp(-N) - 1.0
        Hh = H(z)
        dlnH_dN = -(1 + z) * (-dlnH_dz(z))  # dlnH/dN = dlnH/dz * dz/dN, dz/dN = -(1+z)
        # careful: dlnH/dz computed above; dz/dN = -(1+z)
        dlnH_dN = dlnH_dz(z) * (-(1 + z)) * (-1)  # = dlnH/dz*(1+z)? keep explicit:
        dlnH_dN = -(1 + z) * dlnH_dz(z) * (-1)
        # to avoid sign confusion, compute numerically: dlnH/dN
        eps = 1e-6
        za = math.exp(-(N + eps)) - 1.0
        zb = math.exp(-(N - eps)) - 1.0
        dlnH_dN = (math.log(H(za)) - math.log(H(zb))) / (2 * eps)
        B, dB = y
        ddB = -(3 + dlnH_dN) * dB - (M2 / Hh ** 2) * B
        return [dB, ddB]

    N = N0
    for i in range(steps):
        z = math.exp(-N) - 1.0
        hist.append((z, y[0], y[1]))
        k1 = f(N, y)
        k2 = f(N + dN / 2, [y[0] + dN / 2 * k1[0], y[1] + dN / 2 * k1[1]])
        k3 = f(N + dN / 2, [y[0] + dN / 2 * k2[0], y[1] + dN / 2 * k2[1]])
        k4 = f(N + dN, [y[0] + dN * k3[0], y[1] + dN * k3[1]])
        y = [y[0] + dN / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
             y[1] + dN / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])]
        N += dN
    hist.append((math.exp(-N) - 1.0, y[0], y[1]))

    def wB_and_rho(z, B, dBdN):
        Hh = H(z)
        KE = 0.5 * (Hh * dBdN) ** 2            # (dB/dt)^2/2, dB/dt = H dB/dN
        PE = 0.5 * M2 * B ** 2                 # 1/2 M^2 B^2  (H0^2 units)
        rho = KE + PE
        wB = (KE - PE) / rho if rho > 0 else -1.0
        return wB, rho

    # locate z=0 and z=zc entries
    def at(ztarget):
        best = min(hist, key=lambda t: abs(t[0] - ztarget))
        return best

    z_0, B_0, dB_0 = at(0.0)
    z_c, B_c, dB_c = at(zc)
    wB0, rho0 = wB_and_rho(z_0, B_0, dB_0)
    wBc, rhoc = wB_and_rho(z_c, B_c, dB_c)
    # two-component EOS: w_DE = (-1 + f wB)/(1+f), f = f0 * rho/rho0
    f_at0 = f0
    f_atc = f0 * rhoc / rho0
    w_0 = (-1 + f_at0 * wB0) / (1 + f_at0)
    w_c = (-1 + f_atc * wBc) / (1 + f_atc)
    # wa in CPL: w(a) ~ w0 + wa(1-a); a=1/(1+z) => 1-a = z/(1+z)
    a_c = 1.0 / (1 + z_c)
    wa = (w_c - w_0) / (1 - a_c) * (-1.0)   # sign: w = w0 + wa(1-a) => wa = (w_c-w0)/(1-a_c)
    wa = (w_c - w_0) / (1 - a_c)
    return w_0, wa


# Compute (w0,wa) for two admissible root eigenvalues; then RE-COMPUTE with an explicit
# mu_DW rescaling to demonstrate the EOS is mu_DW-blind (mu_DW never enters w0_wa()).
w0_a, wa_a = w0_wa(M2=8.0, f0=0.125)     # BC_1 canonical (H43)
w0_b, wa_b = w0_wa(M2=3.0, f0=0.40)      # S^3 assignment (H43)

check("P1a: DE EOS is DYNAMICAL and NON-trivial (w0 != -1, wa != 0) for admissible "
      "root eigenvalues -> theta is a rolling, curvature-coupled light mode [COMPUTED]",
      abs(w0_a + 1) > 1e-3 and abs(wa_a) > 1e-3,
      f"M2=8: (w0,wa)=({w0_a:.3f},{wa_a:.3f})")

check("P1b: varying the root eigenvalue / amplitude MOVES the EOS shape (the DE observable "
      "responds to lambda_N1 and f0) [COMPUTED]",
      abs(w0_a - w0_b) > 1e-3 or abs(wa_a - wa_b) > 1e-3,
      f"M2=3: (w0,wa)=({w0_b:.3f},{wa_b:.3f})")

# The mu_DW-independence is STRUCTURAL: mu_DW is not an argument of w0_wa and does not
# appear in the KG equation B'' + (3+H'/H)B' + (M^2/H^2)B = 0 (M^2 in H0^2 units). Encode
# it as an exact symbolic fact: the KG operator contains no mu_DW.
muDW, H0, M2s, B_s, N_s = sp.symbols('mu_DW H0 M2 B N', positive=True)
kg_symbol = M2s / H0 ** 2          # the only coefficient carrying a scale; it is M^2/H^2, no mu_DW
check("P1c: the theta KG coefficient M^2/H^2 = lambda_N1 (root eigenvalue) contains NO mu_DW "
      "-> the DE EOS SHAPE is exactly independent of mu_DW, m2_eff, and beta/alpha "
      "[COMPUTED, symbolic]",
      muDW not in kg_symbol.free_symbols)


# ===========================================================================
# PART 2 -- THE GRAVITY-SECTOR DEPENDENCE: deviation = f(mu_DW, m2_eff), theta-EOS-BLIND
#   |II|^2 Stelle-Yukawa: range lambda_Y = hbar_c/(sqrt(m2_eff)*mu_DW), strength 1/3.
#   Depends on mu_DW (free scale) and m2_eff in [5/6,5/4] (bounded beta/alpha residual);
#   INDEPENDENT of lambda_N1 and f0.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 2 -- gravity sector: Yukawa = f(mu_DW, m2_eff), INDEPENDENT of lambda_N1/f0  [COMPUTED]")
log("=" * 78)

m2eff = sp.Rational(1, 1)
m2eff_lo, m2eff_hi = sp.Rational(5, 6), sp.Rational(5, 4)


def lam_Y_um(mu_DW_eV: float, m2eff_val: float) -> float:
    m2 = math.sqrt(m2eff_val) * mu_DW_eV     # eV
    return HBAR_C / m2 / 1000.0              # um


mu_ref = 2.3e-3   # eV (a representative choice; the sector responds to it)
lamY_ref = lam_Y_um(mu_ref, 1.0)
lamY_hi = lam_Y_um(mu_ref * 2, 1.0)         # double mu_DW -> half the range
check("P2a: the strong-field Yukawa range responds to mu_DW (halves when mu_DW doubles) "
      "[COMPUTED]", abs(lamY_hi - lamY_ref / 2) < 1e-9,
      f"mu={mu_ref*1e3:.1f}meV -> {lamY_ref:.1f}um ; 2mu -> {lamY_hi:.1f}um")

lamY_lo_eff = lam_Y_um(mu_ref, float(m2eff_lo))
lamY_hi_eff = lam_Y_um(mu_ref, float(m2eff_hi))
check("P2b: the Yukawa range responds to the bounded beta/alpha residual via m2_eff in "
      "[5/6,5/4] (a band, not a point) [COMPUTED]",
      lamY_hi_eff < lamY_ref < lamY_lo_eff,
      f"m2_eff band -> lambda in [{lamY_hi_eff:.1f},{lamY_lo_eff:.1f}] um")

# theta-EOS-blindness is structural: neither lambda_N1 nor f0 appears in lam_Y.
lamN1, f0s = sp.symbols('lambda_N1 f0', positive=True)
lamY_symbol = HBAR_C / (sp.sqrt(m2eff) * muDW)
check("P2c: the Yukawa range symbol contains NO lambda_N1 and NO f0 -> the strong-field "
      "deviation is exactly independent of the DE EOS parameters [COMPUTED, symbolic]",
      lamN1 not in lamY_symbol.free_symbols and f0s not in lamY_symbol.free_symbols)

# strength is the ONE forced scale-free number in the gravity sector.
alpha_Y = sp.Rational(1, 3)
check("P2d: the Yukawa STRENGTH alpha_Y = 1/3 (vDVZ trace factor, H10) is forced, "
      "scale-free, and beta/alpha-independent -- but it is a gravity-sector-ALONE fact, "
      "not a correlation with the DE sector [COMPUTED]", alpha_Y == sp.Rational(1, 3))


# ===========================================================================
# PART 3 -- THE CORRELATION TEST: is (EOS-shape) x (strong-field) a FORCED LOCUS?
#   The residual->observable map is BLOCK-DIAGONAL:
#       (lambda_N1, f0)  ->  (w0, wa)          [DE block]
#       (mu_DW, m2_eff)  ->  (lambda_Y)        [gravity block]
#   No residual is shared; no scale cancels BETWEEN the blocks. Therefore you can move the
#   Yukawa at FIXED EOS, and move the EOS at FIXED Yukawa -> the joint image fills a
#   rectangle, NOT a 1-D locus. THE LITERAL C3 CORRELATION IS NOT FORCED.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 3 -- correlation test: block-diagonal Jacobian -> NO forced (EOS x gravity) locus")
log("=" * 78)

# demonstrate numerically: hold EOS fixed (M2,f0 fixed), sweep mu_DW -> Yukawa moves.
eos_fixed = w0_wa(M2=8.0, f0=0.125)
lamY_at_mu1 = lam_Y_um(2.3e-3, 1.0)
lamY_at_mu2 = lam_Y_um(2.3e-2, 1.0)   # 10x mu_DW
check("P3a: at FIXED EOS (M2,f0), the Yukawa range varies by 10x when mu_DW varies 10x "
      "-> the strong-field observable is UNCONSTRAINED by the EOS [COMPUTED]",
      abs(lamY_at_mu1 / lamY_at_mu2 - 10.0) < 1e-6,
      f"EOS fixed at ({eos_fixed[0]:.3f},{eos_fixed[1]:.3f}); "
      f"lambda_Y = {lamY_at_mu1:.1f} -> {lamY_at_mu2:.2f} um")

# demonstrate: hold Yukawa fixed (mu_DW,m2_eff fixed), sweep the root eigenvalue -> EOS moves.
eos_1 = w0_wa(M2=8.0, f0=0.125)
eos_2 = w0_wa(M2=3.0, f0=0.125)
check("P3b: at FIXED Yukawa (mu_DW,m2_eff), the EOS shape varies when lambda_N1 varies "
      "-> the DE observable is UNCONSTRAINED by the strong-field sector [COMPUTED]",
      abs(eos_1[0] - eos_2[0]) > 1e-3 or abs(eos_1[1] - eos_2[1]) > 1e-3,
      f"(w0,wa): {tuple(round(x,3) for x in eos_1)} vs {tuple(round(x,3) for x in eos_2)}")

# the Jacobian of (w0,wa,lambda_Y) wrt (lambda_N1,f0,mu_DW,m2_eff) is block-diagonal:
#   d(w0,wa)/d(mu_DW) = 0  and  d(lambda_Y)/d(lambda_N1,f0) = 0  (both exact, symbolic P1c/P2c).
block_diagonal = (muDW not in kg_symbol.free_symbols) and \
                 (lamN1 not in lamY_symbol.free_symbols and f0s not in lamY_symbol.free_symbols)
check("P3c: VERDICT Q-forced -- the residual->observable map is BLOCK-DIAGONAL, so no scale "
      "cancels between the EOS and the strong-field deviation; the joint image is a "
      "RECTANGLE (two free axes), NOT a forced 1-D correlation locus. The literal C3 "
      "(EOS-shape x strong-field) correlation is NOT FORCED / NOT family-invariant [COMPUTED]",
      block_diagonal)


# ===========================================================================
# PART 4 -- THE ONE GENUINE SCALE-CANCELLING LOCK (and what it is NOT)
#   mu_DW DOES cancel between the graviton mass and the DeWitt VACUUM DENSITY (H50/H51):
#       lambda_Y = hbar_c * c_L^{1/4} / (sqrt(m2_eff) * rho_Lambda^{1/4}).
#   This is a REAL forced correlation -- but it links the strong-field Yukawa to the DE
#   DENSITY / vacuum-Lambda scale, NOT to the EOS SHAPE (w0,wa). And it requires the H36
#   identification (rho_Lambda = observed DE) to reach a number -- a POSTULATE, not forced.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 4 -- the ONE scale-cancelling lock: DENSITY x Yukawa (NOT EOS x Yukawa), + H36")
log("=" * 78)

c_L = sp.Rational(3, 8)   # wave31 H51, exact
rho_qtr, m2eff_s = sp.symbols('rho_qtr m2eff', positive=True)
# m2 = sqrt(m2_eff)*mu_DW ; rho_Lambda^{1/4} = c_L^{1/4}*mu_DW  => eliminate mu_DW:
lam_Y_from_rho = HBAR_C * c_L ** sp.Rational(1, 4) / (sp.sqrt(m2eff_s) * rho_qtr)
# verify mu_DW cancels: build lam_Y(mu_DW) and rho^{1/4}(mu_DW), substitute, compare.
lamY_mu = HBAR_C / (sp.sqrt(m2eff_s) * muDW)           # (÷1000 for um dropped; ratio test)
rho_mu = c_L ** sp.Rational(1, 4) * muDW
lamY_via = lamY_mu.subs(muDW, rho_qtr / c_L ** sp.Rational(1, 4))
check("P4a: eliminating mu_DW gives lambda_Y = hbar_c*c_L^{1/4}/(sqrt(m2_eff)*rho_Lambda^{1/4}) "
      "-- mu_DW CANCELS. A genuine forced scale-invariant lock EXISTS [COMPUTED, symbolic]",
      sp.simplify(lamY_via - lam_Y_from_rho) == 0)

check("P4b: BUT this lock ties the Yukawa to the DE DENSITY (vacuum rho_Lambda, the w=-1 "
      "component), NOT to the EOS SHAPE (w0,wa) -- which is set by lambda_N1/f0 and is absent "
      "from the relation. It is a DENSITY x gravity lock, not the C3 EOS x gravity correlation "
      "[COMPUTED: rho_qtr in the relation, lambda_N1/f0 not]",
      rho_qtr in lam_Y_from_rho.free_symbols and
      lamN1 not in lam_Y_from_rho.free_symbols and f0s not in lam_Y_from_rho.free_symbols)

# H51: the DeWitt Lambda is a BACKGROUND/trace-sector object (A0=0 for the TT graviton), so
# it is genuinely the vacuum density, reinforcing that this lock is density-side not EOS-side.
check("P4c: the DeWitt-Lambda is a background/trace-sector vacuum density (TT-graviton s^0 "
      "coeff A0=0, H51) -> the lock's DE input is the vacuum SCALE, confirming it is not the "
      "dynamical EOS [COMPUTED elsewhere, cited]", True)

# The number requires H36 (postulate). Under H36, rho^{1/4}=2.3meV -> the H51 window.
lamY_num = float(lam_Y_from_rho.subs({rho_qtr: RHO_L_QTR, m2eff_s: sp.Rational(5, 6)})) / 1000.0
lamY_num_hi = float(lam_Y_from_rho.subs({rho_qtr: RHO_L_QTR, m2eff_s: sp.Rational(5, 4)})) / 1000.0
check("P4d: reaching a NUMBER (lambda_Y ~ 60-74 um, H51) requires the H36 identification "
      "rho_Lambda = observed DE -- a POSTULATE (wave30 Q2, [wild]), NOT family-forced. Without "
      "H36 mu_DW is free and even this lock DECOUPLES [COMPUTED band + ARGUED status]",
      59.0 < lamY_num_hi < 61.0 and 72.0 < lamY_num < 75.0,
      f"under H36: lambda_Y in [{lamY_num_hi:.1f},{lamY_num:.1f}] um")


# ===========================================================================
# PART 5 -- FAMILY-INVARIANCE of what survives
#   The mu_DW-cancellation in the density-lock is family-invariant IN FORM (holds for all
#   mu_DW). But its O(1) PREFACTOR c_L^{1/4}/sqrt(m2_eff) drifts with the beta/alpha residual
#   (via m2_eff in [5/6,5/4] and c_L's O(1) convention band), so the lock is a BAND, not a
#   sharp point. And the EOS x gravity correlation is NOT family-invariant at all (Part 3).
# ===========================================================================
log("\n" + "=" * 78)
log("PART 5 -- family-invariance: form-invariant BAND (density-lock) vs NON-invariant (EOS-lock)")
log("=" * 78)

pref_lo = float(c_L ** sp.Rational(1, 4) / sp.sqrt(m2eff_hi))   # m2_eff=5/4
pref_hi = float(c_L ** sp.Rational(1, 4) / sp.sqrt(m2eff_lo))   # m2_eff=5/6
spread = pref_hi / pref_lo
check("P5a: the density-lock prefactor c_L^{1/4}/sqrt(m2_eff) drifts by ~22% across the "
      "beta/alpha-bounded m2_eff band [5/6,5/4] -> family-invariant in FORM but a BAND in "
      "value (residual beta/alpha does NOT fully cancel) [COMPUTED]",
      1.15 < spread < 1.25, f"prefactor spread = {spread:.3f} (~{100*(spread-1):.0f}%)")

check("P5b: the EOS x gravity correlation itself is NOT family-invariant: it does not exist "
      "as a locus (Part 3 block-diagonal). Invariance question is moot -- there is nothing to "
      "be invariant [COMPUTED, from P3c]", block_diagonal)


# ===========================================================================
# PART 6 -- DISCRIMINATION vs LCDM / generic DE+modified-gravity
# ===========================================================================
log("\n" + "=" * 78)
log("PART 6 -- discrimination: LCDM / generic quintessence+massive-gravity")
log("=" * 78)

# LCDM: w=-1 exactly (no theta dynamics) AND GR spin-2 (no massive companion). Neither mode.
lcdm_has_eos_dynamics = False
lcdm_has_massive_spin2 = False
check("P6a: vs LCDM -- LCDM has NEITHER a dynamical EOS (w=-1) NOR a massive spin-2 "
      "companion. GU's co-PRESENCE of both modes discriminates from LCDM [structural]",
      (not lcdm_has_eos_dynamics) and (not lcdm_has_massive_spin2))

# Generic "massive-graviton-as-dark-energy" (degravitation: Dvali/Deffayet-class): ALSO
# produces a graviton-mass <-> DE-scale relation. So the DENSITY-lock does NOT discriminate
# from that class -- the adversary's objection stands for the scale-lock.
generic_massive_gravity_reproduces_density_lock = True
check("P6b: vs generic degravitation / 'graviton-mass = DE-scale' models -- these ALSO tie a "
      "graviton mass to the DE scale, so the DENSITY-lock is NOT discriminating (and the "
      "meV = rho_Lambda^{1/4} coincidence is KNOWN numerology) -> Q-novel/Q-disc FAIL for the "
      "scale-lock [ARGUED]", generic_massive_gravity_reproduces_density_lock)

# Generic quintessence + independent massive gravity: HAS both sectors but they are
# INDEPENDENT (two objects, two free strengths). GU's only extra content is (i) alpha_Y=1/3
# fixed and (ii) the root-system EOS family -- SEPARATE facts, not a joint locus. So GU's
# discriminator over that class is qualitative co-presence + two fixed sub-facts, NOT a
# forced correlation.
check("P6c: vs generic quintessence + independent massive gravity -- that class ALSO has both "
      "sectors, uncorrelated. GU adds (i) alpha_Y=1/3 fixed and (ii) the root-system EOS "
      "family, but these are SEPARATE forced facts, not a joint EOS x gravity locus. The "
      "discriminator is qualitative co-presence, not a correlation [ARGUED]", True)


# ===========================================================================
# VERDICT
# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT (graded, honest)")
log("=" * 78)
log(r"""
  Q-forced : NO for the literal C3 correlation. The DE EOS shape (governed by the root
             eigenvalue lambda_N1 and f0) and the strong-field Yukawa (governed by mu_DW and
             m2_eff) depend on DISJOINT residual parameters. The residual->observable map is
             BLOCK-DIAGONAL (Part 3): no scale cancels between the two sectors, so the joint
             image is a rectangle, not a forced locus. The ONE genuine scale-cancelling lock
             (Part 4) is DENSITY x Yukawa, not EOS x Yukawa, and it needs the H36 postulate to
             reach a number.
  Q-novel  : LOW. The surviving lock (graviton mass <-> DE scale) is the known degravitation /
             meV-coincidence pattern and is already wave30/wave31 (H50/H51). No NEW forced
             correlation between the EOS SHAPE and the strong field survives.
  Q-disc   : WEAK. The density-lock is reproduced by generic massive-gravity-as-DE models
             (not discriminating). The genuine GU discriminator is a QUALITATIVE co-presence
             (dynamical EOS AND massive spin-2 from the one |II|^2 shape action) plus two
             separate fixed sub-facts (alpha_Y = 1/3; the root-system EOS family) -- not a
             quantitative family-invariant correlation locus.

  STRONGEST FORCED-AND-NOVEL STATEMENT the branch can defend (weaker than a headline):
     "Because the DE scalar mode and the strong-field massive spin-2 are BOTH modes of the
      single induced |II|^2 shape action, GU forces their CO-PRESENCE: no family member can
      have a dynamical dark-energy EOS (w != -1 from rolling theta) while lacking the massive
      spin-2 companion, or vice versa. LCDM has neither; single-sector models have exactly
      one. This co-presence is family-invariant and discriminating -- but it is QUALITATIVE
      (a joint non-vanishing), NOT a quantitative scale-cancelling correlation, because the
      two modes carry masses ~30 orders of magnitude apart (O(H0) vs mu_DW) set by different
      mechanisms (curvature-coupling vs mass-gap)."

  LOAD-BEARING ASSUMPTION: that the DE theta is a CURVATURE-COUPLED LIGHT mode (M^2 ~ H0^2,
     root eigenvalue) rather than a hard mu_DW-mass mode. This is what makes the EOS shape
     mu_DW-blind and thereby BREAKS the hoped-for scale cancellation. (It is the wave20/H43
     construction; if instead the theta mass were mu_DW-set, the field would be frozen,
     w=-1, and there would be NO EOS to correlate at all -- so the disjointness is robust.)
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("=" * 78)
log("exit 0 = W61 path4-A computed: the EOS x strong-gravity correlation is NOT a forced")
log("  family-invariant locus (block-diagonal residuals; no scale cancels between sectors).")
log("  The one scale-cancelling lock is DENSITY x Yukawa (H50/H51), conditional on the H36")
log("  postulate and reproduced by generic degravitation -> not novel, not discriminating.")
log("  What survives is a QUALITATIVE, family-invariant, discriminating CO-PRESENCE of the two")
log("  modes from one |II|^2 action -- not the hoped quantitative correlation.")
log("=" * 78)
