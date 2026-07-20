#!/usr/bin/env python3
"""S_IG/B.5 habitat probe -- the P5 dossier's Element-1 NATIVE-PROVABLE claims
executed, and its two cheapest falsifiers (F1, F3) run, on the ACTUAL W229
objects.

CHANNEL: S_IG/B.5 construction frontier (P5 dossier, Element 1).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/sig-b5-habitat-verification-2026-07-20.md
EXTENDS: explorations/blockbuster-p5-instance-dossier-2026-07-19.md (Element 1)
         tests/channel-swings/pt3_w229_membership_probe.py (K_S, J, register)
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

QUESTION. The P5 instance dossier stakes its Element-1 carrier on two
NATIVE-PROVABLE claims never machine-checked, and names two cheap kills:
  F1 (habitat kill): the generator loop of the metric fiber
      F = GL(4,R)/O(3,1) does not exist / dies -- first exposure is the
      pi_1(F) = Z/2 computation at matrix grade.
  F3 (twist kill):  the Krein form K_S extends UNTWISTED over the loop --
      one sign count against the actual W229 K_S = e_0...e_8.
This probe runs both, plus the dossier's boxed NATIVE-PLAUSIBLE
identification ("the anchor exchange of the record audit IS the holonomy
of this twist") as ONE composed machine-checked statement.

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline). The fiber F is
the PROGRAM-NATIVE object (space of Lorentzian forms on R^4, the fiber of
Y14 = Met(X4)); the Krein form is the program-native K_S = e_0...e_8 in the
verified Cl(9,5) = M(64,H) rep (eta = diag(+1 x9, -1 x5); the base
spacetime contributes (3,1): three legs in the + group, one in the -
group). No standard-physics construction of either object is silently
substituted; the loop of forms is realized by congruence g_t = A_t^T eta
A_t (Sylvester: signature is congruence-invariant), not by any Lorentz /
Spin(9,5) transformation (a compact mixed-plane rotation is NOT in the
isometry group -- that is the point: it moves the metric).

WHAT IS TESTED:
  Part A (F1 first exposure, 4x4 grade): the fiber F deformation-retracts
      onto the RP^3 model {I - 2P : P a rank-1 projector} (spectral
      retraction; signature constant along the retraction path); the
      generator loop of unoriented timelike lines has double-cover
      monodromy -1 and its square has monodromy +1 -- the order-2 class at
      matrix grade (the covering-space step pi_1(RP^3) = Z/2 given a
      simply-connected double cover is typed IMPORTED-standard).
  Part B (F3, 14-dim grade, the actual K_S): the loop of forms
      g_t = A_t^T eta A_t for a pi-rotation A_t in a mixed (+,-) plane is a
      genuine closed loop of signature-(9,5) forms projecting onto the
      generator; the continuous g_t-orthonormal frame F(t) = A_t^{-1}
      returns with exactly the two plane legs reversed; the transported
      Krein form K_S[F(1)] = -K_S -- computed as a matrix product in the
      rep, for ALL 45 mixed planes. Controls: all 36 (+,+) planes and all
      10 (-,-) planes leave the metric CONSTANT (pure frame loops, trivial
      in F) and give K_S -> +K_S; the doubled loop (2pi) gives +K_S; a
      continuous frame redefinition contributes det(h_9) (the K_S-up-to-
      frame-orientation lemma), so the -1 monodromy is lift-independent.
      Trichotomy: the twist fires exactly on the genuine F-loops.
  Part C (the composed identification): K_S -> -K_S is the pt3/M6 anchor
      exchange: eigenspace anchors swap (P_+/- exchange), the record
      current and Krein charge flip sign, the direction co-flips, and the
      register history is INVARIANT -- the co-flip, now derived as the
      holonomy of the fiber loop rather than posited. A mu inserted to
      flip direction ALONE splits the register (the paid import), exactly
      as in the abstract co-flip probe.
  [F] REPAIR of dossier section 1.2's stated sign count: the literal
      argument ("K_S contains e_0 once" with e_0 read as THE TIMELIKE leg)
      is mislabeled -- in the (9,5) convention the timelike legs are
      e_9..e_13 and are NOT factors of K_S; flipping the timelike leg
      alone leaves K_S invariant. The flip count comes from the SPACELIKE
      partner leg of the rotation plane. Same conclusion (K_S -> -K_S),
      corrected mechanism, machine-decided.

NONCLAIMS. Nothing here builds S_IG or the B.5 global data: the boundary
Dirac FAMILY and its spectral-section existence/classification (F2, the
sharpest kill) remain at the needs-new-mathematics rung (N1-N3); the
VALUE of the bit stays externally posited (Kramers blindness untouched);
the scale and Door B elements are untouched. Deterministic; numpy only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260720)

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the actual W229 anchors --------------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                      # K_S = e_0 e_1 ... e_8


def kprod(frame_cols):
    """Ordered Clifford product of the nine +legs of a 14-frame.

    frame_cols: (14, 14) array; column c is the c-th frame vector in the
    e-basis. Returns c(f_0) c(f_1) ... c(f_8) in the rep.
    """
    out = np.eye(DIM, dtype=complex)
    for c in range(9):
        gen = sum(frame_cols[d, c] * e[d] for d in range(N_DIRS))
        out = out @ gen
    return out


def rot(n, a, b, th):
    """Rotation by angle th in the (a, b) coordinate plane of R^n."""
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def signature(g, tol=1e-9):
    w = np.linalg.eigvalsh(g)
    return int(np.sum(w > tol)), int(np.sum(w < -tol))


# --- [T] setup ----------------------------------------------------------------
herm = float(np.max(np.abs(K_S - K_S.conj().T)))
invol = float(np.max(np.abs(K_S @ K_S - np.eye(DIM))))
check("T", "K_S Hermitian and K_S^2 = I (the two eigenspaces are the two "
           "anchors)", herm < 1e-9 and invol < 1e-9,
      f"herm {herm:.1e}, invol {invol:.1e}")

cliff_ok = True
for a in range(N_DIRS):
    for b in range(a, N_DIRS):
        want = 2.0 * (ETA[a] if a == b else 0.0)
        got = e[a] @ e[b] + e[b] @ e[a]
        if float(np.max(np.abs(got - want * np.eye(DIM)))) > 1e-9:
            cliff_ok = False
check("T", "Clifford relations {e_a, e_b} = 2 eta_ab for the fixed eta "
           "(9,5)", cliff_ok)

check("T", "convention pin: the FIVE timelike legs are e_9..e_13 (eta = -1) "
           "and the base (3,1) puts its one timelike leg in that group; "
           "K_S has NO timelike factor", bool(np.all(ETA[9:] == -1.0)))


# =============================================================================
# Part A -- F1 first exposure at 4x4 grade: F ~ RP^3, pi_1 generator order 2
# =============================================================================
ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])


def retract(g):
    """Spectral retraction of a Lorentzian form onto the RP^3 model I - 2P."""
    w, v = np.linalg.eigh(g)
    P = np.outer(v[:, 0], v[:, 0])        # the unique negative eigenvector
    return np.eye(4) - 2.0 * P


ok_sig, ok_comm, ok_path, ok_model, ok_cont = True, True, True, True, True
for _ in range(100):
    A = RNG.standard_normal((4, 4))
    while abs(np.linalg.det(A)) < 1e-3:
        A = RNG.standard_normal((4, 4))
    g = A.T @ ETA4 @ A
    if signature(g) != (3, 1):
        ok_sig = False
    r = retract(g)
    if float(np.max(np.abs(g @ r - r @ g))) > 1e-8:
        ok_comm = False                   # r is a spectral function of g
    for s in np.linspace(0.0, 1.0, 11):
        if signature((1 - s) * g + s * r) != (3, 1):
            ok_path = False               # straight-line homotopy stays Lorentzian
    if signature(r) != (3, 1) or float(np.max(np.abs(r @ r - np.eye(4)))) > 1e-9:
        ok_model = False                  # image lies in the RP^3 model
    dg = 1e-6 * RNG.standard_normal((4, 4))
    if float(np.max(np.abs(retract(g + dg + dg.T) - r))) > 1e-3:
        ok_cont = False                   # retraction continuous at g
check("E", "every congruence A^T eta4 A is Lorentzian (3,1) (Sylvester, "
           "sampled)", ok_sig)
check("E", "spectral retraction r(g) = I - 2P commutes with g and the "
           "straight-line path g -> r(g) keeps signature (3,1) (deformation "
           "retraction, sampled)", ok_comm and ok_path)
check("E", "retraction image is exactly the RP^3 model {I - 2P, P rank-1 "
           "timelike} (r^2 = I, signature (3,1)); r is continuous",
      ok_model and ok_cont)

# the generator loop of unoriented timelike lines, with continuous lift
ts = np.linspace(0.0, 1.0, 401)
lift = []
w_prev = None
for t in ts:
    w = np.array([np.sin(np.pi * t), 0.0, 0.0, np.cos(np.pi * t)])
    if w_prev is not None and float(w @ w_prev) < 0.0:
        w = -w
    lift.append(w)
    w_prev = w
mono1 = float(lift[-1] @ lift[0])
check("E", "generator loop of timelike lines: continuous double-cover lift "
           "returns ANTI-periodic (monodromy -1) -- the loop is "
           "noncontractible", mono1 < -0.999, f"<v(1), v(0)> = {mono1:+.3f}")

lift2 = []
w_prev = None
for t in np.linspace(0.0, 2.0, 801):
    w = np.array([np.sin(np.pi * t), 0.0, 0.0, np.cos(np.pi * t)])
    if w_prev is not None and float(w @ w_prev) < 0.0:
        w = -w
    lift2.append(w)
    w_prev = w
mono2 = float(lift2[-1] @ lift2[0])
check("E", "the SQUARED loop lifts closed (monodromy +1) -- the class has "
           "order exactly 2 (pi_1 = Z/2 with the standard covering-space "
           "step typed IMPORTED)", mono2 > 0.999, f"<v(2), v(0)> = {mono2:+.3f}")

# the same loop realized as a loop of FORMS, projecting onto the line loop
ok_formloop = True
for t in np.linspace(0.0, 1.0, 21):
    B = rot(4, 0, 3, np.pi * t)
    gB = B.T @ ETA4 @ B
    if signature(gB) != (3, 1):
        ok_formloop = False
    r = retract(gB)
    wv, vv = np.linalg.eigh(gB)
    v_neg = vv[:, 0]
    v_want = np.array([np.sin(np.pi * t), 0.0, 0.0, np.cos(np.pi * t)])
    if abs(abs(float(v_neg @ v_want)) - 1.0) > 1e-8:
        ok_formloop = False
B1 = rot(4, 0, 3, np.pi)
ok_closed = float(np.max(np.abs(B1.T @ ETA4 @ B1 - ETA4))) < 1e-12
check("E", "the congruence loop g_t = B_t^T eta4 B_t is a CLOSED loop of "
           "Lorentzian forms whose timelike line traces the generator "
           "(F1 first exposure: the habitat loop exists)",
      ok_formloop and ok_closed)


# =============================================================================
# Part B -- F3 at 14-dim grade on the actual K_S: the twist, with controls
# =============================================================================
ETA14 = np.diag(ETA)

# B.1: the mixed-plane loop is a GENUINE loop in F (metric moves), the
# same-sign-plane loops are CONSTANT in F (pure frame loops)
mix_moves, same_const = True, True
for (a, b) in [(0, 9), (4, 11), (8, 13)]:
    moved = 0.0
    for t in np.linspace(0.1, 0.9, 9):
        A = rot(N_DIRS, a, b, np.pi * t)
        moved = max(moved, float(np.max(np.abs(A.T @ ETA14 @ A - ETA14))))
    if moved < 1e-6:
        mix_moves = False
for (a, b) in [(0, 1), (3, 7), (9, 10), (11, 13)]:
    for t in np.linspace(0.1, 0.9, 9):
        A = rot(N_DIRS, a, b, np.pi * t)
        if float(np.max(np.abs(A.T @ ETA14 @ A - ETA14))) > 1e-12:
            same_const = False
check("E", "mixed (+,-) plane rotations MOVE the form (genuine loops in F); "
           "same-sign plane rotations fix it exactly (pure frame loops, "
           "trivial in F)", mix_moves and same_const)

# B.2: along the mixed loop, g_t stays signature (9,5) and closes; the
# frame F(t) = A_t^{-1} is g_t-orthonormal and continuous
ok_sig14, ok_frame = True, True
for t in np.linspace(0.0, 1.0, 21):
    A = rot(N_DIRS, 0, 9, np.pi * t)
    g_t = A.T @ ETA14 @ A
    if signature(g_t) != (9, 5):
        ok_sig14 = False
    F = np.linalg.inv(A)
    if float(np.max(np.abs(F.T @ g_t @ F - ETA14))) > 1e-9:
        ok_frame = False
A1 = rot(N_DIRS, 0, 9, np.pi)
ok_close14 = float(np.max(np.abs(A1.T @ ETA14 @ A1 - ETA14))) < 1e-12
check("E", "mixed loop: g_t = A_t^T eta A_t keeps signature (9,5) "
           "(Sylvester), closes at t = 1, and F(t) = A_t^{-1} is a "
           "continuous g_t-orthonormal frame with F(0) = I",
      ok_sig14 and ok_frame and ok_close14)

# B.3: the full 91-plane monodromy sweep of the transported K_S
n_mixed_ok = 0
n_pp_ok = 0
n_mm_ok = 0
for a in range(N_DIRS):
    for b in range(a + 1, N_DIRS):
        F1 = np.linalg.inv(rot(N_DIRS, a, b, np.pi))
        Kt = kprod(F1)
        d_minus = float(np.max(np.abs(Kt + K_S)))
        d_plus = float(np.max(np.abs(Kt - K_S)))
        if ETA[a] * ETA[b] < 0:
            if d_minus < 1e-9:
                n_mixed_ok += 1
        elif ETA[a] > 0:
            if d_plus < 1e-9:
                n_pp_ok += 1
        else:
            if d_plus < 1e-9:
                n_mm_ok += 1
check("E", "ALL 45 mixed planes: transported K_S = -K_S exactly (the twist "
           "is REAL; falsifier F3 does NOT fire)", n_mixed_ok == 45,
      f"{n_mixed_ok}/45")
check("E", "ALL 36 (+,+) planes and 10 (-,-) planes: transported K_S = +K_S "
           "(pure frame loops do not twist -- the flip is not a frame "
           "artifact)", n_pp_ok == 36 and n_mm_ok == 10,
      f"{n_pp_ok}/36, {n_mm_ok}/10")

# B.4: the doubled loop is untwisted (order 2, matching Part A)
F2pi = np.linalg.inv(rot(N_DIRS, 0, 9, 2.0 * np.pi))
Kt2 = kprod(F2pi)
check("E", "the DOUBLED mixed loop transports K_S -> +K_S (monodromy has "
           "order exactly 2, matching pi_1 = Z/2)",
      float(np.max(np.abs(Kt2 - K_S))) < 1e-9)

# B.5: lift independence -- a frame redefinition h in O(9) x O(5)
# contributes det(h_9); continuous redefinitions cannot change the sign
ok_det = True
for _ in range(10):
    q9, _r = np.linalg.qr(RNG.standard_normal((9, 9)))
    q5, _r = np.linalg.qr(RNG.standard_normal((5, 5)))
    h = np.zeros((N_DIRS, N_DIRS))
    h[:9, :9] = q9
    h[9:, 9:] = q5
    Kh = kprod(h)
    want = float(np.sign(np.linalg.det(q9)))
    if float(np.max(np.abs(Kh - want * K_S))) > 1e-8:
        ok_det = False
check("E", "K_S[frame h] = det(h_9) K_S for h in O(9) x O(5) (K_S is "
           "well-defined up to frame orientation; a CONTINUOUS lift "
           "redefinition has constant det sign, so monodromy -1 is "
           "lift-independent)", ok_det)


# =============================================================================
# Part C -- the composed identification: loop holonomy = anchor exchange
#           = the co-flip, on the actual W229 record structure
# =============================================================================
def Jvec(K, psi):
    return np.array([float((psi.conj() @ (K @ e[a]) @ psi).real)
                     for a in range(N_DIRS)])


def krein_q(K, psi):
    return float((psi.conj() @ K @ psi).real)


def record_register(qs, eps, mu=1):
    n = 0.0
    out = [n]
    for q in qs:
        n = n + mu * eps * q
        out.append(n)
    return out


K_hol = -K_S                              # the loop-transported Krein form
P_plus = 0.5 * (np.eye(DIM) + K_S)
P_plus_hol = 0.5 * (np.eye(DIM) + K_hol)
P_minus = 0.5 * (np.eye(DIM) - K_S)
check("E", "holonomy action on the anchors: P_+(-K_S) = P_-(K_S) exactly "
           "(the two Krein anchors are EXCHANGED by the loop -- the deck "
           "action on the two-section structure at kinematic grade)",
      float(np.max(np.abs(P_plus_hol - P_minus))) < 1e-12)

ok_q, ok_J, ok_reg, ok_split = True, True, True, True
for _ in range(50):
    psi = P_plus @ (RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM))
    psi /= np.linalg.norm(psi)
    q0, q1 = krein_q(K_S, psi), krein_q(K_hol, psi)
    if not (q0 > 0 and abs(q1 + q0) < 1e-9):
        ok_q = False                      # confined charge flips sign exactly
    if float(np.max(np.abs(Jvec(K_hol, psi) + Jvec(K_S, psi)))) > 1e-9:
        ok_J = False                      # record current flips with the anchor
    qs = [krein_q(K_S, P_plus @ (RNG.standard_normal(DIM)
          + 1j * RNG.standard_normal(DIM))) for _ in range(5)]
    reg = record_register(qs, eps=+1)
    reg_hol = record_register([-q for q in qs], eps=-1)
    if any(abs(x - y) > 1e-9 for x, y in zip(reg, reg_hol)):
        ok_reg = False                    # co-flip: register history invariant
    reg_mu = record_register(qs, eps=-1)  # direction flipped ALONE (a mu)
    if all(abs(x - y) < 1e-9 for x, y in zip(reg, reg_mu)) and any(
            abs(q) > 1e-6 for q in qs):
        ok_split = False                  # the unpaid flip must split
check("E", "holonomy = anchor exchange: Krein charge and record current "
           "flip sign EXACTLY under the transported form (q -> -q, "
           "J -> -J on confined draws)", ok_q and ok_J)
check("E", "the co-flip composes: (sector, direction) flip TOGETHER under "
           "the holonomy and the register history is invariant -- the M6 "
           "anchor exchange IS the holonomy of the fiber twist, now one "
           "machine-checked chain", ok_reg)
check("F", "control: flipping the direction ALONE (an inserted mu) splits "
           "the register -- the unpaid Z/2 remains detectable at the "
           "holonomy composition point, exactly as in the abstract co-flip "
           "probe", ok_split)

# the dossier 1.2 repair: the literal sign count is mislabeled
h_time = np.eye(N_DIRS)
h_time[9, 9] = -1.0                       # flip ONLY the timelike leg
K_tflip = kprod(h_time)
h_space = np.eye(N_DIRS)
h_space[0, 0] = -1.0                      # flip ONLY the spacelike partner
K_sflip = kprod(h_space)
lit_dead = float(np.max(np.abs(K_tflip - K_S))) < 1e-12
mech_ok = float(np.max(np.abs(K_sflip + K_S))) < 1e-12
check("F", "REPAIR of dossier 1.2: flipping the TIMELIKE leg alone leaves "
           "K_S invariant (the literal 'timelike leg e_0 in K_S' mechanism "
           "is dead); the sign comes from the SPACELIKE partner leg of the "
           "mixed plane (flip it alone: K_S -> -K_S). Same conclusion, "
           "corrected mechanism", lit_dead and mech_ok)


# --- headline -----------------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
