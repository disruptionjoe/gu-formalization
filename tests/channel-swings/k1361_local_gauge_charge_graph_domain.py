#!/usr/bin/env python3
"""Graph-domain and local gauge controls for K1361."""
import cmath, hashlib, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1361-local-gauge-charge-graph-domain.json").read_text());n=0
def check(label,value):
 global n;assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
G,L,Q=D["graph_domain"],D["local_gauge_theorem"],D["decision"]
check("completed domain typed","H1(Sigma;H_ps)" in G["completed_domain"] and "Q phi" in G["completed_domain"])
check("graph norm typed","||Q phi||" in G["graph_norm"])
check("dense core typed","H_Kfin" in G["density"])
check("gauge action typed","exp(i alpha(x) Q)" in L["action"])
check("charge commutation typed","Q G_alpha" in L["charge_commutation"])
check("weak derivative typed","partial_j alpha" in L["weak_derivative"])
alpha=.37; dalpha=-.21; phi=1.2-.4j; dphi=-.7+.3j
for q in (-8,-4,-2,0,2,4,8):
 phase=cmath.exp(1j*alpha*q)
 lhs=phase*(dphi+1j*dalpha*q*phi)
 rhs=phase*dphi+1j*dalpha*q*phase*phi
 check(f"derivative identity q={q}",abs(lhs-rhs)<1e-12)
check("inverse stated","G_minus_alpha" in L["inverse"])
for N in (1,4,16,64):
 ordinary=sum(1/(k*k) for k in range(1,N+1))
 charge=sum((4*k)**2/(k*k) for k in range(1,N+1))
 check(f"ordinary bounded N={N}",ordinary<math.pi**2/6+1e-12)
 check(f"charge exact N={N}",charge==16*N)
check("ordinary H1 failure stated","not D(Q)" in L["ordinary_H1_failure"])
check("domain decision",Q["minimal_completed_first_order_graph_domain_constructed"] and Q["local_circle_gauge_action_preserves_graph_domain"])
check("ordinary H1 rejected",not Q["ordinary_H1_preserved_for_all_H_ps_fields"])
check("source ceiling",not Q["source_selects_domain"] and not Q["coupled_global_BV_domain_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==29;print("RESULT: PASS 29/29")
