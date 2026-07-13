#!/usr/bin/env python3
"""THREAD A9 -- post-A8 background Willmore-EL inventory gate.

A8 closed the first A7 open slot by showing Delta^perp H0 = 0 at the flat
constant section. This gate keeps the executable Thread A boundary current:

  * A3-A8 are computed exact/background slots with companion tests and notes;
  * Delta^perp H0 is no longer an open frontier item;
  * the next honest frontier starts at the Rperp_0 EL insertion and ambient
    R^Y.H0/B0 assembly, before full W(H)|s0 and M-linearization.

Run: python tests/threads/A9_post_a8_background_inventory.py
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
    Slot(
        slot_id="A7_BACKGROUND_ASSEMBLY_INVENTORY",
        status="computed_inventory",
        role="pre-A8 executable inventory of computed and open background-assembly slots",
        companion_test="tests/threads/A7_background_assembly_inventory.py",
        companion_note="explorations/threads/A7-background-assembly-inventory-2026-07-13.md",
        verdict_boundary="inventory only; no new first-variation term or status movement",
    ),
    Slot(
        slot_id="A8_DELTA_PERP_H0",
        status="computed_exact",
        role="normal-connection Laplacian of constant-section H0",
        companion_test="tests/threads/A8_constant_section_delta_perp_h0.py",
        companion_note="explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md",
        verdict_boundary="Delta^perp H0=0; full background EL still open",
    ),
]

OPEN_SLOTS = [
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


def file_contains(relative: str, needle: str) -> bool:
    return needle in (ROOT / relative).read_text(encoding="utf-8")


print("[A9] post-A8 background Willmore-EL inventory gate\n")

all_slots = COMPUTED_SLOTS + OPEN_SLOTS
slot_ids = [slot.slot_id for slot in all_slots]
open_ids = [slot.slot_id for slot in OPEN_SLOTS]

check("slot identifiers are unique", len(slot_ids) == len(set(slot_ids)))
check("post-A8 computed-slot count is exactly six", len(COMPUTED_SLOTS) == 6)
check("post-A8 open background-assembly slot count is exactly five", len(OPEN_SLOTS) == 5)
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
    "A8 is now represented as a computed slot, not as an open frontier item",
    "A8_DELTA_PERP_H0" in [slot.slot_id for slot in COMPUTED_SLOTS] and "DELTA_PERP_H0" not in open_ids,
)
check(
    "A8 companion note records the vanishing Delta^perp H0 result",
    file_contains(
        "explorations/threads/A8-constant-section-delta-perp-h0-2026-07-13.md",
        "Delta^perp H0 = 0",
    ),
)
check(
    "A8 companion test still refuses full background EL closure",
    file_contains("tests/threads/A8_constant_section_delta_perp_h0.py", "full background EL remains open"),
)
check(
    "next frontier starts with Rperp EL insertion, then ambient RY.H0/B0",
    open_ids[:2] == ["RPERP_EL_INSERTION", "AMBIENT_RY_H0_B0"],
)
check(
    "full background, M-linearization, and OQ2-A remain downstream in that order",
    open_ids[2:] == ["FULL_BACKGROUND_EL", "BACKGROUND_SUBTRACTED_LINEARIZATION", "OQ2A_FUNCTIONAL_SELECTION"],
)
check(
    "all slot boundaries explicitly refuse premature closure or status movement where appropriate",
    all(
        any(marker in slot.verdict_boundary for marker in ("open", "still", "not", "no", "required", "unclosed"))
        for slot in all_slots
    ),
)

print("    computed slots:")
for slot in COMPUTED_SLOTS:
    print(f"      {slot.slot_id}: {slot.role}")

print("    open slots:")
for slot in OPEN_SLOTS:
    print(f"      {slot.slot_id}: {slot.role}")

print("\n[verdict]")
print("  A8 moved Delta^perp H0 from the open frontier into the computed")
print("  constant-background inventory. The next honest Thread A computation is")
print("  not another Delta^perp H0 pass; it is the Rperp_0 EL insertion and the")
print("  ambient RY.H0/B0 background assembly.")
print()
print("  Honest scope: this is a post-A8 inventory guard. It does not compute a")
print("  new first-variation term, choose a sign convention, change claim status,")
print("  move canon, edit public posture, or touch Lean/source-action/paper surfaces.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = post-A8 inventory is current; remaining Thread A frontier is explicit.")
