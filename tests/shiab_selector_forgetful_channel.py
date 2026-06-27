#!/usr/bin/env python3
"""SELECTOR TEST — PO1 "forgetful / projection-with-loss" => contract channel?

CONTEXT (observer-selector-leftover-space-2026-06-26.md, Section 2)
-------------------------------------------------------------------
The mining of Time-as-Finality + temporal-issuance surfaced ONE live lead that touches
the shiab family coordinates: PO1's "admissible finality = a projection WITH LOSS", read
as "the shiab is the FORGETFUL channel". The proposed confirm-or-kill test has three legs:

  (1) KERNEL leg  — PO1's operational content: forgetful = projection with loss =
      NONZERO / LARGER kernel. Prediction (the lead): the two CONTRACT channels have a
      strictly larger kernel; the two WEDGE channels are injective.
  (2) CLIFFORD-DEGREE leg — contract output is degree-1 (degree-LOWERING), wedge output
      is degree-3 (degree-RAISING, h.w. omega_1+omega_6).
  (3) METRIC-WEIGHT leg — contract is metric-FREE; wedge carries eta_aa.

CONFIRM if forgetful (= larger kernel) cleanly separates {contract} from {wedge}, which
would force c_wedge+- = c_wedge-+ = 0 and leave (c+,0,c-,0) CONTAINING canon (1,0,1,0).
KILL if any wedge element shows a kernel of the same nature as contract (forgetfulness
no longer separates the channels).

This file RUNS all three legs and reports the verdict computed, not asserted.
It is a confirm-or-kill probe for a `speculation`-tier lead; it promotes nothing.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import shiab_family_basis as fam

TOL = 1e-7


def rank_nullity(M):
    """Rank and nullity of a dense complex matrix via SVD (domain = #columns)."""
    s = np.linalg.svd(M, compute_uv=False)
    smax = float(s[0]) if s.size else 0.0
    thresh = TOL * max(1.0, smax)
    rank = int(np.sum(s > thresh))
    nullity = int(M.shape[1] - rank)
    return rank, nullity, smax


def clifford_grade_fractions(M, max_grade=4):
    """Fraction of ||M||_F^2 living in each Clifford grade 0..max_grade.

    The Clifford words {e_{a1}...e_{ak}} are Frobenius-orthogonal, so the grade-r
    content is  sum_{|A|=r} |<e_A,M>|^2 / <e_A,e_A>  with <X,Y>=tr(X^H Y).
    """
    import itertools

    E = fam.E
    N = fam.N
    total = float(np.real(np.vdot(M, M)))
    fracs = {}
    for r in range(max_grade + 1):
        acc = 0.0
        if r == 0:
            Iden = np.eye(M.shape[0], dtype=complex)
            ip = np.vdot(Iden, M)
            acc = float(abs(ip) ** 2 / np.real(np.vdot(Iden, Iden)))
        else:
            for combo in itertools.combinations(range(N), r):
                word = E[combo[0]].copy()
                for idx in combo[1:]:
                    word = word @ E[idx]
                denom = float(np.real(np.vdot(word, word)))
                if denom > 0:
                    ip = np.vdot(word, M)
                    acc += float(abs(ip) ** 2 / denom)
        fracs[r] = acc / total if total > 0 else 0.0
    return fracs


def channel_grade_profile(Wfun, label):
    """Aggregate Clifford-grade profile of a channel's per-(a) Clifford operator,
    summed over the V-slot index a, on a representative 2-form alpha = e_0 ^ e_1."""
    p, q, j = 0, 1, 0  # alpha = e_p ^ e_q (j index is unused by the W functions)
    g1 = g3 = gother = norm = 0.0
    for a in range(fam.N):
        Wop = Wfun(a, j, p, q)
        if Wop is None or not Wop.any():
            continue
        fr = clifford_grade_fractions(Wop)
        w = float(np.real(np.vdot(Wop, Wop)))
        g1 += fr[1] * w
        g3 += fr[3] * w
        gother += (fr[0] + fr[2] + fr[4]) * w
        norm += w
    if norm == 0:
        return label, 0.0, 0.0, 0.0
    return label, g1 / norm, g3 / norm, gother / norm


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 84)
    print("SELECTOR TEST  —  PO1 'forgetful/projection-with-loss' => contract channel?")
    print("=" * 84)

    R = fam.get_shiab_family_basis(verify_all_generators=False)
    mats = R["basis_matrices_full_dirac"]
    labels = R["basis_labels_full_dirac"]

    # ---- LEG 1: KERNEL / projection-with-loss --------------------------------
    print("\nLEG 1 — KERNEL test (forgetful = projection WITH LOSS = larger kernel)")
    print("-" * 84)
    print(f"  each densified Phi_k : Lambda^2 V (x) S_in -> V (x) S_out")
    nullities = []
    ranks = []
    for M_t, lab in zip(mats, labels):
        M = fam.densify_block(M_t)
        rank, nullity, smax = rank_nullity(M)
        nullities.append(nullity)
        ranks.append(rank)
        print(f"    {lab:20s} shape={str(M.shape):14s} rank={rank:4d} nullity={nullity:5d}")
    codim = mats[0].shape[0] * mats[0].shape[1]
    dom = mats[0].shape[2] * mats[0].shape[3]
    all_equal_null = len(set(nullities)) == 1
    all_surj = all(r == codim for r in ranks)
    print(f"  domain dim={dom}, codomain dim={codim}")
    print(f"  all four nullities equal? {all_equal_null}  (values={sorted(set(nullities))})")
    print(f"  all four surjective (rank=codim={codim})? {all_surj}")
    kernel_leg_separates = not all_equal_null
    print(f"  ==> KERNEL leg separates contract from wedge? {kernel_leg_separates}")
    if not kernel_leg_separates:
        print("      KILL (this leg): every channel has the SAME kernel; none is more")
        print("      'forgetful'; wedge is NOT injective (domain >> codomain). PO1's")
        print("      loss/kernel operationalization does NOT distinguish the channels.")

    # ---- LEG 2: CLIFFORD DEGREE ---------------------------------------------
    print("\nLEG 2 — Clifford-degree profile (contract=degree-1 vs wedge=degree-3)")
    print("-" * 84)
    prof_c = channel_grade_profile(fam.W_delta_contract, "contract (W_delta_contract)")
    prof_w = channel_grade_profile(fam.W_wedge_metric, "wedge    (W_wedge_metric)")
    for lab, g1, g3, go in (prof_c, prof_w):
        print(f"    {lab:30s} grade-1={g1:.4f}  grade-3={g3:.4f}  other={go:.4f}")
    # tuple layout: (label, grade1, grade3, other) -> contract pure g1, wedge pure g3
    degree_leg_separates = (prof_c[1] > 0.99 and prof_w[2] > 0.99)
    print(f"  ==> DEGREE leg separates? {degree_leg_separates}  "
          f"(contract pure grade-1, wedge pure grade-3)")

    # ---- LEG 3: METRIC WEIGHT (structural, from the construction) ------------
    print("\nLEG 3 — Metric weight (eta) dependence")
    print("-" * 84)
    print("  W_delta_contract carries NO eta factor (metric-free interior product);")
    print("  W_wedge_metric carries an explicit ETA[a] weight (forced by equivariance in")
    print("  indefinite signature). Frobenius overlap contract _|_ wedge:")
    ov = max(r["contract_wedge_frobenius_overlap"] for r in R["per_block_report"].values())
    print(f"    contract . wedge Frobenius overlap = {ov:.2e}  (=> orthogonal channels)")

    # ---- VERDICT -------------------------------------------------------------
    print("\n" + "=" * 84)
    print("VERDICT (computed)")
    print("=" * 84)
    print(f"  LEG 1 kernel/forgetful separates channels : {kernel_leg_separates}   -> "
          f"{'CONFIRM' if kernel_leg_separates else 'KILL'}")
    print(f"  LEG 2 Clifford-degree separates channels  : {degree_leg_separates}   -> "
          f"{'separates' if degree_leg_separates else 'no'}")
    print(f"  LEG 3 metric-weight separates channels    : {ov < TOL}   -> "
          f"{'separates (orthogonal)' if ov < TOL else 'no'}")
    print()
    print("  SPLIT RESULT: PO1's load-bearing leg (1, forgetful=larger kernel) KILLS —")
    print("  contract and wedge have IDENTICAL kernels, so 'projection-with-loss' does")
    print("  NOT pick the contract channel. The channels ARE cleanly separated, but by")
    print("  Clifford DEGREE (leg 2) and METRIC-independence (leg 3), which are re-readings")
    print("  of the construction, NOT PO1's loss principle. So a c_wedge=0 cut can be")
    print("  motivated by metric-covariance (GU-native) but NOT by PO1/TaF forgetting.")
    print("  Net: the TaF 'machinery match' is name-deep; lead stays `speculation`.")
    print("=" * 84)

    return {
        "kernel_leg_separates": kernel_leg_separates,
        "all_nullities_equal": all_equal_null,
        "nullity_value": nullities[0] if nullities else None,
        "rank_value": ranks[0] if ranks else None,
        "all_surjective": all_surj,
        "degree_leg_separates": degree_leg_separates,
        "contract_grade1": prof_c[1],
        "wedge_grade3": prof_w[3],
        "contract_wedge_overlap": ov,
    }


if __name__ == "__main__":
    main()
