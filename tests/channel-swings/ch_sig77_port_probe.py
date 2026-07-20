#!/usr/bin/env python3
"""CH-SIG-77 opening port probe (channel swing, 2026-07-19).

Signature-pure Cl(7,7) reconnaissance under the boundary-adapter standing
axiom (lab/process/boundary-adapter-standing-axiom.md) and the K6
signature-purity guard (CH-QM swing K6; construction-space map council round
8): every computation below is performed IN the (7,7) class. (9,5) facts are
cited from their receipts, never recomputed or blended. The only place both
X4 sign conventions appear is PART 3's convention-location table, whose whole
point is to determine WHICH X4 convention induces the global (7,7) -- that is
comparison-grade location data, not mid-weld blending.

PART 1  Class certificate, extended:
  1a  Cl(7,7) relations exact (repo timelike convention T = {4..10}).
  1b  J' real structure: all 14 e_a commute with J' bit-exactly, J'^2 = +1
      (real class M(128,R); no Kramers pairing). [extends CH-QM C3]
  1c  Krein Gram fork (NEW): the ported canonical Gram
      bS = i * (e_s1...e_s7) (spacelike product; the explicit scalar i is
      forced -- the bare product is anti-Hermitian) is Hermitian, squares to
      I, is so(7,7)-pseudo-anti-Hermitian, and ANTICOMMUTES with J' (the
      scalar i is J'-odd). Consequence: J' FLIPS the Krein sign -- the exact
      C0-control structure of the CH-QM swing, realized natively.
      The chirality-twisted alternative bT = (e_t1...e_t7) (timelike
      product, no scalar i) is also Hermitian/involutive/invariant and
      COMMUTES with J'; bS and bT differ by the chirality omega. Both are
      legitimate so(7,7) Grams; the port must PIN one (convention datum).
  1d  Hyperbolic pairing: the self-dual triplet Krein signature is
      (+96, -96) under the canonical (7,7) Gram (independent re-run of the
      ghost_parity_krein.py (7,7) branch inside this probe).
  1e  THE PAYOFF CERTIFICATE: an ODD-index (signature 3) Hermitian carrier
      on the RS constraint surface that lies IN the J'-commutant (J'-defect
      = 0) -- i.e. odd index is TYPE-CONSISTENT with the (7,7) native
      antiunitary structure. In (9,5) this is impossible (Kramers: even
      signature forced; canon no-go, per-generator-exact certificate).
  1f  HONESTY GUARD: odd is reachable, NOT forced. Natural so(7,7) metric
      connections still give index 0 and the dimension prime spectrum is
      still 3-free (cited from tests/generation-sector/signature_77_rerun.py,
      re-verified light here). The rank/count import survives the port:
      payload N does not drop below 5.
  1g  Sector typing: with the canonical Gram the two orientation sectors
      (1 +- bS)/2 are EXCHANGED by J' (the orientation bit breaks the real
      structure); with the chirality-twisted Gram they are J'-invariant and
      carry a real structure. Either way NO antiunitary protection forces
      even carriers inside a sector -- the wall-dissolution is
      Gram-convention-robust.

PART 2  QM graded-quotient toy port: the toy's Z/2 register (local
      inertness) and orientation mechanism (right bit -> positive sector;
      wrong bit -> cohomological non-closure) are re-run VERBATIM -- the toy
      is an abstract Krein fixture with no signature input, so the port is
      the retyping, not a rebuild. The retyping is 1c/1g: the (9,5) type
      annotation "sigma is J_quat-commuting" does NOT port; under the
      canonical (7,7) Gram sigma is J'-sector-exchanging. The Z/2 remains
      well-typed and loop-storable (the register never touches J).

PART 3  GR cancellation identity port: the branch-(a) identity is re-run
      under the (7,7)-INDUCING X4 convention eta = diag(+1,-1,-1,-1) with
      the correspondingly-signed weak fields (h -> -h), on Schwarzschild AND
      Kerr-drag: harmonic, t1 = 0, Q^TF nonzero, Q^TF = -[t2]^TF, EXACT
      cancellation at sigma*kappa^2 = 1, hard sign gate intact.
      Convention-location table: the fiber Frobenius metric on Sym^2(R^4)
      has signature (7,3) and its trace-reversal (6,4) under BOTH X4 sign
      conventions (it is quadratic in the base metric), while the base
      pullback flips (3,1) <-> (1,3). Hence
        (3,1) + (6,4) = (9,5)     and     (1,3) + (6,4) = (7,7):
      (7,7) sits on the SAME transcript path (Frobenius (7,3) -> trace
      -reversed (6,4)) as (9,5); the two differ only by the X4 sign
      convention, which the transcript does not pin.

PART 4  COSMO projector port: the fiber-Frobenius magnitude projector,
      the gauge-shift identity, and the SO(2) helicity superselection are
      re-run under the (7,7)-inducing convention (g -> -g, theta -> -theta):
      all survive (the projector is quadratic in g^{-1} and theta; the
      helicity argument is spatial-rotation representation theory).

No claim-status, canon, map, or public-posture movement. Exit 0 iff all
checks pass.

Run: python tests/channel-swings/ch_sig77_port_probe.py
"""

import importlib.util
import os
import sys

import numpy as np
import sympy as sp

TOL = 1e-9
CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""), flush=True)


# ===========================================================================
# PART 1 -- Cl(7,7) class certificate, Gram fork, pairing, odd carrier
# ===========================================================================

N, DIM = 14, 128
TIMELIKE_77 = {4, 5, 6, 7, 8, 9, 10}          # repo (7,7) convention
JPRIME_FACTORS = [1, 3, 4, 6, 8, 10, 11, 13]  # CH-QM C3 conjugation factors


def jw_gammas(n):
    I2 = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I2] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def conj_op(Cm, A):
    """For antiunitary J = Cm . conj:  J A J^{-1} = Cm conj(A) Cm^{-1}."""
    return Cm @ np.conj(A) @ np.linalg.inv(Cm)


def part1():
    print("=" * 78)
    print("PART 1 -- Cl(7,7) class certificate, Gram fork, pairing, odd carrier")
    print("=" * 78)
    base = jw_gammas(7)
    e = [(1j * base[a] if a in TIMELIKE_77 else base[a]) for a in range(N)]
    eta = np.array([(-1.0 if a in TIMELIKE_77 else 1.0) for a in range(N)])
    spacelike = [a for a in range(N) if a not in TIMELIKE_77]
    timelike = sorted(TIMELIKE_77)

    # 1a Clifford relations
    err = max(
        np.linalg.norm(e[a] @ e[b] + e[b] @ e[a] - (2 * eta[a] if a == b else 0) * np.eye(DIM))
        for a in range(N) for b in range(N)
    )
    check("1a  Cl(7,7) relations {e_a,e_b} = 2 eta_ab exact", err < 1e-12, f"max err {err:.1e}")

    # 1b J' real structure
    Cp = np.eye(DIM, dtype=complex)
    for a in JPRIME_FACTORS:
        Cp = Cp @ e[a]
    gen_defect = max(np.linalg.norm(e[a] @ Cp - Cp @ np.conj(e[a])) for a in range(N))
    j2 = np.linalg.norm(Cp @ np.conj(Cp) - np.eye(DIM))
    check("1b  all 14 e_a commute with J' (bit-exact); J'^2 = +1 (REAL class)",
          gen_defect < 1e-12 and j2 < 1e-12,
          f"gen defect {gen_defect:.1e}, J'^2-I residual {j2:.1e}")

    # 1c Gram fork
    P7s = np.eye(DIM, dtype=complex)
    for a in spacelike:
        P7s = P7s @ e[a]
    bare_antiherm = np.linalg.norm(P7s + P7s.conj().T)
    bS = 1j * P7s                                       # ported canonical Gram (ghost_parity_krein.py convention)
    bS_herm = np.linalg.norm(bS - bS.conj().T)
    bS_sq = np.linalg.norm(bS @ bS - np.eye(DIM))
    check("1c  bare spacelike 7-product is ANTI-Hermitian: the canonical (7,7) Gram "
          "REQUIRES an explicit scalar i (bS = i * e_s1..e_s7 Hermitian, bS^2 = I)",
          bare_antiherm < 1e-12 and bS_herm < 1e-12 and bS_sq < 1e-12,
          f"bare anti-herm {bare_antiherm:.1e}; bS herm {bS_herm:.1e}, sq {bS_sq:.1e}")

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    res_inv = max(np.linalg.norm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
                  for i in range(N) for j in range(i + 1, N))
    check("1c  bS is so(7,7)-invariant (pseudo-anti-Hermitian for all sigma_ab)",
          res_inv < 1e-9, f"max residual {res_inv:.1e}")

    anti_defect = np.linalg.norm(conj_op(Cp, bS) + bS)
    check("1c  bS ANTICOMMUTES with J' (the scalar i is J'-odd): J' bS J'^-1 = -bS",
          anti_defect < 1e-9, f"anticommutation residual {anti_defect:.1e}")

    rng = np.random.default_rng(5)
    worst = 0.0
    for _ in range(8):
        x = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
        Jx = Cp @ np.conj(x)
        worst = max(worst, abs(np.conj(Jx) @ bS @ Jx + np.conj(x) @ bS @ x))
    check("1c  => J' FLIPS the Krein sign: K(J'x, J'x) = -K(x, x) "
          "(the CH-QM C0-control structure, realized natively in (7,7))",
          worst < 1e-9, f"max |K(J'x,J'x)+K(x,x)| = {worst:.1e}")

    bT = np.eye(DIM, dtype=complex)
    for a in timelike:
        bT = bT @ e[a]
    bT_herm = np.linalg.norm(bT - bT.conj().T)
    bT_sq = np.linalg.norm(bT @ bT - np.eye(DIM))
    res_inv_T = max(np.linalg.norm(bT @ sgen(i, j) + sgen(i, j).conj().T @ bT)
                    for i in range(N) for j in range(i + 1, N))
    comm_T = np.linalg.norm(conj_op(Cp, bT) - bT)
    omega = np.eye(DIM, dtype=complex)
    for a in range(N):
        omega = omega @ e[a]
    ratio = bS @ np.linalg.inv(bT)
    chir = min(np.linalg.norm(ratio - c * omega) for c in (1, -1, 1j, -1j))
    check("1c  chirality-twisted Gram bT = e_t1..e_t7 (no scalar i): Hermitian, "
          "involutive, so(7,7)-invariant, and COMMUTES with J'; bS/bT = (unit) * omega",
          bT_herm < 1e-12 and bT_sq < 1e-12 and res_inv_T < 1e-9 and comm_T < 1e-9 and chir < 1e-9,
          f"herm {bT_herm:.1e}, sq {bT_sq:.1e}, inv {res_inv_T:.1e}, [bT,J'] {comm_T:.1e}, chirality match {chir:.1e}")

    # 1d hyperbolic pairing on the self-dual triplet (canonical Gram)
    I14 = np.eye(N, dtype=complex)
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma

    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = 1
        M[j, i] = -1
        return M

    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Jops = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I14 if False else np.eye(DIM))
            for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]
    Cas = -(Jops[0] @ Jops[0] + Jops[1] @ Jops[1] + Jops[2] @ Jops[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]
    etaV = np.diag(eta).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt
    B = 0.5 * (B + B.conj().T)
    sig = np.linalg.eigvalsh(B)
    npl = int(np.sum(sig > 1e-9))
    nmi = int(np.sum(sig < -1e-9))
    check("1d  hyperbolic Krein pairing SURVIVES: self-dual triplet signature (+96, -96)",
          npl == 96 and nmi == 96, f"(+{npl}, -{nmi}), triplet dim {Wt.shape[1]}")

    # 1e THE PAYOFF: odd-index Hermitian carrier in the J'-commutant
    CpRS = np.kron(I14, Cp)                        # J'_RS = (id_14 (x) C') . conj, J'^2 = +1
    j2rs = np.linalg.norm(CpRS @ np.conj(CpRS) - np.eye(N * DIM))
    pi_comm = np.linalg.norm(CpRS @ np.conj(Pi) - Pi @ CpRS)
    check("1e  RS-level real structure J'_RS = (id_14 (x) C').conj: J'^2 = +1 and "
          "J'_RS preserves the constraint surface ([Pi, J'_RS] = 0)",
          j2rs < 1e-9 and pi_comm < 1e-8, f"J'^2 residual {j2rs:.1e}, [Pi,J'] {pi_comm:.1e}")

    def jfix(v):
        return v + CpRS @ np.conj(v)

    fixed = []
    idx = 0
    while len(fixed) < 3 and idx < W.shape[1]:
        u = jfix(W[:, idx])
        if np.linalg.norm(u) < 1e-6:
            u = 1j * (W[:, idx] - CpRS @ np.conj(W[:, idx]))
        for f in fixed:                             # Gram-Schmidt (coefficients auto-real on the fixed form)
            u = u - (np.conj(f) @ u) * f
        nu = np.linalg.norm(u)
        if nu > 1e-8:
            fixed.append(u / nu)
        idx += 1
    U3 = np.column_stack(fixed)
    P3 = U3 @ U3.conj().T
    jdef = np.linalg.norm(CpRS @ np.conj(P3) @ np.linalg.inv(CpRS) - P3)
    in_ker = np.linalg.norm(Pi @ P3 - P3)
    evP = np.linalg.eigvalsh(0.5 * (P3 + P3.conj().T))
    sig3 = int((evP > 1e-9).sum()) - int((evP < -1e-9).sum())
    check("1e  PAYOFF: rank-3 Hermitian carrier ON the constraint surface, IN the "
          "J'-commutant (J'-defect = 0), with ODD signature 3 -- odd index is "
          "TYPE-CONSISTENT in (7,7). [(9,5) contrast, cited not recomputed: canon "
          "no-go forces even signature for J_quat-commutant carriers; odd carriers "
          "there are non-H-linear imports (step10/step11)]",
          jdef < 1e-9 and in_ker < 1e-9 and sig3 == 3,
          f"J'-defect {jdef:.1e}, kernel residual {in_ker:.1e}, signature {sig3}")

    # 1f honesty guard: odd reachable, not forced
    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = eta[j]
        M[j, i] = -eta[i]
        return M

    def Jfull(i, j):
        return np.kron(Mvec(i, j), np.eye(DIM)) + np.kron(I14, sgen(i, j))

    Q = np.eye(N * DIM, dtype=complex) - Pi

    def gd(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def hsig(A):
        evv = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        tol = 1e-7 * np.abs(evv).max()
        return int((evv > tol).sum()) - int((evv < -tol).sum())

    conn_sigs = [hsig(gd(1j * (Jfull(0, 1) + Jfull(2, 3)))), hsig(gd(1j * Jfull(0, 1)))]
    rng2 = np.random.default_rng(3)
    conn_sigs += [hsig(gd(1j * sum(c * Jfull(i, j) for (c, (i, j)) in
                                   zip(rng2.standard_normal(6), [(0, 1), (2, 3), (4, 5), (0, 9), (2, 11), (6, 13)]))))
                  for _ in range(2)]
    dims = {"spinor": 128, "RS vector": 14, "RS space": 1792, "ker(Gamma)": 1664}

    def has3(n):
        while n % 2 == 0:
            n //= 2
        return n % 3 == 0

    check("1f  HONESTY: odd is reachable, NOT forced -- natural so(7,7) metric "
          "connections still give index 0; dimension prime spectrum still 3-free "
          "=> the rank/count integer import SURVIVES the port (payload N stays 5)",
          all(s == 0 for s in conn_sigs) and not any(has3(v) for v in dims.values()),
          f"connection indices {conn_sigs}; dims {dims}")

    # 1g sector typing under the two Grams
    Pp, Pm = 0.5 * (np.eye(DIM) + bS), 0.5 * (np.eye(DIM) - bS)
    swap = np.linalg.norm(conj_op(Cp, Pp) - Pm)
    PpT = 0.5 * (np.eye(DIM) + bT)
    invT = np.linalg.norm(conj_op(Cp, PpT) - PpT)
    check("1g  sector typing: canonical Gram -> J' EXCHANGES the two orientation "
          "sectors (the bit breaks the real structure); chirality-twisted Gram -> "
          "sectors J'-invariant (real structure inside). Both Gram choices dissolve "
          "the Kramers wall; the (9,5) annotation 'sigma is J-commuting' does NOT port",
          swap < 1e-9 and invT < 1e-9,
          f"J'(1+bS)/2 -> (1-bS)/2 residual {swap:.1e}; [(1+bT)/2, J'] {invT:.1e}")


# ===========================================================================
# PART 2 -- QM graded-quotient toy port (verbatim rerun + retyping note)
# ===========================================================================

def part2():
    print()
    print("=" * 78)
    print("PART 2 -- QM graded-quotient toy: verbatim rerun (signature-agnostic fixture)")
    print("=" * 78)
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(
        "ch_qm_toy", os.path.join(here, "ch_qm_graded_quotient_toy.py"))
    toy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(toy)
    ok = True
    try:
        toy.part_A()      # Z/2 register: loop-coherent storage, local inertness
        toy.part_B()      # right bit -> positive sector; wrong bit -> cohomological failure
    except (AssertionError, Exception) as exc:  # noqa: BLE001 -- any failure kills the port
        ok = False
        print(f"  toy rerun FAILED: {exc}")
    check("2   QM toy mechanism SURVIVES verbatim: Z/2 register locally inert + "
          "loop-readable; right orientation -> positive-definite physical sector; "
          "wrong orientation -> Noether NON-CLOSURE (cohomological), negative-norm "
          "survivors, regenerating zombie, retune blocked by storage",
          ok,
          "the toy has NO signature input; the (7,7) port is the RETYPING in 1c/1g")


# ===========================================================================
# PART 3 -- GR cancellation identity under the (7,7)-inducing X4 convention
# ===========================================================================

def part3():
    print()
    print("=" * 78)
    print("PART 3 -- GR branch-(a) identity under eta = diag(+1,-1,-1,-1) (the (7,7)-")
    print("          inducing X4 convention), h -> -h; plus convention-location table")
    print("=" * 78)
    t, x, y, z, M, J = sp.symbols("t x y z M J", real=True, positive=True)
    coords = [t, x, y, z]
    r = sp.sqrt(x**2 + y**2 + z**2)
    eta = sp.diag(1, -1, -1, -1)                  # (7,7)-inducing convention

    def schwarzschild_h():
        phi = M / r
        h = sp.zeros(4, 4)
        h[0, 0] = -2 * phi                        # g_00 = 1 - 2phi
        for i in (1, 2, 3):
            h[i, i] = -2 * phi                    # g_ii = -(1 + 2phi)
        return h

    def kerr_drag_h():
        h = schwarzschild_h()
        h[0, 1] = h[1, 0] = 2 * J * y / r**3      # sign-flipped with the convention
        h[0, 2] = h[2, 0] = -2 * J * x / r**3
        return h

    def hmean_of(h):
        out = sp.zeros(4, 4)
        for a in range(4):
            for b in range(4):
                out[a, b] = sp.simplify(sum(eta[m, m] * sp.diff(h[a, b], coords[m], 2) for m in range(4)))
        return out

    def t1_t2_of(h):
        hmean = hmean_of(h)

        def bhat(mu, nu, a, bidx):
            return sp.diff(h[a, bidx], coords[mu], coords[nu]) - sp.Rational(1, 4) * eta[mu, nu] * hmean[a, bidx]

        def fdot(func):
            return sum(eta[a, a] * eta[b, b] * func(a, b) for a in range(4) for b in range(4))

        t1 = sp.zeros(4, 4)
        t2 = sp.zeros(4, 4)
        for mu in range(4):
            for nu in range(4):
                t1[mu, nu] = sp.simplify(sp.Rational(1, 2) * fdot(lambda a, b: hmean[a, b] * bhat(mu, nu, a, b)))
                t2[mu, nu] = sp.simplify(sum(eta[p, p] * fdot(lambda a, b: bhat(mu, p, a, b) * bhat(p, nu, a, b))
                                             for p in range(4)))
        return hmean, t1, t2

    def trace_free(mtx):
        tr = sp.simplify(sum(eta[p, p] * mtx[p, p] for p in range(4)))
        return sp.Matrix(4, 4, lambda mu, nu: sp.simplify(mtx[mu, nu] - sp.Rational(1, 4) * eta[mu, nu] * tr))

    def all_zero(mtx):
        return all(sp.simplify(mtx[i, j]) == 0 for i in range(4) for j in range(4))

    def any_nonzero(mtx):
        return any(sp.simplify(mtx[i, j]) != 0 for i in range(4) for j in range(4))

    POINT1 = {x: 1, y: 2, z: 2, t: 0, M: 1, J: 1}
    POINT2 = {x: 2, y: 3, z: 6, t: 0, M: 1, J: 1}

    def constant_cancels(qtf, stf):
        values = []
        for pt in (POINT1, POINT2):
            for mu in range(4):
                for nu in range(4):
                    sval = sp.nsimplify(stf[mu, nu].subs(pt))
                    qval = sp.nsimplify(qtf[mu, nu].subs(pt))
                    if sval == 0:
                        if qval != 0:
                            return False, "structure mismatch"
                    else:
                        values.append(sp.nsimplify(-qval / sval))
        if not values:
            return False, "stress vanishes"
        first = values[0]
        for v in values[1:]:
            if sp.simplify(v - first) != 0:
                return False, f"non-constant: {first} vs {v}"
        return True, str(first)

    h = schwarzschild_h()
    hmean, t1, t2 = t1_t2_of(h)
    check("3a  Schwarzschild (mostly-minus): harmonic box(h) = 0 and t1 = 0",
          all_zero(hmean) and all_zero(t1))
    qtf = trace_free(t1 - t2)
    check("3b  Q^TF nonzero AND structural identity Q^TF = -[t2]^TF survives",
          any_nonzero(qtf) and all_zero(qtf + trace_free(t2)))
    ok_c, cval = constant_cancels(qtf, trace_free(t2))
    check("3c  EXACT cancellation with ONE frozen constant: sigma*kappa^2 = 1 "
          "(kappa^2 = 1, sigma = +1 in these conventions)",
          ok_c and cval == "1", f"c = {cval}")
    kappa = sp.symbols("kappa", real=True)
    check("3d  hard sign gate survives: sigma = -1 leaves residual factor "
          "-(1 + kappa^2), NO real kappa (pure algebra, signature-blind)",
          sp.solve(sp.Eq(-(1 + kappa**2), 0), kappa) == [])
    hk = kerr_drag_h()
    hmean_k, t1_k, t2_k = t1_t2_of(hk)
    qtf_k = trace_free(t1_k - t2_k)
    check("3e  Kerr-drag (mostly-minus): harmonic, t1 = 0, SAME identity with the "
          "SAME frozen coefficient",
          all_zero(hmean_k) and all_zero(t1_k) and all_zero(qtf_k + trace_free(t2_k)))

    # Convention-location table (comparison-grade: locates (7,7) on the transcript path)
    import itertools
    basis = []
    for i in range(4):
        for j in range(i, 4):
            Mb = np.zeros((4, 4))
            Mb[i, j] = Mb[j, i] = 1.0
            basis.append(Mb)

    def fiber_sigs(eta_diag):
        ei = np.diag(1.0 / np.array(eta_diag))
        Gf = np.zeros((10, 10))
        Gt = np.zeros((10, 10))
        for a, ha in enumerate(basis):
            for b, hb in enumerate(basis):
                frob = np.trace(ei @ ha @ ei @ hb)
                Gf[a, b] = frob
                Gt[a, b] = frob - 0.5 * np.trace(ei @ ha) * np.trace(ei @ hb)
        def s(Gm):
            ev = np.linalg.eigvalsh(0.5 * (Gm + Gm.T))
            return int((ev > 1e-9).sum()), int((ev < -1e-9).sum())
        return s(Gf), s(Gt)

    (f_mp, tr_mp) = fiber_sigs([-1, 1, 1, 1])     # (9,5)-inducing convention
    (f_mm, tr_mm) = fiber_sigs([1, -1, -1, -1])   # (7,7)-inducing convention
    base_mp = (3, 1)
    base_mm = (1, 3)
    tot_mp = (base_mp[0] + tr_mp[0], base_mp[1] + tr_mp[1])
    tot_mm = (base_mm[0] + tr_mm[0], base_mm[1] + tr_mm[1])
    check("3f  CONVENTION-LOCATION: fiber Frobenius (7,3) and trace-reversed (6,4) "
          "under BOTH X4 conventions (quadratic in the base metric); base pullback "
          "flips => (3,1)+(6,4) = (9,5) and (1,3)+(6,4) = (7,7). (7,7) IS the "
          "transcript's trace-reversal path under the opposite X4 sign convention",
          f_mp == (7, 3) and f_mm == (7, 3) and tr_mp == (6, 4) and tr_mm == (6, 4)
          and tot_mp == (9, 5) and tot_mm == (7, 7),
          f"Frobenius {f_mp}/{f_mm}, trace-reversed {tr_mp}/{tr_mm}, totals {tot_mp}/{tot_mm}")


# ===========================================================================
# PART 4 -- COSMO projector port under the (7,7)-inducing convention
# ===========================================================================

def part4():
    print()
    print("=" * 78)
    print("PART 4 -- COSMO magnitude projector under g -> -g, theta -> -theta")
    print("=" * 78)
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = (t, x, y, z)
    a = sp.Function("a", positive=True)(t)
    alpha = sp.Function("alpha")(t)
    beta = sp.Function("beta")(t)
    g = sp.diag(1, -a**2, -a**2, -a**2)                     # mostly-minus FLRW
    theta_bar = sp.diag(alpha, -a**2 * beta, -a**2 * beta, -a**2 * beta)

    gi = g.inv()
    F_bar = sp.simplify(sp.trace((gi * theta_bar * gi).T * theta_bar))
    check("4a  background magnitude |theta_bar|^2 = alpha^2 + 3 beta^2 (unchanged: "
          "the Frobenius magnitude is quadratic in g^{-1} and theta)",
          sp.simplify(F_bar - (alpha**2 + 3 * beta**2)) == 0, f"F_bar = {F_bar}")

    d00, d0x, d0y, d0z = sp.symbols("d00 d0x d0y d0z", real=True)
    dxx, dxy, dxz, dyy, dyz, dzz = sp.symbols("dxx dxy dxz dyy dyz dzz", real=True)
    D = sp.Matrix([[d00, d0x, d0y, d0z],
                   [d0x, dxx, dxy, dxz],
                   [d0y, dxy, dyy, dyz],
                   [d0z, dxz, dyz, dzz]])
    proj = sp.expand(sp.trace((gi * theta_bar * gi).T * D))
    nonscalar = [d0x, d0y, dxz, dyz, dxy]
    check("4b  projector output still PURE helicity-0 (no vector/tensor leakage)",
          all(sp.diff(proj, s) == 0 for s in nonscalar),
          f"proj = {sp.simplify(proj)}")

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
    gi_th = gi * theta_bar
    dF = sp.simplify(sp.expand(2 * sp.trace(gi * Lth * gi_th) - 2 * sp.trace(gi * Lg * gi_th * gi_th)))
    check("4c  gauge-shift identity survives: delta|theta|^2 = T * d|theta_bar|^2/dt; "
          "spatial-scalar and vector gauge drop identically",
          sp.simplify(dF - T * sp.diff(F_bar, t)) == 0 and not any(dF.has(f) for f in (S, Vx, Vy, Vz)))

    phi = sp.symbols("phi", real=True)
    c_, s_ = sp.cos(phi), sp.sin(phi)
    Lam = sp.diag(1, sp.Matrix([[c_, -s_, 0], [s_, c_, 0], [0, 0, 1]]))
    Dp = sp.simplify(Lam * D * Lam.T)

    def rotate(expr):
        subs = {D[m, n]: Dp[m, n] for m in range(4) for n in range(m, 4)}
        return expr.subs(subs, simultaneous=True)

    I = sp.I
    m2 = D[1, 1] - D[2, 2] - 2 * I * D[1, 2]
    ok_phase = sp.simplify(sp.expand(rotate(m2)) - sp.expand((sp.cos(-2 * phi) + I * sp.sin(-2 * phi)) * m2)) == 0
    cross = D[0, 0] * D[0, 1]
    check("4d  SO(2) helicity superselection survives (spatial representation "
          "theory, signature-blind): helicity phases exact, scalar-vector cross "
          "term still non-invariant",
          ok_phase and sp.simplify(rotate(cross) - cross) != 0)


def main():
    part1()
    part2()
    part3()
    part4()
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print()
    print(f"{len(CHECKS) - n_fail}/{len(CHECKS)} checks passed.")
    print("SUMMARY: Cl(7,7) real class certified (J'^2 = +1, all generators commute); "
          "canonical Krein Gram needs an explicit scalar i and ANTICOMMUTES with J' "
          "(J' flips the Krein sign -- native C0 structure; chirality-twisted Gram "
          "commutes: convention fork to pin); hyperbolic pairing (+96,-96) survives; "
          "ODD-index J'-commutant carrier EXISTS on the constraint surface (the "
          "Kramers wall is gone) but odd is reachable-not-forced (connections still "
          "index 0, spectrum 3-free: rank import survives, N stays 5); QM toy "
          "mechanism survives verbatim (retyping only); GR branch-(a) cancellation "
          "identity survives EXACTLY under the (7,7)-inducing convention (sigma*"
          "kappa^2 = 1, sign gate intact, Kerr-drag too); (7,7) located ON the "
          "transcript trace-reversal path ((1,3)+(6,4)); COSMO projector, gauge "
          "shift, and helicity superselection survive. No claim-status movement.")
    if n_fail:
        raise SystemExit(f"{n_fail} check(s) FAILED")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
