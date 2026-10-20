#!/usr/bin/env sage-python
"""K1830 exact conditional paired reduction; no physical action selection."""
import hashlib,json,argparse
from pathlib import Path
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1830-k77-paired-action-nilpotent-completion.json'
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
    eta=[1]*7+[-1]*7;I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);om=I
    for g in gs:om=om*g
    pp=(I+om)/2;pm=(I-om)/2;W=pp+2*pm;S=11*pp/24+11*pm/12;T=gs[0]*S;Ti=(24*pp/11+12*pm/11)*gs[0]
    blk=lambda a:block_matrix(QQ,a,sparse=True)
    D=blk([[eta[r]*gs[r]*gs[0]*gs[c]*W if r!=0 and c not in (r,0) else Z for c in range(14)]+[I if r==0 else Z] for r in range(14)]+[[-I]+[Z]*13+[T]])
    obs=(0,7,8,9);O=blk([[I if r==s else Z for r in range(15)] for s in obs+(14,)])
    L=blk([[I if s==r else Z for s in obs+(14,)] if r in obs+(14,) else [-eta[r]*gs[r]*gs[s]/20 for s in obs]+[Z] for r in range(15)])
    G=blk([[eta[s]*gs[s] for s in obs]]);J=blk([[gs[s]/4] for s in obs]);P=block_diagonal_matrix([identity_matrix(QQ,512,sparse=True)-J*G,I],sparse=True)
    Q=blk([[Z]*14+[I]]);Qo=blk([[Z]*4+[I]]);R=L*P*O
    check('left_inverse',O*L==identity_matrix(QQ,640,sparse=True));check('projector_rank',P*P==P and P.trace()==512)
    check('ambient_retract',R*R==R and R.trace()==512);check('input_survives_retract',Q*R==Q)
    F=(D*L)[1792:1920,:];check('raw_return_on_corrected',(F-blk([[-I,Z,Z,Z,T]]))*P==0)
    cases={'zero':Z,'identity':I,'rank_one':matrix(QQ,128,128,{(0,0):1},sparse=True),'nonsymmetric':matrix(QQ,128,128,{(0,1):1},sparse=True),'chirality_half':pp,'gamma':gs[7]}
    ranks={}
    for name,B in cases.items():
        # psi0=-B, psi7=I, psi8=gamma8 gamma0 B + gamma8 gamma7, psi9=nu=0.
        U=blk([[-B],[I],[gs[8]*gs[0]*B+gs[8]*gs[7]],[Z],[Z]])
        C=L*U*Q;K=D*C
        check(name+'_corrected',P*U==U);check(name+'_square_zero_column',Qo*U==Z)
        check(name+'_left_right_retract',R*C==C==C*R)
        check(name+'_raw_southeast',K[1792:1920,1792:1920]==B)
        check(name+'_nilpotent',C*C==zero_matrix(QQ,1920,1920,sparse=True))
        check(name+'_rank128',U.rank()==128 and (U*Qo).rank()==128)
        check(name+'_dual_invariance',C.transpose()*R.transpose()==C.transpose()==R.transpose()*C.transpose())
        ranks[name]={'rank':128,'homology_on_E512':256,'doubled_homology':512}
    # General completed column includes non-nilpotent and nonsymmetric operators.
    N=matrix(QQ,128,128,{(0,1):1},sparse=True);U=blk([[Z],[Z],[Z],[Z],[N]])
    C=L*U*Q;check('nonsymmetric_allowed',C!=C.transpose());check('nonsymmetric_reduced',R*C*R==C)
    Uid=blk([[Z],[Z],[Z],[Z],[I]]);Cid=L*Uid*Q
    check('generic_completion_not_complex',Cid*Cid==Cid and Cid!=0)
    check('minimal_invertible_SE_not_nilpotent',(Ti*I)**2!=Z)
    # Reference primal/dual Hessian and differential distinction on a small exact block.
    A=matrix(QQ,[[0,1],[0,0]]);z2=zero_matrix(QQ,2);i2=identity_matrix(QQ,2)
    H=block_matrix([[z2,A.transpose()],[A,z2]]);d=block_diagonal_matrix([A,-A.transpose()]);pair=block_matrix([[z2,i2],[i2,z2]])
    check('bilinear_hessian_symmetric',H==H.transpose());check('hessian_not_differential',H*H!=0 and d*d==0)
    check('dual_differential_skew',d.transpose()*pair+pair*d==0)
    return {'result_id':'K1830','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'all_completed_columns_reduce_paired_action':True,'fixed_SE_all_B_rank128_square_zero_completion':True,'homology_dimension':256,'paired_homology_signature':[256,256],'source_action_selected':False,'Hessian_identified_with_differential':False,'physical_or_canon_promotion':False},'cases':ranks,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1822-k77-rational-corrected-carrier.json','lab/process/k1828-k77-raw-zero-form-completion.json']}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K1830',len(v['checks']),'exact checks')
