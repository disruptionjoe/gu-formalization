"""Toy cryptoeconomic security-budget selector.

This module deliberately does not compute GU physics. It gives candidate source-action
attempts a small, explicit minimax interface:

    score = growth - validation_cost - finalization_cost - max(adversarial_losses)

The useful property is discipline: a proposed source-action lens must state its loss channels
and hard guards before it can claim to select anything.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


@dataclass(frozen=True)
class CandidateScore:
    """A scored candidate source extension."""

    name: str
    growth_value: float
    validation_cost: float
    finalization_cost: float
    adversarial_losses: Mapping[str, float]
    hard_guards: Mapping[str, bool] = field(default_factory=dict)

    def worst_case_adversarial_loss(self) -> float:
        if not self.adversarial_losses:
            raise ValueError(f"{self.name}: adversarial_losses must not be empty")
        return max(float(v) for v in self.adversarial_losses.values())

    def passes_hard_guards(self) -> bool:
        return all(bool(v) for v in self.hard_guards.values())

    def security_budget_score(self) -> float:
        if not self.passes_hard_guards():
            return float("-inf")
        return (
            float(self.growth_value)
            - float(self.validation_cost)
            - float(self.finalization_cost)
            - self.worst_case_adversarial_loss()
        )


def select_security_budget_winner(candidates: Sequence[CandidateScore]) -> CandidateScore:
    """Return the unique highest-scoring candidate, or raise on no candidate / tie."""
    if not candidates:
        raise ValueError("at least one candidate is required")
    ranked = sorted(candidates, key=lambda c: c.security_budget_score(), reverse=True)
    if len(ranked) > 1 and ranked[0].security_budget_score() == ranked[1].security_budget_score():
        raise ValueError(
            "security-budget selector tied; no unique source-action selection was earned"
        )
    if ranked[0].security_budget_score() == float("-inf"):
        raise ValueError("all candidates failed hard GU guards")
    return ranked[0]

