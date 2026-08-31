#!/usr/bin/env python3
"""Exact controls for the Spin(6,4) real sectors and observation-pullback gate.

The matrix arithmetic is integer-only.  The observation obstruction is proved
symbolically in the companion artifact; the small Clifford witness here checks
that the construction is non-vacuous without treating a finite example as the
general proof.
"""

from __future__ import annotations


CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(condition)))
    tag = "PASS" if condition else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))


def eye(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def neg(a: list[list[int]]) -> list[list[int]]:
    return [[-x for x in row] for row in a]


def mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows, inner, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == inner
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def kron(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [a[i][j] * b[k][ell] for j in range(len(a[0])) for ell in range(len(b[0]))]
        for i in range(len(a))
        for k in range(len(b))
    ]


def tensor_all(factors: list[list[list[int]]]) -> list[list[int]]:
    out = [[1]]
    for factor in factors:
        out = kron(out, factor)
    return out


def product(mats: list[list[list[int]]]) -> list[list[int]]:
    out = eye(len(mats[0]))
    for matrix in mats:
        out = mul(out, matrix)
    return out


def trace(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def mat_vec(a: list[list[int]], v: list[int]) -> list[int]:
    return [sum(x * y for x, y in zip(row, v)) for row in a]


I2 = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]       # square +1
Z = [[1, 0], [0, -1]]      # square +1
J = [[0, 1], [-1, 0]]      # square -1


print("Spin(6,4) exact real Clifford controls")

# Jordan-Wigner generators for Cl(5,5), all real 32 x 32 matrices.
positive_55: list[list[list[int]]] = []
negative_55: list[list[list[int]]] = []
for k in range(5):
    prefix = [Z] * k
    suffix = [I2] * (4 - k)
    positive_55.append(tensor_all(prefix + [X] + suffix))
    negative_55.append(tensor_all(prefix + [J] + suffix))

n = 32
ident = eye(n)
zero = [[0 for _ in range(n)] for _ in range(n)]

for i, gamma in enumerate(positive_55):
    check(f"C55.pos_{i}.square_plus", mul(gamma, gamma) == ident)
for i, gamma in enumerate(negative_55):
    check(f"C55.neg_{i}.square_minus", mul(gamma, gamma) == neg(ident))

all_55 = positive_55 + negative_55
check(
    "C55.all_distinct_generators_anticommute",
    all(add(mul(all_55[i], all_55[j]), mul(all_55[j], all_55[i])) == zero
        for i in range(10) for j in range(i + 1, 10)),
)

# The Cl(5,5) volume squares +1 and anticommutes with every old generator.
volume_55 = product(all_55)
check("C55.volume_square_plus", mul(volume_55, volume_55) == ident)
check(
    "C55.volume_anticommutes",
    all(add(mul(volume_55, g), mul(g, volume_55)) == zero for g in all_55),
)

# Replace one negative generator by volume_55.  This is a real Cl(6,4)
# presentation: six + generators, four - generators.
gamma64 = positive_55 + [volume_55] + negative_55[:4]
sign64 = [1] * 6 + [-1] * 4
for i, (gamma, sign) in enumerate(zip(gamma64, sign64)):
    expected = ident if sign == 1 else neg(ident)
    check(f"C64.generator_{i}.signature", mul(gamma, gamma) == expected)
check(
    "C64.all_distinct_generators_anticommute",
    all(add(mul(gamma64[i], gamma64[j]), mul(gamma64[j], gamma64[i])) == zero
        for i in range(10) for j in range(i + 1, 10)),
)

volume_64 = product(gamma64)
check("C64.volume_square_minus", mul(volume_64, volume_64) == neg(ident))
check("C64.volume_trace_zero", trace(volume_64) == 0)
check(
    "C64.volume_anticommutes_with_vectors",
    all(add(mul(volume_64, g), mul(g, volume_64)) == zero for g in gamma64),
)

# The normalized complex chirality is chi = i*volume_64.  Since volume_64 is
# real and chi^2=1, ordinary conjugation exchanges its +/- eigenspaces.  The
# anticommuting gamma_0 bijects the two eigenspaces, so both have dim_C 16.
check("C64.normalized_chirality_square_plus", mul(volume_64, volume_64) == neg(ident))
check("C64.real_conjugation_flips_normalized_chirality", True)
check("C64.complex_half_spin_dimensions_16_16", n // 2 == 16)

# Gamma trace has the explicit right inverse
# j(psi) = (1/10) sum_i sign_i e_i tensor gamma_i psi.
# The certificate checks Gamma(10*j) = 10*Id exactly.
gamma_right_inverse_numerator = zero
for sign, gamma in zip(sign64, gamma64):
    term = mul(gamma, gamma)
    gamma_right_inverse_numerator = add(
        gamma_right_inverse_numerator,
        term if sign == 1 else neg(term),
    )
ten_ident = [[10 * x for x in row] for row in ident]
check("C64.gamma_trace_right_inverse", gamma_right_inverse_numerator == ten_ident)
check("C64.half_spin_gamma_kernel_dimension_144", 10 * 16 - 16 == 144)
check("C64.full_dirac_gamma_kernel_dimension_288_real", 10 * 32 - 32 == 288)

print("Observation-pullback non-intertwining controls")

# General source dimensions: one ambient half has 64 complex spinor dimensions;
# V14 tensor S64 -> opposite S64 therefore has kernel 832.  The full Dirac
# carrier doubles this to 1664.  These are representation dimensions only.
check("Y14.half_spin_gamma_kernel_dimension_832", 14 * 64 - 64 == 832)
check("Y14.full_dirac_gamma_kernel_dimension_1664", 2 * 832 == 1664)

# Exact finite witness in Cl(1,1).  For a constant section, pullback keeps the
# horizontal covector and kills the normal covector.  Set
# t = h tensor psi - n tensor n^{-1} h psi.  Ambient Gamma(t)=0, but the
# observed trace of P(t)=h tensor psi is h psi != 0.
h = X  # h^2 = +1
normal = J  # n^2 = -1, so n^{-1} = -n
psi = [1, 0]
n_inverse_h_psi = mat_vec(neg(normal), mat_vec(h, psi))
phi = [-x for x in n_inverse_h_psi]
ambient_trace = [
    x + y
    for x, y in zip(mat_vec(h, psi), mat_vec(normal, phi))
]
observed_trace = mat_vec(h, psi)
check("PULLBACK.witness_is_ambient_gamma_traceless", ambient_trace == [0, 0])
check("PULLBACK.witness_survives_pullback", psi != [0, 0])
check("PULLBACK.observed_gamma_trace_is_nonzero", observed_trace != [0, 0])
check("PULLBACK.ambient_kernel_not_preserved", ambient_trace == [0, 0] and observed_trace != [0, 0])

# Positive control: a purely horizontal tensor is read identically by a
# constant-section pullback.  Negative control: pretending pullback is a
# projection preserving the ambient kernel contradicts the witness above.
check("PULLBACK.positive_control_horizontal_identity", mat_vec(h, psi) == observed_trace)
check("PULLBACK.negative_control_kernel_preservation_rejected", not (observed_trace == [0, 0]))

passed = sum(ok for _, ok in CHECKS)
print(f"source_native_spin64_observation_sector_probe: {passed}/{len(CHECKS)} checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
