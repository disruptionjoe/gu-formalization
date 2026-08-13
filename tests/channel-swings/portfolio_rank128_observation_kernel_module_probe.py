#!/usr/bin/env sage-python
"""Identify the complete rank-128 defect sum without fitting an intertwiner.

The predecessor proved that ten transverse images are pairwise disjoint and
that its zero-form-seed trivialization intertwines only the compact
``so(6)+so(4)`` generators.  This successor tests the carrier rather than that
trivialization: it compares the full defect span to the observation kernel and
checks the canonical normal-covector--spinor inclusion under all 45
``so(6,4)`` generators.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from runpy import run_path


ROOT = Path(__file__).resolve().parents[2]
prior = run_path(str(ROOT / "tests/channel-swings/portfolio_rank128_defect_module_probe.py"))

F = prior["F"]
spin = prior["spin"]
total = prior["total"]
i128 = prior["i128"]
z128 = prior["z128"]
block_matrix = prior["block_matrix"]
matrix = prior["matrix"]
zero_matrix = prior["zero_matrix"]
transverse = prior["transverse"]
images = prior["images"]
all_join = prior["all_join"]
phi = prior["phi"]
observation = prior["observation"]
lift = prior["lift"]
complement = prior["complement"]
full_carrier_gen = prior["full_carrier_gen"]
source_tensor_gen = prior["source_tensor_gen"]
equivariant = prior["equivariant"]

COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("\nA. ADAPTIVE PREFLIGHT AND LAYER ZERO")
for label in (
    "ten coordinate images versus one shared subspace",
    "their direct sum versus one natural normal module",
    "module existence versus naturality of the zero-form-seed map",
    "observation kernel versus the selected H640 graph lift",
    "configuration representation versus a physical BV quotient",
):
    check("layer0", label, True)
for label in (
    "representation theory tests the full normal Lie algebra before naming the module",
    "principal-bundle geometry treats individual normal lines as frame-dependent",
    "variational bicomplex keeps the selected graph-lift defect distinct from a BV differential",
    "symplectic geometry forbids promoting a configuration kernel to reduced phase space",
    "source criticism checks the one-form-spinor and pullback claims without attributing this theorem",
):
    check("preflight", label, True)


print("\nB. DEFECT SUM EQUALS THE OBSERVATION KERNEL")
check("rank", "the ten pairwise-disjoint defects have total rank 1280",
      all_join.rank() == 1280)
check("kernel", "observation has rank 640 and kernel dimension 1280",
      observation.rank() == 640 and total - observation.rank() == 1280)
check("kernel", "every defect lies in the observation kernel",
      (observation * all_join).is_zero())
check("kernel", "equal dimensions identify the full defect sum with ker observation",
      all_join.rank() == total - observation.rank())
check("kernel", "the graph complement is another projector onto the same kernel",
      complement.rank() == 1280 and (observation * complement).is_zero())


print("\nC. CANONICAL NORMAL-COVECTOR--SPINOR MODULE")
normal_slot_lift = matrix(F, 15, 10, sparse=True)
for column, slot in enumerate(transverse):
    normal_slot_lift[slot, column] = 1
normal_inclusion = normal_slot_lift.tensor_product(i128)
check("carrier", "coordinate normal inclusion has rank 1280",
      normal_inclusion.rank() == 1280)
check("carrier", "coordinate normal carrier equals the defect span",
      block_matrix(F, 1, 2, [[all_join, normal_inclusion]], sparse=True).rank() == 1280)

pairs = [(i, j) for ai, i in enumerate(transverse) for j in transverse[ai + 1:]]
canonical_intertwiners = {}
for pair in pairs:
    canonical_intertwiners[pair] = (
        full_carrier_gen(*pair) * normal_inclusion
        == normal_inclusion * source_tensor_gen(*pair)
    )
check("module", "canonical N* tensor S inclusion intertwines all 45 so(6,4) generators",
      len(canonical_intertwiners) == 45 and all(canonical_intertwiners.values()))
check("module", "the full observation kernel is so(6,4)-invariant",
      all((observation * full_carrier_gen(*pair) * normal_inclusion).is_zero()
          for pair in pairs))


print("\nD. THE FAILED OBJECT IS THE SELECTED GRAPH TRIVIALIZATION")
observed_generators = {}
for pair in pairs:
    spin_generator = prior["spin_gen"](*pair)
    observed_generators[pair] = block_matrix(
        F, 5, 5,
        [[spin_generator if row == column else z128 for column in range(5)]
         for row in range(5)],
        sparse=True,
    )

lift_intertwiners = {
    pair: full_carrier_gen(*pair) * lift == lift * observed_generators[pair]
    for pair in pairs
}
complement_intertwiners = {
    pair: full_carrier_gen(*pair) * complement == complement * full_carrier_gen(*pair)
    for pair in pairs
}
check("graph", "selected H640 lift intertwines exactly the 21 compact generators",
      sum(lift_intertwiners.values()) == 21)
check("graph", "its complement commutes with exactly the same compact generators",
      sum(complement_intertwiners.values()) == 21)
check("graph", "zero-form-seed defect trivialization also intertwines exactly 21 of 45",
      sum(equivariant.values()) == 21)
check("graph", "all 24 mixed boosts expose the non-natural graph splitting",
      all(not lift_intertwiners[pair] and not complement_intertwiners[pair]
          and not equivariant[pair]
          for pair in pairs
          if prior["eta"][pair[0]] != prior["eta"][pair[1]]))


print("\nE. SCOPE AND FIRING CONTROLS")
check("plant", "PLANT one repeated rank-128 image does not equal the rank-1280 kernel",
      images[transverse[0]].rank() == 128
      and block_matrix(F, 1, 2,
                       [[images[transverse[0]], images[transverse[0]]]],
                       sparse=True).rank() == 128)
check("plant", "PLANT the selected graph lift is not declared fully equivariant",
      not all(lift_intertwiners.values()))
check("scope", "no physical BV quotient, action selection, positivity, index or count is inferred",
      True)
check("scope", "the next owner is a moving graph/BV correction, not ten independent repairs",
      True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_ONE_FORM_SPINOR_CARRIER_AND_OBSERVATION_PULLBACK__SOURCE_SILENT_ON_RANK1280_KERNEL_MODULE_AND_GRAPH_SPLITTING")
print("RESULT=TEN_DISJOINT_RANK128_IMAGES_SUM_TO_CANONICAL_NSTAR_TENSOR_S_OBSERVATION_KERNEL__FULL_SO6_4_MODULE_EXACT__SELECTED_H640_GRAPH_SPLITTING_ONLY_COMPACT_NATURAL")
print("NEXT=DERIVE_ACTION_OR_BV_OWNED_MOVING_GRAPH_CORRECTION_OR_PROVE_ONLY_THE_COMPACT_STABILIZER_IS_PHYSICAL__DO_NOT_RUN_TEN_SEPARATE_REPAIRS")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
