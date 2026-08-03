#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anchor-council Wave A-1, item Q2 — chirality grading of the imposter 128
under BOTH real forms ((9,5) and (7,7)) and ALL five sign allocations of the
4+10 split.

PREREGISTERED (before this script was written) in
explorations/chirality-grading-and-77-rerun-2026-08-03.md §1.1:
  P-Q2-1: imposter block omega-grading 64+64 (balanced), both forms, all
          allocations  =>  kinematically vectorlike Reading-A block.
  P-Q2-2: full 1664 block structure grades 192+192 / 576+576 / 64+64,
          summing to the banked (832, 832).
  P-Q2-3: joint (omega_4, omega_10) grading of the source module S = C^128 is
          32/32/32/32 (each internal chirality pairs with both base-side
          chiralities equally).

CONSTRUCTION (Layer-0 typed in the exploration): ambient vector-spinor space
C^14 (x) C^128 on the explicit Jordan-Wigner Clifford fixtures
(tests/oq_rk1_cl95_explicit_rep.py); Gamma = sum_a e_a x_a; record sector
ker Gamma (dim 1664); metric-dual embeddings iota_B(psi)_a = eta_aa e_a psi
(a in B), likewise iota_F, so Gamma o iota_B = 4 I and Gamma o iota_F = 10 I
allocation-invariantly; imposter block = image of (10 iota_B - 4 iota_F), the
(10,-4) relative gamma-trace antidiagonal (hinge panel mechanism). Grading
operator = the AMBIENT 14D volume word omega = e_0..e_13 (restricted; it is
the unique constraint-preserving generator, trichotomy probe census). This is
NOT 4D Weyl chirality; the vectorlike bridge runs through the joint
(omega_4, omega_10) grading of S and the identification psi |-> x_psi, both
computed below.

FENCES (verbatim discipline):
  (1) kinematic carrier only — Pi_RS^phys does not exist (OQ-RK1
      BLOCKED_NEEDS_SPEC); nothing here is a statement about the physical
      carrier;
  (2) multiplicity is not count (Rung 1): 384/1152/128 are multiplicities,
      blocks are not generations;
  (3) reading A of the "imposter" homonym only (the 128 S(V)(x)S(W)); reading
      B (the RS spin-3/2 384) is untouched; Q1 adjudicates, not this script;
  (4) no verdict, bar(b), H59, or claim-status change: results are
      pre-deposit. PH-K1-KINEMATIC may be confirmed; PH-K1-PHYSICAL remains
      open on the unresolved referent and physical reduction.

Run:
  PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
      tests/generation-sector/q2_imposter_chirality_grading.py
Every check is a hard assert; the script exits nonzero on any failure.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.dont_write_bytecode = True

_HERE = os.path.dirname(os.path.abspath(__file__))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
for _p in (_TESTS, _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402  (verified JW gammas)
import gen_sector_bridge as gu_bridge    # noqa: E402  (fixture lineage: XI)

N, DIM = 14, 128
NV = (N - 1) * DIM            # 1664
XI = gu_bridge.XI             # the fixtures' Dirac coefficient vector
TOL = 1e-9

_n_checks = [0]


def check(name: str, cond: bool, detail: str = ""):
    _n_checks[0] += 1
    tag = "ok " if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""), flush=True)
    assert cond, f"CHECK FAILED: {name}  {detail}"


def fnorm(X) -> float:
    return float(np.linalg.norm(X))


def build_form(eta):
    """Explicit Clifford gammas for the given +/-1 signature list."""
    G = cl95.jordan_wigner_gammas(7)
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]


def word(e, idxs):
    out = np.eye(DIM, dtype=complex)
    for a in idxs:
        out = out @ e[a]
    return out


def normalize_involution(w):
    """Return (w', c_used) with w' proportional to w and w'^2 = +I."""
    sq = w @ w
    c = complex(np.trace(sq)) / DIM
    assert abs(abs(c) - 1.0) < 1e-9, f"word square not unimodular scalar: {c}"
    assert fnorm(sq - c * np.eye(DIM)) < 1e-7, "word square not scalar"
    if abs(c - 1.0) < 1e-6:
        return w, 1.0
    if abs(c + 1.0) < 1e-6:
        return 1j * w, 1j
    raise AssertionError(f"word square is {c}, expected +/-1")


def apply_W(e_omega, Y):
    """(I_14 (x) omega) Y for Y with 14*128 rows, applied blockwise."""
    ncol = Y.shape[1]
    Z = Y.reshape(N, DIM, ncol)
    out = np.einsum("ij,ajk->aik", e_omega, Z)
    return out.reshape(N * DIM, ncol)


def grading(Q, e_omega, label):
    """Grading of the omega-invariant block spanned by orthonormal Q."""
    WQ = apply_W(e_omega, Q)
    P = Q.conj().T @ WQ
    inv_res = fnorm(WQ - Q @ P) / (1.0 + fnorm(WQ))
    check(f"{label}: block is (I x omega)-invariant", inv_res < 1e-8,
          f"rel residual {inv_res:.2e}")
    check(f"{label}: restricted omega squares to +I",
          fnorm(P @ P - np.eye(P.shape[0])) < 1e-7)
    tr = float(np.trace(P).real)
    d = P.shape[1]
    n_plus = (d + tr) / 2.0
    n_minus = (d - tr) / 2.0
    check(f"{label}: grading dims are integers",
          abs(n_plus - round(n_plus)) < 1e-6 and abs(n_minus - round(n_minus)) < 1e-6,
          f"({n_plus:.4f}, {n_minus:.4f})")
    return int(round(n_plus)), int(round(n_minus))


def run_form(form_name, eta):
    print(f"\n{'=' * 78}\nREAL FORM {form_name}: eta = {eta}\n{'=' * 78}", flush=True)
    t0 = time.time()
    e = build_form(eta)
    Iden = np.eye(DIM, dtype=complex)

    # Clifford relations
    cerr = max(
        float(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                            - (2.0 * eta[a] if a == b else 0.0) * Iden)))
        for a in range(N) for b in range(N))
    check(f"{form_name}: Clifford relations {{e_a,e_b}} = 2 eta_ab", cerr < TOL,
          f"max err {cerr:.2e}")

    # volume word
    omega = word(e, tuple(range(N)))
    check(f"{form_name}: omega^2 = +I", fnorm(omega @ omega - Iden) < 1e-7)
    ac = max(fnorm(omega @ e[a] + e[a] @ omega) for a in range(N))
    check(f"{form_name}: omega anticommutes with every e_a", ac < 1e-7,
          f"max {ac:.2e}")
    check(f"{form_name}: tr omega = 0 (S grades 64+64)",
          abs(complex(np.trace(omega))) < 1e-6)

    # constraint objects + anchors (signature-identical by construction)
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) \
        - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    M_D = np.kron(np.eye(N, dtype=complex), sum(XI[a] * e[a] for a in range(N)))
    bare = fnorm(Pi @ M_D - M_D @ Pi)
    c2 = fnorm(Gamma @ M_D @ Pi)
    check(f"{form_name}: anchor bare ||[Pi_RS, M_D]|| = 58.7215",
          abs(bare - 58.7215) < 1e-2, f"{bare:.4f}")
    check(f"{form_name}: anchor C2 = 155.3625", abs(c2 - 155.3625) < 1e-2, f"{c2:.4f}")
    dimker = int(round(float(np.trace(Pi).real)))
    check(f"{form_name}: dim ker Gamma = 1664 = 13*128", dimker == NV, str(dimker))

    # total grading of ker Gamma: tr((I x omega) Pi) blockwise
    tr_tot = sum(complex(np.trace(omega @ Pi[a * DIM:(a + 1) * DIM,
                                              a * DIM:(a + 1) * DIM]))
                 for a in range(N))
    check(f"{form_name}: ker Gamma grades 832 + 832 (tr omega_V = 0)",
          abs(tr_tot) < 1e-5, f"tr = {tr_tot:.2e}")

    # the five sign allocations of the 4+10 split
    plus_idx = [a for a in range(N) if eta[a] > 0]
    minus_idx = [a for a in range(N) if eta[a] < 0]
    allocations = []
    for k in range(4, -1, -1):
        if k <= len(plus_idx) and 4 - k <= len(minus_idx):
            allocations.append((k, sorted(plus_idx[:k] + minus_idx[:4 - k])))
    check(f"{form_name}: five allocations available", len(allocations) == 5,
          str([(k, b) for k, b in allocations]))

    imp_gradings, blk_reports = [], []
    for k, B in allocations:
        F = [a for a in range(N) if a not in B]
        tag = f"{form_name} alloc base({k}+,{4 - k}-) B={B}"
        print(f"-- {tag} --", flush=True)

        # metric-dual embeddings
        IB = np.zeros((N * DIM, DIM), dtype=complex)
        IF = np.zeros((N * DIM, DIM), dtype=complex)
        for a in B:
            IB[a * DIM:(a + 1) * DIM] = eta[a] * e[a]
        for a in F:
            IF[a * DIM:(a + 1) * DIM] = eta[a] * e[a]
        check(f"{tag}: Gamma o iota_B = 4 I (allocation-invariant)",
              fnorm(Gamma @ IB - 4.0 * Iden) < 1e-8)
        check(f"{tag}: Gamma o iota_F = 10 I (allocation-invariant)",
              fnorm(Gamma @ IF - 10.0 * Iden) < 1e-8)

        # imposter block: the (10, -4) antidiagonal
        X = 10.0 * IB - 4.0 * IF
        check(f"{tag}: imposter block lies in ker Gamma",
              fnorm(Gamma @ X) < 1e-7 * fnorm(X))
        gram = X.conj().T @ X
        check(f"{tag}: X^dag X = 560 I (dim_C imposter = 128, exact frame)",
              fnorm(gram - 560.0 * Iden) < 1e-6)
        QI = X / np.sqrt(560.0)

        # mechanism identity: (I x omega) x_psi = - x_{omega psi}
        mech = fnorm(apply_W(omega, X) + X @ omega) / (1.0 + fnorm(X))
        check(f"{tag}: (I x omega) o iota = - iota o omega (grading mirror)",
              mech < 1e-8, f"rel residual {mech:.2e}")

        gI = grading(QI, omega, f"{tag}: imposter 128")
        imp_gradings.append(gI)
        print(f"  imposter grading under omega: {gI[0]} + {gI[1]}", flush=True)

        # native blocks: ker Gamma_B on V4 (x) S and ker Gamma_F on V10 (x) S
        def native_block(idxs, expect_dim, nm):
            GamX = np.hstack([e[a] for a in idxs])
            _, s_, vh = np.linalg.svd(GamX)
            check(f"{tag}: Gamma_{nm} surjective onto S", s_[-1] > 1e-6,
                  f"s_min = {s_[-1]:.3e}")
            kerX = vh[DIM:].conj().T
            check(f"{tag}: dim ker Gamma_{nm} = {expect_dim}",
                  kerX.shape[1] == expect_dim, str(kerX.shape))
            Q = np.zeros((N * DIM, expect_dim), dtype=complex)
            for i, a in enumerate(idxs):
                Q[a * DIM:(a + 1) * DIM] = kerX[i * DIM:(i + 1) * DIM]
            check(f"{tag}: block {nm} lies in ker Gamma",
                  fnorm(Gamma @ Q) < 1e-7 * max(fnorm(Gamma), 1.0))
            check(f"{tag}: block {nm} orthonormal",
                  fnorm(Q.conj().T @ Q - np.eye(expect_dim)) < 1e-8)
            return Q

        QB = native_block(B, 384, "B")
        QF = native_block(F, 1152, "F")
        gB = grading(QB, omega, f"{tag}: native 384")
        gF = grading(QF, omega, f"{tag}: native 1152")
        print(f"  native-B grading: {gB[0]} + {gB[1]};  native-F grading: "
              f"{gF[0]} + {gF[1]}", flush=True)

        # direct sum: QB _|_ QF by support; imposter independent of both
        check(f"{tag}: QB _|_ QF (disjoint supports)",
              fnorm(QB.conj().T @ QF) < 1e-10)
        Mcross = np.vstack([QB.conj().T @ QI, QF.conj().T @ QI])
        smax = float(np.linalg.svd(Mcross, compute_uv=False)[0])
        check(f"{tag}: 384 (+) 1152 (+) 128 is a DIRECT sum filling ker Gamma "
              f"(max principal cosine < 1)", smax < 0.999, f"sigma_max = {smax:.6f}")
        tot = (gB[0] + gF[0] + gI[0], gB[1] + gF[1] + gI[1])
        check(f"{tag}: block gradings sum to (832, 832)", tot == (832, 832),
              str(tot))
        blk_reports.append((tag, gB, gF, gI, smax))

        # sub-grading of the SOURCE module S: joint (omega_4, omega_10)
        w4, c4 = normalize_involution(word(e, tuple(B)))
        w10, c10 = normalize_involution(word(e, tuple(F)))
        check(f"{tag}: [omega_4, omega_10] = 0 (even/even split)",
              fnorm(w4 @ w10 - w10 @ w4) < 1e-7)
        prod = w4 @ w10
        cprod = complex(np.trace(prod @ omega.conj().T)) / DIM
        check(f"{tag}: omega_4 omega_10 = c * omega with |c| = 1 "
              f"(2+1 product rule, even/even)",
              abs(abs(cprod) - 1.0) < 1e-6
              and fnorm(prod - cprod * omega) < 1e-6, f"c = {cprod:.3f}")
        joint = []
        for s4 in (+1, -1):
            for s10 in (+1, -1):
                P44 = 0.25 * ((np.eye(DIM) + s4 * w4) @ (np.eye(DIM) + s10 * w10))
                joint.append(int(round(float(np.trace(P44).real))))
        check(f"{tag}: joint (omega_4, omega_10) grading of S is 32/32/32/32",
              joint == [32, 32, 32, 32], str(joint))
        for s in (+1, -1):
            Pw = 0.5 * (np.eye(DIM) + s * (prod / cprod))
            t4 = complex(np.trace(w4 @ Pw))
            check(f"{tag}: omega_4 balanced INSIDE the omega={'+' if s > 0 else '-'}1 "
                  f"half of S (tr = 0)", abs(t4) < 1e-6, f"{t4:.2e}")

    balanced = all(g == (64, 64) for g in imp_gradings)
    print(f"\n[{form_name}] imposter gradings across allocations: {imp_gradings}",
          flush=True)
    print(f"[{form_name}] elapsed {time.time() - t0:.0f}s", flush=True)
    return balanced, imp_gradings, blk_reports


def main():
    t0 = time.time()
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print(f"[env] numpy {np.__version__}; Q2 imposter chirality grading, "
          f"both real forms, five allocations each", flush=True)

    res95 = run_form("(9,5)", [1.0] * 9 + [-1.0] * 5)
    res77 = run_form("(7,7)", [1.0] * 7 + [-1.0] * 7)

    print("\n" + "=" * 78)
    print("VERDICT — Q2 chirality grading (deterministic finite numerical computation, pre-deposit)")
    print("=" * 78)
    all_balanced = res95[0] and res77[0]
    # REGRESSION PIN of the preregistered/observed outcome (P-Q2-1): remove
    # only with a recorded re-derivation.
    assert all_balanced, ("regression pin: imposter grading was 64+64 balanced "
                          "under BOTH real forms and ALL allocations on 2026-08-03")
    for nm, res in (("(9,5)", res95), ("(7,7)", res77)):
        _, imp, blocks = res
        tag0, gB, gF, gI, _ = blocks[0]
        print(f"  {nm}: imposter 128 grades {imp[0][0]}+{imp[0][1]} under omega "
              f"(all five allocations identical); full structure "
              f"{gB[0]}+{gB[1]} / {gF[0]}+{gF[1]} / {gI[0]}+{gI[1]} "
              f"summing to (832, 832)")
    print("  Joint (omega_4, omega_10) grading of S: 32/32/32/32 — through the")
    print("  identification psi |-> x_psi, every internal chirality half appears")
    print("  with BOTH base-side chiralities in equal multiplicity: VECTORLIKE.")
    print("-" * 78)
    print("  PH-K1-KINEMATIC: the Reading-A imposter block is VECTORLIKE at")
    print("  the kinematic level.")
    print("  ==> PH-K1-KINEMATIC: CONFIRMED for Reading A.")
    print("      PH-K1-PHYSICAL: OPEN/BLOCKED on A/B adjudication and the")
    print("      observation/VEV/BRST/reality/SM-gauge map. Conditional only:")
    print("      unchanged descent without chiral selection or mirror decoupling")
    print("      would conflict with measured V-A weak currents. No anomaly claim.")
    print("-" * 78)
    print("MANDATORY FENCES: kinematic carrier only (Pi_RS^phys does not exist);")
    print("multiplicity is not count (blocks are not generations); imposter")
    print("reading A only (Q1 adjudicates A-vs-B); no verdict/bar/H59/claim")
    print("movement — results are pre-deposit under J5.")
    print(f"[summary] {_n_checks[0]} checks passed; elapsed {time.time() - t0:.0f}s; "
          f"exit 0", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
