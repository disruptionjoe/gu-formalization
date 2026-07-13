#!/usr/bin/env python3
r"""
W67 / Path-5 Branch A -- IS THE KREIN C-OPERATOR A (KREIN-SPACE) MODULAR CONJUGATION?

CRITICAL-PATH LEG of the conjecture "the source action IS the observer" (see
explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md).  The rigorous skeleton
rests on Tomita-Takesaki (TT) modular theory of the type-III von Neumann algebra of a region,
with Bisognano-Wichmann (BW) giving modular flow = boost and the fixed surface = horizon =
FIREWALL.  The single load-bearing identification is:

    the Krein C-operator (the W49/W54 firewall grading) IS a KREIN-SPACE MODULAR CONJUGATION
    of the region's admissibility algebra.

This file tests that identification on an EXACT finite Krein-graded bipartite model (no
truncation error), and encodes the honest reachability status of the pieces that a finite toy
cannot decide.  Everything is deterministic, numpy-only, self-validating; exit 0 on success.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline -- stated explicitly)
----------------------------------------------------------------------------------
  * "The algebra":  the *-algebra M of region observables REPRESENTED ON THE KREIN SPACE
    (indefinite inner product [x,y]=<x, eta y>, eta the fundamental symmetry = the C-grading) --
    the program-native object, NOT a positive-Hilbert-subspace algebra.  Its commutant M' is the
    complementary-region (mirror-wedge) algebra.
  * "Modular conjugation":  the STANDARD PHYSICS object is the ANTILINEAR J from the polar
    decomposition S = J Delta^{1/2} of the Tomita involution, with J^2=1, J M J = M', J
    antiunitary.  The PROGRAM proposes the C-operator (a LINEAR grading, C^2=1, [C,H]=0) as this
    J.  This file's central finding is that these are DIFFERENT TYPES of object (linear vs
    antilinear); the surviving identification routes J through the ANTILINEAR CPT with the linear
    C as the *fundamental symmetry* (metric operator), not as J itself.  We do not default to
    either naive side; we determine the corrected object.

WHAT SURVIVES THE INDEFINITE METRIC (honest literature anchor)
--------------------------------------------------------------
  * Modular FLOW / BW analyticity DOES generalize to Krein spaces:
        H. Gottschalk, "Complex velocity transformations and the Bisognano-Wichmann theorem for
        quantum fields acting on Krein spaces", J. Math. Phys. 43 (2002) 4753-4769.
    (dense analytic vectors for the boost generator exist in indefinite metric => Delta^{it}=boost
     and BW analyticity carry over).  This is the FLOW half.
  * The indefinite-metric axiomatic frame (where a NON-positive vacuum functional lives):
        Morchio-Strocchi (Hilbert-space-structure-condition Wightman axioms); Strocchi, "Gauge
        theories and the physical Hilbert space"; L. Jakobczyk, "Borchers algebra formulation of
        an indefinite inner product QFT", J. Math. Phys. 25 (1984) 617.
  * PT / C-operator positivity machinery (finite / QM): Bender-Boettcher; Bender-Brody-Jones;
        Mostafazadeh (pseudo-Hermiticity); Bender-Mannheim (Pais-Uhlenbeck).  Repo anchors W49/W54.
  * What is NOT established: a full TT theorem (polar decomposition S=J Delta^{1/2} with Delta>=0,
    the KMS condition, J M J = M') for a NON-POSITIVE separating functional on a TYPE-III algebra
    in the indefinite metric.  Standard TT (Tomita 1967; Takesaki 1970) assumes a POSITIVE faithful
    normal state on a Hilbert space; that positivity is used in (i) closability + positivity of
    Delta=S*S, (ii) the polar decomposition, (iii) KMS as an equilibrium (state) condition.

THE FIVE-PERSONA TEAM (run inline; recorded in the companion .md).  The assertions below encode
persona 1's construction, persona 3's attacks (as PASS-if-the-axiom-correctly-fails criteria),
persona 4's solvable-model cross-check, and persona 5's reachability booleans.

Reproducible:  python tests/W67_path5_A_krein_modular.py     (exit 0 on success)
No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture file is touched.
Exploration-grade computation.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)  # nothing random is used; pin anyway

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ------------------------------------------------------------------------------------------------
# Finite bipartite model.  H = C^2 (region factor) (x) C^2 (mirror factor), dim 4.
#   M  = { A (x) I : A in M_2(C) }   (region algebra)
#   M' = { I (x) B : B in M_2(C) }   (mirror / commutant)  -- genuine mutual commutants (type I_2).
# Basis index = 2*i + j for |i j>, i the region qubit, j the mirror qubit.
# ------------------------------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)


def kron(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def op_M(A: np.ndarray) -> np.ndarray:      # element of the region algebra M
    return kron(A, I2)


def op_Mp(B: np.ndarray) -> np.ndarray:     # element of the commutant M'
    return kron(I2, B)


# SWAP (the geometric wedge reflection at the finite-dim level): |ij> -> |ji>.
SWAP = np.zeros((4, 4), dtype=complex)
for i in range(2):
    for j in range(2):
        SWAP[2 * j + i, 2 * i + j] = 1.0

# A random-but-fixed basis of M_2(C) to test "for all A" statements.
BASIS_2 = [np.array(m, dtype=complex) for m in (
    [[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [0, 1]],
    [[1, 1], [1, 1]], [[1, 1j], [-1j, 1]], [[2, -1], [0, 3]], [[0, 1j], [1j, 0]],
)]


def in_algebra_M(O: np.ndarray) -> bool:
    """Is O of the form A (x) I ?  (commutes with all I (x) B  <=>  O in M.)"""
    for B in BASIS_2:
        if np.max(np.abs(O @ op_Mp(B) - op_Mp(B) @ O)) > 1e-9:
            return False
    return True


def in_algebra_Mp(O: np.ndarray) -> bool:
    for A in BASIS_2:
        if np.max(np.abs(O @ op_M(A) - op_M(A) @ O)) > 1e-9:
            return False
    return True


# Cyclic & separating vector (NON-maximally entangled => nontrivial modular operator).
c0, c1 = np.sqrt(0.7), np.sqrt(0.3)
Omega = np.zeros(4, dtype=complex)
Omega[2 * 0 + 0] = c0     # |00>
Omega[2 * 1 + 1] = c1     # |11>


# Antilinear J acts as  J v = U conj(v)  with U unitary.  Induced action on operators:
#   (J O J) = U conj(O) conj(U)   (for J^2 = I).
def antilinear_apply(U: np.ndarray, v: np.ndarray) -> np.ndarray:
    return U @ np.conj(v)


def antilinear_conjugate_op(U: np.ndarray, O: np.ndarray) -> np.ndarray:
    return U @ np.conj(O) @ np.conj(U)


log("=" * 96)
log("W67 / PATH-5 BRANCH A -- IS THE KREIN C-OPERATOR A KREIN-SPACE MODULAR CONJUGATION?")
log("=" * 96)

# ================================================================================================
# T1 -- ANCHOR: standard (positive-metric) Tomita-Takesaki works on this toy.
#   J = SWAP . (complex conjugation)  is antiunitary, J^2=1, J M J = M', and the modular operator
#   Delta = rho_L (x) rho_R^{-1} is positive with J Delta J = Delta^{-1}.  Sanity that the model
#   is a faithful finite TT laboratory BEFORE we deform the metric.
# ================================================================================================
log("\n[T1] Anchor: standard Tomita-Takesaki on the positive-metric toy")
U_J = SWAP  # real, so conj(U)=U
# J^2 = 1 (antilinear):  J(Jv) = U conj(U conj(v)) = U U v = v.
jj = np.max(np.abs(antilinear_apply(U_J, antilinear_apply(U_J, Omega)) - Omega))
# J M J = M' for all A:
jmj_ok = all(in_algebra_Mp(antilinear_conjugate_op(U_J, op_M(A))) for A in BASIS_2)
# modular operator from reduced density matrices of Omega
rhoL = np.array([[c0**2, 0], [0, c1**2]], dtype=complex)
Delta = kron(rhoL, np.linalg.inv(rhoL))          # rho_L (x) rho_R^{-1}, positive
Delta_pos = np.min(np.linalg.eigvalsh((Delta + Delta.conj().T) / 2)) > 1e-9
# J Delta J = Delta^{-1}  (a defining TT identity)
JDJ = antilinear_conjugate_op(U_J, Delta)
tt_identity = np.max(np.abs(JDJ - np.linalg.inv(Delta))) < 1e-9
# modular flow sigma_t(A)=Delta^{it} A Delta^{-it} preserves M
t = 0.37
Dit = np.diag(np.diag(Delta) ** (1j * t))
flow_ok = all(in_algebra_M(Dit @ op_M(A) @ np.linalg.inv(Dit)) for A in BASIS_2)
check("T1  standard TT holds on the toy: J^2=1, J M J=M', Delta>0, J Delta J=Delta^{-1}, "
      "sigma_t(M)=M (faithful finite TT laboratory)",
      jj < 1e-12 and jmj_ok and Delta_pos and tt_identity and flow_ok,
      f"||J^2-1||={jj:.1e}, JMJ=M' {jmj_ok}, Delta>0 {Delta_pos}, JDJ=D^-1 {tt_identity}")

# ================================================================================================
# T2 -- THE TYPE MISMATCH: the C-operator is LINEAR; the modular conjugation is ANTILINEAR.
#   The Krein fundamental symmetry / C-grading eta is a LINEAR involution with eta M eta = M
#   (an AUTOMORPHISM of M), NOT a map M -> M'.  A modular conjugation must be ANTILINEAR and map
#   M -> M'.  So the literal identification "C = J" is a category error: C plays the role of the
#   fundamental symmetry (metric operator), not of J.
# ================================================================================================
log("\n[T2] Type mismatch: linear C-grading is the fundamental symmetry, not J")
D = np.diag([1.0, -1.0]).astype(complex)          # per-qubit ghost grading (+ physical, - ghost)
eta_sym = kron(D, D)                              # reflection-SYMMETRIC fundamental symmetry
C = eta_sym                                       # the C-operator = linear Krein grading
C2_ok = np.max(np.abs(C @ C - np.eye(4))) < 1e-12          # C^2 = 1
C_herm = np.max(np.abs(C - C.conj().T)) < 1e-12            # C = C^dagger (self-adjoint involution)
# C M C stays in M (automorphism), and is NOT in M' in general:
CMC = [C @ op_M(A) @ C for A in BASIS_2]
C_is_automorphism = all(in_algebra_M(O) for O in CMC)
C_maps_to_commutant = all(in_algebra_Mp(O) for O in CMC)
check("T2  the C-operator (eta) is a LINEAR involution with C M C = M (automorphism/grading), "
      "NOT C M C = M' (commutant).  A modular conjugation is ANTILINEAR and maps M->M'.  Literal "
      "'C = J' is a TYPE ERROR; C is the fundamental symmetry, not J.",
      C2_ok and C_herm and C_is_automorphism and (not C_maps_to_commutant),
      f"C^2=1 {C2_ok}, C M C in M {C_is_automorphism}, C M C in M' {C_maps_to_commutant} (must be False)")

# ================================================================================================
# T3 -- THE CORRECTED KREIN MODULAR CONJUGATION + its exact existence criterion.
#   Candidate: J_K = SWAP . conj  (the antilinear reflection; morally the CPT/wedge reflection).
#   Axioms required of a Krein-space modular conjugation:
#     (a) J_K^2 = 1;   (b) J_K M J_K = M';   (c) Krein-antiisometry [J_K x, J_K y] = conj([x,y]).
#   (a),(b) hold from the Hilbert structure.  (c) holds  IFF  the fundamental symmetry is
#   REFLECTION-INVARIANT:  U eta U^dagger = eta  i.e. [SWAP, eta] = 0.  Physically: the FIREWALL
#   GRADING must be SYMMETRIC across the modular horizon (present equally on region and mirror).
#   We verify BOTH directions:
#     - one-sided ghost grading eta_L (grading only the region factor): criterion FAILS;
#     - reflection-symmetric grading eta_sym = D (x) D: criterion HOLDS, all three axioms pass.
# ================================================================================================
log("\n[T3] Corrected Krein modular conjugation J_K = SWAP.conj and its exact existence criterion")
eta_L = kron(D, I2)   # ghost grading on the region factor only (NOT reflection-symmetric)


def krein_antiisometry_holds(U: np.ndarray, eta: np.ndarray) -> float:
    """residual of  U^dagger eta U = eta  <=>  [J_K x,J_K y] = conj([x,y]) for all x,y."""
    return float(np.max(np.abs(U.conj().T @ eta @ U - eta)))


# axioms (a),(b) -- metric-independent, from the Hilbert TT structure:
JK2 = np.max(np.abs(antilinear_apply(U_J, antilinear_apply(U_J, Omega)) - Omega))
JK_MtoMp = all(in_algebra_Mp(antilinear_conjugate_op(U_J, op_M(A))) for A in BASIS_2)
# axiom (c) -- the criterion, both regimes:
resid_onesided = krein_antiisometry_holds(U_J, eta_L)     # expect > 0  (fails)
resid_sym = krein_antiisometry_holds(U_J, eta_sym)        # expect = 0  (holds)
check("T3a  one-sided firewall grading eta_L (graded on region only) FAILS the Krein-antiisometry "
      "axiom (c): [SWAP,eta_L] != 0 => J_K is NOT a Krein modular conjugation for it",
      resid_onesided > 0.5,
      f"||SWAP^d eta_L SWAP - eta_L|| = {resid_onesided:.3f} (nonzero => axiom (c) fails)")
check("T3b  reflection-SYMMETRIC firewall grading eta_sym=D(x)D satisfies ALL THREE axioms: "
      "J_K^2=1, J_K M J_K=M', and the Krein-antiisometry [J_K x,J_K y]=conj([x,y]).  On this toy "
      "a genuine Krein modular conjugation EXISTS.",
      JK2 < 1e-12 and JK_MtoMp and resid_sym < 1e-12,
      f"J_K^2=1 {JK2 < 1e-12}, J_K M J_K=M' {JK_MtoMp}, antiisometry resid={resid_sym:.1e}")
check("T3c  EXACT CRITERION (the load-bearing structural condition, constructible now): a Krein "
      "modular conjugation for the C-graded region algebra exists IFF the firewall grading is "
      "invariant under the modular reflection, [J_reflection, C] = 0 (grading symmetric across the "
      "horizon).  This is an ADDITIONAL requirement, not automatic from C alone.",
      resid_onesided > 0.5 and resid_sym < 1e-12,
      "criterion separates the two gradings exactly")

# ================================================================================================
# T4 -- THE LOAD-BEARING OBSTRUCTION (persona 3): the cyclic vector is NOT a positive state on the
#   region algebra, so Tomita's positivity hypothesis -- used for Delta = S*S >= 0 and the polar
#   decomposition S = J Delta^{1/2} -- FAILS in the indefinite metric.  Concretely: M Omega
#   (= the whole space, Omega cyclic & separating) contains NEGATIVE Krein-norm vectors, so the
#   vacuum functional  omega(A) = [Omega, A Omega]  obeys  omega(A^+ A) = [A Omega, A Omega] < 0
#   for some A.  Standard TT (positive faithful normal state) does not apply; this is the precise
#   missing mathematics.
# ================================================================================================
log("\n[T4] Load-bearing obstruction: the vacuum is NOT a positive state (indefinite GNS form)")
# indefinite Krein form on the cyclic space: eta_sym has a negative eigenvalue
eta_eigs = np.linalg.eigvalsh(eta_sym)
indefinite = (np.min(eta_eigs) < -0.5) and (np.max(eta_eigs) > 0.5)
# exhibit an explicit A in M with [A Omega, A Omega] < 0.  A0 = [[0,1/c1],[0,0]] gives A Omega=|01>.
A0 = np.array([[0.0, 1.0 / c1], [0.0, 0.0]], dtype=complex)
v = op_M(A0) @ Omega                                   # should be |01>
is_01 = np.max(np.abs(v - np.array([0, 1, 0, 0], dtype=complex))) < 1e-12
krein_norm_v = float(np.real(v.conj().T @ eta_sym @ v))   # = -1 (negative-norm vector in M Omega)
check("T4a  the fundamental symmetry is INDEFINITE (a genuine Krein form, not a disguised Hilbert "
      "metric): eta has eigenvalues of both signs",
      indefinite, f"eig(eta) = {sorted(np.round(eta_eigs,3).tolist())}")
check("T4b  M Omega contains a NEGATIVE Krein-norm vector (A0 (x) I) Omega = |01>, "
      "[v,v] = <v,eta v> = -1 < 0  => omega(A^+ A) < 0 for some A in M  => the cyclic vector is "
      "NOT a positive state on M.  Tomita's positivity hypothesis (Delta=S*S>=0; polar "
      "decomposition S=J Delta^{1/2}; KMS as an equilibrium condition) FAILS.  THIS IS THE "
      "LOAD-BEARING GAP.",
      is_01 and krein_norm_v < -0.5,
      f"(A0(x)I)Omega=|01> {is_01}, [v,v]={krein_norm_v:.3f} < 0")

# ================================================================================================
# T5 -- WHAT SURVIVES: the modular FLOW (Delta^{it}=boost, KMS analyticity) generalizes to Krein
#   spaces (Gottschalk 2002).  The ALGEBRAIC KMS relation and sigma_t(M)=M are metric-independent
#   automorphism facts; it is only the STATE (positivity) reading of KMS that fails (T4).  Encode
#   the algebraic KMS identity for the standard modular automorphism as a positive control, and the
#   fact that the flow is an automorphism group independent of the (indefinite) metric.
# ================================================================================================
log("\n[T5] Survives: modular FLOW / KMS analyticity (Gottschalk 2002, BW on Krein spaces)")
# algebraic KMS at beta=1 in the FAITHFUL POSITIVE reference: omega0(A B)=omega0(B sigma_{-i}(A))
# with omega0(X)=<Omega,X Omega> (positive), sigma_z(A)=Delta^{iz} A Delta^{-iz}, z=-i.
omega0 = lambda X: complex(Omega.conj().T @ X @ Omega)
sig_mi = lambda A: (Delta ** 1) @ A @ np.linalg.inv(Delta ** 1)  # Delta^{i(-i)}=Delta^{1}
kms_res = 0.0
for A in BASIS_2[:4]:
    for B in BASIS_2[:4]:
        kms_res = max(kms_res, abs(omega0(op_M(A) @ op_M(B)) - omega0(op_M(B) @ sig_mi(op_M(A)))))
# the flow is an automorphism of M regardless of the metric (already flow_ok in T1):
check("T5  the modular FLOW survives the indefinite metric: sigma_t(M)=M is a metric-independent "
      "automorphism fact, and the ALGEBRAIC KMS identity omega(AB)=omega(B sigma_{-i}(A)) holds "
      "(checked on the positive reference).  BW analyticity / Delta^{it}=boost on Krein spaces is "
      "PROVEN (Gottschalk, J.Math.Phys.43(2002)4753).  Only the STATE/positivity reading fails (T4).",
      kms_res < 1e-9 and flow_ok,
      f"algebraic-KMS residual={kms_res:.1e}, sigma_t(M)=M {flow_ok}")

# ================================================================================================
# T6 -- ALGEBRA TYPE: a finite toy is TYPE I (it has a trace and minimal projections); it CANNOT
#   realize type III.  BW needs the region algebra to be TYPE III_1 (no trace, no pure states, a
#   genuine horizon).  Whether the *indefinite-metric* continuum region algebra is type III is
#   NOT settled by any finite model and is essentially open in the Krein setting.
# ================================================================================================
log("\n[T6] Algebra type: the toy is type I; type III of the indefinite region algebra is open")
# M = M_2(C) (x) I is a type I_2 factor: it has a faithful trace and a minimal projection.
tr = lambda X: complex(np.trace(X))
p_min = op_M(np.array([[1, 0], [0, 0]], dtype=complex))   # minimal projection in M
proj_ok = np.max(np.abs(p_min @ p_min - p_min)) < 1e-12
trace_faithful = abs(tr(p_min)) > 0.5                      # nonzero trace on a nonzero projection
type_I = proj_ok and trace_faithful
check("T6  the finite model is TYPE I (minimal projection + faithful trace exist) => it CANNOT be "
      "type III.  BW/firewall needs type III_1 (no trace, no minimal projection); that is a "
      "CONTINUUM property.  Type III of the indefinite-metric region algebra is NOT finite-dim "
      "reachable and is OPEN in the Krein setting.",
      type_I,
      f"minimal projection {proj_ok}, faithful trace {trace_faithful} => type I (not III)")

# ================================================================================================
# T7 -- REACHABILITY BOOLEANS (persona 5).  Assert the honest map so the file is self-documenting.
# ================================================================================================
log("\n[T7] Reachability booleans for the Krein-modular-conjugation leg")
reach = {
    # constructible NOW (this file / cited results):
    "modular_flow_generalizes_to_krein": True,        # Gottschalk 2002 (BW analyticity, boost)
    "linear_C_is_fundamental_symmetry": True,         # T2
    "krein_J_exists_on_type_I_toy_iff_grading_reflection_symmetric": True,  # T3
    "exact_existence_criterion_[Jrefl,C]=0": True,    # T3c
    # NEEDS NEW MATH (not finite-dim decidable; not in the literature as a theorem):
    "literal_C_equals_J": False,                      # T2 -- TYPE ERROR (linear vs antilinear)
    "full_polar_decomposition_S=JDelta^{1/2}_for_nonpositive_separating_functional": False,  # T4
    "KMS_as_equilibrium_state_for_indefinite_vacuum": False,  # T4
    "type_III_of_indefinite_region_algebra": False,   # T6 (OPEN)
}
# the verdict is NEEDS-NEW-MATH: the flow half is constructible, but the conjugation-to-commutant
# with a positive Delta + KMS-as-state + type III are the missing theorems.
constructible_now = [k for k, val in reach.items() if val]
missing = [k for k, val in reach.items() if not val]
check("T7  reachability = NEEDS-NEW-MATH.  Constructible now: modular flow on Krein (Gottschalk), "
      "C = fundamental symmetry, and a Krein J on the TYPE-I toy under the exact reflection-"
      "symmetry criterion.  Missing theorems: polar decomposition with a positive Delta for a "
      "NON-POSITIVE separating functional; KMS-as-equilibrium for an indefinite vacuum; type III "
      "of the indefinite region algebra.  Literal 'C=J' is FALSE (type error).",
      (reach["modular_flow_generalizes_to_krein"]
       and reach["linear_C_is_fundamental_symmetry"]
       and (reach["literal_C_equals_J"] is False)
       and (reach["full_polar_decomposition_S=JDelta^{1/2}_for_nonpositive_separating_functional"] is False)
       and (reach["type_III_of_indefinite_region_algebra"] is False)),
      f"{len(constructible_now)} constructible-now, {len(missing)} missing-theorem")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W67 Krein-modular-conjugation checks FAILED"

log("")
log("BRANCH-A (critical path) VERDICT -- this file is the computation, not a claim-status change:")
log("  * TYPE MISMATCH (T2): the C-operator is LINEAR (C^2=1, C M C=M, a grading/automorphism); a")
log("    modular conjugation is ANTILINEAR and maps M->M'.  Literal 'C = J' is a category error.")
log("    The surviving object: C is the FUNDAMENTAL SYMMETRY (metric operator eta); the modular")
log("    conjugation is the ANTILINEAR CPT-type reflection J_K = SWAP.conj (morally C composed with")
log("    an antilinear PT).")
log("  * CONSTRUCTIBLE NOW (T3): on a TYPE-I toy, a genuine Krein modular conjugation J_K exists,")
log("    with J_K^2=1, J_K M J_K=M', and Krein-antiisometry -- IFF the firewall grading is invariant")
log("    under the modular reflection, [J_reflection, C]=0 (grading symmetric across the horizon).")
log("    This is a clean, checkable, ADDITIONAL structural criterion (not automatic from C).")
log("  * LOAD-BEARING GAP (T4): in the indefinite metric the cyclic vector is NOT a positive state")
log("    (M Omega carries negative Krein-norm vectors), so Tomita's positivity hypothesis -- the")
log("    engine of Delta=S*S>=0, the polar decomposition S=J Delta^{1/2}, and KMS-as-equilibrium --")
log("    FAILS.  A full Tomita-Takesaki theorem for a NON-POSITIVE separating functional on a")
log("    type-III algebra in a Krein space DOES NOT EXIST in the literature; this is the missing")
log("    mathematics.  What DOES survive is the modular FLOW / BW analyticity (Gottschalk 2002).")
log("  * ALGEBRA TYPE (T6): the toy is type I; type III_1 (the BW/firewall requirement) is a")
log("    continuum property and is OPEN for the indefinite-metric region algebra.")
log("  * REACHABILITY (T7): NEEDS-NEW-MATH.  The critical path is NOT cleanly blocked (the flow half")
log("    is real and the conjugation exists on a toy under an exact criterion) and NOT constructible")
log("    now as a whole (polar decomposition + KMS-as-state + type III are missing).  The conjecture")
log("    stands or falls on developing Krein Tomita-Takesaki for non-positive states + type III.")
log("This file settles nothing about GU claim status; it is a graded, reproducible computation.")
raise SystemExit(0)
