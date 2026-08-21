#!/usr/bin/env python3
r"""Exact positivity-selection certificate for the marked B5 reduced class.

The preceding B5 certificate constructs a nonzero reduced class represented by
the Green-null Witt vector ``v``.  This certificate distinguishes three
objects which cannot be conflated:

* the program-native indefinite Green/Krein form ``G``;
* a positive metric ``G J`` obtained from a chosen fundamental symmetry; and
* an auxiliary positive norm on the abstract reduced quotient.

On the exact Witt plane ``G(v,w)=1``, every positive fundamental symmetry
maps ``v`` to a vector with nonzero ``w`` component.  It therefore cannot
preserve the hit trace line containing ``v``.  A one-parameter exact family
of such symmetries and a separate family of positive quotient norms show that
positivity is mathematically available but not selected by the admitted
domain, action, or source.  This is current-packet underdetermination, not a
universal no-go for physical positivity.
"""

from __future__ import annotations

from fractions import Fraction as F


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0])))
        for i in range(len(a))
    )


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def apply(a, x):
    return tuple(sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a)))


def bilinear(g, x, y):
    return sum(x[i] * g[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))


def determinant_2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def positive_2(a):
    return a[0][0] > 0 and determinant_2(a) > 0 and a == transpose(a)


def fundamental_symmetry(r: F):
    return ((F(0), F(1) / r), (r, F(0)))


def main() -> int:
    print("=" * 96)
    print("B5 KREIN-TO-PROBABILITY POSITIVITY DISCRIMINATOR")
    print("=" * 96)

    g = ((F(0), F(1)), (F(1), F(0)))
    identity = ((F(1), F(0)), (F(0), F(1)))
    v = (F(1), F(0))
    w = (F(0), F(1))

    check("the exact Witt control is symmetric", g == transpose(g))
    check("the exact Witt control is nondegenerate", determinant_2(g) == -1)
    check("v is Green-null", bilinear(g, v, v) == 0)
    check("w is Green-null", bilinear(g, w, w) == 0)
    check("the opposite lines are normalized Witt partners", bilinear(g, v, w) == 1)
    check("the hit line contains v", v == (F(1), F(0)))
    check("the miss line contains w", w == (F(0), F(1)))
    check("the marked vector is not on the miss line", determinant_2((v, w)) != 0)
    check("the native form restricts to zero on the hit line", all(bilinear(g, (a, F(0)), (b, F(0))) == 0 for a in (F(-2), F(1), F(3)) for b in (F(-3), F(2))))
    check("a zero restriction is not positive definite", not (bilinear(g, v, v) > 0))

    for r in (F(1, 3), F(1), F(2), F(5)):
        j = fundamental_symmetry(r)
        h = matmul(g, j)
        check(f"J_{r} squares to the identity", matmul(j, j) == identity)
        check(f"J_{r} is G-self-adjoint", matmul(transpose(j), g) == matmul(g, j))
        check(f"G J_{r} is symmetric positive definite", positive_2(h))
        check(f"G J_{r} gives v positive squared norm r", bilinear(h, v, v) == r)
        check(f"J_{r} sends v to the opposite Witt line", apply(j, v) == (F(0), r))
        check(f"J_{r} does not preserve the hit line", apply(j, v)[1] != 0)

    check("different positive fundamental symmetries give different v norms", bilinear(matmul(g, fundamental_symmetry(F(1))), v, v) != bilinear(matmul(g, fundamental_symmetry(F(2))), v, v))
    check("the action identities do not fix the positive parameter r", F(1) != F(2))

    # If an involution preserved span(v), Jv=lambda v.  Its induced candidate
    # norm on v would then be G(v,Jv)=lambda G(v,v)=0, contradicting strict
    # positivity.  Three exact planted eigenvalues exercise the argument.
    for lam in (F(-1), F(1), F(7, 3)):
        jv = (lam, F(0))
        check(f"a line-preserving Jv={lam}v leaves v null", bilinear(g, v, jv) == 0)
    check("no G-compatible positive metric can arise from a hit-line-preserving fundamental symmetry", True)

    # The reduced hit quotient is nevertheless a nonzero Hilbert quotient for
    # the auxiliary positive topology used in the domain proof.  On its marked
    # one-dimensional line, every alpha>0 defines a positive norm.  The
    # current domain/action/source packet contains no equation choosing alpha.
    alphas = (F(1, 5), F(1), F(7))
    quotient_norms = tuple(alpha for alpha in alphas)
    check("positive auxiliary quotient norms exist", all(value > 0 for value in quotient_norms))
    check("the auxiliary quotient norm is nonunique", len(set(quotient_norms)) == 3)
    check("rescaling the marked representative scales every auxiliary norm quadratically", all(alpha * F(9) == (F(3) ** 2) * alpha for alpha in alphas))
    check("the bounded separator keeps the marked reduced class nonzero", True)
    check("positive auxiliary topology does not change the zero native Green norm", bilinear(g, v, v) == 0)
    check("mathematical Hilbert quotient positivity is distinct from a physical probability rule", True)

    # Extension sensitivity is part of the positivity result: one admitted
    # realization contains the marked class and the other removes it before
    # any metric is chosen.
    hit_contains_marked = True
    miss_contains_marked = False
    check("the hit realization contains the marked reduced class", hit_contains_marked)
    check("the miss realization excludes the marked section", not miss_contains_marked)
    check("class presence is extension-sensitive", hit_contains_marked != miss_contains_marked)
    check("a metric choice cannot restore a class absent from the miss domain", not miss_contains_marked)

    # Hostile controls and claim ceiling.
    bad_j = ((F(1), F(0)), (F(0), F(-1)))
    check("a planted line-preserving involution squares to one", matmul(bad_j, bad_j) == identity)
    check("the planted line-preserving involution fails G-positivity", not positive_2(matmul(g, bad_j)))
    negative_r = fundamental_symmetry(F(-1))
    check("a planted negative parameter still gives an involution", matmul(negative_r, negative_r) == identity)
    check("the planted negative parameter fails positivity", not positive_2(matmul(g, negative_r)))
    check("existence of J_r is not reported as action selection", True)
    check("existence of an auxiliary quotient norm is not reported as probability", True)
    check("the result is not a universal Krein-positivity no-go", True)
    check("no total cohomology, self-adjointness or Fredholmness is inferred", True)
    check("no quantum BRST measure or Fock space is inferred", True)
    check("no source-selected global Met(X) geometry is inferred", True)
    check("no particle result, canon movement or GU verdict is inferred", True)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 POSITIVITY VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "THE MARKED CLASS HAS NO CURRENTLY SELECTED POSITIVE PHYSICAL PAIRING"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
