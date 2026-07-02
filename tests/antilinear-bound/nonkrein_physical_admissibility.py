#!/usr/bin/env python3
"""
WC-ANTILINEAR-BOUND, addendum for reviewer point #2 ("the delimited Krein class S
still leaves loopholes -- could an operator evade S while still acting on the
physical chiral sector?").

ANSWER (computed grade, finite-dimensional kinematics): the admissible class is
STRICTLY BROADER than the Krein-compatible S, and the index-nullity theorem holds
on ALL of it.  The index-nullity proof never used the full Krein condition
M^dag K M = lambda K-bar.  It used ONE fact: the re-graded chirality eigenspaces
C(W_+), C(W_-) are K-ISOTROPIC (K-null / Lagrangian).  That is the intrinsic mark
of a *chirality* re-grading: the ORIGINAL chirality Gamma_c already has K-NULL
eigenspaces W_+/- (K is purely cross-chirality -- it pairs W_+ with W_-).  A
re-grading "of the same kind" (a chirality) must likewise have K-null eigenspaces.
Call that class

    P_iso := { antilinear C = M . conj :  C(W_+), C(W_-) are K-isotropic }  ⊇  S.

Then for ANY physical (maximal K-positive) subspace P and ANY C in P_iso:
P meets the K-null spaces C(W_+/-) only at 0, so the net re-graded chiral index
chi_C(P) = dim(P^C(W_+)) - dim(P^C(W_-)) = 0 - 0 = 0.  No Krein condition needed.

Certified below on the explicit Cl(9,5) 192-dim carrier:
  (B) P_iso STRICTLY contains S.  We build antilinear operators whose re-graded
      chirality eigenspaces are an arbitrary complementary pair of K-Lagrangians
      (the Lagrangian Grassmannian -- vastly larger than the S-orbit).  These have
      Krein residual of order 1 (NOT in S) yet K-isotropic re-graded eigenspaces
      (a bona fide chirality re-grading).  So "acts on physical chirality" does not
      require Krein-compatibility.
  (C) INDEX NULLITY on P_iso: every such non-Krein operator still gives chi_C(P)=0
      on every physical subspace, as exact integer ranks.  The reviewer's escape
      (evade S, still supply a chirality) is INHABITED and still forces nothing.
  (D) THE BOUNDARY IS THE NULL CONDITION, and it is load-bearing.  A re-grading
      whose eigenspaces are K-DEFINITE (not null) -- e.g. eigenspaces = the
      K-positive / K-negative subspaces -- is NOT a chirality: it grades physical
      vs ghost norm.  It DOES carry +-96 (the paper's vectorlike count), which is
      exactly why the null hypothesis (isotropy) is the real content, not scenery.
      Such an operator also fails to act on the physical sector (it maps a physical
      subspace to a K-indefinite image).

HONEST RESIDUAL (unchanged): finite-dimensional kinematics on the explicit carrier.
A genuine QFT effective / non-perturbative operator lives in the function-space
setting, where "physical / K-definite subspace" and the chirality grading are
subtler -- the separate open card WC-FUNCTION-SPACE-EXT, NOT closed here.  What #2
asked at the kinematic level is answered: the admissible class is the null-eigenspace
class P_iso (>> S), and index nullity holds on all of it.

Deterministic, numpy-only.  A nonzero chi_C on any P_iso operator fires the FAILURE
CONDITION and aborts.
"""
import time
import numpy as np
from itertools import combinations

T0 = time.time()
N, DIM = 14, 128
SEED = 20260704
TIMELIKE = {4, 5, 6, 7, 8}
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


# ------------------------------------------------------------- substrate + carrier (as bound script)
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


print("=" * 98)
print("WC-ANTILINEAR-BOUND #2 addendum: carrier + premises")
print("=" * 98)
base = jw(7)
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
      for (a, b, c, d), S in zip(SD, Sig)]
Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
Cas = 0.5 * (Cas + Cas.conj().T)
cw, cV = np.linalg.eigh(Cas)
W = cV[:, np.abs(cw - cw.max()) < 1e-6]
check(abs(cw.max() - 8.0) < 1e-9 and W.shape[1] == 192, "carrier j=1 Casimir-8, dim 192")

om = I128.copy()
for a in range(N):
    om = om @ e[a]
om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
Gc = W.conj().T @ np.kron(I4, om) @ W
Gc = 0.5 * (Gc + Gc.conj().T)
gev, gV = np.linalg.eigh(Gc)
check(int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96, "chirality split 96/96")
P0 = gV[:, gev > 0.5]                                   # W_+ basis (192 x 96)
N0 = gV[:, gev < -0.5]                                  # W_- basis (192 x 96)

spacelike = [a for a in range(N) if a not in TIMELIKE]
bS = I128.copy()
for s in spacelike:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
Kc = W.conj().T @ np.kron(I4, bS) @ W
Kc = 0.5 * (Kc + Kc.conj().T)
Kb = Kc.conj()
kev2, kVv = np.linalg.eigh(Kc)
check(int((kev2 > 1e-8).sum()) == 96 and int((kev2 < -1e-8).sum()) == 96, "K signature (96,96)")
check(np.linalg.norm(Kc @ Kc - np.eye(192)) < 1e-10, "K^2 = I")
check(np.linalg.norm(Kc @ Gc + Gc @ Kc) < 1e-10, "K Gamma_c = -Gamma_c K (chirality eigenspaces K-null)")
check(np.linalg.norm(P0.conj().T @ Kc @ P0) < 1e-10, "W_+ K-isotropic (original chirality is null-graded)")
check(np.linalg.norm(N0.conj().T @ Kc @ N0) < 1e-10, "W_- K-isotropic")
Pphys = kVv[:, kev2 > 1e-8]                             # a maximal K-positive (physical) subspace
Nphys = kVv[:, kev2 < -1e-8]                            # a maximal K-negative subspace


def rank_gap(A, tol=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    r = int((s > tol * s.max()).sum())
    return r, ((s[r - 1] / s[r]) if r < len(s) else np.inf)


def krein_residual(M):
    KM = M.conj().T @ Kc @ M
    lam = (np.vdot(Kb, KM) / np.vdot(Kb, Kb)).real
    return np.linalg.norm(KM - lam * Kb) / max(np.linalg.norm(KM), 1e-30)


def images(M):
    """the re-graded chirality eigenspaces C(W_+) = M conj(W_+), C(W_-) = M conj(W_-)."""
    return M @ P0.conj(), M @ N0.conj()


def image_isotropy(M):
    Wp, Wm = images(M)
    s = np.linalg.norm(M) ** 2 / 192
    return max(np.linalg.norm(Wp.conj().T @ Kc @ Wp),
               np.linalg.norm(Wm.conj().T @ Kc @ Wm)) / s


def chi_on_physical(Wp, Wm):
    """paper's index: dim(P ^ E_+) - dim(P ^ E_-) over physical P (exact integers)."""
    out = []
    for P in phys_list:
        r1, _ = rank_gap(np.hstack([P, Wp]))
        r2, _ = rank_gap(np.hstack([P, Wm]))
        out.append((192 - r1) - (192 - r2))
    return out


def expm_ss(X):
    k = max(0, int(np.ceil(np.log2(max(1e-16, np.linalg.norm(X, 2))))) + 2)
    Y, E, T = X / (2 ** k), np.eye(X.shape[0], dtype=complex), np.eye(X.shape[0], dtype=complex)
    for n in range(1, 18):
        T = T @ Y / n
        E = E + T
    for _ in range(k):
        E = E @ E
    return E


phys_list = [Pphys]
for _ in range(3):
    H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
    H = 0.4 * (H - H.conj().T) / np.linalg.norm(H)
    phys_list.append(expm_ss(Kc @ H) @ Pphys)
for j, P in enumerate(phys_list):
    check(np.linalg.eigvalsh(P.conj().T @ Kc @ P).min() > 1e-6, f"P{j} K-positive-definite")

# Lagrangian pairing basis: graphs of anti-Hermitian U are exactly the K-Lagrangians
Gpair = P0.conj().T @ Kc @ N0
Q = np.hstack([P0, N0 @ np.linalg.inv(Gpair)])
Xh = np.zeros((192, 192), dtype=complex)
Xh[:96, 96:] = np.eye(96)
Xh[96:, :96] = np.eye(96)
check(np.linalg.norm(Q.conj().T @ Kc @ Q - Xh) < 1e-9, "Lagrangian pairing basis Q^dag K Q = X")
Qc_inv = np.linalg.inv(np.hstack([P0.conj(), N0.conj()]))   # inv[conj(W_+), conj(W_-)]


def lagrangian(U):
    return Q @ np.vstack([np.eye(96), U])                    # K-Lagrangian iff U anti-Hermitian


def anti_herm():
    A = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
    return 0.5 * (A - A.conj().T)


# =============================================== PART B: P_iso is STRICTLY bigger than S
print("\n" + "=" * 98)
print("PART B -- non-Krein operators that STILL supply a chirality re-grading (P_iso \\ S)")
print("=" * 98)
iso_ops = []
for j in range(5):
    Lp, Lm = lagrangian(anti_herm()), lagrangian(anti_herm())      # complementary K-Lagrangians
    check(rank_gap(np.hstack([Lp, Lm]))[0] == 192, f"L+/L- complementary (op {j})")
    # antilinear C = M.conj with C(W_+) = L+, C(W_-) = L-
    M = np.hstack([Lp, Lm]) @ Qc_inv
    kr, iso = krein_residual(M), image_isotropy(M)
    print(f"  op {j}: Krein residual = {kr:.3f} (order 1 => NOT in S); "
          f"re-graded eigenspaces K-isotropy = {iso:.2e} (=> a bona fide chirality re-grading)")
    check(kr > 0.3, f"op {j}: genuinely non-Krein (outside S)")
    check(iso < 1e-8, f"op {j}: re-graded chirality eigenspaces are K-null (in P_iso)")
    iso_ops.append((f"P_iso#{j}", M))
print("  => a chirality re-grading (K-null eigenspaces) need NOT be Krein-compatible:")
print("     P_iso strictly contains S (the Lagrangian Grassmannian >> the S-orbit).")

# ============================================= PART C: INDEX NULLITY holds on all of P_iso
print("\n" + "=" * 98)
print("PART C -- index nullity on P_iso: the non-Krein chirality re-gradings STILL force nothing")
print("=" * 98)
worst = 0
for name, M in iso_ops:
    Wp, Wm = images(M)
    check(rank_gap(np.hstack([Wp, Wm]))[0] == 192, f"{name}: E_+ (+) E_- = W (complementary)")
    chis = chi_on_physical(Wp, Wm)
    worst = max(worst, max(abs(c) for c in chis))
    for c in chis:
        check(c == 0, f"{name}: chi_C(P) = {c} != 0 -- FAILURE CONDITION FIRED")
    print(f"  [{name}] chi_C(P) over {len(chis)} physical subspaces = {chis} (exact integers, all 0)")
check(worst == 0, "index nullity holds on every constructed P_iso operator")
print("  Proof (not luck): E_+/- = C(W_+/-) are K-null; a physical (K-positive) P meets a K-null")
print("  space only at 0, so both intersections vanish and chi_C(P) = 0.  Isotropy is the ONLY")
print("  hypothesis used -- so the theorem covers all of P_iso, not merely S.")

# ================================= PART D: the null condition is the boundary, and it bites
print("\n" + "=" * 98)
print("PART D -- a K-DEFINITE re-grading is not a chirality: it carries +-96 (load-bearing)")
print("=" * 98)
# build antilinear C whose re-graded eigenspaces are the K-positive / K-negative subspaces
Mdef = np.hstack([Pphys, Nphys]) @ Qc_inv              # C(W_+) = Pphys, C(W_-) = Nphys
Ep, Em = images(Mdef)
iso_def = image_isotropy(Mdef)
defp = np.linalg.eigvalsh(Ep.conj().T @ Kc @ Ep).min()
defn = np.linalg.eigvalsh(Em.conj().T @ Kc @ Em).max()
chi_def = chi_on_physical(Ep, Em)
print(f"  re-graded eigenspaces = (K-positive, K-negative): min/max Gram {defp:+.2f}/{defn:+.2f}")
print(f"    (K-DEFINITE, not null: eigenspace isotropy {iso_def:.2f} order 1) -- this grades")
print(f"    physical-vs-ghost norm, NOT chirality.  Its raw index on physical subspaces = {chi_def}")
print("    (the vectorlike +-96).  So a nonzero count needs a NON-null (K-definite) re-grading,")
print("    which is not a chirality at all -- exactly why isotropy is the load-bearing hypothesis.")
check(iso_def > 0.3, "K-definite eigenspaces are NOT K-null: not a chirality re-grading")
check(max(abs(c) for c in chi_def) == 96, "the K-definite re-grading carries +-96 (control non-vacuous)")

# and: outside P_iso an operator also fails to act on the physical sector (indefinite image)
print()
for j in range(3):
    Mbad = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
    iso_bad = image_isotropy(Mbad)
    img = Mbad @ Pphys.conj()
    ev = np.linalg.eigvalsh(img.conj().T @ Kc @ img)
    print(f"  random op {j}: eigenspace isotropy {iso_bad:.2f} (not in P_iso); "
          f"image of a physical subspace Krein Gram in [{ev.min():+.2f},{ev.max():+.2f}]: INDEFINITE")
    check(iso_bad > 0.3, f"random op {j} outside P_iso")
    check(ev.min() < -1e-6 and ev.max() > 1e-6, f"random op {j}: physical image non-physical")

# ---------------------------------------------------------------------------------- verdict
print("\n" + "#" * 98)
print("# #2 ADDENDUM -- VERDICT")
print("#" * 98)
print(f"""
  Reviewer #2 asks: can an operator evade the Krein-compatible class S and still act on the
  physical chiral sector?  It CAN evade S -- and it still forces nothing.  The admissible class
  is the larger, intrinsic

      P_iso = {{ antilinear C : the re-graded chirality eigenspaces C(W_+), C(W_-) are K-null
                (Lagrangian) }}  strictly ⊇ S,

  i.e. re-gradings of the SAME kind as the physical chirality (whose eigenspaces W_+/- are
  themselves K-null).  Index nullity holds on ALL of P_iso -- the proof used only isotropy,
  never the full Krein form M^dag K M = lambda K-bar.  We CONSTRUCTED non-Krein members
  (Krein residual order 1, eigenspace isotropy < 1e-8) and they are still index-null:
  chi_C(P) = 0 on every physical subspace, exact integers.

  The boundary is the null condition itself, and it bites: a re-grading with K-DEFINITE
  eigenspaces (e.g. the K-positive/K-negative split) is NOT a chirality -- it grades
  physical-vs-ghost -- and THAT is what carries the vectorlike +-96.  Such an operator also
  fails to map physical states to physical states (indefinite image).  So a nonzero count
  requires abandoning chirality (a non-null re-grading), not merely abandoning Krein-compat.

  HONEST RESIDUAL (unchanged): finite-dimensional kinematics on the explicit carrier; the QFT
  effective / non-perturbative (function-space) setting is the separate open card
  WC-FUNCTION-SPACE-EXT.  The kinematic form of #2's loophole is closed: admissibility is
  the null-eigenspace class P_iso (>> S), and index nullity holds on all of it.

  hard asserts passed: {NASSERT}
  total runtime: {time.time() - T0:.1f}s""")
# EOF
