#!/usr/bin/env python3
"""H1 exhaustiveness probe -- machine check for the G-A1 theorem upgrade.

HARDENING SWING H1 (gap G-A1). The CH-REC co-flip (P1) and split-costs-one
(P2) results were ENUMERATED: proven over a 16-composite involution
inventory of a specific finite structure, with the standing R2 concession
that no exhaustiveness proof existed. This swing replaces the inventory
with a characterization. Proofs live in the design document
(explorations/hardening-h1-exhaustiveness-2026-07-19.md); the statements:

  L0 (decomposition).  Admissibility (J^2 = I, G.J symmetric positive
      definite) forces K = K_+ (+) K_- G-orthogonally, with G eps-definite
      on K_eps = ker(J - eps).
  L1 (sector rigidity).  sigma(X) = eps IDENTICALLY on the class: the
      G-sign of ran P_eps is eps for every admissible configuration -- an
      identity of admissibility, not an inventory fact.  This is exactly
      what kills every partial-flip attack (J -> -J alone, G -> -G alone)
      structurally rather than case-by-case.
  L2 (direction rigidity).  q(Psi) >= 0 for EVERY state of every
      admissible configuration; hence on witnessed trajectories
      sgn(Delta N) = mu * eps -- independent of U, tdir, basis, and state.
  THEOREM A (exhaustive co-flip).  (sigma, d) = (eps, eps) on the
      zero-import stratum; therefore EVERY map between zero-import
      witnessed configurations -- continuous or not, natural or not,
      invertible or not, dimension-preserving or not -- acts diagonally
      on the pair.  No zero-import operation splits, over ALL operations.
  THEOREM B (exact price).  sigma * d = mu on the envelope class: split
      <=> mu = -1 <=> import exactly 1, necessary AND sufficient.  The
      one-bit price is the fiber structure of the observable map; the
      import counter is itself observable (split parity).
  THEOREM C (structure).  The observable action of any operation family
      factors through Z/2 x Z/2 (generators: [E] co-flip, [M] paid
      split); the zero-import image is the diagonal Z/2, already realized
      by the enumerated {E}.  The kernel contains: all covariant relabels
      R_S (S in GL); the total form flip F : (G,J) -> (-G,-J) (the BENIGN
      MISS -- the ADAPTER2-01 anchor exchange as a standalone zero-import
      operation, absent from the CH-REC inventory; it fixes the pair
      while exchanging physical and mirror charge); all deformations of
      the fundamental symmetry within the contractible set J(G) (the D1
      C-operator continuum -- connected, hence observable-inert); all
      dynamics substitutions and tdir.

WHAT THIS SCRIPT CHECKS.  Finite witnesses on a WIDENED moduli sample the
original probe never left base for: random covariant relabels (dense G,
non-diagonal J), an exotic-J family built from strict-contraction angle
operators at fixed G0 (the fundamental-symmetry continuum), a sampled
rational path through that continuum with degenerate (maximal-commutant)
dynamics -- the D1 shape of the connected-component argument -- the
widened 32-composite table over {E, F, Rl, T, M}, propagator-independence
of the direction under deliberately NON-admissible dynamics, and failing
controls showing the positivity gate G.J > 0 is the load-bearing wall
(without it, sector rigidity has no floor).

NONCLAIMS.  Action grade, finite dimension: nothing here touches the
cohomological/BV grade (G-A2), the 192-dim lift (G-B1), D1 discharge
(G-B2), or membership of GU's actual law (T3/P9 -- unchanged, still the
load-bearing external condition).  Exact rational arithmetic; stdlib
only; deterministic (seeded).  [T] setup, [E] evidential, [F] failing
controls that must fire.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass, replace
from fractions import Fraction as Fr
from itertools import combinations, product

# ---------------------------------------------------------------------------
# exact linear algebra (tuples of tuples of Fractions)
# ---------------------------------------------------------------------------

N_DIM = 4  # signature (2, 2) instance; the theorems are stated for any (p, q)


def mat(rows):
    return tuple(tuple(Fr(x) for x in r) for r in rows)


def vec(xs):
    return tuple(Fr(x) for x in xs)


def ident(n):
    return tuple(tuple(Fr(1) if i == j else Fr(0) for j in range(n)) for i in range(n))


def matT(a):
    return tuple(tuple(col) for col in zip(*a))


def matmul(a, b):
    bt = matT(b)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt) for row in a)


def matvec(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def scal(c, a):
    return tuple(tuple(Fr(c) * x for x in row) for row in a)


def madd(a, b):
    return tuple(tuple(x + y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def det(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    total = Fr(0)
    for j in range(n):
        minor = tuple(row[:j] + row[j + 1:] for row in a[1:])
        total += (Fr(-1) ** j) * a[0][j] * det(minor)
    return total


def matinv(a):
    n = len(a)
    aug = [list(row) + [Fr(1) if i == j else Fr(0) for j in range(n)]
           for i, row in enumerate(a)]
    for col in range(n):
        piv = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return tuple(tuple(row[n:]) for row in aug)


def is_sym(a):
    return a == matT(a)


def is_pd(a):
    n = len(a)
    if not is_sym(a):
        return False
    for k in range(1, n + 1):
        sub = tuple(row[:k] for row in a[:k])
        if det(sub) <= 0:
            return False
    return True


def quad(g, v):
    return sum(x * y for x, y in zip(v, matvec(g, v)))


def sgn(x):
    return (x > 0) - (x < 0)


# ---------------------------------------------------------------------------
# the class (same axioms as ch_rec_coflip_probe.py)
# ---------------------------------------------------------------------------

G0 = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
J0 = G0


def rot(c, s):
    return ((Fr(c), -Fr(s)), (Fr(s), Fr(c)))


def blockdiag(b1, b2):
    z = ((Fr(0), Fr(0)), (Fr(0), Fr(0)))
    top = tuple(r1 + rz for r1, rz in zip(b1, z))
    bot = tuple(rz + r2 for rz, r2 in zip(z, b2))
    return top + bot


U_A = blockdiag(rot(Fr(3, 5), Fr(4, 5)), rot(Fr(5, 13), Fr(12, 13)))
U_B = blockdiag(rot(Fr(5, 13), Fr(12, 13)), rot(Fr(3, 5), Fr(4, 5)))

STATES = [vec([1, 2, 1, -1]), vec([1, 1, 1, 1]), vec([2, -1, 1, 3])]
N_STEPS = 4


@dataclass(frozen=True)
class Config:
    G: tuple
    J: tuple
    U: tuple
    eps: int
    mu: int    # the unique axiom slot for an underived sign; mu != +1 = 1 import
    tdir: int  # dynamics direction (zero-import)

    @property
    def imports(self):
        return 0 if self.mu == 1 else 1


def admissible(cfg):
    if not is_sym(cfg.G) or det(cfg.G) == 0:
        return False, "form not symmetric nondegenerate"
    if matmul(cfg.J, cfg.J) != ident(N_DIM):
        return False, "J not an involution"
    gj = matmul(cfg.G, cfg.J)
    if not is_pd(gj):
        return False, "G.J not positive definite (J not a fundamental symmetry)"
    if matmul(matT(cfg.U), matmul(cfg.G, cfg.U)) != cfg.G:
        return False, "U not Krein-unitary"
    if matmul(cfg.U, cfg.J) != matmul(cfg.J, cfg.U):
        return False, "U does not preserve the grading"
    if cfg.eps not in (1, -1):
        return False, "eps not a Z/2 value"
    return True, "ok"


def proj(cfg, eps=None):
    e = cfg.eps if eps is None else eps
    return scal(Fr(1, 2), madd(ident(N_DIM), scal(e, cfg.J)))


def sector_sign(cfg):
    """Intrinsic G-sign of the selected physical subspace ran(P_eps)."""
    p = proj(cfg)
    signs = set()
    for i in range(N_DIM):
        e = vec([1 if k == i else 0 for k in range(N_DIM)])
        v = matvec(p, e)
        if any(x != 0 for x in v):
            s = sgn(quad(cfg.G, v))
            if s == 0:
                raise ValueError("degenerate vector in selected sector")
            signs.add(s)
    if len(signs) != 1:
        raise ValueError("selected sector is not G-definite")
    return signs.pop()


def q_of(cfg, psi):
    """Sector charge; q >= 0 for EVERY state of every admissible config (L2)."""
    w = matvec(proj(cfg), psi)
    val = cfg.eps * quad(cfg.G, w)
    if val < 0:
        raise ValueError("sector charge negative: config outside the class")
    return val


def mirror_q(cfg, psi):
    """Mirror-sector charge (also >= 0 by L0); F exchanges q <-> mirror_q."""
    w = matvec(proj(cfg, -cfg.eps), psi)
    return -cfg.eps * quad(cfg.G, w)


def record_register(qs, eps, mu=1):
    n = Fr(0)
    out = [n]
    for q in qs:
        n = n + mu * eps * q
        out.append(n)
    return out


def trajectory(cfg, psi0, steps=N_STEPS):
    step = cfg.U if cfg.tdir == 1 else matinv(cfg.U)
    psi = psi0
    qs = []
    for _ in range(steps):
        qs.append(q_of(cfg, psi))
        psi = matvec(step, psi)
    return qs


def observe(cfg, psi0):
    """(sector G-sign, record direction, witnessed?)."""
    qs = trajectory(cfg, psi0)
    ns = record_register(qs, cfg.eps, cfg.mu)
    return sector_sign(cfg), sgn(ns[-1]), any(q > 0 for q in qs)


# ---------------------------------------------------------------------------
# operations
# ---------------------------------------------------------------------------

def op_E(cfg, psi):
    """Payload flip (zero import)."""
    return replace(cfg, eps=-cfg.eps), psi


def op_T(cfg, psi):
    """Dynamics reversal (zero import)."""
    return replace(cfg, tdir=-cfg.tdir), psi


def op_M(cfg, psi):
    """Record-law sign insert (ONE Z/2 import)."""
    return replace(cfg, mu=-cfg.mu), psi


def op_F(cfg, psi):
    """Total form flip (G,J) -> (-G,-J): the anchor exchange as a standalone
    operation (zero import).  The BENIGN MISS: absent from the CH-REC
    inventory as a generator; Theorem A forces it diagonal (in fact inert)."""
    return replace(cfg, G=scal(-1, cfg.G), J=scal(-1, cfg.J)), psi


def op_R(S, cfg, psi):
    """Full covariant relabel by arbitrary invertible S (gauge, zero import)."""
    Sinv = matinv(S)
    g = matmul(matT(S), matmul(cfg.G, S))
    j = matmul(Sinv, matmul(cfg.J, S))
    u = matmul(Sinv, matmul(cfg.U, S))
    return replace(cfg, G=g, J=j, U=u), matvec(Sinv, psi)


# ---------------------------------------------------------------------------
# widened moduli sample
# ---------------------------------------------------------------------------

def base_config(eps, u, tdir=1, mu=1):
    return Config(G=G0, J=J0, U=u, eps=eps, mu=mu, tdir=tdir)


def rand_S(rng):
    while True:
        S = mat([[rng.randint(-2, 2) for _ in range(N_DIM)] for _ in range(N_DIM)])
        if det(S) != 0:
            return S


def contraction_ok(T):
    """Strict contraction gate, exact: I - T^t T positive definite."""
    return is_pd(madd(ident(2), scal(-1, matmul(matT(T), T))))


def J_from_contraction(T):
    """Fundamental symmetry for G0 whose positive sector is graph(T):
    the angle-operator parametrization of J(G0) by strict contractions --
    a CONVEX (hence connected, contractible) parameter set."""
    Tt = matT(T)
    B = [[Fr(0)] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            B[i][j] = Fr(1) if i == j else Fr(0)
            B[i + 2][j] = T[i][j]
            B[i][j + 2] = Tt[i][j]
            B[i + 2][j + 2] = Fr(1) if i == j else Fr(0)
    B = tuple(tuple(r) for r in B)
    D = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    return matmul(B, matmul(D, matinv(B)))


T_START = mat([[Fr(1, 3), 0], [0, Fr(-1, 4)]])
T_END = mat([[0, Fr(1, 2)], [Fr(1, 3), 0]])


def T_path(t):
    return madd(scal(1 - t, T_START), scal(t, T_END))


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    status = "PASS" if ok else "FAIL"
    line = f"[{tag}] {status}  {name}"
    if detail and not ok:
        line += f"  ({detail})"
    print(line)


def main():
    rng = random.Random(20260719)

    # ----- widened config families ---------------------------------------
    bases = [base_config(eps, u, tdir)
             for eps, u, tdir in product((1, -1), (U_A, U_B), (1, -1))]

    relabels = []
    S_list = [rand_S(rng) for _ in range(6)]
    for S in S_list:
        c1, _ = op_R(S, base_config(1, U_A), STATES[0])
        c2, _ = op_R(S, base_config(-1, U_B), STATES[0])
        relabels += [c1, c2]

    exotics = []
    t_samples = [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1)]
    for t in t_samples:
        Tt = T_path(t)
        if not contraction_ok(Tt):
            exotics = None
            break
        Jt = J_from_contraction(Tt)
        for eps, u in product((1, -1), (ident(N_DIM), Jt)):
            exotics.append(Config(G=G0, J=Jt, U=u, eps=eps, mu=1, tdir=1))

    # ----- [T] setup ------------------------------------------------------
    ok = all(admissible(c)[0] for c in bases)
    check("T", "setup: base configurations admissible (both eps, both U, both tdir)", ok)

    ok = exotics is not None
    if ok:
        for c in relabels + exotics:
            adm, why = admissible(c)
            ok = ok and adm
        # construction soundness: exotic J really is a new fundamental symmetry
        j_start = J_from_contraction(T_START)
        j_end = J_from_contraction(T_END)
        ok = ok and matmul(j_start, j_start) == ident(N_DIM)
        ok = ok and j_start != J0 and j_end != J0 and j_start != j_end
    check("T", "setup: widened families admissible -- 12 random-relabel configs "
               "(dense G, non-diagonal J) and 20 exotic-J configs from the "
               "strict-contraction parametrization of J(G0); exotic J distinct "
               "from J0 and from each other at the path endpoints", ok)

    sample = bases + relabels + exotics

    # ----- [E] L1: sector rigidity across the widened sample -------------
    ok = True
    for c in sample:
        ok = ok and (sector_sign(c) == c.eps)
        # and for the opposite payload value on the SAME structure:
        ok = ok and (sector_sign(replace(c, eps=-c.eps)) == -c.eps)
    check("E", "L1 sector-rigidity: sigma = eps identically across the widened "
               "moduli sample (40 configs x both eps; dense forms, exotic "
               "fundamental symmetries) -- the G-sign of the selected sector is "
               "welded to eps by the positivity gate, everywhere, not just on "
               "the original probe's base structure", ok)

    # ----- [E] L2: direction rigidity, both mu strata ---------------------
    ok = True
    n_wit, n_unwit = 0, 0
    for c in sample:
        for m in (1, -1):
            cm = replace(c, mu=m)
            for psi in STATES:
                s, d, w = observe(cm, psi)
                if w:
                    n_wit += 1
                    ok = ok and (d == m * c.eps)
                else:
                    # unwitnessed = zero orientation witness (the P10 structure):
                    # a state confined to the mirror sector has NO direction --
                    # d = 0, not a split resource
                    n_unwit += 1
                    ok = ok and (d == 0)
    ok = ok and n_wit >= 200 and n_unwit >= 1
    check("E", "L2 direction-rigidity: sgn(Delta N) = mu * eps on every witnessed "
               "trajectory of every sampled configuration, in both mu strata -- "
               "the direction reads (mu, eps) and nothing else; the sample also "
               "contains unwitnessed instances (a state sitting exactly in a "
               "relabeled mirror sector), and there d = 0 exactly: an "
               "unwitnessed state has NO direction (P10's witness structure), "
               "never a wrong one", ok)

    # ----- [E] Theorem A: arbitrary-map diagonality -----------------------
    pool = []
    for c in sample:
        for psi in STATES:
            s, d, w = observe(c, psi)
            if w and c.imports == 0:
                pool.append((s, d))
    ok = len(pool) >= 100
    for _ in range(200):
        (s0, d0) = rng.choice(pool)
        (s1, d1) = rng.choice(pool)
        # an arbitrary operation instance: source |-> target, no structure assumed
        split = (s1 == -s0) != (d1 == -d0)
        ok = ok and (s0 == d0) and (s1 == d1) and not split
    check("E", "Theorem-A all-maps diagonality: 200 arbitrary ordered pairs of "
               "zero-import witnessed instances (any map whatever between them, "
               "no naturality or continuity assumed): (sigma, d) lies on the "
               "diagonal at BOTH ends, so no operation of any kind splits -- "
               "exhaustiveness holds over all operations, not an inventory", ok)

    # ----- [E] Theorem B: the stratum table / import is observable --------
    ok = True
    table_cfgs = [base_config(1, U_A), relabels[0], exotics[2]]
    for c in table_cfgs:
        for eps, m in product((1, -1), (1, -1)):
            cm = replace(c, eps=eps, mu=m)
            s, d, w = observe(cm, STATES[0])
            ok = ok and w and (s == eps) and (d == m * eps)
            ok = ok and (s * d == m)                      # import is observable
            ok = ok and ((s == d) == (cm.imports == 0))   # split parity = mu
    check("E", "Theorem-B exact price: (sigma, d) = (eps, mu*eps) over all four "
               "(eps, mu) strata on base, relabeled, and exotic configurations; "
               "sigma*d = mu -- the import counter IS the split parity, an "
               "observable; split <=> exactly one paid bit, necessary and "
               "sufficient", ok)

    # ----- [E] widened 32-composite table over {E, F, Rl, T, M} ----------
    OPS = {"E": op_E, "F": op_F,
           "Rl": (lambda cfg, psi, S=S_list[0]: op_R(S, cfg, psi)),
           "T": op_T, "M": op_M}
    ORDER = ("E", "F", "Rl", "T", "M")
    all_subsets = [frozenset(c) for r in range(6) for c in combinations(ORDER, r)]
    ok = len(all_subsets) == 32
    for c in table_cfgs:
        for psi in STATES:
            s0, d0, w0 = observe(c, psi)
            ok = ok and w0
            for subset in all_subsets:
                c2, psi2 = c, psi
                for name in ORDER:
                    if name in subset:
                        c2, psi2 = OPS[name](c2, psi2)
                adm, why = admissible(c2)
                ok = ok and adm
                s1, d1, w1 = observe(c2, psi2)
                ok = ok and w1
                sector_flip = (s1 == -s0)
                dir_flip = (d1 == -d0)
                split = sector_flip != dir_flip
                if c2.imports == 0:
                    ok = ok and not split
                    ok = ok and (sector_flip == ("E" in subset))
                if "M" in subset:
                    ok = ok and split and (c2.imports == 1)
                    # which split: M alone flips direction; M.E flips sector
                    ok = ok and (sector_flip == ("E" in subset))
                    ok = ok and (dir_flip == ("E" not in subset))
                ok = ok and (split == ("M" in subset))
    check("E", "widened composite table: all 32 composites of {eps-flip, total "
               "form flip F, random relabel, dynamics reversal, mu-insert} on "
               "base + relabeled + exotic configurations -- zero-import "
               "composites diagonal with flip iff E present; split iff M "
               "present, always at import cost exactly 1; F and Rl and T never "
               "contribute a flip (kernel)", ok)

    # ----- [E] the benign miss: F ----------------------------------------
    ok = True
    for c in table_cfgs + [exotics[0]]:
        cF, _ = op_F(c, STATES[0])
        adm, why = admissible(cF)
        ok = ok and adm and cF.imports == 0
        s0, d0, _ = observe(c, STATES[0])
        s1, d1, _ = observe(cF, STATES[0])
        ok = ok and (s1 == s0) and (d1 == d0)         # inert on the pair
        moved = False
        for psi in STATES:
            ok = ok and (q_of(cF, psi) == mirror_q(c, psi))  # anchor exchange
            moved = moved or (q_of(cF, psi) != q_of(c, psi))
        ok = ok and moved                              # yet not trivial
    check("E", "benign-miss F: the total form flip (G,J) -> (-G,-J) -- the "
               "ADAPTER2-01 anchor exchange as a standalone operation, absent "
               "from the CH-REC generator inventory -- is admissible, "
               "zero-import, INERT on (sector-sign, direction), and exchanges "
               "physical with mirror charge (so it is gauge for the pair while "
               "genuinely moving the charge assignment); Theorem A guaranteed "
               "its benignity in advance", ok)

    # ----- [E] the D1 continuum: connected, observable-inert --------------
    ok = True
    seen_J = set()
    for t in t_samples:
        Tt = T_path(t)
        ok = ok and contraction_ok(Tt)
        Jt = J_from_contraction(Tt)
        seen_J.add(Jt)
        for eps in (1, -1):
            for u in (ident(N_DIM), Jt):  # degenerate/maximal-commutant dynamics
                c = Config(G=G0, J=Jt, U=u, eps=eps, mu=1, tdir=1)
                adm, why = admissible(c)
                ok = ok and adm
                s, d, w = observe(c, STATES[0])
                ok = ok and w and (s == eps) and (d == eps)
    ok = ok and len(seen_J) == len(t_samples)
    check("E", "continuum-inert (the D1 shape): a rational path of five distinct "
               "fundamental symmetries J_t through the convex angle-operator "
               "parametrization of J(G0), under degenerate maximal-commutant "
               "dynamics (U = I and U = J_t): every point admissible, and "
               "(sigma, d) = (eps, eps) CONSTANT along the path -- the "
               "C-operator continuum is one connected component on which the "
               "observable pair is frozen; a bit needs two components, and the "
               "continuum has one; only the discrete data (eps, mu) move the "
               "observables", ok)

    # ----- [E] propagator independence (P3 at theorem grade) --------------
    while True:
        W = mat([[rng.randint(-2, 2) for _ in range(N_DIM)] for _ in range(N_DIM)])
        if det(W) != 0 and matmul(matT(W), matmul(G0, W)) != G0 \
                and matmul(W, J0) != matmul(J0, W):
            break
    ok = True
    for eps, m in product((1, -1), (1, -1)):
        c = base_config(eps, U_A, mu=m)
        for psi0 in STATES:
            psi, qs = psi0, []
            for _ in range(N_STEPS):
                qs.append(q_of(c, psi))     # q >= 0 holds for ANY state (L2)
                psi = matvec(W, psi)
            ns = record_register(qs, c.eps, c.mu)
            ok = ok and any(q > 0 for q in qs) and (sgn(ns[-1]) == m * eps)
    check("E", "propagator-independence: driving the register with a matrix that "
               "is deliberately NOT Krein-unitary and NOT grading-preserving "
               "(both dynamics axioms violated) still gives direction = mu*eps "
               "-- the arrow is stored entirely in (record law, eps), and "
               "dynamics-reversal inertness (P3) is the trivial special case of "
               "a theorem that holds for arbitrary dynamics", ok)

    # ----- [F] controls ---------------------------------------------------
    ok = True
    for c in [bases[0], relabels[0], relabels[1], exotics[0], exotics[3]]:
        adm_g, _ = admissible(replace(c, G=scal(-1, c.G)))
        adm_j, _ = admissible(replace(c, J=scal(-1, c.J)))
        ok = ok and not adm_g and not adm_j
    check("F", "partial-flips-rejected: G -> -G alone and J -> -J alone are "
               "inadmissible at EVERY sampled configuration (base, relabeled, "
               "exotic) -- the positivity gate G.J > 0 welds the two sign "
               "conventions together across the whole moduli sample; only the "
               "TOTAL flip F survives, and it is inert", ok)

    J_bad = mat([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
    cfg_bad = replace(base_config(1, U_A), J=J_bad, U=ident(N_DIM))
    adm, why = admissible(cfg_bad)
    gate_fired = (not adm) and ("positive definite" in why)
    ok = gate_fired and matmul(J_bad, J_bad) == ident(N_DIM)
    if ok:
        try:
            sector_sign(cfg_bad)   # bypass the gate: rigidity must collapse
            ok = False
        except ValueError:
            pass
    check("F", "gate-load-bearing: an involution J' with G.J' symmetric but "
               "INDEFINITE is rejected by the gate; bypassing the gate, the "
               "selected sector is not even G-definite (sector_sign raises) -- "
               "without G.J > 0 the sector rigidity L1 has no floor, so the "
               "exhaustiveness theorem's entire load rests on the class axioms, "
               "exactly where the referee re-score says it now lives", ok)

    c = base_config(1, U_A)
    cM, _ = op_M(c, STATES[0])
    s0, d0, _ = observe(c, STATES[0])
    s1, d1, _ = observe(cM, STATES[0])
    check("F", "mu-import-detected: the only splitting move flips the direction "
               "with the sector fixed and is flagged at import cost exactly 1",
          (s1 == s0) and (d1 == -d0) and cM.imports == 1)

    # ----- summary --------------------------------------------------------
    e = sum(1 for t, _, ok_ in RESULTS if t == "E" and ok_)
    f = sum(1 for t, _, ok_ in RESULTS if t == "F" and ok_)
    t_ = sum(1 for t, _, ok_ in RESULTS if t == "T" and ok_)
    failures = [(t, n) for t, n, ok_ in RESULTS if not ok_]
    print()
    print(f"headline: {e} [E] + {f} [F] = {e + f}  (setup [T] = {t_}, excluded)")
    if failures:
        print("FAILURES:")
        for t, n in failures:
            print(f"  [{t}] {n}")
        print("VERDICT: RIGIDITY BROKEN -- if sigma != eps or d != mu*eps "
              "anywhere on the widened sample, the exhaustiveness theorem's "
              "lemmas are false and P1/P2 fall back to enumerated grade.")
        return 1
    print("VERDICT: EXHAUSTIVENESS WITNESSED AT THEOREM SHAPE. sigma = eps and "
          "d = mu*eps identically on the widened moduli sample; (sigma, d) is "
          "a faithful copy of the discrete data (eps, mu); every zero-import "
          "operation -- enumerated or not, continuous or not -- is diagonal, "
          "and the split price is exactly one bit, necessary and sufficient. "
          "The benign miss F is inert; the D1 continuum is observable-inert; "
          "the load now rests on the class axioms (T3/P9 membership, G-A2 "
          "cohomological grade -- unchanged, still open).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
