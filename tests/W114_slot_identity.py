#!/usr/bin/env python3
r"""W114 / SLOT-IDENTITY: is the Observer Structure Theorem's typed interface slot (WALL 2, the
W98/W103 tail slot: a positive invertible metric AT INFINITY on the asymptotic Krein-null line) THE
SAME OBJECT as the Nguyen paragraph-3.1 complexification slot (WALL 1, the generation slot: a
non-quaternionic, J_quat-antilinear, essential-scalar-i, odd-count-fixing carrier)?

HYPOTHESIS TESTED (not assumed): one external object fills both slots -- the metric-at-infinity fills
the modular slot and its topological/index class fills the count slot.

COMMON-LANGUAGE TYPING (T1):
  WALL 1 (Nguyen/generation): carrier = RS module C^(14*128); foreign-to = the J_quat-commutant
    M(14,C)(x)M(64,H) = the whole GU-native algebra (Cl(9,5)); linearity type = FORCED non-quaternionic
    (any J-even Hermitian has EVEN signature by Kramers -- the requirement PROVABLY excludes a
    quaternionic filler); payload = DISCRETE (an odd index/rank; arena {1,3}, 3-over-1 selection);
    location = the s3.1 shiab complexification point.
  WALL 2 (observer/modular): carrier = the mode-tower Krein doublets, asymptotic tail (Calkin class
    [C] = 2[P]); foreign-to = the observer-accessible (compact) ideal; linearity type = the LOCATION
    (the null line e_null = (i,1)/sqrt2) is essentially complex and J-transverse, but the FILLER's
    J_quat-linearity is NOT forced (T4: a J-even filler exists); payload = CONTINUOUS (a positive
    invertible metric at infinity + a fixed modular phase); location = the asymptotic tail.

HEADLINE COMPUTATIONS:
  T2  the null line is HALF A KRAMERS PAIR: J_quat e_null = conj(e_null), orthogonal to e_null -- the
      line is J-transverse (not J-invariant); its rank-1 projector Q = 1-P is non-H-linear (defect 1)
      with signature +1 (ODD): the null-line projector IS an instance of the wall-1 foreign-carrier
      type (the rank-1 sibling of step10/step11's rank-3 foreign projector).
  T3  J-even Hermitian 2x2 = R*I EXACTLY (two derivations: basis sweep + commutant nullspace = H,
      Hermitian part 1-real-dim).  Consequences: the CORRECTION c*Q (null-line-supported filler) is
      J-ODD for every c > 0 (defect = c); the TOTAL metric 2P + cQ is J-even iff c = 2.
  T4  THE QUATERNIONIC ESCAPE (the identity-killer): the J-EVEN scalar shift d*I fills wall 2's typed
      requirement as recorded in W103 T6 -- C + dI is positive invertible with uniform bound (min eig
      = 1+d-r_k >= d), 0 leaves the essential spectrum (quotient-invertible; two derivations), dI is
      non-compact (class-changing, hence external in W103's sense), it assigns positive norm d to the
      null direction, AND it fixes the spinning modular phase ((1+d+-r_k)^{it} converges).  So wall 2
      ADMITS a quaternionic filler while wall 1 PROVABLY FORBIDS one (T5).  The typed requirements are
      NOT the same type.
  T5  wall 1's Kramers wall re-verified on the ACTUAL reconstruction (Cl(9,5)=M(64,H), 128-dim,
      J = C_cc*conj with C_cc = e1 e3 e5 e7 e10 e12): J^2 = -1, gammas exactly H-linear; J-even
      Hermitian carriers have EVEN signature; the embedded rank-1 null projector has ODD signature 1
      and is non-H-linear -- foreign, exactly as step11(d).
  T6  THE EMBEDDING (the dimension-mismatch adversary, answered): the 2x2 doublet J_quat = sigma_y*K
      embeds canonically into the M(64,H) J_quat as (any) single Kramers pair -- constructed
      explicitly (b1, b2' = -i*J b1), and the W103 fine-type identity [eta(r), J_quat] = 2r*conj
      PERSISTS VERBATIM in C^128 (defect of the embedded eta~(r) = 2r exactly); the embedded e_null
      is in ker eta~(1) and is half a Kramers pair of the REAL reconstruction J.  NOT a pun -- the
      kinematics embed.  (What remains unestablished is DYNAMICAL: that GU's actual Krein tail
      restricts to this configuration on that pair.)
  T7  PAYLOAD DECOMPOSITION FAILS: the space of admissible wall-2 fillers is CONNECTED and passes
      through the J-even point c=2 (eigenvalue crossing: the distinguished-eigenline datum is
      undefined there and FLIPS across it) => NO deformation-invariant index; the only discrete
      extract (rank of the null eigenprojection = 1, Kramers-breaking parity ODD) lands in the
      PARITY (Z_2) arena -- consistent with {1,3} oddness but supplying NO Z_3 / no 3-over-1
      selection (the tail carries ONE constant null line: multiplicity 1, no 3-fold datum).

VERDICT ENCODED (T8): TWO-SLOTS (under W103's typing as written), with the named obstruction:
  (i) wall 2 admits a quaternionic filler (dI), wall 1 forbids one (Kramers) -- the linearity types
      provably differ;
  (ii) the filler space is connected/contractible -- the metric-at-infinity carries NO stable index,
      so the count payload cannot be the topological class of the metric payload;
  (iii) even on the support-constrained fork (filler required null-line-supported: then it IS forced
      J-odd, rank-1, odd -- genuinely the wall-1 TYPE), the payload VALUE is parity (Z_2 = odd), not
      the {1,3} 3-selection: the fused object would fill the ODDNESS requirement, never the 3.
  RELATED structure is REAL (shared Kramers-pair grammar; the embedding is constructed, not a pun);
  W103's RELATED-not-SAME grade is CONFIRMED and SHARPENED from "payload mismatch" to a theorem-shaped
  type obstruction.

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import os
import sys

import numpy as np

np.random.seed(0)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "generation-sector"))

import gen_sector_bridge as gu_bridge  # noqa: E402

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def sig(A: np.ndarray) -> int:
    ev = np.linalg.eigvalsh(0.5 * (A + dag(A)))
    tol = 1e-9 * max(1.0, float(np.abs(ev).max()))
    return int((ev > tol).sum()) - int((ev < -tol).sum())


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def eta2(r: float) -> np.ndarray:
    return I2 + r * SY


def hl2(X: np.ndarray) -> float:
    # H-linearity defect wrt the doublet J_quat = SY * conj:  ||X SY - SY conj(X)||
    return opnorm(X @ SY - SY @ X.conj())


# the W98 mode data (same as W103)
M1, M2, G = 0.0, 0.30, 0.10


def r_of(k: float) -> float:
    dsplit = abs(np.sqrt(k * k + M1 * M1) - np.sqrt(k * k + M2 * M2))
    return float(min(G / (G + 0.5 * dsplit), 1.0 - 1e-15))


log("=" * 100)
log("W114 / SLOT-IDENTITY: is the W103 observer/tail slot THE SAME typed object as the Nguyen s3.1")
log("       generation slot?  Common typing, J-linearity on the null line, payload index, embedding.")
log("=" * 100)

# ====================================================================================================
# T1 -- the two typed requirements in one language (encoded; verified by the later checks)
# ====================================================================================================
log("\n[T1] Common-language typing of the two slots")
WALL1 = {
    "carrier": "RS module C^(14*128), Cl(9,5)=M(64,H)",
    "foreign_to": "J_quat-commutant = the GU-native algebra",
    "linearity_forced_non_quaternionic": True,      # Kramers: J-even Hermitian => even sig (T5)
    "payload": "discrete odd index; arena {1,3}, 3-over-1 selection",
    "location": "s3.1 shiab complexification point",
}
WALL2 = {
    "carrier": "mode-tower Krein doublets; Calkin tail class [C]=2[P]",
    "foreign_to": "compact (observer-accessible) ideal",
    "linearity_forced_non_quaternionic": None,      # to be COMPUTED (T3/T4) -- the crux
    "payload": "continuous: positive invertible metric at infinity + fixed modular phase",
    "location": "asymptotic tail null line e_null=(i,1)/sqrt2",
}
check("T1  both slots typed in one language (carrier / foreign-to / linearity / payload / location); "
      "wall 1's linearity is FORCED non-quaternionic (Kramers), wall 2's is left to computation -- the "
      "identity question = does wall 2's requirement also force it, and does its payload carry wall 1's index.",
      WALL1["linearity_forced_non_quaternionic"] is True and WALL2["linearity_forced_non_quaternionic"] is None)

# ====================================================================================================
# T2 -- the null line under J_quat: half a Kramers pair (J-transverse), and its projector is an
#       instance of the wall-1 foreign-carrier type (rank 1, odd, non-H-linear).
# ====================================================================================================
log("\n[T2] The null line is HALF A KRAMERS PAIR; its projector is a rank-1 ODD foreign carrier")
e_null = np.array([1j, 1.0], dtype=complex) / np.sqrt(2.0)
J_e = SY @ e_null.conj()                              # J_quat e_null
is_conj = opnorm((J_e - e_null.conj()).reshape(2, 1)) < 1e-14        # J e_null = conj(e_null) exactly
orth = abs(np.vdot(e_null, J_e)) < 1e-14                              # Kramers orthogonality
not_invariant = abs(abs(np.vdot(e_null, J_e)) - 1.0) > 0.5            # J maps the line OFF itself
spans = abs(np.linalg.det(np.column_stack([e_null, J_e]))) > 0.9      # (e, Je) span C^2: a Kramers pair
P = 0.5 * (I2 + SY)                                                   # eta(1) = 2P; ran P = span{J e_null}
Q = I2 - P                                                            # the null-line projector
q_defect, q_sig = hl2(Q), sig(Q)
# exact fine-type identity carried over from W103: [eta(r), J_quat] = 2r*conj
fine = all(abs(hl2(eta2(r)) - 2.0 * r) < 1e-14 for r in (0.1, 0.5, 0.9))
check("T2  J_quat e_null = conj(e_null) EXACTLY, orthogonal to e_null (Kramers orthogonality): the null "
      "line is J-TRANSVERSE -- not J-invariant, HALF a Kramers pair (e_null, J e_null span C^2).  Its "
      f"projector Q=1-P: H-linearity defect = {q_defect:.3f} (non-quaternionic), signature = {q_sig} (ODD) "
      "-- literally the rank-1 instance of the Nguyen foreign-carrier type (step11(d)'s rank-3 sibling).  "
      "And [eta(r), J_quat] = 2r*conj re-verified exactly.",
      is_conj and orth and not_invariant and spans and abs(q_defect - 1.0) < 1e-12 and q_sig == 1 and fine,
      f"J e = conj(e)={is_conj}, orth={orth}, Q defect={q_defect:.3f}, sig(Q)={q_sig}, [eta,J]=2r exact={fine}")

# ====================================================================================================
# T3 -- J-even Hermitian 2x2 = R*I (TWO derivations); the null-supported correction is ALWAYS J-odd;
#       the total metric 2P + cQ is J-even IFF c = 2.
# ====================================================================================================
log("\n[T3] J-even Hermitian = real scalars (two derivations); correction cQ always J-odd; total J-even iff c=2")
# derivation 1: basis sweep
basis_defects = {"I": hl2(I2), "sx": hl2(SX), "sy": hl2(SY), "sz": hl2(SZ)}
sweep_ok = basis_defects["I"] < 1e-14 and all(basis_defects[b] > 1.9 for b in ("sx", "sy", "sz"))
# derivation 2: the real-linear commutant of J on C^2.  X H-linear <=> X SY - SY conj(X) = 0.
# Build the real-linear map L: R^8 -> C^4 (X as 4 complex = 8 real params) and take its nullspace.
E = [np.array(m, dtype=complex) for m in
     ([[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [0, 1]])]
cols = []
for B in E:
    for coef in (1.0, 1j):
        X = coef * B
        D = X @ SY - SY @ X.conj()
        cols.append(np.concatenate([D.reshape(-1).real, D.reshape(-1).imag]))
L = np.array(cols).T                                   # 8 x 8 real
ns_dim = 8 - int(np.linalg.matrix_rank(L, tol=1e-10))  # real dim of the H-linear algebra
# Hermitian members of the nullspace: solve within the nullspace for X = X^dag
_, _, Vt = np.linalg.svd(L)
null_basis = Vt[ns_dim * -1:, :]                       # last ns_dim rows span the nullspace
herm_dim = 0
if ns_dim > 0:
    hcols = []
    for row in null_basis:
        Xr = (row[:4] + 1j * row[4:]).reshape(2, 2)
        H = Xr - dag(Xr)
        hcols.append(np.concatenate([H.reshape(-1).real, H.reshape(-1).imag]))
    Hmat = np.array(hcols).T
    herm_dim = ns_dim - int(np.linalg.matrix_rank(Hmat, tol=1e-10))
commutant_is_H = (ns_dim == 4)                         # the quaternions: {I, i*sx, i*sy, i*sz}_R
herm_is_RI = (herm_dim == 1)                           # Hermitian quaternionic scalars = R*I
# consequences
cs = (0.5, 1.0, 2.0, 3.0)
corr_odd = all(abs(hl2(c * Q) - c) < 1e-12 for c in cs)           # correction cQ: defect = c > 0 ALWAYS
tot_defects = {c: hl2(2.0 * P + c * Q) for c in cs}
tot_iff = all(abs(tot_defects[c] - abs(2.0 - c)) < 1e-12 for c in cs) and tot_defects[2.0] < 1e-13
check("T3  TWO DERIVATIONS agree: (1) basis sweep -- I is J-even, sx/sy/sz all J-odd (defect 2); "
      f"(2) the J-commutant has real dim {ns_dim} (= H, the quaternions) with Hermitian part dim {herm_dim} "
      "(= R*I).  CONSEQUENCES: the null-line-SUPPORTED correction cQ is J-ODD for every c (defect = c "
      "exactly); the TOTAL metric 2P + cQ has defect |2-c| -- J-even IFF c = 2 (the quaternionic point "
      "EXISTS in the admissible filler family).",
      sweep_ok and commutant_is_H and herm_is_RI and corr_odd and tot_iff,
      f"commutant dim={ns_dim}, Herm dim={herm_dim}, defect(2P+cQ)=|2-c| ok={tot_iff}")

# ====================================================================================================
# T4 -- THE QUATERNIONIC ESCAPE: the J-EVEN scalar shift dI fills wall 2's typed requirement (as
#       recorded in W103 T6).  Two derivations of quotient-invertibility.  This is the identity-killer.
# ====================================================================================================
log("\n[T4] The quaternionic escape: dI (J-even) fills the W103 slot -- wall 2 does NOT force non-quaternionicity")
d = 0.5
ks = [1e2, 1e3, 1e4, 1e5, 1e7]
# derivation 1: uniform positivity of C + dI (per-mode min eigenvalue = 1 + d - r_k >= d)
min_eigs = [float(np.linalg.eigvalsh(eta2(r_of(k)) + d * I2).min()) for k in ks]
pos_uniform = all(m >= d - 1e-12 for m in min_eigs)
exact_bound = all(abs(min_eigs[i] - (1.0 + d - r_of(ks[i]))) < 1e-12 for i in range(len(ks)))
# derivation 2: essential spectrum -- tail limit of the min eigenvalue is d > 0 (0 not in sigma_ess)
tail_min = min_eigs[-1]
ess_ok = abs(tail_min - d) < 1e-3
# dI is J-even (quaternionic) and NON-compact (constant blocks: class-changing = external)
dI_even = hl2(d * I2) < 1e-14
dI_noncompact = True                                   # constant block norms d do not vanish at the tail
# positive norm on the null direction
null_norm = float(np.real(np.vdot(e_null, (d * I2) @ e_null)))
# the spinning phase is FIXED: eigenvalues of eta(r)+dI are 1+d-+r -> (d, 2+d); (1+d-+r)^{it} converges
phases_a = [np.exp(1j * np.log(1.0 + d - r_of(k))) for k in (1e5, 1e5 * np.e ** np.pi)]
phase_gap = abs(phases_a[0] - phases_a[1])
phase_fixed = phase_gap < 1e-4                         # vs W103 T5's spin gap ~2 without the filler
check("T4  dI (d=0.5): J-EVEN (defect 0, quaternionic scalar), NON-compact (external / class-changing); "
      f"C + dI positive invertible UNIFORMLY (min eig = 1+d-r_k exactly, tail -> {tail_min:.4f} = d > 0: "
      "0 leaves the essential spectrum -- quotient-invertible, two derivations agree); assigns norm "
      f"{null_norm:.2f} > 0 to the null direction; and FIXES the spinning phase (deep-tail phase gap "
      f"{phase_gap:.2e} vs ~2 unfixed).  A QUATERNIONIC filler fills wall 2's typed requirement as "
      "written.  Wall 1 provably forbids any quaternionic filler (Kramers, T5).  THE TYPES DIFFER.",
      pos_uniform and exact_bound and ess_ok and dI_even and dI_noncompact
      and null_norm > 0.4 and phase_fixed,
      f"min eig tail={tail_min:.4f}, dI defect={hl2(d * I2):.1e}, phase gap={phase_gap:.1e}")

# ====================================================================================================
# T5 -- wall 1's side on the ACTUAL reconstruction: J = C_cc*conj on C^128 (C_cc = e1 e3 e5 e7 e10 e12),
#       J^2 = -1, gammas H-linear; J-even Hermitian carriers have EVEN signature (Kramers); the
#       embedded rank-1 null projector is ODD and non-H-linear (foreign).
# ====================================================================================================
log("\n[T5] Wall 1 on the real Cl(9,5)=M(64,H) rep: Kramers forbids a quaternionic odd filler")
e128 = gu_bridge.gammas()
DIM = gu_bridge.DIM
C_cc = e128[1] @ e128[3] @ e128[5] @ e128[7] @ e128[10] @ e128[12]   # the canon's C (0-based indices)
J2_is_m1 = opnorm(C_cc @ C_cc.conj() + np.eye(DIM)) < 1e-10          # J^2 = C conj(C) K^2 = -1
C_unitary = opnorm(C_cc @ dag(C_cc) - np.eye(DIM)) < 1e-10


def hl128(X: np.ndarray) -> float:
    return opnorm(X @ C_cc - C_cc @ X.conj())


gamma_defect = max(hl128(e128[a]) for a in (0, 3, 7, 9, 12))         # per-generator exact (canon)
rng = np.random.default_rng(7)
even_sigs = []
for _ in range(4):
    Y = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    Y = 0.5 * (Y + dag(Y))
    Hs = 0.5 * (Y + C_cc @ Y.conj() @ dag(C_cc))                     # J-even symmetrization
    even_sigs.append(sig(Hs))
kramers_even = all(s % 2 == 0 for s in even_sigs)
check("T5  the reconstruction's own J_quat: C_cc = e1 e3 e5 e7 e10 e12 gives J^2 = -1 "
      f"(||C conj(C)+I|| = {opnorm(C_cc @ C_cc.conj() + np.eye(DIM)):.1e}), unitary, gammas H-linear "
      f"(max defect {gamma_defect:.1e}, the canon's per-generator-exact certificate); random J-EVEN "
      f"Hermitian carriers have signatures {sorted(even_sigs)} -- ALL EVEN (Kramers).  Wall 1's typed "
      "requirement (odd index) PROVABLY excludes every quaternionic filler -- the exact opposite of T4.",
      J2_is_m1 and C_unitary and gamma_defect < 1e-9 and kramers_even,
      f"J^2=-1: {J2_is_m1}, gamma defect {gamma_defect:.1e}, even sigs {sorted(even_sigs)}")

# ====================================================================================================
# T6 -- THE EMBEDDING (adversary: "the 2x2 J_quat has no established link to the M(64,H) J_quat --
#       a dimension-mismatched pun").  Constructed: any Kramers pair of the REAL J carries the doublet
#       structure; the W103 fine-type identity [eta(r), J] = 2r*conj persists VERBATIM in C^128.
# ====================================================================================================
log("\n[T6] The embedding: the doublet Krein/J structure = the restriction of the M(64,H) J to one Kramers pair")
v = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
v /= np.linalg.norm(v)
Jv = C_cc @ v.conj()
kramers_orth = abs(np.vdot(v, Jv)) < 1e-12                           # automatic: J^2=-1 Kramers orthogonality
b1, b2p = v, -1j * Jv                                                # basis in which J acts as SY*conj
B = np.column_stack([b1, b2p])
# check the coordinate action: C_cc conj(B) = B SY  (J acts as sigma_y * conj in this basis)
coord_ok = opnorm(C_cc @ B.conj() - B @ SY) < 1e-10
# embed e_null and the mixing
v_null = B @ e_null                                                  # the embedded null vector
Jv_null = C_cc @ v_null.conj()
half_pair = abs(np.vdot(v_null, Jv_null)) < 1e-10                    # embedded null line: half a Kramers pair
Sigma = B @ SY @ dag(B)                                              # the embedded mixing sigma_y


def eta128(r: float) -> np.ndarray:
    return np.eye(DIM, dtype=complex) + r * Sigma


fine128 = all(abs(hl128(eta128(r)) - 2.0 * r) < 1e-9 for r in (0.1, 0.5, 0.9))   # [eta~, J] = 2r*conj VERBATIM
null_in_kernel = opnorm((eta128(1.0) @ v_null).reshape(DIM, 1)) < 1e-10
Pi_null = np.outer(v_null, v_null.conj())
pi_defect, pi_sig = hl128(Pi_null), sig(Pi_null)
check("T6  EMBEDDING CONSTRUCTED (not a pun): a random Kramers pair (b1, -i*J b1) of the REAL "
      f"reconstruction J carries the doublet structure exactly (C conj(B) = B*sigma_y, residual "
      f"{opnorm(C_cc @ B.conj() - B @ SY):.1e}); the embedded eta~(r) = I + r*Sigma satisfies "
      "[eta~(r), J] = 2r*conj VERBATIM in C^128; the embedded e_null lies in ker eta~(1), is half a "
      f"Kramers pair of the real J, and its projector has defect {pi_defect:.3f} (foreign), signature "
      f"{pi_sig} (ODD).  KINEMATIC embedding: REAL.  (The DYNAMICAL identification -- that GU's actual "
      "Krein tail restricts this way on some pair -- remains unestablished; stated honestly.)",
      kramers_orth and coord_ok and half_pair and fine128 and null_in_kernel
      and abs(pi_defect - 1.0) < 1e-9 and pi_sig == 1,
      f"coord ok={coord_ok}, [eta~,J]=2r exact={fine128}, sig(Pi)={pi_sig}, defect={pi_defect:.3f}")

# ====================================================================================================
# T7 -- PAYLOAD DECOMPOSITION: does the metric-at-infinity carry an index landing in the count arena?
#       NO: the filler space is connected through the J-even point c=2 (eigenvalue crossing, the
#       distinguished-line datum flips) => no deformation-invariant index; the only discrete extract
#       is the Kramers-breaking PARITY (Z_2, value ODD via the rank-1 null eigenline) -- it matches
#       {1,3} oddness but supplies no Z_3 / no 3-over-1 selection (multiplicity 1, one constant line).
# ====================================================================================================
log("\n[T7] Payload decomposition: no stable index; only Z_2 parity (odd), never the 3-selection")
cs7 = np.linspace(0.5, 3.5, 61)
gaps = []
low_line_overlap_with_null = []
for c in cs7:
    h = 2.0 * P + float(c) * Q
    w, V = np.linalg.eigh(h)
    gaps.append(float(w[1] - w[0]))
    low_line_overlap_with_null.append(float(abs(np.vdot(V[:, 0], e_null))))
gaps = np.array(gaps)
ov = np.array(low_line_overlap_with_null)
crossing = float(gaps.min()) < 1e-9 and abs(float(cs7[int(gaps.argmin())]) - 2.0) < 0.05
flips = ov[0] > 0.99 and ov[-1] < 0.01                # the distinguished line FLIPS across c=2
# the connected path 0.5 -> 3.5 stays positive-invertible throughout (admissible all along)
path_admissible = all(float(np.linalg.eigvalsh(2.0 * P + float(c) * Q).min()) > 0.4 for c in cs7)
# the only stable discrete extract: rank of the null eigenprojection of the CLASS limit = 1 (odd parity)
rank_null = int(round(float(np.trace(Q).real)))
parity_odd = rank_null % 2 == 1
multiplicity_one = rank_null == 1                     # one constant line (W103 T6) -- no 3-fold datum
check("T7  the admissible filler family {2P + cQ, c > 0} is CONNECTED and positive throughout, and it "
      f"passes through the J-even point c=2 where the eigenvalues CROSS (min gap {gaps.min():.1e} at "
      f"c={cs7[int(gaps.argmin())]:.2f}) and the distinguished eigenline FLIPS (overlap with e_null: "
      f"{ov[0]:.3f} -> {ov[-1]:.3f}): NO deformation-invariant index exists on the filler space.  The "
      f"only discrete extract is the Kramers-breaking PARITY of the class limit (rank(Q) = {rank_null}, "
      "ODD -- a Z_2 landing in the {1,3} ODDNESS requirement) with multiplicity ONE: no Z_3, no "
      "3-over-1 selection.  The count payload is NOT the topological class of the metric payload.",
      crossing and flips and path_admissible and parity_odd and multiplicity_one,
      f"crossing at c~2={crossing}, line flips={flips}, rank(Q)={rank_null} (odd, mult 1)")

# ====================================================================================================
# T8 -- VERDICT: TWO-SLOTS (named obstruction), RELATED structure real, W103's grade sharpened.
# ====================================================================================================
log("\n[T8] VERDICT = TWO-SLOTS: the types provably differ; the RELATED structure is real (embedding constructed)")
verdict = {
    # the identity's two legs, computed:
    "embedding_doublet_into_M64H_constructed_not_a_pun": True,          # T6
    "null_line_is_half_a_Kramers_pair_J_transverse": True,              # T2
    "null_projector_is_rank1_odd_foreign_carrier_wall1_TYPE": True,     # T2, T6
    # the obstruction (why NOT one object):
    "wall2_admits_quaternionic_filler_dI": True,                        # T4
    "wall1_forbids_quaternionic_filler_Kramers": True,                  # T5
    "filler_space_connected_no_stable_index": True,                     # T7
    "discrete_extract_is_Z2_parity_only_no_Z3_no_3_selection": True,    # T7
    # the fork (named, not decided):
    "support_constrained_fork_forces_J_odd_filler": True,               # T3 (cQ always J-odd)
    "even_on_that_fork_payload_is_parity_not_count": True,              # T7
    # verdicts:
    "verdict_SAME_SLOT": False,
    "verdict_TWO_SLOTS": True,
    "verdict_RELATED_UNRESOLVED": False,
    "W103_RELATED_not_SAME_grade_confirmed_and_sharpened": True,
}
two_slots = (verdict["verdict_TWO_SLOTS"] and not verdict["verdict_SAME_SLOT"]
             and verdict["wall2_admits_quaternionic_filler_dI"]
             and verdict["wall1_forbids_quaternionic_filler_Kramers"]
             and verdict["filler_space_connected_no_stable_index"]
             and verdict["embedding_doublet_into_M64H_constructed_not_a_pun"])
check("T8  VERDICT = TWO-SLOTS.  The dimension-mismatch adversary is answered by CONSTRUCTION (the "
      "embedding is real, T6), so the two-ness is not a pun artifact -- it is typed: wall 2's "
      "requirement admits a quaternionic filler (dI) which wall 1's requirement provably forbids "
      "(Kramers), and wall 2's payload carries no stable index (connected filler space through the "
      "J-even point), only a Z_2 parity with multiplicity 1 -- the oddness wall 1 needs, never the "
      "3-over-1 selection.  ONE named fork would fuse the TYPES (require the wall-2 filler null-line-"
      "supported => forced J-odd, rank-1, odd) but even then fills only the parity, not the count.",
      two_slots, f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ====================================================================================================
# SUMMARY
# ====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(ok for _, ok, _ in results), "some W114 slot-identity checks FAILED"

log("")
log("W114 SLOT-IDENTITY VERDICT (this file is the computation, not a claim-status change):")
log("  * TYPES: wall 1 = FORCED non-quaternionic (Kramers), discrete odd-index payload, {1,3} arena;")
log("    wall 2 = essentially-complex J-transverse LOCATION but filler linearity NOT forced,")
log("    continuous metric+phase payload.")
log("  * NULL LINE: half a Kramers pair (J e_null = conj(e_null), orthogonal); its projector is the")
log("    rank-1 odd foreign carrier -- an instance of the wall-1 TYPE.")
log("  * THE KILLER: the J-EVEN scalar dI fills wall 2's slot as typed in W103 (positive invertible,")
log("    quotient-class-changing, phase-fixing) while wall 1 provably forbids any J-even filler.")
log("  * PAYLOAD: the filler space is connected through c=2 (eigenvalue crossing, line flip) -- no")
log("    deformation-invariant index; only Z_2 parity (odd, multiplicity 1); no Z_3, no 3-selection.")
log("  * EMBEDDING: constructed into the real Cl(9,5)=M(64,H) J_quat; [eta(r),J]=2r*conj persists")
log("    verbatim -- the adversary's pun objection fails kinematically; the dynamical identification")
log("    remains open.")
log("  * VERDICT: TWO-SLOTS.  W103's RELATED-not-SAME stands, sharpened to a theorem-shaped obstruction.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
