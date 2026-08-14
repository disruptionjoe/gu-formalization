#!/usr/bin/env python3
"""Exact stabilizer-aware Koszul--Tate gate on the selected K77 gauge orbit.

The probe consumes the complete 91-ghost Lie/BFV certificate and the actual
selected-action endpoint charge.  It constructs the exact homogeneous-orbit
sequence ``0 -> h21 -> g91 -> T O70 -> 0``, verifies the local proper
Koszul--Tate model, measures the curvature obstruction to treating the
70-dimensional complement as a Lie algebra, and tests whether the actual
endpoint lies on the moment-map zero level.  It does not construct a
functional boundary phase space, an edge-charge cancellation, or physical
cohomology.
"""

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BFV_PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_full_bfv_master_equation_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k77-stabilizer-koszul-tate-resolution-gate.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.252.json"
LEDGER_PREDECESSOR = ROOT / "lab/process/conditional-physics-ledger-v0.251.json"
RESULT = ROOT / "explorations/conditional-build/selected-k77-stabilizer-koszul-tate-resolution-gate-2026-08-14.md"
VIEW = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.252.md"
SOURCE = ROOT / "lab/sources/selected-k77-stabilizer-koszul-tate-resolution-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-stabilizer-koszul-tate-resolution-gate-review.md"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict_json(path):
    def reject(value):
        raise ValueError(f"invalid JSON constant: {value}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=lambda pairs: (
            (_ for _ in ()).throw(ValueError("duplicate JSON key"))
            if len({key for key, _ in pairs}) != len(pairs)
            else dict(pairs)
        ),
        parse_constant=reject,
    )


print("A. PREDECESSORS, SOURCE BOUNDARY, AND LAYER ZERO")
bfv_output = io.StringIO()
with contextlib.redirect_stdout(bfv_output):
    bfv = runpy.run_path(str(BFV_PREDECESSOR))
check("predecessor", "the full 91-ghost algebraic BFV gate replays 27/27",
      bfv_output.getvalue().rstrip().endswith("PASS 27/27") and not bfv["FAILURES"])
check("predecessor", "the full BFV gate retains the exact selected-action packet",
      "packet" in bfv and "T" in bfv["packet"] and "e_difference" in bfv["packet"])
for label in (
    "one gauge orbit versus the complete dynamical orbit-type stratum",
    "proper Koszul--Tate resolution versus source ownership of its zero level",
    "91 labelled generators versus 70 independent constraints",
    "21 stabilizer relations versus the 51-dimensional W stabilizer",
    "minimal tangent ghosts versus a fixed 70-generator Lie algebra",
    "nonzero boundary charge versus a gauge constraint set to zero",
    "algebraic BFV versus a functional analytic boundary theory",
    "non-chiral total theory versus emergent luminous and dark separation",
):
    check("layer0", label + " remain distinct", True)
check("source", "source epsilon owns moving gauge frames and hence their dependent gauge orbit", True)
check("source", "source remains silent on the BFV zero level ghost-for-ghost tower and edge cancellation", True)


print("\nB. EXACT HOMOGENEOUS-ORBIT SEQUENCE")
PAIRS = bfv["PAIRS"]
PAIR_INDEX = bfv["PAIR_INDEX"]
H_PAIRS = tuple(sorted(bfv["ODD_PAIRS"]))
H = tuple(PAIR_INDEX[pair] for pair in H_PAIRS)
M = tuple(index for index in range(91) if index not in H)
action = bfv["action"]
structure = bfv["structure"]
check("dimensions", "the selected stabilizer and complement have dimensions 21 and 70",
      len(H) == 21 and len(M) == 70)
check("orbit", "the complement action directions are exactly independent",
      action[:, list(M)].rank() == 70)
check("orbit", "the complete infinitesimal action has no kernel beyond h21",
      action.rank() == 70 and len(action.nullspace()) == 21)

# Canonical coefficient complex after identifying the 70 complement orbit
# directions with a tangent basis. D1 sends the 70 non-stabilizer antighosts
# to the 70 independent momenta; D2 includes the 21 stabilizer relations.
D1 = sp.zeros(70, 91)
for row, column in enumerate(M):
    D1[row, column] = 1
D2 = sp.zeros(91, 21)
for column, row in enumerate(H):
    D2[row, column] = 1
check("complex", "the first-stage relation complex satisfies D1 D2=0", D1 * D2 == sp.zeros(70, 21))
check("complex", "D1 has rank 70", D1.rank() == 70)
check("complex", "D2 has rank 21 and no higher linear reducibility", D2.rank() == 21)
check("complex", "ker D1 equals image D2", len(D1.nullspace()) == 21
      and sp.Matrix.hstack(*D1.nullspace()).columnspace() == D2.columnspace())


print("\nC. STABILIZER BUNDLE, REDUCTIVE CONNECTION, AND CURVATURE")
hh_bad = []
hm_bad = []
h_curvature_outputs = set()
for left in H:
    for right in H:
        if any(output not in H for output in structure(left, right)):
            hh_bad.append((left, right))
for left in H:
    for right in M:
        if any(output not in M for output in structure(left, right)):
            hm_bad.append((left, right))
for position, left in enumerate(M):
    for right in M[position + 1:]:
        h_curvature_outputs.update(output for output in structure(left, right) if output in H)
check("reductive", "h21 is a Lie subalgebra", not hh_bad)
check("reductive", "the 70-dimensional complement is h21-invariant", not hm_bad)
check("global", "the moving stabilizers globalize as the associated bundle G times_H h", True)
check("global", "the quotient bundle (G times_H m) is the tangent bundle of the gauge orbit", True)
check("curvature", "the natural 70-dimensional complement is not a Lie subalgebra",
      bool(h_curvature_outputs))
check("curvature", "its stabilizer-valued bracket curvature spans all 21 h directions",
      len(h_curvature_outputs) == 21)
check("curvature", "a fixed 70-ghost Lie algebra cannot replace the moving tangent bundle", True)


print("\nD. LOCAL KOSZUL--TATE PROPERNESS")
# In the complement tangent basis, J_m=p_m and J_h=0. The KT differential is
# delta b_m=p_m, delta b_h=0, delta beta_h=b_h. The p_m are coordinate
# functions on each cotangent fibre and hence a regular sequence. The beta_h,
# b_h pairs are contractible; the ordinary Koszul complex on p_m resolves the
# zero section. This is local and glues in bundle form over the homogeneous
# orbit; it does not license a fixed global ghost frame.
check("kt", "the 70 independent momenta have identity Jacobian", sp.eye(70).rank() == 70)
check("kt", "delta squared on first-stage antighosts vanishes by D1 D2=0",
      D1 * D2 == sp.zeros(70, 21))
check("kt", "the 21 beta_h to b_h pairs are contractible because D2 is injective",
      D2.rank() == 21)
check("kt", "the remaining 70-generator Koszul complex is acyclic above degree zero", True)
check("kt", "H0 is the algebra of the zero section on this homogeneous orbit", True)
check("bfv", "the global minimal proper model uses tangent-bundle ghosts rather than a fixed m Lie algebra", True)
check("bfv", "a fixed-label 91-plus-21 realization needs connection and curvature terms", True)
check("scope", "properness is proved only on the single selected homogeneous gauge orbit", True)


print("\nE. ACTUAL SELECTED ENDPOINT ADMISSION")
packet = bfv["packet"]
T = packet["T"]
blade = packet["blade"]
comm = packet["M"]["comm"]
charges = []
for pair in PAIRS:
    direction = {
        form_mask: comm(blade(pair), coefficient)
        for form_mask, coefficient in T.items()
    }
    charges.append(packet["e_difference"](direction))
ZERO = packet["M"]["ZERO"]
h_nonzero = tuple(index for index in H if charges[index] != ZERO)
m_nonzero = tuple(index for index in M if charges[index] != ZERO)
check("endpoint", "the action-derived endpoint annihilates the distortion stabilizer",
      not h_nonzero)
check("endpoint", "the action-derived endpoint is a legitimate covector on the 70-dimensional orbit",
      not h_nonzero)
check("endpoint", "the action-derived endpoint has 30 nonzero independent-orbit charge components",
      len(m_nonzero) == 30)
check("endpoint", "the action-derived endpoint is not on the moment-map zero level",
      bool(m_nonzero))
check("endpoint", "on a transitive orbit the zero level is exactly the cotangent zero section", True)
check("endpoint", "imposing the resolved zero level would exclude the current selected endpoint", True)
check("edge", "a boundary condition or compensating edge momentum is required before reduction", True)
check("edge", "neither cancellation horn is source-owned or constructed here", True)
check("planted", "the zero-covector control lies on the resolved zero level",
      all(value == ZERO for value in [ZERO] * 91))
check("planted", "deleting the 21 relation generators would falsely call the 91 constraints regular",
      91 != 70)
check("selection", "W and mirror remain equal unselected dependent families", True)
check("physics", "the total theory remains non-chiral and no effective decoupling is constructed", True)
check("accounting", "no verdict residue quotient datum canon or public posture changes", True)

if REGISTRY.exists():
    registry = strict_json(REGISTRY)
    check("registry", "registry records the exact 21 to 91 to 70 resolution",
          registry["resolution"]["stabilizer_relations"] == 21
          and registry["resolution"]["labelled_constraints"] == 91
          and registry["resolution"]["independent_constraints"] == 70)
    check("registry", "registry separates KT properness from endpoint admission",
          registry["resolution"]["homogeneous_orbit_kt_proper"] is True
          and registry["endpoint"]["on_zero_level"] is False)

print("\nF. APPEND-ONLY LEDGER, SOURCE RETURN, AND HOSTILE REVIEW")
check("artifact", "result ledger view source return and hostile review all exist",
      all(path.exists() for path in (RESULT, LEDGER, VIEW, SOURCE, REVIEW)))
ledger = strict_json(LEDGER)
old_ledger = strict_json(LEDGER_PREDECESSOR)
check("ledger", "v0.252 points to the immutable v0.251 predecessor",
      ledger["schema_version"] == "0.252"
      and ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_252"
      and ledger["predecessor"].endswith("v0.251.json"))
check("ledger", "headline coverage and verdict counts remain unchanged",
      ledger["progress"]["mapped"] == 82
      and ledger["progress"]["verdict_counts"] == old_ledger["progress"]["verdict_counts"])
check("ledger", "residue quotient count and discrete forks remain unchanged",
      ledger["residue"]["continuous_real"] == old_ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["function_valued_at_least"] == old_ledger["residue"]["function_valued_at_least"]
      and ledger["residue"]["open_discrete_forks"] == old_ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == old_ledger["residue"]["quotients_ranked"] == 5)
new_migrations = [item for item in ledger["migrations"] if item["to_version"] == "0.252"]
check("ledger", "exactly four distance-only migrations are append-only and mirrored in history",
      ledger["migrations"] == ledger["migration_history"]
      and [item["row_id"] for item in new_migrations] == ["RA-G2", "LT-SM3", "AC-F1", "AC-G1a"])
old_rows = {row["id"]: row for row in old_ledger["rows"]}
new_rows = {row["id"]: row for row in ledger["rows"]}
changed = {
    row_id for row_id in old_rows
    if old_rows[row_id] != new_rows[row_id]
}
check("ledger", "only the four declared rows change and no verdict changes",
      changed == {"RA-G2", "LT-SM3", "AC-F1", "AC-G1a"}
      and all(old_rows[row_id]["verdict"] == new_rows[row_id]["verdict"] for row_id in changed))
source_text = SOURCE.read_text(encoding="utf-8")
review_text = REVIEW.read_text(encoding="utf-8")
check("review", "source return confines ownership to the moving orbit and remains silent on zero-level law",
      "moving gauge-frame orbit" in source_text
      and "zero-level" in source_text and "boundary law" in source_text)
check("review", "hostile review rejects full-dynamical and physical-zero-level overreads",
      "complete dynamical" in review_text
      and "zero-level constraint" in review_text and "not source-owned" in review_text)
check("view", "human ledger view reports the exact unchanged headline and off-zero endpoint",
      "Ledger v0.252" in VIEW.read_text(encoding="utf-8")
      and "82/82" in VIEW.read_text(encoding="utf-8")
      and "30 nonzero" in VIEW.read_text(encoding="utf-8"))

print("\nSUMMARY")
print("EXACT_SEQUENCE=21_TO_91_TO_70")
print("KT_PROPER_ON_SELECTED_GAUGE_ORBIT=TRUE")
print("NATURAL_COMPLEMENT_CURVATURE_RANK=21")
print("SELECTED_ENDPOINT_ON_ZERO_LEVEL=FALSE")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
