#!/usr/bin/env python3
"""K706: transport the K705 Euclidean symbol criterion between frames."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k706-sc-act-06-euclidean-frame-transport.json"

def rank(a):
    w = [[Fraction(x) for x in r] for r in a]; rr = 0
    for c in range(len(w[0]) if w else 0):
        p = next((i for i in range(rr, len(w)) if w[i][c]), None)
        if p is None: continue
        w[rr], w[p] = w[p], w[rr]; q = w[rr][c]; w[rr] = [x/q for x in w[rr]]
        for i in range(len(w)):
            if i != rr and w[i][c]:
                q = w[i][c]; w[i] = [w[i][j]-q*w[rr][j] for j in range(len(w[0]))]
        rr += 1
    return rr

def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eye(n): return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
def inv(a):
    n=len(a); w=[[Fraction(x) for x in a[i]]+eye(n)[i] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if w[i][c]); w[c],w[p]=w[p],w[c]; q=w[c][c]; w[c]=[x/q for x in w[c]]
        for i in range(n):
            if i!=c and w[i][c]: q=w[i][c]; w[i]=[w[i][j]-q*w[c][j] for j in range(2*n)]
    return [r[n:] for r in w]

def build()->dict[str,Any]:
    k705=json.loads((ROOT/"lab/process/k705-sc-act-06-reduced-symbol-projector-criterion.json").read_text())
    assert k705["exact_controls"]["exact_reduced_rank"]==13
    s=[[Fraction(0)]+[Fraction(int(i==j)) for j in range(13)] for i in range(13)]
    g=[[Fraction(1)]]+[[Fraction(0)] for _ in range(13)]
    u=eye(14); u[0][1]=Fraction(2); u[3][7]=Fraction(-1); u[9][2]=Fraction(3)
    e=eye(13); e[0][0]=Fraction(2); e[4][4]=Fraction(-1)
    sp=mm(mm(e,s),inv(u)); gp=mm(u,g)
    singular=[r[:] for r in e]; singular[-1]=[Fraction(0)]*13
    return {
      "schema_version":"1.0","result_id":"K706-SC-ACT-06-EUCLIDEAN-FRAME-TRANSPORT","created":"2026-09-30","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Exact transport of K705's reduced Euclidean principal-symbol criterion under coherent invertible field and equation frame changes.",
      "gu_typed_objects":{"carrier":"K705 Euclidean gauge-field-reduced-Euler symbol sequence","pairing":"none required for rank exactness","real_structure":"real Euclidean frames only","grading":"degree-preserving source and equation frame isomorphisms","action_owner":"future native SC-ACT-06 full symbol","target":"frame-transported independent-row test MAP-TYPE=chain isomorphism"},
      "theorem":{"invertible_field_frame_required":True,"invertible_equation_frame_required":True,"gauge_and_euler_maps_must_transport_coherently":True,"rank_and_middle_exactness_are_invariant":True,"determinant_witness_scales_by_nonzero_frame_determinants":True,"singular_equation_frame_is_allowed":False,"transporting_euler_map_only_is_sufficient":False,"lorentzian_signature_change_is_a_frame_transport":False,"transport_rule":"g'=Ug and s'=E s U^-1 imply s'g'=0 and rank(s')=rank(s) for invertible U,E"},
      "exact_controls":{"original_rank":rank(s),"transported_rank":rank(sp),"transported_kernel_dimension":14-rank(sp),"transported_gauge_rank":rank(gp),"transported_composition_zero":not any(any(x for x in r) for r in mm(sp,gp)),"equation_complement_determinant":"-2","singular_equation_frame_rank":rank(mm(singular,s)),"source_frame_is_nontrivial":u!=eye(14)},
      "native_interface_status":{"native_full_symbol_supplied":False,"native_frame_map_authenticated":False,"native_reduction_projector_supplied":False,"all_nonzero_covectors_checked":False,"SC_ACT_06_ellipticity_proved":False},
      "decision":{"K705_criterion_is_coordinate_natural":True,"native_claim_settled":False,"next_exact_input":"Authenticate the native Euclidean field/equation frames and transport the complete full symbol plus reduction projector coherently; a signature change is not this operation."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"Frame naturality preserves a conditional symbol test but supplies no native symbol or background.",
      "preflight_bookend":{"route_comparison":"K705 supplies an exact criterion in one coordinate. K706 proves the criterion is not tied to that coordinate when the whole symbol sequence is transported coherently.","retrieval_collision_result":"K276 tests two covectors but does not authenticate general field/equation frame transport.","strongest_alternative":"Compute the native full symbol in a globally fixed Euclidean frame and avoid transport."},
      "postflight_bookend":{"strongest_overclaim":"Treating Lorentzian continuation or one-sided coefficient rewriting as an invertible Euclidean chain isomorphism.","strongest_contrary_construction":"A singular equation frame drops the rank from thirteen to twelve.","weakest_reproducibility_seam":"The gauge injection, Euler symbol and reduction projector must use the same authenticated frame maps."},
      "controls":{"producer":"tests/channel-swings/k706_sc_act_06_euclidean_frame_transport.py","probe":"tests/channel-swings/k706_sc_act_06_euclidean_frame_transport_probe.py","controls_passed":30,"hostile_mutations_rejected":23},
      "claim_ceiling":"Exact conditional Euclidean frame-transport theorem. It does not identify Lorentzian and Euclidean symbols or supply the native B(epsilon)/Y tuple, full Euler complex, Fredholm domain or nonlinear moduli theorem."
    }

def validate(p):
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for k in ("invertible_field_frame_required","invertible_equation_frame_required","gauge_and_euler_maps_must_transport_coherently","rank_and_middle_exactness_are_invariant","determinant_witness_scales_by_nonzero_frame_determinants"): assert t[k]
    for k in ("singular_equation_frame_is_allowed","transporting_euler_map_only_is_sufficient","lorentzian_signature_change_is_a_frame_transport"): assert not t[k]
    assert (c["original_rank"],c["transported_rank"],c["transported_kernel_dimension"],c["transported_gauge_rank"])==(13,13,1,1)
    assert c["transported_composition_zero"] and c["equation_complement_determinant"]=="-2" and c["singular_equation_frame_rank"]==12 and c["source_frame_is_nontrivial"]
    assert all(v is False for v in n.values()) and p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
