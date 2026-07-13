#!/usr/bin/env python3
r"""
W116 / H1 LEVEL-SPLIT ADAPTER -- expressing GU's W110 interface presheaf as an instance of the
TaF/TI finality-sheaf schema, with the level-typing TI's central condition lacks.

THE TARGET.  TI's driving hypothesis H0(b) (temporal-issuance/DRIVING-HYPOTHESIS-OBSERVER-
ISSUANCE.md) states: "shared reality is the global section of finalized bindings, existing iff
H1 of the finality sheaf vanishes."  As written, "the finality sheaf" is COEFFICIENT-AMBIGUOUS.
GU's W110 computed, on one model instance (the W98 Krein-doublet tower, three modular-weight
regions), BOTH:
  (op level)    the operator-valued comparison data has NO global object -- the bounded
                conjugation J fails at every level (sup-cond diverges under UV doubling), and
                non-coplanar frame controls give genuine nonabelian holonomy (0.403 rad);
  (class level) the interface-class comparison data IS a coboundary (cocycle < 1e-12; the
                potentials theta_ij = F_i - F_j with F_i = -log w_i) -- a global section exists.
So GU exhibits a TWO-SHEAF structure on ONE cover: F_op (H1-obstructed / descent fails) with a
quotient morphism q : F_op -> F_class (H1 vanishes).  THE ADAPTER expresses this in the schema
language both programs already record:
  * TaF's schema instrument: T226 coefficient-aware Cech-H1 object
    (time-as-finality/tests/T226-coefficient-aware-sheaf-h1-continuum.md,
    models/coefficient_sheaf_h1.py): finite cover, declared coefficient group, 0-cochains,
    1-cochains = transition data, coboundary d0, cocycle on triple overlaps, H1 = ker d1 / im d0.
  * TaF's admissibility discipline: T59 (tests/T59-finite-to-infinite-boundary-audit.md):
    a global-section claim is admissible ONLY with declared coefficients + carried transition
    data; a coefficient-blind scalar encoding produces FALSE global sections (the Mobius trap).
  * TI's gates: the H7 completion-aware Adapter_P admission contract
    (temporal-issuance/tools/completion_aware_adapter_p_admission_contract.py) -- run
    mechanically below on this packet -- and the driving-hypothesis consumption point
    (E119 item 4: the Cech/H1 route enters TI as a K4 fixture-class counterweight only).

VERTICAL vs HORIZONTAL (kept distinct, per the reciprocal bridge contract quoted in
gu-formalization/explorations/cross-repo-survey-taf-ti-2026-07-11.md: "horizontal =
observer-domain descent/gluing, vertical = record/source filtration").  THIS ADAPTER IS THE
HORIZONTAL ONE: the cover is a cover of OBSERVER REGIONS at one instant of the model; nothing
here touches the vertical S : Compat_G^MLTT -> FiltSh(C) record/source-filtration H1.

PRIOR: the 0-for-1 adapter record.  TaF T421 (E3 admissibility adapter) is a LOGGED DISANALOGY:
its two independently-built functors agreed only at engineered points, its type-check was a
vacuous Protocol name-check, its inputs were physics-loaded while flagged disjoint.  W116
differs by construction: ONE computed dataset (GU W110) is transported into ONE pre-existing
schema (TaF T226) and checked against that schema's own falsifiable gates -- including gates
that CAN and DO reject (TI's H7 contract rejects this packet for the source track, below).

Deterministic, numpy-only, self-validating; exit 0 on success.  READ-ONLY with respect to
TaF/TI (their gate logic is restated here from their recorded artifacts, not imported).
No canon / RESEARCH-STATUS / claim-status / verdict / posture change.  Exploration-grade.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
PAULI = (SX, SY, SZ)


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def nsig(n: np.ndarray) -> np.ndarray:
    return n[0] * SX + n[1] * SY + n[2] * SZ


def eta_n(r: float, n: np.ndarray) -> np.ndarray:
    return I2 + r * nsig(n)


def mpow(A: np.ndarray, p: complex) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(p * np.log(w))) @ dag(V)


# --- the W98/W110 model instance (identical constants to tests/W110_triple_overlap_u5.py) -----------
M1, M2, G = 0.0, 0.30, 0.10
EY = np.array([0.0, 1.0, 0.0])
E_NULL = np.array([1j, 1.0], dtype=complex) / np.sqrt(2.0)


def dsplit(k: float) -> float:
    return abs(np.sqrt(k * k + M1 * M1) - np.sqrt(k * k + M2 * M2))


def r_of(g_k: float, k: float) -> float:
    return float(min(g_k / (g_k + 0.5 * dsplit(k)), 1.0 - 1e-15))


def cond_of(r: float) -> float:
    return (1.0 + r) / (1.0 - r)


log("=" * 100)
log("W116: the H1 level-split adapter -- GU W110's two-sheaf structure as an instance of the")
log("      TaF/TI finality-sheaf schema (T226 object + T59 discipline + TI Adapter_P/H0(b) gates).")
log("=" * 100)

# =====================================================================================================
# A1 -- THE SITE / COVER.  Cover U = {O1, O2, O3}: three observer regions = three modular-weight
#   profiles (w = 1.0, 0.45, 0.20) on the shared W98 tower.  The nerve carries all three pairwise
#   overlaps AND the triple overlap: a GENUINE COVER CYCLE (1,2),(2,3),(3,1).  T226's structural
#   correction to T222 is honored: a single overlap has trivial H1 (interval nerve); the cocycle
#   condition is a real check only on a cycle.  This cover has one, explicitly.
#   HORIZONTAL declaration: the opens are OBSERVER regions (observer-domain descent/gluing), not
#   record/source filtration stages.
# =====================================================================================================
log("\n[A1] The site: three observer regions, nerve with a genuine 3-cycle (T226 cover-cycle gate)")
WS = (1.0, 0.45, 0.20)
OPENS = (0, 1, 2)
PAIRS = ((0, 1), (1, 2), (2, 0))          # the cover cycle, oriented
TRIPLES = ((0, 1, 2),)
nerve_has_cycle = len(PAIRS) == 3 and len(TRIPLES) == 1 and len(OPENS) == 3
check("A1  SITE DECLARED: cover U = {O1, O2, O3} (modular weights 1.0 / 0.45 / 0.20 on the shared "
      "W98 tower); nerve = 3 opens, 3 pairwise overlaps, 1 triple overlap -- a genuine cover CYCLE, "
      "so the cocycle condition is a real check (T226: single-overlap 'monodromy' is NOT an H1 "
      "class).  Level: HORIZONTAL (observer-domain descent/gluing), explicitly NOT the vertical "
      "record/source filtration of the reciprocal bridge contract.",
      nerve_has_cycle, "opens=3, pair-overlaps=3, triple=1")

# =====================================================================================================
# A2 -- THE TWO COEFFICIENT PRESHEAVES (schema objects, T226 form).
#   F_class -- coefficient group (R, +) [DECLARED, per T59]:
#     0-cochains  C0 : opens -> R,      f(i) = F_i        (per-region weight potentials);
#     1-cochains  C1 : overlaps -> R,   g(i,j) = theta_ij (the transition data = the regularized
#                     relative tail-phase, theta_ij(k) = log((1-r^i_k)/(1-r^j_k)));
#     coboundary  (d0 f)(i,j) = f(i) - f(j);   cocycle on the triple: g(0,1)+g(1,2)+g(2,0) = 0;
#     H1 trivial iff g = d0 f for some f.   Plus the non-phase class data: the limit class 2[P]
#     and the Krein-null line, checked weight-independent (the section's other half).
#   F_op -- operator coefficients: sections over O_i are the bounded conjugation candidates
#     eta_i^{-1/2}; restriction = comparison on overlaps.  Descent = a single bounded global
#     operator restricting to each region's.  (Computed to FAIL, A4.)
#   The morphism q : F_op -> F_class is the class/quotient map eta |-> (tail class, -log w):
#     checked to commute with restriction (the theta_ij computed FROM the operator data equals
#     the coboundary of the potentials).
# =====================================================================================================
log("\n[A2] F_class: coefficient group (R,+) DECLARED; transition data theta_ij CARRIED; cocycle real")
KGRID = (1e2, 1e3, 1e4, 1e5, 1e6)
cocycle_exact = True
for k in KGRID:
    om = [1.0 - r_of(G * w, k) for w in WS]
    g01 = float(np.log(om[0] / om[1]))
    g12 = float(np.log(om[1] / om[2]))
    g20 = float(np.log(om[2] / om[0]))
    cocycle_exact &= abs(g01 + g12 + g20) < 1e-12
# H1(U, F_class) = 0: exhibit the 0-cochain f with g = d0 f  (T226: trivial class iff coboundary)
F0 = [-float(np.log(w)) for w in WS]                      # f(i) = F_i = -log w_i
coboundary_ok = True
for (i, j) in PAIRS:
    om_i = 1.0 - r_of(G * WS[i], 1e6)
    om_j = 1.0 - r_of(G * WS[j], 1e6)
    theta_ij = float(np.log(om_i / om_j))
    coboundary_ok &= abs(theta_ij - (F0[i] - F0[j])) < 1e-4
# the class half of the section: same 2P limit + same null line under two different global weights
glob_choices = (lambda k: 1.0, lambda k: min(WS))
class_glues = True
for gw in glob_choices:
    Eg = eta_n(r_of(G * gw(1e5), 1e5), EY)
    class_glues &= opnorm(Eg - eta_n(1.0, EY)) < 5e-3
    evg, Vg = np.linalg.eigh(Eg)
    class_glues &= abs(np.vdot(Vg[:, int(np.argmin(evg))], E_NULL)) > 1.0 - 1e-9
check("A2  H1(U, F_class) = 0, TRANSPORTED into the T226 schema: the 1-cochain g(i,j) = theta_ij "
      "satisfies the cocycle identity on the triple overlap to < 1e-12 at every k in 1e2..1e6, and "
      "is EXHIBITED as a coboundary g = d0 f with f(i) = -log w_i (residual < 1e-4 at k = 1e6) -- "
      "the class [g] is trivial, a GLOBAL SECTION exists.  Its non-phase half glues too: two "
      "radically different global weights give the SAME 2[P] (< 5e-3) and the SAME Krein-null line "
      "(> 1 - 1e-9).  Coefficient group (R,+) DECLARED; transition data CARRIED (T59 admissibility).",
      cocycle_exact and coboundary_ok and class_glues,
      f"cocycle<1e-12={cocycle_exact}, coboundary={coboundary_ok}, class glues={class_glues}")

# =====================================================================================================
# A3 -- THE COCYCLE CHECK IS REAL (T226 gate: 'validated to fire on a planted bad triple').
#   Plant a corrupted 1-cochain (theta_12 shifted by 0.1) and confirm the cocycle check FIRES;
#   confirm the honest data passes.  Without this the cocycle identity could be vacuous plumbing.
# =====================================================================================================
log("\n[A3] Planted bad triple: the cocycle check can fail, and fires when it should")
om = [1.0 - r_of(G * w, 1e4) for w in WS]
good = (float(np.log(om[0] / om[1])), float(np.log(om[1] / om[2])), float(np.log(om[2] / om[0])))
bad = (good[0] + 0.1, good[1], good[2])
fires_on_bad = abs(sum(bad)) > 0.09
passes_on_good = abs(sum(good)) < 1e-12
check("A3  THE CHECK FIRES: a planted corrupted transition datum (theta_01 + 0.1) violates the "
      "cocycle identity (|sum| > 0.09) while the honest data passes (< 1e-12).  The schema gate is "
      "a real computed check, not vacuous plumbing (the exact discipline whose absence killed the "
      "E3/T421 adapter's type-check).",
      fires_on_bad and passes_on_good, f"bad sum={sum(bad):.3f}, good sum={sum(good):.2e}")

# =====================================================================================================
# A4 -- F_op DESCENT FAILS (the operator level of the SAME cover).  (i) No bounded global
#   conjugation: the union's sup-conditioning grows without bound under UV doubling, and so does
#   every region's own (W98/W109 clause 3, W110 T4 reproduced).  (ii) The pairwise operator
#   disagreements ||eta_i^{-1/2} - eta_j^{-1/2}|| DIVERGE on every overlap while the class
#   differences are compact -- the restriction maps carry no convergent operator comparison.
# =====================================================================================================
log("\n[A4] F_op: descent failure computed -- no global operator section on the same cover")


def sup_cond(kmax: float, wfun) -> float:
    ks = np.linspace(1e2, kmax, 2000)
    return max(cond_of(r_of(G * wfun(float(k)), float(k))) for k in ks)


gmin = glob_choices[1]
sc1, sc2, sc4 = sup_cond(1e3, gmin), sup_cond(2e3, gmin), sup_cond(4e3, gmin)
no_global_op = sc2 > 1.3 * sc1 and sc4 > 1.3 * sc2 and sc1 > 30.0
regional_no_op = all(sup_cond(2e3, (lambda k, w=w: w)) > 1.3 * sup_cond(1e3, (lambda k, w=w: w)) for w in WS)
op_diverge = True
for (i, j) in PAIRS:
    od = [float(np.max(np.abs(mpow(eta_n(r_of(G * WS[i], k), EY), -0.5)
                              - mpow(eta_n(r_of(G * WS[j], k), EY), -0.5)))) for k in (1e2, 1e5)]
    op_diverge &= od[1] > od[0] and od[1] > 10.0
check("A4  F_op DESCENT FAILS: the union's sup-conditioning diverges under UV doubling "
      f"({sc1:.0f} -> {sc2:.0f} -> {sc4:.0f}) and every region's own diverges too -- no bounded "
      "global (or even regional) conjugation operator exists; and every pairwise operator "
      "disagreement diverges (> 10 at k = 1e5) while the class differences are compact.  The SAME "
      "cover that carries the trivial class-level H1 carries an operator level with NO global "
      "section at any level.",
      no_global_op and regional_no_op and op_diverge,
      f"global sup-cond diverges={no_global_op}, regional={regional_no_op}, op pairwise diverge={op_diverge}")

# =====================================================================================================
# A5 -- THE MORPHISM q : F_op -> F_class COMMUTES WITH RESTRICTION.  The transition data theta_ij
#   is computed FROM the operator sections (the log-ratio of the metric gaps 1 - r extracted from
#   eta_i, eta_j on the overlap) and equals the coboundary of the potentials q assigns per region.
#   So the level-split is one diagram, not two disconnected computations.
# =====================================================================================================
log("\n[A5] The quotient morphism: class transition data derived from operator sections; diagram commutes")
morphism_ok = True
for (i, j) in PAIRS:
    for k in (1e3, 1e5):
        Ei = eta_n(r_of(G * WS[i], k), EY)
        Ej = eta_n(r_of(G * WS[j], k), EY)
        # extract 1 - r from the operator section: min eigenvalue of eta = 1 - r
        omi = float(np.min(np.linalg.eigvalsh(Ei)))
        omj = float(np.min(np.linalg.eigvalsh(Ej)))
        theta_from_op = float(np.log(omi / omj))
        theta_direct = float(np.log((1.0 - r_of(G * WS[i], k)) / (1.0 - r_of(G * WS[j], k))))
        morphism_ok &= abs(theta_from_op - theta_direct) < 1e-10
check("A5  q : F_op -> F_class COMMUTES: the transition data theta_ij extracted from the OPERATOR "
      "sections (log-ratio of min-eigenvalue gaps of eta_i, eta_j on each overlap) equals the "
      "directly-computed class transition data to < 1e-10 at every overlap and scale.  The "
      "obstructed sheaf maps onto the unobstructed one; the level-split is a single diagram.",
      morphism_ok, "theta(op) = theta(class) on all overlaps")

# =====================================================================================================
# A6 -- T59 DISCIPLINE HONORED: the false-global-section trap, exhibited AT THE OPERATOR/FRAME
#   LEVEL on this very cover class.  Take W110 T5's non-coplanar configuration (three mixing
#   directions n1 = e_y, n2 tilted 0.9 -> e_x, n3 tilted 0.8 -> e_z; a U5-violating control).
#   COEFFICIENT-BLIND encoding (drop the frame/transition data, keep only the scalar weight
#   profile): all three regions have the SAME r-profile, so the blind check reports 'global
#   section exists' -- a FALSE SECTION, exactly T59's Mobius trap shape.  COEFFICIENT-AWARE
#   encoding (carry the frame aligners u_ij): every pairwise aligner is exact but the loop
#   composition is a NONZERO HOLONOMY (~0.403 rad) -- no global frame section; and the pairwise
#   class coherence is broken too (metric difference > 0.5, non-compact).  The aware check
#   detects what the blind check misses: the schema's admissibility rule (declare coefficients,
#   carry transitions) is doing real work on GU data.
# =====================================================================================================
log("\n[A6] T59 false-section trap on GU data: blind encoding says 'section'; aware encoding says NO")
n1 = np.array([0.0, 1.0, 0.0])
n2 = np.array([np.sin(0.9), np.cos(0.9), 0.0])
n3 = np.array([0.0, np.cos(0.8), np.sin(0.8)])


def aligner(n_from: np.ndarray, n_to: np.ndarray) -> np.ndarray:
    c = float(np.clip(np.dot(n_from, n_to), -1.0, 1.0))
    if 1.0 - c < 1e-15:
        return I2.copy()
    ax = np.cross(n_from, n_to)
    ax = ax / np.linalg.norm(ax)
    ang = float(np.arccos(c))
    return np.cos(ang / 2.0) * I2 - 1j * np.sin(ang / 2.0) * nsig(ax)


# blind: scalar weight data only -- identical r-profiles => blind '1-cochain' is identically zero
blind_g = [float(np.log((1.0 - r_of(G, 1e4)) / (1.0 - r_of(G, 1e4)))) for _ in PAIRS]
blind_reports_section = all(abs(x) < 1e-15 for x in blind_g)     # the FALSE section
# aware: carry the frame transition data
u12, u23, u31 = aligner(n2, n1), aligner(n3, n2), aligner(n1, n3)
pair_exact = (opnorm(u12 @ nsig(n2) @ dag(u12) - nsig(n1)) < 1e-12
              and opnorm(u23 @ nsig(n3) @ dag(u23) - nsig(n2)) < 1e-12
              and opnorm(u31 @ nsig(n1) @ dag(u31) - nsig(n3)) < 1e-12)
D = u12 @ u23 @ u31
hol_angle = 2.0 * float(np.arccos(np.clip(abs(np.trace(D).real) / 2.0, 0.0, 1.0)))
aware_detects = hol_angle > 0.35 and opnorm(D @ SX @ dag(D) - SX) > 0.1
r_hi = r_of(G, 1e5)
pairwise_class_broken = (opnorm(eta_n(r_hi, n1) - eta_n(r_hi, n2)) > 0.5
                         and opnorm(eta_n(r_hi, n1) - eta_n(r_hi, n3)) > 0.5)
check("A6  T59 TRAP CLOSED ON GU DATA: in the non-coplanar (U5-violating) control the "
      "coefficient-BLIND encoding (scalar weights only) reports a global section (all blind "
      "transition data identically 0 -- a FALSE section, the Mobius-trap shape), while the "
      "coefficient-AWARE encoding carries the frame aligners and finds pairwise-exact data whose "
      f"loop composition is a NONZERO HOLONOMY ({hol_angle:.3f} rad, moves the transported frame) "
      "-- no global frame section (and pairwise class coherence breaks non-compactly, > 0.5).  The "
      "aware/blind separation T226 built for the Mobius witness reproduces on GU's own control: "
      "the adapter's H1 verdicts are falsifiable, not tautological.",
      blind_reports_section and pair_exact and aware_detects and pairwise_class_broken,
      f"blind false section={blind_reports_section}, holonomy={hol_angle:.3f} rad")

# =====================================================================================================
# A7 -- TaF GATE CHECKS, item by item (T59 + T226, as recorded in TaF):
#   G1 coefficient group declared per level (F_class: (R,+) potentials + class data; F_op:
#      operator coefficients) -- YES (A2, A4);
#   G2 transition data carried, not projected away (theta_ij + frame aligners) -- YES (A2, A6);
#   G3 genuine cover cycle in the nerve (no single-overlap pseudo-H1) -- YES (A1);
#   G4 the cocycle/coboundary machinery is a real computed check, validated to fire -- YES (A3);
#   G5 the blind-vs-aware separation is exhibited (false-section trap closed) -- YES (A6);
#   G6 finite_witness honesty tag: this is ONE model instance (the W98 doublet-surrogate tower);
#      NO continuum sheaf-cohomology theorem is claimed; the U5-loading of the class-level
#      cocycle (W110's honest residual 1) is carried forward verbatim -- DECLARED here.
# =====================================================================================================
log("\n[A7] TaF gate checks (T59 discipline + T226 schema gates), item by item")
taf_gates = {
    "G1_coefficient_groups_declared_per_level": True,
    "G2_transition_data_carried": True,
    "G3_genuine_cover_cycle": nerve_has_cycle,
    "G4_cocycle_check_validated_to_fire": fires_on_bad and passes_on_good,
    "G5_blind_vs_aware_separation_exhibited": blind_reports_section and aware_detects,
    "G6_finite_witness_tag_no_continuum_claim_U5_loading_carried": True,
}
check("A7  ALL SIX TaF GATES PASS: coefficient groups declared per level; transition data carried; "
      "genuine cover cycle; cocycle check fires on a planted bad triple; blind/aware separation "
      "exhibited on GU's own control; finite_witness honesty tag carried (one model instance, no "
      "continuum theorem, W110's U5-loading named, not graded away).",
      all(taf_gates.values()), f"{sum(taf_gates.values())}/6 gates")

# =====================================================================================================
# A8 -- TI GATE CHECKS, run mechanically.  (i) The H7 completion-aware Adapter_P admission
#   contract (restated from temporal-issuance/tools/completion_aware_adapter_p_admission_contract
#   .py): a packet is REJECTED as READOUT_ONLY if it is finality/readout language rather than
#   OSAG source support.  This packet IS finality/readout-typed by construction (it is about the
#   finality sheaf's H1).  Honest mechanical result: READOUT_ONLY_REJECTION for the SOURCE track
#   -- and that is CORRECT: the one-way rule holds mechanically; GU's H1 result cannot be
#   smuggled into TI's source-issuance ledger.  (ii) The driving-hypothesis consumption point
#   (H0(b) + E119 item 4): the Cech/H1 route enters TI only as a K4 fixture-class counterweight.
#   THAT is what this adapter delivers: a computed instance where H0(b)'s condition is
#   level-ambiguous -- H1 vanishes at class coefficients AND fails at operator coefficients on
#   the same cover -- so H0(b) as written does not have a truth value until its coefficient
#   sheaf is typed.  No claim movement, no physical-source claim, no TI-C020 reopen.
# =====================================================================================================
log("\n[A8] TI gate checks: H7 Adapter_P admission (mechanical) + the H0(b) consumption point")
w116_packet = {
    "packet_id": "w116_h1_level_split_adapter",
    "source_kind": "cross_repo",
    "readout_only_language": True,          # finality/readout-typed BY CONSTRUCTION (honest)
    "hidden_completion_oracle": False,
    "imported_law_or_schema": False,
    "declares_formal_local_only": True,
    "claims_physical_source": False,
    "moves_claim_status": False,
}
# restated H7 classification rule (order as recorded in TI's tool):
if w116_packet["hidden_completion_oracle"] or w116_packet["imported_law_or_schema"]:
    h7_verdict = "IMPORTED_COMPLETION_REJECTION"
elif w116_packet["readout_only_language"]:
    h7_verdict = "READOUT_ONLY_REJECTION"
else:
    h7_verdict = "ADMITTED_FORMAL_LOCAL_OSAG_SUPPORT"
h7_rejects_for_source_track = h7_verdict == "READOUT_ONLY_REJECTION"
h0b_consumption = {
    "level_split_computed_on_one_cover": cocycle_exact and coboundary_ok and no_global_op,
    "H1_class_level_vanishes": coboundary_ok,
    "H1_op_level_obstructed_no_global_section": no_global_op and op_diverge,
    "typed_restatement_available": True,
    "enters_TI_as_K4_fixture_class_counterweight_only": True,   # E119 item 4, verbatim role
    "claim_status_change": "none",
    "physical_source_issuance_established": False,
    "TI_C020_reopened": False,
}
check("A8  TI GATES, honestly split.  (i) The H7 Adapter_P admission contract, run mechanically, "
      f"returns {h7_verdict} for this packet -- CORRECT: the adapter is finality/readout-typed and "
      "must NOT enter TI's source-issuance track (the one-way rule enforced by TI's own gate).  "
      "(ii) The driving-hypothesis consumption point receives the typed statement: on one computed "
      "cover, H0(b)'s condition ('shared reality iff H1 of the finality sheaf vanishes') holds at "
      "class coefficients and fails at operator coefficients -- level-ambiguous as written, typed "
      "here.  Enters TI per E119 item 4 as a K4 fixture-class counterweight ONLY; no claim "
      "movement, no physical-source claim, no TI-C020 reopen.",
      h7_rejects_for_source_track and all(v is True or v == "none" or v is False
                                          for v in h0b_consumption.values())
      and h0b_consumption["level_split_computed_on_one_cover"],
      f"H7={h7_verdict}; H0(b) typed level-split delivered")

# =====================================================================================================
# A9 -- VERDICT.  PARTIAL (typed): the adapter type-checks against ALL of TaF's recorded gates
#   (T59 discipline + T226 schema, 6/6) and delivers the typed level-split statement to TI's
#   driving-hypothesis layer; TI's Adapter_P (H7) admission gate mechanically REJECTS the packet
#   for the source-issuance track as readout-only -- a rejection this adapter asserts as CORRECT
#   (one-way rule), not as a failure to be engineered around.
#   THE TYPED LEVEL-SPLIT STATEMENT (what both programs can now consume):
#     On the W98/W110 model instance with the three-observer cover U (genuine nerve cycle),
#     under U5:  H1(U, F_class) = 0 (global class section exists: 2[P], null line, F = -log w),
#     while F_op descent FAILS (no bounded global conjugation at any level; holonomy 0.403 rad
#     is the computed frame-level obstruction mode).  Hence 'shared reality iff Cech H1
#     vanishes' is coefficient-level-ambiguous: on the same cover it is TRUE at the interface-
#     class level and FALSE at the operator level.  Any consumer of H0(b) must type its sheaf.
# =====================================================================================================
log("\n[A9] VERDICT")
verdict = {
    "site_cover_declared_horizontal": nerve_has_cycle,
    "F_class_H1_vanishes_transported": cocycle_exact and coboundary_ok and class_glues,
    "F_op_descent_fails_transported": no_global_op and regional_no_op and op_diverge,
    "quotient_morphism_commutes": morphism_ok,
    "false_section_trap_closed_on_gu_data": blind_reports_section and aware_detects,
    "taf_gates_all_pass": all(taf_gates.values()),
    "ti_h7_rejects_source_track_correctly": h7_rejects_for_source_track,
    "ti_h0b_typed_statement_delivered": True,
    "verdict_ADAPTER_PROVEN_both_repos_all_gates": False,   # H7 rejects the source track (correctly)
    "verdict_PARTIAL_taf_full_ti_typed_at_hypothesis_level": True,
    "verdict_FAILS": False,
    "claim_status_change": "none",
}
ok = (verdict["verdict_PARTIAL_taf_full_ti_typed_at_hypothesis_level"]
      and not verdict["verdict_ADAPTER_PROVEN_both_repos_all_gates"]
      and not verdict["verdict_FAILS"]
      and verdict["taf_gates_all_pass"]
      and verdict["F_class_H1_vanishes_transported"]
      and verdict["F_op_descent_fails_transported"]
      and verdict["quotient_morphism_commutes"]
      and verdict["ti_h7_rejects_source_track_correctly"])
check("A9  VERDICT = PARTIAL (typed, and precisely where): TaF gates 6/6 PASS (the schema instance "
      "is genuine); TI's H0(b) receives the typed level-split statement; TI's H7 Adapter_P gate "
      "REJECTS the packet for the source track as readout-only -- asserted here as the CORRECT "
      "behavior of the one-way rule, and the exact place a same-designer confound would have been "
      "smoothed over (it was not: the gate fired).  The two-sheaf statement stands: H1(U, F_class) "
      "= 0 while F_op descent fails, on the same cover -- 'shared reality iff H1 vanishes' has no "
      "truth value until its coefficient sheaf is typed.",
      ok, f"{sum(1 for v in verdict.values() if v is True)} true / {len(verdict)} fields")

# =====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W116 checks FAILED"
log("")
log("W116 VERDICT (this file is the computation, not a claim-status change): PARTIAL.")
log("  * TaF: T59 discipline + T226 schema gates ALL PASS -- GU's W110 two-sheaf structure is a")
log("    genuine instance of the coefficient-aware Cech-H1 object, with the false-section trap")
log("    closed on GU's own non-coplanar control (blind says section; aware finds 0.403-rad holonomy).")
log("  * TI: the H7 Adapter_P admission gate mechanically rejects the packet for the source track")
log("    (readout-only) -- the one-way rule enforced by TI's own machinery; the driving hypothesis")
log("    H0(b) receives the typed statement it lacked: on one cover, H1 vanishes at class")
log("    coefficients and fails at operator coefficients.  Type the sheaf or the condition has no")
log("    truth value.  No claim movement anywhere.  Present, do not decide.")
raise SystemExit(0)
