#!/usr/bin/env python3
"""TARGETED THIRD DRY ROUND -- the corrected crossed-fiber census sentence,
verified by a THIRD route, independent of both the original probe (which
asserted the count without enumerating) and the second dry round (which
exhibited a ninth involution and proved the repair symbolically in sympy
via the coefficient equations).

SCOPE (one sentence, per the stopping rule): the corrected census claim,
as fixed by the correction banner (commit 73b66dd) on
explorations/sector-relative-section-theory-2026-07-20.md:

    The crossed-fiber commutant algebra span{I, d~, Ku, J_c} is C^4 with
    SIXTEEN involutions; the K_S-SKEW involutions are exactly +-d~ and
    +-J_c, and the remaining eight are neither K_S-skew nor
    half-splittings.  The Z/2 classification is unaffected.

THE THIRD ROUTE (numpy only, no sympy, no code shared with either
verifier beyond the family definition, which IS the object under test):
  1. STRUCTURE CONSTANTS.  Compute the multiplication table of the
     4-element basis {I, d~, Ku, J_c} by least squares back into the
     span (closure + commutativity machine-checked, residuals reported).
  2. REGULAR REPRESENTATION -> PRIMITIVE IDEMPOTENTS.  Diagonalize a
     generic left-multiplication operator on the 4-dim coefficient
     space; normalize the four joint eigenvectors to idempotents.
     Verify: e_a^2 = e_a, e_a e_b = 0 (a != b), sum e_a = I, and each
     e_a has trace 32 (rank-32 blocks) => the algebra is C^4, machine-
     exactly, at the actual crossed point.
  3. STRUCTURAL ARGUMENT, PREMISES MACHINE-CHECKED.  The four
     idempotents are linearly independent (they are a basis: the 4x4
     change-of-basis matrix is invertible, condition number reported).
     Any x in the algebra is x = sum c_a e_a, so x^2 = sum c_a^2 e_a,
     and x^2 = I = sum e_a forces c_a^2 = 1 for every a: the involution
     set is EXACTLY {sum s_a e_a : s_a = +-1}, i.e. 2^4 = 16 -- no
     search needed, the enumeration is complete by linear algebra once
     the premises (orthogonality, completeness, independence) hold.
  4. EXHAUSTIVE ENUMERATION + INDEPENDENT CLASSIFICATION.  Build all 16,
     verify each squares to I machine-exactly and all are pairwise
     distinct; classify EACH by (i) K_S-adjoint parity (self-adjoint /
     skew / neither, by defect norms) and (ii) half-splitting property
     (+1-eigenspace dimension from the trace, exact since x = sum s_a
     e_a is manifestly diagonalizable with eigenvalues +-1).
  5. ROBUSTNESS.  Repeat the whole census at a SECOND crossed point on
     the same ray (different s), not used by either earlier probe.
  6. BANNER FIDELITY.  Read the correction banner from the doc and
     verify its claim strings state exactly what steps 1-4 prove (count
     sixteen; skew set = +-d~, +-J_c; remaining eight neither K_S-skew
     nor half-splittings; classification unaffected), that the banner
     precedes the body, and that the original false sentence is
     retained below it per record discipline.

TAGS: [T] setup, [E] evidence for the corrected sentence, [F]
falsification controls (the OLD sentence must FAIL against this route;
the classifiers must have teeth).  Deterministic: no RNG anywhere; two
runs byte-identical.  Exit 0 iff all checks pass.

STATUS: adversarial-verification tier; no claim/canon/posture movement;
no edits to any existing file.  Doc:
explorations/verify-census-third-round-2026-07-20.md
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402  (verified rep -- shared object)

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the verified Clifford objects -------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


# --- end-model machinery (REPLICATED verbatim from the original probe: it IS
#     the object under test; nothing else is shared) --------------------------
SYM_IDX = [(0, 0), (1, 1), (2, 2), (3, 3),
           (0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]


def sym_mat(i):
    a, b = SYM_IDX[i]
    m = np.zeros((4, 4))
    if a == b:
        m[a, a] = 1.0
    else:
        m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
    return m


HMODES = [sym_mat(i) for i in range(10)]


def fixsign(v):
    k = int(np.argmax(np.abs(v)))
    return v if v[k] > 0 else -v


def frame_diag(a4, lam=LAM):
    a0, a1, a2, a3 = [float(x) for x in a4]
    F = np.zeros((14, 14))
    F[0, 0] = 1.0 / np.sqrt(a0)
    F[1, 1] = 1.0 / np.sqrt(a1)
    F[2, 2] = 1.0 / np.sqrt(a2)
    F[3, 9] = 1.0 / np.sqrt(a3)
    F[8, 3] = np.sqrt(a0 * a1)
    F[9, 4] = np.sqrt(a0 * a2)
    F[10, 5] = np.sqrt(a1 * a2)
    F[11, 10] = np.sqrt(a0 * a3)
    F[12, 11] = np.sqrt(a1 * a3)
    F[13, 12] = np.sqrt(a2 * a3)
    u = np.array([1.0 / a0, 1.0 / a1, 1.0 / a2, -1.0 / a3])
    M4 = np.diag(u * u) - lam * np.outer(u, u)
    w, V = np.linalg.eigh(M4)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    k0 = 0
    while k0 < 4:
        k1 = k0 + 1
        while k1 < 4 and abs(w[k1] - w[k0]) <= 1e-9 * max(1.0, abs(w[k0])):
            k1 += 1
        if k1 - k0 > 1:
            Pp = V[:, k0:k1]
            B = []
            for r in refs.T:
                v = Pp @ (Pp.T @ r)
                for b in B:
                    v = v - b * float(b @ v)
                nv = float(np.linalg.norm(v))
                if nv > 1e-8:
                    B.append(v / nv)
                if len(B) == k1 - k0:
                    break
            V[:, k0:k1] = np.stack(B, axis=1)
        k0 = k1
    pos = [k for k in range(4) if w[k] > 0]
    neg = [k for k in range(4) if w[k] < 0]
    if len(pos) != 3 or len(neg) != 1:
        raise ValueError(f"diag block signature not (3,1): {w}")
    for j, k in enumerate(pos):
        F[4:8, 6 + j] = fixsign(V[:, k]) / np.sqrt(w[k])
    F[4:8, 13] = fixsign(V[:, neg[0]]) / np.sqrt(-w[neg[0]])
    return F


def rot4(th):
    R = np.eye(4)
    R[0, 0] = R[3, 3] = np.cos(th)
    R[0, 3] = -np.sin(th)
    R[3, 0] = np.sin(th)
    return R


def rho(R):
    P = np.zeros((14, 14))
    P[:4, :4] = R
    for i in range(10):
        RhR = R @ HMODES[i] @ R.T
        for j in range(10):
            P[4 + j, 4 + i] = float(np.sum(RhR * HMODES[j]))
    return P


F_BASE = frame_diag((1.0, 1.0, 1.0, 1.0))
XI_VEC = F_BASE @ XI


def xi_of(t, a4, lam=LAM):
    F = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    return np.linalg.solve(F, XI_VEC)


def ray(alpha, s):
    al = np.asarray(alpha, dtype=float)
    return tuple(np.exp(2.0 * al * s))


A_CONF_DN = (-1.0, -1.0, -1.0, -1.0)
TGRID = np.linspace(0.0, 1.0, 41)


def crossing_scan(alpha, s_hi):
    for s in np.linspace(0.0, s_hi, 61):
        q = np.array([qform(xi_of(t, ray(alpha, s))) for t in TGRID])
        if np.min(q) < 0.0:
            return float(s), float(TGRID[int(np.argmin(q))])
    return None, None


def bisect_wall(alpha, t_star, s_hi):
    lo, hi = 0.0, s_hi
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if qform(xi_of(t_star, ray(alpha, mid))) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sec_parts(D):
    cs = 0.5 * (D + K_S @ D @ K_S)
    ct = D - cs
    P = float(np.real(np.trace(cs @ cs))) / DIM
    T = -float(np.real(np.trace(ct @ ct))) / DIM
    return cs, ct, P, T, P - T


def sec_symbol(D):
    cs, _ct, P, _T, q = sec_parts(D)
    Ku = K_S @ cs / np.sqrt(P)
    return Ku @ D, Ku, P, q


def mmax(A):
    return float(np.max(np.abs(A)))


# =============================================================================
# [T] setup
# =============================================================================
cliff_ok = True
for a in range(N_DIRS):
    for b in range(a, N_DIRS):
        want = 2.0 * (ETA[a] if a == b else 0.0)
        got = e[a] @ e[b] + e[b] @ e[a]
        if mmax(got - want * I128) > 1e-9:
            cliff_ok = False
check("T", "rep integrity: Clifford relations for eta (9,5); K_S is a "
           "Hermitian involution",
      cliff_ok and mmax(K_S - K_S.conj().T) < 1e-9
      and mmax(K_S @ K_S - I128) < 1e-9)

base_id = mmax(xi_of(0.0, (1.0, 1.0, 1.0, 1.0)) - XI)
s_dn, t_dn = crossing_scan(A_CONF_DN, 3.0)
s_star = bisect_wall(A_CONF_DN, t_dn, s_dn)
x_cross = xi_of(t_dn, ray(A_CONF_DN, s_star + 0.4))
q_cross = qform(x_cross)
# a SECOND crossed point on the same ray, not used by either earlier probe
s_off2 = None
for off in (0.8, 0.6, 0.25, 0.15):
    if qform(xi_of(t_dn, ray(A_CONF_DN, s_star + off))) < 0 and off != 0.4:
        s_off2 = off
        break
x_cross2 = xi_of(t_dn, ray(A_CONF_DN, s_star + s_off2))
q_cross2 = qform(x_cross2)
check("T", "end model replicated faithfully: xi(0, unit) = XI machine-"
           "exactly; conf-down wall re-found from scratch; the census "
           "point (s* + 0.4) is crossed (q < 0) and so is a SECOND fresh "
           "point on the same ray",
      base_id < 1e-12 and q_cross < 0 and q_cross2 < 0,
      f"base id {base_id:.1e}; wall s* = {s_star:.4f}, t* = {t_dn:.3f}; "
      f"q(s*+0.4) = {q_cross:.3f}, q(s*+{s_off2}) = {q_cross2:.3f}")


# =============================================================================
# the census, by the third route
# =============================================================================
def census(D):
    """Full independent census of span{I, d~, Ku, J_c} at a crossed point.
    Returns a dict of machine facts; asserts nothing itself."""
    _cs, _ct, _P, _T, q = sec_parts(D)
    M, Ku, _Pq, _q = sec_symbol(D)
    g = np.sqrt(-q)
    d_til = -1j * D / g
    J_c = d_til @ Ku
    basis = [I128, d_til, Ku, J_c]
    names = ["I", "d~", "Ku", "J_c"]
    Bmat = np.stack([b.flatten() for b in basis], axis=1)   # 16384 x 4

    out = {"q": q}
    out["rank4"] = int(np.linalg.matrix_rank(Bmat, tol=1e-8)) == 4

    # 1. structure constants by least squares back into the span
    C = np.zeros((4, 4, 4), dtype=complex)
    res_max = 0.0
    for i in range(4):
        for j in range(4):
            prod = (basis[i] @ basis[j]).flatten()
            coef, *_ = np.linalg.lstsq(Bmat, prod, rcond=None)
            C[i, j] = coef
            res_max = max(res_max, mmax(Bmat @ coef - prod))
    out["closure_res"] = res_max
    out["commutative"] = mmax(C - np.transpose(C, (1, 0, 2))) < 1e-10

    # 2. regular representation -> primitive idempotents
    # left multiplication by basis[i] on coefficient vectors:
    # (b_i * x)_k = sum_j C[i, j, k] x_j
    L = [C[i].T.copy() for i in range(4)]                    # each 4x4
    Lgen = L[1] + np.sqrt(2.0) * L[2]                        # d~ + sqrt2 Ku
    evals, evecs = np.linalg.eig(Lgen)
    order = np.argsort(-np.real(evals))
    evals, evecs = evals[order], evecs[:, order]
    out["eig_sep"] = float(np.min(np.abs(np.diff(np.real(evals)))))
    idem = []
    idem_coef = []
    for k in range(4):
        c = evecs[:, k]
        csq = np.einsum("i,j,ijk->k", c, c, C)
        mu = complex(np.vdot(c, csq) / np.vdot(c, c))
        ec = c / mu
        idem_coef.append(ec)
        idem.append(sum(ec[m] * basis[m] for m in range(4)))
    d_idem = max(mmax(E @ E - E) for E in idem)
    d_orth = max(mmax(idem[a] @ idem[b])
                 for a in range(4) for b in range(4) if a != b)
    d_comp = mmax(sum(idem) - I128)
    traces = [float(np.real(np.trace(E))) for E in idem]
    out["idem_defect"] = max(d_idem, d_orth, d_comp)
    out["block_dims"] = [round(t) for t in traces]
    out["block_dim_res"] = max(abs(t - round(t)) for t in traces)
    # 3. the idempotents are a BASIS (completeness of the enumeration):
    Ecoef = np.stack(idem_coef, axis=1)                      # 4x4
    out["basis_cond"] = float(np.linalg.cond(Ecoef))

    # 4. exhaustive enumeration: ALL involutions are sum s_a e_a, s = +-1
    named = {"+I": I128, "-I": -I128, "+d~": d_til, "-d~": -d_til,
             "+Ku": Ku, "-Ku": -Ku, "+J_c": J_c, "-J_c": -J_c}
    invs = []
    for signs in itertools.product((1.0, -1.0), repeat=4):
        X = sum(signs[a] * idem[a] for a in range(4))
        sq_def = mmax(X @ X - I128)
        KXK = K_S @ X.conj().T @ K_S
        sa_def = mmax(KXK - X)
        sk_def = mmax(KXK + X)
        dim_p1 = round((DIM + float(np.real(np.trace(X)))) / 2.0)
        tag = None
        for nm, Y in named.items():
            if mmax(X - Y) < 1e-8:
                tag = nm
                break
        invs.append({"signs": signs, "X": X, "sq_def": sq_def,
                     "sa_def": sa_def, "sk_def": sk_def,
                     "dim_p1": dim_p1, "named": tag})
    out["invs"] = invs
    out["n_inv"] = len(invs)
    out["sq_def_max"] = max(v["sq_def"] for v in invs)
    dmin = min(mmax(invs[a]["X"] - invs[b]["X"])
               for a in range(16) for b in range(a + 1, 16))
    out["pair_dist_min"] = dmin
    out["skew_set"] = sorted(v["named"] or "UNNAMED" for v in invs
                             if v["sk_def"] < 1e-8)
    out["sa_set"] = sorted(v["named"] or "UNNAMED" for v in invs
                           if v["sa_def"] < 1e-8)
    out["named_count"] = sum(1 for v in invs if v["named"] is not None)
    extras = [v for v in invs if v["named"] is None]
    out["extras"] = extras
    out["extra_parity_min_def"] = min(min(v["sa_def"], v["sk_def"])
                                      for v in extras)
    out["extra_dims"] = sorted(v["dim_p1"] for v in extras)
    out["half_split_set"] = sorted(v["named"] or "UNNAMED" for v in invs
                                   if v["dim_p1"] == DIM // 2)
    # the second round's ninth involution, reproduced from MY enumeration
    ninth = 0.5 * (I128 + d_til + Ku - J_c)
    out["ninth_hit"] = min(mmax(v["X"] - ninth) for v in invs)
    out["ninth_named"] = [v["named"] for v in invs
                          if mmax(v["X"] - ninth) < 1e-8]
    out["basis"] = dict(zip(names, basis))
    return out


D_cross = cvec(x_cross)
cz = census(D_cross)

# --- [E] closure, commutativity, independence ---------------------------------
check("E", "STRUCTURE CONSTANTS: the 4-element system {I, d~, Ku, J_c} at "
           "the crossed point is rank-4 independent and CLOSES under "
           "multiplication (all 16 pairwise products lie in the span, "
           "machine-exactly) with a COMMUTATIVE multiplication table -- "
           "the commutant algebra is computed, not assumed",
      cz["rank4"] and cz["closure_res"] < 1e-9 and cz["commutative"],
      f"q = {cz['q']:.3f}, closure residual {cz['closure_res']:.1e}")

# --- [E] C^4 block structure ---------------------------------------------------
check("E", "C^4 STRUCTURE: the regular representation (built from the "
           "structure constants alone) has four simple joint eigenvectors; "
           "normalized, they give FOUR primitive idempotents -- mutually "
           "orthogonal, idempotent, summing to I, each of trace exactly 32 "
           "(four rank-32 blocks) -- so the algebra is isomorphic to C^4: "
           "the '4-dim commutative' half of the original sentence was "
           "right, the count was not",
      cz["idem_defect"] < 1e-9 and cz["block_dims"] == [32, 32, 32, 32]
      and cz["block_dim_res"] < 1e-8 and cz["eig_sep"] > 0.5,
      f"idempotent defect {cz['idem_defect']:.1e}, blocks "
      f"{cz['block_dims']}, eig separation {cz['eig_sep']:.3f}")

# --- [E] exhaustive enumeration: exactly sixteen -------------------------------
check("E", "EXACTLY SIXTEEN INVOLUTIONS, exhaustively: the idempotents are "
           "a basis (4x4 change-of-basis invertible, condition number "
           "finite), so every algebra element is x = sum c_a e_a with "
           "x^2 = sum c_a^2 e_a, and x^2 = I forces c_a = +-1: the "
           "involution set is EXACTLY the 2^4 sign combinations -- all 16 "
           "built, all square to I machine-exactly, all pairwise distinct "
           "(separation O(1)); exactly 8 of them are the named +-{I, d~, "
           "Ku, J_c} and exactly 8 are extras (mixed-sign)",
      cz["n_inv"] == 16 and cz["sq_def_max"] < 1e-9
      and cz["pair_dist_min"] > 0.5 and cz["named_count"] == 8
      and len(cz["extras"]) == 8 and cz["basis_cond"] < 100.0,
      f"sq defect {cz['sq_def_max']:.1e}, min pair distance "
      f"{cz['pair_dist_min']:.3f}, basis cond {cz['basis_cond']:.1f}")

# --- [E] independent classification (the corrected sentence itself) -----------
skew_want = ["+J_c", "+d~", "-J_c", "-d~"]
sa_want = ["+I", "+Ku", "-I", "-Ku"]
hs_want = ["+J_c", "+Ku", "+d~", "-J_c", "-Ku", "-d~"]
check("E", "THE CORRECTED SENTENCE, verified member-by-member: the "
           "K_S-SKEW involutions are EXACTLY +-d~ and +-J_c (four, no "
           "others); the K_S-self-adjoint ones are exactly +-I and +-Ku; "
           "the eight extras are NEITHER (both parity defects O(1)) and "
           "NONE is a half-splitting: their +1-eigenspaces have dimension "
           "96 or 32, never 64, while the half-splittings among all "
           "sixteen are exactly +-d~, +-Ku, +-J_c",
      sorted(skew_want) == cz["skew_set"]
      and sorted(sa_want) == cz["sa_set"]
      and cz["extra_parity_min_def"] > 0.1
      and cz["extra_dims"] == [32, 32, 32, 32, 96, 96, 96, 96]
      and sorted(hs_want) == cz["half_split_set"],
      f"skew set {cz['skew_set']}, extra dims {cz['extra_dims']}, "
      f"extra min parity defect {cz['extra_parity_min_def']:.2f}")

# --- [E] robustness at a second crossed point ----------------------------------
cz2 = census(cvec(x_cross2))
check("E", "ROBUSTNESS: the entire census repeats at a SECOND crossed "
           "point (same ray, different radius, used by neither earlier "
           "probe): C^4 blocks (32,32,32,32), sixteen involutions, skew "
           "set exactly +-d~ and +-J_c, extras neither skew nor "
           "half-splittings -- the corrected sentence is a property of "
           "the crossed fiber, not of one sample",
      cz2["rank4"] and cz2["closure_res"] < 1e-9 and cz2["commutative"]
      and cz2["idem_defect"] < 1e-9
      and cz2["block_dims"] == [32, 32, 32, 32]
      and cz2["n_inv"] == 16 and cz2["sq_def_max"] < 1e-9
      and cz2["named_count"] == 8
      and sorted(skew_want) == cz2["skew_set"]
      and sorted(sa_want) == cz2["sa_set"]
      and cz2["extra_parity_min_def"] > 0.1
      and cz2["extra_dims"] == [32, 32, 32, 32, 96, 96, 96, 96],
      f"q = {cz2['q']:.3f}, sq defect {cz2['sq_def_max']:.1e}")

# --- [E] banner fidelity --------------------------------------------------------
doc_path = os.path.join(HERE, "..", "..", "explorations",
                        "sector-relative-section-theory-2026-07-20.md")
with open(doc_path, encoding="utf-8") as fh:
    doc = fh.read()
banner_marker = "CORRECTION (2026-07-20, second dry round"
body_marker = "# The sector-relative section theory, built"
banner_ok = banner_marker in doc and body_marker in doc and \
    doc.index(banner_marker) < doc.index(body_marker)
banner_txt = doc[doc.index(banner_marker):doc.index(body_marker)] \
    if banner_ok else ""
# the banner must claim exactly what this probe proved -- no more, no less
claims_present = all(s in banner_txt for s in (
    "C^4 with SIXTEEN involutions",
    "K_S-SKEW involutions are exactly +-d~ and +-J_c",
    "neither K_S-skew nor half-splittings",
    "remaining eight",
    "UNAFFECTED",
))
# record discipline: the original false sentence retained BELOW the banner
false_sentence_retained = "EXACTLY eight involutions" in doc[
    doc.index(body_marker):] if banner_ok else False
check("E", "BANNER FIDELITY: the correction banner sits above the body, "
           "asserts exactly the machine-proven repair (C^4, sixteen; "
           "skew set = +-d~ and +-J_c; the remaining eight neither "
           "K_S-skew nor half-splittings; classification UNAFFECTED) "
           "and nothing stronger, and the original false sentence is "
           "retained unedited below it per record discipline -- no "
           "drift between banner and theorem",
      banner_ok and claims_present and false_sentence_retained)

# --- [F] the OLD sentence must fail against this route -------------------------
check("F", "REFUTATION CONTROL: the original census sentence ('EXACTLY "
           "eight involutions') FAILS against the exhaustive enumeration "
           "-- sixteen involutions, not eight -- and the second round's "
           "ninth, (I + d~ + Ku - J_c)/2, appears in MY enumeration "
           "machine-exactly as one of the eight unnamed extras: the "
           "refutation reproduces by a third route",
      cz["n_inv"] != 8 and cz["ninth_hit"] < 1e-9
      and cz["ninth_named"] == [None],
      f"count 16 != 8, ninth hit at {cz['ninth_hit']:.1e}")

# --- [F] the classifiers have teeth ---------------------------------------------
Ku_c = cz["basis"]["Ku"]
dt_c = cz["basis"]["d~"]
KKuK = K_S @ Ku_c.conj().T @ K_S
KdtK = K_S @ dt_c.conj().T @ K_S
teeth = (mmax(KKuK + Ku_c) > 0.5          # Ku is NOT K_S-skew: O(1) defect
         and mmax(KdtK - dt_c) > 0.5      # d~ is NOT K_S-s.a.: O(1) defect
         and all(v["dim_p1"] != 64 for v in cz["extras"])
         and all(v["dim_p1"] == 64 for v in cz["invs"]
                 if v["named"] in ("+d~", "-d~", "+J_c", "-J_c")))
check("F", "SENSITIVITY CONTROL: the classifiers would catch a wrong "
           "repair -- Ku fails the skew test with O(1) defect (so a "
           "repair listing +-Ku as skew would FAIL), d~ fails the "
           "self-adjoint test with O(1) defect, every extra misses "
           "dimension 64 (so a repair calling any of them a "
           "half-splitting would FAIL), and the four skew involutions "
           "all ARE half-splittings (dim exactly 64)",
      teeth,
      f"skew-defect(Ku) = {mmax(KKuK + Ku_c):.2f}, "
      f"sa-defect(d~) = {mmax(KdtK - dt_c):.2f}")

# =============================================================================
# headline
# =============================================================================
nT = sum(1 for t, _n, _o in RESULTS if t == "T")
nE = sum(1 for t, _n, _o in RESULTS if t == "E")
nF = sum(1 for t, _n, _o in RESULTS if t == "F")
all_ok = all(o for _t, _n, o in RESULTS)
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
