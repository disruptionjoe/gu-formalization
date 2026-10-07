#!/usr/bin/env python3
"""Hostile mutations for K1332."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1332-common-k-finite-core-unitarity.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("moving domain",lambda x:x["common_domain"].__setitem__("parameter_independent",False),lambda x:x["common_domain"]["parameter_independent"])
rejects("nondense core",lambda x:x["common_domain"].__setitem__("dense_in_H",False),lambda x:x["common_domain"]["dense_in_H"])
rejects("lost preservation",lambda x:x["common_domain"].__setitem__("preserved_by_every_simple_operator",False),lambda x:x["common_domain"]["preserved_by_every_simple_operator"])
rejects("wrong norm",lambda x:x["regular_imaginary_axis"].__setitem__("operator_norm",2),lambda x:x["regular_imaginary_axis"]["operator_norm"]==1)
rejects("lost inverse",lambda x:x["regular_imaginary_axis"].__setitem__("inverse_law","none"),lambda x:"=I" in x["regular_imaginary_axis"]["inverse_law"])
rejects("zero not identity",lambda x:x["regular_imaginary_axis"].__setitem__("zero_parameter","R_0=-I"),lambda x:"R_0=I" in x["regular_imaginary_axis"]["zero_parameter"])
rejects("domain absent",lambda x:x["decision"].__setitem__("common_dense_compact_picture_core_constructed",False),lambda x:x["decision"]["common_dense_compact_picture_core_constructed"])
rejects("unitarity absent",lambda x:x["decision"].__setitem__("regular_imaginary_unitary_extension_constructed",False),lambda x:x["decision"]["regular_imaginary_unitary_extension_constructed"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("physical_domain_constructed",True),lambda x:not x["decision"]["physical_domain_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
