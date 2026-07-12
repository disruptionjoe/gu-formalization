#!/usr/bin/env python3
"""Wave 36 / H54 -- guardian-symmetry necessary-condition gate.

The current H54 question is whether GU's newly sharpened structures

    Sp(32,32;H) + [P,S] = 0

already furnish the local-SUSY / super-IG guardian that a UV-complete interacting
massive Rarita-Schwinger sector would need.

This test deliberately checks only necessary conditions.  It does not try to
construct the source action and it does not change any scientific verdict.  The
point is to keep "guardian" from collapsing into "even Krein symmetry": a real
guardian must include local odd gauge data, an odd-square bracket, an action on
the RS/spin-1/2 block system, and a Ward identity preserving the gamma-trace
constraint.  The existing even data can be compatible with such a structure
without being that structure.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet


REQUIRED_FOR_GUARDIAN = frozenset(
    {
        "local_odd_parameter",
        "nonzero_equivariant_odd_square",
        "rs_block_transformation",
        "gamma_trace_ward_identity",
        "super_higgs_scale_relation",
        "krein_square_compatibility",
    }
)


@dataclass(frozen=True)
class Candidate:
    name: str
    supplied: FrozenSet[str]
    expected_grade: str

    def missing(self) -> FrozenSet[str]:
        return REQUIRED_FOR_GUARDIAN - self.supplied

    def passes(self) -> bool:
        return not self.missing()


def dim_sp_pq_h(p: int, q: int) -> int:
    """Real dimension of sp(p,q;H), same as the compact real form sp(p+q)."""
    n = p + q
    return n * (2 * n + 1)


def dim_so(p: int, q: int) -> int:
    d = p + q
    return d * (d - 1) // 2


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        raise AssertionError(name)


def main() -> int:
    print("=" * 88)
    print("H54 guardian-symmetry gate: necessary conditions")
    print("=" * 88)

    # Anchor the current H54 data to the Wave 34/35 dimension bookkeeping.
    dim_sp = dim_sp_pq_h(32, 32)
    dim_spin_lift = dim_so(9, 5)
    codim_soldering = dim_sp - dim_spin_lift
    check(
        "dimension anchor for the even source-action arena",
        dim_sp == 8256 and dim_spin_lift == 91 and codim_soldering == 8165,
        f"dim sp(32,32;H)={dim_sp}, dim so(9,5)={dim_spin_lift}, codim={codim_soldering}",
    )

    current_h54_data = Candidate(
        name="current H54 data: Sp(32,32;H) plus [P,S]=0",
        supplied=frozenset(
            {
                "even_source_action_arena",
                "cartan_krein_involution",
                "finite_field_content",
                "krein_square_compatibility",
            }
        ),
        expected_grade="necessary-condition negative control",
    )

    formal_super_ig_with_beta = Candidate(
        name="formal super-IG after supplying Q and beta",
        supplied=frozenset(
            {
                "local_odd_parameter",
                "nonzero_equivariant_odd_square",
            }
        ),
        expected_grade="algebraic but not yet guardian",
    )

    supergravity_template = Candidate(
        name="supergravity gravitino template",
        supplied=REQUIRED_FOR_GUARDIAN,
        expected_grade="positive control",
    )

    expected_current_missing = frozenset(
        {
            "local_odd_parameter",
            "nonzero_equivariant_odd_square",
            "rs_block_transformation",
            "gamma_trace_ward_identity",
            "super_higgs_scale_relation",
        }
    )
    check(
        "current even data are not a guardian",
        not current_h54_data.passes() and current_h54_data.missing() == expected_current_missing,
        "passes Krein compatibility only; lacks Q, beta, RS-block action, Ward identity, and scale law",
    )

    expected_formal_missing = frozenset(
        {
            "rs_block_transformation",
            "gamma_trace_ward_identity",
            "super_higgs_scale_relation",
            "krein_square_compatibility",
        }
    )
    check(
        "a formal Q,beta super-IG algebra is still not a VZ/super-Higgs guardian",
        not formal_super_ig_with_beta.passes()
        and formal_super_ig_with_beta.missing() == expected_formal_missing,
        "odd algebra alone does not preserve Gamma psi=0 or pin mu_DW",
    )

    check(
        "positive control: the supergravity template satisfies the guardian checklist",
        supergravity_template.passes(),
        "local odd gauge symmetry, closure, Ward identity, and super-Higgs scale relation all present",
    )

    construction_burden = current_h54_data.missing()
    check(
        "H54 construction burden is exactly the missing guardian data",
        construction_burden == expected_current_missing,
        ", ".join(sorted(construction_burden)),
    )

    print("-" * 88)
    print("VERDICT: CURRENT_STRUCTURES_COMPATIBLE_BUT_NOT_GUARDIAN")
    print("The H54 question remains open only as a construction problem: supply Q, beta,")
    print("the RS/spin-1/2 transformation law, a gamma-trace Ward identity, and a")
    print("super-Higgs-like relation that pins mu_DW.  Sp(32,32;H)+[P,S]=0 alone")
    print("does not furnish those ingredients.")
    print("=" * 88)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
