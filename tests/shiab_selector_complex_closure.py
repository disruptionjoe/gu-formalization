#!/usr/bin/env python3
"""SELECTOR TEST: complex closure / d^2=0 on the natural Spin(9,5) shiab family.

CONTEXT (SHIAB-03)
------------------
The family Hom_{Spin(9,5)}(Lambda^2 V (x) S, V (x) S) is NOT 1-dimensional:
  - complex dim = 2 per chiral block (Clifford-trace channel + Rarita-Schwinger
    channel), 4 for full Dirac, real dim >= 8 (quaternionic doubling).
GU's canon shiab Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s is ONE
element of this family: the Clifford-trace (contraction) channel, coords (1,0,1,0)
in the order [contract_+-, wedge_+-, contract_-+, wedge_-+].

THE SELECTOR UNDER TEST
-----------------------
"Complex closure / d^2=0": fold the family element T (a degree-LOWERING map
Lambda^2 (x) S -> Lambda^1 (x) S) with the connection / de Rham differential d_A
(degree-RAISING) into a single super-operator and demand it square to zero:

        D = d_A + T            on   (Lambda^1 (x) S)  (+)  (Lambda^2 (x) S)
        D^2 = 0  (the "complex closure" / d^2=0 analog)

D^2 = d_A^2 + {d_A, T} + T^2.  The PRINCIPAL-SYMBOL piece of the cross term
{d_A, T} is, at a covector xi (sigma(d_A)(xi) = e(xi) = xi ^ . (x) id_S):

        on Lambda^1 (x) S :   T . e(xi)        (Lambda^1 -> Lambda^2 -> Lambda^1)
        on Lambda^2 (x) S :   e(xi) . T        (Lambda^2 -> Lambda^1 -> Lambda^2)

These must vanish for ALL xi for D to be a genuine differential (D^2 = 0). This is
the well-typed NECESSARY closure condition that lives entirely inside the family
(it uses only the family map T and the canonical symbol e(xi) of d_A; it needs no
ad hoc extension of T to other form degrees -- indeed T^2 is not even well typed,
since T is only defined Lambda^2 -> Lambda^1, which is itself a sign that "complex
closure" is not native to the family).

Because e(xi) is linear in xi, vanishing for the 14 coordinate covectors xi = e^c
is EQUIVALENT to vanishing for all xi -- so the test is exact and complete.

The closure obstruction is LINEAR in the family coordinates k = (k0,k1,k2,k3), so
the surviving subspace is the NULL SPACE of the 4x4 Hermitian Gram matrix

        M_ij = sum_xi [ <T_i e(xi), T_j e(xi)>_F + <e(xi) T_i, e(xi) T_j>_F ]

dim null(M) = surviving COMPLEX dimension of the family after imposing closure.
Real surviving dim = 2 * complex (quaternionic doubling; the obstruction is
quaternionic-linear so the i-multiples survive iff the complex maps do).

DISCIPLINE (FC4-HOLONOMY-01): nothing is tuned. M is computed from first
principles; the surviving dimension is reported as whatever null(M) comes out to.
"""

from __future__ import annotations

import itertools
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) anchor

TOL = 1e-7
N = 14


# ---------------------------------------------------------------------------
# Verified Cl(9,5) = M(64,H) ~ M(128,C) representation.
# ---------------------------------------------------------------------------
def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
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
    Pplus = 0.5 * (Iden + omega)
    Pminus = 0.5 * (Iden - omega)
    return dim, eta, e, omega, Pplus, Pminus, cliff_err


DIM, ETA, E, OMEGA, PPLUS, PMINUS, CLIFF_ERR = build_rep()
ZERO = np.zeros((DIM, DIM), dtype=complex)


# ---------------------------------------------------------------------------
# The two natural-map channels as 128x128 Clifford operators W(a,u,v):
#   T(e^u ^ e^v (x) s) = sum_a e^a (x) W(a,u,v) s
# Both antisymmetric in (u,v); valid for any u != v.
# ---------------------------------------------------------------------------
def W_contract(a, u, v):
    """Clifford-trace / canon contraction channel (GU canon shiab).
    W = delta_{a,u} c(e^v) - delta_{a,v} c(e^u).  Nonzero only for a in {u,v}."""
    out = ZERO
    if a == u:
        out = out + E[v]
    if a == v:
        out = out - E[u]
    return out


def W_wedge(a, u, v):
    """Rarita-Schwinger channel: eta_aa * (1/2){c(e_a), c(e^u^e^v)} = degree-3
    Clifford word eta_aa c(e_a^e^u^e^v).  Nonzero only for a not in {u,v}."""
    G2 = E[u] @ E[v]
    return ETA[a] * 0.5 * (E[a] @ G2 + G2 @ E[a])


def chiral(W, Pout, Pin):
    """Project a 128x128 channel operator to the Pin -> Pout chiral block."""
    return Pout @ W @ Pin


# The 4 complex basis maps of the full-Dirac family, in canon order
#   [contract_+-, wedge_+-, contract_-+, wedge_-+].
# basis map i is encoded by (channel_fn, Pout, Pin).
BASIS = [
    ("contract(S+->S-)", W_contract, PMINUS, PPLUS),
    ("wedge(S+->S-)", W_wedge, PMINUS, PPLUS),
    ("contract(S-->S+)", W_contract, PPLUS, PMINUS),
    ("wedge(S-->S+)", W_wedge, PPLUS, PMINUS),
]
NB = len(BASIS)  # 4

# canon shiab = contraction channel on BOTH chiralities, zero wedge -> (1,0,1,0)
CANON_COORDS = np.array([1.0, 0.0, 1.0, 0.0], dtype=complex)


from functools import lru_cache


@lru_cache(maxsize=None)
def basis_block(i, a, u, v):
    """128x128 operator of basis map i for output 1-form a, input 2-form (u,v).
    Cached: independent of the covector xi, so build each block once."""
    _, fn, Pout, Pin = BASIS[i]
    W = fn(a, u, v)
    if not W.any():
        return None
    return chiral(W, Pout, Pin)


# 2-forms (ordered) and helpers --------------------------------------------
TWOFORMS = list(itertools.combinations(range(N), 2))  # 91 ordered (p<q)
TWOIDX = {pq: k for k, pq in enumerate(TWOFORMS)}


def ordered_2form(u, v):
    """Return (idx, sign) for the ordered 2-form basis element of e^u ^ e^v,
    or (None, 0) if u == v."""
    if u == v:
        return None, 0
    if u < v:
        return TWOIDX[(u, v)], +1.0
    return TWOIDX[(v, u)], -1.0


# ---------------------------------------------------------------------------
# Obstruction operators for one basis map i at one covector xi = e^{c0}.
#   e(xi): e^b -> e^{c0} ^ e^b   (degree raiser, identity on S)
#
#   O1_i = e(xi) . T_i   : Lambda^2 (x) S -> Lambda^2 (x) S
#     T_i(e^p^e^q (x) s) = sum_a e^a (x) B_i(a,p,q) s ;  then wedge e^a by e^{c0}.
#     stored as dict (j_in, k_out 2form) -> 128x128.
#
#   O2_i = T_i . e(xi)   : Lambda^1 (x) S -> Lambda^1 (x) S
#     e(xi)(e^b (x) s) = e^{c0}^e^b (x) s ; then apply T_i.
#     stored as dict (b_in 1form, a_out 1form) -> 128x128.
# ---------------------------------------------------------------------------
def obstruction_O1(i, c0):
    """e(xi=e^{c0}) . T_i  as dict {(jin, kout): 128x128}."""
    out = {}
    for (p, q) in TWOFORMS:
        jin = TWOIDX[(p, q)]
        # which output slots a are nonzero for this channel?
        a_list = (p, q) if BASIS[i][1] is W_contract else [a for a in range(N) if a not in (p, q)]
        for a in a_list:
            B = basis_block(i, a, p, q)
            if B is None:
                continue
            kout, sg = ordered_2form(c0, a)  # e^{c0} ^ e^a
            if kout is None:
                continue
            key = (jin, kout)
            out[key] = out.get(key, ZERO) + sg * B
    return out


def obstruction_O2(i, c0):
    """T_i . e(xi=e^{c0})  as dict {(bin, aout): 128x128}."""
    out = {}
    for b in range(N):
        # e(xi)(e^b) = e^{c0} ^ e^b  -> ordered 2-form (u,v) with sign
        jidx, sg0 = ordered_2form(c0, b)
        if jidx is None:
            continue
        (u, v) = TWOFORMS[jidx]
        a_list = (u, v) if BASIS[i][1] is W_contract else [a for a in range(N) if a not in (u, v)]
        for a in a_list:
            B = basis_block(i, a, u, v)
            if B is None:
                continue
            key = (b, a)
            out[key] = out.get(key, ZERO) + sg0 * B
    return out


def dict_inner(Da, Db):
    """Frobenius inner product <Da, Db>_F = sum_key Tr(Da[key]^dag Db[key])."""
    s = 0.0 + 0.0j
    for key, A in Da.items():
        B = Db.get(key)
        if B is not None:
            s += np.vdot(A, B)  # vdot conjugates first arg = Frobenius inner product
    return s


def dict_norm2(Da):
    s = 0.0
    for A in Da.values():
        s += float(np.linalg.norm(A) ** 2)
    return s


# ---------------------------------------------------------------------------
# Build the 4x4 Hermitian closure-Gram M and report.
# ---------------------------------------------------------------------------
def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 84)
    print("SELECTOR: complex closure / d^2=0  on the Spin(9,5) shiab family")
    print("=" * 84)
    print(f"Cl(9,5)=M(64,H)~M(128,C): dimC={DIM}, Clifford max err={CLIFF_ERR:.2e}")
    print(f"family basis (complex dim 4): {[b[0] for b in BASIS]}")
    print("closure tested via the folded super-operator D = d_A + T, D^2=0;")
    print("principal-symbol cross term {d_A,T} must vanish for ALL xi (14 coord covectors).")

    M = np.zeros((NB, NB), dtype=complex)
    # per-channel individual obstruction masses (summed over xi)
    indiv_O1 = np.zeros(NB)
    indiv_O2 = np.zeros(NB)

    for c0 in range(N):  # xi = e^{c0}; spanning the whole cotangent space
        O1 = [obstruction_O1(i, c0) for i in range(NB)]
        O2 = [obstruction_O2(i, c0) for i in range(NB)]
        for i in range(NB):
            indiv_O1[i] += dict_norm2(O1[i])
            indiv_O2[i] += dict_norm2(O2[i])
        for i in range(NB):
            for j in range(NB):
                M[i, j] += dict_inner(O1[i], O1[j]) + dict_inner(O2[i], O2[j])

    # Hermitian eigen-decomposition: null space = surviving (closing) subspace.
    M = 0.5 * (M + M.conj().T)
    evals, evecs = np.linalg.eigh(M)
    scale = max(1.0, float(abs(evals[-1])))
    surviving_mask = evals <= TOL * scale
    surviving_dim_complex = int(np.sum(surviving_mask))
    surviving_dim_real = 2 * surviving_dim_complex  # quaternionic doubling

    # closure obstruction of GU's canon shiab (coords (1,0,1,0))
    canon_obstruction2 = float(np.real(CANON_COORDS.conj() @ M @ CANON_COORDS))
    canon_closes = canon_obstruction2 <= TOL * scale * float(np.real(CANON_COORDS.conj() @ CANON_COORDS))

    print("\n" + "-" * 84)
    print("INDIVIDUAL CHANNEL CLOSURE OBSTRUCTIONS (summed over 14 xi)")
    print("-" * 84)
    for i in range(NB):
        tot = np.sqrt(indiv_O1[i] + indiv_O2[i])
        tag = "CLOSES" if tot < TOL else "does NOT close"
        print(f"  {BASIS[i][0]:18s}  ||e.T||={np.sqrt(indiv_O1[i]):.4f}  "
              f"||T.e||={np.sqrt(indiv_O2[i]):.4f}  total={tot:.4f}  [{tag}]")

    print("\n" + "-" * 84)
    print("CLOSURE-GRAM M (4x4 Hermitian); eigenvalues = squared closure obstruction")
    print("-" * 84)
    print("  eigenvalues:", np.array2string(evals, formatter={'float_kind': lambda x: f'{x:.4e}'}))
    print(f"  null(M) dimension (maps that CLOSE, complex) = {surviving_dim_complex}")
    print(f"  ==> SURVIVING COMPLEX DIM = {surviving_dim_complex}")
    print(f"  ==> SURVIVING REAL DIM (quaternionic x2)     = {surviving_dim_real}")

    print("\n" + "-" * 84)
    print("GU CANON SHIAB (contraction channel, coords (1,0,1,0))")
    print("-" * 84)
    print(f"  closure obstruction ||{{d_A,canon}}_symbol||^2 = {canon_obstruction2:.6f}")
    print(f"  canon shiab CLOSES (in surviving subspace)?  {bool(canon_closes)}")

    # If anything survives, show a surviving coordinate vector.
    surviving_vectors = []
    if surviving_dim_complex > 0:
        for idx in np.where(surviving_mask)[0]:
            surviving_vectors.append(evecs[:, idx])
        print("\n  surviving (closing) coordinate directions (columns):")
        for v in surviving_vectors:
            print("   ", np.array2string(v, formatter={'complex_kind': lambda z: f'{z.real:+.3f}{z.imag:+.3f}j'}))

    report = {
        "selector": "complex closure / d^2=0 (folded D=d_A+T, principal-symbol cross term {d_A,T}=0 for all xi)",
        "family_basis": [b[0] for b in BASIS],
        "family_dim_complex_before": NB,
        "family_dim_real_before": 2 * NB,
        "closure_gram_eigenvalues": [float(x) for x in evals],
        "surviving_dim_complex": surviving_dim_complex,
        "surviving_dim_real": surviving_dim_real,
        "individual_channel_obstruction_norm": {
            BASIS[i][0]: float(np.sqrt(indiv_O1[i] + indiv_O2[i])) for i in range(NB)
        },
        "canon_shiab_coords": [float(x.real) for x in CANON_COORDS],
        "canon_shiab_closure_obstruction2": canon_obstruction2,
        "canon_shiab_closes": bool(canon_closes),
        "clifford_max_err": float(CLIFF_ERR),
        "note": ("e(xi) linear in xi so 14 coordinate covectors = all xi (exact). "
                 "This is the NECESSARY principal-symbol closure condition; T^2 is not even "
                 "well typed (T only defined Lambda^2->Lambda^1), so strict D^2=0 is no weaker."),
    }
    print("\n" + "=" * 84)
    print("MACHINE JSON")
    print("=" * 84)
    print(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    main()
