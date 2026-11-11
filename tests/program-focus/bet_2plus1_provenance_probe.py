#!/usr/bin/env python3
"""Exact provenance augmentation and unchanged K2236 evolution controls."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2236_raw_observation_closure_probe as old
REPORT=ROOT/'lab/process/bet-2plus1-provenance-observation.json'

def build():
    checks=[];controls=[]
    def ck(name,value,negative=False):
        assert bool(value),name
        (controls if negative else checks).append(name)
    X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]]);I=s.eye(2)
    ck('real_Cl21_controls',X*X==Z*Z==I and J*J==-I and X*Z+Z*X==s.zeros(2) and X*J+J*X==s.zeros(2) and Z*J+J*Z==s.zeros(2))
    P=s.eye(6)[:2,:];GH=X;GN=Z.row_join(J);G=GH.row_join(GN)
    jH=X;jN=(Z/2).col_join(-J/2);jY=(X/3).col_join(Z/3).col_join(-J/3)
    R=s.Matrix.hstack(*G.nullspace());K=s.eye(6)[:,2:];KR=K*s.Matrix.hstack(*GN.nullspace())
    ck('compatible_insertions',GH*jH==I and GN*jN==I and G*jY==I and P*jY==jH/3)
    ck('owned_surjectivity_reused',(P*R).rank()==P.rows)
    def overlap(L):
        Q=P.col_join(L);T=Q*jY;U=Q*R
        return T.rank()+U.rank()-T.row_join(U).rank()
    Ln=s.zeros(2,2).row_join(GN);F=P.col_join(G)
    ck('trace_augmented_surjective',F.rank()==4)
    ck('trace_augmented_hidden_kernel',F*KR==s.zeros(4,2) and len(F.nullspace())==2)
    ck('minimum_normal_trace_separates',overlap(Ln)==0)
    ck('minimum_total_trace_separates',overlap(G)==0)
    M=s.Matrix([[2,3],[-1,4]]);A=s.Matrix([[1,2],[3,5]])
    L=M.row_join(A*GN);Q=P.col_join(L)
    shear=s.eye(2).row_join(s.zeros(2)).col_join((GH-A.inv()*M).row_join(A.inv()))
    ck('all_minimum_shear_fixture',shear*Q==F and overlap(L)==0)
    noise=s.Matrix([[0,0,1,0,0,0]])
    ck('extra_hidden_information_cost', (noise*KR).rank()==1 and overlap(Ln.col_join(noise))==0)
    bad=Ln.copy();bad[0,:]+=noise
    ck('minimal_width_hidden_noise_breaks_separation',overlap(bad)>0,True)
    ck('too_few_extra_channels_fail',overlap(Ln[:1,:])>0,True)
    ck('literal_observation_overlap',overlap(s.zeros(0,6))==2,True)
    QH=I-jH*GH
    ck('trace_subtraction_loses_trace',QH*P*jY==s.zeros(2),True)
    # Original scalar raw matrices, not a copied quotient formula.
    OBS=[0,7,8,9];UN=[a for a in range(14) if a not in OBS]
    def m(k):return s.Matrix([[s.Rational(old.o.scalar_m(k,a,c)) for c in range(15)] for a in range(15)])
    M0=m(0);MI=M0.inv();E=s.zeros(15,6);R0=s.zeros(6,15)
    for r,a in enumerate(OBS):E[a,r]=1;R0[r,a]=1
    for a in UN:E[a,4]=1;R0[4,a]=s.Rational(1,10)
    E[14,5]=R0[5,14]=1
    ck('old_quotient_RE',R0*E==s.eye(6))
    pull=s.eye(15).extract(OBS+[14],range(15));gamma=s.Matrix([[int(a<14) for a in range(15)]])
    augmented=pull.col_join(gamma)
    ck('same_old_dynamic_kernel',augmented.rank()==R0.rank()==6 and augmented.col_join(R0).rank()==6)
    t=s.Matrix([1,1,1,1,1,0])/14;r=s.Matrix([1,0,0,0,-s.Rational(1,10),0]);nu=s.Matrix([0,0,0,0,0,1]);g=s.Matrix([[1,1,1,1,10,0]])
    ck('trace_and_remainder_input_typing',(g*t)[0]==1 and (g*r)[0]==0)
    outputs={}
    for j,k in enumerate(OBS[1:],1):
        evolution=MI*m(k);T=R0*evolution*E
        ck(f'actual_raw_quotient_{j}',evolution*E==E*T)
        expected=s.zeros(6,1);expected[0]=s.Rational(1,14);expected[j]=s.Rational(12,14);expected[5]=s.Rational(12,14)
        ck(f'trace_mixing_{j}',T*t==expected and (T*t)[5]!=0)
        er=s.Matrix([0,s.Rational(1,12),s.Rational(1,12),s.Rational(1,12),-s.Rational(1,60),-1])
        ck(f'remainder_mixing_{j}',T*r==er and (g*T*r)[0]==s.Rational(1,12))
        ck(f'scalar_mixing_{j}',(T*nu)[:5]!=[0]*5)
        N=T*T-s.eye(6)
        ck(f'owned_Jordan_control_{j}',N.rank()==1 and N*N==s.zeros(6))
        # Genuine coefficient faults on the matrix actually used by each consumer.
        wrong=T.copy();wrong[5,4]+=1
        ck(f'fault_raw_trace_return_{j}',wrong*t!=expected,True)
        wrong2=T.copy();wrong2[1,0]+=1
        ck(f'fault_remainder_gamma_{j}',(g*wrong2*r)[0]!=s.Rational(1,12),True)
        outputs[str(j)]={'trace':[str(v) for v in T*t],'remainder':[str(v) for v in T*r],'scalar':[str(v) for v in T*nu],'remainder_output_trace':str((g*T*r)[0])}
    deps=['tests/channel-swings/k2236_raw_observation_closure_probe.py','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2236-raw-observation-closure-2026-10-29.md','explorations/conditional-build/k2239-moving-observation-closure-2026-10-29.md']
    return dict(artifact='BET_2PLUS1_PROVENANCE_OBSERVATION',program_target='BET-2PLUS1',tier='T1',status='conditional_internal_result',checks=checks,contrary_controls=controls,raw_outputs=outputs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),new_effect='All minimum linear provenance-separating augmentations classified; actual held raw evolution mixes the separated labels.',reused='VZ4 full image; Aug31 trace projector; K2236 rank768 closure/Jordan/Green and K2239 moving graph results.',ceiling='No guessed action, source-selected augmented observation, physical family count, class-C or matrix verdict. Linear pointwise fixed-split provenance only.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=build()
    if args.write:REPORT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==d,'report or dependency changed'
    print(f"PASS {len(d['checks'])} supporting checks; {len(d['contrary_controls'])} contrary controls")
