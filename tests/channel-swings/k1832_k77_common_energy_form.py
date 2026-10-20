#!/usr/bin/env sage-python
"""Exact common positive symmetrizer of the conditional corrected K77 symbols."""
import argparse,hashlib,json
from pathlib import Path
from collections import Counter
from sage.all import QQ,matrix,identity_matrix
from k1824_k77_joint_observed_symbol_algebra import build_family,intertwiner_basis,entries
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1832-k77-common-energy-form.json'
def ldlt_pivots(H):
    A=matrix(QQ,H);out=[]
    for k in range(A.nrows()):
        d=A[k,k];out.append(d)
        assert d>0,'nonpositive LDL pivot'
        for i in range(k+1,A.nrows()):
            for j in range(k+1,A.nrows()):A[i,j]-=A[i,k]*A[k,j]/d
    return out

def produce():
    P,family,oldchecks,_=build_family();checks={};n=P.nrows()
    def ck(k,v):checks[k]=bool(v);assert v,k
    adj=[set() for _ in range(n)]
    for M in [P]+family:
        for i,j in M.dict():adj[i].add(j);adj[j].add(i)
    seen=set();components=[]
    for start in range(n):
        if start in seen:continue
        todo=[start];c=set()
        while todo:
            x=todo.pop()
            if x in c:continue
            c.add(x);todo.extend(adj[x]-c)
        seen.update(c);components.append(sorted(c))
    ck('32_support_components',len(components)==32 and all(len(c)==20 for c in components))
    types=[];blocks=[];kinds=[]
    for c in components:
        pb=P.matrix_from_rows_and_columns(c,c);B=pb.matrix_from_columns(pb.pivots());rr=B.transpose().pivots();L=B.matrix_from_rows(rr).inverse()
        ambient=[M.matrix_from_rows_and_columns(c,c) for M in family];a=[L*M.matrix_from_rows(rr)*B for M in ambient]
        ck('corrected_basis_'+str(len(kinds)),B.ncols()==16 and all(M*B==B*A for M,A in zip(ambient,a)))
        if a not in types:types.append(a)
        kinds.append(types.index(a))
    ck('four_types',Counter(kinds)==Counter({0:8,1:8,2:8,3:8}))
    for i,a in enumerate(types):
        forms=intertwiner_basis(a,[M.transpose() for M in a]);ck('form_space_dim2_'+str(i),len(forms)==2)
        sym_eq=matrix(QQ,256,len(forms),[[(F-F.transpose()).list()[k] for F in forms] for k in range(256)])
        weights=sym_eq.right_kernel().basis();ck('symmetric_space_dim1_'+str(i),len(weights)==1)
        H=sum((w*F for w,F in zip(weights[0],forms)),matrix(QQ,16,16));H/=H[0,0]
        ck('symmetric_'+str(i),H==H.transpose());ck('all_three_symmetrized_'+str(i),all(H*A==A.transpose()*H for A in a))
        piv=ldlt_pivots(H);ck('positive_exact_LDL_'+str(i),len(piv)==16)
        roots=H.charpoly().roots(QQ)
        if i==0:ck('base_exact_spectrum',sum(m for _,m in roots)==16 and all(l>0 for l,_ in roots))
        central=intertwiner_basis(a,a);J=next(J for J in central if J*J==-identity_matrix(QQ,16))
        ck('complex_structure_H_skew_'+str(i),J.transpose()*H==-H*J)
        ck('euclidean_shortcut_fails_'+str(i),any(A!=A.transpose() for A in a))
        blocks.append({'matrices':[entries(A) for A in a],'H':entries(H),'J':entries(J),'ldlt_pivots':list(map(str,piv)),'rational_eigenvalues':[[str(l),int(m)] for l,m in roots],'characteristic_polynomial':str(H.charpoly())})
    base=types[0];H=matrix(QQ,16,16,{(i,j):QQ(v) for i,j,v in blocks[0]['H']['entries']});A=base[0];I=identity_matrix(QQ,16)
    eigs=[QQ(-1),QQ(-1)/24,QQ(1)/24,QQ(1)];projectors=[]
    for l in eigs:
        E=I
        for m in eigs:
            if m!=l:E=E*(A-m*I)/(l-m)
        ck('projector_'+str(l),E*E==E and H*E==E.transpose()*H);projectors.append(E)
    ck('projector_complete',sum(projectors)==I)
    ck('flux_inertia_8_8',sum(E.rank() for l,E in zip(eigs,projectors) if l>0)==8 and sum(E.rank() for l,E in zip(eigs,projectors) if l<0)==8)
    bad=matrix(H);bad[0,0]+=1;ck('planted_energy_fault_rejected',any(bad*A!=A.transpose()*bad for A in base))
    return {'result_id':'K1832','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'common_positive_symmetrizer':True,'real_module_dimension':16,'copies':32,'all_positive_forms':'positive Hermitian 32 by 32 matrices after fixed complex module identifications','real_parameter_dimension':1024,'maximal_speed':1,'constant_coefficient_energy_estimate':True,'nonzero_nilpotent_dissipative_zero_order_possible':False,'physical_pairing_selected':False,'source_or_canon_promotion':False},'component_types':kinds,'blocks':blocks,'checks':checks,'reused_fixture_checks':oldchecks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1824-k77-joint-observed-symbol-algebra.json','tests/channel-swings/k1824_k77_joint_observed_symbol_algebra.py','lab/process/k1830-k77-paired-action-nilpotent-completion.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1832',len(v['checks']),'new checks;',len(v['reused_fixture_checks']),'reused fixture checks')
