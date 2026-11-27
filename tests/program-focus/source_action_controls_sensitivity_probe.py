#!/usr/bin/env python3
"""Small exact comparator controls and bounded original GU arithmetic replay.

Conventional comparators bind only their declared actions, fields and domains.
They are not GU candidates or a bridge to a source-selected physical state space.
No native operator assembly, inverse regeneration, PDE simulation or physical
admission theorem is performed. The certificate distinguishes original-routine
replay from the new shared arithmetic adapter and analytic consequences.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BUNDLE = "lab/process/source-action-controls-certificates.json"
PRIOR = "tests/program-focus/source_action_q7_propagation_probe.py"
PRIOR_CERT = "lab/process/source-action-q7-propagation-certificates.json"
CHECKS = []
SOURCES = {
    "ADM": "https://arxiv.org/html/gr-qc/0405109v1",
    "harmonic_Einstein": "https://arxiv.org/html/1410.3490v1",
    "Stelle": "https://link.springer.com/article/10.1007/BF00760427",
    "Dirac_author_derivation": "https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S4.html",
}


class P:
    """Exact Q[k] coefficients, low degree only; no numerical extrapolation."""
    def __init__(self, value=0):
        self.c = value.c if isinstance(value, P) else tuple(map(F, value)) if isinstance(value, (tuple, list)) else (F(value),)
        while self.c and not self.c[-1]:
            self.c = self.c[:-1]

    def __add__(a, b):
        b = P(b)
        return P(tuple((a.c[i] if i < len(a.c) else 0) + (b.c[i] if i < len(b.c) else 0)
                       for i in range(max(len(a.c), len(b.c)))))
    __radd__ = __add__

    def __neg__(a): return P(tuple(-x for x in a.c))
    def __sub__(a, b): return a + -P(b)
    def __rsub__(a, b): return P(b) + -a

    def __mul__(a, b):
        b = P(b)
        if not a.c or not b.c:
            return P()
        c = [F(0)] * (len(a.c) + len(b.c) - 1)
        for i, x in enumerate(a.c):
            for j, y in enumerate(b.c):
                c[i+j] += x*y
        return P(c)
    __rmul__ = __mul__

    def __truediv__(a, b): return P(tuple(x/F(b) for x in a.c))
    def __eq__(a, b): return a.c == P(b).c
    def __bool__(a): return bool(a.c)
    def at(a, k): return sum((x*F(k)**i for i, x in enumerate(a.c)), F(0))
    def derivative(a): return P(tuple(i*a.c[i] for i in range(1, len(a.c))))


def require(value, label):
    if not value:
        raise AssertionError(label)
    CHECKS.append(label)


def zero(n, m=None): return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]
def eye(n): return [[F(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return [list(c) for c in zip(*a)]
def add(a, b): return [[x+y for x, y in zip(row, other)] for row, other in zip(a, b)]
def scale(c, a): return [[c*x for x in row] for row in a]
def mul(a, b): return [[sum((x*y for x, y in zip(row, col)), 0) for col in zip(*b)] for row in a]
def mv(a, v): return [sum((x*y for x, y in zip(row, v)), 0) for row in a]
def conj(x): return x.conj() if hasattr(x, "conj") else x
def pair(v, w): return sum((conj(x)*y for x, y in zip(v, w)), 0)
def quadratic(v, q): return pair(v, mv(q, v))
def iszero(a): return all(not x for row in a for x in row)
def eq(a, b): return a == b
def evaluated(a, k): return [[x.at(k) if isinstance(x, P) else F(x) for x in row] for row in a]
def conservation(k, q): return add(mul(transpose(k), q), mul(q, k))
def diag(values): return [[v if i == j else F(0) for j in range(len(values))] for i, v in enumerate(values)]


def blockdiag(*blocks):
    result = zero(sum(len(b) for b in blocks))
    start = 0
    for b in blocks:
        for i, row in enumerate(b):
            for j, x in enumerate(row):
                result[start+i][start+j] = x
        start += len(b)
    return result


def symplectic(n):
    j = zero(2*n)
    for i in range(n): j[i][n+i], j[n+i][i] = F(1), F(-1)
    return j


def rref(a):
    a = [[F(x) for x in row] for row in a]
    pivots, r = [], 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][col]
        a[r] = [x/divisor for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][col]
                a[i] = [x-c*y for x, y in zip(a[i], a[r])]
        pivots.append(col)
        r += 1
        if r == len(a): break
    return a, pivots


def rank(a): return len(rref(a)[1])


def kernel(a):
    reduced, pivots = rref(a)
    free = [j for j in range(len(a[0])) if j not in pivots]
    columns = []
    for j in free:
        v = [F(0)]*len(a[0]); v[j] = F(1)
        for i, p in enumerate(pivots): v[p] = -reduced[i][j]
        columns.append(v)
    return transpose(columns)


def inertia(a):
    """Rational congruence elimination, including zero-diagonal 2x2 cases."""
    a = [[F(x) for x in row] for row in a]
    require(a == transpose(a), "inertia input symmetric")
    pos = neg = null = 0
    while a:
        pivot = next((i for i in range(len(a)) if a[i][i]), None)
        if pivot is None:
            off = next(((i, j) for i in range(len(a)) for j in range(i+1, len(a)) if a[i][j]), None)
            if off is None:
                null += len(a); break
            i, j = off
            t = eye(len(a)); t[j][i] = 1  # replace e_i by e_i+e_j
            a = mul(transpose(t), mul(a, t)); pivot = i
        order = [pivot] + [i for i in range(len(a)) if i != pivot]
        a = [[a[i][j] for j in order] for i in order]
        d = a[0][0]
        pos += d > 0; neg += d < 0
        a = [[a[i][j]-a[i][0]*a[0][j]/d for j in range(1, len(a))] for i in range(1, len(a))]
    return {"positive": pos, "negative": neg, "zero": null}


def oscillator(s): return [[F(0), F(1)], [-s, F(0)]]


def adm_control():
    k = P((0, 1)); s = k*k
    # q=(h11,h22,h33,h12,h13,h23), p=(pi11,pi22,pi33,2pi12,2pi13,2pi23).
    # E=pi_ij*pi_ij-tr(pi)^2/2 + s*(h12^2-h11*h22)/2.
    v = zero(6); v[0][1] = v[1][0] = -s/2; v[3][3] = s
    t = blockdiag([[F(2*(i == j)-1) for j in range(3)] for i in range(3)], eye(3))
    h = blockdiag(v, t); j = symplectic(6); evolution = mul(j, h)
    c = zero(4, 12)
    c[0][0] = c[0][1] = 1
    c[1][8] = c[2][10] = c[3][11] = 1
    z = kernel(c); gauge = mul(j, transpose(c))
    restricted = mul(transpose(z), mul(h, z))
    require(rank(c) == 4 and len(z[0]) == 8 and rank(gauge) == 4, "ADM computed constraint/gauge ranks")
    require(iszero(mul(c, gauge)), "ADM first-class constraint algebra")
    require(iszero(mul(c, mul(evolution, z))), "ADM constraint propagation on kernel")
    require(iszero(mul(transpose(z), mul(h, gauge))), "ADM gauge is energy radical on constrained space")
    numeric_restricted = evaluated(restricted, 1)
    radical = mul(z, kernel(numeric_restricted))
    require(rank(radical) == 4 and rank([a+b for a, b in zip(radical, gauge)]) == 4, "ADM full constrained radical equals derived gauge image")
    computed_inertia = inertia(numeric_restricted)
    require(computed_inertia == {"positive": 4, "negative": 0, "zero": 4}, "ADM constrained inertia from congruence")
    # Canonical quotient coordinates (u,v,P,Q): h11=u,h22=-u,h12=v;
    # pi11=P/2,pi22=-P/2,2pi12=Q.
    f = zero(12, 4)
    f[0][0] = f[3][1] = f[9][3] = 1; f[1][0] = -1
    f[6][2], f[7][2] = F(1, 2), F(-1, 2)
    physical_h = mul(transpose(f), mul(h, f))
    physical_k = mul(symplectic(2), physical_h)
    require(iszero(mul(c, f)) and rank([a+b for a, b in zip(f, gauge)]) == 8, "ADM quotient section spans kernel modulo gauge")
    require(mul(transpose(f), mul(j, f)) == symplectic(2), "ADM quotient coordinates canonical")
    require(physical_h == diag([s, s, 1, 1]), "ADM quotient energy derived positive for every k>0")
    require(mul(evolution, f) == mul(f, physical_k), "ADM quotient evolution intertwines full generator")
    require(mul(physical_k, physical_k) == scale(-s, eye(4)), "ADM both physical pairs have wave frequency k")
    require(iszero(conservation(evolution, h)) and iszero(conservation(physical_k, physical_h)), "ADM canonical energy conservation")
    trace_momentum = [F(0)]*12
    trace_momentum[6:9] = [F(1)]*3
    raw = quadratic(trace_momentum, evaluated(h, 1))/2
    require(raw == -F(3, 2) and any(mv(c, trace_momentum)), "ADM negative raw trace is excluded by constraints")
    bad_c = c[1:]; bad_z = kernel(bad_c)
    bad_inertia = inertia(mul(transpose(bad_z), mul(evaluated(h, 1), bad_z)))
    require(bad_inertia["negative"] > 0, "ADM deleting scalar constraint exposes negative energy")
    wrong = [row[:] for row in physical_h]; wrong[3][3] = 4
    wrong_k = mul(symplectic(2), wrong)
    require(mul(wrong_k, wrong_k) != scale(-s, eye(4)), "ADM wrong off-diagonal canonical factor fails wave normalization")
    negative_mode = diag([-s, s, -1, 1]); negative_k = mul(symplectic(2), negative_mode)
    require(mul(negative_k, negative_k) == scale(-s, eye(4)), "ADM whole oscillator sign flip preserves wave equation")
    require(iszero(conservation(negative_k, physical_h)), "ADM sign-flipped oscillator still has positive conserved estimate norm")
    return {"domain": "Linearized vacuum ADM, nonzero Fourier vector rotated to (0,0,k), k>0; each real Fourier quadrature.",
            "canonical_coordinates": "q=(h11,h22,h33,h12,h13,h23); p=(pi11,pi22,pi33,2pi12,2pi13,2pi23)",
            "energy_hessian": h, "generator": evolution, "normalized_constraints": c,
            "constraint_kernel": z, "gauge_image": gauge, "constrained_inertia_at_k1": computed_inertia,
            "all_k_positive_quotient_hessian": physical_h, "quotient_generator": physical_k,
            "raw_trace_energy": raw, "raw_trace_admitted": False,
            "scalar_constraint_deleted_inertia_at_k1": bad_inertia,
            "ceiling": "Linearized constraint/gauge quotient only. A negative unphysical trace direction is not a physical ghost. No nonlinear GR theorem is computed."}


def harmonic_control():
    k = P((0, 1)); s = k*k
    a, q = oscillator(s), diag([s, 1])
    require(iszero(conservation(a, q)), "harmonic wave positive weighted norm conservation for all k")
    require(mul(a, a) == scale(-s, eye(2)), "harmonic wave equation for all k")
    # All ten trace-reversed metric components obey this block. A harmonic
    # constraint is a constant combination of components and first derivatives;
    # commutation with the common wave operator propagates C and dt C.
    ten = blockdiag(*([a]*10))
    require(mul(ten, ten) == scale(-s, eye(20)), "ten harmonic components share the same wave operator")
    require(iszero(conservation(ten, blockdiag(*([q]*10)))), "ten harmonic waves conserve componentwise estimate norm")
    require(not iszero(conservation(a, eye(2))), "unweighted equal-order wave norm is not the conserved norm")
    return {"generator_one_component": a, "positive_estimate_form": q,
            "domain": "Mean-zero torus modes or |k|>=1; (h,dt h) in H^(s+1) x H^s. Low frequencies require a separate bounded-time inhomogeneous estimate.",
            "constraint_propagation": "Analytic: C_nu=partial^mu hbar_mu_nu commutes with the common wave operator; zero C and dt C initial data propagate.",
            "ceiling": "The probe checks the common flat wave operator, not the nonlinear harmonic-gauge existence theorem or full physical quotient."}


def linearized_bianchi_control():
    """Off-shell tensor contraction, independent of ADM canonical energy."""
    eta = [F(-1), F(1), F(1), F(1)]
    xi = list(map(F, (2, 1, 3, 4)))
    raised = [eta[i]*xi[i] for i in range(4)]
    norm = pair(xi, raised)
    require(norm == 22, "Bianchi declared all-nonzero covector is non-null")
    rows = []
    trace_failures = raising_failures = 0
    for a in range(4):
        for b in range(a, 4):
            h = zero(4); h[a][b] = h[b][a] = F(1)
            trace_h = sum(eta[i]*h[i][i] for i in range(4))
            v = mv(transpose(h), raised)
            ricci = [[(norm*h[i][j]+xi[i]*xi[j]*trace_h-xi[i]*v[j]-xi[j]*v[i])/2
                      for j in range(4)] for i in range(4)]
            scalar = sum(eta[i]*ricci[i][i] for i in range(4))
            require(scalar == norm*trace_h-pair(raised, v), f"Bianchi basis{a}{b} Ricci trace identity")
            trace_term = diag([eta[i]*scalar/2 for i in range(4)])
            einstein = add(ricci, scale(-1, trace_term))
            divergence = mv(transpose(einstein), raised)
            require(not any(divergence), f"Bianchi basis{a}{b} off-shell divergence zero")
            wrong_trace = mv(transpose(add(ricci, trace_term)), raised)
            wrong_raising = mv(transpose(einstein), xi)
            trace_failures += any(wrong_trace)
            raising_failures += any(wrong_raising)
            rows.append({"symmetric_basis": [a, b], "linearized_scalar": scalar,
                         "divergence": divergence, "wrong_trace_sign_divergence": wrong_trace,
                         "wrong_index_raising_divergence": wrong_raising})
    require(trace_failures == 10, "Bianchi wrong relative trace sign fails on every declared basis")
    require(raising_failures > 0, "Bianchi missing Lorentz index raising detected")
    return {"metric_diagonal": eta, "covector_lower": xi, "covector_norm_squared": norm,
            "basis_checks": rows, "wrong_trace_sign_failure_count": trace_failures,
            "wrong_index_raising_failure_count": raising_failures,
            "finite_scope": "At this one declared covector, linearity and all ten symmetric h basis tensors give the off-shell identity for arbitrary h. This is not a frequency sampling proof of the generic identity.",
            "generic_analytic_derivation": "For arbitrary xi, v_nu=xi^rho h_rho,nu and r=xi^2 tr(h)-xi^rho v_rho. Direct contraction gives xi^mu R_mu,nu=xi_nu r/2. Subtraction of eta_mu,nu r/2 therefore gives xi^mu G_mu,nu=0, with no field equation or non-null assumption. The displayed cancellation supplies the generic proof; the tensor implementation tests it at the declared covector.",
            "typing_ceiling": "Adapter-only tensor-contraction control for linearized Einstein G. It is not a native GU theta coderivative replay, a theta=T to stress dictionary, or a proof of GU conservation."}


def stelle_control():
    k = P((0, 1)); a = k*k; d = F(4); b = a+d
    # One TT helicity, positive Einstein branch, m2^2=d=4. An overall positive
    # polarization normalization has been removed. L=(-hddot^2+(a+b)hdot^2-ab*h^2)/(2d).
    h = [[a*b/d, 0, 0, 0], [0, -(a+b)/d, 1, 0], [0, 1, 0, 0], [0, 0, 0, -d]]
    canonical_k = mul(symplectic(2), h)
    jet_k = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-a*b, 0, -(a+b), 0]]
    # z=(h,hdot,hddot,hdddot); canonical momenta P0=((a+b)hdot+hdddot)/d, P1=-hddot/d.
    momenta = [[1, 0, 0, 0], [0, 1, 0, 0], [0, (a+b)/d, 0, 1/d], [0, 0, -1/d, 0]]
    require(mul(momenta, jet_k) == mul(canonical_k, momenta), "Stelle Ostrogradsky generator matches original fourth-order equation")
    jet_h = mul(transpose(momenta), mul(h, momenta))
    expected_jet_h = [[a*b/d, 0, 0, 0], [0, (a+b)/d, 0, 1/d], [0, 0, -1/d, 0], [0, 1/d, 0, 0]]
    require(jet_h == expected_jet_h, "Stelle canonical energy derived in original jet variables")
    transform = [[b/d, 0, 1/d, 0], [0, b/d, 0, 1/d], [-a/d, 0, -1/d, 0], [0, -a/d, 0, -1/d]]
    inverse = [[1, 0, 1, 0], [0, 1, 0, 1], [-a, 0, -b, 0], [0, -a, 0, -b]]
    factor_k = blockdiag(oscillator(a), oscillator(b))
    signed = diag([a, 1, -b, -1]); positive = diag([a, 1, b, 1])
    require(mul(transform, inverse) == eye(4) and mul(inverse, transform) == eye(4), "Stelle factor-variable map exactly invertible")
    require(mul(transform, jet_k) == mul(factor_k, transform), "Stelle fourth-order equation factors into two wave oscillators")
    require(mul(transpose(transform), mul(signed, transform)) == jet_h, "Stelle energy split is a derived congruence")
    require(iszero(conservation(jet_k, jet_h)), "Stelle original canonical energy conserved")
    require(iszero(conservation(factor_k, signed)) and iszero(conservation(factor_k, positive)), "Stelle signed energy and positive estimate norm both conserved")
    require(inertia(evaluated(signed, 1)) == {"positive": 2, "negative": 2, "zero": 0}, "Stelle physical TT energy has both signs")
    require(inertia(evaluated(positive, 1)) == {"positive": 4, "negative": 0, "zero": 0}, "Stelle positive estimate form")
    # Initial jets of h=cos(sqrt(a)t) and h=cos(sqrt(b)t), evaluated at k=1.
    positive_jet, negative_jet = [F(1), 0, -F(1), 0], [F(1), 0, -F(5), 0]
    energy_plus = quadratic(positive_jet, evaluated(jet_h, 1))/2
    energy_minus = quadratic(negative_jet, evaluated(jet_h, 1))/2
    require(energy_plus == F(1, 2) and energy_minus == -F(5, 2), "Stelle actual sinusoidal solution jets have opposite canonical energy")
    require(mul(add(mul(jet_k, jet_k), scale(a, eye(4))), add(mul(jet_k, jet_k), scale(b, eye(4)))) == zero(4), "Stelle characteristic factorization identity in all k")
    return {"domain": "One real TT polarization of ordinary classical flat quadratic gravity, positive Einstein branch, m2^2=4, k>0; no alternate quantum prescription.",
            "lagrangian": "[-hddot^2+(2k^2+4)hdot^2-k^2(k^2+4)h^2]/8",
            "canonical_order": "(h,hdot,P0,P1)", "canonical_hessian": h, "canonical_generator": canonical_k,
            "jet_order": "(h,hdot,hddot,hdddot)", "jet_generator": jet_k, "jet_energy_hessian": jet_h,
            "factor_transform": transform, "factor_inverse": inverse, "factor_generator": factor_k,
            "factor_signed_energy": signed, "factor_positive_estimate_form": positive,
            "sinusoid_energies_at_k1": [energy_plus, energy_minus],
            "finite_loss_analytic_bound": "On k>=1, U=diag(k,1,sqrt(k^2+4),1)T has norm O(k^3), inverse O(k^2). Factor evolution is U-unitary. Hence the original unweighted four-jet propagator is O(k^5), giving a (nonoptimal) finite five-derivative-loss Duhamel bound. Polynomial matrix identities are computed; this norm estimate is the displayed analytic deduction.",
            "ceiling": "Negative canonical energy is an actual TT ghost under the stated classical prescription, but it does not establish high-frequency exponential growth, nonlinear runaway or a quantum verdict."}


def realify(a, b):
    return [x+[-z for z in y] for x, y in zip(a, b)] + [x+y for x, y in zip(b, a)]


def dirac_control():
    pauli_real = [[[0, 1], [1, 0]], zero(2), [[1, 0], [0, -1]]]
    pauli_imag = [zero(2), [[0, -1], [1, 0]], zero(2)]
    alpha = []
    for sr, si in zip(pauli_real, pauli_imag):
        ar, ai = zero(4), zero(4)
        for i in range(2):
            for j in range(2):
                ar[i][j+2] = ar[i+2][j] = sr[i][j]
                ai[i][j+2] = ai[i+2][j] = si[i][j]
        alpha.append(realify(ar, ai))
    beta = realify(diag([1, 1, -1, -1]), zero(4))
    clifford = alpha+[beta]
    for i, a in enumerate(clifford):
        require(a == transpose(a), f"Dirac realified Hermitian generator {i}")
        for j, b in enumerate(clifford):
            require(add(mul(a, b), mul(b, a)) == scale(2*(i == j), eye(8)), f"Dirac Clifford anticommutator {i},{j}")
    imaginary = realify(zero(4), eye(4))
    d = add(scale(3, alpha[0]), scale(4, beta)); k = scale(-1, mul(imaginary, d))
    require(iszero(conservation(k, eye(8))) and iszero(conservation(k, d)), "Dirac positive norm and two-sided energy conserved")
    require(mul(d, d) == scale(25, eye(8)), "Dirac sample dispersion exactly 25")
    plus, minus = [F(3), 0, 0, 1, 0, 0, 0, 0], [F(1), 0, 0, -3, 0, 0, 0, 0]
    require(mv(d, plus) == [5*x for x in plus] and mv(d, minus) == [-5*x for x in minus], "Dirac exact positive/negative energy spinors")
    require(quadratic(plus, d) == 50 and quadratic(minus, d) == -50 and pair(plus, plus) == pair(minus, minus) == 10, "Dirac negative energy is distinct from positive norm")
    rest = [F(1), 0, 0, 0, 0, 0, 0, 0]
    require(mv(scale(4, beta), rest) == [4*x for x in rest], "Dirac second current spinor on shell")
    current = []
    for matrix in [eye(8)]+alpha:
        value = mv(matrix, plus)
        current.append([pair(rest, value), -pair(rest, mv(imaginary, value))])
    residual = [current[0][i]-3*current[1][i] for i in range(2)]
    require(current[0] == [3, 0] and current[1] == [1, 0] and residual == [0, 0], "Dirac nonzero polarized current obeys full on-shell continuity cancellation")
    mutated = [2*current[0][i]-3*current[1][i] for i in range(2)]
    require(mutated == [3, 0], "Dirac off-shell energy mutation fails continuity")
    # Wrong complex transpose pairing represented by Re(psi^T psi), not psi^dagger psi.
    wrong_pairing = diag([1]*4+[-1]*4)
    require(not iszero(conservation(k, wrong_pairing)), "Dirac dropping complex conjugation fails norm conservation")
    return {"domain": "Ordinary free complex Dirac comparator on flat R3 or torus with Hermitian pairing; realified to eight real coordinates.",
            "sample_momentum_mass": {"k": [3, 0, 0], "m": 4}, "hamiltonian_realified": d, "generator_realified": k,
            "positive_norm_form": eye(8), "sample_energies": [50, -50], "sample_norms": [10, 10],
            "all_frequency_reason": "Computed Clifford anticommutators imply D(k)^2=(|k|^2+m^2)I and K^*+K=0 for every real k,m, so every H^s norm is conserved.",
            "polarized_current": current, "current_covector_difference": [1, -3, 0, 0], "continuity_residual": residual,
            "off_shell_mutant_residual": mutated,
            "ceiling": "A negative first-quantized Dirac energy eigenvalue is not by itself a physical ghost. CAR/vacuum and interacting QFT are outside this control."}


def growth_and_density_controls():
    k = P((0, 1)); wave = [[0, k], [-k, 0]]; elliptic = [[0, k], [k, 0]]; nilpotent = [[0, k], [0, 0]]
    require(iszero(conservation(wave, eye(2))), "balanced wave positive norm conserved")
    require(mul(wave, wave) == scale(-k*k, eye(2)), "balanced wave imaginary-frequency square")
    require(mv(elliptic, [1, 1]) == [k, k], "elliptic exact growing eigenvector")
    require(iszero(conservation(elliptic, diag([1, -1]))), "elliptic exponential system can conserve an indefinite form")
    require(not iszero(conservation(elliptic, eye(2))), "elliptic system fails positive Euclidean conservation")
    require(iszero(mul(nilpotent, nilpotent)) and not iszero(nilpotent), "nilpotent square zero but nonzero")
    traces = {}
    for name, matrix in (("wave", wave), ("elliptic", elliptic), ("nilpotent", nilpotent)):
        square = mul(matrix, matrix)
        traces[name] = {"trace": sum(matrix[i][i] for i in range(2)), "trace_square": sum(square[i][i] for i in range(2))}
    require(traces["elliptic"]["trace_square"] == 2*k*k and traces["wave"]["trace_square"] == -2*k*k and not traces["nilpotent"]["trace_square"], "trace-square sufficient growth criterion distinguishes these exact controls")
    # Rindler density: div J=(1/x) d_x(x J^x). For J=1/x the densitized flux is 1.
    require(P(1).derivative() == 0 and k.derivative() == 1, "Rindler densitized flux differentiation")
    x = F(2); derivative = -1/(x*x); density_term = 1/(x*x)
    require(derivative+density_term == 0 and derivative != 0, "Rindler omission of density term detected")
    return {"balanced_wave_generator": wave, "elliptic_generator": elliptic, "nilpotent_generator": nilpotent,
            "trace_checks": traces,
            "analytic_growth_consequences": {
                "elliptic": "Exact eigenvector (1,1) evolves by exp(k t). For any fixed t>0 this exceeds every polynomial k^N, ruling out every fixed finite Sobolev-loss bound in polynomially comparable norms.",
                "nilpotent": "exp(tK)=I+tK exactly. At fixed nonzero t its norm grows linearly in k, so equal-order uniform bounds fail, while one derivative loss suffices, including the Duhamel forcing estimate on bounded time intervals.",
                "wave": "Balanced generator is skew and has a conserved positive Euclidean norm.",
                "criterion_ceiling": "Trace zero plus positive real trace-square is a sufficient spectral-growth test. Its absence is not a general stability certificate."},
            "density_control": {"metric": "-x^2 dt^2+dx^2+dy^2+dz^2, x>0", "Jx=1/x": "divergence 0", "Jx=1": "divergence 1/x", "wrong_no_density_residual_at_x2": derivative},
            "typing_ceiling": "The density contraction is an adapter control only. A vector/Noether current and native adjoint-valued theta=T are different objects; no theta-to-stress map is supplied."}


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def interval(center, error):
    center, error = F(center), F(error)
    require(error >= 0, "nonnegative certified contraction error")
    low, high = center-error, center+error
    return {"center": str(center), "error_bound": str(error), "lower": str(low), "upper": str(high),
            "sign": "positive" if low > 0 else "negative" if high < 0 else "unresolved"}


def gu_arithmetic_adapter(repo):
    # This module imports standard-library definitions only. native_parity/run
    # are intentionally never called. Existing dependency hashes are enforced.
    spec = importlib.util.spec_from_file_location("gu_control_prior_q7", repo/PRIOR)
    prior = importlib.util.module_from_spec(spec); spec.loader.exec_module(prior)
    bindings, evolution, constraints, backgrounds = prior.load_bound(repo)
    prior_certificate = json.loads((repo/PRIOR_CERT).read_text())
    require(prior_certificate["dependency_bindings"] == bindings, "GU prior certificate dependency identities")
    original = prior.replay_diagonals(evolution, constraints, backgrounds)
    require(original == prior_certificate["roots"], "original GU replay_diagonals reproduces complete saved roots")
    rows = {row["basis_index"]: row for row in evolution["exact_probe"]["source_receivers"]}
    reproduced = []
    for root_index in (0, 1):
        root_rows = []
        for basis in (5, 12):
            require(rows[basis]["b7_lowered"] == [], f"GU root{root_index} witness{basis} N7 source exactly zero in owned data")
            source = {i: prior.C(*z) for i, z in rows[basis]["b6"]}
            coefficients, errors = {}, {}
            active_blocks = 0
            for block in constraints["spin6_inverse_candidates"][root_index]["blocks"]:
                ids = block["indices"]
                if not any(i in source for i in ids): continue
                inverse = [[prior.C(*value) for value in row] for row in block["rational_inverse"]]
                b = [source.get(i, prior.C()) for i in ids]
                solved = [-x for x in mv(inverse, b)]
                eta = F(block["neumann_bound"])
                require(0 <= eta < 1, f"GU root{root_index} witness{basis} Neumann eta admissible")
                bound = eta/(1-eta)*max(prior.cnorm(x) for x in solved)
                coefficients.update(zip(ids, solved)); errors.update((i, bound) for i in ids)
                active_blocks += 1
            ids = sorted(source)
            b = [source[i] for i in ids]; solved = [coefficients[i] for i in ids]
            value = pair(b, solved)  # The same contraction primitive as all control energies.
            error = sum(prior.cnorm(source[i])*errors[i] for i in ids)+abs(value.b)
            new = interval(value.a, error)
            old = next(row for row in original[root_index]["diagonals"] if row["basis_index"] == basis)
            require(all(new[key] == old[key] for key in new), f"GU root{root_index} witness{basis} full center/error/endpoints/sign reproduced by adapter")
            wrong = pair(b, [-x for x in solved])
            require(wrong == -value and str(wrong.a) != old["center"], f"GU root{root_index} witness{basis} missing auxiliary minus sign rejected")
            require(error > 0 and interval(value.a, 0) != new, f"GU root{root_index} witness{basis} discarded error bound detected")
            root_rows.append({"basis_index": basis, "active_saved_inverse_blocks": active_blocks, **new})
        require({row["sign"] for row in root_rows} == {"positive", "negative"}, f"GU root{root_index} both energy signs retained")
        reproduced.append({"root": root_index, "witnesses": root_rows})
    bindings = {**bindings, PRIOR: sha(repo/PRIOR), PRIOR_CERT: sha(repo/PRIOR_CERT)}
    return {"bindings": bindings, "roots": reproduced,
            "original_routines_executed": ["source_action_q7_propagation_probe.load_bound", "source_action_q7_propagation_probe.replay_diagonals"],
            "shared_adapter_executed": "pair and matrix-vector product independently recompute the exact saved b-dagger-c centers plus Neumann interval errors, comparing complete values rather than sign labels.",
            "not_run": ["native seed/parity reconstruction", "full reduced-evolution probe", "dense native M assembly or inverse solve", "native on-shell-current/conservation routines", "native microlocal packet or PDE proof"],
            "ceiling": "This is fresh bounded replay of owned GU energy arithmetic plus adapter calibration. It does not independently establish the imported source decomposition, inverse theorem, physical state admission, native PDE estimate or theta conservation."}


def serial(value):
    if isinstance(value, P): return {"Q_k_coefficients_ascending": [str(x) for x in value.c]}
    if isinstance(value, F): return str(value)
    if isinstance(value, dict): return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [serial(x) for x in value]
    return value


def run(repo):
    CHECKS.clear()
    # Check the small exact arithmetic itself against independent identities.
    k = P((0, 1))
    require((k+1)*(k-1) == k*k-1 and ((k+1)*(k-1)).at(3) == 8, "polynomial ring arithmetic sanity")
    require(inertia([[0, 1], [1, 0]]) == {"positive": 1, "negative": 1, "zero": 0}, "congruence handles zero-diagonal indefinite block")
    result = {"schema": "gu-controls-sensitivity-certificates-v1", "final_probe_sha256": sha(Path(__file__)),
              "status": "exact_controls_and_bounded_original_arithmetic_replay_pass",
              "polynomial_convention": "Q[k], coefficient lists ascending; identities checked coefficientwise for all real k. Positivity/domain statements use declared k>0 or k>=1. Stelle mass squared fixed at 4.",
              "source_urls": SOURCES, "GR_ADM": adm_control(), "GR_harmonic": harmonic_control(),
              "GR_linearized_Bianchi": linearized_bianchi_control(),
              "Stelle_TT": stelle_control(), "Dirac": dirac_control(),
              "growth_and_density": growth_and_density_controls(), "GU_energy_arithmetic": gu_arithmetic_adapter(repo),
              "routing_notice": "Conventional comparators bind only their stated model. No typed bridge to source-native GU physical mechanisms, no hypothesis vote, no default successor, and no source/GU exclusion follows from these controls.",
              "not_certified": ["global/nonlinear stability", "quantum unitarity or vacuum choice", "source-selected physical state rule", "theta=T as Einstein stress", "complete native diagnostic pipeline", "native finite-loss analytic packet proof"]}
    result["checks"] = CHECKS[:]; result["check_count"] = len(CHECKS)
    return serial(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write-certificate", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args(); repo = args.repo.resolve(); start = time.monotonic()
    result = run(repo); path = repo/BUNDLE
    if args.write_certificate:
        path.write_text(json.dumps(result, indent=2)+"\n")
    else:
        recorded = json.loads(path.read_text())
        require(recorded == result, "current exact replay equals recorded certificate")
    print(json.dumps({"passed": True, "checks": result["check_count"], "seconds": time.monotonic()-start,
                      "probe_sha256": sha(Path(__file__)), "certificate_sha256": sha(path),
                      "certificate_bytes": path.stat().st_size, "mode": "write" if args.write_certificate else "verify",
                      "no_dense_native_rebuild": True}, indent=2))


if __name__ == "__main__":
    main()
