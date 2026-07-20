#!/usr/bin/env python3
"""D1 C-operator build probe -- the interacting C-operator constructed on gu's
structures with the Bender-Mannheim technology, plus the degeneracy check.

CHANNEL: CH-REC D1 (the typed conditionality of the P-T3-W229 MEMBER verdict),
         executed as the blockbuster follow-through swing 2026-07-19.
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/d1-coperator-build-2026-07-19.md (five-lens council +
         primary verification; this script implements the machine-checkable
         half). Primary sources read in full this swing: arXiv:2104.03708,
         arXiv:2004.00376 (Mannheim; technology import ONLY, never the
         ontology -- gu's mirror half stays real/gapped/causality-required).
STATUS:  exploration tier; conditional (R0_COND); no claim/canon/posture moves.

WHAT IS BUILT. The Bender-Mannheim dynamical C-operator (equivalently the
positive V-metric G = K.C effecting V H V^-1 = H-dagger with positive norm,
arXiv:2104.03708 eq 1.4 + Sec V) is constructed from the spectral data of the
CH-QM toy Hamiltonian -- gu's structural miniature: Krein form B, baked-in
orientation sigma*, three hyperbolic (generation, mirror) record pairs, gauge
block, causality coupling, record drive. Recipe (the R1 big-swing recipe, now
on gu's own fixture): group eigenvalues, B-orthogonalize each real eigengroup,
C = sum_k sign(nu_k) P_k with nu_k the measured Krein norms and P_k the
K-orthogonal projectors. NO free choice enters. K-indefinite or K-null
eigengroups abort the recipe -- that abort IS the honest failure mode.

CHECKS (swing items 2a/2b/2c and 3):
  [T] toy fidelity (H reproduces ch_qm_graded_quotient_toy's part-B
      Hamiltonian bit-exactly) and primary anchors: the PU 4x4 mode matrix is
      diagonalizable at w1 != w2 and DEFECTIVE (Jordan) at w1 = w2
      (2104.03708 Sec VII, eq 7.9); the Q-operator coefficient
      alpha = log((w1+w2)/(w1-w2))/(w1 w2) grows without bound at the
      boundary (eq 5.7) -- V = e^-Q determination is singular there.
  [E] (a) dynamical determination, non-degenerate regime: C exists on the
      real-spectrum matter sector (7 states; the 2 complex-pair gauge states
      are Mannheim's third realization, quotiented), C^2 = Pi, [C,H] = 0,
      G = B.C Hermitian positive of full sector rank, G H = H^dag G; stable
      under pseudo-Hermitian perturbation; the global sign is PINNED by
      G > 0 (-C inadmissible) -- the only Z/2 freedom is the JOINT anchor
      flip (B,C) -> (-B,-C), payload item 1, co-flip verified. The two
      cross-pair degeneracies (E = mu+delta and mu-delta, each 3-fold,
      K-DEFINITE) are the benign parity-non-mixing kind (R1's qualifier).
  [E] (b) C grades records positive: record modes w(i,+sigma*) C-positive,
      mirrors C-negative; C restricted to the record pairs EQUALS the
      kinematic K-grading EXACTLY, causality coupling on -- the interacting C
      is IDENTIFIABLE with the kinematic orientation (the audit's watched
      second anchor freedom does NOT appear); register direction = eps on
      C-confined draws; the wrong-orientation candidate sector is graded
      NEGATIVE (the interacting-grade Q6 refusal). A weak record drive
      dresses the grading without moving it; the toy part-D drive strength
      sits ABOVE the PT threshold and breaks the near-resonant cross-norm
      pair into complex eigenvalues -- a named finding: an overdriven
      register loses definite grade (realization 3), so interaction-grade
      record drives carry a PT-unbroken-ness condition.
  [F] (c) SRC-COH-1 control: feeding -B to the recipe slot while the register
      keeps B anti-aligns the grading exactly -- the Da3/mu-import shape.
  [E] DEGENERACY CHECK (the armed falsification): at gu's vacuum-anchor
      degeneracy (delta -> 0: every record pair exactly degenerate, each
      eigenspace K-balanced -- the toy image of the R3 sign-blind result and
      of the exactly-degenerate K_S = +/-1 vacuum anchors, which the Casimir
      scalar check ties to the actual Cl(9,5) carrier):
        - H stays DIAGONALIZABLE: gu's degeneracy is NOT the PU Jordan form;
        - C-determination FAILS by NON-UNIQUENESS: the recipe aborts
          (K-indefinite eigengroup) and an explicit continuum of admissible
          C's (hyperbolic boosts) all satisfy C^2 = Pi, [C,H] = 0, B.C >= 0;
          dynamics selects none;
        - given the anchor B the canonical Z/2-typed choice is pinned
          (-C_swap inadmissible): the datum dynamics fails to supply is
          exactly the anchor eps -- the external Z/2 -- not a new bit;
  [F] the continuum COLLAPSES when the gap is restored (delta != 0 kills
      [C_s, H] = 0 for s != 0): dynamical determination IS the gapped-pair
      phenomenon; at exactly-degenerate anchors it fails. (If C were still
      determined at delta = 0 the external-bit result would break -- checked,
      it is not.)

NONCLAIMS. Toy-grade: the 9-dim fixture, not the 192-dim triplet (lift path
in the swing doc); no claim about GU's unbuilt S_IG; Mannheim's ontology
(ghost reinterpreted away, no negative metric) NOT imported -- the Krein form
stays real and the mirror sector stays in the state space throughout.
Deterministic; numpy only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import ch_qm_graded_quotient_toy as toy  # noqa: E402  (fidelity anchor only)
import gen_sector_bridge as gb           # noqa: E402  (verified Cl(9,5) rep)

TOL = 1e-9
RNG = np.random.default_rng(20260719)
RESULTS = []

DIM = 9
OMEGA, GAMMA, MU, DELTA0, CPL, LAM_D = 1.0, 0.7, 1.3, 0.2, 0.35, 0.15
SIGMA_STAR = +1


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def record_register(qs, eps, mu=1):
    """CH-REC composition interface (identical to the sibling probes)."""
    n = 0.0
    out = [n]
    for q in qs:
        n = n + mu * eps * q
        out.append(n)
    return out


# --- gu-structure builders (parametrized mirror of the CH-QM toy) ------------

def basis_vec(i):
    v = np.zeros(DIM, dtype=complex)
    v[i] = 1.0
    return v


def build_B():
    B = np.zeros((DIM, DIM), dtype=complex)
    B[0, 0] = 1.0
    B[1, 2] = B[2, 1] = 1.0
    for i in range(3):
        B[3 + i, 6 + i] = B[6 + i, 3 + i] = 1.0
    return B


def n_vec(sigma):
    return (basis_vec(1) + 1j * sigma * basis_vec(2)) / np.sqrt(2)


def w_vec(i, sign):
    return (basis_vec(3 + i) + sign * basis_vec(6 + i)) / np.sqrt(2)


def build_H(B, delta=DELTA0, cpl=CPL, drive=0.0):
    """The CH-QM toy dynamics with the pair gap delta, causality coupling cpl
    and record-drive strength as parameters (delta = DELTA0, cpl = CPL,
    drive = 0 reproduces the toy's part-B H exactly; drive = LAM_D adds the
    toy's part-D record drive; delta -> 0 is gu's vacuum-anchor degeneracy)."""
    H = np.zeros((DIM, DIM), dtype=complex)
    H[0, 0] = OMEGA
    npv, nmv = n_vec(SIGMA_STAR), n_vec(-SIGMA_STAR)
    S = np.column_stack([npv[1:3], nmv[1:3]])
    H[1:3, 1:3] = S @ np.diag([1j * GAMMA, -1j * GAMMA]) @ np.linalg.inv(S)
    for i in range(3):
        H[3 + i, 3 + i] = H[6 + i, 6 + i] = MU
        H[3 + i, 6 + i] = H[6 + i, 3 + i] = delta
    w1 = w_vec(0, +1)
    H = H + cpl * (np.outer(npv, np.conj(B @ w1)) + np.outer(w1, np.conj(B @ npv)))
    if drive:
        t_v, q1 = basis_vec(0), basis_vec(3)
        H = H + drive * (np.outer(t_v, np.conj(B @ q1)) + np.outer(q1, np.conj(B @ t_v)))
    assert np.linalg.norm(B @ H - H.conj().T @ B) < TOL, "H must be pseudo-Hermitian"
    return H


# --- the Bender-Mannheim recipe on a Krein fixture ---------------------------

def bm_c_operator(H, B, tol_real=1e-8, tol_group=1e-6, tol_null=1e-8):
    """C = sum sign(nu_k) P_k over the real-spectrum sector, with K-orthogonal
    projectors built per eigengroup. Returns (C, info). Raises ValueError if a
    real eigengroup is K-indefinite or K-null (the recipe's honest failure)."""
    evals, V = np.linalg.eig(H)
    real_idx = [k for k in range(len(evals)) if abs(evals[k].imag) < tol_real]
    cplx_idx = [k for k in range(len(evals)) if abs(evals[k].imag) >= tol_real]
    groups, used = [], set()
    for k in real_idx:
        if k in used:
            continue
        g = [j for j in real_idx if abs(evals[j].real - evals[k].real) < tol_group]
        used.update(g)
        groups.append(g)
    C = np.zeros((DIM, DIM), dtype=complex)
    Pi_sector = np.zeros((DIM, DIM), dtype=complex)
    nus = []
    for g in groups:
        W = V[:, g]                                   # eigengroup basis
        Gm = W.conj().T @ B @ W                       # Krein Gram of the group
        Gm = 0.5 * (Gm + Gm.conj().T)
        ev, U = np.linalg.eigh(Gm)
        if any(abs(x) < tol_null for x in ev):
            raise ValueError(
                f"K-null direction in eigengroup at E = {evals[g[0]].real:.4f}"
                f" (Gram eigenvalues {np.round(ev, 6)}) -- C undefined")
        if not (all(x > tol_null for x in ev) or all(x < -tol_null for x in ev)):
            raise ValueError(
                f"K-INDEFINITE eigengroup at E = {evals[g[0]].real:.4f}"
                f" (Gram eigenvalues {np.round(ev, 6)}) -- C non-unique")
        Wo = W @ U                                    # K-orthogonal basis
        for j in range(Wo.shape[1]):
            v = Wo[:, j]
            nu = float((v.conj() @ B @ v).real)
            nus.append(nu)
            P = np.outer(v, np.conj(B @ v)) / nu      # K-orthogonal projector
            C += np.sign(nu) * P
            Pi_sector += P
    info = {"n_real": len(real_idx), "n_complex": len(cplx_idx),
            "min_abs_nu": min(abs(x) for x in nus) if nus else 0.0,
            "Pi": Pi_sector, "evals": evals}
    return C, info


def c_on_pairs(C, B, pair_modes):
    """C in the Krein pair-mode frame: entries K(a, C b) * sign(K(a,a))."""
    return np.array([[complex(np.conj(a) @ B @ (C @ b)) * np.sign(
        float((a.conj() @ B @ a).real)) for b in pair_modes] for a in pair_modes])


# =============================================================================
print("=" * 78)
print("PART 0  toy fidelity + primary anchors (arXiv:2104.03708 / 2004.00376)")
print("=" * 78)

B = build_B()
H = build_H(B)                                        # part-B H: drive = 0

check("T", "gu fixture fidelity: H reproduces the CH-QM toy part-B "
           "Hamiltonian exactly (same B, sigma*, gap, gauge block, causality "
           "coupling)",
      np.allclose(H, toy.build_H(toy.build_B()), atol=1e-14)
      and np.allclose(B, toy.build_B()),
      f"||dH|| = {np.linalg.norm(H - toy.build_H(toy.build_B())):.1e}")


def pu_mode_matrix(w1, w2):
    """First-order system for z'''' + (w1^2 + w2^2) z'' + w1^2 w2^2 z = 0."""
    A = np.zeros((4, 4))
    A[0, 1] = 1.0
    A[1, 2] = 1.0
    A[2, 3] = 1.0
    A[3, 0] = -(w1 ** 2) * (w2 ** 2)
    A[3, 2] = -(w1 ** 2 + w2 ** 2)
    return A


def geo_mult(A, lam, tol=1e-8):
    s = np.linalg.svd(A - lam * np.eye(A.shape[0]), compute_uv=False)
    return int(sum(1 for x in s if x < tol * max(1.0, s[0])))


A_neq = pu_mode_matrix(1.9, 1.1)
ev_neq = np.linalg.eigvals(A_neq)
diag_neq = all(geo_mult(A_neq, l) == 1 for l in ev_neq)
A_eq = pu_mode_matrix(1.5, 1.5)
gm_eq = geo_mult(A_eq, 1.5j)
check("T", "PU anchor: mode matrix diagonalizable at w1 != w2 (eigenvalues "
           "+/-i w1, +/-i w2 simple); DEFECTIVE at w1 = w2 (geometric mult 1 "
           "vs algebraic 2 -- the t e^{iwt} Jordan form, 2104.03708 eq 7.9)",
      diag_neq and gm_eq == 1,
      f"equal-freq geometric multiplicity = {gm_eq} (algebraic 2)")


def alpha_pu(dw, w0=1.5):
    w1, w2 = w0 + dw / 2, w0 - dw / 2
    return np.log((w1 + w2) / (w1 - w2)) / (w1 * w2)


dws = (0.8, 0.4, 0.1, 0.01, 1e-4, 1e-8)
avals = [alpha_pu(dw) for dw in dws]
print("      alpha = log((w1+w2)/(w1-w2))/(w1 w2)  [2104.03708 eq 5.7]:")
print("      " + ", ".join(f"dw={dw:g}: {a:.3f}" for dw, a in zip(dws, avals)))
check("T", "PU anchor: the Q/V-determination coefficient alpha grows without "
           "bound (log-divergent) as w1 -> w2 -- V = e^-Q singular at the "
           "degeneracy (2004.00376 Sec IV: 'e^-Q becomes singular when the "
           "energies become equal')",
      all(b > a for a, b in zip(avals, avals[1:])) and avals[-1] / avals[0] > 8)

# =============================================================================
print()
print("=" * 78)
print("PART 1  the build: interacting C on gu's structure, NON-degenerate")
print("=" * 78)

C_int, info = bm_c_operator(H, B)
Pi = info["Pi"]
pair_modes = [w_vec(i, s) for i in range(3) for s in (+1, -1)]
kin = np.diag([+1.0, -1.0] * 3)                       # kinematic K-grading

check("E", "(a) sector split: 7 real-spectrum matter states (transverse + 3 "
           "record pairs) and 2 complex-conjugate gauge states (Mannheim's "
           "third realization, removed by the graded quotient); the two "
           "3-fold cross-pair degeneracies are K-DEFINITE (benign, "
           "parity-non-mixing -- R1's load-bearing qualifier exercised)",
      info["n_real"] == 7 and info["n_complex"] == 2
      and info["min_abs_nu"] > 0.5,
      f"{info['n_real']} real + {info['n_complex']} complex; "
      f"min |nu| = {info['min_abs_nu']:.3f}")

c2 = np.linalg.norm(C_int @ C_int - Pi)
comm = np.linalg.norm(C_int @ H - H @ C_int)
G = B @ C_int
G = 0.5 * (G + G.conj().T)
evG = np.linalg.eigvalsh(G)
n_pos = int((evG > 1e-9).sum())
pseudoH = np.linalg.norm(G @ H - H.conj().T @ G)
check("E", "(a) C^2 = Pi, [C, H] = 0, G = B.C Hermitian positive of rank 7 "
           "on the sector, G H = H^dag G -- the interacting V-metric "
           "(V H V^-1 = H^dag with POSITIVE norm, 2104.03708 eq 1.4 + Sec V) "
           "exists and is dynamically determined on gu's structure",
      c2 < 1e-7 and comm < 1e-7 and evG.min() > -1e-9 and n_pos == 7
      and pseudoH < 1e-7,
      f"||C^2-Pi|| {c2:.1e}, ||[C,H]|| {comm:.1e}, rank(G) = {n_pos}, "
      f"||GH - H^dag G|| {pseudoH:.1e}")

Z = RNG.standard_normal((DIM, DIM)) + 1j * RNG.standard_normal((DIM, DIM))
Z = 0.5 * (Z + B @ Z.conj().T @ B)                    # B-pseudo-Hermitian (B^2 = I)
Z = 1e-6 * Z / np.linalg.norm(Z)
C_pert, _ = bm_c_operator(H + Z, B)
stab = np.linalg.norm(C_pert - C_int)
G_neg = B @ (-C_int)
G_neg = 0.5 * (G_neg + G_neg.conj().T)
neg_inadmissible = np.linalg.eigvalsh(G_neg).min() < -0.5
check("E", "(a) determination: C stable under O(1e-6) pseudo-Hermitian "
           "perturbation; global flip -C INADMISSIBLE (B.(-C) negative) -- "
           "given the anchor B the recipe has NO residual sign freedom",
      stab < 1e-3 and neg_inadmissible,
      f"||dC|| = {stab:.1e} under 1e-6 perturbation")

# (b) C grades records; identifiability with the kinematic orientation
C_pair = c_on_pairs(C_int, B, pair_modes)
ident = np.linalg.norm(C_pair - kin)
cg = [float((w_vec(i, s).conj() @ B @ C_int @ w_vec(i, s)).real) /
      float((w_vec(i, s).conj() @ B @ w_vec(i, s)).real)
      for i in range(3) for s in (+1, -1)]
check("E", "(b) C grades the records: record modes w(i,+sigma*) C-positive, "
           "mirrors C-negative, and C restricted to the record pairs EQUALS "
           "the kinematic K-grading EXACTLY with the causality coupling ON "
           "(the coupling dresses toward the quotiented gauge sector, not "
           "across the pairs) -- the interacting C is IDENTIFIABLE with the "
           "kinematic orientation: the audit's watched second anchor freedom "
           "does NOT appear",
      ident < 1e-7 and all(abs(cg[2 * i] - 1) < 1e-7 for i in range(3))
      and all(abs(cg[2 * i + 1] + 1) < 1e-7 for i in range(3)),
      f"||C|pairs - kin|| = {ident:.1e}, grades {[round(x, 3) for x in cg]}")

# register direction on C-confined draws; anchor co-flip at interacting grade
Pi_plus = 0.5 * (Pi + C_int)
ok_reg = True
for _ in range(200):
    z = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
    psi = Pi_plus @ z
    psi = psi / np.linalg.norm(psi)
    q = float((psi.conj() @ B @ psi).real)
    ok_reg = ok_reg and q > 1e-10
    ok_reg = ok_reg and np.sign(record_register([q] * 5, +1)[-1]) == +1
C_flip, _ = bm_c_operator(H, -B)
coflip = np.linalg.norm(C_flip + C_int)
psi = Pi_plus @ (RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM))
psi /= np.linalg.norm(psi)
q_m = float((psi.conj() @ (-B) @ psi).real)           # renamed-anchor charge
check("E", "(b) register direction = eps on 200 C-confined draws (q > 0, "
           "direction +1); anchor flip B -> -B yields C -> -C exactly -- "
           "sector selection and record direction CO-FLIP; the one Z/2 is "
           "the joint anchor naming (payload item 1), not a second bit",
      ok_reg and coflip < 1e-7 and q_m < 0,
      f"||C(-B) + C(B)|| = {coflip:.1e}")

refuse = all(float((w.conj() @ B @ C_int @ w).real) /
             float((w.conj() @ B @ w).real) < -0.5
             for w in (w_vec(i, -SIGMA_STAR) for i in range(3)))
check("E", "(b) refusal: the wrong-orientation candidate record modes are "
           "graded NEGATIVE by the interacting C -- a wrong-bit record "
           "sector is not C-positive-confinable (the toy Q6 failure, now at "
           "interacting grade)",
      refuse)

# record drive: weak drive dresses; the toy part-D strength PT-breaks
H_wd = build_H(B, drive=0.03)
C_wd, info_wd = bm_c_operator(H_wd, B)
ident_wd = np.linalg.norm(c_on_pairs(C_wd, B, pair_modes) - kin)
check("E", "(b) a WEAK record drive (lam = 0.03, below the PT threshold of "
           "the cross-norm near-resonance) keeps all 7 matter states real "
           "and only dresses the grading -- records stay C-graded under "
           "driving",
      info_wd["n_real"] == 7 and ident_wd < 0.2,
      f"{info_wd['n_real']} real; ||C|pairs - kin|| = {ident_wd:.3f}")

H_od = build_H(B, drive=LAM_D)
ev_od = np.linalg.eigvals(H_od)
n_real_od = sum(1 for x in ev_od if abs(x.imag) < 1e-8)
broken = [x for x in ev_od if 1e-3 < abs(x.imag) < 0.5]
check("E", "(b) NAMED FINDING: at the toy part-D drive strength (lam = 0.15) "
           "the near-resonant cross-norm pair (transverse E = 1.0, K = +1 vs "
           "mirror w1- E = 1.1, K = -1) goes COMPLEX -- PT breaks, those "
           "eigenvectors are K-null, and C-determination fails for that pair "
           "(Mannheim's realization 3 on gu's fixture): an overdriven record "
           "register has NO definite grade; interaction-grade record drives "
           "carry a PT-unbroken-ness condition",
      n_real_od == 5 and len(broken) == 2,
      f"{n_real_od} real; broken pair at "
      f"{np.round(sorted(broken, key=lambda z: z.imag)[-1], 4)} and conj")

C_bad, _ = bm_c_operator(H, -B)                       # recipe slot fed -B
anti = np.linalg.norm(c_on_pairs(C_bad, B, pair_modes) + kin)
check("F", "(c) SRC-COH-1 control: recipe fed -B while the register keeps B "
           "anti-aligns the grading EXACTLY (C|pairs = -kinematic) -- a "
           "relative form sign between slots is the Da3/mu-import shape, one "
           "paid Z/2, exactly what the one-form rule forbids",
      anti < 1e-7, f"||C_bad|pairs + kin|| = {anti:.1e}")

# =============================================================================
print()
print("=" * 78)
print("PART 2  the degeneracy check: gu's vacuum anchors (delta -> 0)")
print("=" * 78)

H_deg = build_H(B, delta=0.0, cpl=0.0, drive=0.0)

gm = geo_mult(H_deg, MU)
check("E", "degeneracy shape: at delta = 0 the eigenvalue mu has geometric "
           "multiplicity 6 = algebraic 6 (three K-balanced hyperbolic pairs) "
           "-- gu's vacuum-anchor degeneracy is DIAGONALIZABLE and "
           "sign-blind, NOT the PU equal-frequency Jordan form",
      gm == 6, f"geometric mult = {gm}")

try:
    bm_c_operator(H_deg, B)
    recipe_failed, msg = False, "recipe unexpectedly succeeded"
except ValueError as exc:
    recipe_failed, msg = True, str(exc)
check("E", "C-determination FAILS at the degeneracy: the mu-eigengroup Krein "
           "Gram is K-INDEFINITE (signature (+3,-3)), sign(nu) is "
           "basis-dependent, the recipe aborts -- dynamics does not "
           "determine C at gu's vacuum anchors",
      recipe_failed, msg)

C_swap = np.zeros((DIM, DIM), dtype=complex)          # canonical grading
for i in range(3):
    C_swap[3 + i, 6 + i] = C_swap[6 + i, 3 + i] = 1.0
Pi_pairs = np.zeros((DIM, DIM), dtype=complex)
for i in range(3):
    Pi_pairs[3 + i, 3 + i] = Pi_pairs[6 + i, 6 + i] = 1.0


def boost(s):
    T = np.eye(DIM, dtype=complex)
    for i in range(3):
        T[3 + i, 3 + i] = np.exp(s)
        T[6 + i, 6 + i] = np.exp(-s)
    return T


cont_ok, dists = True, []
for s in (0.0, 0.4, 0.9):
    T = boost(s)
    Cs = T @ C_swap @ np.linalg.inv(T)
    isom = np.linalg.norm(T.conj().T @ B @ T - B)     # K-isometry
    c2s = np.linalg.norm(Cs @ Cs - Pi_pairs)
    comms = np.linalg.norm(Cs @ H_deg - H_deg @ Cs)
    Gs = B @ Cs
    Gs = 0.5 * (Gs + Gs.conj().T)
    evs = np.linalg.eigvalsh(Gs)
    pos = int((evs > 1e-9).sum()) == 6 and evs.min() > -1e-9
    cont_ok = cont_ok and isom < TOL and c2s < TOL and comms < TOL and pos
    dists.append(float(np.linalg.norm(Cs - C_swap)))
check("E", "the continuum: every hyperbolic boost of the canonical C is "
           "ADMISSIBLE at delta = 0 (C_s^2 = Pi, [C_s, H] = 0, B.C_s >= 0 "
           "with rank 6) -- admissible C's EXIST but form a continuum; "
           "dynamics selects none (the R1-verifier non-uniqueness, exhibited "
           "on gu's structure)",
      cont_ok, f"||C_s - C_0|| = {[round(d, 3) for d in dists]}")

G_msw = B @ (-C_swap)
G_msw = 0.5 * (G_msw + G_msw.conj().T)
check("E", "the completion datum is the anchor bit itself: -C_swap with B is "
           "INADMISSIBLE (B.(-C_swap) negative on the pairs) -- within the "
           "Z/2-typed payload family the choice set is exactly {(B, C), "
           "(-B, -C)}: what dynamics fails to supply at the degeneracy is "
           "eps, the external Z/2, and nothing larger of Z/2 type",
      np.linalg.eigvalsh(G_msw).min() < -0.5)

H_gap = build_H(B, delta=DELTA0, cpl=0.0, drive=0.0)
defects = [float(np.linalg.norm(
    boost(s) @ C_swap @ np.linalg.inv(boost(s)) @ H_gap
    - H_gap @ boost(s) @ C_swap @ np.linalg.inv(boost(s))))
    for s in (0.4, 0.9)]
C_gap, _ = bm_c_operator(H_gap, B)
gap_ident = np.linalg.norm(C_gap @ Pi_pairs - C_swap)
check("F", "armed-falsification control: restoring the gap (delta != 0) "
           "KILLS the continuum ([C_s, H] != 0 for s != 0, growing with "
           "sinh(s)*delta) and the recipe reconverges to the canonical C -- "
           "dynamical determination is exactly the gapped-pair phenomenon; "
           "it fails at the exactly-degenerate anchors and NOT elsewhere. "
           "(Had C stayed determined at delta = 0, the external-bit result "
           "would break: it does not.)",
      all(d > 0.1 for d in defects) and gap_ident < 1e-7,
      f"[C_s,H] defects {[round(d, 3) for d in defects]}, "
      f"||C_gap|pairs - C_swap|| = {gap_ident:.1e}")

# carrier-level anchor: the so(9,5) Casimir on the verified 128-dim spinor
e = gb.gammas()
eta_diag = [1.0] * 9 + [-1.0] * 5
Cas = np.zeros((128, 128), dtype=complex)
for a in range(14):
    for b in range(a + 1, 14):
        Sab = 0.5 * (e[a] @ e[b])
        Cas += eta_diag[a] * eta_diag[b] * (Sab @ Sab)
lam0 = np.trace(Cas).real / 128
scal = np.linalg.norm(Cas - lam0 * np.eye(128)) / np.linalg.norm(Cas)
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
sigK = np.linalg.eigvalsh(0.5 * (K_S + K_S.conj().T))
balanced = int((sigK > 0).sum()) == 64 and int((sigK < 0).sum()) == 64
check("E", "carrier anchor: the so(9,5) Casimir on the verified Cl(9,5) "
           "spinor is a SCALAR (one exactly-degenerate eigenspace) and K_S "
           "has signature (+64,-64) -- gu's actual vacuum anchors are "
           "exactly degenerate and K-balanced under native Casimir-type "
           "dynamics: the delta = 0 fixture is the faithful miniature "
           "(triplet-sector enumeration: big-swing R3, sign-blind, "
           "SUSTAINED)",
      scal < 1e-12 and balanced,
      f"||Cas - lam I||/||Cas|| = {scal:.1e}, lam = {lam0:.4f}")

# =============================================================================
print()
nE = sum(1 for t, _, ok in RESULTS if t == "E" and ok)
nF = sum(1 for t, _, ok in RESULTS if t == "F" and ok)
nT = sum(1 for t, _, ok in RESULTS if t == "T" and ok)
fails = [(t, n) for t, n, ok in RESULTS if not ok]
print(f"headline: {nE} [E] + {nF} [F] = {nE + nF}  (setup [T] = {nT}, excluded)")
if fails:
    print("FAILURES:")
    for t, n in fails:
        print(f"  [{t}] {n}")
    sys.exit(1)
print("VERDICT: the interacting C-operator EXISTS and is dynamically "
      "determined on gu's structure wherever the record pairs are gapped; it "
      "grades records positive, refuses the wrong orientation, is "
      "identifiable with the kinematic K-grading (no second anchor freedom), "
      "and respects SRC-COH-1. At gu's exactly-degenerate vacuum anchors the "
      "structure is DIAGONALIZABLE sign-blind (not PU-Jordan) and "
      "C-determination FAILS by non-uniqueness (an admissible continuum); "
      "within the Z/2-typed payload family the undetermined datum is exactly "
      "the anchor eps -- the external Z/2 completing what dynamics cannot. "
      "The external-bit result STANDS.")
sys.exit(0)
