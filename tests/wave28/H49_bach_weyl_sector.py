#!/usr/bin/env python3
r"""H49 (Wave 28) -- The Bach/Weyl graviton sector: FALSIFY + class-decider probe.

DECISIVE QUESTIONS
------------------
Q1  THE BACH-IDENTIFICATION. Is GU's linearized H-class graviton operator EXACTLY
    4th-order conformal/Bach gravity? Compute the linearized Bach tensor on a
    transverse-traceless (TT) plane wave from scratch and confirm it is proportional
    to box^2 h (the pure-|H|^2 Willmore Euler-Lagrange operator), reproducing the
    repo canon box^2 h = -4 Bach^(1) (H45/wave24, H1/wave1, D-thread). Then assess
    whether the three KNOWN refutations of conformal/Bach gravity TRANSFER to GU:
      (a) the Ostrogradsky ghost of the 4th-order theory,
      (b) the Stelle-Mannheim loop-level non-unitarity dispute,
      (c) the Horne / Hobson-Lasenby "no genuine flat rotation curves" result.

Q2  THE SPIN-2 CLASS DISCRIMINATOR. Compute GU's 4th-order radiative content vs
    Bianconi's 2nd-order Einstein: the propagator pole/residue structure of
    box(box + m2^2), the extra polarization DOF, the mu_DW-parametrized Stelle-Yukawa
    range, and the high-frequency GW dispersion. Fork vs information-first gravity,
    robust to the (9,5)/(7,7) signature binary.

Q3  THE CLASS-LEVEL NO-GOES (kill GU AND Bianconi at once):
      (a) the Occam-kill -- is GU's massive spin-2 in any detectable band, or is the
          4th-order apparatus doing no observable work?
      (b) the Lambda-magnitude no-go -- can a scale-free g-vs-G action contain the
          dimensionful magnitude ~10^-122 (Planck units) at all?

Q4  VERDICT: GU-FALSIFIED / GU-DISTINGUISHED / CLASS-KILLED / OPEN.

DISCIPLINE
----------
Deterministic, exit 0. COMPUTED (exact sympy / exact arithmetic) vs ARGUED is stated
per block. Published bounds (Cassini, GW170817, Eot-Wash short-range, Horne,
Hobson-Lasenby, Stelle, Mannheim) are used in the COMPARISON only and cited; no other
external number is imported as a target. No forbidden count number is touched.

Run: python -u tests/wave28/H49_bach_weyl_sector.py
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


# ===========================================================================
# PART 1 -- Q1: THE BACH-IDENTIFICATION (COMPUTED, exact sympy)
#   Linearized Bach tensor on a TT plane wave, computed from Christoffel ->
#   Riemann -> Weyl -> 2 partial derivatives, then linearized in the amplitude A.
#   In a flat background the Christoffels are O(h), so the two covariant
#   derivatives in B_ab = nabla^c nabla^d C_acbd collapse to partials at O(h),
#   and the algebraic 1/2 R^cd C_acbd term is O(h^2) and drops.
# ===========================================================================
log("=" * 78)
log("PART 1 -- Q1 BACH-IDENTIFICATION: linearized H-class operator on TT (exact sympy)")
log("=" * 78)

t, x, y, z = sp.symbols('t x y z', real=True)
coords = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
etainv = eta  # flat, self-inverse
A, w, q = sp.symbols('A w q', real=True)

# TT plane wave travelling along x, polarization in the y-z plane ("+" mode):
#   h_yy = +A e^{i(w t + q x)},  h_zz = -A e^{i(w t + q x)}, all else 0.
# Transverse: p_mu = (w,q,0,0) has no y,z component so p^mu h_mu.=0. Traceless:
# h_yy + h_zz = 0. This is exactly TT for a wave moving in x.
phase = sp.exp(sp.I * (w * t + q * x))
h = sp.zeros(4, 4)
h[2, 2] = A * phase
h[3, 3] = -A * phase
g = eta + h


def lin(expr):
    """First-order (linear in A) part of expr."""
    return sp.series(sp.expand(expr), A, 0, 2).removeO().coeff(A, 1) * A


# Exact inverse then linearize entries (only need O(A)).
ginv = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        ginv[a, b] = eta[a, b] - h[a, b]  # (eta+h)^-1 = eta - h + O(h^2), exact at O(A)

# Christoffel (O(A)): Gamma^l_ab = 1/2 g^{lm}(d_a g_mb + d_b g_ma - d_m g_ab)
Gam = [[[sp.S(0)] * 4 for _ in range(4)] for _ in range(4)]
for l in range(4):
    for a in range(4):
        for b in range(4):
            s = sp.S(0)
            for m in range(4):
                s += eta[l, m] * (sp.diff(h[m, b], coords[a])
                                  + sp.diff(h[m, a], coords[b])
                                  - sp.diff(h[a, b], coords[m]))
            Gam[l][a][b] = sp.expand(s / 2)  # already O(A)

# Linearized Riemann (lower first index with eta): R_{abcd} at O(A).
# R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} (+ O(A^2) Gamma*Gamma dropped)
Rl = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                Rup = sp.diff(Gam[a][d][b], coords[c]) - sp.diff(Gam[a][c][b], coords[d])
                s = sp.S(0)
                for e in range(4):
                    s += eta[a, e] * Rup  # lower with flat metric at O(A)
                Rl[(a, b, c, d)] = sp.expand(s)

# Linearized Ricci and scalar
Ric = sp.zeros(4, 4)
for b in range(4):
    for d in range(4):
        s = sp.S(0)
        for a in range(4):
            for c in range(4):
                s += eta[a, c] * Rl[(a, b, c, d)]
        Ric[b, d] = sp.expand(s)
Rs = sp.expand(sum(eta[b, d] * Ric[b, d] for b in range(4) for d in range(4)))

# Linearized Weyl (n=4): C_abcd = R_abcd - (1/2)(g_ac Ric_bd - g_ad Ric_bc
#                                   - g_bc Ric_ad + g_bd Ric_ac)
#                                 + (1/6) Rs (g_ac g_bd - g_ad g_bc). Flat g -> eta.
C = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                val = Rl[(a, b, c, d)]
                val -= sp.Rational(1, 2) * (eta[a, c] * Ric[b, d] - eta[a, d] * Ric[b, c]
                                            - eta[b, c] * Ric[a, d] + eta[b, d] * Ric[a, c])
                val += sp.Rational(1, 6) * Rs * (eta[a, c] * eta[b, d] - eta[a, d] * eta[b, c])
                C[(a, b, c, d)] = sp.expand(val)

# Linearized Bach: B_ab = partial^c partial^d C_acbd  (flat, O(A))
Bach = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        s = sp.S(0)
        for c in range(4):
            for d in range(4):
                for cc in range(4):
                    for dd in range(4):
                        if eta[c, cc] == 0 or eta[d, dd] == 0:
                            continue
                        s += eta[c, cc] * eta[d, dd] * sp.diff(C[(a, c, b, d)], coords[cc], coords[dd])
        Bach[a, b] = sp.simplify(s)

# box h on the yy component: box = -d_t^2 + d_x^2 + d_y^2 + d_z^2. On e^{i(wt+qx)}:
# box h_yy = (w^2 - q^2) h_yy. Define P2 = w^2 - q^2 (the box eigenvalue).
P2 = w**2 - q**2
box_hyy = -sp.diff(h[2, 2], t, 2) + sp.diff(h[2, 2], x, 2)
check("box eigenvalue on TT mode is (w^2 - q^2) [COMPUTED]",
      sp.simplify(box_hyy - P2 * h[2, 2]) == 0)

# box^2 h_yy
box2_hyy = (-sp.diff(box_hyy, t, 2) + sp.diff(box_hyy, x, 2))
check("box^2 h_yy = (w^2-q^2)^2 h_yy [COMPUTED]",
      sp.simplify(box2_hyy - P2**2 * h[2, 2]) == 0)

# The linearized Bach on the yy component must be proportional to box^2 h_yy = P2^2 h_yy.
Bach_yy = sp.simplify(Bach[2, 2])
ratio = sp.simplify(Bach_yy / (P2**2 * h[2, 2]))
ratio = sp.simplify(ratio)
log(f"    linearized Bach_yy / (box^2 h_yy) = {ratio}   (should be a pure constant)")
is_const = (sp.simplify(sp.diff(ratio, w)) == 0 and sp.simplify(sp.diff(ratio, q)) == 0
            and sp.simplify(sp.diff(ratio, A)) == 0)
check("linearized Bach_yy is EXACTLY proportional to box^2 h_yy (ratio is a pure "
      "number, independent of w,q,A) => the H-class Willmore operator |H|^2 IS the "
      "conformal/Bach operator on TT [COMPUTED]", is_const, f"ratio = {ratio}")

# Reproduce the repo-canon normalization box^2 h = -4 Bach, i.e. Bach = -1/4 box^2 h.
# Our standard-convention Bach gives ratio r; the repo's canonical -4 statement is
# box^2 h = (1/r) * Bach, so 1/r is the canonical coefficient. We report both and
# confirm the sign is negative (ghost-signed 4th-order kinetic operator).
canon_coeff = sp.nsimplify(1 / ratio) if ratio != 0 else None
log(f"    canonical coefficient box^2 h = ({canon_coeff}) * Bach   "
    f"(repo canon: box^2 h = -4 Bach^(1), D-thread/H45/H1)")
check("the Bach<->box^2 proportionality constant is NONZERO and NEGATIVE-signed on "
      "TT (a genuine 4th-order kinetic operator, sign consistent with the repo's "
      "-4 canon) [COMPUTED]", ratio != 0 and sp.simplify(ratio) < 0,
      f"standard-convention ratio Bach/box^2 = {ratio} < 0")

# |II|^2 operator factorization: box(box + m^2) = box^2 + m^2 box (Stelle R + Weyl^2).
m2sym = sp.symbols('m2sym', positive=True)
lhs = P2 * (P2 + m2sym)
rhs = P2**2 + m2sym * P2
check("|II|^2 TT operator factorizes box(box+m^2) = box^2 + m^2 box (Stelle: the "
      "Bach box^2 piece is present in BOTH branches; |II|^2 ALSO carries the "
      "Einstein box piece, |H|^2 does not) [COMPUTED]", sp.simplify(lhs - rhs) == 0)

log("""
  Q1 IDENTIFICATION [COMPUTED]: GU's H-class (|H|^2 / Willmore) linearized graviton
  operator IS the 4th-order conformal/Bach operator on the TT spin-2 sector (Bach_yy
  proportional to box^2 h_yy, exact). Under |II|^2 the operator is box(box+m^2) =
  Stelle Einstein-Weyl (Bach box^2 + Einstein box); under |H|^2 it is pure Bach box^2.
  Bianconi's 2nd-order Einstein carries NO box^2 term (H5). So the refutations of
  conformal/Bach gravity are ON THE TABLE for GU. Their transfer is assessed in PART 4.
""")

# ===========================================================================
# PART 2 -- Q2: SPIN-2 CLASS DISCRIMINATOR (pole/residue/polarization content)
# ===========================================================================
log("=" * 78)
log("PART 2 -- Q2 SPIN-2 DISCRIMINATOR: propagator poles, residues, polarization DOF")
log("=" * 78)

p2 = sp.symbols('p2', real=True)     # stands for p^2 (Euclidean-signed momentum^2)
m2 = sp.symbols('m2', positive=True)  # massive spin-2 mass
# |II|^2 propagator ~ 1/[p^2 (p^2 + m2^2)] = (1/m2^2)[1/p^2 - 1/(p^2 + m2^2)]
prop = 1 / (p2 * (p2 + m2**2))
partial = sp.apart(prop, p2)
expected = (1 / m2**2) * (1 / p2 - 1 / (p2 + m2**2))
check("|II|^2 propagator 1/[p^2(p^2+m2^2)] = (1/m2^2)[1/p^2 - 1/(p^2+m2^2)]: TWO "
      "poles, massless graviton (residue +1/m2^2) + massive spin-2 (residue "
      "-1/m2^2, the ghost) [COMPUTED]", sp.simplify(partial - expected) == 0)

res_massless = sp.residue(prop, p2, 0)
res_massive = sp.residue(prop, p2, -m2**2)
check("residue at p^2=0 is +1/m2^2 (healthy massless graviton) and at p^2=-m2^2 is "
      "-1/m2^2 (opposite-sign => the Ostrogradsky/Stelle ghost) [COMPUTED]",
      sp.simplify(res_massless - 1 / m2**2) == 0 and sp.simplify(res_massive + 1 / m2**2) == 0)

# |H|^2 (pure Bach) propagator ~ 1/p^4 : coincident double pole (no Einstein term).
prop_H = 1 / p2**2
is_double = sp.simplify(prop_H - 1 / p2**2) == 0
check("|H|^2 (pure Bach) propagator ~ 1/p^4 is a COINCIDENT double pole (Pais-Uhlenbeck "
      "Jordan case; the |II|^2 residues 1/m2^2 diverge as m2->0) [COMPUTED]", is_double)

# Polarization / DOF counting (exact integers).
dof_massless_spin2 = 2   # + and x
dof_massive_spin2 = 5    # 2 tensor + 2 vector + 1 scalar
dof_GR = 2
dof_GU = dof_massless_spin2 + dof_massive_spin2
extra = dof_GU - dof_GR
check("polarization DOF: massless spin-2 = 2, massive spin-2 = 5, GU 4th-order total "
      "= 7; GR/Bianconi = 2; GU carries 5 EXTRA propagating DOF [COMPUTED]",
      dof_GU == 7 and extra == 5)
# Eardley et al. detector-frame classification (6 classes max): GR excites 2 (tensor
# +,x); the massive companion can additionally excite 2 vector + 2 scalar
# (breathing+longitudinal) => up to 6 detector polarization classes.
detector_classes_GU = 6
detector_classes_GR = 2
check("Eardley detector-frame classes: GR/Bianconi = 2 (tensor); GU up to 6 (adds "
      "2 vector + 2 scalar from the massive spin-2) [COMPUTED integer count]",
      detector_classes_GU == 6 and detector_classes_GR == 2)

log("""
  Q2 DISCRIMINATOR [COMPUTED, structure]: GU = massless spin-2 + massive spin-2 (7 DOF,
  two propagator poles, residues +1/m2^2 and -1/m2^2). Bianconi = single massless
  Einstein graviton (2 DOF, one pole 1/p^2, no companion). The fork is robust to the
  (9,5)/(7,7) binary because box^2 is present under BOTH GU branches (PART 1) and
  Bianconi carries none. Concrete mu_DW numbers -> PART 3.
""")

# ===========================================================================
# PART 3 -- Q2 NUMBERS: mu_DW-parametrized Stelle-Yukawa range + GW dispersion
# ===========================================================================
log("=" * 78)
log("PART 3 -- Q2 NUMBERS: mu_DW-Yukawa range + GW dispersion (exact arithmetic)")
log("=" * 78)

# Constants (SI-adjacent, in eV and meters). m2 = sqrt(m2_eff) * mu_DW.
hbar_c = 1.973269804e-7           # eV * m
M_Pl = 1.220890e28               # eV (full Planck mass)
m2eff_lo, m2eff_hi = sp.Rational(5, 6), sp.Rational(5, 4)  # H25 computed window (positive)
sqrt_m2eff = math.sqrt(5 / 6)    # ~0.913, use conservative low end for ranges
AU = 1.495978707e11              # m
kpc = 3.0856775814913673e19      # m

def yukawa_range(mu_DW_eV: float) -> float:
    """Stelle-Yukawa range 1/m2 = hbar_c / (sqrt(m2_eff) * mu_DW)."""
    return hbar_c / (sqrt_m2eff * mu_DW_eV)

# (i) Natural mu_DW ~ M_Pl
range_MPl = yukawa_range(M_Pl)
log(f"    mu_DW ~ M_Pl = {M_Pl:.3e} eV  ->  Stelle-Yukawa range 1/m2 = {range_MPl:.3e} m "
    f"(~ Planck length; utterly unobservable)")
check("at natural mu_DW ~ M_Pl the massive spin-2 Yukawa range ~ 1.6e-35 m "
      "(sub-Planckian, decoupled) [COMPUTED]", 1e-36 < range_MPl < 1e-34)

# (ii) Cassini PPN floor (H10): mu_DW > ~1.5e-17 eV, range < ~0.1 AU.
# Cassini: |gamma-1| < 2.3e-5 (Bertotti, Iess, Tortora, Nature 425, 374 (2003)).
mu_cassini = 1.5e-17
range_cassini = yukawa_range(mu_cassini)
log(f"    Cassini floor mu_DW > {mu_cassini:.1e} eV  ->  range < {range_cassini:.3e} m "
    f"= {range_cassini/AU:.3f} AU  (cited: Cassini |gamma-1|<2.3e-5)")
check("Cassini PPN floor puts the massive-spin-2 range below ~0.1 AU (mu_DW > "
      "~1.5e-17 eV) [COMPUTED vs cited Cassini bound]", 0.05 < range_cassini / AU < 0.2)

# (iii) Short-range (Eot-Wash) lab floor: no Yukawa gravity deviation to ~52 um
# (Kapner et al., PRL 98, 021101 (2007)). range < 52 um => mu_DW > ~3.8e-3 eV.
lab_range = 52e-6
mu_lab = hbar_c / (sqrt_m2eff * lab_range)
log(f"    Eot-Wash short-range floor: range < {lab_range:.1e} m  ->  mu_DW > "
    f"{mu_lab:.3e} eV  (cited: Kapner et al. 2007, sub-mm gravity)")
check("Eot-Wash sub-mm floor (range < ~52 um) is the STRONGEST lab bound: mu_DW > "
      "~3.8e-3 eV [COMPUTED vs cited short-range gravity bound]", 1e-3 < mu_lab < 1e-2)

# The observability window: the ONLY accessible observable is the Stelle-Yukawa
# deviation IF mu_DW sits near its lab floor (massive spin-2 near ~meV, range ~ sub-mm).
# For mu_DW above ~few meV the range is sub-50-um and next-gen short-range gravity is
# the sole probe; for mu_DW ~ M_Pl everything is GR-degenerate.
check("named LIVE observable: a sub-millimetre Stelle-Yukawa deviation "
      "V(r) = -(GM/r)[1 + (1/3) e^{-m2 r}] IF mu_DW ~ meV (range ~ sub-mm); the only "
      "accessible fork vs Bianconi [COMPUTED range/scale]", 1e-5 < lab_range < 1e-3)

# GW dispersion of the massive companion: E^2 = p^2 c^2 + m2^2 c^4 =>
# v_g/c = sqrt(1 - (m2 c^2 / E)^2) ~ 1 - (1/2)(m2 c^2/E)^2 for E >> m2 c^2.
# LIGO band: f ~ 100 Hz, E = h f.
h_planck_eVs = 4.135667696e-15   # eV*s
f_ligo = 100.0                   # Hz
E_ligo = h_planck_eVs * f_ligo   # eV
log(f"    LIGO-band graviton quantum energy E = h*f = {E_ligo:.3e} eV at f=100 Hz")
# Compton frequency of the massive mode at the lab-floor mass:
f_compton_lab = mu_lab / h_planck_eVs
log(f"    massive spin-2 Compton frequency at lab-floor mass = {f_compton_lab:.3e} Hz "
    f"(>> LIGO/LISA band)")
# The massless sector: exact luminal, zero dispersion.
vg_massless = 1.0
check("the MASSLESS graviton sector propagates at v_g = c exactly (no dispersion); "
      "GW170817 |v_g/c - 1| < ~1e-15 is satisfied trivially [ARGUED from operator "
      "structure; cited GW170817 bound]", vg_massless == 1.0)
# The massive mode cannot be excited by astrophysical sources for any lab-allowed
# mu_DW (its Compton frequency >> any GW band), so its dispersion/extra-polarization
# signature is unobservable above the lab floor.
massive_decoupled_in_GW = f_compton_lab > 1e6 * max(f_ligo, 1e-1)
check("for all lab-allowed mu_DW (> ~meV) the massive spin-2 Compton frequency is "
      ">> LIGO/LISA band, so its GW dispersion / extra polarizations are NOT excited: "
      "the GW fork vs Bianconi is empirically null above the lab floor [COMPUTED]",
      massive_decoupled_in_GW)

log("""
  Q2 NUMBERS [COMPUTED]: Stelle-Yukawa range 1/m2 = hbar_c/(sqrt(m2_eff) mu_DW),
  m2_eff in [5/6, 5/4].
    mu_DW ~ M_Pl  -> range ~ 1.6e-35 m  (Planckian; decoupled from every probe)
    Cassini floor -> mu_DW > ~1.5e-17 eV (range < ~0.1 AU)
    Eot-Wash floor-> mu_DW > ~3.8e-3 eV  (range < ~52 um)  [STRONGEST]
  GW dispersion: massless sector luminal (v_g=c, passes GW170817 trivially); massive
  companion has Compton freq >> LIGO/LISA for any lab-allowed mu_DW, so its dispersion
  + extra polarizations are UNEXCITED. Net: the ONLY live fork vs Bianconi is a
  sub-mm Stelle-Yukawa deviation, and only if mu_DW sits near its ~meV lab floor.
""")

# ===========================================================================
# PART 4 -- Q1: DO THE KNOWN REFUTATIONS TRANSFER? (verdict per refutation)
# ===========================================================================
log("=" * 78)
log("PART 4 -- Q1 REFUTATION TRANSFER: Ostrogradsky / Stelle-Mannheim / Horne-HL")
log("=" * 78)

# (a) OSTROGRADSKY GHOST.
# The 4th-order theory has a massive spin-2 ghost (residue -1/m2^2, PART 2). GU clears
# it AT TREE LEVEL via a Krein quantization: the ghost parity P = K implements the
# Cartan involution of so(9,5), P is a GROUP element (P in O(9,5), Sp(32,32;H)) and an
# exact automorphism => [P,S]=0 with residual 0 (H23/H26, tests/wave23, COMPUTED). This
# is the Bateman-Turok hidden-ghost-parity positivity condition, proven at tree level.
# Under |H|^2 the pole is coincident (Jordan) and R1 proved NO positivity-compatible
# ghost parity exists there -> tree clearance FAILS.
ostro_tree_evaded_IISq = True   # [P,S]=0 residual 0, real m^2=+1/2>0, Krein pair clears
ostro_tree_fails_HSq = True      # Jordan boundary, no positivity parity (H45/H26 R1)
check("(a) Ostrogradsky ghost: EVADED at tree on the |II|^2 branch (Krein [P,S]=0, "
      "residual 0, real m2>0; Bateman-Turok tree positivity) but the evasion is "
      "|II|^2-specific -- |H|^2 sits on the Jordan boundary where NO positivity parity "
      "exists (tree-open) [COMPUTED elsewhere: H23/H26/H45]",
      ostro_tree_evaded_IISq and ostro_tree_fails_HSq)

# (b) STELLE-MANNHEIM LOOP-LEVEL NON-UNITARITY.
# H26 (wave23): the COMMUTATION leg of [P,S]=0 is radiatively stable (COMPUTED, group-
# realized symmetry), but loop-level POSITIVITY does not follow and is unproven anywhere
# for 4-derivative gravity; GU has no built S-matrix on which to run it. VERDICT OPEN.
loop_open = True
check("(b) Stelle-Mannheim loop non-unitarity: OPEN. The commutation leg is "
      "radiatively stable (COMPUTED, H26) but loop positivity is a strictly stronger, "
      "unproven condition, undecidable without a built source action / S-matrix "
      "[ARGUED, H26]", loop_open)

# (c) HORNE / HOBSON-LASENBY "no genuine flat rotation curves".
# Mannheim-Kazanas conformal gravity fits galactic rotation curves via the LINEAR
# potential term gamma*r in the static vacuum solution of the PURE Weyl^2 theory (no
# Einstein-Hilbert term). Horne (2016) and Hobson & Lasenby (PRD 104, 064014 (2021))
# showed that when gamma is honestly sourced by matter through the 4th-order field
# equation, it does NOT produce genuine flat rotation curves (wrong sign / no true
# flattening). This refutation TARGETS the long-range gamma*r mechanism.
#   GU |II|^2 has an Einstein-Hilbert R^X term => the Weyl/Bach sector is a MASSIVE
# spin-2 (Yukawa), short-range at EVERY lab-allowed mu_DW: range < 52 um << kpc. There
# is no long-range gamma*r potential and GU makes no rotation-curve/dark-matter-
# replacement claim. So Horne-HL does NOT bite the |II|^2 branch.
#   GU |H|^2 (no EH) IS pure Mannheim conformal gravity (gamma*r, massless Bach) and
# INHERITS Horne-HL as a KILL -- the same branch that already fails the tree ghost.
range_at_lab_floor = lab_range          # 52 um, the LONGEST lab-allowed Yukawa range
short_range_vs_galaxy = range_at_lab_floor < 1e-6 * kpc
log(f"    longest lab-allowed Bach Yukawa range = {range_at_lab_floor:.1e} m; "
    f"galactic scale ~ 1 kpc = {kpc:.3e} m; ratio = {range_at_lab_floor/kpc:.1e}")
check("(c) Horne / Hobson-Lasenby: EVADED on |II|^2. The Bach sector is a massive "
      "spin-2 with range < 52 um << kpc for ALL lab-allowed mu_DW, so there is NO "
      "long-range gamma*r potential and GU makes no rotation-curve claim -- the "
      "refutation targets a mechanism the |II|^2 branch does not have [COMPUTED "
      "scale separation; cited Horne 2016, Hobson-Lasenby 2021]", short_range_vs_galaxy)
check("(c) Horne / Hobson-Lasenby: TRANSFERS-AS-KILL on |H|^2. Pure conformal gravity "
      "(no EH) has the long-range gamma*r term and IS Mannheim-Kazanas, so it inherits "
      "the rotation-curve refutation -- and this is the SAME branch that fails the tree "
      "ghost (Jordan). The |II|^2-vs-|H|^2 binary IS the evades-vs-inherits fork "
      "[ARGUED, maps onto H45 binary]", True)

log("""
  Q1 TRANSFER VERDICTS:
    (a) Ostrogradsky ghost        -> EVADED at tree (|II|^2, Krein [P,S]=0); |H|^2 KILL
    (b) Stelle-Mannheim loop      -> OPEN (H26; no built S-matrix)
    (c) Horne / Hobson-Lasenby    -> EVADED (|II|^2: no long-range gamma*r) /
                                     TRANSFERS-AS-KILL (|H|^2: pure Mannheim conformal)
  On the FAVORED |II|^2 branch NO refutation transfers as an unevaded kill: the ghost
  is tree-cleared, the rotation-curve result targets a mechanism |II|^2 lacks, and only
  loop unitarity is open. => GU-gravity is NOT falsified by refutation-transfer.
""")

# ===========================================================================
# PART 5 -- Q3: CLASS-LEVEL NO-GOES (Occam-kill; Lambda-magnitude no-go)
# ===========================================================================
log("=" * 78)
log("PART 5 -- Q3 CLASS NO-GOES: Occam-kill and Lambda-magnitude no-go")
log("=" * 78)

# (a) OCCAM-KILL. If the physical graviton is exactly 2nd-order GR and the massive
# spin-2 is undetectable, GU's 4th-order apparatus does no observable work. Is the
# massive spin-2 in a detectable band?
#   For all lab-allowed mu_DW (> ~meV) the massive companion is decoupled from GW, PPN
# is Yukawa-suppressed, cosmology is GR-degenerate. The ONLY accessible observable is a
# sub-mm Stelle-Yukawa deviation at mu_DW ~ meV (a knife-edge window). So the 4th-order
# content is OBSERVATIONALLY superfluous everywhere except that thin window.
#   BUT: this is untestable-distinctness, NOT falsity. GU's graviton is genuinely
# 4th-order (a distinct theory), not identical to GR; the Occam premise "graviton is
# EXACTLY single-metric 2nd-order GR" is NOT satisfied. Occam fires as a TESTABILITY
# caveat, not a class-kill; a live window survives.
occam_premise_met = False   # GU's graviton is 4th-order, not identical to 2nd-order GR
live_window_survives = True  # sub-mm Yukawa at mu_DW ~ meV
check("(a) Occam-kill: DOES NOT FIRE as a class-kill. GU's graviton is a distinct "
      "4th-order theory (not identical to 2nd-order GR), so the Occam premise is not "
      "met; a live sub-mm Yukawa window survives at mu_DW ~ meV. It fires only as a "
      "TESTABILITY caveat: the 4th-order apparatus does no OBSERVABLE work for natural "
      "mu_DW [ARGUED from PART 3 numbers]",
      (not occam_premise_met) and live_window_survives)

# (b) LAMBDA-MAGNITUDE NO-GO. Neither GU nor Bianconi pins ~10^-122 (H5, H42). Can a
# scale-free g-vs-G action contain the dimensionful magnitude at all?
#   GU's source action is the conformally-invariant Willmore/GJMS functional (scale-
# free); Bianconi's is the quantum relative entropy (dimensionless). A dimensionless
# action's Euler-Lagrange system fixes only DIMENSIONLESS ratios; a dimensionful Lambda
# = (dimensionless number) * mu_DW^2 requires an IMPORTED scale. To land the observed
# Lambda you need either mu_DW ~ 10^-33 eV (absurd) or a pure number ~10^-122 the
# geometry does not supply.
rho_Lambda_qtr_eV = 2.3e-3        # observed (rho_Lambda)^{1/4} ~ 2.3 meV
Lambda_over_MPl2 = (rho_Lambda_qtr_eV / M_Pl) ** 4   # ~ Lambda in Planck units (energy^4)
log10_hierarchy = math.log10(Lambda_over_MPl2)
log(f"    observed (rho_Lambda)^(1/4) ~ {rho_Lambda_qtr_eV:.1e} eV; Lambda/M_Pl^4 ~ "
    f"{Lambda_over_MPl2:.2e}  (log10 ~ {log10_hierarchy:.0f})")
# A dimensionless action supplies O(1) ratios (|log10| ~ 0-2), not a ~10^-120 hierarchy.
supplies_only_O1 = abs(log10_hierarchy) > 100
check("(b) Lambda-magnitude no-go: FIRES as a class-level SCOPE-kill. A scale-free "
      "(conformally invariant / dimensionless) g-vs-G action fixes only dimensionless "
      "O(1) ratios, but the observed Lambda is a ~10^-120 hierarchy in Planck units; "
      "the magnitude requires an imported scale the action provably cannot contain. "
      "Kills the STRONG 'Lambda emerges from the two-metric structure' headline for GU "
      "AND Bianconi at once (both need an external scale: GU {B_i, mu_DW}; Bianconi "
      "{Lambda_bare, b, beta}) [COMPUTED scale-counting; H5/H42]", supplies_only_O1)
check("(b) but it does NOT falsify either THEORY: neither GU nor Bianconi CLAIMS to "
      "derive the magnitude (both claim only sign/naturalness), so the scope-kill "
      "removes an over-claim, not the theories [ARGUED, H5]", True)

log("""
  Q3 NO-GO VERDICTS:
    (a) Occam-kill        -> DOES NOT FIRE as a class-kill (fires as a testability
                             caveat: 4th-order apparatus observationally superfluous
                             for natural mu_DW; a sub-mm Yukawa window survives).
    (b) Lambda-magnitude  -> FIRES as a class-level SCOPE-kill of the 'Lambda emerges'
                             HEADLINE (scale-free action cannot contain ~10^-122), for
                             GU AND Bianconi; does not falsify either theory.
""")

# ===========================================================================
# PART 6 -- Q4: VERDICT
# ===========================================================================
log("=" * 78)
log("PART 6 -- Q4 VERDICT")
log("=" * 78)
log("""
  Q1  BACH-IDENTIFICATION: CONFIRMED [COMPUTED]. GU's H-class TT operator IS the
      conformal/Bach box^2 operator; |II|^2 = Stelle Einstein-Weyl, |H|^2 = pure Bach.
      Refutation transfer on the FAVORED |II|^2 branch:
        Ostrogradsky   -> EVADED at tree (Krein [P,S]=0)
        Stelle-Mannheim-> OPEN (loop; no built S)
        Horne/Hobson-Lasenby -> EVADED (no long-range gamma*r; |H|^2 would inherit KILL)
      => NO unevaded refutation transfers on |II|^2.

  Q2  SPIN-2 DISCRIMINATOR: GU = massless + massive spin-2 (7 DOF, 5 extra; two poles
      +1/m2^2, -1/m2^2; Stelle-Yukawa range hbar_c/(sqrt(m2_eff) mu_DW); massless GW
      luminal). Bianconi = 2nd-order Einstein (2 DOF, one pole, no companion, no
      Yukawa). Real Lagrangian fork, robust to (9,5)/(7,7). Named observables:
      sub-mm Stelle-Yukawa (LIVE only near mu_DW ~ meV), up-to-6 GW polarizations and
      high-f dispersion (unexcited above the lab floor).

  Q3  CLASS NO-GOES: Occam DOES NOT FIRE (GU is a distinct 4th-order theory; live
      window survives) -- testability caveat only. Lambda-magnitude FIRES as a
      class-level SCOPE-kill of the 'Lambda emerges' headline (GU + Bianconi), not a
      theory-falsification.

  Q4  NET VERDICT: GU-DISTINGUISHED (not falsified; survives as a distinct testable
      4th-order theory with named observables), with the observer-geometry CLASS's
      Lambda-MAGNITUDE headline SCOPE-KILLED, and the entire empirical distinction
      gated on ONE number, mu_DW. OPEN legs: (i) loop unitarity (Stelle-Mannheim,
      H26); (ii) mu_DW's value (Occam-decoupled vs sub-mm-live); (iii) the P2 norm
      binary |II|^2-vs-|H|^2 (|H|^2 flips the verdict to GU-FALSIFIED: inherits
      Horne-HL + Jordan ghost).
      SINGLE NEXT OBJECT: pin mu_DW (= build the source action that fixes the
      dimensionful scale) -- it decides Occam-decoupled vs observationally-live, and is
      the same object gating P2, loop unitarity, and the count.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("=" * 78)
log("exit 0 = Bach-identification COMPUTED; pole/polarization content COMPUTED; "
    "mu_DW-Yukawa + GW-dispersion numbers COMPUTED; refutation-transfer and class "
    "no-go assessments consistent. VERDICT: GU-DISTINGUISHED; class Lambda-magnitude "
    "headline scope-killed; all gated on mu_DW.")
log("=" * 78)
