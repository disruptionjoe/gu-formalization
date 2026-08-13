#!/usr/bin/env python3
"""PW2F-R2 primary-source and Layer-0 collision for total swervature."""

from __future__ import annotations

import hashlib
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
    portal_path = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
    rendered_path = ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    g2_path = ROOT / "explorations/g2-field-space-native-variational-shiab-2026-07-31.md"
    pack = pack_path.read_text()
    portal = portal_path.read_text()
    rendered = rendered_path.read_text()
    g2 = g2_path.read_text()

    expected_digests = {
        pack_path: "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f",
        portal_path: "bd9f53ab7dc631fb01265c7a89893a773592e6a1215211b21a5833cc5cd4165d",
        rendered_path: "1a8474008d7e472245367970de364c4e7c58b1e4c53784bc7324c3f8b43e8cd4",
        g2_path: "0fdad12722887a1ece6bf65085c5ca7b3cfbb19df1d661d9b08ee218ad593c29",
    }
    check("exact", "all four declared evidence/control artifacts match pinned SHA-256 digests", all(digest(path) == expected for path, expected in expected_digests.items()))
    check("source", "author-draft custody records the official PDF digest", "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4" in pack)
    check("source", "draft equation 9.4 fixes the one-half/one-third first-action grammar", "\\frac12d_{B_\\omega}T_\\omega" in pack and "\\frac13[T_\\omega,T_\\omega]" in pack)
    check("source", "rendered pages 44-45 record action, Euler packet, and gathered swervature equation", "DGU01-TR-03" in rendered and "DGU01-TR-04" in rendered and "Upsilon" in rendered)
    check("source", "Portal 02:35:10 requires a quadratic eddy for variational exactness", "02:35:10" in portal and "quadratic eddy tensor" in portal and "total swervature" in portal)
    check("source", "Portal 02:41:39 calls the eddy quadratic in augmented torsion", "02:41:39" in portal and "eddy tensor, which is quadratic in the augmented torsion" in portal)
    check("source", "Portal places the equation upstairs on Y before pullback to X", "not on \\(X\\)" in portal and "on \\(Y\\)" in portal)
    check("source", "the draft compressed translation variation and native noncyclic slot variation are recorded as a live fork", "slot-symmetrized" in g2 and "compressed" in g2)

    check("type", "SOURCE-CONFIRMS the need for the eddy completion, not a component formula for the active native C4")
    check("type", "the source locates an eddy on the Euler/current side; a repository identification must be derived from the full Euler variation without double-counting action inputs")
    check("type", "literal odot_epsilon, abbreviated odot_omega, and the repository moving noncentral contraction remain distinct")
    check("type", "source epsilon and repository h=exp(u) remain distinct")
    check("type", "metric-section tangent, observation-current motion, and equation pushdown remain distinct")
    check("type", "source silence on the active C4 is not a no-go")
    check("type", "P1/P2/P3 remain unused; Curt remains separate; the conjunctive third-lane gate stays closed")

    check("plant", "identify the Portal eddy with the action integrand's 1/3 bracket term by shared quadratic language", False)
    check("plant", "treat the draft compressed Upsilon as the native noncyclic Euler covector without the G2 slot test", False)
    check("plant", "insert the observation delta-current into the smooth Y bulk C4", False)
    check("plant", "use source authority to select kappa1", False)
    check("plant", "call a finite G2 restriction the complete Y14 metric coefficient", False)

    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: SOURCE-SILENT ON THE REPOSITORY EDDY CANDIDATE, FINITE-FAMILY C4, AND KAPPA1; SOURCE CONFIRMS ONLY THE ACTION GRAMMAR AND AN UNSPECIFIED EDDY COMPLETION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
