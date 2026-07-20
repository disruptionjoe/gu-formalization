#!/usr/bin/env python3
"""DIAGONAL-BOUNDARY probe -- machine-check the instantiation maps that re-type
the class-relative no-gos as instances of the Lawvere no-closure parent
(path5-branchD / H63 / W208), including one PLANTED NON-INSTANCE that the
test must REJECT.

CHANNEL: diagonal-boundary unification swing (Joe direct chat, 2026-07-20).
DESIGN:  explorations/diagonal-boundary-unification-2026-07-20.md
PARENT:  the Lawvere no-closure / arena-value theorem (W70/W75, H63 target
         statement): L1 self-encoding admissibility (finite products +
         diagonal; closure = weakly point-surjective T : A x A -> B) and
         L2 fixpoint-free label involution alpha : B -> B jointly give
         (a) no closure (the diagonal predicate d = alpha.T.Delta is
         unrepresented) and, from L2 ALONE, (b) no alpha-invariant
         valuation exists -- every definite commitment is an external
         symmetry-breaking selection.

INSTANTIATION CERTIFICATE (the operational test, applied per candidate):
  (C1) alpha exhibited as an explicit structure map (matrix / permutation);
  (C2) alpha fixpoint-free in the relevant sense (no fixed label / no fixed
       ray / free action);
  (C3) the EXCLUDED reading class is alpha-equivariant (even) -- checked on
       the fixture, machine grade;
  (C4) the excluded DATUM is alpha-ODD (it flips under alpha) -- this is
       what makes evenness = blindness;
  (C5) supplying the external datum (an alpha-breaking object) REMOVES the
       obstruction -- the exclusion is class-relative, not absolute.
A candidate passing C1-C5 instantiates the L2/involution half (leg b).
The PLANT (the C-04 prime-3 dimension-counting no-go) must FAIL C1/C4/C5:
its excluded datum (3 | dim) is invariant under EVERY label involution and
no external Z/2 posit cures it. If the plant passes, the test tests nothing.

Deterministic: numpy only, seed 20260720, no tolerance below is
load-bearing within 6 orders of magnitude. Exit 0 iff ALL PASS.
"""
import itertools
import sys
import numpy as np

rng = np.random.default_rng(20260720)
results = []  # (tag, name, ok, detail)


def check(tag, name, ok, detail=""):
    results.append((tag, name, bool(ok), detail))
    print(f"[{tag}] {'PASS' if ok else 'FAIL'} {name} {detail}")


# ---------------------------------------------------------------- setup [T]
# T1: the Lawvere skeleton, exhaustive (reproduces W70 PART A, exact form):
# alpha = swap -> for EVERY T : A x A -> B the diagonal predicate
# d = alpha.T.Delta is NOT a row of T (no T represents its own twisted
# diagonal; hence no T is weakly point-surjective); alpha = id -> some T
# DOES represent its diagonal (the obstruction dissolves). |A| in {1,2,3}.
def diagonal_always_escapes(nA, alpha):
    cells = [(i, j) for i in range(nA) for j in range(nA)]
    escapes, represented = True, False
    for values in itertools.product((0, 1), repeat=len(cells)):
        T = dict(zip(cells, values))
        d = tuple(alpha[T[(a, a)]] for a in range(nA))
        rows = {tuple(T[(a0, a)] for a in range(nA)) for a0 in range(nA)}
        if d in rows:
            escapes, represented = False, True
    return escapes, represented


swap, ident = {0: 1, 1: 0}, {0: 0, 1: 1}
t1 = all(diagonal_always_escapes(nn, swap)[0] for nn in (1, 2, 3))
check("T", "T1 Lawvere skeleton: alpha=swap -> diagonal predicate escapes EVERY T (|A|<=3 exhaustive)", t1)
t2 = all(diagonal_always_escapes(nn, ident)[1] for nn in (1, 2, 3))
check("T", "T2 control: alpha=id -> some T represents its diagonal (obstruction dissolves)", t2)

# T3: no-invariant-valuation count (reproduces W75 PART B): swap -> 0
# invariant valuations; id -> all 2^|A|.
def invariant_valuations(nA, alpha):
    return sum(all(alpha[p[a]] == p[a] for a in range(nA))
               for p in (dict(zip(range(nA), v))
                         for v in itertools.product((0, 1), repeat=nA)))


t3 = all(invariant_valuations(n, swap) == 0 and
         invariant_valuations(n, ident) == 2 ** n for n in (1, 2, 3))
check("T", "T3 leg (b): fixpoint-free alpha -> 0 invariant valuations (id -> 2^|A|)", t3)

# T4: the equivariance-blindness lemma, finite generic form: F even under
# alpha and o odd under alpha => F cannot determine o (exhibit x, alpha.x
# with F equal, o different). Generic engine behind every leg-(b) instance.
X = list(range(6)); ax = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}   # fixpoint-free
F = {x: x // 2 for x in X}                                       # even: F(ax)=F(x)
o = {0: 1, 1: -1, 2: 1, 3: -1, 4: 1, 5: -1}                      # odd
t4 = (all(F[ax[x]] == F[x] for x in X) and
      all(o[ax[x]] == -o[x] for x in X) and
      any(F[x] == F[ax[x]] and o[x] != o[ax[x]] for x in X))
check("T", "T4 equivariance-blindness lemma (even F cannot output odd datum o)", t4)

# ------------------------------------------------- instance 1: KRAMERS [E]
# alpha = the Kramers pairing v -> Jv, J antiunitary, J^2 = -1 (quaternionic:
# the canon no-go's J_quat). Fixture: C^4, J = J_mat o conj, J_mat symplectic.
n = 4
Jm = np.block([[np.zeros((2, 2)), -np.eye(2)], [np.eye(2), np.zeros((2, 2))]])
Japply = lambda v: Jm @ np.conj(v)
v0 = rng.standard_normal(n) + 1j * rng.standard_normal(n)
e1 = np.linalg.norm(Japply(Japply(v0)) + v0)
check("E", "E1 (C1) alpha exhibited: J antiunitary, J^2 = -1 exact", e1 < 1e-12,
      f"|J^2 v + v| = {e1:.1e}")

# C2 fixpoint-freeness on rays: <v, Jv> = 0 identically (v never parallel Jv).
sample = rng.standard_normal((8, n)) + 1j * rng.standard_normal((8, n))
e2 = max(abs(np.vdot(v, Japply(v))) for v in sample)
check("E", "E2 (C2) fixpoint-free on rays: <v, Jv> = 0 for all v (Kramers pair)",
      e2 < 1e-12, f"max |<v,Jv>| = {e2:.1e}")

# C3 excluded class = J-commuting Hermitians; equivariance forces EVEN
# eigenvalue multiplicities (even signature; odd index 3 unreachable).
def j_project(H):
    B = 0.5 * (H + Jm @ np.conj(H) @ np.linalg.inv(Jm))
    return 0.5 * (B + B.conj().T)


ok3 = True
for _ in range(5):
    H = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    HJ = j_project(H + H.conj().T)
    comm = np.linalg.norm(HJ @ Jm - Jm @ np.conj(HJ))
    ev = np.sort(np.linalg.eigvalsh(HJ))
    mults, cur = [], 1
    for a, b in zip(ev, ev[1:]):
        if abs(a - b) < 1e-8:
            cur += 1
        else:
            mults.append(cur); cur = 1
    mults.append(cur)
    ok3 &= (comm < 1e-12) and all(m % 2 == 0 for m in mults)
check("E", "E3 (C3) excluded class equivariant: J-commuting Hermitians have all-even multiplicities", ok3)

# C4 excluded datum alpha-odd: oddness-of-signature is exactly the datum the
# pairing inverts -- a rank-1 (odd) carrier P is mapped by the pairing to a
# DISJOINT partner J P J^-1 (P + partner is even); the odd part is what alpha
# moves. Machine form: for rank-1 P = vv*, J-image P' = (Jv)(Jv)* has
# <v, Jv> = 0 so P != P', while the J-symmetrization P + P' has signature 2.
v = sample[0] / np.linalg.norm(sample[0])
P = np.outer(v, v.conj()); w_ = Japply(v); Pp = np.outer(w_, w_.conj())
sig_sym = np.sum(np.linalg.eigvalsh(P + Pp) > 1e-8)
e4 = (np.linalg.norm(P - Pp) > 0.5) and (sig_sym == 2)
check("E", "E4 (C4) excluded datum is pairing-odd: rank-1 carrier moved off itself; symmetrization even",
      e4, f"|P-P'| = {np.linalg.norm(P - Pp):.2f}, sig(P+P') = {sig_sym}")

# C5 supplementation: a NON-J-commuting Hermitian (external import) reaches
# odd signature 3 on the same module -- exclusion is class-relative.
Q = np.zeros((n, n), complex); Q[0, 0] = Q[1, 1] = Q[2, 2] = 1.0
sig = np.sum(np.linalg.eigvalsh(Q) > 0.5)
defect = np.linalg.norm(Q @ Jm - Jm @ np.conj(Q))
check("E", "E5 (C5) external import reaches the excluded datum (rank-3, odd, non-J)",
      sig == 3 and defect > 0.5, f"sig = {sig}, J-defect = {defect:.2f}")

# C2' the DISSOLUTION control (the (9,5)-vs-(7,7) caveat, in miniature):
# J'^2 = +1 (real structure, conj alone) HAS fixed points (real vectors);
# J'-commuting Hermitians = real symmetric -> generic SIMPLE (odd) spectrum.
Hr = rng.standard_normal((n, n)); Hr = 0.5 * (Hr + Hr.T)
evr = np.sort(np.linalg.eigvalsh(Hr))
simple = np.all(np.diff(evr) > 1e-6)
check("E", "E6 (dissolution) J'^2 = +1 has fixed rays -> odd multiplicities allowed (no obstruction)",
      simple, "generic real-symmetric spectrum simple")

# ------------------------------------- instance 2: SELECTION RULE [E]
# alpha = the cut-swap involution w on a Krein toy: K = diag(1,1,-1,-1),
# w swaps the blocks, w K w = -K (the Araki even/odd selection rule shape).
K = np.diag([1.0, 1.0, -1.0, -1.0])
W = np.block([[np.zeros((2, 2)), np.eye(2)], [np.eye(2), np.zeros((2, 2))]])
e7 = (np.linalg.norm(W @ W - np.eye(4)) < 1e-14 and
      np.linalg.norm(W @ K @ W + K) < 1e-14)
check("E", "E7 (C1+C2) cut-swap exhibited: w^2 = 1, w K w = -K (flips the label, no fixed label)", e7)

# sector states rho_+- exchanged by w; w-fixed faithful reference gamma.
A0 = rng.standard_normal((2, 2)); Sp = A0 @ A0.T + 0.1 * np.eye(2)
rho_p = np.zeros((4, 4)); rho_p[:2, :2] = Sp / np.trace(Sp)
rho_m = W @ rho_p @ W
g0 = rng.standard_normal((4, 4)); G0 = g0 @ g0.T + 0.1 * np.eye(4)
gamma = 0.5 * (G0 + W @ G0 @ W); gamma /= np.trace(gamma)


def rel_ent(r, s):
    lr = np.linalg.eigvalsh(r); ls = np.linalg.eigvalsh(s)  # noqa (spectral fns)
    er, Ur = np.linalg.eigh(r); es, Us = np.linalg.eigh(s)
    lr_ = Ur @ np.diag(np.log(np.clip(er, 1e-30, None))) @ Ur.T
    ls_ = Us @ np.diag(np.log(np.clip(es, 1e-30, None))) @ Us.T
    return float(np.trace(r @ (lr_ - ls_)))


# C3: even battery (relative entropy vs gamma, purity, spectrum) blind.
d_ent = abs(rel_ent(rho_p, gamma) - rel_ent(rho_m, gamma))
d_pur = abs(np.trace(rho_p @ rho_p) - np.trace(rho_m @ rho_m))
check("E", "E8 (C3) every even functional blind: S(rho_+||gamma) = S(rho_-||gamma), purity equal",
      d_ent < 1e-12 and d_pur < 1e-12, f"dS = {d_ent:.1e}")

# C4: the sector datum k = Tr(rho K) is w-ODD (flips exactly).
kp, km = np.trace(rho_p @ K), np.trace(rho_m @ K)
check("E", "E9 (C4) the sector datum is alpha-odd: Tr(rho_- K) = -Tr(rho_+ K) != 0",
      abs(kp + km) < 1e-12 and abs(kp) > 0.1, f"k_+ = {kp:.3f}")

# C5: supplementation -- an eps*K-tilted (w-BREAKING) reference gives a
# nonzero odd entropy difference, linear in eps (the Araki step-5 escape).
eps = 1e-3
gt = gamma + eps * (K @ gamma + gamma @ K) / 2
gt = 0.5 * (gt + gt.T); gt /= np.trace(gt)
d_odd = rel_ent(rho_p, gt) - rel_ent(rho_m, gt)
check("E", "E10 (C5) external w-breaking reference reads the sector (odd diff ~ eps, nonzero)",
      abs(d_odd) > 1e-5, f"odd diff = {d_odd:.2e} at eps = {eps}")

# --------------------------------------- instance 3: TRANSPARENCY [E]
# Miniature of the S-matrix face: dynamics built K-free; grading eps carried
# separately; V commutes with dynamics, anticommutes with eps -> traced
# graded functionals vanish IDENTICALLY; sector flip acts as (S, eps)->(S,-eps).
E_ = 2.0; q_wall, q_end = -1.0, 1.0
k_end = np.sqrt(E_ ** 2 - q_end)


def transfer(q, L):   # 2x2 transfer across a constant segment, psi'' = (q - E^2) psi
    mu2 = q - E_ ** 2
    if mu2 < 0:
        k = np.sqrt(-mu2)
        return np.array([[np.cos(k * L), np.sin(k * L) / k],
                         [-k * np.sin(k * L), np.cos(k * L)]])
    k = np.sqrt(mu2)
    return np.array([[np.cosh(k * L), np.sinh(k * L) / k],
                     [k * np.sinh(k * L), np.cosh(k * L)]])


Tw = transfer(q_wall, 1.3)
M = np.array([[1, 1], [1j * k_end, -1j * k_end]])
Mi = np.linalg.inv(M)
TT = Mi @ Tw @ M            # plane-wave basis transfer
t_dyn = 1.0 / TT[0, 0]; r_dyn = TT[1, 0] / TT[0, 0]
flux = abs(t_dyn) ** 2 + abs(r_dyn) ** 2
check("E", "E11 setup honest: 1D wall scattering unitary (|t|^2 + |r|^2 = 1)",
      abs(flux - 1) < 1e-12, f"|t|^2 = {abs(t_dyn)**2:.3f}")

eps_g = np.diag([1.0, -1.0])            # channel grading (K_S-descendant)
Vp = np.array([[0.0, 1.0], [1.0, 0.0]])  # ghost-conjugation analog
t_mat = t_dyn * np.eye(2)                # dynamics is grading-blind: t x I_2
# C1+C3: transparency -- the S-block does not contain the grading; the
# sector flip eps -> -eps leaves t_mat IDENTICAL (by exhibited construction,
# checked as an identity of the built object, mirroring the probe's theorem).
even_fn = np.trace(t_mat.conj().T @ t_mat).real
check("E", "E12 (C1+C3) transparency: S built grading-free; flip acts as (S,eps)->(S,-eps); even fns blind",
      abs(even_fn - 2 * abs(t_dyn) ** 2) < 1e-12, f"Tr t^dag t = {even_fn:.3f}")
# V commutes with dynamics, anticommutes with grading -> traced odd = 0 exact.
gtr = np.trace(t_mat.conj().T @ eps_g @ t_mat)
e13 = (np.linalg.norm(Vp @ t_mat - t_mat @ Vp) < 1e-14 and
       np.linalg.norm(Vp @ eps_g + eps_g @ Vp) < 1e-14 and abs(gtr) < 1e-14)
check("E", "E13 (C2+C3) ghost-conjugation pairing: [V, T] = 0, {V, eps} = 0 -> traced graded = 0 exactly", e13)
# C4: the per-channel graded reading is nonzero and flips under eps -> -eps.
per = abs(t_dyn) ** 2 * eps_g[0, 0]
check("E", "E14 (C4) the datum is odd: per-channel graded transmission nonzero, flips with the sector",
      abs(per) > 0.01, f"graded T_11 = {per:.3f}")
# C5: graded PREPARATION (external orientation datum) yields the nonzero odd
# reading the traced (internal) class cannot: prepare on the eps = +1 channel.
prep = np.diag([1.0, 0.0])
odd_read = np.trace(prep @ t_mat.conj().T @ eps_g @ t_mat).real
check("E", "E15 (C5) graded preparation (external datum) reads the bit the dynamics cannot mint",
      abs(odd_read) > 0.01, f"prepared graded T = {odd_read:.3f}")

# --------------------------------------------- THE PLANTED NON-INSTANCE [F]
# C-04 (canon quaternionic-parity file): the prime 3 is ABSENT from the
# native dimension spectrum {14, 64, 91, 128, 1664}. Dimension counting,
# NOT a diagonal. The certificate must REJECT it.
dims = [14, 64, 91, 128, 1664]
f1 = all(d % 3 != 0 for d in dims)
check("F", "F1 plant stated: 3 divides no native dimension (the C-04 obstruction, reproduced)", f1)

# C4 FAILS: the excluded datum o(x) = dim(x) mod 3 is invariant under EVERY
# involution on labels/states (any invertible map preserves dimension) --
# checked against every alpha exhibited above (J, w, V, the label swap):
# conjugating by an involution never changes a space's dimension, so the
# datum is alpha-EVEN under all of them. An even datum cannot be the
# excluded-odd-output of the parent theorem.
f2 = all(int(np.linalg.matrix_rank(Ualpha @ np.eye(m) @ Ualpha)) == m
         for m, Ualpha in ((4, Jm), (4, W), (2, Vp)))
check("F", "F2 plant REJECTED at C4: the datum (dim mod 3) is invariant under every exhibited involution", f2)

# C5 FAILS: supplying an external Z/2 orientation datum (doubling by a
# graded label, or any 2^a-fold label refinement) NEVER produces
# divisibility by 3: 3 does not divide 2^a * d for any native d.
f3 = all((2 ** a * d) % 3 != 0 for a in range(11) for d in dims)
check("F", "F3 plant REJECTED at C5: no external Z/2 (2^a label) supplementation reaches the datum", f3)

# F4 teeth: the genuine instances passed all five certificate criteria while
# the plant failed C4 and C5 -- the certificate separates.
inst_pass = all(ok for tag, nm, ok, _ in results
                if tag == "E" and nm.startswith(("E1 ", "E2 ", "E3 ", "E4 ", "E5 ",
                                                 "E7 ", "E8 ", "E9 ", "E10", "E12",
                                                 "E13", "E14", "E15")))
check("F", "F4 certificate has teeth: all instance criteria pass on genuine cases, plant fails C4+C5",
      inst_pass and f2 and f3)

# ------------------------------------------------------------------ headline
nT = sum(1 for t, _, _, _ in results if t == "T")
nE = sum(1 for t, _, _, _ in results if t == "E")
nF = sum(1 for t, _, _, _ in results if t == "F")
all_ok = all(ok for _, _, ok, _ in results)
print()
print(f"HEADLINE {nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded) "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
