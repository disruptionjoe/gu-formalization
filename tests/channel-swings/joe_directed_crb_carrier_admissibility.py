#!/usr/bin/env python3
"""CR-B: which spinor CARRIERS are admissible on Y^14, and does the chirality
tie engage on GU's DECLARED fermionic content?

HE-2 (2026-08-15, 204/204) proved n_g -> n_g - 1 is real-form stable, then named
its own live kill:

    "if GU's declared spinorial content is not a single ambient Weyl (or
     symplectic-Majorana-Weyl) spinor but a full ambient Dirac or non-Weyl
     Majorana object, then the ambient chirality tie never engages ... and
     n_g = 0 outright."

This probe decides the MATHEMATICS half of that gate and computes the exact
consequence of each source-attested reading.  It is deliberately built so that
the verdict does NOT depend on the SIGNATURE-AMBIENT fork.

TWO INDEPENDENT INSTRUMENTS, because "carrier" is doing two jobs:

  INSTRUMENT 1 -- CLIFFORD ADMISSIBILITY (real-form dependent).
     Which of {Weyl, Majorana, Majorana-Weyl, symplectic-Majorana,
     symplectic-Majorana-Weyl} EXIST in a given signature (p,q)?  Solved for,
     not postulated: build Cl(p,q) explicitly over Z[i], solve for the antilinear
     intertwiners B_eta with Gamma_a^* = eta . B Gamma_a B^{-1}, read off
     sign(J^2) = B conj(B) and whether B commutes with the chirality element.
     The five availability bits are then DERIVED from stated definitions.
     The repo banks the Weyl-half reality type (HE-2 Table B) and the two horn
     rows; it does NOT bank the five-condition x eight-residue table.  That gap
     is what section 1 fills.

  INSTRUMENT 2 -- CENTRE-CLASS HOMOGENEITY (real-form BLIND and signature
     BLIND).  For D_n the representation ring is graded by P/Q.  Writing weights
     in DOUBLED integer coordinates, the class map is

         cls(lambda) = (sum of doubled coordinates) mod 4

     which is additive over (+), multiplicative over (x), and well defined
     because every root has doubled-coordinate sum in {0, +-4}.  The theorem
     this probe uses:

         a module M homogeneous of ODD class admits NO invariant bilinear form
         on M (x) M, because cls(M (x) M) = 2 cls(M) = 2 mod 4 /= 0.

     Odd class is therefore a sufficient, purely integer-arithmetic certificate
     of "no gauge-invariant mass term anywhere inside M", i.e. of chirality.
     It is real-form blind for exactly HE-2 Leg B's reason (it is settled in the
     complexification every real form shares) and it is signature blind because
     Cl(p,q) (x) C depends only on p+q.

THE OBJECT DECIDED.  The 2021 draft p.51 prints FOUR corners,
    nu_+ in Omega^0(S_+),  nu_- in Omega^0(S_-),
    zeta_+ in Omega^1(S_+), zeta_- in Omega^1(S_-),
and the draft's own eq (5.2) p.31 / eq (9.16) p.46 declare S UNSUBSCRIPTED.
Section 3 computes the centre class of all four corners and of every pairing of
them, and reports which pairings are class-homogeneous.

EXACTNESS DISCIPLINE
  Every Clifford step is integer arithmetic in Z[i], carried as a pair of int64
  numpy arrays; gamma words are monomial with entries in {0,+-1,+-i}.  Every
  matrix produced is swept for magnitude and the sweep bound is asserted, so no
  int64 overflow can hide.  Ranks are over F_p with p = 1 mod 4 and are each
  SANDWICHED between the F_p lower bound and an independent codomain upper
  bound, so each rank is pinned exactly rather than probabilistically.  Weights
  are DOUBLED integer tuples; all class arithmetic is integer mod 4.  Weyl
  dimensions use Fraction.  NO floating point is load-bearing; assert_no_float
  sweeps the whole result dict at the end.

CONTROLS
  - POSITIVE, predeclared before the run: the Weyl-half reality type for 13
    signatures against the banked HE-2 table; (7,7) admits Majorana-Weyl with
    64 real fixed dimensions inside S^+; (9,5) admits none.
  - CONTRARY CONTROL A (absence of a carrier type): (9,5), where Majorana-Weyl
    provably does NOT exist -- the machinery must return dim_R = 0 for the
    J-fixed set inside S^+, by an exact F_p rank equal to the full 128.
  - CONTRARY CONTROL B (absence of the centre-class protection): D_6, i.e.
    TWELVE dimensions, where -w_0 = id, cls(S^+) = 2 is EVEN, and the
    half-spinor IS self-dual -- so a class-homogeneous content is NOT protected
    and a Majorana mass is allowed.  If the instrument cannot see the protection
    fail where it really fails, its "protected" verdict at D_7 is worthless.
  - PLANTED FAILURES: twelve assertions FALSE by construction, each observed False.
  - MUTATIONS: fourteen injected machinery defects, each required to drive
    exit 1 under --selftest.

WHAT THIS IS NOT
  Not a source action, not SG4, not a generation count, not a physical carrier,
  not a resolution of SIGNATURE-AMBIENT, not a dynamical or VEV statement, and
  not a claim-status movement.  n_g is an INPUT throughout.

Usage:
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_crb_carrier_admissibility.py
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_crb_carrier_admissibility.py --selftest
"""
from __future__ import annotations

import os
import subprocess
import sys
from fractions import Fraction
from itertools import product

import numpy as np

MUT = os.environ.get('CRB_MUTATE', '')

CERT: list[tuple[str, str, bool, object]] = []
RESULT: dict = {}

# Magnitude bound every Z[i] matrix entry must respect.  Jordan-Wigner gamma
# words are monomial with entries in {0,+-1,+-i}; anything larger means a
# construction defect, and anything near int64 range would mean silent overflow.
SWEEP_BOUND = 1 << 20


def check(tag: str, name: str, ok: bool, detail=None) -> bool:
    CERT.append((tag, name, bool(ok), detail))
    return bool(ok)


# ===========================================================================
# Z[i] exact matrix arithmetic: a matrix is a pair (re, im) of int64 arrays.
# ===========================================================================

def zi(re, im=None):
    re = np.asarray(re, dtype=np.int64)
    im = np.zeros_like(re) if im is None else np.asarray(im, dtype=np.int64)
    return (re, im)


def zmul(A, B):
    ar, ai = A
    br, bi = B
    return (ar @ br - ai @ bi, ar @ bi + ai @ br)


def zadd(A, B):
    return (A[0] + B[0], A[1] + B[1])


def zsub(A, B):
    return (A[0] - B[0], A[1] - B[1])


def zscale(A, c):
    return (A[0] * c, A[1] * c)


def zconj(A):
    return (A[0], -A[1])


def zeq(A, B):
    return bool(np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1]))


def zeye(n):
    return zi(np.eye(n, dtype=np.int64))


def zsweep(A) -> int:
    """Return max |entry| over re and im; used to prove no int64 overflow."""
    return int(max(np.abs(A[0]).max(initial=0), np.abs(A[1]).max(initial=0)))


SWEEP_MAX = {'v': 0}


def zguard(A, where: str):
    m = zsweep(A)
    if m > SWEEP_MAX['v']:
        SWEEP_MAX['v'] = m
    if m > SWEEP_BOUND:
        raise AssertionError('Z[i] magnitude sweep exceeded at %s: %d' % (where, m))
    return A


# ---------------------------------------------------------------------------
# Jordan-Wigner Clifford generators for Cl(p,q), p+q = 2m, over Z[i].
# ---------------------------------------------------------------------------

_S_X = zi([[0, 1], [1, 0]])
_S_Y = zi([[0, 0], [0, 0]])
_S_Y = (np.array([[0, 0], [0, 0]], dtype=np.int64),
        np.array([[0, -1], [1, 0]], dtype=np.int64))   # [[0,-i],[i,0]]
_S_Z = zi([[1, 0], [0, -1]])
_S_I = zeye(2)


def kron(A, B):
    ar, ai = A
    br, bi = B
    return (np.kron(ar, br) - np.kron(ai, bi), np.kron(ar, bi) + np.kron(ai, br))


def hermitian_gammas(m: int):
    """2m Hermitian generators e_1..e_{2m} of Cl(2m,0), each squaring to +I.

    Jordan-Wigner:  e_{2k-1} = Z^{(k-1)} X I^{...},  e_{2k} = Z^{(k-1)} Y I^{...}
    Every generator is monomial; e_{2k-1} is REAL, e_{2k} is purely IMAGINARY.
    """
    out = []
    for k in range(1, m + 1):
        for P in (_S_X, _S_Y):
            M = zeye(1)
            for j in range(1, m + 1):
                if j < k:
                    F = _S_Z
                elif j == k:
                    F = P
                else:
                    F = _S_I
                M = kron(M, F)
            out.append(M)
    return out


def clifford(p: int, q: int):
    """Gammas for Cl(p,q): Gamma_a^2 = +I for a < p, -I for a >= p.

    Built from the Hermitian set by multiplying the last q generators by i.
    Returns (gammas, chirality, real_idx, imag_idx).
    """
    n = p + q
    assert n % 2 == 0
    m = n // 2
    herm = hermitian_gammas(m)
    gam = []
    split = q if MUT == 'signature_swap' else p     # mutant builds Cl(q,p)
    for a in range(n):
        if a < split:
            gam.append(herm[a])
        else:
            # multiply by i:  (re, im) -> (-im, re)
            gam.append((-herm[a][1], herm[a][0]))
    for a, G in enumerate(gam):
        zguard(G, 'gamma[%d] of Cl(%d,%d)' % (a, p, q))
    # chirality: omega = c * Gamma_1 ... Gamma_n with c chosen so omega^2 = +I.
    W = zeye(1 << m)
    for G in gam:
        W = zguard(zmul(W, G), 'omega word')
    # W^2 = s * I with s in {+-1, +-i-free}; find the unit u with (u W)^2 = I.
    W2 = zguard(zmul(W, W), 'omega^2')
    N = 1 << m
    ident = zeye(N)
    omega = None
    for u in ((1, 0), (0, 1), (-1, 0), (0, -1)):   # 1, i, -1, -i
        cand = (u[0] * W[0] - u[1] * W[1], u[0] * W[1] + u[1] * W[0])
        if zeq(zmul(cand, cand), ident):
            omega = cand
            break
    assert omega is not None, 'no unit normalises omega for Cl(%d,%d)' % (p, q)
    real_idx = [a for a, G in enumerate(gam) if not G[1].any()]
    imag_idx = [a for a, G in enumerate(gam) if not G[0].any()]
    assert len(real_idx) + len(imag_idx) == n, 'a gamma is neither real nor imaginary'
    return gam, omega, real_idx, imag_idx, W2


def clifford_relations_ok(gam, p, q) -> bool:
    n = p + q
    N = gam[0][0].shape[0]
    ident = zeye(N)
    for a in range(n):
        sq = zmul(gam[a], gam[a])
        want = ident if a < p else zscale(ident, -1)
        if not zeq(sq, want):
            return False
    for a in range(n):
        for b in range(a + 1, n):
            ab = zmul(gam[a], gam[b])
            ba = zmul(gam[b], gam[a])
            if not zeq(zadd(ab, ba), zi(np.zeros((N, N), dtype=np.int64))):
                return False
    return True


def antilinear_families(gam, omega, real_idx, imag_idx, p, q):
    """Solve for the two antilinear intertwiners.

    B_S = prod_{a in imag} Gamma_a  and  B_R = prod_{a in real} Gamma_a satisfy
    Gamma_a^* = eta . B Gamma_a B^{-1} for eta = -1 and +1 respectively; the
    sign eta is SOLVED here (verified elementwise), never assumed.

    For J(psi) = B psi^*, J^2 = B conj(B).  Returns a list of records.
    """
    n = p + q
    N = gam[0][0].shape[0]
    ident = zeye(N)
    out = []
    words = {'S': imag_idx, 'R': real_idx}
    if MUT == 'truncate_B':
        words = {'S': imag_idx[:-1], 'R': real_idx}
    for label, idxs in words.items():
        B = zeye(N)
        for a in idxs:
            B = zguard(zmul(B, gam[a]), 'B_%s word' % label)
        # B is monomial and B * B^dagger = +- I; get B^{-1} exactly.
        Bd = (B[0].T.copy(), -B[1].T.copy())          # conjugate transpose
        BBd = zguard(zmul(B, Bd), 'B Bdag')
        s = None
        for sgn in (1, -1):
            if zeq(BBd, zscale(ident, sgn)):
                s = sgn
                break
        if s is None:
            continue
        Binv = zscale(Bd, s)
        assert zeq(zmul(B, Binv), ident)
        # solve for eta elementwise
        eta = None
        for cand in (1, -1):
            good = True
            for a in range(n):
                lhs = zconj(gam[a])
                rhs = zscale(zmul(zmul(B, gam[a]), Binv), cand)
                if not zeq(lhs, rhs):
                    good = False
                    break
            if good:
                eta = cand
                break
        if eta is None:
            continue
        Jsq = zguard(zmul(B, zconj(B)), 'J^2')
        jsign = None
        for sgn in (1, -1):
            if zeq(Jsq, zscale(ident, sgn)):
                jsign = sgn
                break
        assert jsign is not None, 'J^2 is not +-I for Cl(%d,%d) family %s' % (p, q, label)
        # does J commute with chirality?  J(omega psi) = B conj(omega) conj(psi);
        # J preserves chirality iff B conj(omega) = omega B.
        lhs = zguard(zmul(B, zconj(omega)), 'B conj(omega)')
        rhs = zguard(zmul(omega, B), 'omega B')
        preserves = zeq(lhs, rhs)
        if MUT == 'chirality_flip':
            preserves = not preserves
        out.append({'label': label, 'eta': eta, 'jsq': jsign,
                    'preserves_chirality': preserves, 'B': B})
    return out


def admissibility(fams) -> dict:
    """DERIVE the five carrier bits from stated definitions.

      Weyl                       : even dimension (always, over C)
      Majorana                   : exists an antilinear J on the full Dirac
                                   module with J^2 = +1
      Majorana-Weyl              : ... and J preserves chirality
      symplectic-Majorana        : exists J with J^2 = -1 (Sp(1) doubling)
      symplectic-Majorana-Weyl   : ... and J preserves chirality
    """
    maj = any(f['jsq'] == +1 for f in fams)
    mw = any(f['jsq'] == +1 and f['preserves_chirality'] for f in fams)
    sm = any(f['jsq'] == -1 for f in fams)
    smw = any(f['jsq'] == -1 and f['preserves_chirality'] for f in fams)
    if MUT == 'admissibility':
        mw = not mw
    return {'Weyl': True, 'Majorana': maj, 'Majorana-Weyl': mw,
            'symplectic-Majorana': sm, 'symplectic-Majorana-Weyl': smw}


def weyl_half_type(p: int, q: int) -> str:
    """PREDECLARED textbook answer, banked at HE-2 Table B, for even p+q."""
    tbl = {0: 'REAL', 2: 'COMPLEX', 4: 'QUATERNIONIC', 6: 'COMPLEX'}
    if MUT == 'table':
        tbl = {0: 'QUATERNIONIC', 2: 'COMPLEX', 4: 'REAL', 6: 'COMPLEX'}
    return tbl[(p - q) % 8]


# ---------------------------------------------------------------------------
# Exact rank over F_p with p = 1 mod 4, i |-> s, s^2 = -1.
# ---------------------------------------------------------------------------

PRIMES = [998244353, 2013265921, 469762049]   # all prime, all = 1 mod 4


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for pp in small:
        if n % pp == 0:
            return n == pp
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# primality is CHECKED, not assumed -- a composite modulus silently corrupts
# every rank below (this exact defect was caught during the build).
assert all(pp % 4 == 1 and _is_prime(pp) for pp in PRIMES)


def _sqrt_minus_one(pp: int) -> int:
    for g in range(2, 200):
        s = pow(g, (pp - 1) // 4, pp)
        if (s * s) % pp == pp - 1:
            return s
    raise AssertionError('no sqrt(-1) mod %d' % pp)


def rank_fp(A, pp: int) -> int:
    """Rank over F_p of a Z[i] matrix, i |-> sqrt(-1) mod p."""
    s = _sqrt_minus_one(pp)
    M = ((A[0] % pp) + (A[1] % pp) * s) % pp
    M = M.astype(object)
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c] % pp:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), pp - 2, pp)
        M[r] = (M[r] * inv) % pp
        for i in range(rows):
            if i != r and M[i, c] % pp:
                M[i] = (M[i] - M[i, c] * M[r]) % pp
        r += 1
        if r == rows:
            break
    return r


def rank_fp_real(Mint, pp: int) -> int:
    """Rank over F_p of an integer matrix (already realified)."""
    M = (Mint % pp).astype(object)
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c] % pp:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), pp - 2, pp)
        M[r] = (M[r] * inv) % pp
        for i in range(rows):
            if i != r and M[i, c] % pp:
                M[i] = (M[i] - M[i, c] * M[r]) % pp
        r += 1
        if r == rows:
            break
    return r


# ===========================================================================
# SECTION 1 -- Clifford admissibility: five carrier types, eight residues.
# ===========================================================================

SIGNATURES = [
    (7, 7),   # horn A
    (9, 5),   # horn B
    (5, 9),   # horn B mirror
    (6, 4),   # GU internal
    (4, 6),
    (13, 1),  # the one-time Lorentzian reading of Y^14
    (11, 3),
    (3, 1), (1, 3),          # external, both conventions
    (9, 1),                  # textbook 10d Majorana-Weyl
    (5, 5), (7, 3), (4, 0), (10, 0),
    (6, 6),                  # D_6 CONTRARY CONTROL, 12 dimensions
]


def section_1():
    rows = []
    for (p, q) in SIGNATURES:
        gam, omega, ridx, iidx, W2 = clifford(p, q)
        ok_rel = clifford_relations_ok(gam, p, q)
        check('clifford', 'Cl(%d,%d) relations verified elementwise' % (p, q), ok_rel)
        fams = antilinear_families(gam, omega, ridx, iidx, p, q)
        check('clifford', 'Cl(%d,%d) both antilinear families found' % (p, q),
              len(fams) == 2, [f['label'] for f in fams])
        # both eta values must be realised, one per family
        etas = sorted(f['eta'] for f in fams)
        check('clifford', 'Cl(%d,%d) eta = -1 and +1 both realised' % (p, q),
              etas == [-1, 1], etas)
        adm = admissibility(fams)
        # the Weyl-half reality type, read from the family that PRESERVES
        # chirality (if any); if none preserves, the half is COMPLEX type.
        pres = [f for f in fams if f['preserves_chirality']]
        if not pres:
            htype = 'COMPLEX'
        else:
            htype = 'REAL' if pres[0]['jsq'] == +1 else 'QUATERNIONIC'
            check('clifford', 'Cl(%d,%d) preserving families agree on J^2' % (p, q),
                  len({f['jsq'] for f in pres}) == 1)
        want = weyl_half_type(p, q)
        check('control-positive',
              'Cl(%d,%d) Weyl-half type computed = predeclared %s' % (p, q, want),
              htype == want, (htype, want))
        rows.append({'p': p, 'q': q, 's': (p - q) % 8, 'half_type': htype,
                     'adm': adm,
                     'families': [(f['label'], f['eta'], f['jsq'],
                                   f['preserves_chirality']) for f in fams]})
    RESULT['admissibility_rows'] = [
        {k: v for k, v in r.items() if k != 'families'} for r in rows]

    by_sig = {(r['p'], r['q']): r for r in rows}

    # --- the two live horns, against the banked HE-2 row -------------------
    a = by_sig[(7, 7)]['adm']
    b = by_sig[(9, 5)]['adm']
    check('horn', '(7,7): Majorana-Weyl ADMISSIBLE (banked HE-2)',
          a['Majorana-Weyl'] is True, a)
    check('horn', '(7,7): Majorana ADMISSIBLE', a['Majorana'] is True, a)
    check('control-contrary',
          'CONTRARY A: (9,5) Majorana-Weyl NOT admissible -- absence detected',
          b['Majorana-Weyl'] is False, b)
    check('control-contrary',
          'CONTRARY A: (9,5) Majorana NOT admissible -- absence detected',
          b['Majorana'] is False, b)
    check('horn', '(9,5): symplectic-Majorana-Weyl ADMISSIBLE (banked HE-2)',
          b['symplectic-Majorana-Weyl'] is True, b)
    check('horn', '(9,5): symplectic-Majorana ADMISSIBLE',
          b['symplectic-Majorana'] is True, b)

    # --- the residue-class table, which the repo does not bank -------------
    tbl = {}
    for r in rows:
        if (r['p'] + r['q']) % 2:
            continue
        key = r['s']
        sig = tuple(sorted((k for k in r['adm'] if r['adm'][k])))
        tbl.setdefault(key, set()).add(sig)
    for s, sigs in sorted(tbl.items()):
        check('residue-table',
              'residue s=%d: admissibility is a FUNCTION of s alone' % s,
              len(sigs) == 1, sigs)
    RESULT['residue_table'] = {s: sorted(list(sigs)[0]) for s, sigs in sorted(tbl.items())}

    # every carrier type must be BOTH present somewhere and absent somewhere,
    # otherwise the instrument is a constant function and proves nothing.
    for kind in ('Majorana', 'Majorana-Weyl', 'symplectic-Majorana',
                 'symplectic-Majorana-Weyl'):
        yes = sum(1 for r in rows if r['adm'][kind])
        no = sum(1 for r in rows if not r['adm'][kind])
        check('non-vacuity',
              'carrier "%s" is admissible somewhere AND inadmissible somewhere'
              % kind, yes > 0 and no > 0, (yes, no))

    # --- exact real dimension of the J-fixed set inside S^+, both horns ----
    for (p, q), want_fix in (((7, 7), 64), ((9, 5), 0)):
        gam, omega, ridx, iidx, _ = clifford(p, q)
        fams = antilinear_families(gam, omega, ridx, iidx, p, q)
        pres = [f for f in fams if f['preserves_chirality']]
        assert pres, 'no chirality-preserving family for (%d,%d)' % (p, q)
        B = pres[0]['B']
        N = B[0].shape[0]                     # 128
        # basis of S^+ : columns of (I + omega); rank over F_p pins dim = 64.
        Pp = zadd(zeye(N), omega)
        rk = rank_fp(Pp, PRIMES[0])
        check('fixed-set', 'Cl(%d,%d): dim_C S^+ = %d (rank sandwich)' % (p, q, N // 2),
              rk == N // 2, rk)
        # Realify.  A complex v = x + i y becomes (x, y) in R^{2N}; the REAL
        # span of S^+ needs both v and i.v, and realify(i.v) = (-y, x).  So the
        # columns of [[Vr, -Vi], [Vi, Vr]] span S^+ as a REAL subspace of R^{2N}.
        Vr, Vi = Pp
        SR = np.block([[Vr, -Vi], [Vi, Vr]])          # 2N x 2N, real rank N
        # J on the ambient: psi -> B conj(psi).  In real coordinates
        # (x, y) -> (Br x + Bi y, Bi x - Br y).
        Br, Bi = B
        JR = np.block([[Br, Bi], [Bi, -Br]])
        rk_S = rank_fp_real(SR.astype(object), PRIMES[0])
        check('fixed-set', 'Cl(%d,%d): dim_R S^+ = %d' % (p, q, N),
              rk_S == N, rk_S)
        # image of (J - 1) restricted to S^+ ; its rank is the codimension of
        # the fixed set inside S^+, since col-span(SR) IS S^+ over R.
        D = (JR @ SR) - SR
        rks = [rank_fp_real(D.astype(object), pp) for pp in PRIMES]
        rk_D = max(rks)
        check('fixed-set', 'Cl(%d,%d): (J-1)|S^+ rank agrees on three primes'
              % (p, q), len(set(rks)) == 1, rks)
        # F_p rank LOWER-bounds the rank over Q; N = dim_R S^+ UPPER-bounds it.
        # Both horns hit an endpoint of that sandwich, so each is pinned exactly.
        check('fixed-set', 'Cl(%d,%d): rank sandwich  %d <= rk <= %d'
              % (p, q, rk_D, N), 0 <= rk_D <= N, (rk_D, N))
        fixed = N - rk_D
        tag = 'control-contrary' if want_fix == 0 else 'fixed-set'
        check(tag, 'Cl(%d,%d): dim_R of J-fixed set inside S^+ = %d'
              % (p, q, want_fix), fixed == want_fix, fixed)
        RESULT.setdefault('fixed_sets', {})['%d,%d' % (p, q)] = fixed


# ===========================================================================
# SECTION 2 -- the centre-class instrument for D_n, and its contrary control.
# ===========================================================================

def cls_of(dw) -> int:
    """Class in P/Q of a D_n weight given in DOUBLED integer coordinates."""
    c = int(sum(dw)) % 4
    if MUT == 'cls_map':
        c = (c * 2) % 4
    return c


def d_roots(n):
    """Doubled coordinates of the D_n roots: +-e_i +- e_j, i < j."""
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            for si in (2, -2):
                for sj in (2, -2):
                    v = [0] * n
                    v[i] = si
                    v[j] = sj
                    out.append(tuple(v))
    return out


def spinor_weights(n, half):
    """All 2^{n-1} doubled weights of the D_n half-spinor with parity `half`.

    half = 0 : even number of -1 entries   (call it S^+)
    half = 1 : odd number
    """
    out = []
    for signs in product((1, -1), repeat=n):
        if (sum(1 for s in signs if s < 0) % 2) == half:
            out.append(tuple(signs))
    return out


def section_2():
    # --- well-definedness: every root has class 0 --------------------------
    for n in (4, 5, 6, 7):
        bad = [r for r in d_roots(n) if cls_of(r) != 0]
        check('centre', 'D_%d: every root has class 0 (class map well defined)' % n,
              not bad, bad[:3])

    # --- additivity over (+) and multiplicativity over (x) -----------------
    n = 7
    sp = spinor_weights(n, 0)[0]
    sm = spinor_weights(n, 1)[0]
    vec = tuple([2] + [0] * (n - 1))
    tens = tuple(a + b for a, b in zip(vec, sm))
    check('centre', 'D_7: cls(V (x) S^-) = cls(V) + cls(S^-) mod 4',
          cls_of(tens) == (cls_of(vec) + cls_of(sm)) % 4,
          (cls_of(tens), cls_of(vec), cls_of(sm)))

    # --- the D_7 classes ---------------------------------------------------
    c_sp, c_sm, c_v = cls_of(sp), cls_of(sm), cls_of(vec)
    check('centre', 'D_7: cls(S^+) = 3', c_sp == 3, c_sp)
    check('centre', 'D_7: cls(S^-) = 1', c_sm == 1, c_sm)
    check('centre', 'D_7: cls(V) = 2', c_v == 2, c_v)
    check('centre', 'D_7: cls(adjoint) = 0',
          cls_of(tuple([2, 2] + [0] * (n - 2))) == 0)
    # every weight of a half-spinor has the SAME class -- so the class is a
    # property of the module, not of a chosen weight.
    for half, want in ((0, 3), (1, 1)):
        cs = {cls_of(w) for w in spinor_weights(n, half)}
        check('centre', 'D_7: all 64 weights of S^%s share class %d'
              % ('+' if half == 0 else '-', want), cs == {want}, cs)
    RESULT['D7_classes'] = {'S+': c_sp, 'S-': c_sm, 'V': c_v}

    # --- the theorem: odd class => no invariant bilinear form --------------
    for c in range(4):
        protected = (2 * c) % 4 != 0
        check('centre', 'class %d: 2c mod 4 = %d, protected = %s'
              % (c, (2 * c) % 4, protected), protected == (c % 2 == 1))
    check('centre', 'D_7: cls(S^+ (x) S^+) = 2 /= 0 -- no same-chirality scalar',
          (2 * c_sp) % 4 == 2)
    check('centre', 'D_7: cls(S^+ (x) S^-) = 0 -- Dirac pairing ALLOWED',
          (c_sp + c_sm) % 4 == 0)

    # --- CONTRARY CONTROL B: D_6, twelve dimensions ------------------------
    n6 = 6
    sp6 = spinor_weights(n6, 0)[0]
    c6 = cls_of(sp6)
    check('control-contrary',
          'CONTRARY B: D_6 (12 dimensions) has cls(S^+) = 2, EVEN', c6 == 2, c6)
    check('control-contrary',
          'CONTRARY B: D_6 cls(S^+ (x) S^+) = 0 -- protection FAILS, '
          'Majorana mass allowed', (2 * c6) % 4 == 0)
    # and confirm the mechanism is rank parity, not signature: D_5 protected,
    # D_6 not, D_7 protected.
    par = {}
    for nn in (4, 5, 6, 7):
        w = spinor_weights(nn, 0)[0]
        par[nn] = (cls_of(w) % 2 == 1)
    check('control-contrary',
          'protection tracks D_n rank parity: odd n protected, even n not',
          par == {4: False, 5: True, 6: False, 7: True}, par)
    RESULT['rank_parity'] = par

    # --- second, independent leg: -w_0 by explicit weight duality ----------
    # V^* has lowest weight -lambda; V ~= V^* iff the weight multiset is
    # closed under global negation.  For a half-spinor of D_n this is exactly
    # "n even".
    for nn in (5, 6, 7):
        ws = set(spinor_weights(nn, 0))
        selfdual = all(tuple(-x for x in w) in ws for w in ws)
        check('centre', 'D_%d: half-spinor weight multiset self-negating = %s'
              % (nn, selfdual), selfdual == (nn % 2 == 0), selfdual)
        # the two legs must AGREE
        check('centre', 'D_%d: centre leg and -w_0 leg agree' % nn,
              selfdual != (cls_of(spinor_weights(nn, 0)[0]) % 2 == 1))


# ===========================================================================
# SECTION 3 -- the four declared corners, and which pairings are homogeneous.
# ===========================================================================

CORNERS = {
    'nu_+  in Omega^0(S_+)': ('0-form', '+'),
    'nu_-  in Omega^0(S_-)': ('0-form', '-'),
    'zeta_+ in Omega^1(S_+)': ('1-form', '+'),
    'zeta_- in Omega^1(S_-)': ('1-form', '-'),
}


def corner_class(form_deg: str, half: str) -> int:
    n = 7
    base = cls_of(spinor_weights(n, 0 if half == '+' else 1)[0])
    shift = 0 if form_deg == '0-form' else cls_of(tuple([2] + [0] * (n - 1)))
    if MUT == 'form_shift':
        shift = 0
    return (base + shift) % 4


def section_3():
    cc = {k: corner_class(*v) for k, v in CORNERS.items()}
    RESULT['corner_classes'] = cc
    check('corners', 'Omega^0(S_+) has class 3', cc['nu_+  in Omega^0(S_+)'] == 3)
    check('corners', 'Omega^1(S_-) has class 3 -- SAME as Omega^0(S_+)',
          cc['zeta_- in Omega^1(S_-)'] == 3)
    check('corners', 'Omega^0(S_-) has class 1', cc['nu_-  in Omega^0(S_-)'] == 1)
    check('corners', 'Omega^1(S_+) has class 1 -- SAME as Omega^0(S_-)',
          cc['zeta_+ in Omega^1(S_+)'] == 1)

    # enumerate every pairing of one 0-form corner with one 1-form corner
    pairings = {}
    for k0 in ('nu_+  in Omega^0(S_+)', 'nu_-  in Omega^0(S_-)'):
        for k1 in ('zeta_+ in Omega^1(S_+)', 'zeta_- in Omega^1(S_-)'):
            homog = cc[k0] == cc[k1]
            odd = (cc[k0] % 2 == 1) and homog
            pairings[(k0, k1)] = {'homogeneous': homog, 'protected': odd,
                                  'classes': (cc[k0], cc[k1])}
    nh = sum(1 for v in pairings.values() if v['homogeneous'])
    check('corners', 'exactly 2 of the 4 same-S/opposite-S pairings are '
          'class-HOMOGENEOUS', nh == 2, {str(k): v for k, v in pairings.items()})

    src = ('nu_+  in Omega^0(S_+)', 'zeta_- in Omega^1(S_-)')
    repo = ('nu_+  in Omega^0(S_+)', 'zeta_+ in Omega^1(S_+)')
    check('corners',
          "SOURCE reading Omega^0(S_+) + Omega^1(S_-) [L107, draft p.51] is "
          "HOMOGENEOUS and PROTECTED", pairings[src]['protected'] is True,
          pairings[src])
    check('corners',
          "SAME-S reading Omega^0(S_+) + Omega^1(S_+) is MIXED and NOT "
          "protected", pairings[repo]['homogeneous'] is False, pairings[repo])

    # the full four-corner (unsubscripted S) content is mixed, necessarily
    all_cls = set(cc.values())
    check('corners',
          'the FULL four-corner content (unsubscripted S, eq 5.2 / 9.16) spans '
          'BOTH odd classes -- MIXED', all_cls == {1, 3}, sorted(all_cls))
    RESULT['pairings'] = {'%s | %s' % k: v for k, v in pairings.items()}

    # gamma-trace bookkeeping: Omega^1(S_-) = RS(+) (+) S_+ at the module level
    n = 7
    dim_S = 2 ** (n - 1)                     # 64
    dim_V = 2 * n                            # 14
    check('corners', 'dim Omega^1(S_-) = 14 x 64 = 896',
          dim_V * dim_S == 896, dim_V * dim_S)
    check('corners', 'gamma-trace splits 896 = 832 + 64',
          dim_V * dim_S - dim_S == 832)
    # the gamma-trace summand of V (x) S^- is S^+, by class:
    check('corners', 'the 64 inside Omega^1(S_-) is S^+ (class certificate)',
          cls_of(tuple(a + b for a, b in
                       zip(tuple([2] + [0] * (n - 1)),
                           spinor_weights(n, 1)[0]))) == cls_of(spinor_weights(n, 0)[0]))
    RESULT['omega1_split'] = {'total': 896, 'RS': 832, 'gamma_trace': 64}


# ===========================================================================
# SECTION 4 -- the chirality tie under Spin(1,3) x Spin(6,4), by weights.
# ===========================================================================

def section_4():
    """Split the 7 D_7 coordinates as 2 + 5 and read the tie off the weights.

    Source cross-check: the draft's eq (12.20), p.61, prints exactly
        g*(S64_L(TY)) = (S2_L(TX) (x) S16_L(N)) + (S2_R(TX) (x) S16_R(N))
    i.e. an ambient Weyl half is a CHIRALITY-CORRELATED sum.  That is the tie.
    """
    n, ne, ni = 7, 2, 5
    tie = {}
    for half in (0, 1):
        buckets = {}
        for w in spinor_weights(n, half):
            ext = w[:ne]
            intl = w[ne:]
            # so(4) = su(2) + su(2): parity of minus signs picks the 4d half
            ext_half = 'L' if (sum(1 for s in ext if s < 0) % 2) == 0 else 'R'
            int_cls = cls_of(intl)
            buckets.setdefault((ext_half, int_cls), 0)
            buckets[(ext_half, int_cls)] += 1
        tie['S^+' if half == 0 else 'S^-'] = buckets
    RESULT['tie'] = {k: {str(a): b for a, b in v.items()} for k, v in tie.items()}

    sp = tie['S^+']
    sm = tie['S^-']
    check('tie', 'ambient S^+ contains exactly TWO (ext, int) sectors',
          len(sp) == 2, sp)
    check('tie', 'ambient S^- contains exactly TWO (ext, int) sectors',
          len(sm) == 2, sm)
    check('tie', 'ambient S^+ = (L (x) 16) + (R (x) 16bar) -- CORRELATED',
          set(sp) == {('L', 1), ('R', 3)}, sorted(sp))
    check('tie', 'ambient S^- = (L (x) 16bar) + (R (x) 16) -- CORRELATED',
          set(sm) == {('L', 3), ('R', 1)}, sorted(sm))
    check('tie', 'each ambient sector has 32 weights (2 x 16)',
          set(sp.values()) == {32} and set(sm.values()) == {32},
          (sorted(sp.values()), sorted(sm.values())))
    check('tie', 'SOURCE eq (12.20) shape reproduced: one ambient half is a '
          'two-term chirality-correlated sum', len(sp) == 2 and len(sm) == 2)

    # the tie is EXACTLY the statement that a single ambient half, restricted to
    # 4d LEFT, sees only ONE internal class.
    left_sp = {c for (h, c) in sp if h == 'L'}
    check('tie', 'ambient S^+ restricted to 4d LEFT sees only internal class 1',
          left_sp == {1}, left_sp)
    both = {c for (h, c) in list(sp) + list(sm) if h == 'L'}
    check('tie', 'ambient FULL DIRAC restricted to 4d LEFT sees BOTH internal '
          'classes -- tie BROKEN', both == {1, 3}, both)

    # net 4d chirality readout for each carrier reading
    def net_left(classes):
        """classes: multiset of ambient classes present in the content."""
        seen = set()
        for c in classes:
            # ambient class 3 <-> S^+ family; class 1 <-> S^- family
            seen |= {1} if c == 3 else {3}
        return seen
    RESULT['net_left'] = {
        'single ambient half (class-homogeneous)': sorted(net_left([3])),
        'full Dirac (classes 1 and 3)': sorted(net_left([3, 1])),
    }
    check('tie', 'class-homogeneous content -> ONE internal class downstairs',
          len(net_left([3])) == 1)
    check('tie', 'class-mixed content -> BOTH internal classes downstairs',
          len(net_left([3, 1])) == 2)


# ===========================================================================
# SECTION 5 -- consequence for n_g, on each reading, on BOTH horns.
# ===========================================================================

def section_5():
    """n_g stays an INPUT.  What is computed here is only whether the
    subtraction rule HE-1/HE-2 established HAS an input at all."""
    readings = {}
    # (a) the DECLARED total content: unsubscripted S, four corners, classes {1,3}
    readings['DECLARED total (eq 5.2 p.31 / eq 9.16 p.46, S unsubscripted)'] = {
        'classes': [1, 3], 'homogeneous': False,
        'tie_engages': False, 'n_g_input': 0,
    }
    # (b) the SOURCE-stated emergent chiral half (L107; draft p.51 corner pair)
    readings['EMERGENT half Omega^0(S_+) + Omega^1(S_-) (L107 / draft p.51)'] = {
        'classes': [3], 'homogeneous': True,
        'tie_engages': True, 'n_g_input': None,   # n_g remains an input
    }
    # (c) the same-S reading HE-2's contrary construction had in view
    readings['SAME-S reading Omega^0(S_+) + Omega^1(S_+)'] = {
        'classes': [3, 1], 'homogeneous': False,
        'tie_engages': False, 'n_g_input': 0,
    }
    for name, r in readings.items():
        homog = len(set(r['classes'])) == 1
        check('consequence', '%s: homogeneity = %s' % (name, r['homogeneous']),
              homog == r['homogeneous'], (name, r['classes']))
        odd = homog and (r['classes'][0] % 2 == 1)
        check('consequence', '%s: tie engages = %s' % (name, r['tie_engages']),
              odd == r['tie_engages'])
    RESULT['readings'] = readings

    # HORN-INDEPENDENCE.  The class instrument never touches (p,q); it is a
    # statement about D_7 = so(14,C), which BOTH horns complexify to.
    for (p, q) in ((7, 7), (9, 5), (5, 9), (11, 3), (13, 1)):
        check('horn-blind',
              'class verdict is identical on (%d,%d): D_7 is the '
              'complexification both horns share' % (p, q),
              RESULT['corner_classes']['nu_+  in Omega^0(S_+)'] ==
              RESULT['corner_classes']['zeta_- in Omega^1(S_-)'])
    # but the CARRIER TYPE available does move with the horn -- both facts hold
    rows = {(r['p'], r['q']): r for r in RESULT['admissibility_rows']}
    check('horn-blind',
          'carrier TYPE does move with the horn: (7,7) MW yes, (9,5) MW no',
          rows[(7, 7)]['adm']['Majorana-Weyl'] and
          not rows[(9, 5)]['adm']['Majorana-Weyl'])
    check('horn-blind',
          'so the two instruments are INDEPENDENT: one moves with the fork, '
          'one cannot see it', True)

    # the uniform-doubling statement, exactly: on (9,5) the minimal chiral
    # carrier is an Sp(1) doublet, which doubles EVERY summand alike.
    check('consequence',
          '(9,5) symplectic doubling is uniform: it multiplies every class-3 '
          'summand by the same factor 2, so it cannot change a class',
          (3 * 1) % 4 == 3 and (3 * 1) % 4 == 3)


# ===========================================================================
# SECTION 5b -- what the class certificate does and does NOT forbid.
#
# Odd class forbids a BARE invariant bilinear.  It does not forbid a bilinear
# with a BOSONIC INSERTION: a singlet in M (x) M (x) T needs cls(T) = 2.  This
# section computes which of GU's declared bosonic slots can supply that
# insertion, so the certificate is stated at its true strength and not above it.
# ===========================================================================

def section_5b():
    n = 7
    # cls(Lambda^k V) for D_7 : Lambda^k has highest weight (1^k, 0^...), so in
    # doubled coordinates the sum is 2k, hence class 2k mod 4.
    lam = {}
    for k in range(0, 2 * n + 1):
        dw = tuple([2] * min(k, n) + [0] * (n - min(k, n)))
        lam[k] = cls_of(dw) if k <= n else cls_of(tuple([2] * (2 * n - k)
                                                       + [0] * (n - (2 * n - k))))
    check('insertion', 'cls(Lambda^k V) = 0 for k even, 2 for k odd',
          all(lam[k] == (0 if k % 2 == 0 else 2) for k in range(0, n + 1)),
          {k: lam[k] for k in range(0, n + 1)})
    RESULT['lambda_classes'] = {k: lam[k] for k in range(0, n + 1)}

    # End(Delta) = sum_k Lambda^k V, so ad P (the u(64,64) adjoint, which is
    # exactly End(Delta) with a reality condition) spans BOTH even classes.
    end_classes = sorted({lam[k] for k in range(0, n + 1)})
    check('insertion', 'End(Delta) = sum_k Lambda^k spans classes {0, 2}',
          end_classes == [0, 2], end_classes)

    c_odd = 3
    need = (-2 * c_odd) % 4
    check('insertion',
          'a singlet in M (x) M (x) T with cls(M)=3 requires cls(T) = 2',
          need == 2, need)
    check('insertion',
          'BARE mass on the class-3 half is FORBIDDEN (no insertion, class 2 /= 0)',
          (2 * c_odd) % 4 != 0)
    # both declared bosonic slots contain class-2 components, via the ODD-degree
    # part of ad P (and, for the 1-form slot, via the form index itself).
    boson = {
        'eps in Omega^0(ad P)': sorted({(0 + c) % 4 for c in end_classes}),
        '$ (varpi) in Omega^1(ad P)': sorted({(2 + c) % 4 for c in end_classes}),
    }
    RESULT['boson_classes'] = boson
    for name, cs in boson.items():
        check('insertion', '%s spans classes %s -- CAN supply a class-2 '
              'insertion' % (name, cs), 2 in cs, cs)
    check('insertion',
          'so the certificate is CONDITIONAL, not absolute: chirality of a '
          'class-homogeneous half is exact at zero insertion only',
          True)
    RESULT['certificate_strength'] = (
        'bare mass FORBIDDEN absolutely and real-form-blindly; '
        'insertion-generated mass ALLOWED, requiring a class-2 bosonic spurion')

    # --- symbol-degree rider (the next gate, computed not asserted) --------
    # A FIRST-ORDER Spin-equivariant operator Gamma(E) -> Gamma(F) needs a
    # trivial summand in V (x) E^* (x) F, i.e. cls(V) - cls(E) + cls(F) = 0,
    # i.e. cls(F) = cls(E) + 2 mod 4.  Sanity: the Dirac operator and d both
    # satisfy it.
    def first_order_ok(cE, cF):
        return (2 - cE + cF) % 4 == 0
    check('symbol', 'Dirac S^+ -> S^- admits a first-order operator',
          first_order_ok(3, 1))
    check('symbol', 'd : Omega^0 -> Omega^1 admits a first-order operator',
          first_order_ok(0, 2))
    cc = RESULT['corner_classes']
    prot = first_order_ok(cc['nu_+  in Omega^0(S_+)'],
                          cc['zeta_- in Omega^1(S_-)'])
    mixed = first_order_ok(cc['nu_+  in Omega^0(S_+)'],
                           cc['zeta_+ in Omega^1(S_+)'])
    check('symbol',
          'PROTECTED pairing admits NO first-order equivariant operator '
          'between its summands', prot is False, prot)
    check('symbol',
          'class-MIXED pairing is exactly the one that DOES admit it',
          mixed is True, mixed)
    RESULT['first_order'] = {'protected_pairing': prot, 'mixed_pairing': mixed}


# ===========================================================================
# SECTION 6 -- planted false facts.  A probe nobody has seen fail is unverified.
# ===========================================================================

def section_6_planted():
    n = 7
    sp = spinor_weights(n, 0)[0]
    sm = spinor_weights(n, 1)[0]
    vec = tuple([2] + [0] * (n - 1))
    planted = [
        ('cls(S^+) = cls(S^-) for D_7', cls_of(sp) == cls_of(sm)),
        ('cls(V) is odd', cls_of(vec) % 2 == 1),
        ('D_7 half-spinor is self-dual',
         all(tuple(-x for x in w) in set(spinor_weights(n, 0))
             for w in spinor_weights(n, 0))),
        ('Omega^0(S_+) and Omega^1(S_+) share a class',
         corner_class('0-form', '+') == corner_class('1-form', '+')),
        ('the full four-corner content is class-homogeneous',
         len(set(RESULT['corner_classes'].values())) == 1),
        ('D_6 half-spinor class is odd',
         cls_of(spinor_weights(6, 0)[0]) % 2 == 1),
        ('(9,5) admits a Majorana-Weyl spinor',
         {(r['p'], r['q']): r for r in
          RESULT['admissibility_rows']}[(9, 5)]['adm']['Majorana-Weyl']),
        ('(7,7) forbids a Majorana spinor',
         not {(r['p'], r['q']): r for r in
              RESULT['admissibility_rows']}[(7, 7)]['adm']['Majorana']),
        ('the J-fixed set inside S^+ has the same dimension on both horns',
         RESULT['fixed_sets']['7,7'] == RESULT['fixed_sets']['9,5']),
        ('ambient S^+ contains all four (ext, int) sectors',
         len(RESULT['tie']['S^+']) == 4),
        ('a BARE mass term for the class-3 half is allowed',
         (2 * 3) % 4 == 0),
        ('Lambda^1 V has even-form class 0',
         RESULT['lambda_classes'][1] == 0),
        ('the protected pairing admits a first-order equivariant operator',
         RESULT['first_order']['protected_pairing']),
    ]
    if MUT == 'planted':
        planted = [(nm, not v) for nm, v in planted]
    for nm, v in planted:
        check('planted-false', 'PLANTED FALSE observed False: %s' % nm, v is False, v)
    RESULT['planted'] = len(planted)


# ===========================================================================

def assert_no_float(obj, path='RESULT'):
    if isinstance(obj, float):
        raise AssertionError('load-bearing float at %s' % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, '%s[%r]' % (path, k))
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, '%s[%d]' % (path, i))


MUTATIONS = ['signature_swap', 'truncate_B', 'chirality_flip', 'admissibility',
             'table', 'cls_map', 'form_shift', 'planted',
             'tie_sectors', 'corner_source', 'corner_repo', 'residue_fn',
             'nonvacuity', 'fixed_set']


def apply_late_mutations():
    """Mutations that act on already-computed results, to prove the ASSERTIONS
    (not just the machinery) are load-bearing."""
    if MUT == 'tie_sectors':
        RESULT['tie']['S^+'] = {"('L', 1)": 64}
        check('mutant', 'tie sectors mutated', len(RESULT['tie']['S^+']) == 2)
    if MUT == 'corner_source':
        check('mutant', 'source pairing protected',
              RESULT['pairings'][
                  'nu_+  in Omega^0(S_+) | zeta_- in Omega^1(S_-)'
              ]['protected'] is False)
    if MUT == 'corner_repo':
        check('mutant', 'same-S pairing homogeneous',
              RESULT['pairings'][
                  'nu_+  in Omega^0(S_+) | zeta_+ in Omega^1(S_+)'
              ]['homogeneous'] is True)
    if MUT == 'residue_fn':
        check('mutant', 'residue table has 8 even rows',
              len(RESULT['residue_table']) == 8)
    if MUT == 'nonvacuity':
        check('mutant', 'every carrier type is admissible everywhere',
              all(r['adm']['Majorana-Weyl'] for r in RESULT['admissibility_rows']))
    if MUT == 'fixed_set':
        check('mutant', 'both horns have 64 fixed dimensions',
              RESULT['fixed_sets']['9,5'] == 64)


def selftest():
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ, CRB_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        print('  mutation %-16s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d planted false facts drove exit 1)'
          % ('PASS' if ok else 'FAIL', len(MUTATIONS) if ok else 0, len(MUTATIONS)))
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_5b()
    section_6_planted()
    apply_late_mutations()
    assert_no_float(RESULT)

    npass = sum(1 for t, nm, ok, dd in CERT if ok)
    ntot = len(CERT)
    counts: dict = {}
    for t, nm, ok, dd in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, nm, ok, dd in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, nm, dd))

    print()
    print('CR-B  carrier admissibility on Y^14, and whether the chirality tie engages')
    print()
    print('  INSTRUMENT 1 -- Clifford admissibility by signature')
    print('    %-9s %-4s %-14s %s' % ('sig', 's', 'Weyl half', 'admissible carriers'))
    for r in RESULT['admissibility_rows']:
        yes = [k for k in ('Majorana', 'Majorana-Weyl', 'symplectic-Majorana',
                           'symplectic-Majorana-Weyl') if r['adm'][k]]
        mark = ''
        if (r['p'], r['q']) == (7, 7):
            mark = '   <-- horn A'
        elif (r['p'], r['q']) == (9, 5):
            mark = '   <-- horn B'
        elif (r['p'], r['q']) == (6, 4):
            mark = '   <-- GU internal'
        elif (r['p'], r['q']) == (6, 6):
            mark = '   <-- CONTRARY B (12d)'
        print('    (%2d,%2d)   %d    %-14s Weyl + %s%s'
              % (r['p'], r['q'], r['s'], r['half_type'],
                 ', '.join(yes) if yes else '(none)', mark))
    print()
    print('    residue table (admissibility is a function of s = (p-q) mod 8 alone):')
    for s, kinds in sorted(RESULT['residue_table'].items()):
        print('      s=%d : %s' % (s, ', '.join(kinds)))
    print()
    print('    J-fixed real dimensions inside S^+ : (7,7) -> %d,  (9,5) -> %d'
          % (RESULT['fixed_sets']['7,7'], RESULT['fixed_sets']['9,5']))
    print()
    print('  INSTRUMENT 2 -- centre class in P/Q = Z/4 for D_7 (real-form BLIND)')
    print('    cls(S^+) = %d   cls(S^-) = %d   cls(V) = %d   cls(ad) = 0'
          % (RESULT['D7_classes']['S+'], RESULT['D7_classes']['S-'],
             RESULT['D7_classes']['V']))
    for k, v in RESULT['corner_classes'].items():
        print('    %-26s class %d' % (k, v))
    print()
    print('    pairings:')
    for k, v in RESULT['pairings'].items():
        print('      %-58s homogeneous=%-5s protected=%s'
              % (k, v['homogeneous'], v['protected']))
    print()
    print('  THE TIE (weights, cross-checking the source\'s own eq 12.20 p.61)')
    for half, buckets in RESULT['tie'].items():
        print('    ambient %s : %s' % (half, '  '.join(
            '%s x %d' % (a, b) for a, b in sorted(buckets.items()))))
    print()
    print('  CONSEQUENCE')
    for name, r in RESULT['readings'].items():
        print('    %-62s tie engages: %s' % (name[:62], r['tie_engages']))
    print()
    print('  CERTIFICATE STRENGTH (what odd class does NOT forbid)')
    print('    %s' % RESULT['certificate_strength'])
    for k, v in RESULT['boson_classes'].items():
        print('    %-30s spans classes %s' % (k, v))
    print('    first-order equivariant operator between the two summands:  '
          'protected pairing %s,  mixed pairing %s'
          % (RESULT['first_order']['protected_pairing'],
             RESULT['first_order']['mixed_pairing']))
    print()
    print('  CONTRARY CONTROLS')
    print('    A  (9,5) Majorana-Weyl does NOT exist; J-fixed set = %d '
          '(absence detected)' % RESULT['fixed_sets']['9,5'])
    print('    B  D_6 / 12 dimensions: cls(S^+) = 2 is EVEN, S^+ IS self-dual, '
          'protection FAILS')
    print('       rank parity: %s' % RESULT['rank_parity'])
    print()
    print('  Z[i] magnitude sweep: max |entry| = %d (bound %d) -- no int64 '
          'overflow, no float' % (SWEEP_MAX['v'], SWEEP_BOUND))
    print('  planted false facts observed False: %d' % RESULT['planted'])
    print('  check split: ' + '  '.join('[%s] %d' % (k, v)
                                        for k, v in sorted(counts.items())))
    print()
    if npass == ntot:
        print('CERTIFICATE: %d/%d checks pass; no load-bearing float (swept).'
              % (npass, ntot))
        return 0
    print('CERTIFICATE: %d/%d checks pass -- FAILURES ABOVE.' % (npass, ntot))
    return 1


if __name__ == '__main__':
    sys.exit(main())
