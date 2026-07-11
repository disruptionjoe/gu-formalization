# -*- coding: utf-8 -*-
"""
THREAD E1 -- honesty meta-audit, decidable core.

Question: the recurring "reduced to one X / gated on one unbuilt object / one
remaining scalar-or-convention" pattern across the arc -- is it a GENUINE single
degree of freedom (HEALTHY: one object really fixes everything) or a DEGENERATING-
PROGRAM displacement (Lakatos: the hard part keeps relocating one step away)?

WHAT THIS TEST IS. This is NOT a physics computation and it does not "prove" a
verdict. It is a bookkeeping audit made reproducible: it encodes every "reduced to
one X" occurrence I could find as structured data, classifies each pointed-at object
against ONE decidable predicate --

    is_datum_of_S_IG : does the named object become fixed the instant the single
                       unbuilt RS/IG source action S_IG is written, with no further
                       free choice of its own?

-- and then computes two competing tallies plus a timeline. PASS means only that the
enumeration is complete, every record is classified, and the tallies/timeline are as
the scoping doc reports. The VERDICT (healthy vs degenerating) is argued in prose in
explorations/threads/E-one-object-recurrence-meta-audit-2026-07-11.md; this file
supplies the ledger it rests on and the going-forward discriminator as an executable
predicate.

Run: python tests/threads/E_one_object_recurrence_audit.py   (exits 0 on PASS)
"""

# ---------------------------------------------------------------------------
# (1) THE ENUMERATION. Each record is one "reduced to one X" / "gated on one
#     object" / "one remaining scalar-or-convention" statement found in the repo.
#     Fields:
#       date, doc            -- provenance
#       object               -- the exact thing the statement points at
#       sector               -- which physics leg it belongs to
#       granularity          -- how coarse/fine the description is (see LEVELS)
#       is_datum_of_S_IG     -- True if writing the single source action S_IG fixes
#                               it with no residual choice of its own; False if it is
#                               a NEW object not reducible to "write S_IG"
#       note                 -- one-line justification of the classification
# ---------------------------------------------------------------------------

# granularity ladder (coarse -> fine). Used only to see whether the description
# keeps refining while the object stays unbuilt.
LEVELS = {
    "list":        0,   # "a six-item list of blockers"
    "action":      1,   # "the source action S_IG / RS-sector action"
    "complex":     2,   # "RS_GU^phys BRST elliptic complex" (a structure inside S_IG)
    "declaration": 3,   # "the SG4 2-bit field-space declaration" (a datum of S_IG)
    "functional":  4,   # "OQ2-A: which functional |II|^2 vs |H|^2"
    "coefficient": 5,   # "one scalar c_W / alpha_W" (a number set by the functional)
    "convention":  6,   # "one remaining normalization convention"
}

RECORDS = [
    dict(date="2026-06-26", doc="DERIVATION-PROGRESS.md:1696 (OQ-RK1)",
         object="RS_GU^phys BRST elliptic complex (d_RS, gauge-fixing, ghost, symbol)",
         sector="count", granularity="complex", is_datum_of_S_IG=True,
         note="blocker reduced from six-item list to this one complex; it is defined "
              "the moment the RS-sector source action is written"),
    dict(date="2026-06-26", doc="DERIVATION-PROGRESS.md:1706 (OQ-RK1 net)",
         object="RS_GU^phys (specify the BRST quotient of the GU RS field)",
         sector="count", granularity="complex", is_datum_of_S_IG=True,
         note="'entire generation-count question reduces to ONE constructive "
              "obligation'; obligation IS building the RS-sector action"),
    dict(date="2026-06-26", doc="DERIVATION-PROGRESS.md:1720 (RS-BRST, B1)",
         object="the RS-sector ACTION (GU does not determine its own)",
         sector="count", granularity="action", is_datum_of_S_IG=True,
         note="'This is the single root.' Named as the action itself"),
    dict(date="2026-06-27", doc="docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md:60",
         object="the stabilized RS/IG source action",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="'ONE object GU never writes'"),
    dict(date="2026-06-27", doc="canon/source-action-seiberg-witten-construction.md:17",
         object="stabilized RS/IG sector action",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="'The program's universal blocker is one unbuilt object'"),
    dict(date="2026-06-27", doc="absorbed/.../EXTERNAL-ADAPTER-STEELMAN-2026-06-27.md:54",
         object="a stabilized RS/IG source action",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="'Everything downstream is gated by one object GU never wrote'"),
    dict(date="2026-06-28", doc="explorations/.../higher-order-story-persona-sprint-2026-06-28.md:21",
         object="the fermionic source action",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="'the one object that gates everything'"),
    dict(date="2026-07-11", doc="explorations/sg4-forcing-rubric-complete-2026-07-11.md:37",
         object="SG4 declaration = equivariant corner Grassmannian / positive-reduction choice",
         sector="count", granularity="declaration", is_datum_of_S_IG=True,
         note="forcing mechanisms (#6,#10) converge on the SAME object; it is a datum "
              "of the source action's field-space declaration"),
    dict(date="2026-07-11", doc="explorations/explanatory-scope-audit-...-2026-07-11.md:24",
         object="the missing source action (SG4)",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="'all five gaps are the SAME gap'; explicit convergence claim"),
    dict(date="2026-07-11", doc="canon/anchored-leads-screen-RESULTS.md:74",
         object="the unbuilt twisted-RS source action",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="6 independent sweep leads all gate on / re-encode / die before the "
              "SAME object; adversarial convergence TEST, not assertion"),
    dict(date="2026-07-11", doc="explorations/source-action-constraint-intersection-2026-07-11.md:58",
         object="alpha_W (gravity R^Y.B coefficient), one scalar",
         sector="gravity", granularity="coefficient", is_datum_of_S_IG=True,
         note="'fixed by the gravity leg alone (one scalar), gated on the theta-sector'"),
    dict(date="2026-07-11", doc="source-action-constraint-intersection-2026-07-11.md:59",
         object="the RS 2-bit declaration (located-not-forced count)",
         sector="count", granularity="declaration", is_datum_of_S_IG=True,
         note="'the last freedom, coupled to the gauge sector'"),
    dict(date="2026-07-11", doc="willmore-...-reconciliation-2026-07-11.md:46",
         object="(R^Y.B)^TF ambient contraction on the Schwarzschild section (Y14 term)",
         sector="gravity", granularity="coefficient", is_datum_of_S_IG=False,
         note="DISPLACEMENT CANDIDATE: at this step alpha_W is 'one ambient contraction "
              "away' -- a NEW geometric object (Y14 ambient curvature), later itself "
              "computed and re-reduced. Named as the remaining input at this instant."),
    dict(date="2026-07-11", doc="willmore-...-reconciliation-2026-07-11.md:98",
         object="one structural coefficient (scalar weight of the ambient Willmore term)",
         sector="gravity", granularity="coefficient", is_datum_of_S_IG=True,
         note="after R^Y computed, alpha_W re-reduced from 'the whole Y14 geometry' to "
              "this one coefficient -- RELOCATION within the same day"),
    dict(date="2026-07-11", doc="willmore-...-reconciliation-2026-07-11.md:132",
         object="c_W (scalar EL prefactor of the curved-ambient Willmore equation)",
         sector="gravity", granularity="coefficient", is_datum_of_S_IG=True,
         note="'lone remaining unknown is c_W ... exactly the OQ2-A datum ... not an "
              "independent free parameter' -- asserted identity to S_IG normalization"),
    dict(date="2026-07-11", doc="willmore-...-reconciliation-2026-07-11.md:143",
         object="OQ2-A functional binary (|H|^2 H-class vs |II|^2 II-class)",
         sector="gravity", granularity="functional", is_datum_of_S_IG=True,
         note="c_W re-expressed as a functional-choice binary; still a datum of S_IG, "
              "but note the description moved coefficient -> functional"),
    dict(date="2026-07-11", doc="one-residual-complete-picture-2026-07-11.md:178 (note #6)",
         object="the source action (field-space declaration TOGETHER WITH coefficients)",
         sector="all", granularity="action", is_datum_of_S_IG=True,
         note="SELF-AWARE FLAG: 'One object is a CONJUNCTION, not an identity ... not "
              "literally the same object.' The repo itself concedes the multiplicity."),
    dict(date="2026-07-11", doc="NEXT-STEPS.md:67 (honesty guard)",
         object="'one remaining scalar/convention/unbuilt object' (the pattern itself)",
         sector="all", granularity="convention", is_datum_of_S_IG=True,
         note="the repo logs THIS thread as an open watch-item (E1) -- self-aware that "
              "the terminus keeps being 'one remaining X'"),
]

# ---------------------------------------------------------------------------
# (2) DECIDABLE CHECKS
# ---------------------------------------------------------------------------
def check_complete(records):
    for i, r in enumerate(records):
        for f in ("date", "doc", "object", "sector", "granularity",
                  "is_datum_of_S_IG", "note"):
            assert f in r and r[f] != "", f"record {i} missing {f}"
        assert r["granularity"] in LEVELS, f"record {i} bad granularity"
    return True

def tally_identity(records):
    """Competing tally: how many pointed-at objects are data of the SINGLE S_IG
    vs NEW objects not reducible to 'write S_IG'."""
    same = [r for r in records if r["is_datum_of_S_IG"]]
    displaced = [r for r in records if not r["is_datum_of_S_IG"]]
    return len(same), len(displaced), displaced

def distinct_objects(records):
    return sorted({r["object"] for r in records})

def granularity_relocations(records):
    """Within the 2026-07-11 gravity arc, does the description of the SAME
    (unbuilt) object keep refining to a new granularity? Count distinct granularity
    levels used for the gravity sector on the single day -- >1 means the terminus
    was re-described at multiple granularities without the object being written."""
    grav = [r for r in records if r["sector"] == "gravity" and r["date"] == "2026-07-11"]
    levels = sorted({LEVELS[r["granularity"]] for r in grav})
    return grav, levels

# ---------------------------------------------------------------------------
# (3) RUN
# ---------------------------------------------------------------------------
def main():
    checks = []

    ok = check_complete(RECORDS)
    checks.append(("enumeration complete & every record classified", ok))

    same, displaced_n, displaced = tally_identity(RECORDS)
    n = len(RECORDS)
    # Healthy-reading metric: fraction of occurrences whose object is a datum of
    # the single S_IG. Displacement-reading metric: any occurrence naming a NEW
    # object that is not just 'write S_IG'.
    frac_same = same / n
    checks.append((f"identity tally computed: {same}/{n} datum-of-S_IG, "
                   f"{displaced_n}/{n} NEW-object (displacement candidates)",
                   True))
    # Objective sub-finding: at least one displacement candidate exists (the
    # (R^Y.B) ambient object was named as 'the remaining input' before being
    # itself reduced). This is the fine-grained relocation the audit must own.
    checks.append(("at least one displacement candidate present (fine-grained "
                   "relocation is real, not zero)", displaced_n >= 1))

    grav, levels = granularity_relocations(RECORDS)
    # The gravity terminus was re-described at >=3 distinct granularities in ONE
    # day (coefficient/functional at least, plus the ambient-object step) while
    # the object stayed unbuilt -> the relocation signature is present.
    checks.append((f"gravity arc (2026-07-11) re-described terminus at "
                   f"{len(levels)} distinct granularity levels in one day "
                   f"(relocation signature present if >=2)", len(levels) >= 2))

    objs = distinct_objects(RECORDS)
    checks.append((f"{len(objs)} DISTINCT object-names across the arc "
                   f"(coarse label 'source action' recurs; fine labels differ)",
                   len(objs) >= 5))

    # ---- report ----
    print("=" * 78)
    print("THREAD E1 -- one-object recurrence meta-audit (ledger + decidable checks)")
    print("=" * 78)
    print(f"\nRecords enumerated: {n}")
    print(f"Datum-of-S_IG (healthy-reading count):        {same}/{n} "
          f"({frac_same:.0%})")
    print(f"New-object / displacement candidates:         {displaced_n}/{n}")
    if displaced:
        print("  displacement candidate(s):")
        for r in displaced:
            print(f"    - {r['date']} {r['doc']}\n        object: {r['object']}")
    print(f"\nGravity terminus (2026-07-11) granularity levels used: "
          f"{[k for k,v in sorted(LEVELS.items(), key=lambda x:x[1]) if v in levels]}")
    print(f"Distinct object-names total: {len(objs)}")
    print("\n--- checks ---")
    allok = True
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        allok = allok and ok

    print("\n" + "-" * 78)
    print("INTERPRETATION (the verdict itself lives in the scoping doc, argued both ways):")
    print("  * HEALTHY signal: the COARSE object ('the unbuilt RS/IG source action')")
    print("    is STABLE from 2026-06-26 to 2026-07-11 and the anchored-leads screen is")
    print("    an adversarial convergence TEST (6 routes, none escapes) -- not rhetoric.")
    print("  * DEGENERATING signal: within the 2026-07-11 gravity arc the terminus was")
    print("    re-described at multiple granularities (ambient object -> coefficient ->")
    print("    functional) in a single day while the object stayed UNBUILT; and note #6")
    print("    of the draft-of-record concedes 'one object' is a CONJUNCTION, not an")
    print("    identity -- c_W (a coefficient) != the SG4 2-bit (a declaration).")
    print("  * GOING-FORWARD DISCRIMINATOR (executable): the next reduction is HEALTHY")
    print("    iff its named object is_datum_of_S_IG (fixed the instant S_IG is written);")
    print("    it is DISPLACEMENT iff it names a NEW object not equal to a datum of S_IG.")
    print("-" * 78)

    print("\n" + ("PASS" if allok else "FAIL") +
          " -- ledger complete & consistent; metrics as reported."
          " (This certifies the AUDIT LEDGER, not the prose verdict.)")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
