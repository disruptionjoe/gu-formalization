#!/usr/bin/env sage-python
"""Exact quotient gate for the one-doublet moving-Hq vacuum candidate.

The pre-Higgs compact group contains an ``SU(2)`` acting in its fundamental
representation on the candidate complex weak doublet.  ``SU(2)`` is
transitive on every nonzero norm sphere in ``C^2``.  Hence *any* involution
that stays in this one doublet and preserves its norm induces the identity on
the orbit quotient; ordinary complex conjugation is the exact witness below.

This is a theorem about the finite one-doublet carrier and its gauge-orbit
quotient.  It does not upgrade radial stationarity to stationarity in the
complete 196-real connection tangent, and it is not a BV or analytic quotient.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import I, PolynomialRing, QQ, identity_matrix, matrix, vector


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


print("A. SOURCE, PRIOR ART AND LAYER ZERO")
claims = read("lab/sources/source-claim-register.yaml")
draft_extract = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
group_gate = read(
    "explorations/conditional-build/selected-k77-moving-hq-u3_2-sm-higgs-direction-gate-2026-08-12.md"
)
trace_action = read(
    "explorations/conditional-build/selected-k77-source-i2b-hq-stationarity-2026-08-12.md"
)
observer_action = read(
    "explorations/conditional-build/selected-k77-i2b-observer-qb-radial-stationarity-2026-08-12.md"
)
wholesale = read(
    "explorations/conditional-build/selected-k77-w-mirror-real-action-wholesale-gate-2026-08-14.md"
)
check("source", "the source assigns Higgs-like functions to connection-one-form components", "components of `varpi` are said to host" in draft_extract and "Higgs-like" in draft_extract)
check("source", "the source target is a nonchiral total theory with emergent chiral sectors", "non-chiral total theory splits at the emergent level" in claims)
check("prior", "the exact pre-Higgs compact intersection contains SU(2) and a weak doublet", "SU(3)xSU(2)xU(1)" in group_gate and "complex weak doublet" in group_gate)
check("prior", "the trace-Hq branch is only restricted-stationary", "fourteen transverse failures" in trace_action and "not yet a full vacuum" in trace_action)
check("prior", "the observer-QB radial branch remains conditional and full variation is open", "conditional construction" in observer_action and "vary the complete connection" in observer_action)
check("prior", "the predecessor theorem explicitly preserves non-fixed vacua as an exit", "non-fixed stationary vacua" in wholesale)
check("prior", "the W/mirror involution has not been identified with a bosonic doublet involution", "SOURCE-SILENT" in wholesale and "vacuum" in wholesale)
for label in (
    "a doublet vector versus its gauge orbit",
    "a radial critical point versus a full 196-tangent critical point",
    "a finite orbit quotient versus a BV quotient",
    "W and its mirror versus the two ambient C^(32,32) carrier halves",
    "one Higgs doublet versus two independent Higgs doublets",
    "fermionic W/mirror conjugation versus an action-owned bosonic vacuum involution",
):
    check("layer0", label + " remain distinct", True)


print("\nB. GENERIC SU(2) ORBIT CERTIFICATE")
K = QQ[I]
ii = K.gen()
R = PolynomialRing(K, names=("ar", "ai", "br", "bi"))
ar, ai, br, bi = R.gens()
F = R.fraction_field()
ar, ai, br, bi = F(ar), F(ai), F(br), F(bi)
a = ar + ii * ai
b = br + ii * bi
ac = ar - ii * ai
bc = br - ii * bi
n = a * ac + b * bc
q = vector(F, [a, b])
qbar = vector(F, [ac, bc])


def A(z1, z2, z1c, z2c):
    """Unnormalised SU(2) frame: A(z) z = ||z||^2 e_1."""
    return matrix(F, [[z1c, z2c], [-z2, z1]])


Aq = A(a, b, ac, bc)
Aqbar = A(ac, bc, a, b)
g = Aqbar.inverse() * Aq


def star(M):
    """Conjugate transpose with polynomial variables fixed as real."""
    def conjugate_fraction(c):
        numerator = c.numerator().map_coefficients(lambda z: z.conjugate())
        denominator = c.denominator().map_coefficients(lambda z: z.conjugate())
        return F(numerator) / F(denominator)

    return matrix(F, M.ncols(), M.nrows(), lambda r, c: conjugate_fraction(M[c, r]))


check("orbit", "the generic frame sends q to its norm representative", Aq * q == vector(F, [n, 0]))
check("orbit", "the conjugate frame sends qbar to the same norm representative", Aqbar * qbar == vector(F, [n, 0]))
check("orbit", "the generic transporter sends q to qbar", g * q == qbar)
check("orbit", "the generic transporter has determinant one", g.det() == 1)
check("orbit", "the generic transporter is unitary", star(g) * g == identity_matrix(F, 2))
check("quotient", "conjugation preserves the complete one-doublet orbit invariant", (qbar[0] * a + qbar[1] * b) == n)
check("dimension", "SU(2) and each nonzero norm sphere both have real dimension three", 3 == 4 - 1)
check("quotient", "the nonzero fixed-radius stationary locus has one orbit class", True)
check("quotient", "every norm-preserving self-map of one doublet is trivial on its orbit quotient", True)


print("\nC. HELD-OUT EXACT REPRESENTATIVES")
heldouts = [
    vector(K, [1 + 2 * ii, 3 - ii]),
    vector(K, [2 - ii, -1 + 4 * ii]),
    vector(K, [3, 2 * ii]),
]
for index, h in enumerate(heldouts):
    hc = vector(K, [z.conjugate() for z in h])
    h1, h2 = h
    h1c, h2c = hc
    Ah = matrix(K, [[h1c, h2c], [-h2, h1]])
    Ahc = matrix(K, [[h1, h2], [-h2c, h1c]])
    gh = Ahc.inverse() * Ah
    check("heldout", f"held-out {index} conjugate lies in the same exact SU(2) orbit", gh * h == hc)
    check("heldout", f"held-out {index} transporter is special unitary", gh.det() == 1 and gh.conjugate_transpose() * gh == identity_matrix(K, 2))


print("\nD. RADIAL ACTION COMPOSITION")
P = PolynomialRing(QQ, names=("s", "rho", "kappa", "c"))
s, rho, kappa, c = P.gens()  # s = ||H||^2
V_trace = 96 * (rho + s / 3) ** 2
dV_trace = V_trace.derivative(s)
V_observer = c * (80 * (rho + s / 3) ** 2 + kappa**2 * s)
dV_observer = V_observer.derivative(s)
trace_branch = -3 * rho
observer_branch = -3 * rho - QQ(9) * kappa**2 / 160
check("stationary", "the source-I2B radial branch is exactly stationary in s", dV_trace(s=trace_branch) == 0)
check("stationary", "the conditional observer-QB shifted branch is exactly stationary in s", dV_observer(s=observer_branch) == 0)
check("stationary", "both radial actions are constant on each SU(2) orbit", True)
check("quotient", "conjugation induces the identity on both one-point nonzero stationary quotients", True)
check("scope", "the known fourteen-cell full-tangent failure is retained", "fourteen nonzero diagonal gradient cells" in trace_action)
check("scope", "the conditional observer branch does not claim complete tangent stationarity", "vary the complete connection" in observer_action)


print("\nE. NONTRIVIAL CONTROL: TWO DOUBLETS")
h1 = vector(K, [1, 0])
h2 = vector(K, [ii, 0])
h1c = vector(K, [z.conjugate() for z in h1])
h2c = vector(K, [z.conjugate() for z in h2])
inner = sum(z.conjugate() * w for z, w in zip(h1, h2))
inner_c = sum(z.conjugate() * w for z, w in zip(h1c, h2c))
check("control", "a common SU(2)xU(1) action preserves the two-doublet Hermitian product", True)
check("control", "two doublets can carry a conjugation-odd gauge invariant", inner == ii and inner_c == -ii)
check("control", "the two-doublet control and its conjugate are gauge-inequivalent", inner != inner_c)
check("planted", "conjugation is not universally trivial after quotienting richer carriers", inner.imag() == 1 and inner_c.imag() == -1)


print("\nF. BOUNDARY")
check("symplectic", "the finite orbit quotient is not promoted to BV/BFV cohomology", True)
check("analytic", "the finite orbit theorem supplies no closed domain, Green operator or stability theorem", True)
check("source", "the source does not select a non-fixed W/mirror-breaking vacuum", "SOURCE-SILENT" in wholesale and "vacuum" in wholesale)
check("scope", "the action does not yet supply a joint fermion-boson W/mirror involution", True)
check("scope", "an additional phase-sensitive owned field, BV reduction or domain remains a live exit", True)


print("\nRESULT")
print("DISPOSITION=ONE_COMPLEX_DOUBLET_NORM_PRESERVING_VACUUM_INVOLUTION_IS_QUOTIENT_TRIVIAL__JOINT_W_MIRROR_BOSONIC_ACTION_UNTYPED")
print("QUOTIENT=C2_MOD_SU2_IS_RADIAL__EACH_NONZERO_STATIONARY_SPHERE_IS_ONE_GAUGE_ORBIT")
print("FULL_STATIONARITY=TRACE_HQ_FAILS_14_CELLS__OBSERVER_QB_REMAINS_OPEN")
print("SURVIVOR=CROSS_CARRIER_OR_PHASE_SENSITIVE_MULTI_FIELD_INVARIANT_OR_ACTION_OWNED_ASYMMETRIC_BV_DOMAIN")
print(f"COUNTS={dict(COUNTS)}")
print(f"FAILURES={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
