#!/usr/bin/env python3
"""K2202 exact matrix controls; no large elimination or port search."""
import sys
sys.dont_write_bytecode = True
from itertools import combinations
import sympy as S

def controls(fault=None):
    cs={}
    def ck(k,v): cs[k]=bool(v)
    I=S.eye(32); Z=S.zeros(32); gam=[]
    for sign in [1,-1]:
        for j in range(5):
            G=S.zeros(32)
            for mask in range(32):
                p=(-1)**((mask&((1<<j)-1)).bit_count())
                if not mask&(1<<j): G[mask|(1<<j),mask]=p
                else: G[mask^(1<<j),mask]=sign*p
            gam.append(G)
    gam[4]=S.I*gam[4]
    B=S.zeros(32)
    for mask in range(32):
        comp=31^mask; k=mask.bit_count()
        swaps=sum((comp&((1<<j)-1)).bit_count() for j in range(5) if mask&(1<<j))
        B[mask,comp]=(-1)**(k*(k-1)//2+swaps)
    if fault=='pairing_sign': B[0,31]=-B[0,31]
    ids=[[m for m in range(32) if m.bit_count()%2==p] for p in range(2)]
    ck('halves_16',list(map(len,ids))==[16,16])
    ck('B_symmetric',B==B.T)
    ck('B_nondegenerate',B*B.T==I)
    ck('B_opposite_chirality',all(B.extract(ix,ix)==S.zeros(16) for ix in ids))
    for j,G in enumerate(gam):
        ck('gamma_square_'+str(j),G*G==(1 if j<4 else -1)*I)
        ck('gamma_selfadjoint_'+str(j),G.T*B==B*G)
    for j,k in combinations(range(10),2):
        ck(f'gamma_anticommutator_{j}_{k}',gam[j]*gam[k]+gam[k]*gam[j]==Z)
    for degree in [3,7]:
        for inds in combinations(range(10),degree):
            X=I
            for j in inds: X=X*gam[j]
            ck('blade_skew_'+str(inds),X.T*B==(-1 if fault!='blade_sign' else 1)*B*X)
    IN=I; C=I
    for j,G in enumerate(gam):
        IN=IN*G
        if j!=4: C=C*G
    ci=-C
    ck('normal_volume_square',IN*IN==-I)
    ck('quaternionic_square',C*C.conjugate()==-I)
    ck('quaternionic_inverse',C*ci==I)
    ck('real_structure_fixes_all_gamma',all(C*G.conjugate()*ci==G for G in gam))
    ck('real_structure_fixes_volume',C*IN.conjugate()*ci==IN)
    ck('real_structure_exchanges_halves',all(C.extract(ix,ix)==S.zeros(16) for ix in ids))
    A=gam[0]*gam[1]*gam[2]
    BB=gam[0]*gam[3]*gam[4]
    CC=gam[0]*gam[1]*gam[5]
    w=A+BB; u=A+CC; v=IN*w; t=S.I*u
    P=7*v-15*t; bp=7*v+15*t; Y=P.inv()*bp
    ck('actual_port_both_commutators_nonzero',v*t-t*v!=Z and v*t+t*v!=Z)
    ck('actual_port_nonscalar_square',v*v!=(v*v).trace()*I/32)
    ck('actual_barP',C*P.conjugate()*ci==bp)
    ck('actual_norm_one',C*Y.conjugate()*ci*Y==I)
    for i,ix in enumerate(ids):
        Om=(B*P).extract(ix,ix); YY=Y.extract(ix,ix)
        ck(f'actual_omega_skew_{i}',Om.T==-Om)
        ck(f'actual_omega_invertible_{i}',Om.det()!=0)
        ck(f'actual_Y_selfadjoint_{i}',YY.T*Om==Om*YY)
        ck(f'actual_omegaY_is_barP_{i}',Om*YY==(B*bp).extract(ix,ix))
    # Abstract construction: explicitly NOT asserted to be a real3/7 port.
    j2=S.Matrix([[0,1],[-1,0]])
    Om=S.diag(*([j2]*8)); D=S.diag(*[k*S.eye(2) for k in range(2,10)])
    z=S.zeros(16); ii=S.eye(16)
    BA=z.row_join(ii).col_join(ii.row_join(z))
    CA=z.row_join(ii).col_join((-ii).row_join(z))
    PA=z.row_join(-Om*D).col_join(Om.row_join(z))
    bpa=CA*PA.conjugate()*(-CA); YA=PA.inv()*bpa
    ck('abstract_quaternionic_square',CA*CA==-I)
    ck('abstract_skew_P',(BA*PA).T==-BA*PA)
    ck('abstract_skew_barP',(BA*bpa).T==-BA*bpa)
    ck('abstract_Y_diagonal',YA==S.diag(D,D.inv()))
    ck('abstract_norm_one',CA*YA.conjugate()*(-CA)*YA==I)
    vals={}
    for val in YA.diagonal(): vals[val]=vals.get(val,0)+1
    ck('abstract_exactly_two_multiplicity',len(vals)==16 and set(vals.values())=={2})
    ck('abstract_not_fourfold',any(n%4!=0 for n in vals.values()))
    # Paired nonsemisimple positive control.
    JJ=S.Matrix([[2,1],[0,2]])
    O4=S.zeros(2).row_join(S.eye(2)).col_join((-S.eye(2)).row_join(S.zeros(2)))
    D4=S.diag(JJ,JJ.T)
    if fault=='jordan_pair': D4[3,2]=0
    ck('paired_Jordan_selfadjoint',D4.T*O4==O4*D4)
    ck('paired_Jordan_nonsemisimple',(D4-2*S.eye(4))!=S.zeros(4) and (D4-2*S.eye(4))**2==S.zeros(4))
    # Unique size2 block forbidden although characteristic polynomial is square.
    BAD=S.diag(JJ,2*S.eye(14)); N=BAD-2*S.eye(16)
    k0=0; k1=16-N.rank(); k2=16-(N*N).rank(); k3=16-(N*N*N).rank()
    ck('bad_total_even',BAD.trace()==32)
    ck('bad_size2_count_odd',2*k2-k1-k3==1)
    ck('bad_size1_count_even',2*k1-k0-k2==14)
    return cs

from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    cs=controls(); assert all(cs.values()),[k for k,v in cs.items() if not v]
    faults={}
    for f in ['pairing_sign','blade_sign','jordan_pair']:
        bad=[k for k,v in controls(f).items() if not v]
        assert bad,('undetected',f);faults[f]=bad
    deps=['explorations/conditional-build/k2202-ordered-clifford-adapter-consequences-2026-10-28.md','explorations/conditional-build/k2169-invertible-pencil-full-descent-2026-10-27.md','explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md']
    report=dict(result_id='K2202',status='conditional_exact_paired_Jordan_necessity',checks=cs,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal alternating primary-quotient proof, exact normal Fock and actual port controls, explicitly abstract non-fourfold and Jordan controls. No actual-port exhaustion or physical quotient.')
    dst=ROOT/'lab/process/k2202-ordered-clifford-adapter-consequences.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2202',controls=len(cs),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
