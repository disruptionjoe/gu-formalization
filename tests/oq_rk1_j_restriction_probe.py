#!/usr/bin/env python3
"""OQ-RK1 probe: how the quaternionic structure J acts on the D2 x D5
(Spin(4) x Spin(10)) branched slots of the Rarita-Schwinger carrier.

LAYER-0 FENCE (verbatim, load-bearing):
this computation classifies the antiunitary's action on a decomposition; it
does NOT by itself compute rank_H(S_RS^+), does NOT close OQ-RK1 (which is
BLOCKED_NEEDS_SPEC on the physical projector Π_RS^phys per
tests/oq_rk1_e_rs_eff_assembly.py), and no count claim follows. How the
H-structure factorizes across the tensor splitting is a naming/spec question
this probe INFORMS, not answers.

WHAT IS COMPUTED
----------------
The frozen B5 ledger (explorations/shiab-operator/
b5-observer-symbol-multiplicity-matrix-2026-07-24.md) branches the RS carrier
under H_C = Spin(4,C) x Spin(10,C) into slots

    (3,2,16+) 96   (2,3,16-) 96   (2,1,144+) 288   (1,2,144-) 288
    (3,2,16-) 96   (2,3,16+) 96   (2,1,144-) 288   (1,2,144+) 288

(the 1536-dim X block) plus multiplicity-2 small sectors, using the exact D5
identities 10 (x) 16+/- = 144+/- + 16-/+.  The verified antilinear
quaternionic structure J = M.conj (J^2 = -I, commutes with every Clifford
generator e_a, hence with omega, T, Pi_RS; same construction as
tests/hardening-pass/oqrk1_indh_rank.py) acts on the common RS fiber
V = R^14 (x) S, dim_C = 1792, as J_V = (I_14 (x) M).conj.

This probe builds the slot projectors CANONICALLY from subalgebra invariant
data only -- no basis choice, no target import:

    C4   : quadratic Casimir of so(4)_C      (3/2 on (2,1)/(1,2); 11/2 on (3,2)/(2,3))
    C10  : quadratic Casimir of so(10)_C     (45/4 on 16-type; 85/4 on 144-type)
    OmF  : internal D5 chirality I (x) om_F  (+1 on 16+/144+ side, -1 mirror)
    P4   : degree-2 so(4) Pfaffian Casimir   (prop. to C_L - C_R; separates L/R)

All four commute; joint Lagrange spectral interpolation yields the 12
equivariant slot projectors (8 X slots + 4 multiplicity-2 small sectors),
verified by idempotence, completeness, pairwise orthogonality, exact traces,
equivariance, gamma-trace annihilation (X slots lie in ker T), and total
chirality grading.  Then the permutation action of J is measured directly:

    D[i,j] = || P_i - J P_j J^{-1} ||_F ,   J P J^{-1} = (I(x)M) conj(P) (I(x)M)^{-1}.

The D2 x D5 subalgebra is fixed only up to the signature allocation of the
4-plane inside (9,5) -- itself part of the UNFROZEN native real/Krein spec
(B5-NATIVE-REAL-KREIN-ADJOINT-FREEZE).  The probe therefore sweeps all five
allocations: base (4,0), (3,1), (2,2), (1,3), (0,4).

HARD ASSERTS: positive controls first (Clifford, omega^2=+I, J^2=-I,
antilinearity, J-commutation with all 91 so(9,5) generators and omega,
structure constants, Casimir calibration, annihilating polynomials, projector
idempotence/completeness/orthogonality/traces/equivariance), then the
classification result.  Exit nonzero on any failure.
"""

from __future__ import annotations

import json
import sys

import numpy as np

# ---------------------------------------------------------------------------
# tolerances
# ---------------------------------------------------------------------------
T_EXACT = 1e-10   # exact algebraic identities (Clifford, J, structure consts)
T_ANN = 5e-8      # annihilating-polynomial residuals
T_PROJ = 5e-8     # projector idempotence / orthogonality / completeness (max abs)
T_MATCH = 1e-5    # Frobenius distance for a certified J-permutation match
SEP_MIN = 1e4     # required separation matched vs best unmatched

N14 = 14
DIMS = 128
DIMV = N14 * DIMS

CHECKS = {"n": 0}


def check(label: str, cond: bool, detail: str = "") -> None:
    CHECKS["n"] += 1
    if not cond:
        print(f"FAIL [{CHECKS['n']:03d}]: {label}  {detail}")
        sys.exit(1)
    print(f"PASS [{CHECKS['n']:03d}]: {label}  {detail}")


def mx(A) -> float:
    return float(np.max(np.abs(A)))


def fro(A) -> float:
    return float(np.linalg.norm(A))


# ---------------------------------------------------------------------------
# Clifford data: identical construction to tests/oq_rk1_cl95_explicit_rep.py
# ---------------------------------------------------------------------------
def kron_list(mats):
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def jordan_wigner_gammas(n_pairs: int):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas = []
    for k in range(n_pairs):
        left = [s3] * k
        right = [I] * (n_pairs - 1 - k)
        gammas.append(kron_list(left + [s1] + right))
        gammas.append(kron_list(left + [s2] + right))
    return gammas


def build_clifford_9_5():
    G = jordan_wigner_gammas(7)
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(N14)]
    omega = np.eye(DIMS, dtype=complex)
    for a in range(N14):
        omega = omega @ e[a]
    return e, eta, omega


def build_quaternionic_structure(e):
    """J = M.conj with J^2=-I commuting with every e_a (same as hardening pass)."""
    M = np.eye(DIMS, dtype=complex)
    for a in (1, 3, 5, 7, 10, 12):
        M = M @ e[a]
    scalar = (M @ M.conj())[0, 0]
    M = M / np.sqrt(abs(scalar))
    return M


# ---------------------------------------------------------------------------
# subalgebra generators (vector 14-dim block rep + spinor rep)
# ---------------------------------------------------------------------------
def vec_gen(a: int, b: int, eta):
    """so(9,5) generator on R^14: M_ab e_d = eta_bd e_a - eta_ad e_b (M_aa = 0)."""
    m = np.zeros((N14, N14), dtype=complex)
    if a != b:
        m[a, b] = eta[b]
        m[b, a] = -eta[a]
    return m


def spin_gen(a: int, b: int, e):
    """Sigma_ab = (1/4)[e_a,e_b] = (1/2) e_a e_b for a != b (Sigma_aa = 0)."""
    if a == b:
        return np.zeros((DIMS, DIMS), dtype=complex)
    return 0.5 * (e[a] @ e[b])


def bracket_rhs(gen, a, b, c, d, eta):
    """eta_bc M_ad - eta_ac M_bd - eta_bd M_ac + eta_ad M_bc (diagonal eta)."""
    out = 0.0 * gen(0, 1)
    if b == c:
        out = out + eta[b] * gen(a, d)
    if a == c:
        out = out - eta[a] * gen(b, d)
    if b == d:
        out = out - eta[b] * gen(a, c)
    if a == d:
        out = out + eta[a] * gen(b, c)
    return out


def chirality_op(idxs, e):
    """Normalized chirality: c * prod_{a in idxs} e_a with square +I, c in {1, i}."""
    raw = np.eye(DIMS, dtype=complex)
    for a in sorted(idxs):
        raw = raw @ e[a]
    sq = raw @ raw
    s = sq[0, 0]
    assert mx(sq - s * np.eye(DIMS)) < T_EXACT, "chirality square not scalar"
    if abs(s - 1.0) < 1e-9:
        c = 1.0 + 0j
    elif abs(s + 1.0) < 1e-9:
        c = 1j
    else:
        raise AssertionError(f"chirality square is {s}, not +/-1")
    return c * raw, c


# ---------------------------------------------------------------------------
# slot catalogue: name -> (C4, C10, OmF sign, P4 factor f with eigenvalue f*c, dim)
# Labeling conventions (stated, convention-only; the classification statements
# are invariant under relabeling):
#   left "L" (first su(2) label active)  := om_B = +1 side of S;
#   16+ := om_F = +1 side of S;  144+ := the 144 slot with ambient OmF = +1
#   (i.e. the 144 inside 10 (x) 16+, which is the Racah-Speiser 144+).
# ---------------------------------------------------------------------------
FR = 5.0 / 3.0
SLOT_DEFS = [
    ("X32p", 5.5, 11.25, +1, +FR, 96),
    ("X23p", 5.5, 11.25, +1, -FR, 96),
    ("X32m", 5.5, 11.25, -1, +FR, 96),
    ("X23m", 5.5, 11.25, -1, -FR, 96),
    ("X2Tp", 1.5, 21.25, +1, +1.0, 288),
    ("X1Tp", 1.5, 21.25, +1, -1.0, 288),
    ("X2Tm", 1.5, 21.25, -1, +1.0, 288),
    ("X1Tm", 1.5, 21.25, -1, -1.0, 288),
    ("SM21p", 1.5, 11.25, +1, +1.0, 64),
    ("SM12p", 1.5, 11.25, +1, -1.0, 64),
    ("SM21m", 1.5, 11.25, -1, +1.0, 64),
    ("SM12m", 1.5, 11.25, -1, -1.0, 64),
]
X_SLOTS = [s[0] for s in SLOT_DEFS[:8]]
MIRROR = {  # the documented B5 mirror coflip (flips D5 chirality only)
    "X32p": "X32m", "X32m": "X32p", "X23p": "X23m", "X23m": "X23p",
    "X2Tp": "X2Tm", "X2Tm": "X2Tp", "X1Tp": "X1Tm", "X1Tm": "X1Tp",
    "SM21p": "SM21m", "SM21m": "SM21p", "SM12p": "SM12m", "SM12m": "SM12p",
}
EXCHANGE_PERM = {  # flip BOTH su(2) factors AND D5 chirality (total chirality kept)
    "X32p": "X23m", "X23m": "X32p", "X23p": "X32m", "X32m": "X23p",
    "X2Tp": "X1Tm", "X1Tm": "X2Tp", "X1Tp": "X2Tm", "X2Tm": "X1Tp",
    "SM21p": "SM12m", "SM12m": "SM21p", "SM12p": "SM21m", "SM21m": "SM12p",
}


def run_split(tag, base_idx, e, eta, omega, M, KM, KMi, T, IdenV, primary):
    print("\n" + "=" * 78)
    print(f"SPLIT {tag}: base 4-plane indices {base_idx}  "
          f"(eta {[eta[a] for a in base_idx]})")
    print("=" * 78)
    rec = {"base_idx": list(base_idx)}
    base = sorted(base_idx)
    intern = [a for a in range(N14) if a not in base]
    q_base = sum(1 for a in base if eta[a] == -1)
    rec["base_signature"] = f"({4 - q_base},{q_base})"
    rec["internal_signature"] = f"({10 - (5 - q_base)},{5 - q_base})"
    I128 = np.eye(DIMS, dtype=complex)
    I14 = np.eye(N14, dtype=complex)

    # -- structure constants: vector and spinor reps agree (sampled quadruples)
    rng = np.random.default_rng(20260803)
    quads = []
    for _ in range(12):
        a, b = rng.choice(base, 2, replace=False)
        c, d = rng.choice(base, 2, replace=False)
        quads.append((a, b, c, d))
    for _ in range(12):
        a, b = rng.choice(intern, 2, replace=False)
        c, d = rng.choice(intern, 2, replace=False)
        quads.append((a, b, c, d))
    for _ in range(6):  # cross-factor pairs must commute
        a, b = rng.choice(base, 2, replace=False)
        c, d = rng.choice(intern, 2, replace=False)
        quads.append((a, b, c, d))
    err_sc = 0.0
    for (a, b, c, d) in quads:
        for gen in (lambda p, q: vec_gen(p, q, eta), lambda p, q: spin_gen(p, q, e)):
            lhs = gen(a, b) @ gen(c, d) - gen(c, d) @ gen(a, b)
            rhs = bracket_rhs(gen, a, b, c, d, eta)
            err_sc = max(err_sc, mx(lhs - rhs))
    check(f"{tag}: structure constants agree, vector and spinor reps",
          err_sc < T_EXACT, f"(max err {err_sc:.1e})")

    # -- Casimirs (normalization C = -sum_{a<b} eta^a eta^b rho(M_ab)^2) ------
    def casimirs(idxs):
        Cv = np.zeros((N14, N14), dtype=complex)
        Cs = np.zeros((DIMS, DIMS), dtype=complex)
        cross = np.zeros((DIMV, DIMV), dtype=complex)
        for i, a in enumerate(idxs):
            for b in idxs[i + 1:]:
                s = eta[a] * eta[b]
                A = vec_gen(a, b, eta)
                B = spin_gen(a, b, e)
                Cv -= s * (A @ A)
                Cs -= s * (B @ B)
                cross -= 2.0 * s * np.kron(A, B)
        CV = np.kron(Cv, I128) + np.kron(I14, Cs) + cross
        return Cv, Cs, CV

    Cv4, Cs4, C4V = casimirs(base)
    Cv10, Cs10, C10V = casimirs(intern)

    # calibration on the small factors (exact rep-theory values)
    check(f"{tag}: so(4) Casimir on S = 3/2 (spinor is (2,1)+(1,2))",
          mx(Cs4 - 1.5 * I128) < T_EXACT)
    check(f"{tag}: so(10) Casimir on S = 45/4 (spinor is 16-type throughout)",
          mx(Cs10 - 11.25 * I128) < T_EXACT)
    dv4 = np.diag([3.0 if a in base else 0.0 for a in range(N14)])
    dv10 = np.diag([0.0 if a in base else 9.0 for a in range(N14)])
    check(f"{tag}: vector-block Casimirs (3 on base 4, 9 on internal 10)",
          mx(Cv4 - dv4) < T_EXACT and mx(Cv10 - dv10) < T_EXACT)

    # -- chirality operators --------------------------------------------------
    omB, cB = chirality_op(base, e)
    omF, cF = chirality_op(intern, e)
    rec["c_base_phase"] = "1" if abs(cB - 1) < 1e-9 else "i"
    rec["c_internal_phase"] = "1" if abs(cF - 1) < 1e-9 else "i"
    XBF = omB @ omF
    z = omega[0, 0] / XBF[0, 0] if abs(XBF[0, 0]) > 0.5 else np.trace(
        XBF.conj().T @ omega) / np.trace(XBF.conj().T @ XBF)
    err_z = mx(omega - z * XBF)
    check(f"{tag}: om_B om_F = total chirality up to sign (z={z.real:+.0f})",
          err_z < T_EXACT and abs(abs(z) - 1) < 1e-9 and abs(z.imag) < 1e-9)
    check(f"{tag}: [om_B, om_F] = 0", mx(omB @ omF - omF @ omB) < T_EXACT)

    # J vs the chirality gradings: the structural 'why' numbers
    sB = complex(np.conj(cB) / cB).real
    sF = complex(np.conj(cF) / cF).real
    dB = mx(M @ omB.conj() - sB * (omB @ M))
    dF = mx(M @ omF.conj() - sF * (omF @ M))
    check(f"{tag}: J om_B J^-1 = ({sB:+.0f}) om_B ; J om_F J^-1 = ({sF:+.0f}) om_F",
          dB < T_EXACT and dF < T_EXACT,
          f"(errs {dB:.1e}, {dF:.1e})")
    check(f"{tag}: co-occurrence forced by [J,omega]=0: sign flips together",
          abs(sB - sF) < 1e-12)
    rec["J_conj_omB_sign"] = sB
    rec["J_conj_omF_sign"] = sF

    # -- so(4) Pfaffian Casimir P4 (degree 2) --------------------------------
    b0, b1, b2, b3 = base
    pairings = [((b0, b1), (b2, b3), +1.0),
                ((b0, b2), (b1, b3), -1.0),
                ((b0, b3), (b1, b2), +1.0)]
    P4V = np.zeros((DIMV, DIMV), dtype=complex)
    P4S = np.zeros((DIMS, DIMS), dtype=complex)
    for (p, q), (r, s), sgn in pairings:
        coef = sgn * eta[p] * eta[q] * eta[r] * eta[s]
        A1, A2 = vec_gen(p, q, eta), vec_gen(r, s, eta)
        B1, B2 = spin_gen(p, q, e), spin_gen(r, s, e)
        P4V += coef * (np.kron(A1 @ A2, I128) + np.kron(A1, B2)
                       + np.kron(A2, B1) + np.kron(I14, B1 @ B2))
        P4S += coef * (B1 @ B2)

    # scalar c on the om_B=+1 (left) half of S: defines the L/R eigenvalue scale
    PL = 0.5 * (I128 + omB)
    Xc = P4S @ PL
    c = complex(np.trace(Xc) / 64.0)
    err_c = mx(Xc - c * PL)
    check(f"{tag}: P4 on S is scalar c on left half", err_c < T_EXACT,
          f"c = {c:.6g}")
    check(f"{tag}: |c| = 3/4 exactly", abs(abs(c) - 0.75) < 1e-9)
    c_real = abs(c.imag) < 1e-9
    c_imag = abs(c.real) < 1e-9
    check(f"{tag}: c is purely real or purely imaginary", c_real or c_imag,
          f"({'real' if c_real else 'imaginary'})")
    rec["P4_left_scalar_c"] = [c.real, c.imag]
    rec["P4_scalar_reality"] = "real" if c_real else "imaginary"

    # -- annihilating polynomials: the certified joint spectrum ---------------
    ann4 = (C4V - 1.5 * IdenV) @ (C4V - 5.5 * IdenV)
    check(f"{tag}: spec(C4 on V) = {{3/2, 11/2}}", mx(ann4) < T_ANN,
          f"(residual {mx(ann4):.1e})")
    ann10 = (C10V - 11.25 * IdenV) @ (C10V - 21.25 * IdenV)
    check(f"{tag}: spec(C10 on V) = {{45/4, 85/4}}", mx(ann10) < T_ANN,
          f"(residual {mx(ann10):.1e})")
    fs = [FR, -FR, 1.0, -1.0]
    annP = IdenV.copy()
    for f in fs:
        annP = annP @ (P4V - c * f * IdenV)
    check(f"{tag}: spec(P4 on V) = c*{{+5/3,-5/3,+1,-1}}", mx(annP) < T_ANN,
          f"(residual {mx(annP):.1e})")
    OmF_V = np.kron(I14, omF)
    check(f"{tag}: OmF^2 = I on V", mx(OmF_V @ OmF_V - IdenV) < T_EXACT)

    # commutation of the four invariants (vector-level spot check)
    v = rng.standard_normal(DIMV) + 1j * rng.standard_normal(DIMV)
    ops = {"C4": C4V, "C10": C10V, "P4": P4V, "OmF": OmF_V}
    cerr = 0.0
    names = list(ops)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            Op1, Op2 = ops[names[i]], ops[names[j]]
            cerr = max(cerr, mx(Op1 @ (Op2 @ v) - Op2 @ (Op1 @ v)))
    check(f"{tag}: C4, C10, P4, OmF pairwise commute (vector probe)",
          cerr < 1e-9, f"(max err {cerr:.1e})")

    # -- slot projectors via joint spectral interpolation ---------------------
    PC4 = {1.5: (5.5 * IdenV - C4V) / 4.0, 5.5: (C4V - 1.5 * IdenV) / 4.0}
    PC10 = {11.25: (21.25 * IdenV - C10V) / 10.0,
            21.25: (C10V - 11.25 * IdenV) / 10.0}
    POm = {+1: 0.5 * (IdenV + OmF_V), -1: 0.5 * (IdenV - OmF_V)}
    PP4 = {}
    for f in fs:
        prod = None
        for g in fs:
            if g == f:
                continue
            factor = (P4V - c * g * IdenV) / (c * (f - g))
            prod = factor if prod is None else prod @ factor
        PP4[f] = prod

    coarse = {}
    for c4 in (1.5, 5.5):
        for c10 in (11.25, 21.25):
            for om in (+1, -1):
                coarse[(c4, c10, om)] = PC4[c4] @ PC10[c10] @ POm[om]
    for om in (+1, -1):
        emp = fro(coarse[(5.5, 21.25, om)])
        check(f"{tag}: coarse cell (11/2, 85/4, {om:+d}) empty -- no (3,2)x144 type",
              emp < 1e-6, f"(|.|_F {emp:.1e})")

    P = {}
    for name, c4, c10, om, f, dim in SLOT_DEFS:
        P[name] = coarse[(c4, c10, om)] @ PP4[f]
    del coarse, PP4, PC4, PC10, POm

    ide = max(mx(P[n] @ P[n] - P[n]) for n in P)
    check(f"{tag}: all 12 slot projectors idempotent", ide < T_PROJ,
          f"(max err {ide:.1e})")
    terr = max(abs(np.trace(P[n]).real - d) + abs(np.trace(P[n]).imag)
               for (n, _, _, _, _, d) in SLOT_DEFS)
    check(f"{tag}: slot traces exact: 4x96 + 4x288 + 4x64 = 1536 + 256 = 1792",
          terr < 1e-6, f"(max err {terr:.1e})")
    comp = mx(sum(P.values()) - IdenV)
    check(f"{tag}: completeness sum_slots P = I on V", comp < T_PROJ,
          f"(max err {comp:.1e})")

    if primary:
        oerr = 0.0
        keys = list(P)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                oerr = max(oerr, mx(P[keys[i]] @ P[keys[j]]))
        check(f"{tag}: pairwise orthogonality of all 66 slot pairs",
              oerr < T_PROJ, f"(max err {oerr:.1e})")
        # equivariance under sampled subalgebra generators (incl. mixed-signature)
        gens = [(base[0], base[1]), (base[0], base[3]),
                (intern[0], intern[1]), (intern[0], intern[-1])]
        eerr = 0.0
        for (a, b) in gens:
            R = np.kron(vec_gen(a, b, eta), I128) + np.kron(I14, spin_gen(a, b, e))
            for n in P:
                eerr = max(eerr, mx(P[n] @ R - R @ P[n]))
        check(f"{tag}: slot projectors equivariant (4 sampled generators)",
              eerr < 1e-6, f"(max err {eerr:.1e})")

    # X slots lie in ker T (gamma-trace annihilation); total chirality grading
    kerr = max(mx(T @ P[n]) for n in X_SLOTS)
    check(f"{tag}: all 8 X slots inside ker(gamma-trace)", kerr < 1e-6,
          f"(max err {kerr:.1e})")
    Omega_V = np.kron(I14, omega)
    chi = {}
    gerr = 0.0
    for n in P:
        q = complex(np.sum(Omega_V.T * P[n])) / np.trace(P[n])
        chi[n] = int(round(q.real))
        if primary and n in X_SLOTS:
            gerr = max(gerr, mx(Omega_V @ P[n] - q * P[n]))
    if primary:
        check(f"{tag}: every X slot has definite total chirality", gerr < 1e-6,
              f"(max err {gerr:.1e})")
    check(f"{tag}: X slots have chirality +/-1; SM sectors mix (32+32, trace 0)",
          all(abs(chi[n]) == 1 for n in X_SLOTS)
          and all(chi[n] == 0 for n in P if n not in X_SLOTS))
    blocks_ok = (chi["X32p"] == chi["X23m"] == chi["X2Tp"] == chi["X1Tm"]
                 and chi["X32m"] == chi["X23p"] == chi["X2Tm"] == chi["X1Tp"]
                 == -chi["X32p"])
    check(f"{tag}: chirality blocks match B5 table rows "
          f"({{X32p,X23m,X2Tp,X1Tm}} vs mirrors)", blocks_ok,
          f"(X32p block: {chi['X32p']:+d})")
    rec["total_chirality"] = {n: chi[n] for n in P}

    # -- THE MEASUREMENT: permutation action of J on the slots ----------------
    names = [s[0] for s in SLOT_DEFS]
    Q = {}
    for n in names:
        Q[n] = KM @ np.conj(P[n]) @ KMi
    D = np.zeros((len(names), len(names)))
    for jn, nj in enumerate(names):
        for in_, ni in enumerate(names):
            D[in_, jn] = fro(P[ni] - Q[nj])
    perm = {}
    matched = []
    unmatched = []
    for jn, nj in enumerate(names):
        order = np.argsort(D[:, jn])
        perm[nj] = names[order[0]]
        matched.append(D[order[0], jn])
        unmatched.append(D[order[1], jn])
    max_match = max(matched)
    min_unmatch = min(unmatched)
    check(f"{tag}: J maps every slot projector exactly onto a slot projector",
          max_match < T_MATCH,
          f"(max matched dist {max_match:.2e})")
    check(f"{tag}: match separation is decisive",
          min_unmatch / max(max_match, 1e-300) > SEP_MIN,
          f"(min unmatched {min_unmatch:.3e}; ratio {min_unmatch/max(max_match,1e-300):.1e})")
    check(f"{tag}: the J-permutation is a bijection",
          sorted(perm.values()) == sorted(names))
    check(f"{tag}: the J-permutation is an involution",
          all(perm[perm[n]] == n for n in names))
    check(f"{tag}: the J-permutation preserves total chirality ([J,omega]=0)",
          all(chi[n] == chi[perm[n]] for n in names))

    if all(perm[n] == n for n in names):
        classification = "WITHIN"
    elif perm == EXCHANGE_PERM:
        classification = "EXCHANGE_SAME_CHIRALITY_PAIRS"
    else:
        classification = "OTHER:" + json.dumps(perm)
    check(f"{tag}: classification is WITHIN or the same-chirality exchange",
          classification in ("WITHIN", "EXCHANGE_SAME_CHIRALITY_PAIRS"),
          classification)

    # J is NEVER the documented B5 mirror coflip (mirror flips total chirality)
    mirror_dist = min(fro(P[MIRROR[n]] - Q[n]) for n in X_SLOTS)
    check(f"{tag}: J does NOT implement the B5 mirror coflip on any X slot",
          all(perm[n] != MIRROR[n] for n in X_SLOTS)
          and mirror_dist > 1.0,
          f"(min |P_mirror - JPJ^-1|_F {mirror_dist:.3f})")

    # consistency: measured classification == sign of J-conjugation on Om_F
    check(f"{tag}: classification consistent with J om_F J^-1 = ({sF:+.0f}) om_F",
          (classification == "WITHIN") == (sF > 0))

    rec["classification"] = classification
    rec["J_permutation"] = perm
    rec["max_matched_distance"] = max_match
    rec["min_unmatched_distance"] = min_unmatch
    rec["mirror_coflip_min_distance"] = mirror_dist
    print(f"\n  {tag} RESULT: {classification}")
    for n in X_SLOTS:
        print(f"    J : {n:>5s} -> {perm[n]:<5s}   "
              f"(dist {D[names.index(perm[n]), names.index(n)]:.2e})")
    return rec


def main():
    print("=" * 78)
    print("OQ-RK1 J-restriction probe: quaternionic structure vs D2 x D5 branching")
    print("=" * 78)

    # [0] Clifford positive controls -----------------------------------------
    e, eta, omega = build_clifford_9_5()
    Iden = np.eye(DIMS, dtype=complex)
    IdenV = np.eye(DIMV, dtype=complex)
    err = 0.0
    for a in range(N14):
        for b in range(N14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            err = max(err, mx(anti - (2 * eta[a] if a == b else 0) * Iden))
    check("Clifford relations {e_a,e_b} = 2 eta_ab, signature (9,5)",
          err < T_EXACT, f"(max err {err:.1e})")
    check("omega^2 = +I and omega Hermitian",
          mx(omega @ omega - Iden) < T_EXACT
          and mx(omega - omega.conj().T) < T_EXACT)

    # [1] J certificate -------------------------------------------------------
    M = build_quaternionic_structure(e)
    check("J^2 = -I (M conj(M) = -I): quaternionic, not real",
          mx(M @ M.conj() + Iden) < T_EXACT)
    rng = np.random.default_rng(0)
    x = rng.standard_normal(DIMS) + 1j * rng.standard_normal(DIMS)
    check("J antilinear: J(ix) = -i J(x)",
          mx(M @ np.conj(1j * x) + 1j * (M @ np.conj(x))) < T_EXACT)
    jerr = max(mx(M @ e[a].conj() - e[a] @ M) for a in range(N14))
    check("J commutes with every Clifford generator e_a", jerr < T_EXACT,
          f"(max err {jerr:.1e})")
    serr = 0.0
    for a in range(N14):
        for b in range(a + 1, N14):
            B = spin_gen(a, b, e)
            serr = max(serr, mx(M @ B.conj() - B @ M))
    check("J commutes with all 91 so(9,5) generators Sigma_ab", serr < T_EXACT,
          f"(max err {serr:.1e})")
    check("J commutes with omega", mx(M @ omega.conj() - omega @ M) < T_EXACT)

    # [2] common RS fiber and J on V -----------------------------------------
    T = np.hstack([e[a] for a in range(N14)])  # gamma-trace map V -> S
    check("gamma-trace map T is 128 x 1792 and surjective",
          T.shape == (DIMS, DIMV)
          and int(np.linalg.matrix_rank(T, tol=1e-9)) == DIMS)
    KM = np.kron(np.eye(N14, dtype=complex), M)
    KMi = np.kron(np.eye(N14, dtype=complex), -np.conj(M))  # M^-1 = -conj(M)
    check("(I (x) M)(I (x) M^-1) = I on V", mx(KM @ KMi - IdenV) < T_EXACT)
    check("J_V is T-equivariant: T (I(x)M) = M conj(T) (ker T is J-stable)",
          mx(T @ KM - M @ np.conj(T)) < T_EXACT)

    # [3][4] per-split slot construction + measurement ------------------------
    SPLITS = [
        ("(3,1)", (0, 1, 2, 9), True),      # Lorentzian observer base (primary)
        ("(1,3)", (0, 9, 10, 11), False),   # opposite Lorentzian convention
        ("(4,0)", (0, 1, 2, 3), False),     # Euclidean base
        ("(2,2)", (0, 1, 9, 10), False),    # split base
        ("(0,4)", (9, 10, 11, 12), False),  # anti-Euclidean base
    ]
    records = {}
    for tag, base_idx, primary in SPLITS:
        records[tag] = run_split(tag, base_idx, e, eta, omega, M, KM, KMi, T,
                                 IdenV, primary)

    # [5] the cross-split law -------------------------------------------------
    print("\n" + "=" * 78)
    print("CROSS-SPLIT LAW")
    print("=" * 78)
    for tag, base_idx, _ in SPLITS:
        r = records[tag]
        q_base = sum(1 for a in base_idx if eta[a] == -1)
        expected = "WITHIN" if q_base % 2 == 0 else "EXCHANGE_SAME_CHIRALITY_PAIRS"
        check(f"law: base {tag} (q_base={q_base}) -> {expected}",
              r["classification"] == expected)
        print(f"  base {tag}  internal {r['internal_signature']}  "
              f"c = {r['P4_left_scalar_c'][0]:+.2f}{r['P4_left_scalar_c'][1]:+.2f}i  "
              f"om_F phase {r['c_internal_phase']:>1s}  ->  {r['classification']}")
    check("classification depends ONLY on parity of timelike directions in the "
          "4-plane; Lorentzian allocations (3,1)/(1,3) give EXCHANGE, "
          "(4,0)/(2,2)/(0,4) give WITHIN",
          all(records[t]["classification"]
              == ("WITHIN" if sum(1 for a in b if eta[a] == -1) % 2 == 0
                  else "EXCHANGE_SAME_CHIRALITY_PAIRS")
              for t, b, _ in SPLITS))
    check("in NO split does J implement the B5 mirror coflip "
          "(J preserves total chirality; the mirror flips it)",
          all(all(records[t]["J_permutation"][n] != MIRROR[n] for n in X_SLOTS)
              for t, _, _ in SPLITS))

    print("\n" + "=" * 78)
    print("LAYER-0 FENCE (verbatim):")
    print("this computation classifies the antiunitary's action on a")
    print("decomposition; it does NOT by itself compute rank_H(S_RS^+), does NOT")
    print("close OQ-RK1 (which is BLOCKED_NEEDS_SPEC on the physical projector")
    print("Π_RS^phys per tests/oq_rk1_e_rs_eff_assembly.py), and no count claim")
    print("follows. How the H-structure factorizes across the tensor splitting is")
    print("a naming/spec question this probe INFORMS, not answers.")
    print("=" * 78)
    print(f"\nALL {CHECKS['n']} CHECKS PASSED")
    print("\nMACHINE JSON:")
    print(json.dumps(records, indent=2, default=str))
    return records


if __name__ == "__main__":
    main()
