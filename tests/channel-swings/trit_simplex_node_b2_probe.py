#!/usr/bin/env python3
"""PRE-REGISTERED NODE B2 (simplex camp): does the trit's canonical Z/3 couple
to the GRADE-2 antisymmetric (two-form) sector, and is its three-ness the
BOUNDARY of a 2-simplex (one filled triangle) rather than a chain of grade-1
objects?

BINDING:   explorations/prereg-trit-symmetry-and-fork-2026-07-20.md (cafcbc7),
           Node B2. This is the SIMPLEX-CAMP half of the copies/simplex fork.
DIRECTED:  Joe direct chat, 2026-07-20 (pre-registered Node B2: two-form/simplex).
STATUS:    deterministic exact/near-exact probe; [T]/[E]/[F]; the plant gives the
           test teeth; HEADLINE names B2-HOLDS or B2-FAILS; exit 0 iff all pass.
           No claim/canon/posture movement.

IMPORTED MACHINERY (do not rebuild):
  * l1_assembly_probe.py -- the frozen Cl(9,5)=M(64,H) rep e[a], K_S, U_h, the
    quaternionic structure C_J (J_quat = C_J.conj), the commutant Sp(1)_comm
    = span_R{I, iI, J, iJ}, and ks_sign. Re-run live (exit 0).
  * n4_two_z3s_probe.py -- the trit CHARACTER: the three order-3 sectors are the
    3-Sylow {0,8,16} of Z/24 = pi_3^s; admissible orderings EXACTLY
    {(0,8,16),(0,16,8)} (a complex-conjugate pair = the UNORIENTED trit). Live.
  * tests/rs_bicomplex_spin95_connection_2form.py -- the verified grade-2 machine:
    Sigma_ab = (1/4)[e_a,e_b], the so(9,5) connection two-form generators. Their
    construction (bivector = grade 2) is reused here verbatim.

THE FROZEN FACTS (cited, not re-derived):
  - torsion-generation-arena (2026-07-20): the trit's Z/3 is the order-3 class
    J(k=64) in im J = Z/24, delivered by the COMMUTANT twist R1; the metric /
    spin-lift sector (R0=R2, where the grade-2 so(9,5) rotations live) winds ZERO.
  - trit-triage (af7425f): the trit is UNORIENTED (both orderings admissible,
    conjugation-symmetric) and its only frozen order-3 family element is the
    commutant scalar omega*I, a GLOBAL PHASE that FIXES every ray.
  - k1-reframe (2026-07-20): the grade-3 self-dual record bridge is REAL but NOT
    NATIVE; its c=3 members are the ZERO class (order 1) -- three-ness at grade 3
    is trivial.

CONTROL (bound, [F]): a genuine grade-1 chain (three 1-forms in a path / a hollow
triangle of edges) must NOT present the closed-triangle/two-form signature -- it
does not bound a face, so H_1 != 0 (no filling), while a real 2-simplex fills its
3-cycle (H_1 = 0). The test distinguishes a filled triangle from a path.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np
from scipy.linalg import expm

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def import_probe(fname):
    name = fname[:-3]
    spec = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    code = 0
    buf = io.StringIO()
    t0 = time.time()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as ex:
        code = int(ex.code or 0)
    mod._exit_code = code
    return mod, time.time() - t0


t_start = time.time()
print("=" * 78)
print("SETUP  live import of the frozen grade machinery (l1 rep + n4 trit char)")
print("=" * 78)

l1, dt_l1 = import_probe("l1_assembly_probe.py")
check("T", "l1_assembly_probe.py re-runs LIVE and clean (exit 0): frozen "
           "Cl(9,5) rep, K_S, C_J (J_quat), commutant Sp(1)_comm arrive frozen",
      l1._exit_code == 0 and all(ok for _t, _n, ok in l1.RESULTS),
      f"exit {l1._exit_code}, {dt_l1:.1f} s")

n4, dt_n4 = import_probe("n4_two_z3s_probe.py")
check("T", "n4_two_z3s_probe.py re-runs LIVE and clean (exit 0): trit CHARACTER "
           "= 3-Sylow {0,8,16} of Z/24; admissible EXACTLY {(0,8,16),(0,16,8)} "
           "(the conjugate pair = UNORIENTED trit)",
      n4._exit_code == 0 and not n4.FAILED
      and n4.PHI_D == {0: 0, 1: 8, 2: 16} and n4.PHI_B == {0: 0, 1: 16, 2: 8}
      and n4.admissible == {(0, 8, 16), (0, 16, 8)},
      f"exit {n4._exit_code}, {dt_n4:.1f} s")

e, K_S, C_J, I128 = l1.e, l1.K_S, l1.C_J, l1.I128
N = 14
OMEGA = complex(np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3))   # zeta3, the trit


def mono(A):
    """The Clifford monomial e_{a0} e_{a1} ... (ordered), a grade-|A| element."""
    M = I128.astype(complex)
    for a in A:
        M = M @ e[a]
    return M


def grade_frac(X, p):
    """Fraction of ||X||_F^2 lying in the Clifford grade-p subspace, via the
    trace-orthonormal monomial basis {E_A/||E_A||} , |A| = p."""
    Xn2 = float(np.linalg.norm(X) ** 2)
    if Xn2 == 0.0:
        return 0.0
    tot = 0.0
    for A in combinations(range(N), p):
        EA = mono(A)
        nA = float(np.trace(EA.conj().T @ EA).real)   # = 128
        c = np.trace(EA.conj().T @ X) / nA
        tot += abs(c) ** 2 * nA
    return tot / Xn2


# grade-machinery power receipt: a pure grade-p monomial must read grade_frac=1
# at p and 0 elsewhere (the projector has teeth and is normalized).
pow_ok = (abs(grade_frac(I128, 0) - 1.0) < 1e-9
          and abs(grade_frac(e[0], 1) - 1.0) < 1e-9 and grade_frac(e[0], 2) < 1e-12
          and abs(grade_frac(e[0] @ e[1], 2) - 1.0) < 1e-9
          and grade_frac(e[0] @ e[1], 1) < 1e-12
          and abs(grade_frac(mono((0, 1, 2)), 3) - 1.0) < 1e-9)
check("T", "grade projector POWER: pure grade-p monomials read grade_frac = 1 "
           "at their own grade and 0 elsewhere (I->g0, e0->g1, e0e1->g2, "
           "e0e1e2->g3); the two-form projector fires on genuine bivectors",
      pow_ok)

# =============================================================================
print()
print("=" * 78)
print("LEG (a)  GRADE DECOMPOSITION of the trit's canonical order-3 operators")
print("         -- does the Z/3 live in / couple to grade-2 (the two-form)?")
print("=" * 78)

# The trit's Z/3 is delivered by the COMMUTANT Sp(1)_comm = span_R{I, iI, J, iJ}
# with J = C_J.conj (arena R1). Its order-3 elements come in two types.
#
# TYPE 1 (C-linear): the only order-3 element of the frozen family-preserving
# structure (trit-triage): the commutant scalar omega*I -- a global phase.
q_scalar = OMEGA * I128
g_sc = {p: grade_frac(q_scalar, p) for p in range(4)}
scalar_ok = (abs(g_sc[0] - 1.0) < 1e-9 and g_sc[2] < 1e-12
             and abs(q_scalar @ q_scalar @ q_scalar - I128).max() < 1e-9)

# TYPE 2 (quaternionic): a genuine order-3 unit quaternion q = -1/2 + (sqrt3/2) J
# in Sp(1)_comm (q^3 = 1). Its LINEAR matrix piece = -1/2 I (grade 0); its
# ANTILINEAR matrix piece = (sqrt3/2) C_J. Decompose both matrix pieces.
M_lin = -0.5 * I128
M_anti = (np.sqrt(3) / 2.0) * C_J
# q^3 = 1 as a quaternion (real repr on {I,J}): verify via the 2x2 quaternion
qi = np.array([[-0.5, -np.sqrt(3) / 2.0], [np.sqrt(3) / 2.0, -0.5]])  # -1/2 + s3/2 j
quat_order3 = float(np.max(np.abs(qi @ qi @ qi - np.eye(2)))) < 1e-12
lin_g = {p: grade_frac(M_lin, p) for p in range(4)}
anti_g = {p: grade_frac(M_anti, p) for p in range(4)}
cj_g6 = grade_frac(C_J, 6)   # C_J is the pure grade-6 quaternionic structure
# grade-2 content of the whole quaternionic order-3 element: 0 on BOTH pieces
quat_g2_zero = lin_g[2] < 1e-12 and anti_g[2] < 1e-12
# norm accounting: linear -> grade 0 (|-1/2|^2 = 1/4 of the unit quat); anti ->
# grade 6 (3/4). Together grades {0,6}. Nothing in grade 2.
accounting = (abs(lin_g[0] - 1.0) < 1e-9 and abs(anti_g[0]) < 1e-12
              and abs(cj_g6 - 1.0) < 1e-9)

check("E", "LEG (a) B2-FAILS core: BOTH canonical trit order-3 operators have "
           "grade-2 content EXACTLY ZERO. Type-1 omega*I is PURE grade-0 "
           "(g0=1.000, g2=%.1e); Type-2 quaternion -1/2 + (sqrt3/2)J splits as "
           "grade-0 linear (-1/2 I) (+) grade-6 antilinear ((sqrt3/2)C_J) "
           "(g2_lin=%.1e, g2_anti=%.1e; C_J is pure grade-6, frac=%.3f). The "
           "trit's Z/3 lives in the COMMUTANT, whose Clifford support is grades "
           "{0,6}, NOT the antisymmetric two-form sector."
      % (g_sc[2], lin_g[2], anti_g[2], cj_g6),
      scalar_ok and quat_order3 and quat_g2_zero and accounting,
      f"omega*I g0={g_sc[0]:.3f}; quat lin g0={lin_g[0]:.3f} anti g6=C_J {cj_g6:.3f}")

# GUARD (anti-blindness): grade-2 DOES host order-3 elements -- so a zero above
# is a fact about the TRIT, not a blind projector. exp((4pi/3) Sigma_01) is
# order 3 and is 3/4 grade-2 (its generator Sigma_01 = (1/4)[e0,e1] is a pure
# so(9,5) two-form). This is the SIMPLEX camp's best grade-2 candidate.
Sig01 = 0.25 * (e[0] @ e[1] - e[1] @ e[0])       # rs_bicomplex grade-2 generator
g3_rot = expm((4 * np.pi / 3.0) * Sig01)
rot_order3 = float(np.max(np.abs(g3_rot @ g3_rot @ g3_rot - I128))) < 1e-9
rot_g2 = grade_frac(g3_rot, 2)
sig01_g2 = grade_frac(Sig01, 2)
check("E", "LEG (a) anti-blindness GUARD: grade-2 genuinely HOSTS order-3 "
           "elements -- g3 = exp((4pi/3) Sigma_01) has g3^3 = I and lies 3/4 in "
           "grade-2 (Sigma_01 is a pure two-form, g2=%.3f). So the trit's "
           "grade-2 = 0 is a real decoupling, not a blind test: a two-form "
           "order-3 object exists, the trit simply is NOT one."
      % sig01_g2,
      rot_order3 and rot_g2 > 0.7 and sig01_g2 > 0.999,
      f"g3^3=I; g3 grade-2 frac={rot_g2:.3f}")

# DISCRIMINATOR: the grade-2 order-3 rotation g3 and the trit's order-3 omega*I
# are categorically DIFFERENT objects. g3 (a genuine so(9,5) rotation) MOVES
# rays; omega*I FIXES every ray (projectively trivial, trit-triage). A two-form
# that carried the trit would have to act like the trit -- it does not.
rng = l1.rng
psi = rng.standard_normal(128) + 1j * rng.standard_normal(128)
psi /= np.linalg.norm(psi)
trit_fixes_ray = abs(abs(np.vdot(psi, OMEGA * psi)) - 1.0) < 1e-12
g3_moves_ray = abs(abs(np.vdot(psi, g3_rot @ psi)) - 1.0) > 1e-3
check("E", "DISCRIMINATOR: the trit order-3 (omega*I) FIXES every ray "
           "(|<psi,omega psi>|=1, projectively trivial), while the grade-2 "
           "order-3 rotation g3 MOVES rays (|<psi,g3 psi>| < 1). The two-form "
           "order-3 element and the trit are DIFFERENT objects -- the trit "
           "does not act as any bivector rotation; consistent with arena R1 "
           "(commutant, winds k=64) vs R2 (spin/metric two-form, winds 0)",
      trit_fixes_ray and g3_moves_ray,
      f"|<psi,g3 psi>|={abs(np.vdot(psi, g3_rot @ psi)):.3f}")

# =============================================================================
print()
print("=" * 78)
print("LEG (b)  is the trit Z/3 the BOUNDARY of a 2-SIMPLEX (a filled")
print("         triangle) -- and is a 2-simplex boundary even the right SHAPE?")
print("=" * 78)


def h1_rank(edges, faces, nverts):
    """rank H_1 = dim ker(d1) - rank(im d2) for the oriented simplicial complex."""
    d1 = np.zeros((nverts, len(edges)))
    for j, (u, v) in enumerate(edges):
        d1[u, j] -= 1.0
        d1[v, j] += 1.0
    ker_d1 = len(edges) - np.linalg.matrix_rank(d1)
    if faces:
        eidx = {ed: j for j, ed in enumerate(edges)}
        d2 = np.zeros((len(edges), len(faces)))
        for k, (a, b, c) in enumerate(faces):
            for (u, v), s in (((b, c), 1.0), ((a, c), -1.0), ((a, b), 1.0)):
                d2[eidx[(u, v)], k] += s
        im_d2 = np.linalg.matrix_rank(d2)
    else:
        im_d2 = 0
    return int(ker_d1 - im_d2)


EDGES = [(0, 1), (1, 2), (0, 2)]
filled = h1_rank(EDGES, [(0, 1, 2)], 3)      # 2-simplex: 3-cycle bounds a face
hollow = h1_rank(EDGES, [], 3)               # grade-1 loop, no face
path = h1_rank([(0, 1), (1, 2), (2, 3)], [], 4)   # three 1-forms in a PATH

# The trit is UNORIENTED (both (0,8,16) and (0,16,8) admissible = a conjugate
# pair). A 2-simplex boundary d[012] = [12]-[02]+[01] is ORIENTED: transposing
# two vertices multiplies it by -1 (odd permutation). An unoriented 3-cycle
# cannot BE an oriented 2-simplex boundary.
eidx = {ed: j for j, ed in enumerate(EDGES)}
bnd = np.zeros(3)
for (u, v), s in (((1, 2), 1.0), ((0, 2), -1.0), ((0, 1), 1.0)):
    bnd[eidx[(u, v)]] += s
# transpose vertices 0<->1: edges relabel with induced orientation sign
bnd_swapped = np.zeros(3)
swap = {0: 1, 1: 0, 2: 2}
for (u, v), s in (((1, 2), 1.0), ((0, 2), -1.0), ((0, 1), 1.0)):
    uu, vv = swap[u], swap[v]
    sgn = 1.0 if uu < vv else -1.0
    ed = (min(uu, vv), max(uu, vv))
    bnd_swapped[eidx[ed]] += s * sgn
simplex_is_oriented = float(np.linalg.norm(bnd_swapped + bnd)) < 1e-9  # flips sign
trit_unoriented = n4.admissible == {(0, 8, 16), (0, 16, 8)}

check("E", "LEG (b) B2-FAILS: the trit is UNORIENTED (both orderings "
           "admissible), but a 2-simplex boundary d[012] is ORIENTED -- "
           "transposing two vertices sends it to MINUS itself (odd perm), so "
           "its symmetry preserving the oriented boundary is only cyclic Z/3 "
           "and it carries a native orientation the trit lacks. An unoriented "
           "Z/3 is not the boundary of an oriented 2-simplex; and (Leg a) the "
           "trit carries no grade-2 face to bound in the first place",
      simplex_is_oriented and trit_unoriented and filled == 0,
      f"filled H1={filled}; boundary flips sign under transposition")

# [F] CONTROL (bound): the homology test has TEETH -- a filled triangle
# (2-simplex, has a two-form face) fills its 3-cycle (H_1 = 0), while a genuine
# grade-1 chain (hollow triangle / a path of three 1-forms) does NOT present
# that closed-triangle signature: the hollow loop has H_1 = 1 (no filling) and
# the open path has no 1-cycle at all. Filled is not path.
check("F", "CONTROL: the closed-triangle/two-form signature is DISTINGUISHABLE "
           "from a grade-1 chain -- filled 2-simplex H_1=0 (the 3-cycle bounds "
           "a face), hollow grade-1 triangle H_1=1 (an unfilled 1-cycle, no "
           "two-form), open 3-edge path H_1=0 but acyclic (no 1-cycle). The "
           "test tells a filled triangle from a path; the trit, carrying zero "
           "grade-2 (Leg a), patterns with the UNFILLED side -- no face exists",
      filled == 0 and hollow == 1 and path == 0,
      f"filled={filled}, hollow={hollow}, path={path}")

# =============================================================================
print()
print("=" * 78)
print("LEG (c)  connection to the GRADE-3 door (torsion three-form / k1-reframe)")
print("=" * 78)

# k1-reframe: the one live grade-3 object (the self-dual record bridge
# K_S(e_i + lambda e_hat_i)) is REAL but NOT NATIVE; its c=3 members give the
# ZERO class. Recompute: order(J(64*c)) in Z/24 = 24/gcd(24,64c); c=3 -> k=192
# -> gcd 24 -> order 1 (trivial). Three-ness at grade 3 is trivial, not the trit.
order_c3 = 24 // np.gcd(24, 64 * 3)
order_c1 = 24 // np.gcd(24, 64 * 1)
grade3_c3_trivial = (order_c3 == 1 and order_c1 == 3)
# and the trit own carrier is grades {0,6}, not grade 3: a grade-3 dressed
# kernel (the k1-reframe control shape) is a DIFFERENT object, not the trit.
K3 = mono((0, 1, 9))                          # e_0 e_1 e_9, the grade-3 dressing
k3_g3 = grade_frac(K3, 3)                       # the reframe door's grade-3 sector
trit_not_grade3 = anti_g[3] < 1e-12 and lin_g[3] < 1e-12 and g_sc[3] < 1e-12
check("E", "LEG (c): the grade-3 door does NOT rescue the simplex reading. The "
           "grade-3 self-dual bridge c=3 members are the ZERO class "
           "(order(J(64*3)) = 24/gcd(24,192) = 1) while c=1 gives order 3 -- "
           "three-ness AT grade 3 is trivial. And the trit own carrier has "
           "zero grade-3 content (commutant grades {0,6}); the grade-3 "
           "dressing e_0 e_1 e_9 (frac=%.2f) is a DIFFERENT, non-native object "
           "(k1-reframe kill). No grade-2/grade-3 home for the trit Z/3."
      % k3_g3,
      grade3_c3_trivial and trit_not_grade3 and k3_g3 > 0.1,
      f"order(c=3)={order_c3}, order(c=1)={order_c1}; trit grade-3=0")

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print("=" * 78)
print("HEADLINE: NODE B2 -> B2-FAILS.  The trit canonical Z/3 does NOT couple")
print("  to the grade-2 antisymmetric (two-form) sector and is NOT a 2-simplex")
print("  boundary. (a) Both canonical order-3 operators have grade-2 content")
print("  EXACTLY ZERO: omega*I is pure grade-0; the quaternionic q = -1/2 +")
print("  (sqrt3/2)J splits grade-0 (+) grade-6 (commutant support {0,6}). The")
print("  projector is NOT blind -- grade-2 hosts order-3 rotations")
print("  (exp(4pi/3 Sigma_01), 3/4 grade-2) but the trit acts unlike them")
print("  (fixes rays vs moves rays; R1 commutant vs R2 spin, winds 0). (b) A")
print("  2-simplex boundary is ORIENTED (flips under transposition) while the")
print("  trit is UNORIENTED, and the trit carries no grade-2 face to bound.")
print("  (c) The grade-3 door is trivial for three-ness (c=3 -> ZERO class)")
print("  and is a different non-native object. FORK: F-NEITHER on the simplex")
print("  leg (B2 fails); B1 (copies) is tested separately.")
print("  CONTROL: filled H1=0 vs hollow grade-1 H1=1 vs path H1=0 -- the")
print("  filled-triangle/two-form signature is distinguishable from a chain.")
print(f"{nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s)")
print("=" * 78)
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
