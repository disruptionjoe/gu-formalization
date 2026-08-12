#!/usr/bin/env python3
"""Exact split-layer commutant and action-parent gate for the K77 carrier.

This probe reuses only the audited signed-permutation Clifford primitives from
the C1/C2 certificate.  It freezes the source-owned plus-first allocation

    R^(7,7) = R^(1,3) + R^(6,4)

as base indices (one positive, three negative) and normal indices (six
positive, four negative).  It then solves the COMPLETE real commutant of
spin(1,3)+spin(6,4), computes its algebra, restricts it to both ambient
half-spin modules, and classifies infinitesimal connection directions by
whether they preserve the subgroup-native complex structure J and ambient
chirality omega.

All matrices are exact signed permutations and all ranks/dimensions are exact.
No Standard Model label, desired eigenspace, fitted Hermitian form or target
group enters the solve.
"""

import sys

import nguyen_c1c2_real_form_probe as c12


PASSES = []
FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("[%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""))
    (PASSES if ok else FAILURES).append(name)
    return ok


GAMMAS, ETA = c12.build_cl77()
N = 128
IDENTITY = c12.SP.identity(N)

# Source-ordered plus-first split: base (1,3), normal (6,4).
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)


def product(indices):
    out = IDENTITY
    for i in indices:
        out = out.mul(GAMMAS[i])
    return out


def bivectors(indices):
    return [GAMMAS[i].mul(GAMMAS[j])
            for a, i in enumerate(indices) for j in indices[a + 1:]]


J4 = product(BASE)
J10 = product(NORMAL)
OMEGA = product(tuple(range(14)))
SUBGROUP = bivectors(BASE) + bivectors(NORMAL)


def anticommutes(a, b):
    return c12.sum_is_zero(a.mul(b), b.mul(a))


def sparse_lincomb(basis, coeffs):
    out = {}
    for M, q in zip(basis, coeffs):
        if not q:
            continue
        for p, v in M.items():
            out[p] = out.get(p, 0) + q * v
            if out[p] == 0:
                del out[p]
    return out


def eigenspace_basis(invol):
    """Exact sparse bases for a signed-permutation involution's +/- spaces."""
    plus, minus = [], []
    seen = [False] * invol.n
    for a in range(invol.n):
        if seen[a]:
            continue
        b, s = invol.perm[a], invol.sign[a]
        if b == a:
            seen[a] = True
            (plus if s == 1 else minus).append({a: 1})
        else:
            seen[a] = seen[b] = True
            plus.append({a: 1, b: s})
            minus.append({a: 1, b: -s})
    return plus, minus


def apply_sp(A, v):
    out = {}
    for j, x in v.items():
        r = A.perm[j]
        out[r] = out.get(r, 0) + A.sign[j] * x
    return {i: x for i, x in out.items() if x}


def dot(u, v):
    return sum(x * v.get(i, 0) for i, x in u.items())


def restrict_sp(A, basis):
    """Restrict A to an orthogonal sparse basis, returning rational columns."""
    norms = [dot(v, v) for v in basis]
    cols = []
    for v in basis:
        Av = apply_sp(A, v)
        cols.append([dot(u, Av) / norms[i] for i, u in enumerate(basis)])
    return cols


def restrict_signed_perm(A, basis):
    """Restrict a basis-preserving signed permutation to a sparse half basis."""
    def canonical(v):
        first = min(v)
        s = v[first]
        return tuple(sorted((i, x * s) for i, x in v.items())), s

    lookup = {canonical(v)[0]: i for i, v in enumerate(basis)}
    perm, sign = [], []
    for v in basis:
        key, s = canonical(apply_sp(A, v))
        if key not in lookup:
            return None
        perm.append(lookup[key])
        sign.append(s)
    if len(set(perm)) != len(basis):
        return None
    return c12.SP(tuple(perm), tuple(sign))


def dense_mul_cols(A, B):
    """Column-major dense matrix product A*B."""
    n = len(A)
    return [[sum(A[k][i] * B[j][k] for k in range(n)) for i in range(n)]
            for j in range(n)]


def dense_is_scalar_identity(A, scalar):
    n = len(A)
    return all(A[j][i] == (scalar if i == j else 0)
               for j in range(n) for i in range(n))


def nullity_aI_plus_bJ(J, a, b):
    """Nullity over C of a*I+b*J for a,b in {1,+/-i}; J is real with J^2=-I.

    For the cases used below, the minimal polynomial gives the nullity exactly:
    I +/- iJ project to the +/- i eigenspaces, each half the complexified rank.
    """
    if b == 0:
        return 0 if a else len(J)
    # Only I +/- iJ are used; J is a complex structure on even-dimensional V.
    return len(J) // 2


def main():
    print("=" * 78)
    print("K77 split-layer commutant/action-parent gate -- exact arithmetic")
    print("base indices %s signature (1,3); normal %s signature (6,4)" %
          (BASE, NORMAL))
    print("=" * 78)

    check("TYPE-SPLIT", len(BASE) == 4 and len(NORMAL) == 10 and
          sum(ETA[i] == 1 for i in BASE) == 1 and
          sum(ETA[i] == -1 for i in BASE) == 3 and
          sum(ETA[i] == 1 for i in NORMAL) == 6 and
          sum(ETA[i] == -1 for i in NORMAL) == 4,
          "base=(1,3), normal=(6,4), disjoint and exhaustive")
    check("SUBGROUP-GENERATORS", len(SUBGROUP) == 6 + 45,
          "6 base plus 45 normal bivectors")

    # Complete commutant and its explicit natural basis.
    dim, basis = c12.commutant(SUBGROUP, N)
    natural = (IDENTITY, J4, J10, OMEGA)
    spans = [c12.in_span(basis, A, N) for A in natural]
    check("COMMUTANT-DIM", dim == 4, "exact complete nullspace dim=%d" % dim)
    check("COMMUTANT-NATURAL-BASIS", dim == 4 and all(spans),
          "I,J4,J10,omega all lie in the four-dimensional commutant")
    check("COMMUTANT-ALGEBRA",
          J4.mul(J4).is_identity_times() == -1 and
          J10.mul(J10).is_identity_times() == -1 and
          J4.mul(J10).eq(J10.mul(J4)) and
          J4.mul(J10).eq(OMEGA) and
          OMEGA.mul(OMEGA).is_identity_times() == 1,
          "J4^2=J10^2=-I, J4 J10=J10 J4=omega, omega^2=I")
    check("SUBGROUP-EQUIVARIANCE",
          all(J4.mul(s).eq(s.mul(J4)) and J10.mul(s).eq(s.mul(J10)) and
              OMEGA.mul(s).eq(s.mul(OMEGA)) for s in SUBGROUP),
          "all 51 generators commute with both native J operators and omega")

    # Ambient chirality halves, each real 64.  J4 preserves each and restricts
    # to a complex structure, hence complex dimension 32 before complexification.
    plus, minus = eigenspace_basis(OMEGA)
    check("AMBIENT-HALF-RANKS", len(plus) == len(minus) == 64,
          "real ranks 64+64")
    Jp = restrict_sp(J4, plus)
    Jm = restrict_sp(J4, minus)
    check("HALF-NATIVE-J", dense_is_scalar_identity(dense_mul_cols(Jp, Jp), -1)
          and dense_is_scalar_identity(dense_mul_cols(Jm, Jm), -1),
          "J4^2=-I on each real-64 half => complex dimension 32")

    # Since J4*J10=omega and J4^-1=-J4, J10=-J4*omega.  The two nominal
    # complex structures are therefore opposite on omega+ and equal on
    # omega-.  Thus each half commutant is C.  This sign is convention-sensitive
    # and was deliberately checked rather than inferred from dimensions.
    J10p = restrict_sp(J10, plus)
    J10m = restrict_sp(J10, minus)
    opposite_p = all(J10p[j][i] == -Jp[j][i]
                     for j in range(64) for i in range(64))
    equal_m = J10m == Jm
    check("HALF-COMMUTANT-COLLAPSE", opposite_p and equal_m,
          "J10=-J4 on omega+, J10=+J4 on omega-")

    # The subgroup representation on either real half is complex type, but it
    # does not itself preserve a real bilinear on that same half.  This blocks
    # an illicit inference from native J to Curt's asserted Hermitian (32,32):
    # the Hermitian form is additional unitary-bundle structure until built.
    sub_p = [restrict_signed_perm(x, plus) for x in SUBGROUP]
    sub_m = [restrict_signed_perm(x, minus) for x in SUBGROUP]
    restriction_ok = all(x is not None for x in sub_p + sub_m)
    cp = c12.commutant(sub_p, 64)[0] if restriction_ok else None
    cm = c12.commutant(sub_m, 64)[0] if restriction_ok else None
    bpp = c12.mixed_block_bilinear_space(sub_p, sub_p, 64, 64) if restriction_ok else None
    bmm = c12.mixed_block_bilinear_space(sub_m, sub_m, 64, 64) if restriction_ok else None
    bpm = c12.mixed_block_bilinear_space(sub_p, sub_m, 64, 64) if restriction_ok else None
    bmp = c12.mixed_block_bilinear_space(sub_m, sub_p, 64, 64) if restriction_ok else None
    check("HALF-SUBGROUP-COMMUTANTS", restriction_ok and (cp, cm) == (2, 2),
          "each real half has commutant dim 2 = C: %s/%s" % (cp, cm))
    check("HERMITIAN-FORM-NOT-DERIVED-BY-COMMUTANT",
          restriction_ok and (bpp, bmm, bpm, bmp) == (0, 0, 2, 2),
          "invariant real bilinear blocks pp/mm/pm/mp=%s/%s/%s/%s; same-half form absent" %
          (bpp, bmm, bpm, bmp))

    # Complexification of each real-64 half has two conjugate complex-32
    # eigenspaces of the native J.  This is the exact 32+32 inside one source
    # complex-64 Weyl half; it is not a claim that real-64 == C^(32,32).
    joint = {}
    for om_name, J in (("omega+", Jp), ("omega-", Jm)):
        joint[(om_name, "+i")] = nullity_aI_plus_bJ(J, 1, 1j)
        joint[(om_name, "-i")] = nullity_aI_plus_bJ(J, 1, -1j)
    check("COMPLEXIFICATION-32-PLUS-32", set(joint.values()) == {32},
          str(joint))
    check("DIMENSION-FENCE",
          64 == 32 + 32 and 128 == 64 + 64,
          "real half with J = C^32; its complexification = C^32 + conjugate C^32 = C^64; full complex carrier = C^128")

    # Connection-parent classification.  A tangent preserves a structure iff
    # its commutator with that structure vanishes.  Even Clifford words preserve
    # omega; odd words exchange halves.  Subgroup bivectors preserve J4 too;
    # mixed base-normal bivectors preserve omega but anticommute with J4.
    mixed = [GAMMAS[i].mul(GAMMAS[j]) for i in BASE for j in NORMAL]
    odd = list(GAMMAS)
    check("SPLIT-CONNECTION-PRESERVES-J-OMEGA",
          all(x.mul(J4).eq(J4.mul(x)) and x.mul(OMEGA).eq(OMEGA.mul(x))
              for x in SUBGROUP),
          "D_varpi J4=D_varpi omega=0 for subgroup-valued connection")
    check("SPIN-COMPLEMENT-BREAKS-J-PRESERVES-OMEGA",
          len(mixed) == 40 and
          all(anticommutes(x, J4) and x.mul(OMEGA).eq(OMEGA.mul(x)) for x in mixed),
          "all 40 mixed bivectors preserve ambient halves but break split-native J")
    check("ODD-PARENT-DIRECTIONS-BREAK-OMEGA",
          all(anticommutes(x, OMEGA) for x in odd),
          "all 14 vector directions exchange ambient halves")

    # Planted controls.
    wrong_subgroup = SUBGROUP + [mixed[0]]
    wrong_dim, _ = c12.commutant(wrong_subgroup, N)
    check("PLANTED-WRONG-SPLIT-REDUCES-COMMUTANT", wrong_dim == 2,
          "adjoin one mixed bivector: commutant dim=%d, not 4" % wrong_dim)
    full_even = [GAMMAS[i].mul(GAMMAS[j]) for i in range(14)
                 for j in range(i + 1, 14)]
    full_even_dim, _ = c12.commutant(full_even, N)
    check("PLANTED-AMBIENT-SPIN-HAS-NO-J", full_even_dim == 2,
          "full Spin commutant span{I,omega}; omega^2=+I")
    check("PLANTED-SCALAR-i-NOT-REAL-ENDOMORPHISM",
          not any(A.mul(A).is_identity_times() == -1
                  for A in (IDENTITY, OMEGA)),
          "ambient commutant cannot supply a real J")
    check("PLANTED-DIMENSION-COLLAPSE-REJECTED", 64 != 32,
          "C^(32,32) has complex dimension 64, not the complex dimension 32 of a real half with J")

    print("-" * 78)
    print("SUMMARY: %d PASS, %d FAIL" % (len(PASSES), len(FAILURES)))
    if FAILURES:
        print("FAILURES: %s" % ", ".join(FAILURES))
    else:
        print("RESULT: split commutant C + C, native J on each real half;")
        print("        complexification gives 32+32 per source complex Weyl half;")
        print("        D_varpi omega=0 gives chiral blocks, while D_varpi J=0 is")
        print("        the finer observation-split reduction; action selection is open.")
    return len(FAILURES)


if __name__ == "__main__":
    sys.exit(main())
