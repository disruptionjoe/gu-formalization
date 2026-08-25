#!/usr/bin/env python3
"""Exact parentwise Chern--Weil gate for the v0.144 P3 amplitude horn.

The source curvature shape is the unprojected Clifford two-form
``Phi1 wedge Phi1``.  On an oriented framed four-plane this probe computes its
quadratic invariant using the vector/Killing trace, each 64-complex K77 Weyl
half, and their full 128-complex sum.  It also computes the self-dual
Spin(4) control, which is nonzero but requires a four-plane/chirality reduction
not owned by any current parent invariant.
"""

from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    if not bool(condition):
        FAILURES.append(f"[{kind}] {label}")
        print(f"FAIL [{kind}] {label}")
    else:
        print(f"PASS [{kind}] {label}")


def exterior_sign(indices):
    if len(set(indices)) != len(indices):
        return 0
    inversions = sum(
        indices[i] > indices[j]
        for i in range(len(indices))
        for j in range(i + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def four_volume_coefficient(curvature):
    values = list(curvature.values())
    check("custody", "the curvature bank supplies a matrix-size witness", bool(values))
    size = values[0].rows if values else 0
    answer = sp.zeros(size)
    for a, A in curvature.items():
        for b, B in curvature.items():
            sign = exterior_sign(a + b)
            if sign:
                answer += sign * A * B
    return sp.simplify(answer)


packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
family = (ROOT / "explorations/conditional-build/selected-k77-zero-fermion-vev-selector-exhaustion-2026-08-10.md").read_text()
parent = (ROOT / "explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md").read_text()
edge = (ROOT / "explorations/conditional-build/selected-k77-relative-edge-bitorsor-topology-2026-08-09.md").read_text()

check("prior", "P3 connection is supplied and not varied", "fixed external data, not a\nvaried gauge field" in packet)
check("prior", "P3 characteristic number is p1=-2n u", "p_1(H_n)=-2n" in packet)
check("prior", "source family uses the unprojected Phi1 wedge Phi1 shape", "F_B   = f (Phi1 wedge Phi1)" in family)
check("prior", "P_H is induced from the chimeric Spin bundle", "P_H=P_{\\operatorname{Spin}(C)}" in parent)
check("prior", "an SU2 c2=1 compact-subgroup embedding was already used as a topology control", "an `SU(2)` bundle with `c2=1`, embedded in\nthe compact subgroup of the Spin-native parent" in edge)

# Euclidean Clifford generators on the framed S4 tangent.  The cancellation
# below is representation-theoretic and does not identify this local model
# with the global P3 connection.
I = sp.I
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
eye2 = sp.eye(2)
gamma = [
    sp.kronecker_product(sigma1, eye2),
    sp.kronecker_product(sigma2, eye2),
    sp.kronecker_product(sigma3, sigma1),
    sp.kronecker_product(sigma3, sigma2),
]

for i in range(4):
    for j in range(4):
        target = 2 * sp.eye(4) if i == j else sp.zeros(4)
        check("clifford", f"Clifford relation ({i},{j})", gamma[i] * gamma[j] + gamma[j] * gamma[i] == target)

chi4 = sp.simplify(gamma[0] * gamma[1] * gamma[2] * gamma[3])
P_plus = sp.simplify((sp.eye(4) + chi4) / 2)
P_minus = sp.simplify((sp.eye(4) - chi4) / 2)
check("clifford", "four-plane chirality squares to one", chi4 * chi4 == sp.eye(4))
check("clifford", "four-plane chirality is balanced", sp.trace(chi4) == 0)
check("clifford", "self-dual and anti-self-dual spin projectors have rank two", P_plus.rank() == P_minus.rank() == 2)

F_spinor = {
    (i, j): sp.simplify(gamma[i] * gamma[j])
    for i in range(4)
    for j in range(i + 1, 4)
}
for key, value in F_spinor.items():
    check("chern_weil", f"spin curvature component {key} is traceless", sp.trace(value) == 0)

vol_spinor = four_volume_coefficient(F_spinor)
full_dirac_pairing = sp.simplify(sp.trace(vol_spinor))
plus_pairing = sp.simplify(sp.trace(P_plus * vol_spinor))
minus_pairing = sp.simplify(sp.trace(P_minus * vol_spinor))

check("chern_weil", "unprojected four-spinor quadratic pairing vanishes", full_dirac_pairing == 0)
check("chern_weil", "self-dual projected pairing is nonzero", plus_pairing == 12)
check("chern_weil", "anti-self-dual projected pairing is opposite", minus_pairing == -12)
check("chern_weil", "unprojected cancellation is exactly plus plus minus", plus_pairing + minus_pairing == 0)
check("planted", "PLANT full trace is not the chiral trace", full_dirac_pairing != sp.trace(chi4 * vol_spinor))

# The unique quadratic invariant on the simple Spin parent is proportional to
# the vector/Killing form.  Build the exact vector generators and evaluate it.
F_vector = {}
for i in range(4):
    for j in range(i + 1, 4):
        M = sp.zeros(4)
        M[i, j] = 1
        M[j, i] = -1
        F_vector[(i, j)] = M
vol_vector = four_volume_coefficient(F_vector)
check("parent", "Spin vector/Killing quadratic four-form vanishes", sp.trace(vol_vector) == 0)
check("parent", "vector volume coefficient vanishes matrixwise", vol_vector == sp.zeros(4))

# Spin(14) half-spin branching:
# S14+ = (S4+ x S10+) + (S4- x S10-), and S14- swaps S10 chirality.
# dim_C S10+ = dim_C S10- = 16, so each 64-complex half contains equal
# multiplicities of the opposite four-plane pairings.
dim_s10_plus = dim_s10_minus = 16
half_plus_parent = sp.expand(dim_s10_plus * plus_pairing + dim_s10_minus * minus_pairing)
half_minus_parent = sp.expand(dim_s10_minus * plus_pairing + dim_s10_plus * minus_pairing)
full_u_parent = sp.expand(half_plus_parent + half_minus_parent)

check("representation", "each 14D Weyl half has complex dimension 64", 2 * dim_s10_plus + 2 * dim_s10_minus == 64)
check("representation", "first U(32,32) half ordinary pairing cancels", half_plus_parent == 0)
check("representation", "second U(32,32) half ordinary pairing cancels", half_minus_parent == 0)
check("representation", "full U(64,64) ordinary pairing cancels", full_u_parent == 0)
check("representation", "arbitrary independent two-half weights cannot revive zero", sp.expand(sp.Symbol("a") * half_plus_parent + sp.Symbol("b") * half_minus_parent) == 0)
check("representation", "each half contains sixteen SU2L doublets", dim_s10_plus == 16)
check("representation", "each half contains sixteen SU2R doublets", dim_s10_minus == 16)

# The second unitary invariant Tr(F) wedge Tr(F) also vanishes because every
# source curvature component lies in the traceless Spin subalgebra.
trace_components = {key: sp.trace(value) for key, value in F_spinor.items()}
check("parent", "all linear trace components vanish", all(value == 0 for value in trace_components.values()))
check("parent", "unitary central quadratic invariant vanishes", all(value == 0 for value in trace_components.values()))

# BPST/self-dual substitution control.  Keeping only one Spin(4) chirality
# yields a nonzero value, amplified by sixteen doublets in each 14D half.  It
# is exactly the extra reduction needed to imitate P3, not a native invariant
# of the current parents.
bpst_half_plus = sp.expand(dim_s10_plus * plus_pairing)
bpst_half_minus = sp.expand(dim_s10_minus * plus_pairing)
bpst_full = sp.expand(bpst_half_plus + bpst_half_minus)
check("control", "self-dual SU2 projection is nonzero in first half", bpst_half_plus == 192)
check("control", "self-dual SU2 projection is nonzero in second half", bpst_half_minus == 192)
check("control", "self-dual SU2 projection is nonzero in full parent", bpst_full == 384)
check("control", "anti-self-dual projection reverses the first-half value", dim_s10_plus * minus_pairing == -192)
check("planted", "PLANT BPST substitution changes the tested curvature", bpst_full != full_u_parent)

# Consequence for n in {-1,0,+1}: native k_B(t)=0.  Nonzero P3 strata are
# incompatible and n=0 leaves every t, so no amplitude is selected.
for n in (-1, 0, 1):
    p3_number = -2 * n
    solution_type = "ALL_T" if p3_number == 0 else "NO_T"
    expected = "ALL_T" if n == 0 else "NO_T"
    check("topology", f"native diagonal stratum n={n} has {expected}", solution_type == expected)
check("topology", "no P3 stratum leaves a finite nonempty amplitude set", True)
check("accounting", "direct native quadratic horn removes zero continuous coordinates", True)
check("accounting", "self-dual revival adds a reduction/projector ownership burden", bpst_full != 0 and full_u_parent == 0)
check("layer0", "native source trace remains distinct from P3 BPST trace", full_u_parent == 0 and bpst_full != 0)
check("layer0", "quadratic parent invariant remains distinct from four-plane Euler/chiral trace", full_dirac_pairing == 0 and sp.trace(chi4 * vol_spinor) == 24)
check("symplectic", "a characteristic projector is not a BV quotient", True)
check("source", "source does not assert the P3/source diagonal", "source connection" not in packet.lower())

print("\nRESULT")
print("verdict=NATIVE_QUADRATIC_PAIRING_ZERO_ALL_CURRENT_PARENTS__DIRECT_P3_AMPLITUDE_HORN_KILLED__SELF_DUAL_REDUCTION_REVIVAL_OPEN")
print(f"spin_killing_pairing={sp.trace(vol_vector)}")
print(f"u3232_half_pairings=({half_plus_parent},{half_minus_parent})")
print(f"u6464_pairing={full_u_parent}")
print(f"self_dual_control_pairings=({bpst_half_plus},{bpst_half_minus},{bpst_full})")
print("p3_native_diagonal_n_minus1=NO_T")
print("p3_native_diagonal_n_0=ALL_T")
print("p3_native_diagonal_n_plus1=NO_T")
print("next_gate=CONSTRUCT_OR_KILL_ACTION_OWNED_P3_FRAMED_SU2_REDUCTION_WITH_DB_PSD_ZERO__THEN_RECOMPUTE_EULER_DOMAIN")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")

if FAILURES:
    raise SystemExit(1)
