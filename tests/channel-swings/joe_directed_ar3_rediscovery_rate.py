#!/usr/bin/env python3
"""AR-3 rediscovery-rate probe — recompute the re-derivation rate mechanically
from a DECLARED cluster list, and prove the certificate has power.

Companion artifact:
`lab/active-research/joe-directed/archaeology/ar3-rediscovery-rate-2026-08-15.md`

Run FROM THE REPO ROOT:

    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ar3_rediscovery_rate.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ar3_rediscovery_rate.py --selftest

WHAT THIS COMPUTES
------------------
1. The DENOMINATOR, from the filesystem: the dated artifacts of the
   Joe-directed channel in the window 2026-08-14..2026-08-15.  A PINNED list of
   44 paths is asserted to exist exactly; the live count is asserted only as a
   FLOOR, because the checkout is shared with concurrent agents who can only
   raise it.
2. Every declared cluster is VERIFIED against the repository before it is
   allowed to contribute to any numerator:
     - both files exist;
     - the filename date matches the declared date and the ordering is right;
     - the declared ANCHOR string is actually present in BOTH files, searched
       on WHITESPACE-NORMALISED text (see §3);
     - the declared citation status is re-derived, not trusted: the probe reads
       the later file and checks whether the earlier owner is named.
3. The HARD-WRAP result: RB1's operative sentence is invisible to line-based
   `grep` and visible to normalised search.  Asserted both ways.
4. The METACHARACTER result: the string `MET(X^{1,3})` is present in the corpus
   and returns ZERO hits under a default regex search, because `{1,3}` is an
   interval quantifier.  Asserted both ways.
5. The RATE under FOUR inclusion rules, as exact `fractions.Fraction`.  A
   single number with no sensitivity analysis is not a measurement, so the
   spread is part of the output, not a footnote.

EXACTNESS
---------
Every asserted quantity is an int or a `fractions.Fraction`.  `assert_no_float`
sweeps the whole result dict and the module source is checked for float
literals.  No tolerance band is used anywhere: a tolerance that swallows a
planted control is the defect this gate family exists to detect.

WHAT THIS DOES NOT DO
---------------------
* It does not discover clusters.  The cluster list is a DECLARED, human-audited
  object; this probe recomputes the arithmetic over it and verifies each row
  against the files.  A cluster the sweep missed is invisible here, and the
  artifact says so.
* It does not adjudicate any GU physics claim, move any ledger row, or
  transport any comparator result across the source-native boundary.
* It does not assert that the classification of any cluster as REDERIVED
  rather than REPRODUCED is correct.  It asserts that the classification is
  DECLARED, that its stated textual evidence EXISTS, and that the arithmetic
  over the declaration is right.  That distinction is the whole measurement.
"""

from __future__ import annotations

import os
import re
import sys
from fractions import Fraction

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CHECKS: list[tuple[str, str, bool, str]] = []


def E(name: str, ok: bool, detail: str = "") -> None:
    """Exact result: must hold."""
    CHECKS.append(("E", name, bool(ok), detail))


def C(name: str, holds: bool, detail: str = "") -> None:
    """Planted control: `holds` must be FALSE, i.e. the certificate has power."""
    CHECKS.append(("C", name, not bool(holds), detail))


def assert_no_float(obj, path: str = "$") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"FLOAT FOUND at {path}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(k, f"{path}.<key>")
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple, set, frozenset)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# --------------------------------------------------------------------------
# 0. text access.  NORMALISED = whitespace collapsed.  This is load-bearing:
#    the corpus is hard-wrapped, so a line-based search cannot see a sentence
#    that crosses a newline.  Cluster K1 exists because of exactly that.
# --------------------------------------------------------------------------

_RAW: dict[str, str] = {}
_NORM: dict[str, str] = {}


def raw(rel: str) -> str:
    if rel not in _RAW:
        with open(os.path.join(REPO, rel), encoding="utf-8", errors="ignore") as fh:
            _RAW[rel] = fh.read()
    return _RAW[rel]


def norm(rel: str) -> str:
    if rel not in _NORM:
        _NORM[rel] = re.sub(r"\s+", " ", raw(rel))
    return _NORM[rel]


def exists(rel: str) -> bool:
    return os.path.isfile(os.path.join(REPO, rel))


def file_date(rel: str) -> str | None:
    m = re.findall(r"(20\d\d-\d\d-\d\d)", os.path.basename(rel))
    return m[-1] if m else None


def days_between(d0: str, d1: str) -> int:
    from datetime import date

    a = date(*(int(x) for x in d0.split("-")))
    b = date(*(int(x) for x in d1.split("-")))
    return (b - a).days


ID_SHAPE = re.compile(r"^(?:[A-Za-z]{1,3}-?[A-Za-z]?\d{1,3}[a-z]?|[a-z]{2}-[a-z])$")

# Wave/programme prefixes that name a CAMPAIGN, not an artifact.  Matching
# these would let "k77" in a later file count as a citation of any one of the
# ~200 k77 artifacts.  That false positive would erase the K6 finding, so it is
# excluded explicitly and the exclusion is itself a planted control.
WAVE_PREFIXES = frozenset({"k77", "k78", "k79", "k80", "w2", "v0"})


def short_ids(core: str) -> set[str]:
    """Artifact ids the repo uses in prose.  Only the LEADING one or two
    hyphen-segments of a filename are an id (`rb1-...`, `ot1-...`, `cb-c-...`,
    `W168-...`); a segment in the middle of a descriptive slug is not."""
    segs = [s for s in core.split("-") if s]
    out = set()
    for cand in ({segs[0]} if segs else set()) | (
        {"-".join(segs[:2])} if len(segs) > 1 else set()
    ):
        c = cand.lower()
        if c in WAVE_PREFIXES:
            continue
        if ID_SHAPE.match(cand) and len(cand) >= 2:
            out.add(cand)
    return out


def names_owner(later_rel: str, earlier_rel: str) -> bool:
    """Does the later artifact NAME the earlier owner anywhere in its text?

    Deliberately generous — a generous citation test makes UNCITED findings
    HARDER to claim, which is the direction of error this probe wants.
    """
    t = norm(later_rel)
    stem = os.path.basename(earlier_rel)[: -len(".md")]
    if stem in t:
        return True
    core = re.sub(r"-20\d\d-\d\d-\d\d$", "", stem)
    if len(core) > 16 and core in t:
        return True
    for tok in short_ids(core):
        if re.search(r"\b" + re.escape(tok) + r"\b", t, re.I):
            return True
    return False


def contains(text: str, anchor: str) -> bool:
    """Anchor test, insensitive to intra-token spacing.

    The corpus writes the same inertia as `(49,42)` and as `(49, 42)`.  A
    spacing-sensitive test would have silently split cluster K6 in two, so the
    comparison is run on the space-stripped forms as well."""
    if anchor in text:
        return True
    return anchor.replace(" ", "") in text.replace(" ", "")


# --------------------------------------------------------------------------
# 1. THE DENOMINATOR — pinned, then floor-checked against the live tree
# --------------------------------------------------------------------------

WINDOW_DIR = "lab/active-research/joe-directed"
WINDOW_DATES = ("2026-08-14", "2026-08-15")

# Pinned list of the 44 dated artifacts of the window.  Pinned because the
# checkout is SHARED: a concurrent agent adding a 45th file must not silently
# change a published denominator.
DENOM_FILES: tuple[str, ...] = (
    "anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
    "baryon-number-and-proton-decay/bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md",
    "base-duality/bd-a-the-base-duality-is-the-observation-and-positivity-is-the-obstruction-2026-08-15.md",
    "base-duality/bd-b-obstruction-is-fibre-independent-and-evades-only-at-translation-depth-one-2026-08-15.md",
    "base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md",
    "base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md",
    "base-duality/bd-disposition-packet-2026-08-15.md",
    "base-duality/bd-reg-routing-backlog-disposition-2026-08-15.md",
    "coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md",
    "cosmological-constant-sign/cc1-killing-signature-cannot-sign-lambda-2026-08-14.md",
    "coupling-unification/cu1-left-right-degeneracy-forbids-unification-2026-08-14.md",
    "four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md",
    "high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md",
    "high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md",
    "ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md",
    "ledger-advancement/la10-the-cut-vertex-survives-and-is-not-the-second-action-2026-08-15.md",
    "ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md",
    "ledger-advancement/la2-aca1-needs-no-kernel-selection-and-the-cascade-is-two-thirds-already-banked-2026-08-15.md",
    "ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
    "ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md",
    "ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md",
    "ledger-advancement/la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-constructible-cover-object-2026-08-15.md",
    "ledger-advancement/la7-lt-sm7-moves-t0-to-t2-and-the-lt-sm1-split-is-banked-2026-08-15.md",
    "ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md",
    "ledger-advancement/la9-eleven-real-defects-eight-defective-filings-and-one-denominator-mover-2026-08-15.md",
    "majorana-126-neutrino/bd2-126-channel-is-repulsive-2026-08-14.md",
    "majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md",
    "majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md",
    "majorana-126-neutrino/mj3-4-source-vev-channel-and-twenty-lens-hypothesis-2026-08-14.md",
    "majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md",
    "majorana-126-neutrino/sg4-1-minimal-carrier-constraint-2026-08-14.md",
    "majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md",
    "majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md",
    "majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md",
    "majorana-126-neutrino/src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md",
    "massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md",
    "massless-vector-cosmology/mv2-all-four-abelian-mass-routes-closed-2026-08-14.md",
    "metric-cone-boundedness/mc1-the-cone-does-not-bound-and-the-negative-direction-is-the-cone-itself-2026-08-14.md",
    "ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md",
    "ownership-theorem/ot2-lt-sm3b-is-not-an-ownership-row-and-the-cheapest-pair-is-the-terminal-pair-2026-08-15.md",
    "phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md",
    "phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md",
    "photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md",
    "photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md",
)

WIN = {f"{WINDOW_DIR}/{p}" for p in DENOM_FILES}


def live_window_count() -> int:
    n = 0
    root = os.path.join(REPO, WINDOW_DIR)
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            if not f.endswith(".md"):
                continue
            d = file_date(f)
            if d in WINDOW_DATES:
                n += 1
    return n


# --------------------------------------------------------------------------
# 2. THE DECLARED CLUSTER LIST
#
# Each row is one (result, later-artifact) MEMBER of a cluster.
#   cid       cluster id
#   result    what was produced twice
#   first     the earliest repository artifact that established it
#   later     the window artifact that produced it again
#   anchor    a string that must be present in BOTH files (normalised search)
#   cls       REDERIVED  = later derived it without holding it
#             REPRODUCED = later re-ran it as a declared certification of first
#   cites     DECLARED citation status; the probe RE-DERIVES this and asserts
#   find      findability of `first` at the time `later` was written
# --------------------------------------------------------------------------

RB1 = "explorations/rb1-source-repo-current-musical-2026-07-30.md"
K77RP = "explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md"
REINSP = "lab/sources/selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md"
DGU01 = "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
GEOM = "GEOMETER-VS-PHYSICS-OBJECTS.md"
J = WINDOW_DIR
BDA = f"{J}/base-duality/bd-a-the-base-duality-is-the-observation-and-positivity-is-the-obstruction-2026-08-15.md"
BDB = f"{J}/base-duality/bd-b-obstruction-is-fibre-independent-and-evades-only-at-translation-depth-one-2026-08-15.md"
BDC = f"{J}/base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md"
BDD = f"{J}/base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md"
LA7 = f"{J}/ledger-advancement/la7-lt-sm7-moves-t0-to-t2-and-the-lt-sm1-split-is-banked-2026-08-15.md"
LA11 = f"{J}/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md"

REDERIVED = "REDERIVED"
REPRODUCED = "REPRODUCED"

# findability classes
FINDABLE = "FINDABLE"                       # obvious search would have hit it
WRAPPED = "FINDABLE_BUT_LINE_WRAPPED"       # invisible to line-based grep
BURIED_VOCAB = "BURIED_DIFFERENT_VOCABULARY"
BURIED_TAG = "BURIED_UNDER_QUARANTINE_TAG"
CONCURRENT = "UNFINDABLE_CONCURRENT"        # did not exist when the work ran

CLUSTERS: tuple[dict, ...] = (
    dict(cid="K1",
         result="the composite (g_s^-1 (x) kappa) musical map on the connection "
                "covector, and that positivity is neither used nor available on it",
         first=RB1, first_date="2026-07-30", later=BDA, later_date="2026-08-15",
         anchor="Positivity is neither used nor available",
         cls=REDERIVED, cites=True, find=WRAPPED),
    dict(cid="K2",
         result="same map, same ceiling",
         first=RB1, first_date="2026-07-30", later=BDD, later_date="2026-08-15",
         anchor="Positivity is neither used nor available",
         cls=REDERIVED, cites=True, find=WRAPPED),
    dict(cid="K3",
         result="metric variation is explicit through MET(X): the base metric is "
                "an ARGUMENT of the source's own first action, not an unsupplied "
                "background",
         first=REINSP, first_date="2026-08-09", later=BDC, later_date="2026-08-15",
         anchor="MET(X)",
         cls=REDERIVED, cites=True, find=FINDABLE),
    dict(cid="K4",
         result="ghost clearance is KEEP-AND-GRADE via a Krein form; the demand "
                "is a Krein structure, not positivity",
         first=GEOM, first_date="2026-07-06", later=BDD, later_date="2026-08-15",
         anchor="KEEP-AND-GRADE",
         cls=REDERIVED, cites=True, find=FINDABLE),
    dict(cid="K5a",
         result="the ledger denominator moves 82 -> 83",
         first=LA7, first_date="2026-08-15", later=LA7, later_date="2026-08-15",
         anchor="82 canonical targets", anchor_first="82 canonical targets",
         cls=REDERIVED, cites=False, find=CONCURRENT),
    dict(cid="K5b",
         result="the ledger denominator moves 82 -> 83",
         first=LA7, first_date="2026-08-15", later=LA11, later_date="2026-08-15",
         anchor="denominator moves 82 -> 83", anchor_first="82 canonical targets",
         cls=REDERIVED, cites=False, find=CONCURRENT),
    dict(cid="K6",
         result="inertia (49,42) of the invariant trace form on so(7,7), i.e. on "
                "Lambda^2 R^{7,7}, i.e. on Clifford grade 2 of Cl(7,7)",
         first=K77RP, first_date="2026-08-08", later=BDA, later_date="2026-08-15",
         anchor="(49,42)",
         cls=REDERIVED, cites=False, find=BURIED_VOCAB),
    dict(cid="K7",
         result="inertia (49,42), same object",
         first=K77RP, first_date="2026-08-08", later=BDB, later_date="2026-08-15",
         anchor="(49,42)",
         cls=REDERIVED, cites=False, find=BURIED_VOCAB),
    dict(cid="K8",
         result="inertia (49,42), same object, credited one hop to BD-A",
         first=K77RP, first_date="2026-08-08", later=BDD, later_date="2026-08-15",
         anchor="(49,42)",
         cls=REDERIVED, cites=False, find=BURIED_VOCAB),
    dict(cid="K9",
         result="I_1^B : G x MET(X^{1,3}) --> R at draft p.43 eq (9.1) — the base "
                "metric is the second argument of the source's first action",
         first=DGU01, first_date="2026-06-25", later=BDC, later_date="2026-08-15",
         anchor="MET(X^{1,3})",
         cls=REDERIVED, cites=False, find=BURIED_TAG),

    # ---- disciplined reproduction.  NOT waste.  Counted only under rule R3,
    # ---- which exists to show what calling discipline "waste" would cost.
    dict(cid="D1a", result="so(6,4) = k(21) + p(24), Killing -/+",
         first=f"{J}/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md",
         later_date="2026-08-14", anchor="PV-2", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D1b", result="so(6,4) = k(21) + p(24), Killing -/+",
         first=f"{J}/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/cosmological-constant-sign/cc1-killing-signature-cannot-sign-lambda-2026-08-14.md",
         later_date="2026-08-14", anchor="PV-2", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D1c", result="so(6,4) = k(21) + p(24), Killing -/+",
         first=f"{J}/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md",
         later_date="2026-08-14", anchor="PV-2", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D1d", result="so(6,4) = k(21) + p(24), Killing -/+",
         first=f"{J}/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md",
         later_date="2026-08-14", anchor="PV-2", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D2a", result="MD-1's contraction results E1/E2/E3 on the form leg",
         first=f"{J}/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md",
         later_date="2026-08-15", anchor="MD-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D2b", result="MD-1's contraction results E1/E2/E3 on the form leg",
         first=f"{J}/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md",
         later_date="2026-08-15", anchor="MD-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D3a", result="LA-3's 4D rank-4 anomaly lattice L",
         first=f"{J}/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
         first_date="2026-08-15",
         later=f"{J}/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md",
         later_date="2026-08-15", anchor="LA-3", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D3b", result="LA-3's 4D rank-4 anomaly lattice L",
         first=f"{J}/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
         first_date="2026-08-15",
         later=f"{J}/ledger-advancement/la9-eleven-real-defects-eight-defective-filings-and-one-denominator-mover-2026-08-15.md",
         later_date="2026-08-15", anchor="LA-3", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D3c", result="LA-3's 4D rank-4 anomaly lattice L",
         first=f"{J}/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
         first_date="2026-08-15",
         later=f"{J}/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md",
         later_date="2026-08-15", anchor="LA-3", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D4a", result="CB-C's 14D system: 12x15, rank 5, kernel dim 10",
         first="explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md",
         first_date="2026-08-05",
         later=f"{J}/ledger-advancement/la2-aca1-needs-no-kernel-selection-and-the-cascade-is-two-thirds-already-banked-2026-08-15.md",
         later_date="2026-08-15", anchor="kernel dim 10", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D4b", result="CB-C's 14D system: 12x15, rank 5, kernel dim 10",
         first="explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md",
         first_date="2026-08-05",
         later=f"{J}/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md",
         later_date="2026-08-15", anchor="kernel dim 10", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D5", result="the conformal/trace mode is the single flipped direction",
         first="explorations/W168-reduction-krein-signature-2026-07-14.md",
         first_date="2026-07-14",
         later=f"{J}/metric-cone-boundedness/mc1-the-cone-does-not-bound-and-the-negative-direction-is-the-cone-itself-2026-08-14.md",
         later_date="2026-08-14", anchor="W168", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D6", result="BD-A's ambient inertias, reproduced [R] before use",
         first=BDA, first_date="2026-08-15", later=BDD, later_date="2026-08-15",
         anchor="(189, 175)", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D7a", result="OT-1's clause-O4 pairing obstruction",
         first=f"{J}/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md",
         first_date="2026-08-15", later=BDB, later_date="2026-08-15",
         anchor="OT-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D7b", result="OT-1's clause-O4 pairing obstruction",
         first=f"{J}/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md",
         first_date="2026-08-15", later=LA11, later_date="2026-08-15",
         anchor="OT-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D8a", result="AC-1's RS spin factors (3,4,5) / (-21,-20,-19)",
         first=f"{J}/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md",
         later_date="2026-08-15", anchor="AC-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D8b", result="AC-1's RS spin factors (3,4,5) / (-21,-20,-19)",
         first=f"{J}/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
         later_date="2026-08-15", anchor="AC-1", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D9a", result="SRC-3's unbounded-below ray",
         first=f"{J}/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md",
         later_date="2026-08-14", anchor="SRC-3", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D9b", result="SRC-3's unbounded-below ray",
         first=f"{J}/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md",
         first_date="2026-08-14",
         later=f"{J}/majorana-126-neutrino/src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md",
         later_date="2026-08-15", anchor="SRC-3", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D10a", result="the hypercharge line is unique mod Weyl, 0 bits",
         first="explorations/channel-swing-CH-SM-2026-07-19.md", first_date="2026-07-19",
         later=f"{J}/ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md",
         later_date="2026-08-15", anchor="channel-swing-CH-SM-2026-07-19",
         anchor_first="hypercharge line", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D10b", result="the hypercharge line is unique mod Weyl, 0 bits",
         first="explorations/channel-swing-CH-SM-2026-07-19.md", first_date="2026-07-19",
         later=f"{J}/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md",
         later_date="2026-08-15", anchor="channel-swing-CH-SM-2026-07-19",
         anchor_first="hypercharge line", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D11", result="VG-V2's B_theta positive-definite result",
         first="explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md",
         first_date="2026-07-06",
         later=f"{J}/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md",
         later_date="2026-08-14", anchor="VG-V2", cls=REPRODUCED, cites=True, find=FINDABLE),
    dict(cid="D12", result="(7,3) -> (6,4) under trace reversal",
         first="canon/shiab-existence-cl95.md", first_date="2026-07-06",
         later=f"{J}/metric-cone-boundedness/mc1-the-cone-does-not-bound-and-the-negative-direction-is-the-cone-itself-2026-08-14.md",
         later_date="2026-08-14", anchor="shiab-existence-cl95", anchor_first="(7,3)",
         cls=REPRODUCED, cites=True, find=FINDABLE),
)


# --------------------------------------------------------------------------
# 3. VERIFY the declaration against the repository
# --------------------------------------------------------------------------

def verify_clusters(mutations: dict | None = None) -> list[dict]:
    """Return the clusters that SURVIVE verification.  A cluster that fails
    verification does not silently drop: it raises an E-check failure."""
    mut = mutations or {}
    ok_rows = []
    for row in CLUSTERS:
        r = dict(row)
        r.update(mut.get(r["cid"], {}))
        cid = r["cid"]

        E(f"{cid}.first_exists", exists(r["first"]), r["first"])
        E(f"{cid}.later_exists", exists(r["later"]), r["later"])
        if not (exists(r["first"]) and exists(r["later"])):
            continue

        # declared date must match the filename date where the filename has one
        fd = file_date(r["first"])
        if fd is not None:
            E(f"{cid}.first_date_matches_filename", fd == r["first_date"],
              f"filename={fd} declared={r['first_date']}")
        ld = file_date(r["later"])
        E(f"{cid}.later_date_matches_filename", ld == r["later_date"],
          f"filename={ld} declared={r['later_date']}")

        # ordering: first must not be later than later
        E(f"{cid}.ordering", r["first_date"] <= r["later_date"],
          f"{r['first_date']} <= {r['later_date']}")

        # the anchor must actually be in both files, on NORMALISED text
        a = r["anchor"]
        af = r.get("anchor_first", a)
        E(f"{cid}.anchor_in_first", contains(norm(r["first"]), af),
          f"{af!r} in {r['first']}")
        E(f"{cid}.anchor_in_later", contains(norm(r["later"]), a),
          f"{a!r} in {r['later']}")

        # the declared citation status is RE-DERIVED, not trusted
        if r["first"] != r["later"]:
            actual = names_owner(r["later"], r["first"])
            E(f"{cid}.citation_status_as_declared", actual == r["cites"],
              f"declared={r['cites']} observed={actual}")

        ok_rows.append(r)
    return ok_rows


# --------------------------------------------------------------------------
# 4. THE FOUR INCLUSION RULES
# --------------------------------------------------------------------------

def numerator_artifacts(rows: list[dict], rule: str) -> set[str]:
    """Distinct WINDOW artifacts that carry >= 1 qualifying re-derived result."""
    out: set[str] = set()
    for r in rows:
        if r["later"] not in WIN:
            continue
        if rule == "R0":       # only clusters the repository itself caught
            if r["cls"] == REDERIVED and r["cites"]:
                out.add(r["later"])
            if r["cid"] in ("K5a", "K5b"):   # caught downstream by the packet
                out.add(r["later"])
        elif rule == "R1":     # primary
            if r["cls"] == REDERIVED:
                out.add(r["later"])
        elif rule == "R2a":    # strict-undisclosed, concurrency excluded
            if r["cls"] == REDERIVED and not r["cites"] and r["find"] != CONCURRENT:
                out.add(r["later"])
        elif rule == "R3":     # broad: disciplined reproduction counted too
            if r["cls"] in (REDERIVED, REPRODUCED):
                out.add(r["later"])
        else:
            raise ValueError(rule)
    return out


def main(selftest: bool = False, mutations: dict | None = None) -> int:
    del selftest
    rows = verify_clusters(mutations)

    # ---- denominator ----------------------------------------------------
    missing = [p for p in WIN if not exists(p)]
    E("denominator.all_pinned_files_exist", not missing, f"missing={missing}")
    D = len(WIN)
    E("denominator.pinned_is_44", D == 44, f"D={D}")
    live = live_window_count()
    E("denominator.live_count_is_a_floor", live >= D, f"live={live} floor={D}")

    # EXCLUSION RULE, declared rather than left to drift.  The window contains
    # files that are not research artifacts of the channel and must not sit in
    # a denominator that measures the channel's own output:
    #   (a) `archaeology/*` — the AR-1/AR-2/AR-3 sweeps are META-audits OF this
    #       channel, commissioned to measure it.  Counting a measurement of the
    #       corpus as a member of the corpus is circular, and in AR-3's case it
    #       would let this artifact lower its own rate by existing.
    #   (b) the steward maintenance pass — housekeeping, derives nothing.
    # The exclusion is asserted as a PATTERN, not a file list, because sibling
    # sweeps land in a shared checkout mid-run.
    live_paths = set()
    for dp, _dn, fn in os.walk(os.path.join(REPO, WINDOW_DIR)):
        for f in fn:
            if f.endswith(".md") and file_date(f) in WINDOW_DATES:
                live_paths.add(
                    os.path.relpath(os.path.join(dp, f), REPO).replace(os.sep, "/")
                )
    extra = sorted(live_paths - WIN)
    def excluded(p: str) -> bool:
        tail = p[len(WINDOW_DIR) + 1:]
        return tail.startswith("archaeology/") or tail.startswith("steward-")
    unexplained = [p for p in extra if not excluded(p)]
    E("denominator.every_unpinned_window_file_is_a_declared_exclusion",
      not unexplained, f"unexplained={unexplained}")
    E("denominator.exclusions_are_nonempty_so_the_rule_is_exercised",
      len(extra) >= 1, f"excluded={len(extra)}")

    # ---- the two retrieval-failure mechanisms, asserted both ways --------
    # (a) hard wrap: RB1's operative sentence is invisible to a line search
    phrase = "Positivity is neither used nor available"
    line_hits = sum(1 for ln in raw(RB1).split("\n") if phrase in ln)
    E("wrap.line_search_finds_zero_in_RB1", line_hits == 0, f"line_hits={line_hits}")
    E("wrap.normalised_search_finds_it_in_RB1", phrase in norm(RB1))

    # (b) regex metacharacters: MET(X^{1,3}) is un-greppable by default because
    #     {1,3} is an interval quantifier applied to the literal caret.
    lit = "MET(X^{1,3})"
    n_literal = sum(1 for p in (DGU01, BDC) if lit in norm(p))
    E("meta.literal_search_finds_it", n_literal == 2, f"files={n_literal}")
    # (b1) pasted verbatim as a Python regex the pattern does not even COMPILE:
    #      `{1,3}` is an interval quantifier and there is nothing to repeat.
    try:
        re.compile("MET\\(X^{1,3}\\)")
        compiled = True
    except re.error:
        compiled = False
    E("meta.verbatim_pattern_does_not_compile", not compiled,
      "re.error 'nothing to repeat'")
    # (b2) under GNU-grep semantics `(` `)` are literal and `{1,3}` applies to
    #      the caret, so the pattern means "MET(X" + 1..3 carets + ")".
    #      That compiles, and it matches NOTHING in the corpus.
    rx = re.compile(r"MET\(X\^{1,3}\)")
    n_regex = sum(1 for p in (DGU01, BDC) if rx.search(norm(p)))
    E("meta.grep_semantics_find_zero", n_regex == 0, f"files={n_regex}")

    # (c) the buried owner carries a quarantine tag — which is WHY it was missed
    E("K9.first_is_quarantined", "quarantined" in norm(DGU01).lower())
    E("K9.first_carries_the_page_and_equation", "p.43, eq. (9.1)" in norm(DGU01))

    # ---- day gaps -------------------------------------------------------
    gaps = {r["cid"]: days_between(r["first_date"], r["later_date"])
            for r in rows if r["cls"] == REDERIVED}
    E("gap.K1_is_16", gaps.get("K1") == 16, str(gaps.get("K1")))
    E("gap.K3_is_6", gaps.get("K3") == 6, str(gaps.get("K3")))
    E("gap.K4_is_40", gaps.get("K4") == 40, str(gaps.get("K4")))
    E("gap.K5b_is_0", gaps.get("K5b") == 0, str(gaps.get("K5b")))
    E("gap.K6_is_7", gaps.get("K6") == 7, str(gaps.get("K6")))
    E("gap.K9_is_51", gaps.get("K9") == 51, str(gaps.get("K9")))

    # ---- the rate under four rules --------------------------------------
    rates: dict[str, Fraction] = {}
    nums: dict[str, int] = {}
    for rule in ("R0", "R1", "R2a", "R3"):
        s = numerator_artifacts(rows, rule)
        nums[rule] = len(s)
        rates[rule] = Fraction(len(s), D)

    E("rate.R1_numerator_is_6", nums["R1"] == 6, str(nums["R1"]))
    E("rate.R1_is_3_over_22", rates["R1"] == Fraction(3, 22), str(rates["R1"]))
    E("rate.R2a_numerator_is_4", nums["R2a"] == 4, str(nums["R2a"]))
    E("rate.R2a_is_1_over_11", rates["R2a"] == Fraction(1, 11), str(rates["R2a"]))
    E("rate.R0_numerator_is_5", nums["R0"] == 5, str(nums["R0"]))
    E("rate.R3_numerator_is_21", nums["R3"] == 21, str(nums["R3"]))
    E("rate.R3_is_21_over_44", rates["R3"] == Fraction(21, 44), str(rates["R3"]))
    E("rate.ordering_R2a_le_R0_le_R1_le_R3",
      rates["R2a"] <= rates["R0"] <= rates["R1"] <= rates["R3"])
    # the spread between "waste only" and "count every repeat" is the whole point
    E("rate.spread_R3_minus_R1_is_15_over_44",
      rates["R3"] - rates["R1"] == Fraction(15, 44),
      str(rates["R3"] - rates["R1"]))

    # ---- findability split ----------------------------------------------
    red = [r for r in rows if r["cls"] == REDERIVED]
    E("split.rederived_members_is_10", len(red) == 10, str(len(red)))
    by = {}
    for r in red:
        by[r["find"]] = by.get(r["find"], 0) + 1
    E("split.findable_or_wrapped_is_4",
      by.get(FINDABLE, 0) + by.get(WRAPPED, 0) == 4,
      str(by))
    E("split.structurally_buried_is_4",
      by.get(BURIED_VOCAB, 0) + by.get(BURIED_TAG, 0) == 4, str(by))
    E("split.concurrent_is_2", by.get(CONCURRENT, 0) == 2, str(by))

    # ---- PLANTED CONTROLS: each must FAIL, proving the checks have power --
    C("ctl.absent_anchor_must_not_be_found",
      "Positivity is neither used nor available" in norm(K77RP),
      "the RB1 phrase must NOT be in the k77 residual-pairing file")
    C("ctl.BDA_must_not_cite_the_49_42_owner",
      names_owner(BDA, K77RP),
      "if this passes, K6 is not an uncited re-derivation")
    C("ctl.LA7_must_not_cite_LA11", names_owner(LA7, LA11),
      "if this passes, K5 is not uncoordinated")
    C("ctl.LA11_must_not_cite_LA7", names_owner(LA11, LA7),
      "if this passes, K5 is not uncoordinated")
    C("ctl.BDC_must_not_cite_the_june_transcription", names_owner(BDC, DGU01),
      "if this passes, K9 is not an uncited re-derivation")
    C("ctl.rate_is_not_one", rates["R1"] == Fraction(1, 1),
      "a rule that returns 1 is a broken rule")
    C("ctl.rate_is_not_zero", rates["R1"] == Fraction(0, 1),
      "a rule that returns 0 is a broken rule")
    C("ctl.R3_must_differ_from_R1", rates["R3"] == rates["R1"],
      "if these coincide the sensitivity analysis is vacuous")
    C("ctl.denominator_is_not_the_whole_repo", D > 3000,
      "the denominator is the window, not the corpus")
    C("ctl.wave_prefix_is_not_a_citation", "k77" in short_ids("selected-k77-residual-pairing-invariance"),
      "'k77' names a wave, not an artifact; treating it as a citation erases K6")

    # ---- exactness -------------------------------------------------------
    result = dict(denominator=D, live_floor=live, numerators=nums,
                  rates={k: (v.numerator, v.denominator) for k, v in rates.items()},
                  gaps=gaps, split=by)
    assert_no_float(result)
    import ast
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    floats = [n for n in ast.walk(ast.parse(src))
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    E("exact.no_float_literals_in_source", not floats,
      f"{len(floats)} float constant(s) in the AST")

    # ---- report ----------------------------------------------------------
    npass = sum(1 for k, _n, ok, _d in CHECKS if ok)
    total = len(CHECKS)
    nE = sum(1 for k, *_ in CHECKS if k == "E")
    nC = total - nE
    print("=" * 78)
    print("AR-3 REDISCOVERY RATE — mechanical recomputation")
    print("=" * 78)
    print(f"denominator (pinned window artifacts) : {D}")
    print(f"live window count (floor check)       : {live}")
    print()
    print(f"{'rule':6s} {'numerator':>10s} {'rate':>10s}   meaning")
    meaning = {
        "R2a": "uncited AND not concurrent (pure retrieval failure)",
        "R0": "only what the repository itself caught",
        "R1": "PRIMARY: derived-again without holding it",
        "R3": "broad: disciplined reproduction counted as duplication",
    }
    for rule in ("R2a", "R0", "R1", "R3"):
        print(f"{rule:6s} {nums[rule]:>10d} {str(rates[rule]):>10s}   {meaning[rule]}")
    print()
    print(f"findability of the {len(red)} re-derived cluster members:")
    for k in (FINDABLE, WRAPPED, BURIED_VOCAB, BURIED_TAG, CONCURRENT):
        if by.get(k):
            print(f"   {by[k]}  {k}")
    print()
    print("day gaps (first -> re-derivation):")
    for cid in sorted(gaps):
        print(f"   {cid:5s} {gaps[cid]:3d} days")
    print()
    for kind, name, ok, detail in CHECKS:
        if not ok:
            print(f"FAIL [{kind}] {name}  {detail}")
    print("-" * 78)
    print(f"{npass}/{total} checks pass  ({nE} exact [E], {nC} planted controls [C])")
    return 0 if npass == total else 1


# --------------------------------------------------------------------------
# 5. SELFTEST — plant FALSE FACTS; every one must force exit 1
# --------------------------------------------------------------------------

FALSE_FACTS: tuple[tuple[str, dict], ...] = (
    ("K6 re-labelled REPRODUCED (the discipline/waste line erased)",
     {"K6": {"cls": REPRODUCED}}),
    ("K6 declared CITED (denies the uncited finding)",
     {"K6": {"cites": True}}),
    ("K9 declared CITED (denies the 51-day buried finding)",
     {"K9": {"cites": True}}),
    ("K9 first owner back-dated to after the later artifact",
     {"K9": {"first_date": "2026-09-01"}}),
    ("K1 anchor replaced by a phrase that is not in RB1",
     {"K1": {"anchor": "Positivity is fully available and used throughout"}}),
    ("K3 first owner swapped to a file that does not exist",
     {"K3": {"first": "lab/sources/does-not-exist-2026-01-01.md"}}),
    ("K5b declared non-concurrent (denies the coordination failure)",
     {"K5b": {"find": FINDABLE}}),
    ("D6 re-labelled REDERIVED (calls disciplined [R] reproduction waste)",
     {"D6": {"cls": REDERIVED}}),
    ("K4 date falsified to make the 40-day gap vanish",
     {"K4": {"first_date": "2026-08-15"}}),
    ("K7 later artifact swapped to one outside the window",
     {"K7": {"later": "explorations/rb1-source-repo-current-musical-2026-07-30.md",
             "later_date": "2026-07-30"}}),
)


def selftest() -> int:
    print("=" * 78)
    print("AR-3 SELFTEST — planting false facts; each MUST force exit 1")
    print("=" * 78)
    bad = 0
    for i, (label, mut) in enumerate(FALSE_FACTS, 1):
        CHECKS.clear()
        _RAW.clear()
        _NORM.clear()
        buf = sys.stdout
        try:
            sys.stdout = open(os.devnull, "w")
            try:
                rc = main(mutations=mut)
            except Exception:
                rc = 1
        finally:
            sys.stdout.close()
            sys.stdout = buf
        ok = rc == 1
        if not ok:
            bad += 1
        print(f"  [{'OK ' if ok else 'DEAD'}] {i:2d}. {label}  -> exit {rc}")
    print("-" * 78)
    if bad:
        print(f"SELFTEST FAILED: {bad} planted false fact(s) did not fire.")
        return 1
    print(f"SELFTEST PASSED: all {len(FALSE_FACTS)} planted false facts forced exit 1.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
