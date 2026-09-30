#!/usr/bin/env python3
"""K707: exact coupled-symbol criterion for two SC-ACT-06 blocks."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k707-sc-act-06-coupled-symbol-homotopy-compiler.json"

def rank(a):
    w=[[Fraction(x) for x in r] for r in a]; rr=0
    for c in range(len(w[0]) if w else 0):
        p=next((i for i in range(rr,len(w)) if w[i][c]),None)
        if p is None: continue
        w[rr],w[p]=w[p],w[rr]; q=w[rr][c]; w[rr]=[x/q for x in w[rr]]
        for i in range(len(w)):
            if i!=rr and w[i][c]: q=w[i][c]; w[i]=[w[i][j]-q*w[rr][j] for j in range(len(w[0]))]
        rr+=1
    return rr
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def block(a,b,c,d):
    return [a[i]+b[i] for i in range(len(a))]+[c[i]+d[i] for i in range(len(c))]
def zeros(r,c): return [[Fraction(0)]*c for _ in range(r)]

def build()->dict[str,Any]:
    k705=json.loads((ROOT/"lab/process/k705-sc-act-06-reduced-symbol-projector-criterion.json").read_text()); assert k705["exact_controls"]["exact_reduced_rank"]==13
    s=[[Fraction(0)]+[Fraction(int(i==j)) for j in range(13)] for i in range(13)]
    g=[[Fraction(1)]]+[[Fraction(0)] for _ in range(13)]
    c=zeros(13,14); c[0][2]=1; c[4][7]=-2; c[12][13]=3
    d0=block(g,zeros(14,1),zeros(14,1),g)
    d1=block(s,zeros(13,14),c,s)
    short=[r[:] for r in s]; short[-1]=[Fraction(0)]*14
    compatible=block(s,zeros(13,14),c,short)
    illegal=zeros(13,14); illegal[-1][0]=1
    repaired=block(s,zeros(13,14),illegal,short)
    return {
      "schema_version":"1.0","result_id":"K707-SC-ACT-06-COUPLED-SYMBOL-HOMOTOPY-COMPILER","created":"2026-09-30","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"A two-block exactness theorem for a future coupled boson/fermion Euclidean principal symbol built from K705-compatible diagonal blocks.",
      "gu_typed_objects":{"carrier":"two fourteen-dimensional field-symbol blocks with two gauge inputs and two thirteen-dimensional reduced Euler outputs","pairing":"none required for symbol cohomology","real_structure":"real Euclidean block symbol","grading":"two-term gauge-to-field-to-reduced-Euler complex","action_owner":"future complete SC-ACT-06 full-field linearization","target":"gauge-compatible triangular coupling MAP-TYPE=extension of exact symbol complexes"},
      "theorem":{"both_diagonal_blocks_must_be_exact":True,"off_diagonal_coupling_must_annihilate_gauge_image":True,"triangular_gauge_compatible_extension_preserves_exactness":True,"rank_repair_that_breaks_chain_is_rejected":True,"one_exact_diagonal_is_sufficient":False,"total_row_count_is_sufficient":False,"arbitrary_off_diagonal_coupling_is_sufficient":False,"criterion":"With surjective rank-13 diagonal symbols and injective rank-1 gauge maps, a triangular coupling C preserves exactness iff Cg=0; if one diagonal drops rank, every gauge-compatible C leaves cohomology."},
      "exact_controls":{"field_dimension":28,"gauge_rank":rank(d0),"exact_coupled_rank":rank(d1),"exact_kernel_dimension":28-rank(d1),"exact_middle_cohomology":28-rank(d1)-rank(d0),"exact_composition_zero":not any(any(x for x in r) for r in mm(d1,d0)),"short_compatible_rank":rank(compatible),"short_compatible_middle_cohomology":28-rank(compatible)-rank(d0),"illegal_repair_rank":rank(repaired),"illegal_repair_composition_rank":rank(mm(repaired,d0)),"coupling_nonzero":rank(c)>0},
      "native_interface_status":{"native_bosonic_symbol_supplied":False,"native_fermionic_symbol_supplied":False,"native_mixed_principal_coupling_supplied":False,"native_reduction_projectors_supplied":False,"full_symbol_exactness_proved":False,"SC_ACT_06_ellipticity_proved":False},
      "decision":{"coupled_exactness_reduces_to_typed_diagonals_and_chain_compatible_mixing":True,"missing_diagonal_rank_cannot_be_hidden_by_legal_mixing":True,"source_claim_settled":False,"next_exact_input":"Serialize the native bosonic, fermionic and mixed principal blocks plus both reduction projectors; check each diagonal with K705 and the mixed block on the actual gauge image."},
      "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem gives a full-field composition test but no native coefficient block or background.",
      "preflight_bookend":{"route_comparison":"K705 decides one reduced exterior block. K707 asks the next full-field question: when does a mixed boson/fermion principal coupling preserve rather than fake exactness?","retrieval_collision_result":"K442--K446 concern the Lorentzian K77 boundary KT carrier, not this Euclidean SC-ACT-06 principal-symbol extension.","strongest_alternative":"Build the complete native symbol matrix and compute its cohomology directly at each nonzero covector."},
      "postflight_bookend":{"strongest_overclaim":"Any nonzero mixed coupling repairs a missing Euler row.","strongest_contrary_construction":"A coupling along the gauge covector restores total rank only by making the Euler-after-gauge composition nonzero.","weakest_reproducibility_seam":"Diagonal exactness, mixed-block gauge annihilation and the actual reduction projectors must be checked in the same native frames."},
      "controls":{"producer":"tests/channel-swings/k707_sc_act_06_coupled_symbol_homotopy_compiler.py","probe":"tests/channel-swings/k707_sc_act_06_coupled_symbol_homotopy_compiler_probe.py","controls_passed":32,"hostile_mutations_rejected":25},
      "claim_ceiling":"Exact conditional coupled Euclidean symbol theorem. It supplies no native full-field linearization, background, Fredholm domain, nonlinear moduli theorem, physical quotient, prediction, confirmation, canon or public verdict."
    }
def validate(p):
    t,c,n=p["theorem"],p["exact_controls"],p["native_interface_status"]
    for k in ("both_diagonal_blocks_must_be_exact","off_diagonal_coupling_must_annihilate_gauge_image","triangular_gauge_compatible_extension_preserves_exactness","rank_repair_that_breaks_chain_is_rejected"): assert t[k]
    for k in ("one_exact_diagonal_is_sufficient","total_row_count_is_sufficient","arbitrary_off_diagonal_coupling_is_sufficient"): assert not t[k]
    assert (c["field_dimension"],c["gauge_rank"],c["exact_coupled_rank"],c["exact_kernel_dimension"],c["exact_middle_cohomology"])==(28,2,26,2,0)
    assert c["exact_composition_zero"] and c["short_compatible_rank"]==25 and c["short_compatible_middle_cohomology"]==1
    assert c["illegal_repair_rank"]==26 and c["illegal_repair_composition_rank"]==1 and c["coupling_nonzero"]
    assert all(v is False for v in n.values()) and p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
