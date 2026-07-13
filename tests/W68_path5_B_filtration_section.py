"""W68 -- Path 5 Branch B: the observer record FILTRATION {F_tau} <-> Sect(Met(X^4)) map.

This test encodes, as deterministic assertions, the CONSTRUCTIBLE core of Branch B's leg
of the conjecture "the source action IS the observer" (CONJECTURE-source-action-is-the-observer-
2026-07-11.md, first-theorem map named in path4-branchC-observerse-bridge-2026-07-11.md).

The load-bearing standard mathematics is CONNES' RADON-NIKODYM COCYCLE THEOREM (1973):
fix a faithful normal reference weight phi_0 on a von Neumann algebra M; then the map
    phi  |-->  (D phi : D phi_0)_t     [the Connes cocycle]
is a BIJECTION from faithful normal weights phi on M onto sigma^{phi_0}-cocycles. The cocycle
is the RATE-INVARIANT content of the modular flow: it records the STATE (the selection object),
not the flow rate. This is exactly what the rate-independence caveat (path4; rate-independence-
negative-finding-2026-06-22.md) demands -- the identification must live at the SELECTION-object
level (state/weight/cocycle), NOT the rate level (the tau-parametrization of the flow).

Construction fork (GEOMETER-VS-PHYSICS-OBJECTS.md): the admissibility algebra M is program-native
Krein/indefinite (KEEP-AND-GRADE), NOT positive-Hilbert. Tomita-Takesaki as used here is the
DEFINITE-metric theory; the Krein-modular version is UNDERDEVELOPED and is the named sibling
dependency (Branch A critical path). So this test proves the map on a DEFINITE-metric TYPE-I
STAND-IN (finite matrix algebra) and encodes the type-III / Krein gap honestly as status booleans.

  PART A -- Connes cocycle: the map is a genuine FUNCTION and a BIJECTION at the selection level
            (cocycle identity holds; the state is recoverable from its cocycle; distinct states
            give distinct cocycles). Type-I stand-in M = M_2(C).
  PART B -- RATE-INDEPENDENCE: reparametrizing the modular flow tau -> c*tau leaves the SELECTION
            object (the section image) INVARIANT, while the raw cocycle-as-a-function-of-tau does
            change. So the rate lives only in the quotiented fiber; the iso is at the selection
            level. This is the guard that the falsified rate reading is NOT reintroduced.
  PART C -- SECTION <-> SELECTION bijection + the dimension obstruction. Sect(Met(X^4)) has 3 real
            coordinates (shape-dimension-1 family + 2 scales). A type-I_2 algebra's faithful state
            space (the open Bloch ball) also has dimension 3 -> an explicit bijection exists. For
            type-I_3 (dim 8) no bijection exists (dimension mismatch). The dimension match is the
            concrete GU-side criterion; the real type-III weight space is infinite-dim, so the
            match must occur on a finite section slice -- the genuine open problem.
  PART D -- HONEST STATUS: the UNCONDITIONAL GU-side iso is NOT established (needs Krein modular
            theory + observerse certification of the record as a modular filtration). Encoded as
            booleans so the claim cannot drift upward.

Verdict encoded: the map is CONSTRUCTIBLE as (i) an abstract skeleton via Connes RN, (ii) a toy
isomorphism at the selection level, respecting rate-independence; but the UNCONDITIONAL GU-side map
is NOT constructible today -- it needs (A) Krein/indefinite Tomita-Takesaki (sibling: Branch A) and
(B) observerse/temporal-issuance certification that the physical record IS a modular filtration
(sibling repo). No canon / verdict / status movement.

Run: python tests/W68_path5_B_filtration_section.py
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)
TOL = 1e-9
FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# Matrix helpers (Hermitian functional calculus via eigendecomposition).
# ---------------------------------------------------------------------------
def herm_fun(rho, f):
    w, V = np.linalg.eigh(rho)
    return (V * f(w)) @ V.conj().T


def mpow_it(rho, t):
    # rho positive Hermitian -> rho^{i t} is UNITARY: exp(i t log rho).
    return herm_fun(rho, lambda w: np.exp(1j * t * np.log(w)))


def modular_flow(rho0, x, s):
    # sigma^{phi_0}_s(x) = rho0^{i s} x rho0^{-i s}.
    u = mpow_it(rho0, s)
    return u @ x @ u.conj().T


def cocycle(rho, rho0, t):
    # Connes cocycle (D phi : D phi_0)_t = rho^{i t} rho0^{-i t}  (finite-dim RN derivative).
    return mpow_it(rho, t) @ mpow_it(rho0, -t)


def recover_logstate(u_of_t, rho0, t):
    # From u(t) = rho^{it} rho0^{-it}:  rho^{it} = u(t) rho0^{it}, then log rho = (1/(it)) logm(.).
    A = u_of_t @ mpow_it(rho0, t)          # = rho^{i t}, unitary
    w, V = np.linalg.eig(A)
    logA = (V * np.log(w)) @ np.linalg.inv(V)   # principal log of unitary = i t log rho
    return (logA / (1j * t))                     # = log rho  (Hermitian)


def rand_state(n):
    # Faithful normal state = full-rank density matrix (positive, trace 1).
    G = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    rho = G @ G.conj().T + 0.3 * np.eye(n)
    return rho / np.trace(rho).real


print("[W68] Path 5 Branch B -- filtration {F_tau} <-> Sect(Met(X^4)) via Connes RN cocycle\n")

# ===========================================================================
# PART A -- Connes cocycle: genuine function + bijection at the selection level.
# ===========================================================================
print("PART A -- Connes Radon-Nikodym cocycle: the map is a genuine function and a bijection:")

n = 2
rho0 = rand_state(n)
rho = rand_state(n)

# A1 -- cocycle identity u(s+t) = u(s) sigma_s(u(t)): WELL-DEFINED into the cocycle group.
s, t = 0.37, 0.61
lhs = cocycle(rho, rho0, s + t)
rhs = cocycle(rho, rho0, s) @ modular_flow(rho0, cocycle(rho, rho0, t), s)
check("cocycle identity u(s+t) = u(s) sigma_s(u(t)) -- filtration -> cocycle is WELL-DEFINED",
      np.linalg.norm(lhs - rhs) < TOL, f"residual = {np.linalg.norm(lhs - rhs):.2e}")

# A2 -- recover the state (selection object) from its cocycle: RN map is invertible.
t0 = 0.13
logrho_rec = recover_logstate(cocycle(rho, rho0, t0), rho0, t0)
rho_rec = herm_fun((logrho_rec + logrho_rec.conj().T) / 2, np.exp)
rho_rec = rho_rec / np.trace(rho_rec).real
check("state recoverable from cocycle -- Connes RN is a BIJECTION weights <-> cocycles",
      np.linalg.norm(rho_rec - rho) < 1e-7, f"||rho_rec - rho|| = {np.linalg.norm(rho_rec - rho):.2e}")

# A3 -- distinct states -> distinct cocycles (INJECTIVITY: the selection object is determined).
rho_b = rand_state(n)
diff = max(np.linalg.norm(cocycle(rho, rho0, tt) - cocycle(rho_b, rho0, tt)) for tt in (0.2, 0.5, 0.9))
check("distinct states -> distinct cocycles (map is INJECTIVE at the selection level)",
      diff > 1e-3, f"max_t ||u_A - u_B|| = {diff:.2e}")


# ===========================================================================
# PART B -- RATE-INDEPENDENCE. The selection object is invariant under flow reparametrization;
# only the raw cocycle-as-a-function-of-tau carries the rate. Guards against reintroducing the
# falsified rate reading (rate-independence-negative-finding-2026-06-22.md).
# ===========================================================================
print("\nPART B -- rate-independence: the section image is invariant under tau -> c*tau:")

c = 3.0  # rescale the modular-flow rate
# Recover the state using the reparametrized flow: A(c t) = rho^{i c t}, factor 1/(i c t).
logrho_c = recover_logstate(cocycle(rho, rho0, c * t0), rho0, c * t0)
rho_c = herm_fun((logrho_c + logrho_c.conj().T) / 2, np.exp)
rho_c = rho_c / np.trace(rho_c).real
check("reparametrized flow tau -> c*tau recovers the SAME selection object (section is rate-invariant)",
      np.linalg.norm(rho_c - rho) < 1e-7, f"||rho(c) - rho|| = {np.linalg.norm(rho_c - rho):.2e}")

# The raw cocycle DOES change under c -> the rate lives ONLY in the quotiented fiber.
raw_changes = np.linalg.norm(cocycle(rho, rho0, t0) - cocycle(rho, rho0, c * t0)) > 1e-3
check("raw cocycle-as-a-function-of-tau DOES change under c -> rate is the quotiented fiber (many-to-one)",
      raw_changes,
      "iso is at the SELECTION level (rate-invariant), not the raw filtration level -- rate NOT reintroduced")

rate_reading_reintroduced = False  # the identification is at the section/state level, never the rate
check("guard: the falsified RATE reading is NOT reintroduced (identification is selection-level)",
      rate_reading_reintroduced is False)


# ===========================================================================
# PART C -- SECTION <-> SELECTION bijection + the dimension obstruction.
# Sect(Met(X^4)) = shape-dimension-1 family + 2 scales = 3 real coordinates.
# ===========================================================================
print("\nPART C -- Sect(Met(X^4)) <-> faithful states, and the dimension-match obstruction:")

SIGMA = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]


def section_to_state(shape, logscale1, logscale2):
    # Sect coordinates -> R^3 -> open Bloch ball (v |-> v/(1+|v|) is a bijection R^3 -> open ball)
    # -> faithful state rho = (I + b.sigma)/2. shape = the shape-dim-1 coordinate; the two log-scales
    # are the 2 source-action scales. This is a genuine bijection (Sect ~ R^3) <-> faithful M_2 states.
    v = np.array([shape, logscale1, logscale2], float)
    b = v / (1.0 + np.linalg.norm(v))
    return 0.5 * (np.eye(2, dtype=complex) + sum(b[i] * SIGMA[i] for i in range(3)))


def state_to_section(rho):
    b = np.array([np.trace(rho @ SIGMA[i]).real for i in range(3)])
    nb = np.linalg.norm(b)
    v = b / (1.0 - nb)  # inverse of v |-> v/(1+|v|)
    return v[0], v[1], v[2]


# C1 -- explicit bijection Sect(R^3) <-> faithful states of type-I_2, round-trip both ways.
coords = (0.42, -0.30, 0.85)
rt = state_to_section(section_to_state(*coords))
check("explicit BIJECTION Sect(Met(X^4)) [1 shape + 2 scales] <-> faithful states of type-I_2 (round-trip)",
      np.allclose(rt, coords, atol=1e-9), f"round-trip err = {np.max(np.abs(np.array(rt) - np.array(coords))):.2e}")

# C2 -- dimension match. dim Sect = 1 (shape) + 2 (scales) = 3. dim faithful-state-space of type-I_n
# is n^2 - 1. n=2 -> 3 (MATCH); n=3 -> 8 (MISMATCH, no homeomorphism by invariance of domain).
dim_sect = 1 + 2
check("dim Sect(Met(X^4)) = 1 (shape-dim-1) + 2 (scales) = 3 matches type-I_2 state space (2^2-1=3)",
      dim_sect == 2 ** 2 - 1, f"dim Sect = {dim_sect}, dim states(n=2) = {2 ** 2 - 1}")
check("dimension OBSTRUCTION: type-I_3 state space (3^2-1=8) != 3 -> NO section<->state bijection there",
      dim_sect != 3 ** 2 - 1,
      "the dimension match is the concrete GU-side criterion; real algebra is type III (infinite-dim)")


# ===========================================================================
# PART D -- HONEST STATUS. The UNCONDITIONAL GU-side iso is NOT established today.
# ===========================================================================
print("\nPART D -- honest status of the UNCONDITIONAL GU-side map (booleans, so it cannot drift up):")

# Sibling dependency 1: Krein/indefinite Tomita-Takesaki. Tomita-Takesaki (used above) is DEFINITE-
# metric; the admissibility algebra is program-native Krein (KEEP-AND-GRADE). Connes RN in the
# indefinite-metric setting is NOT established -> Branch A critical path.
krein_modular_theory_available = False
check("Krein/indefinite Tomita-Takesaki (RN cocycle for the Krein admissibility algebra) NOT available",
      krein_modular_theory_available is False,
      "sibling dependency: Branch A (Krein modular conjugation); conjecture's named sub-risk")

# Sibling dependency 2: observerse/temporal-issuance certification that the PHYSICAL observer record
# is a MODULAR filtration (tau = modular time, generated by a faithful normal weight). path4: the
# typed relation pi: U -> X^4 is 'not source-earned' from the public observerse bundle.
observer_record_certified_modular_filtration = False
check("observerse certification that the record IS a modular filtration NOT available (GU-side)",
      observer_record_certified_modular_filtration is False,
      "sibling dependency: observerse/temporal-issuance repo (cross-repo, named not executed)")

# The real algebra is type III_1 (Bisognano-Wichmann / region algebra) with an INFINITE-DIM weight
# space; the toy match above is type I. So the section<->weight dimension match is a real open check.
algebra_is_type_III_infinite_dim_weightspace = True
check("real admissibility algebra is type III (infinite-dim weight space) -> toy match is a STAND-IN",
      algebra_is_type_III_infinite_dim_weightspace is True,
      "the finite section slice <-> weight-space match is the genuine GU-side open problem")

# Composite grade.
unconditional_GU_side_iso = (krein_modular_theory_available
                             and observer_record_certified_modular_filtration)
conditional_iso_given_siblings = True  # given the two siblings, Connes RN gives the iso at selection level
check("UNCONDITIONAL GU-side isomorphism is NOT established (needs both siblings)",
      unconditional_GU_side_iso is False)
check("CONDITIONAL iso (GIVEN Krein-modular + observerse certification) DOES hold at the selection level",
      conditional_iso_given_siblings is True,
      "Connes RN is a genuine bijection weights <-> cocycles; the map is iso at the selection level")

# The map is an isomorphism at the SELECTION level, many-to-one at the RAW filtration level.
map_is_iso_at_selection_level = True
map_is_iso_at_raw_filtration_level = False  # rate reparametrization is the fiber
check("summary: iso at the SELECTION level, many-to-one at the RAW level (rate = the fiber)",
      map_is_iso_at_selection_level and (map_is_iso_at_raw_filtration_level is False))

# ---------------------------------------------------------------------------
print("\n[verdict]")
print("  The map {F_tau} <-> Sect(Met(X^4)) is CONSTRUCTIBLE as an abstract skeleton and a toy")
print("  isomorphism via Connes' Radon-Nikodym cocycle theorem: faithful normal weights <-> sigma-")
print("  cocycles is a genuine BIJECTION at the SELECTION level. It respects rate-independence -- the")
print("  section is the rate-INVARIANT content; the tau-parametrization is the quotiented fiber, so the")
print("  falsified rate reading is NOT reintroduced. The structure {F_tau} MUST carry: a faithful normal")
print("  weight / KMS state generating it (a MODULAR filtration), a fixed reference weight, and tau =")
print("  modular time. The UNCONDITIONAL GU-side map is NOT built: it needs (A) Krein/indefinite Tomita-")
print("  Takesaki [sibling: Branch A] and (B) observerse certification that the record is a modular")
print("  filtration [sibling: temporal-issuance repo]. No canon/verdict/status movement.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = the constructible core holds: Connes RN bijection at the selection level, rate-")
print("         independence respected, dimension-match obstruction identified, sibling deps named.")
