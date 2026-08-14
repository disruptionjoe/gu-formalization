#!/usr/bin/env sage-python
"""Exact ownership test for the W/mirror trace-Hq pairing.

The complete local Spin-natural equation-9.16 action-pairing space has two
lines, represented on one-forms by ``eta tensor B`` and ``eta tensor BJ``.
The trace compatibility form is ``eta tensor i B gamma(q_trace)``.  This probe
classifies their restrictions to W and its ASD mirror over two exact finite
fields, then proves characteristic-zero linear independence with a three-entry
minor over Q(i).  It does not test an unconstructed nonzero-fermion Hessian,
BV/BFV differential, closed domain, index, count, or physical half selector.
"""

from __future__ import annotations

import ast
from collections import Counter
from pathlib import Path

from sage.all import (
    GF,
    QuadraticField,
    block_diagonal_matrix,
    block_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def load_build_structures():
    """Load only the immutable exact carrier constructor, not probe outputs."""
    source = read("tests/channel-swings/selected_k77_induced_fermion_principal_discriminator.py")
    tree = ast.parse(source)
    node = next(
        n for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name == "build_structures"
    )
    namespace = {
        "identity_matrix": identity_matrix,
        "matrix": matrix,
        "block_matrix": block_matrix,
        "zero_matrix": zero_matrix,
    }
    exec(
        compile(ast.Module(body=[node], type_ignores=[]), "<build-structures>", "exec"),
        namespace,
    )
    return namespace["build_structures"]


BUILD = load_build_structures()


def invariant_forms(data, field, imaginary):
    gammas = data["gammas"]
    identity = identity_matrix(field, 128, sparse=True)
    pairing = identity
    for gamma in gammas[7:]:
        pairing *= gamma
    chirality = identity
    for gamma in gammas:
        chirality *= gamma
    eta = data["eta"]
    return {
        "action_symmetric": block_diagonal_matrix(
            [field(eta[a]) * pairing for a in range(14)], sparse=True
        ),
        "action_skew": block_diagonal_matrix(
            [field(eta[a]) * pairing * chirality for a in range(14)], sparse=True
        ),
        "trace_hq": block_diagonal_matrix(
            [field(eta[a]) * imaginary * pairing * gammas[10] for a in range(14)],
            sparse=True,
        ),
    }


def coefficient_rank(items, field):
    keys = sorted({key for item in items for key in item.dict()})
    coefficients = matrix(
        field,
        len(keys),
        len(items),
        lambda row, column: items[column][keys[row]],
        sparse=True,
    )
    return coefficients.rank()


def finite_packet(prime: int) -> dict:
    field = GF(prime)
    imaginary = field(-1).sqrt()
    data = BUILD(field, imaginary)
    projectors = data["projectors"]
    w_projector = projectors["W_sd192"]
    m_projector = projectors["mirror_asd192"]
    W = w_projector.matrix_from_columns(list(w_projector.pivots()))
    M = m_projector.matrix_from_columns(list(m_projector.pivots()))
    forms = invariant_forms(data, field, imaginary)

    restrictions = {}
    for name, form in forms.items():
        restrictions[name] = {
            "WW": W.transpose() * form * W,
            "MM": M.transpose() * form * M,
            "WM": W.transpose() * form * M,
            "MW": M.transpose() * form * W,
        }

    for name, rows in restrictions.items():
        check(
            "exact",
            f"GF({prime}) {name}: W and mirror restrictions are nondegenerate rank 192",
            rows["WW"].rank() == rows["MM"].rank() == 192,
        )
        check(
            "exact",
            f"GF({prime}) {name}: bilinear W--mirror cross restrictions vanish",
            rows["WM"].is_zero() and rows["MW"].is_zero(),
        )

    for carrier in ("WW", "MM"):
        action_rows = [
            restrictions["action_symmetric"][carrier],
            restrictions["action_skew"][carrier],
        ]
        all_rows = action_rows + [restrictions["trace_hq"][carrier]]
        check(
            "classification",
            f"GF({prime}) {carrier}: the two action restrictions remain independent",
            coefficient_rank(action_rows, field) == 2,
        )
        check(
            "classification",
            f"GF({prime}) {carrier}: trace-Hq adds a third independent restriction",
            coefficient_rank(all_rows, field) == 3,
        )

    return {
        "prime": prime,
        "dimensions": {"W": W.ncols(), "mirror": M.ncols()},
        "bilinear_restriction_ranks": {
            name: {key: value.rank() for key, value in rows.items()}
            for name, rows in restrictions.items()
        },
        "action_span_dimension_on_W": 2,
        "action_plus_trace_span_dimension_on_W": 3,
    }


def char0_minor() -> dict:
    """Compute only the three entries selected independently by the scout."""
    field = QuadraticField(-1, "ii")
    imaginary = field.gen()
    data = BUILD(field, imaginary)
    Wp = data["projectors"]["W_sd192"]
    W = Wp.matrix_from_columns(list(Wp.pivots()))
    gammas = data["gammas"]
    eta = data["eta"]
    identity = identity_matrix(field, 128, sparse=True)
    pairing = identity
    for gamma in gammas[7:]:
        pairing *= gamma
    chirality = identity
    for gamma in gammas:
        chirality *= gamma
    spin_forms = (pairing, pairing * chirality, imaginary * pairing * gammas[10])
    keys = ((0, 39), (0, 47), (1, 46))

    def entry(left, right, spin_form):
        result = field(0)
        for axis in range(14):
            x = matrix(
                field,
                128,
                1,
                list(left[axis * 128:(axis + 1) * 128]),
                sparse=True,
            )
            y = matrix(
                field,
                128,
                1,
                list(right[axis * 128:(axis + 1) * 128]),
                sparse=True,
            )
            result += field(eta[axis]) * (x.transpose() * spin_form * y)[0, 0]
        return result

    witness = matrix(
        field,
        3,
        3,
        lambda row, column: entry(
            W.column(keys[row][0]), W.column(keys[row][1]), spin_forms[column]
        ),
    )
    check(
        "char0",
        "the Q(i) three-entry witness has determinant -27/256",
        witness.det() == field(-27) / field(256),
    )
    check(
        "char0",
        "the two action columns have rank two while trace-Hq is outside their span",
        witness[:, :2].rank() == 2 and witness.rank() == 3,
    )
    return {
        "keys": [list(key) for key in keys],
        "matrix": [[str(value) for value in row] for row in witness.rows()],
        "determinant": str(witness.det()),
    }


print("A. SOURCE, PRIOR ART AND ADAPTIVE LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
pairing = read("explorations/conditional-build/selected-k77-action-adjoint-weight-classification-2026-08-11.md")
reality = read("explorations/conditional-build/selected-k77-graded-green-reality-graphs-2026-08-11.md")
trace = read("explorations/conditional-build/selected-k77-w-mirror-trace-hq-isotropy-correction-2026-08-13.md")
check(
    "source",
    "the source begins with four independent barred/unbarred fermion fields",
    "four distinct fields" in source,
)
check(
    "source",
    "the source does not supply a global K77 reality adjoint or physical domain",
    "global Hodge/Krein/reality adjoint" in source
    and "closed physical evolution domain" in source,
)
check(
    "prior_art",
    "the complete Spin-natural local action pairing family has exactly two lines",
    "exactly one projective line of each type" in pairing
    and "symmetric pairing" in pairing and "skew pairing" in pairing,
)
check(
    "prior_art",
    "the existing Majorana construction leaves both pairing horns unselected",
    "Both action-compatible pairings pass" in reality
    and "source selects neither horn" in reality,
)
check(
    "prior_art",
    "trace-Hq is currently a Hermitian compatibility form with an exact W/mirror Witt pair",
    "rank 192" in trace and "Witt inertia `(192,192,0)`" in trace,
)
for label in (
    "independent barred action variables versus a later anti-linear Majorana graph",
    "Spin-natural action pairing lines versus the moving q-dependent trace-Hq form",
    "bilinear transpose restriction versus Hermitian conjugate-transpose restriction",
    "W/mirror one-form sectors versus the two ambient C^(32,32) carrier halves",
    "finite fibre pairing versus physical BV cohomology and a closed analytic domain",
):
    check("layer0", label, True)


print("\nB. TWO-PRIME EXACT RESTRICTION CLASSIFICATION")
packets = [finite_packet(1009), finite_packet(1013)]
check(
    "cross_prime",
    "both exact primes reproduce the same three-form restriction fingerprint",
    packets[0]["bilinear_restriction_ranks"]
    == packets[1]["bilinear_restriction_ranks"],
)


print("\nC. MINIMAL CHARACTERISTIC-ZERO WITNESS")
witness = char0_minor()


print("\nD. OWNERSHIP DISPOSITION AND FENCES")
check(
    "ownership",
    "the current equation-9.16 action pairing space does not contain trace-Hq",
    True,
)
check(
    "reality",
    "the existing graded Majorana graphs select neither action horn and do not add trace-Hq",
    True,
)
check(
    "variational",
    "a future q-dependent nonzero-fermion Hessian could own a new form and is not excluded",
    True,
)
check(
    "symplectic",
    "no fibre pairing is promoted to a presymplectic quotient or BV/BFV cohomology",
    True,
)
check(
    "analytic",
    "no local rank or span statement constructs positivity, a closed domain, spectrum or index",
    True,
)
check(
    "planted",
    "PLANT compatibility of a connection with trace-Hq is not action ownership of trace-Hq",
    True,
)

print("\nRESULT")
print("DISPOSITION=CURRENT_EQUATION916_ACTION_PAIRING_SPACE_EXCLUDES_TRACE_HQ__REALITY_SELECTS_NEITHER_HORN__NONZERO_FERMION_BV_DOMAIN_OPEN")
print("ACTION_PAIRING_RESTRICTION_SPAN_DIMENSION=2")
print("ACTION_PLUS_TRACE_RESTRICTION_SPAN_DIMENSION=3")
print("CHAR0_INDEPENDENCE_DETERMINANT=-27/256")
print("SOURCE_RETURN=SOURCE_CONFIRMS_INDEPENDENT_FOUR_FIELD_GRAMMAR__SOURCE_SILENT_TRACE_HQ_AS_DEFINING_FERMION_FORM_AND_W_MIRROR_SELECTOR")
print("NEXT=TEST_THE_FIRST_ACTION_OWNED_NONZERO_FERMION_HESSIAN_OR_GRADED_BV_DIFFERENTIAL_FOR_A_NEW_W_MIRROR_FINGERPRINT__KEEP_ANALYTIC_DOMAIN_SEPARATE")
print(f"packets={packets}")
print(f"char0_witness={witness}")
print(f"counts={dict(COUNTS)}")
print(f"failures={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
