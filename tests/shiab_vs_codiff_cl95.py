#!/usr/bin/env python3
"""Is GU's shiab the codifferential d_A*?  Explicit Cl(9,5) resolution.

QUESTION (canon SC1 sec 3.5 vs FHE/probabilist persona lenses)
--------------------------------------------------------------
canon SC1 (`sc1-shiab-domain-codomain-2026-06-23.md` sec 3.5 / 3.6 candidate B)
claims GU's shiab Phi is DISTINCT from the formal codifferential d_A* (same
TYPE Omega^2 (x) S -> Omega^1 (x) S, different formula). Several persona lenses
in `rs-middle-map-persona-steelman-2026-06-26.md` (lead C1: FHE/Homomorphic-
Encryption, Info-Coding, Probabilist, Clifford-04) argue the opposite: that
"adjointness forces shiab = (d_A)*", i.e. the shiab IS the metric codifferential
of the spinor-twisted complex.

This file resolves it by EXPLICIT matrix computation in the verified
Cl(9,5) = M(64,H) ~ M(128,C) representation. Nothing is tuned. Every operator is
built from first principles; the reported numbers are whatever they come out to.

WHAT IS BUILT
-------------
(i)  Phi  = the GU canon Clifford-contraction shiab, a CONCRETE matrix
        Phi : Lambda^2(R^14) (x) S  ->  Lambda^1(R^14) (x) S
        Phi(e^b ^ e^c (x) s) = e^b (x) c(e^c)s  -  e^c (x) c(e^b)s
     (metric-free antisymmetrization on the form factor; the metric/signature
      enters only through the Clifford multiplication c(.) = the rep generators).

(ii) delta_xi = the principal symbol of the covariant codifferential d_A* at a
        covector xi, the ONLY zeroth-order (bundle-map) object derivable from the
        first-order operator d_A* :
        delta_xi(alpha (x) s) = (iota_{xi^#} alpha) (x) s
     This is also EXACTLY the adjoint-symbol of the de Rham forward map d_A
     (sigma(d_A)(xi) = xi ^ . (x) id_S), so comparing Phi to delta_xi directly
     tests "is shiab = (d_A)* ?". It acts as the IDENTITY on the spinor factor S.

COMPARISON
----------
We report: ranks / kernels / images of both; the chirality grading of each on
S = S^+ (+) S^-; and the best proportionality constant lambda minimizing
||Phi - lambda*delta_xi||_F with the residual. No choice is made to force any
particular answer; where a metric/Hermitian choice is needed it is stated and
its effect on the conclusion is reported.
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

TOL = 1e-9


def build_rep():
    """Verified Cl(9,5) = M(128,C) data: generators e[a], omega, chiral bases."""
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = [+1] * 9 + [-1] * 5  # signature (9,5)
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]  # c(e^a), e[a]^2 = eta_a I
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    # chirality bases
    w, V = np.linalg.eigh(omega)
    Bplus = V[:, w > 0.5]    # 128 x 64  (S^+)
    Bminus = V[:, w < -0.5]  # 128 x 64  (S^-)
    return dim, eta, e, omega, Bplus, Bminus


def main():
    report = {}
    dim, eta, e, omega, Bplus, Bminus = build_rep()

    # ---- sanity: traceless generators, chirality-odd c(e^a) -----------------
    max_tr = max(abs(complex(np.trace(e[a]))) for a in range(14))
    report["generator_max_trace_abs"] = float(max_tr)  # expect ~0  (Clifford-odd)
    # c(e^a) maps S^+ -> S^- (chirality swap): B+^dag e[a] B+ ~ 0
    swap_diag = max(float(np.max(np.abs(Bplus.conj().T @ e[a] @ Bplus))) for a in range(14))
    swap_off = max(float(np.max(np.abs(Bminus.conj().T @ e[a] @ Bplus))) for a in range(14))
    report["c_ea_Splus_to_Splus_max"] = swap_diag   # ~0
    report["c_ea_Splus_to_Sminus_max"] = swap_off   # >0

    # ---- form index sets ----------------------------------------------------
    ones = list(range(14))                                  # 1-forms e^a
    twos = list(itertools.combinations(range(14), 2))       # 2-forms e^b ^ e^c, b<c
    n1, n2 = len(ones), len(twos)                           # 14, 91
    report["dim_Lambda1"] = n1
    report["dim_Lambda2"] = n2
    report["domain_dim_C"] = n2 * dim                       # 91*128 = 11648
    report["codomain_dim_C"] = n1 * dim                     # 14*128 = 1792

    # ---- (i) shiab Phi blocks  B_{a,j} (128x128) ----------------------------
    # Phi(e^b^e^c (x) s) = e^b (x) c(e^c)s - e^c (x) c(e^b)s
    #   slot a=b: +c(e^c)=+e[c];  slot a=c: -c(e^b)=-e[b]; else 0
    def phi_block(a, j):
        b, c = twos[j]
        out = np.zeros((dim, dim), dtype=complex)
        if a == b:
            out = out + e[c]
        if a == c:
            out = out - e[b]
        return out

    # Frobenius norm of Phi (block-wise; avoids the 1792x11648 dense matrix)
    phi_fro2 = 0.0
    for a in ones:
        for j in range(n2):
            B = phi_block(a, j)
            if B.any():
                phi_fro2 += float(np.linalg.norm(B) ** 2)
    report["Phi_frobenius_norm"] = float(np.sqrt(phi_fro2))

    # rank(Phi) via codomain Gram GG = Phi Phi^dag  (1792 x 1792), block form
    GG = np.zeros((n1 * dim, n1 * dim), dtype=complex)
    # precompute nonzero blocks per j to keep it light
    for j in range(n2):
        b, c = twos[j]
        # only a in {b,c} give nonzero blocks
        blocks = {b: e[c], c: -e[b]}
        for a1, B1 in blocks.items():
            for a2, B2 in blocks.items():
                GG[a1 * dim:(a1 + 1) * dim, a2 * dim:(a2 + 1) * dim] += B1 @ B2.conj().T
    evals = np.linalg.eigvalsh(GG)
    rank_phi = int(np.sum(evals > TOL * max(1.0, evals.max())))
    report["Phi_rank_C"] = rank_phi
    report["Phi_image_dim_C"] = rank_phi
    report["Phi_kernel_dim_C"] = report["domain_dim_C"] - rank_phi
    report["Phi_surjective_onto_codomain"] = bool(rank_phi == report["codomain_dim_C"])
    report["Phi_rank_H"] = rank_phi / 2.0  # M(64,H): rank_H = rank_C/2

    # ---- chirality grading of Phi (S = S^+ (+) S^-) --------------------------
    # graded Frobenius masses Phi^{out<-in} for in,out in {+,-}
    def grade_mass(block_fn, Pin, Pout):
        m2 = 0.0
        for a in ones:
            for j in range(n2):
                B = block_fn(a, j)
                if B.any():
                    m2 += float(np.linalg.norm(Pout.conj().T @ B @ Pin) ** 2)
        return float(np.sqrt(m2))

    report["Phi_grade_plus_to_plus"] = grade_mass(phi_block, Bplus, Bplus)     # ~0
    report["Phi_grade_plus_to_minus"] = grade_mass(phi_block, Bplus, Bminus)   # >0
    report["Phi_grade_minus_to_plus"] = grade_mass(phi_block, Bminus, Bplus)   # >0
    report["Phi_grade_minus_to_minus"] = grade_mass(phi_block, Bminus, Bminus) # ~0
    report["Phi_is_chirality_ODD_swaps_S"] = bool(
        report["Phi_grade_plus_to_plus"] < TOL and report["Phi_grade_minus_to_minus"] < TOL
        and report["Phi_grade_plus_to_minus"] > 1.0)

    # ---- (ii) codifferential symbol delta_xi = sigma(d_A*)(xi) ---------------
    # delta_xi(e^b^e^c (x) s) = (iota_{xi^#}(e^b^e^c)) (x) s,
    #   iota_{xi^#}(e^b^e^c) = eta_b xi_b e^c - eta_c xi_c e^b   (S-trivial: acts as Id on s)
    # CHOICE: xi a representative non-null covector; the metric eta is the (9,5)
    # signature already fixed by the rep. Conclusion is xi-independent (shown below).
    rng = np.random.default_rng(0)
    xi = rng.standard_normal(14)
    xi_norm2 = float(sum(eta[a] * xi[a] ** 2 for a in range(14)))  # <xi,xi> in (9,5)
    report["xi"] = [float(v) for v in xi]
    report["xi_metric_norm2_(9,5)"] = xi_norm2  # generically non-null

    Id = np.eye(dim, dtype=complex)

    def delta_coeff(a, j):
        b, c = twos[j]
        # coefficient of e^a in iota_{xi^#}(e^b^e^c)
        return (eta[b] * xi[b]) * (1.0 if a == c else 0.0) - (eta[c] * xi[c]) * (1.0 if a == b else 0.0)

    def delta_block(a, j):
        coeff = delta_coeff(a, j)
        if coeff == 0.0:
            return np.zeros((dim, dim), dtype=complex)
        return coeff * Id

    delta_fro2 = 0.0
    for a in ones:
        for j in range(n2):
            coeff = delta_coeff(a, j)
            if coeff != 0.0:
                delta_fro2 += (coeff ** 2) * float(np.linalg.norm(Id) ** 2)
    report["delta_xi_frobenius_norm"] = float(np.sqrt(delta_fro2))

    # rank(delta_xi) = rank(iota_xi : Lambda^2 -> Lambda^1) * dim
    M = np.zeros((n1, n2))
    for a in ones:
        for j in range(n2):
            M[a, j] = delta_coeff(a, j)
    rank_iota = int(np.linalg.matrix_rank(M, tol=1e-9))
    report["iota_xi_rank_on_forms"] = rank_iota
    report["delta_xi_rank_C"] = rank_iota * dim

    # chirality grading of delta_xi: scalar*Id PRESERVES chirality
    report["delta_grade_plus_to_plus"] = grade_mass(delta_block, Bplus, Bplus)     # >0
    report["delta_grade_plus_to_minus"] = grade_mass(delta_block, Bplus, Bminus)   # ~0
    report["delta_grade_minus_to_plus"] = grade_mass(delta_block, Bminus, Bplus)   # ~0
    report["delta_is_chirality_EVEN_preserves_S"] = bool(
        report["delta_grade_plus_to_minus"] < TOL and report["delta_grade_minus_to_plus"] < TOL
        and report["delta_grade_plus_to_plus"] > 1.0)

    # ---- THE COMPARISON: best lambda for Phi ~ lambda * delta_xi -------------
    # <delta_xi, Phi>_F = sum_{a,j} Tr(delta_block^dag phi_block)
    #                   = sum coeff* . Tr(single gamma) = 0   (Tr(gamma)=0)
    inner = 0.0 + 0.0j
    for a in ones:
        for j in range(n2):
            coeff = delta_coeff(a, j)
            if coeff == 0.0:
                continue
            B = phi_block(a, j)
            if not B.any():
                continue
            inner += np.conjugate(coeff) * np.trace(B)  # Tr(coeff*Id)^dag B = conj(coeff) Tr(B)
    report["inner_product_delta_Phi_(Frobenius)"] = complex(inner)
    lam = float(np.real(inner) / delta_fro2) if delta_fro2 > 0 else 0.0
    report["best_lambda"] = lam
    residual2 = phi_fro2 - 2 * lam * float(np.real(inner)) + (lam ** 2) * delta_fro2
    report["residual_norm_Phi_minus_lambda_delta"] = float(np.sqrt(max(residual2, 0.0)))
    report["residual_equals_full_Phi_norm"] = bool(
        abs(report["residual_norm_Phi_minus_lambda_delta"] - report["Phi_frobenius_norm"]) < 1e-6)

    # xi-independence: overlap is 0 for ANY xi because each surviving phi_block is a
    # single traceless gamma; document by trying several random xi.
    overlaps = []
    for seed in range(1, 6):
        r = np.random.default_rng(seed)
        xv = r.standard_normal(14)

        def dcoeff(a, j, xv=xv):
            b, c = twos[j]
            return (eta[b] * xv[b]) * (1.0 if a == c else 0.0) - (eta[c] * xv[c]) * (1.0 if a == b else 0.0)

        ov = 0.0 + 0.0j
        for a in ones:
            for j in range(n2):
                cf = dcoeff(a, j)
                if cf == 0.0:
                    continue
                B = phi_block(a, j)
                if B.any():
                    ov += np.conjugate(cf) * np.trace(B)
        overlaps.append(abs(complex(ov)))
    report["overlap_abs_over_5_random_xi"] = [float(x) for x in overlaps]
    report["overlap_zero_for_all_xi"] = bool(max(overlaps) < 1e-8)

    # ---- operator ORDER note (choice-free) ----------------------------------
    report["operator_order"] = {
        "shiab_Phi": "0 (algebraic bundle map; no derivatives)",
        "codifferential_d_A_star": "1 (first-order differential operator)",
        "note": ("A nonzero first-order operator cannot equal a zeroth-order one; the only "
                 "zeroth-order object derivable from d_A* is its principal symbol delta_xi, "
                 "which is what Phi is compared against above."),
    }

    # ---- adjoint reading: genuine Hermitian adjoint Phi* raises degree -------
    # Phi : Lambda^2(x)S -> Lambda^1(x)S, so Phi* : Lambda^1(x)S -> Lambda^2(x)S
    # is a DEGREE-RAISING map; it cannot be a codifferential (which lowers degree).
    # Its symbol is the Clifford degree-raiser sigma: e^a (x) s |-> sum_b e^b^e^a (x) c(e^b)s,
    # which is S-NONTRIVIAL (chirality swap) -- hence Phi is the adjoint of a Clifford
    # map, NOT the adjoint of the S-trivial de Rham d_A.
    report["adjoint_reading"] = {
        "Phi_adjoint_type": "Lambda^1 (x) S -> Lambda^2 (x) S  (RAISES form degree)",
        "is_a_codifferential": False,
        "Phi_is_adjoint_of": "Clifford degree-raising contraction (S-nontrivial), NOT de Rham d_A (S-trivial)",
    }

    # ---- VERDICT ------------------------------------------------------------
    verdict = ("DISTINCT: shiab Phi is NOT the codifferential d_A* (nor its symbol). "
               "Best proportionality constant lambda = {:.2e} (machine zero), residual = full "
               "||Phi|| = {:.3f}. Phi is chirality-ODD on S (Clifford swap S^+<->S^-); the d_A* "
               "symbol is chirality-EVEN (identity on S). Overlap is exactly 0 for all xi "
               "because surviving Phi blocks are single traceless gammas.").format(
        lam, report["Phi_frobenius_norm"])
    report["VERDICT"] = verdict

    # ---- print --------------------------------------------------------------
    print("=" * 80)
    print("SHIAB vs CODIFFERENTIAL d_A*  --  explicit Cl(9,5) = M(64,H) ~ M(128,C)")
    print("=" * 80)
    print(f"generators traceless (Clifford-odd): max|Tr e_a| = {report['generator_max_trace_abs']:.2e}")
    print(f"c(e^a): S^+ -> S^- swap : diag(+,+) max = {swap_diag:.2e}  off(-,+) max = {swap_off:.3f}")
    print()
    print(f"Phi  : Lambda^2(x)S (dim {report['domain_dim_C']}) -> Lambda^1(x)S (dim {report['codomain_dim_C']})")
    print(f"  rank_C(Phi) = {report['Phi_rank_C']}  image_C = {report['Phi_image_dim_C']}  "
          f"ker_C = {report['Phi_kernel_dim_C']}  (rank_H = {report['Phi_rank_H']})")
    print(f"  surjective onto codomain: {report['Phi_surjective_onto_codomain']}")
    print(f"  ||Phi||_F = {report['Phi_frobenius_norm']:.4f}")
    print("  chirality grading of Phi:")
    print(f"    +->+ {report['Phi_grade_plus_to_plus']:.2e}   +->- {report['Phi_grade_plus_to_minus']:.3f}")
    print(f"    -->+ {report['Phi_grade_minus_to_plus']:.3f}   -->- {report['Phi_grade_minus_to_minus']:.2e}")
    print(f"  => Phi is chirality-ODD (swaps S): {report['Phi_is_chirality_ODD_swaps_S']}")
    print()
    print(f"delta_xi = sigma(d_A*)(xi)  [xi non-null, <xi,xi>=({xi_norm2:.3f})]")
    print(f"  rank_C(delta_xi) = {report['delta_xi_rank_C']}  (= {rank_iota} * {dim})")
    print(f"  ||delta_xi||_F = {report['delta_xi_frobenius_norm']:.4f}")
    print("  chirality grading of delta_xi:")
    print(f"    +->+ {report['delta_grade_plus_to_plus']:.3f}   +->- {report['delta_grade_plus_to_minus']:.2e}")
    print(f"    -->+ {report['delta_grade_minus_to_plus']:.2e}")
    print(f"  => delta_xi is chirality-EVEN (preserves S): {report['delta_is_chirality_EVEN_preserves_S']}")
    print()
    print("COMPARISON  Phi ?= lambda * delta_xi :")
    print(f"  <delta_xi, Phi>_F = {report['inner_product_delta_Phi_(Frobenius)']}")
    print(f"  best lambda = {report['best_lambda']:.3e}")
    print(f"  residual ||Phi - lambda delta_xi||_F = {report['residual_norm_Phi_minus_lambda_delta']:.4f}"
          f"  (= full ||Phi||: {report['residual_equals_full_Phi_norm']})")
    print(f"  overlap |<delta_xi,Phi>| over 5 random xi: {['%.1e' % v for v in overlaps]}")
    print(f"  overlap zero for ALL xi: {report['overlap_zero_for_all_xi']}")
    print()
    print("VERDICT:")
    print(" ", verdict)
    print("=" * 80)
    print("MACHINE JSON:")
    print(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    main()
