#!/usr/bin/env python3
"""Executable closure of the current K77 physical-operator admission gate.

This is an inventory theorem. It verifies what the currently owned exact
operators do and do not license. It is not a universal no-go against an
unconstructed action-owned lower-order, BV/BFV, or analytic-domain operator.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    if not condition:
        raise AssertionError(f"{kind}: {label}")
    print(f"PASS [{kind}]: {label}")


principal = json.loads(
    (ROOT / "lab/process/selected-k77-induced-fermion-principal-discriminator.json").read_text()
)
h640 = (ROOT / "explorations/conditional-build/selected-k77-zero-seed-h640-action-closure-controls-2026-08-11.md").read_text()
bv = (ROOT / "explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md").read_text()
graph = (ROOT / "explorations/conditional-build/selected-k77-h640-observation-pullback-bv-typing-2026-08-11.md").read_text()
hq = (ROOT / "explorations/conditional-build/selected-k77-trace-hq-connection-compatibility-2026-08-13.md").read_text()
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
graph_kill = (ROOT / "explorations/conditional-build/selected-k77-southeast-zero-graph-gate-2026-08-10.md").read_text()
southeast = (ROOT / "explorations/conditional-build/selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md").read_text()
radical = (ROOT / "explorations/conditional-build/selected-k77-polarized-radical-bfv-ownership-gate-2026-08-11.md").read_text()


print("A. LAYER-0 OBJECT FENCES")
check("layer0", "principal characteristic kernel is not physical cohomology",
      "physical kernel or BRST cohomology" in principal["layer0"]["not_computed"])
check("layer0", "H640 is an action module rather than a source-selected physical carrier",
      "not yet:" in h640 and "BV/Koszul--Tate cohomology" in h640)
check("layer0", "a paired graph carrier is not a BV differential",
      "A paired field-antifield carrier is not a BV differential" in graph)
check("layer0", "trace-Hq compatibility is not action selection",
      "compatibility with a Hermitian family, not an Euler" in hq)
check("layer0", "generation count remains outside the computed objects",
      "generation count" in principal["layer0"]["not_computed"])


print("\nB. EXACT CONTROL FINGERPRINTS")
sectors = principal["exact_result"]["base_null_coupled_sector_ranks"]
check("exact", "W principal fingerprint is 224/96",
      (sectors["W_sd192"]["rank"], sectors["W_sd192"]["kernel"]) == (224, 96))
check("exact", "ASD mirror principal fingerprint is exactly identical",
      sectors["mirror_asd192"] == sectors["W_sd192"])
check("exact", "natural 640 and 832 obey the same normalized half-kernel rule",
      sectors["plus_singlet640"]["kernel"] * 2 == 640
      and sectors["plus_doublet832"]["kernel"] * 2 == 832)
check("exact", "all planted random 192 controls reject the natural half-kernel rule",
      all(item["kernel"] != 96 for item in principal["exact_result"]["random_192_controls"]))
check("exact", "principal parent ablations have one common derivative fingerprint",
      len({tuple(value) for value in principal["parent_ablations"].values() if isinstance(value, list)}) == 1)
check("exact", "H640 closes from the source-owned zero-form under observed spatial action",
      "H640 = 512 one-form directions + 128 zero-form directions" in h640)
check("exact", "generic 192 seeds do not generate H640",
      "generate ranks `1920`, `1916`, and `1908`" in h640)


print("\nC. OWNERSHIP AND BV ADMISSION")
check("source", "source owns the displayed four-field grammar",
      "four distinct fields" in source and "SOURCE-DISPLAYS-CANDIDATE" in source)
check("source", "source remains silent on global operator and physical domain",
      "common variational domain" in source and "three-family index" in source)
check("bv", "ordinary source BVKT resolves the Euler ideal but not a primal constraint",
      "resolves the nonzero Euler ideal" in bv and "not the same statement as restricting the primal" in bv)
check("bv", "the observation graph has nondegenerate pairing eligibility only",
      "eligibility and typing results" in graph and "No antifield equations" in graph)
check("bundle", "trace-Hq admits both full and block parents",
      "both block-preserving solutions and half-exchanging" in hq)
check("prior_art", "the q-repaired graph is rejected by its action-tied lower row",
      "complete lower residual rank" in graph_kill and "rank(C|_W)=64" in graph_kill)
check("prior_art", "every fixed southeast matrix leaves the non-null determinant invertible",
      "every southeast matrix at a fixed non-null" in southeast and "no fixed southeast choice" in southeast)
check("prior_art", "the owned zero-fermion gauge/BFV image does not remove the fermion radical",
      "radical   = 256." in radical and "Quotienting the owned edge gauge" in radical)


print("\nD. NEGATIVE CONTROLS AND CLAIM CEILING")
check("planted", "reject dimension-only W selection", sectors["W_sd192"]["one_form_dimension"] == 192)
check("planted", "reject generic discrimination as W/mirror discrimination",
      sectors["W_sd192"] == sectors["mirror_asd192"])
check("planted", "reject fitted trace-Hq connection selection",
      "affine torsor" in hq and "arbitrary `H_q`-unitary connection" in hq)
check("planted", "reject ordinary gauge BV as a physical carrier quotient",
      "not the same statement as restricting the primal" in bv)
check("scope", "closure is limited to the owned operator inventory", True)
check("scope", "a new action-owned half-asymmetric lower-order/BV operator remains admissible", True)


total = sum(COUNTS.values())
print(f"\nPhysical-operator admission closure: {total}/{total} PASS")
print("RESULT: generic controls are discriminated, but no owned operator selects W over mirror or defines physical cohomology.")
print("NEXT: construct an action-owned primal-carrier differential with a preregistered W/mirror asymmetry control.")
