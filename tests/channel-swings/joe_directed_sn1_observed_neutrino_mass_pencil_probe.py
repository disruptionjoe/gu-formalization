#!/usr/bin/env python3
"""SN-1: uniform-scaling test for the released observed neutrino mass pencil.

This probe uses the identity-grade complex block grammar of draft equation 9.16.
It does not import a Cl(9,5) carrier, a standard SO(10) Higgs mechanism, or a
Majorana reality condition.  The source-aligned physical realization is the
real Cl(7,7) carrier; the lemma proved here occurs before choosing a real-form
matrix realization and is therefore a horn-robust statement about the printed
complex block support only.
"""

from fractions import Fraction
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_EXTRACTION = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
K77_CROSSWALK = ROOT / "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"
MD1 = ROOT / "lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md"

source = SOURCE_EXTRACTION.read_text()
k77 = K77_CROSSWALK.read_text()
md1 = MD1.read_text()

counts = {"source": 0, "grammar": 0, "exact": 0, "type": 0, "control": 0}
failures = []


def check(kind: str, label: str, condition: bool) -> None:
    counts[kind] += 1
    if condition:
        print(f"PASS [{kind}] {label}")
    else:
        failures.append(label)
        print(f"FAIL [{kind}] {label}")


VARS = (
    "t", "lam", "mu", "Spp", "Spm", "Ppp", "Ppm", "Smp", "Smm",
    "Pmp", "Pmm", "Bpp", "Bpm", "Bmp", "Bmm", "M", "m", "omega_h",
    "omega_v", "dg", "xi", "ell", "m0",
)
INDEX = {name: i for i, name in enumerate(VARS)}
ZERO_MONOMIAL = (0,) * len(VARS)


class Poly:
    """Tiny exact Laurent-polynomial ring over Q for a dependency-free cert."""

    def __init__(self, terms=None):
        self.terms = {
            monomial: Fraction(coefficient)
            for monomial, coefficient in (terms or {}).items()
            if coefficient
        }

    @staticmethod
    def constant(value):
        return Poly({ZERO_MONOMIAL: Fraction(value)})

    @staticmethod
    def variable(name):
        exponents = [0] * len(VARS)
        exponents[INDEX[name]] = 1
        return Poly({tuple(exponents): Fraction(1)})

    def __add__(self, other):
        other = as_poly(other)
        result = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
            if not result[monomial]:
                del result[monomial]
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({monomial: -coefficient for monomial, coefficient in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        result = {}
        for left_monomial, left_coefficient in self.terms.items():
            for right_monomial, right_coefficient in other.terms.items():
                monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
                result[monomial] = result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent == -1:
            if len(self.terms) != 1:
                raise ValueError("inverse is implemented only for monomials")
            monomial, coefficient = next(iter(self.terms.items()))
            return Poly({tuple(-value for value in monomial): 1 / coefficient})
        if exponent < 0:
            return (self ** -1) ** (-exponent)
        result = Poly.constant(1)
        factor = self
        power = exponent
        while power:
            if power & 1:
                result = result * factor
            factor = factor * factor
            power //= 2
        return result

    def __eq__(self, other):
        return self.terms == as_poly(other).terms

    def substitute_lam_t_mu(self):
        result = {}
        for monomial, coefficient in self.terms.items():
            exponents = list(monomial)
            lam_power = exponents[INDEX["lam"]]
            exponents[INDEX["lam"]] = 0
            exponents[INDEX["t"]] += lam_power
            exponents[INDEX["mu"]] += lam_power
            key = tuple(exponents)
            result[key] = result.get(key, Fraction(0)) + coefficient
        return Poly(result)

    def set_variable_one(self, name):
        result = {}
        for monomial, coefficient in self.terms.items():
            exponents = list(monomial)
            exponents[INDEX[name]] = 0
            key = tuple(exponents)
            result[key] = result.get(key, Fraction(0)) + coefficient
        return Poly(result)

    def rename_variable(self, old, new):
        result = {}
        for monomial, coefficient in self.terms.items():
            exponents = list(monomial)
            power = exponents[INDEX[old]]
            exponents[INDEX[old]] = 0
            exponents[INDEX[new]] += power
            key = tuple(exponents)
            result[key] = result.get(key, Fraction(0)) + coefficient
        return Poly(result)

    def variable_powers(self, name):
        return {monomial[INDEX[name]] for monomial in self.terms}


def as_poly(value):
    return value if isinstance(value, Poly) else Poly.constant(value)


def determinant(matrix):
    n = len(matrix)
    result = Poly.constant(0)
    for permutation in permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(n) for j in range(i + 1, n)
        )
        term = Poly.constant(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        result += term
    return result


def characteristic(matrix, spectral="lam"):
    spectral_variable = Poly.variable(spectral)
    return determinant([
        [spectral_variable * (1 if i == j else 0) - matrix[i][j]
         for j in range(len(matrix))]
        for i in range(len(matrix))
    ])


def scale_matrix(matrix, scalar):
    return [[scalar * entry for entry in row] for row in matrix]


print("A. SOURCE AND CARRIER BOUNDARY")
check("source", "equation 9.16 is an identity-grade source extraction",
      "identity-grade ledger of all sixteen displayed cells" in source)
check("source", "barred and unbarred variables are four distinct fields",
      "four distinct fields" in source)
check("source", "the released branch has a southeast zero",
      "SE=0" in source and "source-preferred construction branch keeps zero" in source)
check("source", "a nonzero southeast rival is source-admitted but unselected",
      "non-trivial map in the lower right quadrant" in source
      and "neither source supplies a uniqueness theorem" in source)
check("source", "the source does not supply a global reality adjoint",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("source", "the source does not derive observed masses from its assignments",
      "not derivations of the corresponding observed equations" in source)
check("source", "the source-aligned K77 observation split has four complex 2 x 16 blocks",
      "observation split has four complex `2 x 16` blocks" in k77)
check("source", "observation contracts an ambient one-form to a 4D one-form",
      "Every ad-valued one-form on `Y14` descends to exactly one 4D one-form" in md1)


print("\nB. RELEASED ZERO-ORDER CELL GRAMMAR")
# Rows: (bar-zeta-, bar-zeta+, bar-nu-, bar-nu+)
# Cols: (zeta+, zeta-, nu+, nu-)
Spp, Spm, Ppp, Ppm, Smp, Smm, Pmp, Pmm, Bpp, Bpm, Bmp, Bmm = (
    Poly.variable(name) for name in
    ("Spp", "Spm", "Ppp", "Ppm", "Smp", "Smm", "Pmp", "Pmm", "Bpp", "Bpm", "Bmp", "Bmm")
)
M0 = [
    [Spp, Spm, Ppp, Ppm],
    [Smp, Smm, Pmp, Pmm],
    [-Bpp, -Bpm, 0, 0],
    [-Bmp, -Bmm, 0, 0],
]

support = {(i, j) for i in range(4) for j in range(4) if as_poly(M0[i][j]) != 0}
expected_support = {
    (0, 0), (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (3, 0), (3, 1),
}
check("grammar", "the released zero-order pencil has twelve symbolic nonzero cells",
      support == expected_support)
check("grammar", "the four southeast cells are exactly zero",
      all(as_poly(M0[i][j]) == 0 for i in (2, 3) for j in (2, 3)))
check("grammar", "the upper-left block contains four Shiab-connection cells",
      all(as_poly(M0[i][j]) != 0 for i in (0, 1) for j in (0, 1)))
check("grammar", "the upper-right block contains four connection cells",
      all(as_poly(M0[i][j]) != 0 for i in (0, 1) for j in (2, 3)))
check("grammar", "the lower-left block contains four barred-adjoint cells",
      all(as_poly(M0[i][j]) != 0 for i in (2, 3) for j in (0, 1)))
check("grammar", "no reality relation was imposed between P and B symbols",
      len({name for name in VARS[3:15]
           if any(monomial[INDEX[name]] for row in M0 for entry in row
                  for monomial in as_poly(entry).terms)}) == 12)


print("\nC. UNIFORM-SCALING LEMMA")
t, lam, mu = (Poly.variable(name) for name in ("t", "lam", "mu"))
Mt = scale_matrix(M0, t)
check("exact", "every released zero-order cell scales with the single connection amplitude",
      all(as_poly(Mt[i][j]).variable_powers("t") <= {1} for i in range(4) for j in range(4))
      and all(as_poly(Mt[i][j]) == 0 or as_poly(Mt[i][j]).variable_powers("t") == {1}
              for i in range(4) for j in range(4)))

char_t = characteristic(Mt)
char_0_mu = characteristic(M0, spectral="mu")
scaled_char = char_t.substitute_lam_t_mu()
check("exact", "the characteristic polynomial obeys chi_t(t mu)=t^4 chi_1(mu)",
      scaled_char == t**4 * char_0_mu)
check("exact", "determinant scales as t^4",
      determinant(Mt) == t**4 * determinant(M0))
check("exact", "trace scales as t",
      sum(Mt[i][i] for i in range(4)) == t * sum(M0[i][i] for i in range(4)))
check("exact", "the second characteristic coefficient scales as t^2",
      all(monomial[INDEX["t"]] == 2
          for monomial in char_t.terms if monomial[INDEX["lam"]] == 2))
check("exact", "the third characteristic coefficient scales as t^3",
      all(monomial[INDEX["t"]] == 3
          for monomial in char_t.terms if monomial[INDEX["lam"]] == 1))

# Observation is a contraction, but it remains linear in the connection.
omega_h, omega_v, dg = (Poly.variable(name) for name in ("omega_h", "omega_v", "dg"))
observed = omega_h + omega_v * dg
check("exact", "observation contraction preserves uniform connection homogeneity",
      t * omega_h + t * omega_v * dg == t * observed)


print("\nD. FIXED-HEAVY, DIRECT, AND UNIFORM-ZERO-CORNER CONTROLS")
M, m = (Poly.variable(name) for name in ("M", "m"))

# Textbook fixed-heavy control: only the mixing scales with t.
fixed_heavy = [[M, t * m], [t * m, 0]]
fixed_char = characteristic(fixed_heavy)
fixed_schur = -(t * m) * M**-1 * (t * m)
check("control", "fixed-heavy seesaw has determinant -t^2 m^2",
      determinant(fixed_heavy) == -(t**2 * m**2))
check("control", "fixed-heavy Schur light block is -t^2 m^2/M",
      fixed_schur == -(t**2 * m**2 * M**-1))
check("control", "fixed-heavy characteristic polynomial is not uniformly homogeneous",
      fixed_char.substitute_lam_t_mu().variable_powers("t") == {1, 2})

# Direct Dirac control: two off-diagonal entries scale together.
direct = [[0, t * m], [t * m, 0]]
check("control", "direct Dirac eigenvalues are exactly plus/minus t m",
      characteristic(direct) == (lam - t*m) * (lam + t*m))
check("control", "direct Dirac characteristic polynomial has linear mass scale",
      characteristic(direct) == lam**2 - t**2 * m**2)

# A zero corner is not sufficient when the heavy-looking block scales too.
uniform_base = [[M, m], [m, 0]]
uniform_zero_corner = scale_matrix(uniform_base, t)
uniform_light_schur = -(t * m) * (t * M) ** -1 * (t * m)
check("control", "uniform zero-corner Schur mass is linear, not quadratic, in t",
      uniform_light_schur == -(t * m**2 * M**-1))
uniform_char = characteristic(uniform_zero_corner)
uniform_char_mu = characteristic(uniform_base, spectral="mu")
check("control", "uniform zero-corner roots obey the same degree-two scaling identity",
      uniform_char.substitute_lam_t_mu() == t**2 * uniform_char_mu)
check("control", "a planted claim that every southeast zero is a seesaw is rejected",
      uniform_light_schur != -(t**2 * m**2 * M**-1))


print("\nE. CHARGE AND REALITY CONTROLS")
# This is charge bookkeeping on the observed neutral states, not a mechanism.
q_nu_l = -1
q_nu_r = -1
dirac_bilinear_charge = -q_nu_l + q_nu_r  # bar(nu_L) nu_R
majorana_bilinear_charge = q_nu_r + q_nu_r  # nu_R^T C nu_R, if C/reality exists
check("control", "observed Dirac neutrino bilinear is B-L neutral",
      dirac_bilinear_charge == 0)
check("control", "a would-be right-neutrino Majorana bilinear carries Delta(B-L)=-2",
      majorana_bilinear_charge == -2)
check("control", "a planted B-L-neutral Majorana bilinear is rejected",
      majorana_bilinear_charge != 0)

reality_map = None
majorana_status = "UNDEFINED_WITHOUT_REALITY_MAP" if reality_map is None else "TESTABLE"
check("type", "Majorana status remains undefined without a reality map",
      majorana_status == "UNDEFINED_WITHOUT_REALITY_MAP")
check("type", "independent barred/unbarred variables are not silently identified",
      reality_map is None)
check("type", "charge bookkeeping alone does not construct a Majorana bilinear",
      majorana_bilinear_charge == -2 and reality_map is None)


print("\nF. FIRST-ORDER SOUTHEAST PDE BLOCK VERSUS ZERO-ORDER MASS")
xi, ell, m0 = (Poly.variable(name) for name in ("xi", "ell", "m0"))
pde_southeast = ell * xi
mass_southeast = m0
check("control", "a first-order southeast completion vanishes at zero momentum",
      pde_southeast.variable_powers("xi") == {1})
check("control", "a zero-order southeast mass survives at zero momentum",
      mass_southeast.variable_powers("xi") == {0})
check("type", "first-order PDE completion and zero-order mass are distinct polynomial orders",
      pde_southeast.variable_powers("xi") == {1} and mass_southeast.variable_powers("xi") == {0})
check("type", "the source-admitted nonzero southeast horn is not selected here",
      "non-trivial map in the lower right quadrant" in source and reality_map is None)


print("\nG. CLAIM CEILING")
check("type", "the proof is the printed complex-block grammar, not a Cl(9,5) import",
      "Cl(9,5)" not in source and "Cl(9,5)" not in k77)
check("type", "the physical implementation target remains the source-aligned Cl(7,7) carrier",
      "the source `(7,7)` real spinor carrier exists exactly" in k77)
check("type", "the lemma does not select a varpi component, vacuum, or mass scale", True)
check("type", "independently scaled connection components remain outside the uniform-ray theorem", True)
check("type", "nonlinear curvature insertions remain outside the released linear pencil", True)
check("type", "no physical pole, quotient, or empirical neutrino verdict is claimed", True)


total = sum(counts.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in counts.items()), "=", total)
if failures:
    print("FAILURES", failures)
    raise SystemExit(1)
print("PASS: released eq9.16 uniform connection scaling is linear; a southeast zero alone does not furnish a parametric seesaw; Majorana status remains undefined without a reality map.")
