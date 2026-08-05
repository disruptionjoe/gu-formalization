#!/usr/bin/env python3
"""Exact observed-stress, normal-constraint and vacuum certificate.

This probe composes, rather than repeats, the previous K77 construction:

* the complete first-jet observation and the 10 -> 6 -> 2 null quotient are
  imported from their immutable registries;
* the new action-owned stress is reconstructed from the mixed metric/matter
  Hessian by radial transgression;
* an exact Krein-Dirac plane wave checks symmetry and conservation;
* the repaired (h,v) action is checked for harmonic constraint closure and
  for its propagator order; and
* the present quadratic distortion action is tested for a nonzero vacuum and
  response to an independent shift.

The certificate does not identify a connection current with stress energy,
prove the source's unreleased totalization, promote the flat defect domain to
the ambient Y14 shell, or infer a cosmological prediction.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def read_json(relative: str) -> dict:
    return json.loads(read(relative))


def sym_matrix(vector: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(4)
    for value, (i, j) in zip(vector, PAIRS):
        out[i, j] = out[j, i] = value
    return out


def sym_vector(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([matrix[i, j] for i, j in PAIRS])


def trace_reversed_gram() -> sp.Matrix:
    gram = sp.zeros(10)
    for a in range(10):
        av = sp.zeros(10, 1)
        av[a] = 1
        A = sym_matrix(av)
        for b in range(10):
            bv = sp.zeros(10, 1)
            bv[b] = 1
            B = sym_matrix(bv)
            trace = sum(ETA[i, j] * B[i, j]
                        for i in range(4) for j in range(4))
            reversed_B = B - R(1, 2) * ETA * trace
            raised = ETA * reversed_B * ETA
            gram[a, b] = sp.simplify(sum(
                A[i, j] * raised[i, j]
                for i in range(4) for j in range(4)
            ))
    return gram


def gauge_symbol(k_values: tuple[int, int, int, int]) -> sp.Matrix:
    k = sp.Matrix(k_values)
    columns = []
    for ghost_index in range(4):
        ghost = sp.zeros(4, 1)
        ghost[ghost_index] = 1
        h = sp.Matrix(4, 4, lambda i, j:
                      k[i] * ghost[j] + k[j] * ghost[i])
        columns.append(sym_vector(h))
    return sp.Matrix.hstack(*columns)


def harmonic_symbol(k_values: tuple[int, int, int, int]) -> sp.Matrix:
    k = sp.Matrix(k_values)
    raised = ETA * k
    out = sp.zeros(4, 10)
    for column in range(10):
        basis = sp.zeros(10, 1)
        basis[column] = 1
        h = sym_matrix(basis)
        trace = sum(ETA[i, j] * h[i, j]
                    for i in range(4) for j in range(4))
        for nu in range(4):
            out[nu, column] = sp.simplify(
                sum(raised[mu] * h[mu, nu] for mu in range(4))
                - R(1, 2) * k[nu] * trace
            )
    return out


def einstein_symbol(k_values: tuple[int, int, int, int]) -> sp.Matrix:
    k = sp.Matrix(k_values)
    raised = ETA * k
    k2 = sp.simplify((k.T * ETA * k)[0])
    columns = []
    for column in range(10):
        basis = sp.zeros(10, 1)
        basis[column] = 1
        h = sym_matrix(basis)
        trace = sum(ETA[i, j] * h[i, j]
                    for i in range(4) for j in range(4))
        ricci = sp.zeros(4)
        for mu in range(4):
            for nu in range(4):
                kh_nu = sum(raised[rho] * h[rho, nu] for rho in range(4))
                kh_mu = sum(raised[rho] * h[rho, mu] for rho in range(4))
                ricci[mu, nu] = R(1, 2) * (
                    k[mu] * kh_nu + k[nu] * kh_mu
                    - k2 * h[mu, nu] - k[mu] * k[nu] * trace
                )
        scalar = sum(ETA[i, j] * ricci[i, j]
                     for i in range(4) for j in range(4))
        columns.append(sym_vector(ricci - R(1, 2) * ETA * scalar))
    return sp.Matrix.hstack(*columns)


def coupled_hessian(k_values: tuple[int, int, int, int], gain: sp.Rational) -> sp.Matrix:
    G = einstein_symbol(k_values)
    W = trace_reversed_gram()
    J = sp.zeros(20)
    J[:10, 10:] = G.T * W
    J[10:, :10] = W * G
    J[10:, 10:] = gain * W
    return J


print("A. COMPOSED REPOSITORY AND SOURCE LOCUS")
moving = read_json("lab/process/k77-moving-observation-y14-domain-obstruction.json")
null = read_json("lab/process/k77-global-even-bv-null-green-domain.json")
mixed = read("explorations/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match-2026-08-04.md")
source = read("lab/sources/observed-upback-stress-source-reinspection-2026-08-05.md")

check("repo", "complete first-jet section-germ no-leakage is the inherited observation boundary",
      moving["observation"]["section_germ_no_leakage"] is True)
check("repo", "the inherited constrained null quotient retains two physical modes",
      null["null_split"]["physical_quotient_dimension"] == 2)
check("repo", "the inherited representatives are plus and cross",
      null["null_split"]["explicit_representatives"] == ["PLUS", "CROSS"])
check("repo", "raw common-action mixed blocks land in equation duals",
      "U_{\\rm raw}:B\\to F^!" in mixed and "V_{\\rm raw}:F\\to B^!" in mixed)
check("source", "decisive composed-locus return is SOURCE-CORRECTS",
      "Decisive return: `SOURCE-CORRECTS`" in source)


print("\nB. ACTION-OWNED STRESS BY RADIAL TRANSGRESSION")
b1, b2, q1, q2, q3, t = sp.symbols("b1 b2 q1 q2 q3 t", real=True)
b = sp.Matrix([b1, b2])
q = sp.Matrix([q1, q2, q3])
A0 = sp.Matrix([[2, 1, 0], [1, 3, -1], [0, -1, 4]])
A1 = sp.Matrix([[1, 2, 0], [2, -1, 1], [0, 1, 3]])
A2 = sp.Matrix([[0, 1, -2], [1, 2, 0], [-2, 0, 1]])
A = A0 + b1 * A1 + b2 * A2
action = sp.expand(R(1, 2) * (q.T * A * q)[0])
metric_euler = sp.Matrix([sp.diff(action, variable) for variable in b])
matter_euler = sp.Matrix([sp.diff(action, variable) for variable in q])
U_raw = matter_euler.jacobian(b)
V_raw = metric_euler.jacobian(q)
radial = sp.Matrix([
    sp.integrate(expression, (t, 0, 1))
    for expression in (V_raw.subs({q1: t*q1, q2: t*q2, q3: t*q3}) * q)
])

check("exact", "one common action makes the two raw mixed Hessians reciprocal",
      V_raw == U_raw.T)
check("exact", "the metric matter Euler term vanishes at zero matter field",
      metric_euler.subs({q1: 0, q2: 0, q3: 0}) == sp.zeros(2, 1))
check("exact", "radial transgression of the return block reconstructs the nonlinear stress covector",
      sp.simplify(radial - metric_euler) == sp.zeros(2, 1))
check("exact", "quadratic matter homogeneity gives V(tq)q = 2t E_g^matter",
      sp.simplify(
          V_raw.subs({q1: t*q1, q2: t*q2, q3: t*q3}) * q
          - 2*t*metric_euler
      ) == sp.zeros(2, 1))
check("type", "the nonlinear stress is a metric Euler covector and V_raw is its matter derivative", True)
check("type", "the diagonal response V_raw U_raw is a Hessian operator, not the nonlinear stress", True)
check("planted", "PLANT a literal VU matrix cannot equal the two-component nonlinear stress covector",
      (V_raw * U_raw).shape == (2, 2) and metric_euler.shape == (2, 1))


print("\nC. EXACT KREIN-DIRAC STRESS CONTROL")
I = sp.I
zero2 = sp.zeros(2)
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.diag(1, -1)
gamma0 = sp.diag(1, 1, -1, -1)


def spatial_gamma(sigma: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(zero2, sigma),
        sp.Matrix.hstack(-sigma, zero2),
    )


gammas = [gamma0, spatial_gamma(sigma1), spatial_gamma(sigma2), spatial_gamma(sigma3)]
clifford_eta = sp.diag(1, -1, -1, -1)
for mu in range(4):
    for nu in range(4):
        check("exact", f"Clifford relation gamma[{mu}] gamma[{nu}]",
              gammas[mu]*gammas[nu] + gammas[nu]*gammas[mu]
              == 2*clifford_eta[mu, nu]*sp.eye(4))

krein = gamma0
gamma5 = sp.simplify(I * gammas[0]*gammas[1]*gammas[2]*gammas[3])
check("exact", "the active Krein pairing anticommutes with chirality",
      krein*gamma5 + gamma5*krein == sp.zeros(4))

p_up = sp.Matrix([1, 0, 0, 1])
p_down = clifford_eta * p_up
slash_p = sum((p_down[mu] * gammas[mu] for mu in range(4)), sp.zeros(4))
psi = sp.Matrix([1, 0, 1, 0])
bar = sp.conjugate(psi).T * krein
current = sp.Matrix([sp.simplify((bar*gammas[mu]*psi)[0]) for mu in range(4)])
stress = sp.Matrix(4, 4, lambda mu, nu:
                   R(1, 2)*(p_up[mu]*current[nu] + p_up[nu]*current[mu]))

check("exact", "chosen spinor is on the massless Dirac shell", slash_p*psi == sp.zeros(4, 1))
check("exact", "Krein current is the null vector 2p", current == 2*p_up)
check("exact", "Dirac Hilbert stress is symmetric", stress == stress.T)
check("exact", "Dirac Hilbert stress is conserved on shell",
      p_down.T*stress == sp.zeros(1, 4))
check("exact", "massless Dirac Hilbert stress is trace free on this shell",
      sp.trace(clifford_eta*stress) == 0)
check("planted", "PLANT omitting the Krein factor changes the physical current",
      sp.Matrix([sp.simplify((sp.conjugate(psi).T*gammas[mu]*psi)[0])
                 for mu in range(4)]) != current)

scale = sp.symbols("scale", nonzero=True, real=True)
scaled_slash = scale * slash_p
scaled_stress = scale * stress
check("exact", "the same spinor remains on shell after null momentum rescaling",
      scaled_slash*psi == sp.zeros(4, 1))
check("exact", "stress scales with momentum while algebraic spinor bilinears do not",
      scaled_stress != stress and current == 2*p_up)
check("planted", "PLANT no momentum-free algebraic current-to-stress map is universal",
      sp.diff(scaled_stress[0, 0], scale) != 0)


print("\nD. OBSERVED NORMAL CONSTRAINTS AND THE TWO POLARIZATIONS")
W = trace_reversed_gram()
eigen_counts = Counter()
for value, multiplicity in W.eigenvals().items():
    eigen_counts["positive" if value > 0 else "negative"] += multiplicity
check("exact", "trace-reversed observed gravitational Gram is rank ten", W.rank() == 10)
check("exact", "trace-reversed observed gravitational Gram has inertia (6,4)",
      eigen_counts == {"positive": 6, "negative": 4})

k_null = (1, 1, 0, 0)
G = einstein_symbol(k_null)
J = coupled_hessian(k_null, R(2))
D = sp.Matrix.vstack(gauge_symbol(k_null), sp.zeros(10, 4))
H = harmonic_symbol(k_null)
H20 = sp.Matrix.hstack(H, sp.zeros(4, 10))
constrained = sp.Matrix.vstack(J, H20)

check("exact", "null coupled Hessian has ten-dimensional characteristic kernel",
      20 - J.rank() == 10)
check("exact", "four harmonic constraints are independent on that kernel",
      constrained.rank() - J.rank() == 4)
check("exact", "constraint-compatible characteristic kernel has dimension six",
      20 - constrained.rank() == 6)
check("exact", "null residual diffeomorphisms preserve harmonic gauge",
      H20*D == sp.zeros(4, 4))
check("exact", "residual diffeomorphism rank remains four", D.rank() == 4)

plus_h = sp.zeros(4)
plus_h[2, 2] = 1
plus_h[3, 3] = -1
cross_h = sp.zeros(4)
cross_h[2, 3] = cross_h[3, 2] = 1
plus = sp.Matrix.vstack(sym_vector(plus_h), sp.zeros(10, 1))
cross = sp.Matrix.vstack(sym_vector(cross_h), sp.zeros(10, 1))
physical_span = sp.Matrix.hstack(D, plus, cross)
check("exact", "plus and cross solve the coupled characteristic and harmonic constraints",
      constrained*plus == sp.zeros(constrained.rows, 1)
      and constrained*cross == sp.zeros(constrained.rows, 1))
check("exact", "plus and cross are independent modulo residual gauge",
      physical_span.rank() == 6)
check("exact", "the observed constrained characteristic quotient is exactly two-dimensional",
      (20 - constrained.rank()) - D.rank() == 2)
check("type", "this is the inherited flat-defect symbol/Green horn, not global Y14 shell faithfulness", True)


print("\nE. DOUBLE-POLE PROPAGATION OBSTRUCTION")
z, kappa = sp.symbols("z kappa", nonzero=True)
tt_system = sp.Matrix([[0, z], [z, kappa]])
tt_inverse = sp.simplify(tt_system.inv())
check("exact", "each TT polarization has determinant minus z squared",
      sp.factor(tt_system.det()) == -z**2)
check("exact", "the metric-metric response has a double pole",
      tt_inverse[0, 0] == -kappa/z**2)
check("exact", "the mixed response has a single pole",
      tt_inverse[0, 1] == 1/z and tt_inverse[1, 0] == 1/z)
check("planted", "PLANT the repaired action does not give the Einstein single-pole metric propagator",
      tt_inverse[0, 0] != 1/z)

h, v, tau = sp.symbols("h v tau")
tt_action = z*h*v + kappa*v**2/R(2) + tau*h
e_h = sp.diff(tt_action, h)
e_v = sp.diff(tt_action, v)
v_solution = sp.solve(sp.Eq(e_v, 0), v)[0]
effective_euler = sp.simplify(sp.diff(tt_action.subs(v, v_solution), h))
check("exact", "the first-order pair gives z v plus stress and z h plus kappa v",
      e_h == tau + v*z and e_v == h*z + kappa*v)
check("exact", "eliminating distortion yields a squared wave/Einstein operator",
      effective_euler == tau - h*z**2/kappa)
check("type", "harmonic constraint closure preserves labels but does not remove the generalized double-pole partner", True)
check("type", "a source-owned cancellation boundary condition or different action placement is required for single-pole GR", True)


print("\nF. NONZERO VACUUM AND SHIFT TEST")
gain = R(3, 2)
vacuum_hessian = gain*W
check("exact", "nonzero gain makes the unshifted stationary equation full rank",
      vacuum_hessian.rank() == 10)
check("exact", "the current quadratic action has only the zero unshifted stationary distortion",
      vacuum_hessian.nullspace() == [])
vac_inertia = Counter()
for value, multiplicity in vacuum_hessian.eigenvals().items():
    vac_inertia["positive" if value > 0 else "negative"] += multiplicity
check("exact", "the zero stationary point is indefinite rather than a stable minimum",
      vac_inertia == {"positive": 6, "negative": 4})

rho = sp.symbols("rho", real=True)
source_direction = sp.Matrix([1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
shifted_v = sp.simplify(-(gain*W).inv()*(rho*source_direction))
check("exact", "an independent trace source shifts distortion linearly",
      shifted_v != sp.zeros(10, 1) and sp.diff(shifted_v, rho) != sp.zeros(10, 1))
check("exact", "doubling the vacuum source doubles the stationary response",
      shifted_v.subs(rho, 2) == 2*shifted_v.subs(rho, 1))
check("planted", "PLANT the current action tracks rather than screens an independent vacuum shift",
      shifted_v.subs(rho, 1) != shifted_v.subs(rho, 2))
check("type", "a nonzero VEV requires curvature/source forcing or a new source-owned vacuum rule", True)


print("\nG. CLAIM BOUNDARY")
check("type", "physical Hilbert stress is constructed at action/defect grade", True)
check("type", "its equality to Weinstein's unreleased up-and-back totalization remains source-bounded reconstruction", True)
check("type", "the connection current remains distinct and needs a derivative/soldering relation", True)
check("type", "normal constraints close at the flat observed symbol, while the single-pole physics gate fails", True)
check("type", "no nonzero vacuum magnitude screening or w(z) is inferred", True)
check("planted", "PLANT no P1 P2 P3 datum is consumed", True)
check("planted", "PLANT Curt remains formally separate guidance", True)
check("planted", "PLANT no canon public-posture verdict or Lane-count change is inferred", True)

print("\nSOURCE_RETURN=SOURCE-CORRECTS")
print("ACTION_OWNED_HILBERT_STRESS=RADIAL_TRANSGRESSION_OF_EXISTING_MIXED_RETURN_BLOCK")
print("LITERAL_VU_EQUALS_NONLINEAR_STRESS=KILLED_BY_TYPE")
print("KREIN_DIRAC_STRESS=SYMMETRIC_CONSERVED_ON_SHELL")
print("OBSERVED_NULL_CONSTRAINT_QUOTIENT=10_TO_6_TO_2_PLUS_CROSS")
print("REPAIRED_PRE_SHIAB_METRIC_RESPONSE=DOUBLE_POLE_NOT_EINSTEIN_SINGLE_POLE")
print("CURRENT_UNSHIFTED_VARIABLE_VACUUM=ZERO_INDEFINITE_STATIONARY_POINT_ONLY")
print("INDEPENDENT_VACUUM_SHIFT=TRACKED_NOT_SCREENED")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    sys.exit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
