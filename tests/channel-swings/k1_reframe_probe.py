#!/usr/bin/env python3
"""Phase-1 close: K1 (Node 4) formal execution + the pre-declared REFRAME PASS.

CHANNEL: ID-1 torsor identification -- the two outstanding obligations of the
         kill sequence (explorations/torsor-k-sequence-2026-07-20.md, commit
         6a285c0) before any program-level conclusion is permitted.
DESIGN:  explorations/phase0-torsor-identification-tree-2026-07-20.md (the
         Node-4 kill/survive conditions and the Section-4 exhaustion-clause
         reframe pass BIND this probe; no condition altered in flight).
DIRECTED: Joe direct chat, 2026-07-20 (Phase 1 close: K1 + mandatory reframe
         pass; kill-gets-a-defense-attorney discipline).
STATUS:  exploration tier; conditional (R0_COND framed-reading fork + (9,5)
         H-class); no claim/canon/posture movement.

MACHINERY REUSE. phase0_torsor_checks.py is imported live (stdout captured,
SystemExit(0) asserted): it supplies the Test N battery + its power receipt
(R1 bit-exact pass; R2 and the plant K7 killed), order24, and the frozen
fixtures. Degree computation here is NEW machinery (signed preimage counting
on an exactly-evaluated cubic map) and is power-validated inside this probe
on two maps of known degree (+1 and +3) before any kill is read from it.

WHAT IS TESTED.

  K1 (Node 4) -- transport by record-current conservation, executed on its
      OWN pre-declared conditions (not by importing K4's verdict):
      (i) the conservation rule is non-vacuous on the core family (the spin
          lift moves the current at O(0.5));
      (ii) K1's own test: ON K1's family states, every commutant unitary
          moves J^a by < 1e-12, so the conservation equation is INFEASIBLE
          wherever the current moved and solved by the FULL group Sp(1)_comm
          wherever it did not: the rule locates a coset, never a map;
      (iii) the intertwining reading dies by the same exact relations
          (commutant conjugation fixes every K_S e_a at 0.0 while the family
          rotates them at O(1));
      (iv) the only other in-row variant (conserve the H-valued pairing
          h(Psi,Psi)) is VACUOUS: its Im H part is identically zero;
      (v) therefore the only posit-free section is constant: deck +I (not
          the verified co-flip -I), degree c = 0, k = 0 -> the pre-declared
          kill 'degree 0' FIRES.

  REFRAME (a) -- the one live door: higher-grade (grade-3) dressed transport.
      Native provenance candidate: the pin-plane Hodge duals of the record
      legs (K_S e_hat, e_hat = product of the other three frozen pin legs),
      i.e. the SELF-DUAL record bridge K_S(e_i + lambda * e_hat_i). Receipts:
      the kill-sequence detectability control (K_S e_0 e_1 e_9 responds at
      O(0.1)) and operator-grade-end Discovery 1 (grade-3 torsion-type terms
      are the K-honest J-odd sector). Findings, each machine-checked:
        - the K4 protection identities are GRADE-1-SPECIFIC: both fail at
          maximal defect on every pin-dual; the duals reach the commutant;
        - exact type split: grade-3 duals are ANTI-Hermitian, so a pure
          grade-3 bridge has identically zero real column (rank <= 3), and
          pure grade-1 has zero commutant columns (rank 1, K4): only the
          self-dual mix is full-quaternion -- and it IS full-rank at generic
          states with EXACT co-flip deck restriction q(-v) = -q(v);
        - KILL 1 (class not native): the exact integer degree of the induced
          transport is fixture- and pin-dependent (|c| = 1 AND |c| = 3 both
          witnessed, larger odd values occur; frozen-variant sign(det) is a
          coin flip over 40 draws/pin -- the Section-5 residue hope dies
          with it), while lambda-independent within a draw: the instability
          belongs to the state posit, so any class selection costs
          import >= 1;
        - KILL 2 (Test W inside the family): the c = 3 members give
          k = 192 = 0 mod 24, the ZERO class (order 1, not 3);
        - KILL 3 (third exact identity, K_S-parity): every pin-dual carrying
          the single negative-signature pin leg ANTICOMMUTES with K_S at 0.0,
          so on K_S-confined states the bridge collapses to rank exactly 2:
          the record habitat itself refuses the grade-3 completion.

  REFRAME (b) -- sharpened demand (the pass's positive output): the frozen
      kernel inventory splits exactly: commutant-blind (H-self-adjoint,
      grade-1 record; Sigma with commutant projection 0) vs commutant-
      reaching but habitat-collapsing (pin-duals). NO frozen kernel passes
      both admission gates (reach the commutant AND stay nondegenerate on
      the confined habitat) -- the two-gate demand is the new testable
      statement fed to the B.5 ledger.

NONCLAIMS. No MS construction; R0_COND untouched; no claim/canon/posture
movement; clause 6(a) satisfaction is recorded at exploration tier only --
line-closure verdicts stay Joe-gated.
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
G = bridge.cl95.jordan_wigner_gammas(7)
I128 = np.eye(128, dtype=complex)
C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]      # J_quat = C . conj (canon)
K_S = e[0].copy()
for i in range(1, 9):
    K_S = K_S @ e[i]                                # K_S = e_0 ... e_8
RNG = np.random.default_rng(20260720)

herm_def = max(float(np.max(np.abs(K_S @ e[a] - (K_S @ e[a]).conj().T)))
               for a in range(14))
sym_def = max(float(np.max(np.abs(
    C.conj().T @ K_S @ e[a] + (C.conj().T @ K_S @ e[a]).T))) for a in range(14))
check("T", "fixtures: J_quat^2 = -1 exact; K_S Hermitian unitary; the two "
           "K4 identities re-verified at 0.0 on all 14 legs (premises here)",
      float(np.max(np.abs(C @ C.conj() + I128))) == 0.0
      and float(np.max(np.abs(K_S - K_S.conj().T))) < 1e-12
      and float(np.max(np.abs(K_S @ K_S - I128))) < 1e-12
      and herm_def == 0.0 and sym_def == 0.0,
      f"herm {herm_def:.1e}, antisym {sym_def:.1e}")

p0, dt0 = import_probe("phase0_torsor_checks.py")
check("T", "imported battery re-runs clean: phase0_torsor_checks.py "
           "(Test N power: R1 bit-exact pass; R2 and the plant K7 killed "
           "while the plant passes the Z/2 shadow)",
      p0._exit_code == 0 and p0.r1_lin == 0.0 and p0.r1_anti == 0.0
      and p0.r2_res > 1.0 and p0.p_res > 1.0 and p0.shadow7 < 1e-12,
      f"exit {p0._exit_code}, {dt0:.1f} s; R2 {p0.r2_res:.2f}, "
      f"plant {p0.p_res:.2f}, shadow {p0.shadow7:.1e}")
order24 = p0.order24

# the core family: the frozen spin lift on both habitat leg pins
PINS = ((9, 0, 1, 2), (13, 3, 7, 8))
QFAM = {PINS[0]: [G[9] @ G[k] for k in (0, 1, 2)],
        PINS[1]: [G[13] @ G[k] for k in (3, 7, 8)]}


def lam_v(v, pin):
    Q = QFAM[pin]
    return v[0] * I128 + v[1] * Q[0] + v[2] * Q[1] + v[3] * Q[2]


vt = np.array([0.5, 0.5, 0.5, 0.5])
fam_ok = True
for pin in PINS:
    L = lam_v(vt, pin)
    fam_ok = fam_ok and float(np.max(np.abs(L @ L.conj().T - I128))) < 1e-12 \
        and float(np.max(np.abs(lam_v(-vt, pin) + L))) == 0.0
check("T", "core family (both pins): the spin-lift family is unitary with "
           "EXACT deck oddness Lambda(-v) = -Lambda(v) (the verified co-flip "
           "shadow; basepoint Lambda(v0) = I)",
      fam_ok and float(np.max(np.abs(lam_v(np.array([1.0, 0, 0, 0]), PINS[0])
                                     - I128))) == 0.0)

UMU = [(1.0, 0.0), (1j, 0.0), (0.0, 1.0), (0.0, 1j)]   # I, iI, J, iJ


def comm_op(al, be, psi):
    """u = al*I + be*J acting on the carrier (J = C conj)."""
    return al * psi + be * (C @ psi.conj())


def Jcur(psi):
    return np.array([float((psi.conj() @ K_S @ e[a] @ psi).real)
                     for a in range(14)])


# =============================================================================
print()
print("=" * 78)
print("K1 (Node 4)  transport by record-current conservation, own conditions")
print("=" * 78)

psi_base = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
psi_base /= np.linalg.norm(psi_base)
J0 = Jcur(psi_base)
V_SAMPLE = [np.array([0.6, 0.8, 0.0, 0.0]), np.array([0.5, 0.5, 0.5, 0.5]),
            np.array([0.0, 0.0, 0.6, -0.8])]
D_min, D_max, worst_move = np.inf, 0.0, 0.0
for pin in PINS:
    for v in V_SAMPLE:
        psiv = lam_v(v, pin) @ psi_base
        D = float(np.max(np.abs(Jcur(psiv) - J0)))
        D_min, D_max = min(D_min, D), max(D_max, D)
        for _ in range(20):
            q = RNG.standard_normal(4)
            q /= np.linalg.norm(q)
            upsi = comm_op(q[0] + 1j * q[1], q[2] + 1j * q[3], psiv)
            worst_move = max(worst_move,
                             float(np.max(np.abs(Jcur(upsi) - Jcur(psiv)))))
check("E", "K1 rule is NON-VACUOUS on its core family: the spin lift moves "
           "the record current at O(0.2-0.5) at generic v (both pins) -- "
           "there is a real conservation equation to solve",
      D_min > 0.1, f"defect range [{D_min:.3f}, {D_max:.3f}]")

check("E", "K1's OWN TEST fires: ON K1's family states, every commutant "
           "unitary moves J^a by < 1e-12 (120 random u across both pins and "
           "all sampled v), so the conservation equation J^a(u Psi_v) = "
           "J^a(Psi_0) is INFEASIBLE wherever the current moved (defect "
           "unreachable by the whole group) and is solved by ALL of "
           "Sp(1)_comm wherever it did not (v = +-v0): the rule locates the "
           "coset Sp(1)_comm, never a map -- this is the K4 invariance "
           "identity executed AS K1's decisive test, on K1's own states",
      worst_move < 1e-12 and D_max > 0.25,
      f"worst commutant motion {worst_move:.1e} vs defect O({D_max:.1f})")

tw_J = max(float(np.max(np.abs(K_S @ e[a] @ C - C @ (K_S @ e[a]).conj())))
           for a in range(14))
rot_def = 0.0
for pin in PINS:
    L = lam_v(vt / np.linalg.norm(vt), pin)
    rot_def = max(rot_def, max(float(np.max(np.abs(
        L.conj().T @ K_S @ e[a] @ L - K_S @ e[a]))) for a in range(14)))
check("E", "the INTERTWINING reading of K1 dies by the same exact relations: "
           "commutant conjugation fixes every current kernel K_S e_a exactly "
           "(twisted-commute defect 0.0 for J; e^{i theta} trivially), while "
           "the core family rotates the kernels at O(1) -- no commutant "
           "unitary intertwines the transported current with the frozen one",
      tw_J == 0.0 and rot_def > 1.0,
      f"[J, K_S e_a] twisted defect {tw_J:.1e}; family rotation {rot_def:.2f}")

worst_pair = 0.0
for _ in range(6):
    psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
    psi /= np.linalg.norm(psi)
    w = np.array([float((comm_op(al, be, psi).conj() @ psi).real)
                  for (al, be) in UMU])
    worst_pair = max(worst_pair, float(np.max(np.abs(w[1:]))))
anti_C = float(np.max(np.abs(C + C.T)))
check("E", "the only other in-row variant (conserve the H-valued pairing "
           "h(Psi,Psi)) is VACUOUS: the Im H part of the pairing is "
           "IDENTICALLY zero (iI component = Re(-i|Psi|^2) = 0; J/iJ "
           "components are quadratic forms of the ANTISYMMETRIC kernel C) "
           "-- the quaternionic norm form is real, so 'conserve it' selects "
           "nothing", worst_pair < 1e-14 and anti_C == 0.0,
      f"max Im-part {worst_pair:.1e}; |C + C^T| = {anti_C:.1e}")

check("E", "K1 KILLED on its pre-declared condition: the only posit-free "
           "section of the solution correspondence is the constant u = I "
           "(deck restriction +I, NOT the verified co-flip -I), degree "
           "c = 0, k = 64*0 = 0, order(J(0)) = 1 -- the 'degree 0' horn of "
           "Node 4's kill condition FIRES; the gauge-fixed variant pays the "
           "row's own +1 posit (import >= 1 on this route). No in-row "
           "variant escapes: the modified-current variant (non-H-self-"
           "adjoint kernel) is a NEW object and is exactly reframe (a) below",
      order24(0 % 24) == 1 and worst_move < 1e-12,
      "order(J(0)) = 1 (trivial class)")

# =============================================================================
print()
print("=" * 78)
print("REFRAME (a)  the grade-3 / self-dual record bridge (the one live door)")
print("=" * 78)


def duals(pin):
    """Pin-plane Hodge duals: for each pin leg, the product of the other
    three pin legs (in listed order; orientation freedom is the honest +-)."""
    out = []
    for i in range(4):
        rest = [pin[j] for j in range(4) if j != i]
        out.append(e[rest[0]] @ e[rest[1]] @ e[rest[2]])
    return out


def kernels(pin, lc):
    DU = duals(pin)
    return [K_S @ (e[pin[i]] + lc * DU[i]) for i in range(4)]


def mu_cols(M, psi):
    w = M @ psi
    return np.array([float((comm_op(al, be, psi).conj() @ w).real)
                     for (al, be) in UMU])


def Bfull(psi, KER):
    return np.array([mu_cols(M, psi) for M in KER])


worst_h, worst_s, worst_ah, worst_col = 0.0, 0.0, 0.0, np.inf
for pin in PINS:
    for D3 in duals(pin):
        M = K_S @ D3
        worst_h = max(worst_h, 2.0 - float(np.max(np.abs(M - M.conj().T))))
        worst_s = max(worst_s, 2.0 - float(np.max(np.abs(
            C.conj().T @ M + (C.conj().T @ M).T))))
        worst_ah = max(worst_ah, float(np.max(np.abs(M + M.conj().T))))
        best = 0.0
        for _ in range(4):
            psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
            psi /= np.linalg.norm(psi)
            best = max(best, float(np.max(np.abs(mu_cols(M, psi)[1:]))))
        worst_col = min(worst_col, best)
check("E", "the K4 protection theorem is GRADE-1-SPECIFIC: on every pin-dual "
           "kernel K_S e_hat (both pins) BOTH protection identities fail at "
           "maximal defect (Hermiticity and C^dag-antisymmetry defects = 2.0) "
           "and the commutant columns respond at O(0.1) -- commutant-"
           "DETECTING kernels exist in the frozen algebra (the defense's "
           "input, extended from the kill-sequence control to the full "
           "dual family)",
      worst_h < 1e-12 and worst_s < 1e-12 and worst_col > 0.01,
      f"identity defects 2.0 exactly; weakest dual's strongest column "
      f"{worst_col:.3f}")

check("E", "exact type split (why only the SELF-DUAL mix can work): every "
           "pin-dual K_S e_hat is ANTI-Hermitian at 0.0, so a pure grade-3 "
           "bridge has identically zero real column (rank <= 3, misses the "
           "identity direction), while pure grade-1 has zero commutant "
           "columns (rank 1, K4): the full-quaternion completion is "
           "K_S(e_i + lambda e_hat_i), whose lambda and pin orientation are "
           "IMPORTS (priced in the companion exploration)",
      worst_ah == 0.0, f"anti-Hermiticity defect {worst_ah:.1e}")

P_plus = 0.5 * (I128 + K_S)
# dedicated deterministic stream for the degree study, decoupled from the
# ambient fixture stream so the draw set is stable under probe edits
RNG_DEG = np.random.default_rng(20260721)
GEN_DRAWS = []
for _ in range(4):
    psi = RNG_DEG.standard_normal(128) + 1j * RNG_DEG.standard_normal(128)
    psi /= np.linalg.norm(psi)
    GEN_DRAWS.append(psi)

ok_rank, det_min, cond_max, odd_worst, even_min = True, np.inf, 0.0, 0.0, np.inf
v_probe = np.array([0.36, 0.48, 0.6, -0.52])
v_probe /= np.linalg.norm(v_probe)
for pin in PINS:
    KER = kernels(pin, 1.0)
    for psi in GEN_DRAWS:
        B = Bfull(psi, KER)
        det_min = min(det_min, abs(np.linalg.det(B)))
        cond_max = max(cond_max, float(np.linalg.cond(B)))
        # deck restriction of the pointwise transport: quadratic in Psi, odd in v
        q_p = v_probe @ Bfull(lam_v(v_probe, pin) @ psi, KER)
        q_m = (-v_probe) @ Bfull(lam_v(-v_probe, pin) @ psi, KER)
        odd_worst = max(odd_worst, float(np.max(np.abs(q_p + q_m))))
        # the mixed (one-basepoint-slot) contraction is deck-EVEN: excluded
        def q_mixed(vv):
            Wm = np.array([[float((comm_op(al, be, psi).conj()
                                   @ (KER[i] @ (lam_v(vv, pin) @ psi))).real)
                            for (al, be) in UMU] for i in range(4)])
            return vv @ Wm
        qm_p, qm_m = q_mixed(v_probe), q_mixed(-v_probe)
        even_worst = float(np.max(np.abs(qm_p - qm_m)))
        even_min = min(even_min, float(np.linalg.norm(qm_p)))
        if even_worst > 0.0:
            even_min = -1.0                            # evenness must be exact
check("E", "the self-dual bridge is REAL, not a strawman: full-rank at "
           "generic states (both pins, 4 draws) with EXACT co-flip deck "
           "restriction q(-v) = -q(v) (quadratic in Psi, odd in v -- the "
           "only deck-compatible contraction shape: the one-basepoint-slot "
           "variant is exactly deck-EVEN, a nonzero map with q(-v) = +q(v), "
           "and is excluded by the verified co-flip)",
      det_min > 1e-9 and cond_max < 1e6 and odd_worst == 0.0
      and even_min > 1e-3,
      f"min |det| {det_min:.1e}, max cond {cond_max:.1f}, deck-odd defect "
      f"{odd_worst:.1e}, mixed-variant norm {even_min:.3f} (evenness exact)")


# ---- exact-cubic evaluation + signed preimage degree machinery -------------
def forms(psi0, pin, lc):
    """A[i,mu]: 4x4 real symmetric forms with B[i,mu](v) = v^T A v along the
    family, so q_mu(v) = sum_i v_i (v^T A_imu v) EXACTLY (cubic in v)."""
    Q = QFAM[pin]
    P = np.stack([psi0, Q[0] @ psi0, Q[1] @ psi0, Q[2] @ psi0], axis=1)
    KER = kernels(pin, lc)
    U = [P, 1j * P, C @ P.conj(), 1j * (C @ P.conj())]
    A = np.zeros((4, 4, 4, 4))
    for i in range(4):
        W = KER[i] @ P
        for mu in range(4):
            Ar = (U[mu].conj().T @ W).real
            A[i, mu] = 0.5 * (Ar + Ar.T)
    return A


def qv(v, A):
    quad = np.einsum('a,imab,b->im', v, A, v)
    return v @ quad


def jac(v, A):
    quad = np.einsum('a,imab,b->im', v, A, v)
    Av = np.einsum('imab,b->ima', A, v)
    return quad.T + 2.0 * np.einsum('i,imb->mb', v, Av)


def tangent_basis(v):
    _, _, Vt = np.linalg.svd(v.reshape(1, 4))
    T = Vt[1:].T
    if np.linalg.det(np.column_stack([v, T])) < 0:
        T[:, 0] = -T[:, 0]
    return T


def degree_by_preimage(qfun, jfun, w, nstarts=3000, seed=3):
    """Exact integer degree of v -> qfun(v)/|qfun(v)| by signed preimage
    count over the regular value w. Deterministic."""
    rng = np.random.default_rng(seed)
    Pw = np.eye(4) - np.outer(w, w)
    roots = []
    V = rng.standard_normal((nstarts, 4))
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    for v0 in V:
        v = v0.copy()
        ok = False
        for _ in range(50):
            q = qfun(v)
            r = Pw @ q
            if np.linalg.norm(r) < 1e-13:
                ok = True
                break
            T = tangent_basis(v)
            try:
                s, *_ = np.linalg.lstsq(Pw @ jfun(v) @ T, -r, rcond=None)
            except np.linalg.LinAlgError:
                break
            if np.linalg.norm(s) > 0.8:
                s *= 0.8 / np.linalg.norm(s)
            v = v + T @ s
            v /= np.linalg.norm(v)
        if not ok:
            continue
        q = qfun(v)
        if q @ w <= 0 or np.linalg.norm(q) < 1e-8:
            continue
        if any(np.linalg.norm(v - r0) < 1e-6 for r0 in roots):
            continue
        roots.append(v)
    deg = 0
    for v in roots:
        T = tangent_basis(v)
        q = qfun(v)
        nq = np.linalg.norm(q)
        Jm = jfun(v)
        cols = []
        for k in range(3):
            dq = Jm @ T[:, k]
            dqh = (dq - (dq @ q) * q / nq ** 2) / nq
            cols.append(dqh - (dqh @ w) * w)
        deg += int(np.sign(np.linalg.det(np.column_stack([w] + cols))))
    return deg, len(roots)


W1 = np.array([0.3, -0.5, 0.6, 0.55])
W1 /= np.linalg.norm(W1)
W2 = np.array([-0.7, 0.1, 0.2, 0.68])
W2 /= np.linalg.norm(W2)


def hamilton(p, q):
    return np.array([
        p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3],
        p[0] * q[1] + p[1] * q[0] + p[2] * q[3] - p[3] * q[2],
        p[0] * q[2] - p[1] * q[3] + p[2] * q[0] + p[3] * q[1],
        p[0] * q[3] + p[1] * q[2] - p[2] * q[1] + p[3] * q[0]])


def q_id(v):
    return v


def j_id(v):
    return np.eye(4)


def q_cube(v):
    return hamilton(v, hamilton(v, v))


def j_cube(v):
    h = 1e-6
    J = np.zeros((4, 4))
    for b in range(4):
        vp = v.copy()
        vm = v.copy()
        vp[b] += h
        vm[b] -= h
        J[:, b] = (q_cube(vp) - q_cube(vm)) / (2 * h)
    return J


d_id1, n_id1 = degree_by_preimage(q_id, j_id, W1)
d_id2, _ = degree_by_preimage(q_id, j_id, W2)
d_c1, n_c1 = degree_by_preimage(q_cube, j_cube, W1)
d_c2, _ = degree_by_preimage(q_cube, j_cube, W2)
check("F", "degree machinery POWER (validated before any kill is read from "
           "it): the signed-preimage counter certifies the identity map at "
           "degree +1 and the quaternion-cube map at degree +3, on two "
           "independent regular values each -- it distinguishes exactly the "
           "classes at stake (1 vs 3)",
      d_id1 == 1 and d_id2 == 1 and d_c1 == 3 and d_c2 == 3,
      f"id: {d_id1},{d_id2} ({n_id1} preimages); cube: {d_c1},{d_c2} "
      f"({n_c1} preimages)")

b1_col = 0.0
for a in PINS[0]:
    b1_col = max(b1_col, float(np.max(np.abs(
        mu_cols(K_S @ e[a], GEN_DRAWS[0])[1:]))))
check("F", "kill-direction control (live plant-analog): the SAME bridge "
           "pipeline on pure grade-1 record kernels reads commutant columns "
           "< 1e-13 -- the construction distinguishes the protected sector "
           "from the detecting sector; the grade-3 responses above are not "
           "an artifact", b1_col < 1e-13, f"max grade-1 column {b1_col:.1e}")

# the decisive computation: exact integer degrees of the pointwise transport
DEG = {}
for pin, ndr in ((PINS[0], 4), (PINS[1], 3)):
    for k in range(ndr):
        A = forms(GEN_DRAWS[k], pin, 1.0)
        d1, n1 = degree_by_preimage(lambda v: qv(v, A), lambda v: jac(v, A), W1)
        d2, n2 = degree_by_preimage(lambda v: qv(v, A), lambda v: jac(v, A), W2)
        DEG[(pin, k)] = (d1, d2, n1, n2)
        print(f"       pointwise degree pin{pin} draw{k}: "
              f"deg(w1) = {d1} ({n1} preimages), deg(w2) = {d2} ({n2})")
lam_degs = []
for lc in (0.5, 2.0):
    Al = forms(GEN_DRAWS[0], PINS[0], lc)
    dl, _ = degree_by_preimage(lambda v: qv(v, Al), lambda v: jac(v, Al), W1)
    lam_degs.append(dl)
consistent = all(d1 == d2 for (d1, d2, _, _) in DEG.values())
all_odd = all(d1 % 2 == 1 for (d1, _, _, _) in DEG.values())
absvals = sorted({abs(d1) for (d1, _, _, _) in DEG.values()})
d_ref = DEG[(PINS[0], 0)][0]
check("E", "REFRAME (a) KILL 1 -- the class is NOT native: the exact integer "
           "degree of the pointwise self-dual transport is target-consistent "
           "and odd on every fixture (the deck-oddness guarantees odd degree "
           "by Borsuk-Ulam -- existence of SOME odd class is free, exactly "
           "as K6 said) but the class SCATTERS with the fixture state and "
           "the pin: |c| = 1 AND |c| = 3 are both witnessed (and larger odd "
           "values occur), while lambda-independent within a draw -- the "
           "instability belongs to the state posit, so no Psi_0-independent "
           "class exists and any selection costs import >= 1",
      consistent and all_odd and 1 in absvals and 3 in absvals
      and lam_degs == [d_ref, d_ref],
      "degrees " + ", ".join(f"pin{k[0][0]}/draw{k[1]}: {d[0]:+d}"
                             for k, d in DEG.items())
      + f"; lambda 0.5/2.0 -> {lam_degs}")

signs_ok = True
sign_detail = []
for pin in PINS:
    KER = kernels(pin, 1.0)
    signs = []
    for _ in range(40):
        psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
        psi /= np.linalg.norm(psi)
        signs.append(np.sign(np.linalg.det(Bfull(psi, KER))))
    plus, minus = signs.count(1.0), signs.count(-1.0)
    sign_detail.append(f"pin{pin[0]}: +{plus}/-{minus}")
    signs_ok = signs_ok and min(plus, minus) >= 10
check("E", "the tree's Section-5 residue hope dies too: the sign of the "
           "identification (the {8nu vs 16nu} residue capability -- 'B is "
           "orientation-sensitive, so the bridge might pin the orientation') "
           "is a COIN FLIP of the fixture state over 40 generic draws on "
           "each pin: the bridge does NOT natively fix an orientation; the "
           "honest +- stays honest",
      signs_ok, "; ".join(sign_detail))

check("E", "REFRAME (a) KILL 2 -- Test W fires INSIDE the family: the "
           "witnessed |c| = 3 members give k = 64*3 = 192 = 0 mod 24, the "
           "ZERO class (order 1, not 3); no native rule selects the order-3-"
           "delivering members over them (|c| = 5 members would deliver "
           "order 3, but selection is exactly what nativity cannot supply)",
      3 in absvals and order24((64 * 3) % 24) == 1
      and order24(64 % 24) == 3 and order24((64 * 5) % 24) == 3,
      "order(J(192)) = 1; order(J(64)) = order(J(320)) = 3")

par_ok = True
rank_ok = True
struct_worst = 0.0
for pin in PINS:
    DU = duals(pin)
    for i in range(4):
        M = K_S @ DU[i]
        anti = float(np.max(np.abs(M @ K_S + K_S @ M)))
        comm = float(np.max(np.abs(M @ K_S - K_S @ M)))
        if pin[i] >= 9:                      # dual OF the negative leg
            par_ok = par_ok and comm == 0.0
        else:                                # dual CONTAINS the negative leg
            par_ok = par_ok and anti == 0.0
    KER = kernels(pin, 1.0)
    for _ in range(3):
        psi = P_plus @ (RNG.standard_normal(128) + 1j * RNG.standard_normal(128))
        psi /= np.linalg.norm(psi)
        B = Bfull(psi, KER)
        struct_worst = max(struct_worst, abs(B[0, 0]),
                           float(np.max(np.abs(B[1:, 1:]))))
        rank_ok = rank_ok and np.linalg.matrix_rank(B, tol=1e-10) == 2
check("E", "REFRAME (a) KILL 3 -- the THIRD exact identity (K_S-parity): "
           "every pin-dual carrying the single negative-signature pin leg "
           "ANTICOMMUTES with K_S at 0.0 (and the dual of the negative leg "
           "commutes), so on K_S-confined states the bridge tensor has "
           "exact structural zeros and rank EXACTLY 2 (both pins): the "
           "record-confined habitat itself refuses the grade-3 completion "
           "-- the record sector protects the commutant at grade 3 by "
           "PARITY, as it does at grade 1 by H-reality",
      par_ok and rank_ok and struct_worst < 1e-14,
      f"parity defects 0.0; max structural zero {struct_worst:.1e}; "
      f"confined rank 2 on all draws")

# =============================================================================
print()
print("=" * 78)
print("REFRAME (b)  the sharpened demand (the pass's positive output)")
print("=" * 78)


def realify_linear(X):
    return np.block([[X.real, -X.imag], [X.imag, X.real]])


R_J = np.block([[C.real, C.imag], [C.imag, -C.real]])
R_iJ = np.block([[-C.imag, C.real], [C.real, C.imag]])
BASIS = [realify_linear(I128), realify_linear(1j * I128), R_J, R_iJ]


def Sigma(a, b):
    return 0.25 * (e[a] @ e[b] - e[b] @ e[a])


R_W = realify_linear(1.0 * Sigma(0, 9) + 0.7 * Sigma(1, 2))
sig_proj = max(abs(float(np.sum(R_W * b))) / 256.0 for b in BASIS)
check("E", "REFRAME (b) -- the two-gate admission demand is exhaustive over "
           "the enumerated frozen kernel inventory: grade-1 record kernels "
           "fail gate 1 (commutant-blind: H-self-adjoint at 0.0, columns "
           "< 1e-13); the Sigma dressing fails gate 1 (commutant projection "
           "exactly 0, K3 receipt re-verified); the pin-duals pass gate 1 "
           "but fail gate 2 (habitat-nondegeneracy: confined rank 2) and "
           "class-nativity -- NO frozen kernel passes both gates. The "
           "sharpened demand fed to the B.5 ledger: a native ID-1 occupant "
           "must supply a kernel that reaches the commutant AND survives "
           "the confined habitat AND carries a Psi_0-independent class",
      herm_def == 0.0 and b1_col < 1e-13 and sig_proj < 1e-12
      and rank_ok and worst_col > 0.01,
      f"Sigma commutant projection {sig_proj:.1e}")

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print(f"HEADLINE: K1 KILLED on its own pre-declared condition (conservation "
      f"locates the coset Sp(1)_comm, never a map: infeasible where the "
      f"current moves, fully degenerate where it does not; posit-free "
      f"section = deck +I, degree 0; intertwining and pairing variants die "
      f"by exact identities). REFRAME PASS EXECUTED: the grade-3/self-dual "
      f"record bridge is REAL (full-rank, exact co-flip deck, odd degree) "
      f"but NOT NATIVE -- exact degree fixture/pin-dependent (|c| = 1 and 3 "
      f"witnessed), sign a coin flip, c = 3 members are the ZERO class "
      f"(Test W), and a "
      f"THIRD exact identity (K_S-parity) collapses the bridge to rank 2 on "
      f"the confined habitat. No reframe-as-mechanism qualifies; the "
      f"sharpened two-gate demand is adopted as the pass's output. All four "
      f"node legs of clause 6(a) are now formally dead. "
      f"{nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s)")
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
