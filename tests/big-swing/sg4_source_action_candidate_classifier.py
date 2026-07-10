#!/usr/bin/env python3
"""SG4 -- boundary-supply-ledger: fill one candidate source-action packet and classify it.

Sequential-goals run 2026-07-09, goal 4.

CONTEXT
-------
Today's roadmap ledger (`lab/roadmap/boundary-supply-ledger-generation-count-source-action-2026-07-09.md`)
names the single most useful next Progress run: "select one proposed source-action term or
security-budget extension and fill the [minimal candidate] packet. If the packet survives the hard
guards, add a small executable check under the source-action test surface that classifies the
candidate as closed, blocked, target-import fail, eta-zero obstructed, underdetermined, or
missing-carrier blocked."

This certificate implements that executable classifier and applies it to a concrete candidate. It
does NOT build the source action, does NOT force the count, and changes no verdict.

THE CLASSIFIER (a decision procedure over the minimal packet, hard guards first)
--------------------------------------------------------------------------------
Given a filled packet, the classifier applies the ledger's failure modes in order:
  1. TARGET-IMPORT FAIL  -- uses any of {24/8=3, chi(K3)=24, assumed K3, fitted holonomy,
                            reverse-engineered rank, post-hoc target normalization}.
  2. MISSING-CARRIER BLOCKED -- requires the definite vertical fiber Dirac operator on
                            GL(4,R)/O(3,1), which has NO GU-native definite (Riemannian) fiber
                            metric: the only invariant trace form is indefinite (computed here,
                            signature (7,3)), so definiteness must be imported. If the packet needs
                            a definite vertical carrier and does not supply a named non-native
                            import for it, it is missing-carrier blocked.
  3. ETA-ZERO OBSTRUCTED -- the boundary Dirac inherits the anticommuting chiral grading
                            G = Pi_RS - Q (particle-hole C = J_quat . G, AZ class CII), forcing
                            eta = 0, so the candidate's index half is identically zero unless it
                            supplies an explicit grading-breaking term.
  4. UNDERDETERMINED    -- the integer extraction depends on a free modeling convention (the count
                            scatters across admissible completions), i.e. "completion M forces c",
                            not "GU forces c".
  5. CLOSED             -- integer-valued by construction, compatible with the order-3 carrier, no
                            import, passes every guard. (A CLOSED verdict would be a promotion and
                            PAUSES FOR JOE; the classifier only flags it, never asserts it.)

THE APPLIED CANDIDATE (filled minimal packet)
---------------------------------------------
Candidate: the Stueckelberg-compensator stabilized RS/IG source action S_IG^susy on
Y14 = Met(X4), with the definite vertical fiber Dirac operator over GL(4,R)/O(3,1) as its
integer-extraction carrier (the object every 2026-07-03..07 route bottoms out on). Filled packet
below; the classifier returns MISSING-CARRIER BLOCKED, grounded in the computed indefinite trace
form -- the honest current standing, consistent with BIG-SWING-1 and the ledger.

Run from repo root:   python tests/big-swing/sg4_source_action_candidate_classifier.py   (exit 0)
"""
from __future__ import annotations

import sys
import numpy as np

TOL = 1e-9


def invariant_trace_form_signature():
    """Signature of the GL(4,R)-invariant trace form on the tangent space of GL(4,R)/O(3,1).

    Tangent space ~ Sym^2(R^4) (dim 10); invariant form g(S,T) = tr(eta S eta T), eta = diag(1,1,1,-1).
    Returns (n_pos, n_neg, n_zero).
    """
    eta = np.diag([1.0, 1.0, 1.0, -1.0])
    basis = []
    for i in range(4):
        for j in range(i, 4):
            E = np.zeros((4, 4))
            E[i, j] += 1.0
            E[j, i] += 1.0
            basis.append(E / (np.sqrt(2) if i != j else 1.0))
    n = len(basis)
    G = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            G[a, b] = np.trace(eta @ basis[a] @ eta @ basis[b])
    w = np.linalg.eigvalsh(G)
    return int(np.sum(w > TOL)), int(np.sum(w < -TOL)), int(np.sum(np.abs(w) < TOL))


TARGET_IMPORT_TOKENS = {
    "24/8=3", "chi(K3)=24", "assumed K3", "fitted holonomy",
    "reverse-engineered rank", "post-hoc target normalization", "ind_H=8", "16+8=24",
}


def classify(packet):
    """Return (label, reason) by applying the ledger's hard guards in order."""
    # Guard 1: target import
    imports = set(packet.get("anti_import_violations", []))
    hits = imports & TARGET_IMPORT_TOKENS
    if hits:
        return "TARGET-IMPORT FAIL", f"uses forbidden target token(s): {sorted(hits)}"

    # Guard 2: missing carrier (definite vertical fiber Dirac)
    if packet.get("needs_definite_vertical_carrier", False):
        pos, neg, zero = invariant_trace_form_signature()
        definite = (neg == 0 or pos == 0) and zero == 0
        if not definite and not packet.get("named_nonnative_definiteness_import"):
            return ("MISSING-CARRIER BLOCKED",
                    f"needs a definite vertical fiber Dirac on GL(4,R)/O(3,1), but the only "
                    f"invariant trace form is indefinite signature ({pos},{neg}); no GU-native "
                    f"definite metric exists and the packet names no non-native import for it")

    # Guard 3: eta-zero obstruction
    if packet.get("boundary_dirac_inherits_PH_grading", False) and not packet.get("grading_breaking_term"):
        return ("ETA-ZERO OBSTRUCTED",
                "boundary Dirac inherits the anticommuting chiral grading G = Pi_RS - Q "
                "(AZ class CII), forcing eta = 0; no explicit grading-breaking term supplied")

    # Guard 4: under-determination
    scatter = packet.get("count_scatter_across_completions")
    if scatter and len(set(scatter)) > 1:
        return ("UNDERDETERMINED",
                f"integer extraction is convention-dependent; count scatters {sorted(set(scatter))} "
                f"across admissible completions ('completion M forces c', not 'GU forces c')")

    # Guard 5: closed (flagged only; PAUSES FOR JOE)
    if (packet.get("integer_valued_by_construction") and packet.get("carrier_order3_compatible")
            and not imports):
        return ("CLOSED (FLAG ONLY -- PAUSES FOR JOE)",
                "packet claims integer-by-construction, order-3-carrier-compatible, no import; "
                "a CLOSED verdict is a promotion and requires the maintainer")

    return ("UNDERDETERMINED", "packet does not pin an integer without a free choice or an import")


def main():
    print("=" * 78)
    print("SG4  boundary-supply-ledger: candidate source-action packet + executable classifier")
    print("=" * 78)

    pos, neg, zero = invariant_trace_form_signature()
    print(f"\n[backbone] GL(4,R)-invariant trace form on GL(4,R)/O(3,1): "
          f"signature ({pos},{neg},{zero}) -- INDEFINITE (no GU-native definite fiber metric).")
    assert (pos, neg, zero) == (7, 3, 0), "trace-form signature must be (7,3,0)"

    # The filled minimal candidate packet (mirrors the ledger's template fields)
    candidate = {
        "name": "Stueckelberg-compensator stabilized RS/IG source action S_IG^susy on Y14=Met(X4)",
        "input_gu_native_data": "Cl(9,5) RS sector, Pi_RS, M_D, BV/BRST apparatus, Stueckelberg compensator",
        "variation_space": "RS 1-form A + compensator field on Y14 = Met(X4)",
        "fixed_data": "Spin(9,5) frame, self-dual so(4)_+ connection carrying dim(Lambda^2_+)=3",
        "integer_extraction": "APS index of the definite vertical fiber Dirac over GL(4,R)/O(3,1)",
        "needs_definite_vertical_carrier": True,
        "named_nonnative_definiteness_import": None,   # none supplied -> the wall
        "boundary_dirac_inherits_PH_grading": True,
        "grading_breaking_term": None,
        "integer_valued_by_construction": True,
        "carrier_order3_compatible": True,
        "count_scatter_across_completions": [0, 832, 1664, -4],  # from the 2026-07-03 scatter cert
        "anti_import_violations": [],                  # honestly declares no target token used
    }

    print("\n[candidate packet]")
    for key in ("name", "variation_space", "fixed_data", "integer_extraction"):
        print(f"    {key}: {candidate[key]}")

    label, reason = classify(candidate)
    print("\n[classification]")
    print(f"    LABEL : {label}")
    print(f"    REASON: {reason}")

    # A small control panel: show the classifier discriminates (each guard reachable)
    print("\n[classifier discrimination controls]")
    ctl_import = dict(candidate, anti_import_violations=["chi(K3)=24"])
    ctl_eta = dict(candidate, needs_definite_vertical_carrier=False, named_nonnative_definiteness_import="x")
    ctl_under = dict(candidate, needs_definite_vertical_carrier=False,
                     boundary_dirac_inherits_PH_grading=False)
    ctl_closed = dict(ctl_under, count_scatter_across_completions=[3])
    for nm, pk in [("target-import", ctl_import), ("eta-zero", ctl_eta),
                   ("underdetermined", ctl_under), ("closed-flag", ctl_closed)]:
        lb, _ = classify(pk)
        print(f"    control[{nm:16s}] -> {lb}")

    ok = True
    ok &= (label == "MISSING-CARRIER BLOCKED")
    ok &= classify(ctl_import)[0] == "TARGET-IMPORT FAIL"
    ok &= classify(ctl_eta)[0] == "ETA-ZERO OBSTRUCTED"
    ok &= classify(ctl_under)[0] == "UNDERDETERMINED"
    ok &= classify(ctl_closed)[0].startswith("CLOSED")

    print("\n" + "-" * 78)
    print("ADJUDICATION")
    print("  Candidate classified MISSING-CARRIER BLOCKED: the integer extraction requires a definite")
    print("  vertical fiber Dirac on GL(4,R)/O(3,1), but the only GU-native invariant trace form is")
    print("  indefinite (7,3) -- definiteness must be imported, and the packet names no import. This is")
    print("  the honest current standing (consistent with BIG-SWING-1 and the ledger). The classifier")
    print("  is reusable: future candidates fill the packet and receive a taxonomy label. No source")
    print("  action is built; the generation count stays OPEN (located, not forced).")
    print("=" * 78)
    if not ok:
        print("CONTRACT FAILED", file=sys.stderr)
        sys.exit(1)
    print("SG4 CONTRACT OK (exit 0): candidate packet classified; classifier discriminates all labels.")


if __name__ == "__main__":
    main()
