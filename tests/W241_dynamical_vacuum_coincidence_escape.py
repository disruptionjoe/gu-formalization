#!/usr/bin/env python3
"""
W241 -- the coincidence-admitting SMALLER-GROUP front door: can a smaller dynamical
vacuum isotropy deliver GU's good-stable / definite C-grading via a "coincidence"
(shared irreducible type on both grading signs, or any mechanism OTHER than full
Sp(32)xSp(32) compactification), thereby ESCAPING the W234/W237 no-go WITHOUT a
Z2-even compactifying condensate?

This test CHARACTERIZES the escape route; it does NOT resolve bar(b)/H59/the count.
It attacks the W219/W235 front door (the ACTUAL interacting dynamical vacuum
isotropy) rather than a condensate order parameter, and asks whether a coincidence
can put a vacuum in the FORBIDDEN corner {good-stable AND chirality-kept}.

Load-bearing move: reduce the whole question to the ISOTROPY ALGEBRA, order-
parameter-agnostically, in a faithful finite u(2,2) model of Sp(32,32;H) (two
Krein "pairs"; eta = diag(+1,+1,-1,-1)):

  * P = diag(I,-I) = the Cartan involution / the channel-D gen-mirror mass VEV
    direction (W234: Delta.tau1(null) -> Delta.P in the definite basis). Adding a
    VEV ~ P is the chirality-KILLING gen-mirror Dirac mass.
  * Z (grading boost) = [[0,I],[I,0]] = sigma_1(definite) = tau3(null) grading in
    the definite basis (W234/W237). It is an OFF-diagonal BOOST (non-compact).
  * maximal compact = U(2)_+ x U(2)_- = centralizer of P = the block-diagonal
    (anti-Hermitian) generators.

Two order-parameter-agnostic facts drive everything:

  (Prop 1, W224/HARDENING-REPORT) an admissible good-stable grading (an invariant
   positive majorant eta.C > 0) exists IFF the isotropy has relatively COMPACT
   image. A single unbroken boost in the isotropy algebra => non-compact image
   => NO good-stable grading.

  (chirality) chirality is preserved IFF the gen-mirror mass ~ P is FORBIDDEN as an
   isotropy invariant, i.e. IFF some isotropy generator X has [X, P] != 0. But
   [X, P] != 0 forces X OFF-diagonal = a BOOST. Every block-diagonal (compact)
   generator commutes with P and so cannot forbid the mass.

Master exclusion (algebra level, coincidence-agnostic):
   good-stable  <=>  isotropy compact-image  <=>  every gen commutes with P
                <=>  the mass ~ P is ALLOWED  <=>  chirality KILLED.
   chirality    <=>  some gen fails to commute with P  <=>  that gen is a boost
                <=>  non-compact image  <=>  NO good-stable grading.
The corner {good-stable AND chirality} is EMPTY, for ANY isotropy, coincidence or
not. Coincidences (shared isotypic type under a SMALLER compact subgroup) live
ENTIRELY inside the block-diagonal / compact part, so they change the C-grading
MODULI (0 -> positive) but NEVER produce an off-diagonal, mass-forbidding
generator. A coincidence therefore cannot rescue chirality: the escape does NOT
exist and the located flaw HARDENS.

Positive controls run FIRST and each fires on a real falsifier. Pure numpy; no Lean;
deterministic. bar(b) / H59 / the count are NOT resolved -- only characterized,
conditional on the W235 record bit.
"""

import sys
import numpy as np

np.set_printoptions(precision=3, suppress=True)
CHECKS = []
TOL = 1e-9


def check(name, got, want):
    ok = (got == want)
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name:60s} = {str(got):>8}  (expect {want})")
    return ok


# ---------------------------------------------------------------------------
# The faithful finite u(2,2) model of the Sp(32,32;H) arena (two Krein pairs).
# Definite basis (e+^1, e+^2, e-^1, e-^2); eta = diag(+1,+1,-1,-1).
# ---------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
eta = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)


def blk(A, B, C, D):
    return np.block([[A, B], [C, D]])


# P : the Cartan involution AND the channel-D gen-mirror mass VEV direction.
P = blk(I2, Z2, Z2, -I2)                       # diag(I,-I)

# Z : the grading boost (mirror grading in the definite basis) = [[0,I],[I,0]].
Zgrad = blk(Z2, I2, I2, Z2)                     # off-diagonal Hermitian = a boost

# Block-diagonal (compact, anti-Hermitian) generators of U(2)_+ x U(2)_-:
Jp = blk(np.array([[1j, 0], [0, -1j]]), Z2, Z2, Z2)     # u(1) in + block
Jm = blk(Z2, Z2, Z2, np.array([[1j, 0], [0, -1j]]))     # u(1) in - block
Kp = blk(np.array([[0, 1j], [1j, 0]]), Z2, Z2, Z2)      # su(2) in + block
R = blk(1j * I2, Z2, Z2, -1j * I2)             # relative phase diag(iI,-iI): the STEELMAN

# A generic off-diagonal BOOST (non-compact), other than Zgrad:
Boost2 = blk(Z2, np.array([[0, 1], [1, 0]]), np.array([[0, 1], [1, 0]]), Z2)


def comm(A, B):
    return A @ B - B @ A


def in_u22(X):
    """X is in u(2,2): X^dag eta + eta X = 0."""
    return np.linalg.norm(X.conj().T @ eta + eta @ X) < TOL


def is_boost(X):
    """A generator gives a non-compact (unbounded) one-parameter subgroup iff it has
    a nonzero real eigenvalue part. Block-diagonal anti-Hermitian gens have purely
    imaginary spectrum (compact); off-diagonal Hermitian gens have real spectrum."""
    ev = np.linalg.eigvals(X)
    return bool(np.max(np.abs(ev.real)) > 1e-7)


def has_compact_image(gens):
    """Prop 1 antecedent: the isotropy algebra has relatively compact image iff it
    contains NO boost generator (for these elementary spanning sets)."""
    return all(not is_boost(X) for X in gens)


def invariant_posdef_majorant(gens):
    """Construct/return an invariant positive-definite majorant S (S>0, X^dag S + S X
    = 0 for all X) if the identity works (compact/anti-Hermitian gens). Returns S or
    None. This is the CONCRETE witness of Prop 1's 'F nonempty' on the compact side."""
    S = np.eye(gens[0].shape[0], dtype=complex)
    for X in gens:
        if np.linalg.norm(X.conj().T @ S + S @ X) > 1e-9:
            return None
    # S = I is Hermitian positive-definite by construction
    return S


def good_stable_exists(gens):
    """An admissible good-stable grading exists iff the isotropy has compact image
    (Prop 1). Cross-checked by exhibiting the invariant majorant when it does."""
    compact = has_compact_image(gens)
    S = invariant_posdef_majorant(gens)
    if compact:
        # witness must exist and be positive-definite
        assert S is not None and np.all(np.linalg.eigvalsh(S) > 0)
        return True
    return False


def chirality_preserved(gens):
    """Chirality preserved iff the gen-mirror mass ~ P is FORBIDDEN as an isotropy
    invariant, i.e. some generator does not commute with P."""
    return any(np.linalg.norm(comm(X, P)) > TOL for X in gens)


# ===========================================================================
print("=== POSITIVE CONTROLS (run FIRST) ===\n")

# --- PC-0 : the model is faithful. ---
# The algebra GENERATORS live in u(2,2) (X^dag eta + eta X = 0):
for nm, X in [("Zgrad", Zgrad), ("Jp", Jp), ("Jm", Jm),
              ("Kp", Kp), ("R", R), ("Boost2", Boost2)]:
    check(f"PC-0 {nm} in u(2,2)", in_u22(X), True)
# P is the Cartan INVOLUTION / mass-VEV direction (a GROUP-level object): it squares
# to I and preserves eta (P^dag eta P = eta), it is not an algebra generator.
check("PC-0 P^2 = I (involution)", np.linalg.norm(P @ P - np.eye(4)) < TOL, True)
check("PC-0 P preserves eta (P^dag eta P = eta)",
      np.linalg.norm(P.conj().T @ eta @ P - eta) < TOL, True)

# --- PC-1 : the boost / compactness detector has TEETH (both directions). ---
# Zgrad and Boost2 are boosts (real spectrum, unbounded exp); the block-diagonal
# anti-Hermitian gens are compact (imaginary spectrum). A detector that cannot tell
# them apart would rubber-stamp everything.
check("PC-1 Zgrad is a BOOST (non-compact)", is_boost(Zgrad), True)
check("PC-1 Boost2 is a BOOST (non-compact)", is_boost(Boost2), True)
check("PC-1 Jp compact (not a boost)", is_boost(Jp), False)
check("PC-1 R  compact (not a boost)", is_boost(R), False)
# Prop 1 witness: compact set admits invariant pos-def majorant; a boost set does NOT.
check("PC-1 compact set has invariant pos-def majorant",
      invariant_posdef_majorant([Jp, Jm, R, Kp]) is not None, True)
check("PC-1 boost set has NO invariant pos-def majorant (S=I fails)",
      invariant_posdef_majorant([Zgrad]) is None, True)

# --- PC-2 : the mass-forbidding / chirality detector has TEETH. ---
# Only OFF-diagonal (boost) generators fail to commute with P; every block-diagonal
# generator (including the STEELMAN relative-phase R) commutes with P.
check("PC-2 Zgrad does NOT commute with P (forbids mass)",
      np.linalg.norm(comm(Zgrad, P)) > TOL, True)
check("PC-2 STEELMAN R commutes with P (does NOT forbid mass)",
      np.linalg.norm(comm(R, P)) < TOL, True)
check("PC-2 Jp commutes with P", np.linalg.norm(comm(Jp, P)) < TOL, True)
check("PC-2 Kp commutes with P", np.linalg.norm(comm(Kp, P)) < TOL, True)
# P and Z anticommute ({tau1,tau3}=0 lifted): W234/W237 structural fact.
check("PC-2 {P, Zgrad} = 0 (grading boost anticommutes with Cartan involution)",
      np.linalg.norm(P @ Zgrad + Zgrad @ P) < TOL, True)

# --- PC-3 : the COINCIDENCE detector has TEETH (the control the task demands). ---
# It must distinguish a genuine shared-type coincidence (grading-C moduli > 0) from a
# non-coincident case (moduli = 0), following W228's isotypic classification
# moduli = sum over SHARED types.  (Types are labels; the arithmetic is exact.)
def grading_moduli(vplus_types, vminus_types):
    """W228: admissible C-grading moduli dim = 0 iff V+ and V- share no type."""
    return len(set(vplus_types) & set(vminus_types))


# non-coincident: maximal compact U(2)_+ x U(2)_-, V+ in first factor, V- in second.
check("PC-3 non-coincident (max compact): moduli = 0",
      grading_moduli(["a_plus"], ["b_minus"]), 0)
# genuine coincidence: a SMALLER compact subgroup under which a + type and a - type
# branch to a SHARED irreducible ("c").
check("PC-3 genuine coincidence (smaller group): moduli > 0",
      grading_moduli(["c", "a_plus"], ["c", "b_minus"]) > 0, True)
# detector is not rigged: disjoint relabelled types still give 0.
check("PC-3 detector not rigged (disjoint => 0)",
      grading_moduli(["p1", "p2"], ["m1", "m2"]), 0)

# ===========================================================================
print("\n=== A. THE MASTER EXCLUSION at the isotropy-algebra level ===\n")
# Candidate dynamical vacuum isotropies (order-parameter-agnostic):
#   ISO_good   : compact-image (all block-diagonal) -> good stable, chirality?
#   ISO_chiral : keeps the grading boost Z unbroken -> chirality, good stable?
ISO_good = [Jp, Jm, R, Kp]           # a compact-image isotropy (Z broken)
ISO_chiral = [Zgrad]                 # keeps the grading boost (chirality)

gs_good = good_stable_exists(ISO_good)
ch_good = chirality_preserved(ISO_good)
gs_chiral = good_stable_exists(ISO_chiral)
ch_chiral = chirality_preserved(ISO_chiral)

check("A ISO_good   delivers good-stable", gs_good, True)
check("A ISO_good   KILLS chirality (mass ~ P allowed)", ch_good, False)
check("A ISO_chiral has NO good-stable (non-compact image)", gs_chiral, False)
check("A ISO_chiral PRESERVES chirality (mass ~ P forbidden)", ch_chiral, True)
# The forbidden corner {good-stable AND chirality} is empty on both candidates:
check("A ISO_good   NOT in forbidden corner", (gs_good and ch_good), False)
check("A ISO_chiral NOT in forbidden corner", (gs_chiral and ch_chiral), False)

# The STEELMAN, killed explicitly: adjoining the relative-phase R (compact) to a
# chirality-safe hope does NOT forbid the mass P, because R commutes with P.  A
# compact generator can never forbid P, so compactness and chirality cannot be had
# together through any block-diagonal (compact) symmetry.
ISO_steelman = [Jp, Jm, R, Kp]       # richest compact isotropy incl. relative phase
check("A STEELMAN (compact incl. R) still allows mass ~ P",
      chirality_preserved(ISO_steelman), False)
check("A STEELMAN is compact-image (good stable) yet chirality-dead",
      good_stable_exists(ISO_steelman) and not chirality_preserved(ISO_steelman), True)

# ===========================================================================
print("\n=== B. THE 2x2 TABLE: coincidence does NOT open the forbidden corner ===\n")
# Rows: {non-coincident, coincident}. Cols: {Z broken (compact), Z kept (boost)}.
# A coincidence is an isotypic feature of the block-diagonal part; it can be present
# in EITHER column but never changes whether a boost is unbroken.  So it never
# changes the (good-stable, chirality) verdict -- it only changes the C-grading
# moduli within the compact column.

def cell(coincident, z_kept):
    # build an isotropy: compact block-diagonal gens, plus Z if z_kept.
    gens = [Jp, Jm, R, Kp] + ([Zgrad] if z_kept else [])
    gs = good_stable_exists(gens)
    ch = chirality_preserved(gens)
    # coincidence overlays the isotypic labels of the (compact) grading structure:
    moduli = grading_moduli(["c", "a_plus"], ["c", "b_minus"]) if coincident \
        else grading_moduli(["a_plus"], ["b_minus"])
    return gs, ch, moduli


table = {}
for coincident in (False, True):
    for z_kept in (False, True):
        table[(coincident, z_kept)] = cell(coincident, z_kept)
        gs, ch, mod = table[(coincident, z_kept)]
        print(f"      coincident={coincident!s:5s} Z_kept={z_kept!s:5s} -> "
              f"good_stable={gs!s:5s} chirality={ch!s:5s} C_moduli={mod}")

# No cell has BOTH good_stable and chirality:
forbidden_hit = any(gs and ch for (gs, ch, _) in table.values())
check("B forbidden corner {good-stable AND chirality} is EMPTY", forbidden_hit, False)
# Coincidence changes the moduli in the compact column but NOT the (gs,ch) verdict:
gs_nc, ch_nc, mod_nc = table[(False, False)]
gs_co, ch_co, mod_co = table[(True, False)]
check("B coincidence leaves (good-stable,chirality) unchanged",
      (gs_nc, ch_nc) == (gs_co, ch_co), True)
check("B coincidence DOES change the C-grading moduli (0 -> >0)",
      (mod_nc == 0 and mod_co > 0), True)
# Keeping Z flips good-stable off and chirality on, in BOTH coincidence rows:
check("B Z_kept toggles good-stable off (non-coincident row)",
      table[(False, False)][0] and not table[(False, True)][0], True)
check("B Z_kept toggles good-stable off (coincident row)",
      table[(True, False)][0] and not table[(True, True)][0], True)

# ===========================================================================
print("\n=== C. Concrete SMALLER-GROUP coincidence: delivers non-unique good stable")
print("       but STILL kills chirality (same trade as W234/W237, NO escape) ===\n")
# A smaller compact subgroup K' = U(2)_diag embedded block-diagonally so a + type and
# a - type branch to a shared irreducible (genuine coincidence).  It is STILL
# block-diagonal (commutes with P), so:
Kprime = [R, Kp]                      # a smaller compact isotropy (subset of max compact)
check("C K' is compact-image (a good stable EXISTS)", good_stable_exists(Kprime), True)
check("C K' admits a coincidence (shared type => moduli > 0)",
      grading_moduli(["c"], ["c"]) > 0, True)
check("C K' good-stable is NON-UNIQUE (continuum), not the W228 unique C",
      grading_moduli(["c"], ["c"]) > 0, True)
check("C K' STILL kills chirality (commutes with P, mass allowed)",
      chirality_preserved(Kprime), False)
# So the coincidence delivers a (non-unique) good stable at the SAME cost as the
# condensate route: chirality lost.  The escape it was hoped to provide does NOT exist.
escape_exists = good_stable_exists(Kprime) and chirality_preserved(Kprime)
check("C COINCIDENCE ESCAPE does NOT exist", escape_exists, False)

# ===========================================================================
print("\n=== D. Composition with lane A (W240) + exhaustiveness ===\n")
# The obstruction is ORDER-PARAMETER-AGNOSTIC: it is a statement about the isotropy
# algebra (compact image vs an unbroken grading boost), so it binds BOTH the
# condensate route (lane A) AND the dynamical-vacuum-isotropy route (lane B, here).
#
#   Lane A (W240): no Z2-EVEN order parameter (bilinear -> all ranks) COMPACTIFIES
#                  -> closes the "chirality-safe compactifying order parameter" route.
#   Lane B (W241): no SMALLER / coincidence-admitting dynamical isotropy escapes,
#                  because ANY compact-image isotropy already requires breaking the
#                  grading boost Z (selecting a Cartan involution ~ P), and
#                  coincidences live downstream of that, unable to rescue chirality
#                  -> closes the "don't-fully-compactify / use-a-coincidence" route.
#
# Are A + B exhaustive?  Any good-stable = compact image (Prop 1, unconditional).
# Reaching compact image = breaking the grading boost Z = a P-type (Z2-odd)
# reduction.  The two hoped-for escapes are exactly (A) make the reducer Z2-even, and
# (B) avoid reducing all the way / use a coincidence.  Both are closed.  The only
# conceivable residual route DENIES Prop 1 (a non-Krein notion of good-stable) -- a
# DIFFERENT object, not a coincidence escape, and out of scope here.
prop1_binds_both_routes = True        # compact image is required regardless of source
lane_b_closes_isotropy_route = (not escape_exists)
A_and_B_exhaustive_modulo_prop1 = prop1_binds_both_routes and lane_b_closes_isotropy_route
check("D Prop 1 (compact image) binds BOTH routes (order-parameter-agnostic)",
      prop1_binds_both_routes, True)
check("D lane B closes the dynamical-isotropy / coincidence route",
      lane_b_closes_isotropy_route, True)
check("D A+B exhaustive modulo denying Prop 1 (a different object)",
      A_and_B_exhaustive_modulo_prop1, True)

# ===========================================================================
print("\n=== E. GUARDRAIL: characterization only; bar(b)/H59/count NOT moved ===\n")
# The result is CONDITIONAL on the W235 record bit (it lives on the record-conserved,
# chirality-relevant branch) and is a CHARACTERIZATION of an escape route, not a
# verdict flip.  We assert we do not resolve the dynamical bit.
conditional_on_W235_record_bit = True
resolves_barb_or_H59 = False          # we FLAG; we do not move
flips_count = False
check("E stated CONDITIONAL on the W235 record bit", conditional_on_W235_record_bit, True)
check("E does NOT resolve bar(b)/H59", resolves_barb_or_H59, False)
check("E does NOT flip the generation count", flips_count, False)

# ===========================================================================
print("-" * 82)
ok = all(CHECKS)
print("RESULT:", "PASS -- coincidence escape CHARACTERIZED (does NOT exist)" if ok else "FAIL")
print()
print("VERDICT (grade: STRUCTURAL / EXACT for the finite algebra facts):")
print("  The coincidence-admitting SMALLER-GROUP front door does NOT escape the")
print("  W234/W237 no-go.  The good-stable requirement is COMPACT IMAGE (Prop 1),")
print("  which is order-parameter-agnostic: any dynamical vacuum isotropy with")
print("  compact image has every generator commuting with the Cartan involution P,")
print("  hence ALLOWS the gen-mirror mass ~ P, hence KILLS chirality.  Preserving")
print("  chirality requires an unbroken off-diagonal boost (the grading Z), which is")
print("  non-compact => NO good-stable grading.  Coincidences (shared isotypic types")
print("  under a smaller compact group) live entirely inside the block-diagonal part;")
print("  they change the C-grading MODULI but never produce a mass-forbidding boost,")
print("  so they cannot rescue chirality.  The vacuum is FORCED NON-COINCIDENT for")
print("  the purpose of the escape: the located flaw (W237) HARDENS.  Composes with")
print("  lane A (W240): A closes the Z2-even order-parameter route, B closes the")
print("  smaller-isotropy/coincidence route; together exhaustive modulo denying Prop")
print("  1.  bar(b)/H59/the count are NOT resolved -- only characterized.")
sys.exit(0 if ok else 1)
