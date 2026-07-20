#!/usr/bin/env python3
"""Phase-1 torsor kill sequence K3 -> K4 -> K2 (pre-registered), plus the
k = 64c general-m bookkeeping re-derivation.

CHANNEL: ID-1 torsor identification (the rep-weight half of the torsor demand).
DESIGN:  explorations/phase0-torsor-identification-tree-2026-07-20.md
         (commit f31f8d7; the ledger rows and node kill/survive conditions of
         that tree BIND this probe; target = the tree's MINIMAL SUFFICIENT
         STATEMENT MS, not the full-carrier-rep statement).
DIRECTED: Joe direct chat, 2026-07-20 (Phase 1: torsor kill sequence, K3 then
         K4 then K2, per the tree's own kill order).
STATUS:  exploration tier; conditional (R0_COND framed-reading fork); no
         claim/canon/posture movement.

MACHINERY REUSE (import, not rebuild). The sibling probes are terminal
scripts (module-level battery + sys.exit), so they are imported via importlib
with stdout captured and SystemExit(0) ASSERTED -- each import re-runs the
frozen battery live and its exit code is itself a [T] check here:
  - phase0_torsor_checks.py       (Test N battery + R1/R2 power + PLANT K7)
  - sig_b5_habitat_probe.py       (the verified co-flip / deck holonomy)
  - pt3_w229_membership_probe.py  (K_S / record current / register fixtures)
  - d1_coperator_build_probe.py   (the frozen D1 degenerate-anchor fixture)
  - torsion_arena_probe.py        (WZW quadrature, quat_right, order24)
  - verify_torsion_arena_probe.py (the verifier battery on the arena result)
Only tiny derived objects are built here; every fixture and kill test is the
imported one. Deterministic (fixed seeds throughout); numpy only.

WHAT IS TESTED (per node, pre-declared conditions from the tree):

  K3 (Node 1, expected kill) -- the Sigma bicomplex dressing
      W = 1.0 Sigma_09 + 0.7 Sigma_12 (the a-priori operator-grade pin).
      Decisive: Test N on the dressing generator. Section-7 guard honored:
      the commutant PROJECTION of the generator is computed BEFORE killing
      (a mixed candidate must not be killed while carrying a commutant part).

  K4 (Node 3, highest prior) -- the bridge tensor B from the record-current
      bilinear J^a = Re<Psi, K_S e_a Psi> (W203). The bridge tensor is the
      current bilinear with one commutant insertion:
          B[a, mu] = Re< u_mu Psi, K_S e_a Psi >,
      u_mu in {I, iI, J, iJ} the commutant quaternion basis (J = C conj).
      Contracting the model direction v against B[a, .] is the only frozen
      route from model-space directions to Sp(1)_comm. Pre-declared kill:
      B degenerate or non-equivariant. Also checked: two EXACT algebraic
      identities that force the outcome; the Sp(1)_comm-invariance of the
      current (placement-robustness of the verdict + K1 prior consequence);
      synthetic detectability controls (the construction CAN see commutant
      couplings when they exist -- the zero is the record current's own).

  K2 (Node 2) -- the C-weld ambiguity shape at the frozen D1 degenerate
      anchor. Pre-declared kill: the admissible-C set is bigger than one
      commutant orbit, or not a (free) orbit at all. Carrier grade (the d1
      probe's faithful-miniature receipt): exhibit an admissible continuum
      through the canonical C = K_S and compute the Sp(1)_comm conjugation
      orbit through it; toy grade: the ad-rank of the K-isometry action on
      the delta = 0 pair block (the symmetric-space dimension) vs dim sp(1).

  BK (confidence note) -- independent re-derivation of the k = 64c
      general-m bookkeeping at control grade: multiplicity padding rides
      identity (m-independence), block doubling and pointwise squaring are
      additive in c (Dynkin additivity, two routes), and the Z/24 arithmetic
      v2(64c) >= 6, order 3 iff 3-not-|c.

NONCLAIMS. No MS construction is claimed (all three nodes KILL -- see the
companion exploration for what that does and does not entail); the framed-
reading fork (R0_COND) is untouched; K1 (Node 4) is NOT executed here --
only its naturality prior is hit by the shared-source identity; nothing
here moves claims, canon, or public posture.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as bridge  # noqa: E402

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def import_probe(fname):
    """Import a terminal sibling probe: run its battery with stdout captured,
    assert it exits 0, return (module, seconds). The import IS a live re-run
    of the frozen receipt."""
    name = fname[:-3]
    spec = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    t0 = time.time()
    code = 0
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as ex:
        code = int(ex.code or 0)
    mod._captured_output = buf.getvalue()
    mod._exit_code = code
    return mod, time.time() - t0


t_start = time.time()
print("=" * 78)
print("SETUP  fixtures + live re-run of the imported machinery")
print("=" * 78)

e, Gamma, Pi_RS, M_D = bridge.constraint_objects()
I128 = np.eye(128, dtype=complex)
C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]      # J_quat = C . conj (canon)
K_S = e[0].copy()
for i in range(1, 9):
    K_S = K_S @ e[i]                                # K_S = e_0 ... e_8
RNG = np.random.default_rng(20260720)

check("T", "fixtures: J_quat^2 = -1 exact; K_S Hermitian unitary",
      float(np.max(np.abs(C @ C.conj() + I128))) == 0.0
      and float(np.max(np.abs(K_S - K_S.conj().T))) < 1e-12
      and float(np.max(np.abs(K_S @ K_S - I128))) < 1e-12)

MODS = {}
for fname in ("phase0_torsor_checks.py", "sig_b5_habitat_probe.py",
              "pt3_w229_membership_probe.py", "d1_coperator_build_probe.py",
              "torsion_arena_probe.py", "verify_torsion_arena_probe.py"):
    mod, dt = import_probe(fname)
    MODS[fname] = mod
    check("T", f"imported battery re-runs clean: {fname}", mod._exit_code == 0,
          f"exit {mod._exit_code}, {dt:.1f} s")

p0 = MODS["phase0_torsor_checks.py"]
tap = MODS["torsion_arena_probe.py"]
d1 = MODS["d1_coperator_build_probe.py"]

# planted-control reuse per the tree: the pipeline's power receipt, live
check("T", "Test N power receipt (phase0, live): R1 passes bit-exact; R2 and "
           "the PLANT K7 are killed at O(1) while the plant passes the Z/2 "
           "shadow test",
      p0.r1_lin == 0.0 and p0.r1_anti == 0.0 and p0.r2_res > 1.0
      and p0.p_res > 1.0 and p0.shadow7 < 1e-12,
      f"R1 ({p0.r1_lin:.1f}, {p0.r1_anti:.1f}); R2 {p0.r2_res:.2f}; "
      f"plant {p0.p_res:.2f}, shadow {p0.shadow7:.1e}")

res_linear = p0.res_linear          # the tree's Test N battery, imported
res_antilinear = p0.res_antilinear

# =============================================================================
print()
print("=" * 78)
print("K3 (Node 1, expected kill)  the Sigma bicomplex dressing")
print("=" * 78)


def Sigma(a, b):
    return 0.25 * (e[a] @ e[b] - e[b] @ e[a])


B_EVEN = 1.0 * Sigma(0, 9) + 0.7 * Sigma(1, 2)      # the a-priori named pin

r_k3 = res_linear(B_EVEN)
check("E", "K3 KILLED by Test N: the dressing generator is algebra-valued, "
           "commutator battery residual O(1) against R1's bit-exact 0.0 "
           "(pre-declared expected kill FIRES; no surprise survival)",
      r_k3 > 0.5, f"residual {r_k3:.2f} (R1 passes at 0.0; kill gate 0.5)")

jreal = float(np.max(np.abs(B_EVEN @ C - C @ B_EVEN.conj())))
check("E", "K3 feature attribution: Sigma dressing is J_quat-REAL exactly, "
           "so the K_S-forced symbol dressing i*W is J-ODD -- the same "
           "algebra-side / rep-weight-blind class as R2 and the plant "
           "(operator-grade Discovery 1 confirmed on the named pin)",
      jreal == 0.0, f"J-reality defect {jreal:.1e}")

# Section-7 guard: project onto the commutant BEFORE killing.
# Realify to 256x256; commutant basis {I, iI, J, iJ} realified.
def realify_linear(X):
    return np.block([[X.real, -X.imag], [X.imag, X.real]])


R_I = realify_linear(I128)
R_iI = realify_linear(1j * I128)
R_J = np.block([[C.real, C.imag], [C.imag, -C.real]])          # J = C conj
R_iJ = np.block([[-C.imag, C.real], [C.real, C.imag]])         # i(C conj)
BASIS = [R_I, R_iI, R_J, R_iJ]
gram = np.array([[np.sum(a * b) for b in BASIS] for a in BASIS])
gram_ok = float(np.max(np.abs(gram - 256.0 * np.eye(4)))) < 1e-9
R_W = realify_linear(B_EVEN)
comps = [float(np.sum(R_W * b)) / 256.0 for b in BASIS]
check("E", "K3 mixed-candidate guard (tree Section 7): the commutant "
           "projection of the dressing generator is EXACTLY ZERO on all four "
           "quaternion directions -- no hidden commutant part is being "
           "killed; the induced commutant transport is trivial, degree 0",
      gram_ok and max(abs(x) for x in comps) < 1e-12,
      "components " + str([round(x, 15) for x in comps]))

# =============================================================================
print()
print("=" * 78)
print("K4 (Node 3, highest prior)  the record-current bridge tensor")
print("=" * 78)

herm_def = max(float(np.max(np.abs(K_S @ e[a] - (K_S @ e[a]).conj().T)))
               for a in range(14))
sym_def = max(float(np.max(np.abs(
    C.conj().T @ K_S @ e[a] + (C.conj().T @ K_S @ e[a]).T))) for a in range(14))
check("T", "two EXACT identities of the frozen material, ALL 14 legs: "
           "(i) K_S e_a is Hermitian; (ii) C^dag K_S e_a is ANTISYMMETRIC",
      herm_def == 0.0 and sym_def == 0.0,
      f"herm defect {herm_def:.1e}, sym part {sym_def:.1e}")

UMU = [(1.0, 0.0), (1j, 0.0), (0.0, 1.0), (0.0, 1j)]   # I, iI, J, iJ


def comm_op(al, be, psi):
    """u = al*I + be*J acting on the carrier (J = C conj)."""
    return al * psi + be * (C @ psi.conj())


def bridge_tensor(psi, legs):
    """B[i, mu] = Re< u_mu psi, K_S e_{legs[i]} psi > -- the record-current
    bilinear with one commutant insertion (the only frozen model-space ->
    commutant contraction)."""
    B = np.zeros((4, 4))
    for i, b in enumerate(legs):
        w = K_S @ (e[b] @ psi)
        for mu, (al, be) in enumerate(UMU):
            B[i, mu] = float((comm_op(al, be, psi).conj() @ w).real)
    return B


P_plus = 0.5 * (I128 + K_S)
LEG_PINS = ((9, 0, 1, 2), (13, 3, 7, 8))               # both habitat pins
worst_dead, worst_alive_min = 0.0, np.inf
for legs in LEG_PINS:
    for kind in ("generic", "K_S-confined"):
        for _ in range(6):
            psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
            if kind == "K_S-confined":
                psi = P_plus @ psi
            psi /= np.linalg.norm(psi)
            B = bridge_tensor(psi, legs)
            worst_dead = max(worst_dead,
                             float(np.max(np.abs(B[:, 1:]))))   # commutant cols
            worst_alive_min = min(worst_alive_min,
                                  float(np.linalg.norm(B[:, 0])))
check("E", "K4 KILLED -- pre-declared condition 'B degenerate' FIRES: on both "
           "frozen leg pins and both fixture families (generic and "
           "K_S-confined draws) the three commutant columns (iI, J, iJ) of "
           "the bridge tensor vanish IDENTICALLY (forced by the two exact "
           "identities: Re<i psi, K_S e_a psi> needs a non-Hermitian kernel; "
           "the J/iJ columns are quadratic forms of an ANTISYMMETRIC "
           "bilinear kernel). B has rank <= 1: the record current couples "
           "the model index to the IDENTITY direction of the commutant only",
      worst_dead < 1e-13 and worst_alive_min > 1e-3,
      f"max |commutant cols| = {worst_dead:.1e}; "
      f"min ||J-column|| = {worst_alive_min:.3f}")

worst_inv = 0.0
for _ in range(8):
    psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
    psi /= np.linalg.norm(psi)
    q = RNG.standard_normal(4)
    q /= np.linalg.norm(q)
    upsi = comm_op(q[0] + 1j * q[1], q[2] + 1j * q[3], psi)
    for a in range(14):
        J0 = float((psi.conj() @ K_S @ e[a] @ psi).real)
        J1 = float((upsi.conj() @ K_S @ e[a] @ upsi).real)
        worst_inv = max(worst_inv, abs(J1 - J0))
check("E", "the record current is Sp(1)_comm-INVARIANT: J^a(u psi) = "
           "J^a(psi) to machine eps for random unit quaternions u, all 14 "
           "legs -- the kill is PLACEMENT-ROBUST (no contraction of the "
           "current, one-slot, two-slot, or kernel-inserted, can see "
           "commutant motion) AND K1's naturality prior collapses: every "
           "commutant element conserves J^a exactly, so 'transport by "
           "J^a-conservation' is underdetermined by exactly the torsor group",
      worst_inv < 1e-12, f"worst defect {worst_inv:.1e}")

check("E", "MS consequence: the induced transport family is CONSTANT "
           "(commutant part of the bridge = 0), so its deck restriction is "
           "+I, not the verified co-flip -I, and its degree is c = 0 -> "
           "k = 64*0 = 0, the ZERO class (Test W kill as well): all three "
           "MS clauses fail through this bridge",
      worst_dead < 1e-13 and tap.order24(0 % 24) == 1,
      "order(J(0)) = 1 (trivial)")

# detectability controls: the construction CAN see commutant couplings
psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
psi /= np.linalg.norm(psi)


def mu_columns(X, psi):
    return np.array([float((comm_op(al, be, psi).conj() @ X @ psi).real)
                     for (al, be) in UMU])


c1 = mu_columns(e[9], psi)                    # non-Hermitian kernel
c2 = mu_columns(K_S @ e[0] @ e[1] @ e[9], psi)  # K_S-dressed grade-3 kernel
check("F", "detectability control (plant-analog for the kill direction): "
           "synthetic non-record kernels light up the commutant columns at "
           "O(0.1) -- the tensor construction has demonstrated power, so the "
           "zero is a property of the record current itself, not of the "
           "probe", float(np.max(np.abs(c1[1:]))) > 0.01
      and float(np.max(np.abs(c2[1:]))) > 0.01,
      f"e_9 cols {np.round(c1, 3)}; K_S e_0 e_1 e_9 cols {np.round(c2, 3)}")

# =============================================================================
print()
print("=" * 78)
print("K2 (Node 2)  the C-weld ambiguity shape at the D1 degenerate anchor")
print("=" * 78)

# carrier grade (d1's faithful-miniature receipt: Casimir scalar, K_S
# balanced (+64,-64); canonical admissible C at the anchor is K_S itself)
G0 = K_S @ K_S                                          # = I: C = K_S admissible
check("T", "canonical admissible C at the carrier anchor: C = K_S has "
           "C^2 = I and B.C = K_S.K_S = I > 0 ([C, Casimir] = 0 trivially "
           "-- the Casimir is scalar, d1's carrier receipt)",
      float(np.max(np.abs(G0 - I128))) < 1e-12)

P_minus = 0.5 * (I128 - K_S)
n_dirs = 8
tangents = []
adm_ok = True
for k in range(n_dirs):
    Z = RNG.standard_normal((128, 128)) + 1j * RNG.standard_normal((128, 128))
    X = P_plus @ Z @ P_minus
    X = X + X.conj().T                                  # Hermitian, {X, K_S} = 0
    X /= np.linalg.norm(X)
    w, V = np.linalg.eigh(X)
    T = V @ np.diag(np.exp(0.5 * w)) @ V.conj().T       # expm(X/2), numpy-only
    Ti = V @ np.diag(np.exp(-0.5 * w)) @ V.conj().T
    Cs = T @ K_S @ Ti
    Gs = K_S @ Cs
    Gs = 0.5 * (Gs + Gs.conj().T)
    adm_ok = adm_ok and float(np.max(np.abs(Cs @ Cs - I128))) < 1e-9 \
        and float(np.linalg.eigvalsh(Gs).min()) > 0.0 \
        and float(np.linalg.norm(Cs - K_S)) > 0.3
    tangents.append((X @ K_S - K_S @ X).flatten())      # dC/ds at s = 0
rank_t = np.linalg.matrix_rank(np.array(tangents), tol=1e-8)
check("E", "the admissible set at the anchor is a LARGE continuum: 8 random "
           "Hermitian K_S-anticommuting directions X all give admissible "
           "C_s = e^{sX/2} K_S e^{-sX/2} != K_S (C_s^2 = I, B.C_s > 0), with "
           "8 INDEPENDENT tangent directions (the full parameter space is "
           "the 8192-real-dimensional off-diagonal Hermitian block "
           "U(64,64)/(U(64)xU(64)); dim sp(1) = 3)",
      adm_ok and rank_t == n_dirs, f"tangent rank {rank_t}/{n_dirs}")

d_j = float(np.max(np.abs(C @ K_S.conj() - K_S @ C)))
check("E", "K2 KILLED -- pre-declared condition FIRES on both prongs: "
           "(i) the Sp(1)_comm conjugation orbit through the canonical C is "
           "a SINGLE POINT (e^{i theta} is conjugation-central; J commutes "
           "with K_S exactly), so the admissible set is vastly bigger than "
           "one commutant orbit; (ii) NO orbit is free: U(1) inside "
           "Sp(1)_comm conjugates every complex-linear C trivially. The D1 "
           "non-uniqueness is symmetric-space freedom, NOT Sp(1)-torsor "
           "freedom", d_j == 0.0,
      f"J-conjugation defect on K_S = {d_j:.1e}; orbit dim 0 vs continuum")

# toy corroboration on the frozen d1 delta = 0 fixture (the 6-dim pair block)
B9 = d1.build_B()
S6 = np.zeros((6, 6), dtype=complex)                    # C_swap on pair block
for i in range(3):
    S6[i, 3 + i] = S6[3 + i, i] = 1.0
B6 = S6.copy()                                          # B restricted = swap too
gens = []
for i in range(6):
    for j in range(6):
        for v in (1.0, 1j):
            A = np.zeros((6, 6), dtype=complex)
            A[i, j] += v
            A = A - A.conj().T                          # anti-Hermitian
            if np.linalg.norm(A) > 1e-12:
                gens.append(B6 @ A)                     # X^dag B6 + B6 X = 0
ad_vecs = [np.concatenate([(X @ S6 - S6 @ X).real.flatten(),
                           (X @ S6 - S6 @ X).imag.flatten()]) for X in gens]
rank_ad = np.linalg.matrix_rank(np.array(ad_vecs), tol=1e-8)
check("E", "toy corroboration (frozen d1 delta = 0 pair block): the "
           "K-isometry orbit of the canonical weld C_swap has dimension 18 "
           "= dim U(3,3)/(U(3)xU(3)) -- the d1 'admissible continuum' is an "
           "18-real-dimensional symmetric space at toy grade, not a "
           "3-dimensional Sp(1) orbit",
      rank_ad == 18 and np.allclose(B9[3:, 3:], B6.real),
      f"ad-rank {rank_ad} (sp(1) would give <= 3)")

# =============================================================================
print()
print("=" * 78)
print("BK  the k = 64c general-m bookkeeping, re-derived at control grade")
print("=" * 78)

wzw = tap.wzw_winding
qr = tap.quat_right
sph = tap.sphere
EPS1 = tap.EPS1

w_ctrl = wzw(lambda p, t, f: qr(sph(p, t, f), EPS1), 10)
check("T", "control: 1-quaternion right multiplication winds +-2 "
           "(k = +-1), matching the frozen E2 receipt",
      abs(abs(w_ctrl) - 2.0) < 0.05, f"W = {w_ctrl:+.4f}")


def padded(p, t, f):
    """q(v) on the first H summand, IDENTITY on the second (Sp(1) corner
    of Sp(2)): multiplicity padding must ride identity."""
    out = np.eye(8, dtype=complex)
    out[:4, :4] = qr(sph(p, t, f), EPS1)
    return out


w_pad = wzw(padded, 10)
check("E", "multiplicity padding rides identity: the Sp(1)-corner family in "
           "Sp(2) still winds +-2 -- extra quaternionic multiplicity "
           "contributes ZERO, so k = 64c is m-INDEPENDENT (the 64 comes from "
           "the frozen irrep block count, never from m)",
      abs(abs(w_pad) - 2.0) < 0.05 and abs(w_pad - w_ctrl) < 0.05,
      f"W = {w_pad:+.4f}")


def doubled(p, t, f):
    out = np.zeros((8, 8), dtype=complex)
    Q = qr(sph(p, t, f), EPS1)
    out[:4, :4] = Q
    out[4:, 4:] = Q
    return out


w_dbl = wzw(doubled, 10)
w_sq = wzw(lambda p, t, f: qr(sph(p, t, f), EPS1) @ qr(sph(p, t, f), EPS1), 10)
check("E", "additivity in the class c, two routes: the diagonal Sp(1) in "
           "Sp(2) winds +-4 (Dynkin additivity across blocks) and the "
           "pointwise-squared family winds +-4 (group multiplication adds "
           "pi_3 classes) -- k = 64c is LINEAR in c",
      abs(abs(w_dbl) - 4.0) < 0.1 and abs(abs(w_sq) - 4.0) < 0.1,
      f"W(diag) = {w_dbl:+.4f}, W(square) = {w_sq:+.4f}")

order24 = tap.order24
ok_arith = all(
    (64 * c) % 64 == 0 and ((64 * c) % 2 ** 6 == 0)
    and ((order24((64 * c) % 24) == 3) == (c % 3 != 0)) for c in range(1, 200))
check("E", "arithmetic leg: v2(64c) >= 6 for every c, and order(J(64c)) = 3 "
           "iff 3-not-|c (c = 1..199) -- the tree's automatic-v2 note and "
           "Test W arithmetic re-verified; the general-m bookkeeping is "
           "SUSTAINED", ok_arith)

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print(f"HEADLINE: K3 KILLED (Test N, expected; commutant projection exactly "
      f"0), K4 KILLED (bridge tensor rank 1: the record current is "
      f"Sp(1)_comm-blind by two exact identities -- deck +I, degree 0), "
      f"K2 KILLED (admissible-C set is symmetric-space-sized, commutant "
      f"orbit is a point, no free orbit); k = 64c general-m bookkeeping "
      f"SUSTAINED. MS NOT established; no survivor. "
      f"{nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s)")
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
