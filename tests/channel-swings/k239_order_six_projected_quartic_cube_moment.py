#!/usr/bin/env python3
"""K239: exact K218-weighted six-coordinate moment of K231's quartic."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json

from k225_order_six_diagonal_cancellation import ROOT

OUT = ROOT / "lab/process/k239-order-six-projected-quartic-cube-moment.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K231 = ROOT / "lab/process/k231-order-six-projected-diagonal-jet.json"
K232 = ROOT / "lab/process/k232-order-six-quartic-sos.json"


def cube_data(q: int) -> dict:
    assert q > 1
    # K218's density is cosh(t) dt, NOT sinh(t) dt. Write T=log(q).
    s = Q(q*q-1, 2*q)  # sinh(T)
    c = Q(q*q+1, 2*q)  # cosh(T)
    m0 = s
    m1_const = s*c/2  # int cosh(t)^2 dt = T/2+sinh(2T)/4
    m1_log = Q(1, 2)
    m2 = s+s**3/3  # int cosh(t)^3 dt, z=sinh(t)
    # b(q)=(m1_const+m1_log*T)/m0. The unnormalized variance
    # V=int cosh(t)*(cosh(t)-b)^2 dt = m2-m1^2/m0.
    v = (m2-m1_const**2/m0,
         -2*m1_const*m1_log/m0,
         -m1_log**2/m0)
    square = tuple(sum((v[i]*v[k-i] for i in range(max(0,k-2), min(2,k)+1)), Q())
                   for k in range(5))
    moment = tuple(15*m0**4*entry for entry in square)
    return {"q": q, "T": f"log({q})", "cosh_T": str(c),
            "m0": str(m0), "m1_constant": str(m1_const),
            "m1_log_coefficient": str(m1_log), "m2": str(m2),
            "center_b_coefficients_in_log_q": [str(m1_const/m0), str(m1_log/m0)],
            "unnormalized_centered_second_coefficients_in_log_q": list(map(str,v)),
            "weighted_six_coordinate_P_moment_coefficients_in_log_q": list(map(str,moment))}


def generate() -> dict:
    k218 = json.loads(K218.read_text())
    k230 = json.loads(K230.read_text())
    k231 = json.loads(K231.read_text())
    k232 = json.loads(K232.read_text())
    assert k218["terms"] == 1864 and k230["retained_orbits"] == 307
    assert "quartic_normal_form" in k231 and k232["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem: sha256(p.read_bytes()).hexdigest()
                         for p in (K218, K230, K231, K232)},
        "object": "K230 S6-projected original signed K185/K218 rational-cosh core Hbar, not the unsymmetrized pointwise core or a physical state",
        "measure_identity": "K218 integrates H with product_j cosh(t_j)dt_j, not sinh(t_j)dt_j. For z_j=sinh(t_j), the measure is product_j dz_j while the denominator coordinates c_j=cosh(t_j)=sqrt(1+z_j^2). In c coordinates the density is product_j c_j/sqrt(c_j^2-1)dc_j. Uniform c moments are inapplicable.",
        "quartic_moment_theorem": "Fix u=c0,v=c1, q>1 and T=log(q). Put M_k=int_0^T cosh(t)^(k+1)dt for k=0,1,2, b=M1/M0, x_j=cosh(t_j)-b for j=2..7. K231's quartic is A(u,v,b)P(x), P=m22-m211/2+m1111. The six c_j are independent under product cosh(t_j)dt_j; their centered first integral is zero and centered second integral V=M2-M1^2/M0. Thus all m211/m1111 integrals vanish, and the fifteen m22 terms give exactly int_[0,T]^6 product_j cosh(t_j)dt_j P(c-b)=15 V^2 M0^4. M0=sinh(T), M1=T/2+sinh(2T)/4, M2=sinh(T)+sinh(T)^3/3. This is an analytic identity; the log(q) polynomial coefficients are serialized exactly.",
        "full_cube_quartic_formula": "For each q=4,5, the projected quartic contribution on [0,log(q)]^8 is C*15*V(q)^2*M0(q)^4 * int_0^T int_0^T cosh(t0)cosh(t1) A(cosh(t0),cosh(t1),b(q)) dt0dt1, C=2^8*256^6/(5!*pi^8). The complete third shell is q=5 cube minus q=4 cube, including the separately integrated R5=Hbar-A*P remainders. This is an exact decomposition, not a certified error or two-dimensional cubature.",
        "cubes": [cube_data(4), cube_data(5)],
        "required_next_certificate": "Uniform signed enclosure for A on each weighted u/v square and an integrated correlated bound for R5 on both full cubes, or a direct shell enclosure preserving common contributions; then compose pi^-8, K224's remaining 1.7933e-22 and practical evaluation cost. Difference of two absolute cube uppers may lose cancellation.",
        "source_routing": "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. Internal mathematics, not source-action or physical-state evidence.",
        "claim_ceiling": "Exact K218-weighted six-dimensional quartic polynomial moment for K230's S6-projected core on the q=4,5 full cubes. No uniform A sign/upper, R5 remainder or whole-shell bound, feasible cost, K215 prefix, coalescent/quotient/common-reference composition, source/physics/ledger/canon/public move."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K239 weighted quartic moment", [x["q"] for x in result["cubes"]])
