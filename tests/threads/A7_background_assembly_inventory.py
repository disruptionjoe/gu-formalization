#!/usr/bin/env python3
"""THREAD A7 -- background Willmore-EL assembly inventory gate.

A3-A6 computed several constant-section pieces needed by the higher-codimension
Willmore first variation. This gate does not compute a new EL term. It makes
the current boundary executable:

  * which constant-background slots have exact companion checks;
  * which slots remain open before the full background EL can be assembled;
  * which surfaces must stay untouched by a safe scheduled Progress pass.

Run: python tests/threads/A7_background_assembly_inventory.py
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Slot:
    slot_id: str
    status: str
    role: str
    companion_test: str | None
    companion_note: str | None
    verdict_boundary: str


COMPUTED_SLOTS = [
    Slot(
        slot_id="A3_SHAPE_COMMUTATOR",
        status="computed_exact",
        role="Ricci-equation shape-operator commutator piece of Rperp_0",
        companion_test="tests/threads/A3_constant_section_normal_curvature.py",
        companion_note="explorations/threads/A3-constant-section-normal-curvature-2026-07-12.md",
        verdict_boundary="commutator nonzero; full Rperp_0 still required ambient projection",
    ),
    Slot(
        slot_id="A4_AMBIENT_NORMAL_PROJECTION",
        status="computed_exact",
        role="ambient R^Y normal projection half of constant-section Rperp_0",
        companion_test="tests/threads/A4_constant_section_rperp_ambient_projection.py",
        companion_note="explorations/threads/A4-constant-section-rperp-ambient-projection-2026-07-12.md",
        verdict_boundary="ambient term does not cancel commutator; no full EL closure",
    ),
    Slot(
        slot_id="A5_RPERP_INVARIANT",
        status="computed_exact",
        role="DeWitt/tangent invariant contraction of full commutator-plus-ambient Rperp_0",
        companion_test="tests/threads/A5_constant_section_rperp_invariants.py",
        companion_note="explorations/threads/A5-constant-section-rperp-invariants-2026-07-12.md",
        verdict_boundary="Rperp_0 non-null; actual EL insertion still open",
    ),
    Slot(
        slot_id="A6_SIMONS_QTF_BACKGROUND",
        status="computed_exact",
        role="constant-section Simons / shape-stress trace-free background slot",
        companion_test="tests/threads/A6_constant_section_simons_stress.py",
        companion_note="explorations/threads/A6-constant-section-simons-stress-2026-07-12.md",
        verdict_boundary="QTF(B0)=0; remaining background terms still open",
    ),
]

OPEN_SLOTS = [
    Slot(
        slot_id="DELTA_PERP_H0",
        status="open",
        role="normal-connection Laplacian of the constant-section mean-curvature vector H0",
        companion_test=None,
        companion_note=None,
        verdict_boundary="must be computed before W(H)|s0 is assembled",
    ),
    Slot(
        slot_id="RPERP_EL_INSERTION",
        status="open",
        role="the coefficient/sign/slot where A5 Rperp_0 enters the Willmore EL",
        companion_test=None,
        companion_note=None,
        verdict_boundary="A5 pins tensor invariants, not the final EL contribution",
    ),
    Slot(
        slot_id="AMBIENT_RY_H0_B0",
        status="open",
        role="ambient R^Y acting on H0/B0 in the background first variation",
        companion_test=None,
        companion_note=None,
        verdict_boundary="alpha_W/c_W background term not assembled",
    ),
    Slot(
        slot_id="FULL_BACKGROUND_EL",
        status="open",
        role="complete O(M^0) W(H)|s0 background residual",
        companion_test=None,
        companion_note=None,
        verdict_boundary="no Lambda coefficient or full field equation follows yet",
    ),
    Slot(
        slot_id="BACKGROUND_SUBTRACTED_LINEARIZATION",
        status="open",
        role="W(H)|s0+M ds minus W(H)|s0 leading-order computation",
        companion_test=None,
        companion_note=None,
        verdict_boundary="H-class versus II-class order selection remains unclosed",
    ),
    Slot(
        slot_id="OQ2A_FUNCTIONAL_SELECTION",
        status="open",
        role="selection between H-class and II-class source-action functionals",
        companion_test=None,
        companion_note=None,
        verdict_boundary="no OQ2-A, canon, claim-status, or public-posture movement",
    ),
]

RESTRICTED_PREFIXES = (
    "Lean/",
    "absorbed/gu-source-action/",
    "canon/",
    "papers/",
    "CANON.md",
    "RESEARCH-STATUS.md",
    "RESEARCH-POSTURE.md",
    "NEXT-STEPS.md",
    "VERIFICATION.md",
    "README.md",
)


def repo_path_exists(relative: str | None) -> bool:
    return relative is not None and (ROOT / relative).is_file()


print("[A7] background Willmore-EL assembly inventory gate\n")

all_slots = COMPUTED_SLOTS + OPEN_SLOTS
slot_ids = [slot.slot_id for slot in all_slots]

check("slot identifiers are unique", len(slot_ids) == len(set(slot_ids)))
check("A3-A6 computed-slot count is exactly four", len(COMPUTED_SLOTS) == 4)
check("open background-assembly slot count is exactly six", len(OPEN_SLOTS) == 6)
check(
    "all computed slots have existing companion tests and notes",
    all(repo_path_exists(slot.companion_test) and repo_path_exists(slot.companion_note) for slot in COMPUTED_SLOTS),
)
check(
    "open slots deliberately have no companion computation yet",
    all(slot.companion_test is None and slot.companion_note is None for slot in OPEN_SLOTS),
)
check(
    "computed-slot companions avoid restricted governance/proof/paper/source-action surfaces",
    all(
        not (slot.companion_test or "").startswith(RESTRICTED_PREFIXES)
        and not (slot.companion_note or "").startswith(RESTRICTED_PREFIXES)
        for slot in COMPUTED_SLOTS
    ),
)
check(
    "all slot boundaries explicitly refuse full EL or status movement where appropriate",
    all(
        any(marker in slot.verdict_boundary for marker in ("open", "still", "not", "no", "must", "remain"))
        for slot in all_slots
    ),
)

computed_order = [slot.slot_id for slot in COMPUTED_SLOTS]
check(
    "computed sequence preserves the A3 -> A4 -> A5 -> A6 dependency chain",
    computed_order
    == [
        "A3_SHAPE_COMMUTATOR",
        "A4_AMBIENT_NORMAL_PROJECTION",
        "A5_RPERP_INVARIANT",
        "A6_SIMONS_QTF_BACKGROUND",
    ],
)

frontier_order = [slot.slot_id for slot in OPEN_SLOTS]
check(
    "next frontier starts with Delta^perp H0 before full background subtraction",
    frontier_order[:3] == ["DELTA_PERP_H0", "RPERP_EL_INSERTION", "AMBIENT_RY_H0_B0"],
)
check(
    "OQ2-A selection remains last, after background EL and M-linearization",
    frontier_order[-1] == "OQ2A_FUNCTIONAL_SELECTION",
)

print("    computed slots:")
for slot in COMPUTED_SLOTS:
    print(f"      {slot.slot_id}: {slot.role}")

print("    open slots:")
for slot in OPEN_SLOTS:
    print(f"      {slot.slot_id}: {slot.role}")

print("\n[verdict]")
print("  A3-A6 are inventory-complete for four constant-background checks, but the")
print("  background Willmore EL is not assembled. The next honest computation is")
print("  Delta^perp H0 / Rperp EL insertion / ambient RY.H0/B0, followed only then")
print("  by W(H)|s0, background-subtracted M-linearization, and OQ2-A selection.")
print()
print("  Honest scope: this is an inventory guard. It does not compute a new")
print("  first-variation term, change claim status, move canon, edit public posture,")
print("  or touch Lean/source-action/paper surfaces.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = A7 inventory gate preserves the computed/open boundary for Thread A.")
