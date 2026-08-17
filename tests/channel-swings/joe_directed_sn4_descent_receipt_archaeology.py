#!/usr/bin/env python3
"""SN-4 read-only archaeology probe: descent/receipt absence certificate.

SN-3's steering licenses exactly one continuation for the neutrino lane:

    "Permit only a read-only archaeology check for an already-owned
    source-native zero-order/coindex descent together with an
    equation-9.16 slot-to-observed-line receipt."

This probe re-runs that archaeology mechanically.  It (1) verifies the SN-3
specification anchors still read as quoted, (2) re-derives every pattern-family
hit list over the declared source-native K77 corpus, (3) verifies the lineage
receipt that disqualifies each near-collision candidate is still byte-present
in the candidate's own file, (4) proves detector power with a planted fake
receipt that MUST be found and credited, and a planted wrong-lineage candidate
that MUST be rejected, and (5) certifies zero credits over the real corpus.

It constructs nothing: no descent, coefficient, southeast owner, action,
vacuum, external datum, family row, scale relation, quotient, domain, or
conventional 126 mechanism.  A corpus or quote drift makes this probe FAIL,
which is the intended staleness alarm for the absence verdict, not a defect.

--selftest verifies the CLEAN BASELINE FIRST, then applies machinery-corruption
mutations only (corrupted pattern, corrupted corpus root, corrupted spec
anchor, force-credit classifier, force-nocredit classifier, corrupted lineage
quote, disabled whitespace normalization).  Each mutation must produce >= 1
genuine [FAIL]; a crash does not count as a catch and fails the selftest.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CB = os.path.join(ROOT, "explorations", "conditional-build")
SRC = os.path.join(ROOT, "lab", "sources")
EXPL = os.path.join(ROOT, "explorations")
SN = os.path.join(ROOT, "lab", "active-research", "joe-directed",
                  "majorana-126-neutrino")

# ---------------------------------------------------------------- corpus pins
EXPECTED_G1 = 274   # explorations/conditional-build/selected-k77-*.md
EXPECTED_G2 = 154   # lab/sources/selected-k77-*.md
EXPECTED_G3 = 24    # explorations/k77-wave2-*.md

SINGLETONS = (
    os.path.join(SRC, "gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"),
    os.path.join(SRC, "curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md"),
    os.path.join(SRC, "k77-exact-bank-source-custody-2026-08-09.md"),
    os.path.join(EXPL, "resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"),
    os.path.join(EXPL, "resolver-wave-d-native-126-connection-placement-2026-08-03.md"),
)

# ------------------------------------------------------------ pattern families
CLEAN_PATTERNS = {
    "coindex":  (r"coindex", 0),
    "obsline":  (r"N\^c|L\^0|neutral line|observed line|nu_R|seesaw", 0),
    "wordnu":   (r"\b(lepton|neutrino)\b", re.I),
    "zorder":   (r"zero.order|zeroth", 0),
    "varpi":    (r"varpi", re.I),
    "se":       (r"southeast|lower.right", re.I),
    "eq916":    (r"9\.16", 0),
    # Broad sweep shape (line-bounded because `.` never crosses newlines):
    # any line mentioning Omega0 ... -> ... Omega0 is a candidate line for
    # human adjudication.  The credit classifier separately requires strict
    # `Omega0 -> Omega0` adjacency, because a chain through Omega1 is a
    # complex, not a degree-preserving insertion.
    "o0arrow":  (r"Omega\^?0.*->.*Omega\^?0", 0),
}

# Expected pattern-family hit lists (basenames), pinned 2026-08-17.
EXP_ZORDER_VARPI_G1 = sorted([
    "selected-k77-action-stabilizer-connection-flag-reconciliation-2026-08-12.md",
    "selected-k77-common-field-formal-adjoint-green-2026-08-08.md",
    "selected-k77-complete-euler-jet-tangent-closure-2026-08-10.md",
    "selected-k77-common-metric-dupsilon-coefficient-bank-2026-08-08.md",
    "selected-k77-common-physical-equation-dual-green-2026-08-08.md",
    "selected-k77-coupled-gauge-noether-bv-2026-08-11.md",
    "selected-k77-fixed-varpi-normal-frechet-closure-2026-08-08.md",
    "selected-k77-full-carrier-stationary-residual-2026-08-10.md",
    "selected-k77-i2b-principal-preserving-moving-coefficient-absorption-2026-08-13.md",
    "selected-k77-i2b-principal-degeneracy-retype-2026-08-13.md",
    "selected-k77-induced-fermion-principal-discriminator-2026-08-10.md",
    "selected-k77-moving-varpi-stationary-intersection-2026-08-10.md",
    "selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md",
    "selected-k77-sr1c-fixed-varpi-metric-stationarity-2026-08-14.md",
    "selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md",
])
EXP_SE_G1 = sorted([
    "selected-k77-action-owned-leakage-composition-2026-08-10.md",
    "selected-k77-degree-duality-pair-graph-gate-2026-08-10.md",
    "selected-k77-four-field-zero-order-port-2026-08-10.md",
    "selected-k77-full-carrier-stationary-residual-2026-08-10.md",
    "selected-k77-gamma-trace-graph-dynamics-gate-2026-08-10.md",
    "selected-k77-high-conviction-receiver-completion-2026-08-10.md",
    "selected-k77-induced-fermion-principal-discriminator-2026-08-10.md",
    "selected-k77-independent-dual-weight-trivialization-2026-08-11.md",
    "selected-k77-moving-varpi-stationary-intersection-2026-08-10.md",
    "selected-k77-natural-trace-constraint-gate-2026-08-11.md",
    "selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md",
    "selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md",
    "selected-k77-polarized-green-dual-gate-2026-08-11.md",
    "selected-k77-physical-operator-admission-closure-2026-08-13.md",
    "selected-k77-polarized-radical-bfv-ownership-gate-2026-08-11.md",
    "selected-k77-southeast-zero-graph-gate-2026-08-10.md",
    "selected-k77-tautological-total-residual-zero-background-2026-08-14.md",
    "selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md",
    "selected-k77-unrestricted-four-field-euler-image-2026-08-11.md",
    "selected-k77-vertical-soldering-adapter-order-gate-2026-08-11.md",
    "selected-k77-wedge-shiab-southeast-completion-2026-08-11.md",
    "selected-k77-zero-order-w-mirror-parent-leakage-2026-08-10.md",
])
EXP_916_G1 = sorted([
    "selected-k77-action-owned-leakage-composition-2026-08-10.md",
    "selected-k77-four-field-zero-order-port-2026-08-10.md",
    "selected-k77-degree-duality-pair-graph-gate-2026-08-10.md",
    "selected-k77-full-carrier-stationary-residual-2026-08-10.md",
    "selected-k77-induced-fermion-principal-discriminator-2026-08-10.md",
    "selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md",
    "selected-k77-moving-varpi-stationary-intersection-2026-08-10.md",
    "selected-k77-southeast-zero-graph-gate-2026-08-10.md",
    "selected-k77-tautological-total-residual-zero-background-2026-08-14.md",
    "selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md",
    "selected-k77-two-half-hermitian-witt-rotation-gate-2026-08-12.md",
    "selected-k77-w-mirror-action-pairing-ownership-2026-08-13.md",
    "selected-k77-w-mirror-trace-hq-isotropy-correction-2026-08-13.md",
    "selected-k77-zero-order-w-mirror-parent-leakage-2026-08-10.md",
])
EXP_OBSLINE_G3 = sorted([
    "k77-wave2-dirac-derham-superig-rebase-2026-08-04.md",
    "k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md",
    "k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md",
    "k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md",
    "k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md",
    "k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md",
])
EXP_WORDNU_ALL = sorted([
    "k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md",
])
EXP_O0ARROW_G1 = sorted([
    "selected-k77-full-carrier-stationary-residual-2026-08-10.md",
    "selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md",
])

# -------------------------------------------------------------- spec anchors
CLEAN_ANCHORS = [
    ("A1-steering-license",
     os.path.join(SN, "sn3-wave-varpi-incidence-reprioritization-2026-08-16.md"),
     "Permit only a read-only archaeology check for an already-owned "
     "source-native zero-order/coindex descent together with an "
     "equation-9.16 slot-to-observed-line receipt."),
    ("A2-reopen-condition",
     os.path.join(SN, "sn3-wave-varpi-incidence-reprioritization-2026-08-16.md"),
     "SN-3 reopens only if archaeology finds an already-owned source-native "
     "zero-order/coindex descent and a matching equation-(9.16) "
     "slot-to-observed-line receipt."),
    ("A3-descent-definition",
     os.path.join(SN, "sn3-existing-varpi-xr-incidence-census-2026-08-16.md"),
     "If a future source-native `SN3-ZERO-ORDER-COINDEX-DESCENT` horn removes "
     "or transmutes the coindex while producing a declared class-two "
     "zero-order insertion"),
    ("A4-descent-unbuilt",
     os.path.join(SN, "sn3-existing-varpi-xr-incidence-census-2026-08-16.md"),
     "ZERO_ORDER_COINDEX_DESCENT_UNBUILT"),
    ("A5-receipt-unwitnessed",
     os.path.join(SN, "sn3-existing-varpi-xd-incidence-census-2026-08-16.md"),
     "OBSERVED_LINE_AND_COINDEX_INCIDENCE_UNWITNESSED"),
    ("A6-receipt-definition",
     os.path.join(SN, "sn3-existing-varpi-xd-incidence-census-2026-08-16.md"),
     "But no source receipt identifies any formally compatible position with "
     "the observed `L,N^c` lines, nor supplies the needed one-form "
     "coindex/Clifford contraction."),
    ("A7-xr-ports-zero",
     os.path.join(SN, "sn3-source-slot-neutral-line-incidence-classifier-2026-08-16.md"),
     "displayed X_R ports = 0,"),
    ("A8-xr-positions-zero",
     os.path.join(SN, "sn3-source-slot-neutral-line-incidence-classifier-2026-08-16.md"),
     "source-populated X_R positions = 0."),
    ("A9-hostile-review-steering",
     os.path.join(ROOT, "lab", "process", "hostile-reviews",
                  "2026-08-16-joe-directed-sn3-varpi-incidence-review.md"),
     "Reopen only if read-only archaeology finds an already-owned "
     "source-native zero-order/coindex descent and slot-to-observed-line "
     "incidence receipt; do not construct either antecedent here."),
]

# --------------------------------------------------------- lineage receipts
# Each entry: (name, path, quote).  The quote is the candidate file's OWN
# lineage line that types it as a different object than the SN-3 spec, or as
# open/silent rather than owned.  Whitespace-normalized substring match.
CLEAN_LINEAGE = [
    ("L1-port-is-cross-degree",
     os.path.join(CB, "selected-k77-four-field-zero-order-port-2026-08-10.md"),
     "Its ordinary `Omega0(S) -> Omega1(S)` connection cell has exact rank `128`"),
    ("L2-port-no-graph-map",
     os.path.join(CB, "selected-k77-four-field-zero-order-port-2026-08-10.md"),
     "image inclusion does not construct the graph map or make it physical"),
    ("L3-iceberg-reconstructs",
     os.path.join(SRC, "curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md"),
     "CURT-RECONSTRUCTS-ZERO-ORDER-PLACEMENT"),
    ("L4-iceberg-cell-unidentified",
     os.path.join(SRC, "curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md"),
     "the exact `varpi_rs` cell and reduction representation are not identified"),
    ("L5-iceberg-source-silent",
     os.path.join(SRC, "curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md"),
     "`SOURCE-SILENT`: the exact draft `varpi_rs` cell carrying a physical Higgs"),
    ("L6-traceq-no-cell",
     os.path.join(EXPL, "k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md"),
     "It does **not** identify which `varpi_rs` block carries the physical Higgs"),
    ("L7-blockwise-descent-is-global-and-open",
     os.path.join(EXPL, "k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md"),
     "FULL_H_DESCENT_OPEN"),
    ("L8-wedge-is-construction-not-selection",
     os.path.join(CB, "selected-k77-wedge-shiab-southeast-completion-2026-08-11.md"),
     "This is a real construction gain, not a theory selection."),
    ("L9-wedge-source-return-silent-on-selection",
     os.path.join(SRC, "selected-k77-wedge-shiab-southeast-completion-source-return-2026-08-11.md"),
     "Disposition: `SOURCE_CONFIRMS` on operator-family grammar; `SOURCE_SILENT` on selection."),
    ("L10-schur-source-silent",
     os.path.join(CB, "selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md"),
     "SOURCE_SILENT_MAXIMAL_RANK_EFFECTIVE_MAP_NONZERO_STATIONARY"),
    ("L11-crosswalk-no-particle",
     os.path.join(EXPL, "resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"),
     "no physical particle is yet recovered"),
    ("L12-waved-placement-open",
     os.path.join(EXPL, "resolver-wave-d-native-126-connection-placement-2026-08-03.md"),
     "source-owned moving full-20 placement remains open"),
    ("L13-s9-no-sign-correction",
     os.path.join(SRC, "gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"),
     "SOURCE-CORRECTS-SIGNS: NONE FOUND"),
    ("L14-register-scop04-no-descent",
     os.path.join(SRC, "source-claim-register.yaml"),
     "It certifies no global adjoint, descent, or domain."),
    ("L15-register-scop05-verbatim",
     os.path.join(SRC, "source-claim-register.yaml"),
     "noting that other versions of the theory exist including one with a "
     "non-trivial map in the lower right quadrant of the operator."),
    ("L16-trace-constraint-route-killed",
     os.path.join(CB, "selected-k77-natural-trace-constraint-gate-2026-08-11.md"),
     "NATURAL_ZERO_ORDER_CONSTRAINT_ROUTE_KILLED"),
    ("L17-bv-kernel-se-independence",
     os.path.join(CB, "selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md"),
     "it holds for every southeast matrix at a fixed non-null"),
    ("L18-rebase-seesaw-slot-retained-zero",
     os.path.join(EXPL, "k77-wave2-dirac-derham-superig-rebase-2026-08-04.md"),
     "The southeast zero is Weinstein's stated seesaw slot. It is retained as a"),
    ("L19-shiab-duality-seesaw-fence",
     os.path.join(EXPL, "k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md"),
     "the seesaw source analogy is not a mass or neutrino prediction."),
    ("L20-twistor-arrow-is-codifferential",
     os.path.join(CB, "selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md"),
     "Omega0(V) --d_D--> Omega1(V) --M_D--> Omega1(V) --delta_D--> Omega0(V)"),
    ("L21-full-carrier-arrow-is-total-block",
     os.path.join(CB, "selected-k77-full-carrier-stationary-residual-2026-08-10.md"),
     "D = [ A B ] : Omega1(S) + Omega0(S) -> Omega1(S) + Omega0(S)."),
    ("L22-se-graph-gate-is-negative",
     os.path.join(CB, "selected-k77-southeast-zero-graph-gate-2026-08-10.md"),
     "status: exact_scoped_negative_result"),
    ("L23-md1-scalar-descent-refuted",
     os.path.join(ROOT, "lab", "methods", "source-native-comparator-routing.md"),
     "an ad-valued one-form descends to a **one-form**, not to scalars"),
]

# Candidate files whose file-level supersession state is pinned (none carries
# a supersession/correction banner at adjudication time).  The routing METHOD
# file is excluded from the candidate scan: it is not a candidate, and its
# withdrawn-clause [!CAUTION] banner is itself load-bearing evidence FOR the
# absence verdict (the refuted scalar-descent reading); a separate check
# asserts that banner exists.
ROUTING_METHOD = os.path.join(ROOT, "lab", "methods",
                              "source-native-comparator-routing.md")
BANNER_FILES = [e[1] for e in CLEAN_LINEAGE
                if e[1].endswith(".md") and e[1] != ROUTING_METHOD]
BANNER_RE = re.compile(r"\[!CAUTION\]|\[!WARNING\]|(?<![A-Z_])SUPERSEDED(?![A-Z_])")

# ------------------------------------------------------------ planted texts
P1_FAKE_RECEIPT = """
planted control - fake receipt (synthetic; MUST be caught and credited)
The equation-9.16 southeast cell (bar-nu-,nu-) is populated by the named owner
varpi_se acting as a class-two zero-order insertion Omega0 -> Omega0 zero-order
map, and SOURCE-STATES that the source places that slot on the observed N^c
line paired with L^0. The seesaw is realized in this synthetic text.
"""

P2_WRONG_LINEAGE = """
planted control - wrong lineage (synthetic; MUST be rejected)
This artifact discusses the zero-order port and the blockwise adjoint descent.
Here the port is the ordinary cross-degree Omega0(S) -> Omega1(S) connection
cell of equation 9.16, input degree zero and output degree one, retaining the
one-form coindex, and the descent is global H-equivariant overlap descent,
left open. varpi appears throughout. No southeast owner is supplied.
"""


# ----------------------------------------------------------------- machinery
def build_machinery(mut):
    mut = mut or {}

    if mut.get("norm_off"):
        def norm(s):
            return s
    else:
        def norm(s):
            return re.sub(r"\s+", " ", s)

    patterns = {}
    for key, (pat, flags) in CLEAN_PATTERNS.items():
        if mut.get("corrupt_pattern") == key:
            pat = r"ZZ-NEVER-MATCHES-ZZ"
        patterns[key] = re.compile(pat, flags)

    cb_dir = CB + "-nonexistent" if mut.get("corrupt_root") else CB

    anchors = []
    for name, path, quote in CLEAN_ANCHORS:
        if mut.get("corrupt_anchor") == name:
            quote = quote + "XX-CORRUPTED"
        anchors.append((name, path, quote))

    lineage = []
    for name, path, quote in CLEAN_LINEAGE:
        if mut.get("corrupt_lineage") == name:
            quote = quote + "XX-CORRUPTED"
        lineage.append((name, path, quote))

    force_credit = bool(mut.get("force_credit"))
    force_nocredit = bool(mut.get("force_nocredit"))

    arrow_line = re.compile(r"Omega\^?0(\([^)]*\))?\s*->\s*Omega\^?0")

    def credit_descent(text):
        """CREDIT iff the text owns a source-custody class-two zero-order
        Omega0 -> Omega0 varpi insertion (the SN3-B object)."""
        if force_credit:
            return True
        if force_nocredit:
            return False
        t = norm(text)
        has_insertion = (any(arrow_line.search(ln) for ln in text.splitlines())
                         or "zero-order insertion" in t)
        has_varpi = re.search(r"varpi", t, re.I) is not None
        has_class2 = re.search(r"class[- ]two|class[- ]2", t, re.I) is not None
        owned = re.search(r"SOURCE-(STATES|DISPLAYS|SELECTS)", t) is not None
        return bool(has_insertion and has_varpi and has_class2 and owned)

    def credit_receipt(text):
        """CREDIT iff the text owns an equation-9.16 slot-to-observed-line
        placement (the SN3-A/SN3-C object): a named cell, a named owner, an
        observed line, and a placement verb."""
        if force_credit:
            return True
        if force_nocredit:
            return False
        t = norm(text)
        has_cell = re.search(
            r"\((bar-)?nu[+-]?\s*,\s*(bar-)?nu[+-]?\)|southeast cell|cell \(\d,\d\)",
            t) is not None
        has_owner = re.search(r"varpi[_-][a-z]+", t, re.I) is not None
        has_obsline = re.search(r"N\^c|L\^0|observed line|neutral line", t) is not None
        has_placement = re.search(
            r"is populated|is placed|places that slot|incidence witness", t) is not None
        return bool(has_cell and has_owner and has_obsline and has_placement)

    return {
        "norm": norm,
        "patterns": patterns,
        "cb_dir": cb_dir,
        "anchors": anchors,
        "lineage": lineage,
        "credit_descent": credit_descent,
        "credit_receipt": credit_receipt,
    }


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def run_suite(mut=None):
    """Return list of (name, status, detail); status in PASS/FAIL/CRASH."""
    m = build_machinery(mut)
    results = []

    def check(name, fn):
        try:
            ok, detail = fn()
            results.append((name, "PASS" if ok else "FAIL", detail))
        except Exception as exc:  # crash is not a catch
            results.append((name, "CRASH", repr(exc)))

    g1 = sorted(glob.glob(os.path.join(m["cb_dir"], "selected-k77-*.md")))
    g2 = sorted(glob.glob(os.path.join(SRC, "selected-k77-*.md")))
    g3 = sorted(glob.glob(os.path.join(EXPL, "k77-wave2-*.md")))

    # 1. corpus pins ---------------------------------------------------------
    check("corpus-G1-count", lambda: (len(g1) == EXPECTED_G1,
                                      "%d vs %d" % (len(g1), EXPECTED_G1)))
    check("corpus-G2-count", lambda: (len(g2) == EXPECTED_G2,
                                      "%d vs %d" % (len(g2), EXPECTED_G2)))
    check("corpus-G3-count", lambda: (len(g3) == EXPECTED_G3,
                                      "%d vs %d" % (len(g3), EXPECTED_G3)))
    for s in SINGLETONS:
        check("singleton-exists-" + os.path.basename(s)[:40],
              lambda s=s: (os.path.isfile(s), s))

    # 2. spec anchors --------------------------------------------------------
    for name, path, quote in m["anchors"]:
        def fn(path=path, quote=quote):
            return (m["norm"](quote) in m["norm"](read(path)), path)
        check("anchor-" + name, fn)

    # 3. pattern-family hit lists -------------------------------------------
    def hits(files, key):
        pat = m["patterns"][key]
        return sorted(os.path.basename(f) for f in files if pat.search(read(f)))

    def hits_both(files, key_a, key_b):
        pa, pb = m["patterns"][key_a], m["patterns"][key_b]
        out = []
        for f in files:
            t = read(f)
            if pa.search(t) and pb.search(t):
                out.append(os.path.basename(f))
        return sorted(out)

    check("F1-coindex-zero-hits-everywhere",
          lambda: (hits(g1 + g2 + g3 + list(SINGLETONS[:3]), "coindex") == [],
                   "coindex is SN-lane vocabulary; corpus never uses it"))
    check("F2-obsline-zero-hits-G1",
          lambda: (hits(g1, "obsline") == [], "no observed-line vocab in G1"))
    check("F2-obsline-zero-hits-G2",
          lambda: (hits(g2, "obsline") == [], "no observed-line vocab in G2"))
    check("F2-obsline-G3-is-seesaw-analogy-set",
          lambda: (hits(g3, "obsline") == EXP_OBSLINE_G3, str(hits(g3, "obsline"))))
    check("F3-word-neutrino-lepton-single-fenced-hit",
          lambda: (hits(g1 + g2 + g3, "wordnu") == EXP_WORDNU_ALL,
                   str(hits(g1 + g2 + g3, "wordnu"))))
    check("F4-zorder-varpi-list-G1",
          lambda: (hits_both(g1, "zorder", "varpi") == EXP_ZORDER_VARPI_G1,
                   "%d files" % len(hits_both(g1, "zorder", "varpi"))))
    check("F5-southeast-list-G1",
          lambda: (hits(g1, "se") == EXP_SE_G1, "%d files" % len(hits(g1, "se"))))
    check("F6-eq916-list-G1",
          lambda: (hits(g1, "eq916") == EXP_916_G1,
                   "%d files" % len(hits(g1, "eq916"))))

    check("F7-o0arrow-exactly-two-typed-hits-G1",
          lambda: (hits(g1, "o0arrow") == EXP_O0ARROW_G1,
                   str(hits(g1, "o0arrow"))))

    # 4. lineage receipts ----------------------------------------------------
    for name, path, quote in m["lineage"]:
        def fn(path=path, quote=quote):
            return (m["norm"](quote) in m["norm"](read(path)), os.path.basename(path))
        check("lineage-" + name, fn)

    # 5. supersession banners ------------------------------------------------
    def banner_state():
        flagged = sorted(os.path.basename(p) for p in set(BANNER_FILES)
                         if BANNER_RE.search(read(p)))
        return (flagged == [], "flagged: %s" % flagged)
    check("supersession-no-banners-on-candidates", banner_state)
    check("supersession-routing-method-caution-present",
          lambda: ("[!CAUTION]" in read(ROUTING_METHOD),
                   "the withdrawn-clause record must remain visible"))

    # 6. planted controls: detector power ------------------------------------
    check("P1-fake-receipt-hit-by-obsline",
          lambda: (m["patterns"]["obsline"].search(P1_FAKE_RECEIPT) is not None, ""))
    check("P1-fake-receipt-hit-by-se",
          lambda: (m["patterns"]["se"].search(P1_FAKE_RECEIPT) is not None, ""))
    check("P1-fake-receipt-hit-by-zorder-and-varpi",
          lambda: (m["patterns"]["zorder"].search(P1_FAKE_RECEIPT) is not None
                   and m["patterns"]["varpi"].search(P1_FAKE_RECEIPT) is not None, ""))
    check("P1-fake-receipt-credited-as-descent",
          lambda: (m["credit_descent"](P1_FAKE_RECEIPT) is True,
                   "classifier must have credit power"))
    check("P1-fake-receipt-credited-as-receipt",
          lambda: (m["credit_receipt"](P1_FAKE_RECEIPT) is True,
                   "classifier must have credit power"))
    check("P2-wrong-lineage-token-matches",
          lambda: (m["patterns"]["zorder"].search(P2_WRONG_LINEAGE) is not None
                   and m["patterns"]["eq916"].search(P2_WRONG_LINEAGE) is not None
                   and "descent" in P2_WRONG_LINEAGE, "must look tempting"))
    check("P2-wrong-lineage-rejected-as-descent",
          lambda: (m["credit_descent"](P2_WRONG_LINEAGE) is False,
                   "token match must not credit"))
    check("P2-wrong-lineage-rejected-as-receipt",
          lambda: (m["credit_receipt"](P2_WRONG_LINEAGE) is False,
                   "token match must not credit"))

    # 7. the absence certificate ---------------------------------------------
    def zero_credits(fn_key):
        fn = m[fn_key]
        credited = sorted(os.path.basename(f)
                          for f in g1 + g2 + g3 + list(SINGLETONS)
                          if fn(read(f)))
        return (credited == [], "credited: %s" % credited)
    check("ABSENT-descent-zero-credits-over-corpus",
          lambda: zero_credits("credit_descent"))
    check("ABSENT-receipt-zero-credits-over-corpus",
          lambda: zero_credits("credit_receipt"))

    return results


MUTATIONS = [
    ("M1-corrupt-obsline-pattern", {"corrupt_pattern": "obsline"}),
    ("M2-corrupt-corpus-root", {"corrupt_root": True}),
    ("M3-corrupt-spec-anchor", {"corrupt_anchor": "A1-steering-license"}),
    ("M4-force-credit-classifier", {"force_credit": True}),
    ("M5-force-nocredit-classifier", {"force_nocredit": True}),
    ("M6-corrupt-lineage-quote",
     {"corrupt_lineage": "L8-wedge-is-construction-not-selection"}),
    ("M7-disable-normalization", {"norm_off": True}),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    results = run_suite(None)
    passed = sum(1 for _, s, _ in results if s == "PASS")
    failed = [(n, d) for n, s, d in results if s == "FAIL"]
    crashed = [(n, d) for n, s, d in results if s == "CRASH"]
    for name, status, detail in results:
        line = "%s %s" % (status, name)
        if status != "PASS" and detail:
            line += " :: %s" % detail
        print(line)
    print("checks: %d/%d pass, %d fail, %d crash"
          % (passed, len(results), len(failed), len(crashed)))

    if not args.selftest:
        if failed or crashed:
            print("SN4 FAIL: absence certificate did not verify; "
                  "re-adjudicate before citing ABSENT.")
            return 1
        print("PASS: the licensed corpus owns neither a source-native "
              "zero-order/coindex descent nor an equation-9.16 "
              "slot-to-observed-line receipt; the planted fake receipt is "
              "caught and the planted wrong-lineage candidate is rejected.")
        return 0

    # --selftest: clean baseline FIRST, then machinery corruptions.
    if failed or crashed:
        print("SELFTEST REFUSED: clean baseline is not green "
              "(%d fail, %d crash); mutations prove nothing on a red baseline."
          % (len(failed), len(crashed)))
        return 1
    print("selftest: clean baseline verified first (%d/%d)."
          % (passed, len(results)))

    bad = 0
    for name, mut in MUTATIONS:
        mres = run_suite(mut)
        mfail = sum(1 for _, s, _ in mres if s == "FAIL")
        mcrash = sum(1 for _, s, _ in mres if s == "CRASH")
        if mcrash:
            print("SELFTEST FAIL %s: %d crash(es); a crash is not a catch."
                  % (name, mcrash))
            bad += 1
        elif mfail == 0:
            print("SELFTEST FAIL %s: mutation produced no genuine [FAIL]."
                  % name)
            bad += 1
        else:
            print("selftest OK %s: caught by %d genuine [FAIL] check(s), 0 crashes."
                  % (name, mfail))
    if bad:
        print("SN4 SELFTEST FAIL: %d mutation(s) not properly caught." % bad)
        return 1
    print("PASS: selftest clean baseline first; %d/%d machinery mutations "
          "each caught by genuine [FAIL] checks with zero crashes."
          % (len(MUTATIONS), len(MUTATIONS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
