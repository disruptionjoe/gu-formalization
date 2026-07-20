#!/usr/bin/env python3
"""H4 hardening probe -- class generalization (G-A3) + BV-grade co-flip (G-A2).

CHANNEL: hardening swing H4 (dossier gaps G-A3 + G-A2).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/hardening-h4-class-generalization-2026-07-19.md
EXTENDS: tests/channel-swings/ch_rec_coflip_probe.py (single (2,2) instance)
         tests/rs_bicomplex_spin95_connection_2form.py (verified BV bicomplex)
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

PART 1 (exact rational arithmetic, stdlib only for this part).
The class C(p,q; Phi) of finite oriented Krein systems with sign-free record
laws is axiomatized (A1-A5, see the design doc) and the co-flip +
split-costs-one statements are verified over a parametrized FAMILY:
signatures (1,1) (2,2) (3,3) (2,1) (3,1) (4,2), transported (de-standardized)
instances, several Krein-unitary dynamics per instance, four record-law
couplings Phi (linear / weighted multi-mode / quadratic / mixed), and an
ENLARGED zero-import operation inventory: eps-flip E, dynamics reversal T,
dynamics substitution Usub, generic covariant GL transports Rl_S (not just
the block swap), anchor swap Sw where p == q, against the paid record-law
sign insert M.  The abstract theorem (design doc, Lemmas 1-3 + Theorem)
predicts, for every instance and every composite: sector flips iff E in the
composite; direction flips iff exactly one of {E, M}; split iff M; import 1
iff M.  The sweep checks the prediction exactly.

PART 1b (exact Gaussian-rational complex arithmetic).
Per-signature-class TYPING models, cleanly separated:
  * quaternionic-type model ((9,5)-like): an antiunitary J_q with J_q^2 = -1
    COMMUTING with the grading -- sector-preserving; Krein sign preserved.
  * real-type model ((7,7)-like): an antiunitary T_c with T_c^2 = +1
    ANTICOMMUTING with the grading -- sector-EXCHANGING; Krein sign flipped;
    plus the fork twin T'_c = conj (commuting, sector-preserving) exhibiting
    that the typing annotation is Gram/antiunitary-convention dependent
    (GRAM-PIN-77 image) while the accounting identity is not.
Both models re-run the co-flip + split accounting unchanged.

PART 2 (numpy/scipy; the quaternionic-class channel only).
The BV-grade co-flip question on the verified Spin(9,5) bicomplex machinery
(rep imported from tests/oq_rk1_cl95_explicit_rep.py; connection dressing,
constraint co-differential, Koszul-Tate leg exactly as the verified
fixture), plus the Cl(1,3) miniature for the eigen-level constructions:
  (2a) the one genuinely NEW zero-import resource at cohomological grade --
       representative choice -- is exhibited as a split against any
       representative-level register reading (structural identity
       B K B^dag = 14 beta => the Krein form on the exact space has
       signature (64,64), so s-exact shifts drive the representative-level
       charge to either sign), and shown INERT against the canonical
       (harmonic/confined) reading;
  (2b) inventory diagonality at BV grade: anchor flip co-flips; ghost-sign,
       antifield-sign, xi -> -xi (symbol direction), W -> -W (connection
       flip) all act diagonally; xi-inertness is the BV image of P3
       (time-reversal inertness);
  (2c) the internal-mu question (H-REC-CAUS): a K-grade-reversing symmetry
       R of the retained structure (the unpaid mu) is searched for across
       three layers of structure and two loci; the empirical findings:
       * BARE symbol dynamics (no constraint): its +-sqrt(Q) eigenspaces
         are K-BALANCED -- the K-indefinite degenerate diagonalizable
         shape, exactly the d1 vacuum-anchor/Casimir degeneracy -- and a
         K-grade-reversing symmetry R' of the dynamics alone EXISTS: at
         the structure-free grade the grade flip is free (unpaid mu);
       * CONSTRAINED, gapped locus (generic non-null xi), even under the
         block-diagonal VZ decoupling: every eigengroup of the compressed
         sector dynamics is K-DEFINITE, and since the commutant of a
         diagonalizable operator preserves each eigenspace, NO
         dynamics-commuting sector-preserving operator can reverse the
         K-grade -- the constraint structure ([R', Pi] != 0) removes the
         bare-grade flip, and no unpaid mu exists at the gapped locus even
         decoupled: protection STRONGER than the H-REC-CAUS hypothesis;
       * degenerate locus (null xi, Q = 0): the fixture's own degenerate
         surface is the JORDAN wall (nilpotent sector dynamics, empty
         diagonalizable zero block -- every kernel vector a chain end):
         no admissible grading exists there at all (R1's
         positivity-unrescuable wall), so the direction observable is
         VACUOUS rather than split; the K-indefinite-diagonalizable
         SECTOR locus (where the coupled-vs-decoupled contrast would be
         decisive) is not realized by this fixture's symbol family --
         named residual, S_IG/G-B2 territory;
       * the ESCAPE IDENTITY: any surplus symmetry of the decoupled
         realization pays, in the coupled theory, a defect EXACTLY equal
         to its non-commutation with the escape term ([R, M_D] =
         [R, M_off] identically, since [R, M_dec] = 0) -- the
         causality-required coupling removes the decoupled variant's
         whole symmetry surplus, the reservoir any internal mu would
         have to come from.

Check tags: [T] setup/regression, [E] evidential, [F] failing controls that
must fire.  Exit 0 iff all checks pass.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, replace
from fractions import Fraction as Fr
from itertools import combinations, product

# ---------------------------------------------------------------------------
# shared check machinery
# ---------------------------------------------------------------------------

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    status = "PASS" if ok else "FAIL"
    line = f"[{tag}] {status}  {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ===========================================================================
# PART 1 -- exact rational linear algebra over the class C(p,q; Phi)
# ===========================================================================

def mat(rows):
    return tuple(tuple(Fr(x) for x in r) for r in rows)


def vec(xs):
    return tuple(Fr(x) for x in xs)


def ident(n):
    return tuple(tuple(Fr(1) if i == j else Fr(0) for j in range(n))
                 for i in range(n))


def zeros(n):
    return tuple(tuple(Fr(0) for _ in range(n)) for _ in range(n))


def matT(a):
    return tuple(tuple(col) for col in zip(*a))


def matmul(a, b):
    bt = matT(b)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt)
                 for row in a)


def matvec(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def scal(c, a):
    return tuple(tuple(Fr(c) * x for x in row) for row in a)


def madd(a, b):
    return tuple(tuple(x + y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def matinv(a):
    """Exact inverse by Gauss-Jordan over Fractions."""
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


def det(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    total = Fr(0)
    for j in range(n):
        minor = tuple(row[:j] + row[j + 1:] for row in a[1:])
        total += (Fr(-1) ** j) * a[0][j] * det(minor)
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


# ---- configurations -------------------------------------------------------

@dataclass(frozen=True)
class Cfg:
    """A full configuration of the class: structure + payload + register."""
    name: str
    G: tuple
    J: tuple
    Us: tuple          # available Krein-unitary dynamics
    modes: tuple       # mode projectors (commute with J)
    eps: int
    mu: int            # record-law sign datum; mu != +1 is one Z/2 import
    tdir: int
    uix: int

    @property
    def imports(self):
        return 0 if self.mu == 1 else 1

    @property
    def n(self):
        return len(self.G)


def admissible(cfg):
    n = cfg.n
    if not is_sym(cfg.G) or det(cfg.G) == 0:
        return False, "form not symmetric nondegenerate"
    if matmul(cfg.J, cfg.J) != ident(n):
        return False, "J not an involution"
    gj = matmul(cfg.G, cfg.J)
    if not is_pd(gj):
        return False, "G.J not positive definite (J not a fundamental symmetry)"
    for U in cfg.Us:
        if matmul(matT(U), matmul(cfg.G, U)) != cfg.G:
            return False, "U not Krein-unitary"
        if matmul(U, cfg.J) != matmul(cfg.J, U):
            return False, "U does not preserve the grading"
    for P in cfg.modes:
        if matmul(P, cfg.J) != matmul(cfg.J, P):
            return False, "mode projector does not commute with J"
    if cfg.eps not in (1, -1):
        return False, "eps not a Z/2 value"
    return True, "ok"


def proj(cfg):
    return scal(Fr(1, 2), madd(ident(cfg.n), scal(cfg.eps, cfg.J)))


def sector_sign(cfg):
    """Intrinsic G-sign of ran P_eps (Lemma 1 predicts == eps)."""
    p = proj(cfg)
    signs = set()
    for i in range(cfg.n):
        e = vec([1 if k == i else 0 for k in range(cfg.n)])
        v = matvec(p, e)
        if any(x != 0 for x in v):
            s = sgn(quad(cfg.G, v))
            if s == 0:
                raise ValueError("degenerate vector in selected sector")
            signs.add(s)
    if len(signs) != 1:
        raise ValueError("selected sector is not G-definite")
    return signs.pop()


def mode_charges(cfg, psi):
    """Per-mode sector charges q_i = eps<Pi_i P psi, Pi_i P psi>_G >= 0."""
    w = matvec(proj(cfg), psi)
    out = []
    for P in cfg.modes:
        u = matvec(P, w)
        val = cfg.eps * quad(cfg.G, u)
        if val < 0:
            raise ValueError("sector charge negative: outside the class")
        out.append(val)
    return tuple(out)


PHIS = {
    "linear": lambda qv: sum(qv),
    "weighted": lambda qv: sum(Fr(i + 1) * q for i, q in enumerate(qv)),
    "quadratic": lambda qv: sum(q * q for q in qv),
    "mixed": lambda qv: sum(qv) + sum(qv) ** 2,
}

N_STEPS = 4


def trajectory_charges(cfg, psi0):
    U = cfg.Us[cfg.uix]
    step = U if cfg.tdir == 1 else matinv(U)
    psi = psi0
    out = []
    for _ in range(N_STEPS):
        out.append(mode_charges(cfg, psi))
        psi = matvec(step, psi)
    return out

def observe(cfg, psi0, phi):
    """Observable pair (sector G-sign, record direction) for coupling phi."""
    n = Fr(0)
    for qv in trajectory_charges(cfg, psi0):
        n += cfg.mu * cfg.eps * phi(qv)
    return sector_sign(cfg), sgn(n)


def op_obs(cfg, psi0, phi):
    """Operational observables only (charge tuples + register trajectory)."""
    ns = [Fr(0)]
    qs = trajectory_charges(cfg, psi0)
    for qv in qs:
        ns.append(ns[-1] + cfg.mu * cfg.eps * phi(qv))
    return tuple(qs), tuple(ns)


# ---- instances ------------------------------------------------------------

def pyth_rot(c, s):
    return ((Fr(c), -Fr(s)), (Fr(s), Fr(c)))


def embed_block(n, i0, block):
    rows = [list(r) for r in ident(n)]
    k = len(block)
    for a in range(k):
        for b in range(k):
            rows[i0 + a][i0 + b] = block[a][b]
    return tuple(tuple(r) for r in rows)


def std_instance(name, p, q):
    n = p + q
    G = tuple(tuple(Fr(1 if i == j and i < p else (-1 if i == j else 0))
                    for j in range(n)) for i in range(n))
    J = G
    Us = [ident(n)]
    if p >= 2:
        Us.append(embed_block(n, 0, pyth_rot(Fr(3, 5), Fr(4, 5))))
    else:
        Us.append(embed_block(n, 0, ((Fr(-1),),)))
    if q >= 2:
        Us.append(embed_block(n, p, pyth_rot(Fr(5, 13), Fr(12, 13))))
    else:
        Us.append(embed_block(n, p, ((Fr(-1),),)))
    Us.append(matmul(Us[1], Us[2]))
    # modes: coordinate projectors commuting with J
    dA = [Fr(0)] * n
    dA[0] = Fr(1)
    dA[p] = Fr(1)
    PA = tuple(tuple(dA[i] if i == j else Fr(0) for j in range(n))
               for i in range(n))
    PB = madd(ident(n), scal(-1, PA))
    return Cfg(name=name, G=G, J=J, Us=tuple(Us), modes=(PA, PB),
               eps=1, mu=1, tdir=1, uix=0)


def transport(cfg, S, psi=None):
    """Full covariant transport by invertible S (Lemma 2 move)."""
    Si = matinv(S)
    G = matmul(matT(S), matmul(cfg.G, S))
    J = matmul(Si, matmul(cfg.J, S))
    Us = tuple(matmul(Si, matmul(U, S)) for U in cfg.Us)
    modes = tuple(matmul(Si, matmul(P, S)) for P in cfg.modes)
    out = replace(cfg, G=G, J=J, Us=Us, modes=modes)
    if psi is None:
        return out
    return out, matvec(Si, psi)


def generic_S(n, variant=0):
    """Deterministic invertible rational matrices (not isometries)."""
    rows = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    rows[0][0] = Fr(2)
    for i in range(1, n):
        rows[i][i - 1] = Fr(1, 2) if variant == 0 else Fr(-1, 3)
    if n >= 3:
        rows[n - 1][0] = Fr(1, 3) if variant == 0 else Fr(1, 5)
    return tuple(tuple(r) for r in rows)


def block_swap(p):
    n = 2 * p
    return tuple(tuple(Fr(1) if (j == i + p or j == i - p) else Fr(0)
                       for j in range(n)) for i in range(n))


def states_for(cfg):
    n = cfg.n
    pool = [[1, 2, -1, 3, 1, -2], [2, 1, 1, -1, 2, 1], [1, -1, 2, 1, -3, 2]]
    return [vec(s[:n]) for s in pool]


def part1():
    print("=" * 78)
    print("PART 1 -- class generalization sweep (exact rational)")
    print("=" * 78)

    instances = [std_instance("(1,1)", 1, 1),
                 std_instance("(2,2)", 2, 2),
                 std_instance("(3,3)", 3, 3),
                 std_instance("(2,1)", 2, 1),
                 std_instance("(3,1)", 3, 1),
                 std_instance("(4,2)", 4, 2)]
    # de-standardized (transported) family members
    t22 = transport(std_instance("(2,2)T", 2, 2), generic_S(4, 0))
    t21 = transport(std_instance("(2,1)T", 2, 1), generic_S(3, 1))
    instances += [t22, t21]
    dims = {c.name: (len(c.G)) for c in instances}
    print(f"family: {[c.name for c in instances]}  dims {dims}")

    # ----- [T] admissibility across the family ----------------------------
    ok = True
    for cfg in instances:
        for eps, tdir, uix in product((1, -1), (1, -1), range(len(cfg.Us))):
            adm, why = admissible(replace(cfg, eps=eps, tdir=tdir, uix=uix))
            if not adm:
                ok = False
                print(f"    inadmissible: {cfg.name} eps={eps} ({why})")
    check("T", "family setup: every instance admissible for both eps, both "
               "tdir, all dynamics", ok)

    # ----- [E] Lemma 1 (sector rigidity) across the family ----------------
    ok = True
    for cfg in instances:
        for eps in (1, -1):
            ok = ok and sector_sign(replace(cfg, eps=eps)) == eps
    check("E", "sector rigidity (Lemma 1): the selected sector's G-sign "
               "equals eps in EVERY instance -- signature- and "
               "dimension-blind; q >= 0 automatic (no exception raised)", ok)

    # ----- [E] co-flip across family x couplings --------------------------
    ok = True
    for cfg in instances:
        for eps, tdir, uix in product((1, -1), (1, -1), range(len(cfg.Us))):
            c0 = replace(cfg, eps=eps, tdir=tdir, uix=uix)
            for psi in states_for(cfg):
                if all(q == 0 for q in mode_charges(c0, psi)):
                    continue
                for pname, phi in PHIS.items():
                    s0, d0 = observe(c0, psi, phi)
                    c1 = replace(c0, eps=-eps)
                    s1, d1 = observe(c1, psi, phi)
                    ok = ok and d0 != 0 and s1 == -s0 and d1 == -d0
    check("E", "co-flip (family form): flipping eps flips sector AND record "
               "direction together in every instance, every signature, both "
               "time directions, all dynamics, all four record-law "
               "couplings", ok)

    # ----- [E] enlarged zero-import inventory diagonality -----------------
    # generators per instance: E, T, Usub, Rl(S_generic), [Sw if p == q], M
    ok_pred = True
    n_composites = 0
    for cfg in instances:
        n = cfg.n
        gens = ["E", "T", "Usub", "Rl"]
        p_dim = sum(1 for i in range(n) if cfg.J[i][i] == 1) \
            if cfg.J == cfg.G else None
        # anchor swap available only for standard (n,n) instances
        swap_ok = (cfg.name in ("(1,1)", "(2,2)", "(3,3)"))
        if swap_ok:
            gens.append("Sw")
        gens.append("M")

        Sgen = generic_S(n, 0)

        def apply_op(op, c, psi):
            if op == "E":
                return replace(c, eps=-c.eps), psi
            if op == "T":
                return replace(c, tdir=-c.tdir), psi
            if op == "Usub":
                return replace(c, uix=(c.uix + 1) % len(c.Us)), psi
            if op == "Rl":
                return transport(c, Sgen, psi)
            if op == "Sw":
                return transport(c, block_swap(len(c.G) // 2), psi)
            if op == "M":
                return replace(c, mu=-c.mu), psi
            raise ValueError(op)

        subsets = [c for r in range(len(gens) + 1)
                   for c in combinations(gens, r)]
        base = replace(cfg, eps=1, mu=1, tdir=1, uix=0)
        for psi in states_for(cfg)[:2]:
            if all(q == 0 for q in mode_charges(base, psi)):
                continue
            for pname in ("linear", "quadratic"):
                phi = PHIS[pname]
                s0, d0 = observe(base, psi, phi)
                for sub in subsets:
                    c, ps = base, psi
                    for op in sub:
                        c, ps = apply_op(op, c, ps)
                    adm, why = admissible(c)
                    if not adm:
                        ok_pred = False
                        print(f"    composite inadmissible: {cfg.name} {sub}")
                        continue
                    s1, d1 = observe(c, ps, phi)
                    sector_flip = (s1 == -s0)
                    dir_flip = (d1 == -d0 and d0 != 0)
                    pred_sector = ("E" in sub)
                    pred_dir = (("E" in sub) != ("M" in sub))
                    pred_import = 1 if ("M" in sub) else 0
                    good = (sector_flip == pred_sector
                            and dir_flip == pred_dir
                            and c.imports == pred_import
                            and ((sector_flip != dir_flip) == ("M" in sub)))
                    if not good:
                        ok_pred = False
                        print(f"    prediction failed: {cfg.name} {sub} "
                              f"phi={pname}")
                    n_composites += 1
    check("E", "inventory diagonality (Theorem, operational form): over the "
               "ENLARGED generator set {E, T, Usub, generic GL transport, "
               "anchor swap (n,n only)} x {M}, every composite in every "
               "instance obeys: sector flips iff E; direction flips iff "
               "exactly one of E,M; split iff M; import 1 iff M",
          ok_pred, detail=f"{n_composites} composites checked")

    # ----- [F] paid split + gate rejection --------------------------------
    cfg = replace(instances[1], eps=1)
    psi = states_for(cfg)[0]
    s0, d0 = observe(cfg, psi, PHIS["linear"])
    cm = replace(cfg, mu=-1)
    s1, d1 = observe(cm, psi, PHIS["linear"])
    check("F", "mu-import-detected: the record-law sign insert flips "
               "direction only and is flagged as one paid Z/2",
          s1 == s0 and d1 == -d0 and cm.imports == 1)

    ok = True
    for cfg in instances:
        S = generic_S(cfg.n, 0)
        bad = replace(cfg, J=matmul(matinv(S), matmul(cfg.J, S)))
        adm, _ = admissible(bad)
        ok = ok and not adm
    check("F", "partial-relabel-rejected (family form): moving J without "
               "transporting the rest fails the admissibility gate in EVERY "
               "instance -- the relabel attack cannot split the pair "
               "anywhere in the class", ok)

    # ----- [E] vacuum + mirror-only content -------------------------------
    ok = True
    for cfg in instances:
        vac = vec([0] * cfg.n)
        a = op_obs(replace(cfg, eps=1), vac, PHIS["linear"])
        b = op_obs(replace(cfg, eps=-1), vac, PHIS["linear"])
        flat = [x for tup in a for grp in tup for x in
                (grp if isinstance(grp, tuple) else (grp,))]
        ok = ok and a == b and all(x == 0 for x in flat)
    check("E", "vacuum-unwitnessed (family form): Psi = 0 gives identical, "
               "identically-zero operational observables for both anchors "
               "in every instance", ok)

    ok = True
    for name, p, q in (("(2,2)", 2, 2), ("(2,1)", 2, 1), ("(3,1)", 3, 1)):
        cfg = std_instance(name, p, q)
        mirror = vec([0] * p + [1] * q)   # entirely in the -1 eigenspace
        c0 = replace(cfg, eps=1)
        qs, ns = op_obs(c0, mirror, PHIS["linear"])
        ok = ok and all(x == 0 for qv in qs for x in qv) and ns[-1] == 0
    check("E", "mirror-only content drives no record: a nonzero state with "
               "zero eps-sector content has q = 0 and direction 0 -- the "
               "register sees only the selected sector's content", ok)

    # ----- [T] anchor-exchange is an (n,n) phenomenon ----------------------
    note = []
    for name, p, q in (("(2,1)", 2, 1), ("(3,1)", 3, 1), ("(4,2)", 4, 2)):
        note.append(f"{name}: sector dims {p} vs {q}")
    check("T", "anchor-exchange scope: for p != q the two anchors select "
               "sectors of different dimension -- no linear isomorphism can "
               "exchange them; the RELATIONAL anchor symmetry is an (n,n) "
               "feature, while co-flip + price hold for all (p,q)",
          True, detail="; ".join(note))
    return True


# ===========================================================================
# PART 1b -- per-signature-class typing models (exact Gaussian rationals)
# ===========================================================================

class CF:
    """Gaussian-rational complex number (exact)."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        return CF(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CF(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CF(self.re * o.re - self.im * o.im,
                  self.re * o.im + self.im * o.re)

    def __neg__(self):
        return CF(-self.re, -self.im)

    def conj(self):
        return CF(self.re, -self.im)

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return f"({self.re}+{self.im}i)"


def cmat(rows):
    out = []
    for r in rows:
        row = []
        for x in r:
            if isinstance(x, tuple):
                row.append(CF(x[0], x[1]))
            else:
                row.append(CF(x))
        out.append(tuple(row))
    return tuple(out)


def cvec(xs):
    return tuple(CF(x[0], x[1]) if isinstance(x, tuple) else CF(x)
                 for x in xs)


def cmatvec(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), CF(0)) for row in a)


def cconjvec(v):
    return tuple(x.conj() for x in v)


def cherm(g, v, w=None):
    """Hermitian form v^dag G w (G real diagonal-ish stored as CF matrix)."""
    if w is None:
        w = v
    gw = cmatvec(g, w)
    return sum((x.conj() * y for x, y in zip(v, gw)), CF(0))


def part1b():
    print()
    print("=" * 78)
    print("PART 1b -- per-signature-class typing models (exact complex)")
    print("=" * 78)

    # ---------- quaternionic-type model ((9,5)-like typing) ---------------
    # C^4, G = J = diag(1,1,-1,-1); J_q(v) = Om.conj(v), Om = Om2 (+) Om2.
    G4 = cmat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    Om = cmat([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])

    def Jq(v):
        return cmatvec(Om, cconjvec(v))

    tests_v = [cvec([1, 2, (0, 1), -1]), cvec([(1, 1), 0, 2, (0, -1)]),
               cvec([0, (2, 1), 1, 3])]
    ok = all(all((Jq(Jq(v))[i] + v[i]).is_zero() for i in range(4))
             for v in tests_v)
    check("E", "quaternionic-type model: J_q^2 = -1 (antiunitary, "
               "quaternionic structure)", ok)

    def Pq(eps, v):
        # J = G4 diagonal real: P_eps = (I + eps J)/2 acts coordinatewise
        keep = (0, 1) if eps == 1 else (2, 3)
        return tuple(v[i] if i in keep else CF(0) for i in range(4))

    ok = True
    for v in tests_v:
        for eps in (1, -1):
            a = Jq(Pq(eps, v))
            b = Pq(eps, Jq(v))
            ok = ok and all((a[i] - b[i]).is_zero() for i in range(4))
    check("E", "quaternionic-type model: [J_q, P_eps] = 0 -- the bit is "
               "J_q-COMMUTING (sector-preserving typing; the (9,5) "
               "annotation, cf. canon C07 / CH-QM A4)", ok)

    ok = True
    for v in tests_v:
        a = cherm(G4, Jq(v))
        b = cherm(G4, v)
        ok = ok and (a - b).is_zero()
    check("E", "quaternionic-type model: J_q preserves the Krein sign "
               "(G(J_q v, J_q v) = G(v, v) exactly)", ok)

    # accounting on the complex instance: U = conjugate-paired phases
    U4 = cmat([[(Fr(3, 5), Fr(4, 5)), 0, 0, 0],
               [0, (Fr(3, 5), Fr(-4, 5)), 0, 0],
               [0, 0, (Fr(5, 13), Fr(12, 13)), 0],
               [0, 0, 0, (Fr(5, 13), Fr(-12, 13))]])

    def cobserve(g, u, eps, mu, psi, steps=4):
        n = Fr(0)
        cur = psi
        for _ in range(steps):
            w = Pq(eps, cur)
            qv = eps * cherm(g, w).re
            assert cherm(g, w).im == 0 and qv >= 0
            n += mu * eps * qv
            cur = cmatvec(u, cur)
        # sector sign: G-sign of ran P_eps (rigidity: = eps)
        return eps, sgn(n)

    ok = True
    for psi in tests_v:
        s0, d0 = cobserve(G4, U4, 1, 1, psi)
        s1, d1 = cobserve(G4, U4, -1, 1, psi)
        sm, dm = cobserve(G4, U4, 1, -1, psi)
        ok = ok and s1 == -s0 and d1 == -d0 and sm == s0 and dm == -d0
    # [U, J_q] check
    okU = True
    for v in tests_v:
        a = Jq(cmatvec(U4, v))
        b = cmatvec(U4, Jq(v))
        okU = okU and all((a[i] - b[i]).is_zero() for i in range(4))
    check("E", "quaternionic-type model: co-flip + split-costs-one hold "
               "verbatim with quaternionic-compatible dynamics "
               "([U, J_q] = 0) -- same accounting identity, J-commuting "
               "typing", ok and okU)

    # ---------- real-type model ((7,7)-like typing) ------------------------
    # C^2, G = J = diag(1,-1); T_c(v) = sx.conj(v) with sx = [[0,1],[1,0]].
    G2 = cmat([[1, 0], [0, -1]])
    sx = cmat([[0, 1], [1, 0]])

    def Tc(v):
        return cmatvec(sx, cconjvec(v))

    tv2 = [cvec([1, (0, 1)]), cvec([(2, 1), -1]), cvec([1, 3])]
    ok = all(all((Tc(Tc(v))[i] - v[i]).is_zero() for i in range(2))
             for v in tv2)
    check("E", "real-type model: T_c^2 = +1 (antiunitary, real class)", ok)

    def P2(eps, v):
        keep = (0,) if eps == 1 else (1,)
        return tuple(v[i] if i in keep else CF(0) for i in range(2))

    ok = True
    for v in tv2:
        for eps in (1, -1):
            a = Tc(P2(eps, v))
            b = P2(-eps, Tc(v))
            ok = ok and all((a[i] - b[i]).is_zero() for i in range(2))
    check("E", "real-type model: T_c P_eps = P_(-eps) T_c -- the bit is "
               "SECTOR-EXCHANGING under the native antiunitary (the (7,7) "
               "canonical-Gram annotation, cf. CH-SIG-77 1c/1g)", ok)

    ok = True
    for v in tv2:
        ok = ok and (cherm(G2, Tc(v)) + cherm(G2, v)).is_zero()
    check("E", "real-type model: T_c FLIPS the Krein sign "
               "(G(T v, T v) = -G(v, v)) -- the C0-control structure "
               "realized natively", ok)

    ok = True
    for v in tv2:
        for eps in (1, -1):
            w = P2(eps, v)
            qe = eps * cherm(G2, w).re
            wt = P2(-eps, Tc(v))
            qt = (-eps) * cherm(G2, wt).re
            ok = ok and qe == qt
    check("E", "real-type model: q_(-eps)(T v) = q_eps(v) -- the antiunitary "
               "implements the anchor exchange (relational move), not a "
               "split", ok)

    # fork twin: T'_c = plain conjugation -- commuting typing, same instance
    def Tp(v):
        return cconjvec(v)

    ok = True
    for v in tv2:
        for eps in (1, -1):
            a = Tp(P2(eps, v))
            b = P2(eps, Tp(v))
            ok = ok and all((a[i] - b[i]).is_zero() for i in range(2))
        ok = ok and (cherm(G2, Tp(v)) - cherm(G2, v)).is_zero()
    check("E", "real-type fork twin: T'_c = conj on the SAME instance is "
               "sector-PRESERVING and Krein-sign-preserving -- the typing "
               "annotation depends on the antiunitary/Gram convention "
               "(GRAM-PIN-77 image); the accounting does not", ok)

    U2 = cmat([[(Fr(3, 5), Fr(4, 5)), 0], [0, (Fr(5, 13), Fr(12, 13))]])
    ok = True
    for psi in tv2:
        def obs2(eps, mu):
            n = Fr(0)
            cur = psi
            for _ in range(4):
                w = P2(eps, cur)
                qv = eps * cherm(G2, w).re
                assert qv >= 0
                n += mu * eps * qv
                cur = cmatvec(U2, cur)
            return eps, sgn(n)
        s0, d0 = obs2(1, 1)
        s1, d1 = obs2(-1, 1)
        sm, dm = obs2(1, -1)
        ok = ok and s1 == -s0 and d1 == -d0 and sm == s0 and dm == -d0
    check("E", "real-type model: co-flip + split-costs-one hold verbatim -- "
               "same accounting identity, sector-exchanging typing", ok)
    return True


# ===========================================================================
# PART 2 -- BV-grade co-flip on the verified bicomplex machinery (numpy)
# ===========================================================================

def part2():
    import numpy as np
    from scipy.linalg import expm

    HERE = os.path.dirname(os.path.abspath(__file__))
    TESTS = os.path.dirname(HERE)
    if TESTS not in sys.path:
        sys.path.insert(0, TESTS)
    import oq_rk1_cl95_explicit_rep as cl95

    def fro(A):
        return float(np.linalg.norm(A))

    def null_basis(M, tol=1e-9):
        u, s, vh = np.linalg.svd(M, full_matrices=True)
        smax = s.max() if s.size else 0.0
        rank = int((s > tol * max(smax, 1.0)).sum())
        return vh[rank:].conj().T

    def range_basis(M, tol=1e-9):
        u, s, vh = np.linalg.svd(M, full_matrices=False)
        smax = s.max() if s.size else 0.0
        rank = int((s > tol * max(smax, 1.0)).sum())
        return vh[:rank].conj().T   # orthonormal basis of row space = im(M^dag)

    print()
    print("=" * 78)
    print("PART 2 -- BV-grade co-flip (quaternionic-class channel: the")
    print("verified Spin(9,5) bicomplex fixture + its Cl(1,3) miniature)")
    print("=" * 78)

    # ---------- (9,5) fixture ---------------------------------------------
    N = 14
    n_pairs = 7
    dim = 2 ** n_pairs
    Gm = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [Gm[a] if eta[a] > 0 else 1j * Gm[a] for a in range(N)]
    VS = N * dim

    ok = True
    for a in range(N):
        r = e[a] @ e[a] - eta[a] * np.eye(dim)
        ok = ok and fro(r) < 1e-12
    r = e[0] @ e[9] + e[9] @ e[0]
    ok = ok and fro(r) < 1e-12
    check("T", "(9,5) rep sanity: Clifford relations (spot check) on the "
               "verified rep", ok)

    beta = np.eye(dim, dtype=complex)
    for a in range(9):
        beta = beta @ e[a]
    XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
                   1.1, 0.3, 2.2, 1.7, 0.9, 1.3])
    cxi = sum(XI[a] * e[a] for a in range(N))
    ok = (fro(beta - beta.conj().T) < 1e-12
          and fro(beta @ beta - np.eye(dim)) < 1e-12
          and fro(beta @ cxi.conj().T @ beta - cxi) < 1e-12)
    check("T", "(9,5) Krein Gram: beta = e_0..e_8 Hermitian, beta^2 = I, "
               "and the symbol c(xi) is K-Hermitian (beta c^dag beta = c)",
          ok)

    K = np.kron(np.diag(eta).astype(complex), beta)   # Krein form on V (x) S

    Sig09 = 0.25 * (e[0] @ e[9] - e[9] @ e[0])
    GW = expm(0.8 * Sig09)   # named a-priori single-boost connection
    ok = fro(beta @ GW.conj().T @ beta @ GW - np.eye(dim)) < 1e-9
    check("T", "(9,5) connection dressing G_W = exp(0.8 Sigma_09) is "
               "K-orthogonal (spin generators are K-skew)", ok)

    Gamma = np.hstack(e)                                # 128 x 1792
    B = np.hstack([e[a] @ GW for a in range(N)])        # dressed constraint
    gram = B @ B.conj().T
    Pi = np.eye(VS, dtype=complex) - B.conj().T @ np.linalg.pinv(gram) @ B
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])
    A_W = Pi @ gauge
    M_KT = B.conj().T @ B

    # blockwise closure of s (the only two candidate nonzero s^2 blocks)
    c1 = fro(M_KT @ A_W)          # (s_KT s_long) on c*
    c2 = fro(A_W.conj().T @ M_KT)  # (s_long s_KT) on psi*
    rk_A = int(np.linalg.matrix_rank(A_W, tol=1e-7))
    rk_M = int(np.linalg.matrix_rank(M_KT, tol=1e-7))
    raw = fro(M_KT @ gauge)       # raw-generator control must BREAK closure
    check("T", "(9,5) bicomplex closure (blockwise): ||M_KT A_W|| and "
               "||A_W^dag M_KT|| both ~ 0 with non-vacuous leg ranks",
          c1 < 1e-8 and c2 < 1e-8 and rk_A > 0 and rk_M > 0,
          detail=f"c1={c1:.2e} c2={c2:.2e} ranks A_W={rk_A} M_KT={rk_M}")
    check("F", "(9,5) raw-generator control: the undressed gauge map breaks "
               "closure (||M_KT gauge|| >> 0) -- the bicomplex checks have "
               "teeth", raw > 1.0, detail=f"raw={raw:.2f}")

    # ---------- (2a) the representative-choice attack ----------------------
    BKB = B @ K @ B.conj().T
    resid_14beta = fro(BKB - 14.0 * beta) / fro(14.0 * beta)
    check("E", "STRUCTURAL IDENTITY: B K B^dag = 14 beta exactly -- the "
               "Krein form restricted to the s-exact space has signature "
               "(64, 64): INDEFINITE, so representative-level charges are "
               "unboundedly shiftable by zero-import s-exact moves",
          resid_14beta < 1e-9, detail=f"rel resid={resid_14beta:.2e}")

    Eb = range_basis(B)                       # 1792 x 128, im(B^dag) = exact
    stacked = np.vstack([B, gauge.conj().T])  # closed & harmonic: ker of this
    Hb = null_basis(stacked)                  # 1792 x dim(harmonic)
    dimH = Hb.shape[1]
    closed_dim = null_basis(gauge.conj().T @ Pi).shape[1]
    check("T", "(9,5) cohomology bookkeeping: harmonic dim + exact dim = "
               "closed dim at ghost number 0",
          dimH + Eb.shape[1] == closed_dim,
          detail=f"harmonic={dimH} exact={Eb.shape[1]} closed={closed_dim}")

    KH = Hb.conj().T @ K @ Hb
    evH = np.linalg.eigvalsh(0.5 * (KH + KH.conj().T))
    npos = int((evH > 1e-9).sum())
    nneg = int((evH < -1e-9).sum())
    nnul = dimH - npos - nneg
    check("E", "(9,5) Krein signature of the HARMONIC (gh-0 physical) "
               "space: both grades present and nondegenerate -- the "
               "confined reading is well-posed and two-sided content exists",
          npos > 0 and nneg > 0 and nnul == 0,
          detail=f"signature (+{npos}, -{nneg}, 0:{nnul})")

    # a K-positive harmonic state
    rng = np.random.default_rng(20260719)
    sub = Hb @ rng.normal(size=(dimH, 8))
    sub, _ = np.linalg.qr(sub)
    gsub = sub.conj().T @ K @ sub
    w, V = np.linalg.eigh(0.5 * (gsub + gsub.conj().T))
    x_pos = sub @ V[:, -1]
    c_pos = float(np.real(x_pos.conj() @ K @ x_pos))

    wneg, Vneg = np.linalg.eigh(beta)
    u = Vneg[:, 0]                      # beta u = -u
    x_e = B.conj().T @ u
    x_e = x_e / np.linalg.norm(x_e)
    c_e = float(np.real(x_e.conj() @ K @ x_e))

    lin = float(np.real(x_e.conj() @ K @ x_pos))
    lam = 1.0
    while c_pos + 2 * lam * lin + lam * lam * c_e > -0.5 * abs(c_pos):
        lam *= 2.0
        if lam > 1e9:
            break
    y = x_pos + lam * x_e
    c_y = float(np.real(y.conj() @ K @ y))
    same_class = fro(Hb @ (Hb.conj().T @ y) - x_pos)
    still_closed = fro(gauge.conj().T @ Pi @ y)
    in_exact = fro((y - x_pos) - Eb @ (Eb.conj().T @ (y - x_pos)))
    check("E", "REPRESENTATIVE-SHIFT SPLIT (the new BV-grade zero-import "
               "attack): an s-exact shift flips the representative-level "
               "Krein charge's SIGN while leaving the cohomology class and "
               "the sector selection untouched -- any register that reads "
               "raw representatives is split at zero import",
          c_pos > 0 and c_e < 0 and c_y < 0 and same_class < 1e-8
          and still_closed < 1e-7 and in_exact < 1e-8,
          detail=f"charge {c_pos:.3f} -> {c_y:.3f} (lam={lam:.1f}); "
                 f"class drift {same_class:.1e}")

    c_canon = float(np.real((Hb @ (Hb.conj().T @ y)).conj()
                            @ K @ (Hb @ (Hb.conj().T @ y))))
    check("E", "CANONICAL (harmonic/confined) READING IMMUNE: the harmonic "
               "projection annihilates the shift exactly; the descended "
               "charge is representative-independent -- the attack has zero "
               "grip on descended observables",
          abs(c_canon - c_pos) < 1e-8,
          detail=f"canonical charge {c_canon:.6f} vs {c_pos:.6f}")

    lin_full = fro(Eb.conj().T @ K @ Hb)
    print(f"    (informational) linear exact-harmonic K-pairing "
          f"||E^dag K H|| = {lin_full:.4f} "
          f"(nonzero: the attack is live at linear AND quadratic order)")

    # ---------- (2b) inventory diagonality on descended observables --------
    def confined_direction(Kf, harm, epsv, muv, ndraw=6):
        """Register direction on eps-confined harmonic content."""
        gs = harm.conj().T @ Kf @ harm
        wv, Vv = np.linalg.eigh(0.5 * (gs + gs.conj().T))
        cols = Vv[:, wv > 1e-9] if epsv == 1 else Vv[:, wv < -1e-9]
        if cols.shape[1] == 0:
            return 0
        tot = 0.0
        for j in range(min(ndraw, cols.shape[1])):
            x = harm @ cols[:, j]
            q = epsv * float(np.real(x.conj() @ Kf @ x))
            assert q > -1e-12
            tot += muv * epsv * q
        return int(np.sign(tot))

    d_p = confined_direction(K, Hb, +1, +1)
    d_m = confined_direction(K, Hb, -1, +1)
    check("E", "(9,5) BV-grade anchor flip CO-FLIPS: flipping eps flips the "
               "selected K-grade AND the register direction on confined "
               "harmonic content, together",
          d_p == 1 and d_m == -1, detail=f"dir(+)={d_p} dir(-)={d_m}")

    d_mu = confined_direction(K, Hb, +1, -1)
    check("F", "(9,5) BV-grade paid split: the mu insert flips direction "
               "with the sector fixed -- flagged as the one paid Z/2 "
               "(control must fire)", d_mu == -1)

    # ghost-sign and antifield-sign flips: closure preserved, reading blind
    ok = True
    for sg_A, sg_M in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        cc1 = fro((sg_M * M_KT) @ (sg_A * A_W))
        cc2 = fro((sg_A * A_W).conj().T @ (sg_M * M_KT))
        ok = ok and cc1 < 1e-8 and cc2 < 1e-8
    check("E", "(9,5) ghost-sign and antifield-sign flips: closure survives "
               "all four leg-sign patterns and the harmonic reading never "
               "touches ghost data -- both redefinitions are inert on the "
               "pair", ok)

    # xi -> -xi: the BV image of time-reversal inertness (P3)
    stacked2 = np.vstack([B, (-gauge).conj().T])
    Hb2 = null_basis(stacked2)
    proj_diff = fro(Hb @ Hb.conj().T - Hb2 @ Hb2.conj().T)
    d_rev = confined_direction(K, Hb2, +1, +1)
    check("E", "(9,5) xi -> -xi (symbol/propagation direction) is INERT: "
               "identical harmonic space, identical confined direction -- "
               "the BV-grade image of P3 (the arrow is not in the "
               "propagator)", proj_diff < 1e-7 and d_rev == d_p,
          detail=f"projector drift {proj_diff:.1e}")

    # W -> -W: connection flip is diagonal
    GW2 = expm(-0.8 * Sig09)
    B2 = np.hstack([e[a] @ GW2 for a in range(N)])
    stacked3 = np.vstack([B2, gauge.conj().T])
    Hb3 = null_basis(stacked3)
    KH3 = Hb3.conj().T @ K @ Hb3
    ev3 = np.linalg.eigvalsh(0.5 * (KH3 + KH3.conj().T))
    npos3 = int((ev3 > 1e-9).sum())
    nneg3 = int((ev3 < -1e-9).sum())
    d_w = confined_direction(K, Hb3, +1, +1)
    check("E", "(9,5) connection flip W -> -W is DIAGONAL: harmonic "
               "K-signature unchanged, confined direction unchanged -- the "
               "dressing carries no sign grip on the pair",
          npos3 == npos and nneg3 == nneg and d_w == d_p,
          detail=f"signature (+{npos3},-{nneg3})")

    # ---------- (2c) the internal-mu question: decoupled vs cohomological --
    print()
    print("---- (2c) H-REC-CAUS contrast: Cl(1,3) miniature "
          "(quaternionic-class miniature of the fixture) ----")

    g0 = np.array([[0, 0, 1, 0], [0, 0, 0, 1],
                   [1, 0, 0, 0], [0, 1, 0, 0]], dtype=complex)
    s1m = np.array([[0, 1], [1, 0]], dtype=complex)
    s2m = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3m = np.array([[1, 0], [0, -1]], dtype=complex)
    Z2 = np.zeros((2, 2), dtype=complex)

    def offblock(sk):
        return np.block([[Z2, sk], [-sk, Z2]])

    em = [g0, offblock(s1m), offblock(s2m), offblock(s3m)]
    eta_m = [1.0, -1.0, -1.0, -1.0]
    ok = True
    for a in range(4):
        ok = ok and fro(em[a] @ em[a] - eta_m[a] * np.eye(4)) < 1e-12
        for b in range(a + 1, 4):
            ok = ok and fro(em[a] @ em[b] + em[b] @ em[a]) < 1e-12
    beta_m = em[0]
    xi_m = np.array([2.0, 0.5, 1.0, 0.3])
    cxi_m = sum(xi_m[a] * em[a] for a in range(4))
    ok = ok and fro(beta_m @ cxi_m.conj().T @ beta_m - cxi_m) < 1e-12
    check("T", "mini rep sanity: Cl(1,3) relations, beta = e_0, c(xi) "
               "K-Hermitian, xi non-null (Q = 2.66)", ok)

    Km = np.kron(np.diag([1.0, -1.0, -1.0, -1.0]).astype(complex), beta_m)
    Sig01 = 0.25 * (em[0] @ em[1] - em[1] @ em[0])
    GWm = expm(0.8 * Sig01)
    Bm = np.hstack([em[a] @ GWm for a in range(4)])          # 4 x 16
    gram_m = Bm @ Bm.conj().T
    Pim = np.eye(16, dtype=complex) - Bm.conj().T @ np.linalg.pinv(gram_m) @ Bm
    MD_m = np.kron(np.eye(4, dtype=complex), cxi_m)
    gauge_m = np.vstack([xi_m[a] * np.eye(4, dtype=complex) for a in range(4)])
    A_Wm = Pim @ gauge_m
    MKT_m = Bm.conj().T @ Bm
    ok = (fro(MKT_m @ A_Wm) < 1e-10
          and fro(A_Wm.conj().T @ MKT_m) < 1e-10)
    check("T", "mini bicomplex closure (blockwise s^2 = 0)", ok)

    # block-diagonal (VZ-decoupled) variant: EXACT invariant subspace
    Pp = np.eye(16, dtype=complex) - Pim
    M_off = Pim @ MD_m @ Pp + Pp @ MD_m @ Pim   # the escape/coupling blocks
    MD_dec = MD_m - M_off                        # = P M P + P" M P"
    comm_dec = fro(Pim @ MD_dec - MD_dec @ Pim)
    check("T", "mini decoupled variant: removing BOTH escape blocks makes "
               "the sector exactly dynamics-invariant ([Pi, M_dec] = 0)",
          comm_dec < 1e-10, detail=f"residual {comm_dec:.1e}")

    # the same statement at (9,5), cheaply (matmuls only)
    Pp95 = np.eye(VS, dtype=complex) - Pi
    M_D95 = np.kron(np.eye(N, dtype=complex), cxi)
    M_off95 = Pi @ M_D95 @ Pp95 + Pp95 @ M_D95 @ Pi
    MD_dec95 = M_D95 - M_off95
    comm95 = fro(Pi @ MD_dec95 - MD_dec95 @ Pi)
    esc95 = fro(Pp95 @ M_D95 @ Pi)
    check("T", "(9,5) anchor: the SAME block-diagonal decoupling exists at "
               "full scale ([Pi, M_dec] = 0) and the removed coupling is "
               "the nonzero escape term (the VZ-priced object)",
          comm95 < 1e-8 and esc95 > 1.0,
          detail=f"[Pi,M_dec]={comm95:.1e}, ||escape||={esc95:.2f}")

    # ---- gapped locus: eigengroups of the decoupled sector dynamics ------
    uu, ss, vv = np.linalg.svd(Pim)
    Y = uu[:, ss > 0.5]                       # orthonormal basis of ran Pi
    Dc = Y.conj().T @ MD_dec @ Y              # 12 x 12
    evals, evecs = np.linalg.eig(Dc)
    order = np.argsort(evals.real + 1e-6 * evals.imag)
    evals, evecs = evals[order], evecs[:, order]
    groups = []
    tol_g = 1e-7
    i = 0
    while i < len(evals):
        j = i + 1
        while j < len(evals) and abs(evals[j] - evals[i]) < tol_g:
            j += 1
        groups.append(list(range(i, j)))
        i = j
    print("    GAPPED locus (xi generic, Q = 2.66): decoupled sector "
          "spectrum (grouped):")
    n_indef = 0
    all_nondeg = True
    for grp in groups:
        X = Y @ evecs[:, grp]
        X, _ = np.linalg.qr(X)
        Gg = X.conj().T @ Km @ X
        evg = np.linalg.eigvalsh(0.5 * (Gg + Gg.conj().T))
        np_g = int((evg > 1e-8).sum())
        nn_g = int((evg < -1e-8).sum())
        nz_g = len(grp) - np_g - nn_g
        lam0 = evals[grp[0]]
        print(f"      lambda = {lam0.real:+.6f}{lam0.imag:+.6f}i  "
              f"dim {len(grp)}  K-signature (+{np_g}, -{nn_g}, 0:{nz_g})")
        if np_g >= 1 and nn_g >= 1:
            n_indef += 1
        if nz_g != 0:
            all_nondeg = False
    check("E", "GAPPED locus: every eigengroup of the decoupled sector "
               "dynamics is K-DEFINITE; since the commutant of a "
               "diagonalizable operator preserves each eigenspace, NO "
               "dynamics-commuting sector-preserving operator can reverse "
               "the record K-grade -- no unpaid mu exists at the gapped "
               "locus EVEN UNDER CLEAN DECOUPLING (protection stronger "
               "than the H-REC-CAUS hypothesis)",
          n_indef == 0 and all_nondeg,
          detail=f"{len(groups)} groups, {n_indef} indefinite")

    # ---- degenerate locus: null xi (Q = 0), the vacuum-adjacent surface --
    xi_null = np.array([1.0, 1.0, 0.0, 0.0])
    cxi_n = sum(xi_null[a] * em[a] for a in range(4))
    nilp = fro(cxi_n @ cxi_n)
    Bn = np.hstack(em)                              # undressed constraint
    Pin = np.eye(16, dtype=complex) \
        - Bn.conj().T @ np.linalg.pinv(Bn @ Bn.conj().T) @ Bn
    MDn = np.kron(np.eye(4, dtype=complex), cxi_n)
    Ppn = np.eye(16, dtype=complex) - Pin
    M_offn = Pin @ MDn @ Ppn + Ppn @ MDn @ Pin
    MD_decn = MDn - M_offn
    esc_n = fro(Ppn @ MDn @ Pin)
    check("T", "DEGENERATE locus setup: null xi (c(xi)^2 = 0 exactly, the "
               "Q = 0 vacuum-adjacent surface named by the D1 degeneracy "
               "result), with the coupling/escape term still NONZERO -- "
               "the coupled-vs-decoupled contrast is live there",
          nilp < 1e-12 and esc_n > 1.0,
          detail=f"||c^2||={nilp:.1e}, ||escape||={esc_n:.3f}")

    uun, ssn, _ = np.linalg.svd(Pin)
    Yn = uun[:, ssn > 0.5]
    Dcn = Yn.conj().T @ MD_decn @ Yn
    kerD = null_basis(Dcn, tol=1e-7)
    imD_perp = null_basis(Dcn.conj().T, tol=1e-7)   # (im D)^perp = ker D^dag
    # N_0 = ker(D) cap (im D)^perp: the diagonalizable zero block,
    # computed as the eigenvalue-1 space of the symmetrized projector product
    PK = kerD @ kerD.conj().T
    PI2 = imD_perp @ imD_perp.conj().T
    wN = np.linalg.eigvalsh(0.5 * (PK @ PI2 + PI2 @ PK))
    dimN0 = int((wN > 1 - 1e-8).sum())
    ranks = []
    Mk = np.eye(12, dtype=complex)
    for k in range(1, 5):
        Mk = Mk @ Dcn
        ranks.append(int(np.linalg.matrix_rank(Mk, tol=1e-7)))
    nilnorm = fro(np.linalg.matrix_power(Dcn, 12))
    Gker = (Yn @ kerD).conj().T @ Km @ (Yn @ kerD)
    evk = np.linalg.eigvalsh(0.5 * (Gker + Gker.conj().T))
    npk = int((evk > 1e-8).sum())
    nnk = int((evk < -1e-8).sum())
    nzk = kerD.shape[1] - npk - nnk
    check("E", "DEGENERATE locus is the JORDAN WALL, not the d1 shape: the "
               "sector dynamics is exactly nilpotent and its diagonalizable "
               "zero block N_0 = ker(D) cap (im D)^perp is EMPTY -- every "
               "kernel vector is a chain end; no admissible grading exists "
               "there at all (R1's positivity-unrescuable wall), so the "
               "direction observable is VACUOUS rather than split at this "
               "fixture's own degenerate surface",
          dimN0 == 0 and kerD.shape[1] == 4 and nilnorm < 1e-6,
          detail=f"dim ker={kerD.shape[1]}, dim N_0={dimN0}, "
                 f"ranks D^k={ranks}, ||D^12||={nilnorm:.1e}, "
                 f"ker K-sig (+{npk},-{nnk},0:{nzk})")

    # ---- where the d1 shape actually lives: the BARE symbol dynamics -----
    # eigenspaces of the (K-Hermitian, non-normal) symbol are K-orthogonal,
    # not dagger-orthogonal, so the swap must be built with the K-dual.
    Qxi = float(np.sum(xi_m ** 2 * np.array(eta_m)))
    sq = np.sqrt(Qxi)
    Eplus = null_basis(MD_m - sq * np.eye(16, dtype=complex), tol=1e-9)
    Gp = Eplus.conj().T @ Km @ Eplus
    wp, Vp = np.linalg.eigh(0.5 * (Gp + Gp.conj().T))
    npp = int((wp > 1e-8).sum())
    nnp = int((wp < -1e-8).sum())
    a2 = Eplus @ Vp[:, -1] / np.sqrt(abs(wp[-1]))
    b2 = Eplus @ Vp[:, 0] / np.sqrt(abs(wp[0]))
    M2 = np.column_stack([a2, b2])
    swap2 = np.array([[0, 1], [1, 0]], dtype=complex)
    Kdual = np.diag([1.0, -1.0]).astype(complex) @ M2.conj().T @ Km
    R2 = np.eye(16, dtype=complex) + M2 @ (swap2 - np.eye(2)) @ Kdual
    dR2_MD = fro(R2 @ MD_m - MD_m @ R2)
    dR2_Pi = fro(R2 @ Pim - Pim @ R2)
    qa2 = float(np.real(a2.conj() @ Km @ a2))
    qRa2 = float(np.real((R2 @ a2).conj() @ Km @ (R2 @ a2)))
    check("E", "THE d1 SHAPE LIVES IN THE BARE DYNAMICS: the +sqrt(Q) "
               "eigenspace of the raw symbol dynamics is K-INDEFINITE "
               "degenerate diagonalizable -- the vacuum-anchor degeneracy "
               "shape -- and a K-grade-reversing symmetry R' of the "
               "dynamics ALONE exists there: without the constraint/sector "
               "structure the grade flip is FREE (the unpaid mu exists at "
               "the structure-free grade)",
          npp >= 1 and nnp >= 1 and dR2_MD < 1e-8 and qa2 > 0 and qRa2 < 0,
          detail=f"+sqrtQ K-sig (+{npp},-{nnp}); [R',M_D]={dR2_MD:.1e}; "
                 f"charge {qa2:+.3f} -> {qRa2:+.3f}")

    check("E", "THE CONSTRAINT STRUCTURE IS THE ENFORCEMENT: the same R' "
               "BREAKS the sector projector ([R', Pi] != 0) -- the "
               "constraint surface installed by the cohomological "
               "realization is what removes the bare-grade flip; combined "
               "with the K-definite compressed eigengroups above, the "
               "decoupled sector inherits NO grade-flipping symmetry at "
               "the gapped locus (exhaustive over the commutant there)",
          dR2_Pi > 1e-3, detail=f"[R',Pi]={dR2_Pi:.4f}")

    # ---- the escape identity, exhibited on a DECOUPLED-ONLY symmetry -----
    # The compression-born singlet eigendirections of the decoupled sector
    # dynamics (eigenvalues +-0.50 +- 0.35i, NOT eigenvalues of M_D) carry
    # spectral reflections R = I - 2 P_spec that are exact symmetries of the
    # decoupled realization and of nothing else: in the coupled theory they
    # pay a defect EXACTLY equal to their non-commutation with the escape
    # term -- [R, M_D] = [R, M_off] since [R, M_dec] = 0.
    singlets = [g for g in groups if len(g) == 1]
    Vinv = np.linalg.inv(evecs)
    i0 = singlets[0][0]
    Rc = np.eye(12, dtype=complex) \
        - 2.0 * np.outer(evecs[:, i0], Vinv[i0, :])
    Rs = Y @ Rc @ Y.conj().T + (np.eye(16, dtype=complex) - Pim)
    dRs_dec = fro(Rs @ MD_dec - MD_dec @ Rs)
    dRs_Pi = fro(Rs @ Pim - Pim @ Rs)
    dRs_MD = fro(Rs @ MD_m - MD_m @ Rs)
    dRs_off = fro(Rs @ M_off - M_off @ Rs)
    check("E", "THE ESCAPE IDENTITY: a decoupled-ONLY symmetry (spectral "
               "reflection through a compression-born eigendirection) "
               "commutes with the decoupled dynamics and the sector "
               "projector, yet in the coupled theory pays a defect EXACTLY "
               "equal to its non-commutation with the escape term "
               "([R, M_D] = [R, M_off] identically) -- the "
               "causality-required coupling removes the decoupled "
               "variant's symmetry surplus, the reservoir any internal mu "
               "would have to come from",
          dRs_dec < 1e-6 and dRs_Pi < 1e-8 and dRs_MD > 1e-3
          and abs(dRs_MD - dRs_off) < 1e-8,
          detail=f"[R,M_dec]={dRs_dec:.1e} [R,Pi]={dRs_Pi:.1e} "
                 f"||[R,M_D]||={dRs_MD:.4f} = ||[R,M_off]||={dRs_off:.4f}")
    return True


# ===========================================================================

def main():
    part1()
    part1b()
    part2()

    e = sum(1 for t, _, ok in RESULTS if t == "E" and ok)
    f = sum(1 for t, _, ok in RESULTS if t == "F" and ok)
    t_ = sum(1 for t, _, ok in RESULTS if t == "T" and ok)
    failures = [(t, n) for t, n, ok in RESULTS if not ok]
    print()
    print(f"headline: {e} [E] + {f} [F] = {e + f}  (setup [T] = {t_}, "
          f"excluded)")
    if failures:
        print("FAILURES:")
        for t, n in failures:
            print(f"  [{t}] {n}")
        print("VERDICT: FAMILY OR BV-GRADE CO-FLIP BROKEN -- if a "
              "zero-import composite split the pair at either grade, the "
              "class claim is dead at that grade and N -> 5.")
        return 1
    print("VERDICT: (1) The co-flip + split-costs-one accounting holds "
          "over the axiomatized class C(p,q; Phi) -- all signatures, "
          "dimensions, couplings, and the enlarged operation inventory; "
          "same identity under quaternionic-type (J-commuting) and "
          "real-type (sector-exchanging) antiunitary typing. "
          "(2) At BV/cohomological grade the ONE new zero-import attack "
          "(representative choice) splits any representative-level "
          "register and has zero grip on the descended (harmonic/"
          "confined) reading; the enumerated BV inventory acts "
          "diagonally. (3) The internal mu exists FREE at the "
          "structure-free grade (bare symbol dynamics, K-indefinite "
          "degenerate eigenspaces -- the d1 shape); the CONSTRAINT "
          "structure removes it, no unpaid mu survives at any gapped "
          "locus even under clean VZ decoupling, the fixture's own "
          "degenerate surface is the (vacuous, ungradable) Jordan wall, "
          "and every surplus decoupled symmetry pays exactly the "
          "escape/coupling term in the coupled theory ([R,M_D] = "
          "[R,M_off]). The BV-grade co-flip survives on descended "
          "observables; the N->5 route through this gap is closed at "
          "this fixture grade, conditional on the canonical/confined "
          "reading (the D1 condition) and on the S_IG-locus residual.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
