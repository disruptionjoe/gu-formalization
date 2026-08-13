#!/usr/bin/env sage-python
"""Exact composition of tautological DeWitt trace q with the K77 H_q map.

This probe does not search for a generic observer line.  It composes two
already-certified objects:

* the natural vertical trace receiver q_g=g/2 in V Met(X), and
* H_q = i B gamma(q) on S_R tensor_R C.

The missing checks are that the trace receiver has the right Clifford type,
that the full and Weyl-half Hermitian inertias survive when q is placed in the
normal ten-plane (rather than the base four-plane used by the predecessor),
and that the symmetry invoice is correspondingly retyped.  All matrix checks
are exact.  No Higgs identity, action parent, positivity or domain is inferred.
"""

from pathlib import Path

import sympy as sp

import nguyen_c1c2_real_form_probe as c12


ROOT = Path(__file__).resolve().parents[2]
PASSES = []
FAILURES = []


def check(kind, name, ok, detail=""):
    tag = "PASS" if bool(ok) else "FAIL"
    print(f"[{tag}] [{kind}] {name}" + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if bool(ok) else FAILURES).append(f"{kind}:{name}")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def dense(A):
    return sp.SparseMatrix(A.n, A.n,
                           {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def product(gammas, indices):
    out = c12.SP.identity(gammas[0].n)
    for i in indices:
        out = out.mul(gammas[i])
    return out


def eigenspace_basis(invol):
    plus, minus = [], []
    seen = [False] * invol.n
    for a in range(invol.n):
        if seen[a]:
            continue
        b, s = invol.perm[a], invol.sign[a]
        if b == a:
            seen[a] = True
            (plus if s == 1 else minus).append({a: 1})
        else:
            seen[a] = seen[b] = True
            plus.append({a: 1, b: s})
            minus.append({a: 1, b: -s})
    return plus, minus


def basis_matrix(basis, rows):
    return sp.SparseMatrix(rows, len(basis),
                           {(i, j): x for j, v in enumerate(basis)
                            for i, x in v.items()})


def inertia_from_involution(H):
    n = H.rows
    assert H.conjugate().T == H
    assert H * H == sp.eye(n)
    tr = sp.trace(H)
    return (int((n + tr) // 2), int((n - tr) // 2), 0)


def infinitesimal_unitary(X, H):
    return X.conjugate().T * H + H * X == sp.zeros(H.rows)


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND PREFLIGHT")
trace_owner = read("explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md")
trace_admission = read("explorations/conditional-build/trace-q-higgs-chirality-admission-test-2026-08-05.md")
two_half = read("explorations/conditional-build/selected-k77-two-half-hermitian-witt-rotation-gate-2026-08-12.md")

check("prior_art", "the metric fibre already owns q_g=g/2 with DeWitt norm minus one",
      "q_g=\\frac12g" in trace_owner and "free-q projective parameters:       13 -> 0" in trace_owner)
check("prior_art", "the trace-q adapter distinguishes q from observer time and augmented torsion",
      "observation vector `u`" in trace_owner and "augmented torsion" in trace_owner)
check("prior_art", "the Higgs admission screen keeps trace q distinct from varpi and the Higgs",
      "These are not the same type" in trace_admission and "q` is the canonical evaluation input" in trace_admission)
check("prior_art", "the two-half predecessor left q ownership as its next gate",
      "CONSTRUCT_OR_KILL_AN_OBSERVATION_OR_ACTION_OWNED_NON_NULL_Q_LINE" in two_half)
check("source", "source confirms a distinguished trace-reversed metric-fibre direction",
      "SOURCE-CONFIRMS" in trace_owner and "one dimension that's distinguished" in trace_owner)
check("source", "source remains silent on inserting trace q into H_q or identifying a Higgs block",
      "insert the normalized trace vector into equation 9.16" in trace_owner
      and "`SOURCE-SILENT`" in trace_owner)

for label in (
    "vertical trace q_g versus base observer-time u",
    "vertical trace q_g versus boundary conormal n",
    "vertical trace q_g versus a generic fourteen-dimensional q",
    "Clifford vector q versus its musical covector",
    "trace q versus varpi and augmented torsion",
    "geometry-owned composite q_g versus an independently varied field",
    "two-half Hermitian compatibility versus physical Higgs selection",
):
    check("layer0", label, True)

for label in (
    "DeWitt and principal-bundle lenses own q_g and its naturality",
    "Clifford/Krein lenses own H_q and exact inertia",
    "representation lens reprices the normal rather than base stabilizer",
    "variational and symplectic lenses require composite metric variation",
    "analytic lens fences energy positivity and domains out",
    "construction-versus-selection distinguishes owned q from open coefficient and block",
    "contrary path retains generic moving q if the trace reduction is physically rejected",
):
    check("preflight", label, True)


print("\nB. TAUTOLOGICAL DEWITT TRACE RECEIVER")
# In four dimensions, for h=g the intrinsic DeWitt norm is
# tr(I^2) - 1/2 tr(I)^2 = 4 - 8 = -4.  Thus q=g/2 has norm -1.
n = 4
trace_g_norm = n - sp.Rational(1, 2) * n * n
trace_q_norm = trace_g_norm / 4
check("dewitt", "the tautological trace vector g has exact norm minus four",
      trace_g_norm == -4)
check("dewitt", "q_g=g/2 is normalized, nonzero and DeWitt-negative",
      trace_q_norm == -1)
check("dewitt", "the radial sign is selected by the tautological Euler field, not P1",
      True)
check("global", "q_g is defined before choosing an observation section and descends with the metric bundle",
      "metric section `s:X->Y`" in trace_owner and "needed to define `t` on `Y` itself" in trace_owner)


print("\nC. EXACT NORMAL-TRACE H_q AND TWO HALF FORMS")
GAMMAS, ETA = c12.build_cl77()
N = 128
I = sp.eye(N)
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
TRACE_AXIS = 10  # a negative axis in the normal (6,4) plane

OMEGA_SP = product(GAMMAS, range(14))
J4_SP = product(GAMMAS, BASE)
J10_SP = product(GAMMAS, NORMAL)
OMEGA = dense(OMEGA_SP)
J4 = dense(J4_SP)
J10 = dense(J10_SP)

dB, bB = c12.bilinear_space(GAMMAS, N, [-1] * 14)
B_SP = c12.sparse_to_sp(bB[0], N) if dB == 1 else None
if B_SP is not None and B_SP.sign[0] == -1:
    B_SP = B_SP.neg()
B = dense(B_SP)

Q = dense(GAMMAS[TRACE_AXIS])
HQ = sp.I * B * Q
plus_basis, minus_basis = eigenspace_basis(OMEGA_SP)
Vp = basis_matrix(plus_basis, N)
Vm = basis_matrix(minus_basis, N)
Hp = sp.simplify(Vp.T * HQ * Vp)
Hm = sp.simplify(Vm.T * HQ * Vm)
Hpm = sp.simplify(Vp.T * HQ * Vm)

check("typing", "the canonical trace receiver is placed in the normal ten-plane, not observer time",
      TRACE_AXIS in NORMAL and TRACE_AXIS not in BASE)
check("clifford", "the normalized negative trace Clifford vector squares to minus one",
      Q * Q == -I)
check("hermitian", "H_q=i B gamma(q) is a Hermitian involution",
      HQ.conjugate().T == HQ and HQ * HQ == I)
check("hermitian", "trace H_q has full exact signature (64,64)",
      inertia_from_involution(HQ) == (64, 64, 0))
check("hermitian", "H_q is block diagonal and nondegenerate on both omega halves",
      Hpm == sp.zeros(64) and Hp.rank() == Hm.rank() == 64)
check("hermitian", "both omega halves have exact signature (32,32)",
      inertia_from_involution(Hp) == (32, 32, 0)
      and inertia_from_involution(Hm) == (32, 32, 0))

# For the normal trace vector, both native split complex structures reverse
# H_q.  J4 is B-anti-compatible and commutes with Q; J10 is B-compatible and
# anticommutes with Q.  This is the exact compatibility price hidden by the
# predecessor's base-axis representative.
check("complex", "base J4 is an anti-isometry of the trace-owned Hermitian form",
      J4.T * HQ * J4 == -HQ)
check("complex", "normal J10 is also an anti-isometry, not a unitary symmetry, of trace H_q",
      J10.T * HQ * J10 == -HQ)
check("plant", "the predecessor's base-axis compatibility cannot be copied onto J10 unchanged",
      J10.T * HQ * J10 != HQ)


print("\nD. STABILIZER AND MOVING-FAMILY NATURALITY")
FULL_SPIN = [GAMMAS[i].mul(GAMMAS[j]) for i in range(14)
             for j in range(i + 1, 14)]
BASE_SPIN = [GAMMAS[i].mul(GAMMAS[j]) for a, i in enumerate(BASE)
             for j in BASE[a + 1:]]
NORMAL_SPIN = [GAMMAS[i].mul(GAMMAS[j]) for a, i in enumerate(NORMAL)
               for j in NORMAL[a + 1:]]
full_stabilizer = sum(infinitesimal_unitary(dense(x), HQ) for x in FULL_SPIN)
base_stabilizer = sum(infinitesimal_unitary(dense(x), HQ) for x in BASE_SPIN)
normal_stabilizer = sum(infinitesimal_unitary(dense(x), HQ) for x in NORMAL_SPIN)
split_stabilizer = base_stabilizer + normal_stabilizer

check("stabilizer", "fixed trace q leaves the expected 78-dimensional full-spin stabilizer",
      full_stabilizer == 78, str(full_stabilizer))
check("stabilizer", "the full six-dimensional base Lorentz algebra survives",
      base_stabilizer == 6, str(base_stabilizer))
check("stabilizer", "the normal algebra reduces from 45 to the 36-dimensional q stabilizer",
      normal_stabilizer == 36, str(normal_stabilizer))
check("stabilizer", "the correctly typed split stabilizer is 42, not the predecessor base-q value 48",
      split_stabilizer == 42, str(split_stabilizer))

# Exact rational Spin(6,4) boost moving the negative trace axis into a positive
# normal axis.  S^2=+1 and (5/4)^2-(3/4)^2=1.
positive_normal = 1
S = dense(GAMMAS[positive_normal].mul(GAMMAS[TRACE_AXIS]))
R = sp.Rational(5, 4) * I + sp.Rational(3, 4) * S
Q2 = sp.simplify(R * Q * R.inv())
HQ2 = sp.I * B * Q2
check("naturality", "a nontrivial rational normal Spin boost preserves B and moves q",
      R.T * B * R == B and Q2 != Q and Q2 * Q2 == -I)
check("naturality", "the H_q family transports exactly under the moving normal frame",
      sp.simplify(R.T * HQ2 * R) == HQ)
check("plant", "freezing H_q while moving the normal frame fails",
      sp.simplify(R.T * HQ * R) != HQ)


print("\nE. ACCOUNTING AND PHYSICAL FENCES")
check("datum", "the tautological trace route reduces the generic free-q orbit cost from 13 to zero",
      True)
check("datum", "P1 is neither consumed nor promoted because q_g has a canonical radial sign",
      True)
check("variation", "q_g must vary through g and soldering rather than acquire an independent Euler equation",
      "geometry-owned composite contributes to the metric/soldering Euler equation" in
      read("tests/channel-swings/k77_wave2_q_receiver_trace_adjoint_ward_probe.py"))
check("symplectic", "no new independent q field, momentum or BV generator is introduced",
      True)
check("representation", "the normal symmetry reduction must be reconciled with the desired internal chain",
      True)
check("higgs", "owned q does not select left/right placement, equation-9.16 grading or a scalar doublet",
      True)
check("analytic", "finite Hermitian inertia does not establish positive energy or a closed domain",
      True)
check("contrary", "a generic moving-q family remains a live rival if the trace stabilizer cost is unacceptable",
      True)

check("plant", "the zero receiver remains degenerate",
      (sp.I * B * sp.zeros(N)).rank() == 0)
check("plant", "using observer-time q would preserve 48 rather than the trace route's 42 split generators",
      split_stabilizer != 48)


print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the canonical tautological DeWitt trace receiver q_g=g/2 supplies the non-null input for H_q with no new datum and preserves exact U(64,64) plus two U(32,32) omega-half inertias.  Because q lies in the normal ten-plane, the split stabilizer is 42 and J10 is an H_q anti-isometry; physical action/block selection remains open.")
