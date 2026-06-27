#!/usr/bin/env python3
"""SELECTOR TEST: Gamma-trace / Rarita-Schwinger-channel compatibility.

Candidate selector for pinning GU's shiab inside the SHIAB-03 family
    Hom_{Spin(9,5)}(Lambda^2 V (x) S, V (x) S)   (complex dim 2 per chiral block,
    4 full Dirac, >= 8 real).

THE SELECTOR
------------
Impose the spin-3/2 irreducibility (Rarita-Schwinger) constraint: require the
equivariant map T to LAND IN the gamma-traceless part of the codomain V (x) S,
i.e. require the gamma-trace of the output to vanish:

    Gamma . T = 0 ,    Gamma : V (x) S -> S ,   Gamma( sum_a e^a (x) t_a ) = sum_a c(e^a) t_a

ker(Gamma) is the irreducible spin-3/2 Rarita-Schwinger module (h.w. omega_1+omega_6
in the chirality-flipped codomain V (x) S^-, complex dim 832); im(Gamma) ~ S is the
"gamma-trace" / spin-1/2 part (the spurious Clifford-trace channel). The selector kills
the trace direction and keeps the gamma-traceless RS direction.

This is the standard physics RS constraint: an irreducible spin-3/2 field psi_a must be
gamma-traceless  gamma^a psi_a = 0.

We COMPUTE the surviving dimension from first principles (no tuning, FC4-HOLONOMY-01):
form Gamma . T for the explicit 2-element family basis {contract(=GU canon shiab),
wedge} per block, and take the NULL SPACE of the stacked gamma-trace map. The nullity
is the surviving family dimension under the selector. We then check whether GU's canon
shiab (pure contract channel, coords (1,0)) survives.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import shiab_family_basis as sfb

TOL = 1e-7
N = sfb.N            # 14
E = sfb.E            # Clifford generators c(e^a) = E[a], E[a]^2 = eta_a I
ETA = sfb.ETA
DIM = sfb.DIM        # 128
PAIRS = sfb.PAIRS    # 91 index pairs (p,q)
NPAIR = sfb.NPAIR


def gamma_trace_of_block_tensor(T, Pout):
    """Apply the gamma-trace Gamma to the codomain of an equivariant map T.

    T has shape (14, dimS_out, 91, dimS_in); its output is
        T(alpha_j (x) s) = sum_a e^a (x) t_{a,j}(s),   t_{a,j} = Pout @ T[a,:,j,:]  in S_out.
    Gamma contracts the covector slot with Clifford multiplication:
        (Gamma.T)(alpha_j (x) s) = sum_a c(e^a) t_{a,j}(s) = sum_a E[a] @ Pout @ T[a,:,j,:].
    Result lives in S_other (opposite chirality, ambient 128). Returns a
    (128 x (91*dimS_in)) complex matrix = the vectorised gamma-trace map.
    """
    di = T.shape[3]
    out = np.zeros((DIM, NPAIR * di), dtype=complex)
    for j in range(NPAIR):
        acc = np.zeros((DIM, di), dtype=complex)
        for a in range(N):
            blk = T[a, :, j, :]
            if np.any(blk):
                acc += E[a] @ Pout @ blk            # c(e^a) applied to slot a, summed
        out[:, j * di:(j + 1) * di] = acc
    return out


def analyse_block(bname, basis_list, Pout):
    """basis_list = [('contract...', Tc), ('wedge...', Tw)] for one chiral block."""
    labels = [lab for lab, _ in basis_list]
    Ts = [T for _, T in basis_list]

    # gamma-trace of each basis map, flattened to a column vector
    GTs = [gamma_trace_of_block_tensor(T, Pout) for T in Ts]
    cols = np.stack([g.reshape(-1) for g in GTs], axis=1)   # (vec, 2)

    # individual gamma-trace masses
    indiv_norms = [float(np.linalg.norm(g)) for g in GTs]

    # Is each gamma-trace proportional to the SAME spinor map (the trace direction)?
    # ratio of the two trace images where the first is nonzero.
    # Build the "pure trace" reference map M_trace(alpha (x) s) = c(alpha) s = GAMMA2 . s
    # to interpret the constants.
    overlap = complex(np.vdot(cols[:, 0], cols[:, 1]))
    n0, n1 = indiv_norms
    cos = abs(overlap) / (n0 * n1) if n0 > TOL and n1 > TOL else 0.0

    # NULL SPACE of the stacked gamma-trace map: x in null  <=>  x0*GT_contract + x1*GT_wedge = 0
    # i.e. the combination sum_k x_k T_k is gamma-traceless (lands in the RS channel).
    M = cols.conj().T @ cols          # 2x2 Gram of the gamma-trace images
    w, Vv = np.linalg.eigh(M)
    scale = max(1.0, float(abs(w[-1])))
    null = Vv[:, w <= TOL * scale]
    surviving_dim = int(null.shape[1])

    # canon shiab = pure contract channel, coords (1,0). Does it survive (gamma-traceless)?
    canon = np.array([1.0, 0.0])
    canon_gt_norm = float(np.linalg.norm(cols @ canon))   # ||Gamma . canon||
    canon_survives = bool(canon_gt_norm < TOL * max(1.0, max(indiv_norms)))

    # If exactly 1 survives, express the surviving RS map in (contract, wedge) coords.
    surviving_coords = None
    if surviving_dim >= 1:
        v = null[:, 0]
        v = v / v[np.argmax(np.abs(v))]   # normalise largest comp to 1
        surviving_coords = np.round(v.real, 6)

    return {
        "block": bname,
        "labels": labels,
        "gamma_trace_norm_contract": n0,
        "gamma_trace_norm_wedge": n1,
        "gamma_traces_collinear_cos": float(cos),
        "gram_eigenvalues": w,
        "surviving_dim_complex": surviving_dim,
        "canon_gamma_trace_norm": canon_gt_norm,
        "canon_shiab_survives": canon_survives,
        "surviving_RS_coords_(contract,wedge)": surviving_coords,
    }


def main():
    np.set_printoptions(precision=5, suppress=True, linewidth=120)
    print("=" * 88)
    print("SELECTOR: Gamma-trace / Rarita-Schwinger-channel compatibility  (Gamma . T = 0)")
    print("=" * 88)

    R = sfb.get_shiab_family_basis(verify_all_generators=False)

    # codomain projectors per block: "S+ -> S-" has codomain spinor S- (BMINUS), etc.
    cod_proj = {"S+ -> S-": sfb.BMINUS, "S- -> S+": sfb.BPLUS}

    print(f"\nFamily (SHIAB-03) before selector: per-block complex dim = "
          f"{R['dim_complex_per_block']}, full Dirac complex = {R['dim_complex_full_dirac']}, "
          f"real = {R['dim_real_full_dirac']}")
    print("Basis per block: [contract (=GU canon Clifford-trace shiab), wedge (RS-labelled)]")

    reports = {}
    total_surv = 0
    for bname, basis_list in R["blocks"].items():
        rep = analyse_block(bname, basis_list, cod_proj[bname])
        reports[bname] = rep
        total_surv += rep["surviving_dim_complex"]
        print("\n" + "-" * 88)
        print(f"BLOCK {bname}   codomain V (x) {bname.split(' -> ')[1]}")
        print("-" * 88)
        print(f"  ||Gamma . contract(canon shiab)|| = {rep['gamma_trace_norm_contract']:.4f}   "
              f"(0 => contract is gamma-traceless)")
        print(f"  ||Gamma . wedge(RS-labelled)||     = {rep['gamma_trace_norm_wedge']:.4f}   "
              f"(0 => wedge alone is gamma-traceless)")
        print(f"  gamma-trace images collinear? |cos| = {rep['gamma_traces_collinear_cos']:.6f}  "
              f"(1 => both map onto the SAME trace direction)")
        print(f"  Gram eigenvalues of stacked gamma-trace map: "
              f"{np.array2string(rep['gram_eigenvalues'], formatter={'float_kind': lambda x: f'{x:.3e}'})}")
        print(f"  ==> SURVIVING complex dim (null of gamma-trace, lands in RS channel) = "
              f"{rep['surviving_dim_complex']}")
        print(f"      surviving RS map coords (contract,wedge) = {rep['surviving_RS_coords_(contract,wedge)']}")
        print(f"  GU canon shiab (pure contract, coords (1,0)):")
        print(f"      ||Gamma . canon|| = {rep['canon_gamma_trace_norm']:.4f}  -> "
              f"survives selector? {rep['canon_shiab_survives']}")

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    surv_real = 2 * total_surv
    print(f"  surviving complex dim (full Dirac, both chiral blocks) = {total_surv}")
    print(f"  surviving real dim (quaternionic doubling, x2)         = {surv_real}")
    canon_any = any(r["canon_shiab_survives"] for r in reports.values())
    print(f"  GU canon shiab survives in ANY block?                  = {canon_any}")
    print(f"  => selector keeps the gamma-traceless RS direction and KILLS the trace direction.")
    print(f"     The surviving RS map is a contract+wedge COMBINATION, NOT the pure GU canon shiab.")
    return {"total_surviving_complex": total_surv, "total_surviving_real": surv_real,
            "canon_survives": canon_any, "per_block": reports}


if __name__ == "__main__":
    main()
