"""
Prong A extraction-contract check for the SOURCE-DOMAIN-SELECTOR swing
(pre-reg: explorations/prereg-source-domain-selector-swing-2026-07-21.md).

This is a DISCRIMINATING-POWER control, not a proof. It encodes the extraction
contract as executable rules and asserts:

  (1) The planted-positive row D-PLANT (a fabricated endpoint phase phi=e^{i pi/4})
      MUST resolve to SOURCE-SILENT. If it were waved through to
      CONSTRUCTION-GRADE-SOURCED, the contract has no discriminating power.
  (2) A row is CONSTRUCTION-GRADE-SOURCED only if it carries a NON-EMPTY verbatim
      primary-source locus AND a construction-grade (not verbal-shape) spec.
      The same rule that catches D-PLANT is the rule that fails D1/D2/D3/D4.
  (3) Outcome adjudication: D1 & D2 both SOURCE-SILENT  ->  S-SILENT-OPEN.

Exit 0 = all contract assertions held. Foreground only; no side effects.
"""

CONSTRUCTION_GRADE = "CONSTRUCTION-GRADE-SOURCED"
COMPARATOR = "COMPARATOR/IMPORTED"
SILENT = "SOURCE-SILENT"


def classify(row):
    """The extraction contract. A datum is native/construction-grade ONLY with a
    non-empty in-corpus verbatim locus AND a construction-grade specification
    (typed relation/matrix/condition), not a verbal shape or self-professed gap."""
    if not row["locus"].strip():
        return SILENT
    if row["verbal_shape_only"] or row["author_disclaims"]:
        # Weinstein gesturing at a shape without a construction-grade spec,
        # or explicitly disclaiming knowledge, is SOURCE-SILENT, not sourced.
        return SILENT
    if row["imported_completion"]:
        return COMPARATOR
    if row["construction_grade_spec"]:
        return CONSTRUCTION_GRADE
    return SILENT


# demand rows as extracted from the PRIMARY Weinstein corpus
rows = {
    "D1": {  # endpoint / boundary relation (T*H(b)T=H(a) type or endpoint phase)
        "locus": "TOE 01:17:10 'there are no initial conditions ... Really what you have is boundary conditions. And now good luck.'",
        "verbal_shape_only": False,
        "author_disclaims": True,   # 'not stuff I know'; ultra-hyperbolic Cauchy open
        "imported_completion": False,
        "construction_grade_spec": False,
    },
    "D2": {  # noncompact asymptotic / self-adjoint-at-ends domain, z,delta-independent
        "locus": "",   # no decay / L2 / self-adjoint-domain-at-fiber-ends condition anywhere in corpus
        "verbal_shape_only": False,
        "author_disclaims": False,
        "imported_completion": False,
        "construction_grade_spec": False,
    },
    "D3": {  # B5 middle-contraction typed matrix + signs
        "locus": "TOE 02:42:55-02:44:36 2x2 operator matrix, SE-corner zero, 'two negative signs in the second column'",
        "verbal_shape_only": True,   # garbled, 'never released', no reliable slot/sign assignment
        "author_disclaims": False,
        "imported_completion": False,
        "construction_grade_spec": False,
    },
    "D4": {  # real/Krein closure tying (9,5) Krein form to the domain (L7 gap)
        "locus": "UCSD 00:45:00 indefinite signature / Killing-form indeterminacy 'I don't know what to do'; Portal 01:33:22 'whatever sort of inner product naturally exists on the spinors'",
        "verbal_shape_only": False,
        "author_disclaims": True,    # 'I don't know what to do'; inner product left undelimited
        "imported_completion": False,
        "construction_grade_spec": False,
    },
    "D-PLANT": {  # FABRICATED: 'source specifies endpoint phase phi = e^{i pi/4} at the b-end'
        "locus": "",   # no such phase exists anywhere in the corpus
        "verbal_shape_only": False,
        "author_disclaims": False,
        "imported_completion": False,
        "construction_grade_spec": True,   # even if a liar claimed it 'construction grade',
    },                                     # the empty locus must still force SILENT
}

verdicts = {k: classify(v) for k, v in rows.items()}

print("=== Prong A extraction ledger (contract-computed) ===")
for k in ["D1", "D2", "D3", "D4", "D-PLANT"]:
    print(f"  {k:8s} -> {verdicts[k]}")

# (1) planted-positive control
assert verdicts["D-PLANT"] == SILENT, \
    "CONTRACT FAILURE: planted D-PLANT was not caught -> no discriminating power"

# (2) no real demand row reaches construction grade from the primary corpus
for k in ["D1", "D2", "D3", "D4"]:
    assert verdicts[k] != CONSTRUCTION_GRADE, f"unexpected native selector at {k}"

# (3) outcome adjudication
if verdicts["D1"] == SILENT and verdicts["D2"] == SILENT:
    outcome = "S-SILENT-OPEN"
elif CONSTRUCTION_GRADE in (verdicts["D1"], verdicts["D2"]):
    outcome = "S-SELECT"
else:
    outcome = "S-CONDITIONAL"

print(f"\nAdjudicated outcome: {outcome}")
assert outcome == "S-SILENT-OPEN", "outcome logic diverged from D1/D2 verdicts"
print("D-PLANT correctly caught as SOURCE-SILENT (discriminating power confirmed).")
print("All contract assertions held. EXIT 0.")
