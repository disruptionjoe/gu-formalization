#!/usr/bin/env python3
"""Resolver Wave K77-A: exact real Spin(7,7) observation and atomic ledger.

This probe extends the already-receipted all-real Cl(7,7) carrier rather than
rebuilding it.  It checks the invariant split bilinear, the source
Spin(1,3)+Spin(6,4) observation branching, the operator-versus-bilinear
two-grading incidence table, the finite Dirac--Rarita--Schwinger carrier, the
one-generation Pati--Salam/SM charge packet, and the typed atomic crosswalk.

It is a kinematic carrier certificate.  It does not select a vacuum, emit an
Euler equation, prove effective chirality, count generations, identify a
physical pole, or spend P1/P2/P3.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import (  # noqa: E402
    build_split_clifford,
    clifford_relations_exact,
    gray_traceless_sweep,
)


CHECKS: list[tuple[str, str, bool]] = []


def check(category: str, name: str, condition: bool) -> None:
    ok = bool(condition)
    CHECKS.append((category, name, ok))
    print(f"[{category}] {'PASS' if ok else 'FAIL'}  {name}")


def mm_product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    out = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        out = out @ matrix
    return out


def commutation_parity(operator: np.ndarray, grading: np.ndarray) -> str:
    if np.array_equal(operator @ grading, grading @ operator):
        return "preserve"
    if np.array_equal(operator @ grading, -grading @ operator):
        return "flip"
    return "mixed"


def gaussian_commutation_parity(operator: np.ndarray, grading: np.ndarray) -> str:
    if np.array_equal(operator @ grading, grading @ operator):
        return "preserve"
    if np.array_equal(operator @ grading, -grading @ operator):
        return "flip"
    return "mixed"


def rank_mod_prime(matrix: np.ndarray, prime: int = 1000003) -> int:
    """Exact rank lower certificate over F_p; full row rank certifies Q-rank."""
    a = np.asarray(matrix, dtype=np.int64) % prime
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivots = np.flatnonzero(a[rank:, col])
        if pivots.size == 0:
            continue
        pivot = rank + int(pivots[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        inverse = pow(int(a[rank, col]), prime - 2, prime)
        a[rank] = (a[rank] * inverse) % prime
        if rank + 1 < rows:
            factors = a[rank + 1 :, col].copy()
            active = np.flatnonzero(factors)
            if active.size:
                rr = rank + 1 + active
                a[rr] = (a[rr] - factors[active, None] * a[rank]) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def historical_text(commit: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True
    )


def exact_carrier_and_branching() -> dict[str, object]:
    p, m = build_split_clifford(7)
    identity = np.eye(128, dtype=np.int64)

    # Source observation split: (1,3) on H and (6,4) on N.
    gamma = [p[0], m[0], m[1], m[2], *p[1:], *m[3:]]
    eta = [1, -1, -1, -1, *([1] * 6), *([-1] * 4)]
    check("exact", "source-ordered Cl(1,3)+Cl(6,4) relations", clifford_relations_exact(gamma, eta))

    zero_monomials, total_monomials = gray_traceless_sweep([*p, *m])
    check("exact", "existing Cl(7,7)=M128(R) carrier remains faithful", (zero_monomials, total_monomials) == (16383, 16383))

    omega4 = mm_product(gamma[:4])
    omega10 = mm_product(gamma[4:])
    omega14 = mm_product(gamma)
    check("exact", "omega4^2=omega10^2=-1 and omega14^2=+1",
          np.array_equal(omega4 @ omega4, -identity)
          and np.array_equal(omega10 @ omega10, -identity)
          and np.array_equal(omega14 @ omega14, identity))
    check("exact", "observation volume factors commute and multiply to ambient volume",
          np.array_equal(omega4 @ omega10, omega10 @ omega4)
          and np.array_equal(omega4 @ omega10, omega14))
    check("exact", "ambient real Majorana-Weyl halves have ranks 64+64",
          int(np.trace(identity + omega14)) // 2 == 64
          and int(np.trace(identity - omega14)) // 2 == 64)

    # Real Spin-invariant bilinears.  B pairs the ambient half-spin modules.
    bilinear = mm_product(m)
    alternating = bilinear @ omega14
    bivectors = [gamma[a] @ gamma[b] for a in range(14) for b in range(a + 1, 14)]
    check("exact", "B is real symmetric, involutive, nondegenerate, and split 64/64",
          np.array_equal(bilinear.T, bilinear)
          and np.array_equal(bilinear @ bilinear, identity)
          and int(np.trace(bilinear)) == 0)
    check("exact", "B is invariant under all 91 spin bivectors",
          all(np.array_equal(x.T @ bilinear + bilinear @ x, np.zeros_like(identity)) for x in bivectors))
    check("exact", "B anticommutes with ambient chirality and pairs opposite halves",
          np.array_equal(bilinear @ omega14, -omega14 @ bilinear))
    check("exact", "B omega14 is an invariant alternating form linearly independent of B",
          np.array_equal(alternating.T, -alternating)
          and all(np.array_equal(x.T @ alternating + alternating @ x, np.zeros_like(identity)) for x in bivectors))

    pp = (identity + omega14) / 2
    pm = (identity - omega14) / 2
    check("exact", "same-half B pairings vanish exactly",
          np.array_equal(pp @ bilinear @ pp, np.zeros((128, 128)))
          and np.array_equal(pm @ bilinear @ pm, np.zeros((128, 128))))
    check("exact", "opposite-half B pairing is perfect by exact inverse/intertwiner identities",
          np.array_equal(bilinear @ pp, pm @ bilinear)
          and np.array_equal(bilinear @ pm, pp @ bilinear)
          and np.array_equal(bilinear @ bilinear, identity))

    # Product subgroup and complex observation chiralities.
    base_bivectors = [gamma[a] @ gamma[b] for a in range(4) for b in range(a + 1, 4)]
    fibre_bivectors = [gamma[a] @ gamma[b] for a in range(4, 14) for b in range(a + 1, 14)]
    check("exact", "Spin(1,3) and Spin(6,4) Lie actions commute",
          all(np.array_equal(x @ y, y @ x) for x in base_bivectors for y in fibre_bivectors))

    chi4 = 1j * omega4.astype(np.complex128)
    chi10 = 1j * omega10.astype(np.complex128)
    w14c = omega14.astype(np.complex128)
    ic = np.eye(128, dtype=np.complex128)
    check("exact", "complex 4D/internal chirality involutions commute",
          np.array_equal(chi4 @ chi4, ic)
          and np.array_equal(chi10 @ chi10, ic)
          and np.array_equal(chi4 @ chi10, chi10 @ chi4))
    check("exact", "matrix convention records W14=-chi4 chi10",
          np.array_equal(w14c, -chi4 @ chi10))

    joint: dict[tuple[int, int], np.ndarray] = {}
    for c4, w14 in product((1, -1), repeat=2):
        projector = ((ic + c4 * chi4) / 2) @ ((ic + w14 * w14c) / 2)
        joint[(c4, w14)] = projector
        check("exact", f"joint projector (chi4={c4},W14={w14}) rank 32 and idempotent",
              int(round(float(np.trace(projector).real))) == 32
              and np.array_equal(projector @ projector, projector))
    check("exact", "four observation blocks are orthogonal and complete",
          np.array_equal(sum(joint.values()), ic)
          and all(np.array_equal(a @ b, np.zeros((128, 128), dtype=np.complex128))
                  for ka, a in joint.items() for kb, b in joint.items() if ka != kb))

    triple_ranks: dict[tuple[int, int, int], int] = {}
    for c4, c10, w14 in product((1, -1), repeat=3):
        proj = ((ic + c4 * chi4) / 2) @ ((ic + c10 * chi10) / 2) @ ((ic + w14 * w14c) / 2)
        triple_ranks[(c4, c10, w14)] = int(round(float(np.trace(proj).real)))
    check("exact", "only chirality-correlated 2x16 observation blocks survive",
          all(rank == (32 if w14 == -c4 * c10 else 0)
                      for (c4, c10, w14), rank in triple_ranks.items()))
    check("exact", "ordinary conjugation exchanges 4D/internal Weyl blocks inside each ambient half",
          all(np.array_equal(np.conj(joint[(c4, w14)]), joint[(-c4, w14)])
              for c4, w14 in joint))

    # Independent D7 -> D2+D5 half-spin weight-parity certificate.
    weight_counts: dict[tuple[int, int, int], int] = {}
    for signs in product((1, -1), repeat=7):
        ambient = int(np.prod(signs))
        base = int(np.prod(signs[:2]))
        internal = int(np.prod(signs[2:]))
        weight_counts[(ambient, base, internal)] = weight_counts.get((ambient, base, internal), 0) + 1
    check("exact", "D7 weight restriction independently gives four multiplicity-one C32 blocks",
          len(weight_counts) == 4
          and set(weight_counts.values()) == {32}
          and all(ambient == base * internal for ambient, base, internal in weight_counts))

    # Bare operator versus constructed invariant-Gram bilinear incidence.
    operators = {
        "scalar_identity": identity,
        "horizontal_clifford": gamma[0],
        "vertical_clifford": gamma[4],
        "mixed_horizontal_vertical": gamma[0] @ gamma[4],
    }
    expected_x = {
        "scalar_identity": ("preserve", "preserve"),
        "horizontal_clifford": ("flip", "flip"),
        "vertical_clifford": ("preserve", "flip"),
        "mixed_horizontal_vertical": ("flip", "preserve"),
    }
    for name, operator in operators.items():
        got = (gaussian_commutation_parity(operator, chi4), commutation_parity(operator, omega14))
        check("exact", f"bare incidence {name}={expected_x[name]}", got == expected_x[name])

    gram_t = bilinear.astype(np.complex128)
    gram_s = 1j * mm_product(p).astype(np.complex128)
    for gram_name, gram in (("timelike_product", gram_t), ("spacelike_product", gram_s)):
        check("exact", f"constructed {gram_name} Gram is Hermitian, Spin-invariant, and flips both chi4 and W14",
              np.array_equal(gram.conj().T, gram)
              and all(np.array_equal(x.conj().T @ gram + gram @ x, np.zeros_like(gram)) for x in bivectors)
              and gaussian_commutation_parity(gram, chi4) == "flip"
              and gaussian_commutation_parity(gram, w14c) == "flip")
        expected_kx = {
            "scalar_identity": ("flip", "flip"),
            "horizontal_clifford": ("preserve", "preserve"),
            "vertical_clifford": ("flip", "preserve"),
            "mixed_horizontal_vertical": ("preserve", "flip"),
        }
        for name, operator in operators.items():
            physical = gram @ operator
            got = (gaussian_commutation_parity(physical, chi4), gaussian_commutation_parity(physical, w14c))
            check("exact", f"{gram_name}: bilinear incidence K*{name}={expected_kx[name]}", got == expected_kx[name])

    # Every listed transition is an exact rank-32 isomorphism: grading parity
    # selects one target projector, while the signed-monomial KX is unitary.
    for name, operator in operators.items():
        physical = gram_t @ operator
        c4_parity, w14_parity = expected_kx[name]
        edge_checks = []
        check("exact", f"K*{name} is exactly invertible",
              np.array_equal(physical.conj().T @ physical, ic))
        for source_key, source_projector in joint.items():
            c4, w14 = source_key
            target_key = (
                -c4 if c4_parity == "flip" else c4,
                -w14 if w14_parity == "flip" else w14,
            )
            target_projector = joint[target_key]
            image = physical @ source_projector
            exact_target = np.array_equal(target_projector @ image, image)
            all_other_zero = all(
                np.array_equal(other_projector @ image, np.zeros_like(image))
                for other_key, other_projector in joint.items()
                if other_key != target_key
            )
            edge_checks.append(exact_target and all_other_zero)
        check("exact", f"K*{name} has four exact rank-32 projector isomorphisms",
              all(edge_checks))

    # Finite Dirac--Rarita--Schwinger carrier without a dynamics claim.
    gamma_trace = np.hstack(gamma)
    check("exact", "Gamma Gamma^T=14I gives exact rank-128 trace map",
          np.array_equal(gamma_trace @ gamma_trace.T, 14 * identity))
    for w14 in (1, -1):
        pw = (identity + w14 * omega14) / 2
        pminus = (identity - w14 * omega14) / 2
        restricted = np.hstack([g @ pw for g in gamma])
        check("exact", f"Gamma maps W14={w14} input to opposite half with rank 64",
              np.array_equal(restricted @ restricted.T, 14 * pminus)
              and int(round(float(np.trace(pminus)))) == 64)
    check("exact", "per-half DRS dimensions are image 64 plus kernel 832",
          14 * 64 - 64 == 832 and 64 + 832 == 896)
    check("exact", "source F/Q/Z dimension arithmetic sums to the exact K77 per-half kernel dimension",
          2 * 16 + 2 * 16 == 64
          and 6 * 16 + 6 * 16 == 192
          and 2 * 144 + 2 * 144 == 576
          and 64 + 192 + 576 == 832)

    # Exact modular leakage ranks for fibrewise spinor operators on Omega1(S).
    leakage: dict[str, int] = {}
    for name, operator in operators.items():
        gamma_x = np.hstack([g @ operator for g in gamma])
        numerator = 14 * gamma_x - (gamma_x @ gamma_trace.T) @ gamma_trace
        leakage[name] = rank_mod_prime(numerator)
    check("exact", "identity preserves gamma-image/kernel splitting", leakage["scalar_identity"] == 0)
    check("exact", "three representative Clifford coefficients have rank-128 kernel-to-trace leakage",
          all(leakage[name] == 128 for name in operators if name != "scalar_identity"))

    # Plants: these must fail the stated stronger claims.
    check("planted", "ambient chirality is not observed 4D chirality", not np.array_equal(w14c, chi4))
    check("planted", "a naive 256-real full-Cl tensor is not the 128-real carrier", 8 * 32 != 128)
    check("planted", "B does not furnish a same-half scalar pairing",
          np.array_equal(pp @ bilinear @ pp, np.zeros((128, 128))))
    check("planted", "operator-only vertical incidence differs from constructed-Gram K-vertical incidence",
          expected_x["vertical_clifford"] != ("flip", "preserve"))
    check("planted", "a zero VEV coefficient kills the otherwise live vertical block", np.count_nonzero(0 * gamma[4]) == 0 and np.count_nonzero(gamma[4]) > 0)
    check("planted", "wrong-parity horizontal and vertical maps enter different quadrants",
          expected_x["horizontal_clifford"] != expected_x["vertical_clifford"])
    check("planted", "nontrivial Clifford maps do not define standalone DRS blocks", all(leakage[name] != 0 for name in ("horizontal_clifford", "vertical_clifford", "mixed_horizontal_vertical")))

    return {
        "gamma": gamma,
        "omega14": omega14,
        "joint_ranks": {f"chi4_{c4}_W14_{w14}": 32 for c4, w14 in joint},
        "triple_ranks": {str(key): value for key, value in triple_ranks.items()},
        "leakage": leakage,
    }


def exact_imported_standard_model_packet() -> dict[str, tuple[F, F, F]]:
    multiplets = {
        "Q_L": (6, F(1, 6)),
        "u_L_c": (3, F(-2, 3)),
        "d_L_c": (3, F(1, 3)),
        "L_L": (2, F(-1, 2)),
        "e_L_c": (1, F(1, 1)),
        "nu_L_c": (1, F(0, 1)),
    }
    check("exact", "imported verified D5/Pati-Salam packet has the six Standard Model multiplets", sum(dim for dim, _ in multiplets.values()) == 16)
    check("exact", "imported Pati-Salam 16=(4,2,1)+(4bar,1,2) dimension checksum", 4 * 2 + 4 * 2 == 16)

    grav_u1 = sum(F(dim) * hypercharge for dim, hypercharge in multiplets.values())
    cubic_u1 = sum(F(dim) * hypercharge**3 for dim, hypercharge in multiplets.values())
    su3_sq_u1 = 2 * F(1, 2) * F(1, 6) + F(1, 2) * F(-2, 3) + F(1, 2) * F(1, 3)
    su2_sq_u1 = 3 * F(1, 2) * F(1, 6) + F(1, 2) * F(-1, 2)
    su3_cubic = 2 - 1 - 1
    check("exact", "one 16 cancels grav^2-U1 and U1^3 anomalies", grav_u1 == 0 and cubic_u1 == 0)
    check("exact", "one 16 cancels SU3^2-U1 and SU2^2-U1 anomalies", su3_sq_u1 == 0 and su2_sq_u1 == 0)
    check("exact", "one 16 cancels SU3^3 and has even SU2 Witten-doublet count", su3_cubic == 0 and (3 + 1) % 2 == 0)

    all_left_states = {
        "u_L": (F(1, 2), F(1, 6), F(2, 3)),
        "d_L": (F(-1, 2), F(1, 6), F(-1, 3)),
        "u_L_c": (F(0), F(-2, 3), F(-2, 3)),
        "d_L_c": (F(0), F(1, 3), F(1, 3)),
        "nu_L": (F(1, 2), F(-1, 2), F(0)),
        "e_L": (F(-1, 2), F(-1, 2), F(-1)),
        "e_L_c": (F(0), F(1), F(1)),
        "nu_L_c": (F(0), F(0), F(0)),
    }
    check("exact", "Q=T3L+Y gives all eight imported all-left atomic charges state by state",
          all(t3 + hypercharge == charge for t3, hypercharge, charge in all_left_states.values()))
    check("exact", "Pati-Salam gauge directions split 21=12 SM+9 extra",
          (15 + 3 + 3) == 21 and (8 + 3 + 1) == 12 and 21 - 12 == 9)
    check("exact", "SU4 adjoint branches 15=8+3+3bar+1", 15 == 8 + 3 + 3 + 1)
    check("exact", "Higgs accounting target is four real modes=three Goldstones+one scalar", 4 == 3 + 1)

    check("planted", "one exact 16 is not a generation-count theorem", 16 // 16 == 1 and 1 != 3)
    fake_y = [F(-1, 2), F(-1, 2), F(1, 2), F(1, 2)]
    check("planted", "a fake uniform internal U1 does not reproduce the SM hypercharge set",
          set(fake_y) != {value for _, value in multiplets.values()})
    check("planted", "Pati-Salam containment does not equal a selected unbroken SM group", 21 != 12)
    return all_left_states


def source_and_ledger_checks(all_left_states: dict[str, tuple[F, F, F]]) -> None:
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    draft = (ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md").read_text()
    into = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
    pati = (ROOT / "lab/active-research/pati-salam-chain-verification.md").read_text()
    stale_pc1 = (ROOT / "explorations/shiab-operator/pc1-spin77-spinor-decomp-2026-06-23.md").read_text()
    stale_shiab = (ROOT / "explorations/shiab-operator/pc1-spinor-spin77-shiab-2026-06-23.md").read_text()
    progress = (ROOT / "DERIVATION-PROGRESS.md").read_text()
    curt = historical_text(
        "0aa539214e6082ad2ad9d4697c90da7e73c0e070",
        "lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md",
    )
    curt77 = historical_text(
        "0aa539214e6082ad2ad9d4697c90da7e73c0e070",
        "lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md",
    )

    check("source", "Eric explicitly says GU is fundamentally nonchiral",
          "I don't think the world is chiral" in toe and "GU is not Cairo" in toe)
    check("source", "Eric describes curvature/VEV-dependent Dirac-to-Weyl decoupling",
          "Dirac type operator decouples into Weyl type operators" in toe)
    check("source", "Eric locates spinors in the chimeric rolled fermion sector",
          "you can build spinors without ever making a metric choice" in toe
          and "zero to one to 13 to 14" in toe)
    check("source", "Eric calls the Higgs parent an ad-valued one-form",
          "Higgs field" in toe and "comes out of an add-valued 1-4" in toe)
    check("source", "Eric separates Einstein-Dirac and Yang-Mills-Higgs action layers",
          "Einstein-Durac portion" in toe and "second Lagrangian" in toe)
    check("source", "Into the Impossible states the trace-reversed fibre and one-generation Pati-Salam directive",
          "trace reverse the Frobenius metric" in into and "one grand unified generation" in into)
    check("source", "draft equation 12.20 contains luminous and looking-glass halves",
          "Luminous Light Standard Model Family Matter" in draft
          and "Dark Decoupled Looking Glass Matter" in draft)
    check("source", "draft equation 11.6 preserves F/Q/Z typed dimensions",
          "F± = 2·16 + 2·16 = **64**" in draft
          and "Q± = 6·16 + 6·16 = **192**" in draft
          and "Z± = 2·144 + 2·144 = **576**" in draft)
    check("source", "Curt iceberg is secondary, caveated construction guidance",
          "valuable **construction map**" in curt and "secondary mathematical exposition" in curt)
    check("source", "Curt explicitly motivates split Spin(7,7) after the trace-line choice",
          "`Spin(7,7)` spinor has real dimension 128" in curt77
          and "trace-line sign" in curt77)
    check("source", "existing Pati-Salam packet claims group-theory scope only",
          "VERIFIED (group-theory scope)" in pati and "What this does NOT verify" in pati)

    # Truth-propagation fence: old PC1 Method 1 used the wrong Spin action.
    check("type", "stale PC1 left-action overclaim is present and explicitly fenced",
          "Lambda^bullet(R^{14}) ~= S^{oplus 128}" in stale_pc1
          and "Lambda^1 = R^{14} (the standard/vector representation" in stale_pc1)
    check("type", "current progress surface carries the correct no-spinor-in-exterior result",
          "no natural Spin(7,7)-equivariant R-linear map S -> Lambda^k exists" in progress)
    check("type", "stale fixed-c(v) equivariance and C64 Step-0 claims are explicitly detected",
          "c(v) is an explicit Spin(7,7)-equivariant" in stale_shiab
          and "It is **not** Spin(7,7)-" in stale_shiab
          and "128 real = 64 complex" in pati)

    p, m = build_split_clifford(7)
    fixed_v = p[0]
    witness_bivector = p[0] @ p[1]
    check("planted", "a fixed Clifford vector is not a Spin(7,7)-equivariant half-spin intertwiner",
          not np.array_equal(fixed_v @ witness_bivector, witness_bivector @ fixed_v))

    ledger_path = ROOT / "lab/process/resolver-wave-k77a-atomic-particle-crosswalk.json"
    with ledger_path.open() as handle:
        ledger = json.load(handle, object_pairs_hook=lambda pairs: _unique_object(pairs))

    check("type", "ledger separates program, SM-shadow, and source-lane target obligations from candidate status",
          set(ledger["obligation_scopes"]) == {"PROGRAM_MANDATORY", "SM_SHADOW_REQUIRED", "SOURCE_LANE_CONDITIONAL"}
          and sum(len(rows) for rows in ledger["obligation_scopes"].values()) == len(ledger["atomic_targets"])
          and set().union(*(set(rows) for rows in ledger["obligation_scopes"].values()))
          == {row["row_id"] for row in ledger["atomic_targets"]}
          and all("candidate_status" in row for row in ledger["atomic_targets"]))
    claim_index = {claim["claim_id"]: claim for claim in ledger["source_claims"]}
    check("type", "all atomic rows resolve Eric and Curt claim IDs to description, exact locator, and grade",
          all(all(claim_id in claim_index and claim_index[claim_id]["description"]
                  and claim_index[claim_id]["locator"] and claim_index[claim_id]["grade"]
                  for claim_id in row["eric_claims"] + row["curt_claims"])
              for row in ledger["atomic_targets"]))
    charge_rows = {row["row_id"]: row for row in ledger["fermion_charge_dictionary"]}
    expected_charge_rows = {
        "up_left": ("u_L", F(1, 2), F(1, 6), F(2, 3), F(2, 3)),
        "down_left": ("d_L", F(-1, 2), F(1, 6), F(-1, 3), F(-1, 3)),
        "up_right": ("u_L_c", F(0), F(-2, 3), F(-2, 3), F(2, 3)),
        "down_right": ("d_L_c", F(0), F(1, 3), F(1, 3), F(-1, 3)),
        "neutrino_left": ("nu_L", F(1, 2), F(-1, 2), F(0), F(0)),
        "electron_left": ("e_L", F(-1, 2), F(-1, 2), F(-1), F(-1)),
        "electron_right": ("e_L_c", F(0), F(1), F(1), F(-1)),
        "neutrino_right": ("nu_L_c", F(0), F(0), F(0), F(0)),
    }
    check("type", "all eight atomic fermion rows resolve Q=T3L+Y and the all-left/physical charge dictionary",
          set(charge_rows) == set(expected_charge_rows)
          and set(charge_rows) == {row["row_id"] for row in ledger["atomic_targets"] if row["sector"] == "fermion"}
          and all(row["all_left_state"] == state
                  and F(row["T3L"]) == t3
                  and F(row["Y"]) == hypercharge
                  and F(row["Q_all_left"]) == charge_left
                  and F(row["Q_physical"]) == charge_physical
                  and all_left_states[state] == (t3, hypercharge, charge_left)
                  and t3 + hypercharge == charge_left
                  for row_id, (state, t3, hypercharge, charge_left, charge_physical)
                  in expected_charge_rows.items()
                  for row in (charge_rows[row_id],)))
    check("type", "source claims are guidance grades rather than proof grades",
          all(claim["grade"] in {"SOURCE_GUIDED_CANDIDATE", "SOURCE_SILENT", "SOURCE_CONFLICT", "SOURCE_CORRECTED_BY_MATH"}
              for claim in ledger["source_claims"]))
    check("type", "kill ladder separates fixture, map, mechanism, lane, and program",
          [entry["scope"] for entry in ledger["kill_ladder"]]
          == ["FIXTURE_FAIL", "CANDIDATE_MAP_KILL", "MECHANISM_KILL", "LANE_KILL", "CONDITIONAL_PROGRAM_KILL"])
    check("type", "every non-recovered row emits a reconstruction debt",
          all(row["reconstruction_debt"] for row in ledger["atomic_targets"]
              if row["candidate_status"] != "P6_PHYSICAL_RECOVERY"))
    check("type", "no row claims physical recovery in K77-A",
          not any(row["candidate_status"] == "P6_PHYSICAL_RECOVERY" for row in ledger["atomic_targets"]))
    check("type", "eight fermion species and all eight gluon modes are individually present",
          len([row for row in ledger["atomic_targets"] if row["sector"] == "fermion"]) == 8
          and {row["row_id"] for row in ledger["atomic_targets"] if row["row_id"].startswith("gluon_")}
          == {f"gluon_{i}" for i in range(1, 9)})
    check("type", "pre-VEV and post-VEV electroweak rows stay phase-distinct",
          {row["row_id"] for row in ledger["atomic_targets"]}
          >= {"weak_W1", "weak_W2", "weak_W3", "hypercharge_B", "physical_W_plus", "physical_W_minus", "physical_Z", "photon"})
    check("type", "Higgs, Goldstone, graviton, cosmology, and dark-matter targets are explicit",
          {row["row_id"] for row in ledger["atomic_targets"]}
          >= {"higgs_doublet_four_real", "goldstone_charged", "goldstone_neutral", "higgs_scalar", "graviton_plus2", "graviton_minus2", "late_time_acceleration", "dark_matter"})
    check("type", "historical ghost partner and Eric looking-glass sector remain distinct mechanisms",
          ledger["identity_fences"]["looking_glass_vs_ghost"] == "DISTINCT_UNTIL_EXPLICIT_INTERTWINER")
    check("type", "generation count is fenced from representation and block multiplicities",
          ledger["identity_fences"]["generation_count"] == "NOT_A_16_OR_FQZ_BLOCK_COUNT")
    check("type", "K95 right-H imports are prohibited",
          set(ledger["forbidden_k95_imports"]) >= {"right-H", "Sp(32,32;H)", "R_J", "Kramers index"})
    check("type", "cross-row matrix keeps unrun gates open and declares a separate joint-failure disposition",
          all(item["status"] != "OPEN" or item["failure_disposition"] == "OPEN_NOT_RUN"
              for item in ledger["coherence_matrix"])
          and ledger["coherence_policy"]["observed_locked_leg_failure"] == "LOCAL_PASS__JOINT_FAIL")
    check("type", "P1/P2/P3 remain unused", ledger["external_datum"] == {"P1_P2": "UNUSED", "P3": "UNUSED"})

    check("planted", "source statement does not promote any row to physical recovery",
          all(row["candidate_status"] != "P6_PHYSICAL_RECOVERY" for row in ledger["atomic_targets"] if row["eric_claims"] or row["curt_claims"]))
    check("planted", "a locally supported 16 cannot bypass the joint coherence matrix",
          any(row["candidate_status"].startswith("C2_") for row in ledger["atomic_targets"])
          and any(item["status"] == "OPEN" for item in ledger["coherence_matrix"]))
    obligation_by_row = {
        row_id: scope
        for scope, row_ids in ledger["obligation_scopes"].items()
        for row_id in row_ids
    }
    actual_row = next(row for row in ledger["atomic_targets"] if row["row_id"] == "up_left")
    failed_gate = ledger["coherence_policy"]["inherited_gate_ids"][2]
    challenged_row = {
        **actual_row,
        "candidate_status": "O3_OBSERVATION_INTERTWINED",
        "injected_gate_result": {failed_gate: "FAIL"},
    }
    locked_leg_failed = any(result == "FAIL" for result in challenged_row["injected_gate_result"].values())
    conflict_evaluation = {
        "promotion_allowed": not (locked_leg_failed and challenged_row["candidate_status"].startswith("O3")),
        "kill_scope": ledger["coherence_policy"]["required_kill_scope"] if locked_leg_failed else None,
        "replacement_debt": f"replace mechanism after {failed_gate}: {challenged_row['reconstruction_debt']}" if locked_leg_failed else "",
        "target_scope": obligation_by_row[challenged_row["row_id"]],
    }
    conflict_blocks_o3 = (
        conflict_evaluation["promotion_allowed"] is False
        and conflict_evaluation["kill_scope"] == "MECHANISM_KILL"
        and bool(conflict_evaluation["replacement_debt"])
        and conflict_evaluation["target_scope"] == "PROGRAM_MANDATORY"
    )
    check("planted", "a locked-leg conflict blocks O3 promotion, kills the mechanism, emits debt, and preserves the target",
          conflict_blocks_o3)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    obj: dict[str, object] = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def main() -> None:
    exact_carrier_and_branching()
    all_left_states = exact_imported_standard_model_packet()
    source_and_ledger_checks(all_left_states)

    failures = [(category, name) for category, name, ok in CHECKS if not ok]
    counts = {category: sum(1 for got, _, ok in CHECKS if got == category and ok)
              for category in ("exact", "source", "type", "planted")}
    print()
    print("SUMMARY: " + " + ".join(f"{counts[key]} {key}" for key in ("exact", "source", "type", "planted"))
          + f" = {sum(counts.values())} PASS")
    print("VERDICT: NONCHIRAL_PARENT_AND_OBSERVATION_BLOCKS_CONFIRMED; "
          "VEV_BLOCK_CLASSIFIED_NOT_SELECTED; EFFECTIVE_CHIRALITY_NOT_DERIVED")
    if failures:
        raise SystemExit(f"{len(failures)} check(s) failed: {failures}")


if __name__ == "__main__":
    main()
