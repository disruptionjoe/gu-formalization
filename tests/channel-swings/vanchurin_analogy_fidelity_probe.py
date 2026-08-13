#!/usr/bin/env python3
"""Declared-score contract for the Vanchurin/GU analogy side quest.

This script checks the audit ledger's arithmetic, metadata, Layer-0 caps, and
planted rejection rules.  It does *not* execute the cited mathematics or
verify that a proposed inter-formalism map exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Iterable


@dataclass(frozen=True)
class Analogy:
    key: str
    perspective: int
    cluster: str
    title: str
    scores: tuple[int, int, int, int]
    map_statement: str
    source_anchor: str
    provenance_rank: int
    explicit_map: bool = False
    layer0_closed: bool = False
    gu_target_map_built: bool = False
    parameter_delta: int | None = None
    target_coded: bool = False
    count_inference: bool = False
    hard_reject: bool = False
    type_conflation: bool = False
    positive_metric_as_krein: bool = False
    p3_physical_line_identification: bool = False
    canonical_line_identification_built: bool = False
    splits_shared_lsigma: bool = False

    def validate(self) -> None:
        assert 1 <= self.perspective <= 10, self
        assert len(self.scores) == 4, self
        assert all(isinstance(x, int) and 0 <= x <= 5 for x in self.scores), self
        assert self.map_statement.strip(), self
        assert self.explicit_map, self
        assert self.source_anchor.strip(), self
        assert 1 <= self.provenance_rank <= 4, self
        assert "->" in self.map_statement or "↔" in self.map_statement, self
        if self.parameter_delta is not None:
            assert self.parameter_delta >= 0, self

    @property
    def rejected(self) -> bool:
        forbidden_line_collapse = (
            self.p3_physical_line_identification
            and not self.canonical_line_identification_built
        )
        return any((
            self.count_inference,
            self.target_coded,
            self.hard_reject,
            self.type_conflation,
            self.positive_metric_as_krein,
            forbidden_line_collapse,
            self.splits_shared_lsigma,
        ))

    @property
    def fidelity(self) -> float:
        raw = mean(self.scores)
        min_aware = min(self.scores) + 1
        cap = 5.0
        if not self.explicit_map or not self.map_statement.strip():
            cap = min(cap, 3.0)
        if not self.layer0_closed:
            cap = min(cap, 2.0)
        if not self.gu_target_map_built:
            cap = min(cap, 3.0)
        return round(min(raw, min_aware, cap), 2)

    @property
    def band(self) -> str:
        score = self.fidelity
        if score >= 4.5:
            return "literal-operation"
        if score >= 3.5:
            return "strong-structural"
        if score >= 2.5:
            return "partial-structural"
        if score >= 1.5:
            return "heuristic"
        return "false-friend"

    @property
    def constructive_value(self) -> bool:
        return all((
            self.parameter_delta == 0,
            not self.rejected,
            self.fidelity >= 2.5,
            self.provenance_rank <= 2,
            bool(self.source_anchor.strip()),
            bool(self.map_statement.strip()),
        ))


def row(
    key: str,
    perspective: int,
    cluster: str,
    title: str,
    scores: tuple[int, int, int, int],
    map_statement: str,
    source_anchor: str,
    provenance_rank: int,
    layer0_closed: bool,
    *,
    parameter_delta: int | None = 0,
    **flags: bool,
) -> Analogy:
    return Analogy(
        key=key,
        perspective=perspective,
        cluster=cluster,
        title=title,
        scores=scores,
        map_statement=map_statement,
        source_anchor=source_anchor,
        provenance_rank=provenance_rank,
        explicit_map=bool(map_statement.strip()),
        layer0_closed=layer0_closed,
        gu_target_map_built=False,
        parameter_delta=parameter_delta,
        **flags,
    )


ANALOGIES: tuple[Analogy, ...] = (
    # Perspective 1: learning thermodynamics / free energy.
    row("1A", 1, "datum-role", "datum as architecture-role comparator",
        (3, 2, 2, 3), "fixed neural architecture -> typed GU datum interface",
        "2004.09280 §2, eqs. (2.1)-(2.5)", 1, True),
    row("1B", 1, "restriction-emission", "boundary/bulk loss vs defect action",
        (3, 2, 1, 2), "boundary/bulk projections -> ambient/defect incidence",
        "2004.09280 eq. (2.12), eqs. (3.1)-(3.2)", 1, True),
    row("1C", 1, "relative-line", "Gaussian integration vs conditional line comparison",
        (2, 2, 1, 1),
        "positive Gaussian effective functional -> separately gated physical and relative Det/Pf lines",
        "2004.09280 eq. (5.1), eqs. (5.13)-(5.14)", 1, True),
    row("1D", 1, "gravity-subterm", "Onsager entropy production vs induced gravity",
        (3, 2, 2, 2), "Onsager EH-shaped functional -> GU Gauss/EH subchannel",
        "2008.01540 §9, eqs. (9.11)-(9.13)", 1, True),
    # Perspective 2: stochastic HJ/Madelung.
    row("2A", 2, "fast-slow", "fast hidden vs slow geometric variables",
        (3, 1, 1, 2), "fast/slow learning variables -> candidate GU Hessian blocks",
        "2111.00903 §2, eqs. (2.5)-(2.9)", 1, True),
    row("2B", 2, "current-parent", "stochastic pair vs response/current parent",
        (3, 2, 2, 3), "paired stochastic variation -> GU theta/current elimination branches",
        "2008.01540 eqs. (5.1)-(5.6)", 1, True),
    row("2C", 2, "madelung-bv", "Madelung variables vs BV fields/antifields",
        (1, 0, 0, 0), "Madelung density/phase ↔ BV field/antifield",
        "2012.05082 §2", 1, False, parameter_delta=None,
        type_conflation=True),
    row("2D", 2, "neuron-count", "grand-canonical integer vs P3/index/count",
        (2, 1, 1, 0), "neuron-number branch integer -> GU P3/index/generation value",
        "2012.05082 eq. (3.7), eqs. (4.1)-(4.8)", 1, False,
        parameter_delta=None, count_inference=True),
    # Perspective 3: information geometry / CGD.
    row("3A", 3, "riesz", "CGD metric raising vs connection-current musical",
        (4, 5, 3, 3), "g_CGD^{-1}F -> candidate R_{G,kappa}(delta_A S)",
        "2504.05279 eqs. (2.7)-(2.8)", 1, True),
    row("3B", 3, "full-hessian", "gradient covariance vs coupled GU Hessian",
        (3, 3, 2, 3), "full gradient covariance -> exact coupled GU Hessian diagnostic",
        "2504.05279 eqs. (3.1)-(3.8), eq. (4.9)", 1, True),
    row("3C", 3, "restriction-emission", "encoder/decoder vs restriction/emission",
        (3, 2, 2, 2), "dataset encoder/decoder -> candidate pull/push mnemonic",
        "2504.05279 §2, before eq. (2.1)", 1, True),
    row("3D", 3, "learned-dewitt", "learned covariance metric vs DeWitt/Krein metric",
        (2, 1, 1, 1), "positive adaptive metric ↔ DeWitt/Krein metric",
        "2504.05279 eq. (4.9)", 1, False,
        parameter_delta=None, positive_metric_as_krein=True),
    # Perspective 4: graph propagation.
    row("4A", 4, "reverse-mode", "connection current as chain-rule pullback",
        (4, 4, 3, 3), "direct+implicit derivative -> typed GU A-dependency pullback chain",
        "2411.08138 §2, eqs. (2.3)-(2.4)", 1, True),
    row("4B", 4, "restriction-emission", "defect current as gather/scatter mnemonic",
        (4, 4, 3, 3), "finite gather/scatter -> distributional s^*/s_* adjunction prompt",
        "2504.05279 §2 encoder/decoder maps", 1, True),
    row("4C", 4, "typed-block-graph", "S/I/R operator as typed message graph",
        (3, 2, 2, 2), "weighted adjacency -> typed full-20 block-incidence ledger",
        "2004.09280 §2, eqs. (2.1)-(2.5)", 1, True),
    # Perspective 5: gauge-equivariant / geometric deep learning.
    row("5A", 5, "gauge-covariance", "gauge components in weights/biases",
        (4, 4, 2, 4), "U(1) weight/bias covariance -> GU local-covariance control",
        "2411.08138 §5, eqs. (5.2)-(5.10)", 1, True),
    row("5B", 5, "riesz", "covariant raising vs connection-current musical",
        (4, 5, 3, 3), "CGD covector raising -> candidate GU connection musical",
        "2504.05279 eqs. (2.7)-(2.8)", 1, True),
    row("5C", 5, "moving-clifford", "dynamic architecture vs moving Clifford plane",
        (3, 2, 1, 3), "dynamic neural tensors -> candidate epsilon_IG orbit prompt",
        "2411.08138 eqs. (4.24)-(4.33), eqs. (5.6)-(5.10)", 1, True),
    row("5D", 5, "placement-intersection", "invariant features vs placement constraints",
        (3, 3, 3, 3),
        "scalar invariant bottleneck -> intersection of GU intertwining/reality constraints",
        "2301.10077 §2 eq. (2.2), §4", 1, True),
    # Perspective 6: representation learning / depth / RG.
    row("6A", 6, "parent-factorization", "learning factorizations vs auxiliary elimination",
        (3, 3, 2, 3), "many-to-one discretizations -> GU parent/Schur comparison prompt",
        "2411.08138 eqs. (3.13), (3.19) and following paragraph", 1, True),
    row("6B", 6, "layers-generations", "three sectors/layers as generations",
        (1, 0, 1, 0), "network depth/block count -> generation/index count",
        "2004.09280 eqs. (2.1), (2.5), (2.9)", 1, False,
        parameter_delta=None, count_inference=True),
    row("6C", 6, "field-role", "trainable/hidden vs field/datum roles",
        (2, 1, 2, 1), "trainable/non-trainable roles -> varied/external GU roles",
        "2008.01540 §§4-6", 1, False),
    row("6D", 6, "schur-probe", "RG/depth vs Schur-complement diagnostic",
        (3, 2, 3, 4), "dynamical coarse description -> conditional GU Schur probe",
        "2004.09280 §7, eq. (7.9)", 1, True),
    # Perspective 7: fast/slow / adiabatic dynamics.
    row("7A", 7, "fast-slow", "Z/background block as fast/slow split",
        (2, 1, 2, 1), "fast/slow sectors -> candidate GU generalized-eigenvalue test",
        "2111.00903 §2", 1, True),
    row("7B", 7, "riesz", "CGD cotangent-to-tangent vs N3 current map",
        (4, 3, 3, 3), "CGD musical -> candidate GU connection musical",
        "2504.05279 eqs. (2.7)-(2.8)", 1, True),
    row("7C", 7, "macro-duality", "quantum/gravity dual vs coupled GU sectors",
        (3, 2, 1, 3), "alternative neural macroscopes -> GU coupled-sector comparison",
        "2111.00903 §§3-4, §§7-9", 1, True),
    row("7D", 7, "cosmological-subterm", "neuron multiplier Lambda vs GU bare Lambda",
        (0, 4, 0, 0), "neuron-number multiplier Lambda -> GU bare cosmological coefficient",
        "2111.00903 eqs. (8.12)-(8.13)", 1, False,
        parameter_delta=None, type_conflation=True),
    # Perspective 8: neural fields / emergent PDE.
    row("8A", 8, "restriction-emission", "boundary maps vs pull/push pair",
        (3, 2, 2, 2), "neural boundary maps -> GU pull/push adjunction prompt",
        "2504.05279 §2, before eq. (2.1)", 1, True),
    row("8B", 8, "clifford-subplane", "antisymmetric channel vs 4D Clifford subplane",
        (3, 3, 2, 2), "antisymmetric neural factors -> physical 4-plane Clifford test",
        "2411.08138 §4, eqs. (4.15)-(4.37)", 1, True),
    row("8C", 8, "gauge-covariance", "dynamic weights/biases vs gauge covariance",
        (3, 2, 3, 3), "dynamic U(1) tensors -> GU local-covariance/Noether control",
        "2411.08138 §5, eqs. (5.3)-(5.10)", 1, True),
    row("8D", 8, "gravity-subterm", "emergent EH vs GU Gauss subterm",
        (2, 4, 1, 2), "entropy-production EH term -> GU isolated EH-shaped subchannel",
        "2111.00903 eqs. (8.8)-(8.13)", 1, True),
    # Perspective 9: topological ML / index.
    row("9A", 9, "scalar-ko", "neural scalar invariant vs KO/Fredholm index",
        (0, 0, 1, 0), "Galilean scalar invariant -> KO/symbol/Fredholm index",
        "2301.10077 §2 eq. (2.2), eqs. (4.3)-(4.7)", 1, False,
        parameter_delta=None, hard_reject=True),
    row("9B", 9, "datum-role", "fixed hyperparameters vs external datum role",
        (2, 1, 2, 3), "fixed architecture tuple -> supplied GU datum role",
        "2504.05279 §2, eqs. (2.1)-(2.3)", 1, False),
    row("9C", 9, "p1-monodromy", "free-energy phase vs P1 monodromy",
        (2, 2, 2, 2), "U(1) free-energy branch -> Z/2 DeWitt-loop holonomy prompt",
        "2012.05082 eqs. (3.7)-(3.13), eqs. (4.1)-(4.5)", 1, True),
    row("9D", 9, "neuron-count", "neuron-number branch vs P3/index/generations",
        (0, 0, 0, 0), "active-neuron-number ambiguity -> P3/index/generation value",
        "2012.05082 §4; 2111.00903 eqs. (8.12)-(8.13)", 1, False,
        parameter_delta=None, count_inference=True),
    # Perspective 10: formal analogy / Layer-0 red team.
    row("10A", 10, "loss-action", "loss vs indefinite source action",
        (2, 3, 1, 2), "learning loss ↔ indefinite stationary GU action",
        "2411.08138 §2", 1, False),
    row("10B", 10, "equivalence-relation", "many-to-one relation vs construction quotient",
        (3, 3, 2, 4), "many-to-one continuum relation -> quotient of GU factorizations",
        "2411.08138 §3, paragraph after eq. (3.19)", 1, True),
    row("10C", 10, "constraint-surplus", "antisymmetry constraint vs GU surplus method",
        (3, 3, 3, 3), "assumed neural tensor constraint -> GU placement-surplus audit prompt",
        "2411.08138 §4, eqs. (4.13)-(4.16)", 1, True),
    row("10D", 10, "observer-homonym", "learning observer vs GU section/source",
        (1, 1, 1, 0), "learning subsystem/observer ↔ GU section/source",
        "TOE transcript 01:24:09-01:29:03", 3, False,
        parameter_delta=None, type_conflation=True),
)


def by_key(key: str) -> Analogy:
    return next(item for item in ANALOGIES if item.key == key)


def cluster_summary(
    items: Iterable[Analogy],
) -> list[tuple[str, int, float, float]]:
    grouped: dict[str, list[Analogy]] = {}
    for item in items:
        if item.constructive_value:
            grouped.setdefault(item.cluster, []).append(item)
    rows = []
    for name, group in grouped.items():
        rows.append((
            name,
            len({item.perspective for item in group}),
            round(max(item.fidelity for item in group), 2),
            round(mean(item.fidelity for item in group), 2),
        ))
    return sorted(rows, key=lambda result: (-result[2], -result[1], result[0]))


def run_controls() -> None:
    identity = Analogy(
        "PC1", 10, "control", "identity", (5, 5, 5, 5),
        "object -> same object", "self-identity", 1,
        explicit_map=True, layer0_closed=True, gu_target_map_built=True,
        parameter_delta=0,
    )
    assert identity.fidelity == 5.0
    assert identity.band == "literal-operation"

    different_metrics = Analogy(
        "PC2", 10, "control", "different metrics", (4, 5, 3, 3),
        "one musical -> another musical", "typed control", 1,
        explicit_map=True, layer0_closed=True, gu_target_map_built=False,
        parameter_delta=0,
    )
    assert different_metrics.fidelity == 3.0
    assert different_metrics.band == "partial-structural"

    missing_map = Analogy(
        "NC1", 10, "control", "missing map", (5, 5, 5, 5),
        "", "typed control", 1, layer0_closed=True,
        gu_target_map_built=True, parameter_delta=0,
    )
    assert missing_map.fidelity == 3.0

    homonym = Analogy(
        "NC2", 10, "control", "datum word plant", (5, 5, 5, 5),
        "dataset datum -> GU external datum", "typed control", 1,
        explicit_map=True, layer0_closed=False, gu_target_map_built=True,
        parameter_delta=0,
    )
    assert homonym.fidelity == 2.0

    arbitrary_matrix = Analogy(
        "NC3", 10, "control", "dimension-only map", (3, 3, 0, 3),
        "dimension match -> equivariant map", "typed control", 1,
        explicit_map=True, layer0_closed=True, gu_target_map_built=True,
        parameter_delta=0,
    )
    assert arbitrary_matrix.fidelity == 1.0

    count_plant = Analogy(
        "NC4", 10, "control", "three layers", (5, 5, 5, 5),
        "three layers -> three generations", "typed control", 1,
        explicit_map=True, layer0_closed=False, gu_target_map_built=True,
        parameter_delta=0, count_inference=True,
    )
    target_plant = Analogy(
        "NC5", 10, "control", "desired P3 in loss", (5, 5, 5, 5),
        "target P3 -> loss parameter", "typed control", 1,
        explicit_map=True, layer0_closed=False, gu_target_map_built=True,
        parameter_delta=1, target_coded=True,
    )
    positivity_plant = Analogy(
        "NC6", 10, "control", "positive metric equals Krein", (5, 5, 5, 5),
        "positive optimizer metric -> Krein form", "typed control", 1,
        explicit_map=True, layer0_closed=False, gu_target_map_built=True,
        parameter_delta=0, positive_metric_as_krein=True,
    )
    p3_line_plant = Analogy(
        "NC7", 10, "control", "P3 comparator equals physical line",
        (5, 5, 5, 5), "P3 relative line -> physical source line",
        "frozen N1 comparator rule", 1, explicit_map=True,
        layer0_closed=False, gu_target_map_built=False, parameter_delta=0,
        p3_physical_line_identification=True,
    )
    shared_line_plant = Analogy(
        "NC8", 10, "control", "split shared L_sigma", (5, 5, 5, 5),
        "one L_sigma -> two independent datum pieces", "frozen N1 datum rule",
        1, explicit_map=True, layer0_closed=False,
        gu_target_map_built=False, parameter_delta=0,
        splits_shared_lsigma=True,
    )
    promo_plant = Analogy(
        "NC9", 10, "control", "promo-only conclusion", (5, 5, 5, 5),
        "promo wording -> constructive import", "episode description", 4,
        explicit_map=True, layer0_closed=True, gu_target_map_built=True,
        parameter_delta=0,
    )
    for planted in (
        count_plant, target_plant, positivity_plant, p3_line_plant,
        shared_line_plant,
    ):
        assert planted.rejected
        assert not planted.constructive_value
    assert not promo_plant.constructive_value


def run_audit() -> None:
    for item in ANALOGIES:
        item.validate()

    assert {item.perspective for item in ANALOGIES} == set(range(1, 11))
    assert all(
        sum(item.perspective == perspective for item in ANALOGIES) >= 3
        for perspective in range(1, 11)
    )
    assert {item.provenance_rank for item in ANALOGIES} == {1, 3}
    assert all(item.fidelity <= 3.0 for item in ANALOGIES)

    assert by_key("3A").fidelity == 3.0
    assert by_key("4A").fidelity == 3.0
    assert by_key("5B").fidelity == 3.0
    assert by_key("1C").fidelity == 1.5
    assert by_key("5D").fidelity == 3.0
    assert by_key("6B").rejected
    assert by_key("7D").rejected
    assert by_key("9A").rejected
    assert by_key("9D").rejected
    assert by_key("3D").rejected

    run_controls()


def main() -> None:
    run_audit()
    clusters = cluster_summary(ANALOGIES)
    print(f"DECLARED-SCORE-CONTRACT-PASS: {len(ANALOGIES)} rows / 10 perspectives")
    print("PASS: metadata, missing-map, homonym, symmetry, count, target,")
    print("      positivity, P3-line, shared-L_sigma, and provenance plants")
    print("TOP CONSTRUCTION-PROMPT CLUSTERS (max F / perspective judgments / mean F):")
    for cluster, perspectives, maximum, average in clusters[:10]:
        print(f"  {cluster}: {maximum:.2f} / {perspectives} / {average:.2f}")
    print("BOUNDARY: declared-score arithmetic only; source mathematics not executed")
    print("VERDICT: METHOD-TRANSFER-PROMPTS; NO-NEURAL/GU-MAP-CONSTRUCTED")


if __name__ == "__main__":
    main()
