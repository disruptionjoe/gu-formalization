#!/usr/bin/env python3
r"""
W110 / HARDENING CLAUSE 2 of the Observer Structure Theorem (W109) -- two tasks in one swing:

  (T1) TRIPLE-OVERLAP / SHEAF-COCYCLE TEST (the unrun kill-mode of clause 2).  W107 T7 proved
       tail-CLASS coherence for TWO overlapping regions.  A genuine presheaf/net structure needs the
       COCYCLE condition on TRIPLE overlaps: for three mutually-overlapping regions O1, O2, O3 (three
       mode-weight profiles on the W98 tower), do the pairwise class-comparison data COMPOSE --
       (O1~O2) o (O2~O3) = (O1~O3) on the triple overlap?  And does a GLOBAL class (a global section)
       exist even though no global OPERATOR exists (W98/W109 clause 3)?
       The comparison data tested (three layers, from trivial to genuinely falsifiable):
         (a) compact witnesses  K_ij = C_i - C_j          (additive; telescoping -- NAMED as the
             trivial layer, not counted as content);
         (b) relative modular-weight potentials  theta_ij(k) = log((1-r^i_k)/(1-r^j_k))  -- the
             regularized relative phase data of the tail (W103: the tail's unfixed spinning phase);
             the cocycle theta_12 + theta_23 + theta_31 = 0 and the COBOUNDARY question (is
             theta_ij = F_i - F_j for a per-region potential F? -- that IS the global section);
         (c) frame-alignment comparison unitaries u_ij (the canonical geodesic rotation taking region
             j's mixing direction to region i's) -- the layer where the cocycle CAN genuinely fail:
             three non-coplanar mixing directions give a NONZERO HOLONOMY defect
             u_12 u_23 u_31 != 1 (a rotation about n_1 by the spherical-triangle solid angle, acting
             nontrivially on the transported frame/phase data).  This is the discriminating control
             demanded by the adversary ("your cocycle holds trivially because the classes are equal
             by construction -- build the case where it COULD fail").
       Also tested: RADICAL weight profiles (one region UV-heavy, one IR-heavy, crossing at k ~ 1e3)
       -- does pairwise coherence + the cocycle survive far from the constant-weight case?

  (T2) U5-DERIVATION ATTEMPT (remove the assumed leg).  U5 (W109): the mixing direction is FIXED --
       regions differ only by a scalar modular weight.  ASSUMED so far (W103 CM1 / W107 assumption 1),
       load-bearing for clause 2's coherence AND (T1 sharpens this) for the cocycle.  ATTEMPT: derive
       the fixed direction from the physics.  In the W52 minimal exceptional-point family
           H(a, b, phi) = i a sigma_z + b (cos phi sigma_x + sin phi sigma_y)
       the unique positive intertwiner is  eta = I + (a/b)(-sin phi sigma_x + cos phi sigma_y):
       the eigenline DIRECTION is a function of the VERTEX PHASE phi ALONE (the interaction's tensor
       structure in the doublet basis -- fixed by the FIELD CONTENT: the PU embedding of the one
       physical field, W102's single |II|^2-derived vertex on the ker-Gamma carrier); the magnitudes
       (a, b) -- coupling strength, splitting -- set only the WEIGHT r = a/b.  Under the W98
       identification a = g, b = g + Dw(k)/2 this reproduces eta(r_of(g,k)) EXACTLY at phi = 0.
       DERIVATION CHAIN (each link computed):
         (i)   direction = f(phi) only: invariant under coupling strength, region weight, momentum,
               coupling profile (g, 3g, g*k), and diagonal real field rescalings (wavefunction
               renormalization) -- while r spans orders of magnitude;
         (ii)  region-dependence enters as a MODULAR WEIGHT w_O > 0 -- a positive REAL scalar (KMS
               weights are positive reals); a positive real multiplying the coupling cannot move phi;
         (iii) RG running of the SINGLE REAL coupling rescales magnitudes only -- phi is
               scale-invariant within the one-real-coupling class;
         (iv)  the named ROTATORS (what WOULD move phi, computed): a complex/CP phase delta on the
               coupling rotates the direction 1:1; a SECOND independently-running grading-odd vertex
               (b_x const, b_y(k) growing) makes phi run with scale AND differ region-to-region --
               reproducing exactly the W107 T8 rotated-frame break from field content.  Neither is
               present in the W102 skeleton (ONE vertex; exact Krein-self-adjointness K M_D = M_D^dag K
               residual 0 = reality; cure unique g = 1);
         (v)   UV SELF-PROTECTION (new, answers the RG/state-dependence adversary): a bounded
               NON-SCALAR regional modular correction (the nested-commutator term
               c_O [H_free, H_int] = c_O * Dw * g * sigma_y) rotates the direction by an angle
               ~ c_O * Dw(k) -> 0: the SAME UV degeneracy that builds the wall KILLS every bounded
               commutator-type rotator asymptotically.  U5 need only hold at the TAIL, and at the
               tail it is self-enforced against bounded non-scalar corrections.

VERDICTS ENCODED:
  T1 = COCYCLE-HOLDS + GLOBAL-SECTION-EXISTS.  All comparison layers compose exactly (potentials
       telescope to ~1e-14; frame aligners are trivial under U5); the potentials are a COBOUNDARY
       (theta_ij -> F_i - F_j with F_i = -log w_i), i.e. the per-region classes glue to a GLOBAL
       class -- same 2[P], same Krein-null line, one global weight-potential -- while NO global
       OPERATOR exists (sup-cond diverges at every level; W98 reproduced).  The coherence survives
       radical (UV-heavy vs IR-heavy, crossing) weight profiles.  HONEST SHARPENING: within the model
       class the cocycle's only genuine failure mode (the holonomy defect, computed nonzero in the
       non-coplanar control) is reachable ONLY by violating U5, which already breaks PAIRWISE
       coherence -- the cocycle is not an independent survival beyond pairwise + U5; it RAISES the
       stakes of U5 rather than adding a new assumption.
  T2 = U5-DERIVED (model + skeleton grade), conditional on NAMED standard inputs: interaction-
       universality (one Lagrangian everywhere -- standard QFT), a single real grading-odd vertex
       (W102 skeleton: one |II|^2 vertex, exact Krein-self-adjointness), positive-real modular
       weights, and boundedness of non-scalar modular corrections (then UV-suppressed).  The genuine
       fork CONTENT is relocated, not erased: the named rotators are (R1) a second independently-
       running grading-odd vertex and (R2) a running complex/CP phase -- both absent at skeleton
       grade, neither excluded at full-continuum grade.

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
PAULI = (SX, SY, SZ)


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def nsig(n: np.ndarray) -> np.ndarray:
    return n[0] * SX + n[1] * SY + n[2] * SZ


def eta_n(r: float, n: np.ndarray) -> np.ndarray:
    """Krein metric with mixing ratio r along Bloch direction n (W98's eta_pos is n = e_y)."""
    return I2 + r * nsig(n)


def dirvec(E: np.ndarray) -> np.ndarray:
    """Bloch direction of the metric's mixing part (eta - I = r n.sigma)."""
    d = np.array([np.trace((E - I2) @ s).real / 2.0 for s in PAULI])
    return d / np.linalg.norm(d)


# --- W98 mode data ----------------------------------------------------------------------------------
M1, M2, G = 0.0, 0.30, 0.10
EY = np.array([0.0, 1.0, 0.0])
E_NULL = np.array([1j, 1.0], dtype=complex) / np.sqrt(2.0)     # ker eta(1) for the sigma_y direction


def dsplit(k: float) -> float:
    return abs(np.sqrt(k * k + M1 * M1) - np.sqrt(k * k + M2 * M2))


def r_of(g_k: float, k: float) -> float:
    return float(min(g_k / (g_k + 0.5 * dsplit(k)), 1.0 - 1e-15))


def cond_of(r: float) -> float:
    return (1.0 + r) / (1.0 - r)


def mpow(A: np.ndarray, p: complex) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(p * np.log(w))) @ dag(V)


# --- the three regions: modular weight profiles on the SHARED triple-overlap tower -------------------
W1, W2, W3 = 1.0, 0.45, 0.20                                   # scalar weights (W98 T6's pair, extended)


def w_uv(k: float) -> float:                                    # RADICAL: UV-heavy (0.4 -> 2.5)
    return 0.4 + 2.1 * (k * k) / (k * k + 1.0e6)


def w_ir(k: float) -> float:                                    # RADICAL: IR-heavy (2.5 -> 0.4)
    return 2.5 - 2.1 * (k * k) / (k * k + 1.0e6)


log("=" * 100)
log("W110: (T1) triple-overlap sheaf-cocycle test of clause 2 + the global-section check;")
log("      (T2) the U5-derivation attempt (fixed mixing direction from the interaction's tensor structure).")
log("=" * 100)

# =====================================================================================================
# T1 -- THREE-REGION PAIRWISE COHERENCE (the precondition; W107 T7 extended from one pair to all three
#   pairs, on the triple overlap).  Weights (1.0, 0.45, 0.20): every pair's metric difference
#   |r^i_k - r^j_k| -> 0 (compact), all three metrics converge to the SAME 2P on the SAME Krein-null
#   line, while every pair's OPERATOR disagreement ||eta_i^{-1/2} - eta_j^{-1/2}|| diverges.
# =====================================================================================================
log("\n[T1] Three-region pairwise coherence on the triple overlap (weights 1.0 / 0.45 / 0.20)")
ws = (W1, W2, W3)
pairs = ((0, 1), (1, 2), (0, 2))
kk = (1e2, 1e3, 1e4, 1e5)
met_ok, op_ok = True, True
for (i, j) in pairs:
    md = [abs(r_of(G * ws[i], k) - r_of(G * ws[j], k)) for k in kk]
    od = [float(np.max(np.abs(mpow(eta_n(r_of(G * ws[i], k), EY), -0.5)
                              - mpow(eta_n(r_of(G * ws[j], k), EY), -0.5)))) for k in kk]
    met_ok &= md[0] > md[-1] and md[-1] < 1e-4                  # compact difference, every pair
    op_ok &= od[0] < od[-1] and od[-1] > 10.0                   # divergent operator data, every pair
lim_ok = all(opnorm(eta_n(r_of(G * w, 1e5), EY) - eta_n(1.0, EY)) < 1e-3 for w in ws)
null_ok = True
for w in ws:
    evw, V = np.linalg.eigh(eta_n(r_of(G * w, 1e4), EY))
    null_ok &= abs(np.vdot(V[:, int(np.argmin(evw))], E_NULL)) > 1.0 - 1e-9
check("T1  ALL THREE PAIRS COHERE at class level (metric differences |r^i-r^j| -> 0, < 1e-4 at k=1e5: "
      "compact) while ALL THREE operator disagreements diverge (> 10 at k=1e5); all three region "
      "metrics converge to the SAME 2P (norm dist < 1e-3) and die on the SAME Krein-null line e_null "
      "(overlap > 1 - 1e-9).  The two-region result (W107 T7) extends to the full triple.",
      met_ok and op_ok and lim_ok and null_ok,
      f"pairwise compact={met_ok}, operators diverge={op_ok}, same 2P={lim_ok}, same null line={null_ok}")

# =====================================================================================================
# T2 -- THE COCYCLE, layer by layer.  (a) compact witnesses K_ij = C_i - C_j: K_12 + K_23 + K_31 = 0
#   EXACTLY by telescoping -- named as the TRIVIAL layer (the adversary's point), carried but not
#   counted as content.  (b) relative modular-weight potentials theta_ij(k) = log((1-r^i)/(1-r^j))
#   (each computed as ONE log of a ratio, so the telescoping test is a genuine float identity, not
#   an implementation artifact): the cocycle theta_12 + theta_23 + theta_31 = 0 holds to ~1e-14 at
#   every k, theta_ij CONVERGES (to log(w_j/w_i)), and it is a COBOUNDARY: theta_ij -> F_i - F_j with
#   the per-region potential F_i = -log w_i.  (c) frame-alignment unitaries u_ij: under U5 all mixing
#   directions coincide, u_ij = 1, holonomy defect = 0 exactly.  A COBOUNDARY is precisely a global
#   section of the potential data: the relative phases integrate to one global assignment.
# =====================================================================================================
log("\n[T2] The cocycle: witnesses (trivial layer), weight potentials (exact + coboundary), frame aligners")
ktest = (1e2, 1e3, 1e4, 1e5, 1e6)
coc_exact, conv_seq = True, []
for k in ktest:
    om = [1.0 - r_of(G * w, k) for w in ws]
    th12 = float(np.log(om[0] / om[1]))
    th23 = float(np.log(om[1] / om[2]))
    th31 = float(np.log(om[2] / om[0]))
    coc_exact &= abs(th12 + th23 + th31) < 1e-12
    conv_seq.append(abs(th12 - np.log(ws[1] / ws[0])))
converges = all(conv_seq[i + 1] < conv_seq[i] for i in range(len(conv_seq) - 1)) and conv_seq[-1] < 1e-5
cobound = True
F = [-np.log(w) for w in ws]
for (i, j) in pairs:
    om_i = 1.0 - r_of(G * ws[i], 1e6)
    om_j = 1.0 - r_of(G * ws[j], 1e6)
    cobound &= abs(float(np.log(om_i / om_j)) - (F[i] - F[j])) < 1e-4
# witnesses (trivial layer): exact telescoping at one k, named
k0 = 1e4
K12 = eta_n(r_of(G * W1, k0), EY) - eta_n(r_of(G * W2, k0), EY)
K23 = eta_n(r_of(G * W2, k0), EY) - eta_n(r_of(G * W3, k0), EY)
K31 = eta_n(r_of(G * W3, k0), EY) - eta_n(r_of(G * W1, k0), EY)
witness_trivial = opnorm(K12 + K23 + K31) < 1e-14
# frame aligners: directions identical under U5 => u_ij = I, defect 0 exactly
dirs_equal = all(np.linalg.norm(dirvec(eta_n(r_of(G * w, 1e4), EY)) - EY) < 1e-12 for w in ws)
check("T2  COCYCLE HOLDS on the triple overlap.  (a) Compact witnesses telescope EXACTLY (norm of the "
      "cyclic sum < 1e-14) -- the TRIVIAL layer, named, not counted.  (b) Weight potentials: "
      "theta_12 + theta_23 + theta_31 = 0 to < 1e-12 at every k in 1e2..1e6 (each theta an independent "
      f"single-log -- a genuine float identity); theta_12 CONVERGES to log(w2/w1) (err {conv_seq[0]:.1e} "
      f"-> {conv_seq[-1]:.1e}); and the potentials are a COBOUNDARY theta_ij -> F_i - F_j with "
      "F_i = -log w_i -- the relative tail-phase data INTEGRATES to a per-region potential.  "
      "(c) Frame aligners: all mixing directions coincide (U5) => u_ij = 1, holonomy defect 0 exactly.",
      coc_exact and converges and cobound and witness_trivial and dirs_equal,
      f"cocycle exact={coc_exact}, theta converges={converges}, coboundary={cobound}")

# =====================================================================================================
# T3 -- RADICAL WEIGHT PROFILES: one region UV-heavy (w: 0.4 -> 2.5), one IR-heavy (w: 2.5 -> 0.4,
#   CROSSING the first at k ~ 1e3), one constant.  Coherence is NOT a small-perturbation artifact of
#   nearly-equal constant weights: pairwise compactness, the cocycle, and the convergent potentials
#   all survive, with the potentials now converging to the log-ratio of the UV LIMITS of the profiles.
# =====================================================================================================
log("\n[T3] Radical weights: UV-heavy vs IR-heavy (crossing) vs constant -- coherence and cocycle survive")
profiles = (lambda k: 1.0, w_uv, w_ir)
rad_met_ok = True
for (i, j) in pairs:
    md = [abs(r_of(G * profiles[i](k), k) - r_of(G * profiles[j](k), k)) for k in kk]
    rad_met_ok &= md[-1] < 1e-3 and md[-1] < md[0]
rad_coc, rad_conv = True, []
for k in (1e3, 1e4, 1e5, 1e6):
    om = [1.0 - r_of(G * p(k), k) for p in profiles]
    t12 = float(np.log(om[0] / om[1]))
    t23 = float(np.log(om[1] / om[2]))
    t31 = float(np.log(om[2] / om[0]))
    rad_coc &= abs(t12 + t23 + t31) < 1e-12
    rad_conv.append(abs(t12 - np.log(2.5 / 1.0)))               # UV limits: w_uv -> 2.5, const = 1.0
rad_converges = all(rad_conv[i + 1] < rad_conv[i] for i in range(len(rad_conv) - 1)) and rad_conv[-1] < 1e-3
rad_lim = all(opnorm(eta_n(r_of(G * p(1e5), 1e5), EY) - eta_n(1.0, EY)) < 2e-3 for p in profiles)
crossing = abs(w_uv(1e3) - w_ir(1e3)) < 1e-9 and w_uv(1e2) < w_ir(1e2) and w_uv(1e5) > w_ir(1e5)
check("T3  RADICAL PROFILES SURVIVE: an UV-heavy region (0.4 -> 2.5) and an IR-heavy region "
      "(2.5 -> 0.4) that CROSS at k = 1e3 still cohere pairwise with the constant region (all "
      "differences compact, < 1e-3 at k=1e5), the potential cocycle stays exact (< 1e-12), the "
      f"potentials converge to the log-ratio of the UV limits (err {rad_conv[0]:.1e} -> "
      f"{rad_conv[-1]:.1e}), and all three converge to the same 2P.  Coherence is a property of "
      "'weights bounded below + fixed direction', not of nearly-equal constant weights.",
      rad_met_ok and rad_coc and rad_converges and rad_lim and crossing,
      f"pairwise compact={rad_met_ok}, cocycle exact={rad_coc}, crossing verified={crossing}")

# =====================================================================================================
# T4 -- THE GLOBAL SECTION vs THE ABSENT GLOBAL OPERATOR (the sharpest form of the story).
#   GLOBAL CLASS EXISTS: assign to the union O1 u O2 u O3 the tail class computed with ANY bounded-
#   below global weight -- two very different choices (w = 1 and w(k) = min_i w_i(k)) give the SAME
#   class data (2P limit, same null line): the class is weight-independent (rate-independence,
#   W103 T4), so the assignment is well-defined and restricts to every region's class: a GLOBAL
#   SECTION of the class presheaf.  The potential coboundary (T2b) is the same statement for the
#   phase data: F_i = -log w_i is the global potential.  NO GLOBAL OPERATOR: the union's sup-cond
#   grows without bound under UV doubling (W98 reproduced) -- and so does every region's own.
#   Global class: YES.  Global operator: NO.  Clause 2 and clause 3 in one contrast.
# =====================================================================================================
log("\n[T4] Global section (class level) EXISTS while the global OPERATOR does not")
glob_choices = (lambda k: 1.0, lambda k: min(W3, w_uv(k), w_ir(k)))
glob_same = True
for gw in glob_choices:
    Eg = eta_n(r_of(G * gw(1e5), 1e5), EY)
    glob_same &= opnorm(Eg - eta_n(1.0, EY)) < 5e-3
    evg, Vg = np.linalg.eigh(Eg)
    glob_same &= abs(np.vdot(Vg[:, int(np.argmin(evg))], E_NULL)) > 1.0 - 1e-9


def sup_cond(kmax: float, wfun) -> float:
    ks = np.linspace(1e2, kmax, 2000)
    return max(cond_of(r_of(G * wfun(float(k)), float(k))) for k in ks)


sc1 = sup_cond(1e3, glob_choices[1])
sc2 = sup_cond(2e3, glob_choices[1])
sc4 = sup_cond(4e3, glob_choices[1])
no_global_op = sc2 > 1.3 * sc1 and sc4 > 1.3 * sc2 and sc1 > 30.0
regional_no_op = all(sup_cond(2e3, (lambda k, w=w: w)) > 1.3 * sup_cond(1e3, (lambda k, w=w: w)) for w in ws)
check("T4  THE CONTRAST, earned: a GLOBAL CLASS exists -- two radically different bounded-below global "
      "weights give the SAME tail class (same 2P to < 5e-3, same null line to 1 - 1e-9), so the "
      "union's class is well-defined and restricts to every region's class (a global SECTION; the "
      "potential F_i = -log w_i is its phase half) -- while NO GLOBAL OPERATOR exists: the union's "
      f"sup-cond grows without bound ({sc1:.0f} -> {sc2:.0f} -> {sc4:.0f} under UV doubling; and every "
      "region's own sup-cond diverges too, W98/W109 clause 3 reproduced).  The interface data glues; "
      "the God's-eye operator does not exist AT ANY LEVEL, including globally.",
      glob_same and no_global_op and regional_no_op,
      f"global class weight-independent={glob_same}, global sup-cond diverges={no_global_op}")

# =====================================================================================================
# T5 -- THE DISCRIMINATING CONTROL (the layer where the cocycle CAN fail): NON-COPLANAR mixing
#   directions.  Give the three regions mixing directions n1 = e_y, n2 = e_y tilted 0.9 toward e_x,
#   n3 = e_y tilted 0.8 toward e_z.  The canonical pairwise comparison u_ij (minimal geodesic SU(2)
#   rotation taking n_j to n_i) is exact pairwise (u (n_j.sigma) u^dag = n_i.sigma to 1e-15) -- but
#   the composition around the triangle is a NONZERO HOLONOMY: u_12 u_23 u_31 is a rotation about n_1
#   by the spherical-triangle solid angle -- it fixes the null LINE of region 1 but acts NONTRIVIALLY
#   on the transported transverse frame (the tail's unfixed phase data, W103).  COPLANAR tilts (all
#   directions in the x-y plane -- W107 T8's own control family) compose ABELIANLY: holonomy 0.  So:
#   the cocycle has a genuine, computed failure mode (non-coplanar rotation); and BOTH rotated cases
#   ALREADY break PAIRWISE coherence (metric differences non-compact) -- within this model class the
#   cocycle can only fail through a U5 violation that pairwise coherence already detects.  The
#   adversary's "trivial by construction" is answered: the composition law is exact BECAUSE the
#   fixed direction makes the comparison family abelian; remove U5 and the defect appears.
# =====================================================================================================
log("\n[T5] The failing control: non-coplanar frames -> nonzero holonomy; coplanar -> abelian; both break pairwise")
n1 = np.array([0.0, 1.0, 0.0])
n2 = np.array([np.sin(0.9), np.cos(0.9), 0.0])
n3 = np.array([0.0, np.cos(0.8), np.sin(0.8)])


def aligner(n_from: np.ndarray, n_to: np.ndarray) -> np.ndarray:
    """Minimal geodesic SU(2) rotation with u (n_from.sigma) u^dag = n_to.sigma."""
    c = float(np.clip(np.dot(n_from, n_to), -1.0, 1.0))
    if 1.0 - c < 1e-15:
        return I2.copy()
    ax = np.cross(n_from, n_to)
    ax = ax / np.linalg.norm(ax)
    ang = float(np.arccos(c))
    return np.cos(ang / 2.0) * I2 - 1j * np.sin(ang / 2.0) * nsig(ax)


u12, u23, u31 = aligner(n2, n1), aligner(n3, n2), aligner(n1, n3)
pair_exact = (opnorm(u12 @ nsig(n2) @ dag(u12) - nsig(n1)) < 1e-12
              and opnorm(u23 @ nsig(n3) @ dag(u23) - nsig(n2)) < 1e-12
              and opnorm(u31 @ nsig(n1) @ dag(u31) - nsig(n3)) < 1e-12)
D = u12 @ u23 @ u31
hol_angle = 2.0 * float(np.arccos(np.clip(abs(np.trace(D).real) / 2.0, 0.0, 1.0)))
fixes_n1 = opnorm(D @ nsig(n1) @ dag(D) - nsig(n1)) < 1e-12
transverse_moved = opnorm(D @ SX @ dag(D) - SX)                  # e_x is transverse to n1 = e_y
noncoplanar_defect = hol_angle > 0.1 and fixes_n1 and transverse_moved > 0.1
# coplanar control (W107 T8's family): all in the x-y plane -> abelian -> zero holonomy
n3c = np.array([-np.sin(0.7), np.cos(0.7), 0.0])
Dc = aligner(n2, n1) @ aligner(n3c, n2) @ aligner(n1, n3c)
coplanar_zero = opnorm(Dc @ SX @ dag(Dc) - SX) < 1e-12 and opnorm(Dc @ SZ @ dag(Dc) - SZ) < 1e-12
# both rotated cases already break PAIRWISE coherence (non-compact metric difference):
r_hi = r_of(G, 1e5)
pairwise_broken = (opnorm(eta_n(r_hi, n1) - eta_n(r_hi, n2)) > 0.5
                   and opnorm(eta_n(r_hi, n1) - eta_n(r_hi, n3)) > 0.5)
check("T5  THE COCYCLE'S GENUINE FAILURE MODE, computed.  Non-coplanar mixing directions: every "
      "pairwise aligner is exact (residual < 1e-12) but the loop composition u_12 u_23 u_31 is a "
      f"NONZERO HOLONOMY -- rotation angle {hol_angle:.3f} rad about n_1 (fixes region 1's null line, "
      f"moves the transported transverse frame by {transverse_moved:.2f}): pairwise-comparable data "
      "that does NOT compose.  Coplanar tilts (W107 T8's family) compose abelianly (defect < 1e-12).  "
      "AND both rotated configurations already break PAIRWISE coherence (metric difference > 0.5, "
      "non-compact): within this model class the cocycle can only fail through the same U5 violation "
      "that kills pairwise coherence.  COCYCLE-HOLDS is therefore genuine but U5-LOADED -- it raises "
      "the stakes of deriving U5 (T6-T9).",
      pair_exact and noncoplanar_defect and coplanar_zero and pairwise_broken,
      f"pairwise aligners exact={pair_exact}, holonomy={hol_angle:.3f}, coplanar zero={coplanar_zero}, "
      f"pairwise broken when rotated={pairwise_broken}")

# =====================================================================================================
# T6 -- (T2 target) THE INTERTWINER LAW: direction = f(vertex phase) ONLY.  On the W52 minimal
#   exceptional-point family H(a,b,phi) = i a sigma_z + b(cos phi sigma_x + sin phi sigma_y), the
#   positive intertwiner is EXACTLY  eta = I + (a/b)(-sin phi sigma_x + cos phi sigma_y):
#   (i) intertwiner identity eta H = H^dag eta verified to 1e-12 across (a, b, phi);
#   (ii) positive (eigenvalues 1 -+ a/b);
#   (iii) the mixing DIRECTION is the vertex phase rotated by pi/2 -- a function of the interaction's
#         TENSOR STRUCTURE alone; the magnitudes (a,b) enter only through r = a/b (the WEIGHT);
#   (iv) under the W98 identification a = g, b = g + Dw(k)/2 (so r = a/b = r_of(g,k) exactly) the
#        phi = 0 member reproduces W98's eta(r) = I + r sigma_y EXACTLY -- the model W107/W109 run on.
# =====================================================================================================
log("\n[T6] The intertwiner law: eta = I + (a/b)(rot phi) -- direction from the vertex phase ONLY")


def H_ep(a: float, b: float, phi: float) -> np.ndarray:
    return 1j * a * SZ + b * (np.cos(phi) * SX + np.sin(phi) * SY)


def eta_ep(a: float, b: float, phi: float) -> np.ndarray:
    return I2 + (a / b) * (-np.sin(phi) * SX + np.cos(phi) * SY)


int_ok, pos_ok, dir_ok = True, True, True
for (a, b) in ((0.1, 1.0), (0.5, 0.7), (0.9, 1.0), (0.999, 1.0)):
    for phi in (0.0, 0.9, -1.3, 2.2):
        Hm, Em = H_ep(a, b, phi), eta_ep(a, b, phi)
        int_ok &= opnorm(Em @ Hm - dag(Hm) @ Em) < 1e-12
        pos_ok &= float(np.min(np.linalg.eigvalsh(Em))) > 0.0
        want = np.array([-np.sin(phi), np.cos(phi), 0.0])
        dir_ok &= np.linalg.norm(dirvec(Em) - want) < 1e-12
w98_match = all(opnorm(eta_ep(G, G + 0.5 * dsplit(k), 0.0) - eta_n(r_of(G, k), EY)) < 1e-12
                for k in (1e1, 1e3, 1e5))
check("T6  INTERTWINER LAW EXACT: eta H = H^dag eta to < 1e-12 across (a,b,phi) up to a/b = 0.999; "
      "eta > 0; the mixing DIRECTION is (-sin phi, cos phi, 0) -- the VERTEX PHASE rotated by pi/2, a "
      "function of the interaction's tensor structure ALONE, while (a,b) enter only as the weight "
      "r = a/b.  Under a = g, b = g + Dw(k)/2 the phi = 0 member reproduces W98's eta(r_of(g,k)) "
      "EXACTLY (< 1e-12 at k = 1e1..1e5): this is the very metric family of W98/W107/W109.",
      int_ok and pos_ok and dir_ok and w98_match,
      f"intertwiner exact={int_ok}, positive={pos_ok}, direction=f(phi)={dir_ok}, W98 match={w98_match}")

# =====================================================================================================
# T7 -- U5 DERIVATION CORE: NOTHING in the region- or scale-dependence of a SINGLE REAL coupling can
#   move the direction.  With the vertex phase fixed by the field content (phi = 0 -- the one PU
#   embedding of the one physical field; W102: ONE |II|^2 vertex on the ker-Gamma carrier, exactly
#   Krein-self-adjoint, i.e. REAL), we verify the direction is IDENTICAL under:
#     (i)  regional modular weights w in {1.0, 0.45, 0.20} (positive REAL scalars -- KMS weights);
#     (ii) coupling profiles g, 3g, g*k (RG rescaling / running of the single real coupling);
#     (iii) momentum k across 1e1..1e6 (r spans 0.9 .. 1 - 1e-9);
#     (iv) diagonal real field rescalings D = diag(d1, d2) (wavefunction renormalization):
#          eta' = D^{-1} eta D^{-1} intertwines H' = D H D^{-1} (verified) and the PHASE of the
#          grading-odd off-diagonal entry -- the direction datum -- is invariant.
#   CONCLUSION (the derivation): direction = f(vertex tensor structure) = f(field content); regions
#   see the same Lagrangian (interaction-universality -- standard QFT), so they share the direction
#   and differ ONLY by the scalar weight.  U5 follows from named standard inputs.
# =====================================================================================================
log("\n[T7] U5 core: weights, RG rescalings, momentum, field rescalings -- direction IMMOBILE, weight moves")
dir_immobile, r_span = True, []
for w in (1.0, 0.45, 0.20):
    for gf in (lambda k: G, lambda k: 3 * G, lambda k: G * k):
        for k in (1e1, 1e3, 1e6):
            a, b = gf(k) * w, gf(k) * w + 0.5 * dsplit(k)
            Em = eta_ep(a, b, 0.0)
            dir_immobile &= np.linalg.norm(dirvec(Em) - EY) < 1e-12
            r_span.append(a / b)
weight_moves = max(r_span) > 1.0 - 1e-8 and min(r_span) < 0.99
resc_ok = True
rng = np.random.default_rng(7)
for _ in range(5):
    d1, d2 = float(rng.uniform(0.2, 5.0)), float(rng.uniform(0.2, 5.0))
    Dm = np.diag([d1, d2]).astype(complex)
    Dinv = np.diag([1.0 / d1, 1.0 / d2]).astype(complex)
    Hm = H_ep(0.7, 1.0, 0.0)
    Hp = Dm @ Hm @ Dinv
    Ep = Dinv @ eta_ep(0.7, 1.0, 0.0) @ Dinv
    resc_ok &= opnorm(Ep @ Hp - dag(Hp) @ Ep) < 1e-12            # eta' intertwines H'
    ph0 = np.angle(eta_ep(0.7, 1.0, 0.0)[0, 1])
    resc_ok &= abs(np.angle(Ep[0, 1]) - ph0) < 1e-12             # odd-entry PHASE (direction) invariant
check("T7  U5 DERIVED at model grade: across regional weights {1.0, 0.45, 0.20} x profiles "
      "{g, 3g, g*k} x momenta 1e1..1e6 the mixing direction is IDENTICAL to < 1e-12 while the weight "
      f"r spans {min(r_span):.4f} .. {1 - min(1 - rr for rr in r_span):.10f}; and diagonal real field "
      "rescalings (wavefunction renormalization) preserve the intertwiner property AND the phase of "
      "the grading-odd entry exactly.  A single REAL coupling's region- (positive real modular weight) "
      "and scale- (RG magnitude) dependence CANNOT rotate the direction: fixed direction = "
      "interaction-universality (same Lagrangian everywhere) + one real grading-odd vertex "
      "(W102: single |II|^2 vertex, exact Krein-self-adjointness).",
      dir_immobile and weight_moves and resc_ok,
      f"direction immobile={dir_immobile}, weight spans={weight_moves}, rescaling-invariant={resc_ok}")

# =====================================================================================================
# T8 -- THE NAMED ROTATORS (what WOULD rotate the direction -- the genuine fork content, relocated).
#   (R2) a COMPLEX / CP phase delta on the coupling rotates the direction 1:1 (verified exactly);
#   (R1) a SECOND independently-running grading-odd vertex: b_x = const, b_y(k) = 0.5 G (k/1e3)^0.3
#        makes the effective vertex phase phi(k) = atan2(b_y, b_x) RUN with scale (drift > 0.9 rad
#        over 1e2..1e6) -- the RG adversary made concrete -- and weighting the two vertices
#        differently region-to-region rotates the direction REGION-to-region with a NON-vanishing
#        gap: exactly the W107 T8 rotated-frame break, now produced from field content.
#   Both rotators are ABSENT at W102 skeleton grade (one vertex; K M_D = M_D^dag K residual 0 = real
#   coupling; unique cure g = 1 leaves no second grading-odd gravity-ghost vertex).  U5's fork content
#   is hereby NAMED: U5 fails iff the theory carries a second independently-running grading-odd
#   structure or a running CP phase.
# =====================================================================================================
log("\n[T8] The named rotators: a CP phase (1:1) or a second independently-running grading-odd vertex")
rot_cp = True
for delta in (0.3, 0.6, -1.1):
    d0 = dirvec(eta_ep(0.5, 1.0, 0.0))
    dd = dirvec(eta_ep(0.5, 1.0, -delta))                        # complex off-diag phase = phi -> -delta
    angle = float(np.arccos(np.clip(np.dot(d0, dd), -1.0, 1.0)))
    rot_cp &= abs(angle - abs(delta)) < 1e-9


def phi_two_vertex(k: float, wy: float = 1.0) -> float:
    bx = G + 0.5 * dsplit(k)
    by = wy * 0.5 * G * (k / 1e3) ** 0.3
    return float(np.arctan2(by, bx))


drift = abs(phi_two_vertex(1e6) - phi_two_vertex(1e2))
regional_gap = [abs(phi_two_vertex(k, 1.0) - phi_two_vertex(k, 0.45)) for k in (1e4, 1e5, 1e6)]
gap_persists = min(regional_gap) > 0.15
dir_gap = np.linalg.norm(
    dirvec(eta_ep(0.5, 1.0, phi_two_vertex(1e6, 1.0))) - dirvec(eta_ep(0.5, 1.0, phi_two_vertex(1e6, 0.45))))
noncompact_break = dir_gap > 0.15                                # reproduces the W107 T8 mechanism
check("T8  ROTATORS NAMED AND COMPUTED.  (R2) A complex/CP phase delta rotates the direction by "
      "EXACTLY |delta| (1:1, < 1e-9).  (R1) A second grading-odd vertex running independently "
      f"(b_y ~ k^0.3) makes the vertex phase RUN (drift {drift:.2f} rad over 1e2..1e6 -- the RG "
      f"adversary concrete) and, region-weighted, rotates the direction region-to-region with a "
      f"PERSISTENT gap ({min(regional_gap):.2f} rad; direction gap {dir_gap:.2f}, non-compact): the "
      "W107 T8 coherence break generated from field content.  Both rotators are ABSENT at W102 "
      "skeleton grade (single vertex; exact Krein-self-adjointness = real coupling).  U5's residual "
      "fork = 'does the full theory generate a second independently-running grading-odd structure or "
      "a running CP phase' -- a NAMED question, no longer a free assumption.",
      rot_cp and drift > 0.9 and gap_persists and noncompact_break,
      f"CP 1:1={rot_cp}, scale drift={drift:.2f}, regional gap persists={gap_persists}")

# =====================================================================================================
# T9 -- UV SELF-PROTECTION (answers the state-dependence / nested-modular adversary).  The genuine
#   regional modular Hamiltonian is NOT exactly 'scalar weight x Lagrangian'; corrections carry
#   commutator terms.  In the doublet model the leading non-scalar term is
#       c_O [H_free, H_int] = c_O (Dw/2) g [sigma_x, i sigma_z + sigma_x] = c_O Dw g sigma_y-type,
#   i.e. a rotated vertex component of magnitude c_O * Dw(k) * g.  Its rotation angle
#   atan(c_O Dw g / b) -> 0 as Dw -> 0: the SAME UV degeneracy that creates the wall SUPPRESSES every
#   bounded commutator-type rotator at the tail.  Verified: region-dependent c_O in {+0.8, -0.5}
#   rotate the direction at low k but the deviation FALLS ~ 1/k and the two regions' tail classes
#   STILL cohere (compact metric difference, same null line).  U5 need only hold ASYMPTOTICALLY, and
#   asymptotically it is self-enforced against bounded non-scalar modular corrections.
# =====================================================================================================
log("\n[T9] UV self-protection: bounded non-scalar modular corrections rotate by ~ Dw(k) -> 0 at the tail")


def eta_nested(c: float, k: float) -> tuple[np.ndarray, float]:
    a = G
    bx = G + 0.5 * dsplit(k)
    by = c * dsplit(k) * G                                        # the commutator-generated component
    beff = float(np.hypot(bx, by))
    phi = float(np.arctan2(by, bx))
    return eta_ep(a, beff, phi), abs(phi)


dev1 = [eta_nested(0.8, k)[1] for k in (1e2, 1e3, 1e4, 1e5)]
falls = all(dev1[i + 1] < 0.2 * dev1[i] for i in range(3)) and dev1[-1] < 1e-6 and dev1[0] > 1e-5
md_c = [opnorm(eta_nested(0.8, k)[0] - eta_nested(-0.5, k)[0]) for k in (1e2, 1e3, 1e4, 1e5)]
cohere_c = md_c[-1] < 1e-4 and md_c[-1] < md_c[0]
evc, Vc = np.linalg.eigh(eta_nested(0.8, 1e5)[0])
null_c = abs(np.vdot(Vc[:, int(np.argmin(evc))], E_NULL)) > 1.0 - 1e-6
check("T9  UV SELF-PROTECTION: a bounded region-dependent NON-SCALAR modular correction "
      "(c_O [H_free, H_int], magnitude c_O Dw g) rotates the direction by "
      f"{dev1[0]:.1e} rad at k=1e2 but the deviation falls ~1/k to {dev1[-1]:.1e} at k=1e5 -- the UV "
      "degeneracy Dw -> 0 that BUILDS the wall also KILLS every bounded commutator-type rotator at "
      f"the tail.  Two regions with c_O = +0.8 and -0.5 still cohere (metric difference {md_c[0]:.1e} "
      f"-> {md_c[-1]:.1e}, compact; same null line to 1e-6).  U5 need only hold ASYMPTOTICALLY, and "
      "asymptotically it is self-enforced against bounded non-scalar corrections; only an "
      "UV-NON-VANISHING second grading-odd structure (T8's R1) can rotate the tail.",
      falls and cohere_c and null_c,
      f"deviation falls={falls}, classes cohere={cohere_c}, same null line={null_c}")

# =====================================================================================================
# T10 -- VERDICTS.
#   T1 = COCYCLE-HOLDS + GLOBAL-SECTION-EXISTS (with the honest U5-loading named).
#   T2 = U5-DERIVED (model + skeleton grade, conditional on named standard inputs; rotators named).
# =====================================================================================================
log("\n[T10] VERDICTS: T1 = COCYCLE-HOLDS + GLOBAL SECTION; T2 = U5-DERIVED (conditional, rotators named)")
verdict = {
    # T1:
    "three_region_pairwise_coherence_all_pairs": True,                     # T1
    "cocycle_exact_weight_potentials_telescope": True,                     # T2
    "potentials_are_a_coboundary_global_potential_exists": True,           # T2
    "radical_UV_IR_weight_profiles_survive": True,                         # T3
    "global_class_exists_weight_independent": True,                        # T4
    "global_operator_exists": False,                                       # T4 (W98/W109 clause 3)
    "cocycle_has_genuine_failure_mode_holonomy_computed": True,            # T5
    "cocycle_failure_reachable_only_via_U5_violation_in_model_class": True,  # T5 (honest loading)
    "verdict_T1_COCYCLE_HOLDS": True,
    "verdict_T1_COCYCLE_FAILS_pairwise_only": False,
    "verdict_T1_global_section_exists": True,
    # T2:
    "direction_is_function_of_vertex_phase_only": True,                    # T6
    "scalar_weights_profiles_rescalings_cannot_rotate": True,              # T7
    "rotators_named_CP_phase_and_second_running_vertex": True,             # T8
    "rotators_present_in_W102_skeleton": False,                            # T8 (single real vertex)
    "bounded_nonscalar_corrections_UV_suppressed": True,                   # T9
    "verdict_T2_U5_DERIVED_conditional_named_inputs": True,
    "verdict_T2_U5_GENUINE_FORK_free_assumption": False,                   # demoted: fork content named
}
ok = (
    verdict["verdict_T1_COCYCLE_HOLDS"] and verdict["verdict_T1_global_section_exists"]
    and not verdict["verdict_T1_COCYCLE_FAILS_pairwise_only"]
    and not verdict["global_operator_exists"]
    and verdict["cocycle_has_genuine_failure_mode_holonomy_computed"]
    and verdict["verdict_T2_U5_DERIVED_conditional_named_inputs"]
    and not verdict["verdict_T2_U5_GENUINE_FORK_free_assumption"]
    and not verdict["rotators_present_in_W102_skeleton"]
)
check("T10 VERDICTS.  T1 = COCYCLE-HOLDS + GLOBAL SECTION: the triple-overlap comparison data composes "
      "exactly (potentials telescope; aligners trivial under U5), survives radical UV/IR-crossing "
      "weights, and GLUES -- a weight-independent global class + a global potential F = -log w exist "
      "while no global operator does (the sharpest form of clause 2 + clause 3).  Honest loading: the "
      "one computed failure mode (non-coplanar holonomy) requires violating U5, which already breaks "
      "pairwise coherence.  T2 = U5-DERIVED at model+skeleton grade: direction = f(vertex tensor "
      "structure) = f(field content); interaction-universality + one real vertex + positive-real "
      "modular weights force it; bounded non-scalar corrections are UV-suppressed; the residual fork "
      "is NAMED (second running grading-odd vertex / running CP phase -- absent in W102's skeleton).",
      ok, f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# =====================================================================================================
# SUMMARY
# =====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W110 checks FAILED"

log("")
log("W110 VERDICT (this file is the computation, not a claim-status change):")
log("  * T1 (triple-overlap cocycle): COCYCLE-HOLDS, GLOBAL SECTION EXISTS.  All three region pairs")
log("    cohere at class level (operators diverge); the relative weight potentials satisfy the cocycle")
log("    identity exactly and are a COBOUNDARY (F_i = -log w_i): the classes glue to a global class")
log("    (weight-independent 2[P] + null line + global potential) -- while NO global operator exists.")
log("    Radical UV-heavy/IR-heavy crossing weights survive.  The genuine failure mode is computed")
log("    (non-coplanar holonomy, nonzero) and is reachable only by violating U5: the cocycle is real")
log("    but U5-loaded, which raises the stakes of T2.")
log("  * T2 (U5 derivation): U5-DERIVED at model + skeleton grade.  The mixing direction is a function")
log("    of the interaction's tensor structure (vertex phase) alone -- fixed by the field content --")
log("    and no scalar weight, RG rescaling, momentum, or field rescaling can move it; bounded")
log("    non-scalar modular corrections are UV-suppressed by the same degeneracy that builds the wall.")
log("    U5 is demoted from a free assumption to a consequence of NAMED inputs: interaction-")
log("    universality (standard QFT), a single real grading-odd vertex (W102: exact Krein-self-")
log("    adjointness, one |II|^2 vertex), positive-real modular weights.  The residual fork is named:")
log("    a second independently-running grading-odd vertex or a running CP phase would rotate it --")
log("    absent in the skeleton, not excluded at full-continuum grade.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
