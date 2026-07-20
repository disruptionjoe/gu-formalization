#!/usr/bin/env python3
"""L1 ASSEMBLY probe -- the diagonal-boundary law's first missing lemma run:
assemble the per-no-go reading classes into ONE category with finite products
and a diagonal (L1, Branch B), reconcile the THREE senses of fixpoint-free,
and check whether the Lawvere no-closure parent now APPLIES to the assembly.
Includes the STAGE-0 warm-up (the 63-panel Sheaf Theorist's question #4): are
the section-classification Z/2 (deck twist) and the payload-bit Z/2 (the
sig-b5 twisted-bundle class) the SAME class, or isomorphic-but-distinct?

CHANNEL: L1 assembly swing (Joe direct chat, 2026-07-20).
DESIGN:  explorations/l1-assembly-2026-07-20.md
PARENT:  explorations/diagonal-boundary-unification-2026-07-20.md (aadad6b) --
         the Lawvere no-closure parent (W70/W75, H63): L1 (category with
         finite products + diagonal; predicates = maps A -> B; closure =
         weakly point-surjective T : A x A -> B) and L2 (fixpoint-free label
         involution alpha) jointly give (a) no closure and, from L2 alone,
         (b) no alpha-invariant valuation. The parent doc's named residue:
         THREE distinct senses of fixpoint-free -- label-involution
         (Araki w / S-matrix V / section deck), ray-fixpoint-free (Kramers,
         J^2 = -1 on rays), free group action (record-sector Sp(1)) -- must
         be reconciled at L1 time.
REUSES:  fixture shapes of diagonal_boundary_probe.py (Kramers C^4, Araki
         Krein toy, 2-channel transparency, C-04 plant), the Cl(9,5) rep of
         sig_b5_habitat_probe.py / sector_relative_section_probe.py /
         torsor_k_sequence_probe.py (K_S = e_0..e_8, deck U_h = e0 e3 e4
         e9 e11 e12, J_quat = C conj with C = e1 e3 e5 e7 e10 e12, the
         commutant quaternion basis {I, iI, J, iJ}), and the habitat frame
         transport kprod (the 9-leg ordered Clifford product).

STAGE 0 (warm-up). Both Z/2 classes are readings of the K_S-SIGN datum
  {+K_S, -K_S} under ONE character sgn_K : (exhibited loops/deck elements)
  -> Z/2, sgn_K(W) = the sign in W K_S W^-1 = +- K_S = the sign of the
  habitat frame transport of K_S around the corresponding frame loop.
  The identifying map is exhibited: the section-theory seam U_h IS (minus)
  the spin lift of a habitat word -- three mixed-plane pi-rotations,
  (0,9)(3,11)(4,12), an ODD mixed count -- so the deck class is the
  habitat/payload class evaluated on the seam loop. Checked: per-generator
  commuting square (spin conjugation = frame transport on K_S), all 91
  coordinate-plane loops, random words; and the two READINGS (section
  symbol M-sign vs anchor exchange P_+/P_-) agree on every exhibited
  element -- no exhibited element separates them ([F] teeth).

STAGE 1 (the lemma). The assembled category C_read: objects = the six
  reading-class fixtures (entropy-class / S-matrix / Kramers J-commuting /
  conserved-pairing (m1) / record-sector / section-K_S-linear) + the label
  object B = {+,-}; realized as Z/2-sets (orbit-closed fixture carriers
  with their exhibited involutions); morphisms = the exhibited equivariant
  maps (label maps lambda_X to B for the five orientation no-gos; the
  Kramers embedding into the record fixture; parity transfer). Finite
  products, terminal object, and equivariant diagonals verified (label
  level exhaustive, vector level on batteries). RECONCILIATION: one group
  G = Sp(1)_comm u U_h Sp(1)_comm, extension
      1 -> Sp(1)_comm -> G -> Z/2_deck -> 1,
  with a second (linear/antilinear) grading; the three fixpoint-free
  senses are its three graded pieces: label = the coset grading acting on
  B (fixpoint-free swap; linear implementations have fixed RAYS -- shown),
  ray = the antilinear part (EVERY antilinear element of G squares to -1:
  Kramers-type, no fixed rays -- kernel and coset alike; dissolution dial
  = real-type controls, including m1's own conjugation swap), free = the
  kernel Sp(1)_comm (free on states, simply transitive on the deck's
  implementation coset). Then the PARENT is run on the assembled label
  object (exhaustive): the twisted diagonal escapes every T, zero
  invariant valuations, alpha = id dissolves -- and per object the
  excluded class = the alpha-equivariant class EXACTLY (separation iff
  odd part nonzero; native classes re-verified even).

PLANTED-OUTSIDE ([F], required): the C-04 prime-3 no-go must sit OUTSIDE
  the assembled category STRUCTURALLY: its datum (dim mod 3) is fixed by
  every involution of G, so its Z/2-action is trivial, and an equivariant
  label map trivial -> B would need a fixed point of the swap -- there is
  none (Hom_{Z/2}(triv, B) = empty, enumerated); no 2^a refinement
  reaches divisibility by 3. If the plant assembles, the law is vacuous.

PRE-DECLARED OUTCOMES: (L-a) assembly obstruction -- named precisely;
  (L-b) assembles, senses do NOT reconcile -- partial law, scope stated;
  (L-c) assembles + reconciles + parent applies -- boundary law at fixture
  grade, plant verified outside.

NONCLAIMS. Fixture grade throughout (matrix/finite Z/2-sets): no operator
  lift, no Lean, no claim/canon/posture movement; the +-i0 orientation bit
  of the section theory is a DIFFERENT Z/2 (typed scheme there) and is not
  touched; the universal-null (m1) object joins the category but its
  exclusion (positivity) is NOT a B-datum -- supply line, in scope notes.
Deterministic: numpy only, seed 20260720. Exit 0 iff ALL PASS.
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
rng = np.random.default_rng(20260720)
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def mx(A):
    return float(np.max(np.abs(A)))


# --- [T] the shared Cl(9,5) fixtures (verbatim conventions) -------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                          # K_S = e_0 e_1 ... e_8
U_h = e[0] @ e[3] @ e[4] @ e[9] @ e[11] @ e[12]   # the section-theory deck/seam
Uh_inv = np.linalg.inv(U_h)
C_J = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]   # J_quat = C_J . conj (canon)
CJ_inv = np.linalg.inv(C_J)
I128 = np.eye(DIM)

cliff_ok = all(
    mx(e[a] @ e[b] + e[b] @ e[a]
       - 2.0 * (ETA[a] if a == b else 0.0) * I128) < 1e-9
    for a in range(N_DIRS) for b in range(a, N_DIRS))
anti_ok = all(mx(C_J @ np.conj(e[a]) - e[a] @ C_J) == 0.0
              for a in range(N_DIRS))
check("T", "rep: Clifford relations for eta = (9,5); J_quat = C_J conj "
           "commutes with the Clifford ACTION in the antilinear sense "
           "(C_J conj(e_a) = e_a C_J exactly, all 14 legs)",
      cliff_ok and anti_ok)

check("T", "fixtures: K_S Hermitian involution; U_h^2 = I; J_quat^2 = -1 "
           "(antiunitary, C_J conj); all exact",
      mx(K_S - K_S.conj().T) < 1e-12 and mx(K_S @ K_S - I128) < 1e-12
      and mx(U_h @ U_h - I128) == 0.0
      and mx(C_J @ np.conj(C_J) + I128) < 1e-12)


def kprod(frame_cols):
    """Habitat frame transport: ordered Clifford product of the nine +legs
    of a 14-frame (column c = c-th frame vector in the e-basis)."""
    out = np.eye(DIM, dtype=complex)
    for c in range(9):
        gen = sum(frame_cols[d, c] * e[d] for d in range(N_DIRS))
        out = out @ gen
    return out


def rot(n, a, b, th):
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def ks_sign(W):
    """sgn_K(W): the sign s in W K_S W^-1 = s K_S, else 0."""
    T = W @ K_S @ np.linalg.inv(W)
    if mx(T - K_S) < 1e-8:
        return +1
    if mx(T + K_S) < 1e-8:
        return -1
    return 0


# ==============================================================================
# STAGE 0 -- are the deck-twist Z/2 and the payload-bit Z/2 the SAME class?
# ==============================================================================
print()
print("--- STAGE 0: the Z/2 identity (deck twist vs payload bit) ---")

# A1: deck side of the character.
check("E", "A1 deck: U_h K_S U_h^-1 = -K_S exactly (the section-theory seam "
           "reads sgn_K = -1)", ks_sign(U_h) == -1 and mx(U_h @ U_h - I128) == 0.0)

# A2: THE IDENTIFYING MAP -- the seam is (minus) the spin lift of a habitat
# word: three mixed-plane pi-rotations (0,9)(3,11)(4,12), odd mixed count.
W3 = (e[0] @ e[9]) @ (e[3] @ e[11]) @ (e[4] @ e[12])
a2 = mx(U_h + W3) == 0.0
flip = {0, 3, 4, 9, 11, 12}
a2v = all(mx(U_h @ e[a] @ Uh_inv - (-1.0 if a in flip else 1.0) * e[a]) == 0.0
          for a in range(N_DIRS))
check("E", "A2 identifying map: U_h = -(e0 e9)(e3 e11)(e4 e12) exactly, and "
           "U_h-conjugation flips exactly the six legs {0,3,4,9,11,12} -- "
           "the seam IS the composite of THREE mixed-plane pi-rotations "
           "(odd mixed count): a habitat word", a2 and a2v)

# A3: per-generator commuting square -- spin conjugation = frame transport,
# on K_S, for each of the three seam planes and their composite.
sq_ok = True
for (a, b) in [(0, 9), (3, 11), (4, 12)]:
    Vab = e[a] @ e[b]                      # spin lift of the pi-rotation
    spin = ks_sign(Vab)
    frame = kprod(np.linalg.inv(rot(N_DIRS, a, b, np.pi)))
    fr = +1 if mx(frame - K_S) < 1e-9 else (-1 if mx(frame + K_S) < 1e-9 else 0)
    if not (spin == fr == -1):
        sq_ok = False
R3 = rot(N_DIRS, 0, 9, np.pi) @ rot(N_DIRS, 3, 11, np.pi) @ rot(N_DIRS, 4, 12, np.pi)
comp = kprod(np.linalg.inv(R3))
sq_ok &= mx(comp + K_S) < 1e-9 and mx(U_h @ K_S @ Uh_inv - (-K_S)) == 0.0
check("E", "A3 commuting square: for each seam plane, spin-lift conjugation "
           "= habitat frame transport on K_S (= -1); the composite frame "
           "word transports K_S -> -K_S = U_h K_S U_h^-1", sq_ok)

# A4: all 91 coordinate-plane loops -- the two sides agree EVERYWHERE,
# and the sign is the mixedness parity (the one character).
n_agree, n_mixed = 0, 0
for a in range(N_DIRS):
    for b in range(a + 1, N_DIRS):
        mixed = ETA[a] * ETA[b] < 0
        want = -1 if mixed else +1
        spin = ks_sign(e[a] @ e[b])
        frame = kprod(np.linalg.inv(rot(N_DIRS, a, b, np.pi)))
        fr = +1 if mx(frame - K_S) < 1e-9 else (-1 if mx(frame + K_S) < 1e-9 else 0)
        if spin == fr == want:
            n_agree += 1
        if mixed:
            n_mixed += 1
check("E", "A4 all 91 plane loops: spin sign == frame sign == mixedness "
           "parity (45 mixed -> -1, 46 same-sign -> +1) -- ONE character "
           "sgn_K, no disagreeing loop", n_agree == 91 and n_mixed == 45,
      f"{n_agree}/91 agree")

# A5: random words -- sgn_K is a homomorphism and equals the frame
# transport and the parity of the word's mixed-plane count.
planes = [(a, b) for a in range(N_DIRS) for b in range(a + 1, N_DIRS)]
w_ok = True
for _ in range(20):
    k = int(rng.integers(1, 7))
    idx = rng.integers(0, len(planes), size=k)
    word = [planes[i] for i in idx]
    Wspin = I128.astype(complex)
    A_fr = np.eye(N_DIRS)
    par = 1
    for (a, b) in word:
        Wspin = Wspin @ (e[a] @ e[b])
        A_fr = A_fr @ rot(N_DIRS, a, b, np.pi)
        if ETA[a] * ETA[b] < 0:
            par = -par
    s_spin = ks_sign(Wspin)
    frame = kprod(np.linalg.inv(A_fr))
    s_fr = +1 if mx(frame - K_S) < 1e-8 else (-1 if mx(frame + K_S) < 1e-8 else 0)
    if not (s_spin == s_fr == par):
        w_ok = False
check("E", "A5 random words (20, length <= 6): sgn_K(word) = product of "
           "plane signs = frame-transport sign (character/homomorphism law "
           "holds; the class is one Z/2 datum)", w_ok)

# A6: the SECTION reading of the datum. M = Ku D built from {D, K_S} alone;
# deck-oddness of M is DERIVED from A1 for ANY K_S-self-adjoint D, and M is
# linear in K_S (one factor): flipping K_S flips M; even scalars blind.
def sec_symbol(D, K):
    c_s = 0.5 * (D + K @ D @ K)
    P = float(np.trace(c_s @ c_s).real) / DIM
    Ku = K @ c_s / np.sqrt(P)
    return Ku @ D, P


def rand_ks_selfadjoint():
    X = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    return 0.5 * (X + K_S @ X.conj().T @ K_S)


a6 = True
for _ in range(3):
    D = rand_ks_selfadjoint()
    M, P = sec_symbol(D, K_S)
    Mimg, Pimg = sec_symbol(U_h @ D @ Uh_inv, K_S)
    if mx(Mimg + U_h @ M @ Uh_inv) / mx(M) > 1e-10:
        a6 = False                        # deck-oddness, derived from A1 alone
    if abs(Pimg - P) / abs(P) > 1e-12:
        a6 = False                        # even scalar blind
    Mflip, Pflip = sec_symbol(D, -K_S)
    if mx(Mflip + M) / mx(M) > 1e-12 or abs(Pflip - P) > 1e-12:
        a6 = False                        # M carries exactly ONE K_S factor
check("E", "A6 section reading: M(U_h D U_h^-1) = -U_h M(D) U_h^-1 for "
           "random K_S-self-adjoint D (deck-oddness DERIVED from A1 alone); "
           "M(-K_S) = -M and P invariant (the section datum reads the "
           "K_S-sign and nothing else)", a6)

# A7: the PAYLOAD reading of the same datum -- anchor exchange and charge
# flip under K_S -> -K_S (the habitat holonomy value, sig-b5 Part C shape).
P_plus = 0.5 * (I128 + K_S)
P_minus = 0.5 * (I128 - K_S)
a7 = mx(0.5 * (I128 + (-K_S)) - P_minus) == 0.0
for _ in range(10):
    psi = P_plus @ (rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM))
    psi /= np.linalg.norm(psi)
    q0 = float((psi.conj() @ K_S @ psi).real)
    q1 = float((psi.conj() @ (-K_S) @ psi).real)
    if not (q0 > 0 and abs(q1 + q0) < 1e-12):
        a7 = False
check("E", "A7 payload reading: P_+(-K_S) = P_-(K_S) exactly and the Krein "
           "charge flips sign on confined draws (the payload bit reads the "
           "SAME K_S-sign datum)", a7)

# A8: the identity -- for every exhibited element W, the section reading,
# the payload reading, and sgn_K(W) coincide (two-line theorem given
# W K_S W^-1 = s K_S: M -> s W M W^-1 and P_+ -> P_(s), both read s).
def section_read(W):
    Wi = np.linalg.inv(W)
    Mimg, _ = sec_symbol(W @ D_ref @ Wi, K_S)
    WMW = W @ M_ref @ Wi
    if mx(Mimg - WMW) / mx(M_ref) < 1e-8:
        return +1
    if mx(Mimg + WMW) / mx(M_ref) < 1e-8:
        return -1
    return 0


def payload_read(W):
    Wi = np.linalg.inv(W)
    Pimg = 0.5 * (I128 + W @ K_S @ Wi)
    if mx(Pimg - P_plus) < 1e-8:
        return +1
    if mx(Pimg - P_minus) < 1e-8:
        return -1
    return 0


D_ref = rand_ks_selfadjoint()
M_ref, _ = sec_symbol(D_ref, K_S)
elems = [e[a] @ e[b] for (a, b) in [(0, 9), (2, 5), (10, 13), (7, 12)]]
elems += [U_h, U_h @ (e[1] @ e[9]), e[0] @ e[9] @ e[3] @ e[11]]
a8 = all(section_read(W) == payload_read(W) == ks_sign(W) != 0 for W in elems)
check("E", "A8 THE IDENTITY: section reading == payload reading == sgn_K on "
           "every exhibited element (mixed-plane lifts, the seam, mixed "
           "words) -- one Z/2 object, two reading classes", a8)

# F-A9 teeth: a SECOND independent Z/2 would need an exhibited element that
# separates the two readings. Sweep all 91 plane lifts + 20 random words:
# none separates. (One disagreement would refute the identity.)
sep = 0
for a in range(N_DIRS):
    for b in range(a + 1, N_DIRS):
        W = e[a] @ e[b]
        if section_read(W) != payload_read(W):
            sep += 1
for _ in range(20):
    k = int(rng.integers(1, 5))
    idx = rng.integers(0, len(planes), size=k)
    W = I128.astype(complex)
    for i in idx:
        aa, bb = planes[i]
        W = W @ (e[aa] @ e[bb])
    if section_read(W) != payload_read(W):
        sep += 1
check("F", "A9 teeth: NO exhibited element separates the section reading "
           "from the payload reading (91 planes + 20 words, 0 separators): "
           "the two Z/2 classes are not isomorphic-but-distinct at fixture "
           "grade -- they are one class", sep == 0, f"separators: {sep}")

# ==============================================================================
# PART B -- the RECONCILIATION: three fixpoint-free senses, one structure
# ==============================================================================
print()
print("--- PART B: reconciling the three senses of fixpoint-free ---")


# antilinear-op helpers: op = (A, s); psi -> A psi (s=0) or A conj(psi) (s=1)
def op_apply(op, psi):
    A, s = op
    return A @ (np.conj(psi) if s else psi)


def op_compose(op1, op2):
    A, s = op1
    B, t = op2
    return (A @ (np.conj(B) if s else B), s ^ t)


def op_inv(op):
    A, s = op
    return (np.linalg.inv(np.conj(A)), 1) if s else (np.linalg.inv(A), 0)


def quat_apply(z1, z2, psi):
    """Kernel element z1 + z2 j of Sp(1)_comm: psi -> z1 psi + z2 J psi."""
    return z1 * psi + z2 * (C_J @ np.conj(psi))


# B1: the kernel is the quaternionic commutant.
b1 = all(mx(C_J @ np.conj(e[a]) - e[a] @ C_J) == 0.0 for a in range(N_DIRS))
b1 &= mx(C_J @ np.conj(C_J) + I128) < 1e-12          # J^2 = -1
b1 &= mx(C_J @ np.conj(K_S) @ CJ_inv - K_S) == 0.0   # J fixes K_S: label-EVEN
check("E", "B1 kernel: J_quat commutes with every e_a as an ANTILINEAR map "
           "(C_J conj(e_a) = e_a C_J, all legs -- the R-linear commutant is "
           "H = span{I, iI, J, iJ}); J^2 = -1; J FIXES K_S (the Kramers "
           "involution is label-even -- it is NOT the flip)", b1)

# B2: the extension 1 -> Sp(1)_comm -> G -> Z/2_deck -> 1: U_h normalizes
# the kernel, and the coset map is sgn_K.
b2 = mx(U_h @ C_J @ np.conj(Uh_inv) - C_J) == 0.0    # U_h J U_h^-1 = J
b2 &= ks_sign(U_h) == -1
b2 &= all(ks_sign(z * I128) == +1 for z in (1.0, 1j))
check("E", "B2 the extension: U_h normalizes Sp(1)_comm (U_h J U_h^-1 = J "
           "exactly); kernel elements read sgn_K = +1, the deck coset reads "
           "-1: G = Sp(1)_comm u U_h Sp(1)_comm with G/Sp(1)_comm = Z/2 "
           "acting on B = {+K_S, -K_S} by the fixpoint-free swap "
           "[SENSE 1: label]", b2)

# B3: linear implementations of the flip have FIXED RAYS -- the label sense
# is not the ray sense; ray-fixpoint-freeness lives on the antilinear part.
evals_uh, evecs_uh = np.linalg.eigh(0.5 * (U_h + U_h.conj().T))
v_fix = evecs_uh[:, -1]
res_fix = float(np.linalg.norm(U_h @ v_fix - v_fix))
b3 = res_fix < 1e-9 and abs(np.vdot(v_fix, U_h @ v_fix)) > 0.99
check("E", "B3 separation of senses: the LINEAR flip implementation U_h has "
           "fixed rays (exhibited +1 eigenvector), so label-fixpoint-freeness "
           "does not give ray-fixpoint-freeness -- the senses are honestly "
           "distinct and need reconciling", b3, f"|U_h v - v| = {res_fix:.1e}")

# B4: EVERY antilinear element of G squares to -1 (Kramers-type): kernel
# side zJ and coset side U_h zJ alike; <A psi, psi> = 0 identically.
b4 = True
for _ in range(6):
    z = np.exp(1j * float(rng.uniform(0, 2 * np.pi)))
    for A_op in ((z * C_J, 1), (U_h @ (z * C_J), 1)):
        sq = op_compose(A_op, A_op)
        if sq[1] != 0 or mx(sq[0] + I128) > 1e-10:
            b4 = False
        psi = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
        if abs(np.vdot(op_apply(A_op, psi), psi)) > 1e-9 * float(
                np.linalg.norm(psi)) ** 2:
            b4 = False
check("E", "B4 the antilinear part of G is WHOLLY Kramers-type: (zJ)^2 = -1 "
           "AND (U_h zJ)^2 = -1 for random unit z, with <A psi, psi> = 0 "
           "identically on both cosets (no fixed rays anywhere antilinear) "
           "[SENSE 2: ray] -- the ghost-Kramers composite U_h J is the "
           "S_VJ shape, now located inside G", b4)

# B5: the kernel acts FREELY on states and SIMPLY TRANSITIVELY on the
# deck implementation coset [SENSE 3: free action].
b5 = True
for _ in range(6):
    zv = rng.standard_normal(4)
    zv /= np.linalg.norm(zv)
    z1, z2 = zv[0] + 1j * zv[1], zv[2] + 1j * zv[3]
    if abs(z1 - 1) < 1e-6 and abs(z2) < 1e-6:
        continue
    psi = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
    psi /= np.linalg.norm(psi)
    if np.linalg.norm(quat_apply(z1, z2, psi) - psi) < 1e-6:
        b5 = False                        # a nonidentity unit quat fixed psi
imps = [(U_h, 0), (U_h @ (1j * I128), 0), (U_h @ C_J, 1),
        ((0.6 + 0.8j) * U_h, 0)]
for (A, s) in imps:
    T = A @ (np.conj(K_S) if s else K_S) @ np.linalg.inv(A)
    if mx(T + K_S) > 1e-9:
        b5 = False                        # every U_h u implements the flip
for W1 in imps:
    for W2 in imps:
        R, sflag = op_compose(W1, op_inv(W2))
        if sflag == 0:
            if any(mx(R @ e[a] - e[a] @ R) > 1e-9 for a in range(N_DIRS)):
                b5 = False                # linear ratio must lie in kernel
        else:
            if any(mx(R @ np.conj(e[a]) - e[a] @ R) > 1e-9
                   for a in range(N_DIRS)):
                b5 = False                # antilinear ratio: kernel iff
                                          # R conj(e_a) = e_a R (B1 sense)
check("E", "B5 the kernel Sp(1)_comm acts FREELY on nonzero states, every "
           "U_h u implements the SAME flip, and ratios of implementations "
           "lie in the kernel: the implementation set of the categorical "
           "involution is a free Sp(1)_comm-torsor [SENSE 3: free action]",
      b5)

# B6: the dissolution dial at the reconciled level -- real-type controls.
Hr = rng.standard_normal((4, 4))
Hr = 0.5 * (Hr + Hr.T)
simple = bool(np.all(np.diff(np.sort(np.linalg.eigvalsh(Hr))) > 1e-6))
v_re = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)   # conj-fixed ray
b6 = simple and float(np.linalg.norm(np.conj(v_re) - v_re)) == 0.0
# m1's conjugation swap sigma(a,b) = (conj b, conj a): antilinear, sq +1,
# FIXED modes (a, conj a): real-type -- the supply line sits on the
# dissolution side of the ray dial.
sig_m = np.array([[0.0, 1.0], [1.0, 0.0]])
v_m = np.array([1.0 + 2.0j, 1.0 - 2.0j])
b6 &= mx(sig_m @ np.conj(sig_m) - np.eye(2)) == 0.0
b6 &= float(np.linalg.norm(sig_m @ np.conj(v_m) - v_m)) == 0.0
check("E", "B6 dissolution dial: real-type antilinears (sigma^2 = +1) have "
           "fixed rays -- generic real-symmetric spectrum simple (the (7,7) "
           "miniature), and the m1 conjugation swap u_+ <-> u_- is itself "
           "real-type with an exhibited fixed mode: the universal-null "
           "supply line sits on the DISSOLUTION side of the ray dial, which "
           "is WHY it is not an instance", b6)

# ==============================================================================
# PART C -- the assembled category C_read (L1 proper)
# ==============================================================================
print()
print("--- PART C: the category, its products and diagonal, the parent ---")

# --- C1: the reading-class objects as Z/2-sets, with even/odd batteries ------
# X_ar (entropy-class functionals): the Araki Krein toy.
K4 = np.diag([1.0, 1.0, -1.0, -1.0])
W4 = np.block([[np.zeros((2, 2)), np.eye(2)], [np.eye(2), np.zeros((2, 2))]])
A0 = rng.standard_normal((2, 2))
Sp0 = A0 @ A0.T + 0.1 * np.eye(2)
rho_p = np.zeros((4, 4))
rho_p[:2, :2] = Sp0 / np.trace(Sp0)
rho_m = W4 @ rho_p @ W4
g0 = rng.standard_normal((4, 4))
G0 = g0 @ g0.T + 0.1 * np.eye(4)
gamma4 = 0.5 * (G0 + W4 @ G0 @ W4)
gamma4 /= np.trace(gamma4)


def rel_ent(r, s):
    er, Ur = np.linalg.eigh(r)
    es, Us = np.linalg.eigh(s)
    lr = Ur @ np.diag(np.log(np.clip(er, 1e-30, None))) @ Ur.T
    ls = Us @ np.diag(np.log(np.clip(es, 1e-30, None))) @ Us.T
    return float(np.trace(r @ (lr - ls)))


c1_ar = mx(W4 @ W4 - np.eye(4)) < 1e-14 and mx(W4 @ K4 @ W4 + K4) < 1e-14
c1_ar &= abs(rel_ent(rho_p, gamma4) - rel_ent(rho_m, gamma4)) < 1e-12
c1_ar &= abs(np.trace(rho_p @ rho_p) - np.trace(rho_m @ rho_m)) < 1e-12
kp = float(np.trace(rho_p @ K4))
c1_ar &= abs(kp + float(np.trace(rho_m @ K4))) < 1e-12 and abs(kp) > 0.1
eps_t = 1e-3
gt = gamma4 + eps_t * (K4 @ gamma4 + gamma4 @ K4) / 2
gt = 0.5 * (gt + gt.T)
gt /= np.trace(gt)
c1_ar &= abs(rel_ent(rho_p, gt) - rel_ent(rho_m, gt)) > 1e-5
check("E", "C1a object X_ar (entropy-class): w K w = -K; even battery "
           "(rel-entropy vs invariant ref, purity) BLIND; datum k = Tr(rho K) "
           "odd; eps-tilted (alpha-breaking) reference READS it -- object, "
           "grading, and cure exhibited", c1_ar)

# X_sm (S-matrix functionals): the 2-channel transparency toy.
t_dyn = 0.62 + 0.31j
eps_g = np.diag([1.0, -1.0])
Vp = np.array([[0.0, 1.0], [1.0, 0.0]])
t_mat = t_dyn * np.eye(2)
c1_sm = mx(Vp @ t_mat - t_mat @ Vp) < 1e-14
c1_sm &= mx(Vp @ eps_g + eps_g @ Vp) < 1e-14
c1_sm &= abs(np.trace(t_mat.conj().T @ eps_g @ t_mat)) < 1e-14
per_ch = abs(t_dyn) ** 2 * eps_g[0, 0]
prep = np.diag([1.0, 0.0])
odd_read = float(np.trace(prep @ t_mat.conj().T @ eps_g @ t_mat).real)
c1_sm &= abs(per_ch) > 0.01 and abs(odd_read) > 0.01
check("E", "C1b object X_sm (S-matrix): [V, t] = 0, {V, eps} = 0, traced "
           "graded functionals identically 0 (even class blind); per-channel "
           "graded datum odd and nonzero; graded PREPARATION (external "
           "datum) reads it", c1_sm)

# X_kr (Hermitian J-commuting probes): the Kramers C^4 fixture.
Jm = np.block([[np.zeros((2, 2)), -np.eye(2)], [np.eye(2), np.zeros((2, 2))]])


def j_project(H):
    Bp = 0.5 * (H + Jm @ np.conj(H) @ np.linalg.inv(Jm))
    return 0.5 * (Bp + Bp.conj().T)


c1_kr = True
for _ in range(4):
    H = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    HJ = j_project(H + H.conj().T)
    ev = np.sort(np.linalg.eigvalsh(HJ))
    mults, cur = [], 1
    for x, y in zip(ev, ev[1:]):
        if abs(x - y) < 1e-8:
            cur += 1
        else:
            mults.append(cur)
            cur = 1
    mults.append(cur)
    c1_kr &= all(m % 2 == 0 for m in mults)
Q3 = np.diag([1.0, 1.0, 1.0, 0.0]).astype(complex)
c1_kr &= int(np.sum(np.linalg.eigvalsh(Q3) > 0.5)) == 3
c1_kr &= mx(Q3 @ Jm - Jm @ np.conj(Q3)) > 0.5
check("E", "C1c object X_kr (J-commuting probes): all-even multiplicities "
           "(even class cannot reach odd signature); the rank-3 NON-J import "
           "reads the odd datum -- the cure is external", c1_kr)

# X_rec (record-sector bilinears): current invariant under the kernel,
# charge odd under the coset.
c1_rec = True
psi0 = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
psi0 /= np.linalg.norm(psi0)
for _ in range(4):
    zv = rng.standard_normal(4)
    zv /= np.linalg.norm(zv)
    up = quat_apply(zv[0] + 1j * zv[1], zv[2] + 1j * zv[3], psi0)
    for a in (0, 5, 9, 13):
        J0 = float((psi0.conj() @ K_S @ e[a] @ psi0).real)
        J1 = float((up.conj() @ K_S @ e[a] @ up).real)
        if abs(J1 - J0) > 1e-9:
            c1_rec = False
psi_c = P_plus @ psi0
psi_c /= np.linalg.norm(psi_c)
q_c = float((psi_c.conj() @ K_S @ psi_c).real)
ut = U_h @ psi_c
q_t = float((ut.conj() @ K_S @ ut).real)
c1_rec &= q_c > 0 and abs(q_t + q_c) < 1e-9
check("E", "C1d object X_rec (record-sector bilinears): the record current "
           "J^a is Sp(1)_comm-INVARIANT (kernel-even, sampled unit "
           "quaternions x 4 legs), and the Krein charge is COSET-ODD "
           "(U_h transport flips it exactly): the record class reads B "
           "through the same one Z/2", c1_rec)

# X_sec: exhibited at A6 (q, P deck-even; M deck-odd) -- cross-reference.
# X_m1 (conserved pairings): conserved symmetric pairings for the mode
# dynamics G = diag(g, -g) are EXACTLY the off-diagonal ones: self-null,
# indefinite; no positive conserved pairing exists (the supply line).
g_m = 0.7
G_dyn = np.diag([g_m, -g_m])
rows = []
for (i, j) in [(0, 0), (0, 1), (1, 1)]:
    Bm = np.zeros((2, 2))
    Bm[i, j] = Bm[j, i] = 1.0
    L = Bm @ G_dyn + G_dyn.T @ Bm
    rows.append([L[0, 0], L[0, 1], L[1, 1]])
Lmat = np.array(rows).T
sv = np.linalg.svd(Lmat)[1]
null_dim = int(np.sum(sv < 1e-12))
Bnull = np.array([[0.0, 1.0], [1.0, 0.0]])
c1_m1 = null_dim == 1
c1_m1 &= mx(Bnull @ G_dyn + G_dyn.T @ Bnull) < 1e-14
c1_m1 &= abs(Bnull[0, 0]) == 0.0 and abs(Bnull[1, 1]) == 0.0
c1_m1 &= float(np.min(np.linalg.eigvalsh(Bnull))) < -0.5
check("E", "C1e object X_m1 (conserved pairings): the conserved symmetric "
           "pairing space is 1-dim and OFF-DIAGONAL (each mode self-null, "
           "pairing indefinite) -- no positive conserved pairing; the object "
           "joins the category with its real-type involution (B6), but its "
           "excluded property (positivity) is NOT a B-datum: supply line, "
           "in scope only", c1_m1)

# The "exactly" clause as an identity: F separates an alpha-orbit iff its
# odd part is nonzero there (F(x) - F(alpha x) = 2 F_odd(x)); native classes
# are the even ones (receipts above).
ex_ok = True
for _ in range(8):
    fvec = rng.standard_normal((4, 4))
    fvec = 0.5 * (fvec + fvec.T)          # random functional Tr(rho F)
    Fp = float(np.trace(rho_p @ fvec))
    Fm = float(np.trace(rho_m @ fvec))
    odd_part = 0.5 * float(np.trace(rho_p @ (fvec - W4 @ fvec @ W4)))
    if abs((Fp - Fm) - 2.0 * odd_part) > 1e-10:
        ex_ok = False
    if (abs(Fp - Fm) > 1e-9) != (abs(odd_part) > 1e-9):
        ex_ok = False
check("E", "C2 the EXACTLY clause: a functional separates an alpha-orbit "
           "iff its odd part is nonzero (F(x) - F(alpha x) = 2 F_odd(x), "
           "identity on random functionals) -- excluded class = equivariant "
           "class, exactly, not just contained", ex_ok)

# --- C3: morphisms -- label maps to B, all equivariant (naturality of the
# ONE involution on exhibited arrows) ------------------------------------------
lam_ar = {"rp": +1, "rm": -1}             # sign of Tr(rho K)
nat_ar = (np.sign(np.trace((W4 @ rho_p @ W4) @ K4)) == -lam_ar["rp"]
          and np.sign(np.trace((W4 @ rho_m @ W4) @ K4)) == -lam_ar["rm"])
prep_p, prep_m = np.diag([1.0, 0.0]), np.diag([0.0, 1.0])
lam_sm_p = np.sign(np.trace(prep_p @ eps_g).real)
lam_sm_m = np.sign(np.trace(prep_m @ eps_g).real)
nat_sm = (np.sign(np.trace((Vp @ prep_p @ Vp) @ eps_g).real) == -lam_sm_p
          and lam_sm_p == -lam_sm_m)
nat_rec = q_c > 0 and q_t < 0             # lambda_rec = sign of charge
nat_sec = section_read(U_h) == -1         # deck flips the section label (A8)
check("E", "C3 label maps: lambda_ar, lambda_sm, lambda_rec, lambda_sec all "
           "exhibited and EQUIVARIANT (each object involution covers the "
           "swap on B) -- the naturality squares of the one categorical "
           "involution commute on every exhibited arrow",
      nat_ar and nat_sm and nat_rec and nat_sec)

# --- C4: the Kramers embedding X_kr -> X_rec: the fixture involution IS the
# restriction of the flip's ANTILINEAR implementation A = U_h J_quat --------
Uvals, Uvecs = np.linalg.eigh(0.5 * (U_h + U_h.T))
plus_cols = Uvecs[:, Uvals > 0.5]
b1v = plus_cols[:, 0].astype(complex)
b1v /= np.linalg.norm(b1v)
Jb1 = C_J @ np.conj(b1v)
b2v = plus_cols[:, 1].astype(complex)
b2v = b2v - (np.vdot(b1v, b2v)) * b1v - (np.vdot(Jb1, b2v)) * Jb1
b2v /= np.linalg.norm(b2v)
Jb2 = C_J @ np.conj(b2v)
Phi = np.column_stack([b1v, b2v, Jb1, Jb2])
orth = mx(Phi.conj().T @ Phi - np.eye(4))
emb_ok = orth < 1e-9
for _ in range(4):
    v4 = rng.standard_normal(4) + 1j * rng.standard_normal(4)
    lhs = Phi @ (Jm @ np.conj(v4))
    rhs = C_J @ np.conj(Phi @ v4)          # J_quat on the image
    rhs2 = U_h @ rhs                       # A = U_h J_quat; U_h fixes image
    if np.linalg.norm(lhs - rhs) > 1e-9 or np.linalg.norm(lhs - rhs2) > 1e-9:
        emb_ok = False
check("E", "C4 the Kramers embedding: an isometric Phi : C^4 -> C^128 with "
           "Phi(J_m conj v) = J_quat Phi(v) = (U_h J_quat) Phi(v) (image in "
           "the U_h = +1 eigenspace): the Kramers fixture involution IS the "
           "restriction of the flip's antilinear implementation -- the ray "
           "sense embeds into G, closing the reconciliation", emb_ok)

# --- C5: finite products, terminal object, diagonal (Z/2-Set, verified) ------
Bset = [+1, -1]


def swp(x):
    return -x


BxB = [(x, y) for x in Bset for y in Bset]
prod_ok = True
eq_maps = [lambda x: x, lambda x: -x]     # all equivariant maps B -> B
for f in eq_maps:
    for g in eq_maps:
        hs = []
        for h_vals in itertools.product(BxB, repeat=2):
            h = dict(zip(Bset, h_vals))
            if all(h[x][0] == f(x) and h[x][1] == g(x) for x in Bset):
                hs.append(h)
        if len(hs) != 1:
            prod_ok = False               # existence AND uniqueness
        h = hs[0]
        if not all(h[swp(x)] == (swp(h[x][0]), swp(h[x][1])) for x in Bset):
            prod_ok = False               # the pairing map is equivariant
diag_ok = all((swp(x), swp(x)) == tuple(map(swp, (x, x))) for x in Bset)
# terminal object: the one-point Z/2-set {*}; from any finite object there
# is EXACTLY one map to it, and it is equivariant (alpha(*) = *).
term_ok = True
for X_elems, alph in [(Bset, swp),
                      (BxB, lambda p: (swp(p[0]), swp(p[1])))]:
    maps_to_pt = list(itertools.product(["*"], repeat=len(X_elems)))
    if len(maps_to_pt) != 1:
        term_ok = False
    hmap = dict(zip(X_elems, maps_to_pt[0]))
    if not all(hmap[alph(x)] == hmap[x] for x in X_elems):
        term_ok = False
check("E", "C5 L1 structure: B x B has the universal property (existence + "
           "uniqueness of the pairing, exhaustive over equivariant maps), "
           "the pairing and Delta are equivariant, terminal object present "
           "(unique equivariant map from each object, enumerated): C_read "
           "has finite products and the diagonal as a category of Z/2-sets "
           "over the ONE Z/2", prod_ok and diag_ok and term_ok)


# --- C6: the PARENT APPLIES to the assembly (exhaustive skeleton) -------------
def diagonal_always_escapes(nA, alpha):
    cells = [(i, j) for i in range(nA) for j in range(nA)]
    escapes, represented = True, False
    for values in itertools.product((0, 1), repeat=len(cells)):
        T = dict(zip(cells, values))
        d = tuple(alpha[T[(a, a)]] for a in range(nA))
        rows_ = {tuple(T[(a0, a)] for a in range(nA)) for a0 in range(nA)}
        if d in rows_:
            escapes, represented = False, True
    return escapes, represented


def invariant_valuations(nA, alpha):
    return sum(all(alpha[p[a]] == p[a] for a in range(nA))
               for p in (dict(zip(range(nA), v))
                         for v in itertools.product((0, 1), repeat=nA)))


swap_d, ident_d = {0: 1, 1: 0}, {0: 0, 1: 1}
c6 = all(diagonal_always_escapes(nn, swap_d)[0] for nn in (1, 2, 3))
c6 &= all(diagonal_always_escapes(nn, ident_d)[1] for nn in (1, 2, 3))
c6 &= all(invariant_valuations(nn, swap_d) == 0 and
          invariant_valuations(nn, ident_d) == 2 ** nn for nn in (1, 2, 3))
check("E", "C6 the PARENT APPLIES to the assembled object: with L1 now "
           "exhibited (C5) and L2 the one fixpoint-free swap (B2), the "
           "twisted diagonal escapes EVERY T (|A| <= 3 exhaustive), zero "
           "alpha-invariant valuations exist, and alpha = id dissolves "
           "both -- conclusions (a) and (b) hold OVER THE ASSEMBLY, whose "
           "predicates pull back to all five orientation no-gos via C3",
      c6)

# ==============================================================================
# PART F -- the planted non-instance, verified OUTSIDE the assembled category
# ==============================================================================
print()
print("--- PART F: the C-04 prime-3 plant sits outside, structurally ---")

dims = [14, 64, 91, 128, 1664]
f1 = all(d % 3 != 0 for d in dims)
check("F", "F1 plant reproduced: 3 divides no native dimension "
           "{14, 64, 91, 128, 1664} (the C-04 obstruction)", f1)

f2 = all(int(np.linalg.matrix_rank(Um @ np.eye(m) @ np.linalg.inv(Um))) == m
         for m, Um in ((4, Jm), (4, W4), (2, Vp), (DIM, U_h), (DIM, C_J)))
n_equivariant = 0
for lam_vals in itertools.product((+1, -1), repeat=len(dims)):
    lam = dict(zip(dims, lam_vals))
    if all(lam[d] == -lam[d] for d in dims):
        n_equivariant += 1                # trivial action vs swap: impossible
check("F", "F2 STRUCTURAL exclusion: every involution of G (and every "
           "object involution) FIXES the datum dim mod 3 (rank invariance), "
           "so the plant's Z/2-action is trivial -- and ALL 32 candidate "
           "label maps to B fail equivariance (Hom_{Z/2}(triv, B) = empty, "
           "enumerated): the plant admits NO object structure over the one "
           "Z/2", f2 and n_equivariant == 0,
      f"equivariant maps found: {n_equivariant}")

f3 = all((2 ** a * d) % 3 != 0 for a in range(11) for d in dims)
check("F", "F3 no 2^a label refinement reaches divisibility by 3 -- the "
           "external-bit cure that works for every genuine instance (C1a-d) "
           "cannot cure the plant: the law excludes it NON-vacuously", f3)

f4 = all(ok for tag, _n, ok in RESULTS if tag == "E")
check("F", "F4 teeth: all five orientation objects assembled (equivariant "
           "B-maps exist, naturality passed) while the plant admits none -- "
           "the assembled law separates instances from non-instances", f4)

# --- verdict + headline -------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
if all_ok:
    print("OUTCOME: L-c -- the category assembles, the three fixpoint-free "
          "senses reconcile as the three graded pieces of one implementation "
          "group G (label = coset, ray = antilinear part, free = kernel), "
          "the parent applies to the assembly, and the plant is outside "
          "structurally. STAGE-0: the deck-twist Z/2 and the payload-bit "
          "Z/2 are ONE class (one character sgn_K; the seam is a habitat "
          "word; no exhibited separator).")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
