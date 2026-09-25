#!/usr/bin/env python3
"""K500 reduce K494's cyclic/noncyclic cross to normal-action leakage."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k500-k162-noncyclic-leakage-reduction.json"
class CertificateError(ValueError):pass
def q(x:Any)->Fraction:
 try:return x if isinstance(x,Fraction) else Fraction(x)
 except Exception as exc:raise CertificateError("invalid rational") from exc
def qstr(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def cross_block(matrix,v_indices,n_indices):return [[matrix[i][j] for j in n_indices] for i in v_indices]
def max_abs_diagonal(block):
 if any(len(row)!=len(block) for row in block):raise CertificateError("square block required")
 if any(block[i][j] != (block[i][i] if i==j else 0) for i in range(len(block)) for j in range(len(block))):raise CertificateError("diagonal control block required")
 return max((abs(block[i][i]) for i in range(len(block))),default=Fraction())
def control()->dict[str,Any]:
 # Bath levels are (0,2) and (1,3); V takes the first vector in each level.
 scalar=[[Fraction(-256 if i==j else 0) for j in range(4)] for i in range(4)]
 shape=[[Fraction(x if i==j else 0) for j in range(4)] for i,x in enumerate((-2,1,-2,1))]
 normal=[[Fraction() for _ in range(4)] for _ in range(4)]
 for i,j,a,b,c in [(0,2,5,2,7),(1,3,11,3,13)]:normal[i][i]=a;normal[i][j]=normal[j][i]=b;normal[j][j]=c
 v=[0,1];n=[2,3]
 s=cross_block(scalar,v,n);h=cross_block(shape,v,n);w=cross_block(normal,v,n)
 total=[[s[i][j]+h[i][j]+w[i][j] for j in range(2)] for i in range(2)]
 return {"scalar_cross":[[qstr(x) for x in row] for row in s],"shape_cross":[[qstr(x) for x in row] for row in h],"normal_cross":[[qstr(x) for x in row] for row in w],"combined_cross":[[qstr(x) for x in row] for row in total],"combined_cross_norm":qstr(max_abs_diagonal(total)),"bath_number_blocks_preserved":True,"scalar_and_shape_cross_zero":all(x==0 for row in s+h for x in row)}
def build()->dict[str,Any]:
 c=control()
 return {"schema_version":"1.0","result_id":"K500-K162-NONCYCLIC-LEAKAGE-REDUCTION","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","gu_comparator_routing":"GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
 "scope":"K494's cross between the K139 Neumann cyclic closure and its M-orthogonal noncyclic remainder inside one K162 charge sector.",
 "gu_typed_objects":{"result":"noncyclic leakage reduction MAP-TYPE=orthogonal-block-reduction","carrier":"one complete K162 charge sector split into cyclic C and N=C^perp_M","pairing":"M=S* S transported isometrically to the regular-coordinate Hilbert space","form":"fixed K139/K156 base plus K168 shape","real_structure":"CAR adjoint on q00 or q10","grading":"bath-particle number and fixed charge","action_owner":"repository-supplied conditional operator; no source/GU action selection","target":"K494 cyclic/noncyclic same-form cross norm"},
 "theorem":{"isometry":"S maps the M-Hilbert coordinate completion isometrically onto the regular-coordinate Hilbert carrier","physical_cyclic_space":"V=closure span{v_n=G^n phi}","physical_noncyclic_space":"S(N)=V^perp","scalar_cross":"the -256 identity block has P_V I (1-P_V)=0","shape_cross":"K491's Lambda v_n=lambda_n v_n and self-adjoint Lambda make V reducing, hence P_V Lambda (1-P_V)=0","normal_cross":"the complete cyclic/noncyclic cross is P_V W (1-P_V), restricted from V to the image of C0","bath_number_reduction":"because W preserves bath number and v_n lies in level n, P_V W (1-P_V) is the orthogonal direct sum of levelwise leakage blocks","norm":"the full-V leakage norm is sup_n ||P_span(v_n) W_n (1-P_span(v_n))|| and upper-bounds K494's C0/N cross","commutator":"for self-adjoint W, ||P_V W (1-P_V)||=||[P_V,W]||","noncyclic_floor":"the compression (1-P_V)R(1-P_V) still needs its own lower floor"},
 "exact_control":c,
 "native_consequence":{"scalar_cross_eliminated":True,"K168_shape_cross_eliminated":True,"normal_action_leakage_only":True,"native_normal_leakage_evaluated":False,"native_noncyclic_floor_evaluated":False,"K473_released":False,"next_exact_input":"Evaluate or bound the bath-level normal-action leakage and the noncyclic compressed-form floor; combine them with K498/K499's cyclic floor through K494/K473."},
 "source_and_ledger_effect":"none","claim_ceiling":"Exact block reduction only. It removes the scalar and K168 shape from the K494 cyclic/noncyclic cross but supplies neither the normal-action leakage nor the noncyclic floor, so no complete K473 floor, K152 interval, source, ledger, canon, paper, public or physical conclusion follows."}
def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())
