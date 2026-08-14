#!/usr/bin/env python3
"""Joe-directed channel 3, gate MJ-2: is there a CARRIER for the 126 VEV?

MJ-1 established that the SU(5)-singlet direction of the 126 gives an exact,
symmetric, rank-one Majorana block on nu_R.  That result is conditional on a
VEV.  This probe asks whether GU's own field content contains anything that
could carry one.

GU native field content (paper 5.1-5.2, repo candidate 2B):

              Omega^0            Omega^1
    ad        eps (gauge field)  $ (displacement)      <- bosonic
    S/        nu  (Dirac)        zeta (Rarita-Schwinger) <- fermionic

A Lorentz-scalar VEV cannot carry a free 4d index, so every form index must be
internal.  Hence the only Lorentz-scalar internal content available is:

    eps :  Lambda^2(10)            = the internal adjoint, 45
    $   :  Lambda^1(10) (x) Lambda^2(10) = 10 (x) 45

and the question is whether the 126 occurs in either.  nu and zeta are 4d
spinors, so an elementary VEV for them breaks Lorentz invariance; they are
excluded on Lorentz grounds and treated only as composites in MJ-3.

METHOD.  Exact multiplicities by the Racah/Klimyk formula

    n_lambda(W) = sum_{w in Weyl} det(w) * m_W(lambda + rho - w.rho)

over the Weyl group of D5 (order 1920: signed permutations with an even
number of sign changes).  All weights are integer 5-tuples and every step is
exact integer arithmetic.  No floating point, no character tables trusted
from outside -- the weight multisets are enumerated from scratch.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 5                       # rank of D5 = so(10)
RHO = (4, 3, 2, 1, 0)       # rho for D_n = (n-1, ..., 1, 0)


# --- Weyl group of D5: signed permutations with an even number of sign flips
def weyl_d5() -> list[tuple[tuple[int, ...], int]]:
    out = []
    for perm in permutations(range(N)):
        # sign of the permutation
        sgn, seen = 1, list(perm)
        for i in range(N):
            for j in range(i + 1, N):
                if seen[i] > seen[j]:
                    sgn = -sgn
        for flips in product((1, -1), repeat=N):
            if flips.count(-1) % 2:
                continue  # D_n keeps only even sign changes
            out.append((perm, sgn), ) if False else None
            out.append(((perm, flips), sgn))
    return out


WEYL = weyl_d5()


def apply_w(w, vec: tuple[int, ...]) -> tuple[int, ...]:
    perm, flips = w
    # (w.v)_i = flips_i * v_{perm_i}
    return tuple(flips[i] * vec[perm[i]] for i in range(N))


check("Weyl group of D5 has order 1920", len(WEYL) == 1920)
check("all D5 Weyl elements have an even number of sign flips",
      all(f.count(-1) % 2 == 0 for (_, f), _ in WEYL))


# --- weight multisets, enumerated from scratch -----------------------------
# The vector 10 has weights +-e_i.  Basis vectors are indexed by (i, sign).
VEC_BASIS = [tuple((s if k == i else 0) for k in range(N))
             for i in range(N) for s in (1, -1)]
check("vector rep 10 has 10 weights", len(VEC_BASIS) == 10)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def wedge_weights(k: int) -> Counter:
    """Weight multiset of Lambda^k of the 10."""
    c = Counter()
    for sub in combinations(VEC_BASIS, k):
        wt = (0,) * N
        for v in sub:
            wt = add(wt, v)
        c[wt] += 1
    return c


def tensor_weights(a: Counter, b: Counter) -> Counter:
    c = Counter()
    for wa, ma in a.items():
        for wb, mb in b.items():
            c[add(wa, wb)] += ma * mb
    return c


LAM = {k: wedge_weights(k) for k in range(6)}
for k in range(6):
    from math import comb
    check(f"Lambda^{k}(10) weight count == C(10,{k})",
          sum(LAM[k].values()) == comb(10, k))


# --- Racah / Klimyk multiplicity ------------------------------------------
def multiplicity(lam: tuple[int, ...], W: Counter) -> int:
    total = 0
    for w, sgn in WEYL:
        shifted = add(lam, RHO)
        target = tuple(x - y for x, y in zip(shifted, apply_w(w, RHO)))
        m = W.get(target)
        if m:
            total += sgn * m
    return total


# --- Weyl dimension formula, to certify which highest weight is which ------
POS_ROOTS = []
for i in range(N):
    for j in range(i + 1, N):
        e = [0] * N
        e[i], e[j] = 1, 1
        POS_ROOTS.append(tuple(e))
        e2 = [0] * N
        e2[i], e2[j] = 1, -1
        POS_ROOTS.append(tuple(e2))
check("D5 has 20 positive roots", len(POS_ROOTS) == 20)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def weyl_dim(lam: tuple[int, ...]) -> int:
    num = den = 1
    lr = add(lam, RHO)
    for a in POS_ROOTS:
        num *= dot(lr, a)
        den *= dot(RHO, a)
    assert num % den == 0
    return num // den


HW = {
    "10": (1, 0, 0, 0, 0),
    "45": (1, 1, 0, 0, 0),
    "120": (1, 1, 1, 0, 0),
    "210": (1, 1, 1, 1, 0),
    "126": (1, 1, 1, 1, 1),
    "126bar": (1, 1, 1, 1, -1),
    "320": (2, 1, 0, 0, 0),   # = h.w.(10) + h.w.(45), the Cartan piece of 10 (x) 45
}
for name, lam in HW.items():
    want = int(name.replace("bar", ""))
    check(f"Weyl dimension of highest weight {lam} is {want}", weyl_dim(lam) == want)

# Sanity: the method reproduces the wedge tower exactly.
check("mult(45 in Lambda^2) == 1", multiplicity(HW["45"], LAM[2]) == 1)
check("mult(120 in Lambda^3) == 1", multiplicity(HW["120"], LAM[3]) == 1)
check("mult(210 in Lambda^4) == 1", multiplicity(HW["210"], LAM[4]) == 1)
check("POSITIVE CONTROL: mult(126 in Lambda^5) == 1",
      multiplicity(HW["126"], LAM[5]) == 1)
check("POSITIVE CONTROL: mult(126bar in Lambda^5) == 1",
      multiplicity(HW["126bar"], LAM[5]) == 1)
check("Lambda^5 = 126 + 126bar exactly (252)", 126 + 126 == sum(LAM[5].values()))


# --- THE GATE --------------------------------------------------------------
# Only a genuine internal 5-form can carry the 126: it appears in no other
# wedge power.
wedge_profile = {k: multiplicity(HW["126"], LAM[k]) for k in range(6)}
check("126 occurs in NO Lambda^k(10) except k = 5",
      [wedge_profile[k] for k in range(6)] == [0, 0, 0, 0, 0, 1])

# eps : Omega^0 (x) ad  ->  Lorentz-scalar internal content = Lambda^2(10) = 45
eps_content = LAM[2]
check("eps Lorentz-scalar internal content has dimension 45",
      sum(eps_content.values()) == 45)
check("GATE: mult(126 in eps content) == 0", multiplicity(HW["126"], eps_content) == 0)
check("GATE: mult(126bar in eps content) == 0",
      multiplicity(HW["126bar"], eps_content) == 0)

# $ : Omega^1 (x) ad  ->  Lorentz-scalar internal content = 10 (x) 45
disp_content = tensor_weights(LAM[1], LAM[2])
check("$ Lorentz-scalar internal content has dimension 450",
      sum(disp_content.values()) == 450)
check("GATE: mult(126 in $ content) == 0", multiplicity(HW["126"], disp_content) == 0)
check("GATE: mult(126bar in $ content) == 0",
      multiplicity(HW["126bar"], disp_content) == 0)

# Exhibit the full decomposition of 10 (x) 45 so the absence is legible.
d10 = multiplicity(HW["10"], disp_content)
d120 = multiplicity(HW["120"], disp_content)
d320 = multiplicity(HW["320"], disp_content)
check("10 (x) 45 = 10 + 120 + 320 exactly",
      (d10, d120, d320) == (1, 1, 1) and 10 + 120 + 320 == 450)

# Robustness against the tilted structure group: any H inside Spin(7,7) has
# ad(H) a SUBrepresentation of Lambda^2(V14), whose Lorentz-scalar internal
# part is Lambda^2(10).  Multiplicity is monotone under subrepresentation, so
# mult(126) == 0 there forces mult(126) == 0 for every such ad(H).
check("tilted-group robustness: 126 absent from the full Lambda^2(10)",
      multiplicity(HW["126"], LAM[2]) == 0)

# Even-degree lemma, verified rather than asserted: no even wedge power carries
# the 126, so no ad-valued form of even internal degree can either.
check("no even Lambda^{2j}(10) carries the 126",
      all(multiplicity(HW["126"], LAM[k]) == 0 for k in (0, 2, 4)))


# --- What DOES carry it: the composite channel (hands off to MJ-3) ---------
# MJ-1 showed the nu (x) nu bilinear reaches the 126.  Confirm here from the
# independent weight side that Lambda^5 is the unique wedge home, so a
# condensate is the only remaining elementary-field-free route.
check("the 126 has a unique wedge home, Lambda^5",
      sum(1 for k in range(6) if multiplicity(HW["126"], LAM[k])) == 1)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"126 multiplicity profile over Lambda^k(10), k=0..5: "
      f"{[wedge_profile[k] for k in range(6)]}")
print(f"126 in eps (Omega^0 (x) ad): {multiplicity(HW['126'], eps_content)}")
print(f"126 in $   (Omega^1 (x) ad): {multiplicity(HW['126'], disp_content)}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
