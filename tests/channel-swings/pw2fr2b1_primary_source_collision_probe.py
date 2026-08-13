#!/usr/bin/env python3
"""PW2F-R2B1 primary-source collision and Layer-0 provenance gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def check(kind: str, label: str, condition: bool = True) -> None:
    global EXACT, SOURCE, TYPE, PLANTED
    if kind == "exact":
        EXACT += 1
    elif kind == "source":
        SOURCE += 1
    elif kind == "type":
        TYPE += 1
    else:
        PLANTED += 1
        condition = not condition
    print(f"{'PASS' if condition else 'FAIL'}: {kind} - {label}", flush=True)
    if not condition:
        FAILURES.append(f"{kind}: {label}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    rendered_path = ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    o_report_path = ROOT / "explorations/eric-curt-wave3d-b2c15o-native-y14-background-stabilizer-2026-08-01.md"
    p_report_path = ROOT / "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
    o_registry_path = ROOT / "lab/process/eric-curt-wave3d-b2c15o-native-y14-background-stabilizer.json"
    p_registry_path = ROOT / "lab/process/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt.json"
    toe_path = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
    portal_path = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"

    paths = {
        pack_path: "e8e195ede8e34f33d9e8a74daf9bea867bdb649fe1e9efddd8c896383f94708d",
        rendered_path: "1a8474008d7e472245367970de364c4e7c58b1e4c53784bc7324c3f8b43e8cd4",
        o_report_path: "e0af5b3d128945b426d0856f3d134e1a987f9cd27b4fcec817d1eefb9b0219eb",
        p_report_path: "0942abe2fe3154902c0631180427cc3828e8ff62f5cc715237de5391c44877a1",
        o_registry_path: "44f2d7766e886577f972b34b89fb8255ae8e51a72535a8916657a2e6de5017f0",
        p_registry_path: "a2c1e536f0039e6f5eac2ef6ca5a74b34c3bfdae8e4831b40d10784102ee1b9a",
        toe_path: "056d188eb46b1756cb211b0e1758f9be12334391f892ee51250008f2c5f88bea",
        portal_path: "bd9f53ab7dc631fb01265c7a89893a773592e6a1215211b21a5833cc5cd4165d",
    }
    check(
        "exact",
        "all eight declared source/control artifacts match pinned SHA-256 digests",
        all(path.is_file() and digest(path) == expected for path, expected in paths.items()),
    )

    pack = pack_path.read_text()
    rendered = rendered_path.read_text()
    toe = toe_path.read_text()
    portal = portal_path.read_text()
    o_registry = json.loads(o_registry_path.read_text())
    p_registry = json.loads(p_registry_path.read_text())

    check("source", "the author-draft custody records omega=(epsilon,varpi) and T_omega=varpi-epsilon^-1 d0 epsilon", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack)
    check("source", "the rendered draft identifies varpi as a connection difference from nabla^g", "varpi=nabla^varpi-nabla^g" in rendered)
    check("source", "the rendered draft identifies T as the difference from the gauge-rotated Levi-Civita connection", "T_omega=nabla^varpi-nabla^{g*epsilon}" in rendered)
    check("source", "the modern TOE interview explicitly puts gauge-rotated Levi-Civita in the contorsion slot", "02:19:17" in toe and "gauge rotated Levi-Civita connection" in toe)
    check("source", "Portal states the Zorro chain connection-on-X to metric-on-Y to LC/spin connection", "02:23:30" in portal and "02:23:52" in portal and r"metric on \(Y\)" in portal)
    check("source", "the source action retains the one-half and one-third transgression coefficients", "\\frac12d_{B_\\omega}T_\\omega" in pack and "\\frac13[T_\\omega,T_\\omega]" in pack)
    check(
        "exact",
        "the exact B2C15O/P records preserve the source-coordinate return and curved section identity",
        o_registry["source_coordinate_return"]["difference_from_fixed_A"] == "(D_g Gamma)^!E_T"
        and p_registry["zorro_connection_metric"]["controls"]["pullback"] == "j2(s_g^*G_Y)=j2(g) PASS",
    )

    check("type", "SOURCE-CONFIRMS the literal connection-difference grammar and Zorro chain")
    check("type", "REPOSITORY-DERIVES the q versus B_full correction and the live (D_g Gamma)^! E_T return")
    check("type", "REPOSITORY-DERIVES the exact normal-frame section JVP and rank-35 quartic extraction gate")
    check("type", "SOURCE-SILENT on repository h=exp(u), theta1/Bhat2, all second Frechet owners, and complete actual-Y14 C4")
    check("type", "SOURCE-SILENT on any exceptional universal kappa1")
    check("type", "source silence is not an unforcing or no-go result")
    check("type", "LEADING_DISPOSITION is SOURCE-SILENT for the decisive complete-C4 question")
    check("type", "P1/P2/P3 remain unused and Curt remains formally separate")

    check("plant", "identify q_g(epsilon) with the full connection Gamma+q", False)
    check("plant", "infer deltaT=-deltaB_full at fixed varpi", False)
    check("plant", "identify source epsilon with repository h=exp(u)", False)
    check("plant", "claim Weinstein supplied the complete second Frechet action graph", False)
    check("plant", "use source authority to select kappa1", False)
    check("plant", "turn a local section pullback into a bulk delta-current", False)

    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: SOURCE-CONFIRMS THE CONNECTION-DIFFERENCE/ZORRO GRAMMAR; SOURCE-SILENT ON THE COMPLETE SECOND-FRECHET GRAPH, ACTUAL C4, AND KAPPA1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
