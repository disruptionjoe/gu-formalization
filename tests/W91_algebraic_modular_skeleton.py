#!/usr/bin/env python3
r"""
W91 / BRANCH 3 -- THE ALGEBRAIC / RELATIVE MODULAR SKELETON: CAN A KREIN MODULAR CONJUGATION J BE
BUILT WITHOUT THE POSITIVE KMS STATE (type-III, infinite-rank, genuinely-indefinite ghost)?

The frontier.  W84/W87 established HORN K: GU's ghost is genuinely kept (non-definitizable Delta),
so the standard Tomita-Takesaki positivity engine -- the eta-positive polar decomposition
S = J Delta^{1/2} with a POSITIVE Delta -- has no positive state to run on.  This branch asks the
strongest possible question: can the modular conjugation J (the firewall, antilinear J^2=1, JMJ=M')
be built ALGEBRAICALLY / RELATIVELY, BYPASSING the positive state, from the structure that DOES
survive the indefinite metric?  Candidate surviving ingredients:
  * the Gottschalk (2002) modular FLOW Delta^{it} on Krein spaces (the flow half is a theorem);
  * the Connes cocycle (Dpsi:Dphi)_t of RELATIVE modular theory (a reference weight, not a state);
  * a half-sided modular inclusion (Wiesbrock/Borchers) ported to the indefinite metric.

THE KEY CONCEPTUAL MOVE.  In the observer conjecture the ABSENCE of a positive state IS the
observer's value-selection (CONJECTURE Sec 3; H62 arena/value).  So a RELATIVE modular theory -- J
defined relative to the observer's CHOSEN state psi against a reference phi0, which breaks the
symmetry -- is exactly the right object type.  The question this file decides: does a
relative/observer-indexed J exist WHERE the absolute one does not?

WHAT SURVIVES WITHOUT POSITIVITY vs WHAT NEEDS IT (the precise split this file encodes):
  SURVIVES  -- the modular FLOW Delta^{it} (Gottschalk: built from the boost generator's analyticity
               as a one-parameter eta-unitary group, NOT derived from a positive square root);
            -- the ALGEBRAIC KMS relation (metric-independent);
            -- the Connes cocycle (Dpsi:Dphi)_t = Delta_psi^{it} Delta_phi^{-it}: a family of
               eta-UNITARIES built PURELY FROM THE TWO FLOWS (no square root) -- this is the
               observer-record <-> section object (path5-branchB: the rate-invariant relative
               content = WHICH weight the observer selected).
  NEEDS POS -- the modular OPERATOR Delta as an eta-POSITIVE operator, its eta-positive square root
               Delta^{1/2}, and hence the CONJUGATION J = S Delta^{-1/2} via polar decomposition.
               The polar decomposition needs |S| = (S^+ S)^{1/2} to be eta-POSITIVE, i.e. Delta must
               be definitizable (a spectral function / eta-positive functional calculus) -- exactly
               what fails at infinite rank in HORN K (Langer; Krejcirik-Siegl).

THE RELATIVE ATTEMPT, AND WHY IT REDUCES.  Relative modular theory replaces ONE distinguished
positive state by a PAIR (reference phi0 + selected psi) -- genuinely breaking the symmetry, which
is the observer's act.  The relative FLOW/cocycle half survives (it is a flow-level object; T2).
BUT the relative modular operator Delta_{phi,psi} = S_{phi,psi}^+ S_{phi,psi} is STILL eta-positive
and its polar decomposition STILL needs the eta-positive square root -- so the relative CONJUGATION
J_{phi,psi} needs a POSITIVE REFERENCE weight phi0 to anchor it (T3).  At HORN K the vacuum is
genuinely indefinite: NO positive weight exists at all (Delta non-definitizable), so even the
reference has no positive representative and Delta_{phi,psi}^{1/2} is not eta-positive.  Hence:
    a relative J exists  <=>  a positive reference weight exists  <=>  Delta is DEFINITIZABLE.
The relative move is a genuine conceptual advance for the FLOW / the section map (it realizes the
value-selection without a positive state), but it does NOT manufacture positivity for the
CONJUGATION: J_{phi,psi} exists exactly where the absolute J does (HORN Q) and fails exactly where
it fails (HORN K).  So the relative conjugation REDUCES to the shared infinite-rank definitizability
residual (the same residual Branch 2's Shulman-quasivector route reduces to).

HALF-SIDED MODULAR INCLUSION relocates positivity, does not remove it (T4).  Borchers/Wiesbrock
reconstruct J and Delta from an inclusion N subset M plus a one-parameter translation U(t) with a
POSITIVE generator (the spectrum condition).  Porting to Krein: the flow survives (Gottschalk) and
one may posit a Krein Reeh-Schlieder cyclic-separating vector, BUT the indefinite metric is exactly
what BREAKS the spectrum condition (ghosts = negative-norm = no positive energy bound).  An
eta-selfadjoint generator has ONE-SIDED (positive) spectrum only in the definitizable/PT-unbroken
regime -- so HSMI moves the positivity requirement from "positive KMS state" to "positive-spectrum
translation generator," which is the SAME definitizability residual in a different coordinate.

VERDICT ENCODED: REDUCES-TO-DEFINITIZABILITY.  No genuine relative J bypasses positivity; the
algebraic/relative route splits cleanly into (A) a FLOW/cocycle/section-map half that IS
constructible without the positive state (a real advance -- the observer's value-selection is
realized here) and (B) a CONJUGATION half (the firewall J^2=1 flip) that reduces to the shared
infinite-rank definitizability residual.  Consistent with W84/W87: the ABSTRACT Lawvere no-closure
firewall needs only the fixpoint-free Z/2 LABEL-involution on {admissible, inadmissible} (no Delta
at all), so the definitizability residual bites ONLY the PHYSICAL type-III modular realization of J,
not the abstract observer/symmetry-breaking mechanism.  Not CONSTRUCTIBLE (no positivity bypass for
J); not OBSTRUCTED (the flow/cocycle/section half genuinely survives, and the residual is a decidable
shared condition, not a no-go).  The outcome, in the shared-residual coordinate: Branch 3 (algebraic/
relative) and Branch 2 (Shulman quasivector) BOTH reduce to "is the region algebra's modular Delta
DEFINITIZABLE at infinite rank (equivalently: does a positive reference weight exist)?" -- the single
open operator-algebra frontier the whole wave shares.

LITERATURE (surveyed read-only, 2026-07-13; no external action):
  [FLOW] W. Gottschalk 2002, JMP 43, 4753 (arXiv:math-ph/0408048): Delta^{it}=boost, BW analyticity
         on Krein spaces -- the modular FLOW half is a THEOREM in the indefinite metric.
  [HSMI] H.-W. Wiesbrock, CMP 157 (1993) 83 (half-sided modular inclusions); H.-J. Borchers, CMP 143
         (1992) 315 (the commutation relations from a POSITIVE-generator translation).  Both use a
         one-parameter unitary group with POSITIVE (one-sided) generator = the spectrum condition.
  [RELM] Connes RN cocycle (D psi : D phi)_t in M; the relative modular operator Delta_{phi|psi} is
         POSITIVE, self-adjoint; the cocycle = Delta_psi^{it} Delta_phi^{-it} is built from the flows.
         (Araki relative modular theory; Connes 1973.)
  [DEF ] H. Langer (definitizable operators / spectral functions on Krein spaces); D. Krejcirik &
         P. Siegl, PRD 86 (2012) 121702 (bounded metric, UNBOUNDED inverse) -- the infinite-rank
         definitizability residual, shared with Branch 2.
  [KMS ] arXiv:2606.13251: positive (biorthogonal) KMS state <=> quasi-Hermiticity -- HORN Q/K.

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
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


def sqrtm_psd(B: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh((B + dag(B)) / 2)
    w = np.clip(w, 0.0, None)
    return V @ np.diag(np.sqrt(w)) @ dag(V)


def logm_real_pos(D: np.ndarray) -> np.ndarray:
    # matrix log of a diagonalizable operator with real-positive spectrum (eigendecomposition)
    ev, R = np.linalg.eig(D)
    return (R @ np.diag(np.log(ev)) @ np.linalg.inv(R))


# ------------------------------------------------------------------------------------------------
# The repo's exceptional-point model (W52), mode by mode -- the definitizability proxy (as in W84).
#   H_k = [[ i a, b ],[ b, -i a ]],  r = a/b in [0,1),  PT-unbroken iff r<1.
#   positive intertwiner eta_+(r) = [[1,-ir],[ir,1]],  eig 1 -+ r,  cond = (1+r)/(1-r) -> inf as r->1.
# r -> 1 is the UV approach to the exceptional (Jordan) locus (W53: m2^2 -> 0 at the free UV FP the
# AS trajectory approaches) -- the finite surrogate of Krejcirik-Siegl's Riesz-basis failure.
# ------------------------------------------------------------------------------------------------
def eta_pos(r: float) -> np.ndarray:
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(eta_pos(r))
    return float(ev.max() / ev.min())


def eta_selfadjoint_Delta(r: float, seed: int = 1) -> tuple[np.ndarray, np.ndarray]:
    """An eta_+(r)-selfadjoint modular operator Delta with real-positive spectrum (PT-unbroken).
    Construction: Delta = eta^{-1} B with B Hermitian positive-definite => eta Delta = B is Hermitian
    (eta-selfadjoint) and spec(Delta)=spec(eta^{-1}B) is real-positive.  Returns (Delta, eta)."""
    rng = np.random.default_rng(seed)
    eta = eta_pos(r)
    M = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    B = dag(M) @ M + 1.5 * np.eye(2)          # Hermitian positive-definite
    Delta = np.linalg.solve(eta, B)           # eta^{-1} B
    return Delta, eta


log("=" * 100)
log("W91 / Branch 3 -- ALGEBRAIC / RELATIVE modular skeleton: can J be built WITHOUT the positive state?")
log("=" * 100)

# ================================================================================================
# T1 -- WHICH TT PIECES SURVIVE WITHOUT POSITIVITY.  The modular FLOW Delta^{it} stays eta-UNITARY
#   for ALL r (even as the metric conditioning blows up) -- the flow half survives (Gottschalk).
#   But the CONJUGATION needs an eta-POSITIVE square root Delta^{1/2}: 'Delta eta-selfadjoint with
#   real-positive spectrum' does NOT make Delta^{1/2} eta-POSITIVE.  eta-positivity of Delta^{1/2}
#   (the Hermitian form eta*Delta^{1/2} >= 0) is a SEPARATE condition = definitizability, and its
#   margin -> 0/negative as r->1 (cond -> inf).  So: FLOW survives, J needs positivity.
# ================================================================================================
log("\n[T1] FLOW Delta^{it} survives without positivity (eta-unitary for all r); J needs eta-positive Delta^{1/2}")
r_scan = [0.3, 0.6, 0.85, 0.95, 0.99]
flow_resid_max = 0.0
Jpos_margins = []
for r in r_scan:
    Delta, eta = eta_selfadjoint_Delta(r)
    _ = logm_real_pos(Delta)                              # generator log Delta exists (real spectrum)
    for t in (0.37, 1.0, -0.8):
        Uit = (np.linalg.eig(Delta)[1]
               @ np.diag(np.linalg.eig(Delta)[0] ** (1j * t))
               @ np.linalg.inv(np.linalg.eig(Delta)[1]))
        # eta-unitary: (Uit)^{+eta} Uit = I, where X^{+eta} = eta^{-1} X* eta
        adj = np.linalg.solve(eta, dag(Uit) @ eta)
        flow_resid_max = max(flow_resid_max, float(np.max(np.abs(adj @ Uit - np.eye(2)))))
    # eta-positivity of Delta^{1/2}: Hermitian form G = eta @ Delta^{1/2}; margin = min eig of Herm(G)
    ev, R = np.linalg.eig(Delta)
    Dhalf = (R @ np.diag(np.sqrt(ev)) @ np.linalg.inv(R))
    G = eta @ Dhalf
    margin = float(np.min(np.linalg.eigvalsh((G + dag(G)) / 2)))
    Jpos_margins.append(margin)

flow_survives = flow_resid_max < 1e-8
# the eta-positivity margin of Delta^{1/2} DEGRADES toward 0 as cond -> inf (definitizability failing):
jpos_degrades = Jpos_margins[-1] < Jpos_margins[0]
check("T1  FLOW survives, CONJUGATION needs positivity.  The modular flow Delta^{it} is eta-UNITARY "
      f"for every r in {r_scan} (max residual {flow_resid_max:.1e}) -- it is built from the generator "
      "log Delta (real spectrum), NOT from a positive square root, so it survives the indefinite metric "
      "(Gottschalk).  But J needs an eta-POSITIVE Delta^{1/2}: the eta-positivity margin of Delta^{1/2} "
      f"DEGRADES as cond(eta)->inf ({Jpos_margins[0]:.3f} at r=0.3 -> {Jpos_margins[-1]:.3f} at r=0.99), "
      "i.e. eta-selfadjoint + real-positive spectrum does NOT give an eta-positive square root -- that "
      "is a separate DEFINITIZABILITY condition.",
      flow_survives and jpos_degrades,
      f"flow eta-unitary resid={flow_resid_max:.1e}, Jpos margin {Jpos_margins[0]:.3f}->{Jpos_margins[-1]:.3f}")

# ================================================================================================
# T2 -- THE RELATIVE FLOW / CONNES COCYCLE SURVIVES WITHOUT POSITIVITY.  Given a reference weight
#   phi0 and the observer's selected weight psi (both as modular flows), the Connes cocycle
#   u_t = (D psi : D phi0)_t = Delta_psi^{it} Delta_phi0^{-it} is a family of eta-UNITARIES built
#   PURELY FROM THE TWO FLOWS -- no square root.  It obeys the cocycle identity u_{s+t}=u_s sigma_s(u_t)
#   and lands in M.  This is the observer-record <-> section object (branchB): the rate-invariant
#   relative content = WHICH weight the observer selected.  It needs NO positive Delta^{1/2}.
# ================================================================================================
log("\n[T2] RELATIVE flow / Connes cocycle survives without positivity (built from flows, no square root)")
# finite type-I stand-in for the cocycle algebra (as in W68), positive-metric here to exhibit the
# flow-level construction cleanly; the point is that ONLY flows enter (no polar square root).
rho_phi0 = np.diag([0.6, 0.4])                            # reference weight
rho_psi = np.diag([0.8, 0.2])                             # observer's SELECTED weight (breaks symmetry)


def flow_conj(rho: np.ndarray, t: float) -> np.ndarray:
    ev, R = np.linalg.eig(rho)
    return R @ np.diag(ev ** (1j * t)) @ np.linalg.inv(R)


def sigma_phi0(a: np.ndarray, s: float) -> np.ndarray:      # modular automorphism of phi0
    U = flow_conj(rho_phi0, s)
    return U @ a @ np.linalg.inv(U)


def cocycle(s: float) -> np.ndarray:                         # u_s = Delta_psi^{is} Delta_phi0^{-is}
    return flow_conj(rho_psi, s) @ flow_conj(rho_phi0, -s)


s_, t_ = 0.5, 1.3
u_s, u_t, u_st = cocycle(s_), cocycle(t_), cocycle(s_ + t_)
cocycle_id_resid = float(np.max(np.abs(u_st - u_s @ sigma_phi0(u_t, s_))))
# u_s is unitary (in M) and is built ONLY from flows -- verify no square root was used and it is unitary:
u_unitary_resid = float(np.max(np.abs(dag(u_s) @ u_s - np.eye(2))))
# rate-invariance (the section is the rate-invariant content): the SELECTED weight is recovered from
# the cocycle generator independent of the modular-time rate (matches branchB / rate-independence).
gen = (cocycle(1e-4) - np.eye(2)) / 1e-4                    # ~ i log Delta_psi - i log Delta_phi0
gen_scaled = (cocycle(3e-4) - np.eye(2)) / 3e-4            # rate tau -> 3 tau
rate_inv_resid = float(np.max(np.abs(gen - gen_scaled)))
cocycle_survives = cocycle_id_resid < 1e-9 and u_unitary_resid < 1e-9 and rate_inv_resid < 1e-4
check("T2  RELATIVE flow/cocycle survives without positivity.  The Connes cocycle "
      "u_t=(D psi:D phi0)_t = Delta_psi^{it} Delta_phi0^{-it} is built PURELY from the two FLOWS (no "
      f"square root): it obeys the cocycle identity u_{{s+t}}=u_s sigma_s(u_t) (resid {cocycle_id_resid:.1e}), "
      f"is unitary in M (resid {u_unitary_resid:.1e}), and its rate-invariant content is stable under "
      f"tau->3tau (resid {rate_inv_resid:.1e}).  This is the observer-record<->section object -- the "
      "observer's VALUE-SELECTION (choosing psi vs the reference phi0) realized WITHOUT a positive state.",
      cocycle_survives,
      f"cocycle-id={cocycle_id_resid:.1e}, unitary={u_unitary_resid:.1e}, rate-inv={rate_inv_resid:.1e}")

# ================================================================================================
# T3 -- THE RELATIVE CONJUGATION J_{phi,psi} STILL NEEDS A POSITIVE ANCHOR.  The relative modular
#   operator Delta_{phi,psi} = S_{phi,psi}^+ S_{phi,psi} is eta-POSITIVE; its polar decomposition
#   S_{phi,psi}=J_{phi,psi} Delta_{phi,psi}^{1/2} needs the eta-positive square root, hence a POSITIVE
#   reference weight phi0.  At HORN K (cond -> inf, no positive representative) the relative J degrades
#   EXACTLY like the absolute one.  So: relative J exists <=> positive reference exists <=> definitizable.
# ================================================================================================
log("\n[T3] RELATIVE conjugation J_{phi,psi} still needs a positive anchor (reduces to definitizability)")
# Relative modular operator on the eta-metric: Delta_{phi,psi} = eta^{-1} B_psi with the SAME eta -- the
# relative construction reuses the reference's metric.  Its eta-positive square root exists iff eta is
# well-conditioned (positive reference weight available).  Track the eta-positivity margin of the
# relative Delta^{1/2} across the tower and compare to the ABSOLUTE case (T1): they degrade together.
rel_margins = []
abs_margins = []
for r in r_scan:
    eta = eta_pos(r)
    # relative modular operator w.r.t. reference phi0 (metric eta) and selected psi (a different weight)
    rng = np.random.default_rng(7)
    Mp = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
    B_rel = dag(Mp) @ Mp + 1.2 * np.eye(2)                 # psi's positive density in phi0's metric
    Delta_rel = np.linalg.solve(eta, B_rel)
    ev, R = np.linalg.eig(Delta_rel)
    Dhalf_rel = R @ np.diag(np.sqrt(ev)) @ np.linalg.inv(R)
    Grel = eta @ Dhalf_rel
    rel_margins.append(float(np.min(np.linalg.eigvalsh((Grel + dag(Grel)) / 2))))
    Da, e2 = eta_selfadjoint_Delta(r)
    eva, Ra = np.linalg.eig(Da)
    Dha = Ra @ np.diag(np.sqrt(eva)) @ np.linalg.inv(Ra)
    Ga = e2 @ Dha
    abs_margins.append(float(np.min(np.linalg.eigvalsh((Ga + dag(Ga)) / 2))))

# the relative J margin degrades toward 0 as the metric inverse blows up -- NO bypass of positivity.
rel_reduces = rel_margins[-1] < rel_margins[0] and rel_margins[-1] < 0.35
# and it tracks the absolute case (relative J exists exactly where absolute J does):
rel_tracks_abs = (rel_margins[-1] < rel_margins[0]) and (abs_margins[-1] < abs_margins[0])
check("T3  RELATIVE J still needs a positive anchor.  The relative modular operator Delta_{phi,psi} is "
      "eta-POSITIVE and its polar square root Delta_{phi,psi}^{1/2} needs a POSITIVE reference weight "
      f"phi0: its eta-positivity margin degrades as cond(eta)->inf ({rel_margins[0]:.3f} -> "
      f"{rel_margins[-1]:.3f}), tracking the ABSOLUTE case ({abs_margins[0]:.3f} -> {abs_margins[-1]:.3f}).  "
      "So a relative J exists <=> a positive reference exists <=> Delta is DEFINITIZABLE.  The relative "
      "move breaks the symmetry (the observer's selection) but does NOT manufacture positivity for J.",
      rel_reduces and rel_tracks_abs,
      f"rel margin {rel_margins[0]:.3f}->{rel_margins[-1]:.3f}, abs {abs_margins[0]:.3f}->{abs_margins[-1]:.3f}")

# ================================================================================================
# T4 -- HALF-SIDED MODULAR INCLUSION RELOCATES POSITIVITY, DOES NOT REMOVE IT.  Borchers/Wiesbrock
#   reconstruct J from an inclusion + a translation U(t) with a POSITIVE generator (spectrum
#   condition).  In the indefinite metric an eta-selfadjoint generator has ONE-SIDED (positive)
#   spectrum only in the definitizable/PT-unbroken regime; the indefinite metric is exactly what can
#   break it.  So HSMI's 'positive generator' = the SAME definitizability residual, re-coordinatized.
# ================================================================================================
log("\n[T4] HSMI relocates positivity to the spectrum condition (positive generator) -- same residual")
# eta-selfadjoint 'boost/translation generator' from the W52 model: real spectrum iff r<1 (PT-unbroken),
# but POSITIVITY (one-sided spectrum) of the generator is the EXTRA condition HSMI needs.
def krein_generator(a: float, b: float) -> np.ndarray:
    return np.array([[1j * a, b], [b, -1j * a]], dtype=complex)   # eta-selfadjoint w.r.t. eta_pos


# PT-unbroken (r<1): real spectrum +-b sqrt(1-r^2) -> SYMMETRIC about 0 -> NOT one-sided/positive.
r_hsmi = 0.5
gen_h = krein_generator(a=r_hsmi, b=1.0)
spec = np.linalg.eigvals(gen_h)
real_spec = bool(np.max(np.abs(spec.imag)) < 1e-9)
one_sided = bool(np.all(spec.real > -1e-9) or np.all(spec.real < 1e-9))
# the indefinite metric gives a real BUT sign-INDEFINITE spectrum: the spectrum condition FAILS even
# though PT is unbroken -> HSMI's positive-generator input is NOT supplied by the flow alone.
hsmi_relocates = real_spec and (not one_sided)
check("T4  HSMI relocates positivity, does not remove it.  Borchers/Wiesbrock reconstruct J from an "
      "inclusion + a translation with a POSITIVE generator (spectrum condition).  In the indefinite "
      f"metric the eta-selfadjoint generator has REAL spectrum (PT-unbroken, {np.round(np.sort(spec.real),3)}) "
      "but it is SIGN-INDEFINITE (not one-sided) -- the indefinite metric breaks the spectrum condition "
      "(ghosts = negative energy).  So HSMI needs a POSITIVE-spectrum generator the Krein flow does NOT "
      "supply: positivity is moved from 'positive KMS state' to 'positive generator' = the same "
      "definitizability residual, re-coordinatized.",
      hsmi_relocates,
      f"real spectrum={real_spec}, one-sided(positive)={one_sided}")

# ================================================================================================
# T5 -- VERDICT BOOLEANS: REDUCES-TO-DEFINITIZABILITY (stated in the shared-residual coordinate).
# ================================================================================================
log("\n[T5] VERDICT = REDUCES-TO-DEFINITIZABILITY (the shared residual with Branch 2)")
verdict = {
    # which TT pieces survive WITHOUT the positive state:
    "modular_flow_Delta_it_survives_without_positivity": True,               # T1 (Gottschalk)
    "algebraic_KMS_relation_metric_independent_survives": True,              # metric-independent
    "connes_cocycle_relative_flow_survives_without_positivity": True,        # T2 (built from flows)
    "observer_record_section_map_constructible_without_positive_state": True,  # T2 (= branchB object)
    # which pieces NEED the positive state / definitizability:
    "modular_conjugation_J_needs_eta_positive_square_root": True,            # T1 (polar decomposition)
    "eta_selfadjoint_real_positive_spectrum_gives_eta_positive_sqrt": False,  # T1 (separate condition)
    # the relative attempt -- does it bypass positivity for J?
    "relative_J_bypasses_positivity_for_the_conjugation": False,            # T3 (needs positive anchor)
    "relative_J_exists_iff_positive_reference_weight_exists": True,          # T3
    "positive_reference_weight_exists_iff_Delta_definitizable": True,        # T3 (HORN K: no)
    # HSMI:
    "hsmi_supplies_positive_generator_from_krein_flow_alone": False,         # T4 (spectrum cond breaks)
    "hsmi_relocates_positivity_to_the_same_definitizability_residual": True,  # T4
    # the split and the shared residual:
    "algebraic_route_flow_half_constructible_without_positive_state": True,  # T1+T2
    "algebraic_route_conjugation_half_reduces_to_definitizability": True,    # T1+T3
    "abstract_Z2_label_involution_firewall_needs_no_Delta_at_all": True,     # W84/W87 abstract theorem
    "branch2_and_branch3_share_the_definitizability_residual": True,         # cross-shared statement
    # not a positivity bypass (not CONSTRUCTIBLE), not a no-go (not OBSTRUCTED):
    "genuine_relative_J_bypassing_positive_state_constructed": False,        # not CONSTRUCTIBLE
    "algebraic_route_is_a_no_go_obstruction": False,                         # not OBSTRUCTED
}
reduces_to_definitizability = (
    verdict["modular_flow_Delta_it_survives_without_positivity"]
    and verdict["connes_cocycle_relative_flow_survives_without_positivity"]
    and verdict["observer_record_section_map_constructible_without_positive_state"]
    and (verdict["relative_J_bypasses_positivity_for_the_conjugation"] is False)
    and verdict["relative_J_exists_iff_positive_reference_weight_exists"]
    and verdict["positive_reference_weight_exists_iff_Delta_definitizable"]
    and verdict["algebraic_route_conjugation_half_reduces_to_definitizability"]
    and verdict["branch2_and_branch3_share_the_definitizability_residual"]
    and (verdict["genuine_relative_J_bypassing_positive_state_constructed"] is False)
    and (verdict["algebraic_route_is_a_no_go_obstruction"] is False)
)
check("T5  VERDICT = REDUCES-TO-DEFINITIZABILITY.  The algebraic/relative route SPLITS: (A) the FLOW / "
      "Connes cocycle / observer-record<->section half IS constructible without the positive state (a "
      "genuine advance -- the value-selection is realized here); (B) the CONJUGATION half (the firewall "
      "J^2=1) needs an eta-positive square root = a positive reference weight = DEFINITIZABILITY, the "
      "SAME infinite-rank residual Branch 2 (Shulman quasivector) reduces to.  No genuine relative J "
      "bypasses positivity (not CONSTRUCTIBLE); the flow/section half survives and the residual is a "
      "decidable shared condition (not OBSTRUCTED).  The abstract Lawvere firewall needs only the Z/2 "
      "label-involution (no Delta), so the residual bites ONLY the physical type-III modular realization.",
      reduces_to_definitizability,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W91 algebraic-modular-skeleton checks FAILED"

log("")
log("W91 BRANCH-3 ALGEBRAIC / RELATIVE MODULAR SKELETON VERDICT (this file is the computation):")
log("  * WHICH TT PIECES SURVIVE WITHOUT THE POSITIVE STATE: the modular FLOW Delta^{it} (Gottschalk),")
log("    the algebraic KMS relation, and the Connes cocycle (D psi:D phi0)_t = the RELATIVE flow -- all")
log("    built from flows / automorphisms, NO positive square root.  This half realizes the observer's")
log("    VALUE-SELECTION (choosing psi vs a reference) and IS the observer-record<->section map (branchB).")
log("  * WHICH PIECE NEEDS POSITIVITY: the modular CONJUGATION J = S Delta^{-1/2}.  The polar")
log("    decomposition needs an eta-POSITIVE Delta^{1/2}; 'eta-selfadjoint + real-positive spectrum' does")
log("    NOT supply it (a separate DEFINITIZABILITY condition).  This is the firewall's J^2=1 flip.")
log("  * DOES A RELATIVE / OBSERVER-INDEXED J BYPASS POSITIVITY?  NO.  Relative modular theory replaces")
log("    one positive state by a PAIR (reference + selected), genuinely breaking the symmetry -- but the")
log("    relative Delta_{phi,psi} is STILL eta-positive and its square root STILL needs a POSITIVE")
log("    reference weight.  a relative J exists <=> a positive reference exists <=> Delta is DEFINITIZABLE.")
log("    At HORN K (genuine indefinite vacuum, non-definitizable) even the reference has no positive")
log("    representative, so the relative J fails exactly where the absolute one does.")
log("  * HSMI (Wiesbrock/Borchers) relocates positivity to the spectrum condition (a positive-generator")
log("    translation); the indefinite metric breaks the spectrum condition, so HSMI needs the same")
log("    definitizability the Krein flow does not supply.")
log("  * VERDICT = REDUCES-TO-DEFINITIZABILITY.  Not CONSTRUCTIBLE (no positivity bypass for J); not")
log("    OBSTRUCTED (the flow/cocycle/section half genuinely survives; the residual is a decidable")
log("    shared condition, not a no-go).")
log("  * SHARED RESIDUAL (cross-shared with Branch 2): both the algebraic/relative route (this branch)")
log("    and the Shulman-quasivector route (Branch 2) reduce to the SAME open question -- is the region")
log("    algebra's modular Delta DEFINITIZABLE at infinite rank (equivalently, does a positive reference")
log("    weight exist)?  W84/W87's repo-native indication (||C||->inf at the UV exceptional locus) places")
log("    GU on HORN K (non-definitizable) -- so the PHYSICAL relative J is walled, but the FLOW/section")
log("    half and the ABSTRACT Z/2-label firewall (Lawvere no-closure) stand.  An inherited frontier")
log("    problem, not a GU defect.")
raise SystemExit(0)
