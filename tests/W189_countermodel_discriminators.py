#!/usr/bin/env python3
r"""
W189: exact countermodels and a target-free discriminator for the joint
law/shadow plus boundary-selection story.

This is deliberately a small structural test.  It does not fit any observed
number.  It asks whether an architecture has enough independently fixed
structure to predict anything before target data are supplied.

Countermodel A
    Same bulk law and same indefinite bulk metric, but two admissible shadow
    maps land in opposite Krein types.  Their pulled-back quadratic forms have
    opposite signs, so apparent stability is not a property of the bulk law
    alone.

Countermodel B
    Same bulk mode, shadow energy, reservoir energy, and coupling magnitude.
    A like-Krein-signed reservoir gives a real total spectrum, while an
    opposite-Krein-signed reservoir gives a complex pair.  Opening the system
    does not select the healthy total.

Countermodel C
    Three independent boundary parameters enter three observables through the
    identity map.  The boundary-to-observable map is surjective, so every
    target residual can be absorbed and no prediction remains.

The discriminator uses only:
    * the set of admissible shadow stability signatures;
    * the exact rank and dimension of the boundary response map;
    * whether a selector was specified before target data;
    * whether the selected TOTAL keep-and-grade dynamics is healthy;
    * whether shadow and boundary knobs are independent;
    * whether the construction forks were explicitly fixed.

No observed target values occur anywhere in this file.
"""

from dataclasses import dataclass
from fractions import Fraction


Q = Fraction
_checks = []


def check(name, condition, detail=""):
    passed = bool(condition)
    _checks.append(passed)
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}{suffix}")


def qmatrix(rows):
    return [[Q(value) for value in row] for row in rows]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    if not left or not right:
        return []
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matrices_equal(left, right):
    return left == right


def quadratic_form(vector, metric):
    column = [[Q(value)] for value in vector]
    return matmul(matmul(transpose(column), metric), column)[0][0]


def exact_rank(matrix):
    """Gaussian-elimination rank over Q."""
    work = [list(map(Q, row)) for row in matrix]
    if not work:
        return 0
    n_rows = len(work)
    n_cols = len(work[0])
    pivot_row = 0
    for col in range(n_cols):
        pivot = next((row for row in range(pivot_row, n_rows)
                      if work[row][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor != 0:
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j]
                    for j in range(n_cols)
                ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


def characteristic_discriminant_2x2(matrix):
    """Exact discriminant of lambda^2 - tr(H) lambda + det(H)."""
    a, b = matrix[0]
    c, d = matrix[1]
    trace = a + d
    determinant = a * d - b * c
    return trace * trace - 4 * determinant


def is_k_pseudo_hermitian(matrix, krein_metric):
    """For these real controls, test K H = H^T K exactly."""
    return matrices_equal(
        matmul(krein_metric, matrix),
        matmul(transpose(matrix), krein_metric),
    )


@dataclass(frozen=True)
class Architecture:
    shadow_signatures: tuple
    n_observables: int
    boundary_response: tuple
    n_boundary_parameters: int
    selector_predeclared: bool
    selected_total_c_positive: bool
    shadow_boundary_independent: bool
    construction_forks_named: bool


def as_matrix(rows):
    return [list(map(Q, row)) for row in rows]


def discriminator(architecture):
    """Return a score and Boolean without inspecting target values."""
    response = as_matrix(architecture.boundary_response)
    response_rank = exact_rank(response)
    gates = {
        # A theory may have many coordinate descriptions, but its allowed
        # shadow construction must give one qualitative stability signature.
        "shadow_stability_invariant": len(set(architecture.shadow_signatures)) == 1,
        # Selection must not be chosen after seeing the desired world.
        "selector_predeclared": architecture.selector_predeclared,
        # At least one target-independent relation must survive boundary choice.
        "predictive_surplus": response_rank < architecture.n_observables,
        # The declared boundary datum must compress rather than copy the target.
        "boundary_economical": architecture.n_boundary_parameters < architecture.n_observables,
        # KEEP-AND-GRADE is judged on the total system, not the reduced pole alone.
        "selected_total_c_positive": architecture.selected_total_c_positive,
        # A boundary knob may not silently choose or repair the shadow map.
        "level_independence": architecture.shadow_boundary_independent,
        # Fork declarations are part of the evidence, not editorial metadata.
        "construction_forks_named": architecture.construction_forks_named,
    }
    score = sum(gates.values())
    return {
        "gates": gates,
        "score": score,
        "maximum": len(gates),
        "explanatory": all(gates.values()),
        "boundary_rank": response_rank,
        "prediction_codimension": architecture.n_observables - response_rank,
    }


print("=" * 78)
print("PC -- exact algebra controls")
print("=" * 78)

identity2 = qmatrix([[1, 0], [0, 1]])
check("PC1 exact rank(I2)=2", exact_rank(identity2) == 2)
check("PC2 exact rank of a repeated column is 1",
      exact_rank(qmatrix([[1], [1], [1]])) == 1)

# A K-isometry that only changes the sign of the positive basis vector must not
# change its Krein type.  This separates a real construction change from a
# coordinate relabel.
eta = qmatrix([[1, 0], [0, -1]])
r_positive = [1, 0]
r_positive_relabelled = [-1, 0]
check("PC3 K-isometric relabel preserves shadow sign",
      quadratic_form(r_positive, eta) == quadratic_form(r_positive_relabelled, eta) == 1)

print()
print("=" * 78)
print("A -- same bulk law, different shadow map, opposite apparent stability")
print("=" * 78)

# GU construction represented: the actual law-level scalar coefficient is
# linear/shiab-Einstein, c_R=0.  eta represents the indefinite field-space
# metric; the two rows are two not-yet-identified reduction/shadow maps.
bulk_law_c_r = Q(0)
r_stable = [1, 0]
r_unstable = [0, 1]
stable_shadow_sign = quadratic_form(r_stable, eta)
unstable_shadow_sign = quadratic_form(r_unstable, eta)
check("A1 both reductions start from the same linear bulk law c_R=0",
      bulk_law_c_r == 0)
check("A2 first shadow map lands in a positive Krein type",
      stable_shadow_sign == 1, f"q={stable_shadow_sign}")
check("A3 second shadow map lands in a negative Krein type",
      unstable_shadow_sign == -1, f"q={unstable_shadow_sign}")
check("A4 apparent stability is not fixed by the bulk law alone",
      stable_shadow_sign * unstable_shadow_sign < 0)

print()
print("=" * 78)
print("B -- same bulk and shadow, boundary Krein type selects healthy/pathological total")
print("=" * 78)

# One ghost/shadow mode at energy 0, one reservoir mode at energy 1, coupling
# magnitude 1.  Only the reservoir's relative Krein type changes.
h_like = qmatrix([[0, 1], [1, 1]])
k_like = qmatrix([[-1, 0], [0, -1]])
h_opposite = qmatrix([[0, 1], [-1, 1]])
k_opposite = qmatrix([[-1, 0], [0, 1]])

check("B1 like-signed total is exactly K-pseudo-Hermitian",
      is_k_pseudo_hermitian(h_like, k_like))
check("B2 opposite-signed total is exactly K-pseudo-Hermitian",
      is_k_pseudo_hermitian(h_opposite, k_opposite))
disc_like = characteristic_discriminant_2x2(h_like)
disc_opposite = characteristic_discriminant_2x2(h_opposite)
check("B3 like-signed reservoir gives a real, distinct total spectrum",
      disc_like == 5 and disc_like > 0, f"discriminant={disc_like}")
check("B4 opposite-signed reservoir gives a complex-conjugate total pair",
      disc_opposite == -3 and disc_opposite < 0, f"discriminant={disc_opposite}")
check("B5 opening alone does not select health",
      disc_like > 0 > disc_opposite)

# With the coupling removed, both reservoirs have the same real diagonal
# spectrum.  The pathology is an interaction/type statement, not a label.
h_decoupled = qmatrix([[0, 0], [0, 1]])
check("B6 channel-removed control is real for either reservoir type",
      characteristic_discriminant_2x2(h_decoupled) == 1)

print()
print("=" * 78)
print("C -- full-rank boundary response absorbs every observable")
print("=" * 78)

boundary_epicycle = qmatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
boundary_compressed = qmatrix([[1], [1], [1]])
rank_epicycle = exact_rank(boundary_epicycle)
rank_compressed = exact_rank(boundary_compressed)
check("C1 identity boundary map is surjective onto all three observables",
      rank_epicycle == 3)
check("C2 surjectivity leaves zero target-independent predictions",
      3 - rank_epicycle == 0)
check("C3 one shared boundary datum leaves two invariant relations",
      rank_compressed == 1 and 3 - rank_compressed == 2)

# A target-independent absorption certificate: every basis residual has a
# boundary preimage.  By linearity, so does every residual vector.  No target
# values are used.
standard_basis = [
    [[Q(1)], [Q(0)], [Q(0)]],
    [[Q(0)], [Q(1)], [Q(0)]],
    [[Q(0)], [Q(0)], [Q(1)]],
]
check("C4 exact right-inverse certificate: every residual direction is absorbable",
      all(matmul(boundary_epicycle, basis) == basis for basis in standard_basis))

print()
print("=" * 78)
print("D -- target-free explanatory discriminator")
print("=" * 78)

positive_control = Architecture(
    shadow_signatures=(1,),
    n_observables=3,
    boundary_response=((1,), (1,), (1,)),
    n_boundary_parameters=1,
    selector_predeclared=True,
    selected_total_c_positive=True,
    shadow_boundary_independent=True,
    construction_forks_named=True,
)
countermodel_a = Architecture(
    shadow_signatures=(1, -1),
    n_observables=3,
    boundary_response=((1,), (1,), (1,)),
    n_boundary_parameters=1,
    selector_predeclared=True,
    selected_total_c_positive=True,
    shadow_boundary_independent=True,
    construction_forks_named=True,
)
countermodel_b = Architecture(
    shadow_signatures=(1,),
    n_observables=3,
    boundary_response=((1,), (1,), (1,)),
    n_boundary_parameters=1,
    selector_predeclared=False,
    selected_total_c_positive=True,
    shadow_boundary_independent=True,
    construction_forks_named=True,
)
countermodel_c = Architecture(
    shadow_signatures=(1,),
    n_observables=3,
    boundary_response=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    n_boundary_parameters=3,
    selector_predeclared=True,
    selected_total_c_positive=True,
    shadow_boundary_independent=True,
    construction_forks_named=True,
)

pc = discriminator(positive_control)
da = discriminator(countermodel_a)
db = discriminator(countermodel_b)
dc = discriminator(countermodel_c)

check("D1 constrained positive control passes all target-free gates",
      pc["explanatory"] and pc["score"] == pc["maximum"],
      f"score={pc['score']}/{pc['maximum']}")
check("D2 countermodel A fails exactly the shadow-invariance gate",
      (not da["explanatory"]
       and not da["gates"]["shadow_stability_invariant"]
       and da["score"] == da["maximum"] - 1),
      f"score={da['score']}/{da['maximum']}")
check("D3 countermodel B fails the predeclared-selection gate",
      (not db["explanatory"]
       and not db["gates"]["selector_predeclared"]),
      f"score={db['score']}/{db['maximum']}")
check("D4 countermodel C fails predictive-surplus and economy gates",
      (not dc["explanatory"]
       and not dc["gates"]["predictive_surplus"]
       and not dc["gates"]["boundary_economical"]
       and dc["prediction_codimension"] == 0),
      f"score={dc['score']}/{dc['maximum']}, codim={dc['prediction_codimension']}")

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print("  A: a simple bulk law does not explain a stable shadow until the shadow map is fixed.")
print("  B: an open boundary does not explain health until a prior selector fixes the reservoir type")
print("     and the selected TOTAL keep-and-grade dynamics has a positive C-metric.")
print("  C: boundary rank equal to observable dimension is an epicycle certificate, independent of fit.")
print("  D: law/shadow plus boundary selection is explanatory only when every structural gate passes.")

n_pass = sum(_checks)
n_total = len(_checks)
print()
print(f"{n_pass}/{n_total} checks passed.")
if n_pass != n_total:
    raise SystemExit(1)
print("exit 0")
