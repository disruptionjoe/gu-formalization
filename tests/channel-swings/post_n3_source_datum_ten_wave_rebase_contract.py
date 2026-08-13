#!/usr/bin/env python3
"""Dependency and non-regression contract for the post-N3 ten-wave rebase.

This checks the campaign scaffold, not the mathematics proposed by it.  In
particular, it does not construct a current musical, vary either rival action,
solve a Noether identity, select a VEV, close a BV algebra, build a domain, or
compute an index.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REBASE = (
    ROOT
    / "explorations/post-n3-source-datum-ten-wave-rebase-2026-07-30.md"
)
ORIGINAL = (
    ROOT
    / "explorations/ten-perspective-next-ten-swing-council-scaffold-2026-07-30.md"
)
N1 = ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md"
N2_N4 = ROOT / "explorations/n2a-n4a-intersection-handoff-2026-07-30.md"
N3 = ROOT / "explorations/unified-source-datum-variational-emission-map-2026-07-30.md"
VANCHURIN = (
    ROOT
    / "explorations/vanchurin-ten-perspective-neural-network-analogy-audit-2026-07-30.md"
)
WEINSTEIN = (
    ROOT
    / "explorations/weinstein-primary-source-reinspection-overlooked-answers-2026-07-30.md"
)


LEGS = frozenset(
    {
        "Standard Model/Yukawa",
        "quantum/Krein/BV",
        "gravity/dark energy",
        "index/count",
        "UV/causality",
    }
)


@dataclass(frozen=True)
class Completed:
    step_id: str
    artifact: Path
    rerun: bool = False


@dataclass(frozen=True)
class Transfer:
    source: str
    prompt: str
    assigned_wave: str
    role: str
    closes_blocker: bool = False
    asserts_identity: bool = False


@dataclass(frozen=True)
class Wave:
    order: int
    wave_id: str
    depends_on: tuple[str, ...]
    construction: str
    emitted_object: str
    future_artifact: str
    carried_legs: frozenset[str] = LEGS
    action_locked_required: bool = False
    reads_index_or_count: bool = False
    keeps_kc_separate: bool = True
    terminal_missing_object_report: bool = False
    geometry_return: str = (
        "emit a bounded obstruction-driven adjacent geometry and re-enter "
        "at the earliest invalidated wave"
    )


COMPLETED = (
    Completed("N1", N1),
    Completed("N2a", N2_N4),
    Completed("N4a", N2_N4),
    Completed("N3", N3),
)

TRANSFERS = (
    Transfer(
        "Vanchurin",
        "actual A-dependency graph",
        "RB1",
        "method",
    ),
    Transfer(
        "Vanchurin",
        "G/Hodge/kappa_g connection-current musical",
        "RB1",
        "method",
    ),
    Transfer(
        "Vanchurin",
        "zero-order placement intersection",
        "RB3",
        "method",
    ),
    Transfer(
        "Vanchurin",
        "distributional restriction/emission calculus",
        "RB4",
        "method",
    ),
    Transfer(
        "Weinstein",
        "bosonic-plus-fermionic total Euler residual rival",
        "RB2",
        "architecture",
    ),
    Transfer(
        "Weinstein",
        "one-half d_B T plus one-third [T,T] exactness completion",
        "RB2",
        "architecture",
    ),
    Transfer(
        "Weinstein",
        "shared spin-zero gauge-potential VEV branch",
        "RB3",
        "architecture",
    ),
)

WAVES = (
    Wave(
        1,
        "RB1",
        (),
        "source/repo dictionary, actual dependency DAG, and connection-current musical",
        "typed current/dictionary family",
        "explorations/rb1-source-repo-current-musical-2026-07-30.md",
    ),
    Wave(
        2,
        "RB2",
        ("RB1",),
        "total-residual/current-bridge action shootout with eddy exactness and Noether controls",
        "frozen action architecture and Euler system",
        "explorations/rb2-source-action-exactness-shootout-2026-07-30.md",
    ),
    Wave(
        3,
        "RB3",
        ("RB2",),
        "moving soldering or stabilizer plus full-20 shared spin-zero placement",
        "covariant K/C placement and dynamical-versus-supplied VEV role",
        "explorations/rb3-moving-soldering-spinzero-placement-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        4,
        "RB4",
        ("RB3",),
        "moving defect calculus followed by N2b formal hull and N4b Euler-ideal factor",
        "complete local/formal Euler system and finite hull/factor obstruction",
        "explorations/rb4-moving-defect-n2b-n4b-closure-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        5,
        "RB5",
        ("RB4",),
        "unified quadratic five-leg candidate-variety knockout",
        "quadratic survivor variety or minimal inconsistent equations",
        "explorations/rb5-unified-quadratic-five-leg-knockout-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        6,
        "RB6",
        ("RB5",),
        "finite nonlinear BV completion",
        "finite nonlinear CME action or obstruction/proliferation class",
        "explorations/rb6-full20-nonlinear-bv-ladder-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        7,
        "RB7",
        ("RB6",),
        "curved stationary gravity/dark-energy/causality solve",
        "curved local/formal stationary family with frozen differential expression",
        "explorations/rb7-stationary-source-gravity-de-causality-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        8,
        "RB8",
        ("RB7",),
        "common Green/BFV domain and full graded transport",
        "global stationary action/domain/BV packet",
        "explorations/rb8-full20-green-bfv-transport-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        9,
        "RB9",
        ("RB8",),
        "closed X4 reduction, physical Hessian, Standard Model, and anomaly packet",
        "normalizable equation-closed physical operator and Hessian",
        "explorations/rb9-closed-x4-physical-hessian-sm-2026-07-30.md",
        action_locked_required=True,
    ),
    Wave(
        10,
        "RB10",
        ("RB9",),
        "actual twisted-RS analytic index and held-out tournament",
        "target-blind topology/index family, held-out result, or exact underselection",
        "explorations/rb10-full20-twisted-rs-index-tournament-2026-07-30.md",
        action_locked_required=True,
        reads_index_or_count=True,
    ),
)


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"[PASS] {label}")


def transfers_are_admissible(transfers: tuple[Transfer, ...]) -> bool:
    wave_ids = {wave.wave_id for wave in WAVES}
    for transfer in transfers:
        if transfer.assigned_wave not in wave_ids:
            return False
        if transfer.closes_blocker or transfer.asserts_identity:
            return False
        if transfer.source == "Vanchurin" and transfer.role != "method":
            return False
        if transfer.source == "Weinstein" and transfer.role != "architecture":
            return False
    return True


def waves_are_topological(waves: tuple[Wave, ...]) -> bool:
    seen: set[str] = set()
    for expected_order, wave in enumerate(waves, start=1):
        if wave.order != expected_order:
            return False
        if wave.wave_id != f"RB{expected_order}":
            return False
        if not set(wave.depends_on).issubset(seen):
            return False
        seen.add(wave.wave_id)
    return True


def campaign_is_admissible(waves: tuple[Wave, ...]) -> bool:
    if len(waves) != 10 or not waves_are_topological(waves):
        return False
    if waves[0].wave_id != "RB1" or waves[1].wave_id != "RB2":
        return False
    if waves[3].wave_id != "RB4" or waves[4].wave_id != "RB5":
        return False
    if any(wave.carried_legs != LEGS for wave in waves):
        return False
    if any(wave.terminal_missing_object_report for wave in waves):
        return False
    if any(
        not wave.geometry_return or "stop" in wave.geometry_return.lower()
        for wave in waves
    ):
        return False
    if any(wave.reads_index_or_count for wave in waves[:-1]):
        return False
    if not waves[-1].reads_index_or_count:
        return False
    if any(not wave.keeps_kc_separate for wave in waves):
        return False
    action_locked = False
    for wave in waves:
        if wave.wave_id == "RB2":
            action_locked = True
        if wave.action_locked_required and not action_locked:
            return False
    return True


def main() -> None:
    print("Post-N3 source-action/datum ten-wave rebase contract")

    check(
        "completed N1, N2a, N4a, and N3 artifacts exist",
        all(item.artifact.exists() for item in COMPLETED),
    )
    check(
        "no completed construction step is scheduled for rerun",
        all(not item.rerun for item in COMPLETED),
    )
    check(
        "the two side explorations exist",
        VANCHURIN.exists() and WEINSTEIN.exists(),
    )
    check(
        "Vanchurin remains method-only and Weinstein architecture-only",
        transfers_are_admissible(TRANSFERS),
    )
    check(
        "exactly ten post-N3 waves are dependency ordered",
        campaign_is_admissible(WAVES),
    )
    check(
        "RB1 and RB2 precede the deferred N2b/N4b join",
        [wave.wave_id for wave in WAVES[:4]] == ["RB1", "RB2", "RB3", "RB4"],
    )
    check(
        "the original N5 through N10 architecture is retained as RB5 through RB10",
        [wave.wave_id for wave in WAVES[4:]]
        == ["RB5", "RB6", "RB7", "RB8", "RB9", "RB10"],
    )
    check(
        "all five physics legs are carried by every wave",
        all(wave.carried_legs == LEGS for wave in WAVES),
    )
    check(
        "only RB10 may read an index or count",
        all(not wave.reads_index_or_count for wave in WAVES[:-1])
        and WAVES[-1].reads_index_or_count,
    )
    check(
        "future artifact names are unique",
        len({wave.future_artifact for wave in WAVES}) == len(WAVES),
    )

    text = REBASE.read_text(encoding="utf-8")
    normalized_text = " ".join(text.split())
    original_text = ORIGINAL.read_text(encoding="utf-8")
    n1_text = N1.read_text(encoding="utf-8")
    n3_text = N3.read_text(encoding="utf-8")

    for token in (
        "RB1 —",
        "RB2 —",
        "RB3 —",
        "RB4 —",
        "RB5 —",
        "RB6 —",
        "RB7 —",
        "RB8 —",
        "RB9 —",
        "RB10 —",
        "Layer 0 and construction forks",
        "North-Star geometry continuation contract",
        "geometry return packet",
        "Constraint-surplus test",
        "The first executable target is RB1",
    ):
        check(f"rebase contains required token {token!r}", token in text)

    check(
        "the external datum remains one P1/P2 line plus separate weld and P3 comparator",
        "one flat real orientation line serving both P1 and P2" in text
        and "action-domain weld" in text
        and "separate P3 relative comparator" in text,
    )
    check(
        "N1 still rejects target-coded topology",
        "finite topology set contains no target `3`" in n1_text,
    )
    check(
        "N3 still exposes the typed current fork and eight missing maps",
        "The eight named missing maps are" in n3_text
        and "typed disposition of" in n3_text,
    )
    check(
        "the original scaffold records the post-N3 rebase without being rewritten",
        "Post-N3 execution rebase" in original_text
        and "post-n3-source-datum-ten-wave-rebase-2026-07-30.md" in original_text,
    )
    check(
        "source-architecture failure returns to bounded geometry construction",
        "Failure of Weinstein's source-shaped branch is not failure of the geometry program"
        in normalized_text
        and all(wave.geometry_return for wave in WAVES),
    )

    # Discriminating plants.
    old_jump = (
        WAVES[3],
        WAVES[4],
        WAVES[5],
        WAVES[6],
        WAVES[7],
        WAVES[8],
        WAVES[9],
    )
    check(
        "plant: the old immediate N3-to-N2b/N4b/N5 jump is rejected",
        not campaign_is_admissible(old_jump),
    )

    source_transfer = next(
        transfer
        for transfer in TRANSFERS
        if transfer.prompt.startswith("bosonic-plus-fermionic")
    )
    check(
        "plant: a source formula cannot close the current blocker by authority",
        not transfers_are_admissible(
            tuple(
                replace(transfer, closes_blocker=True)
                if transfer == source_transfer
                else transfer
                for transfer in TRANSFERS
            )
        ),
    )

    neural_transfer = next(
        transfer
        for transfer in TRANSFERS
        if transfer.prompt == "actual A-dependency graph"
    )
    check(
        "plant: a Vanchurin method prompt cannot become a neural/GU identity",
        not transfers_are_admissible(
            tuple(
                replace(transfer, asserts_identity=True)
                if transfer == neural_transfer
                else transfer
                for transfer in TRANSFERS
            )
        ),
    )

    premature_vev = (WAVES[2], WAVES[0], WAVES[1], *WAVES[3:])
    check(
        "plant: shared-VEV placement before dictionary/action selection is rejected",
        not campaign_is_admissible(premature_vev),
    )

    early_count = tuple(
        replace(wave, reads_index_or_count=True)
        if wave.wave_id == "RB3"
        else wave
        for wave in WAVES
    )
    check(
        "plant: reading P3/count at the placement wave is rejected",
        not campaign_is_admissible(early_count),
    )

    collapsed_kc = tuple(
        replace(wave, keeps_kc_separate=False)
        if wave.wave_id == "RB3"
        else wave
        for wave in WAVES
    )
    check(
        "plant: collapsing K and C placement branches is rejected",
        not campaign_is_admissible(collapsed_kc),
    )

    missing_only = tuple(
        replace(wave, terminal_missing_object_report=True)
        if wave.wave_id == "RB4"
        else wave
        for wave in WAVES
    )
    check(
        "plant: a large wave cannot terminate at another missing-object report",
        not campaign_is_admissible(missing_only),
    )

    source_failure_stops = tuple(
        replace(wave, geometry_return="STOP the geometry program")
        if wave.wave_id == "RB2"
        else wave
        for wave in WAVES
    )
    check(
        "plant: failure of Weinstein's source-shaped action cannot stop geometry search",
        not campaign_is_admissible(source_failure_stops),
    )

    print(
        "\nTEN-WAVE-REBASE-CONTRACT-PASS: completed work is preserved; "
        "RB1-RB4 repair the immediate dependencies; RB5-RB10 retain the "
        "late campaign; no scientific claim is closed."
    )


if __name__ == "__main__":
    main()
