#!/usr/bin/env python3
"""Data-mutation probe for K1386."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1386-covariant-charge-commutator-filtration.json").read_text())
def validate(x):
 f,q=x["covariant_filtration"],x["decision"];e=[]
 if "[D_mu,D_nu]=i F_mu_nu Q" not in f["operators"]:e.append("operators")
 if "2i F_a^mu Q D_mu u" not in f["basic_wave_commutator"]:e.append("basic")
 if "|beta|+|gamma|<=|alpha|" not in f["iterated_form"]:e.append("iterated")
 if "|alpha|+n+1" not in f["combined_order"]:e.append("order")
 if "triangular rather than rectangular" not in f["mechanism"]:e.append("mechanism")
 if not q["basic_commutator_derived"]:e.append("basic decision")
 if not q["combined_order_preserved"]:e.append("filtration decision")
 if q["rectangular_top_corner_required"]:e.append("corner overclaim")
 if q["null_form_constructed"]:e.append("null-form overclaim")
 if q["global_bound_proved"]:e.append("global overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("operators",lambda x:x["covariant_filtration"].__setitem__("operators","commuting derivatives")),("basic",lambda x:x["covariant_filtration"].__setitem__("basic_wave_commutator","zero")),("iterated",lambda x:x["covariant_filtration"].__setitem__("iterated_form","unknown")),("order",lambda x:x["covariant_filtration"].__setitem__("combined_order","unbounded")),("mechanism",lambda x:x["covariant_filtration"].__setitem__("mechanism","rectangular")),("basic decision",lambda x:x["decision"].__setitem__("basic_commutator_derived",False)),("filtration decision",lambda x:x["decision"].__setitem__("combined_order_preserved",False)),("corner overclaim",lambda x:x["decision"].__setitem__("rectangular_top_corner_required",True)),("null-form overclaim",lambda x:x["decision"].__setitem__("null_form_constructed",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_bound_proved",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
