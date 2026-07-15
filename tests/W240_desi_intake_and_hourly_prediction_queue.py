#!/usr/bin/env python
"""W240 DESI intake and dependency-aware hourly prediction-queue audit.

This deterministic receipt does not validate cosmology from first principles and does
not create a GU prediction. It checks the external-report provenance, demonstrates the
material distance-table mismatch against the already primary-source-verified H46B
values, preserves the verified CPL summaries, and proves that the ten-persona W239
register is covered exactly once by the new work packets.

Run: python -u tests/W240_desi_intake_and_hourly_prediction_queue.py
"""

from __future__ import annotations

import ast
import hashlib
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "lab/deep-research/desi-late-time-dark-energy-cpl-external-report-2026-07-15.md"
W239 = ROOT / "tests/W239_track_b_distinctive_prediction_scan.py"
W240 = ROOT / "explorations/W240-desi-intake-and-hourly-prediction-queue-2026-07-15.md"
NEXT = ROOT / "NEXT-STEPS.md"
LAB_README = ROOT / "lab/deep-research/README.md"

EXPECTED_RAW_SHA256 = "ca125e1f16ee439cdadf3e20ab0198f6fe04baf63858844556743310b022d49a"
FAIL: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    state = "PASS" if condition else "FAIL"
    print(f"{state} :: {name}" + (f"  --  {detail}" if detail else ""))
    if not condition:
        FAIL.append(name)


def extract_literal_assignment(path: Path, name: str):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return ast.literal_eval(node.value)
    raise RuntimeError(f"literal assignment {name!r} not found in {path}")


@dataclass(frozen=True)
class Packet:
    key: str
    impact: int
    first_run_difficulty: int
    state: str
    dependencies: tuple[str, ...] = ()


PACKETS = (
    Packet("DE-AMP", 4, 2, "READY"),
    Packet("FLAVOR-RANK", 5, 2, "READY"),
    Packet("NORM-RANK", 5, 3, "READY"),
    Packet("FLAVOR-OBS", 5, 3, "GATED", ("FLAVOR-RANK",)),
    Packet("PHYSICAL-C", 5, 5, "READY_AFTER_FAST_GATES",
           ("DE-AMP", "FLAVOR-RANK", "NORM-RANK")),
    Packet("POLE-PACKET", 5, 4, "GATED", ("NORM-RANK", "PHYSICAL-C")),
    Packet("MIRROR-ESCAPE", 5, 4, "READY"),
    Packet("MIRROR-PACKET", 5, 5, "GATED", ("MIRROR-ESCAPE", "PHYSICAL-C")),
    Packet("COSMO-X", 4, 4, "GATED", ("DE-AMP",)),
    Packet("RECORD-X", 3, 4, "BACKLOG"),
)


TARGET_PACKETS = {
    "basis-invariant Yukawa singular-value ratio": "FLAVOR-RANK",
    "Z/3 texture-zero mixing sum rule": "FLAVOR-OBS",
    "Dirac-only neutrino mass selection": "FLAVOR-OBS",
    "zero-parameter relation among measured SM inputs": "FLAVOR-OBS",
    "dimensionless overconstraint of existing data": "FLAVOR-OBS",
    "sign prediction opposite a live competitor": "FLAVOR-OBS",

    "physical extra-pole residue and line shape": "PHYSICAL-C",
    "renormalization-group fixed coupling ratio": "PHYSICAL-C",
    "threshold matching relation across GU sectors": "PHYSICAL-C",
    "physical mirror cohomology parity": "PHYSICAL-C",
    "positivity-fixed sign of a scattering interference term": "PHYSICAL-C",
    "channel-S allowed and channel-D forbidden chiral spectrum": "PHYSICAL-C",

    "fixed-strength fixed-range short-distance force": "POLE-PACKET",
    "massive-spin-2 gravitational-wave dispersion": "POLE-PACKET",
    "parameter-free Kerr ringdown correction": "POLE-PACKET",
    "dark-energy to spin-2 scale ratio": "NORM-RANK",
    "exact observable ratio of Einstein Weyl and vacuum terms": "NORM-RANK",
    "fixed tensor ratios in the source response function": "NORM-RANK",
    "torsion-balance force with predeclared alpha and lambda": "POLE-PACKET",

    "complete vectorlike mirror multiplet spectrum": "MIRROR-PACKET",
    "SO(10)-fixed mirror branching-fraction ratios": "MIRROR-PACKET",
    "channel-S composite resonance pattern": "MIRROR-ESCAPE",
    "topologically protected spectral multiplicity": "MIRROR-ESCAPE",
    "fixed-rate mirror production and decay packet": "MIRROR-PACKET",
    "complete correlated smoking-gun spectrum": "MIRROR-PACKET",

    "predeclared w(z) width and crossing shape": "COSMO-X",
    "fixed sign relation between w(z) and f-sigma8": "COSMO-X",

    "retarded record-current transfer function": "RECORD-X",
    "record-creation gravitational memory signal": "RECORD-X",
    "capability-change correlated source pulse": "RECORD-X",
}


def main() -> int:
    raw_bytes = RAW.read_bytes()
    raw = raw_bytes.decode("utf-8")
    w240 = W240.read_text(encoding="utf-8")
    next_steps = NEXT.read_text(encoding="utf-8")
    lab_readme = LAB_README.read_text(encoding="utf-8")
    compact_next = " ".join(next_steps.replace(">", " ").replace("**", "").split())
    compact_lab_readme = " ".join(lab_readme.split())

    print("== EXTERNAL REPORT PROVENANCE ==")
    digest = hashlib.sha256(raw_bytes).hexdigest()
    check("R1 moved report is preserved byte-for-byte", digest == EXPECTED_RAW_SHA256, digest)
    check("R2 report remains explicitly external and non-authoritative in the index",
          "external" in compact_lab_readme.lower()
          and "not a numerical source" in compact_lab_readme.lower()
          and RAW.name in compact_lab_readme)
    check("R3 unusable internal citation tokens are detected rather than trusted",
          raw.count("cite") >= 20 and "internal search tokens" in w240)

    print("\n== MATERIAL DR2 DISTANCE-TABLE FAILURE ==")
    # Values claimed by the external report versus the official DR2 Table 4 values
    # independently verified in H46B. Official sigma is the paper's printed sigma.
    comparisons = (
        ("LRG1 DH", 20.97, 21.863, 0.425),
        ("LRG2 DM", 16.84, 17.351, 0.177),
        ("LRG2 DH", 20.08, 19.455, 0.330),
        ("LRG3+ELG1 DM", 21.77, 21.576, 0.152),
        ("LRG3+ELG1 DH", 17.83, 17.641, 0.193),
        ("ELG2 DM", 27.56, 27.601, 0.318),
        ("ELG2 DH", 13.83, 14.176, 0.221),
        ("Lya DH", 8.53, 8.632, 0.101),
        ("Lya DM", 39.40, 38.988, 0.531),
    )
    pulls = {name: abs(report - official) / sigma
             for name, report, official, sigma in comparisons}
    for name, pull in pulls.items():
        print(f"{name:16s} mismatch = {pull:.2f} official printed sigma")
    check("D1 at least four alleged DR2 means miss by more than 1.5 official sigma",
          sum(pull > 1.5 for pull in pulls.values()) >= 4, str(pulls))
    check("D2 one alleged DR2 mean misses by more than 2.5 official sigma",
          max(pulls.values()) > 2.5, str(max(pulls.values())))
    check("D3 the report also changes the QSO observable from DR2 anisotropic DM,DH to DV",
          "QSO" in raw and "D_V/r_d=26.10" in raw
          and "anisotropic QSO" in w240)

    print("\n== VERIFIED CPL CONTENT AND SCOPE ==")
    cpl_tokens = (
        "-0.42\\pm0.21", "-1.75\\pm0.58",
        "-0.838\\pm0.055", "-0.62^{+0.22}_{-0.19}",
        "-0.667\\pm0.088", "-1.09^{+0.31}_{-0.27}",
        "-0.752\\pm0.057", "-0.86^{+0.23}_{-0.20}",
    )
    check("C1 all four H46B-verified CPL summaries occur in the report",
          all(token in raw for token in cpl_tokens))
    check("C2 W240 keeps raw likelihood, CPL compression, CMB anchor, and SN calibration distinct",
          all(token in w240 for token in
              ("raw BAO distances", "CPL posterior", "CMB", "supernova")))
    check("C3 no current prediction or gate is promoted",
          "No current GU prediction has been found" in w240
          and "bar(b) and H59 remain OPEN" in w240)

    print("\n== W239 THIRTY-TARGET COVERAGE ==")
    proposals = extract_literal_assignment(W239, "persona_proposals")
    targets = [row[2] for row in proposals]
    check("M1 W239 still contains exactly 30 targets", len(targets) == 30)
    check("M2 W239 targets are unique", len(targets) == len(set(targets)))
    check("M3 W240 packet map covers every W239 target exactly once",
          set(TARGET_PACKETS) == set(targets),
          f"missing={sorted(set(targets) - set(TARGET_PACKETS))}; "
          f"extra={sorted(set(TARGET_PACKETS) - set(targets))}")
    packet_keys = {packet.key for packet in PACKETS}
    check("M4 every mapped target points to a declared packet",
          set(TARGET_PACKETS.values()) <= packet_keys)
    plain_w240 = w240.replace("`", "")
    check("M5 the written W240 mapping carries every exact target label",
          all(target in plain_w240 for target in targets))

    print("\n== DEPENDENCY-AWARE HOURLY ORDER ==")
    keys = [packet.key for packet in PACKETS]
    check("Q1 queue begins with three bounded first-run audits",
          keys[:3] == ["DE-AMP", "FLAVOR-RANK", "NORM-RANK"]
          and all(packet.first_run_difficulty <= 3 for packet in PACKETS[:3]))
    check("Q2 protected physical-state North Star precedes dependent pole and mirror packets",
          keys.index("PHYSICAL-C") < keys.index("POLE-PACKET")
          and keys.index("PHYSICAL-C") < keys.index("MIRROR-PACKET"))
    check("Q3 every dependency is declared earlier than its consumer",
          all(keys.index(dep) < keys.index(packet.key)
              for packet in PACKETS for dep in packet.dependencies))
    check("Q4 external releases are passive monitors, not hourly work",
          "These are not hourly work" in w240
          and "passive release monitoring consumes no hourly run" in w240)
    check("Q5 NEXT-STEPS names W240 as the active hourly queue",
          "W240" in next_steps
          and "HOURLY TRACK B PREDICTION QUEUE" in next_steps
          and "highest-ranked READY" in next_steps)
    check("Q6 queue forbids target calibration and qualitative re-brainstorming",
          "No target data may be used" in compact_next
          and "Do not run another qualitative prediction brainstorm" in compact_next)

    print("\n== GOVERNANCE ==")
    check("G1 W240 is exploration-tier and preserves both open gates",
          "Exploration-tier only" in w240 and "bar(b) and H59 remain OPEN" in w240)
    check("G2 no em dash was introduced in GU-authored W240", "\N{EM DASH}" not in w240)

    print("\n" + "=" * 72)
    if FAIL:
        print(f"W240 RESULT: FAIL ({len(FAIL)} checks)")
        for name in FAIL:
            print(f" - {name}")
        return 1
    print("W240 RESULT: PASS")
    print("External report quarantined as evidence; 30 targets fully mapped; queue is live.")
    print("No current distinctive GU prediction. bar(b) and H59 remain OPEN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
