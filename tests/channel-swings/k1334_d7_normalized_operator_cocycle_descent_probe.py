#!/usr/bin/env python3
"""Hostile mutations for K1334."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1334-d7-normalized-operator-cocycle-descent.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("projective cocycle",lambda x:x["normalized_family"].__setitem__("cocycle","up to scalar"),lambda x:"w1 w2" in x["normalized_family"]["cocycle"])
rejects("lost inverse",lambda x:x["normalized_family"].__setitem__("inverse","phase"),lambda x:x["normalized_family"]["inverse"].endswith("=I"))
rejects("word dependence",lambda x:x["normalized_family"].__setitem__("reduced_word_independence",False),lambda x:x["normalized_family"]["reduced_word_independence"])
rejects("wrong chamber count",lambda x:x["d7_descent"].__setitem__("weyl_chambers",42),lambda x:x["d7_descent"]["weyl_chambers"]==322560)
rejects("actions differ",lambda x:x["d7_descent"].__setitem__("transported_chamber_actions_coincide",False),lambda x:x["d7_descent"]["transported_chamber_actions_coincide"])
rejects("projection fails",lambda x:x["d7_descent"].__setitem__("average_projection_commutes_with_block_G_action",False),lambda x:x["d7_descent"]["average_projection_commutes_with_block_G_action"])
rejects("one-dimensional overclaim",lambda x:x["d7_descent"].__setitem__("descended_representation","one-dimensional"),lambda x:"not a one-dimensional" in x["d7_descent"]["descended_representation"])
rejects("descent absent",lambda x:x["decision"].__setitem__("G_equivariant_chamber_descent_constructed",False),lambda x:x["decision"]["G_equivariant_chamber_descent_constructed"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("physical_GU_state_space_constructed",True),lambda x:not x["decision"]["physical_GU_state_space_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
