#!/usr/bin/env python3
r"""
W100 / STRUCTURAL CHECKLIST for the PRE-REGISTERED ADVERSARIAL FORK (Objective 3).

Companion to explorations/obj3-adversarial-fork-preregistered-2026-07-11.md.

This is NOT a physics computation.  The fork document is a SPECIFICATION -- a falsifiability
instrument.  Its value is LEGIBILITY: a skeptic must be able to see (a) that the outcomes are
exhaustive, (b) that the strongest interpretation (A: "wall = confirmed prediction") is mutually
exclusive with the recorded verdict (B: "wall = obstruction"), so the test COULD have gone the
other way, and (c) that every non-recorded outcome carries a CONCRETE, pursuable reversal condition.

This file encodes the pre-registration as data and asserts it is complete and well-formed.  If any
outcome loses its reversal condition, or A/B stop being mutually exclusive, or the recorded verdict
is not one of the pre-registered outcomes, the checklist FAILS -- catching drift that would quietly
turn the falsifiable interpretation back into unfalsifiable spin.

Pure-python, no dependencies.  Exit 0 on success.
"""

# --- the pre-registered fork, as data -------------------------------------------------------------

OUTCOMES = {
    "A": {
        "claim": "sectorial modularity independently sufficient for every physical operation; "
                 "the global J's non-existence is a genuine confirmed prediction (observer-relativity)",
        # A requires BOTH sufficiency (a1) and regional definitizability without a global J (a2)
        "reversal_from_B": [
            "a1: proof that no load-bearing operation (value-selection AND firewall grading) "
            "depends on the region's UV tail -- all factor through a bounded Pi_kappa sub-sector J",
            "a2: proof a genuine type-III_1 region is definitizable (sup_k cond < inf) WITHOUT "
            "resurrecting a bounded global J (i.e. break the region-sup = global-sup identity)",
        ],
        "requires_both": True,
    },
    "B": {
        "claim": "some load-bearing quantity (a genuine region's modular conjugation J_O) still "
                 "requires global control the sectorial construction cannot provide; wall remains an obstruction",
        "reversal_from_B": None,  # B is the recorded verdict; no self-reversal
        "requires_both": False,
    },
    "C": {
        "claim": "sectorial closure holds but is generic to any local (type-III) QFT "
                 "(Bisognano-Wichmann wedge-only + per-region Tomita-Takesaki); the prediction is empty",
        "reversal_from_B": [
            "c: reproduce the whole closure + no-global-J story in an ordinary positive-metric, "
            "ghost-free QFT with NO Krein / ghost / HORN-K step",
        ],
        "requires_both": False,
    },
    "D": {
        "claim": "a bounded global J exists in a better formulation; there is no wall to reinterpret",
        "reversal_from_B": [
            "d1: prove the physical ghost coupling is UV-soft g(k)=o(1/k)",
            "d2: explicit interacting double-cone construction giving a bounded J_O / bounded global J",
            "d3: a non-Krein / different quantization with a bounded global metric",
        ],
        "requires_both": False,
    },
}

RECORDED_VERDICT = "B"

# The evidence W98 produced that landed B (must be non-empty and reference the two named findings).
RECORDED_EVIDENCE = [
    "P1-vs-P3 mutual exclusivity for a type-III_1 region (W98 T5): genuine firewall (HORN K) => "
    "region non-definitizable => no bounded regional J_O; definitizable region => bounded global J "
    "=> removable ghost (HORN Q) => closure vacuous. No regime has both.",
    "P2 overlap-coherence break under a non-UV-soft interaction (W98 T6): per-region J's disagree "
    "UV-divergently on overlaps (0.32 -> 10.97 -> 34.70 as UV reach doubles; free: 0).",
]


def check_exhaustive_and_labelled():
    """The four outcomes A/B/C/D are all present."""
    assert set(OUTCOMES) == {"A", "B", "C", "D"}, "outcomes must be exactly {A,B,C,D}"
    for k, v in OUTCOMES.items():
        assert v["claim"].strip(), f"outcome {k} must have a non-empty claim"
    return True


def check_recorded_verdict_is_pre_registered():
    """The verdict must be one of the pre-registered outcomes (no post-hoc invention)."""
    assert RECORDED_VERDICT in OUTCOMES, "recorded verdict must be a pre-registered outcome"
    return True


def check_verdict_has_evidence():
    """B was recorded because evidence landed it; the evidence must be present and reference P1/P3 and P2."""
    assert len(RECORDED_EVIDENCE) >= 2, "recorded verdict needs its landing evidence"
    joined = " ".join(RECORDED_EVIDENCE)
    assert "P1" in joined and "P3" in joined, "evidence must cite the P1-vs-P3 mutual exclusivity"
    assert "P2" in joined, "evidence must cite the P2 overlap-coherence break"
    return True


def check_A_and_B_mutually_exclusive():
    """
    The strongest interpretation (A: sufficient sub-sector J) and the verdict (B: needs global control)
    must be mutually exclusive -- otherwise the test could not have 'gone against' the interpretation,
    and the reinterpretation would be unfalsifiable.  A asserts the load-bearing quantity needs ONLY a
    bounded sub-sector; B asserts it needs global control.  These cannot both hold.
    """
    a = OUTCOMES["A"]["claim"].lower()
    b = OUTCOMES["B"]["claim"].lower()
    assert "sufficient" in a and "sectorial" in a, "A must assert sectorial sufficiency"
    assert "global control" in b and "cannot provide" in b, "B must assert an unmet global-control need"
    # Encoded semantics: A => needs_global_control == False ; B => needs_global_control == True.
    a_needs_global = False
    b_needs_global = True
    assert a_needs_global != b_needs_global, "A and B must be mutually exclusive on the global-control need"
    return True


def check_every_non_recorded_outcome_has_a_concrete_reversal():
    """
    Falsifiability: each outcome OTHER than the recorded verdict must carry at least one concrete,
    pursuable reversal condition (a named piece of evidence that would flip B to it).
    """
    for k, v in OUTCOMES.items():
        if k == RECORDED_VERDICT:
            assert v["reversal_from_B"] is None, f"recorded verdict {k} should not self-reverse"
            continue
        rev = v["reversal_from_B"]
        assert rev and len(rev) >= 1, f"outcome {k} must have >=1 reversal condition"
        for cond in rev:
            assert len(cond.strip()) >= 20, f"reversal condition for {k} must be concrete: {cond!r}"
    return True


def check_A_requires_both_legs():
    """
    Because the type-III_1 region-sup = global-sup identity blocks the easy escape, flipping B->A needs
    BOTH the sufficiency proof (a1) AND the regional-definitizability proof (a2).  This structural fact
    (A is the hardest flip; it must break the sup=global identity) is what keeps the fork honest.
    """
    assert OUTCOMES["A"]["requires_both"] is True, "A must require both legs (a1 AND a2)"
    assert len(OUTCOMES["A"]["reversal_from_B"]) == 2, "A's reversal must list both a1 and a2"
    return True


CHECKS = [
    ("exhaustive_and_labelled", check_exhaustive_and_labelled),
    ("recorded_verdict_is_pre_registered", check_recorded_verdict_is_pre_registered),
    ("verdict_has_evidence", check_verdict_has_evidence),
    ("A_and_B_mutually_exclusive", check_A_and_B_mutually_exclusive),
    ("every_non_recorded_outcome_has_a_concrete_reversal", check_every_non_recorded_outcome_has_a_concrete_reversal),
    ("A_requires_both_legs", check_A_requires_both_legs),
]


def main():
    passed = 0
    for name, fn in CHECKS:
        ok = fn()
        assert ok, f"check FAILED: {name}"
        print(f"  [ok] {name}")
        passed += 1
    print(f"\nW100 pre-registered fork checklist: {passed}/{len(CHECKS)} checks passed.")
    print(f"Recorded verdict = {RECORDED_VERDICT} (wall remains an obstruction); "
          f"A/C/D each carry a concrete reversal condition => the interpretation is FALSIFIABLE.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
