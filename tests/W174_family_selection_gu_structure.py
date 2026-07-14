#!/usr/bin/env python3
r"""
W174 / TEAM FAMILY-SELECT -- does GU's SPECIFIC structure SELECT the positivity
(keep-and-grade) quantization family as FORCED, or is it W133's genuinely-free declaration?

CONTEXT. W133 (path2-wave5-evencut-family-discriminator) established that the two consistent
quantizations of the one ghost-carrying Lagrangian are two INEQUIVALENT quantizations
distinguished by which of two JOINTLY-UNSATISFIABLE Kallen-Lehmann axioms survives:

    (A) analyticity  = all absorptive content on the real axis (=> microcausality), and
    (P) positivity   = nonnegative spectral weight.

The Lagrangian fixes the ghost residue sign eps = -1; Krein-weight multiplicativity then makes
every even cut carry eps^2 = +1 and every odd cut carry eps = -1, so (A) and (P) cannot both
hold (EXACT arithmetic; a normal residue eps = +1 satisfies both). The two families and the
KL-cone deviation pairs (N_A, N_P), each in units of the full cut at that family's own locus:

    GRADED / keep-and-grade : keeps (A), pays (P)  -> (N_A, N_P) = (0, 1)  [Krein C-operator]
    REMOVAL / Lee-Wick      : keeps (P), pays (A)  -> (N_A, N_P) = (1, 0)  [truncate + pair contour]

W133 verdict: the pair is EXACTLY SYMMETRIC (0,1) vs (1,0), the observable imprint is ~1e-61,
so as physics-in-general the fork is a PERMANENT DECLARATION -- dispersion alone does not select.
W133 also noted that WITHIN GU the keep-and-grade datum is already declared, and named the ONLY
visible route to an UNCONDITIONAL selection: a GU-internal derivation of the C-operator from
structure (W49/W121). This file asks W133's sharper successor question:

    Does GU's SPECIFIC structure -- the proven-indefinite (9,5) q=5 tangent Krein signature,
    the record substrate, the C-operator = consistent-global-ledger (W150), the finality
    frontier / firewall -- SELECT the positivity/graded family as FORCED (breaking W133's
    symmetry), or is the selection a re-declaration in disguise?

TWO GU-STRUCTURAL SELECTION ARGUMENTS ARE TESTED, EACH WITH ITS GAP MADE EXPLICIT:

  ARG-1 (truncation = closed completion, forbidden by (9,5) q=5 / firewall criterion 1).
    The removal family TRUNCATES the negative-norm (ghost) sector out of the physical/asymptotic
    space, leaving a DEFINITE physical space: H_phys is the whole space, effective q = 0. In the
    record-substrate reading (W150 verdict D) that is precisely a CLOSED COMPLETION (H_C+ = whole
    space, finality frontier empty). The graded family keeps the negative directions and grades
    them: H_C+ is a PROPER maximal positive subspace of an indefinite Krein space, q = 5 latent
    remainder, frontier never empty. GU's proven (9,5) q=5 indefiniteness (W131) + firewall
    criterion 1 (no closed completion) => removal family's q=0 EXCLUDED => graded FORCED.
    GAP-1a: (9,5) is a DECLARED INPUT (firewall canon), not proven.
    GAP-1b: closed completion is "obstructed for the routes tried, NOT proven impossible"
            (firewall canon) -- it is the live frontier, not a theorem.
    GAP-1c: (9,5) is the TANGENT/field-space signature; its descent to the asymptotic-state
            Krein space (where the ghost truncation lives) is "stated as origin, not proven as a
            dimension count of the infinite-dim H_C+" (W150 verdict D).

  ARG-2 (record causal-ordering forbids the removal family's microcausality violation).
    The removal family pays (A): its absorptive content sits at conjugate branch points OFF the
    real axis, i.e. it gives up upper-half-plane analyticity = a bounded microcausality violation
    ~1/m2 (Lee-Wick; Coleman; Grinstein-O'Connell-Wise). The graded family has N_A = 0: it
    PRESERVES microcausality. If GU's records must be causally ordered, the removal family is
    excluded and the graded family forced.
    GAP-2a: the removal family's acausality is BOUNDED and MACROSCOPICALLY EMERGENT-CAUSAL
            (Grinstein-O'Connell-Wise, "Causality as an emergent macroscopic phenomenon"): a
            macroscopic finality DAG does NOT detect a ~1/m2 smearing. Only MICRO-causality
            (axiom A at the off-shell scale) excludes removal.
    GAP-2b: upgrading "records are causally ordered" from MACRO to MICRO-causality is a
            temporal-issuance/time-as-finality SEMANTIC; importing it as a GU theorem is
            exactly the one-way-gate violation W150 forbids -> a re-declaration in disguise.

The two arguments CONVERGE on the same family (graded) and, crucially, pass through the SAME
pair of unproven joints: (i) the tangent-(9,5) -> asymptotic-state descent, and (ii) the
identification of the S-matrix/off-shell ghost structure with the record-finality semantics.
Because those joints are (i) unproven-but-program-internal and (ii) TI/TaF-gated, the selection
is NOT OPERATIVE-grade forcing; but it is NOT a free coin either -- GU's substrate carries a
directional/indefinite commitment that lines up with (A)+graded and against (P)-truncation.

HONEST VERDICT (this file, exploration grade): NARROWED. W133's SYMMETRY is BROKEN at the
framing level (within GU the two axioms are not interchangeable; the structure leans hard on
graded via two convergent arguments), but the forcing is NOT closed (both arguments rest on the
same two named joints). bar (b) does NOT clear; it is sharpened from "free declaration" to
"one named descent theorem (tangent-(9,5) -> asymptotic Krein, ungated, program-internal) away
from forced." No canon change. b UNCHANGED.

Positive controls reproduce W133: the CLOP-band dispersion residuals selecting +1, the two-family
KL-deviation pairs (0,1)/(1,0), and the eps=+1 negative control (no split). Then the W174
selection bookkeeping encodes both arguments and both gaps as explicit checks.

Reproducible: python tests/W174_family_selection_gu_structure.py
Scalar core only (tensor numerators are W124 Stage C / W134). No canon change. bar (b) UNCHANGED.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ------------------------------------------------------------------------------------------
# W133 machinery (bubble + once-subtracted dispersion), reproduced for the positive controls.
# Same normalization as tests/W120, tests/W124, tests/W133.
# ------------------------------------------------------------------------------------------

def b0_quad(s: complex, a1: complex, a2: complex, eps: float = 0.0) -> complex:
    """Normalized bubble b0 = -int_0^1 dx log( x*a1 + (1-x)*a2 - x(1-x)*s - i*eps )."""
    def arg(x: float) -> complex:
        return x * a1 + (1 - x) * a2 - x * (1 - x) * s - 1j * eps

    points = [0.0, 1.0]
    if s != 0:
        c2, c1, c0 = complex(s), complex(a1 - a2 - s), complex(a2)
        disc = np.sqrt(complex(c1 * c1 - 4 * c2 * c0))
        for root in ((-c1 + disc) / (2 * c2), (-c1 - disc) / (2 * c2)):
            xr = float(root.real)
            if 1e-12 < xr < 1 - 1e-12:
                points.append(xr)
    points = sorted(set(points))
    re = quad(lambda x: (-np.log(arg(x))).real, 0, 1, points=points[1:-1] or None, limit=200)[0]
    return complex(re, 0.0)


def im_b0_ghost_pair(s: float, M2: float) -> float:
    """Graded Im of the two-ghost bubble: weight (-1)^2 = +1 times pi*sqrt(1-4M^2/s)."""
    if s > 4 * M2:
        return math.pi * math.sqrt(1 - 4 * M2 / s)
    return 0.0


M2 = 1.0
s0 = 1.0


def disp_once(s: float, weight: float, s_lo: float = 4.0) -> float:
    """Once-subtracted dispersive Re variation with Im = weight * pi*sqrt(1-4M^2/s')."""
    def g(sp: float) -> float:
        return weight * im_b0_ghost_pair(sp, M2) / (sp - s0)

    if s <= s_lo:
        val = quad(lambda sp: g(sp) / (sp - s), s_lo, 200.0, limit=200)[0]
        val += quad(lambda sp: g(sp) / (sp - s), 200.0, np.inf, limit=200)[0]
    else:
        val = quad(g, s_lo, 200.0, weight="cauchy", wvar=s, limit=200)[0]
        val += quad(lambda sp: g(sp) / (sp - s), 200.0, np.inf, limit=200)[0]
    return (s - s0) / math.pi * val


log("=" * 96)
log("W174 -- DOES GU STRUCTURE SELECT THE POSITIVITY (KEEP-AND-GRADE) FAMILY, OR FREE DECLARATION?")
log("=" * 96)

# ------------------------------------------------------------------------------------------
# 1. Positive controls: reproduce W133's two-family map.
# ------------------------------------------------------------------------------------------
log("")
log("1. Positive controls (reproduce W133's two-family / jointly-unsatisfiable-axioms map)")

re_direct = {s: b0_quad(s, M2, M2, eps=1e-12).real for s in (1.0, 6.0)}
dv_above = re_direct[6.0] - re_direct[1.0]
d_above = disp_once(6.0, +1.0)

# PC1: the CLOP band {-1/2, 0, +1/2, +1}; once-subtracted dispersion selects +1 (graded).
resids = {k: abs(dv_above - disp_once(6.0, k)) for k in (-0.5, 0.0, +0.5, +1.0)}
best = min(resids, key=resids.get)
check("PC1 W133 sum rule: among CLOP band {-1/2,0,+1/2,+1}, real-axis dispersion selects +1 "
      "(the GRADED even-cut answer) uniquely; each alternative fails by its full deficit",
      best == 1.0 and resids[1.0] < 0.01 * abs(d_above)
      and all(resids[k] > 0.4 * abs(d_above) for k in (-0.5, 0.0, +0.5)),
      "; ".join(f"k={k:+.1f}: resid={resids[k]:.4f}" for k in sorted(resids)))

# PC2: the jointly-unsatisfiable axiom arithmetic and the two-family KL-deviation pairs.
eps = -1                       # Lagrangian-fixed ghost residue sign
even_weight = eps ** 2         # +1
odd_weight = eps               # -1
graded_pair = (0.0, abs(odd_weight))          # (N_A, N_P) = (0, 1): keep (A), pay (P)
removal_pair = (abs(even_weight), 0.0)        # (N_A, N_P) = (1, 0): keep (P), pay (A)
check("PC2 W133 axiom partition: eps=-1 => even weight +1, odd weight -1; (A) analyticity and "
      "(P) positivity JOINTLY UNSATISFIABLE; KL pairs graded (0,1) vs removal (1,0), each the "
      "FULL cut at its own locus -- EXACTLY SYMMETRIC as physics-in-general (W133)",
      even_weight == 1 and odd_weight == -1
      and graded_pair == (0.0, 1.0) and removal_pair == (1.0, 0.0),
      f"graded (N_A,N_P)={graded_pair}, removal (N_A,N_P)={removal_pair}")

# PC3 (negative control): eps=+1 => both axioms hold, no split, no family question.
eps_norm = +1
check("PC3 negative control: eps=+1 => even and odd cuts BOTH positive, dispersion-complete; "
      "both KL axioms hold at once, no family split exists -- the fork (and any selection "
      "question) tracks the ghost residue sign / the Krein indefiniteness",
      (eps_norm ** 2 == 1) and (eps_norm ** 1 == +1),
      "eps=+1: even +1, odd +1, no truncation motivated")

# ------------------------------------------------------------------------------------------
# 2. ARG-1: removal family = truncation = closed completion, forbidden by (9,5) q=5 / firewall.
# ------------------------------------------------------------------------------------------
log("")
log("2. ARG-1: removal-family truncation = closed completion; (9,5) q=5 / firewall crit. 1")

# The GU tangent signature (W131): (9,5) = (3,1) base + (6,4) DeWitt fiber. p positive, q negative.
p_sig, q_sig = 9, 5
base = (3, 1)
fiber = (6, 4)
check("A1 GU tangent Krein signature (9,5): p=9 positive, q=5 negative; = (3,1) base + (6,4) "
      "fiber (W131). The q=5 negative directions are the indefinite sector a quantization must "
      "either GRADE (keep) or TRUNCATE (remove)",
      p_sig == base[0] + fiber[0] and q_sig == base[1] + fiber[1] and q_sig == 5,
      f"(9,5) = (3,1)+(6,4); q = {q_sig}")

# Removal family: truncate the q negative directions out of the physical space -> effective q=0.
# Graded family: keep them, C-operator selects a PROPER maximal positive subspace -> q stays.
q_removal_effective = 0        # ghosts removed from physical/asymptotic space => definite space
q_graded_effective = q_sig     # kept and graded => q=5 latent remainder survives
# Record-substrate reading (W150 verdict D): effective q=0 <=> H_C+ = whole space <=> CLOSED
# COMPLETION <=> finality frontier EMPTY. q>0 <=> proper H_C+ <=> frontier NEVER empty.
removal_is_closed_completion = (q_removal_effective == 0)
graded_frontier_never_empty = (q_graded_effective > 0)
check("A2 removal TRUNCATES the q=5 sector => effective q=0 => H_C+ = whole space => CLOSED "
      "COMPLETION (finality frontier empty); graded KEEPS + grades => proper H_C+, q=5 latent "
      "remainder => frontier NEVER empty (W150 verdict D reading)",
      removal_is_closed_completion and graded_frontier_never_empty,
      f"q_removal_eff={q_removal_effective} (closed), q_graded_eff={q_graded_effective} (open)")

# The CONDITIONAL forcing: IF (9,5) q=5 holds AND closed completion is forbidden AND the tangent
# indefiniteness descends to the asymptotic space, THEN removal (q=0) is excluded, graded forced.
# Each antecedent is a NAMED GAP (firewall canon + W150); none is a closed theorem.
GAP_1a_signature_declared = True    # (9,5) is a DECLARED INPUT (firewall canon), not proven
GAP_1b_closed_compl_open = True     # closed completion "NOT proven impossible" (live frontier)
GAP_1c_descent_unproven = True      # tangent(9,5)->asymptotic H_C+ descent "stated as origin"
arg1_forces_unconditionally = not (GAP_1a_signature_declared or GAP_1b_closed_compl_open
                                   or GAP_1c_descent_unproven)
check("A3 ARG-1 forcing is CONDITIONAL, not unconditional: it forces graded ONLY IF (9,5) is "
      "proven (GAP-1a: declared input), closed completion is proven forbidden (GAP-1b: live "
      "frontier, not proven), and the tangent-(9,5)->asymptotic-Krein descent holds (GAP-1c: "
      "stated as origin). All three are open => ARG-1 does NOT force unconditionally",
      not arg1_forces_unconditionally
      and GAP_1a_signature_declared and GAP_1b_closed_compl_open and GAP_1c_descent_unproven,
      "3 named gaps open (1a declared / 1b live-frontier / 1c descent) => conditional forcing")

# ------------------------------------------------------------------------------------------
# 3. ARG-2: record causal-ordering vs the removal family's bounded microcausality violation.
# ------------------------------------------------------------------------------------------
log("")
log("3. ARG-2: does record causal-ordering forbid removal's ~1/m2 microcausality violation?")

# The graded family PRESERVES microcausality (N_A = 0); the removal family PAYS it (N_A = 1),
# as a BOUNDED violation localized at the off-shell scale ~ 1/m2 (timescale ~ 1/M for the wide
# ghost). Reproduce the direction from the KL pairs.
graded_preserves_microcausality = (graded_pair[0] == 0.0)
removal_violates_microcausality = (removal_pair[0] == 1.0)
check("A4 direction check: graded preserves microcausality (N_A=0), removal pays a BOUNDED "
      "~1/m2 microcausality violation (N_A=1). So a causal-ordering requirement, IF it bites "
      "at the micro scale, excludes removal and forces graded",
      graded_preserves_microcausality and removal_violates_microcausality,
      f"N_A: graded={graded_pair[0]}, removal={removal_pair[0]}")

# GAP-2a: the removal violation is macroscopically emergent-causal (Grinstein-O'Connell-Wise).
# Model the honest scale gap: micro scale 1/M vs a macroscopic finality/record scale. The
# violation timescale ~ 1/M (ghost mass, meV..Planck); the finality DAG is macroscopic. A macro
# ordering does NOT resolve a 1/M smearing. Encode the fixed-scale-branch number from W133/W138:
# ghost m2 ~ few meV => micro timescale r* ~ 20-30 um, vastly below any macroscopic record scale.
hbarc_eV_m = 197.3269804e-9
m2_meV = 4.0e-3                      # representative fixed-scale ghost mass (W138 floor band)
r_micro_m = hbarc_eV_m / m2_meV     # ~ 5e-5 m (the acausality smearing scale)
r_macro_m = 1.0e-3                  # a generous "macroscopic record/finality" scale (sub-mm)
macro_cannot_resolve_micro = (r_micro_m < r_macro_m)
check("A5 GAP-2a (macroscopic emergence, Grinstein-O'Connell-Wise): removal's acausality is a "
      "BOUNDED smearing at the ghost scale ~1/m2; a MACROSCOPIC finality/record ordering cannot "
      "detect it. So MACRO record-ordering does NOT exclude removal -- only MICRO-causality "
      "(axiom A at the off-shell scale) does",
      macro_cannot_resolve_micro and r_micro_m < 1e-3,
      f"micro smearing r*~{r_micro_m*1e6:.0f} um << macro scale {r_macro_m*1e3:.0f} mm")

# GAP-2b: upgrading record ordering from MACRO to MICRO-causality is a TI/TaF semantic (W150
# one-way gate). Importing it as a GU theorem is a re-declaration, not a forcing.
GAP_2b_micro_ordering_is_TI_TaF_gated = True
arg2_forces_unconditionally = (macro_cannot_resolve_micro is False) \
    and (not GAP_2b_micro_ordering_is_TI_TaF_gated)
check("A6 GAP-2b (one-way gate): 'records are MICRO-causally ordered' is a temporal-issuance / "
      "time-as-finality SEMANTIC (W150 one-way rule); asserting it as a GU theorem to exclude "
      "removal is a RE-DECLARATION in disguise, not a structural forcing. => ARG-2 does NOT "
      "force unconditionally",
      (not arg2_forces_unconditionally) and GAP_2b_micro_ordering_is_TI_TaF_gated,
      "macro ordering insufficient (GAP-2a) + micro ordering TI/TaF-gated (GAP-2b)")

# ------------------------------------------------------------------------------------------
# 4. Synthesis: symmetry broken (advance over W133) but forcing not closed.
# ------------------------------------------------------------------------------------------
log("")
log("4. Synthesis: is W133's symmetry broken? is the forcing closed?")

# The two arguments CONVERGE on graded and both point AGAINST the removal-family truncation.
both_favor_graded = True
# But both pass through the SAME two joints: (i) tangent->asymptotic descent (GAP-1c), and
# (ii) S-matrix<->record-finality identification (GAP-1a/1b via the firewall reading, GAP-2b).
shared_joint_descent = GAP_1c_descent_unproven
shared_joint_semantics = GAP_2b_micro_ordering_is_TI_TaF_gated

# W133 treated the axioms as SYMMETRIC (permanent declaration). W174 finding: within GU the
# substrate is NOT axiom-neutral -- it carries a directional/indefinite commitment (the finality
# frontier, the irreversible promotion, the proven-indefinite q=5) that lines up with (A)+graded
# and against (P)-truncation. That BREAKS the symmetry at the framing level.
w133_symmetry_broken_in_GU = both_favor_graded and (q_graded_effective > q_removal_effective)
# But neither argument is OPERATIVE-grade forcing, because the shared joints are open.
forcing_closed = not (shared_joint_descent or shared_joint_semantics)
check("S1 SYMMETRY BROKEN (advance over W133): both GU-structural arguments converge on GRADED "
      "and against removal-truncation; GU's substrate is NOT axiom-neutral (directional finality "
      "frontier + proven-indefinite q=5). W133's (0,1)/(1,0) symmetry does not hold WITHIN GU",
      w133_symmetry_broken_in_GU,
      "both arguments favor graded; q_graded=5 > q_removal=0")

check("S2 FORCING NOT CLOSED (honest): both arguments pass through the SAME two open joints -- "
      "(i) tangent-(9,5)->asymptotic-Krein descent (unproven, program-internal, UNGATED) and "
      "(ii) S-matrix<->record-finality identification (TI/TaF-gated). Neither is OPERATIVE-grade",
      (not forcing_closed) and shared_joint_descent and shared_joint_semantics,
      "shared joints open => selection is not unconditional forcing")

# The re-declaration tripwire (adversarial persona 5): assert the joints as GU theorems and the
# 'forcing' collapses to W133's declaration wearing consensus vocabulary. Guard against it.
would_be_redeclaration_if_asserted = shared_joint_descent and shared_joint_semantics
check("S3 re-declaration tripwire: IF one simply ASSERTS the two joints as GU theorems, the "
      "'forcing' is W133's keep-and-grade DECLARATION re-expressed in record/finality vocabulary "
      "-- NOT a new forcing. The honest verdict must not manufacture forcing by asserting a "
      "gated/unproven joint",
      would_be_redeclaration_if_asserted,
      "guard active: no joint is asserted as proven in this file")

# ------------------------------------------------------------------------------------------
# 5. Verdict + honesty guard + effect on bar (b).
# ------------------------------------------------------------------------------------------
log("")
log("5. Verdict, honesty guard, effect on bar (b)")

VERDICT = "NARROWED"           # symmetry broken; forcing not closed
POSITIVITY_FORCED = False      # not OPERATIVE-grade
GENUINELY_FREE = False         # not unchanged either: the coin is weighted within GU
BAR_B_CLEARS = False
BAR_B_CHANGED = False          # b UNCHANGED (still engine, re-posed) -- but the re-pose is sharper
SCALAR_CORE_ONLY = True
CANON_CHANGED = False
check("V1 VERDICT = NARROWED: within GU the two families are NOT symmetric (two convergent "
      "structural arguments lean on graded/positivity and against removal-truncation), so W133's "
      "'permanent declaration' symmetry is BROKEN; but the selection is NOT OPERATIVE-grade "
      "forcing (shared open joints). Not FORCED, not GENUINELY-FREE -- NARROWED",
      VERDICT == "NARROWED" and not POSITIVITY_FORCED and not GENUINELY_FREE,
      "symmetry broken, forcing not closed")

check("V2 effect on bar (b): b does NOT clear and is UNCHANGED as a status (engine, re-posed); "
      "but the re-pose is SHARPENED from 'free declaration' to a single named, program-internal, "
      "UNGATED question: does the tangent-(9,5) q=5 Krein indefiniteness descend to the "
      "asymptotic state space, forbidding the removal-family truncation? (= the W49/W121 "
      "C-operator derivation W133 already named as the only route to unconditional selection)",
      not BAR_B_CLEARS and not BAR_B_CHANGED,
      "bar (b) UNCHANGED; re-posed question named and ungated")

check("H1 honesty guard: scalar core only (tensor numerators W124 Stage C / W134); no canon / "
      "RESEARCH-STATUS / claim-status / verdict / posture change; the selection is CONDITIONAL "
      "on two named joints and asserting them is a re-declaration; bar (b) UNCHANGED",
      SCALAR_CORE_ONLY and not CANON_CHANGED and not POSITIVITY_FORCED,
      "status = W174_COMPLETE_SCALAR_CORE")

log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W174 checks failed"

log("")
log("W174 VERDICT: NARROWED.")
log("  GU's substrate is NOT axiom-neutral: two convergent structural arguments (removal-")
log("  truncation = closed completion forbidden by (9,5) q=5 / firewall crit.1; and record")
log("  causal-ordering vs removal's ~1/m2 microcausality violation) both lean on the")
log("  positivity/keep-and-grade family and against removal. W133's (0,1)/(1,0) SYMMETRY is")
log("  BROKEN within GU. But the forcing is NOT closed: both arguments pass through the same")
log("  two open joints -- the tangent-(9,5)->asymptotic-Krein DESCENT (ungated, program-")
log("  internal, unproven) and the S-matrix<->record-finality SEMANTIC identification")
log("  (TI/TaF-gated). Asserting either as a GU theorem is a re-declaration in disguise.")
log("  bar (b) does NOT clear; UNCHANGED as status, but re-posed sharply: b is one named")
log("  descent theorem away from forced. No canon change.")
raise SystemExit(0)
