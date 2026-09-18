#!/usr/bin/env python3
"""K240: common-anchor quartic shell decomposition, not an R5 certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json

from k225_order_six_diagonal_cancellation import ROOT
from k239_order_six_projected_quartic_cube_moment import cube_data

OUT = ROOT / "lab/process/k240-order-six-common-anchor-shell.json"
K232 = ROOT / "lab/process/k232-order-six-quartic-sos.json"
K239 = ROOT / "lab/process/k239-order-six-projected-quartic-cube-moment.json"


def polynomial(q: int) -> list[str]:
    """K(q)=15 (M0*M2-M1**2)^2 M0**2, in powers of log(q)."""
    data = cube_data(q)
    return data["weighted_six_coordinate_P_moment_coefficients_in_log_q"]


def generate() -> dict:
    prior = json.loads(K239.read_text())
    sos = json.loads(K232.read_text())
    assert len(prior["cubes"]) == 2 and sos["square_count"] == 45
    assert all(polynomial(q) == next(c for c in prior["cubes"] if c["q"] == q)[
        "weighted_six_coordinate_P_moment_coefficients_in_log_q"] for q in (4, 5))
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem: sha256(p.read_bytes()).hexdigest() for p in (K232, K239)},
        "object": "K230 S6-projected original signed K185/K218 rational-cosh core on nested q=4,5 full cubes, not the unsymmetrized pointwise core or a physical state",
        "anchor_independence": "K232 P is invariant under a common translation of all six coordinates. Thus for ANY fixed b, not only the q-dependent weighted center, int_[0,T]^6 P(c2-b,...,c7-b) product_(2..7) cosh(tj)dtj = K(q)=15 V(q)^2 M0(q)^4. Translation invariance permits setting b=M1/M0 for the proof, but the identity itself does not require that center.",
        "nested_shell_theorem": "Let Tq=log(q), L=[0,T4], U=[0,T5], W=product_(0..7)cosh(tj), Hbar=K230 projection, A_b(u,v)=K231 quartic coefficient at common fixed b, R_b=Hbar-A_b(c0,c1)P(c2-b,...,c7-b), and C=2^8*256^6/(5!*pi^8). Then C*int_(U^8\\L^8) W Hbar = C*[(K5-K4)*int_(L^2) cosh(t0)cosh(t1) A_b(c0,c1)dt0dt1 + K5*int_(U^2\\L^2) cosh(t0)cosh(t1) A_b(c0,c1)dt0dt1 + int_(U^8\\L^8) W R_b]. The two-dimensional shell U^2\\L^2 splits disjointly as (U\\L)*U union L*(U\\L). All three terms share the SAME b, hence the common low-square quartic contribution is combined algebraically before any upper enclosure. This equality also holds for the original H after integration over these S6-invariant domains, not pointwise.",
        "strict_increment": "M0(q)>0 and D(q)=M0*M2-M1^2=(1/2)*int_[0,Tq]^2 cosh(s)cosh(t)*(cosh(s)-cosh(t))^2 dsdt>0. Enlarging T strictly increases D and M0, so K5-K4=15*(D5^2*M0(5)^2-D4^2*M0(4)^2)>0. Positivity of this geometric factor does NOT establish a sign for A_b or R_b.",
        "quartic_factor_polynomial_log_q": {str(q): polynomial(q) for q in (4, 5)},
        "required_next_certificate": "Bound variable A_b on the low square and two disjoint high strips together with the signed SAME-anchor shell integral of R_b, accounting for pi^-8, K224's remaining 1.7933e-22 and evaluation cost. A pair of independent absolute cube remainder bounds can still lose common cancellation. Optimize b only with a rigorous covered residual/cost test.",
        "source_routing": "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. This is internal integration algebra only.",
        "claim_ceiling": "Exact common-anchor quartic shell identity and positive geometric increment, not a sign or bound on A_b or R_b, a signed whole-shell upper, feasible cost, complete K215 prefix, physical action/state, source/ledger/canon/public change."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K240 common-anchor signed shell identity")
