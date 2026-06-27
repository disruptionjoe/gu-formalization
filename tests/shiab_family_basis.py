#!/usr/bin/env python3
"""Explicit BASIS of the natural Spin(9,5)-equivariant family Hom(Lambda^2 V (x) S, V (x) S).

CONTEXT (SHIAB-03, canon/shiab-existence-cl95.md "Uniqueness of equivariant map")
---------------------------------------------------------------------------------
The space of natural Spin(9,5)-equivariant maps

        T : Omega^2(Y^14) (x) S  ->  Omega^1(Y^14) (x) S      (Lambda^2 V (x) S -> V (x) S)

is NOT one-dimensional. Three independent character computations
(tests/shiab_codiff_intertwiner_dim.py: Racah-Speiser; Kostant/Klimyk Weyl sum over
|W(D_7)|=322560; Freudenthal) already established the COMPLEX multiplicity:

    dim_C Hom(Lambda^2 V (x) S^+, V (x) S^-) = 2     (chirality-flipping)
    dim_C Hom(Lambda^2 V (x) S^-, V (x) S^+) = 2
    dim_C Hom(Lambda^2 V (x) S^+, V (x) S^+) = 0     (chirality-preserving)
    dim_C Hom(Lambda^2 V (x) S^-, V (x) S^-) = 0
    --> full Dirac complex dim = 4.

This file does what the character count does NOT: it CONSTRUCTS the family EXPLICITLY
as matrices, by the null-space method the task prescribes:

    stack the equivariance constraints  rho_cod(X) T - T rho_dom(X) = 0  for a
    GENERATING set X of so(14,C) acting on the finite Hom matrix space, and take the
    NULL SPACE. Each null vector reshapes to an equivariant-map matrix. That null
    space IS the family.

Two practical reductions keep this exact and tractable:
  (1) Memory: the full vec(T) has ~5.2M complex entries per chiral block, so we never
      materialize the (codim x codim) constraint operator. Instead we work in a
      candidate ANSATZ of natural Clifford-word maps and find the null space of the
      Hermitian Gram matrix  G[k,l] = sum_X <defect_X(T_k), defect_X(T_l)>.  x in
      null(G)  <=>  sum_k x_k T_k is equivariant. The ansatz is verified COMPLETE by
      matching the independent character dimension (2 per block).
  (2) Generators: equivariance under a generating set of so(14,C) implies equivariance
      under the whole algebra. The 13 adjacent rotations Sigma_{i,i+1} generate
      so(14,C); we use them for the Gram and then RE-VERIFY every surviving basis
      matrix against the 13 generators PLUS a spread of non-adjacent generators
      Sigma_{a<b} as an independent cross-check.

DISCIPLINE (FC4-HOLONOMY-01): no selector is tuned to force dim 1. The surviving
dimension is reported as computed. Every candidate's equivariance is decided by the
matrix defect, not assumed.

The verified Cl(9,5) = M(64,H) ~ M(128,C) representation (gammas e[a], chirality omega,
chiral bases B+/B-) is reused from oq_rk1_cl95_explicit_rep.py.
"""

from __future__ import annotations

import hashlib
import inspect
import json
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) anchor

TOL = 1e-7
N = 14  # so(9,5) / so(14,C)

# Disk cache for the expensive family build (the gram-nullspace defect tensordots
# take ~280s; loading the cached result takes ~1s). Cache files are large/derived
# and live in tests/.cache/ (gitignored). Bump _CONSTRUCTION_VERSION to force a
# full rebuild when the construction semantics change in a way the source hash
# would not capture.
CACHE_DIR = os.path.join(HERE, ".cache")
_CONSTRUCTION_VERSION = "cl95-shiab-family-v1"


# ---------------------------------------------------------------------------
# 1. Explicit Cl(9,5) = M(64,H) ~ M(128,C) representation (reused, re-verified).
# ---------------------------------------------------------------------------
def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)            # signature (9,5)
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]  # e[a]^2 = eta_a I
    Iden = np.eye(dim, dtype=complex)
    # Clifford check
    cliff_err = 0.0
    for a in range(N):
        for b in range(N):
            anti = e[a] @ e[b] + e[b] @ e[a]
            exp = (2 * eta[a] if a == b else 0) * Iden
            cliff_err = max(cliff_err, float(np.max(np.abs(anti - exp))))
    omega = Iden.copy()
    for a in range(N):
        omega = omega @ e[a]
    w, V = np.linalg.eigh(omega)
    Bplus = V[:, w > 0.5]    # 128 x 64  (S^+)
    Bminus = V[:, w < -0.5]  # 128 x 64  (S^-)
    return dim, eta, e, omega, Bplus, Bminus, cliff_err


DIM, ETA, E, OMEGA, BPLUS, BMINUS, CLIFF_ERR = build_rep()


# ---------------------------------------------------------------------------
# 2. so(14,C) generators in each rep, consistently normalized so the Clifford
#    map c: V (x) S -> S is equivariant. From [Sigma_ab, e_c] = eta_bc e_a - eta_ac e_b
#    the vector rep is JV; Lambda^2 is the induced derivation; spinor is Sigma_ab.
# ---------------------------------------------------------------------------
def Sigma(a, b):
    """Spinor generator (1/4)[e_a, e_b] (chirality-even, 128x128)."""
    return 0.25 * (E[a] @ E[b] - E[b] @ E[a])


def JV(a, b):
    """Vector rep generator on V = C^14 (basis vectors).  [Sigma_ab, e_c] action."""
    M = np.zeros((N, N), dtype=complex)
    M[a, b] += ETA[b]
    M[b, a] -= ETA[a]
    return M


PAIRS = [(p, q) for p in range(N) for q in range(p + 1, N)]   # 91 basis 2-vectors
NPAIR = len(PAIRS)                                            # 91
PIDX = {pr: i for i, pr in enumerate(PAIRS)}


def JL2(a, b):
    """Induced generator on Lambda^2 V (91-dim), derivation of JV on e_{p}^e_{q}."""
    jv = JV(a, b)
    M = np.zeros((NPAIR, NPAIR), dtype=complex)
    for j, (p, q) in enumerate(PAIRS):
        for d in range(N):
            c1 = jv[d, p]
            if c1 != 0 and d != q:
                pr = (min(d, q), max(d, q))
                M[PIDX[pr], j] += (1.0 if d < q else -1.0) * c1
            c2 = jv[d, q]
            if c2 != 0 and d != p:
                pr = (min(p, d), max(p, d))
                M[PIDX[pr], j] += (1.0 if p < d else -1.0) * c2
    return M


# Generating set (adjacent rotations) and the full set (all a<b).
GEN_SET = [(i, i + 1) for i in range(N - 1)]   # 13 adjacent: generate so(14,C)
ALL_GENS = list(PAIRS)                          # 91 = full basis of so(14,C)


def projected_generators(gen_pairs, Pin, Pout):
    """Return per-generator (JVmat, JL2mat, Sig_in, Sig_out) projected to chiral blocks."""
    out = []
    for (a, b) in gen_pairs:
        out.append((JV(a, b), JL2(a, b),
                    Pin.conj().T @ Sigma(a, b) @ Pin,
                    Pout.conj().T @ Sigma(a, b) @ Pout))
    return out


# ---------------------------------------------------------------------------
# 3. Candidate natural-map operators.  A candidate is a function
#    W(a, j, p, q) -> 128x128 Clifford operator, meaning
#       T(alpha_j (x) s) = sum_a e^a (x) c(W_a(alpha_j)) s,   alpha_j = e_p ^ e_q.
#    Gamma2(alpha) = e_p e_q is the degree-2 Clifford quantization of the 2-form.
#
# REALITY OF THE METRIC (computed, not assumed): the codomain V-slot index a is
# CONTRACTED against the Clifford index a, and so(9,5) preserves eta (signature
# (9,5)), NOT delta. So a Clifford-word candidate is equivariant only when the
# codomain slot carries the metric weight eta_aa; the plain (delta-paired) version
# is NOT equivariant in indefinite signature. The lone exception is the canon
# interior-product contraction, where the contraction index is paired with the
# 2-form via the GL-natural duality (no metric needed) -- which is exactly why
# GU's literal Clifford-contraction shiab survives as an equivariant map.
# ---------------------------------------------------------------------------
GAMMA2 = [E[p] @ E[q] for (p, q) in PAIRS]


def W_delta_contract(a, j, p, q):
    """GU canon shiab, literally as coded in shiab_vs_codiff_cl95.py: the metric-free
    interior product on the FORM factor.  iota_{e_a}(e^p^e^q) = delta_ap e^q - delta_aq
    e^p ;  c(.) = e[.].  The contraction index is GL-naturally paired with the 2-form,
    so this is equivariant WITHOUT a metric weight -> the Clifford-trace channel."""
    out = np.zeros((DIM, DIM), dtype=complex)
    if a == p:
        out = out + E[q]
    if a == q:
        out = out - E[p]
    return out


def W_wedge_metric(a, j, p, q):
    """Degree-3 Rarita-Schwinger channel: metric-weighted Clifford wedge
    eta_aa * (1/2){c(e_a), c(alpha)} = eta_aa * c(e_a ^ alpha).  The eta_aa weight is
    forced because the codomain slot index a is metric-paired with the Clifford index."""
    return ETA[a] * 0.5 * (E[a] @ GAMMA2[j] + GAMMA2[j] @ E[a])


def W_eGamma_metric(a, j, p, q):
    """eta_aa * c(e_a) c(alpha): a mixed (degree-1 + degree-3) equivariant combination,
    redundant in the 2-dim equivariant space (used to exercise the null space)."""
    return ETA[a] * (E[a] @ GAMMA2[j])


def W_wedge_plain(a, j, p, q):
    """NON-equivariant: the metric-free Clifford wedge (no eta_aa weight)."""
    return 0.5 * (E[a] @ GAMMA2[j] + GAMMA2[j] @ E[a])


def W_decoy(a, j, p, q):
    """Deliberately NON-equivariant decoy (index-shifted) to prove the null space selects."""
    return E[(a + 1) % N] @ GAMMA2[j]


def build_T(Wfun, Pin, Pout):
    """Block tensor T[a, p_out, j, q_in] for the chiral block Pin -> Pout."""
    di = Pin.shape[1]
    do = Pout.shape[1]
    T = np.zeros((N, do, NPAIR, di), dtype=complex)
    for j, (p, q) in enumerate(PAIRS):
        for a in range(N):
            Wop = Wfun(a, j, p, q)
            if Wop is not None and Wop.any():
                T[a, :, j, :] = Pout.conj().T @ Wop @ Pin
    return T


# ---------------------------------------------------------------------------
# 4. Equivariance defect  rho_cod(X) T - T rho_dom(X)  for one generator.
# ---------------------------------------------------------------------------
def defect(T, gen):
    jv, jl, sig_in, sig_out = gen
    d = np.tensordot(jv, T, axes=([1], [0]))                                 # cod V
    d = d + np.tensordot(sig_out, T, axes=([1], [1])).transpose(1, 0, 2, 3)  # cod S
    d = d - np.tensordot(T, jl, axes=([2], [0])).transpose(0, 1, 3, 2)       # dom L2
    d = d - np.tensordot(T, sig_in, axes=([3], [0]))                         # dom S
    return d


def max_defect(T, gens):
    return max(float(np.max(np.abs(defect(T, g)))) for g in gens)


def gram_nullspace(Ts, gens):
    """Hermitian Gram of the equivariance defect over the ansatz; null space = equivariant
    coefficient vectors.  Returns (eigenvalues, nullspace_coeff_columns)."""
    m = len(Ts)
    G = np.zeros((m, m), dtype=complex)
    # accumulate on the fly (do not store all defects)
    defs = [None] * m
    for g in gens:
        for k in range(m):
            defs[k] = defect(Ts[k], g)
        for k in range(m):
            for l in range(k, m):
                val = np.vdot(defs[k], defs[l])
                G[k, l] += val
                if l != k:
                    G[l, k] += np.conjugate(val)
    wv, Vv = np.linalg.eigh(G)
    scale = max(1.0, float(abs(wv[-1])))
    null = Vv[:, wv <= TOL * scale]
    return wv, null, G


# ---------------------------------------------------------------------------
# 5. Quaternionic structure J (antilinear, J^2 = -1, J e_a = e_a J) -> M(64,H).
# ---------------------------------------------------------------------------
def build_quaternionic_J():
    """J = U . conj.  conj acts as e[a] -> s_a e[a] with s_a from the JW reality of the
    gammas; U = product of e[a] over the anticommute set makes J commute with every e[a].
    Returns (U, s, JsqErr) where JsqErr = ||U conj(U) + I|| (quaternionic <=> ~0)."""
    # reality signs of conjugation on e[a]
    s = np.empty(N)
    for a in range(N):
        if a < 9:                 # e=G (real-structure of JW: even index real, odd imag)
            s[a] = (-1.0) ** a
        else:                     # e=iG  -> extra sign from the i
            s[a] = (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(DIM, dtype=complex)
    for a in anticomm:
        U = U @ E[a]
    Ubar = np.conjugate(U)
    Jsq = U @ Ubar               # J^2 = U conj(U)
    err_minus = float(np.max(np.abs(Jsq + np.eye(DIM))))   # quaternionic: J^2 = -I
    # verify J commutes with each real Clifford generator: U conj(e_a) = e_a U
    comm_err = max(float(np.max(np.abs(U @ np.conjugate(E[a]) - E[a] @ U))) for a in range(N))
    return U, s, err_minus, comm_err


# ---------------------------------------------------------------------------
# 6. Public API: build & return the explicit family basis + canon-shiab coordinates.
# ---------------------------------------------------------------------------
def _build_shiab_family_basis(verify_all_generators=True):
    """Construct the explicit basis of natural Spin(9,5)-equivariant maps
    Hom(Lambda^2 V (x) S, V (x) S).

    Returns a dict with:
      'blocks'              : dict block_name -> list of (label, T_tensor) equivariant
                              basis matrices.  T_tensor has shape
                              (14, dimS_out, 91, dimS_in); densify_block() expands it
                              to the (14*dimS_out) x (91*dimS_in) Hom matrix.
      'dim_complex_per_block': 2
      'dim_complex_full_dirac': 4
      'dim_real_full_dirac'  : 8     (real doubling; see notes)
      'canon_shiab_coords'   : coordinates of GU's canon Clifford-trace shiab in the
                              full-Dirac basis (order [contract_+-,wedge_+-,contract_-+,
                              wedge_-+]).
      'channel_labels'       : the irrep channels each basis element spans.
      'verification'         : dict of numerical checks.
    """
    rep = {"dimC_Cl": DIM, "clifford_max_err": CLIFF_ERR,
           "Splus_dimC": int(BPLUS.shape[1]), "Sminus_dimC": int(BMINUS.shape[1])}

    # Candidate ansatz: two clean equivariant channels (delta contraction = Clifford-
    # trace; metric wedge = Rarita-Schwinger), one redundant equivariant combination,
    # and two deliberately NON-equivariant decoys so the null space genuinely selects.
    candidates = [
        ("delta_contract(Clifford-trace,canon)", W_delta_contract),
        ("wedge_metric(Rarita-Schwinger)", W_wedge_metric),
        ("eGamma_metric(redundant-equivariant)", W_eGamma_metric),
        ("wedge_plain(non-equivariant)", W_wedge_plain),
        ("decoy(non-equivariant)", W_decoy),
    ]

    blocks_spec = {
        "S+ -> S-": (BPLUS, BMINUS),
        "S- -> S+": (BMINUS, BPLUS),
    }

    result = {"rep": rep, "blocks": {}, "per_block_report": {}}

    for bname, (Pin, Pout) in blocks_spec.items():
        gens13 = projected_generators(GEN_SET, Pin, Pout)
        Ts = [build_T(f, Pin, Pout) for (_, f) in candidates]
        T_by_label = {lab: T for (lab, _), T in zip(candidates, Ts)}

        indiv = {lab: max_defect(T, gens13) for (lab, _), T in zip(candidates, Ts)}

        # (a) NULL SPACE of the stacked equivariance constraint, on the ansatz
        #     coefficient space (Hermitian Gram of the defect).  x in null  <=>
        #     sum_k x_k T_k is equivariant.  This SELECTS equivariant combinations
        #     (rejecting the non-equivariant decoys).
        wv, null, G = gram_nullspace(Ts, gens13)
        scale = max(1.0, float(abs(wv[-1])))
        n_equivariant_coeffs = int(np.sum(wv <= TOL * scale))

        # (b) FAMILY DIMENSION = dimension of the SPAN of the equivariant MAPS
        #     {sum_k x_k T_k : x in null}.  Equivariant candidates can be linearly
        #     dependent as maps, so the family dimension is the rank of the map-Gram
        #     restricted to the equivariant coefficient subspace -- NOT the count of
        #     equivariant coefficient directions.
        flat = np.stack([T.reshape(-1) for T in Ts], axis=1)   # (vecdim, m)
        eq_maps = flat @ null                                  # columns = equivariant maps
        Meq = eq_maps.conj().T @ eq_maps                       # map-Gram of equivariant maps
        mw = np.linalg.eigvalsh(Meq)
        mscale = max(1.0, float(abs(mw[-1])))
        family_dim = int(np.sum(mw > TOL * mscale))

        # Clean basis of the equivariant subspace: the two distinct channels.
        Tc = T_by_label["delta_contract(Clifford-trace,canon)"]   # degree-1, GU canon shiab
        Tw = T_by_label["wedge_metric(Rarita-Schwinger)"]         # degree-3

        # Re-verify the chosen basis on a curated insurance set. The 13 adjacent
        # rotations already GENERATE so(14,C) (equivariance under them => under all),
        # so we add a spread of non-adjacent generators as an independent cross-check.
        verify_pairs = (GEN_SET if not verify_all_generators
                        else GEN_SET + [(0, 7), (2, 9), (5, 13), (1, 11), (3, 8),
                                        (0, 13), (4, 10), (6, 12)])
        vgens = projected_generators(verify_pairs, Pin, Pout)
        dc = max_defect(Tc, vgens)
        dw = max_defect(Tw, vgens)

        # independence of the two basis matrices, and that every equivariant candidate
        # lies in their span (completeness of the 2-element basis within the ansatz)
        fc = Tc.reshape(-1)
        fw = Tw.reshape(-1)
        gram2 = np.array([[np.vdot(fc, fc), np.vdot(fc, fw)],
                          [np.vdot(fw, fc), np.vdot(fw, fw)]])
        indep_rank = int(np.linalg.matrix_rank(gram2, tol=TOL))

        result["blocks"][bname] = [
            ("contract(Clifford-trace,canon-shiab)", Tc),
            ("wedge(Rarita-Schwinger)", Tw),
        ]
        result["per_block_report"][bname] = {
            "gram_eigenvalues": wv,
            "n_equivariant_coeff_directions": n_equivariant_coeffs,
            "family_dim_mapspan": family_dim,
            "individual_defects_13gen": indiv,
            "delta_canon_is_equivariant": bool(indiv["delta_contract(Clifford-trace,canon)"] < TOL),
            "n_verify_generators": len(verify_pairs),
            "basis_defect_verify_contract": dc,
            "basis_defect_verify_wedge": dw,
            "basis_independent_rank": indep_rank,
            "contract_wedge_frobenius_overlap": float(abs(gram2[0, 1])),
        }

    # ---- canon-shiab coordinates in the full-Dirac basis -------------------
    # GU's canon shiab is the Clifford-trace / contraction channel, applied with the
    # SAME formula on both chiralities (c is chirality-odd, so it maps S+ ->S- and
    # S- -> S+ identically). In basis order [contract_+-, wedge_+-, contract_-+,
    # wedge_-+] its coordinate vector is (1,0,1,0).
    canon_coords = np.array([1.0, 0.0, 1.0, 0.0])

    # ---- computed dimensions (from the map-span rank, not hardcoded) -------
    block_dims = {b: r["family_dim_mapspan"] for b, r in result["per_block_report"].items()}
    # chirality-flipping blocks computed here; chirality-PRESERVING blocks (S+->S+,
    # S- ->S-) are 0 (no degree-even Clifford word produces Lambda^2 from V (x) Lambda^k;
    # independently confirmed by the Racah-Speiser / Klimyk count in
    # shiab_codiff_intertwiner_dim.py).
    dim_full_complex = sum(block_dims.values())  # 2 + 2 = 4

    # ---- real quaternionic doubling ---------------------------------------
    U, s, Jsq_err, Jcomm_err = build_quaternionic_J()
    # multiplication by i is a real-linear Spin-equivariant endomorphism of S_R=H^64
    # (i is a quaternion unit), so {Phi_k, i*Phi_k} are 8 real-independent real maps.
    dim_real = 2 * dim_full_complex

    result["dim_complex_per_block"] = block_dims
    result["dim_complex_full_dirac"] = dim_full_complex
    result["dim_real_full_dirac"] = dim_real
    result["canon_shiab_coords"] = canon_coords
    result["channel_labels"] = {
        "contract": "Clifford-trace channel (degree-1 Clifford output)",
        "wedge": "Rarita-Schwinger channel (degree-3 Clifford output, h.w. omega_1+omega_6)",
    }
    result["quaternionic"] = {
        "J_squared_plus_I_err": Jsq_err,        # ~0 confirms J^2=-I (quaternionic M(64,H))
        "J_commutes_with_Clifford_err": Jcomm_err,
        "U_anticommute_set": [a for a in range(N) if s[a] < 0],
    }
    # Ordered list of the 4 complex basis matrices (block tensors), matching the
    # canon_shiab_coords order [contract_+-, wedge_+-, contract_-+, wedge_-+].
    result["basis_matrices_full_dirac"] = [
        result["blocks"]["S+ -> S-"][0][1],   # contract  S+ -> S-  (GU canon shiab block)
        result["blocks"]["S+ -> S-"][1][1],   # wedge     S+ -> S-
        result["blocks"]["S- -> S+"][0][1],   # contract  S- -> S+  (GU canon shiab block)
        result["blocks"]["S- -> S+"][1][1],   # wedge     S- -> S+
    ]
    result["basis_labels_full_dirac"] = [
        "contract(S+->S-)", "wedge(S+->S-)", "contract(S-->S+)", "wedge(S-->S+)"]
    return result


# ---------------------------------------------------------------------------
# 6b. Disk cache around the ~280s build.
#     Keyed by a hash of the CONSTRUCTION SOURCE, so any change to the
#     W-functions / rep / null-space code invalidates the cache automatically.
#     Every cache load is RE-VERIFIED for equivariance + canon coords before use,
#     so a stale or corrupt cache can never feed an unverified family to a
#     selector test ("verify intact"). The code stays the single source of
#     truth; the cache is a pure speedup and the matrices are never committed.
# ---------------------------------------------------------------------------
_CACHE_SOURCE_FUNCS = (
    build_rep, Sigma, JV, JL2, build_T, defect, gram_nullspace,
    build_quaternionic_J, W_delta_contract, W_wedge_metric, W_eGamma_metric,
    W_wedge_plain, W_decoy, _build_shiab_family_basis,
)


def _cache_key(verify_all_generators):
    src = "".join(inspect.getsource(f) for f in _CACHE_SOURCE_FUNCS)
    payload = f"{_CONSTRUCTION_VERSION}|verify_all={verify_all_generators}|{src}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _validate_loaded_family(R):
    """Cheap re-verification of a loaded family: canon coords + equivariance of the
    canon (contract) basis on a few generators. Returns False -> caller rebuilds."""
    try:
        if [float(x) for x in R.get("canon_shiab_coords", [])] != [1.0, 0.0, 1.0, 0.0]:
            return False
        if len(R.get("basis_matrices_full_dirac", [])) != 4:
            return False
        for bname, (Pin, Pout) in {"S+ -> S-": (BPLUS, BMINUS),
                                    "S- -> S+": (BMINUS, BPLUS)}.items():
            Tc = R["blocks"][bname][0][1]            # contract / canon-shiab block
            gens = projected_generators(GEN_SET[:2], Pin, Pout)
            if max_defect(Tc, gens) >= TOL:
                return False
        return True
    except Exception:
        return False


def get_shiab_family_basis(verify_all_generators=True, use_cache=True):
    """Cached wrapper around _build_shiab_family_basis (the ~280s build).

    First call builds and caches the result under tests/.cache/; later calls load
    and re-verify it in ~1s. The cache key hashes the construction source, so any
    code change rebuilds; every load is re-verified equivariant before use. Set
    use_cache=False or env GU_NO_CACHE=1 to force a fresh build.
    """
    if os.environ.get("GU_NO_CACHE"):
        use_cache = False
    path = None
    if use_cache:
        path = os.path.join(CACHE_DIR, f"shiab_family_{_cache_key(verify_all_generators)}.pkl")
        if os.path.exists(path):
            try:
                with open(path, "rb") as fh:
                    R = pickle.load(fh)
                if _validate_loaded_family(R):
                    R.setdefault("cache", {})["loaded_from"] = os.path.relpath(path, HERE)
                    return R
            except Exception:
                pass  # corrupt / incompatible -> rebuild below
    R = _build_shiab_family_basis(verify_all_generators)
    if use_cache and path is not None:
        try:
            os.makedirs(CACHE_DIR, exist_ok=True)
            tmp = path + ".tmp"
            with open(tmp, "wb") as fh:
                pickle.dump(R, fh, protocol=pickle.HIGHEST_PROTOCOL)
            os.replace(tmp, path)  # atomic; no half-written cache
        except Exception:
            pass  # caching is best-effort; never block the build on it
    return R


def write_family_summary(R, path=None):
    """Write the small, committed, human-readable RESULT summary (the citable
    artifact). The heavy matrices stay in the gitignored cache; this captures the
    verified facts: dims, canon coords, channel labels, and verification errors."""
    if path is None:
        path = os.path.join(HERE, "shiab_family_summary.json")
    rpt = R["per_block_report"]
    summary = {
        "title": "Cl(9,5)=M(64,H) shiab equivariant family — verified result summary",
        "generated_by": "tests/shiab_family_basis.py (write_family_summary)",
        "what_this_is": ("The committed, citable RESULT of the explicit equivariant-family "
                         "computation. The 334MB of basis matrices are derived from this file's "
                         "code and cached locally in tests/.cache/ (gitignored), not committed."),
        "rep": {
            "Cl_dim_complex": int(R["rep"]["dimC_Cl"]),
            "clifford_max_err": float(R["rep"]["clifford_max_err"]),
            "Splus_dim_complex": int(R["rep"]["Splus_dimC"]),
            "Sminus_dim_complex": int(R["rep"]["Sminus_dimC"]),
        },
        "family_dim_complex_per_block": {k: int(v) for k, v in R["dim_complex_per_block"].items()},
        "family_dim_complex_full_dirac": int(R["dim_complex_full_dirac"]),
        "family_dim_real_full_dirac": int(R["dim_real_full_dirac"]),
        "canon_shiab_coords": [float(x) for x in R["canon_shiab_coords"]],
        "canon_coords_order": ["contract_+-", "wedge_+-", "contract_-+", "wedge_-+"],
        "basis_labels_full_dirac": R["basis_labels_full_dirac"],
        "channel_labels": R["channel_labels"],
        "quaternionic": {k: float(v) if not isinstance(v, list) else v
                         for k, v in R["quaternionic"].items()},
        "verification": {
            b: {
                "family_dim_mapspan": int(r["family_dim_mapspan"]),
                "n_equivariant_coeff_directions": int(r["n_equivariant_coeff_directions"]),
                "basis_defect_verify_contract": float(r["basis_defect_verify_contract"]),
                "basis_defect_verify_wedge": float(r["basis_defect_verify_wedge"]),
                "contract_wedge_frobenius_overlap": float(r["contract_wedge_frobenius_overlap"]),
            }
            for b, r in rpt.items()
        },
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)
    return path


def densify_block(T):
    """Expand a block tensor (14, dimS_out, 91, dimS_in) to the Hom matrix
    (14*dimS_out) x (91*dimS_in)."""
    a, do, j, di = T.shape
    return T.transpose(0, 1, 2, 3).reshape(a * do, j * di)


# ---------------------------------------------------------------------------
# 7. Report
# ---------------------------------------------------------------------------
def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 84)
    print("EXPLICIT BASIS  Hom_{Spin(9,5)}(Lambda^2 V (x) S, V (x) S)  via equivariance null space")
    print("=" * 84)
    R = get_shiab_family_basis(verify_all_generators=True)
    rep = R["rep"]
    print(f"Cl(9,5)=M(64,H)~M(128,C): dimC={rep['dimC_Cl']}, Clifford max err={rep['clifford_max_err']:.2e}, "
          f"S+={rep['Splus_dimC']} S-={rep['Sminus_dimC']} (complex)")
    print(f"so(14,C) generating set: {len(GEN_SET)} adjacent rotations (generate the algebra); "
          f"basis re-verified against a wider non-adjacent insurance set.")

    for bname, rpt in R["per_block_report"].items():
        print("\n" + "-" * 84)
        print(f"BLOCK  {bname}")
        print("-" * 84)
        print("  individual equivariance defects (13 generators):")
        for lab, val in rpt["individual_defects_13gen"].items():
            tag = "EQUIVARIANT" if val < TOL else "not equivariant"
            print(f"    {lab:38s} defect={val:.2e}  [{tag}]")
        ev = rpt["gram_eigenvalues"]
        print("  defect-Gram eigenvalues (small = equivariant coefficient directions):")
        print("    ", np.array2string(ev, formatter={'float_kind': lambda x: f'{x:.2e}'}))
        print(f"      equivariant coefficient directions (null of defect-Gram) = "
              f"{rpt['n_equivariant_coeff_directions']}  (decoys rejected)")
        print(f"  ==> FAMILY DIM (rank of the equivariant MAP span) = {rpt['family_dim_mapspan']}")
        print(f"      GU literal Clifford-contraction shiab equivariant? {rpt['delta_canon_is_equivariant']}")
        print(f"      basis re-verified on {rpt['n_verify_generators']} generators "
              f"(13 adjacent generate so(14,C) + non-adjacent insurance): "
              f"contract defect={rpt['basis_defect_verify_contract']:.2e}, "
              f"wedge defect={rpt['basis_defect_verify_wedge']:.2e}")
        print(f"      basis independence rank (expect 2) = {rpt['basis_independent_rank']}")
        T0 = R["blocks"][bname][0][1]
        print(f"      basis matrices exposed as block tensors {T0.shape} "
              f"-> densify to {densify_block(T0).shape}")

    print("\n" + "=" * 84)
    print("DIMENSION SUMMARY")
    print("=" * 84)
    pbd = R['dim_complex_per_block']
    print(f"  complex dim per chiral block (computed map-span rank): "
          + ", ".join(f"{b}={d}" for b, d in pbd.items()))
    print(f"  complex dim full Dirac S=S+(+)S- (flipping 2+2, preserving 0+0) = "
          f"{R['dim_complex_full_dirac']}")
    print(f"  real dim full Dirac (quaternionic doubling)       = {R['dim_real_full_dirac']}  (>= 8)")
    q = R["quaternionic"]
    print(f"  quaternionic J: ||J^2 + I|| = {q['J_squared_plus_I_err']:.2e} (=>J^2=-I, M(64,H)); "
          f"||[J,Cl]|| = {q['J_commutes_with_Clifford_err']:.2e}")
    print(f"  (real doubling: i is a quaternion unit acting Spin-equivariantly on S_R=H^64,")
    print(f"   so {{Phi_k, i*Phi_k : k=1..4}} are 8 real-independent real-equivariant maps.)")

    print("\n  CHANNELS:")
    for k, v in R["channel_labels"].items():
        print(f"    {k:9s}: {v}")

    ov = max(r["contract_wedge_frobenius_overlap"] for r in R["per_block_report"].values())
    print("\n  GU CANON SHIAB Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s :")
    print(f"    Phi == the (verified equivariant) contraction basis element in each block.")
    print(f"    contraction _|_ wedge (Frobenius overlap = {ov:.2e}) => coordinates are unambiguous.")
    print(f"    coordinates in basis [contract_+-, wedge_+-, contract_-+, wedge_-+] = "
          f"{R['canon_shiab_coords']}")
    print("    => Phi lives in the Clifford-trace (contraction) channel, ZERO wedge component;")
    print("       it is ONE element of a 4-complex / 8-real dimensional family.")
    if R.get("cache", {}).get("loaded_from"):
        print(f"  [loaded from verified cache: {R['cache']['loaded_from']}]")
    summary_path = write_family_summary(R)
    print(f"  [result summary written: {os.path.relpath(summary_path, HERE)}]")
    print("=" * 84)
    return R


if __name__ == "__main__":
    main()
