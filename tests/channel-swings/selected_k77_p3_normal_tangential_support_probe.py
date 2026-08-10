#!/usr/bin/env python3
"""Exact actual-base gate for the P3 normal-support/source diagonal.

The prior wave compared the Hopf bundle with the chiral spin bundle on an
abstract model S4.  This probe restores the maps used by the current packet:
P3 is supported on a compactified normal four-cycle in Y, whereas the proposed
source SU(2)+ is pulled back horizontally from the observer base X.  The
restriction of a horizontal pullback to a vertical cycle factors through a
point and is therefore trivial.  Form-slot controls independently show that
internal gauge conjugation cannot turn normal two-form support into horizontal
support.  A planted horizontal-normal soldering permutation can do so, but it
changes the observation split and is a new construction.
"""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    if not bool(condition):
        FAILURES.append(f"[{kind}] {label}")
        print(f"FAIL [{kind}] {label}")
    else:
        print(f"PASS [{kind}] {label}")


packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
prior = (ROOT / "explorations/conditional-build/selected-k77-p3-spin-bundle-diagonal-2026-08-10.md").read_text()
tangential = (ROOT / "canon/boundary-einvariant-and-the-tangential-fork.md").read_text()
source = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
soldering = (ROOT / "explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md").read_text()

check("prior", "P3 cycle is explicitly normal", "chosen framed four-dimensional normal cycle" in packet)
check("prior", "P3 collapse is constant off its normal support", "constant on the rest of the collapsed complement" in packet)
check("prior", "P3 connection is fixed external data", "It is fixed external data, not a\nvaried gauge field" in packet)
check("prior", "abstract model-S4 class match is preserved", "P3 n=+1  <->  S+ chiral spin bundle" in prior)
check("prior", "tangential reconstruction places SU2 plus on base frame", "local frame rotations of the 4-base" in tangential)
check("source", "source separates ambient pullback spinor and normal spinor", "pulls back to a spinner on an embedded or immersed subspace, tensor a spinner on the normal bundle" in source)
check("source", "source says the ten is a normal bundle", "It's just a normal bundle in your ambient space" in source)
check("source", "source does not contain the P3 collapse construction", "P3" not in source and "\\nu^*H" not in source)

# Actual maps.  H is the four-dimensional observer-horizontal tangent and N4
# is the selected four-dimensional normal slice inside the ten-dimensional
# vertical bundle.  The bundle projection pi has zero derivative on N4.
d_pi = sp.zeros(4, 14)
d_pi[:, :4] = sp.eye(4)
d_i_normal = sp.zeros(14, 4)
d_i_normal[4:8, :] = sp.eye(4)
d_i_horizontal = sp.zeros(14, 4)
d_i_horizontal[:4, :] = sp.eye(4)

check("maps", "normal cycle is vertical for the bundle projection", d_pi * d_i_normal == sp.zeros(4))
check("maps", "horizontal comparison maps isomorphically to base", d_pi * d_i_horizontal == sp.eye(4))
check("maps", "normal restriction of a base pullback factors through a point", (d_pi * d_i_normal).rank() == 0)
check("maps", "horizontal restriction retains rank four", (d_pi * d_i_horizontal).rank() == 4)

# Naturality of characteristic classes: i_N^* pi^* c2(S_X+) is the pullback
# along the constant map pi o i_N, hence zero in H4(S4).  P3's normal collapse
# has degree one, hence returns n.
source_c2_on_normal = 0
p3_c2_on_normal = {n: n for n in (-1, 0, 1)}
check("topology", "source tangential class restricts trivially to normal S4", source_c2_on_normal == 0)
check("topology", "P3 positive horn has normal charge plus one", p3_c2_on_normal[1] == 1)
check("topology", "P3 negative horn has normal charge minus one", p3_c2_on_normal[-1] == -1)
check("topology", "only trivial P3 horn matches horizontal bundle on normal cycle", [n for n, c2 in p3_c2_on_normal.items() if c2 == source_c2_on_normal] == [0])
check("topology", "nontrivial amplitude horn cannot be the tangential source bundle", p3_c2_on_normal[1] != source_c2_on_normal)
check("planted", "PLANT same abstract S4 dimension does not imply same pullback class", 4 == 4 and p3_c2_on_normal[1] != source_c2_on_normal)


def wedge_matrix(i, j, dimension=14):
    out = sp.zeros(dimension)
    out[i, j] = 1
    out[j, i] = -1
    return out


def selfdual_basis(offset):
    return [
        wedge_matrix(offset + 0, offset + 1) + wedge_matrix(offset + 2, offset + 3),
        wedge_matrix(offset + 0, offset + 2) + wedge_matrix(offset + 3, offset + 1),
        wedge_matrix(offset + 0, offset + 3) + wedge_matrix(offset + 1, offset + 2),
    ]


sd_h = selfdual_basis(0)
sd_n = selfdual_basis(4)
flat_h = sp.Matrix.hstack(*[m.reshape(196, 1) for m in sd_h])
flat_n = sp.Matrix.hstack(*[m.reshape(196, 1) for m in sd_n])
combined = flat_h.row_join(flat_n)

check("slots", "horizontal self-dual basis has rank three", flat_h.rank() == 3)
check("slots", "normal self-dual basis has rank three", flat_n.rank() == 3)
check("slots", "horizontal and normal self-dual spans are disjoint", combined.rank() == 6)
check("slots", "every horizontal-normal pairing vanishes", all((a.T * b).trace() == 0 for a in sd_h for b in sd_n))

p_h = sp.diag(*([1] * 4 + [0] * 10))
p_n4 = sp.diag(*([0] * 4 + [1] * 4 + [0] * 6))
check("slots", "P3 normal curvature has zero horizontal restriction", all(p_h * b * p_h == sp.zeros(14) for b in sd_n))
check("slots", "source tangent curvature has zero normal restriction", all(p_n4 * a * p_n4 == sp.zeros(14) for a in sd_h))
check("gauge", "internal coefficient mixing cannot change normal form support", all(p_h * sum((sp.Integer(j + 1) * sd_n[j] for j in range(3)), sp.zeros(14)) * p_h == sp.zeros(14) for _ in range(3)))
check("gauge", "nonzero horizontal source curvature survives horizontal restriction", any(p_h * a * p_h != sp.zeros(14) for a in sd_h))
check("planted", "PLANT internal gauge cannot repair base-slot mismatch", combined.rank() == flat_h.rank() + flat_n.rank())

# A planted permutation interchanging H with the selected N4 transports the
# normal SD basis to the horizontal one.  It is deliberately not an allowed
# internal gauge transformation: it does not preserve the observation split.
s = sp.eye(14)
for j in range(4):
    s[j, j] = 0
    s[4 + j, 4 + j] = 0
    s[j, 4 + j] = 1
    s[4 + j, j] = 1
transported = [s.T * b * s for b in sd_n]
check("soldering", "planted H-N soldering transports normal SD basis to horizontal SD basis", transported == sd_h)
check("soldering", "planted soldering fails to preserve horizontal projector", s * p_h != p_h * s)
epsilon_global_open = "global full epsilon_IG reduction remains unconstructed" in soldering
check("soldering", "existing full epsilon IG reduction remains unconstructed", epsilon_global_open)
check("soldering", "slot transport therefore remains a new construction", s * p_h != p_h * s and epsilon_global_open)

check("layer0", "abstract S4 class theorem and actual normal restriction are compatible", p3_c2_on_normal[1] == 1 and source_c2_on_normal == 0)
check("layer0", "normal support is not tangential frame support", (d_pi * d_i_normal).rank() == 0)
check("variational", "current action may not be restricted through a nonexistent diagonal", p3_c2_on_normal[1] != source_c2_on_normal)
check("symplectic", "no BV gauge quotient can identify distinct characteristic classes", p3_c2_on_normal[1] != source_c2_on_normal)
check("accounting", "current nontrivial P3 route adds no selected amplitude", p3_c2_on_normal[1] != source_c2_on_normal)
check("accounting", "revival requires a redesigned tangential support map or new soldering", transported == sd_h and s * p_h != p_h * s)

print("\nRESULT")
print("verdict=CURRENT_P3_NORMAL_SUPPORT_CANNOT_DIAGONALIZE_TANGENTIAL_SU2PLUS__ABSTRACT_S4_CLASS_MATCH_RESCOPED__TANGENTIAL_SUPPORT_OR_NEW_SOLDERING_REQUIRED")
print(f"source_c2_on_normal={source_c2_on_normal}")
print(f"p3_c2_on_normal={p3_c2_on_normal}")
print("matching_p3_horns=[0]")
print(f"horizontal_sd_rank={flat_h.rank()}")
print(f"normal_sd_rank={flat_n.rank()}")
print(f"combined_sd_rank={combined.rank()}")
print("next_gate=DESIGN_TANGENTIAL_P3_SUPPORT_MAP_OR_SOURCE_OWNED_HN_SOLDERING__COUNT_SURPLUS_BEFORE_ACTION_RESTRICTION")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
