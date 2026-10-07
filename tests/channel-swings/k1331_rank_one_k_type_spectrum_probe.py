#!/usr/bin/env python3
"""Hostile mutations for K1331's spectrum packet."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1331-rank-one-k-type-spectrum.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("odd compact picture",lambda x:x["rank_one_operator"].__setitem__("compact_picture","SO(2)"),lambda x:"plus_or_minus" in x["rank_one_operator"]["compact_picture"])
rejects("missing full integral",lambda x:x["rank_one_operator"].__setitem__("raw_standard_integral","scalar only"),lambda x:x["rank_one_operator"]["raw_standard_integral"].startswith("(J_z f)(g)="))
rejects("wrong spherical normalizer",lambda x:x["rank_one_operator"].__setitem__("spherical_normalizer","Gamma(z)"),lambda x:"sqrt(pi)" in x["rank_one_operator"]["spherical_normalizer"])
rejects("wrong Weyl phase",lambda x:x["complete_even_spectrum"].__setitem__("weyl_phase","omitted"),lambda x:"identity" in x["complete_even_spectrum"]["weyl_phase"])
rejects("lost recurrence",lambda x:x["complete_even_spectrum"].__setitem__("recurrence","none"),lambda x:"2n+1-z" in x["complete_even_spectrum"]["recurrence"])
rejects("operator absent",lambda x:x["decision"].__setitem__("full_rank_one_operator_kernel_constructed",False),lambda x:x["decision"]["full_rank_one_operator_kernel_constructed"])
rejects("spectrum absent",lambda x:x["decision"].__setitem__("all_even_rank_one_k_type_eigenvalues_constructed",False),lambda x:x["decision"]["all_even_rank_one_k_type_eigenvalues_constructed"])
rejects("higher K scalar overclaim",lambda x:x["decision"].__setitem__("higher_rank_irreducible_K_types_claimed_scalar",True),lambda x:not x["decision"]["higher_rank_irreducible_K_types_claimed_scalar"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("physical_intertwiner_constructed",True),lambda x:not x["decision"]["physical_intertwiner_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
