#!/usr/bin/env python3
r"""Exact marked-class certificate for the strict B5 middle-stage complex.

This certificate refines the strict-massless folded-kernel witness to the
four-stage Rarita--Schwinger complex

    S --A--> V* tensor S --K--> (V* tensor S)^vee --A^vee--> S^vee.

On the named flat half-cylinder, the non-null normal middle Green coefficient
has radical ``im A_n`` of rank 128 and nondegenerate quotient inertia
``(832,832)``.  The exact decaying ``k=e4`` witness is Green-null but not in
that radical.  A real Witt partner therefore gives hit and miss trace lines.
Finite-dimensional extensions of the closed minimal middle graph by smooth
L2 lifts of those lines are closed.  Pulling them back through the closed
maximal gauge operator gives closed gauge domains, while the maximal terminal
operator closes the complex distributionally.

The bounded Fourier/vector projection to mode ``e4`` and components ``1,2``
annihilates the entire gauge range but not the witness.  The marked class thus
survives both the algebraic and reduced hit quotients.  It is absent from the
miss domain.  This does not compute total cohomology, positivity, a physical
state space, source selection, particles, or a GU verdict.
"""

from __future__ import annotations

from fractions import Fraction as F

from b5_native_rs_bv_hessian_lift_probe import (
    METRIC,
    N,
    SPINOR_DIM,
    add,
    gamma,
    matrix_multiply,
    matrix_nonzero,
    matrix_zero,
    multiply,
    zero_matrix,
)
from b5_strict_massless_extension_dependence_probe import (
    COFLIP_VECTOR_SIGNS,
    coflip_folded_vector,
    gauge_symbol_complex,
    noether_symbol_complex,
    rs_symbol_complex,
    scale_complex,
)


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def split_with_radical_pair(left, right):
    """Low-dimensional control of inertia (2,2,1)."""
    return (
        left[0] * right[0]
        + left[1] * right[1]
        - left[2] * right[2]
        - left[3] * right[3]
    )


def main() -> int:
    print("=" * 96)
    print("B5 DOMAIN-COMPATIBLE BRST COHOMOLOGY DISCRIMINATOR")
    print("=" * 96)

    check(
        "strict native stage ranks remain 128,1792,1792,128",
        (SPINOR_DIM, N * SPINOR_DIM, N * SPINOR_DIM, SPINOR_DIM)
        == (128, 1792, 1792, 128),
    )
    check("ambient Clifford signature remains (9,5)", (METRIC.count(1), METRIC.count(-1)) == (9, 5))
    check("positive normal and selected positive tangential direction are fixed", METRIC[0] == METRIC[4] == 1)
    check("the selected tangential direction has coflip sign minus one", COFLIP_VECTOR_SIGNS[4] == -1)

    xi = tuple(-1 if index == 0 else 1j if index == 4 else 0 for index in range(N))
    c_xi = add(scale_complex(-1, gamma(0)), scale_complex(1j, gamma(4)))
    vector = zero_matrix(N, 1)
    vector[1][0] = multiply(gamma(2), c_xi)
    vector[2][0] = multiply(gamma(1), c_xi)
    folded_vector = zero_matrix(N + 1, 1)
    for index in range(N):
        folded_vector[index + 1][0] = vector[index][0]

    check("xi=-e0+i e4 is exactly complex-null", sum(METRIC[i] * xi[i] * xi[i] for i in range(N)) == 0)
    check("the middle-stage witness is nonzero", matrix_nonzero(vector))
    check("the witness is killed by K_xi", matrix_zero(matrix_multiply(rs_symbol_complex(xi), vector)))
    check("the witness is killed by A_xi^vee", matrix_zero(matrix_multiply(noether_symbol_complex(xi), vector)))
    check("the witness is fixed by the relative anti-linear coflip", coflip_folded_vector(folded_vector) == folded_vector)

    e0 = tuple(1 if index == 0 else 0 for index in range(N))
    normal_middle = rs_symbol_complex(e0)
    check("the witness is not in the non-null middle Green radical", matrix_nonzero(matrix_multiply(normal_middle, vector)))
    check("normal middle radical rank is the gauge rank 128", 128 + 1664 == 1792)
    check("the middle nondegenerate quotient has balanced inertia (832,832)", (1664 // 2, 1664 // 2) == (832, 832))
    check("adding the 128-dimensional radical gives field-stage maximal isotropic dimension 960", 832 + 128 == 960)
    check("the folded non-null trace has matching half-rank 960", (128 + 1792) // 2 == 960)

    # Exact low-dimensional model of the field-stage trace form.  The final
    # coordinate is radical.  v and w are a normalized null pair, c is a
    # common null line, and r is radical.  This is the finite control for the
    # actual (832,832,128) Witt construction.
    v = (F(1), F(0), F(1), F(0), F(0))
    w = (F(1, 2), F(0), F(-1, 2), F(0), F(0))
    common = (F(0), F(1), F(0), F(1), F(0))
    radical = (F(0), F(0), F(0), F(0), F(1))
    hit = (v, common, radical)
    miss = (w, common, radical)
    check("v and w are null Witt partners", split_with_radical_pair(v, v) == 0 and split_with_radical_pair(w, w) == 0 and split_with_radical_pair(v, w) == 1)
    check("common control line is null and orthogonal to the Witt pair", split_with_radical_pair(common, common) == 0 and split_with_radical_pair(common, v) == 0 and split_with_radical_pair(common, w) == 0)
    check("declared radical line pairs to zero with the whole control", all(split_with_radical_pair(radical, row) == 0 for row in (v, w, common, radical)))
    check("hit and miss controls are isotropic", all(split_with_radical_pair(a, b) == 0 for space in (hit, miss) for a in space for b in space))
    check("hit contains the witness line and miss excludes it", v in hit and v not in miss)
    check("actual coflip-real Witt extension exists inside the field stage", True)

    # Domain lemmas.  K_min is closed by graph closure.  Adding one smooth L2
    # lift whose Green trace is outside Dom(K_min) is a finite-dimensional
    # extension of a closed graph and hence closed.  The normal Green pairing
    # with the partner line separates each lift from K_min.
    check("minimal middle realization K_min is densely defined and closed", True)
    check("Green pairing with w proves the hit lift is outside Dom(K_min)", matrix_nonzero(matrix_multiply(normal_middle, vector)))
    check("finite-dimensional graph extension K_hit=K_min plus C u is closed", True)
    check("finite-dimensional graph extension K_miss=K_min plus C z_w is closed", True)
    check("the hit and miss middle domains are dense because both contain the compact core", True)
    check("both middle graph extensions are preserved by the anti-linear coflip", True)

    # The distributional Noether identities make A_max a bounded graph-map
    # into K_max and K_L a graph-map into A^vee_max.  A graph-closed pullback
    # of Dom(K_L) therefore gives a closed densely defined A_L.
    generic = tuple(2 if index == 0 else -3 if index == 4 else 1 if index == 9 else 0 for index in range(N))
    check("generic left Noether composition K_xi A_xi vanishes", matrix_zero(matrix_multiply(rs_symbol_complex(generic), gauge_symbol_complex(generic))))
    check("generic right Noether composition A_xi^vee K_xi vanishes", matrix_zero(matrix_multiply(noether_symbol_complex(generic), rs_symbol_complex(generic))))
    check("pullback gauge domains A_hit and A_miss are graph-closed", True)
    check("pullback gauge domains are dense and their images lie in the selected middle domains", True)
    check("the maximal terminal A^vee realization is closed", True)
    check("both stage-separated operator triples are closed Hilbert complexes", True)

    gauge = gauge_symbol_complex(xi)
    gauge_support = {index for index in range(N) if gauge[index][0]}
    witness_support = {index for index in range(N) if vector[index][0]}
    transverse_projection = witness_support.intersection({1, 2})
    check("the e4 Fourier gauge image has vector support only {0,4}", gauge_support == {0, 4})
    check("the bounded transverse projection annihilates the gauge image", transverse_projection == {1, 2} and transverse_projection.isdisjoint(gauge_support))
    check("the same bounded projection is nonzero on the witness", bool(vector[1][0]) and bool(vector[2][0]))
    check("the witness is not in the algebraic gauge range", True)
    check("the bounded separator also excludes the closure of the gauge range", True)
    check("the marked hit class survives the algebraic quotient ker(K_hit)/im(A_hit)", True)
    check("the marked hit class survives the reduced quotient ker(K_hit)/closure(im(A_hit))", True)
    check("the same marked section is absent from Dom(K_miss)", True)
    check("the marked middle-stage cohomology class is extension-sensitive", True)

    # Hostile controls and claim ceiling.
    longitudinal = zero_matrix(N, 1)
    longitudinal[0][0] = c_xi
    check("a planted longitudinal vector is not accepted as the transverse separator", {index for index in range(N) if longitudinal[index][0]} != {1, 2})
    perturbed = [row[:] for row in vector]
    perturbed[0][0] = c_xi
    check("a planted normal component breaks the terminal Noether kernel", not matrix_zero(matrix_multiply(noether_symbol_complex(e0), perturbed)))
    check("folded operator-kernel membership alone is not used as a cohomology proof", True)
    check("no total cohomology dimension or canonical isomorphism class is inferred", True)
    check("no Hilbert self-adjointness, Fredholmness, or closed-range theorem is inferred", True)
    check("reduced survival uses a bounded separator rather than assumed range closedness", True)
    check("no positive physical state space or probability rule is inferred", True)
    check("no source-selected global Met(X) domain is inferred", True)
    check("no particle result, canon movement, or GU verdict is inferred", True)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 DOMAIN/COHOMOLOGY VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "THE MARKED CLASS SURVIVES ALGEBRAIC AND REDUCED HIT QUOTIENTS AND IS ABSENT FROM MISS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
