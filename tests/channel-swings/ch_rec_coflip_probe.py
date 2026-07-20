#!/usr/bin/env python3
"""CH-REC co-flip probe -- finite falsification test for H-REC.

CHANNEL: CH-REC (records / entropy / arrow of time -- fifth leg).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/channel-swing-CH-REC-2026-07-19.md
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

CLAIM UNDER TEST (CO-FLIP, finite version). Fix the zero-extra-import
construction class C_0: finite Krein space (K, <.,.>) with fundamental
symmetry J, transmitted orientation eps in {+1,-1}, physical projector
P_eps = (I + eps*J)/2, grading-preserving Krein-unitary dynamics, and a
record register whose increment is the record current
J_rec = eps * q(Psi), q(Psi) = eps<P_eps Psi, P_eps Psi> >= 0 (W229
lineage: current sourced by physical content; NO independent sign datum in
the record law). H-REC asserts: within C_0, every zero-import operation
that flips the record-accumulation direction also flips the physical-sector
selection, and conversely -- the Krein choice and the arrow cannot decouple
without paying a second Z/2 import.

KILL SEMANTICS. The probe enumerates the involution inventory of the finite
structure -- eps-flip (E), full covariant basis relabel (Rl), dynamics
reversal (T), record-law sign insert (M) -- and all 16 composites, over
multiple states and two dynamics choices. H-REC DIES here if any
ZERO-IMPORT composite splits the observable pair
(sector G-sign, record direction), i.e. flips exactly one of the two. If
the only splitting composites are those containing M (import cost exactly
one extra Z/2), H-REC survives at this grade and the N -> 5 boundary is
made exact: decoupling the arrow from the Krein sign costs precisely one
additional payload bit.

COMPOSITION INTERFACE (for the CH-QM graded-quotient toy, when built):
`record_register(qs, eps, mu=1)` consumes any nonnegative sector-charge
sequence and returns the register trajectory; `q_of(cfg, psi)` and
`sector_sign(cfg)` expose the observable pair. The CH-QM toy can drive this
register with its own graded-quotient charges without modification.

NONCLAIMS. Not a continuum entropy-production theorem; not a statement
about TaF finality polarity (bar(b) = finality-axis polarity remains OPEN
per ADAPTER2-01); not a verification that GU's actual W229 source law is a
member of C_0 (that membership -- typing constraint T3 -- is the named open
question this probe sharpens). Exact rational arithmetic; stdlib only.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, replace
from fractions import Fraction as Fr
from itertools import product

# ---------------------------------------------------------------------------
# exact linear algebra (tuples of tuples of Fractions)
# ---------------------------------------------------------------------------

N_DIM = 4  # signature (2, 2) Krein space


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
        sign = Fr(-1) ** j
        total += sign * a[0][j] * det(minor)
    return total


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
# base structure
# ---------------------------------------------------------------------------

G0 = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
J0 = G0  # fundamental symmetry in the standard basis
S_SWAP = mat([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])


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
VACUUM = vec([0, 0, 0, 0])
N_STEPS = 5


@dataclass(frozen=True)
class Config:
    G: tuple
    J: tuple
    U: tuple
    eps: int
    mu: int    # record-law sign datum; mu != +1 is an underived Z/2 import
    tdir: int  # dynamics direction: +1 forward, -1 reversed (zero-import)

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


def proj(cfg):
    return scal(Fr(1, 2), madd(ident(N_DIM), scal(cfg.eps, cfg.J)))


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
    """Sector charge: q = eps<P psi, P psi>_G >= 0 by construction in C_0."""
    w = matvec(proj(cfg), psi)
    val = cfg.eps * quad(cfg.G, w)
    if val < 0:
        raise ValueError("sector charge negative: config outside C_0")
    return val


def record_register(qs, eps, mu=1):
    """Register trajectory driven by nonnegative charges (composition API)."""
    n = Fr(0)
    out = [n]
    for q in qs:
        n = n + mu * eps * q
        out.append(n)
    return out


def trajectory(cfg, psi0, steps=N_STEPS):
    step = cfg.U if cfg.tdir == 1 else matT(cfg.U)
    psi = psi0
    qs = []
    for _ in range(steps):
        qs.append(q_of(cfg, psi))
        psi = matvec(step, psi)
    return qs


def observe(cfg, psi0):
    """Observable pair: (sector G-sign, record direction)."""
    qs = trajectory(cfg, psi0)
    ns = record_register(qs, cfg.eps, cfg.mu)
    return sector_sign(cfg), sgn(ns[-1])


def op_obs(cfg, psi0):
    """Operational (state-functional) observables only: charge and register
    trajectories. Used for the vacuum-witness check; excludes structural
    labels that no measurement on the state can access."""
    qs = trajectory(cfg, psi0)
    ns = record_register(qs, cfg.eps, cfg.mu)
    return tuple(qs), tuple(ns)


# ---------------------------------------------------------------------------
# involution inventory
# ---------------------------------------------------------------------------

def t_E(cfg, psi):
    """Payload-bit flip (zero import: it is the transmitted value)."""
    return replace(cfg, eps=-cfg.eps), psi


def t_Rl(cfg, psi):
    """Full covariant basis relabel by the block swap (gauge move, zero
    import): G -> S^T G S, J -> S^-1 J S, U -> S^-1 U S, psi -> S^-1 psi."""
    g = matmul(matT(S_SWAP), matmul(cfg.G, S_SWAP))
    j = matmul(S_SWAP, matmul(cfg.J, S_SWAP))
    u = matmul(S_SWAP, matmul(cfg.U, S_SWAP))
    return replace(cfg, G=g, J=j, U=u), matvec(S_SWAP, psi)


def t_T(cfg, psi):
    """Dynamics reversal (zero import)."""
    return replace(cfg, tdir=-cfg.tdir), psi


def t_M(cfg, psi):
    """Record-law sign insert (ONE Z/2 import: mu is underived)."""
    return replace(cfg, mu=-cfg.mu), psi


TRANSFORMS = {"E": t_E, "Rl": t_Rl, "T": t_T, "M": t_M}
ORDER = ("E", "Rl", "T", "M")


def apply_subset(subset, cfg, psi):
    for name in ORDER:
        if name in subset:
            cfg, psi = TRANSFORMS[name](cfg, psi)
    return cfg, psi


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


def base_config(eps, u, tdir=1):
    return Config(G=G0, J=J0, U=u, eps=eps, mu=1, tdir=tdir)


def main():
    # ----- [T] setup ------------------------------------------------------
    ok = True
    for eps, u, tdir in product((1, -1), (U_A, U_B), (1, -1)):
        adm, why = admissible(base_config(eps, u, tdir))
        ok = ok and adm
    check("T", "setup: base configurations are admissible (both eps, both U, both tdir)", ok)

    ok = True
    for eps in (1, -1):
        cfg = base_config(eps, U_A)
        sigma = sector_sign(cfg)
        # physical norm on the selected sector is eps * <.,.>: positive iff sigma == eps
        ok = ok and (sigma == eps)
    check("T", "setup: two-anchor freedom -- physical norm positive on the selected "
               "sector for BOTH orientations (structural anchor degeneracy, "
               "ADAPTER2-01 residue)", ok)

    # ----- [E] co-flip ----------------------------------------------------
    ok = True
    for eps, u, tdir in product((1, -1), (U_A, U_B), (1, -1)):
        cfg = base_config(eps, u, tdir)
        for psi in STATES:
            s0, d0 = observe(cfg, psi)
            cfg2, psi2 = t_E(cfg, psi)
            s1, d1 = observe(cfg2, psi2)
            ok = ok and (d0 != 0) and (s1 == -s0) and (d1 == -d0)
    check("E", "coflip: flipping the transmitted orientation flips the physical-sector "
               "G-sign AND the record-accumulation direction, together, in every "
               "tested configuration", ok)

    # ----- [E] involution inventory: zero-import composites are diagonal --
    all_subsets = [frozenset(c) for r in range(5)
                   for c in __import__("itertools").combinations(ORDER, r)]
    ok_diag = True
    ok_split = True
    for eps, u in product((1, -1), (U_A, U_B)):
        cfg = base_config(eps, u)
        for psi in STATES:
            s0, d0 = observe(cfg, psi)
            for subset in all_subsets:
                cfg2, psi2 = apply_subset(subset, cfg, psi)
                adm, _ = admissible(cfg2)
                if not adm:
                    ok_diag = False
                    continue
                s1, d1 = observe(cfg2, psi2)
                sector_flip = (s1 == -s0)
                dir_flip = (d1 == -d0 and d0 != 0)
                split = sector_flip != dir_flip
                cost = cfg2.imports
                if cost == 0:
                    ok_diag = ok_diag and not split
                    # predicted diagonal action: both flip iff E present
                    ok_diag = ok_diag and (sector_flip == ("E" in subset))
                if split:
                    ok_split = ok_split and (cost == 1) and ("M" in subset)
                if "M" in subset:
                    ok_split = ok_split and split and (cost == 1)
    check("E", "zero-import diagonal: all 8 zero-import composites of "
               "{eps-flip, relabel, time-reversal} act diagonally on "
               "(sector, direction) -- no zero-cost decoupling exists in the "
               "inventory (H-REC kill did NOT fire)", ok_diag)
    check("E", "split-costs-one: every composite that decouples sector from "
               "direction contains the record-law sign insert and carries import "
               "cost exactly one extra Z/2 -- the N->5 boundary made exact", ok_split)

    # ----- [F] controls ---------------------------------------------------
    cfg = base_config(1, U_A)
    cfg_m, _ = t_M(cfg, STATES[0])
    s0, d0 = observe(cfg, STATES[0])
    s1, d1 = observe(cfg_m, STATES[0])
    check("F", "mu-import-detected: the decoupled configuration (direction flipped, "
               "sector fixed) is flagged by the import counter as paying one "
               "underived Z/2", (s1 == s0) and (d1 == -d0) and cfg_m.imports == 1)

    bad = replace(base_config(1, U_A), J=matmul(S_SWAP, matmul(J0, S_SWAP)))
    adm, why = admissible(bad)
    check("F", "partial-relabel-rejected: flipping J without transporting the form "
               "fails the fundamental-symmetry gate (G.J loses positive "
               "definiteness) -- the relabel attack cannot split the pair", not adm)

    # ----- [E] time reversal is inert without the paid sign --------------
    ok = True
    for eps, u in product((1, -1), (U_A, U_B)):
        cfg = base_config(eps, u)
        for psi in STATES:
            s0, d0 = observe(cfg, psi)
            cfg2, psi2 = t_T(cfg, psi)
            s1, d1 = observe(cfg2, psi2)
            ok = ok and (s1 == s0) and (d1 == d0)
    check("E", "time-reversal-inert: reversing the dynamics alone changes neither "
               "sector nor record direction -- the arrow lives in the record law "
               "plus the orientation, not in the propagator; any zero-import "
               "arrow reversal must therefore flip eps (and with it the sector)", ok)

    # ----- [E] vacuum: one absence seen twice ----------------------------
    obs_plus = op_obs(base_config(1, U_A), VACUUM)
    obs_minus = op_obs(base_config(-1, U_A), VACUUM)
    zeroed = all(x == 0 for tup in obs_plus for x in tup)
    check("E", "vacuum-unwitnessed: Psi=0 gives zero record current and makes every "
               "operational observable orientation-independent -- the GR "
               "presentation (J=0 -> theta=0, no cancellation tensor) and the QM "
               "presentation (anchor choice operationally undetectable) are one "
               "absence", zeroed and obs_plus == obs_minus)

    ok = True
    for eps in (1, -1):
        cfg = base_config(eps, U_A)
        for psi in STATES:
            _, d = observe(cfg, psi)
            ok = ok and (d == eps)
    check("E", "witness-restored: nonzero physical content makes the record "
               "direction equal to the transmitted orientation -- the record "
               "current is the orientation's dynamical witness", ok)

    # ----- [E] curvature-conditioned surrogate (C10 hypothesis shape) ----
    v0 = vec([1, 0, 1, 0])
    ok = True
    for eps in (1, -1):
        mags = []
        for kappa in (0, 1, 2):
            cfg = base_config(eps, U_A)
            psi = tuple(Fr(kappa) * x for x in v0)
            qs = trajectory(cfg, psi)
            ns = record_register(qs, cfg.eps, cfg.mu)
            mags.append(abs(ns[-1]))
        ok = ok and mags[0] == 0 and mags[0] < mags[1] < mags[2]
    check("E", "curvature-surrogate: with a curvature-conditioned vacuum state "
               "Psi_vac = kappa*v (C10 surrogate), record production is zero at "
               "kappa=0 and strictly increasing in kappa -- records concentrate "
               "where the conditioning parameter does (surrogate only, not GR)", ok)

    # ----- [F] direction-erased register control -------------------------
    cfg_p = base_config(1, U_A)
    cfg_n = base_config(-1, U_A)
    qs_p = trajectory(cfg_p, STATES[0])
    qs_n = trajectory(cfg_n, STATES[0])
    abs_p = sgn(sum(abs(cfg_p.mu * cfg_p.eps * q) for q in qs_p))
    abs_n = sgn(sum(abs(cfg_n.mu * cfg_n.eps * q) for q in qs_n))
    true_p = sgn(record_register(qs_p, 1)[-1])
    true_n = sgn(record_register(qs_n, -1)[-1])
    check("F", "direction-erased control: a register built from |J_rec| carries no "
               "orientation information (same sign for both eps), while the true "
               "register's direction flips -- the direction is genuinely "
               "eps-sourced, not register bookkeeping",
          abs_p == abs_n == 1 and true_p == 1 and true_n == -1)

    # ----- summary --------------------------------------------------------
    e = sum(1 for t, _, ok in RESULTS if t == "E" and ok)
    f = sum(1 for t, _, ok in RESULTS if t == "F" and ok)
    t_ = sum(1 for t, _, ok in RESULTS if t == "T" and ok)
    failures = [(t, n) for t, n, ok in RESULTS if not ok]
    print()
    print(f"headline: {e} [E] + {f} [F] = {e + f}  (setup [T] = {t_}, excluded)")
    if failures:
        print("FAILURES:")
        for t, n in failures:
            print(f"  [{t}] {n}")
        print("VERDICT: CO-FLIP VIOLATED OR CONTROL BROKEN -- if a zero-import "
              "composite split the pair, H-REC is DEAD and N -> 5.")
        return 1
    print("VERDICT: CO-FLIP HOLDS IN C_0 AT THIS GRADE. No zero-import decoupling "
          "exists in the involution inventory; decoupling costs exactly one "
          "additional Z/2 import. H-REC survives conditionally; N <= 4 stands, "
          "conditional on GU's actual record law being a member of C_0 "
          "(typing constraint T3, open).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
