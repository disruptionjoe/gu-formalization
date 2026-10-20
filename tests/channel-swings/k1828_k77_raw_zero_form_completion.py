#!/usr/bin/env sage-python
"""Exact raw-column versus evolution compatibility on the frozen K77 fixture."""
import hashlib,json
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, zero_matrix, block_matrix, block_diagonal_matrix
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1828-k77-raw-zero-form-completion.json'
def produce():
    checks={}
    def check(k,v):
        checks[k]=bool(v)
        assert v,k
    i=identity_matrix(QQ,2,sparse=True);x=matrix(QQ,[[0,1],[1,0]],sparse=True);z=matrix(QQ,[[1,0],[0,-1]],sparse=True);e=matrix(QQ,[[0,1],[-1,0]],sparse=True)
    def tensor(fs):
        a=matrix(QQ,[[1]],sparse=True)
        for f in fs:a=a.tensor_product(f)
        return a
    gs=[tensor([z]*j+[v]+[i]*(6-j)) for v in [x,e] for j in range(7)]
    eta=[1]*7+[-1]*7;I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);omega=I
    for g in gs:omega=omega*g
    pp=(I+omega)/2;pm=(I-omega)/2;W=pp+2*pm;Wi=pp+pm/2;S=11*pp/24+11*pm/12;Si=24*pp/11+12*pm/11
    blk=lambda rows:block_matrix(QQ,rows,sparse=True)
    D=blk([[eta[r]*gs[r]*gs[0]*gs[c]*W if r!=0 and c not in (r,0) else Z for c in range(14)]+[I if r==0 else Z] for r in range(14)]+[[-I]+[Z]*13+[gs[0]*S]])
    inv=[[Z]*15 for _ in range(15)];inv[0][0]=gs[0]*S;inv[0][14]=-I;inv[14][0]=I
    for r in range(1,14):
        for c in range(1,14):inv[r][c]=Wi*eta[r]*gs[r]*gs[0]*gs[c]*(QQ(1)/12-(1 if r==c else 0))
    Di=blk(inv);check('full_time_inverse',D*Di==identity_matrix(QQ,1920,sparse=True)==Di*D)
    obs=(0,7,8,9);hidden=[r for r in range(14) if r not in obs]
    O=blk([[I if r==s else Z for r in range(15)] for s in obs+(14,)])
    L=blk([[I if s==r else Z for s in obs+(14,)] if r in obs+(14,) else [-eta[r]*gs[r]*gs[s]/20 for s in obs]+[Z] for r in range(15)])
    G=blk([[eta[s]*gs[s] for s in obs]]);J=blk([[gs[s]/4] for s in obs]);P=block_diagonal_matrix([identity_matrix(QQ,512,sparse=True)-J*G,I],sparse=True)
    E0=blk([[I if r==0 else Z] for r in range(15)]);En=blk([[I if r==14 else Z] for r in range(15)])
    check('actual_graph_left_inverse',O*L==identity_matrix(QQ,640,sparse=True));check('corrected_projector',P*P==P and P.trace()==512);check('zero_form_in_corrected_graph',L*P*O*En==En)
    T=gs[0]*S;Ti=Si*gs[0];check('raw_return_inverse',T*Ti==I==Ti*T)
    raw=Di*En;check('raw_southeast_normalizes_to_negative_time_slot',raw==-E0);defect=raw-L*O*raw
    check('all_hidden_defect_blocks',all(defect[128*r:128*(r+1),:]==-eta[r]*gs[r]*gs[0]/20 for r in hidden))
    check('corrected_trace_defect',G*(O*raw)[:512,:]==-gs[0]);check('universal_defect_injectivity',defect[128:256,:].rank()==128)
    matrices={'identity':I,'rank_one':matrix(QQ,128,128,{(0,0):1},sparse=True),'nilpotent':matrix(QQ,128,128,{(0,1):1},sparse=True),'rank_64':pp,'zero':Z,'gamma':gs[7]};ranks={}
    for name,B in matrices.items():
        N=Ti*B;R=E0*N+En*B;C=Di*R;rank=int(B.rank());ranks[name]=rank
        check(name+'_repair_exact',C==En*N);check(name+'_graph_preserved',C==L*O*C);check(name+'_corrected_preserved',P*O*C==O*C)
        check(name+'_unrepaired_leak_rank',(defect*B)[128:256,:].rank()==rank);check(name+'_repair_rank',C.rank()==rank)
        if rank:check(name+'_wrong_sign_rejected',Di*(-E0*N+En*B)!=L*O*Di*(-E0*N+En*B))
    F=(D*L*P)[1792:1920,:];check('return_surjective',F*O*En*Ti==I);check('affine_kernel_dimension',P.trace()-128==384)
    psi=(identity_matrix(QQ,512,sparse=True)-J*G)[:,:128]
    U=blk([[psi[:128,:]],[psi[128:256,:]],[psi[256:384,:]],[psi[384:512,:]],[Ti*psi[:128,:]]])
    check('homogeneous_corrected',P*U==U);check('homogeneous_raw_southeast_zero',(D*L*U)[1792:1920,:]==Z);check('homogeneous_nonzero',bool(U))
    return {'result_id':'K1828','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'raw_southeast_only_preserves_graph_iff':'B=0','leakage_rank':'rank(B)','minimal_two_cell_repair':'N=S^-1 gamma0 B','corrected_one_column_dimension':512*128,'fixed_southeast_affine_dimension':384*128,'raw_source_action_selected':False,'physical_or_canon_promotion':False},'checks':checks,'test_ranks':ranks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1822-k77-rational-corrected-carrier.json','lab/process/k1826-k77-graph-preserving-internal-coefficients.json']}}
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();data=produce()
    if args.write:OUT.write_text(json.dumps(data,indent=2)+'\n')
    else:assert data==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K1828',len(data['checks']),'exact checks')
