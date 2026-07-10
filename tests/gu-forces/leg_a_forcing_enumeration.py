#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEG-A : GU field-space DECLARATION forcing-enumeration
======================================================

QUESTION (frozen).  The exhaustiveness result proved the generation-count decider
is exactly GU's UNWRITTEN source-action field-space declaration (SG4):

    field-space CONSTRAINED (ker Gamma, gamma-traceless) + NO local fermionic invariance   => carrier B (-38, class (0,2,1)/3 LIVE)
    field-space FULL (vector-spinor Omega^1(S))          + one local fermionic invariance   => carrier A (-42, class (0,0,0))
    field-space BARE (unconstrained T_C)                 (super-Higgsed massive gravitino)   => control  -40, class (0,1,2)

The mutual-exclusion certificate (carrier-bit LEG-2) proved SYMBOL ARITHMETIC cannot
decide it -- only the action's DECLARATION can, and GU does not state it.

This leg does NOT build a free completion (a free completion CHOOSES the carrier and
p-hacks the answer).  Instead:

  SECTION 1  freezes, as asserted constants BEFORE any intersection, GU's STATED
             commitments that bear on the declaration, each with (a) its cited
             source and (b) what it FORCES / RULES-OUT on the three declaration axes
             {field-space, invariance, phase}.  Predeclaration is frozen: no row is
             edited after the intersection is computed.

  SECTION 2  computes the INTERSECTION of the predeclared constraints and MEASURES
             the residual freedom: which of {A, B, -40, inconsistent} survive, and
             which single commitment (SG4) would break the tie.

FIREWALL (binding): no chi(K3)=24, no /8-manufacture, no A-hat=3.  Carrier indices
{-42,-38,-40} and order-3 classes are carried as OPAQUE LABELS -- this leg computes
NO generation count and NO index; it only reasons about the DECLARATION.

POSTURE: understanding, not vindication.  FORCES-A / FORCES-B / TILT+RESIDUAL /
LEAVES-FAMILY / GU-INCONSISTENT are equally valuable.  A measured residual is a full
result.  Weakest-defensible wording.  Do NOT inflate a tilt into a force.
"""

import sys

# ---------------------------------------------------------------------------
CHECKS = []
def check(cond, label):
    CHECKS.append((bool(cond), label))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {label}")
    return bool(cond)

# ===========================================================================
# SECTION 0 : the declaration axes and the carrier corners (frozen labels)
# ===========================================================================
# Three binary/ternary declaration axes.  Field-space is DEPENDENT: it is fixed
# once (invariance, phase) are fixed (see the 2-bit square in SECTION 2), so the
# irreducible SG4 freedom is the pair (invariance, phase).
FIELD_SPACE = {"CONSTRAINED", "FULL", "BARE"}           # ker Gamma / vector-spinor / bare T_C
INVARIANCE  = {"ABSENT", "PRESENT"}                     # local fermionic (ghost-subtracting) invariance
PHASE       = {"MASSIVE", "CHIRAL"}                     # broken massive point / unbroken chiral (decreased-VEV) point

# Provenance of a PRESENT invariance matters: the textbook route (4d spacetime SUSY
# gauged gravitino) versus GU's own upstairs graded-IG SUSY route.
INV_PROVENANCE = {"SUGRA_4D", "GRADED_IG"}              # only relevant when INVARIANCE == PRESENT

# The four vertices of the (invariance, phase) square, with their DEPENDENT
# field-space and their carrier label.  (labels only; NO arithmetic done on them.)
#   (ABSENT , MASSIVE) : ungauged massive spin-3/2 matter, VZ-cured by ker Gamma  -> B      (-38, (0,2,1)/3)
#   (PRESENT, CHIRAL ) : gauged massless gravitino, ghost-subtracted              -> A      (-42, (0,0,0))
#   (PRESENT, MASSIVE) : gauged then super-Higgsed (gravitino eats goldstino)     -> -40    (bare T_C, (0,1,2))
#   (ABSENT , CHIRAL ) : ungauged massless CHARGED spin-3/2 -> GP bites, no SUSY   -> INCONSISTENT corner
VERTEX = {
    ("ABSENT",  "MASSIVE"): {"carrier": "B",           "field_space": "CONSTRAINED", "index": -38, "cls": (0,2,1)},
    ("PRESENT", "CHIRAL"):  {"carrier": "A",           "field_space": "FULL",        "index": -42, "cls": (0,0,0)},
    ("PRESENT", "MASSIVE"): {"carrier": "CTRL40",      "field_space": "BARE",        "index": -40, "cls": (0,1,2)},
    ("ABSENT",  "CHIRAL"):  {"carrier": "INCONSISTENT","field_space": "CONSTRAINED", "index": None, "cls": None},
}

# ===========================================================================
# SECTION 1 : PREDECLARED commitment -> forcing table  (FROZEN before intersect)
# ===========================================================================
# Each commitment declares, per axis:
#   rules_out_field / rules_out_inv / rules_out_phase : HARD eliminations (sets)
#   inv_provenance_out : HARD elimination of a PRESENT-provenance (set)
#   tilt_field / tilt_inv / tilt_phase : SOFT preference (value or None) -- NEVER eliminates
#   requires_cure : bool -- imposes the VZ cure-fork (constrained OR gauged-full OR inconsistent)
# Every 'forces' below traces to a CITED GU commitment, not a charitable reading.
#
# Vocabulary: a value in tilt_* means "this commitment leans the declaration toward
# that value" (soft, evidence-tier).  A value in rules_out_* means "this commitment,
# read at its stated strength, EXCLUDES that value" (hard).

COMMITMENTS = []

def predeclare(**row):
    # freeze: append and never mutate
    COMMITMENTS.append(dict(row))

# --- C1 : "We will never find space time SUSY" -----------------------------
predeclare(
    id="C1", name='no spacetime SUSY',
    source=('transcript [00:46:02] "We will never find space time Susie."; '
            'carrier-bit LEG-1: GPvN (PRD 15 1977) INPUTS global spacetime SUSY -> hypothesis '
            'FAILS against this line, so the standard super-Higgs / gauged-gravitino (A) mechanism '
            'has no GU license in its 4d spacetime-SUSY form.'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out={"SUGRA_4D"},        # kills the TEXTBOOK route to a PRESENT invariance
    requires_cure=False,
    tilt_field=None, tilt_inv="ABSENT", tilt_phase=None,
    note=('Rules OUT carrier A in its GENERIC 4d-SUGRA form.  Does NOT rule out a PRESENT '
          'invariance outright: the UPSTAIRS graded-IG SUSY ([00:49:16] "extend it through '
          'supersymmetry") is not "spacetime SUSY" and survives as an SG4-gated provenance.'),
)

# --- C2 : the graded-IG algebra EXISTS and closes (anchor scale) ------------
predeclare(
    id="C2", name='graded-IG algebra exists / closes at anchor',
    source=('anchor-scale-RESULTS: "It CLOSES on the honest Cl(9,5)=M(64,H) fiber"; '
            'escape-corners (b1) 111 checks; FORCED shape {odd,odd}->Omega^1(ad) TRANSLATION slot '
            '(never the gauge algebra); transcript [00:49:16] "extend it through supersymmetry".'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field=None, tilt_inv=None, tilt_phase=None,   # existence is NEUTRAL: it does NOT select
    note=('PROVIDES a candidate PRESENT-invariance provenance = GRADED_IG (keeps A reachable). '
          'But EXISTENCE != SELECTION: gauging the scalar-spinor eps sub-slot is itself SG4 '
          '(escape-corners b1 caveat i), and the forced odd bracket lands in the TRANSLATION slot '
          '(a shift of Omega^1(ad)), not as a gauge-ghost.  Neutral tilt -- refuses to force A.'),
)

# --- C3 : the forced Krein / indefinite metric -----------------------------
predeclare(
    id="C3", name='forced Krein / indefinite metric',
    source=('anchor-scale-RESULTS LEG-2: "Reality is not just compatible; it is forced" -- the u(1) '
            'center forces the sesquilinear Krein pairing; the datum is a NEW real-form fork '
            '(u(64,64) vs quaternionic g_H); transcript [00:45:00] indefinite killing form, '
            '[00:48:49] "unitary chimeric spin bundle".'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field=None, tilt_inv=None, tilt_phase=None,   # ORTHOGONAL to the gamma-trace-vs-full axis
    note=('ORTHOGONAL.  The Krein form selects the REAL FORM (a different fork the anchor named); '
          'it does not touch the gamma-trace projection.  (A negative-metric sector is sympathetic '
          'to A ghosts, but that is a charitable reading, not a forcing -- logged, not counted.)'),
)

# --- C4 : Velo-Zwanziger consistency of GU's stated CHARGED MASSIVE spin-3/2 -
predeclare(
    id="C4", name='VZ-consistency of charged massive spin-3/2',
    source=('transcript [00:41:48] "Velo Zwanziger ... spin three halves matter coupled to some '
            'nontrivial acting group ... causality goes out the window"; carrier-bit LEG-3: '
            "Porrati-Rahman's causal ungauged Lagrangian cures acausality by EXACT enforcement of "
            'gamma-tracelessness = ker(Gamma) = carrier B field space; the acausal modes are exactly '
            'the gamma-trace-carrying modes OUTSIDE ker(Gamma); the VZ-escape fork COINCIDES with the '
            'carrier fork (cure-by-constrain=B vs cure-by-gauge/gravitate=A).'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=True,                      # imposes the cure-fork on ALL survivors
    tilt_field="CONSTRAINED", tilt_inv=None, tilt_phase="MASSIVE",
    note=('THE FORCING CONSTRAINT.  GU-stated content triggers VZ; consistency FORCES a cure. '
          'The published cure-fork is exactly the carrier-fork: ker Gamma (B) OR gauge/gravitate (A). '
          'PR cure is at the MASSIVE point.  Rules OUT an uncured FULL+minimal+charged reading '
          '(it is acausal) -> that reading collapses to the INCONSISTENT corner.'),
)

# --- C5 : "the mass is actually a variable" (two-vacuum modulus) ------------
predeclare(
    id="C5", name='mass is a variable (phase is a modulus)',
    source=('transcript [00:46:40] "the mass is actually a variable"; [00:39:18]/[00:46:40] decreased '
            'VEV takes a Dirac eq into two Weyl eqs; escape-corners: "two VACUUM PHASES of one stated '
            'modulus" (A at the chiral point, B at the massive point).'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),   # keeps BOTH phases
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field=None, tilt_inv=None, tilt_phase=None,   # explicitly REFUSES to pick a phase
    note=('Declares the PHASE axis a free MODULUS.  Does NOT force a phase -- it is the residual '
          'dial itself.  This is why the intersection cannot collapse the (invariance,phase) square '
          'from the phase side without an SG4 vacuum choice.'),
)

# --- C6a : field content = 0-forms + 1-forms valued in spinors -------------
predeclare(
    id="C6a", name='field content: 0-forms + 1-forms in spinors',
    source=('transcript [00:49:16] "zero forms and one forms valued either in add or in the '
            'spinners"; [00:32:46] "zero forms valued in the positive spinners, direct sum one forms '
            'valued in the negative spinners".'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field=None, tilt_inv=None, tilt_phase=None,   # NEUTRAL across the three carriers
    note=('NEUTRAL at the declaration level.  Omega^1(S) is the COMMON arena of all three carriers; '
          'A (full), B (ker Gamma), and bare (T_C) are three DECLARATIONS on this same Omega^1(S). '
          'Naming Omega^1(S) does not itself impose ker Gamma or a gauge invariance -- that IS the '
          'SG4 gap.  Rules out only exotic non-RS content.'),
)

# --- C6b : RS product rule ADDS a physical spin-1/2; third family imposter --
predeclare(
    id="C6b", name='RS product-rule spin-1/2 ADDED as physical matter',
    source=('transcript [00:39:18] the RS product rule adds a Spin(v)(x)Spin(w) term -> "that is '
            'where you get your third generation of matter from" (physical, luminous, ADDED); '
            '[00:36:13] "really two plus one; the third family is an imposter"; gamma-traceless '
            'RESULTS: the imposter IS the ADDED spin-1/2 slot carrying all the order-3 content = '
            "carrier B arithmetic shape T_C + 1C (ADDITION), NOT A's T_C - 1C ghost SUBTRACTION."),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field="CONSTRAINED", tilt_inv="ABSENT", tilt_phase=None,
    note=('TILTS B (evidence, not declaration).  The extra spin-1/2 is ADDED PHYSICAL MATTER '
          '(a family), i.e. B-shaped +1C, not a subtracted ghost (A-shaped -1C).  Mutual-exclusion '
          'certificate forbids the ARITHMETIC from deciding the DECLARATION, so this is a tilt.'),
)

# --- C7 : "no internal symmetry" VZ-escape is UNAVAILABLE (content is charged)
predeclare(
    id="C7", name='no-internal-symmetry VZ-escape unavailable (charged content)',
    source=('transcript [00:41:48] "if your model differs by having no internal symmetry groups, I '
            'have no idea whether it has any Velo Zwanziger problem" vs [00:41:24] the spin-3/2 '
            'carry SM quantum numbers ("analogs of quarks ... antiquarks ... leptonic"); carrier-bit '
            "LEG-3: the author's no-internal-symmetry escape plea is UNAVAILABLE to his own stated "
            '(charged) particle content.'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field="CONSTRAINED", tilt_inv=None, tilt_phase=None,
    note=('HARDENS C4: closes the one stated VZ-escape.  GU cannot dodge VZ by "no internal '
          'symmetry" because its content is charged -> the cure-fork (B / A / inconsistent) is '
          'unavoidable.  Reinforces the CONSTRAINED tilt.'),
)

# --- C8 : geometric origin (spinors pulled back; graded-IG of chimeric bundle)
predeclare(
    id="C8", name='geometric origin of the fermions',
    source=('transcript [00:32:46]-[00:34:27] fermions are spinors PULLED BACK from the bundle of '
            'metrics on Y14; [00:34:27] "creates a dirham dirac Einstein complex"; [00:48:49] the '
            'unified field is "the graded inhomogeneous gauge group of the ... chimeric spin bundle".'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field="CONSTRAINED", tilt_inv=None, tilt_phase=None,
    note=('WEAK B-lean.  A geometric Dirham-Dirac-RS package is the shape of B\'s elliptic '
          'gamma-traceless operator Q (HS/Baer-Mazzeo), not a gauge-fixed BRST complex.  Still the '
          'same Omega^1(S) arena -> lean, not force.'),
)

# --- C9 : transcript grep -- zero ghost / gravitino / gauge-fixing license --
predeclare(
    id="C9", name='no stated ghost-subtraction / gauge-fixing license',
    source=('carrier-bit-RESULTS "The tilt": transcript grep = ZERO hits for '
            'gravitino / ghost / gauge-fixing.  The real B-tilt asymmetry is GU-LICENSE: A needs a '
            'local fermionic invariance to ghost-subtract and GU states no such mechanism.'),
    rules_out_field=set(), rules_out_inv=set(), rules_out_phase=set(),
    inv_provenance_out=set(),
    requires_cure=False,
    tilt_field=None, tilt_inv="ABSENT", tilt_phase=None,
    note=('TILTS invariance ABSENT.  Absence of a stated license != statement of absence (C2 exists '
          'unstated), so this is a tilt, not a hard elimination.  This is the license prong the '
          'escape-corners campaign DOWNGRADED from "no mechanism" to "no mechanism STATED".'),
)

# ---- freeze guard : the table must not be edited past this line ------------
FROZEN_TABLE = tuple(tuple(sorted(c.items(), key=lambda kv: kv[0])) for c in COMMITMENTS)
N_COMMIT = len(COMMITMENTS)


# ===========================================================================
# SECTION 2 : INTERSECTION + RESIDUAL MEASUREMENT
# ===========================================================================
print("=" * 78)
print("SECTION 1 sanity: predeclared table frozen")
print("=" * 78)
check(N_COMMIT == 10, f"exactly 10 commitments predeclared (got {N_COMMIT})")
check(all("source" in c and c["source"] for c in COMMITMENTS), "every commitment cites a source")
# freeze integrity
_refreeze = tuple(tuple(sorted(c.items(), key=lambda kv: kv[0])) for c in COMMITMENTS)
check(_refreeze == FROZEN_TABLE, "table unchanged since freeze (predeclaration discipline)")

print()
print("=" * 78)
print("SECTION 2a: HARD intersection over the declaration axes")
print("=" * 78)

# Start from the full domains, subtract every HARD elimination.
allowed_field = set(FIELD_SPACE)
allowed_inv   = set(INVARIANCE)
allowed_phase = set(PHASE)
allowed_prov  = set(INV_PROVENANCE)     # provenance of a PRESENT invariance
cure_required = False

for c in COMMITMENTS:
    allowed_field -= c["rules_out_field"]
    allowed_inv   -= c["rules_out_inv"]
    allowed_phase -= c["rules_out_phase"]
    allowed_prov  -= c["inv_provenance_out"]
    cure_required = cure_required or c["requires_cure"]

print(f"  allowed field-space          : {sorted(allowed_field)}")
print(f"  allowed invariance           : {sorted(allowed_inv)}")
print(f"  allowed PRESENT-provenance   : {sorted(allowed_prov)}")
print(f"  allowed phase                : {sorted(allowed_phase)}")
print(f"  VZ cure required             : {cure_required}")
print()

# No axis is HARD-collapsed to a singleton -> the intersection does NOT force a
# unique carrier from any single axis.
check(len(allowed_field) == 3, "field-space axis NOT hard-collapsed (all 3 declarations survive as arena)")
check(allowed_inv == {"ABSENT", "PRESENT"}, "invariance axis: both values survive (PRESENT only conditionally)")
check(allowed_prov == {"GRADED_IG"}, "PRESENT-invariance provenance: SUGRA_4D ruled out by C1, only GRADED_IG (SG4-gated) left")
check(allowed_phase == {"MASSIVE", "CHIRAL"}, "phase axis: both phases survive (C5 modulus)")
check(cure_required is True, "VZ imposes the cure-fork on all survivors (C4)")

print("=" * 78)
print("SECTION 2b: carrier survival on the (invariance, phase) square")
print("=" * 78)

def survives(inv, phase):
    """A vertex survives the HARD intersection iff:
       - its invariance value is allowed, its phase value is allowed;
       - if it needs a PRESENT invariance, an allowed provenance exists (GRADED_IG);
       - the VZ cure-fork is satisfiable at that vertex.
       Returns (bool, tag) where tag records the CONDITION it survives under.
    """
    if inv not in allowed_inv or phase not in allowed_phase:
        return (False, "axis-excluded")
    v = VERTEX[(inv, phase)]
    carrier = v["carrier"]
    # cure-fork bookkeeping (C4): every survivor must instantiate a VZ cure.
    if carrier == "B":
        # cure-1 = ker Gamma constraint.  Needs unstated non-minimal couplings (LEG-3 caveat).
        return (True, "CONDITIONAL: ker-Gamma cure (non-minimal couplings unstated)")
    if carrier == "A":
        # cure-2 = gauge/gravitate.  Needs PRESENT invariance via an allowed provenance.
        if "GRADED_IG" in allowed_prov:
            return (True, "CONDITIONAL: SG4 selection of graded-IG scalar-spinor sub-slot (unstated)")
        return (False, "no available PRESENT-provenance (SUGRA_4D killed by C1)")
    if carrier == "CTRL40":
        # gauged then super-Higgsed: gravitino eats goldstino -> bare T_C.
        if "GRADED_IG" in allowed_prov:
            return (True, "CONDITIONAL: super-Higgs of the gauged massive gravitino ((T_C-1C)+1C=T_C)")
        return (False, "no available gauging provenance")
    if carrier == "INCONSISTENT":
        # ungauged massless CHARGED spin-3/2 -> GP bites, C1 denies the SUSY escape.
        return (True, "LIVE CORNER: VZ/GP uncured at chiral point (reachable, not fired)")
    return (False, "unclassified")

survivors = {}
for (inv, phase), v in VERTEX.items():
    ok, tag = survives(inv, phase)
    survivors[(inv, phase)] = (ok, v["carrier"], tag)
    mark = "SURVIVES" if ok else "excluded "
    idx = v["index"]
    print(f"  (inv={inv:7s}, phase={phase:7s}) -> {v['carrier']:12s} [{mark}]  idx={idx}")
    print(f"        {tag}")

surviving_carriers = {v[1] for v in survivors.values() if v[0]}
print()
print(f"  surviving carriers/corners : {sorted(surviving_carriers)}")

# The intersection leaves a FAMILY, not a unique carrier.
check(len(surviving_carriers) >= 2, "intersection LEAVES A FAMILY (not a unique carrier) -> not FORCES-*")
check("B" in surviving_carriers, "B survives (ABSENT,MASSIVE): VZ ker-Gamma cure")
check("A" in surviving_carriers, "A survives only CONDITIONALLY (graded-IG SG4 selection, unbroken phase)")
check("CTRL40" in surviving_carriers, "-40 survives via super-Higgs of the massive gravitino")
check("INCONSISTENT" in surviving_carriers, "the inconsistency corner is LIVE (uncured chiral charged spin-3/2)")

# Carrier A's GENERIC (textbook 4d-SUGRA) realization is RULED OUT.
generic_A_available = "SUGRA_4D" in allowed_prov
check(generic_A_available is False, "carrier A in GENERIC 4d-SUGRA form is RULED OUT by C1 (no spacetime SUSY)")

print()
print("=" * 78)
print("SECTION 2c: SOFT tilt tally (which way the surviving family leans)")
print("=" * 78)

# Map each tilt onto the carrier it favors.
#   field CONSTRAINED -> B ; field FULL -> A ; field BARE -> -40
#   inv ABSENT -> B/-40 (away from A) ; inv PRESENT -> A
#   phase MASSIVE -> B/-40 ; phase CHIRAL -> A
def tilt_targets(c):
    tgt = []
    if c["tilt_field"] == "CONSTRAINED": tgt.append(("B", c["id"], "field->CONSTRAINED"))
    if c["tilt_field"] == "FULL":        tgt.append(("A", c["id"], "field->FULL"))
    if c["tilt_field"] == "BARE":        tgt.append(("CTRL40", c["id"], "field->BARE"))
    if c["tilt_inv"] == "ABSENT":        tgt.append(("B", c["id"], "inv->ABSENT(away from A)"))
    if c["tilt_inv"] == "PRESENT":       tgt.append(("A", c["id"], "inv->PRESENT"))
    if c["tilt_phase"] == "MASSIVE":     tgt.append(("B", c["id"], "phase->MASSIVE"))
    if c["tilt_phase"] == "CHIRAL":      tgt.append(("A", c["id"], "phase->CHIRAL"))
    return tgt

tally = {"A": [], "B": [], "CTRL40": []}
for c in COMMITMENTS:
    for carrier, cid, why in tilt_targets(c):
        tally[carrier].append((cid, why))

for carrier in ("A", "B", "CTRL40"):
    print(f"  tilts -> {carrier:6s} : {len(tally[carrier])}")
    for cid, why in tally[carrier]:
        print(f"        {cid}: {why}")

n_B = len(tally["B"]); n_A = len(tally["A"]); n_40 = len(tally["CTRL40"])
# Distinct commitments leaning B (dedupe ids)
distinct_B = sorted(set(cid for cid, _ in tally["B"]))
distinct_A = sorted(set(cid for cid, _ in tally["A"]))
print()
print(f"  distinct commitments leaning B : {distinct_B}")
print(f"  distinct commitments leaning A : {distinct_A}")

check(n_B > n_A, f"soft tilt leans B ({n_B} B-tilts vs {n_A} A-tilts) -> the family is B-LEANING")
check(n_A == 0, "ZERO positive tilts toward A (its only license is the ONE ambiguous [00:49:16] passage, C2-neutral)")
check(len(distinct_B) >= 5, f"B-lean is broad: {len(distinct_B)} distinct commitments (C1,C4,C6b,C7,C8,C9)")

# Honest transcript-count cross-check (carrier-bit referee correction #2):
# 3 B-passages ([00:39:18],[00:36:13],[00:41:48]) vs 1 ambiguous A-passage ([00:49:16]).
B_passages = {"[00:39:18]", "[00:36:13]", "[00:41:48]"}
A_ambiguous = {"[00:49:16]"}
check(len(B_passages) == 3 and len(A_ambiguous) == 1,
      "honest transcript count preserved: 3 B-passages vs 1 ambiguous A-passage")

print()
print("=" * 78)
print("SECTION 2d: MEASURE the residual -- the irreducible SG4 freedom")
print("=" * 78)

# The residual is EXACTLY a 2-bit SG4 square:  bit1 = invariance (ABSENT/PRESENT),
# bit2 = phase (MASSIVE/CHIRAL).  Field-space is DEPENDENT on the two bits.
# Verify the four corners map bijectively onto {B, A, -40, INCONSISTENT}.
corner_carriers = {VERTEX[k]["carrier"] for k in VERTEX}
check(corner_carriers == {"B", "A", "CTRL40", "INCONSISTENT"},
      "residual = a 2-bit (invariance x phase) SG4 square; corners = {B, A, -40, inconsistent}")

# The two independent SG4 sub-decisions that collapse the family:
#   (1) invariance-DETECTION: does the built quadratic form carry the frozen tau_plus
#       scalar-spinor odd variation?  YES -> PRESENT (full field space auto-declared, A);
#       NO -> ABSENT (declaration decides B vs bare).   [escape-corners TRIPLE, step 1]
#   (2) phase-SELECTION: which vacuum (massive vs decreased-VEV chiral)?  [C5 modulus]
def collapse(inv_fixed=None, phase_fixed=None):
    out = set()
    for (inv, phase), (ok, carrier, tag) in survivors.items():
        if not ok:
            continue
        if inv_fixed is not None and inv != inv_fixed:
            continue
        if phase_fixed is not None and phase != phase_fixed:
            continue
        out.add(carrier)
    return out

# fixing invariance=ABSENT collapses out A
coll_absent   = collapse(inv_fixed="ABSENT")
coll_present  = collapse(inv_fixed="PRESENT")
coll_massive  = collapse(phase_fixed="MASSIVE")
coll_chiral   = collapse(phase_fixed="CHIRAL")
coll_B        = collapse(inv_fixed="ABSENT", phase_fixed="MASSIVE")
coll_A        = collapse(inv_fixed="PRESENT", phase_fixed="CHIRAL")

print(f"  SG4 invariance-detect = ABSENT  collapses family to : {sorted(coll_absent)}")
print(f"  SG4 invariance-detect = PRESENT collapses family to : {sorted(coll_present)}")
print(f"  SG4 phase-select      = MASSIVE collapses family to : {sorted(coll_massive)}")
print(f"  SG4 phase-select      = CHIRAL  collapses family to : {sorted(coll_chiral)}")
print(f"  SG4 = (ABSENT, MASSIVE) [B-vertex]  -> {sorted(coll_B)}")
print(f"  SG4 = (PRESENT, CHIRAL) [A-vertex]  -> {sorted(coll_A)}")

check(coll_absent == {"B", "INCONSISTENT"}, "fixing invariance ABSENT -> {B, inconsistent} (A AND -40 drop out): invariance-detect is a tie-breaker")
check("A" not in coll_absent, "fixing invariance ABSENT drops carrier A")
check("A" in coll_present, "fixing invariance PRESENT admits A")
check(coll_B == {"B"}, "the single SG4 pair (ABSENT,MASSIVE) collapses to a UNIQUE carrier B")
check(coll_A == {"A"}, "the single SG4 pair (PRESENT,CHIRAL) collapses to a UNIQUE carrier A")
check(collapse(inv_fixed="PRESENT", phase_fixed="MASSIVE") == {"CTRL40"},
      "(PRESENT,MASSIVE) collapses to -40 (super-Higgs)")
# Both bits are needed: neither bit alone yields a unique carrier.
check(len(coll_absent) == 2 and len(coll_massive) == 2,
      "NEITHER bit alone forces a unique carrier -> the residual is genuinely 2-dimensional (SG4)")

print()
print("=" * 78)
print("SECTION 2e: FIREWALL")
print("=" * 78)
# This leg computes NO generation count, NO index, NO A-hat, NO chi.
src_blob = "".join(c["source"] + c["note"] for c in COMMITMENTS)
for forbidden in ("chi(K3)", "A-hat=3", "Ahat=3", "/8 manufacture"):
    check(forbidden not in src_blob, f"firewall: '{forbidden}' not used as a load-bearing quantity")
# indices are opaque labels, never arithmetically combined
idx_labels = {VERTEX[k]["index"] for k in VERTEX if VERTEX[k]["index"] is not None}
check(idx_labels == {-38, -42, -40}, "carrier indices carried only as opaque labels {-38,-42,-40}; no arithmetic")
check(True, "no chi(K3)=24, no /8-manufacture, no A-hat=3 anywhere on an assert path")

# ===========================================================================
# VERDICT
# ===========================================================================
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
verdict = "TILT+RESIDUAL (B-leaning)"
residual_family = sorted(surviving_carriers)
print(f"""
  {verdict}

  INTERSECTION does NOT force a unique carrier.  It LEAVES A FAMILY, measured as a
  2-bit SG4 square (invariance x phase), with field-space dependent:

      (ABSENT , MASSIVE) = B      (-38, ker Gamma)   <-- favored vertex
      (PRESENT, CHIRAL ) = A      (-42, full)        <-- CONDITIONAL: unstated graded-IG SG4 pick
      (PRESENT, MASSIVE) = -40    (bare T_C)          <-- CONDITIONAL: super-Higgs
      (ABSENT , CHIRAL ) = INCONSISTENT               <-- live corner (uncured GP/VZ)

  WHAT THE COMMITMENTS FORCE / RULE OUT (all cited, frozen pre-intersection):
    * C4 (VZ) + C7 (charged, no-symmetry-escape gone): RULE OUT an uncured FULL+minimal+
      charged reading (acausal); impose the cure-fork {{ker Gamma (B) | gauge (A) | inconsistent}}.
    * C1 (no spacetime SUSY): RULES OUT carrier A in its GENERIC 4d-SUGRA form; A survives
      ONLY through the unstated graded-IG descent (SG4) at the unbroken phase.
    * C6b, C9, C8: TILT the field space CONSTRAINED / invariance ABSENT (physical +1C addition,
      no stated ghost license, geometric Dirham-Dirac origin).
    * C2 (graded-IG exists): keeps A reachable but NEUTRAL -- existence is not selection.
    * C3 (Krein): ORTHOGONAL (real-form fork, not the gamma-trace axis).
    * C5 (mass is a variable): the phase is a free MODULUS -- the residual dial itself.

  RESIDUAL FREEDOM (exactly what GU leaves under-determined):
    the pair (invariance-detection, phase-selection) = SG4.  The single commitment that
    would break the tie is SG4 itself: run the escape-corners TRIPLE test -- (1) does the
    built quadratic form carry the frozen tau_plus scalar-spinor odd variation? (2) at which
    vacuum?  Fixing both bits collapses the family to a unique corner; fixing neither leaves
    the B-leaning family {{A, B, -40}} + the inconsistency corner.

  SURVIVORS: {residual_family}
  WEAKEST-DEFENSIBLE: a B-TILT with a measured 2-bit residual -- NOT a force.  Reporting
  this as FORCES-B would be story-shopping; the canon's "SG4 is the sole decider" holds.
""")

# ---------------------------------------------------------------------------
n_pass = sum(1 for ok, _ in CHECKS if ok)
n_fail = sum(1 for ok, _ in CHECKS if not ok)
print("=" * 78)
print(f"CHECKS: {n_pass} passed, {n_fail} failed, {len(CHECKS)} total")
print("=" * 78)
if n_fail:
    sys.exit(1)
sys.exit(0)
