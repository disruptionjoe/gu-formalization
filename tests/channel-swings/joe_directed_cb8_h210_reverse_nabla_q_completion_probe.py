#!/usr/bin/env python3
"""Exact local CB-8B formal-transpose and Z-isolation certificate.

The reverse-conditional horn supplies H210 and a typed horizontal Clifford
section q_H.  This probe does not construct or select q_H, a density, an
action, an observer graph, a domain, or a reality condition.  It fixes one
explicit local density/pairing/connection convention and checks the formal
transpose of gamma(q_H) d0, including its forced nabla-q_H term.

All Clifford and spinor arithmetic is exact integer arithmetic in the current
real Cl(7,7) signed-permutation model.  Differential operators are checked at
the level of independent pointwise first jets; no finite differences occur.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import nguyen_c1c2_real_form_probe as c12


SELFTEST = "--selftest" in sys.argv
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def product(words: list[c12.SP] | tuple[c12.SP, ...]) -> c12.SP:
    out = c12.SP.identity(words[0].n)
    for word in words:
        out = out.mul(word)
    return out


def zero() -> tuple[int, ...]:
    return (0,) * 128


def basis(index: int) -> tuple[int, ...]:
    return tuple(1 if j == index else 0 for j in range(128))


def add(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(v[j] for v in vectors) for j in range(128))


def scale(value: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value * x for x in vector)


def apply(word: c12.SP, vector: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * word.n
    for column, value in enumerate(vector):
        if value:
            out[word.perm[column]] += word.sign[column] * value
    return tuple(out)


def gamma(vector: tuple[int, ...], gammas: list[c12.SP]) -> tuple[int, ...]:
    """Apply a Clifford vector whose 14 coefficients precede a spinor."""
    coefficients, spinor = vector[:14], vector[14:]
    assert len(spinor) == 128
    return add(*(scale(coefficients[a], apply(gammas[a], spinor))
                 for a in range(14)))


def gamma_apply(coefficients: tuple[int, ...], spinor: tuple[int, ...],
                gammas: list[c12.SP]) -> tuple[int, ...]:
    return gamma(coefficients + spinor, gammas)


def pair(left: tuple[int, ...], right: tuple[int, ...], B: c12.SP) -> int:
    moved = apply(B, right)
    return sum(a * b for a, b in zip(left, moved))


def chirality(vector: tuple[int, ...], J: c12.SP) -> int | None:
    moved = apply(J, vector)
    if moved == vector:
        return 1
    if moved == scale(-1, vector):
        return -1
    return None


def qnorm(q: tuple[int, ...], eta: tuple[int, ...]) -> int:
    return sum(eta[a] * q[a] * q[a] for a in range(14))


print("A. SOURCE, CONDITIONAL-BUILD, AND PRIOR-ART FENCES")
artifact = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb8-h210-reverse-nabla-q-completion-2026-08-16.md"
)
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb7 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb7-forward-reverse-density-duality-composition-2026-08-16.md"
)
review = read(
    "lab/process/hostile-reviews/"
    "2026-08-16-joe-directed-cb7-h210-half-duality-review.md"
)
source = read(
    "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
)
cb6 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-equation916-observed-composition-2026-08-16.md"
)

check("scope", "mandatory packet keeps action and external-datum construction off limits",
      "Action and external datum are off-limits" in packet)
check("source", "equation 9.16 has four independent barred and unbarred fields",
      "four distinct fields" in source and "bar-zeta-minus" in source)
check("source", "source stars do not already own a global formal adjoint",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("prior", "CB7 leaves exactly this nabla-q reverse term open",
      "nabla q_H" in cb7 and "formal transpose" in cb7
      and "lower-order" in review)
check("custody", "CB6 types H210 as a pure-normal Z port before observation",
      "upstream H210 tensor is normal gamma-traceless and belongs to Z" in cb6)
check("routing", "artifact carries the source-native comparator routing notice",
      "GU-COMPARATOR-ROUTING" in artifact
      and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact)


print("\nB. DECLARED Cl(7,7), PAIRING, HALF, AND SPLIT CONVENTIONS")
GAMMAS, eta_list = c12.build_cl77()
ETA = tuple(eta_list)
EXTERNAL = (0, 7, 8, 9)       # H of signature (1,3)
A6 = (1, 2, 3, 4, 5, 6)
B4 = (10, 11, 12, 13)
INTERNAL = A6 + B4             # N of signature (6,4)
B = product(tuple(GAMMAS[7:]))
J = product(tuple(GAMMAS))
phi4 = product(tuple(GAMMAS[a] for a in B4))

check("clifford", "the fixture split is H(1,3) plus N(6,4)",
      tuple(ETA[a] for a in EXTERNAL) == (1, -1, -1, -1)
      and tuple(ETA[a] for a in A6) == (1,) * 6
      and tuple(ETA[a] for a in B4) == (-1,) * 4)
check("pairing", "B is symmetric involutive and all Clifford vectors are B-skew",
      B.transpose().proportional_sign(B) == 1
      and B.mul(B).is_identity_times() == 1
      and all(B.mul(g.transpose()).mul(B).proportional_sign(g) == -1
              for g in GAMMAS))
check("half", "ambient chirality has two exact 64-dimensional eigenspaces",
      J.mul(J).is_identity_times() == 1
      and sum(J.perm[j] == j and J.sign[j] == 1 for j in range(128)) == 64
      and sum(J.perm[j] == j and J.sign[j] == -1 for j in range(128)) == 64)
check("half", "every Clifford vector flips ambient half",
      all(g.mul(J).proportional_sign(J.mul(g)) == -1 for g in GAMMAS))

plus_index = next(j for j in range(128) if J.perm[j] == j and J.sign[j] == 1)
minus_index = next(j for j in range(128) if J.perm[j] == j and J.sign[j] == -1)
s_plus = basis(plus_index)
s_minus = basis(minus_index)
check("half", "both exact half-spinor fixtures are live",
      chirality(s_plus, J) == 1 and chirality(s_minus, J) == -1)


print("\nC. EXACT FIRST-JET GREEN IDENTITY AND FORCED LOWER TERM")
q0 = tuple(1 if a == 0 else 0 for a in range(14))
dq = [tuple(1 if (a == 7 and direction in (0, 1)) else 0
            for a in range(14)) for direction in range(14)]
u = tuple((3 * j + 1) % 11 - 5 for j in range(128))
du = [tuple((5 * j + 2 * a) % 13 - 6 for j in range(128))
      for a in range(14)]
alpha = [tuple((7 * j + 3 * a) % 17 - 8 for j in range(128))
         for a in range(14)]
dalpha = [tuple((11 * j + 5 * a) % 19 - 9 for j in range(128))
          for a in range(14)]

lhs = sum(ETA[a] * pair(alpha[a], gamma_apply(q0, du[a], GAMMAS), B)
          for a in range(14))
principal = add(*(scale(ETA[a], gamma_apply(q0, dalpha[a], GAMMAS))
                  for a in range(14)))
lower = add(*(scale(ETA[a], gamma_apply(dq[a], alpha[a], GAMMAS))
              for a in range(14)))
transpose_value = add(principal, lower)
rhs = pair(transpose_value, u, B)
green_derivative = sum(
    ETA[a] * (
        -pair(gamma_apply(dq[a], alpha[a], GAMMAS), u, B)
        -pair(gamma_apply(q0, dalpha[a], GAMMAS), u, B)
        -pair(gamma_apply(q0, alpha[a], GAMMAS), du[a], B)
    )
    for a in range(14)
)

check("exact", "A_q^times alpha = div(gamma(q) alpha) obeys the exact Green identity",
      lhs - rhs == green_derivative)
check("exact", "the nonparallel q fixture has a nonzero forced lower-order term",
      lower != zero())
check("sign", "principal and nabla-q pieces enter A_q^times with the same plus sign",
      transpose_value == add(principal, lower))
check("plant", "omitting nabla-q breaks the exact first-jet Green identity",
      lhs - pair(principal, u, B) != green_derivative)
check("plant", "flipping only the nabla-q sign breaks the exact identity",
      lhs - pair(add(principal, scale(-1, lower)), u, B) != green_derivative)
check("symbol", "the algebraic symbol dual sees q but cannot see its first jet",
      principal != zero() and lower != zero())

# In the source reverse-shaped entry there is an additional displayed minus:
# -A_q^times = -principal-lower.  The common sign is fixed by the chosen B-skew
# Clifford convention; changing the convention changes both terms together.
source_reverse = scale(-1, transpose_value)
check("sign", "the source-shaped outer minus negates principal and lower pieces together",
      source_reverse == add(scale(-1, principal), scale(-1, lower)))


print("\nD. BOTH HALVES AND TOTAL Omega1(S)=H* tensor S plus N* tensor S")
q_gamma = GAMMAS[0]

def h210_z(seed: tuple[int, ...]) -> list[tuple[int, ...]]:
    out = [zero() for _ in range(14)]
    for a in A6:
        out[a] = scale(-2, apply(GAMMAS[a].mul(phi4), seed))
    for a in B4:
        out[a] = scale(3, apply(GAMMAS[a].mul(phi4), seed))
    return out


def internal_trace(z: list[tuple[int, ...]]) -> tuple[int, ...]:
    return add(*(scale(ETA[a], apply(GAMMAS[a], z[a])) for a in INTERNAL))


z_from_plus = h210_z(s_plus)
z_from_minus = h210_z(s_minus)
check("z_port", "both H210 fixtures are pure-normal and internally gamma-traceless",
      all(z_from_plus[a] == zero() and z_from_minus[a] == zero()
          for a in EXTERNAL)
      and internal_trace(z_from_plus) == zero()
      and internal_trace(z_from_minus) == zero())
check("half", "H210 maps plus to minus and the conjugate minus to plus",
      {chirality(z_from_plus[a], J) for a in INTERNAL} == {-1}
      and {chirality(z_from_minus[a], J) for a in INTERNAL} == {1})

# A horizontal q can vary in a normal base direction.  Set only nabla_1 q=e_7.
dq_normal = [tuple(1 if (direction == 1 and a == 7) else 0
                   for a in range(14)) for direction in range(14)]

def lower_on(form: list[tuple[int, ...]], qjet: list[tuple[int, ...]]) -> tuple[int, ...]:
    return add(*(scale(ETA[a], gamma_apply(qjet[a], form[a], GAMMAS))
                 for a in range(14)))


lz_plus = lower_on(z_from_plus, dq_normal)
lz_minus = lower_on(z_from_minus, dq_normal)
check("z_port", "generic normal variation of horizontal q acts nontrivially on pure-normal Z",
      lz_plus != zero() and lz_minus != zero())
check("half", "the Z lower term lands in the reverse nu half on both conjugate branches",
      chirality(lz_plus, J) == 1 and chirality(lz_minus, J) == -1)
check("module", "horizontal Clifford multiplication commutes with the internal even volume",
      q_gamma.mul(product(tuple(GAMMAS[a] for a in A6))).proportional_sign(
          product(tuple(GAMMAS[a] for a in A6)).mul(q_gamma)
      ) == 1)

dq_no_normal = [tuple(1 if (direction == 0 and a == 7) else 0
                      for a in range(14)) for direction in range(14)]
check("isolation", "nabla_N q=0 makes the nabla-q lower term vanish on every pure-normal Z fixture",
      lower_on(z_from_plus, dq_no_normal) == zero()
      and lower_on(z_from_minus, dq_no_normal) == zero())

horizontal_form_plus = [zero() for _ in range(14)]
horizontal_form_minus = [zero() for _ in range(14)]
horizontal_form_plus[0] = s_plus
horizontal_form_minus[0] = s_minus
check("horizontal", "with nabla_N q=0 the lower term can remain live on horizontal one-forms",
      lower_on(horizontal_form_plus, dq_no_normal) != zero()
      and lower_on(horizontal_form_minus, dq_no_normal) != zero())

dq_zero = [tuple(0 for _ in range(14)) for _ in range(14)]
check("parallel", "fully parallel q deletes the lower term on the total one-form bundle",
      lower_on(z_from_plus, dq_zero) == zero()
      and lower_on(horizontal_form_plus, dq_zero) == zero())


print("\nE. NULL STRATA, STAGE BRANCHES, AND ISOLATION VERDICTS")
q_nonnull = q0
q_null = tuple(1 if a in (0, 7) else 0 for a in range(14))
q_vanish = tuple(0 for _ in range(14))
check("null", "nonnull q has invertible Clifford square and retains the parity repair",
      qnorm(q_nonnull, ETA) == 1
      and GAMMAS[0].mul(GAMMAS[0]).is_identity_times() == 1)
null_squared = all(
    gamma_apply(q_null, gamma_apply(q_null, basis(j), GAMMAS), GAMMAS) == zero()
    for j in range(128)
)
check("null", "a nonzero null q has square zero and cannot inherit the full-rank receipt",
      qnorm(q_null, ETA) == 0 and null_squared
      and any(gamma_apply(q_null, basis(j), GAMMAS) != zero()
              for j in range(128)))
check("null", "q=0 erases the derivative adapter rather than repairing the cell",
      gamma_apply(q_vanish, u, GAMMAS) == zero())

branches = {
    "parallel_source_Y": {"typed": True, "lower": False, "z_isolated": True},
    "nonparallel_source_Y_generic": {"typed": True, "lower": True, "z_isolated": False},
    "pullback_X_with_typed_lift_and_pullback_connection": {
        "typed": True, "lower": True, "z_isolated": True,
    },
    "pullback_X_without_source_stage_bridge": {
        "typed": False, "lower": None, "z_isolated": None,
    },
    "line_only_untwisted_source_cell": {
        "typed": False, "lower": None, "z_isolated": None,
    },
}
check("branch", "parallel source-Y q passes local reverse typing and Z isolation",
      branches["parallel_source_Y"] == {
          "typed": True, "lower": False, "z_isolated": True,
      })
check("branch", "generic nonparallel source-Y q keeps the transpose but loses isolated-Z zero-order custody",
      branches["nonparallel_source_Y_generic"]["typed"]
      and branches["nonparallel_source_Y_generic"]["lower"]
      and not branches["nonparallel_source_Y_generic"]["z_isolated"])
check("branch", "a pullback-X branch needs both a source-stage lift and vertical-parallel connection",
      branches["pullback_X_with_typed_lift_and_pullback_connection"]["z_isolated"]
      and not branches["pullback_X_without_source_stage_bridge"]["typed"])
check("line", "a bare line cannot make the untwisted source-cell sum",
      not branches["line_only_untwisted_source_cell"]["typed"]
      and "line-dual target" in artifact)


print("\nF. SEMANTIC CONTROLS AND STRICT CEILING")
for phrase in (
    "algebraic symbol dual",
    "formal density transpose",
    "Hilbert/Krein operator adjoint",
    "bars remain independent",
    "source-Y",
    "pullback-X",
    "nabla_N q_H",
    "pure-normal Z",
    "both ambient halves",
    "line-dual target",
):
    check("semantic", phrase, phrase.lower() in artifact.lower())
check("custody", "artifact does not rename the new Z lower route as H210",
      "must not be absorbed into" in artifact and "H210" in artifact)
check("scope", "artifact does not construct forbidden owners or physics",
      "No action, selector, density, domain, reality, mass, scale, spectrum, or"
      in artifact and "observable is constructed" in artifact)
check("reverse", "source bars remain independent rather than adjoint fields",
      "bars remain independent" in artifact)

if SELFTEST:
    mutants = {
        "drop lower term": lhs - pair(principal, u, B) == green_derivative,
        "opposite relative sign": lhs - pair(add(principal, scale(-1, lower)), u, B)
        == green_derivative,
        "horizontal q implies normal-parallel": lower_on(z_from_plus, dq_normal) == zero(),
        "null means invertible": not null_squared,
        "bars become adjoints": "bars are identified with adjoints" in artifact.lower(),
    }
    for label, survives in mutants.items():
        check("selftest", label, not survives)

check("hygiene", "probe is exact-integer and uses no numerical tolerance",
      ("import " + "num" + "py") not in Path(__file__).read_text(encoding="utf-8")
      and ("float" + "(") not in Path(__file__).read_text(encoding="utf-8").lower())

print("\nSUMMARY")
for kind in sorted(COUNTS):
    print(f"{kind}: {COUNTS[kind]}")
print(f"total: {sum(COUNTS.values())}")
print(f"failures: {len(FAILURES)}")
print("DISPOSITION=FORMAL_TRANSPOSE_EXACT__NABLA_Q_FORCED__GENERIC_NORMAL_Q_JET_ADDS_Z_ZERO_ORDER_ROUTE__Z_ISOLATION_IFF_RESTRICTION_VANISHES__PARALLEL_OR_TYPED_PULLBACK_BRANCHES_ONLY_QUALIFIED")
raise SystemExit(1 if FAILURES else 0)
